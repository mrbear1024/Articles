# GitHub 高频功能实用指南——从日常使用到高效协作

上一篇文章介绍了 Git 的核心概念和基本操作。这篇文章聚焦 GitHub 本身，系统梳理你在日常工作中会反复用到的功能。

GitHub 的功能非常多，但真正高频使用的大概只有十几个。这篇文章只讲这些高频功能，每一个都给出具体的操作路径和使用场景，目标是让你打开 GitHub 时知道每个按钮是干什么的。

## 仓库（Repository）管理

### 创建仓库

点击页面右上角的"+"号，选择"New repository"。

![image-20260506134449870](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/image-20260506134449870.png)

你需要做几个决定：

**仓库名称**——建议用小写字母加连字符，比如 `my-blog`、`data-analysis-tools`。这个名称会出现在 URL 中，清晰简洁比花哨重要。

**Public 还是 Private**——Public 仓库任何人都能看到代码，Private 仓库只有你和你授权的人能看到。个人项目如果没有保密需求，建议选 Public，方便日后当作品展示。

**初始化选项**——创建时可以勾选三个初始文件：

- **README.md**——项目说明书，建议勾选。GitHub 会在仓库首页自动渲染这个文件的内容。
- **.gitignore**——选择你使用的编程语言（如 Python、Node、Java），GitHub 会自动生成对应的忽略规则。
- **LICENSE**——开源协议。如果你打算让别人使用你的代码，需要选一个。MIT License 是最宽松也最常用的选择。

### 仓库设置

进入仓库后，点击顶部的"Settings"标签页，几个常用的设置：

**默认分支**——在 Settings → Branches 中可以修改默认分支名称。GitHub 目前默认使用 `main`。

**分支保护规则**——可以设置规则，比如"合并到 main 分支前必须通过 Pull Request""PR 必须至少有一个人审批"。团队协作时这个功能能有效防止意外。

**Collaborators**——在 Settings → Collaborators 中可以邀请其他人加入仓库。被邀请的人可以直接推送代码，不需要通过 Fork 和 PR 的流程。

**Danger Zone**——页面底部有一个红色区域，包含"修改仓库可见性""转移仓库""删除仓库"等操作。这些操作不可逆或影响较大，谨慎使用。

## 代码浏览与搜索

### 在线浏览代码

GitHub 提供了一个完整的在线代码浏览器。以 facebook/react 仓库为例，这是一个典型的仓库首页：

![仓库首页——以 React 为例，展示了文件列表、分支、Star 数、贡献者等核心信息](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/repo-page.png)

在仓库的"Code"标签页中：

- 点击任何文件可以查看内容，Markdown 文件会自动渲染
- 点击行号可以高亮某一行，URL 会自动更新——你可以把这个 URL 发给别人，对方打开后会直接跳到那一行
- 按住 Shift 再点击另一行，可以高亮一个范围
- 点击文件右上角的"Raw"按钮可以获取文件的原始内容

**快捷键 `.`**——在任何仓库页面按下键盘上的 `.` 键，GitHub 会在浏览器中打开一个 VS Code 编辑器（github.dev），你可以直接在线编辑代码并提交。这个功能在你只需要做小修改时特别方便，不需要把项目克隆到本地。

### 代码搜索

GitHub 的代码搜索功能非常强大。在页面顶部的搜索栏中：

- 搜索当前仓库内的代码：在仓库页面直接搜索
- 搜索全 GitHub 的代码：在 github.com/search 中搜索

搜索支持多种过滤条件：

| 语法 | 作用 | 示例 |
|------|------|------|
| `language:` | 按编程语言过滤 | `language:python` |
| `path:` | 按文件路径过滤 | `path:src/` |
| `extension:` | 按文件扩展名过滤 | `extension:yml` |
| `repo:` | 指定仓库 | `repo:facebook/react` |
| `org:` | 指定组织 | `org:google` |

