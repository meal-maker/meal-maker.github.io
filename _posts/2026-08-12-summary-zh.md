---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 45 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [Qwen 开源 2.4T 参数 MoE 模型 Qwen3.8-2.4T-A95B](#item-tech-news-1) ⭐️ 9.0/10
2. [Tailscale 追查数据库损坏至 16 年 SQLite WAL 重置缺陷](#item-tech-news-2) ⭐️ 8.0/10
3. [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 本地运行](#item-tech-news-3) ⭐️ 8.0/10
4. [xAI 发布 Grok 4.6：长时智能体与视觉升级](#item-tech-news-4) ⭐️ 8.0/10
5. [为何微型 JPEG 在 Chrome 中显示不同](#item-tech-news-5) ⭐️ 7.0/10
6. [uBlock Origin 停止尝试屏蔽 Facebook 广告](#item-tech-news-6) ⭐️ 7.0/10
7. [AI 正在消灭软件工程的中产阶级？](#item-tech-news-7) ⭐️ 7.0/10
8. [Adam 因逐坐标二阶矩破坏低秩隐式偏差](#item-tech-news-8) ⭐️ 7.0/10
9. [企业级 SSD 占 NAND 出货量 48%，长江存储首进前三](#item-tech-news-9) ⭐️ 7.0/10
10. [微信发布 WeLM：80B 用于小微，617B MoE 在研](#item-tech-news-10) ⭐️ 7.0/10

**科技博客**
1. [vLLM Day-0 支持 Qwen3.8-2.4T-A95B](#item-tech-blog-1) ⭐️ 5.0/10

**财经新闻**
1. [CME 推出 AI 算力期货合约，算力成为可交易资产](#item-finance-news-1) ⭐️ 8.0/10
2. [腾讯二季度营收 2048 亿元超预期，资本开支飙至 528 亿元致自由现金流转负](#item-finance-news-2) ⭐️ 8.0/10
3. [CNBC 午盘异动：Wendy&\#x27;s 因私有化消息涨 13%，Quantinuum、CoreWeave 等 AI 股走高](#item-finance-news-3) ⭐️ 7.0/10
4. [美股盘前：超微电脑、CoreWeave 等 AI 基础设施股因业绩指引超预期大涨](#item-finance-news-4) ⭐️ 7.0/10
5. [中国 7 月新能源汽车占乘用车销量 65.1%](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen 开源 2.4T 参数 MoE 模型 Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 在 Hugging Face 上开源发布了混合专家（MoE）语言模型 Qwen3.8-2.4T-A95B，总参数 2.4T，激活参数 95B。该模型原生上下文长度为 262,144 tokens，可扩展至 1,010,000 tokens。社区反馈显示此次只放出了 BF16 和 FP8 权重，未提供 QAT q4 量化版本，BF16 完整模型约 4.9TB。其许可证与 Kimi k3 类似，年收入低于 5000 万美元或内部使用可免费，超过阈值则对模型服务等有限制，因而被社区视为 Kimi k3 的竞品。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**「背景」** Qwen3.8-2.4T-A95B 是 Qwen 团队发布的开放权重稀疏混合专家（MoE）模型，总参数 2.4 万亿，激活参数 950 亿。混合专家模型通过每次仅激活部分专家来大幅降低推理计算量，同时保持极高的总参数量。该模型是 Qwen3.8-Max 的开放权重版本，官方 Max 版本在此基础上增加了视觉输入、非思考模式、默认 100 万 token 上下文长度以及内置工具等功能。

**「影响」** 对年收入低于 5000 万美元或仅内部使用的组织，可以免费使用该模型；但由于只发布 BF16/FP8 且缺少 QAT q4，部署起步硬件成本较高（BF16 约 4.9TB），需要社区或大算力方进一步量化才能降低服务门槛。

**「社区讨论」** 社区讨论主要关注部署成本：有评论称仅 BF16/FP8 权重使起步服务比 k3 更困难，缺少 QAT q4 需要大算力校准；同时 Unsloth 的 1-bit 量化版本约 397GB，被指可在消费级硬件上达到 Opus 4.5 级别。另有评论指出开源权重不包含官方版视觉输入、非思考模式、默认 1M 上下文与内置工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen 3 . 8 2 . 4 T A 95 B - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Open Source`, `#MoE`, `#Machine Learning`

---

<a id="item-tech-news-2"></a>
### [Tailscale 追查数据库损坏至 16 年 SQLite WAL 重置缺陷](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 在一篇技术博文中披露，其数据库损坏问题被追溯至 SQLite 中一个已存在 16 年的 WAL 重置缺陷。尽管该服务采用单进程独占 SQLite 数据库的单写入者设计，符合 SQLite 预期使用方式，但仍触发了该缺陷。为了定位问题，Tailscale 资助开发了一个开源 SQLite VFS shim，该工具几乎立即帮助隔离出竞态条件，并可用于未来类似缺陷的调试。公司还通过购买 SQLite 支持合同来推进修复，并计划继续支持该项目。这一案例展示了企业资助针对性开源调试工具的实践价值。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**「背景」** SQLite 是一种嵌入式关系数据库，支持 WAL（预写式日志）模式以提升并发读取性能。在 WAL 模式下，数据库文件可能被多个连接打开，而 WAL 重置（用于清理日志文件）与另一连接上的写事务并发执行时可能触发一个存在 16 年的缺陷，导致数据库损坏。Tailscale 使用 SQLite 作为其控制平面后端，去年遭遇的多次服务中断正是由该缺陷引起，该公司随后资助开发了一个开源 SQLite VFS shim 调试工具以定位问题。

**「影响」** 使用 SQLite WAL 模式的系统应关注此缺陷，并可从开源 VFS shim 中受益，但具体影响取决于并发和 WAL 重置路径。

**「社区讨论」** 社区普遍赞赏 Tailscale 详细的技术复盘及对开源调试工具的支持；有评论指出测试无法证明无缺陷，并认可其通过支持合同回馈 SQLite 的做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://news.ycombinator.com/item?id=49272832">Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug | Hacker News</a></li>
<li><a href="https://www.theregister.com/databases/2026/08/12/tailscale-says-deeply-buried-16-year-old-sqlite-bug-caused-last-years-outages/5287004">Tailscale says deeply buried 16-year-old SQLite bug caused last year&#x27;s outages</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#database`, `#debugging`, `#tailscale`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [LTX 发布开源视频模型 LTX-2.5，单张 RTX 5090 本地运行](https://ltx.io/model/ltx-2-5) ⭐️ 8.0/10

LTX 发布了开源视频生成基础模型 LTX-2.5，其权重、训练代码与推理管线全部开放。该模型同时支持文生视频与图生视频，改进了多镜头连贯性和提示词遵循，并采用新的扩散视频解码器与 Gemma 4 12B 文本编码器。它可在单张 RTX 5090 上本地运行，年收入低于 1000 万美元的用户可免费商用。在基于 98 个提示词的文生视频瑕疵评测中，LTX 2.5 Pro 在十款模型中排名第一。

telegram · zaihuapd · 8月12日 02:15

**「背景」** LTX 将开源视为世界模型扩展的路径，LTX-2.5 是其最新开放的视频生成模型，权重、训练代码和推理管线均公开。单张 RTX 5090 即可本地运行，说明模型针对消费级高端 GPU 进行了优化，使个人和小团队无需依赖云 API 也能生成视频。该模型采用 Gemma 4 12B 文本编码器和新的扩散视频解码器，以改善提示词遵循与多镜头连贯性。

**「影响」** 个人开发者和小型团队若年收入低于 1000 万美元，可在配备单张 RTX 5090 的本机环境中免费商用该模型，无需依赖付费云视频生成 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ltx.io/model/open-source">LTX-2.5 Model Open Source: AI Video Generator</a></li>
<li><a href="https://blogs.nvidia.com/blog/local-ai-open-source-models-agents-nemotron/">NVIDIA and Local AI Community Fuel Open Source Models and Intelligent Agents | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#open-source`, `#video-generation`, `#AI model`, `#local inference`, `#text-to-video`

---

<a id="item-tech-news-4"></a>
### [xAI 发布 Grok 4.6：长时智能体与视觉升级](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI 于 2026 年 8 月 12 日发布 Grok 4.6，在 Grok 4.5 基础上重点强化长时间运行的智能体与交互、视觉任务。该模型在综合九项基准的 Artificial Analysis 智能指数上与 GPT-5.6 Sol 持平。Grok 4.6 即日起上线 Cursor、Grok Build 及 API，定价为每百万输入 token 2 美元、输出 token 6 美元，另有双倍价格的快速版。发布首周在 Grok Build 和 Cursor 赠送双倍用量。

telegram · zaihuapd · 8月12日 15:54

**「背景」** Artificial Analysis 智能指数是综合多项基准衡量前沿模型能力的指标。Grok 是 xAI 的大模型系列，此前 Grok 4.5 已在部分用户中因快速、简洁而获好评。此次 4.6 升级重点解决长时间运行智能体和视觉任务中的不足。

**「影响」** 需要处理长时智能体或视觉任务的开发者可立即通过 Cursor、Grok Build 和 API 使用 Grok 4.6，并以每百万输入 token 2 美元、输出 token 6 美元的价格获得与 GPT-5.6 Sol 持平的智能指数表现，首周还可享双倍用量。

**「社区讨论」** 社区评论中，部分用户认可 Grok 的速度、简洁和 API 价格优势，并认为其对其他前沿模型形成健康竞争。也有用户反映 API 默认系统提示可能覆盖自定义指令并导致拒绝讨论系统提示，另有人质疑多家实验室约两个月内集体达到 Fable 水平存在基准刷分或蒸馏可能。

**标签**: `#AI`, `#LLM`, `#AI agents`, `#xAI`, `#Grok`

---

<a id="item-tech-news-5"></a>
### [为何微型 JPEG 在 Chrome 中显示不同](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

这篇调查探讨了 Chrome 渲染微型 JPEG 图像时与其他浏览器不同的原因，重点在于 Chrome 的图像缩放优化。作者建议不要用 JPEG 做图标等非照片图形，因为 JPEG 压缩伪影明显；PNG 无损且支持 alpha 更适合图标。社区评论补充，同样的优化进入 Electron 版本后曾破坏产品中的 PNG 图标，导致升级被搁置。Firefox 正在 Bugzilla 2033250 中推进低比例解压工作，且 Chrome 与 Firefox 的缩放算法差异也会造成模糊或振铃差异。

hackernews · gutechh · 8月12日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49272549)

**「背景」** JPEG 是有损压缩格式，适合照片；PNG 是无损格式，适合图标等需要清晰边缘和透明通道的图形。浏览器在显示小于原始尺寸的图像时会进行缩放，不同浏览器可能采用不同的缩放算法；Chrome 为提高性能会对缩放显示的 JPEG 采用更低质量或更快的解码方式，这会导致小尺寸 JPEG 在 Chrome 中看起来与其他浏览器不同。开发者在选择图片格式时应根据内容和显示尺寸匹配分辨率，以减少这类差异和资源浪费。

**「影响」** 依赖 Chrome/Electron 渲染小尺寸 JPEG 或 PNG 图标的 Web 开发者可能遇到图标模糊、伪影或跨浏览器不一致，应改用尺寸合适的 PNG。

**「社区讨论」** 社区共识是应避免用 JPEG 做图标，并使用与显示尺寸匹配的图像；有开发者称 Chrome 的优化进入 Electron 后破坏了多处图标，另有观点认为 Firefox 缩放更锐利但振铃略多，Chrome 更模糊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=8VoCua-dEu0">Reduce image size: use the correct format — PNG or JPEG - YouTube</a></li>

</ul>
</details>

**标签**: `#JPEG`, `#Chrome`, `#image scaling`, `#browser rendering`, `#web development`

---

<a id="item-tech-news-6"></a>
### [uBlock Origin 停止尝试屏蔽 Facebook 广告](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 7.0/10

开源广告拦截扩展 uBlock Origin 据报已停止尝试屏蔽 Facebook 广告，原因是 Facebook 采用了日益复杂的反广告拦截技术。这一变化引发了社区对广告拦截军备竞赛和隐私问题的讨论。该扩展是广泛使用的开源工具，放弃过滤 Facebook 广告意味着用户可能在该平台上看到更多广告。相关讨论出现在 Reddit 和 Neowin 的报道中，社区热度较高。

hackernews · Markoff · 8月12日 11:28 · [社区讨论](https://news.ycombinator.com/item?id=49270726)

**「背景」** uBlock Origin 是一款广泛使用的开源广告拦截浏览器扩展，依赖社区维护的过滤规则来屏蔽网页元素。Facebook 长期通过修改广告投放代码和反拦截机制来规避此类规则；uBlock Origin 开发团队此前一直维护针对 Facebook 的自定义过滤规则。根据 Neowin 等报道，2026 年 8 月开发团队宣布停止更新这些专门针对 Facebook 广告的过滤规则，因为 Facebook 的反广告拦截手段已使维护变得极其困难，部分用户开始看到广告。

**「影响」** 对于依赖 uBlock Origin 屏蔽 Facebook 广告的用户，这一决定意味着他们可能在 Facebook 上看到更多广告，除非改用其他解决方案或不再使用该平台。

**「社区讨论」** 社区讨论中，部分用户认为放弃屏蔽是正确决定，并指出最终可能只能通过弃用 Facebook 来避免广告；也有用户质疑 Facebook 绕过拦截的动机，认为拦截者通常不会点击广告，但 Facebook 可能追求广告展示量。另有用户预测，未来可能出现基于计算机视觉的广告屏蔽方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.neowin.net/news/facebook-ads-are-so-hard-to-block-that-ublock-origin-stopped-filtering-them/">Facebook ads are so hard to block that uBlock Origin ... - Neowin</a></li>
<li><a href="https://privacysavvy.com/news/cybersecurity/ublock-origin-stops-facebook-ad-filters/">uBlock Origin Stops Updating Filters Designed to Block Facebook ...</a></li>
<li><a href="https://piunikaweb.com/2026/08/10/ublock-origin-facebook-ads-not-blocking/">Seeing ads on Facebook even with uBlock Origin ? - PiunikaWeb</a></li>

</ul>
</details>

**标签**: `#ad-blocking`, `#uBlock Origin`, `#Facebook`, `#privacy`, `#open source`

---

<a id="item-tech-news-7"></a>
### [AI 正在消灭软件工程的中产阶级？](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 7.0/10

这篇博客文章认为，AI 正在通过自动化常规编码工作，移除软件工程领域的“中产阶级”，即那些主要从事常规实现工作的工程师。这一观点认为，常规编码任务正被 AI 承担，从而减少了对这类中层岗位的需求。该文章在 Hacker News 上引发了广泛辩论，但作为观点文章，它没有提供具体数据或技术细节来支撑其论断。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994)

**「背景」** 在软件工程语境中，“中产工程师”通常指那些主要价值在于将规格说明转化为可工作代码的中级开发者，有时也被称为“Stack Overflow 工程师”。过去这类岗位的高薪往往源于人才稀缺，而非单纯因为代码编写本身难以替代。随着大语言模型编程工具普及，许多原本需要人工完成的常规实现工作正在被自动化，价值向负责架构和复杂决策的高级工程师倾斜，中间层因此受到挤压。

**「社区讨论」** Hacker News 评论者担心 AI 会放大“糟糕工程师”的破坏力，把“StackOverflow 工程师”的常规工作自动化；也有人提醒不应将批判性思维外包给 LLM。同时，有评论者质疑目前是否已有确凿证据表明 LLM 编码代理导致了软件工程岗位流失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html">AI is removing the middle class of software engineering</a></li>
<li><a href="https://news.ycombinator.com/item?id=49271994">AI is removing the middle class of software engineering | Hacker News</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#labor market`, `#technology industry`, `#opinion`

---

<a id="item-tech-news-8"></a>
### [Adam 因逐坐标二阶矩破坏低秩隐式偏差](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 7.0/10

一项研究在分解模型 W=UV^T 中考察损失对旋转 \(U,V\)→\(UQ,VQ\) 的基不变性，发现 GD 会保留这种不变性，但 Adam 的逐坐标二阶矩依赖因子写法而破坏它。作者在欠定矩阵感知任务上比较了九种更新规则，匹配训练损失后出现两簇：GD、共享标量 Adam、Muon 和 Shampoo 保留 GD 的隐式低秩偏差；Adam、RMSProp、Lion、signum 和 Adafactor 丢失该偏差。通过把 Adam 分母从逐坐标改为单一共享标量的单参数族，恢复效果单调改善，表明损伤来自各向异性而非一般性自适应。Muon 在真正低秩目标上表现准确，但加入谱尾后最快退化，在约 4% 尾能量附近与 GD 交叉；作者还发现用全局范数裁剪替换逐坐标裁剪使恢复误差从 0.347 降至 0.220。论文提醒超光谱数据上 43–44% 的留出误差减少使用仅训练集学习率规则，且该规则让 Adam 拿到最差学习率；若各方法自选最优学习率差距会明显缩小，理论仅覆盖无记忆规则，动量部分仍属经验。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**「背景：基不变性与优化器的隐式偏置」** 在因子分解模型 W=UV^T 中，损失函数对旋转 \(U,V\)→\(UQ,VQ\) 保持不变，即同一预测可以用不同基表示；梯度下降按各坐标同向更新，因而保留这种对称性，而 Adam 的逐坐标二阶矩依赖于所选的基，从而打破不变性。这种差异被用来研究优化器在训练损失匹配时的隐式低秩偏置：它们会选择不同的插值解，即使损失相同。相关论文在 arXiv:2608.05136 中系统比较了九种更新规则，并用单参数消融实验验证了这一机制。

**「影响」** 对于使用分解模型且依赖隐式低秩偏差的从业者，选择 Adam、RMSProp、Lion、signum 或 Adafactor 可能系统性丢失 GD 的低秩诱导行为，而共享标量 Adam、Muon 或 Shampoo 更可能保留该行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05136">The Loss Does Not See the Basis, but Adam Does</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimization`, `#Adam`, `#implicit bias`, `#matrix sensing`

---

<a id="item-tech-news-9"></a>
### [企业级 SSD 占 NAND 出货量 48%，长江存储首进前三](https://china.counterpointresearch.com/%e6%9c%8d%e5%8a%a1%e5%99%a8%e9%9c%80%e6%b1%82%e6%8e%a8%e5%8d%87%e4%bc%81%e4%b8%9a%e7%ba%a7-ssd-%e5%8d%a0-nand-%e5%87%ba%e8%b4%a7%e9%87%8f%e7%99%be%e5%88%86%e4%b9%8b-48/) ⭐️ 7.0/10

Counterpoint 报告显示，受 AI 推理工作负载推动，2026 年第二季度企业级 SSD 占全球 NAND 出货量的 48%，同比接近翻倍，行业营收较去年同期增长五倍。三星以 25%份额领跑，SK 海力士以 22%居第二，长江存储以 14%首次超越铠侠跻身第三，但因产品偏消费级，其营收仅排第五。报告预计年底企业级 SSD 将消耗超一半 NAND 位元总量。

telegram · zaihuapd · 8月12日 11:00

**「背景」** NAND 闪存是固态硬盘等存储介质的基础，企业级 SSD 面向服务器和数据中心，对性能、耐久性和稳定性要求更高。AI 推理工作负载需要高速大容量存储，推动企业级 SSD 需求快速上升。

**「影响」** 长江存储首次进入全球 NAND 出货量前三，但产品结构偏消费级导致其营收仅排第五，说明其在高价值企业级 SSD 市场仍需追赶。

**标签**: `#enterprise SSD`, `#NAND`, `#YMTC`, `#AI infrastructure`, `#storage market`

---

<a id="item-tech-news-10"></a>
### [微信发布 WeLM：80B 用于小微，617B MoE 在研](https://x.com/Weixin_WeChat/status/2087509298310209718) ⭐️ 7.0/10

微信团队正式发布通用大语言模型家族 WeLM，强调“以极致的资源效率拓展智能边界”。其中 WeLM-80B 总参数 80B、激活 3B，已应用于微信内 AI 智能体“小微”，支持对话、搜索、操作微信原生功能及调用小程序服务。研发中的 WeLM-617B 总参数 617B、激活 23B，采用混合专家（MoE）架构，在中等激活规模下提升通用理解与推理能力，计划用于小程序智能开发、“微信小微”小工具生成等复杂任务。该发布展示了腾讯/微信在低成本大规模部署 LLM 方面的具体进展，但官方未提供独立验证数据。

telegram · zaihuapd · 8月12日 13:58

**「背景」** 混合专家（MoE）架构通过每次仅激活部分参数来降低推理成本，是大模型资源效率优化的常见方向。公开资料显示，微信 WeLM 团队曾在 2026 年 1 月分享 80B-A3B MoE 模型的预训练经验，称该模型在不足 14T tokens 语料上性能具有竞争力；后续发布的 Hidden Decoding 博客又披露了 617B MoE 采用隐式序列缩放路径，以中等激活规模提升通用理解与推理能力。

**「影响」** 微信用户已能通过“小微”使用 WeLM-80B 完成对话、搜索、原生功能操作和小程序调用，而 WeLM-617B 未来将面向开发者提供小程序智能开发等复杂任务能力。但 WeLM-617B 尚未上线，其实际效果有待验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hao.cnyes.com/post/260644">把思考折叠进序列：WeLM 617B MoE的隐式Scaling路径 | 科技 | 巨亨号 | Anue巨亨</a></li>
<li><a href="https://finance.sina.cn/2026-07-24/detail-iniiwrah9261623.d.html?vt=4&amp;cid=76993&amp;node_id=76993">把思考折叠进序列：WeLM 617B MoE的隐式Scaling路径|scaling law|Token|大模型|微信|博客_手机新浪网</a></li>
<li><a href="https://welm.weixin.qq.com/posts/building-effective-sparse-moe-models-with-moderate-resources/">以适度资源构建高效稀疏 MoE 模型 | WeLM Blog</a></li>

</ul>
</details>

**标签**: `#LLM`, `#WeChat`, `#MoE`, `#AI agent`, `#resource efficiency`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM Day-0 支持 Qwen3.8-2.4T-A95B](https://vllm.ai/blog/2026-08-12-qwen3.8) ⭐️ 5.0/10

rss · vLLM Blog · 8月12日 00:00

**「背景」** Qwen 团队发布了首个开放权重的 Qwen-Max 级模型 Qwen3.8-2.4T-A95B。该模型基于 Qwen 3.5 架构，拥有 2.4 万亿参数和 512 个专家，并混合全注意力与线性注意力层；由于规模大，全精度推理需多节点 GPU。vLLM 团队宣布复用现有架构即可实现 Day-0 支持。

**「方案」** Inferact 团队在官方 FP8/BF16 之外发布了 NVFP4 与 MXFP4 量化权重，通过对路由专家等选定层进行 RTN 量化并校准激活，使 4-bit 权重和激活在降低显存与带宽的同时保持精度。作者展示的 GSM8K 与 AIME25 基准中，NVFP4 得分与 FP8 相当甚至更高（如 AIME25@3 平均分 92.22% 对 87.78%），但需增大推理预算。为高效运行 2.4T 模型，vLLM 与 NVIDIA、AMD 联合开发线性注意力、GQA、MoE 路由等融合内核，并组合数据并行、张量并行与专家并行；官方推荐 temperature=1.0、top\_p=0.95 等生成参数，并提示为推理模型设置高 max\_tokens。

**「启示」** 这一 Day-0 支持说明：通过 FP4 量化和多供应商内核优化，Qwen-Max 级稀疏 MoE 模型可在较少 GPU 上部署，降低了大规模开源推理的门槛。

**标签**: `#vLLM`, `#Qwen`, `#sparse MoE`, `#quantization`, `#model serving`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [CME 推出 AI 算力期货合约，算力成为可交易资产](https://www.cnbc.com/2026/08/11/ai-computing-power-becomes-a-tradable-asset-class-as-cme-starts-futures.html) ⭐️ 8.0/10

芝加哥商品交易所集团（CME Group）将于 10 月 5 日（待监管批准）推出首批基于 Silicon Data GPU 租赁指数的 AI 算力期货合约，每份合约代表一个月 Nvidia H100 的租金。

rss · CNBC Finance · 8月12日 14:14

**「背景」** 该合约以 Silicon Data 追踪的 Nvidia H100 和 Blackwell B200 图形处理器（GPU）每小时租赁价格为基准，为买卖双方提供公开可交易的参考价格，类似石油或电力等大宗商品。

**「影响」** AI 开发商和数据中心运营商可借此对冲算力成本或收入，投资者则无需直接持有数据中心或芯片即可获得对算力价格的风险敞口。

**标签**: `#AI`, `#futures`, `#CME Group`, `#Nvidia`, `#financial innovation`

---

<a id="item-finance-news-2"></a>
### [腾讯二季度营收 2048 亿元超预期，资本开支飙至 528 亿元致自由现金流转负](https://wallstreetcn.com/articles/3779275) ⭐️ 8.0/10

腾讯控股 2026 年 Q2 营收 2048 亿元，同比增长 11%，略超彭博预期；净利润仅增 0.7%至 560 亿元，低于市场预期。资本支出同比近翻三倍至 528 亿元，自由现金流为-138 亿元。

telegram · zaihuapd · 8月12日 10:30

**「背景」** 公司称，剔除 AI 算力预付款后自由现金流为 376 亿元，显示本季度资本开支扩大是自由现金流转负的直接原因。

**标签**: `#腾讯`, `#财报`, `#资本开支`, `#AI投资`, `#自由现金流`

---

<a id="item-finance-news-3"></a>
### [CNBC 午盘异动：Wendy&\#x27;s 因私有化消息涨 13%，Quantinuum、CoreWeave 等 AI 股走高](https://www.cnbc.com/2026/08/12/stocks-making-the-biggest-moves-midday-wen-hrb-qnt-crwv-cava.html) ⭐️ 7.0/10

CNBC 报道 8 月 12 日美股午盘多只股票大幅波动：Wendy&\#x27;s 因《金融时报》援引消息人士称 Trian Fund Management 准备发出私有化收购要约而上涨 13%，Quantinuum 因 2026 年收入指引高于预期上涨逾 21%。

rss · CNBC Finance · 8月12日 16:53

**「背景」** 这些异动主要来自公司财报、业绩指引或并购消息，并与 FactSet 或 LSEG 汇总的分析师一致预期做对比。

**标签**: `#stock market`, `#earnings`, `#mergers and acquisitions`, `#artificial intelligence`

---

<a id="item-finance-news-4"></a>
### [美股盘前：超微电脑、CoreWeave 等 AI 基础设施股因业绩指引超预期大涨](https://www.cnbc.com/2026/08/12/stocks-making-the-biggest-moves-premarket-crwv-smic-cohr.html) ⭐️ 7.0/10

美股盘前，超微电脑、CoreWeave、Nebius 等 AI 相关公司因财报和指引超预期上涨，Cava 和 H&amp;R Block 也走高。其中，超微电脑将第一财季调整后每股收益指引设在 1.01 至 1.10 美元，高于 LSEG 共识 0.76 美元；CoreWeave 第二财季调整后营业利润率为 5%，高于 FactSet 共识 2.7%。

rss · CNBC Finance · 8月12日 12:12

**「背景」** 财报季中，公司公布的盈利、营收和未来指引常与 LSEG、FactSet 等汇总的分析师共识预期比较，超预期通常推动盘前股价上涨。

**标签**: `#earnings`, `#premarket`, `#stock-movers`, `#guidance`, `#AI-infrastructure`

---

<a id="item-finance-news-5"></a>
### [中国 7 月新能源汽车占乘用车销量 65.1%](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

中国 7 月新能源汽车占乘用车销量的 65.1%，高于去年同期的 54%；1—7 月乘用车整体销量同比下降 20.3%。

rss · CNBC Finance · 8月12日 01:20

**「背景」** 汽车之家数据显示，截至 7 月的六个月里，吉利星愿以近 19.75 万辆居畅销车型首位，特斯拉 Model Y 以超 18 万辆排名第二，比亚迪有三款车型进入前十。

**标签**: `#China auto market`, `#electric vehicles`, `#BYD`, `#Geely`, `#Tesla`

---