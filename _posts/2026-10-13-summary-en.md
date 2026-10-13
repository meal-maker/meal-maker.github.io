---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 42 items, 16 important content pieces were selected

---

**Technology News**
1. [Hackers activate automatic defrosting in supermarket fridges across Europe](#item-tech-news-1) ⭐️ 8.0/10
2. [WiFi 7 Router Repurposed as 320Msps SDR Receiver](#item-tech-news-2) ⭐️ 8.0/10
3. [Python 3.15 Released: Lazy Imports, New Profiler, 3.10 Retired](#item-tech-news-3) ⭐️ 8.0/10
4. [Looped Diffusion Transformer Runs Same Blocks Several Times Per Denoising Step](#item-tech-news-4) ⭐️ 8.0/10
5. [A Modern Web App in C](#item-tech-news-5) ⭐️ 7.0/10
6. [Codex CLI installs persistent self-updating daemon by default](#item-tech-news-6) ⭐️ 7.0/10
7. [Meta Muse Wonder Model Release Triggers Privacy and Performance Concerns](#item-tech-news-7) ⭐️ 7.0/10
8. [U-Space: Single-Pass Label-Free Uncertainty Scoring for Reasoning LLMs](#item-tech-news-8) ⭐️ 7.0/10
9. [learnc tunes C constants for 9.1% smaller JPEGs, VAD F1 gain](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic Says New Defenses Cut Distillation Extraction 90–99%](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [China-EU reach consensus on hybrid and electric vehicle trade, China quota not below other sources](#item-finance-news-1) ⭐️ 8.0/10
2. [China to cut new energy vehicle export VAT rebate to 9% from 2027](#item-finance-news-2) ⭐️ 8.0/10
3. [Cleveland Fed&\#x27;s Hammack says restrictive policy may be needed with PCE at 3.4%](#item-finance-news-3) ⭐️ 7.0/10
4. [Rebuilt Huanggang Port opens with faster joint customs clearance](#item-finance-news-4) ⭐️ 7.0/10
5. [DeepSeek Reportedly to Lead Seed Round for Former Tencent Scientist&\#x27;s Robotics Startup at $400 Million Valuation](#item-finance-news-5) ⭐️ 7.0/10
6. [China sets new tax penalty standards from November 2026, with social insurance arrears fines up to 3x](#item-finance-news-6) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Hackers activate automatic defrosting in supermarket fridges across Europe](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

A cyberattack on commercial refrigeration systems across Europe activated automatic defrosting and disrupted supermarket operations. The incident affected French chain Intermarché, with reports citing up to 150 stores targeted, and also impacted delivery and store pricing. Security researchers from Claroty Team82 had previously uncovered vulnerabilities in legacy Danfoss controllers such as the SM800 \(end-of-support 2021\) and SC355 \(end-of-support 2016\), which are suspected in this incident. The attack highlights the risk of internet-connected industrial control systems in retail, where these devices often remain unpatched. A similar suspected incident at US military base freezers in late August 2026 may be related, though no attribution has been confirmed.

hackernews · Zeekaas · Oct 12, 12:16 · [Discussion](https://news.ycombinator.com/item?id=50055304)

**「Background」** Commercial refrigeration controllers are increasingly networked to enable remote diagnostics, defrost scheduling, and energy management, but many remain connected after vendor support ends. The August 2026 suspected compromise of US military commissary freezers drew attention to Danfoss devices, and Claroty Team82 later published research on their vulnerabilities.

**「Impact」** The attack forced refrigeration shutdowns and defrost cycles at affected European supermarkets, threatening food safety and disrupting deliveries and store pricing.

**「Community Discussion」** Commenters questioned why refrigeration units need internet access, while others explained that remote diagnostics, energy efficiency, and subscription-based lab equipment create business pressure to connect legacy controllers. Several noted a possible link to the August 2026 US military base freezer incident involving similar Danfoss hardware, but no confirmation was provided.

**Tags**: `#cybersecurity`, `#industrial-control-systems`, `#IoT`, `#vulnerability`, `#retail-technology`

---

<a id="item-tech-news-2"></a>
### [WiFi 7 Router Repurposed as 320Msps SDR Receiver](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

A GitHub project called w1700k-sdr demonstrates how to turn a WiFi 7 router into a 320 Msps software-defined radio receiver. The technique repurposes the router&\#x27;s WiFi 7 radio hardware to capture wideband RF signals, offering a low-cost alternative to dedicated high-bandwidth SDR receivers. Because 320 Msps receivers at 5 GHz are typically expensive, this approach is notable for enabling budget RF experimentation and hardware hacking. The project&\#x27;s novel repurposing has drawn attention from the hardware hacking and SDR community as a practical route to high-sample-rate reception.

hackernews · djfergus · Oct 12, 12:41 · [Discussion](https://news.ycombinator.com/item?id=50055593)

**「Background」** Software-defined radio \(SDR\) replaces traditional analog RF components with software processing, allowing flexible reception across a range of frequencies. The project uses the MediaTek MT7996 Wi-Fi 7 radio chip found in the Gemtek W1700K router, which can capture raw 14-bit I/Q samples at up to 320 Msps, while the Airoha AN7581 SoC streams that data over 10 GbE to a Linux host for real-time spectrum display. Previously, exposing such high-rate raw I/Q from a commodity Wi-Fi chipset over Ethernet was not commonly available, making this a notable low-cost approach for wideband RF experimentation.

**「Impact」** SDR enthusiasts and hardware hackers can potentially use compatible WiFi 7 routers as an inexpensive 320 Msps 5 GHz receiver instead of purchasing dedicated equipment, though compatibility with specific router models and firmware modifications may limit practical use. Real-world performance and supported hardware remain to be fully demonstrated.

**「Community Discussion」** Commenters praised the developer&\#x27;s previous ESP32-based SDR project and noted that the same chipset likely means this approach can work on the Banana Pi R4. Some discussed adding attenuators, filters, and a mixer to build a service monitor, while another wondered whether similar capabilities explain why phone manufacturers restrict third-party access to FM radios.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/h0m3us3r/w1700k-sdr">GitHub - h0m3us3r/w1700k-sdr</a></li>
<li><a href="https://zeli.app/story/50055593">Wi-Fi 7 router turned into a 320 Msps · 56 HN comments | Zeli</a></li>
<li><a href="https://hackaday.com/2026/10/12/wifi-router-does-software-defined-radio/">WiFi Router Does Software-Defined Radio | Hackaday</a></li>

</ul>
</details>

**Tags**: `#software-defined-radio`, `#wifi-7`, `#hardware-hacking`, `#open-source`, `#rf-systems`

---

<a id="item-tech-news-3"></a>
### [Python 3.15 Released: Lazy Imports, New Profiler, 3.10 Retired](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 is now available, with release manager Hugo van Kemenade curating the official What&\#x27;s New guide. The release introduces explicit lazy imports via \`lazy import\` and \`lazy from ... import\` \(PEP 810\), unpacking syntax inside comprehensions \(PEP 798\), and a built-in sampling profiler called Tachyon \(\`profiling.sampling\`\) alongside the renamed \`profiling.tracing\` module. Benchmarks by Miguel Grinberg on 3.15.0rc3 show performance roughly equal to 3.14, except the experimental JIT improved a Fibonacci test by 1.2x. For open-source maintainers like Simon Willison, Python 3.15 means they can stop supporting Python 3.10 and adopt Python 3.11 features.

rss · Simon Willison · Oct 12, 18:15

**「Background」** Python now ships annual feature releases and supports each major version for about five years, so the arrival of 3.15 marks the end of support for Python 3.10. Lazy imports defer module loading until first use, reducing startup overhead for CLIs and plugins, and sampling profilers periodically capture stack traces to measure hot functions with low overhead.

**「Impact」** Developers maintaining cross-version Python libraries can drop 3.10 and start using syntax from Python 3.11, while CLI and plugin authors on 3.15 can replace manual deferred imports with native lazy imports to reduce startup time or use the built-in Tachyon sampler instead of third-party tools like py-spy.

**Tags**: `#python`, `#python-3.15`, `#pep-810`, `#lazy-imports`, `#software-engineering`

---

<a id="item-tech-news-4"></a>
### [Looped Diffusion Transformer Runs Same Blocks Several Times Per Denoising Step](https://www.reddit.com/r/MachineLearning/comments/1x49d61/looped_diffusion_transformer_the_same_blocks_run/) ⭐️ 8.0/10

Looped Diffusion Transformer \(arXiv 2609.40305, 30 Sep\) introduces a text-to-image DiT that runs a shared group of transformer blocks multiple times within each denoising step instead of adding more parameters. The authors report that naive looping is unreliable and address it with deep supervision on every loop and self-modulating attention; a 260M looped model reportedly beats a 6.5x larger model on several benchmarks while using 4.9x less inference compute, and at a fixed inference budget, more loop depth helps more than more denoising steps. The B/16 code and weights are MIT-licensed on Hugging Face under sensenova, and the model was trained at loop depth 4, with the README stating other depths work without retraining. A Reddit user tested on an M5 Pro using PyTorch MPS in fp32, 100 Euler steps, CFG 6.0, and one seed per prompt at loop depths 1 to 4, finding most change occurs before depth 3 and that depths 3 and 4 are very close on every shown prompt. Sampling time increased from about 23–24 seconds at depth 1 to 43–47 seconds at depth 4, and loop depth can be selected at inference time like iteration count in recurrent-depth language models.

reddit · r/MachineLearning · /u/Fit-Ant2238 · Oct 12, 18:13

**「Background」** Diffusion transformers \(DiTs\) replace the U-Net backbone in diffusion models with a transformer and are typically scaled by increasing blocks, parameters, and training compute. Looped or recurrent-depth models instead reuse a subset of layers multiple times, reducing memory and parameters while allowing the iteration depth to be adjusted at inference. The Looped Diffusion Transformer applies this recurrent execution inside each denoising step, but requires training modifications because naive layer reuse does not reliably improve performance.

**Tags**: `#diffusion models`, `#transformers`, `#generative AI`, `#efficiency`, `#machine learning`

---

<a id="item-tech-news-5"></a>
### [A Modern Web App in C](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 7.0/10

The post explains how to build a modern web application in C, covering CGI/FastCGI integration and deployment strategies. It emphasizes Unix security mechanisms such as pledge and chroot to drop privileges for each request-handling process. The approach offers a low-dependency alternative to framework-based stacks, but requires careful handling of memory safety and process lifecycle.

hackernews · prophittcorey · Oct 12, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50058528)

**「Historical Context」** Historically, dynamic web content in C was achieved via CGI, where a web server like Apache would fork a separate process for each request, executing a compiled binary in a cgi-bin directory. FastCGI later improved performance by using persistent processes. Modern approaches include the BCHS stack \(BSD, C, httpd, SQLite\) which uses managed C programs with security mechanisms such as pledge and chroot for privilege dropping, as demonstrated by the commercial product marketyour.games.

**「Impact」** For systems developers building lightweight or embedded web services, this post demonstrates that C with CGI/FastCGI can be a practical low-overhead option when combined with OS-level privilege restrictions.

**「Community Discussion」** Commenters generally affirm the technical points, citing BusyBox&\#x27;s built-in CGI support and a 22-year-old FastCGI business that ran well until it was rewritten in a Microsoft stack. Some prefer stateful Rust/SQLite backends over per-request C binaries because frameworks and easy backups are more important to them.

<details><summary>References</summary>
<ul>
<li><a href="https://upstract.com/x/ff7e87d60c67529f">A Modern Web App in C - upstract.com</a></li>
<li><a href="https://zeli.app/story/50058528">A Modern Web App in C · 153 HN comments | Zeli</a></li>

</ul>
</details>

**Tags**: `#c`, `#web-development`, `#systems-programming`, `#cgi`, `#open-source`

---

<a id="item-tech-news-6"></a>
### [Codex CLI installs persistent self-updating daemon by default](https://github.com/openai/codex/issues/48195) ⭐️ 7.0/10

Codex CLI installs a persistent, self-updating background daemon by default and currently has no documented off switch. A community workaround points to an undocumented feature flag in ~/.codex/config.toml under \[features\] daemon\_auto\_start = false. Users report the daemon can ruin file permissions and make .git read-only during auto-updates. One user measured about 12GB of disk usage from retained old versions, while another describes frequent random blocks. The CLI can be blocked from writing its pid/lock files by replacing them with symlinks to /dev/null and marking them unwritable.

hackernews · whimblepop · Oct 12, 18:29 · [Discussion](https://news.ycombinator.com/item?id=50060694)

**「Background」** Codex CLI is OpenAI&\#x27;s command-line coding agent, and since version 0.157.0, opening an interactive session starts a persistent background daemon \(\`codex app-server --managed-daemon\`\) by default. The daemon is self-updating and can be disabled in the user&\#x27;s \`~/.codex/config.toml\` by setting \`\[features\] daemon\_auto\_start = false\`.

**「Impact」** For developers using Codex CLI via npm, the default daemon can consume gigabytes of disk and cause permission changes, but disabling it requires an undocumented config flag or filesystem workarounds.

**「Community Discussion」** Several commenters express frustration over hidden auto-updating and bugs, with one noting it is alarming for an npm-installed CLI to behave this way; others suggest minimal alternatives like hax to avoid overengineered harnesses.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/48195">CLI: make ` daemon _ auto _ start ` opt-in — a persistent, self-updating...</a></li>

</ul>
</details>

**Tags**: `#openai`, `#codex`, `#cli`, `#developer-tools`, `#software-bugs`

---

<a id="item-tech-news-7"></a>
### [Meta Muse Wonder Model Release Triggers Privacy and Performance Concerns](https://research.meta.ai/blog/muse-wonder) ⭐️ 7.0/10

Meta announced Muse Wonder, a multimodal and code generation model, and Hacker News discussion centered on its benchmark claims versus real-world performance. One commenter found Muse Wonder&\#x27;s image-to-HTML output much worse than Opus 5.5, closer to Sonnet or Haiku, and suspected its vision model was underperforming despite strong published benchmarks. Another user reported that signing into the Muse Code site showed unrelated developers&\#x27; profiles and emails during authentication, with account settings inaccessible to deactivate the account. The model&\#x27;s release matters because it expands the number of frontier AI competitors, but mixed practical results and privacy reports dampen enthusiasm.

hackernews · meetpateltech · Oct 12, 16:48 · [Discussion](https://news.ycombinator.com/item?id=50059115)

**「Background」** Muse Wonder and Muse Wonder Full are newly announced Meta models described as its most capable for personal and professional agentic tasks. The Muse Wonder series reports state-of-the-art results on benchmarks for agentic, memory, and coding tasks, with the Full model topping DeepSWE and SWE-Marathon in independent third-party evaluations. Earlier Muse releases referenced in the discussion include Muse Spark 1.2 and Muse 1.3, which were also compared for image and code generation.

**「Impact」** Developers evaluating Muse Wonder should independently test image-to-HTML and coding tasks before relying on benchmark figures, and Meta account holders using Muse Code may face profile/email exposure to unrelated users.

**「Community Discussion」** Commenters generally welcomed more companies near the AI frontier to avoid power concentration but reported underwhelming real-world performance: an image-to-HTML test placed Muse Wonder below Opus 5.5 and closer to Sonnet or Haiku, contradicting its benchmark results. A separate user described a privacy issue where Muse Code sign-in displayed unrelated users&\#x27; profiles and emails while account settings were inaccessible.

<details><summary>References</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/10/introducing-muse-wonder-models/">Introducing Muse Wonder and Muse Wonder Full: Frontier Models ...</a></li>
<li><a href="https://research.meta.ai/blog/muse-wonder">Muse Wonder | Meta AI Research</a></li>
<li><a href="https://dev.meta.ai/models/muse-wonder">Muse Wonder | Meta</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#model release`, `#multimodal`, `#code generation`

---

<a id="item-tech-news-8"></a>
### [U-Space: Single-Pass Label-Free Uncertainty Scoring for Reasoning LLMs](https://www.reddit.com/r/MachineLearning/comments/1x44f9m/uspace_uncovering_when_and_why_uncertainty_arises/) ⭐️ 7.0/10

U-Space introduces a single-pass, label-free uncertainty score for open-weight reasoning models, computed as the hidden state&\#x27;s alignment with four &\#x27;doubt&\#x27; directions multiplied by mean token entropy over reasoning tokens. The method identifies uncertainty types including ambiguity, missing information, conflicting evidence, and general uncertainty. The authors report that it was the best estimator in a 3-seed, 3-model, 4-benchmark evaluation on Gemma 4, Qwen3.5, and Magistral, outperforming 5-pass, 10-pass, and supervised baselines. The only model-specific component is a Jacobian lens, with 40+ pre-fitted lenses available on Hugging Face and an option to fit new ones using roughly 100 unlabeled prompts.

reddit · r/MachineLearning · /u/AdRevolutionary3242 · Oct 12, 15:10

**「Background」** Uncertainty quantification for large language models often relies on multiple sampled generations, judge models, or labeled data, which can be computationally expensive. U-Space instead uses a single forward pass and hidden-state geometry from a Jacobian lens, a technique from Anthropic&\#x27;s global workspace research that maps hidden states to interpretable directions. This reduces the need for repeated sampling or supervised training while still producing a scalar confidence signal.

**「Impact」** Developers of open-weight reasoning models can obtain a reported best-in-class uncertainty estimate and uncertainty type in a single pass, potentially avoiding the cost of multi-pass sampling or supervised baselines when a suitable pre-fitted Jacobian lens is available or fitted with unlabeled data.

**Tags**: `#uncertainty-quantification`, `#large-language-models`, `#model-interpretability`, `#reasoning-models`, `#single-pass-inference`

---

<a id="item-tech-news-9"></a>
### [learnc tunes C constants for 9.1% smaller JPEGs, VAD F1 gain](https://www.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to/) ⭐️ 7.0/10

learnc is a tool that tunes named constants in unmodified C code against a user-written C score function and writes the same file back with new values. In held-out JPEG tests, tuning 128 quantization-table entries in stb\_image\_write.h on 12 Kodak images produced a 9.1% BD-rate improvement at equal SSIM on the remaining 12 Kodak images, verified independently in libjpeg with scikit-image; mozjpeg&\#x27;s tables achieved 2.7%. For Google&\#x27;s WebRTC VAD, tuning every constant in vad\_core.c on LibriParty dev lifted F1 from 0.810 to 0.859 on LibriParty eval. The tool is best suited for tens to hundreds of constants rather than large weight sets, and it shows no JPEG gain below 1 bpp. It is released under the MIT license at github.com/devanmolsharma/learnc.

reddit · r/MachineLearning · /u/keep\_up\_sharma · Oct 12, 20:51

**「Background」** C programs often contain named constants that act as tunable parameters for algorithms, such as quantization table entries in JPEG encoders or thresholds in voice activity detection. Manually adjusting these constants can be tedious and suboptimal, so automatic parameter tuning tools treat the program as a black box and optimize constants against a user-defined objective on data. The source describes learnc, one such tool that modifies the original source file directly, applying this approach to JPEG quantization tables and WebRTC VAD constants with held-out evaluation.

**「Impact」** For systems developers, learnc offers a practical auto-tuning path for existing C codebases, with measured held-out gains of 9.1% BD-rate on JPEG compression and +0.049 F1 on WebRTC VAD; its utility is constrained to tens-to-hundreds of constants and does not improve JPEG below 1 bpp.

**Tags**: `#C programming`, `#auto-tuning`, `#optimization`, `#JPEG`, `#WebRTC`

---

<a id="item-tech-news-10"></a>
### [Anthropic Says New Defenses Cut Distillation Extraction 90–99%](https://www.anthropic.com/research/distillation-defenses) ⭐️ 7.0/10

Anthropic reported on October 12 that preliminary evidence indicates its new protections have reduced data extraction from model distillation attacks aimed at stealing Claude capabilities by approximately 90–99%. The company says it has banned tens of thousands of related accounts, with some banned less than two hours after launching attacks. The defenses include restricting reasoning content from moving across sessions, models, and accounts, and deploying a two-stage classifier with ongoing patching of bypasses. The false positive rate is below 0.1%, but some developers need to update integrations, and intercepted requests may still be billed.

telegram · zaihuapd · Oct 13, 01:25

**「Background」** Model distillation lets developers train smaller models on outputs from a large model like Claude, sharply reducing the compute cost of obtaining frontier-level capabilities compared with training from scratch. Anthropic has previously accused labs such as DeepSeek, Moonshot, and MiniMax of using distillation to copy model capabilities, and the company warns that open-sourcing distilled models can spread those capabilities beyond government control.

**「Impact」** Developers relying on Claude APIs may need to update integrations and could still be charged for intercepted requests, while abusive accounts are being banned more quickly and extractable model output is sharply reduced.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-industry-has-data-problem-anthropic-just-made-ignore-dimitrova-5uvce">Who, What, How stole data from Anthropic</a></li>
<li><a href="https://news.smol.ai/issues/2026-02-23-anthropic-distillation/">Anthropic accuses DeepSeek, Moonshot, and MiniMax of... | AINews</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#LLM APIs`, `#abuse prevention`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China-EU reach consensus on hybrid and electric vehicle trade, China quota not below other sources](https://www.mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_4d502e1d49fd4480b39a6cfd0d752038.html) ⭐️ 8.0/10

China&\#x27;s Ministry of Commerce said China and the EU reached consensus on hybrid and electric vehicle trade, with a hybrid-car arrangement based on 2025 levels and adjusted upward, and a Chinese export quota no lower than other EU import sources; the EU will continue electric-vehicle price-commitment reviews.

telegram · zaihuapd · Oct 12, 06:19

**「Background」** The announcement came under the China-EU trade and investment consultation mechanism; price commitments are agreements in which exporters set minimum prices, and the EU will continue reviewing them for electric vehicles.

**Tags**: `#China-EU trade`, `#electric vehicles`, `#hybrid cars`, `#trade policy`, `#automotive industry`

---

<a id="item-finance-news-2"></a>
### [China to cut new energy vehicle export VAT rebate to 9% from 2027](https://www.news.cn/20261012/9709731f470b42f9a84825c2e4eb914b/c.html) ⭐️ 8.0/10

China will cut the VAT export rebate rate for new energy vehicles from 13% to 9% starting April 1, 2027, and will remove VAT export rebates for electronic cigarette devices, according to a Ministry of Finance and State Taxation Administration announcement.

telegram · zaihuapd · Oct 12, 11:00

**「Background」** The change comes as China phases out other tax benefits for new-energy vehicles: from January 1, 2027, vehicle and vessel tax reductions or exemptions for energy-saving cars and new-energy commercial vehicles are scheduled to end.

**「Impact on exporters」** From April 1, 2027, Chinese new-energy vehicle exporters will receive a lower VAT refund \(9% instead of 13%\), reducing a government subsidy that offsets part of their tax costs.

<details><summary>References</summary>
<ul>
<li><a href="https://m.21jingji.com/article/20260707/herald/cb23a7ef45879953192c505f6a079941.html">车 船 税 红利落幕，中国 新 能 源 汽 车 迈入“成人时代” - 21 财 经</a></li>

</ul>
</details>

**Tags**: `#new energy vehicles`, `#export tax rebate`, `#China`, `#trade policy`, `#fiscal policy`

---

<a id="item-finance-news-3"></a>
### [Cleveland Fed&\#x27;s Hammack says restrictive policy may be needed with PCE at 3.4%](https://www.cnbc.com/2026/10/12/beth-hammack-fed-inflation-policy.html) ⭐️ 7.0/10

Cleveland Federal Reserve President Beth Hammack said Monday that a restrictive monetary policy stance—keeping interest rates high enough to slow inflation—may be needed to return to the Fed&\#x27;s 2% target and prevent an inflationary mindset, with the Personal Consumption Expenditures price index at 3.4% year over year in August and the core measure, excluding food and energy, at 3%. Traders priced an 88% chance of a rate hike at the Fed&\#x27;s December meeting.

rss · CNBC Finance · Oct 13, 02:58

**「Background」** Hammack, a voting member of the Fed&\#x27;s policymaking committee, spoke after the central bank&\#x27;s first rate increase in three years last month and after September meeting minutes signaled possible further hikes without a clear timeline.

**Tags**: `#Federal Reserve`, `#Monetary Policy`, `#Inflation`, `#Interest Rates`, `#Economy`

---

<a id="item-finance-news-4"></a>
### [Rebuilt Huanggang Port opens with faster joint customs clearance](https://sc.isd.gov.hk/TuniS//www.info.gov.hk/gia/general/202610/09/P2026100900280.htm) ⭐️ 7.0/10

The rebuilt Huanggang Port opened at 6:30 a.m. on 12 October 2026 with a “one place, two inspections” and “joint inspection, one release” model, cutting overall passenger processing time from about 30 minutes to about 5 minutes.

telegram · zaihuapd · Oct 12, 05:12

**「Background」** The new 24-hour crossing replaced the previous Huanggang facility and has 134 self-service lanes and 68 manual counters, with an initial estimated peak capacity of 200,000 passengers per day, later expandable to 300,000.

**Tags**: `#Hong Kong`, `#infrastructure`, `#customs clearance`, `#cross-border trade`, `#public policy`

---

<a id="item-finance-news-5"></a>
### [DeepSeek Reportedly to Lead Seed Round for Former Tencent Scientist&\#x27;s Robotics Startup at $400 Million Valuation](https://www.bloomberg.com/news/articles/2026-10-12/deepseek-backs-ex-tencent-ai-scientist-s-400-million-robot-lab) ⭐️ 7.0/10

DeepSeek is reportedly planning to lead a seed investment of tens of millions of dollars in Winverse AI, a robotics startup founded by former Tencent scientist Hu Han, at a post-money valuation of about $400 million, though the deal is not finalized, according to people familiar with the matter.

telegram · zaihuapd · Oct 12, 14:59

**「Background」** Winverse AI is a stealth Chinese startup building artificial intelligence for robots.

<details><summary>References</summary>
<ul>
<li><a href="https://qz.com/deepseek-winverse-ai-robotics-seed-round-101226">DeepSeek leads $400 million seed round for robotics AI startup</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#Winverse AI`, `#robotics`, `#venture capital`, `#funding round`

---

<a id="item-finance-news-6"></a>
### [China sets new tax penalty standards from November 2026, with social insurance arrears fines up to 3x](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5252754/content.html) ⭐️ 7.0/10

China&\#x27;s State Taxation Administration issued nationwide administrative penalty standards effective November 1, 2026, allowing fines of up to three times unpaid social insurance contributions. The penalty applies only after an employer has been ordered to pay by a deadline and remains overdue, and it must be combined with repayment plus a daily 0.05% late fee.

telegram · zaihuapd · Oct 13, 02:45

**「Background」** Before the nationwide baseline was finalized, the State Taxation Administration had released a draft version of the tax administrative penalty discretion baseline for public comment.

**「Impact」** Employers that underpay or fail to pay social insurance contributions face higher maximum fines and daily late fees, increasing payroll compliance costs.

<details><summary>References</summary>
<ul>
<li><a href="https://paper.people.com.cn/rmrb/pc/attachement/202607/18/0378ed27-fe07-41dc-95b0-b5fb063d3b93.pdf">paper.people.com.cn/rmrb/pc/attachement/202607/18/0378ed27-fe07...</a></li>

</ul>
</details>

**Tags**: `#tax policy`, `#social insurance`, `#regulatory compliance`, `#China`, `#penalties`

---