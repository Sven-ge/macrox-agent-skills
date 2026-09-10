# 工作流 · macrox-report-studio

先过 `data-access.md`。全程禁止 `report_get_paper` 成品入正文。

## Phase 0：定刊

| 用户说法 | `report_kind` |
| --- | --- |
| 早报 / 盘前 / 今天早报 / 未说类型 | `morning` |
| 晚报 / 盘后 / 收盘点评 | `evening` |

日期：用户指定则用；否则 `cal_list_days` 取最近开市日。非交易日：用上一开市日并在页眉注明。

## Phase 1：并行取数

最小集（必须并行，失败单项标未取到）：

**早报**

| 原料 | 工具 |
| --- | --- |
| 交易日 | `cal_list_days` |
| 涨跌截面 | `mkt_list_overview` `mode=movers` `sort_by=change_pct` `limit=80` |
| 隔夜快讯 | `news_list_intel` `time_range=session` `page_size=12` |
| 热榜 | `news_list_hot` `limit=10` |
| 异动 | `watch_get_ranks` `trade_date={as_of}` `page_size=20` |

可选：`struct_get_basis view=market_snapshot`（写驱动/风险时）；对领涨领跌 2–4 个品种 `factor_get_sentiment`。

**晚报**（在早报最小集上把快讯改为 `time_range=today`，并加）

| 原料 | 工具 |
| --- | --- |
| 基差截面 | `struct_get_basis` `view=market_snapshot` |
| 期限概览 | `struct_get_term` `view=market_overview` `page_size=20`（可失败） |
| 合约增减仓 | `seat_get_contract_position_chg` `trade_date={as_of}` |
| 龙虎/会员 | 仅对 2–3 个已解析 `ticker`：`seat_get_long_short_board` / `seat_get_member_ranks` |

品种中文名 → `ref_list_symbols`。席位无 ticker 不猜合约月。

**停检**：`movers` 与快讯（intel 或 hot）至少成功一项，否则停止，不编盘面。

## Phase 2：写稿（先填中间对象）

按 `sections.md` 逐栏写。Hero 必须覆盖盘面/驱动/关注/风险。  
榜单驱动列、关注标签、席位解读：没有对应 `data` 就留空或「未取到」。

禁止边取数边出最终 HTML。

## Phase 3：schema → QA → HTML

填 `output-schema.md`，过 `qa-checklist.md`，再按 `html-template.md` 渲染单文件。

## 交付话术

```text
已生成期货{早报|晚报} · {as_of}：
- 定调：…
- 文件：macrox-report-{morning|evening}-{as_of}.html
数据不足项：…
（此为 MCP 原料生成稿，不是终端已发布刊物的转排。）
```
