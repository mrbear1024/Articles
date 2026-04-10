# Pretext 项目深度分析 — 推特线程

> 基于 chenglou 的推特线程和 GitHub 仓库分析

---

## 推特线程（发布用）

### 1/9

Cheng Lou（react-motion 作者、前 React 核心贡献者、现 Midjourney 工程师）刚开源了一个可能改变前端格局的库：Pretext

一句话：纯 TypeScript 实现多行文本高度计算，完全绕过 DOM reflow。

这解决了一个困扰前端开发者 30 年的性能瓶颈。

🔗 github.com/chenglou/pretext

### 2/9

为什么这很重要？

浏览器每次需要知道文本高度时，都要触发 layout reflow —— getBoundingClientRect() 就是罪魁祸首。

当 500 个文本块交替读写 DOM 时，Chrome 要 43ms，Safari 高达 149ms。

而 Pretext 的 layout() 只需 0.09ms。快了 500 倍。

### 3/9

核心设计：两阶段分离

**Phase 1 — prepare(text, font)**
- 用 Intl.Segmenter 分词（支持 CJK 逐字断行、泰语、阿拉伯语等）
- 通过 Canvas measureText() 测量每个分段宽度
- 一次性开销：500 段文本约 19ms

**Phase 2 — layout(prepared, maxWidth, lineHeight)**
- 纯算术运算，遍历缓存的宽度值
- 零 DOM 读取、零 Canvas 调用
- 500 段文本仅 0.09ms

### 4/9

这开启了过去不可能的 UI 范式：

- 🔲 虚拟化数十万个不同高度的文本框，120fps 滚动
- 💬 自适应收缩的聊天气泡
- 📰 响应式多栏杂志排版
- 🎨 可变字体 ASCII 艺术
- 📝 自增长文本域、手风琴组件

演示：chenglou.me/pretext/

### 5/9

最令人印象深刻的是多语言支持：

- CJK：支持禁则处理（行首行尾规则）
- 阿拉伯语/乌尔都语：RTL + Nastaliq 排版
- 泰语/高棉语/缅甸语：复杂文字分段
- Emoji：自动修正 Chrome/Firefox 的 Canvas emoji 测量偏差
- 双向文本：LTR/RTL 混排

跨浏览器精度：Chrome/Safari/Firefox 均为 7680/7680（100%）

### 6/9

Chenglou 原话："Text layout & measurement was the last & biggest bottleneck for unlocking much more interesting UIs, especially in the age of AI."

他的愿景是：80% 的 CSS 规范可以被取代——如果用户空间对文本有更好的控制。这不是在造轮子，而是在把能力从浏览器规范推向用户空间。

### 7/9

开发过程也值得一提：

Chenglou 用 Claude Code 和 Codex 作为核心开发工具，将浏览器实际渲染结果作为 ground truth，让 AI 在每个关键容器宽度下反复测量和迭代，持续数周。

这是 AI 辅助开发的一个标杆案例——不是让 AI 写代码然后人工 review，而是让 AI 成为测试和验证的引擎。

### 8/9

项目数据一览：

- ⭐ 11,496 stars（发布仅数天）
- 📦 npm install @chenglou/pretext（v0.0.3）
- 📄 MIT 协议
- 🗂️ 核心代码仅 8 个文件
- 🌍 测试语料覆盖 12+ 种语言（包括《了不起的盖茨比》全文）

局限：目前仅支持 white-space: normal/pre-wrap，不支持 SSR，版本仍为早期。

### 9/9

我的判断：

Pretext 不是一个「又一个前端库」。它代表的是一种思路转变——把浏览器最昂贵的操作（文本布局）从黑盒中解放出来，交给纯算术。

对于做聊天 UI、Canvas 渲染、虚拟滚动列表、编辑器工具的开发者，这可能是今年最值得关注的前端项目。

Cheng Lou 用 AI 写了一个让未来 UI 变得更快的工具。这就是我理想中 AI 辅助编程的样子。

---

## 附：Chenglou 原始推特线程翻译

**推文 1：**
> 亲爱的前端开发者们（以及所有对界面未来感兴趣的人）：我在地狱深处爬行了许久，为你们带来一个在未来数年内，堪称 UI 工程最重要的基础设施之一：纯 TypeScript 实现的快速、准确、全面的用户空间文本测量算法，可用于在不依赖 CSS 的情况下布局整个网页，完全绕过 DOM 测量和 reflow。

**推文 2：**
> 文本布局和测量是解锁更有趣 UI 的最后也是最大的瓶颈，尤其在 AI 时代。解决了这个问题，我们不再需要在 GL 炫酷落地页和实用博客文章之间做选择。

**推文 3：**
> 1. 数十万个不同高度文本框的遮挡剔除（虚拟化），无需 DOM 测量，将可见性检查简化为高度的单次线性遍历，120fps 滚动和 resize

**推文 4：**
> 2. 自适应收缩的聊天气泡

**推文 5：**
> 3. 多栏杂志布局——但是响应式和动态的

**推文 6：**
> 4. 可变字宽 ASCII 艺术，因为现在这很容易做到

**推文 7：**
> 5. 自增长文本域、手风琴、多行文本居中、纯 Canvas 多行文本——所有曾经是 CSS 难题的东西，现在变成了无聊的脚注

**推文 8：**
> 引擎很小（几 KB），了解浏览器怪癖，支持你需要的所有语言，包括韩文混合 RTL 阿拉伯文和平台特定 emoji。这是通过让 Claude Code 和 Codex 以浏览器 ground truth 为基准，在每个关键容器宽度下反复测量和迭代实现的，持续了数周。

**推文 9：**
> 这种范式比通过 getBoundingClientRect() 布局文本再杂乱地爬出测量结果要快约 500 倍。过去，这种测量还必须批处理，这破坏了 UI 组件边界的编程模型。最大的性能提升来自架构转变！

**推文 10：**
> 项目在 npm/bun install @chenglou/pretext，把你的 AI 丢进去做酷炫的 demo 吧！

**推文 11：**
> 有趣的 demo 列表。有些有用，有些纯粹炫技：chenglou.me/pretext/
