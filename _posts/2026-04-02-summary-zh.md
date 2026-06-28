---
layout: default
title: "Horizon Summary: 2026-04-02 (ZH)"
date: 2026-04-02
lang: zh
---

> From 16 items, 7 important content pieces were selected

---

1. [NASA 阿耳忒弥斯二号载人绕月任务发射日实时更新](#item-1) ⭐️ 8.0/10
2. [Scott Aaronson 的博客文章引发 Hacker News 对真实量子计算进展的辩论](#item-2) ⭐️ 8.0/10
3. [OCaml 编译器提议新增 C++ 后端](#item-3) ⭐️ 8.0/10
4. [Cloudflare 发布 EmDash Beta，一款安全的服务器 less CMS，旨在成为 WordPress 的继任者](#item-4) ⭐️ 8.0/10
5. [快速而美观的 GPU 友好型侵蚀滤镜发布](#item-5) ⭐️ 8.0/10
6. [DRAM 价格飙升正在扼杀爱好者单板计算机市场](#item-6) ⭐️ 7.0/10
7. [OpenClaw 发布了 v2026.3.31 版本，包含重大变更和更严格的安全默认设置。](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [NASA 阿耳忒弥斯二号载人绕月任务发射日实时更新](https://www.nasa.gov/blogs/missions/2026/04/01/live-artemis-ii-launch-day-updates/) ⭐️ 8.0/10

NASA 正在为阿耳忒弥斯二号任务的发射提供实时更新，这是阿耳忒弥斯计划中的首次载人绕月飞行。发射日活动正通过 YouTube 直播链接进行实时流媒体传输。 此次任务是一个关键里程碑，因为它代表了 50 多年来的首次载人月球任务，测试了未来阿耳忒弥斯着陆的关键系统，并推动了人类超越地球轨道的探索。它重新激发了全球对月球探索的兴趣，并为可持续的月球任务奠定了基础。 此次任务使用太空发射系统（SLS）超重型运载火箭和猎户座飞船，采用多次地月转移注入和自由返回轨道。根据社区评论，绕月飞行定于 4 月 6 日，溅落定于 4 月 10 日，未来的阿耳忒弥斯任务将依赖于像 Starship 推进剂转移这样的技术发展。

hackernews · apitman · Apr 1, 17:11

**背景**: 阿耳忒弥斯计划是 NASA 旨在让人类重返月球并最终前往火星的一项倡议，继阿波罗计划之后。它依赖于太空发射系统（SLS）——一种消耗性超重型运载火箭，以及为载人深空探索设计的猎户座飞船。阿耳忒弥斯二号是该计划中的首次载人任务，专注于绕月飞行以在后续任务尝试着陆前验证系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_program">Artemis program - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Space_Launch_System">Space Launch System - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orion_(spacecraft)">Orion (spacecraft) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区表达了广泛的兴奋和情感投入，用户分享了与孩子观看发射等个人经历，并对火箭高速等技术成就感到惊叹。讨论还包括对未来阿耳忒弥斯里程碑和商业太空努力的背景见解，反映出积极且投入的情绪。

**标签**: `#space-exploration`, `#nasa`, `#artemis`, `#launch`, `#human-spaceflight`

---

<a id="item-2"></a>
## [Scott Aaronson 的博客文章引发 Hacker News 对真实量子计算进展的辩论](https://scottaaronson.blog/?p=9665) ⭐️ 8.0/10

Scott Aaronson 的一篇博客文章强调了量子计算领域真实、非恶作剧的进展，引发了一场详细的 Hacker News 讨论，社区成员分享了现实世界的经验并辩论了其影响。 这次讨论之所以重要，是因为它将一位领先量子计算研究人员的权威见解与社区的实际观点相结合，揭示了新兴量子技术带来的实际进展、局限性以及紧迫的密码学威胁。 关键细节包括社区对量子技术近期实用性的怀疑，对当前易出错的 NISQ（嘈杂中型量子）设备的引用，以及量子计算机可能破解比特币等密码系统的具体担忧，这引发了对后量子升级的呼吁。

hackernews · Strilanc · Apr 2, 00:24

**背景**: 量子计算使用可以处于叠加态的量子比特（qubit），为某些问题提供了潜在的加速。NISQ 指的是当前量子计算时代，设备拥有最多 1000 个量子比特，但存在噪声且不具备容错能力。后量子密码学涉及开发能抵抗量子攻击的算法，NIST 正在标准化新方法以替代易受攻击的经典密码学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noisy_intermediate-scale_quantum_computing">Noisy intermediate-scale quantum computing - Wikipedia</a></li>
<li><a href="https://www.nist.gov/pqc">Post - quantum cryptography | NIST</a></li>

</ul>
</details>

**社区讨论**: 讨论揭示了复杂的情绪，包括对量子计算实际价值的怀疑，行业专业人士对当前软硬件局限性的见解，以及关于加密货币易受量子攻击脆弱性的辩论，突显了在比特币硬分叉等升级紧迫性上的分歧。

**标签**: `#quantum-computing`, `#cryptography`, `#research`, `#software-engineering`

---

<a id="item-3"></a>
## [OCaml 编译器提议新增 C++ 后端](https://github.com/ocaml/ocaml/pull/14701) ⭐️ 8.0/10

一项 GitHub pull request（#14701）提议为 OCaml 编译器（ocamlc）添加一个新的 C++ 后端。该提案由贡献者 Stephen Dolan 提交。 此举可极大简化将 OCaml 代码嵌入现有 C++ 项目的过程，消除链接标准 OCaml C 运行时库的障碍。这代表着 OCaml 为提升互操作性及其在以 C++ 为主导的行业中的采用率而采取的一项战略性举措。 该新后端将生成 C++ 代码（很可能通过某种中间表示）来生成可执行文件。讨论中提出的一个关键问题是，其性能（尤其是在长时间运行的进程中）与现有的原生代码编译器（ocamlopt）相比如何。

hackernews · glittershark · Apr 1, 23:35

**背景**: OCaml 是一种静态类型、多范式的编程语言，以其类型安全和性能而闻名。标准的 OCaml 发行版包含两个主要编译器：生成字节码的 ocamlc 和生成优化原生机器码的 ocamlopt。目前，OCaml 主要通过 C 语言外部函数接口（FFI）与其他语言进行互操作，这在处理 C++ 时可能很复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OCaml">OCaml - Wikipedia</a></li>
<li><a href="https://ocaml.org/docs/using-the-ocaml-compiler-toolchain">Using the OCaml Compiler Toolchain · OCaml Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极且充满兴趣。评论者强调了此举可能使 OCaml 更易于嵌入 C++ 代码库，并讨论了技术影响，包括与原生后端的性能比较以及 C++ 中缺少尾调用优化。一位用户幽默地称赞了该后端在计算素数时的高效性。

**标签**: `#OCaml`, `#Compiler`, `#C++`, `#Programming Languages`, `#Interoperability`

---

<a id="item-4"></a>
## [Cloudflare 发布 EmDash Beta，一款安全的服务器 less CMS，旨在成为 WordPress 的继任者](https://blog.cloudflare.com/emdash-wordpress/) ⭐️ 8.0/10

Cloudflare 发布了 EmDash 的 beta 版本，这是一个基于 Astro 6.0 构建的全栈、服务器 less JavaScript/TypeScript CMS。其核心创新在于一个插件系统，插件在安全沙盒化的 Worker 隔离环境中运行，直接解决了 WordPress 插件架构的根本性安全漏洞。 这之所以重要，是因为 WordPress 支撑着超过 40% 的网站，而其庞大的插件生态系统是安全漏洞的主要来源。像 EmDash 这样一个现代、安全且可扩展的替代方案，可能会改变开发者的实践，并为构建网站提供更强大的基础，特别是如果它能在生态系统中获得关注的话。 EmDash 完全使用 TypeScript 编写，采用服务器 less 架构但也可以运行在自有硬件或任何平台上，底层使用 Astro 框架以保证性能。其沙盒机制通过 Cloudflare 的 Dynamic Workers 实现，将插件代码与核心系统以及其他插件隔离开来。

hackernews · elithrar · Apr 1, 16:14

**背景**: WordPress 是一个占据主导地位但已显老态的内容管理系统，以其庞大的插件生态系统而闻名，但这同时也带来了巨大的安全风险，因为插件通常拥有对服务器的完全访问权限。Astro 是一个现代的 Web 框架，专注于使用 "Islands Architecture"（岛屿架构）构建快速的内容驱动型网站，该架构默认只发送极少或不发送客户端 JavaScript。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/emdash-wordpress/">Introducing EmDash — the spiritual successor to WordPress ...</a></li>
<li><a href="https://github.com/emdash-cms/emdash">GitHub - emdash-cms/emdash · GitHub</a></li>
<li><a href="https://astro.build/">Astro</a></li>

</ul>
</details>

**社区讨论**: 讨论显示出观点分歧。一些开发者（如 earthlingdavey）非常赞同其技术方案，赞扬其使用 TypeScript 和沙盒化 Workers 来保障安全。另一些开发者（如 rcarr）则对它的采用前景持怀疑态度，认为 WordPress 的成功源于其网络效应和易用性，而新的技术方案可能无法克服这些障碍。

**标签**: `#CMS`, `#web-security`, `#TypeScript`, `#serverless`, `#WordPress`

---

<a id="item-5"></a>
## [快速而美观的 GPU 友好型侵蚀滤镜发布](https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html) ⭐️ 8.0/10

图形开发者 Rune 发布了一种新颖的侵蚀滤镜技术，无需复杂模拟即可生成逼真的分支沟壑和山脊。该技术的核心在于支持孤立点评估，这使其速度极快、对 GPU 友好，并且可以轻松应用于基于分块的地形生成。 这一突破对于视频游戏和虚拟世界等实时应用意义重大。在这些领域中，高质量的程序化生成地形非常受欢迎，但模拟侵蚀等自然过程的计算成本往往成为瓶颈。该滤镜为实现逼真的侵蚀特征提供了一条快速路径，有望简化地形设计的工作流程。 该技术是早期"Clean Terrain Erosion Filter"的演进，可以作为后处理滤镜应用于任何现有的高度函数。其独立评估每个点的能力使其在 GPU 上极易并行化，非常适合以可管理的分块来生成大规模地形。

hackernews · runevision · Mar 31, 08:41

**背景**: 在计算机图形学中，地形侵蚀是为程序化生成的地貌增添真实感的关键过程，它通常模拟水和沉积物随时间推移如何塑造地表。传统的模拟方法，如水力侵蚀，计算成本高昂，难以实时运行。程序化地形生成常使用噪声函数和算法来创建地形，而如何高效地添加逼真的侵蚀效果，以实现自然的外观，一直是一个长期的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://80.lv/articles/fast-terrain-erosion-filter-that-emulates-erosion-without-simulation">GPU -Friendly Advanced Terrain Erosion Filter</a></li>
<li><a href="https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html">Fast and Gorgeous Erosion Filter - runevision</a></li>

</ul>
</details>

**社区讨论**: 社区反响极为积极，评论称赞该技术是"圣杯"，是地形生成的一次重大升级。用户们强调了它在交互式 Shadertoy 演示中的出色性能，并讨论了其在 3D 游戏中实现更真实、更有趣的随机地图的潜力，并将其与《矮人要塞》等广受喜爱的系统进行了比较。

**标签**: `#graphics`, `#terrain-generation`, `#game-development`, `#procedural-generation`, `#shaders`

---

<a id="item-6"></a>
## [DRAM 价格飙升正在扼杀爱好者单板计算机市场](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/) ⭐️ 7.0/10

DRAM 价格上涨显著提高了单板计算机（如 Raspberry Pi）的成本，降低了其对于爱好者和开发者的可负担性。 这影响了创客社区，限制了用于教育、原型设计和创新的廉价硬件的获取，可能延缓技术学习和项目开发。 值得注意的是，Raspberry Pi 4 4GB 型号的价格已从 2020 年的约 62 美元飙升至目前的 117 美元以上，行业分析预测了更广泛的市场影响，包括智能手机销量可能下降。

hackernews · ingve · Apr 1, 21:36

**背景**: DRAM（动态随机存取存储器）是一种用于临时数据存储的常见计算机内存，需要定期刷新。单板计算机（SBC）是集成在单板上的计算设备，广泛被爱好者用于 DIY 项目，其中 Raspberry Pi 是突出代表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Random-access_memory">Random - access memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single-board_computer">Single-board computer - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪对成本上升表示担忧，讨论中强调优化代码而非增加 RAM，引用了智能手机市场萎缩的预测，并指出氦气短缺等额外供应链挑战。

**标签**: `#DRAM`, `#Single-Board Computers`, `#Hardware Pricing`, `#Tech Market`, `#Hobbyist Electronics`

---

<a id="item-7"></a>
## [OpenClaw 发布了 v2026.3.31 版本，包含重大变更和更严格的安全默认设置。](https://github.com/openclaw/openclaw/releases/tag/v2026.3.31) ⭐️ 6.0/10

v2026.3.31 版本移除了重复的 nodes.run shell 包装器，弃用了旧版插件 SDK 兼容路径，并默认阻止含有严重危险代码发现的安装。 这很重要，因为它通过默认阻止不安全插件安装来增强安全性，保护用户免受潜在风险，并通过逐步淘汰弃用的 SDK 路径来现代化插件生态系统。 关键细节包括节点命令现在需要在设备配对后明确批准才能启用，并且由于更严格的安全扫描，安装可能会失败，除非使用如 --dangerously-force-unsafe-install 的标志进行覆盖。

github · steipete · Mar 31, 20:54

**背景**: OpenClaw 是一个个人 AI 代理平台，它将接口层与执行运行时分离，使用节点执行远程任务，插件用于扩展功能。插件 SDK 已从旧版兼容路径迁移到现代、文档化的入口点，如 openclaw/plugin-sdk/*。安全更新现在包括内置的危险代码扫描，默认在发现严重问题时阻止安装，以解决插件供应链安全性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.openclaw.ai/nodes">Nodes - OpenClaw</a></li>
<li><a href="https://docs.openclaw.ai/plugins/sdk-migration">Plugin SDK Migration - OpenClaw</a></li>
<li><a href="https://phemex.com/news/article/openclaw-update-enhances-security-with-default-install-block-on-critical-findings-70123">OpenClaw Update Blocks Unsafe Installs by Default | Phemex News</a></li>

</ul>
</details>

**标签**: `#cli`, `#plugin-sdk`, `#security`, `#software-update`

---