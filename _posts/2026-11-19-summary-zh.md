---
layout: default
title: "Horizon Summary: 2026-11-19 (ZH)"
date: 2026-11-19
lang: zh
---

> 从 43 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [Xint 披露 5 个 nginx 漏洞可打主机 root](#item-tech-news-1) ⭐️ 9.0/10
2. [Google 发布 Gemini 4 Neon 新模型](#item-tech-news-2) ⭐️ 8.0/10
3. [微软 Ignite 2026 发布七款高性价比新模型](#item-tech-news-3) ⭐️ 7.0/10
4. [DNS 解析器不应成为反盗版战场](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenAI 模型推进芯片设计](#item-tech-news-5) ⭐️ 7.0/10
6. [Genie 4 已向符合条件的 Google AI Ultra 订阅者开放](#item-tech-news-6) ⭐️ 7.0/10
7. [旅行者 1 号交互拆解：从核电池到单个存储位](#item-tech-news-7) ⭐️ 7.0/10
8. [Daniel Stenberg 对比 AI 生成的 Rust 重写与 curl 实际维护](#item-tech-news-8) ⭐️ 7.0/10
9. [微信小微测试范围扩大，日活达 3000 万](#item-tech-news-9) ⭐️ 7.0/10
10. [DeepSeek 服务端搜索与网页抓取改为免费](#item-tech-news-10) ⭐️ 7.0/10
11. [美政府考虑要求企业披露使用中国 AI](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [美联储会议纪要：官员预计将继续加息并担忧 AI 通胀风险](#item-finance-news-1) ⭐️ 8.0/10
2. [美联储理事沃勒：12 月或需加息 50 个基点以“震撼”抗通胀](#item-finance-news-2) ⭐️ 8.0/10
3. [APEC 深圳峰会：特朗普、习近平与普京将举行首次三方会晤](#item-finance-news-3) ⭐️ 7.0/10
4. [腾讯公布三季报：AI 资本开支 814 亿元远超预估，自由现金流转负](#item-finance-news-4) ⭐️ 7.0/10
5. [中韩宣布自贸协定服务投资后续谈判实质性结束](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Xint 披露 5 个 nginx 漏洞可打主机 root](https://nginx2root.com/) ⭐️ 9.0/10

Xint 公开了 NGINX2Root 漏洞链，包含 5 个 nginx 漏洞和 1 个 Linux 内核缺陷，攻击者可从 nginx 访客一路提权到主机 root。其中 CVE-2026-123007 是 HTTP/2 流控内存破坏，无需认证即可在 worker 进程中执行命令。nginx 1.30.7 与 1.31.9 于 11 月 18 日修复了共 10 个 CVE，Rapid7 已放出 PoC，目前暂无在野利用。如果无法升级，应关闭对外 HTTP/2 以缓解风险。

telegram · zaihuapd · 11月18日 16:21

**「背景」** nginx 是一种广泛部署的 Web 服务器、反向代理和负载均衡器；HTTP/2 的多路复用和流控机制实现复杂，历史上多次成为内存破坏类漏洞的来源。此次被称为 NGINX2Root 的链路由五个 nginx 漏洞（含 HTTP/2 流控内存破坏）与一个 Linux 内核缺陷组成：攻击者先在 nginx worker 进程中实现未认证代码执行，再利用内核缺陷把权限提升到主机 root。F5/NGINX 已发布修复版本 1.30.7 和 1.31.9，并建议无法升级时关闭对外 HTTP/2 作为缓解措施。

**「影响」** 对于运行 HTTP/2 且未升级到 nginx 1.30.7 或 1.31.9（或未禁用 HTTP/2）的用户，未经认证的攻击者可利用已公开的 PoC 远程执行代码并结合 Linux 内核缺陷将权限提升到 root，导致服务器完全失陷；目前尚无公开的在野利用报告。

**「社区讨论」** 评论区指出，该修复曾在开源仓库提前一周出现且提交信息包含“Reported by Xint.io”，但 F5/Nginx 和报告方未及时发布 PSA，工作负载仅需禁用 HTTP/2 即可缓解。也有用户强调 HTTP/2 在 nginx 中默认关闭、仅约 12% 服务器启用，且利用需要 128GB HTTP/2 流量和特定 CPU 指令，因此实际风险有限。

<details><summary>参考链接</summary>
<ul>
<li>NGINX2Root: Patched nginx packages released | AlmaLinux OS</li>
<li>NGINX2Root: Five Critical NGINX Flaws Expose Web Servers to Remote Code Execution</li>
<li>Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007 | Wiz Blog</li>
<li>CVE-2026-123007: Critical NGINX HTTP/2 Integer Underflow Leads to RCE (FIXED)</li>
<li>NGINX ( HTTP/2 ) - Critical Remote Code Execution Vulnerability (CVE-2026-123007)</li>

</ul>
</details>

**标签**: `#nginx`, `#security`, `#CVE`, `#privilege escalation`, `#remote code execution`

---

<a id="item-tech-news-2"></a>
### [Google 发布 Gemini 4 Neon 新模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 8.0/10

Google 宣布推出 Gemini 4 Neon，这是其 Gemini AI 家族中的一个新模型。目前可用的公告片段未包含官方技术规格、基准测试或参数细节。社区讨论指出，Neon 在 OpenRouter 上表现出比 Gemini 4 Carbon 更快的生成速度（约 127 tokens/s 对比 46 tokens/s），并被视为整体智能更高但长程研究推理能力较弱的选项。该发布引发了关于模型命名疲劳的讨论，以及将其与 Anthropic Opus 5.5 等竞品的对比。

hackernews · yigitdemirag · 11月18日 21:34 · [社区讨论](https://news.ycombinator.com/item?id=50552424)

**「背景」** Gemini 4 Neon 是谷歌 Gemini 4 系列的新模型，由 Gemini 4 Carbon 适配而来，定位为在复杂编码、分析等任务中提供前沿级智能，同时成本更低、更适合生产代码。它支持文本、图像、音频和视频输入，组合上下文窗口最高可达 1M token。谷歌称其在部分基准上可超越旗舰 Carbon，并且速度最高可达 Carbon 的三倍。

**「影响」** 根据社区观察，开发者若优先考虑响应速度，Neon 在 OpenRouter 上的约 127 tokens/s 生成速度优于 Carbon，但在研究级长程推理任务上可能仍需依赖 Carbon。

**「社区讨论」** 评论区普遍对 Google 不断推出新模型名称感到疲劳，并质疑命名方案能否统一。有人认为即使基准测试领先，Gemini 在实际对话中仍不如 Opus 5.5 自然，也有人对 Neon 的定位及其与 Carbon 的速度差异表示困惑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">Introducing Gemini 4 Neon</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-4-neon/">Gemini 4 Neon - Model Card — Google DeepMind</a></li>
<li><a href="https://www.neowin.net/news/google-launches-gemini-4-neon-claims-its-three-times-faster-than-carbon/">Google launches Gemini 4 Neon , claims it&#x27;s three times... - Neowin</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#large language models`, `#Google`, `#software engineering`

---

<a id="item-tech-news-3"></a>
### [微软 Ignite 2026 发布七款高性价比新模型](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

在 2026 年 Microsoft Ignite 大会上，微软发布了七款新模型，重点强调可扩展的性价比。其中，社区测试报告称 MAI Code 2 代码模型的表现与 Anthropic Opus 或 OpenAI Sol 相当。这一发布正值 Anthropic IPO 讨论和多家公司推出高竞争力模型的背景下，显示出 AI 模型价格与性能竞争加剧。微软此次未在现有信息中明确这些模型是否开放权重或提供开源版本。

hackernews · gmays · 11月18日 16:08 · [社区讨论](https://news.ycombinator.com/item?id=50548021)

**「背景」** 微软的 MAI 模型是其自研的第一方模型系列，此前已用于 GitHub Copilot 等产品；Ignite 是微软面向企业 IT 和开发者的年度大会，2026 年发布的七款模型覆盖编码、推理等场景，并配套 Maia 200 加速器及模型权重授权计划。为理解“价格性能比”，相关公告将 MAI Code 2 与 GPT-6.1 Sol 等外部模型对比：在四项日常编码基准上，MAI Code 2 以约 40% 成本达到后者 98% 性能；MAI Code 2 Flash 则在三项高频编码基准上以 65% 和 20% 的成本达到 GPT-6 Luna 和 Claude Haiku 5.5 的相当性能。

**「影响」** 对于需要高质量代码生成的企业与开发者，MAI Code 2 以显著更低的成本提供接近 OpenAI、Anthropic 领先模型的编程性能，可能降低日常编码和企业代码助手的使用支出。

**「社区讨论」** 社区对 MAI Code 2 的代码质量有正面评价，认为可与 Opus 或 Sol 相比；但多位评论者对微软的市场策略、开源态度和领导力表示怀疑，认为若不开放权重可能重蹈 Windows Phone 覆辙，且有人认为 Ignite 主题演讲缺乏创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026/">Seven new world-class models at scalable price-performance ...</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at scalable ...</a></li>
<li><a href="https://www.linkedin.com/pulse/microsoft-ignite-2026-seven-new-mai-models-chip-your-own-ivana-tilca-hxyef">Microsoft Ignite 2026: Seven New MAI Models, a New Chip, and ...</a></li>
<li><a href="https://mobidevices.com/en/microsoft-mai-code-2">Microsoft releases MAI Code 2 AI model | MobiDevices.com</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at... | Microsoft AI</a></li>

</ul>
</details>

**标签**: `#ai`, `#microsoft`, `#llm`, `#machine-learning`, `#cloud`

---

<a id="item-tech-news-4"></a>
### [DNS 解析器不应成为反盗版战场](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 因法国要求 DNS 解析服务屏蔽盗版网站而宣布退出法国市场。这一决定凸显了围绕 DNS 解析器是否应承担版权执法职能的争议。支持者可能认为 DNS 屏蔽是有效手段，但批评者担心其容易被滥用为审查工具，且无法解决盗版根源。该事件反映了网络基础设施中立性与版权保护之间的紧张关系。

hackernews · ritzaco · 11月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50545958)

**「背景：Quad9 与法国法院的 DNS 封锁之争」** Quad9 是由瑞士非营利基金会运营的免费公共 DNS 解析服务，提供安全过滤并承诺保护用户隐私。2026 年，法国法院因版权侵权指控下令 Quad9 屏蔽涉嫌传播盗版体育直播的域名，并对其未执行屏蔽处以每日罚款。Quad9 认为 DNS 层级封锁超出其职责且可能滥用，宣布自 2026 年 11 月 24 日起停止在法国提供服务。

**「影响」** 法国用户将无法继续使用 Quad9 的 DNS 解析服务，且欧洲其他解析器运营商可能被要求实施类似的基于 DNS 的盗版拦截；Google 已向欧盟表示此类拦截无效并会造成重大附带损害。

**「社区讨论」** 社区讨论中，有评论认为除起诉盗版者外的反盗版手段都是变相压制言论，而改善付费体验（如低价格、无 DRM）才是根本。另有评论质疑应归咎于法院还是立法者，并指出 AI 公司已大量使用 IP，针对个人盗版的意义存疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/10/french-courts-site-blocking-orders-drive-quad9-out-france">French Court’s Site-Blocking Orders Drive Quad9 Out Of France</a></li>
<li><a href="https://digitalmedusa.org/wp-content/uploads/2025/04/DNS-Resolvers-2025-Final.pdf">DNS - Resolvers -2025-Final</a></li>
<li><a href="https://ipspeed.info/infofeed/news/google-tells-brussels-that-blocking-dns-resolvers-and-vpns-to-fight-piracy-does-more-harm-than-good">Google Tells Brussels That Blocking DNS Resolvers and VPNs to...</a></li>

</ul>
</details>

**标签**: `#dns`, `#internet-censorship`, `#copyright`, `#network-policy`, `#piracy`

---

<a id="item-tech-news-5"></a>
### [OpenAI 模型推进芯片设计](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

OpenAI 报告称其正在使用自家 AI 模型推进芯片设计，但本次来源未提供具体技术细节。该消息引发关于 AI 驱动 EDA 和开源硬件实践的讨论。社区评论指出，部分公司可能保留模型并与其客户形成竞争，同时质疑相关 RISC-V 设计是否会被公开。另有工程师分享经验，将芯片设计视为软件设计问题，用 agent 生成电路并自动化 EDA 流程，其中 RTL 仅占一小部分、大部分为模拟电路。

hackernews · vighneshiyer · 11月18日 17:45 · [社区讨论](https://news.ycombinator.com/item?id=50549493)

**「背景」** OpenAI 表示已使用其前沿模型加速首款定制推理芯片 Jalapeño 的开发；该芯片面向大语言模型推理，并针对 OpenAI 的实际模型形状与推理服务模式进行协同优化。根据 IEEE Spectrum 与相关分析，Jalapeño 部署在包含 2,048 颗芯片的 pod 中，工程师采用 AI 辅助工作流改进设计，且模型能力提升带来了意外的设计优化。

**「社区讨论」** 社区讨论中，有评论担忧 AI 公司保留模型并与客户竞争，认为低垂果实已被摘完；也有工程师分享用 agent 生成电路和自动化 EDA 流程的积极体验，并追问是否公开 RISC-V 设计。另有评论称相同改进循环将扩展到所有科学领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/advancing-chip-design-with-our-models/">Advancing chip design with OpenAI models | OpenAI</a></li>
<li><a href="https://spectrum.ieee.org/llms-for-chip-design">Jalapeño Shows Power of LLMs for Chip Design - IEEE Spectrum</a></li>
<li><a href="https://www.explainx.ai/blog/openai-jalapeno-chip-llm-inference-broadcom-2026">OpenAI Jalapeño: 1.9× Perf/W vs Blackwell (Aug 2026) | explainx.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#chip design`, `#OpenAI`, `#RISC-V`, `#EDA`

---

<a id="item-tech-news-6"></a>
### [Genie 4 已向符合条件的 Google AI Ultra 订阅者开放](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 7.0/10

Google DeepMind 官方宣布，生成式世界模型 Genie 4 现已上线，并向“符合条件的 Google AI Ultra 订阅者”开放。该模型属于生成式世界模型，可能用于游戏开发、AI 研究等场景。官方公告未披露具体功能、性能指标或区域资格限制的完整细节。

hackernews · leumon · 11月18日 18:49 · [社区讨论](https://news.ycombinator.com/item?id=50550415)

**「背景」** 世界模型（world model）是一种能根据用户输入生成可交互模拟环境的生成式模型；Project Genie 是 Google DeepMind 用于体验这类模型的产品入口。Genie 4 是该系列的最新版本，相较此前版本新增实时音频、对话与 Gemini 辅助规划，可直接生成可编辑的交互式世界。官方宣布 Genie 4 已开始在 Project Genie 中向符合条件的 Google AI Ultra 订阅者开放，但 Datastudios 的报道提到 Gemini API 早期访问仍显示“即将推出”，具体日期和规格尚未公布。

**「影响」** 符合条件的 Google AI Ultra 订阅者现可使用 Genie 4，但社区报告显示 Workspace 账号和英国等地区用户可能因未明确的资格限制而无法访问。

**「社区讨论」** 社区讨论集中于资格、定价与伦理风险：部分用户反映 Workspace 账号或英国地区无法使用，也有人担忧生成式 AI 的负面影响，同时有人赞赏 DeepMind 的探索并讨论其未来成为游戏引擎的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/">Project Genie update featuring Genie 4</a></li>
<li><a href="https://deepmind.google/models/genie/">Genie 4 — Google DeepMind</a></li>
<li><a href="https://www.datastudios.org/post/google-deepmind-genie-4-real-time-world-model-native-audio-research-preview">Genie 4 : Google DeepMind &#x27;s real-time world model with native audio...</a></li>

</ul>
</details>

**标签**: `#generative-ai`, `#world-models`, `#deepmind`, `#game-development`, `#ai-research`

---

<a id="item-tech-news-7"></a>
### [旅行者 1 号交互拆解：从核电池到单个存储位](https://rshekhar.com/voyager/) ⭐️ 7.0/10

旅行者 1 号今天距地球达到一光日。开发者 raj-shekhar 发布了一个交互式网页体验，用户可以查看两艘旅行者号的实时位置，打开核电池看到其 24 个钚球，进入数据计算机直到单个存储芯片，并了解金唱片封面如何说明其播放方式。该站点还展示了旅行者 1 号如何通过无线电被修复，以及当前正在接收它们信号的地球天线。作者另制作了一部 4 分钟短片。这一深度交互可视化对硬件与计算机系统爱好者具有较高教育价值。

hackernews · raj-shekhar · 11月18日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=50548161)

**「背景」** 旅行者 1 号是 NASA 于 1977 年发射的深空探测器，现已进入星际空间，是离地球最远的人造物体。一个光日是指光在 24 小时内传播的距离，约等于 260 亿公里或 160 亿英里；旅行者 1 号于 2026 年 11 月 18 日达到这一里程碑。该探测器的硬件（如核电池、计算机内存和黄金唱片）均来自上世纪 70 年代的设计，对理解其长期运行和故障有工程价值。

**「社区讨论」** 社区普遍称赞该可视化，但有人指出内容仍有缺失；另有人追问存储芯片故障的具体物理机制，并质疑该项目是否由 AI 生成（vibecoded）以及是否经过权威来源核对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/">Voyager 1: What Is a Light-Day - NASA Science</a></li>

</ul>
</details>

**标签**: `#spacecraft`, `#hardware`, `#visualization`, `#computer-history`, `#embedded-systems`

---

<a id="item-tech-news-8"></a>
### [Daniel Stenberg 对比 AI 生成的 Rust 重写与 curl 实际维护](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

curl 维护者 Daniel Stenberg 对比了 AI 生成的 Rust 重写与真实 curl 项目的维护工作。在一次超过三周的时间段内，编码代理将 185,000 行 C 代码转换成了 340,000 行 Rust 代码，而实际的 curl 项目合并了 300 多个提交，其中包括略多于 200 个错误修复，这些修复在那些 Rust 重写中都没有。真实的 curl 项目同期还修复了若干安全漏洞，Stenberg 预计下个月还会有另外 200 个错误修复以及可能更多的漏洞修复。他质疑这些重写版本能否跟上真正 curl 的持续维护和安全工作。

rss · Simon Willison · 11月18日 15:58

**「背景」** curl 与 libcurl 是 Daniel Stenberg 维护的开源网络传输项目；2026 年秋季出现了多个由 AI 编程代理生成的 Rust 版本，包括几个月前声称从零实现的内存安全重写 urlx，以及 11 月一个同名的 Rust 重写。Daniel Stenberg 在 2026 年 11 月 17 日的博客中，将这些自动生成的 Rust 重写与真实 curl 项目持续合并的提交、bug 修复和漏洞修复进行对比，Simon Willison 随后引用了其中的关键结论。

**「影响」** AI 生成的 Rust 移植版 curl 可能缺少官方 C 项目持续合并的快速错误修复和漏洞补丁，依赖实验性 Rust 克隆的用户可能面临未修补的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/">Actual curl rewrites in rust - daniel.haxx.se</a></li>
<li><a href="https://explainx.ai/blog/daniel-stenberg-curl-rust-agent-rewrites-vs-maintenance-november-2026">Daniel Stenberg: Agentic Rust curl Rewrites Cannot Keep Up ...</a></li>
<li><a href="https://letsdatascience.com/news/curl-maintainer-daniel-stenberg-answers-ai-built-rust-rewrit-53834580">Curl maintainer Daniel Stenberg answers AI-built Rust ...</a></li>

</ul>
</details>

**标签**: `#rust`, `#curl`, `#ai-code-generation`, `#security`, `#open-source`

---

<a id="item-tech-news-9"></a>
### [微信小微测试范围扩大，日活达 3000 万](https://mp.weixin.qq.com/s/r3NthxJZQJgztyLADwNV4A) ⭐️ 7.0/10

腾讯在 2026 年第三季度财报中宣布，微信小微 AI 助手测试范围扩大，日活跃用户数达到 3000 万，并逐步融入微信聊天、朋友圈、公众号和视频号等核心场景。小微采用针对成本效率优化的 WeLM 定制模型，腾讯称其推理成本低且持续下降。未来部分推理任务预计将在用户设备端运行，标志着大规模 AI 能力在微信平台落地。

telegram · zaihuapd · 11月18日 11:35

**「背景」** 微信是腾讯旗下的即时通讯与内容平台，小微是其内置的 AI 助手，此前主要提供语音交互等服务。WeLM 是腾讯针对成本效率优化的定制语言模型；在用户设备端运行部分推理任务，可减少云端算力消耗并降低响应延迟。

**「影响」** 微信用户将能在聊天、朋友圈、公众号和视频号等场景使用小微 AI 助手。

**标签**: `#WeChat`, `#Tencent`, `#AI assistant`, `#on-device inference`, `#WeLM`

---

<a id="item-tech-news-10"></a>
### [DeepSeek 服务端搜索与网页抓取改为免费](https://www.ithome.com/1/029/058.htm) ⭐️ 7.0/10

DeepSeek 宣布，自北京时间 2026 年 11 月 18 日 12:00 起，调用模型时触发的服务端搜索和网页抓取将不再单独计费，仅按模型 Token 用量收费。此项变更适用于联网工具、Anthropic API 的 web\_search 工具以及 Responses API 的 web\_search 工具所触发的服务。此前 Search 和 Fetch API 按请求次数收费，每 1,000 次成功请求 5 元。这一调整降低了开发者在检索增强生成和工具调用场景中通过 API 使用这些服务的成本。

telegram · zaihuapd · 11月18日 13:44

**「背景」** DeepSeek 此前已上线 Search 和 Fetch API，并按成功请求次数单独计费。服务端搜索和网页抓取可以在调用模型时由联网工具或 web\_search 工具自动触发。此次变更仅取消这些触发场景的单独计费，模型 Token 用量仍按原有方式收费。

**「影响」** 从 2026 年 11 月 18 日 12:00（北京时间）起，使用 DeepSeek API 并触发服务端搜索或网页抓取的开发者将不再支付每 1,000 次成功请求 5 元的单独费用，只需为模型 Token 用量付费。

**标签**: `#DeepSeek`, `#API pricing`, `#web search`, `#large language models`, `#software engineering`

---

<a id="item-tech-news-11"></a>
### [美政府考虑要求企业披露使用中国 AI](https://www.reuters.com/world/china/trump-administration-weighs-forcing-us-firms-disclose-chinese-ai-use-2026-11-18/) ⭐️ 7.0/10

特朗普政府正考虑要求美国企业公开披露其使用中国 AI 模型的情况，财政部与白宫科技政策办公室已讨论该方案。Airbnb 使用阿里 Qwen 支撑客服，若方案落地，此类企业须在官网公示。此举意在通过“公开点名”抑制企业对便宜的中国开放权重模型的依赖，而非出台新限制。目前方案是否获政府内部支持、会否进入正式立法程序尚不明朗。

telegram · zaihuapd · 11月19日 02:30

**「背景」** 中国开放权重模型如阿里 Qwen 因成本较低，被部分美国企业用于客服等场景。美国此前对 AI 供应链安全的审查多集中在投资和出口管制，尚未形成普遍强制披露模型来源的制度。特朗普政府此次讨论的“公开点名”策略试图通过透明压力替代新限制。

**标签**: `#AI policy`, `#US regulation`, `#China AI`, `#open-weight models`, `#technology industry`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美联储会议纪要：官员预计将继续加息并担忧 AI 通胀风险](https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html) ⭐️ 8.0/10

美联储 10 月会议纪要显示，官员普遍认为需要进一步加息以遏制通胀，并担心人工智能相关需求是“通胀风险的重要来源”；会议以 10 票赞成、2 票反对决定将联邦基金利率目标区间维持在 3.75%-4%。

rss · CNBC Finance · 11月18日 19:41

**「背景」** 会议纪要公布前，10 月消费者价格指数（CPI）环比上涨 0.4%，核心 CPI 环比上涨 0.3%，均比预期高 0.1 个百分点；官员仍预计通胀将在 2027 年及以后大幅回落。

**「影响」** 市场已完全计入 12 月加息 25 个基点的预期，若实现，持有浮动利率债务的家庭和企业将面临更高还款压力。

**标签**: `#Federal Reserve`, `#interest rates`, `#inflation`, `#monetary policy`, `#AI`

---

<a id="item-finance-news-2"></a>
### [美联储理事沃勒：12 月或需加息 50 个基点以“震撼”抗通胀](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 8.0/10

美联储理事沃勒周三表示，由于通胀高于预期，12 月 8-9 日会议可能需要加息 50 个基点，并称应逆转去年三次 25 个基点的降息、且可能还需更多加息。据 CNBC 报道，期货市场目前完全定价的 12 月加息幅度为 25 个基点。

rss · CNBC Finance · 11月18日 15:13

**「背景」** 美联储在 2025 年曾三次降息以应对劳动力市场担忧，但今年 2 月底美国和以色列打击伊朗后能源价格飙升、关税影响持续，使多数通胀指标高于 3%。

**标签**: `#Federal Reserve`, `#monetary policy`, `#interest rates`, `#inflation`, `#Christopher Waller`

---

<a id="item-finance-news-3"></a>
### [APEC 深圳峰会：特朗普、习近平与普京将举行首次三方会晤](https://www.cnbc.com/2026/11/18/apec-trump-xi-putin-shenzhen.html) ⭐️ 7.0/10

亚太经合组织（APEC）领导人会议在深圳举行，美国总统特朗普、中国国家主席习近平与俄罗斯总统普京将举行首次三方会晤。美中官员称，会谈将聚焦落实今年 9 月宣布的互降 300 亿美元商品关税的贸易协议（未说明生效日期），但各方对取得突破的预期很低。

rss · CNBC Finance · 11月18日 06:04

**「背景」** 去年的 APEC 峰会促成了为期一年的美中贸易休战（降低关税并恢复部分稀土流动），此后延长两个月至 2027 年 1 月；与此同时，华盛顿正收紧对华人工智能技术出口限制并审查英伟达对华芯片销售。

**标签**: `#US-China trade`, `#APEC summit`, `#technology policy`, `#energy markets`, `#geopolitics`

---

<a id="item-finance-news-4"></a>
### [腾讯公布三季报：AI 资本开支 814 亿元远超预估，自由现金流转负](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 7.0/10

腾讯公布 2026 年第三季度财报：营收 2073 亿元，同比增长 8%，低于市场预期；归母净利润 636 亿元，同比增长 0.8%。资本开支 814.33 亿元，远超市场预估的 554 亿元；单季自由现金流为-691 亿元；公司称 WorkBuddy 日均 Token 消耗量超过 100 万亿，为国内大模型产品最高。

telegram · zaihuapd · 11月18日 09:20

**「背景」** 在 2026 年第三季度之前，腾讯第二季度营收为 2047.9 亿元、同比增长 11%；WorkBuddy 是腾讯云代码助手推出的 AI Agent 办公工具，用于自主规划并交付多模态复杂任务。

**「影响」** 腾讯自由现金流为负且资本开支远超预期，将直接影响投资者对其盈利质量和 AI 投入回报的评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办公新范式</a></li>
<li><a href="https://post.smzdm.com/p/axkzngg3/">放弃 元 宝押注 WorkBuddy ， 腾 讯 AI这场转型算成功吗_IT... | 什么值得买</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#earnings`, `#AI capex`, `#free cash flow`, `#WorkBuddy`

---

<a id="item-finance-news-5"></a>
### [中韩宣布自贸协定服务投资后续谈判实质性结束](https://x.com/Jaemyung_Lee/status/2122988472994791476) ⭐️ 7.0/10

11 月 18 日，中韩宣布自贸协定服务与投资后续谈判实质性结束；中国承诺在电影、游戏等领域给予韩国最惠国待遇（不低于给其他国家的待遇），并扩大旅游、法律、建筑、金融等领域开放。谈判自 2018 年 3 月启动，历时 8 年 8 个月；部分技术事项仍将由工作层面协商完成。

telegram · zaihuapd · 11月18日 10:02

**「背景」** 中韩自贸协定服务与投资后续谈判自 2018 年 3 月启动，历时 8 年 8 个月；宣布实质性结束的当天，习近平在深圳会见了来华出席亚太经合组织领导人非正式会议的韩国总统李在明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/yaowen/liebiao/202611/content_7086520.htm">习近平会见 韩 国总统李在明__ 中 国政府网</a></li>

</ul>
</details>

**标签**: `#China-South Korea FTA`, `#services trade`, `#investment liberalization`, `#trade policy`, `#bilateral relations`

---