---
layout: default
title: "Horizon Summary: 2026-11-11 (ZH)"
date: 2026-11-11
lang: zh
---

> 从 24 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Synaptics 专利主张阻止 DisplayLink 驱动开发](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepMind 推出 AlphaProof Code 进行形式化代码验证](#item-tech-news-2) ⭐️ 8.0/10
3. [AMD Zen 6 架构解析：核心、缓存与 I/O 芯片变化](#item-tech-news-3) ⭐️ 8.0/10
4. [.NET 11 运行时新增功能一览](#item-tech-news-4) ⭐️ 8.0/10
5. [七个月后评估：Glasswing 发现结果令开源维护者失望](#item-tech-news-5) ⭐️ 7.0/10
6. [Val Town 云编程平台宣布关停](#item-tech-news-6) ⭐️ 7.0/10
7. [Chrome 等发布面向 AI 编码代理的现代 Web 平台指南 1.0](#item-tech-news-7) ⭐️ 7.0/10
8. [AI 编程生成脆弱代码库引发开发者争论](#item-tech-news-8) ⭐️ 7.0/10
9. [llm-gemini 0.36 发布：Gemini 4 Carbon 全面开放](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [美国汽油均价跌破每加仑 4 美元 为 7 月以来首次](#item-finance-news-1) ⭐️ 8.0/10
2. [美联储理事沃勒：倾向 12 月加息，或考虑 50 个基点](#item-finance-news-2) ⭐️ 8.0/10
3. [Polymarket 年化收入突破 18 亿美元](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Synaptics 专利主张阻止 DisplayLink 驱动开发](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/) ⭐️ 8.0/10

Synaptics 以专利侵权为由发出法律函件，导致开源 DisplayLink 驱动程序的开发停止。该函件要求相关方支付 25,000 美元，用以弥补 Synaptics 制作侵权文件所花费的成本和精力。这一主张引发对 Linux 硬件支持的法律和实际可行性的担忧。评论指出，DisplayLink 本身正因高 DDR 价格上涨而衰落，部分扩展坞厂商已取消相关产品线。

hackernews · speckx · 11月10日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50443824)

**「背景」** DisplayLink 是 Synaptics 旗下用于 USB 扩展坞/显示连接的专有技术。一名开发者此前开发了一个基于 Rust 的开源 DisplayLink 驱动（曾以 Vino 名称进行开发），并通过逆向工程（包括借助 Claude AI 辅助）来理解硬件协议。Synaptics 随后向该开发者发出停止并终止函，声称其侵犯专利，导致相关开源驱动已从公开渠道消失。

**「影响」** 依赖 DisplayLink 扩展坞的 Linux 用户可能因驱动开发停止而失去后续支持。社区指出，Thunderbolt/USB4 扩展坞和 DisplayPort Alt Mode 的替代支持更成熟。

**「社区讨论」** 评论普遍认为 25,000 美元索赔是恐吓手段且法律依据不足，并指出逆向工程本身不构成专利侵权，清洁室逆向工程也应合法。部分评论者认为 DisplayLink 已过时且经济性差，现代 Thunderbolt/USB4 扩展坞是更好的替代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/peripherals/docking-stations-hubs/synaptics-sends-cease-and-desist-order-to-creator-of-open-source-displaylink-driver-dares-him-to-publicize-its-threats-dev-reverse-engineers-displaylink-using-claude-ai-and-rust-synaptics-threatens-to-bill-creator-for-legal-documentation">Synaptics sends cease-and-desist order to creator of open - source ...</a></li>
<li><a href="https://www.phoronix.com/news/Synaptics-Blocks-Vino-Driver">Synaptics Appears To Use Legal Threats To Block Open - Source ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#drivers`, `#patents`, `#linux`, `#hardware`

---

<a id="item-tech-news-2"></a>
### [DeepMind 推出 AlphaProof Code 进行形式化代码验证](https://deepmind.google/blog/introducing-alphaproof-code/) ⭐️ 8.0/10

DeepMind 宣布推出 AlphaProof Code，一个利用证明助手对代码进行形式化验证的 AI 系统。该系统旨在将 AI 应用于形式化代码验证，这一领域对软件工程和 AI 研究具有重要价值。公告在社区中引发了关于其实际能力和“零 bug”说法的讨论。部分评论者怀疑验证范围或定理设定可能存在局限。

hackernews · ilreb · 11月10日 12:11 · [社区讨论](https://news.ycombinator.com/item?id=50439193)

**「背景」** 形式化验证使用证明助手（如 Lean）对代码或协议进行数学证明，检查实现是否满足规格，但传统上成本很高。Google DeepMind 的 AlphaProof Code 是一个由 Gemini Carbon 驱动的多 LLM 代理框架，将验证工作分解为“人类专家决定证明目标、AI 代理执行证明”的流程；它在约四周内生成了超过 600 万行 Lean，对 Signal 协议中实际运行的密码学代码的选定安全性质进行了机器检查。

**「影响」** 若 AlphaProof Code 的方法被广泛采用，软件开发者可能需要更重视形式化验证而非仅依赖测试，但其零缺陷声明目前尚需独立验证。

**「社区讨论」** 评论者普遍对“零 bug”声明表示怀疑，认为 AI 可能仅证明了窄属性或写出了与预期相反的实现；同时也有观点认为未来运行未经验证的软件将显得不合时宜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/introducing-alphaproof-code/">Formal Verification of Signal’s Protocol with Gemini</a></li>
<li><a href="https://explainx.ai/blog/google-deepmind-alphaproof-code-signal-protocol-formal-verification-2026">AlphaProof Code: Signal Protocol Verified in 4 Weeks ...</a></li>
<li><a href="https://aiweekly.co/alerts/google-deepminds-alphaproof-code-formally-verifies-signal-protocol-guarantees">Google DeepMind&#x27;s AlphaProof Code Formally Verifies Signal ...</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#AI`, `#software engineering`, `#DeepMind`, `#proof assistants`

---

<a id="item-tech-news-3"></a>
### [AMD Zen 6 架构解析：核心、缓存与 I/O 芯片变化](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast) ⭐️ 8.0/10

本文分析 AMD Zen 6 家族微架构调整，涵盖核心、缓存与 I/O die 变化及其性能影响。核心方面，每周期可执行四路 256 位向量加载，整数乘法单元由三个减少为两个，PDEP/PEXT 吞吐从每周期三条降至两条。缓存方面，单个 CCD 可容纳 32 个 C 核并增大 L3 缓存；I/O die 的改动旨在改善 AM5 平台的内存控制器表现。整体来看，这些调整侧重于平衡核心吞吐与内存供给，以应对多核扩展需求。

hackernews · pixelpoet · 11月10日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=50443090)

**「背景」** AMD 的 Zen 6 是继 Zen 5 之后的下一代微架构，延续 chiplet 设计：计算核心集中在 CCD 芯片上，而内存控制器、PCIe 等位于独立的 I/O die。此次 Zen 6 的服务器 CCD 集成 12 个核心，并为每核配置 4 MB L3 缓存，同时扩大执行窗口以提高指令级并行度。据早期信息，Zen 6 相比 Zen 5 的 IPC 提升约 10%，主要得益于缓存子系统、分支预测器和流水线的改进。

**「影响」** 依赖 PDEP/PEXT 指令的工作负载在 Zen 6 上可能面临吞吐减半（每周期 3 条降至 2 条），需在性能优化时重新评估。

**「社区讨论」** 社区讨论聚焦于 AM5 内存控制器瓶颈与 Zen 6 新 I/O die 的期待，有用户指出 Zen4/Zen5 双通道内存难以超过 3600 MT/s。另有评论质疑 PDEP/PEXT 与乘法单元是否共享电路，并关注 32 核 CCD 的 NUMA 调度粒度，认为整体改进较均衡但向量 gather 性能仍待验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/review/amd-zen-6-technical-deep-dive/">AMD Zen 6 Technical Deep Dive - TechPowerUp</a></li>
<li><a href="https://www.pchardwarepro.com/en/AMD-Zen-6:-Everything-we-know-about-the-upcoming-Ryzen-architecture/">AMD Zen 6: Features, Cores, and Cache of Ryzen 10000</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Zen 6`, `#CPU architecture`, `#microarchitecture`, `#hardware`

---

<a id="item-tech-news-4"></a>
### [.NET 11 运行时新增功能一览](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime) ⭐️ 8.0/10

微软发布了 .NET 11 运行时的新增功能文档，涵盖多项变更。其中运行时异步支持允许在运行时处理异步方法，减少生成的状态机代码，可能改善堆栈跟踪。decimal 精度更新改变了显式转换行为：在 .NET 10 中 \`\(decimal\)0.1\` 结果为 0.1，而在 .NET 11 中变为 0.1000000000000000055511151231。此外还引入了官方版本管理器 dotnetup。这些变化对升级到 .NET 11 的开发者有直接影响。

hackernews · stevefan1999 · 11月10日 12:20 · [社区讨论](https://news.ycombinator.com/item?id=50439284)

**「背景」** .NET 是微软推出的跨平台开发框架，其运行时负责执行托管代码、JIT 编译与内存管理等核心任务。.NET 11 是计划中的下一个年度主要版本；根据官方文档，运行时将引入 Runtime Async、JIT 改进与硬件加速等变更，并调整 decimal 精度，这可能改变数值的字符串表示等兼容性行为。部分新特性（如 Runtime Async）在发布时可能仍处于预览或实验状态。

**「影响」** 升级到 .NET 11 的 .NET 开发者需检查依赖 \`\(decimal\)0.1 == 0.1\` 等精确比较的代码，因为该转换结果不再四舍五入为 0.1，可能导致行为变化。

**「社区讨论」** 社区对 .NET 11 的运行时异步支持表示惊讶和期待，认为堆栈跟踪更友好；同时多位开发者提醒 C\# 和 .NET 生态被低估，并强调 decimal 行为变化需要留意。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime">What&#x27;s new in .NET 11 runtime | Microsoft Learn</a></li>
<li><a href="https://www.dotnetdevs.io/guides/dotnet-11/">.NET 11: a reading guide to what&#x27;s new | .NET devs</a></li>

</ul>
</details>

**标签**: `#dotnet`, `#runtime`, `#release-notes`, `#csharp`, `#software-engineering`

---

<a id="item-tech-news-5"></a>
### [七个月后评估：Glasswing 发现结果令开源维护者失望](https://www.vulncheck.com/blog/anthropic-glasswing-november-update) ⭐️ 7.0/10

VulnCheck 在 Glasswing 发布七个月后对 Anthropic 的 Glasswing 进行了评估，认为其对开源维护者的总体结果“不尽如人意”。该评估主要基于针对开源项目的协调漏洞披露账目，但有评论者指出，Glasswing 的多数漏洞发现发生在合作伙伴指向专有代码的场景，公开账目不能代表其全部效果。一位评论者（pizlonator）表示，其收到的 9 份针对 Fil-C 的报告全部为真实漏洞、零误报，报告质量出色，部分修复被直接采纳或作为重要参考。其他评论者补充，公开 CVE 数据集表现不佳不能反映私有代码库中的实际问题，并提到 PHP2Shell 漏洞依赖已知逻辑缺陷、利用条件复杂，实际影响有限。

hackernews · panic · 11月10日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=50447074)

**「背景」** Anthropic 于七个月前启动 Project Glasswing，旨在利用 AI 模型发现开源软件漏洞；VulnCheck 持续追踪其公开结果。根据 VulnCheck 11 月更新，已归因于 Anthropic 的 CVE 为 442 个，约占今年全部 CVE 的 0.5%，其中仅 2 个被发现在野利用；在 37,966 条上报发现中，只有 7,349 条（19.4%）已公开，217 条标记为已修复。这组数据被用于讨论 AI 漏洞发现的高产出、低信号以及维护者被大量报告淹没的问题。

**「影响」** 公开协调披露账目可能低估 Glasswing 在专有代码中的实际发现能力，因此开源维护者应谨慎解读 VulnCheck 的“不尽如人意”结论，避免仅凭开源数据否定其价值。

**「社区讨论」** 社区讨论存在分歧。pizlonator 高度评价其收到的 Fil-C 报告，认为质量达到专家水平且部分修复可直接使用；enthuseyourcurb 等则认为私有代码库中的严重问题不会被公开 CVE 数据反映，而 rurcliped 批评博客误用开源披露账目来评价 Glasswing。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vulncheck.com/blog/anthropic-glasswing-november-update">After 7-months, Glasswing Overwelms Maintainers with ...</a></li>
<li><a href="https://news.lavx.hu/article/vulncheck-tracks-slow-fixes-and-few-exploits-in-anthropic-s-glasswing-project">VulnCheck tracks slow fixes and few exploits in Anthropic’s ...</a></li>
<li><a href="https://agihunt.info/en/p/1a1c7b1cf1d907d86a0ab5327d2">After 7 Months, Anthropic&#x27;s Glasswing Overwhelms… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#AI security`, `#vulnerability discovery`, `#Anthropic`, `#Glasswing`, `#software security`

---

<a id="item-tech-news-6"></a>
### [Val Town 云编程平台宣布关停](https://blog.val.town/winding-down) ⭐️ 7.0/10

Val Town，一个基于 Deno 的云端编程平台，已宣布正在逐步结束运营。这一变动影响其现有用户，并再次凸显终端用户编程领域商业化的长期困难。该平台采用 Deno 运行时和无服务器 JavaScript 架构；社区评论还提到，Deno 团队在加入 Cloudflare 后将于明年停止维护该运行时。部分社区成员预计 Val Town 的代码将在 2 月开源，这或许能为用户提供自托管途径。

hackernews · tosh · 11月10日 17:31 · [社区讨论](https://news.ycombinator.com/item?id=50443427)

**「背景」** Val Town 是一个基于 Deno 运行时的云端代码平台，让用户通过“Val”快速构建和托管小型脚本或 API。其依赖的 Deno 运行时本身正面临变化：Deno 核心维护团队宣布将停止维护，官方支持仅到 2027 年 10 月，并建议迁移到 Node、Bun、Cloudflare Workers 或 Vercel Functions。

**「影响」** Val Town 用户需要制定迁移计划；若代码如社区预期在 2 月开源，自托管可能成为延续使用的一种方式。

**「社区讨论」** 社区讨论普遍表示惋惜，并认为终端用户编程业务很难规模化；有评论指出 Val Town 围绕 Deno 构建，而 Deno 团队加入 Cloudflare 后的维护变化增加了不确定性，同时期待其代码开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://braindetox.kr/en/posts/val_town_winding_down.html">Val Town Winding Down: Dec 10 Read-Only and Jan 10 End</a></li>

</ul>
</details>

**标签**: `#val-town`, `#deno`, `#shutdown`, `#serverless`, `#end-user-programming`

---

<a id="item-tech-news-7"></a>
### [Chrome 等发布面向 AI 编码代理的现代 Web 平台指南 1.0](https://github.com/GoogleChrome/modern-web-guidance) ⭐️ 7.0/10

Google Chrome 与 Firefox、MDN 和 Edge 合作发布了开源集合 modern-web-guidance 1.0，包含 200 余篇约 1.7MB 的人工整理指南，帮助 AI 编码代理使用 CSS.highlights、&lt;dialog&gt;/showModal\(\)、field-sizing 等现代 Web 平台原语，而不是过时的 &lt;div&gt;+JS 模式。该发布同时提供可作为代理技能和 RAG CLI 使用的 npm 包，纯 JS 包约 7MB，CPU 上搜索约 10 毫秒；legacy-scan 在 3 万个 GitHub 仓库上训练，留出仓库平均精确率 92%。在 200 个任务、约 1700 条 Playwright/AST 断言的评测中，Codex、Claude 和 AGY 未使用指南时通过率为 55%，使用后达到 92%。用户可通过 npx modern-web-guidance@latest install/search/legacy-scan 使用。

hackernews · paulirish · 11月10日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50443812)

**「背景」** 许多编码代理虽然知道部分新 API 名称，但默认仍生成基于 &lt;div&gt; 和 JavaScript 的传统实现，例如手动管理对话框焦点和文本高亮。近年浏览器已原生支持 &lt;dialog&gt; 与 showModal\(\)、CSS.highlights、field-sizing 等功能，可减少代码量和依赖，但模型缺少足够的领域知识来优先采用这些方案。

**「影响」** 对于使用前端编码代理的开发者，该指南可使相关代理任务的评测通过率从 55% 提高到 92%；但部分推荐特性仅在 Chrome 稳定支持，Firefox 和 Safari 尚未支持，直接采用可能产生跨浏览器兼容风险。

**「社区讨论」** 评论区有人列出 CSS @function、calc-size\(\)、:target-current 等仅 Chrome 稳定的特性，担心代理过度采纳会导致“请使用主导浏览器”的回潮；也有用户建议以 GitHub Pages 发布纯 Markdown 索引以便不安装即可检索，另有人肯定其与 React 被视为遗留技术的讨论相呼应。

**标签**: `#web development`, `#coding agents`, `#browser APIs`, `#open source`, `#developer tools`

---

<a id="item-tech-news-8"></a>
### [AI 编程生成脆弱代码库引发开发者争论](https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/) ⭐️ 7.0/10

这篇文章认为，AI 辅助编码倾向于生成脆弱、难以维护的代码库，并可能降低开发者对代码的理解。该观点在 Hacker News 上引发了大量讨论，开发者对 AI 生成代码的可维护性存在明显分歧。部分评论者以自身经验反驳称已完全转向 AI 编码并认为其具有商业价值，另一些则指出文章所列的浅层测试、过度复杂等问题并非 AI 独有，并强调需要确定性评审和质量门禁来约束 AI 输出。

hackernews · plun9 · 11月10日 10:25 · [社区讨论](https://news.ycombinator.com/item?id=50438318)

**「背景」** AI 辅助编码指开发者使用大型语言模型或编码代理（如 GitHub Copilot、Cursor 等）根据自然语言提示生成或修改代码。所谓“脆弱代码库”通常指结构混乱、测试薄弱、重复逻辑多、难以定位故障且改动风险高的软件系统；文章作者认为，过度依赖 AI 生成代码会加剧这些问题，因为模型可能倾向快速产出表面可运行的代码，而忽视长期可维护性。这一背景源于近年来生成式 AI 在开发流程中的快速普及，使得代码质量与开发效率的权衡成为软件工程讨论的焦点。

**「社区讨论」** 社区评论显示明显分歧：有 20 多年经验的工程师称已 100%使用 AI 编码，认为这是保持竞争力的必要方式；也有评论者指出文章可能过时，并提到 Astra、Fable 5.1/Opus 5.5 等新模型已改善浅层测试问题。多位评论者认为，维护性问题同样存在于人类代码中，更有效的做法是建立对抗性评审、复杂度指标等确定性门禁，而不是一概否定 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://evanxmerz.com/post/ai-usage-generates-a-fragile-codebase/">AI usage generates a fragile codebase</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#software maintainability`, `#code quality`, `#developer tools`, `#tech industry`

---

<a id="item-tech-news-9"></a>
### [llm-gemini 0.36 发布：Gemini 4 Carbon 全面开放](https://simonwillison.net/2026/Nov/10/llm-gemini/) ⭐️ 7.0/10

llm-gemini 0.36 插件更新已发布。Gemini 4 Carbon 在两周前仅向部分网络防御者开放后，现已面向所有用户提供。该模型被 Simon Willison 称为 Google 有史以来最好的 Gemini，首发价格为每百万输入 token 2 美元、每百万输出 token 10 美元（与 GPT-6.1 Sol / Claude Sonnet 5.5 价格相当），但计划于 12 月 1 日翻倍至 4 美元 / 20 美元（与 Opus 5.5 相同）。Simon Willison 测试了低、中、高思考强度的三只鹈鹕图像，并用 Google Antigravity IDE 让该模型生成基于 OpenStreetMap 数据的 Yonkers 机甲动画。此外，他还提到一个 YouTube 视频展示 Carbon 使用 /swarm 功能协调子代理构建浏览器 3D 游戏。

rss · Simon Willison · 11月10日 20:09

**「背景」** Gemini 4 Carbon 是 Google 的新一代 Gemini 模型，最初两周前仅向网络防御者子集开放，现在向所有用户开放。llm-gemini 0.36 是 Simon Willison 发布的插件更新。

**「影响」** 开发者现在可以通过 llm-gemini 0.36 以 $2/$10 的每百万 token 价格使用 Gemini 4 Carbon，但需在 12 月 1 日前部署才能享受首发价，之后价格将翻倍至 $4/$20。

**标签**: `#AI`, `#LLM`, `#Gemini`, `#software tools`, `#pricing`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国汽油均价跌破每加仑 4 美元 为 7 月以来首次](https://www.cnbc.com/2026/11/10/us-gas-prices-below-four-dollars.html) ⭐️ 8.0/10

美国普通汽油全国均价周二降至每加仑 3.9788 美元，为 7 月以来首次跌破 4 美元，数据来自 AAA。

rss · CNBC Finance · 11月10日 16:29

**「背景」** 这一降幅发生在原油价格回落和能源通胀放缓之后：布伦特原油周二一度跌破每桶 90 美元（8 月以来首次），10 月能源价格环比涨幅从 9 月的 5.2%降至 0.7%。

**「影响」** 美国驾车者短期内可能减少加油支出，但美联储理事沃勒提醒称，能源价格对通胀的最终影响取决于价格能维持多久。

**标签**: `#gas prices`, `#inflation`, `#crude oil`, `#consumer spending`, `#Federal Reserve`

---

<a id="item-finance-news-2"></a>
### [美联储理事沃勒：倾向 12 月加息，或考虑 50 个基点](https://www.cnbc.com/2026/11/10/fed-governor-waller-sees-december-hike-likely.html) ⭐️ 8.0/10

美联储理事沃勒表示倾向于在 12 月加息，若通胀数据高于预期会考虑加息 50 个基点（0.5 个百分点）；周二公布的 10 月消费者价格指数整体上涨 0.4%，核心指数上涨 0.3%，均比预期高 0.1 个百分点。

rss · CNBC Finance · 11月10日 17:13

**「背景」** 此前美联储 9 月加息 25 个基点，10 月会议按兵不动且并非一致通过，沃勒称若不兑现加息承诺将有损央行信誉。

**标签**: `#Federal Reserve`, `#interest rates`, `#monetary policy`, `#inflation`, `#financial markets`

---

<a id="item-finance-news-3"></a>
### [Polymarket 年化收入突破 18 亿美元](https://www.cnbc.com/2026/11/10/polymarket-annualized-revenue-us-growth.html) ⭐️ 7.0/10

Polymarket 表示，按当前水平折算的全年收入已超过 18 亿美元，高于 6 月披露的 10 亿美元。

rss · CNBC Finance · 11月10日 13:00

**「背景」** 该公司 6 月时披露的年化收入运行率超过 10 亿美元，当时其美国交易所在 5 月上线；10 月该美国交易所的名义交易量达 145 亿美元，高于 6 月的 40 亿美元。

**标签**: `#Polymarket`, `#prediction markets`, `#revenue growth`, `#CFTC investigation`, `#funding round`

---