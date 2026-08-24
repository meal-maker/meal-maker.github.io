---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> 从 43 条内容中筛选出 13 条重要资讯。

---

**科技新闻**
1. [MS Paint 与 Photos 向 AI 修改图片静默嵌入 GUID 隐形水印](#item-tech-news-1) ⭐️ 8.0/10
2. [seL4 在 AArch64 上完成安全证明](#item-tech-news-2) ⭐️ 8.0/10
3. [延迟校正 Bellman 算子+因果归因约束 RL 方法](#item-tech-news-3) ⭐️ 8.0/10
4. [小米玄戒 O3 对标苹果，多核破 15000](#item-tech-news-4) ⭐️ 7.0/10
5. [OpenAI GPT-5.6 Sol API 输入降 20%、输出降 33%](#item-tech-news-5) ⭐️ 7.0/10
6. [AI 依赖或致编程专长崩塌](#item-tech-news-6) ⭐️ 7.0/10
7. [你的可执行文件也是 SQLite 数据库](#item-tech-news-7) ⭐️ 7.0/10
8. [AgentX-InferenceXv3：代理推理中 CUDA 护城河是否仍成立？](#item-tech-news-8) ⭐️ 7.0/10
9. [AI 空间软件生成可编程 3D 对象](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic Fable 5 企业需求疲软，高价面临替代竞争](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [阿里巴巴 80 亿港元配售投入 AI，港股一度跌 10%](#item-finance-news-1) ⭐️ 8.0/10
2. [比特币延续涨势，三日涨幅创 2023 年以来最大](#item-finance-news-2) ⭐️ 7.0/10
3. [美股盘前：阿里巴巴下跌 2%，钢铁股因加拿大报复性关税上涨](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [MS Paint 与 Photos 向 AI 修改图片静默嵌入 GUID 隐形水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

一项逆向工程分析显示，微软画图（MS Paint）和照片（Photos）应用会在经 AI 修改的图片中静默嵌入不可见的 GUID 唯一水印。即使图片是由本地模型生成或编辑，该水印仍会被添加，且没有用户提示或禁用选项。可见水印可以关闭，但隐形水印无法禁用。由于水印包含每用户唯一标识，可能被用于通过微软账号追溯创作者身份，引发隐私与匿名性担忧。社区评论指出，这削弱了“本地生成”的意义，并认为数据保护机构应介入审查。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**「背景」** 微软的 Paint 和 Photos 应用近期开始捆绑本地 AI 模型，使用户能在设备上完成生成式编辑。为了标识 AI 生成或修改的图像内容，这些应用引入了名为 Watermarker.dll 的组件，该组件会将服务器签发的 GUID 以不可见方式写入图像像素，且该过程独立于用户可关闭的可见水印设置。这意味着即使完全在本地进行的 AI 操作，输出的图像仍可能携带可追溯到特定用户或会话的标识符。

**「影响」** 使用 MS Paint 或 Photos 的 AI 图像编辑功能的用户，其输出图片会携带可追溯至微软账号的隐形标识，即使本地处理也无法避免，从而削弱匿名性。

**「社区讨论」** 社区讨论普遍担忧隐私侵犯和匿名性削弱，有评论认为核心问题不是 AI 而是秘密嵌入可追溯的唯一标识。另有评论提到微软曾错误地为所有 Azure DevOps 提交自动添加 Copilot 水印，直到用户大量反馈后才移除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/49421158">Microsoft Paint and Photos Embed Server-Issued GUIDs as... | Zeli</a></li>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI-generated content`, `#reverse engineering`

---

<a id="item-tech-news-2"></a>
### [seL4 在 AArch64 上完成安全证明](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核在 AArch64 架构上的安全证明现已完成，这是形式化验证操作系统领域的重要里程碑。该结果来自 proofcraft.systems 的公告，标志着这一广受尊重的高保证微内核在 ARM 64 位平台上获得了正式安全属性验证。不过，证明的范围限于非混合关键系统（non-MCS）且单核（unicore）配置，不覆盖多核或 MCS 场景。该进展为高保证嵌入式与军事等领域提供了更强的形式化保障，但社区也提醒需注意侧信道等未涵盖的攻击面。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是经过形式化验证的微内核，此前已在若干架构上完成功能正确性证明；其安全证明需要证明未经授权的信息访问在数学上不可能。AArch64 是 Arm 的 64 位指令集架构，Proofcraft 在该架构上完成了机密性与安全隔离的形式化数学证明，并获得英国国家网络安全中心（NCSC）支持，从而补齐了 AArch64 上的安全证明栈。

**「影响」** 对于在 AArch64 上开发非 MCS、单核 seL4 系统的开发者，这一安全证明提供了形式化保证，但多核或 MCS 配置仍无此证明。

**「社区讨论」** 评论区有人指出证明的细则是“non-MCS、unicore”，并质疑其实际覆盖范围；也有用户讨论 seL4 的采用情况（如 GenodeOS、LionsOS、汽车 hypervisor），认为嵌入式与军用市场可能继续资助，但需要原生 seL4/Linux 才能更可信地宣称能力模型提升安全性。另有评论担心侧信道计时攻击可能影响该结果的有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.linxi.com.au/news/sel4-microkernel-achieves-full-formal-security-verification-on-aarch64">seL4 Microkernel Formal Security Proofs Completed on AArch64 ...</a></li>
<li><a href="https://zeli.app/story/49418255">seL4 security proofs now complete on AArch64 | Zeli</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#operating systems`

---

<a id="item-tech-news-3"></a>
### [延迟校正 Bellman 算子+因果归因约束 RL 方法](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 8.0/10

Reddit 帖子介绍了名为 CCPL（因果后果惩罚学习）的约束强化学习方法，用于处理延迟且随机的约束违背，避免仅惩罚时间上相近但未必因果的动作。该方法使用延迟校正 Bellman 算子，其自适应有效折扣从后果延迟分布中学习，并在未知随机延迟下给出收缩证明；同时采用干预后果网络（ICN）估计每个动作的边际因果贡献以进行归因。作者明确指出当前 ICN 需要访问环境的结构因果模型来生成预训练标签，无法仅从观测或干预数据端到端学习，这限制了其在已知或可合理指定 SCM 的基准场景之外的适用性。

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · 8月24日 12:11

**「背景」** 在强化学习中，贝尔曼算子将值函数映射到其更新后的值，并且在有界值函数空间上通常是一个压缩映射，这是策略评估和值迭代收敛的重要基础（tool-1-2、tool-1-3）。传统的约束强化学习常假设违规后果立即发生并可归因于当前动作，但在真实环境中违规往往是延迟且随机的，导致以时间邻近性进行惩罚会错误归因。该项目中的 CCPL 方法通过从后果延迟分布学习自适应有效折扣来修正贝尔曼算子，并用在结构因果模型标签上预训练的干预后果网络估计动作的边际因果贡献，从而替代时间邻近性归因（tool-1-1）。

**「影响与局限性」** 该方法目前要求访问环境的结构因果模型（SCM）来生成 ICN 的预训练标签，因此在 SCM 未知或难以指定的现实应用中难以直接使用，限制了其在基准测试之外的实用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/ccpl-rl/">Causal Consequence-Penalized Learning for delayed constrained ...</a></li>
<li><a href="https://ai.stackexchange.com/questions/11057/what-is-the-bellman-operator-in-reinforcement-learning">terminology - What is the Bellman operator in reinforcement learning?</a></li>
<li><a href="https://ai.vixra.org/pdf/2604.0016v1.pdf">RL -Calibrated Chaos Engineering: A Constrained</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#constrained RL`, `#causal attribution`, `#delay-corrected Bellman operator`, `#machine learning research`

---

<a id="item-tech-news-4"></a>
### [小米玄戒 O3 对标苹果，多核破 15000](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

小米宣布发布三款玄戒芯片：AI 旗舰 SoC 玄戒 O3、AI 加速芯片玄戒 O100 和智驾 AI 芯片玄戒 D100，均已完成回片验证。玄戒 O3 采用十核全大核 CPU，官方称多核跑分首破 15000 分，社区评论引述 Geekbench 单核约 3945 分、多核 15221 分；其首发 G2-Ultra NX GPU，标称性能提升 85%、功耗降低 64%，并且是全球首个支持 LPDDR6 的移动处理器，带宽 113.8 GB/s。玄戒 O100 采用 6nm 晶圆级垂直堆叠和混合键合，带宽达 1.22 TB/s；玄戒 D100 为国内首款 3nm 智驾芯片，集成 20 核 CPU 与 16 核 NPU，最高支持 160 GB 统一内存，可本地部署 200B 参数模型，计划明年商用。评论提醒，采用同款 ARM C1-Ultra 的联发科天玑 9500 实验室 GB6 超 4000 分，但手机实际散热功耗限制下约 3300 分，且缺少每瓦性能数据，因此“对标苹果”仍需谨慎。

hackernews · tosh · 8月24日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49420873)

**「背景」** 小米玄戒 O3 是小米新发布的旗舰 SoC，采用台积电 3nm 工艺，集成 240 亿晶体管，CPU 由 10 个 Arm C1 系列大核组成，最高主频 4.35GHz。根据 Geekbench 6.5 测试，其单核约 3945 分、多核约 15221 分，安兔兔 V11 跑分约 522 万分，并配备 Arm G2-Ultra NX GPU。该芯片还首次在移动端支持 LPDDR6 内存，带宽达 113.8GB/s。

**「影响」** 小米作为全球第三大智能手机厂商，如今具备类似联发科的旗舰 SoC 能力，可能削弱高通和联发科在小米供应链中的地位。

**「社区讨论」** 社区讨论认为报道中“对标苹果”的说法需要谨慎：有评论指出单核成绩虽接近但并未超越苹果 M5 Max，多核优势来自 10 核对 6 核，且缺少每瓦性能与真实手机功耗数据；也有评论认为小米已具备类似联发科的芯片能力，对高通和联发科是坏消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gadgets.beebom.com/guides/xiaomi-xring-o3-benchmark-specs">Xiaomi Xring O3: Benchmarks and Specs | Beebom Gadgets</a></li>
<li><a href="https://www.itbear.com/hardware/xiaomi-unveils-three-proprietary-chips-to-build-a-full-ecosystem-ai-computing-foundation/">Xiaomi Unveils Three Proprietary Chips to Build a Full ...</a></li>
<li><a href="https://nokiapoweruser.com/xiaomi-xring-o3-chip-specs-benchmarks/">Xiaomi XRING O3 Specs &amp; Benchmarks: 3nm TSMC, 10-Core CPU ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#CPUs`, `#ARM`, `#benchmarks`, `#mobile chips`

---

<a id="item-tech-news-5"></a>
### [OpenAI GPT-5.6 Sol API 输入降 20%、输出降 33%](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI 已将 GPT-5.6 Sol API 的价格下调 20%（输入）和 33%（输出），并至少持续到 2026 年 11 月 21 日。修订后的价目表显示，gpt-5.6-sol 每百万 token 为输入 4.00 美元、缓存输入 0.40 美元、缓存写入 5.00 美元、输出 20.00 美元；gpt-5.6-terra 为 2.00/0.20/2.50/12.00 美元；gpt-5.6-luna 为 0.20/0.02/0.25/1.20 美元。Sol 的价格仍是 Luna 的 20 倍，但相比 Anthropic 等竞品更具吸引力。这一降价发生在模型能力容易被蒸馏复制、市场竞争激烈的背景下，降幅显著且持续期明确。

hackernews · tosh · 8月24日 15:22 · [社区讨论](https://news.ycombinator.com/item?id=49421074)

**「背景」** GPT-5.6 Sol 是 OpenAI API 提供的 GPT-5.6 系列模型之一，该系列还包括 Terra 和 Luna 等不同价格档位。其费用按每百万 tokens 计费，并区分输入、缓存输入、缓存写入和输出；本次调价前 Sol 通常对应输入 $5、输出 $30 的基准价格。OpenAI 也将 GPT-5.6 系列引入 Kiro 开发环境，突出价格性能比的优化。

**「影响」** 对于采用 GPT-5.6 Sol 的开发者，API 调用成本直接下降，且据评论区反馈，OpenRouter 平台上的 50% 折扣仍在生效，实际成本可低至 2/10 美元每百万 token。

**「社区讨论」** 评论区普遍对降价表示欢迎，认为 AI 智能商品化正走向价格战和“逐底竞争”，因为模型容易被蒸馏复制。也有开发者指出 GPT-5.6 Sol 在多步骤、长期任务上不如 Fable，容易在小细节上过度投入而忽略整体规划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6-in-kiro/">Advancing price -performance for developers with GPT ‑ 5 . 6 in... | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API pricing`, `#GPT-5.6`, `#cost reduction`, `#large language models`

---

<a id="item-tech-news-6"></a>
### [AI 依赖或致编程专长崩塌](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 7.0/10

Lars Faye 的评论文章认为，越来越依赖 AI 编码工具会阻碍深层软件工程专长的形成。文章标题即观点：编程专长将因 AI 依赖而崩塌。评论区多位从业者表示已在企业层面看到这一趋势，例如领导层要求“手写代码就是做错了”，代码产出速度超过人工理解和审查能力。也有人指出，无头智能体/氛围式编码受到关注，但引导式编码在经验丰富的开发者手中同样高效且质量更高。讨论强调，技能形成需要持续摩擦，而 LLM 改变了摩擦出现的位置，可能影响下一代工程师的成长路径。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**「背景」** 这篇文章由 Lars Faye 撰写，核心论点是：在软件工程中形成长期深层技能需要持续的“摩擦”（如调试、阅读代码、理解底层机制），而依赖 AI 编码工具可能消除这种必要摩擦，从而阻碍专业能力的培养。文中区分了“引导式编码”（在编辑器集成 LLM，由开发者主导并只让模型处理繁琐部分）与“代理式/氛围式编码”（完全交给模型自动生成代码），认为后者风险更高。相关讨论还提到，一些企业已要求工程师“手动写代码就是错”，导致代码产出速度超过人工审查与理解能力。

**「影响」** 在已经强制要求用 AI 生成代码的企业中，代码产出速度可能超过人工审查能力，导致难以理解、难以审查的代码积累，并减少能够深入排查和修正问题的资深工程师。

**「社区讨论」** 评论区普遍同意 AI 依赖可能侵蚀专长，但存在分歧：有经验开发者强调引导式编码（在编辑器中集成 LLM 辅助而非完全代理）能兼顾效率与质量；也有人认为追求摩擦的工程师会把 LLM 当作移动摩擦点的工具，另一些人则认为当前模式不可持续。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI Coding will Prevent Expertise | Lars Faye</a></li>
<li><a href="https://news.ycombinator.com/item?id=49027909">AI Coding Will Prevent Expertise | Hacker News</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#software engineering`, `#LLM`, `#developer productivity`, `#expertise`

---

<a id="item-tech-news-7"></a>
### [你的可执行文件也是 SQLite 数据库](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 描述了一种 Linux 技巧，可让 SQLite 数据库文件直接作为可执行文件运行。该方法把 SQLite 文件格式偏移 68 字节处的 4 字节应用 ID 设为 SELF（Structured Executable &amp; Linkable Format），并将 ELF 可执行格式的各组件按特定 schema 组织到多个 SQLite 表中。配套的 self-exec 解释器（用 C 语言编写）能提取并执行这些组件。还可通过 Linux 的 binfmt\_misc 机制让内核遇到匹配该二进制模式的可执行文件时自动调用解释器；文中给出的注册命令示例为 printf &\#x27;%s\\n&\#x27; &\#x27;:self:M:68:SELF::/usr/local/bin/self-exec:&\#x27; &gt; /proc/sys/fs/binfmt\_misc/register。

rss · Simon Willison · 8月24日 11:38

**「背景」** SQLite 文件格式在偏移 68 字节处包含一个 4 字节应用 ID 字段，可用于标识文件用途。Linux 的 binfmt\_misc 机制允许内核根据魔数等特征识别自定义二进制格式，并调用指定的解释器执行。

**标签**: `#SQLite`, `#ELF`, `#Linux`, `#Executable Format`, `#Systems Programming`

---

<a id="item-tech-news-8"></a>
### [AgentX-InferenceXv3：代理推理中 CUDA 护城河是否仍成立？](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat) ⭐️ 7.0/10

SemiAnalysis 在 AgentX - InferenceXv3 文章中分析了 CUDA 在代理推理负载中的主导地位是否仍然稳固。文章引用了一个价值 300 万美元的开源数据集、超过 100 万 token 的上下文长度、多轮子代理场景下 95% 以上的 KV 缓存命中率等具体技术指标。分析比较了 GB300 NVL72、MI355 与 B200 等硬件平台在代理推理中的表现。重点讨论了长上下文、KV 缓存效率以及新兴硬件对 CUDA 生态的潜在挑战。该分析对 AI 基础设施和硬件竞争具有重要参考价值。

rss · Semianalysis · 8月24日 00:19

**「背景」** 代理式推理（agentic inference）指模型在多轮交互中自主规划、调用工具并维护长上下文的任务，MLPerf 已将其纳入基准（tool-1-3）。此类负载对 KV 缓存复用、长上下文和硬件利用率提出新要求，而 SemiAnalysis 的对比测试覆盖 MI355X、GB300 NVL72、B200 等超过 1000 颗芯片（tool-1-1）。这为评估“CUDA 护城河”是否仍成立提供了基准背景。

**「影响」** 在 40–60 秒端到端延迟区间，MI355X ATOM 的单位美元性能可超过 GB300 NVL72 上的 vLLM。但在高交互性分离式推理中，MI355X 因 ROCm 软件栈缺少 kernel 与集合通信优化而实际表现更差，且 TensorRT-LLM 使 GB200/GB300 NVL72 在高吞吐下可获得超过一倍的性能优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv 3 : Does CUDA Moat Hold up in Agentic ...</a></li>
<li><a href="https://mlcommons.org/2026/07/agentic-inference-for-mlperf-inference/">Agentic Inference for MLPerf Inference - MLCommons</a></li>
<li><a href="https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat">AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?</a></li>
<li><a href="https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs">InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper - Formerly InferenceMAX</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#agentic AI`, `#CUDA`, `#GPU hardware`, `#KV cache`

---

<a id="item-tech-news-9"></a>
### [AI 空间软件生成可编程 3D 对象](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

一篇研究帖子介绍了一种用大语言模型生成 3D 对象的方法，将对象生成为空间软件而非传统网格体，从而天生可编程、可直接动画化。作者是论文合著者，并给出了演示网址 https://nova3d.xyz/ 和 GitHub 仓库。这类 3D 对象可在生成时携带逻辑，在移动端等弱算力环境与游戏引擎等强算力环境呈现不同效果，并具有完整层级结构与铰链/插槽关节。作者承认该方法在复杂有机形状上仍落后于传统 AI 3D 生成器，但认为代码最终会覆盖所有 3D 内容。帖子未给出具体量化指标或验证结果。

reddit · r/MachineLearning · /u/mhb\_11 · 8月24日 19:10

**「背景：从网格生成到空间软件」** 传统 AI 3D 生成器（如 Meshy.ai、Tripo3D、Luma AI Genie）通常直接输出 GLB、OBJ、FBX 等格式的完整网格模型，这些模型拓扑、UV 和材质相对固定，难以直接编辑和动画化。相比之下，Blender 中的 BlenderGPT 等智能体插件可以让用户通过自然语言生成 Python（bpy）脚本，从而在软件内部创建可编辑的四边主导网格。本文提出的方法将 LLM 用作空间软件生成器，生成的 3D 对象本身以软件形式存在，因此从诞生起就具备可编程、层级结构和铰接等特性。

**「影响」** 如果该方法成熟，工业设计、游戏开发、仿真和 AR/VR/XR 领域的开发者可能获得从生成起即可编程、动画就绪的 3D 资产，但复杂有机形状仍是明显短板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/AI_3D_model_generators">AI 3D model generators — Grokipedia</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#large language models`, `#spatial programming`, `#procedural generation`, `#research`

---

<a id="item-tech-news-10"></a>
### [Anthropic Fable 5 企业需求疲软，高价面临替代竞争](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) ⭐️ 7.0/10

据英国《金融时报》报道，Anthropic 旗舰模型 Fable 5 在企业市场的需求疲软；企业支出管理平台 Ramp 的数据显示，该模型上市首月仅占 Anthropic API token 用量约 6%、支出约 11%。其定价约为每百万输入 token 10 美元、每百万输出 token 50 美元，约为 Anthropic 其他旗舰模型的两倍，也高于 OpenAI 的 GPT-5.6 Sol。报道称，更便宜的开源模型和微软自研模型正在分流客户，而 Anthropic 保留用户数据 30 天的要求进一步抑制了企业采用。Ramp 经济学家认为，这表明企业为前沿 AI 付费的意愿已触及天花板。

telegram · zaihuapd · 8月24日 01:22

**「背景」** Anthropic 是一家人工智能公司，其最新旗舰模型 Fable 5 的定价约为每百万输入 token 10 美元、输出 50 美元，约为该公司其他旗舰模型的两倍，也高于 OpenAI 的 GPT-5.6 Sol。Ramp 是一家支出管理平台，其对超过 7 万家使用其 token 管理产品的企业数据进行了分析，用于衡量各 AI 模型的采用率与支出占比。在 7 月的数据中，Anthropic 于 7 月底以更低价格推出的 Claude Opus 5 已在企业支出中超过 Fable 5。

**「影响」** 对于考虑高端企业 AI 模型的企业客户，Fable 5 定价几乎翻倍且数据保留 30 天，可能推动它们转向开源或微软模型，并压缩 Anthropic 的企业 token 用量与收入份额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/ramp-anthropics-fable-5-plateaus-at-11-as-opus-5-overtakes">Ramp: Anthropic&#x27;s Fable 5 Plateaus at 11% as Opus 5 Overtakes</a></li>
<li><a href="https://xenospectrum.com/en/fable-5-enterprise-adoption/">Despite Top Performance, Fable 5 Adoption Lags: How Much Will ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise software`, `#Anthropic`, `#model pricing`, `#open source competition`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [阿里巴巴 80 亿港元配售投入 AI，港股一度跌 10%](https://www.cnbc.com/2026/08/24/alibaba-share-placement-drop-ai-hong-kong.html) ⭐️ 8.0/10

阿里巴巴宣布以 80 亿港元（约 102 亿美元）向非美国投资者配售新股，所得款项将全部投入 AI 基础设施。配售价为每股 112.70 港元，较上周五收盘价 123 港元折让约 8.4%，消息公布后其港股一度下跌 10%。

rss · CNBC Finance · 8月24日 08:21

**「背景」** 此次配售发生在阿里巴巴公布 6 月季度利润同比大跌 75%、资本开支同比上升 75%至 677 亿元人民币之后。

**「影响」** 新增 7.1 亿股将摊薄现有股东权益，并直接反映在配售价折让和股价下跌中。

**标签**: `#Alibaba`, `#share placement`, `#AI investment`, `#Hong Kong stocks`, `#capital expenditure`

---

<a id="item-finance-news-2"></a>
### [比特币延续涨势，三日涨幅创 2023 年以来最大](https://www.cnbc.com/2026/08/24/crypto-extends-gains-after-biggest-3-day-rally-since-2023.html) ⭐️ 7.0/10

比特币周一继续上涨，交易价格略低于 80,000 美元，此前三日累计上涨约 20%，为 2023 年以来最大；上周现货比特币 ETF 录得 19.2 亿美元资金流入，为 10 月以来最大单周流入。

rss · CNBC Finance · 8月24日 20:02

**「背景」** 这一走势发生在美国财政部表示将把较长期国债的购买量加倍、收益率短暂走低之后，此前比特币自 10 月以来长期困于低迷区间。

**标签**: `#Bitcoin`, `#cryptocurrency`, `#ETF inflows`, `#market rally`, `#Treasury policy`

---

<a id="item-finance-news-3"></a>
### [美股盘前：阿里巴巴下跌 2%，钢铁股因加拿大报复性关税上涨](https://www.cnbc.com/2026/08/24/stocks-making-the-biggest-moves-premarket-baba-mrvl-sndk-and-more.html) ⭐️ 7.0/10

美股盘前，阿里巴巴下跌 2%，此前公司宣布向非美国投资者发行 102 亿美元新股用于 AI 项目；钢铁股 Nucor 和 Steel Dynamics 上涨，因美加贸易谈判破裂，加拿大计划自 9 月 8 日起对美国钢铁行业加征报复性关税。

rss · CNBC Finance · 8月24日 11:31

**「背景」** 此前一周芯片 ETF 已下跌 5.5%，美加贸易谈判于上周五破裂。

**标签**: `#premarket`, `#Alibaba`, `#semiconductors`, `#steel tariffs`, `#cryptocurrency`

---