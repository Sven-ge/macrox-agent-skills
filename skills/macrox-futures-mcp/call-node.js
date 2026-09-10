const fs = require('fs');
const path = require('path');
const https = require('https');
const http = require('http');

const CONFIG = JSON.parse(fs.readFileSync(path.join(__dirname, 'mcp_config.json'), 'utf-8'));
const MCP_URL = String(CONFIG.mcp_url || '').trim();
const API_TOKEN = String(CONFIG.api_token || '').trim();
const BLOCKED_KEYS = new Set(['__proto__', 'prototype', 'constructor']);

let reqId = 0;
let toolNames = null;

function nextId() {
    reqId += 1;
    return reqId;
}

function resolvedUrl() {
    // 生产网关鉴权为 URL ?token=（Authorization Bearer 不可用）
    let url = MCP_URL;
    if (!url) return url;
    if (API_TOKEN && !url.includes('token=')) {
        url += (url.includes('?') ? '&' : '?') + `token=${encodeURIComponent(API_TOKEN)}`;
    }
    return url;
}

function headers() {
    return {
        'Content-Type': 'application/json',
        Accept: 'application/json, text/event-stream',
    };
}

function validateParams(params) {
    if (params === null || typeof params !== 'object' || Array.isArray(params)) {
        throw new TypeError('params must be a JSON object');
    }
    function walk(value) {
        if (value === null) return;
        if (Array.isArray(value)) {
            for (const item of value) walk(item);
            return;
        }
        if (typeof value === 'object') {
            for (const key of Object.keys(value)) {
                if (BLOCKED_KEYS.has(key)) {
                    throw new TypeError('params contains blocked field');
                }
                walk(value[key]);
            }
            return;
        }
        if (typeof value === 'number' && !Number.isFinite(value)) {
            throw new TypeError('params contains invalid number');
        }
        if (['bigint', 'function', 'symbol', 'undefined'].includes(typeof value)) {
            throw new TypeError('params contains unsupported value type');
        }
    }
    walk(params);
    JSON.stringify(params);
}

function post(payload, timeoutSec = 60) {
    return new Promise((resolve, reject) => {
        const endpoint = resolvedUrl();
        if (!endpoint) {
            reject(new Error('mcp_config.json missing mcp_url'));
            return;
        }
        const url = new URL(endpoint);
        const options = {
            hostname: url.hostname,
            port: url.port || (url.protocol === 'https:' ? 443 : 80),
            path: url.pathname + url.search,
            method: 'POST',
            headers: headers(),
            timeout: timeoutSec * 1000,
            rejectUnauthorized: false,
        };
        const transport = url.protocol === 'https:' ? https : http;
        const req = transport.request(options, (res) => {
            let data = '';
            res.on('data', (chunk) => { data += chunk; });
            res.on('end', () => {
                let parsed = null;
                const trimmed = data.trim();
                if (trimmed) {
                    const line = trimmed.startsWith('data:') ? trimmed.split('\n')[0].slice(5).trim() : trimmed;
                    try {
                        parsed = JSON.parse(line);
                    } catch (e) {
                        parsed = line;
                    }
                }
                resolve({ statusCode: res.statusCode, data: parsed });
            });
        });
        req.on('error', reject);
        req.on('timeout', () => {
            req.destroy();
            reject(new Error(`Request timeout after ${timeoutSec}s`));
        });
        req.write(JSON.stringify(payload));
        req.end();
    });
}

function setPath(root, dotted, value) {
    const parts = String(dotted).split('.').filter(Boolean);
    if (!parts.length) return;
    let cur = root;
    for (let i = 0; i < parts.length - 1; i += 1) {
        const p = parts[i];
        if (!cur[p] || typeof cur[p] !== 'object' || Array.isArray(cur[p])) cur[p] = {};
        cur = cur[p];
    }
    cur[parts[parts.length - 1]] = value;
}

function normalizeBusiness(obj) {
    if (!obj || typeof obj !== 'object' || Array.isArray(obj)) return obj;
    const keys = Object.keys(obj);
    if (!keys.some((k) => k.startsWith('data.') || k.startsWith('error.'))) return obj;
    const out = {};
    const data = {};
    const error = {};
    for (const [k, v] of Object.entries(obj)) {
        if (k.startsWith('data.')) setPath(data, k.slice(5), v);
        else if (k.startsWith('error.')) error[k.slice(6)] = v;
        else out[k] = v;
    }
    if (Object.keys(data).length) out.data = data;
    if (Object.keys(error).length) {
        out.error = error;
        if (out.ok === undefined) out.ok = false;
    }
    return out;
}

function unwrapToolResult(payload) {
    if (!payload || typeof payload !== 'object') {
        return { ok: false, error: { code: 'INVALID_RESPONSE', message: String(payload) } };
    }
    if (payload.error && !payload.result) {
        return { ok: false, rpc_error: payload.error, raw: payload };
    }
    const result = payload.result || {};
    const content = result.content || [];
    if (content.length && content[0] && typeof content[0].text === 'string') {
        try {
            const inner = JSON.parse(content[0].text);
            if (inner && typeof inner === 'object') return normalizeBusiness(inner);
        } catch (e) {
            return { ok: true, answer: content[0].text };
        }
    }
    return { ok: true, raw: payload };
}

async function listTools(refresh = false) {
    if (refresh) toolNames = null;
    const { statusCode, data } = await post(
        { jsonrpc: '2.0', id: nextId(), method: 'tools/list', params: {} },
        30,
    );
    if (statusCode < 200 || statusCode >= 300) {
        return {
            ok: false,
            status_code: statusCode,
            error: { code: 'HTTP_ERROR', message: `MCP HTTP ${statusCode}` },
            raw: data,
        };
    }
    if (data && data.error) {
        return { ok: false, status_code: statusCode, error: data.error, raw: data };
    }
    const tools = (((data || {}).result || {}).tools) || [];
    toolNames = new Set(
        tools.map((t) => t && t.name).filter((name) => typeof name === 'string' && name),
    );
    return { ok: true, status_code: statusCode, tools: [...toolNames].sort(), raw: data };
}

async function ensureTool(toolName) {
    if (!toolNames) {
        const listed = await listTools();
        if (!listed.ok) {
            const msg = (listed.error && listed.error.message) || `listTools failed HTTP ${listed.status_code}`;
            throw new Error(msg);
        }
    }
    if (!toolNames || !toolNames.has(toolName)) {
        throw new Error(`tool not available: ${toolName}`);
    }
}

async function call(toolName, params = {}) {
    validateParams(params);
    await ensureTool(toolName);
    const { statusCode, data } = await post(
        {
            jsonrpc: '2.0',
            id: nextId(),
            method: 'tools/call',
            params: { name: toolName, arguments: params },
        },
        120,
    );
    if (statusCode < 200 || statusCode >= 300) {
        return {
            ok: false,
            status_code: statusCode,
            error: { code: 'HTTP_ERROR', message: `MCP HTTP ${statusCode}` },
            raw: data,
        };
    }
    if (data && data.error) {
        return { ok: false, status_code: statusCode, error: data.error, raw: data };
    }
    const parsed = unwrapToolResult(data);
    parsed.status_code = statusCode;
    return parsed;
}

module.exports = { call, listTools };

if (require.main === module) {
    console.log('请通过 call(toolName, params) 发起请求，见 SKILL.md');
}
