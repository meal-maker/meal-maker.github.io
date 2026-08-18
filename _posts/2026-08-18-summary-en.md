---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 38 items, 14 important content pieces were selected

---

**Technology News**
1. [Fixing a Bricked Framework 13 AMD 7040 After Failed Firmware Update](#item-tech-news-1) ⭐️ 8.0/10
2. [Linux 7.3 improves performance when running out of vRAM](#item-tech-news-2) ⭐️ 8.0/10
3. [Mojo Is Now Open Source Under Apache 2](#item-tech-news-3) ⭐️ 8.0/10
4. [TrendForce: China&\#x27;s Domestic AI Chips to Near 90% by 2026](#item-tech-news-4) ⭐️ 8.0/10
5. [Claude Code Weekly Limit Promotion Ends August 19, 2026](#item-tech-news-5) ⭐️ 7.0/10
6. [Qwen 3.8 27B Scores 52 on Artificial Analysis Intelligence Index](#item-tech-news-6) ⭐️ 7.0/10
7. [Camera-Equipped AirPods B790 Reportedly Shown in macOS Tahoe 26.7 RC](#item-tech-news-7) ⭐️ 7.0/10
8. [Enterprise WeChat 5.0.10 Opens CLI and MCP to Agents](#item-tech-news-8) ⭐️ 7.0/10
9. [China Orders Early Uninstall of Customized Windows 10 in State Agencies](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Buy-Now-Pay-Later Loans Expand to Rent and Utilities; U.S. Borrowing Hits $160 Billion in 2025](#item-finance-news-1) ⭐️ 8.0/10
2. [Kweichow Moutai posts first half-year profit drop since 2014](#item-finance-news-2) ⭐️ 7.0/10
3. [Bond market pressure squeezes U.S. households as mortgage rates hit 6.75%](#item-finance-news-3) ⭐️ 7.0/10
4. [Jeanie Buss opposes sale of family&\#x27;s 17.8% Lakers stake to Iger and Kushner](#item-finance-news-4) ⭐️ 7.0/10
5. [Apple US App Store Commission Revenue Falls 18% as User Spending Declines](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Fixing a Bricked Framework 13 AMD 7040 After Failed Firmware Update](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 8.0/10

A technical walkthrough published in August 2026 describes how to unbrick a Framework 13 laptop with an AMD 7040 series processor after a failed firmware update. The article offers a detailed repair procedure intended to help affected users recover their devices without replacing hardware. The issue appears to be widespread among this laptop model, prompting the author to document the steps publicly. The guide emphasizes practical troubleshooting and recovery, reflecting a need for better vendor support for firmware failures.

hackernews · jp\_sc · Aug 18, 13:18 · [Discussion](https://news.ycombinator.com/item?id=49345220)

**「Background」** Framework laptops are designed for modular repair, but a failed UEFI/BIOS update can corrupt the SPI flash firmware and leave the system unbootable, a condition often called &quot;bricked.&quot; The author recovered a Framework 13 AMD 7040 series laptop by flashing the firmware chip directly with inexpensive tools instead of replacing the motherboard as suggested by Framework support.

**「Impact」** Owners of Framework 13 AMD 7040 laptops who experience a bricked state after a firmware update can use the described steps to attempt recovery instead of discarding or replacing the mainboard.

**「Community Discussion」** Commenters share similar BIOS bricking experiences on other laptops and criticize manufacturers for poor firmware update support; one suggests legal action, while another notes a vendor fixed the issue after receiving a flash dump. Some also express regrets about Framework&\#x27;s component lock-in and stock issues.

<details><summary>References</summary>
<ul>
<li><a href="https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/">Fixing a bricked AMD 7040 series Framework 13” laptop with $20 tools | Quantum</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#firmware`, `#bios`, `#repair`, `#framework-laptop`

---

<a id="item-tech-news-2"></a>
### [Linux 7.3 improves performance when running out of vRAM](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

A Linux kernel change described on Pixelcluster.dev improves performance when running out of VRAM by better handling memory overcommit. The change is not yet upstream, according to the analysis summary, and is associated with Linux 7.3. The mechanism involves improved handling of GPU memory overcommit, potentially reducing slowdowns or stalls when applications exceed available VRAM.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**「Background」** This item builds on prior work by pixelcluster on improving AMDGPU VRAM management for low-end GPUs. When applications request more video memory than physically available, the kernel must handle VRAM overcommit, and poor handling can cause severe performance instability. The initial patchset for better VRAM overcommit handling has been merged and is queued for Linux 7.3, with further improvements still being developed for future kernel releases.

**「Impact」** Linux 7.3 is expected to land initial kernel code improving VRAM management, which should reduce performance degradation when GPU memory is overcommitted, particularly benefiting gamers and users with limited VRAM on supported drivers.

**「Community Discussion」** Comments are generally positive, praising the article and expressing eagerness for the change to be upstreamed, with some noting that recent kernel releases like 7.2 already brought performance improvements. Concerns include Nvidia&\#x27;s lack of VRAM paging support, a hope for similar handling of system RAM exhaustion, and a suggestion that applications should provide hints about VRAM allocation preferences rather than relying on kernel guessing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7.3 To Land Initial Code Improving vRAM Management, More Improvements Coming - Phoronix</a></li>
<li><a href="https://pixelcluster.dev/VRAM-Overcommit/">VRAM Management Part 2: Beyond the Limits of Physical VRAM | pixelcluster&#x27;s GPU blog</a></li>
<li><a href="http://pixelcluster.dev/VRAM-Mgmt-fixed/">Fixing AMDGPU&#x27;s VRAM management for low-end GPUs | pixelcluster&#x27;s GPU blog</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7 . 3 To Land Initial Code Improving vRAM Management , More...</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#VRAM`, `#GPU`, `#memory management`, `#performance`

---

<a id="item-tech-news-3"></a>
### [Mojo Is Now Open Source Under Apache 2](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 8.0/10

Mojo, the Python-inspired language for AI and systems programming, has released its compiler and toolchain under the Apache 2 license, fulfilling a promise first made in May 2023 and following the 1.0 release last week. The language is now positioned as its own language rather than a strict Python superset, with syntax inspired by Python and optimized to make GPU programming as painless as possible. This shift was announced in August 2025 when the roadmap stated that Mojo may or may not evolve into a full superset of Python.

rss · Simon Willison · Aug 18, 21:39

**「Background」** Mojo was introduced in 2023 with the goal of being a superset of Python to bootstrap its ecosystem, but that plan changed in 2025 to a standalone language optimized for GPU workloads. Open-sourcing the compiler and toolchain removes a key licensing barrier for developers evaluating the language.

**「Impact」** Developers who were waiting for an open-source release can now inspect, modify, and distribute the Mojo compiler and toolchain under the permissive Apache 2 license, which may accelerate its adoption for GPU and AI workloads.

**Tags**: `#programming-languages`, `#open-source`, `#AI-systems`, `#compilers`, `#high-performance-computing`

---

<a id="item-tech-news-4"></a>
### [TrendForce: China&\#x27;s Domestic AI Chips to Near 90% by 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd) ⭐️ 8.0/10

TrendForce predicts that China&\#x27;s domestic AI accelerators will account for nearly 90% of the country&\#x27;s local market by 2026, up from 45% last year. Cambricon and Huawei are expected to be the biggest winners in the shift away from Nvidia and AMD. In 2025, Nvidia shipped about 2.2 million units for a 55% share, while Huawei shipped 812,000 units for a 20.3% share. To meet the projected domestic share, China would need to increase its high-end AI chip output by 2.2 times to about 1.96 million units within a year, but production capacity remains uncertain.

telegram · zaihuapd · Aug 18, 13:03

**「Background」** TrendForce is a market research firm; this forecast covers AI accelerators, specialized processors for AI workloads, in China&\#x27;s domestic market. The anticipated shift reflects ongoing demand for local alternatives to U.S. suppliers such as Nvidia and AMD, in which Cambricon and Huawei are key domestic players.

**「Impact」** For Chinese AI hardware buyers and data-center operators, a 90% domestic accelerator share by 2026 would sharply reduce reliance on Nvidia and AMD, but it hinges on domestic manufacturers scaling high-end chip production roughly 2.2x to about 1.96 million units within a year, a capacity that TrendForce indicates is not guaranteed.

**Tags**: `#AI accelerators`, `#semiconductors`, `#China tech`, `#market forecast`, `#Huawei`

---

<a id="item-tech-news-5"></a>
### [Claude Code Weekly Limit Promotion Ends August 19, 2026](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion) ⭐️ 7.0/10

Anthropic&\#x27;s Claude Code temporary promotion, which raised weekly usage limits by 50% from May 13, 2026 through August 19, 2026, is ending and limits will revert to pre-promotion levels. The change affects developers who used the extra capacity for AI-assisted coding. Community discussion has centered on whether Anthropic&\#x27;s token-heavy approach is sustainable compared with more efficiency-focused alternatives such as OpenAI&\#x27;s Codex. Some commenters report already hitting 90–100% of their $200/month Claude Code limits and considering a switch to Codex or 5.6 sol.

hackernews · tyre · Aug 18, 17:02 · [Discussion](https://news.ycombinator.com/item?id=49348751)

**「Background」** Claude Code is Anthropic&\#x27;s terminal-based coding assistant tied to subscription usage limits. For a limited-time promotion from May 13, 2026 through August 19, 2026 at 11:59 PM PT, Anthropic increased those weekly usage limits by 50% above the normal plan levels. After the promotion ends, the limits are scheduled to return to their pre-promotion values, which is the change described in the source article.

**「Impact」** Claude Code users on the $200/month plan who regularly approach their weekly cap will see lower limits after August 19, 2026, reducing available AI coding capacity per week.

**「Community Discussion」** Several commenters say they will switch away from Claude Code if limits drop, citing outages and poor Opus/Fable utility; some report already using Codex and 5.6 sol with higher limits and better output than Opus 4.8. Others debate that OpenAI&\#x27;s emphasis on token efficiency may prove more sustainable than Anthropic&\#x27;s token-heavy approach.

<details><summary>References</summary>
<ul>
<li><a href="https://www.threads.com/@technewsonweb/post/Da8TDHqEykX/claude-code-may-august-weekly-limits-promotion-now-run-through-august-limited/">Claude Code May–August 2026 weekly limits promotion - now run through August 19, 2026. ( limited-time promotion that increases weekly usage limits in Claude Code by 50%. )</a></li>
<li><a href="https://aicatchup.com/news/claude-code-weekly-limits-50-percent-promo">Claude Code Weekly Limits +50% Promo -- Now Through August 19 | AI Catchup</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#Anthropic`, `#AI coding tools`, `#usage limits`, `#product update`

---

<a id="item-tech-news-6"></a>
### [Qwen 3.8 27B Scores 52 on Artificial Analysis Intelligence Index](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 7.0/10

Qwen 3.8 27B, a 27-billion-parameter model, scored 52 on the Artificial Analysis Intelligence Index as of August 2026. This matches the maximum score of GPT-5.6 Luna and is only one point behind the maximum scores of GLM-5.2 \(753B parameters\) and DeepSeek V4 Pro 0813 \(1.7T parameters\). GPT-5.6 Luna&\#x27;s parameter count is unknown, but Simon Willison notes it is presumably much larger than 27B. The result highlights exceptional efficiency, as a relatively small model approaches or matches far larger frontier models on the benchmark.

rss · Simon Willison · Aug 17, 23:58

**「Background」** The Artificial Analysis Intelligence Index is a benchmark that provides a single score for language model intelligence. Qwen 3.8 27B is a 27-billion-parameter model from the Qwen family, while the compared GPT-5.6 Luna has undisclosed size and GLM-5.2 and DeepSeek V4 Pro 0813 have 753B and 1.7T parameters respectively. This size difference is central to the item&\#x27;s observation that a relatively small model can match or nearly match much larger models.

**「Impact」** For developers and organizations, this suggests they may obtain near-frontier benchmark performance with drastically lower compute and memory requirements than models with 753B or 1.7T parameters, though the source does not specify deployment costs or task-specific caveats.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen3.8 27B - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/">Qwen 3.8 27B scores 52 on the Artificial Analysis Intelligence Index</a></li>

</ul>
</details>

**Tags**: `#ai`, `#llms`, `#qwen`, `#benchmark`, `#model-efficiency`

---

<a id="item-tech-news-7"></a>
### [Camera-Equipped AirPods B790 Reportedly Shown in macOS Tahoe 26.7 RC](https://www.macrumors.com/2026/08/17/camera-equipped-airpods-macos-26-7/) ⭐️ 7.0/10

MacRumors reports that Apple is developing camera-equipped AirPods under product code B790. A demo in macOS Tahoe 26.7 RC shows the AirPods camera recognizing a book title and using visual intelligence to save the information; Siri can answer questions about the wearer&\#x27;s surroundings and record details. Bloomberg&\#x27;s Mark Gurman says the product could launch as early as September. If accurate, this would bring visual intelligence to a new wearable form factor.

telegram · zaihuapd · Aug 18, 02:00

**「Background」** Bloomberg’s Mark Gurman previously reported that Apple could launch AirPods with cameras as early as this year under the codename B790, and the latest references in macOS 26.7 RC give the clearest look yet at that feature. The demo shows the AirPods camera feeding information to Visual Intelligence, allowing Siri to answer questions about the wearer’s surroundings and log information. Engadget notes that the concept was first tipped by Gurman back in May.

**「Impact」** A September launch would give AirPods users hands-free visual recognition and Siri-based note-taking without an iPhone, though the report remains unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/17/airpods-with-camera-get-their-clearest-leak-yet/">AirPods with cameras get their clearest leak yet - 9to5Mac</a></li>
<li><a href="https://www.macrumors.com/2026/08/17/camera-equipped-airpods-macos-26-7/">Apple&#x27;s Camera-Equipped AirPods Confirmed: See Them in Action - MacRumors</a></li>
<li><a href="https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/">Apple appears to have leaked its camera-equipped AirPods - Engadget</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AirPods`, `#visual intelligence`, `#macOS`, `#AI`

---

<a id="item-tech-news-8"></a>
### [Enterprise WeChat 5.0.10 Opens CLI and MCP to Agents](https://mp.weixin.qq.com/s/uJf57P15-FQL_u6jLHiGYA) ⭐️ 7.0/10

Enterprise WeChat version 5.0.10 has opened CLI and MCP capabilities to all enterprises. Agents such as WorkBuddy, DeepSeek Harness, and self-built enterprise agents can directly invoke 10 core office modules under permission isolation between humans and AI, manual approval for critical operations, time-limited authorization, and complete auditing. The integration also allows AI to read documents and spreadsheets, analyze data, and generate proposal presentations or business dashboards. This gives mainstream agents a controlled path into core Enterprise WeChat office workflows.

telegram · zaihuapd · Aug 18, 06:22

**「Background」** Enterprise WeChat \(WeCom\) is Tencent’s workplace communication and collaboration platform, and its 5.0.10 release marks a broader rollout of agent-facing interfaces to all enterprises. MCP \(Model Context Protocol\) is an open standard for connecting AI models or agents to external tools and data sources, while CLI provides scriptable command-line access; together these allow external agents to invoke office modules such as documents, tables, and approval workflows. WorkBuddy is Tencent Cloud’s AI office agent that can autonomously plan and deliver multi-modal tasks, and it is one of the agents named as compatible with the new interfaces.

**「Impact」** Enterprise developers can now integrate approved agents into Enterprise WeChat’s core office modules with built-in permission isolation, manual approval gates, time-limited access, and audit logs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办 公 新范式</a></li>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>

</ul>
</details>

**Tags**: `#enterprise-software`, `#ai-agents`, `#mcp`, `#enterprise-wechat`, `#automation`

---

<a id="item-tech-news-9"></a>
### [China Orders Early Uninstall of Customized Windows 10 in State Agencies](https://www.bloomberg.com/news/articles/2026-08-18/china-axing-microsoft-windows-from-state-agencies-ahead-of-plan) ⭐️ 7.0/10

China&\#x27;s Ministry of State Security is requiring some government-related agencies to uninstall a customized Windows 10 ahead of schedule, moving the stop-use plan earlier than originally set for February 2027. The directive stems from data security concerns, though the specific vulnerability was not disclosed. Microsoft said it has not identified a security incident affecting the product and that it still receives regular security updates. The affected product is a customized version of Windows 10, but technical details and the full scope of affected agencies are limited.

telegram · zaihuapd · Aug 18, 06:22

**「Background」** The affected software is a customized Windows 10 edition developed for Chinese government customers; it was introduced in 2016 after meeting several of China&\#x27;s security requirements. Reports refer to it as a government-only version or government edition rather than the standard consumer build.

**「Impact」** Government agencies in China that use the customized Windows 10 may need to migrate to alternative systems sooner than planned, but the exact scope and timeline beyond being advanced by months remain unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10">China reportedly orders state agencies to uninstall ... | Tom&#x27;s Hardware</a></li>
<li><a href="https://wccftech.com/china-state-agencies-uninstall-windows-10-cmit-government-edition/">China ’s State -Linked Firms Are Moving Away From Windows 10 Due...</a></li>
<li><a href="https://www.straitstimes.com/asia/east-asia/china-removes-microsoft-windows-at-state-users-ahead-of-plan">China removes Microsoft Windows at state users... | The Straits Times</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#Windows 10`, `#data security`, `#government IT`, `#technology policy`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Buy-Now-Pay-Later Loans Expand to Rent and Utilities; U.S. Borrowing Hits $160 Billion in 2025](https://www.nytimes.com/2026/08/17/business/buy-now-pay-later.html) ⭐️ 8.0/10

Buy-now-pay-later lenders, which split purchases into installments, expanded into utilities, telecom, insurance, rent, and medical expenses, and U.S. consumers borrowed $160 billion through such loans in 2025, nearly double the 2023 amount, The New York Times reported.

telegram · zaihuapd · Aug 18, 01:41

**「Background」** A LendingTree survey cited in the report found half of users said they could not make ends meet without these loans, and a quarter were carrying at least three at the same time.

**「Impact」** Because direct debits can trigger overdraft fees and most buy-now-pay-later loans are not reported to credit bureaus, households using them for rent and utilities may face higher debt-trap risks.

**Tags**: `#buy now pay later`, `#consumer credit`, `#household debt`, `#fintech`, `#US economy`

---

<a id="item-finance-news-2"></a>
### [Kweichow Moutai posts first half-year profit drop since 2014](https://www.cnbc.com/2026/08/19/china-economy-moutai-ai-property.html) ⭐️ 7.0/10

Kweichow Moutai reported first-half net profit fell 1.95% to 44.5 billion yuan \($6.6 billion\), its first decline for the first six months since 2014, according to Wind Information data; the drop follows a 4.5% decline for all of 2025, the first annual fall on record.

rss · CNBC Finance · Aug 18, 23:18

**「Background」** Moutai, a premium baijiu long used at government and business dinners, was China&\#x27;s largest listed company by market value from 2020 to 2023. Analysts link weaker baijiu demand to China&\#x27;s anti-corruption drive and economic shift toward tech, while Citi and Morningstar say a wholesale-to-direct sales shift may have distorted reported results.

**Tags**: `#Moutai`, `#China economy`, `#earnings`, `#consumer staples`, `#baijiu`

---

<a id="item-finance-news-3"></a>
### [Bond market pressure squeezes U.S. households as mortgage rates hit 6.75%](https://www.cnbc.com/2026/08/18/bond-market-treasury-yields-warsh-main-street.html) ⭐️ 7.0/10

Rising U.S. Treasury yields are pushing up household borrowing costs, with a 30-year mortgage now at 6.75%, according to CNBC analysis.

rss · CNBC Finance · Aug 18, 16:48

**「Background」** The run-up in long-term yields has been driven by the Iran war oil shock, heavy tech borrowing for AI infrastructure, and a U.S. budget deficit the CBO estimates at $2.1 trillion for the fiscal year through September, while new Fed Chair Kevin Warsh has signaled comfort with higher market rates.

**Tags**: `#Bond market`, `#Treasury yields`, `#Federal Reserve`, `#Consumer impact`, `#Inflation`

---

<a id="item-finance-news-4"></a>
### [Jeanie Buss opposes sale of family&\#x27;s 17.8% Lakers stake to Iger and Kushner](https://www.cnbc.com/2026/08/17/jeanie-buss-opposes-sale-family-stake.html) ⭐️ 7.0/10

Los Angeles Lakers governor Jeanie Buss is opposing the sale of her family&\#x27;s 17.8% stake in the team to Bob Iger and Joshua Kushner, saying her siblings cannot sell without her consent under a 2017 court order.

rss · CNBC Finance · Aug 18, 21:29

**「Background」** The dispute follows an earlier ESPN report that five Buss siblings had decided to sell the family&\#x27;s remaining stake; last week, Iger and Kushner agreed to buy Mark Walter&\#x27;s majority stake in a deal that valued the team at $12.5 billion.

**Tags**: `#Los Angeles Lakers`, `#sports team ownership`, `#mergers and acquisitions`, `#Bob Iger`, `#Joshua Kushner`

---

<a id="item-finance-news-5"></a>
### [Apple US App Store Commission Revenue Falls 18% as User Spending Declines](https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/) ⭐️ 7.0/10

Apple&\#x27;s US App Store commission revenue fell 18% since early 2026, while US user spending in the second quarter fell 6% year-over-year after 9% growth last year, according to Appfigures and Sensor Tower; Apple said regulatory changes have dragged services growth.

telegram · zaihuapd · Aug 18, 12:17

**「Regulatory pressure on App Store fees」** Regulators in the US and other markets have forced Apple to relax its rules on in-app purchases, which reduces the commission Apple earns from App Store transactions.

**「Impact」** The decline in US App Store commissions and consumer spending pressures Apple&\#x27;s services business, where the App Store is estimated to account for nearly one-third of revenue, and follows June-quarter services revenue of $30.7 billion that missed analysts&\#x27; $31.4 billion expectation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/">Apple&#x27;s US App Store Commission Revenue Down 18% This Year</a></li>
<li><a href="https://9to5mac.com/2026/07/30/apple-says-app-store-regulatory-changes-are-beginning-to-affect-services-growth/">App Store regulatory changes are beginning to affect Apples Services growth - 9to5Mac</a></li>
<li><a href="https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/">Apple&#x27;s US App Store Commission Revenue Down 18% This Year - MacRumors</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Store`, `#regulatory changes`, `#services revenue`, `#consumer spending`

---