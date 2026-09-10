"""MacroX MCP Streamable HTTP 客户端（Python 3，无第三方依赖）。"""

from __future__ import annotations

import json
import math
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

CONFIG = json.loads((Path(__file__).resolve().parent / "mcp_config.json").read_text(encoding="utf-8"))
MCP_URL = str(CONFIG.get("mcp_url", "")).strip()
API_TOKEN = str(CONFIG.get("api_token", "")).strip()
BLOCKED_KEYS = {"__proto__", "prototype", "constructor"}
_req_id = 0
_tool_names: set[str] | None = None


def _next_id() -> int:
    global _req_id
    _req_id += 1
    return _req_id


def _resolved_url() -> str:
    """生产网关鉴权为 URL ?token=（Authorization Bearer 不可用）。"""
    url = MCP_URL
    if not url:
        return url
    if API_TOKEN and "token=" not in url:
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}token={quote(API_TOKEN, safe='')}"
    return url


def _ssl_context() -> ssl.SSLContext | None:
    parsed = urlparse(_resolved_url() or MCP_URL)
    if parsed.scheme != "https":
        return None
    ctx = ssl.create_default_context()
    return ctx


def _headers() -> dict[str, str]:
    return {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }


def _set_path(root: dict[str, Any], dotted: str, value: Any) -> None:
    parts = [p for p in dotted.split(".") if p]
    if not parts:
        return
    cur: dict[str, Any] = root
    for p in parts[:-1]:
        nxt = cur.get(p)
        if not isinstance(nxt, dict):
            nxt = {}
            cur[p] = nxt
        cur = nxt
    cur[parts[-1]] = value


def _normalize_business(obj: dict[str, Any]) -> dict[str, Any]:
    """把生产网关打平键 data.xxx / error.xxx 归一成嵌套 data / error。"""
    if any(str(k).startswith(("data.", "error.")) for k in obj):
        out: dict[str, Any] = {
            k: v for k, v in obj.items() if not str(k).startswith(("data.", "error."))
        }
        data: dict[str, Any] = {}
        error: dict[str, Any] = {}
        for k, v in obj.items():
            sk = str(k)
            if sk.startswith("data."):
                _set_path(data, sk[5:], v)
            elif sk.startswith("error."):
                error[sk[6:]] = v
        if data:
            out["data"] = data
        if error:
            out["error"] = error
            out.setdefault("ok", False)
        return out
    return obj


def _validate_params(params: Any) -> None:
    if not isinstance(params, dict):
        raise TypeError("params must be a JSON object")

    def walk(value: Any) -> None:
        if value is None:
            return
        if isinstance(value, list):
            for item in value:
                walk(item)
            return
        if isinstance(value, dict):
            for key, item in value.items():
                if key in BLOCKED_KEYS:
                    raise TypeError("params contains blocked field")
                walk(item)
            return
        if isinstance(value, float) and not math.isfinite(value):
            raise TypeError("params contains invalid number")
        if not isinstance(value, (str, int, float, bool)):
            raise TypeError("params contains unsupported value type")

    walk(params)
    json.dumps(params, allow_nan=False)


def _post(payload: dict[str, Any], timeout: int = 60) -> tuple[int, Any]:
    url = _resolved_url()
    if not url:
        raise ValueError("mcp_config.json 缺少 mcp_url")

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST", headers=_headers())
    ctx = _ssl_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace").strip()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = body
        return exc.code, parsed

    if not raw:
        return 204, None
    if raw.startswith("data:"):
        raw = raw.split("\n", 1)[0][5:].strip()
    try:
        return 200, json.loads(raw)
    except json.JSONDecodeError:
        return 200, raw


def _unwrap_tool_result(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {"ok": False, "error": {"code": "INVALID_RESPONSE", "message": str(payload)}}

    if "error" in payload and "result" not in payload:
        return {"ok": False, "rpc_error": payload["error"], "raw": payload}

    result = payload.get("result") or {}
    content = result.get("content") or []
    if content and isinstance(content[0], dict):
        text = content[0].get("text")
        if isinstance(text, str):
            try:
                inner = json.loads(text)
                if isinstance(inner, dict):
                    return _normalize_business(inner)
            except json.JSONDecodeError:
                return {"ok": True, "answer": text}
    return {"ok": True, "raw": payload}


def list_tools(refresh: bool = False) -> dict[str, Any]:
    """获取当前 MCP 可用工具列表。"""
    global _tool_names
    if refresh:
        _tool_names = None

    status, data = _post(
        {"jsonrpc": "2.0", "id": _next_id(), "method": "tools/list", "params": {}},
        timeout=30,
    )
    if status < 200 or status >= 300:
        return {
            "ok": False,
            "status_code": status,
            "error": {"code": "HTTP_ERROR", "message": f"MCP HTTP {status}"},
            "raw": data,
        }
    if isinstance(data, dict) and "error" in data:
        return {"ok": False, "status_code": status, "error": data["error"], "raw": data}

    tools = (data or {}).get("result", {}).get("tools", [])
    _tool_names = {
        t.get("name")
        for t in tools
        if isinstance(t, dict) and isinstance(t.get("name"), str) and t.get("name")
    }
    return {"ok": True, "status_code": status, "tools": sorted(_tool_names), "raw": data}


def _ensure_tool(tool_name: str) -> None:
    global _tool_names
    if _tool_names is None:
        listed = list_tools()
        if not listed.get("ok"):
            err = listed.get("error") or {}
            raise ValueError(err.get("message") or f"listTools failed HTTP {listed.get('status_code')}")
    if _tool_names is None or tool_name not in _tool_names:
        raise ValueError(f"tool not available: {tool_name}")


def call(tool_name: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """调用 MacroX MCP 工具。返回解包后的 ok/data/answer/error。"""
    params = params or {}
    _validate_params(params)
    _ensure_tool(tool_name)

    status, data = _post(
        {
            "jsonrpc": "2.0",
            "id": _next_id(),
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": params},
        },
        timeout=120,
    )
    if status < 200 or status >= 300:
        return {
            "ok": False,
            "status_code": status,
            "error": {"code": "HTTP_ERROR", "message": f"MCP HTTP {status}"},
            "raw": data,
        }
    if isinstance(data, dict) and "error" in data:
        return {"ok": False, "status_code": status, "error": data["error"], "raw": data}

    parsed = _unwrap_tool_result(data)
    parsed["status_code"] = status
    return parsed


if __name__ == "__main__":
    print("请通过 call(tool_name, params) 发起请求，见 SKILL.md")
