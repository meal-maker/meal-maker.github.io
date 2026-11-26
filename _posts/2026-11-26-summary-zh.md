---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 31 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [Scott Aaronson 博客讨论 AI 数学进展与矩阵乘法指数 9/4 声明](#item-tech-news-1) ⭐️ 8.0/10
2. [1Password 披露 2026 年 11 月安全事件：疑遭生产环境恶意代码推送](#item-tech-news-2) ⭐️ 8.0/10
3. [GRH Lean 证明缩短 99.56% 且文档更完善](#item-tech-news-3) ⭐️ 8.0/10
4. [Google 发布 Cogentic 研究论文：整数分解与离散对数等](#item-tech-news-4) ⭐️ 8.0/10
5. [Minecraft Java 版 1.20.5 起曝高危 RCE 漏洞](#item-tech-news-5) ⭐️ 8.0/10
6. [Ubuntu 安全更新响应迟缓受关注](#item-tech-news-6) ⭐️ 7.0/10
7. [评估近期模型在 GDPx 基准上的表现](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI 押注网络安全，称市场规模被低估](#item-tech-news-8) ⭐️ 7.0/10
9. [腾讯混元开源 224B Hy4 flash GGUF 量化权重](#item-tech-news-9) ⭐️ 7.0/10
10. [亚洲数据中心转售过剩 AI 算力给美国客户](#item-tech-news-10) ⭐️ 7.0/10
11. [三星和 SK 海力士据传采用长江存储 Xtacking 堆叠技术](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [美国拟对中国、欧盟等 14 个贸易伙伴加征新关税](#item-finance-news-1) ⭐️ 9.0/10
2. [美商务部被曝威胁英特尔交 10%股权，价值约 110 亿美元且未付对价](#item-finance-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Scott Aaronson 博客讨论 AI 数学进展与矩阵乘法指数 9/4 声明](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

该 Hacker News 提交链接至 Scott Aaronson 的博客文章《Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening》，内容涉及近期由 AI 推动的数学进展，并提及一项被声称的矩阵乘法指数 9/4 的结果。矩阵乘法指数是衡量矩阵乘法算法效率的关键参数，数值越低代表算法越快；9/4 远低于过去数十年公开文献中常见的最佳上界，因此若属实将是一项重大突破。但该提交本身仅包含标题、链接和一条“另见”指向相关 PDF，缺乏可验证的技术细节，且 9/4 的结果尚未在材料中被确认为经过同行评议或复现。评论区既有人认为 AI 在公理化数学上的成功不必然推广到其他领域或带来科幻式风险，也有人将其视为人类认知交接的标志性事件。

hackernews · Kotlopou · 11月25日 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**「背景」** 矩阵乘法指数 ω 描述两个 n×n 矩阵相乘所需算术运算的渐近复杂度 n^ω；自 1969 年 Strassen 算法首次将 ω 从 3 降到 2.81 以下后，该指数的理论下界长期未定。OpenAI 于 2026 年 11 月 24 日发布 111 页预印本《The matrix multiplication exponent is nine fourths》，声称证明 ω 恰为 9/4=2.25，即矩阵乘法复杂度约为 n^\{2.25\} 且无法再降低。该论文同时提供 Lean 形式化验证，其核心论证表明更小的指数会压缩张量网络并违背针对多个独立列表去重问题的下界。

**「潜在影响」** 该预印本及其 Lean 形式化将矩阵乘法指数精确确定为 9/4，在任意域上为平方矩阵乘法建立了匹配的上下界，这意味着（若结果成立）不存在比 O\(n^\{2.25\}\) 更快的通用矩阵乘法算法，从而封顶了数十年来的渐近加速空间。

**「社区讨论」** 评论区观点分歧明显：jsLavaGoat 认为 AI 擅长公理化数学并不代表它能解决其他领域或带来生存风险；Nevermark 则认为人类在生物和心理上都无法对这场认知交接做出足够强烈的反应。sunir 从 Bruno Latour 的“计算中心”角度解释这类组织化工作的历史意义，而 utopiah 质疑这一突破是否主要来自 Lean、MathLib 等既有工具和大量算力，而非 LLM 或生成式 AI 的独特贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">The matrix multiplication exponent is nine fourths</a></li>
<li><a href="https://www.advanceintelligence.ai/story/2026-11-24-22">OpenAI Posts a 111 Page Proof That the Matrix Multiplication ...</a></li>
<li><a href="https://lilting.ch/en/articles/matrix-multiplication-exponent-nine-fourths-openai">Checking OpenAI&#x27;s 9/4 Matrix Multiplication Exponent Paper ...</a></li>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>
<li><a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/README.md">math /preprints/The- matrix - multiplication - exponent -is...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#mathematics`, `#matrix multiplication`, `#theoretical computer science`, `#research`

---

<a id="item-tech-news-2"></a>
### [1Password 披露 2026 年 11 月安全事件：疑遭生产环境恶意代码推送](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 披露了 2026 年 11 月的一起安全事件，涉及向生产服务推送恶意代码的可能性。该事件引发了人们对 SaaS 供应链攻击的担忧；安全专家 tptacek 评论称，此类攻击是 SaaS 公司面临的最重要攻击向量，员工笔记本电脑被入侵后攻击者可能将代码推送到 GitHub 并部署。一位用户报告收到高质量钓鱼邮件，邮件引用其 1Password 保管库中的条目并声称创建了对外共享链接，可能与事件相关。其他评论质疑 1Password 是否缺少分支保护规则，并呼吁明确说明“加密保管库未被下载”。

hackernews · lxhrstn · 11月25日 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**「背景」** 软件即服务（SaaS）供应链攻击通常指攻击者通过入侵开发者代码仓库或部署管道，将恶意代码推送到生产环境以窃取数据。1Password 的客户保管库采用端到端加密，其用户保管库内容与后端管理数据分离存储。2026 年 11 月 19 日，该公司确认员工 GitHub 账号被入侵并被用于推送恶意代码，但官方声明强调客户保管库内容及密钥未被访问或泄露。

**「影响」** 1Password 用户可能因事件相关数据泄露而面临针对性钓鱼攻击。

**「社区讨论」** 评论中，安全专家认为这是 SaaS 供应链攻击的标准模式，并强调员工设备被入侵后推送代码的风险；用户则关注 1Password 是否缺少分支保护规则，以及事件声明中未明确说明加密保管库是否被下载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.1password.community/announcements-52/update-on-a-security-incident-involving-1password-s-backend-systems-customer-vaults-were-not-affected-and-all-vault-contents-remain-secure-26259">Update on a security incident involving 1Password’s backend ...</a></li>

</ul>
</details>

**标签**: `#security`, `#saas`, `#supply-chain-attack`, `#password-manager`, `#incident-response`

---

<a id="item-tech-news-3"></a>
### [GRH Lean 证明缩短 99.56% 且文档更完善](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

一个 GitHub 仓库（lsernau/grh-lean）发布了 Anthropic 广义黎曼假设（GRH）证明的 Lean 形式化大幅缩短版本。该版本将原始证明从约 1700 万行压缩至约 7.6 万行，减少了 99.56%，同时保持了清晰的“已知数学”与“新数学”划分以及遍布各处的人类可读文档。与原版相比，新版本的代码组织和解释更为清晰，显著降低了审查门槛。这一改进使这一由 AI 辅助产生的重要数学结果对形式化验证社区更加可审查和实用。

hackernews · nb-t · 11月25日 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**「背景」** Lean 4 是一种基于依赖类型论的交互式定理证明器，Mathlib 是其数学库；此前 Anthropic 对黎曼假设（RH）及狄利克雷 L 函数的广义黎曼假设（GRH）的形式化证明包含约 1700 万行代码，难以审阅。该新仓库 lsernau/grh-lean 提供了两个版本：约 30 万行的可读版和约 7.6 万行的紧凑版，只需使用 propext、Classical.choice 和 Quot.sound 三条公理，并可在 1 到 2 小时内完成构建。

**「影响」** 对于形式化验证研究人员和数学家，这一缩短版使审计 GRH 证明的成本大幅降低，因为行数减少且文档更完善。

**「社区讨论」** 社区讨论总体积极，评论提到更可读的证明有清晰的“已知数学”与“新数学”划分以及人类可读文档。也有评论质疑这是否回应了陶哲轩关于“巨大证明缺乏洞察力”的担忧，并希望出现传统的数学论文和会议报告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lsernau/grh-lean">GitHub - lsernau/grh-lean: A short Lean 4 proof of the ...</a></li>
<li><a href="https://ashutoshai.com/ai-compass/2026/11/25/anthropic-compact-lean-4-grh-proofs/">Anthropic releases 76k-line compact Lean 4 proofs of RH and GRH</a></li>
<li><a href="https://math.mit.edu/~drew/shortgrh/">Shorter GRH Lean proof: verification files - MIT Mathematics</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean`, `#AI`, `#mathematics`, `#GRH`

---

<a id="item-tech-news-4"></a>
### [Google 发布 Cogentic 研究论文：整数分解与离散对数等](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

谷歌在 GitHub 上以“Cogentic”名义发布了一组研究论文，主题包括整数分解、离散对数及相关数学问题。这些问题是许多现代密码学方案的基石，因此引发安全与人工智能领域的高度关注。有社区评论援引可信传闻称，此次发布可能只是更大突破的“冰山一角”，但官方尚未提供技术细节或性能数据。目前公开信息仍非常有限，仅能确认论文集合的存在与主题范围。

hackernews · rgwohlbold · 11月25日 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50642086)

**「背景」** 整数分解和离散对数是密码学中依赖的困难数学问题，其中离散对数可理解为在模运算下由底数和幂求指数（例如模 5 下以 2 为底的结果所示）。Cogentic 并非一套新算法，而更像一个让现有大语言模型协作解决数学猜想的专用框架，包含中心协调器和共享中间证明数据库。

**「影响」** 对依赖整数分解和离散对数难度的密码系统而言，目前没有证据表明存在可立即部署的攻击，因此短期安全影响仍属未知；这些论文更应被视为数学研究方向的新信号。

**「社区讨论」** 评论者观点不一：有人认为这是更大突破的前兆，有人将近期数学发现归因于 AI 对海量搜索空间的探索，也有人对市场低迷与突破并存表示困惑，并重新审视“投入资金能否解决数学难题”的旧观念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer factorization , discrete ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptography`, `#mathematics`, `#Google Research`, `#integer factorization`

---

<a id="item-tech-news-5"></a>
### [Minecraft Java 版 1.20.5 起曝高危 RCE 漏洞](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

11 月 22 日公开的 minecraft2shell 显示，Minecraft Java 版 1.20.5 至 1.21.10 以及 26.1 至 26.4 快照存在高危远程代码执行漏洞，通过服务器资源包中特制 TrueType 字体触发 FreeType 2.14.3 及更早版本的原生越界写，可在 Windows 客户端执行任意代码。1.20.4 及更早版本与基岩版不受影响；Mojang 仍使用 lwjgl-freetype 3.4.3，暂无官方补丁。社区于 11 月 24 日发布 m2sfix 1.0.0，以 Java agent 或 mod 方式关闭字体 hinting 作为临时缓解。投稿人建议在修复前不要添加任何资源包、将多人游戏服务器资源包权限设为“禁用”或安装社区临时修复 mod。

telegram · zaihuapd · 11月25日 12:46

**「背景」** FreeType 是 Minecraft Java 版通过 lwjgl-freetype 使用的字体渲染库，负责解析 TrueType 字体及其 hinting 指令。服务器资源包可向客户端分发自定义字体，因此恶意字体文件能在未修补的解析过程中触发内存越界写入。攻击者只需让玩家连接恶意服务器并接受或启用资源包，就可能获得远程代码执行能力。

**「影响」** 受影响版本的 Windows Minecraft Java 玩家若启用恶意服务器的资源包，可能被远程执行任意代码；在 Mojang 发布官方补丁前，应按建议禁用服务器资源包或安装 m2sfix 1.0.0。

**标签**: `#security`, `#rce`, `#minecraft`, `#freetype`, `#vulnerability`

---

<a id="item-tech-news-6"></a>
### [Ubuntu 安全更新响应迟缓受关注](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

Openwall oss-security 上的一份报告指出 Ubuntu 的安全更新响应出现明显延迟，引发 Hacker News 上关于下游影响和发行版选择的讨论。有系统管理员表示，由于这种延迟，已将服务器镜像从 Ubuntu 全面迁移到 Debian。讨论中引用了稳定内核维护者 2025 年的观点：只挑选应用随机补丁无法修复所有已知和未知问题，可能让系统更不安全，依赖企业发行版提供完整更新是必要前提。也有评论提醒，Debian 等发行版虽然可靠，但回归测试资源有限，曾出现回归问题（Debian bug 1154101）。此外，有用户观察到部分 Ubuntu 安全修复先进入 -updates 仓库而非 security 仓库，因此从只装 security 仓库改为安装全部更新并接受一定风险。

hackernews · gslin · 11月25日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=50647181)

**「背景」** oss-security 是一个公开的开放源代码安全邮件列表，常用于报告和讨论 Linux 发行版的安全更新延迟。Ubuntu 的安全修复通常依赖于将上游内核补丁反向移植到其长期支持内核中，这一过程需要额外的测试和发布周期，可能导致修复时间滞后；近期 Hanno Böck 在该列表上指出 Ubuntu 在修补严重 Linux 内核漏洞（如 CVE-2026-98432 远程 TCP 内存损坏）方面过于缓慢。

**「影响」** 对于依赖 Ubuntu 安全更新的系统管理员，此次报告已促使部分人将生产服务器镜像迁移到 Debian，并调整自动更新策略以覆盖 -updates 仓库、接受可能引入回归的风险。

**「社区讨论」** 评论总体认为 Ubuntu 安全响应延迟不可接受，部分人已转向 Debian；但也有人提醒 Debian 的 QA 资源有限，可能出现回归问题。另有用户困惑于安全修复先出现在 -updates 而非 security 仓库，认为增加了风险。

<details><summary>参考链接</summary>
<ul>
<li>oss-sec: Slow Ubuntu security response times - Seclists.org</li>
<li>Slow Ubuntu security response times | daily.dev</li>
<li>Open Source Security Mailing List - Seclists.org</li>

</ul>
</details>

**标签**: `#Ubuntu`, `#Linux security`, `#open source`, `#vulnerability response`, `#system administration`

---

<a id="item-tech-news-7"></a>
### [评估近期模型在 GDPx 基准上的表现](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases) ⭐️ 7.0/10

文章在 GDPx 基准上评估了近期发布的多个 AI 模型。结果显示，GPT-6.2 Astra 综合表现最佳，但软件工程能力较弱；谷歌的 Gemini 4 Neon 相比前代有明显改进，但仍被认为评价过高；Fable 5.2 能力较强但成本昂贵。评估还涵盖了多款新的中国模型。整体上，这些模型在性能、成本和软件工程能力之间存在明显权衡。

rss · Semianalysis · 11月26日 00:05

**「背景」** GDPx 是 SemiAnalysis 推出的前沿模型能力基准，覆盖芯片设计等 11 个高价值领域的 206 个专家级智能体任务，目前最佳模型得分仅为 12%。Datacurve 协助开发评估与软件工程任务，用于发现模型智能差距。近期被评估的模型包括 GPT-6.2 Astra、Gemini 4 Neon、Fable 5.2 以及中国模型等。

**「影响」** 受影响的软件工程团队在选择这些新模型时需要权衡成本与性能，并应在自身环境中进行基准测试，因为 GPT-6.2 Astra 的软件工程能力不佳、Fable 5.2 昂贵，而成本与产出权衡已成为管理重点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities">GDPx : Measuring Frontier Model Capabilities Across the Most...</a></li>
<li><a href="https://digestai.news/story/semianalysis-releases-gdpx-benchmark-for-frontier-ai-models">SemiAnalysis releases GDPx benchmark for frontier AI models</a></li>
<li><a href="https://www.swarchitect.net/en/semianalysis-gdpx-benchmark-2026-11/">SemiAnalysis GDPx : Opus 5.5 leads agent test at 12% · SW Architect</a></li>
<li><a href="https://www.ibm.com/think/perspectives/where-ai-costs-are-made-saved-in-software-development">Where AI costs are made or saved in software development - IBM</a></li>
<li><a href="https://www.finops.org/wg/optimizing-genai-usage/">Optimizing GenAI Usage: A FinOps Perspective on Cost ...</a></li>
<li><a href="https://www.datadoghq.com/blog/ai-impact/">Measure the real impact of AI coding tools on software ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#model evaluation`, `#benchmarks`, `#software engineering`, `#large language models`

---

<a id="item-tech-news-8"></a>
### [OpenAI 押注网络安全，称市场规模被低估](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 7.0/10

OpenAI 正将网络安全定位为可能超过编程业务的下一个增长引擎。公司 CFO 称外界对网络安全市场规模超 3000 亿美元的估计仍被低估，总裁格雷格·布罗克曼认为网络安全将成为比编程更大的业务板块。OpenAI 已推出面向安全研究的 GPT-6 Cyber，并扩大“网络安全受信访问”计划（Daybreak），截至今年 9 月覆盖数千名经验证的防御者及约 2000 个获批组织和工作空间，支持漏洞发现、代码库分析与二进制逆向。报道同时指出，其与 Anthropic、Google 的竞争以及规模化商业化前景仍不清晰。

telegram · zaihuapd · 11月25日 04:51

**「背景」** OpenAI 的 Daybreak 是其网络安全计划，提供用于漏洞发现、代码库分析和二进制逆向的插件、防御工厂、红队工具及 Codex Security CLI/SDK。GPT-6 Cyber 于 11 月 5 日作为 GPT-6 Astra 的网络安全专用变体发布，用于发现漏洞、重现安全缺陷、开发可用漏洞利用并帮助研究人员测试防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/daybreak/">Daybreak | OpenAI for cybersecurity | OpenAI</a></li>
<li><a href="https://www.youtube.com/watch?v=uz3LF-YBjoE">GPT - 6 Cyber : OpenAI &#x27;s New AI Found 81 Hidden Firefox... - YouTube</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#cybersecurity`, `#AI`, `#GPT-6`, `#software engineering`

---

<a id="item-tech-news-9"></a>
### [腾讯混元开源 224B Hy4 flash GGUF 量化权重](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

腾讯混元通过大模型压缩加速工具箱 AngelSlim 开源了 224B 参数模型 Hy4 flash 的 GGUF 量化权重。原始权重约 410.27GiB，最小 IQ2-AH 版本为 125.73GiB，约为原版的 30%，借助 Strata offload 框架可在 64GB Mac mini 上运行。在 48GB 显存设备上，10K 上下文每秒生成 89 个 token；在 M5 Max 128GB 上，Q3\_K 版本在 32K 上下文下每秒生成 47 个 token。在 DeepSWE v1.1 等评测中，Q3\_K 与原模型的得分差距不超过 0.4 分。

telegram · zaihuapd · 11月25日 09:29

**「背景」** GGUF 是 llama.cpp 生态常用的量化模型格式，可把大模型压缩为适合消费级硬件加载的权重文件。Strata 是一个专门的 MoE 卸载引擎，目前支持少数模型，能把专家参数放在内存或 SSD 上并通过量化降低显存占用；其相关补丁 tandem.cpp 在 16GB 显卡上处理提示的速度比 llama.cpp 快 4–13 倍。腾讯混元此次通过 AngelSlim 工具发布 Hy4 flash 的 GGUF 量化权重，让 224B 参数模型能借助 Strata 在 64GB Mac mini 上运行。

**「影响」** 该发布降低了 224B 级模型本地推理的硬件门槛，使开发者可以在 64GB Mac mini 等消费级设备上运行，而不必依赖高端数据中心硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ewhacc/tandem.cpp">GitHub - ewhacc/tandem.cpp: llama.cpp patch: faster MoE offload for...</a></li>

</ul>
</details>

**标签**: `#large language models`, `#model quantization`, `#GGUF`, `#on-device inference`, `#open-source AI`

---

<a id="item-tech-news-10"></a>
### [亚洲数据中心转售过剩 AI 算力给美国客户](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 7.0/10

彭博社 11 月 25 日报道，在美国收紧一项允许中国科技公司获取英伟达最先进芯片的漏洞后，亚洲多地数据中心正争相把过剩 AI 算力转售给美国买家。Liquid Compute 首席执行官 Ronit Jain 表示，针对先进 AI 加速器出口该地区的新规，正在冲击原本指望把算力租给中国客户的数据中心服务商。报道未披露具体管制细则、受影响芯片型号或算力转售规模，但这一变化显示出政策收紧正促使亚洲 AI 算力供应链从中国客户转向美国市场。

telegram · zaihuapd · 11月25日 11:35

**「背景：算力出口管制漏洞与转售」** 此前美国出口管制禁止中国企业直接购买英伟达最先进 AI 芯片，但东南亚等地企业可合法运营数据中心并向中国客户远程出租算力，相当于绕过限制。美国政府近期收紧了这一漏洞，导致原本依赖中国租用需求的亚洲数据中心出现过剩算力，并开始转向美国买家出售或出租；这解释了 Liquid Compute 等运营商为何表示新规冲击了其把算力租给中国客户的商业模式。

**「影响」** 对原本依赖中国租户的亚洲数据中心运营商而言，新规可能迫使其把过剩算力从中国市场转向美国买家，但报道未提供转售规模或价格影响，具体财务后果仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand">Asia Data Centers Sound Out US Clients to Replace China Demand</a></li>
<li><a href="https://www.nytimes.com/2026/11/16/us/politics/trump-china-ai-chip-loophole.html">Trump Administration Moves to Close A.I. Chip Loophole Ahead of...</a></li>

</ul>
</details>

**标签**: `#AI算力`, `#出口管制`, `#数据中心`, `#英伟达`, `#科技政策`

---

<a id="item-tech-news-11"></a>
### [三星和 SK 海力士据传采用长江存储 Xtacking 堆叠技术](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

三星电子和 SK 海力士据报已通过交叉许可协议，同意在 3D NAND 闪存中采用长江存储的 Xtacking 堆叠技术；但三方均拒绝置评，消息尚未获官方确认。该技术将存储单元与控制电路（CMOS）分别制作在两片晶圆上，再通过键合工艺合二为一，使存储器阵列和逻辑电路可各自独立生产与优化。Omdia 高级分析师称，厂商可自行生产存储阵列，并将逻辑电路交由晶圆代工厂，以使用更先进制程。目前报道仅称“有说法认为”键合技术优势明显，具体协议范围和实施时间未披露。

telegram · zaihuapd · 11月25日 14:33

**「背景：Xtacking 堆叠技术」** 长江存储的 Xtacking 是其 3D NAND 闪存架构，核心是把存储单元阵列和 CMOS 控制电路分别制作在两片晶圆上，再通过键合工艺集成，从而让两部分可以独立优化。该技术在 Flash Memory Summit 上公布后，公开资料显示其可将 NAND I/O 速度提升至 3.0Gbps，接近 DDR4 的水平。

**「影响」** 如果报道属实，三星电子和 SK 海力士采用 Xtacking 后，可分别优化存储阵列和逻辑电路，并有可能将逻辑电路交由晶圆代工厂生产，从而影响 3D NAND 供应链分工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.elecfans.com/article/1010365.html">关于4 D NAND 和 长 江 存 储 Xtacking 的对比分析介绍- 电 子 发烧友网</a></li>
<li><a href="https://www.esmchina.com/news/3936.html">长 江 存 储 首次弯道超车！ 重磅发布 Xtacking 技术，下一代64...</a></li>

</ul>
</details>

**标签**: `#3D NAND`, `#semiconductor manufacturing`, `#YMTC`, `#Samsung`, `#SK Hynix`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国拟对中国、欧盟等 14 个贸易伙伴加征新关税](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 9.0/10

据 CNBC 报道，美国政府拟依据 1974 年《贸易法》第 301 条，对中国、欧盟、日本、印度等 14 个贸易伙伴加征新关税。对华关税将在 2018 年已加征的 25%基础上再加征 20%，若中国违反 2025 年 10 月釜山贸易休战协议，这一附加税率可能升至 40%。

telegram · zaihuapd · 11月25日 13:59

**「背景」** 美国援引 1974 年《贸易法》第 301 条，针对其认定的制造业结构性产能过剩；新关税按国别设定，且除中国外不与现有关税叠加。

**标签**: `#tariffs`, `#trade policy`, `#Section 301`, `#China`, `#global trade`

---

<a id="item-finance-news-2"></a>
### [美商务部被曝威胁英特尔交 10%股权，价值约 110 亿美元且未付对价](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 8.0/10

法庭文件显示，2025 年 8 月美国商务部律师在电话中告诉英特尔首席财务官，不要“误以为这是一场谈判”，并警告拒绝会带来无法预测的后果。几天后，英特尔董事会交出了美方要求的 10%股份；特朗普随后宣布美国政府“完全拥有并控制”该股份，且未支付对价，这批股份当时价值约 110 亿美元。

telegram · zaihuapd · 11月25日 13:25

**「背景」** 这一披露来自英特尔股东 Richard Paisner 对董事会提起的诉讼中解封的法庭文件；该诉讼称，特朗普在讨论约 89 亿美元《芯片法案》拨款时要求英特尔交出 10% 股权，商务部律师随后在电话中表示政府方案不可谈判、拒绝会有未指明后果。

**「影响」** 若法庭文件内容属实，英特尔现有股东的持股比例会被稀释，并可能给其他芯片公司带来被政府以类似施压方式获取股权的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techflowpost.com/en-US/newsletter/146893">Litigation documents reveal the process by which the U.S ...</a></li>
<li><a href="https://www.gate.com/news/detail/intel-lawsuit-reveals-trumps-alleged-10-stake-demand-for-chips-act-funds-25863723">Intel Lawsuit Reveals Trump&#x27;s Alleged 10% Stake Demand for ...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#US government`, `#semiconductors`, `#equity stake`, `#policy`

---