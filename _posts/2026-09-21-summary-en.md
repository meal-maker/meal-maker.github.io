---
layout: default
title: "Horizon Summary: 2026-09-21 (EN)"
date: 2026-09-21
lang: en
---

> From 30 items, 10 important content pieces were selected

---

**Technology News**
1. [ChatGPT now tracks users across other websites via ad collector](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen Image 2.1: Open-Weight 7B Image Gen with Transparency](#item-tech-news-2) ⭐️ 8.0/10
3. [Pirate Face: BitTorrent and Runtime Refusal Vectors for LLMs](#item-tech-news-3) ⭐️ 8.0/10
4. [AI-Hallucinated Intelligence Nearly Led US Troops to Board Chinese Ship](#item-tech-news-4) ⭐️ 8.0/10
5. [ChangXin Technology Mass-Produces Fifth-Generation DRAM Platform](#item-tech-news-5) ⭐️ 8.0/10
6. [Samsung Expected to More Than Double HBM4/HBM4E DRAM Output Next Year](#item-tech-news-6) ⭐️ 7.0/10
7. [Why Decontamination Reports Can&\#x27;t Fix Benchmark Contamination](#item-tech-news-7) ⭐️ 7.0/10
8. [LG TVs Record Audio When Off, Highlight Smart TV ACR Tracking](#item-tech-news-8) ⭐️ 7.0/10
9. [Hunan Police Chiefs Removed Over Alleged Extortion of VPN Software Founder](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [American companies squeezed by tariffs, fuel costs and rising rates](#item-finance-news-1) ⭐️ 9.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ChatGPT now tracks users across other websites via ad collector](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) ⭐️ 8.0/10

ChatGPT has started using standard ad collector mechanisms to track user activity across other websites, combining adtech cross-site tracking with an AI chat product. This development is unprecedented because such tracking has not previously been applied to AI chat products. The tracking mechanism is standard adtech, but its use in ChatGPT raises new privacy concerns for users of AI chat services. The change means that ChatGPT may have access to browsing activity outside its own interface, linking that data to user accounts.

hackernews · lmbbuchodi · Sep 20, 15:18 · [Discussion](https://news.ycombinator.com/item?id=49776729)

**「Background」** Ad-tech cross-site tracking often uses cookies set by a domain&\#x27;s subdomain to identify users across unrelated websites. In this case, OpenAI&\#x27;s bzr.openai.com sets a cookie named \_\_obi scoped to .openai.com, and while on ChatGPT it is tied to the ChatGPT account. This cookie is then sent to OpenAI from ordinary websites, letting the chat product associate off-site browsing with a logged-in user.

**「Impact」** Users who want to avoid this cross-site tracking should use Firefox, Brave, or Safari, as Chrome and Edge do not currently prevent it.

**「Community Discussion」** Commenters expressed discomfort over cross-site tracking, with one noting they left Facebook for similar reasons; others welcomed EU legislative efforts and noted that Firefox, Brave, and Safari block the tracking while Chrome and Edge do not. One commenter also criticized the article as AI-generated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/">ChatGPT now knows what you do on other websites via ad collector</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#AI`, `#adtech`, `#web tracking`, `#ChatGPT`

---

<a id="item-tech-news-2"></a>
### [Qwen Image 2.1: Open-Weight 7B Image Gen with Transparency](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen Image 2.1 is a new open-weight 7-billion-parameter image generation model from Qwen that features improved text rendering and native transparency support. It is significantly smaller than the previous Qwen-Image model, which had 20 billion parameters, making it one of the smaller open-weight text-to-image models available. Community evaluations highlight that its text rendering is much better than other open-weight models and compares favorably with gpt-image-2 in small-text fidelity. However, the model uses a more restrictive license than earlier Qwen models that were mostly Apache-licensed.

hackernews · jmillikin · Sep 20, 13:09 · [Discussion](https://news.ycombinator.com/item?id=49775499)

**「Context」** Qwen Image 2.1 is a multimodal image generation and editing model from Alibaba&\#x27;s Qwen team, serving as a successor to the earlier Qwen-Image model with 20 billion parameters. The new 7-billion-parameter model improves text rendering and adds native transparency support, and it is distributed via Hugging Face with instructions for libraries, notebooks, and local applications such as ComfyUI.

**「Impact」** Developers who need high-fidelity text rendering in locally run image generation may benefit from Qwen Image 2.1, but its restrictive license could limit commercial adoption.

**「Community Discussion」** Commenters praised the model&\#x27;s small 7B parameter size, native transparency support, and major improvement in text rendering compared with other open-weight models; however, they raised concerns about the more restrictive license, with one user sharing tests that showed better text fidelity versus gpt-image-2.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-qwen-image-2-1">What Is Qwen - Image - 2 . 1 ? Native 2K Editing</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen / Qwen - Image - 2 . 1 · Hugging Face</a></li>
<li><a href="https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight">Qwen - Image - 2 . 1 in ComfyUI: Open-Weight Image Generation and...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#image generation`, `#open source`, `#Qwen`, `#text-to-image`

---

<a id="item-tech-news-3"></a>
### [Pirate Face: BitTorrent and Runtime Refusal Vectors for LLMs](https://pirateface.co/) ⭐️ 8.0/10

The Hacker News discussion examines preserving LLM models removed from centralized platforms through BitTorrent and runtime refusal-vector orthogonalization. Commenters argue BitTorrent should be the preferred distribution method for AI model weights instead of relying on Hugging Face as a single point of failure. wren6991 notes that instead of distributing abliterated weights, one can cheaply orthogonalize activations at runtime against stock weights and distribute only refusal vectors of a few thousand floats per layer, with Antirez&\#x27;s DS4 already supporting this. Other comments cite historical torrent-based delivery by Steam and Blizzard, while raising practical concerns about Pirateface&\#x27;s name, missing scripted torrent creation, and whether peers from different trackers such as Academic Torrents can interconnect.

hackernews · skepticalgenius · Sep 20, 15:16 · [Discussion](https://news.ycombinator.com/item?id=49776699)

**「Context」** Pirate Face is a decentralized peer-to-peer layer that converts open models from Hugging Face into checksum-verified torrents held by a global swarm, so model weights are not dependent on a single host. In contrast to distributing &quot;abliterated&quot; model weights, an equivalent runtime technique orthogonalizes activations using refusal vectors, based on the finding that refusal in language models is mediated by a single direction; antirez&\#x27;s DwarfStar4 \(DS4\) supports loading such a steering vector with --dir-steering-file and adjusting its scale during inference without rebuilding the KV cache.

**「Impact」** Adopting this approach would let model distributors preserve uncensored functionality without shipping modified weights, requiring only stock checkpoints plus small refusal vectors per layer. Practical gaps include lack of scripted torrent creation and unclear cross-tracker peer compatibility.

**「Community Discussion」** Commenters broadly support BitTorrent for model weights and runtime orthogonalization as equivalent to abliterated weights with lower distribution overhead; remaining concerns include Pirateface&\#x27;s naming, missing scripted creation, and interoperability between different torrent trackers.

<details><summary>References</summary>
<ul>
<li><a href="https://pirateface.co/">Pirate Face - Turn AI into torrents that live forever</a></li>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm · GitHub</a></li>

</ul>
</details>

**Tags**: `#llm`, `#open-source`, `#torrent`, `#model-distribution`, `#refusal-vectors`

---

<a id="item-tech-news-4"></a>
### [AI-Hallucinated Intelligence Nearly Led US Troops to Board Chinese Ship](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

CNN reported on September 18 that a US military operation to intercept a Chinese ship this spring was called off only after aircraft had been launched, because the core intelligence was fabricated by an AI chatbot. A US Special Operations Command intelligence analyst used an AI chatbot to fuse open-source intelligence with classified signals intelligence, and the chatbot incorrectly identified the ship&\#x27;s cargo manifest. The analyst then used AI to package the false conclusion into a formal, official-looking intelligence report that was distributed to multiple command levels. Four people familiar with the matter said the US military initiated an interception plan; two said armed personnel were ready to board and aircraft were airborne, but officials discovered the report was AI-generated and the cargo information was wrong just before the operation.

telegram · zaihuapd · Sep 20, 03:07

**「Background」** AI hallucination is a known failure mode in which large language models produce fluent but false output, a risk that becomes severe when intelligence analysts use chatbot-style tools to fuse open-source and classified data. Corroborating reports place this incident in spring 2026 and describe the AI-generated report as falsely identifying nuclear weapons components on the Chinese vessel. The near-interception also follows broader warnings about &\#x27;AI-first&\#x27; military workflows that allow generated reports to reach commanders without mandatory verification.

**「Consequences」** A false AI-assisted intelligence report identifying a Chinese ship as carrying nuclear weapons components nearly triggered a U.S. military interception: aircraft were already airborne and armed personnel prepared to board before officials traced the report to an AI chatbot-generated cargo list and halted the operation; the Pentagon and U.S. Special Operations Command Pacific have not commented on the incident.

<details><summary>References</summary>
<ul>
<li><a href="https://securityaffairs.com/199415/ai/ai-hallucination-nearly-triggered-a-us-china-military-confrontation.html">AI Hallucination Nearly Triggered a US-China Military ...</a></li>
<li><a href="https://www.techtimes.com/articles/327796/20260920/us-military-almost-boarded-chinese-ship-over-ai-hallucinated-nuclear-claim.htm">US Military Almost Boarded Chinese Ship Over AI-Hallucinated ...</a></li>
<li><a href="https://www.explainx.ai/blog/us-military-ai-false-intelligence-china-ship-2026">AI Nearly Caused a US-China Naval Incident (2026) | explainx ...</a></li>
<li><a href="https://www.israelnationalnews.com/news/433380">AI -generated false report nearly triggered US ... | Israel National News</a></li>
<li><a href="https://www.geo.tv/latest/682719-ai-generated-false-intelligence-nearly-triggered-us-operation-against-chinese-ship">AI -generated false intelligence nearly triggered US operation against...</a></li>
<li><a href="https://gulfnews.com/world/americas/ai-generated-report-nearly-triggered-us-operation-on-chinese-ship-1.500680241">AI -Generated False Intelligence Nearly Triggered US Military...</a></li>

</ul>
</details>

**Tags**: `#AI hallucination`, `#military AI`, `#AI safety`, `#intelligence analysis`, `#human-AI interaction`

---

<a id="item-tech-news-5"></a>
### [ChangXin Technology Mass-Produces Fifth-Generation DRAM Platform](https://m.thepaper.cn/newsDetail_forward_34108116) ⭐️ 8.0/10

On September 20, at the 2026 World Manufacturing Conference, ChangXin Technology announced that its fifth-generation DRAM technology platform has officially entered mass production. A 24 GB LPDDR5X product built on the platform is also in mass production and has fully entered mainstream Chinese flagship smartphones. The platform reduces the memory array active-area half pitch to 11.95 nm, achieves a storage capacitor aspect ratio of 45:1, and lowers the core functional-area height to 6,762 nm. Under identical conditions, wafer output per wafer is more than 50% higher than the previous generation.

telegram · zaihuapd · Sep 20, 05:19

**「Background」** ChangXin Memory Technologies \(CXMT\) is China&\#x27;s leading DRAM manufacturer. Its fifth-generation DRAM platform reportedly uses quadruple patterning with deep ultraviolet \(DUV\) lithography instead of ASML&\#x27;s extreme ultraviolet \(EUV\) machines, which are restricted by US export controls. The 11.95nm half-pitch and LPDDR5X products put CXMT&\#x27;s global DRAM market share at around 10%, the first time in over a decade that the top three suppliers hold less than 90%.

**「Impact」** Chinese flagship smartphone vendors now have a locally produced 24 Gb LPDDR5X option in 496-ball and 245-ball packages, with 50% higher single-die capacity than the previous generation, reducing dependence on foreign DRAM for high-density mobile memory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businesskorea.co.kr/news/articleView.html?idxno=277366">CXMT Starts Mass Production of 5th-Gen DRAM - Businesskorea</a></li>
<li><a href="https://easternherald.com/2026/09/20/cxmt-g5-dram-mass-production-china-semiconductor/">CXMT&#x27;s G5 DRAM Platform Enters Mass Production: The Chip Built Without ASML&#x27;s Banned Machines</a></li>
<li><a href="https://easternherald.com/2026/09/20/china-cxmt-g5-dram-mass-production-samsung-micron/">China&#x27;s CXMT Starts Mass Production of G5 DRAM at 11.95nm, Challenging Samsung and SK Hynix</a></li>
<li><a href="http://hekangmed.com/m/content/20260921-5302.shtml">夫妻互换老婆干B(完) 长 鑫 科 技 官宣 第 五 代 技 术 平 台 实现 量 产</a></li>
<li><a href="https://www.chip37.com/article/20260915-7928.shtml?id=2026091803372.scm">AAAAAAAAAAAAXX表示什么-百度 长 鑫 科 技 ，最新宣布</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#LPDDR5X`, `#semiconductor manufacturing`, `#memory`, `#hardware`

---

<a id="item-tech-news-6"></a>
### [Samsung Expected to More Than Double HBM4/HBM4E DRAM Output Next Year](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 7.0/10

Samsung is reportedly planning to more than double its HBM4 and HBM4E DRAM output next year, according to sources cited in a financial news report. The expansion targets next-generation high-bandwidth memory used in AI accelerators, where supply has been identified as a constraint. The report indicates a significant capacity increase, although specific production volumes, timeline details, and affected fabs were not disclosed. The move is framed as addressing HBM bottlenecks that currently limit AI accelerator production.

hackernews · giuliomagnifico · Sep 20, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49778029)

**「Background」** High-bandwidth memory \(HBM\) is stacked DRAM designed for AI accelerators and high-performance GPUs, and HBM4/HBM4E are the newest generations in that line. Samsung began mass-production shipments of HBM4 in February and delivered 12-layer HBM4E samples to customers including Nvidia in May. The reported output increase is evidenced by a planned rise in outsourced cleaning of glass carriers used in wafer thinning for HBM, from 20,000 wafers per month this year to 50,000 next year.

**「Impact」** Samsung&\#x27;s planned output increase is expected to ease HBM supply constraints for AI accelerator vendors, but without disclosed volume targets the concrete effect on availability and prices remains uncertain.

**「Community Discussion」** Commenters identify HBM as a key bottleneck, with one noting Chinese AI accelerator production is limited by CXMT HBM capacity rather than processor yields. Others discuss die thinning complexity, question HBM as consumer main memory, worry about worsening consumer DRAM prices, and ask whether the increase will satisfy AI demand.

<details><summary>References</summary>
<ul>
<li><a href="https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say">Samsung to Double HBM4 Output Next Year, Sources Say</a></li>
<li><a href="https://www.kucoin.com/news/flash/samsung-to-double-hbm4-series-production-in-2025">Samsung to Double HBM4 Series Production in 2025 - KuCoin</a></li>
<li><a href="https://www.binance.com/en/square/post/09-20-2026-samsung-electronics-plans-to-double-hbm4-and-hbm4e-output-next-year-analyst-says-368643610309916">Samsung Electronics Plans to Double HBM4 and HBM4E Output ...</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#AI`, `#memory`, `#semiconductors`, `#supply chain`

---

<a id="item-tech-news-7"></a>
### [Why Decontamination Reports Can&\#x27;t Fix Benchmark Contamination](https://www.reddit.com/r/MachineLearning/comments/1wlimaj/why_decontamination_reports_cant_fix_benchmark/) ⭐️ 7.0/10

The post argues that decontamination reports cannot reliably detect benchmark contamination because the lab checks itself, the training corpus cannot be disclosed due to litigation exposure, and matching misses paraphrases, forum walkthroughs, GitHub solutions, and synthetic data. It cites OpenAI&\#x27;s February decision to stop reporting SWE-bench Verified after every frontier model tested could reproduce the human-written reference fix or verbatim details of the problem statement, with progress slowing to six points in six months. The proposed alternative is evaluator-controlled testing: submission never receives labels, evaluation runs with no network, the evaluator builds code from a named commit and reproduces the score, and test data is generated after submissions freeze. The author has built a small prototype at holdoutlabs-ai.github.io/reproduce-it-or-it-doesnt-count and notes that repeated submissions squeezing a hidden test set is the first gap to close.

reddit · r/MachineLearning · /u/NoahPersaud · Sep 20, 14:31

**「Background」** SWE-bench Verified is a coding benchmark created by OpenAI from public GitHub issues and pull requests, designed to measure whether models can resolve real software engineering tasks. Because it is derived from publicly scraped repositories, large language models pretrained on web data may have seen the tasks or solutions, leading to benchmark contamination. In February 2026 OpenAI retired SWE-bench Verified, citing saturation and contamination, and recommended SWE-bench Pro as a replacement.

**「Impact」** For AI benchmark evaluators, relying on vendor decontamination reports is insufficient; only externally reproducible evaluation with withheld labels and post-freeze test data can provide meaningful evidence of capability. However, the author acknowledges this does not prove benchmark quality or prevent test-set squeezing through repeated submissions.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/">Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-swe-bench-verified/">Introducing SWE-bench Verified | OpenAI</a></li>
<li><a href="https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/">OpenAI Drops SWE-bench Verified: What It Means for AI</a></li>

</ul>
</details>

**Tags**: `#benchmark contamination`, `#AI evaluation`, `#SWE-bench`, `#decontamination`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [LG TVs Record Audio When Off, Highlight Smart TV ACR Tracking](https://www.theverge.com/tech/997682/every-tv-company-is-spying) ⭐️ 7.0/10

A Gamers Nexus investigation claims LG smart TVs record and store audio even when they appear to be off, track viewing activity, and could potentially be remotely compromised into surveillance devices. LG&\#x27;s response has not satisfied users. The report says nearly all smart TVs perform automatic content recognition and share viewing data with partners, with authorization often buried in lengthy agreements. It also notes that on rooted devices the microphone can continue recording for 10 to 15 seconds after a voice command ends. Experts are calling for federal privacy legislation that requires explicit consent and limits data collection.

telegram · zaihuapd · Sep 20, 04:22

**「Background」** Automatic content recognition \(ACR\) lets smart TV platforms identify on-screen content, often to support advertising, recommendations, or measurement. Smart TV privacy concerns have grown as manufacturers embed microphones, cameras, and persistent network connections in consumer televisions.

**「Impact」** LG smart TV owners and users of other ACR-enabled smart TVs face hidden audio recording and viewing-data sharing that may continue when devices appear powered off, strengthening the case for opt-in consent and federal privacy rules.

**Tags**: `#privacy`, `#security`, `#smart TV`, `#ACR`, `#consumer electronics`

---

<a id="item-tech-news-9"></a>
### [Hunan Police Chiefs Removed Over Alleged Extortion of VPN Software Founder](https://finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve6751470.shtml) ⭐️ 7.0/10

Two police chiefs in Shaoyang County, Hunan—county public security bureau head Yin Xiangfeng and deputy bureau head Tang Zhanxiong—were removed in July 2025 for allegedly directing officers to Shanghai to extort 100 million yuan from tech company controller Zheng Shuai. Zheng&\#x27;s company developed VPN-capable software that authorities deemed an illegal &\#x27;wall-crossing&\#x27; tool; he was taken into custody in Shanghai in January 2024 and only released on bail after paying the full 100 million yuan. Zheng has now been held for nearly 1,000 days without a judgment, and the Shaoyang County procuratorate has twice issued correction notices to the court over extended detention this year.

telegram · zaihuapd · Sep 20, 14:35

**「Background」** In Chinese legal and tech contexts, “远洋捕捞” \(long-distance fishing\) refers to police from one locality traveling across jurisdictions to detain suspects and extract payments, often described as extortion. Software that provides VPN-like “翻墙” functionality is generally illegal in China without state approval. Prolonged pretrial detention beyond legal limits can trigger a procuratorate’s “纠正违法通知书” \(notice to correct unlawful acts\), as in the case of Zheng Shuai’s near-thousand-day detention.

**「Impact」** For Chinese developers and companies offering VPN-related software, this case shows that cross-jurisdiction police extortion can lead to the removal of senior officials, but the founder remains detained after nearly 1,000 days despite prosecutorial objections, signaling continued legal and operational risk.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve6751470.shtml">finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve...</a></li>

</ul>
</details>

**Tags**: `#China`, `#tech policy`, `#VPN software`, `#legal risk`, `#law enforcement`

---

## Financial News

<a id="item-finance-news-1"></a>
### [American companies squeezed by tariffs, fuel costs and rising rates](https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html) ⭐️ 9.0/10

American companies across manufacturing, transportation, and retail are being squeezed by tariffs, surging fuel costs from the Iran war, and rising interest rates. The Federal Reserve has raised rates for the first time in three years and signaled another hike is possible.

rss · CNBC Finance · Sep 20, 12:47

**「Background」** Tariffs make raw materials and goods more expensive, fuel costs push up making and shipping, and higher rates raise the cost of financing inventory and equipment.

**「Impact」** Airline passengers are seeing fewer flights and fares up more than 23% in August from a year earlier, and Home Depot&\#x27;s CFO says energy and raw-material costs will fully offset $730 million in tariff refunds.

**Tags**: `#tariffs`, `#fuel prices`, `#interest rates`, `#manufacturing`, `#inflation`

---