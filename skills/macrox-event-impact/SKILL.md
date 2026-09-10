---
name: macrox-event-impact
description: >-
  MacroX 事件影响：从快讯/用户给定事件抽取事实，映射到品种影响链路，用事件窗日线与结构对照，
  输出结论卡 + 可公开复述的情景表 HTML。不做内部交易信号。
  触发：「事件影响」「冲击评估」「政策落地影响」「事件窗」「情景表」+ 事件或品种。
  不适用：主题观察刊物（topic-brief）、无事件的品种速览、要买卖点。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-event-impact · 事件驱动影响

把 **一件已发生或正在发生的公开事件** 做成结论卡 + 情景表，不是新闻评论。

## 前置

必读：`references/data-access.md` → `impact-chain.md` → `workflow.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## 数据闸门（硬停）

只允许 MacroX 快讯/研报 + 行情/结构。禁止宿主搜索编事件。A/B 见 `data-access.md`。

## 分流

| 信号 | 动作 |
| --- | --- |
| 事件影响 / 冲击窗 / 情景表 | 进入 |
| 主题刊物 / digest | `macrox-topic-brief` |
| 要开仓点、内部信号 | **停止**：`超出本 Skill 范围。` |

## 工作流摘要

1. 钉事件：用户原文或 `news_search` 标题级事实 + 日期  
2. 按 `impact-chain.md` 映射品种与结构渠道  
3. 用 `cal_list_days` + `mkt_get_daily_bars` 做冲击窗（默认事件日 T−5…T+5 开市日）  
4. 结构脚注：basis / warehouse（相关品种）  
5. 公开情景表：已实现路径 + 2 个后续可观察情景（无目标价）  
6. HTML  

事件无法在 MacroX 资讯中核对且用户未给出可引用事实 → 硬停，请用户补充日期与标题，**不要**用网页新闻补。
