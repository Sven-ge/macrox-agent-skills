---
name: macrox-futures-mcp
description: >-
  MacroX 期货投研工具：品种合约、实时/日/分钟行情、快讯与研究文章、基差与期限结构、仓单与持仓比、
  席位龙虎榜与会员排名、盯盘异动、券商研报、期货早晚报、外盘行情、量化/晴雨表/比价/同构分析。
  用户询问期货行情、沪铜价格、基差、仓单、龙虎榜、快讯、研报、早报晚报、外盘或量化分析时使用。
homepage: https://macrox.cn/
version: 1.4.1
author: MacroX
---

# MacroX 期货投研工具 (macrox-futures-mcp)

- 本技能面向期货投研取数与分析，覆盖行情、资讯、结构、席位、报告与量化能力
- 共 **31** 个结构化工具；入参为字段对象，返回 `ok` / `data` / 可选 `answer`
- 官网：https://macrox.cn/

---

## 使用方法

本 skill 对接 MacroX 期货 MCP，兼容两种落地方式：

1. **仅 Skill（未在客户端/Agent 挂载 MCP）**：用本目录脚本取数  
   - **Node.js**：`call-node.js`（无额外依赖，推荐）  
   - **Python**：`call.py`（标准库即可）  
   - 须配置 `mcp_config.json` 中的 `api_token`（脚本自动拼 `?token=`）
2. **已挂载 MCP + 使用 Skill**：若会话中已提供同名工具（如 `mkt_list_overview`），**优先直接调用 MCP 工具**；Skill 负责场景判断、参数规范与 `/references/` 指引。此时可不依赖脚本与 `mcp_config.json`

跨场景时仍以 `/references/` 为准；先判场景再加载对应文档，避免一次读完全部参考。

---

## 首次使用

- **方式 1（仅 Skill）**：复制 `mcp_config.example.json` 为 `mcp_config.json`，填写运营下发的 `api_token`（`mcp_url` 默认 `https://mcp.macrox.cn/mcp`）；需 Node.js 16+ 或 Python 3.9+
- **方式 2（已挂载 MCP）**：会话内已有 MacroX 工具即可使用本 Skill；脚本配置可选

---

## 数据范围

- **基础**：品种目录、合约规则、交易日历
- **行情**：最新价/涨跌幅榜、日线（可周月重采样）、分钟 K
- **资讯**：快讯、热榜、搜索、原创研究文章、品种舆情评分
- **结构**：现货基差、期限结构、仓单日报、多空持仓比
- **席位**：机构/合约增减仓、盈亏分布、龙虎榜、会员排名
- **报告与分析**：券商研报元数据、期货早晚报、量化深度分析、风险晴雨表、比价、同构
- **外盘**：外盘品种列表、外盘日线
- **盯盘**：异动事件流（突破、新高新低等）

---

## 参考文档加载提示

根据用户问题判断类别，再加载 `/references/` 下对应文档；只加载相关文件。跨类别时再按需加载多个。

| 用户需求类型 | 优先加载 |
| --- | --- |
| 品种、合约、交易日 | `/references/ref_cal.md` |
| 现价、涨跌幅、日/分钟 K | `/references/mkt.md` |
| 快讯、热榜、文章、舆情 | `/references/news.md` |
| 基差、期限、仓单、持仓比 | `/references/struct.md` |
| 增减仓、盈亏、龙虎榜、会员排名 | `/references/seat.md` |
| 早报晚报、量化/晴雨表/比价/同构 | `/references/report_anl.md` |
| 盯盘、研报、外盘 | `/references/watch_research_fx.md` |

---

## 使用技巧

1. **先定工具再填参**：按上表打开参考文档中的参数表，勿凭印象编造字段名
2. **品种与合约**：`symbol` 为大写品种码（如 `CU`）；具体合约用 `ticker`（如 `cu2610`）。席位/龙虎榜/会员排名需 `ticker`
3. **席位时效**：席位类多为 T+1；未传日期时，会员排名会回退到近期有数据的开市日
4. **分析类耗时**：`anl_*` 建议先用较小 `window_years`（如 2–3）
5. **返回解读**：正文可用 `answer` 排版；引用价格、涨跌幅、列表条数等以 `data` 为准。部分网关可能返回打平键（如 `data.items`），解析后按嵌套 `data` 理解即可
6. **工具清单**：不确定当前可用工具时，可对 MCP 执行 `tools/list`，或以脚本 `list_tools` / `listTools` 查看

---

## 场景速查

| 场景 | 工具 | 关键入参 |
| --- | --- | --- |
| 现价 / 涨跌 | `mkt_list_overview` | `symbols` 或 `mode=movers` |
| 日 K | `mkt_get_daily_bars` | `symbol` + `window_days` |
| 分钟 K | `mkt_get_minute_bars` | `ticker` + `interval` |
| 找品种/合约 | `ref_list_symbols` | `query` + `include_contracts` |
| 今日快讯 | `news_list_intel` | `time_range=today` |
| 读文章 | `news_list_articles` → `news_get_article` | `article_id` |
| 基差排名 | `struct_get_basis` | `view=market_snapshot` |
| 仓单 | `struct_get_warehouse` | `symbol` + `window_days` |
| 持仓比 | `struct_get_position_ratio` | `symbol` + `window_days` |
| 龙虎榜 | `seat_get_long_short_board` | `trade_date` + `ticker` |
| 会员排名 | `seat_get_member_ranks` | `ticker` |
| 外盘 | `fx_list_symbols` / `fx_get_daily_bars` | `symbol` |
| 早报 | `report_list_papers` → `report_get_paper` | `report_type=morning` |
| 深度分析 | `anl_run_quant` | `symbol` + `sections` |

---

## 核心函数（脚本方案）

### `call(tool_name, params)`

发起数据请求。

- `tool_name` (str)：工具名，详见 `/references/`
- `params` (dict)：请求参数

```javascript
const { call } = require('./call-node.js');
const result = await call('mkt_list_overview', { symbols: 'CU', limit: 1 });
```

```python
from call import call
result = call('mkt_list_overview', {'symbols': 'CU', 'limit': 1})
```

业务结果一般为：

```json
{ "ok": true, "data": { ... }, "answer": "Markdown 摘要" }
```

`ok=false` 时读取 `error.message`，勿编造数值。

---

## 注意事项

1. `mcp_config.json` 仅脚本方案需要；会话已有 MCP 工具时可直接调用
2. 请求样例默认脚本与 `SKILL.md` 同目录；路径不同时注意引用位置
3. 单次临时取数脚本用完后可清理，避免残留
4. 日期统一 `YYYY-MM-DD`；`rank_type` 支持 `long|short|net|all`（无独立 volume）
