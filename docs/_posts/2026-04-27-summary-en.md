---
layout: default
title: "Horizon Summary: 2026-04-27 (EN)"
date: 2026-04-27
lang: en
---

> From 22 items, 7 important content pieces were selected

---

1. [Fast16 Malware Predates Stuxnet by Five Years](#item-1) ⭐️ 8.0/10
2. [AI Should Elevate Thinking, Not Replace It](#item-2) ⭐️ 8.0/10
3. [OpenAI stops using SWE-bench Verified due to saturation](#item-3) ⭐️ 8.0/10
4. [OpenClaw v2026.4.25-beta.2: TTS, plugins, OpenTelemetry upgrades](#item-4) ⭐️ 7.0/10
5. [Developer Buys Friendster Domain for $30k, Builds Hyperlocal Social App](#item-5) ⭐️ 6.0/10
6. [Clay PCB Tutorial Sparks Debate on Sustainable Electronics](#item-6) ⭐️ 6.0/10
7. [Visual Tool Reveals Zork 1 Z-Machine Internals](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Fast16 Malware Predates Stuxnet by Five Years](https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/) ⭐️ 8.0/10

SentinelOne researchers have discovered a sophisticated Lua-based malware framework from 2005 named 'Fast16' that precisely sabotaged engineering software calculations. This finding reveals high-precision software sabotage techniques five years before the emergence of the Stuxnet worm. The discovery reshapes our understanding of early cyber sabotage, proving that advanced, precision-targeting malware existed long before Stuxnet. It underscores the evolving toolkit of state-sponsored attackers and highlights the use of scripting languages like Lua for clandestine operations. The malware uses Lua scripting to implement complex mathematical transformations that alter critical calculation results in engineering software, potentially affecting simulations for nuclear reactors and other sensitive systems. The malware was identified through analysis of historical samples and references from the Shadow Brokers leak.

hackernews · dd23 · Apr 26, 20:18

**Background**: Stuxnet, discovered in 2010, was a landmark cyber weapon designed to physically damage Iranian nuclear centrifuges by altering their operation. It demonstrated the potential of malware to cause real-world destruction. The Fast16 malware, from 2005, shows that similar capabilities were being developed years earlier, using different technical approaches such as embedded Lua scripts. This finding provides new context for the evolution of cyber warfare tactics.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/04/researchers-uncover-pre-stuxnet-fast16.html">Researchers Uncover Pre-Stuxnet ‘ fast 16 ’ Malware Targeting...</a></li>
<li><a href="https://delimiter.online/blog/fast16-malware/">Researchers Uncover 2005 Malware That Preceded... - Delimiter Online</a></li>

</ul>
</details>

**Discussion**: Comments on the report express excitement about the historical find, with some users highlighting the unusual use of SCCS/RCS version control comments in 2005 Windows kernel code, which suggests a background in government or military computing. Others are curious about the specific targets and the exact nature of the calculation modifications. A user also provided a download link for the malware sample for further analysis.

**Tags**: `#cybersecurity`, `#malware`, `#Stuxnet`, `#history`, `#software sabotage`

---

<a id="item-2"></a>
## [AI Should Elevate Thinking, Not Replace It](https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/) ⭐️ 8.0/10

A blog post by Koshy John argues that AI tools in software engineering should augment human reasoning and judgment, not substitute for them, sparking a vigorous debate on Hacker News. This discussion addresses a central tension in modern software engineering: the risk that reliance on AI-generated code may erode engineers' deep understanding and ownership of their work, potentially harming long-term code quality and intellectual rigor. The post emphasizes that there is no shortcut to judgment and that mastery cannot be transferred via generated explanations without active effort; the Hacker News thread (270 points, 221 comments) includes comparisons to past tool dependencies like IDEs and package managers.

hackernews · koshyjohn · Apr 26, 20:03

**Background**: As AI coding assistants like GitHub Copilot and ChatGPT become widespread, there is growing concern among engineers that over-reliance on these tools may lead to a 'use it or lose it' effect on critical thinking and problem-solving skills. The blog post joins a longstanding philosophical debate about the role of technology in human cognition, echoing concerns from earlier eras about calculators and spell-checkers.

**Discussion**: Commenters expressed a range of views: some likened AI assistance to past tool shifts (e.g., from assembly to high-level languages), arguing it is a natural evolution; others warned of a genuine risk of skill atrophy, citing rising evidence from studies. A key distinction was drawn between using AI to write code one still owns and understands versus treating it as an opaque abstraction layer.

**Tags**: `#AI`, `#philosophy of technology`, `#software engineering`, `#critical thinking`, `#productivity`

---

<a id="item-3"></a>
## [OpenAI stops using SWE-bench Verified due to saturation](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) ⭐️ 8.0/10

OpenAI announced that it will no longer evaluate models using the SWE-bench Verified benchmark, because the top score has reached 93.9%, indicating the benchmark is saturated. This decision highlights the growing problem of benchmark saturation in AI coding evaluation, where models quickly top out, reducing the benchmark's ability to differentiate capabilities. It underscores the urgent need for novel, harder evaluation methods to track real progress in code generation. The saturated score of 93.9% was achieved by Anthropic's model, and OpenAI notes that any remaining room for improvement below that threshold is limited. SWE-bench Verified is a human-verified subset of 500 instances from the original SWE-bench, originally created in collaboration with OpenAI.

hackernews · kmdupree · Apr 26, 13:58

**Background**: SWE-bench is a benchmark that evaluates large language models on solving real-world GitHub issues by generating code patches. Each task runs in an isolated Docker container, and models must produce a correct patch. SWE-bench Verified is a human-filtered subset designed to reduce noise and ambiguity. Benchmarks like this are crucial for measuring coding AI progress, but they often become saturated as models improve and train on overlapping data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.swebench.com/verified.html">SWE - bench Verified</a></li>
<li><a href="https://openai.com/index/introducing-swe-bench-verified/">Introducing SWE - bench Verified | OpenAI</a></li>
<li><a href="https://www.vals.ai/benchmarks/swebench">SWE-bench</a></li>

</ul>
</details>

**Discussion**: SWE-bench co-creator Ofir Press acknowledged the saturation, noted that upcoming benchmarks like SWE-bench Multilingual and Multimodal remain unsaturated, and reminded that all benchmarks eventually saturate. Other commenters raised concerns about benchmark gaming, the short gap between training data cutoff and public release, and the difficulty of creating novel, uncontaminated benchmarks.

**Tags**: `#AI benchmarks`, `#coding AI`, `#SWE-bench`, `#benchmark saturation`, `#machine learning evaluation`

---

<a id="item-4"></a>
## [OpenClaw v2026.4.25-beta.2: TTS, plugins, OpenTelemetry upgrades](https://github.com/openclaw/openclaw/releases/tag/v2026.4.25-beta.2) ⭐️ 7.0/10

OpenClaw v2026.4.25-beta.2 introduces major upgrades including multi-provider TTS support, migration of plugin registry to cold storage, expanded OpenTelemetry observability, and improved browser automation. These enhancements make OpenClaw more versatile for voice interactions, more reliable for plugin management, and more observable for debugging, benefiting developers and users relying on this open-source automation platform. New TTS providers include Azure Speech, Xiaomi, Local CLI, Inworld, Volcengine, and ElevenLabs v3. The plugin registry now uses cold persisted storage to reduce scan overhead and improve determinism. OpenTelemetry coverage spans model calls, token usage, tool loops, and memory pressure.

github · steipete · Apr 26, 12:23

**Background**: OpenClaw is an open-source automation tool supporting browser automation, text-to-speech (TTS), plugins, and observability. OpenTelemetry is a vendor-neutral observability framework for cloud-native software, hosted under the CNCF. The Chrome DevTools Protocol (CDP) enables remote debugging of Chromium-based browsers. Cold storage in the plugin registry refers to persisting data to disk for deterministic and efficient access.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenTelemetry">OpenTelemetry</a></li>
<li><a href="https://opentelemetry.io/">OpenTelemetry</a></li>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#plugins`, `#OpenTelemetry`, `#browser automation`, `#open source`

---

<a id="item-5"></a>
## [Developer Buys Friendster Domain for $30k, Builds Hyperlocal Social App](https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d) ⭐️ 6.0/10

A developer purchased the Friendster.com domain for $30,000 in Bitcoin and a revenue-generating domain, and is now building a hyperlocal social networking app. The app was rejected by Apple's App Store for lacking broad appeal, prompting exploration of Progressive Web App (PWA) and Nostr protocol alternatives. This story highlights the challenges of building niche social apps under centralized app store policies, and the potential shift toward decentralized, cross-platform alternatives like PWAs and Nostr. It also reflects the enduring value of nostalgic internet assets and how they can be repurposed for modern needs. The developer paid $20,000 in Bitcoin plus a domain generating $9,000/year in ad revenue to acquire Friendster.com. He is now considering a QR-code-based PWA to bypass App Store restrictions, and building social features on the Nostr decentralized protocol for censorship resistance and user control.

hackernews · ca98am79 · Apr 26, 20:41

**Background**: Friendster was one of the earliest social networking platforms, launched in 2002, which failed to compete with MySpace and Facebook and eventually shut down. Nostr (Notes and Other Stuff Transmitted by Relays) is an open, decentralized protocol for social networking that uses cryptographic keys and relays to enable censorship-resistant communication. Progressive Web Apps (PWAs) are web applications that can be installed on devices like native apps, running across platforms without needing separate App Store distribution. These technologies offer alternatives to traditional centralized app ecosystems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noster_(protocol)">Noster (protocol)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Progressive_web_app">Progressive web app</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong frustration with Apple's App Store guidelines, arguing that platform owners should not dictate app functionality for niche audiences. Several suggested technical alternatives: one recommended building a QR-code-based PWA on top of the Nostr protocol to reduce costs and increase accessibility, while another shared their own similar hyperlocal gaming project. The discussion also highlighted the unique domain purchase deal involving Bitcoin and revenue-generating domains.

**Tags**: `#domain acquisition`, `#social networking`, `#app store review`, `#progressive web app`, `#decentralized protocols`

---

<a id="item-6"></a>
## [Clay PCB Tutorial Sparks Debate on Sustainable Electronics](https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial) ⭐️ 6.0/10

A tutorial on creating printed circuit boards (PCBs) using wild clay and urban-mined silver, fired in a bonfire, has been published by feministhackerspaces, demonstrating a low-tech, sustainable alternative to conventional PCB fabrication. This project challenges the conventional PCB industry, which relies on conflict minerals and energy-intensive processes, and encourages rethinking hardware production through feminist hacking and artistic methodologies. It highlights the potential for more accessible, small-scale electronics manufacturing. The conductive tracks are made from urban-mined silver, and all components are reused from old electronic devices. The microcontroller used is fully open source, and the final PCB is fired in a campfire-like setting.

hackernews · j0r0b0 · Apr 26, 16:02

**Background**: Printed circuit boards (PCBs) are typically made from fiberglass laminates with copper traces, produced through chemical etching or milling. The clay PCB method replaces these materials with wild clay and conductive silver paste, and uses a bonfire for firing. This approach is part of a broader exploration of alternative, sustainable electronics fabrication, often associated with hacker culture and critical making.

<details><summary>References</summary>
<ul>
<li><a href="https://feministhackerspaces.cargo.site/Clay-PCB-Tutorial">Clay PCB Tutorial — feministhackerspaces</a></li>
<li><a href="https://radical-openness.org/en/programm/2024/clay-pcb">Clay PCB | Art Meets Radical Openness</a></li>
<li><a href="https://media.ccc.de/v/38c3-clay-pcb">Clay PCB - media.ccc.de</a></li>

</ul>
</details>

**Discussion**: Participants shared positive hands-on experiences, with one noting the fun of using clays from Austrian forests. Commentators also debated sustainability: some questioned whether an open fire emits more than 3D printing, while others suggested that for simple circuits, avoiding a PCB altogether might be more sustainable. References were made to earlier work like MIT's 'kit-of-no-parts' project.

**Tags**: `#PCB`, `#alternative manufacturing`, `#sustainability`, `#hacker culture`, `#clay`

---

<a id="item-7"></a>
## [Visual Tool Reveals Zork 1 Z-Machine Internals](https://eblong.com/infocom/visi/zork1/) ⭐️ 6.0/10

A new visualization tool called The Visible Zorker allows users to inspect the internal workings of the Z-machine while running Zork 1, without needing a debugger. This tool makes the inner mechanics of classic interactive fiction accessible to retro computing enthusiasts and developers, helping them understand how early text adventures like Zork operate under the hood. The visualization displays Z-machine memory, stack, and program state in a browser, enabling step-by-step inspection of the game's execution without modifying the original Zork 1 code.

hackernews · PLenz · Apr 26, 16:42

**Background**: The Z-machine is a virtual machine developed by Infocom in the late 1970s and early 1980s specifically for running interactive fiction games like Zork. It abstracts game logic into a portable bytecode format, allowing the same game to run on different platforms. The Visible Zorker takes advantage of this abstraction to provide a live, graphical view of the virtual machine's internal state.

<details><summary>References</summary>
<ul>
<li><a href="https://forums.crackberry.com/blackberry-os-apps-f35/wanted-polished-interactive-fiction-interpreter-65086/">Wanted: Polished Interactive Fiction Interpreter - BlackBerry Forums...</a></li>
<li><a href="https://arstechnica.com/gaming/2024/06/from-infocom-to-80-days-an-oral-history-of-text-games-and-interactive-fiction/">From Infocom to 80 Days: An oral history of text games and interactive ...</a></li>

</ul>
</details>

**Discussion**: Community members find the tool neat for examining Z-machine internals without a debugger. One user asked whether Inform 6 is still a suitable language for developing modern text-based games, while another user noted difficulty navigating because moving west then east could lead to a different location, expressing curiosity about Z-machine behavior.

**Tags**: `#Z-machine`, `#Zork`, `#interactive fiction`, `#retro computing`, `#visualization`

---