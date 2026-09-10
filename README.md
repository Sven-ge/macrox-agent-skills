# MacroX Agent Skills

在 Cursor、Claude Code、Cline、Kimi 等客户端里，用这些 Skill 做期货投研：快问快答、主题简报、品种速览、产业链、深度研报、席位备忘、事件影响、早晚报排版。

数据一律走 [MacroX MCP](https://mcp.macrox.cn/mcp)。Token 在 [MacroX Hub](https://www.soarcloudtech.com/macrox/mcp/) 登录后于个人中心自行复制，安装过程不会代填密钥。

## Skill 列表与场景

先装总索引 `macrox-futures-mcp`（工具说明 + 无 MCP 时的脚本）。书面长报告再按场景加装对应包。

| 安装名 (`--skill`) | 什么时候用 | 不要用它做 |
| --- | --- | --- |
| `macrox-futures-mcp` | 现价、快讯、龙虎榜、基差、仓单、研报列表等**快问快答**；以及给其他 Skill 提供取数脚本 | 硬凑长篇 HTML 报告 |
| `macrox-topic-brief` | 「做一份 XX 观察 / 简报 / digest」，要固定栏目的 HTML 主题刊物 | 单条新闻评论、只要口头三点 |
| `macrox-commodity-tearsheet` | 「品种速览 / 一页纸 / tearsheet」+ 品种（如沪铜 / CU） | 现价一句问、主题观察刊物 |
| `macrox-industry-chain-map` | 「产业链 / 上下游 / 产业地图」有色、黑色、能化 | 公司财报、个股估值 |
| `macrox-commodity-deep-dive` | 「深度研报」并分 light / medium / heavy | 只要一页纸速览（用 tearsheet） |
| `macrox-seat-memo` | 「席位备忘 / 主力假设 / 证伪清单」+ 合约 | 只听一次龙虎榜口述 |
| `macrox-event-impact` | 「事件影响 / 冲击窗 / 情景表」 | 要买卖点或交易信号 |
| `macrox-report-studio` | 把已有早晚报、研究文章拆章排版，并核对现况脚注 | 没有原文却从零写简报 |

选用说明也可看 [docs/MULTI_SKILL.md](docs/MULTI_SKILL.md)。

## 安装

按需安装，一次一个 Skill。不要默认 `--skill '*'`。

```bash
npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp
npx skills add Sven-ge/macrox-agent-skills --skill macrox-topic-brief
npx skills add Sven-ge/macrox-agent-skills --skill macrox-commodity-tearsheet
npx skills add Sven-ge/macrox-agent-skills --skill macrox-industry-chain-map
npx skills add Sven-ge/macrox-agent-skills --skill macrox-commodity-deep-dive
npx skills add Sven-ge/macrox-agent-skills --skill macrox-seat-memo
npx skills add Sven-ge/macrox-agent-skills --skill macrox-event-impact
npx skills add Sven-ge/macrox-agent-skills --skill macrox-report-studio
```

命令会询问装到哪个客户端。可选参数：

| 参数 | 作用 |
| --- | --- |
| `--skill <name>` | 上表中的安装名 |
| `-g` | 全局安装（各项目都能用） |
| `-a <agent>` | 指定客户端，如 `cursor`、`claude-code`、`codex`、`cline`；`'*'` 表示本机已检测到的全部 |
| `-y` | 跳过确认 |

例如已确定用 Claude Code、并要全局安装：

```bash
npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp -g -a claude-code -y
```

无 npx 时，可用 Hub 上的 ZIP / 安装引导：https://www.soarcloudtech.com/macrox/mcp/

不能在客户端里挂自定义 MCP 时（部分 Kimi 等）：场景 Skill **不会**改用搜索引擎顶替数据。请同时安装 `macrox-futures-mcp`，并在该 Skill 目录写入 `mcp_config.json`（见下文）。只装场景包会提示无法取数并停止出稿。

## 配置 MCP

Skill 负责选场景和填参。会话里已经出现 MacroX 工具时，优先直接调 MCP。

1. 打开 [Hub](https://www.soarcloudtech.com/macrox/mcp/) → 登录 → 个人中心 → 复制 Token  
2. 写入客户端的 MCP 配置（合并，不要清空其他 server）：

```json
{
  "mcpServers": {
    "macrox-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.macrox.cn/mcp?token=YOUR_MACROX_MCP_TOKEN"
    }
  }
}
```

把 `YOUR_MACROX_MCP_TOKEN` 换成真实 Token。鉴权写在 URL 的 `?token=` 里，不要只配 Bearer Header。

已经配过 `macrox-mcp` 后，再装其他同网关 Skill **不必再挂一遍 MCP**。

### 未挂 MCP 时的脚本

仅当客户端没有 MacroX 工具时使用。复制 `mcp_config.example.json` 为 `mcp_config.json`，填入 Hub Token。文件放在已安装的 `macrox-futures-mcp` 目录（常见为 `~/.agents/skills/macrox-futures-mcp/`，或该客户端自己的 skills 目录）。

不要把填好 Token 的配置发给他人。

## 相关链接

- 官网：https://macrox.cn/
- Hub（Token 与安装引导）：https://www.soarcloudtech.com/macrox/mcp/
- MCP：`https://mcp.macrox.cn/mcp`

## License

文档与 Skill 内容版权归 MacroX；使用须持有有效 MCP Token。
