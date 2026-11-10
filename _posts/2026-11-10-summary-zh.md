---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 46 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [本周任意地点的卫星过境与照片](#item-tech-news-1) ⭐️ 8.0/10
2. [消费者版 Gemini 被曝将个人 Drive 文件与邮件交给人工标注](#item-tech-news-2) ⭐️ 8.0/10
3. [潜在预测优于重建：LingBot-Touch 触觉预训练](#item-tech-news-3) ⭐️ 8.0/10
4. [SwarmEvolve：潜空间 KV 缓存混合加速进化式数学发现](#item-tech-news-4) ⭐️ 8.0/10
5. [谷歌推出 TPU 8tx 和 8i Max 加速挑战英伟达](#item-tech-news-5) ⭐️ 8.0/10
6. [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](#item-tech-news-6) ⭐️ 7.0/10
7. [E-means：以十分之一轮数超越 k-means](#item-tech-news-7) ⭐️ 7.0/10
8. [2026 论文主题页更新基准](#item-tech-news-8) ⭐️ 7.0/10
9. [字节跳动发布 Seedream 5.5，支持百轮编辑与原生透明素材](#item-tech-news-9) ⭐️ 7.0/10
10. [欧盟数字公平法案拟限成瘾设计](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [英伟达董事会调查黄仁勋，预测市场认为其短期离职概率低](#item-finance-news-1) ⭐️ 8.0/10
2. [前三季度新能源车出口增长 138.8%](#item-finance-news-2) ⭐️ 8.0/10
3. [世界模型 AI 融资快速降温，10 月一级市场融资事件仅 5 起](#item-finance-news-3) ⭐️ 7.0/10
4. [苹果借新加坡转移利润 今年节税 27 亿美元](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [本周任意地点的卫星过境与照片](https://www.watched.earth/) ⭐️ 8.0/10

开发者发布了浏览器工具 watched.earth，用于查找任意地点在过去 7 天内所有卫星过境。它使用 SGP4 模型与 CelesTrak 星表，在浏览器内约半秒完成搜索，并拉取对应过境的真实 Sentinel-2/Landsat/NASA 影像。只有存在真实影像时才显示“watched”，且不存储用户位置；过境搜索在极点、反经线和极窄刈幅上对照暴力搜索实现了 0 漏报。约 1.7 万个在轨物体在 GPU 上每帧求解开普勒方程进行绘制，开发者也发现 Sentinel-2 时间戳常与实际穿越相差 5-10 分钟。代码发布在 GitHub：https://github.com/dev-Armaan/satellites。

hackernews · a585gupt · 11月9日 17:51 · [社区讨论](https://news.ycombinator.com/item?id=50428907)

**「背景」** SGP4 是一种广泛使用的简化轨道预报模型，CelesTrak 提供公开的卫星轨道根数目录。Sentinel-2、Landsat 和 NASA 影像是常用的公开对地观测数据来源；“过境”指卫星经过某地上空并可能拍摄该区域。

**「影响」** 对于地理空间爱好者和背包徒步路线规划者，该工具无需服务器即可在浏览器中快速查看任意地点近 7 天的真实卫星影像，并比 Copernicus 等现有途径更易访问。

**「社区讨论」** HN 评论几乎一致称赞该工具的设计与执行质量，认为这是风格与实质结合最好的网站之一。地理空间从业者称可查看卫星精确影像“做得很好”，有用户表示比 Copernicus 更易访问。

**标签**: `#satellite-imagery`, `#SGP4`, `#geospatial`, `#webgl`, `#earth-observation`

---

<a id="item-tech-news-2"></a>
### [消费者版 Gemini 被曝将个人 Drive 文件与邮件交给人工标注](https://github.com/thisisme6598/gemini_files/) ⭐️ 8.0/10

Hacker News 上的一则讨论指出，连接了应用的消费者版 Google Gemini 可能将个人 Drive 文件和 Gmail 邮件发送给人工标注员；而 Workspace 版 Gemini 和 Workspace Intelligence 仍声称不受人工审查。用户授权 Gmail 等应用后，Gemini 会通过工具加载邮件，这些数据与所有进入对话的数据一样，可能进入人工标注流程。评论还提到，任何带人工审查的 Gemini 与 NotebookLM 都可能让随机人员读到用户数据，或被标记后用于训练和改进模型。

hackernews · gf74918 · 11月9日 18:24 · [社区讨论](https://news.ycombinator.com/item?id=50429426)

**「背景」** 谷歌 Gemini 是谷歌推出的多模态 AI 助手，用户可授权其通过“已连接应用”读取 Gmail、Google Drive 等个人数据。人工标注是 AI 行业常见的质量改进手段，服务商可能安排人工审核用户查询或模型输出；企业版（Workspace）与消费版在数据处理条款上可能存在差异。本次讨论聚焦于消费版 Gemini 在连接个人应用后，是否会将邮件和云盘文件内容发送给人工标注员，而 Workspace 版本则声称不受人工审核约束。

**「用户影响」** 消费者版 Gemini 用户若连接并授权 Gmail 或 Drive，其个人邮件和文件内容可能被第三方人工标注员读取，并可能被用于模型训练或改进。该风险不适用于声称免于人工审查的 Workspace 版本。

**「社区讨论」** 社区讨论普遍对隐私侵蚀表示担忧；一名用户称向 Gemini 询问公园咨询流程时，回答与触发问题的邮件高度吻合，暗示邮件内容被读取。另有评论指出，任何带人工审核的 Gemini 与 NotebookLM 都可能让随机人员读取用户数据或将其用于训练改进。

**标签**: `#privacy`, `#google`, `#gemini`, `#ai`, `#data-annotation`

---

<a id="item-tech-news-3"></a>
### [潜在预测优于重建：LingBot-Touch 触觉预训练](https://www.reddit.com/r/MachineLearning/comments/1xs05uo/latent_prediction_beats_reconstruction_for/) ⭐️ 8.0/10

新论文 LingBot-Touch 提出一种 JEPA 风格的自监督触觉编码器，通过预测被掩码接触区域的潜在表示而非重建原始传感器信号进行预训练，推理代码与检查点已公开。在相同数据上，与同规模 MAE 和 VAE 重建模型对比：1K 小时时触觉到视频 top-5 召回率为 32.1%（JEPA）对 5.6%（MAE）和 4.4%（VAE）；4K 小时时 JEPA 达 49.3%，MAE 仍低于 9%，VAE 降至 3.1%。作者解释触觉片段大部分是接近零的背景，重建损失可在未学到接触信息时下降；实现上掩码率从 40%在 300 步内升至 80%，三种传感器类型经规范指尖坐标和 5D RoPE 输入一个共享 Transformer。在 26 个真实机器人任务与 4 种策略的 104 个组合中，冻结编码器特征在 89 个组合得分最高；在预训练未见过的磁学手上，LingBot-VLA 从 57.21 提升至 75.04，Tiny 模型约 4K 小时后趋于平缓而 Small 模型持续提升。

reddit · r/MachineLearning · /u/Zealousideal-War7154 · 11月9日 18:52

**「背景」** JEPA（联合嵌入预测架构）风格的自监督学习通过预测潜在空间中的表示学习特征，而不是重建像素或原始信号；MAE 和 VAE 则属于重建式预训练。触觉传感器信号通常稀疏且大部分区域接近零，因此重建损失可能主要反映背景而非接触信息。

**「影响」** 这为触觉编码器预训练提供了一种更有效的替代方案，尤其是在数据有限但接触稀疏的真实机器人场景中，机器人团队可直接使用公开的 LingBot-Touch 检查点获得优于同规模重建预训练的冻结特征。

**标签**: `#robotics`, `#self-supervised learning`, `#tactile sensing`, `#representation learning`, `#JEPA`

---

<a id="item-tech-news-4"></a>
### [SwarmEvolve：潜空间 KV 缓存混合加速进化式数学发现](https://www.reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and/) ⭐️ 8.0/10

研究人员提出 SwarmEvolve，一个可扩展的数学发现与优化框架，灵感来自 AlphaEvolve 和 LatentMAS。该框架由数百个具备潜空间推理能力的智能体组成，运行在 Qwen3 8B、14B 和 32B 模型上；智能体不写出思维过程，而是在潜空间中交换并混合 KV 缓存，使不同智能体的想法在模型内部直接融合。作者称，SwarmEvolve 在约 5 分钟内达到 OpenEvolve、ShinkaEvolve 和 CodeEvolve 等开放框架需要超过 1 小时才能达到的分数；仅用 8B 模型就追平了已知最佳的圆填充结果。该框架已扩展到 Qwen3.5 和 Muse 模型并表现更好，代码即将在 GitHub 公开（论文见 alphaxiv）。

reddit · r/MachineLearning · /u/QileHQ · 11月9日 15:30

**「背景」** LLM 引导的进化搜索已用于数学发现：模型生成候选程序，按评分迭代改进；AlphaEvolve 曾用 Gemini 找到更快的 4×4 复数矩阵乘法算法。OpenEvolve、ShinkaEvolve、CodeEvolve 等开源实现通常较慢且昂贵，而 SwarmEvolve 借鉴 LatentMAS，让数百个小规模 Qwen 智能体在隐空间推理，不将中间思路解码成文本。智能体之间通过传递 KV 缓存混合想法，每个子群从不同角度研究问题，从而降低令牌生成开销并提高吞吐量。

**「影响」** 如果作者自述的性能得到复现，使用小型 Qwen3 模型的研究人员可以用约 5 分钟完成此前开源进化式数学发现框架需超过 1 小时的任务，但该结果目前仅来自作者报告，尚未经独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.08483">[2611.08483] SwarmEvolve: Latent Agent Swarms for ...</a></li>
<li><a href="https://arxiv.org/html/2611.08483v1">SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery ...</a></li>

</ul>
</details>

**标签**: `#latent reasoning`, `#agent swarms`, `#evolutionary optimization`, `#math discovery`, `#efficient inference`

---

<a id="item-tech-news-5"></a>
### [谷歌推出 TPU 8tx 和 8i Max 加速挑战英伟达](https://www.bloomberg.com/news/articles/2026-11-09/google-escalates-nvidia-rivalry-with-new-versions-of-its-tpu-systems) ⭐️ 8.0/10

谷歌宣布推出两款新的张量处理单元：TPU 8tx 面向政府机构及受严格监管行业，用于处理安全机密数据，并将与 AMD 芯片协同工作；TPU 8i Max 则针对超长上下文窗口 AI 应用场景，将两颗 TPU 芯片集成在同一封装内，以提供更强算力和更大内存容量。谷歌今年打破过去每两年推出一款新处理器的节奏，连续扩充 TPU 产品线，针对不同应用场景提供专用芯片。随着苹果、Meta、甲骨文和 Anthropic 等企业成为客户，谷歌正试图将 TPU 打造为英伟达 GPU 之外的重要选择。该消息由 Bloomberg 报道，但未披露具体性能、功耗或价格数据。

telegram · zaihuapd · 11月9日 13:36

**「背景」** TPU（张量处理单元）是谷歌自研的 AI 加速芯片，主要用于云端训练和推理，其第八代产品已区分为面向训练的 TPU 8t 和面向推理的 TPU 8i。此次发布的 TPU 8tx 与 TPU 8i Max 是在该代产品基础上进一步细分的型号：前者将 TPU 8t 与第五代 AMD EPYC 处理器结合，并增加硬件层数据与模型权重保护，面向政府及严格监管场景；后者则通过在同一封装内集成两颗 TPU 芯片扩大内存和算力，针对超长上下文 AI 应用。谷歌通过快速扩充 TPU 产品线，试图在 AI 加速器市场提供英伟达 GPU 之外的选择，并已吸引苹果、Meta、甲骨文和 Anthropic 等客户。

**「影响」** 对需要处理安全机密数据或超长上下文 AI 负载的政府机构、受监管行业和云用户，谷歌新增的 TPU 8tx 与 8i Max 提供了英伟达 GPU 之外的专用加速选项，可能降低对单一芯片供应商的依赖。

**「社区讨论」** Hacker News 用户关注谷歌是否直接销售这些 TPU，并指出 Colab 上最强仍为 v6e-1、新模型未提供，难以用于严肃工作。也有人询问每 token 功耗/价格及与英伟达同价位对比，并推荐 Google 的 TPUSync 文章，称 Strata for Qwen 等开源仓库采用类似机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/">Introducing TPU 8 tx and TPU 8 i Max</a></li>
<li><a href="https://dzen.ru/a/avHlCl56vGiwEiaH">Google расширила линейку тензорных процессоров ( TPU )... | Дзен</a></li>
<li><a href="https://www.linkedin.com/posts/john-flabetich_google-tpu-8i-for-inference-and-tpu-8t-for-activity-7454730299583922177-SItp">Google TPU 8 i for Inference and TPU 8 t for Training | LinkedIn</a></li>

</ul>
</details>

**标签**: `#Google`, `#TPU`, `#AI hardware`, `#Nvidia`, `#Cloud computing`

---

<a id="item-tech-news-6"></a>
### [Anthropic 发布 Claude Fable 5.2 与 Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2) ⭐️ 7.0/10

Anthropic 宣布推出 Claude Fable 5.2 和 Mythos 5.2，此次发布在 Hacker News 上引发关注，主要围绕编码能力和模型系列调整。官方未提供详细的基准数据或范式级声明。社区反馈中，有用户报告 Fable 5.2 在编码任务上表现突出，例如在两天内将 600k 行 Fortran 代码库提速 36 倍，并提到 1,000 个 Fable 5.2 智能体用 30 小时完成费马大定理形式化。同时，有评论认为 Anthropic 在 Opus 5.5、Sonnet 5.5 与 Fable 5.2 之间实现了更均衡的定位。

hackernews · lairv · 11月9日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50429068)

**「背景」** Anthropic 是一家专注于人工智能安全的公司，其 Claude 系列大语言模型通过不同版本迭代提升能力，此前已有 Opus、Sonnet 等型号。此次发布的 Fable 5.2 和 Mythos 5.2 是该公司针对高难度技术任务的最新版本，与 OpenAI 的 GPT-6 Astra、Google 的 Gemini 4 Carbon 等竞品形成直接对比。

**「对开发者和研究人员的具体影响」** 对开发者和研究人员而言，Claude Fable 5.2 在编码、金融和科学任务上宣称达到新基准，同时 API 价格降至每百万 tokens 8 美元和 40 美元，比 Fable 5.1 低约 20% 且速度提升最高 30%。不过，社区对部分基准对比方式仍有质疑，独立验证尚未充分。

**「社区讨论」** 社区讨论中，部分用户对 Fable 5.2 的编码能力表示肯定，并认为 Anthropic 的模型定位更均衡；但也有评论质疑官方比较中的基准选择和方法，例如未对 Carbon 进行网络基准测试、切换对比对象等问题。还有人猜测 Fable 5.2 可能是战略保留，真正的 5.5 版本可能留待应对竞争对手新模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=kwRxc8QPhrk">Fable 5 . 2 &amp; Mythos 5 . 2 Are OUT (Not 5.5... Here&#x27;s Why) - YouTube</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5.2">Claude Fable 5 . 2 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-2">Introducing Claude Fable 5.2 and Claude Mythos 5.2</a></li>
<li><a href="https://madrobot.blog/2026/11/09/claude-fable-5-2-released-price-benchmarks/">Claude Fable 5.2 released: price, benchmarks and free resets</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#model release`, `#Anthropic`, `#large language models`, `#software engineering`

---

<a id="item-tech-news-7"></a>
### [E-means：以十分之一轮数超越 k-means](https://e-means.github.io/) ⭐️ 7.0/10

E-means 是一种新的聚类算法，其宣传称仅需 k-means 十分之一的训练轮数即可超越后者，但该链接未提供论文或源码等原始细节。Hacker News 社区交流显示结果因任务而异：一位用户将其用于 IVF 索引的 GPU 实现，报告 146 倍加速；另一位在 Antfly 的批量重建中替换层次平衡增量聚类，得到 2.5 倍构建加速。同时，有用户尝试用其替代 Lloyd 算法来松弛球面等面积网格，发现并不更好。社区还提到其更新规则可能类似于带摩擦项的期望最大化，并具有保持质心在凸包内的性质，但这些技术描述尚未得到官方材料证实。

hackernews · porridgeraisin · 11月9日 18:45 · [社区讨论](https://news.ycombinator.com/item?id=50429734)

**「背景」** E-means 是一种新的聚类算法，它在经典 k-means（Lloyd 算法）的基础上引入指数移动平均优化过程，配合小批量更新并利用现代深度学习工具加速收敛。论文显示，e-means 在多个嵌入数据集上仅用 1.4 到 2.6 个 epoch 就达到 Lloyd k-means 25 个 epoch 的损失，对应 GPU 墙钟时间 10-45 倍加速；在社区实践中，有人报告 GPU 上的 IVF 索引获得 146 倍加速、批量重建索引快 2.5 倍，但也有球面网格松弛等用例未见改善。

**「影响」** 对于 IVF 索引和批量重建等特定聚类任务，E-means 可能带来显著加速（社区报告 GPU 上 146 倍、批量构建 2.5 倍），但球形网格松弛等场景并未受益，实际效果需按任务验证。

**「社区讨论」** 社区讨论呈现分化：有人报告 IVF 索引 GPU 加速 146 倍和批量重建 2.5 倍，但另一用户发现其不适于球面网格松弛；另有评论认为该算法可解释为带摩擦项的期望最大化，并希望纳入 SciPy。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.09501">e-means: outperforming k-means (in one-tenth the epochs)</a></li>
<li><a href="https://arxiv.org/html/2611.09501v1">e-means: outperforming k-means (in one-tenth the epochs)</a></li>
<li><a href="https://openreview.net/pdf?id=pt14gnV3dl">E-MEANS OUTPERFORMING K MEANS IN ONE TENTH THE EPOCHS</a></li>

</ul>
</details>

**标签**: `#clustering`, `#k-means`, `#machine-learning`, `#algorithms`, `#performance`

---

<a id="item-tech-news-8"></a>
### [2026 论文主题页更新基准](https://www.reddit.com/r/MachineLearning/comments/1xs6494/followup_2026_papers_are_finally_in_the_topic/) ⭐️ 7.0/10

Reddit 用户 latenticlabs 更新了其基于十年 ICML/NeurIPS/ICLR/CVPR/AAAI 论文的主题页工具，补上了此前止于 2025 年的基准记录和消融数据。此次从约 10.1 万篇全文（此前为 7.9 万篇）中提取出约 100 万条“尝试 X 得到 Y”发现，2026 年已覆盖几乎所有 ICML、CVPR、AAAI 论文、4.1k/5.4k 篇 ICLR 论文，NeurIPS 2026 只完成过半，主要因大量 PDF 尚未公开。以紧凑/高效高斯泼溅主题为例，Mip-NeRF 360 PSNR 从 2025 年的 29.5 升至 2026 年 30.1（此前 28.01），Deep Blending 仍约 30.4，Tanks&amp;Temples 无变化；基线表中论文对 plain 3DGS 在 Mip-NeRF 360 的报告 PSNR 从 16 到 27.7 不等。同时发布的 ICML/CVPR/ICLR 2026“报纸”显示：ICML 中 LLM 智能体论文占比从 1.2% 升至 4.4%，CVPR 多模态 LLM 论文占比从 5.4% 翻倍至 10.8%，ICLR 中带可验证奖励的 RL 论文从几乎为零增至 110 篇，Qwen 是三个会议结果表中最常用的基础模型，约四分之一被测试的改动按论文自身数据无效或更差。作者提示这些数字由 AI 提取、未经人工核对，且论文倾向报告有效结果，应作为起点而非排行榜。

reddit · r/MachineLearning · /u/latenticlabs · 11月9日 22:39

**「背景」** 该工具最早由该用户数周前发布，聚合十年机器学习顶会论文的基准结果与消融实验，但当时数据停留在 2025 年。此次更新补齐 2026 年数据，并新增各会议年度对比“报纸”。

**「影响」** 研究人员可免费使用该主题页（无需注册）查看 2026 年各会议论文的基准与消融数据，但由于数值由 AI 提取且未经人工核验，应仅作为研究起点，不能当作正式排行榜。

**标签**: `#machine learning`, `#benchmarking`, `#research tools`, `#computer vision`, `#academic papers`

---

<a id="item-tech-news-9"></a>
### [字节跳动发布 Seedream 5.5，支持百轮编辑与原生透明素材](https://seed.bytedance.com/zh/blog/%E7%94%9F%E6%88%90%E6%9B%B4%E7%9C%9F%E5%AE%9E-%E7%99%BE%E8%BD%AE%E7%BC%96%E8%BE%91%E6%9B%B4%E7%A8%B3%E5%AE%9A-seedream-5-5-%E5%8F%91%E5%B8%83) ⭐️ 7.0/10

字节跳动发布了图像创作模型 Seedream 5.5。该模型支持对同一作品进行最多 100 轮连续编辑，并可原生生成带透明通道的素材。新版本还提升了图像真实感和文字渲染能力。字节跳动称，在评测中该模型在影视、办公场景的可用率达到上一版本的两倍以上。目前该模型正陆续上线即梦、豆包、豆包工作和火山方舟。

telegram · zaihuapd · 11月9日 08:34

**「背景」** Seedream 是字节跳动 Seed 团队推出的图像生成与编辑模型系列，此前版本包括 2026 年 7 月发布的 Seedream 5.0 Pro 和 2026 年 10 月展示的 Seedream 5.5 预览版。该系列专注于提升生成图像的真实感、文本渲染和布局控制能力。第三方资料还提到 Seedream 5.5 具备原生 RGBA 透明通道、100 图层拆分和 4K 输出等特点。

**「影响」** 即梦、豆包、豆包工作和火山方舟的用户与开发者可获得最长 100 轮的连续编辑和原生透明通道输出，但字节宣称的影视、办公可用率翻倍尚未经独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5">Seed News - ByteDance Seed Team</a></li>
<li><a href="https://seedream55.org/">Seedream 5 . 5 : Cheaper But Better</a></li>
<li><a href="https://seedream6.dev/">Seedream 6: The Next ByteDance Image Model</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#image generation`, `#ByteDance`, `#Seedream`, `#AI models`

---

<a id="item-tech-news-10"></a>
### [欧盟数字公平法案拟限成瘾设计](https://www.mlex.com/mlex/articles/2546584/digital-businesses-face-addictive-design-controls-under-draft-eu-consumer-law) ⭐️ 7.0/10

一份泄露的欧盟《数字公平法案》草案显示，欧盟拟限制数字企业的成瘾性设计和订阅陷阱：要求允许用户关闭自动播放、连续使用奖励等诱导强迫或过度使用功能；在线订阅须提供取消按钮、续费提醒和人工客服，免费试用转为付费订阅前须取得明确同意。草案还禁止面向未成年人的游戏付费抽奖、“付费获胜”和画像广告，并要求游戏虚拟货币标明真实币值。欧盟委员会定于 11 月 11 日提交该法案，并同步改革消费者保护合作框架。违规企业最高可被处全球营业额 6%的罚款；该法案及合作框架改革均需欧洲议会与欧盟各国政府同意才能生效。

telegram · zaihuapd · 11月9日 16:42

**「背景」** 欧盟《数字服务法》（DSA）已于 2024 年全面生效，其第 25 条首次在法律中明确禁止欺骗或操纵用户的“暗黑模式”，但该法主要针对平台责任。即将推出的《数字公平法案》预计将在 2026 年底前出台，超越 DSA，直接禁止被认为具有成瘾性且对儿童有害的设计特征；据泄露草案，该法案将列出十种操纵性在线设计“陷阱”，并要求游戏内货币显示真实货币价值、默认对儿童关闭除非家长批准。

**「影响」** 若该草案最终获批，面向欧盟用户的数字平台和游戏开发商将须调整自动播放、订阅取消和虚拟货币计价等设计，并可能因违规面临最高全球营业额 6%的罚款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.euronews.com/2026/11/09/eu-to-blacklist-ten-manipulative-online-design-traps-leaked-draft-shows">EU to blacklist ten manipulative online design &#x27;traps&#x27;, leaked draft s...</a></li>
<li><a href="https://cryptobriefing.com/eu-meta-investigation-addictive-design-children/">EU escalates investigation into Meta over addictive design targeting...</a></li>
<li><a href="https://medium.com/design-bootcamp/the-internet-is-lying-to-you-and-its-by-design-06296a598654">The internet is lying to you. And it’s by design | Medium</a></li>

</ul>
</details>

**标签**: `#EU regulation`, `#digital fairness`, `#consumer protection`, `#video games`, `#subscription services`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [英伟达董事会调查黄仁勋，预测市场认为其短期离职概率低](https://www.cnbc.com/2026/11/09/jensen-huang-nvidia-exit-prediction-markets.html) ⭐️ 8.0/10

英伟达董事会正在调查 CEO 黄仁勋，因他承认与一名被美国情报官员指控为中国间谍的女性有婚外情。预测市场显示他短期内被罢免的概率较低，Kalshi 押注其 2027 年前离职概率为 17%，消息公布后英伟达股价周一跌超 5%。

rss · CNBC Finance · 11月9日 18:46

**「背景」** 黄仁勋周日承认婚外情，《纽约时报》援引美国情报官员称该女性为中国国家安全部间谍；英伟达表示黄仁勋成为“外国情报活动”的目标，并据此展开调查。

**标签**: `#Nvidia`, `#Jensen Huang`, `#corporate governance`, `#prediction markets`, `#national security`

---

<a id="item-finance-news-2"></a>
### [前三季度新能源车出口增长 138.8%](https://finance.sina.com.cn/tech/roll/2026-10-26/doc-iniwpfnc2438186.shtml) ⭐️ 8.0/10

2026 年前三季度，中国新能源乘用车出口 388.7 万辆，同比增长 138.8%；同期国内零售量为 775.8 万辆，同比下降 12.8%。

telegram · zaihuapd · 11月10日 02:56

**「背景」** 出口增长成为车企销量增长的重要支撑；新浪财经报道称，国内需求走弱与购车补贴、购置税优惠调整及去年同期销量基数较高有关。

**标签**: `#new energy vehicles`, `#exports`, `#auto industry`, `#China economy`, `#economic data`

---

<a id="item-finance-news-3"></a>
### [世界模型 AI 融资快速降温，10 月一级市场融资事件仅 5 起](https://mp.weixin.qq.com/s/8U3Lwbq2q0klDUTIy7LWNQ) ⭐️ 7.0/10

世界模型 AI 领域一级市场融资正在快速降温，资金向少数顶尖团队集中。据财联社创投通不完全统计，10 月物理 AI 及世界模型相关融资事件仅 5 起。

telegram · zaihuapd · 11月9日 07:10

**「背景」** 此前世界模型赛道曾受资本追捧，但头部风投自 2026 年 5、6 月起放慢投资节奏，导致交割量连续下滑，财联社创投通统计 10 月相关融资仅 5 起。标志性交易包括：AMD 于 2026 年 9 月 28 日宣布以约 82 亿美元全股票收购李飞飞创办的 World Labs；而 Decart 此前被 Anthropic 洽谈以约 60 亿美元收购后放弃，市场又传出亚马逊洽谈约 70 亿美元收购的初步消息。

**「影响」** 该趋势下，缺乏顶尖高校研究背景或已发布模型成果的初创团队获得一级市场资金的机会减少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huxiu.com/article/4894452.html">AMD 官宣82亿美元收购World Labs：李飞飞加入，苏姿丰押注物理AI</a></li>
<li><a href="https://news.qq.com/rain/a/20260815A04VXN00">拟60 亿 美 元 收 购 Decart ，Anthropic在IPO...</a></li>
<li><a href="https://www.odaily.news/en/newsflash/516207">市场消息： Anthropic 据悉放弃 60 亿 美 元 收 购 Decart 的交易 - Odaily</a></li>
<li><a href="https://agihunt.info/p/1a1bfda7de0ce166ab267dfd4d3">世界模型融资骤冷：10 月仅 5 起，头部 VC 只剩四五… · AGI Hunt</a></li>

</ul>
</details>

**标签**: `#世界模型`, `#AI融资`, `#风险投资`, `#并购`, `#科技产业`

---

<a id="item-finance-news-4"></a>
### [苹果借新加坡转移利润 今年节税 27 亿美元](https://appleinsider.com/articles/26/11/08/apple-saves-27b-in-taxes-by-funnelling-finances-through-singapore) ⭐️ 7.0/10

据 AppleInsider 报道，苹果 2026 年经新加坡转移约 500 亿美元利润，由此节税 27 亿美元。

telegram · zaihuapd · 11月9日 09:19

**「背景」** 此前，苹果长期通过爱尔兰转移利润，2025 年因爱尔兰税务案补缴了 170 亿美元；英国《金融时报》报道称，苹果的税务重心已从爱尔兰转向新加坡，新加坡由此成为其最大的节税地。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rbc.ru/business/09/11/2026/6af140da3c02e1f36c5b688e">FT: Apple сэкономила 2,7 млрд долларов на налогах, направив...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#corporate tax`, `#profit shifting`, `#Singapore`, `#tax avoidance`

---