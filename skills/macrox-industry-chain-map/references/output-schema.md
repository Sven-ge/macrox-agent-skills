# Output Schema · macrox-industry-chain-map

```json
{
  "meta": {
    "chain_id": "steel-chain",
    "chain_name": "黑色钢链",
    "period_start": "YYYY-MM-DD",
    "period_end": "YYYY-MM-DD",
    "generated_at": "YYYY-MM-DD",
    "language": "zh"
  },
  "hero": {
    "title": "string",
    "dek": "string",
    "bullets": ["string", "string", "string"]
  },
  "nodes": [
    {
      "stage": "upstream|midstream|downstream|related",
      "label": "string",
      "symbol": "RB",
      "symbol_name": "string",
      "last": "string | 未取到",
      "chg_pct": "string | 未取到",
      "basis_note": "string | 未取到 | skipped",
      "term_note": "string | 未取到 | skipped",
      "warehouse_note": "string | 未取到 | skipped",
      "source_tools": ["mkt_list_overview"]
    }
  ],
  "proxies": [
    {
      "name": "string",
      "rule": "string（可复述的公开规则）",
      "reading": "string",
      "source_tools": ["string"]
    }
  ],
  "inventory_rhythm": {
    "summary": "string",
    "source_tools": ["struct_get_warehouse"]
  },
  "policy_shocks": [
    {
      "date": "YYYY-MM-DD",
      "title": "string",
      "affects_stage": "string",
      "source_kind": "news|report|article"
    }
  ],
  "data_gaps": ["string"],
  "notes": ["string"]
}
```

- `nodes` 至少覆盖目录中的代表品种。  
- `proxies` 1–4 条；规则字段必须能在 `proxy-rules.md` 找到对应类型。  
- `policy_shocks` 目标 2–5 条；不足写入 `data_gaps`。
