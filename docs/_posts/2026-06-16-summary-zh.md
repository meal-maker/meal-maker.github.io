---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> From 25 items, 13 important content pieces were selected

---

1. [领英求职面试中发现 npm 脚本后门](#item-1) ⭐️ 9.0/10
2. [隐藏于 Wi-Fi 智能灯泡中的禁书图书馆](#item-2) ⭐️ 8.0/10
3. [Iroh 1.0 发布点对点网络库](#item-3) ⭐️ 8.0/10
4. [用本地模型取代 Claude/GPT 的实战分享](#item-4) ⭐️ 8.0/10
5. [探讨无人类劳动者的经济是否可能](#item-5) ⭐️ 8.0/10
6. [家庭实验室 AI 开发平台](#item-6) ⭐️ 8.0/10
7. [Hetzner 宣布最高三倍价格大幅上涨](#item-7) ⭐️ 8.0/10
8. [福克斯收购 Roku，重塑流媒体硬件格局](#item-8) ⭐️ 8.0/10
9. [Salesforce 以 36 亿美元收购 Fin（前 Intercom）](#item-9) ⭐️ 8.0/10
10. [TimescaleDB Hypercore 压缩深度解析](#item-10) ⭐️ 8.0/10
11. [美国电池制造业产出持续刷新纪录](#item-11) ⭐️ 7.0/10
12. [铜药物恢复记忆并清除阿尔茨海默病蛋白（小鼠实验）](#item-12) ⭐️ 7.0/10
13. [对计算机的怀旧热爱与行业批判](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [领英求职面试中发现 npm 脚本后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

一名求职者发现，一家加密货币初创公司的招聘人员发送了一个 GitHub 仓库，其中在 npm 的'prepare'脚本中隐藏了后门，当运行'npm install'时会自动执行，从而入侵开发者的机器。 这一事件凸显了一种危险且日益常见的社会工程攻击手段，该手段在技术面试中利用信任和常规操作来针对开发者。同时，它也暴露了在举报机制和平台应对此类网络犯罪方面存在的重大漏洞。 后门隐藏在 package.json 文件中的'prepare'脚本里，被埋在注释掉的测试代码之中。该负载会执行从远程服务器发送的任何命令，相当于一个完整的远程访问木马，而向 GitHub 和 LinkedIn 的报告并未立即得到处理。

hackernews · lwhsiao · Jun 15, 20:00

**背景**: npm 是 Node.js 的包管理器，其中的'prepare'脚本会在'npm install'之后自动运行，通常用于构建包等任务。攻击者越来越多地滥用 npm 生命周期脚本（如'preinstall'、'postinstall'和'prepare'），在安装过程中执行恶意代码，这使得供应链攻击成为 JavaScript 生态系统中持续存在的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem</a></li>

</ul>
</details>

**社区讨论**: 评论者对此表示震惊，认为这种攻击非常接近正常的面试任务，有人提到他们在近几个月内多次遇到类似尝试。其他人则批评缺乏有效的举报渠道以及平台未能及时删除恶意代码，呼吁建立有组织的防御措施来应对此类网络犯罪。

**标签**: `#cybersecurity`, `#npm`, `#backdoor`, `#supply chain attack`, `#social engineering`

---

<a id="item-2"></a>
## [隐藏于 Wi-Fi 智能灯泡中的禁书图书馆](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 8.0/10

一位开发者创建了一个项目，将禁书存储于基于 ESP8266 的 Wi-Fi 智能灯泡的闪存中，使其成为一个本地网页服务器，通过其 Wi-Fi 网络提供书籍访问，无需互联网连接。 该项目展示了一种巧妙且实用的方法，利用日常物联网设备作为隐藏图书馆，规避审查制度，使受限环境中的人们能够访问被禁文学作品。 灯泡固件被替换为自定义 ESP 网页服务器，从其有限的闪存中提供 ePub 文件；社区讨论中提到，这些设备有可能形成网状网络来共享内容。

hackernews · sohkamyung · Jun 15, 22:37

**背景**: 许多 Wi-Fi 智能灯泡基于低成本微控制器（如 ESP8266），具有有限的闪存，可刷入自定义固件。通过重新刷写固件，开发者将灯泡转变为本地文件服务器，在隐藏网络中托管禁书，无需互联网即可访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mischianti.org/esp8266-firmware-and-filesystem-update-with-ftp-client-2/">esp8266 firmware and filesystem update with FTP client - 2</a></li>
<li><a href="https://github.com/cotestatnt/esp-fs-webserver">GitHub - cotestatnt/esp-fs-webserver: ESP32/ESP8266 webserver, WiFi ...</a></li>
<li><a href="https://microcontrollerslab.com/esp8266-nodemcu-web-server-using-littlefs-flash-file-system/">ESP8266 NodeMCU Web Server using LittleFS (Flash File System)</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该项目的创意及其与审查制度和言论自由的关联，并提到了类似的历史项目如 PirateBox 和 LibraryBox。部分评论讨论了存储限制和网状网络的潜力，另一些则指出了'禁书'名单的政治背景。

**标签**: `#IoT`, `#censorship`, `#privacy`, `#hacking`, `#free speech`

---

<a id="item-3"></a>
## [Iroh 1.0 发布点对点网络库](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 是一个重要的里程碑版本，作为模块化的点对点网络库，它使用拨号键（dial keys）替代 IP 地址，实现安全的应用层连接。 该库通过自动处理直接连接、NAT 穿透和中继回退，让开发者能够更轻松地构建分布式应用，用户无需管理账户或网络配置。 Iroh 1.0 内置支持 IPv4、IPv6 和中继传输，并通过自定义传输接口实现可扩展性。它基于 QUIC 提供加密连接，同时利用打洞技术配合中继服务器。

hackernews · chadfowler · Jun 15, 15:13

**背景**: 当设备切换网络或位于 NAT 之后时，传统的基于 IP 的网络连接会失效，从而使点对点连接变得困难。Iroh 通过使用加密的“拨号键”（dial keys）来标识对等节点，不受网络位置限制，并利用打洞技术实现直接连接，中继服务器作为后备方案。该库用 Rust 编写，为开发者提供 QUIC 流接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iroh.computer/">Iroh</a></li>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys instead ...</a></li>
<li><a href="https://docs.rs/iroh/latest/iroh/">iroh - Rust - Docs.rs</a></li>

</ul>
</details>

**社区讨论**: 有评论者将 Iroh 比作“应用层的 Tailscale”，并指出它无需用户账户。一位开发者澄清，可以通过新的传输接口添加 WebRTC 或 BLE 等自定义传输。部分读者对问题描述感到困惑，而另一些则赞赏其去中心化愿景。

**标签**: `#networking`, `#peer-to-peer`, `#Rust`, `#decentralized`, `#secure connectivity`

---

<a id="item-4"></a>
## [用本地模型取代 Claude/GPT 的实战分享](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

一篇 Ask HN 帖子及其评论显示，许多开发者已彻底用本地模型替代了 Claude 和 GPT 等云端编程助手，例如使用双 RTX 3090 运行 Qwen3.6 35B 模型，日常编码任务可达每秒约 150 token。 这一转变表明开源本地模型已足够成熟，能胜任大部分编程任务，在隐私、成本降低和摆脱云端依赖方面具有显著优势，可能重塑开发者使用 AI 辅助编程的方式。 像 Qwen3.6-35B-A3B 这样的模型采用混合专家架构，每个 token 仅激活 30 亿参数，可在消费级硬件上快速推理；评论者报告质量与 8-12 个月前的前沿模型相当，配置通常依赖 llama.cpp 或 pi 编码工具。

hackernews · cloudking · Jun 15, 14:46

**背景**: 本地大型语言模型（LLM）完全在用户自己的硬件上运行，无需将代码或数据发送到外部服务器。混合专家（MoE）模型每个 token 仅激活部分参数，在总模型规模与推理速度之间取得平衡。双 RTX 3090 配置（共 48GB 显存）是本地运行超过 350 亿参数模型的常见选择。Qwen3.6-35B-A3B 于 2026 年 4 月发布，是一款针对编程任务优化的开放权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6-35b-a3b">Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen/Qwen3.6-35B-A3B · Hugging Face</a></li>
<li><a href="https://insiderllm.com/guides/multi-gpu-local-ai/">Best Dual-GPU Local AI Setup: RTX 3090, 5060 Ti (2026)</a></li>

</ul>
</details>

**社区讨论**: 评论以积极为主，用户分享了详细的硬件和软件配置。大多数人认为本地模型不如前沿云端模型智能，但‘足够好’应对大部分日常编码任务。少数人警告不使用新模型可能存在机会成本，但总体情绪是出于隐私和成本考虑，这种权衡是值得的。

**标签**: `#local LLMs`, `#AI coding`, `#developer tools`, `#machine learning`, `#software engineering`

---

<a id="item-5"></a>
## [探讨无人类劳动者的经济是否可能](https://gmalandrakis.com/writings/ad-economicum.html) ⭐️ 8.0/10

一篇来自 gmalandrakis.com 的文章探讨了一个没有人类劳动者的经济的可行性及其后果，引发了关于财富分配和劳动目的的深入讨论。 随着自动化和人工智能的发展，文中提出的问题对社会结构、不平等以及工作的意义具有深远影响，使其成为未来经济的关键辩论。 该文章获得了 8.0/10 的高参与度评分和 182 条评论，表明社区对其重要性的高度认可，但文中未提供具体的技术细节或突破。

hackernews · l0new0lf-G · Jun 15, 21:10

**背景**: “无人民经济”是一种假设的未来状态，其中机器和人工智能完成所有劳动，不再需要人类劳动者。这引发了关于财富如何分配以及人类在此类社会中扮演何种角色的根本性问题。该文章在不假设特定技术时间线的情况下探讨了这些问题。

**社区讨论**: 评论者表达了多种观点：有人警告说自动化将在赢家通吃的场景中进一步集中财富，而另一些人则认为人类仍可以在没有机器人的情况下互相交易。少数人批评基于消费的经济前提存在缺陷，还有一位评论者认为整个讨论充满了逻辑谬误和过早的推测。总体情绪分歧严重，反映出对 AI 长期经济影响的不确定性。

**标签**: `#artificial intelligence`, `#economics`, `#automation`, `#future of work`, `#society`

---

<a id="item-6"></a>
## [家庭实验室 AI 开发平台](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 8.0/10

一位家庭实验室爱好者发布了一篇详细的文章，介绍如何构建一个集成 Forgejo、Argo Workflows 和 AI 代理的 AI 开发平台，以实现代码生成和代码审查的自动化。 这之所以重要，是因为它展示了如何将自托管的 Git 仓库和 Kubernetes 原生工作流引擎与 AI 代理相结合，创建自定义的自动化 CI/CD 开发流水线，为基于云的服务提供了一种替代方案。 该平台使用 Forgejo 作为 Git 托管服务，Argo Workflows 编排工作流程步骤，AI 代理负责生成和审查代码。工作流程包括标记问题、编写拉取请求、测试，以及带有合并互斥锁的审查-修改循环，以防止合并风暴。

hackernews · rsgm · Jun 15, 15:09

**背景**: Forgejo 是一个自托管、轻量级的 Git 托管平台，类似于 GitHub，在家庭实验室爱好者中很受欢迎。Argo Workflows 是一个 Kubernetes 原生工作流引擎，用于编排并行任务。这里提到的 AI 代理是指能够自动生成代码更改和审查代码的语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://forgejo.org/">Forgejo – Beyond coding. We forge .</a></li>
<li><a href="https://github.com/argoproj/argo-workflows">GitHub - argoproj/ argo - workflows : Workflow Engine for Kubernetes</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示多位用户正在构建类似的系统，有人使用 Forgejo action runner 配合 Opencode 进行代码生成，也有人使用 n8n 和不同的 AI 模型。还有用户提到域名 rsgm.dev 被 Quad9 DNS 过滤，引发了一个简短的旁支讨论。

**标签**: `#homelab`, `#AI development`, `#CI/CD`, `#Forgejo`, `#Argo Workflows`

---

<a id="item-7"></a>
## [Hetzner 宣布最高三倍价格大幅上涨](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 8.0/10

Hetzner 宣布对其服务器产品进行大幅提价，部分客户面临高达三倍的价格上涨，官方调价页面已公布详情。 此次调价影响大量依赖 Hetzner 经济型主机的开发者和企业，可能打乱预算并促使迁移至其他服务商，同时反映了 AI 需求推动的硬件成本普遍上涨。 价格变动涉及 Hetzner 的云服务器及其他产品；虽然 25-50%的涨幅或可预料，但部分客户反映高达三倍的增长，此幅度异常之高。

hackernews · tuhtah · Jun 15, 13:19

**背景**: Hetzner 是一家德国网络托管公司，以提供高性价比的专用服务器、云服务器及其他托管服务著称，深受开发者及中小企业欢迎。此次涨价归因于 RAM 和磁盘存储等硬件组件成本上升，而 AI 热潮加剧了全球计算资源需求，进一步推高了价格。

**社区讨论**: 社区评论对涨幅之大表示震惊和不满，用户指出三倍增长前所未有，并质疑其合理性。有人认为这反映了硬件短缺推动成本上涨的行业趋势，另一些人则感叹 Hetzner 性价比时代的终结，并讨论可能的替代服务商。

**标签**: `#Hetzner`, `#Price Adjustment`, `#Cloud Hosting`, `#Hardware Costs`, `#Community Discussion`

---

<a id="item-8"></a>
## [福克斯收购 Roku，重塑流媒体硬件格局](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

福克斯公司宣布收购流媒体硬件与平台巨头 Roku，这笔交易可能显著改变流媒体行业的竞争格局。 此次收购将一家大型内容制作商与主导地位的流媒体设备平台结合起来，引发了关于媒体整合和内容策划潜在偏见的担忧，影响数百万使用 Roku 的美国家庭。 Roku 一直朝着包含自家内容和广告的方向发展，这令偏好服务中立体验的用户感到不满；福克斯的收购加剧了这些担忧，因为福克斯现在同时控制了内容和硬件。

hackernews · thm · Jun 15, 12:50

**背景**: Roku 是领先的流媒体设备平台，拥有数千万家庭用户，以其聚合多种服务内容的中立界面而闻名。福克斯是一家大型媒体集团，旗下拥有福克斯新闻、福克斯体育等娱乐资产。这笔交易将内容创作与硬件分发合并，这一趋势引发了反垄断和消费者选择问题的关注。

**社区讨论**: 社区反应普遍负面，用户对 Roku 未来中立性深感悲观。许多评论者担心福克斯会推广自家内容并带有偏见，部分用户已开始转向 Nvidia Shield 等替代设备，以重新掌控观看体验。

**标签**: `#acquisition`, `#Roku`, `#Fox`, `#streaming`, `#media consolidation`

---

<a id="item-9"></a>
## [Salesforce 以 36 亿美元收购 Fin（前 Intercom）](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce 于 2026 年 6 月 15 日宣布达成最终协议，以 36 亿美元收购前身为 Intercom 的 Fin，以加强其 Agentforce AI 客户支持平台。 此次收购使 Salesforce 能够直接与由其前联合 CEO Bret Taylor 创立的 AI 客服初创公司 Sierra 竞争，并防止独立的 AI 客服代理成为 CRM 生态系统之外的控制点。 Fin 在交易前仅一个月才从 Intercom 更名，收购预计将在 Salesforce 的第四财季完成。36 亿美元的价格反映了 AI 客服代理领域的高估值，竞争对手如 Sierra 估值 158 亿美元，Decagon 估值 45 亿美元。

hackernews · colesantiago · Jun 15, 12:08

**背景**: Salesforce 是最大的客户关系管理平台，其 Agentforce AI 旨在自动化客服任务。Fin（前 Intercom）是领先的 AI 客服机器人，覆盖客户全周期。此次收购是 CRM 供应商收购 AI 初创公司以将智能代理集成到平台中的更广泛行业趋势的一部分，因为客户越来越期待 AI 驱动的客服。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/ai-and-ml/2026/06/15/salesforce-reels-in-customer-support-ai-specialist-fin-for-36b/5255571">Salesforce reels in customer support AI specialist Fin for $3.6B</a></li>
<li><a href="https://fin.ai/">Fin. The highest performing Customer Agent</a></li>
<li><a href="https://sierra.ai/blog/agents-as-a-service">Agents as a service | Sierra</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：一些人指出，执行得当的 AI 客户服务可以超越人工支持，如 Starlink 体验所见，而另一些人则质疑一旦企业能够训练自己的代理，像 Intercom 这样的客服公司的长期生存能力。交易在更名后立即发生以及与 Sierra 的竞争也被强调。

**标签**: `#Salesforce`, `#acquisition`, `#AI customer service`, `#CRM`, `#Fin`

---

<a id="item-10"></a>
## [TimescaleDB Hypercore 压缩深度解析](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

这篇文章详细解释了 TimescaleDB 的 Hypercore 压缩如何在 PostgreSQL 中为时间序列数据实现高压缩比。 这很重要，因为时间序列数据增长迅速，高效的压缩可以降低存储成本并加速查询，使 PostgreSQL 在物联网、监控和分析等工作负载中更具竞争力。 Hypercore 采用列式存储和类型感知技术，包括增量编码、增量之增量编码、simple-8b、游程编码、基于 XOR 的压缩和字典压缩，声称可实现高达 98%的压缩比。

hackernews · lkanwoqwp · Jun 15, 17:29

**背景**: TimescaleDB 是 PostgreSQL 的一个扩展，专门处理时间序列数据。时间序列数据通常具有重复的模式和值，因此可压缩性很高。列式存储按列而非按行分组数据，从而改善分析查询的压缩和扫描性能。Hypercore 是 TimescaleDB 最新的压缩引擎，结合了这些技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.tigerdata.com/use-timescale/latest/hypercore/compression-methods/">Tiger Data Documentation | About compression methods</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/compression/">Timescale Documentation | Compression</a></li>
<li><a href="https://tiger-data-docs.vercel.app/docs/learn/columnar-storage/understand-hypercore">Understand hypercore | Tiger Data Docs</a></li>

</ul>
</details>

**社区讨论**: 社区讨论技术性很强，用户们争论压缩中的 IO 与 CPU 使用权衡（gopalv），分享替代方案如 deltax 扩展（tudorg），并询问物联网的有损压缩（heliosAtWork）。一些人对“高达 98%”的说法表示怀疑（robocat），而 blackoil 指出 Facebook 的 Gorilla 使用了类似的增量技术。

**标签**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-11"></a>
## [美国电池制造业产出持续刷新纪录](https://fred.stlouisfed.org/series/IPG33591S) ⭐️ 7.0/10

美联储的电池制造业工业生产指数（FRED 系列 IPG33591S）已达到历史新高，表明美国电池产出持续增长。 这一纪录表明美国正在扩大本土电池生产，这对电动汽车和储能领域至关重要。但社区评论指出，美国产能（70 GWh）仍远落后于中国（1,755 GWh），凸显了加速投资的必要性。 FRED 系列 IPG33591S 衡量的是归类为耐用品的所有电池产出，包括一次电池。一位评论者指出，增长可能部分反映了一次电池（如 AA 电池）的生产，而非仅电动汽车用的先进电池电芯。

hackernews · epistasis · Jun 15, 20:28

**背景**: 电池制造业产出是衡量储能和电动汽车工业产能的关键指标。美国通过《通胀削减法案》等政策持续投资本土电池生产，但目前中国以巨大规模主导全球生产，欧洲也大幅领先美国。

**社区讨论**: 社区评论对美国增长表示乐观，但强调与中国之间的巨大差距；有用户给出了 2025 年具体产能数据：美国 70 GWh，中国 1,755 GWh，欧洲 252 GWh。另一位评论者质疑增长是否与电动汽车普及率成比例，而其他人则指出该数据可能包含一次电池。

**标签**: `#batteries`, `#manufacturing`, `#energy storage`, `#US industry`, `#China`

---

<a id="item-12"></a>
## [铜药物恢复记忆并清除阿尔茨海默病蛋白（小鼠实验）](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins) ⭐️ 7.0/10

莫纳什大学研究人员报告，铜递送药物 Cu(ATSM) 在阿尔茨海默病小鼠模型中将β-淀粉样蛋白积累减少 42%，并将空间记忆能力提升 44%，且该化合物已在其他疾病中通过安全性评估。 这项研究提供了一种针对阿尔茨海默病中铜失调的新疗法，其机制不同于以往在临床试验中基本失败的淀粉样蛋白导向疗法。如果结果能转化到人类，可能开辟新的治疗路径，但淀粉样蛋白假说仍具争议。 该药物恢复了血脑屏障清除机制，在小鼠模型中将β-淀粉样蛋白斑块减少 42%，空间学习能力提升 44%。Cu(ATSM) 已在其他疾病中完成安全性评估，可能加快其进入阿尔茨海默病人体试验的进程。

hackernews · bookofjoe · Jun 15, 14:48

**背景**: 阿尔茨海默病是一种神经退行性疾病，特征为进行性记忆丧失和大脑中β-淀粉样蛋白斑块的积累。铜失调被认为与疾病相关，过量的铜可能促进淀粉样蛋白聚集和氧化应激。本研究探索了一种递送铜以恢复金属稳态的药物，旨在增强大脑对有毒蛋白的自然清除能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins">Copper drug restores memory and clears toxic Alzheimer's proteins</a></li>
<li><a href="https://medicalxpress.com/news/2026-06-copper-drug-memory-toxic-alzheimer.html">Copper drug restores memory and clears toxic Alzheimer's proteins ...</a></li>
<li><a href="https://www.drugtargetreview.com/copper-drug-cuatsm-reduces-alzheimers-proteins-by-42-percent-in-preclinical-study/2135715.article">Copper drug Cu (ATSM) reduces Alzheimer's proteins by 42 percent in ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪为谨慎乐观，许多评论者指出淀粉样蛋白靶向疗法长期失败的历史，并提醒对小鼠研究持怀疑态度。一些人认为淀粉样蛋白斑块可能是结果而非原因，而其他人则承认基于铜的新颖机制以及因已有安全性数据而可能加快临床试验的潜力。

**标签**: `#Alzheimer's research`, `#amyloid-beta`, `#copper transport`, `#drug repurposing`, `#neuroscience`

---

<a id="item-13"></a>
## [对计算机的怀旧热爱与行业批判](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 6.0/10

Michael Enger 发表了一篇个人随笔，反思他对计算机作为可动手改造的机器的深深热爱，同时批评了现代科技行业以及对编程和 AI 工具的排他性态度。 这篇随笔在 Hacker News 上引发了广泛共鸣，激起了关于热爱计算机本身与厌恶其周边行业之间的张力的讨论，以及将 AI 斥为‘蛇油’是否具有排他性的辩论。 作者将低级编程的乐趣与现代软件开发的挫折进行对比，而 Hacker News 上的讨论补充了关于 AI 作为实用工具以及某些怀旧情绪具有排他性的观点。

hackernews · speckx · Jun 15, 20:14

**背景**: 这篇随笔反映了资深程序员中的常见情绪：对个人计算机早期时光的喜爱，当时机器更简单、更便于探索。‘排他性态度’（gatekeeping）指的是那些排斥新手或贬低他们使用 AI 等现代工具的态度。

**社区讨论**: 评论显示出分歧：一些人同意热爱计算机本身但厌恶行业，另一些人则为 AI 作为合法工具辩护。tptacek 提出了一个值得注意的批评，认为作者的情绪具有排他性，暗示作者通过辛苦学习而获得了对他人使用计算机方式的发言权。

**标签**: `#computing culture`, `#gatekeeping`, `#AI tools`, `#programming nostalgia`, `#hacker ethos`

---