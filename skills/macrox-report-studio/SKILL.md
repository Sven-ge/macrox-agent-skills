---
name: macrox-report-studio
description: >-
  MacroX 期货早晚报生成：按终端 futures-report 已定板块，用行情/快讯/盯盘/结构/席位等原始 MCP 数据
  写成可读早报或晚报 HTML。禁止把 report_get_paper 的成品文案当正文粘贴或改写。
  触发：「写一份早报」「今天早报」「生成晚报」「早晚报 HTML」「盘前简报」「盘后晚报」。
  不适用：朗读官方已发布早报（直调 report_get_paper）、主题观察（topic-brief）、
  品种一页纸（tearsheet）、无书面交付的现价快问。
homepage: https://macrox.cn/
version: 0.2.0
author: MacroX
---

# macrox-report-studio · 机构早晚报生成

按 **终端已定板块** 把原始 MCP 数据写成可读早报/晚报。

> 价值在 **板块契约 + 用原料写稿**，不是改官方成品、也不是另开一套栏目。

## 前置

必读：`references/data-access.md` → `sections.md` → `workflow.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md` → `qa-checklist.md`。

## 数据闸门（硬停）

只允许 MacroX 原始工具（`mkt_*` / `news_*` / `watch_*` / `struct_*` / `seat_*` / `factor_*` / `cal_*` / `ref_*`）。A/B 见 `data-access.md`。

**禁止**把 `report_get_paper` / `report_list_papers` 的 `hero*`、`answer`、KPI、榜单、要闻当正文或改写底稿。  
用户要「官方早报原文」→ **退出本 Skill**，直调 `report_get_paper`。

## 分流

| 信号 | 动作 |
| --- | --- |
| 写/生成早报或晚报、盘前/盘后简报、早晚报 HTML | 进入 |
| 朗读/打开/官方终端里的那份早报晚报 | 退出，调 `report_get_paper` |
| 无盘面结构的主题观察 | `macrox-topic-brief` |
| 单品种一页纸 | `macrox-commodity-tearsheet` |
| 研究文章拆章排版 | 总 Skill 读 `news_get_article`，或 `macrox-topic-brief` |

## 工作流摘要

1. 定刊：`morning`（默认盘前/「今天早报」）或 `evening`（盘后/晚报）；日期默认最近交易日  
2. 按 `sections.md` 并行取 **原始** 截面（涨跌榜、快讯、盯盘、早报可选基差；晚报加席位/基差）  
3. 用原料写稿：Hero 一句定调 +【盘面/驱动/关注/风险】，各板块填证据，缺数标「未取到」  
4. 填 schema → QA → 单一 HTML  

无行情截面且无快讯 → 停止，不编造盘面。
