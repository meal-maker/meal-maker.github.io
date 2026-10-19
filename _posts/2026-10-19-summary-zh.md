---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 34 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [混合推理智能体：潜空间推理，文本行动](#item-tech-news-1) ⭐️ 8.0/10
2. [vLLM v0.32.0 发布：结构化决策与低精度 KV Cache 扩展](#item-tech-news-2) ⭐️ 7.0/10
3. [软件背后的人：价值在品味与产品决策](#item-tech-news-3) ⭐️ 7.0/10
4. [RepRapMicron 开源微米级 3D 打印机](#item-tech-news-4) ⭐️ 7.0/10
5. [DeepSeek 搜索抓取 API 每千次请求 0.75 美元](#item-tech-news-5) ⭐️ 7.0/10
6. [Namecheap 被指停用用户全部域名](#item-tech-news-6) ⭐️ 7.0/10
7. [TempoPFN：面向零样本时间序列预测的线性 RNN 合成预训练](#item-tech-news-7) ⭐️ 7.0/10
8. [英伟达优化 Kimi K3 推理速度](#item-tech-news-8) ⭐️ 7.0/10
9. [Google 开源递归智能体框架 Harness²](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic 游说 AI 安全法案设叫停门槛](#item-tech-news-10) ⭐️ 7.0/10
11. [MIT 研究：AI 内容可植入虚假记忆](#item-tech-news-11) ⭐️ 7.0/10

**财经新闻**
1. [美国 AI 基建热潮出现裂痕，巨额投资面临回报考验](#item-finance-news-1) ⭐️ 8.0/10
2. [外卖大战一年后平台利润回升，商家骑手额外承压](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [混合推理智能体：潜空间推理，文本行动](https://arxiv.org/abs/2610.18861) ⭐️ 8.0/10

研究人员提出“混合推理智能体”（Hybrid Reasoning Agents），一种在潜空间中进行推理、通过文本采取行动的 LLM 智能体架构。该方法将中间推理步骤保持在潜向量中，旨在减少文本输出中的重复表述并提高推理效率。相关代码已在 GitHub（togethercomputer/HybridAgent）开源，模型发布在 Hugging Face 的 togethercomputer/hybridagent 集合中。论文在 arXiv（编号 2610.18861）第 S5 节给出了评测结果。目前已有社区测试报告指出，14B 量化版本在 llama.cpp 中可能因兼容性问题出现循环输出。

hackernews · allinonai · 10月18日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=50145337)

**「背景」** 传统的 LLM 智能体通常通过生成文本 token 来逐步推理和行动，但近期研究开始探索在潜在空间中进行推理以减少 token 开销并提高效率。本文提出了混合推理智能体（HybridAgents），在统一生成过程中动态地在潜在推理和基于文本的交互之间切换。作者还将其与同规模纯文本智能体进行比较，以检验混合推理下暴露的文本是否仍足以支持外部监控、调试和纠正。

**「影响」** 对于需要高效长链推理的智能体开发者，该开源实现提供了一条可尝试的路径，但其在不同推理框架中的稳定性和性能仍需更多验证。

**「社区讨论」** 社区讨论集中在将混合推理应用于 Qwen 等现有模型、进一步扩展潜空间与文本模式结合的可能性；同时有用户报告 llama.cpp 下的量化版本出现循环输出，提示可能需要适配更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.18861">[2610.18861] Hybrid Reasoning Agents - arXiv.org</a></li>
<li><a href="https://arxiv.org/html/2610.18861v1">Hybrid Reasoning Agents - arXiv.org</a></li>
<li><a href="https://arxivsignals.io/papers/2610.18861">Hybrid Reasoning Agents · ArXivSignals</a></li>

</ul>
</details>

**标签**: `#LLM`, `#reasoning`, `#latent-space`, `#ai-agents`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [vLLM v0.32.0 发布：结构化决策与低精度 KV Cache 扩展](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.0/10

vLLM v0.32.0 已发布，包含 814 个提交和来自 363 位贡献者的改动。新版本新增并默认启用 POST /v1/systemone 结构化决策端点，可对 choice、noul 和 score 问题作答，并支持 Cloudflare/clef-omni、LiquidAI/d1-3B 和 DiffusionGemma；新增 --tool-call-parser hf 与 --reasoning-parser hf，通过检查点的 response\_template 实现通用解析。低精度 KV cache 覆盖更多架构：NVFP4 支持 SM8x/SM12x/SM90 等，GLM-5.x 在 SM100 默认 FP8 KV cache（每 rank 内存减半，吞吐提高 2.3–5.5%，TTFT 成本增加 7–11%），ROCm 新增 4-bit ultraquant\_4bit。性能与模型方面，Model Runner V2 加入 GPU n-gram 推测、Elastic EP、流水线并行等并成为 ROCm 默认；新增 EmbeddingGemma 2、MiniCPM-V 4.7、Nemotron 3.5 ASR 等模型，并针对 GLM-5.3、DeepSeek-V4、Qwen 系列做了优化。安全修复覆盖 GHSA-4hhp-h66f-j5j7、GHSA-q97c-p368-75c4、GHSA-frvg-qw88-hww9；破坏性变更包括弃用 Python 3.10、默认 CORS 不再允许所有来源、transformers&gt;=5.16.1,&lt;5.20.0 与 tokenizers&gt;=0.23.2 依赖要求、移除部分旧特性等。

github · khluu · 10月18日 06:50

**「背景」** vLLM 是一个开源的大语言模型及多模态模型推理与服务框架，最初由加州大学伯克利分校 Sky Computing Lab 开发，以 PagedAttention 键值缓存内存管理方法为核心，支持连续批处理、分布式推理等特性。该项目已成为最活跃的开源 AI 项目之一，由超过 2000 名贡献者共同维护。

**「影响」** 升级到 v0.32.0 的用户需注意移除 Python 3.10、默认 CORS 限制及依赖范围等不兼容变更；使用 GLM-5.x 模型的 SM100 用户可通过默认 FP8 KV cache 显著降低显存，但需接受 7–11% 的首 token 延迟上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory ...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#kv-cache`, `#low-precision`, `#api`

---

<a id="item-tech-news-3"></a>
### [软件背后的人：价值在品味与产品决策](https://karrisaarinen.com/posts/someone-behind-the-software/) ⭐️ 7.0/10

这篇文章认为，随着 AI 编码能力提升，软件创作者的核心价值正从代码和架构转向产品愿景、品味以及决定构建什么。文章指出，许多产品的改动主要是叠加新能力而非改进核心问题，导致产品成为缺乏统一观点的功能集合。作者推测这可能与工作组织方式有关，个体借助 AI 代理工作时更容易走向功能添加而非重新思考现有能力。

hackernews · tosh · 10月18日 16:32 · [社区讨论](https://news.ycombinator.com/item?id=50142573)

**「背景」** 这篇文章讨论的是软件创建者在人工智能编码能力提升时的价值转变。传统上，软件的价值常被认为主要在于编写代码和实现功能；但随着大语言模型与 AI 编程工具能够自动生成越来越多的代码，代码实现本身的稀缺性下降。因此，作者将重点转向产品愿景、品味和“决定构建什么、不构建什么”，认为这些才是人类创作者不可替代的核心贡献。

**「社区讨论」** 评论者普遍认同文章观点，认为价值在于决定做什么、产品品味和对客户任务的理解，而非代码或架构。有人补充 AI 没有价值观、意图与品味，产品是人的特定价值观和品味的产物；另有评论引用 Dorothy Sayers 与 Fred Brooks 的创意三阶段（理念、实现、交互）作为佐证。

**标签**: `#software-development`, `#ai`, `#product-management`, `#human-centered-design`, `#opinion`

---

<a id="item-tech-news-4"></a>
### [RepRapMicron 开源微米级 3D 打印机](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 7.0/10

RepRapMicron 是一个托管在 GitHub 上的开源项目，目标是制造微米级分辨率的 3D 打印机。该项目因可能用于芯片制造和自复制而受到关注，并有潜力降低精密微制造的门槛。目前公开的技术细节有限，其实际能力仍属推测。社区讨论将其与拉姆斯登、莫兹利和威尔金森等历史精密制造突破相类比，并关联到前序技术开发视频。

hackernews · RobotToaster · 10月18日 13:48 · [社区讨论](https://news.ycombinator.com/item?id=50141076)

**「背景」** RepRap 是一个开源 3D 打印机项目，其核心目标之一是自我复制。RepRapMicron（μRepRap）是该项目的延伸，旨在将制造精度推进到微米级，让开源或创客环境也能进行高精度微加工。根据 RepRap wiki 和 GitHub 页面，该项目目前主要在 GitHub wiki 上持续开发，并探索诸如芯片制造等潜在应用。

**「影响」** 若该技术成熟，可能降低芯片原型和小批量微制造的门槛，但尚未有公开性能数据支持其可行性。

**「社区讨论」** 评论中有人期待未来自制内存或廉价芯片打印；也有人质疑 1/1000 比例自复制（即 1/1,000,000 打印）的可行性，整体上既有乐观也有保留。

<details><summary>参考链接</summary>
<ul>
<li>VikOlliver/RepRapMicron: μRepRap - A 3D printer project designed to work at the micron scale · GitHub</li>
<li>RepRapMicron - RepRap</li>
<li>RepRapMicron - Hacker News</li>

</ul>
</details>

**标签**: `#3d-printing`, `#open-source-hardware`, `#microfabrication`, `#reprap`, `#makers`

---

<a id="item-tech-news-5"></a>
### [DeepSeek 搜索抓取 API 每千次请求 0.75 美元](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek 推出了搜索与抓取（search and fetch）API，定价为每 1,000 次成功请求 0.75 美元。这一价格显著低于 Brave Search API 的每千次 5 美元和 Kagi API 的每千次 12 美元。该 API 面向需要为 AI 智能体集成网络搜索能力的开发者，提供低成本访问方式。目前公告未提供更多技术细节、版本或性能数据。

hackernews · fagnerbrack · 10月18日 06:50 · [社区讨论](https://news.ycombinator.com/item?id=50138531)

**「背景」** 开发者通常通过托管搜索 API（如 Brave Search API、Kagi API）在程序或 AI 智能体中接入网页搜索，而 Google 不提供付费搜索 API，因此出现了第三方服务。DeepSeek 现在在其 API 中增加了 Search 和 Fetch 接口，分别用于搜索和抓取网页内容；官方定价页显示两者均为每 1,000 次成功请求 0.75 美元。该价格远低于 Brave 的 5 美元和 Kagi 的 12 美元，因此适用于需要低成本网页搜索集成的开发者场景。

**「影响」** 对于需要将网页搜索集成到 AI 智能体工作流的开发者，该定价可能将每千次成功搜索请求成本从 5 或 12 美元降至 0.75 美元，但尚未披露的覆盖范围、速率限制和可靠性可能影响实际采用。

**「社区讨论」** 评论区存在实用替代方案与价格走向的分歧：有用户推荐免费的 searxng-ai-kit 或 oh-my-pi 自托管抓取，并认为这些托管服务仅因 Google 拒绝提供付费搜索 API 而存在；另一观点认为 SEO 和智能体搜索可能推动 API 价格变为负值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202610/1372476.shtml">DeepSeek unveils faster, cheaper AI model, with... - Global Times</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models &amp; Pricing | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#search-api`, `#pricing`, `#ai-agents`, `#web-search`

---

<a id="item-tech-news-6"></a>
### [Namecheap 被指停用用户全部域名](https://www.reddit.com/r/sysadmin/comments/1x8cycd/namecheap_just_seized_and_disabled_all_my_domains/) ⭐️ 7.0/10

一名系统管理员在 Reddit 报告其所有域名被 Namecheap 突然停用，引发对注册商可靠性和支持的讨论。事件具体原因、涉及域名数量和恢复时间未被源内容证实，但多名评论者称经历过类似问题，包括未回复钓鱼邮件 48 小时内域名被关闭、账户被转给未验证第三方等。有评论提到 Namecheap 于 2025 年被私募股权公司 CVC 以 15 亿美元收购，并出现削减人工支持、引入自动化及多次涨价的情况。该案例提示域名注册商单方面处置域名的风险，尤其对依赖自有域名运行服务的系统管理员和工程师。

hackernews · sashk · 10月18日 16:56 · [社区讨论](https://news.ycombinator.com/item?id=50142866)

**「背景」** 域名注册商不仅负责域名注册，还托管域名的权威 DNS 并处理转移、续费与账户安全。如果注册商判定存在滥用、支付、安全或合规问题，或自动化风控触发误判，就可能暂停或禁用相关域名，导致网站、邮件等服务立即中断。Namecheap 是国际常用的域名注册商，近期有被私募股权收购及支持质量下降的讨论，因此这类事件会引起对注册商可靠性和备用 DNS/转移方案的关注。

**「影响」** 对于使用 Namecheap 持有关键域名的用户，这些报告和评论表明其域名可能被无预警停用且恢复耗时（个案中超过 6 小时），应核查账户安全设置、备份 DNS/注册商迁移方案，并评估转向支持更可靠的注册商。

**「社区讨论」** 社区中多位用户称遭遇类似停用，质疑 Namecheap 支持质量与自动化处置；建议选择支持良好、可人工沟通的注册商，并对被私募收购后的成本削减和涨价表示担忧。

**标签**: `#domain-registrar`, `#namecheap`, `#dns`, `#system-administration`, `#tech-industry`

---

<a id="item-tech-news-7"></a>
### [TempoPFN：面向零样本时间序列预测的线性 RNN 合成预训练](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 7.0/10

论文《TempoPFN》已被 NeurIPS 2026 接收，提出了一个合成时间序列生成器与数据增强库，用于预训练时间序列基础模型。作者用该库预训练了一个基于 DeltaProduct 的线性 RNN，实现了零样本时间序列预测。该合成数据已在此前的 Toto-2 和 TS-ICL 项目中使用。代码发布于 GitHub（automl/TempoPFN），模型发布于 HuggingFace（AutoML-org/TempoPFN），作者包括 Vladyslav Moroshan、Julien Siems、Arber Zela、Timur Carstensen 和 Frank Hutter。

reddit · r/MachineLearning · /u/Yossarian\_1234 · 10月18日 16:43

**「背景」** 时间序列基础模型通常依赖大规模真实数据，而合成数据可以提供可扩展的预训练信号。线性 RNN（例如 DeltaProduct）相比 Transformer 在处理长序列时更高效。零样本预测指模型无需在目标数据集上训练即可直接进行预测。

**「影响」** 时间序列预测开发者可通过 TempoPFN 的合成数据生成器和预训练模型快速构建零样本预测基线，无需标注真实训练数据。

**标签**: `#time series forecasting`, `#linear RNN`, `#synthetic data`, `#foundation models`, `#NeurIPS`

---

<a id="item-tech-news-8"></a>
### [英伟达优化 Kimi K3 推理速度](https://x.com/SemiAnalysis_/status/2111627094878790023) ⭐️ 7.0/10

SemiAnalysis 发文称，英伟达通过一项上游 vLLM 优化，在 2.8 万亿参数的 Kimi K3 模型上实现每用户每秒 423 个 token 的速度，相同硬件下快 1.68 倍。具体优化由英伟达 CentML 的 Benjamin 使用 Cute DSL 编写解码专用内核，并通过 Megakernel 融合实现。英伟达还在为 vLLM 开发适配 DeepSeek v4.1 等模型的工作。

telegram · zaihuapd · 10月18日 08:20

**「背景」** Kimi K3 是 Moonshot AI 推出的约 2.8 万亿参数的前沿模型；vLLM 是常用的开源大模型推理服务引擎。NVIDIA 与 vLLM 在 NVIDIA GB300 NVL72 上推出了统一的 CuTe DSL 解码 Megakernel（约 12,000 行，由 NVIDIA CentML 的 Benjamin Chislett 编写），通过融合注意力、MoE 和跨 GPU 通信将每层延迟从 130 微秒（23 个内核）降至 69 微秒（13 个内核）。在 batch=1 且使用 DSpark 投机解码的受控测试中，该优化达到 842 tokens/s；而更早的 Megakernel 方法仅达到 423 tokens/s。

**「影响」** 对于使用 vLLM 部署 Kimi K3 的用户，在相同硬件上每用户推理速度可提升至 423 tokens/s，相当于 1.68 倍加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aicoder.com/news/news-20261018-nvidia-vllm-kimi-k3-gb300-nvl72-cute-dsl-megakernel-842-tok-s">Kimi K3 Hits 842 tok/s on NVIDIA GB300 NVL72: NVIDIA and vLLM ...</a></li>
<li><a href="https://zavino.co/en/news/tokens-per-second-explained-kimi">Tokens Per Second Explained Using the 842 Kimi K3 Benchmark</a></li>

</ul>
</details>

**标签**: `#AI`, `#vLLM`, `#Nvidia`, `#performance-optimization`, `#large-language-models`

---

<a id="item-tech-news-9"></a>
### [Google 开源递归智能体框架 Harness²](https://github.com/google-research/harness2) ⭐️ 7.0/10

Google Research 已开源 Harness²，一个用于递归优化 LLM 智能体的框架。该框架通过两层递归在不更新模型权重的情况下提升智能体表现，在 WorkBuddy-Bench 等基准测试中最高提升 11.5 分。它支持并行与顺序递归模式，已集成多款基准测试，并采用 Apache 2.0 协议开源。项目代码和论文可通过 GitHub 与 arXiv 获取。

telegram · zaihuapd · 10月18日 11:24

**「背景」** LLM 智能体的能力不仅取决于底层模型，也依赖其执行 harness。Harness² 是一个即插即用的递归智能体驾驭框架，面向开放世界中设计时未见过的任务，通过两个相连的递归层次扩展智能体能力。在该框架中，父智能体生成并运行可执行脚本，脚本再生成子智能体 harness；论文将这种机制视为对推理语言模型（RLM）模型递归的代码优先扩展。

**「影响」** 对于希望在不进行权重更新或微调的前提下提升 LLM 智能体在特定基准上表现的开发者和研究者，Harness² 提供了一种 Apache 2.0 许可的递归优化实现，但最高 11.5 分的提升来自特定测试，未必能直接迁移到所有任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2610.14224">Paper page - Harness ^2: Recursive Agent Harnessing for an Open...</a></li>
<li><a href="https://arxiv.org/html/2606.13643">Recursive Agent Harnesses</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM agents`, `#open source`, `#recursive optimization`, `#Google Research`

---

<a id="item-tech-news-10"></a>
### [Anthropic 游说 AI 安全法案设叫停门槛](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model) ⭐️ 7.0/10

Anthropic 正游说推动一项 AI 安全法案，拟规定只有当模型可能造成超过 10 亿美元损失，或导致超过 50 人死亡或受伤时，政府才可阻止发布。该提案会让商务部成为唯一能够启动叫停程序的美国机构，最终决定权交由联邦法官。法案还要求由商务部注册的独立第三方定期评估实验室和模型，并在发现生物武器、AI 网络攻击或失控风险后 72 小时内报告。相关措施旨在为前沿 AI 模型的发布设置高阈值监管触发条件。

telegram · zaihuapd · 10月18日 12:40

**「背景」** 美国联邦层面的 AI 安全监管仍处于立法讨论阶段，核心争议之一是政府何时以及由哪个机构阻止高风险模型发布。Anthropic 作为一家前沿 AI 公司，正通过游说提出具体门槛和流程，以影响这类立法。

**「影响」** 若该提案被采纳，美国 AI 模型发布只有在预计造成超过 10 亿美元损失或超过 50 人死亡/受伤时才可能被政府叫停，并且只有商务部能启动程序、联邦法官做最终裁定，未达门槛的模型不会因此被阻止。

**标签**: `#AI safety`, `#AI regulation`, `#Anthropic`, `#policy`, `#frontier AI`

---

<a id="item-tech-news-11"></a>
### [MIT 研究：AI 内容可植入虚假记忆](https://gizmodo.com/ai-generated-content-can-plant-fake-memories-researchers-say-2000826459) ⭐️ 7.0/10

麻省理工学院 Pattie Maes 团队的研究发现，受试者在看过一组照片后，部分人又接触到经 AI 修改的版本；在随后的记忆测试中，这些人更容易记错原图，并对错误记忆表现出更高自信。相关研究还显示，深度伪造和 AI 生成文本能够植入关于虚构政治丑闻的虚假记忆，甚至降低投票意愿。研究人员称，目前普通人正确识别 AI 生成内容的概率约等于抛硬币。这些结果表明，AI 生成或修改的内容可能通过视觉和文本材料影响人类记忆的准确性。

telegram · zaihuapd · 10月19日 00:16

**「研究背景」** 虚假记忆是指人们对并未发生或与事实不符的事件的回忆。随着生成式 AI 和深度伪造技术普及，研究者开始关注被 AI 编辑的照片、视频能否扭曲人的记忆；例如 MIT Media Lab 的 Pattie Maes 团队在 2025 年 CHI 会议发表的研究中，将 AI 修改后的图像和视频展示给受试者，并测量其对原始画面的回忆是否被改变。该研究属于“合成人类记忆”方向，目的是量化 AI 视觉内容对记忆植入和回忆信心的影响。

**「影响」** 对公众而言，接触 AI 修改或生成的图像、视频和文本可能增加虚假记忆风险，并削弱基于准确记忆的选举等决策。

<details><summary>参考链接</summary>
<ul>
<li>Synthetic Human Memories: AI-Edited Images and Videos Can Implant False Memories and Distort Recollection — MIT Media Lab</li>
<li>AI-Edited Images and Videos Can Implant False Memories and Distort Recollection | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems</li>

</ul>
</details>

**标签**: `#AI-generated content`, `#deepfakes`, `#false memory`, `#AI safety`, `#research`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国 AI 基建热潮出现裂痕，巨额投资面临回报考验](https://www.ft.com/content/9ea5a37d-15c9-4d5b-94d6-719048c9cd3c?syn-25a6b1a6=1) ⭐️ 8.0/10

据《金融时报》报道，美国 AI 基础设施投资热潮遇冷：2025 年至 2032 年预计支出将超过 10 万亿美元，但自 2026 年以来至少 47 个大型数据中心项目被推迟、撤回或叫停，分析机构估计仅约 35%规划项目有较高可行性。融资压力显现，英伟达支持的云服务商 CoreWeave 单日跌超 11%，费城半导体指数追平 2006 年以来最长连跌。

telegram · zaihuapd · 10月18日 08:52

**「背景」** 此前大量资金涌入美国 AI 数据中心，但利率上行推高了项目借贷成本，进而抑制芯片订单，成为近期半导体股持续承压的背景。

**「影响」** AI 基建相关企业和半导体板块正面临融资成本上升与盈利前景重估压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ainvest.com/news/chip-index-longest-losing-streak-2008-bet-ai-paid-2610/">The Chip Index&#x27;s Longest Losing Streak Since 2008 Is a Bet on ...</a></li>

</ul>
</details>

**标签**: `#AI基础设施`, `#数据中心`, `#半导体`, `#融资压力`, `#市场风险`

---

<a id="item-finance-news-2"></a>
### [外卖大战一年后平台利润回升，商家骑手额外承压](https://www.latepost.com/news/dj_detail?id=3762) ⭐️ 7.0/10

外卖补贴战一年后，美团与阿里平台销售费用接近回到战前、经营利润回升，双方日均单量合计从战前的约 9000 万单增至近 1.4 亿单，增长约五成。补贴停止后成本转向商家和骑手，茶饮咖啡上市公司单店营收利润普遍下滑，一二线城市骑手单均收入降至 7-8.5 元。

telegram · zaihuapd · 10月18日 07:40

**「背景」** 此前的外卖补贴战中，平台通过高额补贴刺激订单，推高了销售费用。

**标签**: `#food delivery`, `#platform economy`, `#merchant costs`, `#rider income`, `#Meituan`

---