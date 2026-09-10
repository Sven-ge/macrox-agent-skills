---
name: macrox-topic-brief
description: >-
  MacroX 主题观察简报：对期货相关主题（品种/板块/政策议题/机构）生成固定结构的 HTML 简报。
  强制时间窗、素材确认闸门、JSON→HTML 契约；数据优先 MacroX MCP（快讯/研报/早晚报 + 行情脚注）。
  触发：「做一份XX观察/简报/digest」「主题简报」「topic brief」、或明确要 HTML 主题刊物。
  不适用：单条新闻评论、无书面交付的快问快答、个股财报深度（非本仓范围）、品种投资速览（用 macrox-commodity-tearsheet）。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-topic-brief · 主题观察简报

为期货投研主题生成 **单一 self-contained HTML** 观察简报（可浏览器打开 / 粘贴公众号）。

> **何时必须用本 Skill**：用户要「观察 / 简报 / digest / 刊物」类书面交付，且需要固定栏目与版式。  
> **何时不要用**：一句快讯问答、单条评论——直接对话回答，或只用 `macrox-futures-mcp`。

## 前置条件

1. 已挂载 MacroX MCP（`macrox-mcp`，URL 含 `?token=`），或本机可调用同名工具。  
2. 会话内 **优先 MCP 工具**；无 MCP 时用 `macrox-futures-mcp` 脚本兜底。  
3. 开工前读：`references/workflow.md` → `references/mcp-tools.md` → `references/output-schema.md` → `references/html-template.md`。

## 闸门（Phase 0）

### 拒答范围（命中即停）

政治选举/政党攻讦、军事冲突细节、宗教教义争议、娱乐八卦。回复一行：`超出本 Skill 范围。` 后停止。

### 意图分流

| 信号 | 动作 |
| --- | --- |
| 观察 / 简报 / digest / 主题刊物 / HTML 简报 | 进入本工作流 |
| 「XX 什么价 / 今日快讯」等快问 | **退出本 Skill**，普通回答 |
| 「品种速览 / 一页纸 / tearsheet」 | 改用 `macrox-commodity-tearsheet` |

## 工作流总览（5 步）

详见 `references/workflow.md`。摘要：

1. **收参**（主题、时间窗、署名；缺则一次问清）  
2. **并行取数**（MCP：快讯/搜索/研报/早晚报 + 必要行情脚注；强制时间过滤）  
3. **方向确认**（硬停：列拟写焦点与栏目，用户确认后再写）  
4. **填 schema**（`references/output-schema.md`，不得跳过必填字段）  
5. **渲 HTML**（按 `html-template.md` 输出单文件；自检清单）

## 核心原则

- 不编造价格、日期、席位数字；缺数写「未取到」并注明工具。  
- 引用结论必须能回溯到某次工具返回的 `data` / 原文标题。  
- 禁止用自由长文代替 schema；禁止跳过步骤 3 硬停（除非用户说「跳过确认直接出稿」）。  
- 本 Skill **不**做专有量化打分；深度量化调用 `anl_*` 仅可作附录脚注，且标注来源工具。
