---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 36 items, 12 important content pieces were selected

---

**Technology News**
1. [Google Announces Gemini 3.8 Live and Live Extended Thinking](#item-tech-news-1) ⭐️ 8.0/10
2. [We got admin access to Baseten&\#x27;s production GitHub in 25 minutes](#item-tech-news-2) ⭐️ 8.0/10
3. [Prior Labs Releases TabPFN-3.5 Tabular Foundation Model](#item-tech-news-3) ⭐️ 8.0/10
4. [Typesafe Launches System One Models and Jev for Fast Typed Inference](#item-tech-news-4) ⭐️ 7.0/10
5. [Internet Archive Details Wayback Machine Protections Against Scraper Traffic](#item-tech-news-5) ⭐️ 7.0/10
6. [Datacenter Moratoriums Are Not Killing the US Buildout](#item-tech-news-6) ⭐️ 7.0/10
7. [China’s 15th Five-Year Electronics Plan Targets Advanced Chips, HarmonyOS, RISC-V](#item-tech-news-7) ⭐️ 7.0/10
8. [Google Allows All Engineers to Use Anthropic&\#x27;s Claude Opus 5](#item-tech-news-8) ⭐️ 7.0/10
9. [MediaTek launches Dimensity 9600 Pro 2nm chip](#item-tech-news-9) ⭐️ 7.0/10
10. [Inside Project Lily: Humans Reading Real ChatGPT Chats](#item-tech-news-10) ⭐️ 7.0/10
11. [GPT-5.5 Deprecation Set for October 14, 2026](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s August retail sales miss forecasts as investment slump deepens](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google Announces Gemini 3.8 Live and Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) ⭐️ 8.0/10

Google announced Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, new model versions with live audio interaction and extended reasoning capabilities. The release targets developers and users of Google&\#x27;s Gemini AI and is described as enabling real-time conversational use with low latency. Community feedback highlights strengths in handling thick accents and non-English languages, with one user reporting impressive Afrikaans conversation and grammar practice while driving. Some commenters note the Live mode already feels more natural than GPT Voice and that the release is usable from Workspace accounts, though it is not yet available to Google AI Plus subscribers.

hackernews · leumon · Sep 15, 17:38 · [Discussion](https://news.ycombinator.com/item?id=49715947)

**「What are Gemini 3.8 Live and Extended Thinking?」** Gemini is Google&\#x27;s family of multimodal AI models, and earlier releases already offered a Live API for real-time spoken interaction. Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking are announced as the most advanced live dialogue models in the Gemini line: the standard Live model is built for scale, cost efficiency, fluid dialogue, and visual grounding, while the Extended Thinking model targets high-complexity tasks needing increased intelligence and multi-step reasoning.

**「Impact」** The new live modes are available now on Workspace accounts, giving enterprise users low-latency interactive voice, while personal Google AI Plus subscribers report they cannot yet access Gemini 3.8.

**「Community Discussion」** Community sentiment is largely positive, citing low latency, pleasant voices, and strong accent and Afrikaans handling, though some note Gemini 3.8 is not yet available for Google AI Plus users.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live &amp; Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://www.thurrott.com/a-i/google-gemini-a-i/341685/google-announces-gemini-3-8-live-and-3-8-live-extended-thinking">Google Announces Gemini 3 . 8 Live and 3 . 8 Live Extended Thinking</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#large-language-models`, `#google`, `#gemini`, `#live-api`

---

<a id="item-tech-news-2"></a>
### [We got admin access to Baseten&\#x27;s production GitHub in 25 minutes](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover) ⭐️ 8.0/10

An AI penetration-testing agent from Strix found a live Baseten GitHub personal access token for basetenbot in the public Docker build history within 25 minutes. The token granted admin and push access to Baseten&\#x27;s main product repository, GitOps repository, and Homebrew tap, plus read/write access to other private repositories including customer-specific repos. Baseten confirmed the issue as critical, made the Harbor project private, and rotated the token. The discovery shows how AI-assisted scanning can quickly surface leaked supply-chain credentials, though a motivated human could potentially find the same issue.

hackernews · bearsyankees · Sep 15, 18:11 · [Discussion](https://news.ycombinator.com/item?id=49716476)

**「Background」** Baseten is an ML inference service whose container images are published in a public Harbor registry, and Docker image configurations include a \`history\[\].created\_by\` field that can record build commands, sometimes leaking secrets passed at build time. GitHub personal access tokens \(PATs\) authenticate API and repository actions, so a leaked admin PAT could grant write access to production repositories. Strix is an open-source AI penetration testing tool that automates discovery of such exposures by inspecting artifacts like container layers.

**「Impact」** Baseten&\#x27;s main product, GitOps, and Homebrew repositories, along with customer-specific private repos, were exposed to admin-level compromise through the leaked basetenbot token until it was rotated.

**「Community Discussion」** Commenters praised Baseten&\#x27;s swift response, but debated whether the result demonstrates unique AI capability rather than faster execution of what a motivated human could also find, and raised legality concerns about autonomous penetration testing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.strix.ai/blog/baseten-harbor-github-pat-takeover">We wanted to use Baseten for inference. We ended up with admin access to their GitHub - Strix</a></li>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI agents`, `#DevSecOps`, `#software-supply-chain`, `#GitHub`

---

<a id="item-tech-news-3"></a>
### [Prior Labs Releases TabPFN-3.5 Tabular Foundation Model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a tabular foundation model that the announcement claims is state-of-the-art on TabArena and BeyondArena, including for datasets with up to 1 million rows and 20,000 features. It is offered in Fast \(alpha, about 6x faster than the base model\), Thinking \(available via API and trading compute for accuracy\), and Plus variants. On BeyondArena, TabPFN-3.5 reportedly leads on text-rich, high-cardinality, and high-dimensional data with +250 Elo over the strongest previous baseline and +150 Elo over the previous overall leader; Thinking adds +20 Elo over the base model on BeyondArena and +44 Elo on TabArena. These benchmark claims come from a Reddit announcement and have not been independently verified.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**「Background」** Prior Labs has been developing TabPFN as a tabular foundation model; the previous generation TabPFN-3 already reported strong TabArena results, including outperforming AutoGluon 1.5 while using substantially less runtime and no LLMs or real data. TabArena and BeyondArena are benchmark suites used to rank tabular models, and Prior Labs now reports TabPFN-3.5 ranks first on both.

**「Impact」** Machine learning practitioners considering tabular foundation models now have TabPFN-3.5 variants to evaluate, but should independently validate the reported state-of-the-art benchmark results before adoption.

<details><summary>References</summary>
<ul>
<li><a href="https://storage.googleapis.com/prior-labs-tabpfn-public/reports/TabPFN_3_model_report.pdf">TabPFN-3: Technical Report - Googleapis.com</a></li>
<li><a href="https://priorlabs.ai/technical-reports/tabpfn-3-5">Prior Labs</a></li>

</ul>
</details>

**Tags**: `#tabular data`, `#foundation model`, `#machine learning`, `#SOTA`, `#AutoML`

---

<a id="item-tech-news-4"></a>
### [Typesafe Launches System One Models and Jev for Fast Typed Inference](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 7.0/10

Typesafe.ai has introduced System One Models and Jev, a new type of model optimized for fast typed structured inference rather than general-purpose text generation. Unlike typical LLMs that produce free-form tokens, Jev takes arbitrary text input plus a set of predefined questions \(yes/no, multiple-choice, or scoring\) and returns structured answers such as choices with probabilities and confidence scores. The company positions it for tasks like classification and routing, with responses generated in milliseconds and at low cost \($0.042 per million tokens\). Community discussion on Hacker News notes the approach is genuinely interesting and potentially useful for AI engineering, though the speed comparison with general-purpose LLMs may be misleading because Jev cannot generate arbitrary code or handle tasks outside structured output.

hackernews · albelfio · Sep 15, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49717558)

**「Background」** System One models are a new class of AI models introduced by TypeSafe AI, designed for fast, structured decisions within software rather than general text generation. Jev is the first System One model, currently offered in early access, and serves as TypeSafe&\#x27;s flagship for this approach.

**「Impact」** Developers needing fast, cheap classification or structured decision-making can use Jev as a drop-in for slower general-purpose LLM calls in pipelines that reduce tasks to predefined yes/no, multiple-choice, or scoring questions.

**「Community Discussion」** Hacker News commenters generally praised the idea as novel and useful for typed inference, with one noting it fits well with design-by-contract patterns. However, several pointed out that the announcement lacks explanation and the speed comparison against general-purpose LLMs is misleading, recommending the documentation for technical details.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models &amp; Jev - TypeSafe AI Blog</a></li>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Structured Output`, `#LLMs`, `#Software Engineering`, `#New Models`

---

<a id="item-tech-news-5"></a>
### [Internet Archive Details Wayback Machine Protections Against Scraper Traffic](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 7.0/10

The Internet Archive announced on September 15, 2026 that it has implemented protections for the Wayback Machine in response to high-volume automated traffic from scrapers. The traffic is believed to come from scrapers attempting to bypass blocks on original sites by accessing archived copies. The protections are intended to keep the service running, but have caused access issues such as HTTP 429 rate-limit errors for some users, with reports of inconsistent behavior across devices and networks. The Archive also says some sites have already opted out due to the load, and it describes the scraping as harmful to non-profit internet infrastructure.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**「Background」** The Wayback Machine is a digital archive of the World Wide Web operated by the nonprofit Internet Archive, providing free access to historical snapshots of websites. In recent months, the service has faced challenges from automated scraping and some major media organizations blocking it over concerns about AI scraping, though the Internet Archive has stated such fears are unfounded. These pressures have prompted the Archive to implement protections to keep the service available.

**「Impact」** Wayback Machine users may encounter intermittent HTTP 429 errors or inconsistent access depending on their network or device, and some archived sites could become unavailable if site owners opt out.

**「Community discussion」** Commenters broadly praised the Internet Archive and urged donations. Some reported inconsistent 429 rate-limit errors between work and personal devices, and one suggested AI companies should compensate the Archive for access.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine - Wikipedia</a></li>
<li><a href="https://blog.archive.org/2026/02/18/wayback-machine-director-pushes-back/">Wayback Machine Director Pushes Back on AI Scraping Fears Driving Archive Blocks | Internet Archive Blogs</a></li>

</ul>
</details>

**Tags**: `#internet-archive`, `#wayback-machine`, `#web-scraping`, `#infrastructure`, `#open-internet`

---

<a id="item-tech-news-6"></a>
### [Datacenter Moratoriums Are Not Killing the US Buildout](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums) ⭐️ 7.0/10

SemiAnalysis argues that datacenter moratoriums are not materially slowing the US buildout, contradicting widespread concerns. The analysis cites that 20 GW of potential capacity sits inside restricted local boundaries. However, only 1,525 MW actually slips within those areas. A nationwide total of 2.3 GW, including New York, is affected, indicating a limited share of overall capacity growth.

rss · Semianalysis · Sep 15, 20:54

**「Context on Datacenter Power Constraints」** The article continues SemiAnalysis&\#x27;s recent coverage of US datacenter power constraints and permitting delays, which documented emergency pivots at Oracle Project Jupiter and Nebius New Jersey and forecast as much as 40GW+ of behind-the-meter datacenter capacity by 2028 \(tool-1-1, tool-1-2\). SemiAnalysis has also previously challenged alarming market conclusions about datacenter cancellations, arguing sample limitations rather than actual cancellations explain some figures \(tool-1-3\). In this piece it argues local moratoriums are not materially slowing the US buildout, citing 20GW inside restricted local boundaries, 1,525MW actually slipping, and 2.3GW nationwide including New York.

**「Limited disruption from moratoriums」** Despite local datacenter moratoriums, the US buildout faces limited disruption: of 20GW of capacity located within restricted boundaries, only 1,525MW actually slips, and 2.3GW is affected nationwide including New York, indicating most planned capacity proceeds.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the">What is So Hard About Behind-The-Meter Power For Datacenters? Part 1</a></li>
<li><a href="https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw">US Grid Constraints: Towards 40GW+ of Behind-The-Meter Datacenter by 2028?</a></li>
<li><a href="https://www.bitget.com/amp/news/detail/12560605468135">SemiAnalysis: Half of US Data Centers to Shut Down by 2026? This is a False Alarm “Coded by AI” | Bitget News</a></li>
<li><a href="https://www.brookings.edu/articles/data-center-moratoriums-are-not-a-substitute-for-oversight/">Data center moratoriums are not a substitute for oversight | Brookings</a></li>

</ul>
</details>

**Tags**: `#datacenters`, `#AI infrastructure`, `#energy policy`, `#capacity planning`, `#cloud computing`

---

<a id="item-tech-news-7"></a>
### [China’s 15th Five-Year Electronics Plan Targets Advanced Chips, HarmonyOS, RISC-V](https://www.secrss.com/articles/93961) ⭐️ 7.0/10

China’s Ministry of Industry and Information Technology \(MIIT\) and National Development and Reform Commission \(NDRC\) jointly issued the 15th Five-Year Plan for the electronic information manufacturing industry, laying out 17 key tasks. The plan calls for improving advanced process capability, breaking through high-end smartphone core chips and high-performance PC chips, and expanding deployment of domestic operating systems such as open-source HarmonyOS. It also sets 2030 targets of more than 30 trillion yuan in operating revenue for enterprises above designated size and 3.5% R&amp;D intensity, while promoting RISC-V, AI chips and terminals, and Beidou development.

telegram · zaihuapd · Sep 15, 03:10

**「Background」** China&\#x27;s five-year plans are national strategic blueprints for economic and industrial development; the &quot;15th Five-Year Plan&quot; covers 2026-2030 and includes a sector-specific plan for electronic information manufacturing jointly issued by the Ministry of Industry and Information Technology \(MIIT\) and the National Development and Reform Commission \(NDRC\). The plan sets goals such as advanced semiconductor process capability, high-end mobile and PC chips, and wider adoption of domestic operating systems like open-source HarmonyOS, alongside promotion of RISC-V architecture and AI chips. These directions reflect a continuing push for domestic alternatives in critical hardware and software components.

**「Impact」** Chinese semiconductor, RISC-V, and domestic OS developers now face a formal 2030 state roadmap that pairs advanced-node and high-end chip targets with openHarmony adoption and CLink interconnect standardization, making alignment with these priorities a likely condition for funding, procurement, and market access.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.sina.cn/2026-09-15/detail-inirwfqk4019305.d.html">两部门：推进第五代精简指令集（RISC-V）研发与产业化 支持RISC-V芯片在人工智能、嵌入式系统等领域应用|国家发展改革委|信息化部|工信部|财联社|鸿蒙_手机新浪网</a></li>
<li><a href="https://www.ithome.com/1/002/403.htm">工信部、国家发改委：“十五五”规划提高先进制程能力，突破高端手机核心芯片、PC 高性能芯片，加强开源鸿蒙等国产操作系统搭载 - IT之家</a></li>
<li><a href="http://3g.cnfol.com/sc_stock/gushijujiao/20260915/32370146.shtml">30万亿蓝图出炉！ AI...</a></li>
<li><a href="https://fund.eastmoney.com/a/202609153874514129.html">30万亿蓝图出炉！ AI...</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#芯片`, `#开源鸿蒙`, `#RISC-V`, `#产业政策`

---

<a id="item-tech-news-8"></a>
### [Google Allows All Engineers to Use Anthropic&\#x27;s Claude Opus 5](https://www.businessinsider.com/google-finally-lets-all-engineers-use-anthropics-claude-2026-9) ⭐️ 7.0/10

Google has opened Anthropic&\#x27;s Claude Opus 5 to all of its engineers for internal coding, but only through Google&\#x27;s internal development platform Antigravity. Previously most Google employees were prohibited from using external coding tools such as Claude Code and OpenAI&\#x27;s Codex and were told to use Google&\#x27;s Gemini instead. A Google spokesperson said Gemini remains the primary model for internal development, with Claude provided per-employee quota as a supplement. The move is seen as a response to competitive pressure in AI coding; Google is an Anthropic investor and earlier this year announced plans to invest up to $40 billion in the company.

telegram · zaihuapd · Sep 15, 05:31

**「Background」** Google has been using its own Gemini models for internal development and has restricted employee access to external AI coding tools to protect proprietary workflows. Anthropic is a rival AI lab in which Google is an investor, and Claude is Anthropic&\#x27;s family of AI models.

**「Impact」** For Google engineers, Claude Opus 5 is now available as an internal coding aid only through Antigravity with a per-person quota, while Gemini remains the required primary model.

**Tags**: `#Google`, `#Anthropic`, `#Claude`, `#AI coding tools`, `#tech industry`

---

<a id="item-tech-news-9"></a>
### [MediaTek launches Dimensity 9600 Pro 2nm chip](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 7.0/10

MediaTek launched the Dimensity 9600 Pro and Dimensity 9600M mobile processors on September 15, 2026. The Dimensity 9600 Pro is built on TSMC&\#x27;s 2nm process, making it MediaTek&\#x27;s first mobile processor on that node, while the 9600M uses a 3nm process. MediaTek said the first phones using both chips will be available soon. The 9600 Pro includes a dedicated AI processor that improves performance for handling user prompts before model generation by 51% compared with the previous generation.

telegram · zaihuapd · Sep 15, 08:57

**「Background」** TSMC&\#x27;s 2nm process is currently its most advanced manufacturing node, offering potential improvements in power efficiency and transistor density over older nodes such as 3nm. A dedicated AI processor offloads AI workloads from the CPU and GPU, which matters for on-device generative AI features that need low-latency prompt processing.

**「Impact」** For flagship Android phone makers and users, the Dimensity 9600 Pro promises 2nm-level efficiency and a 51% faster user-prompt handling step for on-device generative AI features, with first devices expected to arrive soon.

**Tags**: `#semiconductors`, `#mobile processors`, `#AI hardware`, `#TSMC`, `#MediaTek`

---

<a id="item-tech-news-10"></a>
### [Inside Project Lily: Humans Reading Real ChatGPT Chats](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 7.0/10

404 Media reports that OpenAI employs hundreds of contractors to read real ChatGPT prompts and complete conversations, score model responses, and suggest edits; these conversations may contain sensitive personal information. OpenAI says it tries to remove personal details before giving them to reviewers but acknowledges sensitive details can still be seen. Anthropic has also confirmed that it uses human review to improve its models. The report exposes data-handling and privacy practices in AI model development.

telegram · zaihuapd · Sep 15, 11:56

**「Background」** AI companies use human reviewers to rate model answers and help refine future responses. When those reviews are based on real user conversations, contractors may encounter personal or sensitive information that users did not expect to be shared.

**「Impact」** ChatGPT and Anthropic model users should be aware that their real conversations may be read by human contractors despite attempts to remove personal information, creating a risk of sensitive data exposure.

**Tags**: `#AI`, `#Privacy`, `#ChatGPT`, `#OpenAI`, `#Data Labeling`

---

<a id="item-tech-news-11"></a>
### [GPT-5.5 Deprecation Set for October 14, 2026](https://x.com/ChatGPT/status/2099954190600876533) ⭐️ 7.0/10

OpenAI will deprecate GPT-5.5 across ChatGPT, ChatGPT Work, and Codex on all plans starting October 14, 2026. The company advises users still running GPT-5.5 in Codex to migrate to GPT-5.6 Sol or GPT-6 Astra. The retirement applies to all platforms and plan tiers, meaning the model will no longer be available after that date. No migration deadline beyond the October 14 date is specified in the announcement. The change affects developers and organizations relying on GPT-5.5 for Codex workflows.

telegram · zaihuapd · Sep 16, 00:12

**「Background」** GPT-5.5 is a model in OpenAI&\#x27;s GPT series used by ChatGPT and Codex. Model deprecation means that after the stated date, OpenAI may remove access and stop serving requests for the model across affected products. The suggested successors, GPT-5.6 Sol and GPT-6 Astra, are described in the announcement as newer OpenAI models intended to replace deprecated capabilities.

**「Impact」** Organizations using GPT-5.5 in Codex must switch to GPT-5.6 Sol or GPT-6 Astra before October 14, 2026 to avoid service interruption.

**Tags**: `#OpenAI`, `#GPT-5.5`, `#model deprecation`, `#AI`, `#ChatGPT`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s August retail sales miss forecasts as investment slump deepens](https://www.cnbc.com/2026/09/15/china-august-retail-sales-industrial-output-investment-exports-.html) ⭐️ 7.0/10

China&\#x27;s August retail sales grew 0.4% from a year earlier, missing the 0.8% forecast in a Reuters poll, while urban fixed-asset investment for the first eight months shrank 7.2% from a year earlier, deepening from a 6.7% decline in the January-July period, according to National Bureau of Statistics data.

rss · CNBC Finance · Sep 15, 09:46

**「Background」** The readings follow a slowdown in the world&\#x27;s second-largest economy to 4.3% year-on-year growth in the second quarter, the weakest pace in more than three years, with Beijing so far relying on incremental measures rather than aggressive stimulus.

**「Impact」** Oxford Economics estimates third-quarter growth at 4.3%, posing downside risks to Beijing&\#x27;s annual target of 4.5% to 5%, with weak consumption and the property slump remaining the biggest drags on growth.

**Tags**: `#China economy`, `#macroeconomic data`, `#retail sales`, `#fixed-asset investment`, `#credit growth`

---