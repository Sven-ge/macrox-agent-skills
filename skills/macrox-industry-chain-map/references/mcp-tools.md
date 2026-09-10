# MCP 工具映射 · macrox-industry-chain-map

只调用 MacroX 同名工具（见 `data-access.md`）。

| 用途 | 工具 | 参数要点 |
| --- | --- | --- |
| 校验品种码 | `ref_list_symbols` | `query` |
| 现价 KPI | `mkt_list_overview` | `symbols` 逗号大写，一次尽量带齐本链节点 |
| 日线节奏（可选） | `mkt_get_daily_bars` | 关键 1–2 个节点，`window_days` 60 |
| 基差 | `struct_get_basis` | 关键节点 `time_series`；或 `market_snapshot` 做截面 |
| 期限 | `struct_get_term` | `single_symbol_curve` |
| 仓单 | `struct_get_warehouse` | `window_days` 20–40 |
| 政策/冲击 | `news_search` / `news_list_intel` | 查询带链名与日期 |
| 机构观点 | `research_list_reports` | 关键词 + limit |
| 附录比价 | `anl_run_rv` | 仅 1 对核心价差，小窗口 |

## 纪律

1. 先 `overview` 再结构；结构按 **关键节点** 取，不要对目录里每个品种打满四件套。  
2. 失败：该单元格「未取到」+ 工具名。禁止换源。  
3. `symbol` 大写。
