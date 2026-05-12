# 如何让自己的博客支持 RSS

很多人搭好了博客，写了几篇文章，却忽略了一个基础功能：RSS。

RSS（Really Simple Syndication）是一种标准化的内容订阅协议。读者通过 RSS 阅读器订阅你的博客后，每次你发布新文章，阅读器会自动拉取更新——不需要读者主动访问你的网站，不需要你去社交媒体上吆喝。

在算法推荐主导信息分发的时代，RSS 反而成了一种稀缺能力：让读者以自己的方式、按自己的节奏消费内容。对创作者来说，RSS 订阅者通常是最忠实的读者群体，因为他们是主动选择关注你的。

这篇文章从 RSS 的原理讲起，手把手教你给博客加上 RSS 支持。无论你用的是静态站点生成器还是自己写的博客系统，都能找到对应的方案。

# RSS 的工作原理

RSS 的核心是一个 XML 文件。你把这个文件托管在博客的某个固定 URL 上（通常是 `/feed.xml` 或 `/rss.xml`），RSS 阅读器定期请求这个地址，解析 XML 内容，就能知道你发了什么新文章。

一个最简的 RSS 文件长这样：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>我的博客</title>
    <link>https://example.com</link>
    <description>关于技术和思考的个人博客</description>
    <language>zh-CN</language>
    <lastBuildDate>Sat, 10 May 2026 08:00:00 +0800</lastBuildDate>

    <item>
      <title>第一篇文章</title>
      <link>https://example.com/posts/first</link>
      <description>这是文章的摘要或全文内容。</description>
      <pubDate>Sat, 10 May 2026 08:00:00 +0800</pubDate>
      <guid>https://example.com/posts/first</guid>
    </item>

  </channel>
</rss>
```

结构非常清晰：`<channel>` 描述博客本身的信息，每个 `<item>` 对应一篇文章。读者的 RSS 阅读器拿到这个文件后，会根据 `<guid>` 判断哪些文章是新的，然后展示给用户。

## RSS 2.0 vs Atom

目前主流的订阅格式有两种：RSS 2.0 和 Atom。两者功能几乎相同，主要区别在于 Atom 的规范更严格、对内容类型的支持更好。大多数 RSS 阅读器同时兼容两种格式，选哪个都可以。本文以 RSS 2.0 为例，因为它的结构更直观。

## 关键字段说明

`<channel>` 层级：

| 字段 | 是否必须 | 说明 |
|------|---------|------|
| `title` | 是 | 博客名称 |
| `link` | 是 | 博客首页 URL |
| `description` | 是 | 博客的一句话介绍 |
| `language` | 否 | 内容语言，如 `zh-CN` |
| `lastBuildDate` | 否 | Feed 最后更新时间 |
| `atom:link` | 推荐 | Feed 自身的 URL（自引用） |

`<item>` 层级：

| 字段 | 是否必须 | 说明 |
|------|---------|------|
| `title` | 是 | 文章标题 |
| `link` | 是 | 文章 URL |
| `description` | 是 | 文章摘要或全文 HTML |
| `pubDate` | 推荐 | 发布时间，RFC 822 格式 |
| `guid` | 推荐 | 全局唯一标识，通常用文章 URL |
| `category` | 否 | 文章分类标签 |

# 各类博客的 RSS 实现方案

## Hugo

Hugo 原生支持 RSS，默认就会在构建时生成 Feed。你要做的只是确认配置正确。

在 `hugo.toml`（或 `config.toml`）中添加：

```toml
[outputs]
  home = ["HTML", "RSS"]

[params]
  description = "关于技术和思考的个人博客"
  author = "你的名字"
```

Hugo 会自动在 `/index.xml` 生成 RSS Feed。如果你想自定义 Feed 的路径和内容，可以创建模板文件 `layouts/_default/rss.xml`：

```xml
{{- printf "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>" | safeHTML }}
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{{ .Site.Title }}</title>
    <link>{{ .Site.BaseURL }}</link>
    <description>{{ .Site.Params.description }}</description>
    <language>{{ .Site.LanguageCode }}</language>
    <lastBuildDate>{{ now.Format "Mon, 02 Jan 2006 15:04:05 -0700" }}</lastBuildDate>
    <atom:link href="{{ .Permalink }}" rel="self" type="application/rss+xml" />
    {{- range first 20 .Site.RegularPages }}
    <item>
      <title>{{ .Title }}</title>
      <link>{{ .Permalink }}</link>
      <description>{{ .Summary | html }}</description>
      <pubDate>{{ .Date.Format "Mon, 02 Jan 2006 15:04:05 -0700" }}</pubDate>
      <guid>{{ .Permalink }}</guid>
    </item>
    {{- end }}
  </channel>
