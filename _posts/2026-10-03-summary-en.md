---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 37 items, 15 important content pieces were selected

---

**Technology News**
1. [AI beats best Stratego player with 34 times fewer training games than DeepNash](#item-tech-news-1) ⭐️ 9.0/10
2. [Greg Kroah-Hartman Critiques LLM-Generated Kernel Vulnerability Reports](#item-tech-news-2) ⭐️ 8.0/10
3. [Google Research&\#x27;s Cogentic Coordinates Multi-Agent Mathematical Proof Discovery](#item-tech-news-3) ⭐️ 8.0/10
4. [Redis Creator’s ds4 Runs LLMs Locally](#item-tech-news-4) ⭐️ 7.0/10
5. [Zig 0.17.0 Release and Community Reactions](#item-tech-news-5) ⭐️ 7.0/10
6. [FLEET: Reward-aware sampling with MCTS for Best-of-N generation](#item-tech-news-6) ⭐️ 7.0/10
7. [Anthropic Proposes Copyright Opt-Out for AI Training in Australia](#item-tech-news-7) ⭐️ 7.0/10
8. [arXiv Caps Submissions to Two Papers per Submitter per Month](#item-tech-news-8) ⭐️ 7.0/10
9. [Claude Code Adds Mods for TypeScript Customization](#item-tech-news-9) ⭐️ 7.0/10
10. [Cloudflare launches unified observability platform](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Traders cut October Fed rate hike odds after weak September jobs report](#item-finance-news-1) ⭐️ 8.0/10
2. [Midday movers: Tesla, Broadcom, Nike, Synaptics and ON Semiconductor](#item-finance-news-2) ⭐️ 7.0/10
3. [Premarket Movers: Nike Falls, ON Semi-Synaptics Deal, Hard-Drive Makers Drop](#item-finance-news-3) ⭐️ 7.0/10
4. [Wall Street Banks&\#x27; AI Job Listings Jump 49%, Led by Agent Orchestration](#item-finance-news-4) ⭐️ 7.0/10
5. [Bitget expects limited recovery from $388 million hack but says user balances unaffected](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AI beats best Stratego player with 34 times fewer training games than DeepNash](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10

A new AI algorithm has beaten the best Stratego player in history, marking a major milestone in reinforcement learning for hidden-information games. The approach is far more sample-efficient than prior work: it played about 34 times fewer training games than DeepMind&\#x27;s 2022 DeepNash system while still becoming much stronger. The research was published in Nature and posted to arXiv. Unlike complete-information games such as chess or Go, Stratego requires reasoning about unknown piece identities and positions, making this a significant advance in sample-efficient hidden-information game AI.

hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

**「Hidden information challenges and prior DeepNash milestone」** Stratego is a classic board game where each player&\#x27;s piece identities and ranks are hidden from the opponent, creating an imperfect-information challenge that limits traditional search-based AI approaches. A previous milestone came in 2022 when DeepMind&\#x27;s DeepNash learned to play from scratch and reached human expert level, but it was not necessarily stronger than the best human players. That system was described as one of the few iconic board games that AI had not yet fully mastered.

**「Impact」** For AI researchers working on hidden-information or imperfect-information games, this work provides a more practical training recipe that needs roughly 34 times less game experience than DeepNash to reach superhuman performance.

**「Community discussion」** Commenters emphasize that Stratego&\#x27;s hidden information makes search and move evaluation unusually difficult, and several agree that the new method&\#x27;s sample efficiency is the key advance over DeepMind&\#x27;s 2022 DeepNash. Some express surprise that a childhood game remained an AI challenge, while one commenter recalled unfairly gaining an edge by noticing marked pieces as a kid.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.15378">[2206.15378] Mastering the Game of Stratego with Model-Free...</a></li>

</ul>
</details>

**Tags**: `#Stratego`, `#reinforcement learning`, `#hidden information games`, `#game AI`, `#sample efficiency`

---

<a id="item-tech-news-2"></a>
### [Greg Kroah-Hartman Critiques LLM-Generated Kernel Vulnerability Reports](https://www.youtube.com/watch?v=NnV_cWeoo5Q) ⭐️ 8.0/10

In a talk titled &\#x27;Security in the LLM Age,&\#x27; Linux kernel maintainer Greg Kroah-Hartman dissects Anthropic&\#x27;s Mythos-generated vulnerability reports against the kernel. He breaks down 79 claimed vulnerabilities: 24 provided no detail beyond &\#x27;something crashed,&\#x27; 14 were not bugs, 3 contained fabricated data, and 15 were already fixed in the latest release. Only 20 needed fixes, and several assumed a malicious filesystem image or other privileged preconditions; the resulting work amounted to about one hour of kernel development. Kroah-Hartman also says Mythos pattern-matched prior kernel patches without citing the original developers, and contrasts this with Anthropic&\#x27;s high-profile safety claims.

hackernews · usernomdeguerre · Oct 2, 02:51 · [Discussion](https://news.ycombinator.com/item?id=49929391)

**「Background」** Greg Kroah-Hartman is a long-time Linux kernel maintainer who presented at the Kernel Recipes 2026 conference. His talk, &quot;Security in the LLM age,&quot; evaluates large language model-generated security reports, using Anthropic&\#x27;s Mythos system as a case study after it claimed to find 79 Linux kernel vulnerabilities.

**「Impact」** For Linux kernel maintainers, LLM-generated vulnerability reports such as Mythos&\#x27;s 79 claimed CVEs demand substantial manual triage while yielding only about one hour of actual kernel development, limiting their practical security value.

**「Community Discussion」** Commenters appreciated Kroah-Hartman&\#x27;s directness, noting that Mythos matched existing patches without crediting original kernel developers and that its safety marketing conflicts with the modest real-world results. Some also caution that specialized models trained on kernel specifics could eventually improve bug discovery and fix accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=NnV_cWeoo5Q">Kernel Recipes 2026 - Security in the LLM age - YouTube</a></li>
<li><a href="https://kernel-recipes.org/en/2026/schedule/">Schedule | Kernel Recipes</a></li>

</ul>
</details>

**Tags**: `#linux-kernel`, `#security`, `#llm`, `#vulnerability-analysis`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [Google Research&\#x27;s Cogentic Coordinates Multi-Agent Mathematical Proof Discovery](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10

Google Research has introduced Cogentic, a multi-agent system for automated proof discovery built on Gemini. It coordinates multiple independent provers exploring different directions, then uses an adversarial verification component to check proposed results in a proof-verification loop and stores confirmed results in a persistent, reusable ledger. In an arXiv paper, the authors report that Cogentic produced new results on five open problems in online learning, auction theory, and mechanism design. Those results were independently verified by domain experts and are expanded in companion papers.

telegram · zaihuapd · Oct 2, 12:04

**「Background」** Automated proof discovery typically combines a proposer that generates candidate proofs with a verifier that checks them, and multi-agent systems extend this by coordinating multiple specialized agents. Cogentic is Google Research&\#x27;s multi-agent harness built on Gemini that starts from problem statements alone and uses separate provers plus adversarial verification to search for proofs. The system targets open problems in areas such as online learning, auction theory, and mechanism design.

**「Impact」** For mathematicians and theoretical computer scientists working on the five open problems in online learning, auction theory, and mechanism design, Cogentic&\#x27;s expert-verified new results provide citable advances, while its adversarial proof–verification loop offers a reusable approach for automating research-level theorem discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.40324">Cogentic : Multi - Agent Orchestration for Automated Proof Discovery</a></li>
<li><a href="https://agihunt.info/en/e/1a0f9cea5c8b68af181e13c5f80">Google &#x27;s Cogentic Multi - Agent System Tackles… · AGI Hunt</a></li>
<li><a href="https://arxiv.org/abs/2609.40324">[2609.40324] Cogentic: Multi-Agent Orchestration for ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#automated theorem proving`, `#AI for mathematics`, `#Google Research`, `#Gemini`

---

<a id="item-tech-news-4"></a>
### [Redis Creator’s ds4 Runs LLMs Locally](https://dwarfstar.sh/) ⭐️ 7.0/10

ds4 is an open-source local LLM inference engine created by antirez, the creator of Redis, and is discussed on Hacker News as a way to run large language models locally without relying on cloud services. The project has attracted active community development, including shared-library forks, Go bindings \(ds4go\), and added support for Vision and Qwen models. Commenters shared practical experiences running models such as DeepSeek V4 Flash and Qwen 3.8 Flash on high-RAM Apple Silicon, reporting fast generation and long context windows. Questions remain about tool-calling performance, exact token-per-second benchmarks, and occasional context-recall issues.

hackernews · fibo · Oct 2, 18:01 · [Discussion](https://news.ycombinator.com/item?id=49936575)

**「Context」** ds4 \(DwarfStar 4\) is a narrow C inference engine created by antirez, the creator of Redis, for high-memory Mac, CUDA, and ROCm machines. It supports DeepSeek V4 and V4.1 Flash, GLM 5.x, and Qwen3.8 Flash Next, with text and vision models, local APIs, a CLI, and a native agent. The engine runs inference directly without a separate HTTP server, preserving token history and live model state together.

**「Impact」** Developers can adopt ds4 and its community bindings to run local LLMs like Qwen and DeepSeek on personal hardware, but they should verify tool-calling reliability and throughput themselves since no benchmarks are provided in the discussion.

**「Community Discussion」** The discussion includes positive reports of using ds4 on an M5 Max with 128GB, with users calling it the best launcher they&\#x27;ve tried; however, some note occasional failure to remember earlier context, and others ask for tool-calling numbers before calling it a game changer.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local ...</a></li>
<li><a href="https://dwarfstar.sh/">DwarfStar 4 (ds4): Local DeepSeek V4.1, Qwen and GLM</a></li>
<li><a href="https://dwarfstar.sh/about/">About DwarfStar 4 (ds4): antirez Local Inference Engine</a></li>

</ul>
</details>

**Tags**: `#local-llm`, `#inference-engine`, `#open-source`, `#ai`, `#software-engineering`

---

<a id="item-tech-news-5"></a>
### [Zig 0.17.0 Release and Community Reactions](https://ziglang.org/download/0.17.0/release-notes.html) ⭐️ 7.0/10

The Zig programming language project published release notes for version 0.17.0, and community discussion highlights improvements in build integration and target support, with some commenters describing the language as well-designed despite its pre-1.0 instability. The release is presented as incremental, focusing on ecosystem and tooling improvements rather than groundbreaking changes. Comments also mention that core maintainer Andrew Kelley is warming up to using LLMs to discover bugs, and community members hope for future additions such as a stackless coroutine I/O implementation and first-class fuzzer tooling. One former contributor reports leaving the ecosystem over maintainer hostility and is porting work to Odin. The release notes themselves were not included in the supplied information, so specific technical details beyond community reactions are unavailable.

hackernews · ErenayDev · Oct 2, 20:56 · [Discussion](https://news.ycombinator.com/item?id=49938521)

**「Background」** Zig is a systems programming language that is still pre-1.0 and has been working toward language stabilization. Version 0.17.0 follows 0.16.0 and is described in its release notes as a key step toward Zig 1.0, with progress made on stabilizing the language. The release includes a redesigned build system, notable improvements to incremental compilation, and changes to several language rules.

**「Impact」** Developers considering Zig 0.17.0 should expect incremental tooling and ecosystem improvements rather than breaking changes or major new language features, and should note that the release remains pre-1.0.

**「Community Discussion」** Community reaction is largely positive about Zig&\#x27;s design and target support, with specific praise for its build integration and hopes for future coroutine and fuzzer improvements. One commenter expresses disagreement over maintainer behavior, reporting a ban and a move to Odin, while another asks about the project&\#x27;s earlier hard line against AI.

<details><summary>References</summary>
<ul>
<li><a href="https://ziglang.org/download/0.17.0/release-notes.html">0 . 17 . 0 Release Notes The Zig Programming Language</a></li>
<li><a href="https://dzen.ru/a/asAsBEZa4EPtW32L">Zig 0 . 17 . 0 : быстрые пересборки становятся реальностью, но... | Дзен</a></li>

</ul>
</details>

**Tags**: `#zig`, `#programming-languages`, `#systems-programming`, `#release-notes`, `#compilers`

---

<a id="item-tech-news-6"></a>
### [FLEET: Reward-aware sampling with MCTS for Best-of-N generation](https://www.reddit.com/r/MachineLearning/comments/1wvs12j/adding_memory_to_search_instead_of_sampling_in/) ⭐️ 7.0/10

FLEET, described in a new preprint by one of its authors, enhances Best-of-N generation by attributing external rewards to individual tokens and using Monte Carlo tree search to adjust logits across runs. It tracks tokens whose logits have high entropy and varentropy as branching points, stores normalized hidden states in a vector store with reward and transition metadata, retrieves similar states via cosine similarity, and uses modified MCTS to rank top-k tokens plus an exploration set while penalizing suboptimal ones before decoding. In experiments with Llama 3.2 3B on GSM8K and LiveCodeBench v6 easy, using greedy decoding after setting suboptimal token probabilities to effectively zero, FLEET solved seven additional GSM8K tasks while reaching the sampling baseline in half the iterations, and improved LiveCodeBench score from 0.59 to 0.69 under the same budget while reaching baseline in 9 iterations instead of 32. The sequential execution is not required because the metadata can be passed as a lookup table and preserved as a prior for other tasks or to enrich SFT/RL.

reddit · r/MachineLearning · /u/Helpful\_Minimum\_2214 · Oct 2, 12:04

**「Background」** Best-of-N generation samples multiple completions and selects the highest-reward one, but typically does not use reward information to guide sampling. Monte Carlo tree search \(MCTS\) is a planning method that builds a tree of decisions and propagates outcomes, while entropy and varentropy of token logits measure the model&\#x27;s uncertainty about token optimality.

**「Impact」** For developers applying Best-of-N sampling to math and code tasks with Llama 3.2 3B, FLEET may reduce iteration counts by roughly half on GSM8K and from 32 to 9 on LiveCodeBench easy, while slightly improving LiveCodeBench accuracy and adding seven GSM8K solutions. However, these results are from a single small model and two benchmarks in a preprint, so broader generalization remains unverified.

**Tags**: `#machine learning`, `#reinforcement learning`, `#large language models`, `#MCTS`, `#inference optimization`

---

<a id="item-tech-news-7"></a>
### [Anthropic Proposes Copyright Opt-Out for AI Training in Australia](https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news) ⭐️ 7.0/10

Anthropic has proposed that Australia allow tech companies to train AI models on Australian copyrighted works under an opt-out mechanism. ABC and SBS oppose weakening copyright rules; they demand that AI companies accept copyright and privacy regulation and compensate media organizations, with ABC warning that journalism could be &\#x27;cannibalized.&\#x27; The Australian government has ruled out a text and data mining exception while continuing to discuss other copyright arrangements. Australia&\#x27;s parliamentary Joint Committee on Artificial Intelligence will hold a hearing next week with Anthropic and OpenAI executives.

telegram · zaihuapd · Oct 2, 03:34

**「Background」** In Australia, copyright law does not currently provide a broad text-and-data-mining exception, so using copyrighted material to train AI models generally requires permission or a licence. Anthropic has proposed a &\#x27;conditional approval&\#x27; scheme under which technology companies could train on Australian copyrighted works unless rightsholders actively opt out, shifting the burden from seeking licences to excluding works. The public broadcasters ABC and SBS, which produce substantial news and media content, oppose this and are calling for stronger obligations, including compensation and oversight of copyright and privacy.

**「Impact」** If the opt-out framework is adopted, Australian rightsholders such as ABC and SBS would face a greater burden to monitor and opt out of AI training while pursuing compensation, whereas AI developers would gain a clearer legal basis for using copyrighted Australian material.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/oct/02/anthropic-ai-opt-out-australia-copyright-abc-cannibalisation-of-news">Anthropic pushes for opt - out model for Australian content as ABC ...</a></li>
<li><a href="https://www.neoteo.com/en/anthropic-proposes-an-opt-out-for-ai-training-in-australia">Anthropic ’s Australia AI training opt - out proposal | NeoTeo</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#copyright`, `#Anthropic`, `#Australia`, `#generative AI`

---

<a id="item-tech-news-8"></a>
### [arXiv Caps Submissions to Two Papers per Submitter per Month](https://www.huxiu.com/article/4895127.html) ⭐️ 7.0/10

arXiv began enforcing a new policy on October 1 that limits each submitter to no more than two papers per calendar month across all subject areas, including computer science, mathematics, and physics. Rejected submissions also count toward the monthly quota, while multi-author papers count only toward the person who actually submits the manuscript. The change follows a record 40,363 submissions in September, the highest in the platform&\#x27;s 35-year history. AI-category papers have grown more than sixfold over the past two years, and the volume of low-quality AI-generated papers is straining manual review resources.

telegram · zaihuapd · Oct 2, 06:21

**「Background」** arXiv is a widely used preprint server where researchers share early versions of papers before peer review. It relies partly on human moderation to screen submissions, and the recent surge in AI-related manuscripts has increased pressure on that review process.

**「Impact」** Researchers who frequently post to arXiv—especially in AI, computer science, and machine learning—must now prioritize and schedule submissions carefully because rejected papers still consume the two-paper monthly allowance.

**Tags**: `#arXiv`, `#academic publishing`, `#AI-generated content`, `#research policy`, `#open science`

---

<a id="item-tech-news-9"></a>
### [Claude Code Adds Mods for TypeScript Customization](https://claude.com/blog/claude-code-mods) ⭐️ 7.0/10

Anthropic has introduced mods to Claude Code, letting developers use small amounts of TypeScript to rewrite prompts, add UI elements, or replace built-in functionality. Mods are distributed as plugins and are now supported in both the CLI and desktop versions. They run with the same permissions as Claude Code and are not sandboxed, so Anthropic advises installing only from trusted sources; users can also ask Claude to write mods. Some built-in features have already been converted into mods, and Anthropic plans to migrate more over time.

telegram · zaihuapd · Oct 2, 12:32

**「Background」** Claude Code is Anthropic&\#x27;s AI coding assistant that works in the terminal and desktop. Plugins are extension packages that can add capabilities to such tools; mods are a new TypeScript-based extension point for customizing how Claude Code behaves. Because mods execute with the same privileges as the host application, they are not sandboxed, which is why Anthropic cautions users to only install them from trusted sources.

**「Impact」** Developers using Claude Code can now tailor its prompts, interface, and underlying features through TypeScript plugins, but must install mods only from trusted sources because they have the same permissions and no sandbox.

**Tags**: `#Claude Code`, `#Anthropic`, `#developer tools`, `#AI coding`, `#plugins`

---

<a id="item-tech-news-10"></a>
### [Cloudflare launches unified observability platform](https://blog.cloudflare.com/one-observability-platform/) ⭐️ 7.0/10

Cloudflare announced eight updates on October 2, 2026 that unify logs, traces, analytics, alerting, dashboards, and data export into a single observability platform. The updates include request tracing and a unified SQL API in open beta, 30-day domain analytics data, custom alerts, and custom dashboards; Logpush is now available to all self-serve plans. A new unified billing model for logs and tracing will take effect on December 1, 2026, charging by ingestion and storage volume. These changes expand observability features to self-serve customers and give engineering teams a consolidated view of Cloudflare traffic.

telegram · zaihuapd · Oct 3, 01:15

**「Background」** Cloudflare&\#x27;s observability products previously existed as separate tools for logs, traces, analytics, alerts, dashboards, and querying. This update consolidates them into one platform with a unified SQL API and expands features such as request tracing, 30-day analytics, custom alerts, and dashboards. A new unified billing model for logs and traces, based on ingestion and storage, becomes effective December 1, 2026.

**「Impact」** For Cloudflare users on self-serve plans, Logpush and the unified observability features \(request tracing, unified SQL API, custom alerts and dashboards\) become available, but logs and traces will move to ingestion- and storage-based billing on December 1, 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/one-observability-platform/">8 major updates to Cloudflare Observability | Cloudflare Blog</a></li>
<li><a href="https://dropagentic.com/cloudflare-observability-updates-unified-platform/">Cloudflare launches eight observability updates</a></li>
<li><a href="https://blog.cloudflare.com/one-observability-platform/">8 major updates to Cloudflare Observability | Cloudflare Blog</a></li>
<li><a href="https://www.brocker.org/cloudflare-observability-eight-updates-logs-traces-sql-api-pricing">Cloudflare Unifies Observability With 8 Updates, New Pricing</a></li>
<li><a href="https://dropagentic.com/cloudflare-observability-updates-unified-platform/">Cloudflare launches eight observability updates</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#observability`, `#logging`, `#tracing`, `#analytics`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Traders cut October Fed rate hike odds after weak September jobs report](https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html) ⭐️ 8.0/10

The U.S. added 29,000 jobs in September, below estimates of more than 80,000, and traders cut the odds of an October Federal Reserve rate hike to 17% on CME FedWatch, down from 36% a week earlier.

rss · CNBC Finance · Oct 2, 13:29

**「Background」** The Federal Reserve raised its benchmark rate to 3.75%–4% at its September 2026 meeting, citing elevated inflation, and its next policy decision is due October 28.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html">Fed rate decision September 2026 : Rates rise to 3.75%-4%</a></li>

</ul>
</details>

**Tags**: `#Federal Reserve`, `#interest rates`, `#jobs report`, `#inflation`, `#market expectations`

---

<a id="item-finance-news-2"></a>
### [Midday movers: Tesla, Broadcom, Nike, Synaptics and ON Semiconductor](https://www.cnbc.com/2026/10/02/stocks-making-the-biggest-moves-midday-tsla-avgo-nke-on-more-.html) ⭐️ 7.0/10

Tesla rose 5% after reporting third-quarter deliveries of 486,532 vehicles, above the 461,100 FactSet estimate, and Broadcom rose more than 3% after Reuters reported it agreed to lend Anthropic up to $42 billion. Nike fell almost 6% after fiscal first-quarter revenue missed LSEG analyst expectations and sales slid 4% citing China declines, while Synaptics surged 14% after ON Semiconductor raised its buyout bid to $123 per share, or $5.7 billion.

rss · CNBC Finance · Oct 2, 17:52

**「Background」** The moves are part of CNBC&\#x27;s midday roundup of stocks making the largest intraday moves on company news, analyst actions, and deal reports.

**Tags**: `#stock movers`, `#earnings`, `#mergers and acquisitions`, `#semiconductors`, `#electric vehicles`

---

<a id="item-finance-news-3"></a>
### [Premarket Movers: Nike Falls, ON Semi-Synaptics Deal, Hard-Drive Makers Drop](https://www.cnbc.com/2026/10/02/stocks-making-the-biggest-moves-premarket-nike-on-semiconductor-synaptics-vylor-more.html) ⭐️ 7.0/10

Nike shares fell over 10% after missing fiscal first-quarter revenue against LSEG consensus and announcing a 2027 layoff plan. Synaptics jumped over 14% and ON Semiconductor over 7% after reports ON Semi will acquire Synaptics for $123 per share in cash, a $5.7 billion deal; Seagate and Western Digital dropped over 11% and 8% after Toshiba said it would double data-center hard-drive capacity.

rss · CNBC Finance · Oct 2, 12:03

**「Background」** The Synaptics acquisition was revised to a $123-per-share cash offer after an unsolicited competing proposal, replacing the prior all-stock agreement; separately, Toshiba’s planned $380 million hard-disk-drive expansion is its first major capacity build-out since AI data-center storage demand tightened supply.

**「Impact on investors」** Nike, Seagate, and Western Digital investors absorbed premarket losses after Nike missed fiscal first-quarter revenue expectations and announced 2027 layoffs, and Toshiba said it would double HDD production capacity; ON Semiconductor and Synaptics investors gained on reports of a $5.7 billion cash acquisition.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/semiconductor-climbs-8-synaptics-surges-131302389.html?ref=biztoc.com">On Semiconductor Climbs 8%, Synaptics Surges 14% as...</a></li>
<li><a href="https://www.alphapilot.tech/discover/toshiba-doubles-hdd-supply-by-fiscal-2027-seagate-western-digital-tumble">Toshiba Doubles HDD Supply by Fiscal 2027: Seagate , Western ...</a></li>
<li><a href="https://finance.yahoo.com/markets/stocks/articles/nike-q1-2027-earnings-job-133725772.html?fr=sycsrp_catchall">Nike Q1 2027 earnings: job cuts, revenue outlook, China sales</a></li>

</ul>
</details>

**Tags**: `#earnings`, `#mergers and acquisitions`, `#semiconductors`, `#hard disk drives`, `#stock market`

---

<a id="item-finance-news-4"></a>
### [Wall Street Banks&\#x27; AI Job Listings Jump 49%, Led by Agent Orchestration](https://www.cnbc.com/2026/10/02/ai-skills-most-in-demand-at-jpmorgan-chase-citigroup-capital-one.html) ⭐️ 7.0/10

AI-related job postings at JPMorgan Chase, Citigroup and Capital One rose 49% this year compared with 2025 to 139,819 listings, according to hiring data firm Draup. References to &\#x27;agent orchestration&\#x27;—designing AI agents to work together—jumped 1,721% over the same period.

rss · CNBC Finance · Oct 2, 11:03

**「Background」** The earlier AI hiring wave was dominated by engineers and data scientists building models, but the boom has expanded to include forward-deployed engineers who embed AI directly into business lines.

**Tags**: `#AI`, `#Wall Street`, `#jobs`, `#banking`, `#agent orchestration`

---

<a id="item-finance-news-5"></a>
### [Bitget expects limited recovery from $388 million hack but says user balances unaffected](https://www.cnbc.com/2026/10/02/bitget-crypto-stolen-hack-recovery.html) ⭐️ 7.0/10

Crypto exchange Bitget lost nearly $388 million in last week&\#x27;s cyberattack, of which about $1.1 million has been frozen, and CEO Gracy Chen told CNBC she is &quot;not expecting to recover a lot of funds.&quot; Bitget said user account balances were unaffected.

rss · CNBC Finance · Oct 2, 06:03

**「Background」** Mandiant and SlowMist reports released Sept. 30 found attackers compromised two third-party security products and exploited a previously unknown, or zero-day, vulnerability traced to Aug. 31 before gaining privileged access to Bitget&\#x27;s production wallet systems.

**Tags**: `#cryptocurrency exchange`, `#cyberattack`, `#Bitget`, `#asset recovery`, `#security`

---