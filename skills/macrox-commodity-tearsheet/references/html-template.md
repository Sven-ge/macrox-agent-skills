# HTML 模板约定 · macrox-commodity-tearsheet

单文件 HTML，自包含 CSS。建议文件名：`macrox-tearsheet-{symbol}-{as_of}.html`。

## 版式区块（顺序固定）

1. **顶栏**：MACROX COMMODITY TEARSHEET · `{symbol_name} ({symbol})` · `{as_of}`  
2. **标题区**：`main_title` / `sub_title` / `core_viewpoint`  
3. **快照条**：现价、涨跌、基差、期限、仓单、舆情（来自 `snapshot`）  
4. **六维**：每维一个小节（结论加粗 + 关键数据要点 + so what）  
5. **催化剂** 与 **风险** 两栏  
6. **情景表** Bull / Base / Bear  
7. **页脚**：MacroX MCP · 不构成投资建议 · 数据缺口列表  

## 视觉

- 白/浅灰底，金强调线 `#C9A227`，无紫渐变、无玻璃拟态。  
- 快照用紧凑定义列表或 6 格网格。  
- 最大宽约 900px。  

## 验收

- [ ] 六维章节齐全  
- [ ] 无「TBD」「待补充」占位（真正缺数用「未取到」并进 data_gaps）  
- [ ] 数字可在对话中指出对应工具  
- [ ] 无目标价 / 下单语句  
