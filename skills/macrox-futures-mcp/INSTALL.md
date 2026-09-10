# MacroX 期货投研工具 · 安装说明

官网：https://macrox.cn/  
Hub（复制 Token）：https://www.soarcloudtech.com/macrox/mcp/  
ZIP / 安装引导：https://www.soarcloudtech.com/macrox/mcp/guides/SKILL_INSTALL_GUIDE.html

## npx 安装

```bash
npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp
```

CLI 会询问装到哪个客户端。若已确定客户端并希望跳过提问：

```bash
npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp -g -a claude-code -y
```

`-a` 换成你的客户端（`cursor`、`claude-code`、`codex`、`cline` 等）。`-g` 为全局，`-y` 跳过确认。

其他场景 Skill 把 `--skill` 换成对应名称即可，列表见仓库根 README。

## 手动拷贝

将本目录放到客户端可读的 skills 路径：

```bash
mkdir -p <skills-root>/macrox-futures-mcp
cp -R . <skills-root>/macrox-futures-mcp/
```

不要把含真实 Token 的 `mcp_config.json` 发给他人。

## 配置 Token（仅脚本需要）

客户端未挂 MCP、需要 `call-node.js` / `call.py` 时：复制 `mcp_config.example.json` → `mcp_config.json`，填入 Hub Token。脚本会拼 `?token=`。

```json
{
  "mcp_url": "https://mcp.macrox.cn/mcp",
  "api_token": "YOUR_MACROX_MCP_TOKEN"
}
```

## 挂载 MCP

在客户端 MCP 配置中合并（不要清空其他 server）：

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

Token 写在 `url` 的 `?token=` 中。若已配置 `macrox-mcp`，可跳过。

## 验证

```bash
node -e "require('./call-node.js').call('mkt_list_overview',{symbols:'CU',limit:1}).then(console.log)"
```

已挂载 MCP 时，可在会话里直接调用同名工具。

## 环境

- 可访问 `mcp.macrox.cn`（ZIP 安装还需 `images.macrox.cn`）
- 脚本方案：Node.js 16+ 或 Python 3.9+
