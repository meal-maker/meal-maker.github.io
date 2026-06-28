---
layout: default
title: "Horizon Summary: 2026-05-30 (EN)"
date: 2026-05-30
lang: en
---

> From 27 items, 13 important content pieces were selected

---

1. [Mistral AI Summit Reveals On-Prem Pivot, Community Debates Lag](#item-1) ⭐️ 8.0/10
2. [Framework 12: Hard to Justify Despite Repairability](#item-2) ⭐️ 8.0/10
3. [A critique of AI slop: say what you mean directly](#item-3) ⭐️ 8.0/10
4. [Optimizing Browser Rendering of Code Diffs](#item-4) ⭐️ 8.0/10
5. [UC Faculty Demand Return of SAT for STEM Admissions](#item-5) ⭐️ 8.0/10
6. [Is AI Repeating Frontend’s Lost Decade?](#item-6) ⭐️ 8.0/10
7. [California Assembly Passes 'Protect Our Games Act'](#item-7) ⭐️ 8.0/10
8. [SQLite Enough for Durable Workflows, Debate Ensues](#item-8) ⭐️ 7.0/10
9. [The Dead Economy Theory: Stagnation and Overcapacity](#item-9) ⭐️ 7.0/10
10. [Bijou64: A compact variable-length integer encoding](#item-10) ⭐️ 7.0/10
11. [Liquid AI Unveils 8B-A1B MoE Trained on 38T Tokens](#item-11) ⭐️ 7.0/10
12. [Hy3 LLM Tops OpenRouter Rankings, Sparking Debate](#item-12) ⭐️ 7.0/10
13. [Token Costs Become Unsustainable for AI Development](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Mistral AI Summit Reveals On-Prem Pivot, Community Debates Lag](https://koenvangilst.nl/lab/mistral-ai-now-summit) ⭐️ 8.0/10

At the Mistral AI Now Summit, the company announced a strategic pivot toward on-premises and European-hosted AI models, emphasizing data sovereignty for regulated industries. This shift was highlighted by customer case studies like BNP Paribas using Mistral on-prem for KYC in Belgium. This pivot positions Mistral as a key player for European enterprises needing GDPR-compliant AI, but community comments indicate Mistral has fallen behind Chinese labs like DeepSeek and MiniMax in reasoning and small model performance. The debate reflects broader concerns about Europe's competitiveness in AI development. Mistral's 'small' model has 120 billion parameters, roughly 4 times larger than competitors like Gemma4 and Qwen3.6, and reportedly struggles with medium-context reasoning. Despite this, European banks like BNP Paribas (KYC) and Abanca (agent orchestration for 2 million customers) are already adopting Mistral on-prem for sensitive data handling.

hackernews · vnglst · May 29, 16:22

**Background**: On-premise AI refers to deploying AI infrastructure and models within an organization's own secure data environment, rather than relying on external cloud providers. Small language models (SLMs) are AI models with fewer parameters designed for specific tasks, offering efficiency and privacy advantages. European data residency requirements, reinforced by regulations like the EU AI Act, make on-prem and European-hosted AI solutions attractive for regulated industries that must keep data within local borders.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ai21.com/knowledge/on-premise-ai/">On-Premise AI: Definition, Benefits & Challenges | AI21</a></li>
<li><a href="https://en.wikipedia.org/wiki/Small_language_model">Small language model - Wikipedia</a></li>
<li><a href="https://lyceum.technology/magazine/eu-data-residency-ai-infrastructure/">EU Data Residency for AI Infrastructure: 2026 Guide | Lyceum Technology</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some commenters praise Mistral's on-prem strategy as smart for regulated European industries, while others argue Mistral has accumulated significant technological delay, particularly in reasoning models. Critics point to Chinese labs like DeepSeek and MiniMax producing smaller, more capable models, and some even question Mistral's relevance today. A minor thread jokingly confuses 'Mistral' with 'mistrial' or criticizes AI company naming.

**Tags**: `#Mistral AI`, `#AI summit`, `#European AI`, `#on-prem AI`, `#small models`

---

<a id="item-2"></a>
## [Framework 12: Hard to Justify Despite Repairability](https://www.jeffgeerling.com/blog/2026/its-hard-to-justify-framework-12/) ⭐️ 8.0/10

Jeff Geerling argues that Framework's 12.2-inch convertible laptop, while aligning with Linux and open-source values through its modular and repairable design, is difficult to justify due to performance and battery-life trade-offs compared to Apple Silicon laptops. His analysis highlights the tension between hardware values and raw specs. This analysis underscores a fundamental choice in the laptop market between investing in repairable, open hardware and accepting the locked-in but high-performance Apple ecosystem. It affects consumers who prioritize long-term ownership, environmental sustainability, and software freedom over peak benchmarks. The Framework Laptop 12 features a 12.2-inch display, 360-degree hinge, stylus support, and is available with 13th Gen Intel Core i3-1315U or i5-1334U CPUs; preorders opened on April 9, 2025. Jeff Geerling's accompanying video further details the trade-offs, noting that while Apple Silicon offers superior performance and battery life, the Framework 12 excels in repairability and Linux support.

hackernews · watermelon0 · May 29, 14:55

**Background**: Framework is a company that builds modular, repairable laptops designed to be easily customized and upgraded by users, contrasting with the sealed, soldered designs of most competitors including Apple. Apple Silicon (M-series) chips deliver exceptional performance and battery efficiency but lock users into macOS and Apple's ecosystem. The debate between these approaches reflects broader tensions around right-to-repair, open-source software, and consumer choice.

<details><summary>References</summary>
<ul>
<li><a href="https://frame.work/laptop12">Framework | Order your Framework Laptop 12 now</a></li>
<li><a href="https://framewiki.net/products/framework-laptop-12">Framework Laptop 12 | Framewiki</a></li>
<li><a href="https://www.engadget.com/framework-laptop-modular-repairable-swappable-right-to-repair-150022495.html">Startup designs a modular , repairable laptop</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that the Framework 12's value proposition lies in its alignment with personal values—such as repairability, Linux support, and freedom from Apple's restrictions—even if it means accepting lower performance and battery life. Some users share personal experiences of choosing Framework for tinkerability, while others criticize Apple's increasing lock-down and Rosetta 2 retirement, reinforcing the sentiment that for many, the trade-off is worth it.

**Tags**: `#hardware`, `#framework`, `#laptop`, `#open-source`, `#repairability`

---

<a id="item-3"></a>
## [A critique of AI slop: say what you mean directly](https://noperator.dev/posts/you-can-just-say-it/) ⭐️ 8.0/10

A blog post by noperator defines AI slop as output that is large in volume but lacks fundamental motivation and understanding, and argues that direct, motivated communication is preferable to AI-generated fluff. This distinction provides a clear mental model to critique AI misuse without blaming AI itself, and encourages more authentic communication in an era of increasing AI-generated content. The author includes a friend's quote: 'If you’re going to use an LLM to write me an email, I’d much rather you just send me the prompt; at least then I’d have an idea of what you actually meant to say,' illustrating the value of the raw prompt over polished AI output.

hackernews · antirez · May 29, 15:54

**Background**: AI slop refers to low-quality digital content created with generative AI, often produced in large quantities and perceived as lacking effort or deeper meaning. This post refines that definition by emphasizing the absence of genuine motivation and understanding as the core problem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>
<li><a href="https://medium.com/never-stop-writing/ai-slop-defined-useless-ai-generated-content-1a62b3a4ec09">AI Slop Defined : Useless AI Generated Content | by Pankaj... | Medium</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion includes wide agreement with the post's definition, with user antirez calling it the best definition of AI slop he has read. Other users share personal strategies for concise communication, such as using 'in brief' headers, and reflect on how AI might force a rethinking of human value beyond work output.

**Tags**: `#AI slop`, `#communication`, `#LLM misuse`, `#authenticity`, `#technology criticism`

---

<a id="item-4"></a>
## [Optimizing Browser Rendering of Code Diffs](https://pierre.computer/writing/on-rendering-diffs) ⭐️ 8.0/10

The article 'On Rendering Diffs' by Pierre presents a deep dive into performance optimizations for rendering code diffs in the browser, introducing techniques such as inverse sticky scrolling and incremental updates. This matters because code diff rendering is a critical yet often slow component of code review tools like GitHub, and the optimizations described can significantly improve the user experience for developers working with large diffs. The inverse sticky scrolling technique uses CSS position: sticky to keep the old code visible while scrolling new code, but as noted in comments, rapid scrolling can still cause visual disruptions. The article also explores incremental rendering to avoid reprocessing unchanged parts.

hackernews · amadeus · May 29, 19:04

**Background**: Code diffs highlight changes between file versions, but rendering large diffs in a browser is challenging due to DOM size and layout costs. Traditional approaches re-render the entire diff on scroll, while inverse sticky scrolling attaches the old code to the viewport, reducing reflow. CSS position: sticky is commonly used for headers, but applying it to diff lines requires careful handling of overflow and scroll sync.

<details><summary>References</summary>
<ul>
<li><a href="https://mastery.games/post/position-sticky/">position: sticky is Amazing</a></li>
<li><a href="https://css-tricks.com/dealing-with-overflow-and-position-sticky/">Dealing With Overflow And Position: Sticky ; | CSS-Tricks</a></li>

</ul>
</details>

**Discussion**: The community discussion (141 points, 40 comments) included mixed reactions: some users questioned the effectiveness of inverse sticky scrolling during fast scrolling, while others praised the article's clarity and suggested similar optimizations for platforms like GitHub. One developer shared plans to adapt the techniques for CAD model diffs.

**Tags**: `#rendering`, `#diffs`, `#performance optimization`, `#web development`

---

<a id="item-5"></a>
## [UC Faculty Demand Return of SAT for STEM Admissions](https://www.latimes.com/california/story/2026-05-27/uc-math-professors-demand-return-of-sat-for-stem-admissions) ⭐️ 8.0/10

A group of University of California faculty have formally demanded the reinstatement of SAT testing for STEM admissions, citing severe math preparation gaps among incoming students that force instructors to reteach middle-school mathematics in college courses. This debate could reshape admission policies at one of the largest public university systems in the U.S., potentially affecting the STEM pipeline and the broader conversation around standardized testing and educational equity. The faculty warned that current preparation gaps are so severe that instructors must simultaneously reteach middle-school math while covering required college-level material for quantitatively demanding fields like engineering and economics.

hackernews · brandonb · May 28, 14:13

**Background**: The University of California system eliminated SAT/ACT requirements in 2020, shifting to a test-blind admission policy. Many educators and researchers have debated whether standardized tests are fair or effective predictors of college success. This new call from faculty suggests that the test-free approach may have unintended consequences on student readiness in STEM fields.

**Discussion**: Commenters shared diverse perspectives: one compared the Italian system with hard exams and free retakes, suggesting that high standards without testing could work; another noted that digital devices in math classes cause distraction, advocating for traditional methods. A teacher argued that prerequisites should be enforced and that reteaching middle-school math is not the instructor's responsibility.

**Tags**: `#education`, `#SAT`, `#STEM`, `#mathematics`, `#university admissions`

---

<a id="item-6"></a>
## [Is AI Repeating Frontend’s Lost Decade?](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/) ⭐️ 8.0/10

The article argues that AI tools, by lowering the barrier to frontend development, risk eroding deep expertise and quality, mirroring the pattern of the 'lost decade' caused by JavaScript frameworks that deskilled the field. This debate is significant because it questions whether productivity gains from AI come at the cost of long-term software quality and accessibility, affecting developers, users, and the web ecosystem. The article references Alex Russell's concept of 'Frontend's Lost Decade' to draw parallels, and notes that while AI enables more people to build, it may also introduce accidental complexity and lower-quality outcomes.

hackernews · xyzal · May 29, 11:09

**Background**: The term 'Frontend's Lost Decade' was coined by Alex Russell to describe how the rise of heavy JavaScript frameworks from around 2010 to 2020 led to poor performance and accessibility, as deep frontend expertise was replaced by framework knowledge. This article suggests AI tools could cause a similar deskilling effect by abstracting away core frontend understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/">Is AI causing a repeat of Frontend’s Lost Decade? | Mastro Blog</a></li>
<li><a href="https://kpwags.com/posts/2026/is-ai-causing-a-repeat-of-frontends-lost-decade/">Extended Note: Is AI causing a repeat of Frontend’s Lost Decade? - Keith Wagner</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that much of the lost 'deep expertise' was actually accidental complexity, and that enabling more people to build is a positive tradeoff. Some argue that lower-quality work existed before AI, and that AI may actually raise the baseline quality for simple tasks. There is debate over whether quality has truly declined or merely changed.

**Tags**: `#AI`, `#frontend development`, `#web standards`, `#software quality`, `#community discussion`

---

<a id="item-7"></a>
## [California Assembly Passes 'Protect Our Games Act'](https://www.invenglobal.com/articles/22330/stop-killing-games-movement-gains-momentum-california-assembly-passes-game-protection-bill) ⭐️ 8.0/10

The California State Assembly has passed the 'Protect Our Games Act', legislation requiring game publishers to maintain functionality of digitally sold games after service termination, though it exempts subscription services and free-to-play games. This bill sets a significant precedent for digital consumer rights in the gaming industry, potentially forcing publishers to consider long-term game preservation and preventing the complete loss of purchased products. The bill applies only to digitally sold games, not subscriptions or free-to-play titles; it also prohibits continued sale of games that have become unusable due to service termination.

hackernews · TechTechTech · May 29, 19:55

**Background**: The 'Stop Killing Games' movement has been pushing for legislation to prevent publishers from rendering paid games unplayable by shutting down servers. This bill represents a direct response to consumer concerns about game preservation and digital ownership.

**Discussion**: Community comments express mixed reactions: some support the regulation as a consumer protection win, while others worry about potential loopholes like shell companies being used to circumvent the law. Questions about jurisdictional reach and impact on live-service games like GTA 6 are also raised.

**Tags**: `#game preservation`, `#legislation`, `#digital rights`, `#consumer protection`, `#software regulation`

---

<a id="item-8"></a>
## [SQLite Enough for Durable Workflows, Debate Ensues](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/) ⭐️ 7.0/10

A blog post argues that SQLite alone is sufficient for building durable workflows, challenging the need for dedicated database servers. The article sparked a lively community debate on Hacker News, with 354 points and 201 comments. This discussion highlights a growing trend of simplifying infrastructure by using embedded databases like SQLite for production workloads, potentially reducing costs and complexity. It also exposes deep disagreements about concurrency and reliability, which are critical for software engineering decisions. The article's claim is that for many workflow patterns, SQLite—a single-file, serverless database—provides enough durability and transactional guarantees without requiring a separate database server. However, critics point out that SQLite's write locking and lack of network access make it unsuitable for distributed, multi-process applications.

hackernews · tomasol · May 29, 17:54

**Background**: Durable workflows are long-lived, reliable functions that survive crashes and network failures without losing state. Traditional implementations often rely on dedicated database servers like Postgres or specialized workflow engines like Temporal. SQLite is an embedded SQL database engine that stores data in a single file, making it lightweight and simple but with limited concurrency support.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.hatchet.run/v1/durable-workflows-overview">Durable Workflows - Hatchet Documentation</a></li>
<li><a href="https://lucumr.pocoo.org/2025/11/3/absurd-workflows/">Absurd Workflows : Durable Execution With Just Postgres</a></li>

</ul>
</details>

**Discussion**: Community reactions were polarized: some users shared success stories of replacing multiple SaaS tools with Go and SQLite on a single server, while others strongly disagreed, calling SQLite 'unsuitable for managing concurrency' and advocating for dedicated database servers. Alternatives like Temporal and DuckDB were also mentioned as better fits for certain use cases.

**Tags**: `#SQLite`, `#workflows`, `#databases`, `#concurrency`, `#software engineering`

---

<a id="item-9"></a>
## [The Dead Economy Theory: Stagnation and Overcapacity](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 7.0/10

An essay titled 'The dead economy theory' has sparked extensive community debate around systemic economic stagnation and overcapacity, particularly in tech labor markets and the implications of AI. This discussion is significant because it connects economic theories to real-world tech industry trends, such as over-hiring in software engineering and the potential for AI to exacerbate labor market imbalances. The essay and comments explore the idea that companies firing workers to save money may destroy their own customer base when those workers are also consumers, leading to a self-defeating cycle.

hackernews · WillDaSilva · May 29, 15:46

**Background**: The 'dead economy theory' refers to a hypothesis that advanced economies are experiencing structural stagnation characterized by persistent overcapacity, low demand, and a declining marginal utility of labor. In the tech sector, this manifests as an oversupply of software engineers and a reliance on AI to replace human workers, which critics argue undermines aggregate demand.

**Discussion**: Community comments draw parallels to historical inefficiencies like India's overstaffed agriculture and question whether tech companies like Facebook had an overcapacity of developers on projects like Messenger. Some commenters suggest that AI may be adding to an already oversupplied talent market, while others discuss the deskilling of frontend development over time.

**Tags**: `#economics`, `#tech labor`, `#AI`, `#overcapacity`, `#software engineering`

---

<a id="item-10"></a>
## [Bijou64: A compact variable-length integer encoding](https://www.inkandswitch.com/tangents/bijou64/) ⭐️ 7.0/10

Bijou64 is a novel variable-length integer encoding that ensures each integer has a unique representation, developed for the Subduction CRDT protocol and outperforming common encodings like LEB128. By eliminating ambiguous encodings, Bijou64 enhances security and parsing speed, potentially benefiting serialization formats, database index encoding, and network protocols that rely on compact integer storage. Bijou64 uses a length-prefixed design where the first byte encodes both the total byte length and the initial data bits, supporting the entire uint64 range in up to 9 bytes (compared to LEB128's potential 10th byte).

hackernews · justinweiss · May 29, 15:03

**Background**: Variable-length integer (varint) encodings represent integers using a variable number of bytes to save space. Common examples include LEB128, used in DWARF debug info and WebAssembly, which uses continuation bits to indicate whether more bytes follow. However, LEB128 permits non-canonical representations (e.g., a small number could be encoded with extra leading zeros), which can be a security and performance concern. Bijou64 was designed to avoid such ambiguities by ensuring each integer has exactly one valid encoding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inkandswitch.com/tangents/bijou64/">bijou64</a></li>
<li><a href="https://en.wikipedia.org/wiki/LEB128">LEB128 - Wikipedia</a></li>
<li><a href="https://bestcadpapers.com/tips-hacks-miscellaneous/bijou64-a-variable-length-integer-encoding/">Bijou64: A variable-length integer encoding - Best CAD papers</a></li>

</ul>
</details>

**Discussion**: Community members highlighted several trade-offs: one commenter noted that Bijou64's layout breaks SIMD acceleration, while others discussed the usefulness of non-canonical encodings like LEB128 in linking (DWARF, WASM). Another comparison to BER-TLV was raised, and a user praised Bijou64's cleaner design for most use cases but acknowledged its larger encoding size for mid-range values compared to LEB128.

**Tags**: `#variable-length encoding`, `#serialization`, `#data compression`, `#integer encoding`, `#performance`

---

<a id="item-11"></a>
## [Liquid AI Unveils 8B-A1B MoE Trained on 38T Tokens](https://www.liquid.ai/blog/lfm2-5-8b-a1b) ⭐️ 7.0/10

Liquid AI has released an 8 billion total parameter mixture-of-experts model with 1 billion active parameters per forward pass, trained on 38 trillion tokens. This release is significant because it demonstrates a large-scale training effort for an efficient MoE architecture, potentially offering high performance with lower inference cost. However, early community feedback suggests mixed results on practical tasks, indicating the model may not yet match expectations despite its large training budget. The model is a Liquid Foundation Model (LFM) 2.5 series with 8B total parameters and 1B active parameters (8B-A1B), making it a sparse MoE model. Some community members expressed concerns about overtraining, as 38 trillion tokens for an 8B model is considered unusually large.

hackernews · simjnd · May 29, 16:19

**Background**: A Mixture-of-Experts (MoE) architecture is a type of neural network that activates only a subset of its parameters (called 'experts') for each input, enabling larger total model sizes while keeping inference efficient. Liquid AI is an AI company founded in December 2023 that focuses on liquid neural networks and foundation models. The model discussed is part of their LFM (Liquid Foundation Model) series.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Liquid_AI">Liquid AI</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: one user reported poor performance on a bug-fixing benchmark compared to a smaller older model, while another joked about the model's lack of common sense. Others expressed excitement about potential applications for vision-language-action models, but concerns about overtraining on 38T tokens were also raised.

**Tags**: `#LLM`, `#Mixture-of-Experts`, `#Liquid AI`, `#AI research`, `#model release`

---

<a id="item-12"></a>
## [Hy3 LLM Tops OpenRouter Rankings, Sparking Debate](https://minimaxir.com/2026/05/openrouter-hy3/) ⭐️ 7.0/10

A mysterious LLM called Hy3, now identified as Tencent's Hunyuan 3 (Hy3 Preview), has surged to the top of OpenRouter's model rankings by a large margin, surprising the AI community. This event underscores how new open-source models can rapidly challenge established leaders like Claude, while also exposing flaws in OpenRouter's token-based ranking system that may not reflect genuine user adoption. Hy3 Preview is a 295B-parameter Mixture-of-Experts model with 21B active parameters and 256K context, built by Tencent in 90 days and claiming to outperform DeepSeek-V3 on math, code, and multilingual benchmarks. However, independent benchmarks by user zone411 show mixed results, with the model ranking between 10th and 60th out of up to 81 models on different tests.

hackernews · freediver · May 29, 00:09

**Background**: OpenRouter is a unified API marketplace providing access to hundreds of AI language models from over 50 providers, and its model rankings are based on total token usage. The Hy3 model is actually Tencent's Hunyuan 3 (Hy3 Preview), an open-source Mixture-of-Experts LLM. Community discussion reveals that token-based rankings can be skewed by a single heavy user pushing billions of tokens a day, making it difficult to distinguish genuine popularity from temporary anomalies.

<details><summary>References</summary>
<ul>
<li><a href="https://hy3ai.com/">Hy3 Preview — Tencent Hunyuan 3 Open-Source Model</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3-preview">Tencent-Hunyuan/Hy3-preview - GitHub</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Discussion**: The community responded with a mix of curiosity and skepticism. Simon Willison praised Hy3 for its creative output, sharing a demo where it produced HTML with a 'Change Pelican Color' button. Zone411 posted mixed benchmark results, while Aurornis and simonw criticized OpenRouter's ranking methodology, noting that token totals don't indicate unique users. Sheepscreek also clarified that a supposed DeepSeek coding platform is actually an independent project not affiliated with DeepSeek.

**Tags**: `#LLM`, `#OpenRouter`, `#AI rankings`, `#machine learning`, `#community discussion`

---

<a id="item-13"></a>
## [Token Costs Become Unsustainable for AI Development](http://www.ruanyifeng.com/blog/2026/05/weekly-issue-398.html) ⭐️ 6.0/10

OpenAI employee Peter Steinberger revealed his monthly AI token usage of 603 billion tokens, which would cost $1.3 million under standard pricing. Companies like Uber and Microsoft have already slashed AI spending after burning through budgets on token fees. These figures highlight that AI programming costs can vastly exceed human salaries, potentially forcing companies to restrict AI usage rather than replacing developers. The economics of token pricing will shape how widely AI coding tools are adopted in production. Steinberger is an OpenAI employee with free token access, so the $1.3 million is not real spending, but it reflects genuine usage volumes. Switching to cheaper open-source models could reduce annual costs per developer to 2–3 million RMB, while top-tier models can exceed 100 million RMB per year.

rss · 阮一峰的个人网站 · May 29, 00:08

**Background**: AI language models charge based on tokens, where a token is roughly a word or subword piece of text. Each API call consumes tokens for both input and output, and high‑frequency usage can quickly lead to millions of dollars in bills. Token‑based pricing is the standard for services like OpenAI, Anthropic Claude, and Google Gemini.

<details><summary>References</summary>
<ul>
<li><a href="https://fieldguidetoai.com/guides/token-economics">Token Economics: Understanding AI Costs - Field Guide to AI</a></li>
<li><a href="https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/">Tokens Explained: The Currency of Generative AI</a></li>
<li><a href="https://github.com/steipete/codexbar">GitHub - steipete/CodexBar: Show usage stats for OpenAI Codex and Claude Code, without having to login. · GitHub</a></li>

</ul>
</details>

**Tags**: `#Token costs`, `#LLM`, `#AI economics`, `#development tools`

---