### Blame 和 History

**Blame**——在查看文件时点击"Blame"按钮，可以看到每一行代码是谁在什么时候写的、属于哪个提交。

![Blame 视图——每一行代码旁边标注了提交者、时间和提交信息](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/blame.png)

当你想知道"这行代码为什么是这样写的"时，Blame 是最直接的工具。

**History**——点击"History"按钮可以看到这个文件的所有修改历史，每次修改的具体内容都一目了然。

## Issue：任务与问题管理

Issue 是 GitHub 上最通用的协作单元。它的用途远不止"报告 Bug"，很多团队把 Issue 当作轻量级的项目管理工具来使用。

### 创建 Issue

![Issues 列表页面——展示了 Issue 标题、标签、创建者和时间](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/issues-page.png)

在仓库的"Issues"标签页点击"New Issue"，填写标题和内容即可。内容支持 Markdown 格式，你可以插入代码块、图片、表格、任务列表等。

一个好的 Issue 应该包含：
- 清晰的标题（概括问题或需求）
- 具体的描述（如果是 Bug，说明复现步骤、预期行为、实际行为）
- 相关的上下文（截图、日志、环境信息）

### Issue 的组织工具

**Labels（标签）**——给 Issue 分类。常见的标签包括 `bug`、`enhancement`、`documentation`、`help wanted`、`good first issue` 等。你也可以创建自定义标签。GitHub 默认提供了一组标签，颜色和名称都可以修改。

**Milestones（里程碑）**——把一组 Issue 归入同一个目标。比如你可以创建一个"v2.0 发布"的里程碑，把所有需要在 v2.0 完成的 Issue 关联进去。里程碑会自动显示完成百分比。

**Assignees（负责人）**——把 Issue 指派给具体的人。一个 Issue 可以有多个负责人。

**关联 PR**——在 Issue 或 PR 的描述中写 `#123`（Issue 编号），GitHub 会自动创建关联。在 PR 描述中写 `Closes #123` 或 `Fixes #123`，PR 合并后会自动关闭对应的 Issue。

### Issue Templates

在仓库中创建 `.github/ISSUE_TEMPLATE/` 目录，放入模板文件，用户创建 Issue 时可以选择模板。常见的模板类型：

- Bug Report（Bug 报告）
- Feature Request（功能建议）
- Question（问题咨询）

模板可以预填标签、负责人等信息，确保 Issue 的格式统一、信息完整。

## Pull Request：代码审查的核心

PR 是 GitHub 上代码从开发到合并的标准流程。它的核心价值在于：代码在合并前必须经过审查，避免了"直接往主分支提交"的风险。

### 创建 PR

![Pull Request 列表页面](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/pull-requests.png)

推送你的分支到 GitHub 后，页面上通常会出现一个黄色横幅，提示你创建 PR。点击"Compare & pull request"按钮即可。

你也可以在"Pull requests"标签页点击"New pull request"，手动选择 base 分支（合并到哪里）和 compare 分支（从哪里合并）。

![PR 详情页——包含标题、描述、标签、审查者、关联 Issue 等信息](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/pr-detail.png)

PR 的描述应该回答两个问题：
- 做了什么改动
- 为什么要做这个改动

### 代码审查（Code Review）

PR 创建后，团队成员可以审查代码：

- **Files changed**——查看所有文件的变更，绿色是新增，红色是删除
- **行内评论**——在具体的代码行旁边点击"+"号，可以留下评论。这是最精确的反馈方式——直接指向你想讨论的那行代码
- **Suggestion**——评论时可以点击"±"按钮，直接给出修改建议。PR 作者可以一键接受这个建议，代码会自动修改并生成提交
- **审查意见**——评论完成后，点击"Review changes"提交审查，有三个选项：
  - **Comment**——只是留言，不表态
  - **Approve**——批准，认为代码可以合并
  - **Request changes**——要求修改，认为代码需要调整后才能合并

