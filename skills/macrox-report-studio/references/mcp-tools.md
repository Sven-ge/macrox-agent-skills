# MCP 工具映射 · macrox-report-studio

| 用途 | 工具 |
| --- | --- |
| 早晚报列表 | `report_list_papers`（`start_date`/`end_date`/`page`） |
| 早晚报正文 | `report_get_paper`（`report_type` + `id` 或 `trade_date`） |
| 文章列表 | `news_list_articles` |
| 文章正文 | `news_get_article` |
| 品种校验 | `ref_list_symbols` |
| 现况脚注 | `mkt_list_overview` |
| 结构脚注（可选） | `struct_get_basis` / `struct_get_warehouse` |

失败：脚注「未取到」。禁止用外部研报网站补全文。
