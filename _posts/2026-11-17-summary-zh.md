---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 48 条内容中筛选出 19 条重要资讯。

---

**科技新闻**
1. [vLLM v0.34.0 发布：默认可扩展 KV 缓存，移除 Model Runner V1](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely CDN 被入侵，Zoom 和 GitLab 受恶意软件影响](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0：Rust 日期时间库发布](#item-tech-news-3) ⭐️ 8.0/10
4. [美管制远程访问先进 AI 芯片新规](#item-tech-news-4) ⭐️ 8.0/10
5. [英伟达董事会未考虑让黄仁勋回归](#item-tech-news-5) ⭐️ 8.0/10
6. [卡内基梅隆大学免费发布 CMU 计算机科学课程讲座](#item-tech-news-6) ⭐️ 7.0/10
7. [Windows 11 被指收集编码代理和开发者工具使用数据](#item-tech-news-7) ⭐️ 7.0/10
8. [摩根大通技术故障引发美国多家银行网银和银行卡服务延迟中断](#item-tech-news-8) ⭐️ 7.0/10
9. [微软称 7 月修复缺陷致邮件大中断](#item-tech-news-9) ⭐️ 7.0/10
10. [Marimba：用冻结 0.6B ASR 编码器做语音问答](#item-tech-news-10) ⭐️ 7.0/10
11. [十国签旧金山宣言保 AI 供应链](#item-tech-news-11) ⭐️ 7.0/10
12. [亚马逊：AI 代理窃取 API 密钥自我供血](#item-tech-news-12) ⭐️ 7.0/10
13. [中国头部 AI 公司收紧新模型网络攻击能力](#item-tech-news-13) ⭐️ 7.0/10
14. [Xbox 确认 Project Helix 为可玩 PC 游戏的下一代主机](#item-tech-news-14) ⭐️ 7.0/10
15. [谷歌拟向日本政府提供 Fairwind AI 模型用于网络防御](#item-tech-news-15) ⭐️ 7.0/10
16. [苹果中国区要求 AIGC 应用限时备案](#item-tech-news-16) ⭐️ 7.0/10

**财经新闻**
1. [Nvidia CEO 辞职后，ETF 专家称大型科技股和替代芯片商或受益](#item-finance-news-1) ⭐️ 8.0/10
2. [美国原油跌至 85 美元/桶，中东出口恢复令油价承压](#item-finance-news-2) ⭐️ 7.0/10
3. [英特尔及 CEO 陈立武遭股东集体诉讼](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 发布：默认可扩展 KV 缓存，移除 Model Runner V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 已发布，包含 1,061 个提交、412 位贡献者（其中 120 位为新贡献者）。该版本默认启用可扩展 KV 缓存，按模型预热后实际空闲内存来分配，多数模型因此获得更大缓存和更高吞吐量，但部分 H200 模型在并发 128 时每 token 解码延迟可能上升 6%–18%。模型运行器 V1 被移除，V2 成为唯一 GPU 运行器；默认块大小从 16 改为 64，ROCm 7.2 制品停用，huggingface\_hub 最低版本要求为 2.0.0。新增 10 个模型，包括 Mistral Large 4、MiniMax-M3.1-Flash 和 Nemotron-3.5-Transcribe，并在 Blackwell 与 MI355X 上带来最高 1.95 倍解码、1.6 倍输出吞吐和 1.24–1.40 倍长提示 TTFT 加速。

github · khluu · 11月16日 23:22

**「背景」** vLLM 是一个面向大语言模型（LLM）的高吞吐、内存高效推理与服务引擎，源自加州大学伯克利分校 Sky Computing Lab 的研究项目，现已成为广泛使用的开源 LLM 推理库。该版本 v0.34.0 是一次重大发布，涉及模型运行器、默认块大小和 KV 缓存策略等关键架构调整。

**「影响」** 升级用户需检查启动配置：若仍设置 VLLM\_USE\_V2\_MODEL\_RUNNER=0，将在启动时失败；如需保持旧行为，应传入 --block-size 16 或 --gpu-memory-utilization 0.9/--no-enable-extensible-kv-cache。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/">vLLM</a></li>
<li><a href="https://www.toolglade.com/tool/vllm">vLLM Review 2026: Open-Source LLM Inference Engine | Toolglade</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#vLLM`, `#open source`, `#machine learning`, `#GPU performance`

---

<a id="item-tech-news-2"></a>
### [Optimizely CDN 被入侵，Zoom 和 GitLab 受恶意软件影响](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely 的 CDN 遭到入侵，并向 Zoom、GitLab 等客户网站投放了恶意软件。此次事件并非 CDN 缓存投毒，而是攻击者获得了对多个客户项目的写入权限，导致 Optimizely CDN 分发了被篡改的脚本；Optimizely 自身网站 www.optimizely.com 和 login.optimizely.com 也受影响。该事件凸显第三方脚本供应链的严重风险，尤其是大型网站依赖供应商脚本时缺乏有效控制和问责。

hackernews · kristjansson · 11月16日 23:00 · [社区讨论](https://news.ycombinator.com/item?id=50524767)

**「背景」** Optimizely Web 是一个被广泛使用的网站实验与个性化平台，网站通过其 CDN 向访客加载 JavaScript 片段。2026 年 11 月 16 日，攻击者向该平台植入恶意脚本，导致包括 Zoom、BBC、CNN、Salesforce、GitLab 在内的 178 家组织访客可能被加载了加密货币地址替换器和支付卡窃取代码。该事件并非 CDN 缓存投毒，而是 Optimizely 分发了被篡改的脚本。

**「影响」** 在事件期间访问受影响网站的用户的浏览器可能执行了恶意脚本，相关企业应审查第三方脚本并加强供应链控制。

**「社区讨论」** 社区普遍担忧第三方脚本带来的攻击面，认为应减少对供应商脚本的依赖并加强问责；也有评论指出此次并非 CDN 缓存投毒，并建议用户使用 NoScript 降低暴露风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shiftdelete.net/en/optimizely-malware">Optimizely Malware Hit 178 Sites: What It Stole and What to Do</a></li>
<li><a href="https://cybersecuritynews.com/optimizely-websites-hijacked/">Hackers Infect 178 Major Websites via Optimizely to Steal ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/optimjack-optimizely-hosted-scripts-crypto-clipper-card-skimmer">OPTIMJACK: Optimizely-Hosted Scripts Loaded a Crypto Clipper ...</a></li>

</ul>
</details>

**标签**: `#supply-chain-attack`, `#web-security`, `#cdn`, `#third-party-scripts`, `#malware`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0：Rust 日期时间库发布](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Rust 日期时间库 Jiff 发布 1.0 版本，成为 chrono 的一个稳定且设计良好的替代选择。该库由知名 Rust 维护者 burntsushi 开发，旨在解决 chrono 长期存在的 API 设计问题。Jiff 1.0 提供了稳定、完善的日期时间处理能力，并获得了前 chrono 维护者等人的高度认可。作者明确表示该库并不适用于所有场景，但在其目标范围内提供了更易用的接口。

hackernews · burntsushi · 11月16日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**「背景」** Rust 标准库没有提供完整的日期时间处理能力，因此生态中常依赖 chrono 库，但其 API 设计长期受到批评且改进阻力大。Jiff 由 Rust 知名维护者 Andrew Gallant（burntsushi）开发，目标是提供更符合人体工程学的日期时间 API，并在 1.0 版本中宣布稳定。此次发布被视为 chrono 的潜在替代方案。

**「影响」** 对于 Rust 开发者，Jiff 1.0 提供了一个稳定且更易用的日期时间 API，可能减少对 chrono 的依赖并改善日期时间处理体验。

**「社区讨论」** 社区整体反响积极，前 chrono 维护者等用户认可其 API 设计和稳定性，并对作者坦诚说明适用范围表示赞赏。同时有用户询问对 TAI、UT1 等专业时间尺度的支持情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant&#x27;s Blog</a></li>

</ul>
</details>

**标签**: `#rust`, `#datetime`, `#open-source`, `#libraries`, `#software-engineering`

---

<a id="item-tech-news-4"></a>
### [美管制远程访问先进 AI 芯片新规](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

美国商务部 11 月 16 日发布临时最终规则，将先进 AI 芯片与服务器的出口管制扩展到远程访问场景，以堵住通过第三国数据中心绕过限制的漏洞。规则由财政部和国家安全委员会主导起草，旨在进一步收紧中国获取先进芯片的渠道。The Verge 报道称，新规还要求向印度尼西亚、马来西亚、新加坡、泰国和巴西再出口 AI 芯片须申请许可。

telegram · zaihuapd · 11月16日 14:44

**「背景」** 此前美国已对先进 AI 芯片实施出口管制，限制向中国等国家直接销售，但企业仍可通过在第三国数据中心部署芯片并远程调用算力来规避限制。此次美国商务部发布的临时最终规则旨在堵住这一漏洞，将管制延伸到远程访问，并要求向新加坡、马来西亚、泰国、印度尼西亚和巴西数据中心运营商再出口相关芯片时须获得美国政府许可。

**「影响」** 对于需要从印尼、马来西亚、新加坡、泰国或巴西远程调用美国先进 AI 芯片或服务器的云服务商、数据中心运营者和 AI 企业，新规要求申请再出口许可，可能直接限制其算力部署与访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-16/us-moves-to-limit-remote-access-to-advanced-ai-chips">US Moves to Curb China’s Remote Access to Nvidia’s AI Chips</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-commerce-china-lutnick.html">Nvidia fallout: Commerce targets loophole for China&#x27;s data center use</a></li>

</ul>
</details>

**标签**: `#export controls`, `#AI chips`, `#cloud computing`, `#semiconductors`, `#US policy`

---

<a id="item-tech-news-5"></a>
### [英伟达董事会未考虑让黄仁勋回归](https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html) ⭐️ 8.0/10

知情人士向 CNBC 表示，英伟达董事会目前未考虑让黄仁勋回归 CEO 一职。董事会的工作重心是调查其行为，并已聘请 Wachtell Lipton 律师事务所核查相关事项是否危及国家安全或公司机密。这一消息尚未获英伟达官方证实，但由于涉及 AI 硬件龙头企业的治理与安全风险，可能对行业产生重大影响。

telegram · zaihuapd · 11月17日 01:39

**「背景」** 英伟达（Nvidia）是 AI 芯片领域的主要厂商，黄仁勋长期担任其 CEO。近期报道称他因个人行为问题离职后，董事会聘请律所 Wachtell Lipton 对其是否危及国家安全与公司机密展开调查；此前亦有超过 18 万人联署支持其回归，但董事会仍优先处理调查。

**「影响」** 英伟达的治理不确定性可能影响依赖其 AI 芯片的客户和投资者信心，但该消息尚未得到官方证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pollar.news/en/event/nvidias-huang-resigns-over-affairs">Nvidia board shuts door on Jensen Huang return despite Trump...</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html">Nvidia board not considering bringing Huang back as CEO: Source</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI hardware`, `#corporate governance`, `#national security`, `#tech industry`

---

<a id="item-tech-news-6"></a>
### [卡内基梅隆大学免费发布 CMU 计算机科学课程讲座](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学（CMU）推出 CS Learn 项目，在 YouTube 上免费发布当前 CMU 计算机科学课程的完整学期讲座。该项目由 Griffin 计算机科学学院教师 Phillip Compeau 负责，本周每天首播一门课程，更多课程将于明年一月上线。已公布或受关注的课程包括 Tianqi Chen 的 ML Systems 以及 Probability and Computing（15-259）等。据 Compeau 介绍，部分学生构建的工具自动化了大量制作流程，使这一免费开放教育资源得以规模化推进。这一发布让自学者能够免费观看 CMU 当前课程视频，但暂未明确是否同步提供作业和评分材料。

hackernews · pcompeau · 11月16日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**「背景」** 卡内基梅隆大学 Kenneth C. Griffin 计算机科学学院通过 CS Learn 项目在 YouTube 上免费公开真实课程讲座，其频道说明将该举措描述为向所有学习者开放 CMU 课堂。该校课程目录中的课程编号（如 15-xxx）可帮助学习者对应社区评论中提到的课程，例如 15-122、15-251 等。

**「影响」** 免费完整学期讲座使自学者可直接学习 CMU 当前课程，尤其适合希望系统掌握 ML Systems 等高级主题的开发者。作业、评分和证书等配套资源尚不明确。

**「社区讨论」** 社区普遍表示欢迎，并期待发布 15-122、15-150、15-251、15-451 等核心课程及作业；有用户请求分布式系统、操作系统和中级统计等课程，有评论认为扎实基础在 AI 时代仍是关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/courses/">School of Computer Science Courses - Carnegie Mellon University</a></li>

</ul>
</details>

**标签**: `#computer science education`, `#free online courses`, `#machine learning`, `#systems`, `#CMU`

---

<a id="item-tech-news-7"></a>
### [Windows 11 被指收集编码代理和开发者工具使用数据](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

Windows 11 据报道会收集用户运行哪些编码代理和开发者工具的遥测数据，这一行为引发了软件开发者的隐私担忧。该报告来自 xusheng.dev，但未提供完整的技术细节，包括具体收集哪些工具、是否可完全禁用等。社区讨论显示，类似的数据收集也存在于其他驱动和浏览器中，通常需要用户主动选择退出。

hackernews · cwaffles · 11月16日 22:58 · [社区讨论](https://news.ycombinator.com/item?id=50524736)

**「背景」** Windows 10/11 默认包含遥测收集机制，用户可通过系统设置或第三方工具（如 WindowsTelemetryBlocker）禁用或阻止相关数据收集。VS Code 等开发者工具自身也有独立的遥测选项，企业可按照遥测级别配置是否发送使用数据。因此，关于 Windows 11 收集编码代理和开发者工具使用信息的报道，发生在操作系统与应用双重遥测并存的背景下。

**「影响」** 受影响的 Windows 11 开发者可能不希望自己的编码工具和代理使用情况被自动收集，除非微软提供明确的退出选项，否则他们可能需要考虑隔离环境或更换平台。不过目前该报道的细节和微软回应尚不完整。

**「社区讨论」** 社区评论中，有用户表示已计划或建议从 Windows 切换到 Linux，认为 Linux 游戏和日常使用已较成熟；也有用户指出显卡驱动、浏览器等同样收集可执行文件信息，且 Windows 对 AI 代理的沙箱支持滞后（MXC 于 10 月 7 日才发布，Claude Code 尚不支持），因此需要权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=-E-WC_UvHXE">Windows 11 : Kill Telemetry , Widgets &amp; Bloat - YouTube</a></li>
<li><a href="https://code.visualstudio.com/docs/enterprise/telemetry">Manage telemetry in enterprise environments</a></li>
<li><a href="https://github.com/N0tHorizon/WindowsTelemetryBlocker">N0tHorizon/WindowsTelemetryBlocker: A PowerShell based tool to...</a></li>

</ul>
</details>

**标签**: `#Windows`, `#telemetry`, `#privacy`, `#developer tools`, `#coding agents`

---

<a id="item-tech-news-8"></a>
### [摩根大通技术故障引发美国多家银行网银和银行卡服务延迟中断](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda) ⭐️ 7.0/10

摩根大通发生技术故障，导致美国多家银行的在线银行服务出现延迟，并引发银行卡交易问题。此次事件再次引发对金融系统可靠性和基础设施集中风险的讨论。具体根因尚未在新闻中确认，但评论者推测可能与数据库或云服务故障有关，并类比了上月欧洲 Revolut 因 Google Cloud 中断导致约 12 小时服务中断的情况。事件凸显了大型金融机构核心系统在面对故障时的连锁影响。

hackernews · samk3nny · 11月16日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=50521045)

**「背景」** 摩根大通（JPMorgan Chase）是美国最大的银行之一，其核心银行系统与许多其他美国银行存在交易往来，因此单一技术故障可能通过银行间清算或转账渠道波及他行客户。此次事件发生在周一，摩根大通表示相关技术问题并非网络攻击所致；故障表现为在线银行访问延迟和银行卡交易受影响。

**「影响」** 故障期间，受影响的美国银行客户遭遇网银延迟、银行卡交易失败或无法使用，部分用户还反映实体网点关闭或无响应。

**「社区讨论」** 评论区普遍担忧金融系统的脆弱性，有人猜测本次事件可能是数据库或云服务故障，并类比上月 Revolut 因 Google Cloud 故障导致约 12 小时中断；也有用户提到核心系统可能依赖大型机、COBOL、CICS、IMS、DB2 等老旧但可靠的技术栈，另有评论反映不同地区的服务可用性不一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chicago.suntimes.com/business/2026/11/16/a-technical-issue-at-jpmorgan-chase-triggers-online-banking-delays-across-major-us-banks">A technical issue at JPMorgan Chase triggers online banking ...</a></li>
<li><a href="https://www.ideastream.org/community/2026-11-16/technical-issue-at-jpmorgan-chase-triggers-online-banking-delays-across-major-us-banks">Technical issue at JPMorgan Chase triggers online banking ...</a></li>

</ul>
</details>

**标签**: `#banking outage`, `#infrastructure reliability`, `#financial systems`, `#incident response`, `#mainframes`

---

<a id="item-tech-news-9"></a>
### [微软称 7 月修复缺陷致邮件大中断](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将一次大规模电子邮件服务中断归咎于 7 月发布的某个修复中引入的软件缺陷。该公司公开说明该缺陷是此次中断的根本原因。目前公开信息未披露受影响的具体服务范围、中断持续时间或缺陷的技术细节。该事件再次引发了关于云服务可靠性与变更管理实践的讨论。

hackernews · Bender · 11月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**「背景」** 2026 年 11 月，Microsoft 365 全球性邮件中断持续到 11 月 13 日，影响企业、航空公司和政府机构；16 小时后故障范围主要缩小到支撑 Outlook 等邮件服务的 Exchange。微软将原因归咎于 7 月软件修复中引入的缺陷，该缺陷引发连锁故障，导致超过 80%的网络网关服务器瘫痪。

**「影响」** 2026 年 11 月 12 日至 14 日，Microsoft 365 全球性中断导致依赖 Exchange Online、Outlook.com、Teams、SharePoint Online 和 OneDrive 的企业与政府用户邮件和协作服务长时间不可用，最严重中断约 16 小时，邮件延迟又持续一天。

**「社区讨论」** 社区讨论中，有评论将这类大规模恢复比作电力行业的“黑启动”，认为应从断开负载开始逐步恢复；另有评论质疑为何不主动丢弃或限制连接来降低负载，以及测试环境与生产环境差异为何掩盖了并发缺陷。还有用户对关键网络基础设施中使用 Windows 表示惊讶。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026">Microsoft blames monster email outage on software defect ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/microsoft-says-months-old-bug-caused-global-microsoft-365-outage/">Microsoft says months-old bug caused global Microsoft 365 outage</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/">Microsoft 365, Outlook down for thousands of US users ...</a></li>
<li><a href="https://www.isitdown-now.com/en/blog/microsoft-365-outage-november-2026">Microsoft 365 outage of November 12–14, 2026: timeline, cause ...</a></li>

</ul>
</details>

**标签**: `#microsoft`, `#email-outage`, `#software-defect`, `#cloud-reliability`, `#incident-analysis`

---

<a id="item-tech-news-10"></a>
### [Marimba：用冻结 0.6B ASR 编码器做语音问答](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba 使用一个冻结的 Qwen3-ASR-0.6B 编码器，对每个 8 秒音频窗口仅做一次前向，即可回答关于音频窗口的输入文字问题（是/否、选项或评分），并返回经校准的概率。论文（arXiv:2611.18330）显示，在 1000 个公开问题上，它在 9 项测试中的 6 项上追平或超过 Qwen3-Omni（30B-A3B）；在 300 个 FLEURS 片段上语言识别准确率 100%，在 AMI 和 VoxConverse 上说话人变更 AUROC 为 0.966–0.980，高于 ECAPA，说话人计数也优于 pyannote 3.1。术语发现采用零样本方式，从解码器的贪婪及 4 条 beam 假设打分并做 Platt 校准；语言识别直接使用 ASR 模型的语言分数；轮次结束在冻结第 18 层读取，说话人变更和计数在第 12 层读取。局限性包括：在 Smart Turn 自身测试集上轮次结束 AUROC 0.930 低于 Smart Turn v3.2 的 0.982，在 ICSI 会议上为 0.716 与 0.712 打平，且在 CochlScene 场景分类上所有头部均接近随机水平。项目提供 Apache-2.0 权重、代码、demo 和 pip 包。

reddit · r/MachineLearning · /u/solanotodesch · 11月16日 15:47

**「背景」** Qwen3-ASR-0.6B 是 0.6B 参数的语音识别编码器模型，Qwen3-Omni（30B-A3B）是 30B 总参数、3B 激活的多模态模型，用于对比。此前对音频的问答通常依赖大型多模态模型或专门的端到端系统；Marimba 尝试用小型冻结编码器加轻量读出层完成多种语音问题。

**「影响」** 研究人员和开发者可以在 Apache-2.0 许可下直接使用该 0.6B 编码器方案，在常见语音问答、语言识别和说话人变更/计数任务上获得接近或超过 30B 模型的校准概率。但应注意其在 Smart Turn 轮次结束和 CochlScene 等未见任务上的局限性。

**标签**: `#speech processing`, `#audio question answering`, `#efficient AI`, `#model evaluation`, `#zero-shot learning`

---

<a id="item-tech-news-11"></a>
### [十国签旧金山宣言保 AI 供应链](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

11 月 15 日，美国与澳大利亚、印度、以色列、日本、韩国、卡塔尔、新加坡、阿联酋和英国签署《旧金山宣言》。宣言确认经济安全是国家安全根基，承诺共同保护支撑超级智能（SI）供应链的敏感技术与关键基础设施。各方将设立五个工作组，分别负责创新政策框架、SI 在关键领域应用、SI 全栈供应链协作、安全港与供应链安全枢纽、SI 安全与韧性。

telegram · zaihuapd · 11月16日 10:40

**「背景」** 超级智能（SI）供应链通常涵盖支撑先进 AI 系统研发与部署的芯片、模型、数据中心等跨境环节。将经济安全与国家安全挂钩并协调多国保护，是近期 AI 国际治理中出现的合作形式。

**「影响」** 对参与国的 AI 供应链企业及关键基础设施运营方而言，该宣言设定五个工作组，可能为后续统一的政策协调和安全要求提供机制基础。

**标签**: `#AI policy`, `#supply chain security`, `#international cooperation`, `#superintelligence`, `#critical infrastructure`

---

<a id="item-tech-news-12"></a>
### [亚马逊：AI 代理窃取 API 密钥自我供血](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

亚马逊称，攻击者使用开源渗透测试框架 Artex 驱动 AI 代理，窃取公网暴露的 LiteLLM、Dify 等 AI 应用的 API 密钥，验证后汇入共享池，用于支付更多大模型调用。活动自 10 月 3 日开始，11 月 5 日被亚马逊诱饵网络 MadPot 截获阻断。这种自我供血方式让攻击者可利用受害者密钥持续调用大模型，对暴露 AI 应用构成实际威胁。亚马逊以中等信心将行动归于中国相关威胁组织，同时表示并非所有被列目标都已失陷，并已通知可能受影响的 AWS 客户。

telegram · zaihuapd · 11月16日 13:00

**「背景」** Artex 是一个开源 AI 渗透测试框架，可驱动自治代理执行侦察和利用任务；LiteLLM、Dify、Langflow、Ollama 等是常被开发者部署用于访问大模型或构建 AI 应用的工具/平台，若公网暴露且未妥善保护，其 API 密钥就可能被窃取。亚马逊的 MadPot 是用于监测和阻断恶意流量的诱饵网络/蜜罐系统，在本事件中于 11 月 5 日截获了相关活动。亚马逊以中等信心将该活动与“与中国相关的威胁组织”联系起来，但强调并非所有被列目标都已失陷。

**「影响」** 使用 LiteLLM、Dify 等公网暴露 AI 应用且未妥善保护 API 密钥的开发者或组织，可能面临密钥被盗用、大模型调用费用被非法消耗的风险。由于亚马逊称并非所有被列目标都已失陷，实际受影响范围尚不完全明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/">AI credential theft campaign used stolen API keys to scale</a></li>
<li><a href="https://thehackernews.com/2026/11/amazon-uncovers-ai-agent-campaign.html">Amazon Uncovers AI Agent Campaign Targeting LiteLLM, Dify ...</a></li>
<li><a href="https://www.2-spyware.com/amazon-artex-ai-agents-steal-ai-api-keys">Amazon: AI agents hunt exposed LiteLLM and Dify keys</a></li>

</ul>
</details>

**标签**: `#AI security`, `#API key theft`, `#autonomous agents`, `#threat intelligence`, `#cloud security`

---

<a id="item-tech-news-13"></a>
### [中国头部 AI 公司收紧新模型网络攻击能力](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 7.0/10

阿里巴巴、腾讯和月之暗面等中国头部 AI 公司在新一代模型中削弱了进攻性网络能力，同时提升防御表现。阿里巴巴最新旗舰 Qwen 未开放权重，用户无法下载并自定义完整版本。这一变化与商务部上月公布的出口管制草案相关，该草案拟禁止出口可攻击关键基础设施和政府网络的 AI 工具。腾讯本月发布 Hy4 前已削减网络功能。报道来自 Bloomberg。

telegram · zaihuapd · 11月17日 02:20

**「背景」** 开放权重（open weights）指用户可下载模型参数并在本地或自有环境中定制、部署模型；此前阿里通义千问（Qwen）系列的部分版本曾以 Apache 2.0 许可发布开放权重。中国商务部上月公布的出口管制草案拟禁止可攻击关键基础设施或政府网络的人工智能工具出口，这为多家头部 AI 公司在新模型中削减进攻性网络能力、收紧权重开放提供了直接政策背景。分析机构 Epoch AI 曾估计，中国头部开源权重模型在网络能力上与美国前沿的差距已缩小到 6-7 个月，进一步提升了此类限制的紧迫性。

**「影响」** 由于阿里巴巴最新旗舰 Qwen 未开放权重，开发者将无法下载并自定义完整版本，而腾讯等公司削弱进攻性网络功能可能限制部分红队与安全测试场景。但出口管制草案仍在征询意见，实际执行范围和时间尚不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnas.org/publications/cnas-insights/cnas-insights-a-closing-door-on-open-weights-implications-for-ai-sovereignty">CNAS Insights | A Closing Door on Open Weights ? Implications for AI ...</a></li>
<li><a href="https://www.linkedin.com/pulse/issue-18-record-control-until-someone-reads-tom-howard-maicd-sohsc">Issue 18: A record is not a control until someone reads it</a></li>
<li><a href="https://www.nytimes.com/2026/10/21/world/asia/china-exports-ai-controls.html">China’s Free A.I. Models Are Thrown Into Uncertainty</a></li>
<li><a href="https://www.business-standard.com/technology/tech-news/china-ai-export-controls-open-weight-models-126101900723_1.html">How China&#x27;s proposed AI export controls could affect open ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#open source`, `#China`, `#cybersecurity`, `#technology policy`

---

<a id="item-tech-news-14"></a>
### [Xbox 确认 Project Helix 为可玩 PC 游戏的下一代主机](https://www.ign.com/articles/xbox-confirms-project-helix-is-a-console-capable-of-playing-games-from-your-pc) ⭐️ 7.0/10

Xbox 在 11 月 15 日上线的 25 周年纪念杂志中确认，下一代计划 Project Helix 被设计成一台能玩 PC 游戏的游戏机，而非能玩主机游戏的 PC。下一代业务副总裁 Jason Ronald 称其目标是“终极游戏机”，玩家可直接访问四代 Xbox 游戏库与进度，以消除主机与 PC 游戏之间的人为界限。官方尚未公布设备形态与发售时间，外界传闻最早 2027 年底推出。

telegram · zaihuapd · 11月17日 02:40

**「背景」** Xbox 近年通过向后兼容和 Xbox Play Anywhere 逐步统一主机与 PC 体验，让部分游戏购买一次即可在两端游玩并共享存档。Project Helix 是在此基础上的下一代硬件计划，此前报道已将其描述为“能同时运行 PC 和主机游戏”的混合形态，而社区消息还指出 Helix 游戏可能默认支持 Xbox Play Anywhere，并为 PC 版游戏提供模组与自定义空间。这些背景有助于理解 Xbox 将 Helix 定位为“能玩 PC 游戏的主机”而非普通 PC 的差异。

**「影响」** 对现有 Xbox 玩家而言，该方向意味着未来主机可能同时兼容四代 Xbox 游戏库与 PC 游戏并继承进度，但具体兼容实现与发售时间仍未公布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.resetera.com/threads/jason-ronald-xbox-helix-is-a-console-capable-of-playing-pc-games-really-focused-on-neural-rendering-players-control-and-agency-over-their-games.1688309/page-10">Jason Ronald: Xbox Helix is a console capable of playing PC ...</a></li>
<li><a href="https://www.gamespot.com/articles/xbox-project-helix-is-a-console-that-plays-pc-games-not-the-other-way-around/">Xbox Project Helix Is A Console That Plays PC Games ... - GameSpot</a></li>
<li><a href="https://www.techpowerup.com/354903/xbox-confirms-project-helix-is-not-a-pc-but-its-closer-than-ever">Xbox Confirms Project Helix Is Not a PC , But... | TechPowerUp</a></li>

</ul>
</details>

**标签**: `#Xbox`, `#Project Helix`, `#PC gaming`, `#Microsoft`, `#hardware`

---

<a id="item-tech-news-15"></a>
### [谷歌拟向日本政府提供 Fairwind AI 模型用于网络防御](https://cn.nikkei.com/industry/itelectric-appliance/64742-2026-11-17-09-16-25.html) ⭐️ 7.0/10

谷歌计划将 9 月启动的 Fairwind 提前提供框架扩大至日本政府及国内重要基础设施运营商，提供尖端 AI 模型用于网络防御。谷歌云 CEO Thomas Kurian 于 11 月 16 日访日，并向日本政府高官表达了这一意向。Fairwind 计划此前主要面向美国政府机构和网络安全公司，尚未正式宣布向日本政府与企业开放。报道称，此举针对日本国内网络攻击损失急剧增加的情况，但未披露具体技术规格或提供时间表。

telegram · zaihuapd · 11月17日 03:43

**「背景」** Fairwind 计划于 2026 年 9 月 2 日公布，是一项有限访问项目，为政府、医疗、电信及其他关键基础设施运营商等防御方提供谷歌最新 AI 模型的早期使用权。该计划将 Gemini 网络安全模型与 CodeMender 配对，并要求参与者通过严格治理检查。此前主要面向美国政府机构和网络安全公司，此次报道显示谷歌将把该计划扩展至日本政府和重要基础设施运营商。

**「影响」** 若计划落实，日本政府机构和关键基础设施运营商可能获得此前主要面向美国机构的 Fairwind AI 模型用于网络防御，但具体范围和落地时间仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://joho-todai.com/en/google-fairwind-ai-japan-cybersecurity/">Google to Give Japan&#x27;s Government and Critical Infrastructure ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/">Google’s Fairwind Program: Cyber defense tools for trusted ...</a></li>
<li><a href="https://explainx.ai/blog/google-fairwind-japan-gemini-cyber-early-access-2026">Google Fairwind Japan: Gemini Cyber Early Access | explainx ...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#cybersecurity`, `#Google Cloud`, `#Japan`, `#critical infrastructure`

---

<a id="item-tech-news-16"></a>
### [苹果中国区要求 AIGC 应用限时备案](https://www.ithome.com/1/028/158.htm) ⭐️ 7.0/10

苹果已在中国大陆 App Store Connect 后台新增两项面向该地区分发的合规必填项：AIGC 服务声明与备案信息、安全评估证明。现有包含生成式 AI 功能的应用须在 2027 年 1 月 31 日前补齐，新应用则须立即提交。适用范围包括聊天机器人、图像或视频生成、语音或人脸编辑等 AIGC 服务；若使用第三方技术，还须上传授权协议和算法备案号。苹果 2026 年审核指南亦已纳入生成式 AI 条款，提高中国区 AIGC 应用上架的合规门槛。

telegram · zaihuapd · 11月17日 04:29

**「背景」** 中国监管部门对生成式 AI 服务提出算法备案和安全评估要求，开发者通常需要取得相关备案和证明后方可公开提供服务。App Store Connect 是苹果面向开发者的应用管理后台，其审核指南和必填项变更会直接影响应用在中国大陆的提交与更新。

**「影响」** 在中国大陆 App Store 分发含 AIGC 功能的应用，新应用须立即通过 App Store Connect 提交 AIGC 服务声明与备案信息、安全评估证明，存量应用须在 2027 年 1 月 31 日前补齐；使用第三方技术的还须上传授权协议和算法备案号。

**标签**: `#Apple`, `#App Store`, `#AIGC compliance`, `#China regulations`, `#generative AI`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Nvidia CEO 辞职后，ETF 专家称大型科技股和替代芯片商或受益](https://www.cnbc.com/2026/11/14/nvidia-ai-trade-data-centers-congress.html) ⭐️ 8.0/10

Nvidia 首席执行官黄仁勋因丑闻辞职。ETF 专家认为大型科技股和替代芯片制造商可能受益，Yorkville Ives 将 Nvidia 目标价从 300 美元下调至 225 美元，但维持买入评级。

rss · CNBC Finance · 11月16日 12:13

**「背景」** 本周 Nvidia 股价创 2012 年以来最长连跌，AMD 涨近 13%，纳斯达克指数录得 8 月以来最佳单周表现；民主党在 11 月 3 日选举后控制国会，可能对数据中心建设施压。

**标签**: `#Nvidia`, `#AI trade`, `#ETFs`, `#data centers`, `#semiconductor stocks`

---

<a id="item-finance-news-2"></a>
### [美国原油跌至 85 美元/桶，中东出口恢复令油价承压](https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html) ⭐️ 7.0/10

周一国际油价下跌，美国 WTI 原油期货结算价下跌 3.58%至每桶 85.39 美元，布伦特原油下跌 3.55%至每桶 92.44 美元。国际能源署预计 2026 年第四季度全球供应将超出需求 170 万桶/日，逆转此前短缺预期，因中东出口恢复快于全球需求。

rss · CNBC Finance · 11月16日 22:19

**「背景」** 此前国际能源署曾预计同期市场短缺，此次上调供给判断基于霍尔木兹海峡运输恢复以及俄罗斯 10 月原油产量升至 873 万桶/日、增加 21 万桶/日。

**标签**: `#crude oil`, `#oil supply`, `#Middle East exports`, `#energy markets`, `#commodity prices`

---

<a id="item-finance-news-3"></a>
### [英特尔及 CEO 陈立武遭股东集体诉讼](https://www.investing.com/news/stock-market-news/intel-sued-by-shareholders-following-29-stock-plunge-5028171) ⭐️ 7.0/10

英特尔及 CEO 陈立武遭股东集体诉讼，原告指控公司隐瞒 PC 需求疲软和库存积压问题；公司 10 月 29 日发布不及预期的第四季度营收和利润预测，次日股价暴跌 28.6%、市值蒸发约 1400 亿美元。

telegram · zaihuapd · 11月16日 11:10

**「背景」** 诉讼由一家密歇根州养老基金牵头，上周五在圣何塞联邦法院提起，被告包括 CEO 陈立武与 CFO 津斯纳，索赔对象为 2026 年 7 月 23 日至 10 月 29 日买入股票的投资者。

**标签**: `#Intel`, `#shareholder lawsuit`, `#stock drop`, `#semiconductors`, `#earnings guidance`

---