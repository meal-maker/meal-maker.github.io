---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 36 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [智谱和月之暗面旗舰模型发布或延期](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 让自托管重新变得有趣](#item-tech-news-2) ⭐️ 7.0/10
3. [AMD gfx906 专用 llama.cpp 分支](#item-tech-news-3) ⭐️ 7.0/10
4. [RansomwareHelp CTO 因电信欺诈被起诉](#item-tech-news-4) ⭐️ 7.0/10
5. [谷歌将让 AI 代理使用其 MCP 服务器，但 Gmail 集成无法发送邮件](#item-tech-news-5) ⭐️ 7.0/10
6. [sqlite3\_rsync：免本地副本的 SQLite 远程复制工具](#item-tech-news-6) ⭐️ 7.0/10
7. [Neuralink 脑机接口获 FDA 批准启动渐冻症关键试验](#item-tech-news-7) ⭐️ 7.0/10
8. [阿斯麦 CEO：全面断供中国只会逼中国自己造](#item-tech-news-8) ⭐️ 7.0/10
9. [Cloudflare 控制台与 API 故障已持续半小时](#item-tech-news-9) ⭐️ 7.0/10
10. [微软 CEO 承认应届生招聘放缓：AI 预算优先于招人](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [英伟达暂停向东南亚四国发运 AI 服务器](#item-finance-news-1) ⭐️ 9.0/10
2. [荷兰反对美国限制 ASML 对华销售法案](#item-finance-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [智谱和月之暗面旗舰模型发布或延期](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 8.0/10

路透社报道，智谱原计划本月发布约 3 万亿参数的旗舰模型 GLM-5.5 但尚未推出，知情人士称受反蒸馏防护措施日趋有效等因素影响，其发布可能推迟至 2027 年第一季度或更晚。月之暗面内部预计，若完全失去海外算力，重大版本发布间隔将从 6 个月拉长到一年以上，下一代旗舰 Kimi K4 或推迟至 2027 年年中。推迟原因还包括 Anthropic 与 OpenAI 的反蒸馏措施提高了训练数据获取难度，月之暗面已转而蒸馏谷歌和 Meta 的模型。网传朋友圈截图显示智谱方面对相关报道表示否认。

telegram · zaihuapd · 11月26日 15:14

**「背景」** 反蒸馏措施指美国 AI 实验室为防止其他开发者利用自己模型输出训练竞品而加入的技术防护。美国对华出口管制限制了先进 AI 芯片和算力的获取。智谱和月之暗面是中国头部大模型公司，GLM 和 Kimi 分别是其旗舰模型系列。

**「影响」** 若延期属实，依赖 GLM-5.5 和 Kimi K4 的企业用户和开发者可能至少到 2027 年仍需使用现有版本，并需评估海外算力受限和反蒸馏措施带来的能力更新放缓风险。但智谱已否认报道，延期尚未得到官方确认。

**标签**: `#AI`, `#large language models`, `#compute restrictions`, `#China tech`, `#anti-distillation`

---

<a id="item-tech-news-2"></a>
### [AI 让自托管重新变得有趣](https://janlukas.blog/posts/ai-self-hosting) ⭐️ 7.0/10

博客文章《AI made self-hosting fun again》及其 Hacker News 讨论指出，AI 工具显著降低了自托管的门槛。多位评论者分享了具体实践：一名用户用 Claude Code 管理近 60 个 Docker 服务，涵盖备份、家庭自动化和云 API 集成；另一名用户在 k3s 和 Tailscale 上让 AI 代理直接部署到家服务器。文章作者提醒，当实现想法变得太容易时，应追问是否值得实现。同时，评论也强调更便捷的创建意味着后续安全维护责任加重，例如需要在严重 CVE 发布后 24 小时内打补丁。

hackernews · jlelse · 11月26日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50660180)

**「背景」** 自托管指用户在自己的服务器或家庭硬件上运行自主管理的软件服务，常涉及 Docker、NixOS、k3s 等工具，启动成本较高但配置好后稳定高效。AI 编程和命令行代理（如 Claude Code CLI）可帮助用户生成配置、部署服务、编写自动化脚本，从而降低这类复杂技术栈的上手门槛。此外，一些在线目录（如 Self-Hosted Apps）提供自托管应用浏览和发现，辅助用户挑选适合自己环境的服务。

**「影响」** 对于采用 AI 辅助自托管的用户，这意味着他们可以更快上线更多服务，但必须建立更严格的安全补丁响应流程，不能只依赖以往的 fail2ban 和每隔几个月更新系统。

**「社区讨论」** 讨论中既有对 AI 代理带来的“vibe 部署”和效率提升的认可，也有对安全补丁加速和自动化可能引入风险的担忧；没有出现明确的一致反对，更多是分享个人权衡与经验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50660180">AI made self - hosting fun again | Hacker News</a></li>
<li><a href="https://selfh.st/apps/">Self - Hosted Software and Apps</a></li>
<li><a href="https://blog.fnxexp.dev/tech-131/">Self - Hosting Made Easy: Fun CLI Agents for Home... - blog .fnxexp.dev</a></li>

</ul>
</details>

**标签**: `#AI`, `#self-hosting`, `#DevOps`, `#LLM`, `#security`

---

<a id="item-tech-news-3"></a>
### [AMD gfx906 专用 llama.cpp 分支](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

2025 年初，社区发现 AMD 2018 年左右的 gfx906 数据中心显卡虽然计算能力一般，但 HBM2 显存带宽高达 1 TB/s，32GB 显存二手价约 200 美元，于是催生了针对这些无张量核心、无原生 bf16 支持的特殊硬件的 llama.cpp 优化分支。该分支让低成本老卡可以高吞吐运行本地 LLM，例如在单张卡上用 4-bit 智能量化的 Qwen3.8-27b 模型（KLD 0.006、top-1 0.972）实现 2400 tok/s 预填充和 150 tok/s 解码，并可承载 3 路 200k 上下文的 agent 并发任务。还有用户在 MI100 上通过积极优化 AMD 代码并将 Nvidia 内核移植到 ROCm，使 Qwen3.8 性能提高两到三倍。这些分支共同构成了围绕 gfx906 等老卡的小型生态，为本地 AI 实践者提供了低成本的推理方案。

hackernews · julianlam · 11月26日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=50657265)

**「背景」** llama.cpp 是常用的本地大语言模型推理框架，而 AMD 的 gfx906 架构（包括 MI50、MI60、Radeon VII 等 2018 年前后发布的 GPU）虽然缺少张量核心和原生 bf16 支持，但凭借 HBM2 显存提供了很高的内存带宽。该 fork 针对这一架构做优化，以在单卡上最大化 prompt 处理与推理速度；它并不是完整独立分支，而是对固定版本的 llama.cpp 打上一组最小改动，并持续将其重放到较新版本上。ROCm 官方稳定版不完全支持 gfx906，但 nightly 版本已提供支持，已有用户在 MI25 等卡上运行编译后的 llama.cpp。

**「对低成本 AMD gfx906 本地推理用户的影响」** 对于使用 AMD gfx906（MI50/MI60/Vega VII）等低成本 HBM2 显卡的用户，该优化 fork 通过定制 kernel、Flash Attention 和 Q8/MXFP4 等低比特路径实现显著吞吐提升，社区基准也显示其可作为可行的本地大模型推理方案；不过部分性能数据来自个体测试，实际效果仍取决于具体模型、量化方式和驱动版本。

**「社区讨论」** 社区普遍认可 gfx906 老卡凭借 HBM2 高带宽带来的性价比，并分享实际性能：radiance 引擎在 r9700 上达到 2400 tok/s 预填充和 150 tok/s 解码；MI100 用户通过 ROCm 内核移植获得两到三倍提升。有用户持续使用一个月处理 agentic 和编码任务，运行稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50657265">AMD - specific fork of llama . cpp | Hacker News</a></li>
<li><a href="https://github.com/thickprogrammer/llama.cpp-gfx906">thickprogrammer/ llama . cpp - gfx 906 : llama . cpp optimized for AMD ...</a></li>
<li><a href="https://devnull.land/amd-specific-llama-cpp">AMD - specific fork of llama . cpp | devnull.land</a></li>
<li><a href="https://www.youtube.com/watch?v=h6bK1-EX42A">AMD MI 50 32GB for Local AI: Qwen 3.6 &amp; Gemma 4 on llama . cpp ...</a></li>
<li><a href="https://github.com/thickprogrammer/llama.cpp-gfx906">GitHub - thickprogrammer/ llama . cpp - gfx 906 : llama . cpp optimized for...</a></li>
<li><a href="https://forum.level1techs.com/t/glm-and-i-created-a-llama-cpp-fork-optimized-for-amd-gfx906-mi50-mi60-radeon-vii-gcn-hip/254257">GLM and I created a llama . cpp fork optimized for AMD GFX 906 ( Mi 50 ...)</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AMD GPU`, `#HBM2`, `#inference optimization`, `#open source`

---

<a id="item-tech-news-4"></a>
### [RansomwareHelp CTO 因电信欺诈被起诉](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/) ⭐️ 7.0/10

安全公司 RansomwareHelp 的首席技术官因涉嫌在勒索软件赎金事件中误导受害者而面临电信欺诈指控。此次指控涉及该公司向受害者传达的赎金支付相关信息与实际行为之间可能存在的差异。该案由 Krebs on Security 报道，凸显了网络事件响应和赎金谈判中的法律风险。目前没有更多公开的起诉细节或判决结果。

hackernews · Bender · 11月26日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50657645)

**「背景」** 勒索软件事件响应公司通常会帮助受害者与攻击者谈判并恢复数据；部分公司公开承诺“不推广、不中介、不代付赎金”，但内部流程可能并非如此。本案涉及的电汇欺诈（wire fraud）是美国联邦罪名，指利用跨州电汇等通信手段实施骗取钱财或财产的欺诈计划。根据 Krebs on Security 的报道，RansomwareHelp 的 CTO 因被控在赎金谈判中误导受害者而遭起诉，这使公众关注事件响应行业在赎金支付声明与实际操作之间的差异。

**「社区讨论」** 社区讨论对是否构成电信欺诈存在分歧：有观点认为客户最终取回数据且支付了可接受的价格，因此未必存在欺诈故意；另一些人则强调公司公开宣称“绝不支付赎金”与实际支付行为之间的矛盾。还有人建议在合同中写入“必要时可支付赎金”的应急条款以降低法律风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/">CTO of ‘ RansomwareHelp ’ Indicted for Wire Fraud – Krebs on...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#ransomware`, `#wire-fraud`, `#legal`, `#incident-response`

---

<a id="item-tech-news-5"></a>
### [谷歌将让 AI 代理使用其 MCP 服务器，但 Gmail 集成无法发送邮件](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 7.0/10

谷歌据报道将让其 Workspace MCP 服务器供 AI 代理使用，但 Gmail 集成无法发送邮件。MCP（模型上下文协议）是一种让 AI 模型与外部工具交互的开放协议。该限制引发关于安全性与商业决策的讨论，以及实际绕过方案。社区评论指出，MCP 已有 elicitation 机制可暂停工具调用并要求用户确认，因此该限制可能更多出于商业考量。也有人提到通过浏览器自动化或 SMTP/IMAP 的替代方案。

hackernews · ritzaco · 11月26日 09:44 · [社区讨论](https://news.ycombinator.com/item?id=50653477)

**「背景」** MCP（Model Context Protocol）是一种让 AI 代理以标准化方式调用外部工具和数据的协议。Google 为 Gmail 等 Workspace 服务提供官方 MCP 服务器，可供代理读取邮件、创建草稿和添加标签，但官方发布的操作列表中不包含发送邮件功能。评论者指出，MCP 本身已有 elicitation 机制可以在执行前请求用户确认，因此限制发送邮件更像商业决策而非纯安全考量。

**「影响」** 对于希望使用 Gmail MCP 服务器发送邮件的 AI 代理开发者，此限制可能迫使他们采用浏览器自动化或 SMTP/IMAP 等替代方案，增加复杂性并可能违反服务条款。

**「社区讨论」** 社区普遍认为该限制更多是商业决策而非安全必需，因为 MCP 已有 elicitation 机制。也有开发者表示将使用浏览器自动化或 SMTP/IMAP 绕过限制，并担忧官方 API 计费模式和账户封禁风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server">Configure the Gmail MCP server | Google for Developers</a></li>
<li><a href="https://commandmail.app/en/guides/gmail-mcp-server">Gmail MCP server : official Google preview, open... | Command Mail</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#Google Workspace`, `#Gmail`, `#API access`

---

<a id="item-tech-news-6"></a>
### [sqlite3\_rsync：免本地副本的 SQLite 远程复制工具](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 7.0/10

sqlite3\_rsync 是 SQLite 自 3.47.0（2024 年 10 月，实验性）起提供、并在 3.50.0（2025 年 5 月）增强的数据库远程复制工具。它可通过 SSH 将数据库快照复制到另一台机器，而无需先在本机创建完整副本；这避免了 backup API 或 VACUUM INTO 需要足够磁盘空间创建重复副本的限制，对磁盘使用过半的小实例尤其有用。该工具还支持增量同步现有副本，类似 rsync：副本端发送页哈希，源端仅回传有差异的页内容；若两端差异极大，总网络带宽可能超过整个数据库大小，但超出部分通常只有几个百分点。作者指出自己早在 2024 年 10 月就写过该工具的应用。

rss · Simon Willison · 11月26日 06:08

**「背景」** SQLite 数据库通常是单个文件，常见快照方式 backup API 或 VACUUM INTO 需要在本机生成一份完整副本，因此消耗额外磁盘空间。sqlite3\_rsync 基于类似 rsync 的哈希比对协议，通过 SSH 在源端和副本端之间只传输差异页，降低网络传输量。

**「影响」** 对于磁盘空间不足、无法使用 backup API 或 VACUUM INTO 创建本地副本的 SQLite 用户，sqlite3\_rsync 提供了一种通过 SSH 远程复制快照或增量同步的可行替代方案。

**标签**: `#SQLite`, `#database`, `#remote-copy`, `#sysadmin`, `#software-engineering`

---

<a id="item-tech-news-7"></a>
### [Neuralink 脑机接口获 FDA 批准启动渐冻症关键试验](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 7.0/10

Neuralink 宣布获得美国 FDA 批准，将启动名为“LINK”的植入式脑机接口关键临床试验，面向渐冻症（ALS）患者招募，旨在将大脑信号直接转化为计算机控制指令，这也是美国首个获批的此类关键试验。此前，Neuralink 通过早期研究已在全球为超过 30 名瘫痪患者植入设备。此次进入关键临床阶段标志着其技术正从安全验证加速迈向商业化上市审批，相关数据将作为未来申请医疗器械上市许可的核心依据。

telegram · zaihuapd · 11月26日 07:15

**「背景」** Neuralink 是一家美国神经科技公司，由埃隆·马斯克与八名科学家和工程师共同创立，自 2016 年启动，开发可植入式脑机接口（BCI），用于将大脑信号转化为设备控制指令。关键试验（pivotal trial）指为支持医疗器械上市审批而设计的关键性临床研究；此前获批的早期研究已用于验证设备安全性，而 LINK 关键研究针对渐冻症（ALS）导致的严重瘫痪患者，测试植入式 BCI 的疗效与安全性。

**「影响」** 渐冻症患者将有机会通过美国首个获批的植入式脑机接口关键试验“LINK”接受治疗，Neuralink 也可凭借该试验数据向 FDA 申请医疗器械上市许可，推动其技术从安全验证走向商业化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuralink">Neuralink - Wikipedia</a></li>
<li><a href="https://interestingengineering.com/health/neuralink-fda-approval-link-pivotal-brain-implant-trial">Neuralink gets FDA approval for first pivotal brain implant trial</a></li>
<li><a href="https://neuralink.com/updates/neuralink-receives-fda-approval-to-launch-link-pivotal-study/">Neuralink Receives FDA Approval to Launch LINK Pivotal Study</a></li>
<li><a href="https://interestingengineering.com/health/neuralink-fda-approval-link-pivotal-brain-implant-trial">Neuralink gets FDA approval for first pivotal brain implant trial</a></li>

</ul>
</details>

**标签**: `#Neuralink`, `#brain-computer interface`, `#FDA approval`, `#clinical trial`, `#ALS`

---

<a id="item-tech-news-8"></a>
### [阿斯麦 CEO：全面断供中国只会逼中国自己造](https://www.semafor.com/article/11/25/2026/asml-makes-the-case-for-selling-chips-to-china) ⭐️ 7.0/10

阿斯麦 CEO 富凯在 Semafor《Future Proof》节目中表示，出口管制应保护最先进技术，但不能把中国完全排除在外，否则将促使中国在自研上“加倍甚至三倍投入”。他称阿斯麦卖给中国的设备落后最先进制程十多年，维持这道代差反而让中国继续依赖西方设备；过去近 30 年阿斯麦在中国光刻机市场的份额接近 100%，中国已接受这种技术依赖。美国正在推动 MATCH 法案，拟将管制范围从 EUV 扩大到浸没式 DUV 和维护服务，荷兰政府和阿斯麦均表示反对。

telegram · zaihuapd · 11月26日 12:19

**「背景」** 光刻机是芯片制造的核心设备，EUV 光刻用于最先进制程，浸没式 DUV 常用于成熟及次先进制程。美国此前已限制 EUV 对华出口，MATCH 法案则寻求进一步限制浸没式 DUV 和维护服务。阿斯麦是极紫外和深紫外光刻设备的主要供应商，因此其表态涉及出口管制对全球产业链的影响。

**「影响」** 若 MATCH 法案通过，中国芯片制造商可能无法继续获得浸没式 DUV 光刻机和相关维护服务，进而影响成熟及次先进制程的扩产与运行；而阿斯麦判断这将迫使中国加大自研光刻机投入。

**标签**: `#semiconductors`, `#export controls`, `#ASML`, `#lithography`, `#China`

---

<a id="item-tech-news-9"></a>
### [Cloudflare 控制台与 API 故障已持续半小时](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare 于 11 月 26 日在状态页发布事故通告，称正在调查 Cloudflare Dashboard 及相关 API 的问题。使用控制台和 API 的客户会受到影响，请求可能失败或页面显示错误提示。截至该通告发布，故障已持续约半小时。

telegram · zaihuapd · 11月26日 16:33

**「背景」** Cloudflare 的 Dashboard 与 API 属于控制平面，客户通过它们管理域名、DNS、防火墙规则等配置，与处理实际流量的 CDN 边缘节点和边缘安全功能相分离。根据下游状态追踪，本次 11 月 26 日的事故持续约 2.3 小时，主要导致管理请求失败或报错，而核心 CDN 和边缘安全功能未受影响。

**「影响范围」** 此次故障主要影响依赖 Cloudflare Dashboard 和相关 API 进行服务管理与配置的用户：请求可能失败或页面报错，但 Cloudflare 的核心 CDN 与边缘安全功能未受影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://isdown.app/status/cloudflare/incidents/698019-cloudflare-dashboard-and-cloudflare-api-service-issues">Cloudflare Cloudflare Dashboard and Cloudflare API — Nov 2026 ...</a></li>
<li><a href="https://isdown.app/status/cloudflare/incidents/698019-cloudflare-dashboard-and-cloudflare-api-service-issues">Cloudflare Cloudflare Dashboard and Cloudflare API — Nov 2026 ...</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#outage`, `#API`, `#dashboard`, `#infrastructure`

---

<a id="item-tech-news-10"></a>
### [微软 CEO 承认应届生招聘放缓：AI 预算优先于招人](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

微软 CEO 纳德拉在 The Pragmatic Engineer 播客中承认，应届生招聘已经放缓：公司会优先把现有员工调配到合适岗位，之后才补招新人。他称 AI 原生公司会“先用完 AI 预算，再招下一个人类”，并预测未来每家公司都会如此。截至 6 月 30 日，微软员工数降至 22.3 万人，一年减少 5000 人，是 2016 年以来首次年度下滑。MIT 与微软研究院论文显示，采用 GitHub Copilot 的企业季度技术岗招聘减少 29%，初级岗位受影响最大。

telegram · zaihuapd · 11月27日 03:03

**「背景」** 微软等大型科技公司在 AI 投入上升背景下压缩人力成本，GitHub Copilot 等 AI 编码工具已大规模部署。此前纳德拉曾表示仍相信校园招聘，本次表态与公司员工数量下滑和 AI 招聘研究相互印证。

**「影响」** 这意味着软件工程应届生和初级开发者在已采用 Copilot 的企业中可能面临更少的初级岗位和更激烈的竞争；但论文呈现的是关联而非因果，招聘放缓也可能受宏观因素影响。

**标签**: `#Microsoft`, `#AI hiring trends`, `#software engineering`, `#job market`, `#GitHub Copilot`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达暂停向东南亚四国发运 AI 服务器](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 9.0/10

英伟达已要求主要制造伙伴暂停向马来西亚、新加坡、泰国和印度尼西亚发运 AI 服务器。美国商务部上周出台新规，要求区域云服务商在 90 天内取得出口许可并核实客户不含受限中国实体。

telegram · zaihuapd · 11月26日 07:38

**「背景」** 美国商务部上周出台新规，要求区域云服务商在 90 天内取得出口许可，并核实客户不含受限中国实体；马来西亚、新加坡、泰国和印度尼西亚此前是中国 AI 公司获取英伟达先进处理器的中转地。

**「影响」** 此举可能加剧东南亚 AI 数据中心供应链压力，迫使区域云服务商和数据中心运营商重新审查订单、申请出口许可并核实客户，影响当地快速扩张的 AI 基础设施项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-halts-ai-chip-shipments-four-southwest-asian-countries">&quot;Causing Sheer Chaos&quot;: Nvidia Halts AI Chip Shipments ... | ZeroHedge</a></li>
<li><a href="https://asia.nikkei.com/business/technology/artificial-intelligence/nvidia-server-suppliers-halt-southeast-asia-shipments-over-us-curbs">Nvidia server suppliers halt Southeast Asia shipments ... - Nikkei Asia</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#export controls`, `#AI servers`, `#Southeast Asia`, `#US-China tech`

---

<a id="item-finance-news-2"></a>
### [荷兰反对美国限制 ASML 对华销售法案](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 8.0/10

荷兰外贸与发展合作大臣 Sjoerd Sjoerdsma 11 月 26 日表示，荷兰不会接受美国进一步限制 ASML 对华销售，并反对 MATCH Act 的域外管辖效力。

telegram · zaihuapd · 11月26日 14:56

**「背景」** MATCH Act 由美国两党提出，要求荷兰、日本等盟友对华实施更严格出口管制，否则美方将单方面限制其半导体设备。

**「影响」** 中国约占 ASML 今年销售额的 20%，若法案通过将直接影响其中国市场收入。

**标签**: `#ASML`, `#export controls`, `#semiconductors`, `#US-China trade`, `#Netherlands`

---