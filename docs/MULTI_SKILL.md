# 多 Skill 约定

本仓是 **MacroX Agent Skills monorepo**：一个 Git 仓库、多个可独立安装的 Skill。

## 目录与命名

```text
macrox-agent-skills/
  README.md
  docs/
    MULTI_SKILL.md          ← 本文
  skills/
    macrox-futures-mcp/          ← 工具总索引
    macrox-topic-brief/          ← 主题观察简报
    macrox-commodity-tearsheet/  ← 品种 Tear Sheet
    macrox-industry-chain-map/   ← 产业链地图
    macrox-commodity-deep-dive/  ← 品种深度研报
    macrox-seat-memo/            ← 席位资金备忘
    macrox-event-impact/         ← 事件影响
    macrox-report-studio/        ← 刊物派生
```

| 规则 | 说明 |
| --- | --- |
| 前缀 | 一律 `macrox-`，降低与社区 Skill 撞名 |
| 目录名 | = `SKILL.md` frontmatter `name` = `npx skills add --skill` 参数 |
| 版本号 | **不进目录名**；写在 `SKILL.md` 的 `version` 与发版 tag |
| 密钥 | 只允许 `mcp_config.example.json`；禁止提交真实 `mcp_config.json` |

## 安装粒度

```bash
# 推荐：按需安装；不加 -a，让 CLI 询问客户端
npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp

# 指定客户端并跳过确认（把 <agent> 换成 cursor / claude-code / codex / cline 等）
# npx skills add Sven-ge/macrox-agent-skills --skill macrox-futures-mcp -g -a <agent> -y

# 不推荐作为产品默认：一次装全部
# npx skills add Sven-ge/macrox-agent-skills --skill '*' -g --agent '*' -y
```

产品页 / Hub 卡片应为 **每个 Skill 一条独立命令**，且 **不要写死 `-a cursor`**。

## 与 MCP 的关系

| 类型 | 何时用 | MCP 配置 |
| --- | --- | --- |
| 同网关用法包 | 同一 `macrox-mcp` 端点，Skill 只换场景与参数规范 | Token 与 `mcpServers.macrox-mcp` **共用**；多装几个 Skill 不必重复挂 MCP |
| 独立产品线 | 新端点或不同工具集 | 该 Skill 的 `SKILL.md` / `INSTALL.md` 写明自己的 server 名与 URL；Token 仍由用户在 Hub（或对应产品）自助复制 |

当前 `macrox-futures-mcp` 属于 **同网关用法包**。场景 Skill 无 MCP 时必须调用本包脚本，禁止改用宿主搜索。

会话内若已出现 MacroX MCP 工具，**优先直调 MCP**；Skill 负责何时调用、如何填参；脚本为未挂 MCP 时的兜底。

## 与内部仓

草稿在内部仓 `期策智能体及mcp/skills/`。本仓是分发源。内部仓脚本：

```bash
bash scripts/sync-skills.sh to-public    # 草稿 → 本仓
bash scripts/sync-skills.sh from-public  # 本仓 → 草稿
```

公开 Skill 只对接对外 MCP（`macrox-mcp` / `https://mcp.macrox.cn/mcp`），不对内 7 工具 Dify MCP。

## 发版

1. 更新对应 `skills/<name>/SKILL.md` 的 `version`。
2. 提交并打 tag，建议：`<skill-name>@<semver>`（例：`macrox-futures-mcp@1.4.1`）。
3. 若仍发布 ZIP CDN，与本仓 **同源同版本**，避免内容漂移。
4. 发版检查：无真实 Token、无 `__pycache__`、example 占位符为 `YOUR_MACROX_MCP_TOKEN`。

## 新增 Skill 清单

1. 在 `skills/` 下新建 `macrox-<short-name>/`，至少包含 `SKILL.md`。
2. 在根 `README.md` 的「当前 Skills」表增加一行（说明 + MCP 类型）。
3. 本地验证：`npx skills add <本地路径或远程> --skill macrox-<short-name>`（按本机客户端选择 `-a`）。
