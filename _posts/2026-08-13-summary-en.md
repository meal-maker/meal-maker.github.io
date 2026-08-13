---
layout: default
title: "Horizon Summary: 2026-08-13 (EN)"
date: 2026-08-13
lang: en
---

> From 42 items, 21 important content pieces were selected

---

**Technology News**
1. [Cerebras and OpenAI Claim 7x Faster GPT-5.6 Sol Inference](#item-tech-news-1) ⭐️ 8.0/10
2. [Spaghettifying DRAM](#item-tech-news-2) ⭐️ 8.0/10
3. [DeepSeek V4 Pro 0813 Available with 1.7T Open Weights](#item-tech-news-3) ⭐️ 8.0/10
4. [Trump Memo Lets Supervised Firms Conduct Overseas Surveillance and Cyberattacks](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepMind SL2T Brings Sign Language AI to Pixel 11](#item-tech-news-5) ⭐️ 8.0/10
6. [DeepSeek-V4-Pro Official Release and Peak/Off-Peak API Pricing](#item-tech-news-6) ⭐️ 8.0/10
7. [OpenAI Previews Ultrafast Mode for GPT-5.6 Sol](#item-tech-news-7) ⭐️ 8.0/10
8. [Gemini 3.7 Flash](#item-tech-news-8) ⭐️ 7.0/10
9. [DeepSeek Harness Developer Preview Offers Traceable Plugin-Based AI Agents](#item-tech-news-9) ⭐️ 7.0/10
10. [Choose Boring Technology: Spend Innovation Tokens Sparingly](#item-tech-news-10) ⭐️ 7.0/10
11. [City2Graph Python Library for Heterogeneous Urban Graph Neural Networks](#item-tech-news-11) ⭐️ 7.0/10
12. [Worldproof: Diagnosing World-Model Failures and Pixel Metric Limits on Robot Video](#item-tech-news-12) ⭐️ 7.0/10
13. [Claude Chrome Extension Adds Cross-Device Session Continuity and Auto-Approve Mode](#item-tech-news-13) ⭐️ 7.0/10
14. [DeepSeek Harness Released; DeepSeek-V4-Pro-0813 Weights Opened](#item-tech-news-14) ⭐️ 7.0/10
15. [Google Releases Gemini 3.7 Flash Three Weeks After 3.6](#item-tech-news-15) ⭐️ 7.0/10

**Financial News**
1. [CXMT Overtakes Tencent as China&\#x27;s Most Valuable Company](#item-finance-news-1) ⭐️ 8.0/10
2. [S&amp;P 500 profit margins hit a record 16.9% in Q2](#item-finance-news-2) ⭐️ 7.0/10
3. [Steve Eisman Warns AI Boom Depends on OpenAI and Anthropic](#item-finance-news-3) ⭐️ 7.0/10
4. [Chinese YMTC Tops Micron and Kioxia in NAND Chip Shipments](#item-finance-news-4) ⭐️ 7.0/10
5. [China EV sales reach 65.1% of July new passenger car sales](#item-finance-news-5) ⭐️ 7.0/10
6. [China&\#x27;s gig workforce tops 53m as slowdown squeezes jobs](#item-finance-news-6) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Cerebras and OpenAI Claim 7x Faster GPT-5.6 Sol Inference](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras and OpenAI have announced an &\#x27;Ultrafast&\#x27; inference mode for GPT-5.6 Sol that they claim runs 7× faster on Cerebras specialized hardware. The announcement reports that Ultrafast mode answered all 2,500 HLE benchmark questions in 11 hours and 11 minutes, while Claude Fable 5 required 78 hours and 27 minutes to reach the same conclusions. The companies describe this as working through the frontier of human knowledge in a single working day with comparable accuracy. The result is presented as an infrastructure optimization rather than a new model paradigm, and external verification details are still limited.

hackernews · pr337h4m · Aug 13, 18:10 · [Discussion](https://news.ycombinator.com/item?id=49289844)

**「What is Ultrafast mode and HLE?」** Humanity&\#x27;s Last Exam \(HLE\) is a 2,500-question benchmark spanning graduate-level subjects such as chemistry, economics, and literature, typically answerable only by PhD holders. Ultrafast is a new OpenAI API service tier for GPT-5.6 Sol powered by Cerebras hardware, advertised to run up to 14× faster and deliver up to 750 output tokens per second.

**「Impact」** If the claimed 7× speedup holds, developers and enterprises using Cerebras hardware could run full HLE benchmark workloads in a single working day rather than more than three days, but official pricing and exact parity with standard GPT-5.6 Sol remain unconfirmed.

**「Community Discussion」** Commenters are excited by the claimed speedup but skeptical about evidence; several note the posts do not explicitly state that Ultrafast matches standard GPT-5.6 Sol performance, and pricing has not been disclosed. Others argue speed itself improves reasoning quality by enabling iterative passes, and hope the mode becomes publicly available.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed - OpenAI</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/cerebras-powers-ultrafast-mode-openai-170000002.html">Cerebras Powers Ultrafast Mode for OpenAI&#x27;s GPT-5.6 Sol</a></li>

</ul>
</details>

**Tags**: `#AI`, `#large language models`, `#hardware acceleration`, `#OpenAI`, `#Cerebras`

---

<a id="item-tech-news-2"></a>
### [Spaghettifying DRAM](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

The GitHub project &quot;Spaghettifying DRAM&quot; presents a tool and technical exploration for directly manipulating DRAM behavior on AMD Jaguar processors, with notes that Zen3 uses a different memory controller register base address. It targets the 2013 AMD Jaguar architecture and expands the attack surface for system security by exposing low-level DRAM control. Community discussion anticipates an accompanying Black Hat talk by Christopher Domas and asks which newer CPUs are affected beyond the documented Jaguar target.

hackernews · matt\_d · Aug 13, 14:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**「DRAM address translation and hidden carveouts」** Modern x86 systems map physical DRAM addresses through a memory controller that translates them into row, column, and bank accesses, and firmware often reserves hidden address ranges \(carveouts\) for System Management Mode, confidential computing, or other privileged contexts. The skitter-creek-bath-salts tool targets AMD Jaguar and reports different memory-controller register base addresses for Zen 3, allowing ring-0 code to alter these translations so that normal memory accesses land in those otherwise inaccessible carveouts. This concept builds on earlier research into &\#x27;negative ring&\#x27; firmware secrets and is relevant to hardware security researchers and console security teams.

**「Community Discussion」** Commenters express excitement for Christopher Domas&\#x27;s upcoming Black Hat talk and note the large attack surface created by modern DRAM complexity. Several ask whether the technique works on CPUs newer than the 2013 AMD Jaguar, observing that only a base-address difference is noted for Zen3.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#hardware security`, `#low-level programming`, `#exploitation`, `#reverse engineering`

---

<a id="item-tech-news-3"></a>
### [DeepSeek V4 Pro 0813 Available with 1.7T Open Weights](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek&\#x27;s latest Pro model, V4 Pro 0813, is available through OpenRouter&\#x27;s API, and its open weights have now been published on Hugging Face under deepseek-ai/DeepSeek-V4-Pro-0813 at 1.7 trillion parameters and 893 GB. DeepSeek has not posted an official announcement page, so Simon Willison linked to OpenRouter as the primary reference. He also observed that the model&\#x27;s low, medium, and high reasoning levels produced visibly different pelican illustrations, a behavior he has not seen with other models. Benchmark figures reportedly circulated through DeepSeek&\#x27;s WeChat group, were reposted in a deleted Reddit thread, and appeared in an ASCII-art table on Hacker News. This release follows earlier open-weight DeepSeek V4 Pro and V4 Flash models, continuing DeepSeek&\#x27;s pattern of open-source LLM availability.

rss · Simon Willison · Aug 12, 23:59

**「Background」** DeepSeek is a Chinese AI research company known for releasing open-weight large language models, including April&\#x27;s DeepSeek-V4-Pro and July&\#x27;s DeepSeek-V4-Flash-0731 on Hugging Face. OpenRouter is an API aggregator that offers unified access to many large language models. Since DeepSeek provided no dedicated announcement for the new model, OpenRouter served as the publicly accessible reference point.

**「Impact」** Developers and researchers can now download and run the 1.7T parameter DeepSeek V4 Pro 0813 locally from Hugging Face, though the 893 GB footprint requires high-end hardware.

**Tags**: `#deepseek`, `#open-source-ai`, `#large-language-models`, `#ai-release`, `#huggingface`

---

<a id="item-tech-news-4"></a>
### [Trump Memo Lets Supervised Firms Conduct Overseas Surveillance and Cyberattacks](https://www.bloomberg.com/news/articles/2026-08-13/trump-enlists-private-sector-to-boost-cyber-offensive-arsenal) ⭐️ 8.0/10

President Trump signed a memorandum allowing private companies under direct federal control and supervision to conduct overseas surveillance and cyberattacks against foreign cyber-enabled transnational criminal organizations targeting Americans. The Department of Homeland Security will run the program, coordinating oversight with the Department of Justice. Participating firms must maintain at least a $1 million compliance bond or escrow, which can be forfeited if they fail to meet contract terms.

telegram · zaihuapd · Aug 13, 05:10

**「Background」** The action takes the form of a National Security Presidential Memorandum and reverses decades of U.S. policy that prohibited private companies from conducting offensive cyber operations or &quot;hack back&quot; attacks. Under the announced framework, the Department of Homeland Security will oversee participating firms in coordination with the Justice Department, and companies must keep at least $1 million in bond or escrow.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/">In a first, US will allow some private firms to carry out ...</a></li>
<li><a href="https://cybersecuritynews.com/trump-memos-private-firms-cyber/">Trump Signs Memo Authorizing Private Firms for Cyber ...</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/trump-signs-memo-allowing-us-091707731.html?fr=sycsrp_catchall">Trump signs memo allowing US firms to carry out cyber attacks</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#offensive cyber operations`, `#technology policy`, `#government surveillance`, `#private sector`

---

<a id="item-tech-news-5"></a>
### [DeepMind SL2T Brings Sign Language AI to Pixel 11](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

Google DeepMind released SL2T, a large multilingual sign language-to-text model. It first ships in Pixel 11&\#x27;s Gboard and Live Transcribe, supporting American Sign Language to English, with more devices and languages to follow. The model was trained on over 100,000 hours of data across more than 50 sign languages. On the FLEURS-ASL benchmark it achieves a zero-shot score of 70 BLEURT, far above previous records. For privacy, it processes only hand and body pose keypoints and does not read raw video.

telegram · zaihuapd · Aug 13, 08:55

**「Background」** Sign language-to-text systems traditionally analyze video frames, which can expose sensitive visual data and require significant on-device compute. Keypoint-based processing extracts only skeletal coordinates of hands and body, reducing privacy risk and bandwidth. FLEURS-ASL is a benchmark for sign language translation, and BLEURT is a learned metric for evaluating generated text quality.

**「Impact」** Pixel 11 owners can use Gboard and Live Transcribe to transcribe American Sign Language into English without sending raw video to Google, with additional languages and devices expected later.

**Tags**: `#sign-language-recognition`, `#accessibility`, `#deepmind`, `#on-device-ai`, `#machine-translation`

---

<a id="item-tech-news-6"></a>
### [DeepSeek-V4-Pro Official Release and Peak/Off-Peak API Pricing](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 8.0/10

DeepSeek-V4-Pro has been officially released on the app, web, and API platforms. The model, available as deepseek-v4-pro, enhances agent capabilities and natively supports the Responses API format, with adaptation for Codex. Both V4-Pro and V4-Flash thinking modes now offer three levels: low, high, and max. The API will introduce peak and off-peak pricing effective August 17, 2026 at 00:00, with off-peak prices set at half of peak-hour prices.

telegram · zaihuapd · Aug 13, 11:12

**「Background」** DeepSeek’s V4 lineup includes V4-Pro and V4-Flash, and this release makes V4-Pro generally available while keeping the existing \`deepseek-v4-pro\` model name in the API. Previously the API used flat usage-based pricing; the V4 release introduces peak and off-peak rates, with off-peak set at half the peak price, and V4-Pro adds native OpenAI Responses API support for Codex agent workflows.

**「Impact」** From 2026-08-17, DeepSeek V4 API billing shifts to peak/off-peak rates \(off-peak is half of peak\), and external reports indicate increases of up to 1,100% over current prices depending on model, token type, and time. Developers should schedule non-urgent workloads off-peak or budget for peak-hour surge costs.

<details><summary>References</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260813/">DeepSeek-V4-Pro GA Release | DeepSeek API Docs</a></li>
<li><a href="https://x.com/deepseek_ai/status/2087864589895798968">API pricing update 💰 With the V4 lineup release, we&#x27;re ...</a></li>
<li><a href="https://deepseek.day/en/blog/deepseek-v4-peak-pricing-launch/">DeepSeek V4 Official Launch Mid-July! Peak-Valley API Pricing ...</a></li>
<li><a href="https://runaihome.com/blog/deepseek-v4-peak-pricing-gpu-roi-2026/">DeepSeek V4 Peak-Hour Pricing 2026: Does the 2× Surcharge ...</a></li>
<li><a href="https://techstartups.com/2026/08/13/deepseek-raises-v4-api-prices-by-up-to-1100-just-as-chinese-ai-startup-launches-deepseek-v4-pro/">DeepSeek raises V4 API prices by up to 1,100% just as Chinese ...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI`, `#API pricing`, `#release`, `#machine learning`

---

<a id="item-tech-news-7"></a>
### [OpenAI Previews Ultrafast Mode for GPT-5.6 Sol](https://openai.com/index/previewing-ultrafast/) ⭐️ 8.0/10

OpenAI has previewed an Ultrafast inference mode for GPT-5.6 Sol, claiming up to 14x faster processing than standard and a maximum throughput of 750 tokens per second. The mode is available first through the OpenAI API and is powered by Cerebras. It is aimed at time-sensitive use cases such as incident response, financial research, customer service, and e-commerce. Access is currently limited to a small set of customers in a limited preview, and OpenAI says it will gradually expand access as compute capacity grows.

telegram · zaihuapd · Aug 13, 17:04

**「Context」** Ultrafast mode is a new OpenAI API service tier that runs the GPT-5.6 Sol model on Cerebras inference hardware, separate from OpenAI&\#x27;s standard serving path. The advertised 750 output tokens per second is a measure of text-generation throughput, and the tier is initially available only to a select group of API customers.

**「Impact」** Developers using the OpenAI API for latency-sensitive applications may see substantially faster responses from GPT-5.6 Sol once the preview expands beyond the current limited set of customers.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to ... - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI inference`, `#latency`, `#Cerebras`, `#LLM`

---

<a id="item-tech-news-8"></a>
### [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

Google has introduced Gemini 3.7 Flash, a new large language model in the Gemini family, with model documentation available at ai.google.dev/gemini-api/docs/models/gemini-3.7-flash. The submitted link contains limited technical detail, but Hacker News commenters are actively evaluating the model on tasks such as image-to-HTML conversion and different reasoning levels. Community discussion highlights unusual introductory pricing that is scheduled to double on December 31, 2026; one comment quotes post-introductory rates of $1.50 per 1M input tokens and $7.50 per 1M output tokens from January 1, 2027. Commenters also compare the model&\#x27;s benchmarks and cost against rivals such as GPT-5.6 Luna and Opus 5, with some arguing that cheaper alternatives undercut the need for Flash.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**「Background」** Gemini is Google&\#x27;s family of large language models, and the Flash line targets lower-cost, faster inference for high-volume or latency-sensitive tasks. Gemini 3.7 Flash is built on the preceding Gemini 3.6 Flash model and was released in August 2026, following shortly after that predecessor. Independent analysis describes it as leading in intelligence for its price, notably fast, and fairly concise.

**「Impact on developers」** Developers building coding and agent workflows get immediate performance improvements and lower introductory pricing with Gemini 3.7 Flash, though Google has not disclosed when its flagship Pro model will arrive.

**「Community Discussion」** Commenters note that Gemini 3.7 Flash performs respectably on image-to-HTML conversion relative to its price, though Opus 5 remains better; several users question the introductory pricing and argue that models like GPT-5.6 Luna offer stronger benchmark results at lower cost, particularly on DeepSWE 1.1.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-7-flash/">Gemini 3 . 7 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-3-7-flash">Gemini 3 . 7 Flash (high) - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://www.androidheadlines.com/2026/08/google-gemini-3.7-flash-launch-price-cut-performance-boost.html">Google Drops Gemini 3.7 Flash AI Model with Price Cut</a></li>
<li><a href="https://www.reuters.com/business/google-unveils-gemini-37-flash-ai-model-coding-agent-workflows-2026-08-13/">Google unveils Gemini 3.7 Flash AI model for coding, agent ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Gemini`, `#model release`, `#Google`

---

<a id="item-tech-news-9"></a>
### [DeepSeek Harness Developer Preview Offers Traceable Plugin-Based AI Agents](https://deepseek.com/harness/en/) ⭐️ 7.0/10

DeepSeek has released an early MIT-licensed developer preview of DeepSeek Harness, an open-source framework for building traceable AI agents with a plugin architecture based on the newly released Cordis v4 paper. The preview records an append-only session log of everything the model sees—system prompts, reasoning, tool calls and results, subagent scheduling, and context injection—enabling inspection, resumption, forking, and replay from the same event stream. The framework treats nearly every component as a plugin and supports hot-loading and unloading of plugins with state and side-effect rollback, without restarting the process. The project is explicitly not production-ready, with rough edges and compatibility-breaking changes expected, and the authors invite feedback.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**「Background」** DeepSeek Harness is an early MIT-licensed developer preview that presents an open-source framework for building traceable AI agents; its source code was released alongside the preview. It implements every agent capability as a plugin, and its plugin architecture builds on the newly published Cordis v4 paper, which describes hot-reloading and unloading of plugins with automatic reversion of side effects. The preview explicitly warns that compatibility-breaking changes are expected as it iterates rapidly, so it is not production-ready.

**「Impact」** Developers can now experiment with fully traceable AI agent runs and hot-swappable plugins, but should avoid production use until the preview stabilizes because breaking changes are likely.

**「Community Discussion」** Commenters highlight the append-only traceability and hot-reload lifecycle as standout features, while some report plugin fatigue and one reader finds the underlying Cordis v4 paper &\#x27;useful, but not that useful.&\#x27;

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview : Everything is a plugin</a></li>
<li><a href="https://qcode.cc/en/deepseek-harness-guide">DeepSeek Harness + Cordis (2026): Developer Preview ... | QCode.cc</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>

</ul>
</details>

**Tags**: `#deepseek`, `#ai-agents`, `#open-source`, `#developer-tools`, `#traceability`

---

<a id="item-tech-news-10"></a>
### [Choose Boring Technology: Spend Innovation Tokens Sparingly](https://mcfunley.com/choose-boring-technology) ⭐️ 7.0/10

Dan McKinley&\#x27;s 2015 essay &\#x27;Choose Boring Technology&\#x27; argues that engineering teams should limit innovation to a few critical areas and use proven, boring technology elsewhere. It introduces the &\#x27;innovation tokens&\#x27; concept: each company has a fixed supply of about three tokens to spend on novel technology choices, because every new tool adds operational burden and risk. The essay advises defaulting to well-understood technologies unless there is a compelling reason to adopt something new, and it remains influential among software engineers, engineering managers, and product managers. The piece is a classic in engineering decision-making, not a new development but still widely referenced.

hackernews · tosh · Aug 13, 17:48 · [Discussion](https://news.ycombinator.com/item?id=49289512)

**「Background」** Dan McKinley&\#x27;s 2015 essay argues that teams have a limited budget of roughly three &quot;innovation tokens&quot; for adopting new technology, so each choice like NodeJS or MongoDB consumes one token. He defines &quot;boring technology&quot; as technology that is familiar, well-established, well-tested, and widely adopted, and recommends using it except where innovation directly benefits the business. The essay also exists as a spoken-word version presented at conferences.

**「Impact」** Engineering teams that adopt the innovation-token heuristic are likely to concentrate novel technology adoption in a few high-value areas and use proven tools elsewhere, reducing operational overhead and integration risk.

**「Community Discussion」** Commenters largely praise the concept, with one noting it helps explain tradeoffs to colleagues at all levels and another suggesting that in the age of AI agents, teams should push all innovation tokens into agents and use &\#x27;in-distribution&\#x27; boring tech like Rust. However, some push back that the token metaphor is arbitrary and engineers should evaluate technologies on actual requirements and risks, while others note a shortage of companies that actually practice this pragmatism.

<details><summary>References</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Choose Boring Technology - Dan McKinley</a></li>
<li><a href="https://boringtechnology.club/">Choose Boring Technology</a></li>
<li><a href="https://jadon.us/posts/notes-on-choose-boring-technology/">Notes on - Choose Boring Technology by Dan McKinley</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#architecture`, `#innovation tokens`, `#technology strategy`, `#engineering management`

---

<a id="item-tech-news-11"></a>
### [City2Graph Python Library for Heterogeneous Urban Graph Neural Networks](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph is a new Python library for converting geospatial urban data into heterogeneous graphs for spatial analysis, network analysis, and Graph Neural Networks; the associated paper was published as Sato et al., Computers, Environment and Urban Systems, 130, 102492 \(2026\). It constructs morphological graphs from OpenStreetMap and Overture Maps buildings, streets, and tessellated urban fabric, and imports GTFS/GBFS transit feeds through DuckDB with stop-to-stop graph aggregation, as well as OD matrices and flow data as weighted spatial graphs. Proximity and contiguity methods include KNN, Delaunay, Gilbert, Waxman, and queen/rook contiguity under Euclidean, Manhattan, or network distances. The library supports multiple node and edge types in one graph, metapath-derived edges, and round-trip conversion between GeoDataFrames, NetworkX, rustworkx, and PyTorch Geometric Data/HeteroData while preserving geometries and attributes.

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · Aug 13, 11:59

**「Background」** City2Graph is a Python library for converting urban geospatial datasets—such as buildings, streets, transit feeds, and origin-destination matrices—into graph structures for spatial network analysis and graph neural networks \(GNNs\). It provides interfaces to GeoPandas, NetworkX, and PyTorch Geometric, allowing users to move between tabular geospatial data and heterogeneous graph representations. The library is motivated by the idea that urban systems are better modeled as heterogeneous graphs than as flat feature tables, preserving relational and structural information for GeoAI applications.

**「Impact」** Urban computing researchers and GeoAI practitioners now have a citable open-source tool that preserves geometry and graph structure when converting OSM/Overture, GTFS/GBFS, and mobility data into GNN-ready heterogeneous graphs.

<details><summary>References</summary>
<ul>
<li><a href="https://city2graph.net/">city2graph — GeoAI with Graph Neural Network (GNN) in Python</a></li>
<li><a href="https://medium.com/@yuta.sato.now/city2graph-a-python-package-for-spatial-network-analysis-and-graph-neural-networks-gnns-bc943dd6d85e">city2graph: A Python package for GeoAI with GNNs and spatial network analysis</a></li>
<li><a href="https://github.com/c2g-dev/city2graph">GitHub - c2g-dev/city2graph: Transform geospatial relations into graphs for Graph Neural Networks and spatial network analysis · GitHub</a></li>

</ul>
</details>

**Tags**: `#python`, `#graph-neural-networks`, `#geospatial-analysis`, `#urban-computing`, `#open-source`

---

<a id="item-tech-news-12"></a>
### [Worldproof: Diagnosing World-Model Failures and Pixel Metric Limits on Robot Video](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

The post introduces worldproof, an Apache-2.0 open-source tool \(pip install worldproof\) for diagnosing world-model prediction failures by comparing rollouts to ground truth and physical invariants, reporting horizon curves for PSNR, SSIM, LPIPS, and other metrics. While validating it, the author found that a copy-last-frame baseline on a real SO-101 arm recording scores 0.983 SSIM and 53.9 dB PSNR, with error that stays flat across 1–6 steps, meaning pixel metrics cannot rank models in that setup. On DROID footage at 15fps and 48-step rollouts, the same baseline shows near-perfect ties for steps 1–3, a steep monotonic decline from steps 4–24, and then a floor around 0.20 SSIM/10.3 dB from step 28 onward, suggesting only the roughly 8–24 step window separates models. Evaluation used 64 rollouts, interquartile mean with stratified bootstrap CIs following Agarwal et al. 2021, and dynamic-region masking to avoid static background inflation; caveats include LPIPS failure to separate datasets and step 0 inflating summary scalars due to high frame rate, with the tool still v0.1 and acknowledging tracker/FVD limitations.

reddit · r/MachineLearning · /u/georgia\_bucea · Aug 13, 19:58

**「Background」** World models predict future video frames from an initial context and a sequence of actions, and are often evaluated with pixel-fidelity metrics such as SSIM, PSNR, and LPIPS. A copy-last-frame baseline simply predicts that nothing changes and serves as a naive reference. Summary metrics over the prediction horizon can hide where predictions degrade, so horizon curves are needed to reveal the usable evaluation window.

**「Impact」** For researchers evaluating world models on real robot video, the usable evaluation horizon should be measured per dataset rather than inherited from papers; on the tested 15fps DROID-like footage, only the roughly 8–24 step range can separate a trivial baseline from better models. A real model may remain correlated longer and extend that upper bound, so this is a lower-bound diagnostic rather than a universal cutoff.

**Tags**: `#world-models`, `#evaluation-metrics`, `#robotics`, `#open-source-tool`, `#machine-learning`

---

<a id="item-tech-news-13"></a>
### [Claude Chrome Extension Adds Cross-Device Session Continuity and Auto-Approve Mode](https://techmymoney.com/2026/08/12/claude-in-chrome-now-carries-your-session-to-the-desktop/) ⭐️ 7.0/10

Anthropic has rebuilt the Claude Chrome extension to run full Cowork sessions, letting a task started in the browser continue on desktop, web, and mobile apps with conversations, skills, and connectors synced through the account. The update is available today for Max and Team users, will reach Pro users in the coming weeks, and is off by default for enterprise plans where admins must enable it. It adds an &quot;auto-approve&quot; mode, but actions such as form submissions, messages, and file downloads are compared with the original instructions, while purchases and personal data still require manual confirmation. Anthropic says the measures reduce but do not eliminate risk, and malicious instructions in webpages remain a challenge. Local files, other Chromium browsers, and mobile are not yet supported.

telegram · zaihuapd · Aug 13, 04:10

**「Background」** Claude&\#x27;s Chrome extension previously provided limited assistant actions within the browser. Cowork is Anthropic&\#x27;s multi-step agentic session format that can use skills and connectors to complete tasks. An auto-approve mode is a permission setting that allows the assistant to take actions without prompting for each step, subject to safety checks.

**「Impact」** For Max and Team accounts, browser-initiated Cowork tasks can now follow the user across devices immediately, while Pro users must wait a few weeks and enterprise deployments stay off by default.

**Tags**: `#Claude`, `#Anthropic`, `#Chrome extension`, `#AI assistant`, `#cross-device sync`

---

<a id="item-tech-news-14"></a>
### [DeepSeek Harness Released; DeepSeek-V4-Pro-0813 Weights Opened](https://mp.weixin.qq.com/s/mANdGRI4fO_sEbC1ECEoZQ) ⭐️ 7.0/10

DeepSeek has released Harness, an MIT-licensed application that treats model, tools, skills, sessions, sandbox, storage, scheduling, and UI as replaceable plugins, offering standard, PTC, minimalist, and creative run modes. The GitHub repository is now open and uses an &quot;everything is a plugin&quot; architecture driven by Cordis. Weights for DeepSeek-V4-Pro-0813 were opened on Hugging Face, and the Hugging Face page temporarily returned a 404 error before being restored.

telegram · zaihuapd · Aug 13, 12:39

**「Context」** An agent harness is a framework for coordinating models, tools, sandboxes, and user interfaces into a unified agent system. The official DeepSeek Harness repository describes its &quot;everything is a plugin&quot; design as powered by Cordis, with design details in the paper &quot;A Programming Paradigm for Spatiotemporal Composability.&quot;

**「Developer impact」** Developers can now adopt the MIT-licensed DeepSeek Harness and use the open DeepSeek-V4-Pro-0813 weights, gaining a plugin-based agent framework with replaceable model, tool, skill, session, sandbox, storage, scheduling, and UI components.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness ...</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek - ai / deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#AI model release`, `#open source`, `#plugin architecture`, `#Hugging Face`

---

<a id="item-tech-news-15"></a>
### [Google Releases Gemini 3.7 Flash Three Weeks After 3.6](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

On August 13, 2026, Google announced Gemini 3.7 Flash and began a gradual rollout to replace Gemini 3.6 Flash, which had launched only three weeks earlier. The update improves coding and agent performance, lifting FrontierCode 1.1 Main from 34.4% to 43.6% and DeepSWE v1.1 from 49% to 65.3%. Google also noted that the previously promised Gemini 3.5 Pro, expected in June, has still not been released. The rapid succession suggests an accelerated release cadence for Flash models, but the changes are incremental rather than foundational.

telegram · zaihuapd · Aug 13, 17:32

**「Background」** Gemini Flash models are lightweight, lower-latency variants in Google&\#x27;s Gemini family, positioned below the larger Pro models. FrontierCode and DeepSWE are benchmarks that evaluate coding ability and agentic software-engineering performance, respectively.

**「Impact」** Developers using Gemini Flash can expect improved coding and agent performance on FrontierCode and DeepSWE tasks, but the rapid replacement of 3.6 Flash may force quick migration or re-evaluation.

**Tags**: `#Gemini`, `#Google`, `#AI`, `#LLM`, `#software engineering`

---

## Financial News

<a id="item-finance-news-1"></a>
### [CXMT Overtakes Tencent as China&\#x27;s Most Valuable Company](https://www.bloomberg.com/news/articles/2026-08-13/cxmt-overtakes-tencent-to-become-most-valuable-chinese-company) ⭐️ 8.0/10

Chinese memory chip maker CXMT overtook Tencent to become China&\#x27;s most valuable company, with a market value of $524 billion versus Tencent&\#x27;s $510 billion as of Thursday, Bloomberg reported.

telegram · zaihuapd · Aug 13, 10:10

**「Background」** CXMT listed in Shanghai last month, surging 467% on its first day and then gaining another 8%, while Tencent&\#x27;s shares fell 4.5% on Thursday as it increased AI investment.

**Tags**: `#CXMT`, `#Tencent`, `#China stock market`, `#semiconductors`, `#market capitalization`

---

<a id="item-finance-news-2"></a>
### [S&amp;P 500 profit margins hit a record 16.9% in Q2](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 7.0/10

The S&amp;P 500’s blended net profit margin reached a record 16.9% in the second quarter, up from 14.8% in the first quarter and 12.9% a year earlier, according to FactSet data cited by CNBC.

rss · CNBC Finance · Aug 13, 20:21

**「Background」** Net profit margin is the share of revenue companies keep after paying all expenses, and the gain was broad-based: even excluding Alphabet and Amazon, the margin was 15%, also the highest since FactSet began tracking it in 2009.

**Tags**: `#profit margins`, `#S&amp;P 500`, `#stock market`, `#corporate earnings`, `#market analysis`

---

<a id="item-finance-news-3"></a>
### [Steve Eisman Warns AI Boom Depends on OpenAI and Anthropic](https://www.cnbc.com/2026/08/13/big-short-investor-steve-eisman-sees-an-achilles-heel-in-the-ai-boom.html) ⭐️ 7.0/10

Investor Steve Eisman warned that the AI boom is heavily dependent on OpenAI and Anthropic. He said the two startups account for roughly 70% of AI-related revenue at Microsoft, Amazon, Alphabet&\#x27;s Google and Oracle, and as much as 25% to 35% of their cloud revenue.

rss · CNBC Finance · Aug 13, 15:16

**「Background」** Eisman, best known for betting against the housing market ahead of the global financial crisis, is adding to a debate over whether AI spending can produce sufficient returns.

**Tags**: `#AI boom`, `#OpenAI`, `#Anthropic`, `#China`, `#cloud computing`

---

<a id="item-finance-news-4"></a>
### [Chinese YMTC Tops Micron and Kioxia in NAND Chip Shipments](https://www.cnbc.com/2026/08/13/chinese-firm-tops-micron-kioxia-shipments-nand-memory-chips.html) ⭐️ 7.0/10

Yangtze Memory Technologies \(YMTC\) reached third place globally in NAND memory chip shipments with a 14% share in the second quarter, surpassing Micron and Kioxia, according to Counterpoint Research.

rss · CNBC Finance · Aug 13, 02:59

**「Background」** Yangtze Memory Technologies \(YMTC\) is a Chinese NAND flash memory maker founded in 2016 with government investment, and it has been expanding domestic production capacity as U.S. export controls restrict access to advanced chipmaking equipment.

**「Competitive pressure on incumbent NAND suppliers」** YMTC&\#x27;s jump to third place in global NAND shipments adds competitive pressure on Micron and Kioxia, particularly as the Chinese firm expands beyond consumer applications toward the higher-value data-center segment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.notebookcheck.net/YMTC-builds-homegrown-NAND-production-line-to-sidestep-U-S-sanctions.1064510.0.html">YMTC builds homegrown NAND production line to sidestep U.S ...</a></li>
<li><a href="https://www.tradingkey.com/analysis/stocks/us-stocks/262101853-ymtc-overtakes-micron-kioxia-nand-shipments-global-third-tradingkey">YMTC NAND Shipments Jump to Third Globally, Surpassing Micron and Kioxia as Micron&#x27;s eSSD Pricing Power Faces Pressure</a></li>
<li><a href="https://seekingalpha.com/news/4632116-chinas-ymtc-overtakes-kioxia-micron-in-global-nand-shipments-counterpoint">China’s YMTC overtakes Kioxia, Micron in global NAND shipments: Counterpoint (MU:NASDAQ) | Seeking Alpha</a></li>

</ul>
</details>

**Tags**: `#NAND memory`, `#semiconductors`, `#YMTC`, `#market share`, `#China tech`

---

<a id="item-finance-news-5"></a>
### [China EV sales reach 65.1% of July new passenger car sales](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

New energy vehicles, including battery and hybrid cars, made up 65.1% of China&\#x27;s new passenger car sales in July, up from 54% a year earlier, according to China Passenger Car Association data. Overall passenger car sales fell 20.3% year over year through July, industry data showed.

rss · CNBC Finance · Aug 13, 01:31

**「Background」** The rankings use Autohome industry data for the six months through July; the new-energy vehicle share is from China Passenger Car Association data released Tuesday and covers battery and hybrid-powered cars.

**「Impact」** The rankings show domestic EV models led by Geely&\#x27;s Xingyuan and BYD are capturing China&\#x27;s top sales spots, while Volkswagen was the only traditional foreign automaker in the top 10.

**Tags**: `#China auto market`, `#electric vehicles`, `#auto sales data`, `#BYD`, `#Tesla`

---

<a id="item-finance-news-6"></a>
### [China&\#x27;s gig workforce tops 53m as slowdown squeezes jobs](https://www.ft.com/content/a3803e70-cb4d-444f-a31e-05be2f2c44f6?accessToken=zwAAAZ_5xcXzkdOjgD5wy01ET9OjHgW-LyxE9g.MEUCIQCWTIny3JTJV8e-PGyK0XL2tg5g_7Ay-rpKkwGZCpp1-AIgbMgJQPlqWgqAsX4s1k4gYaC4b8k0JveZOs35OJQvbZ4&amp;amp;sharetype=gift&amp;amp;token=7e8483bb-395d-429e-afca-2f4ab5ad150b) ⭐️ 7.0/10

China&\#x27;s economic slowdown is squeezing employment: as of 2025, food-delivery and ride-hailing gig workers exceeded 53 million, up 10 million in two years, yet the market remained oversupplied, according to a Financial Times report.

telegram · zaihuapd · Aug 13, 06:40

**「Background」** The report ties the oversupply to the property downturn, weak consumption, contraction in construction and manufacturing, and automation; Shenzhen declared its ride-hailing market saturated in June.

**「Impact」** Gig workers face falling incomes and longer hours, with airport taxi queues reaching up to 7 hours in Shanghai, 8 hours in Beijing and 10 hours in Chengdu.

**Tags**: `#中国经济`, `#就业`, `#零工经济`, `#网约车`, `#外卖`

---