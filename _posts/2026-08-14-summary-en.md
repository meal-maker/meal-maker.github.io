---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 40 items, 17 important content pieces were selected

---

**Technology News**
1. [Qwen 3.8 27B FP8 Shows Strong Local Reasoning but Efficiency Caveats](#item-tech-news-1) ⭐️ 8.0/10
2. [Google Announces Practical Private AI with Homomorphic Encryption](#item-tech-news-2) ⭐️ 8.0/10
3. [Firefox Now Last Major Browser Supporting uBlock Origin](#item-tech-news-3) ⭐️ 8.0/10
4. [Xiaohongshu Opens 280B MoE dots3-note with 16B Active Params](#item-tech-news-4) ⭐️ 8.0/10
5. [PostgreSQL Fixes Critical to\_char Vulnerability Enabling Arbitrary Code Execution](#item-tech-news-5) ⭐️ 8.0/10
6. [Apple trains China-specific AI model with Alibaba support, may be first approved foreign firm](#item-tech-news-6) ⭐️ 8.0/10
7. [RustDesk now supports true unattended remote access on Wayland](#item-tech-news-7) ⭐️ 7.0/10
8. [GLM-5.3 Frontier Coding Model Reported for Cyber Research](#item-tech-news-8) ⭐️ 7.0/10
9. [Hallucinate Tags, Then Match Them With Vector Embeddings](#item-tech-news-9) ⭐️ 7.0/10
10. [Vivodyne Scales AI-Run Human Tissue Testing to 3 Million Samples](#item-tech-news-10) ⭐️ 7.0/10
11. [US Judge Orders Google to Remove Third-Party App Store Install Friction](#item-tech-news-11) ⭐️ 7.0/10

**Technology Blog**
1. [Adaptive Verification in vLLM: DSpark Confidence-Scheduled Verification](#item-tech-blog-1) ⭐️ 9.0/10

**Financial News**
1. [Berkshire Hathaway boosts Alphabet to top-three holding and ends 14-quarter net selling streak](#item-finance-news-1) ⭐️ 8.0/10
2. [Goldman Sachs profits from AI infrastructure financing wave with Nvidia, Intel and Alphabet deals](#item-finance-news-2) ⭐️ 8.0/10
3. [CFTC reviews &\#x27;mention markets&\#x27; as states and banks tighten scrutiny](#item-finance-news-3) ⭐️ 7.0/10
4. [Uber and Pony.ai to deploy 2,000 robotaxis across Europe](#item-finance-news-4) ⭐️ 7.0/10
5. [Trustar Capital Nears Over $1.5 Billion Deal for Alibaba’s Lingxi Gaming Unit](#item-finance-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Qwen 3.8 27B FP8 Shows Strong Local Reasoning but Efficiency Caveats](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 3.8 27B is a newly released open-weight FP8 model on Hugging Face that early community evaluations describe as strong at local reasoning. In one private benchmark it became only the second local model after Gemma 4 to reason correctly, although it used five times as many tokens and took 12 minutes 30 seconds with MTP enabled, and commenters reported less efficient VRAM usage than Gemma 4 or Glimmer. Another tester noted it produced the best pelican-on-a-bicycle drawing among models that run on a laptop, including correct beak and leg placement. Commenters also flagged a distinctive terse &quot;caveman&quot; thinking style compared with Qwen 3.6, with one speculating it may interfere with MTP predictions, and noted that Jinja templates need adjustment.

hackernews · erdaltoprak · Aug 14, 15:00 · [Discussion](https://news.ycombinator.com/item?id=49299605)

**「Background」** Qwen 3.8 27B is an open-weight 27-billion-parameter language model distributed in FP8 format, which roughly halves VRAM compared to BF16, needing about 27GB for full precision on a 48GB GPU or 14–16GB with 4-bit quantization on a 24GB card. It follows the earlier Qwen3.6-27B, which natively supports a 262,144-token context extensible to 1,010,000 tokens. Early third-party coverage describes Qwen3.8-27B as a consistent upgrade over Qwen3.6-27B rather than an isolated benchmark spike.

**「Impact」** For AI practitioners running local inference, Qwen 3.8 27B offers near-frontier reasoning on laptop-class hardware but with higher token usage, longer generation times, and less efficient VRAM than competing local models such as Gemma 4.

**「Community Discussion」** Early commenters are impressed by its reasoning and local image generation, but several note high token usage, suboptimal VRAM efficiency, and broken Jinja templates, while one user suspects the terse &quot;caveman&quot; thinking style may reduce MTP prediction quality.

<details><summary>References</summary>
<ul>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B-FP8">Qwen/Qwen3.6-27B-FP8 · Hugging Face</a></li>
<li><a href="https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/">Qwen3.8-27B: Specs, Benchmarks &amp; Verdict</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#Qwen`, `#inference`

---

<a id="item-tech-news-2"></a>
### [Google Announces Practical Private AI with Homomorphic Encryption](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 8.0/10

Google published a blog post announcing efforts to make private AI practical using homomorphic encryption. The announcement addresses a key challenge in privacy-preserving machine learning by allowing computations on encrypted data. The available source material does not include specific implementation details or performance benchmarks.

hackernews · u1hcw9nx · Aug 14, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49300314)

**「What is homomorphic encryption?」** Homomorphic encryption \(HE\) allows computation on encrypted data without decrypting it, enabling a model to process private inputs and return encrypted outputs that only the data owner can read. Historically, HE has imposed heavy computational overhead, but recent frameworks and tools such as Google&\#x27;s HEIR aim to reduce this cost by converting pre-trained AI models to operate on encrypted inputs. Understanding this overhead and the ongoing effort to lower it is key to evaluating claims that private AI is becoming practical.

**「Impact」** If Google overcomes the current high computational overhead of homomorphic encryption, it could enable privacy-preserving AI inference in cloud services, but commenters note that overhead is currently around 10^3 on inference tasks, making commercial viability uncertain.

**「Community Discussion」** Hacker News commenters shared a free FHE textbook, noted that homomorphic encryption has very high overhead \(~10^3\) on inference and is not yet commercially viable, criticized Google&\#x27;s anti-privacy practices, and raised concerns about increased energy use; one commenter suggested the approach could help Google compete even with inferior models if true.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/">How Google is Making Private AI Practical with Homomorphic Encryption</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2949948825000289">Encrypted intelligence: A comparative analysis of homomorphic encryption frameworks for privacy-preserving AI - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#homomorphic-encryption`, `#privacy`, `#AI`, `#machine-learning`, `#Google`

---

<a id="item-tech-news-3"></a>
### [Firefox Now Last Major Browser Supporting uBlock Origin](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 8.0/10

Firefox has become the last major browser to offer full support for the uBlock Origin extension as Google Chrome transitions to its Manifest V3 extension framework. This change reduces the effectiveness of content blockers in Chromium-based browsers, though community members point out that Brave still enables Manifest V2 extensions through a flag and that Microsoft Edge lists uBlock Origin in its store. Firefox is noted for reviewing uBlock Origin&\#x27;s code with each update as part of its Recommended Extensions program. The shift is seen as a limitation on browser extension freedom, with some commentators stating that ad removal from Google Search is now only possible in Firefox.

hackernews · DemiGuru · Aug 14, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49303202)

**「Background: uBlock Origin and Manifest V3」** uBlock Origin is a free, open-source content-filtering and ad-blocking browser extension available for Firefox and Chromium-based browsers. Chrome, Edge, and other Chromium browsers are transitioning to Manifest V3, an extension platform change that limits the blocking capabilities relied on by extensions such as uBlock Origin. Firefox continues to support the older Manifest V2 APIs and has confirmed it will keep fully supporting uBlock Origin, which is why it is described as the last major browser to do so.

**「Consequence for users」** Chromium users who depend on uBlock Origin will see weaker ad and tracker blocking under Manifest V3, with full capability retained only in Firefox; Brave&\#x27;s hosted version and Edge&\#x27;s listing provide partial workarounds.

**「Community Discussion」** Commenters dispute the &\#x27;last major browser&\#x27; claim, noting that Brave can re-enable Manifest V2 extensions via a flag and that Microsoft Edge still lists uBlock Origin. Others emphasize Firefox&\#x27;s unique vetting of uBlock Origin&\#x27;s code and argue that Manifest V3 represents a loss of extension freedom, with one user stating that ad removal from Google Search is now only possible in Firefox.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html">Firefox is now the last major browser that still supports uBlock Origin</a></li>
<li><a href="https://9to5windows.com/firefox-last-major-browser-supporting-ublock-origin/">Firefox Confirms It Remains the Last Major Browser Supporting ...</a></li>
<li><a href="https://factually.co/fact-checks/technology/ublock-origin-features-lost-under-manifest-v3-privacy-impact-8c0ddb">What uBlock Origin Features Are Lost Under Manifest V3...</a></li>
<li><a href="https://factually.co/fact-checks/technology/manifest-v3-ad-blockers-ublock-origin-brave-firefox-2026-4deb07">How Manifest V3 Changed Ad Blockers: uBlock Origin, Br...</a></li>

</ul>
</details>

**Tags**: `#browser-extensions`, `#ad-blocking`, `#privacy`, `#Manifest V3`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [Xiaohongshu Opens 280B MoE dots3-note with 16B Active Params](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

Xiaohongshu Dots Lab released dots3-note preview, the first open-weight model in the dots3 series, with 280B total parameters and 16B active parameters. It supports a 512K context window and can process text, images, video, and audio. The model introduces TEMPO, a reinforcement learning method that trains long-horizon agents using self-criticism and test-time value estimation. Weights are available on Hugging Face, along with two real-world agent benchmarks: VibeSearchBench and VibeLifeBench.

telegram · zaihuapd · Aug 14, 08:27

**「Background」** Mixture-of-experts \(MoE\) models use many total parameters but activate only a subset per token, reducing inference cost while retaining capacity; dots3-note preview has 280B total parameters with 16B active, based on 256 routed experts plus one shared expert with top-8 routing across 1 dense and 45 MoE layers. It is the first open-weight release in the dots3 family and supports a 512K-token context for text, vision, and audio inputs. TEMPO is introduced as a new reinforcement learning method for training long-horizon agents via self-critique and test-time value estimation.

**「Impact」** Developers and researchers now have open access to a multimodal MoE with 16B active parameters and 512K context, potentially enabling lower-cost inference for long-horizon agent experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/dots-studio/dots3-note-prev">dots-studio/dots3-note-prev · Hugging Face</a></li>
<li><a href="https://www.orcarouter.ai/blog/dots-note-3-0-leak">dots-note-3.0 Leak: vLLM PR Reveals the IMO-Perfect Model</a></li>
<li><a href="https://x.com/BanghuaZ/status/2088088521882140734">Banghua Zhu on X: &quot;The first language model from Rednote dots studio lab! (Yes, rednote from China is also starting to release open model lol.)&quot; / X</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#large language model`, `#MoE`, `#multimodal`, `#AI agents`

---

<a id="item-tech-news-5"></a>
### [PostgreSQL Fixes Critical to\_char Vulnerability Enabling Arbitrary Code Execution](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL disclosed CVE-2026-14669, a high-severity heap buffer overflow in the to\_char\(timestamptz\) function that occurs when processing overly long POSIX time zone abbreviations. The flaw can allow a database user with permission to set the time zone to execute arbitrary code with the operating-system privileges of the PostgreSQL server process; it has a CVSS score of 8.8 and requires a low-privileged database account, not unauthenticated access. The project fixed the issue in minor releases 18.6, 17.11, 16.15, 15.19, and 14.24, with users on 18.x advised to upgrade directly to 18.6 because 18.5 was not officially released due to a regression. Applying the minor update only requires replacing program files and restarting the service, without dumping the database or running pg\_upgrade.

telegram · zaihuapd · Aug 14, 14:35

**「Background」** PostgreSQL&\#x27;s to\_char function formats timestamps, and when used with timestamptz it can handle POSIX time-zone abbreviations. A heap buffer overflow occurs when a program writes past an allocated memory buffer, potentially allowing an attacker to overwrite adjacent memory and hijack execution. PostgreSQL issues minor releases for supported major versions to deliver security fixes without requiring a full database migration.

**「Impact」** PostgreSQL deployments on affected versions should apply the corresponding minor update and restart the service, because any low-privileged user who can set the time zone could run arbitrary code with the server process&\#x27;s OS privileges.

**Tags**: `#PostgreSQL`, `#security vulnerability`, `#CVE`, `#database`, `#arbitrary code execution`

---

<a id="item-tech-news-6"></a>
### [Apple trains China-specific AI model with Alibaba support, may be first approved foreign firm](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

Reuters reports, citing people familiar with the matter, that Apple has trained its own China-specific large language model with Alibaba&\#x27;s support, moving away from its earlier reliance on third-party models. China&\#x27;s Cyberspace Administration of China filed the generative AI service for the record last month. Apple Intelligence is expected to launch in China through iOS updates in the coming months. If the rollout proceeds, Apple could become the first foreign company approved by Beijing to offer its own AI model in China.

telegram · zaihuapd · Aug 14, 14:47

**「Background」** China requires generative AI services to obtain regulatory approval from the Cyberspace Administration of China before public release, and foreign providers often partner with local companies to meet data and content requirements. Apple has previously relied on third-party AI models for its China services rather than offering its own model. According to the reported arrangement, Apple owns the custom large language model while Alibaba provided training support and local expertise.

**「Impact」** The expected iOS rollout would shift China AI services on Apple devices from third-party models to Apple&\#x27;s own model, giving Apple direct control over the experience while it operates under CAC filing requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://qz.com/apple-china-ai-model-alibaba-training-081426">Apple trains China -specific AI model with Alibaba &#x27;s help</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#China`, `#Alibaba`, `#AI`, `#LLM`, `#Regulatory`

---

<a id="item-tech-news-7"></a>
### [RustDesk now supports true unattended remote access on Wayland](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk has added support for true unattended remote access on Wayland, resolving a major limitation that previously hindered remote Linux administration. The change addresses the security model of Wayland, which had made unattended remote desktop access difficult for open-source remote desktop tools. The announcement highlights this as an important step for systems administrators and Linux users who rely on RustDesk for remote management.

hackernews · rustdesk · Aug 14, 16:12 · [Discussion](https://news.ycombinator.com/item?id=49300759)

**「Why Wayland made unattended remote access difficult」** Wayland is a modern Linux display server protocol that isolates applications from each other and from the display server, so remote desktop tools cannot capture screen or input without user consent through portals or libei. RustDesk is an open-source remote desktop application that previously required a local user to accept a sharing dialog, which prevented unattended remote administration on Wayland. The new support eliminates that requirement and works for multi-monitor setups.

**「Impact」** System administrators and Linux users running Wayland can now use RustDesk for genuine unattended remote access, closing a notable gap in open-source remote desktop tooling.

**「Community Discussion」** Comments are largely positive, with users welcoming the fix. One commenter notes that RustDesk still lacks encrypted connections when self-hosting \(issue \#3714\), while others ask how it compares to VNC for specific use cases or to SSH-based tools like Remmina.

<details><summary>References</summary>
<ul>
<li><a href="https://rustdesk.com/blog/unattended-remote-access-wayland/">Unattended Remote Access on Wayland with RustDesk — RustDesk</a></li>
<li><a href="https://github.com/rustdesk/rustdesk/discussions/10016">Wayland : Select the screen to be shared (Operate on the peer side)...</a></li>

</ul>
</details>

**Tags**: `#rustdesk`, `#wayland`, `#remote-desktop`, `#open-source`, `#linux`

---

<a id="item-tech-news-8"></a>
### [GLM-5.3 Frontier Coding Model Reported for Cyber Research](https://z.ai/blog/glm-5.3) ⭐️ 7.0/10

GLM-5.3 is a newly introduced frontier coding model from Z.AI that is drawing developer attention for reported cybersecurity research capabilities. The official announcement highlights coding performance and links to a coordinated vulnerability disclosure portal \(cvd.z.ai\) where Z.AI reports vulnerabilities found at scale in open-source and popular software, many under embargo and rated critical or high. Community reports describe using the model with the Claude Code harness to execute red-team scenarios such as WordPress plugin 0-days, RCE, and a 6.8 kernel exploit adaptation while playing against another GLM agent as defender. Initial user impressions place it just behind Sol and Fable on some benchmarks and describe it as likely GLM 5.2 with post-training improvements, with full weights expected about two weeks after release. The headline&\#x27;s &\#x27;emergent cyber capabilities&\#x27; may overstate verified results, as much of the evidence is from early user reports and an embargoed disclosure list.

hackernews · pella · Aug 14, 05:19 · [Discussion](https://news.ycombinator.com/item?id=49294997)

**「Context」** GLM-5.3 is an update to Z.ai&\#x27;s GLM large language model series, released on August 14, 2026. According to Z.ai, it retains the same base model as GLM-5.2 and achieves its improvements through scaled-up post-training rather than a new pretrained architecture. The model is open-weights and is reported to show strong coding benchmark results, with the company saying cyber capabilities emerged faster than expected during post-training.

**「Impact」** Security researchers and developers evaluating GLM-5.3 may use it for offensive testing and coordinated vulnerability disclosure, but should independently verify its &\#x27;emergent cyber capabilities&\#x27; and the embargoed CVEs before relying on them.

**「Community Discussion」** Commenters report strong red-team performance with GLM-5.3 via the Claude Code harness, including WordPress plugin 0-days and kernel exploit adaptation, and note Z.AI&\#x27;s cvd.z.ai portal lists many embargoed high/critical CVEs; some question how falling scan costs will affect disclosure norms. Others compare it slightly below Sol and Fable and argue there is still no compelling economic reason to switch from OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.unite.ai/z-ai-launches-glm-5-3-with-frontier-coding-and-a-cyber-capability-that-outgrew-its-training/">Z.ai Launches GLM-5.3 With Frontier Coding and a Cyber Capability That Outgrew Its Training – Unite.AI</a></li>
<li><a href="https://www.reddit.com/r/singularity/comments/1vnz30c/glm_53_released_frontier_coding_with_emergent/">r/singularity on Reddit: GLM 5.3 released: Frontier Coding with Emergent Cyber Capabilities</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#cybersecurity`, `#software engineering`, `#GLM`

---

<a id="item-tech-news-9"></a>
### [Hallucinate Tags, Then Match Them With Vector Embeddings](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison spotlights Doug Turnbull&\#x27;s approach to tagging content when the existing vocabulary is too large to include in an LLM prompt. The method asks the model to generate novel plausible tags without seeing the full tag list, optionally using examples of tag structure to guide the guesses. Those imagined tags are then matched against the existing corpus of tags using vector embeddings and similarity search, so the nearest real tag becomes the assigned classification. This avoids needing to feed an LLM all 1,856 tags on Willison&\#x27;s blog while still producing valid, existing tags.

rss · Simon Willison · Aug 14, 21:54

**「Background」** Vector embeddings are numerical representations of text that place semantically similar phrases close together, enabling nearest-neighbor matching. For automatic tagging, a common problem is that large existing tag vocabularies may exceed an LLM&\#x27;s context window or be costly to include in each prompt. The technique described here bypasses that constraint by separating candidate generation from vocabulary matching.

**「Impact」** Developers managing large tag taxonomies can use this generative-then-match workflow to reduce prompt size and still map free-form model output to existing tags, instead of attempting to supply every possible tag.

**Tags**: `#large language models`, `#vector embeddings`, `#tagging`, `#information retrieval`, `#prompt engineering`

---

<a id="item-tech-news-10"></a>
### [Vivodyne Scales AI-Run Human Tissue Testing to 3 Million Samples](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 7.0/10

Vivodyne has built 12 wardrobe-sized &\#x27;hive&\#x27; robotic laboratories south of San Francisco that culture human tissues and use AI to design experiments for predicting drug efficacy and safety. The system can run controlled tests on more than 3 million human tissues per year, which the company says is twice the capacity of all U.S. clinical trials combined. This comes as about 90% of clinical trials still fail after passing animal tests, and the platform may help reduce reliance on animal testing. These figures are company-reported and have not yet been clinically validated.

telegram · zaihuapd · Aug 14, 01:48

**「Context」** Vivodyne is a biotech company that uses robotic automation and AI to grow and test intact human tissues outside the body, aiming to generate human-equivalent data before clinical trials. Traditional drug development relies heavily on animal models, yet about 90% of clinical trials fail after passing animal testing. The company&\#x27;s system can reportedly grow and test over 100,000 human tissues within two weeks, and Vivodyne has raised $40 million to advance this approach.

**「Impact」** If validated, Vivodyne&\#x27;s automated human-tissue testing could substantially increase preclinical throughput for pharmaceutical R&amp;D and reduce animal testing, but its predictive benefit remains unproven outside company-reported results.

<details><summary>References</summary>
<ul>
<li><a href="https://discover-pharma.com/vivodyne-raises-40m-to-advance-human-tissue-testing-as-alternative-to-animal-models/">Vivodyne raises $40M to advance human tissue testing as...</a></li>
<li><a href="https://www.businesswire.com/news/home/20250528498236/en/Vivodyne-to-Replace-Animal-Testing-With-$40-Million-Funding-to-Reverse-95-Clinical-Trial-Failure-Rate">Vivodyne to Replace Animal Testing With $40 Million Funding to...</a></li>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biotech`, `#lab automation`, `#drug discovery`, `#robotics`

---

<a id="item-tech-news-11"></a>
### [US Judge Orders Google to Remove Third-Party App Store Install Friction](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

US District Judge James Donato ordered Google to simplify installation of rival Android app stores by removing extra steps and warning popups in the Play Store within one week. The court found that multi-step flows such as requiring users to tap &\#x27;View&\#x27; before &\#x27;Install&\#x27; were deliberate anti-competitive friction designed to deter ordinary users. The ruling stems from Epic v. Google, where a jury previously found Google illegally monopolized Android app distribution. Google must make installing third-party app markets as direct as installing a standard Android app.

telegram · zaihuapd · Aug 14, 09:55

**「Background」** Epic v. Google is an antitrust lawsuit in which Epic Games challenged Google&\#x27;s control over Android app distribution through the Play Store. A jury found that Google illegally maintained a monopoly, and the court is now imposing remedies to restore competition.

**「Impact」** Google must complete the Play Store changes within one week to remove the extra warning and confirmation steps for third-party app store installations, reducing friction for rival stores and aligning the process with ordinary app installs.

**Tags**: `#antitrust`, `#android`, `#google-play`, `#epic-v-google`, `#app-stores`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Adaptive Verification in vLLM: DSpark Confidence-Scheduled Verification](https://vllm.ai/blog/2026-08-14-dspark-adaptive-verification) ⭐️ 9.0/10

rss · vLLM Blog · Aug 14, 00:00

**「Background」** Speculative decoding trades extra compute for fewer decode steps, nearly free at low batch sizes when the GPU is memory-bound, but at high concurrency rejected draft tokens waste compute and reduce throughput. The vLLM team argues that no static num\_speculative\_tokens is optimal across concurrencies because acceptance rates vary with load and workload.

**「Solution」** DSpark replaces the static speculation length with a per-step adaptive draft budget. A learned confidence head emits a confidence per drafted position; the scheduler converts these to survival probabilities and selects the best B draft slots globally across requests, maximizing expected tokens per unit step time using a profiled cost table \(verification cost indexed by token count and drafter cost by request count\). Sizing runs on CPU while the GPU finishes the previous step, and allocation runs on GPU using current confidences via a Triton-lowered PyTorch kernel, never reading back to host. Varlen decode CUDA graphs support variable-sized verifications, relying on sparse MLA and DeepGEMM varlen indexer kernels. In benchmarks on DeepSeek-V4-Pro-0813 \(TP=8 on B300, concurrency 1–256\), adaptive verification stays on the Pareto frontier, acting like a long fixed block at low concurrency and a short one at high concurrency. The authors note limitations: FULL varlen decode graphs require SM100 attention support, and enforce-eager, LoRA, pipeline parallelism, and output logprobs are unsupported.

**「Takeaway」** DSpark’s confidence-scheduled verification makes speculative decoding beneficial across a wide concurrency range without per-deployment tuning, reducing the need for users to set num\_speculative\_tokens and moving it toward an on-by-default feature.

**Tags**: `#speculative-decoding`, `#vLLM`, `#cuda-graphs`, `#adaptive-verification`, `#LLM-inference`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Berkshire Hathaway boosts Alphabet to top-three holding and ends 14-quarter net selling streak](https://www.cnbc.com/2026/08/14/berkshire-hathaway-boosts-alphabet-to-a-top-three-holding-ups-delta-and-housing-bets.html) ⭐️ 8.0/10

Berkshire Hathaway&\#x27;s latest 13F filing shows it became a net buyer of equities after 14 straight quarters of net sales, with nearly $20 billion in net purchases, and boosted its Alphabet stake by 83% to $37.9 billion.

rss · CNBC Finance · Aug 14, 21:06

**「Background」** The Alphabet increase largely reflects a $10 billion private stock purchase announced in early June, when Alphabet sought capital for its AI infrastructure buildout.

**Tags**: `#Berkshire Hathaway`, `#Alphabet`, `#13F filing`, `#equity holdings`, `#Warren Buffett`

---

<a id="item-finance-news-2"></a>
### [Goldman Sachs profits from AI infrastructure financing wave with Nvidia, Intel and Alphabet deals](https://www.cnbc.com/2026/08/14/goldmans-latest-cash-cow-is-all-about-funding-the-ai-infrastructure-boom.html) ⭐️ 8.0/10

Goldman Sachs is profiting from a wave of AI infrastructure financing; according to company announcements, it helped arrange Nvidia&\#x27;s $500 billion financing plan, served as joint book-running manager on Intel&\#x27;s upsized $20 billion stock offering, and helped steer Alphabet&\#x27;s $85 billion stock sale announced in June.

rss · CNBC Finance · Aug 14, 20:05

**「Background」** As a joint book-running manager, Goldman buys shares from issuers at a discount and resells them to institutional clients; the difference, known as the gross spread, is split into underwriting, management, and selling fees and flows to its Equity Capital Markets team.

**Tags**: `#Goldman Sachs`, `#AI infrastructure`, `#investment banking`, `#Nvidia`, `#Intel`

---

<a id="item-finance-news-3"></a>
### [CFTC reviews &\#x27;mention markets&\#x27; as states and banks tighten scrutiny](https://www.cnbc.com/2026/08/14/prediction-markets-scrutiny-mounts-from-regulators-and-banks.html) ⭐️ 7.0/10

The CFTC is conducting an internal review into &\#x27;mention markets&\#x27; on prediction platforms, people familiar with the matter told CNBC; a Washington state judge blocked several Kalshi markets Thursday, and the Financial Times reported JPMorgan cut off Polymarket last October, a claim Polymarket disputes. Mention markets had about $3.3 million in trading volume on Kalshi last month, according to Dune Analytics.

rss · CNBC Finance · Aug 14, 19:21

**「Background」** Mention markets let traders bet on whether chosen words appear in speeches, earnings calls, or broadcasts, and critics say they are easily manipulated; the CFTC is separately investigating a former Trump teleprompter operator who allegedly made $90,000 in profits on Kalshi.

**Tags**: `#prediction markets`, `#CFTC`, `#regulation`, `#Kalshi`, `#Polymarket`

---

<a id="item-finance-news-4"></a>
### [Uber and Pony.ai to deploy 2,000 robotaxis across Europe](https://www.cnbc.com/2026/08/14/uber-partners-with-chinas-ponyai-for-2000-robotaxis-in-europe.html) ⭐️ 7.0/10

Uber and Pony.ai announced Friday that they plan to deploy 2,000 of Pony.ai’s self-driving taxis across Europe and expand their robotaxi partnership to the Middle East.

rss · CNBC Finance · Aug 14, 01:02

**「Background」** The companies launched a commercial robotaxi service in Zagreb, Croatia, in late March, which they claim was the first in Europe; Friday’s plan adds four other European cities but does not name them or give an exact timeframe.

**「Impact」** The expansion increases competition in Europe’s autonomous ride market, where Alphabet-backed Waymo has about 5,000 vehicles globally and Chinese rivals Baidu Apollo Go and WeRide are also ramping up plans.

**Tags**: `#Uber`, `#Pony.ai`, `#robotaxis`, `#autonomous vehicles`, `#Europe`

---

<a id="item-finance-news-5"></a>
### [Trustar Capital Nears Over $1.5 Billion Deal for Alibaba’s Lingxi Gaming Unit](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 7.0/10

Bloomberg reports that CITIC-backed Trustar Capital is close to acquiring Alibaba&\#x27;s Lingxi gaming business at a valuation of more than $1.5 billion, though talks are ongoing and no final decision has been made.

telegram · zaihuapd · Aug 14, 10:24

**「Background」** Alibaba has been shedding non-core assets under CEO Eddie Wu to focus on AI and cloud computing; Lingxi&\#x27;s flagship title is the strategy game Three Kingdoms Strategic Edition, developed with Koei Tecmo.

**Tags**: `#M&amp;A`, `#Alibaba`, `#CITIC Group`, `#gaming`, `#private equity`

---