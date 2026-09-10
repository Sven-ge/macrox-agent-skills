# MCP 工具映射 · macrox-commodity-deep-dive

| 用途 | 工具 | 档位 |
| --- | --- | --- |
| 品种确认 | `ref_list_symbols` / `ref_get_contract` | 全档 |
| 现价 | `mkt_list_overview` | 全档 |
| 阶段 | `mkt_get_daily_bars` | 全档，`window_days` 60–120 |
| 基差/期限/仓单/持仓比 | `struct_get_*` | light 取 2 个结构；medium+ 尽量齐 |
| 舆情 | `factor_get_sentiment` | medium+ |
| 催化剂 | `news_search` / `news_list_intel` | 全档 |
| 席位 | `seat_get_long_short_board` / `seat_get_member_ranks` | heavy，需 `ticker` |
| 引擎 | `anl_run_quant` | medium+；`window_years` 2–3 |
| 可选引擎 | `anl_run_rv` / `anl_run_echo` / `anl_run_intel` | 仅用户意图明确时 |

失败：该节「未取到」。禁止换源。`symbol` 大写；席位用 `ticker`。
