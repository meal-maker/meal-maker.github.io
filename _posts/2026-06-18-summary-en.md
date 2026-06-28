---
layout: default
title: "Horizon Summary: 2026-06-18 (EN)"
date: 2026-06-18
lang: en
---

> From 30 items, 13 important content pieces were selected

---

1. [Epic Games Open-Sources Lore VCS for Game Development](#item-1) ⭐️ 8.0/10
2. [Leaked financials reveal OpenAI loses billions annually](#item-2) ⭐️ 8.0/10
3. [Firecracker VMs on EC2 launch browsers under 1s](#item-3) ⭐️ 8.0/10
4. [U.S. Science in Chaos as Researchers Flee](#item-4) ⭐️ 8.0/10
5. [RFC 10008 Proposes New HTTP QUERY Method](#item-5) ⭐️ 8.0/10
6. [Tesco to Move 40,000 Workloads Off VMware After Broadcom Changes](#item-6) ⭐️ 8.0/10
7. [US delays DeepSeek blacklist, flags over 100 Chinese firms](#item-7) ⭐️ 7.0/10
8. [Adam Launches CADAM: Open-Source AI CAD from Text Prompts](#item-8) ⭐️ 7.0/10
9. [8-Bit Live Baseball Gamecast](#item-9) ⭐️ 7.0/10
10. [Volkswagen Blocks GrapheneOS Users via Play Integrity](#item-10) ⭐️ 7.0/10
11. [Why Thinking Aloud Beats Thinking Alone](#item-11) ⭐️ 7.0/10
12. [Robot Game Reveals AI Model Trade-offs in Cost and Safety](#item-12) ⭐️ 7.0/10
13. [Human Connection as an AI-Proof Moat](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Epic Games Open-Sources Lore VCS for Game Development](https://lore.org/) ⭐️ 8.0/10

Epic Games has released Lore, an open source, centralized version control system designed specifically for large binary assets in game development, competing with Perforce. Lore addresses a critical gap in the open source ecosystem, providing a modern alternative to Perforce for game studios that struggle with Git's handling of binary files and large repositories. Lore is a content-addressed system using Merkle trees and immutable revision chains, with built-in deduplication, file locking, and on-demand data hydration for sparse checkouts.

hackernews · regnerba · Jun 17, 14:30

**Background**: Git, the dominant version control system for software development, is inefficient for binary files because it stores whole copies of each version. Game development relies heavily on large binary assets like textures and 3D models, requiring file locking and efficient storage. Perforce has been the industry standard for game studios, but it is proprietary and complex to administer. Lore aims to offer a free, modern, open source alternative tailored to these needs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/lore: Lore is a next-generation, open source revision control system · GitHub</a></li>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://www.phoronix.com/news/Epic-Games-Lore-VCS">Epic Games Announces Lore Open-Source Version Control System - Phoronix</a></li>

</ul>
</details>

**Discussion**: The Hacker News community largely agrees that a Perforce alternative is needed for game development, with many pointing out Git's shortcomings with binary assets and praising Epic's move. Some commenters note that Lore is not intended to replace Git for code, and that Perforce's complexity makes it ripe for disruption. There is also specific enthusiasm for Lore's potential within Unreal Engine workflows.

**Tags**: `#version control`, `#game development`, `#open source`, `#scalability`, `#Perforce`

---

<a id="item-2"></a>
## [Leaked financials reveal OpenAI loses billions annually](https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year/) ⭐️ 8.0/10

Leaked financial documents show that OpenAI is losing billions of dollars each year, driven by extremely high selling, general, and administrative (SG&A) costs and astronomical research and development expenditures. These numbers spark debate about OpenAI's long-term sustainability and raise broader questions about the economics of the AI industry, where leading companies burn through cash despite massive user growth. ChatGPT has over 900 million weekly active users, but only about 50 million are paying subscribers. The company spends roughly $100 on sales for each paying customer and SG&A is 55% of revenue.

hackernews · greenchair · Jun 17, 21:31

**Background**: OpenAI is the company behind ChatGPT and other advanced AI models. Despite its rapid user growth and popularity, the company has historically operated at a loss due to the massive compute and talent costs required to train and run cutting-edge AI systems. Leaked financials reveal the scale of these costs in detail.

**Discussion**: Commenters express concern about OpenAI's sustainability, noting that extreme overhead and R&D costs make profitability seem distant. Some argue that the company needs to grow 10-100 times to become profitable, while others point out the difficulty of converting free users to paid subscribers given free alternatives like DeepSeek.

**Tags**: `#OpenAI`, `#financials`, `#AI industry`, `#sustainability`, `#startup economics`

---

<a id="item-3"></a>
## [Firecracker VMs on EC2 launch browsers under 1s](https://browser-use.com/posts/firecracker-browser-infra) ⭐️ 8.0/10

Browser-use.com describes how they run Firecracker microVMs inside EC2 instances using nested virtualization to launch headless Chromium browsers in under 1 second, achieving 81% stealth rate against anti-bot detection on their benchmark. This breakthrough enables extremely fast and stealthy browser automation, which is valuable for web scraping, testing, and AI agents, but also raises ethical concerns about bypassing anti-bot protections that many websites rely on. Nested virtualization on virtual EC2 instances only became available in February 2026, previously requiring bare metal instances. Their browsers also score 84.8% on Halluminate BrowserBench, the highest among providers.

hackernews · gregpr07 · Jun 16, 15:15

**Background**: Firecracker is an open-source microVM manager from AWS, designed for serverless computing with startup times as low as 125 ms. Nested virtualization allows running a hypervisor inside a virtualized EC2 instance, enabling multiple VMs within a single instance. Headless Chromium is a version of the Chrome browser that runs without a graphical user interface, often used for automated tasks like web scraping.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast microVMs for serverless computing. · GitHub</a></li>
<li><a href="https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-ec2-nested-virtualization-on-virtual/">Amazon EC2 supports nested virtualization on virtual Amazon ...</a></li>
<li><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html">Use nested virtualization to run hypervisors in Amazon EC2 ...</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed reactions: some question the ethics of bypassing anti-bot measures, while others note technical nuances like the recent support for nested virtualization on virtual EC2. Alternative approaches, such as using AWS Lambda or switching to lighter browsers like Lightpanda, are also discussed.

**Tags**: `#Firecracker`, `#AWS EC2`, `#browser automation`, `#headless Chromium`, `#nested virtualization`

---

<a id="item-4"></a>
## [U.S. Science in Chaos as Researchers Flee](https://www.scientificamerican.com/article/americas-compact-between-science-and-politics-is-broken/) ⭐️ 8.0/10

The U.S. scientific research enterprise is experiencing severe disruptions due to funding cuts, visa restrictions, and political turmoil, prompting many scientists to leave the country or abandon research careers. This exodus of talent threatens America's leadership in science and technology, undermines long-term research capabilities, and could accelerate a global shift of scientific talent away from the United States. The disruptions include frozen grant funding, inability to hire foreign graduate students due to new visa restrictions, and a pervasive atmosphere of tension and uncertainty within research institutions.

hackernews · presspot · Jun 17, 09:54

**Background**: For decades, the U.S. has been a global leader in scientific research, supported by a compact between science and politics that provided stable funding and openness to international talent. Recent political shifts have broken that compact, with cuts to research budgets and restrictive immigration policies.

**Discussion**: Commenters share personal stories of leaving the U.S. or abandoning science, citing funding freezes, visa barriers, and a demoralizing atmosphere. Some critique past research funding efficiency, but the dominant sentiment is that the current crisis is driving away irreplaceable talent and fundamentally damaging the research enterprise.

**Tags**: `#Science Policy`, `#Research Funding`, `#U.S. Science`, `#Immigration`, `#Academia`

---

<a id="item-5"></a>
## [RFC 10008 Proposes New HTTP QUERY Method](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 8.0/10

RFC 10008, published on April 1, 2025, defines a new HTTP QUERY method that allows clients to send a request body in a safe and idempotent manner, unlike GET which has no body, and POST which is not idempotent. This proposal fills a long-standing gap in HTTP for idempotent requests with a body, which could streamline API design, improve caching semantics, and eliminate the need for workarounds like using POST for queries. It has the potential to become a new standard method used by web applications and services. The QUERY method is similar to POST but is explicitly required to be safe and idempotent, meaning repeated requests have the same effect and no side effects. Caching of QUERY responses is more complex because the cache key must include the request body, which the community discussion highlights as a potential challenge.

hackernews · schappim · Jun 17, 10:51

**Background**: HTTP methods like GET are safe and idempotent but do not support a request body, making them unsuitable for complex queries. POST can include a body but is not idempotent, so refreshing a page after a POST form submission may cause a warning. The QUERY method aims to combine the best of both: allow a request body while guaranteeing idempotency and safety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008: The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent">Idempotent - Glossary - MDN Web Docs - Mozilla</a></li>

</ul>
</details>

**Discussion**: The community discussion shows a mix of interest and technical concern. One commenter finds the idea of including the request body in the cache key odd and potentially unbounded, while another wonders if HTML forms will support QUERY to avoid re-submission warnings. Some praise the decision to create a new method instead of allowing a body in GET, citing interoperability issues, and others note the milestone of reaching a 5-digit RFC number.

**Tags**: `#HTTP`, `#RFC`, `#web standards`, `#API design`, `#protocols`

---

<a id="item-6"></a>
## [Tesco to Move 40,000 Workloads Off VMware After Broadcom Changes](https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/) ⭐️ 8.0/10

Tesco, the UK's largest supermarket chain, is migrating approximately 40,000 server workloads away from VMware in response to Broadcom's aggressive licensing and pricing changes following its acquisition of VMware. This move signals a major industry shift as large enterprises abandon VMware en masse due to Broadcom's controversial licensing practices, potentially reshaping the virtualization market and boosting competitors like Proxmox. Tesco faces migration challenges because its new virtualization software is incompatible with its existing Veeam and Zerto backup products, and the migration requires building duplicate hardware clusters to move production on-premises workloads.

hackernews · Bender · Jun 17, 21:00

**Background**: Broadcom completed its $69 billion acquisition of VMware in November 2023 and subsequently introduced major licensing changes, including moving from perpetual licenses to subscription models and drastically increasing costs, which has angered many customers and prompted migrations to alternatives such as Proxmox and Nutanix.

**Discussion**: Commenters noted that Broadcom has a history of aggressive pricing with other acquisitions, and one user questioned how such large migrations can be affordably executed without duplicate hardware, while another speculated whether Tesco's new software might be Nutanix based on the backup incompatibility issue.

**Tags**: `#virtualization`, `#Broadcom`, `#VMware`, `#enterprise IT`, `#migration`

---

<a id="item-7"></a>
## [US delays DeepSeek blacklist, flags over 100 Chinese firms](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 7.0/10

The US government has delayed placing Chinese AI company DeepSeek on a trade blacklist, while simultaneously designating over 100 other Chinese firms as national security risks. This policy decision directly affects developers and businesses relying on DeepSeek's affordable AI models, especially in coding tools. The temporary reprieve highlights ongoing US-China tech tensions and the potential for future escalation. DeepSeek has not been added to the U.S. Entity List, which restricts American companies from selling goods and services to listed entities. Many Chinese AI firms already have minimal dependence on US technology except for restricted Nvidia GPUs.

hackernews · giuliomagnifico · Jun 17, 03:55

**Background**: DeepSeek is a Chinese AI startup owned by hedge fund High-Flyer, known for its large language models and the DeepSeek-R1 chatbot that became the most downloaded free app on the US iOS App Store in January 2025. The U.S. Entity List is a trade restriction tool used to block exports to entities deemed a national security threat. The move comes amid broader US-China technological competition, including export controls on advanced AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(chatbot)">DeepSeek (chatbot) - Wikipedia</a></li>
<li><a href="https://www.deepseek.com/en/">DeepSeek</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some developers rely on DeepSeek daily and worry about potential restrictions, while others criticize the US policy as protectionist or hypocritical, comparing it to China's approach. A few note that many Chinese AI firms are already on the Entity List and seem unaffected due to limited US dependency.

**Tags**: `#DeepSeek`, `#US-China tech policy`, `#AI regulation`, `#security risks`

---

<a id="item-8"></a>
## [Adam Launches CADAM: Open-Source AI CAD from Text Prompts](https://github.com/Adam-CAD/CADAM) ⭐️ 7.0/10

Adam (YC W25) has launched CADAM, an open-source text-to-CAD platform that generates parametric 3D models from natural language prompts and image references, outputting OpenSCAD code with interactive sliders for dimension editing. This could lower the barrier to mechanical design by allowing non-experts to create 3D models through simple text descriptions, while the open-source nature and code-as-CAD approach may accelerate innovation in AI-assisted engineering design. CADAM runs fully in-browser by compiling OpenSCAD to WebAssembly, supports multiple AI models via the Vercel AI SDK (including Gemini 3.1 Pro as the top performer), and exports to STL, SCAD, OBJ, GLB/GLTF, FBX, and DXF formats.

hackernews · zachdive · Jun 17, 16:14

**Background**: Traditional CAD software like Fusion 360 or SolidWorks requires manual modeling through graphical interfaces. 'CAD as code' is a paradigm where designs are defined programmatically, enabling version control, automation, and AI generation. TanStack Start is a full-stack React framework used in CADAM's frontend.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computer-aided_design">Computer-aided design - Wikipedia</a></li>
<li><a href="https://www.cadascode.com/">CAD as Code | Home</a></li>
<li><a href="https://tanstack.com/start/latest">TanStack Start</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: one engineer expressed strong skepticism about AI's usefulness for mechanical design, arguing it's faster to model manually. However, another user reported a positive experience generating a grommet seal quickly, and several expressed excitement about AI-based CAD tools.

**Tags**: `#AI`, `#CAD`, `#open-source`, `#3D modeling`, `#Y Combinator`

---

<a id="item-9"></a>
## [8-Bit Live Baseball Gamecast](https://ribbie.tv/watch) ⭐️ 7.0/10

The website ribbie.tv converts official MLB data feeds into near real-time 8-bit pixel art broadcasts of live baseball games, complete with stadiums, day/night modes, and scoreboards. This project demonstrates a novel way to visualize live sports data using retro pixel art, making baseball accessible to viewers with limited bandwidth or those who prefer a minimalist aesthetic; it also highlights the creative potential of public MLB APIs. The gamecast is built on the MLB Stats API, and the creator has added details like actual stadium shapes, between-inning interstitials, and live score updates; however, some community members noted that the pixel art generation uses AI, which could be improved with deterministic downsampling.

hackernews · brownrout · Jun 17, 16:44

**Background**: Major League Baseball provides a public Stats API that delivers real-time play-by-play data, box scores, and game events. This API allows developers to build custom visualizations and applications. Ribbie.tv taps into this data stream and renders each game state as a pixel art animation, inspired by classic 8-bit video games.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/MLB_Stats_API">MLB Stats API — Grokipedia</a></li>
<li><a href="https://github.com/pseudo-r/Public-MLB-API">MLB Stats API Documentation - GitHub</a></li>
<li><a href="https://pypi.org/project/MLB-StatsAPI/">MLB-StatsAPI · PyPI</a></li>

</ul>
</details>

**Discussion**: The Hacker News community reacted positively with high engagement, offering detailed suggestions such as adding a play-by-play log, making between-innings tabs clickable, and including sound effects. Some users expressed skepticism about the use of AI for pixel art, recommending deterministic downsampling and real pixel fonts instead.

**Tags**: `#baseball`, `#pixel art`, `#real-time visualization`, `#data streaming`, `#creative coding`

---

<a id="item-10"></a>
## [Volkswagen Blocks GrapheneOS Users via Play Integrity](https://discuss.grapheneos.org/d/35949-volkswagen-app?page=3) ⭐️ 7.0/10

Volkswagen has blocked GrapheneOS users from accessing its mobile app and API by requiring Play Integrity certification, a device attestation check that GrapheneOS does not pass by default. This move restricts user autonomy and privacy for GrapheneOS users, and signals a growing trend of automakers using device attestation to lock out alternative operating systems and community-driven integrations. The API lock also kills community projects like Home Assistant integrations that relied on Volkswagen's API, and users report the official app contains 60% advertisements and only 30% useful features.

hackernews · microtonal · Jun 17, 15:04

**Background**: GrapheneOS is an open-source, privacy-focused mobile operating system based on Android Open Source Project (AOSP), available for Google Pixel devices. It strips out Google proprietary services by default to enhance security and privacy. Google's Play Integrity API assesses whether a device runs a certified Android build with Google services; GrapheneOS typically does not pass this check because it lacks Google's proprietary components, leading to blocked access for apps that enforce the attestation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS : the private and secure mobile OS</a></li>
<li><a href="https://support.google.com/android/answer/7165974?hl=en">Check & fix Play Protect certification status - Android Help How To Guide - FIX play integrity | XDA Forums Play Integrity API | Android Developers Question - Device's play certification is gone, how to fix ... GitHub - osm0sis/PlayIntegrityFork: Fix Play Integrity <A13... GitHub - MeowDump/Integrity-Box: A toolkit for managing Play ...</a></li>

</ul>
</details>

**Discussion**: Community comments express widespread frustration, with some users reconsidering Volkswagen purchases and others criticizing the broader trend of automotive DRM and privacy-invasive practices. A few commenters also highlight how EU mandates for car modems and intrusive driving aids compound the issue.

**Tags**: `#GrapheneOS`, `#Volkswagen`, `#Android security`, `#privacy`, `#API access`

---

<a id="item-11"></a>
## [Why Thinking Aloud Beats Thinking Alone](https://www.thesignalist.io/s/the-dialogue-dividend/) ⭐️ 7.0/10

The article argues that articulating thoughts out loud to another person—rather than silently to oneself—significantly enhances clarity and problem-solving, drawing parallels to the benefits of writing and rubber duck debugging. This insight matters because it offers a low-cost, high-impact technique for improving cognitive performance, especially for software engineers and knowledge workers who regularly tackle complex problems. The article emphasizes that verbalization forces vague impressions into structured sentences, mirroring the mechanism behind rubber duck debugging. Some community commenters argue that speaking aloud to oneself can achieve the same effect, while others note that the key factor is the act of structuring thoughts, not the presence of a listener.

hackernews · kodesko · Jun 17, 13:00

**Background**: Rubber duck debugging is a software engineering technique in which a programmer explains their code step-by-step to an inanimate object (often a rubber duck). The act of verbalizing forces the programmer to think more clearly about each line, often revealing errors that were previously overlooked. This concept extends beyond debugging to any form of problem-solving where articulating ideas helps refine them.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rubber_duck_debugging">Rubber duck debugging - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters offered diverse perspectives: h4kunamata noted that thinking out loud with yourself works just as well. Havoc argued that the key is the forced structuring into sentences, not the external listener. jboggan shared a past attempt to build an LLM-based rubber ducking tool, while dh2022 cited Einstein thanking a colleague for helping him clarify concepts, reinforcing the article's thesis.

**Tags**: `#rubber-duck-debugging`, `#cognition`, `#communication`, `#problem-solving`, `#thought-articulation`

---

<a id="item-12"></a>
## [Robot Game Reveals AI Model Trade-offs in Cost and Safety](https://openrouter.ai/blog/insights/royale-last-agent-standing/) ⭐️ 7.0/10

A blog post on OpenRouter describes a contest where AI models control robots in a 'Last Agent Standing' game, comparing Claude, Grok, and DeepSeek V4 Flash. DeepSeek V4 Flash emerges as the most cost-efficient, while Claude exhibits excessive safety hesitation and Grok is more direct. This comparison highlights practical trade-offs between cost, safety, and action speed for real-time AI applications like robotics, impacting developers' model choices and deployment strategies. DeepSeek V4 Flash has 284B parameters with 13B activated, supports a 1 million token context, and is optimized for fast inference at lower cost. The test ran 30 games costing $482 total, whereas frontier-tier models would have cost $3,000 for the same number of games.

hackernews · Usu · Jun 17, 21:00

**Background**: The blog post conducts a 'Royale' game where AI models drive robots to survive in a competitive arena. DeepSeek V4 Flash is a Mixture-of-Experts model designed for high-throughput tasks, while Claude by Anthropic is known for safety alignment sometimes leading to over-caution, and Grok by xAI tends to be more direct in its responses.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-flash/modelcard">deepseek-v4-flash Model by Deepseek-ai | NVIDIA NIM</a></li>
<li><a href="https://deepseeksr1.com/v4-flash/">DeepSeek-V4-Flash | Fast, Low-Cost AI for Real-Time Apps</a></li>

</ul>
</details>

**Discussion**: Commenters note DeepSeek's strong coding performance and cost efficiency, appreciate Grok's directness, and criticize Claude's verbose safety reasoning. One comment highlights that Grok-4.1-fast was silently rerouted to 4.3 with increased pricing, calling it a bad practice.

**Tags**: `#AI models`, `#model comparison`, `#cost efficiency`, `#robotics`, `#gaming`

---

<a id="item-13"></a>
## [Human Connection as an AI-Proof Moat](https://ghostinthedata.info/posts/2026/2026-06-13-human-connection-moat/) ⭐️ 6.0/10

An opinion piece argues that authentic human connection provides a sustainable competitive advantage that AI cannot replicate, illustrating the point with a restaurant that kept its reservation team after switching to online booking. This challenges the prevailing narrative that AI will inevitably replace human roles in customer service, suggesting that businesses may sacrifice long-term loyalty by prioritizing efficiency over genuine relationships. The restaurant owner moved to an online booking system but repurposed the reservation team for personalized guest outreach, demonstrating a hybrid approach combining AI efficiency with human warmth.

hackernews · speckx · Jun 17, 17:14

**Background**: The concept of a 'competitive moat' comes from investing, referring to a business's durable advantage that protects it from competitors. In customer service, AI chatbots and automation have become widespread, often prioritizing cost savings over service quality. This piece argues that genuine human connection remains a moat that AI cannot easily bridge.

**Discussion**: Comments are sharply divided: some readers agree with the post's premise, while others express frustration with transactional interactions that fail to provide basic service. One skeptic notes the irony of an AI-written post advocating for human connection, and another argues that the restaurant's successful hybrid model may not scale universally.

**Tags**: `#AI`, `#human connection`, `#customer service`, `#business strategy`, `#competitive moat`

---