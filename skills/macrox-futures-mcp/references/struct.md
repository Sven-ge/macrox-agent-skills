# 结构工具（基差 / 期限 / 仓单 / 持仓比）

调用前读本文件。注意 `view` 决定必填字段是否变化。

---

## `struct_get_basis` · 现货与基差

**用途**：单品种基差序列，或全市场基差截面排名。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `view` | string | 否 | `time_series` | `time_series` 单品种序列；`market_snapshot` 全市场截面 |
| `symbol` | string | view=time_series 时**必填** | `""` | 品种代码；snapshot 时可作过滤 |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `window_days` | int | 否 | `30` | 未给起止日时回溯天数 |

**选用**

| 问法 | 参数 |
|------|------|
| 今日基差排名 | `{ "view": "market_snapshot" }` |
| 沪铜近 30 日基差 | `{ "symbol": "CU", "view": "time_series", "window_days": 30 }` |

```python
call("struct_get_basis", {"view": "market_snapshot"})
call("struct_get_basis", {"symbol": "CU", "view": "time_series", "window_days": 20})
```

---

## `struct_get_term` · 期限结构

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `view` | string | 否 | `single_symbol_curve` | `single_symbol_curve` 单品种远近月曲线；`market_overview` 全市场形态列表 |
| `symbol` | string | curve 时**必填** | `""` | 品种代码 |
| `trade_date` | string | 否 | `""` | 截面日 `YYYY-MM-DD` |
| `page` | int | 否 | `1` | 仅 `market_overview` |
| `page_size` | int | 否 | `20` | 仅 `market_overview` |

```python
call("struct_get_term", {"symbol": "CU", "view": "single_symbol_curve"})
call("struct_get_term", {"view": "market_overview", "page": 1, "page_size": 20})
```

---

## `struct_get_warehouse` · 仓单日报

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码 |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `window_days` | int | 否 | `30` | 回溯天数 |

```python
call("struct_get_warehouse", {"symbol": "CU", "window_days": 30})
```

---

## `struct_get_position_ratio` · 多空持仓比

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码 |
| `start_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `end_date` | string | 否 | `""` | `YYYY-MM-DD` |
| `window_days` | int | 否 | `30` | 回溯天数 |

```python
call("struct_get_position_ratio", {"symbol": "RB", "window_days": 30})
```
