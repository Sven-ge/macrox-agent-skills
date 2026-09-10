# 资讯与舆情工具

调用前读本文件。快讯 / 热榜 / 搜索 / 文章 / 舆情评分参数各不相同。

---

## `news_list_intel` · 快讯列表

**用途**：按时间窗、品种、重要程度筛选快讯。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `time_range` | string | 否 | `today` | `today` 当天；`session` 上一交易日 18:00 后；`range` 自定义 |
| `symbol` | string | 否 | `""` | 有值则查该品种相关快讯 |
| `min_importance` | int | 否 | `1` | 1–5；1=一般，5=重磅 |
| `asset_category` | string | 否 | `""` | 大类名，如 `有色金属`、`黑色系` |
| `category_id` | int | 否 | `0` | 分类 ID，0=不限 |
| `plate_id` | int | 否 | `0` | 板块 ID，0=不限 |
| `start_time` | string | `range` 时必填 | `""` | 自定义起点 |
| `end_time` | string | `range` 时必填 | `""` | 自定义终点 |
| `pre_day` | int | 否 | `2` | 按 `symbol` 查询时回溯天数 |
| `page` | int | 否 | `1` | 页码 |
| `page_size` | int | 否 | `12` | 每页条数 |

```python
call("news_list_intel", {"time_range": "today", "page_size": 10})
call("news_list_intel", {"symbol": "CU", "min_importance": 3, "pre_day": 3})
call("news_list_intel", {"time_range": "range", "start_time": "2026-08-20 00:00:00", "end_time": "2026-08-28 23:59:59"})
```

---

## `news_list_hot` · 热门快讯

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `limit` | int | 否 | `10` | 1–50 |
| `symbol` | string | 否 | `""` | 仅保留与该品种相关的条目 |

```javascript
await call("news_list_hot", { limit: 10 });
await call("news_list_hot", { symbol: "CU", limit: 15 });
```

---

## `news_search` · 关键词搜索快讯

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `keyword` | string | **是** | — | 搜索词，如 `铜`、`库存` |
| `limit` | int | 否 | `20` | 最多返回条数 |

```python
call("news_search", {"keyword": "库存", "limit": 20})
```

---

## `news_list_articles` · 研究文章列表

**用途**：标题、摘要、标签。**不含正文**；读全文用 `news_get_article`。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `keyword` | string | 否 | `""` | 标题关键词 |
| `tag` | string | 否 | `""` | 标签名，如 `化工`、`热门推荐` |
| `symbol` | string | 否 | `""` | 按品种相关过滤 |
| `time_range` | string | 否 | `today` | `today` \| `week` \| `range` |
| `start_date` | string | `range` 时必填 | `""` | `YYYY-MM-DD` |
| `end_date` | string | `range` 时必填 | `""` | `YYYY-MM-DD` |
| `page` | int | 否 | `1` | 页码 |
| `page_size` | int | 否 | `10` | 每页条数 |

```python
call("news_list_articles", {"tag": "化工", "time_range": "week", "page_size": 5})
call("news_list_articles", {"keyword": "铜", "time_range": "range", "start_date": "2026-08-01", "end_date": "2026-08-28"})
```

---

## `news_get_article` · 文章详情

**用途**：正文已转为 Markdown，可直接展示。

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `article_id` | string | **是** | — | 列表返回的 ID，如 `A61797` |

```python
# 先 list 取 id，再 get
lst = call("news_list_articles", {"time_range": "week", "page_size": 3})
aid = lst["data"]["items"][0]["article_id"]  # 字段名以实际 data 为准
call("news_get_article", {"article_id": aid})
```

---

## `factor_get_sentiment` · 品种舆情多空分

| 参数 | 类型 | 必填 | 默认 | 说明 |
|------|------|------|------|------|
| `symbol` | string | **是** | — | 品种代码，如 `CU` |
| `trade_date` | string | 否 | 今天 | 锚定日 `YYYY-MM-DD` |
| `window_days` | int | 否 | `0` | `>0` 时只返回最近 N 个点；`0`=全量 |

```python
call("factor_get_sentiment", {"symbol": "CU", "window_days": 7})
```
