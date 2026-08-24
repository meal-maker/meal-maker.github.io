---
layout: default
title: "Horizon Summary: 2026-08-24 (EN)"
date: 2026-08-24
lang: en
---

> From 43 items, 13 important content pieces were selected

---

**Technology News**
1. [MS Paint and Photos Embed Invisible GUID Watermarks](#item-tech-news-1) ⭐️ 8.0/10
2. [SeL4 Security Proofs Complete on AArch64](#item-tech-news-2) ⭐️ 8.0/10
3. [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](#item-tech-news-3) ⭐️ 8.0/10
4. [Xiaomi XuanRing O3 CPU Matches Apple Single-Core, Leads Multi-Core](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenAI Reduces GPT-5.6 Sol API Prices Through Nov 21, 2026](#item-tech-news-5) ⭐️ 7.0/10
6. [Coding expertise is going to collapse from AI reliance](#item-tech-news-6) ⭐️ 7.0/10
7. [Your executable is a SQLite database](#item-tech-news-7) ⭐️ 7.0/10
8. [Does CUDA&\#x27;s Moat Hold Up in Agentic Inferencing?](#item-tech-news-8) ⭐️ 7.0/10
9. [LLM-Based Spatial Software Generates Programmable, Animation-Ready 3D Objects](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic Fable 5 Faces Weak Enterprise Demand Over High Pricing](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Alibaba announces $10.2 billion share placement to fund AI push; shares fall](#item-finance-news-1) ⭐️ 8.0/10
2. [Bitcoin extends gains near $80,000 after biggest 3-day rally since 2023](#item-finance-news-2) ⭐️ 7.0/10
3. [Premarket movers: Alibaba down on $10.2 billion share sale; steel stocks up on U.S.-Canada tariff tension](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [MS Paint and Photos Embed Invisible GUID Watermarks](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

A reverse-engineering analysis found that Microsoft Paint and Photos silently embed invisible GUID watermarks into images that have been AI-manipulated. This occurs even when the AI operation is performed using a local model, meaning output created locally still carries the watermark. The applications also add a visible watermark that users can disable, but the invisible watermark cannot be turned off and is applied without notice. The embedded GUID is per-user, raising privacy concerns because it could potentially be linked to a Microsoft account and used to identify the creator.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**「Background」** Microsoft Paint and Microsoft Photos are built-in Windows applications that have recently gained AI-powered editing features such as generative fill, background removal, and super-resolution. Some of these features can run locally on the user&\#x27;s device, but the apps may still connect to Microsoft servers for licensing or identity-related tasks. An invisible watermark is a modification to image pixels that is not visually apparent but can encode data like a GUID \(globally unique identifier\) for later extraction or tracking.

**「Impact」** Users of MS Paint and Photos who use AI editing features may have unique, non-removable identifiers embedded in their images, potentially exposing their identity if the image is shared.

**「Community Discussion」** Commenters focused on the covert per-user identifier as the core issue rather than AI watermarking, arguing it could enable identification via Microsoft subpoenas and undermine anonymity. Some noted that disclosure exists, but criticized that local generation still results in remote-linked marking.

**Tags**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI-generated content`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [SeL4 Security Proofs Complete on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

Proofcraft.systems announced on 2026-08-21 that the seL4 microkernel&\#x27;s security proofs are now complete for the AArch64 architecture. This marks a major milestone in formal verification of a high-assurance operating system, extending the proofs beyond earlier architectures. The result currently applies only to non-MCS unicore configurations, meaning mixed-criticality and multicore setups are not covered. The completion strengthens seL4&\#x27;s assurance case for security-critical deployments such as embedded and military systems.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**「Background」** seL4 is a formally verified microkernel that was the first operating system kernel with a machine-checked proof of functional correctness; its security proofs extend this to confidentiality and integrity guarantees. The new announcement from Proofcraft completes those security proofs for the 64-bit Arm AArch64 architecture, with support from the UK&\#x27;s National Cyber Security Centre \(NCSC\). The verification currently covers non-MCS \(non-mixed-criticality\) unicore configurations, meaning it does not yet include multicore or mixed-criticality system modes.

**「Impact」** Developers targeting AArch64 in high-assurance environments can now rely on formally verified security properties of seL4, but only for single-core, non-mixed-criticality configurations.

**「Community Discussion」** Commenters highlighted the restriction to non-MCS unicore configurations and raised concerns that side-channel timing attacks could undermine the guarantees. Others discussed seL4 adoption in systems like GenodeOS, LionsOS, and automotive hypervisors, with some arguing broader impact requires native seL4/Linux support.

<details><summary>References</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/sel4-microkernel-achieves-full-formal-security-verification-on-aarch64">seL4 Microkernel Formal Security Proofs Completed on AArch64 ...</a></li>
<li><a href="https://zeli.app/story/49418255">seL4 security proofs now complete on AArch64 | Zeli</a></li>

</ul>
</details>

**Tags**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#operating systems`

---

<a id="item-tech-news-3"></a>
### [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 8.0/10

A Reddit post in r/MachineLearning by /u/No\_Cauliflower7923 describes CCPL \(Causal Consequence-Penalized Learning\), a constrained reinforcement learning approach intended to handle delayed and stochastic violations instead of penalizing the action that merely preceded an observed violation. The method uses a delay-corrected Bellman operator with an adaptive effective discount learned from the consequence-delay distribution, and the post states that a contraction proof holds under unknown stochastic delay. It also introduces an Interventional Consequence Net \(ICN\) pretrained on structural-causal-model labels to estimate each action&\#x27;s marginal causal contribution for attribution, rather than relying on temporal proximity. A stated limitation is that the ICN currently requires access to the environment&\#x27;s structural causal model to generate pretraining labels, so it is not learned end-to-end from observational or interventional data alone, restricting applicability outside benchmark settings where the SCM is known or can be reasonably specified. The author invites contributions and collaborators in constrained/safe RL or causal inference.

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · Aug 24, 12:11

**「Background」** Standard constrained reinforcement learning assigns observed constraint violations to the current action, which fails when consequences are delayed and stochastic; this motivates methods that correct for delay. The Bellman operator is the usual value update in RL, and its contraction property guarantees convergence of iterative value estimation. The work described here uses a delay-corrected Bellman operator with an adaptive effective discount and an Interventional Consequence Net pretrained on structural-causal-model labels for action-level causal attribution.

**「Impact」** Practitioners cannot apply CCPL end-to-end in real-world constrained RL environments where the structural causal model is unknown: the Interventional Consequence Net needs SCM-generated pretraining labels, limiting the method to benchmarks or settings where the SCM is known or can be reasonably specified.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/ccpl-rl/">Causal Consequence-Penalized Learning for delayed constrained ...</a></li>
<li><a href="https://ai.stackexchange.com/questions/11057/what-is-the-bellman-operator-in-reinforcement-learning">terminology - What is the Bellman operator in reinforcement learning?</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#constrained RL`, `#causal attribution`, `#delay-corrected Bellman operator`, `#machine learning research`

---

<a id="item-tech-news-4"></a>
### [Xiaomi XuanRing O3 CPU Matches Apple Single-Core, Leads Multi-Core](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi announced its XuanRing O3, a 10-core all-big-core ARM CPU that it says matches Apple single-threaded Geekbench results and posts a multi-core score above 15,000, a first. The chip includes LPDDR6 support at 113.8 GB/s, a G2-Ultra NX GPU with claimed 85% performance and 64% power improvements, and a 45% NPU AI gain. Xiaomi also unveiled the O100 AI accelerator with 1.22 TB/s bandwidth \(16x a flagship phone\) and the D100, a 3nm autonomous-driving AI chip with a 20-core CPU and 16-core NPU capable of local 200B-parameter model deployment. Community commenters caution that the single-threaded comparison is against Apple&\#x27;s previous generation product and that the multi-core lead comes from using 10 cores versus Apple&\#x27;s 6. They also point out that no power-per-watt data has been provided, and real phone thermal limits previously reduced a similar chip&\#x27;s lab score from over 4,000 to about 3,300.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**「What is Xiaomi&\#x27;s Xring O3?」** Xiaomi&\#x27;s new chip is the Xring O3, a 3nm TSMC system-on-chip with 10 Arm C1-series CPU cores \(peak 4.35 GHz\), a 16-core Arm G2-Ultra NX GPU, and 24 billion transistors. It is the first mobile processor to support LPDDR6 memory at 113.8 GB/s, and Xiaomi reports Geekbench scores of 3,945 single-core and 15,221 multi-core, plus an AnTuTu V11 score of 5.22 million. These benchmark figures are the basis for the claim that it matches Apple&\#x27;s single-threaded performance and exceeds it in multithreaded workloads.

**「Impact」** If Xiaomi ships the O3 in its own smartphones, the company&\#x27;s in-house silicon capability could reduce orders from MediaTek and Qualcomm, hurting two major SoC vendors while raising the bar for Apple&\#x27;s sustained efficiency. The benchmark claim&\#x27;s real-world value remains uncertain until power-per-watt and phone cooling performance are confirmed.

**「Community Discussion」** Commenters mostly agree that missing power-per-watt and phone-limited sustained scores are the critical caveat, with one noting the single-core &\#x27;match&\#x27; is against Apple&\#x27;s prior generation and another pointing out the multithreaded result uses 10 cores versus Apple&\#x27;s 6. Several also see Xiaomi&\#x27;s third-place smartphone scale and chip capability as bad news for MediaTek and Qualcomm.

<details><summary>References</summary>
<ul>
<li><a href="https://gadgets.beebom.com/guides/xiaomi-xring-o3-benchmark-specs">Xiaomi Xring O3: Benchmarks and Specs | Beebom Gadgets</a></li>
<li><a href="https://www.itbear.com/hardware/xiaomi-unveils-three-proprietary-chips-to-build-a-full-ecosystem-ai-computing-foundation/">Xiaomi Unveils Three Proprietary Chips to Build a Full ...</a></li>
<li><a href="https://nokiapoweruser.com/xiaomi-xring-o3-chip-specs-benchmarks/">Xiaomi XRING O3 Specs &amp; Benchmarks: 3nm TSMC, 10-Core CPU ...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#CPUs`, `#ARM`, `#benchmarks`, `#mobile chips`

---

<a id="item-tech-news-5"></a>
### [OpenAI Reduces GPT-5.6 Sol API Prices Through Nov 21, 2026](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI has reduced GPT-5.6 Sol API prices by 20% on input tokens and 33% on output tokens through at least November 21, 2026, according to the pricing page. The revised schedule lists GPT-5.6 Sol at $4.00 per million input tokens, $0.40 for cached input, $5.00 for cache writes, and $20.00 per million output tokens. The reduction makes the model more competitive against offerings from Anthropic and other rivals, although it remains significantly more expensive than GPT-5.6 Luna at $0.20 input and $1.20 output per million tokens.

hackernews · tosh · Aug 24, 15:22 · [Discussion](https://news.ycombinator.com/item?id=49421074)

**「Context for GPT-5.6 pricing」** OpenAI&\#x27;s GPT-5.6 model family is offered through the API in three tiers—Sol, Terra, and Luna—with varying capabilities and per-token prices; Sol is the most capable and most expensive. Pricing is typically listed per million tokens for input, cached input, cache writes, and output. API price reductions like this one are part of ongoing competition among AI providers, and developers commonly track such changes to estimate operational costs.

**「Impact」** Developers using GPT-5.6 Sol via the API will see input costs drop 20% and output costs drop 33% through at least November 21, 2026, directly lowering token-based inference expenses for applications that rely on this model.

**「Community Discussion」** Commenters largely view the cut as part of a broader price war and race to the bottom, with one noting that distillation and open-source models are eroding AI vendors&\#x27; pricing power; others flag practical limitations where Sol underperforms alternatives like Fable for long-horizon &\#x27;vibe coding&\#x27; tasks. One commenter adds that an additional 50% discount on OpenRouter brings Sol to $2/$10 per million tokens, and asks for live price comparisons on Artificial Analysis.

**Tags**: `#OpenAI`, `#API pricing`, `#GPT-5.6`, `#cost reduction`, `#large language models`

---

<a id="item-tech-news-6"></a>
### [Coding expertise is going to collapse from AI reliance](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

The article argues that increasing reliance on AI coding tools risks preventing developers from forming deep software engineering expertise. It draws on enterprise observations where leadership mandates that manually written code is wrong, leading to more code than humans can review and understand. Practitioners in the discussion distinguish between &\#x27;guided&\#x27; coding, which uses integrated LLM assistance while writing and planning, and headless agentic or &\#x27;vibe&\#x27; coding, with guided coding reported as more productive and higher quality. Commenters also note that skill formation requires friction, which LLMs shift rather than eliminate, and some warn that generating AI code faster than it can be reviewed is unsustainable.

hackernews · larsfaye · Aug 24, 15:52 · [Discussion](https://news.ycombinator.com/item?id=49421554)

**「Background」** AI coding tools include LLM-powered assistants that generate code from natural language prompts, with modes ranging from agentic \(autonomous\) to guided \(assisted\) coding. The article draws on the idea that encountering and overcoming difficulty, or &\#x27;friction,&\#x27; is essential for long-term skill formation and deep expertise. However, some practitioners counter that curious individuals can use AI to learn faster, and that friction is not inherently beneficial, framing the broader debate about whether AI reliance helps or hinders software engineering competence.

**「Impact」** Enterprises that mandate AI-assisted coding may already be producing code faster than it can be reviewed and understood, creating a risk of maintenance problems if deep expertise erodes.

**「Community Discussion」** Commenters broadly agree on the risk to expertise but differ on methods: some advocate guided LLM coding as a productive alternative, while others report that engineers who avoid AI end up reviewing poor AI-generated code from colleagues. Several point to enterprise mandates, code review bottlenecks, and the unsustainability of unreviewable AI output as practical concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI Coding will Prevent Expertise | Lars Faye</a></li>
<li><a href="https://www.linkedin.com/posts/larsfaye_previously-i-wrote-agentic-coding-is-a-trap-activity-7485755846581321728-fMhW">Becoming Expert in a Skill-Atrophying World | Lars Faye ... | LinkedIn</a></li>
<li><a href="https://news.ycombinator.com/item?id=49027909">AI Coding Will Prevent Expertise | Hacker News</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#software engineering`, `#LLM`, `#developer productivity`, `#expertise`

---

<a id="item-tech-news-7"></a>
### [Your executable is a SQLite database](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria describes a Linux pattern that stores an ELF executable as a SQLite database file by setting the 4-byte application ID at offset 68 to &\#x27;SELF&\#x27; \(Structured Executable &amp; Linkable Format\). The ELF components are reorganized into SQLite tables using a published schema, and a self-exec interpreter extracts and runs them. The Linux binfmt\_misc mechanism can be registered to automatically invoke the interpreter whenever a file matching the SELF pattern at offset 68 is executed; Simon Willison shows a registration line for non-NixOS systems. This demonstrates a clever reuse of SQLite as an executable container format, though it depends on custom kernel registration.

rss · Simon Willison · Aug 24, 11:38

**「Background」** SQLite reserves a 4-byte application ID field at byte offset 68 for identifying file subtypes. ELF is the standard executable and linking format on Linux, and binfmt\_misc lets administrators register custom binary formats by matching a magic byte sequence at a specified offset and running a user-space interpreter.

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#Executable Format`, `#Systems Programming`

---

<a id="item-tech-news-8"></a>
### [Does CUDA&\#x27;s Moat Hold Up in Agentic Inferencing?](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 7.0/10

SemiAnalysis examines whether CUDA&\#x27;s competitive moat remains intact for agentic inference workloads. The analysis cites an open-sourced dataset that cost $3 million USD, support for context lengths over 1 million tokens, multi-turn interactions with sub-agents achieving a 95%+ KV cache hit rate, and comparisons of NVIDIA GB300 NVL72, AMD MI355, and NVIDIA B200. The piece focuses on how long context and KV cache reuse could shift hardware and software advantages in emerging agentic AI.

rss · Semianalysis · Aug 24, 00:19

**「Background」** Agentic inference workloads involve multi-turn interactions where an LLM calls tools and coordinates sub-agents, creating long conversational contexts and making KV cache reuse critical; SemiAnalysis reports sub-agent KV cache hit rates above 95% in this setting. NVIDIA’s CUDA ecosystem has long served as a software moat for GPU compute, but alternatives are emerging: the SemiAnalysis evaluation spans over 1,000 chips including AMD MI355X and NVIDIA GB300 NVL72, while SambaNova claims its SN50 RDU delivers 5× the speed and 3× the throughput of a Blackwell B200 for agentic inference. MLCommons has also introduced an agentic inference benchmark within MLPerf Endpoints to standardize such measurements.

**「Impact」** For agentic inference workloads with 40–60 second end-to-end latency, AMD MI355X using ATOM beats NVIDIA GB300 NVL72 running vLLM on performance per dollar. However, earlier InferenceX v2 results indicate that disaggregated inference on MI355Xs can underperform at higher interactivity levels due to ROCm optimization gaps, while NVIDIA TensorRT LLM on GB200/GB300 NVL72 delivers more than double the performance at high throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv 3 : Does CUDA Moat Hold up in Agentic ...</a></li>
<li><a href="https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference">Introducing the SN50 RDU: Purpose-Built for Agentic Inference</a></li>
<li><a href="https://mlcommons.org/2026/07/agentic-inference-for-mlperf-inference/">Agentic Inference for MLPerf Inference - MLCommons</a></li>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?</a></li>
<li><a href="https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs">InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper - Formerly InferenceMAX</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#agentic AI`, `#CUDA`, `#GPU hardware`, `#KV cache`

---

<a id="item-tech-news-9"></a>
### [LLM-Based Spatial Software Generates Programmable, Animation-Ready 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

A Reddit post by one of the paper&\#x27;s co-authors introduces a method that uses large language models to generate 3D objects as executable spatial programs rather than monolithic mesh outputs. The author claims these objects are inherently programmable and animation-ready, with full hierarchical structure, hinge/socket articulation, and logic to adapt their appearance to weak or powerful compute environments. The approach currently lags behind traditional AI 3D generators for complex organic shapes, but the author argues that software-like 3D will eventually dominate and that industrial design, game development, simulations, and AR/VR/XR will be most affected.

reddit · r/MachineLearning · /u/mhb\_11 · Aug 24, 19:10

**「Context: 3D generation approaches」** Conventional AI 3D model generators like Meshy.ai, Tripo3D, and Luma AI&\#x27;s Genie typically output static mesh files in formats such as GLB, OBJ, FBX, and USD. Some Blender add-ons \(e.g., BlenderGPT, 3D-Agent\) generate editable models by executing Python scripts, but they remain within a mesh-editing paradigm. This work treats the 3D object itself as executable spatial code, enabling hierarchical structure and articulation from the outset.

**「Impact」** Game developers, simulation builders, and AR/VR/XR creators could obtain 3D assets that are programmable and articulated at authoring time, though the post does not provide quantitative validation against traditional generators.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/AI_3D_model_generators">AI 3D model generators — Grokipedia</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#large language models`, `#spatial programming`, `#procedural generation`, `#research`

---

<a id="item-tech-news-10"></a>
### [Anthropic Fable 5 Faces Weak Enterprise Demand Over High Pricing](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) ⭐️ 7.0/10

Anthropic&\#x27;s flagship Fable 5 model is seeing weak enterprise demand, with Ramp data showing it accounted for only about 6% of Anthropic API token usage and 11% of spend in its first month. Priced at about $10 per million input tokens and $50 per million output tokens, it is roughly twice as expensive as Anthropic&\#x27;s other flagship models and pricier than OpenAI&\#x27;s GPT-5.6 Sol. Cheaper open-source models and Microsoft&\#x27;s in-house models are drawing customers away, and Anthropic&\#x27;s 30-day data retention requirement is further suppressing adoption. Ramp&\#x27;s economists interpret this as evidence that enterprises&\#x27; willingness to pay for frontier AI has reached a ceiling.

telegram · zaihuapd · Aug 24, 01:22

**「Context」** Anthropic’s Fable 5 is the company’s flagship model, priced at about $10 per million input tokens and $50 per million output tokens. Ramp, a spend-management platform, tracks token usage and dollar spending across roughly 70,000 businesses, offering third-party data on enterprise adoption. The model competes with OpenAI’s GPT-5.6 Sol, Anthropic’s own lower-priced Claude Opus 5, and open-source or Microsoft alternatives.

**「Impact」** Enterprise customers evaluating Anthropic API usage are shifting token consumption and spend toward cheaper open-source or Microsoft alternatives, limiting Fable 5&\#x27;s initial share to about 6% of token usage and 11% of spend.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes">Ramp: Anthropic&#x27;s Fable 5 Plateaus at 11% as Opus 5 Overtakes</a></li>
<li><a href="https://xenospectrum.com/en/fable-5-enterprise-adoption/">Despite Top Performance, Fable 5 Adoption Lags: How Much Will ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#enterprise software`, `#Anthropic`, `#model pricing`, `#open source competition`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Alibaba announces $10.2 billion share placement to fund AI push; shares fall](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 8.0/10

Alibaba announced an $10.2 billion \(HK$80 billion\) placement of 710 million newly issued shares to non-U.S. investors to fund AI infrastructure. The shares were priced at HK$112.70 apiece, a discount to Friday&\#x27;s HK$123 close, and the stock fell as much as 10%.

rss · CNBC Finance · Aug 24, 08:21

**「Background」** The placement comes days after Alibaba reported a 75% drop in June-quarter profit and a 75% jump in capital expenditure to 67.7 billion yuan, amid a broader ramp-up in AI spending by Chinese tech firms.

**Tags**: `#Alibaba`, `#share placement`, `#AI investment`, `#Hong Kong stocks`, `#capital expenditure`

---

<a id="item-finance-news-2"></a>
### [Bitcoin extends gains near $80,000 after biggest 3-day rally since 2023](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 7.0/10

Bitcoin and crypto stocks extended gains on Monday after a more than 20% three-day rally—the largest since 2023—with bitcoin trading just under $80,000.

rss · CNBC Finance · Aug 24, 20:02

**「Background」** The move followed the Treasury&\#x27;s announcement that it would double purchases of longer-dated government bonds, briefly lowering yields and reviving demand for risk assets.

**Tags**: `#Bitcoin`, `#cryptocurrency`, `#ETF inflows`, `#market rally`, `#Treasury policy`

---

<a id="item-finance-news-3"></a>
### [Premarket movers: Alibaba down on $10.2 billion share sale; steel stocks up on U.S.-Canada tariff tension](https://www.cnbc.com/2026/08/24/stocks-making-the-biggest-moves-premarket-baba-mrvl-sndk-and-more.html) ⭐️ 7.0/10

Alibaba&\#x27;s U.S.-listed shares fell 2% in premarket trading after the company announced a $10.2 billion sale of new shares to non-U.S. investors to fund AI projects, while Nucor rose more than 4% and Steel Dynamics rose 3.5% after U.S.-Canada trade talks collapsed and Canada targeted U.S. steel with Sept. 8 tariffs.

rss · CNBC Finance · Aug 24, 11:31

**「Background」** Monday&\#x27;s premarket moves follow a week in which the iShares Semiconductor ETF fell 5.5% and bitcoin surged 22% over three days before stalling around $77,000.

**Tags**: `#premarket`, `#Alibaba`, `#semiconductors`, `#steel tariffs`, `#cryptocurrency`

---