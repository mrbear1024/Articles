#!/usr/bin/env python3
"""
build.py - Articles 静态站点生成器
将所有 Markdown 文件渲染为 HTML，生成按时间降序的首页索引。

用法: python3 build.py
依赖: pip3 install markdown pygments
"""

import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
from urllib.parse import quote

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from pygments.formatters import HtmlFormatter

# ── Configuration ────────────────────────────────────────────────

ROOT = Path(__file__).parent.resolve()
OUT = ROOT / "_site"

SITE_TITLE = "Articles"
SITE_DESC = "个人文章合集"

EXCLUDE_DIRS = {
    ".git", ".obsidian", ".claude", ".gstack",
    "_site", "node_modules", "数据", "url-to-markdown",
}
EXCLUDE_FILES = {"CLAUDE.md", "README.md", "MEMORY.md"}

CATEGORY_DISPLAY = {
    "AI技术": "AI 技术",
    "创业与IP": "创业与IP",
    "个人成长": "个人成长",
    "OpenClaw": "OpenClaw",
    "视频笔记": "视频笔记",
    "文章": "文章",
    "Articles": "文章",
    "思考与反思": "思考与反思",
    "其他": "其他",
}


# ── Data ─────────────────────────────────────────────────────────

@dataclass
class Article:
    source: Path
    title: str
    category: str
    date: datetime
    description: str
    url: str


# ── Utilities ────────────────────────────────────────────────────

def get_git_dates() -> dict[str, datetime]:
    """批量获取所有文件最近一次提交的日期。"""
    result = subprocess.run(
        ["git", "log", "--format=COMMIT:%aI", "--name-only"],
        capture_output=True, text=True, cwd=ROOT,
    )
    dates: dict[str, datetime] = {}
    current = None
    for line in result.stdout.splitlines():
        if line.startswith("COMMIT:"):
            current = datetime.fromisoformat(line[7:])
        elif line.strip() and current:
            key = line.strip()
            if key not in dates:
                dates[key] = current
    return dates


def get_category(rel: Path) -> str:
    parts = rel.parts
    if len(parts) == 1:
        return "其他"
    top = parts[0]
    if top == "文章" and len(parts) > 2:
        return parts[1]
    return top


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def extract_title_desc(filepath: Path) -> tuple[str, str]:
    try:
        text = filepath.read_text("utf-8")
    except Exception:
        return filepath.stem, ""

    text = strip_frontmatter(text)

    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = m.group(1).strip() if m else filepath.stem
    title = re.sub(r"[*_`\[\]]", "", title)

    desc = ""
    for line in text.split("\n"):
        s = line.strip()
        if (
            s
            and not s.startswith("#")
            and not s.startswith("---")
            and not s.startswith("![")
            and not s.startswith("- [")
            and not s.startswith("|")
            and not s.startswith("```")
        ):
            desc = re.sub(r"[*_`\[\]\(\)]", "", s)[:160]
            break

    return title, desc


def render_md(text: str) -> str:
    text = strip_frontmatter(text)
    md = markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(css_class="highlight", guess_lang=False),
            TableExtension(),
            TocExtension(permalink=False),
            "sane_lists",
        ],
        output_format="html",
    )
    html = md.convert(text)
    html = re.sub(r'href="([^"]*?)\.md"', r'href="\1.html"', html)
    html = re.sub(r'href="([^"]*?)\.md#', r'href="\1.html#', html)
    return html


def strip_first_h1(html: str) -> str:
    return re.sub(r"<h1[^>]*>.*?</h1>", "", html, count=1, flags=re.DOTALL)


# ── CSS ──────────────────────────────────────────────────────────

def build_css() -> str:
    pygments_css = HtmlFormatter(style="monokai").get_style_defs(".highlight")
    return (
        CSS_CORE
        + "\n/* ── Pygments (monokai) ── */\n"
        + pygments_css
        + "\n.highlight pre { margin: 0; }\n"
    )


