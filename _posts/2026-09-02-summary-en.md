---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 49 items, 18 important content pieces were selected

---

**Technology News**
1. [Anthropic Releases Claude Fable 5.1 and Mythos 5.1](#item-tech-news-1) ⭐️ 8.0/10
2. [Python 3.15.0 Release Candidate 2 Announced](#item-tech-news-2) ⭐️ 8.0/10
3. [Korea&\#x27;s Trillion-Dollar Sovereign AI Investment: Nvidia Wins, Hynix Loses](#item-tech-news-3) ⭐️ 8.0/10
4. [Virtualizor Update Infrastructure BGP-Hijacked to Deliver Root Backdoor](#item-tech-news-4) ⭐️ 8.0/10
5. [Unverified Report: John Ternus Is Apple&\#x27;s New CEO, Tim Cook Executive Chairman](#item-tech-news-5) ⭐️ 8.0/10
6. [How accurate have Ed Zitron&\#x27;s AI skeptic predictions been?](#item-tech-news-6) ⭐️ 7.0/10
7. [Google Play Blocks Open Collective Donation Link in AnkiDroid](#item-tech-news-7) ⭐️ 7.0/10
8. [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](#item-tech-news-8) ⭐️ 7.0/10
9. [Mapping Latent Reasoning Families in 2026: BDH-CQ, HRM/TRM, Coconut](#item-tech-news-9) ⭐️ 7.0/10
10. [TontaubeV1: Open-Weight 2.9B Character-Level TTS for Long-Form Speech](#item-tech-news-10) ⭐️ 7.0/10
11. [EvoUndo: Recoverability Verification for LLM Agent Self-Evolution](#item-tech-news-11) ⭐️ 7.0/10
12. [Google to Release Gemini 3.8 Flash, Coding Skills Said to Rival OpenAI and Anthropic](#item-tech-news-12) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s solar capacity overtakes coal as largest power source](#item-finance-news-1) ⭐️ 9.0/10
2. [Qualcomm to raise chip prices by double digits for shipments after September 1, 2026](#item-finance-news-2) ⭐️ 8.0/10
3. [Fed Governor Barr says he&\#x27;d support rate hike if inflation doesn&\#x27;t ease](#item-finance-news-3) ⭐️ 7.0/10
4. [China issues guidelines for automakers&\#x27; overseas competition and compliance](#item-finance-news-4) ⭐️ 7.0/10
5. [China clarifies 20% individual income tax on foreign individuals&\#x27; dividends from foreign-invested enterprises](#item-finance-news-5) ⭐️ 7.0/10
6. [Japan Relaxes Overtime Rules, 45-Hour Monthly Cap Not Enforced](#item-finance-news-6) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Anthropic Releases Claude Fable 5.1 and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 8.0/10

Anthropic has released Claude Fable 5.1 and Claude Mythos 5.1, a point update to its language model family. The release is accompanied by documentation and a system card. Community discussion highlights a cache read price reduction from $1 per million tokens to $0.25 per million tokens and claimed improvements in writing style, though benchmark comparisons remain debated.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**「Background」** Claude Fable 5.1 and Claude Mythos 5.1 are incremental updates in Anthropic&\#x27;s Claude model family, released on September 1, 2026, with Fable 5.1 as the generally available model and Mythos 5.1 under restricted access. They follow Claude Fable 5 and retain base API input/output pricing of $10 and $50 per million tokens while cutting cache-read prices by 75%, from $1 to $0.25 per million tokens. Anthropic estimates this reduction lowers typical Fable spending by about 25% and highly agentic spending by more, and the update also reports improved science benchmarks and fewer false refusals.

**「Impact」** Developers using Claude Fable 5.1&\#x27;s cache reads will pay 75% less, from $1 to $0.25 per million tokens, and half the cache read cost of Claude Opus.

**「Community Discussion」** An Anthropic employee praised the improved writing style and more reliable style instruction following. Other commenters debated whether benchmark gains are substantial, with some noting that excluding Terminal-Bench Science 0.1 results shows little change, and expressed skepticism about the Mythos release and removed thought traces.

<details><summary>References</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/">Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1: 52.6% on Terminal-Bench-Science and 75% Cheaper Cache Reads - MarkTechPost</a></li>
<li><a href="https://coursiv.io/blog/claude-fable-5-1">Claude Fable 5.1 and Mythos 5.1: What Anthropic&#x27;s New Models Change, and What They Cost</a></li>
<li><a href="https://claudefa.st/blog/models/claude-fable-5-1">Claude Fable 5.1: Up to 45% Cheaper, 3 Breaking Changes</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#model release`, `#pricing`

---

<a id="item-tech-news-2"></a>
### [Python 3.15.0 Release Candidate 2 Announced](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

Hugo van Kemenade, release manager for Python 3.14 and 3.15, announced Python 3.15.0 release candidate 2, the final RC before the scheduled October release. During the RC phase, only reviewed bug-fix changes are allowed. Third-party maintainers are strongly encouraged to publish Python 3.15 wheels on PyPI, and any binary wheels built against 3.15.0 release candidates will work with future 3.15 versions. Simon Willison notes that the RC is not yet available for GitHub Actions, but provides a testing matrix using actions/setup-python@v7 with allow-prereleases and check-latest flags.

rss · Simon Willison · Sep 1, 14:59

**「Background」** Release candidates are the final pre-release stage, where only reviewed bug fixes are allowed before the stable release. Python 3.15.0 RC2 is the last planned candidate before the final release on 2026-10-01, and the Python team states there will be no ABI changes in the 3.15 series from this point forward. This means binary wheels built against the release candidate are expected to remain compatible with the final 3.15 release.

**「Impact」** Python library maintainers should use this RC window to build and publish binary wheels against Python 3.15, because wheels built against any 3.15 release candidate will remain compatible with the final 3.15.0 release.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.python.org/2026/09/python-3150-rc2/">Python 3 . 15 . 0 candidate 2 is here! | Python Insider</a></li>

</ul>
</details>

**Tags**: `#Python`, `#release candidate`, `#open source`, `#programming languages`, `#software development`

---

<a id="item-tech-news-3"></a>
### [Korea&\#x27;s Trillion-Dollar Sovereign AI Investment: Nvidia Wins, Hynix Loses](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 8.0/10

South Korea is pursuing a trillion-dollar sovereign AI investment program, according to an analysis by Max Kan at SemiAnalysis. The initiative is reshaping competitive dynamics in AI and semiconductors, favoring NVIDIA while putting pressure on Korean memory makers such as SK Hynix and Samsung. The article describes a national AI tournament, likened to a &\#x27;Squid Games&\#x27; competition, in which a leading non-Chinese open-source model was eliminated, illustrating challenges for open-source contenders. It also discusses why Nvidia benefits from open-source models and outlines the implications for Hynix and Samsung.

rss · Semianalysis · Sep 1, 20:14

**「South Korea&\#x27;s sovereign AI context」** South Korea has launched a government-led AI initiative worth about $880 billion, under which SK hynix and Samsung are expected to increase investment; SK hynix separately announced a 19 trillion won \($12.9 billion\) advanced packaging plant to meet AI demand. NVIDIA&\#x27;s data-center GPUs depend on high-bandwidth memory from these Korean suppliers, so the initiative&\#x27;s competitive shifts directly affect memory makers.

**「Nvidia-SK Hynix HBM4 ties persist despite sovereign AI push」** South Korea’s sovereign AI investment has not displaced SK Hynix; the two companies signed a multi-year HBM4 co-development deal on June 8 and SK Hynix remains Nvidia’s largest memory partner, while Samsung and Micron also passed HBM4 certification, and VAST Data will supply its AI OS to SK Telecom’s Petasus GPU cloud.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/nick-florous-ph-d-2821a84_artificial-intelligence-korean-activity-7416803883169120256-aSsc">#artificial #intelligence # korean #cheongju #hbm #us # nvidia ...</a></li>
<li><a href="https://au.finance.yahoo.com/news/sk-hynix-u-listing-tops-124454286.html">SK Hynix U.S. Listing Tops 7x Demand, Targets $24.5 Billion Raise</a></li>
<li><a href="https://thebytedive.com/ai/ai-memory-bottleneck-hbm-sk-hynix-trillion/">AI Memory Bottleneck HBM: The 3-Way Race Re- Opens</a></li>
<li><a href="https://coinlaw.io/nvidia-sk-hynix-ai-memory-supply-deal/">Nvidia Secures SK Hynix AI Memory Supply Deal</a></li>
<li><a href="https://www.blocksandfiles.com/ai-ml/2025/08/14/vast-data-ai-os-inside-south-korea-sovereign-ai-cloud-gpu-service/1593194">VAST Data AI OS inside South Korea sovereign AI cloud GPU service</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductors`, `#NVIDIA`, `#South Korea`, `#open source`

---

<a id="item-tech-news-4"></a>
### [Virtualizor Update Infrastructure BGP-Hijacked to Deliver Root Backdoor](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 8.0/10

Between August 28 and 30, 2026, Virtualizor&\#x27;s update infrastructure was BGP-hijacked, and attackers used a valid TLS certificate to distribute malicious update packages to installations that updated during that window. Virtualizor officially confirmed the incident as a software distribution chain compromise, not a vulnerability in the code itself, and said only a small number of installations were affected. Forensic analysis showed the malicious package writes an attacker-controlled root SSH key, installs a Java payload, and creates a persistence service. Hosting provider AlbaHost found indicators of compromise on 5 of 34 hypervisors it checked. Softaculous stated there is currently no evidence that other products were affected.

telegram · zaihuapd · Sep 1, 06:05

**「Background」** BGP hijacking occurs when an attacker falsely announces ownership of IP address ranges, redirecting traffic to infrastructure they control. Virtualizor is a virtualization management panel developed by Softaculous, and its update mechanism relies on signed updates fetched from official servers. Valid TLS certificates are normally used to authenticate those servers, but a certificate obtained for the hijacked route allowed the malicious updates to appear legitimate.

**「Impact」** Administrators who applied Virtualizor updates between August 28 and 30, 2026, should assume possible compromise and check for unauthorized root SSH keys and new persistence services; AlbaHost identified 5 affected hypervisors out of 34 checked.

**Tags**: `#security`, `#supply-chain-attack`, `#BGP-hijacking`, `#virtualization`, `#root-backdoor`

---

<a id="item-tech-news-5"></a>
### [Unverified Report: John Ternus Is Apple&\#x27;s New CEO, Tim Cook Executive Chairman](https://weibo.com/n/JohnTernus) ⭐️ 8.0/10

An unverified report circulating on Telegram claims that John Ternus has become Apple&\#x27;s CEO and has opened social media accounts on Weibo and X under the handles JohnTernus and @johnternus. The same report says former CEO Tim Cook&\#x27;s bio has changed to &\#x27;Apple Executive Chairman.&\#x27; It also claims that Apple&\#x27;s official X account \(@Apple\) unfollowed Tim Cook and followed John Ternus. The information originates from a repost attributed to &\#x27;Marvin Cui&\#x27; and has not been independently confirmed. If accurate, this would represent a major leadership transition at Apple.

telegram · zaihuapd · Sep 1, 16:07

**「Context」** John Ternus previously served as Apple’s senior vice president of hardware engineering, a role he held since 2021. In April 2026, Apple announced that Tim Cook would become executive chairman of the board and that Ternus would succeed him as CEO, with the transition effective September 1, 2026. Ternus has spent 25 years at Apple and took over after Cook’s 15 years as chief executive.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/John_Ternus">John Ternus - Wikipedia</a></li>
<li><a href="https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/">Tim Cook to become Apple Executive Chairman John Ternus to become Apple CEO - Apple</a></li>
<li><a href="https://www.bbc.com/news/articles/c1kr19lry18o">John Ternus named as Apple chief executive to replace Tim Cook</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#leadership`, `#Tim Cook`, `#John Ternus`, `#tech industry`

---

<a id="item-tech-news-6"></a>
### [How accurate have Ed Zitron&\#x27;s AI skeptic predictions been?](https://danluu.com/zitron/) ⭐️ 7.0/10

Dan Luu published an analysis evaluating the accuracy of Ed Zitron&\#x27;s predictions about AI, focusing on claims that model capabilities have peaked and that AI lab user and revenue growth has stalled. The evaluation is part of ongoing scrutiny of AI industry hype and skepticism. Commenters note that Luu&\#x27;s refutations rely heavily on assertions of error without detailed counter-evidence, and some raise unaddressed accounting practices involving hyperscaler investments in AI startups.

hackernews · jatins · Sep 1, 18:35 · [Discussion](https://news.ycombinator.com/item?id=49526069)

**「Context」** Ed Zitron is an English author, podcaster, and public relations specialist known as a critic of technology companies, particularly those involved in the generative AI boom. He has argued that AI startups are unprofitable at their core and that the industry resembles a bubble. Dan Luu&\#x27;s article evaluates the accuracy of Zitron&\#x27;s specific predictions about AI model capability, lab growth, and adoption.

**「Community Discussion」** Commenters are divided: some find Luu&\#x27;s rebuttals unconvincing and argue that Zitron is likely correct about limited model progress, while others criticize Zitron for becoming a distorted mirror of AI boosters and tailoring his skepticism to a political audience. A few also highlight that hyperscalers&\#x27; accounting for equity investments in AI startups may distort revenue and earnings figures, which the post does not discuss.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ed_Zitron">Ed Zitron - Wikipedia</a></li>
<li><a href="https://www.drjoshcsimmons.com/writing/ed-zitron-ai-predictions">Ed Zitron &#x27;s AI Predictions : What He Got Wrong · Josh C. Simmons</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#skepticism`, `#predictions`, `#technology industry`

---

<a id="item-tech-news-7"></a>
### [Google Play Blocks Open Collective Donation Link in AnkiDroid](https://github.com/ankidroid/Anki-Android/issues/21656) ⭐️ 7.0/10

AnkiDroid reports in GitHub issue \#21656 that Google Play no longer allows its Open Collective donation link, restricting in-app support for the open-source Android app. The policy affects open-source projects that use Open Collective&\#x27;s Open Source Collective fiscal host, which is a 501\(c\)\(6\) entity and not a 501\(c\)\(3\) charity, so donations are not tax-deductible for donors. Commenters point out that Google took similar action against WireGuard in 2019 and cite Play Billing rules that prohibit payments including tax-exempt donations. The issue underscores tensions between app-store control and open-source project funding.

hackernews · hexa555 · Sep 1, 10:11 · [Discussion](https://news.ycombinator.com/item?id=49520022)

**「Background」** AnkiDroid is an open-source Android flashcard application distributed through Google Play. Google Play&\#x27;s payments policy restricts apps from linking to external donation services unless the donations meet certain tax-exempt or charitable conditions, stating that Play billing &quot;must not be used in cases where payments include … tax exempt donations.&quot; AnkiDroid&\#x27;s donation link points to Open Collective, whose fiscal host for AnkiDroid is an IRS 501\(c\)\(6\) organization, meaning contributions are not tax-deductible; the maintainers are asking Google whether a 501\(c\)\(6\) determination satisfies the &quot;tax exempt donations&quot; requirement.

**「Impact」** AnkiDroid and other open-source Android apps relying on Open Collective donations may have to remove in-app donation links from Google Play releases or face policy rejection, potentially reducing their funding options unless they adopt alternative schemes like 501\(c\)\(3\) fiscal sponsors or external donation pages.

**「Community Discussion」** Commenters note Google previously removed WireGuard for a similar donation-link issue in 2019 and discuss whether Open Source Collective&\#x27;s 501\(c\)\(6\) status—meaning donations are not tax-deductible—triggers the Play Billing restriction on tax-exempt donations. Others argue this shows the problem with app-store monopolies and suggest PWAs as an alternative distribution path.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ankidroid/Anki-Android/issues/21656">[Community Help Needed] Google Play : no longer allowing our Open ...</a></li>

</ul>
</details>

**Tags**: `#google-play`, `#open-source`, `#donations`, `#app-store-policy`, `#ankidroid`

---

<a id="item-tech-news-8"></a>
### [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 7.0/10

A blog post reports that a small autoregressive transformer trained from scratch for roughly 1.5 hours achieves strong results on the ARC benchmark, outperforming many larger LLMs. The author clarifies that this is not an LLM and argues that extremely complex problems can be tackled without LLM-scale training costs. Key technical changes included SwiGLU instead of GELU, RMSNorm instead of LayerNorm, more diverse and better-shuffled data, and scaling from 4 to 8 layers. Because ARC is a meta-learning benchmark, the model is intended to learn from evaluation puzzles, and the author states that test labels were not trained on; the result remains a blog-post claim pending independent verification.

hackernews · porridgeraisin · Sep 1, 09:52 · [Discussion](https://news.ycombinator.com/item?id=49519939)

**「Background」** ARC-AGI-1 is a benchmark for abstract reasoning and few-shot generalization from visual puzzles, where many top submissions have used large language models or complex architectures. The described work instead trains a small autoregressive transformer from scratch in 1.5 hours on an NVIDIA 5090 GPU, costing about 67 cents, to explore sample efficiency and the limits of transformers at low cost.

**「Impact」** For researchers working on ARC-style reasoning or sample-efficient models, this suggests a small from-scratch transformer can be competitive with large LLMs at vastly lower training cost, though the finding is based on a single blog report and needs replication.

**「Community Discussion」** Commenters generally engaged positively, asking the author about architecture choices and sample efficiency; one user cautioned that architecture tweaks like SwiGLU/RMSNorm and scaling layers are often &\#x27;squeezing the lemon&\#x27; compared with a new method. The discussion also clarified that training on the evaluation puzzles is not &\#x27;training on test&\#x27; because labels are not used and ARC is a meta-learning benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://mvakde.github.io/blog/44-on-arc-1/">44 % on ARC -AGI- 1 in 67 cents - Mithil Vakde’s Homepage</a></li>
<li><a href="https://news.ycombinator.com/item?id=47262751">44 % on ARC -AGI- 1 in 67 cents | Hacker News</a></li>

</ul>
</details>

**Tags**: `#transformer`, `#ARC benchmark`, `#LLM`, `#sample efficiency`, `#AI research`

---

<a id="item-tech-news-9"></a>
### [Mapping Latent Reasoning Families in 2026: BDH-CQ, HRM/TRM, Coconut](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 7.0/10

The post surveys latent reasoning approaches as an alternative to verbose chain-of-thought, arguing that token-level traces do not reliably track the underlying computation. It groups methods into five families: continuous thoughts in autoregressive LMs \(Coconut, Soft Thinking\), compressed discrete non-linguistic tokens \(Abstract-CoT\), recurrent-depth and looped models \(recurrent-depth LMs, looped Transformers\), task-trained recursive solvers \(HRM, TRM\), and in-context recurrent latent solvers \(BDH-CQ\). Key distinctions proposed are how a system acquires a new task—through context, memory, or gradient-based optimization—and where intermediate computation occurs—through language tokens, abstract tokens, or continuous latent states. The post notes BDH-CQ reports surpassing the previously published cost–accuracy Pareto frontier on public ARC-AGI-1 and pretraining scaling up to 600B parameters, while HRM and TRM are transductive and require a backward pass per unseen ARC task. It frames the central question as whether readable traces are a temporary artifact of scaling or a safety property worth preserving if latent reasoning is more efficient.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 15:14

**「Background」** Chain-of-thought \(CoT\) reasoning in large language models produces explicit intermediate natural-language steps before the final answer, but studies such as Kambhampati \(2025\) note these traces can be unfaithful to the model&\#x27;s actual computation. Latent reasoning is an alternative approach that avoids verbalizing every step, instead repeatedly transforming continuous hidden states or using compressed discrete tokens, and decodes only the final answer. The post surveys this area and distinguishes families including continuous thoughts, compressed non-linguistic tokens, recurrent-depth models, task-trained recursive solvers, and in-context recurrent latent solvers like BDH-CQ.

**「Impact」** The post identifies a concrete tension for AI safety and evaluation: if latent reasoning wins on efficiency, current interpretability tools that depend on readable chain-of-thought traces may lose their target.

**Tags**: `#latent reasoning`, `#large language models`, `#chain-of-thought`, `#machine learning`, `#AI research`

---

<a id="item-tech-news-10"></a>
### [TontaubeV1: Open-Weight 2.9B Character-Level TTS for Long-Form Speech](https://www.reddit.com/r/MachineLearning/comments/1w4afjn/we_released_tontaubev1_a_characterlevel_tts_model/) ⭐️ 7.0/10

TontaubeV1 is a 2.9B-parameter open-weight text-to-speech model for expressive long-form speech, low-latency local inference, and zero-shot voice cloning from up to one minute of reference audio, primarily aimed at English and German. It was trained on about 200k hours of audio across seven languages and builds on DualCodec, a multi-codebook discrete audio codec. The model starts from a Qwen3-1.7B checkpoint but uses character-level tokenization instead of the backbone BPE tokenizer, which the authors report reduced out-of-distribution text-token sequences and simplified character-to-sound mapping. Its chunking scheme places text, semantic audio, and lower acoustic codebooks in one flat sequence with separate logical position IDs, paired split markers, and 25 reserved character positions at boundaries to keep context bounded across long passages. The current release requires 24 GB of VRAM for low-VRAM and balanced profiles or 32 GB for high-throughput, with quantized and fine-tuning releases planned; an LLM-as-judge benchmark scored 50.1% against ElevenLabs Flash v2.5 on prosody and preferred it over Fish Audio S2 Pro, Gradium, and Cartesia Sonic 3, though the authors caution that human listening tests remain the gold standard.

reddit · r/MachineLearning · /u/EAVDR · Sep 1, 12:23

**「Background」** Most LLM-based TTS models add audio tokens to the backbone language model&\#x27;s original BPE tokenizer and predict the next token. TontaubeV1 instead forces Qwen3&\#x27;s tokenizer to emit individual characters, which the authors argue retains language understanding while avoiding rare token combinations in TTS training data; the chunked layout uses logical position IDs rather than standard sequential positions to align text and audio streams.

**「Impact」** ML engineers and TTS developers can now run an open-weight long-form English/German TTS model with zero-shot voice cloning locally, but only on GPUs with at least 24–32 GB of VRAM until the planned quantized and on-device releases arrive.

**Tags**: `#text-to-speech`, `#open-weight model`, `#machine-learning`, `#voice-cloning`, `#audio-generation`

---

<a id="item-tech-news-11"></a>
### [EvoUndo: Recoverability Verification for LLM Agent Self-Evolution](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 7.0/10

EvoUndo introduces a framework for representing, synthesizing, diagnosing, and independently verifying recoverability of LLM agent self-modifications across counterfactual states. Across 600 unseen one-shot self-evolution tasks, the authors identify 197 capability-improving mutations that fail recoverability verification; conventional repair under the original recovery representation recovers 0 of these, while an extended recovery calculus raises empirical oracle recovery to 191/197. A protocol-locked 2×2 grounding-by-expressivity intervention shows exact state-address grounding increases successful recovery from 0/48 to 38/48 when the original language is sufficient, and extending the recovery language enables recovery on 142/143 failures in the oracle-defined S1 stratum. On the primary gpt-oss-120b backbone, adding exact-address diagnostics to the richer language reduces recovery to 133/143, while a Qwen3.8-27B replication preserves grounding and expressivity effects but not this negative interaction, indicating model-dependent behavior. These results suggest reliable agent self-evolution requires co-designing verification, state grounding, witness semantics, and recovery-language expressivity rather than iterative prompting alone.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Sep 1, 19:17

**「Background」** LLM agents can modify their own prompts, tools, middleware, resources, and execution harnesses at runtime, a process known as self-evolution. Such mutations may improve capability but can leave persistent effects that cannot be safely reversed in states different from the one where they were created. Recoverability verification evaluates whether a self-modification can be undone across counterfactual states, which is important for the safety and reliability of evolving AI systems.

**「Impact」** This work shifts the design requirement for agent self-evolution from post-hoc repair to upfront co-design of recovery languages and grounding, because a model’s ability to undo its own mutations depends on these components.

**Tags**: `#LLM agents`, `#self-modification`, `#recoverability`, `#AI safety`, `#machine learning`

---

<a id="item-tech-news-12"></a>
### [Google to Release Gemini 3.8 Flash, Coding Skills Said to Rival OpenAI and Anthropic](https://www.wsj.com/tech/ai/new-google-ai-model-said-to-narrow-gap-on-coding-ability-264c6052) ⭐️ 7.0/10

Google DeepMind reportedly plans to release Gemini 3.8 Flash, internally codenamed Skimaki, as early as this Wednesday with a major upgrade to coding ability. In comparisons using the company&\#x27;s internal programming tool Jetski, engineers are said to have preferred the new model over Anthropic&\#x27;s Opus model. The move is intended to narrow Google&\#x27;s gap in coding performance behind OpenAI and Anthropic, according to people familiar with the matter cited by The Wall Street Journal. The report is based on unnamed sources, and details remain unconfirmed.

telegram · zaihuapd · Sep 2, 00:35

**「Background」** Gemini 3.8 Flash is an unreleased Google Flash-series AI model reportedly being tested internally on the Jetski coding platform; its specifications, public availability, and pricing are not yet confirmed. The Flash line is generally Google&\#x27;s cost-focused workhorse tier, distinct from larger Pro or Ultra models, which makes coding improvements there notable for broad developer access.

**「Impact」** If the reported release occurs, developers using Google&\#x27;s Gemini models for coding could gain a model whose internal JetSki comparisons favored it over Anthropic&\#x27;s Opus, potentially narrowing Google&\#x27;s coding gap. The report is based on unnamed sources and details remain unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-gemini-3-8-flash">Gemini 3 . 8 Flash Is a Cost-Focused Workhorse — Its 1M-Token...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Google`, `#Coding`, `#Software Engineering`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s solar capacity overtakes coal as largest power source](https://content-static.cctvnews.cctv.com/) ⭐️ 9.0/10

China&\#x27;s photovoltaic installed capacity reached 1.286 billion kilowatts by end-July 2026, surpassing coal to become the country&\#x27;s largest power source and making up 31.5% of total installed capacity, according to CCTV News. In January–July 2026, solar generation rose 15.5% year on year to 802.4 billion kilowatt-hours, meaning roughly 1 in 8 kilowatt-hours came from solar.

telegram · zaihuapd · Sep 1, 02:42

**「Background」** Coal had previously been China&\#x27;s largest installed power source, and the country produces about 80% of the world&\#x27;s photovoltaic modules.

**「Impact」** CCTV News reports an expected more than 2 trillion yuan of solar industry investment over the next five years, a figure relevant to solar manufacturers and energy project developers.

**Tags**: `#光伏`, `#能源转型`, `#煤电`, `#中国经济`, `#电力行业`

---

<a id="item-finance-news-2"></a>
### [Qualcomm to raise chip prices by double digits for shipments after September 1, 2026](https://www.macrumors.com/2026/08/31/qualcomm-chip-price-increase/) ⭐️ 8.0/10

Qualcomm announced it will raise prices by double digits for all chips shipped after September 1, 2026, with the exact increase negotiated per customer. CEO Cristiano Amon said the company can no longer absorb rising supplier costs, and Apple is still purchasing Qualcomm modem chips for the iPhone 17.

telegram · zaihuapd · Sep 1, 04:10

**「Background」** Apple&\#x27;s iPhone 17 uses Apple&\#x27;s A19 processor but still relies on Qualcomm for its modem, so Qualcomm&\#x27;s price increases can affect Apple&\#x27;s component costs.

**「Impact」** Electronics manufacturers that buy Qualcomm chips, including Apple for iPhone 17 modems, will face higher component costs once the increase takes effect.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IPhone_17">iPhone 17 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#高通`, `#芯片涨价`, `#半导体`, `#苹果`, `#供应链成本`

---

<a id="item-finance-news-3"></a>
### [Fed Governor Barr says he&\#x27;d support rate hike if inflation doesn&\#x27;t ease](https://www.cnbc.com/2026/09/01/fed-governor-barr-says-hell-support-rate-hike-if-inflation-doesnt-ease.html) ⭐️ 7.0/10

Federal Reserve Governor Michael Barr said he would support raising interest rates if inflation does not ease, with headline inflation at 3.7% over the past year, above the Fed&\#x27;s 2% target.

rss · CNBC Finance · Sep 1, 14:01

**「Background」** Barr, a permanent voting member of the Fed&\#x27;s rate-setting committee, spoke as the central bank has kept its benchmark rate in a target range of 3.5%–3.75% and futures markets price about a 66% chance of an increase this month, according to CME Group&\#x27;s FedWatch.

**Tags**: `#Federal Reserve`, `#interest rates`, `#inflation`, `#monetary policy`, `#rate hike`

---

<a id="item-finance-news-4"></a>
### [China issues guidelines for automakers&\#x27; overseas competition and compliance](https://weibo.com/1664176597/Rg5PKzXXE) ⭐️ 7.0/10

China&\#x27;s commerce, industry, and market regulators jointly issued guidelines for automakers&\#x27; overseas competition and compliance, requiring them to avoid low-price dumping that disrupts market order and to cooperate with local supply chains.

telegram · zaihuapd · Sep 1, 08:15

**「Background」** The guideline was issued by China&\#x27;s Ministry of Commerce, Ministry of Industry and Information Technology, and State Administration for Market Regulation to guide overseas competition and compliance for Chinese automakers.

**「Impact」** The guidelines directly affect Chinese automakers and auto parts suppliers expanding overseas, as they must now manage their foreign pricing to avoid low-price dumping and unfair market-distorting competition.

<details><summary>References</summary>
<ul>
<li><a href="https://cd.nbd.com.cn/articles/2026-09-01/4568721.html">叫停海外市场价格战！三部门整肃汽车出口秩序：规范定价营销，强化全链条合规 | 每经网</a></li>

</ul>
</details>

**Tags**: `#automotive industry`, `#China`, `#regulation`, `#overseas expansion`, `#compliance`

---

<a id="item-finance-news-5"></a>
### [China clarifies 20% individual income tax on foreign individuals&\#x27; dividends from foreign-invested enterprises](https://m.cnfin.com/wx/share?url=//m.cnfin.com/yw-lb//zixun/20260901/4463424_1.html) ⭐️ 7.0/10

China&\#x27;s Ministry of Finance and State Taxation Administration announced that dividends received by foreign individuals from foreign-invested enterprises will be subject to a 20% individual income tax rate from September 1, 2026. Foreign-invested enterprises must withhold the tax and file within 15 days after the month of payment, replacing the relevant clause of Caishuizi \[1994\] No. 20.

telegram · zaihuapd · Sep 1, 09:33

**「Background」** Before this change, China’s 1994 tax notice \(Caishuizi \[1994\] No. 20\) temporarily exempted foreign individuals from individual income tax on dividends and bonuses received from foreign-invested enterprises. A State Council reform opinion in 2013 had already proposed removing that exemption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minterpku.com/publications/news/1825822202373738497.html">税筹的挑战：港澳身份还能享受“外籍个人”股息免税待遇吗？</a></li>
<li><a href="https://guangdong.chinatax.gov.cn/gdsw/sltydyl_jlct_wtjd/2025-01/21/content_9a80ca1cf0d441289aea94e1f41f43c7.shtml">外籍个人从外商投资企业取得的股息、红利所得是否免征个人所得税？</a></li>
<li><a href="https://www.chinatax.gov.cn/chinatax/c102449/c5222170/content.html">外籍个人从外商投资企业取得的股息、红利所得是否免征个人所得税？_国家税务总局</a></li>

</ul>
</details>

**Tags**: `#tax policy`, `#foreign investment`, `#individual income tax`, `#dividend withholding`, `#China`

---

<a id="item-finance-news-6"></a>
### [Japan Relaxes Overtime Rules, 45-Hour Monthly Cap Not Enforced](https://www.orientaldaily.com.my/news/international/2026/09/01/844683) ⭐️ 7.0/10

Japan relaxed overtime rules on September 1, with labor standards inspectors no longer enforcing the monthly 45-hour overtime cap. About 40% of Japanese firms already allow up to 100 hours of monthly overtime, and government officials warn that exceeding 45 hours raises the risk of death from overwork.

telegram · zaihuapd · Sep 1, 12:56

**「Background」** The easing follows the growth strategy adopted by Prime Minister Takaichi&\#x27;s government in July; labor unions criticized the change as reversing shorter-work-hour reforms.

**Tags**: `#Japan`, `#labor policy`, `#overtime regulation`, `#economic growth`, `#work reform`

---