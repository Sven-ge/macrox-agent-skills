# 数据入口（硬闸门）

本 Skill **没有**自己的取数脚本。合法数据只有两条，按顺序探测；都失败则 **硬停**。

## 合法路径

| 优先级 | 条件 | 做法 |
| --- | --- | --- |
| A | 会话里已有 MacroX 工具（如 `news_search`、`mkt_list_overview`） | **直调 MCP**，不要走脚本 |
| B | 无 MCP，但本机有 `macrox-futures-mcp` 且 Token 已写入 | 用该目录的 `call-node.js`（优先）或 `call.py` 调同名工具 |

## 禁止

- 宿主自带搜索 / 网页浏览 / 新闻插件（含 Kimi、ChatGPT、通义等内置检索）
- 其他 MCP、爬虫、付费资讯 API
- 用模型记忆编造快讯标题、研报结论、价格与涨跌幅
- 为凑「调用次数」而改用上述来源

工具失败或无数据：该条标 **「未取到」**，写入 `notes`（工具名 + 错误摘要）。**不得**换源顶替。

## 探测 A

看当前会话是否已暴露 MacroX 工具名（`news_*` / `mkt_*` / `report_*` / `research_*` / `struct_*` / `factor_*`）。有则走 A，跳过 B。

## 探测 B（无 MCP 时必须做）

先定位 `macrox-futures-mcp` 目录（**实际 ls，禁止臆测**），候选：

1. 本 Skill 的**同级**目录：`../macrox-futures-mcp/`
2. 常见 skills 根：`~/.cursor/skills/macrox-futures-mcp/`、`~/.claude/skills/macrox-futures-mcp/`、`~/.agents/skills/macrox-futures-mcp/`
3. 用户本会话已给出的路径

目录须同时满足：

- 存在 `call-node.js` 或 `call.py`
- 存在 `mcp_config.json`（不是只有 `mcp_config.example.json`）
- `api_token` 不是空、不是 `YOUR_MACROX_MCP_TOKEN`

用 Node（无 Node 再用 Python）做一次连通性探测，例如：

```bash
node -e "require('$SCRIPTS/call-node.js').call('news_list_hot',{limit:1}).then(r=>console.log(JSON.stringify(r))).catch(e=>{console.error(e);process.exit(1)})"
```

```bash
python3 -c "import json,sys; sys.path.insert(0,'$SCRIPTS'); from call import call; print(json.dumps(call('news_list_hot',{'limit':1}),ensure_ascii=False))"
```

把 `$SCRIPTS` 换成探测到的绝对路径。后续取数同样用 `call('工具名', {参数})`，工具名与 `mcp-tools.md` 一致。

脚本读同目录 `mcp_config.json`，会把 `api_token` 拼到 `https://mcp.macrox.cn/mcp?token=`。

## 硬停（A、B 皆不可用）

**立刻停止**本工作流：不要写 schema、不要出 HTML、不要改用其他源。只回复：

```text
无法使用 MacroX 数据，已停止出稿。

本 Skill 禁止用搜索引擎或其他插件顶替行情/快讯/研报。

请任选其一后再重试：
1. 客户端可挂 MCP：在 MCP 配置中加入
   url: https://mcp.macrox.cn/mcp?token=你的Token
2. 客户端不能挂 MCP（如部分 Kimi）：必须同时安装技能 macrox-futures-mcp，
   复制 mcp_config.example.json 为 mcp_config.json，填入 Hub Token。

Token 在 MacroX Hub 个人中心生成（不代填密钥）：
https://www.soarcloudtech.com/macrox/mcp/
```

缺目录 → 引导安装 `macrox-futures-mcp`。  
缺 `mcp_config.json` 或仍是占位 Token → 引导复制 example 并填写，**不要**用占位符发请求。