CSS_CORE = """\
:root {
    --bg: #fafaf9;
    --surface: #ffffff;
    --text: #1c1917;
    --text-2: #57534e;
    --text-3: #a8a29e;
    --border: #e7e5e4;
    --accent: #2563eb;
    --accent-h: #1d4ed8;
    --tag-bg: #eff6ff;
    --tag-text: #1d4ed8;
    --radius: 8px;
    --max-w: 860px;
}
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 "PingFang SC", "Noto Sans SC", "Microsoft YaHei", sans-serif;
    background: var(--bg); color: var(--text);
    line-height: 1.8; font-size: 16px;
    -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-h); }
.container { max-width: var(--max-w); margin: 0 auto; padding: 0 24px; }

/* ── Header ── */
.site-header {
    border-bottom: 1px solid var(--border);
    padding: 20px 0; background: var(--surface);
}
.site-header .container {
    display: flex; align-items: center; justify-content: space-between;
}
.site-title { font-size: 20px; font-weight: 700; letter-spacing: -0.02em; }
.site-title a { color: var(--text); }
.site-title a:hover { text-decoration: none; }
.site-desc { color: var(--text-3); font-size: 14px; }

/* ── Filters ── */
.filters { display: flex; flex-wrap: wrap; gap: 8px; margin: 32px 0 24px; }
.filter-btn {
    padding: 6px 16px; border: 1px solid var(--border); border-radius: 20px;
    background: var(--surface); color: var(--text-2); font-size: 14px;
    cursor: pointer; transition: all 0.15s;
}
.filter-btn:hover { border-color: var(--accent); color: var(--accent); }
.filter-btn.active {
    background: var(--accent); color: #fff; border-color: var(--accent);
}

/* ── Article List ── */
.stats { color: var(--text-3); font-size: 14px; margin-bottom: 16px; }
.article-list { list-style: none; }
.article-item {
    padding: 20px 0; border-bottom: 1px solid var(--border);
}
.article-item:first-child { padding-top: 0; }
.article-link { display: block; color: inherit; }
.article-link:hover { text-decoration: none; }
.article-link:hover .article-title { color: var(--accent); }
.article-meta {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 6px; font-size: 13px;
}
.article-category {
    display: inline-block; padding: 2px 10px;
    background: var(--tag-bg); color: var(--tag-text);
    border-radius: 4px; font-size: 12px; font-weight: 500;
}
.article-date { color: var(--text-3); }
.article-title {
    font-size: 18px; font-weight: 600; line-height: 1.4;
    margin-bottom: 4px; transition: color 0.15s;
}
.article-desc { color: var(--text-2); font-size: 14px; line-height: 1.6; }

/* ── Article Page ── */
.back-link {
    display: inline-flex; align-items: center; gap: 4px;
    color: var(--text-2); font-size: 14px; margin: 24px 0;
}
.back-link:hover { color: var(--accent); }
.article-header {
    margin-bottom: 40px; padding-bottom: 20px;
    border-bottom: 1px solid var(--border);
}
.article-header .article-meta { margin-bottom: 12px; }
.article-header h1 {
    font-size: 28px; font-weight: 700;
    line-height: 1.4; letter-spacing: -0.02em;
}

/* ── Article Content ── */
.article-content { font-size: 16px; line-height: 2; }
.article-content h1 { font-size: 26px; margin: 2em 0 0.8em; font-weight: 700; }
.article-content h2 {
    font-size: 22px; margin: 1.8em 0 0.6em; font-weight: 700;
    padding-bottom: 8px; border-bottom: 1px solid var(--border);
}
.article-content h3 { font-size: 18px; margin: 1.5em 0 0.5em; font-weight: 600; }
.article-content h4 { font-size: 16px; margin: 1.2em 0 0.4em; font-weight: 600; }
.article-content p { margin: 1em 0; }
.article-content ul, .article-content ol { margin: 1em 0; padding-left: 2em; }
.article-content li { margin: 0.3em 0; }
.article-content li > ul, .article-content li > ol { margin: 0.2em 0; }
.article-content blockquote {
    margin: 1.5em 0; padding: 12px 20px;
    border-left: 4px solid var(--accent); background: #f8fafc;
    color: var(--text-2);
}
.article-content blockquote p { margin: 0.5em 0; }
.article-content img {
    max-width: 100%; height: auto;
    border-radius: var(--radius); margin: 1em 0;
}
.article-content table {
    width: 100%; border-collapse: collapse;
    margin: 1.5em 0; font-size: 14px;
}
.article-content th, .article-content td {
    padding: 10px 14px; border: 1px solid var(--border); text-align: left;
}
.article-content th { background: #f9fafb; font-weight: 600; }
.article-content code {
    font-family: "SF Mono", "Fira Code", Consolas, monospace;
    font-size: 0.9em; background: #f1f5f9;
    padding: 2px 6px; border-radius: 4px;
}
.article-content pre {
    margin: 1.5em 0; padding: 16px 20px;
    background: #272822; color: #f8f8f2;
    border-radius: var(--radius); overflow-x: auto;
    font-size: 14px; line-height: 1.6;
}
.article-content pre code {
    background: none; padding: 0; color: inherit; font-size: inherit;
}
.article-content .highlight {
    margin: 1.5em 0; border-radius: var(--radius); overflow: hidden;
}
.article-content .highlight pre {
    margin: 0; border-radius: 0;
}
.article-content hr {
    border: none; border-top: 1px solid var(--border); margin: 2em 0;
}
.article-content a {
    text-decoration: underline; text-underline-offset: 3px;
}

/* ── Footer ── */
.site-footer {
    margin-top: 60px; padding: 24px 0;
    border-top: 1px solid var(--border);
    text-align: center; color: var(--text-3); font-size: 13px;
}

/* ── Responsive ── */
@media (max-width: 640px) {
    .container { padding: 0 16px; }
    .article-header h1 { font-size: 22px; }
    .article-content { font-size: 15px; }
    .article-title { font-size: 16px; }
    .filters { gap: 6px; }
    .filter-btn { padding: 4px 12px; font-size: 13px; }
}
"""


