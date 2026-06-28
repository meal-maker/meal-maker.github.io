---
layout: default
title: "Horizon Summary: 2026-06-16 (EN)"
date: 2026-06-16
lang: en
---

> From 25 items, 13 important content pieces were selected

---

1. [Backdoor in npm script discovered in LinkedIn job interview](#item-1) ⭐️ 9.0/10
2. [Banned Book Library Hidden in a Wi-Fi Smart Bulb](#item-2) ⭐️ 8.0/10
3. [Iroh 1.0 Releases Peer-to-Peer Networking Library](#item-3) ⭐️ 8.0/10
4. [Developers Share Success Replacing Claude/GPT with Local Models](#item-4) ⭐️ 8.0/10
5. [Essay Debates a Peopleless Economy Without Human Workers](#item-5) ⭐️ 8.0/10
6. [Homelab AI Dev Platform with Forgejo and Argo Workflows](#item-6) ⭐️ 8.0/10
7. [Hetzner Announces Major Price Hikes Up to 3x](#item-7) ⭐️ 8.0/10
8. [Fox Acquires Roku in Landmark Streaming Hardware Deal](#item-8) ⭐️ 8.0/10
9. [Salesforce Acquires Fin (ex-Intercom) for $3.6B](#item-9) ⭐️ 8.0/10
10. [TimescaleDB Hypercore compression deep dive](#item-10) ⭐️ 8.0/10
11. [US battery manufacturing output continues to break records](#item-11) ⭐️ 7.0/10
12. [Copper drug restores memory, clears Alzheimer's proteins in mice](#item-12) ⭐️ 7.0/10
13. [Nostalgic Love for Computers Amid Industry Critique](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Backdoor in npm script discovered in LinkedIn job interview](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

A job applicant discovered that a recruiter for a cryptocurrency startup sent a GitHub repository containing a hidden backdoor in the npm 'prepare' script, which executes automatically when 'npm install' is run, compromising the developer's machine. This incident highlights a dangerous and increasingly common social engineering attack vector targeting developers during technical interviews, exploiting trust and routine actions. It also underscores significant gaps in reporting mechanisms and platform responses for such cybercrimes. The backdoor was hidden in a 'prepare' script within the package.json file, buried among commented-out tests. The payload runs any commands sent from a remote server, making it a full remote access trojan, and reports to GitHub and LinkedIn yielded no immediate action.

hackernews · lwhsiao · Jun 15, 20:00

**Background**: npm is the package manager for Node.js, and its 'prepare' script runs automatically after 'npm install', intended for tasks like building the package. Attackers have increasingly abused npm lifecycle scripts (such as 'preinstall', 'postinstall', and 'prepare') to execute malicious code during installation, making supply chain attacks a persistent threat in the JavaScript ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem</a></li>

</ul>
</details>

**Discussion**: Commenters expressed alarm that this attack is dangerously close to normal interview tasks, with some noting they had encountered similar attempts multiple times in recent months. Others criticized the lack of effective reporting channels and platforms' failure to remove malicious code, calling for an organized defense against such cybercrime.

**Tags**: `#cybersecurity`, `#npm`, `#backdoor`, `#supply chain attack`, `#social engineering`

---

<a id="item-2"></a>
## [Banned Book Library Hidden in a Wi-Fi Smart Bulb](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 8.0/10

A developer created a project that stores banned books on the flash storage of an ESP8266-based Wi-Fi smart light bulb, turning it into a local web server that serves the books over its Wi-Fi network without needing internet access. This project demonstrates a creative and practical method for circumventing censorship by using everyday IoT devices as hidden libraries, making censored literature accessible in restricted environments. The light bulb's firmware was replaced with a custom ESP Web Server that serves ePub files from its limited flash storage; the devices can potentially form a mesh network to share content, as discussed in the community.

hackernews · sohkamyung · Jun 15, 22:37

**Background**: Many Wi-Fi smart bulbs are built around low-cost microcontrollers like the ESP8266, which have limited flash memory and can be reflashed with custom firmware. By reflashing the bulb, the developer turned it into a local file server that hosts banned books on a hidden network, making them accessible without internet.

<details><summary>References</summary>
<ul>
<li><a href="https://mischianti.org/esp8266-firmware-and-filesystem-update-with-ftp-client-2/">esp8266 firmware and filesystem update with FTP client - 2</a></li>
<li><a href="https://github.com/cotestatnt/esp-fs-webserver">GitHub - cotestatnt/esp-fs-webserver: ESP32/ESP8266 webserver, WiFi ...</a></li>
<li><a href="https://microcontrollerslab.com/esp8266-nodemcu-web-server-using-littlefs-flash-file-system/">ESP8266 NodeMCU Web Server using LittleFS (Flash File System)</a></li>

</ul>
</details>

**Discussion**: The community praised the project's ingenuity and its relevance to censorship and free speech, referencing similar past projects like PirateBox and LibraryBox. Some comments discussed the limitations of storage and the potential for mesh networking, while others noted the political context of 'banned books' lists.

**Tags**: `#IoT`, `#censorship`, `#privacy`, `#hacking`, `#free speech`

---

<a id="item-3"></a>
## [Iroh 1.0 Releases Peer-to-Peer Networking Library](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 is a major milestone release of a modular peer-to-peer networking library that replaces IP addressing with dial keys for secure, application-layer connectivity. This library makes it significantly easier for developers to build distributed applications by handling direct connectivity, NAT traversal, and relay fallbacks automatically, without requiring users to manage accounts or network configurations. Out of the box, Iroh 1.0 supports IPv4, IPv6, and relay transports, and it provides a custom transport interface for extendability. It builds on QUIC for encrypted connections and uses hole punching complemented by relay servers.

hackernews · chadfowler · Jun 15, 15:13

**Background**: Traditional IP-based networking breaks when devices change networks or are behind NATs, making peer-to-peer connections difficult. Iroh solves this by using cryptographic 'dial keys' that identify peers independent of network location, enabling direct connections through hole punching with relay servers as fallback. It is written in Rust and exposes a QUIC stream interface for developers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/">Iroh</a></li>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys instead ...</a></li>
<li><a href="https://docs.rs/iroh/latest/iroh/">iroh - Rust - Docs.rs</a></li>

</ul>
</details>

**Discussion**: One commenter likens Iroh to 'Tailscale at the application layer,' noting it avoids requiring user accounts. A developer clarifies that custom transports like WebRTC or BLE can be added via the new transport interface. Some readers expressed confusion about the problem statement, while others praised the decentralization vision.

**Tags**: `#networking`, `#peer-to-peer`, `#Rust`, `#decentralized`, `#secure connectivity`

---

<a id="item-4"></a>
## [Developers Share Success Replacing Claude/GPT with Local Models](https://news.ycombinator.com/item?id=48542100) ⭐️ 8.0/10

An Ask HN post and its comments reveal that many developers have fully swapped cloud-based coding assistants like Claude and GPT for local models, using setups such as Qwen3.6 35B on dual RTX 3090s to achieve around 150 tokens per second for daily coding tasks. This shift demonstrates that open-source local models have matured enough to handle most coding tasks, offering significant advantages in privacy, cost reduction, and independence from cloud providers, potentially reshaping how developers approach AI-assisted programming. Models like Qwen3.6-35B-A3B use a mixture-of-experts architecture with only 3 billion active parameters per token, enabling fast inference on consumer hardware; commenters report quality comparable to frontier models from 8–12 months ago, with setups typically relying on tools like llama.cpp or pi coding harness.

hackernews · cloudking · Jun 15, 14:46

**Background**: Local large language models (LLMs) run entirely on a user's own hardware, eliminating the need to send code or data to external servers. Mixture-of-experts (MoE) models activate only a subset of parameters per token, balancing total model size with inference speed. Dual RTX 3090 setups (48 GB total VRAM) are a popular choice for running models with over 35 billion parameters locally. Qwen3.6-35B-A3B, released in April 2026, is an open-weight model specifically optimized for coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6-35b-a3b">Qwen3.6-35B-A3B: Agentic Coding Power, Now Open to All</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-35B-A3B">Qwen/Qwen3.6-35B-A3B · Hugging Face</a></li>
<li><a href="https://insiderllm.com/guides/multi-gpu-local-ai/">Best Dual-GPU Local AI Setup: RTX 3090, 5060 Ti (2026)</a></li>

</ul>
</details>

**Discussion**: The comments are overwhelmingly positive, with users sharing detailed hardware and software configurations. Most agree that local models are not as smart as frontier cloud models but are 'good enough' for the majority of daily coding tasks. A few caution about the opportunity cost of not using the latest models, but the overall sentiment is that the trade-off is worthwhile for privacy and cost reasons.

**Tags**: `#local LLMs`, `#AI coding`, `#developer tools`, `#machine learning`, `#software engineering`

---

<a id="item-5"></a>
## [Essay Debates a Peopleless Economy Without Human Workers](https://gmalandrakis.com/writings/ad-economicum.html) ⭐️ 8.0/10

An essay by gmalandrakis.com contemplates the feasibility and consequences of an economy with no human workers, generating deep discussion on wealth distribution and the purpose of labor. As automation and AI advance, the questions raised have profound implications for societal structure, inequality, and the meaning of work, making this a critical debate for the future of the economy. The essay received a high engagement score of 8.0/10 with 182 comments, indicating strong community validation of its importance, though no specific technical details or breakthroughs are provided.

hackernews · l0new0lf-G · Jun 15, 21:10

**Background**: A 'peopleless economy' is a hypothetical future where machines and AI perform all labor, eliminating the need for human workers. This raises fundamental questions about how wealth is distributed and what role humans would play in such a society. The essay explores these questions without assuming any specific technological timeline.

**Discussion**: Commenters express a range of views: some warn that automation will concentrate wealth even further in a winner-takes-all scenario, while others argue that humans can still trade among themselves without robots. A few criticize the consumer-based economy premise as flawed, and one commenter dismisses the entire discussion as full of logical fallacies and premature speculation. Overall, the sentiment is deeply divided and reflects uncertainty about the long-term economic impact of AI.

**Tags**: `#artificial intelligence`, `#economics`, `#automation`, `#future of work`, `#society`

---

<a id="item-6"></a>
## [Homelab AI Dev Platform with Forgejo and Argo Workflows](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 8.0/10

A homelab enthusiast published a detailed post about building an AI development platform that integrates Forgejo, Argo Workflows, and AI agents to automate code generation and code review processes. This matters because it demonstrates how self-hosted Git forges and Kubernetes-native workflow engines can be combined with AI agents to create a custom, automated CI/CD pipeline for development, offering an alternative to cloud-based services. The platform uses Forgejo as a Git hosting service, Argo Workflows to orchestrate workflow steps, and AI agents to generate and review code. The workflow includes tagging issues, writing pull requests, testing, and a review-revise loop with a merge mutex to prevent merge storms.

hackernews · rsgm · Jun 15, 15:09

**Background**: Forgejo is a self-hosted, lightweight Git hosting platform similar to GitHub, popular among homelab enthusiasts. Argo Workflows is a Kubernetes-native workflow engine for orchestrating parallel jobs. AI agents in this context refer to language models that can automatically generate code changes and review code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo - Wikipedia</a></li>
<li><a href="https://forgejo.org/">Forgejo – Beyond coding. We forge .</a></li>
<li><a href="https://github.com/argoproj/argo-workflows">GitHub - argoproj/ argo - workflows : Workflow Engine for Kubernetes</a></li>

</ul>
</details>

**Discussion**: Community comments show several users are building similar setups, with some using Forgejo action runners with Opencode for code generation, and others using n8n and different AI models. One user also noted that the domain rsgm.dev was filtered by Quad9 DNS, sparking a brief side discussion.

**Tags**: `#homelab`, `#AI development`, `#CI/CD`, `#Forgejo`, `#Argo Workflows`

---

<a id="item-7"></a>
## [Hetzner Announces Major Price Hikes Up to 3x](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 8.0/10

Hetzner has announced substantial price increases for its server products, with some customers facing up to 3x hikes, as documented in their official price adjustment page. This price adjustment affects many developers and businesses that rely on Hetzner for affordable hosting, potentially disrupting budgets and prompting migration to other providers, while reflecting broader hardware cost increases driven by AI demand. The price changes apply to Hetzner's Cloud servers and other products; while increases of 25-50% might be expected, some customers reported 3x jumps, which is unusually high.

hackernews · tuhtah · Jun 15, 13:19

**Background**: Hetzner is a German web hosting company known for offering high-quality dedicated servers, cloud servers, and other hosting services at competitive prices, making it popular among developers and small to medium-sized businesses. The recent price increase is attributed to rising costs of hardware components such as RAM and disk storage, exacerbated by the AI boom which has increased demand for computing resources globally.

**Discussion**: Community comments express shock and frustration at the magnitude of the increase, with users noting that 3x jumps are unprecedented and questioning the justification. Some see it as a broader industry trend where hardware scarcity drives costs up, while others lament the end of Hetzner's budget-friendly era and discuss potential alternative providers.

**Tags**: `#Hetzner`, `#Price Adjustment`, `#Cloud Hosting`, `#Hardware Costs`, `#Community Discussion`

---

<a id="item-8"></a>
## [Fox Acquires Roku in Landmark Streaming Hardware Deal](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

Fox Corporation has announced its acquisition of Roku, a major streaming hardware and platform provider, in a deal that could significantly alter the competitive landscape of the streaming industry. This acquisition combines a major content producer with a dominant streaming device platform, raising concerns about media consolidation and potential bias in content curation, affecting millions of U.S. households that use Roku. Roku has been moving toward including its own content and ads, which has frustrated users who prefer a service-agnostic experience; this acquisition by Fox intensifies those concerns as Fox now controls both the content and the hardware.

hackernews · thm · Jun 15, 12:50

**Background**: Roku is a leading streaming device platform used by tens of millions of households, known for its neutral interface that aggregates content from various services. Fox is a major media conglomerate that owns Fox News, Fox Sports, and other entertainment properties. The deal merges content creation with hardware distribution, a trend that has raised antitrust and consumer choice issues.

**Discussion**: Community reactions are overwhelmingly negative, with users expressing deep pessimism about the future of Roku's neutrality. Many commenters fear that Fox will push its own content and bias, and some have already started migrating to alternatives like the Nvidia Shield to regain control over their viewing experience.

**Tags**: `#acquisition`, `#Roku`, `#Fox`, `#streaming`, `#media consolidation`

---

<a id="item-9"></a>
## [Salesforce Acquires Fin (ex-Intercom) for $3.6B](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce announced on June 15, 2026, a definitive agreement to acquire Fin, formerly known as Intercom, for $3.6 billion to bolster its Agentforce AI customer support platform. This acquisition positions Salesforce to directly compete with Sierra, the AI customer service startup founded by its former co-CEO Bret Taylor, and prevents independent AI agents from becoming a control point outside the CRM ecosystem. Fin was rebranded from Intercom only a month before the deal, and the acquisition is expected to close in Salesforce's fourth fiscal quarter. The $3.6 billion price tag reflects the high valuation in the AI customer support agent space, where competitors like Sierra are valued at $15.8 billion and Decagon at $4.5 billion.

hackernews · colesantiago · Jun 15, 12:08

**Background**: Salesforce is the largest customer relationship management (CRM) platform, and its Agentforce AI aims to automate customer service tasks. Fin (formerly Intercom) is a leading AI customer service bot that handles the entire customer journey. The acquisition is part of a broader industry trend where CRM vendors acquire AI startups to integrate intelligent agents into their platforms, as customers increasingly expect AI-powered customer support.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/ai-and-ml/2026/06/15/salesforce-reels-in-customer-support-ai-specialist-fin-for-36b/5255571">Salesforce reels in customer support AI specialist Fin for $3.6B</a></li>
<li><a href="https://fin.ai/">Fin. The highest performing Customer Agent</a></li>
<li><a href="https://sierra.ai/blog/agents-as-a-service">Agents as a service | Sierra</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some noted that AI customer service, when executed well, can surpass human support, as seen with a Starlink experience, while others questioned the long-term viability of helpdesk companies like Intercom once businesses can train their own agents. The timing of the sale right after the rebrand and the competition with Sierra were also highlighted.

**Tags**: `#Salesforce`, `#acquisition`, `#AI customer service`, `#CRM`, `#Fin`

---

<a id="item-10"></a>
## [TimescaleDB Hypercore compression deep dive](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

The article provides a detailed technical explanation of how TimescaleDB's Hypercore compression achieves high compression ratios for time-series data in PostgreSQL. This matters because time-series data grows rapidly, and efficient compression reduces storage costs and can speed up queries, making PostgreSQL more competitive for IoT, monitoring, and analytics workloads. Hypercore uses columnar storage and type-aware techniques such as delta encoding, delta-of-delta, simple-8b, run-length encoding, XOR-based compression, and dictionary compression, claiming up to 98% compression ratio.

hackernews · lkanwoqwp · Jun 15, 17:29

**Background**: TimescaleDB is an extension for PostgreSQL that specializes in time-series data. Time-series data often has repeating patterns and values, making it highly compressible. Columnar storage groups data by column instead of row, which improves compression and scan performance for analytical queries. Hypercore is TimescaleDB's latest compression engine that combines these techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.tigerdata.com/use-timescale/latest/hypercore/compression-methods/">Tiger Data Documentation | About compression methods</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/compression/">Timescale Documentation | Compression</a></li>
<li><a href="https://tiger-data-docs.vercel.app/docs/learn/columnar-storage/understand-hypercore">Understand hypercore | Tiger Data Docs</a></li>

</ul>
</details>

**Discussion**: The community discussion is highly technical, with users debating compression trade-offs like I/O vs CPU usage (gopalv), sharing alternative approaches such as the deltax extension (tudorg), and asking about lossy compression for IoT (heliosAtWork). Some skepticism is expressed about the "up to 98%" claim (robocat), while blackoil notes that Facebook's Gorilla used similar delta techniques.

**Tags**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-11"></a>
## [US battery manufacturing output continues to break records](https://fred.stlouisfed.org/series/IPG33591S) ⭐️ 7.0/10

The Federal Reserve's industrial production index for battery manufacturing (FRED series IPG33591S) has reached new all-time highs, indicating continued growth in US battery output. This record shows the US is scaling up domestic battery production, which is critical for electric vehicles and energy storage. However, community comments reveal that US capacity (70 GWh) still lags far behind China (1,755 GWh), underscoring the need for accelerated investment. The FRED series IPG33591S measures output of all batteries classified as durable goods, including primary batteries. One commenter suggests the growth may partly reflect primary battery production (e.g., AA cells) rather than just advanced battery cells for EVs.

hackernews · epistasis · Jun 15, 20:28

**Background**: Battery manufacturing output is a key indicator of industrial capacity for energy storage and electric vehicles. The US has been investing in domestic battery production through policies like the Inflation Reduction Act, but China currently dominates global production with massive scale, while Europe also holds a significant lead over the US.

**Discussion**: Community comments express optimism about US growth but highlight the enormous gap with China, with one user providing specific 2025 capacity figures: US 70 GWh, China 1,755 GWh, Europe 252 GWh. Another commenter questions whether the growth is proportional to EV adoption, while others note that the data may include primary batteries.

**Tags**: `#batteries`, `#manufacturing`, `#energy storage`, `#US industry`, `#China`

---

<a id="item-12"></a>
## [Copper drug restores memory, clears Alzheimer's proteins in mice](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins) ⭐️ 7.0/10

Monash University researchers reported that the copper-delivering drug Cu(ATSM) reduced amyloid-beta accumulation by 42% and improved spatial memory by 44% in Alzheimer's mouse models, with the compound already having undergone safety evaluations for other diseases. This study offers a novel approach targeting copper dysregulation in Alzheimer's, a different mechanism from previous amyloid-directed therapies that have largely failed in clinical trials. If results translate to humans, it could open a new treatment pathway, though the amyloid hypothesis remains controversial. The drug restored blood-brain barrier clearance mechanisms, reducing amyloid-beta plaques by 42% and improving spatial learning by 44% in mouse models. Cu(ATSM) has already been evaluated for safety in other conditions, which could accelerate its path to human Alzheimer's trials.

hackernews · bookofjoe · Jun 15, 14:48

**Background**: Alzheimer's disease is a neurodegenerative disorder characterized by progressive memory loss and accumulation of amyloid-beta plaques in the brain. Copper dysregulation has been implicated in the disease, as excess copper can promote amyloid-beta aggregation and oxidative stress. The current study explores a drug that delivers copper to restore proper metal homeostasis, aiming to enhance the brain's natural clearance of toxic proteins.

<details><summary>References</summary>
<ul>
<li><a href="https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins">Copper drug restores memory and clears toxic Alzheimer's proteins</a></li>
<li><a href="https://medicalxpress.com/news/2026-06-copper-drug-memory-toxic-alzheimer.html">Copper drug restores memory and clears toxic Alzheimer's proteins ...</a></li>
<li><a href="https://www.drugtargetreview.com/copper-drug-cuatsm-reduces-alzheimers-proteins-by-42-percent-in-preclinical-study/2135715.article">Copper drug Cu (ATSM) reduces Alzheimer's proteins by 42 percent in ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is cautiously optimistic, with many commenters noting the long history of failed amyloid-targeting therapies and urging skepticism of mouse studies. Some argue that amyloid plaques may be a consequence rather than cause of Alzheimer's, while others acknowledge the novelty of the copper-based mechanism and the potential for faster clinical trials due to prior safety data.

**Tags**: `#Alzheimer's research`, `#amyloid-beta`, `#copper transport`, `#drug repurposing`, `#neuroscience`

---

<a id="item-13"></a>
## [Nostalgic Love for Computers Amid Industry Critique](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 6.0/10

Michael Enger published a personal essay reflecting on his deep love for computers as intrinsically tinkerable machines, while criticizing the modern tech industry and gatekeeping attitudes toward programming and AI tools. The essay resonated widely on Hacker News, sparking debate about the tension between loving the computer itself and disliking the surrounding industry, and about whether criticizing AI as 'snake oil' is exclusionary. The author contrasts the joy of low-level tinkering with the frustrations of modern software development, and the Hacker News discussion adds perspectives on AI as a useful tool and the gatekeeping nature of some nostalgic sentiments.

hackernews · speckx · Jun 15, 20:14

**Background**: The essay reflects a common sentiment among veteran programmers: a fondness for the early days of personal computing when machines were simpler and more open to exploration. The term 'gatekeeping' refers to attitudes that exclude newcomers or devalue their use of modern tools like AI.

**Discussion**: Comments show a split: some agree with the love for the computer but not the industry, while others defend AI as a legitimate tool. A notable critique (tptacek) argues the author's sentiment is gatekeepy, implying that their effortful learning gives them authority over how others should use computers.

**Tags**: `#computing culture`, `#gatekeeping`, `#AI tools`, `#programming nostalgia`, `#hacker ethos`

---