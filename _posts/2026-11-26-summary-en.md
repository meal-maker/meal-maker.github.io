---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 31 items, 13 important content pieces were selected

---

**Technology News**
1. [Hacker News Debates Claimed Matrix Multiplication Exponent of Nine Fourths](#item-tech-news-1) ⭐️ 8.0/10
2. [1Password Discloses November 2026 Production Code Push Security Incident](#item-tech-news-2) ⭐️ 8.0/10
3. [Shorter, better documented GRH Lean proof from Anthropic](#item-tech-news-3) ⭐️ 8.0/10
4. [Google Releases Cogentic Papers on Integer Factorization and Discrete Logs](#item-tech-news-4) ⭐️ 8.0/10
5. [Minecraft Java RCE via crafted TrueType fonts affects 1.20.5+](#item-tech-news-5) ⭐️ 8.0/10
6. [Ubuntu Security Update Delays Prompt Debian Migration Discussion](#item-tech-news-6) ⭐️ 7.0/10
7. [Evaluating Recent Model Releases on GDPx](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI Bets Cybersecurity Will Surpass Coding, Launches GPT-6 Cyber and Daybreak](#item-tech-news-8) ⭐️ 7.0/10
9. [Tencent Open-Sources Hy4 Flash Quantized GGUF Weights](#item-tech-news-9) ⭐️ 7.0/10
10. [Asia Data Centers Sell Surplus AI Compute to US After Export Curbs](#item-tech-news-10) ⭐️ 7.0/10
11. [Samsung, SK Hynix Said to Adopt YMTC Xtacking NAND Technique](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [US plans new Section 301 tariffs on 14 trading partners, with extra 20% on China](#item-finance-news-1) ⭐️ 9.0/10
2. [US Commerce Department Allegedly Threatened Intel to Hand Over 10% Stake Worth $11 Billion](#item-finance-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Hacker News Debates Claimed Matrix Multiplication Exponent of Nine Fourths](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

A Hacker News discussion links to Scott Aaronson&\#x27;s blog and to a paper claiming that the matrix multiplication exponent is nine fourths \(ω = 9/4\). The submission reflects high engagement around AI-assisted mathematical progress and a potentially significant theoretical computer science result, but the supplied source content provides only the link and no proof details or confirmation. Commenters debate whether the claimed exponent reduction, if verified, would represent a major advance for fast matrix multiplication algorithms and what it implies for AI&\#x27;s broader capabilities.

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**「Background」** The matrix multiplication exponent ω is the smallest real number such that two n×n matrices can be multiplied using O\(n^ω\) arithmetic operations; schoolbook multiplication gives ω=3, Strassen&\#x27;s 1969 algorithm first showed ω&lt;3, and later refinements lowered the known upper bound to roughly 2.37. A trivial lower bound is ω≥2, and determining the exact value has been a central open problem in theoretical computer science. On November 24, 2026, OpenAI posted a preprint claiming a proof that ω=9/4 \(2.25\) over every field, based on a tensor-network compression argument and accompanied by a Lean formalization with 592 dependent modules.

**「Matrix multiplication exponent」** If confirmed, the OpenAI preprint would settle the matrix multiplication exponent at exactly 9/4 by providing matching upper and lower bounds over every field, with a Lean formalization, giving researchers a definitive reference for the asymptotic complexity of n×n matrix multiplication.

**「Community Discussion」** Comments show a split: some argue that success in axiomatic mathematics does not imply AI will solve other sciences or pose existential risk, while others insist the scale of change is being underestimated. One commenter asks whether Lean, MathLib, and large compute without LLMs might have produced the same result, questioning the causal role of generative AI.

<details><summary>References</summary>
<ul>
<li><a href="https://raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf">The matrix multiplication exponent is nine fourths</a></li>
<li><a href="https://www.advanceintelligence.ai/story/2026-11-24-22">OpenAI Posts a 111 Page Proof That the Matrix Multiplication ...</a></li>
<li><a href="https://lilting.ch/en/articles/matrix-multiplication-exponent-nine-fourths-openai">Checking OpenAI&#x27;s 9/4 Matrix Multiplication Exponent Paper ...</a></li>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>
<li><a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/README.md">math /preprints/The- matrix - multiplication - exponent -is...</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#mathematics`, `#matrix multiplication`, `#theoretical computer science`, `#research`

---

<a id="item-tech-news-2"></a>
### [1Password Discloses November 2026 Production Code Push Security Incident](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password disclosed a November 2026 security incident involving a potential malicious code push to its production services. The company&\#x27;s announcement raised concerns about SaaS supply chain attacks, where a compromised employee laptop can allow attackers to push code to GitHub and deploy it. Community discussion flagged the lack of sufficient detail on whether branch protection rules were missing or bypassable for backend services, and one commenter reported receiving a high-quality phishing email that referenced their 1Password vault details. The incident illustrates the central risk that production code deployment from compromised employee endpoints poses for widely used SaaS password managers.

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**「Background」** 1Password, a widely used password manager, disclosed that on November 19, 2026 an attacker gained access to an employee&\#x27;s corporate GitHub account and used it to push malicious code to backend services. The code downloaded administrative data about customers, but 1Password states that vault contents, secrets, passwords, and encryption keys were not accessed or compromised. This incident illustrates a SaaS supply-chain attack, in which compromising a developer&\#x27;s source-control account can lead to deploying malicious code into production services.

**「Impact」** One commenter reports receiving a high-quality phishing email referencing their 1Password vault sharing details, suggesting attackers may be using incident-related information to target users.

**「Community Discussion」** Commenters describe compromised employee laptops leading to malicious production code pushes as a standard and critical SaaS attack vector, with one urging a clear statement that encrypted vaults were not downloaded. Several express concern that the announcement does not address whether branch protection rules or push-to-main controls were missing or bypassed, and a user reports a follow-on phishing message that includes personal vault details.

<details><summary>References</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.1password.community/announcements-52/update-on-a-security-incident-involving-1password-s-backend-systems-customer-vaults-were-not-affected-and-all-vault-contents-remain-secure-26259">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/">1Password customer data stolen after employee GitHub account ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#saas`, `#supply-chain-attack`, `#password-manager`, `#incident-response`

---

<a id="item-tech-news-3"></a>
### [Shorter, better documented GRH Lean proof from Anthropic](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

A much shorter and better documented Lean formalization of Anthropic&\#x27;s GRH proof has been published, reducing the line count from roughly 17 million to about 76,000 lines—a 99.56% reduction. The new version organizes the proof into a clear &\#x27;known math&\#x27; vs &\#x27;new math&\#x27; split and adds human-readable documentation throughout. This substantially improves accessibility and makes the formal verification result easier to review by the community. A Zulip discussion is available for further technical details.

hackernews · nb-t · Nov 25, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50648050)

**「Background」** The original Anthropic formalization of the Riemann Hypothesis and Generalized Riemann Hypothesis in Lean 4 consisted of about 17.4 million lines of code. The new repository provides a much shorter verification, with a compact edition of about 76,000 lines and a readable edition of about 300,000 lines, both built on Mathlib and using only the axioms propext, Classical.choice, and Quot.sound.

**「Impact」** The shorter proof should make the Anthropic GRH verification far more practical for independent review and reuse by Lean users and formal verification researchers.

**「Community Discussion」** Commenters welcomed the reduction and clearer structure, with some hoping mathematicians will eventually extract a conventional paper and conference presentation from the core argument.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lsernau/grh-lean">GitHub - lsernau/grh-lean: A short Lean 4 proof of the ...</a></li>
<li><a href="https://ashutoshai.com/ai-compass/2026/11/25/anthropic-compact-lean-4-grh-proofs/">Anthropic releases 76k-line compact Lean 4 proofs of RH and GRH</a></li>
<li><a href="https://math.mit.edu/~drew/shortgrh/">Shorter GRH Lean proof: verification files - MIT Mathematics</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean`, `#AI`, `#mathematics`, `#GRH`

---

<a id="item-tech-news-4"></a>
### [Google Releases Cogentic Papers on Integer Factorization and Discrete Logs](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

Google Research has published a collection of technical papers under the name &quot;Cogentic&quot; in a GitHub repository. The papers address integer factorization, discrete logarithms, and related mathematical problems that underlie widely used public-key cryptography. The release is generating expert discussion because advances in these areas could affect the security assumptions of schemes such as RSA and Diffie-Hellman. Specific results, dates, and performance data are not provided in the source snippet.

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**「Background」** Integer factorization and discrete logarithms are foundational computational problems in number theory whose presumed difficulty underpins the security of widely used cryptographic schemes such as RSA and Diffie-Hellman. The discrete logarithm problem involves finding the exponent needed to map one group element to another under repeated multiplication, as illustrated in the Wikipedia reference. Cogentic is described in community discussion as a specialized harness that enables existing large language models to collaborate on mathematical conjectures using a central orchestrator and a shared database of intermediate proofs.

**「Impact」** Because integer factorization and discrete logarithms underpin widely used public-key cryptography, researchers and security practitioners may use these papers to reassess the security margins of algorithms like RSA and Diffie-Hellman.

**「Community Discussion」** Commenters broadly frame the release as part of a wave of AI-driven mathematical breakthroughs, with one noting credible rumors that this is only &quot;the tip of something bigger&quot; and another drawing parallels to AlphaGo&\#x27;s exploration of large search spaces. Some express astonishment at the pace, while others question why markets are not reacting more positively.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer factorization , discrete ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cryptography`, `#mathematics`, `#Google Research`, `#integer factorization`

---

<a id="item-tech-news-5"></a>
### [Minecraft Java RCE via crafted TrueType fonts affects 1.20.5+](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10

The minecraft2shell disclosure on November 22 showed that a crafted TrueType font in a server resource pack can trigger an out-of-bounds write in FreeType 2.14.3 and earlier, allowing arbitrary code execution on Windows Java Edition clients. The vulnerability affects Java Edition versions 1.20.5 through 1.21.10 and snapshots 26.1 through 26.4, while 1.20.4 and earlier and Bedrock Edition are not affected. Mojang still uses lwjgl-freetype 3.4.3 and has released no patch, but a community fix named m2sfix 1.0.0 was released on November 24 as a Java agent or mod that disables hinting. Until a fix is applied, users are advised not to add resource packs, to set multiplayer server resource packs to disabled, or to install the community mod.

telegram · zaihuapd · Nov 25, 12:46

**「Background」** Minecraft Java Edition uses the FreeType library to render TrueType fonts, including fonts supplied by server resource packs. Crafting a malformed TrueType font can exploit a native out-of-bounds write in FreeType 2.14.3 and earlier, turning font loading into code execution on vulnerable Windows clients.

**「Impact」** Windows Minecraft Java Edition users on versions 1.20.5-1.21.10 or snapshots 26.1-26.4 should disable server resource packs or install the m2sfix 1.0.0 Java agent/mod until Mojang provides an official patch, because a malicious server font can execute arbitrary code.

**Tags**: `#security`, `#rce`, `#minecraft`, `#freetype`, `#vulnerability`

---

<a id="item-tech-news-6"></a>
### [Ubuntu Security Update Delays Prompt Debian Migration Discussion](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

An Openwall oss-security post reports delays in Ubuntu security updates, drawing notable Hacker News discussion. The delays affect one of the most widely used Linux distributions, raising concerns about downstream exposure to known vulnerabilities. Community members describe migrating server images from Ubuntu to Debian and point to cases where fixes reach the -updates repository before the security repository. One quoted stable kernel maintainer emphasizes that secure systems require taking all stable/LTS releases rather than cherry-picking patches. The discussion highlights trade-offs between timely patching and regression testing resources across distributions.

hackernews · gslin · Nov 25, 20:38 · [Discussion](https://news.ycombinator.com/item?id=50647181)

**「Context」** Ubuntu, a widely used Linux distribution maintained by Canonical, publishes security fixes through dedicated repositories such as -security, while oss-security is a public mailing list used for discussing and coordinating open-source vulnerabilities. Hanno Böck&\#x27;s post on that list argues that Ubuntu has been slow to ship fixes for severe Linux kernel flaws, citing a remote TCP memory corruption issue \(CVE-2026-98432\) where details were public on November 16 before Ubuntu patched it. Debian, another major distribution, is often compared for its careful regression testing and patch reliability, and some administrators have migrated to it because of these delays.

**「Impact」** For system administrators relying on Ubuntu&\#x27;s security repositories, delayed patches may extend exposure to known vulnerabilities; some community members have already switched server images to Debian.

**「Community Discussion」** Commenters largely consider the slow response unacceptable and report moving to Debian, while others caution that Debian has limited QA resources and can ship regressions; one user notes fixes often appear in -updates before the security repo.

<details><summary>References</summary>
<ul>
<li>oss-sec: Slow Ubuntu security response times - Seclists.org</li>
<li>Slow Ubuntu security response times | daily.dev</li>
<li>Open Source Security Mailing List - Seclists.org</li>

</ul>
</details>

**Tags**: `#Ubuntu`, `#Linux security`, `#open source`, `#vulnerability response`, `#system administration`

---

<a id="item-tech-news-7"></a>
### [Evaluating Recent Model Releases on GDPx](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases) ⭐️ 7.0/10

GPT-6.2 Astra leads the GDPx benchmark but performs poorly on software engineering tasks, while Gemini 4 Neon shows significant improvement from Google yet remains overrated. Fable 5.2 is intelligent but comes with high cost, and new Chinese models are also evaluated. The article highlights trade-offs among performance, cost, and software engineering capability across these recent releases.

rss · Semianalysis · Nov 26, 00:05

**「What is GDPx?」** GDPx is a benchmark from SemiAnalysis that evaluates frontier AI models on 206 agent tasks across 11 high-value domains like chip design, with top models initially scoring only around 12%. It was released in November 2026 and uses realistic work setups, with early leaders including Claude Opus 5.5 and Gemini 4 Carbon. The current evaluation applies GDPx to newer releases such as GPT-6.2 Astra, Gemini 4 Neon, Fable 5.2, and several Chinese models, focusing on performance, cost, and software engineering capability.

**「Impact」** For teams choosing among these models, GDPx leadership does not translate directly to software engineering utility: GPT-6.2 Astra tops the benchmark but is weak at coding, while Fable 5.2&\#x27;s high cost must be weighed against its intelligence, making use-case-specific evaluation of cost-performance trade-offs necessary.

<details><summary>References</summary>
<ul>
<li><a href="https://digestai.news/story/semianalysis-releases-gdpx-benchmark-for-frontier-ai-models">SemiAnalysis releases GDPx benchmark for frontier AI models</a></li>
<li><a href="https://www.swarchitect.net/en/semianalysis-gdpx-benchmark-2026-11/">SemiAnalysis GDPx : Opus 5.5 leads agent test at 12% · SW Architect</a></li>
<li><a href="https://www.finops.org/wg/optimizing-genai-usage/">Optimizing GenAI Usage: A FinOps Perspective on Cost ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#model evaluation`, `#benchmarks`, `#software engineering`, `#large language models`

---

<a id="item-tech-news-8"></a>
### [OpenAI Bets Cybersecurity Will Surpass Coding, Launches GPT-6 Cyber and Daybreak](https://www.theinformation.com/newsletters/ai-agenda/openais-roadmap-making-cyber-bigger-coding-remains-blurry) ⭐️ 7.0/10

OpenAI is positioning cybersecurity as a potential growth area that could surpass its coding business. The company&\#x27;s CFO said external estimates of a cybersecurity market above $300 billion are still significantly underestimated, and President Greg Brockman stated that cybersecurity will become a larger business segment for OpenAI than programming. OpenAI has introduced GPT-6 Cyber for security research and is expanding its Daybreak trusted access program, which as of September covered thousands of verified defenders and about 2,000 approved organizations and workspaces. Daybreak supports vulnerability discovery, codebase analysis, and binary reverse engineering. However, competition with Anthropic and Google and the ability to scale commercialization remain unclear.

telegram · zaihuapd · Nov 25, 04:51

**「Background」** OpenAI&\#x27;s Daybreak program provides cybersecurity tools including a plugin, Defense Factory for connected repositories, Red Team for authorized security testing, and Codex Security CLI/SDK for terminal workflows and custom integrations. GPT-6 Cyber was introduced on November 5 as a specialized cybersecurity variant of GPT-6 Astra, designed to discover vulnerabilities, reproduce security flaws, develop working exploits, and help researchers test defenses.

**「Impact」** Security researchers and vetted organizations may gain access to GPT-6 Cyber through Daybreak for tasks such as vulnerability discovery, codebase analysis, and binary reverse engineering, though OpenAI&\#x27;s commercial scale against Anthropic and Google is not yet clear.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/daybreak/">Daybreak | OpenAI for cybersecurity | OpenAI</a></li>
<li><a href="https://www.youtube.com/watch?v=uz3LF-YBjoE">GPT - 6 Cyber : OpenAI &#x27;s New AI Found 81 Hidden Firefox... - YouTube</a></li>
<li><a href="https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html">OpenAI Launches GPT - 6 Cyber After AI Helps Find 81 Firefox Flaws...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#cybersecurity`, `#AI`, `#GPT-6`, `#software engineering`

---

<a id="item-tech-news-9"></a>
### [Tencent Open-Sources Hy4 Flash Quantized GGUF Weights](https://mp.weixin.qq.com/s/o0xxShVQX6g2UllrrEv1WQ) ⭐️ 7.0/10

Tencent Hunyuan has open-sourced GGUF quantized weights for its 224B-parameter Hy4 flash model through the AngelSlim model compression toolkit. The original weights are about 410.27 GiB, while the smallest IQ2-AH quantization is 125.73 GiB, roughly 30% of the original, and can run on a 64 GB Mac mini using the Strata offload framework. Reported performance includes 89 tokens per second on a 48 GB VRAM device with 10K context, and 47 tokens per second for the Q3\_K version on an M5 Max with 128 GB memory at 32K context. In DeepSWE v1.1 evaluations, the Q3\_K quantization scores within 0.4 points of the original model.

telegram · zaihuapd · Nov 25, 09:29

**「Background」** GGUF is a binary format widely used to distribute quantized large language model weights for CPU and GPU inference via runtimes such as llama.cpp. Quantization reduces model size at some cost to quality; the Hy4 flash is a 224B-parameter mixture-of-experts model originally about 410 GiB in full precision. Strata is a dedicated MoE offload engine that can run only a few models, moving expert layers between memory tiers to allow large models on limited hardware like a 64 GB Mac mini.

**「Impact」** Developers with modest hardware such as a 64 GB Mac mini can now run a 224B-parameter Hunyuan model locally via Strata offload and the IQ2-AH GGUF quantization, with Q3\_K retaining near-original DeepSWE v1.1 scores.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ewhacc/tandem.cpp">GitHub - ewhacc/tandem.cpp: llama.cpp patch: faster MoE offload for...</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#model quantization`, `#GGUF`, `#on-device inference`, `#open-source AI`

---

<a id="item-tech-news-10"></a>
### [Asia Data Centers Sell Surplus AI Compute to US After Export Curbs](https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand) ⭐️ 7.0/10

The US government has tightened a loophole that allowed Chinese technology companies to obtain Nvidia&\#x27;s most advanced chips. Data centers across Asia are now rushing to resell surplus AI compute to American buyers. Liquid Compute CEO Ronit Jain said the new restrictions on exporting advanced AI accelerators to the region are disrupting providers that had counted on leasing compute to Chinese customers. The shift was reported by Bloomberg on November 25, 2026.

telegram · zaihuapd · Nov 25, 11:35

**「Background」** The US restricts direct exports of Nvidia&\#x27;s most advanced AI chips to China, so some operators set up data centers in Southeast Asia where Chinese firms could legally rent remote access to those chips. The US government has now tightened this loophole, leaving Asian data centers with excess AI compute capacity that they are trying to sell to US buyers.

**「Impact」** Data center operators with capacity originally built for Chinese AI renters now face potential stranded utilization and are pivoting sales to US customers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-25/asia-data-centers-sound-out-us-clients-to-replace-china-demand">Asia Data Centers Sound Out US Clients to Replace China Demand</a></li>
<li><a href="https://www.nytimes.com/2026/11/16/us/politics/trump-china-ai-chip-loophole.html">Trump Administration Moves to Close A.I. Chip Loophole Ahead of...</a></li>

</ul>
</details>

**Tags**: `#AI算力`, `#出口管制`, `#数据中心`, `#英伟达`, `#科技政策`

---

<a id="item-tech-news-11"></a>
### [Samsung, SK Hynix Said to Adopt YMTC Xtacking NAND Technique](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 7.0/10

Samsung Electronics and SK Hynix have reportedly agreed through a cross-license deal to adopt part of Yangtze Memory Technologies&\#x27; Xtacking chip-stacking technology for 3D NAND flash, according to a Phoenix Tech report. The technique fabricates NAND memory cells and CMOS control circuits on separate wafers and then bonds them together, allowing each part to be produced and optimized independently. An Omdia senior analyst noted that this would let manufacturers make memory arrays themselves while outsourcing logic circuits to wafer foundries that can use more advanced process nodes. All three companies declined to comment, and the report has not been officially confirmed.

telegram · zaihuapd · Nov 25, 14:33

**「Background」** Yangtze Memory Technologies \(YMTC\) introduced its Xtacking architecture for 3D NAND at the Flash Memory Summit. Xtacking fabricates the memory array and CMOS control circuitry on separate wafers and then bonds them together, allowing each part to be produced and optimized independently. The approach can boost NAND I/O speed to 3.0 Gbps, comparable to DDR4, and prioritizes storage density and high-speed I/O.

**「Impact」** If confirmed, the cross-license would give Samsung and SK Hynix a path to make memory arrays in-house while sending CMOS logic circuits to foundries using more advanced process nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://m.elecfans.com/article/1010365.html">关于4 D NAND 和 长 江 存 储 Xtacking 的对比分析介绍- 电 子 发烧友网</a></li>
<li><a href="https://www.esmchina.com/news/3936.html">长 江 存 储 首次弯道超车！ 重磅发布 Xtacking 技术，下一代64...</a></li>

</ul>
</details>

**Tags**: `#3D NAND`, `#semiconductor manufacturing`, `#YMTC`, `#Samsung`, `#SK Hynix`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US plans new Section 301 tariffs on 14 trading partners, with extra 20% on China](https://www.cnbc.com/2026/11/25/us-tariffs-trump-section-301.html) ⭐️ 9.0/10

CNBC reports that the US government plans new Section 301 tariffs on 14 trading partners, including China, the EU, Japan and India. China would face an additional 20% tariff on top of the existing 25%, potentially rising to 40% if it breaks the October 2025 Busan trade truce.

telegram · zaihuapd · Nov 25, 13:59

**「Background」** The measures are authorized under Section 301 of the Trade Act of 1974 and target manufacturing overcapacity from subsidized production; country-specific rates will not exceed levels in reciprocal trade framework agreements and, except for China, will not stack with existing tariffs.

**Tags**: `#tariffs`, `#trade policy`, `#Section 301`, `#China`, `#global trade`

---

<a id="item-finance-news-2"></a>
### [US Commerce Department Allegedly Threatened Intel to Hand Over 10% Stake Worth $11 Billion](https://www.wired.com/story/inside-trumps-demands-to-another-chips-ceo/) ⭐️ 8.0/10

Court documents allege that US Commerce Department lawyers pressured Intel in August 2025, warning that refusal to hand over a stake would bring unpredictable consequences. Intel&\#x27;s board later gave the US a 10% equity stake worth about $11 billion with no US payment, and President Trump announced the government controlled that stake.

telegram · zaihuapd · Nov 25, 13:25

**「Background」** The allegations emerged from documents unsealed in a lawsuit by shareholder Richard Paisner against Intel&\#x27;s board, which claims the equity demand was tied to $8.9 billion in CHIPS Act funding.

**「Impact」** The alleged transfer dilutes existing Intel shareholders by a 10% equity stake now controlled by the US government without compensation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gate.com/news/detail/intel-lawsuit-reveals-trumps-alleged-10-stake-demand-for-chips-act-funds-25863723">Intel Lawsuit Reveals Trump&#x27;s Alleged 10% Stake Demand for ...</a></li>

</ul>
</details>

**Tags**: `#Intel`, `#US government`, `#semiconductors`, `#equity stake`, `#policy`

---