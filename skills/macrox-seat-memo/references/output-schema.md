# Output Schema · macrox-seat-memo

```json
{
  "meta": {
    "ticker": "cu2610",
    "symbol": "CU",
    "trade_date": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "tables": [
    { "id": 1, "name": "龙虎榜", "tool": "seat_get_long_short_board", "ok": true, "highlights": ["string"] }
  ],
  "hypotheses": [
    {
      "id": "H1",
      "statement": "string",
      "evidence": ["string"],
      "falsify_if": ["string"],
      "watch_next": "string"
    }
  ],
  "tensions": ["string"],
  "structure_check": { "note": "string", "source_tools": ["string"] },
  "data_gaps": ["string"]
}
```

`tables` 应含四表记录（`ok=false` 时 highlights 空，gap 进 data_gaps）。  
`hypotheses` 1–3 条。禁止目标价。
