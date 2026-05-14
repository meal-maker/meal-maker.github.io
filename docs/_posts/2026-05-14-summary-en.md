---
layout: default
title: "Horizon Summary: 2026-05-14 (EN)"
date: 2026-05-14
lang: en
---

> From 23 items, 7 important content pieces were selected

---

1. [The Emacsification of Software](#item-1) ⭐️ 8.0/10
2. [Princeton ends 133-year unproctored exam tradition](#item-2) ⭐️ 8.0/10
3. [Twin brothers wipe 96 government databases after firing](#item-3) ⭐️ 8.0/10
4. [Needle: A 26M Model for Tool Calling Distilled from Gemini](#item-4) ⭐️ 8.0/10
5. [Guide to Free .city.state.us Locality Domains (2025)](#item-5) ⭐️ 7.0/10
6. [Linus Torvalds creates branch in GuitarPedal repo](#item-6) ⭐️ 6.0/10
7. [Claude Design Projects Inaccessible After Unsubscribing](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [The Emacsification of Software](https://sockpuppet.org/blog/2026/05/12/emacsification/) ⭐️ 8.0/10

This article argues that large language models (LLMs) have made building personal software easier than adopting existing prepackaged tools, leading to what the author calls 'Emacsification' — a future where everyone has their own custom software cocoon. This shift could fundamentally alter how software is produced and consumed, moving away from one-size-fits-all applications toward highly personalized, user-built tools, which has major implications for the software industry and for end-user empowerment. Notably, security researcher tptacek lists several software categories—including podcast apps, music players, and note-taking tools—where LLM-generated replacements now surpass 'good enough' quality for personal use. Hacker News moderator dang adds that software production is now so easy that everything becomes a '.emacs file,' meaning each individual has their own endlessly customizable software cocoon.

hackernews · rdslw · May 13, 07:06

**Background**: Emacs is a highly extensible and customizable text editor, often described as 'an OS within an editor,' because users can modify nearly every aspect of its behavior using its built-in language Emacs Lisp. The term 'Emacsification' draws an analogy: just as Emacs users tailor their editor into a unique personal environment, today’s developers and power users are beginning to craft custom software for their own needs with the help of LLMs, rather than settling for off-the-shelf applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.w3tutorials.net/blog/differences-between-emacs-and-vim/">Emacs vs Vim: Practical Differences, Key Features... — w3tutorials.net</a></li>
<li><a href="https://operavps.com/blog/emacs-vs-vim/">Emacs vs Vim Comparison Guide for Power Users</a></li>

</ul>
</details>

**Discussion**: In the discussion, tptacek catalogs software categories (e.g., podcast apps, feed readers, chat clients) that LLMs can now produce at a usable quality, advocating that 'nerds should reclaim' these domains. dang strongly agrees, noting that software production has become trivial enough to create personal 'cocoons.' shaokind shares personal experience building such tools with LLMs but cautions that Emacs itself can be brittle across platforms. SoftTalker connects the trend to the original 1960s vision of personal computing, where everyone would write their own programs.

**Tags**: `#software development`, `#LLMs`, `#personal software`, `#Emacs`, `#AI-assisted programming`

---

<a id="item-2"></a>
## [Princeton ends 133-year unproctored exam tradition](https://www.dailyprincetonian.com/article/2026/05/princeton-news-adpol-proctoring-in-person-examinations-passed-faculty-133-years-precedent) ⭐️ 8.0/10

Princeton University voted to require proctoring for all in-person exams, reversing a 133-year-old honor code policy that allowed unsupervised testing. This policy shift at a prestigious institution signals how widely AI tools have eroded trust in academic integrity, forcing even the most tradition-bound honor systems to adapt. The change ends a policy that relied entirely on student honor and peer reporting; under the new system, faculty or proctors will supervise exams. The decision follows concerns about students using multimodal AI models like Gemini to cheat during tests.

hackernews · bookofjoe · May 13, 20:12

**Background**: Princeton had a historic honor code where undergraduates took exams without proctors, trusting students to neither cheat nor tolerate cheating. The code relied on a student-run committee to handle violations. With the rise of free, powerful AI tools that can answer exam questions in real time, faculty argued that the honor system was no longer tenable.

**Discussion**: Commenters expressed a range of views: some nostalgic for the old trust-based system, others arguing that society's declining trust, not just AI, is to blame. A student shared firsthand accounts of classmates using AI to photograph and answer exam questions, while another commenter from a different university was surprised that Princeton ever allowed unproctored exams.

**Tags**: `#academic integrity`, `#AI`, `#proctoring`, `#education policy`, `#trust`

---

<a id="item-3"></a>
## [Twin brothers wipe 96 government databases after firing](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/) ⭐️ 8.0/10

Two twin brothers, working as IT contractors for a company called Opexus, retaliated after being fired by using their active database access to execute 'DROP DATABASE' commands on 96 government databases, including one belonging to the Department of Homeland Security. This incident underscores the critical importance of immediately revoking access privileges upon termination, as a failure to do so enabled a massive insider threat attack that compromised sensitive government data and systems. According to the community discussion, the brother Sohaib was found with seven firearms and 370 rounds of .30 caliber ammunition during a search warrant execution, despite a prior criminal record that should have prohibited firearm possession. The attackers used the SQL command 'DROP DATABASE dhsproddb' and subsequently searched for how to clear system logs.

hackernews · jnord · May 12, 22:28

**Background**: Insider threats occur when current or former employees misuse their authorized access to harm an organization. In this case, the twins were IT contractors with database administration privileges. The 'DROP DATABASE' command permanently deletes an entire database, including all tables and data. The incident reveals failures in termination procedures—namely, that access was not revoked before or immediately after the firing, and that background checks may not have been thorough enough given one brother's criminal history.

**Discussion**: Community commenters expressed amusement and disbelief at the attackers' blatant actions, such as asking an AI how to clear logs immediately after dropping a database. Some criticized the hiring practices and questioned how non-U.S. citizens could access sensitive DHS systems. Another comment noted the irony that the brothers were apparently committing additional crimes (illegal firearm possession) while carrying out the database attack.

**Tags**: `#insider-threat`, `#cybersecurity`, `#database-security`, `#it-security`, `#incident-response`

---

<a id="item-4"></a>
## [Needle: A 26M Model for Tool Calling Distilled from Gemini](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus has open-sourced Needle, a 26M-parameter function-calling model distilled from Gemini, which achieves 6000 tokens/second prefill and 1200 tokens/second decode on consumer devices. This model demonstrates that massive models are overkill for tool calling—a retrieval-and-assembly task—and that a tiny, efficient model can run on edge devices like phones, watches, and glasses, making on-device agentic AI practical. Needle uses a simple attention network architecture with only attention and gating, completely removing MLP layers, and was pretrained on 200B tokens then post-trained on 2B tokens of synthesized function-calling data from 15 tool categories.

hackernews · HenryNdubuaku · May 12, 18:03

**Background**: Tool calling (or function calling) allows large language models to interact with external APIs and data sources by converting natural language into structured API calls. Model distillation transfers knowledge from a large, powerful teacher model (like Gemini) to a smaller student model, enabling efficient inference on resource-constrained devices. Most transformer-based LLMs include feed-forward layers (MLPs) for memorizing knowledge, but Cactus found that for tasks relying on external context (tool use, RAG), MLPs are unnecessary because the required facts are provided in the input.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.promptingguide.ai/applications/function_calling">Function Calling with LLMs | Prompt Engineering Guide</a></li>

</ul>
</details>

**Discussion**: Community comments were largely positive but raised several concerns. Some questioned whether Needle can handle complex, multi-tool scenarios beyond simple examples like weather queries, while others saw potential in using it for command-line natural language interfaces. A notable concern was about Google's proactive defenses against distillation, which could have degraded the model's performance if detected. A discussant confirmed the finding that removing MLPs from Qwen preserved transformation tasks but lost knowledge, aligning with Needle's design.

**Tags**: `#tool calling`, `#model distillation`, `#edge AI`, `#small language models`, `#attention networks`

---

<a id="item-5"></a>
## [Guide to Free .city.state.us Locality Domains (2025)](https://fredchan.org/blog/locality-domains-guide/) ⭐️ 7.0/10

A comprehensive guide published in May 2025 explains how to register a free locality domain under the .us TLD, such as yourname.city.state.us, using an Interim .US Domain Template and a delegated locality manager. This guide makes a niche but valuable resource accessible to anyone wanting a short, geographically meaningful domain for free, while also surfacing real obstacles like notarized letters and defunct registrars that complicate the process. Registrants must locate a delegated locality, fill out the official Interim .US Domain Template, and send it to the locality's delegated manager; some managers require a notarized letter from the local government, and if the locality operator is defunct, registration may be impossible.

hackernews · speckx · May 13, 14:45

**Background**: The .us TLD includes a hierarchical namespace: state.us (e.g., ma.us), locality.state.us (e.g., boston.ma.us), and organization.locality.state.us. Locality domains are delegated to local entities (cities, counties, or approved ISPs) who can subdelegate names to residents or businesses. Though free in principle, the process varies widely because each locality sets its own rules and may charge fees or require documentation.

<details><summary>References</summary>
<ul>
<li><a href="https://fredchan.org/blog/locality-domains-guide/">Setting up a free *.city.state.us locality domain | Frederick's Perch</a></li>
<li><a href="https://en.wikipedia.org/wiki/.us">.us - Wikipedia</a></li>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/254/36/us-domain-registration-requirements/">.US domain registration requirements - Domains - Namecheap.com</a></li>

</ul>
</details>

**Discussion**: Commenters shared real-world struggles: one user spent 18 months tracking down a widow of a defunct registrar, while another found that Boston city government had no notary available for the required letter. Several people noted that .us domains forbid WHOIS privacy, which is a privacy concern for personal use.

**Tags**: `#domain registration`, `#.us TLD`, `#locality domains`, `#DNS`, `#practical guide`

---

<a id="item-6"></a>
## [Linus Torvalds creates branch in GuitarPedal repo](https://github.com/torvalds/GuitarPedal) ⭐️ 6.0/10

Linus Torvalds has created a new branch in his personal GuitarPedal repository on GitHub, indicating he is actively learning analog circuit design. While this is a minor personal project, it highlights Linus Torvalds' curiosity beyond software, which could inspire the open-source community to explore hardware and analog electronics. The repository is named GuitarPedal, and the branch creation suggests he is experimenting with circuit modifications or learning exercises.

github · torvalds · May 13, 22:43

**Background**: Linus Torvalds is the creator of the Linux kernel and Git. Analog circuits are electronic circuits that process continuous signals, often used in audio equipment like guitar pedals to modify sound. This project shows Torvalds exploring a domain outside his usual software expertise.

**Tags**: `#linus-torvalds`, `#open-source`, `#hardware`, `#analog-circuits`, `#personal-project`

---

<a id="item-7"></a>
## [Claude Design Projects Inaccessible After Unsubscribing](https://news.ycombinator.com/item?id=48128003) ⭐️ 6.0/10

A user reports that after unsubscribing from Claude Code Max, they lost access to all their Claude Design projects and credits, unlike other LLM apps where past sessions remain accessible. This incident highlights a critical data portability and ownership issue in subscription-based AI tools, where users may lose work when downgrading or canceling. It could affect trust in Anthropic's product ecosystem and influence how users back up their AI-generated work. The user also lost promotional credits that had a time limit, and resubscribing did not restore them. A community member noted that Claude Design chats can be exported via data export as JSON files, providing a workaround.

hackernews · pycassa · May 13, 21:40

**Background**: Claude Design is a research preview tool from Anthropic that allows creating code-powered prototypes using voice, video, shaders, and AI. It is available to Pro, Max, Team, and Enterprise plan subscribers. Claude Code Max is a higher-tier subscription that includes Claude Code for terminal-based coding workflows. Users experiencing billing issues or subscription changes may lose access to features if not properly handled by the system.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-design-anthropic-labs">Introducing Claude Design by Anthropic Labs</a></li>
<li><a href="https://support.claude.com/en/articles/11049741-what-is-the-max-plan">What is the Max plan? | Claude Help Center</a></li>

</ul>
</details>

**Discussion**: Community comments reveal mixed experiences: some users suggest using data export to recover projects, while others criticize Anthropic for prioritizing gimmicky features over bug fixes. One user had a positive experience with Claude Design and Claude Code integration. Overall sentiment is cautious, with advice to back up data regularly.

**Tags**: `#data access`, `#subscription trap`, `#AI design tools`, `#user experience`, `#data portability`

---