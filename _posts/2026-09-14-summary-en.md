---
layout: default
title: "Horizon Summary: 2026-09-14 (EN)"
date: 2026-09-14
lang: en
---

> From 39 items, 12 important content pieces were selected

---

**Technology News**
1. [Homebrew 7.0.0 Brings Official macOS GUI, Drops macOS 10.15](#item-tech-news-1) ⭐️ 9.0/10
2. [Cars Collect and Sell Driver Data as California Moves to Ban It](#item-tech-news-2) ⭐️ 8.0/10
3. [Why 4-hi HBM Stacks Reduce AI Inference Costs](#item-tech-news-3) ⭐️ 8.0/10
4. [Fable 5.1 Solves 370-Year-Old Cyphral Distich Cipher](#item-tech-news-4) ⭐️ 7.0/10
5. [Why Google Still Serves Scam Ads](#item-tech-news-5) ⭐️ 7.0/10
6. [Paul Graham: Startup Power Through Generosity and Full-Stack Strategy](#item-tech-news-6) ⭐️ 7.0/10
7. [Garry Tan wants US open-weight AI labs to &\#x27;distill&\#x27; frontier models, too](#item-tech-news-7) ⭐️ 7.0/10
8. [CUDA Moat: AMD DeepSeek v4.1 Flash Lags Up to 42x per Dollar](#item-tech-news-8) ⭐️ 7.0/10
9. [GitHub Incident Affected Issues, Pages, and Pull Requests](#item-tech-news-9) ⭐️ 7.0/10
10. [Kirin 9050 Pro Review: 3D Stacking Boosts Performance and Efficiency](#item-tech-news-10) ⭐️ 7.0/10
11. [Unconfirmed leak claims iOS 27 enables third-party Siri models](#item-tech-news-11) ⭐️ 7.0/10
12. [Trump Rejects Tech Executives&\#x27; Call to Slow AI Development](#item-tech-news-12) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Homebrew 7.0.0 Brings Official macOS GUI, Drops macOS 10.15](https://brew.sh/2026/09/13/homebrew-7.0.0/) ⭐️ 9.0/10

Homebrew 7.0.0 was released on September 13, 2026, introducing an official native macOS graphical user interface. The release focuses on faster installation and upgrade speeds, stricter sandboxing, and built-in vulnerability checks backed by a security advisory database. Support for macOS 10.15 and earlier has ended, and Intel Macs are moved to Tier 3, so no new precompiled packages are provided for them. On Linux, the sandbox implementation changed from Bubblewrap to Landlock.

telegram · zaihuapd · Sep 13, 11:23

**「Context」** Homebrew is a widely used open-source package manager for macOS and Linux. The previous major version, Homebrew 6.0.0, introduced Bubblewrap sandboxing; Homebrew 7.0.0 replaces this with Landlock, which requires no extra dependencies or elevated Docker permissions that had caused setup problems with Bubblewrap. This release also shifts Intel Macs to a lower support tier with no new precompiled packages and drops support for macOS 10.15 and earlier.

**「Impact」** Users on macOS 10.15 or earlier and Intel Mac users will no longer receive new precompiled packages from Homebrew 7.0.0, so they must build from source or remain on an older Homebrew version.

<details><summary>References</summary>
<ul>
<li><a href="https://brew.sh/2026/09/13/homebrew-7.0.0/">Homebrew: 7.0.0</a></li>
<li><a href="https://daily.dev/posts/homebrew-7-0-0-cj7h7kzxv">Homebrew 7.0.0 | daily.dev</a></li>
<li><a href="https://brew.sh/2026/09/13/homebrew-7.0.0/">Homebrew : 7 . 0 . 0</a></li>

</ul>
</details>

**Tags**: `#homebrew`, `#macos`, `#package-manager`, `#developer-tools`, `#security`

---

<a id="item-tech-news-2"></a>
### [Cars Collect and Sell Driver Data as California Moves to Ban It](https://www.theverge.com/column/994172/your-car-is-selling-your-data) ⭐️ 8.0/10

Modern connected cars collect detailed driver telemetry such as speed, location, and timestamps, and automakers can sell that data to third parties. Community reports specifically cite GM selling speed, location, and timestamp data, while a driver found a Carfax request for current mileage despite disabling collection in a Volkswagen. California&\#x27;s AB-1542, likely to be signed this week, would make the sale or sharing of sensitive personal information illegal, including geolocation data that can locate an individual within 1,850 feet. Commenters distinguish between persistent facts about a car \(VIN, recall status, odometer\) and facts about the driver \(speed, location, timestamp\), arguing the latter should be banned rather than merely anonymized. The proposed DRIVER Act treats both types as the same, which critics say fails to fix the core problem.

hackernews · bookofjoe · Sep 13, 13:45 · [Discussion](https://news.ycombinator.com/item?id=49683953)

**「Background」** Connected vehicles typically include telematics systems that transmit location, driving behavior, and vehicle status to manufacturers or partners, creating a data trail. California&\#x27;s privacy framework treats precise geolocation as sensitive personal information, and AB-1542 specifically restricts the sale and sharing of such data. This explains why automakers&\#x27; data practices are drawing regulatory attention.

**「Impact」** If signed, AB-1542 would make it illegal in California to sell or share geolocation data able to locate an individual within 1,850 feet, directly targeting automakers&\#x27; sale of driver telemetry such as speed and location.

**「Community Discussion」** Commenters disagree on whether the DRIVER Act adequately addresses the issue; several argue it incorrectly lumps car facts with driver telemetry and fails to ban collection of sensitive driver data. Others propose technical countermeasures such as Faraday cages and point to the lack of meaningful data protection laws as the root cause.

**Tags**: `#car data`, `#privacy`, `#telemetry`, `#data regulation`, `#connected vehicles`

---

<a id="item-tech-news-3"></a>
### [Why 4-hi HBM Stacks Reduce AI Inference Costs](https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi) ⭐️ 8.0/10

SemiAnalysis explains that 4-hi HBM stacks can provide the same memory bandwidth as taller HBM stacks while using fewer DRAM dies. Fewer dies per stack reduce DRAM usage and inference costs for bandwidth-constrained AI accelerators. The article, authored by Myron Xie, argues that this lower stack height does not sacrifice bandwidth but makes scarce DRAM go further. The result is a more cost-efficient memory configuration for AI inference systems that need high bandwidth.

rss · Semianalysis · Sep 13, 18:19

**「Background」** High Bandwidth Memory \(HBM\) stacks multiple DRAM dies vertically and connects them through a base logic die; a 4-hi stack uses four DRAM dies and provides eight 128-bit channels, for a total bus width of 1024 bits per stack. In AI inference workloads, token throughput is often limited by memory bandwidth rather than compute, so reducing stack height from taller configurations such as 8-hi or 12-hi to 4-hi can preserve the same interface bandwidth while using fewer DRAM dies and lowering cost per bit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi">Long Live the Short King: Why 4 - hi HBM Wins</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#AI inference`, `#memory bandwidth`, `#semiconductor hardware`, `#cost optimization`

---

<a id="item-tech-news-4"></a>
### [Fable 5.1 Solves 370-Year-Old Cyphral Distich Cipher](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 7.0/10

According to a Vals.ai blog post, Fable 5.1 reportedly solved the Cyphral Distich, a cipher that had remained unsolved for about 370 years. The result is presented as a demonstration of AI-assisted codebreaking, but the available item does not include the source text, the cipher&\#x27;s details, the method used, or independent verification. Because the report originates from the model&\#x27;s vendor and only the title and brief analysis are available, the claim should be considered provisional. The significance is concrete but narrow, affecting historical cryptography rather than broad AI benchmarks.

hackernews · u1hcw9nx · Sep 13, 21:06 · [Discussion](https://news.ycombinator.com/item?id=49688695)

**「Background」** The Cyphral Distich is a short enciphered text printed by Sir Thomas Urquhart in his 1653 work Logopandecteision. It remained unsolved for roughly 370 years and is included in Klaus Schmeh&\#x27;s list of the fifty most famous unsolved ciphers. The ciphertext consists of a sequence of dot-separated numbers such as 1.2.12.1.20.20.49.20.20.35.33.4.6.8.35.5.33.5.5.18.10.3.11.32.42, and no authoritative plaintext was publicly known before this evaluation.

**「Impact」** For historical cryptographers and codebreaking enthusiasts, a verified solution would close a long-standing puzzle and add an example of LLM-assisted analysis; it does not indicate a threat to modern encryption.

**「Community Discussion」** Commenters shared examples such as ChatGPT cracking a handwritten childhood cipher and speculation that Fable 5.1 may fall back to Opus 5 for this type of problem. Several emphasized that the result may be due to low prior attention rather than a fundamental advance in AI codebreaking.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://itdoeswhatnow.com/m/2026-08-31-claude-fable-5-1-solves-a-370-year-old-cipher/">Claude Fable 5.1 solves a 370-year-old cipher in a Vals AI test • It Does What Now?</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cryptography`, `#historical-cipher`, `#codebreaking`, `#machine-learning`

---

<a id="item-tech-news-5"></a>
### [Why Google Still Serves Scam Ads](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 7.0/10

An article from Atomic14 examines why Google continues to serve scam advertisements, citing platform moderation failures and revenue incentives as core causes. Community reports describe AdSense placing thousands of scam pop-ups on publisher sites, often hosted on rotating subdomains under azurestaticapps.net, azurewebsites.net, herokuapp.com, ondigitalocean.app, digitaloceanspaces.com, and netlify.app, and note that Google will not allow publishers to block these domains because it treats them as TLDs. A marketer who has spent more than $100 million on Google Ads says the company is aggressively maximizing ad revenue in unprecedented ways, possibly to mask AI losses or extract value before AI disrupts ad revenue. Users also report seeing repeated AI-generated scam ads on YouTube for products such as free electricity, anti-aging goods, and hand-carved birdhouses, reinforcing the view that Google&\#x27;s advertising standards have declined.

hackernews · iamflimflam1 · Sep 13, 17:37 · [Discussion](https://news.ycombinator.com/item?id=49686445)

**「Background」** Google Ads policy strictly prohibits advertisements that imitate operating system dialogs, system warnings, or error messages \(tool-1-1\). Scammers often evade ad review processes through cloaking and rotating subdomains on legitimate top-level domains such as azurestaticapps.net and netlify.app, which Google treats as domains that cannot be blocked \(tool-1-2\). In some reported cases, Google’s manual review rejects user complaints about such ads even when automated analysis by tools like Gemini identifies multiple deceptive elements \(tool-1-3\).

**「Impact」** Despite Google reporting removal of over 602 million scam-related ads and suspension of 4 million accounts in 2025, AdSense publishers and YouTube users continue to encounter recurring AI-generated scam ads and cannot block scammer subdomains, eroding trust in the platform&\#x27;s ad moderation.

**「Community Discussion」** Commenters broadly agree that Google&\#x27;s ad moderation is inadequate, with multiple reports of recurring AI-generated scam ads on YouTube and scam pop-ups on AdSense publisher sites. Some attribute the problem to revenue maximization or an overwhelmed review system, while one commenter argues that Google should face strict liability for serving such ads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads">Why is Google still serving dodgy ads ? | atomic 14</a></li>
<li><a href="https://sesamedisk.com/problems-with-google-ads/">Why Are Google Ads Still Serving Dodgy Ads ? - Sesame Disk</a></li>
<li><a href="https://dzen.ru/b/aqbya-6lSHKwoSKj">Google отклонила жалобы на рекламу, которую забраковала... | Дзен</a></li>
<li><a href="https://blog.google/products/ads-commerce/google-ads-safety-report-2023/">Our 2023 Ads Safety Report - The Keyword ads_safety_report_2024 - services.google.com Google’s 2025 Ads Safety Report - The Keyword 2023 Ads Safety Report - Google Search Why advertisers can no longer trust Google - LinkedIn Google Ads Safety Report 2025: 8.3B Ads Removed - almcorp.com</a></li>

</ul>
</details>

**Tags**: `#google`, `#online-advertising`, `#trust-safety`, `#tech-industry`, `#scam-ads`

---

<a id="item-tech-news-6"></a>
### [Paul Graham: Startup Power Through Generosity and Full-Stack Strategy](https://paulgraham.com/powerful.html) ⭐️ 7.0/10

Paul Graham&\#x27;s essay argues that startups become powerful by creating more value than they capture, adopting a full-stack approach, and noticing when users unexpectedly misuse products. He advises founders to be generous rather than squeeze every penny, because giving users surplus value creates lasting wealth and influence. Going full-stack means taking on more of the customer&\#x27;s hardest work rather than staying a narrow component, which can strengthen the company&\#x27;s position. The essay also treats unexpected user behavior as a strong signal of unmet demand worth pursuing. Aimed at startup founders, the advice has generated substantial discussion on Hacker News.

hackernews · tosh · Sep 13, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49684196)

**「Background」** Paul Graham is a co-founder of Y Combinator and a well-known essayist on startups and technology. His widely shared startup advice includes making something users want, releasing early, and avoiding distractions. &\#x27;Making Startups Powerful&\#x27; sits within that ongoing series of essays and focuses on how startups can accumulate power by creating more value than they capture, integrating vertically, and responding to unexpected user behavior.

**「Community Discussion」** Commenters largely endorse the essay&\#x27;s advice, with one noting that founders who remember needing to delight users are more likely to be generous than hired CEOs. Another adds a full-stack example where a banking software provider could expand into banking itself, while a final comment highlights real-world inconsistency between generosity rhetoric and practices like high cleaning fees.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gavrilobozovic.com/thoughts/paul-graham">Paul Graham&#x27;s greatest advice for startuppers — Gavrilo Bozovic</a></li>
<li><a href="https://www.jaakkoj.com/blog/graham">Paul Graham 101</a></li>
<li><a href="https://medium.com/swlh/graham-for-the-lazy-51a170dacc86">Paul Graham’s Startup Advice for the Lazy | by Stelios Constantinides | The Startup | Medium</a></li>

</ul>
</details>

**Tags**: `#startups`, `#business strategy`, `#paul graham`, `#technology industry`, `#entrepreneurship`

---

<a id="item-tech-news-7"></a>
### [Garry Tan wants US open-weight AI labs to &\#x27;distill&\#x27; frontier models, too](https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/) ⭐️ 7.0/10

Garry Tan, president of Y Combinator, argues that US open-weight AI labs should be allowed to distill frontier models, citing the fact that proprietary AI labs trained their models on vast amounts of publicly available and copyrighted data without permission. He frames a single proprietary provider controlling frontier AI as the larger nightmare scenario, while open-weight distillation offers a counterweight by spreading advanced capabilities. The position challenges licensing restrictions imposed by companies like Anthropic, which Tan and commenters say lack moral high ground after strip-mining the commons. The debate reflects broader tensions over AI training data, copyright, and competition as open-weight models increasingly approach frontier quality.

hackernews · TheJCDenton · Sep 13, 15:44 · [Discussion](https://news.ycombinator.com/item?id=49685253)

**「Background」** Model distillation is a technique in which a smaller model is trained on the outputs of a larger, more capable model to approximate its behavior at lower cost. Frontier AI labs such as OpenAI and Anthropic build proprietary models using massive datasets, while open-weight labs release trained model weights for others to use and modify. Garry Tan, CEO of Y Combinator, has argued that smaller American open-weight labs should be allowed to distill American frontier models—describing a possible &\#x27;American distillation regime&\#x27;—so the US has open-weight options that are not Chinese.

**「Community Discussion」** Commenters largely endorse Tan&\#x27;s view, arguing that frontier labs cannot claim ethical ownership after training on scraped copyrighted works; several note that open-weight models are already nearly as capable as frontier models and predict that legal barriers to distillation will become unsustainable. Some specifically call out Anthropic&\#x27;s attempt to make distillation orderly but not illegal as contradictory.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/">Y Combinator&#x27;s Garry Tan wants US open-weight AI labs to &#x27;distill&#x27; frontier models, too | TechCrunch</a></li>
<li><a href="https://github.com/hanzhad/squelch-news-engine/issues/831">Y Combinator’s Garry Tan wants US open-weight AI labs to ‘distill’ frontier models, too · Issue #831 · hanzhad/squelch-news-engine</a></li>

</ul>
</details>

**Tags**: `#AI`, `#model distillation`, `#open source`, `#policy`, `#copyright`

---

<a id="item-tech-news-8"></a>
### [CUDA Moat: AMD DeepSeek v4.1 Flash Lags Up to 42x per Dollar](https://x.com/SemiAnalysis_/status/2098618867035557984) ⭐️ 7.0/10

AMD released its DeepSeek v4.1 Flash image two days after CUDA vLLM gained support for the model. While the AMD image is ready to use out of the box, its per-dollar performance is up to 14.8 times worse than NVIDIA H200 and up to 42 times worse than NVIDIA B200/B300. SemiAnalysis attributes the gap to NVIDIA&\#x27;s CUDA ecosystem of about 6 million developers, which allowed day-one optimization. This highlights CUDA&\#x27;s competitive moat in AI infrastructure.

telegram · zaihuapd · Sep 13, 05:55

**「Background」** CUDA is NVIDIA&\#x27;s proprietary parallel computing platform and API that has become the default for GPU-accelerated AI workloads; its &\#x27;moat&\#x27; refers to the large ecosystem of libraries, tools, and developers that allows new models to be optimized on NVIDIA hardware almost immediately. DeepSeek v4.1 Flash is a recent large language model, and per-dollar performance measures tokens per second per unit cost across different accelerators. SemiAnalysis has chronicled this dynamic in its DeepSeekV4 reports, noting that CUDA distributed inference is supported near day one while alternatives lag \(tool-1-1\).

**「Consequence for AMD deployments」** For organizations deploying DeepSeek v4.1 Flash on AMD GPUs, the reported per-dollar performance gap—up to 42x versus Nvidia B200/B300 and up to 14.8x versus H200—makes the platform economically impractical for this workload without significant cost reductions or kernel optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/deepseekv4-16t-day-0-to-day-43-performance">DeepSeekV4 1.6T Day 0 to Day 43 Performance Over Time - GB300 NVL72, Huawei, MI355X, B200</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#AMD`, `#DeepSeek`, `#AI hardware`, `#performance`

---

<a id="item-tech-news-9"></a>
### [GitHub Incident Affected Issues, Pages, and Pull Requests](https://www.githubstatus.com/incidents/0rn90wk115q9) ⭐️ 7.0/10

GitHub experienced an incident affecting Issues, Pages, and Pull Requests. The official status page attributed the problem to a database replication delay in the collaboration platform, which caused an increase in system error rates. To mitigate the issue, GitHub applied internal rate limiting to reduce cluster load, but Pull Requests still exhibited degraded performance at 18:28. The incident was reported resolved at 18:44.

telegram · zaihuapd · Sep 13, 09:20

**「Background」** GitHub is a major code hosting and collaboration platform used by developers worldwide. Its status page publishes official updates during service incidents. Database replication delay can lead to stale or inconsistent data across services, increasing error rates.

**「Impact」** Users of GitHub Issues, Pages, and Pull Requests encountered elevated error rates and degraded performance during the incident, though the official update states the issue is now resolved.

**Tags**: `#github`, `#outage`, `#incident report`, `#developer tools`, `#platform status`

---

<a id="item-tech-news-10"></a>
### [Kirin 9050 Pro Review: 3D Stacking Boosts Performance and Efficiency](https://www.bilibili.com/video/BV1HEYv6XETo) ⭐️ 7.0/10

A Geekerwan review reports that Huawei&\#x27;s Kirin 9050 Pro mobile SoC uses microcircuit 3D stacking to improve performance and power efficiency. Its 9-core, 16-thread CPU cuts power consumption by more than 30% at the same 2.75 GHz frequency compared with the previous generation, while the 3.1 GHz peak frequency does not significantly increase power draw. The Maliang 955 GPU scores nearly 40% higher in 3DMark than its predecessor, and the NPU delivers 67.7 TOPS of measured INT8 performance. In three demanding mobile games, the Mate XT 2&\#x27;s overall performance reportedly reaches the level of Snapdragon 8 Elite.

telegram · zaihuapd · Sep 13, 13:22

**「Background」** The Kirin 9050 Pro is a Huawei/HiSilicon mobile system-on-chip introduced in the Mate XT 2 and reported to use a 3D stacking technology called LogicFolding, along with HarmonyOS 7. It is primarily available in Huawei&\#x27;s China-centric device ecosystem, which limits direct global comparisons with Qualcomm Snapdragon chips. The Geekerwan review measures CPU, GPU, and NPU performance and efficiency within this hardware and software context.

**「Impact」** For Mate XT 2 buyers, the Kirin 9050 Pro provides Snapdragon 8 Elite-class gaming performance with significantly lower CPU power consumption, improving battery life in sustained loads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ixbt.com/news/2026/09/12/435253-noveisii-kirin-9050-pro-2-tb-pamiati-ocen-iarkii-ekran-6500-nit-privacy-display-i-novaia-konstrukciia-huawei-mate-xt-2-postupil-v-prodazu-v-kitae.html">Новейший Kirin 9050 Pro , 2 ТБ памяти, очень яркий экран 6500 нит...</a></li>

</ul>
</details>

**Tags**: `#Kirin 9050 Pro`, `#3D stacking`, `#mobile SoC`, `#NPU`, `#hardware review`

---

<a id="item-tech-news-11"></a>
### [Unconfirmed leak claims iOS 27 enables third-party Siri models](https://x.com/itspdfu/status/2099122424209916015) ⭐️ 7.0/10

An unverified leak claims that iOS 27 and macOS Golden Gate include private Model Delegation APIs that would let apps add third-party models such as Claude to Siri through App Intents. The feature would allow Claude to appear in Siri&\#x27;s Ask menu and generate a CSV, while handing off system actions such as setting reminders back to Siri for execution. Access would require the private com.apple.developer.model-delegation entitlement. The leak describes using a third-party model to replace Siri&\#x27;s AI service backend, but Apple has not confirmed the capability.

telegram · zaihuapd · Sep 13, 13:48

**「Background」** Apple&\#x27;s Siri currently relies on Apple-controlled models, while third-party apps can only extend Siri through limited App Intents or SiriKit domains. The leak describes private Model Delegation APIs in iOS 27 and macOS Golden Gate \(macOS 27\) that would let an app provide a general-purpose model such as Claude as the Siri backend, with system actions handed back to Siri; a MacRumors forum thread corroborates the existence of the private com.apple.developer.model-delegation entitlement in macOS 27.

**「Impact」** If accurate, these private APIs would let developers integrate third-party AI models into Siri workflows and offload supported tasks, but the leak is unofficial and the entitlement is not publicly available.

<details><summary>References</summary>
<ul>
<li><a href="https://forums.macrumors.com/threads/apples-rumored-siri-extensions-quietly-shipped-in-macos-27-i-got-ask-claude-working.2486206/">Apple ’s rumored Siri Extensions quietly shipped in macOS 27 . I got...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#iOS`, `#macOS`, `#third-party AI`, `#API leak`

---

<a id="item-tech-news-12"></a>
### [Trump Rejects Tech Executives&\#x27; Call to Slow AI Development](https://www.ft.com/content/cae60732-f929-4735-a627-db8c14e7c7ed?syn-25a6b1a6=1) ⭐️ 7.0/10

US President Donald Trump rejected calls from technology executives to slow development of artificial intelligence and opposed tightening regulation based on safety risks. He said the concerns were influenced by “very negative forces” and stressed that the United States cannot fall behind China in the AI race. The position came as tech industry figures and Democrats pushed for stricter rules. The stance signals continued prioritization of rapid AI advancement over safety-focused regulatory measures.

telegram · zaihuapd · Sep 14, 00:07

**「Background」** Recent calls from AI executives including Anthropic’s Dario Amodei, OpenAI’s Sam Altman, and Elon Musk urged slowing AI model development over safety concerns, with Democrats using the administration&\#x27;s resistance to such regulation as a political attack. The Trump administration and Republican lawmakers have argued that AI companies can voluntarily moderate their own pace without sweeping new rules, while framing the issue as a race against China for global AI supremacy.

**「Impact」** The statement signals that federal AI policy under Trump will prioritize competition with China over safety restrictions, reducing the likelihood of imminent US safety-based regulation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.washingtonpost.com/politics/2026/09/13/trump-rejects-calls-so-slow-ai-development-citing-chinese-competition/">Trump rejects calls to slow AI development, citing Chinese competition - The Washington Post</a></li>
<li><a href="https://www.timesnownews.com/world/us/us-news/whoever-wins-ai-wins-trump-rejects-tech-bosses-call-for-an-ai-slow-down-article-156152473">&#x27;Whoever Wins AI, Wins&#x27;: Trump Rejects Tech Bosses&#x27; Call for an AI Slow Down | Times Now</a></li>
<li><a href="https://world-today-journal.com/trump-rejects-calls-to-slow-ai-development-citing-race-against-china/">Trump Rejects Calls to Slow AI Development, Citing Race Against China - World Today Journal</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#US politics`, `#AI safety`, `#technology regulation`, `#US-China competition`

---