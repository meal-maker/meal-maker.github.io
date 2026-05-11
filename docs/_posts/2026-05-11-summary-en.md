---
layout: default
title: "Horizon Summary: 2026-05-11 (EN)"
date: 2026-05-11
lang: en
---

> From 19 items, 6 important content pieces were selected

---

1. [Hardware Attestation Risks as Monopoly Enabler](#item-1) ⭐️ 8.0/10
2. [Local AI needs to become the norm](#item-2) ⭐️ 8.0/10
3. [Fictional Incident Report Exposes Rust Supply Chain Risks](#item-3) ⭐️ 8.0/10
4. [AWS Complexity and Lock-in Frustrations Resurface](#item-4) ⭐️ 7.0/10
5. [Maryland Residents Hit with $2B Grid Upgrade for Out-of-State AI](#item-5) ⭐️ 7.0/10
6. [Joanna Rutkowska Launches Personal Blog on Rationality vs Humanism](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Hardware Attestation Risks as Monopoly Enabler](https://grapheneos.social/@GrapheneOS/116550899908879585) ⭐️ 8.0/10

A community discussion highlights that the EU Digital Identity Wallet requires hardware attestation from Google or Apple, effectively tying European digital identities to the US tech duopoly and raising concerns about digital sovereignty and user privacy. If implemented, this requirement could entrench the market power of Apple and Google, making it impossible for users with alternative devices or operating systems to participate in essential digital identity services. It also risks undermining the EU's own goals of digital sovereignty and privacy protection. The attestation process uses cryptographic keys burned into device hardware to prove unmodified software, but critics note it lacks zero-knowledge proofs or blind signatures, meaning each use leaves a traceable attestation packet linking actions to a specific device.

hackernews · ChuckMcM · May 10, 17:54

**Background**: Hardware attestation is a cryptographic process that verifies a device's integrity by checking its hardware and software configuration against manufacturer-signed keys. It is commonly used for security, but when mandated by a digital identity system, it forces reliance on device manufacturers like Apple and Google. The EU Digital Identity Wallet, established by regulation in 2024, aims to provide a unified digital identity for EU citizens, but its technical requirements are still being defined through implementing regulations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EU_Digital_Identity_Wallet">EU Digital Identity Wallet - Wikipedia</a></li>
<li><a href="https://www.securview.com/ai-security-essentials/hardware-attestation">Hardware Attestation: Definition and Key Concepts</a></li>

</ul>
</details>

**Discussion**: The community expresses strong criticism, noting the irony of requiring US tech company attestation for European digital sovereignty. Some commenters highlight additional privacy flaws, such as the absence of zero-knowledge proofs, and draw historical parallels to Intel's abandoned CPU serial number and the rise of TPMs and walled gardens. Others mention Microsoft's Pluton as another example of similar hardware-level lock-in.

**Tags**: `#hardware attestation`, `#digital sovereignty`, `#privacy`, `#monopoly`, `#EU digital wallet`

---

<a id="item-2"></a>
## [Local AI needs to become the norm](https://unix.foo/posts/local-ai-needs-to-be-norm/) ⭐️ 8.0/10

A widely-discussed blog post argues that local AI—running large language models on consumer devices—should become the standard approach, pointing to a clear progression from data-center-scale inference to modern laptops and phones with sufficient memory and compute. Shifting AI execution from cloud servers to local devices dramatically improves privacy, reduces dependency on external providers, and makes advanced AI accessible even without an internet connection—benefits that matter to both individual users and enterprises seeking data sovereignty. Current consumer hardware like the MacBook Pro with up to 128 GB unified memory or AMD's Strix Halo can already run practical local models, and open-source tools like llama.cpp with the GGUF format make deployment straightforward. Even with smaller models, tasks such as text-to-speech, document summarization via RAG, and basic image generation are already feasible on a typical laptop.

hackernews · cylo · May 10, 17:19

**Background**: Local AI refers to running AI models directly on a user's own device rather than sending data to a remote cloud server. Projects like llama.cpp provide high-performance inference in C/C++ for various LLMs, and the GGUF format standardizes model packaging for efficient loading on consumer hardware. Meanwhile, recent CPUs from Intel, AMD, and Qualcomm now contain dedicated Neural Processing Units (NPUs) designed to accelerate small AI models locally, marking a hardware shift that supports the local-AI vision.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_processing_unit">Neural processing unit - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are broadly optimistic about local AI's trajectory, drawing parallels to the early days of open-source software when proprietary solutions were far ahead. Some emphasize separating "private AI" (e.g., self-hosted servers) from strictly "local AI" on personal devices, noting that a Plex-like self-hosted inference solution could satisfy privacy needs without requiring everything to run on a phone or laptop.

**Tags**: `#local AI`, `#AI accessibility`, `#privacy`, `#open source AI`, `#hardware progression`

---

<a id="item-3"></a>
## [Fictional Incident Report Exposes Rust Supply Chain Risks](https://nesbitt.io/2026/02/03/incident-report-cve-2024-yikes.html) ⭐️ 8.0/10

A fictional yet highly realistic incident report, CVE-2024-YIKES, satirically details a supply-chain attack on Rust crates, highlighting how a seemingly benign crate with a cartoon fox logo could be a transitive dependency of cargo itself and lead to widespread compromise. This satire underscores very real systemic vulnerabilities in package ecosystems like Rust's crates.io, where even a low-star, joke crate can become a critical dependency. It serves as a wake-up call for developers and security teams to audit dependency chains and prioritize security headcount. The report mentions a specific crate 'vulpine-lz4' described as 'blazingly fast Firefox-themed LZ4 decompression' with only 12 GitHub stars yet a transitive dependency of cargo, and lists other crates like flate2, tar, curl-sys, libgit2-sys that already have build.rs and could be targeted.

hackernews · miniBill · May 10, 17:43

**Background**: Rust's package manager, Cargo, relies on crates.io, a central registry for sharing libraries (crates). A supply-chain attack occurs when an attacker compromises a dependency used by many downstream projects, allowing malicious code to spread. The satire uses exaggerated but plausible scenarios to illustrate how easy it is to slip a malicious crate into the dependency tree.

<details><summary>References</summary>
<ul>
<li><a href="https://crates.io/">crates .io: Rust Package Registry</a></li>
<li><a href="https://doc.rust-lang.org/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html">Packages , Crates , and Modules - The Rust Programming Language</a></li>

</ul>
</details>

**Discussion**: Commenters initially mistook the article for real, which shows its realism. They highlighted specific technical details like the list of crates that could be compromised, and appreciated the satirical elements such as the maintainer receiving a fake YubiKey and the fish shell being called not malware. The overall sentiment is positive, with recognition of the serious underlying message.

**Tags**: `#supply-chain security`, `#Rust`, `#software security`, `#satire`, `#CVE`

---

<a id="item-4"></a>
## [AWS Complexity and Lock-in Frustrations Resurface](http://fourlightyears.blogspot.com/2026/05/i-returned-to-aws-and-was-reminded-hard.html) ⭐️ 7.0/10

A developer returning to AWS after a hiatus details frustrations with its complexity, unpredictable pricing, and data transfer obstacles, reigniting debate on cloud vendor lock-in. This article highlights persistent pain points in cloud computing and the ethical tensions around AWS's approach to open source, affecting developers, startups, and enterprises evaluating cloud strategies. The author criticizes AWS's data egress process, which can take a month and require extensive justification, and points to AWS's cloning of open source projects like Elasticsearch, Redis, and MongoDB into services like OpenSearch, Valkey, and DocumentDB.

hackernews · andrewstuart · May 9, 08:37

**Background**: Cloud vendor lock-in occurs when customers become dependent on a provider's services and face high costs or technical barriers to switch. AWS is the dominant cloud provider, but its complex pricing and data transfer fees have long been criticized. The company has also been accused of exploiting open source projects by offering managed versions without contributing back, leading to new restrictive licenses.

**Discussion**: Commenters offered diverse perspectives: one user described a lengthy and bureaucratic data transfer request process, while another defended AWS, arguing that its complexity is justified for enterprise use and that simple CRUD apps are not the target audience. Others criticized AWS's open source cloning practices, noting that it forced projects to adopt defensive licenses.

**Tags**: `#AWS`, `#cloud computing`, `#open source`, `#vendor lock-in`, `#data egress`

---

<a id="item-5"></a>
## [Maryland Residents Hit with $2B Grid Upgrade for Out-of-State AI](https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises) ⭐️ 7.0/10

Maryland citizens are being charged $2 billion for power grid upgrades needed to support AI data centers located outside the state, prompting the state to complain to federal energy regulators about broken promises on ratepayer protection. This case highlights a growing conflict between the expansion of AI infrastructure and fair cost allocation, potentially setting a precedent for how grid upgrade costs are distributed across states and ratepayers. The grid upgrades are required to serve out-of-state AI data center loads, yet the costs are being passed on to Maryland residents through their electricity bills, despite previous pledges to protect ratepayers from such expenses.

hackernews · lemonberry · May 10, 21:16

**Background**: Power grid upgrades are typically paid for by all ratepayers in a region, but when new large loads like data centers cause the need for major infrastructure investments, the question arises whether those costs should be borne by the specific beneficiaries or spread across the entire customer base. Maryland's complaint to federal regulators argues that the current cost allocation breaks earlier pledges to protect ratepayers. AI data centers consume enormous amounts of electricity, often requiring new transmission lines and substations.

**Discussion**: Commenters express frustration that large corporations can override local regulators, with one noting similar situations in Nevada. Others question whether the charges are solely due to data centers or also from other load growth like housing and EVs, and debate the fairness of fixed infrastructure fees versus usage-based pricing.

**Tags**: `#AI infrastructure`, `#energy policy`, `#data centers`, `#regulation`, `#grid modernization`

---

<a id="item-6"></a>
## [Joanna Rutkowska Launches Personal Blog on Rationality vs Humanism](https://tracesofhumanity.org/hello-world/) ⭐️ 6.0/10

Joanna Rutkowska, the renowned security researcher known for the Blue Pill attacks, has launched a new personal blog titled 'Traces Of Humanity' where she intends to document her struggles between rationality and humanism, pragmatism and beauty, and other dichotomies. This launch is significant because Rutkowska is a highly influential figure in computer security, and her shift to writing about personal philosophical struggles may offer unique insights from someone with a technical background, potentially fostering discussion at the intersection of technology and human values. The blog's first post is a personal manifesto rather than a technical piece; it does not announce any new security research or project. Comments on the community site show some readers are confused about the context, while others welcome her return to writing.

hackernews · alex77456 · May 10, 17:15

**Background**: Joanna Rutkowska is best known for her 'Blue Pill' rootkit demonstration in 2006, which used hardware virtualization to create an undetectable hypervisor-based rootkit, subverting the operating system. This work highlighted that hardware virtualization was not a panacea for security. She later founded the security research firm Invisible Things Lab and has been a prominent voice in OS security. Her new blog marks a departure from technical topics toward personal and philosophical reflections.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blue_Pill_(software)">Blue Pill (software) - Wikipedia</a></li>
<li><a href="https://www.forbes.com/sites/daveywinder/2024/11/27/is-your-router-in-the-matrix-35-million-devices-under-blue-pill-attack/">Are You Already In The Matrix—35 Million Devices Under Blue ...</a></li>

</ul>
</details>

**Discussion**: The community reactions are mixed: some users express confusion about the blog's purpose, while others welcome her warmly and express interest in future posts. One user asks why she left the computer security industry, and another notes her influential background for those unfamiliar with her work.

**Tags**: `#security research`, `#Joanna Rutkowska`, `#personal blog`, `#community discussion`

---