# 四表交叉（必须）

席位接口要 **`ticker` + 交易日**。当日可能无数据，回退到有数据的开市日（T+1）。

| 表 | 工具 | 作用 |
| --- | --- | --- |
| 1 龙虎 | `seat_get_long_short_board` | 多/空/净多谁在榜 |
| 2 会员 | `seat_get_member_ranks` | `rank_type=all`（或 long/short/net） |
| 3 机构增减仓 | `seat_get_broker_position_chg` | 同日 `increase` 与 `decrease` 各一次 |
| 4 合约增减仓 | `seat_get_contract_position_chg` | 同日增/减（截面排行，用于对照当日资金偏好） |

可选第五表：`seat_get_profit_loss`（当日盈亏分布）。

## 交叉读法（公开、可复述）

1. 龙虎多头席位是否同时出现在会员净多前列。  
2. 机构增仓榜与龙虎方向是否一致。  
3. 合约增减仓排行是否显示该合约处于资金关注区（描述性，不作信号）。  
4. 任何一对表冲突 → 写入 `tensions`，不要合成「主力一致看多」。

禁止把席位解读成内部「拥挤度打分」。
