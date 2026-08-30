---
layout: default
title: "Horizon Summary: 2026-08-30 (EN)"
date: 2026-08-30
lang: en
---

> From 26 items, 9 important content pieces were selected

---

**Technology News**
1. [Tencent Releases and Open-Sources Hy4 Preview Model](#item-tech-news-1) ⭐️ 8.0/10
2. [South Korea Selects Consortiums for Free Nationwide Domestic AI Service](#item-tech-news-2) ⭐️ 8.0/10
3. [Sony Music, Warner Chappell Sue Anthropic Over Pirated Lyrics Training Data](#item-tech-news-3) ⭐️ 8.0/10
4. [DHS uses obscure 1509 summons to snoop on journalists and NGOs](#item-tech-news-4) ⭐️ 7.0/10
5. [Chips and Cheese Analyzes Samsung&\#x27;s Hot Chips 2026 PIM Design](#item-tech-news-5) ⭐️ 7.0/10
6. [100-Year-Old SPC Beats SOTA on TSB-AD-M Anomaly Benchmark](#item-tech-news-6) ⭐️ 7.0/10
7. [Chinese Chipmaker CXMT Sues Pentagon Over Military Blacklist](#item-tech-news-7) ⭐️ 7.0/10

**Financial News**
1. [US Appeals Court Rules Sports Event Contracts Are Bets, Creating Circuit Split](#item-finance-news-1) ⭐️ 7.0/10
2. [China&\#x27;s Four Ministries Launch One-Year Motor Vehicle Quality Inspection Campaign](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Tencent Releases and Open-Sources Hy4 Preview Model](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

Tencent released and open-sourced Hy4 preview, a new AI model that has quickly gained traction on OpenRouter, processing trillions of tokens within a couple of days, surpassing GLM 5.3&\#x27;s weekly volume. The model is notable for a claimed early-stage recursive self-improvement loop, in which it contributed to automated optimization of training methods, data strategies, evaluation frameworks, and low-level operators by proposing approaches, running experiments, and iterating on results. Hy4 preview is also aggressively priced, with a 5% cache cost compared to the 10–20% typical among competitors. Community reports note its predecessor Hy3 performed well as a general-purpose agentic model, close to DeepSeek4-flash in their tests. The release includes open-source availability, though detailed benchmark data and the full validation of the recursive self-improvement claim are not specified in the supplied content.

hackernews · shenli3514 · Aug 29, 19:33 · [Discussion](https://news.ycombinator.com/item?id=49492632)

**「Background」** Tencent Hy4 preview is a large language model using a mixture-of-experts \(MoE\) architecture with 770 billion total parameters and 49 billion active parameters, and it has a context window of over 1 million tokens. It is released under the Apache 2.0 license and made available through Tencent Cloud, OpenRouter, and public repositories, allowing self-hosted inference.

**「Impact」** Developers can now access Hy4 preview via OpenRouter at $0.834 per million input tokens and $2.501 per million output tokens with a 1,048,576-token context window, while the Apache 2.0 weights allow self-hosting of the 770B-parameter \(49B active\) mixture-of-experts model.

**「Community Discussion」** Commenters highlight Hy4&\#x27;s rapid OpenRouter adoption and unusually low 5% cache pricing as key adoption drivers, while one user notes Hy3 was a strong general-purpose agentic model. However, some criticize Tencent&\#x27;s release visuals for &\#x27;chart crimes&\#x27; such as order inconsistencies and over-highlighting, and the recursive self-improvement claim remains a point of interest but is not independently validated in the comments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open - Sources Tencent Hy 4 preview - Tencent</a></li>
<li><a href="https://www.testingcatalog.com/tencent-released-open-source-hy4-preview-model/">Tencent releases open - source Hy 4 preview model</a></li>
<li><a href="https://www.brocker.org/tencent-hy4-preview-open-source-770b-parameters-1m-context">Tencent open - sources Hy 4 preview 770B MoE model</a></li>
<li><a href="https://openrouter.ai/tencent/hy4-preview">Hy4 preview - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://explainx.ai/blog/tencent-hy4-preview-770b-moe-1m-context-august-2026">Hy4 Preview: 770B Open Weights at $0.83/M Input | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#LLM`, `#open source`, `#Tencent`

---

<a id="item-tech-news-2"></a>
### [South Korea Selects Consortiums for Free Nationwide Domestic AI Service](https://www.koreatimes.co.kr/business/tech-science/20260828/skt-kt-kakao-consortiums-selected-for-free-ai-service-for-public) ⭐️ 8.0/10

South Korea’s Ministry of Science and ICT has selected consortiums led by SK Telecom, KT, and Kakao to operate the &quot;AI for All&quot; project, which will offer a nationwide free AI service with no token limits to all citizens. The service will use domestically developed large language models, begin internal testing in September, and officially launch by the end of the year. The government will supply the three consortiums with 512 Nvidia B200 chips and, starting in 2027, subsidize nationwide operating costs. The service can be integrated into government systems for tasks such as medical appointment booking, housing search, and tax consultation. Naver is not participating in the project.

telegram · zaihuapd · Aug 29, 15:31

**「Background」** South Korea&\#x27;s science ministry is running the &\#x27;AI for All&\#x27; initiative as a public infrastructure project to make AI services accessible to everyone. It has selected consortia led by SK Telecom, KT, and Kakao to build free general-purpose AI chatbots and public AI agents, with government-provided access to a combined 512 Nvidia B200 GPUs this year.

**「Impact」** South Korean citizens will gain free, token-unlimited access to domestic AI services integrated with government functions, while the selected consortiums receive state-backed GPU and operating-cost support.

<details><summary>References</summary>
<ul>
<li><a href="https://www.telecompaper.com/news/skt-kt-kakao-consortia-selected-for-national-ai-for-all-project-in-korea--1581062">SKT , KT , Kakao consortia selected for national &#x27; AI ... - Telecompaper</a></li>
<li><a href="https://www.ajupress.com/view/20260828104218642">Korea picks SKT , Kakao , KT for nationwide AI service ... | Aju Press</a></li>

</ul>
</details>

**Tags**: `#South Korea`, `#AI policy`, `#domestic LLMs`, `#Nvidia B200`, `#free AI service`

---

<a id="item-tech-news-3"></a>
### [Sony Music, Warner Chappell Sue Anthropic Over Pirated Lyrics Training Data](https://www.musicbusinessworldwide.com/files/2026/08/COMPLAINT-in-Sony_Music_Publishing_US_LLC_e.pdf) ⭐️ 8.0/10

Sony Music Publishing, Warner Chappell Music, and other companies have sued Anthropic and its founders in U.S. federal court in California, alleging that the company illegally downloaded more than 7 million books from pirate libraries such as LibGen and PiLiMi and scraped song lyrics to train its Claude model. The complaint also accuses Anthropic of removing copyright management information from lyrics. The plaintiffs are seeking statutory damages of up to $150,000 per infringed work and a permanent injunction. The filing notes that similar prior litigation has resulted in a $1.5 billion settlement.

telegram · zaihuapd · Aug 30, 01:00

**「Background」** Anthropic is the AI company behind the Claude large language models, which have faced copyright lawsuits from book publishers and music rights holders over the data used for training. LibGen and PiLiMi are commonly named pirate libraries that provide unauthorized access to books and lyrics; prior litigation by music publishers over AI training data led to a $1.5 billion settlement. This complaint alleges that Anthropic removed copyright management information from lyrics and used millions of pirated books, with statutory damages of up to $150,000 per infringed work.

**「Impact」** If the court rules in the plaintiffs&\#x27; favor, Anthropic could face damages of up to $150,000 per work and an injunction that restricts its training practices, potentially raising the cost and legal risk of using pirated or scraped copyrighted material in AI model development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.musicbusinessworldwide.com/now-sony-music-publishing-and-warner-chappell-sue-anthropic-in-multi-billion-dollar-lawsuit-one-of-the-largest-and-most-blatant-ongoing-thefts-of-intellectual-property-in-history/">Sony Music Publishing and Warner Chappell sue Anthropic in multi-billion dollar lawsuit</a></li>
<li><a href="https://www.businessinsider.com/anthropic-claude-training-copyright-music-lyrics-sony-lawsuit-2026-8">Sony accuses Anthropic of &#x27;brazen campaign&#x27; to train Claude on its music — and wants up to $150,000 a song</a></li>

</ul>
</details>

**Tags**: `#copyright`, `#AI training data`, `#Anthropic`, `#music industry`, `#legal`

---

<a id="item-tech-news-4"></a>
### [DHS uses obscure 1509 summons to snoop on journalists and NGOs](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits) ⭐️ 7.0/10

The US Department of Homeland Security is using an obscure statutory summons, referred to as a 1509 summons, to obtain records from third parties, including phone logs of journalists, non-profits, and unions, without a judge&\#x27;s approval. In at least one case, DHS obtained six months of a journalist&\#x27;s phone records from T-Mobile covering more than 10,000 calls and texts, while Google refused a similar request. The affected person was not notified until months later, when the records were produced in litigation. In several challenges, DHS withdrew the summons before a court could rule on its legality, which critics describe as a strategy to avoid judicial scrutiny. This creates compliance uncertainty for tech and telecom companies and raises significant privacy concerns.

hackernews · firefax · Aug 29, 18:44 · [Discussion](https://news.ycombinator.com/item?id=49492219)

**「Background on 19 U.S.C. § 1509 and DHS Use」** 19 U.S.C. § 1509 is a customs statute that allows the Department of Homeland Security to issue administrative summonses for records relevant to customs investigations, traditionally without prior judicial approval. The Trump administration has invoked this provision to demand call logs, financial records, and other information from journalists, unions, and nonprofit organizations, often without notifying the targets or obtaining a warrant. Legal challenges have arisen because, unlike subpoenas or warrants, these summonses are not reviewed by a judge before issuance, and DHS has withdrawn them after court challenges to avoid a ruling on their legality.

**「Impact」** Telecom and technology companies now face inconsistent pressure to comply with 1509 summons: some providers such as T-Mobile have handed over extensive call records without notifying the subscriber, while Google has refused, leaving users&\#x27; communications metadata exposed to government collection without judicial oversight and with no uniform industry standard.

**「Community Discussion」** HN commenters express concern that DHS is withdrawing challenged summonses to avoid a court ruling on legality, and note that compliance is voluntary unless DHS goes to court to enforce it. Some highlight the divergent responses of T-Mobile and Google, and one user recommends self-hosted email infrastructure for journalists who cannot rely on centralized systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits">Trump’s DHS is using an obscure law to secretly snoop on journalists, non-profits and unions: ‘It’s outrageous’ | Trump administration | The Guardian</a></li>
<li><a href="https://aaronparnas.substack.com/p/saturday-update-impeachment-calls">Saturday Update: Impeachment Calls, DHS Spies on Journalists, Cherry Trees Cut Down, McConnell Update, Major CSAM Ruling</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#surveillance`, `#tech-policy`, `#telecom`, `#legal`

---

<a id="item-tech-news-5"></a>
### [Chips and Cheese Analyzes Samsung&\#x27;s Hot Chips 2026 PIM Design](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) ⭐️ 7.0/10

Chips and Cheese published a technical analysis of Samsung&\#x27;s processing-in-memory \(PIM\) design presented at Hot Chips 2026. The article examines the architecture&\#x27;s potential to accelerate AI workloads by reducing data movement and its limitations in practical deployment. It notes that similar PIM concepts have been shown at earlier Hot Chips events, making this presentation an incremental refinement rather than a breakthrough. The analysis targets readers interested in AI hardware and computer architecture.

hackernews · ingve · Aug 29, 06:06 · [Discussion](https://news.ycombinator.com/item?id=49487341)

**「Processing-in-memory background」** Processing-in-memory \(PIM\) integrates compute logic directly into DRAM to reduce data movement between memory and processors. At Hot Chips 2026, Samsung presented LPDDR5X-PIM, which adds multiply-accumulate \(MAC\) units inside LPDDR5X DRAM while keeping the chip compatible with a standard memory controller, targeting AI inference workloads.

**「Impact」** AI hardware developers should treat Samsung&\#x27;s PIM as experimental rather than near-term infrastructure: the design&\#x27;s requirement for exact data placement and concerns about data movement overhead limit its applicability, while Samsung&\#x27;s commercial memory focus remains on HBM4 for AI computing.

**「Community Discussion」** Commenters observed that processing-in-memory is a decades-old concept, with similar Samsung presentations at Hot Chips in 2020 or 2021, and questioned whether this design will progress beyond trade-show demonstrations. Some argued the approach is well suited to AI, gaming, and crypto workloads but requires developers to know exactly where dependent data resides, making general programming highly constrained; a specific concern was that matrix multiplication still involves substantial data movement that PIM may not eliminate.

<details><summary>References</summary>
<ul>
<li><a href="https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing">Hot Chips 2026: Samsung&#x27;s Processing-in-Memory (PIM)</a></li>
<li><a href="https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth">Hot Chips 2026: Samsung makes LPDDR5X smart with logic unit in memory ...</a></li>
<li><a href="https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing">Samsung Ships Industry-First Commercial HBM4 With Ultimate...</a></li>

</ul>
</details>

**Tags**: `#processing-in-memory`, `#Samsung`, `#AI hardware`, `#computer architecture`, `#Hot Chips`

---

<a id="item-tech-news-6"></a>
### [100-Year-Old SPC Beats SOTA on TSB-AD-M Anomaly Benchmark](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 7.0/10

The author argues that the widely used Paparrizos TSB-AD-M benchmark for time series anomaly detection is too trivial, reporting that a 100-year-old Statistical Process Control \(SPC\) method can outperform state-of-the-art methods on many of its datasets. They demonstrate perfect SPC results on an example ECG trace and say dozens of traces marked &quot;TAO&quot; are even more trivial. The post calls for community introspection, stating that most progress over the last decade appears illusory and that the benchmark does not support meaningful claims about proposed algorithms. The author adds they have done 90% of the work to introduce more challenging TSAD problems using domains such as sled dogs, tuna, fuel cells, and smart manufacturing.

reddit · r/MachineLearning · /u/eamonnkeogh · Aug 29, 20:16

**「Background」** The TSB-AD benchmark \(from Paparrizos et al., published at VLDB 2022\) is a widely used evaluation suite for univariate time-series anomaly detection, offering datasets and evaluation scripts for comparing detection algorithms \[tool-1-1\]\[tool-1-2\]. Recent papers such as PaAno rely on an updated version, TSB-AD \(Liu &amp; Paparrizos, 2024\), which is described as correcting dataset-related labeling flaws to enable more rigorous comparisons \[tool-1-3\]. The Reddit post challenges whether even this corrected benchmark remains too easy, since a simple statistical process control method outperforms modern methods on many of its datasets.

**「Impact」** Researchers evaluating time-series anomaly detection methods on TSB-AD-M should treat reported state-of-the-art improvements with skepticism, because simple statistical process control can achieve perfect or near-perfect results on many of its datasets. The critique targets the benchmark&\#x27;s difficulty rather than the proposed algorithms themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://vldb.org/pvldb/vol15/p1697-paparrizos.pdf">TSB -UAD: An End-to-End Benchmark Suite for Univariate</a></li>
<li><a href="https://github.com/TheDatumOrg/TSB-AD">GitHub - thedatumorg/ TSB - AD : Time - Series Anomaly Detection</a></li>
<li><a href="https://arxiv.org/pdf/2602.01359">PaAno: Patch-Based Representation Learning for Time - Series ...</a></li>

</ul>
</details>

**Tags**: `#time series`, `#anomaly detection`, `#benchmarking`, `#machine learning`, `#statistical process control`

---

<a id="item-tech-news-7"></a>
### [Chinese Chipmaker CXMT Sues Pentagon Over Military Blacklist](https://www.bloomberg.com/news/articles/2026-08-29/chinese-chipmaker-cxmt-sues-pentagon-to-get-off-us-blacklist) ⭐️ 7.0/10

ChangXin Memory Technologies \(CXMT\), the world&\#x27;s fourth-largest DRAM maker, has sued the US Department of Defense in the US District Court for the District of Columbia, naming Defense Secretary Hegseth as a defendant. The suit asks the court to remove CXMT from a Pentagon list of companies alleged to have links to the Chinese military, arguing its memory chips are for civilian and commercial use. The company says it has suffered reputational and commercial harm since being added to the list in January 2025 but that the designation will not affect daily operations. Bloomberg reports that CXMT&\#x27;s market value has surpassed Tencent, making it China&\#x27;s largest company.

telegram · zaihuapd · Aug 29, 05:43

**「Background」** The lawsuit concerns the U.S. Department of Defense’s “Chinese military companies” list, which can cause reputational and commercial harm even when it does not directly prohibit transactions. CXMT, a Chinese DRAM manufacturer, was first added to this list in January 2025 during the Biden administration and was retained when the Pentagon updated the list in June under the Trump administration. The company claims it provided information to the Pentagon for over a year and that the listing decisions lacked a factual record, applicable law, or reasonable basis.

**「Impact」** A ruling in CXMT&\#x27;s favor would remove the world&\#x27;s fourth-largest DRAM maker from the Pentagon&\#x27;s military-linked blacklist, alleviating the reputational and commercial harm it has cited since January 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.sina.cn/2026-08-29/detail-inipymqr3700531.d.html?vt=4&amp;pos=108">长鑫存储起诉五角大楼，赫格塞斯也被列为被告|美国国防部|彭博社|中国|芯片|黑名单_手机新浪网</a></li>
<li><a href="https://finance.ifeng.com/c/8vz5ghKcjD2">长鑫存储起诉美国国防部_凤凰网</a></li>
<li><a href="https://finance.sina.com.cn/wm/2026-08-29/doc-inipyrwp3624195.shtml">中国芯片企业起诉美国国防部_新浪财经_新浪网</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#DRAM`, `#US-China tech policy`, `#legal`, `#hardware`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US Appeals Court Rules Sports Event Contracts Are Bets, Creating Circuit Split](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

A U.S. appeals court ruled that sports-related event contracts offered by Kalshi, Crypto.com, and Robinhood are sports bets rather than CFTC-regulated swaps, denying their requests to block Nevada&\#x27;s gambling enforcement.

rss · CNBC Finance · Aug 29, 02:23

**「Background」** The platforms and the Commodity Futures Trading Commission argued that event contracts are swaps under exclusive federal jurisdiction, while Nevada and 44 states view the sports-related offerings as sports betting; the 9th Circuit&\#x27;s ruling conflicts with an April 3rd Circuit decision that only the CFTC can regulate such contracts.

**Tags**: `#prediction markets`, `#CFTC`, `#sports betting`, `#regulation`, `#Supreme Court`

---

<a id="item-finance-news-2"></a>
### [China&\#x27;s Four Ministries Launch One-Year Motor Vehicle Quality Inspection Campaign](https://weibo.com/1893892941/5336817496754349) ⭐️ 7.0/10

Four Chinese ministries, led by the Ministry of Industry and Information Technology, launched a one-year special action on August 27, 2026 to inspect production consistency, quality, and new technology testing across six categories of motor vehicle manufacturers, products, and inspection agencies. Violators may face penalties including notification, suspension of product announcements and certifications, registration suspension, or fines.

telegram · zaihuapd · Aug 29, 13:30

**「Background」** The action follows a July 2026 pledge by the Ministry of Industry and Information Technology to deepen road motor vehicle production consistency—making sure manufactured vehicles match their approved design—and its 2026 annual inspections cover approved manufacturers, products, and sales locations.

**「Impact」** Automakers, component suppliers, and inspection agencies in China may face increased compliance obligations and the risk of suspended product approvals or registrations during the inspection period.

<details><summary>References</summary>
<ul>
<li><a href="https://m.jiemian.com/article/14457411_microcontent.html">工 信 部 组织开展 2026 ...</a></li>
<li><a href="http://jjckb.xinhuanet.com/20260717/6f074de6236e4feeb51ccda9c8942923/c.html">jjckb.xinhuanet.com/20260717/6f074de6236e4feeb51ccda9c8942923...</a></li>

</ul>
</details>

**Tags**: `#China auto regulation`, `#vehicle quality enforcement`, `#automotive industry`, `#regulatory policy`

---