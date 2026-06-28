---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 22 items, 8 important content pieces were selected

---

1. [First Public macOS Kernel Memory Corruption Exploit on Apple M5](#item-1) ⭐️ 9.0/10
2. [Removing Modem and GPS from 2024 RAV4 Hybrid](#item-2) ⭐️ 8.0/10
3. [Antirez Announces DwarfStar4 for Local DeepSeek 4 Inference](#item-3) ⭐️ 8.0/10
4. [M4 MacBook Air Gains RTX 5090 via eGPU](#item-4) ⭐️ 8.0/10
5. [New Nginx Exploit Enables Code Execution with Rewrite/Set](#item-5) ⭐️ 8.0/10
6. [arXiv Plans 1-Year Ban for Hallucinated References](#item-6) ⭐️ 8.0/10
7. [Codex Now Free in ChatGPT Mobile App](#item-7) ⭐️ 7.0/10
8. [HDD Firmware Reverse Engineering Exposes Weak Obfuscation](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [First Public macOS Kernel Memory Corruption Exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Security research firm Calif published the first public kernel memory corruption exploit targeting Apple's M5 chip, demonstrating a bypass of the hardware-based Memory Tagging Extension (MTE) security feature. This is a major security finding against Apple's latest chip, showing that even hardware defenses like MTE can be circumvented. It could significantly impact macOS security research, bug bounty valuations, and the broader effort to make memory corruption attacks harder. The exploit avoids MTE's tagging checks, but the researchers have not yet disclosed full technical details and expect to release a 55-page technical report. Community speculation suggests the bug could be valued between $100,000 and $1.5 million on Apple's bug bounty platform, depending on how it is demonstrated.

hackernews · quadrige · May 14, 18:25

**Background**: Memory Tagging Extension (MTE) is an ARM specification from 2019 that helps detect memory corruption bugs at the hardware level by assigning tags to memory allocations. Apple has been integrating MTE into its latest M5 chip and other devices to improve memory safety. A kernel memory corruption exploit can allow an attacker to gain elevated privileges or bypass security boundaries within the operating system. The M5 is Apple's newest processor, featuring enhanced security measures like MTE to protect against such attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory safety in...</a></li>
<li><a href="https://support.apple.com/en-ph/guide/security/sec8b776536b/web">Operating system integrity - Apple Support (PH)</a></li>

</ul>
</details>

**Discussion**: Comments show a mix of excitement, skepticism, and curiosity. Some users are eager to read the upcoming 55-page report, while others note the lack of detailed disclosure and question how the exploit bypassed MTE. There is also discussion about the potential bug bounty value and some sarcastic remarks about fabricated vulnerabilities.

**Tags**: `#kernel exploit`, `#Apple M5`, `#macOS security`, `#memory corruption`, `#MTE`

---

<a id="item-2"></a>
## [Removing Modem and GPS from 2024 RAV4 Hybrid](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

A detailed technical guide published on May 13, 2026, provides step-by-step instructions for physically removing the Data Communication Module (DCM) and GPS antenna from a 2024 Toyota RAV4 Hybrid to prevent vehicle telemetry data transmission. This guide highlights the escalating tension between consumer privacy and automotive telematics, empowering owners to take physical control of their vehicle's data. It also prompts broader discussions about automakers' data collection practices and the difficulty of opting out of telemetry sharing. The author notes that even after removing the modem, connecting a phone via Bluetooth allows the car to use the phone's internet connection to send telemetry data, whereas a wired USB connection avoids this. Additionally, both CarPlay and Android Auto themselves collect vehicle telemetry.

hackernews · arkadiyt · May 14, 17:08

**Background**: Modern vehicles like the 2024 RAV4 are equipped with a Data Communication Module (DCM) that uses cellular connectivity to transmit telemetry data — including location, driving behavior, and diagnostics — to the manufacturer. Concerns arise because this data may be shared with third parties, such as insurance companies, often without explicit owner consent. Physically disabling the DCM is an extreme measure for owners seeking full privacy, as standard opt-out options are often limited or unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rav4world.com/threads/where-is-the-telemetry-device-that-communicates-with-the-app.330240/">Where is the telemetry device that communicates with the app? - Toyota RAV4 Forums</a></li>
<li><a href="https://www.toyotanation.com/threads/how-to-turn-off-sharing-data-with-toyota.1699485/">How To Turn Off Sharing Data With Toyota? | Toyota Forum</a></li>

</ul>
</details>

**Discussion**: Commenters offer additional insights: one warns that Bluetooth still enables data transmission through the phone, while another notes that the Ford Maverick has a single fuse for the telematics unit whose removal does not trigger errors. Another clarifies that Toyota shares driving data with insurers only if the owner is opted into a program, often inadvertently during dealer setup.

**Tags**: `#privacy`, `#automotive`, `#telemetry`, `#Toyota`, `#IoT`

---

<a id="item-3"></a>
## [Antirez Announces DwarfStar4 for Local DeepSeek 4 Inference](https://antirez.com/news/165) ⭐️ 8.0/10

Antirez released DwarfStar4 (DS4), a compact LLM inference runtime specifically designed for DeepSeek 4, supporting Metal and CUDA backends and targeting hardware with at least 96GB of VRAM. This project brings high-quality local LLM inference to powerful consumer hardware, potentially reducing reliance on cloud APIs and enabling privacy-preserving AI applications on MacBooks and NVIDIA DGX Spark systems. DS4 currently requires 96GB of VRAM and primarily supports Metal (for Apple Silicon) and CUDA (for NVIDIA), with separate ROCm support maintained by the community due to antirez's lack of direct hardware access.

hackernews · caust1c · May 14, 22:29

**Background**: DwarfStar4 is an inference runtime, a lightweight software layer that runs large language models locally without a cloud connection. DeepSeek 4 is a recent large language model from Chinese AI lab DeepSeek, known for high performance and efficiency. The project builds on previous work like llama.cpp and GGML, which pioneered efficient local LLM inference.

<details><summary>References</summary>
<ul>
<li><a href="https://forums.developer.nvidia.com/t/fully-custom-cuda-native-deepseek-4-flash-optimized-for-1x-spark-antirez-ds4/369791">Fully custom CUDA-native Deepseek 4 Flash optimized for 1x Spark! antirez/ds4</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 : 1T Parameter AI Model Guide | Independent DeepSeek ...</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about DS4's performance, with one user noting it feels close to Claude in quality but slower, and another highlighting that imatrix quantization appears superior to backends on OpenRouter. There is optimism about the trajectory of local models, with questions about whether similar intelligence might run on 16GB hardware in a few years.

**Tags**: `#LLM inference`, `#local AI`, `#DeepSeek`, `#DwarfStar`, `#antirez`

---

<a id="item-4"></a>
## [M4 MacBook Air Gains RTX 5090 via eGPU](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

A blog post demonstrates running an RTX 5090 as an external GPU on an M4 MacBook Air, successfully enabling Windows game play and significantly improving LLM prompt processing speeds. This achievement contradicts Apple's official stance that eGPUs are not supported on Apple Silicon, and it opens up GPU-intensive gaming and AI inference for Mac users who previously lacked such options. The setup relies on a virtual machine with GPU passthrough, but it still faces limitations such as a restricted 1.5 GB memory window and no official Apple support.

hackernews · allenleee · May 14, 15:47

**Background**: An eGPU is an external graphics processing unit that connects to a computer to boost graphical performance, commonly used with laptops lacking powerful internal GPUs. Apple has officially stated that eGPUs only work with Intel-based Macs and only with AMD GPUs, not NVIDIA. This community-driven hack bypasses those restrictions on Apple Silicon Macs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lenovo.com/us/en/glossary/external-gpu/">What is an external graphics processing unit (GPU)?</a></li>
<li><a href="https://biztechmagazine.com/article/2022/08/what-external-graphics-processing-unit-perfcon">What Is an External Graphics Processing Unit (eGPU) and How Does it Boost Performance?</a></li>

</ul>
</details>

**Discussion**: Community members expressed surprise and admiration at the workaround, with one VM developer noting they had requested GPU passthrough for years. Many highlighted the LLM performance gains as the most practical benefit, though some pointed out remaining limitations like the small memory window and lack of official support.

**Tags**: `#eGPU`, `#Apple Silicon`, `#Mac Gaming`, `#LLM`, `#RTX 5090`

---

<a id="item-5"></a>
## [New Nginx Exploit Enables Code Execution with Rewrite/Set](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

A new Nginx exploit named Nginx-Rift has been published on GitHub, demonstrating potential code execution when a rewrite directive containing a question mark is followed by a set directive referencing a numbered regex capture group. The vulnerability has been assigned CVE-2026-42945 and patched in Nginx versions 1.31.0 and 1.30.1. This exploit is significant because Nginx powers a large portion of the internet's web servers; however, the exploit requires specific configuration conditions and ASLR protection mitigates the published proof-of-concept, though the author claims a reliable ASLR bypass exists. The exploit requires a rewrite directive with a question mark in the replacement string and a subsequent set directive that references a numbered regex capture group (e.g., set $var $1). The published proof-of-concept assumes ASLR is disabled, and the official mitigation is to use named captures instead of unnamed captures in rewrite rules.

hackernews · hetsaraiya · May 14, 17:17

**Background**: Nginx is a widely used open-source web server and reverse proxy. Its rewrite module processes URL rewriting using regular expressions, where captured groups can be referenced as $1, $2, etc. The set directive assigns values to Nginx variables. This vulnerability, which has existed for 18 years, exploits memory corruption in the rewrite module's handling of PCRE captures. ASLR (Address Space Layout Randomization) is a defense-in-depth technique that randomizes memory addresses to make exploitation more difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/18-year-old-nginx-vulnerability-allows-dos-potential-rce/">18-year-old NGINX vulnerability allows DoS, potential RCE - Bleeping Computer</a></li>
<li><a href="https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html?m=1">18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated RCE</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that while the published PoC requires ASLR to be disabled, the author claims a reliable ASLR bypass exists, which security practitioners should take seriously. Others discuss the specific preconditions (rewrite with ? and set with $1) and note that F5 recommends using named captures as a mitigation. One user asks about memory-safe alternatives like Caddy and Jetty, but expresses skepticism about their security records.

**Tags**: `#security`, `#nginx`, `#exploit`, `#vulnerability`, `#cve`

---

<a id="item-6"></a>
## [arXiv Plans 1-Year Ban for Hallucinated References](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv announced a new policy that bans authors for one year if they submit papers containing AI-hallucinated references, and requires subsequent submissions to be accepted at a reputable peer-reviewed venue before being posted on arXiv. This policy directly addresses the growing problem of AI-generated false citations polluting the scientific literature, which a Nature analysis estimates could affect tens of thousands of publications in 2025. It upholds academic integrity and places responsibility on authors to verify AI-generated content. The ban applies to the submitting author, and after the ban, future submissions must first be accepted at a reputable peer-reviewed venue. The policy appears to be planned but not yet live, as it is not clearly listed on arXiv's policies page.

hackernews · gjuggler · May 14, 20:39

**Background**: Hallucinated references are false or nonexistent citations generated by large language models (LLMs), which can fabricate author names, paper titles, and publication details. This issue has become widespread as researchers increasingly use AI tools like ChatGPT to assist in writing papers. A Nature analysis found that tens of thousands of publications from 2025 might include such invalid references, and even top conferences like NeurIPS have reported hallucinated citations in accepted papers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific literature. What can be done? - Nature</a></li>

</ul>
</details>

**Discussion**: The community broadly supports the policy, with commenters praising it as 'incredibly good for science' and noting that arXiv is a privilege. Some express concerns about careful vetting before imposing bans, such as whether accidental inclusions without permission could lead to penalties. Others note that LLM proponents are angry about any hindrance to rapid AI adoption.

**Tags**: `#arXiv`, `#academic integrity`, `#AI-generated content`, `#hallucinated references`, `#scientific publishing`

---

<a id="item-7"></a>
## [Codex Now Free in ChatGPT Mobile App](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 7.0/10

OpenAI has made Codex, its AI coding assistant, available for free within the ChatGPT mobile app, allowing users to code with AI assistance directly from their smartphones. This move significantly lowers the barrier to AI-assisted coding by making it accessible on mobile devices without a paid subscription, potentially boosting developer productivity on the go and expanding the user base for AI coding tools. Codex in the ChatGPT mobile app is included in the free plan, though interactions may be used for model training. The feature also works on the desktop app and CLI, but Linux support for the app is still absent, and the mobile experience may be less effective without a keyboard.

hackernews · mikeevans · May 14, 20:06

**Background**: Codex is an AI model by OpenAI that translates natural language into code, originally powering GitHub Copilot. The ChatGPT mobile app already offered general chat capabilities, and this update integrates Codex directly into that interface, allowing users to write and debug code on the go. The free plan includes usage limitations and data usage for training.

**Discussion**: Community members expressed surprise and appreciation that Codex is free, with some noting they had expected to pay. However, several users reported mixed results on mobile, citing the smaller screen and lack of keyboard as limiting factors for effective coding. Others discussed integration challenges, such as the absence of Linux support for the desktop app and difficulties with remote repository access.

**Tags**: `#OpenAI`, `#Codex`, `#ChatGPT`, `#AI coding`, `#mobile app`

---

<a id="item-8"></a>
## [HDD Firmware Reverse Engineering Exposes Weak Obfuscation](https://icode4.coffee/?p=1465) ⭐️ 7.0/10

A detailed blog post series demonstrates how to dump, analyze, and modify hard drive firmware, exposing trivial obfuscation techniques used by vendors and providing practical exploitation methods including JTAG debugging. This work highlights the security fragility of hard drive firmware, which if compromised can give attackers persistent, hard-to-detect control; it also empowers security researchers and data recovery specialists to better understand and protect embedded storage systems. The author dumps firmware via JTAG, reverse-engineers the code without AI, and shows that vendor obfuscation is easily bypassed—for example, one utility decrypts firmware before uploading, and a simple seccomp filter can capture the decrypted version.

hackernews · jsploit · May 14, 16:19

**Background**: Hard drive firmware is low-level software that controls the internal operations of a drive. Reverse engineering it often requires specialized hardware like JTAG debuggers and knowledge of embedded systems. Previous work, including SpritesMods' HDD hack and the malwaretech series, have explored similar territory, while NSA documents have confirmed that firmware can be used for persistent espionage.

<details><summary>References</summary>
<ul>
<li><a href="https://icode4.coffee/?p=1465">HDD Firmware Hacking Part 1 – I Code 4 Coffee</a></li>
<li><a href="https://malwaretech.com/2015/04/hard-disk-firmware-hacking-part-1.html">Hard Disk Firmware Hacking (Part 1)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Obfuscation_(software)">Obfuscation (software) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters shared real-world examples, such as Samsung SSD firmware decompilation and a trivial bypass using seccomp; one noted the article could be useful for interview CTF challenges, while another linked to related NSA firmware hacking disclosures.

**Tags**: `#firmware`, `#reverse-engineering`, `#hard-drive`, `#security`, `#embedded-systems`

---