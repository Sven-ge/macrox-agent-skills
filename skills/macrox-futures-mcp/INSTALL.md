# MacroX 期货投研工具 · Skill 安装说明

官网：https://macrox.cn/

- Hub：https://www.soarcloudtech.com/macrox/mcp/
- 安装引导（ZIP / Agent 剧本）：https://www.soarcloudtech.com/macrox/mcp/guides/SKILL_INSTALL_GUIDE.html
- 技能包 ZIP：https://images.macrox.cn/macrox-analysis/mcp/macrox-mcp-skill-1.4.1.zip

推荐用 **npx skills** 安装；ZIP / 拷贝目录为兜底。Token 请在 Hub 个人中心自行生成并复制。

## 推荐：npx skills

在本仓库根（或已发布的 GitHub 地址）执行：

```bash
npx skills add Sven-ge/macrox-agent-skills \
  --skill macrox-futures-mcp \
  --agent cursor \
  --global \
  --yes
```

需要 Claude Code 等可再加 `--agent claude-code`。

## 兜底：手动拷贝

将 `macrox-futures-mcp` 目录放到 Agent 可读的 skills 路径：

```bash
mkdir -p <skills-root>/macrox-futures-mcp
cp -R . <skills-root>/macrox-futures-mcp/
```

建议覆盖拷贝。勿外发含真实 Token 的 `mcp_config.json`。

## 配置 Token（Skill 脚本，可选）

仅在未挂载 MCP、需用 `call-node.js` / `call.py` 时需要。复制 `mcp_config.example.json` → `mcp_config.json`，填写 Hub 复制的 Token。脚本通过 `?token=` 鉴权。

```json
{
  "mcp_url": "https://mcp.macrox.cn/mcp",
  "api_token": "YOUR_MACROX_MCP_TOKEN"
}
```

## 挂载宿主 MCP（与 Skill 并列）

在 Cursor / Claude Desktop / Cline 等宿主的 MCP 配置中合并（勿清空其他 server）：

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

生产须把 Token 写在 `url` 的 `?token=` 中。若已配置 `macrox-mcp`，可跳过本步。

## 验证

```bash
node -e "require('./call-node.js').call('mkt_list_overview',{symbols:'CU',limit:1}).then(console.log)"
```

会话内亦可直接调用同名 MCP 工具（挂载生效后）。

## 环境

- 出网访问 `mcp.macrox.cn`（及 ZIP 场景下的 `images.macrox.cn`）
- 脚本方案：Node.js 16+ 或 Python 3.9+
