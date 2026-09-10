# 工作流 · macrox-event-impact

## 步骤 1：事件卡片

字段：`event_title`、`event_date`、`facts[]`（每条可回溯到新闻标题或用户原话）。  
MacroX 搜不到且用户没给事实 → 停止并要标题/日期。

## 步骤 2：链路（可短确认）

列出 1–4 个 `symbol` + 渠道。用户可改品种。含糊则问一次。

## 步骤 3：取数

1. 资讯核对：`news_search`  
2. `cal_list_days`  
3. 每个核心品种：`mkt_get_daily_bars`（覆盖冲击窗）+ overview  
4. 渠道需要时：basis / warehouse / term  

## 步骤 4：情景表

三列建议：`realized`（窗内已发生）/ `scenario_a` / `scenario_b`。  
每格：可观察条件 + 对价格或结构的含义。无目标价。

## 步骤 5：schema → HTML
