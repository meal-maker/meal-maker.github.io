---
layout: default
title: "Horizon Summary: 2026-05-21 (EN)"
date: 2026-05-21
lang: en
---

> From 21 items, 9 important content pieces were selected

---

1. [OpenAI Model Disproves 80-Year-Old Conjecture in Discrete Geometry](#item-1) ⭐️ 10.0/10
2. [SpaceX Files for IPO, Reveals $18.7B Revenue and Anthropic Deal](#item-2) ⭐️ 9.0/10
3. [GitHub Confirms 3,800 Repos Breached via Malicious VSCode Extension](#item-3) ⭐️ 8.0/10
4. [Colorado Amended SB051 to Exclude Open Source Projects](#item-4) ⭐️ 8.0/10
5. [Qwen3.7-Max: Open-Weight Agent Model Reaches SOTA](#item-5) ⭐️ 8.0/10
6. [SpiderMonkey Removes asm.js Support](#item-6) ⭐️ 8.0/10
7. [Google AI Threatens Web Traffic Ecosystem](#item-7) ⭐️ 8.0/10
8. [Qian Xuesen: The Missile Genius America Lost and China Gained](#item-8) ⭐️ 7.0/10
9. [Flipper One Specs Drop Radio Features](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Model Disproves 80-Year-Old Conjecture in Discrete Geometry](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) ⭐️ 10.0/10

OpenAI's reasoning model disproved the 80-year-old unit distance problem conjecture by finding a counterexample, marking the first AI-assisted disproof of a central conjecture in discrete geometry. This achievement demonstrates that AI can not only assist in routine calculations but also produce novel, non-trivial mathematical insights, potentially accelerating discovery in pure mathematics and shifting the role of AI from helper to co-discoverer. The disproof was achieved by constructing a counterexample that brought sophisticated ideas from algebraic number theory to bear on an elementary geometric question, and the proof was formalized in the Lean theorem prover.

hackernews · tedsanders · May 20, 19:05

**Background**: Discrete geometry studies combinatorial properties of finite or discrete sets of geometric objects like points and lines. The unit distance problem asks how many unit distances can appear among n points in the plane. This problem originated from a 1946 conjecture by Paul Erdős, which had remained open for decades.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/model-disproves-discrete-geometry-conjecture/">An OpenAI model has disproved a central conjecture in discrete geometry | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_geometry">Discrete geometry</a></li>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-model-cracks-geometry-s-toughest-nut">OpenAI Model Cracks Geometry's Toughest Nut | StartupHub.ai</a></li>

</ul>
</details>

**Discussion**: Community reaction was largely positive, with a math postdoc calling the proof exciting and novel. However, some commenters noted that disproving a conjecture via counterexample is less satisfying than proving it true, while others praised the model's cross-domain knowledge transfer and ability to break through specialization.

**Tags**: `#AI`, `#mathematics`, `#discrete geometry`, `#research breakthrough`, `#OpenAI`

---

<a id="item-2"></a>
## [SpaceX Files for IPO, Reveals $18.7B Revenue and Anthropic Deal](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm) ⭐️ 9.0/10

SpaceX has filed an S-1 registration statement with the SEC for an initial public offering, disclosing $18.7 billion in revenue for 2025, up from $14.0 billion in 2024, alongside a $1.25 billion per month cloud services agreement with AI company Anthropic for compute capacity on its Colossus data centers. This IPO filing provides unprecedented financial transparency into SpaceX, revealing that Starlink's $4.4 billion operating income is offsetting losses in its launch business, and highlighting the growing importance of AI compute deals as a new revenue stream. The filing could value SpaceX at over $1 trillion, making it one of the largest public offerings in history and a bellwether for the space and AI compute industries. SpaceX reported an operating loss of $2.6 billion and net loss of $4.9 billion in 2025, despite $6.6 billion in adjusted EBITDA, with massive capital expenditures of $20.7 billion. The Anthropic agreement is for access to compute capacity across Colossus and Colossus II data centers, ramping up in May-June 2026 at a reduced fee, and runs through May 2029.

hackernews · cachecow · May 20, 20:49

**Background**: An S-1 filing is the initial registration form required by the U.S. Securities and Exchange Commission for companies planning to go public, revealing detailed financials and business risks. SpaceX, founded by Elon Musk, has been a private company primarily known for rocket launches and the Starlink satellite internet constellation. Starlink's profitability is a key development, as it provides a stable cash flow to support SpaceX's other ventures, including the capital-intensive AI compute business.

**Discussion**: Commenters expressed skepticism about SpaceX's valuation and financials, with one calling it 'Elon trying to be the first trillionaire and make investors whole by suckering the public.' Others noted that while Starlink is a 'real cash machine,' the company's revenue of $18.7B is relatively low compared to its proposed trillion-dollar valuation, and questioned the feasibility of profitable space-based data centers.

**Tags**: `#SpaceX`, `#IPO`, `#Starlink`, `#Anthropic`, `#AI compute`

---

<a id="item-3"></a>
## [GitHub Confirms 3,800 Repos Breached via Malicious VSCode Extension](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/) ⭐️ 8.0/10

GitHub confirmed that a malicious Visual Studio Code (VSCode) extension compromised an employee's device, leading to unauthorized access and breach of 3,800 repositories. This breach underscores the severe supply chain risks posed by VSCode extensions, which have weak security models and can access a developer's entire file system, potentially compromising many downstream projects. GitHub detected and contained the compromise, removed the malicious extension version, and isolated the endpoint, but the specific extension name was not disclosed. The attack highlights how even internal tools like IDE extensions can become attack vectors.

hackernews · Timofeibu · May 20, 13:43

**Background**: VSCode extensions have no permissions model and can access all parts of the file system, making them a high-risk attack vector. Supply chain attacks through IDE plugins are a growing concern, as they can monitor coding sessions and execute arbitrary code. GitHub and VSCode are both owned by Microsoft, yet the extension ecosystem remains largely ungoverned.

<details><summary>References</summary>
<ul>
<li><a href="https://vscan.dev/">VSCan | VSCode Extension Security Analyzer</a></li>
<li><a href="https://biggo.com/news/202506250723_VSCode_Extensions_Security_Vulnerabilities">VSCode Extensions Lack Basic Security Permissions... - BigGo News</a></li>
<li><a href="https://www.linkedin.com/posts/shur-net-solutions_cybersecurity-devsecops-softwaredevelopment-activity-7429928601531154432-Gf3R">VSCode Extension Security Alert: Vulnerabilities Exposed | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Community comments expressed shock at the breach and frustration with the lack of a proper security model for VSCode extensions. Some noted that extensions often appear official but are from random developers, and questioned why the specific extension name was withheld.

**Tags**: `#security`, `#vscode`, `#github`, `#supply-chain-attack`, `#incident-response`

---

<a id="item-4"></a>
## [Colorado Amended SB051 to Exclude Open Source Projects](https://legiscan.com/CO/bill/SB051/2026) ⭐️ 8.0/10

Colorado's SB051 age verification bill was amended to explicitly exclude open source projects from the definition of 'covered application,' meaning open source software distributed through free public code repositories is not subject to the bill's age verification requirements. This amendment is a significant win for the open source community, as it prevents burdensome compliance costs and privacy intrusion for developers of free and open source software. However, it also highlights ongoing concerns about the broader trend of age verification laws expanding beyond their original scope, which could still affect proprietary applications. The bill defines 'covered application' as a consumer software application accessed through a covered application store, but explicitly excludes applications that do not process users' personal data or applications from a free, publicly available code repository. This exemption directly shields open source projects from the law's requirements.

hackernews · ki4jgt · May 20, 20:28

**Background**: Age verification bills like SB051 are part of a growing legislative trend in the U.S. aimed at restricting minors' access to age-inappropriate online content, initially targeting pornographic sites but expanding to social media and other platforms. Open source projects, which are often developed and distributed by small communities without commercial backing, would face disproportionate compliance burdens if not exempted.

**Discussion**: Community comments reflect a mix of skepticism and cautious optimism. Some users, like declan_roberts, express suspicion about the motives behind age verification laws, while others like HDBaseT warn of a 'boiling frog' scenario where exemptions gradually disappear. Mlinksva notes this development is positive and points to similar changes in California's bill, suggesting coordinated advocacy efforts.

**Tags**: `#age verification`, `#open source`, `#legislation`, `#Colorado`, `#privacy`

---

<a id="item-5"></a>
## [Qwen3.7-Max: Open-Weight Agent Model Reaches SOTA](https://qwen.ai/blog?id=qwen3.7) ⭐️ 8.0/10

Alibaba's Qwen team released Qwen3.7-Max, a new open-weight large language model that achieves state-of-the-art performance on agent tasks and non-hallucination benchmarks, surpassing proprietary models like Opus 4.7, Gemini 3.1 Pro, and GPT-5.5. This release strengthens the open-weight AI ecosystem by providing a powerful, free alternative to proprietary coding agents like Claude Code, potentially lowering costs and increasing accessibility for developers worldwide. It also demonstrates that open models can compete at the frontier of agentic AI, a rapidly growing area focused on autonomous task completion. The model achieved a SOTA non-hallucination rate on the AA-omniscience benchmark, though the announcement did not include comparisons against the latest versions of competing models, a point noted by community members. Qwen3.7-Max is an incremental improvement over prior Qwen versions, with community excitement focused on its open-weight availability and potential for production workloads via local deployment.

hackernews · kevinsimper · May 20, 10:35

**Background**: Agent tasks refer to AI systems that can autonomously plan and execute multi-step actions using external tools, often driven by large language models. Non-hallucination measures a model's ability to avoid generating fabricated or incorrect information, a critical challenge for reliable AI. Open-weight models release the trained parameters (weights) for public use, differing from fully open-source models that also include training code and data; this allows developers to run the model locally or fine-tune it without relying on proprietary APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**Discussion**: The community expressed excitement about the model's performance and open-weight availability, with one user praising it as a great free alternative to Claude Code after hitting usage limits. However, some users criticized the lack of comparisons against the latest competitor versions, and others expressed a desire for partnerships with US cloud providers to enable production use in the US.

**Tags**: `#AI`, `#Open-Source Models`, `#Qwen`, `#Agent AI`, `#LLM`

---

<a id="item-6"></a>
## [SpiderMonkey Removes asm.js Support](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html) ⭐️ 8.0/10

Mozilla's SpiderMonkey JavaScript engine has announced the removal of asm.js support, as WebAssembly has fully superseded it. This marks the end of an important era in web performance, as asm.js pioneered near-native speed for web applications and paved the way for WebAssembly. The removal simplifies the engine and encourages developers to migrate fully to WebAssembly. asm.js was a strict subset of JavaScript that allowed C/C++ code compiled via Emscripten to run efficiently in the browser. Its optimizations are no longer needed because modern WebAssembly provides better performance and smaller bundle sizes.

hackernews · eqrion · May 20, 12:01

**Background**: asm.js was introduced by Mozilla in 2013 as a response to Google's Native Client (NaCl/PNaCl), aiming to bring near-native performance to the web by restricting JavaScript to a subset that engines could aggressively optimize. It enabled early demos like Unreal Engine in Firefox and was used by Figma to prove browser-based design tools. WebAssembly, a binary format designed from the start as a compilation target, became the successor and is now supported by all major browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asm.js">Asm.js</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpiderMonkey_(Javascript_engine)">SpiderMonkey (Javascript engine)</a></li>
<li><a href="http://asmjs.org/">asm . js</a></li>

</ul>
</details>

**Discussion**: The Hacker News community expressed a mix of nostalgia and agreement, noting asm.js's pivotal role in projects like Figma and its historical significance. Many referenced Gary Bernhardt's iconic talk 'The Birth and Death of JavaScript,' which eerily predicted this transition, and shared fond memories of early demos like Unreal Engine in the browser.

**Tags**: `#asm.js`, `#webassembly`, `#spidermonkey`, `#firefox`, `#javascript`

---

<a id="item-7"></a>
## [Google AI Threatens Web Traffic Ecosystem](https://tante.cc/2026/05/20/on-google-declaring-war-on-the-web/) ⭐️ 8.0/10

An article argues that Google's shift toward AI-generated answers in search is undermining the traffic-driven relationship between websites and Google. This change breaks the long-standing symbiotic exchange where websites allowed crawling in return for user referrals. This matters because millions of content creators and small websites depend on Google for traffic and revenue; if AI summaries replace clicks, the web's content economy could collapse. The shift also threatens the diversity and quality of online information as independent publishing becomes less viable. The article specifically critiques Google's AI overviews and direct answer features that keep users on Google's own pages. Community comments highlight that even when AI summaries are wrong, websites lose traffic and ad revenue, while large corporations benefit from the aggregated content.

hackernews · cdrnsf · May 20, 21:33

**Background**: For years, Google Search acted as a gateway: it crawled and indexed websites, and in return sent users to those sites via organic links. This symbiotic relationship allowed content creators to monetize their work through traffic and advertising. With the rise of AI, Google now often generates direct answers within its search results, reducing the need for users to click through to external sites. This fundamentally changes the economic model of the open web.

**Discussion**: Commenters express a mix of frustration and resignation, with some noting that websites voluntarily gave up control of their traffic to Google and now face the consequences. Others worry that AI will devalue human creativity and discourage independent content creation, while a few suggest seeking alternative traffic sources like StumbleUpon or decentralization. A common sentiment is that the symbiotic relationship between Google and web publishers is breaking down, leaving creators with fewer options to monetize.

**Tags**: `#Google`, `#AI`, `#Web`, `#Search`, `#ContentMonetization`

---

<a id="item-8"></a>
## [Qian Xuesen: The Missile Genius America Lost and China Gained](https://www.usni.org/magazines/naval-history/2025/december/missile-genius-america-lost-and-china-gained) ⭐️ 7.0/10

A detailed historical article published in 2025 by the U.S. Naval Institute examines the life and legacy of Qian Xuesen, the rocket scientist deported from the United States who became the father of China's missile and space program. This story highlights the long-term consequences of immigration policy and national security actions during the Second Red Scare, and remains relevant to current debates about Chinese-American scientists and U.S.-China technology competition. Qian Xuesen co-founded NASA's Jet Propulsion Laboratory and held the rank of colonel in the U.S. Army before being stripped of his security clearance in 1950 and placed under house arrest for five years. He was deported in 1955 in exchange for captured U.S. pilots and then led China's development of the Dongfeng ballistic missile series and the broader space program.

hackernews · thnaks · May 20, 17:48

**Background**: Qian Xuesen was a Chinese-born aerospace engineer who studied at MIT and Caltech, making major contributions to aerodynamics and rocket science. During the McCarthy era, he was accused of communist sympathies, subjected to five years of house arrest, and ultimately deported to China. After returning, he became known as the 'Father of Chinese Rocketry' and played a central role in the Two Bombs, One Satellite project. His deportation is widely seen as a pivotal moment in which the United States inadvertently transferred critical technological expertise to China.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qian_Xuesen">Qian Xuesen - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/stories-54695598">Qian Xuesen : The man the US deported - who then helped China into...</a></li>
<li><a href="https://aerospace.caltech.edu/about/legends-of-galcit/qian-xuesen-tsien-hsue-shen">Qian Xuesen (Tsien Hsue-Shen) - Aerospace Caltech - Lynn Booth...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that a biopic of Qian would likely be boring because he excelled at building organizations, with one pointing to a podcast episode covering the Cultural Revolution and attempted coup at his institute. Others argued the US continues to repeat the mistake of persecuting Chinese-American scientists, though one commenter questioned the counterfactual that China could not have achieved its rocket program without him.

**Tags**: `#history`, `#rocketry`, `#immigration`, `#US-China relations`, `#science policy`

---

<a id="item-9"></a>
## [Flipper One Specs Drop Radio Features](https://docs.flipper.net/one/general/tech-specs) ⭐️ 6.0/10

The Flipper One tech specs were released, showing a hardware upgrade with a quad-core ARM Cortex-M4 and 512MB RAM, but omitting NFC, RFID, and sub-1GHz radio capabilities that defined the Flipper Zero. As the successor to a widely used hacking tool, this omission could limit the device's appeal to security researchers and hobbyists who relied on radio features for real-world tests. The shift toward a more general-purpose Linux device may alienate the core user base. The device includes an aluminum enclosure with Gorilla Glass, a low-resolution grayscale display connected to the microcontroller rather than the Linux SoC, and two Ethernet ports for network diagnostics.

hackernews · gregsadetsky · May 20, 18:33

**Background**: Flipper Zero is a popular multi-tool for security researchers, capable of reading, storing, and emulating radio frequencies from 300-928 MHz, as well as NFC, RFID, and infrared signals. It became known for its ability to interact with a wide range of wireless devices. The Flipper One was anticipated as an upgraded successor but the published specs reveal a different direction, focusing on a Linux-based platform with Wi-Fi, Bluetooth, and Ethernet rather than dedicated radio hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flipper_Zero">Flipper Zero - Wikipedia</a></li>
<li><a href="https://docs.flipper.net/one/general/tech-specs">Tech specs - Flipper One Documentation</a></li>
<li><a href="https://1023jack.com/news/flipper-one-tech-specs/">Flipper One Tech Specs - 1023 Jack</a></li>

</ul>
</details>

**Discussion**: Community members expressed disappointment, with one user noting the absence of NFC, RFID, and sub-1GHz radio, stating that the Flipper always needed to be a software-defined transceiver. Others questioned design choices like the low-resolution display and the display being connected to the microcontroller. Some found the Ethernet ports interesting for network diagnostics and MITM attacks.

**Tags**: `#hardware`, `#flipper`, `#embedded`, `#security`, `#hacking`

---