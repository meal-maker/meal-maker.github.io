---
layout: default
title: "Horizon Summary: 2026-05-25 (EN)"
date: 2026-05-25
lang: en
---

> From 21 items, 7 important content pieces were selected

---

1. [Memory now accounts for ~2/3 of AI chip component costs](#item-1) ⭐️ 8.0/10
2. [Constraint Decay: LLM Agents Fail at Structured Backend Code](#item-2) ⭐️ 8.0/10
3. [Scammers abuse internal Microsoft account to send spam](#item-3) ⭐️ 8.0/10
4. [Audiomass: Free Open-Source Web Multitrack Audio Editor](#item-4) ⭐️ 7.0/10
5. [DeepSeek Reasonix: A Native Coding Agent with High Caching](#item-5) ⭐️ 7.0/10
6. [Microsoft open-sources earliest known DOS source code](#item-6) ⭐️ 7.0/10
7. [Mastering Dyalog APL Now Available as Jupyter Notebook](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Memory now accounts for ~2/3 of AI chip component costs](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

According to an Epoch AI data insight, memory (especially High Bandwidth Memory, HBM) now accounts for nearly two-thirds of the total component cost of AI chips, driven by surging demand for AI training and inference. This cost structure reveals a critical bottleneck in AI hardware; if DRAM manufacturing capacity catches up with demand, AI hardware costs could drop by roughly 3x without any new technical breakthroughs, making AI more affordable. HBM is a specialized 3D-stacked memory technology that provides extremely high bandwidth for AI accelerators, but its complex fabrication process makes it much more expensive to produce than standard DDR5 memory.

hackernews · intelkishan · May 24, 16:31

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked synchronous DRAM interface developed by Samsung, AMD, and SK Hynix, offering a 1024-bit wide access path and bandwidth up to 256 GB/s per package. Unlike conventional DDR memory used in consumer PCs, HBM requires specialized fabrication processes, making it significantly harder and more costly to produce. The recent explosive growth of AI workloads has created an insatiable demand for HBM, straining global DRAM supply and driving up prices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://medium.com/@tanmaysorte25/the-hbm-vs-ddr5-tug-of-war-why-ai-is-stealing-your-pcs-performance-f4a683c7fd3f">The HBM vs. DDR5 Tug-of-War: Why AI is Stealing Your... | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters observe that RAM prices have soared—one user notes 96 GB of RAM that cost $250 a few years ago now costs $1,200. There is a sense that while AI demand is insatiable, DRAM supply growth at 20-25% per year may be insufficient, leading to a prolonged cost crunch for both AI hardware and consumer electronics like PCs and phones.

**Tags**: `#AI hardware`, `#memory costs`, `#DRAM`, `#chip economics`, `#HBM`

---

<a id="item-2"></a>
## [Constraint Decay: LLM Agents Fail at Structured Backend Code](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

A new study introduces the phenomenon of 'constraint decay,' where LLM-based coding agents perform significantly worse when forced to follow explicit architectural rules, with assertion pass rates dropping by approximately 30 percentage points on multi-file backend generation tasks. This finding exposes a critical limitation of current LLM agents: they are reliable for rapid prototyping but unreliable for production-grade backend development, which has significant implications for practitioners relying on AI-assisted coding in real-world projects. The study systematically evaluated LLM agents on multi-file backend generation under accumulating constraints (architectural, ORM, framework) and found performance drops concentrated on convention-heavy frameworks. The study did not fully test frontier models due to cost, so the specific performance numbers may not represent the absolute state-of-the-art.

hackernews · wek · May 24, 12:55

**Background**: Large language model (LLM) agents are increasingly used for code generation, especially for backend development that involves multiple files and strict architectural patterns. 'Constraint decay' refers to the tendency of these agents to produce fewer correct assertions or tests as the number of explicit constraints increases. This is different from unconstrained generation where they excel. The study used a benchmark of multi-file backend generation tasks with added structural rules.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.06445">Constraint decay : The Fragility of LLM Agents in Backend Code...</a></li>
<li><a href="https://agentpatterns.ai/verification/constraint-decay-backend-agents/">Constraint Decay in Backend Code Generation - AgentPatterns.ai</a></li>

</ul>
</details>

**Discussion**: Commenters largely confirm the phenomenon from personal experience, with one user noting they have to add more constraints in complex projects. Another commenter critiques the study for not testing frontier models due to cost, questioning the generality of the findings. A third user mentions building a plugin with a status machine to monitor LLM activities to avoid constraint decay.

**Tags**: `#LLM agents`, `#code generation`, `#backend development`, `#software engineering`, `#AI reliability`

---

<a id="item-3"></a>
## [Scammers abuse internal Microsoft account to send spam](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 8.0/10

For months, scammers have been exploiting the internal Microsoft account msonlineservicesteam@microsoftonline.com to send spammy emails, taking advantage of a loophole in Microsoft's system. This incident undermines trust in Microsoft's email security and authentication, showing that even internal accounts can be abused, and highlights broader issues with domain management that affect both consumers and enterprises. The abused address is normally reserved for legitimate account notifications and security alerts, but the exact mechanism of abuse remains unclear, pointing to a failure in Microsoft's internal email authentication controls.

hackernews · spike021 · May 24, 00:51

**Background**: Email authentication relies on standards like SPF, DKIM, and DMARC to verify that emails come from legitimate senders. Internal Microsoft accounts like msonlineservicesteam@microsoftonline.com should be protected by strict controls to prevent spoofing or abuse. The current incident suggests those controls are insufficient, echoing longstanding criticisms of Microsoft's tangled domain portfolio and inconsistent security practices.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account ... | TechCrunch</a></li>
<li><a href="https://techplanet.today/post/microsofts-internal-account-abuse-a-critical-security-failure-that-undermines-user-trust">Microsoft 's Internal Account Abuse : A Critical Security... | TechPlanet</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Microsoft's domain management, noting that even internal domains like microsoftonline.com are difficult to verify. Others shared related complaints about empty login history and unwarranted authenticator notifications, while some pointed out phishing risks due to similar-looking domain names.

**Tags**: `#security`, `#microsoft`, `#phishing`, `#spam`, `#domain`

---

<a id="item-4"></a>
## [Audiomass: Free Open-Source Web Multitrack Audio Editor](https://audiomass.co/?multitrack=1) ⭐️ 7.0/10

Audiomass, a free and open-source multitrack audio editor that runs entirely in the web browser, was launched on Hacker News and gained 156 points with 40 comments. This provides a high-quality, accessible alternative to desktop audio editors like Audacity, enabling anyone with a browser to edit multiple audio tracks without installation, which is especially valuable for users on restricted devices or for quick collaborative workflows. The editor supports importing FLAC files out of the box, a feature appreciated by users, and the codebase uses older JavaScript patterns (safety closures, var declarations) that some developers find nostalgic.

hackernews · pantelisk · May 24, 15:25

**Background**: Multitrack audio editors allow users to layer and edit multiple audio clips simultaneously, a common need in music production and podcasting. Desktop tools like Audacity are popular but require installation and are not inherently collaborative. Web-based editors eliminate these barriers, though they have traditionally faced performance limitations.

**Discussion**: The Hacker News community reacted positively, with comments praising the app's design, FLAC support, and nostalgic code style. Users also suggested features like cloud-based track collaboration and support for tracker module formats (XM), indicating interest in extending the tool's capabilities.

**Tags**: `#open-source`, `#audio-editing`, `#web-app`, `#music-production`, `#hackernews`

---

<a id="item-5"></a>
## [DeepSeek Reasonix: A Native Coding Agent with High Caching](https://esengine.github.io/DeepSeek-Reasonix/) ⭐️ 7.0/10

The DeepSeek team announced Reasonix, a native coding agent that runs in the terminal and is designed to maximize API cache hits to reduce costs. By leveraging a cache-first loop, Reasonix could significantly lower the cost of using DeepSeek's API for coding tasks, making AI-assisted development more accessible. However, the mixed community reception highlights concerns about the tool's user experience and whether its caching strategy is truly optimal. Reasonix employs a 'cache-first loop' and 'flash-first cost control' to prioritize cached responses, and supports both local Ollama embeddings and DeepSeek-hosted embeddings. The tool is available via npm (npx) or a global installation from GitHub.

hackernews · Alifatisk · May 24, 13:02

**Background**: DeepSeek is an AI model provider known for cost-effective large language models. AI coding agents are tools that integrate with language model APIs to help developers write code. Caching in this context refers to reusing previous responses to avoid redundant API calls, thereby reducing latency and cost. Reasonix is built specifically for DeepSeek's API to take advantage of its caching infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://esengine.github.io/DeepSeek-Reasonix/">Reasonix — DeepSeek -native AI coding agent</a></li>
<li><a href="https://github.com/esengine/deepseek-reasonix">GitHub - esengine/ DeepSeek - Reasonix : DeepSeek -native AI coding...</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/agent_integrations/reasonix">Integrate with Reasonix | DeepSeek API Docs</a></li>

</ul>
</details>

**Discussion**: Community comments on Hacker News are mixed. Several users criticized the Reasonix website for poor mobile UX and an over-produced design that resembles AI-generated pages. Others questioned the assumption that always appending to the prefix for cache hits is optimal, noting that established harnesses sometimes break caching intentionally for better overall results. Some users expressed a preference for a single self-contained binary written in Rust or Go rather than a Node.js-based tool.

**Tags**: `#DeepSeek`, `#AI coding agent`, `#caching`, `#developer tools`, `#low cost`

---

<a id="item-6"></a>
## [Microsoft open-sources earliest known DOS source code](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 7.0/10

Microsoft has open-sourced what is believed to be the earliest known version of the DOS source code, painstakingly recovered from paper printouts using OCR technology, alongside the source code for their early BASIC interpreter. This release offers an unprecedented window into the foundational software that launched the PC era, preserving a critical piece of computing history and allowing developers and historians to study the origins of Microsoft's operating system and developer tools business. The source code was recovered from decades-old paper printouts by the "DOS Disassembly Group," led by Yufeng Gao and Rich Cini, who used OCR that struggled with the deteriorated print quality. Microsoft also published the corresponding early BASIC source code as part of the same preservation effort.

hackernews · DamnInteresting · May 24, 01:21

**Background**: DOS (Disk Operating System) was the original operating system for the IBM PC, and Microsoft's BASIC interpreter was the company's primary product in the early days. At the time, Microsoft was mainly a developer tools company; the DOS contract with IBM was a stepping stone that helped establish the company. The source code for such early software was typically not preserved digitally, so the recovery from printouts is a significant archival achievement.

**Discussion**: Commenters expressed gratitude to Microsoft for the release, with many highlighting the historical value of the BASIC source code as equally important. There was nostalgia for the era when a few thousand lines of assembly could launch a successful company, while others wondered how long it would take for early Windows source code to be released.

**Tags**: `#history`, `#open-source`, `#DOS`, `#Microsoft`, `#retrocomputing`

---

<a id="item-7"></a>
## [Mastering Dyalog APL Now Available as Jupyter Notebook](https://mastering.dyalog.com/README.html) ⭐️ 6.0/10

The respected APL tutorial 'Mastering Dyalog APL' is now available as an interactive Jupyter notebook, enabling hands-on learning with executable code examples. This interactive format significantly lowers the entry barrier for learning APL's unique symbol-based syntax, potentially broadening the language's appeal among data scientists and programmers interested in array-oriented thinking. The notebook format allows learners to execute code in-browser, building muscle memory for APL's special symbols. The original PDF version remains available through Dyalog's website.

hackernews · tosh · May 24, 11:42

**Background**: APL (A Programming Language) was created in the 1960s by Kenneth E. Iverson and is built around multidimensional arrays as its core data structure. It uses a wide range of special graphic symbols to represent functions, enabling extremely concise code. Dyalog APL is a modern, proprietary implementation first released in 1983, and it remains the most widely used APL dialect today. Array programming languages like APL allow operations to be applied to entire arrays at once, which is highly efficient for scientific and data-intensive computing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dyalog_APL">Dyalog APL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Array_programming_language">Array programming language</a></li>
<li><a href="https://aplwiki.com/wiki/Dyalog_APL">Dyalog APL - APL Wiki</a></li>

</ul>
</details>

**Discussion**: Commenters generally praise the interactive notebook format, with one noting it helps build muscle memory for APL symbols. However, several users express concerns about Dyalog APL's proprietary enterprise licensing, contrasting it with open-source alternatives. A few share alternative learning resources like the 'Learn APL' tutorial and their own experiences translating APL to NumPy.

**Tags**: `#APL`, `#educational resource`, `#array programming`, `#Dyalog`

---