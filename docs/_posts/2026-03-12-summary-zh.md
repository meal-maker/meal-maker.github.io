---
layout: default
title: "Horizon Summary: 2026-03-12 (ZH)"
date: 2026-03-12
lang: zh
---

> From 16 items, 12 important content pieces were selected

---

1. [Temporal API 历经九年终完成，旨在修复 JavaScript 的 Date 对象](#item-1) ⭐️ 8.0/10
2. [Mozilla 推进 WebAssembly 成为 Web 一级语言。](#item-2) ⭐️ 8.0/10
3. [许多通过 SWE-bench 测试的 AI 生成 PR 不会被合并](#item-3) ⭐️ 8.0/10
4. [谷歌完成以 320 亿美元收购网络安全公司 Wiz 的交易。](#item-4) ⭐️ 8.0/10
5. [PNAS 论文调查促进大规模科学欺诈的实体（2025 年）。](#item-5) ⭐️ 8.0/10
6. [Hacker News 禁止 AI 生成评论以维护人类对话。](#item-6) ⭐️ 7.0/10
7. [AI 机器人面试个人经历引发伦理争议](#item-7) ⭐️ 7.0/10
8. [Site Spy：监控网页变化并通过 RSS 曝光的工具](#item-8) ⭐️ 7.0/10
9. [MacBook Neo 以硬件优势引发 PC 行业震动](#item-9) ⭐️ 7.0/10
10. [微软发布 BitNet 推理框架，支持在 CPU 上高效运行 1.58 位大语言模型。](#item-10) ⭐️ 7.0/10
11. [OpenClaw Beta 版 v2026.3.11 修复 WebSocket 劫持漏洞并新增 AI 模型试用](#item-11) ⭐️ 6.0/10
12. [s@ 协议：基于静态站点的去中心化社交网络](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Temporal API 历经九年终完成，旨在修复 JavaScript 的 Date 对象](https://bloomberg.github.io/js-blog/post/temporal/) ⭐️ 8.0/10

经过九年的开发，Temporal API 这一新的 JavaScript 日期和时间 API 现已在 ECMAScript 中标准化，旨在全面替代有问题的内置 Date 对象。它通过区分瞬间和日历日期，强制明确处理时间复杂性。 这很重要，因为它解决了 JavaScript 中影响所有 Web 开发者的一个根本痛点，减少了与时区、夏令时和日期处理歧义相关的常见错误，从而提升了全球应用的可靠性。 Temporal 引入了不可变对象和一个类似 Math 的顶级命名空间，使得 API 更冗长但更不易出错；然而，Temporal 对象不是纯 JSON，这在某些架构中可能会使序列化和反序列化复杂化。

hackernews · robpalmer · Mar 11, 15:35

**背景**: JavaScript 的 Date 对象长期以来因对时区和夏令时的处理不当而受到批评，常常导致应用中出现错误。时区是具有统一时间的区域，而夏令时涉及为节能而进行的季节性时钟调整。瞬间代表一个特定的时间点，而日历日期是日历上的一个日期，混淆两者可能导致日期时间计算中的错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tc39/proposal-temporal">GitHub - tc39/proposal-temporal: Provides standard objects and functions for working with dates and times. · GitHub</a></li>
<li><a href="https://tc39.es/proposal-temporal/docs/">Temporal documentation</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户赞扬 Temporal 强制明确处理时间复杂性并防止了如夏令时错误等常见问题。然而，也存在对 API 设计的批评，例如序列化问题，以及与其他语言如 Python 和 Java 中类似历史努力的比较。

**标签**: `#JavaScript`, `#Time Handling`, `#Software Engineering`, `#Web Development`, `#API Design`

---

<a id="item-2"></a>
## [Mozilla 推进 WebAssembly 成为 Web 一级语言。](https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/) ⭐️ 8.0/10

Mozilla 详细阐述了包括提议的 WebAssembly 组件模型在内的多项努力，以提升 WebAssembly 在 Web 上的集成度和性能，旨在将其从'二级'地位提升。该倡议着重于改善对 Web API 的直接访问，并减少中间代码的需求。 这一进展至关重要，因为它可以显著简化 Web 开发，使应用程序在浏览器中实现接近本地的性能，并允许更多编程语言在网络上高效使用，从而将生态系统扩展到 JavaScript 之外。它解决了长期存在的集成挑战，这些挑战限制了 WebAssembly 在复杂 Web 项目中的采用。 一个关键的技术细节是 WebAssembly 组件模型，它旨在标准化模块之间的互操作性并减少'胶水'代码，不过当前的工具链复杂性仍然是开发者的一个障碍。该提案寻求改善 WebIDL 支持和 DOM 访问，这些一直是历史上的痛点。

hackernews · mikece · Mar 11, 04:44

**背景**: WebAssembly (Wasm) 是一种二进制指令格式，被设计为 C++和 Rust 等编程语言的便携式编译目标，使它们能够在网络上与 JavaScript 一起高速运行。传统上，它在沙箱环境中运行，与 Web API 的直接交互有限，Mozilla 领导的这项努力旨在通过更好地将 Wasm 与 Web 标准集成来改变这一点。了解这一背景对于理解使其成为'一级'语言为何涉及提升其在 Web 平台上的原生能力至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://webassembly.org/">WebAssembly</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly - MDN Web Docs - Mozilla</a></li>
<li><a href="https://www.infoworld.com/article/4140823/webassembly-proposal-touted-to-improve-wasm-web-integration.html">WebAssembly proposal touted to improve Wasm web integration - InfoWorld</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示了对 WebAssembly 组件模型在简化跨语言互操作性方面潜力的热情，但也强调了对其工具链复杂性（被称为'WASM 悬崖'）的担忧，以及对 Web 集成历史延误的沮丧。一些评论者建议进一步将 Web API 分解为更小的子集，以增强灵活性并避免强制混合呈现和应用逻辑。

**标签**: `#WebAssembly`, `#Web Development`, `#Programming Languages`, `#Performance`

---

<a id="item-3"></a>
## [许多通过 SWE-bench 测试的 AI 生成 PR 不会被合并](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/) ⭐️ 8.0/10

分析指出，许多通过 SWE-bench 测试的 AI 生成的拉取请求不会被合并到主代码库中，原因是代码结构差且不符合人类编码习惯。 这揭示了当前评估 AI 软件工程能力的基准测试的关键缺陷，因为通过测试并不能保证代码质量或合并价值，影响了 AI 代码生成工具在实际应用中的评估方式。 AI 生成的代码通常在功能上有效，但引入了不必要抽象、奇怪流程和偏离现有项目模式等问题，使得人类难以维护和集成。

hackernews · mustaphah · Mar 11, 20:56

**背景**: SWE-bench 是一个基准测试，用于评估大语言模型通过生成代码补丁解决真实 GitHub 问题的能力。它通过在隔离的 Docker 容器中测试生成的代码是否通过现有测试，来模拟软件工程任务。该基准包含来自开源项目的任务，以衡量 AI 在实际场景中的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/SWE-bench/SWE-bench">SWE-bench: Can Language Models Resolve Real-world Github Issues?</a></li>
<li><a href="https://openai.com/index/introducing-swe-bench-verified/">Introducing SWE-bench Verified - OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍同意，通过 SWE-bench 的 AI 生成代码通常缺乏类人的结构和可维护性，有关于奇怪代码流程的轶事，并建议采用差异大小或抽象深度等替代评估指标。

**标签**: `#AI Code Generation`, `#Software Engineering`, `#Benchmarks`, `#Code Quality`

---

<a id="item-4"></a>
## [谷歌完成以 320 亿美元收购网络安全公司 Wiz 的交易。](https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz) ⭐️ 8.0/10

谷歌已正式完成以 320 亿美元收购网络安全公司 Wiz 的交易，确认了此前于 2025 年 3 月宣布的协议。 此次收购是谷歌加强其云安全能力的重大战略举措，可能改变市场动态并加剧云行业的竞争，同时也引起了人们对网络安全领域伦理问题的关注。 Wiz 的安全平台具有云无关性，通过 API 集成提供跨云资源的广泛覆盖且不中断运营，但被谷歌收购后，其中立性能否保持将是维护其价值的关键因素。

hackernews · aldarisbm · Mar 11, 14:58

**背景**: Wiz 是一个云原生安全平台，通过 API 连接快速部署和集成，帮助组织保护云工作负载，包括 PaaS 资源、虚拟机和容器。它旨在弥合开发与安全团队之间的差距，实现跨云环境可扩展且民主化的安全防护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/platform">Wiz cloud security platform | Wiz - Cool</a></li>
<li><a href="https://assets-global.website-files.com/60c0e55050c1de3103a2ccc7/6111d76d5a21365c167b80e6_DS_Wiz-Cloud-Security-Platform_060721.pdf">Wiz Cloud Security Platform</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对涉及 Wiz 投资者贿赂指控的伦理担忧，对谷歌长期承诺的怀疑（提及可能关闭服务），以及对以色列经济影响和 Wiz 云无关方法战略重要性的观察。

**标签**: `#acquisitions`, `#cybersecurity`, `#google`, `#cloud-computing`, `#business-ethics`

---

<a id="item-5"></a>
## [PNAS 论文调查促进大规模科学欺诈的实体（2025 年）。](https://doi.org/10.1073/pnas.2420092122) ⭐️ 8.0/10

2025 年发表在《美国国家科学院院刊》（PNAS）上的一篇论文调查了促进大规模科学欺诈的实体，探讨了研究出版中的促成因素和挑战。 这项研究意义重大，因为它揭露了学术出版中威胁科学完整性的系统性漏洞，可能导致资金浪费、政策缺陷并削弱对研究结果的信任。 该研究强调了期刊实践（如拒绝发表重复研究）和指标驱动激励（如古德哈特定律）如何助长欺诈。社区评论指出，由于有组织的网络和潜在的国家支持，检测面临挑战。

hackernews · peyton · Mar 11, 13:32

**背景**: 科学欺诈通常涉及数据捏造（创建虚假数据）或篡改（更改真实数据）。论文工厂是商业实体，利用学术界的发表压力大规模生产和销售欺诈性研究论文。同行评审操纵可能发生在评审过程受损以接受此类欺诈性工作时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Research_paper_mill">Research paper mill - Wikipedia</a></li>
<li><a href="https://blog.mdpi.com/2022/05/09/paper-mills/">Paper Mills—The Dark Side of the Academic Publishing Industry</a></li>
<li><a href="https://scientific-publishing.webshop.elsevier.com/manuscript-review/research-fraud-falsification-and-fabrication-research-data/">Research Fraud: Falsification and Fabrication of Data - Elsevier</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了对学术界系统性问题的广泛关注。关键观点包括批评期刊不发表重复研究或阴性结果的研究，引用古德哈特定律解释指标驱动的欺诈，个人遭遇欺诈论文的轶事，以及观察到与潜在欺诈相关的排名异常。

**标签**: `#scientific-fraud`, `#academia`, `#research-integrity`, `#publishing`, `#ethics`

---

<a id="item-6"></a>
## [Hacker News 禁止 AI 生成评论以维护人类对话。](https://news.ycombinator.com/newsguidelines.html#generated) ⭐️ 7.0/10

Hacker News 已明确更新其社区指南，禁止发布 AI 生成或经过大量 AI 编辑的评论，如其 newsguidelines.html 中所述。这一变化正式确立了一条规则，旨在防止非人类贡献，以维护平台上的真实对话。 这项政策之所以重要，是因为它应对了日益增长的担忧，即 AI 生成内容可能侵蚀在线社区中人类互动的真实性和质量，为其他技术论坛树立了先例。它还引发了关于 AI 在社交平台中的作用以及内容审核策略的更广泛讨论。 该指南特别针对“生成/AI 编辑的评论”，并且是 Hacker News 官方规则的一部分，引发了社区的高度参与，获得超过 3100 点积分和 1170 条评论。执行依赖于社区举报和审核，因为 AI 内容检测工具仍不完善，其准确性存在争议。

hackernews · usefulposter · Mar 11, 19:29

**背景**: AI 生成的评论通常使用基于 transformer 架构的大型语言模型（LLM）生产，例如 OpenAI 的 GPT 系列，这些模型在庞大数据集上训练，以生成类似人类的文本。Transformer 模型作为深度学习中的架构，实现了先进的自然语言生成能力，驱动了许多生成式 AI 工具。作为应对，AI 内容检测算法已被开发出来以识别非人类文本，尽管其在在线论坛中的可靠性参差不齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/transformer-model">What is a Transformer Model? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示对该规则总体持支持态度，用户重视维护人类对话，并表达了对 AI 可能平均化创造力的担忧。关键观点包括建议 AI 工具应协助而非取代人类写作，以及批评 Hacker News 投资 AI 公司所带来的讽刺性。

**标签**: `#AI Ethics`, `#Community Guidelines`, `#Online Forums`, `#Human-Computer Interaction`, `#Content Moderation`

---

<a id="item-7"></a>
## [AI 机器人面试个人经历引发伦理争议](https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job) ⭐️ 7.0/10

一位求职者分享了被 AI 机器人面试的第一人称经历，这引发了关于招聘自动化、AI 偏见和伦理问题的广泛讨论。这一个人叙述突显了 AI 系统在招聘流程中的实际应用。 这很重要，因为它突显了 AI 在招聘中日益广泛的应用，可能导致求职体验非人化，并加剧 AI 模型中嵌入的社会偏见，从而影响求职者的公平性和职场多样性。这关联到自动化重塑就业实践的更广泛趋势。 AI 面试机器人通常使用算法扫描简历，并分析视频回答中的表情、关键词和语调。然而，底层的大型语言模型（LLM）常基于包含历史偏见的互联网数据训练，这导致在候选者评估中存在不公平歧视的风险。

hackernews · speckx · Mar 11, 18:17

**背景**: AI 驱动的面试涉及自动化系统，如聊天机器人，使用自然语言处理和计算机视觉进行初步筛选以评估候选人。大型语言模型（LLM）是这些系统的关键组成部分，基于互联网海量文本语料库训练，这些数据可能反映并放大与性别、种族等因素相关的社会偏见。这一背景对于理解自动化招聘中的伦理和技术挑战至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/">AI tools show biases in ranking job applicants' names according to perceived race and gender - UW</a></li>
<li><a href="https://finance.yahoo.com/news/your-next-job-interview-might-be-with-an-ai-bot-heres-how-to-ace-it-180459573.html">Your next job interview might be with an AI bot. Here's how ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论整体持批评态度，用户表达了对招聘非人化、AI 系统内在偏见以及自动化面试负面体验的担忧。关键观点包括将求职比作非个人的在线约会、主张通过关系网络而非正式流程，以及对 AI 面试所谓好处的怀疑。

**标签**: `#AI-interviews`, `#hiring-ethics`, `#LLM-bias`, `#automation`

---

<a id="item-8"></a>
## [Site Spy：监控网页变化并通过 RSS 曝光的工具](https://sitespy.app/) ⭐️ 7.0/10

开发者创建了 Site Spy，这是一个浏览器扩展和网页仪表板，用于监控网页上特定元素的变化，并通过 RSS 源曝光更新。 这个工具之所以重要，是因为它实现了精确的元素级网页监控，为预约时段或价格变化等关键更新提供及时警报，减少干扰，并通过 RSS 和 AI 代理与现代工作流程集成。 关键功能包括用于针对性跟踪的元素选择器、带有快照历史的差异视图、每个监控的 RSS 源，以及通过 MCP 服务器与 AI 代理的集成，但处理 JavaScript 渲染的网站可能构成挑战。

hackernews · vkuprin · Mar 11, 16:21

**背景**: RSS（Really Simple Syndication）是一种网络源格式，允许用户订阅网站上的更新内容。MCP（Model Context Protocol）是一种开放标准，使如 Claude 和 Cursor 这样的 AI 应用能够通过一致的接口连接到外部工具和数据源。网页监控工具自动化跟踪网站变化，以无需手动检查即可通知用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@sonali.nogja.08/what-is-an-mcp-server-and-why-every-ai-agent-is-rushing-to-use-them-afb35e0bf901">What Is an MCP Server? (And Why Every AI Agent Is Rushing to Use Them) - Medium</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体上是积极的，用户赞赏该工具的执行和元素级跟踪，同时提出了对 JavaScript 渲染网站兼容性的担忧，并就 RSS 源与电子邮件通知等直接警报的实用性进行了辩论。

**标签**: `#web-monitoring`, `#rss`, `#browser-extension`, `#automation`, `#diff-tool`

---

<a id="item-9"></a>
## [MacBook Neo 以硬件优势引发 PC 行业震动](https://daringfireball.net/2026/03/the_macbook_neo) ⭐️ 7.0/10

华硕联合首席执行官表示，MacBook Neo 凭借其卓越的硬件和整合的软件对传统 PC 行业构成了巨大冲击，挑战了传统 x86 Windows 笔记本电脑的价值定位。 这件事之所以重要，是因为如果这款设备在中端市场重新设定了性价比预期，可能会迫使整个传统 PC 行业从根本上重新评估其产品策略。 值得注意的细节包括其缺少摄像头硬件指示灯，这引发了隐私担忧；以及尽管有人称其为“内容消费”设备，但它实际上是一台能胜任真正工作的机器。

hackernews · etothet · Mar 11, 11:37

**背景**: 讨论的核心是苹果转向使用其自研的基于 ARM 架构的处理器（Apple Silicon），这些处理器以每瓦高性能著称。Mac 的这一转型需要借助 Rosetta 2 等软件翻译层来运行为之前 Intel (x86) 架构构建的应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_architecture_family">ARM architecture family - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rosetta_(software)">Rosetta ( software ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要包含对传统 PC 市场碎片化的批评、关于苹果软件生态系统及其“围墙花园”模式的争论、反驳该设备仅为“内容消费”设备的观点，以及对摄像头指示灯等硬件隐私功能的具体担忧。

**标签**: `#Apple`, `#PC Industry`, `#Hardware`, `#Consumer Electronics`

---

<a id="item-10"></a>
## [微软发布 BitNet 推理框架，支持在 CPU 上高效运行 1.58 位大语言模型。](https://github.com/microsoft/BitNet) ⭐️ 7.0/10

微软开源了 BitNet，这是一个专为 1 位（技术上为 1.58 位或三元）大语言模型优化的推理框架（bitnet.cpp），据称能够在消费级 CPU 上高效运行参数高达 1000 亿的模型。然而，它只是一个推理框架和训练套件，并非一个预训练好的 100B 模型，且模型必须使用其架构从头开始训练。 这代表了向极致模型效率迈进的重要一步，可能使得大规模 AI 模型能够在内存和计算资源有限的设备（如个人电脑和边缘设备）上本地运行，而无需依赖强大的 GPU 或云服务。如果成功，它将使更多人能够使用先进的大语言模型，并加速高效、设备端 AI 的发展趋势。 BitNet b1.58 模型使用三元值（-1， 0， +1），实际上需要 2 位存储，这将矩阵乘法运算转换为加法运算，提供了对 CPU 有利的、根本不同的计算模式。社区分析指出，为了达到与标准 16 位模型相当的性能，1.58 位模型可能需要多 4-5 倍的参数；并且，虽然其推理速度可能快于训练后量化（PTQ）方法，但目前兼容的模型选择有限。

hackernews · redm · Mar 11, 12:27

**背景**: 模型量化是一种通过使用较低精度（如 8 位或 4 位整数）表示权重和激活值，来降低 AI 模型内存和计算成本的技术，用以替代标准的 32 位或 16 位浮点数。边缘计算是指在数据源附近（例如在智能手机或物联网设备上）处理数据，而不是在集中式的云端，这可以降低延迟并可能提高隐私性。传统的训练后量化（PTQ）会降低预训练模型的精度，而 BitNet 的方法则需要使用专为极低精度（1.58 位）设计的架构，从头开始训练一个新模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bitnet.live/">BitNet - Official Inference Framework for 1-bit LLMs | Microsoft</a></li>
<li><a href="https://github.com/microsoft/BitNet">GitHub - microsoft/BitNet: Official inference framework for 1 ...</a></li>
<li><a href="https://www.junia.ai/blog/bitnet-1-bit-model-local-ai-workflows">BitNet Explained: Why 1-Bit AI Models Matter in 2026</a></li>

</ul>
</details>

**社区讨论**: 社区讨论对新闻标题中“100B 参数 1 位模型”的说法表示质疑，澄清其仅是一个推理框架，而非训练好的模型。然而，人们对其技术方法表现出浓厚兴趣，特别是三元权重如何改变 CPU 上的计算动态，以及其相对于高位宽 PTQ 的潜在速度优势。讨论还包括技术澄清（例如，它实际使用 2 位而非 1 位，以及与生物神经网络的潜在类比）以及对“1 位”与“1.58 位”命名的困惑。

**标签**: `#model-quantization`, `#inference-optimization`, `#edge-computing`, `#machine-learning`, `#efficient-ai`

---

<a id="item-11"></a>
## [OpenClaw Beta 版 v2026.3.11 修复 WebSocket 劫持漏洞并新增 AI 模型试用](https://github.com/openclaw/openclaw/releases/tag/v2026.3.11-beta.1) ⭐️ 6.0/10

OpenClaw 发布了 2026.3.11-beta.1 版本，包含一个安全补丁，强制进行浏览器源验证以修复 `trusted-proxy` 模式下的跨站 WebSocket 劫持漏洞。此次更新还向 OpenRouter 模型目录添加了临时性的 'Hunter Alpha' 和 'Healer Alpha' AI 模型条目，引入了 iOS 主屏幕和 macOS 聊天界面的改进，并包含了多项其他功能和入门流程的增强。 WebSocket 安全修复至关重要，因为它堵上了一个可能允许不受信任的来源获得管理员操作员权限的漏洞，直接影响使用 OpenClaw 网关的部署安全。同时，添加临时的免费 AI 模型条目降低了用户试用新模型的门槛，符合将多样化 AI 能力更易获取并集成到开发者工具中的行业趋势。 跨站 WebSocket 劫持修复专门针对安全公告 GHSA-5wcw-8jjv-m286，并在处于 `trusted-proxy` 模式时应用于所有浏览器发起的连接。新增的 'Hunter Alpha' 和 'Healer Alpha' 模型条目仅在内置的 OpenRouter 目录中提供大约一周，这表明是一次短期试用或推广活动。

github · steipete · Mar 12, 04:23

**背景**: 跨站 WebSocket 劫持（CSWSH）是一种 Web 安全漏洞，攻击者可以通过恶意网站代表已认证的用户与存在漏洞的应用程序建立 WebSocket 连接。之所以可能发生这种情况，是因为 WebSocket 握手请求会自动包含用户 Cookie，但默认情况下不受同源策略（SOP）的约束。OpenRouter 是一个聚合了来自不同提供商的各种 AI 模型的平台，为开发者提供付费和免费选项以集成到其应用程序中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking">Cross-site WebSocket hijacking | Web Security Academy</a></li>
<li><a href="https://openrouter.ai/models">Models - OpenRouter</a></li>

</ul>
</details>

**标签**: `#security`, `#websocket`, `#ios`, `#ai-models`, `#github-release`

---

<a id="item-12"></a>
## [s@ 协议：基于静态站点的去中心化社交网络](http://satproto.org/) ⭐️ 6.0/10

s@（sAT）协议已被推出，通过在静态网站上以加密的 JSON 存储用户数据，并使用客户端加密和浏览器存储，实现去中心化社交网络。 该协议通过使用户能够在静态站点上拥有自己的数据，挑战了集中式社交媒体模式，有助于促进用户主权和抗审查能力的去中心化网络基础设施发展趋势。 关键技术特征包括使用 X25519 密钥对进行加密，并将私钥存储在浏览器的 localStorage 中，但这种方法因在长期数据持久性方面的易变性和不可靠性而受到批评。

hackernews · remywang · Mar 12, 00:22

**背景**: 去中心化社交网络协议，如 DSNP，旨在建立不依赖于特定应用或集中式平台的社交图谱。静态网站是预先构建的页面，无需服务器端处理即可提供，通常托管在 GitHub Pages 或 Netlify 等服务上。客户端加密涉及在用户浏览器中使用 JavaScript（通常通过 Web Crypto API）加密数据，以在没有后端服务器的情况下保护隐私。然而，浏览器存储机制如 localStorage 设计用于临时数据，容易被清除，对加密密钥等重要信息构成风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://satproto.org/">s @: social networking over static sites | sAT Protocol</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Client-side_storage">Client-side storage - Learn web development | MDN</a></li>
<li><a href="https://metafunctor.com/post/2026-02-13-pagevault/">pagevault: Client-Side Encryption for Static Sites | metafunctor</a></li>

</ul>
</details>

**社区讨论**: 社区讨论持批评态度，关注点包括过度依赖加密以及使用浏览器的 localStorage 存储私钥的不可靠性等可用性缺陷，用户还提出了改进建议，例如采用标准的 /.well-known/ URI 以提高互操作性。

**标签**: `#decentralization`, `#social-networking`, `#static-sites`, `#encryption`, `#web-protocol`

---