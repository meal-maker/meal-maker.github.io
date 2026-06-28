---
layout: default
title: "Horizon Summary: 2026-05-03 (EN)"
date: 2026-05-03
lang: en
---

> From 17 items, 8 important content pieces were selected

---

1. [VS Code PR Defaults Co-Authored-by Copilot to All Commits](#item-1) ⭐️ 9.0/10
2. [VideoLAN Launches Dav2d: Fastest AV2 Decoder](#item-2) ⭐️ 8.0/10
3. [Tesla Owner Wins $10k Over FSD Lies, Company Appeals](#item-3) ⭐️ 8.0/10
4. [Six-Year Evolution of Custom Map App on Apple Watch](#item-4) ⭐️ 7.0/10
5. [Long-Awaited NetHack 5.0.0 Released](#item-5) ⭐️ 7.0/10
6. [macOS VM Performance: Minimal Configs Still Work Well](#item-6) ⭐️ 7.0/10
7. [Ladybird Browser April 2026 Newsletter Details Fixes and Progress](#item-7) ⭐️ 6.0/10
8. [New DO_NOT_TRACK Shell Script Aggregates Telemetry Opt-Out Env Vars](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [VS Code PR Defaults Co-Authored-by Copilot to All Commits](https://github.com/microsoft/vscode/pull/310226) ⭐️ 9.0/10

A pull request to Visual Studio Code (vscode#310226) changed the default setting for adding 'Co-Authored-by: Copilot' to all git commits, even when Copilot was not actually used. This change undermines developer trust by falsifying commit authorship records, which may have legal implications for version control history integrity and misrepresent Copilot usage statistics. The PR's configuration schema default was set to 'all', but the runtime fallback still used 'off', causing inconsistency. The community criticized the change as a breach of trust and record falsification.

hackernews · indrora · May 2, 19:57

**Background**: Git supports 'Co-Authored-by' commit trailers to credit multiple authors on a single commit. GitHub uses this to display multiple contributors. Historically, these trailers are added manually or with explicit intent; defaulting them without actual co-authorship breaks the convention.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors">Creating a commit with multiple authors - GitHub Docs</a></li>
<li><a href="https://stackoverflow.com/questions/58525836/git-magic-keywords-in-commit-messages-signed-off-by-co-authored-by-fixes">github - Git magic keywords in commit messages (Signed-off-by...)</a></li>

</ul>
</details>

**Discussion**: The community reacted strongly, with many comments calling the move a breach of trust, record falsification, and a dangerous precedent. One comment noted that even Copilot's own bot commented on the PR suggesting reverting the change, but was ignored.

**Tags**: `#VS Code`, `#GitHub Copilot`, `#Git`, `#Ethics`, `#Microsoft`

---

<a id="item-2"></a>
## [VideoLAN Launches Dav2d: Fastest AV2 Decoder](https://code.videolan.org/videolan/dav2d) ⭐️ 8.0/10

VideoLAN has announced dav2d, a fast and portable AV2 video decoder, claiming it to be the fastest AV2 decoder on all platforms. AV2 is the next-generation video codec from the Alliance for Open Media, offering up to 30% bitrate savings over AV1, and dav2d's high performance could accelerate the adoption of AV2 for streaming, broadcasting, and software playback. Dav2d is designed to be small, portable, and very fast, following the success of VideoLAN's dav1d decoder for AV1. The AV2 specification is still in draft status as of May 2026, with final release expected by late 2025.

hackernews · dabinat · May 2, 17:32

**Background**: AV2 is an open, royalty-free video coding format developed by the Alliance for Open Media as the successor to AV1. It aims to deliver superior compression efficiency with significant improvements in intra-frame prediction, partitioning, and inter-frame modes. VideoLAN previously created dav1d, a highly optimized AV1 decoder, and dav2d follows a similar philosophy to provide the fastest possible software decoding for AV2.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://av2.aomedia.org/">AV2 Specification</a></li>

</ul>
</details>

**Discussion**: The community is enthusiastic about dav2d's potential but expresses concern about encoder maturity, noting that it took a long time for SVT-AV1 to become usable. Some users ask for quantitative comparisons between AV2 and AV1, while others highlight the growing friction of web access (bot checks, cookies).

**Tags**: `#AV2`, `#video codec`, `#decoder`, `#VideoLAN`, `#performance`

---

<a id="item-3"></a>
## [Tesla Owner Wins $10k Over FSD Lies, Company Appeals](https://electrek.co/2026/05/02/this-tesla-owner-won-10k-in-court-for-teslas-fsd-lies-tesla-is-still-fighting-him/) ⭐️ 8.0/10

A Tesla owner won a court judgment of $10,672.88, the full amount he paid for Full Self-Driving (FSD), after proving Tesla misrepresented the capability of the system. Tesla continues to fight the ruling, appealing the decision. This case sets a potential precedent for consumer protection against misleading claims in autonomous driving technology. If upheld, it could open the door to a flood of similar lawsuits from other Tesla owners who paid for FSD. The awarded amount includes the purchase price of FSD plus taxes and court fees, but notably does not include interest. The owner, identified as Gawiser, repeatedly reported safety issues such as unintended emergency lane departure activations.

hackernews · breve · May 2, 22:45

**Background**: Tesla's Full Self-Driving (FSD) is an advanced driver-assistance system that Tesla has marketed as capable of fully autonomous driving. Critics and regulators have accused Tesla of overpromising and misleading consumers about the system's true capabilities, leading to multiple investigations and lawsuits.

**Discussion**: Commenters highlight that Tesla is likely fighting the case not over the small amount but to avoid setting a legal precedent that could trigger many similar claims. One user shared a personal experience recovering $250,000 under California's lemon law for software issues, while others expressed skepticism that Tesla will actually pay without a public stunt.

**Tags**: `#Tesla`, `#FSD`, `#legal`, `#false advertising`, `#autonomous driving`

---

<a id="item-4"></a>
## [Six-Year Evolution of Custom Map App on Apple Watch](https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/) ⭐️ 7.0/10

Developer David Smith published a detailed blog post recounting the six-year development of a third-party map app for Apple Watch, which relies on pre-rendered custom image tiles to deliver detailed and aesthetically pleasing maps beyond Apple's native capabilities. This story underscores the limitations of Apple's first‑party maps on watchOS and shows how third‑party developers can create superior experiences through creative technical workarounds. It serves as inspiration for developers aiming to push the boundaries of what is possible on Apple Watch. Instead of using dynamic vector rendering like Apple Maps, the app displays static pre‑rendered map image tiles that include custom cartographic details such as hiking trails. This approach achieves superior visual quality but requires separate tile downloads for each zoom level and does not support live updates.

hackernews · valzevul · May 2, 21:14

**Background**: A tiled web map displays a map by seamlessly stitching together many small image files called tiles. Pre‑rendered tile sets are generated in advance as static images, unlike dynamically rendered maps that fetch vector data on the fly. On Apple Watch, the standard MapKit has limited support for custom overlays, so developers often use SpriteKit or other rendering engines to display custom tile images. David Smith even hired a professional cartographer to design the tiles for his app.

<details><summary>References</summary>
<ul>
<li><a href="https://www.david-smith.org/blog/2026/04/29/maps-on-watchos/">Six Years Perfecting Maps on watchOS - David Smith, Independent iOS Developer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tiled_web_map">Tiled web map - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/60544111/how-to-make-scrollable-and-zoomable-custom-map-on-apple-watch">swift - How to make scrollable and zoomable custom map on Apple Watch? - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: Community comments expressed disappointment that Apple still lacks a first‑party hiking and topography map on the Apple Watch, especially for the Ultra model. Many praised the developer's attention to detail and the clever use of static tiles, while also noting the trade‑offs (separate downloads, no live updates). A user highlighted the personal touch of commissioning a cartographer, which was seen as a cool and dedicated move.

**Tags**: `#watchOS`, `#maps`, `#app development`, `#design`, `#Apple Watch`

---

<a id="item-5"></a>
## [Long-Awaited NetHack 5.0.0 Released](https://nethack.org/v500/release.html) ⭐️ 7.0/10

NetHack 5.0.0 has been officially released, replacing the decades-old yacc/lex-based level and dungeon compilers with Lua scripts, and introducing other major architectural changes. This release marks a major modernization of one of the oldest active roguelike games, improving moddability and maintainability while preserving its legendary gameplay, reigniting interest in the roguelike community. NetHack 5.0.0 embeds Lua 5.4.8, eliminating the need for external Lua installations, and existing saved games or bones files are incompatible. The build system now processes dungeon and level data at runtime via Lua.

hackernews · rsaarelm · May 2, 18:03

**Background**: Yacc (Yet Another Compiler-Compiler) and Lex are classic Unix tools for generating parsers and lexers from formal grammars, used in NetHack since its early days to compile level and dungeon descriptions. Replacing them with Lua scripts moves the data processing from compile-time to runtime, making it easier for developers and modders to modify game content without recompilation. Lua, a lightweight scripting language dating back to 1993, has long been used in game development for modding and configuration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yacc">Yacc - Wikipedia</a></li>
<li><a href="https://deepwiki.com/NetHack/NetHack/5-build-system">Build System | NetHack/NetHack | DeepWiki</a></li>
<li><a href="https://news.ycombinator.com/item?id=47988776">NetHack 5.0.0 | Hacker News</a></li>

</ul>
</details>

**Discussion**: The community expressed nostalgia, with one player recalling a 17-year-old save file now incompatible. There was appreciation for the technical decision, though some noted it marks the end of an era. Others expressed hope that clients like the 3D viewer will be updated for 5.0.0.

**Tags**: `#NetHack`, `#roguelike`, `#Lua`, `#game development`, `#retro computing`

---

<a id="item-6"></a>
## [macOS VM Performance: Minimal Configs Still Work Well](https://eclecticlight.co/2026/05/02/how-fast-is-a-macos-vm-and-how-small-could-it-be/) ⭐️ 7.0/10

A performance exploration of macOS virtual machines shows that reducing cores and memory to as low as 2 virtual cores and 4 GB of RAM still allows the VM to handle lightweight tasks smoothly, with memory usage scaling down proportionally. This matters for Mac developers and users who run VMs for lightweight tasks, as it demonstrates that they can allocate fewer resources to save host memory while still maintaining acceptable performance. It also highlights important trade-offs, such as the lack of GPU compute acceleration in macOS VMs. Each virtual core consumes additional memory for page cache and concurrency handling, so reducing cores also reduces memory usage. However, the virtio-gpu layer in macOS VMs only passes through graphics GPU, not compute GPU, making PyTorch GPU acceleration impossible, and Docker via colima remains relatively inefficient.

hackernews · moosia · May 2, 09:30

**Background**: macOS virtualization on Apple Silicon uses the Virtualization.framework to run macOS guests. VM performance depends on allocated virtual CPUs and memory, but graphics acceleration is limited to basic display output—compute GPU features like those needed for machine learning are not passed through. This article explores how low resource allocations can still support lightweight tasks effectively.

**Discussion**: Community comments largely agree with the findings, noting that memory usage scales with core count. Some users lament the inability to use PyTorch GPU acceleration in VMs due to compute GPU not being passed through. Others share real-world experiences: colima+Docker is found painful but usable, and a link to trycua/lume is offered as an alternative. One commenter questions whether full allocated memory would be consumed once applications are launched inside the VM.

**Tags**: `#macOS`, `#virtualization`, `#performance`, `#VM`, `#Mac`

---

<a id="item-7"></a>
## [Ladybird Browser April 2026 Newsletter Details Fixes and Progress](https://ladybird.org/newsletter/2026-04-30/) ⭐️ 6.0/10

The April 2026 newsletter for Ladybird browser reports multiple bug fixes and improvements, including CSS Doom fixes and better compatibility for sites like Strava and Reddit. These incremental improvements demonstrate Ladybird's steady progress toward an alpha release later in 2026, showing that a truly independent, non-Chromium browser is becoming more viable for everyday use. The newsletter notes fixes such as making `Navigator.getBattery` throw the correct error type, which enabled Strava login to work, along with improvements to Reddit rendering.

hackernews · richardboegli · May 2, 20:46

**Background**: Ladybird is an open-source web browser developed by the non-profit Ladybird Browser Initiative, originally part of SerenityOS but now a standalone project. It is built from scratch using its own engine, not based on Chromium or Firefox. An alpha release is planned for 2026, beta in 2027, and stable in 2028, funded entirely through donations from sponsors like Cloudflare, FUTO, Shopify, and 37signals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_browser">Ladybird browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_(web_browser)">Ladybird (web browser) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community reaction is positive, with commenters noting Ladybird is becoming 'pretty usable' and comparing its update style to gaming emulator updates. One commenter highlighted that Reddit is already working in Ladybird, while another discussed a no-JavaScript browser alternative built with Dioxus. There was also a minor discussion about a sponsor's background.

**Tags**: `#browser`, `#open-source`, `#ladybird`, `#software engineering`

---

<a id="item-8"></a>
## [New DO_NOT_TRACK Shell Script Aggregates Telemetry Opt-Out Env Vars](https://donottrack.sh/) ⭐️ 6.0/10

A new shell script at donottrack.sh aggregates dozens of telemetry opt-out environment variables (e.g., DOTNET_CLI_TELEMETRY_OPTOUT, HF_HUB_DISABLE_TELEMETRY) into a single DO_NOT_TRACK environment variable, aiming to simplify user privacy controls. This initiative revives the long-standing debate over telemetry opt-out defaults and the effectiveness of a single 'do not track' signal, especially given the failure of the similar DNT browser header. If widely adopted, it could simplify privacy management for users, but also raises concerns about creating a honeypot for trackers to ignore. The DO_NOT_TRACK variable is not a standard; it is a community-driven aggregation that requires software authors to explicitly support it. The script currently covers environment variables from tools like .NET SDK, Hugging Face, n8n, and others, but adoption remains minimal.

hackernews · RubyGuy · May 2, 17:40

**Background**: Many software tools and libraries collect telemetry data by default to improve their products, but provide environment variables to opt out. However, each tool uses a different variable name, making it cumbersome for users to disable telemetry across all tools. The DO_NOT_TRACK environment variable aims to provide a single, universal opt-out signal that tools can check. This concept echoes the earlier 'Do Not Track' HTTP header, which was widely ignored by websites and eventually deprecated.

<details><summary>References</summary>
<ul>
<li><a href="https://donottrack.sh/">Do _ not _ track</a></li>
<li><a href="https://docs.telemetry-kit.dev/privacy">Privacy Controls | telemetry-kit Docs</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the initiative's effectiveness. Several users draw parallels to the failed DNT browser header, predicting the same fate. Others warn that the script could become a honeypot, allowing trackers to specifically target users who set DO_NOT_TRACK. A user also shares frustration with the difficulty of actually stopping telemetry in the Python transformers library, highlighting the real-world challenge this initiative attempts to address.

**Tags**: `#telemetry`, `#privacy`, `#environment-variables`, `#opt-out`, `#open-source`

---