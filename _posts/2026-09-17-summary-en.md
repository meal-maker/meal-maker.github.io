---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
lang: en
---

> From 42 items, 15 important content pieces were selected

---

**Technology News**
1. [Nvidia Announces Native Rust GPU Kernel Programming](#item-tech-news-1) ⭐️ 8.0/10
2. [Apple Unveils A20 Pro: First 2nm Phone Chip in iPhone 18 Pro](#item-tech-news-2) ⭐️ 8.0/10
3. [Micron showcases world&\#x27;s first 512GB DDR5 module, production-ready in 2027](#item-tech-news-3) ⭐️ 8.0/10
4. [Xiaomi Releases Live Post-Training Dashboard for Mimo 2.6](#item-tech-news-4) ⭐️ 7.0/10
5. [Mistral and Mozilla Bring Private Multilingual AI to Firefox](#item-tech-news-5) ⭐️ 7.0/10
6. [Dream-RSI: Evolving-World Training with Replay-Based Off-Policy Evaluation](#item-tech-news-6) ⭐️ 7.0/10
7. [Security Analysis Exposes Hardcoded Credentials in Flock Cameras](#item-tech-news-7) ⭐️ 7.0/10
8. [Datasette 0.65.5 fixes table permission bypass via trailing newline](#item-tech-news-8) ⭐️ 7.0/10
9. [Claude Cowork and Chat Merge Into One Claude](#item-tech-news-9) ⭐️ 7.0/10
10. [GoBench Evaluates LLM Reasoning via 9x9 Go Against KataGo](#item-tech-news-10) ⭐️ 7.0/10
11. [Chinese Casino Sites Hide APT Command-and-Control Infrastructure](#item-tech-news-11) ⭐️ 7.0/10
12. [Doubao 2.1 Pro Update Adds Multimodal Coding and Agent Verification](#item-tech-news-12) ⭐️ 7.0/10

**Financial News**
1. [Fed raises key rate to 3.75%–4%, signals another hike this year](#item-finance-news-1) ⭐️ 10.0/10
2. [Pinglu Canal Opens, Connecting Southwest China to ASEAN](#item-finance-news-2) ⭐️ 8.0/10
3. [Hong Kong announces 11 measures to encourage births](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Nvidia Announces Native Rust GPU Kernel Programming](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia has announced official support for writing CUDA GPU kernels in Rust, introducing two tracks for native Rust GPU programming on its developer blog. The move marks a significant step for systems programming and GPU compute by offering a memory-safe alternative to CUDA C++. The announcement is aimed at integrating Rust with CUDA&\#x27;s low-level GPU kernel development, though specific compatibility constraints and performance details are not provided in the available source. The news has drawn strong interest from the Hacker News community, with 224 points and 76 comments.

hackernews · nonmaskable · Sep 16, 11:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**「Background」** CUDA is NVIDIA&\#x27;s parallel computing platform and programming model for writing kernels that run on NVIDIA GPUs, historically using CUDA C++ and more recently CUDA Python. Rust is a systems programming language known for memory safety without a garbage collector, making it attractive for low-level GPU code. The new CUDA Rust offering provides two tracks—SIMT and Tile—for writing native GPU kernels in Rust, and NVIDIA states it is early-stage but will be grown and matured into 2027 and beyond.

**「Impact」** Rust developers targeting CUDA can now write GPU kernels natively in Rust and compile them to PTX using NVIDIA&\#x27;s two-track SIMT and Tile model, eliminating the need for CUDA C++ or wrapper crates for supported kernel development.

**「Community Discussion」** Community reaction is mixed: some developers see Rust&\#x27;s memory safety as a potential game changer for GPU kernels, while others criticize CUDA&\#x27;s proprietary lock-in and prefer separate kernel files with APIs like Metal or OpenCL. One commenter speculates that the Nvidia post may be AI-generated based on its phrasing.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels</a></li>
<li><a href="https://forums.developer.nvidia.com/t/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/382704">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels</a></li>
<li><a href="https://blockchain.news/news/nvidia-cuda-rust-gpu-kernels">NVIDIA Launches CUDA Rust for GPU Kernels, Expands Rust ...</a></li>
<li><a href="https://www.sourcetrail.com/rust/rust-in-2026-nvidia-and-microsoft-double-down-but-debugging-tools-still-lag/">Rust Gains Ground in GPU and Enterprise, Debugging Lags</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust : Two Tracks for Writing GPU Kernels</a></li>

</ul>
</details>

**Tags**: `#gpu`, `#rust`, `#cuda`, `#nvidia`, `#systems-programming`

---

<a id="item-tech-news-2"></a>
### [Apple Unveils A20 Pro: First 2nm Phone Chip in iPhone 18 Pro](https://www.bilibili.com/video/BV1oZeA6fERD) ⭐️ 8.0/10

Geekerwan reports that Apple has introduced the iPhone 18 Pro series with the A20 Pro, described as the first 2nm flagship smartphone chip. The A20 Pro integrates a 6-core CPU with a 20% faster performance core, a 7-core GPU that is 40% faster, and a dual 16-core neural engine, along with 50% more memory bandwidth than the A19 Pro. The chip uses a new M-series-inspired packaging design and a three-times-larger vapor chamber, enabling up to 40% better sustained performance. Apple also announced the self-developed C2 modem with 50% faster uploads and 15% lower power consumption, plus its first custom N1 wireless chip supporting Wi-Fi 7 and Bluetooth 6.

telegram · zaihuapd · Sep 16, 13:24

**「Background」** The A20 Pro succeeds the A19 Pro, moving Apple&\#x27;s mobile system-on-chip from a 3nm-class process to a 2nm-class node. &quot;2nm&quot; refers to the next-generation semiconductor manufacturing technology, which uses nanosheet transistor structures and new packaging to improve transistor density, power efficiency, and on-device AI performance compared with earlier nodes.

**「Impact」** If the claims are accurate, iPhone 18 Pro buyers can expect substantially higher sustained CPU/GPU and neural engine performance plus lower modem power draw, though these figures are not yet independently verified.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/09/09/apple-unveils-a20-pro-as-first-2nm-smartphone-chip/">Apple Unveils A20 Pro as First 2nm Smartphone Chip - MacRumors</a></li>
<li><a href="https://applemagazine.com/a20-pro-2nm-iphone-18-pro-chip/">A20 Pro: Inside the 2nm Chip Expected for iPhone 18 Pro - AppleMagazine</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#2nm chip`, `#mobile processor`, `#hardware`, `#technology news`

---

<a id="item-tech-news-3"></a>
### [Micron showcases world&\#x27;s first 512GB DDR5 module, production-ready in 2027](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 8.0/10

Micron has showcased what it describes as the world&\#x27;s first 512GB DDR5 RDIMM, aimed at servers and capable of up to 9200 MT/s. The module uses 3D-stacked DRAM chips, and 24 such modules can provide 12TB of total memory. Micron states that a single module consumes 16W, compared with 44.2W for four 128GB modules, a reduction of more than 60%. AMD and Intel are validating the module for future server platforms, and Micron expects it to be production-ready in 2027.

telegram · zaihuapd · Sep 16, 16:15

**「Background」** DDR5 is the current mainstream server memory standard, and RDIMMs are registered DIMMs commonly used in servers to support larger capacities and signal integrity. High-capacity servers often combine multiple lower-capacity modules, such as 128GB RDIMMs, to achieve large memory pools. Micron&\#x27;s 512GB module uses 3D stacking of DRAM dies to increase per-module capacity.

**「Impact」** Server deployments that need very large memory capacities could reduce memory power consumption by over 60% per 512GB using Micron&\#x27;s module once it reaches production in 2027.

**Tags**: `#hardware`, `#DDR5`, `#memory`, `#servers`, `#semiconductors`

---

<a id="item-tech-news-4"></a>
### [Xiaomi Releases Live Post-Training Dashboard for Mimo 2.6](https://mimo.xiaomi.com/rl/) ⭐️ 7.0/10

Xiaomi has released a live dashboard at https://mimo.xiaomi.com/rl/ that tracks the post-training process of its Mimo 2.6 model, providing real-time visibility into training metrics and progress. This move is seen as a novel transparency initiative for an open-source LLM, drawing attention from AI/ML developers. Community discussions highlight positive experiences with earlier Mimo versions like Mimo-V2.5 in software engineering tasks, citing very low cost and high ROI, though some users note occasional hallucination loops that can be resolved with a stop-then-continue approach. A user referenced DeepSWE 1.1 scores, noting Mimo-v2.5-Pro scored 19%, while leading models such as Fable \(70%\), Kimi K3 \(69%\), and Astra \(74%\) achieved much higher results, providing context for the model&\#x27;s current capabilities.

hackernews · krackers · Sep 16, 20:09 · [Discussion](https://news.ycombinator.com/item?id=49732270)

**「Context」** Xiaomi MiMo is a family of large language models developed by Xiaomi, initially released in April 2025 with the MiMo-7B model and used within Xiaomi&\#x27;s &quot;Human x Car x Home&quot; ecosystem. The Mimo 2.6 dashboard at mimo.xiaomi.com/rl displays live training metrics from the trainer&\#x27;s logs for reinforcement-learning runs of the mimo-v2.6-pro and mimo-v2.6-flash models.

**「Impact」** Developers gain real-time insight into Mimo 2.6&\#x27;s post-training process, enabling them to monitor training progress and plan adoption based on actual metrics rather than only release announcements.

**「Community Discussion」** Community comments reflect strong interest and mostly positive practical experience with earlier Mimo versions \(e.g., Mimo-V2.5\) for software engineering, praising low cost and high ROI, though some note occasional hallucinations and weaker performance on DeepSWE benchmarks \(19% vs 70%+ for leading models\). Several users appreciate the transparency and ask why other model providers do not offer similar dashboards.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xiaomi_MiMo">Xiaomi MiMo - Wikipedia</a></li>
<li><a href="https://mimo.xiaomi.com/rl/">mimo -v 2 . 6 RL</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#LLM`, `#open source`, `#post-training`

---

<a id="item-tech-news-5"></a>
### [Mistral and Mozilla Bring Private Multilingual AI to Firefox](https://mistral.ai/news/mistral-x-mozilla/) ⭐️ 7.0/10

Mistral and Mozilla announced a partnership to integrate private, multilingual AI into Firefox. The collaboration adds features such as context-aware search, page summaries, and memory retrieval across browser tabs. The experience is live in France and North America, with launches in the UK and Germany planned later this year. The service is described as built on a zero data retention policy, but the announcement has sparked debate about whether inference happens locally or in the cloud. Community comments highlight that cloud inference may require uploading browsing history, raising trust and consent concerns.

hackernews · vertigoruntime · Sep 16, 08:08 · [Discussion](https://news.ycombinator.com/item?id=49723408)

**「Background」** Firefox Smart Window \(beta\) is Mozilla’s AI browsing assistant, now powered by Mistral models under a newly announced partnership aimed at private, multilingual AI browsing and user choice. Mistral is described as a multilingual European AI company, and the collaboration is intended to expand AI competition and give Firefox users an independent option without limiting their ability to choose other providers.

**「Impact」** Firefox users in France and North America gain AI-powered browsing features under a zero data retention policy, but the value for privacy-focused users depends on whether the cloud inference path can be trusted not to expose browsing history.

**「Community Discussion」** Comments largely debate whether AI features should run locally or in the cloud; some argue a small local model would better protect privacy for summaries and search, while others believe Mozilla&\#x27;s cloud approach still requires trust but may be preferable to directly using other AI providers. One commenter compares it to Chrome&\#x27;s built-in Gemini Nano.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/mistral-x-mozilla/">Mistral x Mozilla: Private, Multilingual AI Browsing</a></li>
<li><a href="https://blog.mozilla.org/en/firefox/mozilla-mistral-partnership/">Mozilla and Mistral partner to expand AI competition, user choice | The Mozilla Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#privacy`, `#Firefox`, `#Mistral`, `#browsers`

---

<a id="item-tech-news-6"></a>
### [Dream-RSI: Evolving-World Training with Replay-Based Off-Policy Evaluation](https://arxiv.org/abs/2609.14858) ⭐️ 7.0/10

Dream-RSI \(arXiv:2609.14858\) introduces an evolving-world training method framed as recursive self-improvement. The approach uses a replay simulator built from past experience for off-policy evaluation, reducing the cost of expensive rollouts during agent training. Commenters view the method as a useful optimization of current training techniques rather than true perpetual recursive self-improvement, noting its clever replay component but limited breakthrough status.

hackernews · bananaflag · Sep 16, 13:44 · [Discussion](https://news.ycombinator.com/item?id=49726955)

**「What is Dream-RSI and recursive self-improvement?」** Recursive self-improvement \(RSI\) refers to an AI system&\#x27;s ability to improve its own learning or optimization process, a concept often discussed in the context of potential intelligence explosion. Dream-RSI&\#x27;s name draws on Danijar Hafner&\#x27;s Dreamer line of model-based reinforcement learning, which learns a world model to simulate imagined agent trajectories and reduce costly real-environment rollouts. The paper introduces a framework for &quot;recursively self-improving exploration&quot; that adds a lightweight orchestration layer while leaving the underlying coding agent unchanged, with authors from Google, Google DeepMind, and the University of Maryland.

**「Community Discussion」** Commenters largely agree the replay simulator for off-policy evaluation is clever, but several argue that labeling it &\#x27;recursive self-improvement&\#x27; is misleading because the method does not enable perpetual self-improvement. Others raise concerns about possible policy overfitting to already-discovered branches and note the work&\#x27;s relation to Danijar Hafner&\#x27;s Dreamer line.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.14858">Dream-RSI: Recursive Self-Improvement through Evolving Worlds</a></li>
<li><a href="https://dream-rsi.com/">Dream-RSI: Recursive Self-Improvement through Evolving Worlds</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#machine learning`, `#reinforcement learning`, `#self-improvement`, `#research`

---

<a id="item-tech-news-7"></a>
### [Security Analysis Exposes Hardcoded Credentials in Flock Cameras](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 7.0/10

Security researchers gained access to a Flock camera and conducted a security analysis that uncovered hardcoded credentials and other vulnerabilities. The findings expose how the Flock surveillance system works internally, raising privacy and security concerns. The cameras are automatic license plate recognition devices used in public spaces, making the flaws especially consequential for people whose movements are logged. The analysis highlights the dangers of weak security in widely deployed surveillance hardware.

hackernews · driverdan · Sep 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**「Background」** Flock Safety manufactures automated license plate recognition \(ALPR\) cameras that are widely deployed by police departments and neighborhood associations, often mounted in public spaces to capture vehicle data. Independent researchers have repeatedly found serious security flaws in these devices, including hardcoded credentials, unencrypted data storage, and lack of secure boot, enabling physical or remote access to sensitive surveillance footage and metadata. These findings provide essential context for understanding how hackers were able to get inside a Flock camera and what that implies for the broader surveillance ecosystem.

**「Impact」** Organizations and communities using Flock cameras face a concrete risk that unauthorized individuals with physical access to a camera can exploit the documented credentials and vulnerabilities to compromise the device and its data.

**「Community Discussion」** Commenters agreed that hardcoded credentials indicate poor security practices, with one describing them as a sign of total incompetence and another blaming reduced time-to-market pressure. Several also criticized Flock&\#x27;s vulnerability disclosure policy for excluding testing that involves interacting with the device or downloading its data, and one noted that captured data is not suitably encrypted.

<details><summary>References</summary>
<ul>
<li><a href="https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/">Flock Safety Camera Vulnerabilities: 50+ Flaws Found</a></li>
<li><a href="https://hackerfeeds.com/news/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-yzdwbf">Flock cameras are riddled with security vulnerabilities and ...</a></li>
<li><a href="https://cybernews.com/privacy/hackers-flock-teardown-encryption-key-secrets/">Flock camera hacked: hackers crack open spy camera secrets ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#IoT`, `#surveillance`, `#privacy`, `#embedded systems`

---

<a id="item-tech-news-8"></a>
### [Datasette 0.65.5 fixes table permission bypass via trailing newline](https://simonwillison.net/2026/Sep/16/datasette-2/) ⭐️ 7.0/10

Datasette 0.65.5 has been released as a security fix for a permission bypass vulnerability in which a trailing newline in a table name could bypass table permissions and expose private rows. The issue was reported by dpfkdlemtp and is tracked as GitHub Security Advisory GHSA-h547-rmjf-5m2m. The vulnerability affects the handling of requested table names, allowing an attacker to append a newline character to evade access controls. Users of affected Datasette versions should upgrade to 0.65.5 to prevent unauthorized exposure of private data.

rss · Simon Willison · Sep 16, 23:51

**「Background」** Datasette is an open-source tool for exploring and publishing data as a web application, often used to share SQLite databases. It supports permissions that can restrict access to specific tables or rows. This security update addresses an edge case in how table names are parsed when checking those permissions.

**「Impact」** Datasette users with table-level permissions should upgrade to 0.65.5 immediately, as prior versions can expose private rows to an attacker who requests a table name with a trailing newline.

**Tags**: `#security`, `#datasette`, `#vulnerability`, `#open-source`, `#data-exposure`

---

<a id="item-tech-news-9"></a>
### [Claude Cowork and Chat Merge Into One Claude](https://simonwillison.net/2026/Sep/16/one-claude/) ⭐️ 7.0/10

Anthropic is merging Claude Cowork and regular Claude chat into a single Claude product, with rollout beginning today on Pro and Max plans. The unified Claude will arrive in the Claude app on web, desktop, and mobile over the coming weeks for existing and new users on those plans. It is designed to handle both quick questions and delegated tasks such as a report due at noon, continuing work after the laptop is closed. Simon Willison views this as Claude becoming a general agent in its own right and notes it echoes OpenAI&\#x27;s recent renaming of its Codex desktop app to ChatGPT. The consolidation follows confusion among users about the separation between Cowork, Claude, and Claude Code.

rss · Simon Willison · Sep 16, 18:09

**「Background」** Anthropic previously offered Claude Cowork as a separate product surface from Claude chat, while Claude Code remained a distinct developer tool. This separation caused confusion, and the author had intended to write a follow-up explaining the boundaries between Cowork and regular Claude. The change simplifies the product lineup by consolidating Cowork and chat into one assistant.

**「Impact」** Pro and Max subscribers will see Cowork and chat unified in the Claude app across web, desktop, and mobile over the coming weeks, reducing the need to choose between two separate interfaces. However, the exact feature and surface changes remain to be clarified as the rollout progresses.

**Tags**: `#Anthropic`, `#Claude`, `#AI assistant`, `#product announcement`, `#software engineering`

---

<a id="item-tech-news-10"></a>
### [GoBench Evaluates LLM Reasoning via 9x9 Go Against KataGo](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 7.0/10

GoBench is a new benchmark that evaluates LLMs on 9x9 Go games against a ladder of KataGo opponents, ranging from random to superhuman. The benchmark measures general reasoning ability, shows a strong correlation with ARC-AGI 2 \(r=0.83\), and remains highly unsaturated. GPT-6 Astra max achieves 2500 Elo, much lower than the best KataGo at 4400 Elo. With coding tools and two hours of preparation before evaluation, Codex with Astra reaches 3560 Elo. The leaderboard will be updated while unsaturated, and code and paper are available.

reddit · r/MachineLearning · /u/Roland31415 · Sep 16, 18:54

**「Background」** Go is a complex board game that has served as a milestone for AI, with KataGo being a widely used open-source engine capable of superhuman play. LLM reasoning benchmarks often rely on text or puzzle tasks, but Go requires spatial reasoning, long-term planning, and board-state understanding. Using a 9x9 board reduces game length and computational cost, making it practical for evaluating LLMs.

**「Impact」** For researchers evaluating LLM reasoning, GoBench offers a reproducible and currently unsaturated benchmark that correlates with ARC-AGI 2, potentially serving as a complementary signal for tracking progress in general reasoning.

**Tags**: `#machine learning`, `#benchmark`, `#LLM`, `#game of Go`, `#reasoning evaluation`

---

<a id="item-tech-news-11"></a>
### [Chinese Casino Sites Hide APT Command-and-Control Infrastructure](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 7.0/10

A security firm traced about 1.7 million Chinese-language casino websites and found that some are being used to conceal command-and-control \(C2\) infrastructure for malware and espionage. Since 2023, a China-linked advanced persistent threat \(APT\) group has used a framework named PeckBirdy to hide malware C2 domains within low-quality gambling sites and to distribute malicious programs through fake software updates. Because these sites closely resemble ordinary gambling sites, security personnel may mistake related network access for employee policy violations and ignore it.

telegram · zaihuapd · Sep 16, 07:31

**「Background」** Advanced persistent threat \(APT\) groups are typically state-sponsored actors that conduct long-term cyber espionage or sabotage. Command-and-control \(C2\) infrastructure allows malware to receive instructions from its operators. Fake software updates are a common delivery method that tricks users into installing malicious code.

**「Impact」** Organizations that monitor network traffic may misclassify malicious C2 connections as employees visiting gambling sites, delaying detection and allowing the APT campaign to persist unnoticed.

**Tags**: `#cybersecurity`, `#APT`, `#malware`, `#command-and-control`, `#threat-intelligence`

---

<a id="item-tech-news-12"></a>
### [Doubao 2.1 Pro Update Adds Multimodal Coding and Agent Verification](https://mp.weixin.qq.com/s/Fp_mgF6wxMk0bkUVBqOKqA) ⭐️ 7.0/10

Volcano Engine released the Doubao-Seed-2.1-pro 0915 update on September 16, making the API fully available. The release focuses on agent task delivery, multimodal coding, and multimodal understanding. Agents gain evidence tracing and multi-source verification and can orchestrate hundreds of sub-agents to cross-check and reduce hallucinations; multimodal coding can read design drafts and screen recordings to generate code directly. Image and video reasoning token consumption is reduced by more than 30% compared with the previous generation, and Doubao Work and TRAE have been integrated while Doubao-Seed-Evolving has been updated to the same version.

telegram · zaihuapd · Sep 16, 09:48

**「Background」** Doubao is ByteDance&\#x27;s family of large language models, and the Seed 2.1 generation includes Pro and Turbo variants \(tool-1-3\). Volcano Engine provides the API and underlying model infrastructure, while Doubao Work operates as an Agent execution environment and Feishu supplies enterprise context and collaboration \(tool-1-1\). The previous Seed 2.1 Pro release already exposed the model through the Doubao API, alongside image generation APIs such as Seedream 5.0 Pro \(tool-1-2\).

**「Practical impact」** Developers and enterprise users on Volcengine Ark can now call the Doubao-Seed-2.1-pro 0915 API, gaining agentic multi-source verification and multimodal coding from design drafts or screen recordings while paying for over 30% fewer vision reasoning tokens; the same update is integrated into Doubao Work and TRAE.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uied.cn/posts/921858">字节把 AI 办公这条线串起来了： 豆 包 2 . 1 Pro 0915 ... - UIED学习社区</a></li>
<li><a href="https://apimaster.ai/zh/blog/doubao-seed-2-1-seedream-5-0-pro-api">豆 包 Seed 2 . 1 与 Seedream 5.0 Pro API | APIMaster.ai | APIMaster.AI</a></li>
<li><a href="https://linux.do/t/topic/2455605">免费体验 豆 包 Doubao - Seed - 2 . 1 - Pro ... - LINUX DO</a></li>
<li><a href="https://www.houdao.com/d/22004-DoubaoSeed2-1pro-Model-Review-Analyzing-1M-Context-and-Frontend-3D-Generation-Capabilities">Doubao-Seed-2.1-pro Model Review: Analyzing 1M Context and ...</a></li>

</ul>
</details>

**Tags**: `#large-language-models`, `#multimodal-ai`, `#ai-agents`, `#coding-assistants`, `#doubao`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Fed raises key rate to 3.75%–4%, signals another hike this year](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html) ⭐️ 10.0/10

The Federal Reserve voted 12-0 to raise its benchmark interest rate by 25 basis points \(0.25 percentage point\) to a target range of 3.75%–4% on Wednesday, its first hike since July 2023, and most Fed officials projected one more quarter-point increase this year.

rss · CNBC Finance · Sep 16, 21:07

**「Background」** The central bank had kept rates steady since July 2023, and it said the move responds to persistent inflation, partly driven by higher oil prices linked to Middle East tensions.

**「Impact on borrowers」** The rate increase raises borrowing costs for households and businesses, with the 30-year fixed mortgage rate already up to 7.19% before the decision, and the signal of another hike this year points to further tightening.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html">Fed rate decision September 2026 : Rates rise to 3.75%-4%</a></li>
<li><a href="https://www.cnn.com/2026/09/16/business/live-news/federal-reserve-interest-rate-september">Fed raises interest rates for the first time since 2023 | CNN Business</a></li>

</ul>
</details>

**Tags**: `#Federal Reserve`, `#interest rate hike`, `#monetary policy`, `#inflation`, `#economic projections`

---

<a id="item-finance-news-2"></a>
### [Pinglu Canal Opens, Connecting Southwest China to ASEAN](https://www.news.cn/politics/20260916/4d3b671357d14c8db202cbf6120f2c43/c.html) ⭐️ 8.0/10

The 134.2-kilometer Pinglu Canal has opened to navigation, and Xinhua reports it connects southwest China to the Beibu Gulf and ASEAN, cutting shipping distances by more than 560 kilometers and logistics costs by 18–30%.

telegram · zaihuapd · Sep 16, 09:10

**「Background」** Construction began in August 2022 and involved investment of more than 70 billion yuan; the canal can handle ships up to 5,000 tons.

**Tags**: `#Pinglu Canal`, `#infrastructure`, `#logistics costs`, `#China-ASEAN trade`, `#shipping`

---

<a id="item-finance-news-3"></a>
### [Hong Kong announces 11 measures to encourage births](https://www.info.gov.hk/gia/general/202609/16/P2026091600265.htm) ⭐️ 7.0/10

Hong Kong announced 11 measures to encourage births, including extending its HK$20,000 newborn baby bonus for three years and raising it to HK$30,000 for second and later children born from the announcement date.

telegram · zaihuapd · Sep 16, 08:01

**「Background」** The measures were announced in Chief Executive John Lee’s latest Policy Address, which said the government was shifting from its past non-intervention approach to encouraging births.

**「Impact」** Eligible Hong Kong permanent-resident families buying a home within one year before or two years after a child’s birth would be eligible for up to HK$20,000 in stamp-duty relief once the amendment bill passes.

**Tags**: `#Hong Kong`, `#pro-natalist policy`, `#housing incentives`, `#childcare`, `#fiscal policy`

---