</rss>
```

## Hexo

Hexo 需要安装插件。在项目目录下执行：

```bash
npm install hexo-generator-feed --save
```

然后在 `_config.yml` 中添加配置：

```yaml
feed:
  enable: true
  type: rss2
  path: feed.xml
  limit: 20
  content: true       # 是否在 Feed 中包含文章全文
  content_limit: 300   # 摘要截取字数（content 为 false 时生效）
```

运行 `hexo generate` 后，Feed 会自动生成在 `/feed.xml`。

## Next.js

Next.js 没有内置的 RSS 支持，需要自己生成。推荐在构建阶段用脚本生成静态 XML 文件。

安装依赖：

```bash
npm install rss
```

创建生成脚本 `scripts/generate-rss.mjs`：

```javascript
import { writeFileSync } from 'fs';
import RSS from 'rss';
import { getAllPosts } from '../lib/posts.mjs';

const feed = new RSS({
  title: '我的博客',
  site_url: 'https://example.com',
  feed_url: 'https://example.com/feed.xml',
  language: 'zh-CN',
});

const posts = getAllPosts();

posts.forEach((post) => {
  feed.item({
    title: post.title,
    url: `https://example.com/posts/${post.slug}`,
    description: post.summary,
    date: new Date(post.date),
  });
});

writeFileSync('./public/feed.xml', feed.xml({ indent: true }));
console.log('RSS feed generated.');
```

在 `package.json` 中把这个脚本加到构建流程里：

```json
{
  "scripts": {
    "build": "node scripts/generate-rss.mjs && next build"
  }
}
```

如果你用的是 App Router，也可以通过 Route Handler 动态生成：

```typescript
// app/feed.xml/route.ts
import { getAllPosts } from '@/lib/posts';

export async function GET() {
  const posts = getAllPosts();

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>我的博客</title>
    <link>https://example.com</link>
    <description>关于技术和思考的个人博客</description>
    <language>zh-CN</language>
    ${posts
      .map(
        (post) => `
    <item>
      <title>${escapeXml(post.title)}</title>
      <link>https://example.com/posts/${post.slug}</link>
      <description>${escapeXml(post.summary)}</description>
      <pubDate>${new Date(post.date).toUTCString()}</pubDate>
      <guid>https://example.com/posts/${post.slug}</guid>
    </item>`
      )
      .join('')}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600',
    },
  });
}

function escapeXml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
```

## Jekyll

Jekyll 和 Hugo 类似，生态中有成熟的插件。在 `Gemfile` 中添加：

```ruby
gem "jekyll-feed"
```

在 `_config.yml` 中启用：

```yaml
plugins:
  - jekyll-feed

title: 我的博客
description: 关于技术和思考的个人博客
url: https://example.com
```

构建后会自动在 `/feed.xml` 生成 RSS Feed。GitHub Pages 默认支持这个插件，不需要额外配置。

## 纯手写博客

如果你的博客是纯手写的 HTML 页面，没有用任何框架，可以写一个简单的脚本在每次发布时重新生成 `feed.xml`。

用 Python 实现：

```python
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import format_datetime

def generate_feed(posts, output_path='feed.xml'):
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')

    ET.SubElement(channel, 'title').text = '我的博客'
    ET.SubElement(channel, 'link').text = 'https://example.com'
    ET.SubElement(channel, 'description').text = '关于技术和思考的个人博客'
    ET.SubElement(channel, 'language').text = 'zh-CN'

    for post in posts:
        item = ET.SubElement(channel, 'item')
        ET.SubElement(item, 'title').text = post['title']
        ET.SubElement(item, 'link').text = post['url']
        ET.SubElement(item, 'description').text = post['summary']
        ET.SubElement(item, 'pubDate').text = format_datetime(post['date'])
        ET.SubElement(item, 'guid').text = post['url']

    tree = ET.ElementTree(rss)
    ET.indent(tree, space='  ')
    tree.write(output_path, encoding='unicode', xml_declaration=True)


