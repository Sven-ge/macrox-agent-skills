---
name: macrox-seat-memo
description: >-
  MacroX 席位资金研究备忘：对指定合约交叉龙虎榜、会员排名、机构/合约增减仓与盈亏分布，
  形成可证伪的主力行为假设、待观察项，并与基差/期限/价格对照。输出备忘录 HTML。
  触发：「席位备忘」「资金研究」「主力假设」「证伪清单」「龙虎交叉」+ 合约。
  不适用：只读一次龙虎榜口述、无合约的快问、品种一页纸（tearsheet）。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-seat-memo · 席位资金研究备忘

这不是「读一下龙虎榜」。交付物是 **假设可证伪** 的投研备忘。

## 前置

必读：`references/data-access.md` → `four-tables.md` → `workflow.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## 数据闸门（硬停）

只允许 MacroX。席位为 T+1，禁止用搜索或记忆补席位数字。A/B 见 `data-access.md`。

## 分流

| 信号 | 动作 |
| --- | --- |
| 席位备忘 / 主力假设 / 证伪清单 / 四表交叉 | 进入 |
| 「今天龙虎谁买了」且不要书面备忘 | **退出**，用总 Skill 单次工具回答 |
| 一页纸 / 深度研报 | tearsheet / deep-dive |

## 工作流摘要

1. 收参：`ticker`（必填）+ `trade_date`（默认上一交易日，用 `cal_list_days`）  
2. 拉齐四表（见 `four-tables.md`），能拉第五表盈亏则拉  
3. 归纳 **1–3 条主力行为假设**（谁、方向、可观察后果）  
4. 写 **证伪清单** 与待观察项  
5. 用 `mkt_list_overview` + 1–2 个 `struct_*` 对照，冲突写入备忘  
6. HTML 备忘录  

无 `ticker`：先 `ref_list_symbols` 解析，仍不确定则问用户，**不要**只拿品种码调龙虎榜。
