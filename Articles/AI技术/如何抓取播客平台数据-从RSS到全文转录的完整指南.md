# 如何抓取播客平台数据：从 RSS 到全文转录的完整指南

播客是一座被低估的内容富矿。主流媒体的选题往往滞后，真正有价值的行业观点、深度访谈、一线实践常常先在播客里流通。把播客数据结构化地抓下来，配合全文转录与检索，能做的事远比"听完一期节目"多：追踪某档节目的选题脉络、做细分领域的趋势分析、给 AI 助手喂行业语料、建一个带搜索的私人知识库。

本文从最实用的角度出发，讲清楚抓取播客数据的三条主流路径，并给出一条可以直接跑通的完整流水线：从查找 RSS 地址、解析节目元数据、下载音频，到用 Whisper 做本地转录。

## 播客数据的三条抓取路径

不同的平台有不同的数据形态，选对路径能省掉大量试错成本。

**第一条路径：RSS Feed。** 这是绝对的首选。几乎所有播客在底层都是 RSS：Apple Podcasts、Spotify、小宇宙只是 RSS 的分发渠道，它们从同一个 feed 抓数据再在自己的客户端里展示。抓 RSS 的好处在于合法、稳定、字段标准化，拿到的是主播自己发布的权威元数据。局限是只有节目本身的信息，没有评论、播放量、订阅数这类平台侧数据。

**第二条路径：官方或第三方 API。** Spotify 有 Web API，能查节目元数据但不给音频流，需要 OAuth；Apple 的 iTunes Search API 免费无 key，特别适合批量查 feed URL 和基础元数据；Listen Notes 聚合了全球播客，付费但省力；Podcast Index 开源且免费，覆盖面已经相当广。做分析类项目，第三方聚合 API 通常比自己一个个平台抓更高效。

**第三条路径：网页爬虫与移动端抓包。** 主要针对小宇宙、喜马拉雅这类没有开放 RSS 或 API 的国内平台。小宇宙的 Web 端有 GraphQL 接口，用 Charles 或 mitmproxy 能看到请求结构，但有签名和设备指纹；喜马拉雅的移动端接口反爬较重，批量抓取容易触发风控。这条路径属于灰色地带，个人研究、低频、不商用、不绕付费墙时风险相对可控，商业项目建议走合作或直接采购数据。

## 为什么 RSS 是首选

从数据完整度看，RSS 提供的字段已经覆盖了绝大多数分析需求：播客名、主播、封面、节目标题、发布时间、时长、描述、音频直链、章节标记。对于做内容分析的场景，这些已经够用。

从工程成本看，解析 RSS 在 Python 里用 `feedparser` 一行代码就能拿到结构化数据，不用写任何爬虫规则、不用维护反爬策略、不用担心平台改版。

从合规角度看，RSS 本身就是为机器读取设计的，主播公开发布 feed 的那一刻就默认允许抓取。这意味着可以长期稳定地做这件事，而不必担心某天突然被封。

## 找到 RSS 地址

播客平台的页面上通常不会直接显示 RSS URL，需要借助工具反查。三种常用方法：

**通过 iTunes Search API。** 这是最快的方法，免费且不需要 API key：

```bash
curl "https://itunes.apple.com/search?term=硅谷101&entity=podcast&country=cn&limit=3"
```

返回的 JSON 里 `feedUrl` 字段就是 RSS 地址。例如搜索"硅谷101"能拿到 `https://feeds.fireside.fm/sv101/rss`。

**通过 Podcast Index。** 打开 podcastindex.org，搜节目名，点进详情页能看到完整的 RSS URL，同时还有订阅数、评分等附加信息。

**通过 Apple Podcast 链接反查。** 如果已经有 Apple 的播客页面链接（形如 `podcasts.apple.com/cn/podcast/id1438706620`），把 ID 丢给 iTunes Lookup 接口：

```bash
curl "https://itunes.apple.com/lookup?id=1438706620"
```

