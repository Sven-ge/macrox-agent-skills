---
name: macrox-report-studio
description: >-
  MacroX 早晚报/研报再生产：选定一份 MacroX 早报、晚报或研究文章，拆章、建品种索引，
  用实时行情/结构做脚注核对后输出派生 HTML。价值在版式与 QA，不重写投研结论。
  触发：「早晚报转 HTML」「研报再生产」「拆章排版」「报告脚注核对」。
  不适用：从零写主题简报（topic-brief）、无原文的深度研报（deep-dive）、快问现价。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-report-studio · 机构刊物派生

把 **已有 MacroX 刊物** 做成可浏览的派生 HTML，并核对近端数据是否已过时。

> 价值在 **版式契约 + QA**，不是重新发明正文。

## 前置

必读：`references/data-access.md` → `qa-checklist.md` → `workflow.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## 数据闸门（硬停）

原文必须来自 MacroX：`report_get_paper` / `news_get_article` / 用户粘贴且声明来源为 MacroX 导出。  
禁止用宿主搜索找研报正文顶替。A/B 见 `data-access.md`。

## 分流

| 信号 | 动作 |
| --- | --- |
| 早晚报/研报再生产、拆章、脚注核对 | 进入 |
| 无指定刊物的主题观察 | `macrox-topic-brief` |
| 自写品种深度 | `macrox-commodity-deep-dive` |

## 工作流摘要

1. 选刊：`report_list_papers` 或 `news_list_articles` → 取 id → 拉详情  
2. 拆章：按原文小标题切块，保留原意  
3. 品种索引：从正文提取 `symbol`，`ref_list_symbols` 校验  
4. 实时脚注：对各索引品种 `mkt_list_overview`（必要再 basis）对照报告日  
5. QA：过时数字打标「稿内 vs 现况」，**不擅自改原文结论句**  
6. 派生 HTML  

无可用原文 → 停止，请用户指定日期/类型或文章 id。