### 合并策略

PR 审查通过后，点击"Merge"按钮合并。GitHub 提供三种合并方式：

**Merge commit**——创建一个合并提交，保留分支上的所有提交历史。适合需要完整历史记录的场景。

**Squash and merge**——把分支上的所有提交压缩成一个提交后合并。适合分支上有很多细碎提交（如"修复拼写错误""调整缩进"）的情况，让主分支的历史更干净。

**Rebase and merge**——把分支上的提交逐个应用到主分支上，不产生合并提交。保持线性历史。

团队通常会在仓库设置中统一合并策略，避免混用。

### Draft PR

如果你的代码还在开发中，还没准备好接受审查，可以创建 Draft PR。Draft PR 不能被合并，但团队成员可以看到你的进度和方向，提前给出反馈。准备好后点击"Ready for review"即可转为正式 PR。

## GitHub Actions：自动化工作流

GitHub Actions 是 GitHub 内置的 CI/CD（持续集成/持续部署）工具。它可以在特定事件发生时自动执行一系列任务。

### 基本概念

**Workflow（工作流）**——一个自动化流程，定义在 `.github/workflows/` 目录下的 YAML 文件中。

**Event（触发事件）**——什么时候运行这个工作流。常见的事件包括：
- `push`——代码被推送时
- `pull_request`——PR 被创建或更新时
- `schedule`——定时运行（cron 表达式）
- `workflow_dispatch`——手动触发

**Job（任务）**——工作流中的一组步骤，运行在一个虚拟机上。

**Step（步骤）**——任务中的每一个操作，可以是运行命令或使用别人发布的 Action。

### 常见用途

**自动运行测试**——每次提交代码时自动跑测试，确保新代码没有破坏现有功能。

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm install
      - run: npm test
```

**自动部署**——代码合并到主分支后自动部署到服务器或云平台。

**自动发布**——创建 Release 时自动构建并上传产物（如编译后的二进制文件）。

**代码质量检查**——自动运行 Lint 工具检查代码风格，运行类型检查等。

### 查看运行结果

![Actions 页面——展示工作流列表和运行状态](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/actions-page.png)

在仓库的"Actions"标签页可以看到所有工作流的运行历史。每次运行会显示成功（绿色对勾）或失败（红色叉号），点击进去可以看到每个步骤的详细日志。

PR 页面也会显示 Actions 的运行状态。如果测试失败，PR 会显示红色标记，提醒你修复问题后再合并。

## GitHub Pages：免费建站

GitHub Pages 可以把仓库中的静态文件（HTML、CSS、JavaScript）发布为一个网站。

### 开启方式

进入仓库 Settings → Pages，选择发布源：

- **从分支发布**——选择一个分支（通常是 `main`）和目录（`/` 根目录或 `/docs`），GitHub 会自动把该目录下的文件发布为网站
- **从 GitHub Actions 发布**——通过工作流构建网站内容后发布，适合需要构建步骤的项目（如 Jekyll、Hugo 等静态网站生成器）

发布后，网站地址是 `https://你的用户名.github.io/仓库名/`。

### 常见用途

- 个人博客
- 项目文档网站
- 作品集展示
- 简历页面

如果仓库名是 `你的用户名.github.io`，则网站地址是 `https://你的用户名.github.io/`——这是你的 GitHub 个人站点。

## Releases：版本发布

当你的项目达到一个稳定的节点时，可以创建一个 Release 来标记这个版本。

![Releases 页面——以 Node.js 为例，展示版本号、发布日期和变更说明](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/releases.png)

### 创建 Release

在仓库右侧的"Releases"区域点击"Create a new release"：

1. **选择或创建 Tag**——通常使用语义化版本号，如 `v1.0.0`、`v2.1.3`
2. **填写标题和说明**——描述这个版本有哪些新功能、修复了哪些问题
3. **上传附件**——可以附带编译后的二进制文件、压缩包等
4. **标记为 Pre-release**——如果是测试版本，勾选此项

