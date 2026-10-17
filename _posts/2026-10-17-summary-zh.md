---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 40 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Claude 揭示 NIST ECDSA 曲线种子来源](#item-tech-news-1) ⭐️ 9.0/10
2. [JPEG XL 与 AVIF 网页图像格式对比](#item-tech-news-2) ⭐️ 8.0/10
3. [利用 OpenBSD 中隐藏 37 年的内核漏洞](#item-tech-news-3) ⭐️ 8.0/10
4. [开源 ORL 让扩散 LLM 单卡 RTX 5090 达 2,788 tokens/s](#item-tech-news-4) ⭐️ 8.0/10
5. [苹果 MLX 在 Mac Studio 集群运行近万亿参数模型](#item-tech-news-5) ⭐️ 7.0/10
6. [研究：AI 基准未覆盖九成美国实际工作任务](#item-tech-news-6) ⭐️ 7.0/10
7. [Anthropic Claude Code 团队改用持续自动化代码审查](#item-tech-news-7) ⭐️ 7.0/10
8. [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [AI 数据中心多项上市计划被撤回或暂停，亚洲并购交易额翻倍](#item-finance-news-1) ⭐️ 7.0/10
2. [商务部就人工智能、生物医药、光伏 40 项技术出口管理公开征求意见](#item-finance-news-2) ⭐️ 7.0/10
3. [Anthropic IPO 估值预期降至约 1.5 万亿美元](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude 揭示 NIST ECDSA 曲线种子来源](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10

Anthropic 的 Claude 在不到半小时内发现 NIST P-192、P-224、P-256、P-384 和 P-521 曲线种子并非来自任何哈希算法，而是由 C 库的 lrand48 随机数生成器以 Unix 时间戳作为种子生成。这一发现解开了长期存在的密码学谜团，驳斥了关于 NIST 曲线后门的怀疑。不过，第五个二进制种子 B-163 仍无法用该方法解释，最可能的原因是发布时输入错误。社区指出，这一结果只证实了生成方式，并不能排除通过搜索时间戳来选取具有特定性质的曲线的可能性。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**「背景」** 美国国家标准与技术研究院（NIST）在 2000 年前后发布的椭圆曲线数字签名算法（ECDSA）标准中包含多条曲线（P-192、P-224、P-256、P-384、P-521）的种子值，这些种子用于生成曲线参数，但其来源长期未公开，因而被怀疑可能隐藏后门。Anthropic 公司的内部研究模型 Claude 在 2026 年 10 月追溯发现，这些种子并非来自任何哈希算法，而是 C 库中 lrand48 伪随机数生成器的输出，并以 Unix 时间戳作为随机种子。外部报道确认对应时间戳约为 1997 年 5 月至 1998 年 4 月，说明生成过程与当时常规做法一致。

**「影响」** 对依赖 NIST ECDSA 曲线的系统而言，种子来源的澄清降低了曲线被恶意构造的风险，但 B-163 的未解释和“可能丢弃候选曲线”的保留意见意味着尚不能完全排除选择性构造。

**「社区讨论」** 多数评论认为这终结了持续十余年的 NIST 后门阴谋论，但 fidotron 等提醒：生成方式不等于选择方式，曲线是在数月内生成，无法看到被丢弃的候选，仍可设想通过搜索时间戳来挑选具备特定属性的曲线；B-163 仍无解释，可能只是发布时打错数字。

<details><summary>参考链接</summary>
<ul>
<li>Anthropic Says Claude Traced NIST ECDSA Curve Seeds to a ... - Unite.AI</li>
<li>Claude discovered nist p-192 seed origins - Facebook</li>
<li>Claude Traces NIST ECDSA Curve Seeds to Unix Timestamps - HyperAI</li>

</ul>
</details>

**标签**: `#cryptography`, `#ECDSA`, `#NIST`, `#AI`, `#software-security`

---

<a id="item-tech-news-2"></a>
### [JPEG XL 与 AVIF 网页图像格式对比](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

这篇文章对 JPEG XL 与 AVIF 在网页场景中的表现进行了技术对比，涵盖压缩性能、工具链和实际部署建议。文章通过性能数据说明两种格式在不同类型图像上的体积与质量差异，并讨论了编码速度、参数调优以及兼容性等影响选型的因素。其核心价值在于为 Web 开发者提供基于数据的格式选择依据，而非仅凭格式宣传。

hackernews · farlight · 10月16日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**「背景」** JPEG XL 和 AVIF 是两种面向 Web 的现代图像格式，均旨在替换传统的 JPEG、PNG 和 WebP，提供更好的压缩效率或额外功能（如无损、HDR、透明、渐进渲染）。AVIF 基于 AV1 视频编解码器的帧内压缩，而 JPEG XL 是专门设计的静态图像编解码器，支持有损与无损、HDR 和渐进式解码。本条目发布时，JPEG XL 已在所有主流浏览器中落地，Jake Archibald 的文章通过实际基准测试比较二者在文件大小、编解码速度、内存占用等 Web 使用场景下的表现。

**「影响」** 对于需要在网页中部署现代图像格式的开发者，该比较提供了基于压缩性能与工具链数据的选型参考，帮助避免仅凭宣传决定。

**「社区讨论」** 社区中既有用户分享 AVIF 的 ffmpeg 调参经验以实现小体积与透明支持，也有评论指出 AVIF 在汽车高光等细节上会擦除并替换为“看似合理”的伪影。另有观点提醒应等待编解码器进一步成熟，类似 MP3 和 WebP 曾经历的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jakearchibald.com/2026/jpeg-xl-vs-avif/">JPEG XL vs AVIF for web use-cases - JakeArchibald.com</a></li>
<li><a href="https://daily.dev/posts/jpeg-xl-vs-avif-for-web-use-cases-omcokbhou">JPEG XL vs AVIF for web use-cases - daily.dev</a></li>
<li><a href="https://news.e-ink.me/en/archive/2026-10-16/article/jpeg-xl-vs-avif-for-web-use-cases">JPEG XL vs AVIF for web use-cases | E-Ink News Daily</a></li>

</ul>
</details>

**标签**: `#image compression`, `#web performance`, `#JPEG XL`, `#AVIF`, `#codec comparison`

---

<a id="item-tech-news-3"></a>
### [利用 OpenBSD 中隐藏 37 年的内核漏洞](https://calif.io/research/big-fish) ⭐️ 8.0/10

该文章详细分析了一个在 OpenBSD 中存活了 37 年的内核漏洞及其利用过程。尽管 OpenBSD 以严格的安全审计著称，该漏洞仍长期未被发现，凸显了仅靠代码审查难以发现某些深层内核缺陷。文章通过实际利用展示了这一漏洞的可利用性，并讨论了长期存活的漏洞对系统安全的警示意义。

hackernews · rs\_rs\_rs\_rs\_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**「背景」** OpenBSD 内核源自最初的 BSD 代码，其 SysV 共享内存附加计数器是一个有符号 16 位整数，可追溯到约 37 年前。攻击者通过 fork 259 个进程使该计数器溢出，并与之竞态造成释放后使用，再结合 IP 多播选项处理中的越界写入，可绕过 SMAP/SMEP 实现本地提权。安全公司 Calif 于 2026 年 10 月 16 日发布了概念验证利用代码，相关漏洞已被修复。

**「社区讨论」** 社区评论指出，该漏洞很可能在 1999 年 8 月 NetBSD 重写相关代码时被意外修复。还有评论认为，这类缺陷未必能被模糊测试或静态分析发现，可能需要人工构造利用原语才能暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/37-year-old-kernel-openbsd-flaw/">37-Year-Old Kernel Flaw Exploited to Gain Root Access on ...</a></li>
<li><a href="https://thedailytechfeed.com/37-year-old-kernel-bug-in-openbsd-finally-patched-after-root-exploit-poc/">37-Year-Old Kernel Bug in OpenBSD Finally Patched After Root ...</a></li>
<li><a href="https://daily.dev/posts/big-fish-exploiting-a-37-year-old-kernel-bug-in-openbsd-u6hc8g4lt">Big Fish: Exploiting a 37-Year-Old Kernel Bug in OpenBSD</a></li>

</ul>
</details>

**标签**: `#openbsd`, `#kernel`, `#security`, `#vulnerability`, `#exploitation`

---

<a id="item-tech-news-4"></a>
### [开源 ORL 让扩散 LLM 单卡 RTX 5090 达 2,788 tokens/s](https://www.reddit.com/r/MachineLearning/comments/1x7qgr0/research_2788_tokenss_on_a_single_rtx_5090_with_a/) ⭐️ 8.0/10

研究人员发布开源方法 ORL（On-Policy Residual Learning）和推理引擎 dlmrt，用于加速扩散语言模型（dLLM）。在单请求解码（batch size 1）中，单张 RTX 5090 运行 LLaDA-2.1-mini + ORL（NVFP4）达到 2,788 tokens/s，8 张 B200 运行 DiffusionGemma 26B MoE + ORL 达到 7,708 tokens/s，自研 QwenDLM-4B 端到端吞吐最高提升 6.9 倍且 HumanEval pass@1 从 82.9%提高到 89.6%，并在 H100 上比 DFlash 快 1.74 倍且精度匹配。ORL 通过在线策略残差学习与相邻熵收缩，让模型每次前向传播确认更多 token；dlmrt 将整个去噪循环捕捉到 CUDA 图中并在 Blackwell GPU 上支持 NVFP4，比 SGLang/vLLM 快 1.2–1.6 倍。所有模型、训练代码、评测流程和推理引擎均已开源；以上数字是特定基准上的峰值结果，不代表任意提示的平均值。

reddit · r/MachineLearning · /u/arty\_photography · 10月16日 20:03

**「背景」** 扩散语言模型（dLLM）与传统自回归 LLM 不同，可在去噪步骤中并行生成和细化多个 token，但通常需要更多前向传播才能收敛。ORL 通过让模型携带上一步预测作为残差上下文并在线训练这些残差，减少去噪步数；dlmrt 则是针对低延迟单请求扩散解码的定制推理引擎。

**「影响」** 对于使用扩散语言模型的开发者和研究人员，开源的 ORL 方法与 dlmrt 引擎可将单请求解码速度提升至单个 RTX 5090 上 LLaDA-2.1-mini 的 2,788 tokens/s（NVFP4），显著降低本地推理延迟。需要注意的是，这些数字是特定基准上的峰值结果，而非任意提示词的平均性能。

**标签**: `#diffusion language models`, `#inference optimization`, `#open source`, `#machine learning research`, `#AI performance`

---

<a id="item-tech-news-5"></a>
### [苹果 MLX 在 Mac Studio 集群运行近万亿参数模型](https://machinelearning.apple.com/research/mlx-distributed-inference) ⭐️ 7.0/10

苹果机器学习研究团队演示了使用最新版 MLX 在由四台 Mac Studio 组成的集群上运行近万亿参数的 Muse Spark Open 模型，生成速度超过 36 tokens/s，高于人类平均阅读速度。该方案从单台 Mac Studio（最高 512GB 统一内存）起步，可横向扩展至多台设备。此次演示展示了在苹果硬件上本地运行前沿级开源模型的能力，并公布了具体性能数据。

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**「背景」** MLX 是苹果为 Apple Silicon 推出的机器学习框架，支持在 Mac 上本地及通过 RDMA 进行分布式大模型推理。Muse Spark Open 是 Meta 与苹果合作发布的开源权重模型，约 8160 亿参数（近万亿），针对苹果硬件（尤其是新 Mac Studio）优化，并已开放权重下载。

**「影响」** 该演示为本地运行近万亿参数模型提供了可行性参考，但评论区指出性能数据基于 8192 token 上下文，可能不足以支持当前常见的多轮对话或长文档任务。

**「社区讨论」** 评论区对苹果硬件运行大模型的能力表示认可，但也存在明显质疑。有评论指出基准测试将 Meta 模型以 4-bit 量化与 Qwen 的 BF16 原生精度对比不公平，且 Muse Spark 未进入其考虑前列；另有评论认为 8192 token 上下文过短，并给出单台 M5 Ultra 运行 DeepSeek 4.1 Flash 约 45 tokens/s 的对照数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://machinelearning.apple.com/research/mlx-distributed-inference">Local and Distributed Large LLM Inference with MLX and RDMA on...</a></li>
<li><a href="https://www.theverge.com/news/1012293/meta-apple-muse-spark-open-ai-model-mlx">Meta and Apple team up to make Muse AI models run better on Macs</a></li>

</ul>
</details>

**标签**: `#distributed-inference`, `#MLX`, `#Apple-silicon`, `#large-language-models`, `#performance`

---

<a id="item-tech-news-6"></a>
### [研究：AI 基准未覆盖九成美国实际工作任务](https://www.mercor.com/research/labor-index/benchmark-map/) ⭐️ 7.0/10

一项来自 Mercor 的研究将美国劳动者实际任务与现有 AI 基准提示进行映射，发现约 90% 的美国工作小时所对应的任务几乎没有或完全没有被现有基准覆盖。该研究通过任务级映射量化了这一差距，指出其使模型在美国劳动者实际从事的工作上的真实表现难以评估。因此，现有基准对真实劳动场景下 AI 能力的判断存在明显盲区，引发了对模型实际性能的质疑。

hackernews · speckx · 10月16日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**「背景」** AI 基准测试是通过标准化任务集评估模型能力的方法；O\*NET 是美国劳工部的职业信息网络，将职业分解为具体任务。Mercor 的研究将 29 个公开的智能体基准映射到 O\*NET 的 924 项任务（共 18,797 项），以量化基准对实际工作的覆盖情况，并发现现有基准集中在少数高薪、AI 暴露度高的职业任务上。

**「影响」** 对于依赖 AI 基准进行模型选型或自动化评估的团队，这一覆盖缺口意味着当前评测分数可能无法代表模型在大部分美国实际岗位上的表现。

**「社区讨论」** 评论者对“覆盖良好”的定义提出质疑，举例称“社会工作者及照护——就育儿问题向父母提供咨询”仅由 13 条提示复盖，难以代表真实任务。另有评论引用门卫谬误和 Baumol 成本病，并提到 AI 实际只处理约 2–5% 的工作，且基准过度偏向高薪职业任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mercor.com/research/labor-index/benchmark-map/">A benchmark map of the US economy | Mercor</a></li>
<li><a href="https://runtimewire.com/article/mercor-benchmark-map-human-work-thesis">Mercor estimates 90% of US work hours lack AI benchmark coverage</a></li>
<li><a href="https://www.explainx.ai/blog/mercor-benchmark-map-90-percent-us-working-hours-not-covered-ai-benchmarks-2026">AI Benchmark Coverage: 90% of US Work Is Unmeasured ...</a></li>

</ul>
</details>

**标签**: `#ai-benchmarks`, `#ai-evaluation`, `#labor-automation`, `#economics`, `#research`

---

<a id="item-tech-news-7"></a>
### [Anthropic Claude Code 团队改用持续自动化代码审查](https://simonwillison.net/2026/Oct/16/code-review/) ⭐️ 7.0/10

西蒙·威利森引用了 Anthropic Claude Code 团队博客作者 Addy Osmani、Morgan Westlee Lunt 和 Qing Wang 的观点。该团队认为，“是否有人读过代码”是对“哪里可能出错，以及自动化或人工检查哪个更合适”的不精确代理。这一认识改变了审查时机：过去审查是流程末端的门禁，写完代码、开 PR、等同事；现在审查持续进行，更像写作时的拼写检查。大多数变更在请人查看前至少已被 Claude 审查并修复过一次。这能捕捉大多数常规错误，把团队注意力留给更高层次的问题和审查。

rss · Simon Willison · 10月16日 22:06

**「背景」** 这句话出自 Anthropic Claude Code 团队在 claude.dev 发布的博客文章，作者为 Addy Osmani、Morgan Westlee Lunt 和 Qing Wang。传统代码审查把“人类是否读过代码”作为合并前的最终门禁，但智能体大量产出代码后，团队转为连续运行自动化审查，目标是在不增加回滚或事故的前提下，尽量减少人工审查时间。

**「影响」** 对于采用 Claude Code 的团队，这意味着可以将代码审查从 PR 末端的人工门禁转变为持续自动检查，从而减少常规错误并让人工审查专注于更高层次问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.dev/blog/solving-code-review-at-anthropic/">How the Claude Code team does code review / claude.dev Blog</a></li>

</ul>
</details>

**标签**: `#ai`, `#code-review`, `#software-engineering`, `#anthropic`, `#claude-code`

---

<a id="item-tech-news-8"></a>
### [阶跃星辰发布 Step 5 Preview 智能体旗舰模型](https://huggingface.co/stepfun-ai/Step-5-Preview) ⭐️ 7.0/10

阶跃星辰在 Hugging Face 发布旗舰模型 Step 5 Preview，主要面向智能体工作。该模型采用稀疏 MoE 架构，总参数 6000 亿、激活参数 270 亿，支持最高 100 万 token 上下文，可接收文本、图像和视频输入。官方称其在软件工程、长周期智能体执行和专业知识任务上表现领先，尤其擅长金融场景。模型可通过 OpenAI 兼容 API 配合 vLLM 或 SGLang 部署，并采用 StepFun Model License 1.0 许可。目前该版本为 Preview 状态。

telegram · zaihuapd · 10月16日 06:36

**「背景」** Step 5 Preview 被定位为阶跃星辰的新一代开源旗舰基础模型。模型采用稀疏 MoE 架构，将 6000 亿总参数划分为多个专家，推理时仅激活约 270 亿参数，以平衡能力与计算成本；百万 token 上下文主要面向长文档和长周期智能体任务。第三方 Artificial Analysis 评测显示其综合得分进入全球开源模型前三，为“旗舰”定位提供了外部参照。

**「对开发者与组织的影响」** 开发者现在可通过 OpenAI 兼容 API 配合 vLLM 或 SGLang 部署 Step 5 Preview，获得 100 万 token 上下文的多模态智能体能力，尤其适用于软件工程和金融任务。其预览状态和 StepFun Model License 1.0 许可意味着生产采用仍需谨慎评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7687542245026922496">阶 跃 星 辰 发布 Step 5 Preview ：600B MoE...</a></li>
<li><a href="https://post.smzdm.com/p/ak8kd7zk/">体验完 Step 5 Preview ，我发现 阶 跃 重新坐上国产大 模 型 主桌_IT...</a></li>
<li><a href="https://www.woshipm.com/ai/6467696.html">实测 Step 5 Preview ，又一个能打的国产 模 型 来了 | 人人都是产品经理</a></li>

</ul>
</details>

**标签**: `#large language model`, `#agentic AI`, `#sparse MoE`, `#multimodal`, `#model release`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [AI 数据中心多项上市计划被撤回或暂停，亚洲并购交易额翻倍](https://www.kitco.com/news/off-the-wire/2026-10-15/market-selloff-rising-rates-test-ai-data-centre-deal-boom) ⭐️ 7.0/10

过去一周，AirTrunk 的 REIT 上市计划、英伟达支持的 Firmus 及软银支持的 SB Energy 上市安排均因市场抛售和利率上升被撤回或暂停。据 Dealogic 数据，今年亚洲数据中心并购交易额达 213 亿美元，约为 2025 年全年 100 亿美元的两倍，股权融资同比下降 4.6%。

telegram · zaihuapd · 10月16日 05:10

**「背景」** 此前，黑石支持的 AirTrunk 已因利率上升和 REIT 板块下跌推迟了原计划融资约 15 亿美元的新加坡 REIT 上市，英伟达支持的 Firmus 也取消了 55 亿美元的 IPO，市场对未建成基础设施的估值保持怀疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/asia-pacific/airtrunk-delay-singapore-ipo-wsj-reports-2026-10-13/">Blackstone-backed AirTrunk delays Singapore REIT IPO amid AI ...</a></li>
<li><a href="https://www.ainvest.com/news/blackstone-ai-data-center-deals-unsteady-2610/">Blackstone’s AI Data Center Deals Appear Unsteady | AInvest</a></li>

</ul>
</details>

**标签**: `#AI data centers`, `#IPO withdrawals`, `#interest rates`, `#M&amp;A`, `#equity financing`

---

<a id="item-finance-news-2"></a>
### [商务部就人工智能、生物医药、光伏 40 项技术出口管理公开征求意见](https://aqygzj.mofcom.gov.cn/flzc/gzjgfxwj/art/2026/art_c99f95ca0cd043829ac9991495fc283c.html) ⭐️ 7.0/10

商务部拟修订《中国禁止出口限制出口技术目录》并公开征求意见，涉及人工智能、生物医药、光伏三个领域共 40 项技术。

telegram · zaihuapd · 10月16日 09:12

**「背景」** 该目录用于管理中国禁止或限制出口的技术；此次修订尚在征求意见阶段，尚未正式实施。

**标签**: `#export controls`, `#technology policy`, `#China`, `#artificial intelligence`, `#photovoltaics`

---

<a id="item-finance-news-3"></a>
### [Anthropic IPO 估值预期降至约 1.5 万亿美元](https://www.reuters.com/business/finance/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-2026-10-15/) ⭐️ 7.0/10

Anthropic 第三季度营收 168 亿美元、环比增长 45%并实现经调整盈利，但部分投资者已将其 IPO 估值预期从 2 万亿美元下调至约 1.5 万亿美元，理由包括增速放缓、模型价格竞争加剧及算力投入压力。

telegram · zaihuapd · 10月16日 15:46

**「背景」** Anthropic 预计在 11 月上市；此前部分投资者曾讨论约 2 万亿美元的 IPO 估值，高于当前约 1.5 万亿美元的下调预期。

**「影响」** 该预期下调可能成为中国 AI 公司（如智谱、MiniMax、Kimi、DeepSeek）的估值压力测试，市场将更关注收入持续性、毛利率和资本效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beincrypto.com/anthropic-ipo-valuation-1-5-trillion/">Anthropic ’s $2 Trillion IPO Dream Meets a $ 1 . 5 Trillion Reality Check</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI sector`, `#valuation`

---