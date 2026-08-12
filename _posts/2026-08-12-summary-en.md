---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 45 items, 16 important content pieces were selected

---

**Technology News**
1. [Qwen3.8-2.4T-A95B Open-Weight MoE Model Released on Hugging Face](#item-tech-news-1) ⭐️ 9.0/10
2. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-tech-news-2) ⭐️ 8.0/10
3. [LTX Releases Open-Source LTX-2.5 Video Model That Runs on One RTX 5090](#item-tech-news-3) ⭐️ 8.0/10
4. [xAI Releases Grok 4.6 for Long-Running Agent Tasks](#item-tech-news-4) ⭐️ 8.0/10
5. [Why tiny JPEGs look different in Chrome](#item-tech-news-5) ⭐️ 7.0/10
6. [uBlock Origin Stops Trying to Block Facebook Ads](#item-tech-news-6) ⭐️ 7.0/10
7. [AI is removing the middle class of software engineering?](#item-tech-news-7) ⭐️ 7.0/10
8. [Basis Dependence Explains Adam&\#x27;s Loss of Implicit Low-Rank Bias](#item-tech-news-8) ⭐️ 7.0/10
9. [Enterprise SSDs hit 48% of NAND shipments; YMTC enters top three](#item-tech-news-9) ⭐️ 7.0/10
10. [WeChat Releases WeLM: Resource-Efficient 80B and 617B MoE LLMs](#item-tech-news-10) ⭐️ 7.0/10

**Technology Blog**
1. [Day 0 Support for Qwen3.8-2.4T-A95B on vLLM](#item-tech-blog-1) ⭐️ 5.0/10

**Financial News**
1. [CME Group plans first AI computing power futures contracts](#item-finance-news-1) ⭐️ 8.0/10
2. [Tencent Q2 2026 Revenue Beats Estimates as AI Capex Surge Turns Free Cash Flow Negative](#item-finance-news-2) ⭐️ 8.0/10
3. [Wendy&\#x27;s jumps 13% on reported Trian take-private bid; AI and tech stocks rally midday](#item-finance-news-3) ⭐️ 7.0/10
4. [Premarket movers: CoreWeave, Super Micro rise on earnings and guidance](#item-finance-news-4) ⭐️ 7.0/10
5. [Electric cars reach 65.1% of China&\#x27;s July passenger car sales as overall market drops](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Qwen3.8-2.4T-A95B Open-Weight MoE Model Released on Hugging Face](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen released Qwen3.8-2.4T-A95B, a mixture-of-experts language model with 2.4 trillion total parameters and 95 billion active parameters, on Hugging Face. The model&\#x27;s native context length is 262,144 tokens, expandable to 1,010,000 tokens, and it is available in BF16 and FP8 formats. Community benchmarks and the model card place its performance between Claude Opus 4.8 and Fable 5, making it competitive with frontier models. At launch, only BF16 and FP8 weights are provided; no QAT 4-bit quantization is offered, which may make serving more resource-intensive than comparable Kimi K3 until lower-precision versions appear.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**「Background」** Qwen3.8-2.4T-A95B is an open-weight sparse mixture-of-experts \(MoE\) model, meaning it has 2.4 trillion total parameters but only activates 95 billion per token, reducing computational cost. It is the open-weight variant of Qwen3.8-Max, which adds vision input, non-thinking support, a 1M-token default context length, and built-in tools.

**「Impact」** For users with under $50 million annual revenue, the model is free for internal use, but larger organizations face serving restrictions; deployment also currently requires handling BF16 or FP8 weights, with no official 4-bit quantization.

**「Community Discussion」** Commenters view Qwen3.8-2.4T-A95B as a Kimi K3 rival, but note the launch weights \(BF16/FP8\) make it harder to serve than K3 until QAT 4-bit quantization is released. Some highlight Unsloth&\#x27;s 397GB 1-bit quant as making Opus 4.5-level performance accessible on consumer hardware, while others point out the open-weight model lacks vision input, non-thinking support, and the 1M-token default context available in the official Qwen3.8-Max.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen 3 . 8 2 . 4 T A 95 B - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Open Source`, `#MoE`, `#Machine Learning`

---

<a id="item-tech-news-2"></a>
### [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale traced a database corruption issue to a 16-year-old SQLite WAL-reset bug. The company funded development of an open-source SQLite VFS shim that helped isolate the race condition almost immediately and is expected to aid in debugging similar bugs. The investigation involved a single Go process exclusively accessing the database, though commenters note the underlying SQLite bug can occur with multiple connections. The writeup provides a detailed technical account of the long-standing bug and the funded debugging tooling.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**「Background」** SQLite&\#x27;s write-ahead logging \(WAL\) mode allows concurrent readers and a writer by recording changes in a separate WAL file, and a WAL reset truncates or marks that file after checkpoints. Tailscale runs SQLite as a single-writer coordination server and traced database corruption and prior outages to a race between a write transaction and a WAL reset; the SQLite team&\#x27;s writeup states the bug requires WAL mode and multiple open connections to the same database file. To isolate the issue, Tailscale funded an open-source SQLite VFS shim for debugging and also took out a support contract with the SQLite team.

**「Impact」** Tailscale&\#x27;s debugging effort produced a reusable open-source SQLite VFS shim, giving other developers a tool to isolate similar SQLite race conditions and potentially preventing future corruption.

**「Community Discussion」** Commenters praised the detailed writeup and Tailscale&\#x27;s funding of the debugging tool, with one clarifying that the SQLite bug occurs only with multiple connections. Others noted the value of tests and support contracts in catching such long-standing bugs.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49272832">Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug | Hacker News</a></li>
<li><a href="https://www.theregister.com/databases/2026/08/12/tailscale-says-deeply-buried-16-year-old-sqlite-bug-caused-last-years-outages/5287004">Tailscale says deeply buried 16-year-old SQLite bug caused last year&#x27;s outages</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#database`, `#debugging`, `#tailscale`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [LTX Releases Open-Source LTX-2.5 Video Model That Runs on One RTX 5090](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX has released LTX-2.5, an open-source video generation foundation model whose weights, training code, and inference pipeline are all publicly available. The model supports text-to-video and image-to-video generation and can run locally on a single RTX 5090; it is free for commercial use for entities with under $10 million annual revenue. It improves multi-shot coherence and prompt adherence, and introduces a new diffusion video decoder and a Gemma 4 12B text encoder. In a text-to-video artifact evaluation across 98 prompts, LTX 2.5 Pro ranked first among ten models.

telegram · zaihuapd · Aug 12, 02:15

**「Background」** Open-weight video generation models are increasingly released to let developers run models locally on their own hardware instead of relying solely on cloud APIs. LTX describes open source as central to scaling world models and positions LTX-2.5 as the latest open-world video generation model, with NVIDIA highlighting it as a foundation for use cases across media, entertainment, robotics, and real-time applications.

**「Impact」** AI practitioners and organizations with under $10 million annual revenue can run a competitive open-source video generation model locally on a single RTX 5090 without licensing fees.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/open-source">LTX-2.5 Model Open Source: AI Video Generator</a></li>
<li><a href="https://blogs.nvidia.com/blog/local-ai-open-source-models-agents-nemotron/">NVIDIA and Local AI Community Fuel Open Source Models and Intelligent Agents | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#video-generation`, `#AI model`, `#local inference`, `#text-to-video`

---

<a id="item-tech-news-4"></a>
### [xAI Releases Grok 4.6 for Long-Running Agent Tasks](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI released Grok 4.6 on August 12, 2026, an incremental upgrade to Grok 4.5 focused on long-running agent interactions and visual tasks. The model matches GPT-5.6 Sol on the Artificial Analysis Intelligence Index across nine benchmarks. It is available immediately through Cursor, Grok Build, and the API at $2 per million input tokens and $6 per million output tokens, with a faster version priced at double. For the first week, xAI is offering double usage in Grok Build and Cursor. The release is meant to improve performance for AI agent workloads.

telegram · zaihuapd · Aug 12, 15:54

**「Background」** Grok is xAI&\#x27;s series of large language models, with Grok 4.5 as the immediate predecessor. Long-running agent tasks require sustained context, tool use, and visual reasoning, while the Artificial Analysis Intelligence Index aggregates nine benchmarks for comparing frontier models. The update targets these capabilities rather than a wholesale architecture change.

**「Impact」** Developers using Cursor, Grok Build, or the xAI API can immediately use a model with GPT-5.6 Sol-level benchmark scores and introductory doubled usage for the first week, at $2 per million input tokens and $6 per million output tokens.

**「Community Discussion」** Comments are split: some praise Grok 4.6 as cheaper than Kimi K3 and stronger than GPT-5.6 Sol on most benchmarks, while others suspect benchmark hacking or find a default system prompt causes refusals to discuss system prompts. A user notes Grok 4.5&\#x27;s concise, fast responses were preferable to GPT-5.6 Sol and Claude for agent use.

**Tags**: `#AI`, `#LLM`, `#AI agents`, `#xAI`, `#Grok`

---

<a id="item-tech-news-5"></a>
### [Why tiny JPEGs look different in Chrome](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

An investigation examines why small JPEG images render differently in Chrome compared with other browsers, focusing on Chrome’s scaling optimizations. Commenters report that the same issue affects PNGs and caused icon problems in an Electron release after Chrome introduced the optimization, prompting a hold on upgrades. Chrome and Firefox use different scaling algorithms: Chrome is blurrier in general, while Firefox is sharper but has slightly more ringing artifacts. The practical advice is not to use JPEG for icons and to use images at an appropriate resolution for the size they will be displayed. Firefox is working on decompressing at a lower scale, tracked in Bugzilla bug 2033250.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**「Background」** When browsers display an image at smaller dimensions than its original size, they must downsample it; different resampling algorithms trade blurriness against ringing artifacts. Chrome includes a performance optimization that can decode JPEG and PNG images at a reduced scale or use lower-quality filtering for small displayed sizes, which can make tiny graphics such as icons look visibly different from Firefox or Safari. Firefox is tracking work to implement lower-scale decompression as well, so the difference may change in future versions.

**「Impact」** Web developers who use small JPEG or PNG icons may see inconsistent rendering across Chrome and Firefox, and an Electron upgrade incorporating Chrome’s optimization can visibly alter icons, so they should test or use appropriately sized PNGs.

**「Community discussion」** Commenters note the scaling difference also affects PNGs and caused icon issues in an Electron upgrade. One recommends using appropriately sized images instead of JPEG for icons, and another points to Firefox’s lower-scale decompression work in bug 2033250 while preferring Firefox’s sharper scaling.

**Tags**: `#JPEG`, `#Chrome`, `#image scaling`, `#browser rendering`, `#web development`

---

<a id="item-tech-news-6"></a>
### [uBlock Origin Stops Trying to Block Facebook Ads](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 7.0/10

uBlock Origin has reportedly stopped trying to block ads on Facebook, according to a Digital Escape Tools article referencing Reddit and Neowin. The decision follows Facebook&\#x27;s increasingly sophisticated anti-adblocking measures that make filtering ads technically impractical. The development, posted to Hacker News, generated 259 points and 360 comments as of the source snapshot. Commenters describe an ad-blocking arms race and note that users may eventually need computer vision models to classify on-screen ads. Some users say they will leave Facebook rather than view ads, while others question the business logic of targeting ad-blocker users.

hackernews · Markoff · Aug 12, 11:28 · [Discussion](https://news.ycombinator.com/item?id=49270726)

**「Background」** uBlock Origin \(uBO\) is a widely used open-source browser extension that blocks ads and trackers using filter lists, which are rule sets maintained by the project and volunteers. Facebook has engaged in an escalating anti-adblocking arms race by frequently changing its ad delivery code to evade these lists, making sustained blocking difficult. In August 2026, the uBO developer announced that the project would stop updating custom filters designed specifically for Facebook ads, meaning new ad circumventions would no longer be patched and users should expect ads to appear.

**「Impact」** Users of uBlock Origin on Facebook will likely see ads they previously could filter out, unless they adopt alternative blocking tools or stop using the platform.

**「Community Discussion」** Comments largely frame the situation as an escalating arms race, with predictions that ad blocking will move to computer vision models that overlay rectangles on ad-like elements. Some users say they will leave Facebook rather than tolerate ads, while others question whether bypassing blockers yields meaningful revenue from users unlikely to click.

<details><summary>References</summary>
<ul>
<li><a href="https://www.neowin.net/news/facebook-ads-are-so-hard-to-block-that-ublock-origin-stopped-filtering-them/">Facebook ads are so hard to block that uBlock Origin ... - Neowin</a></li>
<li><a href="https://privacysavvy.com/news/cybersecurity/ublock-origin-stops-facebook-ad-filters/">uBlock Origin Stops Updating Filters Designed to Block Facebook ...</a></li>
<li><a href="https://piunikaweb.com/2026/08/10/ublock-origin-facebook-ads-not-blocking/">Seeing ads on Facebook even with uBlock Origin ? - PiunikaWeb</a></li>

</ul>
</details>

**Tags**: `#ad-blocking`, `#uBlock Origin`, `#Facebook`, `#privacy`, `#open source`

---

<a id="item-tech-news-7"></a>
### [AI is removing the middle class of software engineering?](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 7.0/10

This opinion piece argues that AI is removing the &\#x27;middle class&\#x27; of software engineering by automating routine coding work, thereby eliminating the traditional hand-off from senior designers to mid-level implementers. It prompts significant debate on Hacker News, with some commenters agreeing that AI amplifies poor engineering and others contesting whether the trend is supported by evidence. The piece is characterized as timely and widely discussed but lacking technical depth or data.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**「Background」** The &quot;middle class&quot; of software engineering refers to mid-level engineers whose work often involves translating specifications into routine code, a role that AI coding tools are increasingly able to automate. Florian Herrengt&\#x27;s blog post argues that because companies have historically paid high salaries for engineers who do more than just turn specs into working code, AI will likely widen the salary gap rather than eliminate all engineering jobs.

**「Impact」** If the argument is correct, mid-level developers focused on routine implementation may face reduced demand as seniors can directly generate code with AI; however, commenters note there is not yet irrefutable evidence of actual software engineering job losses attributable to LLM coding agents.

**「Community Discussion」** Commenters generally debate whether AI eliminates mid-level coding roles or merely shifts responsibilities upward, with some describing it as automating the &\#x27;Stack Overflow engineer&\#x27; hand-off and others warning against outsourcing critical thinking to LLMs. Several also question the lack of concrete evidence for job losses and raise economic arguments that tool improvements may lead to little net employment change.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html">AI is removing the middle class of software engineering</a></li>
<li><a href="https://blog.florianherrengt.com/">Blog – Florian Herrengt</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#labor market`, `#technology industry`, `#opinion`

---

<a id="item-tech-news-8"></a>
### [Basis Dependence Explains Adam&\#x27;s Loss of Implicit Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 7.0/10

A new study on factored models W = UV^T finds that the loss is basis-invariant under rotations, but Adam&\#x27;s per-coordinate second moment depends on the factor basis; this basis dependence is proposed as the mechanism that separates optimizers by implicit low-rank bias. In underdetermined matrix sensing with nine update rules matched at equal training loss, GD, shared-scalar Adam, Muon, and Shampoo retained the low-rank bias, while Adam, RMSProp, Lion, signum, and Adafactor lost it. A one-parameter interpolation from Adam&\#x27;s per-coordinate denominator to a single shared scalar produced monotonic recovery improvement, indicating anisotropy rather than adaptivity causes the loss of bias. Muon was exact on truly low-rank targets but degraded fastest with added spectral tail and ceded to GD near 4% tail energy, while a global-norm clip change improved the author&\#x27;s earlier optimizer recovery error from 0.347 to 0.220. The paper includes caveats that the 43–44% held-out error reduction on hyperspectral data uses a train-only learning-rate rule and that momentum results are empirical, with theory covering memoryless rules only.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**「Background」** Factored models such as W = U V^T are common in matrix sensing and transformer weights, and their loss is invariant under gauge rotations \(U,V\) → \(UQ, VQ\) because only the product affects the loss. Gradient descent preserves this invariance due to its linear update rule, but adaptive optimizers like Adam use per-coordinate second-moment estimates that depend on the chosen basis, breaking the symmetry and making the optimizer&\#x27;s trajectory basis-dependent. This mechanism is relevant to implicit bias: optimizers that preserve gauge symmetry tend to inherit gradient descent&\#x27;s low-rank bias, while basis-dependent updates can select different interpolants.

**「Impact」** Practitioners using factored models should be aware that Adam, RMSProp, Lion, signum, and Adafactor may lose GD&\#x27;s implicit low-rank bias in underdetermined matrix sensing, while shared-scalar Adam, Muon, and Shampoo preserve it.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05136">The Loss Does Not See the Basis, but Adam Does</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#Adam`, `#implicit bias`, `#matrix sensing`

---

<a id="item-tech-news-9"></a>
### [Enterprise SSDs hit 48% of NAND shipments; YMTC enters top three](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 7.0/10

Counterpoint reported that enterprise SSDs accounted for 48% of global NAND shipments in Q2 2026, nearly double the year-earlier share, driven by AI inference workloads. Industry revenue increased fivefold year over year. Samsung led with 25% share, followed by SK hynix at 22%. Yangtze Memory Technologies Co. \(YMTC\) reached 14% share and entered the top three suppliers for the first time, surpassing Kioxia, though its consumer-focused product mix kept it at only fifth in revenue. Counterpoint expects enterprise SSDs to consume more than half of all NAND bits by the end of the year.

telegram · zaihuapd · Aug 12, 11:00

**「Background」** NAND flash is the nonvolatile memory used in SSDs; enterprise SSDs are high-performance drives designed for data-center servers and AI infrastructure. Market share is typically measured both by bits shipped and by revenue, and Samsung, SK hynix, Kioxia, and Micron have historically been leading suppliers. YMTC is a Chinese NAND maker that has been expanding its presence in the global market.

**「Impact」** The shift means AI-driven data-center storage demand is redrawing NAND supplier rankings, with YMTC now a top-three volume supplier even though its consumer-heavy mix keeps its revenue rank lower.

**Tags**: `#enterprise SSD`, `#NAND`, `#YMTC`, `#AI infrastructure`, `#storage market`

---

<a id="item-tech-news-10"></a>
### [WeChat Releases WeLM: Resource-Efficient 80B and 617B MoE LLMs](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 7.0/10

The WeChat team has released WeLM, a general-purpose large language model family designed for extreme resource efficiency to scale AI across WeChat&\#x27;s massive user scenarios. WeLM-80B, with 3B active parameters out of 80B total, is already deployed in WeChat&\#x27;s in-app AI agent Xiaowei, supporting conversation and search, operating native WeChat functions, and invoking mini-program services. A larger WeLM-617B model with 23B active parameters out of 617B total uses a mixture-of-experts \(MoE\) architecture and is under development to deliver stronger general understanding and reasoning at moderate activation scale. This 617B model will later be applied to complex tasks in the WeChat ecosystem, including intelligent mini-program development and WeChat Xiaowei gadget generation.

telegram · zaihuapd · Aug 12, 13:58

**「Background」** Resource-efficient large language models often use mixture-of-experts \(MoE\) architectures, where only a subset of total parameters is active per token, reducing compute while increasing capacity. WeChat&\#x27;s WeLM blog previously described an 80B total/3B active MoE trained on under 14T tokens, and the item notes this model is already integrated into WeChat&\#x27;s &\#x27;Xiaowei&\#x27; AI assistant. A newer 617B total/23B active MoE was demonstrated in Hidden Decoding research, achieving open-source-leading evaluation results with incremental continued training using only 5.3% of full training compute.

**「Impact」** WeChat users now have an in-app AI agent powered by WeLM-80B \(3B active parameters\), and developers can expect the 617B MoE model to handle complex mini-program and gadget-generation tasks in future WeChat releases.

<details><summary>References</summary>
<ul>
<li><a href="https://hao.cnyes.com/post/260644">把思考折疊進序列：WeLM 617B MoE的隱式Scaling路徑 | 科技 | 鉅亨號 | Anue鉅亨</a></li>
<li><a href="https://finance.sina.cn/2026-07-24/detail-iniiwrah9261623.d.html?vt=4&amp;cid=76993&amp;node_id=76993">把思考折叠进序列：WeLM 617B MoE的隐式Scaling路径|scaling law|Token|大模型|微信|博客_手机新浪网</a></li>
<li><a href="https://welm.weixin.qq.com/posts/building-effective-sparse-moe-models-with-moderate-resources/">以适度资源构建高效稀疏 MoE 模型 | WeLM Blog</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#WeChat`, `#MoE`, `#AI agent`, `#resource efficiency`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Day 0 Support for Qwen3.8-2.4T-A95B on vLLM](https://vllm.ai/blog/2026-08-12-qwen3.8) ⭐️ 5.0/10

rss · vLLM Blog · Aug 12, 00:00

**「Background」** The vLLM Team and Inferact announce day-0 support for Qwen3.8-2.4T-A95B, a 2.4-trillion-parameter sparse Mixture-of-Experts model that is the first Qwen-Max-class open-weight release. Running such a large model has required at least two NVIDIA B300 or AMD MI355X nodes unless the FP4-quantized version is used, so reducing memory and bandwidth is the central challenge.

**「Solution」** Because the model reuses the Qwen 3.5 architecture, vLLM runs it with no architecture changes, supporting FP8, BF16, NVFP4, and MXFP4 checkpoints. The authors&\#x27; key mechanism for cost reduction is FP4 quantization of selected layers including routed experts, using round-to-nearest quantization with activation calibration to enable 4-bit activations. The announcement reports near-equal accuracy on GSM8K \(about 90% strict\) and AIME25 @3 \(about 88% average FP8 vs 92% NVFP4\), though it notes that a larger reasoning budget is required and only two benchmarks are shown. On NVIDIA, the team co-developed fused kernels for linear attention \(Gated Delta Rule\), GQA, dense GEMMs, and MoE routing, and tuned a hybrid parallelization of data + tensor parallelism for attention and expert parallelism for MoE. On AMD, AITER-fused Gated DeltaNet decode, attention, and MoE kernels reduce launch and data-movement overhead; the shared-expert path uses hipBLASLt GEMMs while routed experts use AITER FusedMoE, and AMD Quark enables MXFP4. The article also provides recommended generation parameters \(temperature 1.0, top\_p 0.95, top\_k 20\) and advises allocating a high max\_tokens budget because the model is a reasoning model.

**「Takeaway」** Day-0 vLLM support, FP4 quantization, and co-developed cross-vendor kernels make the first open-weight Qwen-Max-class MoE model deployable at lower memory cost, but the reported quality evidence is preliminary and requires increased reasoning budget.

**Tags**: `#vLLM`, `#Qwen`, `#sparse MoE`, `#quantization`, `#model serving`

---

## Financial News

<a id="item-finance-news-1"></a>
### [CME Group plans first AI computing power futures contracts](https://www.cnbc.com/2026/08/11/ai-computing-power-becomes-a-tradable-asset-class-as-cme-starts-futures.html) ⭐️ 8.0/10

CME Group plans to launch the first futures contracts tied to AI computing power on Oct. 5, pending regulatory approval, based on Silicon Data indexes that track hourly Nvidia H100 and Blackwell B200 GPU rental prices. Each contract will represent one month&\#x27;s rent for an Nvidia H100, giving companies and investors a way to trade and hedge AI computing capacity.

rss · CNBC Finance · Aug 12, 14:14

**「Background」** The launch is part of a broader push by Wall Street to finance and gain exposure to the massive AI infrastructure buildout, with Nvidia and asset managers exploring an effort that could channel as much as $500 billion into AI infrastructure.

**「Impact」** The contracts would allow AI developers and data-center operators to hedge their computing costs or revenues, and investors to gain exposure to AI computing prices without owning chips or data centers.

**Tags**: `#AI`, `#futures`, `#CME Group`, `#Nvidia`, `#financial innovation`

---

<a id="item-finance-news-2"></a>
### [Tencent Q2 2026 Revenue Beats Estimates as AI Capex Surge Turns Free Cash Flow Negative](https://wallstreetcn.com/articles/3779275) ⭐️ 8.0/10

Tencent&\#x27;s Q2 2026 revenue rose 11% year on year to 204.8 billion yuan, slightly above Bloomberg&\#x27;s estimate, while capital spending nearly tripled to 52.8 billion yuan and pushed free cash flow to -13.8 billion yuan.

telegram · zaihuapd · Aug 12, 10:30

**「Background」** The company said that excluding AI compute prepayments, free cash flow would have been 37.6 billion yuan, and net profit rose only 0.7% to 56.0 billion yuan, below market expectations.

**Tags**: `#腾讯`, `#财报`, `#资本开支`, `#AI投资`, `#自由现金流`

---

<a id="item-finance-news-3"></a>
### [Wendy&\#x27;s jumps 13% on reported Trian take-private bid; AI and tech stocks rally midday](https://www.cnbc.com/2026/08/12/stocks-making-the-biggest-moves-midday-wen-hrb-qnt-crwv-cava.html) ⭐️ 7.0/10

CNBC reports the biggest midday stock moves, led by Wendy&\#x27;s 13% jump after The Financial Times reported, citing sources, that Nelson Peltz&\#x27;s Trian Fund Management was preparing a bid to take the company private.

rss · CNBC Finance · Aug 12, 16:53

**「Background」** The source attributes the Wendy&\#x27;s move to an FT report citing unnamed sources; other moves were driven by earnings and guidance results compared with FactSet or LSEG consensus estimates.

**Tags**: `#stock market`, `#earnings`, `#mergers and acquisitions`, `#artificial intelligence`

---

<a id="item-finance-news-4"></a>
### [Premarket movers: CoreWeave, Super Micro rise on earnings and guidance](https://www.cnbc.com/2026/08/12/stocks-making-the-biggest-moves-premarket-crwv-smic-cohr.html) ⭐️ 7.0/10

AI infrastructure and consumer stocks moved sharply in premarket trading after earnings and guidance, led by CoreWeave up more than 18.5% and Super Micro Computer up more than 7.5%. Super Micro guided first-quarter adjusted EPS to $1.01–$1.10, above the $0.76 LSEG consensus.

rss · CNBC Finance · Aug 12, 12:12

**「Background」** Premarket trading occurs before the regular U.S. session and can react to earnings released after the prior close or before the open; LSEG and FactSet consensus figures are average analyst forecasts used as the comparison baseline.

**Tags**: `#earnings`, `#premarket`, `#stock-movers`, `#guidance`, `#AI-infrastructure`

---

<a id="item-finance-news-5"></a>
### [Electric cars reach 65.1% of China&\#x27;s July passenger car sales as overall market drops](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

New energy vehicles accounted for 65.1% of new passenger cars sold in China in July, up from 54% a year earlier, while overall passenger car sales fell 20.3% in the first seven months, according to industry data.

rss · CNBC Finance · Aug 12, 01:20

**「Background」** Autohome rankings for the six months through July show Geely&\#x27;s Xingyuan electric hatchback was the best-selling model with nearly 197,500 units sold, ahead of Tesla&\#x27;s Model Y with more than 180,000, and BYD&\#x27;s top model, the Yuan UP SUV, placed fifth with nearly 97,700 units.

**Tags**: `#China auto market`, `#electric vehicles`, `#BYD`, `#Geely`, `#Tesla`

---