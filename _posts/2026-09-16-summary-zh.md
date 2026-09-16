---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 36 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Google 发布 Gemini 3.8 Live 与扩展思考版](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 渗透代理 25 分钟获取 Baseten 生产 GitHub 管理员权限](#item-tech-news-2) ⭐️ 8.0/10
3. [TabPFN-3.5 发布：新的 SOTA 表格基础模型](#item-tech-news-3) ⭐️ 8.0/10
4. [TypeSafe 发布 System One 模型与 Jev 快速结构化推理](#item-tech-news-4) ⭐️ 7.0/10
5. [Wayback Machine 因爬虫流量启用访问保护](#item-tech-news-5) ⭐️ 7.0/10
6. [SemiAnalysis 称数据中心暂停令未实质拖慢美国建设](#item-tech-news-6) ⭐️ 7.0/10
7. [工信部和发改委印发电子信息制造业“十五五”规划](#item-tech-news-7) ⭐️ 7.0/10
8. [谷歌允许全体工程师使用 Claude Opus 5](#item-tech-news-8) ⭐️ 7.0/10
9. [联发科发布天玑 9600 Pro 2 纳米芯片](#item-tech-news-9) ⭐️ 7.0/10
10. [OpenAI 合同工人工审读 ChatGPT 真实聊天记录](#item-tech-news-10) ⭐️ 7.0/10
11. [GPT-5.5 将于 2026 年 10 月 14 日下线并建议迁移](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [中国 8 月零售销售不及预期，投资下滑加深](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Google 发布 Gemini 3.8 Live 与扩展思考版](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google 宣布推出 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，为 Gemini AI 模型增加实时交互和扩展推理能力。这一新版本面向开发者和 AI 用户，官方博客发布了模型研究更新。社区实测反馈显示实时语音延迟低、能应对较重的口音，并可在 Workspace 账户上使用；有用户称 Gemini Live Mode 的对话体验优于 GPT Voice，更像真人。不过也有评论指出 Gemini 3.8 尚未向 Google AI Plus 用户开放。

hackernews · leumon · 9月15日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49715947)

**「背景」** Google 的 Gemini 系列大语言模型此前已提供实时语音对话的 Live 模式和用于复杂推理的 Extended Thinking 能力。此次发布的 Gemini 3.8 Live 与 Gemini 3.8 Live Extended Thinking 被官方称为“迄今最先进的实时对话模型”，其中 3.8 Live 面向规模化和成本效率，结合对话智能、流畅对话与视觉 grounding；Extended Thinking 版本则用于高复杂度任务，具备更强智能和多步推理。

**「影响」** 开发者可通过 Live API 获得 Gemini 3.8 的实时交互与扩展推理能力，Workspace 账户用户也能使用该版本，但 Google AI Plus 用户目前尚未获得更新。

**「社区讨论」** 社区普遍认可 Gemini 3.8 Live 的低延迟和自然语音体验，有用户用它练习南非荷兰语并称其比 GPT Voice 更自然；同时存在对 Gemini 是否已领先 Fable/Astra 的质疑，以及对 Google AI Plus 未获更新的不满。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live &amp; Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://www.thurrott.com/a-i/google-gemini-a-i/341685/google-announces-gemini-3-8-live-and-3-8-live-extended-thinking">Google Announces Gemini 3 . 8 Live and 3 . 8 Live Extended Thinking</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#large-language-models`, `#google`, `#gemini`, `#live-api`

---

<a id="item-tech-news-2"></a>
### [AI 渗透代理 25 分钟获取 Baseten 生产 GitHub 管理员权限](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

Strix.ai 的 AI 渗透测试代理在 25 分钟内，从 Baseten 公开 Docker 构建历史中发现了一个仍然有效的 GitHub 个人访问令牌（PAT），该令牌属于 basetenbot，并授予对生产仓库的管理员访问权限。该令牌对 Baseten 主产品仓库、驱动其集群的 GitOps 仓库以及 Homebrew tap 拥有管理员和推送权限，并对其他私有仓库（包括特定客户仓库）拥有读写权限。Baseten 于 7 月 14 日下午确认该问题为严重级别，已先将 Harbor 项目设为私有，随后轮换令牌并要求报告方安全删除相关镜像。这一事件凸显了公开构建产物中遗留长期凭据可被自动化代理快速利用，从而扩大软件供应链风险。

hackernews · bearsyankees · 9月15日 18:11 · [社区讨论](https://news.ycombinator.com/item?id=49716476)

**「背景」** Strix 是一个开源的 AI 渗透测试工具，可本地通过 Docker 和用户自己的 LLM 密钥运行。Docker 镜像的构建历史（history\[\].created\_by）中可能残留构建时的命令和凭据；攻击者或自动化代理可以拉取公开镜像层来检查这些元数据。GitHub 个人访问令牌（PAT）是一种可替代密码的凭据，能按配置授予对私有仓库的读写、推送或管理员权限。

**「影响」** 这类自动化发现意味着使用 Docker 构建历史公开镜像的组织必须审计暴露的 CI/CD 凭据，因为长期有效的管理员 PAT 可能在数十分钟内被转化为对生产仓库和客户私有仓库的未授权访问。

**「社区讨论」** 评论区有人认为，这类代理的价值在于比人类更快地完成本可能被忽略的检查，而非发现人类完全无法找到的漏洞，并质疑 Strix 相对 Claude 或 Codex 等代理的独特优势。另有人关注此类主动测试的合法边界，以及事件对 Strix 营销和 Baseten 声誉的不同影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.strix.ai/blog/baseten-harbor-github-pat-takeover">We wanted to use Baseten for inference. We ended up with admin access to their GitHub - Strix</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.</a></li>

</ul>
</details>

**标签**: `#security`, `#AI agents`, `#DevSecOps`, `#software-supply-chain`, `#GitHub`

---

<a id="item-tech-news-3"></a>
### [TabPFN-3.5 发布：新的 SOTA 表格基础模型](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs 发布了 TabPFN-3.5，声称在 TabArena 和 BeyondArena 两个基准上排名第一，并支持最多 100 万行和 2 万特征的 SOTA 性能。该版本提供三种变体：TabPFN-3.5-Fast（alpha，速度比基础模型快 6 倍）、TabPFN-3.5-Thinking（通过 API 用计算换精度）和 TabPFN-3.5-Plus。在 BeyondArena 上，TabPFN-3.5 在文本丰富、高基数和 high-dimensional 数据上领先，比此前最强基线高 250 Elo，比此前整体排行榜第一高 150 Elo；Thinking 变体在 BeyondArena 上比基础模型高 20 Elo，在 TabArena 上高 44 Elo。这些基准声明来自 Reddit 发布帖，尚未经独立验证。

reddit · r/MachineLearning · /u/tuanacelik · 9月15日 16:18

**「背景」** TabPFN 是 Prior Labs 开发的表格基础模型系列，此前的 TabPFN-3 已在 TabArena 基准上取得领先并扩展了模型能力。TabArena 和 BeyondArena 是用于评估表格模型在不同数据规模和特征维度上性能的基准。此次发布的 TabPFN-3.5 在这些基准上排名第一，并更新了 Thinking 模式和 Plus 变体。

**「影响」** 对于处理大型表格数据的机器学习从业者，TabPFN-3.5 提供了一个声称达到 SOTA 且支持大维度数据的候选模型，但应等待独立基准复现后再做生产决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://priorlabs.ai/technical-reports/tabpfn-3">TabPFN-3: Technical Report</a></li>
<li><a href="https://storage.googleapis.com/prior-labs-tabpfn-public/reports/TabPFN_3_model_report.pdf">TabPFN-3: Technical Report - Googleapis.com</a></li>
<li><a href="https://priorlabs.ai/technical-reports/tabpfn-3-5">Prior Labs</a></li>

</ul>
</details>

**标签**: `#tabular data`, `#foundation model`, `#machine learning`, `#SOTA`, `#AutoML`

---

<a id="item-tech-news-4"></a>
### [TypeSafe 发布 System One 模型与 Jev 快速结构化推理](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 7.0/10

TypeSafe.ai 宣布推出 System One Models 与 Jev，一种用于快速类型化/结构化推理的新模型方法。Jev 以任意文本输入（可为复杂 JSON）和一组问题（是/否、多选或评分）作为输入，输出对应答案及概率/置信度，与通用生成式模型不同。官方文档给出的指标包括毫秒级延迟和 0.042 美元/百万 token 的成本。Hacker News 上的讨论认为该模型只能生成结构化输出而非可执行代码，并指出公告中速度对比可能具有误导性，但它对分类和结构化推理任务具有实用价值。

hackernews · albelfio · 9月15日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49717558)

**「背景」** TypeSafe AI 是一个专注于机器原生智能基础设施的 AI 实验室，其 System One 模型旨在为软件提供快速、结构化的决策能力。Jev 是该公司的旗舰模型，也是首个 System One 模型，它放弃通用文本生成，转而输出类型化的结构化结果，目前处于早期访问阶段。

**「影响」** 对于需要高频分类、评分或从复杂 JSON 中提取结构化答案的 AI 工程场景，Jev 提供了一种低延迟、低成本且与通用生成模型互补的选项，但其能力边界限于结构化输出。

**「社区讨论」** HN 评论普遍认可该方法的新颖性和文档质量，但指出公告未充分解释工作原理，且将 Jev 与通用生成模型的速度对比可能不恰当；开发者还提到可与 Python 设计契约模式结合使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://runtimewire.com/article/typesafe-jev-system-one-ai-model-early-access">TypeSafe opens Jev early access for fast, typed AI decisions</a></li>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Structured Output`, `#LLMs`, `#Software Engineering`, `#New Models`

---

<a id="item-tech-news-5"></a>
### [Wayback Machine 因爬虫流量启用访问保护](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 7.0/10

互联网档案馆于 2026 年 9 月 15 日发布更新，说明 Wayback Machine 正遭受高流量自动化爬虫攻击。这些爬虫疑似通过存档副本绕过原网站的反爬限制，给这一非营利基础设施带来额外负载。档案馆已部署防护措施以维持服务运行，但部分用户因此遇到 429 错误或访问不稳定，甚至已有网站选择退出存档。

hackernews · ChrisArchitect · 9月15日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49716176)

**「背景」** 韦伯机器是互联网档案馆运营的非营利网页存档服务，保存了数十亿网页的历史快照。近期，包括《纽约时报》《卫报》和 Reddit 在内的一些主要网站开始阻止韦伯机器存档，部分原因是对 AI 抓取的担忧（tool-1-2）。与此同时，互联网档案馆的存档项目遭遇困难，新闻出版物的页面抓取量在 2025 年 5 月至 10 月间下降了 87%（tool-1-1）。

**「影响」** 受影响用户可能遭遇 429 限流或访问不稳定，且部分网站退出存档将进一步缩小可检索的历史网页范围。

**「社区讨论」** 社区普遍赞赏档案馆在压力下维持开放访问，但也有用户反映特定网络环境持续返回 429 错误，并有人提出 AI 公司应为访问付费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine - Wikipedia</a></li>
<li><a href="https://blog.archive.org/2026/02/18/wayback-machine-director-pushes-back/">Wayback Machine Director Pushes Back on AI Scraping Fears Driving Archive Blocks | Internet Archive Blogs</a></li>

</ul>
</details>

**标签**: `#internet-archive`, `#wayback-machine`, `#web-scraping`, `#infrastructure`, `#open-internet`

---

<a id="item-tech-news-6"></a>
### [SemiAnalysis 称数据中心暂停令未实质拖慢美国建设](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums) ⭐️ 7.0/10

半分析（SemiAnalysis）的 Maya Barkin 撰文反驳“数据中心暂停令正在扼杀美国算力建设”的流行说法，认为暂停令并未实质性拖慢美国数据中心建设。该分析给出具体容量数据：有 20 吉瓦（GW）数据中心项目位于受限的地方行政边界内，但其中实际滑落的仅为 1,525 兆瓦（MW）；全国范围内（包括纽约）受影响容量为 2.3 吉瓦。文章以此说明，尽管大量项目名义上处于暂停令覆盖区域，实际受影响的规模有限，不足以改变美国整体建设速度。

rss · Semianalysis · 9月15日 20:54

**「背景」** 美国部分地方政府对大型数据中心项目设置暂停审批（moratorium），通常出于电网容量、用水和环境担忧。业界普遍将此类禁令视为数据中心建设放缓的主因；本文作者则持不同意见，认为受限地区虽有约 20GW 的规划容量，但真正被推迟的仅 1,525MW，全国含纽约州约 2.3GW。SemiAnalysis 的其他报道也显示，许可延迟会迫使项目改用备用电源或调整选址，但未必等同于整体建设停滞。

**「实际建设影响有限」** 对数据中心开发商和容量规划者而言，暂停令造成的实际施工损失有限：受限边界内虽有 20GW 项目，但真正滑落的仅 1,525MW，全国（含纽约）合计也只有 2.3GW；外部分析同样认为此类措施不会减缓在建项目的全国势头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the">What is So Hard About Behind-The-Meter Power For Datacenters? Part 1</a></li>
<li><a href="https://www.brookings.edu/articles/data-center-moratoriums-are-not-a-substitute-for-oversight/">Data center moratoriums are not a substitute for oversight | Brookings</a></li>

</ul>
</details>

**标签**: `#datacenters`, `#AI infrastructure`, `#energy policy`, `#capacity planning`, `#cloud computing`

---

<a id="item-tech-news-7"></a>
### [工信部和发改委印发电子信息制造业“十五五”规划](https://www.secrss.com/articles/93961) ⭐️ 7.0/10

工信部与国家发展改革委联合印发《电子信息制造业发展“十五五”规划》，部署 17 项重点任务。规划提出到 2030 年规模以上企业营业收入突破 30 万亿元，产业研发投入强度达到 3.5%。在核心技术方面，要求提高先进制程能力，突破高端手机核心芯片和 PC 高性能芯片，并加强开源鸿蒙等国产操作系统搭载。规划还明确推进 RISC-V、人工智能芯片和终端以及北斗等领域发展。

telegram · zaihuapd · 9月15日 03:10

**「背景」** 《电子信息制造业发展“十五五”规划》是中国“十五五”时期（2026—2030 年）国民经济和社会发展规划在电子信息制造领域的专项部署，由工业和信息化部、国家发展改革委联合发布。开源鸿蒙（OpenHarmony）是由开放原子开源基金会管理的国产操作系统根社区，RISC-V 则是开放指令集架构，常被视为替代 ARM/x86 的自主芯片技术路线。

**「影响」** 对先进制程、RISC-V、AI 芯片及开源鸿蒙相关企业和开发者而言，该规划提供了到 2030 年的明确政策方向，可能引导更多资源投向高带宽内存池、全光交换、液冷散热和 CLink 高速互连等配套技术；但规划未披露具体资金或强制性措施，实际推进效果仍取决于后续执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.cn/2026-09-15/detail-inirwfqk4019305.d.html">两部门：推进第五代精简指令集（RISC-V）研发与产业化 支持RISC-V芯片在人工智能、嵌入式系统等领域应用|国家发展改革委|信息化部|工信部|财联社|鸿蒙_手机新浪网</a></li>
<li><a href="http://3g.cnfol.com/sc_stock/gushijujiao/20260915/32370146.shtml">30万亿蓝图出炉！ AI...</a></li>
<li><a href="https://fund.eastmoney.com/a/202609153874514129.html">30万亿蓝图出炉！ AI...</a></li>

</ul>
</details>

**标签**: `#半导体`, `#芯片`, `#开源鸿蒙`, `#RISC-V`, `#产业政策`

---

<a id="item-tech-news-8"></a>
### [谷歌允许全体工程师使用 Claude Opus 5](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 7.0/10

谷歌已向全公司工程师开放 Anthropic 的 Claude Opus 5，用于内部开发。该模型只能在谷歌内部开发平台 Antigravity 上使用；过去谷歌通常禁止大多数员工使用 Claude Code、OpenAI Codex 等外部编程工具，并要求使用自家 Gemini。谷歌发言人表示，Gemini 仍是内部开发的主要模型，Claude 按每位员工配额提供，作为补充。此举被视为对 AI 编码竞争压力的回应。谷歌是 Anthropic 的投资者，今年早些时候宣布计划向该公司投入最多 400 亿美元。

telegram · zaihuapd · 9月15日 05:31

**「背景」** Antigravity 是谷歌内部的开发平台。谷歌此前限制员工使用外部 AI 编程工具，要求使用自家 Gemini；Anthropic 的 Claude 是主流代码生成模型之一，谷歌也是其投资方。

**标签**: `#Google`, `#Anthropic`, `#Claude`, `#AI coding tools`, `#tech industry`

---

<a id="item-tech-news-9"></a>
### [联发科发布天玑 9600 Pro 2 纳米芯片](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 7.0/10

联发科于 9 月 15 日发布旗舰手机芯片天玑 9600 Pro，采用台积电 2 纳米制程，是该公司首款采用该制程的手机处理器。同场发布采用 3 纳米制程的天玑 9600M，两款芯片搭载的首批手机将很快上市。天玑 9600 Pro 配备专用 AI 处理器，在用户提示词处理及启动模型生成前的性能较上一代提升 51%。

telegram · zaihuapd · 9月15日 08:57

**「背景」** 手机芯片的制程节点（如 2 纳米和 3 纳米）指晶体管工艺尺寸，数字越小通常代表更高集成度和能效。专用 AI 处理器可在设备本地加速模型推理，减少部分云端依赖。

**「影响」** 手机厂商可据此推出下一代旗舰机型，天玑 9600 Pro 的专用 AI 处理器使设备端处理用户提示词和模型生成前性能比上一代提升 51%。

**标签**: `#semiconductors`, `#mobile processors`, `#AI hardware`, `#TSMC`, `#MediaTek`

---

<a id="item-tech-news-10"></a>
### [OpenAI 合同工人工审读 ChatGPT 真实聊天记录](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 7.0/10

404 Media 调查披露，OpenAI 通过内部项目“Project Lily”雇用数百名合同工，阅读大量真实 ChatGPT 用户的提示词和完整对话，并为模型回复评分、提出修改意见。这些聊天内容可能包含敏感个人信息，OpenAI 表示会在交给审核员前尽量删除个人信息，但承认敏感细节仍可能被看到。Anthropic 也确认其使用人工审核来改进模型。该报道揭示了大模型训练数据标注和评估中的人工介入及其隐私风险。

telegram · zaihuapd · 9月15日 11:56

**「背景」** 大语言模型通常需要人类反馈强化学习（RLHF）等流程，由人工对模型输出进行评分和排序，以改进回复质量。此类评分常依赖外包合同工审核真实用户数据，因而可能触及用户隐私。404 Media 的报道聚焦 OpenAI 的内部数据标注操作。

**「影响」** 使用 ChatGPT 和 Anthropic 模型的用户应当意识到，其对话内容可能被第三方合同工人工阅读；即使服务商尝试删除个人信息，敏感细节仍可能泄露给审核人员。

**标签**: `#AI`, `#Privacy`, `#ChatGPT`, `#OpenAI`, `#Data Labeling`

---

<a id="item-tech-news-11"></a>
### [GPT-5.5 将于 2026 年 10 月 14 日下线并建议迁移](https://x.com/ChatGPT/status/2099954190600876533) ⭐️ 7.0/10

OpenAI 宣布 GPT-5.5 将于 2026 年 10 月 14 日起在 ChatGPT、ChatGPT Work 和 Codex 的全平台全计划中下线。官方建议仍在 Codex 中使用 GPT-5.5 的用户迁移至 GPT-5.6 Sol 或 GPT-6 Astra。此次下线覆盖三个产品线，意味着依赖 GPT-5.5 的开发者与组织需要在截止日期前完成迁移，否则相关调用可能中断。

telegram · zaihuapd · 9月16日 00:12

**「背景」** 模型下线通常是指服务商停止对特定版本提供 API 或界面访问，以集中资源维护更新版本。OpenAI 过去也会在发布新模型后逐步淘汰旧版本，并给出官方迁移路径。此次 GPT-5.5 的下线同时涉及 ChatGPT、ChatGPT Work 和 Codex，因此影响范围不仅限于聊天界面。

**「影响」** 依赖 GPT-5.5 的 ChatGPT、ChatGPT Work 和 Codex 用户必须在 2026 年 10 月 14 日前迁移到 GPT-5.6 Sol 或 GPT-6 Astra，否则会面临服务不可用的风险。

**标签**: `#OpenAI`, `#GPT-5.5`, `#model deprecation`, `#AI`, `#ChatGPT`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中国 8 月零售销售不及预期，投资下滑加深](https://www.cnbc.com/2026/09/15/china-august-retail-sales-industrial-output-investment-exports-.html) ⭐️ 7.0/10

国家统计局数据显示，8 月社会消费品零售总额同比仅增长 0.4%，低于路透调查预期的 0.8%并较 7 月的 0.6%放缓；1—8 月城镇固定资产投资同比下降 7.2%，降幅较 1—7 月的 6.7%扩大。

rss · CNBC Finance · 9月15日 09:46

**「背景」** 此前二季度 GDP 同比增速放缓至 4.3%，为三年多来最低，决策层一直未推出大规模刺激，而是依靠增量措施支撑增长。

**「影响」** 这加大了北京出台更多财政支持的压力，但分析师认为只要出口增长足够强劲、能使经济落在目标区间内，政府大幅加码刺激的可能性不大。

**标签**: `#China economy`, `#macroeconomic data`, `#retail sales`, `#fixed-asset investment`, `#credit growth`

---