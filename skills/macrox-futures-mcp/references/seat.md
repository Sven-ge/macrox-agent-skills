# 席位工具

调用前读本文件。席位数据多为 **T+1**：问「今天」可能无数据，请用上一交易日。  
龙虎榜 / 会员排名必须用 **`ticker`（合约）**，不能只用品种 `symbol`。合约不明时先 `ref_list_symbols`。

---

## `seat_get_broker_position_chg` · 机构增减仓排行

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `trade_date` | string | **是** | — | `YYYY-MM-DD` |
| `direction` | string | 否 | `increase` | `increase` 增仓 \| `decrease` 减仓 |
| `top_limit` | int | 否 | `5` | 1–20 |

```javascript
await call("seat_get_broker_position_chg", { trade_date: "2026-08-25", direction: "increase", top_limit: 5 });
await call("seat_get_broker_position_chg", { trade_date: "2026-08-25", direction: "decrease" });
```

---

## `seat_get_contract_position_chg` · 合约增减仓排行

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `trade_date` | string | **是** | — | `YYYY-MM-DD` |
| `direction` | string | 否 | `increase` | `increase` \| `decrease` |
| `top_limit` | int | 否 | `5` | 1–20 |

```python
call("seat_get_contract_position_chg", {"trade_date": "2026-08-25", "direction": "increase", "top_limit": 10})
```

---

## `seat_get_profit_loss` · 席位盈亏分布

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `trade_date` | string | **是** | — | `YYYY-MM-DD` |

```python
call("seat_get_profit_loss", {"trade_date": "2026-08-25"})
```

---

## `seat_get_long_short_board` · 合约龙虎榜

**用途**：多头持仓 / 空头持仓 / 净多持仓三块榜单。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `trade_date` | string | **是** | — | `YYYY-MM-DD`；当日可能无数据 |
| `ticker` | string | **是** | — | 合约代码，如 `cu2609`、`ih2612` |
| `top_limit` | int | 否 | `5` | 各榜条数 1–20 |

```javascript
await call("seat_get_long_short_board", {
  trade_date: "2026-06-22",
  ticker: "ih2612",
  top_limit: 5,
});
```

---

## `seat_get_member_ranks` · 会员持仓/成交排名

**用途**：期货公司会员多头/空头/净多排名（默认 Top 20）。席位多为 T+1。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `ticker` | string | **是** | — | 合约代码，如 `cu2610` |
| `rank_type` | string | 否 | `all` | `long` \| `short` \| `net` \| `all`（无独立 `volume` 接口） |
| `start_date` | string | 否 | 最近有数据开市日 | `YYYY-MM-DD`；空则自动取 ≤今天 的开市日并 T+1 回退 |
| `end_date` | string | 否 | 同 start | `YYYY-MM-DD` |

```python
# 只传 ticker 即可（未填日期时回退到近期有数据的开市日）
call("seat_get_member_ranks", {"ticker": "cu2610"})
call("seat_get_member_ranks", {"ticker": "cu2610", "rank_type": "long", "start_date": "2026-09-03", "end_date": "2026-09-03"})
```