# ── HTML Templates ───────────────────────────────────────────────

def page_wrap(title: str, body: str, css_path: str = "style.css") -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{css_path}">
</head>
<body>
{body}
</body>
</html>"""


def build_index_html(articles: list[Article], categories: list[str]) -> str:
    btns = ['<button class="filter-btn active" data-cat="all">全部</button>']
    for c in categories:
        btns.append(
            f'<button class="filter-btn" data-cat="{escape(c)}">'
            f"{escape(CATEGORY_DISPLAY.get(c, c))}</button>"
        )

    items = []
    for a in articles:
        cat_display = escape(CATEGORY_DISPLAY.get(a.category, a.category))
        date_str = a.date.strftime("%Y-%m-%d")
        desc = (
            f'<div class="article-desc">{escape(a.description)}</div>'
            if a.description
            else ""
        )
        items.append(
            f'<li class="article-item" data-category="{escape(a.category)}">'
            f'<a class="article-link" href="{quote(a.url, safe="/")}">'
            f'<div class="article-meta">'
            f'<span class="article-category">{cat_display}</span>'
            f'<span class="article-date">{date_str}</span>'
            f"</div>"
            f'<div class="article-title">{escape(a.title)}</div>'
            f"{desc}"
            f"</a></li>"
        )

    body = f"""<header class="site-header">
<div class="container">
  <div>
    <div class="site-title">{SITE_TITLE}</div>
    <div class="site-desc">{SITE_DESC}</div>
  </div>
