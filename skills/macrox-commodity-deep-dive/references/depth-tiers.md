# 分档 · macrox-commodity-deep-dive

用户未指定时 **问一次**，不要默认为 heavy。

| 档 | 信号 | 篇幅与硬停 | 最低取数 | 引擎章节 |
| --- | --- | --- | --- | --- |
| **light** | 短深度、简版、快速深挖 | 假设 1 条；确认可跳；HTML 约 4–6 节 | overview + daily_bars + basis + warehouse + 资讯 1 次 | 可不跑 `anl_*` |
| **medium** | 默认「做个深度」、研报体 | 假设 2–3 条；建议确认提纲 | light + term + position_ratio + sentiment；资讯 ≥2 | `anl_run_quant` 一章，`window_years` 2–3，`sections` 精简 |
| **heavy** | 完整深度、交叉验证、QA | 假设 3 条；**必须**提纲硬停 | medium + 席位（需 ticker）+ 对照至少两类结构 vs 价格 | quant 必做；可选 `anl_run_echo`（用户给了目标区间）或 `anl_run_rv`（明确对标品种） |

## 随档变化

- **页数**：light 单滚动页紧凑；medium 分章；heavy 分章 + QA 附录。  
- **图**：本 Skill 不强制画图；若环境能用返回序列做简单表即可，禁止虚构点位。  
- **硬停**：heavy 未确认提纲不得写终稿（除非用户明确跳过）。

## `anl_*` 使用边界

- 只当「分析引擎章节」：引用 `data`/`answer` 并写 `source_tool`。  
- 不得改服务端算法、不得把输出改写成未标注的「模型看多」。  
- 算法若需保密阈值 → 不属于本 Skill（第二类 MCP）。
