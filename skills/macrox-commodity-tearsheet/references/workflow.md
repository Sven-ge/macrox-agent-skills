# 工作流 · macrox-commodity-tearsheet

## Phase 1：取数编排（按维准备原料）

先通过 `data-access.md` 闸门。下列调用必须走 MacroX（MCP 或脚本）；**宿主搜索不计入**。

对 `symbol` 建议最小工具集（可并行）：

| 维度原料 | 工具 |
| --- | --- |
| 价格与波动 | `mkt_list_overview`，`mkt_get_daily_bars`（如 `window_days=60` 或 120） |
| 结构 | `struct_get_basis`，`struct_get_term`，`struct_get_warehouse`，`struct_get_position_ratio` |
| 舆情/资讯 | `factor_get_sentiment`，`news_search` 或 `news_list_intel`（品种相关） |
| 席位（可选增强） | 若用户给了/能解析 `ticker`：`seat_get_long_short_board`，`seat_get_member_ranks`；否则席位维写「未指定合约，跳过明细」 |
| 日历/规则（可选） | `ref_get_contract`，`cal_list_days`（临近假期时） |
| 深度附录（可选） | `anl_run_quant`（小窗口，如 `window_years=2`，sections 精简） |

详见 `mcp-tools.md`。脚本调用见 `data-access.md`。

**停检**：核心价格 + 至少 2 个结构序列成功，否则询问用户是否继续（数据不足版）或更换品种。仍不得改用非 MacroX 源补数。

## Phase 2：六维分析（强制）

严格按 `six-dimension.md` 逐维写完。  
每维结构：数据基础 → 推理 → 结论（含置信度 High/Medium/Low）。

全部完成后进入 Phase 3（禁止边分析边出最终 HTML）。

## Phase 3：填充 Output Schema

将六维与元数据写入 `output-schema.md` 契约（brief 文件）。  
自检：

- [ ] 六维均有结论句  
- [ ] 关键数字带工具来源或「未取到」  
- [ ] 催化剂 ≥3 条（可来自快讯；无则注明本期资讯稀疏）  
- [ ] 风险清单 ≥3 条  
- [ ] Bull/Base/Bear 情景表有可检验表述（基于结构/价格，不编造目标价）

## Phase 4：渲染 Tear Sheet HTML

按 `html-template.md` 生成单文件 HTML。  
不做 PDF 强制要求；若环境可导出 PDF 可作为附加，但 HTML 为验收物。

## Phase 5：交付话术

```text
已生成 {symbol} 品种速览：
- 结论摘要：…
- 文件：…
六维：①… ②… …
数据不足项：…
```
