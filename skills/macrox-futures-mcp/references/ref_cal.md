# 基础与日历工具

调用前读本文件，按参数表填参：`call(tool_name, params)`。

通用约定：`symbol` 大写品种码；`ticker` 具体合约；日期 `YYYY-MM-DD`。

---

## `ref_list_symbols` · 品种目录 / 解析合约

**用途**：搜索品种；需要合约列表或席位可用合约时打开 `include_contracts`。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `keyword` | string | 否 | `""` | 中文名/代码模糊搜索 |
| `query` | string | 否 | `""` | 与 `keyword` 等价，可二选一 |
| `exchange` | string | 否 | `""` | 交易所过滤 |
| `include_contracts` | bool | 否 | `false` | `true` 时返回合约列表 |
| `purpose` | string | 否 | `general` | `general` \| `quote`（行情）\| `seat`（仅保留当日可查席位的合约） |
| `trade_date` | string | 否 | 最近开市日 | 解析合约用的交易日 |

**何时传参**

- 只搜品种名：`keyword` 或 `query`
- 要合约列表：`include_contracts=true`
- 为龙虎榜找可查席位合约：`purpose=seat` + `trade_date`

```javascript
await call("ref_list_symbols", { query: "CU", include_contracts: true });
await call("ref_list_symbols", { keyword: "螺纹" });
await call("ref_list_symbols", { query: "CU", purpose: "seat", trade_date: "2026-08-25", include_contracts: true });
```

---

## `ref_get_contract` · 合约规则

**用途**：交易单位、涨跌停、保证金、交易时段等静态规则。  
**不做**：历史 K 线（用 `mkt_get_daily_bars`）、现价（用 `mkt_list_overview`）。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码，如 `CU` |
| `ticker` | string | 否 | `""` | 合约代码（可选） |

```python
call("ref_get_contract", {"symbol": "CU"})
```

---

## `cal_list_days` · 交易日历

**用途**：区间内交易日与市场事件。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `start_date` | string | **是** | — | `YYYY-MM-DD` |
| `end_date` | string | **是** | — | `YYYY-MM-DD` |

```python
call("cal_list_days", {"start_date": "2026-08-01", "end_date": "2026-08-31"})
```
