---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 45 items, 16 important content pieces were selected

---

**Technology News**
1. [Apple introduces M6 and M5 Ultra](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI Jalapeño: Better than Nvidia Blackwell](#item-tech-news-2) ⭐️ 8.0/10
3. [Nitter Project Receives Cease and Desist, Instances Down](#item-tech-news-3) ⭐️ 8.0/10
4. [Firefox 157 enables JPEG XL by default on all platforms](#item-tech-news-4) ⭐️ 8.0/10
5. [FDA Authorizes First Wearable for Continuous Ketone and Blood Sugar Monitoring](#item-tech-news-5) ⭐️ 7.0/10
6. [New Mac Studio with M5 Max and M5 Ultra](#item-tech-news-6) ⭐️ 7.0/10
7. [New Mac mini with M6 and M5 Pro](#item-tech-news-7) ⭐️ 7.0/10
8. [SpaceX Announces Starbase, LA Launch Site](#item-tech-news-8) ⭐️ 7.0/10
9. [EVE Online Starts Python 3 Migration from Stackless Python 2.7](#item-tech-news-9) ⭐️ 7.0/10
10. [Continual Learning of Open-Weight Models for Sovereign AI](#item-tech-news-10) ⭐️ 7.0/10
11. [How Papers with Code Built Hybrid Search with PostgreSQL, pgvector, Qwen3](#item-tech-news-11) ⭐️ 7.0/10
12. [Proposal for a Fair Coding Agent Benchmark](#item-tech-news-12) ⭐️ 7.0/10
13. [Qwen to Open-Source Qwen3.8-Flash-Next on August 26, 2026](#item-tech-news-13) ⭐️ 7.0/10
14. [Nvidia Launches Jetson Orin Nano 2 with 78 TOPS and 8GB Memory](#item-tech-news-14) ⭐️ 7.0/10

**Financial News**
1. [U.S. threatens Chinese banks with dollar cutoff over Iran sanctions](#item-finance-news-1) ⭐️ 8.0/10
2. [Unitree shares fall 45% from first-day high, erasing 200.8 billion yuan](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Apple introduces M6 and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

Apple introduced the M6 and M5 Ultra chips on August 25, 2026, along with new Mac systems including a Mac mini with M6 and a Mac Studio with M5 Ultra. The company says the new silicon delivers major performance and AI compute gains for Mac systems, with the M5 Ultra described as its most powerful chip ever. The M6 serves as the base variant of the next-generation M6 family, while the M5 Ultra targets high-end creative and AI workloads. The announcement marks a significant update to Apple&\#x27;s Mac lineup, though details on higher-end M6 Pro, Max, and Ultra variants were not included.

hackernews · interpol\_p · Aug 25, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49433292)

**「Context: Apple Silicon M-series」** Apple&\#x27;s M-series system-on-chips have powered Macs since 2020, replacing Intel processors and enabling unified memory and integrated graphics. The M6 and M5 Ultra are the latest additions, announced alongside updated Mac mini and Mac Studio models in August 2026; the M5 Ultra is the higher-end variant with up to a 36-core CPU and 80-core GPU.

**「Impact」** Mac mini and Mac Studio buyers can expect substantial performance and AI compute improvements from the M6 and M5 Ultra, with the M5 Ultra providing Apple&\#x27;s most powerful chip option for demanding workflows.

**「Community Discussion」** Commenters praised the performance leap, with one user noting the M5 Pro felt significantly faster than M1 Pro, while others debated the high cost of maxed-out configurations. A rumor from Bloomberg suggests Apple may skip M6 Pro, Max, and Ultra variants to accelerate development of a more AI-capable M7.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M 6 and M 5 Ultra for a big leap in performance and...</a></li>
<li><a href="https://digg.com/tech/hkwl4kvz">Apple Introduces M 6 Chip and M 5 Ultra · Digg</a></li>

</ul>
</details>

**Tags**: `#apple-silicon`, `#hardware`, `#ai-compute`, `#chip-announcement`, `#technology-industry`

---

<a id="item-tech-news-2"></a>
### [OpenAI Jalapeño: Better than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 8.0/10

OpenAI announced initial benchmark results for Jalapeño, its first self-designed inference ASIC developed with Broadcom, claiming it outperforms Nvidia’s GB300 in efficiency and latency. On GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T, the chip delivers 1.5–1.9× higher peak-throughput work per watt, 1.7–3.6× lower end-to-end latency, and 2.1–4.1× better performance in high-interaction scenarios. The chip is rated at 700 W but sustained power is no more than 550 W, and OpenAI plans to deploy it in its own infrastructure by the end of the year. OpenAI did not compare Jalapeño to Nvidia’s newer Vera Rubin and does not use it for training; second-generation development is underway and a third is being designed. These results are vendor claims and have not been independently verified.

hackernews · Semianalysis · Aug 25, 14:06 · [Discussion](https://news.ycombinator.com/item?id=49434378)

**「Background」** OpenAI’s Jalapeño is a first-generation custom inference ASIC developed with Broadcom, announced at Hot Chips on August 25, 2026, and aimed at reducing dependence on Nvidia GPUs for running large language models. Nvidia’s Blackwell architecture, represented by the GB300 system, is the incumbent high-end AI accelerator against which OpenAI compared Jalapeño’s efficiency and latency. SemiAnalysis’s InferenceX benchmark suite is used to measure AI work per watt, end-to-end latency, and throughput per kilowatt for such inference chips.

**「Impact」** If the claims hold, OpenAI could reduce inference cost and latency for its large-model workloads, but the lack of independent verification and comparison to Vera Rubin adds uncertainty.

**「Community Discussion」** Commenters speculated about baking LLM weights directly into ASICs for long-lived models like GPT-OSS 120B, noted the industry’s reliance on DeepSeek and Kimi as benchmarks, and compared the inference-chip landscape to the early 3D accelerator market; one noted humans are still 22× more energy-efficient per token.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia">OpenAI Jalapeño: Better Than Nvidia Blackwell</a></li>
<li><a href="https://wccftech.com/openais-first-gen-jalapeno-asic-blows-competition-out-of-the-park-performs-1-5x-to-1-9x-more-work-per-kilowatt-than-nvidias-blackwell-chips-while-threatening-the-cuda-moat/">OpenAI&#x27;s First-Gen Jalapeno ASIC Blows Competition Out Of The Park, Performs 1.5x to 1.9x More Work Per Kilowatt Than NVIDIA&#x27;s Blackwell Chips, While Threatening The CUDA Moat</a></li>
<li><a href="https://www.briefs.co/news/openai-s-jalape-o-chip-beats-nvidia-blackwell-on-key-ai-benc/">OpenAI&#x27;s Jalapeño Chip Beats Nvidia Blackwell on Key AI Benchmarks</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#OpenAI`, `#Nvidia`, `#ASICs`, `#semiconductors`

---

<a id="item-tech-news-3"></a>
### [Nitter Project Receives Cease and Desist, Instances Down](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

The Nitter project announced in GitHub issue \#1442 that it has received cease and desist letters and is awaiting legal advice. All Nitter instances are expected to remain down for the foreseeable future. The project did not provide details about the sender or specific legal claims. Nitter is a popular open-source alternative frontend for Twitter/X that allowed users to view tweets without an account and with enhanced privacy, so its shutdown removes that access.

hackernews · Banditoz · Aug 25, 17:08 · [Discussion](https://news.ycombinator.com/item?id=49437283)

**「Background」** Nitter is an open-source alternative frontend for Twitter/X that lets users read posts without using the official site or API, often to avoid tracking and login walls. X Corp. has increasingly restricted third-party access to its platform, and on Monday it sent cease-and-desist letters demanding a permanent takedown of Nitter instances and the project’s repository. The developer, known as Zedeus, is seeking legal advice while all instances remain offline.

**「Impact」** If the cease-and-desist is enforced, Nitter instances and its code repository would be taken down, removing one of the few remaining ways to view public X posts without an account, ads, or personalized tracking.

**「Community Discussion」** Commenters noted that some users depended on Nitter to follow public posts from organizations and local councils that still use X, and one observed that Claude AI had used Nitter or xcancel to retrieve tweet context, speculating that the takedown may be linked to AI data access negotiations. Others called for legal protections for such projects and for building dignified alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/">X sends cease - and - desist to open source project Nitter ... | TechCrunch</a></li>
<li><a href="https://www.theverge.com/tech/984819/nitter-which-let-you-read-x-posts-without-using-x-is-offline">Nitter , which let you read X posts without using X, is offline. | The Verge</a></li>
<li><a href="https://mezha.net/eng/bukvy/ac17548c_x_corp-_demands/">X Corp. demands Nitter shut down over alleged API and data access violations | Ukraine news - #Mezha</a></li>
<li><a href="https://techcrunch.com/2026/08/25/x-sends-cease-and-desist-to-open-source-project-nitter-over-alleged-scraping/">X sends cease-and-desist to open source project Nitter over alleged scraping | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#nitter`, `#open-source`, `#twitter`, `#cease-and-desist`, `#privacy`

---

<a id="item-tech-news-4"></a>
### [Firefox 157 enables JPEG XL by default on all platforms](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 8.0/10

Firefox 157 will enable JPEG XL \(jxl\) image format support by default on all platforms. This change aligns Firefox with Chromium, which is also adopting JPEG XL, and advances open web image standards. Users will not need to enable a flag or install an extension to view JPEG XL images, and web developers can adopt the format with greater confidence.

hackernews · yboris · Aug 25, 17:55 · [Discussion](https://news.ycombinator.com/item?id=49437946)

**「Context: JPEG XL and the Rust decoder」** JPEG XL is a royalty-free image format designed for efficient lossy and lossless compression with modern features. Before Firefox 157, JPEG XL decoding was not enabled by default for all users, though Firefox Nightly had it on by default for testing. Mozilla said it would ship a decoder only if Google Research built a safe, performant Rust implementation, and Google Research met that challenge with jxl-rs, which is now the core of Firefox&\#x27;s JPEG XL support. Firefox 157 is scheduled for release at the end of September and will enable JPEG XL decoding by default on all available platforms.

**「Impact」** Users of Firefox 157 on any platform will be able to view JPEG XL images directly, and developers can serve JPEG XL files without requiring fallbacks for Firefox.

**「Community Discussion」** Commenters note that Chromium appears to be enabling JPEG XL as well, discuss Apple&\#x27;s use of C++ libjxl versus Rust-based jxl-rs, and raise practical issues like upload field compatibility and backporting to Firefox 115 for older Windows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Firefox-JPEG-XL-2026-Plans">Mozilla Presents Their Plan For Shipping JPEG - XL In Firefox 157</a></li>
<li><a href="https://news.ycombinator.com/item?id=49437946">Firefox 157 will include JPEG XL by default on all platforms</a></li>
<li><a href="https://contentbuffer.com/news/firefox-enables-jpeg-xl-decoding-default-version-157-aa292b2f">Firefox Enables JPEG XL Decoding by Default in Version 157</a></li>

</ul>
</details>

**Tags**: `#JPEG XL`, `#Firefox`, `#web platform`, `#open source`, `#browsers`

---

<a id="item-tech-news-5"></a>
### [FDA Authorizes First Wearable for Continuous Ketone and Blood Sugar Monitoring](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 7.0/10

The U.S. Food and Drug Administration has authorized the first wearable device capable of continuously monitoring both ketone levels and blood sugar. This marks a new regulatory category in wearable health technology, moving beyond glucose-only continuous monitors to track two metabolic markers at once. Continuous monitoring of both ketone and glucose may help detect metabolic changes, though the source does not specify the device&\#x27;s intended use or limitations. The available source does not name the device, manufacturer, or timeline for commercial availability. The decision represents a notable milestone for biosensor hardware and medical-device regulation.

hackernews · sunnynagra · Aug 25, 19:07 · [Discussion](https://news.ycombinator.com/item?id=49439017)

**「Context」** Continuous glucose monitors \(CGMs\) are established wearable sensors that track interstitial glucose in near real time, reducing fingersticks for people with diabetes. Ketones are produced when the body breaks down fat for fuel; dangerously high ketone levels can lead to diabetic ketoacidosis, a life-threatening complication, so monitoring ketones alongside glucose can provide earlier warning. The Libre Duo 10 Day system is Abbott’s dual glucose-ketone sensor authorized by the FDA for people aged 2 years and older living with diabetes, building on existing Libre glucose monitoring technology.

**「Impact」** The FDA&\#x27;s action creates a new wearable-device category for simultaneous ketone and glucose monitoring, expanding beyond previous glucose-only continuous monitors and potentially influencing future biosensor submissions.

**「Community Discussion」** Commenters shared personal experiences with diabetic ketoacidosis and expressed cautious optimism, while one noted that ketone levels may only be relevant in extreme metabolic states and questioned utility for average diabetics. Others raised concerns about reimbursement, noninvasive sensing accuracy, and how this device compares to existing wearables like Stelo and Lingo.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar">FDA Authorizes First Wearable Device That Continuously Monitors Both Ketone Levels and Blood Sugar | FDA</a></li>
<li><a href="https://www.upi.com/Top_News/US/2026/08/25/fda-oks-blood-sugar-ketone-monitor/5521787688375/">FDA approves first wearable device to monitor blood sugar, ketone levels - UPI.com</a></li>

</ul>
</details>

**Tags**: `#health-tech`, `#wearables`, `#medical-devices`, `#biosensors`, `#FDA`

---

<a id="item-tech-news-6"></a>
### [New Mac Studio with M5 Max and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 7.0/10

Apple introduced new Mac Studio desktop computers featuring M5 Max and M5 Ultra chips. The announcement positions these models for high-performance computing and local AI workloads, with emphasis on high memory bandwidth and capacity for running large models on-device. This hardware release is aimed at developers and professionals who need substantial local AI inference capabilities. No detailed technical specifications or pricing are included in the provided source content.

hackernews · interpol\_p · Aug 25, 13:03 · [Discussion](https://news.ycombinator.com/item?id=49433316)

**「Background」** The Mac Studio line was last updated in March 2025 with M4 Max and M3 Ultra configurations. The new models, announced in August 2026, replace those with M5 Max and M5 Ultra chips and start at $2,499 for the M5 Max, with preorders opening now and shipping from September 22, 2026 \(the 512GB unified memory option ships in late October\). Apple&\#x27;s emphasis on &\#x27;local AI&\#x27; reflects the growing use of high-bandwidth unified memory for on-device large language model inference.

**「Impact」** The M5 Ultra Mac Studio&\#x27;s up to 512GB unified memory, 1.2TB/s bandwidth, and 4.5x peak AI compute over M3 Ultra enable researchers to run larger local AI models and simulations via tools like LM Studio Bionic and MATLAB, reducing cloud dependency.

**「Community Discussion」** Community discussion focuses on pricing and local AI use cases, with commenters noting $10,000 for 256GB memory and 512GB not finalized until October. Others describe M5 Ultra as two M5 Max dies connected via 4.4TB/s inter-die fabric, estimating around 1000+ tokens/s prefill and 50+ tokens/s generation for a non-quantized Deepseek V4 flash, while also pointing out Apple&\#x27;s heavy use of &quot;up to&quot; and expressing hope for optimized open-weight models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html">New Mac Studio M5 Max and M5 Ultra: Everything you need to know | Macworld</a></li>
<li><a href="https://mashable.com/tech/aug-25-preorder-mac-studio">Mac Studio preorder: Mac Studio with M5 Max and Mac Studio with M5 Ultra arrive on Sept. 22. | Mashable</a></li>
<li><a href="https://appleinsider.com/articles/26/08/25/mac-studio-gets-update-to-m5-max-and-m5-ultra">Mac Studio gets update to M5 Max and M5 Ultra</a></li>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/">Apple introduces new Mac Studio with M5 Max and M5 Ultra - Apple</a></li>
<li><a href="https://daily.dev/posts/apple-s-m5-ultra-mac-studio-targets-local-llm-users-7ip5z6cvb">Apple&#x27;s M5 Ultra Mac Studio targets local LLM users | daily.dev</a></li>

</ul>
</details>

**Tags**: `#apple`, `#mac-studio`, `#hardware`, `#ai`, `#m5`

---

<a id="item-tech-news-7"></a>
### [New Mac mini with M6 and M5 Pro](https://www.apple.com/newsroom/2026/08/apple-unveils-a-more-powerful-mac-mini-featuring-the-all-new-m6-and-m5-pro/) ⭐️ 7.0/10

Apple has announced a new Mac mini featuring the all-new M6 and M5 Pro chips, a significant update to its compact desktop line. The announcement positions the hardware for developers and tech professionals seeking next-generation Apple silicon, though the available source text does not include full specifications, benchmarks, pricing, or a release date. In the absence of detailed performance data, the precise gains over previous M-series models remain unverified. Community reaction suggests that European pricing may exceed €1000 for an M6/16GB/256GB configuration, moving the Mac mini away from its previous budget positioning.

hackernews · runako · Aug 25, 13:13 · [Discussion](https://news.ycombinator.com/item?id=49433450)

**「Mac mini lineup context」** Apple&\#x27;s Mac mini is the company&\#x27;s compact desktop computer, positioned as an entry-level Mac. Reports indicate the new M6 Mac mini starts with 16GB of unified memory and 256GB of storage at $899, while the M5 Pro model starts with 24GB of memory and 512GB of storage, reflecting a higher price point than previous low-cost Mac mini configurations. Ongoing global memory shortages may constrain higher-end configuration availability.

**「Impact」** Potential buyers seeking the previous budget-friendly Mac mini positioning may face a higher starting price, with European commenters reporting over €1000 for an M6/16GB/256GB configuration.

**「Community Discussion」** Commenters expressed nostalgia for the $499 base M4 Mac mini and noted that European pricing above €1000 for an M6/16GB/256GB model breaks a psychological barrier. Some also criticized Apple&\#x27;s change from same-day ordering to later availability and questioned whether M6 benchmarks meaningfully compare against the M5 Pro.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macworld.com/article/2964754/2026-mac-mini-m5-pro-design-specs-release-date.html">Mac mini M5/M5 Pro: Release date, specs, AI upgrades, and latest rumors | Macworld</a></li>
<li><a href="https://zeerawireless.com/blogs/news/mac-mini-m6-price-specs-release-date-buying-guide">Mac mini M6 Price, Specs &amp; Release Date (2026)</a></li>
<li><a href="https://www.theverge.com/tech/984190/apple-mac-mini-m6-m5-pro-price-specs">Apple’s new Mac Mini has fresh M6 and M5 Pro chip offerings — and higher prices | The Verge</a></li>

</ul>
</details>

**Tags**: `#apple-silicon`, `#mac-mini`, `#hardware`, `#m6`, `#m5-pro`

---

<a id="item-tech-news-8"></a>
### [SpaceX Announces Starbase, LA Launch Site](https://www.spacex.com/sites/starbase-la) ⭐️ 7.0/10

SpaceX has officially announced Starbase, LA, a new launch site in Louisiana that would provide Sun-Synchronous Orbit access. A commenter notes that Sun-Synchronous Orbit launches require a launch angle of about 98 degrees relative to the equator, making the southern Louisiana location suitable for such trajectories. The announcement follows months of speculation, including local realtor reports from May and Ars Technica coverage earlier this month. Community members highlight potential long-term construction opportunities for Louisiana trades but also express uncertainty about project timelines.

hackernews · bilsbie · Aug 25, 16:37 · [Discussion](https://news.ycombinator.com/item?id=49436822)

**「Background」** SpaceX has been developing Starship at its Starbase in Boca Chica, Texas, but a Louisiana coastal site offers a clear southward launch corridor over the Gulf of Mexico for Sun-Synchronous Orbit missions. According to reports, the new facility in Vermilion Parish is a $100 billion Starship manufacturing and launch complex on a former Exxon property, intended to support thousands of launches annually. This announcement follows months of speculation by local realtors and coverage by Ars Technica.

**「Impact」** If built, Starbase Louisiana would give SpaceX additional dedicated Sun-Synchronous Orbit launch capacity and could create years of construction and trade work in an economically disadvantaged coastal region.

**「Community Discussion」** Comments are cautiously optimistic, welcoming real-world ambitious projects and the prospect of jobs in coastal Louisiana, while also noting Musk timeline skepticism and questioning whether parts of the announcement page were AI-generated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/25/spacex-louisiana-spaceport.html">SpaceX plans to build a $100 billion spaceport in Louisiana</a></li>
<li><a href="https://www.space.com/space-exploration/private-spaceflight/spacex-announces-enormous-usd100-billion-starbase-louisiana-starship-launch-site">Starbase Louisiana: SpaceX announces enormous $100 billion Starbase launch site | Space</a></li>
<li><a href="https://qz.com/spacex-starbase-louisiana-spaceport-100-billion-082526">SpaceX announces $100 billion Starbase Louisiana spaceport</a></li>

</ul>
</details>

**Tags**: `#spacex`, `#space`, `#launch-site`, `#louisiana`, `#starbase`

---

<a id="item-tech-news-9"></a>
### [EVE Online Starts Python 3 Migration from Stackless Python 2.7](https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/) ⭐️ 7.0/10

EVE Online has announced the start of its migration from Stackless Python 2.7 to Python 3. The upgrade will use the futurize script against 2.4 million lines of code, followed by manual review of roughly 20,000 places where Python 2 and Python 3 behavior differs, such as integer division \(\`1 / 2\` yielding 0 versus 0.5\). The announcement comes 16 years after the game&\#x27;s last major Python upgrade to Stackless Python 2.7 in 2010. It does not describe how Stackless&\#x27;s tasklet/microthread functionality will be replaced in the main EVE Online server, though CCP previously presented a Carbon scheduler replacement for the newer EVE Frontier engine and open-sourced the carbonengine/scheduler library.

rss · Simon Willison · Aug 25, 22:59

**「Background」** Stackless Python is a fork of CPython that adds lightweight microthreads called tasklets, which EVE Online has used since its 2003 launch to handle large-scale concurrent simulation. Python 3 introduced backward-incompatible changes from Python 2, including different integer division semantics, requiring migration tools and manual audits for large codebases.

**Tags**: `#Python`, `#Python 3 migration`, `#EVE Online`, `#Stackless Python`, `#software engineering`

---

<a id="item-tech-news-10"></a>
### [Continual Learning of Open-Weight Models for Sovereign AI](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 7.0/10

A technical report and accompanying open-weights model named Thomson argue that continual learning on readily available open-weight models can allow a wider range of institutions to reach frontier AI performance without massive funding. The method uses a modern mid- and post-training stack, safeguards for plasticity and stability, and minimal high-impact parameter interventions instead of narrow fine-tuning, prompt engineering, or frozen-model tool augmentation. The authors report that Thomson, focused on high-stakes professional work, performs competitively with recent frontier models on agentic tasks, safety, legal, tax, multilingualism, and large-scale Deep Research. They describe a π-shaped pattern of broad improvements, including untargeted capabilities, while almost eliminating forgetting. These claims come from the technical report and have not been independently verified in the Reddit post.

reddit · r/MachineLearning · /u/Forsaken\_Scientist · Aug 25, 10:30

**「Background」** Frontier models are the most capable AI models, typically developed by a few well-funded labs; open-weight variants make their parameters publicly available for reuse and adaptation. SovereignAI is the goal of enabling an organization to independently build, deploy, and govern AI systems rather than depending on external providers. Continual learning, as used by Thomson Reuters for its Thomson model, refers to updating an existing model with new data or training stages while trying to retain prior capabilities, rather than training from scratch or narrow fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/hz3yri31">Thomson Reuters Launches Thomson - 1 . 0 AI Model · Digg</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#sovereign AI`, `#open weights`, `#frontier models`, `#technical report`

---

<a id="item-tech-news-11"></a>
### [How Papers with Code Built Hybrid Search with PostgreSQL, pgvector, Qwen3](https://www.reddit.com/r/MachineLearning/comments/1vxyrsr/how_we_built_a_sota_search_engine_using/) ⭐️ 7.0/10

Papers with Code has implemented a hybrid search system that combines keyword and semantic search, which the author reports yields better results than either approach alone. The stack uses PostgreSQL with pgvector and Qwen3-Embedding-0.6B for text embeddings, with Hugging Face Jobs running on an NVIDIA L4 for batch embedding generation and Hugging Face Buckets for storing artifacts. A live embedding model is served through Hugging Face Inference Endpoints. The same infrastructure also powers the related papers recommendations on individual paper pages. The author, who works at Hugging Face and on Papers with Code, published a technical breakdown of the system.

reddit · r/MachineLearning · /u/NielsRogge · Aug 25, 12:42

**「Background」** Hybrid search combines traditional keyword matching with semantic vector search: keyword retrieval matches exact query terms, while semantic search uses dense embeddings to rank documents by meaning even when vocabulary differs \(tool-1-1\). PostgreSQL&\#x27;s pgvector extension adds vector storage and similarity queries to a relational database, enabling this in a single system. The Qwen3-Embedding-0.6B model is a lightweight 595M-parameter text embedding model with 32K context that converts text into dense vectors for retrieval \(tool-1-3\).

<details><summary>References</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/20693-papers-with-code-uses-hugging-face-services-for-hybrid-paper-search/">Papers with Code uses Hugging Face services for hybrid paper search</a></li>
<li><a href="https://llm.co/llms/qwen3-embedding-0-6b">Qwen 3 - Embedding - 0 . 6 B : Private, Self-Hosted Semantic Search</a></li>

</ul>
</details>

**Tags**: `#hybrid search`, `#pgvector`, `#semantic search`, `#Qwen3`, `#technical deep-dive`

---

<a id="item-tech-news-12"></a>
### [Proposal for a Fair Coding Agent Benchmark](https://www.reddit.com/r/MachineLearning/comments/1vy0ki7/what_would_a_fair_benchmark_for_agent/) ⭐️ 7.0/10

Reddit user jonah\_omninode proposes a fair benchmark for coding agents by crossing workflow decomposition \(monolithic vs. bounded slices with explicit contracts\) with model policy \(frontier-only vs. cheapest-capable with escalation\), yielding four cells. The design aims to isolate model capability from harness effects, such as context assembly, task decomposition, tool design, retry policy, and acceptance gates, which are typically collapsed into a single score. The proposal freezes original tasks, source revisions, tools, retry budgets, acceptance criteria, validator versions, and verifier, and suggests primary measures like cost per accepted change, false acceptance/rejection, first-pass accepted yield, verification time, and reproducibility across three runs. The author highlights the unresolved confound of budget normalization between monolithic and decomposed conditions and asks for preregistration feedback before running the experiment.

reddit · r/MachineLearning · /u/jonah\_omninode · Aug 25, 13:55

**「Why harness confounds agent benchmarks」** Coding-agent benchmarks often report a single score that combines the underlying model with the surrounding harness—including context assembly, task decomposition, tool design, retry policy, and acceptance gates—so failures or inflated scores cannot be cleanly attributed to model capability. External evaluations have noted that the same model can receive different scores under different harnesses and that some benchmark comparisons do not control for harness effects. The Reddit post builds on this problem by proposing a 2x2 design that crosses workflow \(monolithic vs decomposed\) with model policy \(frontier-only vs routed escalation\) to isolate those architectural choices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/reacher-z/awesome-agent-harness-toreal">GitHub - reacher-z/awesome- agent - harness -toreal: Curated bilingual...</a></li>
<li><a href="https://nerdleveltech.com/muse-code-benchmarks-harness-confound">Muse Code Benchmarks 2026: The Harness ... | Nerd Level Tech</a></li>

</ul>
</details>

**Tags**: `#agent benchmarking`, `#AI evaluation`, `#coding agents`, `#model policy`, `#workflow design`

---

<a id="item-tech-news-13"></a>
### [Qwen to Open-Source Qwen3.8-Flash-Next on August 26, 2026](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 7.0/10

Qwen has posted a preview page on ModelScope for Qwen3.8-Flash-Next, an open-source multimodal mixture-of-experts model, with downloads expected to open on August 26, 2026 at 23:00 UTC+8. The release will offer two versions: a standard version and an FP8 version. The model is based on the next-generation Qwen4 architecture, and Qwen says the early open-sourcing of these architecture advances is intended to help the community prepare for the Qwen4 series. No actual model weights or detailed technical specifications are available yet, only the pre-release announcement.

telegram · zaihuapd · Aug 25, 12:59

**「Background」** Qwen is an open-source large language model family from Alibaba Cloud, with previous releases including Qwen2.5 and Qwen3. Qwen3.8-Flash-Next is presented as a multimodal mixture-of-experts model, which uses only a subset of parameters per token to improve efficiency. The announcement indicates it is built on the upcoming Qwen4 architecture, but technical details have not been published.

**「Impact」** Developers and researchers can plan to access the standard and FP8 Qwen3.8-Flash-Next checkpoints from ModelScope starting August 26, 2026 at 23:00 UTC+8. Expected performance remains unknown because weights and benchmarks have not been released.

**Tags**: `#AI`, `#open-source`, `#LLM`, `#Qwen`, `#multimodal`

---

<a id="item-tech-news-14"></a>
### [Nvidia Launches Jetson Orin Nano 2 with 78 TOPS and 8GB Memory](https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/) ⭐️ 7.0/10

Nvidia announced the Jetson Orin Nano 2, an entry-level edge AI module with 78 TOPS of compute and 8GB of memory. The company says the new module doubles inference performance over the previous Orin Nano Super and uses 40% less power at the same performance level. The module and developer kit are expected to become available in the first half of 2027. Nvidia positions the device for running large models such as Cosmos and Qwen 3 in real time at the edge. It also states that more than 3 million developers use its robotics stack, and companies including Wing and Matic are evaluating or adopting the new product.

telegram · zaihuapd · Aug 25, 16:54

**「Background」** NVIDIA’s Jetson Orin Nano line is its entry-level edge AI computing family for robotics and embedded machine learning; the previous Jetson Orin Nano Super developer kit was marketed with 67 TOPS of neural processing performance. The new Jetson Orin Nano 2 module increases that to 78 TOPS with 8 GB of memory, continuing the series’ role in running large models on-device at the edge.

**「Impact」** For robotics and edge AI developers, the Orin Nano 2&\#x27;s 78 TOPS and 8GB memory enable real-time execution of models such as Cosmos and Qwen 3, but modules and developer kits will not be available until H1 2027, so near-term deployments cannot yet rely on it.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/nvidia-jetson-orin-nano-2-boosts-robotics-edge-ai-by-2x/">NVIDIA Jetson Orin Nano 2 Boosts Robotics &amp; Edge AI by 2x While...</a></li>
<li><a href="https://www.tiktok.com/discover/nvidia-jetson-orin-nano-project">Nvidia Jetson Orin Nano Project | TikTok</a></li>
<li><a href="https://www.therobotreport.com/jetson-orin-nano-2-doubles-inference-performance-robotics-edge-says-nvidia/">Jetson Orin Nano 2 doubles inference... - The Robot Report</a></li>

</ul>
</details>

**Tags**: `#edge AI`, `#NVIDIA Jetson`, `#robotics`, `#AI hardware`, `#inference`

---

## Financial News

<a id="item-finance-news-1"></a>
### [U.S. threatens Chinese banks with dollar cutoff over Iran sanctions](https://www.cnbc.com/2026/08/25/china-iran-us-sanctions-banks-cips.html) ⭐️ 8.0/10

U.S. Treasury Secretary Scott Bessent warned that Chinese banks facilitating Iran sanctions evasion could be cut off from the U.S. dollar system. Before the war, China bought about 90% of Iran&\#x27;s exported oil, roughly 12% of its total crude imports, according to analysts at the U.S.-China Economic and Security Review Commission.

rss · CNBC Finance · Aug 25, 16:00

**「Background」** China has been building its Cross-Border Interbank Payment System \(CIPS\), an alternative bank-messaging network, as a hedge against dollar-centered finance; the U.S. dollar still accounted for more than half of global payments in July, while the yuan ranked fifth at 3.1%, according to Swift.

**「Impact」** Removing a major Chinese bank from SWIFT would significantly increase yuan devaluation pressure, Eurasia Group&\#x27;s China director said, while an EIU economist expected China to retaliate with rare-earth controls.

**Tags**: `#China`, `#US sanctions`, `#Iran`, `#CIPS`, `#dollar dominance`

---

<a id="item-finance-news-2"></a>
### [Unitree shares fall 45% from first-day high, erasing 200.8 billion yuan](https://www.reuters.com/business/finance/china-robot-maker-unitrees-post-listing-slump-sparks-bubble-fears-2026-08-25/) ⭐️ 7.0/10

Unitree&\#x27;s shares have fallen 45% from their first-day high after three consecutive days of declines following a STAR Market debut, erasing 200.8 billion yuan in market value from a peak of 444.9 billion yuan.

telegram · zaihuapd · Aug 25, 12:38

**「Background」** Unitree, a leading Chinese humanoid robot maker, listed on the STAR Market, a Nasdaq-style board for Chinese tech stocks; its founder said a &\#x27;ChatGPT moment&\#x27; for embodied intelligence is still 2-10 years away.

**「Impact」** The slide has sparked concerns about a bubble in humanoid robotics and retail investor losses, with analysts saying the valuation was overheated.

**Tags**: `#Unitree`, `#IPO`, `#humanoid robotics`, `#stock bubble`, `#Chinese equities`

---