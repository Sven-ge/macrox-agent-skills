# Output Schema · macrox-report-studio

```json
{
  "meta": {
    "source_kind": "morning|evening|article",
    "source_id": "string",
    "source_date": "YYYY-MM-DD",
    "source_title": "string",
    "source_tool": "report_get_paper",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "chapters": [
    { "heading": "string", "body_md": "string", "origin": "verbatim-adapted" }
  ],
  "symbol_index": [
    {
      "symbol": "CU",
      "name": "沪铜",
      "in_copy": "string（稿内原句摘要）",
      "live_note": "string | 未取到",
      "source_tool": "mkt_list_overview"
    }
  ],
  "unresolved_names": ["string"],
  "qa_flags": ["string"],
  "data_gaps": ["string"]
}
```

`body_md` 允许为排版做轻微分段，禁止改结论。`qa_flags` 列出所有现况冲突。
