# Output Schema · macrox-report-studio

中间对象，渲染 HTML 前必须填完。`origin` 只能是 `generated-from-mcp`。

```json
{
  "meta": {
    "report_kind": "morning|evening",
    "as_of": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "source_tools": ["mkt_list_overview", "news_list_intel"],
    "language": "zh"
  },
  "hero": {
    "conclusion": "string",
    "tape": "string",
    "driver": "string",
    "watch": "string",
    "risk": "string"
  },
  "kpis": [
    { "label": "上涨家数", "value": "28", "note": "string|未取到", "source_tool": "mkt_list_overview" }
  ],
  "ranking": [
    {
      "rank": 1,
      "symbol": "SC",
      "name": "原油",
      "ticker": "sc2610",
      "last": 769,
      "change_pct": 6.44,
      "driver": "string|",
      "source_tool": "mkt_list_overview"
    }
  ],
  "news": [
    { "time": "21:08", "text": "string", "symbol": "HC|", "source_tool": "news_list_intel" }
  ],
  "radar": [
    { "symbol": "CU", "name": "铜", "indicator": "string", "summary": "string", "source_tool": "watch_get_ranks" }
  ],
  "focus": ["string"],
  "evening_highlights": [
    { "category_label": "结构 · 黑色", "title": "string", "summary": "string" }
  ],
  "seat_changes": [
    { "symbol": "RB", "ticker": "rb2701", "interpretation": "string", "source_tool": "seat_get_long_short_board" }
  ],
  "basis_rows": [
    { "symbol": "RB", "term_structure": "string", "near_basis_rate_pct": 0, "source_tool": "struct_get_basis" }
  ],
  "unresolved_names": ["string"],
  "data_gaps": ["string"]
}
```

早报：`evening_highlights` / `seat_changes` / `basis_rows` 可空数组。  
晚报：`news` 用作时间线；`focus` 为明日关注。  
`ranking` 须含涨跌两端，不要只写领涨。
