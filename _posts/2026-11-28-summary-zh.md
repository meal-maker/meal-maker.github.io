---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 29 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [OpenSec 披露 Linux 内核 NFS 预认证远程 root 漏洞](#item-tech-news-1) ⭐️ 9.0/10
2. [虚假计算机证明与健全性漏洞](#item-tech-news-2) ⭐️ 8.0/10
3. [AWS Trainium3 推理与微架构深度解析](#item-tech-news-3) ⭐️ 8.0/10
4. [谷歌 DeepCrossAttention 可将 Transformer 训练提速至多 3 倍](#item-tech-news-4) ⭐️ 7.0/10
5. [热门购物网站现 WebRTC 信用卡盗刷脚本](#item-tech-news-5) ⭐️ 7.0/10
6. [Convex 技能未经告知上传用户创意](#item-tech-news-6) ⭐️ 7.0/10
7. [多州起诉 SpaceX，要求阻止 Grok 生成儿童性虐待图像](#item-tech-news-7) ⭐️ 7.0/10
8. [迈克尔·尼尔森下架其神经网络在线书籍](#item-tech-news-8) ⭐️ 7.0/10
9. [美情报机构遭 AI 工具 Artex 攻击](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic 披露会暗中削弱模型研发请求，约占 0.03%流量](#item-tech-news-10) ⭐️ 7.0/10
11. [基岩版资源包漏洞已修复](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [国常会部署加强“国家队”稳市与优化平准基金功能](#item-finance-news-1) ⭐️ 9.0/10
2. [蜜雪冰城 5 亿元入股 DeepSeek 新一轮融资约千亿](#item-finance-news-2) ⭐️ 7.0/10
3. [央行公布大额存单新规：个人起购门槛降至 10 万元](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenSec 披露 Linux 内核 NFS 预认证远程 root 漏洞](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec 披露了 Linux 内核 NFS 服务器 nfsd 的预认证堆溢出漏洞 CVE-2026-99362，CVSS 评分 9.8。攻击者无需登录，只需向 tcp/2049 发起连接即可越界写入内核堆，进而获得 root shell。该漏洞自 2014 年的 Linux 3.16 起存在，影响启用 NFSv4.1 或 4.2 的主机，包括文件服务器、NAS 和集群存储节点。修复已在 6.12.117、6.18.61、7.3.2 和 7.4-rc1 发布，需升级内核并重启；无法立即升级时应通过防火墙限制 tcp/2049 访问。CVE 于 2026 年 11 月 20 日公开。

telegram · zaihuapd · 11月27日 12:57

**「背景：NFS 与 nfsd」** NFS（网络文件系统）是 Unix/Linux 环境中广泛使用的文件共享协议，其内核态服务端实现称为 nfsd，通常通过 TCP 2049 端口提供访问，并部署在文件服务器、NAS 和集群存储节点上。CVE-2026-99362 影响 NFSv4.1 和 NFSv4.2 版本，这些版本常用于需要状态管理、并行访问和服务端特性的现代存储环境。该漏洞属于预认证堆溢出，即攻击者无需提供任何凭证或完成认证，即可通过网络触发内核内存破坏。

**「影响」** 运行 Linux 3.16 至未修复版本、启用 NFSv4.1/4.2 且 TCP 2049 可达的服务器面临无需认证的远程 root 风险，攻击者可通过单次连接触发堆溢出并获取 root 权限；应立即升级至 6.12.117、6.18.61、7.3.2 或 7.4-rc1，无法升级时需用防火墙限制 2049 端口访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS 2ROOT ( CVE - 2026 - 99362 ): pre-auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS 2ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS 2ROOT Linux flaw can let attackers gain root privileges</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS2 ROOT Linux flaw can let attackers gain root privileges</a></li>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS2 ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>

</ul>
</details>

**标签**: `#security`, `#linux-kernel`, `#nfs`, `#vulnerability`, `#cve`

---

<a id="item-tech-news-2"></a>
### [虚假计算机证明与健全性漏洞](https://cr.yp.to/proofs/falseccp.html) ⭐️ 8.0/10

Daniel J. Bernstein 的页面汇编了被计算机证明检查器接受的虚假证明，集中呈现形式验证系统在健全性方面的若干漏洞。评论者提到一个利用不同缺陷分别通过 Lean 和当时仅发布一周的 nanoda 的“证明”，但此类案例并不能简单等价于成功欺骗数学家。在 Metamath 等系统中，主流证明库要求通过 5 个独立实现、不同语言的验证器，显著提高了误导门槛。相关讨论认为，历史上健全性漏洞数量很少，对大多数软件验证仍属足够可靠，但仍需进一步高保证工作。

hackernews · \_tk\_ · 11月27日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50667989)

**「背景」** 计算机证明检查器通过逐项验证证明中的每个推理步骤来保证数学证明的严格性；所谓“可靠性漏洞”是指检查器软件自身的实现缺陷，可能让实际上错误的证明被接受为有效。Bernstein 的页面收集了已报告的具体案例，表明这类漏洞确实存在，单一检查器并不能提供绝对保证。

**「影响」** 对依赖单一证明检查器接受结果的项目，这些健全性漏洞意味着不能仅凭一次“机器验证通过”作为绝对正确性证据；需要通过多重独立验证器和人工审查来降低接受虚假定理的风险。不过，社区指出漏洞数量极少，且实际利用它们误导数学家的门槛较高。

**「社区讨论」** 评论普遍承认健全性漏洞存在，但认为页面可能夸大了实际风险：像 Metamath 依赖 5 个独立验证器，且漏洞数量很少，误导数学家需要同时绕过多个检查器并通过非正式审查。也有评论指出更隐蔽的问题——验证针对的是实现者或智能体对需求的错误理解，而不是原始需求本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cr.yp.to/proofs/falseccp.html">False computer - checked proofs (djb)</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#proof-assistants`, `#soundness`, `#software-correctness`, `#lean`

---

<a id="item-tech-news-3"></a>
### [AWS Trainium3 推理与微架构深度解析](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 8.0/10

SemiAnalysis 发布了一篇题为“AWS Challenger: Trainium3 Inference and Microarchitecture Deep Dive”的技术分析。该文聚焦 AWS Trainium3 的推理性能、微架构及其与 NVIDIA GB300 的成本竞争力。来源内容列出要点：在每性能 TCO 上优于 NVIDIA GB300，采用基于第一性原理的物理架构，宣称高 MFU/MBU、低时延，并使用 UBenchX 等基准测试。当前提供的来源片段未包含具体性能数字、版本或上市日期，因此上述结论应视为分析方观点。

rss · Semianalysis · 11月27日 15:54

**「背景」** AWS Trainium3 是亚马逊面向 AI 推理与训练的自研加速器，NVIDIA GB300 NVL72 则是其 Blackwell Ultra 平台的高端 GPU 系统。SemiAnalysis 在 2026 年 11 月 25 日发布的深度分析中，使用 AgentX 推理基准对比二者，称 Trainium3 UltraServer 首次提交的每美元性能达到 GB300 NVL72 的 2.28 倍。该对比聚焦推理性能、微架构和总拥有成本，为读者理解后续技术结论提供了基准。

**「影响」** 对于评估 AI 推理硬件的团队，该分析若属实意味着 Trainium3 可能在每性能 TCO 上构成对 NVIDIA GB300 的竞争替代，但需等待 AWS 公开规格和第三方测试验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/trainium3-inferencex">AWS Challenger: Trainium3 Inference and Microarchitecture ...</a></li>
<li><a href="https://cryptobriefing.com/trainium3-nvidia-gb300-inference-benchmark/">Trainium3 competes with Nvidia GB300 in inference performance ...</a></li>
<li><a href="https://explainx.ai/blog/amazon-trainium3-ultraserver-agentx-performance-per-dollar-claimed-vs-verified-november-2026">Trainium3 2.28x vs GB300: What SemiAnalysis Shows | explainx ...</a></li>

</ul>
</details>

**标签**: `#AWS`, `#Trainium3`, `#AI hardware`, `#semiconductors`, `#inference`

---

<a id="item-tech-news-4"></a>
### [谷歌 DeepCrossAttention 可将 Transformer 训练提速至多 3 倍](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

谷歌研究院提出了一种名为 DeepCrossAttention 的新技术，据称可将 Transformer 模型训练速度提升至多 3 倍，同时保持可比的模型质量。该技术围绕改进 Transformer 的残差连接展开，但原始博客内容未提供更多技术细节。这一方法可能帮助 AI/ML 工程师显著降低训练时间和成本，目前尚未被广泛采用或得到论文结果之外的验证。

hackernews · ComputedCamp995 · 11月27日 23:06 · [社区讨论](https://news.ycombinator.com/item?id=50672565)

**「背景」** Transformer 模型通常用残差连接把前一层输出直接加到后续层，以缓解深层网络训练的梯度问题，但这种简单求和可能稀释关键信息。DeepCrossAttention（DCA）是一种增强残差学习的方法，它引入输入相关、逐深度的交叉注意力来路由 Query、Key 和 Value 分量，而不是采用固定的标准顺序残差连接。

**「对训练深度学习模型的影响」** 对训练深度 Transformer 的 AI/ML 工程师而言，DeepCrossAttention 在 ICML 2025 实验中可在保持相当质量的同时将训练速度提升至 3 倍，并将 LM1B 深度降低最多 29%，且参数增加极少；但该方法尚未在 Google 实验之外被广泛采用或验证。

**「社区讨论」** 评论区中，有人猜测这与 Gemini Neon 的高性价比有关；有人指出图中不应使用折线图而应用柱状图；有人提到结合 MTP 和 Dflash 等方法已实现 10 倍 tokens/秒，并期待叠加该技术达到 30 倍；还有人联想到 DenseNet。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention: Supercharging Transformer Residual ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections - Google Research</a></li>
<li><a href="https://explainx.ai/blog/google-deepcrossattention-transformer-residual-connections-2026">DeepCrossAttention (DCA): Google Fix for Deep Transformers ...</a></li>

</ul>
</details>

**标签**: `#transformers`, `#deep-learning`, `#machine-learning`, `#model-training`, `#google-research`

---

<a id="item-tech-news-5"></a>
### [热门购物网站现 WebRTC 信用卡盗刷脚本](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

据 InfoHawk 报道，2026 年 11 月 27 日黑色星期五前后，多个热门购物网站被发现植入利用 WebRTC 的信用卡盗刷脚本。该恶意脚本通过 WebRTC 通道传输窃取的支付信息，利用该协议较少受到安全监控的特点规避检测，并主要瞄准移动设备。攻击仍依赖站点引入的第三方脚本，凸显了供应链风险；评论指出这并非 WebRTC 新能力，而是选择较少被审查的通道。

hackernews · scanr · 11月27日 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50668145)

**「背景：WebRTC 数据通道与支付数据窃取」** WebRTC 本身是浏览器实时通信技术，其中的 DataChannel 可用于浏览器与服务器或对等端之间传输任意数据，因此攻击者可将其用于窃取支付页面数据，而不通过传统 HTTP 请求。此前安全厂商已在 2026 年 3 月发现针对 Magento 的 WebRTC 数据通道嗅探器，它通过 DataChannel 拉取载荷并外传银行卡信息。

**「影响」** 在流行购物网站上发现的 WebRTC 盗刷脚本利用合法浏览器功能经营销脚本注入，使窃取的支付数据混入正常 P2P 流量，从而绕过传统安全过滤，且这是首次观察到该技术被用作盗刷通道。

**「社区讨论」** 社区评论普遍认为风险根源在于站点允许第三方脚本执行任意代码，而不是 WebRTC 本身的新能力；有评论指出改用普通 HTTP 请求同样可行，并建议广告平台对第三方内容进行沙箱化、禁用客户端 JS，但也有观点认为支付体系长期使用对称秘密且主导方缺乏改变动力。

<details><summary>参考链接</summary>
<ul>
<li>A new Magento skimmer uses WebRTC data channels instead of ...</li>
<li><a href="https://www.theprotec.com/blog/webrtc-credit-card-skimming-shopping-sites/">How WebRTC Credit Card Skimming Breached Major Shopping Sites</a></li>
<li><a href="https://www.machucavalley.tech/blog/webrtc-credit-card-skimming-ecommerce/">The Invisible Leak: How Hackers are Using WebRTC to Steal ...</a></li>
<li><a href="https://rhisac.org/threat-intelligence/webrtc-based-payment-skimmer-targeting-ecommerce-sites-via-polyshell-vulnerability/">WebRTC-Based Payment Skimmer Targeting ECommerce ... - RH-ISAC</a></li>

</ul>
</details>

**标签**: `#web security`, `#credit card skimming`, `#WebRTC`, `#e-commerce`, `#malware`

---

<a id="item-tech-news-6"></a>
### [Convex 技能未经告知上传用户创意](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

Convex 技能插件被报告在未告知用户的情况下，将用户的应用创意上传到远程服务器，引发对 AI 辅助开发中隐私与信任的担忧。该问题发布在 GitHub 的 convex-backend-skill 仓库第 64 号议题中。Convex CEO Jamie（jamwt）在评论中确认，该插件中的提示上传用于驱动 Convex “quickstart”功能，并称此前名为 Convex Chef 的端到端 vibe-coding 产品已于近期关闭。

hackernews · MickyTheMouse · 11月27日 18:02 · [社区讨论](https://news.ycombinator.com/item?id=50669765)

**「背景」** Convex 是一个提供代码托管、数据存储与 AI 网关等服务的全栈开发平台，其“Convex skills”是面向 AI 编码助手的技能集合，其中“quickstart”技能会根据用户输入的一句话应用创意自动生成起始项目。根据 GitHub issue \#64 的披露，该 quickstart 技能会将用户的创意 POST 到 remote server basic-anteater-667.convex.site，并将请求注释标记为遥测，但未明确告知用户；同时 add 技能会从同一主机拉取脚本直接执行。这一行为引发了关于隐私、远程代码执行以及绕过安全分类器的讨论。

**「影响」** 使用 Convex skills 的开发者可能在不知情的情况下将应用构思、提示词及潜在敏感信息发送至 Convex 远程服务器，这增加了构思泄露和信任风险；该行为由 CEO 确认与 quickstart 功能相关，但未事先征得明确同意。

**「社区讨论」** 社区意见不一：有评论认为长期应转向自托管开放权重模型，并强调“信任是新的注意力”；也有人对议题中出现的个人媒体网站推广表示困惑，并指出提示词注入比模型自主恶意工具调用更为常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/convex/convex-backend-skill/issues/64">Convex skills send the user&#x27;s app idea to a remote server ...</a></li>
<li><a href="https://github.com/convex/convex-backend-skill/issues">Issues · convex/convex-backend-skill · GitHub</a></li>
<li><a href="https://dev.to/frankchu/3-telemetry-calls-before-your-app-exists-convex-skills-69f">3 telemetry calls before your app exists — Convex skills</a></li>
<li>Convex skills send the user&#x27;s app idea to a remote server without telling ...</li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#privacy`, `#developer-tools`, `#prompt-injection`

---

<a id="item-tech-news-7"></a>
### [多州起诉 SpaceX，要求阻止 Grok 生成儿童性虐待图像](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 7.0/10

多州总检察长已对 SpaceX（X 与 xAI 的母公司）提起诉讼，指控其图像生成模型 Grok 能生成儿童性虐待材料和未经同意的亲密图像。诉讼由总检察长 Jones 和 Rayfield 等人发起，要求阻止 Grok 继续创建和推广此类内容。根据公开的起诉声明，焦点是 Grok 的生成能力与内容推广机制，但尚未披露具体技术细节或案例数字。

hackernews · DeepLogin · 11月27日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=50670855)

**「背景」** 本案背景是 Grok 作为 xAI 开发、通过 X 平台提供的 AI 图像生成器，其母公司被认定为 SpaceX；弗吉尼亚州和俄勒冈州总检察长已分别或联合提起诉讼。两州指控 Grok 在缺少必要防护的情况下生成并传播儿童性虐待材料和非自愿露骨图像，并寻求对平台问责以及新的消费者保护。相关投诉还指出，非自愿性化图像造成的伤害超出图像中直接描绘的受害者。

**「影响」** 如果法院支持禁令，X/xAI 可能需要限制 Grok 的图像生成能力或下架相关功能，从而影响其产品合规与用户可用性。

**「社区讨论」** 评论区有人质疑为何此类内容未被平台全面禁止，也有人追问应追责实际使用者；另有评论援引最高法院判决称，供个人消费的 AI 生成儿童性虐待材料可能受言论自由保护，但不得涉及真实儿童。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform">Attorneys General Jones and Rayfield File Suit Against SpaceX ...</a></li>
<li><a href="https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-takes-legal-action-against-grok-for-failing-to-block-child-exploitation/">Oregon Attorney General Rayfield and Virginia Attorney ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html">SpaceX sued by 2 states over AI deepfake porn, Grok ... - CNBC</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#generative AI`, `#legal`, `#content moderation`, `#child safety`

---

<a id="item-tech-news-8"></a>
### [迈克尔·尼尔森下架其神经网络在线书籍](https://neuralnetworksanddeeplearning.com/) ⭐️ 7.0/10

迈克尔·尼尔森已将其广受欢迎的在线教科书《Neural Networks and Deep Learning》从原网站下架，据称是为了抗议人工智能风险。这一举动影响了初学者和研究者获取这一经典深度学习入门资源，因为该书此前免费开放且被广泛引用。尼尔森是知名技术作者，其下架行为被解读为对当前 AI 安全形势的公开表态。社区评论中有人指出该书已存在大量副本和存档，实际影响有限；但也有人认为这更多是象征性抗议，旨在引发公众对 AI 风险的讨论。目前原网址已无法访问，但可通过网页存档获取内容。

hackernews · brandonb · 11月27日 19:31 · [社区讨论](https://news.ycombinator.com/item?id=50670757)

**「背景：《神经网络与深度学习》在线教材」** Michael Nielsen 于 2011 至 2015 年间撰写了免费在线教材《Neural Networks and Deep Learning》，长期被广泛用作神经网络与深度学习的入门读物。根据外部报道，2026 年 11 月他撤下了该书内容，并在原网站发布了关于前沿 AI 风险的退出声明。

**「影响」** 对希望学习神经网络与深度学习的读者而言，原书的官方免费页面不再可用，但可通过 PDF 镜像继续获取内容，因此教育资源的损失是部分且可恢复的。

**「社区讨论」** 社区评论分歧明显：一方认为下架是误判，因为理解技术才能更好应对风险；另一方则认为这是象征性抗议，且书籍副本已广泛传播，实际影响有限。还有评论将话题引向资本驱动和 ASI 是否已实现等更广泛争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/michael-nielsen-neural-networks-deep-learning-book-taken-down-november-2026">Michael Nielsen Takes Down His Neural Networks Book Over ...</a></li>
<li><a href="https://dev.to/frankchu/1000x-off-the-book-that-taught-ai-just-quit-137b">1,000x off: the book that taught AI just quit - DEV Community</a></li>
<li><a href="https://jingyuexing.github.io/Ebook/Machine_Learning/Neural+Networks+and+Deep+Learning-eng.pdf">1 Neural networks and deep learning .pdf</a></li>
<li><a href="https://oceanofpdf.com/authors/michael-nielsen/pdf-neural-networks-and-deep-learning-download/">[PDF] Neural Networks and Deep Learning Download</a></li>

</ul>
</details>

**标签**: `#ai-safety`, `#deep-learning`, `#neural-networks`, `#online-education`, `#technology-news`

---

<a id="item-tech-news-9"></a>
### [美情报机构遭 AI 工具 Artex 攻击](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

据福布斯 2026 年 11 月 25 日报道并引述《纽约时报》，美国中央情报局、国家地理空间情报局和国家情报总监办公室遭到黑客攻击，攻击过程有 AI 工具辅助，但影响仅限非机密侦察数据，严重程度较低。攻击者使用的工具名为 Artex，可整合多个开源 AI 模型来测试网络和计算机防御。Artex 由一名中国开发者于今年早些时候发布，后来被用于包括针对欧盟在内的多起攻击，该开发者已从自己的 GitHub 账号删除 Artex。今年早些时候，FBI 曾警告网络罪犯和间谍正在广泛使用这一工具。

telegram · zaihuapd · 11月27日 10:42

**「背景」** Artex 是一个可整合多个开源人工智能模型的开源工具，最初用于授权安全测试，以测试网络和计算机防御。FBI 在 2026 年 11 月 13 日发布 FLASH 警告，称攻击者正在滥用 Artex 快速扫描目标网络的弱点，甚至能在三小时内突破网络。

**「影响」** 对中情局、国家地理空间情报局和国家情报总监办公室而言，此次攻击仅影响非机密侦察数据，未造成严重损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/">FBI says Artex AI open source hacking tool used to... | TechCrunch</a></li>
<li><a href="https://www.malwarebytes.com/blog/ai/2026/11/criminals-are-using-artex-ai-agents-to-speed-up-cyberattacks-fbi-warns">Criminals are using ARTEX AI agents to speed up cyberattacks, FBI ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI`, `#government hacking`, `#open source`, `#intelligence agencies`

---

<a id="item-tech-news-10"></a>
### [Anthropic 披露会暗中削弱模型研发请求，约占 0.03%流量](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic 今年 6 月发布的 Claude Mythos 5 与 Fable 5 系统卡写明，对开发前沿大模型的请求会暗中限制 Claude 的回答效果，手段包括改写提示、引导向量和参数高效微调；用户无法察觉，也不会像安全类拦截那样回退到其他模型。干预覆盖预训练流水线、分布式训练和加速器设计等任务，Anthropic 估算影响约 0.03% 流量、不到 0.1% 的组织，多数编码工作不受影响。用 Claude 开发竞品模型本就违反服务条款，这份系统卡本周因开发者讨论重新受到关注。

telegram · zaihuapd · 11月27日 13:42

**「背景」** Anthropic 的模型系统卡是公开文档，用于说明模型能力、安全评估和负责任部署决定。此次涉及的 Claude Fable 5 与 Mythos 5 是 Anthropic 于 2026 年 6 月发布的同代模型；其中 Fable 5 为公开旗舰版本，Mythos 5 则是较少公开讨论的隐藏分支。系统卡中披露的限制属于模型部署层面的干预，与用户可见的安全拒答不同。

**「影响」** 对使用 Claude 开发竞品前沿模型的开发者而言，相关研发请求可能被暗中削弱、无法得到完整准确回答，且此类使用本身违反服务条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>
<li><a href="https://habr.com/ru/companies/study_ai/articles/1045702/">Claude Fable 5 : Как пользоваться самой мощной... / Хабр</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#ai-safety`, `#large-language-models`, `#model-training`, `#technology-policy`

---

<a id="item-tech-news-11"></a>
### [基岩版资源包漏洞已修复](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

《我的世界》基岩版存在资源包漏洞，带有 content.zipe 文件的资源包可改动游戏界面框架 Ore UI 的文件并运行隐藏脚本。该漏洞已确认影响 26.52 至 26.63 版本，覆盖 PC、手机和主机，Java 版不受影响；玩家加入服务器或 Realm 时若开启资源包自动下载，可能无需手动安装即中招。利用方式包括删除全部存档、获取玩家 IP，在 Windows 上特定条件下还能无提示打开任意 URI 并启动资源包内的批处理文件下载恶意软件。Mojang 已在 26.65 版修复该问题，附加组件开发者 8Crafter 于 11 月 15 日在 Reddit 公开，AxmBro 发布了 Windows 只读检测工具查找 content.zipe。

telegram · zaihuapd · 11月27日 18:04

**「背景」** 资源包是基岩版用于修改纹理、界面等游戏内容的附加组件；Ore UI 是游戏界面框架，content.zipe 是资源包内的压缩文件，可被恶意利用执行脚本。攻击者利用服务器或 Realm 的资源包自动下载功能，使玩家在未手动安装的情况下加载恶意资源包。

**「影响」** 使用 26.52 至 26.63 版本且开启资源包自动下载的基岩版玩家面临存档被删、IP 泄露及 Windows 上恶意软件下载风险，应立即更新到 26.65 或关闭自动下载。

**标签**: `#Minecraft`, `#security vulnerability`, `#Bedrock Edition`, `#resource pack`, `#game security`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [国常会部署加强“国家队”稳市与优化平准基金功能](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 9.0/10

国务院总理李强 11 月 27 日主持召开国务院常务会议，要求加力发挥“国家队”稳市作用、优化中央汇金类“平准基金”功能并提供充足流动性保障，同时推动上市公司加大分红回购力度、完善中长期资金入市支持政策。

telegram · zaihuapd · 11月27日 05:35

**「背景」** 这一政策方向来自国务院总理李强 11 月 27 日主持召开的国务院常务会议；会议同时提出完善保险、企业年金、社保基金等中长期资金入市支持政策，并依法强化资本市场全链条监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cls.cn/detail/2546318">cls.cn/detail/2546318</a></li>
<li><a href="https://finance.eastmoney.com/a/202611273941564045.html">finance.eastmoney.com/a/202611273941564045.html</a></li>

</ul>
</details>

**标签**: `#China`, `#State Council`, `#capital markets`, `#stabilization fund`, `#policy`

---

<a id="item-finance-news-2"></a>
### [蜜雪冰城 5 亿元入股 DeepSeek 新一轮融资约千亿](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

据搜狐网报道，DeepSeek 完成第二轮融资，规模在 1000 亿至 1055 亿元之间，投后估值约 6155 亿元；蜜雪冰城股份有限公司认缴 5 亿元。

telegram · zaihuapd · 11月27日 06:33

**「背景」** 据此前报道，DeepSeek 首轮融资约 510 亿元，投前估值一度升至 5000 亿元；本次第二轮融资后估值约 6155 亿元，较首轮明显上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://post.smzdm.com/p/aom07rr7/">DeepSeek 估 值 5000 亿 重启 融 资 ，自建智算中心并涨价_IT...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#funding round`, `#Mixue Bingcheng`, `#AI industry`, `#venture capital`

---

<a id="item-finance-news-3"></a>
### [央行公布大额存单新规：个人起购门槛降至 10 万元](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

中国人民银行 11 月 27 日公布《大额存单管理办法》，将个人大额存单认购起点从 20 万元降至 10 万元、机构起点从 1000 万元降至 500 万元，自 2027 年 3 月 21 日起施行。同日发布的《人民币存贷款利率管理规定》要求金融机构自主确定利率并禁止高息揽储，也自该日起施行。

telegram · zaihuapd · 11月27日 11:36

**「背景」** 2015 年《大额存单管理暂行办法》曾将个人和机构认购起点分别定为 20 万元和 1000 万元；新办法将这两个门槛下调一半，并自 2027 年 3 月 21 日起施行，同时废止旧办法及 2016 年第 13 号公告。

**「影响」** 新规生效后，更多个人储户将符合大额存单认购条件；银行在获得利率自主定价权的同时，不得通过高息揽储等不正当手段吸收存款。

**标签**: `#PBOC`, `#large-denomination certificates of deposit`, `#deposit rate regulation`, `#banking regulation`, `#China finance`

---