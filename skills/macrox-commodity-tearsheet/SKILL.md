---
name: macrox-commodity-tearsheet
description: >-
  MacroX 品种投资速览（Tear Sheet）：对单一期货品种输出固定维度的机构级一页纸/短报告（建议 HTML）。
  含意图澄清、六维分析框架、MCP 取数编排、output schema 与版式契约。
  触发：「品种速览」「一页纸」「tearsheet」「投资速览」+ 品种名/代码（铜/CU/沪铜等）；
  「帮我系统看看XX品种」且用户确认要书面速览时。
  不适用：现价一句问、单次龙虎榜口述、主题观察简报（用 macrox-topic-brief）、
  个股财报/DCF（非本仓）、需要专有模型分数且不愿公开规则时（属第二类，应落工具）。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-commodity-tearsheet · 品种投资速览

对 **单个商品期货品种** 生成机构风格的 **Tear Sheet**（短报告），不是聊天摘要。

> 没有本 Skill 时，模型容易只调 `mkt_list_overview` 写一段话。  
> 本 Skill 强制：**六维框架 + 中间 brief + HTML 契约**。

## 前置

1. MacroX MCP 已挂载（优先）或 `macrox-futures-mcp` 脚本可用。  
2. 必读顺序：`references/workflow.md` → `six-dimension.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## Phase 0：路由

### 语言

用户中文 → 全程中文交付。

### 意图

| 档 | 信号 | 动作 |
| --- | --- | --- |
| A | 速览 / 一页纸 / tearsheet / 投资速览 | 直接进入工作流 |
| B | 「看看铜 / 分析一下铁矿」等含糊 | **先问**：1) 品种速览 Tear Sheet 2) 只要口头三点 3) 改做主题简报（topic-brief）。选 2 则 **退出本 Skill** |
| C | 纯现价/涨跌幅 | **退出**，直接调行情工具回答 |

### 品种归一

解析为 `symbol`（大写品种码，如 `CU`）。不确定时用 `ref_list_symbols` 确认，再向用户确认主力关注合约是否需要（席位维可选 `ticker`）。

## 核心原则

1. **禁止抄近路**：六维每一维都要有数据支撑段落；禁止用「整体偏好」一笔带过。  
2. **禁止编造**：工具失败或无数据 → 该维结论标「数据不足」，不得填假数字。  
3. **先 brief 后排版**：必须先完成符合 `output-schema.md` 的分析简报，再渲染 HTML。  
4. **不构成投资建议**：文案与页脚必须免责；不做目标价/下单指令。  
5. **专有模型**：可用 `anl_run_quant` 等作为「附录引用」，不得把黑盒分数改写成「本 Skill 自有结论」而不标注工具。

## 交付物

1. 中间件：`{symbol}_tearsheet_brief.md`（或等价结构化内容）  
2. 终稿：`macrox-tearsheet-{symbol}-{date}.html`  
3. 向用户给路径 + 六维各一句结论摘要  
