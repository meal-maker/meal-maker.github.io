---
layout: default
title: "Horizon Summary: 2026-11-16 (ZH)"
date: 2026-11-16
lang: zh
---

> 从 36 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [Meta FAIR 与 NYU：视觉编码器预训练可选但视觉专用参数必要](#item-tech-news-1) ⭐️ 8.0/10
2. [美团开源 LongCat-2.5：训练未用英伟达 GPU](#item-tech-news-2) ⭐️ 8.0/10
3. [理解现代大语言模型中的位置嵌入](#item-tech-news-3) ⭐️ 7.0/10
4. [让 B300 上的 cudaMemcpy 速度提升 5 倍的工具](#item-tech-news-4) ⭐️ 7.0/10
5. [鲁比奥与 Anthropic 疑为“猎杀”黄仁勋推手](#item-tech-news-5) ⭐️ 7.0/10
6. [华为云上线开源盘古模型 openPangu-2.1-Pro](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [卢特尼克面临英伟达相关利益冲突质疑，其子公司英伟达持仓减半](#item-finance-news-1) ⭐️ 7.0/10
2. [美法官驳回美光、三星、SK 海力士 DRAM 价格操纵案撤诉动议](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Meta FAIR 与 NYU：视觉编码器预训练可选但视觉专用参数必要](https://www.reddit.com/r/MachineLearning/comments/1xx1k2o/meta_fair_nyu_unbundling_multimodal_vision/) ⭐️ 8.0/10

Meta FAIR 与 NYU 训练了 200 多个多模态 LLM，从零开始使用相同数据，以分离视觉编码器的三个耦合选择：单独预训练、仅视觉 token 使用的参数、以及编码器在 LLM 前的位置。结果显示单独预训练是可选：四种预训练目标即使在匹配计算量下最多与从零训练的编码器打平，MetaCLIP 预训练延长 6.5 倍虽将 ImageNet linear-probe 从 80.4% 提升到 84.4%，但未提升 VQA；而仅视觉参数是必须，无编码器模型在 0.6B 到 6.4B 各规模落后，需约 3 倍计算量才能追平。置于 LLM 之前也非必须：在 1.7B–6.4B 下，将零初始化的视觉专用注意力投影和 FFN 注入 LLM 前 8 层的 &\#x27;in-fusion&\#x27; 与编码器相当，且首 token 时间降低约 13%；1.7B 时前 8 层视觉分支 VQA 达 45.0（编码器 44.4），而文本共享为 42.3、置于后 8 层为 35.1，使用预训练 LLM 时结论一致。

reddit · r/MachineLearning · /u/trungh98 · 11月15日 17:38

**「背景」** 当前实验室对视觉编码器存在分歧：Gemma 4 12B 去除编码器，Kimi K3 从零训练编码器，而 Inkling 2 Small 重新引入编码器。由于已发布模型在数据、计算量上不同且很少控制编码器预训练，无法单独回答这些架构选择；本研究将标准编码器拆为三个独立选择，以受控实验比较。

**「影响」** 对于多模态 LLM 开发者，这项研究提示可在 LLM 早期层分配视觉专用参数、跳过单独的视觉编码器预训练，在相同计算下达到或超过编码器基线并降低约 13% 首 token 时间，但完全无编码器的设计需要约 3 倍计算量才能追平。

**标签**: `#multimodal LLMs`, `#vision encoders`, `#model architecture`, `#pretraining`, `#empirical study`

---

<a id="item-tech-news-2"></a>
### [美团开源 LongCat-2.5：训练未用英伟达 GPU](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) ⭐️ 8.0/10

美团 LongCat 团队在模型正式发布一周后公布了 LongCat-2.5 的权重。该模型是 1.6 万亿参数的多模态 MoE 智能体模型，每个 token 激活约 480 亿参数，支持文本、图像和视频输入，专注于自主完成冗长多步骤任务尤其是编程任务。官方称训练全程使用华为升腾加速卡，未使用英伟达 GPU，权重以 MIT 许可证发布，可商用。其在 Terminal Bench v2.1 上得分为 88.4，略低于 Claude Opus 5 的 89.1。

telegram · zaihuapd · 11月15日 11:08

**「背景」** 美团 LongCat 系列此前已推出 LongCat-Next，其视觉建模思路是将原生分辨率视觉特征离散化为 token，再与文本在共享语义空间中对齐。LongCat-2.5 采用混合专家（MoE）架构，总参数约 1.6 万亿，每个 token 仅激活约 480 亿参数，以在控制算力成本的同时支撑多模态长程智能体任务。开源采用 MIT 协议，权重可商用、可二次训练；官方自托管指南仅覆盖华为升腾硬件，训练过程也未使用英伟达 GPU。

**「影响」** MIT 许可证意味着企业可将 LongCat-2.5 权重用于商业产品，且其训练不依赖英伟达 GPU，为受采购限制的团队提供了基于华为升腾的可复现训练与部署选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.meituan.com/2026/11/10/Meituan-LongCat-2.5-Open-Source.html">美团 LongCat-2.5 正式开源：从看见，到抵达 | 美团 · 技术团队</a></li>
<li><a href="https://pulse.adyog.com/insights/meituan-longcat-2-5-open-agent-model-huawei">Meituan LongCat-2.5: Open Agent Model, Huawei Ascend Guide</a></li>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-2.5">meituan-longcat/LongCat-2.5 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#open source`, `#large language models`, `#AI agents`, `#Huawei Ascend`, `#multimodal`

---

<a id="item-tech-news-3"></a>
### [理解现代大语言模型中的位置嵌入](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings) ⭐️ 7.0/10

这篇发表于 Sebastian Raschka 杂志的技术文章系统梳理了现代大语言模型中位置嵌入的实现与理论。文章面向实践者，重点讲解常见的位置嵌入方案（如旋转位置嵌入等）在 Transformer 中的工作机制。该内容属于教育性深度解析，并非新的技术突破，但在 Hacker News 上引发了从业者的关注。有读者指出，仅了解实现还不够，位置嵌入本质上对应群表示，例如旋转位置嵌入是平移群的表示。

hackernews · vismit2000 · 11月15日 12:14 · [社区讨论](https://news.ycombinator.com/item?id=50506376)

**「背景」** 在基于 Transformer 的大语言模型中，自注意力机制本身对 token 顺序不敏感，因此通常需要位置编码来注入顺序信息。绝对位置嵌入（如 GPT-2 所用方案）会在进入第一个 Transformer 块之前将可学习的绝对位置向量加到 token 嵌入上，并与固定上下文长度（最初为 1024 个位置）绑定；旋转位置嵌入（RoPE）则属于相对位置编码，旨在改善长序列处理和外推能力。

**「社区讨论」** 有评论认为文章主要侧重实现层面，深入理解位置嵌入需要借助群表示论；例如旋转位置嵌入是平移群的表示，这为参数化和可微学习提供了理论依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://daily.dev/posts/understanding-positional-embeddings-in-modern-llms-415mglzuo">Understanding Positional Embeddings in Modern LLMs</a></li>

</ul>
</details>

**标签**: `#positional-embeddings`, `#LLMs`, `#transformers`, `#deep-learning`, `#AI`

---

<a id="item-tech-news-4"></a>
### [让 B300 上的 cudaMemcpy 速度提升 5 倍的工具](https://www.reddit.com/r/MachineLearning/comments/1xx2n25/making_cudamemcpy_5x_faster_on_a_b300_p/) ⭐️ 7.0/10

作者 /u/makneeee 发布了一款工具，声称能将 NVIDIA B300 GPU 上可分页（pageable）cudaMemcpy 传输速度提升约 5 倍。其 Python 基准测试使用 PyTorch 创建一个 1 GiB 的 uint8 张量并复制到 GPU，默认测得约 10.2 GB/s，使用 \`cmt tune\` 后提升至 51.5 GB/s。该工具通过 \`cmt tune -- python bench.py\` 方式运行，并提供了博客说明和 GitHub 开源代码。目前演示范围限于可分页内存的 cudaMemcpy 传输，而非所有内存类型；成果来自作者自述，尚未提供独立验证或社区评论。

reddit · r/MachineLearning · /u/makneeee · 11月15日 18:20

**「背景：CUDA 分页内存与固定内存传输」** 在 CUDA 中，主机内存分为可分页（pageable）内存和固定（pinned）内存。使用 cudaMemcpy 从可分页内存向设备传输时，驱动通常会先把数据复制到一个固定内存缓冲区，再执行设备端传输，因此带宽可能低于直接使用固定内存。NVIDIA 文档指出两者使用相同的 cudaMemcpy 语法，但固定内存传输速率更高，并提供了 bandwidthtest 程序进行比较。

**「性能影响」** 在 NVIDIA B300 上使用开源工具 cudamemcpy-tuner 可将可分页（pageable）cudaMemcpy 的 1GB 张量传输吞吐从约 10.2 GB/s 提升至约 51.5 GB/s，约 5 倍加速；但该结果仅针对可分页传输，且来自作者自报的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/">How to Optimize Data Transfers in CUDA C/C++ | NVIDIA Technical...</a></li>
<li><a href="https://stackoverflow.com/questions/50184146/cuda-pinned-memory-vs-pageable-memory-tradeoffs">optimization - CUDA - Pinned Memory vs. Pageable ... - Stack Overflow</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#GPU`, `#performance optimization`, `#machine learning infrastructure`, `#data transfer`

---

<a id="item-tech-news-5"></a>
### [鲁比奥与 Anthropic 疑为“猎杀”黄仁勋推手](https://www.washingtonpost.com/technology/2026/11/13/behind-jensen-huangs-spy-scandal-shadow-war-trumps-ear-china/) ⭐️ 7.0/10

《华盛顿邮报》报道称，英伟达创始人黄仁勋离职背后疑似是一场针对他的“猎杀”。黄仁勋此前凭借与特朗普的私交成功游说放宽对华芯片出口，并公开批评对华鹰派“是耻辱、不爱国”，此举惹怒美国国安官员。报道指卢比奥借 CIA 情报撰写强硬备忘录向总统施压，而 Anthropic 则被怀疑是向媒体提供调查线索的幕后推手，因《纽约时报》记者曾收到“科技行业内部联系人”的线报去调查与黄仁勋有关的新加坡公司 Megaspeed，硅谷舆论将矛头指向 Anthropic 高管，但记者与 Anthropic 均未回应。Anthropic 与英伟达存在直接冲突：前者游说严格限制对华芯片出口、主张给西方 GPU 加“固件级锁”或追踪机制，后者则反对在芯片中装追踪和后门并成功推动放宽销售。如今反对芯片限制的阻力大减，众议院中国问题特别委员会主席等人正推动将三项新条款纳入年底重大国防法案，包括进一步限制高端 AI 芯片出口、强制芯片内置防走私追踪技术以及限制中国获取芯片制造设备。

telegram · zaihuapd · 11月15日 08:08

**「相关背景：黄仁勋卸任与芯片出口管制分歧」** 该事件发生在黄仁勋卸任英伟达 CEO 之后；美国国会已就芯片对华出口问题传唤黄仁勋与卢特尼克。与此同时，Anthropic 正推进约 1.4 万亿美元估值的 IPO，黄仁勋的退出被认为可能影响其上市进程及 AI 芯片供应链。背景中的核心分歧是：Anthropic 长期游说严格限制对华 GPU 出口并主张加入固件级追踪机制，而黄仁勋则反对在芯片中内置追踪或后门功能，并曾推动放宽对华销售。

**「影响」** 据路透社、CNBC 等报道，黄仁勋事件已使美国国会更可能通过收紧对华 AI 芯片出口的立法，并推动强制芯片内置防走私追踪技术的讨论升温。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techmeme.com/261113/p9">Source: at an August 2026 finance meeting, Jensen Huang interrupted...</a></li>
<li><a href="https://www.businessinsider.com/jensen-huang-fall-could-reshape-anthropic-ipo-ai-chip-race-2026-11">How Jensen Huang &#x27;s Fall Could Reshape Anthropic IPO and AI Chip ...</a></li>
<li><a href="https://www.politico.com/newsletters/decoded-by-politico/2026/11/13/a-jensen-huang-sized-hole-01164435">A Jensen Huang -sized hole - POLITICO</a></li>
<li><a href="https://www.reuters.com/legal/litigation/nvidia-spy-allegations-likely-spur-laws-to-tighten-chinas-access-ai-chips-2026-11-09/">Nvidia spy allegations likely to spur laws to tighten China&#x27;s ...</a></li>
<li><a href="https://www.technologyreview.com/2026/11/12/1148483/nvidia-chip-tracking/">Nvidia privately confirmed it could track chips to fight ...</a></li>
<li><a href="https://www.cnbc.com/2026/11/12/nvidia-trump-jensen-chip-export-controls-china-xi-.html">Nvidia fallout revives push for chip curbs ahead of China summit</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#chip export controls`, `#NVIDIA`, `#Anthropic`, `#US-China tech`

---

<a id="item-tech-news-6"></a>
### [华为云上线开源盘古模型 openPangu-2.1-Pro](https://mp.weixin.qq.com/s/8JfFmscBTDl_mPQMycD8Nw) ⭐️ 7.0/10

11 月 15 日，华为云在 MaaS 模型即服务平台上线开源盘古模型 openPangu-2.1-Pro。该版本围绕 Agent 开发、AI 编码和推理优化升级，基于超过 10 万条专项数据优化 Skills 触发与工具调用，重点适配鸿蒙 ArkTS 开发和升腾算子生成。模型已接入智果 AgentArts、码道 CodeArts、果办 OfficeAce 等产品。推理价格为输入 0.8 元/百万 tokens、输出 3.2 元/百万 tokens、缓存命中输入 0.016 元/百万 tokens。

telegram · zaihuapd · 11月15日 16:03

**「背景」** 此前，华为云已通知用户将停售并下线 openPangu-2.0-Flash 和 Pro 模型，服务于 11 月 30 日逐步停止，并建议迁移至 DeepSeek-V4.1-Flash-1017 与 GLM-5.3。因此，11 月 15 日上线 openPangu-2.1-Pro 属于华为云 MaaS 平台对开源盘古系列的迭代更新，替换旧版 Flash/Pro 模型。

**「影响」** 鸿蒙 ArkTS 与升腾算子开发者可使用该开源模型在华为云以 0.8 元/百万 tokens 输入、3.2 元/百万 tokens 输出的价格进行 Agent 工具调用与 AI 编码集成，降低适配成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/huawei-cloud-to-discontinue-pangu-2-0-models-recommends-deepseek-and-glm-alternatives">Huawei Cloud to Discontinue Pangu 2 .0 Models... | KuCoin</a></li>
<li><a href="https://pandaily.com/huawei-cloud-maas-openpangu-2-0-flash-pro-offline-nov-30-deepseek-v4-1-flash-glm-5-3">Huawei Cloud to Retire openPangu - 2 .0 Models From... - Pandaily</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Pangu`, `#open-source LLM`, `#AI coding`, `#HarmonyOS`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [卢特尼克面临英伟达相关利益冲突质疑，其子公司英伟达持仓减半](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 7.0/10

据 CNBC 报道，美国商务部长霍华德·卢特尼克因其儿子经营的坎托·菲茨杰拉德公司与英伟达的业务关系面临利益冲突质疑；该公司披露的英伟达持股数量在 2025 年 9 月至 2026 年 3 月间下降近 50%，至 178 万股。

rss · CNBC Finance · 11月15日 19:58

**「背景」** 此前 Axios 报道称，卢特尼克多次抵制对涉嫌向中国走私英伟达芯片的新加坡公司 Megaspeed 采取行动，而英伟达 CEO 黄仁勋已于周四辞职。目前没有证据表明卢特尼克的儿子提前知悉相关情报，或坎托的持仓变化与上述警告有关。

**标签**: `#Nvidia`, `#Howard Lutnick`, `#Cantor Fitzgerald`, `#export controls`, `#conflict of interest`

---

<a id="item-finance-news-2"></a>
### [美法官驳回美光、三星、SK 海力士 DRAM 价格操纵案撤诉动议](https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge) ⭐️ 7.0/10

美国法官 Noël Wise 驳回美光、三星和 SK 海力士要求撤销 DRAM 价格操纵集体诉讼的动议，认为原告提出的三家厂商同步限制供应证据使指控成立具有合理性；原告称价格最高上涨 500%，三家公司须在 12 月 7 日前回应。

telegram · zaihuapd · 11月15日 16:39

**「背景」** 该集体诉讼由 17 名个人和小企业提起，指控美光、三星、SK 海力士在一年内四次协同限制 DRAM 供应，导致价格最高上涨 500%；本次裁定仅是驳回被告撤诉动议，案件仍将继续审理。

**「后续影响」** 该程序性裁决使集体诉讼继续推进，美光、三星和 SK 海力士可能面临赔偿与法律成本，进而影响依赖 DRAM 的电子产品制造商和买家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/big-tech/judge-denies-motion-to-dismiss-dram-price-fixing-lawsuit-against-micron-samsung-and-sk-hynix-says-chipmakers-acted-like-hawks-flying-in-formation-finds-evidence-of-dram-collusion-plausible-after-500-percent-price-surge">Judge denies motion to dismiss DRAM price - fixing lawsuit against...</a></li>
<li><a href="https://finance.yahoo.com/technology/articles/judge-denies-motion-dismiss-dram-152445837.html?fr=sycsrp_catchall">Judge denies motion to dismiss DRAM price-fixing lawsuit ...</a></li>

</ul>
</details>

**标签**: `#DRAM price-fixing`, `#Micron Technology`, `#Samsung Electronics`, `#SK Hynix`, `#semiconductor litigation`

---