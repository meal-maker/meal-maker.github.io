---
layout: default
title: "Horizon Summary: 2026-04-12 (EN)"
date: 2026-04-12
lang: en
---

> From 16 items, 8 important content pieces were selected

---

1. [Small AI models detect same vulnerabilities as Mythos in isolated code.](#item-1) ⭐️ 8.0/10
2. [Beating the Two-VM Limit on Apple Silicon Macs](#item-2) ⭐️ 8.0/10
3. [Berkeley Paper Exposes Critical Vulnerabilities in AI Agent Benchmarks](#item-3) ⭐️ 8.0/10
4. [OpenClaw v2026.4.10 Adds Codex Model Management, Active Memory Plugin, and Experimental macOS Speech.](#item-4) ⭐️ 7.0/10
5. [Advanced Mac Substitute Reimplements 1980s Mac OS APIs](#item-5) ⭐️ 7.0/10
6. [OpenAI acquires Cirrus Labs, shutting down Cirrus CI by June 2026.](#item-6) ⭐️ 7.0/10
7. [The Problem That Built an Industry](#item-7) ⭐️ 7.0/10
8. [Show HN: Pardonned.com – A Searchable Database of US Presidential Pardons](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Small AI models detect same vulnerabilities as Mythos in isolated code.](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) ⭐️ 8.0/10

Research shows that smaller, cheaper AI models can identify the same software vulnerabilities as large models like Anthropic's Claude Mythos when tested on isolated code snippets. However, the real-world application of such detection requires context-aware analysis that considers the entire system. This finding challenges the narrative that only frontier AI models are effective for cybersecurity, potentially enabling more cost-effective vulnerability detection and broadening AI adoption in software security. It underscores the critical role of context in real-world bug hunting, where understanding code in its full environment is key. In tests, eight out of eight small open-weights models detected Mythos's flagship FreeBSD exploit, with one model having only 3.6 billion active parameters and costing $0.11 per million tokens. A major caveat is that this success was achieved on isolated code, which simplifies the task compared to finding vulnerabilities in complex, integrated software systems where context matters.

hackernews · dominicq · Apr 11, 16:47

**Background**: Claude Mythos is an AI model previewed by Anthropic designed to autonomously discover zero-day vulnerabilities and develop exploits, as highlighted in recent announcements. Context-aware analysis in cybersecurity involves evaluating threats based on factors like application behavior, user identity, and network data, rather than examining code in isolation, which is essential for accurate vulnerability prioritization and detection.

<details><summary>References</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://www.todyl.com/blog/role-of-context-cybersecurity">The role of context in cybersecurity - Todyl</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the methodology, with users arguing that isolating code fundamentally alters the vulnerability detection task and that real-world bug finding requires understanding context in large programs. There is acknowledgment of cost savings with small models but disagreement on their practical efficacy outside controlled settings.

**Tags**: `#AI`, `#Cybersecurity`, `#Machine Learning`, `#Software Engineering`, `#Vulnerability Detection`

---

<a id="item-2"></a>
## [Beating the Two-VM Limit on Apple Silicon Macs](https://khronokernel.com/macos/2023/08/08/AS-VM.html) ⭐️ 8.0/10

A blog post published in August 2023 details technical methods to circumvent Apple's restriction that limits users to running only two macOS virtual machines simultaneously on Apple Silicon Macs. This is significant for developers, testers, and enterprises who rely on multiple isolated environments for software testing, development, or emulation, as it challenges Apple's control over virtualization licensing and hardware usage. The workaround involves using custom kernel collections, which disables streamlined OS updates. Additionally, with macOS 15 Sequoia, nested virtualization on M3+ Macs might provide an alternative way to bypass this limit.

hackernews · krackers · Apr 11, 20:58

**Background**: Apple's Virtualization.framework is a software layer that manages virtual machines on Apple Silicon Macs, enforcing a license limit of two macOS VMs per device. Nested virtualization allows a virtual machine to host another VM, a feature supported in ARMv8.3 architecture and introduced in macOS 15 for M3+ chips.

<details><summary>References</summary>
<ul>
<li><a href="https://eclecticlight.co/2022/08/04/virtualisation-on-apple-silicon-macs-8-how-apple-limits-vms/">Virtualisation on Apple silicon Macs: 8 How Apple limits VMs</a></li>
<li><a href="https://forum.parallels.com/threads/macos-15-sequoia-nested-virtualization-for-m3-macs.364397/">macOS 15 Sequoia: nested virtualization for M3+... | Parallels Forums</a></li>

</ul>
</details>

**Discussion**: Community comments express frustration with the uniform two-VM limit, suggest tiered limits based on Mac performance, and note the irony of a developer moving to Apple. There is also speculation that nested virtualization in newer Macs could bypass the restriction.

**Tags**: `#Apple Silicon`, `#Virtualization`, `#macOS`, `#Systems Engineering`, `#Workaround`

---

<a id="item-3"></a>
## [Berkeley Paper Exposes Critical Vulnerabilities in AI Agent Benchmarks](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/) ⭐️ 8.0/10

Researchers from UC Berkeley published a paper demonstrating how to exploit vulnerabilities in top AI agent benchmarks, such as FieldWorkArena and Terminal-Bench, achieving near-perfect scores without solving any tasks. This exposes fundamental flaws in current benchmarking practices, which could lead to misleading performance metrics and erode trust in AI evaluations, necessitating a reevaluation of how benchmarks are designed to prevent exploitation. The exploits range from simple tactics like sending empty JSON objects ({}) to FieldWorkArena to more complex methods like trojanizing binary wrappers in Terminal-Bench, all capitalizing on evaluations that optimize for score rather than genuine task completion.

hackernews · Anon84 · Apr 11, 19:15

**Background**: AI agent benchmarks are standardized tests used to evaluate AI systems' capabilities in interactive environments, similar to how traditional benchmarks assess machine learning models. However, like adversarial attacks in machine learning where models can be deceived, these benchmarks are susceptible to exploitation if not designed with security measures. Recent discussions, such as those from NIST and Anthropic, highlight ongoing challenges in creating robust evaluations for AI agents and the need to address loopholes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nist.gov/blogs/caisi-research-blog/cheating-ai-agent-evaluations">Cheating On AI Agent Evaluations | NIST</a></li>
<li><a href="https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents">Demystifying evals for AI agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed, with some praising the paper for exposing vulnerabilities and advocating for benchmark reform, while others debate the novelty, noting that benchmark gaming through methods like training on test data is already known. Additional comments include concerns about the blog being AI-written and discussions on the reliability of benchmarks like ARC-AGI.

**Tags**: `#AI`, `#benchmarks`, `#evaluation`, `#research`, `#security`

---

<a id="item-4"></a>
## [OpenClaw v2026.4.10 Adds Codex Model Management, Active Memory Plugin, and Experimental macOS Speech.](https://github.com/openclaw/openclaw/releases/tag/v2026.4.10) ⭐️ 7.0/10

OpenClaw version 2026.4.10 introduces a bundled Codex provider for managing 'codex/gpt-*' models with separate auth and threading, a new optional Active Memory plugin for automatic context retrieval in chats, and an experimental MLX-based speech provider for local text-to-speech in Talk Mode on macOS. The release also includes updates for video generation, Microsoft Teams, and new QA testing lanes. This release significantly enhances OpenClaw's core capabilities by streamlining model management for developers, introducing a novel 'active memory' paradigm that could make AI assistants more context-aware and less reliant on manual user prompts, and offering a high-performance, local speech synthesis option for macOS users, improving privacy and latency. These features collectively push the project towards more autonomous, efficient, and user-friendly AI assistant systems. The Active Memory plugin is configurable with different context modes (message/recent/full), offers live inspection via `/verbose`, and allows for prompt overrides and opt-in transcript persistence for debugging. The experimental MLX speech provider for macOS includes explicit provider selection, local utterance playback, and handles interruptions with a system-voice fallback. The Codex provider creates a distinct management path separate from the standard 'openai/gpt-*' models.

github · steipete · Apr 11, 02:43

**Background**: OpenAI Codex refers to a series of language models and an AI agent product from OpenAI, historically optimized for coding tasks but now encompassing broader AI agent capabilities. An 'Active Memory' plugin in chatbot systems is designed to automatically manage and retrieve relevant past information (context, preferences) within a conversation, reducing the need for users to explicitly reference history. MLX is an array framework for machine learning on Apple Silicon, and projects like 'mlx-audio' build upon it to provide fast, local text-to-speech and speech-to-text functionalities on macOS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://www.memoryplugin.com/">Memoryplugin</a></li>
<li><a href="https://mlx-framework.org/">MLX</a></li>

</ul>
</details>

**Tags**: `#AI-assistants`, `#memory-management`, `#open-source`, `#chat-systems`, `#speech-synthesis`

---

<a id="item-5"></a>
## [Advanced Mac Substitute Reimplements 1980s Mac OS APIs](https://www.v68k.org/advanced-mac-substitute/) ⭐️ 7.0/10

The Advanced Mac Substitute project has developed an API-level reimplementation of 1980s-era Mac OS, enabling classic 68K Mac applications to run on modern systems without requiring Apple ROM or original system software. This is significant for retro computing and software preservation, as it allows legacy Mac apps to run natively on contemporary hardware without emulated ROMs, contributing to API compatibility research. It supports 68K Mac applications up to Mac OS 6 and operates without proprietary Apple ROMs, which are typically required in other emulators like Basilisk II.

hackernews · zdw · Apr 11, 15:39

**Background**: In classic Macintosh systems from the 1980s, the operating system relied on ROM for core functions, with API calls often redirecting to this hardware. Traditional emulators require original Apple ROMs to run software, but Advanced Mac Substitute reimplements these APIs at the software level. This approach mimics the original OS behavior without copying its code, enabling compatibility without legal or technical dependencies on obsolete components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.v68k.org/advanced-mac-substitute/">Advanced Mac Substitute</a></li>
<li><a href="https://arstechnica.com/information-technology/2019/01/emulator-project-aims-to-resurrect-classic-mac-apps-and-games-without-the-os/">Emulator project aims to resurrect classic Mac apps... - Ars Technica</a></li>

</ul>
</details>

**Discussion**: Community comments show positive sentiment, with users appreciating the technical effort and discussing comparisons to other emulators like Basilisk II and Executor. Some express nostalgia for original hardware, while others see practical benefits for preserving and running classic software on modern systems.

**Tags**: `#retro-computing`, `#emulation`, `#operating-systems`, `#mac-os`, `#api-compatibility`

---

<a id="item-6"></a>
## [OpenAI acquires Cirrus Labs, shutting down Cirrus CI by June 2026.](https://cirruslabs.org/) ⭐️ 7.0/10

OpenAI has acquired Cirrus Labs in a talent-focused deal, leading to the scheduled shutdown of the Cirrus CI service on June 1, 2026. This acquisition disrupts the CI/CD ecosystem, forcing users of Cirrus CI to migrate and highlighting a trend where AI companies prioritize talent acquisition over product integration, potentially affecting open-source projects. Cirrus CI is a modern continuous integration system that supports Linux, Windows, macOS, FreeBSD, and cloud services like Kubernetes, AWS, and Azure, and it will remain operational until the shutdown date.

hackernews · seekdeep · Apr 11, 13:01

**Background**: Continuous Integration (CI) is a software development practice that automates testing and integration of code changes. Cirrus CI is a tool that facilitates this process across various computing environments. OpenAI is an AI research company known for advancements like ChatGPT, and this acquisition aims to integrate Cirrus Labs' engineering talent into OpenAI's projects.

<details><summary>References</summary>
<ul>
<li><a href="https://cirrus-ci.org/">Cirrus CI - Cirrus CI</a></li>

</ul>
</details>

**Discussion**: The community discussion emphasizes that this is a talent acquisition leading to product shutdown, with concerns raised about its impact on major open-source projects like SciPy and PostgreSQL. Some users expressed sadness over losing a preferred CI tool, while others noted the trend of AI companies acquiring development talent, with mixed sentiments of congratulations to the founders and cynicism about the move.

**Tags**: `#CI/CD`, `#OpenAI`, `#Acquisition`, `#Open Source`, `#DevTools`

---

<a id="item-7"></a>
## [The Problem That Built an Industry](https://ajitem.com/blog/iron-core-part-1-the-problem-that-built-an-industry/) ⭐️ 7.0/10

The article presents a historical analysis of IBM's Transaction Processing Facility (TPF) and the SABRE reservation system, developed starting in the 1960s, which solved airline booking challenges and built the modern reservation industry. It contrasts TPF's design principles, such as having no daemons or background threads, with contemporary software architecture practices. This analysis is significant because it shows how legacy systems like TPF achieved high efficiency and reliability, processing tens of thousands of transactions per second with low latency, offering lessons for modern system design and cloud optimization in transaction-heavy industries. Notable details include TPF's specialized architecture for high-volume transaction processing without persistent connection state in memory, and its ability to handle over 50,000 transactions per second on cost-effective hardware, despite being considered non-modern by today's standards.

hackernews · ShaggyHotDog · Apr 11, 14:03

**Background**: Transaction Processing Facility (TPF) is an IBM mainframe operating system specialized for high-volume, low-latency transaction processing, such as in airline reservations. The SABRE system, developed by IBM for American Airlines in 1961, was a pioneering computerized reservation system that automated booking processes. TPF focuses on processing input and output messages on a 1:1 basis with minimal overhead, making it highly efficient for real-time transactions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transaction_Processing_Facility">Transaction Processing Facility - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/IBM">IBM - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments include debates on historical accuracy, such as correcting the timeline of the IBM-American Airlines partnership, and discussions on TPF's design efficiency versus modern architectural reviews. Additional viewpoints highlight programming language influences, like Lisp and Rust, and a request for an RSS feed to follow the site.

**Tags**: `#systems-design`, `#transaction-processing`, `#historical-computing`, `#software-architecture`

---

<a id="item-8"></a>
## [Show HN: Pardonned.com – A Searchable Database of US Presidential Pardons](https://news.ycombinator.com/item?id=47727960) ⭐️ 6.0/10

A new website, Pardonned.com, was launched to provide a searchable database of US presidential pardons, built by scraping the Department of Justice website with Playwright, storing data in SQLite, and generating a static site using Astro. All code is open source and available on GitHub. This matters because it democratizes access to US presidential pardon data, enabling easier verification of claims and fostering transparency in the legal system. It serves as a valuable civic tech tool for journalists, researchers, and the public to analyze pardons and understand trends. Key technical details include using Playwright for web scraping the DOJ website, SQLite for local data storage, and Astro 6 for static site generation. However, as a static site, it might not reflect real-time updates to the source data without manual re-scraping.

hackernews · vidluther · Apr 11, 06:19

**Background**: US presidential pardons are official acts where the president forgives federal crimes, with records maintained by the Department of Justice (DOJ). Playwright is a web scraping tool that automates browsers to extract data from websites, SQLite is a lightweight database for local storage, and Astro is a static site generator that builds fast, pre-rendered websites from data.

<details><summary>References</summary>
<ul>
<li><a href="https://oxylabs.io/blog/playwright-web-scraping">Playwright Web Scraping Tutorial for 2026</a></li>
<li><a href="https://sqlite.org/quickstart.html">SQLite In 5 Minutes Or Less</a></li>
<li><a href="https://astro.build/">Astro</a></li>

</ul>
</details>

**Discussion**: The community discussion shows positive engagement, with users sharing raw data extracts, suggesting enhancements like offense type analysis, and debating the constitutional power of presidential pardons. Some users pointed out a spelling error ('pardoned' vs. 'pardonned') in the site's name.

**Tags**: `#web-scraping`, `#open-data`, `#legal-tech`, `#civic-tech`

---