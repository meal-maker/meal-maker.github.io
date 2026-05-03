---
layout: default
title: "Horizon Summary: 2026-05-03 (ZH)"
date: 2026-05-03
lang: zh
---

> From 17 items, 8 important content pieces were selected

---

1. [VS Code PR 默认在所有提交中添加 Co-Authored-by Copilot](#item-1) ⭐️ 9.0/10
2. [VideoLAN 发布 Dav2d：最快的 AV2 解码器](#item-2) ⭐️ 8.0/10
3. [特斯拉车主因 FSD 虚假宣传胜诉获 1 万美元，公司仍上诉](#item-3) ⭐️ 8.0/10
4. [Apple Watch 自定义地图应用的六年演变](#item-4) ⭐️ 7.0/10
5. [NetHack 5.0.0 长期等待后发布](#item-5) ⭐️ 7.0/10
6. [macOS 虚拟机性能：最低配置仍能良好运行](#item-6) ⭐️ 7.0/10
7. [Ladybird 浏览器 2026 年 4 月简报：修复与进展](#item-7) ⭐️ 6.0/10
8. [新的 DO_NOT_TRACK Shell 脚本汇总遥测退出环境变量](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [VS Code PR 默认在所有提交中添加 Co-Authored-by Copilot](https://github.com/microsoft/vscode/pull/310226) ⭐️ 9.0/10

一项针对 Visual Studio Code 的拉取请求（vscode#310226）更改了默认设置，使得即使未实际使用 Copilot，也会在所有 Git 提交中添加 'Co-Authored-by: Copilot'。 这一变更通过伪造提交作者记录削弱了开发者信任，可能对版本控制历史的完整性产生法律影响，并错误地代表 Copilot 的使用统计数据。 该 PR 的配置架构默认值被设置为 'all'，但运行时回退仍使用 'off'，导致不一致。社区批评这一变更是对信任的背叛和记录伪造。

hackernews · indrora · May 2, 19:57

**背景**: Git 支持 'Co-Authored-by' 提交尾注，以在单个提交中标记多个作者。GitHub 使用该信息显示多个贡献者。传统上，这些尾注是手动或基于明确意图添加的；在无实际共同作者时默认添加违背了惯例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors">Creating a commit with multiple authors - GitHub Docs</a></li>
<li><a href="https://stackoverflow.com/questions/58525836/git-magic-keywords-in-commit-messages-signed-off-by-co-authored-by-fixes">github - Git magic keywords in commit messages (Signed-off-by...)</a></li>

</ul>
</details>

**社区讨论**: 社区反应强烈，许多评论称此举为信任背叛、记录伪造和危险先例。有评论指出，Copilot 自己的机器人也在 PR 中评论建议撤销此更改，但被忽略。

**标签**: `#VS Code`, `#GitHub Copilot`, `#Git`, `#Ethics`, `#Microsoft`

---

<a id="item-2"></a>
## [VideoLAN 发布 Dav2d：最快的 AV2 解码器](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN 宣布推出 dav2d，一款快速且可移植的 AV2 视频解码器，并声称它是所有平台上最快的 AV2 解码器。 AV2 是开放媒体联盟（AOMedia）推出的下一代视频编解码器，相比 AV1 可节省高达 30%的码率，而 dav2d 的高性能可能加速 AV2 在流媒体、广播和软件播放中的采用。 Dav2d 被设计为小巧、可移植且速度极快，延续了 VideoLAN 为 AV1 开发的 dav1d 解码器的成功。截至 2026 年 5 月，AV2 规范仍处于草案状态，最终版本预计在 2025 年底发布。

hackernews · dabinat · May 2, 17:32

**背景**: AV2 是开放媒体联盟（AOMedia）开发的开源、免版税视频编码格式，是 AV1 的继任者。它旨在通过帧内预测、分区和帧间模式的显著改进，提供卓越的压缩效率。VideoLAN 此前曾创建高度优化的 AV1 解码器 dav1d，而 dav2d 遵循类似的理念，为 AV2 提供尽可能快的软件解码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://av2.aomedia.org/">AV2 Specification</a></li>

</ul>
</details>

**社区讨论**: 社区对 dav2d 的潜力表示热情，但对其编码器的成熟度表示担忧，指出 SVT-AV1 花了很长时间才变得可用。一些用户要求提供 AV2 与 AV1 的量化比较，而其他用户则强调了网络访问中日益增加的摩擦（机器人验证、cookie）。

**标签**: `#AV2`, `#video codec`, `#decoder`, `#VideoLAN`, `#performance`

---

<a id="item-3"></a>
## [特斯拉车主因 FSD 虚假宣传胜诉获 1 万美元，公司仍上诉](https://electrek.co/2026/05/02/this-tesla-owner-won-10k-in-court-for-teslas-fsd-lies-tesla-is-still-fighting-him/) ⭐️ 8.0/10

一位特斯拉车主赢得法院判决，获得 10,672.88 美元（约合人民币 7.7 万元），即他购买全自动驾驶（FSD）功能的全部费用，原因是证明了特斯拉对该系统能力的虚假宣传。特斯拉继续对这一裁决提出上诉。 此案可能为自动驾驶技术领域的消费者保护树立先例，对抗虚假宣传。如果维持原判，可能会引发其他购买 FSD 的特斯拉车主提起类似诉讼的浪潮。 赔偿金额包括 FSD 的购买价格、税费和诉讼费，但值得注意的是不包括利息。车主（Gawiser）多次报告安全问题，例如意外激活紧急车道偏离功能。

hackernews · breve · May 2, 22:45

**背景**: 特斯拉的全自动驾驶（FSD）是一种高级驾驶辅助系统，特斯拉一直宣传其能够实现完全自动驾驶。批评者和监管机构指责特斯拉过度承诺并误导消费者关于该系统的实际能力，导致多项调查和诉讼。

**社区讨论**: 评论者指出，特斯拉之所以继续抗争，很可能不是因为金额小，而是为了避免创下可能引发大量类似诉讼的法律先例。一位用户分享了根据加州柠檬法因软件问题获得 25 万美元赔偿的个人经历，而其他人则对特斯拉是否会实际付款表示怀疑，除非采取公开抗议等极端手段。

**标签**: `#Tesla`, `#FSD`, `#legal`, `#false advertising`, `#autonomous driving`

---

<a id="item-4"></a>
## [Apple Watch 自定义地图应用的六年演变](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 7.0/10

开发者 David Smith 发布了一篇详细的博客文章，讲述了一款 Apple Watch 第三方地图应用六年的开发历程。该应用使用预渲染的自定义图像瓦片，提供了比苹果原生地图更细致、更美观的地图体验。 这一故事突显了苹果在 watchOS 上原生地图的不足，并展示了第三方开发者如何通过创造性技术手段实现更优秀的用户体验。它激励开发者们突破 Apple Watch 平台的限制。 与 Apple Maps 的动态矢量渲染不同，该应用显示静态预渲染的地图图像瓦片，其中包含如徒步小径等自定义制图细节。这种方法实现了更佳的视觉效果，但需要为每个缩放级别单独下载瓦片，且不支持实时更新。

hackernews · valzevul · May 2, 21:14

**背景**: 瓦片式网络地图通过无缝拼接多个称为“瓦片”的小图像文件来显示地图。预渲染的瓦片集是提前生成的静态图像，而动态渲染的地图则实时获取矢量数据。在 Apple Watch 上，标准的 MapKit 对自定义叠加层的支持有限，因此开发者常借助 SpriteKit 或其他渲染引擎来显示自定义瓦片图像。David Smith 甚至聘请了专业制图师为他的应用设计瓦片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/">Six Years Perfecting Maps on watchOS - David Smith, Independent iOS Developer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tiled_web_map">Tiled web map - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/60544111/how-to-make-scrollable-and-zoomable-custom-map-on-apple-watch">swift - How to make scrollable and zoomable custom map on Apple Watch? - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 社区评论对苹果仍未在 Apple Watch（尤其是 Ultra 系列）上提供官方徒步和地形地图表示失望。许多评论赞扬了开发者的细致入微以及巧妙使用静态瓦片的方法，同时也指出了其取舍（需单独下载、无法实时更新）。有用户特别提到了聘请制图师这一细节，认为这是非常酷且专注的做法。

**标签**: `#watchOS`, `#maps`, `#app development`, `#design`, `#Apple Watch`

---

<a id="item-5"></a>
## [NetHack 5.0.0 长期等待后发布](https://nethack.org/v500/release.html) ⭐️ 7.0/10

NetHack 5.0.0 正式发布，用 Lua 脚本取代了沿用数十年的 yacc/lex 关卡和地牢编译器，并引入了其他重大架构变更。 此次发布标志着这款历史最悠久的活跃 roguelike 游戏的一次重大现代化升级，提升了可修改性和可维护性，同时保留了其传奇性的玩法，重新点燃了 roguelike 社区的关注。 NetHack 5.0.0 内嵌 Lua 5.4.8，无需外部安装，但现有的存档文件和骨头文件不兼容。构建系统现在通过 Lua 在运行时处理地牢和关卡数据。

hackernews · rsaarelm · May 2, 18:03

**背景**: Yacc（Yet Another Compiler-Compiler）和 Lex 是经典的 Unix 工具，用于从形式文法生成解析器和词法分析器。自 NetHack 早期起，它们就被用来编译关卡和地牢描述。用 Lua 脚本替代它们，将数据处理从编译时移至运行时，使开发者和模组作者无需重新编译即可更轻松地修改游戏内容。Lua 是一种轻量级脚本语言，自 1993 年就已存在，在游戏开发中广泛用于模组和配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yacc">Yacc - Wikipedia</a></li>
<li><a href="https://deepwiki.com/NetHack/NetHack/5-build-system">Build System | NetHack/NetHack | DeepWiki</a></li>
<li><a href="https://news.ycombinator.com/item?id=47988776">NetHack 5.0.0 | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区表达了对旧版本的怀旧之情，一位玩家回忆其 17 年历史的存档文件现已不兼容。技术决策受到赞赏，但有人指出这标志着一个时代的结束。其他人希望 3D 客户端等工具能尽快更新以支持 5.0.0。

**标签**: `#NetHack`, `#roguelike`, `#Lua`, `#game development`, `#retro computing`

---

<a id="item-6"></a>
## [macOS 虚拟机性能：最低配置仍能良好运行](https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/) ⭐️ 7.0/10

一项关于 macOS 虚拟机的性能探索表明，将虚拟核心和内存降低至 2 核和 4 GB RAM，虚拟机仍能流畅处理轻量级任务，且内存使用量按比例下降。 这对需要在 Mac 上运行轻量级虚拟机的开发者和用户很重要，表明他们可以分配更少的资源以节省主机内存，同时仍能获得可接受的性能。同时，它也揭示了 macOS 虚拟机中缺乏 GPU 计算加速等重要权衡。 每个虚拟核心会消耗额外的内存用于页缓存和并发处理，因此减少核心数也会降低内存使用量。但 macOS 虚拟机中的 virtio-gpu 层仅传递图形 GPU，不传递计算 GPU，导致无法进行 PyTorch GPU 加速，且通过 colima 运行的 Docker 效率仍然较低。

hackernews · moosia · May 2, 09:30

**背景**: 在 Apple Silicon 上，macOS 通过 Virtualization.framework 支持运行 macOS 客户机。虚拟机性能依赖于分配的虚拟核心数和内存量，但图形加速仅限于基本显示输出，机器学习所需的 GPU 计算功能并未直通。本文探讨了多低的资源分配仍能有效支持轻量级任务。

**社区讨论**: 社区评论普遍认同内存使用量随核心数按比例下降的发现。有用户感叹虚拟机中无法使用 PyTorch GPU 加速，因为计算 GPU 未被直通。其他用户分享了实际体验：colima + Docker 虽然可用但效率较低，也有人推荐了 trycua/lume 作为替代方案。有评论质疑在虚拟机内启动应用程序后是否会占用全部分配的内存。

**标签**: `#macOS`, `#virtualization`, `#performance`, `#VM`, `#Mac`

---

<a id="item-7"></a>
## [Ladybird 浏览器 2026 年 4 月简报：修复与进展](https://ladybird.org/newsletter/2026-04-30/) ⭐️ 6.0/10

2026 年 4 月的 Ladybird 浏览器简报报告了多项错误修复和改进，包括修复 CSS Doom 以及提升与 Strava 和 Reddit 等网站的兼容性。 这些渐进式改进表明 Ladybird 正稳步迈向 2026 年晚些时候的 Alpha 版本，证明一个真正独立、非 Chromium 内核的浏览器在日常使用中正变得越来越可行。 简报提到诸如使`Navigator.getBattery`抛出正确的错误类型，从而让 Strava 登录正常工作，还包括对 Reddit 渲染的改进。

hackernews · richardboegli · May 2, 20:46

**背景**: Ladybird 是一个开源网络浏览器，由非营利组织 Ladybird Browser Initiative 开发，最初是 SerenityOS 的一部分，现已独立。它从头开始构建，使用自有引擎，不基于 Chromium 或 Firefox。计划于 2026 年发布 Alpha 版本，2027 年 Beta 版本，2028 年稳定版，资金完全来自 Cloudflare、FUTO、Shopify 和 37signals 等赞助商的捐赠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_(web_browser)">Ladybird (web browser) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，评论者注意到 Ladybird 变得“相当可用”，并将其更新风格比作游戏模拟器更新。一位评论者强调 Reddit 已在 Ladybird 上运行，另一位则讨论了用 Dioxus 构建的无 JavaScript 浏览器替代方案。还有一段关于赞助商背景的简短讨论。

**标签**: `#browser`, `#open-source`, `#ladybird`, `#software engineering`

---

<a id="item-8"></a>
## [新的 DO_NOT_TRACK Shell 脚本汇总遥测退出环境变量](https://donottrack.sh/) ⭐️ 6.0/10

donottrack.sh 上的一个新 Shell 脚本将数十个遥测退出环境变量（如 DOTNET_CLI_TELEMETRY_OPTOUT、HF_HUB_DISABLE_TELEMETRY）汇总为一个 DO_NOT_TRACK 环境变量，旨在简化用户隐私控制。 该倡议重新引发了关于遥测退出默认设置以及单一'禁止跟踪'信号有效性的长期争论，特别是考虑到类似的 DNT 浏览器标头已经失败。如果被广泛采用，它可以简化用户的隐私管理，但也引发了关于创建追踪者可以忽略的蜜罐的担忧。 DO_NOT_TRACK 变量并非标准，而是社区驱动的汇总，需要软件作者明确支持。该脚本目前涵盖来自.NET SDK、Hugging Face、n8n 等工具的环境变量，但采用率仍然很低。

hackernews · RubyGuy · May 2, 17:40

**背景**: 许多软件工具和库默认收集遥测数据以改进产品，但提供环境变量供用户选择退出。然而，每个工具使用不同的变量名，使得用户难以在所有工具中禁用遥测。DO_NOT_TRACK 环境变量旨在提供一个单一的通用退出信号，供工具检查。这一概念呼应了早期的'Do Not Track' HTTP 标头，该标头被网站广泛忽略并最终被弃用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://donottrack.sh/">Do _ not _ track</a></li>
<li><a href="https://docs.telemetry-kit.dev/privacy">Privacy Controls | telemetry-kit Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该倡议的有效性表示怀疑。几位用户将其与失败的 DNT 浏览器标头相提并论，并预测其会遭遇同样的命运。其他人警告该脚本可能成为蜜罐，让追踪者专门针对设置 DO_NOT_TRACK 的用户。还有一位用户分享了对实际阻止 Python transformers 库遥测的困难感到沮丧，凸显了该倡议试图解决的实际挑战。

**标签**: `#telemetry`, `#privacy`, `#environment-variables`, `#opt-out`, `#open-source`

---