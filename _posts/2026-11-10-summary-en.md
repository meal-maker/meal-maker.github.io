---
layout: default
title: "Horizon Summary: 2026-11-10 (EN)"
date: 2026-11-10
lang: en
---

> From 46 items, 14 important content pieces were selected

---

**Technology News**
1. [Show HN: Every satellite that passed over any place this week, and its photos](#item-tech-news-1) ⭐️ 8.0/10
2. [Google Gemini routes personal Drive files and emails to human annotators](#item-tech-news-2) ⭐️ 8.0/10
3. [Latent prediction beats reconstruction for tactile pretraining](#item-tech-news-3) ⭐️ 8.0/10
4. [SwarmEvolve: Latent KV-Cache Mixing Across Qwen Agents Accelerates Math Discovery](#item-tech-news-4) ⭐️ 8.0/10
5. [Google Launches New TPU 8tx and 8i Max to Challenge Nvidia](#item-tech-news-5) ⭐️ 8.0/10
6. [Anthropic Announces Claude Fable 5.2 and Mythos 5.2](#item-tech-news-6) ⭐️ 7.0/10
7. [E-means Outperforms k-means in One-Tenth the Epochs](#item-tech-news-7) ⭐️ 7.0/10
8. [2026 ML Conference Papers Added to Topic Pages with Benchmark Trends](#item-tech-news-8) ⭐️ 7.0/10
9. [ByteDance releases Seedream 5.5 with 100-round editing](#item-tech-news-9) ⭐️ 7.0/10
10. [EU Draft Digital Fairness Act Targets Addictive Design and Virtual Currency Pricing](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Nvidia board probes CEO Jensen Huang; prediction markets see low near-term exit odds](#item-finance-news-1) ⭐️ 8.0/10
2. [China&\#x27;s new energy vehicle exports rise 138.8% in first three quarters of 2026](#item-finance-news-2) ⭐️ 8.0/10
3. [World model AI funding cools sharply as capital concentrates in top teams](#item-finance-news-3) ⭐️ 7.0/10
4. [Apple Reportedly Saved $2.7 Billion in Taxes by Routing $50 Billion in Profit Through Singapore in 2026](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Show HN: Every satellite that passed over any place this week, and its photos](https://www.watched.earth/) ⭐️ 8.0/10

A browser-based tool at watched.earth finds every satellite that passed over a user-specified location in the last seven days and retrieves real imagery from those passes. It performs SGP4 propagation on the CelesTrak catalog locally in about half a second, and draws all ~17,000 tracked objects on the GPU while solving Kepler&\#x27;s equation every frame. The pass search was validated against brute force at poles, the antimeridian, and tiny swaths with zero missed passes. Imagery comes from Sentinel-2, Landsat, and NASA, and the tool only labels a pass as &\#x27;watched&\#x27; if a real image exists; it does not store location data. The author notes that Sentinel-2 timestamps are often 5–10 minutes off from the actual crossing time and invites feedback on additional data sources.

hackernews · a585gupt · Nov 9, 17:51 · [Discussion](https://news.ycombinator.com/item?id=50428907)

**「Background」** SGP4 is a standard mathematical model for predicting satellite positions from orbital elements, and CelesTrak maintains a public catalog of active and tracked objects. Solving Kepler&\#x27;s equation is a necessary step in converting orbital elements to a satellite&\#x27;s position at a given time. Sentinel-2 and Landsat are Earth-observation satellite programs that capture optical imagery, while NASA provides additional imagery sources.

**「Impact」** Users who need recent satellite imagery for a specific place—such as backpackers planning routes or geospatial professionals checking coverage—can use watched.earth to quickly identify and view the actual images captured in the past week, with a commenter noting it is easier and more comprehensive than Copernicus.

**「Community Discussion」** Comments are strongly positive, praising the tool&\#x27;s visual rendering, data integration, and execution quality; one geospatial professional called it &\#x27;really good&\#x27; for viewing exact images, and another said it is easier and more comprehensive than Copernicus for backpacking trip planning. No negative concerns or counterexamples were raised in the supplied comments.

**Tags**: `#satellite-imagery`, `#SGP4`, `#geospatial`, `#webgl`, `#earth-observation`

---

<a id="item-tech-news-2"></a>
### [Google Gemini routes personal Drive files and emails to human annotators](https://github.com/thisisme6598/gemini_files/) ⭐️ 8.0/10

A Hacker News discussion describes how consumer Google Gemini with connected apps may send personal Drive files and emails to human annotators. When users authorize connected apps such as Gmail, Gemini can load email content, and that data may then be reviewed by human annotators as part of normal Gemini data practices. Workspace Gemini and Workspace Intelligence are stated not to be subject to human review, creating a policy distinction between consumer and Workspace accounts. The exposure affects personal Drive files and emails, raising significant privacy concerns for consumer Gemini users.

hackernews · gf74918 · Nov 9, 18:24 · [Discussion](https://news.ycombinator.com/item?id=50429426)

**「Consumer Gemini vs. Workspace Gemini and human review」** Google Gemini is a consumer AI assistant that can integrate with connected apps such as Gmail and Google Drive, allowing it to read personal emails and files when answering user requests. For consumer accounts, Google&\#x27;s data practices permit human annotators to review some prompts and retrieved content to improve the models, while Workspace enterprise and education Gemini features explicitly state they are not subject to human review. This distinction is central to the privacy concern raised in the discussion.

**「Impact」** Consumer Gemini users who authorize connected apps risk having personal Drive and email content viewed by human annotators, while Workspace accounts are covered by a stated exemption from human review.

**「Community discussion」** Commenters emphasize that the human review applies specifically to consumer Gemini with connected apps, and that similar manual review exists across Gemini and NotebookLM; one user reported Gemini responses that seemed informed by their emails. Others express frustration at privacy erosion and note Google Photos data is used to infer interests, relationships, and locations for training generative AI.

**Tags**: `#privacy`, `#google`, `#gemini`, `#ai`, `#data-annotation`

---

<a id="item-tech-news-3"></a>
### [Latent prediction beats reconstruction for tactile pretraining](https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/) ⭐️ 8.0/10

A new self-supervised tactile model, LingBot-Touch, is trained JEPA-style to predict latent representations of masked contact rather than reconstruct raw tactile sensor signals. In tactile-to-video top-5 recall, it reaches 32.1% at 1K hours and 49.3% at 4K hours, while same-size MAE and VAE baselines stay below 9% and the VAE declines to 3.1%. The masking ratio warms up from 40% to 80% over 300 steps, and three sensor types \(magnetic, piezoresistive, visuotactile\) are fused into a shared Transformer using canonical fingertip coordinates with 5D RoPE. On 26 real robot tasks with four policies, frozen encoder features score highest in 89 of 104 policy-task combinations, and on a magnetic hand never seen in pretraining, LingBot-VLA improves from 57.21 to 75.04. The paper reports inference code and checkpoints are public.

reddit · r/MachineLearning · /u/Zealousideal-War7154 · Nov 9, 18:52

**「Background」** Tactile pretraining for dexterous manipulation often uses reconstruction objectives like masked autoencoding \(MAE\) or variational autoencoding \(VAE\), but raw tactile clips are sparse and dominated by near-zero background, so reconstruction loss can decrease without learning contact-relevant features. JEPA-style latent prediction avoids pixel-level reconstruction by predicting representations of masked input in latent space.

**「Impact」** Robotics practitioners using the public LingBot-Touch code and checkpoints can expect stronger frozen-feature performance than MAE/VAE baselines on dexterous manipulation, with the caveat that results cover 26 real robot tasks and three sensor types, and the Tiny model plateaus around 4K hours.

**Tags**: `#robotics`, `#self-supervised learning`, `#tactile sensing`, `#representation learning`, `#JEPA`

---

<a id="item-tech-news-4"></a>
### [SwarmEvolve: Latent KV-Cache Mixing Across Qwen Agents Accelerates Math Discovery](https://www.reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and/) ⭐️ 8.0/10

SwarmEvolve is a new framework for evolutionary math discovery and optimization that runs swarms of hundreds of latent-reasoning agents on Qwen3 8B, 14B, and 32B models, avoiding written chain-of-thought and instead passing KV caches between agents so ideas mix in latent space. Inspired by LatentMAS, this approach improves throughput and lets many small, differently focused agents explore the solution space in parallel; the authors report reaching in about 5 minutes scores that OpenEvolve, ShinkaEvolve, and CodeEvolve took more than 1 hour to achieve. The framework has been extended to Qwen3.5 and Muse models, which the post says show even better performance, and the 8B Qwen3 configuration matched the best known circle packing result. This work is self-reported in a paper at alphaxiv.org/abs/2611.08483, with code described as &quot;available soon&quot; on GitHub.

reddit · r/MachineLearning · /u/QileHQ · Nov 9, 15:30

**「Background」** SwarmEvolve builds on evolutionary program search, where a model iteratively writes, scores, and improves candidate programs, an approach popularized by DeepMind’s AlphaEvolve for mathematical discovery. Instead of decoding textual reasoning steps, the framework has agents reason in latent space and exchange information by passing KV caches within swarms of hundreds of low-cost open-weight Qwen agents. This design draws on recent latent multi-agent system work, such as LatentMAS, to avoid token-by-token text decoding and improve throughput.

**「Impact」** For researchers and developers using open evolutionary optimization frameworks, SwarmEvolve could cut wall-clock time from over an hour to about five minutes on Qwen3-class hardware if the reported results replicate.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.08483">[2611.08483] SwarmEvolve: Latent Agent Swarms for ...</a></li>

</ul>
</details>

**Tags**: `#latent reasoning`, `#agent swarms`, `#evolutionary optimization`, `#math discovery`, `#efficient inference`

---

<a id="item-tech-news-5"></a>
### [Google Launches New TPU 8tx and 8i Max to Challenge Nvidia](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 8.0/10

Google announced two new Tensor Processing Units: the TPU 8tx, aimed at government agencies and tightly regulated industries handling secure confidential data and designed to work with AMD chips, and the TPU 8i Max, targeted at ultra-long context window AI applications by packing two TPU chips into a single package for greater compute and memory. Google is breaking its previous two-year cadence for new processors and has expanded its TPU lineup this year. With customers including Apple, Meta, Oracle, and Anthropic, Google is positioning its TPUs as a significant alternative to Nvidia GPUs.

telegram · zaihuapd · Nov 9, 13:36

**「Context on Google&\#x27;s TPU generations」** Google&\#x27;s Tensor Processing Units \(TPUs\) are custom AI accelerator chips originally introduced as an alternative to Nvidia GPUs. The eighth-generation TPU family split into a training-focused TPU 8t and an inference-focused TPU 8i, and Google has been expanding the lineup to target specific workloads rather than offering a single general-purpose processor.

**「Impact」** Google Cloud customers in government or tightly regulated industries gain a secure inference option via TPU 8tx with AMD co-processing, and developers of long-context models get TPU 8i Max&\#x27;s dual-chip packaging for more compute and memory, strengthening Google&\#x27;s challenge to Nvidia in cloud AI.

**「Community Discussion」** Hacker News commenters link to a prior 16-point, 4-comment discussion and recommend Google&\#x27;s TPUSync post for understanding how open-source projects like Strata for Qwen models use TPUs. Some users ask why Google does not sell these chips and request watt-per-token or dollar-per-token comparisons with Nvidia equivalents, while another notes that Google Colab still only offers the older v6e-1 TPU.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/">Introducing TPU 8 tx and TPU 8 i Max</a></li>
<li><a href="https://www.linkedin.com/posts/john-flabetich_google-tpu-8i-for-inference-and-tpu-8t-for-activity-7454730299583922177-SItp">Google TPU 8 i for Inference and TPU 8 t for Training | LinkedIn</a></li>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/">Introducing TPU 8 tx and TPU 8 i Max</a></li>

</ul>
</details>

**Tags**: `#Google`, `#TPU`, `#AI hardware`, `#Nvidia`, `#Cloud computing`

---

<a id="item-tech-news-6"></a>
### [Anthropic Announces Claude Fable 5.2 and Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 7.0/10

Anthropic has announced Claude Fable 5.2 and Mythos 5.2, as submitted on Hacker News linking to anthropic.com. The release is described as drawing significant attention for its coding ability and changes to the model lineup. Specific technical details, benchmark comparisons, and compatibility constraints are not available in the provided source content.

hackernews · lairv · Nov 9, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50429068)

**「Background」** Claude Fable is Anthropic&\#x27;s flagship model line for demanding technical work, with Fable 5.2 succeeding Fable 5.1 and adding gains in coding, reasoning, and vision; Claude Mythos is a separate model line also updated to 5.2. The release is compared against Anthropic&\#x27;s Opus 5.5 and competitor models such as GPT-6 Astra and Gemini 4 Carbon, with benchmark scores reported for tasks like FrontierCode 2.0 and RoboDojo.

**「Pricing and performance improvement」** Claude Fable 5.2 is available at $8 per million input tokens and $40 per million output tokens, a 20% price reduction and up to 30% faster than Fable 5.1, lowering cost and latency for developers using it for coding, finance, and scientific workloads.

**「Community Discussion」** Early commenters report that Fable 5.2 feels close to Opus 5.5 for ordinary coding and that the model lineup is now more balanced, with one user citing a 36x speedup on a 600k-line Fortran codebase. Others question the benchmark comparisons in the announcement and speculate that Anthropic may be holding back a 5.5 release, while a separate comment mentions a claimed 1,000-agent formalization of Fermat’s Last Theorem in 30 hours.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=kwRxc8QPhrk">Fable 5 . 2 &amp; Mythos 5 . 2 Are OUT (Not 5.5... Here&#x27;s Why) - YouTube</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5.2">Claude Fable 5 . 2 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://madrobot.blog/2026/11/09/claude-fable-5-2-released-price-benchmarks/">Claude Fable 5.2 released: price, benchmarks and free resets</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#model release`, `#Anthropic`, `#large language models`, `#software engineering`

---

<a id="item-tech-news-7"></a>
### [E-means Outperforms k-means in One-Tenth the Epochs](https://e-means.github.io/) ⭐️ 7.0/10

E-means is a new clustering algorithm introduced as an alternative to k-means/Lloyd&\#x27;s algorithm, claiming similar or better results in one-tenth the epochs. The method reduces passes over large datasets, which matters for iterative clustering tasks. Community evaluations report a 146x GPU speedup when adapted to an IVF index and 2.5x faster bulk rebuilds for hierarchical balanced incremental clustering, though overall insertion times changed little. However, results are mixed: one user found it not better for relaxing an icosahedral equal-area mesh on a sphere, and commenters describe the update rule \(Sj = sj - a\(sj - Sj\)\) as an EM-like friction that keeps centroids within the convex hull.

hackernews · porridgeraisin · Nov 9, 18:45 · [Discussion](https://news.ycombinator.com/item?id=50429734)

**「Background: k-means and e-means」** E-means is a clustering algorithm introduced as an exponential moving average optimization procedure for k-means with mini-batch updates, leveraging modern deep learning machinery. It is designed to improve on Lloyd&\#x27;s k-means, which iteratively recomputes centroids over full dataset passes, by converging faster and to lower clustering loss. The work reports that e-means beats Lloyd k-means loss at 25 epochs in 1.4–2.6 epochs on embeddings datasets, translating to 10–45x GPU wall-clock speedups.

**「Impact」** Developers building or rebuilding IVF indexes and bulk clustering pipelines may see large speedups \(146x GPU for IVF, 2.5x bulk builds\), but incremental insertion workloads see little change and the benefit does not extend to all use cases.

**「Community Discussion」** Community reaction is positive but mixed: developers report 146x GPU speedups in IVF indexing and 2.5x faster bulk rebuilds, while a mesh-relaxation test found no improvement; commenters also relate the update rule to EM/simulated annealing and hope for scipy inclusion.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.09501">e-means: outperforming k-means (in one-tenth the epochs)</a></li>
<li><a href="https://arxiv.org/html/2611.09501v1">e-means: outperforming k-means (in one-tenth the epochs)</a></li>
<li><a href="https://openreview.net/pdf?id=pt14gnV3dl">E-MEANS OUTPERFORMING K MEANS IN ONE TENTH THE EPOCHS</a></li>

</ul>
</details>

**Tags**: `#clustering`, `#k-means`, `#machine-learning`, `#algorithms`, `#performance`

---

<a id="item-tech-news-8"></a>
### [2026 ML Conference Papers Added to Topic Pages with Benchmark Trends](https://www.reddit.com/r/MachineLearning/comments/1xs6494/followup_2026_papers_are_finally_in_the_topic/) ⭐️ 7.0/10

The author updated the atlas.scime.ai topic pages to include nearly all 2026 ICML, CVPR, and AAAI papers, 4,100 of 5,400 ICLR papers, and over half of NeurIPS 2026, expanding extraction to about 101,000 full texts and roughly one million “tried X, got Y” findings. They also created ICML, CVPR, and ICLR 2026 “newspapers” that compare this year with last; front pages are open and full editions require a free account. Among the highlighted shifts, LLM agent papers grew from 1.2% to 4.4% of ICML, multimodal LLM papers doubled at CVPR from 5.4% to 10.8%, ICLR papers on RL with verifiable rewards jumped from near zero to 110, and Qwen became the most-used base model across all three venues. In the compact/efficient Gaussian splatting topic, Mip-NeRF 360 PSNR rose from 28.01 to 30.1 this year while Deep Blending stayed around 30.4 and Tanks &amp; Temples did not move; reported baseline 3DGS results ranged from 16 to 27.7 PSNR. The numbers are AI-extracted and unchecked, and papers tend to over-report successful changes, so the resource should be used as a starting point, not a leaderboard.

reddit · r/MachineLearning · /u/latenticlabs · Nov 9, 22:39

**「Background」** The topic pages were originally built from ten years of ICML, NeurIPS, ICLR, CVPR, and AAAI papers, but their benchmark records and ablations stopped at 2025. The update pulls findings from full texts to aggregate benchmark results and ablation outcomes, helping researchers track state-of-the-art performance and trends. The associated newspapers compare conference activity year over year and rely on automatically extracted examples rather than manual curation.

**「Impact」** Researchers can now browse updated 2026 topic pages and newspapers to spot newer benchmark trends and conference shifts, but any specific number should be manually verified before use because the extraction is AI-generated, unchecked, and biased by papers over-reporting improvements.

**Tags**: `#machine learning`, `#benchmarking`, `#research tools`, `#computer vision`, `#academic papers`

---

<a id="item-tech-news-9"></a>
### [ByteDance releases Seedream 5.5 with 100-round editing](https://seed.bytedance.com/zh/blog/%E7%94%9F%E6%88%90%E6%9B%B4%E7%9C%9F%E5%AE%9E-%E7%99%BE%E8%BD%AE%E7%BC%96%E8%BE%91%E6%9B%B4%E7%A8%B3%E5%AE%9A-seedream-5-5-%E5%8F%91%E5%B8%83) ⭐️ 7.0/10

ByteDance has released Seedream 5.5, an image creation model that supports up to 100 consecutive rounds of editing on the same work and can natively generate assets with transparent channels. The model also improves image realism and text rendering. ByteDance claims that in evaluations, the model&\#x27;s usability in film and office scenarios reached more than double that of the previous version. The model is being rolled out gradually to Jimeng, Doubao, Doubao Work, and Volcano Ark. These claims have not been independently verified.

telegram · zaihuapd · Nov 9, 08:34

**「Background」** ByteDance&\#x27;s Seed team develops the Seedream family of image generation and editing models; Seedream 5.5 follows Seedream 5.0 Pro \(released July 2026\) and an October 2026 preview. The update introduces native RGBA transparency output and multi-round consistent editing, addressing workflows that need layered assets and iterative revisions.

**「Impact」** Creators and developers using ByteDance&\#x27;s platforms can now perform up to 100 iterative edits and produce native transparent assets, but the doubled usability figure is based on ByteDance&\#x27;s own evaluation and not yet independently confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5">Seed News - ByteDance Seed Team</a></li>
<li><a href="https://seedream6.dev/">Seedream 6: The Next ByteDance Image Model</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#image generation`, `#ByteDance`, `#Seedream`, `#AI models`

---

<a id="item-tech-news-10"></a>
### [EU Draft Digital Fairness Act Targets Addictive Design and Virtual Currency Pricing](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

A leaked draft of the European Union’s Digital Fairness Act proposes restricting addictive design and subscription traps, requiring digital businesses to let users disable features such as autoplay and continuous-use rewards that induce compulsive or excessive use. For online subscriptions, it would mandate cancellation buttons, renewal reminders, human customer service, and explicit consent before a free trial converts to paid service. It would ban paid loot boxes, pay-to-win mechanics, and profiling ads aimed at minors, and require game virtual currencies to display their real-money value. The European Commission is scheduled to present the bill on November 11, alongside a reform of the consumer protection cooperation framework, with fines of up to 6% of global turnover for violations. Both proposals need approval from the European Parliament and EU member state governments to take effect.

telegram · zaihuapd · Nov 9, 16:42

**「Background」** The EU’s existing Digital Services Act, in force since 2024, already prohibits online platforms from using deceptive or manipulative interface designs under Article 25. The proposed Digital Fairness Act is expected to go further by introducing outright bans on design features considered addictive or harmful, particularly for children, and by requiring in-game currencies to display real-money values. A formal proposal is scheduled for 11 November, according to leaked drafts.

**「Impact」** If adopted, online platforms and game publishers in the EU would need to redesign engagement features, subscription flows, and virtual currency displays, and could face fines up to 6% of global turnover for non-compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.euronews.com/2026/11/09/eu-to-blacklist-ten-manipulative-online-design-traps-leaked-draft-shows">EU to blacklist ten manipulative online design &#x27;traps&#x27;, leaked draft s...</a></li>
<li><a href="https://cryptobriefing.com/eu-meta-investigation-addictive-design-children/">EU escalates investigation into Meta over addictive design targeting...</a></li>
<li><a href="https://medium.com/design-bootcamp/the-internet-is-lying-to-you-and-its-by-design-06296a598654">The internet is lying to you. And it’s by design | Medium</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#digital fairness`, `#consumer protection`, `#video games`, `#subscription services`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia board probes CEO Jensen Huang; prediction markets see low near-term exit odds](https://www.cnbc.com/2026/11/09/jensen-huang-nvidia-exit-prediction-markets.html) ⭐️ 8.0/10

Nvidia&\#x27;s board is investigating CEO Jensen Huang after he admitted an affair with a woman who, according to The New York Times, U.S. intelligence officials say is a spy for China&\#x27;s Ministry of State Security. Kalshi traders price a 17% chance he is gone by 2027, and Nvidia shares fell more than 5% Monday.

rss · CNBC Finance · Nov 9, 18:46

**「Background」** The board cited reports that Huang had been targeted by a &quot;foreign intelligence effort.&quot;

**Tags**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#prediction markets`, `#national security`

---

<a id="item-finance-news-2"></a>
### [China&\#x27;s new energy vehicle exports rise 138.8% in first three quarters of 2026](https://finance.sina.com.cn/tech/roll/2026-10-26/doc-iniwpfnc2438186.shtml) ⭐️ 8.0/10

China&\#x27;s new energy passenger vehicle exports rose 138.8% year over year to 3.887 million units in the first three quarters of 2026, while domestic retail fell 12.8% to 7.758 million units.

telegram · zaihuapd · Nov 10, 02:56

**「Background」** The article attributes the domestic retail decline to purchase subsidies, purchase tax incentive changes, and a high sales base in the prior year.

**Tags**: `#new energy vehicles`, `#exports`, `#auto industry`, `#China economy`, `#economic data`

---

<a id="item-finance-news-3"></a>
### [World model AI funding cools sharply as capital concentrates in top teams](https://mp.weixin.qq.com/s/8U3Lwbq2q0klDUTIy7LWNQ) ⭐️ 7.0/10

Funding for world model AI startups has cooled sharply, with only five primary-market financing deals in physical AI and world model in October, according to incomplete statistics from Chinese venture-capital data tracker Cailian Press, and capital is concentrating in a few teams. AMD is proposing to acquire World Labs for $8.2 billion, while Amazon is in talks to buy Decart for about $7 billion.

telegram · zaihuapd · Nov 9, 07:10

**「Background」** World model startups attracted heavy investment in 2026, with more than 100 financing deals in physical AI and world models, but activity has slowed sharply: October recorded only five deals, and investors now favor teams with top university research backgrounds and published models. The trend is punctuated by AMD&\#x27;s announced all-stock acquisition of World Labs, founded by Fei-Fei Li, for about $8.2 billion and reported talks by Amazon to buy Decart for about $7 billion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huxiu.com/article/4894452.html">AMD 官宣82亿美元收购World Labs：李飞飞加入，苏姿丰押注物理AI</a></li>
<li><a href="https://agihunt.info/p/1a1bfda7de0ce166ab267dfd4d3">世界模型融资骤冷：10 月仅 5 起，头部 VC 只剩四五… · AGI Hunt</a></li>

</ul>
</details>

**Tags**: `#世界模型`, `#AI融资`, `#风险投资`, `#并购`, `#科技产业`

---

<a id="item-finance-news-4"></a>
### [Apple Reportedly Saved $2.7 Billion in Taxes by Routing $50 Billion in Profit Through Singapore in 2026](https://appleinsider.com/articles/26/11/08/apple-saves-27b-in-taxes-by-funnelling-finances-through-singapore) ⭐️ 7.0/10

AppleInsider reported that Apple moved about $50 billion in profit through Singapore in 2026, saving $2.7 billion in taxes, more than the $2.6 billion saved through Ireland.

telegram · zaihuapd · Nov 9, 09:19

**「Background」** Apple has long routed international profits through low-tax jurisdictions; in 2025 it paid $17 billion to Ireland after a tax dispute, and Singapore has now become a larger source of tax savings than Ireland.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rbc.ru/business/09/11/2026/6af140da3c02e1f36c5b688e">FT: Apple сэкономила 2,7 млрд долларов на налогах, направив...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#corporate tax`, `#profit shifting`, `#Singapore`, `#tax avoidance`

---