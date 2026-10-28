---
layout: default
title: "Horizon Summary: 2026-10-28 (EN)"
date: 2026-10-28
lang: en
---

> From 41 items, 18 important content pieces were selected

---

**Technology News**
1. [OpenAI Releases Three Model-Generated Math and Complexity Results for External Validation](#item-tech-news-1) ⭐️ 9.0/10
2. [Google DeepMind Releases Genie 4 World Simulation Model](#item-tech-news-2) ⭐️ 8.0/10
3. [Apple Introduces 14-inch MacBook Pro with M6](#item-tech-news-3) ⭐️ 8.0/10
4. [Classification of Finite Simple Groups Formalized in Lean](#item-tech-news-4) ⭐️ 8.0/10
5. [Chinese Team Claims 3.2 Pb/s Real-Time Optical Fiber Record](#item-tech-news-5) ⭐️ 8.0/10
6. [Google Proposes Sleep Framework for LLMs to Retain Knowledge in Continual Learning](#item-tech-news-6) ⭐️ 8.0/10
7. [Triton 3.9.0 adds atomic load/store and backend improvements](#item-tech-news-7) ⭐️ 7.0/10
8. [Ghostty 1.4 Released with libghostty Progress Highlighted](#item-tech-news-8) ⭐️ 7.0/10
9. [Tailscale SSH vulnerability investigation and remediation update](#item-tech-news-9) ⭐️ 7.0/10
10. [Python&\#x27;s experimental JIT to be removed](#item-tech-news-10) ⭐️ 7.0/10
11. [Amazon Reportedly Scales Back AI Division After Nova Model Failures](#item-tech-news-11) ⭐️ 7.0/10
12. [Papers with Code Revival Now Open-Source Under Apache 2.0](#item-tech-news-12) ⭐️ 7.0/10
13. [Psi-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model](#item-tech-news-13) ⭐️ 7.0/10
14. [Boston Dynamics Employees Petition to Block ICE Robot Dog Sale](#item-tech-news-14) ⭐️ 7.0/10
15. [Microsoft Fixes High-Severity Android Authenticator Vulnerability](#item-tech-news-15) ⭐️ 7.0/10
16. [Anthropic Confirms Researchers Accessed Some Internal Systems, Says Customer Data Unaffected](#item-tech-news-16) ⭐️ 7.0/10
17. [Anthropic Manager Drops Coding Interviews as Claude Outperforms Candidates](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [Pop Mart’s Q3 Revenue Falls 45–50% as Labubu Hype Cools](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI Releases Three Model-Generated Math and Complexity Results for External Validation](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 9.0/10

OpenAI has released three internal model-generated research results: a proof of the local smoothing conjecture in all dimensions, a disproof of the Exponential Time Hypothesis \(ETH\), and an existence proof for 4D Yang-Mills theory. OpenAI describes these results as more like raw research data and is inviting external experts to serve as interpreters and validators; the computer science group publicly released its proof and Lean formalization immediately, while the physics group has withheld its result for now. If verified, these claims would be historic breakthroughs: a false ETH would undermine many lower-bound assumptions in exact, parameterized, and fine-grained complexity research, and a full-dimensional local smoothing proof would also resolve core harmonic-analysis conjectures such as Kakeya and Stein restriction. The 4D Yang-Mills existence result directly targets one of the seven Millennium Prize problems. All three results remain pending external validation.

telegram · zaihuapd · Oct 27, 15:00

**「Background」** The Exponential Time Hypothesis \(ETH\) is a strengthening of P ≠ NP that rules out subexponential-time algorithms for 3-SAT, and many exact, parameterized, and fine-grained complexity results depend on it. The local smoothing conjecture is a central problem in harmonic analysis whose proof in all dimensions would settle the Kakeya and restriction conjectures. The Yang–Mills existence and mass gap problem is one of the seven Clay Millennium Prize Problems; the announced result claims existence in four dimensions but does not mention the mass gap.

**「Impact」** If the reported results are verified, researchers relying on ETH-based lower bounds would need to revisit foundational assumptions in fine-grained complexity, and the Yang-Mills result would resolve a Millennium Prize problem; however, all claims are currently unverified and await external confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/building-scientific-understanding-with-academic-communities/">Working with academic communities to build scientific ... | OpenAI</a></li>
<li><a href="https://gizmodo.com/openai-trumpets-3-more-math-and-science-results-along-with-a-new-plan-for-publishing-them-2000830956">OpenAI Trumpets 3 More Math and Science Results, Along With...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#theoretical computer science`, `#mathematics`, `#AI research`, `#formal verification`

---

<a id="item-tech-news-2"></a>
### [Google DeepMind Releases Genie 4 World Simulation Model](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) ⭐️ 8.0/10

Google DeepMind has introduced Genie 4, a world simulation model that generates interactive video and audio from text prompts. The release describes a new generation of world simulation focused on real-time interaction and scene editing. Early demonstrations show notable progress in maintaining in-frame consistency, but some examples reveal limitations such as objects changing after leaving the frame and audio mismatches.

hackernews · acossta · Oct 27, 16:06 · [Discussion](https://news.ycombinator.com/item?id=50261319)

**「What is Genie 4?」** World models are AI systems that generate interactive simulated environments from natural-language prompts, letting users steer actions and camera in real time. Google DeepMind has been developing the Genie line of world models, and Genie 4 is the latest iteration, introducing native audio and more photorealistic, physics-aware worlds. According to a TechCrunch report, it was released in research preview on Tuesday, following earlier DeepMind research on real-time interactive simulation.

**「Impact」** Project Genie Ultra subscribers and Gemini API/AI Studio partners are expected to gain access after the research preview, but early examples show object persistence and audio mismatches that may limit reliability for real-time interactive use.

**「Community Discussion」** Commenters generally acknowledge Genie 4&\#x27;s in-frame consistency but flag clear limitations: out-of-frame changes cause object duplication or appearance shifts, and audio can mismatch the prompt \(e.g., a saxophone prompt yields a clarinet sound\). Some also note that photorealistic prompts can produce game-like output and point out that Tencent&\#x27;s open-weight HY-World 2.0 received less attention.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">Genie 4: A new generation of world simulation — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/">We’re announcing Genie 4, our new world model for real-time ...</a></li>
<li><a href="https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/">Google’s Genie 4 world model adds audio, more realistic ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#world models`, `#deepmind`, `#generative video`, `#simulation`

---

<a id="item-tech-news-3"></a>
### [Apple Introduces 14-inch MacBook Pro with M6](https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/) ⭐️ 8.0/10

Apple has introduced a new 14-inch MacBook Pro powered by the M6 chip, with presales starting October 28, 2026 and shipping expected November 6. The entry-level configuration is priced at $1,999 with 16GB of memory, matching the previous M5 model&\#x27;s starting price. Apple describes the M6 as its first 2nm chip, moving from a 10-core to a 12-core CPU for up to 1.2x multithreaded performance, paired with a 12-core GPU and dual 16-core Neural Engines for lower power consumption. This update brings next-generation Apple Silicon to a more affordable MacBook Pro tier for developers and professionals.

hackernews · beex · Oct 27, 16:08 · [Discussion](https://news.ycombinator.com/item?id=50261352)

**「Background」** The 14-inch MacBook Pro is part of Apple&\#x27;s pro laptop lineup powered by Apple Silicon, with previous generations using M-series chips like M1 through M5. The M6 is Apple&\#x27;s first chip built on a 2nm process, upgrading the base 14-inch MacBook Pro while M6 Pro and M6 Max variants are not introduced in this announcement. This standard M6 model starts at $1,999 with 16GB of memory and 1TB of storage, with pre-orders opening October 28 and availability beginning November 6.

**「Impact」** Developers and professionals who buy the entry-level 14-inch MacBook Pro get a same-price upgrade to 2nm M6 silicon with 12 CPU cores, a 12-core GPU, and stronger on-device AI acceleration, without needing to move to a higher-cost model.

**「Community Discussion」** Commenters are generally hesitant: several say they will keep using older M1 hardware or wait for M7 Pro/Max, citing high prices and confusing naming between base M-series and previous-generation Pro/Max chips. Others call for standardized offline AI performance metrics or express hope for better AAA game support on MacBooks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/">Apple introduces the new 14-inch MacBook Pro with M6</a></li>
<li><a href="https://applescoop.org/story/m6-14-inch-macbook-pro-price-release-date-specs-features">M6 MacBook Pro: price, release date, specs and every new feature</a></li>
<li><a href="https://www.macworld.com/article/3203946/m6-macbook-pro-rumors-release-date-specs.html">M6 MacBook Pro Guide: Release date, specs, price | Macworld</a></li>

</ul>
</details>

**Tags**: `#apple`, `#hardware`, `#macbook-pro`, `#apple-silicon`, `#technology-industry`

---

<a id="item-tech-news-4"></a>
### [Classification of Finite Simple Groups Formalized in Lean](https://cfsg.axiommath.ai/) ⭐️ 8.0/10

The Classification of Finite Simple Groups \(CFSG\), a central result in abstract algebra, has been formalized in the Lean proof assistant, according to a project page at cfsg.axiommath.ai. The formalization represents a landmark in proof assistant technology and durable mathematical software libraries. Community discussion notes that the work identified and repaired one gap in the previously accepted proof, which spanned more than 1,000 pages. The original classification was a collaboration of roughly 100 mathematicians, and earlier efforts had occasionally missed classes or sporadic groups.

hackernews · pfdietz · Oct 27, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50261647)

**「Background」** Lean is a proof assistant and a functional programming language based on the calculus of constructions with inductive types, which permits mathematical proofs to be expressed and machine-checked. The Classification of Finite Simple Groups is a central theorem in abstract algebra whose first-generation proof is exceptionally long and complex; the formalization at cfsg.axiommath.ai follows this first-generation proof, with every logical step verified by Lean&\#x27;s kernel.

**「Impact」** The Lean formalization of the Classification of Finite Simple Groups provides a machine-checked verification of the first-generation proof, eliminating reliance on human-checked mathematics and enabling the result to be reused as a trusted foundation in formal mathematics libraries.

**「Community Discussion」** Commenters highlighted that the formalization uncovered and repaired a gap in the previously accepted 1,000+ page proof, with one noting the original classification involved around 100 mathematicians. Others debated whether large language models could auto-formalize all math textbooks and lamented the continued use of set-theoretic rather than homotopical foundations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean ( proof assistant ) - Wikipedia</a></li>
<li><a href="https://cfsg.axiommath.ai/">CFSG in Lean</a></li>
<li><a href="https://cfsg.axiommath.ai/">CFSG in Lean</a></li>
<li><a href="https://mozgi.io/news/auto-mvqzshz6-zvaz/?lang=en">AxiomMath has formally verified the classification of finite simple ...</a></li>

</ul>
</details>

**Tags**: `#formal verification`, `#Lean`, `#proof assistant`, `#mathematics`, `#finite simple groups`

---

<a id="item-tech-news-5"></a>
### [Chinese Team Claims 3.2 Pb/s Real-Time Optical Fiber Record](https://www.tomshardware.com/networking/3-2-pb-s-real-time-optical-fiber-transfer-speed-world-record-claimed-by-chinese-team-speed-fast-enough-to-download-more-than-20-000-4k-movies-in-one-second) ⭐️ 8.0/10

A Chinese research team claims a real-time optical fiber transmission record of 3.2 Pb/s using 24-core fiber and S+C+L multi-band transmission, enough to transfer more than 20,000 4K movies in one second. The result exceeds the team’s earlier 2.5 Pb/s record by nearly 30 percent. The test used a commercially compatible hardware architecture and verified spatial division multiplexing and multi-band transmission techniques. For comparison, a laboratory fiber transmission record of 5.29 Pb/s has been reported using advanced or experimental equipment and signal processing.

telegram · zaihuapd · Oct 27, 03:45

**「Background」** Real-time transmission records differ from laboratory experiments because they use hardware that can operate continuously rather than specialized experimental setups. Spatial division multiplexing uses multiple cores within a single fiber, while S+C+L multi-band transmission combines multiple wavelength bands to increase capacity. These techniques are being explored to meet growing backbone bandwidth demand.

**Tags**: `#optical networking`, `#fiber optics`, `#high-speed data transmission`, `#hardware`, `#networking infrastructure`

---

<a id="item-tech-news-6"></a>
### [Google Proposes Sleep Framework for LLMs to Retain Knowledge in Continual Learning](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research has introduced a sleep framework that adds an offline sleep phase to continual learning for large language models. During this phase, the model consolidates short-term context into long-term parameters, helping to mitigate catastrophic forgetting. The system alternates periodically between active interaction and offline consolidation. In reported tests, it outperformed GPT-4 and supervised fine-tuning baselines on tasks including 10-million-token long-context processing, continual translation, and mathematical reasoning.

telegram · zaihuapd · Oct 28, 01:46

**「Background」** Large language models are typically frozen after pre-training and fine-tuning, retaining only knowledge encoded during those stages; in-context learning uses a limited context window without updating model parameters. Continual learning aims to let models integrate new information sequentially, but direct updates risk catastrophic forgetting of prior knowledge. Google Research&\#x27;s sleep framework addresses this by adding an offline consolidation phase in which recent short-term context is converted into long-term parameters, inspired by biological sleep.

**「Impact」** For AI/ML practitioners building continually learning LLMs, this framework offers a replication target because Google reports it outperformed GPT-4 and supervised fine-tuning baselines on long-context, continual translation, and math reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/">The sleep framework: A new way for LLMs to retain knowledge ...</a></li>
<li><a href="https://alphasignal.ai/news/google-s-sleep-framework-lets-ai-models-keep-learning-without-forgetting">Google&#x27;s Sleep Framework Lets AI Models Keep Learning Without ...</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#large language models`, `#catastrophic forgetting`, `#Google Research`, `#machine learning`

---

<a id="item-tech-news-7"></a>
### [Triton 3.9.0 adds atomic load/store and backend improvements](https://github.com/triton-lang/triton/releases/tag/v3.9.0) ⭐️ 7.0/10

Triton v3.9.0 introduces atomic memory operations: new \`tl.atomic\_load\` and \`tl.atomic\_store\` operations, with loads defaulting to acquire and stores defaulting to release, as well as \`tl.atomic\_poll\`, which waits until a pointer&\#x27;s value matches an expected value and returns \`False\` on timeout. The release also adds approximate FP32 division via \`tl.fdiv\(..., approx=True\)\`, chained comparisons, keyword-only parameters, and integer \`tl.clamp\`. Compiler improvements include an LLVM update to commit b010a18d, a rewritten barrier insertion pass, CTA-wide barriers for acquire/release atomics, and up to 40x faster batched MMAv2 dots on NVIDIA. Fixes address wrong results in reductions, scans, softmax, unaligned TMA, and multi-CTA synchronization, and change E8M0 scale decoding so \`0x00\` maps to \`2^-127\` and \`0xFF\` to NaN.

github · warrendeng · Oct 27, 18:56

**「Background」** Triton is an open-source language and compiler designed for writing high-performance GPU kernels, widely adopted in machine learning and scientific computing. It translates Python-like Triton code into optimized low-level GPU instructions through a pipeline of optimization passes.

**「Impact」** For Triton kernel developers, v3.9.0 provides new synchronization primitives and can substantially accelerate batched matmul workloads on NVIDIA, but existing code may need updates because E8M0 scale decoding changed and read-modify-write/CAS atomics now default to \`acq\_rel\` semantics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/triton-kernels">Triton Kernels : High-Performance GPU Programming</a></li>
<li><a href="https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html">Unlock Peak Performance on AMD GPUs with Triton Kernel ...</a></li>

</ul>
</details>

**Tags**: `#compiler`, `#gpu`, `#machine-learning`, `#open-source`, `#software-engineering`

---

<a id="item-tech-news-8"></a>
### [Ghostty 1.4 Released with libghostty Progress Highlighted](https://ghostty.org/docs/install/release-notes/1-4-0) ⭐️ 7.0/10

Ghostty 1.4 has been released, with release notes focused on GUI changes but highlighting libghostty progress since version 1.3. libghostty is described as a highly portable, embeddable library providing core terminal emulation, render state, and more, and project lead Mitchell Hashimoto states it was his primary goal for the project. The supplied source content is unavailable, so specific technical changes in 1.4 cannot be independently verified. Community discussion includes feature requests such as Kitty&\#x27;s hints mode, a reported bug where the find textbox does not respect keyboard shortcuts, and comparisons with Kitty, WezTerm, Konsole, and iTerm2.

hackernews · deaux · Oct 27, 16:51 · [Discussion](https://news.ycombinator.com/item?id=50261998)

**「Background」** Ghostty is a fast, feature-rich, cross-platform terminal emulator developed as an open-source project. Its 1.4.0 release notes, published on October 27, 2026, note that libghostty—the embeddable library providing core terminal emulation and render state—is not directly part of the 1.4 release, but the 1.4 development cycle included substantial work on it. The previous 1.3.1 patch release from March 2026 focused on regression fixes, primarily for macOS, indicating an active release cadence.

**「Impact」** Developers evaluating Ghostty may delay adoption due to missing hints-mode functionality and the find-textbox shortcut bug, as noted by commenters, though the full release scope remains unconfirmed.

**「Community Discussion」** Commenters show mixed reception: Mitchell Hashimoto emphasizes libghostty as the project&\#x27;s true purpose, while others cite missing features like Kitty hints mode, a find dialog shortcut bug, and question speed or feature advantages over Konsole and iTerm2.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/docs/install/release-notes/1-4-0">Release notes for Ghostty 1 . 4 .0, released on October 27, 2026.</a></li>
<li><a href="https://releasebot.io/updates/ghostty">Ghostty Release Notes - March 2026 Latest Updates - Releasebot</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>

</ul>
</details>

**Tags**: `#terminal emulator`, `#open source`, `#software development tools`, `#libghostty`, `#ghostty`

---

<a id="item-tech-news-9"></a>
### [Tailscale SSH vulnerability investigation and remediation update](https://tailscale.com/ssh-investigation-update) ⭐️ 7.0/10

Tailscale has published an investigation and remediation update for SSH vulnerabilities affecting configurations that use Tailscale SSH with ACLs. The issue does not affect standard OpenSSH services or users who lack Tailscale SSH access and connectivity to the affected node. According to a community reviewer, the vulnerability only matters when ACLs grant Tailscale SSH access but do not provide a path to sudoers or root. The update addresses the vulnerable Tailscale SSH implementation; users should review their ACLs and apply the recommended remediations.

hackernews · figmert · Oct 27, 19:55 · [Discussion](https://news.ycombinator.com/item?id=50264857)

**「Background」** Tailscale is a mesh VPN service built on WireGuard that connects an organization&\#x27;s devices over a private peer-to-peer network. Tailscale SSH is a feature that lets approved devices log in to each other over that network, with access governed by ACLs. External reports describe newly disclosed vulnerabilities in Tailscale SSH that could allow an attacker with already-approved network access to escalate privileges to root on connected servers, and Tailscale is preparing patches and mitigations.

**「Impact」** Organizations using Tailscale SSH with ACLs should apply the vendor&\#x27;s remediation promptly, because the ACL misconfiguration can allow privilege escalation on devices where a user has Tailscale SSH access but no predefined root or sudoers path.

**「Community Discussion」** Commenters debated whether Tailscale SSH should be used at all: some recommend disabling it in favor of stock OpenSSH, arguing it adds attack surface and introduces a single point of failure, while others want a lockdown mode that disables risky features. A former Tailscale employee clarifies the vulnerability only affects ACL-granted Tailscale SSH without a root or sudo path.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/tailscale-warns-of-serious-ssh-flaws-allowing-root-privilege-escalation/">Tailscale warns of SSH flaws allowing root privilege escalation</a></li>
<li><a href="https://tailscale.com/security-bulletins">Security Bulletins - Tailscale Tailscale SSH Vulnerabilities Let Attackers Gain Root Access ... Tailscale is patching SSH flaws that can exceed local user ... Tailscale Rushes Patches After Uncoordinated Disclosure of ... Tailscale SSH Flaws Could Let Hackers Gain Root Access Across ... Tailscale SSH: Investigation and remediation update</a></li>
<li><a href="https://cyberpress.org/tailscale-ssh-vulnerabilities/">Tailscale SSH Vulnerabilities Let Attackers Gain Root Access ...</a></li>
<li><a href="https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html">Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach...</a></li>
<li><a href="https://tamiz.pro/insights/securing-ssh-tailscale-ts-2026-009-lessons-learned">Securing SSH on Tailscale : Lessons from Critical Vulnerability ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#tailscale`, `#ssh`, `#vulnerability`, `#networking`

---

<a id="item-tech-news-10"></a>
### [Python&\#x27;s experimental JIT to be removed](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/) ⭐️ 7.0/10

CPython&\#x27;s experimental copy-and-patch JIT, introduced in Python 3.13, is being removed. The change affects the language&\#x27;s performance roadmap and its free-threading future. The JIT was part of an experimental effort to improve execution speed in the reference implementation. Its removal marks a reversal for CPython&\#x27;s performance work. No specific technical details about the removal timing or replacement strategy are available in the item.

hackernews · f311a · Oct 27, 11:17 · [Discussion](https://news.ycombinator.com/item?id=50257419)

**「Background」** The experimental copy-and-patch JIT was introduced in CPython 3.13 to bring runtime code generation and performance improvements. It worked by extending Python&\#x27;s internal APIs to support pluggable optimizers and could be enabled at build time with the --enable-experimental-jit flag. The JIT was also considered a potential counterbalance to performance penalties from Python&\#x27;s free-threading mode.

**「Impact」** The withdrawal of PEP 836 removes CPython&\#x27;s experimental copy-and-patch JIT, so Python users cannot rely on it for performance gains or to offset free-threading overhead; future JIT efforts must first address compatibility with free-threading, profilers, and debuggers.

**「Community Discussion」** Commenters note that CPython&\#x27;s role as the de facto specification complicates JIT retrofitting, and some express disappointment that the JIT was expected to offset free-threading performance penalties. Others propose explicit Cython-based compilation as a practical alternative, while noting many prior Python JIT experiments have struggled.

<details><summary>References</summary>
<ul>
<li><a href="https://tonybaloney.github.io/posts/python-gets-a-jit.html">Python 3 . 13 gets a JIT</a></li>
<li><a href="https://realpython.com/python313-free-threading-jit/">Python 3 . 13 : Free Threading and a JIT Compiler – Real Python</a></li>
<li><a href="https://softaims.com/blog/python-313-free-threaded-jit-features-2026">Python 3 . 13 Free-Threaded Mode &amp; JIT Guide 2026</a></li>
<li><a href="https://braindetox.kr/en/posts/cpython_experimental_jit_removal_2026.html">CPython experimental JIT leaves main: PEP 836 withdrawn</a></li>
<li><a href="https://github.com/python/cpython/issues/141594">JIT x Free-Threading · Issue #141594 · python/cpython - GitHub</a></li>

</ul>
</details>

**Tags**: `#python`, `#cpython`, `#jit`, `#performance`, `#compiler`

---

<a id="item-tech-news-11"></a>
### [Amazon Reportedly Scales Back AI Division After Nova Model Failures](https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova) ⭐️ 7.0/10

Futurism reports that Amazon is scaling back its internal AI division after sustained difficulties with its Nova models. The company is said to be pivoting toward hosting third-party AI models rather than continuing to invest heavily in its own frontier model development. The report describes a significant strategic shift for the cloud provider, though specific headcount or product details are not included in the available summary. Without the original article text, the extent and exact nature of the cutbacks remain unclear.

hackernews · dpflan · Oct 27, 16:25 · [Discussion](https://news.ycombinator.com/item?id=50261589)

**「Amazon Nova Foundation Models」** Amazon Nova is Amazon&\#x27;s family of in-house foundation models, including Amazon Nova 2 Lite, Amazon Nova Act, and Amazon Nova 2 Sonic, which are accessible through the Nova portal and an API. The reported scaling back of Amazon&\#x27;s AI division concerns this internal model development effort and a possible shift toward hosting third-party models instead.

**「What this means for AWS users」** For AWS customers and developers, Amazon&\#x27;s reported pivot away from its in-house Nova models means they should expect fewer proprietary model improvements and more emphasis on hosting third-party models, custom AI chips, and partnerships, reinforced by hundreds of AWS layoffs tied to AI-driven restructuring.

**「Community Discussion」** Hacker News commenters largely agree that Amazon lacks the engineering talent and innovation culture needed for frontier AI research, and that hosting third-party models is more profitable. One user notes the article was published on July 29, while another describes a hands-on test in which Nova performed markedly worse than Gemini.

<details><summary>References</summary>
<ul>
<li><a href="https://nova.amazon.com/">Amazon Nova</a></li>
<li><a href="https://hrme.economictimes.indiatimes.com/news/industry/amazon-cuts-hundreds-of-jobs-in-aws-amid-ai-driven-restructuring/122762988">Amazon Layoffs: Amazon Cuts Hundreds of Jobs in AWS Amid AI ...</a></li>
<li><a href="https://aiera.blog/amazon-ai-division-changes-what-just-happened-in-2026/">Amazon AI Division Changes: What Just Happened in 2026</a></li>

</ul>
</details>

**Tags**: `#amazon`, `#ai-strategy`, `#amazon-nova`, `#cloud-computing`, `#technology-industry`

---

<a id="item-tech-news-12"></a>
### [Papers with Code Revival Now Open-Source Under Apache 2.0](https://www.reddit.com/r/MachineLearning/comments/1xgoadu/papers_with_code_is_now_opensource_p/) ⭐️ 7.0/10

Papers with Code has been revived as an open-source project under the Apache 2.0 license, with its code available at github.com/huggingface/paperswithcode. The website tracks trending AI research, benchmarks, and state-of-the-art results, serving as a successor to the original Papers with Code that Meta acquired and later shut down. The codebase uses a Python FastAPI backend and React frontend, hosted as a monorepo on a Hetzner VPS, and exposes a public API plus an accompanying MCP server. The project lead, NielsRogge, is opening the repository to community contributions after receiving feature requests, aiming to collaboratively build the best paper interface.

reddit · r/MachineLearning · /u/NielsRogge · Oct 27, 09:54

**「Background」** Papers with Code is a community platform that catalogs AI research papers along with code, models, datasets, benchmarks, and leaderboards. The original paperswithcode.com was retired by Meta in 2025, and this revival recreates that functionality with automated imports from Hugging Face.

**「Impact」** Researchers and developers can now fork or contribute to the repository and use its public API and MCP server to build custom interfaces or integrate paper and benchmark data into their own tools.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huggingface/paperswithcode">GitHub - huggingface / paperswithcode : This repository hosts the...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#machine-learning`, `#research-tools`, `#papers-with-code`, `#hugging-face`

---

<a id="item-tech-news-13"></a>
### [Psi-0.6: Adaptive Streams of Thought in a Unified Vision-Language World Model](https://www.reddit.com/r/MachineLearning/comments/1xgwq9u/%CF%8806_adaptive_streams_of_thought_in_a_unified/) ⭐️ 7.0/10

A research post introduces Psi-0.6, a unified vision-language world model that adaptively reasons through multiple representation streams—text, depth, motion, camera pose, and imagined scenes—rather than relying on word-only chain-of-thought. The authors report that Psi-0.6 surpasses leading open-weight models on zero-shot MindCube spatial reasoning and outperforms other world models on FlowBench for predicting object motion. Trained on simulated rooms, the model transfers to real robot tabletop settings, and reinforcement learning is used to select which representation stream to reason through. The same model serves as perceiver, VLM, world model, reasoner, and policy.

reddit · r/MachineLearning · /u/FaeriaManic · Oct 27, 16:09 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1xgwq9u/%CF%8806_adaptive_streams_of_thought_in_a_unified/)

**「Background」** Chain-of-thought has improved reasoning in large language models but typically remains confined to text tokens. The arXiv abstract and Hugging Face summary describe Ψ-0.6 as a unified vision-language world model that adaptively composes perception, language, geometry, and simulation through interleaved reasoning streams, extending chain-of-thought to non-text modalities such as depth, motion, camera pose, and imagined scenes in order to improve spatial reasoning and counterfactual simulation.

**「Impact」** For spatial reasoning and tabletop robotics developers, this unified model could reduce the need to integrate separate perception, world-model, reasoning, and policy components, provided the reported MindCube, FlowBench, and sim-to-real results are reproducible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.32177">[2610.32177] ||Psi;$-0.6: Adaptive Streams of Thought in a ...</a></li>
<li><a href="https://huggingface.co/papers/2610.32177">Ψ-0.6: Adaptive Streams of Thought in a Unified Vision ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#vision-language models`, `#world models`, `#reinforcement learning`, `#robotics`

---

<a id="item-tech-news-14"></a>
### [Boston Dynamics Employees Petition to Block ICE Robot Dog Sale](https://arstechnica.com/ai/2026/10/boston-dynamics-employees-want-to-block-sale-of-robot-dogs-to-ice/) ⭐️ 7.0/10

Boston Dynamics employees submitted a petition calling on executives to halt a $1.3 million U.S. Immigration and Customs Enforcement \(ICE\) contract for four modified Spot robots intended to detect radiation, gas leaks, and explosives. The petition gathered more than 300 signatures, roughly one-fifth of the company’s 1,400 employees, after the Department of Homeland Security awarded the contract to Connecticut-based Radeco on September 25. Executives defended the deal, stating the robots would not be weaponized and would serve a non-weaponized detection role. The dispute highlights dual-use concerns over government deployment of commercially available robotics and growing tech worker activism on ethical use.

telegram · zaihuapd · Oct 27, 09:52

**「Background」** Boston Dynamics’ Spot is a four-legged robot commonly used for industrial inspection and remote sensing missions. ICE is the U.S. agency responsible for immigration enforcement, and its potential use of robotics has raised civil liberties and weaponization concerns among employees and outside critics.

**「Impact」** If the contract stands, ICE will receive four modified Spot robots for detecting radiation, gas, and explosives, while the petition signals unresolved internal disagreement over Boston Dynamics&\#x27; government sales policy.

**Tags**: `#robotics`, `#AI ethics`, `#Boston Dynamics`, `#government technology`, `#tech worker activism`

---

<a id="item-tech-news-15"></a>
### [Microsoft Fixes High-Severity Android Authenticator Vulnerability](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-80097) ⭐️ 7.0/10

Microsoft has fixed a high-severity vulnerability in the Android version of Microsoft Authenticator, tracked as CVE-2026-80097. A malicious app already installed and running on the device could obtain tokens for logged-in work accounts without requesting Android permissions. The fix is included in version 6.2606.4246. Microsoft said there was no evidence of exploitation at the time of its initial advisory, while researchers said no further user action was needed but Microsoft said attackers would need to trick the user into completing authentication.

telegram · zaihuapd · Oct 27, 12:04

**「Microsoft Authenticator Android broker context」** Microsoft Authenticator on Android functions as an authentication broker for work or school accounts, managing access tokens that allow enterprise resource access. CVE-2026-80097 is a high-severity elevation-of-privilege flaw \(CVSS 8.6\) caused by improper authentication in the broker component, allowing a malicious Android app with no declared permissions to steal those tokens; Microsoft fixed it in version 6.2606.4246, and as of October 26, 2026, the flaw was not listed in CISA&\#x27;s Known Exploited Vulnerabilities catalog.

**「Impact」** Android Microsoft Authenticator users should update to version 6.2606.4246 or later to mitigate the risk that a malicious app already installed on the device could steal logged-in work account tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html">Microsoft Authenticator Flaw Let Permissionless Android Apps Steal...</a></li>
<li><a href="https://cybersecuritynews.com/microsoft-authenticator-flaw/">Microsoft Authenticator Flaw Lets Malicious Android Apps Steal...</a></li>

</ul>
</details>

**Tags**: `#security`, `#Microsoft Authenticator`, `#Android`, `#token theft`, `#CVE-2026-80097`

---

<a id="item-tech-news-16"></a>
### [Anthropic Confirms Researchers Accessed Some Internal Systems, Says Customer Data Unaffected](https://www.washingtonpost.com/technology/2026/10/26/researchers-cybersecurity-start-up-cathedral-got-inside-anthropic/) ⭐️ 7.0/10

Anthropic confirmed that researchers from Cathedral, a cybersecurity startup founded by former DOGE members, accessed some of its internal sales, HR, and IT systems by exploiting a vulnerability in third-party commercial software. Cathedral reported that an AI agent found the path within 12 hours and reached meeting notes, payroll and hiring information, and Slack messages. Anthropic stated that customer messages to models, model responses, AI system code, and model weights were not accessed, and that its monitoring had already detected some activity and shut down the path before Cathedral&\#x27;s report. The company said Cathedral exaggerated national security implications and did not fully disclose its activity, while Cathedral said it followed normal security research practices and limited data access to the minimum necessary.

telegram · zaihuapd · Oct 27, 12:43

**「Background」** Cathedral is a cybersecurity startup founded by former DOGE members. Anthropic distinguishes core AI systems from corporate back-office systems, a distinction central to its claim that model weights and customer conversations were untouched despite the internal access.

**「Impact」** Anthropic now faces public scrutiny over its third-party software security and the conflicting accounts with Cathedral about severity and disclosure, while customer-facing AI data remains unaffected according to the company.

**Tags**: `#Anthropic`, `#cybersecurity`, `#AI infrastructure`, `#third-party vulnerability`, `#incident response`

---

<a id="item-tech-news-17"></a>
### [Anthropic Manager Drops Coding Interviews as Claude Outperforms Candidates](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) ⭐️ 7.0/10

Anthropic hiring manager Felix Rieseberg stopped using coding questions in interviews this month, saying Claude already outperforms candidates on such tasks and that writing code is no longer a valid screening criterion. He argues that with lower execution costs, tenure no longer determines impact. Rieseberg advises junior engineers to target business goals and use their fresh perspective to build a single prototype over a weekend to win support. He cites Claude Code&\#x27;s graphical interface, which was prototyped by two newcomers in a weekend and had its first public release about eight days later.

telegram · zaihuapd · Oct 28, 01:46

**「Background」** Live coding interviews have traditionally been used to assess software engineering candidates&\#x27; programming ability. AI assistants such as Anthropic&\#x27;s Claude can now generate and edit code, challenging that assumption. Claude Code is Anthropic&\#x27;s coding tool, and its graphical interface is mentioned as the recent prototype example in the source.

**「Impact」** Engineers interviewing with this manager may no longer face coding questions, and junior engineers can pursue influence by shipping a business-focused weekend prototype; this change is reported as one manager&\#x27;s practice, not a confirmed company-wide policy.

**Tags**: `#AI`, `#software engineering`, `#hiring`, `#Claude`, `#tech industry`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Pop Mart’s Q3 Revenue Falls 45–50% as Labubu Hype Cools](https://asia.nikkei.com/business/consumer/pop-mart-s-revenue-halves-in-q3-as-labubu-craze-cools) ⭐️ 7.0/10

Pop Mart said in an Oct. 27 Hong Kong stock exchange filing that third-quarter revenue fell 45–50% year over year, with Labubu hype cooling. The company also said the proportion of high-margin overseas sales declined, and it expects second-half gross margin to narrow by up to 2 percentage points from the first half.

telegram · zaihuapd · Oct 27, 14:30

**「Background」** Labubu, a character in Pop Mart’s Monsters series, had been the company’s top sales contributor, making up more than one-third of total revenue in the first half of 2025, according to a stock exchange filing.

**「Impact」** Pop Mart investors now face a weaker second-half profit outlook because the sharp drop in high-margin overseas Labubu sales trims the company&\#x27;s expected gross margin by up to 2 percentage points, eroding the profit engine that drove a 385.6% first-half profit jump.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/ywang/2025/08/20/chinas-pop-mart-targets-4-billion-in-sales-this-year-amid-labubu-lunacy/">China’s Pop Mart Targets $4 Billion In Sales This Year Amid Labubu ...</a></li>
<li><a href="https://www.scmp.com/business/china-business/article/3372313/pop-mart-reports-45-50-revenue-decline-labubu-sales-weaken-across-major-markets">Pop Mart reports 45 to 50% revenue decline as Labubu sales...</a></li>
<li><a href="https://www.caixinglobal.com/2025-08-21/labubu-carries-pop-mart-stock-to-all-time-high-102354054.html">Labubu Carries Pop Mart Stock to All-Time High - Caixin Global</a></li>

</ul>
</details>

**Tags**: `#Pop Mart`, `#Labubu`, `#Q3 revenue`, `#consumer discretionary`, `#collectibles`

---