posts = [
    {
        'title': '第一篇文章',
        'url': 'https://example.com/posts/first',
        'summary': '这篇文章讲了什么',
        'date': datetime(2026, 5, 10, 8, 0, 0),
    },
]

generate_feed(posts)
```

把这个脚本加到你的发布流程中，每次写完新文章时运行一次即可。

# 让 RSS Feed 被发现

生成了 Feed 文件还不够，你需要告诉浏览器和爬虫"这个网站有 RSS"。

在 HTML 的 `<head>` 中添加一行：

```html
<link rel="alternate" type="application/rss+xml"
      title="我的博客" href="/feed.xml" />
```

这行标签的作用是：当用户使用支持 RSS 自动发现的浏览器插件（如 Feedbro、RSSHub Radar）访问你的网站时，插件能自动检测到 Feed 地址并提示订阅。

另外，在网站的页脚或导航栏放一个 RSS 图标链接也很有必要。很多读者习惯通过视觉提示来判断一个网站是否支持 RSS。

# 全文输出还是摘要输出

生成 RSS Feed 时需要做一个决定：`<description>` 里放文章全文还是只放摘要？

**全文输出**的好处是读者体验好——打开阅读器就能读完，不用跳转到你的网站。这对读者来说是最方便的。缺点是 Feed 文件体积会比较大，而且你无法统计文章的实际阅读量。

**摘要输出**的好处是读者必须点击链接才能阅读全文，你可以通过网站统计工具掌握真实的访问数据。缺点是多了一步跳转，部分读者会因为嫌麻烦而跳过。

实际的选择取决于你的优先级。如果你更看重读者体验和传播效率，选全文；如果你需要精确的流量数据或者网站本身有广告等商业化需求，选摘要。

一种折中方案是输出前 300-500 字的内容作为"丰富摘要"，既给了足够的信息让读者判断是否值得阅读，又保留了引导点击的动机。

# 验证和调试

Feed 写完后，用以下工具验证格式是否正确：

- **W3C Feed Validation Service**（`validator.w3.org/feed/`）——输入你的 Feed URL，它会检查 XML 格式和字段是否符合规范，并给出详细的错误提示。
- **直接在浏览器中打开 Feed URL**——大多数浏览器会以原始 XML 的形式展示内容，检查一下结构是否完整、中文是否乱码。

几个常见的问题：

**日期格式错误。** RSS 2.0 的 `<pubDate>` 要求使用 RFC 822 格式，如 `Sat, 10 May 2026 08:00:00 +0800`。ISO 8601 格式（`2026-05-10T08:00:00+08:00`）在 RSS 2.0 中是无效的，但在 Atom 格式中是标准写法。

**XML 特殊字符未转义。** 文章标题或摘要中如果包含 `&`、`<`、`>` 等字符，必须转义为 `&amp;`、`&lt;`、`&gt;`，否则整个 XML 会解析失败。最安全的做法是用 `<![CDATA[...]]>` 包裹内容：

```xml
<description><![CDATA[
  <p>这篇文章讲了 A & B 的关系，以及为什么 X < Y。</p>
]]></description>
```

**编码声明缺失。** XML 文件的第一行应该声明编码方式：`<?xml version="1.0" encoding="UTF-8"?>`。中文内容必须确保文件实际保存为 UTF-8 编码。

# 进阶：自动化与持续集成

如果你的博客部署在 Vercel、Netlify 或 GitHub Pages 上，Feed 的生成可以完全自动化。

以 GitHub Pages + GitHub Actions 为例，你可以在 `.github/workflows/deploy.yml` 中添加 Feed 生成步骤：

```yaml
- name: Generate RSS Feed
  run: python scripts/generate_feed.py

- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./public
```

每次推送新文章到仓库，CI 会自动重新生成 Feed 并部署。你只需要专注于写作本身。

# 最后

给博客加上 RSS 是一件投入产出比很高的事情。实现成本低——多数情况下就是一个 XML 文件加几行配置，维护成本也低——生成流程可以完全自动化。但它给读者提供了一种干净、稳定、不被算法干扰的内容获取方式。

如果你正在经营个人博客，RSS 值得作为一个基础设施来对待，而不只是一个可有可无的附加功能。
