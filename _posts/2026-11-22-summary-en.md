---
layout: default
title: "Horizon Summary: 2026-11-22 (EN)"
date: 2026-11-22
lang: en
---

> From 21 items, 8 important content pieces were selected

---

**Technology News**
1. [Lean Verification of the Riemann Hypothesis](#item-tech-news-1) ⭐️ 10.0/10
2. [GPGME Vulnerability Prior to 2.3.0 May Lead to Remote Code Execution](#item-tech-news-2) ⭐️ 8.0/10
3. [Microsoft Previews RDMA over USB4 for Multi-PC Local AI](#item-tech-news-3) ⭐️ 8.0/10
4. [Zhejiang University Reports First Real-Machine QRAM on Superconducting Quantum Chip](#item-tech-news-4) ⭐️ 8.0/10
5. [Tesla Begins Rolling Out FSD v15 With Reality View](#item-tech-news-5) ⭐️ 8.0/10
6. [Muru: New AI-Assisted Rust Server for Python ASGI/WSGI Apps](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenRouter Warns MiniMax Prompts May Have Been Read by Third Parties](#item-tech-news-7) ⭐️ 7.0/10

**Financial News**
1. [Trump Backs Lutnick, Urges Nvidia CEO to Apologize and Return](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Lean Verification of the Riemann Hypothesis](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 10.0/10

A Lean formalization and verification of the Riemann Hypothesis has been presented. Community reports state that Levent Alpöge released the formal proof on November 20, 2026, with a codebase of about 17 million lines, and Lean FRO and the Mathlib Initiative certified on November 21 that the proposition matches Mathlib&\#x27;s RiemannHypothesis, the code compiles without errors, and multiple independent proof checkers validate the proof. The formalization reportedly involved Claude AI formalizing a substantial part of modern mathematics, making this a landmark result for formal verification and AI-assisted theorem proving. The source item does not provide independent confirmation beyond these community reports.

hackernews · g-b-r · Nov 21, 14:36 · [Discussion](https://news.ycombinator.com/item?id=50589618)

**「Background」** Lean is an interactive theorem prover and programming language that checks every step of a mathematical proof against a small, independently implemented kernel, reducing the risk of unnoticed errors. The Riemann Hypothesis is a famous unproven conjecture about the distribution of prime numbers. On November 20, 2026, Levent Alpöge released a proof of the Riemann Hypothesis as a Lean library comprising 17 million lines of code, with the formalization reportedly done with the assistance of Anthropic&\#x27;s Claude AI.

**「Impact」** If independently confirmed, this would provide a machine-checked proof of the Riemann Hypothesis and demonstrate that AI-assisted formalization can handle large-scale modern mathematics, affecting formal verification, mathematics, and AI theorem proving. However, the result currently rests on community reports and independent checkers, so caution is warranted.

**「Community Discussion」** Commenters note that a false proof would require bugs in all independent proof-checking kernels, but point to a past fake Collatz refutation as a cautionary example. They also credit Levent Alpöge for eliciting the formalization from Claude and raise questions about what larger mathematical problems this could enable.

<details><summary>References</summary>
<ul>
<li>Lean verification of the Riemann Hypothesis | Lean community blog</li>
<li>Anthropic mathematician proves Riemann hypothesis, most famous ...</li>

</ul>
</details>

**Tags**: `#Lean`, `#Riemann Hypothesis`, `#formal verification`, `#AI-assisted theorem proving`, `#mathematics`

---

<a id="item-tech-news-2"></a>
### [GPGME Vulnerability Prior to 2.3.0 May Lead to Remote Code Execution](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

A vulnerability in the GPGME library affects all versions prior to 2.3.0 and was publicly disclosed on 2026-11-20 after GitLab informed the GnuPG project on 2026-11-12. The flaw is a double free that may be exploitable for remote code execution in some contexts, though the severity is debated; it affects software using GPGME, including GitLab, Gpg4win, GnuPG Desktop, many mail clients, XMPP clients, Samba, and Flatpak. GitLab had to update earlier than the initially planned 2026-11-25 coordinated disclosure due to a separate Ruby2Shell bug. Red Hat reportedly fixed the issue about five years ago in its downstream package, but the fix was missed upstream.

hackernews · gdgghhhhh · Nov 21, 08:32 · [Discussion](https://news.ycombinator.com/item?id=50587208)

**「What is GPGME and why this vulnerability matters」** GPGME is a library that provides applications with a simplified interface to GnuPG cryptographic operations, so it is embedded in mail clients, GitLab, Samba, and other software. The vulnerability, tracked as CVE-2026-129975, is a double-free bug in GPGME versions before 2.3.0 that can be triggered by a specially crafted OpenPGP key, and developers have stated that remote code execution cannot be ruled out, prompting an immediate update recommendation. Because the bug was present for many years and affects both shared and statically linked deployments, the exposure extends across a wide ecosystem rather than a single application.

**「Impact」** All software using GPGME prior to version 2.3.0—including most mail clients, many XMPP clients, Samba, Flatpak, Gpg4win, GnuPG Desktop, and GitLab—must upgrade or apply patches, as a malicious OpenPGP key can trigger the critical flaw \(CVE-2026-129975\). The reported impact ranges from application data exposure to possible code execution; some commenters note the underlying bug is a double free, so exploitability may be overstated.

**「Community Discussion」** Commenters note that the bug is a double free rather than a ready-made RCE chain, with some questioning whether the report is overstated; others emphasize the widespread exposure of GPGME across mail clients, XMPP clients, Samba, and Flatpak. One commenter asks whether apt is affected since it does not use gpgme.

<details><summary>References</summary>
<ul>
<li>GnuPG Warns Critical GPGME Flaw Could Expose App Data via ...</li>
<li>Fwd: GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975)</li>
<li>GPGME Double Free Bug Hid in GnuPG&#x27;s Glue Library for 24 Years ...</li>
<li>GnuPG Warns Critical GPGME Flaw Could Expose App Data via ...</li>
<li>GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975)</li>
<li>Security Alert: A Critical Bug Affecting Everyday Email and Chat Apps Just ...</li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#GPGME`, `#GnuPG`

---

<a id="item-tech-news-3"></a>
### [Microsoft Previews RDMA over USB4 for Multi-PC Local AI](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

Microsoft has released a developer preview of RDMA over USB4 for Windows, enabling multiple PCs to pool memory and GPU compute over standard USB4 connections to run a single local AI model without dedicated network cards or switches. In a demonstration, three AMD Ryzen AI Max+ 395 systems ran the Qwen3-235B-A22B model with 4-bit quantization at about 18.5 tokens per second. The feature will be distributed through Windows Insider releases. This makes multi-machine local inference more accessible by using common USB4 connectivity instead of specialized networking hardware.

telegram · zaihuapd · Nov 21, 06:13

**「Background」** RDMA \(Remote Direct Memory Access\) enables direct memory-to-memory data transfers between computers without involving the operating system CPU stack, reducing latency and overhead for distributed workloads. USB4 is a standard high-speed interconnect that provides sufficient bandwidth for this use case. In this developer preview, Microsoft adds RDMA over USB4 to Windows&\#x27; NetworkDirect interface, allowing compatible AI frameworks to use the combined memory capacity and GPU compute of multiple connected PCs.

**「What this means」** Windows users with multiple compatible PCs and USB4 connections can pool GPU memory and compute to run larger local models like Qwen3-235B-A22B that would not fit on one machine, as shown by Microsoft&\#x27;s developer preview achieving about 18.5 token/s across three AMD Ryzen AI Max+ 395 systems. The capability is currently limited to the Windows Insider developer preview and requires a compatible inference framework using NetworkDirect, so production use is not yet available.

<details><summary>References</summary>
<ul>
<li>Introducing RDMA over USB4® on Windows: run larger local AI models ...</li>
<li>Microsoft previews linking Windows PCs over USB4 to run larger AI ...</li>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftusbblog/introducing-rdma-over-usb4%C2%AE-on-windows-run-larger-local-ai-models-across-pcs/4574602">Introducing RDMA over USB4® on Windows: run larger local AI ...</a></li>
<li><a href="https://windowsreport.com/windows-pcs-can-now-team-up-over-usb4-to-run-ai-models-that-wont-fit-on-one-machine/">Windows PCs Can Now Team Up Over USB4 to Run AI Models That ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#RDMA`, `#USB4`, `#Local AI`, `#AI infrastructure`

---

<a id="item-tech-news-4"></a>
### [Zhejiang University Reports First Real-Machine QRAM on Superconducting Quantum Chip](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 8.0/10

Zhejiang University researchers have reported the first real-machine implementation of quantum random access memory \(QRAM\) on a superconducting quantum chip, named Tianmu 2. The work, published in Nature Physics, successfully ran prototypes that can retrieve 4-bit and 8-bit data, with accuracies of 80.9% and 60.4%, respectively. The QRAM circuit depth was reduced by more than 30% compared with an unoptimized scheme, and the team said it verified local noise-resilience properties for the first time. The group plans to advance large-scale QRAM research next.

telegram · zaihuapd · Nov 21, 08:31

**「Background」** Quantum random access memory \(QRAM\) is a proposed memory architecture that would let a quantum processor query stored data in superposition, analogous to how classical RAM provides indexed access for conventional processors. Superconducting qubits are a leading quantum computing platform because they can be fabricated on chips and controlled with microwave pulses, but adding memory access without destroying fragile quantum states remains difficult.

**「Impact」** The result gives quantum computing researchers an early experimental benchmark for QRAM on superconducting hardware, while the 8-bit prototype&\#x27;s 60.4% accuracy signals that scaling to practical sizes remains an open challenge.

**Tags**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#quantum memory`, `#Nature Physics`

---

<a id="item-tech-news-5"></a>
### [Tesla Begins Rolling Out FSD v15 With Reality View](https://x.com/Tesla/status/2124222447855743019) ⭐️ 8.0/10

Tesla has begun rolling out FSD v15 overseas, claiming a 25x improvement in handling of safety-critical scenarios. The update introduces the Tesla Reality View visualization interface, which overlays camera footage and FSD driving plans on the vehicle screen and supports full-screen, map, and split-screen views as well as a quiet mode. Navigation can overlay turn information, turn signal sounds are softer and gradually fade, and the update also improves driving over potholes and debris and speed control near schools and in bad weather.

telegram · zaihuapd · Nov 22, 00:03

**「Background」** Tesla&\#x27;s Full Self-Driving \(FSD\) system has been released in stages, with FSD v14 Lite becoming available in South Korea in July 2026 as the first non-North American deployment on HW3 vehicles, limited to US-built Model 3 and Y. Ahead of the v15 release, reports indicated that FSD v15 would introduce new visualizations, and Tesla CEO Elon Musk described the interface as rendering reality in a mind-bending way.

**「Impact」** Tesla owners receiving FSD v15 in overseas markets should see the new camera-overlay visualization and the claimed safety-critical handling improvements, though the rollout may be staged and region-specific. The 25x safety-critical improvement is Tesla&\#x27;s claim and was not independently verified in the source.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot">Tesla Autopilot - Wikipedia</a></li>
<li><a href="https://www.notateslaapp.com/news/5057/tesla-fsd-v15-coming-next-month-with-holiday-update-musk">Tesla FSD V 15 Arriving Next Month: Home Garage... - Not a Tesla App</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#FSD`, `#autonomous driving`, `#AI`, `#software update`

---

<a id="item-tech-news-6"></a>
### [Muru: New AI-Assisted Rust Server for Python ASGI/WSGI Apps](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

Graham Dumpleton, creator of mod\_wsgi, has introduced Muru, an early-stage AI-assisted Rust server designed to run ASGI and WSGI Python web applications in both development and production. Over three weeks beginning November 4, 2026, he has published an extraordinarily detailed development log covering import-once-fork-many, HTTPS in development, releases instead of restarts, canaries without a service mesh, Kubernetes integration, scaling to zero, overlays, and an on-page toolbar with tracing. The project builds on his twenty years of mod\_wsgi experience and aims to provide the best possible tools for serving Python apps. Dumpleton notes that while AI assists with much of the surface work, his own judgment and history of mod\_wsgi mistakes guide the polishing to make it trustworthy.

rss · Simon Willison · Nov 21, 23:56

**「Background」** WSGI is the older Python web server interface, while ASGI is its asynchronous successor; servers must implement one or both to host Python web applications. Graham Dumpleton is known as the original author of mod\_wsgi, a widely used Apache module for hosting Python WSGI applications that he started 20 years ago. Rust is a systems programming language valued for memory safety and performance, increasingly used for web infrastructure tools.

**「Impact」** Python web developers and operators gain a new Rust-based server option that could combine production reliability from mod\_wsgi experience with modern ASGI/WSGI support and AI-assisted development, though it remains early-stage and not yet production-ready based on the published progress.

**Tags**: `#Python`, `#Rust`, `#ASGI`, `#WSGI`, `#web servers`

---

<a id="item-tech-news-7"></a>
### [OpenRouter Warns MiniMax Prompts May Have Been Read by Third Parties](https://news.ycombinator.com/item?id=50585962) ⭐️ 7.0/10

OpenRouter warned users that prompts sent to MiniMax models through its API may have been read by third parties. A security researcher sent prompts containing test URLs to MiniMax models between July and October 2026, and those URLs were accessed 40 to 130 hours later. OpenRouter attributes the issue to MiniMax and its forwarding providers AtlasCloud, Novita, and StreamLake, and has removed zero-data-retention labels from affected endpoints. It advises users who included sensitive credentials to rotate API keys and passwords. No official statement has been posted on OpenRouter&\#x27;s website yet.

telegram · zaihuapd · Nov 21, 06:53

**「Background」** OpenRouter operates as an API gateway that lets developers call multiple model providers under one interface, and it may route requests through intermediary forwarding providers. MiniMax is an AI model vendor, and AtlasCloud, Novita, and StreamLake are forwarding or reseller partners that transmit requests to MiniMax. A zero-data-retention label indicates a provider claims not to persist or inspect user prompts and outputs, so its removal reduces privacy assurance for affected endpoints.

**「Impact」** Users who sent prompts containing API keys, passwords, or other secrets to MiniMax endpoints via OpenRouter should immediately rotate those credentials and monitor for unauthorized access, because the accessed test URLs indicate third-party retrieval of request contents.

**Tags**: `#security`, `#AI`, `#OpenRouter`, `#MiniMax`, `#data-privacy`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Trump Backs Lutnick, Urges Nvidia CEO to Apologize and Return](https://www.reuters.com/world/us/trump-says-he-still-backs-lutnick-urges-nvidias-huang-apologize-2026-11-20/) ⭐️ 8.0/10

President Trump said on Nov. 20, according to Reuters, he still backs Commerce Secretary Lutnick and wants resigned Nvidia CEO Jensen Huang to apologize and return, amid criticism over China chip sales; he also said he raised the matter with China&\#x27;s Xi, which Treasury Secretary Bessent contradicted.

telegram · zaihuapd · Nov 21, 05:03

**「Context」** The dispute stems from Commerce Secretary Howard Lutnick’s handling of advanced Nvidia AI chip sales to China, which drew Republican criticism over potential diversion of chips; Jensen Huang resigned as Nvidia’s CEO amid this controversy.

**「Nvidia faces leadership and policy uncertainty」** Nvidia and its investors face continued leadership uncertainty and a weaker advocacy position in Washington over China chip export rules, while Asian governments have begun seeking to confirm chip supply commitments after Huang&\#x27;s resignation.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/11/trump-was-in-bed-with-jensen-critics-balk-at-huangs-wish-to-return-to-nvidia/">“ Trump was in bed with Jensen ”: Critics balk at Huang ’s wish to...</a></li>
<li><a href="https://www.cnbc.com/2026/11/16/trump-lutnick-nvidia-national-security-jensen-huant.html">Trump says he&#x27;s OK with Jensen Huang returning as Nvidia CEO</a></li>
<li><a href="https://www.cnn.com/2026/11/20/politics/trump-news-conference-takeaways">Takeaways from Trump ’s news briefing on Putin, Xi | CNN Politics</a></li>
<li><a href="https://observer.com/2026/11/jensen-huang-resigns-leaving-nvidias-china-chip-fight-without-its-chief-advocate/">Jensen Huang Resigns, Leaving Nvidia’s China Chip Fight In ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-13/jensen-huang-exit-sets-up-us-china-showdown-over-ai-chip-curbs">Jensen Huang Exit Sets Up US-China Showdown Over AI Chip ...</a></li>
<li><a href="https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/">Asian governments react to Nvidia CEO Jensen Huang’s exit</a></li>

</ul>
</details>

**Tags**: `#US-China trade`, `#Nvidia`, `#semiconductor export controls`, `#Trump administration`, `#corporate leadership`

---