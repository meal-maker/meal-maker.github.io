---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 25 items, 11 important content pieces were selected

---

1. [Over 10k GitHub repos found distributing Trojan malware](#item-1) ⭐️ 9.0/10
2. [Zero-Touch OAuth Brings Enterprise Auth to MCP](#item-2) ⭐️ 8.0/10
3. [Ubiquiti Unveils Enterprise NAS with ZFS and Dual 25 GbE](#item-3) ⭐️ 8.0/10
4. [Hospitals and Universities Repurpose Drugs at Massive Cost Cuts](#item-4) ⭐️ 8.0/10
5. [Elkjop fined €1.8M for forced consent under GDPR](#item-5) ⭐️ 8.0/10
6. [Noam Shazeer Leaves Google to Join OpenAI](#item-6) ⭐️ 8.0/10
7. [Cornell's CS 6120 Advanced Compilers Now Self-Guided](#item-7) ⭐️ 7.0/10
8. [Swiss parliament lifts ban on new nuclear power plants](#item-8) ⭐️ 7.0/10
9. [Beyond .gitignore: Alternative Git ignore methods](#item-9) ⭐️ 7.0/10
10. [Website Checks If LLMs Recognize You Online](#item-10) ⭐️ 7.0/10
11. [TesterArmy Launches Agentic Testing Platform](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Over 10k GitHub repos found distributing Trojan malware](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

A security researcher discovered over 10,000 GitHub repositories distributing Trojan malware by analyzing push event patterns from GHArchive data. The attack uses deceptive commit patterns, frequent deletion and re-pushing of commits, and search manipulation to target automated software agents. This discovery reveals a massive-scale malware distribution campaign exploiting GitHub's trust, threatening the entire software supply chain. Developers and organizations using automated dependency tools could inadvertently pull malicious code, leading to widespread compromise. The attacker creates new repositories, deletes and re-pushes commits every few hours to appear 'recently updated' in search results. This pattern is optimized to infect automated agent searches, not human users, aiming to inject backdoors into downstream projects through dependency confusion or direct clone actions.

hackernews · theorchid · Jun 18, 11:45

**Background**: Software supply chain attacks inject malicious code into trusted platforms like GitHub, where developers automatically download dependencies. Attackers exploit the trust in open-source ecosystems by creating fake repositories that mimic legitimate projects or hijack tags and commits. Such attacks have grown significantly, with incidents like the SolarWinds breach and recent compromises of tools like Axios and LiteLLM.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/orchidfiles/git-malware-finder/">GitHub - orchidfiles/git- malware -finder: A script that searches GitHub ...</a></li>
<li><a href="https://www.securityweek.com/threat-actors-manipulate-github-search-to-deliver-malware/">Threat Actors Manipulate GitHub Search to Deliver Malware</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/over-3-000-github-accounts-used-by-malware-distribution-service/">Over 3,000 GitHub accounts used by malware distribution service</a></li>

</ul>
</details>

**Discussion**: Community members expressed alarm, with one user (Jimmc414) reporting that their name was attached to unknown malicious projects. Others analyzed the attacker's methods, noting that the rapid commit-deletion pattern is designed to manipulate GitHub search ranking and target automated agents, not humans. The discussion highlights the growing threat of AI-led dependency poisoning and supply chain attacks.

**Tags**: `#malware`, `#supply chain security`, `#github`, `#cybersecurity`, `#trojan`

---

<a id="item-2"></a>
## [Zero-Touch OAuth Brings Enterprise Auth to MCP](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/) ⭐️ 8.0/10

The Model Context Protocol (MCP) has introduced Zero-Touch OAuth, an enterprise-managed authorization mechanism that allows secure data sharing between applications using a common SSO provider without per-app OAuth configuration. This update makes MCP viable for large organizations by simplifying authentication workflows, reducing administrative overhead, and improving security—paving the way for broader enterprise adoption of AI tools built on MCP. The mechanism is powered by a new token format called ID-JAG (Identity-Justified Access Grant), which is not specific to MCP and can be used wherever data is shared between applications using the same SSO provider.

hackernews · niyikiza · Jun 18, 21:54

**Background**: The Model Context Protocol (MCP) is an open standard announced by Anthropic in November 2024 for connecting AI assistants to external data sources and tools. It provides a standardized interface for reading files, executing functions, and handling prompts. Zero-touch OAuth, part of 'Enterprise-Managed Authorization,' ensures that MCP servers are connected automatically on first login without requiring individual OAuth setup for each application.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/">Enterprise-Managed Authorization: Zero-touch OAuth for MCP | Model Context Protocol Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with praise from contributors at Okta, Microsoft, Figma, and Linear, alongside technical insights about the ID-JAG token format. However, some developers expressed frustration over the lack of long-running cookie support, with one user reporting they had to hack the spec to achieve a similar result.

**Tags**: `#MCP`, `#OAuth`, `#authentication`, `#AI tools`, `#enterprise`

---

<a id="item-3"></a>
## [Ubiquiti Unveils Enterprise NAS with ZFS and Dual 25 GbE](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 8.0/10

Ubiquiti announced a new enterprise NAS appliance built on the ZFS file system, featuring dual 25 Gigabit SFP28 ports and redundant power supplies. The product is priced at $3,999 and targets high-performance storage for businesses. This marks Ubiquiti's entry into enterprise storage, leveraging ZFS's proven data integrity features and high-speed networking. The no-monthly-fee model could disrupt subscription-heavy competitors, but community discussion highlights concerns about Ubiquiti's software quality track record. The NAS supports dual 25 GbE links which may be difficult to fully saturate with spinning hard drives, as noted in community comments. The device includes redundant power supplies and is listed at $3,999 on Ubiquiti's store.

hackernews · ksec · Jun 18, 14:24

**Background**: ZFS is a combined file system and volume manager known for features like data integrity verification via checksums, snapshots, and efficient replication. 25 Gigabit Ethernet provides 25 Gbps per link, commonly used in data centers for high-speed connectivity. Ubiquiti is primarily known for networking equipment (e.g., UniFi) but is expanding into storage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZFS">ZFS - Wikipedia</a></li>
<li><a href="https://itsfoss.com/what-is-zfs/">What is ZFS ? Why are People Crazy About it?</a></li>
<li><a href="https://www.linkedin.com/pulse/introduction-25g-40g-ethernet-network-fancy-wang">Introduction to 25 G and 40G Ethernet Network</a></li>

</ul>
</details>

**Discussion**: Community feedback is mixed: some praise the ZFS foundation and no-MRR model, while others raise serious concerns about Ubiquiti's software quality, citing past security incidents and UI/UX issues. A technical concern is whether spinning drives can saturate the 25 GbE links, questioning real-world performance.

**Tags**: `#Ubiquiti`, `#NAS`, `#ZFS`, `#enterprise storage`, `#networking`

---

<a id="item-4"></a>
## [Hospitals and Universities Repurpose Drugs at Massive Cost Cuts](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

Hospitals and universities are repurposing existing drugs to treat new conditions, achieving cost reductions of up to 90% compared to standard treatments. For example, the cancer drug Avastin is being used off-label for macular degeneration at 1/30th the price of the approved drug Lucentis. This trend could dramatically lower healthcare costs for patients and insurers, especially for expensive biologics and rare diseases. It also challenges the pharmaceutical industry's pricing model and highlights a path for non-profit innovation in medicine. Avastin and Lucentis are molecularly identical, but Avastin costs about $50 per dose while Lucentis costs $1,500 per dose — the main difference is packaging for ophthalmic use. Similarly, esketamine (Spravato) is a patented derivative of off-patent ketamine, yet is less effective and more expensive, illustrating misaligned incentives in drug development.

hackernews · giuliomagnifico · Jun 18, 10:33

**Background**: Drug repurposing involves finding new uses for existing approved medications, often for different diseases than originally intended. Because these drugs have already passed safety trials, they can be brought to new patients at a fraction of the cost and time of developing a new drug. However, without a regulatory pathway or manufacturer support, such off-label uses often remain unapproved and inaccessible at scale. Non-profits and academic medical centers are stepping in to fill this gap, funding clinical trials for rare and neglected diseases.

**Discussion**: Commenters shared real-world examples and concerns: one user with ophthalmology insight confirmed that Avastin and Lucentis are molecularly identical, with Avastin costing 1/30th the price. Another user described how their insurance pays high prices for esketamine (Spravato), a less effective derivative of the cheaper, off-patent ketamine. A third user praised Cures Within Reach, a nonprofit funding repurposing studies for rare diseases like Huntington's, while another noted the lack of a clear regulatory pathway to officially extend indications without manufacturer consent.

**Tags**: `#drug repurposing`, `#healthcare costs`, `#pharmaceuticals`, `#off-label use`, `#medical innovation`

---

<a id="item-5"></a>
## [Elkjop fined €1.8M for forced consent under GDPR](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

A Norwegian retailer, Elkjop, was fined €1.8 million by the Norwegian Data Protection Authority for requiring customers to consent to marketing as a condition of joining its customer club, which violates the GDPR's requirements for freely given consent. This case demonstrates that GDPR enforcement can result in significant penalties for forced consent practices, setting a precedent that may deter similar bundling of consent with service terms across the EU. The privacy advocate first reported the practice in 2019, but the fine was only issued five years later; the company's own email confirming that consent was a condition of membership became the critical evidence in the case.

hackernews · speckx · Jun 18, 18:31

**Background**: Under the GDPR, consent must be freely given, specific, informed, and unambiguous; conditioning a service on consent is considered unlawful coercion. Many companies historically bundled marketing consent with account registration, but regulators are increasingly enforcing that this practice violates data protection law.

**Discussion**: Commenters expressed mixed reactions: some praised the individual's persistence and the importance of exercising rights, while others found it ironic that he effectively sued the legal entity that won the case for him. One comment described the approach as a 'jurisprudence fetishist gets off on technicality,' reflecting a view that the case was won on a narrow legal point.

**Tags**: `#privacy`, `#GDPR`, `#consent`, `#legal`, `#EU`

---

<a id="item-6"></a>
## [Noam Shazeer Leaves Google to Join OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 8.0/10

Noam Shazeer, co-author of the seminal "Attention Is All You Need" paper and former co-lead of Google's Gemini project, has announced he is leaving Google to join OpenAI. This move was reported by Reuters on June 18, 2026. Shazeer is one of the most influential AI researchers, having co-invented the transformer architecture that underpins nearly all modern large language models. His move to OpenAI could significantly strengthen OpenAI's research capabilities and further intensify the talent competition between major AI labs. Shazeer originally left Google in 2021 to co-found Character.AI, but returned in 2024 through a licensing and talent deal valued at around $2.7 billion, becoming a co-lead of Gemini. Now, just two years later, he is departing again for OpenAI.

hackernews · lukasgross · Jun 18, 00:26

**Background**: The transformer architecture, introduced in the 2017 paper "Attention Is All You Need" co-authored by Noam Shazeer, revolutionized natural language processing and became the foundation for models like GPT, BERT, and Gemini. Shazeer has been a key researcher at Google since 2000, known for his engineering contributions. His career path reflects the intense demand for top AI talent and the strategic moves between leading companies.

**Discussion**: The community comments provide important context about Shazeer's history and significance. Commenters note that Shazeer was a legendary engineer at Google in the 2000s, and that his contributions to the transformer paper were critical. Some express surprise that he is leaving Google again so soon after returning, with speculation about the reasons.

**Tags**: `#AI`, `#OpenAI`, `#Google`, `#transformers`, `#industry-news`

---

<a id="item-7"></a>
## [Cornell's CS 6120 Advanced Compilers Now Self-Guided](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

Cornell University's CS 6120 advanced compilers course, taught by Adrian Sampson, is now available as a free, self-guided online course, with all lectures and materials publicly accessible. This makes a high-quality, advanced compiler curriculum freely accessible to a global audience, benefiting aspiring compiler engineers and systems programmers who lack access to formal education. The course covers topics such as SSA form, data-flow analysis, and dynamic compilation, but one commenter noted that its section on dynamic compilers focuses heavily on trace compilation, which is considered a dead end by some.

hackernews · ibobev · Jun 18, 11:04

**Background**: Compiler design is a core topic in computer science, typically covered in undergraduate courses with basic optimization techniques. An advanced compilers course delves into modern optimization passes, intermediate representations, and runtime compilation strategies like just-in-time (JIT) compilation. CS 6120 is known for its hands-on approach using the LLVM compiler infrastructure.

**Discussion**: Community reaction is generally positive, with many thanking Adrian Sampson for the resource. However, there is technical critique: Titzer argues that the focus on trace compilation is outdated, while j2kun questions whether the content qualifies as 'advanced,' noting that many topics appear in first compiler courses. The discussion also includes comparisons to other learning resources like Nora Sandler's 'Writing a C Compiler.'

**Tags**: `#compilers`, `#education`, `#systems`, `#programming languages`, `#online course`

---

<a id="item-8"></a>
## [Swiss parliament lifts ban on new nuclear power plants](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) ⭐️ 7.0/10

The Swiss parliament voted to lift the ban on constructing new nuclear power plants, overturning a post-Fukushima moratorium, though the decision is subject to a public referendum. This policy shift could reshape Switzerland's energy strategy, potentially allowing nuclear to complement renewables for winter energy security, and sparks debate on nuclear's role in achieving carbon neutrality. The ban was originally enacted after the 2011 Fukushima disaster; the new law still requires approval in a referendum, and political opposition from left-leaning and green parties is strong.

hackernews · leonidasrup · Jun 18, 14:17

**Background**: Switzerland has a seasonal energy imbalance, producing more electricity from hydro in spring/summer and less in winter. Nuclear power provides steady baseload, but safety concerns and high costs have limited its expansion. The country is also pursuing renewable energy expansion.

**Discussion**: Commenters are divided: some argue nuclear has the lowest death rate per TWh and provides energy security, while others believe new plants will be too expensive and slow compared to renewables, and suggest joining French nuclear projects or expanding hydro storage instead.

**Tags**: `#nuclear energy`, `#energy policy`, `#Switzerland`, `#technology policy`, `#geopolitics`

---

<a id="item-9"></a>
## [Beyond .gitignore: Alternative Git ignore methods](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/) ⭐️ 7.0/10

This article highlights two lesser-known ways to ignore files in Git: a global exclude file configured via core.excludesFile and the use of .gitattributes to control diff or archive behavior. These methods allow developers to ignore files without modifying a project's local .gitignore. These alternative ignore techniques help developers keep project .gitignore files clean and avoid committing IDE, OS, or personal configuration files across all repositories. They also enable fine-grained control over which files appear in diffs or archives, reducing noise and improving workflow efficiency. The global exclude file can be set with `git config --global core.excludesFile ~/.gitignore_global` and applies ignore rules to every repository on the machine. The .gitattributes file supports attributes like `export-ignore` to exclude files from `git archive` and `diff=<driver>` to treat certain files as binary for diff purposes.

hackernews · FergusArgyll · Jun 18, 10:29

**Background**: Git traditionally ignores files using a .gitignore file in each repository, which is committed and shared with the team. However, some files (like .DS_Store or editor configs) are machine-specific and should be ignored globally. Additionally, Git's .gitattributes file allows per-path attribute settings beyond ignoring, such as controlling how Git handles binary files or archive exports. Understanding these additional mechanisms helps developers manage their Git workflow more effectively.

<details><summary>References</summary>
<ul>
<li><a href="https://git-scm.com/docs/gitattributes">Git - gitattributes Documentation</a></li>
<li><a href="https://andreynautilus.github.io/posts/2024-12-24-gitignore-global/">Set global .gitignore file via core . excludesFile</a></li>
<li><a href="https://gist.github.com/subfuzion/db7f57fff2fb6998a16c">Global gitignore. GitHub Gist: instantly share code, notes, and snippets.</a></li>

</ul>
</details>

**Discussion**: Community comments praise the global exclude feature for reducing clutter in project .gitignore files, with one user noting it solves the problem of contributors adding IDE files to every repo. Another user suggests using ~/.config/git/ignore as the default path for the global ignore file, while a third shares a clever trick: adding an 'attic' directory to the global ignore for storing temporary files that should never be committed.

**Tags**: `#git`, `#version control`, `#.gitignore`, `#developer tools`, `#configuration`

---

<a id="item-10"></a>
## [Website Checks If LLMs Recognize You Online](https://www.intheweights.com/) ⭐️ 7.0/10

The website 'Are You in the Weights?' queries multiple large language models in parallel to determine if they recognize a person based on their online presence, then clusters the responses and assigns a strength score. This tool raises awareness about the extent of personal data embedded in LLM training sets and highlights privacy implications as more traffic moves into AI models. It also demonstrates name disambiguation challenges, as people with common names may be recognized differently across models. The tool queries both frontier and small models simultaneously, clusters their outputs, and provides a strength score indicating how strongly the models recognize the individual. The creator notes it is non-deterministic and that adding more keywords about yourself increases the score.

hackernews · turtlesoup · Jun 18, 20:49

**Background**: Large language models (LLMs) are trained on vast datasets scraped from the internet, including public profiles, forum posts, and other online content. When a person has a significant online presence, their information may become part of the training data, allowing the model to generate responses that 'recognize' that person. The 'strength score' likely measures consistency across model responses, similar to clustering techniques used in LLM evaluation metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2601.11118">Optimized Algorithms for Text Clustering with LLM-Generated ...</a></li>
<li><a href="https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00648/120476/Large-Language-Models-Enable-Few-Shot-Clustering">Large Language Models Enable Few-Shot Clustering - MIT Press</a></li>
<li><a href="https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation">LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide - Confident AI</a></li>

</ul>
</details>

**Discussion**: Community members shared personal experiences: some found themselves recognized (e.g., nickcw in open source), while others with common names like setgree had mixed results due to name disambiguation. Users noted the tool's non-deterministic nature and joked about digital legacy, but also expressed mild privacy concerns over being 'immortal in the weights' without consent.

**Tags**: `#LLM`, `#privacy`, `#recognition`, `#tool`, `#AI`

---

<a id="item-11"></a>
## [TesterArmy Launches Agentic Testing Platform](https://tester.army/) ⭐️ 6.0/10

TesterArmy, a YC P26 startup, launched an agentic testing platform that lets users define and execute end-to-end tests for web and mobile apps using natural language. The platform uses AI agents to run these tests before deployment and continuously in production. This addresses a key bottleneck where testing remains slow and manual even as AI coding tools accelerate code writing. By automating test creation and execution, TesterArmy could significantly reduce testing time and maintenance costs, improving development velocity for engineering teams. The platform relies on models like Google Gemini Flash and OpenAI GPT-5.4 for different tasks, with step-level timeouts and visual call limits per step. It integrates with GitHub, Slack, and Discord for alerts, and claims growth from 0 to 30+ teams within months.

hackernews · okwasniewski · Jun 18, 14:49

**Background**: Agentic testing platforms use AI agents that can autonomously plan, execute, and adapt tests without manual scripting. Traditional end-to-end testing requires writing and maintaining brittle code with UI selectors, which is time-consuming and costly. Natural language test specification allows engineers to describe tests in plain English, and the AI agent translates that into executable actions. This approach aims to make testing more accessible and reduce the overhead of test infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://vtestcorp.com/insights/agentic-testing-the-complete-guide-to-ai-powered-software-testing-in-2026/">Agentic Testing: Complete Guide to AI-Powered QA | VTEST</a></li>
<li><a href="https://dev.to/devdev2413/i-got-tired-of-writing-e2e-tests-so-i-built-an-ai-that-runs-them-for-me-4p32">I got tired of writing E2E tests , so I built an AI that... - DEV Community</a></li>
<li><a href="https://testrigor.com/ai-agents-in-software-testing/">AI Agents in Software Testing - testRigor AI-Based Automated Testing Tool</a></li>

</ul>
</details>

**Discussion**: Community comments show cautious interest. Some question how TesterArmy ensures deterministic results and how token costs compare to using LLMs to generate traditional scripts. Others express concern about relying on a third-party SaaS for critical testing infrastructure. The technical details revealed specific model choices and timeouts, prompting further questions about limitations and model freshness.

**Tags**: `#testing`, `#AI agents`, `#web development`, `#mobile development`, `#startup`

---