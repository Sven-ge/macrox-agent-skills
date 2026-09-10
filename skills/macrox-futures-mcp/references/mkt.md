# 行情工具

调用前读本文件。**现价/涨跌用 overview；历史走势用日 K；日内分时用分钟 K。**

---

## `mkt_list_overview` · 最新行情 / 涨跌幅榜

**用途**：单品种或多品种现价、涨跌、成交；或全市场涨跌幅排行。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `mode` | string | 否 | `symbols` | `symbols` 指定品种；`movers` 涨跌幅榜 |
| `symbols` | string | mode=symbols 时建议填 | `""` | 逗号分隔，如 `CU` 或 `CU,RB,AU` |
| `keyword` | string | 否 | `""` | 按中文名/代码筛品种 |
| `ticker` | string | 否 | `""` | 指定合约，如 `cu2610` |
| `sort_by` | string | 否 | `change_pct` | `change_pct` \| `volume` \| `amount` \| `last` \| `open_interest` |
| `limit` | int | 否 | `30` | 最多 80 |
| `include` | string | 否 | `""` | 字段组：空=默认；或 `行情数据` / `技术指标` / `突破信号` / `全部`；英文 `market,technicals,breakout,all` |

**选用**

| 问法 | 参数 |
|------|------|
| 沪铜现在多少钱 | `{ "symbols": "CU" }` |
| 涨幅榜前 20 | `{ "mode": "movers", "limit": 20 }` |
| 铜带技术指标 | `{ "symbols": "CU", "include": "行情数据,技术指标" }` |

```javascript
await call("mkt_list_overview", { symbols: "CU", limit: 1 });
await call("mkt_list_overview", { mode: "movers", sort_by: "change_pct", limit: 20 });
await call("mkt_list_overview", { symbols: "CU,RB", include: "market,technicals" });
```

---

## `mkt_get_daily_bars` · 日线 / 周线 / 月线

**用途**：OHLCV、持仓；可重采样周/月。仅传 `symbol` 时取主力。涨跌幅为百分点。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码 |
| `ticker` | string | 否 | `""` | 指定合约 |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD`；与 end 成对 |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `window_days` | int | 否 | `30` | 未给起止日时的回溯交易日数 |
| `grain` | string | 否 | `day` | `day` \| `week` \| `month` |
| `derive` | string | 否 | `""` | 可选 `trend,range_stats` |

**时间范围二选一**：`start_date`+`end_date`，或只设 `window_days`。

```python
call("mkt_get_daily_bars", {"symbol": "CU", "window_days": 30})
call("mkt_get_daily_bars", {"symbol": "CU", "start_date": "2026-01-01", "end_date": "2026-08-28"})
call("mkt_get_daily_bars", {"symbol": "RB", "grain": "week", "window_days": 120})
```

---

## `mkt_get_minute_bars` · 分钟 K 线

**用途**：完整分钟序列。**不要**用来查「现在多少钱」（请用 `mkt_list_overview`）。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `ticker` | string | 推荐 | `""` | 合约代码，如 `cu2610` |
| `symbol` | string | ticker 空时填 | `""` | 品种；会解析主力 |
| `trade_date` | string | 否 | 当日 | 单日 `YYYY-MM-DD` |
| `start_date` | string | 否 | `""` | 区间起点 |
| `end_date` | string | 否 | `""` | 区间终点 |
| `interval` | int | 否 | `1` | `1` \| `5` \| `15` \| `30` \| `60`（分钟） |

```javascript
await call("mkt_get_minute_bars", { ticker: "cu2610", trade_date: "2026-08-25", interval: 5 });
await call("mkt_get_minute_bars", { symbol: "CU", interval: 15 });
```
