# 工作流 · macrox-report-studio

## 步骤 1：选刊

用户指定日期/早报晚报 → `report_list_papers` → `report_get_paper`。  
指定研究文章 → `news_list_articles` → `news_get_article`。  
用户粘贴正文：仅当其声明来自 MacroX 刊物；仍建议补 id 以便溯源。

## 步骤 2：拆章

按 `answer`/正文标题切 `chapters`。无法切分则整篇一章，不要用模型另写一篇。

## 步骤 3：品种索引

抽取品种中文名/代码 → `ref_list_symbols`。无法对应的名称进 `unresolved_names`。

## 步骤 4：脚注核对

索引品种并行 `mkt_list_overview`；用户关心结构时再 `struct_get_basis`。  
报告日与 today 不同必须标注 as_of。

## 步骤 5：QA → HTML

走完 `qa-checklist.md` 再渲染。
