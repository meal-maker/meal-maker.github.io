---
layout: default
title: "Horizon Summary: 2026-10-26 (EN)"
date: 2026-10-26
lang: en
---

> From 28 items, 5 important content pieces were selected

---

**Technology News**
1. [Brotli CVE-2026-111497 RCE Impacts Python, Node.js HTTP Components](#item-tech-news-1) ⭐️ 8.0/10
2. [10-Year-Old CNN Beats Frontier LLMs for Skin Cancer Diagnosis](#item-tech-news-2) ⭐️ 7.0/10
3. [Nanbeige Releases Apache 2.0 33B Teacher Model for Smaller Agents](#item-tech-news-3) ⭐️ 7.0/10
4. [Apple to unveil first touchscreen MacBook Pro Wednesday](#item-tech-news-4) ⭐️ 7.0/10

**Financial News**
1. [China&\#x27;s population falls 3.39 million in 2025 to 1.40489 billion](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Brotli CVE-2026-111497 RCE Impacts Python, Node.js HTTP Components](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

A critical vulnerability in Google&\#x27;s Brotli decoder, CVE-2026-111497, has been assigned a CVSS 4.0 score of 9.2 and affects Brotli versions 1.0.3 through 1.2.0. Remote unauthenticated attackers can send a specially crafted compressed stream to trigger memory corruption, sensitive data disclosure, process crashes, or potential arbitrary code execution. The flaw impacts Python and Node.js HTTP components and was initially disclosed as Node2Shell before being renamed HTTP2Shell. Fixed versions include Python Brotli 1.2.1 and brotlicffi 1.2.1.0, as well as Node.js 22.23.4, 24.22.1, or 26.12.1; OpenAI reported discovering the issue in February of this year.

telegram · zaihuapd · Oct 25, 02:42

**「Background」** Brotli is a lossless compression format developed by Google and widely used for HTTP content encoding, making its decoder a common attack surface when processing untrusted network data. The vulnerability is in the decoder and can be triggered by remote unauthenticated attackers through compressed streams. CVSS 4.0 is a scoring system used to communicate severity, with 9.2 indicating critical risk.

**「Impact」** Organizations using Brotli 1.0.3–1.2.0 in Python or Node.js components are at immediate risk of remote code execution and should upgrade to the specified patched versions \(Python Brotli 1.2.1, brotlicffi 1.2.1.0, Node.js 22.23.4/24.22.1/26.12.1\).

**Tags**: `#security`, `#vulnerability`, `#Brotli`, `#Python`, `#Node.js`

---

<a id="item-tech-news-2"></a>
### [10-Year-Old CNN Beats Frontier LLMs for Skin Cancer Diagnosis](https://lynchlab.net/llm-skin-cancer) ⭐️ 7.0/10

A fine-tuned Inception v3 CNN, roughly 10 years old, outperformed frontier large language models at classifying skin cancer from dermoscopic and clinical images. The model was pretrained on everyday photographs and then fine-tuned on all layers using 68,011 images from the ISIC Archive on a single H100 GPU. Evaluation used 200 held-out test lesions, with all images of the same lesion or patient removed from training and validation to prevent data leakage. The result demonstrates that specialized computer-vision models can be more accurate than general-purpose LLMs for medical imaging tasks. Frontier LLMs were not competitive despite their scale and general capabilities.

hackernews · sungam · Oct 25, 17:15 · [Discussion](https://news.ycombinator.com/item?id=50233779)

**「Background」** Convolutional neural networks \(CNNs\) like Inception v3 are image-classification architectures that can be fine-tuned on specialized datasets; frontier LLMs, by contrast, are general-purpose multimodal models trained on broad web data rather than optimized for pixel-level medical diagnosis. The ISIC Archive provides a large public collection of dermoscopic and clinical skin-lesion images used for benchmarking such models.

**「Impact」** For developers and clinicians working on skin-lesion classification, a dedicated fine-tuned CNN is likely the better tool than a frontier LLM, based on this comparison. The finding is limited to this dataset and task.

**「Community Discussion」** Commenters largely found the result unsurprising, comparing LLMs to a calculator for arithmetic and to specialized models like KataGo that beat LLMs in Go. One commenter noted the test design was &\#x27;benchmaxxing,&\#x27; while another recalled earlier arguments that LLMs would be useful for cancer diagnosis.

<details><summary>References</summary>
<ul>
<li><a href="https://lynchlab.net/llm-skin-cancer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#computer vision`, `#LLMs`, `#medical AI`

---

<a id="item-tech-news-3"></a>
### [Nanbeige Releases Apache 2.0 33B Teacher Model for Smaller Agents](https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/) ⭐️ 7.0/10

Nanbeige has released Nanbeige4.3-33B, an Apache 2.0-licensed model intended as a teacher for smaller agents, including an upcoming 3B model, with a reported 512K context window. The releasing team reports a score of 80.9 on Terminal-Bench 2.1, compared with 73.0 for Qwen3.8-27B, using the same harness and inference settings within each benchmark. On SWE-Bench Pro, the reported scores are 60.3 versus 61.7, so the model does not win everywhere. These are the team&\#x27;s own evaluations, not independent replication. The agent evaluations retain earlier reasoning with preserve\_thinking=true, which the model card recommends for multi-turn tool use but not for general chat, and the submitter notes that comparing task success and total generated tokens with that setting fixed would be more meaningful than headline scores.

reddit · r/MachineLearning · /u/jatingargiitk · Oct 25, 16:32

**「Background」** Nanbeige4.3-33B is a 33-billion-parameter dense transformer model released by Nanbeige LLM Lab under the Apache 2.0 license. It has a context window of up to 524,288 tokens \(512K\), supports English and Chinese, and is designed for agentic coding, tool use, and professional &\#x27;cowork&\#x27; tasks with reasoning enabled by default. The model is described by the team as the flagship &\#x27;teacher&\#x27; model for the Nanbeige4.3 series, which is intended to guide smaller agents including an upcoming 3B model.

**「Impact」** Open-source agent builders gain an Apache 2.0 33B teacher model with a 512K context window, but its benchmark lead over Qwen3.8-27B is currently supported only by the releasing team&\#x27;s own evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>
<li><a href="https://aiweekly.co/alerts/nanbeige-opens-33b-model-under-apache-20-with-512k-context">Nanbeige Opens 33B Model Under Apache 2.0 With 512K Context</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>

</ul>
</details>

**Tags**: `#open-source LLM`, `#agentic AI`, `#Apache 2.0`, `#benchmarks`, `#software engineering`

---

<a id="item-tech-news-4"></a>
### [Apple to unveil first touchscreen MacBook Pro Wednesday](https://www.bloomberg.com/news/newsletters/2026-10-25/apple-to-unveil-touch-screen-macbook-pro-executive-promotions-in-box-checker) ⭐️ 7.0/10

Apple will unveil its first touchscreen MacBook Pro this Wednesday, Bloomberg reports. The new Mac will be the first in the lineup to support touch and an OLED screen and will add Dynamic Island, coming in 14-inch and 16-inch versions and priced higher than the current $2,499 starting price. Apple executives have long rejected touchscreen laptops on ergonomic grounds, and the shift is driven more by revenue and marketing, with touch acting as a supplement to the keyboard and trackpad. The move reflects a change in Apple&\#x27;s attitude toward being more willing to reconsider and adjust its approach.

telegram · zaihuapd · Oct 25, 14:25

**「Background」** Apple has avoided touchscreens on Mac notebooks for years, with executives citing ergonomic reasons, even as touch-enabled Windows laptops became common. Dynamic Island, first introduced on iPhone 14 Pro, is a flexible display notch that shows system alerts and live activities. Recent reports said the first touchscreen MacBook Pro models would use OLED panels and add Dynamic Island, expected with M5 Pro and M5 Max chips.

**「Impact」** MacBook Pro buyers will be able to use touch as an additional input method on OLED displays with Dynamic Island, but at a higher starting price than the current $2,499.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macworld.com/article/2931833/touchscreen-macbook-pro-design-processor-specs-release.html">Touchscreen MacBook Pro: OLED, design and release date rumors</a></li>
<li><a href="https://www.macworld.com/article/3070324/touchscreen-macbook-pro-to-feature-dynamic-island-and-big-macos-changes.html">Apple’s touchscreen MacBook Pro might get its own Dynamic Island</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#MacBook Pro`, `#touchscreen`, `#OLED`, `#hardware`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China&\#x27;s population falls 3.39 million in 2025 to 1.40489 billion](https://weibo.com/1796087453/5357878513767954) ⭐️ 7.0/10

China&\#x27;s population fell by 3.39 million in 2025 to 1.40489 billion at year-end, according to the 2026 China Statistical Yearbook, with 7.92 million births and a natural growth rate of -2.41 per 1,000 people \(births minus deaths\).

telegram · zaihuapd · Oct 25, 12:02

**「Background」** According to the China Statistical Yearbook 2026, nine provinces had birth rates above 7‰ and seven had positive natural growth, mostly in western and southern China, while Heilongjiang, Jilin, and Liaoning had the lowest birth rates.

**「Economic impact」** The decline in total population, particularly among working-age people, may reduce labor supply and consumer spending, affecting businesses dependent on young workers and domestic markets.

<details><summary>References</summary>
<ul>
<li><a href="https://t.me/linux_do_channel/545902">LINUX DO Channel – Telegram</a></li>
<li><a href="https://www.brookings.edu/wp-content/uploads/2010/11/1127_china_wang.pdf">Untitiled</a></li>

</ul>
</details>

**Tags**: `#population decline`, `#China demographics`, `#birth rate`, `#macroeconomic data`, `#natural growth`

---