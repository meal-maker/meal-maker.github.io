---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 33 items, 9 important content pieces were selected

---

**Technology News**
1. [LLM-guided program evolution improves 10 best-known circle-packing solutions](#item-tech-news-1) ⭐️ 8.0/10
2. [KV Cache as an Agent Runtime](#item-tech-news-2) ⭐️ 8.0/10
3. [Huawei releases high-performance chip after six years](#item-tech-news-3) ⭐️ 8.0/10
4. [Git.kernel.org spends more CPU on crawler-rendered commits than legitimate access](#item-tech-news-4) ⭐️ 7.0/10
5. [TPU Inference Externalization Full Steam Ahead - InferenceX](#item-tech-news-5) ⭐️ 7.0/10
6. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-tech-news-6) ⭐️ 7.0/10
7. [Longitudinal LLM Benchmarking: 31,352 Repeated Measurements Reveal Temporal Variation](#item-tech-news-7) ⭐️ 7.0/10
8. [China Supreme Court Clarifies AI Liability for Deepfakes and Price Discrimination](#item-tech-news-8) ⭐️ 7.0/10

**Financial News**
1. [China announces smaller-than-expected $53.6 billion capital injection into state banks and insurers](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [LLM-guided program evolution improves 10 best-known circle-packing solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An LLM-guided iterative program evolution method improved 10 best-known Packomania circle-packing solutions for N=101 through 114 by 2.4% to 5.4% in 15 iterations. Instead of solving the packing directly, an LLM proposed algorithmic changes to a simple seed solver, guided by a scoreboard of results and prior attempt histories; each candidate was scored by an independent verifier so only improvements were kept. The total LLM cost was $27.72, and Packomania independently accepted the updated best-known sum-of-radii values. A paper is available at arxiv.org/abs/2609.05093 and code plus solutions at github.com/ucsandman/discovery-loop. The author highlighted the plateau-detection stopping rule as the component they most want critique on.

reddit · r/MachineLearning · /u/SIGH\_I\_CALL · Sep 7, 16:54

**「Background」** Packomania is a longstanding benchmark collection that maintains best-known circle packings; its csqv series asks for N circles of variable radius inside a unit square with the goal of maximizing the total sum of radii \(and thus packing density\). The new method, a minimal system called Discovery Loop, uses an LLM to propose changes to an optimization algorithm, with an independent verifier scoring candidates so only improvements are kept. The reported 2.4–5.4% gains are therefore comparisons against previously published Packomania best-known records for N=101–114.

**「Impact」** Researchers working on the Packomania csqv benchmark or similar continuous optimization problems can use the published paper and code to reproduce the verified improvements for N=101–114 at a reported LLM cost of $27.72.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing ...</a></li>
<li><a href="https://packomania.com/csqv/csqv.html">The best known packings of unequal circles in a square</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing :Breaking 10...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#program synthesis`, `#optimization`, `#circle packing`, `#benchmark`

---

<a id="item-tech-news-2"></a>
### [KV Cache as an Agent Runtime](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

A Yandex research team proposes treating an LLM&\#x27;s inference state, specifically its KV cache, as an agent runtime to enable more interactive and responsive systems. The approach builds on prior lab papers &\#x27;Hogwild\! Inference&\#x27; and &\#x27;AsyncReasoning&\#x27; and is previewed with a Qwen3.8-27B agent playing DOOM interactively. The team argues that inference/runtime design may be an underexplored axis between changing the model and the harness, offering a middle path for agent capabilities.

reddit · r/MachineLearning · /u/\_puhsu · Sep 7, 09:03

**「Background: KV Cache as Inference State」** In autoregressive LLM inference, the KV cache stores keys and values for previous tokens so they are not recomputed at each step, typically serving as a static optimization. Hogwild\! Inference shows that multiple LLM instances can share the same attention cache concurrently, using Rotary Position Embeddings to avoid recomputation and improve parallel hardware utilization, with reasoning-capable LLMs performing this out of the box without fine-tuning. AsyncReasoning further lets private reasoning and public output progress concurrently through separate views over shared KV-cache state, forming the basis for using modified inference state as an interactive agent runtime.

**「Impact」** For LLM agent developers, this suggests KV-cache-level runtime manipulation could offer responsiveness gains without retraining models or replacing agent harnesses, though the work is presented as a research preview rather than a production-ready system.

<details><summary>References</summary>
<ul>
<li><a href="https://research.yandex.com/blog/the-kv-cache-as-an-agent-runtime">The KV cache as an agent runtime | Yandex Research</a></li>
<li><a href="https://www.alphaxiv.org/abs/2504.06261">Hogwild ! Inference : Parallel LLM Generation via Concurrent... | alphaXiv</a></li>
<li><a href="https://research.yandex.com/blog/the-kv-cache-as-an-agent-runtime">The KV cache as an agent runtime</a></li>

</ul>
</details>

**Tags**: `#kv-cache`, `#llm-inference`, `#agent-runtime`, `#interactive-llm`, `#machine-learning`

---

<a id="item-tech-news-3"></a>
### [Huawei releases high-performance chip after six years](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

Huawei released the Mate XT 2 tri-fold phone on 7 September 2026 in Guangzhou, powered by the new Kirin 9050 Pro chip. The company describes the Kirin 9050 Pro as the first high-performance chip to use logic folding technology, layering logic units within a single chip and adding vertical interconnect channels to shorten signal paths, reduce latency, and improve performance. This marks Huawei&\#x27;s first new Kirin chip at a flagship launch in six years, following the Huawei Mate40 global launch.

telegram · zaihuapd · Sep 7, 08:20

**「Background」** Huawei last unveiled a new flagship Kirin chip at a flagship event during the Mate 40 global launch about six years ago. The Kirin 9050 Pro is described as the first high-performance processor to adopt &\#x27;logic folding,&\#x27; which layers logic units within a single chip and adds vertical interconnects to shorten signal transmission paths and reduce latency.

**「Impact」** Huawei’s Mate XT 2 buyers can expect lower latency and improved performance from the Kirin 9050 Pro’s stacked logic units and vertical interconnects, according to the launch announcement and corroborating reports.

<details><summary>References</summary>
<ul>
<li><a href="https://www.chinadailyasia.com/hk/article/639166">Huawei introduces latest tri- fold smartphone featuring new Kirin 9050 ...</a></li>
<li><a href="https://www.globaltimes.cn/page/202609/1369991.shtml">Huawei unveils high-performance chip for first time in... - Global Times</a></li>
<li><a href="https://www.globaltimes.cn/page/202609/1370015.shtml">Huawei launches high-performance Kirin 9050 Pro chip ...</a></li>
<li><a href="https://www.chinadaily.com.cn/a/202609/07/WS6a9e722be4b06d4aa055cbfd.html">Huawei unveils high-performance Kirin 9050 Pro chip - China Daily</a></li>
<li><a href="https://english.news.cn/20260907/7ba2bc121c6548038f98fdca6b9a65ce/c.html">EyesOnSci | Huawei unveils high-performance Kirin 9050 Pro ...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9050 Pro`, `#mobile chips`, `#semiconductors`, `#hardware`

---

<a id="item-tech-news-4"></a>
### [Git.kernel.org spends more CPU on crawler-rendered commits than legitimate access](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev reports that git.kernel.org, the official Git repository for the Linux kernel, now spends more CPU cycles rendering commits as HTML for abusive scrapers than on all other kinds of legitimate access, including Git clones. Across five geo-distributed nodes, 14 CPU cores are continuously occupied doing nothing but rendering commits for scrapers. This highlights the severe &quot;background radiation&quot; of crawler abuse on open source infrastructure. Simon Willison notes the same concern for Datasette, which serves a huge number of crawlable web pages.

rss · Simon Willison · Sep 7, 23:08

**「Background: Crawling and Git.kernel.org」** Git.kernel.org is the official Git repository for the Linux kernel, and it renders commit pages as HTML in addition to serving Git operations. Web crawlers, including AI scrapers, increasingly send automated requests to crawl such pages; according to Konstantin Ryabitsev, many now come from millions of residential or mobile IPs and make only a few requests before disappearing. This background radiation of abusive crawling consumes significant compute resources, as measured by Ryabitsev.

**「Impact」** git.kernel.org now spends more CPU cycles rendering commit pages for abusive scrapers than on all legitimate access, with 14 CPU cores across five geo-distributed nodes dedicated solely to rendering commits as HTML at any one time, reducing capacity for actual Git clones and kernel development.

<details><summary>References</summary>
<ul>
<li><a href="https://people.kernel.org/monsieuricon/creepy-crawlies">Creepy crawlies — Konstantin Ryabitsev</a></li>
<li><a href="https://letsdatascience.com/news/kernelorg-reports-crawler-load-on-git-infrastructure-05ae4912">Kernel.org Reports Crawler Load on Git Infrastructure | Let&#x27;s Data Science</a></li>
<li><a href="https://elsolitario.org/en/2026/08/30/kernel-org-ai-bots-anubis-cpu/">AI Crawlers: Kernel.org Burns 14 CPU Cores</a></li>
<li><a href="https://pinggy.io/blog/ai_crawlers_cost_more_cpu_than_real_traffic/">AI Crawlers Now Cost More CPU Than All Your Real Traffic ...</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#git`, `#Linux kernel`, `#infrastructure`, `#web scraping`

---

<a id="item-tech-news-5"></a>
### [TPU Inference Externalization Full Steam Ahead - InferenceX](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 7.0/10

SemiAnalysis reports that externalization of Google&\#x27;s TPU inference stack is accelerating under the InferenceX effort. It claims up to 50% better performance per dollar compared with unspecified existing alternatives, along with new Ironwood/TPUv8i hardware and a growing customer base. The report frames these developments as reducing the CUDA moat and challenging CUDA dominance. The source item itself provides only bullet-point phrases rather than detailed evidence.

rss · Semianalysis · Sep 7, 20:00

**「Background」** Google&\#x27;s Tensor Processing Units \(TPUs\) are custom AI accelerators used for training and inference. Ironwood and TPUv8i are recent inference-focused TPU generations, with industry analyses reporting substantial performance-per-dollar gains over earlier hardware. “Externalization” refers to Google offering these TPU-based inference capabilities to external cloud customers, positioning them against NVIDIA&\#x27;s GPU hardware and CUDA software ecosystem.

**「Impact」** For organizations evaluating AI inference infrastructure, the report suggests Google&\#x27;s InferenceX/TPU stack may offer up to 50% better performance per dollar and lower CUDA dependency, though the underlying evidence is not detailed.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/">Ironwood: The first Google TPU for the age of inference</a></li>
<li><a href="https://justoborn.com/tpu-8i-cost-analysis/">Google TPU 8i Cost Analysis: 80% Better Performance-Per-Dollar Explained - Artificial Intelligence World</a></li>

</ul>
</details>

**Tags**: `#TPU`, `#AI hardware`, `#inference`, `#CUDA`, `#SemiAnalysis`

---

<a id="item-tech-news-6"></a>
### [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 7.0/10

Rustuna, a high-speed and memory-efficient Rust implementation of Optuna, has been released by the Optuna project at github.com/optuna/rustuna. It keeps the familiar Optuna API and concepts, has zero Python dependencies to reduce supply-chain attack risk, and uses native Rust memory management for a lower memory footprint. The announcement points to a Medium blog post for details but does not include benchmark numbers or performance comparisons in the post itself.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**「Background」** Optuna is a widely used hyperparameter optimization framework originally written in Python. In March 2024, Optuna maintainers began prototyping a faster Rust implementation with Python, JavaScript, and C bindings to address execution speed and integration needs. The resulting project, Rustuna, is now available as an official Optuna repository with Python and JavaScript bindings.

**「Impact」** Rust developers and ML engineers now have an Optuna-compatible hyperparameter optimization option that removes Python runtime and dependency overhead, though the source post provides no benchmark evidence for its performance and memory claims.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/optuna/rustuna">GitHub - optuna/rustuna: A faster Optuna implementation in Rust. · GitHub</a></li>
<li><a href="https://medium.com/optuna/prototyping-a-faster-optuna-implementation-in-rust-e76efba3761b">Prototyping a Faster Optuna Implementation in Rust | by c-bata | Optuna | Medium</a></li>
<li><a href="https://github.com/optuna/optuna/discussions/5362">Prototyping a Faster Optuna Implementation in Rust · optuna/optuna · Discussion #5362</a></li>

</ul>
</details>

**Tags**: `#rust`, `#optuna`, `#hyperparameter-optimization`, `#machine-learning`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [Longitudinal LLM Benchmarking: 31,352 Repeated Measurements Reveal Temporal Variation](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 7.0/10

A Reddit post by the founder of AI Stupid Level describes a longitudinal approach to LLM benchmarking that treats model performance as a time series rather than a static leaderboard score. The methodology continuously evaluates API-served models on coding, multi-turn reasoning, and tool use, with one historical analysis covering 31,352 repeated score observations across 49 models. The analysis reports a within-day score standard deviation of 2.80 points versus a between-day daily median standard deviation of 8.43 points, roughly a 3:1 difference, though the author cautions that confounders like task composition, sampling, missingness, provider behavior, and methodology changes prevent concluding providers are changing models day-to-day. The current approach keeps benchmark configurations versioned, uses execution-based evaluation where possible, separates availability failures from valid task outcomes, tracks serving/version metadata, runs change-point detection over the resulting series, and withholds exact live tasks to reduce contamination; the full methodology is published in a PDF.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**「Background」** LLM benchmarks typically evaluate models on fixed task suites and publish aggregate scores on leaderboards, such as those tracked by llm-stats.com, BenchLM.ai, and Artificial Analysis. Because API-served models can change serving infrastructure, provider configurations, or underlying versions without public notice, snapshot leaderboard scores may not reflect model behavior over time. The source post argues that longitudinal, repeated measurements are needed to distinguish real performance drift from normal run-to-run variability.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks">AI &amp; LLM Benchmarks 2026: Rankings, Scores &amp; Results</a></li>
<li><a href="https://benchlm.ai/benchmarks">AI Benchmarks : 422 LLM Evaluations Ranked... | BenchLM. ai</a></li>
<li><a href="https://artificialanalysis.ai/leaderboards/models">LLM Leaderboard - Comparison of AI models from... | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#LLM benchmarking`, `#performance drift`, `#model reliability`, `#API models`, `#AI/ML`

---

<a id="item-tech-news-8"></a>
### [China Supreme Court Clarifies AI Liability for Deepfakes and Price Discrimination](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 7.0/10

On September 7, 2026, China&\#x27;s Supreme People&\#x27;s Court issued a judicial interpretation on artificial intelligence dispute cases, comprising 5 parts and 24 articles. It addresses AI face swaps, algorithmic price discrimination, AI impersonation for endorsements, autonomous driving, and intellectual property. The interpretation states that unauthorized AI-generated identifiable faces or voices may infringe personality rights, algorithmic price discrimination that harms rights must bear liability, and AI impersonation used to induce consumption may support punitive damages claims. It also regulates AI-enabled &quot;network doxxing&quot; and &quot;human flesh searches&quot; as privacy violations. The rules provide clearer legal responsibility for AI deployment in China.

telegram · zaihuapd · Sep 7, 09:32

**「Background」** The Supreme People&\#x27;s Court issued the &quot;Opinions on Several Issues Concerning the Application of Law in Hearing Artificial Intelligence-Related Dispute Cases&quot; on September 7, 2026, as its first judicial interpretation specifically for AI-related civil disputes. The document responds to emerging legal problems from widespread use of generative AI, including deepfake face and voice cloning, algorithmic price discrimination, fake endorsement by impersonating celebrities, autonomous driving accidents, and privacy violations such as doxxing. Judicial interpretations are binding guidance that the Supreme People&\#x27;s Court issues to unify adjudication standards in lower courts across China.

**「Impact」** Developers and deployers of AI face-swap, pricing, endorsement, autonomous driving, and data-scraping systems in China now face clearer statutory liability, including possible punitive damages for AI impersonation endorsements.

<details><summary>References</summary>
<ul>
<li><a href="https://huacheng.gz-cmc.com/pages/2026/09/07/f54c947aa50d4bee8feeab61af427167.html">“AI...”</a></li>
<li><a href="https://www.jiemian.com/article/15063986.html">AI...</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#deepfake`, `#algorithmic pricing`, `#privacy`, `#autonomous driving`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China announces smaller-than-expected $53.6 billion capital injection into state banks and insurers](https://www.cnbc.com/2026/09/07/china-state-banks-lenders-insurers-capital-solvency-bankrupt-nim-.html) ⭐️ 7.0/10

China announced a planned 360 billion yuan \($53.6 billion\) capital injection into three state-owned banks and five insurers, led by the finance ministry and the state tobacco company; analysts said it is the first recapitalization extended to insurers and was smaller than markets expected.

rss · CNBC Finance · Sep 7, 23:23

**「Background」** This follows last year&\#x27;s 500 billion yuan injection into four major state banks and a March pledge to issue 300 billion yuan in special treasury bonds, as low interest rates squeezed bank margins and insurer solvency.

**Tags**: `#China`, `#state-owned banks`, `#insurers`, `#capital injection`, `#financial policy`

---