---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 23 items, 7 important content pieces were selected

---

1. [软件的 Emacs 化：LLM 时代的个人软件浪潮](#item-1) ⭐️ 8.0/10
2. [普林斯顿大学终止 133 年无人监考考试传统](#item-2) ⭐️ 8.0/10
3. [孪生兄弟被解雇后删除 96 个政府数据库](#item-3) ⭐️ 8.0/10
4. [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](#item-4) ⭐️ 8.0/10
5. [2025 年免费.city.state.us 地方域名指南](#item-5) ⭐️ 7.0/10
6. [Linus Torvalds 在 GuitarPedal 仓库中创建分支](#item-6) ⭐️ 6.0/10
7. [取消订阅后无法访问 Claude Design 项目](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [软件的 Emacs 化：LLM 时代的个人软件浪潮](https://sockpuppet.org/blog/2026/05/12/emacsification/) ⭐️ 8.0/10

本文认为，大型语言模型（LLM）使得构建个人软件比采用现有的预制工具更加容易，导致作者所称的“Emacsification”现象——未来每个人都将拥有自己定制的软件茧。 这一转变可能从根本上改变软件的生产和消费方式，从一刀切的应用程序转向高度个人化的用户自建工具，对软件行业和终端用户赋能具有重大意义。 值得注意的是，安全研究员 tptacek 列出了几类软件——包括播客应用、音乐播放器和笔记工具——其中 LLM 生成的替代品如今已能达到个人使用“足够好”的质量。Hacker News 版主 dang 补充说，软件生产现在如此容易，以至于一切都变成了“.emacs 文件”，即每个人都拥有自己无限可定制的软件茧。

hackernews · rdslw · May 13, 07:06

**背景**: Emacs 是一个高度可扩展和可定制的文本编辑器，常被描述为“编辑器中的操作系统”，因为用户可以使用其内置语言 Emacs Lisp 修改几乎所有的行为。术语“Emacsification”借此类比：正如 Emacs 用户将编辑器定制成独特的个人环境，如今的开发者和高级用户也开始借助 LLM 为自己打造定制软件，而不是满足于现成的应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.w3tutorials.net/blog/differences-between-emacs-and-vim/">Emacs vs Vim: Practical Differences, Key Features... — w3tutorials.net</a></li>
<li><a href="https://operavps.com/blog/emacs-vs-vim/">Emacs vs Vim Comparison Guide for Power Users</a></li>

</ul>
</details>

**社区讨论**: 在讨论中，tptacek 列举了 LLM 现在可以以可用质量生成的软件类别（例如播客应用、feed 阅读器、聊天客户端），主张“技术极客应该重新占领这些领域”。dang 强烈赞同，指出软件生产已变得足够简单以创建个人“茧”。shaokind 分享了自己用 LLM 构建此类工具的个人经验，但警告说 Emacs 本身在跨平台时可能脆弱。SoftTalker 将这一趋势与 20 世纪 60 年代个人计算的原始愿景联系起来，即每个人都编写自己的程序。

**标签**: `#software development`, `#LLMs`, `#personal software`, `#Emacs`, `#AI-assisted programming`

---

<a id="item-2"></a>
## [普林斯顿大学终止 133 年无人监考考试传统](https://www.dailyprincetonian.com/article/2026/05/princeton-news-adpol-proctoring-in-person-examinations-passed-faculty-133-years-precedent) ⭐️ 8.0/10

普林斯顿大学投票决定，所有线下考试必须设置监考人员，推翻了该校实行 133 年、允许无人监考考试的信誉守则政策。 这所顶尖学府的政策转变，标志着 AI 工具已广泛侵蚀学术诚信信任，迫使即使是最传统的信誉制度也不得不做出调整。 这一变化终结了完全依赖学生信誉和同学举报的政策；新制度下，教师或监考人员将监督考试。此举源于学生对在多模态 AI 模型（如 Gemini）帮助下作弊的担忧。

hackernews · bookofjoe · May 13, 20:12

**背景**: 普林斯顿大学历史上实行信誉守则，本科生考试无需监考，相信学生不会作弊也不会容忍作弊。该守则由学生委员会负责处理违规行为。随着免费且强大的 AI 工具能够实时回答考试题目，教师认为这一信誉体系已无法维持。

**社区讨论**: 评论者表达了多种观点：有人怀念旧日基于信任的制度，也有人认为社会信任度下降（而非仅仅是 AI）才是原因。一名学生分享了同学用 AI 拍摄并解答考试题目的亲身经历，而来自另一所大学的评论者则对普林斯顿竟曾允许无人监考考试感到惊讶。

**标签**: `#academic integrity`, `#AI`, `#proctoring`, `#education policy`, `#trust`

---

<a id="item-3"></a>
## [孪生兄弟被解雇后删除 96 个政府数据库](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/) ⭐️ 8.0/10

两名孪生兄弟在受雇于 Opexus 公司担任 IT 合同工时，被解雇后利用其仍然有效的数据库访问权限，对 96 个政府数据库执行了“DROP DATABASE”命令，其中包括一个属于国土安全部的数据库。 这一事件凸显了在解雇时立即撤销访问权限的极端重要性，因为未能及时撤销权限导致了一次严重的内部威胁攻击，危及了敏感的政府数据和系统。 根据社区讨论，兄弟之一的 Sohaib 在执行搜查令时被发现持有七支枪支和 370 发.30 口径弹药，尽管其前科记录应禁止其持有枪支。攻击者使用了 SQL 命令“DROP DATABASE dhsproddb”，并随后搜索如何清除系统日志。

hackernews · jnord · May 12, 22:28

**背景**: 内部威胁指现任或前雇员滥用其授权访问权限对组织造成损害的情况。在此案例中，这对孪生兄弟是拥有数据库管理权限的 IT 合同工。“DROP DATABASE”命令会永久删除整个数据库，包括所有表和数据。该事件暴露了解雇程序中的失败——即在解雇之前或之后未能立即撤销访问权限，并且背景调查可能不够彻底，因为其中一名兄弟有犯罪记录。

**社区讨论**: 社区评论者对这些攻击者明目张胆的行为感到好笑且难以置信，例如在删除数据库后立即询问 AI 如何清除日志。一些人批评了招聘流程，并质疑非美国公民如何能够接触敏感的国土安全部系统。另一条评论指出，兄弟俩在实施数据库攻击的同时还犯下了其他罪行（非法持有枪支），颇具讽刺意味。

**标签**: `#insider-threat`, `#cybersecurity`, `#database-security`, `#it-security`, `#incident-response`

---

<a id="item-4"></a>
## [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus 开源了 Needle，这是一个从 Gemini 蒸馏出的 2600 万参数函数调用模型，在消费级设备上可实现每秒 6000 个 token 的预填充和每秒 1200 个 token 的解码。 该模型表明，对于工具调用这种检索和组装任务，大型模型是大材小用；一个微小高效的模型即可在手机、手表和眼镜等边缘设备上运行，使端侧智能体 AI 变得切实可行。 Needle 采用仅包含注意力和门控机制的简单注意力网络架构，完全去除了 MLP 层；该模型先在 200B token 上预训练，然后在来自 15 个工具类别的 20 亿 token 合成函数调用数据上进行后训练。

hackernews · HenryNdubuaku · May 12, 18:03

**背景**: 工具调用（函数调用）使大语言模型能够通过将自然语言转换为结构化的 API 调用来与外部 API 和数据源交互。模型蒸馏将知识从大型教师模型（如 Gemini）转移到更小的学生模型，从而在资源受限设备上实现高效推理。大多数基于 Transformer 的大模型包含前馈层（MLP）用于记忆知识，但 Cactus 发现，对于依赖外部上下文的任务（工具使用、RAG），由于所需事实已在输入中提供，因此 MLP 并非必要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.promptingguide.ai/applications/function_calling">Function Calling with LLMs | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，但也提出了若干问题。有人质疑 Needle 能否处理超出简单示例（如天气查询）的复杂多工具场景，而另一些人则看到了将其用于命令行自然语言交互的潜力。一个值得关注的问题是 Google 针对蒸馏的主动防御机制，如果被检测到，可能会降低模型性能。有评论者证实，从 Qwen 中移除 MLP 后，模型仍能处理转换任务但丧失了知识，这与 Needle 的设计思路一致。

**标签**: `#tool calling`, `#model distillation`, `#edge AI`, `#small language models`, `#attention networks`

---

<a id="item-5"></a>
## [2025 年免费.city.state.us 地方域名指南](https://fredchan.org/blog/locality-domains-guide/) ⭐️ 7.0/10

2025 年 5 月发布的一份全面指南解释了如何通过使用临时.us 域名模板和委托的地方管理者，在.us 顶级域名下注册免费的.locality.state.us 格式域名（例如 yourname.city.state.us）。 这份指南让想免费获得简短且具有地理意义的域名的人能接触到这一小众但宝贵的资源，同时也揭示了公证函和已停止运营的注册商等实际障碍。 注册者必须找到已委托的地方，填写官方的临时.us 域名模板，并发送给该地方的管理者；部分管理者要求提供当地政府出具的公证函，而如果地方运营者已停止运营，注册可能无法完成。

hackernews · speckx · May 13, 14:45

**背景**: .us 顶级域名包含一个层级命名空间：state.us（如 ma.us）、locality.state.us（如 boston.ma.us）以及 organization.locality.state.us。地方域名被委托给当地实体（城市、县或经批准的 ISP），这些实体可将名称再委托给居民或企业。虽然原则上免费，但流程因各地方自行制定规则而差异很大，可能收取费用或要求提供文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fredchan.org/blog/locality-domains-guide/">Setting up a free *.city.state.us locality domain | Frederick's Perch</a></li>
<li><a href="https://en.wikipedia.org/wiki/.us">.us - Wikipedia</a></li>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/254/36/us-domain-registration-requirements/">.US domain registration requirements - Domains - Namecheap.com</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实际困难：一位用户花了 18 个月寻找已停止运营的注册商的遗孀，另一位发现波士顿市政府无法提供公证人出具所需信函。有几人指出.us 域名禁止 WHOIS 隐私保护，这对个人使用来说是一个隐私问题。

**标签**: `#domain registration`, `#.us TLD`, `#locality domains`, `#DNS`, `#practical guide`

---

<a id="item-6"></a>
## [Linus Torvalds 在 GuitarPedal 仓库中创建分支](https://github.com/torvalds/GuitarPedal) ⭐️ 6.0/10

Linus Torvalds 在 GitHub 上他的个人仓库 GuitarPedal 中创建了一个新分支，表明他正在积极学习模拟电路设计。 虽然这只是一个小众的个人项目，但它凸显了 Linus Torvalds 在软件之外的兴趣，这可能会激励开源社区探索硬件和模拟电子领域。 该仓库名为 GuitarPedal，创建分支表明他正在试验电路修改或进行学习练习。

github · torvalds · May 13, 22:43

**背景**: Linus Torvalds 是 Linux 内核和 Git 的创建者。模拟电路是处理连续信号的电子电路，常用于吉他效果器之类的音频设备来修改声音。这个项目表明 Torvalds 正在探索他通常软件专长之外的领域。

**标签**: `#linus-torvalds`, `#open-source`, `#hardware`, `#analog-circuits`, `#personal-project`

---

<a id="item-7"></a>
## [取消订阅后无法访问 Claude Design 项目](https://news.ycombinator.com/item?id=48128003) ⭐️ 6.0/10

一位用户报告称，在取消 Claude Code Max 订阅后，他们无法访问之前所有的 Claude Design 项目和积分，而其他 LLM 应用通常保留历史会话。 此事件凸显了基于订阅的 AI 工具中数据可移植性和所有权的重要问题，用户降级或取消时可能丢失工作成果。这可能会影响对 Anthropic 产品生态的信任，并促使用户更频繁备份 AI 生成的内容。 用户还丢失了有时效限制的促销积分，重新订阅后也未恢复。有社区成员指出，可以通过数据导出功能将 Claude Design 聊天记录导出为 JSON 文件，这是一种变通方法。

hackernews · pycassa · May 13, 21:40

**背景**: Claude Design 是 Anthropic 推出的一款研究预览工具，支持通过语音、视频、着色器及 AI 创建代码驱动的原型。该工具面向 Pro、Max、Team 和 Enterprise 计划订阅者。Claude Code Max 是更高等级的订阅，包含用于终端编码工作流的 Claude Code。如果系统未能妥善处理计费问题或订阅变更，用户可能会失去对某些功能的访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-design-anthropic-labs">Introducing Claude Design by Anthropic Labs</a></li>
<li><a href="https://support.claude.com/en/articles/11049741-what-is-the-max-plan">What is the Max plan? | Claude Help Center</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出不同体验：部分用户建议通过数据导出恢复项目，另一些用户批评 Anthropic 优先添加花哨功能而非修复漏洞。一位用户对 Claude Design 与 Claude Code 的整合表示正面评价。整体态度谨慎，建议定期备份数据。

**标签**: `#data access`, `#subscription trap`, `#AI design tools`, `#user experience`, `#data portability`

---