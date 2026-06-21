---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> From 16 items, 4 important content pieces were selected

---

1. [SMPTE 免费开放其标准库](#item-1) ⭐️ 8.0/10
2. [UHF X11 将 X11 窗口系统引入 Apple Vision Pro 的 visionOS](#item-2) ⭐️ 6.0/10
3. [F-15 Strike Eagle II 逆向工程招募测试员](#item-3) ⭐️ 6.0/10
4. [CSSQuake：用纯 CSS 重现雷神之锤](#item-4) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SMPTE 免费开放其标准库](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

电影电视工程师协会（SMPTE）宣布，其所有标准、推荐实践和工程指南现已免费向公众开放，无需任何费用或注册限制。此举向全球开发者、工程师和媒体专业人士开放了完整的 SMPTE 标准库。 通过取消标准文档的付费门槛，SMPTE 消除了初创公司、独立开发者和小型制作公司此前必须购买昂贵文档以确保合规的重大障碍。这一转变使 SMPTE 与开放标准运动保持一致，可能加速媒体制作和分发技术的创新。 免费访问适用于所有 SMPTE 标准、推荐实践和工程指南，现可从 SMPTE 网站下载。SMPTE 还在现代化其标准开发流程，采用基于 GitHub 的工作流、结构化 HTML 编写以及集成式发布管道。

hackernews · zdw · Jun 20, 17:01

**背景**: SMPTE 是一个全球性的专业协会，致力于为电影和电视行业制定技术标准，包括广泛使用的 SMPTE 时间码和数字电影包等规范。历史上，这些标准只能通过购买获取，限制了许多开发者和小型组织的访问。通过免费开放标准，SMPTE 效仿了 IETF 等其他成功的开放标准组织，后者免费提供标准推动了互联网的爆炸式增长。这一变化是 SMPTE 现代化其标准制定和发布流程的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.smpte.org/standards/overview">Standards Overview | Society of Motion Picture & Television ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Society_of_Motion_Picture_and_Television_Engineers">Society of Motion Picture and Television Engineers - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为积极，评论者如 lambdaone 称赞此举早该实现，并指出免费访问是 IETF 标准成功的关键因素。geerlingguy 等人则表示惊讶，认为任何标准组织都应将此作为默认做法。社区还对 SMPTE 同步推进的现代化努力表示赞赏，包括采用 GitHub 工作流和结构化编写。

**标签**: `#standards`, `#media technology`, `#open access`, `#SMPTE`, `#video production`

---

<a id="item-2"></a>
## [UHF X11 将 X11 窗口系统引入 Apple Vision Pro 的 visionOS](https://www.lispm.net/apps/uhf-x11/) ⭐️ 6.0/10

UHF X11 是一款新应用，它将 X11 窗口系统移植到 Apple Vision Pro 的 visionOS 上，使得传统的 Linux 图形界面应用能够在空间计算环境中运行。每个 X11 顶级窗口都会作为独立的 visionOS 窗口打开，用户可以将它们放置在任何位置。 该项目将传统的 Linux 桌面环境与苹果的空间计算平台连接起来，为 Vision Pro 用户开启了大量经典 Unix 图形界面应用的使用可能。这代表了传统桌面计算与 AR/VR 的新颖融合，不过其实际影响可能仅限于爱好者群体。 该应用通过 X11 上的 GLX 渲染支持 OpenGL 客户端，但兼容性因 GL 版本和功能而异。UHF X11 已在 App Store 上架，社区讨论中还提到了其他项目，如用于在头显上使用 Linux 桌面的 WayVR。

hackernews · zdw · Jun 20, 17:04

**背景**: X11 是 Unix 和 Linux 系统的传统窗口系统，数十年来广泛应用于桌面环境。Apple Vision Pro 运行 visionOS，这是一个源于 iPadOS 的扩展现实操作系统，专为混合现实体验设计。将 X11 移植到 visionOS 使得 Linux 图形界面应用能够在 3D 空间环境中以独立窗口形式显示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apps.apple.com/us/app/uhf-x11/id6772673274">UHF X11 App - App Store</a></li>
<li><a href="https://en.wikipedia.org/wiki/VisionOS">visionOS - Wikipedia</a></li>
<li><a href="https://developer.apple.com/documentation/visionos">visionOS | Apple Developer Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区评论轻松活泼，参与度中等。有用户调侃“3D 中的 2D 中的 3D”，并回忆起 GLX 兼容性挑战。另一位评论者猜测 X11 会比 visionOS 更长寿，还有用户推荐了替代项目 WayVR，用于在头显上使用 Linux 桌面。

**标签**: `#X11`, `#VisionOS`, `#Apple Vision Pro`, `#AR/VR`, `#Linux compatibility`

---

<a id="item-3"></a>
## [F-15 Strike Eagle II 逆向工程招募测试员](https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html) ⭐️ 6.0/10

一名开发者正在对 DOS 飞行模拟游戏 F-15 Strike Eagle II 进行逆向工程，将其汇编代码转换为等效的 C 语言，以便最终移植到现代平台，并正在招募测试人员帮助发现转换过程中引入的漏洞。 该项目使得经典游戏摆脱对 DOS 模拟器的依赖，能够在现代操作系统上原生运行，同时也丰富了复古计算社区对于从汇编到 C 语言代码移植的理解。 转换过程首先将游戏完整逆向为汇编代码，现在目标是将汇编重写为二进制等效的编译 C 代码，整个过程仍在 DOS 下运行，直到没有汇编代码残留，之后再进行 Linux 和 Windows 的移植。

hackernews · LowLevelMahn · Jun 20, 15:10

**背景**: 《F-15 Strike Eagle II》是 1990 年代初的经典 DOS 飞行模拟游戏。逆向工程是指分析已编译程序以理解其结构和逻辑，通常用于重新创建源代码。开发者的方法是将原始汇编代码转换回 C 语言，保留精确行为，以便为不同平台编译。

**社区讨论**: 评论者们表达了兴趣和怀旧之情，提到该游戏是他们童年的一部分。有人询问为何不直接用 DOSBox 模拟，其他人则强调了原生移植在兼容性和低开销方面的价值。还有建议认为 AI 可以帮助从反编译代码中推断结构而无需符号名称。

**标签**: `#reverse engineering`, `#DOS`, `#game porting`, `#retro computing`, `#open source`

---

<a id="item-4"></a>
## [CSSQuake：用纯 CSS 重现雷神之锤](https://cssquake.com/) ⭐️ 6.0/10

CSSQuake 是一个可玩的演示项目，它仅使用 CSS、HTML 和 JavaScript（无需 Canvas 或 WebGL）重现了经典第一人称射击游戏《雷神之锤》。 该项目展示了 CSS 作为渲染媒介的创意和技术极限，引发了关于 Web 能力以及经典游戏怀旧的讨论。 该实现是在 JavaScript 中完整重现了《雷神之锤》的引擎逻辑，通过 CSS 变换和 HTML 元素进行渲染，但与原始游戏相比存在性能问题和行为不准确之处。

hackernews · msalsas · Jun 20, 10:49

**背景**: 《雷神之锤》是 1996 年具有里程碑意义的第一人称射击游戏，以其完全 3D 环境而闻名。CSS（层叠样式表）通常用于网页样式设计，而非实时 3D 渲染。CSSQuake 是一个技术演示，将 CSS 推向了其典型用途之外，但在性能和准确性方面不及原生游戏引擎。

**社区讨论**: 评论者对这一成就印象深刻，但指出它在现代硬件上运行速度比原始游戏慢，并且存在一些玩法不准确之处，例如按钮需要射击而非触碰。一些用户认为尽管有这些瑕疵，它仍然令人怀旧和有趣。

**标签**: `#css`, `#quake`, `#web development`, `#game`, `#demo`

---