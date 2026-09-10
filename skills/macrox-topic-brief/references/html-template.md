# HTML 模板约定 · macrox-topic-brief

输出 **单个** HTML5 文件，自包含 CSS。

## 结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{hero.title} · MacroX Topic Brief</title>
  <style>/* 见下方样式要点 */</style>
</head>
<body>
  <header class="cover">
    <p class="eyebrow">MACROX TOPIC BRIEF</p>
    <h1>{hero.title}</h1>
    <p class="dek">{hero.dek}</p>
    <p class="meta">{period_start} — {period_end} · 生成 {generated_at}</p>
    <!-- author 非空时 -->
  </header>

  <section class="hero-bullets">
    <ul>…{hero.bullets}…</ul>
  </section>

  <article class="focus">
    <h2>{focus_story.headline}</h2>
    <div class="kpis">…key_numbers 卡片…</div>
    <div class="body">…summary…</div>
    <p class="sources">来源：…</p>
  </article>

  <!-- 每个 section -->
  <section class="rail">
    <h2>{section.title}</h2>
    <div class="item">…</div>
  </section>

  <section class="footnotes">
    <h2>行情脚注</h2>
    …
  </section>

  <footer>数据来源：MacroX MCP · 本简报由 Agent 按 macrox-topic-brief 生成，不构成投资建议。</footer>
</body>
</html>
```

## 样式要点（须落实）

- 背景近白 `#f7f8fa`，正文深灰；**禁止**默认紫渐变、玻璃拟态。  
- 页眉一条金色强调线 `#C9A227`（MacroX 点缀），eyebrow 小字追踪。  
- KPI 用简单边框卡片，非大阴影。  
- 正文字号约 15–16px，行高 1.6；栏目标题清晰层级。  
- 最大宽约 820px，居中。

## 交付

- 文件名：`macrox-topic-brief-{slug}-{period_end}.html`  
- 向用户给出文件路径，并简述栏目结构；不要再贴一整份重复 Markdown 长文（可给 3 条导读）。
