---
layout: default
title: "Horizon Summary: 2026-10-21 (EN)"
date: 2026-10-21
lang: en
---

> From 42 items, 16 important content pieces were selected

---

**Technology News**
1. [eMudhra Intermediate CA Compromise](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepSeek Open-Sources DeepInfer Inference Framework](#item-tech-news-2) ⭐️ 8.0/10
3. [Mistral Announces Voxtral 3 Real-Time Open-Weight Voice Model and SDK](#item-tech-news-3) ⭐️ 8.0/10
4. [Google Open-Sources TorchTPU Native PyTorch Backend for TPUs](#item-tech-news-4) ⭐️ 8.0/10
5. [Tsrs: Cloudflare&\#x27;s Rust Port of TypeScript Compiler](#item-tech-news-5) ⭐️ 8.0/10
6. [Google Cloud europe-west2 outage disrupts banking and other services](#item-tech-news-6) ⭐️ 8.0/10
7. [Nvidia Reportedly Bars Small Cloud Providers Using AMD or TPUs From GTC](#item-tech-news-7) ⭐️ 8.0/10
8. [OpenAI New Models Boost COBOL Migration Accuracy to 97.9%](#item-tech-news-8) ⭐️ 8.0/10
9. [Ofcom concedes defeat in 4chan case](#item-tech-news-9) ⭐️ 7.0/10
10. [How I Got Over 300 Tor Exit Nodes Removed](#item-tech-news-10) ⭐️ 7.0/10
11. [2026 Rust compiler work targets trait solver, Polonius, specialization](#item-tech-news-11) ⭐️ 7.0/10
12. [Xiaomi MiMo-V2.6-Pro Launches on WorkBuddy](#item-tech-news-12) ⭐️ 7.0/10
13. [OpenAI API Adds 12-Hour Prompt Caching](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s micro-dramas projected to become fourth-largest global online entertainment format](#item-finance-news-1) ⭐️ 8.0/10
2. [HSBC CEO warns AI boom won’t make every data center a good bet](#item-finance-news-2) ⭐️ 7.0/10
3. [Treasury Secretary: Over $8 Billion Deposited in Trump Child Accounts](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [eMudhra Intermediate CA Compromise](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 9.0/10

Private keys for eight eMudhra intermediate CA certificates have been compromised. These certificates chain to roots trusted by the Mozilla, Microsoft, Apple, and Chrome root programs and many downstream trust stores. All software that bundles trusted certificate lists must be updated; Linux distributions need new ca-certificates packages, and Python releases uv 0.13.4, pip 26.2.2, and certifi 2026.10.19 already include upgraded certificate lists.

rss · Simon Willison · Oct 20, 23:50

**「Background」** eMudhra is a certificate authority whose intermediate CA certificates chain to root certificates trusted by the Mozilla, Microsoft, Apple, and Chrome root programs. In the Web PKI, intermediate CAs issue end-entity TLS certificates, and possession of an intermediate private key would allow an attacker to forge valid HTTPS certificates for arbitrary domains. Many applications and operating systems maintain static CA bundle files and must be updated to remove trust in the compromised intermediates.

**「Impact」** Users and administrators must update all CA bundles—including those embedded in third-party applications—because patching only the system CA bundle may leave systems vulnerable.

**「Community Discussion」** Commenters highlighted that the compromised keys were trivially weak, including one whose private key was the single byte &\#x27;4&\#x27;. They also noted uneven remediation: browsers with OneCRL/CRLite were protected automatically, while many applications embed their own CA stores and may remain vulnerable until patched; eMudhra attributed the incident to a flaw in its ECC key-generation script.

<details><summary>References</summary>
<ul>
<li><a href="https://emudhra.we-have-a-problem.com/">eMudhra Intermediate CA Compromise</a></li>
<li><a href="https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/">Protecting Firefox users following the compromise of eMudhra ...</a></li>

</ul>
</details>

**Tags**: `#certificate-authority`, `#security`, `#TLS`, `#software-supply-chain`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [DeepSeek Open-Sources DeepInfer Inference Framework](https://github.com/deepseek-ai/DeepInfer) ⭐️ 8.0/10

DeepSeek has open-sourced DeepInfer, a high-performance inference framework for DeepSeek models. The project reports using the framework to achieve high-throughput, low-latency large-scale inference services for DeepSeek V4.1 Flash, with a single cluster throughput of 155 trillion tokens per day and revenue of $38 per card per hour at off-peak pricing. The release follows closely after a DHS exclusion order was made public, which some commenters interpret as a tactical move prepared in advance, and includes support for Huawei Ascend 950 NPUs according to community discussion. The open-sourcing is presented as part of a strategy to make AI models and inference available as raw materials, potentially reshaping AI infrastructure and hardware competition.

hackernews · ggcr · Oct 20, 09:08 · [Discussion](https://news.ycombinator.com/item?id=50163277)

**「What is DeepInfer?」** DeepInfer is the high-performance inference framework that DeepSeek uses to serve its models in large-scale production environments. This open-source release provides offline inference and was originally built primarily on vLLM, covering core features needed for serving at scale. The release focuses on the inference engine codebase only; DeepSeek states it will synchronize inference-related engineering efforts with hardware partners before future model launches.

**「High-throughput serving for DeepSeek models」** According to a DeepSeek-linked post cited in the discussion, DeepInfer provides developers and infrastructure operators a route to high-throughput, low-latency serving for DeepSeek V4.1 Flash, with a single cluster throughput of 155 trillion tokens per day and overall revenue of $38 per card per hour at off-peak pricing.

**「Community Discussion」** Community members see the release as a strategic challenge to US AI labs and Nvidia&\#x27;s hardware dominance, with open-weight models and Ascend NPU support lowering barriers for smaller players. Some commenters note the timing relative to a DHS exclusion order and describe the framework&\#x27;s performance metrics as a &\#x27;nuclear bomb&\#x27; for US frontier labs, while others emphasize the broader economic shift toward treating AI as raw material.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek-ai/DeepInfer: DeepInfer: High-performance ...</a></li>
<li><a href="https://github.com/deepseek-ai/open-infra-index/blob/main/OpenSourcing_DeepSeek_Inference_Engine/README.md">open-infra-index/OpenSourcing_DeepSeek_Inference ... - GitHub</a></li>
<li><a href="https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/">DeepSeek Open-Sources DeepInfer, the Inference Framework ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50163277">DeepSeek just open-sourced its inference engine | Hacker News</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#inference-framework`, `#open-source`, `#llm-serving`, `#ai-infrastructure`

---

<a id="item-tech-news-3"></a>
### [Mistral Announces Voxtral 3 Real-Time Open-Weight Voice Model and SDK](https://mistral.ai/news/voxtral-3/) ⭐️ 8.0/10

Mistral has announced Voxtral 3, a real-time open-weight voice model and voice agent SDK for speech-to-text and spoken agent workflows. The SDK combines listening, reasoning, tool calling, and speaking into a real-time experience, allowing agents to retrieve information, interact with business systems, and complete tasks during live conversations over phone or web. The announcement positions Voxtral 3 as an open-weight option for developers building spoken command interfaces and voice agents.

hackernews · ilreb · Oct 20, 16:02 · [Discussion](https://news.ycombinator.com/item?id=50168396)

**「Context」** Voxtral 3 is Mistral&\#x27;s voice agent SDK for real-time speech in 50+ languages, combining transcription, reasoning, tool calls, and speech. It is built on LiveKit and can be EU-hosted or self-deployed, with a streaming pipeline that includes Voxtral Realtime Transcribe 3, a general reasoning model like Mistral Small, and Voxtral Speech 3.

**「Impact」** Developers building voice agents can now consider an open-weight real-time speech model and SDK from Mistral, potentially reducing dependence on cloud-only proprietary STT/TTS services; however, community comments indicate that local deployment constraints and transcription quality remain practical concerns.

**「Community Discussion」** Commenters expressed skepticism about the realism of the demo, with one noting that fast dermatologist appointments are unrealistic in France, while others praised offline inference of the prior Voxtral Mini 4B Realtime model on 4GB VRAM. Some raised concerns about STT quality in corporate tools and local deployment, and one commenter described the new offering as closed despite the open-weight framing.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/voxtral-3/">Voxtral 3: Voice Agent SDK &amp; Speech Models in 50+ Languages</a></li>
<li><a href="https://www.goodiebase.com/news/mistral-voxtral-3-voice-agent-sdk-2026-10-20">Mistral launches Voxtral 3 speech models and a toolkit for ...</a></li>
<li><a href="https://www.explainx.ai/blog/voxtral-3-mistral-voice-agent-sdk-speech-models">Voxtral 3: Mistral Voice Agent SDK, $13/1M Chars TTS ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#voice AI`, `#speech-to-text`, `#open-weight models`, `#Mistral`

---

<a id="item-tech-news-4"></a>
### [Google Open-Sources TorchTPU Native PyTorch Backend for TPUs](https://github.com/google-pytorch/torch_tpu) ⭐️ 8.0/10

Google Cloud has open-sourced TorchTPU, a native PyTorch backend for TPUs co-developed with Meta&\#x27;s PyTorch team, making TPUs a first-party PyTorch target alongside GPUs and CPUs. Existing PyTorch code requires little or no modification to run on TPUs with the new backend. Several serving and training frameworks including vLLM, SGLang, llm-d, and TorchTitan have already integrated TorchTPU, and Hugging Face Transformers v5 can deploy models to TPU directly. The move simplifies PyTorch deployment on Google&\#x27;s AI accelerators and removes the need to work through XLA for PyTorch on TPUs.

hackernews · ilreb · Oct 20, 16:40 · [Discussion](https://news.ycombinator.com/item?id=50169053)

**「Background」** Prior to TorchTPU, running PyTorch on Google TPUs typically relied on the XLA compiler and required workarounds; TorchTPU is an open source collaboration between Google and Meta that provides a native PyTorch backend for Google TPUs. TPUs, Google&\#x27;s Tensor Processing Units, are custom AI accelerators, and this backend makes TPUs a native option alongside GPUs and CPUs for PyTorch execution.

**「Impact」** PyTorch developers can now run existing code on TPUs with minimal changes, and serving frameworks such as vLLM, SGLang, and Hugging Face Transformers v5 have already integrated TorchTPU for direct TPU deployment.

**「Community Discussion」** Commenters broadly welcomed first-party PyTorch support on TPUs, with one noting an open-source libtpu implementation for Tenstorrent accelerators already runs most of TorchTPU and another pointing to Amazon&\#x27;s similar torch-neuronx effort for Trainium. Some see TorchTPU as a sign of XLA&\#x27;s viability beyond TensorFlow or as the &\#x27;final nail&\#x27; for TensorFlow, while one commenter frames it as a shift toward edge inference by Google and Apple.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus">TorchTPU is now open source: Run native PyTorch on TPUs</a></li>
<li><a href="https://pytorch.org/blog/introducing-torchtpu/">Introducing TorchTPU - PyTorch</a></li>

</ul>
</details>

**Tags**: `#pytorch`, `#tpu`, `#google`, `#open-source`, `#ai-infrastructure`

---

<a id="item-tech-news-5"></a>
### [Tsrs: Cloudflare&\#x27;s Rust Port of TypeScript Compiler](https://blog.cloudflare.com/typescript-rust-port/) ⭐️ 8.0/10

Cloudflare&\#x27;s tsrs project ports the TypeScript compiler to Rust, achieving significant speedups and enabling TypeScript compilation in WebAssembly-only sandboxes without a Go runtime. The initial motivation was to run a TypeScript compiler in Cloudflare&\#x27;s WASM sandbox, where exporting tsc/Go would include the full Go runtime; the Rust port is reportedly faster than the reference tsc/Go implementation. The TypeScript team has been collaborating with tsrs maintainers to understand which optimizations are safe, and suspects much of the speed comes from algorithmic improvements rather than language choice, with some changes expected to make TypeScript 7.1 faster and leaner. The project uses a unique memory model with never-freed arenas to simulate garbage collection for long-lived objects. The port was largely AI-generated, with the author stating they wrote zero code.

hackernews · hnisjafx40 · Oct 20, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50165953)

**「Background」** Cloudflare and VoidZero are incubating tsrs, an experimental Rust port of the TypeScript compiler inside the Oxc toolchain. The project is explicitly described as not a fork of TypeScript, and early benchmarks show it running up to 8x faster than TypeScript 7.0 while using 70% less memory. It was originally started at Owner.com last month before moving to Cloudflare.

**「Impact」** Developers can use tsrs via the @tsrs/wasm npm package to type-check TypeScript code with 8x faster performance and 70% less memory, enabling compilation in WASM sandboxes without a platform-specific binary. However, the compiler has known compatibility gaps and WASM limits, so teams should verify support for their codebase before switching.

**「Community Discussion」** Commenters highlight the TypeScript team&\#x27;s close collaboration and the innovative arena-based memory model for sidestepping Rust&\#x27;s lack of GC; one user clarifies the project originated from needing a compiler for Cloudflare&\#x27;s WASM-only sandbox rather than purely speed. Some express concern that the port is largely AI-generated, worrying about maintainability of a carefully handwritten compiler replaced by model output.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/typescript-rust-port/">Introducing tsrs: a Port of TypeScript to Rust | Cloudflare Blog</a></li>
<li><a href="https://www.webpronews.com/cloudflare-voidzero-tsrs-rust-port-typescript-compiler/">Cloudflare and VoidZero Take On tsrs, a Rust Port of the ...</a></li>
<li><a href="https://thenewstack.io/cloudflare-rust-typescript-tsrs/">“We are not forking TypeScript”: Cloudflare spearheads Rust ...</a></li>
<li><a href="https://www.npmjs.com/package/@tsrs/wasm">@tsrs/wasm - npm</a></li>
<li><a href="https://book.st-hakky.com/en/news/introducing-tsrs-a-port-of-typescript-to-rust">tsrs: 8x Faster and 70% Less Memory than TypeScript</a></li>

</ul>
</details>

**Tags**: `#typescript`, `#rust`, `#compiler`, `#webassembly`, `#performance`

---

<a id="item-tech-news-6"></a>
### [Google Cloud europe-west2 outage disrupts banking and other services](https://www.neowin.net/news/google-cloud-outage-takes-down-hsbc-revolut-bank-of-scotland-llyods-equifax-more/) ⭐️ 8.0/10

A Google Cloud outage in the europe-west2 region began on Monday, 2026-10-19 at 23:08 PDT after a power event in the europe-west2-b zone. The disruption affected multiple services, with reports of banking and financial platforms including HSBC, Revolut, Bank of Scotland, Lloyds, and Equifax experiencing issues. Google stated the power event was mitigated and partial mitigation to infrastructure services was expected within 30 minutes, while remaining services would follow. The outage left some users unable to access accounts or make payments, underscoring the operational risk of concentrated cloud infrastructure for financial services.

hackernews · paweladamczuk · Oct 20, 10:26 · [Discussion](https://news.ycombinator.com/item?id=50163961)

**「Background」** Google Cloud organizes compute resources into regions and zones; europe-west2 is one such region serving parts of Europe. Major banks and financial institutions increasingly rely on these cloud regions for customer-facing apps and transaction processing, so a zone-level power failure can propagate into wider service disruptions.

**「Impact」** Users of affected services, particularly Revolut and possibly Lloyds, HSBC, Bank of Scotland, and Equifax, experienced interrupted access to banking apps and payment operations during the europe-west2 incident, though one commenter reported HSBC services remained operational.

**「Community Discussion」** Commenters shared Google&\#x27;s status-page note that the outage stemmed from a power event in europe-west2-b and that mitigation was underway. User experiences varied: one reported Revolut was inaccessible with no support contact, another said HSBC was working and criticized Downdetector as an unreliable source, while a third expected continued Lloyds login issues even after cloud recovery.

**Tags**: `#cloud-computing`, `#outage`, `#infrastructure`, `#google-cloud`, `#banking`

---

<a id="item-tech-news-7"></a>
### [Nvidia Reportedly Bars Small Cloud Providers Using AMD or TPUs From GTC](https://x.com/SemiAnalysis_/status/2111162214891610496?s=20) ⭐️ 8.0/10

Nvidia has reportedly refused several small cloud providers entry to the upcoming GTC Berlin because they deploy AMD GPUs, Google TPUs, or other competing accelerators, not because they fail technical requirements. Nvidia has not publicly commented. The company is both a chip supplier and a major investor in emerging cloud firms such as CoreWeave and Nebius, with $2 billion strategic investments in each and revenue guarantees for rented compute, which creates pressure on smaller providers to avoid publicly using rival chips for fear of losing GPU supply, financing, or IPO prospects. The reported restriction reportedly does not apply to hyperscale cloud providers with enough purchasing volume and in-house chip capability.

telegram · zaihuapd · Oct 20, 12:32

**「Background」** Nvidia&\#x27;s GTC Berlin conference is scheduled for October 20–22, 2026, and serves as a key industry event for AI hardware announcements and partner engagement. The affected providers are &\#x27;neoclouds&\#x27;—smaller GPU cloud operators that rent accelerated computing capacity; Nvidia both supplies chips to and has strategic investments in some of them, including CoreWeave and Nebius. The exclusion claims were reported by chip research firm SemiAnalysis in an X post on October 16, 2026.

**「Impact」** Small cloud providers that use AMD GPUs or Google TPUs may be excluded from Nvidia GTC events, creating pressure to avoid competitor hardware and potentially affecting their access to Nvidia supply and investment, though Nvidia has not publicly commented.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/nvidia-neoclouds-gtc-berlin-amd-tpu/">Nvidia reportedly bars neoclouds from GTC Berlin over AMD and ...</a></li>
<li><a href="https://thebuildout.ai/intel/55074a0e-dd6a-4ca0-a816-56a6ff0ce8db">Nvidia reportedly denies GTC Berlin access to cloud providers ...</a></li>
<li><a href="https://aistockwire.com/blog/nvidia-nvda-gtc-berlin-neoclouds-refused-amd-tpu-semianalysis-october-2026">SemiAnalysis: neoclouds refused GTC Berlin over AMD, TPUs</a></li>
<li><a href="https://thebuildout.ai/intel/55074a0e-dd6a-4ca0-a816-56a6ff0ce8db">Nvidia reportedly denies GTC Berlin access to cloud providers ...</a></li>
<li><a href="https://cryptobriefing.com/nvidia-neoclouds-gtc-berlin-amd-tpu/">Nvidia reportedly bars neoclouds from GTC Berlin over AMD and ...</a></li>
<li><a href="https://www.ainvest.com/news/nvidia-reported-gtc-berlin-snub-amd-neoclouds-share-defense-weakest-link-flex-2610/">Nvidia&#x27;s reported GTC Berlin snub of AMD-using neoclouds is a ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#GPU`, `#Cloud Computing`, `#AI Hardware`, `#Antitrust`

---

<a id="item-tech-news-8"></a>
### [OpenAI New Models Boost COBOL Migration Accuracy to 97.9%](https://openai.com/index/low-resource-programming-languages/) ⭐️ 8.0/10

OpenAI reports that its latest models substantially improved development and migration for low-resource programming languages including COBOL, Fortran, and Visual Basic. In a test of building a SQLite engine from scratch across 20 languages, GPT-6 Astra&\#x27;s average pass rate rose from GPT-5.6 Sol&\#x27;s 26.8% to 87.4%, while the lower-cost GPT-6 Luna achieved 40.3% with API costs down 78%. For migrating legacy COBOL code to modern languages, GPT-6.1 Sol at low inference intensity improved accuracy from 5.4% to 86.6% with costs reduced 39%, and reached 97.9% at high inference intensity. The evaluation set has been open-sourced on GitHub.

telegram · zaihuapd · Oct 20, 14:24

**「Background」** Low-resource programming languages such as COBOL and Fortran have less publicly available training data than mainstream languages, which historically made AI-generated code for them less reliable. COBOL remains widely used in legacy financial and government systems, so migrating its code to modern languages requires high accuracy to avoid operational failures. OpenAI’s new evaluations cover software engineering tasks, building a SQLite engine across 20 languages, and translating legacy COBOL code.

**「Impact on COBOL modernization」** For organizations maintaining COBOL systems, OpenAI&\#x27;s reported 97.9% high-reasoning migration accuracy and 39% lower cost at low reasoning could make AI-assisted modernization more attractive, but external sources caution that a tool alone does not migrate a system and validation still depends on human judgment and management.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/low-resource-programming-languages/">Advancing coding in low ‑ resource programming languages | OpenAI</a></li>
<li><a href="https://insights.mgm-tp.com/en/2026/insurance/claude-can-migrate-cobol-migration-who-is-making-the-transition/">Claude COBOL Migration : Who&#x27;s Making the Transition?</a></li>
<li><a href="https://abstracta.us/blog/ai/cobol-migration">How to Validate a COBOL Migration with AI | Abstracta</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Code Generation`, `#COBOL`, `#Programming Languages`, `#OpenAI`

---

<a id="item-tech-news-9"></a>
### [Ofcom concedes defeat in 4chan case](https://prestonbyrne.com/2026/10/20/ofcom-concedes-defeat/) ⭐️ 7.0/10

Ofcom, the UK communications regulator, has conceded defeat in its enforcement case against 4chan. The concession highlights the limits of national online safety rules when applied to foreign platforms that do not have a local presence. The outcome is being viewed as a potential precedent for how foreign internet platforms can resist UK online safety obligations.

hackernews · iamnothere · Oct 20, 14:30 · [Discussion](https://news.ycombinator.com/item?id=50167028)

**「Background」** 4chan is an anonymous English-language imageboard launched in 2003, hosting boards on many topics. Ofcom, the UK communications regulator, had fined 4chan £520,000 in an online safety enforcement action, but 4chan disputed the action as a US-based platform. Commenters on the dispute noted that enforcement against foreign sites often relies on domestic measures such as DNS blocking rather than direct action abroad.

**「Impact」** Ofcom&\#x27;s concession indicates that non-UK platforms can resist the Online Safety Act with limited practical consequences, as a £20,000 fine and open investigations did not force 4chan to comply.

**「Community Discussion」** Community commenters dispute the practical significance: some call the case largely symbolic because Ofcom cannot easily enforce against operators with no UK presence, while others warn it may push the UK toward technical blocking or deep packet inspection and criticize civil service capacity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/4chan">4 chan - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50167028">Ofcom concedes defeat in 4 chan case | Hacker News</a></li>
<li><a href="https://www.linkedin.com/posts/harrybrignull_ofcom-fines-4chan-520000-lawyer-responds-activity-7440404299685314561-xAOX">&quot; Ofcom Fines 4 chan £520,000, Lawyer Responds With Picture of...&quot;</a></li>
<li><a href="https://www.theguardian.com/technology/2025/jun/10/ofcom-4chan-online-safety-breaches">UK media regulator investigates possible online safety breaches at...</a></li>
<li><a href="https://cybernews.com/news/ofcom-issues-20k-fine-to-4chan-for-ignoring-information-requests/">Ofcom fines 4 chan £20K over safety law | Cybernews</a></li>
<li><a href="https://www.bbc.co.uk/news/articles/ckgqwlvq180o">4 chan and porn sites investigated by Ofcom - BBC News</a></li>

</ul>
</details>

**Tags**: `#ofcom`, `#4chan`, `#online-safety`, `#regulation`, `#internet-governance`

---

<a id="item-tech-news-10"></a>
### [How I Got Over 300 Tor Exit Nodes Removed](https://kaba.cx/posts/20261020_Tor/) ⭐️ 7.0/10

On October 2, 333 malicious Tor exit nodes—about 10% of all exits—began redirecting SSH port 22 connections to 12 interception servers. These servers ran a paramiko-based man-in-the-middle that stole passwords and attempted to deliver Ebury malware to connecting clients. The author detected the attacks with exitmap and worked to remove the nodes; SSH&\#x27;s host-key warning banner made the interception immediately visible. The operation affected password-based SSH logins but not key-based authentication.

hackernews · kabakabakaba · Oct 20, 13:39 · [Discussion](https://news.ycombinator.com/item?id=50166257)

**「Background」** Tor exit nodes are the final relays in the Tor anonymity network that forward traffic to its destination, making them able to observe or tamper with unencrypted data. SSH clients normally verify a server&\#x27;s host key to prevent man-in-the-middle attacks, but if a user ignores a key-change warning, an attacker can intercept credentials. The Ebury malware is an OpenSSH backdoor used to steal SSH credentials, and the Tor network has roughly 3000 exit relays total, so 333 compromised nodes represent about 10% of exit capacity.

**「Impact」** Users who made password-authenticated SSH connections through affected Tor exit nodes risked credential theft and Ebury malware delivery, while key-based authentication was not directly exposed.

**「Community Discussion」** Some commenters argued the attack was poorly conceived because SSH&\#x27;s host-key warning exposed the MITM and enabled rapid tracing. Others noted that key-based authentication was not vulnerable to the password theft, and exitmap&\#x27;s original author welcomed continued use of the tool.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/how-i-got-over-300-tor-exit-nodes-removed-luas3vpcw">How I got over 300 Tor exit nodes removed - daily.dev</a></li>

</ul>
</details>

**Tags**: `#security`, `#tor`, `#ssh`, `#malware`, `#network-security`

---

<a id="item-tech-news-11"></a>
### [2026 Rust compiler work targets trait solver, Polonius, specialization](https://yoyo-code.com/2026-is-exciting-year-for-rust-compiler-and-me/) ⭐️ 7.0/10

Panstromek&\#x27;s post frames 2026 as a pivotal year for the Rust compiler, highlighting anticipated work on the new trait solver and Polonius. These projects are described as resolving major technical debt that compiler developers have wanted for years. If completed, they could unblock long-awaited language features such as specialization. The post is forward-looking and does not describe shipped changes, so the improvements remain prospective.

hackernews · panstromek · Oct 20, 13:53 · [Discussion](https://news.ycombinator.com/item?id=50166502)

**「Background」** Rust&\#x27;s compiler has carried long-standing technical debt in its trait system and borrow checker, which has blocked advanced language features. The next-generation trait solver has been in development for almost 10 years, and Polonius is a separate new borrow-checking engine intended to improve precision. Several of these initiatives are described as reaching maturity together in 2026, making that year pivotal for unblocking features like specialization.

**「Impact」** For Rust developers, the anticipated 2026 compiler changes could unblock specialization and address long-standing trait-solver limitations, but this remains prospective rather than a delivered release.

**「Community Discussion」** Comments express cautious optimism about the new trait solver and Polonius unblocking specialization, with questions about async improvements and polymorphism hints. A dissenting comment argues Rust&\#x27;s compile times and complexity may lead to a successor language with Go&\#x27;s simplicity, Zig&\#x27;s speed, and Rust&\#x27;s safety.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/2026-is-an-exciting-year-for-the-rust-compiler-and-me--52dhmmibn">2026 is an exciting year for the Rust compiler (and me)</a></li>
<li><a href="https://yoyo-code.com/2026-is-exciting-year-for-rust-compiler-and-me/">2026 is an exciting year for the Rust compiler (and me)</a></li>

</ul>
</details>

**Tags**: `#rust`, `#compiler`, `#traits`, `#polonius`, `#programming-languages`

---

<a id="item-tech-news-12"></a>
### [Xiaomi MiMo-V2.6-Pro Launches on WorkBuddy](https://weibo.com/6486870325/5356179212995907) ⭐️ 7.0/10

Xiaomi has announced that MiMo-V2.6-Pro is now available on WorkBuddy. According to Xiaomi, the model scored 46 on the Artificial Analysis intelligence index, ranking first among open-source models globally. It supports a 1 million token context, multi-agent collaboration, and joint understanding of images, video, audio, and text. Xiaomi positions it for long-task hosting, deep research, design drafts, document office work, and small tool development, and it is currently open for trial. The ranking claim comes from Xiaomi&\#x27;s promotional announcement and has not been independently verified.

telegram · zaihuapd · Oct 20, 13:40

**「Background」** Artificial Analysis&\#x27;s Intelligence Index is a composite benchmark for comparing model intelligence, and on that index MiMo-V2.6-Pro scores 46.32, which Xiaomi&\#x27;s own materials say surpasses Kimi K3 and Qwen3.8 Max to become the strongest open-source model to date. The MiMo-V2.6 series keeps the API pricing of the V2.5 series, with MiMo-V2.6-Pro listed at $0.43 per 1M input tokens and $0.87 per 1M output tokens.

**「Impact」** Developers and organizations evaluating open-source models can now try MiMo-V2.6-Pro on WorkBuddy for long-context, multimodal, multi-agent workflows, but the claimed Artificial Analysis \#1 ranking should be treated as unverified until independent benchmarks confirm it.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://artificialanalysis.ai/models/mimo-v2-6-pro">MiMo - V 2 . 6 - Pro - Intelligence , Performance... | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#Xiaomi`, `#MiMo`, `#open-source AI`, `#multimodal`, `#WorkBuddy`

---

<a id="item-tech-news-13"></a>
### [OpenAI API Adds 12-Hour Prompt Caching](https://x.com/OpenAIDevs/status/2112603916076781778) ⭐️ 7.0/10

OpenAI announced that its API now supports 12-hour prompt caching. Persistent agents such as dots can reuse shared instructions, tools, and context throughout the day, even when requests are hours apart, and pay the lower cached input rate. Additionally, logged-in Codex and Work users receive permanent caching, with no penalty when returning to old conversations or pausing for hours, and a guaranteed cache hit.

telegram · zaihuapd · Oct 21, 01:21

**「Prompt caching context」** Prompt caching reuses the beginning of a prompt \(such as system instructions, tool schemas, and shared context\) across API calls so repeated prefixes are processed once and billed at a lower cached-input rate. OpenAI has previously offered shorter cache retention windows for some users and services; for example, reports note a 5-hour Codex/Work cap for ChatGPT Plus and a 24-hour cache retention flag for GPT-5.1/GPT-5/GPT-4.1. Anthropic&\#x27;s Claude Code, by comparison, added a 1-hour prompt cache. This extension to 12-hour API caching and permanent caching for logged-in Codex/Work users therefore matters for long-running agents that need to reuse context hours later.

**「Impact」** Developers building long-running agents on the OpenAI API can reduce input-token costs by using cached prompts for up to 12 hours, while Codex and Work logged-in users get permanent caching with guaranteed hits.

<details><summary>References</summary>
<ul>
<li><a href="https://nowline.net/reports/openai-s-responses-api-keeps-agents-working-while-your-tools-run">OpenAI &#x27;s Responses API keeps agents working while your tools run...</a></li>
<li><a href="https://www.linkedin.com/posts/sahar-mor_alpha-tip-for-openai-api-users-to-significantly-activity-7399469492470280192-m8dR">Alpha tip for OpenAI API users to significantly reduce latency and...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#prompt caching`, `#API`, `#AI agents`, `#developer tools`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s micro-dramas projected to become fourth-largest global online entertainment format](https://content-static.cctvnews.cctv.com/snow-book/index.html?toc_style_id=feeds_default&amp;amp;item_id=11947338521606813154&amp;amp;channelId=1119) ⭐️ 8.0/10

China&\#x27;s National Radio and Television Administration reported that the country&\#x27;s micro-drama industry is becoming the fourth-largest global online entertainment format, with the 2026 domestic market projected at 850 billion yuan and the overseas market outside China projected to exceed US$16 billion, up 67% from 2025.

telegram · zaihuapd · Oct 20, 08:39

**「Background」** The report positions Chinese micro-dramas, short episodic video series, alongside US films, Japanese anime, and Korean TV dramas.

**Tags**: `#micro-dramas`, `#China entertainment industry`, `#market size`, `#overseas expansion`, `#AI-generated content`

---

<a id="item-finance-news-2"></a>
### [HSBC CEO warns AI boom won’t make every data center a good bet](https://www.cnbc.com/2026/10/20/data-center-financing-ai-debt-hsbc.html) ⭐️ 7.0/10

HSBC CEO Georges Elhedery warned Tuesday that investors should be selective in data center investments, saying not all tenancy agreements and pricing are strong enough to support. JPMorgan Chase estimates $4.1 trillion in AI-related debt will be issued by the end of the decade.

rss · CNBC Finance · Oct 20, 10:39

**「Background」** HSBC is both a financier and operator of data centers, ranked the seventh-largest bank globally with close to $3 trillion in assets last year.

**「Impact」** AI-related borrowing is already a source of tension in bond markets, with major economy bond yields hitting multi-decade highs in 2026.

**Tags**: `#AI`, `#data centers`, `#debt financing`, `#bond markets`, `#HSBC`

---

<a id="item-finance-news-3"></a>
### [Treasury Secretary: Over $8 Billion Deposited in Trump Child Accounts](https://x.com/SecScottBessent/status/2112323120380129562) ⭐️ 7.0/10

U.S. Treasury Secretary Scott Bessent said on X that over $8 billion has been deposited into Trump child savings accounts, and he thanked Elon Musk for donating stock to the program.

telegram · zaihuapd · Oct 20, 09:57

**「Background」** Trump Accounts are U.S. government-backed savings accounts for children; automatic enrollment has expanded the program to nearly 70 million minors under 18 with Social Security numbers, while the initial rollout gave $1,000 seed investments to children born in 2025–2028.

**「Household impact」** Households with children born in 2025–2028 are eligible for automatically opened investment savings accounts with a $1,000 seed investment, affecting nearly 70 million minors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.whitehouse.gov/releases/2026/10/a-financial-stake-in-the-future-for-nearly-70-million-american-children-trump-accounts-made-it-possible/">Trump Accounts Put 70 Million Kids on the Path to Financial Freedom</a></li>

</ul>
</details>

**Tags**: `#child savings accounts`, `#fiscal policy`, `#US Treasury`, `#Elon Musk`, `#Trump Account`

---