</div>
</header>
<main class="container">
<div class="filters">{"".join(btns)}</div>
<div class="stats">共 {len(articles)} 篇文章</div>
<ul class="article-list">{"".join(items)}</ul>
</main>
<footer class="site-footer"><div class="container">Built with Python &amp; Markdown</div></footer>
<script>
document.querySelectorAll('.filter-btn').forEach(function(btn){{
  btn.addEventListener('click',function(){{
    document.querySelectorAll('.filter-btn').forEach(function(b){{b.classList.remove('active')}});
    btn.classList.add('active');
    var cat=btn.dataset.cat;
    var count=0;
    document.querySelectorAll('.article-item').forEach(function(el){{
      var show=(cat==='all'||el.dataset.category===cat);
      el.style.display=show?'':'none';
      if(show) count++;
    }});
    document.querySelector('.stats').textContent='共 '+count+' 篇文章';
  }});
}});
</script>"""
    return page_wrap(SITE_TITLE, body)


def build_article_html(article: Article, content_html: str) -> str:
    cat_display = escape(CATEGORY_DISPLAY.get(article.category, article.category))
    date_str = article.date.strftime("%Y-%m-%d")
    depth = len(Path(article.url).parent.parts)
    css_path = ("../" * depth + "style.css") if depth else "style.css"
    root = ("../" * depth) if depth else ""

    body = f"""<header class="site-header">
<div class="container">
  <div class="site-title"><a href="{root}index.html">{SITE_TITLE}</a></div>
</div>
</header>
<main class="container">
<a class="back-link" href="{root}index.html">&larr; 返回首页</a>
<article>
  <div class="article-header">
    <div class="article-meta">
      <span class="article-category">{cat_display}</span>
      <span class="article-date">{date_str}</span>
    </div>
    <h1>{escape(article.title)}</h1>
  </div>
  <div class="article-content">{content_html}</div>
</article>
</main>
<footer class="site-footer"><div class="container">Built with Python &amp; Markdown</div></footer>"""
    return page_wrap(f"{article.title} - {SITE_TITLE}", body, css_path)


# ── Build ────────────────────────────────────────────────────────

def collect_articles(git_dates: dict[str, datetime]) -> list[Article]:
    articles = []
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT)
        parts = rel.parts
        if any(p in EXCLUDE_DIRS or p.startswith(".") for p in parts):
            continue
        if rel.name in EXCLUDE_FILES:
            continue

        category = get_category(rel)
        title, desc = extract_title_desc(md)
        date = git_dates.get(str(rel))
        if date is None:
            date = datetime.fromtimestamp(md.stat().st_mtime).astimezone()
        url = str(rel.with_suffix(".html"))

        articles.append(
            Article(
                source=rel,
                title=title,
                category=category,
                date=date,
                description=desc,
                url=url,
            )
        )

    articles.sort(key=lambda a: a.date, reverse=True)
    return articles


def copy_assets():
    """复制所有非 Markdown 静态文件到输出目录。"""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = Path(dirpath).relative_to(ROOT)
        parts = rel.parts if str(rel) != "." else ()

        # 跳过排除目录
        if any(p in EXCLUDE_DIRS or p.startswith(".") for p in parts):
            dirnames[:] = []
            continue
        # 不递归进入排除目录
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]

        for fname in filenames:
            if fname.startswith(".") or fname.endswith(".md"):
                continue
            # 跳过 build.py 自身
            if str(rel) == "." and fname == "build.py":
                continue
            src = Path(dirpath) / fname
            dst = OUT / rel / fname
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def build():
    print(f"Building site → {OUT}/")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    # CSS
    (OUT / "style.css").write_text(build_css(), encoding="utf-8")
    print("  ✓ style.css")

    # 静态资源
    copy_assets()
    print("  ✓ static assets")

    # Git 日期
    git_dates = get_git_dates()

    # 收集文章
    articles = collect_articles(git_dates)
    print(f"  ✓ found {len(articles)} articles")

    # 渲染每篇文章
    for art in articles:
        src = ROOT / art.source
        try:
            text = src.read_text("utf-8")
        except Exception as e:
            print(f"  ⚠ skip {art.source}: {e}")
            continue

        html_body = render_md(text)
        html_body = strip_first_h1(html_body)
        html_page = build_article_html(art, html_body)

        out_file = OUT / art.url
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(html_page, encoding="utf-8")

    # 首页
    cats = list(dict.fromkeys(a.category for a in articles))
    idx = build_index_html(articles, cats)
    (OUT / "index.html").write_text(idx, encoding="utf-8")
    print("  ✓ index.html")

    print(f"\nDone! {len(articles)} articles built.")
    print(f"Open: file://{OUT}/index.html")


if __name__ == "__main__":
    build()
