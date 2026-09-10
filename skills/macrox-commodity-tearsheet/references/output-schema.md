# Output Schema · macrox-commodity-tearsheet

```json
{
  "meta": {
    "symbol": "CU",
    "symbol_name": "沪铜",
    "ticker": "cu2610 | null",
    "as_of": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "headline": {
    "main_title": "string (8-20 chars)",
    "sub_title": "string",
    "core_viewpoint": "string (3-5 sentences)"
  },
  "snapshot": {
    "last": "string",
    "chg_pct": "string",
    "basis_note": "string",
    "term_note": "string",
    "warehouse_note": "string",
    "sentiment_note": "string"
  },
  "dimensions": [
    {
      "id": "H1",
      "name": "价格阶段",
      "conclusion": "string",
      "confidence": "High|Medium|Low",
      "key_data": ["string"],
      "so_what": "string"
    }
  ],
  "catalysts": [
    { "date": "YYYY-MM-DD", "text": "string", "source": "string" }
  ],
  "risks": ["string"],
  "scenarios": {
    "bull": { "condition": "string", "implication": "string" },
    "base": { "condition": "string", "implication": "string" },
    "bear": { "condition": "string", "implication": "string" }
  },
  "appendix_tools": [
    { "tool": "anl_run_quant", "note": "string | omitted if unused" }
  ],
  "data_gaps": ["string"]
}
```

`dimensions` 必须含 H1–H6 共 6 项。  
`catalysts` 目标 ≥3；不足则在 `data_gaps` 说明。  
禁止目标价字段。
