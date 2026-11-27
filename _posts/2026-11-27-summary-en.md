---
layout: default
title: "Horizon Summary: 2026-11-27 (EN)"
date: 2026-11-27
lang: en
---

> From 36 items, 12 important content pieces were selected

---

**Technology News**
1. [Zhipu and Moonshot AI Flagship Model Releases Delayed by Compute and Anti-Distillation Limits](#item-tech-news-1) ⭐️ 8.0/10
2. [AI made self-hosting fun again](#item-tech-news-2) ⭐️ 7.0/10
3. [AMD gfx906 llama.cpp fork delivers fast cheap LLM inference](#item-tech-news-3) ⭐️ 7.0/10
4. [CTO of RansomwareHelp Indicted for Wire Fraud](#item-tech-news-4) ⭐️ 7.0/10
5. [Google&\#x27;s Workspace MCP: Gmail Cannot Send Email](#item-tech-news-5) ⭐️ 7.0/10
6. [SQLite sqlite3\_rsync Copies Databases Without Duplicate Disk Space](#item-tech-news-6) ⭐️ 7.0/10
7. [Neuralink Gets FDA Approval for ALS Brain-Implant Trial](#item-tech-news-7) ⭐️ 7.0/10
8. [ASML CEO: Full China Chip Ban Would Push China to Build Its Own](#item-tech-news-8) ⭐️ 7.0/10
9. [Cloudflare Dashboard and API Outage Reported](#item-tech-news-9) ⭐️ 7.0/10
10. [Microsoft CEO: New Grad Hiring Slows as AI Budgets Take Priority](#item-tech-news-10) ⭐️ 7.0/10

**Financial News**
1. [Nvidia halts AI server shipments to four Southeast Asian countries](#item-finance-news-1) ⭐️ 9.0/10
2. [Netherlands rejects proposed US curbs on ASML China sales](#item-finance-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Zhipu and Moonshot AI Flagship Model Releases Delayed by Compute and Anti-Distillation Limits](https://www.reuters.com/world/china/us-chip-curbs-distillation-crackdown-threaten-chinese-ai-model-development-2026-11-26/) ⭐️ 8.0/10

Chinese AI developers Zhipu and Moonshot AI face delays to flagship model releases attributed to US export controls and more effective anti-distillation protections from US labs, according to a Reuters report. Zhipu&\#x27;s GLM-5.5, a roughly 3-trillion-parameter model originally planned for this month, may not arrive until Q1 2027 or later, while Moonshot AI&\#x27;s next flagship Kimi K4 could be pushed to mid-2027. Moonshot also estimates that if overseas compute is fully lost, its major release interval could stretch from six months to more than a year, and the company has reportedly turned to distilling Google and Meta models because Anthropic and OpenAI protections have made training data harder to obtain. Zhipu denies the report, according to a circulating WeChat Moments screenshot.

telegram · zaihuapd · Nov 26, 15:14

**「Background」** Large language model training depends heavily on advanced accelerators such as NVIDIA GPUs, which are subject to US export controls affecting Chinese firms. Distillation is a technique where a newer or smaller model is trained on outputs from a stronger model, and major US labs have added technical barriers to prevent unauthorized extraction of their models&\#x27; behavior.

**「Impact」** If the reported delays materialize, developers and enterprises relying on Zhipu and Moonshot flagship models would wait longer for next-generation capabilities, and Moonshot&\#x27;s internal estimate suggests its major release cadence could slow to more than a year without overseas compute.

**Tags**: `#AI`, `#large language models`, `#compute restrictions`, `#China tech`, `#anti-distillation`

---

<a id="item-tech-news-2"></a>
### [AI made self-hosting fun again](https://janlukas.blog/posts/ai-self-hosting) ⭐️ 7.0/10

The post argues that AI tools have made self-hosting more accessible by simplifying deployment and automation, while also introducing new security and maintenance challenges. HN commenters illustrate this shift, with one running a platform on k3s where an AI agent can deploy services behind Tailscale, and another using Claude Code to manage a 60-service setup with automated backups and API integrations for Backblaze, UniFi, and Cloudflare. A commenter notes that while agents can spin up a VPS or Cloudflare proxy end-to-end, operators now face the burden of patching critical CVEs within 24 hours as exposure accelerates. Some users are adopting more declarative infrastructure, such as a custom Debian-based bootc image or Ansible, to keep pace with rapid changes.

hackernews · jlelse · Nov 26, 21:47 · [Discussion](https://news.ycombinator.com/item?id=50660180)

**「Background」** Self-hosting refers to running applications on one&\#x27;s own hardware or VPS instead of using managed cloud services. Traditionally, setting up and maintaining self-hosted services involved manual configuration for deployment, updates, and security, which could be time-consuming. Recent AI coding agents such as Claude Code \(CLI\) can automate much of this setup and management, reducing the startup effort for complex tools and frameworks, as noted in community discussions.

**「Impact」** Self-hosters who delegate deployment to AI agents must take on a heightened security responsibility, including patching critical CVEs within 24 hours, according to one commenter.

**「Community Discussion」** Commenters express enthusiasm for using AI agents to quickly deploy and manage many services, while others caution that easier deployment shifts the burden to continuous security patching and can encourage over-implementation without careful evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50660180">AI made self - hosting fun again | Hacker News</a></li>
<li><a href="https://blog.fnxexp.dev/tech-131/">Self - Hosting Made Easy: Fun CLI Agents for Home... - blog .fnxexp.dev</a></li>

</ul>
</details>

**Tags**: `#AI`, `#self-hosting`, `#DevOps`, `#LLM`, `#security`

---

<a id="item-tech-news-3"></a>
### [AMD gfx906 llama.cpp fork delivers fast cheap LLM inference](https://devnull.land/amd-specific-llama-cpp) ⭐️ 7.0/10

An AMD-specific fork of llama.cpp has emerged targeting gfx906 datacenter GPUs with HBM2 memory. These circa-2018 cards offer 32GB VRAM and roughly 1 TB/s memory bandwidth for around $200, making them attractive for local LLM inference despite lacking tensor cores and native bf16 support. Community reports describe optimizations such as the Radiance engine achieving 2400 tokens/s prefill and 150 tokens/s decode on a single card with a 4-bit Qwen3.8-27B model. Other users report porting Nvidia kernels to ROCm on an MI100 to double or triple Qwen3.8 performance. The fork addresses a niche high-bandwidth, low-compute hardware segment for local AI practitioners.

hackernews · julianlam · Nov 26, 17:11 · [Discussion](https://news.ycombinator.com/item?id=50657265)

**「Context on AMD gfx906 and llama.cpp」** The AMD GFX906 architecture \(used in MI50, MI60, and Radeon VII\) from 2018 has relatively weak compute but very high HBM2 memory bandwidth, making used 32GB cards available for around $200, far cheaper than modern equivalents. llama.cpp is a widely used open-source LLM inference engine, but official ROCm support for GFX906 has been limited to nightly builds rather than stable releases. In response, the community has developed forks such as llama.cpp-gfx906 and llama-cpp-rdna-boosts that optimize llama.cpp specifically for these cards to maximize inference throughput.

**「Impact」** Owners of low-cost AMD gfx906 GPUs \(MI50, MI60, Radeon VII\) can use this fork to run high-throughput local LLM inference on HBM2 cards, as shown by community benchmarks and the dedicated repository.

**「Community Discussion」** Commenters share concrete benchmarks: one reports 2400 tok/s prefill and 150 tok/s decode on a single gfx906-class card with Qwen3.8-27b; another tripled Qwen speed on M1 Max via a separate port; and another doubled or tripled Qwen3.8 performance on an MI100 by porting Nvidia kernels to ROCm. Practical experiences are positive but note the hardware lacks tensor cores and bf16 support.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50657265">AMD - specific fork of llama . cpp | Hacker News</a></li>
<li><a href="https://github.com/thickprogrammer/llama.cpp-gfx906">thickprogrammer/ llama . cpp - gfx 906 : llama . cpp optimized for AMD ...</a></li>
<li><a href="https://devnull.land/amd-specific-llama-cpp">AMD - specific fork of llama . cpp | devnull.land</a></li>
<li><a href="https://github.com/thickprogrammer/llama.cpp-gfx906">GitHub - thickprogrammer/ llama . cpp - gfx 906 : llama . cpp optimized for...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AMD GPU`, `#HBM2`, `#inference optimization`, `#open source`

---

<a id="item-tech-news-4"></a>
### [CTO of RansomwareHelp Indicted for Wire Fraud](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/) ⭐️ 7.0/10

The CTO of RansomwareHelp has been indicted for wire fraud, according to a November 2026 report by Krebs on Security. The charges stem from allegations that the incident response firm misled ransomware victims by claiming it never pays ransoms while actually negotiating and paying threat actors on behalf of clients, with a markup. The case highlights legal risks around deceptive practices in ransom negotiation. It has drawn attention because it tests the boundaries between legitimate incident response services and fraud.

hackernews · Bender · Nov 26, 17:47 · [Discussion](https://news.ycombinator.com/item?id=50657645)

**「Background」** In ransomware incident response, a key ethical and legal question is whether firms may negotiate or pay ransoms on behalf of victims. Some companies publicly state they do not pay ransoms, but are accused of doing so secretly while adding undisclosed fees or margins. Wire fraud \(18 U.S.C. § 1343\) criminalizes schemes to defraud using interstate wire communications, and applies when material misrepresentations induce victims to part with money.

**「Impact」** For ransomware victims and incident response providers, this prosecution signals that misrepresenting whether a firm pays ransoms can expose individuals to wire fraud charges, even if victims receive their data back.

**「Community Discussion」** Community discussion is split: some commenters question whether the alleged conduct meets the legal standard for wire fraud since the victim obtained their data and the margin was small, while others suggest that explicit contract terms authorizing ransom payment could avoid liability.

**Tags**: `#cybersecurity`, `#ransomware`, `#wire-fraud`, `#legal`, `#incident-response`

---

<a id="item-tech-news-5"></a>
### [Google&\#x27;s Workspace MCP: Gmail Cannot Send Email](https://techstackups.com/articles/google-workspace-ai-agents-mcp/) ⭐️ 7.0/10

Google is making Workspace MCP servers available for AI agents, but the Gmail-facing server does not include a send-email capability. Users and developers immediately noted that MCP&\#x27;s elicitation mechanism already supports pausing a tool call for user confirmation, which would allow a send-message tool to be gated behind approval. Some commenters therefore argue the restriction is more likely a business decision than a pure safety concern. Practical workarounds include browser automation or SMTP/IMAP access, which commenters describe as messier or more variable.

hackernews · ritzaco · Nov 26, 09:44 · [Discussion](https://news.ycombinator.com/item?id=50653477)

**「Background」** MCP \(Model Context Protocol\) is an open standard that lets AI agents call tools and access external data through a common interface. Google has published official Workspace MCP servers, including a Gmail MCP server that, according to Google for Developers, can read email data and create draft emails or label messages. However, Google&\#x27;s published tool lists indicate the official Gmail MCP server does not provide a send-email action, which is the limitation discussed in the source article.

**「Impact」** Developers integrating AI agents with Google Workspace Gmail via the official MCP server cannot send messages through that server and must use alternative paths such as browser automation or SMTP/IMAP, adding complexity and reliability risk.

**「Community Discussion」** Commenters largely argue the Gmail send restriction is a business choice, noting MCP elicitation already supports user confirmation for safety. Some report using NeoMutt with SMTP/IMAP as a more reliable workaround than browser automation or MCP.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.google.com/workspace/gmail/api/guides/configure-mcp-server">Configure the Gmail MCP server | Google for Developers</a></li>
<li><a href="https://commandmail.app/en/guides/gmail-mcp-server">Gmail MCP server : official Google preview, open... | Command Mail</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI agents`, `#Google Workspace`, `#Gmail`, `#API access`

---

<a id="item-tech-news-6"></a>
### [SQLite sqlite3\_rsync Copies Databases Without Duplicate Disk Space](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) ⭐️ 7.0/10

Simon Willison highlights that sqlite3\_rsync can copy a SQLite database snapshot over an SSH connection to another machine without first creating a full local copy. The tool was added as experimental in SQLite 3.47.0 in October 2024 and enhanced in SQLite 3.50.0 in May 2025. Existing snapshot methods such as the backup API or VACUUM INTO require enough disk space to create a duplicate copy, which can fail on small instances using more than half the available disk. sqlite3\_rsync also synchronizes an existing database copy by having the replica send cryptographic hashes for pages or groups of pages, and the origin sends back differing page content. If origin and replica start vastly different, total network bandwidth can exceed the size of the entire database due to hash exchange overhead, but the excess bandwidth is a few percent at most.

rss · Simon Willison · Nov 26, 06:08

**「Background」** SQLite is an embedded relational database commonly used in applications and small servers. Its backup API and VACUUM INTO command are standard ways to create database copies, but both require sufficient local disk space for a second copy. sqlite3\_rsync is a separate tool included with SQLite releases that provides remote synchronization via SSH using a hash-based protocol similar to rsync.

**「Impact」** Users on small instances with less than half of available disk free can create SQLite snapshots by copying over SSH, avoiding the disk-space limitation of the backup API and VACUUM INTO.

**Tags**: `#SQLite`, `#database`, `#remote-copy`, `#sysadmin`, `#software-engineering`

---

<a id="item-tech-news-7"></a>
### [Neuralink Gets FDA Approval for ALS Brain-Implant Trial](https://www.bloomberg.com/news/articles/2026-11-25/neuralink-gets-clearance-for-brain-implant-trial-in-als-patients?srnd=phx-technology) ⭐️ 7.0/10

Neuralink has received FDA approval to begin a pivotal brain-computer interface clinical trial in the United States called LINK for patients with ALS \(amyotrophic lateral sclerosis\). The trial aims to translate brain signals directly into computer control commands and is described as the first approved pivotal trial of this kind in the U.S. Neuralink previously implanted devices in more than 30 paralyzed patients globally through early studies. Entering the pivotal clinical stage marks accelerated progress from safety validation toward commercial medical device approval, and the resulting data will serve as the core basis for a future marketing authorization application.

telegram · zaihuapd · Nov 26, 07:15

**「Background」** Neuralink is an American neurotechnology company founded by Elon Musk and launched in 2016 that develops implantable brain-computer interfaces \(BCIs\). According to Neuralink, the LINK Pivotal Study is the first FDA-approved pivotal trial for an implantable BCI in the United States, testing the device in people with severe paralysis from ALS. Data from a pivotal trial are typically used as core evidence when seeking medical device marketing approval.

**「Impact」** The FDA approval enables Neuralink to begin a pivotal trial that, if successful, will supply the clinical data needed for a future premarket approval application for its LINK implant in patients with ALS-related paralysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuralink">Neuralink - Wikipedia</a></li>
<li><a href="https://interestingengineering.com/health/neuralink-fda-approval-link-pivotal-brain-implant-trial">Neuralink gets FDA approval for first pivotal brain implant trial</a></li>
<li><a href="https://neuralink.com/updates/neuralink-receives-fda-approval-to-launch-link-pivotal-study/">Neuralink Receives FDA Approval to Launch LINK Pivotal Study</a></li>
<li><a href="https://interestingengineering.com/health/neuralink-fda-approval-link-pivotal-brain-implant-trial">Neuralink gets FDA approval for first pivotal brain implant trial</a></li>

</ul>
</details>

**Tags**: `#Neuralink`, `#brain-computer interface`, `#FDA approval`, `#clinical trial`, `#ALS`

---

<a id="item-tech-news-8"></a>
### [ASML CEO: Full China Chip Ban Would Push China to Build Its Own](https://www.semafor.com/article/11/25/2026/asml-makes-the-case-for-selling-chips-to-china) ⭐️ 7.0/10

ASML CEO Christophe Fouquet argued in a Semafor Future Proof interview that export controls should protect the most advanced technology but not exclude China entirely, warning that a full cutoff would push China to double or triple its domestic lithography investment. He said the tools ASML sells to China are more than a decade behind the most advanced processes, and preserving that gap keeps China dependent on Western equipment. Fouquet noted that ASML has held nearly 100 percent of China&\#x27;s lithography market for nearly 30 years, and China has accepted that dependency. The United States is pushing the MATCH Act to expand controls from EUV to immersion DUV tools and maintenance services, a move opposed by both the Dutch government and ASML.

telegram · zaihuapd · Nov 26, 12:19

**「Background」** ASML is the leading supplier of photolithography machines that print circuit patterns on chips; EUV tools are needed for the most advanced nodes, while DUV tools serve older processes. Current export controls restrict EUV sales to China but still allow older DUV equipment and maintenance. The proposed U.S. MATCH Act would extend restrictions to immersion DUV tools and related services.

**「Impact」** If the MATCH Act passes, Chinese chipmakers that have relied on ASML for nearly 100 percent of their lithography tools would lose access to immersion DUV maintenance and upgrades, potentially disrupting production and accelerating domestic alternatives. The measure remains proposed and is opposed by the Dutch government and ASML.

**Tags**: `#semiconductors`, `#export controls`, `#ASML`, `#lithography`, `#China`

---

<a id="item-tech-news-9"></a>
### [Cloudflare Dashboard and API Outage Reported](https://www.cloudflarestatus.com/incidents/xiqj67vl5pqm) ⭐️ 7.0/10

Cloudflare published an incident notice on its status page on November 26 stating that it is investigating problems with the Cloudflare Dashboard and related APIs. Customers using the dashboard or APIs may be affected, and requests may fail or pages may show error messages. The incident is ongoing and had already lasted about half an hour at the time of the notice.

telegram · zaihuapd · Nov 26, 16:33

**「Background」** Cloudflare is a major content delivery network and security provider; customers typically manage DNS records, firewall rules, and other settings through the Cloudflare Dashboard and its API. The Dashboard and API are control-plane interfaces, separate from the data plane that serves cached content and mitigates attacks, so edge services often remain available during such management-plane incidents. Third-party status trackers later reported that the November 26, 2026 incident was resolved after about 2.3 hours and that core CDN functionality remained unaffected.

**「Customer impact」** Customers attempting to manage their services through the Cloudflare Dashboard or API may experience request failures or error messages, while core CDN and edge security functionality remained unaffected during the incident.

<details><summary>References</summary>
<ul>
<li><a href="https://isdown.app/status/cloudflare/incidents/698019-cloudflare-dashboard-and-cloudflare-api-service-issues">Cloudflare Cloudflare Dashboard and Cloudflare API — Nov 2026 ...</a></li>
<li><a href="https://www.technobezz.com/news/cloudflare-service-incident-25f5a50f">Cloudflare Dashboard and API service issues resolved</a></li>
<li><a href="https://cyberattack.ai/outages/cloudflare/2026-11-26-cloudflare-dashboard-and-cloudflare-api-service-issues">Cloudflare Dashboard and API issues (Nov 26, 2026 ...</a></li>
<li><a href="https://isdown.app/status/cloudflare/incidents/698019-cloudflare-dashboard-and-cloudflare-api-service-issues">Cloudflare Cloudflare Dashboard and Cloudflare API — Nov 2026 ...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#outage`, `#API`, `#dashboard`, `#infrastructure`

---

<a id="item-tech-news-10"></a>
### [Microsoft CEO: New Grad Hiring Slows as AI Budgets Take Priority](https://www.windowslatest.com/2026/11/27/lets-add-the-next-human-satya-nadella-admits-new-grad-hiring-slowed-as-companies-rebuild-around-ai-and-says-every-company-will-add-its-next-person-after-it-burns-through-its-ai-budget/) ⭐️ 7.0/10

Microsoft CEO Satya Nadella acknowledged on The Pragmatic Engineer podcast that new graduate hiring has slowed, saying companies will redeploy existing employees before adding new ones. He said AI-native companies will &\#x27;burn through their AI budget before adding their next human,&\#x27; and that every company will eventually do the same. Microsoft&\#x27;s headcount fell to 223,000 as of June 30, down 5,000 from a year earlier, its first annual decline since 2016. A paper from MIT and Microsoft Research found that companies adopting GitHub Copilot reduced quarterly technical hiring by 29%, with junior positions most affected.

telegram · zaihuapd · Nov 27, 03:03

**「Background」** The remarks come as companies increasingly invest in AI tools like GitHub Copilot, which automates parts of software development. Microsoft had previously signaled support for campus recruitment, with Nadella saying at Davos earlier this year that he still believed in it.

**「Impact」** For software engineering graduates and junior developers, hiring opportunities may shrink as AI tool adoption grows, especially at firms using GitHub Copilot, where the study found 29% lower quarterly technical hiring.

**Tags**: `#Microsoft`, `#AI hiring trends`, `#software engineering`, `#job market`, `#GitHub Copilot`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia halts AI server shipments to four Southeast Asian countries](https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370) ⭐️ 9.0/10

Nvidia has ordered manufacturing partners to stop shipping AI servers to Malaysia, Singapore, Thailand, and Indonesia after new US export restrictions require regional cloud providers to obtain export licenses within 90 days and verify customers are not restricted Chinese entities, according to the Financial Times.

telegram · zaihuapd · Nov 26, 07:38

**「Background」** The suspension follows a US Commerce Department rule issued last week requiring regional cloud service providers to obtain export licences within 90 days and verify that customers do not include restricted Chinese entities. The four countries have been used as transshipment hubs for China-bound advanced Nvidia chips.

**「Impact」** Regional cloud providers and data center operators in Malaysia, Singapore, Thailand, and Indonesia face possible delays or cancellation of AI server orders because manufacturers like Dell and Supermicro must pause shipments of Nvidia-based systems under the new U.S. export controls.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ft.com/content/7838a715-07d4-4605-aa60-21f5af2b2370?syn-25a6b1a6=1">Nvidia halts chip shipments to south - east Asia</a></li>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/11/26/nvidia-reportedly-halts-ai-chip-shipments-to-southeast-asia-as-us-tightens-china-curbs/">Nvidia Halts Server Shipments To 4 Southeast Asian Countries...</a></li>
<li><a href="https://www.zerohedge.com/ai/nvidia-halts-ai-chip-shipments-four-southwest-asian-countries">&quot;Causing Sheer Chaos&quot;: Nvidia Halts AI Chip Shipments ... | ZeroHedge</a></li>
<li><a href="https://asia.nikkei.com/business/technology/artificial-intelligence/nvidia-server-suppliers-halt-southeast-asia-shipments-over-us-curbs">Nvidia server suppliers halt Southeast Asia shipments ... - Nikkei Asia</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#export controls`, `#AI servers`, `#Southeast Asia`, `#US-China tech`

---

<a id="item-finance-news-2"></a>
### [Netherlands rejects proposed US curbs on ASML China sales](https://www.bloomberg.com/news/articles/2026-11-26/netherlands-plans-to-fight-rollout-of-proposed-us-curbs-on-asml) ⭐️ 8.0/10

Dutch Foreign Trade Minister Sjoerd Sjoerdsma told parliament on Nov 26 that the Netherlands will not accept proposed US export controls further restricting ASML&\#x27;s China sales, and is lobbying EU partners to remove the MATCH Act from a US defense bill. China accounts for about 20% of ASML&\#x27;s sales this year.

telegram · zaihuapd · Nov 26, 14:56

**「Background」** The MATCH Act is a bipartisan US proposal that would require allies such as the Netherlands and Japan to impose stricter China export controls, or face unilateral US restrictions on their semiconductor equipment.

**Tags**: `#ASML`, `#export controls`, `#semiconductors`, `#US-China trade`, `#Netherlands`

---