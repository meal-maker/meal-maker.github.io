---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 35 items, 16 important content pieces were selected

---

**Technology News**
1. [NariQ: BF16-level Qwen3.8-27B in a 10 GB File](#item-tech-news-1) ⭐️ 8.0/10
2. [GLM-5.4: Toward generalized coding with our first loop transformer](#item-tech-news-2) ⭐️ 8.0/10
3. [Codex2api Supply-Chain Attack: Malicious v3.1.11 Removes Authentication](#item-tech-news-3) ⭐️ 8.0/10
4. [Anthropic Claims Claude Proved VP≠VNP, Releases Lean 4 Proof](#item-tech-news-4) ⭐️ 8.0/10
5. [Nvidia Board Reinstates Jensen Huang as CEO](#item-tech-news-5) ⭐️ 7.0/10
6. [Stalwart Announces Drop-In Microsoft Exchange Replacement with Caveats](#item-tech-news-6) ⭐️ 7.0/10
7. [Ladybird Browser Reaches Alpha](#item-tech-news-7) ⭐️ 7.0/10
8. [ChatGPT Announces GPT-6.2 Sol Rollout to Paid Users](#item-tech-news-8) ⭐️ 7.0/10
9. [AI-Claimed Riemann Proof Vacuous, Author Says Code Is Garbage but Compiles](#item-tech-news-9) ⭐️ 7.0/10
10. [Over 45,000 EU Organizations Urge EU to Challenge Apple Browser Rules](#item-tech-news-10) ⭐️ 7.0/10
11. [Singapore PM: No Conduit for US Chip Control Evasion](#item-tech-news-11) ⭐️ 7.0/10

**Technology Blog**
1. [Day-0 vLLM Support for ERNIE 5.5 Flash Preview](#item-tech-blog-1) ⭐️ 8.0/10

**Financial News**
1. [Anthropic IPO Selloff Wipes $1.7 Trillion From Chinese Tech Stocks, Clouding AI Listings](#item-finance-news-1) ⭐️ 8.0/10
2. [Nvidia board reinstates Jensen Huang as CEO](#item-finance-news-2) ⭐️ 8.0/10
3. [Shanghai Metro Adjusts Fares for First Time in 21 Years](#item-finance-news-3) ⭐️ 7.0/10
4. [SpaceX reported to rent AI compute to Anthropic and Google, earning billions monthly](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [NariQ: BF16-level Qwen3.8-27B in a 10 GB File](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10

NariQ introduces 3-bit-or-lower quantizations of Qwen3.8-27B in a 10 GB GGUF file that reportedly retain near-BF16 performance on long-horizon agentic, math, multilingual, and image understanding tasks. Benchmarks show the 3-bit and 2.5-bit versions match or exceed BF16 on DeepSWE \(41.0/41.9 vs 39.8\) and Terminal-Bench 2.1 \(63.8/60.2 vs 62.6\), while 2-bit drops to 28.6 on DeepSWE. Decode speed is comparable to other quantizations on an RTX PRO 6000, but long-context accuracy falls at 64K, and running the model requires the project&\#x27;s llama.cpp fork.

hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

**「Background」** Low-bit quantization compresses model weights to reduce memory and compute, but going below 4 bits usually degrades quality, especially on long-horizon tasks. Qwen3.8-27B is a 27-billion-parameter open-weight model, and a 10 GB file corresponds to roughly 3 bits per weight. NariQ targets these aggressive bit widths while claiming to preserve BF16-level behavior across multiple task types.

**「Impact」** Users with around 10 GB of memory can locally run a 27B model with claimed near-BF16 agentic and reasoning quality, but must use the custom llama.cpp fork and may see slower decode on Apple Silicon \(about 3.8 tok/s on an M3 Pro\).

**「Community Discussion」** Comments are cautiously positive, praising the inclusion of multiple long-horizon tasks and held-out checks, though one user argues that much of the apparent gain may come from harness differences rather than the model; others request Bonsai 2 comparisons and note the proliferation of new quantization methods.

**Tags**: `#quantization`, `#LLM`, `#open-source`, `#AI-inference`, `#Qwen`

---

<a id="item-tech-news-2"></a>
### [GLM-5.4: Toward generalized coding with our first loop transformer](https://z.ai/blog/glm-5.4) ⭐️ 8.0/10

Z.ai has announced GLM-5.4, described as its first loop transformer model for generalized coding. The release has drawn significant technical discussion around the loop transformer architecture. The supplied item does not include benchmark results or detailed specifications, but the model is positioned for coding tasks.

hackernews · foohis · Nov 23, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50609685)

**「Loop Transformer Architecture」** GLM-5.4 is Z.ai&\#x27;s latest flagship model and the first built on a Loop Transformer architecture, which reuses the same transformer block iteratively rather than stacking distinct layers, allowing a smaller model to reach intelligence levels comparable to 2T–3T parameter models. Unlike conventional transformers that compute each layer once during inference, this looped design repeats computation over shared weights, reducing memory bandwidth constraints. The model is introduced as the start of &\#x27;Generalized Coding,&\#x27; where code serves as a foundation for broader tasks, though Z.ai notes it still has limitations.

**「Impact」** Access currently requires Z.ai&\#x27;s separate Coding Plan: the model is not available through OpenRouter or the regular Z.ai API plan, although Coding Plan API keys work like standard Z.ai keys.

**「Community Discussion」** Commenters praised the transparency of the technical details and explained that loop transformers can reduce memory bandwidth bottlenecks by reusing weights during inference. Some users, however, reported that Chinese models with extended reasoning produce frustrating marathon thinking and second-guess simple tasks, making time-to-completion higher than frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ... - z.ai</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.4">GLM-5.4 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#coding`, `#transformer architecture`

---

<a id="item-tech-news-3"></a>
### [Codex2api Supply-Chain Attack: Malicious v3.1.11 Removes Authentication](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

Codex2api&\#x27;s author account was compromised, and the attacker bypassed the main branch by pushing a tag that caused the release pipeline to build a backdoored version. The malicious release v3.1.11 removes authentication, effectively enabling passwordless remote command execution, and a workflow exfiltrates 16 GitHub Actions secrets across at least 21 repositories under the same account. Users who installed or updated to version 3.1.10 through 3.1.12 should immediately stop using it, roll back to 3.1.9, and rotate GitHub tokens, SSH keys, database credentials, and DeepSeek keys. The report was shared on Telegram by zaihuapd and links to an incident recap and original report.

telegram · zaihuapd · Nov 23, 11:21

**「Background」** Open-source supply-chain attacks can involve compromising a maintainer account to push malicious tags or releases and exfiltrate secrets from CI/CD systems such as GitHub Actions. Similar incidents have targeted GitHub Actions and npm ecosystems, making verification of release authenticity and rapid rollback important.

<details><summary>References</summary>
<ul>
<li><a href="https://www.darkreading.com/application-security/supply-chain-attacks-github-actions-gravity-forms-npm">Malware Spotted in GitHub Actions , Gravity Forms, npm</a></li>

</ul>
</details>

**Tags**: `#supply-chain-attack`, `#open-source-security`, `#codex2api`, `#github-actions`, `#rce`

---

<a id="item-tech-news-4"></a>
### [Anthropic Claims Claude Proved VP≠VNP, Releases Lean 4 Proof](https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md) ⭐️ 8.0/10

Anthropic announced on November 24 that an internal Claude research model discovered a proof that VP ≠ VNP over every field and released the paper and Lean 4 formalization. The repository states the paper and code were written by AI and presents a superpolynomial arithmetic circuit lower bound for the Hamiltonian cycle polynomial, implying VP is a proper subclass of VNP. If correct, this would resolve Valiant’s 1979 algebraic complexity conjecture, but the result concerns arithmetic circuits only and does not address P versus NP. The formalization has passed three standard axiom audits and an independent nanoda kernel check with no \`sorry\` outside reserved files, but no human mathematician has fully reviewed it, Lean cannot verify that the formal statement matches the claimed theorem, and Appendix Q lists discrepancies pending independent review.

telegram · zaihuapd · Nov 24, 06:02

**「Background」** VP vs VNP is the algebraic analogue of the P vs NP problem, posed by Leslie Valiant in 1979; it asks whether certain polynomial families can be computed by polynomial-size arithmetic circuits. A proof that VP ≠ VNP over every field would resolve this long-open conjecture in algebraic complexity theory, but it does not settle the classical P vs NP question because it is restricted to arithmetic circuits. Lean 4 is a proof assistant that can mechanically check formalized proofs.

**「Limited to algebraic complexity until reviewed」** Algebraic complexity researchers should treat VP≠VNP as provisional until the Lean 4 proof and its correspondence to the claimed theorem are independently audited; even if confirmed, the result would settle Valiant&\#x27;s conjecture only for algebraic circuits and does not imply P≠NP.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UuOiRi9T-9c">Claude &#x27;s VP VNP Proof : 47 Years Open, Still Unchecked... - YouTube</a></li>
<li><a href="https://cstheory.stackexchange.com/questions/529/does-vp-neq-vnp-imply-p-neq-np">cc. complexity theory - Does $ VP \neq VNP $ imply $P \neq NP</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#VP vs VNP`, `#computational complexity`, `#Lean 4`, `#AI-generated proof`

---

<a id="item-tech-news-5"></a>
### [Nvidia Board Reinstates Jensen Huang as CEO](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html) ⭐️ 7.0/10

Nvidia&\#x27;s board reinstated Jensen Huang as president, CEO, and board director, according to a company news release linked in the report. The board said it received input from senior levels of the U.S. government and, based on that input, is confident the reinstatement poses no national security risk. The move restores Huang to leadership of the major AI hardware vendor after a recent leadership upheaval, though full details remain sparse. It highlights the apparent role of U.S. government officials in governance decisions at a key AI chipmaker.

hackernews · jaz · Nov 23, 14:00 · [Discussion](https://news.ycombinator.com/item?id=50611576)

**「Background」** Nvidia&\#x27;s board announced on November 23, 2026, that Jensen Huang has been reinstated as President, CEO, and board director, effective immediately, and said the decision followed input from senior levels of the U.S. government. The company said the board is confident the reinstatement poses no national security risk. This reverses Huang&\#x27;s earlier removal from those roles, which had been one of the most startling corporate leadership changes at the world&\#x27;s largest chipmaker.

**「Impact」** Nvidia&\#x27;s leadership is stabilized under Huang after board-level uncertainty, reducing immediate governance risk for customers and partners in its AI hardware ecosystem.

**「Community Discussion」** Commenters emphasized the board&\#x27;s statement that senior U.S. government input assured no national security risk. Some discussed Delaware&\#x27;s Caremark precedent and the surprising unanimous reversal, while others criticized perceived inconsistency with U.S. export controls toward China.

<details><summary>References</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Board-Reinstates-Jensen-Huang-as-President-CEO-and-Board-Director/default.aspx">NVIDIA Corporation - NVIDIA Board Reinstates Jensen Huang as ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-23/nvidia-reinstates-jensen-huang-as-ceo-with-government-input">Nvidia Rehires Huang in Stunning Comeback Following... - Bloomberg</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/nvidia-reinstates-jensen-huang-rcna610864">Nvidia reinstates Jensen Huang as CEO</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#AI hardware`, `#technology industry`

---

<a id="item-tech-news-6"></a>
### [Stalwart Announces Drop-In Microsoft Exchange Replacement with Caveats](https://stalw.art/blog/microsoft-exchange-replacement/) ⭐️ 7.0/10

Stalwart mail server now offers a drop-in replacement for Microsoft Exchange, according to a new announcement. The move targets organizations seeking open-source alternatives to Exchange. The announcement acknowledges practical caveats, including Outlook client compatibility issues, missing regulatory archiving features, and protocol lock-in concerns.

hackernews · shaunpud · Nov 23, 22:32 · [Discussion](https://news.ycombinator.com/item?id=50620349)

**「Background」** Stalwart is an open-source mail and collaboration server written in Rust. Microsoft Exchange is a proprietary server tightly integrated with Outlook and other clients through protocols such as MAPI, EWS, ActiveSync, and Autodiscover. Version 1.2.0 of Stalwart adds compatibility with these protocols, enabling organizations to replace Exchange while continuing to use familiar email clients.

**「Potential impact」** Organizations can now deploy Stalwart 1.2.0 as a drop-in replacement for on-premises Microsoft Exchange, potentially eliminating Exchange licensing costs, but they must address Outlook client compatibility changes, missing regulatory archiving features such as GoBD, and continued reliance on Microsoft email protocols.

**「Community Discussion」** Community comments express skepticism about the &\#x27;drop-in replacement&\#x27; label, pointing to Outlook&\#x27;s shift away from on-premises Exchange support, missing GoBD-compliant archiving for German users, and broader protocol lock-in concerns. Some also note that Stalwart powers Mozilla&\#x27;s Thundermail, but caution that supporting Microsoft&\#x27;s protocol stack may not benefit the open email ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://linuxiac.com/stalwart-1-2-offers-open-source-microsoft-exchange-replacement/">Stalwart 1.2 Offers Open-Source Microsoft Exchange Replacement</a></li>
<li><a href="https://stalw.art/blog/microsoft-exchange-replacement/">Stalwart is now a drop-in replacement for Microsoft Exchange</a></li>

</ul>
</details>

**Tags**: `#email`, `#microsoft-exchange`, `#open-source`, `#mail-server`, `#interoperability`

---

<a id="item-tech-news-7"></a>
### [Ladybird Browser Reaches Alpha](https://ladybird.org/posts/alpha/) ⭐️ 7.0/10

Ladybird, an open-source browser built from scratch, has reached alpha status. The release follows a shift away from some self-developed libraries toward production-grade components like SQLite and Skia, which community members said improved rendering. Early testers reported correct rendering across many sites, including news sites and Proxmox&\#x27;s NoVNC web console, with one tester finding NoVNC snappier than in Firefox. The main reported issue was slightly jerky page scrolling. The alpha is not yet a daily driver replacement, but it marks significant progress for an independent browser not tied to Google&\#x27;s ads.

hackernews · janvdberg · Nov 23, 16:13 · [Discussion](https://news.ycombinator.com/item?id=50614249)

**「Background」** Ladybird is an open-source web browser engine built from scratch, not based on Chromium or Firefox, and is developed by a 501\(c\)\(3\) non-profit organization. The project has now released its first alpha version, available for macOS and Linux, marking a milestone toward a stable release expected in 2028 according to its public roadmap.

**「Impact」** Developers and early adopters can now test an independent, from-scratch browser engine against real websites, but alpha status and minor scrolling issues mean it is not yet positioned as a daily driver replacement.

**「Community Discussion」** Early testers in the thread were broadly impressed, reporting correct rendering on many sites and snappier NoVNC than Firefox, while noting slight scrolling jerkiness. Some commenters also expressed hope that Ladybird will address fingerprinting resistance and more granular permissions in the future.

<details><summary>References</summary>
<ul>
<li>Ladybird</li>
<li>Ladybird (web browser) - Wikipedia</li>

</ul>
</details>

**Tags**: `#web browser`, `#open source`, `#alpha release`, `#systems programming`, `#web engine`

---

<a id="item-tech-news-8"></a>
### [ChatGPT Announces GPT-6.2 Sol Rollout to Paid Users](https://x.com/ChatGPT/status/2124942186425069836) ⭐️ 7.0/10

ChatGPT announced on November 23 that it is rolling out GPT-6.2 Sol in the Chat tab to Plus, Pro, Business, and Enterprise users. The model is positioned for everyday conversation and reportedly better handles complex requests, including detailed instructions and web lookups. It also claims improvements in reading photo details such as label text and road-sign symbols, narrowing online options by price or location, and offering proactive follow-up suggestions like price-drop reminders. These capability descriptions come from the official announcement and have not been independently verified.

telegram · zaihuapd · Nov 24, 00:44

**「GPT-6 Model Family」** OpenAI’s GPT-6 generation includes the flagship Astra model and smaller Sol and Luna models, which are described as extending Astra’s intelligence while being more efficient and accessible \(tool-1-2\). GPT-6.2 Sol is an updated version of the Sol model, and compared with GPT-6 it is reported to be better at detecting fine details in photos such as symbols on signs or text on labels \(tool-1-1\).

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/11/23/openai-gpt-6-2-sol-chatgpt/">OpenAI Brings GPT - 6 . 2 Sol to ChatGPT &#x27;s Chat Tab - MacRumors</a></li>
<li><a href="https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/">OpenAI launches GPT - 6 Sol and Luna, boasting lower... | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#OpenAI`, `#GPT-6.2`, `#AI`, `#product-update`

---

<a id="item-tech-news-9"></a>
### [AI-Claimed Riemann Proof Vacuous, Author Says Code Is Garbage but Compiles](https://x.com/i/web/status/2124987173439209561) ⭐️ 7.0/10

Alpöge and Claude claimed to have proved the Riemann Hypothesis and a generalized version, but published only about 17 million lines of Lean across 175,000 files and no human-readable proof. The Lean and Mathlib communities initially said they had &quot;full confidence&quot; that the code proved the proposition. Researchers then found that key definitions were written as tautologies and geometric conditions were vacuous, suggesting the proof might be empty. On the 23rd, Alpöge admitted the &quot;250,000 pages is a joke,&quot; the code was &quot;full of garbage but compiles,&quot; and that criticism was completely reasonable.

telegram · zaihuapd · Nov 24, 01:29

**「Background」** The Riemann Hypothesis is a major unsolved problem about the zeros of the Riemann zeta function. Lean is an interactive theorem prover, and Mathlib is its formalized mathematics library. A formal proof must be built on meaningful definitions; tautological or vacuous assumptions can make code compile without proving the intended statement.

**「Impact」** The dispute shows that an AI-generated formal proof can compile while proving nothing about the Riemann Hypothesis, so formal-math communities must inspect definitions and derived statements, not just compilation success.

**Tags**: `#AI`, `#formal verification`, `#Lean`, `#Riemann Hypothesis`, `#controversy`

---

<a id="item-tech-news-10"></a>
### [Over 45,000 EU Organizations Urge EU to Challenge Apple Browser Rules](https://appleinsider.com/articles/26/11/23/eu-urges-to-challenge-apples-grip-on-iphone-browsers?utm_source=rss) ⭐️ 7.0/10

A coalition representing more than 45,000 EU enterprises and organizations, including Mozilla and Shopify, has urged the European Commission to open a Digital Markets Act case against Apple&\#x27;s iPhone browser restrictions. The signatories say they represent roughly 45,000 to 55,000 EU businesses and organizations, and the signature collection runs until December 3, 2026. Although Apple now allows rival browsers to use their own engines in the EU to comply with the DMA, the letter argues that technical and legal requirements still prevent vendors from migrating existing EU users off WebKit, leaving enterprises dependent on the App Store to reach users. The coalition estimates that if half of native iOS apps moved to the web, EU enterprises could save €11 billion in development costs and €1.3 billion in App Store fees annually.

telegram · zaihuapd · Nov 24, 03:02

**「Background」** The Digital Markets Act is EU legislation designating large platforms as gatekeepers and imposing interoperability and fair-choice obligations. Apple&\#x27;s iOS has historically required all iPhone browsers to use its WebKit engine, limiting differentiation and web capabilities. Under DMA enforcement, Apple has permitted alternative browser engines in the EU, but the signatories contend the implementation still restricts real competition.

**「Impact」** If the European Commission opens a case and finds non-compliance, Apple could be forced to further loosen browser engine and distribution restrictions, potentially reducing App Store dependence for EU enterprises and cutting their costs by the estimated amounts. The outcome remains uncertain because the letter is a request for action, not a final ruling.

**Tags**: `#Apple`, `#EU`, `#browser`, `#WebKit`, `#DMA`

---

<a id="item-tech-news-11"></a>
### [Singapore PM: No Conduit for US Chip Control Evasion](https://www.bloomberg.com/news/articles/2026-11-24/singapore-won-t-be-conduit-to-skirt-us-chip-curbs-wong-says) ⭐️ 7.0/10

Singapore Prime Minister Lawrence Wong said the country will not be used as a conduit to evade US chip export controls, and that authorities are investigating Megaspeed&\#x27;s procurement of Nvidia chips. Wong stressed that Singapore will not provide a path to bypass the restrictions. A day earlier, the US Commerce Department added Megaspeed and six other Southeast Asian entities to its trade blacklist, with the Federal Register citing a &quot;significant risk&quot; that they could transfer advanced computing products to unauthorized users; the listing includes related entities in Malaysia and Thailand. Reuters reported that Alibaba&\#x27;s Singapore subsidiary Apex Enterprise Solutions is also on the list, while Alibaba said it has never transferred controlled advanced computing chips.

telegram · zaihuapd · Nov 24, 05:03

**「Background」** The US Entity List imposes licensing requirements on designated firms for all items subject to US export controls, and it is used to curb diversion of advanced computing chips. Recent blacklistings of Southeast Asian entities, including Singapore-based Megaspeed and Alibaba&\#x27;s Apex Enterprise Solutions, reflect concern that regional subsidiaries may re-export restricted chips to unauthorized users, which Alibaba has denied.

**「Impact」** As a result, exports of advanced semiconductors to Singapore, Indonesia, Malaysia, Thailand, and Brazil now require destination-based licenses under new U.S. Anti-Diversion Country Controls, meaning legitimate chip buyers and suppliers in those markets face immediate compliance hurdles and potential delays.

<details><summary>References</summary>
<ul>
<li><a href="https://uz.kursiv.media/en/2026-11-24/us-blacklist-megaspeed-alice-huang/">US blacklists Megaspeed , once led by China spy suspect Alice Huang</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/us-blacklists-alibaba-owned-company-014536273.html">US Blacklists Alibaba-Owned Company in Setback to AI Ambitions</a></li>
<li><a href="https://wccftech.com/the-u-s-shuts-chinas-access-to-advanced-chips-via-singapore-brazil-indonesia-malaysia-and-thailand-as-scott-bessent-gives-nvidia-10-days-to-show-it-did-not-goose-its-revenues/">The U.S. Shuts China&#x27;s Access To Advanced Chips Via Singapore ...</a></li>

</ul>
</details>

**Tags**: `#chip export controls`, `#semiconductors`, `#AI hardware`, `#US-China tech policy`, `#Singapore`

---

## Technology Blog

<a id="item-tech-blog-1"></a>
### [Day-0 vLLM Support for ERNIE 5.5 Flash Preview](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview) ⭐️ 8.0/10

rss · vLLM Blog · Nov 24, 00:00

**「Background」** ERNIE 5.5 Flash Preview is a 280B-parameter sparse MoE with 14B active parameters, 1M context, reasoning and tool calling; rather than wait for upstream vLLM integration or maintain a fork, the Baidu ERNIE and vLLM teams released a standalone vLLM-ERNIE plugin for the official vllm==0.32.0 wheel.

**「Solution」** The plugin registers the ERNIE architecture via vllm.general\_plugins at startup, importing model code only when config.json names it, while reusing vLLM&\#x27;s attention kernels, KV cache manager, speculative decoding, and server. For the model&\#x27;s novel structures, the authors built fused kernels—VHA cross-head mixing, Multi-Router latent MoE, MultiMax output head, and gated attention—reporting 1.55–6.53× per-kernel speedups over naive implementations with bitwise-identical selected outputs. FlashIndexer adds a lightweight dynamic head router and threshold pre-filtering to the sparse indexer, yielding a 1.4× speedup at 1M context. The default checkpoint uses FP4 QAT for W4A8 routed experts and FP8 elsewhere, and a bundled 3-layer DSpark draft model proposes up to 7 tokens per step with mean acceptance length above 4.0. The 43-layer model mixes 37 HCA and 6 MLA-DSA layers, routes tokens to top-10 of 512 experts, and supports data-parallel/expert-parallel plus PD disaggregation. Performance figures are vendor-reported.

**「Takeaway」** The plugin mechanism separates model-specific changes from vLLM core, allowing day-0 support while architecture-aware fusions, sparse indexer acceleration, FP4 QAT, and multi-stage speculative decoding make the large MoE&\#x27;s long-context inference efficient.

**Tags**: `#LLM inference`, `#vLLM`, `#mixture-of-experts`, `#kernel fusion`, `#speculative decoding`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic IPO Selloff Wipes $1.7 Trillion From Chinese Tech Stocks, Clouding AI Listings](https://www.bloomberg.com/news/articles/2026-11-23/china-s-next-ai-deals-clouded-by-selloff-after-anthropic-ipo) ⭐️ 8.0/10

Anthropic&\#x27;s record $119.5 billion IPO triggered a global stock selloff that erased $1.7 trillion from Chinese tech stocks since the end of June, clouding planned IPOs by DeepSeek, Moonshot AI, and Stepfun.

telegram · zaihuapd · Nov 23, 09:31

**「Background」** According to Bloomberg, DeepSeek, Moonshot AI, and Stepfun were all preparing or considering share offerings before the selloff.

**Tags**: `#Artificial Intelligence`, `#IPO`, `#China`, `#Stock Market Selloff`, `#Anthropic`

---

<a id="item-finance-news-2"></a>
### [Nvidia board reinstates Jensen Huang as CEO](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director) ⭐️ 8.0/10

Nvidia&\#x27;s board unanimously reinstated Jensen Huang as president, CEO, and board director, effective immediately, and said Colette Kress will continue as CFO. The board said it found no national security risk after consulting senior U.S. government officials; Bloomberg separately reported, citing unnamed people, that the decision was made without consulting management and after political pressure from President Trump.

telegram · zaihuapd · Nov 23, 14:02

**「Background」** Huang had been replaced on an interim basis by Kress following reports that he was a target of foreign intelligence activity; the board&\#x27;s independent investigation committee says its work will continue, and it has created a national-security and export-control committee and begun recruiting a chief compliance officer.

**Tags**: `#Nvidia`, `#corporate governance`, `#leadership change`, `#national security`, `#semiconductors`

---

<a id="item-finance-news-3"></a>
### [Shanghai Metro Adjusts Fares for First Time in 21 Years](https://weibo.com/1699432410/5368461393397183) ⭐️ 7.0/10

Shanghai Metro will adjust fares for the first time in 21 years, effective December 1. The new starting fare is 3 yuan for 0–4 km, with 1-yuan increments after 4, 4, 4, 7, 7, 10, and 10 km, and every 15 km above 50 km; four multi-ride passes \(35, 45, 60, or 90 rides for 190, 210, 270, or 390 yuan\) go on sale November 26, and spending 90 yuan in a month on one payment channel earns a 10% discount.

telegram · zaihuapd · Nov 23, 10:45

**「Background」** Shanghai Metro had kept its base fare structure unchanged for 21 years before this adjustment; a preliminary estimate cited in reporting put the previous average fare at 4.23 yuan per ride.

<details><summary>References</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260819A0ARAE00">时隔 21 ...</a></li>

</ul>
</details>

**Tags**: `#Shanghai Metro`, `#fare adjustment`, `#public transportation policy`, `#consumer prices`, `#urban economics`

---

<a id="item-finance-news-4"></a>
### [SpaceX reported to rent AI compute to Anthropic and Google, earning billions monthly](https://www.nytimes.com/2026/11/23/business/elon-musk-ai-anthropic-google.html) ⭐️ 7.0/10

The New York Times reported that since May this year, SpaceX has been renting compute from its data centers to Anthropic and Google, earning billions of dollars per month.

telegram · zaihuapd · Nov 24, 02:06

**「Background」** Three unnamed sources told the Times that Elon Musk said SpaceX is behind in AI and renting compute is more profitable than using it internally, and in August he renamed a team chat “Sell compute because we can&\#x27;t compete”.

**Tags**: `#SpaceX`, `#AI infrastructure`, `#Anthropic`, `#Google`, `#compute market`

---