---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 29 items, 14 important content pieces were selected

---

**Technology News**
1. [OpenSec Discloses Critical Pre-Auth Linux NFS Root Vulnerability CVE-2026-99362](#item-tech-news-1) ⭐️ 9.0/10
2. [DJB Catalogs False Proofs Accepted by Proof Checkers](#item-tech-news-2) ⭐️ 8.0/10
3. [AWS Trainium3 Inference and Microarchitecture Deep Dive](#item-tech-news-3) ⭐️ 8.0/10
4. [Google&\#x27;s DeepCrossAttention achieves comparable model quality up to 3x faster](#item-tech-news-4) ⭐️ 7.0/10
5. [Credit Card Skimming Scripts Using WebRTC Found on Shopping Sites](#item-tech-news-5) ⭐️ 7.0/10
6. [Convex skills upload user app ideas to remote server without disclosure](#item-tech-news-6) ⭐️ 7.0/10
7. [States Sue SpaceX Over Grok Child Sex and Revenge Porn Images](#item-tech-news-7) ⭐️ 7.0/10
8. [Michael Nielsen Removes Neural Networks and Deep Learning Book](#item-tech-news-8) ⭐️ 7.0/10
9. [US Intelligence Agencies Hit by AI-Assisted Hack Using Artex](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic System Cards Reveal Covert Degradation of Frontier Model Requests](#item-tech-news-10) ⭐️ 7.0/10
11. [Minecraft Bedrock Resource Pack Vulnerability Fixed in 26.65](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s State Council vows to strengthen national team market stabilization and optimize Huijin quasi stabilization fund](#item-finance-news-1) ⭐️ 9.0/10
2. [Mixue Bingcheng invests 500 million yuan in DeepSeek&\#x27;s reported second funding round](#item-finance-news-2) ⭐️ 7.0/10
3. [PBOC Lowers Personal Large-Denomination CD Minimum to 100,000 Yuan](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenSec Discloses Critical Pre-Auth Linux NFS Root Vulnerability CVE-2026-99362](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 9.0/10

OpenSec has publicly disclosed CVE-2026-99362, a pre-authentication heap overflow in the Linux kernel&\#x27;s NFS server \(nfsd\) with a CVSS score of 9.8. An attacker who can reach TCP port 2049 can trigger an out-of-bounds kernel heap write without logging in and obtain a root shell. The flaw has existed since Linux 3.16 \(2014\) and affects hosts with NFSv4.1 or 4.2 enabled, including file servers, NAS devices, and cluster storage nodes. Fixes are available in kernel versions 6.12.117, 6.18.61, 7.3.2, and 7.4-rc1, requiring a kernel upgrade and reboot; organizations that cannot upgrade immediately should restrict access to tcp/2049 with a firewall. The CVE was made public on November 20, 2026.

telegram · zaihuapd · Nov 27, 12:57

**「Background」** The Linux kernel NFS server \(nfsd\) implements the Network File System protocol and listens on TCP port 2049; NFSv4.1 and 4.2 are commonly enabled versions on file servers, NAS appliances, and cluster storage nodes. CVE-2026-99362 is a pre-authentication heap overflow: an attacker who can reach port 2049 can write past a kernel heap object without logging in, because the flaw exists in code reachable before authentication. The vulnerability reportedly dates back to Linux 3.16 \(2014\), making it a roughly 12-year-old issue in widely deployed kernels.

**「Impact」** Any unauthenticated remote attacker who can reach TCP port 2049 on a Linux NFS server running NFSv4.1 or 4.2 can exploit this heap overflow to gain root, putting internet-exposed NFS servers and internal storage nodes at immediate risk until they upgrade to fixed kernels \(6.12.117, 6.18.61, 7.3.2, 7.4-rc1\) or block port 2049.

<details><summary>References</summary>
<ul>
<li><a href="https://opensec.in/blog/nfs2root-cve-2026-99362">NFS 2ROOT ( CVE - 2026 - 99362 ): pre-auth root in Linux nfsd | OpenSec</a></li>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS 2ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS 2ROOT Linux flaw can let attackers gain root privileges</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-nfs2root-linux-flaw-can-let-attackers-gain-root-privileges/">New NFS2 ROOT Linux flaw can let attackers gain root privileges</a></li>
<li><a href="https://www.getpagespeed.com/server-setup/security/nfs2root-cve-2026-99362-centos-7">NFS2 ROOT ( CVE - 2026 - 99362 ) on CentOS 7: Fixed Kernel</a></li>

</ul>
</details>

**Tags**: `#security`, `#linux-kernel`, `#nfs`, `#vulnerability`, `#cve`

---

<a id="item-tech-news-2"></a>
### [DJB Catalogs False Proofs Accepted by Proof Checkers](https://cr.yp.to/proofs/falseccp.html) ⭐️ 8.0/10

Daniel J. Bernstein&\#x27;s page catalogues cases in which computer proof checkers have accepted false proofs, exposing soundness vulnerabilities in formal verification systems. The collection documents concrete bugs across multiple checkers, including an exploit by a DeepMind researcher that passed Lean and a then-week-old version of nanoda using different flaws. These cases matter because a single incorrect verification is not enough to mislead working mathematicians: independent reviews and multiple independent verifiers create defense in depth, but the bugs show that trust in any one checker can be misplaced. The page also notes that systems such as Metamath require proofs to pass five independently created verifiers in five programming languages before acceptance into main databases. Despite the historical soundness bugs being relatively few, the catalog argues for further high-assurance work.

hackernews · \_tk\_ · Nov 27, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50667989)

**「Background」** Computer proof checkers are programs that claim to verify every step of a formal proof; a soundness bug is a defect that can allow a false statement to be accepted as proved. Daniel J. Bernstein&\#x27;s page collects cases where such bugs were reported in systems including Lean, nanoda, and Metamath, showing that formal verification is not immune to implementation errors.

**「Impact」** Users of formal verification systems cannot treat a passing proof as absolute proof of mathematical truth; they must rely on multiple independent checkers and informal review to mitigate soundness bugs.

**「Community Discussion」** Commenters broadly agreed that soundness bugs exist but emphasized that multiple independent verifiers and informal review provide strong mitigations; some argued the page understates the difficulty of deceiving mathematicians, while others noted that the total known soundness bugs remain small relative to typical software assurance levels. A separate comment highlighted a deeper issue where formal proofs can be correct against an incorrect formalization of the requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://cr.yp.to/proofs/falseccp.html">False computer - checked proofs (djb)</a></li>

</ul>
</details>

**Tags**: `#formal-verification`, `#proof-assistants`, `#soundness`, `#software-correctness`, `#lean`

---

<a id="item-tech-news-3"></a>
### [AWS Trainium3 Inference and Microarchitecture Deep Dive](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 8.0/10

SemiAnalysis published a deep dive by Kimbo Chen examining AWS Trainium3 inference performance, microarchitecture, and cost competitiveness against NVIDIA GB300. The analysis reports better performance per total cost of ownership \(TCO\) than GB300 and describes a first-principles physics-based architecture, high model FLOPs utilization \(MFU\) and memory bandwidth utilization \(MBU\), the UBenchX benchmark, and low-latency characteristics. The article is intended for AI/ML infrastructure and hardware readers evaluating next-generation inference silicon.

rss · Semianalysis · Nov 27, 15:54

**「Background」** AWS Trainium3 is Amazon&\#x27;s custom AI accelerator designed to compete with NVIDIA&\#x27;s GB300 NVL72 rack-scale GPU systems for AI inference. SemiAnalysis&\#x27; deep dive examines Trainium3&\#x27;s microarchitecture and reports that AWS&\#x27;s first Trainium3 UltraServer AgentX submission achieved up to 2.28x better inference performance per dollar compared with GB300 NVL72, B300, and MI355 systems. The analysis also uses UBenchX to assess low-level latency, memory bandwidth, and compute utilization.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/trainium3-inferencex">AWS Challenger: Trainium3 Inference and Microarchitecture ...</a></li>
<li><a href="https://cryptobriefing.com/trainium3-nvidia-gb300-inference-benchmark/">Trainium3 competes with Nvidia GB300 in inference performance ...</a></li>
<li><a href="https://explainx.ai/blog/amazon-trainium3-ultraserver-agentx-performance-per-dollar-claimed-vs-verified-november-2026">Trainium3 2.28x vs GB300: What SemiAnalysis Shows | explainx ...</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#Trainium3`, `#AI hardware`, `#semiconductors`, `#inference`

---

<a id="item-tech-news-4"></a>
### [Google&\#x27;s DeepCrossAttention achieves comparable model quality up to 3x faster](https://research.google/blog/supercharging-transformer-residual-connections/) ⭐️ 7.0/10

Google Research has introduced DeepCrossAttention, described in the blog post “Supercharging Transformer Residual Connections,” which speeds up transformer training by up to 3x while maintaining comparable model quality. The technique modifies transformer residual connections and is aimed at AI/ML engineers. According to the item, the method could inform model training practices, but it is not yet widely adopted or proven beyond the presented results.

hackernews · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**「Background」** Transformer models commonly use residual connections that add the output of a previous layer to the current layer&\#x27;s output, but these simple sums can dilute crucial information. DeepCrossAttention \(DCA\) instead uses input-dependent, depth-wise cross-attention for the Query, Key, and Value components of the transformer, which refines residual learning. Google Research details this approach in a blog post and an associated paper, reporting up to 3x faster training with comparable model quality.

**「Impact」** For developers training deep transformer models, Google Research reports that DeepCrossAttention can match model quality up to 3× faster and cut LM1B model depth by up to 29%, but these results come from research experiments and are not yet widely adopted.

**「Community Discussion」** Commenters questioned the use of line graphs where bar graphs would be more appropriate, speculated whether the efficiency gains relate to Gemini Neon&\#x27;s low cost and speed, and wondered if combining DeepCrossAttention with techniques like MTP and DFlash could yield further throughput improvements; one commenter also noted a resemblance to DenseNet.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2502.06785v1">DeepCrossAttention : Supercharging Transformer Residual ...</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention: Supercharging Transformer Residual ...</a></li>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections - Google Research</a></li>
<li><a href="https://explainx.ai/blog/google-deepcrossattention-transformer-residual-connections-2026">DeepCrossAttention (DCA): Google Fix for Deep Transformers ...</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#deep-learning`, `#machine-learning`, `#model-training`, `#google-research`

---

<a id="item-tech-news-5"></a>
### [Credit Card Skimming Scripts Using WebRTC Found on Shopping Sites](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer) ⭐️ 7.0/10

Malicious credit card skimming scripts have been discovered on popular shopping sites using WebRTC, a technique that is less frequently monitored for nefarious behavior than standard HTTP requests. The skimmers exfiltrate payment data while evading detection by using WebRTC, which often bypasses content security policies and network monitoring focused on HTTP traffic. The discovery was reported on November 27, 2026, during the Black Friday shopping period, a high-volume time for online transactions. This represents a new evasive tactic for e-commerce skimming attacks and highlights the persistent risk of embedding third-party scripts on retail websites. The technique does not rely on any special WebRTC capability but rather on the relative lack of monitoring for that protocol.

hackernews · scanr · Nov 27, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50668145)

**「Background」** WebRTC is a browser API for real-time peer-to-peer communication that also supports data channels capable of sending arbitrary data between browsers and servers. Traditional payment-card skimmers typically exfiltrate stolen card numbers via HTTP requests to attacker-controlled endpoints, but using WebRTC data channels instead is a newer evasion tactic because such traffic is encrypted and less commonly monitored or flagged by security tools. The technique was observed on Magento-based online stores before Black Friday, including Lascana, Samsonite, and American Tourister.

**「Impact」** Online shoppers and e-commerce operators face increased risk of payment-card theft because WebRTC-based skimmers hide exfiltration inside legitimate peer-to-peer traffic that evades traditional security filters, and a March 2026 campaign exploited a PolyShell vulnerability in Magento and Adobe Commerce to inject skimmers through poisoned marketing scripts.

**「Community Discussion」** Commenters note that the attack exploits the lack of WebRTC monitoring rather than any inherent capability, and that any third-party script execution carries risk. Some argue the root cause is the web&\#x27;s model of allowing arbitrary code execution and the continued use of symmetric payment secrets, while others suggest sandboxing ads or disabling JavaScript for third-party content.

<details><summary>References</summary>
<ul>
<li>Credit card skimming scripts using WebRTC found on... - daily.dev</li>
<li>A new Magento skimmer uses WebRTC data channels instead of ...</li>
<li><a href="https://www.theprotec.com/blog/webrtc-credit-card-skimming-shopping-sites/">How WebRTC Credit Card Skimming Breached Major Shopping Sites</a></li>
<li><a href="https://www.machucavalley.tech/blog/webrtc-credit-card-skimming-ecommerce/">The Invisible Leak: How Hackers are Using WebRTC to Steal ...</a></li>
<li><a href="https://rhisac.org/threat-intelligence/webrtc-based-payment-skimmer-targeting-ecommerce-sites-via-polyshell-vulnerability/">WebRTC-Based Payment Skimmer Targeting ECommerce ... - RH-ISAC</a></li>

</ul>
</details>

**Tags**: `#web security`, `#credit card skimming`, `#WebRTC`, `#e-commerce`, `#malware`

---

<a id="item-tech-news-6"></a>
### [Convex skills upload user app ideas to remote server without disclosure](https://github.com/convex/convex-backend-skill/issues/64) ⭐️ 7.0/10

A GitHub issue reports that Convex skills upload a user&\#x27;s app idea to a remote server without informing them. Convex CEO Jamie confirmed that the prompt upload powers the Convex &\#x27;quickstart&\#x27; feature, the spiritual successor to the now-shut-down Convex Chef project. The disclosure has raised privacy and trust concerns in AI-assisted development, particularly because users are not explicitly told their prompts are sent to the server.

hackernews · MickyTheMouse · Nov 27, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50669765)

**「Background」** Convex is a backend platform that provides “skills” for AI coding assistants to scaffold and configure projects. The quickstart skill sends the user’s one-sentence app idea to a Convex-hosted endpoint as telemetry, and the add skill pipes a remote script from the same host directly into bash, without informing the user. A developer’s verification documented three telemetry calls before app creation, including fetching an unpinned 3,015-line bootstrap with an instruction to avoid safety classifiers.

**「Privacy and trust risk」** Developers using the Convex skills plugin or quickstart feature may unknowingly send their app ideas and prompts to Convex&\#x27;s servers without explicit informed consent, eroding trust in AI-assisted development tools.

**「Community Discussion」** Comments highlight trust concerns, with one user saying &\#x27;Trust is the new attention&\#x27; and another advocating self-hosted open weight models as a long-term path. A commenter also notes that prompt injection is more common than malicious tool calls, and one user is confused by an unrelated content promotion in the issue thread.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/convex/convex-backend-skill/issues/64">Convex skills send the user&#x27;s app idea to a remote server ...</a></li>
<li><a href="https://dev.to/frankchu/3-telemetry-calls-before-your-app-exists-convex-skills-69f">3 telemetry calls before your app exists — Convex skills</a></li>
<li>Convex skills send the user&#x27;s app idea to a remote server without telling ...</li>

</ul>
</details>

**Tags**: `#AI`, `#security`, `#privacy`, `#developer-tools`, `#prompt-injection`

---

<a id="item-tech-news-7"></a>
### [States Sue SpaceX Over Grok Child Sex and Revenge Porn Images](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform) ⭐️ 7.0/10

State attorneys general have sued SpaceX, the parent company of X and xAI, alleging that the Grok image generator creates and promotes child sexual abuse material and non-consensual intimate images, including revenge porn. The legal action, announced by the Virginia Attorney General’s office, seeks to stop Grok from generating such content and to hold the platform accountable. It names SpaceX, X, xAI, and Grok and focuses on alleged violations related to child exploitation and non-consensual imagery.

hackernews · DeepLogin · Nov 27, 19:42 · [Discussion](https://news.ycombinator.com/item?id=50670855)

**「Background」** Grok is an AI image generation tool created by xAI and available on the X platform; the lawsuits name SpaceX as the parent company of X, xAI, and Grok. Virginia Attorney General Jay Jones and Oregon Attorney General Rayfield filed separate but similar suits alleging that SpaceX allowed Grok and X to create, host, and share child sexual abuse material and non-consensual sexualized images, and that the product was designed without the necessary safeguards. The cases seek accountability and new consumer protections, reflecting growing state-level enforcement against AI-generated deepfake and child exploitation content.

**「Community Discussion」** Commenters debated whether Grok needed to be tricked into producing the images or was unusually permissive; one noted that U.S. Supreme Court precedent may protect AI-generated CSAM for private use, while revenge porn involving real people remains legally distinct.

<details><summary>References</summary>
<ul>
<li><a href="https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform">Attorneys General Jones and Rayfield File Suit Against SpaceX ...</a></li>
<li><a href="https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-takes-legal-action-against-grok-for-failing-to-block-child-exploitation/">Oregon Attorney General Rayfield and Virginia Attorney ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/23/oregon-virginia-spacex-grok-deepfake-lawsuits.html">SpaceX sued by 2 states over AI deepfake porn, Grok ... - CNBC</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#generative AI`, `#legal`, `#content moderation`, `#child safety`

---

<a id="item-tech-news-8"></a>
### [Michael Nielsen Removes Neural Networks and Deep Learning Book](https://neuralnetworksanddeeplearning.com/) ⭐️ 7.0/10

Michael Nielsen has removed his free online book &quot;Neural Networks and Deep Learning&quot; from its website, apparently as a protest over AI risks. The book had been a widely used introductory resource for learning neural networks. Its removal restricts direct access to the original site, though archived copies remain available. The move has sparked debate in the AI community about whether restricting educational material helps or hinders AI safety.

hackernews · brandonb · Nov 27, 19:31 · [Discussion](https://news.ycombinator.com/item?id=50670757)

**「Background」** Neural Networks and Deep Learning is a free online textbook written by Michael Nielsen between 2011 and 2015. It offers a mathematically grounded introduction to neural networks and deep learning, making it a common starting point for students and practitioners. The book&\#x27;s step-by-step explanations and worked examples helped it become a widely referenced resource in AI education.

**「Impact on Access to Learning Resource」** The deliberate removal means newcomers to neural networks lose direct access to a widely used free online textbook at its original location, though the text remains available through archived and mirror copies.

**「Community Discussion」** Commenters disagreed on the effectiveness of the removal: some argued withholding knowledge is a misstep because understanding neural networks better prepares people for outcomes, while others saw it as a symbolic protest that may increase interest in the book. One commenter also claimed artificial superintelligence has already been achieved, and another provided an archived copy.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/frankchu/1000x-off-the-book-that-taught-ai-just-quit-137b">1,000x off: the book that taught AI just quit - DEV Community</a></li>
<li><a href="http://neuralnetworksanddeeplearning.com/">Neural networks and deep learning</a></li>
<li><a href="https://jingyuexing.github.io/Ebook/Machine_Learning/Neural+Networks+and+Deep+Learning-eng.pdf">1 Neural networks and deep learning .pdf</a></li>

</ul>
</details>

**Tags**: `#ai-safety`, `#deep-learning`, `#neural-networks`, `#online-education`, `#technology-news`

---

<a id="item-tech-news-9"></a>
### [US Intelligence Agencies Hit by AI-Assisted Hack Using Artex](https://www.forbes.com/sites/the-wiretap/2026/11/25/us-government-under-ai-cyberattack) ⭐️ 7.0/10

According to The New York Times, hackers targeted the CIA, the National Geospatial-Intelligence Agency, and the Office of the Director of National Intelligence in an attack assisted by the open-source AI tool Artex. The attack appeared not severe and affected unclassified reconnaissance data. Artex integrates multiple open-source AI models to test network and computer defenses. A Chinese developer released Artex earlier this year and later removed it from GitHub after it was used in multiple attacks, including one against the EU. Earlier this year the FBI warned that cybercriminals and spies were widely using Artex.

telegram · zaihuapd · Nov 27, 10:42

**「What is Artex?」** Artex is an open-source AI tool that can integrate multiple open-source AI models to test network and computer defenses. Originally created for authorized security testing, it has been repurposed by attackers to rapidly scan victim networks for weaknesses; the FBI issued a FLASH advisory on November 13 warning that cybercriminals and spies are widely abusing Artex, reportedly enabling network breaches in under three hours.

**「Impact」** The concrete consequence is limited because the attack compromised unclassified reconnaissance data, not classified intelligence systems.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/">FBI says Artex AI open source hacking tool used to... | TechCrunch</a></li>
<li><a href="https://www.malwarebytes.com/blog/ai/2026/11/criminals-are-using-artex-ai-agents-to-speed-up-cyberattacks-fbi-warns">Criminals are using ARTEX AI agents to speed up cyberattacks, FBI ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI`, `#government hacking`, `#open source`, `#intelligence agencies`

---

<a id="item-tech-news-10"></a>
### [Anthropic System Cards Reveal Covert Degradation of Frontier Model Requests](https://news.ycombinator.com/item?id=50664325) ⭐️ 7.0/10

Anthropic&\#x27;s June system cards for Claude Mythos 5 and Fable 5 state that requests aimed at developing frontier large models are silently limited through prompt rewriting, steering vectors, and parameter-efficient fine-tuning, without visible fallback. The intervention covers pretraining pipelines, distributed training, and accelerator design tasks, and Anthropic estimates it affects about 0.03% of traffic and fewer than 0.1% of organizations, with most coding unaffected. Because using Claude to build competing models already violates Anthropic&\#x27;s terms of service, the disclosure gained renewed attention in developer discussions this week.

telegram · zaihuapd · Nov 27, 13:42

**「Background」** System cards are documents that AI developers like Anthropic publish to describe a model’s capabilities, safety evaluations, and responsible deployment decisions; Anthropic’s system-cards page lists cards for Claude models. The source item refers to system cards for Claude Mythos 5 and Fable 5, which Anthropic released in June of this year. These cards can include details on how the model handles particular request types, including interventions that differ from normal safety blocking.

**「Impact」** Users or organizations attempting frontier-model development with Claude may receive degraded assistance in pretraining, distributed training, and accelerator design without any visible notice or fallback.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#anthropic`, `#ai-safety`, `#large-language-models`, `#model-training`, `#technology-policy`

---

<a id="item-tech-news-11"></a>
### [Minecraft Bedrock Resource Pack Vulnerability Fixed in 26.65](https://www.zaikei.co.jp/article/20261119/878386.html) ⭐️ 7.0/10

A resource pack vulnerability in Minecraft Bedrock Edition allowed packs containing a content.zipe file to modify Ore UI framework files and execute hidden scripts. The issue was publicly disclosed by add-on developer 8Crafter on Reddit on November 15 and was confirmed to affect versions 26.52 through 26.63, with earlier versions possibly affected; it impacts PC, mobile, and console versions, while Java Edition is unaffected. Players joining a server or Realm with automatic resource pack downloads enabled could receive the problematic file without manual installation. Documented exploit methods include deleting all saves and obtaining player IP addresses; on Windows under certain conditions, it can also open arbitrary URIs without prompting or launch a batch file inside the resource pack to download malware. Mojang has fixed the vulnerability in version 26.65, and AxmBro released a Windows read-only detection tool that finds content.zipe but cannot determine whether a resource pack is malicious.

telegram · zaihuapd · Nov 27, 18:04

**「Background」** Minecraft Bedrock Edition supports resource packs that customize game assets, and Ore UI is its user interface framework. Automatic resource pack downloads are a common feature when joining servers or Realms, which can deliver pack files to players without a separate manual installation step.

**「Impact」** Players on Bedrock Edition versions 26.52 through 26.63 who join servers or Realms with automatic resource pack downloads enabled should update to 26.65 or avoid auto-downloading packs to prevent hidden script execution, save deletion, IP exposure, and possible malware delivery on Windows.

**Tags**: `#Minecraft`, `#security vulnerability`, `#Bedrock Edition`, `#resource pack`, `#game security`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s State Council vows to strengthen national team market stabilization and optimize Huijin quasi stabilization fund](https://www.tmtpost.com/nictation/8220182.html) ⭐️ 9.0/10

China&\#x27;s State Council said on Nov. 27 it will strengthen the &\#x27;national team&\#x27; market stabilization role, optimize Central Huijin&\#x27;s quasi stabilization fund, and improve policies guiding insurers, annuities, and social security funds into markets.

telegram · zaihuapd · Nov 27, 05:35

**「Background」** Premier Li Qiang chaired the November 27 State Council executive meeting; Central Huijin is a state-owned investment company whose market-buying role is often described as a quasi stabilization fund.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cls.cn/detail/2546318">cls.cn/detail/2546318</a></li>

</ul>
</details>

**Tags**: `#China`, `#State Council`, `#capital markets`, `#stabilization fund`, `#policy`

---

<a id="item-finance-news-2"></a>
### [Mixue Bingcheng invests 500 million yuan in DeepSeek&\#x27;s reported second funding round](https://m.sohu.com/a/1107027659_115479) ⭐️ 7.0/10

DeepSeek has completed a second financing round of 100 billion to 105.5 billion yuan at a post-investment valuation of about 615.5 billion yuan, according to a Sohu report; Mixue Bingcheng invested 500 million yuan, joining Tencent, CATL, China Mobile, and vivo among 31 new investors.

telegram · zaihuapd · Nov 27, 06:33

**「Background」** Prior to this round, DeepSeek had completed its first financing in June with about 50 billion yuan raised at a valuation above 350 billion yuan, and reports before the second round placed its pre-investment valuation at 500 billion yuan.

<details><summary>References</summary>
<ul>
<li><a href="https://post.smzdm.com/p/aom07rr7/">DeepSeek 估 值 5000 亿 重启 融 资 ，自建智算中心并涨价_IT...</a></li>
<li><a href="https://www.php.cn/faq/2947867.html">消息称 DeepSeek 重启 第 二 轮 500 亿 元 融 资 投 前 估 值 升至 5000...</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#funding round`, `#Mixue Bingcheng`, `#AI industry`, `#venture capital`

---

<a id="item-finance-news-3"></a>
### [PBOC Lowers Personal Large-Denomination CD Minimum to 100,000 Yuan](https://www.news.cn/fortune/20261127/70789d77822242cc82216f51a416f872/c.html) ⭐️ 7.0/10

The People&\#x27;s Bank of China announced new large-denomination certificate of deposit rules on November 27, lowering the personal purchase threshold from 200,000 yuan to 100,000 yuan and the institutional threshold from 10 million yuan to 5 million yuan, effective March 21, 2027. The same day it issued rate rules requiring financial institutions to set deposit and loan rates independently and barring high-interest deposit solicitation.

telegram · zaihuapd · Nov 27, 11:36

**「Background」** The new rules replace the 2015 interim measures, under which the minimum purchase amounts were 200,000 yuan for individuals and 10 million yuan for institutions.

**「Impact」** From March 21, 2027, individual savers with 100,000–200,000 yuan gain access to large-denomination certificates of deposit, while banks face tighter restrictions on competing for deposits through high interest rates.

**Tags**: `#PBOC`, `#large-denomination certificates of deposit`, `#deposit rate regulation`, `#banking regulation`, `#China finance`

---