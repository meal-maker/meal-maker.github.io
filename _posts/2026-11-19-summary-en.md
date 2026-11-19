---
layout: default
title: "Horizon Summary: 2026-11-19 (EN)"
date: 2026-11-19
lang: en
---

> From 43 items, 16 important content pieces were selected

---

**Technology News**
1. [Xint Discloses Five nginx Flaws and Kernel Bug Leading to Root](#item-tech-news-1) ⭐️ 9.0/10
2. [Google Announces Gemini 4 Neon Model](#item-tech-news-2) ⭐️ 8.0/10
3. [Microsoft Ignite 2026 Unveils Seven New Models](#item-tech-news-3) ⭐️ 7.0/10
4. [DNS resolvers are the wrong place to fight piracy](#item-tech-news-4) ⭐️ 7.0/10
5. [Advancing chip design with OpenAI models](#item-tech-news-5) ⭐️ 7.0/10
6. [Genie 4 is now available](#item-tech-news-6) ⭐️ 7.0/10
7. [Show HN: Take Voyager 1 Apart, Down to a Single Memory Chip](#item-tech-news-7) ⭐️ 7.0/10
8. [Daniel Stenberg Questions Whether AI Rust Ports Can Keep Up With Curl](#item-tech-news-8) ⭐️ 7.0/10
9. [WeChat Xiaowei Expands Testing to 30M Daily Users](#item-tech-news-9) ⭐️ 7.0/10
10. [DeepSeek Makes Server-Side Search and Web Scraping Free](#item-tech-news-10) ⭐️ 7.0/10
11. [US Weighs Forcing Firms to Disclose Chinese AI Use](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [Fed October minutes: More rate hikes expected, AI seen as inflation risk](#item-finance-news-1) ⭐️ 8.0/10
2. [Fed’s Waller calls for half-point December rate hike to shock inflation](#item-finance-news-2) ⭐️ 8.0/10
3. [Trump, Xi and Putin gather at APEC in Shenzhen amid extended US-China trade truce](#item-finance-news-3) ⭐️ 7.0/10
4. [Tencent Q3: Revenue misses estimates, AI capex soars, WorkBuddy token use tops China](#item-finance-news-4) ⭐️ 7.0/10
5. [China and South Korea Conclude FTA Services and Investment Follow-Up Negotiations](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Xint Discloses Five nginx Flaws and Kernel Bug Leading to Root](https://nginx2root.com/) ⭐️ 9.0/10

Xint has disclosed a chain of five nginx vulnerabilities plus a Linux kernel flaw, which can be chained to escalate from an nginx visitor to host root. The most severe, CVE-2026-123007, is an HTTP/2 flow-control memory corruption that allows unauthenticated remote code execution in an nginx worker. nginx versions 1.30.7 and 1.31.9, released on November 18, address 10 CVEs, and Rapid7 has published a proof of concept; there are currently no reports of in-the-wild exploitation. Administrators who cannot upgrade should disable public HTTP/2 access as a mitigation.

telegram · zaihuapd · Nov 18, 16:21

**「Background」** NGINX is a widely deployed open-source web server and reverse proxy, and its HTTP/2 support is an optional module that can be disabled when immediate patching is not possible. The NGINX2Root advisory from F5 and AlmaLinux identifies five nginx CVEs, including CVE-2026-123633, CVE-2026-123007, and CVE-2026-123634, fixed in nginx 1.30.7 and 1.31.9. watchTowr&\#x27;s FAQ provides details on affected versions, the fix, and configuration requirements for vulnerable deployments.

**「Operational risk for NGINX deployments with HTTP/2」** NGINX installations with HTTP/2 explicitly enabled are vulnerable to unauthenticated remote code execution via CVE-2026-123007, an integer underflow in HTTP/2 flow-control accounting that allows an attacker to read and overwrite memory, and when chained with other disclosed flaws can lead to full host root compromise. The risk is limited because HTTP/2 is not enabled by default, and according to community reports exploitation may require very high HTTP/2 traffic volume and specific CPU instructions; affected administrators should upgrade to nginx 1.30.7 or 1.31.9 or disable external HTTP/2 immediately.

**「Community Discussion」** Commenters note that HTTP/2 is disabled by default and only about 12% of servers have it enabled, while one user claims exploitation requires 128 GB of HTTP/2 traffic and specific CPU instructions. Others criticize the delay between the open-source fix and public advisory, arguing the simple HTTP/2-disabling workaround could have been communicated earlier.

<details><summary>References</summary>
<ul>
<li>NGINX2Root: Patched nginx packages released | AlmaLinux OS</li>
<li>NGINX2Root: Five Critical NGINX Flaws Expose Web Servers to Remote Code Execution</li>
<li>NGINX2root (CVE-2026-123633) FAQ - watchTowr</li>
<li>Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007 | Wiz Blog</li>
<li>NGINX ( HTTP/2 ) - Critical Remote Code Execution Vulnerability (CVE-2026-123007)</li>

</ul>
</details>

**Tags**: `#nginx`, `#security`, `#CVE`, `#privilege escalation`, `#remote code execution`

---

<a id="item-tech-news-2"></a>
### [Google Announces Gemini 4 Neon Model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 8.0/10

Google has announced Gemini 4 Neon, a new model in its Gemini AI family, according to the item title and linked blog URL. The supplied item does not include the announcement&\#x27;s content, so official technical details, benchmarks, release dates, and compatibility constraints cannot be confirmed from the source. The announcement draws significant discussion on Hacker News, but no official capabilities are available in the provided text.

hackernews · yigitdemirag · Nov 18, 21:34 · [Discussion](https://news.ycombinator.com/item?id=50552424)

**「Background」** Gemini 4 Neon is part of Google&\#x27;s Gemini AI model family, adapted from Gemini 4 Carbon with a combined 1-million-token context window and multimodal inputs including text, images, audio, and video. Google positions it as delivering frontier-level intelligence for complex coding and analysis at lower cost, with claims of three times faster performance than Carbon in some benchmarks.

**「Community Discussion」** Commenters express fatigue with Gemini naming schemes and difficulty mapping model names to use cases; one asks whether naming indicates size class. Some compare Neon to Anthropic&\#x27;s Opus 5.5 and find Opus more human-level, while others note Neon appears faster than Carbon on OpenRouter \(127 vs 46 tokens per second\) and that Carbon remains positioned for long-horizon research reasoning despite Neon&\#x27;s higher overall scores on the AA Index.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">Introducing Gemini 4 Neon</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-4-neon/">Gemini 4 Neon - Model Card — Google DeepMind</a></li>
<li><a href="https://www.neowin.net/news/google-launches-gemini-4-neon-claims-its-three-times-faster-than-carbon/">Google launches Gemini 4 Neon , claims it&#x27;s three times... - Neowin</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#large language models`, `#Google`, `#software engineering`

---

<a id="item-tech-news-3"></a>
### [Microsoft Ignite 2026 Unveils Seven New Models](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 7.0/10

Microsoft used Ignite 2026 to announce seven new models focused on scalable price-performance. The lineup includes MAI Code 2, a coding model that a Hacker News commenter tested and found comparable to Anthropic&\#x27;s Opus or OpenAI&\#x27;s Sol for typical work. The commenter noted Microsoft reportedly built the model from scratch and got it right. The announcement positions Microsoft&\#x27;s new models as cost-efficient alternatives in a competitive AI market.

hackernews · gmays · Nov 18, 16:08 · [Discussion](https://news.ycombinator.com/item?id=50548021)

**「What are MAI models and the Ignite 2026 context」** Microsoft&\#x27;s MAI models are the company&\#x27;s in-house large language models, offered through Azure AI and increasingly compared against OpenAI and Anthropic models on coding and enterprise benchmarks. The Ignite 2026 announcements introduce seven new MAI models, including MAI Code 2 and MAI Code 2 Flash, with performance and cost metrics reported on benchmarks such as DeepSWE 1.1, Terminal Bench 2.1, SWE-Atlas, and FrontierCode v1.1. MAI Code 2 is described as delivering 98% of GPT-6.1 Sol&\#x27;s performance at 40% of the cost, while the Flash variant offers comparable performance to GPT-6 Luna and Claude Haiku 5.5 at 65% and 20% of the cost respectively.

**「Impact」** Developers and enterprises can now use Microsoft&\#x27;s MAI Code 2 and Code 2 Flash coding models, which deliver code-generation performance approaching leading OpenAI and Anthropic models at significantly lower cost.

**「Community Discussion」** Community reaction is mixed: one commenter reports MAI Code 2 performs on par with Opus or Sol, while others criticize the keynote as shallow and urge Microsoft to open-source model weights to win developer trust.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/microsoft-ignite-2026/">Seven new world-class models at scalable price-performance ...</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at scalable ...</a></li>
<li><a href="https://www.linkedin.com/pulse/microsoft-ignite-2026-seven-new-mai-models-chip-your-own-ivana-tilca-hxyef">Microsoft Ignite 2026: Seven New MAI Models, a New Chip, and ...</a></li>
<li><a href="https://mobidevices.com/en/microsoft-mai-code-2">Microsoft releases MAI Code 2 AI model | MobiDevices.com</a></li>
<li><a href="https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/">MAI Code 2 and Code 2 Flash: Everyday coding at... | Microsoft AI</a></li>

</ul>
</details>

**Tags**: `#ai`, `#microsoft`, `#llm`, `#machine-learning`, `#cloud`

---

<a id="item-tech-news-4"></a>
### [DNS resolvers are the wrong place to fight piracy](https://techstackups.com/articles/quad9-leaves-france-dns-blocking/) ⭐️ 7.0/10

Quad9 has withdrawn its DNS resolver service from France rather than comply with DNS-based piracy blocking obligations. The move follows a French court decision requiring DNS-level blocking of content deemed to facilitate copyright infringement. DNS resolvers translate domain names to IP addresses, and using them for content blocking is technically broad because it can affect entire domains and unrelated services beyond the targeted infringement. The withdrawal highlights a policy conflict over whether network infrastructure operators should act as copyright enforcement intermediaries.

hackernews · ritzaco · Nov 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50545958)

**「Background」** Quad9 is a Swiss non-profit foundation that operates a free public DNS resolver, offering both general resolution and cybersecurity filtering. Following a French court ruling that required Quad9 to block domains accused of unauthorized sports broadcasts and imposed daily financial penalties, Quad9 announced it will stop serving users in France on November 24, 2026 rather than comply, highlighting tensions between DNS-level blocking and the role of resolvers.

**「Impact」** Quad9&\#x27;s withdrawal means French users lose access to its DNS resolver, and it exemplifies how DNS-based piracy blocking shifts enforcement burdens onto resolver operators, as Google has separately warned the EU that such blocking is ineffective and causes collateral damage.

**「Community discussion」** Commenters largely criticize DNS-based blocking as an ineffective and potentially speech-suppressing approach, suggesting that better legal purchasing experiences, not infrastructure filtering, would reduce piracy. Some also argue that AI companies have already ingested the IP and question the focus on individual users, while one commenter asks whether the French courts or lawmakers deserve blame.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/">Quad9’s withdrawal from France: A canary in the coal mine</a></li>
<li><a href="https://cyberinsider.com/quad9-to-leave-france/">Quad9 to leave France after court orders piracy-related DNS ...</a></li>
<li><a href="https://www.eff.org/deeplinks/2026/10/french-courts-site-blocking-orders-drive-quad9-out-france">French Court’s Site-Blocking Orders Drive Quad9 Out Of France</a></li>
<li><a href="https://digitalmedusa.org/wp-content/uploads/2025/04/DNS-Resolvers-2025-Final.pdf">DNS - Resolvers -2025-Final</a></li>
<li><a href="https://ipspeed.info/infofeed/news/google-tells-brussels-that-blocking-dns-resolvers-and-vpns-to-fight-piracy-does-more-harm-than-good">Google Tells Brussels That Blocking DNS Resolvers and VPNs to...</a></li>

</ul>
</details>

**Tags**: `#dns`, `#internet-censorship`, `#copyright`, `#network-policy`, `#piracy`

---

<a id="item-tech-news-5"></a>
### [Advancing chip design with OpenAI models](https://openai.com/index/advancing-chip-design-with-our-models/) ⭐️ 7.0/10

OpenAI has reported using its own models to advance chip design, according to the item&\#x27;s analysis summary. The development has prompted discussion about AI-driven electronic design automation and open-source hardware practices, including questions about whether associated RISC-V designs are being shared. A community comment refers to a chip named Jalapeño, though no technical details about it are available in the provided material.

hackernews · vighneshiyer · Nov 18, 17:45 · [Discussion](https://news.ycombinator.com/item?id=50549493)

**「Background」** OpenAI&\#x27;s Jalapeño is the company&\#x27;s first custom inference chip, designed to serve its own model workloads and deployed in pods of 2,048 chips. OpenAI engineers used their frontier models to accelerate and improve the chip design process, an example of applying large language models to electronic design automation \(EDA\). According to one analysis, Jalapeño achieves 1.9× performance per watt compared with NVIDIA Blackwell.

**「Community Discussion」** Comments express concern that AI companies are diversifying into other industries while withholding models and competing with their own customers. Other commenters share practical experience using AI agents to automate analog circuit design and simulation runs, and question the lack of shared RISC-V designs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/advancing-chip-design-with-our-models/">Advancing chip design with OpenAI models | OpenAI</a></li>
<li><a href="https://spectrum.ieee.org/llms-for-chip-design">Jalapeño Shows Power of LLMs for Chip Design - IEEE Spectrum</a></li>
<li><a href="https://www.explainx.ai/blog/openai-jalapeno-chip-llm-inference-broadcom-2026">OpenAI Jalapeño: 1.9× Perf/W vs Blackwell (Aug 2026) | explainx.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#chip design`, `#OpenAI`, `#RISC-V`, `#EDA`

---

<a id="item-tech-news-6"></a>
### [Genie 4 is now available](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 7.0/10

Google DeepMind has announced that its Genie 4 world model is now available to eligible Google AI Ultra subscribers, according to a post on the official Google blog. The announcement describes Genie 4 as a generative world model, but the supplied content does not include specific technical capabilities, performance data, or rollout details. Availability is tied to Google AI Ultra subscription status, with eligibility conditions not fully clarified in the source. The development is significant for AI research and game development, as world models can generate interactive environments. No version numbers, dates, or regional limitations are provided in the source item.

hackernews · leumon · Nov 18, 18:49 · [Discussion](https://news.ycombinator.com/item?id=50550415)

**「Background」** Genie is Google DeepMind&\#x27;s family of generative world models that create interactive, real-time environments from user prompts. Genie 4 is the latest iteration, accessible through Project Genie, the interface where eligible Google AI Ultra subscribers can generate and edit these worlds with newly added real-time audio.

**「Community Discussion」** Commenters expressed confusion over Google&\#x27;s eligibility rules for Genie 4, with reports that workspace accounts are not eligible and UK users may only see Genie 3. Others debated potential negative consequences, questioned the definition of a world model, appreciated DeepMind&\#x27;s research focus, and speculated about future use as a game engine like &quot;Roblox on crack.&quot;

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/">Project Genie update featuring Genie 4</a></li>
<li><a href="https://deepmind.google/models/genie/">Genie 4 — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#generative-ai`, `#world-models`, `#deepmind`, `#game-development`, `#ai-research`

---

<a id="item-tech-news-7"></a>
### [Show HN: Take Voyager 1 Apart, Down to a Single Memory Chip](https://rshekhar.com/voyager/) ⭐️ 7.0/10

An interactive web experience at rshekhar.com/voyager lets users disassemble a detailed 3D model of Voyager 1 down to individual memory chips, including its nuclear battery, data computer, Golden Record cover, and live dish tracking. The site notes that Voyager 1 reached one light-day from Earth today and shows the current positions of both Voyagers, the 24 plutonium spheres inside the radioisotope thermoelectric generator, and how the Golden Record cover explains playback. It also visualizes how a Voyager 1 fault was fixed by radio and links to a four-minute film.

hackernews · raj-shekhar · Nov 18, 16:18 · [Discussion](https://news.ycombinator.com/item?id=50548161)

**「Background」** Voyager 1 is a NASA space probe that performed flybys of Jupiter, Saturn, and Titan, and has been traveling for nearly 50 years. On November 18, 2026, it reached one light-day from Earth — about 16 billion miles \(26 billion kilometers\), a milestone no other human-made object has achieved.

**「Community Discussion」** Commenters praised the interactive model and shared related Golden Record projects, while some noted missing elements. Others asked for more detail on the physical failure mode of the memory chip and questioned whether the content was primarily AI-generated or verified against authoritative sources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voyager_1">Voyager 1 - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/">Voyager 1: What Is a Light-Day - NASA Science</a></li>

</ul>
</details>

**Tags**: `#spacecraft`, `#hardware`, `#visualization`, `#computer-history`, `#embedded-systems`

---

<a id="item-tech-news-8"></a>
### [Daniel Stenberg Questions Whether AI Rust Ports Can Keep Up With Curl](https://simonwillison.net/2026/Nov/18/daniel-stenberg/) ⭐️ 7.0/10

In a November 17, 2026 post, curl maintainer Daniel Stenberg compared AI-generated Rust rewrites of curl with the actual project&\#x27;s ongoing work. He counted that agents converted 185,000 lines of C code into 340,000 lines of Rust code during a little more than three weeks. In that same period, the real curl project merged over 300 commits, including just over 200 bugfixes and a few vulnerability fixes. Stenberg notes that none of those Rust rewrites have those bugfixes, and he questions whether the clones will be able to keep up.

rss · Simon Willison · Nov 18, 15:58

**「Background」** curl is a widely used command-line tool and HTTP client library written in C, maintained by Daniel Stenberg. In late 2026, coding agents produced automatic Rust “vibe ports” of curl and libcurl, converting 185,000 lines of C into 340,000 lines of Rust. Rust is a memory-safe systems programming language, but such generated rewrites may not absorb the continuous security and bug fixes applied to the original C codebase.

**「Impact」** Curl users relying on AI-generated Rust ports may miss the maintainer&\#x27;s latest bugfixes and security patches unless those clones incorporate the real project&\#x27;s rapid updates.

<details><summary>References</summary>
<ul>
<li><a href="https://daniel.haxx.se/blog/2026/11/17/actual-curl-rewrites-in-rust/">Actual curl rewrites in rust - daniel.haxx.se</a></li>
<li><a href="https://explainx.ai/blog/daniel-stenberg-curl-rust-agent-rewrites-vs-maintenance-november-2026">Daniel Stenberg: Agentic Rust curl Rewrites Cannot Keep Up ...</a></li>

</ul>
</details>

**Tags**: `#rust`, `#curl`, `#ai-code-generation`, `#security`, `#open-source`

---

<a id="item-tech-news-9"></a>
### [WeChat Xiaowei Expands Testing to 30M Daily Users](https://mp.weixin.qq.com/s/r3NthxJZQJgztyLADwNV4A) ⭐️ 7.0/10

Tencent said in its third-quarter 2026 earnings report that WeChat&\#x27;s Xiaowei AI assistant has expanded testing and reached 30 million daily active users. Xiaowei is being gradually integrated into WeChat chats, Moments, Official Accounts, and Channels. It uses a custom WeLM model optimized for cost efficiency, with low and continuously declining inference costs, according to Tencent. The company also said some inference tasks are expected to run on user devices in the future.

telegram · zaihuapd · Nov 18, 11:35

**「Background」** WeChat is Tencent&\#x27;s widely used messaging and social media platform in China. Xiaowei is its built-in AI assistant, which was previously available only in limited testing. The reported expansion to 30 million daily active users, along with integration into chat, Moments, Official Accounts, and Channels, indicates a broad rollout across the app&\#x27;s core surfaces.

**「Impact」** WeChat users in the expanded test may encounter Xiaowei across core surfaces including chats, Moments, Official Accounts, and Channels, and the planned on-device inference could later shift some processing away from Tencent&\#x27;s servers.

**Tags**: `#WeChat`, `#Tencent`, `#AI assistant`, `#on-device inference`, `#WeLM`

---

<a id="item-tech-news-10"></a>
### [DeepSeek Makes Server-Side Search and Web Scraping Free](https://www.ithome.com/1/029/058.htm) ⭐️ 7.0/10

DeepSeek announced that starting at 12:00 Beijing time on November 18, 2026, server-side search and web scraping triggered when calling its models will no longer be billed separately, and users will be charged only for model token usage. The change applies to web tool usage, the Anthropic API web\_search tool, and the Responses API web\_search tool. Previously, the Search and Fetch APIs were billed per request at 5 yuan for every 1,000 successful requests. The removal of separate per-request charges lowers costs for developers using the API for retrieval-augmented generation and tool use.

telegram · zaihuapd · Nov 18, 13:44

**「Background」** Server-side search and web scraping allow API calls to fetch live web content without developers running their own crawlers. DeepSeek had introduced the Search and Fetch APIs with usage-based per-request pricing, and this update removes that separate fee.

**「Impact」** Developers using DeepSeek&\#x27;s API for web-enabled tool calls or retrieval-augmented generation will see lower total costs and simplified billing, because only token usage is charged after the 2026-11-18 start time.

**Tags**: `#DeepSeek`, `#API pricing`, `#web search`, `#large language models`, `#software engineering`

---

<a id="item-tech-news-11"></a>
### [US Weighs Forcing Firms to Disclose Chinese AI Use](https://www.reuters.com/world/china/trump-administration-weighs-forcing-us-firms-disclose-chinese-ai-use-2026-11-18/) ⭐️ 7.0/10

According to Reuters, the Trump administration is considering requiring U.S. companies to publicly disclose their use of Chinese AI models, with the Treasury Department and the White House Office of Science and Technology Policy having discussed the proposal. Airbnb’s use of Alibaba’s Qwen to support customer service is cited as an example of a deployment that would need to be disclosed on a company’s website if the plan moves forward. The approach is intended to curb reliance on inexpensive Chinese open-weight models through public naming rather than new restrictions. It is unclear whether the proposal has support within the government or will advance to formal legislation.

telegram · zaihuapd · Nov 19, 02:30

**「Background」** Chinese open-weight models such as Alibaba’s Qwen can be freely downloaded and fine-tuned, making them cheaper than many proprietary alternatives for tasks like customer service. U.S. policymakers have expressed concerns about security and supply-chain dependence on Chinese AI systems. The proposed disclosure would use transparency pressure instead of bans to influence corporate choices.

**「Impact」** If adopted, U.S. companies using Chinese AI models like Qwen would face new public disclosure obligations on their websites, increasing transparency and potentially affecting reputation and procurement decisions.

**Tags**: `#AI policy`, `#US regulation`, `#China AI`, `#open-weight models`, `#technology industry`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Fed October minutes: More rate hikes expected, AI seen as inflation risk](https://www.cnbc.com/2026/11/18/fed-minutes-october-2026.html) ⭐️ 8.0/10

Federal Reserve minutes from October show officials expect further interest-rate increases and view AI as a material inflation risk. The FOMC voted 10-2 to keep its benchmark rate at 3.75%-4%, while markets are fully pricing in a quarter-point hike at the December 8-9 meeting.

rss · CNBC Finance · Nov 18, 19:41

**「Background」** October inflation data released after the meeting showed the consumer price index rose 0.4% overall and 0.3% core, both 0.1 percentage point above expectations, keeping inflation above the Fed&\#x27;s 2% target.

**「Impact」** Fed staff warned that AI-related firms and their lenders could face amplified losses if AI investment returns disappoint, because much of the recent AI debt growth has come through complex, opaque financing structures.

**Tags**: `#Federal Reserve`, `#interest rates`, `#inflation`, `#monetary policy`, `#AI`

---

<a id="item-finance-news-2"></a>
### [Fed’s Waller calls for half-point December rate hike to shock inflation](https://www.cnbc.com/2026/11/18/federal-reserve-governor-christopher-waller.html) ⭐️ 8.0/10

Federal Reserve Governor Christopher Waller said on Wednesday that a half-percentage-point rate increase is probably necessary at the Fed’s December 8-9 meeting to “shock people” and reverse last year’s three quarter-point cuts; futures prices currently fully price only a quarter-point hike.

rss · CNBC Finance · Nov 18, 15:13

**「Background」** The Fed cut rates three times in 2025, but inflation reignited earlier this year after U.S. and Israel struck Iran in late February, keeping most inflation readings above 3% against the central bank’s 2% target.

**Tags**: `#Federal Reserve`, `#monetary policy`, `#interest rates`, `#inflation`, `#Christopher Waller`

---

<a id="item-finance-news-3"></a>
### [Trump, Xi and Putin gather at APEC in Shenzhen amid extended US-China trade truce](https://www.cnbc.com/2026/11/18/apec-trump-xi-putin-shenzhen.html) ⭐️ 7.0/10

President Trump, China&\#x27;s Xi Jinping, and Russia&\#x27;s Vladimir Putin are meeting at the APEC summit in Shenzhen this week with low expectations for breakthroughs. The U.S.-China trade truce of lower tariffs has been extended by two months to January 2027, and both countries have said they will lower tariffs on $30 billion worth of goods from the other country but have not specified an effective date.

rss · CNBC Finance · Nov 18, 06:04

**「Background」** The APEC summit is an annual meeting of Asia-Pacific leaders; this week&\#x27;s gathering in Shenzhen is the first-ever meeting of the U.S., Chinese, and Russian leaders together.

**Tags**: `#US-China trade`, `#APEC summit`, `#technology policy`, `#energy markets`, `#geopolitics`

---

<a id="item-finance-news-4"></a>
### [Tencent Q3: Revenue misses estimates, AI capex soars, WorkBuddy token use tops China](https://api3.cls.cn/share/article/2537922?os=android&amp;amp;sv=8.8.5&amp;amp;app=cailianpress&amp;amp;selected=) ⭐️ 7.0/10

Tencent reported third-quarter 2026 revenue of 207.3 billion yuan, up 8% from a year earlier and below market expectations, while capital spending hit 81.4 billion yuan—far above the 55.4 billion yuan estimate—and free cash flow was negative 69.1 billion yuan. Net profit rose 0.8% to 63.6 billion yuan, and the company said WorkBuddy&\#x27;s daily token consumption exceeded 100 trillion, the highest among domestic large language model products.

telegram · zaihuapd · Nov 18, 09:20

**「Background」** WorkBuddy is an AI Agent office tool from Tencent&\#x27;s cloud code assistant that autonomously plans and completes multimodal tasks. A media report said Tencent has shifted its AI focus from Yuanbao to WorkBuddy, and in the second quarter of 2026 revenue grew 11% year on year to 204.79 billion yuan.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办公新范式</a></li>
<li><a href="https://post.smzdm.com/p/axkzngg3/">放弃 元 宝押注 WorkBuddy ， 腾 讯 AI这场转型算成功吗_IT... | 什么值得买</a></li>

</ul>
</details>

**Tags**: `#Tencent`, `#earnings`, `#AI capex`, `#free cash flow`, `#WorkBuddy`

---

<a id="item-finance-news-5"></a>
### [China and South Korea Conclude FTA Services and Investment Follow-Up Negotiations](https://x.com/Jaemyung_Lee/status/2122988472994791476) ⭐️ 7.0/10

China and South Korea announced on November 18 that follow-up negotiations on services and investment under their free trade agreement had substantively concluded, with China agreeing to grant South Korea most-favored-nation treatment in film and games and to expand market access in tourism, legal, architecture, and finance.

telegram · zaihuapd · Nov 18, 10:02

**「Background」** The services and investment follow-up talks began in March 2018 and substantively concluded after eight years and eight months; the announcement came on 18 November as President Xi Jinping met South Korean President Lee Jae-myung in Shenzhen on the sidelines of the APEC leaders&\#x27; meeting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gov.cn/yaowen/liebiao/202611/content_7086520.htm">习近平会见 韩 国总统李在明__ 中 国政府网</a></li>

</ul>
</details>

**Tags**: `#China-South Korea FTA`, `#services trade`, `#investment liberalization`, `#trade policy`, `#bilateral relations`

---