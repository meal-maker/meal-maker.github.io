---
layout: default
title: "Horizon Summary: 2026-11-09 (EN)"
date: 2026-11-09
lang: en
---

> From 30 items, 5 important content pieces were selected

---

**Technology News**
1. [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](#item-tech-news-1) ⭐️ 7.0/10
2. [Outlook.com Reportedly Rejecting Email from Domains Without DMARC](#item-tech-news-2) ⭐️ 7.0/10
3. [Goldman Sachs Pulls Claude Code from Bankers and Traders](#item-tech-news-3) ⭐️ 7.0/10
4. [Drex Max v1.1 Claims State-of-the-Art Multimodal Decision Model](#item-tech-news-4) ⭐️ 7.0/10
5. [Apple may make Siri more agentic as early as 2027](#item-tech-news-5) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [KetchUp – Open-source SketchUp alternative built with Rust and WebGPU](https://ketchup3d.github.io/app/) ⭐️ 7.0/10

KetchUp is a new open-source browser-based 3D modeling tool that provides a SketchUp-like experience and is built with Rust and WebGPU. It runs directly in the browser at ketchup3d.github.io/app and aims to fill the gap left by SketchUp&\#x27;s increasing commercial restrictions. The project has attracted positive community interest and demonstrates the viability of Rust for cross-platform web and mobile application interfaces.

hackernews · dcoulmbe · Nov 8, 22:35 · [Discussion](https://news.ycombinator.com/item?id=50418176)

**「Background」** SketchUp is a popular 3D modeling tool known for its intuitive push/pull interface; after Google sold it to Trimble, its free version became increasingly restricted, motivating open-source alternatives. KetchUp is a free, open-source SketchUp alternative built with Rust, WebAssembly, and WebGPU, running in the browser or on desktop and aimed especially at woodworking and furniture design. It requires no account, can import existing SketchUp .skp geometry, and exports models as Wavefront OBJ files.

**「Impact」** Users seeking a free SketchUp-style modeler can use KetchUp directly in the browser without installing desktop software.

**「Community Discussion」** Commenters largely welcome KetchUp as a spiritual successor to SketchUp and praise its browser UI and text rendering, but one user notes that trackpad navigation is currently unsupported and another suggests adding feature showcases to the landing page.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Ketchup3D/app">GitHub - Ketchup3D/app: Free, open-source 3D modeling ...</a></li>
<li><a href="https://daily.dev/posts/ketchup-open-source-sketchup-alternative-built-with-rust-and-webgpu-lquqfnjed">KetchUp – Open-source SketchUp alternative built with Rust ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#rust`, `#webgpu`, `#3d-modeling`, `#sketchup-alternative`

---

<a id="item-tech-news-2"></a>
### [Outlook.com Reportedly Rejecting Email from Domains Without DMARC](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 7.0/10

A Mailroute blog post reports that Outlook.com has begun rejecting email from domains lacking DMARC, a significant deliverability change for senders. Community comments describe both silent non-delivery and explicit 5xx permanent failures, with one commenter recalling similar Gmail enforcement in 2024. The change is seen as overdue by some and as consistent with existing pressure on mail server operators, though others highlight long-standing Outlook.com filtering issues unrelated to DMARC.

hackernews · xmddmx · Nov 8, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50416158)

**「Background」** DMARC \(Domain-based Message Authentication, Reporting, and Conformance\) is an email authentication protocol that builds on SPF and DKIM, enabling domain owners to publish a policy for how receiving mail servers should treat messages that fail authentication. Major mailbox providers have increasingly pushed for DMARC adoption to reduce spoofing and phishing, with some already requiring it for high-volume senders. According to MailRoute, Outlook.com and Hotmail began bouncing mail from domains without any DMARC record on November 5, and the fix is a single DMARC DNS TXT record when SPF or DKIM aligns with the From domain.

**「Impact」** Email sent to Outlook.com addresses from domains without DMARC may be rejected or silently dropped, requiring senders to implement DMARC to ensure delivery. Reports include both silent drops and 5xx failures, so exact behavior may vary.

**「Community Discussion」** Commenters generally agree that requiring DMARC is reasonable, but they disagree on whether the rejection is silent: one reports silent drops, another says Outlook sends 5xx permanent failures. Some also note Outlook.com has long filtered legitimate mail based on non-public blocklists.

<details><summary>References</summary>
<ul>
<li><a href="https://mailroute.net/blog/outlook-rejecting-email-without-dmarc">Outlook.com Is Quietly Rejecting Email From Domains Without DMARC</a></li>
<li><a href="https://news.lavx.hu/article/outlook-com-rejects-some-email-from-domains-without-dmarc-records">Outlook.com Rejects Some Email From Domains Without DMARC ...</a></li>

</ul>
</details>

**Tags**: `#email`, `#DMARC`, `#Outlook.com`, `#Microsoft`, `#deliverability`

---

<a id="item-tech-news-3"></a>
### [Goldman Sachs Pulls Claude Code from Bankers and Traders](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

Goldman Sachs is removing access to Claude Code for its bankers, traders, and other non-engineering staff. The reported reasons include security, compliance, and billing challenges associated with letting non-engineers run a coding agent on finance workstations. The restriction follows concerns that semi-autonomous coding tools on machines with access to client, trade, and internal data pose unacceptable governance risks. Billing overages and the lack of normalized consumption pricing are also cited as factors undermining the rollout. The change highlights enterprise governance hurdles for AI coding agents in regulated financial institutions.

hackernews · TheWiggles · Nov 8, 18:16 · [Discussion](https://news.ycombinator.com/item?id=50415628)

**「Background」** Claude Code is Anthropic&\#x27;s interactive coding agent, and Goldman Sachs had previously allowed bankers and traders to use it alongside Microsoft GitHub for tasks like tracking client flows and building market models. The firm also partnered with Anthropic to deploy Claude AI agents for trade accounting and client due diligence. Financial institutions operate under strict regulatory, data privacy, and auditability requirements, so expanding coding agents beyond engineering can create conflicts between experimentation and controlled production use.

**「Impact」** Bankers and traders at Goldman Sachs can no longer rely on Claude Code for coding-related tasks until the firm addresses the cited security, compliance, and billing controls.

**「Community Discussion」** Commenters attribute the pullback to the danger of running semi-autonomous coding agents on machines with client, trade, email, and internal network access, and to consumption-billing overages; one notes that Gemini is gaining ground by offering flat, throttled billing. Others cite regulatory accuracy failures that led a finance team to be dismissed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers">Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders</a></li>
<li><a href="https://www.finalroundai.com/blog/goldman-sachs-claude-ai-agents">Goldman Sachs Deploys AI Agents for Accounting and Compliance...</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#enterprise security`, `#fintech`, `#AI governance`, `#Claude Code`

---

<a id="item-tech-news-4"></a>
### [Drex Max v1.1 Claims State-of-the-Art Multimodal Decision Model](https://www.reddit.com/r/MachineLearning/comments/1xr4hkm/artificial_analysis_multimodal_decision_model/) ⭐️ 7.0/10

A Reddit post by Nace&\#x27;s Alti announces Drex Max v1.1, claiming state-of-the-art and Pareto frontier performance for multimodal decision models. The post states the model has a roughly 256k context window, can run locally on Macs through the Kapitsa inference engine, and is 8x cheaper than the next best model in the Artificial Analysis index. Drex Max v1 weights are available on Hugging Face under an Open RAIL-M license, v1.1 weights are promised soon after local inference optimization, and a training paper titled &\#x27;Towards Foundation Decision Models: Drex&\#x27; is linked. The announcement is self-promotional and lacks independent verification or detailed benchmark metrics.

reddit · r/MachineLearning · /u/m4rkGS · Nov 8, 17:54

**「Background」** Drex Max is a multimodal decision model from Nace.AI that takes a state \(text, JSON, or images\) plus named questions and returns a probability for each option in a single forward pass. The Artificial Analysis Decision Index compares such models on accuracy and calibration, with each benchmark weighted equally. Nace.AI previously released Drex Max v1 weights under an Open RAIL-M license and described training in the paper &\#x27;Towards Foundation Decision Models: Drex.&\#x27;

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index">Artificial Analysis Decision Index | Artificial Analysis</a></li>
<li><a href="https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/">Nace AI Open-Sources Drex Max v 1 : A 27B Decision Model That...</a></li>
<li><a href="https://huggingface.co/nace-ai/drex-max-v1">nace-ai/ drex - max - v 1 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#decision-models`, `#open-source`, `#benchmarks`, `#AI`

---

<a id="item-tech-news-5"></a>
### [Apple may make Siri more agentic as early as 2027](https://9to5mac.com/2026/11/08/apple-working-on-agentic-siri-ai-next-year-report/) ⭐️ 7.0/10

Apple is reportedly planning to make Siri more agentic as early as 2027, according to Bloomberg&\#x27;s Mark Gurman in Power On. Siri already gained personalization in iOS 27 but still lacks the ability to proactively act on a user&\#x27;s behalf. To support this shift, Apple is changing its internal development process for iOS 28&\#x27;s first cycle from the usual four weeks of coding plus four weeks of integration to six weeks of coding exploration plus two weeks of convergence, giving engineers more time for innovation.

telegram · zaihuapd · Nov 8, 16:36

**「Context」** According to Bloomberg&\#x27;s Mark Gurman, Apple&\#x27;s current Siri was rebuilt in iOS 27 and gained personalization, but it remains primarily responsive rather than proactive. To allow more time for innovative agentic features, Apple is changing its iOS 28 development schedule from a standard four-week coding and four-week integration cycle to six weeks of exploration and two weeks of convergence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/11/08/apple-tweaks-ios-28-development-process/">Apple Taking New Approach to Developing iOS 28 and... - MacRumors</a></li>
<li><a href="https://9to5mac.com/2026/05/12/ios-27s-completely-rebuilt-siri-will-include-a-new-system-wide-search-gesture-report/">iOS 27’s ‘completely rebuilt’ Siri will include a new... - 9to5Mac</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Siri`, `#agentic AI`, `#iOS`, `#tech industry`

---