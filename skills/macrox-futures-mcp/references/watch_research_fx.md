# 盯盘 · 研报 · 外盘

调用前读本文件。

---

## `watch_get_ranks` · 盯盘异动

**用途**：异动事件流（突破、新高新低等）。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | 否 | `""` | 品种过滤 |
| `trade_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `indicator_code` | string | 否 | `""` | 指标代码过滤 |
| `page` | int | 否 | `1` | 页码 |
| `page_size` | int | 否 | `20` | 每页条数 |

```python
call("watch_get_ranks", {"page_size": 20})
call("watch_get_ranks", {"symbol": "CU", "page_size": 10})
```

---

## `research_list_reports` · 券商研报列表

**用途**：标题、机构、日期等元数据；**不含全文**。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `keyword` | string | 否 | `""` | 标题关键词 |
| `symbol` | string | 否 | `""` | 若未填 keyword，可用作检索词 |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `report_type` | string | 否 | `""` | 研报类型过滤 |
| `page` | int | 否 | `1` | 页码 |
| `page_size` | int | 否 | `10` | 每页条数 |

```python
call("research_list_reports", {"keyword": "铜", "page_size": 5})
call("research_list_reports", {"symbol": "RB", "start_date": "2026-08-01", "end_date": "2026-08-28"})
```

---

## `fx_list_symbols` · 外盘品种列表

无入参。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| （无） | — | — | — | 传空对象 `{}` |

```python
call("fx_list_symbols", {})
```

---

## `fx_get_daily_bars` · 外盘日线

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 外盘品种代码，如 `FEF`、`GC` |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |

```python
call("fx_get_daily_bars", {"symbol": "GC", "start_date": "2026-08-01", "end_date": "2026-09-03"})
```
