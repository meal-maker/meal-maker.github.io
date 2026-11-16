---
layout: default
title: "Horizon Summary: 2026-11-16 (EN)"
date: 2026-11-16
lang: en
---

> From 36 items, 8 important content pieces were selected

---

**Technology News**
1. [Unbundling Vision Encoders: Pretraining Optional, Vision-Only Parameters Required](#item-tech-news-1) ⭐️ 8.0/10
2. [Meituan open-sources LongCat-2.5, trained without Nvidia GPUs](#item-tech-news-2) ⭐️ 8.0/10
3. [Understanding Positional Embeddings in Modern LLMs](#item-tech-news-3) ⭐️ 7.0/10
4. [Open-Source Tool Claims 5x Faster Pageable cudaMemcpy on NVIDIA B300](#item-tech-news-4) ⭐️ 7.0/10
5. [Rubio and Anthropic Suspected of Orchestrating Jensen Huang Campaign](#item-tech-news-5) ⭐️ 7.0/10
6. [Huawei Cloud Releases Open-Source Pangu Model openPangu-2.1-Pro](#item-tech-news-6) ⭐️ 7.0/10

**Financial News**
1. [Cantor Fitzgerald cut reported Nvidia shares by nearly 50% amid Lutnick conflict questions](#item-finance-news-1) ⭐️ 7.0/10
2. [US Judge Denies Motion to Dismiss DRAM Price-Fixing Lawsuit Against Micron, Samsung, SK Hynix](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Unbundling Vision Encoders: Pretraining Optional, Vision-Only Parameters Required](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

Meta FAIR and NYU trained over 200 multimodal LLMs from scratch on the same data to isolate three bundled vision encoder choices. They found separate vision encoder pretraining is optional: encoders pretrained with four objectives at best tie scratch-trained encoders at matched compute, and even free pretraining does not improve VQA. Vision-only parameters are necessary: encoder-free models trail at every size from 0.6B to 6.4B and need about 3x the compute to catch up, while giving the LLM the encoder parameters improves text but not VQA. Placement before the LLM is optional: an in-fusion approach that adds zero-initialized vision-only weights to the LLM&\#x27;s first 8 layers matches an encoder from 1.7B to 6.4B with about 13% lower time to first token. Main comparisons use Qwen3-1.7B and 4B configurations with 0.4B parameters of vision capacity, evaluated on 16 VQA benchmarks and 12 language benchmarks.

reddit · r/MachineLearning · /u/trungh98 · Nov 15, 17:38

**「Background」** Current multimodal LLM labs disagree on vision encoder design: Gemma 4 12B removed the encoder, Kimi K3 trains it from scratch, and Inkling 2 Small reintroduced it. A standard encoder bundles three choices—separate pretraining, vision-only parameters, and placement before the LLM—which published models cannot isolate because they vary in data and compute.

**「Impact」** For practitioners and architects, the evidence suggests they can skip separate vision encoder pretraining and even the encoder itself if they add dedicated vision-only parameters inside the LLM, potentially reducing time to first token by about 13% without losing VQA performance.

**Tags**: `#multimodal LLMs`, `#vision encoders`, `#model architecture`, `#pretraining`, `#empirical study`

---

<a id="item-tech-news-2"></a>
### [Meituan open-sources LongCat-2.5, trained without Nvidia GPUs](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

Meituan&\#x27;s LongCat team has released the weights for LongCat-2.5 one week after the model&\#x27;s official launch. The 1.6-trillion-parameter mixture-of-experts agent model is designed for long, multi-step autonomous tasks, especially coding, and activates about 48 billion parameters per token. It supports text, image, and video input and was trained entirely on Huawei Ascend accelerators without using Nvidia GPUs, according to the team. The weights are published under the MIT license, allowing commercial use. On Terminal Bench v2.1, LongCat-2.5 scores 88.4, slightly below Claude Opus 5&\#x27;s 89.1.

telegram · zaihuapd · Nov 15, 11:08

**「Background」** Mixture-of-Experts \(MoE\) architectures activate only a subset of parameters per token, enabling models with very large total parameter counts while keeping inference compute manageable. Huawei Ascend is a family of AI accelerator chips developed by Huawei, positioned as an alternative to Nvidia GPUs, particularly in China. LongCat-2.5 builds on Meituan&\#x27;s earlier LongCat-Next model, adding multimodal inputs and long-horizon agentic reinforcement learning for complex software engineering tasks.

**「Impact」** Developers can now use and modify LongCat-2.5 commercially under the MIT license, while its claimed Huawei Ascend-only training demonstrates a viable large-model path that avoids Nvidia GPUs. The training-hardware claim is reported from Meituan and was not independently verified in the source item.

<details><summary>References</summary>
<ul>
<li><a href="https://pulse.adyog.com/insights/meituan-longcat-2-5-open-agent-model-huawei">Meituan LongCat-2.5: Open Agent Model, Huawei Ascend Guide</a></li>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-2.5">meituan-longcat/LongCat-2.5 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#open source`, `#large language models`, `#AI agents`, `#Huawei Ascend`, `#multimodal`

---

<a id="item-tech-news-3"></a>
### [Understanding Positional Embeddings in Modern LLMs](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

Sebastian Raschka&\#x27;s article offers a technical deep-dive into positional embeddings, the mechanisms that let transformer-based LLMs encode token order. The submission describes it as covering both implementation details and theoretical context relevant to practitioners, though the full text is not included in the hackernews item. Positional embeddings are a core architectural component affecting sequence modeling in modern LLMs, and the article is educational rather than a novel research announcement.

hackernews · vismit2000 · Nov 15, 12:14 · [Discussion](https://news.ycombinator.com/item?id=50506376)

**「Background」** Transformer-based LLMs require positional encoding because self-attention treats tokens independently of their order. Early approaches, such as GPT-2&\#x27;s learned absolute position embeddings, add a learned position vector to each token embedding before the first transformer block and are tied to a fixed context length \(1,024 positions originally\). More recent methods like rotary positional embeddings \(RoPE\) encode relative positions differently, and Raschka&\#x27;s article surveys these schemes across 2025 and 2026 open-weight architectures.

**「Impact」** Practitioners implementing or fine-tuning LLMs can use this article to understand how different positional embedding approaches affect model behavior and architecture choices.

**「Community Discussion」** A commenter argues that the article focuses on implementation but lacks the deeper theory, stating that positional embeddings are group representations and that rotary positional embeddings correspond to representations of the translation group.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/understanding-positional-embeddings-in-modern-llms-415mglzuo">Understanding Positional Embeddings in Modern LLMs</a></li>
<li><a href="https://sebastianraschka.com/blog/">Blog and Notes - Sebastian Raschka, PhD Positional embeddings in modern LLMs: from GPT-2 to RoPE and ... RoPE vs NoPE: Modern LLM Position Encoding (2026 ... No Positional Embeddings (NoPE) | Sebastian Raschka, PhD Ahead of AI | Sebastian Raschka, PhD | Substack</a></li>

</ul>
</details>

**Tags**: `#positional-embeddings`, `#LLMs`, `#transformers`, `#deep-learning`, `#AI`

---

<a id="item-tech-news-4"></a>
### [Open-Source Tool Claims 5x Faster Pageable cudaMemcpy on NVIDIA B300](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

A Reddit post by /u/makneeee describes an open-source tool, cudamemcpy-tuner, that tunes pageable cudaMemcpy transfers on an NVIDIA B300 GPU and reports a roughly 5x speedup. In the included Python benchmark, copying a 1 GB uint8 tensor from CPU to GPU with PyTorch measured 10.2 GB/s baseline, while running under \`cmt tune -- python bench.py\` measured 51.5 GB/s. The tool is invoked as a command wrapper and targets pageable \(non-pinned\) host memory, which is the slower path for CUDA copies. The post includes benchmark code, a blog post, and a GitHub repository, but the result is presented by the tool&\#x27;s author and has not been independently verified.

reddit · r/MachineLearning · /u/makneeee · Nov 15, 18:20

**「Pageable vs. pinned memory in CUDA」** In CUDA, host-to-device transfers via cudaMemcpy are faster when the host memory is pinned \(page-locked\) because the driver can use direct memory access; pageable memory may first be copied to a pinned staging buffer, reducing throughput. Python frameworks like PyTorch often use pageable memory by default, so improving pageable transfer speed is relevant for common workloads.

**「Impact」** Users running pageable CPU-to-GPU transfers on NVIDIA B300 GPUs can use this tool to increase throughput from about 10.2 GB/s to 51.5 GB/s, a 5x speedup for a 1 GB PyTorch tensor.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA Technical...</a></li>
<li><a href="https://stackoverflow.com/questions/50184146/cuda-pinned-memory-vs-pageable-memory-tradeoffs">optimization - CUDA - Pinned Memory vs. Pageable ... - Stack Overflow</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU`, `#performance optimization`, `#machine learning infrastructure`, `#data transfer`

---

<a id="item-tech-news-5"></a>
### [Rubio and Anthropic Suspected of Orchestrating Jensen Huang Campaign](https://www.washingtonpost.com/technology/2026/11/13/behind-jensen-huangs-spy-scandal-shadow-war-trumps-ear-china/) ⭐️ 7.0/10

The Washington Post reports suspicions that US Senator Marco Rubio and AI company Anthropic helped orchestrate a campaign against NVIDIA founder Jensen Huang that preceded his departure and renewed calls for stricter AI chip export controls. Huang had used his personal relationship with Donald Trump to win relaxed chip sales to China and publicly called China hawks “a disgrace and unpatriotic,” angering national security officials; Rubio reportedly wrote a hardline memo citing CIA intelligence to pressure the president. Anthropic is suspected of feeding the New York Times an initial tip about a Singapore company, Megaspeed, linked to a woman involved with Huang, although neither the journalist nor Anthropic has confirmed this. Anthropic has lobbied for strict export limits and firmware-level locks or tracking on Western GPUs to block unapproved open-source models, directly opposing Huang&\#x27;s stance against tracking and backdoors. With resistance to a chip restriction bill now significantly reduced, the House China select committee chair is pushing three new provisions into the year-end defense bill: further restricting high-end AI chip exports, mandating built-in anti-smuggling tracking technology, and limiting China&\#x27;s access to chip manufacturing equipment.

telegram · zaihuapd · Nov 15, 08:08

**「Background: Huang&\#x27;s exit and the AI-chip lobbying fight」** Jensen Huang built Nvidia into the leading AI-chip supplier and used his personal relationship with President Trump to oppose strict export controls on chips to China before resigning as CEO. Anthropic, an AI company with a competing lobbying agenda, has pushed the White House for tighter restrictions, including firmware-level locks or tracking mechanisms in GPUs. Meanwhile, Congress has summoned Huang and Lutnick over chip exports and is moving to add export-control and anti-smuggling provisions to the year-end defense bill, while Huang&\#x27;s exit has created a vacuum across Silicon Valley and raised questions about Anthropic&\#x27;s IPO and US-China AI chip policy.

**「Likely impact」** The alleged campaign against Jensen Huang is likely to accelerate passage of stricter AI chip export restrictions, mandatory chip anti-smuggling tracking technology, and limits on China&\#x27;s access to chipmaking equipment in the year-end defense bill, tightening constraints on NVIDIA and other high-end chip suppliers and on China&\#x27;s access to AI hardware. However, the underlying suspicions about Rubio and Anthropic remain unconfirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techmeme.com/261113/p9">Source: at an August 2026 finance meeting, Jensen Huang interrupted...</a></li>
<li><a href="https://www.businessinsider.com/jensen-huang-fall-could-reshape-anthropic-ipo-ai-chip-race-2026-11">How Jensen Huang &#x27;s Fall Could Reshape Anthropic IPO and AI Chip ...</a></li>
<li><a href="https://www.politico.com/newsletters/decoded-by-politico/2026/11/13/a-jensen-huang-sized-hole-01164435">A Jensen Huang -sized hole - POLITICO</a></li>
<li><a href="https://www.reuters.com/legal/litigation/nvidia-spy-allegations-likely-spur-laws-to-tighten-chinas-access-ai-chips-2026-11-09/">Nvidia spy allegations likely to spur laws to tighten China&#x27;s ...</a></li>
<li><a href="https://www.technologyreview.com/2026/11/12/1148483/nvidia-chip-tracking/">Nvidia privately confirmed it could track chips to fight ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/12/nvidia-trump-jensen-chip-export-controls-china-xi-.html">Nvidia fallout revives push for chip curbs ahead of China summit</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#chip export controls`, `#NVIDIA`, `#Anthropic`, `#US-China tech`

---

<a id="item-tech-news-6"></a>
### [Huawei Cloud Releases Open-Source Pangu Model openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

On November 15, Huawei Cloud launched the open-source openPangu-2.1-Pro model on its MaaS platform, focusing on Agent development, AI coding, and inference optimization. The model was optimized with over 100,000 specialized data items to improve Skills triggering and tool calling, with particular support for HarmonyOS ArkTS development and Ascend operator generation. It is integrated into Zhiguo AgentArts, Madao CodeArts, and Guoban OfficeAce. Pricing is set at 0.8 yuan per million input tokens, 3.2 yuan per million output tokens, and 0.016 yuan per million cached input tokens.

telegram · zaihuapd · Nov 15, 16:03

**「Context」** Huawei Cloud&\#x27;s Model-as-a-Service \(MaaS\) platform hosts large language models, including the Pangu series. Huawei Cloud previously announced that the openPangu-2.0 Flash and Pro models would be discontinued, with services ending by November 30, and recommended users transition to DeepSeek-V4.1-Flash-1017 and GLM-5.3. The newly launched openPangu-2.1-Pro is the successor model on this platform, targeting Agent development, AI coding, and inference optimization.

**「Impact」** Developers targeting HarmonyOS ArkTS or Ascend on Huawei Cloud MaaS can use this open-source model for improved tool calling and coding at the listed per-token prices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/huawei-cloud-to-discontinue-pangu-2-0-models-recommends-deepseek-and-glm-alternatives">Huawei Cloud to Discontinue Pangu 2 .0 Models... | KuCoin</a></li>
<li><a href="https://pandaily.com/huawei-cloud-maas-openpangu-2-0-flash-pro-offline-nov-30-deepseek-v4-1-flash-glm-5-3">Huawei Cloud to Retire openPangu - 2 .0 Models From... - Pandaily</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Pangu`, `#open-source LLM`, `#AI coding`, `#HarmonyOS`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Cantor Fitzgerald cut reported Nvidia shares by nearly 50% amid Lutnick conflict questions](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

CNBC reported that Cantor Fitzgerald, now led by Commerce Secretary Howard Lutnick&\#x27;s sons, cut its reported Nvidia share count by nearly 50% between September 2025 and March 2026 amid questions over Lutnick&\#x27;s ties to Nvidia and alleged chip smuggling to China. CNBC found no evidence the sons had advance knowledge or that the share decline was tied to intelligence warnings.

rss · CNBC Finance · Nov 15, 19:58

**「Background」** The scrutiny follows Nvidia CEO Jensen Huang&\#x27;s resignation Thursday and Axios reports that Lutnick repeatedly resisted a crackdown on companies suspected of smuggling Nvidia chips to China.

**Tags**: `#Nvidia`, `#Howard Lutnick`, `#Cantor Fitzgerald`, `#export controls`, `#conflict of interest`

---

<a id="item-finance-news-2"></a>
### [US Judge Denies Motion to Dismiss DRAM Price-Fixing Lawsuit Against Micron, Samsung, SK Hynix](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

A US judge denied a motion to dismiss a DRAM price-fixing class action against Micron, Samsung, and SK Hynix, finding plaintiffs&\#x27; new evidence of coordinated supply restrictions made collusion plausible; the plaintiffs allege prices rose as much as 500%.

telegram · zaihuapd · Nov 15, 16:39

**「Background」** This is only a preliminary ruling, not a final decision on the accusations. DRAM \(dynamic random-access memory\) is the standard memory chip used in computers and smartphones.

**「Impact」** The ruling keeps the proposed consumer and small-business class action against Micron, Samsung, and SK Hynix alive, requiring the companies to answer the complaint by December 7 and scheduling a case management conference for January 2027.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge">Judge denies motion to dismiss DRAM price - fixing lawsuit against...</a></li>
<li><a href="https://www.techpowerup.com/354863/samsung-sk-hynix-and-micron-fail-to-get-dram-antitrust-suit-dismissed">Samsung , SK hynix , and Micron Fail to Get DRAM Antitrust Suit ...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/judge-denies-motion-dismiss-dram-152445837.html?fr=sycsrp_catchall">Judge denies motion to dismiss DRAM price-fixing lawsuit ...</a></li>

</ul>
</details>

**Tags**: `#DRAM price-fixing`, `#Micron Technology`, `#Samsung Electronics`, `#SK Hynix`, `#semiconductor litigation`

---