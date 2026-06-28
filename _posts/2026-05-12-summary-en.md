---
layout: default
title: "Horizon Summary: 2026-05-12 (EN)"
date: 2026-05-12
lang: en
---

> From 20 items, 9 important content pieces were selected

---

1. [UCLA discovers first drug to repair stroke-damaged brain connections](#item-1) ⭐️ 9.0/10
2. [Google: Criminal Hackers Used AI to Find Zero-Day Flaw](#item-2) ⭐️ 9.0/10
3. [TanStack npm Supply-Chain Compromise Postmortem](#item-3) ⭐️ 8.0/10
4. [GitLab Lays Off Staff, Abandons CREDIT Values for AI Pivot](#item-4) ⭐️ 8.0/10
5. [Ratty: A terminal emulator with inline 3D graphics](#item-5) ⭐️ 8.0/10
6. [Optimizing Matrix Multiplication in Swift from Gflop/s to Tflop/s](#item-6) ⭐️ 8.0/10
7. [Gmail Registration Now Requires Scanning a QR Code to Send SMS](#item-7) ⭐️ 7.0/10
8. [Is Python Still Needed if AI Writes Code?](#item-8) ⭐️ 6.0/10
9. [TypedMemory: Fast Java Record-to-Native Memory Mapping](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [UCLA discovers first drug to repair stroke-damaged brain connections](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

UCLA researchers have identified a drug candidate that promotes axonal sprouting and reconnects neural networks disrupted by stroke, targeting the molecular program for brain repair. This is the first pharmacological agent specifically designed for stroke rehabilitation rather than acute treatment. If validated in further trials, this drug could dramatically reduce the need for intensive physical therapy by enabling stroke patients to take a medicine that produces rehabilitation-like effects. It offers a new avenue for recovery in the millions of stroke survivors worldwide who currently have limited options for restoring lost function. The drug targets the ATRX gene, which is involved in controlling DNA structure and accessibility, and has not previously been linked to axonal sprouting after brain injury. The study focuses on restoring rhythm in surviving neural networks surrounding the infarct, not on regenerating dead brain cells at the stroke core.

hackernews · bookofjoe · May 11, 17:53

**Background**: Stroke often damages brain tissue by blocking blood flow, leading to cell death in the core infarct area. However, surrounding regions may contain 'bruised' but living neurons that lose connections and rhythm. The brain can naturally sprout new axonal connections after stroke through a process called axonal sprouting, but this is limited. UCLA researchers discovered a molecular program involving the ATRX gene that controls this sprouting, and they developed a drug to enhance it.

<details><summary>References</summary>
<ul>
<li><a href="https://www.newswise.com/articles/ucla-researchers-identify-molecular-program-for-brain-repair-following-stroke">Researchers Identify Molecular Program for Brain Repair ... | Newswise</a></li>
<li><a href="https://www.mdpi.com/2076-3425/15/11/1217">Reconnecting Brain Networks After Stroke : A Scoping Review of...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4980303/">Molecular, Cellular and Functional Events in Axonal Sprouting after ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlighted that the drug targets surviving networks, not dead cells, which addresses a common misconception about stroke recovery. One commenter referenced Ted Chiang's short story 'Understand' as a literary parallel, while another provided a PubMed link to the specific compound. Some readers asked whether the treatment could apply to other neurodegenerative diseases.

**Tags**: `#stroke`, `#rehabilitation`, `#neuroscience`, `#drug discovery`, `#UCLA`

---

<a id="item-2"></a>
## [Google: Criminal Hackers Used AI to Find Zero-Day Flaw](https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html) ⭐️ 9.0/10

Google's Threat Intelligence Group (GTIG) reported with high confidence that a hacker group used an AI model to discover and weaponize a zero-day vulnerability, marking the first documented case of AI-assisted cyber attacks in the wild. This incident represents a paradigm shift in cybersecurity, as AI tools can now drastically lower the barrier for discovering critical vulnerabilities, potentially devaluing traditional zero-day exploit stashes and accelerating the arms race between attackers and defenders. Google's report from the GTIG AI Threat Tracker indicates that the adversary likely leveraged a large language model (LLM) to support both discovery and exploitation, while new models like Anthropic's Mythos are also capable of such discoveries but are restricted to limited release.

hackernews · donohoe · May 11, 13:20

**Background**: A zero-day vulnerability is a software flaw unknown to the vendor, leaving it unpatched and exploitable by attackers. Traditional discovery requires significant expertise, but AI models—especially large language models fine-tuned for code analysis—can automate and accelerate vulnerability research. Techniques like LLM fuzzing have been explored by security researchers to test both AI models themselves and traditional software.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access">Adversaries Leverage AI for Vulnerability ... | Google Cloud Blog</a></li>
<li><a href="https://nullsec.news/ai-model-vulnerability-scanning-moves-beyond">AI Model Vulnerability Scanning Moves Beyond Theory... | NullSec</a></li>
<li><a href="https://www.crowdstrike.com/en-us/blog/feedback-guided-fuzzing-reveals-llm-blind-spots/">Feedback-Guided Fuzzing Reveals LLM Blind Spots | CrowdStrike</a></li>

</ul>
</details>

**Discussion**: Commenters questioned how Google determined AI was used, with some expressing skepticism about attribution. Others debated the implications for open-weight models—arguing that security concerns could be used to restrict them—and noted that AI-assisted hacking devalues zero-day exploit stashes.

**Tags**: `#cybersecurity`, `#AI`, `#zero-day`, `#hacking`, `#LLM`

---

<a id="item-3"></a>
## [TanStack npm Supply-Chain Compromise Postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 8.0/10

TanStack published a postmortem detailing a supply-chain compromise where a malicious commit in a fork of their repository used npm postinstall scripts to steal GitHub authentication tokens and spread to other packages. This incident underscores the severe risk of postinstall scripts in the npm ecosystem and shows that even widely-used open-source projects are vulnerable to supply-chain attacks. It also highlights the limitations of current security measures like Trusted Publishing when an attacker gains access to a CI pipeline or repo credentials. The malicious code was introduced via an orphan commit in a fork, and npm's use of shared object storage made the commit URI indistinguishable from the legitimate repository. The payload installed a dead-man's switch that would delete the user's home directory if the stolen token was revoked, and the worm also compromised other packages such as @mistralai/mistralai.

hackernews · varunsharma07 · May 11, 21:08

**Background**: npm postinstall scripts are automatically executed during package installation, and they run with the user's system permissions, making them a common vector for malware. Supply-chain attacks target the software development and distribution process to inject malicious code into trusted packages. TanStack is a popular open-source project providing React libraries like React Query and React Router.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">How npm handles the " scripts " field</a></li>
<li><a href="https://www.trendmicro.com/en_us/research/25/i/npm-supply-chain-attack.html">What We Know About the NPM Supply Chain Attack | Trend Micro (US)</a></li>

</ul>
</details>

**Discussion**: Community members warned about a dangerous dead-man's switch installed by the payload that could wipe the user's home directory upon token revocation. Others noted that additional packages, including @mistralai/mistralai, were also compromised. Some argued that the attack highlights the insufficiency of Trusted Publishing alone and recommended using pnpm to mitigate postinstall script risks, while several commenters blamed GitHub for allowing fork commits to be reachable via the same object storage.

**Tags**: `#supply-chain security`, `#npm`, `#open-source`, `#security incident`, `#postinstall scripts`

---

<a id="item-4"></a>
## [GitLab Lays Off Staff, Abandons CREDIT Values for AI Pivot](https://about.gitlab.com/blog/gitlab-act-2/) ⭐️ 8.0/10

GitLab announced a workforce reduction and replaced its long-standing CREDIT values (Collaboration, Results, Efficiency, Diversity, Inclusion, Transparency) with new values emphasizing speed, ownership, and customer outcomes, signaling a strategic pivot toward AI and agentic development. This move reflects a broader industry trend where companies are cutting costs and refocusing on AI, often at the expense of diversity, equity, and inclusion (DEI) initiatives. GitLab's shift could influence other DevOps and tech companies to adopt similar strategies, potentially reshaping corporate culture and workforce priorities. The new values are 'Speed with Quality,' 'Ownership Mindset,' and 'Customer Outcomes,' replacing the previous CREDIT framework which included Diversity, Inclusion & Belonging. GitLab stated that the agentic era represents the largest opportunity in its history and that the company had grown into a shape unsuitable for this new era.

hackernews · AnonGitLabEmpl · May 11, 20:51

**Background**: GitLab is a major DevOps platform that provides source code management, CI/CD, and observability tools. The company previously promoted CREDIT values, which included Diversity, Inclusion & Belonging as core principles. This announcement, which also involves layoffs, marks a significant cultural and strategic departure as GitLab refocuses on AI agents and operational efficiency.

**Discussion**: Community comments on Hacker News were largely critical. Many commenters expressed skepticism about GitLab's AI pivot, with one noting that the new values essentially mean 'work harder, not smarter, and no more DEI.' Others questioned the logic of reducing headcount while claiming the largest opportunity ever, and expressed concerns about worsening UX through increased reliance on AI bots.

**Tags**: `#GitLab`, `#layoffs`, `#corporate values`, `#AI pivot`, `#DevOps`

---

<a id="item-5"></a>
## [Ratty: A terminal emulator with inline 3D graphics](https://ratty-term.org/) ⭐️ 8.0/10

Ratty is a new GPU-rendered terminal emulator that natively supports inline 3D graphics via its own Ratty Graphics Protocol (RGP), allowing users to place 3D objects directly within terminal cells. This innovation breaks the traditional text-only boundary of terminal emulators, opening up new possibilities for interactive data visualization, debugging, and development workflows that blend text and 3D content. Ratty is built with Rust and Ratatui, inspired by TempleOS, and uses a GPU-accelerated rendering pipeline to handle 3D assets in .obj and .glb formats with animation, scaling, and color attributes.

hackernews · orhunp_ · May 11, 10:13

**Background**: Traditional terminal emulators only display text and simple glyphs, though protocols like kitty's graphics protocol have enabled inline 2D images. Ratty extends this by adding native 3D object rendering directly in the terminal, leveraging the GPU for performance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/orhun/ratty">GitHub - orhun/ ratty : A GPU-rendered terminal emulator with inline ...</a></li>
<li><a href="https://ratty-term.org/">Ratty — A GPU-rendered terminal emulator with inline 3 D graphics</a></li>
<li><a href="https://blog.orhun.dev/introducing-ratty/">Ratty : A terminal emulator with inline 3 D graphics - Orhun's Blog</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion highlights enthusiasm for the concept, with comparisons to historical systems like Xerox workstations and Lisp machines that had inline graphics in the 1980s. Users also discuss potential applications in VR, SSH compatibility issues with GPU acceleration, and comparisons to other innovative terminals like kitty.

**Tags**: `#terminal`, `#3D graphics`, `#emulator`, `#Hacker News`, `#open-source`

---

<a id="item-6"></a>
## [Optimizing Matrix Multiplication in Swift from Gflop/s to Tflop/s](https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html) ⭐️ 8.0/10

Matt Gallagher published a detailed guide on optimizing matrix multiplication in Swift for LLM training on Apple Silicon, achieving a performance leap from Gflop/s to Tflop/s. This article demonstrates that Swift, combined with Apple Silicon's hardware accelerators like AMX, can achieve competitive performance for machine learning workloads, potentially reducing reliance on external GPU frameworks. It also fills a gap in documented Swift performance optimization techniques. The author used Apple's AMX (Apple Matrix Coprocessor) instructions and compiler flags like -ffast-math to boost matrix multiplication performance. The M3 Max GPU's theoretical peak is around 15 Tflop/s, but the real ceiling for such tasks is 3-5 Tflop/s.

hackernews · zdw · May 10, 17:05

**Background**: Matrix multiplication is a core operation in training large language models (LLMs). Apple Silicon chips include a dedicated AMX coprocessor for accelerating matrix operations, but utilizing it effectively requires low-level optimization. Swift is a modern programming language developed by Apple, and frameworks like MLX Swift are emerging to support on-device ML research on Apple hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://research.meekolab.com/the-elusive-apple-matrix-coprocessor-amx">The Elusive Apple Matrix Coprocessor (AMX)</a></li>
<li><a href="https://www.swift.org/blog/mlx-swift/">On-device ML research with MLX and Swift | Swift .org</a></li>

</ul>
</details>

**Discussion**: Commenters praised the article's quality and novelty, noting it fills a gap in Swift performance optimization literature. Some discussed the secrecy of AMX instructions, compiler flags for FMA (fused multiply-add), and the software moat of Nvidia's CUDA in GPU compute.

**Tags**: `#Swift`, `#matrix multiplication`, `#performance optimization`, `#LLM`, `#Apple Silicon`

---

<a id="item-7"></a>
## [Gmail Registration Now Requires Scanning a QR Code to Send SMS](https://discuss.privacyguides.net/t/google-account-registration-now-requires-sending-an-sms-via-phone-instead-of-receiving-an-sms/36082) ⭐️ 7.0/10

Gmail has changed its registration process: instead of receiving an SMS verification code, new users must now scan a QR code with their smartphone, which opens a pre-filled SMS message that they must send to Google to verify their phone number. This change shifts the cost and privacy burden from Google to the user, as it requires users to actively send a message from their own phone, potentially revealing their phone number to Google. It also raises accessibility concerns for users without a smartphone or SMS capability, and intensifies the ongoing debate about Google's monopoly power and anti-spam measures. The QR code does not automatically send the SMS; it only opens a pre-composed text message that the user must manually send. This is effectively the old phone number verification but with a QR code convenience, and it may be part of Google's efforts to reduce automated account creation and spam.

hackernews · negura · May 11, 07:26

**Background**: Previously, Gmail registration involved entering a phone number and receiving a verification code via SMS. The new method inverts the flow: the user scans a QR code on the Gmail sign-up page with their smartphone, which triggers an SMS URI that the user then sends to a Google number. This change has sparked privacy concerns because it potentially gives Google the user's outgoing SMS metadata, and it also places the cost of the SMS on the user. Additionally, it may limit access for individuals who rely on landlines or do not have a mobile phone capable of sending SMS.

**Discussion**: Community comments show mixed sentiments. Some users sympathize with Google's struggle against spam and maintain free infrastructure, while others see this as another example of Google abusing its monopoly power. A technical clarification notes that the QR code only opens a pre-composed SMS and does not automatically send anything. One commenter argues that this move should be used as evidence in antitrust cases to force Google to make Gmail compete independently.

**Tags**: `#Gmail`, `#registration`, `#privacy`, `#Google`, `#SMS verification`

---

<a id="item-8"></a>
## [Is Python Still Needed if AI Writes Code?](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055) ⭐️ 6.0/10

A Medium blog post questions whether Python remains necessary when AI can write code for developers, but community comments push back by highlighting that Python's dominance in training data and the need for human oversight keep it essential. This discussion reflects a growing debate in the developer community about programming language choices in an era of AI-assisted coding, influencing how teams decide which languages to learn, adopt, or deprecate. Large language models (LLMs) are trained on vast amounts of text, including massive volumes of Python code, which makes them better at generating Python compared to less common languages. Additionally, AI code suggestions frequently contain errors, requiring human developers to review and fix them, so knowing the language is still necessary.

hackernews · indigodaddy · May 11, 20:45

**Background**: Large language models (LLMs) are deep learning models pre-trained on enormous text corpora for natural language processing and generation, and they power modern AI coding assistants like GitHub Copilot. These models use probabilistic methods to suggest code based on patterns in their training data, which for code is heavily dominated by Python. As a result, the quality of AI-generated code varies significantly across programming languages, and developers must still understand the code to verify correctness and security.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI pair programmer · GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments strongly counter the blog's premise: users note that Python's massive presence in training data makes AI much more reliable for Python than for exotic languages, and that AI frequently makes mistakes, so human review is indispensable. One commenter jokes 'If AI writes your articles, why use brain?' and another warns against shipping an app in a language no one on the team knows.

**Tags**: `#AI coding assistants`, `#Python`, `#programming languages`, `#LLM limitations`, `#developer tooling`

---

<a id="item-9"></a>
## [TypedMemory: Fast Java Record-to-Native Memory Mapping](https://github.com/mamba-studio/TypedMemory) ⭐️ 6.0/10

A new Java library called TypedMemory enables mapping Java record types directly to off-heap native memory, aiming to simplify high-performance data structures. However, community discussions question whether the library truly achieves zero allocation, as getters and setters may still allocate record objects. This library addresses a long-standing need for type-safe, off-heap data access in Java, which is critical for low-latency and large-scale applications. However, if object allocation is not eliminated, the performance benefits may be limited, reducing its practical value for zero-allocation use cases. TypedMemory uses Java records to define data layouts and provides methods like getters that may instantiate new record objects per call, potentially undermining zero-allocation claims. The library lacks a direct performance comparison with established alternatives such as SBE or GraalVM.

hackernews · joe_mwangi · May 11, 19:33

**Background**: Off-heap memory in Java refers to memory allocated outside the Java heap, which is not managed by garbage collection and can improve performance and predictability in latency-sensitive applications. Java records are a concise syntax for declaring immutable data carriers introduced in Java 16. Libraries like TypedMemory attempt to combine the type safety of records with the performance of off-heap storage, but avoiding object allocation during access is a key challenge in such designs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/manojkhanwalkar/offheap">GitHub - manojkhanwalkar/ offheap : Data structures that utilize...</a></li>
<li><a href="https://www.w3computing.com/articles/how-to-use-javas-unsafe-class-for-low-level-programming/">How to Use Java 's Unsafe Class for Low-Level Programming</a></li>
<li><a href="https://github.com/OpenHFT/Zero-Allocation-Hashing">GitHub - OpenHFT/Zero-Allocation-Hashing: Zero-allocation hashing for Java</a></li>

</ul>
</details>

**Discussion**: Community comments are skeptical about the library's zero-allocation claims, pointing out that getter methods likely create new record objects on the heap, which defeats the purpose in high-performance contexts. Some commenters suggest comparing with established frameworks like SBE or GraalVM, while others see potential if the allocation issue can be resolved through flyweight patterns or code generation.

**Tags**: `#java`, `#off-heap`, `#memory-mapping`, `#records`, `#performance`

---