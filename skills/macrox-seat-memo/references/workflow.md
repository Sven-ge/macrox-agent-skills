# 工作流 · macrox-seat-memo

## 步骤 1：收参

`ticker` 小写合约（如 `cu2610`）。`trade_date` 缺省则 `cal_list_days` 取 ≤今天 的开市日并按 T+1 理解。

## 步骤 2：四表

按 `four-tables.md` 取数。某表失败：该表「未取到」，**不得**用其他合约或网页席位顶替。四表全失败 → 停止出稿，说明日期/合约无数据。

## 步骤 3：假设 + 证伪

每条假设：`if 观察成立 then 未来可检验的公开条件`。  
证伪清单 ≥ 假设条数。待观察项写清下次看哪张表、哪个交易日。

## 步骤 4：结构对照

`mkt_list_overview`（品种码从 ticker 提取，如 cu2610→CU）+ `struct_get_basis` 或 `struct_get_position_ratio`。  
席位叙事与结构相反必须写明。

## 步骤 5：schema → HTML
