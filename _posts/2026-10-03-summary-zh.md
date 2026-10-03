---
layout: default
title: "Horizon Summary: 2026-10-03 (ZH)"
date: 2026-10-03
lang: zh
---

> 从 37 条内容中筛选出 15 条重要资讯。

---

**科技新闻**
1. [AI 击败史上最强 Stratego 玩家且训练成本大幅降低](#item-tech-news-1) ⭐️ 9.0/10
2. [Greg Kroah-Hartman 谈 LLM 时代内核安全](#item-tech-news-2) ⭐️ 8.0/10
3. [Google 公布 Cogentic 多智能体数学证明系统](#item-tech-news-3) ⭐️ 8.0/10
4. [Redis 作者推出本地 LLM 推理引擎 ds4](#item-tech-news-4) ⭐️ 7.0/10
5. [Zig v0.17.0 发布：生态与工具链改进](#item-tech-news-5) ⭐️ 7.0/10
6. [FLEET：用奖励记忆和 MCTS 增强 Best-of-N](#item-tech-news-6) ⭐️ 7.0/10
7. [Anthropic 提议澳大利亚允许以退出机制训练版权作品](#item-tech-news-7) ⭐️ 7.0/10
8. [arXiv 全面限投：每人每月仅限 2 篇](#item-tech-news-8) ⭐️ 7.0/10
9. [Claude Code 新增 mods 自定义功能](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare 推出统一可观测性平台](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [美国 9 月就业报告疲弱，10 月美联储加息概率骤降](#item-finance-news-1) ⭐️ 8.0/10
2. [午间异动股：特斯拉 Q3 交付超预期，博通据报向 Anthropic 贷款 420 亿美元](#item-finance-news-2) ⭐️ 7.0/10
3. [盘前异动：耐克营收不及预期跌超 10%，安森美收购 Synaptics，硬盘股承压](#item-finance-news-3) ⭐️ 7.0/10
4. [华尔街银行 AI 岗位激增，智能体编排技能需求一年涨 1721%](#item-finance-news-4) ⭐️ 7.0/10
5. [Bitget 遭黑客攻击损失近 3.88 亿美元，CEO 预计只能追回少量资金](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [AI 击败史上最强 Stratego 玩家且训练成本大幅降低](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10

一项新的强化学习算法击败了历史上最强的 Stratego 玩家，这是 AI 在隐藏信息游戏领域的重要里程碑。与 DeepMind 此前发布的 DeepNash 相比，新算法的训练成本大幅降低，约只用了 DeepNash 三十四分之一的训练对局，最终却更强。该成果已发表在《自然》杂志，并在 arXiv 上提供预印本。Stratego 的大部分棋子信息对对手隐藏，此前长期难倒 AI；新方法提升了样本效率，证明隐藏信息博弈可以用更少对局掌握。

hackernews · PaulHoule · 10月2日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49933740)

**「背景」** Stratego 是一款双方棋子身份互相隐藏的经典棋盘游戏，属于不完全信息博弈：当前局面下看似合理的行动，可能因为对手隐藏的棋子而变成坏棋，因此无法像国际象棋、围棋那样进行完全搜索。2022 年 DeepMind 的 DeepNash 使用无模型多智能体强化学习从零学习，达到了人类专家水平，但尚未稳定击败顶尖人类玩家。新的工作在此基础上重点改进样本效率，用远少于 DeepNash 的训练对局数实现了对历史最佳玩家的超越。

**「影响」** 这一结果证明隐藏信息游戏可以通过样本高效的强化学习掌握，有望降低未来游戏 AI 和类似决策任务的训练计算门槛。

**「社区讨论」** 多位评论者回忆童年玩 Stratego；技术讨论集中在样本效率上，有人指出比 DeepNash 少约 34 倍训练对局却更强是关键。也有评论认为 2022 年 DeepMind 所称的“掌握”其实并未真正超越人类，新方法才做到了这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.15378">[2206.15378] Mastering the Game of Stratego with Model-Free...</a></li>

</ul>
</details>

**标签**: `#Stratego`, `#reinforcement learning`, `#hidden information games`, `#game AI`, `#sample efficiency`

---

<a id="item-tech-news-2"></a>
### [Greg Kroah-Hartman 谈 LLM 时代内核安全](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

Greg Kroah-Hartman 在一场演讲中分析了 AI 生成的内核漏洞报告的可靠性，重点拆解了 Anthropic 的 Mythos 声称发现的 79 个漏洞。他将这 79 个报告分为：24 个没有任何细节、14 个根本不是缺陷、3 个数据完全虚构、15 个在最新版本中已修复（其中 11 个由他人修复、4 个由 Anthropic 修复），只有 20 个确实需要修复。他指出 Mythos 实际上是对过去几十年内核开发者的补丁进行模式匹配，并把机制套用到其他地方，而不是真正的漏洞发现，且没有引用原始修复者。他总结称这场被广泛宣传的 79 个漏洞最终只相当于一小时的内核开发工作。

hackernews · usernomdeguerre · 10月2日 02:51 · [社区讨论](https://news.ycombinator.com/item?id=49929391)

**「背景」** Greg Kroah-Hartman 是 Linux 内核的长期维护者，本次演讲来自 2026 年 Kernel Recipes 会议。他重点核查了 Anthropic 的 Mythos 系统声称在 Linux 内核中发现的 79 个 CVE 漏洞，并公开了逐项检查结果。CVE 是公开的漏洞编号，而 Linux 内核作为开源项目，其补丁历史和代码变更均可公开追溯，这为验证 AI 生成的漏洞报告提供了条件。

**「影响」** 对依赖 LLM 进行内核漏洞分析的开发者和安全团队而言，当前 Mythos 的报告需逐条人工核实，大量内容缺少细节或并非缺陷，不能直接作为修复或安全决策依据。

**「社区讨论」** 评论普遍认可 Greg Kroah-Hartman 的直接批评，指出 Mythos 只是模式匹配历史补丁且未引用原始内核开发者；也有评论认为虽然当前效果不佳，但针对 Linux 内核特化的模型未来可能显著提升漏洞发现与修复效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=NnV_cWeoo5Q">Kernel Recipes 2026 - Security in the LLM age - YouTube</a></li>
<li><a href="https://news.ycombinator.com/item?id=49929391">Greg Kroah - Hartman – Security in the LLM Age [video] | Hacker News</a></li>

</ul>
</details>

**标签**: `#linux-kernel`, `#security`, `#llm`, `#vulnerability-analysis`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [Google 公布 Cogentic 多智能体数学证明系统](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10

Google Research 在 arXiv 上公布了 Cogentic，一套用于自动发现数学证明的多智能体系统。该系统采用“证明—验证”循环，让多个独立证明器探索不同方向，由专门组件进行对抗式验证，并将已确认结果存入可持续使用的验证账本。Cogentic 以 Gemini 为基础模型，在在线学习、拍卖理论和机制设计领域的 5 个开放问题上产出了新结果。这些结果均已由领域专家独立验证，并在配套论文中展开。若得到确认，这是多智能体自动定理证明在开放数学问题上的重要进展。

telegram · zaihuapd · 10月2日 12:04

**「背景」** Cogentic 是 Google Research 在 arXiv 上提出的多智能体证明发现系统（论文《Cogentic: Multi-Agent Orchestration for Automated Proof Discovery》），其核心是用多个独立证明器探索不同方向，并由对抗式验证组件检查结果，已确认的证明存入可持续使用的验证账本。该系统以 Gemini 为基础模型，属于大语言模型推理与自动定理证明的结合，试图仅从问题陈述出发处理理论计算机科学中的开放问题，而不依赖专家提示。

**「影响」** 对在线学习、拍卖理论和机制设计领域的研究者来说，Cogentic 提供了 5 个经独立验证的新开放问题结果，并展示了一种可复用的“证明—对抗验证”多智能体流程，有望降低人工验证成本。但其最终影响仍需等待正式同行评议和复现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic : Multi - Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://agihunt.info/en/e/1a0f9cea5c8b68af181e13c5f80">Google &#x27;s Cogentic Multi - Agent System Tackles… · AGI Hunt</a></li>
<li><a href="https://arxiv.org/abs/2609.40324">[2609.40324] Cogentic: Multi-Agent Orchestration for ...</a></li>
<li><a href="https://arxiv.org/html/2609.40324v1">Cogentic: Multi-Agent Orchestration for Automated Proof Discovery</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#automated theorem proving`, `#AI for mathematics`, `#Google Research`, `#Gemini`

---

<a id="item-tech-news-4"></a>
### [Redis 作者推出本地 LLM 推理引擎 ds4](https://dwarfstar.sh/) ⭐️ 7.0/10

ds4 是一个由 Redis 作者（antirez）开发的开源本地 LLM 推理引擎，HN 帖子链接到 dwarfstar.sh 作为入口。社区讨论显示，已有维护者将其 fork 为共享库并可通过 FFI 供其他语言调用（例如 ds4go），并跟随 ds4 上游添加了 Vision 和 Qwen 支持。有用户报告在 Apple M5 Max 128GB 上运行 DeepSeek V4 Flash 和 Qwen 3.8 Flash，称速度快且上下文窗口长，但偶尔出现模型忘记前文的情况，可能来自 agentic AI harness。也有评论者关心工具调用能力，指出 GitHub 仓库暗示 SSD 即可运行，并询问是否接近 50 TPS；另有人受 DwarfStar 启发开发了面向 Intel Xe-LP（无 XMX）的推理引擎，目前仅支持量化 Gemma-4。

hackernews · fibo · 10月2日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49936575)

**「背景」** ds4（DwarfStar 4）是 Redis 创始人 antirez 开发的窄向本地推理引擎，用 C 语言编写，面向高内存 Mac、CUDA 和 ROCm 机器。它支持 DeepSeek V4 和 V4.1 Flash、GLM 5.x 以及 Qwen3.8 Flash Next 等文本和视觉模型，并提供本地 API、命令行界面和原生 agent。ds4 -agent 直接运行推理，不依赖单独的 HTTP 服务器，同时保留 token 历史和实时模型状态。

**「影响」** 对于希望在本地运行大模型的开发者和用户，社区提供的 FFI 绑定与多个语言工具降低了集成门槛，但性能数据（如工具调用和 TPS）目前主要来自个人报告，尚未有官方基准验证。

**「社区讨论」** 评论总体对 ds4 在 Apple silicon 上的速度和长上下文表现表示认可，但对其工具调用能力和准确 TPS 仍存疑问；一名维护者提供的 fork 和 Go 绑定表明扩展性良好，而另一名用户指出模型偶尔忘记前文可能是 agent 框架的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local ...</a></li>
<li><a href="https://dwarfstar.sh/">DwarfStar 4 (ds4): Local DeepSeek V4.1, Qwen and GLM</a></li>
<li><a href="https://dwarfstar.sh/about/">About DwarfStar 4 (ds4): antirez Local Inference Engine</a></li>

</ul>
</details>

**标签**: `#local-llm`, `#inference-engine`, `#open-source`, `#ai`, `#software-engineering`

---

<a id="item-tech-news-5"></a>
### [Zig v0.17.0 发布：生态与工具链改进](https://ziglang.org/download/0.17.0/release-notes.html) ⭐️ 7.0/10

Zig 编程语言发布了 v0.17.0。根据发布说明与社区反馈，本次更新主要集中在生态系统和工具链改进，包括构建集成与目标平台支持方面的增强。社区讨论还提到核心维护者 Andrew Kelley 对使用 LLM 辅助发现程序漏洞持更务实态度，并将其视为通往无缺陷软件的工具之一。Zig 目前仍处于 1.0 之前的阶段，语言与生态尚不稳定但正在改善。

hackernews · ErenayDev · 10月2日 20:56 · [社区讨论](https://news.ycombinator.com/item?id=49938521)

**「背景」** Zig 是一种注重性能与控制的系统编程语言，常被看作 C 的潜在替代品。0.17.0 是 Zig 走向 1.0 版本的一个稳定化步骤，发布于 0.16.0 之后；该版本重新设计了构建系统，改进了增量编译，并调整了若干语言规则。根据 release notes，对于 x86\_64-linux 上的大多数项目，修改后可以更快地重新构建和验证代码。

**「社区讨论」** 社区总体对 Zig 的构建集成和跨平台目标支持表示欢迎，并认为其设计出色，但仍有用户对其 1.0 前的不稳定和小生态表示担忧。也有用户反映过去对核心成员沟通方式不满并转向 Odin，同时讨论中提到项目对 LLM 的态度正在从强硬转向务实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ziglang.org/download/0.17.0/release-notes.html">0 . 17 . 0 Release Notes The Zig Programming Language</a></li>
<li><a href="https://dzen.ru/a/asAsBEZa4EPtW32L">Zig 0 . 17 . 0 : быстрые пересборки становятся реальностью, но... | Дзен</a></li>

</ul>
</details>

**标签**: `#zig`, `#programming-languages`, `#systems-programming`, `#release-notes`, `#compilers`

---

<a id="item-tech-news-6"></a>
### [FLEET：用奖励记忆和 MCTS 增强 Best-of-N](https://www.reddit.com/r/MachineLearning/comments/1wvs12j/adding_memory_to_search_instead_of_sampling_in/) ⭐️ 7.0/10

FLEET 通过将外部奖励归因到具体 token，并在后续生成中利用 MCTS 调整 logits，增强 Best-of-N 生成。它跟踪 logits 熵和 varentropy 较高处作为分支点，将归一化隐藏状态存入向量库并关联奖励历史与节点转移元数据，检索时基于余弦相似度更新。修改后的 MCTS 对 top-k token 和探索集合排序并惩罚次优 token，再对修改后的 logits 应用解码策略。在 Llama 3.2 3B 上测试 GSM8K 和 LiveCodeBench v6 easy split，结合将次优 token 概率设为零和贪心解码：GSM8K 多解决 7 题但用一半迭代达到采样基线，LiveCodeBench 相同预算下分数从 0.59 提升到 0.69，仅用 9 次迭代达到基线而基线需要 32 次。算法不需要顺序执行，元数据存储可作为其他任务或 SFT/RL 的先验。

reddit · r/MachineLearning · /u/Helpful\_Minimum\_2214 · 10月2日 12:04

**「背景」** Best-of-N 是重复采样多个候选并依据外部奖励选择最佳结果的常见推理策略，但传统方法不利用奖励信息调整采样过程。MCTS（蒙特卡洛树搜索）通常用于通过树搜索和奖励回溯优化决策；FLEET 将其适配到语言模型 token 选择中。

**「影响」** 对于使用 Llama 3.2 3B 在 GSM8K 或 LiveCodeBench easy split 上进行 Best-of-N 的研究者，FLEET 声称可在相同预算下提升结果或显著减少达到基线的迭代次数（例如 LiveCodeBench 从 32 次降至 9 次）。目前这些结果来自作者预印本，尚需独立复现。

**标签**: `#machine learning`, `#reinforcement learning`, `#large language models`, `#MCTS`, `#inference optimization`

---

<a id="item-tech-news-7"></a>
### [Anthropic 提议澳大利亚允许以退出机制训练版权作品](https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news) ⭐️ 7.0/10

Anthropic 建议澳大利亚政府有条件批准科技公司在“退出”机制下使用澳大利亚受版权保护的作品训练 AI 模型。ABC 和 SBS 反对放宽版权规则，要求 AI 公司接受版权、隐私等监管并补偿媒体，ABC 警告新闻业可能被“蚕食”。澳政府已排除建立文本和数据挖掘豁免，但仍在讨论其他版权安排；澳大利亚议会人工智能联合委员会将于下周举行听证，Anthropic 和 OpenAI 高管将出席。

telegram · zaihuapd · 10月2日 03:34

**「背景：退出机制与澳大利亚版权框架」** Anthropic 是一家定位为 AI 安全与研究的公司，其提出的“退出”机制与“选择加入”相反：默认允许使用受版权保护的内容训练模型，除非权利人主动声明退出。澳大利亚目前未设立文本和数据挖掘豁免，科技公司在训练生成式模型时通常需要寻求版权授权或其他合法依据。这一机制对比是理解相关争议的基础。

**「影响」** 若该提案被采纳，澳大利亚版权人需主动选择退出，否则其作品可被 AI 公司用于训练，而公共广播机构 ABC 和 SBS 将面临缺少强制补偿的监管风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news">Anthropic pushes for opt - out model for Australian content as ABC ...</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#copyright`, `#Anthropic`, `#Australia`, `#generative AI`

---

<a id="item-tech-news-8"></a>
### [arXiv 全面限投：每人每月仅限 2 篇](https://www.huxiu.com/article/4895127.html) ⭐️ 7.0/10

自 10 月 1 日起，全球最大预印本平台 arXiv 实施新规，每位提交者每个自然月最多提交 2 篇论文，覆盖全部学科，且被拒稿件也占用当月额度。9 月投稿量达到 40363 篇，创 35 年新高；其中 AI 分类论文两年增长超过 6 倍，大量低质量 AI 生成论文挤占人工审核资源。多作者论文只计算实际提交者，其余合著者不受影响。该政策旨在应对 AI 生成投稿激增和创纪录的提交量。

telegram · zaihuapd · 10月2日 06:21

**「背景」** arXiv 是全球广泛使用的预印本平台，研究人员在正式同行评审前发布成果，尤其在人工智能、计算机和机器学习领域影响重大。随着生成式 AI 工具普及，平台出现大量疑似 AI 生成的论文，增加了审核负担。

**「影响」** 对于依赖 arXiv 快速公开研究成果的研究者，该限额意味着需要更谨慎地规划投稿顺序和数量，且被拒稿件也会消耗每月配额。

**标签**: `#arXiv`, `#academic publishing`, `#AI-generated content`, `#research policy`, `#open science`

---

<a id="item-tech-news-9"></a>
### [Claude Code 新增 mods 自定义功能](https://claude.com/blog/claude-code-mods) ⭐️ 7.0/10

Anthropic 为 Claude Code 推出 mods 功能，开发者可以用少量 TypeScript 代码改写提示词、新增界面或替换内置功能。Mods 随插件分发，现已支持 CLI 和桌面版。Mods 与 Claude Code 具有相同权限且不设沙箱，官方提醒只安装可信来源；用户也可以让 Claude 自行编写 mods。部分内置功能已改为 mods，官方计划后续迁移更多。

telegram · zaihuapd · 10月2日 12:32

**「背景」** Claude Code 是 Anthropic 提供的 AI 编程助手，可在命令行和桌面应用中使用。Mods 是通过 TypeScript 编写的扩展插件，能让开发者在不修改核心代码的情况下定制工具行为；这类插件通常通过插件系统分发，但此处的 mods 与主程序权限相同。

**「影响」** 对于 Claude Code 的开发者用户，新功能允许以较低代码量深度定制提示词、界面和内置功能，但由于 mods 无沙箱且权限与主程序一致，必须只安装可信来源的插件。

**标签**: `#Claude Code`, `#Anthropic`, `#developer tools`, `#AI coding`, `#plugins`

---

<a id="item-tech-news-10"></a>
### [Cloudflare 推出统一可观测性平台](https://blog.cloudflare.com/one-observability-platform/) ⭐️ 7.0/10

Cloudflare 于 2026 年 10 月 2 日宣布推出 8 项更新，将日志、追踪、分析、告警、仪表板和数据导出整合到统一可观测性平台。更新包括处于开放测试中的请求追踪和统一 SQL API、30 天域名分析数据、自定义告警和自定义仪表板；Logpush 也向所有自助服务计划开放。日志和追踪的新统一计费模式将于 2026 年 12 月 1 日生效，按摄入和存储量计费。这些更新对依赖 Cloudflare 的工程团队而言，扩展了自助服务计划的使用范围，并提供更集中的可观测性能力。

telegram · zaihuapd · 10月3日 01:15

**「背景」** 可观测性是通过日志、追踪和指标来了解系统运行状态的一套实践，工程团队用它定位故障并分析性能。Cloudflare 此前已提供 Logpush、分析和日志等分散的功能，此次将这些能力统一到同一平台，并引入统一 SQL API 来降低跨数据源查询的复杂度。

**「对 Cloudflare 用户的影响」** 对于依赖 Cloudflare 的工程团队，Logpush 现已向自助服务计划开放，且从 2026 年 12 月 1 日起日志和追踪将按摄入与存储量统一计费，这可能改变其可观测性成本与数据导出方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/one-observability-platform/">8 major updates to Cloudflare Observability | Cloudflare Blog</a></li>
<li><a href="https://blog.cloudflare.com/one-observability-platform/">8 major updates to Cloudflare Observability | Cloudflare Blog</a></li>
<li><a href="https://www.brocker.org/cloudflare-observability-eight-updates-logs-traces-sql-api-pricing">Cloudflare Unifies Observability With 8 Updates, New Pricing</a></li>
<li><a href="https://dropagentic.com/cloudflare-observability-updates-unified-platform/">Cloudflare launches eight observability updates</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#observability`, `#logging`, `#tracing`, `#analytics`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国 9 月就业报告疲弱，10 月美联储加息概率骤降](https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html) ⭐️ 8.0/10

美国 9 月非农就业仅新增 2.9 万人，低于市场预期的 8 万以上，交易员因此大幅下调美联储 10 月加息概率；CME FedWatch 工具显示概率从一周前约 36%降至 17%，预测平台 Kalshi 从近 70%降至 18%。市场仍预计美联储将在 12 月加息，FedWatch 概率超过 75%，Kalshi 为 65%。

rss · CNBC Finance · 10月2日 13:29

**「背景」** 美联储在 9 月会议上刚将政策利率目标区间上调 25 个基点至 3.75%–4%，理由是通胀仍高于目标；9 月就业报告仅新增 2.9 万个岗位，远低于 8 万以上的预期，使交易员下调了对 10 月继续加息的押注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html">Fed rate decision September 2026 : Rates rise to 3.75%-4%</a></li>

</ul>
</details>

**标签**: `#Federal Reserve`, `#interest rates`, `#jobs report`, `#inflation`, `#market expectations`

---

<a id="item-finance-news-2"></a>
### [午间异动股：特斯拉 Q3 交付超预期，博通据报向 Anthropic 贷款 420 亿美元](https://www.cnbc.com/2026/10/02/stocks-making-the-biggest-moves-midday-tsla-avgo-nke-on-more-.html) ⭐️ 7.0/10

CNBC 午间异动股综述显示，特斯拉第三季度交付 486,532 辆，高于 FactSet 调查分析师预期的 461,100 辆，股价上涨 5%；博通涨逾 3%，因路透社报道其同意向 Anthropic 提供最高 420 亿美元融资。

rss · CNBC Finance · 10月2日 17:52

**「背景」** FactSet 与 LSEG 的调查数据为相关业绩对比基准；路透社报道博通对 Anthropic 的贷款将用于后者购买或租赁芯片等计算硬件。

**标签**: `#stock movers`, `#earnings`, `#mergers and acquisitions`, `#semiconductors`, `#electric vehicles`

---

<a id="item-finance-news-3"></a>
### [盘前异动：耐克营收不及预期跌超 10%，安森美收购 Synaptics，硬盘股承压](https://www.cnbc.com/2026/10/02/stocks-making-the-biggest-moves-premarket-nike-on-semiconductor-synaptics-vylor-more.html) ⭐️ 7.0/10

盘前多只个股大幅波动。耐克第一财季营收不及 LSEG 共识、销售下降 4%，股价跌超 10%；安森美据报将以每股 123 美元现金收购 Synaptics，交易估值 57 亿美元，Synaptics 涨超 14%、安森美涨超 7%；东芝据报将倍增数据中心硬盘产能并投资 3.8 亿美元，希捷和西部数据分别跌超 11%和 8%。

rss · CNBC Finance · 10月2日 12:03

**「背景」** 安森美与 Synaptics 的收购协议在 10 月 1 日修改，由全股票安排改为每股 123 美元现金，交易估值约 57 亿美元，因出现了第三方竞争性报价。硬盘驱动器（HDD）市场上，东芝、西部数据和希捷几乎占据全部份额，而东芝此次 3.8 亿美元菲律宾扩产是 AI 存储需求紧张以来三者中首次大规模扩产。

**「对耐克股东和员工的影响」** 耐克财年第一季度收入下降 4%、中国区收入骤降，导致股价盘前走低；公司计划 2027 年开始裁员，直接冲击现有员工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/semiconductor-climbs-8-synaptics-surges-131302389.html?ref=biztoc.com">On Semiconductor Climbs 8%, Synaptics Surges 14% as...</a></li>
<li><a href="https://finviz.com/news/398186/synaptics-shares-rise-138-after-merger-terms-revised-to-123-per-share-cash-offer">Synaptics Shares Rise 13.8% After Merger Terms Revised to...</a></li>
<li><a href="https://www.alphapilot.tech/discover/toshiba-doubles-hdd-supply-by-fiscal-2027-seagate-western-digital-tumble">Toshiba Doubles HDD Supply by Fiscal 2027: Seagate , Western ...</a></li>
<li><a href="https://www.trendforce.com/news/2026/10/02/news-toshiba-to-double-ai-data-center-hdd-capacity-by-fy2027-with-380m-expansion-as-ai-storage-demand-surges/">[News] Toshiba to Double AI Data Center HDD Capacity by FY2027...</a></li>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/nike-q1-2027-earnings-job-133725772.html?fr=sycsrp_catchall">Nike Q1 2027 earnings: job cuts, revenue outlook, China sales</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/nike-quarterly-sales-miss-estimates-china-weakness-competition-weigh-2026-10-01/">Nike quarterly sales miss estimates as China weakness ...</a></li>

</ul>
</details>

**标签**: `#earnings`, `#mergers and acquisitions`, `#semiconductors`, `#hard disk drives`, `#stock market`

---

<a id="item-finance-news-4"></a>
### [华尔街银行 AI 岗位激增，智能体编排技能需求一年涨 1721%](https://www.cnbc.com/2026/10/02/ai-skills-most-in-demand-at-jpmorgan-chase-citigroup-capital-one.html) ⭐️ 7.0/10

根据 Draup 为 CNBC 独家提供的分析，摩根大通、花旗和 Capital One 等银行的 AI 相关职位今年较 2025 年增长 49%，达到 139,819 个招聘信息；其中“智能体编排”技能提及次数激增 1,721%。

rss · CNBC Finance · 10月2日 11:03

**「背景」** 此前银行 AI 招聘以构建或适配模型的工程师和数据科学家为主，如今需求正扩展到把 AI 直接嵌入交易、后台和人力资源等业务线的岗位。

**「影响」** 据 Draup 数据，生成式 AI 经理的基本工资中位数约为 19 万美元，但银行仍难招到足够人才，正通过内部再培训现有开发人员和领域专家来补缺。

**标签**: `#AI`, `#Wall Street`, `#jobs`, `#banking`, `#agent orchestration`

---

<a id="item-finance-news-5"></a>
### [Bitget 遭黑客攻击损失近 3.88 亿美元，CEO 预计只能追回少量资金](https://www.cnbc.com/2026/10/02/bitget-crypto-stolen-hack-recovery.html) ⭐️ 7.0/10

加密货币交易所 Bitget 在近期的黑客攻击中损失近 3.88 亿美元，已冻结约 110 万美元；CEO Gracy Chen 对 CNBC 表示，预计只能追回少量资金，但用户账户余额未受影响，保护基金也已得到补充。

rss · CNBC Finance · 10月2日 06:03

**「背景」** Mandiant 和 SlowMist 发布的调查显示，攻击者先攻破两款第三方安全产品，其中最早在 8 月 31 日利用一款产品的零日漏洞，获取内部权限后绕过正常客户提现流程，但未窃取私钥。

**「影响」** 受事件影响，比特币、以太币和 USDT 提现已恢复，其余加密货币及法币、P2P 服务计划周五恢复，财务冲击由平台自有资本承担。

**标签**: `#cryptocurrency exchange`, `#cyberattack`, `#Bitget`, `#asset recovery`, `#security`

---