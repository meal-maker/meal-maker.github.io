---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 45 items, 11 important content pieces were selected

---

**Technology News**
1. [Linux Kernel IPv4 TCP Use-After-Free CVE-2026-98432 Warning](#item-tech-news-1) ⭐️ 9.0/10
2. [vLLM v0.33.0rc3: 927 Commits, PyTorch 2.14, CUDA 13.0 Only](#item-tech-news-2) ⭐️ 8.0/10
3. [ChatGPT Share-Link Flaw Allowed Account Takeover](#item-tech-news-3) ⭐️ 8.0/10
4. [Hundreds of AI Apps Disguised as Tools Offer Pornographic Deepfakes](#item-tech-news-4) ⭐️ 8.0/10
5. [Astra can read and write weights to improve Qwen](#item-tech-news-5) ⭐️ 7.0/10
6. [Subvocal smart glasses decode silent speech via RF](#item-tech-news-6) ⭐️ 7.0/10
7. [Cloudflare Halves DNS Build Delay, Cuts Memory Use 85%](#item-tech-news-7) ⭐️ 7.0/10
8. [Census Bureau AI Survey Now Asks About Super Intelligence](#item-tech-news-8) ⭐️ 7.0/10
9. [LightMIS: Ultra-lightweight medical image segmentation for edge devices](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Oracle plans $20 billion capital raise; Marvell to buy Lumentum for $115 billion](#item-finance-news-1) ⭐️ 7.0/10
2. [UK proposes extending settlement period for most immigrants to 10 years](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Linux Kernel IPv4 TCP Use-After-Free CVE-2026-98432 Warning](https://telegram.me/zaihuapd/44866) ⭐️ 9.0/10

A Telegram post warns that the Linux kernel IPv4 TCP stack contains a high-risk use-after-free vulnerability tracked as CVE-2026-98432, exploitable by unauthenticated network attackers without user interaction. The post states that Anthropic has published a remote code execution exploit example targeting MPTCP listen ports, but the flaw is not limited to MPTCP scenarios. According to the Go official security team cited in the post, Go 1.24 and later on Linux enable MPTCP on listen sockets by default, leaving Go services exposed by default, and similar attacks may be possible even without MPTCP listeners. The post urges users with servers to update their kernels.

telegram · zaihuapd · Nov 3, 02:37

**「Background」** CVE-2026-98432 is a use-after-free vulnerability in the Linux kernel&\#x27;s IPv4 TCP handshake code, affecting kernel versions 4.4 and later; a remote unauthenticated attacker can send crafted TCP packets with IP options to trigger memory corruption and potential remote code execution \(AWS, Red Hat\). Multipath TCP \(MPTCP\) is an extension that allows a TCP connection to use multiple paths, and since Go 1.24, Linux listen sockets in Go programs enable MPTCP by default, thereby exposing many Go services to this attack vector even without explicit MPTCP configuration.

**「Impact」** Operators of Linux servers running Go 1.24+ services must treat CVE-2026-98432 as an urgent kernel-update requirement because those services enable MPTCP listeners by default, matching the unauthenticated RCE exploit demonstrated by Anthropic. The per-program godebug multipathtcp=0 mitigation is fragile: a single accidentally exposed MPTCP listener leaves the host vulnerable.

**「Community Discussion」** Commenters debate mitigations, with one suggesting an iptables/nftables raw PREROUTING u32 rule to drop affected TCP options, while others note Ubuntu has delayed a fix and that consumer routers rarely receive kernel security updates. Some also point to a RHEL mitigation that reduces exposure but cannot fully prevent exploitation, without further explanation.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/2026-160-aws/">CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free ...</a></li>
<li><a href="https://access.redhat.com/security/vulnerabilities/RHSB-2026-016">RHSB-2026-016 Use-after-free - kernel IPv4 (CVE-2026-98432 ...</a></li>
<li><a href="https://lilting.ch/en/articles/linux-ipv4-tcp-options-uaf-mptcp-rce">CVE - 2026 - 98432 Linux TCP Use-After-Free Can Give... | lilting channel</a></li>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux&#x27;s October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/2026/10/30/1">oss-security - Fwd: Protecting against CVE - 2026 - 98432 when using Go ...</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#CVE`, `#TCP vulnerability`, `#MPTCP`, `#Go`

---

<a id="item-tech-news-2"></a>
### [vLLM v0.33.0rc3: 927 Commits, PyTorch 2.14, CUDA 13.0 Only](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 8.0/10

vLLM v0.33.0rc3 is a large pre-release with 927 commits from 389 contributors, including 122 new contributors. It adds day-0 support for models such as Reflection Beam-1.0, Yandex AliceAI-Foundation-80B-A3B, Recursive Flint, MiniCPM-OCR 1.0, and many others, and upgrades to PyTorch 2.14.0, torchvision 0.29.0, and Triton 3.8.0. Release wheels and Docker images are now CUDA 13.0 only, dropping CUDA 12.9, and the CUDA wheel is libtorch ABI stable; a new AWS EFA image and a shorter vllm/vllm image alias are also introduced. Speculative decoding, NVIDIA decode performance, and AMD ROCm 10.0 support receive significant improvements, while breaking changes remove Medusa and the MLP speculator, the legacy Ray compiled-graph executor, and deprecate several options.

github · khluu · Nov 2, 10:10

**「Background」** vLLM is an open-source inference and serving engine for large language models, and release candidates are pre-release builds intended for testing before a stable tag. The CUDA 13.0-only wheel change means users running older NVIDIA driver/toolkit combinations tied to CUDA 12.9 must upgrade their environment, and libtorch ABI stability prevents compiled extensions from breaking across libtorch updates.

**「Impact」** Organizations using vLLM on NVIDIA hardware need to migrate to CUDA 13.0-compatible drivers and artifacts immediately if they were pulling the dropped CUDA 12.9 wheels or -cu129 images, and deployments relying on removed Medusa/MLP speculator or the legacy Ray compiled-graph executor must switch to alternatives.

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#PyTorch`, `#CUDA`

---

<a id="item-tech-news-3"></a>
### [ChatGPT Share-Link Flaw Allowed Account Takeover](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter&\#x27;s research team found that a malicious ChatGPT share link could execute code in a logged-in user&\#x27;s session, allowing an attacker to read private conversations and send data to an external server. The victim only needed to open the crafted link; no app installation was required. The issue stemmed from a message-handling flaw between the preview feature and the chart component. OpenAI fixed the vulnerability on October 26, classified it as P1, and paid a $5,000 bounty.

telegram · zaihuapd · Nov 2, 10:24

**「Background」** ChatGPT lets users share conversations through links that render in the browser while the recipient may be logged into their OpenAI account. The preview and chart components process shared content before full navigation, so a crafted link can reach browser-side message handling logic tied to the active session.

**「Impact」** ChatGPT users who opened a malicious share link before the October 26 fix could have had private conversations exposed to an attacker.

**Tags**: `#security`, `#vulnerability`, `#ChatGPT`, `#OpenAI`, `#account-takeover`

---

<a id="item-tech-news-4"></a>
### [Hundreds of AI Apps Disguised as Tools Offer Pornographic Deepfakes](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 8.0/10

WIRED reported on November 2 that a network of more than 400 linked AI apps and websites uses innocuous tools such as pet portraits and language learning as a front, then loads pornographic deepfake interfaces that let users upload people&\#x27;s photos to generate explicit images or videos. Researchers connected the apps through code, domain names, and advertising trackers; 27 apps remained on Google Play in September with more than 350,000 combined downloads, many labeled suitable for all ages. Apple removed 19 apps after WIRED shared its findings, saying developers replaced remote web content after passing review, while Google had already removed most of the apps before being contacted and Meta blocked 209 related apps from advertising. The investigation links the network to Chinese developers and a Hong Kong-registered company based on Chinese-language code, hosting information, and domain clues, though the operators did not respond to requests for comment and that association is the outlet&\#x27;s reporting judgment.

telegram · zaihuapd · Nov 2, 12:45

**「Context」** Sexually explicit deepfakes are AI-generated synthetic images or videos that realistically place a person’s face or body into pornographic scenes without consent. App store review processes typically inspect code and behavior at submission time, but apps can evade this screening by loading remote web content or activating hidden features after approval, which is why platforms must rely on later reports or investigations to remove offenders.

**「Impact」** Users of the affected Google Play and Apple App Store apps were exposed to hidden deepfake tools despite age labels, and enforcement depended in part on WIRED&\#x27;s tip rather than proactive review detection.

**Tags**: `#AI伦理`, `#深度伪造`, `#应用安全`, `#科技调查`, `#平台审核`

---

<a id="item-tech-news-5"></a>
### [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 7.0/10

Astra demonstrates the ability to read and write neural network weights directly, reportedly improving Qwen&\#x27;s math performance. The findings have sparked significant technical debate, with some researchers noting that weight-space editing has prior work and cautioning that the blog may overstate the results. Key claims include identifying the games that small networks were trained on and editing weights to improve outcomes, though specific details are contested.

hackernews · dbreunig · Nov 2, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50341174)

**「Background」** Weight-space programming refers to directly reading and modifying a neural network&\#x27;s weights rather than optimizing text artifacts such as prompts or surrounding programs. The blog post &\#x27;Sparks of Weight - Space Programming&\#x27; reports that Astra, a frontier LLM, inspected Qwen 3.5-0.8B&\#x27;s weights, diagnosed a repetition/loop pathology, and hand-edited 131,072 weights to improve its math performance.

**「Impact」** Researchers can now use GPT-6 Astra to directly edit a small fraction of Qwen&\#x27;s weights—131,072 entries \(0.016% of 800M parameters\)—to improve its math performance, but the reported gains may be overstated and weight-space editing has prior work.

**「Community Discussion」** Community reaction is split: some call the results &\#x27;insane&\#x27; and highlight a reported 5x math improvement for a small Qwen model, while others argue the blog overstates the work and that weight-space editing is not new, pointing to prior research. Some suggest the capability may arise from training on neural weight data rather than emergent understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://huggingface.co/akhaliq/Qwen3.5-0.8B-weight-space-programming">akhaliq/ Qwen 3.5-0.8B- weight - space - programming · Hugging Face</a></li>
<li><a href="https://kingy.ai/blog/weight-space-programming-ai-agent-model-weights/">Weight-Space Programming: GPT-6 Astra Edits Qwen - kingy.ai</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#neural networks`, `#large language models`, `#model editing`, `#AI research`

---

<a id="item-tech-news-6"></a>
### [Subvocal smart glasses decode silent speech via RF](https://news.ycombinator.com/item?id=50340088) ⭐️ 7.0/10

The Subvocal Company, a YC F26 startup founded by two Georgia Tech CS students, is showing smart glasses that decode silent mouthing or internal speech to text using radio-frequency sensing, with a demo video of YC&\#x27;s Dave using the device. The glasses emit Bluetooth-like radio waves through the face; tongue, lip, and soft-palate movements modulate the signal, and foundation models decode the perturbations after a short 20-sentence calibration. The founders initially built an EMG prototype at Stanford&\#x27;s TreeHacks but switched to RF after EMG failed due to sweat, interference, placement variability, and the need for facial electrodes, then scaled cross-user pretraining data. They have opened preorders for a first batch of 500 units with a $200 discount and plan to ship in Q1 2027, positioning it for discreet voice dictation and accessibility, though no independent technical validation is provided.

hackernews · aarushyadav · Nov 2, 17:16

**「Background」** Silent speech interfaces aim to let users communicate without audible voice, often using sensors on or near the face; MIT Media Lab&\#x27;s AlterEgo is a well-known academic example. This implementation uses RF sensing embedded in glasses frames instead of EMG electrodes or cameras, claiming it can observe articulator motion even with lips closed. The post states that &\#x27;internal speech&\#x27; here means mouthing with lips closed rather than automatic tongue movements from thinking words.

**「Impact」** Prospective buyers should treat this as an early-stage prototype: shipments are targeted for Q1 2027, the first batch is 500 units, and the company has not published where inference occurs or whether offline use is supported, leaving privacy-critical users without key information.

**「Community Discussion」** Commenters are enthusiastic about the sci-fi and accessibility potential but raise practical concerns, including fit for high-bridge noses and large heads, a preference for an attachment to existing prescription glasses, and privacy questions about where inference occurs and offline support. One commenter asks whether the same mouth movement could be captured by a standard laptop webcam instead of dedicated hardware, while another requests more technical detail on the website.

**Tags**: `#silent speech recognition`, `#wearable computing`, `#RF sensing`, `#accessibility`, `#smart glasses`

---

<a id="item-tech-news-7"></a>
### [Cloudflare Halves DNS Build Delay, Cuts Memory Use 85%](https://blog.cloudflare.com/dns-targeted-zone-builds/) ⭐️ 7.0/10

Cloudflare has documented an optimization that uses targeted DNS zone builds, cutting DNS build delay by half and reducing memory use by 85%. The change addresses performance and memory efficiency in its large-scale DNS infrastructure.

hackernews · wondersky · Nov 2, 14:47 · [Discussion](https://news.ycombinator.com/item?id=50337558)

**「Background」** Cloudflare runs authoritative DNS infrastructure and must compile and deploy DNS zone files when user configuration changes. Previously, any zone-setting change triggered a full rebuild of the entire zone—even for zones with tens of millions of records—leading to large memory usage and build delays \[tool-1-1\]\[tool-1-2\]. The new targeted build planner identifies the smallest safe set of changes and rebuilds only affected parts of a zone, which is essential context for the reported 85% memory reduction and halved build delay \[tool-1-1\]\[tool-1-3\].

**「Community Discussion」** Commenters questioned whether 700 zone changes per second is low given Cloudflare&\#x27;s scale, asked about the ROI of reducing memory footprint, and wondered about potential bugs introduced before and after the change. Others praised Cloudflare&\#x27;s consistently strong technical blog posts.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-targeted-zone-builds/">How we halved DNS build delay and cut memory use by 85%</a></li>
<li><a href="https://daily.dev/posts/how-we-halved-dns-build-delay-and-cut-memory-use-by-85--jhnmypmtx">How we halved DNS build delay and cut memory use by 85%</a></li>
<li><a href="https://runtimewire.com/article/cloudflare-dns-targeted-zone-builds-memory-delay">Cloudflare stops rebuilding 20-million-record DNS zones to ...</a></li>

</ul>
</details>

**Tags**: `#dns`, `#cloudflare`, `#performance`, `#systems`, `#infrastructure`

---

<a id="item-tech-news-8"></a>
### [Census Bureau AI Survey Now Asks About Super Intelligence](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 7.0/10

Simon Willison revisits U.S. Census Bureau Business Trends and Outlook Survey data and finds the AI adoption metric changed due to Executive Order 14434. Previously the survey asked whether businesses used AI &quot;in producing goods or services&quot;; on November 17, 2025, the wording was broadened to &quot;in any of its business functions.&quot; Starting October 19, 2026, collection changed to ask about &quot;Super Intelligence or SI \(formerly referred to as Artificial Intelligence or AI\).&quot; Under the broadened wording, the largest firms \(250+ employees\) reported about 40.7% use by October 2026, up from around 12% under the old wording in September 2025, but the series are not directly comparable. First survey results reflecting the Super Intelligence wording are due for publication on Thursday.

rss · Simon Willison · Nov 2, 13:31

**「Background」** The Business Trends and Outlook Survey \(BTOS\) is conducted every two weeks by the U.S. Census Bureau, sampling 200,000 businesses out of 1.2 million with a rotating panel. Simon Willison previously used BTOS data to create charts of AI adoption by firm size in September 2025, which showed large-company AI adoption trending down. Executive Order 14434, titled &quot;Inaugurating the Era of Super Intelligence,&quot; was issued in September 2026 and prompted the Bureau to update instrument wording.

**「Impact」** Data analysts using BTOS to measure business AI adoption must treat figures before and after November 17, 2025, and after October 19, 2026, as separate, non-comparable series.

**Tags**: `#AI`, `#policy`, `#data`, `#Census Bureau`, `#executive order`

---

<a id="item-tech-news-9"></a>
### [LightMIS: Ultra-lightweight medical image segmentation for edge devices](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 7.0/10

LightMIS is a 131K-parameter model for 2D binary medical image segmentation that aggregates multi-scale encoder features directly and omits a learned stage-wise decoder. According to one of its authors, it achieves observed modality-macro Dice and IoU averages close to nnWNet on six datasets across five imaging modalities, while using 98.14% fewer parameters and 94.58% fewer GFLOPs under the same nnU-Net v2.3.1 protocol. On an Arm Mali-G52 MC2 GPU edge device, the full LightMIS model ran about 10.5× faster than nnWNet, and all LightMIS variants achieved 100% GPU operator coverage without CPU fallback. The source code, checkpoints, and reproduction details are publicly available on GitHub and in the arXiv paper. These results are self-reported by the author and have not been independently verified.

reddit · r/MachineLearning · /u/OkLion2068 · Nov 2, 20:22

**「Background」** In medical image segmentation, U-Net-style encoder-decoder networks dominate, and nnU-Net is a widely used self-configuring framework that standardizes training and evaluation across datasets and modalities. LightMIS instead removes the learned stage-wise decoder and directly aggregates multi-scale encoder features, which reduces parameters and compute for deployment on edge devices.

**「Edge deployment impact」** For developers deploying 2D binary medical image segmentation on edge devices, LightMIS offers a practical lightweight option: the full model uses 131K parameters, 94.58% fewer GFLOPs than nnWNet, and ran about 10.5× faster on an Arm Mali-G52 MC2 GPU with 100% GPU operator coverage, while maintaining modality-macro Dice and IoU close to nnWNet under the same nnU-Net v2.3.1 protocol. These results are author-reported and await independent verification.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.28327">LightMIS: Ultra-Lightweight Medical Image Segmentation ...</a></li>
<li><a href="https://arxiv.org/abs/2609.28327">[2609.28327] LightMIS : Ultra-Lightweight Medical Image ...</a></li>

</ul>
</details>

**Tags**: `#medical image segmentation`, `#edge AI`, `#deep learning`, `#model efficiency`, `#computer vision`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Oracle plans $20 billion capital raise; Marvell to buy Lumentum for $115 billion](https://www.cnbc.com/2026/11/02/stocks-making-the-biggest-moves-midday-orcl-spcx-tem-rivn.html) ⭐️ 7.0/10

Oracle shares fell another 6% after the company filed plans to sell $10 billion in common stock and $10 billion in senior notes to fund its artificial-intelligence buildout. Marvell Technology agreed to buy Lumentum in an all-stock transaction valued at $115 billion.

rss · CNBC Finance · Nov 2, 20:00

**「Background」** The transaction is expected to close in the first half of 2028.

**Tags**: `#stock movers`, `#earnings`, `#mergers and acquisitions`, `#capital raise`, `#market update`

---

<a id="item-finance-news-2"></a>
### [UK proposes extending settlement period for most immigrants to 10 years](https://www.gov.uk/government/news/home-secretary-unveils-new-rules-for-migrants-settling-in-the-uk) ⭐️ 7.0/10

The UK government has proposed extending the standard settlement period for most immigrants from five to ten years, while allowing the highest earners to apply after three years and those earning over £50,271 or working in public service roles such as doctors, nurses, and teachers to apply after five years.

telegram · zaihuapd · Nov 2, 23:50

**「Background」** Under current rules, many migrants can apply for indefinite leave to remain after five years of lawful residence; the Home Office has consulted on replacing this with a 10-year &quot;earned settlement&quot; model, with the consultation closing on 12 February 2026 and the changes not yet in force.

**「Impact」** MPs warn that the proposed 10-year settlement baseline could worsen staff shortages in health and social care and risk a repeat of the Windrush scandal for affected migrants.

<details><summary>References</summary>
<ul>
<li><a href="https://gardencourtchambers.co.uk/potential-legal-challenge-to-home-office-proposals-to-retrospectively-extend-earned-settlement-ilr-to-ten-years/">Potential legal challenge to Home Office proposals to retrospectively...</a></li>
<li><a href="https://www.visaandmigration.com/news/uk-doubles-the-qualifying-period-for-settlement-to-10-years-under-the-new-earned-settlement-model/297.html">UK doubles the qualifying period for settlement to 10 years</a></li>
<li><a href="https://www.theguardian.com/politics/2026/nov/01/home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush">Home secretary to make some migrants wait 10 years or more ...</a></li>

</ul>
</details>

**Tags**: `#immigration policy`, `#UK`, `#labor market`, `#public services`, `#settlement rules`

---