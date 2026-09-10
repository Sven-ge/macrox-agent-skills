# 公开代理指标规则

本 Skill **不**使用内部吨钢利润、TC/RC、裂解公式库。只允许用 MCP 已返回的价格/结构序列做代理。

## 允许的代理

| 代理 | 工具 | 怎么写 |
| --- | --- | --- |
| 近端涨跌 | `mkt_list_overview` | 写 `last` / `chg_pct` + 时点 |
| 近远月 | `struct_get_term` | 用返回曲线描述 contango / backwardation 或近月相对远月强弱；**不要**自己发明未出现在 `data` 里的价差点数 |
| 基差松紧 | `struct_get_basis` | 序列方向 + 与价格是否同向 |
| 库存节奏 | `struct_get_warehouse` | 窗口内仓单升/降（如 5 日 vs 20 日，以返回点为准） |
| 跨品种相对 | 两个品种都成功取到 overview | 只对比涨跌幅或价位描述；禁止输出「吨利润 = A−B×系数」除非系数来自用户给定且两边价格都有 |
| 比价引擎（可选附录） | `anl_run_rv` | 必须标注工具；`window_years` 建议 2–3；不得改写成「本 Skill 自有利润模型」 |

## 禁止

- 用记忆中的历史利润、盘面口播数字。  
- 股票估值、ROE、公司成本曲线。  
- 一边腿未取到却写裂解/利润结论。

## 政策冲击

只用 `news_search` / `news_list_intel` / `research_list_reports` / `report_*` 窗口内材料。  
每条冲击：日期 + 标题级事实 + 可能作用的 **环节**（不是目标价）。