### 自动生成 Release Notes

点击"Generate release notes"按钮，GitHub 会自动根据上一个 Release 到当前 Tag 之间的 PR 和提交记录，生成一份变更说明。省去手动整理的工作。

## Notifications：通知管理

GitHub 的通知系统默认会发送大量邮件和站内通知，不加管理会很快变成噪音。

### 通知级别

**Watch（关注）**——你可以选择关注一个仓库的不同级别：
- **Participating and @mentions**——只在你被 @提到或参与讨论时通知（推荐）
- **All Activity**——仓库的所有活动都通知（只对你密切关注的核心项目开启）
- **Ignore**——完全忽略

### 过滤和管理

在 github.com/notifications 页面可以管理所有通知。几个实用技巧：

- 用 `reason:` 过滤通知来源（如 `reason:mention`、`reason:review-requested`）
- 已处理的通知点击"Done"归档，保持收件箱清洁
- 在 Settings → Notifications 中可以细粒度地控制哪些事件触发邮件通知

## GitHub CLI（gh 命令行工具）

GitHub 提供了官方的命令行工具 `gh`，可以在终端中直接操作 GitHub，不需要打开浏览器。

### 安装

```bash
# macOS
brew install gh

# Windows
winget install GitHub.cli

# Linux
sudo apt install gh
```

安装后执行 `gh auth login` 完成认证。

### 高频命令

```bash
# 创建仓库
gh repo create my-project --public

# 克隆仓库
gh repo clone owner/repo

# 创建 PR
gh pr create --title "添加搜索功能" --body "实现了关键词搜索"

# 查看 PR 列表
gh pr list

# 审查并合并 PR
gh pr review 42 --approve
gh pr merge 42

# 创建 Issue
gh issue create --title "首页加载缓慢" --label "bug"

# 查看 Issue 列表
gh issue list --label "bug"

# 查看 Actions 运行状态
gh run list
gh run view 12345

# 创建 Release
gh release create v1.0.0 --title "v1.0.0" --notes "首个正式版本"
```

`gh` 命令的优势在于效率。创建 PR、查看 Issue、触发工作流等操作都可以在终端中一行命令完成，不需要在浏览器和终端之间反复切换。

## Projects：项目管理看板

GitHub Projects 是一个内置的项目管理工具，类似 Trello 或 Jira 的看板。

### 创建和使用

在你的个人主页或组织主页的"Projects"标签页创建新项目。GitHub 提供了两种视图：

**Board（看板）**——卡片在不同列之间移动，适合"待办 → 进行中 → 已完成"这样的流程管理。

**Table（表格）**——类似电子表格，可以添加自定义字段（如优先级、截止日期、负责人），适合需要多维度管理的场景。

### 与 Issue 和 PR 联动

Project 中的每一个条目都可以关联到 Issue 或 PR。当 Issue 被关闭或 PR 被合并时，对应的卡片状态会自动更新。这让项目管理和代码开发自然地联系在一起。

## 个人主页（Profile）的经营

GitHub 主页是你的技术名片。以下几个功能可以帮你建立专业形象：

**Profile README**——创建一个和你用户名同名的仓库（比如你的用户名是 `zhangsan`，就创建 `zhangsan` 仓库），在其中放一个 `README.md`，这个文件的内容会显示在你的个人主页上。你可以用它来展示自我介绍、技术栈、当前项目等。

**Pinned Repositories**——你可以把最多 6 个仓库"置顶"到主页上。选择你最有代表性的项目，而非最近活跃的。

**贡献图（Contribution Graph）**——主页下方的绿色格子图展示了你过去一年的提交活动。它能直观地体现你的活跃程度，但不要为了填格子而刷无意义的提交。

## 安全相关功能

### SSH 密钥

