# MCP 工具映射 · macrox-report-studio

只调用 MacroX 同名工具（会话 MCP 或 `macrox-futures-mcp` 脚本）。数字以返回 `data` 为准。

| 板块 | 工具 | 参数惯例 |
| --- | --- | --- |
| 交易日 | `cal_list_days` | 锚定 `as_of` |
| 涨跌榜 / KPI 原料 | `mkt_list_overview` | `mode=movers` `sort_by=change_pct` `limit=80`；必要时再 `sort_by=volume` |
| 隔夜要闻 | `news_list_intel` | 早报：`time_range=session`；晚报时间线：`time_range=today` |
| 热榜 / 关注标签 | `news_list_hot` | `limit=10` |
| 补充检索 | `news_search` | 仅当用户点名事件；keyword 来自已出现快讯，不凭空搜 |
| 异动雷达 | `watch_get_ranks` | `trade_date` + `page_size=20` |
| 品种校验 | `ref_list_symbols` | 中文名/代码 |
| 基差（晚报必做，早报可选） | `struct_get_basis` | `view=market_snapshot` |
| 期限（晚报可选） | `struct_get_term` | `view=market_overview` |
| 席位（仅晚报） | `seat_get_contract_position_chg` | `trade_date`；再对 2–3 个 `ticker` 调 `seat_get_long_short_board` 或 `seat_get_member_ranks` |
| 舆情脚注 | `factor_get_sentiment` | 领涨/领跌品种，`window_days=7` |

## 不要用

| 工具 | 原因 |
| --- | --- |
| `report_get_paper` / `report_list_papers` | 终端已处理成品；本 Skill 用原料写稿 |
| `news_get_article` / `news_list_articles` | 那是研究文章，不是早晚报原料 |
| `anl_run_*` | 耗时长，且不是终端早晚报栏目 |

失败：该栏「未取到」（工具名 + 错误摘要）。禁止换源。
