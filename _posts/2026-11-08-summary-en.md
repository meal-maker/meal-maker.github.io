---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 39 items, 13 important content pieces were selected

---

**Technology News**
1. [Undocumented macOS Daemons Build Personal Relationship Graph Since 2022](#item-tech-news-1) ⭐️ 8.0/10
2. [China’s 800MW Wind-Powered AI Data Center Campus in Inner Mongolia](#item-tech-news-2) ⭐️ 8.0/10
3. [Apple Discloses HALO Humanoid Robot System Using Two Qwen Models](#item-tech-news-3) ⭐️ 8.0/10
4. [GitHub&\#x27;s Rubicon Architecture Handles 7,200 Pushes/Sec](#item-tech-news-4) ⭐️ 8.0/10
5. [Microsoft Research AI Frontiers group ends, John Langford exits](#item-tech-news-5) ⭐️ 7.0/10
6. [Claude Code&\#x27;s &quot;Don&\#x27;t Ask Again&quot; exposes passwords in 1,122 public GitHub files](#item-tech-news-6) ⭐️ 7.0/10
7. [Coldframe Honeypot Mimics Supermarket Fridge Controllers](#item-tech-news-7) ⭐️ 7.0/10
8. [MaxxBench Stress-Tests DeepSWE Scores and Finds Instability](#item-tech-news-8) ⭐️ 7.0/10
9. [Asahi Linux Progress Report 7.3 Details Fedora Remix and Hardware Gaps](#item-tech-news-9) ⭐️ 7.0/10
10. [Claude Code May Leak User Email During Web Searches](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Berkshire Hathaway more than doubles Q3 buybacks to $9.6 billion as earnings decline](#item-finance-news-1) ⭐️ 8.0/10
2. [SoftBank and ABB Weigh China Carve-Out to Revive $5.4 Billion Robotics Deal](#item-finance-news-2) ⭐️ 8.0/10
3. [Nationwide Financial Inspection Launched for 33,500 Buddhist Temples](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Undocumented macOS Daemons Build Personal Relationship Graph Since 2022](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 8.0/10

An investigation reports that every Mac shipped since 2022 includes undocumented daemons that build a personal knowledge graph of users&\#x27; relationships, communications, and locations. The research identifies a family member classifier among these daemons, which infer who users know, how people are related, and where and with whom users go. The daemons appear to operate without clear user disclosure or explicit consent. The finding raises significant privacy questions for macOS users. The author has published follow-up research on Apple Intelligence knowledge graphs.

hackernews · infwhispers · Nov 7, 09:46 · [Discussion](https://news.ycombinator.com/item?id=50403097)

**「Background: Daemons and Personal Knowledge Graphs」** Daemons are background system processes that run without direct user interaction. A personal knowledge graph is a structured collection of entities and relationships describing a user&\#x27;s contacts, communications, and activities. According to the investigation, these daemons are present on every Mac running macOS 13 \(2022\) or later and appear to feed into Apple Intelligence features such as Siri&\#x27;s contextual understanding.

**「Community Discussion」** Comments show mixed reactions: some readers are unsurprised because Photos already identifies people and pets, while others emphasize privacy expectations and the need for explicit consent. One commenter suggests the daemons provide context for local Siri requests such as disambiguating contacts or identifying &\#x27;my boss&\#x27;; the research author is present and points to follow-up work.

<details><summary>References</summary>
<ul>
<li><a href="https://8rank.ai/game/apple-intelligence-personal-knowledge-graph">Anatomy of Apple &#x27;s Personal Knowledge Graph — Eighth Rank</a></li>

</ul>
</details>

**Tags**: `#apple`, `#privacy`, `#macos`, `#knowledge-graph`, `#daemons`

---

<a id="item-tech-news-2"></a>
### [China’s 800MW Wind-Powered AI Data Center Campus in Inner Mongolia](https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner) ⭐️ 8.0/10

SemiAnalysis visited a wind-powered data center campus in Inner Mongolia designed for 800MW total capacity, with 120MW completed within a year. The site includes a 5MW pilot using solid-state transformer \(SST\)-native 800V DC power distribution. Its cooling architecture eliminates central chillers. These innovations are intended to improve power efficiency and deployment speed for AI infrastructure.

rss · Semianalysis · Nov 7, 19:01

**「Context: China’s AI datacenter build-out」** SemiAnalysis reports visiting &\#x27;Galaxy,&\#x27; an AI data center campus in Ulanqab, Inner Mongolia, developed by Envision, planned for up to 800MW of IT capacity and powered mainly by wind. Inner Mongolia is characterized as China&\#x27;s fastest-growing AI datacenter region, compared to a &\#x27;West Texas&\#x27; without anti-datacenter backlash. The visit highlights unusually rapid construction—120MW built within a year—and engineering pilots such as a 5MW solid-state-transformer-native 800V DC system and a chiller-less cooling design.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner">We Visited China’s Stargate in Inner Mongolia</a></li>
<li><a href="https://cryptobriefing.com/envision-galaxy-ai-datacenter-inner-mongolia/">Envision’s Galaxy datacenter shows how fast China is ...</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#AI infrastructure`, `#power distribution`, `#cooling technology`, `#China`

---

<a id="item-tech-news-3"></a>
### [Apple Discloses HALO Humanoid Robot System Using Two Qwen Models](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 8.0/10

On November 4, Apple researchers submitted an arXiv preprint introducing HALO, a three-layer autonomous control system for humanoid robots, and validated it on a Unitree G1 by transferring actions learned in simulation to unfamiliar real rooms. The upper layer uses Qwen3.6-35B-A3B to orchestrate tasks, the middle layer uses Qwen3.5-2B to generate motions, and the bottom layer is an RL-trained action tracker. The team has publicly released code for data generation, model training, and deployment.

telegram · zaihuapd · Nov 7, 13:35

**「Background」** Unitree G1 is a commercially available humanoid robot from Unitree Robotics, often used for research and available in simulation environments such as MuJoCo. Qwen models are large language models that can be used for high-level task planning and action generation in robotic systems. Sim-to-real transfer is a technique where control policies learned in simulation are applied to physical robots in real-world settings.

**「Impact」** Robotics researchers and developers can access the public code for HALO&\#x27;s data generation, model training, and deployment, enabling replication and further work on this hierarchical Qwen-based control approach for humanoid hardware such as the Unitree G1.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=GzX1qOIO1bE">Unitree Introducing | Unitree G 1 Humanoid Agent | AI Avatar - YouTube</a></li>
<li><a href="https://github.com/unitreerobotics/unitree_mujoco">GitHub - unitreerobotics/ unitree _mujoco · GitHub</a></li>

</ul>
</details>

**Tags**: `#humanoid robots`, `#Apple`, `#Qwen`, `#reinforcement learning`, `#sim-to-real`

---

<a id="item-tech-news-4"></a>
### [GitHub&\#x27;s Rubicon Architecture Handles 7,200 Pushes/Sec](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 8.0/10

GitHub has introduced Rubicon, a new Git storage architecture designed for scenarios with many AI agents concurrently operating on a single repository. In internal testing, it supported 5,000 agents collaborating simultaneously and handled 7,200 pushes per second while keeping read latency low. The design stores Git objects in Azure Blob Storage, manages reference state with Ref-CAS, uses virtual replicas for reads and writes, and runs background nodes to compact data packs. Rubicon is currently in a limited private preview and will be expanded gradually.

telegram · zaihuapd · Nov 7, 14:12

**「Background」** Object storage services such as Azure Blob Storage are a natural fit for data-heavy applications like source code storage. In Rubicon, each push adds a pack to Blob Storage, while Ref-CAS coordinates reference state and background nodes compact packs; this decouples storage from compute so compaction can run at thousands of writes per second.

**「Impact」** Developers and organizations targeting AI-agent-scale repository concurrency cannot yet rely on Rubicon because it is in a limited private preview with gradual rollout rather than general availability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/">Inside GitHub &#x27;s new Git storage architecture - The GitHub Blog</a></li>

</ul>
</details>

**Tags**: `#github`, `#git`, `#storage-architecture`, `#ai-agents`, `#infrastructure`

---

<a id="item-tech-news-5"></a>
### [Microsoft Research AI Frontiers group ends, John Langford exits](https://hunch.net/?p=13764006) ⭐️ 7.0/10

Microsoft Research&\#x27;s AI Frontiers group, which focused on fundamental advances in AI, has been declared ended, and researcher John Langford is exiting. The move is part of a broader industry pivot away from exploratory, fundamental AI research toward prioritizing scaling of transformer-based models. Large technology companies are concentrating resources on transformer scale-out and iteration, discouraging work on alternative AI methods.

hackernews · srean · Nov 7, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50406563)

**「Background」** Microsoft Research&\#x27;s AI Frontiers group was founded in 2023 after ChatGPT&\#x27;s release to pursue fundamental advances in AI beyond simply scaling existing models. It built Autogen, a framework for coordinating AI agents, and Fara, an agent that operates a computer, and had roughly 50 researchers. John Langford, a long-time Microsoft Research leader and creator of the Vowpal Wabbit learning library, led the group until its dissolution in November 2026 after a September move into Microsoft AI.

**「Impact」** For AI researchers, the closure signals reduced support for exploratory, non-transformer work at large companies, as resources shift to scaling transformer models.

**「Community discussion」** Commenters largely agree the closure reflects an industry-wide emphasis on transformer scaling and risk aversion, but some caution that starving exploratory research could leave companies behind if the chosen path proves suboptimal; one commenter says the move breaks Microsoft Research&\#x27;s long-standing cultural contract that doing good work leads to good outcomes.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/microsoft-researcher-john-langford-exits-ai-frontiers-group-declared-finished-t8nprypt6">Microsoft Researcher John Langford Exits. AI Frontiers Group ...</a></li>
<li><a href="https://explainx.ai/blog/john-langford-microsoft-ai-frontiers-ended-mai-scaling-only-2026">Microsoft AI Frontiers Ends: Langford on MAI Clash - explainx.ai</a></li>

</ul>
</details>

**Tags**: `#Microsoft Research`, `#AI research`, `#organizational change`, `#machine learning`, `#tech industry`

---

<a id="item-tech-news-6"></a>
### [Claude Code&\#x27;s &quot;Don&\#x27;t Ask Again&quot; exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 7.0/10

Apiiro&\#x27;s recent scan identified 1,122 public GitHub files containing credentials exposed through Claude Code&\#x27;s locally stored &\#x27;Don&\#x27;t Ask Again&\#x27; command approvals. The leaks occur when developers commit their \`.claude/settings.local.json\` file after approving commands that embed passwords or API keys directly in the command string. Claude Code normally writes this file and adds it to \`.gitignore\` automatically, so the affected files were manually created or forced into version control. The findings reflect a user workflow risk rather than an exploitable vulnerability in Claude Code itself. The exposure highlights how AI coding agents can amplify secret-leakage mistakes when local approval settings are accidentally published.

hackernews · shmulc · Nov 7, 20:45 · [Discussion](https://news.ycombinator.com/item?id=50407882)

**「Background」** Claude Code stores locally approved shell commands, including those marked with the &quot;Don&\#x27;t Ask Again&quot; option, in a settings file such as \`.claude/settings.local.json\`. This file is intended to remain local and is automatically gitignored when Claude Code creates it, but developers can manually create or commit it. If such a file contains commands with embedded passwords or API keys, committing it to a public repository exposes those secrets.

**「Impact」** Developers using Claude Code should avoid committing \`.claude/settings.local.json\` and should remove embedded secrets from approved commands, as public exposure of such files has already leaked passwords in over a thousand repositories.

**「Community Discussion」** A Claude Code team member clarified that \`.claude/settings.local.json\` is intended to remain local and is auto-gitignored when generated, and that the company is investigating prevention measures; several commenters emphasized the leak requires manually committing a settings file with secrets embedded in approved commands. Other developers described alternative workflows such as ephemeral VMs, restricted API proxies, or password-manager CLI integration to avoid exposing credentials to AI agents.

**Tags**: `#security`, `#ai-coding-assistant`, `#claude-code`, `#secret-leakage`, `#github`

---

<a id="item-tech-news-7"></a>
### [Coldframe Honeypot Mimics Supermarket Fridge Controllers](https://github.com/hedgerow-dev/coldframe) ⭐️ 7.0/10

Developer hedgerow-dev built Coldframe, a single-file Python honeypot using only the standard library that impersonates Danfoss AK-SM 800A and Dixell XWEB supermarket refrigeration controllers to detect exploitation attempts. The project replicates real device fingerprints by matching header order, page titles, certificate fields, and TLS versions from Shodan records; the Danfoss persona sends nginx headers in the same order as a real AK-SM 800A, and the Dixell persona omits the Server header and pads its page to exactly 8,202 bytes. Coldframe recognizes CVE-2025-41450, the Danfoss &quot;code of the day&quot; login bypass, records whether a submitted code is correct for the current day, and tags attempts targeting three other Danfoss CVEs and XWEB vulnerabilities. Default credentials open a fake store dashboard with defrost buttons so operators can observe the attacker&\#x27;s second move. Two live instances running for about a day have so far only seen generic scanners and Shodan&\#x27;s refrigerator.census.shodan.io crawler.

hackernews · hedgerow-dev · Nov 7, 17:27 · [Discussion](https://news.ycombinator.com/item?id=50406292)

**「Background」** Industrial refrigeration controllers such as Danfoss AK-SM 800A and Dixell XWEB expose web interfaces and have been targeted in recent attacks, making them candidates for internet-wide scanning and compromise. A honeypot is a decoy system designed to attract and log malicious interactions, providing insight into attacker behavior. Shodan is a search engine for internet-connected devices that can be used to study exposed equipment and their fingerprints.

**「Impact」** Security researchers and network defenders can deploy Coldframe to observe exploit attempts against realistic fridge controller interfaces, but the initial day-long deployment only attracted generic scanners, so its effectiveness against targeted attackers remains unproven.

**「Community Discussion」** Commenters were skeptical of using Shodan data for fingerprinting because many indexed devices are themselves honeypots or already compromised, and one suggested obtaining real hardware for more accurate replication. The discussion also noted that supermarkets lack dedicated security teams and raised uncertainty about whether recent refrigeration incidents were coordinated hacks or simultaneous software updates.

**Tags**: `#honeypot`, `#IoT security`, `#industrial control systems`, `#cybersecurity`, `#open source`

---

<a id="item-tech-news-8"></a>
### [MaxxBench Stress-Tests DeepSWE Scores and Finds Instability](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 7.0/10

MaxxBench examines whether high DeepSWE scores hold up under varied task specifications and finds notable instability, especially in smaller models, raising concerns about benchmark reliability. The method varies task parameters to test how much scores change, and the observed degradation suggests that models may be overfitting to particular benchmark task formulations. This critique is timely for AI/ML practitioners who rely on SWE benchmarks.

hackernews · antiuniverse · Nov 7, 17:19 · [Discussion](https://news.ycombinator.com/item?id=50406222)

**「Context」** DeepSWE is a long-horizon software engineering benchmark created to mitigate contamination, narrow repository coverage, overspecified task descriptions, and unreliable verifiers by sourcing original tasks and using hand-written behavioral verifiers \(tool-1-2\). MaxxBench mutates 89 of these DeepSWE tasks by altering instructions or starting code—for example requiring lowercase filenames or UTC timestamps—while keeping median patch growth small, to measure whether coding agents adapt rather than rely on memorized or guessed answers \(tool-1-1\).

**「Impact」** AI/ML practitioners evaluating smaller coding models should be cautious about treating high DeepSWE scores as evidence of generalization, since MaxxBench shows those scores drop sharply when task specifications vary.

**「Community Discussion」** Commenters largely agree that the instability is meaningful and that smaller models, especially &\#x27;-flash&\#x27; and OpenAI Luna variants, show the steepest declines. They also highlight bugs in DeepSWE and suggest the root cause may be labs training in overly narrow RL environments rather than deliberate benchmark gaming, with one practical suggestion to avoid &\#x27;max mode&\#x27;.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/maxxbench-nice-deepswe-score-but-is-it-true--ue9ulip60">MaxxBench – &quot;Nice DeepSWE score. But is it true?&quot;</a></li>
<li><a href="https://zhongzhoutan-coder.github.io/benchmarks/agent-eval/deepswe/">DeepSWE: Long-Horizon Software Engineering Benchmark</a></li>

</ul>
</details>

**Tags**: `#benchmarking`, `#AI evaluation`, `#large language models`, `#software engineering`, `#DeepSWE`

---

<a id="item-tech-news-9"></a>
### [Asahi Linux Progress Report 7.3 Details Fedora Remix and Hardware Gaps](https://asahilinux.org/2026/11/progress-report-7-3/) ⭐️ 7.0/10

Asahi Linux&\#x27;s latest progress report covers updates to Fedora Asahi Remix, remaining hardware support gaps, licensing concerns, and related Vulkan work for Linux on Apple Silicon. Fedora Linux 45 and Fedora Asahi Remix were both released on 3 November, marking the first time the remix shipped on the same day as upstream Fedora. The report also acknowledges USB-C display support as a blocking gap for some Apple Silicon users and addresses multiple attempts to exploit the project&\#x27;s permissive licensing for commercial replacement efforts.

hackernews · ackyshake · Nov 7, 05:20 · [Discussion](https://news.ycombinator.com/item?id=50401867)

**「Background」** Asahi Linux is a community-driven open-source project that ports Linux to Apple Silicon Macs, whose custom hardware and firmware lack official Linux support. The project develops drivers, bootloaders, and a Fedora-based distribution called Fedora Asahi Remix, and all development is conducted in the open. Progress reports are periodic updates covering new hardware support, distribution changes, and project decisions.

**「Impact」** Apple Silicon users who depend on USB-C displays face a concrete blocker to adopting Asahi Linux, and the licensing disputes may slow or fragment community-led Linux support for Apple hardware.

**「Community Discussion」** Commenters largely praised the same-day Fedora Asahi Remix release, while some expressed frustration that USB-C display support remains missing and questioned whether external projects like Gravity Linux are making faster progress on Vulkan and suspend-to-RAM. Others speculated about the licensing exploitation attempts, with one commenter asking if the report refers to Omarchy and questioning why Asahi&\#x27;s work was MIT-licensed rather than GPL.

<details><summary>References</summary>
<ul>
<li><a href="https://asahilinux.org/2026/11/progress-report-7-3/">Progress Report: Linux 7.3 - Asahi Linux</a></li>

</ul>
</details>

**Tags**: `#Asahi Linux`, `#Apple Silicon`, `#Linux`, `#open source`, `#hardware enablement`

---

<a id="item-tech-news-10"></a>
### [Claude Code May Leak User Email During Web Searches](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 7.0/10

A developer reported that Claude Code included the user&\#x27;s login email in model context and could send it in web requests, leading to daily spam and phishing emails. Anthropic engineers explained that the email was added to context to fix Claude incorrectly filling in author names. The issue was first reported in July, with emails sent to sites such as Wikipedia and the U.S. Securities and Exchange Commission. Version 2.1.317 added a block, but it can be bypassed with a Python script. Anthropic plans to remove the login email from context in the next version.

telegram · zaihuapd · Nov 7, 08:09

**「Background」** Claude Code is Anthropic&\#x27;s coding assistant that can perform web requests, and the login email was placed into its model context to prevent incorrect author name generation. This introduced a privacy risk when the model used that context for external web calls.

**「Impact」** Developers using Claude Code risk having their login email exposed in web requests to external sites, potentially increasing spam or phishing until the next version removes the email from context; the 2.1.317 block can be bypassed by a Python script.

**Tags**: `#claude-code`, `#security`, `#privacy`, `#ai-tools`, `#software-engineering`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Berkshire Hathaway more than doubles Q3 buybacks to $9.6 billion as earnings decline](https://www.cnbc.com/2026/11/07/berkshire-hathaway-q3-2026-earnings-buybacks.html) ⭐️ 8.0/10

Berkshire Hathaway more than doubled its share buybacks to $9.6 billion in the third quarter of 2026, from $4.5 billion in the second quarter. Its operating earnings fell 5.8% year over year to $12.705 billion, and overall earnings fell 28% to $22.112 billion.

rss · CNBC Finance · Nov 7, 15:23

**「Background」** The repurchase acceleration came as insurance profits pulled back: underwriting fell 43% year over year to $1.352 billion, and investment income fell 14% to $2.734 billion.

**Tags**: `#Berkshire Hathaway`, `#earnings`, `#buybacks`, `#insurance`, `#cash holdings`

---

<a id="item-finance-news-2"></a>
### [SoftBank and ABB Weigh China Carve-Out to Revive $5.4 Billion Robotics Deal](https://www.bloomberg.com/news/articles/2026-11-07/softbank-abb-weigh-china-carve-out-to-salvage-robotics-deal) ⭐️ 8.0/10

SoftBank and ABB are considering carving out the China portion of ABB&\#x27;s robotics business to revive a $5.4 billion acquisition that Chinese regulators blocked on Thursday. People familiar with the matter say the China business could be valued at $2 billion to $3 billion, but the plan may fail and ABB is also weighing other options including another buyer.

telegram · zaihuapd · Nov 7, 11:24

**「Background」** China’s foreign investment security review office blocked the original $5.4 billion acquisition of ABB’s robotics unit by SoftBank, prompting the companies to weigh a China carve-out into a separate entity led by SoftBank.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/iansayson/2026/11/07/china-blocks-54-billion-abb-robotics-deal-with-billionaire-masayoshi-sons-softbank/">China blocks $5.4 billion ABB Robotics deal with ... - Forbes</a></li>
<li><a href="https://www.wsj.com/business/deals/abb-confirms-china-blocked-softbank-deal-for-robotics-unit-cf1d44bf">China Blocks $5.4 Billion SoftBank, ABB Robot Deal, Flexing ...</a></li>
<li><a href="https://www.ft.com/content/f10c3e24-45e4-47ff-bde2-24a8de90aec4?syn-25a6b1a6=1">China blocks SoftBank’s $5.4bn takeover of ABB’s robotics ...</a></li>

</ul>
</details>

**Tags**: `#SoftBank`, `#ABB`, `#robotics`, `#M&amp;A`, `#China FDI`

---

<a id="item-finance-news-3"></a>
### [Nationwide Financial Inspection Launched for 33,500 Buddhist Temples](https://www.163.com/dy/article/LB2VSRQD0556HNS1.html) ⭐️ 7.0/10

A nationwide financial inspection has been launched covering 33,500 Buddhist temples and more than 9,000 Taoist temples, requiring contracted operations to be cleared, financing channels to be cut, and third-party audits for sites above a certain income threshold.

telegram · zaihuapd · Nov 7, 15:02

**「Background」** The temple counts cited in the report come from a 2018 State Council Information Office white paper, which listed 33,500 Buddhist temples and over 9,000 Taoist temples nationwide.

**「New financial obligations」** The policy requires covered temples and Taoist temples to end contracted operations, cut off stock-market financing, and—at least for those above an income threshold—hire outside auditors, centralize collection of donations and electronic payments, and publicly disclose accounts, changing their financial governance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/1992513/djy/blob/master/gb/26/11/5/n14883359.md">djy/gb/26/11/5/n14883359.md at master · 1992513/djy · GitHub</a></li>

</ul>
</details>

**Tags**: `#宗教商业化监管`, `#财务大检查`, `#寺院经济`, `#第三方审计`, `#政策监管`

---