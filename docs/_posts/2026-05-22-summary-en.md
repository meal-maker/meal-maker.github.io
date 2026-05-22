---
layout: default
title: "Horizon Summary: 2026-05-22 (EN)"
date: 2026-05-22
lang: en
---

> From 24 items, 13 important content pieces were selected

---

1. [Freenet Relaunched with WebAssembly Decentralized Apps](#item-1) ⭐️ 8.0/10
2. [Seattle Shield: Police-Private Intelligence Network Raises Privacy Concerns](#item-2) ⭐️ 8.0/10
3. [Google Antigravity Rebranding Causes Developer Backlash](#item-3) ⭐️ 8.0/10
4. [Interactive Star Map of 1.8 Billion GAIA DR3 Stars](#item-4) ⭐️ 7.0/10
5. [Blog Migrated from Ubuntu 16.04 to FreeBSD After 10 Years](#item-5) ⭐️ 7.0/10
6. [Developer Indexes Year of Video Locally Using Gemma4-31B on MacBook](#item-6) ⭐️ 7.0/10
7. [Python 3.15's Overlooked Features: Lazy Imports, Sync Primitives, Counter Ops](#item-7) ⭐️ 7.0/10
8. [Lost Trinity Nuclear Test Images Restored with Unprecedented Clarity](#item-8) ⭐️ 7.0/10
9. [Waymo pauses Atlanta service over flood incidents](#item-9) ⭐️ 7.0/10
10. [Kagi Search Benefits Users with Low Vision](#item-10) ⭐️ 6.0/10
11. [Spotify to Reserve Concert Tickets for Superfans](#item-11) ⭐️ 6.0/10
12. [BBEdit 16: A New Major Release of a Classic macOS Text Editor](#item-12) ⭐️ 6.0/10
13. [Wealth is Concentrating Towards AI](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Freenet Relaunched with WebAssembly Decentralized Apps](https://freenet.org/) ⭐️ 8.0/10

The new Freenet, a ground-up redesign of the original peer-to-peer network, launched in December 2024 with WebAssembly contracts that define state validation and synchronization, along with early applications like River (decentralized group chat) and Delta (decentralized CMS). This redesign revives a historic peer-to-peer project with modern technology, enabling truly decentralized applications that can be downloaded from the network and run in browsers, reducing reliance on centralized servers and big tech infrastructure. Each contract must define a commutative merge operation, allowing state updates to spread through the network like a virus and achieve global consistency in seconds. Applications run client-side and connect to a local Freenet peer via WebSocket, not to a remote API.

hackernews · sanity · May 21, 14:34

**Background**: The original Freenet (now Hyphanet) was an early 2000s peer-to-peer network focused on anonymous communication and censorship resistance. The new version reimagines it as a global decentralized key-value store where keys are WebAssembly contracts. WebAssembly is a binary instruction format that runs near-native speed in browsers and other environments. The commutative merge property is a core concept in Conflict-free Replicated Data Types (CRDTs), enabling eventual consistency without central coordination.

<details><summary>References</summary>
<ul>
<li><a href="https://freenet.org/">Freenet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_censorship_circumvention">Internet censorship circumvention - Wikipedia</a></li>
<li><a href="https://medium.com/@sairaju.atukuri123/crdts-explained-simply-how-distributed-systems-stay-consistent-without-locks-b331a9a2d115">CRDTs Explained Simply: How Distributed Systems Stay... | Medium</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some praise the technical innovation using WebAssembly and CRDT-like merge functions, while others strongly criticize the project governance, claiming the original development team was sidelined by a board decision without prior discussion. Additional technical points include concerns about ghost keys and reputation centralization, as well as suggestions for alternative state synchronization approaches like update logs.

**Tags**: `#p2p`, `#decentralized`, `#webassembly`, `#freenet`, `#distributed-systems`

---

<a id="item-2"></a>
## [Seattle Shield: Police-Private Intelligence Network Raises Privacy Concerns](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) ⭐️ 8.0/10

The Prism Reports investigation revealed that Seattle Shield, a police-run intelligence-sharing network, includes major companies like Amazon, Facebook, and federal agencies such as ICE, raising concerns about mass surveillance and privacy violations. This matters because it highlights the growing integration of private sector surveillance into law enforcement, potentially enabling unchecked monitoring of citizens without proper oversight, and sparks debate on civil liberties in the tech industry. Seattle Shield's stated mission is counterterrorism intelligence sharing, but critics argue it has been used to surveil protests and activists, and some members like Church of Scientology and U.S. Navy have left the network.

hackernews · root-parent · May 21, 17:55

**Background**: Seattle Shield is a local fusion center-like network that facilitates information sharing between the Seattle Police Department and private entities. Such networks are part of broader post-9/11 intelligence infrastructure, but often lack transparency and accountability. The involvement of tech giants and immigration enforcement raises specific concerns about data collection on marginalized communities.

<details><summary>References</summary>
<ul>
<li><a href="https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/">Amazon, Facebook, ICE have access to Seattle police ...</a></li>
<li><a href="https://seattleshield.org/PageMenuSwitch2.aspx?AspxAutoDetectCookieSupport=1">Seattle Shield</a></li>

</ul>
</details>

**Discussion**: Community comments were mixed: some criticized the reporting as sensationalist clickbait, while others expressed concern about enabling surveillance and urged tech workers to resist. A few defended the network as a legitimate business-neighborhood watch program.

**Tags**: `#privacy`, `#surveillance`, `#police`, `#technology-ethics`, `#civil-liberties`

---

<a id="item-3"></a>
## [Google Antigravity Rebranding Causes Developer Backlash](https://www.0xsid.com/blog/antigravity-bait-n-switch) ⭐️ 8.0/10

Google rebranded its Antigravity developer tool, overwriting previous installations and forcing existing users into a disruptive migration process that broke workflows and settings. This bait-and-switch move erodes developer trust in Google's product consistency and highlights the risks of relying on tools that may be abruptly overhauled without regard for existing users. Users reported that the update overwrote the old Antigravity IDE without warning, required manual reconfiguration, and one developer documented a 90-minute migration effort; a community contributor released a Python script to automate restoration on Mac.

hackernews · ssiddharth · May 21, 13:50

**Background**: Google Antigravity is an AI-powered integrated development environment (IDE) that leverages Gemini models to enable agentic software development. It was announced in November 2025 as a platform for delegating development tasks to autonomous AI agents. The recent rebranding appears to have shifted the product's focus, leaving existing users with a broken migration path.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>
<li><a href="https://antigravity.google/">Google Antigravity - Build the new way</a></li>

</ul>
</details>

**Discussion**: User frustration is widespread, with comments describing the rebranding as disorienting and a 'bait and switch.' One developer created a zero-dependency Python script to restore VS Code settings and chat history, while others criticized Google's lack of focus and slow bug fixes compared to other AI labs.

**Tags**: `#Google`, `#developer tools`, `#IDE`, `#bait-and-switch`, `#migration`

---

<a id="item-4"></a>
## [Interactive Star Map of 1.8 Billion GAIA DR3 Stars](https://valhovey.github.io/gaia-mary/) ⭐️ 7.0/10

This project presents an interactive stellar navigation chart built entirely from the ESA Gaia DR3 star catalog, rendering over 1.8 billion stars using a custom Python script. It demonstrates how real astronomical data can be transformed into an immersive visualization, making the vast scale of star catalogs accessible to the public and useful for educational purposes. The chart uses actual GAIA DR3 positions and colors for most stars, though a few bright stars are excluded; planetary and stellar sizes and orbits are not to scale, as noted in community feedback.

hackernews · speleo · May 21, 16:23

**Background**: The Gaia spacecraft, operated by the European Space Agency, has been mapping the Milky Way since 2014. Its Data Release 3 (DR3) provides precise positions, brightnesses, and colors for more than 1.8 billion stars. This project leverages that dataset to generate a skybox for interactive navigation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cosmos.esa.int/web/gaia/dr3">Gaia Data Release 3 (Gaia DR3) - ESA Cosmos</a></li>

</ul>
</details>

**Discussion**: The creator explained the technical process behind the chart. Commenters appreciated the visualization but noted that the sizes and distances of celestial bodies are not to scale, and one user recommended a similar experience in the game Elite Dangerous.

**Tags**: `#astronomy`, `#data visualization`, `#GAIA`, `#python`, `#space`

---

<a id="item-5"></a>
## [Blog Migrated from Ubuntu 16.04 to FreeBSD After 10 Years](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) ⭐️ 7.0/10

The blog owner migrated their decade-old server from Ubuntu 16.04 to FreeBSD, documenting the technical challenges and benefits of moving away from an outdated Linux distribution. This migration story highlights the risks of long-running systems with no updates, and demonstrates FreeBSD as a viable alternative for self-hosting with its clean design and integrated features like ZFS. Ubuntu 16.04 reached end-of-life in April 2021, leaving the server without security updates; the migration involved moving a WordPress blog and ensuring all services continued to run on FreeBSD.

hackernews · speckx · May 21, 18:54

**Background**: FreeBSD is a free and open-source Unix-like operating system descended from the Berkeley Software Distribution (BSD). It is known for its performance, advanced networking, and fully integrated ZFS filesystem. Unlike Linux, FreeBSD develops its kernel and userland in a single source tree, providing a cohesive system.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FreeBSD">FreeBSD - Wikipedia</a></li>
<li><a href="https://www.freebsd.org/">The FreeBSD Project</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar experiences with long-running systems, noting the difficulty of migrating legacy setups. Some praised FreeBSD's simplicity and 'punk rock' feel, while others reported pain points such as debugging logs and firewall configuration. Alternatives like Docker and Caddy were also discussed.

**Tags**: `#FreeBSD`, `#Ubuntu`, `#server migration`, `#self-hosting`, `#Linux`

---

<a id="item-6"></a>
## [Developer Indexes Year of Video Locally Using Gemma4-31B on MacBook](https://blog.simbastack.com/indexed-a-year-of-video-locally/) ⭐️ 7.0/10

A developer successfully indexed one year of personal video footage on a 2021 MacBook using the Gemma4-31B large language model, relying on 50GB of swap memory, and open-sourced the tool at github.com/Simbastack-hq/framedex. This experiment demonstrates that running a 31-billion-parameter model locally for practical tasks like video indexing is feasible even on consumer hardware with limited RAM, highlighting both the potential and the trade-offs of local LLM deployment. The model used was Gemma4-31B, a dense 31-billion-parameter model from Google, and the system relied on heavy swap (50GB) because the MacBook has only 16GB of unified memory. The tool, named Framedex, creates a searchable index of video frames with metadata like faces and locations.

hackernews · asenna · May 21, 14:01

**Background**: Large language models (LLMs) require significant memory to load all their parameters. Consumer laptops like the 2021 MacBook typically have only 16GB of RAM, which is insufficient for a 31B parameter model. To run such a model, the operating system can use swap space on the SSD as virtual memory, but this is slower and can accelerate SSD wear. The Gemma4-31B model is part of Google's open Gemma family designed for various deployment scenarios, from edge devices to workstations.

<details><summary>References</summary>
<ul>
<li><a href="https://build.nvidia.com/google/gemma-4-31b-it">gemma - 4 - 31 b -it Model by Google | NVIDIA NIM</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 is a family of open models , purpose-built for advanced...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Commenters raised concerns about SSD wear due to heavy swapping, noting that 50GB swap is excessive given that a 4-bit quantized Gemma4-31B should be around 19 GiB. Others shared similar experiences running LLMs on old hardware, like a ThinkPad with upgraded memory. The author responded by open-sourcing the tool and outlining plans to integrate the index with video editing in DaVinci Resolve.

**Tags**: `#local LLM`, `#video indexing`, `#Gemma 4`, `#personal archive`, `#practical AI`

---

<a id="item-7"></a>
## [Python 3.15's Overlooked Features: Lazy Imports, Sync Primitives, Counter Ops](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) ⭐️ 7.0/10

A detailed blog post highlights under-the-radar features in Python 3.15, including explicit lazy imports via the lazy keyword, iterator synchronization primitives for threading, and set-like operations (union, intersection, symmetric difference) on collections.Counter objects. The post also clarifies that lazy imports are implemented using PEP 810 after the earlier PEP 690 was rejected. These features improve Python’s performance and expressiveness: lazy imports reduce startup time and memory for CLI tools and large applications, iterator synchronization primitives simplify safe concurrent iteration, and Counter set operations make data analysis more intuitive. The community discussion corrects an example error and adds real-world use cases, helping developers adopt these features correctly. The lazy import syntax uses a new soft keyword 'lazy' before import or from statements, loading modules only when a name is first accessed. Iterator synchronization primitives include methods like acquire() on iterators to safely coordinate threads, complementing existing threading tools. The Counter set operations now support symmetric difference (^) and other set methods, though the blog post's subtraction example (c-d) was corrected by a commenter to show the actual behavior.

hackernews · rbanffy · May 21, 11:10

**Background**: Lazy imports defer module loading until a name is actually used, reducing unnecessary imports and breaking import cycles. They have been discussed for years (PEP 690 was rejected in 2022) and finally accepted as PEP 810 for Python 3.15. Iterator synchronization primitives help avoid race conditions when multiple threads consume a shared iterator. Counter is a dict subclass for counting hashable objects, and in Python 3.15 it gains set operations like union and symmetric difference for combining count data.

<details><summary>References</summary>
<ul>
<li><a href="https://peps.python.org/pep-0690/">PEP 690 – Lazy Imports | peps.python.org</a></li>
<li><a href="https://docs.python.org/3/library/asyncio-sync.html">Synchronization Primitives — Python 3.14.5 documentation</a></li>
<li><a href="https://www.geeksforgeeks.org/python/counters-in-python-set-1/">Python Collections Counter - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: The community was enthusiastic but cautious: one commenter asked whether lazy imports were finally real and another appreciated the iterator synchronization primitives, sharing their own threaded-generator package. A commenter pointed out that Counter's symmetric difference (^) has practical use cases, and another corrected the blog's subtraction example, showing the actual Counter output. There was also a reference to an interview about free-threading improvements, indicating broader interest in Python concurrency.

**Tags**: `#Python`, `#Python 3.15`, `#language features`, `#software engineering`, `#developer tools`

---

<a id="item-8"></a>
## [Lost Trinity Nuclear Test Images Restored with Unprecedented Clarity](https://spectrum.ieee.org/trinity-nuclear-test) ⭐️ 7.0/10

Historians have restored long-lost photographs of the 1945 Trinity nuclear test, revealing unprecedented clarity of the first atomic bomb explosion. This restoration provides a clearer visual record of a pivotal moment in history, allowing researchers and the public to better understand the dawn of the nuclear age. It also sparks discussions about the test's impact on downwinders and the technical challenges of early nuclear photography. The restored images capture the exact moment of the detonation at 5:29:45 a.m. Mountain War Time on July 16, 1945. The article notes that restoration techniques have brought out details previously invisible in the original, degraded negatives.

hackernews · pseudolus · May 21, 11:02

**Background**: The Trinity test was the first detonation of a nuclear weapon, conducted by the United States during World War II as part of the Manhattan Project. The resulting explosion marked the beginning of the nuclear age. Over the decades, the original photographs have deteriorated, but modern digital restoration methods have now recovered lost details. The test site remains a historical landmark, though it still carries radiation concerns.

**Discussion**: Commenters highlighted the historical significance of the Trinity test, with one former teacher noting it as the starting point for a class on contemporary science. Another commenter explored a rabbit hole about the time zone used in the test (Mountain War Time). A third comment brought attention to the downwinder communities affected by the test who were excluded from the Radiation Exposure Compensation Act, sparking discussion on health and environmental justice.

**Tags**: `#history`, `#nuclear science`, `#technology`, `#restoration`, `#photography`

---

<a id="item-9"></a>
## [Waymo pauses Atlanta service over flood incidents](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) ⭐️ 7.0/10

Waymo has paused its autonomous taxi service in Atlanta following multiple incidents where its robotaxis drove into flooded streets. The company also issued a recall of 3,791 robotaxis after a flood detection failure led to a vehicle being swept away. This event underscores a critical limitation of autonomous vehicles: their inability to handle atypical environmental conditions, known as edge cases. It raises questions about the readiness of self-driving technology for widespread deployment and the safety of relying on AI in unpredictable real-world scenarios. According to the NHTSA recall notice, the flaw is a classification error in the software's decision stack that may allow the vehicle to slow and then drive into standing water on higher-speed roadways. Waymo has deployed an over-the-air software update to improve flood detection and response capabilities.

hackernews · mattas · May 21, 16:30

**Background**: Autonomous vehicles rely on sensors and algorithms to navigate, but they struggle with rare or unusual conditions known as edge cases—situations not well represented in training data. Flooded roads are a classic edge case because water depth and road conditions vary widely and are hard to predict. Waymo is considered one of the leaders in self-driving technology, yet this incident shows that even advanced systems have blind spots.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kognic.com/articles/edge-cases-autonomous-driving">Edge Cases in Autonomous Driving: Detection and Handling Guide</a></li>
<li><a href="https://www.yankodesign.com/2026/05/15/waymos-self-driving-car-saw-the-flood-and-drove-in-anyway-heres-the-problem-plaguing-every-robotaxi/">Waymo’s Self-Driving Car Saw the Flood and Drove In Anyway. Here’s The Problem Plaguing Every Robotaxi. - Yanko Design</a></li>
<li><a href="https://www.tesevo.com/blogs/tesla-news/waymo-recalls-3-791-robotaxis-after-flood-incident-ota-software-fix-deployed">Waymo Recalls 3,791 Robotaxis After Flood Incident: OTA Software Fix D</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some commenters view the pause as a normal part of real-world testing and an opportunity to improve (e.g., dhbradshaw), while others express skepticism about AI's ability to handle such edge cases after years of development (e.g., etempleton). A few users made humorous comparisons to human behavior, with one noting that the robotaxis have achieved 'human level intelligence' by driving into obvious floods.

**Tags**: `#autonomous vehicles`, `#Waymo`, `#AI safety`, `#real-world testing`, `#edge cases`

---

<a id="item-10"></a>
## [Kagi Search Benefits Users with Low Vision](https://veroniiiica.com/using-kagi-search-with-low-vision/) ⭐️ 6.0/10

A blog post by Veronica with low vision details how Kagi Search's minimalist, ad-free interface significantly improves her search experience, sparking community discussion about accessibility shortcomings in mainstream search engines like Google. This personal account highlights critical accessibility and neurodiversity challenges in default search engine interfaces, and demonstrates that a paid, privacy-focused alternative like Kagi can offer a more usable experience for visually impaired and neurodiverse individuals. Kagi is a paid metasearch engine that aggregates results from other search engines and runs its own crawler called Teclis; the author's own blog is also designed with large fonts, high contrast, and minimal clutter to aid low vision users.

hackernews · speckx · May 21, 19:32

**Background**: Kagi (stylized as kagi) is a paid, ad-free search engine launched by Kagi Inc., headquartered in Palo Alto, California; its name means 'key' in Japanese. Unlike free search engines that rely on ads and tracking, Kagi prioritizes user privacy and high-quality results. Users with low vision often struggle with cluttered search result pages, excessive ads, and poor screen reader compatibility on mainstream search engines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kagi_(search_engine)">Kagi (search engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kagi">Kagi - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed that neurodiverse users face similar challenges with superfluous content, and that Google's search results page is abysmal when read by text-to-speech. One user noted the blog's UI is lovely for distant reading, while another missed Google Maps recommendations. Another user declared Kagi the only product they will 'stan'.

**Tags**: `#accessibility`, `#search engines`, `#Kagi`, `#low vision`, `#user experience`

---

<a id="item-11"></a>
## [Spotify to Reserve Concert Tickets for Superfans](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/) ⭐️ 6.0/10

Spotify announced that it will begin reserving concert tickets for its most loyal listeners, known as superfans, as a measure to combat ticket scalping and improve access to live events. This initiative could fundamentally change how concert tickets are distributed in the music industry, ensuring that genuine fans have a better chance of purchasing tickets at face value while reducing the profits of scalpers and bots. The program ties ticket access directly to users' listening data on Spotify, allowing only verified superfans to gain early or reserved access to tickets, thereby creating a data-driven gatekeeping mechanism.

hackernews · elffjs · May 21, 16:26

**Background**: Concert ticket scalping is a widespread problem where bots and resellers buy large quantities of tickets and resell them at inflated prices, making it difficult for ordinary fans to attend shows. Spotify's move leverages its vast user streaming data to identify and reward its most engaged listeners, offering a potential solution that other platforms may adopt.

**Discussion**: Many commenters expressed support for the idea, with some suggesting alternative anti-scalping methods such as auctions or dynamic pricing. There were also calls for Apple to enter this space, noting that Apple Music already includes concert date information.

**Tags**: `#spotify`, `#concert-tickets`, `#scalping`, `#music-industry`, `#fan-engagement`

---

<a id="item-12"></a>
## [BBEdit 16: A New Major Release of a Classic macOS Text Editor](https://www.barebones.com/products/bbedit/bbedit16.html) ⭐️ 6.0/10

BBEdit 16, a new major version of the long-standing macOS text editor, has been released with a one-time license fee of $60. This release reaffirms Bare Bones Software's commitment to a perpetual license model, contrasting with the industry-wide shift toward subscriptions, and sparks nostalgic appreciation among long-time users while inviting comparisons with modern editors like Zed and CotEditor. BBEdit 16 is an incremental update rather than a groundbreaking shift, maintaining its hallmark extensibility via shell scripts, Python tools, or Rust apps. The price has dropped significantly from $120 in 1998 (about $245 adjusted for inflation) to just $60 today.

hackernews · qaz_plm · May 21, 18:21

**Background**: BBEdit is a text editor for macOS that originated as shareware in the early 1990s, developed by Rich Siegel. It has long been favored by developers and writers for its native Mac performance and powerful text processing capabilities. In recent years, modern editors like Zed—an open-source, Rust-based editor focused on speed—and CotEditor, a lightweight native macOS editor, have emerged as alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zed_(text_editor)">Zed (text editor ) - Wikipedia</a></li>
<li><a href="https://coteditor.com/">CotEditor -Text Editor for macOS</a></li>

</ul>
</details>

**Discussion**: The community response is overwhelmingly nostalgic and appreciative, with users noting the remarkable price drop from $120 to $60 and praising Bare Bones for avoiding subscription pricing. Some users mention switching to other editors like Zed or CotEditor, but still respect BBEdit's extensibility and longevity.

**Tags**: `#BBEdit`, `#text editor`, `#macOS`, `#software pricing`, `#developer tools`

---

<a id="item-13"></a>
## [Wealth is Concentrating Towards AI](http://www.ruanyifeng.com/blog/2026/05/weekly-issue-397.html) ⭐️ 6.0/10

The newsletter observes that stock prices of memory, semiconductor, liquid cooling, and optical communication companies have surged dramatically, with examples like SK Hynix employees receiving average bonuses of 6.1 million RMB and OpenAI buying back $6.6 billion in stock from 600 employees. This trend indicates a massive redistribution of societal wealth towards AI, affecting everyone even if they do not directly use AI, through rising costs of electronics and raw materials, and reduced investment in non-AI industries. The newsletter notes that South Korea's two major memory manufacturers alone pulled the Korean stock market from 2600 to 7600 points in one year. Additionally, the article warns against using large language models for precise medical estimations, showing that AI carb counting results vary wildly across models and trials.

rss · 阮一峰的个人网站 · May 21, 23:58

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked SDRAM interface critical for AI accelerators like GPUs, as it provides high bandwidth for processing large datasets. Liquid cooling and optical communication are key enabling technologies for AI data centers, handling the immense heat and data transfer demands. The surge in these stocks reflects the growing infrastructure investment for AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/27118812779">AI 数据中心液冷未来：直接芯片液冷技术解析 - 知乎</a></li>

</ul>
</details>

**Tags**: `#AI`, `#stock market`, `#technology trends`, `#semiconductors`

---