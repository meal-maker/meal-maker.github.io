---
layout: default
title: "Horizon Summary: 2026-08-20 (EN)"
date: 2026-08-20
lang: en
---

> From 49 items, 13 important content pieces were selected

---

**Technology News**
1. [GitHub&\#x27;s August 17 outage post-mortem details retry storm and VS Code bug](#item-tech-news-1) ⭐️ 8.0/10
2. [Malicious Rust Crate Arrayref Executes Build-Time Payload](#item-tech-news-2) ⭐️ 8.0/10
3. [Aaron Swartz Prosecuted for Scraping While Meta Faces Little Consequence](#item-tech-news-3) ⭐️ 7.0/10
4. [AliExpress silent WebAudio fingerprinting breaks Bluetooth multipoint](#item-tech-news-4) ⭐️ 7.0/10
5. [Show HN: 125M Transformer Autocompletes Piano On-Device](#item-tech-news-5) ⭐️ 7.0/10
6. [Linux 7.2 Announced with HDMI 2.1 Support and Device Updates](#item-tech-news-6) ⭐️ 7.0/10
7. [A shot-scraper-style JSON API on Bun 1.4&\#x27;s new Bun.WebView](#item-tech-news-7) ⭐️ 7.0/10
8. [Terence Tao Warns AI Could Trigger Mathematics&\#x27; Biggest Crisis Since Gödel](#item-tech-news-8) ⭐️ 7.0/10
9. [Black Forest Labs Releases FLUX Upscale for Native 4K Video](#item-tech-news-9) ⭐️ 7.0/10
10. [Reverse Lookup Service Exposed Millions of Facial Photos](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Evergrande founder Xu Jiayin sentenced to life imprisonment; companies fined 8.82 billion and 7 billion yuan](#item-finance-news-1) ⭐️ 9.0/10
2. [Stripe Agrees to Acquire OpenRouter](#item-finance-news-2) ⭐️ 7.0/10
3. [Alibaba first-quarter net profit drops 76%](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [GitHub&\#x27;s August 17 outage post-mortem details retry storm and VS Code bug](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) ⭐️ 8.0/10

GitHub published a post-incident review of the August 17 outage. The analysis identifies a client-side retry loop and a latent retry bug in VS Code as key factors that amplified traffic and delayed recovery. Delayed replies to a single internal endpoint triggered the VS Code bug, increasing traffic by approximately 10x and causing delayed recovery for the Copilot Token Service. The incident underscores how retry amplification and client-side dependencies can prolong outages in distributed systems. GitHub also reported that monthly commits grew from 1.4 billion to 2.9 billion since April.

hackernews · 0xedb · Aug 20, 19:22 · [Discussion](https://news.ycombinator.com/item?id=49378957)

**「Background」** Retry behavior is common in distributed services to handle transient failures, but simultaneous retries can create traffic storms. During GitHub&\#x27;s August 17 outage, an autoscaling failure combined with a client-side retry loop and a VS Code retry bug, causing normal traffic of 7,000–9,000 requests per second to spike to approximately 70,000–100,000 requests per second and delaying recovery for the Copilot Token Service.

**「Impact」** GitHub Copilot users experienced delayed service recovery during the August 17 outage because a VS Code retry bug amplified traffic by roughly 10x to the Copilot Token Service.

**「Community Discussion」** Commenters debated retry behavior, with several arguing that automatic retries hide real errors and can turn brief outages into prolonged delays. Others highlighted the jump from 1.4 billion to 2.9 billion monthly commits as a sign of industry-wide productivity pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/saas/2026/08/19/github-blames-8-hour-outage-on-autoscaling-fail-and-vs-code-retry-storm/5289547">GitHub blames 8-hour outage on autoscaling fail and VS Code retry storm</a></li>
<li><a href="https://xenospectrum.com/en/github-outage-retry-storm/">Why Did the GitHub Outage Last 7 Hours 47 Minutes? A Monitoring Gap and 10x Retry Surge | XenoSpectrum</a></li>
<li><a href="https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/">The August 17 outage, and the work ahead - The GitHub Blog</a></li>

</ul>
</details>

**Tags**: `#incident-analysis`, `#distributed-systems`, `#retries`, `#github`, `#sre`

---

<a id="item-tech-news-2"></a>
### [Malicious Rust Crate Arrayref Executes Build-Time Payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 8.0/10

A malicious Rust crate named Arrayref was found executing a payload during the build process, rather than at runtime, indicating a supply-chain attack. The Rust project published an official incident report on August 20, 2026, and the issue was tracked in the RustSec advisory database as issue \#3161. The malicious version was removed from crates.io, leaving users uncertain about formal advisories. The attack highlights the danger of build scripts in Rust dependencies, which can run arbitrary code at compile time without sandboxing.

hackernews · abhisek · Aug 20, 13:23 · [Discussion](https://news.ycombinator.com/item?id=49374269)

**「Background」** Rust crates can execute arbitrary code during compilation through build scripts \(build.rs\) and procedural macros, meaning merely adding a dependency and compiling can run code on the developer&\#x27;s machine. The crates.io registry distributes these packages, and this attack involved a crate named arrayref \(plus related crates\) whose build process downloaded and executed a remote payload. Researchers found infrastructure overlap with recent North Korean \(DPRK\) supply-chain campaigns, and the malicious versions were removed from crates.io.

**「Impact」** Rust developers who used recent versions of the arrayref crate or the associated malicious crates may have downloaded and executed a remote payload during compilation, and the affected crate versions have been yanked or deleted, which can break builds that still reference them. The infrastructure overlaps with known DPRK supply-chain campaigns, indicating a targeted attack, though the full scope of affected downstream projects is still being assessed.

**「Community Discussion」** Commenters expressed frustration with the incident response from GitHub and crates.io, noting that the package version disappeared without a yank notice or advisory, and argued for improvements such as sandboxed build scripts and reducing dependency counts.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build - Time Malware in Crates with...</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref : Significant Overlap... | Wiz Blog</a></li>
<li><a href="https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/">Malicious Rust Crate arrayref Runs a Build - Time Payload</a></li>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates with...</a></li>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref : Significant Overlap... | Wiz Blog</a></li>

</ul>
</details>

**Tags**: `#rust`, `#supply-chain`, `#security`, `#malware`, `#crates.io`

---

<a id="item-tech-news-3"></a>
### [Aaron Swartz Prosecuted for Scraping While Meta Faces Little Consequence](https://blog.curiousquail.com/im-upset-again-about-a-co-creator-of-rss-being-prosecuted-for-something-meta-is-doing-with-little-consequence/) ⭐️ 7.0/10

The post and HN thread argue that Aaron Swartz&\#x27;s prosecution for downloading JSTOR articles contrasts sharply with Meta&\#x27;s large-scale scraping for AI, which faces little immediate consequence. Commenters add nuance: JSTOR did not pursue civil litigation; the US government brought the criminal case. Swartz physically entered a network closet, plugged in a laptop, downloaded papers rapidly, and rotated MAC addresses to evade MIT&\#x27;s bans, which differs from ordinary public-web scraping. Some also note the often-cited 35-year maximum sentence is misleading because sentencing guidelines and charge grouping would reduce it. The comparison raises questions about selective enforcement based on the defendant&\#x27;s power and economic stakes.

hackernews · speckx · Aug 20, 20:07 · [Discussion](https://news.ycombinator.com/item?id=49379550)

**「Background」** Aaron Swartz, a co-creator of RSS, was federally prosecuted in 2011 for using MIT&\#x27;s network to bulk-download scholarly articles from JSTOR; he faced 13 felony charges and up to 50 years in prison, though JSTOR itself did not pursue civil litigation. More recently, Meta has been sued over large-scale scraping of copyrighted data to train AI models, and in June 2025 a court partially ruled in Meta&\#x27;s favor, finding the training highly transformative and thus fair use. This contrast is central to the debate over legal double standards in web scraping.

**「Community discussion」** Commenters generally agree the Swartz metaphor oversimplifies the facts, with several emphasizing that his actions involved physical trespass and MAC rotation rather than simple scraping, and that the US government, not JSTOR, drove prosecution. There is also disagreement about using Swartz as a data point, with one commenter objecting to reducing him to a rhetorical device.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Aaron_Swartz">Aaron Swartz - Wikipedia</a></li>
<li><a href="https://www.rollingstone.com/politics/politics-news/why-did-the-justice-system-target-aaron-swartz-106848/">Why Did the Justice System Target Aaron Swartz?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anna&#x27;s_Archive">Anna&#x27;s Archive - Wikipedia</a></li>
<li><a href="https://news.bloomberglaw.com/litigation/meta-bytedance-hit-with-youtubers-ai-copyright-scraping-suits">news.bloomberglaw.com/litigation/ meta -bytedance-hit-with-youtubers...</a></li>

</ul>
</details>

**Tags**: `#web scraping`, `#AI training data`, `#legal policy`, `#copyright`, `#tech industry`

---

<a id="item-tech-news-4"></a>
### [AliExpress silent WebAudio fingerprinting breaks Bluetooth multipoint](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 7.0/10

According to a blog post and corroborating user reports, AliExpress runs silent WebAudio fingerprinting that can break Bluetooth multipoint audio connections. The technique uses the browser&\#x27;s WebAudio API to generate or process inaudible audio, which can cause connected Bluetooth devices to treat the stream as active and interrupt other audio sources. Affected users describe hearing aid amplification changes, car audio systems reacting as if a voice command was issued, and other multipoint disruptions while the AliExpress page or app is open or backgrounded. Closing the tab or killing the app resolves the issue, and browser tab speaker indicators typically do not light up because the audio is silent. This illustrates how web fingerprinting can have unintended side effects on physical audio hardware.

hackernews · emctech · Aug 20, 10:08 · [Discussion](https://news.ycombinator.com/item?id=49372583)

**「WebAudio fingerprinting and Bluetooth multipoint」** WebAudio fingerprinting uses the WebAudio API to generate and analyze audio signals; because audio processing varies by device, browser, and driver, the resulting measurements can act as a persistent identifier that is invisible to users and not blocked by Do Not Track. Bluetooth multipoint allows headphones to connect to two source devices at once, but an active audio stream from a webpage—even one carrying silence—can keep the Bluetooth channel open or cause interference when switching between devices. The AliExpress pages silently create WebAudio graphs connected to the system audio destination through a zero-gain node, which is why the fingerprinting script causes real-world Bluetooth multipoint disruption.

**「Impact」** Users with Bluetooth multipoint audio devices such as hearing aids and car audio systems may experience unexpected interruptions or mode changes when visiting AliExpress in a browser or with the app backgrounded; closing the page or app is the reported workaround.

**「Community Discussion」** Commenters report similar silent-audio disruptions on iOS and car audio, with one noting that killing or uninstalling AliExpress fixed the problem. Others discuss the lack of a browser speaker icon for silent streams and Firefox&\#x27;s WebAudio fingerprinting mitigations, while one commenter sarcastically doubts Apple will enforce its App Store protections.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html">laserphile: AliExpress webpage keeping multipoint Bluetooth headphones active with WebAudio fingerprinting</a></li>
<li><a href="https://news.ycombinator.com/item?id=49372583">AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint | Hacker News</a></li>

</ul>
</details>

**Tags**: `#webaudio`, `#fingerprinting`, `#privacy`, `#bluetooth`, `#web security`

---

<a id="item-tech-news-5"></a>
### [Show HN: 125M Transformer Autocompletes Piano On-Device](https://simedw.com/2026/08/20/midi-autocomplete/) ⭐️ 7.0/10

A Show HN project demonstrates a 125M-parameter transformer that autocompletes MIDI piano performances in real time on-device. The creator, simedw, trained the model to work like GitHub Copilot or Tabnine: the user plays a few notes on a MIDI piano and the model continues the phrase entirely locally. It runs at about 108 notes per second on an iPhone 15. The app is available for free, and the author invites questions about the model, training, Core ML, and failed approaches.

hackernews · simedw · Aug 20, 12:04 · [Discussion](https://news.ycombinator.com/item?id=49373456)

**「Background」** MIDI represents musical notes as discrete event data, making it a natural fit for sequence modeling with transformers. Small transformer models around 125M parameters are small enough to run locally on modern phones using frameworks like Apple&\#x27;s Core ML. Autocomplete workflows, popularized in code editors, apply the same next-token prediction idea to musical phrases.

**「Impact」** For musicians using the free iOS app, the model provides real-time local piano phrase continuation without sending performance data to a server, with no noticeable latency on an iPhone 15.

**「Community Discussion」** Commenters generally praised the project as a creative application of on-device generation, with one classical pianist comparing it to AI-assisted UX design and another noting its connection to historical compositional training. One commenter asked about the size of the training data, and another found the model&\#x27;s unexpected continuation of Für Elise surprising.

**Tags**: `#transformer`, `#on-device inference`, `#music generation`, `#Core ML`, `#MIDI`

---

<a id="item-tech-news-6"></a>
### [Linux 7.2 Announced with HDMI 2.1 Support and Device Updates](https://www.igalia.com/2026/08/19/Linux-72-Released.html) ⭐️ 7.0/10

According to the submission, Linux 7.2 has been released as an incremental stable update. The release is highlighted for adding HDMI 2.1 support and for updates affecting devices such as Raspberry Pi. Because the linked content is not available, specific implementation details, compatibility constraints, and affected hardware lists are not provided.

hackernews · mariuz · Aug 20, 15:46 · [Discussion](https://news.ycombinator.com/item?id=49376265)

**「Background」** AMD&\#x27;s efforts to implement HDMI 2.1 in its open-source Linux driver were blocked by the HDMI Forum in February 2024, preventing open-source support for features like 4K@120Hz and FreeSync over HDMI 2.1 \(tool-2-1, tool-2-2, tool-2-3\). The Linux 7.2 kernel now includes initial HDMI 2.1 FRL \(Fixed Rate Link\) support in the AMDGPU driver, along with Runtime Power Management for Raspberry Pi 4 and 5 GPUs \(tool-1-1, tool-1-2, tool-1-3\).

**「Impact」** AMD Linux users gain open-source HDMI 2.1 FRL support in Linux 7.2, removing a previous blocker for high-bandwidth 4K/8K displays.

**「Community Discussion」** Commenters questioned how this differs from LWN coverage, asked what changed to allow HDMI 2.1 support after the HDMI Forum blocked the AMD open-source driver, and discussed the intended audience. One user said they are excited to update their Raspberry Pi 4, while another asked why HDMI would be preferred over DisplayPort.

<details><summary>References</summary>
<ul>
<li><a href="https://www.igalia.com/2026/08/19/Linux-72-Released.html">Linux 7.2 Released | Igalia</a></li>
<li><a href="https://www.linuxconsultant.org/linux-kernel-7-2-released-with-amdgpu-hdmi-2-1-frl-support/">Linux Kernel 7.2 Released with AMDGPU HDMI 2.1 FRL Support – Linux Consultant</a></li>
<li><a href="https://9to5linux.com/linux-kernel-7-2-officially-released-this-is-whats-new">Linux Kernel 7.2 Officially Released, This Is What’s New - 9to5Linux</a></li>
<li><a href="https://www.phoronix.com/news/HDMI-2.1-OSS-Rejected">HDMI Forum Rejects Open-Source HDMI 2.1 Driver Support Sought By AMD - Phoronix</a></li>
<li><a href="https://arstechnica.com/gadgets/2024/02/hdmi-forum-to-amd-no-you-cant-make-an-open-source-hdmi-2-1-driver/">HDMI Forum to AMD: No, you can’t make an open source HDMI 2.1 driver - Ars Technica</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/hdmi-forum-rejects-amds-hdmi-21-open-source-driver">HDMI Forum rejects AMD&#x27;s HDMI 2.1 open-source driver | Tom&#x27;s Hardware</a></li>
<li><a href="https://media.patentllm.org/news/hardware/amd-gpu-benchmarks-hdmi-2-1-frl-driver-and-multi-device-ai-w-20260604">AMD GPU Benchmarks, HDMI 2 . 1 FRL Driver, and... - PatentLLM Blog</a></li>

</ul>
</details>

**Tags**: `#linux`, `#kernel`, `#open source`, `#hardware support`, `#systems software`

---

<a id="item-tech-news-7"></a>
### [A shot-scraper-style JSON API on Bun 1.4&\#x27;s new Bun.WebView](https://simonwillison.net/2026/Aug/20/bun-webview-json-api/) ⭐️ 7.0/10

Simon Willison documents a prototype shot-scraper-style JSON API built on Bun 1.4&\#x27;s new Bun.WebView. Bun 1.4 is the first stable release since the Rust rewrite and claims significant performance and Node.js compatibility improvements, including +1,517 Node.js tests, 5x lower idle CPU usage, up to 35% less memory, and 50% faster startup on Linux. Bun.WebView adds first-class browser automation to Bun core using macOS WebKit or a local Chromium process via the Chrome DevTools Protocol. The TypeScript server implementation loads pages and executes JavaScript, needing a 192MB–256MB container to run full Chrome against complex web pages when tested with cgroups.

rss · Simon Willison · Aug 20, 15:37

**「Background」** Bun is a JavaScript/TypeScript runtime and toolkit that recently underwent a rewrite from Zig to Rust. Shot-scraper is Simon Willison&\#x27;s command-line tool for taking screenshots and executing JavaScript against web pages. Bun.WebView provides native browser automation functionality, reducing the need for external automation libraries in Bun applications.

**「Impact」** Developers building browser automation services on Bun can expect a Bun.WebView-based API to run in roughly a 192MB–256MB container for complex pages using full Chrome.

**Tags**: `#Bun`, `#WebView`, `#web scraping`, `#JavaScript`, `#developer tools`

---

<a id="item-tech-news-8"></a>
### [Terence Tao Warns AI Could Trigger Mathematics&\#x27; Biggest Crisis Since Gödel](https://the-decoder.com/terence-tao-says-ai-could-trigger-maths-biggest-crisis-since-godel/) ⭐️ 7.0/10

Terence Tao, in an article for the 2026 International Congress of Mathematicians, warns that AI could push mathematics from proof scarcity to proof surplus, potentially causing the field&\#x27;s biggest crisis since the foundational upheaval of 1900–1930 involving Russell&\#x27;s paradox and Gödel&\#x27;s incompleteness theorems. He argues the mathematical community should stop debating what AI can do and instead confront the avoided question of research goals. Tao cites the First-Proof project, where in its second round four AI systems were tested on 10 unpublished research problems, and 7 were judged qualified by at least one system, at a cost of tens to hundreds of dollars per problem. He contends that even formally verified proofs that no one can clearly explain should be treated as incomplete.

telegram · zaihuapd · Aug 20, 13:19

**「Background」** Kurt Gödel’s 1931 incompleteness theorems demonstrated that any sufficiently powerful formal system contains true statements that cannot be proved within that system, triggering a foundational crisis in mathematics. Modern formal verification allows software to mechanically check proofs, while projects like First-Proof test AI systems on unpublished research problems at low cost. Terence Tao’s essay for the 2026 International Congress of Mathematicians frames the resulting shift from proof scarcity to an overwhelming abundance of machine-generated, human-incomprehensible proofs as a second foundations crisis.

<details><summary>References</summary>
<ul>
<li><a href="https://forum.gnoppix.org/t/terence-tao-says-ai-could-trigger-maths-biggest-crisis-since-godel/7114">Terence Tao says AI could trigger math&#x27;s biggest crisis since Gödel - AI General - Gnoppix Forum</a></li>
<li><a href="https://teorth.github.io/tao-web/ai-views.html">Terence Tao on AI in mathematics (and beyond)</a></li>
<li><a href="https://e.vnexpress.net/news/news/education/fields-medalist-terence-tao-warns-ai-could-produce-more-math-proofs-than-humans-can-handle-5102580.html">Fields Medalist Terence Tao warns AI could produce more math proofs than humans can handle - VnExpress International</a></li>

</ul>
</details>

**Tags**: `#AI`, `#mathematics`, `#formal verification`, `#automated theorem proving`, `#research`

---

<a id="item-tech-news-9"></a>
### [Black Forest Labs Releases FLUX Upscale for Native 4K Video](https://bfl.ai/blog/flux-video-upscale) ⭐️ 7.0/10

Black Forest Labs announced FLUX Upscale, a standalone AI tool that regenerates videos up to native 4K. It uses the same pipeline as the 1080p step in FLUX 3 Video and can fix common artifacts such as blurry faces, water surfaces, and grass texture grids. The tool offers two modes: Precise with 4 steps at $0.07 per megapixel-second and Creative with 8 steps at $0.1 per megapixel-second. The upscale\_factor parameter supports 1.5x, 2x, and 3x scaling.

telegram · zaihuapd · Aug 20, 14:17

**「Background」** Black Forest Labs is a German AI image and video development team known for the open-source FLUX image model. FLUX Upscale is a standalone tool derived from the upscaling step used in FLUX 3 Video&\#x27;s 1080p output.

**「Impact」** Video producers and developers using FLUX Upscale can regenerate footage up to native 4K with selectable Precise or Creative modes and per-megapixel-second pricing.

**Tags**: `#AI video upscaling`, `#Black Forest Labs`, `#FLUX`, `#generative AI`, `#tool release`

---

<a id="item-tech-news-10"></a>
### [Reverse Lookup Service Exposed Millions of Facial Photos](https://arstechnica.com/gadgets/2026/08/reverse-lookup-service-exposed-millions-of-photos-of-peoples-faces/) ⭐️ 7.0/10

A reverse image search service reportedly suffered a data breach that exposed a 450GB database containing more than 9 million facial images and associated personal information, including some email addresses, phone numbers, and IP addresses. Because facial data is biometric and hard to change, the leak raises serious privacy and identity security concerns. Experts warn the exposed data could be used for unauthorized identification, tracking, or fraud. The service has restricted database access, but the full impact and remediation are still being confirmed.

telegram · zaihuapd · Aug 20, 15:14

**「Context」** Reverse image search services let users upload a photo to find similar or matching images, often for identifying people or verifying profiles. Because human faces cannot be easily changed, a breach that exposes facial images alongside email addresses, phone numbers, or IP addresses creates a higher risk than typical password leaks, since the biometric data can be used for unauthorized identification, tracking, or fraud. This explains why such an exposure is treated as a serious privacy and identity security incident.

**「Impact」** Individuals whose facial images and contact details were exposed are at higher risk of identity fraud, unauthorized identification, and personal tracking.

**Tags**: `#data-breach`, `#privacy`, `#facial-recognition`, `#security`, `#reverse-image-search`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Evergrande founder Xu Jiayin sentenced to life imprisonment; companies fined 8.82 billion and 7 billion yuan](https://www.news.cn/legal/20260820/737dfb54ab564fb8a549ba392af9fb0a/c.html) ⭐️ 9.0/10

On 20 August, in a first-instance ruling, the Shenzhen Intermediate People&\#x27;s Court sentenced Evergrande founder Xu Jiayin to life imprisonment with confiscation of all personal property, and fined Evergrande Group 8.82 billion yuan and Evergrande Real Estate 7 billion yuan.

telegram · zaihuapd · Aug 20, 04:06

**「Background」** The court found that from 2016 to 2021 the defendants used large-scale financial fraud to illegally take public deposits, defraud investors, and issue securities fraudulently; the same day, 56 other people including Zhen Litao and Ke Peng were sentenced to prison terms ranging from 18 years to 1 year and 10 months.

**Tags**: `#Evergrande`, `#Xu Jiayin`, `#financial fraud`, `#China real estate`, `#court verdict`

---

<a id="item-finance-news-2"></a>
### [Stripe Agrees to Acquire OpenRouter](https://stripe.com/en-jp/newsroom/news/stripe-agrees-to-acquire-openrouter) ⭐️ 7.0/10

Stripe announced on August 19, 2026 that it has agreed to acquire OpenRouter, an AI model gateway that routes requests across more than 80 providers and more than 400 models.

telegram · zaihuapd · Aug 20, 07:00

**「Background」** OpenRouter had described itself as the &\#x27;Stripe for LLMs,&\#x27; reflecting its role as a model-routing gateway before Stripe&\#x27;s acquisition announcement.

<details><summary>References</summary>
<ul>
<li><a href="https://menlovc.com/perspective/stripe-to-acquire-openrouter-why-everyone-is-obsessed-with-model-routing/">Stripe to Acquire OpenRouter : Why Everyone Is Obsessed With...</a></li>

</ul>
</details>

**Tags**: `#Stripe`, `#OpenRouter`, `#Acquisition`, `#AI infrastructure`, `#Fintech`

---

<a id="item-finance-news-3"></a>
### [Alibaba first-quarter net profit drops 76%](https://www.alibabagroup.com/en-US/document-2026456290057781248) ⭐️ 7.0/10

Alibaba reported net profit attributable to shareholders of RMB 10.54 billion for the first quarter of fiscal year 2027, down 76% from a year earlier.

telegram · zaihuapd · Aug 20, 12:08

**「Background」** Alibaba’s fiscal year starts in April, so this quarter covers April–June 2026. A prior report citing CEO Wu Yongming attributed the company’s profit declines to heavy investment in areas such as cloud and AI, describing the period as focused on “sowing” rather than “harvesting.”

<details><summary>References</summary>
<ul>
<li><a href="https://tele.ofweek.com/2026-05/ART-8320505-8460-30687639.html">利 润 大跌， 阿 里 “烧钱”换未来 - OFweek通信网</a></li>

</ul>
</details>

**Tags**: `#Alibaba`, `#earnings`, `#net profit`, `#China tech`, `#quarterly results`

---