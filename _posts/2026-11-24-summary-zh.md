---
layout: default
title: "Horizon Summary: 2026-11-24 (ZH)"
date: 2026-11-24
lang: zh
---

> 从 35 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [NariQ：10GB 文件实现 Qwen3.8-27B 近 BF16 量化](#item-tech-news-1) ⭐️ 8.0/10
2. [GLM-5.4：Zhipu 推出首个循环 Transformer 编程模型](#item-tech-news-2) ⭐️ 8.0/10
3. [Codex2api 疑似遭供应链投毒：恶意版本删鉴权并窃取机密](#item-tech-news-3) ⭐️ 8.0/10
4. [Anthropic 称 Claude 发现 VP≠VNP 并公开 Lean 4 证明](#item-tech-news-4) ⭐️ 8.0/10
5. [英伟达董事会恢复黄仁勋总裁兼 CEO 职务](#item-tech-news-5) ⭐️ 7.0/10
6. [Stalwart 宣布成为 Exchange 即插即用替代品](#item-tech-news-6) ⭐️ 7.0/10
7. [Ladybird 浏览器进入 alpha 阶段](#item-tech-news-7) ⭐️ 7.0/10
8. [ChatGPT 聊天页上线 GPT-6.2 Sol](#item-tech-news-8) ⭐️ 7.0/10
9. [黎曼猜想 AI 证明被指空转](#item-tech-news-9) ⭐️ 7.0/10
10. [4.5 万企业组织致信欧盟要求调查苹果浏览器限制](#item-tech-news-10) ⭐️ 7.0/10
11. [黄循财：不做芯片管制规避通道](#item-tech-news-11) ⭐️ 7.0/10

**科技博客**
1. [vLLM 对 ERNIE 5.5 Flash Preview 的 Day-0 支持与推理加速](#item-tech-blog-1) ⭐️ 8.0/10

**财经新闻**
1. [Anthropic IPO 引发抛售，中国 AI 公司上市计划蒙上阴影](#item-finance-news-1) ⭐️ 8.0/10
2. [英伟达董事会全票恢复黄仁勋 CEO 职务，称无国家安全风险](#item-finance-news-2) ⭐️ 8.0/10
3. [上海地铁票价时隔 21 年首次调整，新票价 12 月 1 日起实施](#item-finance-news-3) ⭐️ 7.0/10
4. [SpaceX 被曝向 Anthropic、Google 出租 AI 算力，月入数十亿美元](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [NariQ：10GB 文件实现 Qwen3.8-27B 近 BF16 量化](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

NariQ 发布了 Qwen3.8-27B 的 3-bit 及更低比特量化版本，文件约 10GB，并声称在长程智能体、数学、多语言推理和图像理解任务上保持接近 BF16 的水平。其基准显示，3-bit 在 DeepSWE 上为 41.0（BF16 为 39.8）、Terminal-Bench 2.1 为 63.8（BF16 为 62.6）、AIME 25+26 为 98.3（BF16 为 97.7），2.5-bit 多数指标也接近，2-bit 则明显下降。在 RTX PRO 6000 上解码速度与其他量化相当，但 64K 上下文下吞吐从 4K 的 88.9 降至 70.7（3-bit）。运行需使用其 llama.cpp fork，Mac M3 Pro 18GB 上 3-bit 解码约 3.8 tok/s，明显慢于 CUDA。

hackernews · toebee · 11月23日 13:42 · [社区讨论](https://news.ycombinator.com/item?id=50611402)

**「背景」** 量化通过降低权重数值精度来压缩模型大小，通常会在模型能力上做出权衡。Qwen3.8-27B 是近期开源的 27B 参数大语言模型，其 BF16 原始权重体积庞大，难以在常见本地硬件上运行。NariQ 的目标是在约 10GB 以内提供可用的低比特版本。

**「影响」** 对本地部署 Qwen3.8-27B 的用户，3-bit 版本在约 10GB 文件内提供了接近 BF16 的编码、数学和多语言推理指标，但必须使用 Nari Labs 的 llama.cpp fork，且 Apple Silicon 上的解码速度明显低于 CUDA 环境。

**「社区讨论」** 社区既有认可也有质疑：有评论肯定其覆盖多种长程任务并提及留出集检查，但也有人担心基于 QAT 的量化会过度拟合基准、指出部分提升可能来自评测程序差异，并关注低比特量化具体丢失了哪些信息。

**标签**: `#quantization`, `#LLM`, `#open-source`, `#AI-inference`, `#Qwen`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4：Zhipu 推出首个循环 Transformer 编程模型](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Zhipu 发布 GLM-5.4，宣称是其首个面向通用编程的循环 Transformer 模型。与传统 Transformer 将每一层权重依次计算一次不同，该模型在推理中循环复用同一组权重，以减少 HBM 到芯片的权重搬运，从而缓解内存带宽这一主要推理瓶颈。这一设计旨在提升编程任务的推理效率，但具体版本日期、模型规模和基准成绩未在本次来源中披露。

hackernews · foohis · 11月23日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50609685)

**「背景：GLM-5.4 与循环 Transformer」** GLM-5.4 是 Z.ai 最新旗舰模型，也是该公司首款采用循环 Transformer（Loop Transformer）架构的模型，官方称其智能水平可与 2T–3T 参数量的模型相媲美。该模型被视为 Z.ai ‘泛化编码’（Generalized Coding）方向的起点，即以代码作为解决更广泛任务并解锁新能力的基础。

**「影响」** 需要使用 GLM-5.4 的开发者必须订阅 Z.ai 的 Coding Plan 并获取专用 API 密钥，因为该模型未通过 OpenRouter 或 Z.ai 常规 API 计划提供；同时需注意模型可能在简单任务上出现长时间“马拉松式思考”，完成时间高于部分前沿模型。

**「社区讨论」** 社区赞赏 Zhipu 提供技术细节的透明度，认为循环 Transformer 是自然方向；同时有开发者批评中国模型普遍存在的“马拉松式思考”，在简单任务上反复自我质疑，导致完成时间大幅增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ... - z.ai</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM-5.4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.online-tech-tips.com/zai-glm-5-4-loop-transformer/">Z.ai releases GLM-5.4 with a Loop Transformer architecture</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#coding`, `#transformer architecture`

---

<a id="item-tech-news-3"></a>
### [Codex2api 疑似遭供应链投毒：恶意版本删鉴权并窃取机密](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

Codex2api 作者的账号被入侵，攻击者绕过 main 分支直接推送 tag，使 Release 构建出带后门的版本。恶意版本 v3.1.11 移除了鉴权，相当于允许无密码远程执行命令；同时有 workflow 将仓库的 16 个 GitHub Actions secrets 外传，波及同账号下至少 21 个仓库。已安装或更新到 3.1.10–3.1.12 的用户应立即停用并退回 3.1.9，同时轮换 GitHub token、SSH key、数据库和 DeepSeek 等所有相关密钥。

telegram · zaihuapd · 11月23日 11:21

**「背景」** 软件供应链攻击常通过攻破维护者账号或仓库权限，向看似正常的发布版本注入恶意代码；在 GitHub 生态中，攻击者还会滥用 GitHub Actions 工作流窃取仓库机密。此类事件此前已在 GitHub Actions、Gravity Forms 和 npm 等渠道中多次出现，提示发布通道和 CI/CD 凭证需要额外防护。

**「影响」** 使用 Codex2api 3.1.10–3.1.12 的部署面临未授权远程命令执行和凭据泄露风险，应立即回退并轮换相关密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.darkreading.com/application-security/supply-chain-attacks-github-actions-gravity-forms-npm">Malware Spotted in GitHub Actions , Gravity Forms, npm</a></li>

</ul>
</details>

**标签**: `#supply-chain-attack`, `#open-source-security`, `#codex2api`, `#github-actions`, `#rce`

---

<a id="item-tech-news-4"></a>
### [Anthropic 称 Claude 发现 VP≠VNP 并公开 Lean 4 证明](https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md) ⭐️ 8.0/10

Anthropic 于 11 月 24 日公开论文《VP ≠ VNP over every field》及其 Lean 4 形式化证明，声称由内部研究用 Claude 模型发现并撰写。该工作给出哈密顿圈多项式的超多项式算术电路下界，进而推出 VP 是 VNP 的真子类；若成立将解决 Valiant 1979 年提出的代数复杂度猜想，但仅涉及算术电路，不涉及 P 与 NP。代码经三条标准公理审计和独立内核 nanoda 复核，除预留文件外无 sorry，但尚无人类数学家通读，且 Lean 无法确认形式化陈述与所声称命题一致，附录 Q 列出了出入，结果待独立审阅。

telegram · zaihuapd · 11月24日 06:02

**「背景」** VP 与 VNP 是代数复杂度理论中分别对应“易计算”与“易验证”的多项式族类，由 Leslie Valiant 于 1979 年提出；VP≠VNP 是该领域长期未解的核心猜想，常被视为 P≠NP 的代数类比，但仅涉及算术电路。Lean 4 是一种可对数学命题和证明进行机器检查的形式化系统，能独立验证证明是否无逻辑漏洞。

**「对代数复杂度与验证的影响」** 若该证明通过独立审阅，将确立 VP 是 VNP 的真子类，从而解决 Valiant 1979 年提出的代数复杂度猜想；目前尚无人类数学家通读验证，且 Lean 形式化无法保证其陈述与声称命题一致，因此结论仍待确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UuOiRi9T-9c">Claude &#x27;s VP VNP Proof : 47 Years Open, Still Unchecked... - YouTube</a></li>
<li><a href="https://www.alphaxiv.org/abs/2611.vp-vnp-arithmetic-lower-bounds">VP VNP Over Every Field | alphaXiv</a></li>
<li><a href="https://dzen.ru/a/awTKXMRU0TKYtlGb">Anthropic опубликовала доказательство неравенства VP VNP над...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#VP vs VNP`, `#computational complexity`, `#Lean 4`, `#AI-generated proof`

---

<a id="item-tech-news-5"></a>
### [英伟达董事会恢复黄仁勋总裁兼 CEO 职务](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 7.0/10

2026 年 11 月 23 日，英伟达（Nvidia）董事会宣布恢复黄仁勋的总裁、CEO 及董事职务。根据英伟达新闻稿和 CNBC 报道，这一决定是在董事会听取美国政府高级官员的意见后做出的；声明称，基于该意见，董事会确信黄仁勋的复职不构成国家安全风险。此前有报道称黄仁勋曾被董事会短暂罢免，本次复职意味着董事会立场迅速逆转。目前官方披露仍较有限，未说明此前变动的具体原因。

hackernews · jaz · 11月23日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=50611576)

**「背景」** 黄仁勋是英伟达（NVIDIA）联合创始人，长期担任总裁兼首席执行官，带领公司成为 AI 芯片领域的主导厂商。2026 年 11 月 23 日，英伟达董事会宣布立即恢复黄仁勋的总裁、首席执行官及董事职务，这一“复职”意味着他此前已被董事会解除这些职务。英伟达表示，该决定是在听取美国政府高层意见后做出的，并称基于该意见，董事会确信黄仁勋复职不构成国家安全风险。

**「影响」** 该决定使英伟达的最高管理层在短暂波动后恢复，AI 硬件客户与供应链面临的 CEO 空缺不确定性得到缓解。

**「社区讨论」** 社区讨论中，有人强调政府意见是声明的核心，并批评美国在出口管制上要求 ASML 和日本企业遵守制裁、却允许英伟达获得豁免的双重标准。另一些评论援引 Caremark 标准与司法部不起诉推断董事个人责任有限，并将此次事件与 2023 年 OpenAI 风波类比，认为名义治理结构不等于实际控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Board-Reinstates-Jensen-Huang-as-President-CEO-and-Board-Director/default.aspx">NVIDIA Corporation - NVIDIA Board Reinstates Jensen Huang as ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/nvidia-reinstates-jensen-huang-as-ceo-with-government-input">Nvidia Rehires Huang in Stunning Comeback Following... - Bloomberg</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/nvidia-reinstates-jensen-huang-rcna610864">Nvidia reinstates Jensen Huang as CEO</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#AI hardware`, `#technology industry`

---

<a id="item-tech-news-6"></a>
### [Stalwart 宣布成为 Exchange 即插即用替代品](https://stalw.art/blog/microsoft-exchange-replacement/) ⭐️ 7.0/10

Stalwart 邮件服务器现已宣布可作为 Microsoft Exchange 的即插即用替代品，旨在为寻求开源替代方案的组织提供迁移路径。该公告引发社区对实际兼容性的质疑：新版 Outlook 将不再支持本地 Exchange 而只支持云，用户可能需先切换至 Thunderbird 等客户端。此外，德国 GoBD 法规要求邮件存档不可删除或更改并保存长达 10 年，Stalwart 的常规计划及开源版本均未提供此功能。部分评论者认为，支持 MAPI 等专有协议虽能节省授权费用，但会扩大微软协议栈，对开放邮件生态系统构成长期损害。

hackernews · shaunpud · 11月23日 22:32 · [社区讨论](https://news.ycombinator.com/item?id=50620349)

**「背景」** Stalwart 是一个用 Rust 编写的开源邮件与协作服务器；其 1.2.0 版本宣布成为 Microsoft Exchange 的“直接替代品”，新增对 MAPI、EWS、ActiveSync 和 Autodiscover 协议的支持，使组织可用自托管方案替换 Exchange 基础设施，同时继续使用 Outlook 等熟悉客户端。Microsoft Exchange 长期以来是许多企业默认的本地邮件服务器，与 Outlook 客户端深度绑定。此次更新针对希望避免专有许可和云锁定的组织提供迁移路径。

**「影响」** Stalwart 1.2.0 使组织能够将其作为 Microsoft Exchange 的直接替代品部署，但德国用户仍需自行满足 GoBD 归档要求，且新版 Outlook 客户端可能会强制将 IMAP 邮件同步至微软云。

**「社区讨论」** 社区总体认为“即插即用替换”的说法有所夸大，主要担忧包括 Outlook 客户端兼容性、合规存档缺失以及协议锁定效应；也有评论指出 Stalwart 是 Mozilla Thundermail 使用的邮件服务器，显示其实际部署价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart is now a drop-in replacement for Microsoft Exchange</a></li>
<li><a href="https://www.learn.telusko.com/newsletter/stalwart-1-2-0-is-now-a-drop-in-replacement-for-microsoft-exchange">Stalwart 1.2.0 is now a drop-in replacement for Microsoft ...</a></li>
<li><a href="https://linuxiac.com/stalwart-1-2-offers-open-source-microsoft-exchange-replacement/">Stalwart 1.2 Offers Open-Source Microsoft Exchange Replacement</a></li>
<li><a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart is now a drop-in replacement for Microsoft Exchange</a></li>

</ul>
</details>

**标签**: `#email`, `#microsoft-exchange`, `#open-source`, `#mail-server`, `#interoperability`

---

<a id="item-tech-news-7"></a>
### [Ladybird 浏览器进入 alpha 阶段](https://ladybird.org/posts/alpha/) ⭐️ 7.0/10

开源浏览器 Ladybird 已发布 alpha 版本，该浏览器从零构建、独立于 Google 代码。早期社区测试显示，包括新闻网站和 Proxmox 的 NoVNC 在内的多种网站均能正确渲染，有用户称 NoVNC 比在 Firefox 中更流畅，但页面滚动略有卡顿。开发团队已采用 SQLite、Skia 等生产级库替代自研库以提升可靠性。此里程碑对独立浏览器引擎具有重要意义，但该浏览器尚未成为广泛使用的日常选择。

hackernews · janvdberg · 11月23日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50614249)

**「背景」** Ladybird 是一个从零开始构建的独立浏览器引擎，由 501\(c\)\(3\) 非营利组织支持，并非基于 Chromium 或 Gecko。当前 alpha 版本已提供 macOS 和 Linux 版本下载，免费且开源。

**「影响」** 希望尝试的用户现在可以测试独立的 alpha 浏览器，但作为预览版，使用时需谨慎处理敏感数据并关注后续安全更新。

**「社区讨论」** 社区普遍对渲染兼容性感到惊喜，尤其是 NoVNC 的流畅度；主要反馈包括滚动略卡顿、希望改进指纹防护和权限粒度，并询问 alpha 阶段的使用安全注意事项。

<details><summary>参考链接</summary>
<ul>
<li>Ladybird</li>

</ul>
</details>

**标签**: `#web browser`, `#open source`, `#alpha release`, `#systems programming`, `#web engine`

---

<a id="item-tech-news-8"></a>
### [ChatGPT 聊天页上线 GPT-6.2 Sol](https://x.com/ChatGPT/status/2124942186425069836) ⭐️ 7.0/10

据 Telegram 转载的发布信息，ChatGPT 聊天页于 11 月 23 日上线 GPT-6.2 Sol 版本，同日向 Plus、Pro、Business 和 Enterprise 付费用户推送。该版本主要面向日常对话场景，官方称其更能处理复杂请求，包括在用户给出详细指令或要求联网查找信息时表现更好。改进还包括识别照片细节（如标签文字、路牌符号）、按价格或位置等关注点缩小在线选项范围，以及判断何时主动给出后续建议（如降价提醒）。不过，上述能力描述来自官方发布，未经独立验证。

telegram · zaihuapd · 11月24日 00:44

**「相关背景：GPT-6 系列与 Sol 模型」** GPT-6 是 OpenAI 于 2026 年推出的一代模型，其中体积较小的 Sol 和 Luna 模型在 2026 年 9 月发布，用于让 GPT-6 Astra 的智能更高效、更易用。此次推送的 GPT-6.2 Sol 是该系列的更新版本；据 MacRumors 报道，与 GPT-6 相比，它在识别照片细节（如路牌符号、标签文字）方面表现更好。

**「影响」** Plus、Pro、Business 和 Enterprise 订阅者可能自 11 月 23 日起在 Chat 标签页看到 GPT-6.2 Sol，但其复杂请求处理、照片细节识别和主动建议等能力尚未独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/11/23/openai-gpt-6-2-sol-chatgpt/">OpenAI Brings GPT - 6 . 2 Sol to ChatGPT &#x27;s Chat Tab - MacRumors</a></li>
<li><a href="https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/">OpenAI launches GPT - 6 Sol and Luna, boasting lower... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#OpenAI`, `#GPT-6.2`, `#AI`, `#product-update`

---

<a id="item-tech-news-9"></a>
### [黎曼猜想 AI 证明被指空转](https://x.com/i/web/status/2124987173439209561) ⭐️ 7.0/10

Alpöge 与 Claude 宣称用 AI 在 Lean 中证明了黎曼猜想及广义版本，但仅公开约 1700 万行 Lean 代码和 17.5 万个文件，没有人类可读证明。Lean 与 Mathlib 社区次日表示，对代码证明该命题“有充分信心”。随后研究者发现关键定义被写成恒真、几何条件形同虚设，证明可能只是空转。23 日 Alpöge 承认“25 万页是玩笑”，代码“满是垃圾但能编译”，并称批评完全合理。

telegram · zaihuapd · 11月24日 01:29

**「背景」** Lean 是一种交互式定理证明器，Mathlib 是其数学库，形式化证明要求每一步可被机器核验。黎曼猜想是数学中尚未解决的核心难题，涉及黎曼ζ函数非平凡零点的实部是否为 1/2。

**「影响」** 这一争议表明，在 AI 辅助形式化验证中，仅凭代码可编译和社区初始信心不足以确认重大数学证明，必须审查关键定义是否空转或同义反复。

**标签**: `#AI`, `#formal verification`, `#Lean`, `#Riemann Hypothesis`, `#controversy`

---

<a id="item-tech-news-10"></a>
### [4.5 万企业组织致信欧盟要求调查苹果浏览器限制](https://appleinsider.com/articles/26/11/23/eu-urges-to-challenge-apples-grip-on-iphone-browsers?utm_source=rss) ⭐️ 7.0/10

包括 Mozilla 和 Shopify 在内的超过 4.5 万家欧盟企业及民间组织联名致信欧盟委员会，要求依据《数字市场法》对苹果 iPhone 浏览器限制立案。联名方表示，署名方合计代表约 4.5 万至 5.5 万家欧盟企业组织，签名活动将持续到 2026 年 12 月 3 日。虽然苹果已在欧盟允许竞品浏览器使用自有引擎，但技术和法律要求使厂商无法将现有欧盟用户迁出 WebKit，企业更依赖 App Store 触达用户。联名方估算，若半数原生 iOS 应用转向 Web，欧盟企业每年可节省 110 亿欧元开发成本和 13 亿欧元 App Store 费用。

telegram · zaihuapd · 11月24日 03:02

**「背景」** 《数字市场法》将大型平台认定为“守门人”，要求其开放关键服务；浏览器引擎 WebKit 曾长期是 iOS 浏览器的强制内核，苹果在欧盟已允许替代引擎但附加技术条件。此次联名旨在推动欧盟委员会对苹果是否遵守《数字市场法》启动正式调查。

**「影响」** 若欧盟委员会立案，可能迫使苹果进一步放宽对 WebKit 迁移和 App Store 分发的限制，从而降低欧盟企业开发与分发成本；不过目前仅为联名请求，尚未作出立案决定。

**标签**: `#Apple`, `#EU`, `#browser`, `#WebKit`, `#DMA`

---

<a id="item-tech-news-11"></a>
### [黄循财：不做芯片管制规避通道](https://www.bloomberg.com/news/articles/2026-11-24/singapore-won-t-be-conduit-to-skirt-us-chip-curbs-wong-says) ⭐️ 7.0/10

新加坡总理黄循财表示，不允许新加坡被当作企业规避美国芯片出口管制的通道，当局正在调查 Megaspeed 采购英伟达芯片的交易。他强调新加坡不会为绕开管制提供路径。此前一天，美国商务部已将 Megaspeed 及另外 6 家东南亚企业列入贸易黑名单，《联邦公报》称这些企业存在向未获授权用户转移先进计算产品的“重大风险”，名单包括其在马来西亚和泰国的关联实体。路透社报道，阿里巴巴新加坡子公司 Apex Enterprise Solutions 同样在列，阿里称从未转移受管制的先进计算芯片。

telegram · zaihuapd · 11月24日 05:03

**「背景」** 美国商务部将企业列入实体清单，意味着这些企业接收所有受美国出口管制物项时都需额外许可，先进计算芯片是重点管制对象。此次被列名的包括新加坡 Megaspeed、其马来西亚子公司 Speedmatrix 以及阿里巴巴新加坡子公司 Apex Enterprise Solutions；阿里巴巴发言人表示 Apex 从未转移受美国出口限制的先进计算芯片。

**「影响」** 美国已对出口至新加坡、马来西亚、泰国、印尼和巴西的先进芯片新增目的地许可证要求，新加坡实体采购、转运英伟达等先进计算产品将面临更严格审查和调查风险。阿里巴巴新加坡子公司 Apex Enterprise Solutions 被列入黑名单，可能进一步收紧相关供应链的合规压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://uz.kursiv.media/en/2026-11-24/us-blacklist-megaspeed-alice-huang/">US blacklists Megaspeed , once led by China spy suspect Alice Huang</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/us-blacklists-alibaba-owned-company-014536273.html">US Blacklists Alibaba-Owned Company in Setback to AI Ambitions</a></li>
<li><a href="https://www.zerohedge.com/geopolitical/inside-nvidias-supply-china-turmoil-sever-partners-begin-halting-southeast-asia">Nvidia&#x27;s Supply Chain Turmoil Worsens As Several... | ZeroHedge</a></li>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China&#x27;s Access To Advanced Chips Via Singapore ...</a></li>

</ul>
</details>

**标签**: `#chip export controls`, `#semiconductors`, `#AI hardware`, `#US-China tech policy`, `#Singapore`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM 对 ERNIE 5.5 Flash Preview 的 Day-0 支持与推理加速](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview) ⭐️ 8.0/10

rss · vLLM Blog · 11月24日 00:00

**「背景」** Baidu ERNIE 团队与 vLLM 合作，让 ERNIE 5.5 Flash Preview（280B 总参数、14B 激活的稀疏 MoE，支持 1M token 上下文）在发布当天即可运行。此前大模型接入往往需要维护 fork 或等待夜间构建；新架构的长上下文索引和专家路由进一步增加推理开销。

**「方案」** 作者通过独立的 vLLM-ERNIE 插件，经 vllm.general\_plugins 入口自动加载模型代码和内核优化，无需修改官方 wheel；插件仅注册架构路径，不影响其他模型。针对新架构，他们对 VHA 交叉头混合、Multi-Router Latent MoE、MultiMax 输出头、门控注意力等做了算子融合，把可在加载时预计算的参数折叠进权重，减少中间张量和内核启动，作者称融合内核比朴素实现快 1.55–6.53 倍。FlashIndexer 用轻量头路由器做动态头选择和阈值预过滤，在 1M 上下文下索引速度提升 1.4 倍；默认权重对路由专家采用 MXFP4 W4A8 量化并做量化感知训练，KV cache 用 FP8。随权重发布的 DSpark 3 层 MoE 草稿模型经多阶段训练（含在线策略蒸馏），在真实编码和智能体负载上平均接受长度超过 4.0，每步最多草拟 7 个 token。

**「启示」** 该方案表明，通过插件机制与架构级融合、稀疏化和草稿模型协同，新发布的大型稀疏 MoE 可以在不分支、不等待上游合并的情况下获得 Day-0 生产级推理支持。但文中性能数字均为厂商自报，缺少独立基准验证。

**标签**: `#LLM inference`, `#vLLM`, `#mixture-of-experts`, `#kernel fusion`, `#speculative decoding`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic IPO 引发抛售，中国 AI 公司上市计划蒙上阴影](https://www.bloomberg.com/news/articles/2026-11-23/china-s-next-ai-deals-clouded-by-selloff-after-anthropic-ipo) ⭐️ 8.0/10

据彭博报道，Anthropic 创纪录的 IPO 引发全球科技股抛售，自 6 月底以来中国科技股累计蒸发 1.7 万亿美元，DeepSeek、月之暗面和阶跃星辰的上市计划因此蒙上阴影。

telegram · zaihuapd · 11月23日 09:31

**「背景」** Anthropic 这笔 1195 亿美元 IPO 首日上涨 17%、市值达 1.8 万亿美元，次日下跌 8.5%；智谱自 6 月高点跌超 85%，MiniMax 本月跌破发行价。

**标签**: `#Artificial Intelligence`, `#IPO`, `#China`, `#Stock Market Selloff`, `#Anthropic`

---

<a id="item-finance-news-2"></a>
### [英伟达董事会全票恢复黄仁勋 CEO 职务，称无国家安全风险](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director) ⭐️ 8.0/10

英伟达董事会全票通过黄仁勋即刻恢复总裁兼首席执行官职务并重新担任董事，科莱特·克雷斯不再担任临时 CEO、继续担任首席财务官；董事会称其复任不构成国家安全风险。

telegram · zaihuapd · 11月23日 14:02

**「背景」** 此前黄仁勋曾被报道为外国情报活动目标，董事会为此成立独立调查委员会并将调查到底，同时新设国家安全与出口管制委员会并启动首席合规官招聘。另有报道援引知情人士称，董事会未咨询高管层且受政治压力，英伟达未确认。

**标签**: `#Nvidia`, `#corporate governance`, `#leadership change`, `#national security`, `#semiconductors`

---

<a id="item-finance-news-3"></a>
### [上海地铁票价时隔 21 年首次调整，新票价 12 月 1 日起实施](https://weibo.com/1699432410/5368461393397183) ⭐️ 7.0/10

据新华社报道，上海地铁时隔 21 年首次调整票价，新票价 12 月 1 日起实施：起乘价 3 元（0-4 公里），之后每 4、4、4、7、7、10、10 公里加 1 元，50 公里以上每 15 公里加 1 元；同步推出 35/45/60/90 次计次票（定价 190/210/270/390 元，11 月 26 日开售）及同一支付渠道当月累计满 90 元享 9 折，以减轻高频出行者负担。

telegram · zaihuapd · 11月23日 10:45

**「背景」** 上海地铁此前已 21 年未调整票价；在优化票价机制的听证会上，有关部门曾测算方案一平均每人次票价将从 4.23 元提高至 5.22 元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260819A0ARAE00">时隔 21 ...</a></li>
<li><a href="https://hot.online.sh.cn/content/2026-09/09/content_10485162.htm">时隔 21 ...</a></li>

</ul>
</details>

**标签**: `#Shanghai Metro`, `#fare adjustment`, `#public transportation policy`, `#consumer prices`, `#urban economics`

---

<a id="item-finance-news-4"></a>
### [SpaceX 被曝向 Anthropic、Google 出租 AI 算力，月入数十亿美元](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html) ⭐️ 7.0/10

《纽约时报》11 月 23 日援引知情人士报道，自今年 5 月起，SpaceX 每月从其数据中心向 Anthropic、Google 等公司出租算力，月收入达数十亿美元。

telegram · zaihuapd · 11月24日 02:06

**「背景」** 此前 SpaceX 自建的数据中心原本用于内部 AI 研发，但马斯克认为出租算力比自用更赚钱。

**标签**: `#SpaceX`, `#AI infrastructure`, `#Anthropic`, `#Google`, `#compute market`

---