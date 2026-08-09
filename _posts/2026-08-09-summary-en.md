---
layout: default
title: "Horizon Summary: 2026-08-09 (EN)"
date: 2026-08-09
lang: en
---

> From 30 items, 11 important content pieces were selected

---

**Technology News**
1. [Shopify Replaces Redis with MySQL for Inventory Reservations at Scale](#item-tech-news-1) ⭐️ 8.0/10
2. [Triton: Open-Source DirectX 11 Driver for QEMU](#item-tech-news-2) ⭐️ 8.0/10
3. [First AI-Designed Viable Bacteriophages Created](#item-tech-news-3) ⭐️ 8.0/10
4. [Tencent WorkBuddy Tops Office AI Agents, Becomes Strategic Product](#item-tech-news-4) ⭐️ 8.0/10
5. [macOS Screen Sharing Vulnerability Allows Password-less Login, Fixed in macOS 26.6.1](#item-tech-news-5) ⭐️ 8.0/10
6. [Cloudflare Predicts AI Bot Traffic Will Exceed Humans 1000x in 5 Years](#item-tech-news-6) ⭐️ 8.0/10
7. [World&\#x27;s largest single AI computing facility operational in Inner Mongolia](#item-tech-news-7) ⭐️ 8.0/10
8. [Claude Code Makes Auto Mode Default for Paid Plans](#item-tech-news-8) ⭐️ 7.0/10

**Financial News**
1. [Moonshot AI Restructures and Adds State Investors for Hong Kong IPO](#item-finance-news-1) ⭐️ 8.0/10
2. [Nevada Utility Sues Data Center Developer Over $1B Grid Upgrade, Warns of Rate Hikes](#item-finance-news-2) ⭐️ 8.0/10
3. [Berkshire Hathaway earnings rise 16% in Q2; CEO Abel deploys cash hoard](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Shopify Replaces Redis with MySQL for Inventory Reservations at Scale](https://shopify.engineering/scaling-inventory-reservations) ⭐️ 8.0/10

Shopify migrated its high-throughput inventory reservation system from Redis to MySQL. To maintain performance, they implemented a bounded row-pool design where each sellable unit is represented by a row, but the pool is capped at 1,000 rows per item/location combination, with a replenishment process adding rows as needed. This approach avoids large scans and leverages row-level locking, enabling MySQL to handle the workload. The move was driven by the need for stronger consistency and operational simplicity, though it required careful lock ordering to prevent deadlocks.

hackernews · adletbalzhanov · Aug 8, 22:32 · [Discussion](https://news.ycombinator.com/item?id=49226536)

**「Background」** Shopify&\#x27;s inventory system must handle high-throughput reservations during checkout, temporarily holding stock while payments process to prevent overselling. Traditionally, they used Redis, an in-memory data store, but scaling it for their volume proved complex. The article details a migration to MySQL using a novel row-per-unit pool design capped at 1,000 rows per item/location to maintain performance at scale.

**「Impact」** Shopify&\#x27;s successful migration demonstrates that a bounded row-pool design in MySQL can replace Redis for high-throughput inventory reservations, offering a viable alternative for teams prioritizing consistency and operational simplicity.

**「Community Discussion」** Commenters debate the design choices, proposing alternatives such as per-cart reservations or direct inventory deduction with rollback, while others critique the post&\#x27;s clarity and question if the row-pool approach would pass a system design interview.

<details><summary>References</summary>
<ul>
<li><a href="https://shopify.engineering/scaling-inventory-reservations">We replaced Redis with MySQL for inventory ... - Shopify</a></li>

</ul>
</details>

**Tags**: `#software-engineering`, `#databases`, `#scaling`, `#mysql`, `#redis`

---

<a id="item-tech-news-2"></a>
### [Triton: Open-Source DirectX 11 Driver for QEMU](https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/) ⭐️ 8.0/10

Triton is a newly introduced open-source DirectX 11 driver for QEMU that enables hardware-accelerated graphics in Windows virtual machines. This development addresses a long-standing challenge for Linux users who previously needed complex GPU passthrough setups to achieve similar performance in Windows guests. The driver promises to improve the feasibility of gaming and graphical applications within VMs, particularly for systems with a single discrete GPU. The implementation is detailed in a technical article, though full backward compatibility with earlier DirectX versions remains unclear from the initial announcement.

hackernews · electricant · Aug 8, 13:33 · [Discussion](https://news.ycombinator.com/item?id=49221711)

**「Background」** QEMU is a popular open-source virtualization platform that can leverage virglrenderer and Mesa to provide 3D graphics acceleration to guest virtual machines. DirectX 11 is Microsoft’s graphics API commonly required by Windows applications and games. Until now, no open-source DirectX 11 driver existed specifically for QEMU, with the only working open-source user-mode driver being part of VirtualBox and not easily adaptable.

**「Impact」** Linux users now have an open-source option for running DirectX 11 applications with hardware acceleration in Windows virtual machines, removing the previous requirement for dedicated GPU passthrough or dual-boot configurations.

**「Community Discussion」** Commenters express enthusiasm for the driver, while raising questions about support for earlier DirectX versions and compatibility with other virtualization platforms like VirtualBox.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/">Introducing Triton: DirectX 11 driver for QEMU | UTM Blog</a></li>
<li><a href="https://www.phoronix.com/news/Triton-DirectX-11-QEMU-Driver">AI Helped Create A DirectX 11 Driver For QEMU VMs - Phoronix</a></li>

</ul>
</details>

**Tags**: `#virtualization`, `#graphics-drivers`, `#qemu`, `#directx`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [First AI-Designed Viable Bacteriophages Created](https://www.reddit.com/r/MachineLearning/comments/1vjj4pr/r_generative_design_of_novel_bacteriophages_with/) ⭐️ 8.0/10

Researchers report the first generative design of viable bacteriophage genomes using genome language models Evo 1 and Evo 2. Using the lytic phage ΦX174 as a template, they generated whole-genome sequences with desired host tropism and realistic genetic architectures. Experimental validation produced 16 viable phages that exhibit substantial evolutionary novelty. This demonstrates that frontier language models can design functional genomes at whole-genome scale, advancing AI-driven synthetic biology.

reddit · r/MachineLearning · /u/moschles · Aug 9, 07:11

**「Background」** Bacteriophages are viruses that infect bacteria and are widely used as model systems. Genome language models are AI models trained on DNA sequences to understand and generate genomic information. Evo 1 and Evo 2 are frontier models that apply this approach. ΦX174 is a small, well-characterized lytic phage often used as a template in synthetic biology experiments.

**「Impact」** The success in generating functional phage genomes paves the way for AI-driven design of custom bacteriophages for applications in phage therapy, biocontrol, and fundamental research.

**Tags**: `#synthetic biology`, `#genomic AI`, `#language models`, `#generative design`, `#machine learning`

---

<a id="item-tech-news-4"></a>
### [Tencent WorkBuddy Tops Office AI Agents, Becomes Strategic Product](https://mp.weixin.qq.com/s/TRUjakoaprGFSYYQB301xw) ⭐️ 8.0/10

Tencent&\#x27;s WorkBuddy has been elevated to one of the company&\#x27;s highest strategic AI priorities, with internal references comparing it to QQ and WeChat. In Q2 2026, it ranked first among domestic office AI agent platforms with 20.97 million monthly PC visits and reached 20 million monthly active users. The product integrates with Tencent Docs, WeCom, and Tencent Meeting, and supports multiple models including Hunyuan, DeepSeek, and GLM. In July, the QClaw business was merged into the WorkBuddy unit to streamline development. No commercialization KPIs have been set, and the focus this year is on expanding enterprise customer coverage.

telegram · zaihuapd · Aug 8, 13:50

**「Background」** Office AI agents are emerging tools that automate tasks like document drafting, meeting summaries, and workflow management. Tencent, a leading Chinese tech conglomerate, has been expanding its enterprise software ecosystem through products such as WeCom and Tencent Docs.

**「Impact」** Tencent&\#x27;s prioritization of WorkBuddy and its integration with core productivity apps could drive wider enterprise AI agent adoption in China and intensify competition among tech giants.

**Tags**: `#AI agents`, `#office intelligence`, `#Tencent`, `#enterprise AI`, `#LLM applications`

---

<a id="item-tech-news-5"></a>
### [macOS Screen Sharing Vulnerability Allows Password-less Login, Fixed in macOS 26.6.1](https://x.com/calif_io/status/2086022794840793454) ⭐️ 8.0/10

A critical vulnerability \(CVE-2026-65400\) in macOS screen sharing allows any network attacker to log into any account without a password when the feature is enabled. Apple patched the flaw in macOS 26.6.1, and users are urged to update immediately. Security researchers have released a proof-of-concept exploit and will publish a complete technical analysis tomorrow after reverse engineering the fix.

telegram · zaihuapd · Aug 8, 14:20

**「macOS Screen Sharing Background」** macOS includes a built-in Screen Sharing feature that enables remote desktop connections over the network, typically requiring a valid username and password. Vulnerability CVE-2026-65400 allowed an attacker to bypass this authentication when Screen Sharing was enabled, granting unauthorized access. Apple addressed the issue with improved state management in macOS Tahoe 26.6.1, Sequoia 15.7.9, and Sonoma 14.8.9.

**「Impact」** This vulnerability enables unauthorized access to any macOS system with screen sharing turned on, making prompt installation of the macOS 26.6.1 update critical to prevent exploitation.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-65400">Nvd - Cve-2026-65400</a></li>
<li><a href="https://support.apple.com/en-us/148170">About the security content of macOS Tahoe 26.6.1</a></li>

</ul>
</details>

**Tags**: `#macOS`, `#security`, `#vulnerability`, `#CVE-2026-65400`, `#screen sharing`

---

<a id="item-tech-news-6"></a>
### [Cloudflare Predicts AI Bot Traffic Will Exceed Humans 1000x in 5 Years](https://www.techspot.com/news/113410-cloudflare-humans-could-become-rounding-error-bots-generate.html) ⭐️ 8.0/10

During Cloudflare&\#x27;s Q2 earnings call, CFO Thomas Seifert stated that if current trends continue, non-human internet traffic could reach 1,000 times human traffic within five years, reducing humans to a &\#x27;rounding error.&\#x27; CEO Matthew Prince noted that the crossover point where bot traffic exceeds human traffic, originally forecast for late 2027, has already occurred this year. The surge is primarily driven by AI agents that behave like normal browsers but can generate thousands of requests from a single prompt, operating at machine speed.

telegram · zaihuapd · Aug 9, 02:08

**「Background」** Cloudflare is a leading content delivery network and web security provider that processes a substantial portion of global internet traffic, giving it unique visibility into traffic composition. AI agents, which autonomously crawl and interact with web content, are increasingly deployed for data gathering and task execution, causing a rapid rise in non-human traffic that already accounts for a significant share of all requests.

**「Impact」** If the prediction materializes, website operators and internet infrastructure providers will need to massively scale capacity and invest in advanced bot-management systems to handle the surge, potentially altering the economics and architecture of the web.

**Tags**: `#AI`, `#bots`, `#internet traffic`, `#Cloudflare`, `#infrastructure`

---

<a id="item-tech-news-7"></a>
### [World&\#x27;s largest single AI computing facility operational in Inner Mongolia](https://www.globaltimes.cn/page/202608/1367666.shtml) ⭐️ 8.0/10

On August 6, Envision Group announced the commissioning of its Ulanqab Xinghe base, the world&\#x27;s largest single AI computing facility. The 120,000-square-meter facility supports up to one million GPUs for parallel computing, with a planned total capacity of 2 GW and over 80% green energy usage. Located in Ulanqab—a key node of China&\#x27;s &\#x27;East Data West Computing&\#x27; project—it is about 240 km from Beijing, offering 4.2-millisecond data transmission latency and electricity costs roughly 50% lower than in the Beijing-Tianjin-Hebei region. The base is the first flagship project under Envision&\#x27;s &\#x27;Gobi Mission&\#x27; plan, intended to provide a replicable model for domestic AI computing clusters.

telegram · zaihuapd · Aug 9, 05:06

**「Background」** Ulanqab is one of eight national hubs under China&\#x27;s &\#x27;East Data West Computing&\#x27; project, which relocates compute-intensive infrastructure to western regions for cheaper renewable energy and land. Envision Group&\#x27;s &\#x27;Mission Gobi&\#x27; initiative aims to build 5GW of green AI computing capacity in deserts globally by 2030, with this facility serving as the first flagship project.

**「Impact」** The facility may lower barriers for large-scale AI training and inference in China, particularly for organizations prioritizing green energy, though its practical impact hinges on utilization rates and integration with existing AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202608/1367666.shtml">World&#x27;s largest single AI computing facility enters operation in China&#x27;s Ulanqab - Global Times</a></li>
<li><a href="https://aijourn.com/envision-commissions-galaxy-campus-in-ulanqab-establishing-a-new-model-for-gigawatt-scale-ai-infrastructure/">Envision Commissions Galaxy Campus in Ulanqab, Establishing a New Model for Gigawatt-Scale AI Infrastructure | The AI Journal</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data center`, `#large-scale computing`, `#green energy`, `#China`

---

<a id="item-tech-news-8"></a>
### [Claude Code Makes Auto Mode Default for Paid Plans](https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything) ⭐️ 7.0/10

Anthropic will set auto mode as the default in Claude Code for Pro, Max, and Team plans starting on August 14th, signaling strong confidence in its automated code editing safety. In evaluations, auto mode blocked 89% of dangerous commands in a study of 1,053 paid testers, compared to only 13.6% for human reviewers, and a third-party test of 720 prompt injection attacks against Claude models found zero successes. The change aims to reduce friction for developers by minimizing manual approvals, but author Simon Willison highlights remaining risks, particularly from malicious third-party packages, and advises running agents with limited access to sensitive data and tools.

rss · Simon Willison · Aug 8, 22:36

**「Background」** Auto mode in Claude Code allows the agent to execute code and system commands without requiring user approval for each action, enabling faster autonomous workflows. It was previously available as an opt-in feature, but security concerns—especially around prompt injection and accidental harmful actions—had made manual approval the default. Anthropic&\#x27;s decision reflects internal adoption \(nearly everyone at the company uses auto mode\) and new safety evaluations.

**「Impact」** Starting August 14th, Pro, Max, and Team plan users will have auto mode enabled by default, reducing the need for constant manual approvals but increasing exposure to risks if malicious instructions are injected or harmful actions are not blocked.

**Tags**: `#claude-code`, `#anthropic`, `#ai-tools`, `#developer-tools`, `#automation`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Moonshot AI Restructures and Adds State Investors for Hong Kong IPO](https://www.theblockbeats.info//flash/360480) ⭐️ 8.0/10

Moonshot AI is restructuring and introducing state-backed investors to secure Hong Kong IPO approval, according to the Financial Times. Its valuation is estimated up to $50 billion.

telegram · zaihuapd · Aug 8, 09:02

**「Background」** Moonshot AI, a Chinese AI startup, has recently closed two funding rounds and already counts the National Social Security Fund, local government guidance funds, and a People&\#x27;s Daily affiliate among its investors.

**Tags**: `#AI`, `#IPO`, `#state-owned investment`, `#Chinese tech`, `#venture capital`

---

<a id="item-finance-news-2"></a>
### [Nevada Utility Sues Data Center Developer Over $1B Grid Upgrade, Warns of Rate Hikes](https://www.sina.cn/news/detail/5329879165568444.html) ⭐️ 8.0/10

Nevada&\#x27;s largest utility has sued a data center developer, alleging it is trying to shift the cost of a required $1 billion grid upgrade to consumers; the utility warns that without the developer covering the expense, it may raise electricity rates for the 90% of state customers it serves.

telegram · zaihuapd · Aug 9, 01:35

**「Background」** The lawsuit follows a dispute between NV Energy and Tract, a Denver-based developer building two data centers in Nevada, over who should pay for $1 billion in grid upgrades needed to serve the facilities, which would consume about one-third of the utility’s generation capacity.

**「Impact」** If rate increases occur, Nevada households and businesses served by the utility could face higher electricity bills.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/nevada-data-center-lawsuit-ai-energy-costs/">Nevada energy company sues data center in first-of-its-kind fight over who should pay for AI buildout - CBS News</a></li>

</ul>
</details>

**Tags**: `#energy`, `#data centers`, `#electricity rates`, `#legal dispute`, `#infrastructure`

---

<a id="item-finance-news-3"></a>
### [Berkshire Hathaway earnings rise 16% in Q2; CEO Abel deploys cash hoard](https://www.cnbc.com/2026/08/08/berkshire-hathaway-earnings-q2-2026.html) ⭐️ 7.0/10

Berkshire Hathaway reported a 16% increase in operating earnings to $12.98 billion in the second quarter of 2026, and new CEO Greg Abel began deploying the company&\#x27;s record cash pile, with $4.5 billion in share buybacks and nearly $20 billion in net equity purchases.

rss · CNBC Finance · Aug 8, 13:28

**「Background」** The cash deployment marks a shift after 14 consecutive quarters of net stock sales under former CEO Warren Buffett, who handed over the role at the start of 2026.

**Tags**: `#Berkshire Hathaway`, `#earnings`, `#capital allocation`, `#stock buybacks`, `#equity investments`

---