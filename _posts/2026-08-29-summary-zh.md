---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 36 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [OpenAI 就 Cursor 被 SpaceX 收购后的 API 政策作出决定](#item-tech-news-1) ⭐️ 8.0/10
2. [美国将意大利托管组织 Autistici/Inventati 列为恐怖分子并制裁](#item-tech-news-2) ⭐️ 8.0/10
3. [智谱开源 GLM-5.3：主打智能体编程与网络防御](#item-tech-news-3) ⭐️ 8.0/10
4. [仅凭漏洞传言，AI 代理即可开发安全漏洞利用](#item-tech-news-4) ⭐️ 8.0/10
5. [Triton 3.8.0 发布：新聚合类型与 topk 降序参数](#item-tech-news-5) ⭐️ 7.0/10
6. [htmx 4.0.0 发布：超媒体驱动 Web 开发库新主要版本](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenAI Python SDK 迁移至 HTTPX2 以避免 httpx 1.0 破坏性变更](#item-tech-news-7) ⭐️ 7.0/10
8. [RP2350 微控制器实现微型潜流 Transformer 人脸生成](#item-tech-news-8) ⭐️ 7.0/10
9. [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [两部门将个人住房贷款最长期限由 30 年延长至 40 年](#item-finance-news-1) ⭐️ 9.0/10
2. [玉米和小麦期货价格升至三年多来最高](#item-finance-news-2) ⭐️ 8.0/10
3. [美国第九巡回上诉法院裁定体育事件合约属体育博彩，最高法院之争可能性增大](#item-finance-news-3) ⭐️ 7.0/10
4. [美元兑日元重回 160，日美干预效果回撤](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 就 Cursor 被 SpaceX 收购后的 API 政策作出决定](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10

OpenAI 发布声明，说明其在 Cursor 被 SpaceX 收购后对 API 访问作出的政策决定。根据提供的分析，该决定将影响 AI 编程工具 Cursor 的用户通过其平台访问 OpenAI 模型的能力。社区评论指出，这一举措在预期之内：Cursor 长期转售第三方模型 API，而被收购后与自有模型（评论中提及 Grok/Composer）形成竞争；另有评论提到 Anthropic 此前已因类似服务条款问题禁止 xAI。由于源正文不可用，具体限制范围、生效时间、是否完全切断等细节未在提供材料中明确。

hackernews · meetpateltech · 8月29日 01:47 · [社区讨论](https://news.ycombinator.com/item?id=49486172)

**「背景」** Cursor 是 Anysphere 开发的 AI 编程工具，OpenAI 与其合作近四年，并向 Cursor 提供 OpenAI 模型 API。SpaceX 本月以 600 亿美元全股票交易正式收购 Cursor，这是有史以来最大的风投支持的初创公司收购案；该交易使 Cursor 可使用 SpaceX 的算力并接入 xAI 的 Grok 模型，从而停止向 OpenAI 和 Anthropic 支付模型费用。OpenAI 表示，合作协议包含收购后的“有限时间窗口”取消条款，因此决定终止合作。

**「社区讨论」** 社区评论普遍认为这一决定在预期之内，因 Cursor 转售第三方模型 API 的商业模式与收购方自有模型（评论中提及 Grok/Composer）存在冲突；有用户表示会因此减少在 Cursor 中使用 OpenAI 模型、转向 Anthropic，也有用户认为 Cursor 搭配 Grok/Composer 已足够，无需第三方模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://www.businessinsider.com/openai-ends-cursor-contract-elon-musk-spacex-sam-altman-feud-2026-8">OpenAI Ending Deal With Cursor Because XAI... - Business Insider</a></li>
<li><a href="https://businessmodelanalyst.com/spacex-cursor-acquisition-office/">SpaceX Buys Cursor for $60B, a Record Startup Exit</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cursor`, `#OpenAI`, `#API`, `#developer tools`

---

<a id="item-tech-news-2"></a>
### [美国将意大利托管组织 Autistici/Inventati 列为恐怖分子并制裁](https://www.inventati.org/) ⭐️ 8.0/10

美国政府将意大利托管组织 Autistici/Inventati（A/I Collective）指定为“全球恐怖分子”并实施制裁。该组织运营着 noblogs.org 等隐私导向的托管服务，此次制裁被指史无前例，因为它直接针对基础设施提供者。此举引发了关于隐私工具和开源基础设施风险的广泛讨论，涉及 I2P、Monero、Veilid、Tox、Signal 等项目的用户和开发者是否可能被连带视为恐怖分子。

hackernews · exiguus · 8月28日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49477854)

**「背景」** Autistici/Inventati（A/I）是一家意大利科技集体，以提供隐私保护托管服务闻名，包括 noblogs.org 匿名博客平台及邮件、VPN 等工具。此次制裁援引的第 13224 号行政令是美国主要反恐制裁机制，允许冻结被列名实体的资产并禁止美国主体与其交易；美方声明称其服务被所谓极左翼和反法西斯网络使用，但具体证据存在争议。

**「影响」** 依赖 Autistici/Inventati 提供的安全邮件、网站托管和视频会议服务的用户，可能因该组织被美国列为全球恐怖主义实体而面临服务中断或合规风险。

**「社区讨论」** 社区普遍担忧这一先例可能使隐私工具的用户和开发者面临“恐怖分子”连带指控，并讨论了对 I2P、Monero 等项目的潜在影响。部分评论者质疑该组织与 PKK 的关联缺乏可验证证据，并指出 autistici.org 已下线、noblogs.org 部分功能异常，而另一些评论则提供了该组织在热那亚抗议期间的历史背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/us-sanctions-autistici-inventati-terrorism/">United States sanctions Autistici / Inventati for supporting far-left...</a></li>
<li><a href="https://www.radiorebelde.cu/english/u-s-designates-palestine-action-masar-badil-and-autistici-inventati-as-terrorist-groups-26082026/">U . S . Designates Palestine Action, Masar Badil, and Autistici Inventati ...</a></li>
<li><a href="https://www.zerohedge.com/markets/us-sanctions-3-groups-accused-supporting-far-left-terrorism">US Sanctions 3 Groups Accused Of Supporting Far-Left... | ZeroHedge</a></li>
<li><a href="https://www.heraldousa.com/usnews/2026/8/26/marco-rubio-warns-of-far-left-terrorism-and-announces-sanctions-36792.html">Marco Rubio warns of &#x27;far-left terrorism&#x27; and announces sanctions</a></li>
<li><a href="https://www.linkedin.com/feed/update/urn:li:activity:7498405566512406528/">US sanctions this morning against an Italian IT developer that...</a></li>

</ul>
</details>

**标签**: `#sanctions`, `#internet-freedom`, `#privacy`, `#hosting`, `#tech-policy`

---

<a id="item-tech-news-3"></a>
### [智谱开源 GLM-5.3：主打智能体编程与网络防御](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 8.0/10

智谱 AI 已开源 GLM-5.3 权重，可在 Hugging Face 等平台下载和定制。该模型与 GLM-5.2 共用同一基础模型，全部提升来自后训练，重点增强智能体编程和网络防御能力。官方博客显示其在 Terminal Bench 2.1 得分为 88.2，DeepSWE 得分为 66.9，均大幅领先 GLM-5.2。GLM-5.3 采用自定义 GLM-5.3 License，允许个人与中小企业自由使用、微调与商用；对连续 12 个月营收超过 100 亿美元且对外提供模型的主体设有额外限制（原文未完整给出）。社区初步反馈认为其运行门槛低于 Kimi，并在随机复杂问题上表现出比 DeepSeek 4 Flash 更好的直觉。

hackernews · jeudesprits · 8月28日 15:20 · [社区讨论](https://news.ycombinator.com/item?id=49479878)

**「背景」** GLM-5.3 是智谱 AI（Z.ai）发布的开放权重语言模型，参数量约 743B，于 2026 年 8 月 14 日上传至 Hugging Face。此前该模型已通过 API 先行推出，并在完成约两周的安全评估后开放权重。其采用分层许可证，个人和中小企业可自由使用、微调与商用，但连续 12 个月营收超过 100 亿美元且对外提供模型服务的大型云厂商受到商业限制。

**「影响」** 对于需要自托管或本地部署开源模型的开发者，GLM-5.3 在 Terminal Bench 2.1 和 DeepSWE 上分别达到 88.2 和 66.9，并提供个人与中小企业友好的商用许可，成为比 GLM-5.2 更实用的开放权重选项。

**「社区讨论」** 社区反馈总体正面：多位用户称其在复杂任务上比 DeepSeek 4 Flash 更有直觉，运行成本/门槛低于 Kimi，甚至有人感觉像 Opus 4.8。不过也有用户提醒，在高度复杂数据分析任务中，Qwen3.8、GLM-5.2 等模型可能输出过多思考 tokens，需关注 token 与准确率的权衡；GLM-5.3 的该指标被初步认为有前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.llms.blog/posts/z-ai-releases-flagship-glm-5-3-open-weights-with-hyperscaler-commercial-restrictions">Z.ai Releases Flagship GLM-5.3 Open Weights with Hyperscaler ...</a></li>
<li><a href="https://aireleasetracker.com/model/zai/glm-5.3">GLM-5.3 — Benchmarks, Specs &amp; Release Date</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#open-weight`, `#artificial-intelligence`, `#machine-learning`, `#software-engineering`

---

<a id="item-tech-news-4"></a>
### [仅凭漏洞传言，AI 代理即可开发安全漏洞利用](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 8.0/10

剑桥大学教授兼 OCaml 编译器核心维护者 Anil Madhavapeddy 报告，OCaml 项目的安全补丁在公开讨论后约十分钟内就收到针对百分号编码遍历序列的探测，表明自动化监控着公共仓库。现代 AI 编程代理仅凭漏洞传言就能定位缺陷，Anil 使用自己的代理演示了这一过程，并在 Claude Fable 拒绝时切换至 DeepSeek V4 Pro。rclone 维护者 Nick Craig-Wood 确认，该项目过去十年仅约 20 份安全披露，最近一个月却超过 40 份，其中约 75%包含需要关注的内容。GitHub CVE 分配从原来的 2-3 天延长至 3-4 周，导致 rclone 只能在更新日志中标注 CVE-PENDING 发布。Anil 认为这种攻击速度与现有开源漏洞保密流程不兼容，需要新流程保护社区。

rss · Simon Willison · 8月28日 22:12

**「背景」** 传统的开源漏洞处理依赖保密期，在补丁公开前给维护者时间修复；公共仓库的补丁讨论曾被认为不会立即引发攻击。AI 编程代理能够快速分析代码和补丁，将模糊线索转化为可用的漏洞利用，从而缩短了从披露到攻击的时间窗口。

**「影响」** 开源维护者正面临安全披露数量激增和 CVE 分配延迟的双重压力，不得不发布带有 CVE-PENDING 标记的版本，用户可能无法及时获得明确的漏洞编号和修复状态。

**「社区讨论」** 评论区中维护者确认安全披露负担剧增；有观点认为利用 LLM 从补丁或只言片语中推断漏洞并非全新，只是规模化和民主化到低价值目标，也有人担忧自动更新和供应链攻击风险，并提到已有工具监控提交以检测静默修复。

**标签**: `#security`, `#AI coding agents`, `#open source security`, `#vulnerability exploitation`, `#OCaml`

---

<a id="item-tech-news-5"></a>
### [Triton 3.8.0 发布：新聚合类型与 topk 降序参数](https://github.com/triton-lang/triton/releases/tag/v3.8.0) ⭐️ 7.0/10

Triton v3.8.0 正式发布，@triton.aggregate 和 @gluon.aggregate 成为公共 API，支持继承字段、默认值、生成构造函数、不可变实例和 aggregate\_replace\(\)（\#10095、\#9572）。tl.topk 新增 descending 参数，设置 descending=False 可返回最小值（\#9355）。张量描述符现可在元组值内核参数中传递（\#9422），解释器新增 tl.dot\_scaled 支持（\#10311）。后端方面，通用 multi-CTA 支持扩展到布局转换、归约、本地 gather/scatter、TMA gather/scatter 和 multicast，tma.store\_wait 增加 read\_only 参数，默认 True（\#10415、\#10419）。此外，JIT 缓存键改为确定性生成（\#10494），自动调优新增监听器（\#10125），并加入 FpSan、GSan、ConSan 等诊断工具和 AMD gfx1250 的多项改进。

github · warrendeng · 8月28日 18:25

**「背景」** Triton 是一个面向 GPU 的 Python DSL 和编译器，广泛用于 PyTorch、LLM 推理等 AI/ML 工作负载的高性能内核开发。聚合类型允许在 Triton 内核中定义结构化字段，而 topk 常用于注意力机制中的稀疏选择。此次发布延续了其对 NVIDIA 与 AMD 后端的支持，并针对 CDNA5/gfx1250 等新硬件推进编译与内存路径。

**「影响」** 内核开发者现在可以直接使用公共聚合类型组织 GPU 状态，并通过 tl.topk\(descending=False\) 更简洁地实现最小 top-k 选择，同时 AMD gfx1250 上的 TDM/WMMA/warp pipelining 支持扩大了可部署硬件范围；不过 FpSan、GSan、ConSan 仍处于实验或新增阶段，需按目标架构验证。

**标签**: `#GPU`, `#compiler`, `#AI`, `#machine learning`, `#open source`

---

<a id="item-tech-news-6"></a>
### [htmx 4.0.0 发布：超媒体驱动 Web 开发库新主要版本](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 7.0/10

htmx 4.0.0 已发布，这是该超媒体驱动 Web 开发库的一个新主要版本。该版本延续了 htmx 通过服务端渲染 HTML 实现动态界面、避免复杂客户端 JavaScript 的理念。社区反馈特别提到新增的 \`hx-alpine-compat\` 扩展，用于平滑 htmx 与 Alpine.js 之间的兼容性问题。官方详细变更日志未在提供的源内容中给出，但此次发布对构建轻量、以服务端为中心的 Web 应用的用户来说是一个重要里程碑。

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**「背景」** htmx 是一个超媒体驱动的 Web 开发库，4.0 版本是该库的一次重大更新。根据官方公告，4.0 从 XMLHttpRequest 转向 Fetch API，新增 :inherited 修饰符用于显式属性继承，并原生支持流式传输。此外，4.0 内置了基于 idiomorph 算法改进的 morphing 交换（morphing swaps）。

**「影响」** 开发者现在可以升级到 htmx 4.0.0，同时使用 Alpine.js 的用户可能受益于新的 \`hx-alpine-compat\` 兼容层；但由于缺少详细变更日志，升级前应验证是否存在破坏性变更。

**「社区讨论」** 评论总体积极，用户称赞 htmx 的简洁性和有机发展，并期待在新项目中使用；也有相反观点指出 htmx 的服务端生成 UI 会将展示逻辑与业务逻辑混合，可能不适合习惯 API 与前端分离架构的团队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released">htmx 4.0.0 has been released! ~ htmx</a></li>
<li><a href="https://app.daily.dev/posts/announcing-htmx-4-0-embracing-the-fetch-api-and-modern-enhancements-mxhcluue6">Announcing htmx 4.0: Embracing the Fetch API and Modern Enhancements | daily.dev</a></li>

</ul>
</details>

**标签**: `#htmx`, `#hypermedia`, `#web development`, `#open source`, `#frontend`

---

<a id="item-tech-news-7"></a>
### [OpenAI Python SDK 迁移至 HTTPX2 以避免 httpx 1.0 破坏性变更](https://github.com/openai/openai-python/blob/main/httpx2.md) ⭐️ 7.0/10

OpenAI 的 Python SDK 在仓库文档 httpx2.md 中记录了向 HTTPX2 的迁移，HTTPX2 是一个承诺不破坏现有 API 的 httpx fork。这一变更旨在避开 httpx 正在推进的 1.0 版本中预计出现的破坏性改动，使 SDK 的依赖更稳定。社区讨论指出，Anthropic 在 OpenAI 之后数周也对其 Python SDK 做了相同调整，并认为 HTTPX2 作为稳定 fork 更适合作为依赖。公开信息未提供具体迁移版本或时间表。

hackernews · tosh · 8月28日 11:51 · [社区讨论](https://news.ycombinator.com/item?id=49477212)

**「背景」** OpenAI Python SDK 现已改用 HTTPX2 作为同步和异步 HTTP 客户端，该包会随 openai 自动安装，取代原先的 httpx 依赖。这一迁移旨在规避 httpx 在向 1.0 版本演进过程中可能引入的破坏性变更；HTTPX2 是 httpx 的一个分叉，承诺保持现有 API 稳定，从而为依赖它的库提供更可靠的长期基础。

**「影响」** 对于依赖 OpenAI Python SDK 的 Python 项目，此迁移会把底层 HTTP 客户端依赖切换到 HTTPX2，从而降低 httpx 1.0 破坏性变更带来的风险。

**「社区讨论」** 社区评论认为该迁移能带来更稳定的依赖，并提到 Anthropic 已跟进；但也有人询问是否评估过 niquests 等替代方案，并质疑此变更的具体收益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/openai-python/blob/main/httpx2.md">openai-python/httpx2.md at main - GitHub</a></li>

</ul>
</details>

**标签**: `#python`, `#openai`, `#http`, `#sdk`, `#dependency-management`

---

<a id="item-tech-news-8"></a>
### [RP2350 微控制器实现微型潜流 Transformer 人脸生成](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 7.0/10

一位开发者在 RP2350 微控制器上实现了一个参数规模为 240 万至 400 万的潜流 Transformer 图像生成模型，可生成 128×128 人脸图像，并量化到 int8。该模型包含 12 层，使用 AdaLN-Zero 进行条件控制，并支持 CFG（分类器自由引导），在最长生成设置下约 20 秒完成推理。推理引擎通过 DMA 从闪存流式传输权重，同时计算上一层，并利用 ReLU²激活提高稀疏性以跳过计算。作者经过大量消融实验才达到这一效果，并计划发布代码仓库。

reddit · r/MachineLearning · /u/cpldcpu · 8月28日 19:48

**「背景」** RP2350 是 Raspberry Pi 推出的微控制器，相比前代 RP2040 具备更高的内核时钟、翻倍的片上 SRAM 与闪存，并提供双核 Arm Cortex-M33 与 Hazard3 RISC-V 核心可选。Latent Flow Transformer（LFT）是一种结合流匹配概念的 Transformer 架构，已被用于图像与视频生成/编辑任务。在该项目中，开发者将这种架构压缩为 2.4–4M 参数、int8 量化后部署到 RP2350 上，并对权重流式加载与稀疏激活等优化做了适配。

**「影响」** 这一实现证明了在资源受限的微控制器上可运行微型生成式 Transformer，为边缘端低功耗人脸图像生成提供了可行参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sparkfun.com/rp2350">RP2350 - The latest microcontroller from Raspberry Pi ... Buy an RP2350 – Raspberry Pi RP2350 Datasheet - Microcontroller | Raspberry Pi Microcontroller chips - Raspberry Pi Documentation RP2350 Datasheet - Microcontroller IC - English Technical ...</a></li>
<li><a href="https://www.emergentmind.com/topics/latent-flow-transformers-lft">Latent Flow Transformers (LFT)</a></li>

</ul>
</details>

**标签**: `#edge-ai`, `#image-generation`, `#transformers`, `#model-optimization`, `#microcontrollers`

---

<a id="item-tech-news-9"></a>
### [腾讯混元发布 Hy4 preview，盲测得分略胜 GLM-5.3 与 Kimi K3](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 7.0/10

2026 年 8 月 28 日，腾讯发布开源大模型 Hy4 preview，采用混合专家（MoE）架构，总参数量 770B、活跃参数 49B，上下文窗口为 1M token，主攻长周期软件工程、文档办公与科学研究。该模型已上线腾讯云、GitHub、HuggingFace、ModelScope、AtomGit、OpenRouter 等渠道。在 203 项工程任务的盲评中，Hy4 preview 取得 2.99 分，略高于 GLM 5.3 的 2.92 分和 Kimi K3 的 2.94 分。API 定价为每 1M tokens 输入 0.834 美元、输出 2.501 美元。

telegram · zaihuapd · 8月28日 06:11

**「背景」** 腾讯混元团队发布的 Hy4 preview 属于新一代混合专家（MoE）旗舰模型：总参数 770B，但每个 token 只激活 49B，能在大规模容量与推理成本之间取得平衡。其上下文窗口达 1M token，面向编码、办公和科研等长周期任务，并已在 GitHub、Hugging Face 等平台开放权重。理解这一发布需要了解 MoE 架构中“总参数/活跃参数”的区别，以及 GLM、Kimi 等开源模型在工程任务盲评中的竞争背景。

**「影响」** 对需要长上下文和开源部署的软件工程团队，这提供了一个在盲评中略胜 GLM-5.3 与 Kimi K3 的可选模型，并能通过腾讯云、HuggingFace、ModelScope 等多渠道直接获取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent-Hunyuan/Hy4-preview</a></li>
<li><a href="https://www.aimodeling.com/en/news/slug/tencent-hy4-preview-770b-moe">Tencent open-sources Hy4 preview: 770B MoE, 1M context, and a ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open source`, `#Tencent`, `#software engineering`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [两部门将个人住房贷款最长期限由 30 年延长至 40 年](https://news.ifeng.com/c/8vxm6huJOMR) ⭐️ 9.0/10

中国人民银行和国家金融监督管理总局联合印发意见，将个人住房贷款最长期限由 30 年延长至 40 年，具体期限由购房人与商业银行协商确定。

telegram · zaihuapd · 8月28日 12:16

**「背景」** 此前个人住房贷款期限上限为 30 年；两部门称此次延长至最长 40 年是为适应经济社会发展需要、推动加快构建房地产发展新模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.com.cn/money/bank/bank_hydt/2026-08-28/doc-inipwnxp9005397.shtml">两部门：将个人住房贷款期限由最长30年延长至最长40年_新浪财经_新浪网</a></li>

</ul>
</details>

**标签**: `#housing policy`, `#mortgage`, `#China`, `#real estate`, `#regulation`

---

<a id="item-finance-news-2"></a>
### [玉米和小麦期货价格升至三年多来最高](https://www.cnbc.com/2026/08/28/corn-and-wheat-prices-jump-to-highest-prices-in-more-than-three-years.html) ⭐️ 8.0/10

玉米和小麦期货价格跃升至三年多来最高：小麦周五收于每蒲式耳 784 美分，上涨 3.1%；玉米收于 536.5 美分，上涨 0.6%。

rss · CNBC Finance · 8月28日 20:00

**「背景」** 小麦上涨主要受黑海地区俄罗斯与乌克兰谷物出口中断担忧推动，而玉米上涨则源于美国供应预期收紧，美国农业部 8 月报告下调了玉米单产预估且作物巡查结果不佳。

**标签**: `#commodities`, `#wheat`, `#corn`, `#agriculture`, `#global trade`

---

<a id="item-finance-news-3"></a>
### [美国第九巡回上诉法院裁定体育事件合约属体育博彩，最高法院之争可能性增大](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

美国第九巡回上诉法院驳回了 Kalshi、Crypto.com 和 Robinhood 的禁令请求，裁定体育相关事件合约属于体育博彩，而非受美国商品期货交易委员会（CFTC）监管的互换（一种衍生品）；该裁决与第三巡回上诉法院的相反裁定形成分歧，使案件很可能进入最高法院。

rss · CNBC Finance · 8月29日 02:23

**「背景」** 预测市场平台与 CFTC 主张所有事件合约都是 CFTC 独家监管的互换，而 44 个州认为体育类事件合约就是体育博彩；今年 4 月初第三巡回上诉法院曾裁定只有 CFTC 拥有管辖权。

**「影响」** 该裁决使 Kalshi、Crypto.com 和 Robinhood 无法阻止内华达州叫停其体育相关事件合约，并加剧了 CFTC 与州博彩监管机构之间的管辖权不确定性。

**标签**: `#prediction markets`, `#CFTC`, `#sports betting`, `#regulation`, `#Supreme Court litigation`

---

<a id="item-finance-news-4"></a>
### [美元兑日元重回 160，日美干预效果回撤](https://www.reuters.com/world/asia-pacific/dollar-flat-near-one-week-high-investors-await-warshs-jackson-hole-debut-2026-08-28/) ⭐️ 7.0/10

美元兑日元重新升破 160，回吐了此前日美联合干预后从接近 164 回落至 158 附近的日元升值成果；直接催化剂是美联储主席沃什在杰克逊霍尔的偏鹰讲话令市场提高 9 月加息预期。

telegram · zaihuapd · 8月29日 01:53

**「背景」** 此前日美联合干预汇市后，美元兑日元一度从接近 164 回落至 158 附近；最新一轮日元走弱发生在美联储主席沃什在杰克逊霍尔发表偏鹰讲话、市场提高 9 月加息预期之后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/28/treasury-yields-jackson-hole.html">Treasury yields tread water ahead of Warsh’s Jackson Hole speech</a></li>

</ul>
</details>

**标签**: `#USD/JPY`, `#currency intervention`, `#Federal Reserve`, `#Jackson Hole`, `#monetary policy`

---