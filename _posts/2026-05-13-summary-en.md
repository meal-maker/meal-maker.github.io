---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 22 items, 10 important content pieces were selected

---

1. [Fork Restores Full BambuNetwork Support for Bambu Lab Printers](#item-1) ⭐️ 8.0/10
2. [CERT releases six serious CVEs for dnsmasq vulnerabilities](#item-2) ⭐️ 8.0/10
3. [Needle: 26M Parameter Tool-Calling Model Distilled from Gemini](#item-3) ⭐️ 8.0/10
4. [Why Senior Developers Struggle to Share Their Expertise](#item-4) ⭐️ 8.0/10
5. [Rendering the Sky, Sunsets, and Planets](#item-5) ⭐️ 8.0/10
6. [DuckDB Unveils Quack Client-Server Protocol](#item-6) ⭐️ 8.0/10
7. [Bambu Lab Criticized for Blocking Third-Party Access via User-Agent Checks](#item-7) ⭐️ 8.0/10
8. [Petition asks NYT, Atlantic, USA Today to unblock Wayback Machine](#item-8) ⭐️ 7.0/10
9. [Obsidian Unveils Automated Plugin Review System](#item-9) ⭐️ 7.0/10
10. [DeepMind reimagines mouse pointer with AI voice control](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Fork Restores Full BambuNetwork Support for Bambu Lab Printers](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

A fork of OrcaSlicer, maintained by the FULU Foundation, restores full BambuNetwork support for Bambu Lab printers, enabling cloud-based printing without requiring Bambu Studio or Bambu Connect. This fork reignites the debate over vendor lock-in in 3D printing, as it provides users an alternative to Bambu Lab's proprietary cloud authentication, challenging the company's control over printer connectivity and user data. The fork replicates the prior state of OrcaSlicer before Bambu Lab implemented two operating modes—cloud mode requiring Bambu Studio/Bambu Connect and LAN mode—restoring the original cloud-auth-less approach. Some community members have criticized the fork for squashing its Git history.

hackernews · Murfalo · May 12, 21:55

**Background**: OrcaSlicer is an open-source 3D printing slicer forked from Bambu Studio. Bambu Lab recently updated its firmware to enforce two modes: a default cloud mode that requires Bambu Studio or Bambu Connect for sending prints, and a LAN mode with reduced functionality. This change angered users who preferred open-source slicers like OrcaSlicer, leading to the creation of this fork that restores the original unrestricted cloud access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orcaslicer.com/">OrcaSlicer — Official Website & Downloads ( Orca Slicer )</a></li>
<li><a href="https://github.com/OrcaSlicer/OrcaSlicer">GitHub - OrcaSlicer / OrcaSlicer : G-code generator for 3D printers...</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some users appreciate the fork as a way to restore open access, while others criticize it for squashing Git history or question the desire for cloud-based printing. One commenter speculates that Bambu Lab may be seeking usage data or training models. User bri3d provides a technical explanation clarifying the fork's origins and the two-mode system.

**Tags**: `#3D printing`, `#open source`, `#vendor lock-in`, `#firmware`, `#controversy`

---

<a id="item-2"></a>
## [CERT releases six serious CVEs for dnsmasq vulnerabilities](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 8.0/10

CERT has disclosed six Common Vulnerabilities and Exposures (CVEs) for critical security flaws in dnsmasq, a widely-used DNS/DHCP server. These vulnerabilities were announced in a mailing list post on the dnsmasq-discuss list. dnsmasq is embedded in countless routers, IoT devices, and Linux distributions, making these vulnerabilities highly impactful. Remote attackers could crash the service or potentially execute arbitrary code, threatening network infrastructure. The six CVEs include a heap out-of-bounds write, an infinite loop causing denial of service, and other memory corruption issues triggered by malicious DNS or DHCP packets. Community comments note that Debian's stable version ships an outdated dnsmasq that may not receive timely fixes.

hackernews · chizhik-pyzhik · May 12, 18:12

**Background**: dnsmasq is a lightweight, easy-to-configure DNS forwarder and DHCP server designed for small networks, commonly used in home routers and embedded systems. A CVE (Common Vulnerabilities and Exposures) is a standardized identifier for publicly known security vulnerabilities, helping organizations track and prioritize fixes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">dnsmasq - Wikipedia</a></li>
<li><a href="https://wiki.debian.org/dnsmasq">dnsmasq - Debian Wiki</a></li>
<li><a href="https://www.redhat.com/en/topics/security/what-is-cve">What is a CVE?</a></li>

</ul>
</details>

**Discussion**: Community reactions include calls for rewriting dnsmasq in memory-safe languages like Rust or Go, criticism of Debian's slow update practices, and promotions of alternative DNS servers such as MaraDNS. Some users note that OpenWRT is working on an updated build, while others express concern over the severity of the heap out-of-bounds write.

**Tags**: `#dnsmasq`, `#security`, `#CVE`, `#vulnerability`, `#DNS`

---

<a id="item-3"></a>
## [Needle: 26M Parameter Tool-Calling Model Distilled from Gemini](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus has open-sourced Needle, a 26 million parameter model for function calling that uses only cross-attention and gating mechanisms with no MLP layers, achieving 6000 tokens/second prefill and 1200 tokens/second decode on consumer devices. This demonstrates that large language models are overkill for tool-calling tasks, which the authors argue are fundamentally retrieval-and-assembly rather than reasoning, and opens the door to running capable AI agents on budget phones, wearables, and other resource-constrained devices. The model was pretrained on 200 billion tokens and then post-trained on 2 billion tokens of synthesized function-calling data generated by Gemini across 15 tool categories. In single-shot function calling, it outperforms larger models like FunctionGemma-270M, Qwen-0.6B, Granite-350M, and LFM2.5-350M, though those models have broader capabilities for conversational settings.

hackernews · HenryNdubuaku · May 12, 18:03

**Background**: Tool calling (or function calling) is a capability that allows a language model to invoke external APIs or functions by outputting structured JSON arguments. Traditional transformer models include feed-forward networks (FFNs) that memorize factual knowledge, but Cactus found that for tool calling—which relies on external knowledge from tool definitions—FFN parameters are unnecessary. The model uses cross-attention to match user queries to tool names and arguments, and gating to control information flow, a design inspired by the observation that agentic tasks are retrieval-intensive rather than reasoning-intensive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/gated-cross-attention-mechanism">Gated Cross - Attention Mechanism</a></li>
<li><a href="https://www.distillabs.ai/blog/making-functiongemma-work-multi-turn-tool-calling-at-270m-parameters/">Making FunctionGemma Work: Multi-Turn Tool Calling at... — distil labs</a></li>
<li><a href="https://ollama.com/MFDoom/deepseek-r1-tool-calling:70b-llama-distill-fp16">MFDoom/deepseek-r1- tool - calling :70b-llama- distill -fp16</a></li>

</ul>
</details>

**Discussion**: Community comments raised questions about the model's discriminatory power in complex tool-use scenarios beyond simple examples like weather queries, and suggested potential applications such as command-line argument parsing. Another researcher confirmed independently that removing MLPs from a transformer model preserves transformation tasks but loses knowledge, aligning with Needle's design philosophy. There was also a suggestion to publish a live demo to make testing easier.

**Tags**: `#open-source`, `#tool-calling`, `#small-language-models`, `#on-device-ai`, `#attention-mechanism`

---

<a id="item-4"></a>
## [Why Senior Developers Struggle to Share Their Expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise) ⭐️ 8.0/10

The article identifies that senior developers often cannot clearly communicate their expertise because their knowledge is embedded in deeply integrated mental models, leading to communication gaps with less experienced colleagues. This issue affects team productivity, knowledge transfer, and mentorship in software engineering, potentially slowing down junior developers' growth and causing project misunderstandings. The article attributes the difficulty to the fact that experts rely on intuitive, non-verbal mental models rather than explicit rules, making it hard to break down their thought process into step-by-step explanations.

hackernews · nilirl · May 12, 15:08

**Background**: Expertise in complex fields like software engineering often becomes tacit over time, meaning practitioners operate with deep intuition that they cannot easily articulate. This phenomenon is well-documented in cognitive science and is a common challenge in mentoring and technical leadership.

**Discussion**: Commenters offered diverse viewpoints: one noted that expertise is embedded in an internal 'world model' that cannot be separated from the expert, while another criticized blanket statements about senior developers. Another commenter observed that many junior developers are simply not interested in mentorship, reducing opportunities for knowledge sharing.

**Tags**: `#software engineering`, `#communication`, `#expertise`, `#senior developer`, `#team dynamics`

---

<a id="item-5"></a>
## [Rendering the Sky, Sunsets, and Planets](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 8.0/10

Maxime Heckel published a detailed technical blog post explaining how to render realistic skies, sunsets, and planets using atmospheric scattering, complete with interactive WebGL demos and shader code. This post provides an accessible yet rigorous introduction to atmospheric rendering, a topic often considered complex, and its high community engagement highlights its value for aspiring and experienced graphics developers. The post implements real-time atmospheric scattering using GPU-friendly approximations, but commenters note that the sunset model incorrectly turns the sky black immediately after the sun dips below the horizon, ignoring twilight effects that persist until the sun is 18 degrees below the horizon.

hackernews · ibobev · May 12, 13:26

**Background**: Atmospheric scattering is the physical phenomenon responsible for sky colors, caused by sunlight interacting with air molecules (Rayleigh scattering) and aerosols (Mie scattering). Real-time rendering of these effects is challenging because it requires solving complex light transport equations; many techniques, such as the one described in the seminal 1993 paper by Nishita et al., rely on precomputation or GPU acceleration to achieve interactive frame rates.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/gpugems/gpugems2/part-ii-shading-lighting-and-shadows/chapter-16-accurate-atmospheric-scattering">Chapter 16. Accurate Atmospheric Scattering | NVIDIA Developer</a></li>
<li><a href="http://vterrain.org/Atmosphere/">Sky / Atmospheric Rendering</a></li>

</ul>
</details>

**Discussion**: Community response is overwhelmingly positive, with many praising the writeup's clarity and interactivity. Several commenters provide constructive feedback, notably that the sunset model lacks twilight rendering, and others share related resources such as Sebastian Lague's video and the original Nishita et al. paper.

**Tags**: `#graphics programming`, `#atmospheric rendering`, `#shaders`, `#computer graphics`, `#technical blog`

---

<a id="item-6"></a>
## [DuckDB Unveils Quack Client-Server Protocol](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB announced the Quack remote protocol, allowing DuckDB instances to communicate in a client-server setup with support for multiple concurrent writers. This solves a major limitation of DuckDB as an embedded database by enabling horizontal scaling and remote query execution, making it viable for multi-user server deployments. Quack is designed to be simple to set up and builds on proven technologies. It supports multiple concurrent writers, a key feature for server-side use.

hackernews · aduffy · May 12, 17:54

**Background**: DuckDB is an embedded database management system that traditionally runs within a host process, lacking a built-in client-server model. This made horizontal scaling challenging for multi-user scenarios. The Quack protocol introduces a remote communication layer, enabling client-server architecture while maintaining DuckDB's simplicity.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack: The DuckDB Client-Server Protocol – DuckDB</a></li>
<li><a href="https://news.ycombinator.com/item?id=48111765">Quack: The DuckDB Client-Server Protocol | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly positive, with users excited about practical use cases such as scaling internal apps, building columnar spreadsheet tools, and setting up shared analytics servers. Some users note that DuckDB's evolving feature set can make it unclear which usage pattern is best, but overall enthusiasm is high.

**Tags**: `#duckdb`, `#database`, `#protocol`, `#scalability`, `#embedded-database`

---

<a id="item-7"></a>
## [Bambu Lab Criticized for Blocking Third-Party Access via User-Agent Checks](https://www.jeffgeerling.com/blog/2026/bambu-lab-abusing-open-source-social-contract/) ⭐️ 8.0/10

Bambu Lab is facing backlash for implementing user-agent header checks that block third-party tools and clients from accessing its 3D printers, effectively restricting interoperability and violating the open source social contract. This controversy highlights a growing tension between closed ecosystems and open source principles in the 3D printing community, where user trust and hardware freedom are at stake. If companies can unilaterally restrict access via weak technical measures, it undermines the foundation of open source hardware and software collaboration. Bambu Lab claimed the user-agent checks were necessary to prevent service outages from unauthorized traffic, but critics argue that relying on client-supplied metadata like user-agent strings is not a security mechanism and that scaling infrastructure would be a proper solution.

hackernews · rubenbe · May 12, 14:54

**Background**: In HTTP communication, the User-Agent header identifies the client software making a request, but it can be easily spoofed or changed by any client. Relying on user-agent strings for access control is therefore not a security measure but rather a weak barrier that can be bypassed, leading to mistrust from the community when used to block legitimate third-party tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/User_agent_spoofing">User agent spoofing</a></li>
<li><a href="https://cheq.ai/blog/user-agent-spoofing/">User Agent Spoofing: What Is It & Why Does It Matter? - CHEQ</a></li>

</ul>
</details>

**Discussion**: Commenters were largely critical of Bambu Lab's justifications, calling the user-agent excuse flimsy and noting that the company has a history of backtracking under pressure, such as when it initially omitted LAN mode. Some also raised geopolitical concerns about data routing through China and the use of Bambu printers in the Ukrainian war effort, though these claims remain unverified.

**Tags**: `#3D printing`, `#open source`, `#hardware`, `#community`, `#controversy`

---

<a id="item-8"></a>
## [Petition asks NYT, Atlantic, USA Today to unblock Wayback Machine](https://www.savethearchive.com/newsleaders/) ⭐️ 7.0/10

A petition at savethearchive.com urges The New York Times, The Atlantic, and USA Today to stop blocking the Internet Archive's Wayback Machine from archiving their content, citing concerns over digital preservation. This highlights the growing tension between paywalls that protect news revenue and the public interest in preserving access to historical information, directly affecting researchers, historians, and the general public. The blocking is reportedly enforced by these sites adding rules in their robots.txt files that prohibit the Wayback Machine's crawler, and the Internet Archive respects such directives.

hackernews · doener · May 12, 23:11

**Background**: The Wayback Machine is a digital archive of the World Wide Web, operated by the Internet Archive, that allows users to view archived versions of web pages. Robots.txt is a standard used by websites to tell compliant web crawlers which parts of the site they should not access, and the Internet Archive has historically honored these requests. Some news organizations block archiving to protect paywalled content, but critics argue this undermines long-term preservation and public access.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">Robots.txt</a></li>
<li><a href="https://developers.google.com/search/docs/crawling-indexing/robots/intro">Robots.txt Introduction and Guide | Google Search Central | Documentation | Google for Developers</a></li>

</ul>
</details>

**Discussion**: Commenters express disappointment that the Internet Archive's compliance with robots.txt is 'rewarded' with blocking, while others profit by ignoring it. One comment suggests a 30-day embargo model as a compromise, similar to the Financial Times' arrangement with NewsBank. There is also debate about paywall ethics and alternative revenue models.

**Tags**: `#internet archive`, `#digital preservation`, `#paywalls`, `#web archiving`, `#robots.txt`

---

<a id="item-9"></a>
## [Obsidian Unveils Automated Plugin Review System](https://obsidian.md/blog/future-of-plugins/) ⭐️ 7.0/10

Obsidian has introduced a new automated plugin review system and a dedicated community site to replace the manual review process that had become a significant bottleneck. This change relieves a critical scaling bottleneck for the Obsidian ecosystem, reducing developer frustration and team burnout while enabling faster plugin releases. The system uses automated checks to review plugin submissions, but concerns remain about security as there is no proper permissions system or sandboxing, leaving plugins with full system access.

hackernews · xz18r · May 12, 15:45

**Background**: Obsidian is a popular markdown-based note-taking app known for its extensibility through plugins. As the user base grew and AI-assisted plugin development increased, manually reviewing each submission became unsustainable, prompting the need for an automated solution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Obsidian_(software)">Obsidian (software) - Wikipedia</a></li>
<li><a href="https://medium.com/@lennart.dde/why-obsidian-is-the-ultimate-note-taking-app-and-where-it-falls-short-9094e26ddc22">Why Obsidian is the Ultimate Note - Taking App (And Where... | Medium</a></li>

</ul>
</details>

**Discussion**: Community feedback is mixed: CEO kepano expresses excitement and invites questions, while developer dtkav thanks the team for relieving the bottleneck. However, users varun_ch and troad criticize the lack of a proper sandbox and permissions system, arguing that automated checks alone cannot prevent malicious plugins. Another user, sundarurfriend, initially feared the announcement meant restricting plugins.

**Tags**: `#obsidian`, `#plugins`, `#automation`, `#security`, `#community`

---

<a id="item-10"></a>
## [DeepMind reimagines mouse pointer with AI voice control](https://deepmind.google/blog/ai-pointer/) ⭐️ 6.0/10

Google DeepMind has unveiled a concept for an AI-powered mouse pointer that integrates voice commands and context awareness to reduce traditional prompting friction, demonstrated through experimental demos in Chrome. This proposal signals a shift toward intention-based interaction design, where the computer anticipates user needs rather than just responding to clicks. If realized, it could transform everyday computing workflows, but its reliance on voice control raises questions about practicality and user acceptance in shared environments. The AI pointer uses context to suggest actions and allows users to add elements to a prompt via keywords or voice, potentially requiring constant server communication for AI processing. Early demos show it taking several seconds to perform simple edits like changing a number, which critics argue is slower than existing methods.

hackernews · devhouse · May 12, 17:40

**Background**: The traditional mouse pointer has remained largely unchanged for decades, serving as a simple pointing device. DeepMind's proposal is part of a broader trend in human-computer interaction (HCI) toward context-aware and multimodal interfaces that combine voice, gesture, and intent recognition. This concept, sometimes called 'intention design,' aims to make interaction implicit by shifting the design focus from actions to user intent.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/ai-pointer/">Reimagining the mouse pointer for the AI era - deepmind.google</a></li>
<li><a href="https://9to5google.com/2026/05/12/deepmind-googlebook-magic-pointer/">DeepMind details Googlebook ‘Magic Pointer’ with demos you ...</a></li>
<li><a href="https://www.computer.org/publications/tech-news/trends/hci-trends-2026">Top HCI Trends in 2026 - computer.org</a></li>

</ul>
</details>

**Discussion**: Community comments on the concept are mixed. Many skeptics argue that voice control is impractical for routine use, disruptive in shared spaces, and often slower than existing right-click menus or keyboard shortcuts. Some users see potential for continuous LLM conversations while pointing, but overall sentiment leans toward the view that the solution creates new problems rather than solving real ones.

**Tags**: `#AI`, `#human-computer interaction`, `#voice control`, `#UI/UX`, `#DeepMind`

---