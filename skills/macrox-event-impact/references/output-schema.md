# Output Schema · macrox-event-impact

```json
{
  "meta": {
    "event_title": "string",
    "event_date": "YYYY-MM-DD",
    "window_start": "YYYY-MM-DD",
    "window_end": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "facts": [{ "text": "string", "source": "string", "date": "YYYY-MM-DD" }],
  "chain": [
    {
      "symbol": "CU",
      "channel": "price|basis|term|inventory|narrative",
      "logic": "string",
      "observation": "string | 未取到",
      "source_tools": ["string"]
    }
  ],
  "verdict_card": {
    "headline": "string",
    "bullets": ["string", "string", "string"]
  },
  "scenarios": {
    "realized": { "condition": "string", "implication": "string" },
    "scenario_a": { "condition": "string", "implication": "string" },
    "scenario_b": { "condition": "string", "implication": "string" }
  },
  "data_gaps": ["string"]
}
```

`chain` 1–4 条。禁止目标价字段。
