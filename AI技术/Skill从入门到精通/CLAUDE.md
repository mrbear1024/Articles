# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 这是什么

这是《Skill 从入门到精通：Claude Code 技能系统完全指南》的源文件目录——一本由 13 章组成的中文长篇教程，从 Skill 概念入门一路讲到生态、变现与未来。父级仓库 (`/Users/wanghe/workspace/Articles/`) 是更大的内容仓库，本目录只承载这一套教程。

## 文件组织约定

章节按 `NN-标题.md` 编号，`00-目录.md` 是整本教程的导航入口与章节简介，新增/重命名章节时**必须同步更新它**。同一章可能存在多种衍生产物，文件名后缀有明确含义：

- `NN-标题.md` — Markdown 源文件，唯一的"事实来源"
- `NN-标题.pdf` — 导出的 PDF 版本
- `NN-标题-公众号.html` — 经 doocs-md 排版后用于微信公众号的内联 CSS HTML
- `NN-标题-slides.html` — 幻灯片版本（如 `02-安装和使用-slides.html`）
- `NN-文章结构图.html` / `.png` — 章节逻辑结构图（HTML 用 `article-structure-diagram` skill 生成，再截图为 PNG 嵌入 Markdown）

修改正文时只动 `.md`，HTML/PDF 是衍生物，需重新生成而非手动改。

## 已知不一致

`00-目录.md` 中第三章链接指向 `03-开发自己的Skill.md`，但实际文件是 `03-沉淀与开发自己的Skill.md`。如果用户让你改第三章，认准实际文件名；顺手修目录里的链接是合理的小修。

## 内部交叉引用

章节之间通过相对路径互相引用（如 `[第二章](02-安装和使用.md)`），章内锚点用 GitHub 风格的 `#中文标题`。改章节标题或文件名前先 grep 全目录，避免断链。

## 衍生产物的工作流

- 公众号 HTML：`/wechat-article` 或 `wechat-article` skill —— 走 R2 图床上传 → doocs-md 排版 → 生成封面 → 推送草稿箱
- PDF：通常由用户在编辑器或浏览器打印生成，不要主动覆盖
- 结构图：`article-structure-diagram` skill

## 写作规范（本目录特有）

- 章节首部固定结构：一级标题 `# 第 N 章：xxx` → 引言段 → `**本章目录**` 锚点列表 → `---` → 正文
- 解释性"侧栏"用 `>` 引用块包裹，并在首处出现的术语后给出括号或引用块释义（这套教程面向零基础读者，行文风格已锁定为"对一个聪明但非技术背景的读者讲清楚"）
- 父目录 `/Users/wanghe/workspace/CLAUDE.md` 中关于"禁止滥用'不是...不是...而是...'句式"以及标题层级、中文标点等规则同样适用，本文件不再重复
