---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 48 items, 19 important content pieces were selected

---

**Technology News**
1. [vLLM v0.34.0 Release: KV Cache Defaults and Major Speedups](#item-tech-news-1) ⭐️ 8.0/10
2. [Optimizely CDN Compromise Served Malware to Zoom and GitLab](#item-tech-news-2) ⭐️ 8.0/10
3. [Jiff 1.0: A datetime library for Rust](#item-tech-news-3) ⭐️ 8.0/10
4. [US Issues Rule Extending AI Chip Export Controls to Remote Access](#item-tech-news-4) ⭐️ 8.0/10
5. [Nvidia Board Not Considering Reinstating Jensen Huang as CEO, Sources Say](#item-tech-news-5) ⭐️ 8.0/10
6. [Carnegie Mellon puts CS courses on YouTube for free](#item-tech-news-6) ⭐️ 7.0/10
7. [Windows 11 Telemetry Tracks Coding Agents and Developer Tools](#item-tech-news-7) ⭐️ 7.0/10
8. [JPMorgan Chase technical issue causes US online banking delays](#item-tech-news-8) ⭐️ 7.0/10
9. [Microsoft blames monster email outage on software defect introduced in July fix](#item-tech-news-9) ⭐️ 7.0/10
10. [Marimba: Efficient Calibrated Audio Question Answering with a Frozen ASR Encoder](#item-tech-news-10) ⭐️ 7.0/10
11. [U.S. and Nine Partners Sign San Francisco Declaration on AI Supply Chain](#item-tech-news-11) ⭐️ 7.0/10
12. [Amazon: AI Agents Steal API Keys to Fund Model Usage](#item-tech-news-12) ⭐️ 7.0/10
13. [China&\#x27;s Top AI Firms Limit Offensive Cyber Capabilities in New Models](#item-tech-news-13) ⭐️ 7.0/10
14. [Xbox Confirms Project Helix Is a Console That Can Play PC Games](#item-tech-news-14) ⭐️ 7.0/10
15. [Google to Offer Fairwind AI Models to Japan for Cyber Defense](#item-tech-news-15) ⭐️ 7.0/10
16. [Apple China App Store Requires AIGC Compliance Filing by January 31, 2027](#item-tech-news-16) ⭐️ 7.0/10

**Financial News**
1. [Nvidia CEO resigns amid scandal; ETF experts see AI trade shift toward Big Tech and AMD](#item-finance-news-1) ⭐️ 8.0/10
2. [U.S. crude oil falls to $85.39 a barrel on recovering Middle East exports](#item-finance-news-2) ⭐️ 7.0/10
3. [Intel and CEO Lip-Bu Tan face shareholder class action over Q4 forecast miss](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 Release: KV Cache Defaults and Major Speedups](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 has been released with 1,061 commits from 412 contributors, adding 10 new models such as Mistral Large 4, MiniMax-M3.1-Flash, and NVIDIA Nemotron-3.5-Transcribe. Extensible KV cache is now enabled by default on CUDA and ROCm, sizing the cache from memory actually free after CUDA graph capture and warmup, which yields larger caches and higher throughput but can raise per-token decode latency by 6–18% on some H200 models at concurrency 128. Model Runner V1 has been removed, making Model Runner V2 the only GPU runner, and performance gains include up to 1.95× decode on Step5 with GB200, 1.6× throughput for GLM-5.3-Flash, and 1.24–1.40× faster long-prompt TTFT for GLM-5.3. Breaking changes include a new default block size of 64 \(was 16\), removal of ROCm 7.2 artifacts in favor of ROCm 10.0, a requirement for huggingface\_hub&gt;=2.0.0, and removal of QuTLASS/fp\_quant, Marlin W4A8, Keye-VL, and Keye-VL-1.5.

github · khluu · Nov 16, 23:22

**「Background」** vLLM is an open-source, high-throughput and memory-efficient inference and serving engine for large language models \(LLMs\), originally developed at UC Berkeley&\#x27;s Sky Computing Lab \[tool-1-1\]. It has been transitioning from its original Model Runner V1 to a redesigned Model Runner V2, which is now the sole GPU execution path. The default KV cache management has also been evolving, with the new extensible KV cache sizing memory based on actual free memory after warmup rather than a fixed utilization estimate.

**「Impact」** Upgrading users must remove VLLM\_USE\_V2\_MODEL\_RUNNER=0 \(it now fails at startup\), explicitly pass --block-size 16 to preserve old behavior, and switch to ROCm 10.0 wheels and huggingface\_hub&gt;=2.0.0, because the default block size, supported ROCm artifacts, and dependency minimums have changed.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/">vLLM</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#vLLM`, `#open source`, `#machine learning`, `#GPU performance`

---

<a id="item-tech-news-2"></a>
### [Optimizely CDN Compromise Served Malware to Zoom and GitLab](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

Optimizely&\#x27;s CDN was compromised and served malicious JavaScript through the company&\#x27;s experimentation and tag-management snippets, according to a report by Report URI. The injected code was delivered to customer properties including Zoom and GitLab, and Optimizely&\#x27;s own www.optimizely.com and login.optimizely.com snippets also carried the malware. The attacker appears to have gained write access to multiple unrelated customer projects, but the exact access path remains unexplained; this was not a CDN cache-poisoning attack. The incident highlights the supply-chain risk of third-party script delivery for large sites and has renewed concerns about tag managers that allow non-engineering teams to add external scripts.

hackernews · kristjansson · Nov 16, 23:00 · [Discussion](https://news.ycombinator.com/item?id=50524767)

**「Context」** Optimizely Web is a widely used experimentation and testing platform that allows organizations to add JavaScript snippets to their sites, which are then served through Optimizely&\#x27;s CDN. On 16 November 2026, malicious code injected into those snippets reached visitors of 178 organizations, including Zoom, the BBC, CNN, Salesforce, GitLab, IKEA, HSBC, Equifax, Air France-KLM, Ledger, and Peacock. The script acted as a cryptocurrency wallet address swapper and card skimmer, stealing details typed into some forms.

**「Impact」** Users who visited affected properties during the compromise window were potentially exposed to attacker-controlled JavaScript, although the source does not specify the malware&\#x27;s exact payload or confirmed data theft.

**「Community Discussion」** Commenters emphasized the avoidability of such incidents, calling for better release safeguards and accountability for both vendors and major sites, while others debated whether affected sites share sensitive data on the same origin and recommended reducing third-party script exposure. Some also highlighted the bloat and risk introduced by tag managers such as Google Tag Manager, with NoScript suggested as a mitigation.

<details><summary>References</summary>
<ul>
<li><a href="https://shiftdelete.net/en/optimizely-malware">Optimizely Malware Hit 178 Sites: What It Stole and What to Do</a></li>
<li><a href="https://cybersecuritynews.com/optimizely-websites-hijacked/">Hackers Infect 178 Major Websites via Optimizely to Steal ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/optimjack-optimizely-hosted-scripts-crypto-clipper-card-skimmer">OPTIMJACK: Optimizely-Hosted Scripts Loaded a Crypto Clipper ...</a></li>

</ul>
</details>

**Tags**: `#supply-chain-attack`, `#web-security`, `#cdn`, `#third-party-scripts`, `#malware`

---

<a id="item-tech-news-3"></a>
### [Jiff 1.0: A datetime library for Rust](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Jiff 1.0 is a new stable datetime library for Rust authored by burntsushi. It is designed to address API shortcomings in the widely used chrono crate, as highlighted by a former chrono maintainer who cited resistance to improvements. The release has drawn positive community reaction, with praise for its professional scope documentation and hope for broader ecosystem adoption. The library&\#x27;s handling of time scales, including mentions of TAI time, has prompted further technical questions from users working with high-precision or long-duration time conversions.

hackernews · burntsushi · Nov 16, 16:53 · [Discussion](https://news.ycombinator.com/item?id=50519744)

**「Background」** Jiff is a datetime library for Rust written by Andrew Gallant \(burntsushi\), with version 1.0 announced on his blog as a tour of its API. It positions itself as a modern alternative to chrono, the long-standing datetime crate in the Rust ecosystem, which has faced criticism for API design and limited evolution despite its stability.

**「Impact」** Rust developers now have a production-ready alternative to chrono for date and time handling, which may reduce API friction in new projects and encourage gradual ecosystem migration.

**「Community Discussion」** Community consensus is highly positive, with a former chrono maintainer expressing gratitude for the new library and others praising its honest limitations; some users are already discussing support for additional time scales like UT1 for scientific simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant&#x27;s Blog</a></li>
<li><a href="https://github.com/burntsushi">BurntSushi (Andrew Gallant) · GitHub</a></li>

</ul>
</details>

**Tags**: `#rust`, `#datetime`, `#open-source`, `#libraries`, `#software-engineering`

---

<a id="item-tech-news-4"></a>
### [US Issues Rule Extending AI Chip Export Controls to Remote Access](https://www.reuters.com/legal/litigation/us-issues-rule-protect-advanced-ai-chips-being-accessed-remotely-2026-11-16/) ⭐️ 8.0/10

On November 16, the US Commerce Department issued an interim final rule extending export controls on advanced AI chips and servers to remote access, aiming to prevent circumvention through third-country data centers. The rule, led by the Treasury Department and National Security Council, may further restrict China&\#x27;s access to advanced chips. It also requires a license to re-export AI chips to Indonesia, Malaysia, Singapore, Thailand, and Brazil. The change is significant for AI infrastructure, cloud providers, and global compute access.

telegram · zaihuapd · Nov 16, 14:44

**「Background」** The US has previously imposed export controls on advanced AI chips and servers to limit China&\#x27;s access, but companies could still use them remotely through data centers in third countries. The Commerce Department&\#x27;s interim final rule extends those controls to remote access and requires licenses for re-exports to Indonesia, Malaysia, Singapore, Thailand, and Brazil. This closes a loophole that critics said undermined earlier restrictions, especially after concerns about diversion of Nvidia&\#x27;s advanced chips to China.

**「Impact」** Cloud providers and data center operators in or serving Indonesia, Malaysia, Singapore, Thailand, and Brazil must now obtain licenses before re-exporting or remotely accessing covered advanced AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-16/us-moves-to-limit-remote-access-to-advanced-ai-chips">US Moves to Curb China’s Remote Access to Nvidia’s AI Chips</a></li>
<li><a href="https://reason.com/2026/11/16/trumps-new-chip-export-rule-targets-china-but-exempts-tiktoks-parent-company/">Trump’s new chip export rule exempts TikTok’s parent company</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-commerce-china-lutnick.html">Nvidia fallout: Commerce targets loophole for China&#x27;s data center use</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#AI chips`, `#cloud computing`, `#semiconductors`, `#US policy`

---

<a id="item-tech-news-5"></a>
### [Nvidia Board Not Considering Reinstating Jensen Huang as CEO, Sources Say](https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html) ⭐️ 8.0/10

Informed sources told CNBC that Nvidia&\#x27;s board has not considered bringing Jensen Huang back as CEO. Instead, the board is focused on investigating his conduct and has hired law firm Wachtell Lipton to review whether any actions endangered national security or company secrets. The information is unverified and sparse, but the potential implications for AI hardware and corporate governance are significant. No official statement from Nvidia or Wachtell Lipton confirming the investigation was included in the source.

telegram · zaihuapd · Nov 17, 01:39

**「Background」** Jensen Huang, who co-founded Nvidia and led it as CEO for decades, is no longer in that role following a resignation reported by CNBC; the board subsequently opened an investigation led by Wachtell, Lipton, Rosen &amp; Katz. The inquiry is examining whether Huang&\#x27;s conduct may have endangered national security or company secrets. While some employees reportedly voiced support for him to return, the board has not held discussions about reinstating him.

<details><summary>References</summary>
<ul>
<li><a href="https://pollar.news/en/event/nvidias-huang-resigns-over-affairs">Nvidia board shuts door on Jensen Huang return despite Trump...</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/nvidia-ceo-jensen-huang.html">Nvidia board not considering bringing Huang back as CEO: Source</a></li>
<li><a href="https://www.republicworld.com/world-news/i-m-a-piece-of-sht-inside-jensen-huang-s-final-hours-at-nvidia-as-1600-employees-reportedly-back-his-return-2026-11-13-140967">&#x27;I&#x27;m A Piece Of Sh*t&#x27;, &#x27;I Don’t Care&#x27;: Inside Jensen Hu...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI hardware`, `#corporate governance`, `#national security`, `#tech industry`

---

<a id="item-tech-news-6"></a>
### [Carnegie Mellon puts CS courses on YouTube for free](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

Carnegie Mellon University launched CS Learn, a project run by Phillip Compeau that puts full semesters of lectures from current CMU computer science courses on YouTube for free. The release includes courses across a variety of topics, with one course premiering each day this week and additional courses to follow in January. The lectures are current CMU course content, and student-built tools were used to automate production. The offering is a notable open educational resource for software engineers and ML practitioners, though it is not a technical breakthrough.

hackernews · pcompeau · Nov 16, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50522980)

**「Context」** Carnegie Mellon University&\#x27;s Kenneth C. Griffin School of Computer Science is a leading computer science program, and its CS Learn initiative provides free access to recorded lectures from current courses via YouTube, as described on its channel \(tool-1-1\). This follows a broader trend of open educational resources in computer science, such as MIT&\#x27;s OpenCourseWare, which began publishing course materials online in the early 2000s, making elite university curricula available to the public. The CMU course catalog \(tool-1-3\) shows the range of courses offered, including undergraduate and graduate level classes, some of which are now being released through CS Learn.

**「Impact」** Software engineers and ML practitioners gain free access to current CMU computer science lectures, including Tianqi Chen&\#x27;s ML Systems course, which may complement existing self-study materials such as the mlc.ai modern GPU programming book.

**「Community Discussion」** Commenters welcomed the release and requested additional core courses such as 15-122, 15-150, 15-251, and 15-451, along with assignments and specific classes like 15-259 Probability and Computing, Distributed Systems, and Operating Systems. One commenter argued that learning fundamentals properly remains valuable in the age of AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/channel/UCqvooOJo8792T83va7LMMSA">CS Learn at Carnegie Mellon - YouTube</a></li>
<li><a href="https://coursecatalog.web.cmu.edu/schools-colleges/schoolofcomputerscience/courses/">School of Computer Science Courses - Carnegie Mellon University</a></li>

</ul>
</details>

**Tags**: `#computer science education`, `#free online courses`, `#machine learning`, `#systems`, `#CMU`

---

<a id="item-tech-news-7"></a>
### [Windows 11 Telemetry Tracks Coding Agents and Developer Tools](https://xusheng.dev/posts/windows-coding-agent-telemetry/) ⭐️ 7.0/10

Windows 11 reportedly collects telemetry on which coding agents and developer tools users run, according to a developer analysis shared on Hacker News. The collection has prompted privacy concerns among developers, particularly because these tools may be used to build or test sensitive code. The report does not specify an opt-out mechanism for this specific telemetry, but related discussions note that GPU drivers and browsers may collect similar executable names and paths unless users opt out. Microsoft has not confirmed the details in the supplied item, and no source content was available for verification.

hackernews · cwaffles · Nov 16, 22:58 · [Discussion](https://news.ycombinator.com/item?id=50524736)

**「Background」** Windows 10 and 11 include built-in telemetry that can report system and usage data, and users have employed tools such as WindowsTelemetryBlocker or the Windows Toolbox to disable telemetry and related services. Developer tools like Visual Studio Code also have configurable telemetry levels that enterprises can manage centrally. These existing controls provide context for understanding why newly reported collection of coding agent and developer tool usage on Windows has raised privacy concerns.

**「Impact」** Developers running coding agents or developer tools on Windows 11 may have their tool usage transmitted to Microsoft, potentially exposing their workflow and toolchain details without clear consent. The absence of an explicit opt-out could make this a privacy risk for sensitive development environments.

**「Community Discussion」** Commenters note that Intel, AMD, and NVIDIA drivers as well as Chrome may collect similar executable names or browsing data unless opted out, framing Windows telemetry as part of broader data collection. Others discuss switching to Linux as viable for gaming and daily use, while one commenter highlights Windows&\#x27; new MXC sandbox \(launched Oct 7\) lacks Claude Code support and suggests telemetry could help prioritize sandboxing features.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=-E-WC_UvHXE">Windows 11 : Kill Telemetry , Widgets &amp; Bloat - YouTube</a></li>
<li><a href="https://code.visualstudio.com/docs/enterprise/telemetry">Manage telemetry in enterprise environments</a></li>
<li><a href="https://github.com/N0tHorizon/WindowsTelemetryBlocker">N0tHorizon/WindowsTelemetryBlocker: A PowerShell based tool to...</a></li>

</ul>
</details>

**Tags**: `#Windows`, `#telemetry`, `#privacy`, `#developer tools`, `#coding agents`

---

<a id="item-tech-news-8"></a>
### [JPMorgan Chase technical issue causes US online banking delays](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda) ⭐️ 7.0/10

A technical issue at JPMorgan Chase triggered online banking delays and card problems across multiple US banks, according to an Associated Press report. The incident affected services at institutions including Chase, Wells Fargo, and Truist, with users reporting inability to access online banking, card failures, and unresponsive or closed physical branches. The outage prompted broader discussion about the reliability of financial infrastructure, with commenters comparing it to a recent 12-hour Revolut outage tied to a Google Cloud issue. The cause of the JPMorgan Chase incident remained unspecified in the available material, though some community members speculated about database or regional cloud failures. Legacy mainframe environments and reduced QA investment were also cited as relevant context for such disruptions.

hackernews · samk3nny · Nov 16, 18:31 · [Discussion](https://news.ycombinator.com/item?id=50521045)

**「Background」** JPMorgan Chase is one of the largest U.S. banks, and many financial transactions between institutions rely on its payment and clearing systems. When a technical issue occurs at Chase, customers of other banks can experience delays or failures when trying to transact with Chase accounts, as reported during this incident. Chase stated that the problems were not caused by a cyberattack, and the issues appeared centered on Chase customers and interbank transactions with Chase.

**「Impact」** Affected customers could not reliably use online banking or cards during the outage, and some physical branch services were reported unresponsive or closed.

**「Community Discussion」** Commenters compared the incident to a 12-hour Revolut outage caused by a Google Cloud failure, speculated about database or regional infrastructure problems, and noted that legacy mainframe systems and cost-cutting in QA may heighten outage risk.

<details><summary>References</summary>
<ul>
<li><a href="https://chicago.suntimes.com/business/2026/11/16/a-technical-issue-at-jpmorgan-chase-triggers-online-banking-delays-across-major-us-banks">A technical issue at JPMorgan Chase triggers online banking ...</a></li>
<li><a href="https://www.ideastream.org/community/2026-11-16/technical-issue-at-jpmorgan-chase-triggers-online-banking-delays-across-major-us-banks">Technical issue at JPMorgan Chase triggers online banking ...</a></li>

</ul>
</details>

**Tags**: `#banking outage`, `#infrastructure reliability`, `#financial systems`, `#incident response`, `#mainframes`

---

<a id="item-tech-news-9"></a>
### [Microsoft blames monster email outage on software defect introduced in July fix](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

Microsoft has attributed a major email outage to a software defect introduced in a July fix, according to the report. The defect prevented the email infrastructure from handling normal load during recovery. The failure was linked to a testing environment that differed from high-end production systems, allowing a concurrency bug to go undetected. Specific outage scale, affected services, and remediation details were not available in the source item.

hackernews · Bender · Nov 16, 13:18 · [Discussion](https://news.ycombinator.com/item?id=50517321)

**「Context」** The outage occurred in November 2026, disrupting Microsoft 365 email services including Exchange and Outlook for over 16 hours and affecting businesses, airlines, and government agencies worldwide \(tool-1-1\). Microsoft subsequently traced the incident to a software defect introduced in a July fix, which caused a cascading failure that left more than 80% of its networking gateway servers unavailable \(tool-1-3\).

**「Impact」** The software defect introduced in the July fix caused a global Microsoft 365 outage from November 12 to 14, 2026, disrupting Exchange Online, Outlook, Teams, SharePoint Online, and OneDrive for businesses and governments, with the worst disruption lasting about 16 hours and email delays continuing afterward.

**「Community Discussion」** Commenters compared the recovery challenge to power-grid black-start procedures, questioned whether temporary load shedding or connection limiting should have been used, and expressed surprise that Windows runs critical network infrastructure. Others discussed whether mismatched test and production environments are a common trade-off and pointed to additional coverage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/microsoft-says-months-old-bug-caused-global-microsoft-365-outage/">Microsoft says months-old bug caused global Microsoft 365 outage</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Microsoft_outage">2026 Microsoft outage - Wikipedia</a></li>
<li><a href="https://www.isitdown-now.com/en/blog/microsoft-365-outage-november-2026">Microsoft 365 outage of November 12–14, 2026: timeline, cause ...</a></li>

</ul>
</details>

**Tags**: `#microsoft`, `#email-outage`, `#software-defect`, `#cloud-reliability`, `#incident-analysis`

---

<a id="item-tech-news-10"></a>
### [Marimba: Efficient Calibrated Audio Question Answering with a Frozen ASR Encoder](https://www.reddit.com/r/MachineLearning/comments/1xxsqro/marimba_a_system_one_model_for_speech_r/) ⭐️ 7.0/10

Marimba introduces a system that uses a frozen Qwen3-ASR-0.6B encoder to answer typed yes/no, choice, and score questions about 8-second audio windows with calibrated probabilities, requiring only one encoder pass per window. For term queries it scores greedy and 4 beam ASR hypotheses zero-shot and then applies Platt calibration; language ID uses the model&\#x27;s language scores; turn-end, speaker-change, and speaker-count tasks use small readouts on frozen layers 18 and 12. On 1,000 public questions it matches or beats Qwen3-Omni \(30B-A3B\) on 6 of 9 tests, with 100% language ID on 300 FLEURS clips, speaker-change AUROC 0.966-0.980 on AMI and VoxConverse, and speaker count beating pyannote 3.1, but it loses turn-end AUROC 0.930 vs 0.982 on Smart Turn&\#x27;s own test and ties on ICSI. The turn-end readout was trained on Smart Turn data, so that result is in-distribution for Marimba only, and the system does not generalize to unseen tasks such as CochlScene scene classification, where every head is at chance.

reddit · r/MachineLearning · /u/solanotodesch · Nov 16, 15:47

**「Background」** Audio question answering often relies on large multimodal models or dedicated detectors. Marimba instead reuses the frozen encoder of Qwen3-ASR-0.6B, a compact automatic speech recognition model, along with its decoder hypotheses and internal layer activations. Qwen3-Omni \(30B-A3B\) is a much larger multimodal model used as the main comparison baseline.

**「Impact」** Developers can use Marimba&\#x27;s Apache-2.0 weights and API to get calibrated audio question answers from a 0.6B encoder with one pass per 8-second window, but the system does not generalize to unseen scene-classification tasks.

**Tags**: `#speech processing`, `#audio question answering`, `#efficient AI`, `#model evaluation`, `#zero-shot learning`

---

<a id="item-tech-news-11"></a>
### [U.S. and Nine Partners Sign San Francisco Declaration on AI Supply Chain](https://www.state.gov/releases/office-of-the-spokesman/2026/11/the-san-francisco-declaration-on-the-secure-foundations-of-enduring-prosperity/) ⭐️ 7.0/10

On November 15, 2026, the United States and nine partner countries—Australia, India, Israel, Japan, South Korea, Qatar, Singapore, UAE, and the UK—signed the San Francisco Declaration, affirming that economic security is the foundation of national security and pledging to jointly protect sensitive technologies and critical infrastructure supporting the superintelligence \(SI\) supply chain. The declaration establishes five working groups focused on innovation policy frameworks, SI applications in critical domains, full-stack SI supply chain collaboration, safe havens and supply chain security hubs, and SI security and resilience. The agreement reflects coordinated international policy action on superintelligence supply chain security among a broad group of allies and partners. The source does not include technical implementation details or binding enforcement mechanisms.

telegram · zaihuapd · Nov 16, 10:40

**「Background」** The San Francisco Declaration is an intergovernmental statement coordinated by the U.S. State Department and other signatory governments, using working groups rather than a treaty or enforcement body. It formalizes shared concern about protecting sensitive technologies and critical infrastructure that underpin advanced superintelligence systems.

**「Impact」** Signatory governments and companies in their jurisdictions may see future alignment of innovation, security, and supply chain policies for superintelligence-related technologies through the five working groups, although the declaration specifies no binding measures or deadlines.

**Tags**: `#AI policy`, `#supply chain security`, `#international cooperation`, `#superintelligence`, `#critical infrastructure`

---

<a id="item-tech-news-12"></a>
### [Amazon: AI Agents Steal API Keys to Fund Model Usage](https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/) ⭐️ 7.0/10

Amazon reports that attackers are using the open-source penetration testing framework Artex to drive AI agents that steal API keys from publicly exposed AI applications such as LiteLLM and Dify. The stolen keys are validated, pooled, and reused to pay for further large language model calls, effectively allowing the operation to self-fund. The campaign began on October 3 and was intercepted and blocked on November 5 by Amazon&\#x27;s MadPot honeypot network. Amazon attributes the activity with medium confidence to a China-linked threat group, notes that not all listed targets were compromised, and has notified potentially affected AWS customers.

telegram · zaihuapd · Nov 16, 13:00

**「Background」** ARTEX is an open-source framework for AI-driven penetration testing, and exposed AI orchestration tools such as LiteLLM, Dify, Langflow, and Ollama can leak API keys when left publicly accessible. Stolen keys can be validated and reused to cover the cost of further large language model calls, which is why pooled credentials create a self-funding abuse loop.

**「Impact」** Developers and organizations running publicly exposed AI applications such as LiteLLM and Dify should audit API keys and usage; Amazon has already notified potentially affected AWS customers.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/security/amazon-autonomous-cybercrime-artex-framework/">AI credential theft campaign used stolen API keys to scale</a></li>
<li><a href="https://www.2-spyware.com/amazon-artex-ai-agents-steal-ai-api-keys">Amazon: AI agents hunt exposed LiteLLM and Dify keys</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#API key theft`, `#autonomous agents`, `#threat intelligence`, `#cloud security`

---

<a id="item-tech-news-13"></a>
### [China&\#x27;s Top AI Firms Limit Offensive Cyber Capabilities in New Models](https://www.bloomberg.com/news/articles/2026-11-16/china-s-top-ai-firms-limit-cyber-capabilities-in-latest-models) ⭐️ 7.0/10

Alibaba, Tencent, Moonshot, and other leading Chinese AI companies have reduced offensive cyber capabilities in their new models while strengthening defensive performance. Alibaba&\#x27;s latest flagship Qwen model was released without open weights, preventing users from downloading and customizing the full version. The moves follow draft export-control rules from China&\#x27;s Ministry of Commerce, published last month, that would prohibit exporting AI tools capable of attacking critical infrastructure or government networks. Tencent also cut cyber-related functions before releasing its Hy4 model this month.

telegram · zaihuapd · Nov 17, 02:20

**「Context」** Open weights refers to publicly downloadable model parameters that allow users to run and modify a model locally, as opposed to API-only access; Alibaba has previously released Qwen models, such as Qwen 3.8-27B and Qwen 3.8-2.4T-A95B, under the permissive Apache 2.0 license. The item&\#x27;s mention of export-control draft rules refers to a proposal from China&\#x27;s Ministry of Commerce to ban exports of AI tools that could attack critical infrastructure or government networks.

**「Impact」** Developers and downstream users cannot download or customize the full version of Alibaba&\#x27;s latest flagship Qwen model because its weights are no longer open, and Tencent&\#x27;s Hy4 launched with offensive cyber capabilities removed, changes linked to draft export controls that would restrict AI tools capable of attacking critical infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/issue-18-record-control-until-someone-reads-tom-howard-maicd-sohsc">Issue 18: A record is not a control until someone reads it</a></li>
<li><a href="https://www.business-standard.com/technology/tech-news/china-ai-export-controls-open-weight-models-126101900723_1.html">How China&#x27;s proposed AI export controls could affect open ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#open source`, `#China`, `#cybersecurity`, `#technology policy`

---

<a id="item-tech-news-14"></a>
### [Xbox Confirms Project Helix Is a Console That Can Play PC Games](https://www.ign.com/articles/xbox-confirms-project-helix-is-a-console-capable-of-playing-games-from-your-pc) ⭐️ 7.0/10

Xbox confirmed in its 25th anniversary magazine published on November 15 that its next-generation plan, Project Helix, is &quot;designed to be a game console that can play PC games,&quot; rather than a PC that can play console games. Jason Ronald, vice president of next generation, described the goal as an &quot;ultimate console&quot; and said players would be able to directly access four generations of Xbox game libraries and progress. The confirmation is intended to eliminate the artificial boundary between console and PC gaming. No device form factor or release date has been announced, with external rumors pointing to the end of 2027 at the earliest.

telegram · zaihuapd · Nov 17, 02:40

**「Background」** Before this confirmation, Xbox had described Project Helix as an upcoming PC–console hybrid that would play both PC and console games, and recent reporting reiterated that it is a &\#x27;console capable of playing games from your PC&\#x27; rather than the reverse. The new statement by Xbox executive Jason Ronald positions Helix as a device that gives players direct access to four generations of Xbox game libraries and progress, with the stated goal of eliminating the artificial boundary between console and PC gaming.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gamespot.com/articles/xbox-project-helix-is-a-console-that-plays-pc-games-not-the-other-way-around/">Xbox Project Helix Is A Console That Plays PC Games ... - GameSpot</a></li>
<li><a href="https://www.techpowerup.com/354903/xbox-confirms-project-helix-is-not-a-pc-but-its-closer-than-ever">Xbox Confirms Project Helix Is Not a PC , But... | TechPowerUp</a></li>

</ul>
</details>

**Tags**: `#Xbox`, `#Project Helix`, `#PC gaming`, `#Microsoft`, `#hardware`

---

<a id="item-tech-news-15"></a>
### [Google to Offer Fairwind AI Models to Japan for Cyber Defense](https://cn.nikkei.com/industry/itelectric-appliance/64742-2026-11-17-09-16-25.html) ⭐️ 7.0/10

Google plans to extend its Fairwind early-access program to provide advanced AI models to the Japanese government and domestic critical infrastructure operators for cyber defense. Google Cloud CEO Thomas Kurian visited Japan on November 16 and conveyed the intention to senior Japanese government officials. The Fairwind program, launched in September, has so far primarily targeted U.S. government agencies and cybersecurity companies and had not been announced for Japanese government or enterprise users. The move responds to sharply increasing losses from cyberattacks in Japan, according to Nikkei. No technical specifications or implementation timeline were disclosed.

telegram · zaihuapd · Nov 17, 03:43

**「Fairwind Program Background」** The Fairwind Program is Google’s limited-access initiative, announced on September 2, 2026, that provides governments, healthcare providers, telecommunications companies, and other critical infrastructure operators with early access to Google’s latest AI models for cyber defense. It pairs Gemini for cyber models with CodeMender for defenders who pass strict governance checks. The program initially focused mainly on U.S. government agencies and cybersecurity companies.

**「Impact」** Japanese government and critical infrastructure operators could gain earlier access to Google&\#x27;s Fairwind cyber-defense AI models, though no technical details or timeline are confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://joho-todai.com/en/google-fairwind-ai-japan-cybersecurity/">Google to Give Japan&#x27;s Government and Critical Infrastructure ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/">Google’s Fairwind Program: Cyber defense tools for trusted ...</a></li>
<li><a href="https://explainx.ai/blog/google-fairwind-japan-gemini-cyber-early-access-2026">Google Fairwind Japan: Gemini Cyber Early Access | explainx ...</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#cybersecurity`, `#Google Cloud`, `#Japan`, `#critical infrastructure`

---

<a id="item-tech-news-16"></a>
### [Apple China App Store Requires AIGC Compliance Filing by January 31, 2027](https://www.ithome.com/1/028/158.htm) ⭐️ 7.0/10

Apple has added two mandatory compliance fields in App Store Connect for apps distributed in mainland China: an AIGC service declaration and filing information, plus a safety assessment certificate. Existing apps must complete these fields by January 31, 2027, while new apps must submit them immediately. The requirements apply to apps with AIGC features such as chatbots, image or video generation, and voice or face editing. Apps using third-party AIGC technology must also upload an authorization agreement and an algorithm filing number. Apple&\#x27;s 2026 App Review guidelines already include generative AI clauses.

telegram · zaihuapd · Nov 17, 04:29

**「Background」** China&\#x27;s generative AI regulations require public-facing AI services to complete algorithm filing and safety assessments. Apple is now surfacing these compliance obligations in App Store Connect specifically for mainland China distribution.

**「Impact」** Developers distributing AIGC-enabled apps on Apple&\#x27;s China App Store must submit the two compliance documents by January 31, 2027 for existing apps, or immediately for new apps, to meet the new distribution requirements.

**Tags**: `#Apple`, `#App Store`, `#AIGC compliance`, `#China regulations`, `#generative AI`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia CEO resigns amid scandal; ETF experts see AI trade shift toward Big Tech and AMD](https://www.cnbc.com/2026/11/14/nvidia-ai-trade-data-centers-congress.html) ⭐️ 8.0/10

Nvidia CEO Jensen Huang resigned amid a scandal after the stock posted its longest losing streak since 2012, while AMD rose about 13% for the week; ETF experts said Big Tech and alternative chip makers could benefit from investors seeking other chip sources and from potential Democratic congressional limits on data-center growth.

rss · CNBC Finance · Nov 16, 12:13

**「Background」** The resignation followed a week of growing scandal at Nvidia, and the Democratic gains of Nov. 3 gave the party control of Congress, raising the possibility of restrictions on planned data centers.

**Tags**: `#Nvidia`, `#AI trade`, `#ETFs`, `#data centers`, `#semiconductor stocks`

---

<a id="item-finance-news-2"></a>
### [U.S. crude oil falls to $85.39 a barrel on recovering Middle East exports](https://www.cnbc.com/2026/11/16/us-crude-oil-declines-to-87-a-barrel-on-recovering-middle-east-exports.html) ⭐️ 7.0/10

U.S. West Texas Intermediate crude fell 3.58% to settle at $85.39 a barrel Monday, while Brent crude fell 3.55% to $92.44 a barrel. The IEA expects a 1.7 million barrel-a-day global supply surplus in Q4 2026, reversing its earlier deficit forecast.

rss · CNBC Finance · Nov 16, 22:19

**「Background」** The IEA said Middle East exports are recovering faster than global demand, and Russia&\#x27;s October crude output rose by 210,000 barrels a day to 8.73 million barrels.

**Tags**: `#crude oil`, `#oil supply`, `#Middle East exports`, `#energy markets`, `#commodity prices`

---

<a id="item-finance-news-3"></a>
### [Intel and CEO Lip-Bu Tan face shareholder class action over Q4 forecast miss](https://www.investing.com/news/stock-market-news/intel-sued-by-shareholders-following-29-stock-plunge-5028171) ⭐️ 7.0/10

Intel and CEO Lip-Bu Tan are facing a shareholder class action alleging they concealed weak PC demand and inventory problems before a fourth-quarter forecast miss, after which the stock fell 28.6% and about $140 billion in market value was erased.

telegram · zaihuapd · Nov 16, 11:10

**「Background」** The lawsuit, led by a Michigan pension fund and filed in San Jose federal court, seeks to represent investors who bought Intel shares from July 23 to Oct. 29 and also names CFO David Zinsner as a defendant.

**Tags**: `#Intel`, `#shareholder lawsuit`, `#stock drop`, `#semiconductors`, `#earnings guidance`

---