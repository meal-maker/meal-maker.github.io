---
layout: default
title: "Horizon Summary: 2026-03-31 (ZH)"
date: 2026-03-31
lang: zh
---

> From 17 items, 9 important content pieces were selected

---

1. [Axios 在 NPM 上被入侵，恶意版本投放远程访问木马](#item-1) ⭐️ 9.0/10
2. [Android 开发者验证全面向所有开发者推出](#item-2) ⭐️ 8.0/10
3. [GitHub 项目 'Universal Claude.md' 旨在减少 Claude AI 输出令牌](#item-3) ⭐️ 7.0/10
4. [Artemis II 因隔热罩问题被认为不安全。](#item-4) ⭐️ 7.0/10
5. [Fedware 揭露政府应用使用被禁华为跟踪器进行监控](#item-5) ⭐️ 7.0/10
6. [坚持自主写作：为何独立写作至关重要](#item-6) ⭐️ 7.0/10
7. [教程演示如何利用核心内核功能将任意 Linux 设备变成路由器。](#item-7) ⭐️ 7.0/10
8. [2018 年 1 美元 DIY MacBook 触摸屏黑客项目](#item-8) ⭐️ 6.0/10
9. [探索鸟类智力：鸟类物种的认知能力与神经元数量](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Axios 在 NPM 上被入侵，恶意版本投放远程访问木马](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) ⭐️ 9.0/10

Axios 库的恶意版本被发布在 NPM 注册表中，注入了一个名为 plain-crypto-js@4.2.1 的虚假依赖。该依赖运行一个后安装脚本，部署跨平台的远程访问木马（RAT）。 Axios 是用于 HTTP 请求的极其流行的 JavaScript 库，这使得此次事件成为一次严重的软件供应链攻击，可能影响无数项目和开发者。这凸显了现代依赖生态系统中的系统性风险以及对强化安全措施的需求。 恶意版本本身不包含恶意代码，而是利用注入依赖中的后安装脚本来投放 RAT。社区成员指出，设置包的最低发布时间或在包管理器中禁用生命周期脚本等配置更改本可以缓解此漏洞。

hackernews · mtud · Mar 31, 02:54

**背景**: NPM（Node Package Manager）是 JavaScript 的主要包注册表，用于分发和管理代码库。软件供应链攻击指将恶意代码插入合法软件组件以危害下游用户的行为，如供应链安全资源中所定义。远程访问木马（RAT）是一种恶意软件，允许攻击者远程控制受感染系统，常用于数据窃取或进一步利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fortinet.com/resources/cyberglossary/supply-chain-attacks">Supply Chain Attacks: Examples And Countermeasures - Fortinet</a></li>
<li><a href="https://www.malwarebytes.com/blog/threats/remote-access-trojan-rat">Remote Access Trojan (RAT) | RAT Malware | RAT Trojans ...</a></li>

</ul>
</details>

**社区讨论**: 讨论主要集中在缓解策略上，例如配置包管理器设置最低发布时间和禁用脚本执行，用户指出这些措施本可以预防攻击。一些人对 Axios 的流行可能造成的广泛影响表示担忧，而另一些人则批评对传递性依赖的依赖，并将其与像 Rust 等语言中的替代方法进行比较。

**标签**: `#security`, `#npm`, `#supply-chain`, `#javascript`, `#axios`

---

<a id="item-2"></a>
## [Android 开发者验证全面向所有开发者推出](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html) ⭐️ 8.0/10

谷歌宣布正在全球范围内推出 Android 开发者验证，要求开发者在选定区域从 2026 年 9 月起必须验证身份才能注册应用。 此举旨在通过减少未验证来源的恶意软件来增强应用安全性和用户信任，对开发者的操作方式和整个 Android 生态系统的安全性产生重大影响。 开发者需提供并验证个人详细信息，如法定姓名、地址、电子邮件和电话号码。谷歌将于四月推出名为 Android Developer Verifier 的新系统服务，用于检查应用是否由已验证开发者注册。

hackernews · ingve · Mar 30, 22:05

**背景**: Android 开发者验证是开发者确认身份以注册应用的过程，属于谷歌打击恶意软件、提升平台安全性的举措。它专门针对侧载应用相比 Google Play 更高的恶意软件发生率，旨在保护用户的同时保持应用来源的选择性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html">Android developer verification: Rolling out to all developers ...</a></li>
<li><a href="https://developer.android.com/developer-verification">Android developer verification | Android Developers</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出对验证流程复杂性的不满，并就安全性与开放性展开辩论，一些用户批评此举反用户且损害 Android 的传统开放性，而其他人则指出 Google Play 上仍存在恶意软件问题。

**标签**: `#Android`, `#Mobile Development`, `#Security`, `#App Store Policies`, `#Developer Experience`

---

<a id="item-3"></a>
## [GitHub 项目 'Universal Claude.md' 旨在减少 Claude AI 输出令牌](https://github.com/drona23/claude-token-efficient) ⭐️ 7.0/10

一个名为 'claude-token-efficient' 的 GitHub 仓库被创建，提出了减少 Anthropic Claude AI 模型输出令牌的方法。这一举措在 Hacker News 上引发了争论，用户批评该项目的基准测试偏向单次解释性任务，并指出了实现中的问题。 令牌效率对于降低 AI API 的运营成本和改善响应时间至关重要，这使得该主题对开发者和企业具有重要意义。这场争论强调了在 AI 优化中需要采用稳健的基准测试实践，以确保改进在各种使用场景中都有效。 该项目的基准测试仅关注单次提示的输出令牌减少，而未评估响应准确性，这可能导致误导性结果。诸如'答案始终在第一行'的具体指令可能会引入确认偏差，因为大型语言模型是基于先前令牌自回归生成文本的。

hackernews · killme2008 · Mar 31, 01:23

**背景**: CLAUDE.md 文件是基于 Markdown 的配置文件，用于向 Claude AI 提供项目特定的指令，帮助其理解代码库的上下文。在大型语言模型中，令牌减少技术对于通过最小化令牌使用来优化推理成本至关重要。然而，基准测试这些技术需要精心设计，以避免在多次交互或代理场景中出现偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/josix/awesome-claude-md">GitHub - josix/awesome-claude-md: Curated collection of ...</a></li>
<li><a href="https://medium.com/@anicomanesh/token-efficiency-and-compression-techniques-in-large-language-models-navigating-context-length-05a61283412b">Token Efficiency and Compression Techniques in Large Language ...</a></li>
<li><a href="https://www.evidentlyai.com/blog/ai-benchmarks">25 AI benchmarks: examples of AI models evaluation</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论主要是批评性的，用户认为基准测试存在缺陷，未考虑多轮代理循环和准确性。有人担心某些指令可能会消除 AI 纠正错误的能力，还有人指出令牌节省不应以输出质量为代价。

**标签**: `#AI Optimization`, `#Token Efficiency`, `#Claude AI`, `#Benchmarking`, `#Hacker News`

---

<a id="item-4"></a>
## [Artemis II 因隔热罩问题被认为不安全。](https://idlewords.com/2026/03/artemis_ii_is_not_safe_to_fly.htm) ⭐️ 7.0/10

最近一篇文章认为，由于猎户座飞船的隔热罩问题未解决，特别是 Artemis I 测试飞行中观察到意外的碳化和侵蚀，Artemis II 任务不安全飞行。这引发了与历史太空任务技术挑战的比较讨论，并对 NASA 的风险评估提出质疑。 这很重要，因为 Artemis II 是 NASA 重返月球目标的关键载人任务，安全问题可能推迟该计划、危及宇航员生命并削弱公众对太空探索的信任。它反映了航空航天工程中的广泛挑战，如材料科学限制和深空任务现代风险管理的复杂性。 隔热罩使用 Avcoat 这种烧蚀材料，在 Artemis I 中显示出局部碳化，但 NASA 和洛克希德·马丁公司进行了超过 1000 次测试，并声称有充足的安全裕度。然而，批评者指出地面测试设施无法完全复制再入条件，且一些工程师如前宇航员托马斯·卡马达仍对设计的可靠性持怀疑态度。

hackernews · idlewords · Mar 31, 02:23

**背景**: Artemis 计划是 NASA 旨在将人类送上月球并最终前往火星的倡议，使用猎户座飞船进行载人任务。猎户座的热防护系统依赖由 Avcoat 制成的烧蚀隔热罩，在地球再入时通过烧蚀消散热量，类似于阿波罗时代的技术，但为更重的飞船进行了调整。NASA 使用概率风险评估（PRA）来评估任务安全性，整合历史数据和模拟工具以管理复杂太空计划中的不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nasa.gov/humans-in-space/after-15-years-1000-tests-orions-heat-shield-ready-to-take-the-heat/">After 15 Years, 1,000 Tests, Orion’s Heat Shield Ready to ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0094576525003972">Probabilistic Risk Assessment (PRA) for Artemis and future ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出混合情绪：一些用户捍卫 NASA 的立场，引用工程师和宇航员对隔热罩安全性的信心；而另一些人则对与阿波罗任务的设计差异及与过去如挑战者号等灾难的相似性表示担忧。还有关于计划动机和预算的辩论，质疑为什么尽管阿波罗成功仍需要新材料。

**标签**: `#space-exploration`, `#NASA`, `#safety`, `#aerospace-engineering`, `#risk-assessment`

---

<a id="item-5"></a>
## [Fedware 揭露政府应用使用被禁华为跟踪器进行监控](https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/) ⭐️ 7.0/10

最近的一项调查显示，白宫官方移动应用嵌入了来自华为的跟踪器，包括华为移动服务核心 SDK，并通过如自动填充消息的'给总统发短信'按钮等功能收集个人数据。 这凸显了政府行为的双重标准，因为美国以安全风险为由制裁华为，却在官方应用中使用其技术进行监控，引发了公共软件中隐私、道德和信任方面的关键问题。 该应用包含三个嵌入式跟踪器，华为的 SDK 实现了数据收集，而'给总统发短信'功能会收集姓名和电话号码。报道此事的文章因分散注意力的动画和可能缺乏详细证据而受到批评。

hackernews · speckx · Mar 30, 18:16

**背景**: Fedware 是指政府开发的用于监控和数据收集的软件，通常比商业应用更具侵入性。华为是一家因国家安全问题受到美国制裁的中国科技公司，其华为移动服务（HMS）提供用于应用功能和跟踪的 SDK。这些 SDK 允许访问网络浏览器通常限制的设备数据，例如后台位置和生物识别信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sesamedisk.com/fedware-government-surveillance-apps/">Fedware : Government Apps That Spy Harder Than the... - Sesame Disk</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666281722000749">A study on data acquisition based on the Huawei smartphone ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对在禁止华为的政府应用中嵌入其跟踪器表示震惊和讽刺，批评了应用的数据收集做法，并指出原生应用通常用于访问浏览器不可用的敏感设备 API。一些评论还对文章的表现形式和深度提出了质疑。

**标签**: `#privacy`, `#government`, `#mobile-apps`, `#tracking`, `#ethics`

---

<a id="item-6"></a>
## [坚持自主写作：为何独立写作至关重要](https://alexhwoods.com/dont-let-ai-write-for-you/) ⭐️ 7.0/10

Alex H. Woods 发表文章，反对依赖 AI 进行写作，强调自主写作能培养创造力和批判性思维。讨论揭示了人们对 AI 辅助可能削弱人类思维过程的担忧。 这很重要，因为它强调了过度依赖 AI 工具的风险，这可能抑制人类的创造力和独立思考，而这些在数字时代对创新和个人成长至关重要。 关键细节包括，LLM 常生成缺乏细微差别的平庸、主流思想，而自主写作迫使个人面对并解决思维中的矛盾，从而获得更深刻的见解。

hackernews · karimf · Mar 30, 12:39

**背景**: 大语言模型（LLMs）是基于海量数据训练的 AI 系统，用于生成、总结和翻译类人文本。它们越来越多地被用于写作辅助，但批评者认为其生成的内容可能缺乏原创性和深度，这引发了关于创造力的伦理担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/large-language-model/">What is LLM? - Large Language Models Explained - AWS</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认同自主写作对深度思考至关重要，用户分享了写作如何澄清思想并揭示矛盾。人们担忧 LLM 生成的内容平庸，以及分享 AI 生成作品对关系的负面影响。

**标签**: `#AI`, `#Writing`, `#Creativity`, `#Ethics`, `#LLMs`

---

<a id="item-7"></a>
## [教程演示如何利用核心内核功能将任意 Linux 设备变成路由器。](https://nbailey.ca/post/router/) ⭐️ 7.0/10

一篇详细教程发布，演示了如何通过启用 IP 转发和使用 iptables 配置 NAT 等基础命令，将一台标准的 Linux 计算机变为功能性路由器的分步过程。 这很重要，因为它揭示了路由器的基本工作原理，使核心网络概念变得易于理解，让用户能够利用现有硬件创建自定义、高性价比的网络解决方案或执行应急路由任务。 其核心技术依赖于启用 `net.ipv4.ip_forward` 内核参数，并使用 `iptables` 防火墙工具设置网络地址转换（NAT）规则，这正是许多商用路由器及虚拟化平台所使用的底层机制。

hackernews · yabones · Mar 30, 13:28

**背景**: IP 转发，也称为内核 IP 转发，是 Linux 内核的一项功能，允许系统在不同的网络接口间路由网络数据包，从而充当路由器。网络地址转换（NAT）是一种用于修改数据包头部网络地址信息的技术，通常用于让私有网络中的多台设备共享一个公共 IP 地址来访问互联网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linuxconfig.org/how-to-turn-on-off-ip-forwarding-in-linux">IP Forwarding Linux: How to Enable/Disable net.ipv4.ip_forward</a></li>
<li><a href="https://retrhelo.github.io/posts/iptables_nat/">Setting NAT with iptables - Blog of retrhelo</a></li>

</ul>
</details>

**社区讨论**: 社区讨论赞扬了该教程在解释核心概念方面的教育价值。社区成员还分享了如用于快速创建 Wi-Fi 热点的 `create_ap` 脚本等实用工具，指出这与 Docker 和安卓热点等使用相同内核功能的技术原理相通，并回顾了用旧 PC 硬件搭建路由器的历史。部分用户则建议在生产环境中使用 OPNsense/pfSense 等专用路由器操作系统。

**标签**: `#networking`, `#linux`, `#tutorial`, `#routing`, `#systems`

---

<a id="item-8"></a>
## [2018 年 1 美元 DIY MacBook 触摸屏黑客项目](https://anishathalye.com/macbook-touchscreen/) ⭐️ 6.0/10

2018 年，一个 DIY 项目展示了如何使用价值约 1 美元的硬件为 MacBook 添加触摸屏功能，引发了 Hacker News 上关于人体工程学和实用性的讨论。 这个项目展示了低成本硬件修改的可及性，并引发了社区关于将触摸屏集成到传统笔记本电脑形态中的人体工程学挑战和实际实用性的讨论。 这个黑客项目可能采用了红外触摸屏技术，这种技术可能受到如眩光或背光等光线条件的影响。一个重要的注意事项是在垂直屏幕上长时间使用会导致手臂疲劳的人体工程学限制。

hackernews · HughParry · Mar 30, 19:22

**背景**: 红外触摸屏通过检测红外光束网格中的中断来工作，通常通过 DIY 覆盖框架实现。在人体工程学上，垂直笔记本电脑屏幕上的触摸屏因在长时间使用中导致手臂疲劳而受到批评，这是笔记本电脑设计行业讨论中的一个重点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mods-n-hacks.gadgethacks.com/news/make-25-touchscreen-0142949/">How to Make a $25 Touchscreen << Hacks Mods... :: Gadget Hacks</a></li>
<li><a href="https://gizmodo.com/why-the-hell-would-you-want-a-touchscreen-on-your-ultra-5866364">Why the Hell Would You Want a Touchscreen on Your Ultrabook?</a></li>

</ul>
</details>

**社区讨论**: 讨论中情感各异，一些用户引用了 Steve Jobs 对人体工程学的批评并质疑其在生产力任务中的实用性，而另一些人则欣赏这个技术黑客项目，但对如光线依赖性等环境因素表示担忧。

**标签**: `#hardware-hacking`, `#touchscreen`, `#ergonomics`, `#DIY`, `#human-computer-interaction`

---

<a id="item-9"></a>
## [探索鸟类智力：鸟类物种的认知能力与神经元数量](https://www.dhanishsemar.com/writing/bird-brains) ⭐️ 6.0/10

一篇 2023 年的文章发表，探讨了鸟类智力，重点关注鹦鹉和鸣禽等物种的认知能力、神经元数量和心理模型。 这项研究很重要，因为它挑战了关于鸟类认知的传统观点，推动了比较心理学的发展，并为动物福利和认知进化的讨论提供了依据。 关键细节包括使用了各向同性分馏器（isotropic fractionator）方法进行神经元计数，并参考了如鹦鹉 ABC 模型等特定心理模型，这在社区评论中有所体现。

hackernews · DiffTheEnder · Mar 30, 13:14

**背景**: 鸟类智力在比较心理学领域进行研究，该领域使用标准化测试协议评估不同物种的认知能力。各向同性分馏器（isotropic fractionator）等方法可实现准确的神经元计数，而鸟类皮层（avian pallium）作为鸟类大脑区域，参与类似哺乳动物皮层的高级认知功能。这一背景有助于理解鸟类认知研究的相关新闻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons">List of animals by number of neurons - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Avian_pallium">Avian pallium - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示对鸟类智力的强烈认同，包括鹦鹉主人的个人轶事、如《The Bird Way》的进一步阅读推荐以及神经元计数图表等技术见解。同时，也提出了关于鸟类圈养的伦理关切，丰富了讨论内容。

**标签**: `#biology`, `#cognitive-science`, `#animal-intelligence`, `#neuroscience`

---