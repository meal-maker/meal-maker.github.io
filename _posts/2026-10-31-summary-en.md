---
layout: default
title: "Horizon Summary: 2026-10-31 (EN)"
date: 2026-10-31
lang: en
---

> From 35 items, 14 important content pieces were selected

---

**Technology News**
1. [Azure&\#x27;s Weakest Link: Five Full Cross-Tenant Compromises](#item-tech-news-1) ⭐️ 9.0/10
2. [Backdoored Claude Code Extension on Cursor Marketplace Added SSH Key](#item-tech-news-2) ⭐️ 8.0/10
3. [The $6.3B Binance hack was pulled off in just 20 minutes](#item-tech-news-3) ⭐️ 8.0/10
4. [Northflank Reports Security Breach via Status Page](#item-tech-news-4) ⭐️ 7.0/10
5. [Show HN: A working Nintendo in ~1GB of Qwen weights](#item-tech-news-5) ⭐️ 7.0/10
6. [Tangled Launches Federated Code Forge on AT Protocol](#item-tech-news-6) ⭐️ 7.0/10
7. [AI Isn&\#x27;t Replacing SREs, It&\#x27;s Deskilling Them](#item-tech-news-7) ⭐️ 7.0/10
8. [Soft Multi-Token Prediction Claims Better MTP via KL Gradient Recovery](#item-tech-news-8) ⭐️ 7.0/10
9. [FCC to Vote on Banning Chinese Carriers from US Numbering Resources](#item-tech-news-9) ⭐️ 7.0/10
10. [Apple Intelligence Beta in China November 4, iOS 27.3 in December](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [SpaceX says Anthropic is its top AI customer, accounting for 34.5% of quarterly revenue](#item-finance-news-1) ⭐️ 8.0/10
2. [DeepSeek&\#x27;s second funding round reportedly raises 105.5 billion yuan](#item-finance-news-2) ⭐️ 8.0/10
3. [Four Japanese automakers’ China output falls below 40% of 2020 peak](#item-finance-news-3) ⭐️ 7.0/10
4. [US semiconductor stocks drop sharply; Intel falls over 26%](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Azure&\#x27;s Weakest Link: Five Full Cross-Tenant Compromises](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 9.0/10

A new security research report details five full cross-tenant compromise vulnerabilities in Microsoft Azure. The most critical finding is a forgeable admin consent callback in the login.microsoftonline.com/XXX/v2.0/adminconsent flow: an attacker who knows another Azure tenant&\#x27;s ID can forge the redirect target, despite Microsoft&\#x27;s documentation warning never to use that tenant ID for authentication or authorization. The research also describes cross-tenant data leaks, path traversal, and insecure direct object references \(IDOR\), with some flaws possibly present since the affected capabilities were first introduced. These vulnerabilities undermine Azure&\#x27;s multi-tenant isolation boundaries and pose serious risks to enterprise customers.

hackernews · swq115 · Oct 30, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50301854)

**「Azure Cross-Tenant Attack Context」** In Microsoft Azure, cross-tenant attacks occur when a flaw in multi-tenant services or API connections lets an attacker from one Azure Entra ID tenant access resources belonging to another tenant, including Key Vaults, Azure SQL databases, and externally linked services such as Jira or Salesforce. Recent research documents a vulnerability in Azure&\#x27;s default API Connection architecture that could allow full compromise of these resources. Microsoft&\#x27;s identity platform has since introduced shorter token lifetimes and Continuous Access Evaluation for supported apps, while red-team playbooks continue to focus on cross-tenant attacks through B2B collaboration and multi-tenant app exploitation.

**「Impact on Azure Customers」** Azure customers using affected capabilities face full cross-tenant compromise, including complete access to Key Vault secrets, certificates, and cryptographic keys, and compromise of connected services such as Slack, Salesforce, and Jira.

**「Community Discussion」** Commenters focus on the forgeable admin consent callback, with one urging Microsoft security to fix the flow because the documentation warning does not offer a usable authentication method for developers. Others note Azure&\#x27;s apparent lead in cross-tenant leaks, praise the researcher&\#x27;s work, and speculate that path traversal and IDOR issues have existed since those Azure capabilities were launched.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case">Azure &#x27;s Weakest Link - Five Full Cross - Tenant Compromises</a></li>
<li><a href="https://gbhackers.com/azure-default-api-connection-flaw/">Azure Default API Connection Flaw Enables Full Cross - Tenant ...</a></li>
<li><a href="https://hackerxone.com/azure-entra-id-red-team-techniques-2026-attack-playbook/">Azure Entra ID Red Team Techniques: 2026 Attack Playbook</a></li>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case">Azure &#x27;s Weakest Link - Five Full Cross - Tenant Compromises</a></li>
<li><a href="https://gbhackers.com/azure-default-api-connection-flaw/?trk=article-ssr-frontend-pulse_little-text-block">Azure Default API Connection Flaw Enables Full Cross - Tenant ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#azure`, `#cloud`, `#vulnerability`, `#cross-tenant`

---

<a id="item-tech-news-2"></a>
### [Backdoored Claude Code Extension on Cursor Marketplace Added SSH Key](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

A tampered copy of the Claude Code extension was published on Cursor&\#x27;s marketplace and was live from about 2:27 a.m. PT to 1:35 p.m. PT on Thursday, according to Cursor. The malicious extension appended an attacker&\#x27;s SSH public key labeled svc-telemetry to users&\#x27; authorized\_keys, potentially granting remote access. Anthropic confirmed the tampered version was not built or published by Anthropic and that its official channels and systems were not compromised; only Cursor users who installed the malicious marketplace copy are affected. Users can check for the key by searching for svc-telemetry in their SSH authorized\_keys file.

hackernews · \_chall · Oct 30, 07:09 · [Discussion](https://news.ycombinator.com/item?id=50300683)

**「Open VSX and the Cursor Marketplace」** VS Code extensions can be distributed through multiple registries, including Microsoft&\#x27;s Visual Studio Marketplace and the open-source Open VSX registry. Cursor&\#x27;s extension marketplace mirrors Open VSX, so extensions published there become available to Cursor users without being built or published by the original vendor. Anthropic&\#x27;s Claude Code extension \(identifier anthropic.claude-code\) is a popular tool, and the affected versions were 2.1.312 and 2.1.313 for Windows and macOS, according to Cursor&\#x27;s security notice.

**「Impact」** Cursor users who installed the backdoored extension should immediately remove any svc-telemetry entry from their SSH authorized\_keys file, because it grants the attacker remote access.

**「Community Discussion」** Commenters circulated the grep-based detection command and debated whether the Open VSX/Cursor marketplace distribution might also have affected the official Microsoft extension registry; one commenter initially believed the official marketplace build was clean but later expressed uncertainty after reading the write-ups.

<details><summary>References</summary>
<ul>
<li><a href="https://cursor.com/blog/claude-code-extension-security-notice">Security notice — malicious version of Anthropic.claude-code ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/claude-code-extension-trojanized">Trojanized Claude Code Extension Delivered Persistent SSH ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain`, `#vscode`, `#claude-code`, `#cursor`

---

<a id="item-tech-news-3"></a>
### [The $6.3B Binance hack was pulled off in just 20 minutes](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/) ⭐️ 8.0/10

Wired reported that a $6.3 billion hack of cryptocurrency exchange Binance was executed in just 20 minutes. The incident highlights critical security and regulatory concerns for cryptocurrency exchanges. The short execution window underscores how quickly such large-scale thefts can be completed.

hackernews · domhudson · Oct 30, 12:50 · [Discussion](https://news.ycombinator.com/item?id=50303172)

**「Background」** Binance is the world&\#x27;s largest cryptocurrency exchange. On a recent date, it suffered a cyberattack that drained an estimated $6.3 billion in digital assets across 10 blockchains in 20 minutes, making it the largest cryptocurrency theft to date. Attackers exploited EIP-7702, approximately $3 billion was frozen, and one analysis attributed the incident to North Korean hackers.

**「Community Discussion」** Commenters questioned how a compromised laptop could enable a $6 billion loss in minutes and whether Binance should face negligence or regulatory scrutiny. Others noted that fast execution is typical after lengthy preparation, with one speculating about a possible link to a Claude Code supply-chain attack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/">The $ 6 . 3 Billion Binance Hack Was Pulled Off in Just 20 ... | WIRED</a></li>
<li><a href="https://www.cryptotimes.io/insights/binance-hack-explained/">Binance Hack Explained: How $ 6 . 3 Billion Was Drained in 20 Minutes</a></li>
<li><a href="https://www.youtube.com/watch?v=3tmPCylnuKE">How crypto hackers drained Binance of $ 6 . 3 billion in 20 minutes</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#cryptocurrency`, `#exchange-hack`, `#financial-security`, `#incident-response`

---

<a id="item-tech-news-4"></a>
### [Northflank Reports Security Breach via Status Page](https://status.northflank.com/) ⭐️ 7.0/10

Northflank, a cloud platform provider, has reported a security breach on its status page. The company has not yet published technical details about the attack vector, scope, or whether customer data was compromised. The incident follows a series of recent breaches at other multi-tenant SaaS and infrastructure providers, including PingCAP/TiDB, Fireworks AI, Zeabur, OpenCode Console, and Railway. Northflank customers should monitor the status page for official updates and review their own security configurations, as limited information is currently available.

hackernews · js4ever · Oct 30, 15:10 · [Discussion](https://news.ycombinator.com/item?id=50305025)

**「Background」** Northflank is a cloud platform provider for deploying and managing applications, databases, and background jobs. The linked source points to its status page as the location of a security breach notification, though no details are provided in the available content. At the time of these checks, Northflank&\#x27;s status page showed all systems operational, and a separate company security page stated no security breach since the company&\#x27;s formation in April 2019, so the notice may have been transient or removed.

**「Community Discussion」** Commenters note a wave of attacks against multi-tenant vendors since September and debate whether such incidents will shift enterprises back to major hyperscalers. Some suggest mitigations like encrypting environment variables, while others stress that security fundamentals are becoming harder to maintain.

<details><summary>References</summary>
<ul>
<li><a href="https://northflank.com/security">northflank .com/ security</a></li>
<li><a href="https://northflank.instatus.com/default">Northflank - Status</a></li>

</ul>
</details>

**Tags**: `#security`, `#incident`, `#cloud`, `#SaaS`, `#infrastructure`

---

<a id="item-tech-news-5"></a>
### [Show HN: A working Nintendo in ~1GB of Qwen weights](https://github.com/dbreunig/nesformer) ⭐️ 7.0/10

A Show HN project presents nesformer, an approach that emulates a Nintendo Entertainment System using approximately 1GB of Qwen transformer weights. The model simulates both the CPU and RAM, using a gated deltanet architecture to hold state inside the model, and runs 150–290× slower than the real console. The proof-of-concept demonstrates that LLM-style weights can act as a reconfigurable computing substrate, though with significant efficiency overhead. It was built with assistance from Opus 5.5, which generated the weights and code from two prompts.

hackernews · dbreunig · Oct 30, 16:40 · [Discussion](https://news.ycombinator.com/item?id=50306442)

**「NES, Qwen weights, and computed-only emulation」** The NES is built around a 6502 CPU and dedicated RAM, and is typically emulated with deterministic software or implemented on reconfigurable FPGA hardware. Qwen is a transformer language model whose weights are normally learned through training; in this project, a compiler instead calculates the weights directly so that the model executes 6502 instructions, with a gated deltanet architecture representing the NES RAM inside the model.

**「Impact」** The project demonstrates that LLM-style weights can emulate deterministic hardware, but the 150–290× slowdown makes it impractical for real-time or general-purpose emulation.

**「Community Discussion」** Commenters appreciated the technical novelty—especially emulating RAM via gated deltanet—but expressed horror at the inefficiency, noting the multi-million-fold compute difference versus ordinary programs, while some envisioned compiling VMs or tools directly into LLM weights.

<details><summary>References</summary>
<ul>
<li><a href="https://dzen.ru/b/auTxnHpCwlRQnR2n">Процессор NES собрали в весах Qwen 3.5 без обучения nesformer ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#emulation`, `#Qwen`, `#hardware-emulation`, `#novel-computing`

---

<a id="item-tech-news-6"></a>
### [Tangled Launches Federated Code Forge on AT Protocol](https://tangled.org/blog/forge/) ⭐️ 7.0/10

Tangled has launched a federated, self-hostable code forge built on the AT Protocol. The project announced stabilized AT Protocol lexicons, a completely overhauled architecture and UI, support for organizations, and private repositories expected within the following couple of weeks. The launch is notable for decentralized code collaboration because it enables self-hosting of the entire stack or individual components and offers an alternative to centralized platforms like GitHub and GitLab. A co-founder confirmed the details and said the team is happy to answer questions.

hackernews · zlliang · Oct 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=50305573)

**「Background」** AT Protocol is the decentralized social networking protocol originally developed for Bluesky, supporting portable identities and federated data. A code forge typically hosts source code repositories, issues, and pull requests; combining it with a federation protocol allows users to maintain their own instances while interoperating with others.

**「Impact」** Developers can now self-host Tangled and federate with other AT Protocol services, reducing dependence on centralized code hosts, though the platform is still nascent and private repositories are not yet available.

**「Community Discussion」** Community feedback is generally optimistic, with one Gitea user planning to migrate code and releases once suitable bridges exist and another asking about lexicon changes for interoperability with their own forge. Some commenters found the UI busy and suggested adopting familiar activity-chart styles, while the co-founder confirmed private repos are coming in the following weeks.

**Tags**: `#federated-code-forge`, `#at-protocol`, `#code-collaboration`, `#self-hosting`, `#decentralization`

---

<a id="item-tech-news-7"></a>
### [AI Isn&\#x27;t Replacing SREs, It&\#x27;s Deskilling Them](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 7.0/10

The article argues that AI tools in site reliability engineering deskill practitioners rather than replace them. It draws a parallel to aviation, where the FAA requires manual flying time despite capable autopilots, and suggests SRE teams could designate some AI-handleable incidents as human-practice opportunities. Commenters add that earlier infrastructure-as-code tools like Terraform already deskilled SRE work without prompting manual-practice mandates, while others stress that SRE fundamentally depends on understanding data flows, bottlenecks, logs, and SLOs. One practitioner reports AI agents are now superhuman at computer use and can solve issues much faster with read-only access, reinforcing both the productivity gain and the deskilling concern.

hackernews · dorianniemiec · Oct 30, 15:52 · [Discussion](https://news.ycombinator.com/item?id=50305693)

**「Context: SRE and automation」** Site reliability engineering \(SRE\) treats operations as a software engineering problem, emphasizing reliability through service-level objectives, monitoring, and incident response. Automation has long been used to handle routine operational tasks, but the “irony of automation” describes how removing humans from routine loops can erode the very skills needed when automated systems fail or encounter novel situations. This article extends that concern to AI-driven incident response, arguing that over-reliance on AI for routine tasks can weaken problem-solving and hands-on expertise.

**「Impact」** SRE teams adopting AI automation risk losing the core diagnostic understanding needed for novel failures unless they deliberately reserve some incidents for human practice.

**「Community Discussion」** Commenters largely endorse the aviation analogy, but disagree on whether deskilling is harmful: some note that past automation like Terraform already deskilled SREs without harm, while others argue that SRE&\#x27;s value lies in the understanding that AI-generated or AI-resolved systems can erode.

<details><summary>References</summary>
<ul>
<li><a href="https://signoz.io/blog/ai-isnt-replacing-sres-its-deskilling-them/">AI Isn &#x27; t Replacing SREs . It &#x27; s Deskilling Them . | SigNoz</a></li>
<li><a href="https://iliareingold.com/newsletter/190">Daily curated AI &amp; tech stories.</a></li>

</ul>
</details>

**Tags**: `#SRE`, `#AI`, `#automation`, `#site reliability engineering`, `#deskilling`

---

<a id="item-tech-news-8"></a>
### [Soft Multi-Token Prediction Claims Better MTP via KL Gradient Recovery](https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/) ⭐️ 7.0/10

A research paper introduces Soft Multi-Token Prediction \(Soft-MTP\), claiming a simple modification that recovers a KL self-distillation signal and improves multi-token prediction across tasks. The authors argue that the standard MTP gradient hides a KL self-distillation signal behind a noisy residual that harms next-token prediction. The proposed KL gradient-recovery trick is described as a one-line change to the next-token prediction hidden state: h\_ntp += h\_mtp.detach\(\) - h\_mtp. The work provides links to code on GitHub, an arXiv paper \(2610.38331\), and a Hugging Face collection, but the summary is author-provided and not independently verified.

reddit · r/MachineLearning · /u/jayden\_teoh\_ · Oct 30, 18:53

**「Background」** Multi-token prediction \(MTP\) trains language models to predict several future tokens at once and is used in frontier pre-training to improve downstream capabilities with no added training-time overhead, while also enabling speculative decoding where multiple draft tokens are generated per forward pass and then verified to preserve the model&\#x27;s output distribution. Standard MTP mixes a useful KL self-distillation signal with a noisy residual that can harm next-token prediction. The Soft-MTP approach is a one-line change that reuses the existing next-token and MTP cross-entropy computations to backpropagate only the KL self-distillation term.

**「Impact」** For LLM pre-training pipelines that use multi-token prediction, the paper reports that Soft-MTP&\#x27;s one-line change removes a harmful gradient residual and improves next-token and multi-token learning, perplexity, speculative decoding, and accuracy across scales with no extra overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2610.38331">Paper page - Multi - Token Prediction Done Right</a></li>
<li><a href="https://arxiv.org/abs/2610.00888">[2610.00888] Match the Distribution, Not the Compute: Post-Training...</a></li>
<li><a href="https://paperswithcode.co/paper/2404.19737">Better &amp; Faster Large Language Models via Multi - token Prediction ...</a></li>
<li><a href="https://arxiv.org/pdf/2610.38331">Multi-Token Prediction Done Right - arXiv.org</a></li>
<li><a href="https://www.goodpapers.org/paper/arxiv-2610.38331">Multi-Token Prediction Done Right (Highly rated) | Good Papers</a></li>

</ul>
</details>

**Tags**: `#multi-token prediction`, `#speculative decoding`, `#language models`, `#self-distillation`, `#training optimization`

---

<a id="item-tech-news-9"></a>
### [FCC to Vote on Banning Chinese Carriers from US Numbering Resources](https://fccid.io/news/fcc-draft-national-security-voip-direct-access-numbering-rules) ⭐️ 7.0/10

The U.S. Federal Communications Commission said on October 29 that it will vote on November 19 on a proposal to prohibit China Mobile, China Telecom, China Unicom, and related VoIP providers from directly obtaining U.S. phone number resources, citing national security and fraud/robocall prevention. The proposal only targets direct access to U.S. numbering resources and does not affect existing ordinary international calling. A separate proposed measure would also bar service providers using Huawei or ZTE equipment on the risk list from directly obtaining U.S. phone numbers. The U.S. entities of the three Chinese carriers have previously been denied or had revoked their U.S. international telecom service authorizations.

telegram · zaihuapd · Oct 30, 08:01

**「Background」** The FCC oversees U.S. numbering resources, which carriers must use to route calls and assign phone numbers. Direct access lets a provider obtain numbers for use in the United States; international calls can still be completed through other arrangements. National security reviews have previously restricted Chinese telecom operators and equipment vendors.

**「Impact」** If adopted, China Mobile, China Telecom, China Unicom, related VoIP providers, and any service provider using Huawei or ZTE equipment on the covered list would lose direct access to U.S. phone number resources, while ordinary international calls made and received today would remain unaffected.

**Tags**: `#FCC`, `#telecom`, `#China`, `#national security`, `#VoIP`

---

<a id="item-tech-news-10"></a>
### [Apple Intelligence Beta in China November 4, iOS 27.3 in December](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) ⭐️ 7.0/10

Apple announced that its first Apple Intelligence features for China—live translation, a photo cleanup tool, and Writing Tools—will be available in the latest iOS developer beta starting November 4, with a public release to Chinese users in the iOS 27.3 update in December. The rollout is limited to supported iPhones purchased in China or devices whose region and Apple Account country/region are set to China, and support for other platforms will follow after necessary approvals. This initial release does not include the next-generation Siri AI features. Apple has partnered with Alibaba to integrate Qwen models into Siri, Writing Tools, and Visual Intelligence for eligible users in China.

telegram · zaihuapd · Oct 30, 21:44

**「Background」** Apple Intelligence is Apple&\#x27;s suite of AI features that includes writing tools, photo editing, and translation. In China, the rollout requires a local AI partner and regulatory approval, so Apple uses Alibaba&\#x27;s Qwen models for Siri, Writing Tools, and Visual Intelligence instead of its own models.

**「Impact」** Chinese users with supported iPhones and Apple accounts set to China will gain Apple Intelligence features—including real-time translation, photo cleanup, and Writing Tools—starting with the November 4 iOS developer beta and the December iOS 27.3 release, but they will not receive the next-generation Siri AI features and the features run on Alibaba&\#x27;s Qwen models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iclarified.com/103212/apple-intelligence-coming-to-china-in-december-with-ios-273">Apple Intelligence Coming to China in December With iOS 27.3</a></li>
<li><a href="https://thenextweb.com/news/apple-intelligence-china-ios-27-3-alibaba-qwen">Apple confirms its AI features reach China in December, with Qwen</a></li>

</ul>
</details>

**Tags**: `#Apple Intelligence`, `#China`, `#Alibaba Qwen`, `#iOS`, `#AI features`

---

## Financial News

<a id="item-finance-news-1"></a>
### [SpaceX says Anthropic is its top AI customer, accounting for 34.5% of quarterly revenue](https://www.cls.cn/detail/2519914) ⭐️ 8.0/10

SpaceX disclosed that a single AI customer accounted for 34.5% of quarterly revenue, and people familiar with the filing said the customer, identified as “Customer B,” is Anthropic. Anthropic’s IPO filing shows it agreed to pay up to $120.5 billion for SpaceX computing capacity through 2029, equivalent to about $3.1 billion a month starting in December.

telegram · zaihuapd · Oct 30, 06:20

**「Background」** SpaceX’s AI division, now called Super Intelligence, provides computing services from a data center in Memphis, Tennessee.

**Tags**: `#SpaceX`, `#Anthropic`, `#AI infrastructure`, `#revenue concentration`, `#cloud computing`

---

<a id="item-finance-news-2"></a>
### [DeepSeek&\#x27;s second funding round reportedly raises 105.5 billion yuan](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) ⭐️ 8.0/10

The Information reports that DeepSeek&\#x27;s second funding round raised 105.5 billion yuan at a valuation of over 615.5 billion yuan, with nearly 30 investors including Tencent, CATL, and state-affiliated backers.

telegram · zaihuapd · Oct 30, 12:37

**「Background」** DeepSeek&\#x27;s first funding round, completed in June 2026, raised about 51 billion yuan, with only 2% from state-affiliated investors, according to The Information.

**Tags**: `#DeepSeek`, `#funding`, `#AI`, `#China`, `#venture capital`

---

<a id="item-finance-news-3"></a>
### [Four Japanese automakers’ China output falls below 40% of 2020 peak](https://weibo.com/1642634100/Rp6qUwLKa) ⭐️ 7.0/10

Sina Tech reported that in April–September 2026, Toyota, Honda, Nissan, and Mazda produced a combined 1.02 million vehicles in China, down 32% year on year and under 40% of their 2020 peak; Honda said it would cut its China fuel-vehicle annual capacity from 1.49 million to 1 million.

telegram · zaihuapd · Oct 30, 13:38

**「Background」** The four Japanese automakers previously used China as a major production base, and their combined output in the April–September period peaked in 2020, making that year the comparison baseline for the reported decline.

**Tags**: `#Japanese automakers`, `#China auto market`, `#Honda`, `#production decline`, `#capacity reduction`

---

<a id="item-finance-news-4"></a>
### [US semiconductor stocks drop sharply; Intel falls over 26%](https://www.cls.cn/detail/2521210) ⭐️ 7.0/10

On October 30, US semiconductor stocks fell sharply, with the Philadelphia semiconductor index down 5.67% and Intel dropping more than 26%.

telegram · zaihuapd · Oct 30, 13:48

**「Background」** The sell-off followed disappointing quarterly results from Amazon and Alphabet and a weak outlook from Intel, which renewed concerns that the artificial-intelligence rally had pushed tech valuations too high.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-october-30-dow-sp-500-nasdaq-amazon-intel-ai-sell-off-191429143.html">Stock market today: Nasdaq, Dow, S&amp;P 500 clobbered as October ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-10-29/stock-market-today-dow-s-p-live-updates">Stock Market Today: Dow, S&amp;P Live Updates for October 30 , 2026</a></li>

</ul>
</details>

**Tags**: `#semiconductor stocks`, `#market selloff`, `#Intel`, `#AMD`, `#Philadelphia semiconductor index`

---