# MCP 工具映射 · macrox-commodity-tearsheet

| 工具 | 用途 |
| --- | --- |
| `ref_list_symbols` | 中文名/模糊名 → `symbol` |
| `ref_get_contract` | 合约规则脚注 |
| `cal_list_days` | 交易日/假期 |
| `mkt_list_overview` | 现价、涨跌幅 |
| `mkt_get_daily_bars` | 阶段与波动 |
| `mkt_get_minute_bars` | 仅当用户强调盘中；默认可跳过 |
| `struct_get_basis` | 基差 |
| `struct_get_term` | 期限结构 |
| `struct_get_warehouse` | 仓单 |
| `struct_get_position_ratio` | 持仓比 |
| `factor_get_sentiment` | 舆情 |
| `news_search` / `news_list_intel` | 催化剂 |
| `seat_get_long_short_board` | 龙虎榜（需 ticker） |
| `seat_get_member_ranks` | 会员排名（需 ticker） |
| `anl_run_quant` | 可选附录（小窗口） |

## 参数纪律

- `symbol`：大写品种码。  
- `ticker`：小写+合约月，如 `cu2610`；不确定不要猜，先问或跳过席位明细。  
- 日线窗口优先 60–120 日；分析类工具避免默认超长窗口。  
- 解析返回时以 `data` 为准；存在 `answer` 可作叙述参考但仍需核对数字。
