# 早晚报与分析工具

调用前读本文件。分析类（`anl_*`）会拉多年日线，**耗时约 5–30 秒**；先用较小 `window_years`。

---

## `report_list_papers` · 早晚报列表

**用途**：按交易日汇总早报/晚报 ID 与标题。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `start_date` | string | 否 | `""` | `YYYY-MM-DD`；与 end 同时填可附日历标记 |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `page` | int | 否 | `1` | 页码 |
| `page_size` | int | 否 | `20` | 每页条数 |

```python
call("report_list_papers", {"page_size": 10})
call("report_list_papers", {"start_date": "2026-08-01", "end_date": "2026-08-28"})
```

---

## `report_get_paper` · 单份早报/晚报

**用途**：结构化内容 + Markdown 分节报告（优先展示 `answer`）。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `report_type` | string | **是** | — | `morning` \| `evening` |
| `id` | int | 与 trade_date 二选一 | `0` | 列表中的 `morning_id` / `evening_id` |
| `trade_date` | string | 与 id 二选一 | `""` | 按日期取该类型报告 |

**推荐流程**：先 `report_list_papers` → 取 `morning_id`/`evening_id` → 再 `report_get_paper`。

```python
papers = call("report_list_papers", {"page_size": 5})
# 从 data.items[0] 取 morning_id
call("report_get_paper", {"report_type": "morning", "id": 68})
call("report_get_paper", {"report_type": "evening", "trade_date": "2026-08-27"})
```

---

## `anl_run_quant` · 单品种量化深度分析

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码，如 `CU` |
| `window_years` | int | 否 | `5` | 回溯年数；联调建议 2–3 |
| `sections` | string | 否 | `""` | 逗号分隔章节；空=默认三块。常用：`summary`、`risk_management`、`drawdown_rebound`、`calendar_returns` |
| `series_tail` | int | 否 | `60` | 时序保留最近 N 日；`0`=全量 |
| `config` | string | 否 | `""` | 可选 JSON，覆盖均线/VaR 等 |

```python
call("anl_run_quant", {
    "symbol": "CU",
    "sections": "summary,risk_management",
    "window_years": 3,
})
```

---

## `anl_run_intel` · 多品种风险晴雨表

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbols` | string | **是** | — | 逗号分隔，最多约 20 个，如 `CU,RB,AL,I` |
| `window_years` | int | 否 | `3` | 回溯年数 |
| `config` | string | 否 | `""` | 可选 JSON |

```python
call("anl_run_intel", {"symbols": "CU,RB,AL,I", "window_years": 2})
```

---

## `anl_run_rv` · 双品种比价（相对价值）

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol_a` | string | **是** | — | 品种 A，如 `RB` |
| `symbol_b` | string | **是** | — | 品种 B，如 `HC`；不可与 A 相同 |
| `window_years` | int | 否 | `5` | 回溯年数 |
| `config` | string | 否 | `""` | 可选 JSON |

```python
call("anl_run_rv", {"symbol_a": "RB", "symbol_b": "HC", "window_years": 3})
```

---

## `anl_run_echo` · 市场同构（形态相似扫描）

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码 |
| `target_start` | string | **是** | — | 目标区间起点 `YYYY-MM-DD` |
| `target_end` | string | **是** | — | 目标区间终点 `YYYY-MM-DD` |
| `window_years` | int | 否 | `10` | 历史扫描窗口年数 |
| `top_n` | int | 否 | `10` | 各榜返回条数 |

```python
call("anl_run_echo", {
    "symbol": "CU",
    "target_start": "2025-01-01",
    "target_end": "2025-03-31",
    "window_years": 5,
    "top_n": 10,
})
```
