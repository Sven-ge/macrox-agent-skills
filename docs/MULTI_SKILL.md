# 选用哪个 Skill

给用户和 Agent：按意图选包，不要用总索引硬凑长报告。安装命令见 [README.md](../README.md)。

## 快问快答 → `macrox-futures-mcp`

现价、涨跌榜、快讯、基差、仓单、龙虎榜、研报列表、早晚报原文、量化工具单次调用。

## 书面交付 → 场景包

| 用户说法 | Skill | 产出 |
| --- | --- | --- |
| 观察 / 简报 / digest / 主题刊物 | `macrox-topic-brief` | 固定栏目 HTML |
| 品种速览 / 一页纸 / tearsheet | `macrox-commodity-tearsheet` | 六维 Tear Sheet HTML |
| 产业链 / 上下游 / 产业地图 | `macrox-industry-chain-map` | 环节表 + 代理 KPI HTML |
| 深度研报 / light·medium·heavy | `macrox-commodity-deep-dive` | 分档多章节 HTML |
| 席位备忘 / 主力假设 / 证伪 | `macrox-seat-memo` | 四表交叉备忘 HTML |
| 事件影响 / 冲击窗 / 情景表 | `macrox-event-impact` | 结论卡 + 情景表 HTML |
| 早晚报或研报拆章排版 | `macrox-report-studio` | 派生 HTML（不重写结论） |

## 共用数据入口

全部 Skill 使用同一 MCP：`https://mcp.macrox.cn/mcp?token=`。多装几个场景包不必重复挂 MCP。

会话里已有 MacroX 工具时直接调用。未挂 MCP 时，用已安装的 `macrox-futures-mcp` 里的 `call-node.js` / `call.py`（需 `mcp_config.json`）。禁止用搜索引擎顶替行情或快讯。
