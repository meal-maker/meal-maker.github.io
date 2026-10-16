---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 47 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [AdFection：定向广告沦为零点击间谍软件投放管道](#item-tech-news-1) ⭐️ 8.0/10
2. [Libreboot 26.10“Ominous Olive”发布：加入 UEFI 与 Chromebook 支持](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic 三季度营收增至 168 亿美元并收紧蒸馏](#item-tech-news-3) ⭐️ 8.0/10
4. [人工神经网络自行构建学习机制](#item-tech-news-4) ⭐️ 8.0/10
5. [Meta 发布 Muse Spark Open 开放权重模型](#item-tech-news-5) ⭐️ 7.0/10
6. [Jev 与 13 个 AI 模型如何应对电车难题](#item-tech-news-6) ⭐️ 7.0/10
7. [ASML 被曝开发混合键合设备](#item-tech-news-7) ⭐️ 7.0/10
8. [库克：Apple 智能 10 月底在华发布测试版，不含 Siri AI](#item-tech-news-8) ⭐️ 7.0/10
9. [谷歌推出 AI 驱动安卓防诈功能](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [中国称将继续向欧洲出口稀土，不受美中贸易协议到期影响](#item-finance-news-1) ⭐️ 8.0/10
2. [IMF：中国农村医疗支出占可支配收入 8.7%，仅次于美国](#item-finance-news-2) ⭐️ 7.0/10
3. [中国加速更换西方风电设备以保障能源安全](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [AdFection：定向广告沦为零点击间谍软件投放管道](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 8.0/10

Citizen Lab 发布的“AdFection”研究报告揭示了以色列公司 Discover Tech 如何将定向广告转变成零点击雇佣间谍软件的分发管道。该管道利用广告技术生态系统的精准投放能力，使恶意广告无需用户点击或交互即可感染目标设备。报告指出，这种手法让间谍软件得以隐蔽地到达特定个人，扩大了监控风险，并暴露出广告科技行业在内容审核与责任归属上的严重缺失。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**「背景」** 零点击间谍软件允许攻击者在用户不进行任何点击或操作的情况下感染设备，而商业间谍软件通常被出售给政府客户用于监控特定目标。Citizen Lab 是专门研究数字监控的机构，此前已多次曝光此类工具；本次报告首次公开确认通过定向广告投放零点击商业间谍软件，并指出以色列公司 Discover-Tech 表面上是一家广告公司，实则协助多个雇佣监控供应商跟踪和入侵设备。

**「影响」** 这一发现意味着广告平台需要承担更多责任来阻止恶意广告投放，同时高价值目标的移动设备面临更高的零点击间谍软件感染风险。

**「社区讨论」** 评论中有人质疑报告对“零点击”机制描述不够具体，认为其具有炒作成分；也有人指出以色列网络安全公司与政府关系密切，不应被轻易信任，并讨论以色列为何在间谍软件领域领先。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection: How Discover-Tech Turned Targeted Ads ...</a></li>
<li><a href="https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/">Targeted ads delivered 0-click exploits to install mercenary ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#zero-click spyware`, `#targeted advertising`, `#surveillance`, `#adtech`

---

<a id="item-tech-news-2"></a>
### [Libreboot 26.10“Ominous Olive”发布：加入 UEFI 与 Chromebook 支持](https://libreboot.org/news/libreboot2610.html) ⭐️ 8.0/10

Libreboot 26.10“Ominous Olive”已发布，新增 UEFI/EDK 支持，并导入 MrChromebox coreboot 发行版当前支持的 233 款 Chromebook，使开放固件可运行的硬件数量大幅增加。该版本仅提供源代码，用户需自行构建，不提供二进制文件；Baytrail（Kip）机型已经过测试，其余 Chromebook 尚需测试。UEFI/EDK 集成还使未来设备的移植工作更加容易，是该开源固件项目的一次重要扩展。

hackernews · iamnothere · 10月15日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=50102923)

**「背景」** Libreboot 是一个基于 coreboot 的开源固件项目，负责初始化硬件并引导 Linux 或 BSD 等操作系统。此前它缺少完整的 UEFI 支持，因此无法直接启动 Microsoft Windows；此次 26.10 版本通过采用 MrChromebox 的 EDK2 分支作为 coreboot 载荷，默认在几乎所有支持的主板上提供 UEFI。同时，该版本从 MrChromebox coreboot 发行版导入了 233 款受支持的 Chromebook 设备代码，使这些设备成为源码支持（本版本需从源码构建）。

**「影响」** 对希望摆脱专有固件的用户而言，可用的 Chromebook 设备从少量扩展到 233 款，但当前版本仅提供源码且多数设备未经测试，部署前需自行构建并验证兼容性。

**「社区讨论」** 社区普遍认为 UEFI/EDK 与 Chromebook 支持是重大进步，但也有讨论聚焦于该项目对 AI 辅助贡献的严格政策；部分用户认可该政策，同时提醒新支持的 Chromebook 多数未测试且无二进制发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://libreboot.org/news/libreboot2610.html">Libreboot – Libreboot 26.10 “Ominous Olive” released! With ...</a></li>
<li><a href="https://elsolitario.org/en/2026/10/15/libreboot-26-10-adds-full-uefi-and-code-for-233-chromebooks/">Libreboot 26.10: Full UEFI Support and 233 Chromebooks</a></li>

</ul>
</details>

**标签**: `#open-source`, `#firmware`, `#coreboot`, `#uefi`, `#chromebook`

---

<a id="item-tech-news-3"></a>
### [Anthropic 三季度营收增至 168 亿美元并收紧蒸馏](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

据《金融时报》报道，Anthropic 在周三投资者日上披露，2026 年第三季度收入约为 168 亿美元，较第二季度的 115 亿美元增长近 50%，第一季度约为 48 亿美元。第三季度每在算力上支出 1 美元可产生 1.70 美元收入，调整后营业利润率（不包括股权激励）为 11%。Anthropic 还表示已收紧对“蒸馏”的限制——即竞争对手用其模型输出训练自家模型的行为；四名知情人士称蒸馏曾占其收入的 5% 至 7%，并在第三季度被大幅压缩。此次沟通发生在潜在 IPO 之前，且 Anthropic 似乎不再向投资者强调年化经常性收入。

rss · Simon Willison · 10月15日 13:04

**「背景」** 模型蒸馏是一种用更强大模型的输出训练较弱模型的技术，可降低训练成本，但被用于复制头部模型能力时存在争议。Anthropic 是主要 AI 实验室之一，此前在投资者沟通中曾强调年化经常性收入，而本次改用季度收入指标。

**「影响」** 对于依赖调用 Anthropic 模型输出进行蒸馏的第三方实验室，Anthropic 已告知投资者其在第三季度大幅压缩了这部分收入，意味着相关使用可能面临更严格的额度或条款限制。

**标签**: `#AI`, `#Anthropic`, `#business`, `#revenue`, `#IPO`

---

<a id="item-tech-news-4"></a>
### [人工神经网络自行构建学习机制](https://www.reddit.com/r/MachineLearning/comments/1x6hmyg/how_artificial_neural_networks_build_their_own/) ⭐️ 8.0/10

据 MIT 2026 年 10 月 13 日报道和 PNAS 10 月 9 日论文，随机互连的类神经元单元在共享突触可塑性规则下能够自组织形成学习模块，并在模式识别和图像分类任务上取得与反向传播训练的受测网络相近的性能。研究的区别在于，不是直接设计学习回路，而是指定局部规则让其学习机制自行组织。作者明确提醒，自组织现象并不证明大脑使用这一机制；其动机是生物合理性，而非替代大规模模型中的反向传播。

reddit · r/MachineLearning · /u/Dorian182 · 10月15日 10:01

**「背景」** 反向传播是训练深层神经网络的主流算法，依赖全局误差信号更新权重；而生物突触通常被认为只使用局部信息进行可塑性调整。理解局部规则如何自发产生学习能力，有助于连接人工网络与生物神经机制。

**标签**: `#neural networks`, `#self-organization`, `#synaptic plasticity`, `#backpropagation alternative`, `#machine learning research`

---

<a id="item-tech-news-5"></a>
### [Meta 发布 Muse Spark Open 开放权重模型](https://research.meta.ai/blog/muse-spark-open) ⭐️ 7.0/10

Meta 发布了 Muse Spark Open，一个 816B 参数的开放权重混合专家（MoE）模型，主要针对本地执行进行优化，并支持 Unsloth、MLX 等多种推理运行时。该模型在 Hugging Face 上以 Muse-Spark-Open-816B-A42B 名称提供，许可条款基本允许自由使用，但若被用于向第三方提供模型即服务且被许可方及其关联公司合计总收入超过 2000 万美元，则需受额外条款约束。社区基准测试显示，其性能落后于 Qwen3.8 Flash Next 和 GLM 5.3 Flash，这两者均可在单块 B300 上运行。Meta 在部署兼容性上投入较大，但仍需在开放权重领域追赶竞争对手。

hackernews · bigwheels · 10月15日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50107379)

**「背景」** 开放权重模型允许用户下载模型权重并在自有硬件上部署。混合专家（MoE）架构在推理时只激活部分专家参数，从而降低计算需求；Muse-Spark-Open-816B-A42B 的命名表明总参数为 816B、激活参数约 42B。此前 Meta 的 Llama 系列已推动开放权重模型生态，本次发布延续了本地部署的策略。

**「影响」** 若被许可方或其关联公司向第三方提供模型即服务且合计总收入超过 2000 万美元，则受该条款约束，不能直接免费使用该开放权重许可；规模较小的团队和个人仍可自由部署。

**「社区讨论」** 社区普遍认可 Meta 在运行器兼容性上的努力，包括 Unsloth 和 MLX 等；但基准测试显示该模型落后于 Qwen3.8 Flash Next 和 GLM 5.3 Flash，有评论认为 Meta 在开放权重领域需要追赶，并希望基准测试能覆盖低、中推理级别。另有评论澄清许可条款基本自由，仅对合计总收入超 2000 万美元的模型即服务提供商设限。

**标签**: `#large language models`, `#open-weight AI`, `#model release`, `#AI inference`, `#Meta AI`

---

<a id="item-tech-news-6"></a>
### [Jev 与 13 个 AI 模型如何应对电车难题](https://zachlandes.com/trolley-problem/) ⭐️ 7.0/10

作者 Zach Landes 将 Jev 与另外 13 个 AI 模型放在多个版本的电车难题中进行比较，测试它们如何做出伦理决策。为减少单一措辞带来的偏差，他使用了重采样、多种问题变体和不同顺序。文章在 Hacker News 上获得 291 分和 139 条评论，引发关于 AI 安全与对齐的讨论。

hackernews · zlandes86 · 10月15日 16:24 · [社区讨论](https://news.ycombinator.com/item?id=50106023)

**「背景」** Jev 是 TypeSafe AI 开发的一种判别式人工智能模型，于 2026 年 9 月发布，它不生成自然语言文本，而是返回带概率估计和置信度的类型化决策（如选择、分数或“是/否”概率），供软件直接调用，可用于零样本分类等任务。TypeSafe 将其称为“系统一模型”，强调快速、直觉式判断。文章将其与 13 个其他 AI 模型放在“电车难题”等道德困境变体中进行测试，讨论此类决策模型在伦理决策上的表现。

**「影响」** AI 安全与对齐研究者可将这种重采样和多变体排序方法作为评估模型在伦理困境中一致性的可重复基准，减少提示措辞偏差。

**「社区讨论」** 评论区普遍认可该方法论，同时有人担心 AI 被用于银行客服等关键系统造成“卡夫卡式困境”，或用于军事目标识别；也有评论引用阿西莫夫机器人三定律作为参照。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_%28AI_model%29">Jev (AI model)</a></li>
<li><a href="https://jevmodel.org/">Jev AI Model (TypeSafe) — Typed System One Decisions</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#LLM evaluation`, `#ethical AI`, `#decision models`, `#benchmarking`

---

<a id="item-tech-news-7"></a>
### [ASML 被曝开发混合键合设备](https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding) ⭐️ 7.0/10

ASML 似乎正在开发一款混合键合设备，但公司目前尚未正式宣布。这一判断来自该公司的专利文件、一篇新闻报道以及其自身路线图。混合键合是先进半导体封装中的关键技术，对 AI 硬件和高性能芯片制造具有重要意义。由于信息有限，目前缺乏具体技术参数和发布时间。

rss · Semianalysis · 10月15日 19:27

**「背景」** 混合键合（hybrid bonding）是一种先进封装工艺，通过铜-铜直接互连和介质键合将芯片面对面连接，无需传统凸点或焊料，从而显著提高互连密度并降低寄生效应。ASML 以光刻机闻名，同时也在扩展量测与检测等半导体制造设备；其路线图和专利活动近年来覆盖了晶圆键合领域。

**「潜在影响」** 若 ASML 将混合键合工具商业化，它可能成为先进封装和 AI 芯片（尤其是晶圆级 HBM 与混合键合）的关键设备，因为混合键合正成为提升计算密度和 AI 性能的重要瓶颈环节。但公司尚未正式宣布，仍需以官方信息为准。

<details><summary>参考链接</summary>
<ul>
<li>ASML Expands Beyond Lithography With Hybrid Bonding And AI ...</li>
<li>Report: ASML inches forward with hybrid bonding | Paul van Gerven</li>
<li>ASML&#x27;s XT:260 Redefines Advanced Packaging: Onto Innovation&#x27;s AI ...</li>

</ul>
</details>

**标签**: `#ASML`, `#hybrid bonding`, `#semiconductor manufacturing`, `#advanced packaging`, `#chipmaking`

---

<a id="item-tech-news-8"></a>
### [库克：Apple 智能 10 月底在华发布测试版，不含 Siri AI](https://jiemian.com/article/15194723.html) ⭐️ 7.0/10

10 月 15 日，苹果董事会执行主席蒂姆·库克在上海受访表示，Apple Intelligence（Apple 智能）及阿里千问大模型已获批准，将于 10 月晚些时候发布测试版本。该测试版首批功能包括实时翻译、书写工具、照片清除工具等。但 Siri AI 此次不在其中，意味着首批中国版 Apple Intelligence 功能不包含 Siri 的 AI 升级。此次发布是苹果通过阿里千问模型将 Apple Intelligence 引入中国市场的一次有限测试。

telegram · zaihuapd · 10月15日 08:59

**「背景」** Apple Intelligence 是苹果推出的生成式人工智能功能套件，涵盖写作工具、图像处理、通知摘要等能力。在中国市场，生成式人工智能服务需通过监管审批，且通常需与本地模型供应商合作；苹果已与阿里巴巴合作，采用其千问（Qwen）大模型为中国版 Apple Intelligence 提供支持。此次苹果智能与阿里千问大模型获得批准后，国行测试版得以在 10 月底发布，但 Siri 的 AI 对话功能不在首批范围内。

**「影响」** 中国区用户将在 10 月晚些时候的测试版中体验到实时翻译、书写工具和照片清除等 Apple 智能功能，但无法使用 Siri AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202610/1372342.shtml">Apple Intelligence, Alibaba Qwen set for late-October beta ...</a></li>
<li><a href="https://felloai.com/apple-intelligence-china/">Apple Intelligence in China: Powered by Alibaba&#x27;s Qwen</a></li>
<li><a href="https://www.techtimes.com/articles/329055/20261014/china-cleared-apple-intelligence-cloud-queries-go-alibaba-under-chinas-spy-law.htm">China Cleared Apple Intelligence, but Cloud Queries Go to ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [谷歌推出 AI 驱动安卓防诈功能](https://blog.google/security/new-android-scam-protections/) ⭐️ 7.0/10

谷歌宣布推出多项 AI 驱动的安卓防诈新功能。Google Message 上线增强保护模式，通过隐私 AI 计算调用云端 Gemini 模型分析陌生对话的诈骗意图，并结合端侧 Gemini Nano 实时检测未知链接的安全性。屏幕共享自动遮挡密码及支付页面的功能已扩展至 Chrome 与 WebView 网页组件。系统还新增呼叫转移后台拦截与手动输入预警，防止动态验证码被窃取。

telegram · zaihuapd · 10月15日 12:39

**「背景」** 谷歌 Gemini 是新一代多模态 AI 模型家族，其中 Gemini Nano 为端侧轻量版本，可在设备本地处理敏感数据；云端 Gemini 模型则提供更强的推理能力。Google Messages 是多数安卓设备的默认短信应用，本次更新的增强保护模式需用户主动开启，并由云端模型分析陌生对话的诈骗意图。

<details><summary>参考链接</summary>
<ul>
<li>New Android protections to help keep you safe from mobile scams</li>
<li>Google Rolls Out AI Scam Defenses Across Android Messages and Calls</li>

</ul>
</details>

**标签**: `#Android`, `#Security`, `#AI`, `#Gemini`, `#Mobile`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国称将继续向欧洲出口稀土，不受美中贸易协议到期影响](https://www.cnbc.com/2026/10/15/china-rare-earth-exports-europe.html) ⭐️ 8.0/10

中国商务部发言人何亚东向 CNBC 表示，无论美中贸易协议是否延长至 1 月之后，中国都打算继续向欧洲出口稀土，并愿通过“绿色通道”机制继续审批稀土许可证。

rss · CNBC Finance · 10月15日 09:02

**「背景」** 2025 年 10 月中国曾收紧所有稀土出口，中美随后暂停相关措施一年，并在近期将暂停期延长至 1 月。

**「影响」** 对依赖中国稀土的欧洲工业而言，供应不确定性有所降低，但该表态仍是意向，未承诺具体出口数量。

**标签**: `#rare earths`, `#China`, `#European Union`, `#trade policy`, `#supply chain`

---

<a id="item-finance-news-2"></a>
### [IMF：中国农村医疗支出占可支配收入 8.7%，仅次于美国](https://www.cnbc.com/2026/10/15/chinese-spending-nearly-as-much-of-income-as-americans-on-healthcare.html) ⭐️ 7.0/10

国际货币基金组织（IMF）研究发现，中国农村家庭将可支配收入的 8.7%用于医疗，在 20 个主要经济体中仅次于美国的 9.9%；城镇为 5.4%，排第三。高医疗成本是中国人多储蓄、少消费的重要因素。

rss · CNBC Finance · 10月15日 23:00

**「背景」** 研究基于 20 个主要经济体的数据。美国人均可支配收入为 68289 美元，是中国（约 6400 美元）的 10 倍以上；中国城镇人均可支配收入 56502 元、农村 24456 元，农村 2020 年才脱贫。

**标签**: `#China economy`, `#healthcare spending`, `#household savings`, `#IMF`, `#consumer spending`

---

<a id="item-finance-news-3"></a>
### [中国加速更换西方风电设备以保障能源安全](https://www.bloomberg.com/news/articles/2026-10-15/china-removes-western-wind-power-equipment-to-boost-security?srnd=phx-technology) ⭐️ 7.0/10

中国正加快在能源基础设施中替换欧洲等西方国家的风电设备，以能源安全为由推动国产替代；波兰东方研究中心分析逾 1600 份公开采购文件后发现，近 300 份涉及替换外国风机控制系统、工业软件及零部件。

telegram · zaihuapd · 10月15日 14:55

**「背景」** 中国能源企业表示，进口风电设备存在维护成本高、备件供应周期长等问题，并担心外国技术可能带来安全风险，这是本轮替换动作的直接原因之一。

**「影响」** 国内风电设备厂商有望获得新的市场机会，而西方供应商可能面临中国市场份额进一步收缩的压力。

**标签**: `#China`, `#wind power`, `#energy security`, `#domestic substitution`, `#industrial policy`

---