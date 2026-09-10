---
name: macrox-commodity-deep-dive
description: >-
  MacroX 品种深度研报工作流：对单一期货品种按 light/medium/heavy 分档，强制假设→代理指标→交叉验证→QA，
  输出多章节 HTML。anl_run_* 只作分析引擎章节，不改服务端算法。
  触发：「深度研报」「深度分析」「light/medium/heavy」「交叉验证」「品种深度」。
  不适用：一页纸速览（macrox-commodity-tearsheet）、主题简报（macrox-topic-brief）、
  产业链地图（macrox-industry-chain-map）、现价快问。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-commodity-deep-dive · 品种深度研报

对 **单个商品期货品种** 走可复现的研究工作流，不是 Tear Sheet 加长版。

> Tear Sheet 回答「现在怎样」。本 Skill 回答「假设是什么、用什么代理检验、什么能证伪」。

## 前置

必读：`references/data-access.md` → `depth-tiers.md` → `workflow.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## 数据闸门（硬停）

只允许 MacroX。禁止宿主搜索顶替。A/B 探测见 `data-access.md`；都失败则停止出稿。  
不能挂 MCP 时必须同时安装 `macrox-futures-mcp` 并配置 Token。

## 分流

| 信号 | 动作 |
| --- | --- |
| 深度 / 研报工作流 / 分档 / 交叉验证 | 进入；档位见 `depth-tiers.md` |
| 一页纸 / tearsheet / 投资速览 | `macrox-commodity-tearsheet` |
| 产业链 | `macrox-industry-chain-map` |
| 主题观察 | `macrox-topic-brief` |
| 现价一句 | **退出** |

## 工作流摘要

1. 收参：`symbol` + 档位（不明则问一次：light / medium / heavy）  
2. 提出 **可证伪假设**（light 1 条，medium 2–3，heavy 3）并硬停确认（用户说直接出可跳过）  
3. 按档取数：结构/行情/资讯；heavy 必须交叉验证  
4. `anl_run_quant`（及可选 intel/rv/echo）**仅引擎章节**，标注工具，不改算法、不把黑盒分数写成「本 Skill 结论」  
5. QA 清单过完再渲 HTML  

## 核心原则

- 假设必须能被后续数据打脸。  
- 缺数标「未取到」，降低该假设置信度，禁止用记忆补序列。  
- 不构成投资建议，无目标价。
