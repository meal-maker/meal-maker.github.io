---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21
lang: zh
---

> 从 42 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [eMudhra 中间 CA 私钥泄露，八个中间证书受影响](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepSeek 开源高性能推理框架 DeepInfer](#item-tech-news-2) ⭐️ 8.0/10
3. [Voxtral 3：Mistral 发布实时开源语音模型与语音代理 SDK](#item-tech-news-3) ⭐️ 8.0/10
4. [Google 开源 TorchTPU：PyTorch 原生支持 TPU](#item-tech-news-4) ⭐️ 8.0/10
5. [Cloudflare 推出 Rust 版 TypeScript 编译器 tsrs](#item-tech-news-5) ⭐️ 8.0/10
6. [谷歌云欧洲西部 2 区故障影响多家银行及服务](#item-tech-news-6) ⭐️ 8.0/10
7. [英伟达被曝禁止使用竞品芯片的小型云厂商参加 GTC 柏林](#item-tech-news-7) ⭐️ 8.0/10
8. [OpenAI 新模型提升 COBOL 迁移准确率至 97.9%](#item-tech-news-8) ⭐️ 8.0/10
9. [英国 Ofcom 在 4chan 案中承认失败](#item-tech-news-9) ⭐️ 7.0/10
10. [如何移除超过 300 个恶意 Tor 出口节点](#item-tech-news-10) ⭐️ 7.0/10
11. [2026 年 Rust 编译器进展展望](#item-tech-news-11) ⭐️ 7.0/10
12. [小米 MiMo-V2.6-Pro 上线 WorkBuddy](#item-tech-news-12) ⭐️ 7.0/10
13. [OpenAI API 推出 12 小时提示缓存](#item-tech-news-13) ⭐️ 7.0/10

**财经新闻**
1. [广电总局报告称中国微短剧成全球第四大视听新业态](#item-finance-news-1) ⭐️ 8.0/10
2. [汇丰 CEO 警告：AI 热潮不意味着所有数据中心都是好投资](#item-finance-news-2) ⭐️ 7.0/10
3. [特朗普儿童账户存款超 80 亿美元，美财长感谢马斯克捐股](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [eMudhra 中间 CA 私钥泄露，八个中间证书受影响](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 9.0/10

八个 eMudhra 中间 CA 证书的私钥已被泄露。这些证书链向 Mozilla、Microsoft、Apple 和 Chrome 根证书计划及许多下游信任库所信任的根。任何捆绑受信任证书列表的软件都需要更新，Linux 发行版需更新 ca-certificates 软件包。Python 生态中 uv 0.13.4、pip 26.2.2 和 certifi 2026.10.19 已发布，携带更新后的证书列表。

rss · Simon Willison · 10月20日 23:50

**「背景：中间 CA 与信任链」** 证书颁发机构（CA）通常使用根证书签发中间证书，再由中间证书为网站签发 TLS/HTTPS 证书。如果中间 CA 的私钥泄露，攻击者可以伪造任意网站的证书，因此各根证书计划（如 Mozilla、Microsoft、Apple、Chrome）需要将相关中间证书标记为不受信任，并要求下游软件更新可信证书列表。本次事件涉及 eMudhra 的八个中间 CA 证书，其私钥于 2026 年 10 月 17 日被报告泄露，影响多个主流信任库。

**「影响」** 依赖这些中间证书且未更新本地信任库的 TLS 客户端可能继续信任由泄露私钥签发的伪造证书，面临中间人攻击风险。已启用 OneCRL、CRLite 等自动撤销机制的浏览器已自动缓解。

**「社区讨论」** 评论者指出这 8 个“被泄露”的 CA 私钥实际上只是单个字节（其中一个字面为 &\#x27;4&\#x27;）。还有人提到 Mozilla 通过 OneCRL 在数小时内自动保护 Firefox 用户，而大量自带 CA 库的软件难以修补，系统可能长期暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emudhra.we-have-a-problem.com/">eMudhra Intermediate CA Compromise</a></li>
<li><a href="https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/">Protecting Firefox users following the compromise of eMudhra ...</a></li>

</ul>
</details>

**标签**: `#certificate-authority`, `#security`, `#TLS`, `#software-supply-chain`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [DeepSeek 开源高性能推理框架 DeepInfer](https://github.com/deepseek-ai/DeepInfer) ⭐️ 8.0/10

DeepSeek 开源了 DeepInfer，一个用于 DeepSeek 模型的高性能推理框架。该框架旨在实现高吞吐、低延迟的大规模推理服务。社区讨论中引用的数据显示，基于该框架的 DeepSeek V4.1 Flash 服务单集群吞吐量可达每天 155 万亿 token，非高峰时段每卡每小时收入 38 美元。讨论还涉及该框架对华为升腾 950 NPU 等国产硬件的支持，以及开源发布时机与美国相关政策的关系。

hackernews · ggcr · 10月20日 09:08 · [社区讨论](https://news.ycombinator.com/item?id=50163277)

**「背景」** DeepInfer 是 DeepSeek 用于自身模型生产环境的高性能推理框架，此次开源版本提供离线推理及规模化部署所需的核心能力。该框架最初主要基于 vLLM 构建，并已支撑 DeepSeek 的大规模在线服务。DeepSeek 表示此次开源仅限推理引擎代码库，未来模型发布仍会与开源社区和硬件伙伴保持协作。

**「影响」** 基于 DeepInfer 的 DeepSeek V4.1 Flash 服务可实现单集群 155 万亿 tokens/天的吞吐量，非高峰定价下每卡每小时收入 38 美元，为采用该框架的组织提供了明确的大规模推理成本与吞吐参考，但该数据为 DeepSeek 自报，尚未经独立验证。

**「社区讨论」** 评论者意见分歧：有用户认为发布是受美国国土安全部排除令影响的战术动作，并猜测 DeepSeek 提前数月准备；另有用户认为开源推理代码和支持华为升腾 NPU 将削弱英伟达的垄断地位，同时也有评论担忧开放权重模型对美国前沿实验室估值的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek-ai/DeepInfer: DeepInfer: High-performance ...</a></li>
<li><a href="https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md">open-infra-index/OpenSourcing_DeepSeek_Inference ... - GitHub</a></li>
<li><a href="https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/">DeepSeek Open-Sources DeepInfer, the Inference Framework ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50163277">DeepSeek just open-sourced its inference engine | Hacker News</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#inference-framework`, `#open-source`, `#llm-serving`, `#ai-infrastructure`

---

<a id="item-tech-news-3"></a>
### [Voxtral 3：Mistral 发布实时开源语音模型与语音代理 SDK](https://mistral.ai/news/voxtral-3/) ⭐️ 8.0/10

Mistral 宣布推出 Voxtral 3，一款实时开放权重语音模型和语音代理 SDK，用于语音转文本和口语代理工作流。该 SDK 将听、推理、工具调用和说整合为实时体验，使代理能够在电话或网络上的实时对话中检索信息、与业务系统交互并完成任务。社区评论提到演示场景可能不现实，并对比了现有企业转录工具的糟糕表现，但也有开发者表示上一代 Voxtral Mini 4B Realtime 可在普通硬件上离线运行。

hackernews · ilreb · 10月20日 16:02 · [社区讨论](https://news.ycombinator.com/item?id=50168396)

**「背景」** Voxtral 3 是 Mistral 推出的实时语音模型与语音代理 SDK，面向电话或网页中的实时对话流程。该 SDK 基于开源实时媒体框架 LiveKit，把转录、通用模型推理与工具调用、语音回复编排为一条流式流水线。此前 Mistral 已发布过开源权重 STT 模型 Voxtral Mini 4B Realtime，可用于离线推理。

**「影响」** 对于需要实时语音代理的开发者，Voxtral 3 的开放权重和 SDK 降低了构建融合听、说、工具调用的语音系统的门槛。

**「社区讨论」** 有用户质疑演示场景不现实，并抱怨微软 Teams 和 8x8 的转录质量差；另有开发者表示上一代 Voxtral Mini 4B Realtime 离线推理在普通硬件上表现良好，但有人指出语音转文本/文本转语音的本地部署仍不理想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/voxtral-3/">Voxtral 3: Voice Agent SDK &amp; Speech Models in 50+ Languages</a></li>
<li><a href="https://www.goodiebase.com/news/mistral-voxtral-3-voice-agent-sdk-2026-10-20">Mistral launches Voxtral 3 speech models and a toolkit for ...</a></li>
<li><a href="https://www.explainx.ai/blog/voxtral-3-mistral-voice-agent-sdk-speech-models">Voxtral 3: Mistral Voice Agent SDK, $13/1M Chars TTS ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#voice AI`, `#speech-to-text`, `#open-weight models`, `#Mistral`

---

<a id="item-tech-news-4"></a>
### [Google 开源 TorchTPU：PyTorch 原生支持 TPU](https://github.com/google-pytorch/torch_tpu) ⭐️ 8.0/10

Google 开源了 TorchTPU，一个面向 TPU 的原生 PyTorch 后端，仓库地址为 google-pytorch/torch\_tpu。该项目由 Google Cloud 与 Meta 的 PyTorch 团队共同开发，使 TPU 成为与 GPU、CPU 并列的 PyTorch 原生选项，现有代码几乎无需修改即可运行。vLLM、SGLang、llm-d、TorchTitan 等框架已经接入，Hugging Face Transformers v5 可直接将模型部署到 TPU。开源这一后端简化了 PyTorch 在 Google AI 加速器上的部署，并可能影响 AI 基础设施竞争格局。

hackernews · ilreb · 10月20日 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50169053)

**「背景」** TorchTPU 是 Google 与 Meta 合作开发的原生 PyTorch 后端，使 Google TPU 与 GPU、CPU 一样成为 PyTorch 的原生选项。它提供了自定义 ATen 内核、编译缓存、分布式训练与推理示例，并已支持 vLLM、SGLang、llm-d、TorchTitan、Ray、TorchRec、Hugging Face 和 LiteRT 等工具生态。

**「影响」** 对于在 Google TPU 上使用 PyTorch 的开发者，TorchTPU 可减少对 XLA 等中间层的适配工作，并借助已接入的 vLLM、SGLang、TorchTitan 和 Hugging Face Transformers v5 实现更直接的部署。

**「社区讨论」** 社区评论认为 XLA 可能是比 Inductor 更好的编译器基础设施，并称这是 TensorFlow 的“最后一根钉子”；也有人指出 Amazon 为 AWS Trainium 提供了类似的 torch-neuronx，以及有人正在为 Tenstorrent 加速器实现可运行大部分 TorchTPU 的 libtpu 替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus">TorchTPU is now open source: Run native PyTorch on TPUs</a></li>
<li><a href="https://pytorch.org/blog/introducing-torchtpu/">Introducing TorchTPU - PyTorch</a></li>
<li><a href="https://github.com/google-pytorch/torch_tpu">GitHub - google-pytorch/torch_tpu</a></li>

</ul>
</details>

**标签**: `#pytorch`, `#tpu`, `#google`, `#open-source`, `#ai-infrastructure`

---

<a id="item-tech-news-5"></a>
### [Cloudflare 推出 Rust 版 TypeScript 编译器 tsrs](https://blog.cloudflare.com/typescript-rust-port/) ⭐️ 8.0/10

Cloudflare 的 tsrs 项目将 TypeScript 编译器移植到 Rust，据称取得了显著性能提升，并可在 WASM 沙箱中运行 TypeScript 编译。该项目的主要动机是在 Cloudflare 的仅支持 WASM 的沙箱中提供 TypeScript 编译能力，而不是单纯追求更快的编译器；此前只能将 Go 实现的 tsc 导出为 WASM，但会携带完整 Go 运行时。tsrs 使用永不释放的内存区域（arena）模拟垃圾回收，以克服 Rust 无 GC 与从 GC 语言移植的结构重组难题。TypeScript 团队已与 tsrs 维护者合作，认为部分速度提升并非仅源于语言选择，相关优化已体现在 TS 7.1 的更快、更精简改进中。此外，该项目作者表示其代码由前沿 AI 模型几乎独立完成，自己未写任何代码，这引发了对 AI 生成编译器移植可靠性的讨论。

hackernews · hnisjafx40 · 10月20日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50165953)

**「背景」** TypeScript 编译器传统上使用 TypeScript 自举并编译为 JavaScript 运行，因此在大型项目中常面临速度与内存压力。Cloudflare 与 VoidZero 正在 Oxc 工具链中共同孵化实验性 Rust 移植项目 tsrs，并与 TypeScript 团队合作验证其优化；该项目不是官方 TypeScript 的分叉，而是探索用 Rust 的无 GC、可编译为 WASM 等特性实现编译器，并可能将其安全优化反馈回 TypeScript 7.1。

**「影响」** 对于使用 TypeScript 的开发者来说，tsrs 有望带来约 8 倍的速度提升和 70% 的内存降低，并通过 @tsrs/wasm 让 TypeScript 编译能在 WASM 沙盒中运行，无需 Go 运行时开销。不过该实现仍存在兼容性限制和已知缺口。

**「社区讨论」** 社区普遍认可 tsrs 的性能和 WASM 沙箱动机，TypeScript 团队成员确认双方合作，并指出部分优化将反哺 TS 7.1。但讨论中也出现分歧：有开发者担心项目是完全由 AI 生成的移植（作者写零代码），对可靠性和长期维护持保留态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/typescript-rust-port/">Introducing tsrs: a Port of TypeScript to Rust | Cloudflare Blog</a></li>
<li><a href="https://www.webpronews.com/cloudflare-voidzero-tsrs-rust-port-typescript-compiler/">Cloudflare and VoidZero Take On tsrs, a Rust Port of the ...</a></li>
<li><a href="https://thenewstack.io/cloudflare-rust-typescript-tsrs/">“We are not forking TypeScript”: Cloudflare spearheads Rust ...</a></li>
<li><a href="https://www.npmjs.com/package/@tsrs/wasm">@tsrs/wasm - npm</a></li>
<li><a href="https://book.st-hakky.com/en/news/introducing-tsrs-a-port-of-typescript-to-rust">tsrs: 8x Faster and 70% Less Memory than TypeScript</a></li>

</ul>
</details>

**标签**: `#typescript`, `#rust`, `#compiler`, `#webassembly`, `#performance`

---

<a id="item-tech-news-6"></a>
### [谷歌云欧洲西部 2 区故障影响多家银行及服务](https://www.neowin.net/news/google-cloud-outage-takes-down-hsbc-revolut-bank-of-scotland-llyods-equifax-more/) ⭐️ 8.0/10

2026 年 10 月 19 日 23:08 PDT 起，Google Cloud 在 europe-west2 区域发生多服务中断，原因是 europe-west2-b 可用区出现电力事件。受影响的服务包括 HSBC、Revolut、Equifax 等欧洲银行和金融机构，导致网银、移动应用或支付等功能无法使用。Google 表示电力事件已缓解，预计 30 分钟内基础设施服务部分缓解，剩余服务仍在恢复中。该事件显示了单一云区域故障对关键金融业务的广泛影响。

hackernews · paweladamczuk · 10月20日 10:26 · [社区讨论](https://news.ycombinator.com/item?id=50163961)

**「背景」** Google Cloud 按区域（region）和可用区（zone）部署，europe-west2 是伦敦区域，europe-west2-b 是该区域内的一个可用区。电力事件可导致可用区级故障，进而影响部署在该区域或未跨区冗余的服务。此类故障对依赖云服务的金融系统尤其敏感。

**「影响」** 对于使用 europe-west2 区域的欧洲银行和金融科技用户，本次事件可能导致账户访问、提现、卡支付等操作中断；不过个别用户报告 HSBC 服务正常，说明实际影响范围可能因机构冗余配置而异。

**「社区讨论」** 有用户报告 Revolut 无法访问账户、提现或刷卡，且缺乏电话支持，反映新银行的客服短板；另有 HSBC 用户称其服务正常，并批评 Downdetector 数据不可靠，还有评论建议欧盟建立自主云基础设施。

**标签**: `#cloud-computing`, `#outage`, `#infrastructure`, `#google-cloud`, `#banking`

---

<a id="item-tech-news-7"></a>
### [英伟达被曝禁止使用竞品芯片的小型云厂商参加 GTC 柏林](https://x.com/SemiAnalysis_/status/2111162214891610496?s=20) ⭐️ 8.0/10

英伟达近日拒绝多家新兴云服务商参加即将在柏林举行的 GTC 大会，被拒原因是这些厂商在自有云平台中引入了 AMD GPU、Google TPU 等竞品芯片，并非技术不达标。英伟达是 CoreWeave、Nebius 这类新兴云厂商的芯片供应商和重要投资方，已向两家各战略投资 20 亿美元，并为其算力租赁提供收入兜底。不少体量有限的新兴云厂商因此不敢公开使用英伟达竞品，担忧自身 GPU 优先供应、融资及上市计划受影响。该限制不适用于拥有足够采购体量和自研芯片能力的超大规模云厂商，目前英伟达尚未公开置评。

telegram · zaihuapd · 10月20日 12:32

**「背景：GTC 柏林与“neocloud”厂商」** 英伟达 GTC 是其年度技术大会，柏林场次定于 2026 年 10 月 20 日至 22 日举行。SemiAnalysis 于 2026 年 10 月 16 日报道称，多家规模较小的 GPU 云服务商（即“neocloud”）被拒绝参加该活动，原因是它们在其基础设施中加入了 AMD Instinct GPU 或 Google TPU。这类厂商主要依赖外部采购芯片，与拥有自研芯片和足够采购体量的超大规模云厂商不同。

**「影响」** 使用 AMD GPU 或 Google TPU 的中小型云服务商面临被英伟达排除在 GTC Berlin 等活动之外的风险，并可能因此加剧 GPU 供应、融资及上市方面的不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/nvidia-neoclouds-gtc-berlin-amd-tpu/">Nvidia reportedly bars neoclouds from GTC Berlin over AMD and ...</a></li>
<li><a href="https://thebuildout.ai/intel/55074a0e-dd6a-4ca0-a816-56a6ff0ce8db">Nvidia reportedly denies GTC Berlin access to cloud providers ...</a></li>
<li><a href="https://aistockwire.com/blog/nvidia-nvda-gtc-berlin-neoclouds-refused-amd-tpu-semianalysis-october-2026">SemiAnalysis: neoclouds refused GTC Berlin over AMD, TPUs</a></li>
<li><a href="https://thebuildout.ai/intel/55074a0e-dd6a-4ca0-a816-56a6ff0ce8db">Nvidia reportedly denies GTC Berlin access to cloud providers ...</a></li>
<li><a href="https://cryptobriefing.com/nvidia-neoclouds-gtc-berlin-amd-tpu/">Nvidia reportedly bars neoclouds from GTC Berlin over AMD and ...</a></li>
<li><a href="https://www.ainvest.com/news/nvidia-reported-gtc-berlin-snub-amd-neoclouds-share-defense-weakest-link-flex-2610/">Nvidia&#x27;s reported GTC Berlin snub of AMD-using neoclouds is a ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#GPU`, `#Cloud Computing`, `#AI Hardware`, `#Antitrust`

---

<a id="item-tech-news-8"></a>
### [OpenAI 新模型提升 COBOL 迁移准确率至 97.9%](https://openai.com/index/low-resource-programming-languages/) ⭐️ 8.0/10

OpenAI 最新模型在低资源编程语言的开发与迁移上取得显著提升。在从零构建 SQLite 引擎的 20 种语言测试中，GPT-6 Astra 平均通过率从 GPT-5.6 Sol 的 26.8% 升至 87.4%，低成本 GPT-6 Luna 为 40.3%，API 成本降低 78%。在将 COBOL 代码迁移至现代语言的测试中，GPT-6.1 Sol 在低推理强度下准确率从 5.4% 升至 86.6%，成本降低 39%，高推理强度下达 97.9%。相关评测集已在 GitHub 开源。

telegram · zaihuapd · 10月20日 14:24

**「背景」** 低资源编程语言指可公开获取的代码、文档等训练数据较少的语言，COBOL、Fortran 和 Visual Basic 虽使用范围变窄，但在银行、政府等关键系统中仍承担大量遗留代码。将这些语言迁移到现代语言是长期工程难题，传统 AI 代码模型因训练语料不足而在这些任务上表现较差。OpenAI 此次公开了针对软件工程、SQLite 构建和 COBOL 迁移的新评测，并开源了相关评测集，用于衡量 GPT-6 系列模型相对 GPT-5.6 Sol 基线的改进。

**「影响」** 对计划迁移 COBOL 的企业，GPT-6.1 Sol 高达 97.9% 的迁移准确率意味着自动迁移成本与时间可能显著降低；但实际落地仍需人工验证、系统集成与管理判断（tool-2-1、tool-2-2）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/low-resource-programming-languages/">Advancing coding in low ‑ resource programming languages | OpenAI</a></li>
<li><a href="https://insights.mgm-tp.com/en/2026/insurance/claude-can-migrate-cobol-migration-who-is-making-the-transition/">Claude COBOL Migration : Who&#x27;s Making the Transition?</a></li>
<li><a href="https://abstracta.us/blog/ai/cobol-migration">How to Validate a COBOL Migration with AI | Abstracta</a></li>

</ul>
</details>

**标签**: `#AI`, `#Code Generation`, `#COBOL`, `#Programming Languages`, `#OpenAI`

---

<a id="item-tech-news-9"></a>
### [英国 Ofcom 在 4chan 案中承认失败](https://prestonbyrne.com/2026/10/20/ofcom-concedes-defeat/) ⭐️ 7.0/10

英国通信管理局（Ofcom）据报已在针对 4chan 的执法案件中承认失败。这一结果凸显了国家层面的在线安全规则在适用于境外平台时的局限性。该案可能成为外国互联网平台抵制本国在线安全监管的重要参考。报道未提供让步的具体时间、法律依据或后续安排。

hackernews · iamnothere · 10月20日 14:30 · [社区讨论](https://news.ycombinator.com/item?id=50167028)

**「背景」** 4chan 是一个匿名英文贴图论坛，由 Christopher &quot;moot&quot; Poole 于 2003 年 10 月推出，设有多个主题板块。英国通信监管机构 Ofcom 此前依据在线安全法规对 4chan 处以 520,000 英镑罚款，4chan 随后起诉 Ofcom 以阻止其可能的境外执法。此次 Ofcom 的让步意味着该平台可能面临在英国被 DNS 封锁，而非直接受到境外处罚。

**「影响」** Ofcom 在 4chan 案中承认无法继续执法，意味着英国《在线安全法》对拒不配合的境外平台缺乏有效强制手段，4chan 及其用户暂时不会因该监管行动受到实际制裁。

**「社区讨论」** 评论普遍认为，对境外平台的此类执法行动象征意义大于实际效果，因为难以对不进入该国且不依赖该国金融体系的外国运营者施加约束；部分评论担忧此举可能被用作推行深度包检测等更严格网络封锁措施的理由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/4chan">4 chan - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50167028">Ofcom concedes defeat in 4 chan case | Hacker News</a></li>
<li><a href="https://www.linkedin.com/posts/harrybrignull_ofcom-fines-4chan-520000-lawyer-responds-activity-7440404299685314561-xAOX">&quot; Ofcom Fines 4 chan £520,000, Lawyer Responds With Picture of...&quot;</a></li>
<li><a href="https://www.theguardian.com/technology/2025/jun/10/ofcom-4chan-online-safety-breaches">UK media regulator investigates possible online safety breaches at...</a></li>
<li><a href="https://cybernews.com/news/ofcom-issues-20k-fine-to-4chan-for-ignoring-information-requests/">Ofcom fines 4 chan £20K over safety law | Cybernews</a></li>

</ul>
</details>

**标签**: `#ofcom`, `#4chan`, `#online-safety`, `#regulation`, `#internet-governance`

---

<a id="item-tech-news-10"></a>
### [如何移除超过 300 个恶意 Tor 出口节点](https://kaba.cx/posts/20261020_Tor/) ⭐️ 7.0/10

10 月 2 日，333 个 Tor 出口节点（约占 Tor 出口的 10%）开始将 SSH 端口 22 流量重定向到 12 台拦截服务器，运行基于 paramiko 的中间人攻击，窃取密码并试图植入 Ebury 恶意软件。作者检测到这些恶意节点并推动移除了其中超过 300 个。由于 SSH 会显示主机密钥变更警告，攻击很快被发现并追踪到所有受感染节点。该攻击主要影响使用密码认证的 SSH 连接，而密钥认证不受影响。

hackernews · kabakabakaba · 10月20日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=50166257)

**「背景」** Tor 出口节点是洋葱路由匿名网络中用户流量离开加密隧道前的最后一跳，能够观察甚至篡改发往目标服务器的明文流量。SSH 依赖主机密钥指纹标识服务器身份，若中间人转发连接，客户端会因密钥变化发出警报。Ebury 是一种 OpenSSH 后门/凭据窃取恶意软件；本事件中攻击者先用 Ebury 入侵部分出口节点，之后让这些节点将 SSH（端口 22）重定向至 12 台拦截服务器。

**「影响」** 使用这些恶意 Tor 出口节点进行 SSH 密码登录的用户可能已泄露凭据并面临 Ebury 感染风险；密钥认证用户不受影响。

**「社区讨论」** 评论者认为该攻击设计并不高明，SSH 主机密钥警告使其迅速暴露；另有人提醒密钥认证不受影响，并指出可能存在被入侵的托管服务商作为感染源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/how-i-got-over-300-tor-exit-nodes-removed-luas3vpcw">How I got over 300 Tor exit nodes removed - daily.dev</a></li>
<li><a href="https://o-server.main.jp/hacker-news/en/articles/2026/10/20/coordinated-attack-on-tor-exit-nodes-compromised-by-ssh-intercept-50166257.html">Coordinated Attack on Tor Exit Nodes Compromised by SSH ...</a></li>
<li><a href="https://www.linux.org/threads/300-tor-exit-nodes-infected.73084/">300 Tor exit nodes infected. - Linux.org</a></li>

</ul>
</details>

**标签**: `#security`, `#tor`, `#ssh`, `#malware`, `#network-security`

---

<a id="item-tech-news-11"></a>
### [2026 年 Rust 编译器进展展望](https://yoyo-code.com/2026-is-exciting-year-for-rust-compiler-and-me/) ⭐️ 7.0/10

开发者 panstromek 对 2026 年 Rust 编译器的工作表示乐观，认为这可能解决困扰多年的重大技术债。重点包括新版 trait solver 与 Polonius 借用检查器，二者若落地有望解锁长期停滞的 specialization 等语言特性。这些改进被描述为编译器开发者多年来一直期待的变化，但所述内容属于前瞻，并非已发布版本。

hackernews · panstromek · 10月20日 13:53 · [社区讨论](https://news.ycombinator.com/item?id=50166502)

**「背景」** Rust 编译器长期背负 trait 解析相关技术债务；新一代 trait solver 已开发近十年，并计划在 2026 年达到成熟。Polonius 是配套的借用检查改进项目，二者被视为可能为 specialization 等长期停滞特性铺路。

**「社区讨论」** 评论区中，有开发者认同新 trait solver 和 Polonius 可能解锁 specialization；也有用户质疑 Rust 的前景，提出需要兼具 Go 的简单、Zig 的编译速度和 Rust 安全性的新语言。另有评论关注更小的 target 目录、多态化（polymorphism）的编译策略及新 solver 对 async 问题的具体修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/2026-is-an-exciting-year-for-the-rust-compiler-and-me--52dhmmibn">2026 is an exciting year for the Rust compiler (and me)</a></li>

</ul>
</details>

**标签**: `#rust`, `#compiler`, `#traits`, `#polonius`, `#programming-languages`

---

<a id="item-tech-news-12"></a>
### [小米 MiMo-V2.6-Pro 上线 WorkBuddy](https://weibo.com/6486870325/5356179212995907) ⭐️ 7.0/10

小米技术宣布 Xiaomi MiMo-V2.6-Pro 正式上线 WorkBuddy，并在 Artificial Analysis 智能指数中获得 46 分，自称全球开源第一。该模型宣称支持 1M 超长上下文、多智能体分工协作，以及对图像、视频、音频、文本的全模态联合理解。官方称其面向长任务托管、深度研究、设计出稿、文档办公和小工具开发等长程工作流，目前已开放体验。上述均为厂商宣传数据，尚未见独立第三方验证。

telegram · zaihuapd · 10月20日 13:40

**「背景」** 小米 MiMo 是小米推出的多模态大模型系列，MiMo-V2.6-Pro 在 Artificial Analysis 智能指数上得 46.32 分，超过 Kimi K3 和 Qwen3.8 Max，成为目前最强开源模型；其 API 定价与 V2.5 系列一致，输入 token 每百万 0.43 美元、输出 token 每百万 0.87 美元。WorkBuddy 是小米面向长程工作流的上线平台，覆盖长任务托管、深度研究、设计出稿、文档办公和小工具开发等场景，此次接入 MiMo-V2.6-Pro 并开放体验。

**「影响」** WorkBuddy 用户可以立即体验该模型，用于长文档、多模态理解和多智能体任务，但 1M 上下文和“开源第一”等指标尚需独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://artificialanalysis.ai/models/mimo-v2-6-pro">MiMo - V 2 . 6 - Pro - Intelligence , Performance... | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#Xiaomi`, `#MiMo`, `#open-source AI`, `#multimodal`, `#WorkBuddy`

---

<a id="item-tech-news-13"></a>
### [OpenAI API 推出 12 小时提示缓存](https://x.com/OpenAIDevs/status/2112603916076781778) ⭐️ 7.0/10

OpenAI 宣布其 API 现已支持 12 小时提示缓存，持久化智能体可在全天复用共享指令、工具和上下文，即使请求间隔数小时仍按较低缓存输入费率计费。对于 Codex 与 Work 的登录用户，还提供永久缓存，回到旧对话或暂停数小时后继续无需任何惩罚，并保证命中缓存。这一变更为需要长时运行、成本敏感的 AI 智能体降低了持续使用成本。

telegram · zaihuapd · 10月21日 01:21

**「背景：提示缓存与既有保留时长」** 提示缓存（prompt caching）允许 API 在多次请求复用相同前缀（如系统指令、工具定义、上下文）时按缓存命中计费，从而降低长时运行智能体的成本与延迟。此前 OpenAI 曾推出缓存仪表盘并调整过 Codex 与 Work 的缓存上限，社区还观察到 gpt-5.1 等模型提供 24 小时免费缓存选项（需在请求中设置标志）。本次将 API 缓存延长至 12 小时，并为 Codex/Work 登录用户提供永久命中保证，是延续这一成本优化方向的变化。

**「影响」** 使用 OpenAI API 构建长时运行智能体（如 dots）的开发者可以在请求间隔数小时的情况下继续享受较低缓存输入费率，从而降低持续运行成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nowline.net/reports/openai-s-responses-api-keeps-agents-working-while-your-tools-run">OpenAI &#x27;s Responses API keeps agents working while your tools run...</a></li>
<li><a href="https://www.linkedin.com/posts/sahar-mor_alpha-tip-for-openai-api-users-to-significantly-activity-7399469492470280192-m8dR">Alpha tip for OpenAI API users to significantly reduce latency and...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#prompt caching`, `#API`, `#AI agents`, `#developer tools`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [广电总局报告称中国微短剧成全球第四大视听新业态](https://content-static.cctvnews.cctv.com/snow-book/index.html?toc_style_id=feeds_default&amp;amp;item_id=11947338521606813154&amp;amp;channelId=1119) ⭐️ 8.0/10

国家广电总局发布《中国微短剧国际传播发展报告》，称中国微短剧已成为继美国电影、日本动画、韩国电视剧之后的重要视听产品形态；报告预计 2026 年全年国内市场规模达 850 亿元，中国以外海外市场超过 160 亿美元、同比增长 67%。

telegram · zaihuapd · 10月20日 08:39

**「背景」** 该报告由国家广电总局发布，其预测基于 2026 年 1 至 9 月上线 4.7 万部、月活用户超 6 亿的官方数据。

**标签**: `#micro-dramas`, `#China entertainment industry`, `#market size`, `#overseas expansion`, `#AI-generated content`

---

<a id="item-finance-news-2"></a>
### [汇丰 CEO 警告：AI 热潮不意味着所有数据中心都是好投资](https://www.cnbc.com/2026/10/20/data-center-financing-ai-debt-hsbc.html) ⭐️ 7.0/10

汇丰首席执行官乔治·埃尔德雷表示，人工智能虽然具有变革性，但投资者在投资数据中心时必须有所选择，需审视租约质量和合同定价；麦肯锡预测到 2030 年全球数据中心支出可能达到 7 万亿美元。

rss · CNBC Finance · 10月20日 10:39

**「背景」** 此前，超大规模云厂商去年发行了 2000 亿美元债券融资，摩根大通预计到本十年末 AI 相关债务发行将达 4.1 万亿美元，加剧债市紧张。

**标签**: `#AI`, `#data centers`, `#debt financing`, `#bond markets`, `#HSBC`

---

<a id="item-finance-news-3"></a>
### [特朗普儿童账户存款超 80 亿美元，美财长感谢马斯克捐股](https://x.com/SecScottBessent/status/2112323120380129562) ⭐️ 7.0/10

美国财政部长贝森特在社交平台 X 发文称，面向美国未成年人的“特朗普账户”投资储蓄账户已收到超过 80 亿美元存款，并感谢马斯克捐赠股票以进一步推高总额。

telegram · zaihuapd · 10月20日 09:57

**「背景」** 特朗普账户是美国政府为未成年人设立的投资储蓄账户；白宫称截至 2026 年 10 月已开设近 7000 万个账户，其中超过 6000 万个通过自动开户完成，对象为持有社会安全号码的 18 岁以下儿童，慈善捐款可追加存入。

**「对家庭的影响」** 美国财政部长贝森特称，近 7000 万符合条件的美国未成年人已自动开户，其中 2025 至 2028 年出生者每人可获得 1000 美元种子投资，并可能因马斯克捐股而增加账户资金；但相关数字来自社交媒体声明，尚未经独立核实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.whitehouse.gov/releases/2026/10/a-financial-stake-in-the-future-for-nearly-70-million-american-children-trump-accounts-made-it-possible/">Trump Accounts Put 70 Million Kids on the Path to Financial Freedom</a></li>
<li><a href="https://www.foxbusiness.com/politics/trump-celebrates-automatic-enrollment-70-million-trump-accounts-children">Trump celebrates automatic enrollment of 70 M children &#x27;s investment...</a></li>

</ul>
</details>

**标签**: `#child savings accounts`, `#fiscal policy`, `#US Treasury`, `#Elon Musk`, `#Trump Account`

---