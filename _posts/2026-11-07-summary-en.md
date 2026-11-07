---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 42 items, 16 important content pieces were selected

---

**Technology News**
1. [Firecracker VM Escape: PwnEscape Part 2](#item-tech-news-1) ⭐️ 8.0/10
2. [Baidu Open-Sources Wenxin 5.5 Flash Base Foundation Model](#item-tech-news-2) ⭐️ 8.0/10
3. [YMTC Targets Up to 70% Domestic Tools at New Wuhan Fab](#item-tech-news-3) ⭐️ 8.0/10
4. [Libghostty 1.0 Stable Embeddable Terminal Library Released](#item-tech-news-4) ⭐️ 7.0/10
5. [AI Is Dramatically Accelerating AI Research](#item-tech-news-5) ⭐️ 7.0/10
6. [Anthropic IPO buyers see valuation as low as $1.1T](#item-tech-news-6) ⭐️ 7.0/10
7. [Boson AI Higgs Realtime Duplex: 45B MoE Full-Duplex Model](#item-tech-news-7) ⭐️ 7.0/10
8. [Moonshot AI Reported Seeking 8,000 Nvidia Blackwell GPUs in Europe](#item-tech-news-8) ⭐️ 7.0/10
9. [US Democrats Plan Probes of Apple, Meta, Musk Firms](#item-tech-news-9) ⭐️ 7.0/10
10. [EU Charges TikTok Over &\#x27;Rabbit Hole&\#x27; Effects in Recommendation Algorithm](#item-tech-news-10) ⭐️ 7.0/10
11. [Taobao MNN Team Open-Sources 0.3B Mobile Model](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [CoreWeave bond yield tops 16% as AI data-center credit stress rises](#item-finance-news-1) ⭐️ 8.0/10
2. [Anthropic to Start IPO Roadshow Next Week](#item-finance-news-2) ⭐️ 8.0/10
3. [Fed&\#x27;s Daly Says More Rate Hikes Likely as Wages Trail 3.7% Inflation](#item-finance-news-3) ⭐️ 7.0/10
4. [Premarket movers: Lam Research up on buyback, DraftKings down on loss](#item-finance-news-4) ⭐️ 7.0/10
5. [Nasdaq enters correction territory after 5% drop amid election-driven tech selloff](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Firecracker VM Escape: PwnEscape Part 2](https://pwn.ai/blog/firecracker-escape) ⭐️ 8.0/10

The article is a follow-up describing how to exploit the PwnEscape vulnerability in practice on Firecracker VMs; it is not a new vulnerability, as PwnEscape was disclosed several weeks earlier. The demonstrated configuration omitted Firecracker&\#x27;s jailer, leaving the VMM process with more privileges than production deployments, which normally drop privileges and restrict the process using namespaces and seccomp. The author notes that a deployment using these containment controls requires a separate assessment of the privileges and resources available after a VMM compromise. Because Firecracker is widely used to isolate tenant workloads in cloud and serverless environments, practical exploit details are important for security teams.

hackernews · SerCe · Nov 6, 19:33 · [Discussion](https://news.ycombinator.com/item?id=50397219)

**「Background」** Firecracker is a lightweight virtual machine monitor used for serverless and container workloads, relying on Linux&\#x27;s KVM and virtio drivers. PwnEscape \(CVE-2026-99999\) is a recently patched Linux kernel vulnerability that allows a malicious guest to write into host kernel memory and potentially execute code as root on the host; the initial disclosure demonstrated the escape on KVM and Firecracker systems but withheld full exploitation details for a follow-up. The exploit described in this article builds on that vulnerability through virtio-net checksum offload metadata passed between guest and host driver interfaces, with the test environment lacking Firecracker&\#x27;s jailer-based isolation \(namespaces, seccomp, privilege dropping\) that would otherwise constrain a compromised VMM.

**「Practical escape risk for unjailed Firecracker hosts」** The PwnEscape exploit provides a practical guest-to-host escape and root access on Firecracker microVMs that are run without the jailer, namespaces, and seccomp restrictions, leaving deployments that omit these controls exposed to host takeover by any compromised guest workload. Configurations with full production containment require a separate assessment, so the impact on hardened deployments is less certain.

**「Community Discussion」** Comments highlight that the article is a duplicate and not a new vulnerability; one commenter offers a public ClickBench playground as a test service for the escape, and another suggests the Nova Microhypervisor approach as an alternative. A further commenter wished for more detail on the containment assessment for jailed deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50397219">Firecracker VM Escape : PwnEscape Part 2 | Hacker News</a></li>
<li><a href="https://almalinux.org/blog/2026-10-16-pwnescape-cve-2026-99999/">PwnEscape (CVE-2026-99999): Patched kernels... | AlmaLinux OS</a></li>
<li><a href="https://socprime.com/blog/cve-2026-99999-analysis/">CVE-2026-99999: Critical Linux PwnEscape Flaw</a></li>
<li><a href="https://agihunt.info/en/p/1a1ac966bb1df42ba5f2854594d">Firecracker VM escape disclosed: researchers… · AGI Hunt</a></li>

</ul>
</details>

**Tags**: `#firecracker`, `#vm-escape`, `#cloud-security`, `#virtualization`, `#exploit-development`

---

<a id="item-tech-news-2"></a>
### [Baidu Open-Sources Wenxin 5.5 Flash Base Foundation Model](https://www.news.cn/info/20261105/f3bbdb6854f5441ca9fb34062f213875/c.html) ⭐️ 8.0/10

Baidu officially open-sourced its latest foundation model, Wenxin 5.5 Flash Base. The model uses a Mixture-of-Experts \(MoE\) architecture with 280 billion total parameters, activating 14 billion parameters per token. It was pre-trained on 33.5 trillion tokens with a pre-training context length of up to 128K, and it supports up to 1 million tokens of context during fine-tuning and inference. The release focuses on efficiency through systematic optimizations in attention mechanisms, expert routing, and training objectives. This matters to AI and machine learning developers because it makes a very large long-context MoE model openly available.

telegram · zaihuapd · Nov 6, 05:41

**「Background」** Mixture-of-Experts \(MoE\) models use a larger total parameter count but activate only a subset per token, improving efficiency relative to dense models of similar capacity. Baidu&\#x27;s ERNIE 5.5 Flash Base follows this design with 280B total parameters and 14B activated per token, pre-trained on 33.5 trillion tokens with a 128K training context and 1M-token fine-tuning and inference support.

**「Impact」** Because only 14 billion of the 280 billion parameters are active per token, the open model enables lower per-token compute for long-context inference than a dense 280B model would.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/baidu/ERNIE-5.5-Flash-Base">baidu/ERNIE- 5 . 5 - Flash - Base · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#MoE`, `#foundation-model`, `#long-context`, `#Baidu`

---

<a id="item-tech-news-3"></a>
### [YMTC Targets Up to 70% Domestic Tools at New Wuhan Fab](https://www.reuters.com/world/china/chinas-top-flash-memory-chipmaker-targets-more-homegrown-tools-new-factory-2026-11-06/) ⭐️ 8.0/10

China&\#x27;s top flash memory chipmaker YMTC plans to build a fourth Wuhan fab with construction starting in 2027, aiming to raise domestic equipment procurement to at least 60% and up to 70%, up from the third fab&\#x27;s current more-than-50% level. The new facility will produce advanced NAND flash with more than 300 layers, primarily for data center and AI storage demand. US export controls are pushing the company toward local tools, with cleaning, polishing, and etching equipment expected to see the largest increases, while lithography and inspection equipment remain dependent on overseas suppliers. YMTC&\#x27;s share of China&\#x27;s NAND market has reached 38.5%, surpassing Samsung, and once all planned new fabs are fully operational, overall capacity is expected to double.

telegram · zaihuapd · Nov 6, 08:34

**「Background」** YMTC \(Yangtze Memory Technologies Co., Ltd.\) is China&\#x27;s leading producer of 3D NAND flash memory, a key component in smartphones, SSDs, and data center storage. US export controls on advanced semiconductor manufacturing equipment have prompted Chinese chipmakers to substitute domestic tools where possible, though tools such as lithography and inspection are harder to replace. Domestic equipment share is an indicator of supply-chain localization for process steps like etching, cleaning, and polishing.

**「Impact」** If the stated targets are met, this plan would expand YMTC&\#x27;s China-based NAND capacity and demand for domestic tools, while advanced lithography and inspection remain dependent on overseas suppliers.

**Tags**: `#NAND flash`, `#semiconductors`, `#YMTC`, `#AI infrastructure`, `#supply chain`

---

<a id="item-tech-news-4"></a>
### [Libghostty 1.0 Stable Embeddable Terminal Library Released](https://mitchellh.com/writing/libghostty-1-0) ⭐️ 7.0/10

Libghostty 1.0 has been released as a stable embeddable terminal emulator library for software projects. The library provides a stable API for embedding terminal emulation, targeting developers who build terminal-based applications and want to avoid implementing terminal emulation from scratch. Community feedback indicates the library is already being used in projects such as Ghostel for Emacs, experiments with Android terminals, and custom terminal applications. Several contributors describe it as saving significant development effort and working reliably in practice.

hackernews · mfiguiere · Nov 6, 23:30 · [Discussion](https://news.ycombinator.com/item?id=50399933)

**「What is Libghostty?」** Ghostty is a terminal emulator created by Mitchell Hashimoto. Its terminal emulation core was originally available only as a Zig module without a stable C API, but it has now been extracted into libghostty. The 1.0 release provides a portable, high-performance C library with a stable ABI that is already adopted by projects such as JetBrains, Neovim, and Vercel.

**「Impact」** Developers building terminal-adjacent applications now have a stable, embeddable terminal emulation API, with reported adoption in Emacs, Android, and custom terminal projects.

**「Community Discussion」** Commenters broadly praise the release and its contributors, with several confirming personal use in Emacs, Android, and custom terminal projects; no critical concerns are raised in the supplied comments.

<details><summary>References</summary>
<ul>
<li><a href="https://mitchellh.com/writing/libghostty-1-0">Libghostty 1.0 – Mitchell Hashimoto</a></li>
<li><a href="https://news.lavx.hu/article/libghostty-1-0-stabilizes-the-terminal-library-behind-ghostty">Libghostty 1.0 stabilizes the terminal library behind Ghostty</a></li>
<li><a href="https://runtimewire.com/article/libghostty-1-0-mitchell-hashimoto-stable-c-abi">Libghostty 1.0 gives developers a stable terminal engine to embed</a></li>

</ul>
</details>

**Tags**: `#terminal`, `#library`, `#open source`, `#developer tools`, `#software engineering`

---

<a id="item-tech-news-5"></a>
### [AI Is Dramatically Accelerating AI Research](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) ⭐️ 7.0/10

The essay “AI is dramatically accelerating AI research” by yurivish argues that AI tools are greatly speeding up the practice of AI research itself. A Hacker News discussion largely agrees that LLMs accelerate ML research tasks such as model architecture, training strategy, and software experimentation, with one commenter citing up to a 10x speedup in compute-environment work. However, several commenters caution that this does not imply superintelligence or exponential capability growth, noting that benchmark measurements can be self-reinforcing and that massive capital investment confounds progress. The debate highlights that acceleration is concentrated in measurable tasks and may not translate to fundamental breakthroughs or dramatic world-changing progress.

hackernews · yurivish · Nov 6, 20:27 · [Discussion](https://news.ycombinator.com/item?id=50397994)

**「Background: AI feedback loops in research」** The essay comes from Planned Obsolescence, a blog about AI futurism and alignment written primarily by Ajeya Cotra and Kelsey Piper. Its central claim is that current AI systems are accelerating AI research by helping design the next generation of ML models, potentially creating a feedback loop of ever-faster progress. The author treats this acceleration as a strong concrete indicator of extreme capabilities in the very near term, and notes that an earlier version of Anthropic&\#x27;s Responsible Scaling Policy \(May 2025\) used dramatically accelerated AI progress as its highest named risk threshold.

**「Community Discussion」** Commenters generally agree that LLMs make ML research faster, with one practitioner reporting up to 10x faster experiments in compute environments, but disagree on implications. Some warn that benchmark-based measurements may be self-reinforcing and confounded by capital investment, while others note that personal speedups do not necessarily change world impact faster.

<details><summary>References</summary>
<ul>
<li><a href="https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai">AI is dramatically accelerating AI research right now</a></li>
<li><a href="https://planned-obsolescence.ghost.io/">Planned Obsolescence</a></li>
<li><a href="https://forum.effectivealtruism.org/s/6m838NofGdfSuGvBJ">Planned Obsolescence - EA Forum</a></li>

</ul>
</details>

**Tags**: `#AI research`, `#LLMs`, `#benchmarks`, `#machine learning`, `#research acceleration`

---

<a id="item-tech-news-6"></a>
### [Anthropic IPO buyers see valuation as low as $1.1T](https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout) ⭐️ 7.0/10

Anthropic&\#x27;s IPO valuation expectations are dropping amid an AI market downturn, with buyers seeing valuations as low as $1.1 trillion. Major investors had discussed valuations around $1.3 trillion, according to the report. Community discussion highlights additional pressures: local open models like Qwen3.8-Flash-Next are reducing paid subscription usage, and users describe subscription pricing as financially unsustainable.

hackernews · dgellow · Nov 6, 16:54 · [Discussion](https://news.ycombinator.com/item?id=50394906)

**「Background」** Anthropic is an AI lab known for its Claude models and Claude Code developer tools, and it has been preparing an initial public offering \(IPO\). Before the recent AI stock selloff, expectations were much higher; a leaked draft filing in September suggested a valuation around $2 trillion, but as formal IPO marketing approaches, potential buyers are now discussing a range of roughly $1.2–1.3 trillion, with some considering as low as $1.1 trillion. Prediction markets have also cut the odds of an IPO before December 1 from about 80% to near 50%.

**「IPO valuation pressure」** Anthropic&\#x27;s expected IPO valuation has been marked down to as low as $1.1 trillion as the AI market rout weakens investor appetite, reducing the capital it can likely raise in its listing.

**「Community Discussion」** Commenters express concern that capable local open models are eroding paid Claude subscriptions, with one user reporting an 82% drop in quota usage after running Qwen3.8-Flash-Next locally. Others question the IPO&\#x27;s viability due to lockup schedules and political risks, and there is disagreement about whether local LLMs can match Claude Code without high-end hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout">Anthropic IPO Valuation Estimates Fall as AI Stock Selloff Hits Market</a></li>
<li><a href="https://finance.yahoo.com/technology/article/anthropics-ipo-valuation-could-plunge-to-near-1-trillion-amid-market-turmoil-153332732.html">Anthropic &#x27;s IPO valuation could plunge to near $ 1 trillion amid...</a></li>
<li><a href="https://decrypt.co/382716/anthropic-ipo-valuation-could-fall-to-1-trillion-after-ai-stock-rout-report">Anthropic IPO Valuation Could Be Slashed in Half to $1T After AI ...</a></li>
<li><a href="https://www.fastcompany.com/91629897/anthropics-ipo-filing-is-the-start-of-the-put-up-or-shut-up-era-of-ai">Anthropic ’s IPO filing is the start of the &#x27;put up or shut... - Fast Compan...</a></li>
<li><a href="https://www.linkedin.com/pulse/anthropic-ipo-2026-explained-from-965-billion-possible-2-pvgkc">Anthropic IPO 2026 Explained, From $965 Billion to a Possible...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#IPO`, `#valuation`, `#tech-industry`

---

<a id="item-tech-news-7"></a>
### [Boson AI Higgs Realtime Duplex: 45B MoE Full-Duplex Model](https://www.reddit.com/r/MachineLearning/comments/1xpn5pv/higgs_realtime_duplex_a_45b_moe_fullduplex_model/) ⭐️ 7.0/10

Boson AI announced Higgs Realtime Duplex, a 45B mixture-of-experts model that processes audio, video, and text in full-duplex 160 ms chunks, allowing simultaneous listening, speaking, and background thinking or tool use. Everything is tokenized into a unified stream: audio input at 1 token per 160 ms chunk, audio output at 2 tokens, video frames as roughly 12 tokens every six chunks, and silence represented as chunks to decide backchanneling, interruptions, or staying quiet. The model can start speaking before tool results are complete and delegates harder problems to a larger backend model with shared context, unlike turn-based models that wait for end of turn or Thinking Machines&\#x27; interaction models that route all reasoning and tool use to a background model. Trained via continued pretraining on about 2T text, audio, and video tokens plus multi-teacher on-policy distillation and simulated self-improvement, it supports zero-shot voice and face cloning at deployment without fine-tuning. Reported benchmarks place it near or behind OpenAI&\#x27;s best settings on several metrics, with turn-taking on Full-Duplex-Bench as the weakest area; weights are not open and the Duplex API is waitlisted.

reddit · r/MachineLearning · /u/Cali\_Cobarde · Nov 6, 20:23

**「Background」** Full-duplex voice models can listen and speak at the same time, unlike turn-based systems that wait for the end of a user&\#x27;s turn before thinking and responding. Mixture-of-experts models activate only a subset of parameters per token, allowing larger capacity with lower per-token compute; this 45B model uses chunked streaming tokens to coordinate audio, video, text, and background agent actions.

**「Impact」** For developers, the model is not open-weight and the Duplex API is waitlisted, so the announced full-duplex behavior and benchmark results cannot yet be independently tested; Boson AI&\#x27;s earlier turn-based Higgs Realtime is available now.

**Tags**: `#realtime-ai`, `#multimodal`, `#voice-ai`, `#mixture-of-experts`, `#agentic-ai`

---

<a id="item-tech-news-8"></a>
### [Moonshot AI Reported Seeking 8,000 Nvidia Blackwell GPUs in Europe](https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html) ⭐️ 7.0/10

Moonshot AI is reportedly in talks to rent more than 8,000 Nvidia Blackwell GPUs from European neocloud data centers, primarily for inference and also for training. The move is described as a workaround for U.S. export controls that ban Blackwell imports into China; using overseas cloud services remotely is seen as a bypass route. Moonshot AI would need to pay 30% to 50% more in prepayment than non-Chinese buyers, according to one proposal. The White House said in July that the company had obtained Blackwell chips through facilities in Thailand. CNBC reported the negotiations based on informed sources.

telegram · zaihuapd · Nov 6, 05:02

**「Background」** US export controls prohibit importing Nvidia Blackwell GPUs into China, prompting some Chinese AI companies to seek remote computing capacity overseas. In this context, &\#x27;neoclouds&\#x27; are emerging cloud providers that can lease data center GPU capacity; Moonshot AI is exploring such leases in Europe. The White House stated in July that Moonshot had already obtained Blackwell chips via facilities in Thailand.

**「Impact」** If completed, the deal would give Moonshot AI Blackwell-class compute for AI inference and training outside direct export restrictions, at a 30–50% prepayment premium.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html">China&#x27;s Moonshot AI sought Nvidia chip access in Europe amid ...</a></li>
<li><a href="https://www.cnbc.com/2026/08/19/china-ai-nvidia-chips-us-export-controls.html">China AI firms tap Nvidia power overseas as U.S ... - CNBC</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Nvidia`, `#export controls`, `#Moonshot AI`, `#cloud computing`

---

<a id="item-tech-news-9"></a>
### [US Democrats Plan Probes of Apple, Meta, Musk Firms](https://www.washingtonpost.com/technology/2026/11/06/after-courting-trump-corporate-america-faces-democratic-reckoning/) ⭐️ 7.0/10

US Democrats are preparing a wave of congressional investigations into major technology companies after winning House and Senate majorities in the midterm elections. Early targets include Apple, Meta, Alphabet/Google, Amazon, Microsoft, Nvidia, Oracle, OpenAI, Anthropic, and Musk-owned xAI, X, SpaceX, and Tesla. Planned inquiries cover Apple&\#x27;s removal of an ICE tracking app under Trump administration pressure, campaign donations to Trump&\#x27;s White House ballroom project, data center non-disclosure agreements and electricity/water use, and AI safety incident reporting within 48 hours for Google, OpenAI, and Anthropic. Musk&\#x27;s companies could also face scrutiny over DOGE-era layoffs, contract cancellations and data use, federal contracts and conflicts of interest, and preservation of Trump&\#x27;s official conversations with Grok; Nvidia faces a Republican request for a closed-door briefing with CEO Jensen Huang on November 18 about Alice Huang interactions and anti-espionage safeguards. Most measures are still at the stage of document requests, prepared subpoenas, and hearings.

telegram · zaihuapd · Nov 6, 10:37

**「Background」** These moves follow the midterm elections in which Democrats won control of both chambers of Congress, giving the party authority over congressional oversight committees. Congressional investigations can compel companies to produce documents and testimony through subpoenas, and tech firms have faced growing scrutiny over political spending, secretive data center agreements, AI safety reporting, and federal contracting.

**「Impact」** If the planned subpoenas and hearings move forward, the targeted companies could be required to disclose campaign donation records, data center NDAs, AI safety incidents, and federal contract information, with AI labs potentially bound by a 48-hour congressional notification requirement.

**Tags**: `#tech policy`, `#AI regulation`, `#congressional investigations`, `#big tech`, `#Musk`

---

<a id="item-tech-news-10"></a>
### [EU Charges TikTok Over &\#x27;Rabbit Hole&\#x27; Effects in Recommendation Algorithm](https://www.cnbc.com/2026/11/06/eu-charges-tiktok-harmful-algorithmic-rabbit-hole-effects.html) ⭐️ 7.0/10

The European Commission has charged TikTok with violating the Digital Services Act, saying its recommendation algorithm creates &\#x27;rabbit hole&\#x27; effects. The Commission states TikTok has not taken effective measures to mitigate the risk and demands changes to the &\#x27;For You&\#x27; algorithm so it relies more on users&\#x27; explicit preferences, improves control options, and undergoes regular testing. If the issues remain unresolved, ByteDance could face fines of up to 6% of its global annual revenue next year. The EU says continuous delivery of similar content may affect mental health, and this charge is part of a broader investigation.

telegram · zaihuapd · Nov 6, 14:03

**「Digital Services Act and rabbit-hole effects」** The Digital Services Act \(DSA\) requires large online platforms to address systemic risks, including mental-health harms and the spread of harmful or illegal content. A “rabbit hole” effect refers to recommendation algorithms repeatedly surfacing similar content, potentially drawing users into narrow or extreme viewing loops. The EU Commission has preliminarily found that TikTok’s design features—including infinite scrolling and autoplay—breach the DSA by exploiting user psychology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/11/06/eu-charges-tiktok-harmful-algorithmic-rabbit-hole-effects.html">EU charges TikTok over harmful algorithmic &#x27; rabbit hole &#x27; effects</a></li>
<li><a href="https://reclaimthenet.org/eu-commission-tiktok-algorithm-digital-services-act">European Commission Says TikTok Recommendation Algorithm ...</a></li>
<li><a href="https://www.tradingview.com/news/invezz:5852b16a1094b:0-europe-bulletin-ftse-100-surges-eu-charges-tiktok-stellantis-stock-plunges/">Europe bulletin: FTSE 100 surges, EU charges TikTok , Stellantis...</a></li>

</ul>
</details>

**Tags**: `#TikTok`, `#recommendation algorithms`, `#Digital Services Act`, `#tech regulation`, `#EU`

---

<a id="item-tech-news-11"></a>
### [Taobao MNN Team Open-Sources 0.3B Mobile Model](https://www.ithome.com/1/023/212.htm) ⭐️ 7.0/10

Taobao&\#x27;s MNN team open-sourced MNN-Pocket-0.3B, a roughly 0.3B-parameter on-device model, on November 6. It runs fully offline on iPhone 18 Pro with average decoding around 350 tokens per second and an INT4 deployment file of only 173 MB. The team targeted peak memory below 300 MB and decoding over 200 tokens per second, using a 28-layer architecture and reducing the vocabulary from 151K to 64K. They released multiple versions covering pretraining, post-training, and on-device deployment. This provides mobile developers with an efficient small model for edge inference.

telegram · zaihuapd · Nov 6, 15:13

**「Background」** MNN is Alibaba&\#x27;s lightweight on-device inference engine, and the Taobao MNN team has released MNN-Pocket-0.3B as part of a trend toward running small language models entirely on mobile devices. The model uses INT4 quantization to shrink the deployment file to 173 MB, and it adopts a reduced 64K vocabulary with a 28-layer transformer structure to balance speed, memory, and task capability. This approach targets constraints such as sub-300 MB peak memory and offline operation on phones like the iPhone 18 Pro.

**「Impact」** Mobile app developers can integrate this model for fully offline on-device inference with peak memory below 300 MB and about 350 tokens per second decoding on iPhone 18 Pro.

<details><summary>References</summary>
<ul>
<li><a href="https://tool.lu/article/88c/detail">淘 宝 MNN 团 队 开源 0 . 3 B 手机 模 型 ，iPhone 18 Pro上离线跑出350 token/s</a></li>
<li><a href="https://github.com/alibaba/MNN/blob/master/README_CN.md">MNN /README_CN.md at master · alibaba/ MNN · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#edge AI`, `#open source`, `#model optimization`, `#mobile`

---

## Financial News

<a id="item-finance-news-1"></a>
### [CoreWeave bond yield tops 16% as AI data-center credit stress rises](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) ⭐️ 8.0/10

CoreWeave&\#x27;s 2032 bond with a 9.625% coupon now yields more than 16%, while its five-year credit default swaps jumped above 1,289 basis points on Thursday before easing to about 1,155 on Friday, according to CNBC.

rss · CNBC Finance · Nov 6, 17:09

**「Background」** The rise reflects investor concern that Democratic election wins could lead to moratoriums on data-center construction in Texas, Ohio, and Georgia, which hold much of the planned U.S. capacity.

**「Impact」** Higher credit spreads may raise borrowing costs for data-center builders and even large issuers such as Nvidia, Broadcom, and Amazon, while analysts warn possible project delays could reduce future AI debt funding.

**Tags**: `#AI`, `#credit markets`, `#data centers`, `#bonds`, `#credit default swaps`

---

<a id="item-finance-news-2"></a>
### [Anthropic to Start IPO Roadshow Next Week](https://www.theinformation.com/briefings/anthropic-proceed-ipo-roadshow-next-week) ⭐️ 8.0/10

Anthropic plans to start its IPO roadshow next week and list in the week of November 16, The Information reported citing people familiar, with a previously expected valuation of $1.5 trillion and more than $80 billion raised, though that figure may be revised lower amid AI stock concerns.

telegram · zaihuapd · Nov 7, 01:27

**「Background」** The planned roadshow comes after two weeks of sharp swings in tech stocks; investors recently put Anthropic&\#x27;s fair valuation at roughly $1.4–1.5 trillion, but concerns about AI spending have made that $1.5 trillion target look too high, according to reports.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/markets/haircut-no-2-anthropic-ipo-talk-slides-12-trillion-ai-rout-crushes-odds-november-listing">Haircut No. 2: Anthropic IPO Talk Slides To $ 1 .2 Trillion ... | ZeroHedge</a></li>
<li><a href="https://decrypt.co/382716/anthropic-ipo-valuation-could-fall-to-1-trillion-after-ai-stock-rout-report">Anthropic IPO Valuation Could Be Slashed in Half to... - Decrypt</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI`, `#tech stocks`, `#valuation`

---

<a id="item-finance-news-3"></a>
### [Fed&\#x27;s Daly Says More Rate Hikes Likely as Wages Trail 3.7% Inflation](https://www.cnbc.com/2026/11/06/fed-daly-interest-rates-inflation.html) ⭐️ 7.0/10

San Francisco Fed President Mary Daly said Friday she expects the central bank will need to raise interest rates further, though the timing and amount are still undecided. In October, average hourly earnings rose 3.1% from a year earlier while consumer price inflation was 3.7%, which she said leaves workers on a &\#x27;treadmill of high inflation.&\#x27;

rss · CNBC Finance · Nov 6, 19:05

**「Background」** The rate-setting Federal Open Market Committee raised its benchmark overnight borrowing rate by a quarter point in September to a target range of 3.75%-4%, then held steady last week to await more information.

**「Impact」** Further rate rises would increase borrowing costs for households and businesses at a time when wage growth is failing to keep pace with consumer prices.

**Tags**: `#Federal Reserve`, `#interest rates`, `#inflation`, `#jobs report`, `#monetary policy`

---

<a id="item-finance-news-4"></a>
### [Premarket movers: Lam Research up on buyback, DraftKings down on loss](https://www.cnbc.com/2026/11/06/stocks-making-the-biggest-moves-premarket-moderna-airbnb-cloudflare-affirm-more.html) ⭐️ 7.0/10

Several companies moved sharply in premarket trading after earnings and guidance updates, including Lam Research, which surged nearly 11% after authorizing a $25 billion stock buyback.

rss · CNBC Finance · Nov 6, 13:05

**「Background」** The moves followed quarterly earnings reports, guidance changes, and buyback news from the companies involved, with no single economy-wide catalyst.

**Tags**: `#premarket`, `#earnings`, `#stocks`, `#guidance`, `#buyback`

---

<a id="item-finance-news-5"></a>
### [Nasdaq enters correction territory after 5% drop amid election-driven tech selloff](https://www.cnbc.com/2026/11/05/nasdaq-drops-into-correction-territory-heres-what-typically-happens-next.html) ⭐️ 7.0/10

The Nasdaq Composite fell more than 5% on Thursday and closed more than 11% below last month&\#x27;s record, entering correction territory. CNBC reported that the catalyst was Democrats&\#x27; sweep of the House and Senate plus a Texas governor winning on a pledge to impose an immediate data center moratorium.

rss · CNBC Finance · Nov 6, 20:42

**「Background」** CNBC defines a correction as a decline greater than 10% from a recent high; across 10 episodes in the past decade, the Nasdaq gained an average of 9.41% three months and 17.03% six months after the bottom, with 2022 as the notable exception.

**「Impact」** The selloff hit semiconductor stocks: the iShares Semiconductor ETF \(SOXX\) fell 12% on Thursday, its worst day since March 2020, as investors weighed possible state-level data-center restrictions.

**Tags**: `#stock market`, `#Nasdaq`, `#market correction`, `#semiconductors`, `#election impact`

---