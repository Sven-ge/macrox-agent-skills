# MacroX Agent Skills

公开 Skill 仓库，供 [`npx skills`](https://github.com/vercel-labs/skills) 安装到 Cursor / Claude Code 等客户端。

- **不做官方 CLI**；数据能力走 MacroX MCP（Streamable HTTP）。
- **Token 不自动下发**：在 [MacroX Hub](https://www.soarcloudtech.com/macrox/mcp/) 登录后于个人中心生成并复制。
- **多 Skill**：本仓为 monorepo，用 `--skill <name>` 按需安装。

## 当前 Skills

| 目录名 (`--skill`) | 说明 | MCP |
| --- | --- | --- |
| `macrox-futures-mcp` | 期货投研（行情/资讯/结构/席位/研报/量化等） | 共用 `macrox-mcp` |

## 安装 Skill（npx）

```bash
npx skills add Sven-ge/macrox-agent-skills \
  --skill macrox-futures-mcp \
  --agent cursor \
  --global \
  --yes
```

多客户端可再加 `--agent claude-code` 等。若仓库迁到组织账号，把 `Sven-ge` 换成组织名即可。

**不要**默认使用 `--skill '*'`；按产品需要点名安装。

## 配置 MCP（与 Skill 并列）

Skill 负责场景与填参；会话内工具调用优先走已挂载的 MCP。

1. 打开 Hub → 登录 → 个人中心 → 复制 Token  
2. 写入客户端 MCP 配置（例如 `~/.cursor/mcp.json`），**合并**勿清空其他 server：

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

将 `YOUR_MACROX_MCP_TOKEN` 换成真实 Token。生产鉴权使用 URL 查询参数 `?token=`，不要只配 Bearer Header。

若已配置过 `macrox-mcp`，再装同网关的其他 Skill **无需重复挂 MCP**。

### 可选：Skill 脚本兜底

未挂载 MCP 时，可用包内 `call-node.js` / `call.py`。复制 example 后填入 Token：

```bash
cp skills/macrox-futures-mcp/mcp_config.example.json \
   ~/.cursor/skills/macrox-futures-mcp/mcp_config.json
# 编辑 api_token
```

**禁止**把含真实 Token 的 `mcp_config.json` 提交回本仓库。

## 多 Skill 约定

见 [docs/MULTI_SKILL.md](docs/MULTI_SKILL.md)。

摘要：

- 新 Skill 放在 `skills/macrox-<name>/`，目录名 = `--skill` 参数，**不含版本号**。
- 与现网共用 `https://mcp.macrox.cn/mcp` 的，标明「共用 macrox-mcp」；独立产品线则在该 Skill 的 `SKILL.md` 写明自己的 MCP 名与 URL。
- 版本写在各 Skill `SKILL.md` frontmatter；发版可用 git tag（如 `macrox-futures-mcp@1.4.1`），并与 ZIP CDN 同源同版本。

## 相关链接

- 官网：https://macrox.cn/
- Hub：https://www.soarcloudtech.com/macrox/mcp/
- MCP 端点：`https://mcp.macrox.cn/mcp`
- ZIP 兜底包（企业/无 npx）：见 Hub「一键安装 Skill」页

## License

文档与 Skill 内容版权归 MacroX；使用须持有有效 MCP Token。
