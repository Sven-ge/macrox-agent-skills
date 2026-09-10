# Output Schema · macrox-commodity-deep-dive

```json
{
  "meta": {
    "symbol": "CU",
    "symbol_name": "沪铜",
    "ticker": "cu2610 | null",
    "tier": "light|medium|heavy",
    "as_of": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "hypotheses": [
    {
      "id": "H1",
      "statement": "string",
      "proxy": "string",
      "falsify_if": "string",
      "verdict": "supported|mixed|rejected|insufficient",
      "confidence": "High|Medium|Low"
    }
  ],
  "chapters": [
    {
      "id": "string",
      "title": "string",
      "body": "string",
      "source_tools": ["string"]
    }
  ],
  "tensions": ["string"],
  "engine": [
    { "tool": "anl_run_quant", "excerpt": "string", "note": "服务端算法，未改写" }
  ],
  "qa": { "passed": true, "gaps": ["string"] },
  "data_gaps": ["string"]
}
```

- `hypotheses` 条数符合档位。  
- `chapters` light ≥4；medium ≥6；heavy ≥8（含引擎章与 QA）。  
- `engine` 未调用则为 `[]`，light 允许空。
