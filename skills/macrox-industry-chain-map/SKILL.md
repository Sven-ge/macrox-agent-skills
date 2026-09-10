---
name: macrox-industry-chain-map
description: >-
  MacroX 产业链地图：对有色/黑色/能化等商品链输出环节表、代表品种、价差/利润代理、库存节奏与政策冲击的单一 HTML。
  利润用可公开的基差、近远月、仓单作代理，不做公司财报/ROE。
  触发：「产业链」「产业地图」「上下游」「铜铝钢链」「聚烯烃链」「利润代理」+ HTML/地图交付。
  不适用：单品种一页纸（macrox-commodity-tearsheet）、主题观察简报（macrox-topic-brief）、
  个股/公司估值、无书面交付的快问。
homepage: https://macrox.cn/
version: 0.1.0
author: MacroX
---

# macrox-industry-chain-map · 产业链地图

对 **一条商品产业链**（不是单个品种口述）生成机构风格的 **目录 + KPI HTML**。

> 没有本 Skill 时，模型容易只列几个品种名。  
> 本 Skill 强制：**环节表 → 代表品种 → 公开代理指标 → 库存节奏 → 政策冲击**。

## 前置

必读：`references/data-access.md` → `workflow.md` → `chain-catalog.md` → `proxy-rules.md` → `mcp-tools.md` → `output-schema.md` → `html-template.md`。

## 数据闸门（硬停）

只允许 MacroX 数据。禁止宿主搜索、行情网站、公司财报库顶替。

| 优先级 | 条件 | 动作 |
| --- | --- | --- |
| A | 会话已有 `mkt_*` / `struct_*` / `news_*` | 直调 MCP |
| B | 无 MCP | 用同级 `macrox-futures-mcp` 的 `call-node.js` / `call.py` + 真实 Token |
| — | A、B 都不可用 | **停止出稿**（见 `data-access.md`） |

不能挂 MCP 的客户端必须同时安装 `macrox-futures-mcp` 并配置 Token。

## 闸门（Phase 0）

### 拒答

个股财报、ROE、公司股权、非商品产业链。回复：`超出本 Skill 范围（无股票数据源）。` 后停止。

### 意图分流

| 信号 | 动作 |
| --- | --- |
| 产业链 / 上下游 / 产业地图 / 利润代理 | 进入本工作流 |
| 单品种一页纸 / tearsheet | 改用 `macrox-commodity-tearsheet` |
| 单品种深度研报 | 改用 `macrox-commodity-deep-dive` |
| 主题观察简报 | 改用 `macrox-topic-brief` |
| 「铜什么价」快问 | **退出**，普通回答 |

## 工作流摘要

1. 收参：链名（有色铜链 / 黑色钢链 / 能化聚酯等）、时间窗  
2. 用 `chain-catalog.md` 钉环节与代表 `symbol`，`ref_list_symbols` 校验  
3. **硬停**：列出环节表请用户确认（或用户说直接出）  
4. 并行取数：多品种 overview + 关键节点 basis/term/warehouse + 政策资讯  
5. 按 `proxy-rules.md` 填代理，禁止发明未取到的裂解价差数字  
6. 单一 HTML

## 核心原则

- 利润与供需只用 **可观察代理**（基差、近远月、仓单、已取到的现价对比），规则见 `proxy-rules.md`。  
- 缺节点标「未取到」，不得用训练知识补品种价格。  
- 不做目标价、不做公司推荐。
