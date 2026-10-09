---
layout: default
title: "Horizon Summary: 2026-10-09 (ZH)"
date: 2026-10-09
lang: zh
---

> 从 41 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Anthropic 推出开源漏洞扫描服务 OSS Scanner](#item-tech-news-1) ⭐️ 8.0/10
2. [Yes, and：以“是的，而且”态度看待 AI 编程](#item-tech-news-2) ⭐️ 7.0/10
3. [北京不会为前沿限速：中国速度优先的 AI 安全体制](#item-tech-news-3) ⭐️ 7.0/10
4. [ThinkingBox：507 个有状态工作流的重复可靠性与终端状态评估](#item-tech-news-4) ⭐️ 7.0/10
5. [不明攻击者利用 ARTEX 与中转站攻击韩国金融机构](#item-tech-news-5) ⭐️ 7.0/10
6. [OpenAI 封禁俄伊两起 AI 影响行动](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI API 新增 GPT-6.1 Sol Ultrafast 模式](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [美股盘前异动：Wolfspeed、博通、台积电等公司股价波动](#item-finance-news-1) ⭐️ 7.0/10
2. [标普预测中国住宅价格或于 2028 年三季度触底](#item-finance-news-2) ⭐️ 7.0/10
3. [OpenAI 年化收入比此前报道少 200 亿美元](#item-finance-news-3) ⭐️ 7.0/10
4. [美政府暂停微软绿卡申请资格并指控欺诈](#item-finance-news-4) ⭐️ 7.0/10
5. [SpaceX 宣布拟收购全美低频段频谱许可证](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 推出开源漏洞扫描服务 OSS Scanner](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source) ⭐️ 8.0/10

Anthropic 推出 OSS Scanner，为符合条件的开源项目提供免费、自愿接入的 AI 生成漏洞扫描服务。报告由 Claude 等模型生成，未经人工审核，包含漏洞复现、漏洞说明，并在可能时提供补丁建议，可能存在错误。Anthropic 称过去半年发现逾 2.9 万个候选漏洞，人工审查约 6000 个；早期测试的 97 个高危或严重漏洞中，85 个符合其披露流程要求。符合条件的开源项目核心维护者可提交 GitHub PR 申请接入。

telegram · zaihuapd · 10月9日 02:00

**「背景」** 开源项目通常依赖维护者有限的安全审计资源，AI 模型可自动分析代码并生成候选漏洞报告，但结果需要人工确认以避免误报。Anthropic 的 OSS Scanner 将这种能力以自愿接入的方式提供给符合条件的项目。

**「影响」** 符合条件的开源项目核心维护者可通过 GitHub PR 申请接入，获得免费 AI 生成的漏洞报告，但报告未经人工审核，需自行验证以减少误报。

**标签**: `#AI`, `#security`, `#open source`, `#vulnerability scanning`, `#Anthropic`

---

<a id="item-tech-news-2"></a>
### [Yes, and：以“是的，而且”态度看待 AI 编程](https://htmx.org/essays/yes-and/) ⭐️ 7.0/10

htmx.org 于 2026 年 2 月发布了一篇题为《Yes, and》的文章，主张对 AI 在编程中的角色采取“yes, and”态度，目标读者是考虑计算机科学专业的学生和开发者。文章的核心观点是：AI 工具应被用来增强已有技能，而不是替代对编程基础的掌握；有效的 AI 辅助编程（即“vibe coding”）仍要求使用者具备扎实的工程功底。这一观点回应了 AI 快速发展对软件工程职业前景的担忧，强调学习和适应 AI 与打好基础可以并行不悖。

hackernews · Michelangelo11 · 10月8日 09:48 · [社区讨论](https://news.ycombinator.com/item?id=50003796)

**「背景」** htmx 是一个轻量级 JavaScript 库（约 14kB gzip 后），允许开发者直接在 HTML 属性中使用 AJAX、WebSocket 和服务器发送事件，从而以超文本的简洁性构建现代界面。该文的作者是 htmx 的创建者、蒙大拿州立大学计算机科学教授 Carson Gross；他在文中回应“在 AI 进步下是否还应学习编程”，并给出“yes, and”的立场，即编程仍然重要且应与 AI 结合。

**「社区讨论」** 作者在评论中重申文章是为刚上大学的儿子而写，并观察到最有效的 vibe coder 已是优秀开发者。其他评论者中，有人认为正确使用 AI 后其编程能力可超过自己，也有人反对将“编程到提示”类比为“汇编到高级语言”，强调编译器具有确定性而 AI 不具备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://daily.dev/posts/htmx-yes-and--o6bbh9zst">htmx ~ Yes , and ... | daily.dev</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#career advice`, `#vibe coding`, `#programming`

---

<a id="item-tech-news-3"></a>
### [北京不会为前沿限速：中国速度优先的 AI 安全体制](https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier) ⭐️ 7.0/10

SemiAnalysis 通讯作者 Mark Chen 的分析认为，北京不会以放缓前沿 AI 发展为代价换取安全，而是在推行一种“速度优先”的 AI 安全体制。文章探讨该路线对前沿 AI 开发的影响，并涉及 AI 安全、中国科技政策、AI 监管和地缘政治等议题。需要说明的是，所提供源内容仅为预告“AI safety is on fire”，未包含具体政策细节、时间或数据，因此上述概括基于文章标题与元数据摘要。

rss · Semianalysis · 10月8日 17:46

**「背景：中国 AI 安全监管的双轨特征」** 背景：中国的 AI 安全监管呈现出“公众服务端严格、前沿开发端宽松”的双轨特征。SemiAnalysis 分析指出，中国对面向公众的生成内容与流程设置了全球最严格的限制，但对前沿模型开发本身没有施加任何义务；相比之下，欧盟对超过 10²⁵ FLOP 的系统引入系统性风险义务，加州 SB 53 则对超过 10²⁶次运算的模型要求前沿框架与 15 天事件报告。中国官方文件虽使用了递归自我改进、模型欺骗评估者、模型关闭脚本等前沿风险术语，实践中却没有将这些要求延伸到模型开发阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier">Beijing Will Not Pace the Frontier: China’s Speed-First AI ...</a></li>
<li><a href="https://unityriskresearch.com/semianalysis/beijing-will-not-pace-the-frontier-china-s-speed-first-ai-sa">Beijing Will Not Pace the Frontier: China’s Speed-First AI ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#China tech policy`, `#AI regulation`, `#geopolitics`, `#AI governance`

---

<a id="item-tech-news-4"></a>
### [ThinkingBox：507 个有状态工作流的重复可靠性与终端状态评估](https://www.reddit.com/r/MachineLearning/comments/1x17shf/thinkingbox_solving_an_agent_task_once_vs_solving/) ⭐️ 7.0/10

微软发布的 ThinkingBox 基准包含 507 个策略条件业务工作流，覆盖零售、旅游/酒店、汽车保险、新银行内部 IT、咨询 IT/HR 五个领域。每个任务在相同干净后端上独立执行 20 次，每个模型共 10,140 次试验；模拟用户仅在询问时透露私有上下文，评分依据终端后端状态和副作用与要求终态是否一致，其中 477 个任务仅按状态评分，30 个还检查最终回复的窄属性。该基准用 pass@1、pass@20 和 all-20 区分发现能力与可重复性：Kimi-K3 至少成功一次比例最高为 93.89%（476/507），但 20 次全对仅 13.41%（68/507）；Claude Opus 5 至少一次为 79.09%，全对为 47.53%（241 个任务）；Qwen3.8-27B 对应为 89.35% 和 7.50%。在 12 个模型共 121,680 次有效试验中，79,853 次未通过可执行检查，其中 67.24% 干净终止、调用过状态修改工具且无最终工具错误，而这些干净失败中错误字段值占 77.61%、多余效应占 43.30%、缺失必需效应占 25.36%（类别有重叠）。作者说明这些任务是合成重构而非生产流量，20/20 是固定预算下的观测计数而非未来可靠性保证，模拟用户是固定 LLM 可能引入方差，失败类别是确定性诊断标签而非因果解释；代码、数据集和 Hugging Face OpenEnv 环境已公开，可直接运行 507 个任务复现。

reddit · r/MachineLearning · /u/tuhin\_k · 10月9日 00:50

**「背景」** ThinkingBox 由微软提出，包含可复用的沙箱和基准，用于可验证的工具-智能体-用户交互，并附带 Thinkingbox-bench，涵盖 507 个有状态业务工作流。与仅将“代理正常结束对话”视为完成的常见评估不同，该基准检查任务终止时后端数据库的实际状态和副作用，以判断代理是否真正完成了任务。它还对每个任务在同一干净后端上执行 20 次独立尝试，从而区分单次成功与重复可靠性。

**「影响」** 对评估智能体可靠性的团队而言，该基准的量化结果显示仅看单次成功或“完成”信号会显著高估能力，应改为重复试验并直接校验终端数据库状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.19741">[2608.19741] One Success Isn&#x27;t Reliability: Thinkingbox, a ...</a></li>
<li><a href="https://arxiv.org/html/2608.19741v1">One Success Isn’t Reliability: Thinkingbox, a Sandbox and ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark`, `#stateful workflows`, `#evaluation`, `#machine learning`

---

<a id="item-tech-news-5"></a>
### [不明攻击者利用 ARTEX 与中转站攻击韩国金融机构](http://xcai.pro/) ⭐️ 7.0/10

网络安全公司 CrowdStrike 于 10 月 7 日披露，一名身份不明的攻击者在 9 月底至 10 月初针对韩国金融机构实施攻击并窃取数据。攻击者使用了中国开发的开源智能体渗透工具 ARTEX，并在其控制的开放目录中留下 Claude Code 会话记录和 ARTEX 配置。会话显示攻击者疑似通过中转站 xcai.pro 调用 DeepSeek v4.1-flash，并以智谱 GLM-5.3 和 Grok 4.6 作为辅助模型。CrowdStrike 以中等置信度判断对方为中文使用者、动机偏财务，但未归因到已知组织；一次会话还要求生成包含 26 岁、华南理工大学背景及广东茂名信息的安全研究员简历，公司认为这些细节很可能属于攻击者本人。目前身份与泄露规模均未证实，该中转站也已关闭。

telegram · zaihuapd · 10月8日 10:32

**「背景」** ARTEX 是一款由中国开发的开源智能体渗透测试工具，可与大语言模型（如 Anthropic 的 Claude Code）配合，自动执行侦察或攻击任务。报道中提到的“中转站”指集中转发多种大模型 API 的服务，攻击者疑似借此调用 DeepSeek v4.1-flash、智谱 GLM-5.3 和 Grok 4.6 等模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shattered.io/crowdstrike-artex-ai-agent-korea-bank-hack-2026/">CrowdStrike Ties ARTEX AI Agent to Korea Bank Hack</a></li>
<li><a href="https://dev.to/anoymask/artex-llm-integrated-penetration-testing-tool-used-to-target-south-korean-financial-institutions-52n6">ARTEX : LLM-Integrated Penetration Testing Tool... - DEV Community</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI-assisted attacks`, `#open-source tools`, `#LLM misuse`, `#threat intelligence`

---

<a id="item-tech-news-6"></a>
### [OpenAI 封禁俄伊两起 AI 影响行动](https://openai.com/index/disrupting-ai-enabled-false-front-operations/) ⭐️ 7.0/10

OpenAI 封禁了两个利用 ChatGPT 的隐蔽影响行动。俄罗斯行动疑似通过冒用身份控制拉美一个“研究平台”，传播损害乌克兰声誉及影响当地政治的虚假内容；伊朗行动则以 7 个“记者”人设向全球中小网络媒体投稿，并批量生成社交媒体评论。OpenAI 将俄罗斯行动评为影响行动突破量表第 5 类，这是其开始报告以来首次；伊朗行动为第 4 类，产出近 100 篇署名文章。两起行动均结合传统手段与 AI，部分内容进入主流媒体。

telegram · zaihuapd · 10月8日 15:52

**「背景」** OpenAI 将此类伪装成独立媒体或智库、隐藏幕后操纵者的行动称为“虚假前台行动”（false-front operations）。其内部影响行动突破量表用于评估行动者是否越过从文本生成到完整瞒骗链条的阈值；该公司 2026 年 10 月 8 日发布的报告首次将俄罗斯行动评为第 5 类，伊朗“冒名记者”行动被评为第 4 类。

**「影响」** 这显示生成式 AI 已实际被用于跨境舆论操控并渗透主流媒体，要求平台和媒体强化对 AI 生成内容与虚假记者身份的审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/disrupting-ai-enabled-false-front-operations/">Disrupting AI - enabled “ false front ” operations | OpenAI</a></li>
<li><a href="https://cellcog.ai/blog/openai-false-front-operations/">OpenAI &#x27;s False - Front Report : Its First Category 5 Takedown | CellCog</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#misinformation`, `#OpenAI`, `#cybersecurity`, `#influence operations`

---

<a id="item-tech-news-7"></a>
### [OpenAI API 新增 GPT-6.1 Sol Ultrafast 模式](https://developers.openai.com/api/docs/changelog) ⭐️ 7.0/10

OpenAI API 在 Responses API（v1/responses）中新增了 GPT-6.1 Sol 的 Ultrafast 模式，该模式被描述为该接口最快的服务层级。据开发者 Tibo 连续 28 天更新的第 4 天内容，Ultrafast 相比 Standard 最高可达到约 8 倍生成速度。所有 API 用户均可使用，价格为 Standard 的 6 倍：短上下文下每百万 token 输入约 12 美元、缓存输入约 0.60 美元、输出约 60 美元。该消息来自 Telegram 帖子，尚未提供 OpenAI 官方文档的直接确认。

telegram · zaihuapd · 10月9日 00:00

**「背景」** Ultrafast 模式是 OpenAI API 中速度最快的服务层级，此前已用于 GPT-6 Astra 等模型，此次扩展到 GPT-6.1 Sol。该模式面向需要极低延迟的场景，如频繁工具调用的智能体应用，官方建议使用 WebSockets 以避免网络开销抵消速度优势。其高价定位基于“用成本换延迟”的设计，适合调试故障、实时体验等对响应速度敏感的任务。

**「影响」** 该模式若推出，开发者可在 Responses API 中为 GPT-6.1 Sol 选择 Ultrafast 服务层级，以 Standard 6 倍价格换取最高约 8 倍生成速度，适用于延迟敏感任务。但外部报道对具体模型（GPT-6 Astra 或 Sol）和价格（$60/$300 或 $12/$60）说法不一，接入前需核对官方文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/ultrafast-mode">Ultrafast mode | OpenAI API</a></li>
<li><a href="https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475">Ultrafast is rolling out today for GPT-6.1 Sol in the API ...</a></li>
<li><a href="https://apidog.com/blog/openai-ultrafast-mode/">OpenAI Ultrafast : 6x the Speed at 6x the Price. When It Pays for Itself.</a></li>
<li><a href="https://www.latent.space/p/ainews-openai-devday-2026-dots-61">[AINews] OpenAI DevDay 2026: Dots, 6 . 1 Sol , Ultrafast , Decisions...</a></li>

</ul>
</details>

**标签**: `#OpenAI API`, `#GPT-6.1`, `#Ultrafast mode`, `#LLM`, `#AI`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美股盘前异动：Wolfspeed、博通、台积电等公司股价波动](https://www.cnbc.com/2026/10/08/stocks-making-the-biggest-moves-premarket-hae-avgo-lulu-wolf.html) ⭐️ 7.0/10

美股盘前多只个股因公司消息波动：Wolfspeed 在获得美国国防部 15 亿美元有条件贷款后上涨逾 15%；博通据报正为与 OpenAI 合作的定制 AI 芯片安排逾 500 亿美元融资；台积电第三季度营收 160.3 亿美元，高于市场预期。

rss · CNBC Finance · 10月8日 12:28

**「背景」** 这些变动来自 CNBC 盘前汇总，其中 Wolfspeed 的贷款是 30 年期融资承诺，美国国防部在拟议条款下可获得最高 7.5%的认股权证，用于支持美国本土芯片生产。

**标签**: `#stocks`, `#premarket`, `#semiconductors`, `#AI`, `#earnings`

---

<a id="item-finance-news-2"></a>
### [标普预测中国住宅价格或于 2028 年三季度触底](https://www.cnbc.com/2026/10/08/chinas-real-estate-market-may-be-set-for-a-turnaround-sp-says.html) ⭐️ 7.0/10

标普全球评级预测，中国住宅价格可能在 2028 年第三季度触底，一线城市最快明年回升。该机构将判断归因于近期政策：限制开发商预售未完工项目，以及对总价低于 150 万元、面积小于 120 平方米的首套房提供房贷利率补贴。

rss · CNBC Finance · 10月8日 09:27

**「背景」** 标普今年 2 月还认为高库存使楼市复苏无望，但 8 月起政府出台供应限制和房贷补贴改变了其判断。

**「影响」** 摩根士丹利分析师认为，该补贴主要会把购房计划提前，而非创造大量新需求。

**标签**: `#China real estate`, `#S&amp;P Global Ratings`, `#housing market forecast`, `#mortgage policy`, `#property prices`

---

<a id="item-finance-news-3"></a>
### [OpenAI 年化收入比此前报道少 200 亿美元](https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1) ⭐️ 7.0/10

据英国《金融时报》报道，投资者获得的财务文件显示，OpenAI 9 月底年化收入接近 500 亿美元，比此前广泛报道的 700 亿美元少约 200 亿美元。差异部分源于计算口径不同：OpenAI 未计入通过 AWS、谷歌云等云伙伴销售的收入，这可能削弱市场对 AI 需求增长的乐观预期。

telegram · zaihuapd · 10月8日 17:22

**「背景」** 此前媒体广泛引用的约 700 亿美元年化收入估算，与本次披露的接近 500 亿美元存在差异，部分原因在于 Anthropic 将云伙伴渠道收入计入年化收入，而 OpenAI 未采用该口径。

**「市场影响」** 受此消息影响，AI 相关股票周四下跌，投资者对 AI 需求的乐观情绪受到打击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/b66a9858-f8fb-46cb-b506-44bfe26fca2a?syn-25a6b1a6=1">OpenAI annualised revenues $20bn less than previously signalled</a></li>
<li><a href="https://www.investopedia.com/worries-about-openai-revenue-rattle-the-ai-trade-12165038">Worries About OpenAI’s Revenue Rattle the AI Trade</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#artificial intelligence`, `#revenue`, `#financial reporting`, `#technology`

---

<a id="item-finance-news-4"></a>
### [美政府暂停微软绿卡申请资格并指控欺诈](https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea) ⭐️ 7.0/10

特朗普政府宣布暂停微软参与外籍劳工绿卡申请项目，指控其欺诈；副总统万斯称，微软去年裁员 6000 名美国员工，却获得 6300 份 H-1B 签证和近 3000 张绿卡。

telegram · zaihuapd · 10月9日 00:00

**「背景」** H-1B 签证是美国发给外国专业人才的临时工作签证，绿卡则代表美国的永久居留身份；联邦绿卡申请项目允许雇主为持 H-1B 签证的员工申请绿卡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apnews.com/article/h1b-visa-program-vance-microsoft-e7b3a407f822702b269ee277d21343ea">Microsoft being suspended from a green card program as Vance ...</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#immigration policy`, `#H-1B visas`, `#Trump administration`, `#tech industry`

---

<a id="item-finance-news-5"></a>
### [SpaceX 宣布拟收购全美低频段频谱许可证](https://x.com/SpaceX/status/2108291133025698301) ⭐️ 7.0/10

SpaceX 宣布已达成协议，拟收购覆盖全美的低频段频谱许可证组合；公司称，结合 Gen2 星座后，Starlink Mobile 可让美国用户在任何地方获得高速移动宽带。

telegram · zaihuapd · 10月9日 01:04

**「背景」** SpaceX 此前已通过 Starlink 提供卫星宽带服务；低频段频谱（如 800 MHz 频段）传播距离远、穿透力强，适合实现广覆盖的移动网络，此次收购是其进一步进入美国移动通信市场的关键一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/media-telecom/spacex-acquire-spectrum-that-enables-starlink-mobile-services-2026-10-08/">ReutersSpaceX to acquire spectrum that enables Starlink ...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/spacex-agrees-acquire-nationwide-800-212204943.html?fr=sycsrp_catchall">SpaceX Agrees to Acquire Nationwide 800 MHz Low-Band Spectrum ...</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#spectrum acquisition`, `#telecommunications`, `#mobile broadband`

---