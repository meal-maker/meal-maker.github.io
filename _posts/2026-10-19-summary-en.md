---
layout: default
title: "Horizon Summary: 2026-10-19 (EN)"
date: 2026-10-19
lang: en
---

> From 34 items, 13 important content pieces were selected

---

**Technology News**
1. [Hybrid Reasoning Agents: Latent-Space Thought, Text-Based Actions](#item-tech-news-1) ⭐️ 8.0/10
2. [vLLM v0.32.0 Adds Structured Decisions, Generic Parsers, Low-Precision KV Cache](#item-tech-news-2) ⭐️ 7.0/10
3. [Someone Behind the Software](#item-tech-news-3) ⭐️ 7.0/10
4. [RepRapMicron: Open-Source Micron-Resolution 3D Printer](#item-tech-news-4) ⭐️ 7.0/10
5. [DeepSeek introduces search and fetch API at $0.75 per 1,000 successful requests](#item-tech-news-5) ⭐️ 7.0/10
6. [Namecheap user reports all domains disabled amid support concerns](#item-tech-news-6) ⭐️ 7.0/10
7. [TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Forecasting](#item-tech-news-7) ⭐️ 7.0/10
8. [Nvidia Speeds Up Kimi K3 Inference via vLLM](#item-tech-news-8) ⭐️ 7.0/10
9. [Google Open-Sources Harness² Recursive Agent Framework](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic Backs AI Safety Bill Requiring $1B Harm or 50 Casualties to Halt Models](#item-tech-news-10) ⭐️ 7.0/10
11. [AI-Generated Media Can Implant False Memories, MIT Research Finds](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [US AI infrastructure boom shows cracks as projects stall](#item-finance-news-1) ⭐️ 8.0/10
2. [One Year After China’s Food Delivery Subsidy War, Platform Profits Rebound as Merchants and Riders Bear Costs](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Hybrid Reasoning Agents: Latent-Space Thought, Text-Based Actions](https://arxiv.org/abs/2610.18861) ⭐️ 8.0/10

The arXiv paper 2610.18861 introduces Hybrid Reasoning Agents, an LLM agent design that performs internal reasoning in latent space and acts through text. The associated code is available at github.com/togethercomputer/HybridAgent, with model collections on Hugging Face under togethercomputer/hybridagent, and evaluation details are linked in Section 5 of the arXiv HTML version. The approach targets reducing verbose textual restatement during multi-step reasoning by keeping intermediate steps as latent representations. The source announcement does not include benchmark numbers or a formal comparison, so the reported gains are not specified.

hackernews · allinonai · Oct 18, 20:48 · [Discussion](https://news.ycombinator.com/item?id=50145337)

**「Background」** Large language model agents typically perform chain-of-thought reasoning as visible token sequences and act through textual tool calls. Latent reasoning instead updates continuous hidden states without emitting intermediate tokens, which can reduce token cost but makes inspection harder. Hybrid Reasoning Agents \(HybridAgents\) combine these by dynamically switching between latent-space reasoning and text-based interaction within one model, aiming to balance efficiency and interpretability for agentic tasks.

**「Impact」** Developers and researchers can now test hybrid latent/text reasoning with the released code and models, though early llama.cpp runtime reports suggest compatibility and stability may still need work.

**「Community Discussion」** Comments mix practical setup concerns with speculative architecture ideas: one user reports a 14B quantized llama.cpp build looping on a simple summarization task, while others discuss applying it to restatement-heavy Qwen outputs or extending latent links beyond text.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.18861">[2610.18861] Hybrid Reasoning Agents - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#reasoning`, `#latent-space`, `#ai-agents`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [vLLM v0.32.0 Adds Structured Decisions, Generic Parsers, Low-Precision KV Cache](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 7.0/10

vLLM v0.32.0 was released with 814 commits from 363 contributors, adding the new \`POST /v1/systemone\` endpoint for \`choice\`, \`noul\`, and \`score\` questions and a generic \`hf\` tool/reasoning parser that reads a checkpoint&\#x27;s \`response\_template\`. Low-precision KV cache support expands across GPU architectures: NVFP4 runs on SM8x, SM12x, and SM90, GLM-5.x defaults to FP8 KV cache on SM100 \(halving per-rank memory with 2.3-5.5% more throughput at a 7-11% TTFT cost\), and ROCm gains a 4-bit \`ultraquant\_4bit\` cache. Model Runner V2 adds GPU n-gram speculation, Elastic EP, pipeline parallelism with prefill context parallelism for MLA, and a stock torch.compile mode, while startup and serving improvements include FlashInfer precompiled kernel downloads and least-loaded API worker routing \(\#60723 shows 43-85% more req/s on short requests\). The release also adds models like EmbeddingGemma 2, MiniCPM-V 4.7, and Nemotron 3.5 ASR, fixes several security advisories, and introduces breaking changes such as dropping Python 3.10, restricting default CORS origins, and requiring transformers&gt;=5.16.1,&lt;5.20.0.

github · khluu · Oct 18, 06:50

**「Background」** vLLM is an open-source framework for high-throughput inference and serving of large language models and related multimodal models, originally developed at UC Berkeley&\#x27;s Sky Computing Lab and now maintained by a large contributor community. It introduced PagedAttention, a memory-management method for transformer key–value caches, and supports features such as continuous batching and distributed inference. Version 0.32.0 is a major release that adds structured decision endpoints, generic parsers, and expanded low-precision KV cache support.

**「Impact」** Operators running GLM-5.x on SM100 can expect roughly half the KV cache memory per rank by default, with 2.3-5.5% higher throughput at a 7-11% TTFT cost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory ...</a></li>

</ul>
</details>

**Tags**: `#vllm`, `#llm-inference`, `#kv-cache`, `#low-precision`, `#api`

---

<a id="item-tech-news-3"></a>
### [Someone Behind the Software](https://karrisaarinen.com/posts/someone-behind-the-software/) ⭐️ 7.0/10

The article argues that the core value of software creators now lies in product vision, taste, and deciding what to build rather than in code, especially as AI coding capabilities improve. It contends that many product changes are primarily additive, leading to collections of abilities without a unified point of view, because it is easier to add new capabilities than to rethink existing ones. The author suggests this may stem from how work is organized around individuals and agents. Commenters, including a SaaS author, agree that value is not in code or architecture but in deciding what to build and what not to build.

hackernews · tosh · Oct 18, 16:32 · [Discussion](https://news.ycombinator.com/item?id=50142573)

**「Background」** Karri Saarinen&\#x27;s essay argues that as large language models improve at writing code, the durable contribution of a software creator shifts from implementation to product vision, taste, and decisions about what to build. The discussion fits into a broader debate about how AI coding assistants affect the role and value of human developers, especially in product-focused SaaS companies.

**「Community Discussion」** Comments broadly agree with the essay, noting that AI lacks values, intent, and taste, and that human creators bring particular values and cultural desires. A commenter also connects the idea to Dorothy Sayers&\#x27; stages of creative activity: idea, implementation, and interaction.

**Tags**: `#software-development`, `#ai`, `#product-management`, `#human-centered-design`, `#opinion`

---

<a id="item-tech-news-4"></a>
### [RepRapMicron: Open-Source Micron-Resolution 3D Printer](https://github.com/VikOlliver/RepRapMicron/wiki) ⭐️ 7.0/10

RepRapMicron is an open-source GitHub project developing a micron-resolution 3D printer, discussed on Hacker News for its possible use in chip fabrication and self-replication. If successful, it could democratize precision microfabrication for makers and open-source hardware developers. The project&\#x27;s approach is described as novel and valuable for hardware enthusiasts, but the analysis summary cautions that its capabilities are still speculative. The available item does not include specific technical details such as achieved resolution, hardware configuration, or project timeline.

hackernews · RobotToaster · Oct 18, 13:48 · [Discussion](https://news.ycombinator.com/item?id=50141076)

**「Background」** RepRap is an open-source 3D printer project that aims to create machines capable of self-replication by printing many of their own parts. RepRapMicron, also called μRepRap, extends this concept to micron-scale fabrication, where extremely fine resolution could enable applications such as microfabrication and potentially chip manufacturing. The project&\#x27;s development is documented primarily on GitHub and the RepRap wiki.

**「Impact」** If RepRapMicron succeeds, makers and open-source hardware developers could gain an affordable route to micron-scale parts and potentially chip fabrication, but this outcome is not yet demonstrated.

**「Community Discussion」** Commenters draw parallels to late-18th-century precision manufacturing advances and share a related video series. Some express optimism about DIY chip or RAM fabrication, while one commenter asks why a 1/1000 scale self-replicating printer is assumed to be preposterous.

<details><summary>References</summary>
<ul>
<li>VikOlliver/RepRapMicron: μRepRap - A 3D printer project designed to work at the micron scale · GitHub</li>
<li>RepRapMicron - RepRap</li>

</ul>
</details>

**Tags**: `#3d-printing`, `#open-source-hardware`, `#microfabrication`, `#reprap`, `#makers`

---

<a id="item-tech-news-5"></a>
### [DeepSeek introduces search and fetch API at $0.75 per 1,000 successful requests](https://api-docs.deepseek.com/guides/search/) ⭐️ 7.0/10

DeepSeek has launched a search and fetch API, documented at api-docs.deepseek.com/guides/search/, priced at $0.75 per 1,000 successful requests. This rate significantly undercuts existing hosted search APIs such as Brave Search API at $5 per 1,000 requests and Kagi API at $12 per 1,000 requests, according to a community comment. The service is positioned for cost-effective web search integration in AI agent workflows. The pricing applies to successful requests, though the definition of a successful request is not detailed in the available information.

hackernews · fagnerbrack · Oct 18, 06:50 · [Discussion](https://news.ycombinator.com/item?id=50138531)

**「Context」** DeepSeek is an AI research organization that offers large language model APIs. A search API programmatically returns search results from a web index, while a fetch API retrieves the content of a given URL; both are commonly integrated into AI agent workflows for real-time information gathering. Hosted search APIs typically charge per thousand successful requests, with existing providers such as Brave and Kagi pricing their services higher.

**「Impact」** Developers integrating web search into AI agents can reduce per-request search costs to $0.75 per 1,000 successful requests, compared with $5–$12 for comparable hosted APIs.

**「Community Discussion」** Commenters point to self-hosted alternatives such as searxng-ai-kit as free options, and some speculate that search API prices may eventually go negative as providers compete for influence over AI-driven search.

<details><summary>References</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202610/1372476.shtml">DeepSeek unveils faster, cheaper AI model, with... - Global Times</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models &amp; Pricing | DeepSeek API Docs</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#search-api`, `#pricing`, `#ai-agents`, `#web-search`

---

<a id="item-tech-news-6"></a>
### [Namecheap user reports all domains disabled amid support concerns](https://www.reddit.com/r/sysadmin/comments/1x8cycd/namecheap_just_seized_and_disabled_all_my_domains/) ⭐️ 7.0/10

A sysadmin reported on Reddit that Namecheap disabled all of their domains, prompting a wider discussion about registrar trustworthiness. Multiple commenters described similar past incidents, including account access given to an unverified party, domain bans based on an ambiguous tweet, and a business domain shut off for not replying to a phishing email within 48 hours. Another commenter said support removed phone 2FA from an account after only receiving a username and a story, without verifying identity. The thread notes Namecheap was acquired by private equity firm CVC in 2025 for $1.5B, with commenters linking this to reduced human support and multiple .com price increases this year.

hackernews · sashk · Oct 18, 16:56 · [Discussion](https://news.ycombinator.com/item?id=50142866)

**「Namecheap and domain disabling context」** Namecheap is a domain registrar and web hosting provider that manages domain registrations and DNS for customers. A registrar can suspend or disable domains in response to abuse reports, billing issues, or account verification failures, which cuts off websites and email associated with those domains. One commenter notes that Namecheap was acquired by private equity firm CVC in 2025, and other commenters point to past incidents where Namecheap suspended domains or accounts.

**「Impact」** System administrators who rely on Namecheap for domain registration may face unexpected domain suspension and slow recovery, as one commenter reported over 6 hours to restore service after responding to a phishing-related suspension.

**「Community Discussion」** Commenters broadly agreed that Namecheap&\#x27;s support has deteriorated, with some attributing it to the 2025 CVC acquisition and warning to pick registrars carefully. A few expressed more satisfaction with GoDaddy&\#x27;s assigned account executives for large domain portfolios.

**Tags**: `#domain-registrar`, `#namecheap`, `#dns`, `#system-administration`, `#tech-industry`

---

<a id="item-tech-news-7"></a>
### [TempoPFN: Synthetic Pre-training of Linear RNNs for Zero-shot Forecasting](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 7.0/10

TempoPFN introduces a library of synthetic time-series generators and augmentations for pre-training time-series foundation models, demonstrated on a DeltaProduct-based linear RNN. The approach enables zero-shot forecasting, meaning models can make predictions on unseen series without task-specific training. The work was accepted at NeurIPS 2026, with implementations available on GitHub and pretrained models on Hugging Face. The same synthetic data pipeline has already been used in Toto-2 and TS-ICL. Authors are Vladyslav Moroshan, Julien Siems, Arber Zela, Timur Carstensen, and Frank Hutter.

reddit · r/MachineLearning · /u/Yossarian\_1234 · Oct 18, 16:43

**「Background」** Linear recurrent neural networks such as DeltaProduct provide efficient sequence modeling through linear state transitions. Zero-shot time-series forecasting refers to predicting on series without training on them. Synthetic pre-training uses generated data to teach models patterns before deployment.

**「Impact」** Researchers can use the released code and pretrained DeltaProduct RNNs to train or evaluate time-series foundation models with zero-shot forecasting capabilities.

**Tags**: `#time series forecasting`, `#linear RNN`, `#synthetic data`, `#foundation models`, `#NeurIPS`

---

<a id="item-tech-news-8"></a>
### [Nvidia Speeds Up Kimi K3 Inference via vLLM](https://x.com/SemiAnalysis_/status/2111627094878790023) ⭐️ 7.0/10

SemiAnalysis reported that Nvidia has delivered an upstream vLLM optimization for the 2.8-trillion-parameter Kimi K3 model, reaching 423 tokens per second per user and running 1.68x faster on the same hardware. The work includes decode-specific kernels written in Cute DSL by Benjamin from Nvidia CentML and uses Megakernel fusion. Nvidia is also developing vLLM adaptations for models such as DeepSeek v4.1. The improvement demonstrates substantial per-user throughput gains for open-source serving infrastructure without changing hardware.

telegram · zaihuapd · Oct 18, 08:20

**「Background」** Kimi K3 is Moonshot AI&\#x27;s frontier model with roughly 2.8 trillion parameters, and vLLM is the open-source serving engine where NVIDIA contributed this optimization. The work uses CuTe DSL to write decode-specific kernels and fuses attention, mixture-of-experts, and cross-GPU communication into a Megakernel, reducing per-layer latency from 130 µs across 23 kernels to 69 µs across 13 kernels on NVIDIA GB300 NVL72 hardware. Later refinements adding DSpark speculative decoding reached 842 tokens/s at batch size 1, compared with the earlier 423 tokens/s megakernel result reported in the source.

**「Impact」** Users and operators serving the Kimi K3 model via vLLM can expect roughly 1.68x higher per-user throughput on identical hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://aicoder.com/news/news-20261018-nvidia-vllm-kimi-k3-gb300-nvl72-cute-dsl-megakernel-842-tok-s">Kimi K3 Hits 842 tok/s on NVIDIA GB300 NVL72: NVIDIA and vLLM ...</a></li>
<li><a href="https://zavino.co/en/news/tokens-per-second-explained-kimi">Tokens Per Second Explained Using the 842 Kimi K3 Benchmark</a></li>

</ul>
</details>

**Tags**: `#AI`, `#vLLM`, `#Nvidia`, `#performance-optimization`, `#large-language-models`

---

<a id="item-tech-news-9"></a>
### [Google Open-Sources Harness² Recursive Agent Framework](https://github.com/google-research/harness2) ⭐️ 7.0/10

Google Research has open-sourced Harness², a recursive framework for optimizing LLM agents without updating model weights. The framework uses two levels of recursion to improve agent performance and reports gains of up to 11.5 points on benchmarks including WorkBuddy-Bench. Harness² supports both parallel and sequential recursion modes and has been integrated with multiple benchmarks. It is released under the Apache 2.0 license, with code and paper available on GitHub and arXiv.

telegram · zaihuapd · Oct 18, 11:24

**「Background」** LLM agents rely not only on their underlying model but also on the execution harness that controls tool use, prompting, and sub-agent orchestration. Google Research&\#x27;s Harness² is a plug-and-play framework that applies recursive agent harnessing through two connected levels of recursion; a parent agent generates and runs an executable script that can spawn subagent harnesses in parallel or sequentially. It is released under the Apache 2.0 license and targets open-world settings where agents encounter tasks unseen during harness design.

**「Impact」** Developers and researchers evaluating LLM agents can now use an Apache 2.0-licensed recursive optimization approach that showed up to 11.5-point gains on WorkBuddy-Bench without weight updates.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/harness2">GitHub - google - research / harness 2 · GitHub</a></li>
<li><a href="https://huggingface.co/papers/2610.14224">Paper page - Harness ^2: Recursive Agent Harnessing for an Open...</a></li>
<li><a href="https://arxiv.org/html/2606.13643">Recursive Agent Harnesses</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM agents`, `#open source`, `#recursive optimization`, `#Google Research`

---

<a id="item-tech-news-10"></a>
### [Anthropic Backs AI Safety Bill Requiring $1B Harm or 50 Casualties to Halt Models](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model) ⭐️ 7.0/10

Anthropic is lobbying for an AI safety bill that would let the government block a model’s release only if it may cause more than $1 billion in damages or more than 50 deaths or injuries. The proposal would require independent third parties registered by the Commerce Department to regularly evaluate AI labs and models, and to report discovered bioweapon, AI cyberattack, or loss-of-control risks within 72 hours. Under the plan, only the Commerce Department could order a model stopped, and other US agencies would be barred from doing so, with a federal judge making the final decision.

telegram · zaihuapd · Oct 18, 12:40

**「Background」** US debates over AI safety have centered on pre-deployment evaluations for frontier models and which agencies should have authority to intervene against catastrophic risks. Anthropic is an AI lab participating in those policy discussions, and this proposal would formalize third-party assessments while narrowing emergency stop powers to the Commerce Department.

**「Impact」** If adopted, the bill would create a single Commerce Department pathway for halting frontier AI models, imposing 72-hour reporting requirements on labs while reserving stops for extreme harm or casualty thresholds. It remains a lobbying proposal, not law.

**Tags**: `#AI safety`, `#AI regulation`, `#Anthropic`, `#policy`, `#frontier AI`

---

<a id="item-tech-news-11"></a>
### [AI-Generated Media Can Implant False Memories, MIT Research Finds](https://gizmodo.com/ai-generated-content-can-plant-fake-memories-researchers-say-2000826459) ⭐️ 7.0/10

Researchers at MIT led by Pattie Maes found that after viewing a set of photos, participants who later saw AI-modified versions were more likely to misremember the original images and expressed high confidence in those false memories. Other studies indicate that deepfakes and AI-generated text can implant false memories about fictional political scandals and even reduce willingness to vote. The research also notes that ordinary people currently identify AI-generated content correctly at a rate roughly equivalent to chance. The findings, reported by Gizmodo, highlight how AI-generated or altered media may strengthen misinformation and distort personal and political recollection.

telegram · zaihuapd · Oct 19, 00:16

**「False memories and AI-altered visuals」** False memories are recollections of events that did not occur or that deviate from reality, a well-documented distortion in human memory research. The MIT Media Lab study led by Pattie Maes investigated how AI-edited images and videos affect such memories, with the CHI 2025 paper reporting that AI-generated videos of AI-edited images produced the most pronounced increase in reported false memories—2.05 times the control condition.

<details><summary>References</summary>
<ul>
<li>Synthetic Human Memories: AI-Edited Images and Videos Can Implant False Memories and Distort Recollection — MIT Media Lab</li>
<li>AI-Edited Images and Videos Can Implant False Memories and Distort Recollection | Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems</li>

</ul>
</details>

**Tags**: `#AI-generated content`, `#deepfakes`, `#false memory`, `#AI safety`, `#research`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US AI infrastructure boom shows cracks as projects stall](https://www.ft.com/content/9ea5a37d-15c9-4d5b-94d6-719048c9cd3c?syn-25a6b1a6=1) ⭐️ 8.0/10

The US AI infrastructure investment boom is showing cracks, with at least 47 large data center projects delayed, withdrawn, or halted since 2026 and only about 35% of planned projects having high feasibility, according to analysis firms.

telegram · zaihuapd · Oct 18, 08:52

**「Background」** The AI buildout was expected to absorb over $10tn in US spending from 2025 to 2032, but rising financing costs and project delays have cut that outlook; analysts cited by the FT see only about 35% of planned data-center projects as highly feasible, and higher borrowing costs for data centers are now reducing chip orders.

**「Impact」** The uncertainty is weighing on semiconductor and AI-related cloud stocks, with CoreWeave falling more than 11% on Friday and the Philadelphia Semiconductor Index matching its longest losing streak since 2006.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ainvest.com/news/chip-index-longest-losing-streak-2008-bet-ai-paid-2610/">The Chip Index&#x27;s Longest Losing Streak Since 2008 Is a Bet on ...</a></li>

</ul>
</details>

**Tags**: `#AI基础设施`, `#数据中心`, `#半导体`, `#融资压力`, `#市场风险`

---

<a id="item-finance-news-2"></a>
### [One Year After China’s Food Delivery Subsidy War, Platform Profits Rebound as Merchants and Riders Bear Costs](https://www.latepost.com/news/dj_detail?id=3762) ⭐️ 7.0/10

A year after China’s food delivery subsidy war, platform operating profit has rebounded, with Meituan and Alibaba’s combined daily orders at nearly 140 million in September—50% above the pre-war 90 million—while rider per-order income in first- and second-tier cities fell to 7-8.5 yuan.

telegram · zaihuapd · Oct 18, 07:40

**「Background」** The subsidy war began after March last year, and platform sales expenses are now nearly back to pre-war levels.

**「Impact」** The cost shift has hit merchants: listed tea and coffee chains reported generally lower per-store revenue and profit, while Haidilao’s first-half revenue rose 1.6 billion yuan but net profit rose only 9.4 million yuan, with 1 billion yuan from delivery.

**Tags**: `#food delivery`, `#platform economy`, `#merchant costs`, `#rider income`, `#Meituan`

---