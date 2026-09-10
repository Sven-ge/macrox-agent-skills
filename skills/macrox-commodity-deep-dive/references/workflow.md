# 工作流 · macrox-commodity-deep-dive

## 步骤 1：收参与分档

`symbol` 大写；不确定用 `ref_list_symbols`。档位见 `depth-tiers.md`。

## 步骤 2：假设（可证伪）

每条假设写：陈述 + 观察代理 + 打脸条件。  
heavy（及建议 medium）列出提纲后硬停确认。

## 步骤 3：取数（仅 MacroX）

按档执行 `mcp-tools.md`。先价格与结构，再资讯，最后 `anl_*`（耗时，放后面）。

交叉验证（heavy 必做，medium 建议）：

| 对照 | 做法 |
| --- | --- |
| 价格 vs 基差/期限 | 是否同向 |
| 价格 vs 仓单 | 是否背离 |
| 叙事 vs 快讯 | 催化剂是否支撑假设 |
| 席位 vs 结构 | 有 ticker 才做 |

冲突必须写进 `tensions`，禁止抹平。

## 步骤 4：QA

- [ ] 每条假设有证据或「未取到」  
- [ ] 数字有工具名  
- [ ] `anl_*` 已标注且未改写为自有模型  
- [ ] 无目标价  
- [ ] 档位与章节数量匹配  

## 步骤 5：填 schema → HTML
