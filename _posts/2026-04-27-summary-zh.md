---
layout: default
title: "Horizon Summary: 2026-04-27 (ZH)"
date: 2026-04-27
lang: zh
---

> From 22 items, 7 important content pieces were selected

---

1. [Fast16：早于震网五年的高精度破坏](#item-1) ⭐️ 8.0/10
2. [AI 应提升思考，而非替代它](#item-2) ⭐️ 8.0/10
3. [OpenAI 因饱和停止使用 SWE-bench Verified](#item-3) ⭐️ 8.0/10
4. [OpenClaw v2026.4.25-beta.2：TTS、插件、OpenTelemetry 升级](#item-4) ⭐️ 7.0/10
5. [买下 Friendster 域名后，开发者打造本地社交应用](#item-5) ⭐️ 6.0/10
6. [粘土 PCB 教程引发可持续电子制造讨论](#item-6) ⭐️ 6.0/10
7. [可视化工具揭示 Zork 1 的 Z-machine 内部](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Fast16：早于震网五年的高精度破坏](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/) ⭐️ 8.0/10

SentinelOne 研究人员发现了一种名为'Fast16'的复杂 Lua 恶意软件框架，其历史可追溯至 2005 年，能够精确破坏工程软件中的计算。这一发现揭示了在震网（Stuxnet）出现五年前就已存在的高精度软件破坏技术。 这一发现重塑了我们对早期网络破坏的理解，证明在震网之前很久就已经存在高级、精确的恶意软件。它突出了国家支持的黑客不断演变的工具集，并展示了诸如 Lua 等脚本语言在秘密行动中的使用。 该恶意软件使用 Lua 脚本实现复杂的数学变换，从而改变工程软件中的关键计算结果，可能影响核反应堆等敏感系统的模拟。该恶意软件是通过分析历史样本以及影子经纪人（Shadow Brokers）泄露资料中的参考信息而被识别的。

hackernews · dd23 · Apr 26, 20:18

**背景**: 震网（Stuxnet）于 2010 年被发现，是一种具有里程碑意义的网络武器，旨在通过改变伊朗核离心机的运行来造成物理破坏。它展示了恶意软件造成现实世界破坏的可能性。Fast16 恶意软件来自 2005 年，表明类似的能力早在几年前就已经在开发中，并且使用了不同的技术手段，例如嵌入 Lua 脚本。这一发现为网络战战术的演变提供了新的背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/04/researchers-uncover-pre-stuxnet-fast16.html">Researchers Uncover Pre-Stuxnet ‘ fast 16 ’ Malware Targeting...</a></li>
<li><a href="https://delimiter.online/blog/fast16-malware/">Researchers Uncover 2005 Malware That Preceded... - Delimiter Online</a></li>

</ul>
</details>

**社区讨论**: 社区评论对这一历史性发现表示兴奋，一些用户指出 2005 年 Windows 内核代码中异常使用了 SCCS/RCS 版本控制注释，这表明开发者可能来自政府或军事计算背景。其他人则对具体目标和计算修改的确切性质感到好奇。还有用户提供了恶意软件样本的下载链接以供进一步分析。

**标签**: `#cybersecurity`, `#malware`, `#Stuxnet`, `#history`, `#software sabotage`

---

<a id="item-2"></a>
## [AI 应提升思考，而非替代它](https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/) ⭐️ 8.0/10

Koshy John 发表博客文章，主张 AI 工具在软件工程中应增强人类推理和判断，而非取代它们，此文在 Hacker News 上引发了激烈讨论。 这场讨论触及现代软件工程的核心矛盾：对 AI 生成代码的依赖可能侵蚀工程师对工作的深层理解和所有权，长期可能损害代码质量和思维严谨性。 文章强调判断没有捷径，掌握知识不能通过生成的解释无努力地转移；Hacker News 帖子（270 分，221 条评论）包含与过去工具依赖（如 IDE 和包管理器）的类比。

hackernews · koshyjohn · Apr 26, 20:03

**背景**: 随着 GitHub Copilot 和 ChatGPT 等 AI 编程助手的普及，工程师们越来越担心过度依赖这些工具会导致批判性思维和问题解决能力的“用进废退”。这篇博客文章加入了关于技术在人类认知中角色的长期哲学辩论，呼应了早期对计算器和拼写检查器的担忧。

**社区讨论**: 评论者表达了多种观点：有人将 AI 辅助比作过去的工具转变（如从汇编语言到高级语言），认为这是自然进化；另一些人则警告技能退化的真实风险，并引用越来越多的研究证据。一个关键区别在于：使用 AI 编写自己仍然拥有和理解的代码，与将 AI 视为不透明的抽象层之间的差异。

**标签**: `#AI`, `#philosophy of technology`, `#software engineering`, `#critical thinking`, `#productivity`

---

<a id="item-3"></a>
## [OpenAI 因饱和停止使用 SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) ⭐️ 8.0/10

OpenAI 宣布将不再使用 SWE-bench Verified 基准来评估模型，因为最高得分已达到 93.9%，表明该基准已饱和。 这一决定凸显了 AI 编码评估中基准饱和这一日益严重的问题——模型迅速达到上限，降低了基准区分能力的效果。它强调了迫切需要更新、更难的评估方法来追踪代码生成领域的真实进展。 93.9%的饱和分数由 Anthropic 的模型达到，OpenAI 指出低于该阈值的提升空间已十分有限。SWE-bench Verified 是从原始 SWE-bench 中经人工验证的 500 个样本子集，最初由 OpenAI 合作创建。

hackernews · kmdupree · Apr 26, 13:58

**背景**: SWE-bench 是一个基准测试，通过生成代码补丁来评估大语言模型解决真实 GitHub 问题的能力。每个任务在隔离的 Docker 容器中运行，模型必须生成正确的补丁。SWE-bench Verified 是经过人工筛选的子集，旨在减少噪声和歧义。这类基准对于衡量编码 AI 的进展至关重要，但随着模型改进及训练数据重叠，它们往往很快达到饱和。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swebench.com/verified.html">SWE - bench Verified</a></li>
<li><a href="https://openai.com/index/introducing-swe-bench-verified/">Introducing SWE - bench Verified | OpenAI</a></li>
<li><a href="https://www.vals.ai/benchmarks/swebench">SWE-bench</a></li>

</ul>
</details>

**社区讨论**: SWE-bench 联合创建者 Ofir Press 承认了饱和现象，指出即将推出的 SWE-bench Multilingual 和 Multimodal 尚未饱和，并提醒所有基准最终都会饱和。其他评论者则担忧基准被利用、训练数据截止日期与公开发布之间的短暂间隔，以及创建新颖、未被污染基准的难度。

**标签**: `#AI benchmarks`, `#coding AI`, `#SWE-bench`, `#benchmark saturation`, `#machine learning evaluation`

---

<a id="item-4"></a>
## [OpenClaw v2026.4.25-beta.2：TTS、插件、OpenTelemetry 升级](https://github.com/openclaw/openclaw/releases/tag/v2026.4.25-beta.2) ⭐️ 7.0/10

OpenClaw v2026.4.25-beta.2 引入了重大升级，包括多提供商 TTS 支持、插件注册表迁移至冷存储、扩展的 OpenTelemetry 可观测性以及改进的浏览器自动化。 这些增强功能使 OpenClaw 在语音交互方面更加灵活，插件管理更加可靠，调试更加透明，有利于依赖此开源自动化平台的开发者和用户。 新增 TTS 提供商包括 Azure Speech、小米、本地 CLI、Inworld、火山引擎和 ElevenLabs v3。插件注册表现在使用冷持久化存储以减少扫描开销并提高确定性。OpenTelemetry 覆盖了模型调用、令牌使用、工具循环和内存压力。

github · steipete · Apr 26, 12:23

**背景**: OpenClaw 是一个开源自动化工具，支持浏览器自动化、文本转语音（TTS）、插件和可观测性。OpenTelemetry 是一个供应商中立的可观测性框架，用于云原生软件，由 CNCF 托管。Chrome DevTools 协议（CDP）用于远程调试 Chromium 浏览器。插件注册表中的冷存储指将数据持久化到磁盘以实现确定性和高效访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenTelemetry">OpenTelemetry</a></li>
<li><a href="https://opentelemetry.io/">OpenTelemetry</a></li>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol</a></li>

</ul>
</details>

**标签**: `#TTS`, `#plugins`, `#OpenTelemetry`, `#browser automation`, `#open source`

---

<a id="item-5"></a>
## [买下 Friendster 域名后，开发者打造本地社交应用](https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d) ⭐️ 6.0/10

一位开发者以价值 3 万美元的比特币加上一个产生广告收入的域名，购得了 Friendster.com 域名，目前正在开发一款超本地社交网络应用。该应用因被认为受众过窄而被苹果 App Store 拒绝，开发者正在探索基于渐进式 Web 应用（PWA）和 Nostr 协议的替代方案。 这一事件凸显了在集中式应用商店政策下构建小众社交应用的挑战，以及向 PWA、Nostr 等去中心化、跨平台替代方案转型的潜力。同时它也反映了怀旧互联网资产的持久价值，以及如何将其重新用于现代需求。 开发者支付了 2 万美元的比特币加上一个年广告收入约 9000 美元的域名，获得了 Friendster.com 域名。目前他正考虑基于二维码扫描的 PWA 来绕过 App Store 限制，并利用去中心化协议 Nostr 构建社交功能，以实现抗审查和用户自主控制。

hackernews · ca98am79 · Apr 26, 20:41

**背景**: Friendster 是 2002 年推出的最早社交网络平台之一，因未能与 MySpace 和 Facebook 竞争而最终关闭。Nostr（Notes and Other Stuff Transmitted by Relays）是一个开放、去中心化的社交网络协议，使用加密密钥和中继（relays）实现抗审查的通信。渐进式 Web 应用（PWA）是一种可以像原生应用一样安装到设备上的网页应用，无需通过应用商店即可跨平台运行。这些技术为传统的集中式应用生态提供了替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noster_(protocol)">Noster (protocol)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Progressive_web_app">Progressive web app</a></li>

</ul>
</details>

**社区讨论**: 评论者对苹果 App Store 的审核规则表达了强烈不满，认为平台所有者不应为小众受众的应用程序规定功能。多位用户提出了技术替代方案：有人建议基于 Nostr 协议构建二维码扫描的 PWA 以降低成本并提高可访问性，另一位则分享了自己类似的超本地游戏项目。讨论还涉及了涉及比特币和产生收入域名的独特域名购买交易。

**标签**: `#domain acquisition`, `#social networking`, `#app store review`, `#progressive web app`, `#decentralized protocols`

---

<a id="item-6"></a>
## [粘土 PCB 教程引发可持续电子制造讨论](https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial) ⭐️ 6.0/10

一个由女性黑客空间发布的教程展示了如何利用野生粘土和城市开采的银在篝火中烧制出印刷电路板（PCB），这是一种低技术、可持续的替代传统 PCB 制造的方法。 该项目挑战了依赖冲突矿产和能源密集型工艺的传统 PCB 行业，并通过女性主义黑客和艺术方法论鼓励重新思考硬件生产。它凸显了更易获得、小规模电子制造的潜力。 导电线路由城市开采的银制成，所有元器件均从旧电子设备中回收再利用。所使用的微控制器完全开源，最终 PCB 在类似篝火的环境中烧制。

hackernews · j0r0b0 · Apr 26, 16:02

**背景**: 印刷电路板（PCB）通常由玻璃纤维层压板和铜箔线路组成，通过化学蚀刻或机械铣削生产。粘土 PCB 方法用野生粘土和导电银浆替代这些材料，并用篝火烧制。这一做法属于更广泛的替代性、可持续电子制造探索的一部分，常与黑客文化和批判性制作相关联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial">Clay PCB Tutorial — feministhackerspaces</a></li>
<li><a href="https://radical-openness.org/en/programm/2024/clay-pcb">Clay PCB | Art Meets Radical Openness</a></li>
<li><a href="https://media.ccc.de/v/38c3-clay-pcb">Clay PCB - media.ccc.de</a></li>

</ul>
</details>

**社区讨论**: 参与者分享了积极的亲手实践体验，有人提到使用来自奥地利森林的粘土很有趣。评论者也对可持续性展开了讨论：有人质疑篝火燃烧是否比 3D 打印排放更多，另一些人则建议，对于简单电路，完全避免使用 PCB 可能更可持续。讨论还提及了 MIT 的'无部件套件'等早期工作。

**标签**: `#PCB`, `#alternative manufacturing`, `#sustainability`, `#hacker culture`, `#clay`

---

<a id="item-7"></a>
## [可视化工具揭示 Zork 1 的 Z-machine 内部](https://eblong.com/infocom/visi/zork1/) ⭐️ 6.0/10

一款名为 The Visible Zorker 的新可视化工具，允许用户在运行 Zork 1 时查看 Z-machine 的内部工作原理，而无需使用调试器。 该工具让复古计算爱好者和开发者能够深入了解经典交互小说游戏的内部机制，帮助他们理解像 Zork 这样的早期文字冒险游戏在底层是如何运作的。 该可视化工具在浏览器中显示 Z-machine 的内存、堆栈和程序状态，允许用户逐步检查游戏的执行过程，而无需修改原始的 Zork 1 代码。

hackernews · PLenz · Apr 26, 16:42

**背景**: Z-machine 是 Infocom 在 1970 年代末至 1980 年代初专门为运行 Zork 等交互小说游戏而开发的虚拟机。它将游戏逻辑抽象为可移植的字节码格式，使同一款游戏能在不同平台上运行。The Visible Zorker 利用这一抽象特性，提供了虚拟机内部状态的实时图形化视图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forums.crackberry.com/blackberry-os-apps-f35/wanted-polished-interactive-fiction-interpreter-65086/">Wanted: Polished Interactive Fiction Interpreter - BlackBerry Forums...</a></li>
<li><a href="https://arstechnica.com/gaming/2024/06/from-infocom-to-80-days-an-oral-history-of-text-games-and-interactive-fiction/">From Infocom to 80 Days: An oral history of text games and interactive ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员认为这个工具无需调试器就能查看 Z-machine 内部，非常整洁。有用户询问 Inform 6 是否仍是开发现代文字游戏的合适语言，另一用户则指出在游戏中向西再向东移动会到达不同位置，对 Z-machine 的行为感到好奇。

**标签**: `#Z-machine`, `#Zork`, `#interactive fiction`, `#retro computing`, `#visualization`

---