---
layout: default
title: "Horizon Summary: 2026-09-22 (EN)"
date: 2026-09-22
lang: en
---

> From 40 items, 12 important content pieces were selected

---

**Technology News**
1. [Xiaomi Releases Open MiMo v2.6 Pro and Flash Models](#item-tech-news-1) ⭐️ 8.0/10
2. [Cloudflare Python Workers Now Generally Available](#item-tech-news-2) ⭐️ 8.0/10
3. [Apple M6 Mac Mini Benchmarks: Multi-Core Matches Intel Flagship, GPU Nearly Doubles](#item-tech-news-3) ⭐️ 8.0/10
4. [I don&\#x27;t want to read what you didn&\#x27;t write](#item-tech-news-4) ⭐️ 7.0/10
5. [Interactive Visual Guide to Transformer Attention and Token Generation](#item-tech-news-5) ⭐️ 7.0/10
6. [What Sun Got Wrong: Bryan Cantrill&\#x27;s Retrospective](#item-tech-news-6) ⭐️ 7.0/10
7. [xAI Releases Grok 4.7 with 40% More Weights, Same Pricing](#item-tech-news-7) ⭐️ 7.0/10
8. [FAA Halts East Coast Flights After Fiber Line Cut](#item-tech-news-8) ⭐️ 7.0/10
9. [TypeSafe AI&\#x27;s Jev: A New Decision Model for Numerical Outputs](#item-tech-news-9) ⭐️ 7.0/10
10. [Computation and Data Movement for Inference](#item-tech-news-10) ⭐️ 7.0/10
11. [Moonshot AI Releases Kimi Code Desktop for macOS and Windows](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [American companies squeezed by tariffs, fuel costs and higher rates](#item-finance-news-1) ⭐️ 9.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Xiaomi Releases Open MiMo v2.6 Pro and Flash Models](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

Xiaomi released and open-sourced MiMo-V2.6, a set of native multimodal models with two main variants: Pro \(1.02T total parameters, 42B activated\) and Flash \(309B total, 15B activated\). The models target agent tasks including coding, computer use, 3D scenes, and audiovisual content creation, and a Pro-UltraSpeed variant offers up to 20x faster output at similar quality. Training used MixRL to jointly train medium-difficulty verifiable code and agent tasks, then separately trained harder-to-verify game, 3D, and subjective tasks before merging capabilities with MOPD. Xiaomi also released a Qwen model distilled from training trajectories, 7,000 environments, and the full RL framework, along with web, API, and Hugging Face access. The team claims this is among the largest single reinforcement-learning training runs by compute for an open-source model team.

hackernews · volf\_ · Sep 21, 20:12 · [Discussion](https://news.ycombinator.com/item?id=49792730)

**「Background」** MiMo is Xiaomi&\#x27;s open-weight large language model series. The v2.6 release includes MiMo-V2.6-Pro, a mixture-of-experts model with about 1.02 trillion total parameters and 42 billion active parameters, and MiMo-V2.6-Flash, a smaller MoE with around 309 billion total parameters and 15 billion active. Xiaomi trained both with reinforcement learning and published a live dashboard of training metrics, which is unusually transparent for an open model release; the Flash variant also uses an audio patch encoder and speculative decoding for efficient serving.

**「Impact」** Developers and researchers can immediately download the open weights from Hugging Face, access the API, and reuse the released RL framework, 7,000 environments, and distilled Qwen trajectories to build or study agentic multimodal systems.

**「Community Discussion」** Commenters largely praised Xiaomi&\#x27;s transparency, especially the real-time RL dashboard and detailed tech report, with some expressing more excitement for Chinese models due to affordability. Practical details such as activated parameter counts were shared, and one user joked about the recurring &\#x27;01 - UPPERCASE TEXT&\#x27; frontend design motif.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/rl/">mimo-v2.6 RL</a></li>
<li><a href="https://rajeshparikh.substack.com/p/xiaomis-live-mimo-v26-rl-run">Xiaomi’s Live MiMo-V2.6 RL Run - by Rajesh Parikh</a></li>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/MiMo-V2.6-Flash-RL · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#large-language-models`, `#open-source`, `#Xiaomi`, `#mixture-of-experts`

---

<a id="item-tech-news-2"></a>
### [Cloudflare Python Workers Now Generally Available](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 8.0/10

Cloudflare has made Python support generally available on its Workers serverless platform after a two-year preview, describing Python as a first-class, fully supported language on the Cloudflare Developer Platform. The implementation runs Python compiled to WebAssembly via Pyodide inside the V8-based workerd runtime. Documented limitations include non-functional \`multiprocessing\` and \`threading\` modules in the WebAssembly VM. Local development uses the \`pywrangler\` tool, packaged as \`workers-py\` on PyPI, which simulates the full stack with a 123MB \`workerd\` binary. The release announcement credits Gyeongjae Choi, Dominik Picheta, and Hood Chatham, with Gyeongjae and Hood being Pyodide core maintainers.

rss · Simon Willison · Sep 21, 22:25

**「Background」** Cloudflare Workers is a serverless platform where code runs in Cloudflare&\#x27;s global network without server management. Pyodide is a Python distribution that compiles the interpreter and packages to WebAssembly, enabling Python execution inside JavaScript-based runtimes such as Cloudflare&\#x27;s V8-based workerd. This compatibility layer is what allowed Cloudflare to add Python support to Workers during its two-year preview.

**「Impact」** Python developers can now deploy and run Python code on Cloudflare Workers as a supported language, but must avoid \`threading\` and \`multiprocessing\`, and can use \`pywrangler\`/\`workers-py\` for local simulation of the exact runtime.

**「Community Discussion」** Hacker News commenters include an urllib3 maintainer who confirms that upstream Pyodide/Emscripten and JSPI support made Requests work, though funding went to an external contributor rather than maintainers. A Wasmer competitor praises Cloudflare&\#x27;s progress and the standardization of PyEmscripten via PEP 783, while some compare the offering to Google App Engine&\#x27;s 2008 Python support and others note ongoing architectural concerns.

**Tags**: `#cloudflare`, `#python`, `#webassembly`, `#serverless`, `#workers`

---

<a id="item-tech-news-3"></a>
### [Apple M6 Mac Mini Benchmarks: Multi-Core Matches Intel Flagship, GPU Nearly Doubles](https://www.bilibili.com/video/BV1JQhz6fE1x) ⭐️ 8.0/10

Apple&\#x27;s new M6 Mac mini has been benchmarked with a 12-core CPU using a 2+4+6 configuration on TSMC&\#x27;s N2 process and a 4.8 GHz maximum performance core. In Geekerwan tests, its multi-core performance matches Intel&\#x27;s Panther Lake X9 388H, while single-core remains ahead and improves by more than 50 percent over the M4. The GPU has been upgraded to 12 cores, with ray tracing and gaming performance roughly doubling that of the M4. Power measurements show about 25 W under CPU full load and about 65 W for the whole system during a dual stress test.

telegram · zaihuapd · Sep 21, 16:32

**「Context」** Apple&\#x27;s M6 is the successor to the M4 and is expected to be built on TSMC&\#x27;s N2 \(2nm\) process, with the new Mac mini expected to be the first device to use it. Ahead of the launch, unverified Geekbench 7 results for the M6 Mac mini surfaced, and a Reddit thread on those results pointed to Geekerwan as a source for chip testing. The item reports a hands-on Geekerwan M6 Mac mini test that includes CPU core configuration, clock speeds, power draw, and graphics gains.

**「Impact」** For Mac mini buyers and developers, the M6&\#x27;s CPU multi-core performance now matches Intel&\#x27;s Panther Lake X9 388H and its 12-core GPU delivers near-doubled gaming and ray tracing performance over M4, while CPU full load stays around 25 W.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/09/15/apple-m6-chip-benchmark/">M6 Chip Benchmark Surfaces Ahead of New Mac Mini Launch Next Week - MacRumors</a></li>
<li><a href="https://www.reddit.com/r/apple/comments/1wh6gx4/m6_chip_benchmark_surfaces_on_geekbench_ahead_of/">r/apple on Reddit: M6 chip benchmark surfaces on Geekbench ahead of new Mac Mini launch next week</a></li>

</ul>
</details>

**Tags**: `#Apple Silicon`, `#Hardware benchmarks`, `#Mac mini`, `#CPU architecture`, `#GPU`

---

<a id="item-tech-news-4"></a>
### [I don&\#x27;t want to read what you didn&\#x27;t write](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 7.0/10

The post argues that people should not read AI-generated text that the author did not write, questioning the value of LLM-generated documentation and writing. It observes a pattern where builders use AI to create something and then have AI retrospectively summarize it into a design document, describing the result as punishing rather than helpful. This critique targets software engineering documentation and code review, where generated prose can obscure rather than clarify intent.

hackernews · mooreds · Sep 21, 22:30 · [Discussion](https://news.ycombinator.com/item?id=49794330)

**「Author background」** Colin Breck is a software engineer and blogger who has written about software design, team leadership, and simplifying systems for at least two years, publishing roughly one article per month. His site emphasizes judgment and trust in engineering teams, as seen in his statement that ignoring intuitive systems thinkers can lead to deleting the wrong things. The linked post is an opinion essay on AI-generated text, not a technical change or product release.

**「Impact」** Software teams that rely on LLM-generated documentation may face increased code-review friction, as reviewers resist verbose or untrustworthy AI-written descriptions and demand concise, author-written context.

**「Community Discussion」** Commenters mostly agree that LLM-generated text fails to transfer the author’s intended meaning, with one arguing that writing quality has dropped in recent models like Claude Sonnet 4.5 and another reporting pushback on verbose AI-generated PR descriptions. A counterpoint notes the article’s own opening sentence exemplifies the problem it criticizes.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.colinbreck.com/">Colin Breck</a></li>
<li><a href="https://blog.colinbreck.com/author/colin-breck/page/3/">Colin Breck - Colin Breck (Page 3)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#writing`, `#software engineering`, `#documentation`

---

<a id="item-tech-news-5"></a>
### [Interactive Visual Guide to Transformer Attention and Token Generation](https://poloclub.github.io/transformer-explainer/) ⭐️ 7.0/10

The interactive visual guide explains how transformer models work, focusing on attention mechanisms and token generation. It provides technical depth and visual insight into a core deep learning architecture and is intended for practitioners and students. The guide is available at poloclub.github.io/transformer-explainer and was shared on Hacker News.

hackernews · aray07 · Sep 21, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49792342)

**「Background」** Transformer-based models like GPT are a core architecture behind modern large language models. Transformer Explainer is an open-source interactive visualization that runs a live GPT-2 model in the browser, letting users experiment with text input and observe how attention and token probabilities work.

**「Community Discussion」** Commenters recommended Jay Alammar&\#x27;s Illustrated Transformer as an additional resource, and one noted that attention heads effectively construct a small dense-layer weight matrix dynamically from key and query vectors. Others pointed out that &\#x27;transformer&\#x27; also refers to electrical transformers, causing confusion, and criticized the guide&\#x27;s use of &\#x27;safety&\#x27; in its temperature explanation, arguing that low-temperature text can seem artificial rather than safer.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/poloclub/transformer-explainer">GitHub - poloclub/transformer-explainer: Transformer Explained Visually: Learn How LLM Transformer Models Work with Interactive Visualization · GitHub</a></li>
<li><a href="https://poloclub.github.io/transformer-explainer/">Transformer Explainer: LLM Transformer Model Visually Explained</a></li>
<li><a href="https://arxiv.org/html/2408.04619v1">Transformer Explainer: Interactive Learning of Text-Generative Models</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#machine learning`, `#visualization`, `#deep learning`, `#education`

---

<a id="item-tech-news-6"></a>
### [What Sun Got Wrong: Bryan Cantrill&\#x27;s Retrospective](https://bcantrill.dtrace.org/2026/09/20/what-sun-got-wrong/) ⭐️ 7.0/10

Bryan Cantrill&\#x27;s essay &quot;What Sun Got Wrong,&quot; published on September 20, 2026, examines the key strategic and technical mistakes that led to Sun Microsystems&\#x27; decline. The retrospective is historical rather than breaking news, offering lessons for software engineering and technology industry readers. It has sparked high community engagement on Hacker News.

hackernews · chmaynard · Sep 21, 14:03 · [Discussion](https://news.ycombinator.com/item?id=49787436)

**「Background」** Bryan Cantrill is a software engineer who worked at Sun Microsystems and later at Oracle after its acquisition of Sun. He is now the CTO and co-founder of Oxide Computer Company.

**「Community Discussion」** Commenters broadly agree that Sun made serious strategic mistakes, citing examples such as the briefly canceled Solaris on x86 in 2002 and a failed deal with Google over server-count secrecy. Some share firsthand frustration with Sun&\#x27;s cumbersome sales process compared to Dell, while others recall the technology fondly and connect Sun&\#x27;s collapse to current high-valuation tech stocks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill - Wikipedia</a></li>
<li><a href="https://www.tiktok.com/discover/bryan-cantrill-distinguished-engineer">Bryan Cantrill Distinguished Engineer | TikTok</a></li>

</ul>
</details>

**Tags**: `#Sun Microsystems`, `#technology history`, `#industry analysis`, `#operating systems`, `#open source`

---

<a id="item-tech-news-7"></a>
### [xAI Releases Grok 4.7 with 40% More Weights, Same Pricing](https://x.ai/news/grok-4-7) ⭐️ 7.0/10

xAI released Grok 4.7, a new version of its Grok large language model with 40% more weights than Grok 4.6 and unchanged API pricing \($2 input, $6 output\). Early Hacker News commenters report slower inference and mixed performance for coding and agentic workflows, with one noting Grok 4.6 did not meet their use-case floor. The release was delayed nearly two weeks from its originally planned date and came just before a rumored Anthropic Opus 5.5 launch, leading to skepticism that benchmark gains may rely on increased token usage rather than genuine capability improvements.

hackernews · meetpateltech · Sep 21, 15:50 · [Discussion](https://news.ycombinator.com/item?id=49788838)

**「Background」** Grok is a family of generative large language models from xAI, introduced in November 2023 and updated in rapid cycles; Grok 4.6 was the prior version. xAI positions Grok 4.7 as its most capable model for coding and knowledge work, with claims of being twice as fast at half the price of comparable models.

**「Impact」** For developers evaluating the API, Grok 4.7 keeps the same listed price but early reports indicate slower inference and possibly higher token consumption on reasoning tasks, which could increase effective cost and latency.

**「Community Discussion」** Early community reactions are mixed: some commenters doubt the benchmark gains translate to real-world usefulness, citing slower inference and heavy token use, while others see the update as a positive sign of xAI&\#x27;s increasing release cadence and hope Grok 5 will deliver a larger step change.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_%28chatbot%29">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4 . 7 | SpaceXAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#xAI`, `#Grok`, `#Model Release`

---

<a id="item-tech-news-8"></a>
### [FAA Halts East Coast Flights After Fiber Line Cut](https://www.reuters.com/world/us/faa-halts-some-us-east-coast-flights-due-communication-issues-2026-09-21/) ⭐️ 7.0/10

The US Federal Aviation Administration halted flights at busy East Coast airports after a fiber line cut disrupted communication systems. When operators attempted to switch to a backup fiber path, they discovered that the backup fiber was also broken and had not been reported as unserviceable. This exposed a critical redundancy flaw in a life-critical aviation communication network, where the backup path was not actively monitored for integrity. The outage triggered discussion about inadequate network resilience for systems with significant safety and economic impact.

hackernews · allanbreyes · Sep 21, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49791509)

**「Background」** The FAA is the U.S. agency responsible for air traffic control, and it can issue ground stops when safety-critical communication or data systems fail. Many ATC facilities rely on leased fiber-optic circuits for radar, flight data, and voice communications, with physically diverse backup paths intended to prevent single points of failure. On September 21, 2026, a failed primary telecommunications circuit and a severed backup fiber line in New Jersey caused a ground stop affecting airports serving New York, Newark, Philadelphia, and Boston.

**「Impact」** The fiber-line failure forced the FAA to halt incoming flights at major New York, Boston, and Philadelphia airports, disrupting thousands of flights across the East Coast.

**「Community Discussion」** Commenters broadly criticized the lack of monitored, diverse redundant paths, noting that even two fiber paths can fail simultaneously and that backup unserviceability went undetected until switchover. One commenter also pointed to a new ATC system deployment underway on the same day.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aljazeera.com/economy/2026/9/21/faa-halts-flights-to-major-us-east-coast-airports-amid-outage">FAA halts flights to major US East Coast airports amid... | Al Jazeera</a></li>
<li><a href="https://www.ntd.com/faa-halts-east-coast-flights-after-backup-fiber-line-cut_1174093.html">FAA Halts East Coast Flights After Backup Fiber Line Cut | NTD</a></li>
<li><a href="https://www.nytimes.com/2026/09/21/us/east-coast-flights-ground-stop-communication-failure.html">Technical Problems Ground Flights at Major East Coast Airports</a></li>
<li><a href="https://libn.com/2026/09/21/faa-halts-flights-new-york-area-airports-fiber-line-cut/">FAA halts flights at New York area airports after fiber line cut - Long Island Business News</a></li>
<li><a href="https://www.usnews.com/news/top-news/articles/2026-09-21/faa-halts-some-us-east-coast-flights-due-to-communication-issues">US Halts Flights at Busy East Coast Airports, Says Fiber ...</a></li>
<li><a href="https://www.aljazeera.com/economy/2026/9/21/faa-halts-flights-to-major-us-east-coast-airports-amid-outage">FAA halts flights to major US East Coast airports amid outage | Aviation News | Al Jazeera</a></li>

</ul>
</details>

**Tags**: `#fiber-cut`, `#infrastructure`, `#aviation`, `#network-reliability`, `#incident`

---

<a id="item-tech-news-9"></a>
### [TypeSafe AI&\#x27;s Jev: A New Decision Model for Numerical Outputs](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 7.0/10

Last week TypeSafe AI unveiled Jev, the first model in a new category it calls &\#x27;System One models&\#x27;—also referred to as decision models. Unlike standard LLMs, Jev accepts text input but returns floating-point numbers for yes/no questions, choice selections, numeric scores, and confidence levels. It is fast and very cheap: output is free and input costs $0.042 per million tokens, cheaper than OpenAI&\#x27;s GPT-5 Nano at $0.05/million, and the API evaluates many questions against a single state object in parallel. Simon Willison argues it is well suited to classification, spam detection, labeling, prioritization, ranking, and search reranking, but warns it is even more of a black box than text LLMs because it provides no explanation or justification. Within about a week, the community released open-weight recreations such as Kev \(using Qwen 3.5\) and the JevBench benchmark, along with demos like jevchat, jev-leftpad, and jev-2048.

rss · Simon Willison · Sep 21, 23:09

**「Background」** Standard LLMs generate text and are typically priced by both input and output tokens, with output often costing more. TypeSafe AI describes Jev as &\#x27;a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out,&\#x27; meaning it is intended for tasks where a numeric decision or score is the desired result.

**「Impact」** Developers can run hundreds or thousands of classification, scoring, or reranking experiments with Jev for a few cents, but they must rely on structured evals and bias testing because the model&\#x27;s floating-point outputs offer no explanation for how decisions were reached.

**Tags**: `#large language models`, `#decision models`, `#AI`, `#structured outputs`, `#TypeSafe AI`

---

<a id="item-tech-news-10"></a>
### [Computation and Data Movement for Inference](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 7.0/10

The article analyzes how mixture-of-experts \(MoE\) models map onto inference hardware for efficient serving. It examines the structure and data flow involved in executing MoE computations, particularly how activations and parameters move across devices. The analysis notes that this mapping is relevant to AI infrastructure and software engineering, though the available source does not provide specific performance numbers, versions, or compatibility constraints. It presents a technical deep-dive rather than an announced breakthrough.

rss · Semianalysis · Sep 21, 18:14

**「Background」** Mixture-of-experts \(MoE\) models route each token to only a few specialized expert subnetworks instead of the entire model, reducing per-token compute but creating irregular data movement as tokens are gathered for each expert and expert weights are loaded. Efficient inference hardware must keep compute units busy by overlapping these memory transfers with matrix multiplications; for example, SemiAnalysis describes memory bandwidth as the width of the pipe feeding data to compute units and MoE as a team of specialists where only a few experts are called per token. Recent TPU optimization work moved the irregular rearrangement of expert inputs onto the SparseCore, which gathers each expert’s tokens into contiguous groups, while the TensorCore runs the expert matrix multiplications.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://inferencex.semianalysis.com/glossary">AI Inference Glossary | InferenceX by SemiAnalysis</a></li>

</ul>
</details>

**Tags**: `#Mixture of Experts`, `#Inference`, `#AI Infrastructure`, `#Hardware`, `#Model Serving`

---

<a id="item-tech-news-11"></a>
### [Moonshot AI Releases Kimi Code Desktop for macOS and Windows](http://kimi.com/code) ⭐️ 7.0/10

Moonshot AI released Kimi Code Desktop for macOS and Windows, available at kimi.com/code. The official desktop client brings AI Agent coding capabilities to the desktop, letting users read and write code, run commands, and complete automated tasks through conversation. It includes a built-in terminal, browser, and Git status viewing to help developers run and debug projects, review code changes, and track pull request progress.

telegram · zaihuapd · Sep 21, 08:48

**「Background」** Moonshot AI is the developer of the Kimi model family and describes its Kimi K3 flagship as a 2.8T-parameter natively multimodal model with a 1M-token context built for long-horizon coding, knowledge work, and deep reasoning. The company also uses a Kimi Code evaluation harness for coding benchmarks, indicating that Kimi Code is the coding-oriented product line to which this desktop release belongs.

**「Impact」** Developers on macOS and Windows can now use Kimi Code as a native desktop client with integrated terminal, browser, and Git status, reducing context switching during agent-assisted coding and code review.

<details><summary>References</summary>
<ul>
<li><a href="https://www.moonshot.ai/">Welcome to Moonshot AI . Our mission is to seek the optimal...</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI coding assistant`, `#desktop client`, `#Moonshot AI`, `#developer tools`, `#software engineering`

---

## Financial News

<a id="item-finance-news-1"></a>
### [American companies squeezed by tariffs, fuel costs and higher rates](https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html) ⭐️ 9.0/10

US companies across manufacturing, transportation, and retail face a triple squeeze from tariffs, surging fuel prices, and rising interest rates, with the Federal Reserve having raised its benchmark rate for the first time in three years and signaling another hike is possible this year.

rss · CNBC Finance · Sep 21, 15:04

**「background」** The squeeze combines tariffs imposed under President Donald Trump&\#x27;s trade policies, fuel costs driven up by the Iran war, and Federal Reserve rate hikes aimed at curbing stubborn inflation.

**「impact」** Middle-market manufacturers and auto suppliers are bearing the brunt, with Lucerne International stopping US manufacturing and Grupo Antolin filing for Chapter 15 bankruptcy, while airlines have cut less profitable flights and fares rose more than 23% in August from a year earlier.

**Tags**: `#tariffs`, `#fuel costs`, `#interest rates`, `#manufacturing`, `#inflation`

---