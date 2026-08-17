---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
lang: en
---

> From 42 items, 12 important content pieces were selected

---

**Technology News**
1. [DuckDB v2.0 Preview](#item-tech-news-1) ⭐️ 8.0/10
2. [AI-Generated GitHub Copilot Autofix Allowed Snowflake Jira Compromise](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen3.8 27B Scores 52 on Artificial Analysis](#item-tech-news-3) ⭐️ 8.0/10
4. [AirTag Tracked Rare Books to Amazon AI Training Facility](#item-tech-news-4) ⭐️ 8.0/10
5. [GitHub.com Overloaded: Official Status Incident After &\#x27;No Server Available&\#x27; Error](#item-tech-news-5) ⭐️ 7.0/10
6. [Evaluation Tricks That Flatter Sparse Attention and KV Cache Compression](#item-tech-news-6) ⭐️ 7.0/10
7. [ChatGPT macOS Adds Opt-in Computer History Logging Clicks and Keystrokes](#item-tech-news-7) ⭐️ 7.0/10
8. [Apple to Adjust ATT Consent Rules After German Ruling](#item-tech-news-8) ⭐️ 7.0/10

**Technology Blog**
1. [Scaling 200B+ DiT Models with Distributed Layerwise Offload](#item-tech-blog-1) ⭐️ 9.0/10

**Financial News**
1. [Unitree Technology to list on STAR Market at 150.8 yuan per share](#item-finance-news-1) ⭐️ 8.0/10
2. [Stripe reportedly agrees to acquire OpenRouter for over $7 billion](#item-finance-news-2) ⭐️ 7.0/10
3. [Binance to Restrict HTX \(Huobi\) Transactions Starting August 23, 2026](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [DuckDB v2.0 Preview](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

DuckDB has published an official preview of version 2.0, outlining planned features and the development roadmap. As a widely used embedded analytical database, this major version is significant for data engineers and developers who depend on DuckDB for OLAP workloads. The preview has drawn strong community attention, though specific technical details and feature lists are not available in the supplied item. The announcement comes from the official DuckDB blog and is dated August 17, 2026.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**「Background」** DuckDB is an open-source embedded analytical database widely used for OLAP workloads, with features such as spatial support and out-of-core processing for larger-than-memory data. The upcoming v2.0 release, previewed on the official DuckDB blog, will add server mode \(Quack\), triggers, a VARIANT type, asynchronous I/O, a new SQL parser, and a new storage format. The project is governed by the nonprofit DuckDB Foundation, while DuckLabs provides commercial support and paid feature work.

**「Potential Impact」** The publication of an official DuckDB v2.0 preview lets existing users and data engineering teams begin assessing upcoming compatibility, performance, and feature changes before they upgrade production analytical workloads.

**「Community Discussion」** Community comments express enthusiasm for DuckDB v2.0, especially the &\#x27;Quack&\#x27; feature, and appreciation for its ability to handle larger-than-memory processing on consumer hardware. Some users raise concerns about the high number of commits in a short period possibly involving AI, while others hope for incremental materialized views, a feature they associate with ClickHouse, and encourage funding for database research.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights?ref=upstract.com">A Preview of DuckDB v 2 . 0 – DuckDB</a></li>
<li><a href="https://runtimewire.com/article/duckdb-v2-server-mode-embedded-analytics">DuckDB previews v 2 . 0 plan to stabilize Quack server mode</a></li>

</ul>
</details>

**Tags**: `#duckdb`, `#database`, `#data-engineering`, `#olap`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [AI-Generated GitHub Copilot Autofix Allowed Snowflake Jira Compromise](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

Wiz researchers reported that an AI-generated GitHub Copilot Autofix suggestion introduced a template injection vulnerability in a Snowflake GitHub Actions workflow, potentially allowing compromise of Snowflake&\#x27;s Jira instance. The vulnerable workflow was .github/workflows/jira\_issue.yml, where a run block used shell command substitution on issue title and body without escaping, enabling code injection via template expansion. Static analysis tools such as zizmor flag this pattern as &\#x27;code injection via template expansion&\#x27; at line 24. The finding illustrates that AI-generated CI/CD code needs the same security scanning and review as human-written code.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**「Background」** GitHub Actions workflows can be triggered by public events such as \`issues: opened\`; if they use untrusted issue fields \(e.g., the issue title\) in shell commands or template expansions without escaping, this creates a code-injection path. Copilot Autofix is GitHub’s feature that reviews pull requests and suggests or directly applies security patches; in Snowflake’s public \`snowflake-connector-net\` repository, commit \`4a1b8ce\` \(PR \#1218\) co-authored by Copilot Autofix rewrote the \`jira\_issue.yml\` workflow. Wiz Red Agent later reported that this change let an unauthenticated user who opened a crafted GitHub issue execute arbitrary commands on a GitHub Actions runner.

**「Impact」** Snowflake&\#x27;s Jira instance was potentially exposed to compromise through the vulnerable GitHub Actions workflow. No actual compromise is confirmed in the supplied information.

**「Community Discussion」** Commenters largely agreed that CI/CD code, including AI-generated changes, must be scanned with tools like zizmor, with one suggesting the vulnerability was human error for accepting unverified AI code. Another questioned whether the Copilot-authored commit was actually related to the vulnerable change, noting the specific PR&\#x27;s Copilot co-authored commit was not the vulnerable part.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug">Red Agent Exploits Snowflake Vuln Created by Copilot ... | Wiz Blog</a></li>
<li><a href="https://dev.to/jamilxt/copilot-autofix-introduced-a-critical-cicd-bug-at-snowflake-heres-how-to-harden-github-actions-1pf">Copilot Autofix Introduced a Critical CI/CD Bug at Snowflake .</a></li>
<li><a href="https://elsolitario.org/en/2026/08/17/wiz-red-agent-copilot-autofix-snowflake-en/">Copilot Autofix : The Bug an AI Exploited in Snowflake</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#CI/CD`, `#GitHub Actions`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Qwen3.8 27B Scores 52 on Artificial Analysis](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 8.0/10

Qwen3.8 27B has achieved an Artificial Analysis score of 52, a substantial jump from Qwen3.6 27B&\#x27;s score of 38. According to commenters, the model beats all medium models between 40B and 150B parameters and matches DeepSeek V4 Flash 0731, which ranks fifth among large models above 150B. Community reports claim it rivals the frontier-level Opus 4.6 in capability while running on a gaming PC. One user describes strong agentic behavior at higher reasoning levels, with intense goal tracking and tool calling.

hackernews · anana\_ · Aug 17, 17:25 · [Discussion](https://news.ycombinator.com/item?id=49334544)

**「Context on Qwen 3.8 and the comparison models」** Qwen3.8 is part of the recent Qwen 3.8 model family; the larger Qwen3.8-Max reached general availability on August 3, 2026 with competitive pricing, and smaller variants like the 27B model are being evaluated on public benchmarks. Artificial Analysis is an independent evaluation platform that aggregates intelligence scores across benchmarks, enabling cross-model comparison. DeepSeek V4 Flash 0731 is a 284B-parameter \(13B active\) model released July 31, 2026 that leads on many agentic benchmarks at a fraction of the cost of premium models, so matching its score is notable.

**「Impact」** Users and developers may now achieve frontier-competitive inference on consumer gaming hardware, reducing dependence on large cloud-based or datacenter-scale model deployments.

**「Community Discussion」** Commenters express surprise and some skepticism about Qwen3.8 27B matching larger recently released models like Opus 4.6, with one user noting the model can become &\#x27;obsessed&\#x27; with solving problems during extensive use. Several plan or have run their own benchmarks, and at least one says they cannot yet fathom the result but will test extensively.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/qwen-3-8-vs-deepseek-v4">Qwen 3.8 vs DeepSeek V4: The Value King Keeps Its Crown</a></li>
<li><a href="https://lovableapp.org/blog/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash">Qwen 3.8 Max vs GLM 5.2 vs Kimi K3 vs DeepSeek V4 Flash (2026): The Complete Frontier Model Comparison | Lovable APP Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#large language models`, `#benchmarks`, `#open-source`, `#efficiency`

---

<a id="item-tech-news-4"></a>
### [AirTag Tracked Rare Books to Amazon AI Training Facility](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media placed an Apple AirTag inside one of roughly 1,000 books from a large bulk order on the Biblio marketplace and tracked it to the VGT3 corner of Amazon&\#x27;s LAS8 facility in Las Vegas, where a dinosaur-with-book logo marked the entrance. Online forum discussions among Amazon workers described VGT3 as performing destructive scanning of large volumes of books. This provides direct evidence that Amazon is acquiring large volumes of physical books, suspected to be for scanning into AI training datasets, following earlier reports of similar bulk orders and Anthropic&\#x27;s book scanning in 2025. The findings raise copyright and data provenance concerns about using purchased books for AI training without clear authorization.

rss · Simon Willison · Aug 17, 15:21

**「Background」** Booksellers have reported receiving large, price-insensitive orders for books from anonymous customers, leading to suspicion that the books are being scanned to build AI training data. In June 2025, Simon Willison covered Anthropic&\#x27;s practice of buying and scanning physical books for AI training. The 404 Media investigation used a hidden AirTag to verify where one such bulk order was delivered.

**「Impact」** Authors, publishers, and booksellers now have concrete GPS tracking evidence that Amazon receives and destructively scans large volumes of books at its LAS8 facility, which could support copyright or licensing claims regarding AI training data.

**Tags**: `#AI training data`, `#copyright`, `#Amazon`, `#investigative reporting`, `#book scanning`

---

<a id="item-tech-news-5"></a>
### [GitHub.com Overloaded: Official Status Incident After &\#x27;No Server Available&\#x27; Error](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) ⭐️ 7.0/10

A GitHub user reported receiving the error &quot;No server is currently available to service your request&quot; and initially noted that no incident was listed on githubstatus.com, but an official status incident has since been posted at https://www.githubstatus.com/incidents/zkxwbgr0cnmx. The HN post is titled &quot;Tell HN: GitHub Is Overloaded&quot; and describes a significant service disruption on GitHub.com. The incident indicates that GitHub&\#x27;s service was overloaded or unavailable for requests, affecting developers attempting to use the platform. No specific root cause or resolution timeline is provided in the source item.

hackernews · SpyCoder77 · Aug 17, 13:35 · [Discussion](https://news.ycombinator.com/item?id=49330597)

**「Background」** GitHub is a widely used code hosting and collaboration platform whose status page \(githubstatus.com\) is the official channel for incident updates. During outages, users may see errors such as &quot;No server is currently available to service your request&quot; and the status page typically records investigating and resolved states. The current incident was later associated with a database infrastructure issue affecting pull request and issue pages, following a history of reliability concerns including major outages.

**「Impact」** Developers using GitHub.com for hosting, pull requests, diffs, issues, and CI faced service unavailability while the overload persisted, as indicated by the reported &quot;No server is currently available&quot; error.

**「Community Discussion」** Commenters express frustration with the outage&\#x27;s duration and reliability, with one user considering alternatives costing $5-10/month and another suggesting rate limiting or pricing changes to handle LLM-driven traffic. Some speculate the incident reflects broader leadership or scale problems, while others note expected cloud reliability standards have not been met.

<details><summary>References</summary>
<ul>
<li><a href="https://statusfield.com/services/github/incidents">GitHub Incident History | Statusfield</a></li>
<li><a href="https://www.githubstatus.com/">GitHub Status</a></li>
<li><a href="https://blog.incidenthub.cloud/github-reliability-outage-history-2025-2026">GitHub Outages 2025 - 2026: Reliability Analysis and Outage History</a></li>

</ul>
</details>

**Tags**: `#github`, `#outage`, `#infrastructure`, `#developer-tools`, `#site-reliability`

---

<a id="item-tech-news-6"></a>
### [Evaluation Tricks That Flatter Sparse Attention and KV Cache Compression](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 7.0/10

An X thread by p\_nawrot, linked in a Reddit discussion, describes how sparse attention and KV cache compression papers can be made to look good through flawed evaluation choices. Cooperative retrieval settings include single-hop needle-in-a-haystack tasks with no distractors, contaminated QA benchmarks from years ago, and few-shot in-context learning where extra shots are useless, so most tasks pass under Sliding Window Attention and support 5–10x compression claims. Other tactics are not isolating the contribution by changing window or block sizes, keeping baselines as old 2023 implementations with authors&\#x27; recommended hyperparameters while tuning only the new method, adding custom Triton kernels for the new method, moving questions before context, and reporting only aggregate RULER results while burying degradation on NIAH-MK3. The thread also flags saturated tasks and small benchmarks like AIME&\#x27;s 30 samples with 4 seeds, where bolded one-point differences are not statistically meaningful, and notes that simpler routes such as smaller dense models, KV cache quantization, or offloading may be better.

reddit · r/MachineLearning · /u/korec1234 · Aug 17, 12:18

**「Background」** Sparse attention and KV cache compression are techniques for reducing the quadratic attention cost and memory footprint of long-context LLMs. Common evaluations include needle-in-a-haystack retrieval, RULER&\#x27;s 13 tasks, and few-shot in-context learning; Sliding Window Attention and full dense models are frequently used baselines. The thread&\#x27;s critique concerns whether reported compression ratios and quality preservation reflect these evaluation settings rather than true method gains.

**「Impact」** Researchers and practitioners evaluating sparse attention or KV-cache compression should treat headline compression ratios and aggregate benchmarks with caution, demanding per-task results, isolated ablations, tuned baselines, unsaturated benchmarks, and statistical significance.

**Tags**: `#sparse attention`, `#KV cache compression`, `#model evaluation`, `#benchmarks`, `#LLMs`

---

<a id="item-tech-news-7"></a>
### [ChatGPT macOS Adds Opt-in Computer History Logging Clicks and Keystrokes](https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes) ⭐️ 7.0/10

ChatGPT&\#x27;s macOS desktop app now offers an opt-in Computer History feature that records clicks and keystrokes as events, building an activity timeline that ChatGPT and Codex can use. The feature is disabled by default and can exclude specific apps and websites, delete records, and ignore incognito or privacy-labeled tabs. OpenAI says it captures no images, video, or audio—only event data—unlike the earlier screenshot-based Windows Recall approach. The stated goal is to help the AI learn a user&\#x27;s workflow, suggest automations, and take over unfinished tasks.

telegram · zaihuapd · Aug 17, 04:16

**「Background」** Microsoft’s Windows Recall previously introduced a searchable activity timeline by capturing periodic screenshots, which raised privacy concerns; ChatGPT’s Computer History pursues a similar goal but records only input events. On macOS, the feature uses accessibility APIs to log clicks, keystrokes, and app switches, with reports indicating summaries are stored locally as unencrypted Markdown files.

**「Impact」** Users who opt in to ChatGPT&\#x27;s macOS Computer History will create a detailed event-level log of clicks and keystrokes that OpenAI can use for agentic automation, increasing the importance of its built-in exclusions, deletion, and incognito-tab controls.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes">ChatGPT ’s Computer History tracks your clicks and... | The Verge</a></li>
<li><a href="https://best-ai.org/ai-news/openai-introduces-chatgpt-computer-history-for-macos-what-it-tracks-and-how-it-works-znqhif">OpenAI Introduces ChatGPT &#x27; Computer History &#x27; for macOS : What It...</a></li>
<li><a href="https://hwbusters.com/news/chatgpt-computer-history-logs-every-click-and-keystroke-on-your-mac/">ChatGPT Computer History Logs Every Click and Keystroke on...</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#AI agents`, `#privacy`, `#macOS`, `#computer-use`

---

<a id="item-tech-news-8"></a>
### [Apple to Adjust ATT Consent Rules After German Ruling](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

Apple will change how iPhone and iPad apps obtain consent for personalized advertising following a German competition ruling. The German regulator found that Apple&\#x27;s App Tracking Transparency \(ATT\) framework favored Apple&\#x27;s own apps and violated competition rules. Apple must implement the changes within four months after the ruling is served, with its commitments valid for seven years. Third-party consent prompts must be neutral and free of discouraging wording or symbols. France and Italy have previously fined Apple 150 million euros and 98.6 million euros respectively over related issues.

telegram · zaihuapd · Aug 17, 12:50

**「Background」** Apple’s App Tracking Transparency \(ATT\) framework, introduced with iOS 14.5, made cross-app tracking of users largely opt-in and reportedly cost social media apps nearly $10 billion when it launched. Germany’s Federal Cartel Office had been investigating whether ATT treated Apple’s own applications more favorably than third-party apps, and its decision closes that years-long probe. The regulator’s ruling requires redesigned consent prompts that are neutral and fair to third-party apps.

**「Impact」** iOS developers and ad SDK providers will need to redesign third-party ATT consent prompts to remove dissuasive elements and maintain neutrality within four months of the ruling being served.

<details><summary>References</summary>
<ul>
<li><a href="https://english.aawsat.com/technology/5307947-german-regulator-apple-change-app-data-consent-rules">German Regulator : Apple to Change App Data Consent Rules</a></li>
<li><a href="https://www.globalbankingandfinance.com/apple-change-app-data-consent-rules-german-regulator/">Apple to Revise App Data Consent Rules After German Regulator ...</a></li>
<li><a href="https://www.theverge.com/tech/980977/apple-app-tracking-transparency-settlement-germany">Apple ordered to stop scaring iPhone and iPad users away... | The Verge</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Tracking Transparency`, `#privacy`, `#antitrust`, `#iOS development`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Scaling 200B+ DiT Models with Distributed Layerwise Offload](https://vllm.ai/blog/2026-08-17-distributed-layerwise-offload) ⭐️ 9.0/10

rss · vLLM Blog · Aug 17, 00:00

**「Background」** Large diffusion models like Cosmos3-Super \(64B parameters, 124GB BF16\) cannot fit on a single 64GB HBM device, and existing pure-DP layerwise offload keeps a full model copy in every rank&\#x27;s host memory, causing O\(dp\_size × model\_size\) memory and a 178GB cold-start peak for Cosmos3-Nano DP4.

**「Solution」** The author&\#x27;s Distributed Layerwise Offload uses meta-device initialization plus mmap so all ranks share one read-only OS page cache, reducing that cold-start cgroup peak to 47GB \(-73%\). Each rank then stores only 1/dp\_size of weights and reconstructs the full current layer at runtime via AllGather on a dedicated communication stream, lowering total pinned memory to model\_size \(124GB total for Super DP4 vs 496GB\). A fixed double-buffer scheme keeps exactly two layer-sized slots on device and overlaps H2D and AllGather with compute, so HBM scales with the largest block rather than layer count; measured peak HBM rose only from 23.1 to 28.1GB when going from the 17B to 64B model. DP multi-concurrency runs different requests per rank, achieving 3.3× throughput vs single-request HSDP \(83% of ideal 4×\). On Ascend, cgroup-visible host memory scales O\(model\_size + dp\_size × constant\) because pinned shards live in /dev/davinci\_manager DMA memory outside cgroup accounting, and the author&\#x27;s B300 topology study finds AllGather best for DP1×SP8/DP4×SP2 but rank-local DLO best for DP8×SP1.

**「Takeaway」** Combining sharded host weights, runtime AllGather, and double-buffered prefetch makes 200B+ DiT inference memory-feasible across GPUs and NPUs, while the optimal offload mode is topology-dependent and large-scale extrapolations remain unvalidated.

**Tags**: `#distributed inference`, `#layerwise offloading`, `#GPU memory`, `#Ascend NPU`, `#vLLM-Omni`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Unitree Technology to list on STAR Market at 150.8 yuan per share](https://wap.eastmoney.com/a/202608173843415437.html) ⭐️ 8.0/10

Unitree Technology will list on the Shanghai STAR Market on August 19, 2026, at an issue price of 150.80 yuan per share; that price implies a 2025 diluted static price-to-sales ratio \(market value divided by annual revenue\) of 35.89 times, above the average for comparable companies.

telegram · zaihuapd · Aug 17, 13:20

**「Background」** Unitree Technology, also known as Unitree Robotics, is a Hangzhou-based robotics company founded in 2016 and initially focused on quadruped robots for consumers. A static price-to-sales ratio compares the company&\#x27;s valuation implied by its IPO price with its 2025 annual revenue.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-sg/%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80">宇 树 科 技 - 维基百 科 ，自由的百 科 全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#IPO`, `#STAR Market`, `#Unitree Technology`, `#Robotics`, `#Valuation`

---

<a id="item-finance-news-2"></a>
### [Stripe reportedly agrees to acquire OpenRouter for over $7 billion](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 7.0/10

Stripe has agreed to acquire AI model access provider OpenRouter for more than $7 billion, though the final price may change, according to people familiar with the matter cited by Bloomberg.

telegram · zaihuapd · Aug 17, 01:19

**「background」** The Wall Street Journal reported last month that Stripe and OpenRouter were in acquisition talks.

**「Impact」** If completed, the deal would concentrate control of a gateway used by 8 million developers to access more than 400 AI models, affecting developers and AI businesses that depend on OpenRouter for model routing and payment integration.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/">Stripe will reportedly acquire AI gateway startup OpenRouter for $7B+ | TechCrunch</a></li>
<li><a href="https://forkast.news/stripe-acquires-openrouter-for-7b-turning-model-routing-into-a-payments-infrastructure-problem/">Stripe Acquires OpenRouter for $7B+, Turning Model Routing Into a Payments Infrastructure Problem – Forkast</a></li>

</ul>
</details>

**Tags**: `#M&amp;A`, `#Stripe`, `#OpenRouter`, `#AI`, `#fintech`

---

<a id="item-finance-news-3"></a>
### [Binance to Restrict HTX \(Huobi\) Transactions Starting August 23, 2026](https://www.binance.com/en/support/announcement/detail/af2be67dc03c4673b4f56c42db948253) ⭐️ 7.0/10

Binance announced it will stop processing direct or indirect asset transfers with HTX \(Huobi Global SA\) starting August 23, 2026, and affected transactions may be withheld for compliance review. The exchange said this does not amount to a global ban on trading with HTX.

telegram · zaihuapd · Aug 17, 02:39

**「Background」** Binance said the new restrictions stem from regulatory and sanctions-related requirements, and its announcement grouped HTX with roughly 10 other affected platforms.

**「Who is affected」** Traders who move assets between Binance and HTX after August 23, 2026 may have transfers held for compliance review and linked wallets restricted or frozen.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/crypto/articles/binance-restrict-transactions-htx-10-152900808.html">Binance to Restrict Transactions With HTX, 10 Other Crypto Platforms</a></li>
<li><a href="https://www.cointribune.com/en/binance-tightens-restrictions-on-htx-and-15-crypto-firms/">Binance Tightens Restrictions On HTX And 15 Crypto Firms</a></li>
<li><a href="https://en.coinotag.com/htx-binance-transfer-halt-aug-23">HTX (HTX) Faces Binance Transfer Halt Starting Aug. 23 - COINOTAG</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#exchange restriction`, `#Binance`, `#HTX`, `#compliance`

---