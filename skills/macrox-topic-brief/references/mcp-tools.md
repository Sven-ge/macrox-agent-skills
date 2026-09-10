# MCP 工具映射 · macrox-topic-brief

会话内优先调用已挂载的 MacroX MCP 同名工具。参数名以工具 schema 为准；下表为常用约定。

| 用途 | 工具 | 常用参数 |
| --- | --- | --- |
| 关键词快讯 | `news_search` | `q`, `limit`；查询串含日期提示 |
| 快讯流 | `news_list_intel` | `time_range`（如 `today`）或日期相关参数；`limit` |
| 热榜 | `news_list_hot` | `limit` |
| 研究文章列表 | `news_list_articles` | `limit` / 关键词 |
| 文章正文 | `news_get_article` | `article_id` |
| 券商研报元数据 | `research_list_reports` | 关键词、时间、`limit` |
| 早晚报列表 | `report_list_papers` | `report_type=morning\|evening`，日期区间 |
| 早晚报详情 | `report_get_paper` | `report_type` + `id` |
| 现价脚注 | `mkt_list_overview` | `symbols`（大写品种码） |
| 基差脚注 | `struct_get_basis` | `symbol` 或市场快照 view |
| 舆情脚注 | `factor_get_sentiment` | `symbol` |

## 调用纪律

1. 先列表/搜索，再按需拉详情（文章、早晚报）。  
2. 同一事实不重复调用超过合理次数；合并展示。  
3. 工具失败：记录错误信息进 schema.`notes`，改用其他源或标注缺失——禁止臆造。  
4. 品种码大写（`CU`）；合约用 `ticker`（如 `cu2610`）仅在确需席位类时（本简报默认不进席位深挖）。
