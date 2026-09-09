---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 43 items, 15 important content pieces were selected

---

**Technology News**
1. [OpenAI Claims Navier–Stokes Millennium Prize Solution Amid Priority Dispute](#item-tech-news-1) ⭐️ 9.0/10
2. [AlphaGenome Atlas Maps Every Single-Letter DNA Change](#item-tech-news-2) ⭐️ 8.0/10
3. [NeurIPS Desk-Rejected 178 Papers Over AI Detector False Positives](#item-tech-news-3) ⭐️ 8.0/10
4. [ByteDance Founder Oversees Real-Time Spatial Video Model](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI Releases ChatGPT Images 2.5 with Faster Generation and New Editing Tools](#item-tech-news-5) ⭐️ 8.0/10
6. [Meta Introduces Muse, a Personal AI Agent](#item-tech-news-6) ⭐️ 7.0/10
7. [Navier-Stokes Statement Alleges OpenAI Used Research, Threatened Mathematician](#item-tech-news-7) ⭐️ 7.0/10
8. [Qwen3.8 27B Quantization: 4-Bit Holds, 1-Bit Fails](#item-tech-news-8) ⭐️ 7.0/10
9. [Terence Tao Warns AI Rumors Threaten Open Math Research](#item-tech-news-9) ⭐️ 7.0/10
10. [Malaysia Eyes Huawei Ascend 910C for $494M Sovereign AI Project](#item-tech-news-10) ⭐️ 7.0/10
11. [Tim Cook Absent From Apple&\#x27;s September 9 Event Video; Ternus Leads Foldable iPhone Launch](#item-tech-news-11) ⭐️ 7.0/10
12. [ASML and TSMC Plan 12-Inch High NA EUV Photomasks by 2031–2033](#item-tech-news-12) ⭐️ 7.0/10
13. [China Targets 9800 EFLOPS Intelligent Computing by 2030](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [Crypto platforms lost over $3.63 billion to cyberattacks despite security audits](#item-finance-news-1) ⭐️ 7.0/10
2. [Shanghai to fully reimburse maternity costs from October 1](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI Claims Navier–Stokes Millennium Prize Solution Amid Priority Dispute](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

OpenAI announced that an unreleased internal model produced a resolution to the Navier–Stokes existence and smoothness problem, one of seven Millennium Prize Problems with a $1,000,000 prize since May 24, 2000, after launching an effort on September 1 in response to rumors. The agents reached the resolution on September 5 in about 88 hours, with Lean formalization and verification taking an additional 17 hours via GPT‑6 Astra, sending 4.9 million messages and using about 300 billion output tokens overall, of which 2.7 million messages and about 130 billion tokens went to Navier–Stokes. NYU mathematician Tristan Buckmaster accused OpenAI of wrongdoing, saying he and Anthropic’s Levent Alpöge had worked on the problem for almost a year using Claude and Codex \(mainly GPT‑5.6 Sol\) and had a breakthrough on August 15, while OpenAI says it did not access specific user data but cannot rule out that de-identified data derived from their usage improved its models. OpenAI offered concurrent release or asked Buckmaster to author a paper, but excluded Alpöge as co-author due to OpenAI’s competitive relationship with Anthropic. Simon Willison interprets this as a case where a rumor of an unpublished solution triggered a race, similar to how rumors of security bugs now trigger exploit-finding agents.

rss · Simon Willison · Sep 8, 23:55

**「Background」** The Millennium Prize Problems are seven major unsolved mathematics problems announced by the Clay Mathematics Institute in 2000, each carrying a $1,000,000 prize. The Navier–Stokes existence and smoothness problem asks whether solutions to the Navier–Stokes equations for fluid motion always exist and remain smooth, or can develop singularities in finite time. Formal verification with tools like Lean is used to check mathematical proofs mechanically.

**「Impact」** For mathematicians using commercial LLM tools like Codex, this case shows that working drafts and partial solutions may not guarantee priority if the provider launches a competing internal effort, especially because OpenAI cannot rule out influence from de-identified training data.

**「Community Discussion」** Commenters highlight a comment by Terence Tao that even a rumor of someone working on a problem can trigger massive AI-powered effort to finish it before the original project reaches its potential, shifting incentives away from sharing promising research directions. Others note that OpenAI’s claim of an internal model more than twice as capable as GPT‑6 Astra in mathematics, trained in under two weeks, is itself remarkable but overshadowed by the dispute.

**Tags**: `#artificial intelligence`, `#mathematics`, `#Navier-Stokes`, `#OpenAI`, `#scientific discovery`

---

<a id="item-tech-news-2"></a>
### [AlphaGenome Atlas Maps Every Single-Letter DNA Change](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10

Google DeepMind has released AlphaGenome Atlas, a predictive map of all possible single-letter DNA changes in the human genome. The resource is intended to help researchers assess the effects of single-nucleotide variants, though the supplied announcement links provide little technical detail beyond the map&\#x27;s scope and access page. The Atlas is hosted on DeepMind&\#x27;s science site, and the source content does not include a release date, methodology, or performance benchmarks.

hackernews · utiiiD · Sep 8, 14:55 · [Discussion](https://news.ycombinator.com/item?id=49611251)

**「Background」** AlphaGenome is a deep learning model from Google DeepMind that processes 1-megabase DNA sequences to predict functional genomic tracks at single-base resolution \(tool-1-2\). The Atlas provides genome-wide predictions of the effect of every possible single-letter DNA change, known as single nucleotide variants, helping researchers interpret variants in both coding and non-coding regions \(tool-1-3\). This is important because most disease-associated variants fall outside protein-coding genes, where their functional impact has been difficult to assess.

**「Community Discussion」** Commenters ask whether the Atlas covers promoter sequences and whether it can interpret consumer genetic data such as 23andMe results; one commenter confirms that entering &\#x27;None&\#x27; as affiliation grants access. Others note that DeepMind biology models have had uneven impact and call for a systematic comparison.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-10014-0">Advancing regulatory variant effect prediction with AlphaGenome</a></li>
<li><a href="https://deepmind.google.com/science/alphagenome/">AlphaGenome - deepmind.google.com</a></li>

</ul>
</details>

**Tags**: `#AI`, `#genomics`, `#DeepMind`, `#bioinformatics`, `#DNA`

---

<a id="item-tech-news-3"></a>
### [NeurIPS Desk-Rejected 178 Papers Over AI Detector False Positives](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 8.0/10

NeurIPS&\#x27; position paper track desk-rejected 178 submissions—18.4% of the track—using the proprietary AI detector Pangram, with no human review or appeal process. The detector initially flagged 42.7% of submissions, and track chairs adjusted text-window settings to lower the flag rate to 12.7%; papers authored by the track chairs themselves scored between 24% and 69% under the same tool. Twenty-two papers were rejected because they scored above 0.5 while authors had checked a box denying AI use, treating the black-box score as proof of dishonesty. A Stanford study found 61.22% of human-written TOEFL essays are falsely flagged as AI, raising concerns about bias against non-native English writers, and NeurIPS published no demographic calibration data. Affected authors face no misconduct record and can resubmit to ICLR by September 25 or to ICML.

reddit · r/MachineLearning · /u/tughanbulut · Sep 8, 10:19

**「Background」** NeurIPS is one of the largest machine learning conferences, and its position paper track invites short papers on current topics. AI-generated text detectors such as Pangram assign a probability that a text was machine-written, but these tools are known to produce high false-positive rates, especially for formal, formulaic, or non-native English prose. Automated desk rejection using such scores without human review or appeal is unusual for academic peer review.

**「Immediate impact on affected authors」** The 178 authors whose position papers were desk-rejected lost the opportunity to present at NeurIPS 2026 without an appeal, though the rejection does not carry a misconduct record and papers may be resubmitted to other venues such as ICLR or ICML.

<details><summary>References</summary>
<ul>
<li><a href="https://casrai.org/news/neurips-2026-pangram-ai-detector-desk-rejection-controversy">NeurIPS 2026: Pangram AI - Detector Desk Rejections — CASRAI</a></li>

</ul>
</details>

**Tags**: `#NeurIPS`, `#AI detection`, `#academic publishing`, `#machine learning`, `#ethics`

---

<a id="item-tech-news-4"></a>
### [ByteDance Founder Oversees Real-Time Spatial Video Model](https://www.bloomberg.com/news/articles/2026-09-07/bytedance-founder-joins-ai-elite-in-race-to-perfect-world-models) ⭐️ 8.0/10

ByteDance founder Zhang Yiming is personally overseeing development of a real-time spatial video generation model, Bloomberg reported. People familiar with the matter say the model could be released as soon as October 2026, though the timeline may still change. Built on ByteDance&\#x27;s Seedance system, it would generate interactive virtual worlds that respond to voice or movement from Pico VR headset users. The system is said to achieve about 0.05 seconds of latency at 20 frames per second by offloading intensive computation to the cloud, lowering VR hardware requirements. These details are based on unnamed sources and remain unconfirmed.

telegram · zaihuapd · Sep 8, 04:05

**「Context」** ByteDance is the Chinese technology company founded by Zhang Yiming and known for platforms such as TikTok and Douyin. The reported real-time spatial video model is built on Seedance, a video generation model, and is designed to generate interactive virtual worlds that respond to Pico VR headset users&\#x27; speech or movements while offloading heavy computation to the cloud.

**「Impact」** If the reported model ships as described, Pico VR users would be the primary beneficiaries, gaining low-latency interactive spatial content with reduced local processing demands.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ByteDance">ByteDance - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ByteDance`, `#world models`, `#spatial video generation`, `#virtual reality`, `#generative AI`

---

<a id="item-tech-news-5"></a>
### [OpenAI Releases ChatGPT Images 2.5 with Faster Generation and New Editing Tools](https://openai.com/index/introducing-chatgpt-images-2-5/) ⭐️ 8.0/10

OpenAI released ChatGPT Images 2.5 on September 8, improving detail clarity, editing precision, and generation speed, with image generation latency reduced by up to 50 percent compared to 2.0. The update is available to ChatGPT, ChatGPT Work, and Codex users and adds Sketch hand-drawn guidance, templates, image comments, and prompt sharing. The API now exposes two new models: gpt-image-2.5-sunburst, recommended for workflows where editing precision matters most, and gpt-image-2.5-flare, recommended for fast, high-quality everyday generation. OpenAI also says the model follows instructions better across multiple turns and preserves subjects from reference photos more faithfully. The company reports its image models have generated more than 3 billion images across ChatGPT Images and the GPT-Image API.

telegram · zaihuapd · Sep 8, 18:45

**「Background」** ChatGPT Images is OpenAI&\#x27;s image generation and editing feature available in ChatGPT, and the GPT-Image API exposes the same underlying models to developers. Multi-turn instruction following and reference-photo preservation are central to editing workflows, where users progressively refine an image rather than generate it in a single pass.

**「Impact」** ChatGPT, ChatGPT Work, and Codex users gain immediate access to faster image generation and new Sketch, template, and sharing tools, while API developers can select gpt-image-2.5-sunburst for precise multi-turn editing or gpt-image-2.5-flare for quicker everyday generation.

**Tags**: `#OpenAI`, `#image generation`, `#ChatGPT`, `#API`, `#AI model release`

---

<a id="item-tech-news-6"></a>
### [Meta Introduces Muse, a Personal AI Agent](https://ai.meta.com/muse/) ⭐️ 7.0/10

Meta introduced Muse, a personal AI agent. The announcement prompted discussion about its prompt injection security, with Meta AI&\#x27;s David Singleton describing a layered defense including model training, untrusted-source marking, deterministic checks, and an ensemble of classifiers. Commenters noted Meta&\#x27;s large existing user base could help adoption, while others expressed privacy concerns about an agent with broad personal access.

hackernews · yks · Sep 8, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49615537)

**「Background」** Meta&\#x27;s Muse is a personal AI agent designed to help users with everyday tasks such as messaging, scheduling, and information retrieval. It can be accessed through WhatsApp and will soon be available on Meta&\#x27;s AI glasses. The system includes layered privacy and security controls, such as granular permissions, opt-out options for training data, and an architecture that prevents direct access to stored passwords or payment credentials.

**「Impact」** The described layered prompt injection defenses may reduce the risk of malicious instructions for Muse users, but privacy concerns raised by commenters could limit adoption among privacy-conscious individuals.

**「Community Discussion」** Commenters are divided: some believe Meta&\#x27;s massive existing user base could drive mainstream adoption, while others refuse to use a Meta personal agent due to data harvesting concerns. One user hopes to repurpose Muse to scrape their own Facebook groups after API shutdown.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/">Muse, Meta’s New Personal AI Agent, Needs You to Trust It | WIRED</a></li>
<li><a href="https://www.androidheadlines.com/2026/09/meta-launches-muse-ai-agent-everyday-tasks.html">Meet Muse: Meta&#x27;s New Personal AI Agent Built for Daily Errands</a></li>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Meta`, `#personal assistant`, `#prompt injection`, `#product launch`

---

<a id="item-tech-news-7"></a>
### [Navier-Stokes Statement Alleges OpenAI Used Research, Threatened Mathematician](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 7.0/10

A PDF statement by Tristan Buckmaster alleges that OpenAI accessed and may have used unpublished joint work with Levent Alpöge on finite-time blowup for the incompressible Euler, Boussinesq, and porous media equations. The August 15 result does not solve the $1,000,000 Millennium Prize problem, but Buckmaster and Alpöge claim a proof for a related non-Millennium Navier-Stokes problem that could be a step toward it. Buckmaster reports that OpenAI offered to post after them and describe them as the &\#x27;closest humans to the problem,&\#x27; then threatened his career when he declined, while OpenAI states it cannot rule out that de-identified data from product usage helped improve its models. The Hacker News discussion shows strong concern about research integrity and potential misuse of user data, though the central claim that Buckmaster&\#x27;s work was used in training remains unverified.

hackernews · procedurecall · Sep 8, 05:42 · [Discussion](https://news.ycombinator.com/item?id=49605915)

**「Background」** The Navier–Stokes existence and smoothness problem is a Clay Millennium Prize problem that asks whether smooth solutions to the 3D incompressible Navier–Stokes equations can develop singularities from smooth initial data. A related line of research concerns finite-time blowup for the 3D incompressible Euler and Boussinesq equations; Tristan Buckmaster and Levent Alpöge, who works at Anthropic, recently announced progress on these problems without claiming a proof of the Millennium problem. Around the same time, OpenAI said an internal model produced a proof that the 3D Navier–Stokes equations can develop singularities, and Buckmaster subsequently alleged that OpenAI used his research insights without attribution.

**「Impact」** The allegations have cast doubt on OpenAI&\#x27;s claimed Navier-Stokes breakthrough and sparked heated debate in the mathematics community over credit allocation and AI training data use, potentially undermining trust in AI-assisted mathematical research.

**「Community Discussion」** Commenters express anger over the alleged threats and data use, but some note that OpenAI&\#x27;s own statement leaves ambiguous whether Buckmaster&\#x27;s work was actually used in training and frame the conflict as an accelerated version of longstanding academic competition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/09-08-2026-openai-says-ai-solved-navier-stokes-millennium-prize-problem-364521528752966">OpenAI Says AI Solved Navier – Stokes Millennium Prize Problem</a></li>
<li><a href="https://chang.aevumnews.com/en/openai-s-controversial-role-in-solving-navier-stokes-problem">OpenAI &#x27;s Controversial Role in Solving the Navier - Stokes Problem</a></li>
<li><a href="https://www.techmeme.com/260908/p26">Techmeme: Mathematician Tristan Buckmaster alleges OpenAI ...</a></li>
<li><a href="https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/">OpenAI fought dirty on career-making math problem, says NYU mathematician | TechCrunch</a></li>
<li><a href="https://www.wired.com/story/openai-navier-stokes-math-discovery-academics/">OpenAI Just Claimed a Huge Math Discovery. Some Academics Are Crying Foul | WIRED</a></li>
<li><a href="https://www.businessinsider.com/openai-navier-stokes-math-breakthrough-drama-2026-9">OpenAI&#x27;s Big Math Breakthrough Claim Sparks Drama - Business Insider</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#artificial-intelligence`, `#research-integrity`, `#openai`, `#navier-stokes`

---

<a id="item-tech-news-8"></a>
### [Qwen3.8 27B Quantization: 4-Bit Holds, 1-Bit Fails](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 7.0/10

A benchmark of Qwen3.8 27B quantizations found that 4-bit quantization largely maintained model quality, while 1-bit quantization collapsed. The empirical results, published by Quesma, provide practical guidance for practitioners weighing model quality against resource usage. The findings indicate minimal quality loss down to 4-bit precision.

hackernews · stared · Sep 8, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49611128)

**「Background」** Quantization reduces the precision of model weights to shrink memory usage and improve inference speed, with GGUF formats commonly used for local deployment. Previous analysis of Qwen3.6 27B showed that 4-bit variants like Q4\_K\_M require under 30 GB and the smallest 2-bit variant under 18 GB, making them feasible on consumer GPUs or Apple silicon. The current Qwen3.8 27B quantizations are available from Unsloth on Hugging Face, and early independent tests indicate quality holds through 4-bit before degrading sharply at 2-bit and collapsing at 1-bit.

**「Impact」** Practitioners deploying Qwen3.8 27B can use 4-bit quantization to reduce resource requirements with minimal quality loss, but should avoid 1-bit quantization.

**「Community Discussion」** Commenters debated the interpretation of the Wilson 95% confidence intervals, noting they do not capture run-to-run variation. Others requested benchmarks for Q3 and KV cache quantization, and one commenter speculated that extended thinking may help offset quantization-induced quality loss.

<details><summary>References</summary>
<ul>
<li><a href="https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/">Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses - Quesma Blog</a></li>
<li><a href="https://intuitionlabs.ai/articles/qwen3-8-27b-local-research-assistant">Qwen3.8-27B for Local Research: Accuracy and Hardware Guide | IntuitionLabs</a></li>
<li><a href="https://quesma.com/blog/qwen-quantization-quality/">Do Qwen3.6 27B quantizations break the pelican? - Quesma Blog</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#large-language-models`, `#benchmarking`, `#Qwen`, `#model-compression`

---

<a id="item-tech-news-9"></a>
### [Terence Tao Warns AI Rumors Threaten Open Math Research](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 7.0/10

Terence Tao warned on Mathstodon that the collection of good, fruitful open mathematical problems is being mined in a non-renewable fashion, making such problems potentially scarce. He said even a rumor that someone is working on a problem can trigger a massive amount of AI-powered effort to flatten it before the original research project reaches its full potential. As a result, incentives may now point toward researchers no longer sharing promising research directions with the broader community. Tao cautioned that this would reverse centuries of open science traditions and do serious long-term damage to the future of mathematics.

rss · Simon Willison · Sep 9, 00:20

**「Background」** Terence Tao is a Fields Medal-winning mathematician known for contributions across many areas, including fluid dynamics and mathematical physics. In mathematics, &\#x27;open problems&\#x27; are unsolved research questions that guide progress, and the tradition of open science encourages researchers to share promising directions so others can build on them.

**「Impact」** Mathematics researchers may become more reluctant to share promising directions, potentially reducing open collaboration and slowing progress as AI-powered efforts rapidly exhaust open problems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=HUkBz-cdB-k">Terence Tao : Hardest Problems in Mathematics , Physics... - YouTube</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#mathematics`, `#open-science`, `#research-ethics`, `#terence-tao`

---

<a id="item-tech-news-10"></a>
### [Malaysia Eyes Huawei Ascend 910C for $494M Sovereign AI Project](https://www.businesstimes.com.sg/international/malaysia-eyes-huawei-chips-ai-project-despite-us-warning) ⭐️ 7.0/10

Malaysia is evaluating Huawei Ascend 910C chips as the core of a sovereign AI project worth 20 billion ringgit \(about $494 million\). If it proceeds, this would be the first public case of a foreign government officially choosing Chinese AI accelerators over US products. Sources did not disclose how many chips would be purchased. The Trump administration warned that using these Huawei accelerators could violate US export rules, but Malaysia&\#x27;s government views the decision as purely commercial. The plan remains under evaluation and has not been confirmed.

telegram · zaihuapd · Sep 8, 03:35

**「Background」** Huawei’s Ascend 910C is an AI accelerator chip that competes with US products such as Nvidia’s offerings, and Huawei remains subject to US export restrictions imposed over national-security concerns. Malaysia previously signed export-control commitments with Washington, and US officials have warned that using Huawei chips could violate American rules, making the decision a test of those commitments.

**「Impact」** If Malaysia proceeds, the responsible agencies and vendors may face US export-control scrutiny because the Trump administration said using the Huawei Ascend 910C could violate US export rules.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scmp.com/week-asia/politics/article/3366792/will-malaysias-potential-huawei-ai-deal-risk-clash-over-us-trade-pact">Will Malaysia’s potential Huawei AI deal risk clash with US trade pact? | South China Morning Post</a></li>
<li><a href="https://thearabianpost.com/malaysia-evaluates-huawei-chips-for-national-ai-network/">Malaysia evaluates Huawei chips for national AI network — Arabian Post</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#geopolitics`, `#Huawei`, `#export controls`, `#sovereign AI`

---

<a id="item-tech-news-11"></a>
### [Tim Cook Absent From Apple&\#x27;s September 9 Event Video; Ternus Leads Foldable iPhone Launch](https://www.macrumors.com/2026/09/07/tim-cook-wont-appear-apple-sept-9-event-video/) ⭐️ 7.0/10

Tim Cook will not appear in Apple&\#x27;s September 9 event video, according to Bloomberg&\#x27;s Mark Gurman citing sources. Cook stepped down as CEO on September 1 and became executive chairman, with John Ternus taking over as CEO. Cook will attend the &\#x27;Surprise and Shine&\#x27; screening but will stay out of the video. Apple intentionally arranged the handoff so Ternus becomes the public face for the foldable iPhone and future products, and featuring Cook in the event would weaken that effect.

telegram · zaihuapd · Sep 8, 05:03

**「Background」** Apple uses September keynote videos to announce major products, and the foldable iPhone is a new hardware category for the company. Tim Cook moved from CEO to executive chairman on September 1, making John Ternus the new CEO. This event is intended to showcase Ternus as the company&\#x27;s new product spokesperson.

**「Impact」** Apple&\#x27;s foldable iPhone debut will be attributed to new CEO John Ternus rather than Tim Cook, establishing Ternus as the public leader for Apple&\#x27;s hardware direction.

**Tags**: `#Apple`, `#Tim Cook`, `#foldable iPhone`, `#CEO transition`, `#hardware`

---

<a id="item-tech-news-12"></a>
### [ASML and TSMC Plan 12-Inch High NA EUV Photomasks by 2031–2033](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 7.0/10

ASML and TSMC announced cooperation on September 7 to move High NA EUV lithography from 6-inch to 12-inch photomasks. The change aims to increase equipment productivity, lower chip manufacturing costs, and reduce stitching limitations. A 12-inch photomask pilot line is planned for 2031, with associated systems targeted for advanced-node mass production in 2033. TSMC separately intends to start large-scale manufacturing with High NA EUV on advanced nodes from 2030.

telegram · zaihuapd · Sep 8, 06:55

**「Background」** Extreme ultraviolet \(EUV\) lithography currently uses 6-inch photomasks, and High NA EUV is the next-generation version for advanced nodes. ASML and TSMC say a transition to 12-inch photomasks could improve scanner productivity, reduce chipmaking costs, and remove stitching constraints, though initial High NA production will continue with 6-inch masks. Samsung expects to bring High NA EUV machines into high-volume manufacturing by 2028, while TSMC plans advanced-node mass production using High NA in 2030.

**「Impact」** This transition could improve High NA EUV productivity and lower chip costs for advanced-node manufacturers, but benefits are not expected until the early-to-mid 2030s.

<details><summary>References</summary>
<ul>
<li><a href="https://tbreak.com/tsmc-asml-12-inch-photomasks-euv/">12 - inch photomasks : TSMC and ASML plan for High NA EUV</a></li>
<li><a href="https://startupfortune.com/asml-tsmc-samsung-and-intel-agree-on-ai-chip-roadmap-through-2033/">ASML , TSMC , Samsung and Intel Agree on AI Chip... - Startup Fortune</a></li>

</ul>
</details>

**Tags**: `#semiconductor manufacturing`, `#EUV lithography`, `#ASML`, `#TSMC`, `#hardware`

---

<a id="item-tech-news-13"></a>
### [China Targets 9800 EFLOPS Intelligent Computing by 2030](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 7.0/10

China&\#x27;s Ministry of Industry and Information Technology \(MIIT\) has announced a plan to raise the country&\#x27;s intelligent computing power to 9,800 EFLOPS by 2030, with cumulative investment of 3.8 trillion yuan in information infrastructure from 2026 to 2030. The plan includes orderly deployment of intelligent computing clusters at the 10,000-card and 100,000-card scale or larger, and strengthens adaptation between infrastructure and domestically produced computing chips. As of the end of June this year, China&\#x27;s intelligent computing power reached 2,185 EFLOPS, up 177% year-on-year, meaning the 2030 target requires a more than fourfold increase from that level.

telegram · zaihuapd · Sep 8, 11:23

**「Background」** EFLOPS, or exaFLOPS, equals one quintillion floating-point operations per second and is commonly used to quantify large-scale AI compute capacity. MIIT is China&\#x27;s Ministry of Industry and Information Technology, which oversees industrial and information technology policy. The announced figures are policy targets for a five-year period, not current measured capacity.

**「Impact」** If implemented as announced, the plan commits 3.8 trillion yuan to information infrastructure through 2030 and establishes domestic chip compatibility as a requirement for large AI clusters, creating a multi-year demand signal for China&\#x27;s data-center and semiconductor ecosystem.

**Tags**: `#AI infrastructure`, `#China`, `#technology policy`, `#computing power`, `#semiconductors`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Crypto platforms lost over $3.63 billion to cyberattacks despite security audits](https://www.cnbc.com/2026/09/08/crypto-platforms-lost-billions-to-cyberattacks-many-even-after-audits.html) ⭐️ 7.0/10

Crypto platforms lost more than $3.63 billion to cyberattacks between January 2025 and July 2026, according to CoinGecko, even though most affected platforms had completed independent security audits.

rss · CNBC Finance · Sep 8, 08:16

**「Background」** CoinGecko said about 88% of the stolen funds and about 60% of affected platforms had undergone such audits, with most attacks targeting areas those checks do not typically cover.

**「Impact」** Crypto investors holding funds on audited platforms still face theft risk from these overlooked areas.

**Tags**: `#cryptocurrency`, `#cyberattacks`, `#security audits`, `#CoinGecko`, `#Bybit`

---

<a id="item-finance-news-2"></a>
### [Shanghai to fully reimburse maternity costs from October 1](https://mp.weixin.qq.com/s/jORA1qJsrSWa6VQaoM-b4Q) ⭐️ 7.0/10

Shanghai will fully reimburse covered maternity expenses starting October 1, including a 4,500-yuan prenatal allowance and full coverage of delivery costs for insured employees, residents, and eligible spouses.

telegram · zaihuapd · Sep 8, 13:26

**「Background」** The allowance is used first for 42 covered prenatal checkup items, then maternity insurance pays the rest; any remaining allowance can be claimed after a 42-day postpartum review.

**Tags**: `#maternity insurance`, `#healthcare policy`, `#Shanghai`, `#social security`, `#public finance`

---