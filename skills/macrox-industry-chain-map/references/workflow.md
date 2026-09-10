# 工作流 · macrox-industry-chain-map

## 步骤 1：收参

一次问清缺项：

| 字段 | 说明 |
| --- | --- |
| `chain_id` | 见 `chain-catalog.md`；含糊则给 2–3 个选项 |
| `period_start` / `period_end` | 默认近 30 日 |
| `extra_symbols` | 用户点名的增补品种 |

## 步骤 2：钉目录（硬停）

列出拟用环节表（环节名 + 代表 symbol），问：确认 / 增删节点 / 取消。  
用户说「直接出」可跳过。

## 步骤 3：取数（仅 MacroX）

闸门见 `data-access.md`。建议并行：

1. `mkt_list_overview`（本链全部代表品种）  
2. 2–4 个关键节点：`struct_get_basis` + `struct_get_term` + `struct_get_warehouse`  
3. `news_search`（链名 + 时间窗）1 次；政策主题再 `research_list_reports` 或 `report_list_papers`  

宿主搜索不计入。

## 步骤 4：填 schema

按 `output-schema.md` + `proxy-rules.md`。  
未取到的 KPI 不得用记忆填充。

## 步骤 5：HTML + 自检

按 `html-template.md`。

- [ ] 单一 HTML  
- [ ] 环节表完整（可含未取到）  
- [ ] 每个数字有 `source_tool`  
- [ ] 无公司财报/目标价  
- [ ] 页脚「数据来源：MacroX MCP」