拿到 `feedUrl` 字段即可。

## 解析 RSS 拿到节目列表

Python 的 `feedparser` 库是处理 RSS 最省事的选择。先安装：

```bash
pip install feedparser
```

然后几行代码就能拿到整档播客的所有节目信息：

```python
import feedparser

feed = feedparser.parse("https://feeds.fireside.fm/sv101/rss")

print(feed.feed.title)         # 播客名
print(feed.feed.description)   # 简介
print(len(feed.entries))       # 节目数

for ep in feed.entries:
    print(ep.title)                       # 标题
    print(ep.published)                   # 发布时间
    print(ep.summary)                     # 描述
    print(ep.enclosures[0].href)          # 音频 MP3 直链
    print(ep.itunes_duration)             # 时长
```

`feedparser` 会自动处理 RSS、Atom、各种编码和时区差异，开发者直接拿到标准化的 Python 对象。国内播客的 summary 字段里常有 HTML 标签，清洗时用 `BeautifulSoup` 即可。

## 完整流水线：从抓列表到全文转录

下面是一段可以直接运行的完整脚本，把整个流程串起来：抓取 RSS、写入 SQLite、下载最新一期音频、用 Whisper 转录成文字。

先安装依赖：

```bash
pip install feedparser requests openai-whisper
```

保存为 `podcast_pipeline.py`：

```python
import sqlite3
import feedparser
import requests
from pathlib import Path

FEED_URL = "https://feeds.fireside.fm/sv101/rss"
DB_PATH = "podcasts.db"
AUDIO_DIR = Path("audio")
AUDIO_DIR.mkdir(exist_ok=True)


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS episodes (
            id TEXT PRIMARY KEY,
            podcast TEXT,
            title TEXT,
            published TEXT,
            audio_url TEXT,
            summary TEXT,
            duration TEXT,
            local_path TEXT,
            transcript TEXT
        )
    """)
    conn.commit()
    return conn


def fetch_feed(conn, feed_url):
    feed = feedparser.parse(feed_url)
    podcast_name = feed.feed.title
    print(f"播客：{podcast_name}，共 {len(feed.entries)} 期")

    for ep in feed.entries:
        audio_url = ep.enclosures[0].href if ep.enclosures else None
        conn.execute(
            "INSERT OR IGNORE INTO episodes "
            "(id, podcast, title, published, audio_url, summary, duration) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                ep.id,
                podcast_name,
                ep.title,
                ep.published,
                audio_url,
                ep.get("summary", ""),
                ep.get("itunes_duration", ""),
            ),
        )
    conn.commit()


def download_one(conn, episode_id):
    row = conn.execute(
        "SELECT title, audio_url, local_path FROM episodes WHERE id = ?",
        (episode_id,),
    ).fetchone()
    title, audio_url, local_path = row
    if local_path and Path(local_path).exists():
        return local_path

    safe_name = "".join(c for c in title if c.isalnum() or c in " -_")[:60]
    path = AUDIO_DIR / f"{safe_name}.mp3"
    print(f"下载：{title}")
    with requests.get(audio_url, stream=True) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 128):
                f.write(chunk)
    conn.execute(
        "UPDATE episodes SET local_path = ? WHERE id = ?", (str(path), episode_id)
    )
    conn.commit()
    return str(path)


def transcribe(conn, episode_id, model_size="base"):
    import whisper

    row = conn.execute(
        "SELECT local_path, transcript FROM episodes WHERE id = ?", (episode_id,)
    ).fetchone()
    local_path, existing = row
    if existing:
        return existing

    print(f"加载 Whisper 模型：{model_size}")
    model = whisper.load_model(model_size)
    print("转录中（一小时节目约需 10 到 20 分钟）")
    result = model.transcribe(local_path, language="zh")
    text = result["text"]

    conn.execute(
        "UPDATE episodes SET transcript = ? WHERE id = ?", (text, episode_id)
    )
    conn.commit()
    return text


if __name__ == "__main__":
    conn = init_db()
    fetch_feed(conn, FEED_URL)

    latest = conn.execute(
        "SELECT id, title FROM episodes ORDER BY published DESC LIMIT 1"
    ).fetchone()
    ep_id, ep_title = latest
    print(f"\n最新一期：{ep_title}")

    download_one(conn, ep_id)
    text = transcribe(conn, ep_id, model_size="base")
    print(f"\n转录前 500 字：\n{text[:500]}")
```

