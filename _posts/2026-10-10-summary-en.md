---
layout: default
title: "Horizon Summary: 2026-10-10 (EN)"
date: 2026-10-10
lang: en
---

> From 42 items, 9 important content pieces were selected

---

**Technology News**
1. [Cloudflare Acquires Deno, Runtime Support to End in One Year](#item-tech-news-1) ⭐️ 8.0/10
2. [Telegram Desktop Flaw Allowed One-Click File Theft via Malicious Links](#item-tech-news-2) ⭐️ 8.0/10
3. [Carrier-Explode Archives and Decodes Phone Carrier Settings](#item-tech-news-3) ⭐️ 7.0/10
4. [YouTuber Built Flock-Style Camera to Track Police, Got a Visit](#item-tech-news-4) ⭐️ 7.0/10
5. [Amazon Builds 1000th Satellite, Eyes Space Internet by Year-End](#item-tech-news-5) ⭐️ 7.0/10
6. [JetBrains Releases Open-Source Coding Model Mellum2.1](#item-tech-news-6) ⭐️ 7.0/10

**Financial News**
1. [Telecom carriers slide and tower stocks rise on Starlink Mobile expansion](#item-finance-news-1) ⭐️ 7.0/10
2. [SpaceX spectrum deal and Delta earnings miss drive premarket stock moves](#item-finance-news-2) ⭐️ 7.0/10
3. [Apple reportedly cuts iPhone 18 Pro component orders by 15% amid weak demand](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Cloudflare Acquires Deno, Runtime Support to End in One Year](https://deno.com/blog/cloudflare) ⭐️ 8.0/10

Cloudflare has acquired Deno, the JavaScript/TypeScript runtime and developer tools company. Deno says it will support the Deno runtime for one more year with monthly releases containing bug fixes and security updates, after which it will end its development of the runtime. Deno will remain open source, and the company welcomes others who want to continue its development. If no one else picks up development, the Deno runtime will no longer be officially supported. The move is seen as a major consolidation in the JavaScript/TypeScript ecosystem.

hackernews · ilreb · Oct 9, 13:03 · [Discussion](https://news.ycombinator.com/item?id=50019911)

**「Background」** Deno is a JavaScript and TypeScript runtime created by Ryan Dahl, the original creator of Node.js, with a focus on security and web-standard APIs. Cloudflare operates the Workers serverless platform, and Deno&\#x27;s team previously built Celld, a self-hosted take on Cloudflare Workers. With the acquisition, Cloudflare is absorbing the Deno team while the Deno runtime itself is being wound down.

**「Impact」** Deno runtime users and downstream projects have a one-year transition window with monthly maintenance releases before official development ends, and future support depends on community-led forks.

**「Community Discussion」** Commenters express disappointment and view the deal as an acquihire that effectively shuts down Deno development, with some attributing decline to a shift toward npm compatibility over the original clean design. Others note a broader consolidation trend across developer tooling, citing recent acquisitions such as Cursor by SpaceX, Astral/uv by OpenAI, Bun by Anthropic, Astro.js and VoidZero by Cloudflare, NuxtLabs by Vercel, and Hugging Face by NVIDIA.

<details><summary>References</summary>
<ul>
<li><a href="https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl/">Cloudflare acquires Node.js creator’s startup that... - The New Stack</a></li>

</ul>
</details>

**Tags**: `#deno`, `#cloudflare`, `#javascript`, `#runtime`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [Telegram Desktop Flaw Allowed One-Click File Theft via Malicious Links](https://telegram.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop versions below 7.2.9 contained a severe arbitrary file theft vulnerability tracked as CVE-2026-107181. A user clicking a malicious tg:// link could have local files stolen without confirmation. The flaw stemmed from an unescaped semicolon in the link being treated as a separate IPC command, and combined with the interpret: handler it allowed theft of documents, browser sessions, SSH keys, and encrypted wallets. The issue was fixed in version 7.2.9, and users are advised to upgrade immediately, be cautious of suspicious tg:// links, and enable a local password.

telegram · zaihuapd · Oct 9, 09:51

**「Background」** Telegram Desktop uses custom tg:// URI schemes and inter-process communication \(IPC\) to handle deep links. In affected versions, semicolons in these links were not escaped, allowing an attacker to inject an additional IPC command alongside the intended action.

**「Impact」** Users of Telegram Desktop below 7.2.9 who click a malicious tg:// link could have arbitrary local files exfiltrated without confirmation, making immediate upgrade to version 7.2.9 or later the key mitigation.

**Tags**: `#security`, `#telegram`, `#vulnerability`, `#desktop-applications`, `#CVE`

---

<a id="item-tech-news-3"></a>
### [Carrier-Explode Archives and Decodes Phone Carrier Settings](https://carrierexplode.com/) ⭐️ 7.0/10

Carrier-Explode is a side project by simplyalec that continuously archives carrier settings for iPhone, Pixel, and Galaxy devices, along with decoders and explanations for common baseband configurations. The tool has already proven useful for enthusiast groups, including during discussions of the AT&amp;T iPhone 18 Pro Max lockup issue, where it showed that AT&amp;T/Apple disabled 5G Standalone mode, possibly to prevent hardware damage on affected units. The project still has work to do in checking assumptions, but its comprehensive, continuously updated archive fills a niche for understanding carrier-driven behavior across major phone brands.

hackernews · simplyalec · Oct 9, 18:10 · [Discussion](https://news.ycombinator.com/item?id=50024499)

**「Carrier settings and why they matter」** Carrier settings are configuration bundles embedded in phone firmware that control network features such as APNs, VoLTE, Wi-Fi Calling, and 5G mode availability, and they vary by operator and device family. carrier-explode archives these settings from iPhone, Pixel, and Galaxy firmware releases and presents decoded, comparable fields, making it easier to see what a specific carrier enables or disables on each platform. The project includes a web interface and a free JSON API, and its usefulness depends on the accuracy of its decoders.

**「Impact」** For affected AT&amp;T iPhone 18 Pro Max users, installing iOS 27.0.1 and a carrier settings update should prevent the lockup issue from occurring in the first place, according to Apple.

**「Community Discussion」** Commenters confirmed the tool was linked from MacRumors during AT&amp;T iPhone 18 Pro Max lockup reporting and showed the carrier disabled 5G Standalone mode, possibly to prevent a bug from destroying hardware on one batch of phones. Users also appreciated seeing operators beyond the US, discussed carrier disabling of Personal Hotspot, and suggested contributing applicable data to the GNOME mobile-broadband-provider-info project.

<details><summary>References</summary>
<ul>
<li><a href="https://carrierexplode.com/">iPhone, Pixel and Galaxy carrier settings, decoded · carrier ...</a></li>
<li><a href="https://support.apple.com/en-us/109324">Manually update carrier settings on your iPhone or iPad How to Update AT&amp;T Carrier Settings on iPhone 18 Pro Max ... Enable 5G Standalone on iPhone: Toggle &amp; Fixes - unanswered.io iPhone 18 Pro Max AT&amp;T Users: Update to iOS 27.0.1 and New ... Apple iPhone 18 Pro Max - Checking if your phone is carrier ...</a></li>

</ul>
</details>

**Tags**: `#mobile`, `#carrier-settings`, `#reverse-engineering`, `#baseband`, `#tooling`

---

<a id="item-tech-news-4"></a>
### [YouTuber Built Flock-Style Camera to Track Police, Got a Visit](https://gizmodo.com/youtuber-says-cops-paid-him-a-visit-after-he-built-flock-style-camera-to-track-cops-2000824306) ⭐️ 7.0/10

A YouTuber built a Flock-style automated license plate reader \(ALPR\) camera to track police vehicles. Afterward, police visited him, sparking a broader debate about surveillance, privacy, and the legality of ALPR systems. The project reverses the typical Flock deployment, in which law enforcement searches vehicle locations. The incident highlights tension between public oversight and restrictions on location tracking.

hackernews · gumby · Oct 9, 21:06 · [Discussion](https://news.ycombinator.com/item?id=50026555)

**「Background」** Flock Safety operates automated license plate recognition \(ALPR\) cameras that capture vehicle plates, timestamps, and locations, and are widely used by police departments and neighborhoods for investigations; this has prompted privacy debates over mass location tracking. The incident involves a YouTuber who built his own Flock-style camera to record police vehicles&\#x27; plates and movement, turning the surveillance approach back on law enforcement, after which officers reportedly visited him.

**「Impact」** The incident demonstrates that building an ALPR-style camera to track law enforcement can lead to direct police contact, reinforcing legal and practical risks for reverse-surveillance projects.

**「Community Discussion」** Commenters debated whether tracking police is equivalent to Flock&\#x27;s law-enforcement searches, with some arguing that no one—including government—should run plate readers and others citing New Hampshire&\#x27;s law requiring deletion of non-hit plate images within three minutes. Others proposed accountability projects like OpenFlock to track city council members who approved Flock cameras.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/privacy/youtuber-flock-surveillance-police/">YouTuber tracks cops with Flock - Style camera | Cybernews</a></li>
<li><a href="https://san.com/cc/he-built-his-own-flock-style-camera-to-track-police-the-police-didnt-like-it/">He built his own Flock - style camera to track police. The police...</a></li>

</ul>
</details>

**Tags**: `#surveillance`, `#privacy`, `#ALPR`, `#law enforcement`, `#technology policy`

---

<a id="item-tech-news-5"></a>
### [Amazon Builds 1000th Satellite, Eyes Space Internet by Year-End](https://arstechnica.com/space/2026/10/amazon-builds-1000th-satellite-is-weeks-away-from-space-internet-rollout/) ⭐️ 7.0/10

Amazon has manufactured its 1000th satellite at its Kirkland, Washington factory for the Amazon Leo low Earth orbit internet project, putting commercial space internet service weeks away from launch. The company plans to launch the service before the end of the year, with the satellites flying on an upcoming return-to-flight mission of United Launch Alliance’s Vulcan rocket. A second Vulcan rocket is also being prepared to launch additional Amazon Leo satellites in 2026.

telegram · zaihuapd · Oct 9, 04:30

**「Background」** Amazon Leo, formerly Project Kuiper, is Amazon&\#x27;s low Earth orbit satellite internet constellation intended to compete with SpaceX&\#x27;s Starlink. As of April 2026, Amazon had launched 231 Leo satellites across 11 launches and entered enterprise beta on April 8, 2026, targeting a commercial service launch around mid-2026. The company has contracted for 20+ missions in 2026 and 30+ in 2027, with Vulcan Centaur and New Glenn rockets joining the launch manifest.

**「Impact」** Amazon&\#x27;s 1,000-satellite milestone and nearing commercial launch make Amazon Leo a direct satellite broadband rival to Starlink, which already operates over 10,000 satellites, likely increasing competitive pressure on pricing and service availability for consumers while Amazon Leo still trails in deployment scale.

<details><summary>References</summary>
<ul>
<li><a href="https://orbitalradar.com/satellite-internet/kuiper-launch-schedule">Amazon Kuiper Launch Schedule 2026 — Next Missions</a></li>
<li><a href="https://keeptrack.space/deep-dive/amazon-leo-progress-2026">Amazon Leo Satellites in Orbit, Timeline and Service Date ...</a></li>
<li><a href="https://thenextweb.com/news/amazon-leo-satellite-internet-mid-2026">Amazon Leo targets mid-2026 commercial launch as ... - TNW</a></li>
<li><a href="https://orbitalradar.com/satellite-internet/starlink-vs-kuiper">Starlink vs Amazon Kuiper: Speed, Price &amp; Coverage 2026</a></li>
<li><a href="https://satspeedcheck.com/blog/project-kuiper-vs-starlink/">Project Kuiper vs Starlink: Amazon&#x27;s Satellite Internet ...</a></li>

</ul>
</details>

**Tags**: `#satellite-internet`, `#amazon`, `#leo-satellites`, `#broadband`, `#tech-industry`

---

<a id="item-tech-news-6"></a>
### [JetBrains Releases Open-Source Coding Model Mellum2.1](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 7.0/10

JetBrains announced Mellum2.1, an open-source coding model with 12 billion parameters using a mixture-of-experts architecture and 2.5 billion active parameters. It is released under the Apache 2.0 license and trained with real-environment reinforcement learning, enabling it to explore codebases, edit files, and inspect modifications. The model is intended for locally running coding agents, and its weights are available on Hugging Face. This provides developers with a permissively licensed option for agentic coding tasks without relying on cloud-only services.

telegram · zaihuapd · Oct 9, 07:30

**「Background」** Mixture-of-experts \(MoE\) models activate only a subset of parameters per token, reducing inference cost compared to dense models. Real-environment reinforcement learning trains the model by interacting with actual code repositories and tooling rather than static datasets, improving its ability to handle multi-step agent tasks. The Apache 2.0 license permits commercial use, modification, and redistribution.

**「Impact」** Developers and organizations building local coding agents can now use a permissively licensed, lower-footprint model capable of repository exploration and file editing, potentially reducing dependence on closed or cloud-only coding assistants.

**Tags**: `#open-source`, `#coding-agents`, `#large-language-model`, `#JetBrains`, `#AI`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Telecom carriers slide and tower stocks rise on Starlink Mobile expansion](https://www.cnbc.com/2026/10/09/stocks-making-the-biggest-moves-midday-tmus-vz-t-cci-teva.html) ⭐️ 7.0/10

T-Mobile shares fell 13%, and AT&amp;T and Verizon each fell 10%, after SpaceX moved to boost its Starlink Mobile service. Crown Castle rose 12%, SBA Communications added 6%, and American Tower advanced almost 8%.

rss · CNBC Finance · Oct 9, 18:57

**「Background」** The midday roundup also highlighted managed-care stock swings after CMS released its 2027 Medicare Advantage Star Ratings: Humana gained 12% and Alignment Healthcare dropped almost 14%.

**Tags**: `#stocks`, `#telecom`, `#health insurers`, `#earnings`, `#FDA approval`

---

<a id="item-finance-news-2"></a>
### [SpaceX spectrum deal and Delta earnings miss drive premarket stock moves](https://www.cnbc.com/2026/10/09/stocks-making-the-biggest-moves-premarket-dal-spcx-tmus.html) ⭐️ 7.0/10

SpaceX rose 4% premarket after Grain Management announced an agreement to sell its nationwide 800 megahertz spectrum portfolio to SpaceX, a deal expected to bolster Starlink Mobile. T-Mobile fell 7%, AT&amp;T nearly 6%, and Verizon more than 5% on increased competition concerns, while Delta Air Lines dropped 4% after reporting third-quarter adjusted EPS of $1.72, missing the $1.75 LSEG estimate.

rss · CNBC Finance · Oct 9, 12:31

**「Background」** The Centers for Medicare &amp; Medicaid Services released 2027 Medicare Advantage Star Ratings, sending Humana up 14% and Alignment Healthcare down 23%.

**Tags**: `#premarket movers`, `#telecom spectrum`, `#earnings`, `#Medicare Star Ratings`, `#stock market`

---

<a id="item-finance-news-3"></a>
### [Apple reportedly cuts iPhone 18 Pro component orders by 15% amid weak demand](https://www.forbes.com/sites/siladityaray/2026/10/09/apple-shares-dip-after-report-says-its-cutting-iphone-18-pro-component-orders/) ⭐️ 7.0/10

Apple has reportedly cut component orders for the iPhone 18 Pro and Pro Max by at least 15% this month because demand is weaker than expected, and its shares fell more than 1.6% in premarket trading.

telegram · zaihuapd · Oct 9, 13:31

**「Background」** The iPhone 18 Pro launched last month at a starting price of $1,199, $100 more than the previous generation, while the standard iPhone 18 was delayed to early next year; it is unclear whether the iPhone Duo foldable, due October 23, is affected.

**Tags**: `#Apple`, `#iPhone`, `#supply chain`, `#demand`, `#stock market`

---