---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 41 items, 17 important content pieces were selected

---

**Technology News**
1. [Calif Research&\#x27;s WeWorm: AI-Aided Zero-Click Worm via WeChat Calls](#item-tech-news-1) ⭐️ 9.0/10
2. [Shopify Moves from React Native to Native Swift and Kotlin](#item-tech-news-2) ⭐️ 8.0/10
3. [Microsoft Designates Rust as Tier-1 Language](#item-tech-news-3) ⭐️ 8.0/10
4. [Any Nix package, live in your browser](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek V4.1 Flash: Stronger, Faster, More Accessible](#item-tech-news-5) ⭐️ 8.0/10
6. [Concerns Raised About OpenAI Using Unpublished Math Ideas](#item-tech-news-6) ⭐️ 7.0/10
7. [PlanetScale Launches Neki, a Sharded Postgres Offering](#item-tech-news-7) ⭐️ 7.0/10
8. [Sony website references to players &\#x27;owning&\#x27; digital games](#item-tech-news-8) ⭐️ 7.0/10
9. [Behind-the-Meter Power for Datacenters: Part 1 Challenges](#item-tech-news-9) ⭐️ 7.0/10
10. [Ant International, Visa, Mastercard to co-develop AI agent payment standard](#item-tech-news-10) ⭐️ 7.0/10
11. [DeepSelect: High-Performance TopK Kernel for DSA and Samplers](#item-tech-news-11) ⭐️ 7.0/10
12. [Chinese AI chipmakers raise prices as HBM shortage bites](#item-tech-news-12) ⭐️ 7.0/10
13. [Tencent Hunyuan Releases Open-Source Audio Editing Model AuK](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [Kalshi launches CFTC-approved gold and silver perpetual futures](#item-finance-news-1) ⭐️ 8.0/10
2. [Apple prices first foldable iPhone Duo at 15,999 yuan in China](#item-finance-news-2) ⭐️ 7.0/10
3. [Premarket Movers: Macy&\#x27;s Raises Guidance, Copper Miners Slide](#item-finance-news-3) ⭐️ 7.0/10
4. [Ant International, Visa and Mastercard to develop common AI agent payment standards](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Calif Research&\#x27;s WeWorm: AI-Aided Zero-Click Worm via WeChat Calls](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research has released a demo of WeWorm, which it describes as the first zero-click worm to spread through WeChat calls on both iOS and Android. The worm requires no user interaction: victims need not answer the call, and even if they do answer they hear nothing while the exploit still succeeds. According to the researchers, using AI they found the underlying bug and wrote the first remote code execution \(RCE\) exploit in about two days, then built the worm in one more week. Calif Research notes that a worm at this scale previously required a larger team working for months, and says AI can already do most of the work, with the team providing judgment about targeting and safe testing.

rss · Simon Willison · Sep 10, 00:56

**「Background」** Zero-click attacks require no user interaction, meaning victims can be compromised without answering a call or touching their device. WeChat is a widely used messaging and calling platform on iOS and Android. AI-assisted security research uses large language models to accelerate vulnerability discovery and exploit development.

**「Immediate impact for WeChat users」** If exploited, WeWorm could let attackers compromise WeChat accounts on iOS and Android through unanswered incoming calls, but Tencent has reportedly already mitigated the vulnerability; the PoC remains a demonstration of AI-accelerated exploit development rather than an observed in-the-wild worm.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0-Click Worm Spreading Through WeChat Calls Across...</a></li>
<li><a href="https://www.cyberkendra.com/2026/09/weworm-zero-click-wechat-worm-ios-android.html">WeWorm : Zero-Click WeChat Worm Hijacks iOS and Android</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#zero-click`, `#WeChat`, `#vulnerability-research`

---

<a id="item-tech-news-2"></a>
### [Shopify Moves from React Native to Native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify is moving its mobile applications away from React Native to native development, using Swift for iOS and Kotlin for Android. The shift reverses a cross-platform strategy and returns to separate platform-specific codebases. Hacker News commenters discuss this as a significant mobile engineering development, citing debugging complexity across JavaScript, C++, and native threads as a reason to prefer native code, and debating whether LLM-assisted code generation made the migration more affordable.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**「Background」** React Native is a cross-platform mobile framework that lets developers write a single JavaScript codebase to target both iOS and Android, while native development uses platform-specific languages—Swift for iOS and Kotlin for Android—and platform APIs directly. Shopify had adopted React Native to share code across platforms, but its engineering team has now published an article explaining why they are moving back to native languages.

**「Impact」** Shopify&\#x27;s move adds a prominent data point to the native-versus-cross-platform debate, with practitioners arguing that maintaining native codebases can avoid cross-layer debugging costs and allow platform-specific optimization.

**「Community Discussion」** Hacker News commenters broadly welcome the shift, with several describing their own React Native-to-native migrations and arguing that debugging crashes across JavaScript, C++, and native threads costs more than maintaining two codebases. They disagree on the role of LLM assistance: one commenter says the majority of their migration occurred before LLM code assistance, while another contends that improved AI code generation reduces the upside of React Native.

<details><summary>References</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>
<li><a href="https://hybridtonative.com/moving-from-react-native-to-swift-kotlin-what-you-need-to-know/">Moving from React Native to Swift &amp; Kotlin : What... - Hybrid to Native</a></li>

</ul>
</details>

**Tags**: `#mobile development`, `#react-native`, `#swift`, `#kotlin`, `#software engineering`

---

<a id="item-tech-news-3"></a>
### [Microsoft Designates Rust as Tier-1 Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

Microsoft has officially designated Rust as a tier-1 language, according to a Rust Foundation guest post. This designation underscores Rust&\#x27;s growing role in systems and infrastructure software at the company. The recognition signals industry adoption and maturity for systems programming, and it matters for developers building critical, performance-sensitive components.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**「Background」** Rust is a systems programming language overseen by the Rust Foundation, whose platinum members include Microsoft. Microsoft has now formally classified Rust as a Tier-1 language, a designation signifying a critical internal role, while C++ still dominates after decades of development. The Rust Foundation guest post notes that using a unified codegen platform will minimize maintenance and evolution costs.

**「Community Discussion」** Hacker News commenters generally welcomed the tier-1 designation, with some arguing that Rust is no longer a fledgling language and is now a serious competitor to C++ and C\#. Others highlighted DARPA work on automating C-to-Rust conversion and noted that all major OS vendors are diversifying their systems programming options.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rust_%28programming_language%29">Rust (programming language) - Wikipedia</a></li>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://qatrial.com/developer-open-source/rust-is-tier-1-language-at-microsoft/">Rust Is Tier-1 Language At Microsoft - QAtrial</a></li>

</ul>
</details>

**Tags**: `#rust`, `#microsoft`, `#programming-languages`, `#systems-programming`, `#industry-adoption`

---

<a id="item-tech-news-4"></a>
### [Any Nix package, live in your browser](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria has launched trynix.dev, which uses qemu-wasm to run an x86\_64 Linux virtual machine entirely in the browser via WebAssembly. The VM can boot any Nix package from the past 13 years, and packages are URL addressable; for example, https://trynix.dev/?pkg=python3%403.6.2 loads an interactive shell running Python 3.6.2 from 2017. Zakaria also introduced trynix-preview, a GitHub Action that comments a link on a pull request to boot the PR&\#x27;s build in the browser. The service requires no servers beyond the browser execution environment.

rss · Simon Willison · Sep 10, 23:44

**「Background」** Nix is a reproducible package manager whose binary cache retains historical package versions, enabling recreation of old builds. QEMU is a hardware emulator, and qemu-wasm compiles it to WebAssembly so an entire Linux VM can execute client-side in a browser.

**「Impact」** Developers reviewing Nix-based pull requests can now boot the actual PR build through a comment link without provisioning server infrastructure or local VMs.

**Tags**: `#nix`, `#webassembly`, `#qemu`, `#virtualization`, `#developer-tools`

---

<a id="item-tech-news-5"></a>
### [DeepSeek V4.1 Flash: Stronger, Faster, More Accessible](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek has officially released V4.1 Flash, the smallest model in a new architecture series, using a 552B-parameter Causal-Encoder-Decoder design with 8B input activations and 16B output activations and native multimodal visual understanding. The model is available through the DeepSeek API under the model name deepseek-flash, and new pricing takes effect on September 10, 2026 at 12:00. After September 14, 2026 at 12:00, deepseek-v4-pro API requests will be routed to V4.1 Flash and billed according to V4.1 Flash pricing. The announcement does not include benchmark comparisons or detailed performance figures.

telegram · zaihuapd · Sep 10, 05:54

**「DeepSeek company context」** DeepSeek is an AI research company headquartered in Hangzhou, Zhejiang, and is owned and funded by High-Flyer; its co-founder Liang Wenfeng serves as CEO. The company develops and open-sources frontier large language models, including DeepSeek-V4, DeepSeek-R1, and DeepSeek-Coder.

**「Impact」** Developers using deepseek-v4-pro after 2026-09-14 12:00 will receive V4.1 Flash responses and be charged at the new V4.1 Flash rate, so they should evaluate compatibility and cost changes before the routing switch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://deepseek.com/en/index.html">DeepSeek | Into the Unknown</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#large-language-models`, `#multimodal`, `#model-release`, `#api`

---

<a id="item-tech-news-6"></a>
### [Concerns Raised About OpenAI Using Unpublished Math Ideas](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 7.0/10

A Hacker News discussion highlights worries that OpenAI may have incorporated researchers&\#x27; unpublished mathematical ideas shared during model collaborations into later model outputs without attribution. Commenters note that OpenAI gave at least 100,000 researchers free access to its models, and that a researcher feeding fresh mathematical progress into Codex could unwittingly provide training data. The discussion also flags OpenAI&\#x27;s decision to generate 300 billion output tokens from a model still in training shortly after learning a major math proof might be in that model&\#x27;s training data, with one commenter calling it &\#x27;suspicious&\#x27; and akin to parallel construction. These concerns hinge on whether OpenAI&\#x27;s pretraining or reinforcement learning on verifiable math actually memorizes specific techniques from chats, which remains unproven. No official confirmation or resolution is provided in the thread.

hackernews · pred\_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**「Background」** In September 2026, OpenAI announced a historic mathematical result, but researchers Tristan Buckmaster and Andreas Thom questioned whether their unpublished work with Codex and ChatGPT had been used to train OpenAI&\#x27;s models without credit. This followed reports that OpenAI generated 300 billion output tokens from a model still in training after learning a major math proof might be in its training data. The broader issue is whether researchers can safely use frontier AI models for unpublished discoveries without having their ideas absorbed into future models.

**「Community Discussion」** Commenters disagree on whether OpenAI&\#x27;s models actually incorporate specific unpublished techniques from chats: some argue it resembles unethical collaboration with a human researcher who publishes without attribution, while others contend that reinforcement learning on verifiable math discovers superhuman connections largely independent of any single chat technique. A further comment calls OpenAI&\#x27;s generation of 300 billion output tokens from a training model &\#x27;suspicious&\#x27; and akin to parallel construction after learning a major proof may be in its data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit">OpenAI&#x27;s historic math solution overshadowed by credit controversy</a></li>
<li><a href="https://www.progressiverobot.com/2026/09/10/openai-math-mathematicians-want-proof-didnt-use-their-work/">OpenAI Math Risk: Mathematicians Want Definitive Proof</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#machine learning`, `#mathematics`

---

<a id="item-tech-news-7"></a>
### [PlanetScale Launches Neki, a Sharded Postgres Offering](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale has introduced Neki, a sharded Postgres service aimed at addressing scaling and distribution challenges for Postgres. The launch is a product announcement that has drawn community interest and debate, though the available source content provides limited technical detail about how Neki works. Community comments highlight concerns about eventual consistency for workloads that require strong consistency and note that Neki is not open source, contrasting it with Supabase&\#x27;s multigres. The announcement positions Neki as a potential new standard, but many details about its implementation and consistency model remain unclear from the provided information.

hackernews · simon\_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**「Background」** Sharding a database means distributing data across multiple servers to scale beyond a single node; for PostgreSQL this has been more operationally complex than for MySQL, where Vitess simplified horizontal scaling. PlanetScale&\#x27;s Neki page states that Vitess powers large sites such as Slack, GitHub, and Square by making MySQL sharding accessible, and Neki brings this same power to PostgreSQL. According to PlanetScale&\#x27;s sharding documentation, Neki is being built with design partners who already operate Postgres at significant scale.

**「Impact」** Developers evaluating distributed Postgres solutions should note that Neki is closed-source and its consistency guarantees are not yet fully documented, requiring caution for use cases with strict consistency requirements.

**「Community Discussion」** Community reaction is mixed: some users expect Neki to become a new standard, while others criticize the launch post for not clearly explaining what Neki is, take issue with the CEO&\#x27;s comments on competitors, and raise questions about consistency guarantees for distributed Postgres.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/docs/postgres/sharding">Horizontal sharding for Postgres - PlanetScale</a></li>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale</a></li>

</ul>
</details>

**Tags**: `#databases`, `#postgres`, `#sharding`, `#distributed-systems`, `#planetscale`

---

<a id="item-tech-news-8"></a>
### [Sony website references to players &\#x27;owning&\#x27; digital games](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 7.0/10

A consumer rights wiki page catalogues references on Sony websites where the company describes players as &\#x27;owning&\#x27; digital games. The page is being used to support a PlayStation digital ownership lawsuit, which raises questions about whether digital purchases transfer ownership or only a license. The lawsuit reportedly involves binding arbitration and class action waiver clauses in Sony&\#x27;s Terms of Service. Community comments debate the legal weight of Sony&\#x27;s wording and the broader implications for consumer rights.

hackernews · haunter · Sep 10, 12:18 · [Discussion](https://news.ycombinator.com/item?id=49642531)

**「Background」** Sony faces a class-action lawsuit alleging the PlayStation Store uses ownership language such as &quot;Buy Now&quot; and &quot;Confirm Purchase&quot; while the terms of service grant only a limited license. Sony&\#x27;s legal defense claims reasonable consumers understand that digital games are not owned, a stance that has drawn widespread criticism. The wiki page referenced in the article compiles Sony website statements about players &quot;owning&quot; digital games as evidence for the plaintiffs.

**「Impact」** PlayStation users who accept Sony&\#x27;s terms face a binding arbitration clause and class action waiver, which could prevent them from joining a class action over digital game ownership.

**「Community Discussion」** Commenters criticize Sony&\#x27;s binding arbitration clause and class action waiver, with one arguing such clauses should be illegal. Others debate Sony&\#x27;s defense that two buyers cannot each own the same digital game, comparing it to owning distinct copies of a physical book.

<details><summary>References</summary>
<ul>
<li><a href="https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit">Sony PlayStation digital game ownership lawsuit</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lob0xQMEVSRmdzSm96YVJaay1pZ0FQAQ?hl=en-GB&amp;gl=GB&amp;ceid=GB:en">Google News - Gamers sue Sony over digital game ownership ...</a></li>

</ul>
</details>

**Tags**: `#digital ownership`, `#consumer rights`, `#video games`, `#Sony`, `#software licensing`, `#legal`

---

<a id="item-tech-news-9"></a>
### [Behind-the-Meter Power for Datacenters: Part 1 Challenges](https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the) ⭐️ 7.0/10

This Semianalysis article by Ellie Holbrook examines the technical and economic challenges of supplying behind-the-meter power to datacenters, a key constraint for AI infrastructure scaling. The piece is the first part in a series and frames the topic with the contrast between &quot;dumb science experiments&quot; and &quot;money printing machines.&quot; It focuses on why behind-the-meter power arrangements are difficult from both technical and economic standpoints, though the preview does not provide specific figures or case studies. The analysis is timely for systems and hardware readers because power availability affects AI datacenter deployments.

rss · Semianalysis · Sep 10, 14:28

**「Behind-the-Meter Power Context」** Behind-the-meter \(BTM\) power refers to electricity generation or storage located on the customer&\#x27;s side of the utility meter, allowing datacenters to avoid grid interconnection delays and potentially lower energy costs. As datacenter electricity demand surges, BTM solutions are seen as a way to bridge near-term grid limitations, but they face economic and regulatory challenges such as high energy prices and the lack of zonal pricing reforms in this decade.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/goldman-sachs_behind-the-meter-power-may-be-a-solution-activity-7501706619647352833-qaod">&#x27; Behind - the - meter &#x27; power may be a solution to grid constraints...</a></li>
<li><a href="https://datacentrereview.com/2025/04/behind-the-meter-data-centres/">Now is the time for data centres to install behind - the - meter</a></li>
<li><a href="https://www.newsworthy.ai/news/202608112731/behind-the-meter-power-why-texas-data-centers-cant-lean-on-the-grid">Behind - the - Meter Power : Why Texas Data Centers ... | Newsworthy.ai</a></li>

</ul>
</details>

**Tags**: `#datacenter power`, `#energy infrastructure`, `#AI hardware`, `#behind-the-meter`, `#semiconductor analysis`

---

<a id="item-tech-news-10"></a>
### [Ant International, Visa, Mastercard to co-develop AI agent payment standard](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 7.0/10

Ant International, Visa, and Mastercard are jointly developing a common standard for AI agent payments. The three parties plan to create a &quot;Know Your Agent&quot; mechanism that links agents to verified entities, assesses behavior, and monitors risk. The goal is to improve interoperability and security across different payment systems. They cited a McKinsey forecast that AI agents could process $3 trillion to $5 trillion in global consumer commercial transactions by 2030.

telegram · zaihuapd · Sep 10, 03:00

**「Background: AI agent payments need a shared trust framework」** AI agents are increasingly expected to initiate purchases and payments on behalf of users, but identifying which person or business is responsible for an agent and ensuring it acts within approved limits remains an open challenge. The proposed &quot;Know Your Agent&quot; framework borrows from the established &quot;know your customer&quot; compliance model and would let an agent registered with one participating payment provider be recognized by others, reducing repeated verification while adding monitoring for agent behavior and risk.

**「Impact」** For payment networks and AI agent builders, the collaboration signals a future interoperable &quot;Know Your Agent&quot; standard, but its practical impact is uncertain because no technical specification or implementation timeline was provided.

<details><summary>References</summary>
<ul>
<li><a href="https://political.org/2026/09/09/visa-mastercard-and-ant-international-develop-standards-for-ai-agent-payments/">Visa , Mastercard and Ant International Launch ‘ Know Your Agent ...</a></li>
<li><a href="https://crypto.news/ant-international-joins-visa-mastercard-to-build-ai-agent-payment-standards/">Ant International joins Visa , Mastercard to build AI agent payment ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#payments`, `#fintech`, `#standards`, `#interoperability`

---

<a id="item-tech-news-11"></a>
### [DeepSelect: High-Performance TopK Kernel for DSA and Samplers](https://github.com/deepseek-ai/DeepSelect) ⭐️ 7.0/10

DeepSeek-AI released DeepSelect v1.0.0 on September 10, 2026. It is a suite of high-performance TopK kernels designed for DeepSeek Sparse Attention \(DSA\) and samplers. The project claims a 2–20x speedup over native torch.topk and is distributed on GitHub.

telegram · zaihuapd · Sep 10, 07:28

**「Background」** DeepSeek Sparse Attention \(DSA\) is a sparse-attention mechanism used by DeepSeek-style models, and NVIDIA&\#x27;s cuDNN provides a DSA module with CuTe-DSL kernels targeting Hopper \(SM90\) and Blackwell \(SM100+\) GPUs. DeepSelect is DeepSeek-AI&\#x27;s open-source CUDA project \(MIT license\) that supplies TopK kernels for DSA and samplers, released as v1.0.0 on September 10, 2026.

**「Impact」** Developers using DeepSeek Sparse Attention \(DSA\) in DeepSeek V3.2, V4, or V4.1 models or its sampler can expect 2–20× speedup over native torch.topk by adopting DeepSelect v1.0.0.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai">DeepSeek · GitHub</a></li>
<li><a href="https://github.com/orgs/deepseek-ai/repositories">deepseek-ai repositories · GitHub</a></li>
<li><a href="https://docs.nvidia.com/deeplearning/cudnn/latest/fe-oss-apis/dsa.html">DeepSeek Sparse Attention (DSA) — NVIDIA cuDNN</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSelect">GitHub - deepseek-ai/ DeepSelect : DeepSelect : TopK kernels for...</a></li>

</ul>
</details>

**Tags**: `#TopK kernel`, `#sparse attention`, `#performance optimization`, `#DeepSeek`, `#open source`

---

<a id="item-tech-news-12"></a>
### [Chinese AI chipmakers raise prices as HBM shortage bites](https://www.reuters.com/world/asia-pacific/chinas-ai-chipmakers-raise-prices-high-bandwidth-memory-shortage-bites-2026-09-10/) ⭐️ 7.0/10

Chinese AI chipmakers Huawei and Cambricon are raising prices because high-bandwidth memory \(HBM\) supply remains tight and US export restrictions worsen supply pressure. Huawei&\#x27;s Ascend 950DT quotes are about 20%–50% higher than two months ago, with some older chips up about 30%, while Cambricon&\#x27;s next-generation Siyuan 690 is expected to rise roughly 20%–30%. HBM is mainly supplied by SK Hynix, Samsung, and Micron. As domestic AI compute demand grows, HBM shortages are becoming a key bottleneck limiting the expansion of domestic AI chips.

telegram · zaihuapd · Sep 10, 09:29

**「Background」** High-bandwidth memory \(HBM\) is a stacked DRAM technology that provides the high data throughput AI accelerators such as Huawei’s Ascend and Cambricon’s Siyuan chips require. Global HBM supply is concentrated among SK Hynix, Samsung, and Micron, while US export restrictions have compounded China’s access problems, turning memory availability into a critical bottleneck for domestic AI chip production.

**「Impact」** Chinese AI hardware buyers face significantly higher procurement costs and constrained chip availability as HBM shortages and export controls persist.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/china-ai-chipmakers-raise-prices-hbm-shortage/">China&#x27;s AI chipmakers hike prices up to 50% as high-bandwidth memory shortage bites</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#HBM`, `#supply chain`, `#China`, `#semiconductors`

---

<a id="item-tech-news-13"></a>
### [Tencent Hunyuan Releases Open-Source Audio Editing Model AuK](https://x.com/TencentHunyuan/status/2097996926876795197) ⭐️ 7.0/10

Tencent Hunyuan announced the release of AuK, an open-source audio editing model that uses natural language instructions and reference audio for unified speech generation and editing. It supports zero-shot text-to-speech, timbre/style/emotion editing, accent removal, and multi-speaker separation. The company also released AuK-Flash, a 4-step inference variant that is about 4.5x faster under matching conditions. Code, model weights, and demos are available. The announcement highlights capabilities but does not include deep technical benchmarks.

telegram · zaihuapd · Sep 10, 11:56

**「Background」** AuK is a 1.5B-parameter open-weights speech model released under the MIT license, designed to handle cloning, editing, and enhancement tasks from natural-language instructions and reference audio \(tool-1-2\). The project publishes code, model weights, and a demo, and a technical report notes that dedicated denoisers and separators can still outperform it on pure signal-to-noise metrics, while AuK trades some of that edge for unified control across tasks \(tool-1-1, tool-1-3\).

**「Impact」** Developers can now download the open weights and code to build or integrate AuK into TTS, voice editing, and audio separation applications, with AuK-Flash providing around 4.5x faster inference under the stated matching conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/AuK">GitHub - Tencent-Hunyuan/AuK: AuK: An Open-Source Foundational Model for Speech Generation and Editing · GitHub</a></li>
<li><a href="https://www.orcarouter.ai/blog/auk-open-weights-speech-explained">AuK Technical Report: Tencent&#x27;s 1.5B Open Speech Model</a></li>
<li><a href="https://alphasignal.ai/news/tencent-s-auk-replaces-16-speech-tools-with-one-open-source-model">Tencent&#x27;s AuK Replaces 16 Speech Tools With One Open-Source Model | AlphaSignal</a></li>

</ul>
</details>

**Tags**: `#audio generation`, `#open-source AI`, `#text-to-speech`, `#speech editing`, `#Tencent`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Kalshi launches CFTC-approved gold and silver perpetual futures](https://www.cnbc.com/2026/09/10/kalshi-launches-perps-for-gold-and-silver-following-cftc-approval-expanding-futures-offerings.html) ⭐️ 8.0/10

Kalshi launched CFTC-approved perpetual futures on gold and silver on Thursday, the first non-crypto perps approved in the U.S. Its earlier crypto perps have done $44 billion in notional volume since late May, according to the platform&\#x27;s website.

rss · CNBC Finance · Sep 10, 14:00

**「Background」** Kalshi first won CFTC approval for crypto perpetual futures in late May and filed for the gold and silver contracts in July; perpetual futures are contracts with no expiration that track an asset&\#x27;s price through a funding mechanism.

**「Impact」** The launch intensifies competition for traditional futures exchanges; CBOE and CME Group shares fell on disruption fears and CME has sued the CFTC to block approval of perps.

**Tags**: `#perpetual futures`, `#CFTC`, `#gold`, `#silver`, `#commodity derivatives`

---

<a id="item-finance-news-2"></a>
### [Apple prices first foldable iPhone Duo at 15,999 yuan in China](https://www.cnbc.com/2026/09/11/the-iphone-duo-enters-chinas-crowded-foldable-market.html) ⭐️ 7.0/10

Apple announced its first foldable iPhone, the iPhone Duo, at 15,999 yuan \($2,230\) in China, where early WeChat reactions focused on price compared with domestic rivals Xiaomi \(10,999 yuan\) and Huawei \(19,999 yuan\).

rss · CNBC Finance · Sep 11, 00:19

**「Background」** China is Apple&\#x27;s third-largest market, accounting for about 17% of revenue, and domestic rivals Huawei, Xiaomi, Honor, Oppo and Vivo already sell foldables in book-style, flip and triple-screen formats.

**「Impact」** Mainland Chinese buyers of the iPhone Duo may need to visit a carrier store for ID verification to activate an eSIM because the device lacks a physical SIM-card slot.

**Tags**: `#Apple`, `#foldable phones`, `#China smartphone market`, `#product launch`, `#competition`

---

<a id="item-finance-news-3"></a>
### [Premarket Movers: Macy&\#x27;s Raises Guidance, Copper Miners Slide](https://www.cnbc.com/2026/09/10/stocks-making-the-biggest-moves-premarket-.html) ⭐️ 7.0/10

Premarket trading saw sharp moves across retail, tech, energy, and mining after a wave of earnings and corporate news. Macy&\#x27;s raised its full-year guidance for net sales, comparable sales, and earnings per share after a second-quarter revenue beat, while copper miners fell as copper prices retreated from a record high.

rss · CNBC Finance · Sep 10, 11:54

**「Background」** Copper prices had been pushed higher this year by tariff threats before Thursday&\#x27;s decline, dragging Freeport-McMoRan down nearly 7% and Southern Copper down more than 6%.

**Tags**: `#premarket movers`, `#earnings`, `#mergers and acquisitions`, `#copper prices`, `#stock market`

---

<a id="item-finance-news-4"></a>
### [Ant International, Visa and Mastercard to develop common AI agent payment standards](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 7.0/10

Ant International has partnered with Visa and Mastercard to develop common “Know Your Agent” standards for payments made by AI agents. The companies cited McKinsey projections that AI agents will handle $3 trillion to $5 trillion in global consumer commerce by 2030.

rss · CNBC Finance · Sep 10, 01:53

**「Background」** Visa, Mastercard and Ant International had each previously announced their own separate protocols for AI agents to complete payments securely.

**「Impact」** Payment firms, merchants and AI-agent developers could avoid duplicate agent registration across different systems if the common standards are adopted, according to Ant International.

**Tags**: `#AI payments`, `#Ant International`, `#Visa`, `#Mastercard`, `#digital wallets`

---