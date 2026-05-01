---
layout: default
title: "Horizon Summary: 2026-05-01 (ZH)"
date: 2026-05-01
lang: zh
---

> From 21 items, 12 important content pieces were selected

---

1. [CopyFail 漏洞披露争议暴露内核安全流程缺陷](#item-1) ⭐️ 9.0/10
2. [Claude Code 拒绝请求或因提及 'OpenClaw' 额外收费](#item-2) ⭐️ 9.0/10
3. [Rivian 推出禁用车辆全部互联网连接的选项](#item-3) ⭐️ 8.0/10
4. [马克·克莱因揭露 NSA 房间 641A 内幕](#item-4) ⭐️ 8.0/10
5. [Opus 4.7 可通过写作风格去匿名化作者](#item-5) ⭐️ 8.0/10
6. [PyTorch Lightning 依赖中发现 Shai-Hulud 恶意软件](#item-6) ⭐️ 8.0/10
7. [Honker：通过元数据轮询在 SQLite 中实现队列、发布/订阅和定时任务](#item-7) ⭐️ 8.0/10
8. [10GbE 家庭网络部署实践指南](#item-8) ⭐️ 8.0/10
9. [OpenClaw v2026.4.29-beta.2：消息、记忆和提供商增强](#item-9) ⭐️ 7.0/10
10. [用 F#构建 Game Boy 模拟器：函数式编程实践](#item-10) ⭐️ 7.0/10
11. [比利时逆转核电站退役政策，延长运行](#item-11) ⭐️ 7.0/10
12. [炼油厂如何运作：技术深度解析](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [CopyFail 漏洞披露争议暴露内核安全流程缺陷](https://www.openwall.com/lists/oss-security/2026/04/30/10) ⭐️ 9.0/10

一个名为 CopyFail（CVE-2026-31431）的严重 Linux 内核权限提升漏洞在 oss-security 邮件列表上被公开披露，同时附带了可用的概念验证利用代码，而大多数 Linux 发行版维护者尚未收到或部署修复补丁。 此事件暴露了 Linux 内核安全团队与发行版维护者之间的沟通裂痕，可能导致数百万生产系统在补丁广泛部署之前仍暴露于本地提权攻击之下。这也重新引发了关于负责任披露以及内核项目是否需要更正式协调披露流程的讨论。 该漏洞（CVE-2026-31431）位于内核加密 API（AF_ALG）中，影响所有从 2017 年至补丁可用期间构建内核的主流 Linux 发行版。已有社区成员发布了一个基于 eBPF 的缓解措施，适用于 AF_ALG 直接编译进内核的系统。

hackernews · ori_b · Apr 30, 16:43

**背景**: CopyFail 是一个本地权限提升漏洞，利用 Linux 内核加密 API（AF_ALG）中的逻辑缺陷，可使非特权用户获得 root 权限。该漏洞由一名安全研究人员发现并向内核安全团队报告，但修复补丁未提前传达给发行版维护者，随后研究人员将漏洞细节和利用代码公开发布到 oss-security 邮件列表。这一事件引发批评，认为内核的漏洞披露流程不公平地将通知下游消费者的责任推给了报告者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cert.europa.eu/publications/security-advisories/2026-005/">CERT-EU - High Vulnerability in the Linux Kernel (" Copy Fail ")</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/2026/04/29/23">oss-security - CVE-2026-31431: CopyFail : linux local privilege scalation</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍批评当前的披露流程，许多人认为内核安全团队而非报告者应承担与发行版维护者协调的责任。一些评论者对共享托管环境在补丁部署前可能被利用表示担忧，而另一些则提供了技术缓解措施，如 eBPF 解决方案。反复出现的主题是呼吁内核项目改革其披露流程，确保发行版能及时收到通知。

**标签**: `#linux`, `#security`, `#vulnerability-disclosure`, `#kernel`, `#cybersecurity`

---

<a id="item-2"></a>
## [Claude Code 拒绝请求或因提及 'OpenClaw' 额外收费](https://twitter.com/theo/status/2049645973350363168) ⭐️ 9.0/10

用户发现，当提交消息或对话中出现 "OpenClaw" 一词时，Anthropic 的 AI 编码助手 Claude Code 要么拒绝响应，要么迅速消耗使用配额，暗示存在故意内容过滤。 这引发了对 AI 伦理、透明度以及 Anthropic 潜在反竞争行为的严重担忧，因为屏蔽对竞争性开源工具的提及会损害用户对 AI 辅助开发的信任，并可能违反公平使用原则。 多位用户复现了该问题：一名用户报告在包含 "openclaw" 的 JSON 模式提交后立即断开连接且会话使用率达到 100%，另一名用户在发送 openclaw.ai 的直接链接后聊天中断并达到 5 小时使用配额。

hackernews · elmean · Apr 30, 14:36

**背景**: OpenClaw 是一个免费、开源的自主动 AI 代理，充当主动式个人助手，将 AI 模型与本地文件及 WhatsApp、Discord 等消息平台连接以自动执行任务。它由奥地利开发者 Peter Steinberger 开发并迅速走红。Claude Code 报告的过滤行为表明，Anthropic 可能试图限制涉及集成或引用这一竞争工具的使用，可能是为了减轻来自高频用户的服务器负载，或者作为一种反竞争手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>
<li><a href="https://www.digitalocean.com/resources/articles/what-is-openclaw">What is OpenClaw? Your Open-Source AI Assistant for 2026 | DigitalOcean</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示参与度很高，多位用户复现了该问题，一些用户关注审查方面，而一位评论者指出这揭示了 Anthropic 的内部情况，暗示公司可能因负载问题将 OpenClaw 的使用视为生存威胁；其他用户则对严格的使用配额和 A/B 测试做法表示不满。

**标签**: `#AI ethics`, `#Claude Code`, `#censorship`, `#content filtering`, `#Anthropic`

---

<a id="item-3"></a>
## [Rivian 推出禁用车辆全部互联网连接的选项](https://rivian.com/support/article/can-i-disable-all-data-collection-from-my-vehicle) ⭐️ 8.0/10

Rivian 新增一项设置，允许车主完全禁用车辆的互联网连接和数据收集，包括禁用 eSIM 和 OTA 更新功能。 此举让用户对联网汽车的隐私拥有前所未有的控制权，但也引发了严重问题：依赖 OTA 更新的安全召回将如何执行。这可能为其他车企提供类似隐私选项的先例，并可能重塑行业在数据收集方面的做法。 禁用连接后 OTA 更新也无法使用，这可能会延迟通常需要软件补丁的关键安全修复。Rivian 指出，当该设置启用时，导航、远程服务和应用连接等功能将受到限制或完全禁用。

hackernews · Cider9986 · Apr 30, 20:27

**背景**: 现代联网汽车通过远程信息处理控制单元（TCU）连接到互联网，以实现导航、远程诊断和 OTA 更新等功能。OTA 更新使制造商能够远程修复软件问题并改进安全功能，无需前往经销商。这一点对电动汽车尤为重要，因为其性能和安全性更新高度依赖软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Telematic_control_unit_(TCU)">Telematic control unit (TCU)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Over-the-air_update">Over-the-air update - Wikipedia</a></li>
<li><a href="https://www.jdpower.com/cars/shopping-guides/what-are-over-the-air-updates-for-cars">What Are Over the Air Updates for Cars?</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了未解决的问题，例如在车辆连接被禁用后，需要软件更新的安全召回将如何执行。一些人赞扬 Rivian 提供了用户控制的隐私功能，与其他收集侵入性数据（如性活动）的车企形成对比。有用户指出，过去在许多车辆上，物理断开蜂窝天线是唯一的选择，因此 Rivian 的做法是受欢迎的进步。

**标签**: `#privacy`, `#connected vehicles`, `#IoT`, `#data collection`, `#automotive software`

---

<a id="item-4"></a>
## [马克·克莱因揭露 NSA 房间 641A 内幕](https://thereader.mitpress.mit.edu/the-whistleblower-who-uncovered-the-nsas-big-brother-machine/) ⭐️ 8.0/10

一篇书籍节选详细讲述了前 AT&T 技术人员马克·克莱因在 2006 年发现并向电子前哨基金会（EFF）披露了 NSA 无证监视设施房间 641A 的过程。 这一举报事件具有历史意义，因为它揭露了 NSA 的国内大规模监控项目，引发了关于隐私的公共辩论，并导致了如 Hepting 诉 AT&T 等重大诉讼。 房间 641A 位于旧金山 AT&T 的福尔瑟姆街 611 号设施内，负责拦截互联网流量供 NSA 使用；克莱因注意到异常的布线图和秘密施工，从而促使他揭露此事。

hackernews · the-mitr · Apr 30, 16:41

**背景**: 9/11 袭击后，NSA 启动了无证窃听项目，模糊了外国与国内监控之间的法律界限。AT&T 配合 NSA，允许其接入光纤电缆。AT&T 技术人员马克·克莱因发现了秘密房间 641A，并联系了 EFF，后者随后提起了集体诉讼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Room_641A">Room 641A - Wikipedia</a></li>
<li><a href="https://www.sfgate.com/tech/article/nsa-spying-network-att-folsom-room-641a-13028155.php">Secret NSA spying network alleged in San Francisco skyscraper, Seattle, other U.S. cities</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，所谓的外国与国内监控之间的‘墙’早在 9/11 之前就已屡遭突破，有人分享了 2002 年在一个数据中心看到大型光纤束的个人经历。另一些人称赞马克·克莱因是真正的美国英雄，从未追求名人地位，而一位评论者则认为技术进步本质上威胁着民主治理。

**标签**: `#whistleblowing`, `#NSA surveillance`, `#privacy`, `#EFF`, `#surveillance`

---

<a id="item-5"></a>
## [Opus 4.7 可通过写作风格去匿名化作者](https://www.theargumentmag.com/p/i-can-never-talk-to-an-ai-anonymously) ⭐️ 8.0/10

新的人工智能模型 Opus 4.7 已展示出仅通过分析写作风格就能准确识别作者的能力，实际上对匿名或笔名文本进行了作者归因。 这项能力对在线匿名性和隐私构成了严重威胁，因为以前手动且不可靠的文体分析现在可以大规模自动化，可能揭露跨平台的笔名用户。 值得注意的是，社区测试显示 Opus 4.7 甚至可以检测对已知作者风格的模仿并正确归因，表明该模型具有超越简单模式匹配的稳健风格指纹识别能力。

hackernews · ilamont · Apr 29, 17:09

**背景**: 作者归因，即文体学，是通过研究语言风格来识别文本作者。历史上用于法医和文学分析，但通常需要大量人工。先前的人工智能模型在此任务上表现不佳，而 Opus 4.7 在社区讨论中被视为一项突破。对抗性文体学技术（作者故意改变风格）存在，但其对先进模型的有效性尚不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Authorship_attribution">Authorship attribution</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stylometry">Stylometry - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_stylometry">Adversarial stylometry - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者既感到惊讶又表达了担忧。一位用户报告称，Opus 4.7 正确识别出某文本是对 James Mickens 风格的模仿。其他人指出在线匿名性可能不可避免地将终结，有人评论道‘不要指望未来能保住你的秘密’。一位早期测试 GPT-4 的物理学家多年前就观察到了类似现象。

**标签**: `#AI`, `#privacy`, `#deanonymization`, `#large language models`, `#authorship attribution`

---

<a id="item-6"></a>
## [PyTorch Lightning 依赖中发现 Shai-Hulud 恶意软件](https://semgrep.dev/blog/2026/malicious-dependency-in-pytorch-lightning-used-for-ai-training/) ⭐️ 8.0/10

一个以《沙丘》沙虫 Shai-Hulud 为主题的恶意软件包被发现伪装成合法依赖项，存在于 PyTorch Lightning 开源 AI 训练库中。 这一事件凸显了 AI/ML 生态系统中软件供应链攻击日益增长的威胁，像 PyTorch Lightning 这样广泛使用的软件包可能成为恶意软件的传播载体，进而危及数千个下游项目。 根据 Semgrep 博文，该恶意软件包名为'shai-hulud'，并设计为逃避检测；仓库搜索显示，一天内出现了超过 2200 个包含文本'A Mini Shai-Hulud has Appeared'的代码仓库。

hackernews · j12y · Apr 30, 16:09

**背景**: PyTorch Lightning 是一个高级开源库，用于简化 PyTorch 代码在深度学习研究和生产中的使用。软件供应链攻击是指恶意代码被注入到受信任的软件包中，进而传播给安装或更新该包的用户。此类攻击在开源生态系统中日益常见，攻击者瞄准流行库以触达大量用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PyTorch_Lightning">PyTorch Lightning - Wikipedia</a></li>
<li><a href="https://www.microsoft.com/en-us/securityengineering/opensource/ossthreats">OSS Supply Chain Threats</a></li>
<li><a href="https://www.redhat.com/en/blog/understanding-open-source-software-supply-chain-risks">Understanding open source software supply chain risks</a></li>

</ul>
</details>

**社区讨论**: 评论者对供应链攻击的频率表示担忧，指出与 xz 攻击和 left-pad 事件的相似性。部分人主张减少依赖或使用工具仅提取所需代码，也有评论者强调了审计庞大依赖树的困难。

**标签**: `#supply chain attack`, `#malware`, `#pytorch-lightning`, `#AI security`, `#open source security`

---

<a id="item-7"></a>
## [Honker：通过元数据轮询在 SQLite 中实现队列、发布/订阅和定时任务](https://honker.dev/) ⭐️ 8.0/10

Honker 是一个库，它将持久队列、流、发布/订阅消息和定时调度器直接嵌入到 SQLite 数据库文件中，通过轻量级元数据轮询（PRAGMA data_version）检测变更，而非在数据页上争用。 这种方法减少了在单进程或嵌入式应用中使用 Redis 或 RabbitMQ 等外部消息代理的需求，通过利用 SQLite 成熟的事务保证来简化架构并提高可靠性。 Honker 每毫秒轮询一次 PRAGMA data_version，这是 SQLite 在每次提交时（来自任何连接或进程）递增的单调计数器，提供精确的唤醒信号，开销极小（每次读取约 3 微秒）。作者计划未来用操作系统级通知（inotify、kqueue、共享内存）替代轮询。

hackernews · ferriswil · Apr 30, 14:43

**背景**: SQLite 使用文件级锁定和单写入器模型：一次只能有一个事务写入数据库，对同一页面的并发写入尝试会导致争用（SQLITE_BUSY）。PRAGMA data_version 是一个内置计数器，每次写入事务时都会改变，因此无需访问实际数据页面即可轻量级检测修改。然而，传统的数据页面轮询会导致页面缓存压力和写入器锁争用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite.org/lockingv3.html">File Locking And Concurrency In SQLite Version 3</a></li>
<li><a href="https://betterstack.com/community/guides/databases/turso-explained/">How Turso Eliminates SQLite's Single-Writer Bottleneck | Better Stack Community</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些人批评忙轮询不如内核文件监视器，而另一些人则赞同仅元数据的方法，并注意到作者计划添加操作系统通知。一位评论者质疑此类库的必要性，认为在单进程应用中，环形缓冲区和 futex 对于线程间通信效率更高。

**标签**: `#SQLite`, `#queues`, `#pub-sub`, `#embedded databases`, `#cron scheduling`

---

<a id="item-8"></a>
## [10GbE 家庭网络部署实践指南](https://www.gilesthomas.com/2026/04/10g-ethernet-what-i-did) ⭐️ 8.0/10

一篇详细的个人博客文章描述了作者在家中搭建 10 吉比特以太网（10GbE）的实践经验，涉及硬件选择、线缆注意事项和性能优化技巧，社区中超过 100 条评论补充了实用的真实世界建议。 这很重要，因为 10GbE 正逐渐进入家庭用户视野，但散热管理、模块代际差异及软件路由器性能瓶颈等实际陷阱可能影响部署效果；分享的经验有助于家庭实验室社区做出明智决策，避免代价高昂的错误。 博客与评论指出，10GBASE-T SFP+模块存在两代产品：老一代功耗高（约 3 瓦，30 米距离），易过热导致链路抖动；新一代功耗低（约 1.5 瓦，80-100 米距离），运行更凉爽。像 Protectli 这样的软件路由器虽可实现高吞吐量，但在延迟、每秒新建连接数和抖动方面不如硬件卸载方案。Cat-5E 线缆理论上可在短距离内支持 10GbE，但推荐使用 Cat-6A。

hackernews · gpjt · Apr 29, 13:15

**背景**: 10 吉比特以太网（10GbE）是一种网络标准，其数据传输速度是常见千兆以太网的十倍，适用于家庭实验室中的大文件传输或 NAS 访问等高带宽场景。SFP+（增强型小型可插拔接口）是一种模块化收发器接口，允许交换机和网卡通过光纤线缆或铜缆 RJ45 模块（10GBASE-T）进行连接。将家庭网络升级至 10GbE 通常需要兼容的网卡、一台 10GbE 交换机（管理型或非管理型）以及合适的线缆——铜缆常采用 Cat-6A，而长距离传输则选用光纤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gearit.com/blogs/news/10gbe-network-setup-guide">Complete 10GbE Network Setup Guide: Level Up Your Speed - GEARit</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了关键实践洞察：有人提醒 10GBASE-T SFP+模块分为两代（老一代高功耗与新一代低功耗），指出散热和链路稳定性问题；另一位分享了升级至 10GbE 后的满意体验，但强调成本高于预期；还有人警告不要在 10GbE 中使用软件路由器，因为其在延迟、连接速率和抖动方面远不如硬件卸载方案；此外，有评论澄清 Cat-5E 在短距离下仍可支持 10GbE，这与官方规范有所不同。

**标签**: `#networking`, `#10GbE`, `#homelab`, `#SFP+`, `#hardware`

---

<a id="item-9"></a>
## [OpenClaw v2026.4.29-beta.2：消息、记忆和提供商增强](https://github.com/openclaw/openclaw/releases/tag/v2026.4.29-beta.2) ⭐️ 7.0/10

OpenClaw 测试版 v2026.4.29-beta.2 引入了主动运行的消息引导、面向人员的维基记忆系统、扩展的提供商支持（包括 NVIDIA 和 Bedrock Opus 4.7），以及改进的网关和插件可靠性。 此版本显著增强了 OpenClaw 构建自主 AI 代理的能力，通过更好的记忆管理、多代理路由和更广泛的模型支持，使其更适合生产部署。 值得注意的变化包括默认的主动运行引导（强制执行可见回复）、每个对话的活动记忆过滤器，以及记忆子代理超时时的有界部分召回摘要。此版本还添加了 OpenGrep 安全扫描和更安全的 exec/配对/所有者作用域处理。

github · steipete · Apr 30, 16:50

**背景**: OpenClaw 是一个用于构建 AI 代理的开源框架，这些代理可以自主执行任务并管理长期记忆。新的面向人员的维基记忆允许代理维护关于个人和关系的持久知识，从而提高上下文保持能力。子代理路由元数据使多代理系统能够跟踪并交付由父代理生成的子代理的结果，这对于复杂的自主工作流至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/openclaw/openclaw/2.5-multi-agent-routing">Multi-Agent Routing | openclaw/openclaw | DeepWiki</a></li>
<li><a href="https://github.com/SamurAIGPT/llm-wiki-agent">GitHub - SamurAIGPT/llm-wiki-agent: A personal knowledge base that builds and maintains itself. Drop in sources — Claude (or Codex/Gemini) reads them, extracts knowledge, and maintains a persistent interlinked wiki. Works with Claude Code, Codex, OpenCode, Gemini CLI. No API key needed.</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#openclaw`, `#release`, `#AI agents`, `#automation`, `#memory`

---

<a id="item-10"></a>
## [用 F#构建 Game Boy 模拟器：函数式编程实践](https://nickkossolapov.github.io/fame-boy/building-a-game-boy-emulator-in-fsharp/) ⭐️ 7.0/10

开发者 Nick Kossolapov 记录了使用 F#（一种运行在.NET 平台上的函数式优先语言）构建完整 Game Boy 模拟器的过程，并在网上分享了代码和设计决策。 该项目表明，像 F#这样的函数式编程语言也能用于对性能敏感的系统编程，挑战了模拟器必须用命令式语言编写的传统观念。同时，它也引发了关于 F#在.NET 生态中角色及其性能特征的讨论。 该模拟器使用地道的 F#编写，采用可区分联合体表示指令，并用函数式抽象映射硬件。社区成员建议通过将可区分联合体标记为结构体来减少内存分配，以优化性能。

hackernews · elvis70 · Apr 30, 17:14

**背景**: F#是一种强类型、函数式优先的编程语言，运行在.NET 运行时上，同时支持函数式和面向对象编程。Game Boy 模拟器是一种模拟任天堂 Game Boy 硬件的软件，使游戏能在现代系统上运行。构建模拟器是学习底层硬件概念和编程技巧的常见项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F_Sharp_(programming_language)">F Sharp (programming language) - Wikipedia</a></li>
<li><a href="https://sameboy.github.io/">SameBoy</a></li>

</ul>
</details>

**社区讨论**: 社区赞扬该项目的教育价值以及作者学习 F#所付出的努力，并将其与依赖 AI 辅助的教程区分开来。有评论者指出，F#在.NET 生态中常被 C#掩盖，且缺乏专门为其设计的库。其他人则对用函数式语言编写模拟器的难度表示赞赏，并提出了诸如使用结构体可区分联合体等具体优化建议。

**标签**: `#F#`, `#emulator`, `#Game Boy`, `#functional programming`, `#.NET`

---

<a id="item-11"></a>
## [比利时逆转核电站退役政策，延长运行](https://dpa-international.com/general-news/urn:newsml:dpa.com:20090101:260430-930-14717/) ⭐️ 7.0/10

比利时推翻了长期以来的核电站退役政策，决定继续运营这些核电站。此举实际上废除了之前的逐步淘汰计划，确保反应堆在可预见的未来继续发电。 这一决定意义重大，因为它标志着欧洲能源政策的重大转变，而核能在欧洲仍然是一个有争议的话题。这凸显了人们日益认识到核能在实现气候目标和确保能源安全方面可以发挥关键作用，尤其是在当前能源危机的背景下。 这些核电站目前由法国政府持股过半的 Engie 公司所有。根据新安排，比利时将买下这些电站，从而有效阻止法国对其的退役处理。

hackernews · mpweiher · Apr 30, 12:17

**背景**: 比利时此前曾承诺逐步淘汰核电，并制定了退役其反应堆的政策。该国的核电站一直是一个争论的话题，需要在安全性和废物处理问题与对低碳基荷电力的需求之间取得平衡。逆转逐步淘汰的决定与欧洲更广泛的趋势一致，即在能源价格上涨和气候紧迫的情况下，重新考虑核能作为稳定和清洁的能源来源。

**社区讨论**: 社区评论反映了对这项决定的支持和持续的担忧。用户 simplyluke 认为，在相信气候危机的同时反对核能是矛盾的，并称赞核电的安全记录。其他人，如 pjc50，指出此举的交易性质，并因时间和成本原因对新建核电表示不情愿，但同意退役正在运行的电站是一个糟糕的主意。讨论还涉及核废料储存的挑战，提到了德国数十年来寻找永久储存库的努力。

**标签**: `#nuclear energy`, `#energy policy`, `#climate change`, `#engineering`, `#infrastructure`

---

<a id="item-12"></a>
## [炼油厂如何运作：技术深度解析](https://www.construction-physics.com/p/how-an-oil-refinery-works) ⭐️ 6.0/10

Construction Physics 网站发布了一篇教育性文章，全面解释了炼油的流程和意义，涵盖分馏、催化裂化和脱硫等关键步骤。 这篇文章揭示了支撑现代能源和材料的关键工业过程，帮助读者理解汽油、塑料等日常产品背后的工程复杂性。 文章涵盖了整个炼油过程，包括分馏塔的使用、生产高辛烷值汽油的催化裂化以及加氢脱硫以去除硫。社区讨论中还指出，石油中的大部分能量最终以废热形式浪费。

hackernews · chmaynard · Apr 30, 13:54

**背景**: 炼油是将原油转化为汽油、柴油、航空燃料等可用产品的过程。主要方法是分馏，将原油在塔中加热，根据沸点分离成不同馏分。较重的馏分进行催化裂化，利用催化剂将大分子分解为更小、更有价值的分子。脱硫则去除硫化物以满足环保法规要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fractionating_column">Fractionating column - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Catalytic_cracking">Catalytic cracking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hydrodesulfurization">Hydrodesulfurization - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经历，例如一位父亲在全球最大的 Jamnagar 炼油厂工作，称其为工程奇迹。其他人提到了 SimRefinery 游戏，并指出与《异星工厂》等游戏中石油加工的相似之处。还有评论批评了'一次能源谬误'，指出石油的能量大部分以废热形式浪费。

**标签**: `#oil refining`, `#engineering`, `#industrial processes`, `#energy`, `#chemistry`

---