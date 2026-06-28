---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 25 items, 11 important content pieces were selected

---

1. [超 1 万个 GitHub 仓库被发现分发木马恶意软件](#item-1) ⭐️ 9.0/10
2. [MCP 引入零接触 OAuth 企业级认证](#item-2) ⭐️ 8.0/10
3. [Ubiquiti 企业 NAS：ZFS+双 25GbE](#item-3) ⭐️ 8.0/10
4. [医院和大学以极低成本重新利用现有药物](#item-4) ⭐️ 8.0/10
5. [Elkjop 因强制同意被罚 180 万欧元](#item-5) ⭐️ 8.0/10
6. [Noam Shazeer 离开 Google 加入 OpenAI](#item-6) ⭐️ 8.0/10
7. [康奈尔高级编译器课程开放自学](#item-7) ⭐️ 7.0/10
8. [瑞士议会解除新建核电站禁令](#item-8) ⭐️ 7.0/10
9. [不止.gitignore：Git 忽略文件的其他方法](#item-9) ⭐️ 7.0/10
10. [网站可查你是否存在于大模型中](#item-10) ⭐️ 7.0/10
11. [TesterArmy 推出代理化测试平台](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [超 1 万个 GitHub 仓库被发现分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

一名安全研究员通过分析 GHArchive 数据中的推送事件模式，发现超过 1 万个 GitHub 仓库正在分发木马恶意软件。该攻击利用欺骗性提交模式、频繁删除并重新推送提交以及搜索操纵手段，专门针对自动化软件代理。 这一发现揭示了一场大规模利用 GitHub 信任度的恶意软件分发活动，威胁整个软件供应链。使用自动化依赖工具的开发者或组织可能在无意中拉取恶意代码，导致广泛的入侵风险。 攻击者创建新仓库，每隔几小时删除并重新推送提交，使其在搜索结果中显示为“最近更新”。这种模式针对的是自动化代理搜索而非人类用户，旨在通过依赖混淆或直接克隆操作将后门注入下游项目。

hackernews · theorchid · Jun 18, 11:45

**背景**: 软件供应链攻击将恶意代码注入像 GitHub 这样的可信平台，开发者会自动下载依赖。攻击者通过创建模仿合法项目的虚假仓库或劫持标签和提交来利用对开源生态系统的信任。此类攻击已显著增长，例如 SolarWinds 事件以及近期对 Axios、LiteLLM 等工具的破坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/orchidfiles/git-malware-finder/">GitHub - orchidfiles/git- malware -finder: A script that searches GitHub ...</a></li>
<li><a href="https://www.securityweek.com/threat-actors-manipulate-github-search-to-deliver-malware/">Threat Actors Manipulate GitHub Search to Deliver Malware</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/over-3-000-github-accounts-used-by-malware-distribution-service/">Over 3,000 GitHub accounts used by malware distribution service</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了警惕，一位用户（Jimmc414）报告称自己的名字被附加到未知的恶意项目上。其他人分析了攻击者的手法，指出快速删除提交的模式旨在操纵 GitHub 搜索排名并针对自动化代理而非人类用户。讨论突显了 AI 驱动的依赖投毒和供应链攻击威胁日益增长。

**标签**: `#malware`, `#supply chain security`, `#github`, `#cybersecurity`, `#trojan`

---

<a id="item-2"></a>
## [MCP 引入零接触 OAuth 企业级认证](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) ⭐️ 8.0/10

模型上下文协议（MCP）推出了零接触 OAuth，这是一种企业级托管授权机制，允许使用同一 SSO 提供商的应用间安全共享数据，无需逐应用配置 OAuth。 此次更新通过简化认证流程、降低管理开销并提升安全性，使 MCP 在大型组织中具备可行性，为基于 MCP 构建的 AI 工具在企业中的广泛采用铺平了道路。 该机制由一种名为 ID-JAG（Identity-Justified Access Grant，身份证明访问授权）的新型令牌格式驱动，该格式并非 MCP 特有，可在任何使用同一 SSO 提供商的应用间数据共享场景中使用。

hackernews · niyikiza · Jun 18, 21:54

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月宣布的开放标准，用于连接 AI 助手与外部数据源和工具。它提供了读取文件、执行函数和处理提示的标准化接口。零接触 OAuth 作为“企业级托管授权”的一部分，确保 MCP 服务器在首次登录时自动连接，无需为每个应用程序单独设置 OAuth。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/">Enterprise-Managed Authorization: Zero-touch OAuth for MCP | Model Context Protocol Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**社区讨论**: 社区评价总体积极，来自 Okta、Microsoft、Figma 和 Linear 的贡献者表示赞赏，并提供了关于 ID-JAG 令牌格式的技术见解。然而，部分开发者对缺乏长期 cookie 支持表示不满，一位用户称不得不修改规范以实现类似效果。

**标签**: `#MCP`, `#OAuth`, `#authentication`, `#AI tools`, `#enterprise`

---

<a id="item-3"></a>
## [Ubiquiti 企业 NAS：ZFS+双 25GbE](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 8.0/10

Ubiquiti 宣布推出一款基于 ZFS 文件系统的企业级 NAS 设备，配备双 25 Gb SFP28 端口和冗余电源。该产品定价 3999 美元，面向企业高性能存储需求。 这标志着 Ubiquiti 进军企业存储领域，利用了 ZFS 成熟的数据完整性特性和高速网络能力。无月费模式可能颠覆依赖订阅的竞争对手，但社区讨论也指出对 Ubiquiti 软件质量过往记录的担忧。 该 NAS 支持双 25GbE 链路，但社区评论指出使用机械硬盘可能难以完全利用这些带宽。设备配备冗余电源，售价为 3999 美元。

hackernews · ksec · Jun 18, 14:24

**背景**: ZFS 是一种结合文件系统和卷管理的技术，以其通过校验和进行数据完整性验证、快照和高效复制等功能著称。25 Gigabit Ethernet 每链路提供 25 Gbps 带宽，常用于数据中心的高速连接。Ubiquiti 主要以网络设备（如 UniFi）闻名，目前正扩展进入存储领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZFS">ZFS - Wikipedia</a></li>
<li><a href="https://itsfoss.com/what-is-zfs/">What is ZFS ? Why are People Crazy About it?</a></li>
<li><a href="https://www.linkedin.com/pulse/introduction-25g-40g-ethernet-network-fancy-wang">Introduction to 25 G and 40G Ethernet Network</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：一些用户称赞其基于 ZFS 和无月费模式，而另一些则对 Ubiquiti 的软件质量提出严重担忧，提及过去的安全事件和用户界面问题。技术关注点在于机械硬盘能否充分利用 25GbE 链路，质疑实际性能。

**标签**: `#Ubiquiti`, `#NAS`, `#ZFS`, `#enterprise storage`, `#networking`

---

<a id="item-4"></a>
## [医院和大学以极低成本重新利用现有药物](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

医院和大学正在重新利用现有药物治疗新适应症，相比标准疗法成本降低高达 90%。例如，抗癌药 Avastin 被超说明书用于治疗黄斑变性，价格仅为获批药 Lucentis 的三十分之一。 这一趋势可能大幅降低患者和保险公司的医疗成本，特别是对于昂贵的生物药和罕见病。它同时挑战了制药行业的定价模式，并为医学领域的非营利创新指明了方向。 Avastin 和 Lucentis 分子结构相同，但前者每剂约 50 美元，后者需 1500 美元——主要区别仅在于是否经过眼部注射包装。同样，艾司氯胺酮（Spravato）是专利已到期的氯胺酮的衍生物，但疗效更差、价格更贵，凸显了药物研发中的激励扭曲。

hackernews · giuliomagnifico · Jun 18, 10:33

**背景**: 药物重利用是指为已获批的现有药物寻找新的适应症，通常用于与原发病不同的疾病。由于这些药物已通过安全性试验，其应用于新患者群体的成本和时间仅为开发新药的零头。然而，若缺乏监管路径或制药商支持，这类超说明书用药往往无法获得大规模批准和普及。非营利组织和学术医疗中心正在填补这一空白，资助针对罕见病和被忽视疾病的临床试验。

**社区讨论**: 评论者分享了真实案例和担忧：一位有眼科工作经验的用户证实 Avastin 和 Lucentis 分子结构相同，价格仅为后者三十分之一。另一位用户描述其保险为艾司氯胺酮（Spravato）支付高价，而该药是价格更低、专利已过期的氯胺酮的衍生物，疗效却更差。还有用户称赞资助亨廷顿病等罕见病重利用研究的非营利组织 Cures Within Reach，同时有人指出，缺乏明确的监管途径来在未经制药商同意的情况下正式扩展适应症。

**标签**: `#drug repurposing`, `#healthcare costs`, `#pharmaceuticals`, `#off-label use`, `#medical innovation`

---

<a id="item-5"></a>
## [Elkjop 因强制同意被罚 180 万欧元](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

挪威零售商 Elkjop 因要求客户同意接收营销信息作为加入会员俱乐部的条件，违反了 GDPR 关于自由给予同意的规定，被挪威数据保护局处以 180 万欧元罚款。 此案例表明，GDPR 执法可对强制同意行为处以高额罚款，树立了先例，可能阻止欧盟各地类似将同意与服务条款捆绑的做法。 隐私倡导者于 2019 年首次举报该行为，但罚款在五年后才下达；公司自己发出的邮件确认同意是会员条件，成为案件的关键证据。

hackernews · speckx · Jun 18, 18:31

**背景**: 根据 GDPR，同意必须是自由给予、具体、知情且明确的；将服务与同意挂钩被视为非法胁迫。许多公司历史上将营销同意与账户注册捆绑，但监管机构正越来越严格执行这一做法违反数据保护法。

**社区讨论**: 评论者的反应不一：有人赞扬个人的坚持以及行使权利的重要性，也有人觉得他起诉了最终帮他胜诉的法律实体具有讽刺意味。一条评论将这种做法描述为‘法律怪胎在技术细节上得逞’，反映了认为此案仅靠狭窄法律点取胜的观点。

**标签**: `#privacy`, `#GDPR`, `#consent`, `#legal`, `#EU`

---

<a id="item-6"></a>
## [Noam Shazeer 离开 Google 加入 OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 8.0/10

Noam Shazeer，"Attention Is All You Need" 论文的合著者、Google Gemini 项目前联合负责人，宣布离开 Google 加入 OpenAI。路透社于 2026 年 6 月 18 日报道了这一消息。 Shazeer 是最具影响力的 AI 研究者之一，他共同发明了支撑几乎所有现代大型语言模型的 Transformer 架构。他加入 OpenAI 可能显著增强 OpenAI 的研究实力，并进一步加剧主要 AI 实验室之间的人才竞争。 Shazeer 最初于 2021 年离开 Google 共同创立 Character.AI，后于 2024 年通过一项价值约 27 亿美元的许可和人才协议回归，并担任 Gemini 联合负责人。如今仅两年后，他再次离开前往 OpenAI。

hackernews · lukasgross · Jun 18, 00:26

**背景**: Transformer 架构由 Noam Shazeer 等人于 2017 年合著的论文 "Attention Is All You Need" 中提出，彻底改变了自然语言处理，成为 GPT、BERT 和 Gemini 等模型的基础。Shazeer 自 2000 年起就是 Google 的关键研究员，以其工程贡献闻名。他的职业轨迹反映了对顶尖 AI 人才的激烈需求以及领先公司之间的战略流动。

**社区讨论**: 社区评论为 Shazeer 的历史和重要性提供了重要背景。评论者指出，Shazeer 在 2000 年代是 Google 的传奇工程师，他对 Transformer 论文的贡献至关重要。一些人对他在回归后这么快再次离开 Google 表示惊讶，并猜测原因。

**标签**: `#AI`, `#OpenAI`, `#Google`, `#transformers`, `#industry-news`

---

<a id="item-7"></a>
## [康奈尔高级编译器课程开放自学](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

康奈尔大学由 Adrian Sampson 教授的高级编译器课程 CS 6120 现已作为免费自学在线课程开放，所有讲座和资料均可公开获取。 这使得高质量的高级编译器课程对全球学习者免费开放，有助于那些无法接受正规教育的编译器工程师和系统程序员提升技能。 该课程涵盖了 SSA 形式、数据流分析和动态编译等主题，但有评论指出其动态编译器部分过于侧重追踪编译，而后者已被一些人认为是死胡同。

hackernews · ibobev · Jun 18, 11:04

**背景**: 编译器设计是计算机科学的核心主题，通常在本科课程中涵盖基本的优化技术。高级编译器课程深入讲解现代优化过程、中间表示以及运行时编译策略（如即时编译 JIT）。CS 6120 以其使用 LLVM 编译器基础设施的实践方法而闻名。

**社区讨论**: 社区反应总体积极，许多人感谢 Adrian Sampson 提供这一资源。但也存在技术批评：Titzer 认为课程对追踪编译的侧重已过时，j2kun 质疑内容是否称得上“高级”，指出许多主题在初级编译器课程中就已出现。讨论还包括与其他学习资源（如 Nora Sandler 的《编写 C 编译器》）的对比。

**标签**: `#compilers`, `#education`, `#systems`, `#programming languages`, `#online course`

---

<a id="item-8"></a>
## [瑞士议会解除新建核电站禁令](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) ⭐️ 7.0/10

瑞士议会投票决定解除新建核电站的禁令，推翻了福岛核事故后的暂停令，但该决定还需经过全民公投。 这一政策转变可能重塑瑞士的能源战略，使核能有可能在冬季能源安全方面补充可再生能源，并引发了关于核能在实现碳中和方面作用的辩论。 该禁令最初是在 2011 年福岛核事故后实施的；新法律仍需在全民公投中获得批准，左翼和绿党的政治反对声音强烈。

hackernews · leonidasrup · Jun 18, 14:17

**背景**: 瑞士存在季节性能源不平衡问题，春夏季水力发电较多，冬季则较少。核能提供稳定的基荷电力，但安全担忧和高成本限制了其发展。该国也在推进可再生能源的扩张。

**社区讨论**: 评论者意见分歧：一些人认为核能的每太瓦时死亡率最低，并能提供能源安全；而另一些人则认为新核电站相比可再生能源过于昂贵且建设缓慢，建议加入法国核电项目或扩大水力储能。

**标签**: `#nuclear energy`, `#energy policy`, `#Switzerland`, `#technology policy`, `#geopolitics`

---

<a id="item-9"></a>
## [不止.gitignore：Git 忽略文件的其他方法](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/) ⭐️ 7.0/10

本文介绍了两种鲜为人知的 Git 忽略文件方法：通过 core.excludesFile 配置的全局排除文件，以及使用.gitattributes 控制差异对比或归档行为。这些方法使开发者无需修改项目的本地.gitignore 即可忽略文件。 这些替代忽略技巧帮助开发者保持项目.gitignore 文件整洁，并避免在所有仓库中提交 IDE、操作系统或个人配置文件。它们还能精细控制哪些文件出现在差异对比或归档中，减少干扰并提高工作流效率。 全局排除文件可通过`git config --global core.excludesFile ~/.gitignore_global`设置，并将忽略规则应用于本机上的所有仓库。.gitattributes 文件支持`export-ignore`等属性，以从`git archive`中排除文件，还支持`diff=<driver>`属性，将某些文件视为二进制文件以忽略差异。

hackernews · FergusArgyll · Jun 18, 10:29

**背景**: Git 传统上通过每个仓库中的.gitignore 文件来忽略文件，该文件会被提交并与团队共享。然而，某些文件（如.DS_Store 或编辑器配置）是机器特定的，应在全局层面忽略。此外，Git 的.gitattributes 文件允许针对路径设置更多属性，不仅仅是忽略，例如控制 Git 如何处理二进制文件或归档导出。理解这些额外机制有助于开发者更有效地管理其 Git 工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://git-scm.com/docs/gitattributes">Git - gitattributes Documentation</a></li>
<li><a href="https://andreynautilus.github.io/posts/2024-12-24-gitignore-global/">Set global .gitignore file via core . excludesFile</a></li>
<li><a href="https://gist.github.com/subfuzion/db7f57fff2fb6998a16c">Global gitignore. GitHub Gist: instantly share code, notes, and snippets.</a></li>

</ul>
</details>

**社区讨论**: 社区评论赞扬全局排除功能减少了项目.gitignore 文件中的杂乱，有用户指出这解决了贡献者为每个仓库添加 IDE 文件的问题。另一位用户建议使用~/.config/git/ignore 作为全局忽略文件的默认路径，还有一位分享了一个巧妙技巧：在全局忽略中添加一个‘attic’目录，用于存储绝不应提交的临时文件。

**标签**: `#git`, `#version control`, `#.gitignore`, `#developer tools`, `#configuration`

---

<a id="item-10"></a>
## [网站可查你是否存在于大模型中](https://www.intheweights.com/) ⭐️ 7.0/10

名为“Are You in the Weights?”的网站并行查询多个大型语言模型，以判断它们是否基于一个人的在线存在而识别出该人，然后对回答进行聚类并给出一个强度分数。 该工具提高了人们对嵌入在大模型训练集中的个人数据程度的认识，并随着更多流量转向 AI 模型而突显了隐私影响。它还展示了同名消歧的挑战，因为同名者在不同模型中可能被不同地识别。 该工具同时查询前沿模型和小模型，对其输出进行聚类，并提供一个强度分数，表示模型识别该个体的强烈程度。创建者指出这是非确定性的，添加关于你自己的更多关键词会提高分数。

hackernews · turtlesoup · Jun 18, 20:49

**背景**: 大型语言模型是在从互联网抓取的海量数据集上训练的，包括公开资料、论坛帖子和其他在线内容。当一个人有显著的在线存在时，其信息可能成为训练数据的一部分，使模型能够生成“识别”该人的回答。“强度分数”很可能衡量各模型回答之间的一致性，类似于 LLM 评估指标中使用的聚类技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2601.11118">Optimized Algorithms for Text Clustering with LLM-Generated ...</a></li>
<li><a href="https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00648/120476/Large-Language-Models-Enable-Few-Shot-Clustering">Large Language Models Enable Few-Shot Clustering - MIT Press</a></li>
<li><a href="https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation">LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide - Confident AI</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了个人体验：有些人发现自己被识别（如 nickcw 在开源领域），而另一些同名者如 setgree 则因同名消歧而得到混合结果。用户注意到该工具的非确定性，并调侃数字遗产，但也对未经同意就“隐藏在权重中成为不朽”表达了轻微的隐私担忧。

**标签**: `#LLM`, `#privacy`, `#recognition`, `#tool`, `#AI`

---

<a id="item-11"></a>
## [TesterArmy 推出代理化测试平台](https://tester.army/) ⭐️ 6.0/10

TesterArmy，一家 YC P26 创业公司，推出了一个代理化测试平台，允许用户用自然语言定义并执行 Web 和移动应用的端到端测试。该平台使用 AI 代理在部署前及生产环境中持续运行测试。 这解决了在 AI 编码工具加速代码编写的同时，测试仍然缓慢且手动的关键瓶颈。通过自动化测试创建与执行，TesterArmy 可以显著减少测试时间和维护成本，提升工程团队的开发速度。 该平台针对不同任务使用 Google Gemini Flash 和 OpenAI GPT-5.4 等模型，并设有步骤级别的超时和每步视觉调用限制。它集成了 GitHub、Slack 和 Discord 用于警报，并声称在数月内从零增长到 30 多个团队。

hackernews · okwasniewski · Jun 18, 14:49

**背景**: 代理化测试平台使用 AI 代理，可以自主规划、执行和调整测试，无需手动编写脚本。传统的端到端测试需要编写和维护带有 UI 选择器的脆弱代码，耗时且成本高昂。自然语言测试规范允许工程师用纯英语描述测试，AI 代理将其转换为可执行的操作。这种方法旨在降低测试门槛，减少测试基础设施的开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vtestcorp.com/insights/agentic-testing-the-complete-guide-to-ai-powered-software-testing-in-2026/">Agentic Testing: Complete Guide to AI-Powered QA | VTEST</a></li>
<li><a href="https://dev.to/devdev2413/i-got-tired-of-writing-e2e-tests-so-i-built-an-ai-that-runs-them-for-me-4p32">I got tired of writing E2E tests , so I built an AI that... - DEV Community</a></li>
<li><a href="https://testrigor.com/ai-agents-in-software-testing/">AI Agents in Software Testing - testRigor AI-Based Automated Testing Tool</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出谨慎的兴趣。一些人质疑 TesterArmy 如何确保结果确定性，以及其 token 成本与使用 LLM 生成传统脚本相比如何。另一些人则对在关键测试基础设施上依赖第三方 SaaS 表示担忧。公开的技术细节揭示了具体的模型选择和超时设置，引发了关于局限性和模型新鲜度的进一步提问。

**标签**: `#testing`, `#AI agents`, `#web development`, `#mobile development`, `#startup`

---