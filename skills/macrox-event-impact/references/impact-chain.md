# 影响链路（公开规则）

事件 → 商品的传导只写 **可观察渠道**，每条链路必须能指到将要调用的工具。

## 渠道类型

| id | 渠道 | 代理 |
| --- | --- | --- |
| `price` | 近端价格 | `mkt_list_overview` / `mkt_get_daily_bars` |
| `basis` | 现货相对期货 | `struct_get_basis` |
| `term` | 近远月 | `struct_get_term` |
| `inventory` | 仓单/库存节奏 | `struct_get_warehouse` |
| `narrative` | 资讯主线 | `news_*` / `research_*` |

## 写法

每条：`事件事实 → 渠道 → 品种 symbol → 观察什么`。  
禁止：未取数就写「利多铜」；禁止仓位建议、止盈止损。

## 冲击窗

- 事件日 `T` 用资讯日期或用户给定。  
- 默认窗口：`T` 前后各 5 个 **开市日**（`cal_list_days`）。  
- 窗口内描述高低与方向，用 bars 的 `data`，不编造百分比。
