---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 15 items, 7 important content pieces were selected

---

1. [Pope Leo XIV's Encyclical Criticizes AI and Technology](#item-1) ⭐️ 9.0/10
2. [AI-Assisted Code: Slow Down for Quality](#item-2) ⭐️ 7.0/10
3. [Norway's Sovereign LLM Plan: 2PB Huawei Flash + HPE Cray](#item-3) ⭐️ 7.0/10
4. [Mullvad Rolls Out Mitigation for Exit IP Fingerprinting](#item-4) ⭐️ 7.0/10
5. [California Proposes Exempting Linux from Age-Verification Law](#item-5) ⭐️ 7.0/10
6. [Microsoft Copilot Cowork Vulnerability Allows File Exfiltration](#item-6) ⭐️ 7.0/10
7. [OpenClaw v2026.5.24-beta.1: Performance and Real-Time Updates](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Pope Leo XIV's Encyclical Criticizes AI and Technology](https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html) ⭐️ 9.0/10

Pope Leo XIV has released a sweeping encyclical titled 'Magnifica Humanitas' that issues a broad ethical critique of modern technology and artificial intelligence, warning about power concentration and calling for innovation to remain centered on human dignity. This is significant because it brings the moral authority of the Catholic Church into the debate on AI ethics and technology policy, potentially influencing public discourse and policy decisions worldwide. It directly engages technologists and the broader public in considering the societal impacts of their work. The encyclical warns that technologies like AI can concentrate power in the hands of a few, and emphasizes that technology is never neutral. It calls for a human-centered approach that prioritizes the common good over profit.

hackernews · theletterf · May 25, 10:11

**Background**: An encyclical is a formal papal letter addressed to the Church and often to the broader world, used to teach on important matters. Pope Leo XIV's predecessor, Pope Francis, also warned about AI and technology ethics. This new encyclical continues the Vatican's engagement with modern challenges.

**Discussion**: The Hacker News community engaged deeply with the encyclical, with commenters like hn_throwaway_99 questioning whether technology can ever be tamed for broader societal good. Another commenter, redfloatplane, highlighted the Pope's warning about power concentration. qsort, an atheist, praised the Vatican's thoughtful takes on technology, and sethbannon summarized the message as a call for builders to consider their impact on civilization.

**Tags**: `#AI ethics`, `#technology policy`, `#societal impact`, `#papal encyclical`, `#Hacker News discussion`

---

<a id="item-2"></a>
## [AI-Assisted Code: Slow Down for Quality](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 7.0/10

A blog post by Nolan Lawson advocates using AI for code review and implementation in a deliberate, iterative process to improve code quality rather than just speed. This highlights a nuanced approach to AI-assisted coding that prioritizes quality over productivity, addressing concerns about skill degradation and superficial code generation. The post suggests a workflow where AI is used for design, implementation, review, and iterative fixes, with different AI models handling different stages, such as Claude 4.7 Max for implementation and Codex GPT 5.5 for fast review.

hackernews · signa11 · May 25, 23:16

**Background**: Large language models (LLMs) like GPT and Claude are increasingly used by developers to generate code automatically. However, this often leads to faster but possibly lower-quality code, with developers losing critical thinking and code review skills. The article argues for a more deliberate process that maintains human oversight and iterative refinement.

**Discussion**: Community comments reveal diverse perspectives: some users describe their own iterative AI review loops that take more time than manual coding, while others emphasize the potential for AI to catch corner cases without deskilling workers. A skeptical comment warns against over-reliance on AI, and another criticizes the article for lacking concrete examples.

**Tags**: `#AI-assisted coding`, `#code review`, `#software engineering`, `#LLM`, `#development workflow`

---

<a id="item-3"></a>
## [Norway's Sovereign LLM Plan: 2PB Huawei Flash + HPE Cray](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 7.0/10

Norway is building a sovereign large language model (LLM) using 2 petabytes of Huawei flash storage paired with an HPE Cray EX supercomputer (codename Olivia) featuring 448 GPUs and 64,512 CPU cores. This initiative highlights the growing trend of nations developing sovereign AI capabilities to preserve linguistic and cultural data, but the relatively modest hardware scale compared to frontier models raises questions about feasibility and cost-effectiveness. The Olivia system is an HPE Cray Supercomputing EX system, and the project relies on Huawei flash storage. Community commenters noted that the hardware may be insufficient for training a fully fledged LLM compared to major industry efforts.

hackernews · rbanffy · May 25, 19:37

**Background**: A sovereign LLM is an AI language model owned and controlled by a nation-state, trained on its own infrastructure and data to reflect local language, culture, and history. Norway's effort aims to ensure Norwegian language and cultural knowledge are not overshadowed by English-centric models. The HPE Cray EX series is a supercomputer architecture used in many top-tier systems worldwide.

<details><summary>References</summary>
<ul>
<li><a href="https://eric-sandosham.medium.com/sovereign-llm-might-be-a-red-herring-39586e65c9ec">Sovereign LLM might be a Red Herring | by Eric Sandosham, Ph.D. | Apr, 2026 | Medium</a></li>
<li><a href="https://www.hpe.com/us/en/cray-exascale-supercomputing.html">HPE Cray Supercomputing | HPE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cray">Cray - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the project's necessity and feasibility. Some argued that sharing curated training data with frontier model builders might be more effective than building a standalone LLM. Others questioned who would use the model and whether the hardware, with 448 GPUs, is adequate for the stated goal.

**Tags**: `#sovereign LLM`, `#flash storage`, `#Norway`, `#LLM training`, `#HPC`

---

<a id="item-4"></a>
## [Mullvad Rolls Out Mitigation for Exit IP Fingerprinting](https://mullvad.net/en/help/exit-ip-vpn-servers-mitigation-rollout) ⭐️ 7.0/10

Mullvad has announced a mitigation rollout that changes how exit IP addresses are assigned across its VPN servers, preventing them from being used to fingerprint and track users when switching servers. This update addresses a significant privacy vulnerability that could allow an attacker to probabilistically identify a user across different VPN servers, undermining the core privacy promise of a VPN. The new method ensures that the exit IPs assigned to a user on one server provide no information about the exit IPs they use on another server, and this change is currently being tested and rolled out to Mullvad's servers in the coming weeks.

hackernews · Cider9986 · May 25, 17:45

**Background**: Exit IP fingerprinting works by correlating the exit IP addresses assigned to a user's WireGuard connections across multiple VPN servers. If an attacker can observe that the same set of exit IPs appears on different servers, they can infer that the same user is behind those connections. Mullvad's mitigation changes the assignment logic to break this correlation, enhancing user anonymity.

<details><summary>References</summary>
<ul>
<li><a href="https://mullvad.net/en/blog/exit-ip-fingerprinting-between-vpn-servers">Exit IP fingerprinting between VPN servers - Mullvad VPN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mullvad_VPN">Mullvad VPN</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that Mullvad Browser, which uses its own proxy rather than WireGuard, is already unaffected by this issue and also offers a Random mode for per-site IP rotation. Some users discussed broader browser fingerprinting techniques and suggested that browsers like Librewolf should spoof consistent profiles to resist fingerprinting altogether. One comment also noted that the help page should link directly to the blog post for clarity.

**Tags**: `#VPN`, `#privacy`, `#fingerprinting`, `#security`, `#Mullvad`

---

<a id="item-5"></a>
## [California Proposes Exempting Linux from Age-Verification Law](https://www.tomshardware.com/software/linux/california-moves-to-exempt-linux-from-its-upcoming-age-verification-law-after-backlash-over-forcing-operating-systems-to-collect-users-ages-amendment-proposed-by-the-same-lawmaker-who-wrote-the-original-law) ⭐️ 7.0/10

California has proposed an amendment to exempt Linux from its upcoming age-verification law, following significant backlash over the original requirement that operating systems collect users' ages. This policy adjustment is significant for open-source operating systems like Linux, as it avoids imposing privacy-invasive age checks on millions of users. It also sets a potential precedent for how similar laws treat open-source software versus proprietary systems. The amendment was proposed by the same lawmaker who authored the original age-verification law. The exemption specifically applies to Linux, though other operating systems may still be affected.

hackernews · rbanffy · May 25, 18:19

**Background**: California's age-verification law requires online services and operating systems to verify users' ages to protect minors. Critics argued that such mandates for open-source operating systems like Linux would undermine privacy and be technically unfeasible. The proposed exemption addresses these concerns, reflecting a compromise.

**Discussion**: Community comments show a mix of skepticism and approval. Some commenters question the effectiveness of the law itself, while others suspect the exemption might be a strategic move to prevent legal challenges from Linux developers on First Amendment grounds. There is also frustration that the law disregards technical realities and shifts burden to consumers.

**Tags**: `#age-verification`, `#open-source`, `#California law`, `#Linux`, `#privacy`

---

<a id="item-6"></a>
## [Microsoft Copilot Cowork Vulnerability Allows File Exfiltration](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files) ⭐️ 7.0/10

A researcher demonstrated that the Cowork feature in Microsoft 365 Copilot can be exploited through prompt injection to exfiltrate files from an organization's environment. This disclosure highlights a critical security risk for enterprises adopting LLM-based agents like Copilot Cowork, as prompt injection attacks can turn trusted automation tools into data exfiltration channels. The attack targets Copilot Cowork's skill system, where a malicious skill can be crafted to exfiltrate files via command injection, similar to a 'curl $url | bash' scenario; the feature is currently in beta and was reportedly rushed to production.

hackernews · Kneenex · May 25, 21:45

**Background**: Prompt injection is a vulnerability where an attacker embeds malicious instructions in data processed by an LLM, causing it to act against the user's intent. Microsoft Copilot Cowork is an LLM agent that automates tasks across Microsoft 365, such as sending emails and scheduling meetings, by executing skills on behalf of the user. Such agents are increasingly adopted in enterprise settings, making them attractive targets for prompt injection attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft 365 Blog</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/">Copilot Cowork overview (Frontier) | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork">Use Copilot Cowork (Frontier) | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some argue the exploit works as expected for an LLM agent skill, while others criticize Microsoft for rushing the beta feature to production. Some commenters note that prompt injection attacks are not new and that similar vulnerabilities have been found in other LLM-driven tools like OpenAI's Atlas.

**Tags**: `#AI security`, `#prompt injection`, `#Microsoft Copilot`, `#LLM agents`, `#enterprise security`

---

<a id="item-7"></a>
## [OpenClaw v2026.5.24-beta.1: Performance and Real-Time Updates](https://github.com/openclaw/openclaw/releases/tag/v2026.5.24-beta.1) ⭐️ 6.0/10

OpenClaw v2026.5.24-beta.1 optimizes gateway and channel caching to reduce repeated JSON and manifest reads, and introduces real-time interaction capabilities for WebUI and Discord voice, allowing users to steer or queue tasks during active consult runs. These improvements make OpenClaw more efficient and responsive, particularly for users running large-scale agent deployments who need faster startup and lower overhead, while the real-time voice features expand how operators can interact with running agents. The release caches process-stable channel catalog reads and plugin metadata snapshots, adds adaptive image compression with an 'agents.defaults.imageQuality' preference, and includes a meeting-notes plugin with Discord voice as the first live source.

github · github-actions[bot] · May 24, 14:42

**Background**: OpenClaw is a free and open-source autonomous AI agent framework that uses messaging platforms as its primary user interface. It runs a long-lived Gateway process that handles channels, nodes, and sessions, and reads configuration files like SOUL.md and USER.md to define agent identity and behavior. Performance caching reduces redundant filesystem operations, which is critical for production deployments with many plugins and channels.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://docs.openclaw.ai/gateway">Gateway runbook - OpenClaw</a></li>
<li><a href="https://lumadock.com/tutorials/openclaw-troubleshooting-common-errors">OpenClaw not working? Common fixes that actually help - LumaDock</a></li>

</ul>
</details>

**Tags**: `#performance`, `#optimization`, `#real-time`, `#discord`, `#gateway`

---