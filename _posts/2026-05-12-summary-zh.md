---
layout: default
title: "Horizon Summary: 2026-05-12 (ZH)"
date: 2026-05-12
lang: zh
---

> From 20 items, 9 important content pieces were selected

---

1. [UCLA 发现首款修复中风脑损伤的药物](#item-1) ⭐️ 9.0/10
2. [谷歌：犯罪分子利用 AI 发现零日漏洞](#item-2) ⭐️ 9.0/10
3. [TanStack npm 供应链泄露事件回溯](#item-3) ⭐️ 8.0/10
4. [GitLab 裁员并放弃 CREDIT 价值观，转向 AI 战略](#item-4) ⭐️ 8.0/10
5. [Ratty：支持内嵌 3D 图形的终端模拟器](#item-5) ⭐️ 8.0/10
6. [Swift 中矩阵乘法从 Gflop/s 优化到 Tflop/s](#item-6) ⭐️ 8.0/10
7. [Gmail 注册现要求扫描二维码发送短信](#item-7) ⭐️ 7.0/10
8. [AI 写代码，Python 还有必要吗？](#item-8) ⭐️ 6.0/10
9. [TypedMemory：快速将 Java 记录映射到本地内存](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [UCLA 发现首款修复中风脑损伤的药物](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

加州大学洛杉矶分校（UCLA）的研究人员发现一种候选药物，能够促进轴突发芽并重新连接因中风而中断的神经网络，针对脑修复的分子程序。这是首个专为中风康复而非急性治疗设计的药物。 如果在后续试验中得到验证，这种药物可能大幅减少对高强度物理治疗的需求，使中风患者通过服药即可获得类似康复的效果。它为全球数百万目前恢复手段有限的中风幸存者提供了新的康复途径。 该药物靶向 ATRX 基因，该基因参与控制 DNA 结构和可及性，此前从未与脑损伤后的轴突发芽相关联。该研究重点在于恢复梗死灶周围存活神经网络的节律，而非再生中风核心区域的死亡脑细胞。

hackernews · bookofjoe · May 11, 17:53

**背景**: 中风常因血流阻塞而损伤脑组织，导致核心梗死区细胞死亡，但周围区域可能存在‘挫伤’但仍存活的神经元，失去连接与节律。大脑在中风后可通过称为轴突发芽的过程自然生长新的轴突连接，但能力有限。UCLA 研究人员发现了涉及 ATRX 基因的分子程序控制这一发芽过程，并开发出一种药物来增强它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newswise.com/articles/ucla-researchers-identify-molecular-program-for-brain-repair-following-stroke">Researchers Identify Molecular Program for Brain Repair ... | Newswise</a></li>
<li><a href="https://www.mdpi.com/2076-3425/15/11/1217">Reconnecting Brain Networks After Stroke : A Scoping Review of...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4980303/">Molecular, Cellular and Functional Events in Axonal Sprouting after ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，该药物针对的是存活神经网络而非死亡细胞，这澄清了一个关于中风恢复的常见误解。有评论者引用特德·姜的短篇小说《领悟》作为文学类比，另一人提供了该具体化合物的 PubMed 链接。部分读者询问这种疗法是否也适用于其他神经退行性疾病。

**标签**: `#stroke`, `#rehabilitation`, `#neuroscience`, `#drug discovery`, `#UCLA`

---

<a id="item-2"></a>
## [谷歌：犯罪分子利用 AI 发现零日漏洞](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html) ⭐️ 9.0/10

谷歌威胁情报小组（GTIG）高度确信，某个黑客组织利用 AI 模型发现并武器化了一个零日漏洞，这标志着首例有记录的 AI 辅助网络攻击事件。 此事件标志着网络安全领域的范式转变，因为 AI 工具能够大幅降低发现关键漏洞的门槛，可能使传统的零日漏洞储备贬值，并加速攻击者与防御者之间的军备竞赛。 谷歌 GTIG AI 威胁追踪报告指出，攻击者可能利用大型语言模型（LLM）支持漏洞发现和利用，而 Anthropic 的 Mythos 等新模型也具备此类发现能力，但仅对有限机构和美国政府发布。

hackernews · donohoe · May 11, 13:20

**背景**: 零日漏洞是指供应商未知的软件缺陷，因此没有补丁，易被攻击者利用。传统发现需要大量专业知识，但 AI 模型——特别是为代码分析微调的大型语言模型——可以自动化和加速漏洞研究。安全研究人员已探索了 LLM 模糊测试等技术，用于测试 AI 模型本身及传统软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access">Adversaries Leverage AI for Vulnerability ... | Google Cloud Blog</a></li>
<li><a href="https://nullsec.news/ai-model-vulnerability-scanning-moves-beyond">AI Model Vulnerability Scanning Moves Beyond Theory... | NullSec</a></li>
<li><a href="https://www.crowdstrike.com/en-us/blog/feedback-guided-fuzzing-reveals-llm-blind-spots/">Feedback-Guided Fuzzing Reveals LLM Blind Spots | CrowdStrike</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑谷歌如何确定 AI 被使用，部分人对此归因表示怀疑。其他人则讨论了开放权重模型的影响——认为安全问题可能被用来限制这些模型——并指出 AI 辅助的黑客攻击会降低零日漏洞储备的价值。

**标签**: `#cybersecurity`, `#AI`, `#zero-day`, `#hacking`, `#LLM`

---

<a id="item-3"></a>
## [TanStack npm 供应链泄露事件回溯](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 8.0/10

TanStack 发布了事件回溯报告，详细说明了一起供应链泄露事故：攻击者在其仓库的一个分支中提交了恶意代码，利用 npm 的 postinstall 脚本窃取 GitHub 认证令牌，并进一步扩散到其他包。 此事件突显了 npm 生态中 postinstall 脚本的严重风险，表明即便是广泛使用的开源项目也易受供应链攻击。同时，它也揭示了当攻击者获得 CI 流水线或仓库凭证访问权限时，Trusted Publishing 等现有安全措施的局限性。 恶意代码通过一个分支中的孤立提交引入，npm 使用共享对象存储使得该提交的 URI 与合法仓库无法区分。载荷安装了一个死亡开关：如果被盗令牌被撤销，它会删除用户的主目录；该蠕虫还感染了其他包，如 @mistralai/mistralai。

hackernews · varunsharma07 · May 11, 21:08

**背景**: npm 的 postinstall 脚本会在包安装时自动执行，并以用户系统权限运行，因此成为常见的恶意软件传播途径。供应链攻击针对软件开发和分发流程，将恶意代码注入受信任的包中。TanStack 是一个流行的开源项目，提供 React Query 和 React Router 等 React 库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://www.trendmicro.com/en_us/research/25/i/npm-supply-chain-attack.html">What We Know About the NPM Supply Chain Attack | Trend Micro (US)</a></li>

</ul>
</details>

**社区讨论**: 社区成员警告载荷安装了一个危险的死亡开关，在令牌被撤销时可能删除用户的主目录。其他人指出其他包（包括 @mistralai/mistralai）也遭到入侵。有人争论说，这次攻击表明仅靠 Trusted Publishing 是不够的，并建议使用 pnpm 来降低 postinstall 脚本的风险，同时多位评论者指责 GitHub 允许分支提交通过同一对象存储可访问。

**标签**: `#supply-chain security`, `#npm`, `#open-source`, `#security incident`, `#postinstall scripts`

---

<a id="item-4"></a>
## [GitLab 裁员并放弃 CREDIT 价值观，转向 AI 战略](https://about.gitlab.com/blog/gitlab-act-2/) ⭐️ 8.0/10

GitLab 宣布裁员，并用强调速度、主人翁精神和客户成果的新价值观取代了其长期奉行的 CREDIT 价值观（协作、成果、效率、多样性、包容、透明），这标志着公司向人工智能和智能体开发方向的战略转变。 此举反映了更广泛的行业趋势，即企业在削减成本并重新聚焦于人工智能，而常常以牺牲多元化、公平和包容（DEI）举措为代价。GitLab 的这一转变可能会影响其他 DevOps 和科技公司采取类似策略，从而可能重塑企业文化和人力优先事项。 新价值观为‘速度与质量’、‘主人翁心态’和‘客户成果’，取代了此前包含多元化、包容与归属感的 CREDIT 框架。GitLab 表示，智能体时代是其历史上最大的机遇，而公司此前的发展形态已不适合这个新时代。

hackernews · AnonGitLabEmpl · May 11, 20:51

**背景**: GitLab 是一家主要的 DevOps 平台，提供源代码管理、持续集成/持续交付以及可观测性工具。该公司此前推崇 CREDIT 价值观，其中将多元化、包容与归属感作为核心原则。此次公告同时还涉及裁员，标志着 GitLab 在文化及战略上的重大转变，公司正重新聚焦于人工智能智能体和运营效率。

**社区讨论**: Hacker News 上的社区评论大多持批评态度。许多评论者对 GitLab 向人工智能的转向表示怀疑，有人指出新价值观本质上意味着‘更努力地工作，而非更聪明地工作，并且不再有 DEI’。其他人则质疑在声称面临史上最大机遇的同时却裁员的逻辑，并担忧过度依赖 AI 机器人会导致用户体验进一步恶化。

**标签**: `#GitLab`, `#layoffs`, `#corporate values`, `#AI pivot`, `#DevOps`

---

<a id="item-5"></a>
## [Ratty：支持内嵌 3D 图形的终端模拟器](https://ratty-term.org/) ⭐️ 8.0/10

这一创新打破了终端模拟器传统上仅限文本的界限，为交互式数据可视化、调试以及融合文本与 3D 内容的开发工作流开辟了新的可能性。 Ratty 使用 Rust 和 Ratatui 构建，受 TempleOS 启发，并采用 GPU 加速渲染管线处理 .obj 和 .glb 格式的 3D 资产，支持动画、缩放和颜色属性。

hackernews · orhunp_ · May 11, 10:13

**背景**: 传统终端模拟器仅显示文本和简单字符，尽管 kitty 的图形协议等方案已支持内嵌 2D 图像。Ratty 在此基础上进一步扩展，通过 GPU 实现终端内原生 3D 对象渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/orhun/ratty">GitHub - orhun/ ratty : A GPU-rendered terminal emulator with inline ...</a></li>
<li><a href="https://ratty-term.org/">Ratty — A GPU-rendered terminal emulator with inline 3 D graphics</a></li>
<li><a href="https://blog.orhun.dev/introducing-ratty/">Ratty : A terminal emulator with inline 3 D graphics - Orhun's Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论对该概念表示热烈欢迎，有人将其与 1980 年代就具备内嵌图形的 Xerox 工作站和 Lisp 机器进行历史比较。用户还讨论了在 VR 中的应用潜力、GPU 加速带来的 SSH 兼容性问题，以及与其他创新终端（如 kitty）的比较。

**标签**: `#terminal`, `#3D graphics`, `#emulator`, `#Hacker News`, `#open-source`

---

<a id="item-6"></a>
## [Swift 中矩阵乘法从 Gflop/s 优化到 Tflop/s](https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html) ⭐️ 8.0/10

Matt Gallagher 发布了一份详细指南，介绍如何在 Apple Silicon 上优化 Swift 中的矩阵乘法以训练 LLM，性能从 Gflop/s 提升到 Tflop/s。 该文章表明，Swift 结合 Apple Silicon 的硬件加速器（如 AMX）可以在机器学习工作负载中实现有竞争力的性能，可能减少对外部 GPU 框架的依赖。它还填补了 Swift 性能优化文档方面的空白。 作者使用了 Apple 的 AMX（Apple 矩阵协处理器）指令和-ffast-math 等编译器标志来提升矩阵乘法性能。M3 Max GPU 的理论峰值约为 15 Tflop/s，但此类任务的实际上限为 3-5 Tflop/s。

hackernews · zdw · May 10, 17:05

**背景**: 矩阵乘法是训练大型语言模型（LLM）的核心操作。Apple Silicon 芯片包含一个专用的 AMX 协处理器，用于加速矩阵运算，但要有效利用它需要底层优化。Swift 是苹果开发的现代编程语言，像 MLX Swift 这样的框架正在兴起，以支持在 Apple 硬件上进行设备端机器学习研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.meekolab.com/the-elusive-apple-matrix-coprocessor-amx">The Elusive Apple Matrix Coprocessor (AMX)</a></li>
<li><a href="https://www.swift.org/blog/mlx-swift/">On-device ML research with MLX and Swift | Swift .org</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了文章的质量和新颖性，认为它填补了 Swift 性能优化文献的空白。一些人讨论了 AMX 指令的保密性、用于 FMA（融合乘加）的编译器标志，以及 Nvidia CUDA 在 GPU 计算中的软件护城河。

**标签**: `#Swift`, `#matrix multiplication`, `#performance optimization`, `#LLM`, `#Apple Silicon`

---

<a id="item-7"></a>
## [Gmail 注册现要求扫描二维码发送短信](https://discuss.privacyguides.net/t/google-account-registration-now-requires-sending-an-sms-via-phone-instead-of-receiving-an-sms/36082) ⭐️ 7.0/10

Gmail 更改了注册流程：新用户不再接收短信验证码，而是需要用手机扫描二维码，打开一条预填好的短信并发送给 Google 以验证手机号码。 这一变化将成本和隐私负担从 Google 转移给了用户，因为用户需要主动用自己的手机发送短信，可能会向 Google 暴露自己的手机号码。同时，这给没有智能手机或短信功能的用户带来了可访问性问题，也加剧了关于 Google 垄断地位和反垃圾邮件措施的持续争论。 二维码不会自动发送短信，只会打开一条预编好的短信，用户需要手动发送。这实际上是旧的电话号码验证方式，只是增加了二维码的便利性，可能是 Google 减少自动创建账号和垃圾邮件的一部分措施。

hackernews · negura · May 11, 07:26

**背景**: 此前，Gmail 注册流程是输入手机号码，然后通过短信接收验证码。新方法反转了流程：用户使用智能手机扫描 Gmail 注册页面上的二维码，这会触发一个短信 URI，用户随后将短信发送到 Google 的号码。这一变化引发了隐私担忧，因为它可能让 Google 获取用户发出的短信元数据，同时短信费用也由用户承担。此外，这可能会限制那些只使用固定电话或没有发短信功能手机的用户注册。

**社区讨论**: 社区评论呈现了复杂的情绪。一些用户同情 Google 对抗垃圾邮件和维护免费基础设施的困境，而另一些则将此举视为 Google 滥用垄断地位的又一例证。有技术澄清指出，二维码仅打开预编短信，不会自动发送任何内容。一位评论者认为，这一举动应作为反垄断案件的证据，迫使 Google 让 Gmail 独立竞争。

**标签**: `#Gmail`, `#registration`, `#privacy`, `#Google`, `#SMS verification`

---

<a id="item-8"></a>
## [AI 写代码，Python 还有必要吗？](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055) ⭐️ 6.0/10

一篇 Medium 博客文章质疑，当 AI 能够为开发者编写代码时，Python 是否还有必要；但社区评论反驳指出，Python 在训练数据中的主导地位以及人工审查的必要性使其仍然不可或缺。 这一讨论反映了开发者社区在 AI 辅助编程时代对编程语言选择日益激烈的争论，影响着团队如何决定学习、采用或弃用哪些语言。 大型语言模型（LLM）在包括大量 Python 代码在内的海量文本上训练，这使得它们生成 Python 代码的能力优于生成较冷门语言的代码。此外，AI 的代码建议经常包含错误，需要人类开发者审查和修正，因此掌握该语言仍然必要。

hackernews · indigodaddy · May 11, 20:45

**背景**: 大型语言模型（LLM）是在海量文本语料上预训练的深度学习模型，用于自然语言处理和生成，它们驱动着 GitHub Copilot 等现代 AI 编程助手。这些模型基于训练数据中的模式，通过概率方法推荐代码；而在编程领域，训练数据以 Python 为主。因此，AI 生成的代码质量因编程语言而异，开发者仍需要理解代码以验证其正确性和安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI pair programmer · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论强烈反驳了博客的论点：用户指出，Python 在训练数据中占比巨大，使得 AI 对 Python 的可靠性远高于冷门语言，而且 AI 经常犯错误，因此人工审查不可或缺。有评论者打趣说“如果 AI 写你的文章，还要脑子干嘛？”，还有评论者警告不要用团队没人懂的语言交付应用。

**标签**: `#AI coding assistants`, `#Python`, `#programming languages`, `#LLM limitations`, `#developer tooling`

---

<a id="item-9"></a>
## [TypedMemory：快速将 Java 记录映射到本地内存](https://github.com/mamba-studio/TypedMemory) ⭐️ 6.0/10

一个名为 TypedMemory 的新 Java 库允许将 Java 记录类型直接映射到堆外本地内存，旨在简化高性能数据结构。然而，社区讨论质疑该库是否真正实现了零分配，因为 getter 和 setter 可能仍然会分配记录对象。 该库解决了 Java 中对类型安全、堆外数据访问的长期需求，这对低延迟和大规模应用至关重要。然而，如果未能消除对象分配，性能优势可能受限，从而降低其在零分配场景下的实际价值。 TypedMemory 使用 Java 记录定义数据布局，并提供 getter 等方法，每次调用可能实例化新的记录对象，这可能削弱其零分配的声称。该库缺乏与 SBE 或 GraalVM 等成熟替代方案的直接性能对比。

hackernews · joe_mwangi · May 11, 19:33

**背景**: Java 中的堆外内存是指在 Java 堆之外分配的内存，不受垃圾回收管理，可提高延迟敏感型应用的性能和可预测性。Java 记录是 Java 16 引入的一种简洁语法，用于声明不可变的数据载体。像 TypedMemory 这样的库试图结合记录的类型安全与堆外存储的性能，但在访问过程中避免对象分配是此类设计的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/manojkhanwalkar/offheap">GitHub - manojkhanwalkar/ offheap : Data structures that utilize...</a></li>
<li><a href="https://www.w3computing.com/articles/how-to-use-javas-unsafe-class-for-low-level-programming/">How to Use Java 's Unsafe Class for Low-Level Programming</a></li>
<li><a href="https://github.com/OpenHFT/Zero-Allocation-Hashing">GitHub - OpenHFT/Zero-Allocation-Hashing: Zero-allocation hashing for Java</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该库的零分配声称持怀疑态度，指出 getter 方法可能在堆上创建新的记录对象，在高性能场景下适得其反。一些评论者建议与 SBE 或 GraalVM 等成熟框架进行对比，而另一些则认为如果通过享元模式或代码生成解决分配问题，则具有潜力。

**标签**: `#java`, `#off-heap`, `#memory-mapping`, `#records`, `#performance`

---