---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 43 条内容中筛选出 15 条重要资讯。

---

**科技新闻**
1. [OpenAI 声称解决纳维-斯托克斯千年难题](#item-tech-news-1) ⭐️ 9.0/10
2. [AlphaGenome Atlas：人类 DNA 单字母变化高分辨率图谱](#item-tech-news-2) ⭐️ 8.0/10
3. [NeurIPS 用 AI 检测器拒稿 178 篇，检测器误标主席论文 24-69%](#item-tech-news-3) ⭐️ 8.0/10
4. [张一鸣被曝亲自督导字节跳动空间视频模型](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI 发布 ChatGPT Images 2.5 图像模型](#item-tech-news-5) ⭐️ 8.0/10
6. [Meta 推出个人 AI 代理 Muse](#item-tech-news-6) ⭐️ 7.0/10
7. [Buckmaster 指控 OpenAI 窃取 Navier-Stokes 研究](#item-tech-news-7) ⭐️ 7.0/10
8. [基准测试：Qwen3.8 27B 量化 4-bit 保持质量，1-bit 崩溃](#item-tech-news-8) ⭐️ 7.0/10
9. [陶哲轩警告 AI 或致开放问题枯竭](#item-tech-news-9) ⭐️ 7.0/10
10. [马来西亚拟用华为 AI 芯片建主权项目](#item-tech-news-10) ⭐️ 7.0/10
11. [库克缺席苹果 9 月 9 日发布会视频，新 CEO 主推折叠 iPhone](#item-tech-news-11) ⭐️ 7.0/10
12. [ASML 与台积电推进 High NA EUV 升级，12 英寸光掩模计划落地](#item-tech-news-12) ⭐️ 7.0/10
13. [中国计划到 2030 年智能算力提升至 9800 EFLOPS](#item-tech-news-13) ⭐️ 7.0/10

**财经新闻**
1. [CoinGecko 报告：加密货币平台因网络攻击和密钥被盗损失超 36 亿美元，多数已做审计](#item-finance-news-1) ⭐️ 7.0/10
2. [上海 10 月起生育医疗费用个人“无自付”](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 声称解决纳维-斯托克斯千年难题](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

OpenAI 声称使用一款未发布的内部模型解决了纳维-斯托克斯存在性与光滑性问题，这是七大千年大奖难题之一，自 2000 年 5 月 24 日起悬赏 100 万美元。该声明被纽约大学数学家 Tristan Buckmaster 的指控所笼罩，他与现任职于 Anthropic 的 Levent Alpöge 合作近一年，并于 8 月 15 日取得突破，而 OpenAI 在 9 月 1 日听到传闻后启动项目，9 月 5 日得出解，Lean 形式化验证又耗时 17 小时。Buckmaster 质疑 OpenAI 是否在得知其工作后才发起研究、以及模型是否接触过他们存放在 Codex 中的草稿；OpenAI 否认访问特定用户数据，但无法排除去标识化数据可能改进了模型，并称双方证明差异显著。整个过程中智能体发送了 270 万条消息、消耗约 1300 亿输出 token，OpenAI 所有尝试共发送 490 万条消息、消耗约 3000 亿 token。

rss · Simon Willison · 9月8日 23:55

**「背景」** 千年大奖难题由克雷数学研究所于 2000 年设立，共有七个未解决数学问题，每个悬赏 100 万美元。纳维-斯托克斯存在性与光滑性问题询问三维不可压缩流体方程的解是否始终存在且光滑，还是会形成奇点。OpenAI 此次宣称其内部系统证明了解可以在有限时间内产生奇点。

**「影响」** 关于未发表解的传闻已能触发数百万美元的 LLM 支出去抢先解决，这可能促使数学家不再分享进行中的研究方向。

**「社区讨论」** Hacker News 评论中，Terence Tao 警告传闻可引发 AI 驱动的“碾压”并抑制研究分享；也有用户质疑 OpenAI 的成果是否基于他人提示。另有评论指出其内部模型在不到两周内数学能力号称是 Astra 的两倍以上，并希望此类研究由公共机构主导。

**标签**: `#artificial intelligence`, `#mathematics`, `#Navier-Stokes`, `#OpenAI`, `#scientific discovery`

---

<a id="item-tech-news-2"></a>
### [AlphaGenome Atlas：人类 DNA 单字母变化高分辨率图谱](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10

Google DeepMind 发布了 AlphaGenome Atlas，这是一个预测人类基因组中所有可能单字母 DNA 变化的高分辨率图谱。该图谱利用深度学习为每个单核苷酸变异提供效应预测，是基因组学和生物信息学领域的重要数据资源。其目标是帮助研究人员快速评估 DNA 变异的功能后果，可能加速遗传病研究和精准医疗应用。由于发布详情有限，目前尚不清楚该图谱在独立数据集上的性能表现和实际临床效用。

hackernews · utiiiD · 9月8日 14:55 · [社区讨论](https://news.ycombinator.com/item?id=49611251)

**「背景」** AlphaGenome 是 Google DeepMind 开发的统一基因组学模型，输入长达 1Mb 的 DNA 序列，能够以单碱基分辨率预测多种功能基因组轨迹。与此前主要关注蛋白质结构的 AlphaFold 不同，该模型用于破解 DNA 功能并预测变异效应，包括非编码区调控变异。AlphaGenome Atlas 正是基于该模型对人类基因组中所有可能的单字母 DNA 改变进行预测而得到的高分辨率图谱。

**「影响」** 对于从事基因组变异解读与遗传学研究的人员，AlphaGenome Atlas 可能提供一个覆盖全基因组单核苷酸变异的统一查询入口，但当前缺乏详细的基准测试信息，其预测可靠性仍需独立验证。

**「社区讨论」** 社区讨论中，有用户询问该图谱是否覆盖启动子等非编码调控序列，以及能否直接用于 23andMe 等消费级基因组数据来寻找致病突变；同时有人提醒并非所有 DeepMind 生物学模型都产生了同等影响，实际效用需要观察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-10014-0">Advancing regulatory variant effect prediction with AlphaGenome</a></li>
<li><a href="https://deepmind.google.com/science/alphagenome/">AlphaGenome - deepmind.google.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#genomics`, `#DeepMind`, `#bioinformatics`, `#DNA`

---

<a id="item-tech-news-3"></a>
### [NeurIPS 用 AI 检测器拒稿 178 篇，检测器误标主席论文 24-69%](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 8.0/10

NeurIPS 立场论文赛道使用专有 AI 检测器 Pangram 对 18.4%的投稿进行了直接拒稿，共拒稿 178 篇，且没有人工复核或申诉程序。该检测器最初将整个赛道 42.7%的投稿标记为 AI 生成，在缩小文本窗口后才把标记率降至更“可信”的 12.7%。三名赛道主席自己的近期论文经同一检测器测试，被标记概率为 24%至 69%，按照他们自己的执行规则也可能面临拒稿风险。另有 22 篇论文仅因检测器得分大于 0.5 且作者勾选了否认使用 AI 的选项而被认定说谎并拒稿；斯坦福大学研究显示，61.22%的人类撰写的 TOEFL 作文会被误判为 AI 生成，而 NeurIPS 未公布任何人口统计校准数据。

reddit · r/MachineLearning · /u/tughanbulut · 9月8日 10:19

**「背景」** NeurIPS（神经信息处理系统大会）是机器学习领域顶级学术会议之一，其“立场论文”赛道通常较短，用于提出新兴观点或立场。学术会议在同行评审前常进行“desk rejection”（直接拒稿），例如格式不符或明显违规；近年来，由于生成式 AI（如 ChatGPT）的普及，一些会议开始使用 AI 检测工具来筛查可能由 AI 生成的稿件。这类工具通常基于文本特征给出 AI 生成概率，但其准确性和公平性（尤其对非英语母语作者）存在争议。

**「影响」** 对于被 NeurIPS 2026 立场论文赛道以 Pangram 检测器直接退稿的 178 篇论文作者，由于官方不允许申诉且不留下学术不端记录，实际后果是需要将论文改投 ICLR（截止 9 月 25 日）或 ICML；CASRAI 的报道确认了这一无申诉机制的执行过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://casrai.org/news/neurips-2026-pangram-ai-detector-desk-rejection-controversy">NeurIPS 2026: Pangram AI - Detector Desk Rejections — CASRAI</a></li>
<li><a href="https://startupfortune.com/neurips-is-facing-backlash-over-ai-detector-desk-rejections/">NeurIPS is facing backlash over AI detector desk rejections</a></li>

</ul>
</details>

**标签**: `#NeurIPS`, `#AI detection`, `#academic publishing`, `#machine learning`, `#ethics`

---

<a id="item-tech-news-4"></a>
### [张一鸣被曝亲自督导字节跳动空间视频模型](https://www.bloomberg.com/news/articles/2026-09-07/bytedance-founder-joins-ai-elite-in-race-to-perfect-world-models) ⭐️ 8.0/10

据彭博社援引知情人士消息，字节跳动创始人张一鸣正亲自督导一款实时空间视频生成模型，最快或于 2026 年 10 月发布，但时间仍可能调整。该模型基于 Seedance，可生成响应 Pico 头显用户语音或动作的互动虚拟世界。技术上，该模型据称能以约 0.05 秒延迟、每秒 20 帧生成视频，并将高强度计算转移至云端，以降低虚拟现实设备的硬件门槛。这一项目意味着字节跳动加入由张一鸣直接推动的 AI 世界模型竞争，可能影响 VR 内容生成和终端硬件需求。

telegram · zaihuapd · 9月8日 04:05

**「背景」** 字节跳动由张一鸣等人于 2012 年创立，旗下拥有 TikTok/抖音、今日头条等内容平台。张一鸣作为公司联合创始人，在字节跳动的发展中曾扮演重要角色，而字节跳动也通过 Pico 品牌进入虚拟现实头显领域。

**「影响」** 若该模型按传闻发布，Pico 头显用户可能获得低延迟云端生成的互动虚拟世界体验，从而降低本地硬件性能要求。不过发布日期和性能参数尚未经官方确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ByteDance">ByteDance - Wikipedia</a></li>
<li><a href="https://www.bytedance.com/en/">ByteDance - Inspire Creativity, Enrich Life</a></li>

</ul>
</details>

**标签**: `#ByteDance`, `#world models`, `#spatial video generation`, `#virtual reality`, `#generative AI`

---

<a id="item-tech-news-5"></a>
### [OpenAI 发布 ChatGPT Images 2.5 图像模型](https://openai.com/index/introducing-chatgpt-images-2-5/) ⭐️ 8.0/10

OpenAI 于 9 月 8 日发布 ChatGPT Images 2.5 图像模型，细节更清晰、编辑更精准、生成更快，图像生成延迟较 2.0 最高降低 50%。新模型已向 ChatGPT、ChatGPT Work 和 Codex 全平台用户推出，并在 ChatGPT 中新增 Sketch 手绘引导、模板、图片评论与提示词分享功能。API 同步上线 gpt-image-2.5-sunburst 和 gpt-image-2.5-flare 两款模型，其中 Sunburst 适用于编辑精度优先的工作流，Flare 适用于快速、高质量的日常图像生成。OpenAI 表示整体图像生成模型已在 ChatGPT Images 和 API 的 GPT-Image 模型中被用于生成超过 30 亿张图像。新版还提升了多轮指令遵循能力、响应速度，以及参考照片中主体的保持效果。

telegram · zaihuapd · 9月8日 18:45

**「背景」** ChatGPT Images 是 OpenAI 的文本生成与编辑图像模型，此前版本为 2.0；API 中的 GPT-Image 系列则为开发者提供编程调用能力。本次更新通过新的 2.5 版本改进生成质量、编辑一致性并降低延迟。

**「影响」** 对于需要频繁生成或精确编辑图像的用户与开发者，2.5 版本将生成延迟最高降低 50%，并通过 Sunburst（编辑精度优先）与 Flare（日常快速生成）两个 API 模型提供更明确的选择。

**标签**: `#OpenAI`, `#image generation`, `#ChatGPT`, `#API`, `#AI model release`

---

<a id="item-tech-news-6"></a>
### [Meta 推出个人 AI 代理 Muse](https://ai.meta.com/muse/) ⭐️ 7.0/10

Meta 发布了个人 AI 代理 Muse，目标用户为普通大众。该产品在安全上重点防范提示注入，采用分层防御：模型经训练识别并抵抗提示注入，执行框架标记不可信来源内容，确定性代码校验结果，并在代理无法触及的位置运行分类器集合。此设计由 Meta AI 的 David Singleton 在社区讨论中公开。尽管 Muse 可借助 Meta 庞大用户群快速普及，但隐私担忧仍然突出。

hackernews · yks · 9月8日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49615537)

**「背景」** Meta 推出了 Muse，这是一款面向日常任务的个人 AI 代理，用户可以通过 WhatsApp 直接与它对话，未来也会在 Meta 的 AI 眼镜上可用。该代理在设计上采用分层架构，防止直接读取存储的密码或支付凭证，并允许用户设置细粒度的读写权限、选择不将互动用于模型训练。这些功能和隐私控制是理解后续关于提示注入防护和用户接受度讨论的基础。

**「影响」** 对普通 Meta 用户，Muse 可能提升便利性，但其深度访问个人数据使隐私风险更突出；对 AI 安全从业者，其公开的分层提示注入防御提供了可参考的具体实现。

**「社区讨论」** 社区观点分歧：有人认为 Meta 可凭借庞大用户基础吸引不关注模型细节的普通用户，也有人因数据收集历史拒绝使用；还有用户希望用 Muse 抓取自己 Facebook 群组数据以替代已关闭的 API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/">Muse, Meta’s New Personal AI Agent, Needs You to Trust It | WIRED</a></li>
<li><a href="https://www.androidheadlines.com/2026/09/meta-launches-muse-ai-agent-everyday-tasks.html">Meet Muse: Meta&#x27;s New Personal AI Agent Built for Daily Errands</a></li>
<li><a href="https://ai.meta.com/muse/">Muse: Meta&#x27;s personal AI agent, features &amp; capabilities</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Meta`, `#personal assistant`, `#prompt injection`, `#product launch`

---

<a id="item-tech-news-7"></a>
### [Buckmaster 指控 OpenAI 窃取 Navier-Stokes 研究](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 7.0/10

数学家 Tristan Buckmaster 的 PDF 声明在 Hacker News 引发关注，其中提到他与 Levent Alpöge 在有限时间爆破问题上取得进展，涉及不可压缩多孔介质、Boussinesq 方程和三维不可压缩 Euler 方程，并声称证明了一个非千禧年大奖的 Navier-Stokes 相关问题。Buckmaster 指控 OpenAI 在其研究基础上开展工作，并试图与其协调发布；OpenAI 回应称“虽然可能性不大，但不能排除来自用户使用产品的去标识化数据帮助改进了模型”。这一争议引发了关于 AI 研究诚信、用户数据使用和学术优先权的广泛讨论，但相关指控尚未得到证实。

hackernews · procedurecall · 9月8日 05:42 · [社区讨论](https://news.ycombinator.com/item?id=49605915)

**「背景」** 三维纳维-斯托克斯方程解的存在性与光滑性是克雷数学研究所悬赏的千禧年难题之一；与之相关的三维不可压缩欧拉方程、Boussinesq 方程在有限时间内是否发生 blowup 也是重要问题。纽约大学数学家 Tristan Buckmaster 与 Anthropic 的 Levent Alpöge 近期公开了关于带光滑外力下有限时间 blowup 的结果，并称这些进展借助了 AI 模型，但并未证明纳维-斯托克斯千禧年问题。与此同时，OpenAI 声称其内部模型给出了纳维-斯托克斯千年奖问题的证明，Buckmaster 则指控 OpenAI 未经允许使用其研究，引发研究诚信争议。

**「影响」** 该事件已引发数学界对研究优先权和 AI 训练数据使用的广泛争议，可能损害学者与 AI 实验室之间的信任；不过 Buckmaster 的指控尚未得到独立证实。

**「社区讨论」** 评论区情绪强烈：多位评论者认为 OpenAI 窃取了世界级研究者的工作并威胁研究者，以维护企业利益；但也有评论指出 OpenAI 对训练数据来源存在不确定性，认为这可能只是长期存在的学术竞争。对于 Buckmaster 的工作是否实际影响 OpenAI 模型，尚无共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/09-08-2026-openai-says-ai-solved-navier-stokes-millennium-prize-problem-364521528752966">OpenAI Says AI Solved Navier – Stokes Millennium Prize Problem</a></li>
<li><a href="https://chang.aevumnews.com/en/openai-s-controversial-role-in-solving-navier-stokes-problem">OpenAI &#x27;s Controversial Role in Solving the Navier - Stokes Problem</a></li>
<li><a href="https://www.techmeme.com/260908/p26">Techmeme: Mathematician Tristan Buckmaster alleges OpenAI ...</a></li>
<li><a href="https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/">OpenAI fought dirty on career-making math problem, says NYU mathematician | TechCrunch</a></li>
<li><a href="https://www.wired.com/story/openai-navier-stokes-math-discovery-academics/">OpenAI Just Claimed a Huge Math Discovery. Some Academics Are Crying Foul | WIRED</a></li>
<li><a href="https://www.businessinsider.com/openai-navier-stokes-math-breakthrough-drama-2026-9">OpenAI&#x27;s Big Math Breakthrough Claim Sparks Drama - Business Insider</a></li>

</ul>
</details>

**标签**: `#mathematics`, `#artificial-intelligence`, `#research-integrity`, `#openai`, `#navier-stokes`

---

<a id="item-tech-news-8"></a>
### [基准测试：Qwen3.8 27B 量化 4-bit 保持质量，1-bit 崩溃](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 7.0/10

对 Qwen3.8 27B 的量化基准测试显示，4-bit 量化在多数指标上几乎不损失质量，而 1-bit 量化出现崩溃式下降。测试显示直到 4-bit 之前差异很小，2-bit 分数略低。评论区指出，Wilson 95% 置信区间与运行间噪声无关，且基准缺少 Q3 这一关键档位，尤其是面向 16GB 以下显存显卡的部署场景。该基准为需要在质量与资源占用之间做权衡的模型部署者提供了参考。

hackernews · stared · 9月8日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49611128)

**「背景」** 模型量化通过降低权重数值精度来减少内存占用和计算需求，常见 GGUF 格式提供 Q4\_K\_M、IQ2\_XXS 等不同位宽变体。Qwen3.8 27B 是 270 亿参数的大语言模型，其量化版本由 Unsloth 发布在 Hugging Face。此前对 Qwen3.6 27B 的测试显示，8 位量化需约 45GB 内存，Q4\_K\_M 约 30GB，2 位约 18GB，使本地部署成为可能。

**「影响」** 对于需要在有限显存中运行 Qwen3.8 27B 的部署者，4-bit 量化是质量损失较小的可行方案，而 1-bit 量化不可用。

**「社区讨论」** 评论区主要讨论 Wilson 置信区间的适用性、低量化模型可能通过更多思考补偿质量损失，以及基准缺失 Q3 和 KV 缓存量化数据；有用户特别关注 16GB 以下显卡的 Q3 档表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/">Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses - Quesma Blog</a></li>
<li><a href="https://quesma.com/blog/qwen-quantization-quality/">Do Qwen3.6 27B quantizations break the pelican? - Quesma Blog</a></li>

</ul>
</details>

**标签**: `#quantization`, `#large-language-models`, `#benchmarking`, `#Qwen`, `#model-compression`

---

<a id="item-tech-news-9"></a>
### [陶哲轩警告 AI 或致开放问题枯竭](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 7.0/10

陶哲轩在 Mathstodon 上指出，大量优质且富有成果的开放问题正以不可再生的方式被挖掘，可能导致这些问题变得稀缺。他警告，即使只是有人正在研究某个问题的传闻，也可能触发大规模 AI 驱动的工作，在原始研究项目充分发挥潜力之前将其“抹平”。这种情形可能使研究者不愿再与更广泛社区分享有前景的研究方向，从而逆转数百年的开放科学传统，并对该领域的未来造成严重长期损害。

rss · Simon Willison · 9月9日 00:20

**「背景」** 特伦斯·陶（Terence Tao）是菲尔兹奖和数学突破奖得主，在调和分析、偏微分方程、数论等领域有重要贡献。数学界历来有公开分享未解决问题和研究方向以促进合作的开放科学传统；近年来，大语言模型和 AI 证明工具可以在短时间内对公开问题发起大规模尝试，陶提出的“Big Mathematics”模式也设想人类、AI 与形式化证明系统协同解决复杂问题。因此，他担心公开讨论的线索会被 AI 快速“消耗”，导致研究者不愿再分享。

**「对数学开放科学的潜在冲击」** 若该预警成真，数学界可能因研究者不再分享有前景的方向而削弱开放科学传统，并长期损害领域创新。但这一影响目前仍是陶哲轩基于传闻观察的警示，尚未有定量证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=HUkBz-cdB-k">Terence Tao : Hardest Problems in Mathematics , Physics... - YouTube</a></li>
<li><a href="https://eu.36kr.com/en/p/3971371138855176">Did Claude Solve the Millennium Prize Problems ? Terence Tao ...</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#mathematics`, `#open-science`, `#research-ethics`, `#terence-tao`

---

<a id="item-tech-news-10"></a>
### [马来西亚拟用华为 AI 芯片建主权项目](https://www.businesstimes.com.sg/international/malaysia-eyes-huawei-chips-ai-project-despite-us-warning) ⭐️ 7.0/10

马来西亚正认真评估将华为 Ascend 910C 芯片用作其主权 AI 项目核心，项目规模约 20 亿令吉（约 4.94 亿美元）。若落地，将成为首个外国政府正式选择中国 AI 加速器而非美国产品的公开案例。消息人士称目前尚不清楚采购芯片数量。特朗普政府去年曾警告使用该华为 AI 加速器可能违反美国出口规定，但马来西亚政府认为相关决定纯属商业考量。

telegram · zaihuapd · 9月8日 03:35

**「背景」** 华为升腾（Ascend）系列是面向 AI 训练与推理的加速芯片，华为因被美国列入实体清单而受到出口管制约束，其高端芯片采购或使用可能被美方视为违反相关规定。马来西亚在评估 Ascend 910C 用于约 20 亿令吉的主权 AI 项目之际，美国官员警告这类做法可能违反美国出口管制，而马来西亚此前与美国签署的出口管制承诺也面临考验。马方则回应称会遵守所有适用出口管制法律，同时重申其根据国家利益制定政策的自主权。

**「影响」** 若马来西亚最终采用华为芯片，其主权 AI 项目可能面临美国出口管制合规风险，并加深对华为硬件生态的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/week-asia/politics/article/3366792/will-malaysias-potential-huawei-ai-deal-risk-clash-over-us-trade-pact">Will Malaysia’s potential Huawei AI deal risk clash with US trade pact? | South China Morning Post</a></li>
<li><a href="https://thearabianpost.com/malaysia-evaluates-huawei-chips-for-national-ai-network/">Malaysia evaluates Huawei chips for national AI network — Arabian Post</a></li>
<li><a href="https://www.deccanchronicle.com/technology/malaysia-eyes-huawei-chips-for-ai-project-despite-us-warning-1985500">Malaysia Eyes Huawei Chips for AI Project Despite US Warning</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#geopolitics`, `#Huawei`, `#export controls`, `#sovereign AI`

---

<a id="item-tech-news-11"></a>
### [库克缺席苹果 9 月 9 日发布会视频，新 CEO 主推折叠 iPhone](https://www.macrumors.com/2026/09/07/tim-cook-wont-appear-apple-sept-9-event-video/) ⭐️ 7.0/10

据彭博社 Mark Gurman 援引消息源，蒂姆·库克本周三会出席苹果“Surprise and Shine”活动放映会，但不会出现在活动视频中。库克已于 9 月 1 日卸任 CEO、转任执行董事长，约翰·特纳斯接任。苹果精心安排交接，让特纳斯成为折叠 iPhone 及后续新品的门面，若库克现身发布会反而会削弱这一效果。这意味着 9 月 9 日发布会视频将由新任 CEO 特纳斯主导折叠 iPhone 的发布。

telegram · zaihuapd · 9月8日 05:03

**「背景」** 苹果通常会在 9 月举办新品发布会，过去多由 CEO 在视频中主讲新款 iPhone 等产品。此次发布会涉及苹果首款折叠 iPhone，也是库克卸任 CEO、约翰·特纳斯接任后的首次产品发布，因此发布视频的主讲人变化成为外界关注焦点。

**「影响」** 对关注苹果新品发布的用户和投资者而言，9 月 9 日折叠 iPhone 的首次官方亮相将由新任 CEO 约翰·特纳斯主导，库克仅出席现场但不出现在视频中，这标志着苹果产品发布话语权的正式交接。

**标签**: `#Apple`, `#Tim Cook`, `#foldable iPhone`, `#CEO transition`, `#hardware`

---

<a id="item-tech-news-12"></a>
### [ASML 与台积电推进 High NA EUV 升级，12 英寸光掩模计划落地](https://www.nrc.nl/nieuws/2026/09/08/asml-gaat-samenwerken-met-taiwanese-chipgigant-tsmc-om-zijn-nieuwste-chipmachines-te-upgraden-a4936073) ⭐️ 7.0/10

ASML 与台积电于 2026 年 9 月 7 日宣布开展产业合作，推动 High NA EUV 光刻从现有 6 英寸光掩模转向 12 英寸规格，以提升设备生产率、降低芯片制造成本并减少拼接限制。根据计划，双方将在 2031 年建立 12 英寸光掩模试产线，2033 年将相关系统用于先进制程量产；台积电则拟从 2030 年起将 High NA EUV 用于先进节点的大规模制造。这一升级若落地，将改善先进半导体制造的光刻效率与经济性，但距离量产仍有多年的技术验证和基础设施准备期。

telegram · zaihuapd · 9月8日 06:55

**「背景」** 高数值孔径极紫外光刻（High NA EUV）是先进芯片制造中的下一代光刻技术，目前产线使用 6 英寸光掩模。ASML 与台积电认为，转向 12 英寸光掩模可提高扫描仪生产率、降低芯片制造成本并消除拼接限制；台积电计划于 2030 年起将 High NA 用于先进节点的大规模制造。

**「影响」** 对台积电及采用其先进制程的芯片设计公司而言，该路线图若兑现，将带来更高的 High NA EUV 光刻效率和更低的单位芯片制造成本，但真正量产要等到 2033 年前后且仍需试产验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tbreak.com/tsmc-asml-12-inch-photomasks-euv/">12 - inch photomasks : TSMC and ASML plan for High NA EUV</a></li>
<li><a href="https://startupfortune.com/asml-tsmc-samsung-and-intel-agree-on-ai-chip-roadmap-through-2033/">ASML , TSMC , Samsung and Intel Agree on AI Chip... - Startup Fortune</a></li>

</ul>
</details>

**标签**: `#semiconductor manufacturing`, `#EUV lithography`, `#ASML`, `#TSMC`, `#hardware`

---

<a id="item-tech-news-13"></a>
### [中国计划到 2030 年智能算力提升至 9800 EFLOPS](https://www.scmp.com/tech/policy/article/3366733/china-targets-fourfold-boost-ai-computing-capacity-2030-major-tech-push) ⭐️ 7.0/10

工信部发布未来五年产业规划，提出到 2030 年将中国智能算力提升至 9800 EFLOPS。规划明确 2026 年至 2030 年累计投入 3.8 万亿元用于信息基础设施建设，并有序部署万卡级以及 10 万卡以上的智能计算集群。同时，规划要求加强基础设施与国产算力芯片的适配。截至今年 6 月底，中国智能算力为 2185 EFLOPS，同比增长 177%；要实现 2030 年目标，算力规模需在此基础上增长至 4 倍以上。

telegram · zaihuapd · 9月8日 11:23

**「背景」** EFLOPS（exaFLOPS）表示每秒一百亿亿次浮点运算，是衡量超级计算和 AI 集群算力的常用单位。智能算力指面向人工智能训练与推理的计算能力，与通用算力、超算算力并列。

**「影响」** 该规划若按目标推进，将显著扩大国内 AI 训练与推理可用的智能算力供给，并要求云服务商、AI 企业和国产芯片厂商加快万卡级集群部署与国产算力芯片适配。不过，实现目标仍取决于后续资金到位、芯片供应和工程进度。

**标签**: `#AI infrastructure`, `#China`, `#technology policy`, `#computing power`, `#semiconductors`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [CoinGecko 报告：加密货币平台因网络攻击和密钥被盗损失超 36 亿美元，多数已做审计](https://www.cnbc.com/2026/09/08/crypto-platforms-lost-billions-to-cyberattacks-many-even-after-audits.html) ⭐️ 7.0/10

CoinGecko 报告显示，2025 年 1 月至 2026 年 7 月，加密货币平台因网络攻击和密钥被盗损失超过 36.3 亿美元，其中 88%的被盗资金来自已完成独立安全审计的平台。

rss · CNBC Finance · 9月8日 08:16

**「背景」** 安全审计指由外部机构检查平台代码和系统安全的评估，但多数攻击发生在审计未覆盖的环节；受影响最大的 Bybit 在 2025 年 2 月失窃 14 亿美元，Elliptic 认为攻击者来自朝鲜。

**「影响」** 加密货币投资者即使选择经过审计的平台，仍可能因审计覆盖范围之外的安全漏洞而承担资产损失风险。

**标签**: `#cryptocurrency`, `#cyberattacks`, `#security audits`, `#CoinGecko`, `#Bybit`

---

<a id="item-finance-news-2"></a>
### [上海 10 月起生育医疗费用个人“无自付”](https://mp.weixin.qq.com/s/jORA1qJsrSWa6VQaoM-b4Q) ⭐️ 7.0/10

上海宣布自 10 月 1 日起实施生育医疗费用新政：参保职工产前检查先使用每人 4500 元补贴，42 项围产检查超出部分由生育保险全额支付，住院分娩政策范围内费用全部报销。居民医保孕产妇和参加职工医保男职工的未就业配偶也按同样标准保障，合规生育费用个人不再自付。

telegram · zaihuapd · 9月8日 13:26

**「背景」** 生育保险待遇由社保基金支付，参保人无需直接为政策范围内的项目付费；上海此次把职工、居民医保孕产妇和符合条件的未就业配偶都纳入该保障。

**标签**: `#maternity insurance`, `#healthcare policy`, `#Shanghai`, `#social security`, `#public finance`

---