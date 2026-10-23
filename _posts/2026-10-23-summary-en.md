---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 42 items, 18 important content pieces were selected

---

**Technology News**
1. [NVIDIA OpenShell Runtime for Safe Autonomous AI Agent Fleets](#item-tech-news-1) ⭐️ 8.0/10
2. [iOS 16.5 Firmware Runs on Android Devices and QEMU](#item-tech-news-2) ⭐️ 8.0/10
3. [Jailbreaking the Switch 2](#item-tech-news-3) ⭐️ 8.0/10
4. [eMudhra Exits Global SSL/TLS Certificate Business](#item-tech-news-4) ⭐️ 8.0/10
5. [Triangulating 3.7M Map Polygons in 489 ms, Faster Than Earcut](#item-tech-news-5) ⭐️ 8.0/10
6. [Australia Orders Apple to Open iPhone to Third-Party App Stores](#item-tech-news-6) ⭐️ 8.0/10
7. [Oracle Issues Critical Java SE JSSE Vulnerability Alert](#item-tech-news-7) ⭐️ 8.0/10
8. [333 Backdoored Tor Exit Relays Taken Offline](#item-tech-news-8) ⭐️ 8.0/10
9. [Banned Nvidia B300 Servers Appear in Chinese State Network](#item-tech-news-9) ⭐️ 8.0/10
10. [Quad9 DNS Resolver to Exit France](#item-tech-news-10) ⭐️ 7.0/10
11. [pwn.watch: Real-Time Dashboard for Exploited Vulnerabilities](#item-tech-news-11) ⭐️ 7.0/10
12. [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](#item-tech-news-12) ⭐️ 7.0/10
13. [Carbon-X: Open 14.8B Joint DNA/Text Model](#item-tech-news-13) ⭐️ 7.0/10
14. [Open-XTTS-Trainer: Train All XTTS v2 Components and Add New Scripts](#item-tech-news-14) ⭐️ 7.0/10
15. [Steerable TTS Edge Variant Hits 11.84 MB With Unchanged WER](#item-tech-news-15) ⭐️ 7.0/10
16. [Smart TVs Send ACR Data After Opt-Out, Some Unencrypted](#item-tech-news-16) ⭐️ 7.0/10
17. [MiHoYo and Tsinghua Open-Source GameScaling Game Control Model](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [China’s CSI 300 Falls 20% From June High as A-Shares Near Bear Market](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [NVIDIA OpenShell Runtime for Safe Autonomous AI Agent Fleets](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA has released OpenShell, a new open-source runtime for safely and privately running fleets of autonomous AI agents, according to its GitHub repository and a Hacker News discussion. The runtime is designed to allow agents to read files, install packages, call APIs, and use credentials while preventing unrestricted access to data, secrets, and network resources. The announcement generated substantial technical discussion—152 comments—centered on agent isolation, containerization, security, and auditing among software engineers and AI practitioners. No specific version number or release date is provided in the item summary.

hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

**「Background」** OpenShell is an open-source runtime from NVIDIA designed to run fleets of autonomous AI agents safely by enforcing declarative policies. Agents need broad capabilities such as reading files, installing packages, calling APIs, and using credentials; OpenShell provides sandboxed execution and policy enforcement to prevent unauthorized file access, data exfiltration, and uncontrolled network activity. It aims to give agents necessary access without granting unrestricted access to data, secrets, or networks.

**「Impact」** Teams running autonomous AI agents now have an NVIDIA-backed open-source runtime that supports containerized isolation and can be integrated with team policies, safe git usage, and built-in SCA/SAST scanning, reducing the effort needed to manage agent fleets safely. However, community members caution that such runtimes cannot fully eliminate data exfiltration risks when agents are given broad capabilities.

**「Community Discussion」** Practitioners generally agree that running agents in containers or managed sandboxes is essential, with one commenter saying it is &\#x27;crazy&\#x27; not to; yet many highlight unresolved challenges, including preventing codebase exfiltration, auditing process executions when safety classifiers block tooling, and striking a balance between agent access and security. One team reports using OpenShell in production and building additional layers for team policies, safe git access, and built-in SCA/SAST, noting that agent traces show goal-seeking without boundaries is real.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://docs.nvidia.com/openshell/home">NVIDIA OpenShell Developer Guide</a></li>

</ul>
</details>

**Tags**: `#ai-agents`, `#security`, `#open-source`, `#containerization`, `#nvidia`

---

<a id="item-tech-news-2"></a>
### [iOS 16.5 Firmware Runs on Android Devices and QEMU](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 8.0/10

The hackios-xnu-kernel project demonstrates that the full iOS 16.5 firmware can boot on the POCO X5 Pro 5G, some other Xiaomi devices, and QEMU. It is explicitly a research bench rather than a production ROM: each session runs for a fixed number of seconds before the kernel returns to the loader and outputs its log. The open-source code is available on GitHub, with a companion website providing documentation. Because it targets non-Apple hardware, the project offers a rare platform for studying iOS internals and reverse engineering without Apple hardware.

hackernews · aghuang · Oct 22, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50196718)

**「What HackiOS does」** HackiOS boots Apple&\#x27;s open-source XNU kernel \(xnu-8796.121.2, the kernel of iOS 16.5\) on Android phone hardware and runs the unmodified iOS 16.5 user space on top of it, including launchd, backboardd, SpringBoard, and apps. It is a research bench rather than a full ROM: a session lasts a given number of seconds, then the kernel returns to the loader and hands over its log, and it does not replace Android because the iOS environment runs in memory and a reboot returns the device to Android. The project also supports running in QEMU and has been demonstrated on devices such as the POCO X5 Pro 5G and some Xiaomi models.

**「Impact」** For systems researchers and vulnerability analysts, the harness provides an accessible way to observe the iOS 16.5 kernel boot process on QEMU or supported Xiaomi hardware, although its session length limit prevents it from serving as a consumer-ready iOS replacement.

**「Community Discussion」** Commenters call the QEMU and Xiaomi boot demo impressive but caution that the project is not a full ROM, and some note that Android devices skinned to resemble iOS already complicate verification when buying used iPhones.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oosexgang/hackios-xnu-kernel">GitHub - oosexgang/hackios-xnu-kernel</a></li>
<li><a href="https://www.zendot.org/posts/oosexgang-hackios-xnu-kernel">在安卓手机上启动苹果 XNU 内核，跑原版 iOS 16.5 · Zendot</a></li>

</ul>
</details>

**Tags**: `#iOS`, `#Android`, `#emulation`, `#reverse-engineering`, `#kernel`

---

<a id="item-tech-news-3"></a>
### [Jailbreaking the Switch 2](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 8.0/10

A write-up at pepsipu.com describes an apparent jailbreak of the Nintendo Switch 2 that achieves decrypted filesystem read/write access. If the claims are accurate, this could enable game dumps, emulation, and homebrew software on the console. The available item does not provide independent verification or detailed exploit-chain information beyond the assertion of filesystem access.

hackernews · ledoge · Oct 22, 08:01 · [Discussion](https://news.ycombinator.com/item?id=50192536)

**「Background」** Jailbreaking a console means bypassing its software restrictions to run unsigned code such as homebrew or game mods. A userland exploit runs only in an application context without kernel privileges, and a tethered exploit must be reapplied after each reboot using a connected host device. According to the developer&\#x27;s release notes, ns2jb is a software-only tethered userland exploit for the Nintendo Switch 2 on firmware version 23.0.1, and it grants access to most peripherals through MMIO along with decrypted filesystem read/write.

**「Impact」** If confirmed, the jailbreak could enable Switch 2 game dumps and homebrew, undermining Nintendo&\#x27;s platform control and potentially allowing exclusives to run on unofficial hardware.

**「Community Discussion」** Commenters express excitement and expect game dumps to appear quickly, with one calling this a &\#x27;worst-case scenario&\#x27; for Nintendo due to decompilation and recompilation projects. Others discuss the automated hardware setup using JetKVM, Codex, and a SwitchBot button-presser, while some question how Codex was able to assist given usage restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/">pepsipu.com/blog/2026-10- switch 2 - jailbreak - ns 2 jb</a></li>
<li><a href="https://gbatemp.net/news/switch-2-jailbreak-ns2jb-released-software-only-exploit-tethered.685698/">Switch 2 jailbreak &quot; ns 2 jb &quot; released. Software-only... | GBAtemp.net</a></li>

</ul>
</details>

**Tags**: `#console-security`, `#jailbreak`, `#reverse-engineering`, `#nintendo-switch-2`, `#game-emulation`

---

<a id="item-tech-news-4"></a>
### [eMudhra Exits Global SSL/TLS Certificate Business](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 8.0/10

eMudhra has announced its exit from the global SSL/TLS certificate business following an incident that raised serious concerns about its CA operations and key management. The public certificate authority&\#x27;s departure comes amid community scrutiny over the handling of the incident, including questions about the security of private keys and the issuance of end-entity certificates. The company stated that its global SSL/TLS infrastructure is separate from other operations and that no end-entity certificates were issued from the affected CAs, according to comments. Browser vendors and security practitioners have publicly questioned eMudhra, highlighting the incident&\#x27;s importance for web PKI trust.

hackernews · bo0tzz · Oct 22, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50195110)

**「Background」** eMudhra is an Indian certificate authority that operates its global SSL/TLS certificate issuance separately from its other digital signature, eSign, and enterprise PKI services. After a researcher reported recovering private keys for eight of its intermediate CA certificates, the company revoked those certificates; its board then decided to withdraw from the global SSL/TLS business. Intermediate CA private keys are sensitive because anyone with them can issue end-entity certificates that browsers and operating systems would trust.

**「Impact」** Organizations using eMudhra for publicly trusted SSL/TLS certificates will need to migrate to another certificate authority before eMudhra completes its exit.

**「Community Discussion」** Community comments were largely critical: one commenter posted what appeared to be a trivially small RSA private key, another linked to a detailed public question list from the Chrome team, and a third challenged the company&\#x27;s statement that no end-entity certificates were issued from the affected CAs. The overall tone was that eMudhra&\#x27;s lack of explanation and apology made the situation worse.

<details><summary>References</summary>
<ul>
<li><a href="https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business">eMudhra to Exit global SSL / TLS Certificate Business</a></li>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL / TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/">EMudhra Intermediate CA Certificates Compromised</a></li>

</ul>
</details>

**Tags**: `#SSL/TLS`, `#certificate authority`, `#PKI`, `#web security`, `#security incident`

---

<a id="item-tech-news-5"></a>
### [Triangulating 3.7M Map Polygons in 489 ms, Faster Than Earcut](https://globus.software/blog/2026/10/16/cutting-map-polygons/) ⭐️ 8.0/10

A blog post describes a high-throughput triangulation approach that processed 3.7 million map polygons in 489 ms, outperforming the widely used earcut library. The write-up includes benchmark results against earcut and generated substantive technical discussion relevant to GIS, map rendering, and computational geometry. Earcut&\#x27;s author thanked the author and noted that some potential optimizations were deliberately rejected to keep his JavaScript library small, while asking about the size of the new WASM build. Other commenters brought up alternative triangulators such as Triangle and Delaunay32 and raised questions about triangle quality, particularly long thin triangles and GPU rasterization.

hackernews · molind · Oct 22, 09:31 · [Discussion](https://news.ycombinator.com/item?id=50193170)

**「Background」** Polygon triangulation converts polygon outlines into triangles, a common preprocessing step for rendering vector maps and other graphics. Earcut is a small, fast JavaScript library that performs this task and is widely used in mapping applications due to its simplicity and compact bundle size. The post introduces earstrip, a new library from Globus Software that is benchmarked against earcut and Delaunay triangulation on a large corpus of map polygons.

**「Impact」** For developers triangulating very large polygon datasets in map rendering, the reported 489 ms result offers a substantial speed improvement over earcut, but commenters note the output contains many long, thin triangles that may be a worst case for GPU rasterizers.

**「Community Discussion」** Commenters praised the performance improvements, with earcut&\#x27;s author noting he had rejected some optimizations to keep his library small and asking about the WASM build size; others raised comparisons to Triangle and Delaunay32, and questioned whether the generated long thin triangles could hurt GPU rasterization and why ear clipping beats Seidel&\#x27;s method.

<details><summary>References</summary>
<ul>
<li><a href="https://globus.software/blog/2026/10/16/cutting-map-polygons/">Faster than earcut : triangulating 3 . 7 M map polygons in 489 ms</a></li>
<li><a href="https://www.npmjs.com/search?q=earcut">earcut - npm search</a></li>

</ul>
</details>

**Tags**: `#triangulation`, `#computational-geometry`, `#performance`, `#algorithms`, `#mapping`

---

<a id="item-tech-news-6"></a>
### [Australia Orders Apple to Open iPhone to Third-Party App Stores](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

Australia&\#x27;s Federal Court has ruled that Apple must allow Australian iPhone users to install apps through third-party app stores and websites, and must permit alternative payment methods and external payment links, starting March 1, 2027. The ruling also requires Fortnite to return to the Australian App Store immediately. The decision stems from Epic Games&\#x27; antitrust lawsuit, in which the judge found Apple holds substantial market power in iOS app distribution and payments, and that its restrictions breach Australian competition law. Apple said it will appeal the ruling and seek a stay of enforcement. The outcome could reshape iOS app distribution and payment rules in Australia.

telegram · zaihuapd · Oct 22, 06:54

**「Background」** Apple&\#x27;s iOS platform has historically restricted app distribution to the App Store and required in-app purchases to use Apple&\#x27;s payment system. Epic Games, maker of Fortnite, has pursued antitrust litigation against these practices in multiple countries. The Australian Federal Court&\#x27;s ruling applies the country&\#x27;s competition law to those restrictions.

**「Impact」** If the ruling stands, Australian iPhone users and developers would gain sideloading, third-party app stores, and external payment links from March 1, 2027, while Fortnite is set to return to the App Store immediately; Apple&\#x27;s appeal and stay request leave the timeline uncertain.

**Tags**: `#Apple`, `#Epic Games`, `#antitrust`, `#app store`, `#regulation`

---

<a id="item-tech-news-7"></a>
### [Oracle Issues Critical Java SE JSSE Vulnerability Alert](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 8.0/10

Oracle has issued a security alert for CVE-2026-91403, a critical vulnerability in the Java SE JSSE component with a CVSS score of 9.1. The flaw can be exploited remotely by an unauthenticated attacker over the network and may seriously compromise data confidentiality and integrity. Affected versions include Java SE 8u511, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1, and multiple GraalVM releases. Oracle has released patches and urges users to upgrade to supported versions promptly to reduce the risk of network attacks.

telegram · zaihuapd · Oct 22, 12:30

**「Background」** JSSE \(Java Secure Socket Extension\) is the Java component that implements TLS and certificate validation for Java SE applications. The CVE-2026-91403 fix requires Java to distrust a set of impacted intermediate CA certificates associated with eMudhra, a certificate authority, to prevent attackers from abusing mis-issued or compromised certificates to intercept or impersonate encrypted connections.

**「Impact」** Administrators and developers running the listed Java SE or GraalVM versions should apply Oracle&\#x27;s patches immediately to prevent unauthenticated remote attacks that could compromise data confidentiality and integrity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/alert-cve-2026-91403.html">Oracle Security Alert Advisory - CVE-2026-91403</a></li>

</ul>
</details>

**Tags**: `#Java`, `#Security Vulnerability`, `#Oracle`, `#CVE`, `#Patch Management`

---

<a id="item-tech-news-8"></a>
### [333 Backdoored Tor Exit Relays Taken Offline](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

A Tor operator using a script to scan about 3,000 exit relays found 333, or roughly 10%, backdoored with Ebury malware. The backdoor hijacked SSH connections on port 22, redirecting them to 12 interception servers to steal credentials. On October 4 these nodes were flagged as BadExit, and by the next day all were taken offline. The attackers had already compromised the servers in August and blocked some ports specifically to collect unencrypted email traffic. The intrusion vector remains undetermined.

telegram · zaihuapd · Oct 22, 14:52

**「Context」** Ebury is a long-lived SSH backdoor family that has infected hundreds of thousands of Linux servers, often by patching OpenSSH binaries to steal credentials and provide remote access \(tool-1-1, tool-1-2\). Tor exit relays are the final hop of the Tor network where traffic leaves to the public internet, so an attacker controlling them can observe or tamper with unencrypted traffic. In this case, a Tor operator scanned roughly 3000 exit relays and identified 333 \(about 10%\) running Ebury, which hijacked port 22 SSH connections to interception servers and collected unencrypted email traffic \(tool-1-3\).

**「Impact」** Users whose Tor exit traffic passed through these 333 relays between August and early October may have had port 22 SSH connections redirected to attacker-controlled servers, risking credential theft and interception of unencrypted email.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2024/05/ssh-backdoor-has-infected-400000-linux-servers-over-15-years-and-keeps-on-spreading/">Linux maintainers were infected for 2 years by SSH -dwelling backdoor ...</a></li>
<li><a href="https://www.darkreading.com/threat-intelligence/400k-linux-servers-recruited-by-resurrected-ebury-botnet">400K Linux Servers Recruited by Resurrected Ebury Botnet</a></li>
<li><a href="https://kaba.cx/posts/20261020_Tor/">How I got over 300 Tor exit nodes removed - KABA</a></li>

</ul>
</details>

**Tags**: `#security`, `#Tor`, `#Ebury`, `#malware`, `#networking`

---

<a id="item-tech-news-9"></a>
### [Banned Nvidia B300 Servers Appear in Chinese State Network](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

Chinese state-controlled semiconductor leasing group financed the purchase of 32 Asus servers equipped with Nvidia B300 GPUs for Chinese AI firm Glory View Technology \(荣耀视图科技\), part of a deal exceeding 700 servers and worth more than 3 billion yuan, with deployment planned at China Mobile&\#x27;s Ningxia hub. B300 chips are subject to the strictest tier of US export controls and are essentially banned for sale to China. After the procurement filing drew attention, the semiconductor leasing group resubmitted documents and removed the hardware description. Nvidia said it is investigating with manufacturing partners, while Asus stated it complies with export controls.

telegram · zaihuapd · Oct 22, 15:22

**「Background」** The United States restricts exports of advanced AI accelerators to China, requiring licenses for high-performance data-center GPUs and banning sales of the most capable chips without authorization. Nvidia&\#x27;s B300, part of its latest data-center lineup, falls into that most restricted category, so any transfer to Chinese state-affiliated buyers would violate the controls unless an exception or license applies. Chinese state-linked financing entities and enterprises sometimes attempt to acquire restricted hardware through intermediaries or altered procurement records, which can trigger vendor investigations.

**「Impact」** This case shows that US export controls have not prevented Chinese state-backed entities from acquiring Nvidia B300 servers for state-linked AI infrastructure, consistent with broader Chinese efforts to buy Nvidia chips despite bans, and it has triggered vendor investigations and record redactions that may increase compliance scrutiny. Whether the servers were ultimately delivered or deployed remains unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=8s1vlXhm2t0">Why China Is Building an AI Megaplex in the Desert - YouTube</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#B300`, `#export controls`, `#AI hardware`, `#China`

---

<a id="item-tech-news-10"></a>
### [Quad9 DNS Resolver to Exit France](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 7.0/10

Quad9, a recursive DNS resolver, will exit France after court rulings and fines related to piracy blocking and geoIP enforcement. The company has faced legal demands to block piracy-related domain resolutions and was fined for noncompliance with geoIP filtering orders. Quad9 may use geoIP filters to block French users from its service, despite previously arguing such filtering is insufficient for selective denial. This exit removes Quad9&\#x27;s DNS resolution service from the French market.

hackernews · farrokhi · Oct 22, 14:32 · [Discussion](https://news.ycombinator.com/item?id=50195959)

**「Background」** Quad9 is a free DNS resolver operated by the Swiss public-benefit, not-for-profit Quad9 Foundation, headquartered in Zürich, with a focus on privacy and cybersecurity. Since 2024, French courts have repeatedly ordered public DNS resolvers to block access to pirate sports streaming sites, leading some providers such as OpenDNS to suspend service in France. Quad9 has received an unfavorable French court ruling and states that starting November 24 it will no longer be able to offer its free cyberprotection service to users located in France.

**「Impact」** French users will lose access to Quad9&\#x27;s recursive DNS resolution service, with blocking expected to begin after November 24.

**「Community Discussion」** Commenters note the contradiction between geoIP blocking and selective denial, and compare punishing a DNS resolver to punishing a phone book for listing a criminal&\#x27;s number. The CTO confirms Quad9 will likely use geoIP filters to block French users after November 24, while others point to Cisco&\#x27;s earlier exit from France and Google/Cloudflare&\#x27;s forced compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad 9 - Wikipedia</a></li>
<li><a href="https://quad9.net/news/blog/au-revoir-france/">Farewell, France | Quad 9</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/">DNS Resolver Quad 9 Rejects French Piracy Blocks , Weighs Exit as...</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#internet censorship`, `#Quad9`, `#France`, `#network infrastructure`

---

<a id="item-tech-news-11"></a>
### [pwn.watch: Real-Time Dashboard for Exploited Vulnerabilities](https://pwn.watch/) ⭐️ 7.0/10

pwn.watch is a real-time dashboard that tracks actively exploited vulnerabilities and CVEs, offering a current view of security threats. The project was shared on Hacker News with no additional source text, but the submission title and URL indicate a monitoring resource focused on pwned systems. Community interest is high, with commenters noting the rapid rate of flaw discovery and comparing it to related tools such as supplychain.fail. The dashboard’s exact data sources, update frequency, and coverage are not detailed in the available information.

hackernews · mrkd · Oct 22, 14:08 · [Discussion](https://news.ycombinator.com/item?id=50195543)

**「Background」** pwn.watch is a live security-incident dashboard created by @thekitze that tracks actively exploited vulnerabilities. It surfaces entries such as CVE-2026-105134 and CVE-2026-105133, which CISA added to its Known Exploited Vulnerabilities catalog on 2026-10-14 based on evidence of active exploitation. The catalog lists vulnerabilities with confirmed active exploitation, serving as a key source for the dashboard.

**「Community Discussion」** Commenters broadly recognize the value of a live vulnerability dashboard, but they express alarm at the accelerating rate of flaw discovery and the potential role of LLMs in future incidents; one commenter notes pwn.watch complements their own CVE severity timeline tool, supplychain.fail.

<details><summary>References</summary>
<ul>
<li><a href="https://pwn.watch/">pwn . watch · live security incidents</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerabilities`, `#CVE`, `#exploits`, `#infosec`

---

<a id="item-tech-news-12"></a>
### [Anthropic Donates Agent Skills Standard to Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 7.0/10

Anthropic has donated its Agent Skills standard to the Agentic AI Foundation \(AAIF\) under the Linux Foundation, placing the specification under open, community-driven, vendor-neutral governance. The AAIF was co-founded by Anthropic with Block and OpenAI last year and already hosts the Model Context Protocol \(MCP\), which Anthropic previously donated. Anthropic stated it is committed to keeping Agent Skills open, community-driven, and vendor-neutral. Simon Willison noted that he predicted this move last December, when Anthropic first declared Agent Skills to be an open standard.

rss · Simon Willison · Oct 22, 18:09

**「Background」** Agent Skills defines a standard way to package and share reusable capabilities for AI agents, and Anthropic had previously announced it as an open standard. The Agentic AI Foundation is a Linux Foundation project co-founded by Anthropic, Block, and OpenAI to provide vendor-neutral governance for AI agent interoperability; Anthropic donated the Model Context Protocol to it earlier.

**「Impact」** Developers and organizations that adopt Agent Skills can now expect the specification to evolve under multi-vendor Linux Foundation governance rather than Anthropic&\#x27;s sole control, reducing single-vendor lock-in and potentially improving long-term stability.

**Tags**: `#AI`, `#agents`, `#open-source`, `#standards`, `#Anthropic`

---

<a id="item-tech-news-13"></a>
### [Carbon-X: Open 14.8B Joint DNA/Text Model](https://www.reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on/) ⭐️ 7.0/10

Carbon-X is an open 14.8B-parameter decoder-only model trained jointly on DNA and text, released with Apache 2.0 weights and capable of running on a single 80GB GPU in bfloat16. It accepts raw DNA sequences in a normal chat and answers in English, using a shared token stream with 6-mer tokens and mid-training on 302B tokens. Hugging Face reports a 66.7% average across five DNA benchmarks with thinking disabled, compared to 67.5% for GPT-6.1 Sol. The model has not been clinically validated, and its model card advises that exact sequence operations should still be handled by code; its value is enabling local analysis of sensitive genomic datasets.

reddit · r/MachineLearning · /u/jatingargiitk · Oct 22, 12:32

**「Background」** Carbon-X is an open 14.8B-parameter decoder-only language model released by HuggingFaceBio that is trained jointly on DNA sequences and natural-language text, allowing it to accept raw DNA in a chat interface and respond in English. Unlike traditional bioinformatics tools that rely on exact sequence-matching algorithms, it uses a shared token stream for text and DNA based on 6-mer tokens and was mid-trained on 302B tokens. This joint training approach is part of a broader effort to make large language models capable of analyzing biological sequences while keeping sensitive genomic data local.

**「Impact」** Researchers and developers working with sensitive genomic data can run Carbon-X locally on a single 80 GB GPU under Apache 2.0 to perform DNA benchmark tasks such as variant effect prediction without uploading sequences externally. However, the model has not been clinically validated and exact sequence operations should be handled by code.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/HuggingFaceBio/Carbon-X">HuggingFaceBio/ Carbon - X · Hugging Face</a></li>
<li><a href="https://huggingface.co/HuggingFaceBio/Carbon-X">HuggingFaceBio/ Carbon - X · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#bioinformatics`, `#language models`, `#open source AI`, `#DNA sequence modeling`, `#multimodal models`

---

<a id="item-tech-news-14"></a>
### [Open-XTTS-Trainer: Train All XTTS v2 Components and Add New Scripts](https://www.reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new/) ⭐️ 7.0/10

When Coqui AI shut down, XTTS v2 lacked official training code for its DVAE audio tokenizer and Latent HiFi-GAN vocoder, and fine-tuning new scripts broke on fixed vocabularies. The author released Open-XTTS-Trainer, an MPL-2.0 open-source modular pipeline that trains all three XTTS v2 components and extends tokenizers with new Unicode scripts. It includes a Gumbel-Softmax DVAE training loop, GPT vocabulary extension with dynamic embedding resizing, latent HiFi-GAN training with MPD/MSD discriminators, and runs on PyTorch 2.4+ without torchcodec. On an NVIDIA T4 using LJSpeech and JFK audio, reported losses decreased—HiFi-GAN mel loss from 190.83 to 63.49 and DVAE mel error from 8.14 to 2.71—though full end-to-end TTS inference has not been independently validated.

reddit · r/MachineLearning · /u/yashubhakt · Oct 22, 21:03

**「Background」** XTTS v2 is a zero-shot text-to-speech model originally developed by Coqui AI, composed of three trainable components: a DVAE audio tokenizer, a GPT model for text-to-token generation, and a latent HiFi-GAN vocoder. After Coqui announced its shutdown in January 2024, the official repository remained available but only the GPT fine-tuning recipe was commonly accessible; GitHub issues show users asking for ways to retrain the HiFi-GAN vocoder and DVAE, with no official open-source training code released for those stages. Additionally, XTTS v2&\#x27;s tokenizer was hardcoded for 17 languages, so attempts to fine-tune on new scripts like Arabic, Hindi, or Thai caused out-of-vocabulary token errors or matrix dimension mismatches.

**「Impact」** Developers and researchers can now fine-tune all three XTTS v2 components \(DVAE audio tokenizer, GPT text encoder, and Latent HiFi-GAN vocoder\) and add new language scripts such as Arabic or Indic by expanding the tokenizer, using an MPL-2.0 pipeline that runs on PyTorch 2.4+ without torchcodec. The reported GPU convergence benchmarks are component-level, so end-to-end TTS quality after training still requires independent validation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/coqui-ai/TTS/issues/3323">Retraining vocoder (hifigan) and dvae in XTTS #3323 - GitHub</a></li>
<li><a href="https://github.com/coqui-ai/TTS/discussions/3489">&quot;Coqui is shutting down.&quot; · coqui-ai TTS · Discussion #3489</a></li>
<li><a href="https://pyshine.com/coqui-ai-tts/">Coqui TTS: The Voice Zoo That Refused to Die - Inside idiap ...</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#open-source`, `#machine-learning`, `#speech-synthesis`, `#fine-tuning`

---

<a id="item-tech-news-15"></a>
### [Steerable TTS Edge Variant Hits 11.84 MB With Unchanged WER](https://www.reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer/) ⭐️ 7.0/10

WhissleAI released steer-tts-edge, an English steerable text-to-speech model whose entire app footprint \(weights, voices, text frontend, Python runtime\) is 11.84 MB. The acoustic model uses 9.25M parameters with attention and bidirectional Mamba-3 and is quantization-aware trained to int4; a 6.2M-param Vocos-style vocoder is distilled from charactr/vocos-mel-24khz and also int4 QAT, while the text frontend is pure NumPy. In local Open TTS Leaderboard protocol testing, the edge variant matches the fp32 v1 model at 0.96% WER and drops UTMOS only from 4.20 to 4.11. Steering remains intact with all 12 controls retaining at least 95% of their fp32 effect, and the model offers 50 style tags plus inline markup, running at RTF 0.053 on a 2018 Threadripper CPU with about 120 ms to first audio. Limitations include English-only support, 200 voices instead of 2,825, no on-device voice cloning or prompt-based control, and dequantized-to-fp32 loading means the win is size, not speed.

reddit · r/MachineLearning · /u/Working\_Hat5120 · Oct 22, 20:57

**「Background」** Quantization-aware training \(QAT\) incorporates low-precision quantization during training to preserve quality after weights are stored as int4. A vocoder converts acoustic features such as mel spectrograms into audio waveforms, and here it is distilled from a larger 24 kHz vocoder to reduce size. WER measures word error rate for intelligibility, while UTMOS estimates naturalness on a 1–5 scale.

**「Impact」** For developers targeting on-device English TTS within roughly 12 MB, steer-tts-edge preserves intelligibility and most steering behavior compared to the fp32 model, but runtime speed currently gains little because weights are dequantized to fp32 at load.

**Tags**: `#text-to-speech`, `#model quantization`, `#edge computing`, `#model distillation`, `#efficient AI`

---

<a id="item-tech-news-16"></a>
### [Smart TVs Send ACR Data After Opt-Out, Some Unencrypted](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 7.0/10

Researchers tested 12 smart TVs from 10 manufacturers in 5,943 controlled experiments and found that some models continued to send automatic content recognition \(ACR\) data even after users disabled ACR in settings. On two platforms, viewing content was transmitted unencrypted: VIDAA OS sent plaintext MQTT messages containing a non-resettable device ID and audio fingerprint, while Vizio&\#x27;s WatchFree+ encoded program names into unencrypted DNS queries that users cannot turn off. The study documents concrete data exfiltration after opt-out and highlights serious privacy and security issues in smart TV ACR implementations.

telegram · zaihuapd · Oct 22, 09:50

**「Background」** Automatic content recognition \(ACR\) is a feature in smart TVs that identifies what viewers are watching, often for advertising or personalization, and typically offers a setting to disable it. Previous research has raised concerns about smart TV data collection, but empirical measurements of post-opt-out behavior have been limited. This study provides controlled experimental evidence across multiple TV platforms.

**「Impact」** Users of affected VIDAA OS and Vizio WatchFree+ TVs cannot prevent these devices from sending viewing data even after disabling ACR, leaving unencrypted viewing information exposed to network observers and data collectors.

**Tags**: `#smart TV`, `#automatic content recognition`, `#privacy`, `#security`, `#data exfiltration`

---

<a id="item-tech-news-17"></a>
### [MiHoYo and Tsinghua Open-Source GameScaling Game Control Model](https://arxiv.org/abs/2610.28698v1) ⭐️ 7.0/10

MiHoYo&\#x27;s Honkai AI team, together with Tsinghua University and collaborators, has released GameScaling, an open-source vision-language game-operation model based on Qwen3.5. The model was further pretrained for keyboard and mouse control and is available in sizes from 0.8B to 27B parameters. Each output predicts the next 200 milliseconds of keyboard and mouse actions. A scaling study using 120 training configurations found that more data improves same-source performance, diversity helps transfer to similar games but has limited benefit for very different worlds. Eight checkpoints and an inference client are released under Apache-2.0; training code is not included.

telegram · zaihuapd · Oct 22, 11:32

**「Background」** Game-control models translate visual observations into low-level input actions such as mouse movement and key presses. Scaling studies vary model size and training data volume or diversity to measure performance trends. Qwen3.5 is the vision-language base model family used in this work.

**「Impact」** Developers and researchers can use the Apache-2.0 checkpoints and inference client to run or evaluate GameScaling, but cannot reproduce the continued pretraining because training code is not included.

**Tags**: `#game AI`, `#vision-language model`, `#open source`, `#scaling laws`, `#human-computer interaction`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China’s CSI 300 Falls 20% From June High as A-Shares Near Bear Market](https://www.bloomberg.com/news/articles/2026-10-22/china-stocks-set-for-bear-market-as-ai-trade-policy-hopes-fade) ⭐️ 7.0/10

China’s CSI 300 index was down 20% from its June high as of Thursday, putting A-shares close to a bear market. The decline came as investors reacted to weak corporate earnings—including a 12% drop in CATL shares after quarterly profit growth missed estimates—and the lack of substantive fiscal stimulus.

telegram · zaihuapd · Oct 22, 05:05

**「Background」** A 20% drop from a recent peak is commonly used to mark a bear market; the CSI 300 tracks major stocks listed in Shanghai and Shenzhen.

**Tags**: `#China stocks`, `#bear market`, `#market decline`, `#earnings miss`, `#fiscal policy`

---