在 Settings → SSH and GPG keys 中管理你的 SSH 密钥。配置 SSH 后，与 GitHub 的通信不再需要每次输入密码。

```bash
# 生成密钥
ssh-keygen -t ed25519 -C "你的邮箱"

# 查看公钥并复制到 GitHub
cat ~/.ssh/id_ed25519.pub
```

### Personal Access Token（PAT）

如果你使用 HTTPS 方式访问仓库，或者需要在脚本中调用 GitHub API，需要使用 PAT 代替密码。在 Settings → Developer settings → Personal access tokens 中生成。

建议使用 Fine-grained tokens，它可以限制 Token 只能访问特定仓库和特定权限，比传统的 Classic tokens 更安全。

### Dependabot

GitHub 会自动扫描你仓库中的依赖（如 npm 包、pip 包），如果发现已知的安全漏洞，会自动创建 PR 来更新有问题的依赖版本。这个功能默认开启，不需要额外配置。

## 发现与探索优秀项目

GitHub 上托管着数以亿计的开源项目，找到高质量的项目并从中学习，本身就是一种重要的能力。GitHub 提供了多种机制帮你发现值得关注的项目。

### Explore 页面

访问 github.com/explore，这是 GitHub 官方的内容推荐入口，分为几个板块：

**Trending（趋势）**——按日、周、月维度展示最近获得 Star 最多的项目，可以按编程语言过滤。这里是发现新兴项目最直接的渠道。比如一个新的 AI 框架刚发布，通常会在 Trending 上停留数天。访问路径：github.com/trending。

![GitHub Trending 页面——按 Star 增长速度排列的热门项目](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/trending.png)

**Collections（精选集）**——GitHub 编辑团队整理的主题合集，比如"Learn to Code""Machine Learning""Game Engines"等。每个合集收录了该领域最具代表性的项目，适合系统性地了解一个技术方向。

![Collections 页面——官方精选的主题合集](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/collections.png)

**Topics（主题标签）**——每个仓库可以打上主题标签（如 `machine-learning`、`react`、`cli`），在 github.com/topics 页面可以按主题浏览项目。点进任何一个主题，项目会按 Star 数排列，质量普遍较高。

![Topics 页面——按主题浏览项目](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/topics.png)

### 评估一个项目的质量

打开一个陌生仓库，如何快速判断它是否值得投入时间？可以关注以下几个指标：

**Star 数**——社区认可度的粗略指标。但 Star 数高不代表质量一定好，有些项目靠营销获得 Star，有些高质量的小众工具 Star 数不高。它是参考指标，不是决定性指标。

**最近提交时间**——在仓库首页可以看到最后一次提交的时间。如果一个项目半年以上没有任何提交，且有大量未关闭的 Issue，大概率已经停止维护。

**Issue 和 PR 的处理情况**——打开的 Issue 数量和关闭速度反映了维护者的活跃程度。一个健康的项目通常有稳定的 Issue 关闭率，PR 的平均合并时间也不会太长。

**贡献者数量**——在仓库的 Insights → Contributors 页面可以看到所有贡献者的提交活动。只有一个人维护的项目存在"单点风险"，多人参与的项目通常更可持续。

![Contributors 页面——展示每个贡献者的提交频率和趋势](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/contributors.png)

**README 的质量**——好项目的 README 通常结构清晰，包含安装方法、使用示例、文档链接。如果 README 写得潦草，项目的整体质量可能也不会太好。

**License**——没有开源协议的项目在法律上不允许你使用其代码。MIT、Apache 2.0、BSD 是最宽松的协议。

### 关注与订阅

**Star（收藏）**——给项目加 Star 相当于收藏，可以在你的 Stars 页面（github.com/你的用户名?tab=stars）找到所有收藏过的项目。Star 也是对项目维护者的一种认可和鼓励。

**Watch（订阅）**——Watch 一个项目后会收到它的活动通知。建议大多数项目只设置为"Participating and @mentions"级别，只有核心关注的项目才设置为"All Activity"，否则通知会淹没你的收件箱。