脚本跑完会得到三样东西：一个 `podcasts.db` 文件存储整档播客所有节目的元数据；一个 `audio/` 目录放下载的音频；数据库里的 `transcript` 字段保存完整的转录文本。

## 几个工程细节

**增量更新策略。** 维护一张 feed URL 列表，写个定时任务每天跑一次 `fetch_feed`，`INSERT OR IGNORE` 会自动去重，新增节目自动入库。如果要追踪节目的编辑历史（描述修改、标题调整），把 `INSERT OR IGNORE` 改成 `INSERT OR REPLACE`，并加一张 `episode_history` 表记录每次变化。

**Whisper 模型的选择。** 从小到大依次是 `tiny`、`base`、`small`、`medium`、`large`。中文建议至少用 `small`，`base` 识别专业术语时错误率偏高。M 系列 Mac 跑 `medium` 压力不大，一小时的音频大约需要 15 到 25 分钟。若本地算力不够，换 OpenAI 的 API 版 Whisper，按分钟计费，调用方式极简：

```python
from openai import OpenAI
client = OpenAI()
with open("audio.mp3", "rb") as f:
    result = client.audio.transcriptions.create(
        model="whisper-1", file=f, language="zh"
    )
print(result.text)
```

**大文件下载的坑。** 用 `requests.get(url, stream=True)` 配合 `iter_content` 流式写入，避免一次性读进内存。一小时的高码率 MP3 动辄上百 MB，不流式处理容易把内存撑爆。

**国内播客的 RSS 问题。** 小宇宙不提供公开 RSS，部分喜马拉雅节目的 RSS 被藏得较深。这种情况下先去 Podcast Index 搜一下，很多节目其实同步分发到了其他平台，能拿到替代的 feed。实在没有的话，就只能走抓包路线，技术门槛和维护成本都会高一截。

## 合规与风险边界

抓取行为本身并不违法，但有几条边界需要清楚：

抓 RSS 是完全合规的，主播公开发布 feed 就默认允许被抓取与二次分发元数据，但音频文件的版权归主播所有，批量下载后公开重新分发是明确的侵权。

抓取国内平台私有 API 属于灰色地带，个人学习研究用途、控制频率、不商用、不公开分发，风险相对可控。商业项目涉及规模化抓取时，务必先看目标平台的 robots.txt 与用户协议，必要时走官方合作或第三方数据采购。

转录出来的文本用于个人检索、知识库、AI 训练（自用），没有问题；用于公开发布、商业化产品，需要取得主播授权，或者只保留摘要与分析结论，不直接呈现逐字稿。

## 结语

做数据抓取最容易陷入的误区是一上来就想着写复杂爬虫，真正优雅的做法是先检查有没有现成的标准通道。播客领域的标准通道就是 RSS，它的存在让这件事的工程复杂度从"和反爬策略斗智斗勇"降到"解析一个 XML"。在此之上叠加 Whisper 做全文转录，一个个人可用的播客知识库就成型了。

下一步可以思考的方向：给数据库加全文索引（SQLite 的 FTS5 扩展足够用），或者把转录文本喂给向量数据库做语义检索；订阅一批自己关心的播客，每周自动生成一份"本周金句"或"趋势摘要"；再进一步，把播客内容与博客、Twitter、Newsletter 的数据打通，构建一个跨媒介的个人内容索引。
