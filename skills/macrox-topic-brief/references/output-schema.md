# Output Schema · macrox-topic-brief

分析层产出下列结构；渲染层（HTML）只消费本契约，不重做分析结论。

```json
{
  "meta": {
    "subject_name": "string",
    "period_start": "YYYY-MM-DD",
    "period_end": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "author": "string | empty",
    "language": "zh",
    "focus_symbols": ["CU"]
  },
  "hero": {
    "title": "string",
    "dek": "string (1-2 sentences)",
    "bullets": ["string", "string", "string"]
  },
  "focus_story": {
    "headline": "string",
    "summary": "string (150-400 words)",
    "key_numbers": [
      { "label": "string", "value": "string", "as_of": "YYYY-MM-DD", "source_tool": "string" }
    ],
    "sources": [
      { "title": "string", "date": "YYYY-MM-DD", "kind": "news|report|article|market" }
    ]
  },
  "sections": [
    {
      "id": "policy|supply|demand|market|misc",
      "title": "string",
      "items": [
        {
          "headline": "string",
          "date": "YYYY-MM-DD",
          "blurb": "string",
          "source_title": "string",
          "in_window": true
        }
      ]
    }
  ],
  "market_footnotes": [
    {
      "symbol": "CU",
      "last": "string",
      "chg_pct": "string",
      "note": "string",
      "source_tool": "mkt_list_overview"
    }
  ],
  "notes": ["string"]
}
```

## 约束

- `sections` 建议 3–4 个；每个 `items` 2–5 条。  
- `in_window=false` 的条目不得放进栏目，只能进 `focus_story` 背景句并标时点。  
- `key_numbers` / `market_footnotes` 的数值必须有 `source_tool`。  
- `author` 空则 HTML 不渲染署名行。
