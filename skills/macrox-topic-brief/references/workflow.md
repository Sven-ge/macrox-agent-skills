# 工作流 · macrox-topic-brief

## 步骤 1：收集参数

若用户未给全，**一次问清**：

| 字段 | 说明 | 归一化 |
| --- | --- | --- |
| `subject_name` | 主题（区域板块 / 品种链 / 政策议题 / 机构） | 短标题字符串 |
| `period_start` / `period_end` | 时间窗 | ISO `YYYY-MM-DD`；「过去两周/一个月/一季度」按今天换算 |
| `author` | 署名 | 默认空（不显示）；用户指定则写入 |
| `focus_symbols` | 可选：关注品种码列表 | 大写，如 `CU,AL` |

用户已在一句话里给全则可跳过提问。

## 步骤 2：并行素材采集（强制时间窗 · 仅 MacroX）

开工前已通过 `data-access.md` 闸门（A 直调 MCP 或 B 脚本）。**宿主搜索不计入**本步。

**每次检索必须带时间意识**：优先用工具参数里的日期/time_range；自然语言查询在关键词中带上起止日期。

最低取数集（按主题类型取舍，合计建议 ≥4 次 **MacroX** 工具调用）：

| 主题类型 | 建议调用 |
| --- | --- |
| 品种/板块 | `news_search` + `news_list_intel` + `news_list_hot` + 1–2 个 `mkt_list_overview`/`struct_get_basis` 脚注 |
| 政策/宏观议题 | `news_search` + `research_list_reports` + `report_list_papers`（再 `report_get_paper` 1 篇） |
| 机构/研报主题 | `research_list_reports` + `news_list_articles` → `news_get_article` |

规则：

- 栏目条目的事件日期应落在 `[period_start, period_end]`；窗外材料只能进「背景」并显式标时点。  
- 数字脚注（价格、涨跌幅）必须来自 MacroX `data`，写清品种/时点。非 MacroX 来源一律不用。

工具参数细节见 `mcp-tools.md`。脚本调用见 `data-access.md`。

## 步骤 3：方向确认（硬停）⚠️

素材齐后 **停下来** 用条目列表请用户确认，例如：

```text
拟写主题：{subject_name}（{period_start} ~ {period_end}）
焦点稿方向：……
四个栏目各 2–4 条候选标题：……
是否按此出 HTML 简报？（确认 / 修改方向 / 取消）
```

用户确认或明确「直接出」后再进入步骤 4。

## 步骤 4：填充 Output Schema

按 `output-schema.md` 生成中间结构（可先写 JSON 或 Markdown 字段表）。  
**必填字段不得空字符串充数**；无材料的栏目写 `items: []` 并在 `notes` 说明原因。

## 步骤 5：渲染 HTML + 自检

按 `html-template.md` 输出 **一个** HTML 文件（建议路径：`./macrox-topic-brief-{subject}-{period_end}.html`）。

自检清单：

- [ ] 仅一个 HTML 文件，CSS 内联或写在 `<style>`  
- [ ] 封面含主题、时间窗、生成日  
- [ ] 焦点稿 + 至多 4 个栏目，每条有来源标题与日期  
- [ ] 无窗外未标注的「当期」事件  
- [ ] 无编造行情数字  
- [ ] 所有条目可回溯到 MacroX 工具 `data`（非搜索引擎）  
- [ ] 文末有「数据来源：MacroX MCP」字样  
