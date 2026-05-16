---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 25 items, 10 important content pieces were selected

---

1. [Pixel 10 0-click exploit chain revealed by Project Zero](#item-1) ⭐️ 9.0/10
2. [Mitchell Hashimoto Warns of 'AI Psychosis' in Software Companies](#item-2) ⭐️ 8.0/10
3. [Zulip Founders Donate Company to New Nonprofit Foundation](#item-3) ⭐️ 8.0/10
4. [California bill mandates patches or refunds for online game shutdowns](#item-4) ⭐️ 8.0/10
5. [AI progress may not follow sigmoid curves, analysis warns](#item-5) ⭐️ 8.0/10
6. [US DOJ demands Apple and Google unmask over 100k car-tinkering app users](#item-6) ⭐️ 8.0/10
7. [Project Gutenberg announces site improvements and sparks community discussion](#item-7) ⭐️ 7.0/10
8. [Image-blaster Generates 3D Worlds from a Single Image](#item-8) ⭐️ 7.0/10
9. [OpenClaw v2026.5.14-beta.2 released with per-agent overrides](#item-9) ⭐️ 6.0/10
10. [LoRa and Meshtastic: Off-Grid Mesh Networking Alternative](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Pixel 10 0-click exploit chain revealed by Project Zero](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a full zero-click exploit chain for the Pixel 10, combining a remote audio decoding bug in Dolby with a vulnerable video driver to achieve arbitrary kernel code execution without any user interaction. This demonstrates that AI-powered message analysis features on modern smartphones significantly increase the attack surface, and that 0-click exploits are a practical threat even for flagship devices. It also highlights the challenge of securing complex hardware driver ecosystems across Android. The exploit chain uses CVE-2025-54957, a Dolby audio decoding vulnerability that existed across all of Android until patched in January 2026, and a Pixel 10's specific video driver bug that allowed physical memory mapping. Project Zero noted that this was the first Android driver bug they reported that was patched within 90 days of vendor notification.

hackernews · happyhardcore · May 15, 13:39

**Background**: A zero-click exploit is a type of security vulnerability that can be triggered without any user interaction, such as clicking a link or opening a file. In this case, the attack starts by sending a specially crafted audio message that, when automatically processed by the phone's AI-powered message analysis feature, executes malicious code. The exploit then escalates to kernel control via a vulnerable video driver. This illustrates the trade-off between convenience features that pre-process user data and security.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0-click exploit chain for the Pixel 10: When a Door Closes ...</a></li>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about AI features increasing attack surface, with one user noting that this lesson should have been learned already. Another commenter praised Google's relatively fast patch time (under 90 days) but wondered about the rest of Android and Apple's response times. There was also discussion about the recent increase in published exploit announcements, questioning whether it's real or due to AI hype.

**Tags**: `#security`, `#android`, `#mobile`, `#exploit`, `#google pixel`

---

<a id="item-2"></a>
## [Mitchell Hashimoto Warns of 'AI Psychosis' in Software Companies](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto, co-founder of HashiCorp, posted a critique arguing that many companies are suffering from 'AI psychosis'—blindly trusting AI-generated code without understanding consequences, leading to brittle systems and flawed decision-making. This critique highlights a growing risk in the software industry where over-reliance on AI tools can undermine code quality and human oversight, potentially leading to unstable systems and unsustainable development practices. The post received high engagement (795 points, 346 comments) and sparked debate among prominent figures about the practical risks of AI-generated code and the necessity of human review.

hackernews · reasonableklout · May 15, 20:26

**Background**: "AI psychosis" refers to a state where decision-makers blindly trust AI outputs without critical evaluation, analogous to uncritical adoption of AI-generated code. This is relevant as AI coding assistants like GitHub Copilot and ChatGPT become widespread, raising concerns about code maintainability and the erosion of engineering judgment.

**Discussion**: Commenters largely agreed with Hashimoto's warning, with zmmmmm predicting that purely AI-written systems would become unstable beyond human comprehension. impulser_ clarified that the issue is outsourcing decision-making to AI, not using AI itself, while foxfired noted that such practices might turn software engineering into a proper engineering discipline out of necessity.

**Tags**: `#AI`, `#software engineering`, `#critical thinking`, `#AI hype`, `#software development`

---

<a id="item-3"></a>
## [Zulip Founders Donate Company to New Nonprofit Foundation](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

Zulip's founders are stepping back from full-time leadership and donating the company to a newly formed, independent nonprofit called the Zulip Foundation, ensuring the platform's future as a public good free from commercial pressures. This transition secures Zulip's long-term governance and sustainability as an open-source project, building trust with users who fear commercial exploitation, and sets a precedent for other open-source companies. Tim Abbott and several senior team members are leaving to join Anthropic, and the foundation is independent with no ties to the founders' new employer. The announcement was made on a Friday afternoon, a timing some community members noted as unusual.

hackernews · boramalper · May 15, 18:37

**Background**: Zulip is an open-source team chat application founded in 2012, known for its organized, topic-based conversations that combine real-time messaging with structured threads. It is widely used by open-source communities and distributed teams as an alternative to proprietary tools like Slack.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip</a></li>
<li><a href="https://zulip.com/">Zulip — organized team chat</a></li>

</ul>
</details>

**Discussion**: The community expressed mixed feelings: many are optimistic about the foundation's mission to serve the public good, but some are skeptical about the timing and the departure of core team members, noting parallels to recent Bun/Rust acquisition news and the Friday announcement. Others praised Zulip's interface as superior to Discord for serious discussions.

**Tags**: `#zulip`, `#open-source`, `#foundation`, `#governance`, `#nonprofit`

---

<a id="item-4"></a>
## [California bill mandates patches or refunds for online game shutdowns](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

A California bill has cleared a key hurdle that would require game publishers to either patch online games to work offline or provide refunds when they shut down servers. This legislation could fundamentally reshape digital preservation and consumer rights for online games, affecting how publishers sunset games and potentially reducing loss of access to purchased titles. The bill exempts completely free games and games offered solely through a subscription, which could lead publishers to shift business models to avoid compliance. The requirement applies only to games sold in California.

hackernews · Lihh27 · May 15, 19:48

**Background**: Online games often become unplayable when servers are shut down, leaving consumers with no access to games they purchased. This bill aims to address that by mandating either an offline mode patch or a refund. However, implementing such patches can be technically complex and costly, and some argue it may discourage companies from creating online games altogether.

**Discussion**: Commenters expressed mixed views: some suggested open-sourcing server code as a fairer solution, while others warned the bill could increase business risk and lead to more subscription-only models. Concerns were raised about unintended consequences, such as companies creating subsidiaries to go bankrupt and avoid compliance.

**Tags**: `#gaming`, `#legislation`, `#digital preservation`, `#consumer rights`, `#online games`

---

<a id="item-5"></a>
## [AI progress may not follow sigmoid curves, analysis warns](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 8.0/10

Scott Alexander's article 'The sigmoids won't save you' argues that AI progress may not follow a continuous sigmoid curve, challenging the assumption that further scaling and incremental improvements will lead to continued breakthroughs. This analysis is significant because it questions a core belief in the AI field — the scaling hypothesis — and warns against complacency that future breakthroughs are guaranteed, potentially influencing investment, research directions, and public expectations about AI timelines. The article uses historical examples like aircraft speed improvements, where successive sigmoid curves from different technologies (propellers, turbojets, ramjets) each reached fundamental limits, suggesting AI may require similar paradigm shifts rather than continued scaling of current approaches.

hackernews · Tomte · May 15, 10:51

**Background**: A sigmoid curve (S-curve) describes progress that starts slowly, accelerates, then plateaus as limits are reached. The scaling hypothesis in AI posits that increasing model size, data, and compute leads to predictable performance gains. Many believe AI has followed multiple sigmoid curves, with each new technique enabling further scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://gwern.net/scaling-hypothesis">The Scaling Hypothesis · Gwern.net</a></li>
<li><a href="https://finbarr.ca/the-sigmoid/">The Sigmoid: a metaphor for technological progress - Finbarr</a></li>

</ul>
</details>

**Discussion**: Commenters offered a range of perspectives: some felt the article dismissed its own answer about paradigm shifts, others pointed to reasoning as a second sigmoid after transformers, while one noted the inherent uncertainty in predicting AI progress. A few criticized the author for perceived personal bias in his previous AGI timeline predictions.

**Tags**: `#AI progress`, `#sigmoid curves`, `#technological limits`, `#scaling hypothesis`, `#machine learning`

---

<a id="item-6"></a>
## [US DOJ demands Apple and Google unmask over 100k car-tinkering app users](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice has issued subpoenas to Apple and Google demanding they reveal the identities of over 100,000 users of a mobile app used to modify car engine control units and defeat emissions controls. This marks an unprecedented step in targeting individual app users in an emissions crackdown. This request sets a major precedent for government access to app store user data, potentially chilling legitimate car tinkering and raising serious privacy concerns. It also highlights the tension between environmental enforcement and digital rights, as app stores become central to government investigations. The app in question allows users to reflash or tune their vehicle's ECU via smartphone, effectively disabling factory emissions controls—a practice known as using a 'defeat device.' The DOJ is seeking the names, addresses, and other identifying information of every user who downloaded the app, which could affect hundreds of thousands of people.

hackernews · tencentshill · May 15, 17:28

**Background**: A defeat device is any hardware or software that disables emissions controls under real-world driving conditions, even if the vehicle passes lab tests. The U.S. Clean Air Act prohibits tampering with emissions systems, and selling or installing defeat devices can result in fines and jail time. Vehicle tuning apps like the one mentioned allow users to modify engine parameters, which can be used both for legitimate performance tuning and for illegal emissions cheating.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Defeat_device">Defeat device - Wikipedia</a></li>
<li><a href="https://cleanairnortheast.epa.gov/tampering.html">Tampering and Aftermarket Defeat Devices | Clean Air Northeast</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed reactions: some criticized the DOJ for seeking user data without having specific witnesses, while others felt no sympathy for users who exploit the app to 'roll coal' and evade emissions rules. Concerns were raised about the precedent this sets for future government surveillance of app stores, with suggestions that users should rely on decentralized app distribution like F-Droid to protect privacy.

**Tags**: `#privacy`, `#government surveillance`, `#emissions regulations`, `#app stores`, `#digital rights`

---

<a id="item-7"></a>
## [Project Gutenberg announces site improvements and sparks community discussion](https://www.gutenberg.org/) ⭐️ 7.0/10

A programmer from Project Gutenberg announced on a social news platform that the site has undergone significant improvements over the past few months, with more updates to come, and invited users to revisit the website. As one of the oldest and largest free digital libraries, Project Gutenberg's ongoing improvements ensure that millions of public domain works remain accessible to a global audience, reinforcing the importance of open access in an era of increasing digital paywalls. The improvements include a redesigned user interface and enhanced browsing features, though specific technical changes were not detailed. The platform, which started in 1971, now offers over 70,000 free ebooks.

hackernews · JSeiko · May 15, 16:15

**Background**: Project Gutenberg was founded in 1971 by Michael S. Hart, who digitized the U.S. Declaration of Independence as the first ebook. It relies on volunteer efforts to digitize and proofread public domain texts, making classic literature freely available in multiple formats. The platform is a cornerstone of the open access movement and has inspired similar digital libraries worldwide.

**Discussion**: Community members expressed appreciation for the improvements and shared personal anecdotes about using Project Gutenberg, such as helping elderly relatives access classic texts. Some users lamented the lack of direct integration with popular ebook readers like Kindle, while others reported a concerning issue: accessing gutenberg.org from Italy displayed a police seizure notice referencing a criminal case, which may indicate a legal problem.

**Tags**: `#Project Gutenberg`, `#digital library`, `#ebooks`, `#public domain`, `#open access`

---

<a id="item-8"></a>
## [Image-blaster Generates 3D Worlds from a Single Image](https://github.com/neilsonnn/image-blaster) ⭐️ 7.0/10

Image-blaster is an open-source tool that combines multiple AI models, including WorldLabs, to generate interactive 3D environments, special effects, and meshes from a single 2D image. This dramatically lowers the barrier for creating 3D content, enabling game developers, artists, and designers to produce explorable 3D scenes from a single photograph, which was previously only possible with multiple images or complex modeling. The tool leverages WorldLabs' spatial intelligence model to convert a single image into a 3D scene, and it also supports generating meshes and visual effects. Community tests note that results can sometimes hallucinate unrealistic geometry outside the input image's scope.

hackernews · MattRogish · May 15, 15:42

**Background**: WorldLabs is a spatial intelligence model developed by Fei-Fei Li's team that can generate interactive 3D worlds from a single 2D image or text prompt, with realistic depth and consistent geometry. Traditional 3D reconstruction methods like Microsoft PhotoSynth required multiple images to create 3D environments, making single-image approaches a significant leap.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fastcompany.com/91437004/fei-fei-li-world-labs-spatial-ai-mapping-3d">Fei-Fei Li debuts world -generating AI model - Fast Company</a></li>
<li><a href="https://genvr.ai/models/3dgen/worldlabs_3d_scenes">Models /3dgen/ worldlabs _3d_scenes - GenVR AI</a></li>

</ul>
</details>

**Discussion**: The community expressed strong enthusiasm, with one commenter comparing it favorably to Microsoft's PhotoSynth from seventeen years ago. However, some users reported that WorldLabs results often hallucinate unrealistic geometry, and others questioned whether similar tools exist for isometric sprites. The discussion also compared Image-blaster to Microsoft's TRELLIS model for 3D generation.

**Tags**: `#3D generation`, `#AI`, `#computer vision`, `#game development`, `#meshing`

---

<a id="item-9"></a>
## [OpenClaw v2026.5.14-beta.2 released with per-agent overrides](https://github.com/openclaw/openclaw/releases/tag/v2026.5.14-beta.2) ⭐️ 6.0/10

This beta release adds per-agent bootstrap profile overrides for settings like contextInjection and bootstrapMaxChars, introduces lazy-loading for Canvas modules to reduce Gateway startup cost, and includes new maintainer tooling such as a codex-review skill and Docker-based release validation lanes. These enhancements give developers finer-grained control over agent behavior without editing global defaults, while lazy-loading improves Gateway startup time—critical for production deployments with many agents. The new maintainer tooling also raises code quality and release reliability across the OpenClaw ecosystem. Per-agent overrides inherit from agents.defaults when omitted, and are applied to contextInjection, bootstrapMaxChars, and bootstrapTotalMaxChars. Lazy-loading affects the HTTP host, hosted media resolver, CLI implementation, and tool runtime modules of Canvas. The release validation now includes Docker lanes for onboarding, model setup, plugin lifecycle, and Gateway restart survival.

github · steipete · May 15, 11:11

**Background**: OpenClaw is an open-source AI coding assistant platform that supports multi-agent architectures, where different agents can have specialized roles and configurations. Bootstrap profiles define the initial context and limits for each agent's conversation. Lazy-loading is a performance optimization technique that delays loading of modules until they are actually needed, reducing initial resource consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.openclaw.ai/concepts/agent-workspace">Agent workspace - OpenClaw</a></li>
<li><a href="https://docs.openclaw.ai/platforms/mac/canvas">Canvas - OpenClaw</a></li>

</ul>
</details>

**Tags**: `#openclaw`, `#beta release`, `#SDK`, `#agents`, `#performance`

---

<a id="item-10"></a>
## [LoRa and Meshtastic: Off-Grid Mesh Networking Alternative](http://www.ruanyifeng.com/blog/2026/05/weekly-issue-396.html) ⭐️ 6.0/10

Ruan Yifeng's weekly newsletter issue 396 introduces a low-cost, long-range wireless networking solution using LoRa and the open-source Meshtastic project to build a private mesh network when the internet is completely down. The system can cover tens of kilometers, runs on a power bank, and costs only a few hundred RMB per device set. This solution offers a practical emergency fallback for communication during disasters or infrastructure failures, enabling individuals to maintain text messaging without relying on internet service providers. It showcases how open-source community projects can provide resilient, decentralized communication alternatives. The network uses LoRa (Long Range) spread-spectrum radio and the Meshtastic software platform to automatically relay messages between nodes. Each node has a range of 5–15 km in typical urban environments and up to tens of kilometers in open areas, but bandwidth is limited to text messages only, not suitable for web browsing or video.

rss · 阮一峰的个人网站 · May 15, 00:01

**Background**: LoRa is a proprietary spread-spectrum radio modulation technique designed for long-range, low-power communication, often used in IoT applications. Meshtastic is an open-source mesh networking protocol and software that runs on LoRa hardware, allowing devices to form a decentralized mesh without any existing infrastructure; it operates in unlicensed ISM bands such as 433 MHz, 868 MHz, or 915 MHz.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRa">LoRa - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Meshtastic">Meshtastic</a></li>
<li><a href="https://docs.m5stack.com/zh_CN/guide/lora/meshtastic/start">通过M5Stack 产品使用Meshtastic</a></li>

</ul>
</details>

**Tags**: `#互联网通信`, `#组网`, `#无线通信`, `#应急通信`, `#阮一峰周刊`

---