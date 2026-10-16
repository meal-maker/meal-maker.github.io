---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 47 items, 12 important content pieces were selected

---

**Technology News**
1. [AdFection: Targeted Ads as Zero-Click Spyware Pipeline](#item-tech-news-1) ⭐️ 8.0/10
2. [Libreboot 26.10 &\#x27;Ominous Olive&\#x27; Released with UEFI and Chromebook Support](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic reports quarterly revenue up nearly 50% to $16.8bn ahead of IPO](#item-tech-news-3) ⭐️ 8.0/10
4. [How Artificial Neural Networks Build Their Own Learning Machinery](#item-tech-news-4) ⭐️ 8.0/10
5. [Meta&\#x27;s Muse Spark Open: 816B-Parameter Open-Weight Model](#item-tech-news-5) ⭐️ 7.0/10
6. [Jev meets the Trolley Problem](#item-tech-news-6) ⭐️ 7.0/10
7. [ASML Is Building a Hybrid Bonding Tool](#item-tech-news-7) ⭐️ 7.0/10
8. [Cook: Apple Intelligence China Beta in Late October, Without Siri AI](#item-tech-news-8) ⭐️ 7.0/10
9. [Google Launches New AI-Powered Android Scam Protections](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [China indicates rare-earth exports to Europe will continue despite U.S. trade deadline](#item-finance-news-1) ⭐️ 8.0/10
2. [China&\#x27;s rural healthcare spending rivals U.S. as a share of income, IMF says](#item-finance-news-2) ⭐️ 7.0/10
3. [China accelerates replacement of Western wind power equipment, citing energy security](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AdFection: Targeted Ads as Zero-Click Spyware Pipeline](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 8.0/10

Citizen Lab researchers have documented a campaign they call AdFection in which targeted advertising was used as a pipeline to deliver zero-click mercenary spyware. The research, covered by The Guardian and The Verge, links an Israeli firm to malicious digital ads that can install spyware without any user interaction. The report highlights severe privacy and security risks in the adtech ecosystem, because ad impressions themselves can be weaponized against specific individuals. While the full technical exploit chain is not detailed in the available source, the findings indicate that ad delivery infrastructure can be abused for surveillance.

hackernews · jcomp · Oct 15, 10:43 · [Discussion](https://news.ycombinator.com/item?id=50101813)

**「Background」** Zero-click spyware installs without any user interaction, unlike malicious links or attachments that require clicks. Targeted advertising uses real-time bidding and device identifiers to serve ads to specific audiences; Citizen Lab’s research shows that the Israeli advertising company Discover-Tech used this infrastructure to deliver Candiru’s spyware to devices, including those at Al Jazeera, marking the first publicly confirmed case of zero-click spyware distributed through ads.

**「Impact」** Users of ad-supported apps and websites face a heightened risk that targeted malicious advertisements could compromise their devices without a click, increasing pressure on ad platforms and intermediaries to vet ad supply chains more rigorously.

**「Community Discussion」** Some commenters challenge the report&\#x27;s severity, with an adtech engineer calling the zero-click mechanism vague and sensationalized, while others argue Israeli cybersecurity firms should be considered state-aligned and untrustworthy; one commenter also points to Israel&\#x27;s Download Valley as a longstanding cybercrime nexus.

<details><summary>References</summary>
<ul>
<li><a href="https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/">Exposing AdFection: How Discover-Tech Turned Targeted Ads ...</a></li>
<li><a href="https://arstechnica.com/security/2026/10/targeted-ads-delivered-0-click-exploits-to-install-mercenary-malware/">Targeted ads delivered 0-click exploits to install mercenary ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#zero-click spyware`, `#targeted advertising`, `#surveillance`, `#adtech`

---

<a id="item-tech-news-2"></a>
### [Libreboot 26.10 &\#x27;Ominous Olive&\#x27; Released with UEFI and Chromebook Support](https://libreboot.org/news/libreboot2610.html) ⭐️ 8.0/10

Libreboot 26.10, codenamed &\#x27;Ominous Olive&\#x27;, introduces UEFI/EDK integration and adds Chromebook support. The release imports all 233 currently supported Chromebooks from the MrChromebox coreboot distribution, greatly expanding the number of compatible devices and simplifying future device ports. The Baytrail \(Kip\) Chromebook has been tested, while other imported Chromebooks still need testing. This Chromebook support is source-only in this release; no binary images are provided, so users must build from source.

hackernews · iamnothere · Oct 15, 12:52 · [Discussion](https://news.ycombinator.com/item?id=50102923)

**「Background」** Libreboot is a free-software coreboot distribution that provides boot firmware, initializing hardware before an operating system loads. Historically it emphasized fully free firmware without Intel&\#x27;s UEFI reference code; this release adds UEFI support using a MrChromebox fork of Intel&\#x27;s EDK2 as the coreboot payload. MrChromebox is an existing coreboot distribution for Chromebooks, and this release imports support for its 233 currently supported devices.

**「Impact」** Users gain a much larger set of supported open-source firmware options, especially for Chromebooks, but they must build from source and should expect many Chromebook ports to be untested.

**「Community Discussion」** Community comments emphasize the hardware expansion as a major step, with one developer linking it to ongoing ChromeOS ports in Heads, while others discuss the project&\#x27;s strict policy on LLM-assisted contributions.

<details><summary>References</summary>
<ul>
<li><a href="https://libreboot.org/news/libreboot2610.html">Libreboot – Libreboot 26.10 “Ominous Olive” released! With ...</a></li>
<li><a href="https://elsolitario.org/en/2026/10/15/libreboot-26-10-adds-full-uefi-and-code-for-233-chromebooks/">Libreboot 26.10: Full UEFI Support and 233 Chromebooks</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#firmware`, `#coreboot`, `#uefi`, `#chromebook`

---

<a id="item-tech-news-3"></a>
### [Anthropic reports quarterly revenue up nearly 50% to $16.8bn ahead of IPO](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

Anthropic told investors that its quarterly revenue rose nearly 50% to $16.8 billion, up from $11.5 billion in Q2 and about $4.8 billion in Q1, ahead of a possible IPO. The company reported an adjusted operating margin of 11% excluding stock-based compensation and said it generated $1.70 in revenue for every $1 spent on computing power in Q3. Anthropic also said it has clamped down on distillation, a practice that accounted for 5% to 7% of revenue but was cut back materially in the third quarter. The company appears to have stopped using annualized run-rate revenue in investor communications.

rss · Simon Willison · Oct 15, 13:04

**「Background」** Anthropic is a major AI lab known for models such as Claude, and it previously communicated revenue using annualized run-rate figures. Distillation is a practice where rival AI labs train their models on the outputs of more advanced models, which can create heavy API usage and spending. The company is reportedly preparing for a possible initial public offering.

**「Impact」** Rival AI labs that distill Anthropic’s models may face reduced access or higher effective costs, and investors gain more direct quarterly revenue metrics ahead of a potential IPO.

**Tags**: `#AI`, `#Anthropic`, `#business`, `#revenue`, `#IPO`

---

<a id="item-tech-news-4"></a>
### [How Artificial Neural Networks Build Their Own Learning Machinery](https://www.reddit.com/r/MachineLearning/comments/1x6hmyg/how_artificial_neural_networks_build_their_own/) ⭐️ 8.0/10

Researchers report in PNAS \(9 October 2026\) that randomly interconnected neuron-like units with shared plasticity rules can self-assemble into learning motifs and perform pattern recognition and image classification at levels similar to backpropagation-trained networks on the tested tasks. The findings, covered by MIT News on 13 October, distinguish designing a learning circuit directly from specifying local rules that allow learning machinery to self-organize. The authors caution that this self-organization does not prove the brain uses the same mechanism, and the work is motivated by biological plausibility rather than as a replacement for backpropagation in large-scale models. Open questions include stability of motifs under different initial connectivity and generalization beyond the demonstrated tasks.

reddit · r/MachineLearning · /u/Dorian182 · Oct 15, 10:01

**「Background」** Backpropagation is the standard algorithm for training artificial neural networks by computing error gradients, but it is often considered biologically implausible due to its non-local weight updates. Biological synapses are governed by local plasticity rules such as Hebbian learning, and this research explores whether such local rules can self-organize into circuits that compute gradients without global design.

**「Impact」** The result offers a biologically plausible route to gradient learning in simple pattern recognition and image classification tasks, though its applicability beyond these benchmarks is not yet established.

**Tags**: `#neural networks`, `#self-organization`, `#synaptic plasticity`, `#backpropagation alternative`, `#machine learning research`

---

<a id="item-tech-news-5"></a>
### [Meta&\#x27;s Muse Spark Open: 816B-Parameter Open-Weight Model](https://research.meta.ai/blog/muse-spark-open) ⭐️ 7.0/10

Meta released Muse Spark Open, an 816-billion-parameter open-weight mixture-of-experts model optimized for local execution and available on Hugging Face as Muse-Spark-Open-816B-A42B. The model offers deployment support across many runtimes, including Unsloth and MLX, reflecting Meta&\#x27;s effort to make it run on essentially every model runner. Its license permits free use but prohibits offering the model as a service via API for licensees whose aggregate gross revenue exceeds 20 million. Community benchmarks from Artificial Analysis show Muse Spark Open underperforming Qwen3.8 Flash Next and GLM 5.3 Flash, both of which can run on a single B300. This makes the release notable for broad availability rather than state-of-the-art capability.

hackernews · bigwheels · Oct 15, 17:47 · [Discussion](https://news.ycombinator.com/item?id=50107379)

**「Background」** Open-weight models make trained parameters publicly downloadable, enabling local or self-hosted inference without paying per-token API fees. Mixture-of-experts architectures route each input token to a subset of parameters, which allows very large total parameter counts with lower inference cost per token. Public leaderboards such as Artificial Analysis are commonly used to compare reasoning quality across different model sizes and reasoning effort levels.

**「Impact」** Developers and organizations below the 20 million gross revenue threshold can freely self-host Muse Spark Open on supported runtimes like MLX and Unsloth, but those needing top-tier high-reasoning performance may prefer Qwen3.8 Flash Next or GLM 5.3 Flash, which run on a single B300.

**「Community Discussion」** Commenters noted the model&\#x27;s broad runtime support and a license clause restricting large API providers, and some expressed disappointment that Artificial Analysis only provides comparisons at the highest reasoning level rather than low- and medium-reasoning tiers. There is also a view that Meta is building a sticky ecosystem around open models now that price, rather than frontier capability, increasingly drives adoption.

**Tags**: `#large language models`, `#open-weight AI`, `#model release`, `#AI inference`, `#Meta AI`

---

<a id="item-tech-news-6"></a>
### [Jev meets the Trolley Problem](https://zachlandes.com/trolley-problem/) ⭐️ 7.0/10

Zach Landes compared how Jev and 13 other AI models respond to variations of the trolley problem, using resampling and multiple question phrasings and orderings to reduce phrasing bias. The analysis systematically evaluates decision-making consistency across 14 models on moral dilemmas, focusing on AI safety and alignment. The methodology includes resampling and randomized variations to ensure no single lucky phrasing dominates results. The article was posted on Hacker News with high engagement, indicating community interest in systematic LLM evaluation for ethical decisions.

hackernews · zlandes86 · Oct 15, 16:24 · [Discussion](https://news.ycombinator.com/item?id=50106023)

**「Background」** The article tests how Jev, a proprietary TypeSafe AI model released in limited early access on 15 September 2026, handles the trolley problem, a classic ethical dilemma about sacrificing one person to save several others. Unlike generative chatbots, Jev is a discriminative “System One” model that returns typed decisions, scores, or yes/no probabilities with confidence estimates intended for direct software consumption, and it supports zero-shot inference from contextual categories provided at inference time. TypeSafe reports that Jev achieves similar intelligence to existing large language models on such System One tasks while being about two orders of magnitude faster and more efficient.

**「Impact」** For AI safety and alignment practitioners, this systematic resampling methodology offers a more robust way to benchmark how LLMs handle moral trade-offs, though the results do not provide definitive safety conclusions.

**「Community Discussion」** Commenters generally appreciated the systematic approach, with one calling it well thought out, while others voiced concerns about AI-driven kafkaesque systems, potential defense applications, and referenced Asimov&\#x27;s laws; no major disagreement about the methodology emerged.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_%28AI_model%29">Jev (AI model)</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#LLM evaluation`, `#ethical AI`, `#decision models`, `#benchmarking`

---

<a id="item-tech-news-7"></a>
### [ASML Is Building a Hybrid Bonding Tool](https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding) ⭐️ 7.0/10

ASML appears to be developing a hybrid bonding tool, according to patent filings, a news report, and its own roadmap, although the company has not made an official announcement. Hybrid bonding is an advanced semiconductor packaging technique that enables dense die-to-die interconnects, which is becoming important for AI and high-performance computing hardware. The report is based on indirect evidence rather than a confirmed product announcement, and no specific technical details or timeline are provided. If confirmed, such a tool would represent a significant expansion of ASML&\#x27;s portfolio beyond lithography into advanced packaging equipment.

rss · Semianalysis · Oct 15, 19:27

**「Background」** Hybrid bonding is an advanced semiconductor packaging technique that directly connects wafers or dies using copper-to-copper and dielectric bonding, enabling much finer interconnect pitches than traditional solder-based approaches. ASML, best known for lithography equipment, appears to be expanding into this area: according to SemiAnalysis, the company filed 27 bonding patent families between 2022 and 2024, and its roadmap indicates development focused on chip-to-wafer applications.

**「Impact」** ASML&\#x27;s apparent move into hybrid bonding, if realized from its patents and roadmap, could place the company in a segment that is becoming a critical enabler for advanced semiconductor packaging and AI/HBM performance.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/asml-is-building-a-hybrid-bonding">ASML Is Building a Hybrid Bonding Tool!ASML is building a ...</a></li>
<li><a href="https://www.chaincatcher.com/en/article/2296696">SemiAnalysis: ASML is currently developing hybrid bonding ...</a></li>
<li><a href="https://www.kucoin.com/news/flash/asml-developing-hybrid-bonding-equipment-focused-on-chip-to-wafer-applications">ASML is developing hybrid bonding equipment, focused ... - KuCoin</a></li>
<li>Report: ASML inches forward with hybrid bonding | Paul van Gerven</li>
<li>ASML&#x27;s XT:260 Redefines Advanced Packaging: Onto Innovation&#x27;s AI ...</li>

</ul>
</details>

**Tags**: `#ASML`, `#hybrid bonding`, `#semiconductor manufacturing`, `#advanced packaging`, `#chipmaking`

---

<a id="item-tech-news-8"></a>
### [Cook: Apple Intelligence China Beta in Late October, Without Siri AI](https://jiemian.com/article/15194723.html) ⭐️ 7.0/10

Apple board executive chairman Tim Cook said in a Shanghai interview on October 15 that Apple Intelligence and Alibaba&\#x27;s Qwen model have been approved for China. Apple plans to release a beta version later in October. The initial features include real-time translation, writing tools, and a photo cleanup tool. Siri AI is not included in this release. The announcement was reported by Jiemian News.

telegram · zaihuapd · Oct 15, 08:59

**「Context」** Apple Intelligence, Apple&\#x27;s suite of AI features, has faced regulatory hurdles in China, where foreign AI models must comply with local rules and partner with approved domestic providers. Reports indicate Apple Intelligence and Alibaba&\#x27;s Qwen large-language model have received Chinese regulatory approval, with a beta expected in late October. This China version is expected to omit Siri AI and route cloud queries to Alibaba, differing from global versions that use ChatGPT and include Siri integrations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.globaltimes.cn/page/202610/1372342.shtml">Apple Intelligence, Alibaba Qwen set for late-October beta ...</a></li>
<li><a href="https://www.techtimes.com/articles/329055/20261014/china-cleared-apple-intelligence-cloud-queries-go-alibaba-under-chinas-spy-law.htm">China Cleared Apple Intelligence, but Cloud Queries Go to ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#machine learning`

---

<a id="item-tech-news-9"></a>
### [Google Launches New AI-Powered Android Scam Protections](https://blog.google/security/new-android-scam-protections/) ⭐️ 7.0/10

Google announced multiple AI-driven Android scam protections. In Google Messages, an enhanced protection mode uses privacy-preserving AI computation with the cloud Gemini model to analyze scam intent in unknown conversations, while on-device Gemini Nano checks unknown link safety in real time. For calls and privacy, the screen-sharing feature that automatically hides password and payment pages has been expanded to Chrome and WebView. The system also adds background interception of call forwarding and warnings for manual input to prevent theft of dynamic verification codes.

telegram · zaihuapd · Oct 15, 12:39

**「Background」** Google has been integrating its Gemini AI models into Android security, with on-device Gemini Nano handling real-time checks and cloud Gemini models enabling deeper analysis. The new Google Messages &\#x27;Enhanced protection mode&\#x27; opts users into cloud-based analysis of conversations with unknown senders to detect scam intent, while expanded safeguards automatically mask sensitive screen content during sharing and alert on suspicious call-forwarding attempts.

**「Impact」** Android users gain automatic detection of suspicious messages and links and stronger screen-sharing and call-forwarding safeguards that can reduce credential and verification-code theft.

<details><summary>References</summary>
<ul>
<li>New Android protections to help keep you safe from mobile scams</li>
<li>Google Rolls Out AI Scam Defenses Across Android Messages and Calls</li>

</ul>
</details>

**Tags**: `#Android`, `#Security`, `#AI`, `#Gemini`, `#Mobile`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China indicates rare-earth exports to Europe will continue despite U.S. trade deadline](https://www.cnbc.com/2026/10/15/china-rare-earth-exports-europe.html) ⭐️ 8.0/10

China&\#x27;s Commerce Ministry spokesperson He Yadong told CNBC on Thursday that China will keep approving rare-earth export licenses to Europe regardless of whether the U.S.-China trade truce is extended past January.

rss · CNBC Finance · Oct 15, 09:02

**「Background」** Beijing tightened rare-earth export rules in October 2025 after a U.S. entity-list expansion, then suspended those measures with Washington; the suspension is set to expire in January. The announcement follows an EU-China meeting last week where China offered a &quot;green channel&quot; mechanism to keep rare-earth flows to Europe.

**Tags**: `#rare earths`, `#China`, `#European Union`, `#trade policy`, `#supply chain`

---

<a id="item-finance-news-2"></a>
### [China&\#x27;s rural healthcare spending rivals U.S. as a share of income, IMF says](https://www.cnbc.com/2026/10/15/chinese-spending-nearly-as-much-of-income-as-americans-on-healthcare.html) ⭐️ 7.0/10

In a new book, the IMF says high healthcare costs are a major reason Chinese households save rather than spend, with rural China spending 8.7% of disposable income on healthcare, second only to the U.S. at 9.9% among 20 major economies.

rss · CNBC Finance · Oct 15, 23:00

**「Background」** Rural China, which only officially emerged from extreme poverty in 2020, had per capita disposable income of 24,456 yuan versus 56,502 yuan in urban areas, while U.S. per capita disposable income was more than 10 times China&\#x27;s.

**「Impact」** The IMF recommends raising government spending on rural health and social security, saying that would significantly reduce rural household savings rates and lift consumption, especially for migrant workers with fewer social benefits than urban residents.

**Tags**: `#China economy`, `#healthcare spending`, `#household savings`, `#IMF`, `#consumer spending`

---

<a id="item-finance-news-3"></a>
### [China accelerates replacement of Western wind power equipment, citing energy security](https://www.bloomberg.com/news/articles/2026-10-15/china-removes-western-wind-power-equipment-to-boost-security?srnd=phx-technology) ⭐️ 7.0/10

China is accelerating replacement of Western wind power equipment, with a Polish Centre for Eastern Studies analysis of over 1,600 public procurement documents finding nearly 300 involved replacing foreign equipment, Bloomberg reports.

telegram · zaihuapd · Oct 15, 14:55

**「Background」** Chinese energy firms have cited high maintenance costs, long spare-part delivery times and possible security risks from foreign technology, and a review by Poland&\#x27;s Centre for Eastern Studies of more than 1,600 public procurement documents found nearly 300 involving replacement of Western wind-power equipment.

**「Impact」** Domestic wind equipment makers may gain new market opportunities while Western suppliers face further shrinkage of their China market share, according to the report.

**Tags**: `#China`, `#wind power`, `#energy security`, `#domestic substitution`, `#industrial policy`

---