**Star Lists（收藏夹）**——你可以创建多个 Star List 来分类管理收藏。比如创建"前端工具""AI 项目""学习资料"等列表，避免所有 Star 混在一起。在给项目加 Star 时，点击 Star 按钮旁边的下拉箭头就可以选择加入哪个列表。

### 通过代码搜索发现项目

当你遇到一个技术问题，想看看别人是怎么解决的，GitHub 的代码搜索就变成了一个学习工具：

```
# 搜索使用了特定 API 的代码示例
language:python "openai.ChatCompletion.create"

# 搜索特定配置的写法
filename:docker-compose.yml redis

# 搜索某个库的实际用法
language:javascript "import { useQuery }" path:src/
```

![image-20260506134254855](https://article-images.xlearnity.ai/site/AI技术/git-slide/github-guide/image-20260506134254855.png)

这种方式能让你看到真实项目中的代码写法，比看文档更直观。

### 值得关注的几类仓库

**Awesome Lists**——GitHub 上有大量以"awesome-"开头的仓库（如 `awesome-python`、`awesome-react`），它们是社区维护的资源清单，汇总了某个领域的工具、库、教程、文章等。搜索 `awesome-你感兴趣的领域` 通常都能找到对应的列表。

**官方示例仓库**——很多技术团队会在 GitHub 上维护官方的示例项目，比如 `vercel/examples`、`google/generative-ai-docs`。这些仓库包含经过验证的最佳实践，是学习新技术的优质起点。

**个人 dotfiles**——很多知名开发者会在 GitHub 上公开自己的 dotfiles（配置文件），包含 shell 配置、编辑器配置、Git 配置等。搜索 `dotfiles` 可以找到大量优秀的配置方案，从中借鉴适合自己的设置。

## 实用小技巧

**键盘快捷键**——在任何 GitHub 页面按 `?` 键可以查看所有可用的快捷键。几个常用的：
- `t`——在仓库中快速搜索文件名
- `.`——打开 github.dev 在线编辑器
- `s` 或 `/`——聚焦搜索栏
- `g` + `i`——跳转到 Issues 页面
- `g` + `p`——跳转到 Pull requests 页面

**URL 技巧**——
- 在任何仓库 URL 后加 `/compare/main...分支名` 可以直接查看分支差异
- 在文件 URL 中把 `github.com` 改成 `raw.githubusercontent.com` 可以获取文件的原始内容
- 在 commit URL 后加 `.diff` 或 `.patch` 可以获取对应格式的补丁文件

**Markdown 增强**——GitHub 的 Markdown 支持一些额外的语法：
- 任务列表：`- [ ] 待办事项` / `- [x] 已完成事项`
- 表情符号：`:+1:` 会渲染为 👍
- 引用回复：复制文字后按 `r` 键可以自动引用
- 折叠内容：使用 `<details>` 标签可以创建可折叠的内容区域

**GitHub Mobile**——GitHub 有官方的移动端 App（iOS 和 Android），可以在手机上审查 PR、管理 Issue、查看通知。适合在移动场景下快速响应团队协作。

## 总结

这篇文章覆盖了 GitHub 日常使用中最高频的功能。按照使用频率排序，最值得优先掌握的是：

1. **仓库管理和代码浏览**——这是每天都会用到的基础操作
2. **Issue 和 PR**——团队协作的核心工具
3. **GitHub Actions**——自动化可以节省大量重复性工作
4. **GitHub CLI**——提高操作效率

其他功能（Pages、Releases、Projects 等）按需学习即可。GitHub 的功能还在持续迭代，但核心的协作模式——Issue 追踪问题、Branch 隔离开发、PR 审查代码、Actions 自动化流程——在可预见的未来都不会改变。掌握这套流程，比记住每个按钮的位置更重要。
