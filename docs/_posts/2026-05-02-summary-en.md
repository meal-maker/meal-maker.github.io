---
layout: default
title: "Horizon Summary: 2026-05-02 (EN)"
date: 2026-05-02
lang: en
---

> From 23 items, 6 important content pieces were selected

---

1. [Flock Used Children's Gymnastics Cameras for Sales Demo](#item-1) ⭐️ 8.0/10
2. [TI-84 Evo Upgrades to ARM Cortex CPU](#item-2) ⭐️ 7.0/10
3. [WhatCable: Free macOS App Identifies USB-C Cable Capabilities](#item-3) ⭐️ 7.0/10
4. [Credit Card Brute-Force Attacks: Known but Mitigated](#item-4) ⭐️ 7.0/10
5. [Openclaw v2026.4.29: Active-Run Steering and People-Aware Memory](#item-5) ⭐️ 6.0/10
6. [Can We Learn and Communicate While Dreaming?](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Flock Used Children's Gymnastics Cameras for Sales Demo](https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/) ⭐️ 8.0/10

The city of Dunwoody discovered that Flock Safety accessed live camera feeds from a children's gymnastics room for a sales demonstration, yet still renewed its contract with the company. This incident raises serious privacy and ethical concerns, especially involving children, and highlights the lack of proper oversight and dedicated demo environments in surveillance technology sales. Flock's demo partner program allows selected employees to access live camera feeds from partner cities for product demonstrations, and no separate demo environment was used in this case.

hackernews · joshcsimmons · May 1, 18:37

**Background**: Flock Safety is a major provider of automated license plate recognition (ALPR) and video surveillance systems used by police, businesses, and homeowners associations. The company operates a demo partner program where cities authorize live feed access for demonstrations. Previously, Flock camera feeds were found exposed to the open internet without passwords, raising additional privacy concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/">Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves</a></li>
<li><a href="https://www.theverge.com/news/849624/flock-ai-camera-feeds-exposed-benn-jordan">Dozens of Flock AI camera feeds were just out there | The Verge</a></li>

</ul>
</details>

**Discussion**: Commenters questioned why Flock lacked a dedicated demo environment and criticized the city for renewing the contract despite the privacy breach. Some noted that the presence of cameras in the gymnastics room itself raises concerns, while others highlighted broader issues of mass surveillance without barriers.

**Tags**: `#privacy`, `#surveillance`, `#ethics`, `#security`, `#children's safety`

---

<a id="item-2"></a>
## [TI-84 Evo Upgrades to ARM Cortex CPU](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-evo) ⭐️ 7.0/10

Texas Instruments announced the TI-84 Evo, replacing the classic Z80 processor with an ARM Cortex CPU running at 156 MHz, delivering a 3x performance boost while maintaining full backwards compatibility with existing software. This marks the first major processor change in decades for the iconic graphing calculator series used widely in high school and college math education. The upgrade extends the platform's relevance by offering modern performance without disrupting the ecosystem of existing educational programs and exams. The ARM Cortex CPU runs at 156 MHz, compared to the 48 MHz of previous Z80 and eZ80 models. The TI-84 Evo still requires the same TI-84 Plus software and is expected to be compatible with standard exam restrictions.

hackernews · thatxliner · May 1, 20:06

**Background**: The Zilog Z80 is an 8-bit microprocessor first released in 1976, which powered the TI-83 and TI-84 Plus families for over three decades. The Z80 is being discontinued after nearly 50 years, forcing manufacturers to seek modern alternatives like ARM Cortex, a 32-bit architecture offering higher performance and lower power consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zilog_Z80">Zilog Z80 - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/retrobattlestations/comments/1cb2hs6/the_legendary_zilog_z80_cpu_is_being_discontinued/">The legendary Zilog Z80 CPU is being discontinued after nearly 50 years</a></li>

</ul>
</details>

**Discussion**: Community comments include nostalgic stories about using TI calculators in school or even in prison, as well as critical views questioning the educational value of expensive graphing calculators and suggesting cheaper alternatives like Casio scientific calculators. There is also technical discussion confirming the ARM Cortex upgrade and the end of the Z80 era.

**Tags**: `#graphing calculators`, `#TI-84`, `#ARM Cortex`, `#education`, `#hardware`

---

<a id="item-3"></a>
## [WhatCable: Free macOS App Identifies USB-C Cable Capabilities](https://github.com/darrylmorley/whatcable) ⭐️ 7.0/10

Developer darrylmorley released WhatCable, a free open-source macOS menu bar app that reads the e-marker data in USB-C cables to display their charging wattage, data speed, display support, and Thunderbolt capabilities in plain English. USB-C cables look identical but vary enormously in performance, frustrating users who don't know which cable supports fast charging or high-speed data. WhatCable eliminates guesswork by surfacing technical cable data that macOS already has, making it easier to use the right cable for the right task. Built with Swift and SwiftUI, WhatCable reads the cable's e-marker data via macOS IOKit services and presents it in human-readable format. The developer released 16 versions in 7 hours after community feedback, adding both traditional window mode and a command-line interface.

hackernews · sleepingNomad · May 1, 08:43

**Background**: USB-C cables contain an e-marker chip that stores the cable's capabilities such as maximum power (e.g., 240W) and data speed (e.g., USB4 40Gbps). macOS already queries this chip when a cable is plugged in to negotiate safe power delivery, but the data is hidden from normal users. WhatCable reads that same system data and presents it in plain English, helping users understand why, for example, their Mac might be charging slowly with a particular cable.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/darrylmorley/whatcable">GitHub - darrylmorley/whatcable: macOS menu bar app that ...</a></li>
<li><a href="https://byteiota.com/whatcable-free-macos-usb-c-cable-inspector-for-devs/">WhatCable: Free macOS USB-C Cable Inspector for Devs</a></li>
<li><a href="https://zyrontech.com.au/blogs/news/e-marker-chip-usb-c-cable-guide">E - Marker Chip Explained: The Brain of USB - C Cables</a></li>

</ul>
</details>

**Discussion**: The Hacker News community praised the rapid development pace, with 16 releases in 7 hours incorporating user feedback. Commenters also discussed porting the app to other platforms, with one user successfully creating a KDE Plasma widget using AI in 10 minutes, while others noted ChromeOS's similar built-in USB-C inspection feature and asked about Linux equivalents.

**Tags**: `#USB-C`, `#macOS`, `#open-source`, `#hardware`, `#Swift`

---

<a id="item-4"></a>
## [Credit Card Brute-Force Attacks: Known but Mitigated](https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html) ⭐️ 7.0/10

A blog post claims credit card numbers can be brute-forced, but the community notes that payment processors already employ anti-enumeration measures and the analysis overlooks the critical distinction between authorization and settlement. While card enumeration is a real security concern, the post overstates the risk by ignoring existing mitigations; understanding these nuances helps consumers and developers avoid unnecessary panic and implement proper defenses. Payment processors like Stripe actively detect and block card testing, and card schemes such as Visa penalize merchants that fail to prevent enumeration. Additionally, a successful authorization does not guarantee settlement, meaning fraudulent charges can still be reversed.

hackernews · kodbraker · May 1, 20:26

**Background**: Brute-force attacks on credit cards, also known as card enumeration or card cracking, involve trying many combinations of card numbers, expiration dates, and CVV to find valid ones. Payment networks have implemented anti-enumeration best practices and rate limiting to detect and block such attacks. Authorization is the initial check that funds are available, while settlement is the actual transfer of money; a charge can be authorized but never settled if flagged as suspicious.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spreedly.com/blog/payment-authorization-vs-settlement">Payment Authorization vs . Settlement</a></li>
<li><a href="https://usa.visa.com/dam/VCOM/global/support-legal/documents/anti-enumeration-and-account-testing-best-practices-merchant.pdf">[PDF] Anti-Enumeration and Account Testing Best Practices for Merchants - Visa</a></li>
<li><a href="https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-010_Card_Cracking">OAT-010 Card Cracking | OWASP Foundation</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the post fails to mention settlement vs authorization (tialaramex), that payment processors already block enumeration (janpeuker), and that users can freeze cards when not in use (8cvor6j844qw_d6). Another commenter shared a personal story of fraudulent charges persisting even after getting a new card, indicating the attack may not be purely enumeration (julienchastang).

**Tags**: `#security`, `#credit cards`, `#brute force`, `#payment systems`, `#hacker news`

---

<a id="item-5"></a>
## [Openclaw v2026.4.29: Active-Run Steering and People-Aware Memory](https://github.com/openclaw/openclaw/releases/tag/v2026.4.29) ⭐️ 6.0/10

Openclaw v2026.4.29 introduces active-run steering by default for messaging and automation, a people-aware memory wiki with provenance views, expanded provider/model support including NVIDIA and Bedrock Opus 4.7, and reliability fixes for gateways and plugins. This release enhances AI agent orchestration by making runtime behavior more dynamic and context-aware, which improves reliability and user trust in automated workflows. The expanded provider support also lowers integration barriers for teams using diverse AI models. The memory system now includes per-conversation Active Memory filters, partial recall on timeout, and bounded REM preview diagnostics, while the steering queue defaults to draining all pending messages at the next model boundary with a 500ms fallback debounce. Notable fixes include Slack Block Kit limits, Telegram resilience, and startup warnings for restricted profiles that require explicit 'alsoAllow' entries.

github · steipete · Apr 30, 21:01

**Background**: Openclaw is an open-source AI agent framework that enables developers to build and orchestrate autonomous agents for messaging, automation, and complex workflows. It provides features like memory management, tool execution, and multi-channel support for platforms such as Slack, Discord, and Telegram. The 'active-run steering' concept allows agents to adjust their execution paths during runtime based on real-time feedback, while 'people-aware memory' adds metadata about human users to improve contextual recall and privacy handling.

<details><summary>References</summary>
<ul>
<li><a href="https://www.clawbot.blog/blog/openclaw-v2026429-released-active-run-steering-and-visible-reply-enforcement-for/">OpenClaw v2026.4.29 Released: Active - Run Steering ... — clawbot.blog</a></li>
<li><a href="https://docs.openclaw.ai/concepts/queue-steering">Steering queue - OpenClaw</a></li>

</ul>
</details>

**Tags**: `#openclaw`, `#release`, `#automation`, `#memory`, `#AI`

---

<a id="item-6"></a>
## [Can We Learn and Communicate While Dreaming?](https://www.newyorker.com/culture/annals-of-inquiry/its-possible-to-learn-in-our-sleep-should-we) ⭐️ 6.0/10

A New Yorker article reports on new research suggesting that people can learn new skills and even communicate with others while dreaming, challenging traditional views of sleep as a period of complete mental disconnection. If validated, this research could transform how we approach learning and problem-solving, offering a way to utilize sleep for productive cognitive work. It also raises ethical and practical questions about the boundaries of consciousness during sleep. The article highlights anecdotal evidence from software engineers and mathematicians who report solving complex problems or discovering bugs in dreams. However, the scientific evidence for two-way communication during sleep remains limited and controversial.

hackernews · XzetaU8 · May 1, 17:47

**Background**: Sleep, particularly REM sleep, is known to play a critical role in memory consolidation and creative problem-solving. Lucid dreaming, where the dreamer is aware of dreaming, has been studied for potential skill practice. This new research extends these ideas by exploring real-time communication with dreaming individuals.

**Discussion**: Commenters shared personal experiences of solving programming bugs and mathematical problems during dreams, with several noting that the insights were accurate and immediately applicable. There was curiosity and skepticism about the claim of communication, with one user questioning how two sleeping people could interact.

**Tags**: `#sleep`, `#learning`, `#cognition`, `#problem-solving`, `#neuroscience`

---