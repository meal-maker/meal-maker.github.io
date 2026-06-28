---
layout: default
title: "Horizon Summary: 2026-04-09 (ZH)"
date: 2026-04-09
lang: zh
---

> From 18 items, 13 important content pieces were selected

---

1. [Mac OS X 被成功移植到 Nintendo Wii，成就工程壮举](#item-1) ⭐️ 8.0/10
2. [Meta 推出旨在实现个人超智能的 Muse Spark AI 模型。](#item-2) ⭐️ 8.0/10
3. [论文批判机器学习反直觉的扩展轨迹](#item-3) ⭐️ 8.0/10
4. [约翰迪尔就维修权诉讼达成 9.9 亿美元和解。](#item-4) ⭐️ 8.0/10
5. [MegaTrain 实现在单张 GPU 上全精度训练 1000 亿+参数大语言模型。](#item-5) ⭐️ 8.0/10
6. [用户空间 USB 驱动编写入门指南](#item-6) ⭐️ 7.0/10
7. [一份快速理解新代码库的实用 Git 工作流](#item-7) ⭐️ 7.0/10
8. [卡尔曼滤波器教程更新，包含简单雷达追踪示例](#item-8) ⭐️ 7.0/10
9. [开发者推出网站应用，利用抓取的 AIS 数据追踪霍尔木兹海峡航运状态](#item-9) ⭐️ 7.0/10
10. [《纽约时报》文章试图指认比特币创始人中本聪为 Adam Back](#item-10) ⭐️ 7.0/10
11. [uv 0.11.5 发布，新增对 Python 3.13、3.14 和 3.15 的支持](#item-11) ⭐️ 6.0/10
12. [特里·比森经典科幻短篇《他们全是肉做的》再度引发讨论。](#item-12) ⭐️ 6.0/10
13. [Škoda DuoBell：一款针对降噪耳机的自行车铃](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Mac OS X 被成功移植到 Nintendo Wii，成就工程壮举](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html) ⭐️ 8.0/10

一名黑客将 Mac OS X 移植到 Nintendo Wii 上，通过逆向工程和自定义驱动程序开发克服了硬件和软件挑战，并在详细的文档中进行了阐述。 此次移植展示了 Apple Darwin 内核和 I/O Kit 的底层可移植性，为系统程序员提供了案例研究，并拓展了重新利用旧款游戏机的潜力。 该项目需要编写自定义帧缓冲驱动程序，并利用 Mac OS X 的抽象化 I/O Kit 层，尽管 Wii 的 PowerPC 架构在内存管理和外围设备上存在差异，但这些层被证明是有效的。

hackernews · blkhp19 · Apr 8, 15:40

**背景**: Mac OS X 基于 Darwin 构建，这是一个采用结合了 Mach 和 BSD 组件的 XNU 混合内核的类 Unix 操作系统。Nintendo Wii 使用基于 PowerPC 的 CPU，这是旧版 Mac OS 原生支持的架构，使其成为移植的可行目标。移植操作系统涉及将内核和驱动程序适配到新硬件，通常需要对目标系统的固件和接口进行逆向工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PowerPC">PowerPC - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Darwin_(operating_system)">Darwin (operating system) - Wikipedia</a></li>
<li><a href="https://www.retroreversing.com/wii">Nintendo Wii Reverse Engineering - Retro Reversing</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞该项目技术深度十足且文档优秀，专家指出 Mac OS X 抽象层的有效性，并对作者在经济舱座位上完成的令人印象深刻的工作表示赞赏。评论中还将此与其他移植努力（如 Wii 上的 NetBSD）进行了比较。

**标签**: `#Operating Systems`, `#Reverse Engineering`, `#Hardware Hacking`, `#Mac OS X`, `#Nintendo Wii`

---

<a id="item-2"></a>
## [Meta 推出旨在实现个人超智能的 Muse Spark AI 模型。](https://ai.meta.com/blog/introducing-muse-spark-msl/?_fb_noscript=1) ⭐️ 8.0/10

Meta 宣布了 Muse Spark，这是一款旨在向个人超智能扩展的新型大语言模型，并已立即在 Meta AI 应用和 meta.ai 网站上提供查询服务。该模型由首席 AI 官 Alexandr Wang 领导，是 Meta 自重大投资交易后的首个主要 AI 发布。 这很重要，因为 Muse Spark 使 Meta 能够与 OpenAI 和 Google 等公司的前沿模型竞争，可能重塑 AI 格局。它标志着 Meta 向先进、专有 AI 开发的战略转变，这可能影响行业趋势和超智能系统的竞争。 Muse Spark 集成了诸如 Code Interpreter Python 容器和名为'container.visual_grounding'的图像分析工具。然而，早期用户基准测试报告了分析错误，表明其性能可能尚未完全匹配 OpenAI 或 Anthropic 等公司的顶级前沿模型。

hackernews · chabons · Apr 8, 16:01

**背景**: 个人超智能指的是针对个人目标和上下文定制的 AI 系统，旨在在特定领域超越人类智能。前沿模型是最先进的 AI 模型，能够进行推理、多模态生成和智能体工作流，代表了 AI 技术的前沿。Meta 之前专注于像 Llama 这样的开放模型，但 Muse Spark 表明其在 AI 领域向更具竞争性的封闭开发转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.meta.com/blog/introducing-muse-spark-msl/">Introducing Muse Spark: Scaling Towards Personal ... - Meta AI</a></li>
<li><a href="https://www.meta.com/superintelligence/">Personal Superintelligence</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>

</ul>
</details>

**社区讨论**: 社区情绪不一，一些用户对如果 Muse Spark 性能与 Opus 4.6 等模型相似表示乐观，认为 Meta 具有竞争力，而其他人则批评其基准测试结果并质疑 Meta 放弃开放生态系统战略。其他担忧包括关于投资可持续性的辩论以及与铁路狂热等历史经济泡沫的比较。

**标签**: `#Artificial Intelligence`, `#Large Language Models`, `#Meta`, `#AI Research`, `#Technology News`

---

<a id="item-3"></a>
## [论文批判机器学习反直觉的扩展轨迹](https://aphyr.com/posts/411-the-future-of-everything-is-lies-i-guess) ⭐️ 8.0/10

一篇题为《The Future of Everything is Lies, I Guess》的论文批判了机器学习的当前发展路径，强调其严重依赖扩展模型参数和数据而非架构创新，并质疑这种方法是否能带来真正的先进能力。 这一批判挑战了 AI 中占主导地位的扩展范式，可能影响研究重点、行业投资和当前趋势的可持续性，促使重新评估无限扩展是否是最佳前进道路。 论文引用 2017 年 Transformer 论文作为突破性进展，但指出后续更复杂的架构在性能上常不及单纯扩展参数，引用了'苦涩的教训'，并观察到增加训练成本和参数数量带来的收益递减。

hackernews · pabs3 · Apr 8, 13:06

**背景**: 神经扩展定律是经验关系，描述了机器学习性能如何随着参数、数据和计算等扩展因素可预测地提升。涌现能力指的是仅在大语言模型达到一定规模时才出现的不可预测能力，说明了 AI 进展的非线性和有时反直觉的特性。这些概念是理解论文对扩展方法批判的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emergent_abilities_of_large_language_models">Emergent abilities of large language models</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示了批判性和细致入微的辩论，包括与工业革命在资源开采方面的类比，对仅靠扩展实现人类水平智能的怀疑，以及呼吁平衡看待 LLMs 当前在逻辑任务中的能力但在创造性和未见问题上的局限性。

**标签**: `#machine-learning`, `#artificial-intelligence`, `#scaling`, `#future-trends`, `#critique`

---

<a id="item-4"></a>
## [约翰迪尔就维修权诉讼达成 9.9 亿美元和解。](https://www.thedrive.com/news/john-deere-to-pay-99-million-in-monumental-right-to-repair-settlement) ⭐️ 8.0/10

约翰迪尔已同意支付 9.9 亿美元，以了结涉及维修权问题的诉讼，这在消费者和软件自由方面标志着一个重要进展。 此次和解是维修权运动的一个关键时刻，可能赋予农民和消费者独立维修设备的能力，并可能影响针对其他制造商的类似案件。 值得注意的是，2022 年约翰迪尔固件的完全破解可能影响了此次和解，且有指控称该公司未能遵守其 GPL 义务，该义务要求分享衍生作品的源代码。

hackernews · CharlesW · Apr 8, 20:46

**背景**: 固件是嵌入在硬件设备（如拖拉机）中的软件，通过存储在内存中的代码来控制其操作。GNU 通用公共许可证（GPL）是一种广泛使用的开源许可证，要求对软件的修改或衍生作品必须在相同条款下提供。维修权运动倡导消费者在没有制造商限制的情况下自行维修设备的能力，这通常涉及获取工具和软件的权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.freecodecamp.org/news/learn-embedded-systems-firmware-basics-handbook-for-devs/">Learn Embedded Systems Firmware Basics – A Handbook for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_license">Open-source license - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调，9.9 亿美元的和解对约翰迪尔来说相对较小，有人指出股价上涨并呼吁采取更严厉的惩罚措施。此外，讨论了 2022 年的固件破解和可能的 GPL 违规，表明这些因素给公司带来了压力。

**标签**: `#right-to-repair`, `#legal-settlement`, `#john-deere`, `#firmware`, `#open-source`

---

<a id="item-5"></a>
## [MegaTrain 实现在单张 GPU 上全精度训练 1000 亿+参数大语言模型。](https://arxiv.org/abs/2604.05091) ⭐️ 8.0/10

研究人员提出了名为 MegaTrain 的内存中心化系统，该系统通过将参数和优化器状态存储在 CPU 内存中，并逐层流式传输到 GPU，从而高效地在单张 GPU 上全精度训练超过 1000 亿参数的大语言模型。 这一突破可能使大规模 AI 训练更加平民化，让拥有有限 GPU 资源的个人和小团队也能训练最先进的模型，这或许会加速创新并降低 AI 生态系统的门槛。 MegaTrain 通过将 GPU 视为瞬态计算引擎并逐层流式传输参数，最小化了持久设备状态，但这种方法可能涉及 CPU 和 GPU 之间的大量数据传输开销，从而影响训练速度。

hackernews · chrsw · Apr 8, 12:19

**背景**: 深度学习中的全精度训练通常对所有计算使用 32 位浮点数，这保持了高精度，但相比混合精度方法需要更多内存。参数卸载是一种将模型权重存储在 CPU RAM 中，并在需要时传输到 GPU VRAM 的技术，以克服 GPU 内存限制，从而在有限硬件上训练更大模型。训练具有数十亿参数的大语言模型传统上需要 GPU 集群，因为其内存和计算需求巨大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.05091">MegaTrain: Full Precision Training of 100B+ Parameter Large ...</a></li>
<li><a href="https://lightx2v-en.readthedocs.io/en/latest/method_tutorials/offload.html">Parameter Offload — Lightx2v</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出褒贬不一的情绪，一些用户对在有限 VRAM 的家用设备上使用的潜力感到兴奋，而另一些人则质疑在单张 GPU 上训练巨大模型的新颖性和实际效用，并且有关于在 H200 等特定硬件上的训练时间以及对统一内存架构影响的技術讨论。

**标签**: `#AI`, `#Machine Learning`, `#GPU`, `#Deep Learning`, `#Systems`

---

<a id="item-6"></a>
## [用户空间 USB 驱动编写入门指南](https://werwolv.net/posts/usb_for_sw_devs/) ⭐️ 7.0/10

WerWolv 网站上发布了一篇详细教程，向软件开发者介绍如何编写用户空间 USB 驱动，并提供了实用示例和社区见解。 该指南降低了 USB 驱动开发的门槛，使开发者能够在不修改内核的情况下与定制或小众硬件交互，这对于嵌入式系统、原型设计和爱好者项目非常有价值。 该教程可能基于 libusb 库进行跨平台用户空间 USB 访问，但用户空间驱动在性能和与操作系统子系统集成方面可能存在限制，社区讨论中已指出这一点。

hackernews · WerWolv · Apr 8, 19:23

**背景**: USB 驱动负责 USB 设备与操作系统之间的通信。用户空间驱动（如使用 libusb 的驱动）在应用程序空间而非内核空间运行，这使得它们更易于开发和调试，但效率可能较低。libusb 是一个跨平台库，允许从用户空间访问 USB 设备而无需内核模式驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Libusb">libusb - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/26506375/difference-between-user-space-driver-and-kernel-driver">linux - Difference between user - space driver and kernel driver</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极，开发者分享了如用于 USB 访问的 Go 语言库等资源，讨论了驱动与操作系统子系统集成的挑战，并提供了实际用例。批评包括提供的 C++代码示例存在问题。

**标签**: `#USB`, `#Userspace Drivers`, `#Systems Programming`, `#Tutorial`, `#Embedded Systems`

---

<a id="item-7"></a>
## [一份快速理解新代码库的实用 Git 工作流](https://piechowski.io/post/git-commands-before-reading-code/) ⭐️ 7.0/10

一篇详细介绍了作者在阅读代码前，用于分析代码库历史和结构的特定 Git 命令组合的博客文章在 Hacker News 上引起了广泛关注。这篇文章引发了开发者们关于最佳实践、工具替代方案和实际经验的广泛讨论。 这一点很重要，因为它为开发者，特别是新加入项目的成员，提供了一种具体的方法论，以高效地掌握代码库的健康状况、核心贡献者和潜在问题区域。它使初始探索阶段变得更加民主化，节省了大量时间，并降低了面对陌生大型代码库时的畏难情绪。 文章展示的命令包括 `git shortlog -sn --no-merges`（用于列出核心贡献者）以及一个用于查找过去一年中最频繁更改文件的命令管道。一个关键见解是，像提交数量这样的指标可能具有误导性，因为大量的提交不一定代表积极的贡献，这一观点在评论中引发了争论。

hackernews · grepsedawk · Apr 8, 08:53

**背景**: Git 是一个用于跟踪源代码变更的分布式版本控制系统。`git log` 等命令用于显示提交历史，`git shortlog` 用于按作者汇总贡献，`git reflog` 记录本地引用更新并可以帮助恢复丢失的提交。`git bisect` 命令使用二分查找法来高效定位引入错误的提交。使用 `--pretty=format` 自定义 `git log` 的输出是提取特定信息的常见做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/docs/pretty-formats">Git - pretty-formats Documentation</a></li>
<li><a href="https://medium.com/@porteneuve/git-bisect-quickly-zero-in-on-a-bugs-origin-2ff44dc981c9">Git Bisect : quickly zero in on a bug ’s origin | by Christophe... | Medium</a></li>
<li><a href="https://graphite.com/guides/recovering-lost-commits-git-reflog">Recovering lost commits with git reflog</a></li>

</ul>
</details>

**社区讨论**: 讨论揭示了几个关键主题：有人提出了 Jujutsu VCS 等替代工具并给出了等效命令；许多评论哀叹企业环境中提交信息的质量低下；部分用户质疑了所建议的 Git 指标的有效性，并分享了提交量高并不等同于有价值贡献的轶事。

**标签**: `#Git`, `#Software Engineering`, `#Code Review`, `#Version Control`, `#Developer Tools`

---

<a id="item-8"></a>
## [卡尔曼滤波器教程更新，包含简单雷达追踪示例](https://kalmanfilter.net/) ⭐️ 7.0/10

作者 alex_be 更新了其卡尔曼滤波器教程的主页，加入了一个基于简单雷达追踪问题的新示例。此举旨在仅使用基础统计学和线性代数来解释该算法，避免高级数学。 该教程使卡尔曼滤波器——信号处理和控制系统的关键算法——对更广泛的受众（包括学生和工程师）变得易于理解。通过揭开复杂概念的神秘面纱，它促进了在机器人、导航和机器学习等领域的学习和应用。 该教程通过循序渐进的雷达示例来培养直觉，从噪声测量开始，并结合运动模型进行预测。然而，正如社区讨论所强调的，卡尔曼滤波器主要在高速采样噪声数据以补偿低质量测量时表现出色，并且它们并非通用解决方案。

hackernews · alex_be · Apr 8, 17:11

**背景**: 卡尔曼滤波器是一种用于动态系统状态估计的算法，它结合了模型的预测和噪声测量，以产生对当前和未来状态的最优估计。它基于状态空间模型，该模型表示系统的内部变量及其随时间的变化，通常应用于雷达追踪、导航和信号处理中，以滤除噪声并提高准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kalman_filter">Kalman filter - Wikipedia</a></li>
<li><a href="https://kalmanfilter.net/">Kalman Filter Explained Through Examples</a></li>

</ul>
</details>

**社区讨论**: 社区反响总体积极，用户赞赏该教程的易理解方法。关键观点包括对替代可视化资源的推荐、对加权最小二乘等基本原理的直观解释，以及关于实际限制的讨论，例如对噪声数据需要高采样率以实现最佳效果。

**标签**: `#Kalman Filter`, `#Signal Processing`, `#Tutorial`, `#Machine Learning`

---

<a id="item-9"></a>
## [开发者推出网站应用，利用抓取的 AIS 数据追踪霍尔木兹海峡航运状态](https://www.ishormuzopenyet.com/) ⭐️ 7.0/10

一名开发者推出了名为'Is Hormuz Open Yet?'的网站应用，通过从 MarineTraffic 的公共 AIS 地图界面手动抓取实时船舶位置数据，来追踪霍尔木兹海峡的通航状态。开发者还计划使用 AI 代理配合定时 Cron 任务来自动化这一流程，不过当前从 IMF PortWatch 平台获取的数据存在四天的延迟。 这个项目很重要，因为它试图为一个关键的国际航运咽喉要道提供公开的、近实时的可视性，全球约三分之一的海运石油依赖此通道。它展示了开发者如何创造性地获取并重新利用昂贵的商业数据（如实时 AIS 信息流）来制作公共信息工具，融合了网站开发、数据抓取和地缘政治。 该网站最初的数据是通过从 MarineTraffic 网站上手动复制 JSON 获取的，以绕过昂贵的实时 AIS API。作为替代方案，开发者整合了 IMF PortWatch 平台的数据，但也指出其存在四天的显著延迟，这降低了其实时状态检查的实用性。

hackernews · anonfunction · Apr 8, 21:33

**背景**: 自动识别系统（AIS）是船舶上用于识别和广播位置的自动跟踪系统，是 MarineTraffic 等服务的数据基础。Cron job 是类 Unix 操作系统中的基于时间的任务调度程序，用于在指定间隔自动执行脚本或命令，开发者计划将其用于数据收集。IMF 的 PortWatch 是国际货币基金组织与牛津大学合作推出的一个平台，用于监测和模拟极端气候等事件对贸易造成的干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_identification_system">Automatic identification system - Wikipedia</a></li>
<li><a href="https://www.samnet.dev/learn/linux/crontab-tutorial/">Crontab Tutorial: Schedule Tasks on Linux (Beginner Guide)</a></li>
<li><a href="https://portwatch.imf.org/">PortWatch</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包含了对纳入预测市场数据的伦理批评，有用户称其为‘淫秽的预测机制’，会制造有害的经济激励。其他人则指出数据延迟削弱了网站‘实时’的前提，同时一些用户提供了技术建议，例如使用免费的卫星图像，甚至直接提供了获取更好、更持久 AIS 数据源的途径。

**标签**: `#web-development`, `#data-scraping`, `#geopolitics`, `#ai-agents`

---

<a id="item-10"></a>
## [《纽约时报》文章试图指认比特币创始人中本聪为 Adam Back](https://www.nytimes.com/2026/04/08/business/bitcoin-satoshi-nakamoto-identity-adam-back.html) ⭐️ 7.0/10

调查记者 John Carreyrou 在《纽约时报》发表文章，利用风格计量学分析和间接证据，主张 Hashcash 的创始人 Adam Back 就是化名的比特币创始人中本聪。 这一尝试之所以重要，是因为如果得到证实，可能会改变对比特币起源的历史认知，影响对其去中心化理念的看法，并重新引发关于加密货币生态中匿名性与可信度的辩论。 证据主要依赖于写作风格相似性和共同技术兴趣，但并非决定性，许多专家批评该方法忽略了像 Back 这样的早期密码朋克们的共同背景。

hackernews · jfirebaugh · Apr 8, 04:37

**背景**: Adam Back 是一位密码学家，他发明了 Hashcash，这是一种工作量证明系统，是比特币挖矿机制的前身。风格计量学是一种基于语言模式进行作者归属的计算技术。中本聪是 2008 年发布比特币白皮书并在 2011 年消失的匿名实体，其身份一直是科技界最大的谜团之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hashcash">Hashcash - Wikipedia</a></li>
<li><a href="https://www.plagiarismchecker.net/articles/stylometric-methods-for-plagiarism-detection-an-authorship-attribution-approach/">Stylometric methods for plagiarism detection: an authorship ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍持怀疑态度，用户认为风格证据缺乏说服力，指出许多密码朋克都有相似兴趣，并批评文章依赖主观观察而非确凿证据。

**标签**: `#Bitcoin`, `#Cryptography`, `#Journalism`, `#Anonymity`, `#Blockchain`

---

<a id="item-11"></a>
## [uv 0.11.5 发布，新增对 Python 3.13、3.14 和 3.15 的支持](https://github.com/astral-sh/uv/releases/tag/0.11.5) ⭐️ 6.0/10

astral-sh/uv 项目于 2026 年 4 月 8 日发布了版本 0.11.5，该版本增加了对 CPython 3.13.13、3.14.4 和 3.15.0a8 的支持，并修复了错误消息和路径规范化等漏洞，同时预览功能如 `uv audit` 命令也得到了增强。 此次发布确保了 uv 与最新 Python 版本的兼容性，使开发者能够无障碍地采用新功能，同时改进的 `uv audit` 功能通过增强 Python 依赖项的漏洞扫描，加强了安全性。 这是一个常规的增量更新，没有引入主要新功能，侧重于维护和错误修复，如在 Windows 上正确清除连接点以及改进 TLS 证书错误处理。预览功能（如索引配置中的 `exclude-newer`）是实验性的，可能在未来的版本中发生变化。

github · github-actions[bot] · Apr 8, 20:36

**背景**: uv 是由 astral-sh 开发的快速 Python 包安装器和解析器，旨在以更优性能取代 pip 等传统工具。项目 pyproject.toml 文件中的 `build-system.requires` 键指定了构建包所需的依赖项，例如构建后端。`uv audit` 是一个命令，通过检查如 Python Packaging Advisory Database 等数据库，扫描项目依赖项中的已知安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://packaging.python.org/en/latest/guides/writing-pyproject-toml/">Writing your pyproject.toml - Python Packaging User Guide</a></li>
<li><a href="https://github.com/astral-sh/uv/issues/9189">uv audit Command for Security Vulnerability Scanning #9189</a></li>

</ul>
</details>

**标签**: `#Python`, `#Package Management`, `#uv`, `#Release Notes`

---

<a id="item-12"></a>
## [特里·比森经典科幻短篇《他们全是肉做的》再度引发讨论。](http://www.terrybisson.com/theyre-made-out-of-meat-2/) ⭐️ 6.0/10

特里·比森于 1991 年创作的科幻短篇小说《他们全是肉做的》再次被发布在 Hacker News 上，引发了高度关注，获得了 399 的热度分数和 113 条评论。这篇故事是一个简短幽默的对话，两名外星生物对人类意识和智能竟然完全源于生物性的'肉'这一事实表示难以置信。 尽管这是一篇 1991 年的非技术性故事，它在技术社区中反复流行的现象，凸显了人们对意识、智能和具身性等哲学问题的持久兴趣。这篇故事作为一个发人深省且易于理解的切入点，引发了关于心智本质、人工智能以及费米悖论等话题的讨论。 该故事最初发表于 1991 年。它已被改编成一部短片和一部广播剧，社区成员还为其广播剧制作了 ASCII 艺术可视化。故事的核心设定完全通过外星人困惑的对话来呈现，其中没有出现任何人类角色。

hackernews · surprisetalk · Apr 8, 11:20

**背景**: 《他们全是肉做的》是科幻类型中一篇著名的短篇小说。故事完全由两个刚刚完成首次接触的外星人之间的对话构成。他们震惊地发现，所探测到的智慧信号竟然来自其身体和大脑完全由有机组织（'肉'）构成的生物，而他们认为这是一种荒谬且不可能容纳心智的介质。故事探讨了人类中心主义以及我们对智能必须具有的形态所做的假设。

**社区讨论**: 社区讨论显示了对这篇经典故事持续而强烈的兴趣。评论提到了它的各种改编作品，包括一部备受好评的短片和粉丝制作的广播剧 ASCII 可视化。用户还推荐了特里·比森的其他作品，例如《熊发现了火》，并将其与类似主题的哲学科幻作品联系起来，比如特德·姜的《大寂静》，后者探讨了沟通与无法识别的智能等相关主题。

**标签**: `#science-fiction`, `#philosophy`, `#short-story`, `#aliens`

---

<a id="item-13"></a>
## [Škoda DuoBell：一款针对降噪耳机的自行车铃](https://www.skoda-storyboard.com/en/skoda-world/skoda-duobell-a-bicycle-bell-that-outsmarts-even-smart-headphones/) ⭐️ 6.0/10

Škoda 推出了 DuoBell，这是一款机械自行车铃，声称通过使用 750 至 780 Hz 的特定频率范围来穿透主动降噪（ANC）耳机，该范围被认定为 ANC 滤波器中的‘安全间隙’。 这一点很重要，因为随着降噪耳机变得无处不在，骑行者需要可靠的方式来提醒那些听不到周围声音的用户，通过弥合传统警告设备与现代音频技术之间的差距，可能提升城市安全。 该车铃的有效性依赖于未标准化的 750-780 Hz 频率范围，这可能因 ANC 耳机型号而异，且社区反馈对其实际效果表示怀疑，认为它可能更多是一种营销努力而非实用解决方案。

hackernews · ra · Apr 8, 08:50

**背景**: 主动降噪（ANC）耳机通过使用麦克风采集环境噪音并产生反相声波来抵消噪音，主要对发动机嗡鸣等低频噪音有效。然而，ANC 系统存在局限性，可能无法均匀抵消所有频率，从而产生特定声音可以穿透的潜在间隙，如新闻中提到的‘安全间隙’概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainthatstuff.com/soundproofing.html">Soundproofing a room | Science of noise reduction How Much Can You Hear through Walls: Exploring the Limits What is the Science behind Soundproofing? - Soundstop.co.uk Skoda's new bike bell beats active noise-canceling headphones Engineering Acoustics/Sound Absorbing Structures and ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论 largely skeptical，用户对 780 Hz 频率的技术声称及其有效性表示质疑，将其比作三星安全卡车等其他品牌营销噱头。另一些人提出了使用更响喇叭等实用替代方案，并对 ANC 频率响应缺乏标准化表示担忧。

**标签**: `#acoustics`, `#noise-cancellation`, `#bicycle-safety`, `#marketing`, `#consumer-electronics`

---