---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 42 条内容中筛选出 21 条重要资讯。

---

**科技新闻**
1. [Cerebras 与 OpenAI 宣称 GPT-5.6 Sol Ultrafast 推理快 7 倍](#item-tech-news-1) ⭐️ 8.0/10
2. [Spaghettifying DRAM：AMD DRAM 低层操控工具](#item-tech-news-2) ⭐️ 8.0/10
3. [DeepSeek V4 Pro 0813 发布并开放权重](#item-tech-news-3) ⭐️ 8.0/10
4. [特朗普允许私企海外监控与网络攻击](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepMind 发布手语转文字模型 SL2T，首次落地 Pixel 11 键盘与实时字幕](#item-tech-news-5) ⭐️ 8.0/10
6. [DeepSeek-V4-Pro 正式版上线并公布 API 峰谷定价](#item-tech-news-6) ⭐️ 8.0/10
7. [OpenAI 预览 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](#item-tech-news-7) ⭐️ 8.0/10
8. [Google 发布 Gemini 3.7 Flash 模型](#item-tech-news-8) ⭐️ 7.0/10
9. [DeepSeek Harness 开发者预览版发布：可追踪 AI 智能体开源框架](#item-tech-news-9) ⭐️ 7.0/10
10. [选择无聊技术：创新令牌的经典论点](#item-tech-news-10) ⭐️ 7.0/10
11. [City2Graph：面向城市异构图神经网络与空间分析的 Python 库](#item-tech-news-11) ⭐️ 7.0/10
12. [worldproof：诊断世界模型预测失败与像素指标失效窗口](#item-tech-news-12) ⭐️ 7.0/10
13. [Claude Chrome 扩展支持会话跨设备续传与同步](#item-tech-news-13) ⭐️ 7.0/10
14. [DeepSeek Harness 开源并开放 V4-Pro-0813 权重](#item-tech-news-14) ⭐️ 7.0/10
15. [谷歌发布 Gemini 3.7 Flash，距上代仅三周](#item-tech-news-15) ⭐️ 7.0/10

**财经新闻**
1. [长鑫存储市值超越腾讯，登顶中国市值最高公司](#item-finance-news-1) ⭐️ 8.0/10
2. [标普 500 指数二季度净利润率升至 16.9%，或创 2009 年以来最高](#item-finance-news-2) ⭐️ 7.0/10
3. [Steve Eisman 警示：AI 热潮过度依赖 OpenAI 和 Anthropic](#item-finance-news-3) ⭐️ 7.0/10
4. [长江存储升至全球 NAND 出货量第三，份额 14%超美光铠侠](#item-finance-news-4) ⭐️ 7.0/10
5. [电动汽车主导中国车市：7 月新能源车占新乘用车销量 65.1%](#item-finance-news-5) ⭐️ 7.0/10
6. [中国经济放缓挤压就业：零工岗位增至 5300 万仍供过于求](#item-finance-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cerebras 与 OpenAI 宣称 GPT-5.6 Sol Ultrafast 推理快 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 8.0/10

Cerebras 与 OpenAI 宣称推出 GPT-5.6 Sol 的 Ultrafast 模式，其推理速度比 Claude Fable 5 快约 7 倍。在 HLE 基准测试中，GPT-5.6 Sol Ultrafast 用 11 小时 11 分钟回答全部 2,500 道问题，而 Claude Fable 5 需要 78 小时 27 分钟（超过三天连续计算）才得出相同结论。双方表示 Ultrafast 在一个工作日内完成了对人类知识前沿的测试，精度相近但速度快近 7 倍。目前尚未提供独立证据证明该模式与常规 GPT-5.6 Sol 的性能完全一致，也没有公开定价信息。该结果属于专用硬件上的推理优化，而非新模型范式。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**「背景」** GPT-5.6 Sol 是 OpenAI 的最新模型，Ultrafast 是由 Cerebras 硬件支持的新 API 服务层级，可提供最高 750 tokens/s 的输出速度，宣称速度可达 14 倍。Humanity&\#x27;s Last Exam（HLE）是一个包含 2500 道研究生水平问题的基准测试，覆盖化学、经济学和文学等领域，通常只有博士水平才能回答。此前 Cerebras 与 OpenAI 合作，在 HLE 上测试了该模式，完整答题仅用 11 小时多。

**「影响」** 对于依赖长链推理或大规模评测的团队，若该模式上线并保持同等精度，HLE 级任务可从三天以上缩短到约半天；但目前缺少定价和独立复现，实际可用性仍不确定。

**「社区讨论」** 评论区既有对速度提升和迭代思考价值的期待，也有人质疑：双方帖子未明确说明 Ultrafast 与常规 GPT-5.6 Sol 的性能是否完全一致，也没有公开定价信息，仍需独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to 14X the speed - OpenAI</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/cerebras-powers-ultrafast-mode-openai-170000002.html">Cerebras Powers Ultrafast Mode for OpenAI&#x27;s GPT-5.6 Sol</a></li>

</ul>
</details>

**标签**: `#AI`, `#large language models`, `#hardware acceleration`, `#OpenAI`, `#Cerebras`

---

<a id="item-tech-news-2"></a>
### [Spaghettifying DRAM：AMD DRAM 低层操控工具](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

该 GitHub 存储库介绍了“Skitter Creek Bath Salts”项目，一个用于操控 DRAM 行为的技术探索与工具，主要针对 AMD Jaguar 架构，并提到 Zen3 因内存控制器寄存器基址不同而有差异。该工具通过低层访问内存控制器寄存器来“拉长”DRAM 操作，使 ring 0 权限能够触及原先隐藏在负环（negative ring）区域中的功能。此工作被描述为对 DRAM 内部机制的深入探索，可能用于硬件安全研究，并伴随 Black Hat 演讲发布（社区评论提及 Christopher Domas）。当前公开信息未明确列出其他受影响的 AMD 处理器家族，仅确认 Jaguar 可行、Zen3 需调整地址。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**「背景」** 现代 x86 平台中，内存控制器负责把物理地址翻译到 DRAM 的体、行和列，并保留一部分连操作系统内核都无法看到的专用地址区域（carveout）。该项目通过直接操作 AMD Jaguar（2013 年推出的低功耗架构）以及 Zen3 平台的内存控制器寄存器，改写物理 DRAM 地址转换，使一个地址可以映射到任意内存位置，从而暴露这些被隐藏的平台机密。

**「影响」** 在受影响的 AMD Jaguar 系统上，已获得 ring 0 权限的代码可利用该工具访问原本位于负环的隐藏功能，削弱基于权限层级的隔离。Zen3 是否可实际利用尚不明确，仅知道寄存器基址不同。

**「社区讨论」** 社区普遍期待 Christopher Domas 的 Black Hat 演讲，并称赞其讲解能力；同时有评论指出 DRAM 初始化所需的专有固件增加了攻击面。多位用户质疑除 AMD Jaguar 和 Zen3 外还有哪些 CPU 受影响，但页面未给出明确答案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking ...</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#hardware security`, `#low-level programming`, `#exploitation`, `#reverse engineering`

---

<a id="item-tech-news-3"></a>
### [DeepSeek V4 Pro 0813 发布并开放权重](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 最初通过 API 上线，Simon Willison 因 DeepSeek 没有官方公告页面而链接到 OpenRouter；随后该模型权重已在 Hugging Face 上发布，规模为 1.7T 参数、893 GB。该模型没有正式的基准发布渠道，相关数据先从官方微信群流出，经 Reddit 被删帖后转入 Hacker News 的 ASCII 表格。Willison 还发现低、中、高三个推理等级生成的骑自行车鹈鹕图像风格差异非常大，称在其他模型上未见过这种差异。

rss · Simon Willison · 8月12日 23:59

**「背景」** DeepSeek 此前已在 Hugging Face 发布 V4 Pro 和 V4 Flash 系列权重，因此 V4 Pro 0813 开放权重符合其惯例。OpenRouter 是一个聚合多家模型 API 的平台，用户可通过统一接口访问不同模型。

**「影响」** 对于需要本地部署或微调该模型的开发者，开放 893 GB 权重意味着可以自行托管，但需要大量存储和计算资源。

**标签**: `#deepseek`, `#open-source-ai`, `#large-language-models`, `#ai-release`, `#huggingface`

---

<a id="item-tech-news-4"></a>
### [特朗普允许私企海外监控与网络攻击](https://www.bloomberg.com/news/articles/2026-08-13/trump-enlists-private-sector-to-boost-cyber-offensive-arsenal) ⭐️ 8.0/10

美国总统特朗普签署备忘录，允许受联邦政府直接控制和监督的私营企业在海外开展监控和网络攻击，以打击针对美国人的外国网络化跨国犯罪组织。国土安全部将负责运行这一项目，并与司法部协调监督。参与企业须维持至少 100 万美元的保证金或托管款；若未遵守合同约定，该款项将被没收。

telegram · zaihuapd · 8月13日 05:10

**「背景」** 此前美国长期政策禁止私营企业自行发动“黑回去”（hack back）或进攻性网络行动，要求将事件上报执法部门。此次签署的国家安全总统备忘录改变了这一立场，指示政府借助私营部门的能力与创新，在美国联邦机构监督下开展针对外国网络犯罪组织的网络行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/">In a first, US will allow some private firms to carry out ...</a></li>
<li><a href="https://www.yahoo.com/news/politics/articles/trump-signs-memo-allowing-us-091707731.html?fr=sycsrp_catchall">Trump signs memo allowing US firms to carry out cyber attacks</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#offensive cyber operations`, `#technology policy`, `#government surveillance`, `#private sector`

---

<a id="item-tech-news-5"></a>
### [DeepMind 发布手语转文字模型 SL2T，首次落地 Pixel 11 键盘与实时字幕](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 发布大规模多语言手语转文字模型 SL2T，首次将手语 AI 带入消费产品，目前率先支持美国手语转英语，并已上线 Pixel 11 的 Gboard 和 Live Transcribe。该模型使用超过 10 万小时、50 多种手语数据训练，在 FLEURS-ASL 基准上零样本得分为 70 BLEURT，远高于此前纪录。出于隐私保护，SL2T 只处理手部和身体姿态关键点，不读取原始视频。DeepMind 表示后续将扩展更多设备和语言。

telegram · zaihuapd · 8月13日 08:55

**「背景」** 手语识别通常需要分析视频画面，而 SL2T 采用关键点表示，可以避免直接处理原始视频，从而降低隐私风险。FLEURS-ASL 是评估手语翻译的基准，BLEURT 用于衡量译文质量。此前手语 AI 多停留在研究阶段，较少进入主流消费设备。

**「影响」** Pixel 11 用户现在可以在 Gboard 和 Live Transcribe 中将美国手语转换为英语文本，且该过程只处理手部和身体姿态关键点而不读取原始视频，降低隐私风险，并为后续更多设备与语言扩展奠定基础。

**标签**: `#sign-language-recognition`, `#accessibility`, `#deepmind`, `#on-device-ai`, `#machine-translation`

---

<a id="item-tech-news-6"></a>
### [DeepSeek-V4-Pro 正式版上线并公布 API 峰谷定价](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 8.0/10

DeepSeek-V4-Pro 正式版已同步上线 App、网页端和 API，调用方式不变，模型名设为 deepseek-v4-pro。该模型增强了 Agent 能力，并原生支持 Responses API 格式，适配 Codex；V4-Pro 和 V4-Flash 的思考模式新增 low、high、max 三档。API 将实行峰谷定价，新价格于 2026 年 8 月 17 日 0 时生效，闲时价格为高峰时段的一半。

telegram · zaihuapd · 8月13日 11:12

**「背景信息」** DeepSeek 是一家提供大语言模型 API 服务的人工智能公司。本次的 V4-Pro 属于 V4 系列，该系列还包括 V4-Flash；V4-Pro 是总参数 1.6T、激活参数 49B 的混合专家模型，支持 100 万 token 上下文。V4-Pro 原生支持 OpenAI Responses API 格式，并针对 Codex 优化，便于现有 Agent 工作流迁移。

**「影响」** DeepSeek V4 系列 API 从 2026 年 8 月 17 日起实施峰谷定价，高峰时段价格可能达到闲时两倍，且新费率较当前上涨 50%至 1100%不等，直接推高开发者的调用成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/news/news260813/">DeepSeek-V4-Pro GA Release | DeepSeek API Docs</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V4 Pro - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://x.com/deepseek_ai/status/2087864589895798968">API pricing update 💰 With the V4 lineup release, we&#x27;re ...</a></li>
<li><a href="https://techstartups.com/2026/08/13/deepseek-raises-v4-api-prices-by-up-to-1100-just-as-chinese-ai-startup-launches-deepseek-v4-pro/">DeepSeek raises V4 API prices by up to 1,100% just as Chinese ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#API pricing`, `#release`, `#machine learning`

---

<a id="item-tech-news-7"></a>
### [OpenAI 预览 Ultrafast 模式，GPT-5.6 Sol 提速 14 倍](https://openai.com/index/previewing-ultrafast/) ⭐️ 8.0/10

OpenAI 首次展示 Ultrafast 模式，让 GPT-5.6 Sol 比标准处理快至 14 倍，并率先在 OpenAI API 上线。该服务由 Cerebras 驱动，每秒最高输出 750 个 token，面向故障响应、金融研究、客服与电商等对时间敏感的场景。目前仅向少数客户开放限量预览，OpenAI 表示将随算力扩充逐步扩大访问。这些性能数据来自 OpenAI 的预览声明，尚未提供独立验证或详细基准。

telegram · zaihuapd · 8月13日 17:04

**「背景」** Ultrafast 是 OpenAI API 新推出的服务层级，由 AI 芯片公司 Cerebras 提供硬件加速，专门面向需要低延迟、高吞吐量推理的场景。GPT-5.6 Sol 是 OpenAI 当前的前沿大语言模型，此次在 Ultrafast 模式下被部署到 Cerebras 基础设施上，以实现比标准处理更快的输出速度。

**「影响」** 对于已获限量预览资格的时间敏感型 API 用户，这可能将 GPT-5.6 Sol 的生成延迟降低至标准模式的约 1/14、吞吐提升至 750 tokens/s；但普通用户尚未可用，实际效果仍待独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-ultrafast/">Previewing Ultrafast mode: GPT‑5.6 Sol at up to ... - OpenAI</a></li>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI - cerebras.ai</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI inference`, `#latency`, `#Cerebras`, `#LLM`

---

<a id="item-tech-news-8"></a>
### [Google 发布 Gemini 3.7 Flash 模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

Google 发布了新的大语言模型 Gemini 3.7 Flash，并在 Hacker News 上引发社区对其能力与定价的讨论。该模型在图像转 HTML 测试中表现接近同价位模型，但仍逊于 Opus 5；在默认思考级别下生成 SVG 时出现“有缺陷的自行车”等细节问题。社区注意到其“介绍性定价”计划在 2026 年 12 月 31 日翻倍，2027 年 1 月 1 日起的价格将为每百万输入 tokens 1.50 美元、每百万输出 tokens 7.50 美元。部分用户认为与价格更低的 GPT-5.6 Luna 相比，Gemini 3.7 Flash 的性价比优势不足，并指出 3.6 Flash 仅在约三周前发布。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**「背景」** Google 的 Gemini Flash 系列定位为低成本、高吞吐量的模型，常用于总结、解析等大量文本场景。据官方模型卡，Gemini 3.7 Flash 以 Gemini 3.6 Flash 为基础训练，而后者仅在数周前发布。根据 Artificial Analysis 的页面，该模型于 2026 年 8 月作为 Google 专有模型发布。

**「对开发者的影响」** 使用 Gemini Flash 系列进行编码和智能体任务的开发者可以立即以更低价格调用 Gemini 3.7 Flash，因为谷歌在 3.6 Flash 发布三周后即推出并下调了价格。不过谷歌尚未公布 Pro 型号时间表，依赖旗舰模型的用户仍不确定何时能获得更新。

**「社区讨论」** 社区共识认为 Opus 5 在图像转 HTML 任务上仍是最佳，但 Gemini 3.7 Flash 作为价格相近的模型表现值得关注；主要争议在于其定价翻倍的长期计划，以及缺少与 Luna/Terra 的官方基准对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-7-flash/">Gemini 3 . 7 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-3-7-flash">Gemini 3 . 7 Flash (high) - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://www.androidheadlines.com/2026/08/google-gemini-3.7-flash-launch-price-cut-performance-boost.html">Google Drops Gemini 3.7 Flash AI Model with Price Cut</a></li>
<li><a href="https://www.reuters.com/business/google-unveils-gemini-37-flash-ai-model-coding-agent-workflows-2026-08-13/">Google unveils Gemini 3.7 Flash AI model for coding, agent ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Gemini`, `#model release`, `#Google`

---

<a id="item-tech-news-9"></a>
### [DeepSeek Harness 开发者预览版发布：可追踪 AI 智能体开源框架](https://deepseek.com/harness/en/) ⭐️ 7.0/10

DeepSeek 发布了 DeepSeek Harness 的开发者预览版，采用 MIT 许可证开源，这是一个基于新发布的 Cordis v4 论文的插件式框架，用于构建可追踪的 AI 智能体。该框架的核心特性是记录每次运行的追加式会话日志，包括系统提示、推理、工具调用与结果、子智能体调度和上下文注入，并可在轨迹视图中按来源检查，支持恢复、分叉、搜索和重放。它采用“一切皆插件”的架构，底层 Cordis v4 提供插件热加载/卸载及状态回滚能力。作者明确表示这是早期预览，存在许多粗糙之处和兼容性破坏变更，尚不适合生产环境。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**「背景」** DeepSeek Harness 是 DeepSeek 发布的开发者预览版开源框架，用于构建可追踪的 AI 智能体，所有能力均以插件形式实现，采用 MIT 许可证并已公开源码。其架构基于同日发布的 Cordis v4 论文，该插件内核此前已在 Koishi 项目中使用了约四年，支持热加载和卸载插件并在卸载时回滚副作用。该预览版本仍在快速迭代，可能会出现破坏性变更。

**「影响」** 开发者可以借此探索可追踪智能体和热插拔插件系统，但不应在生产环境中依赖它，因为 API 可能发生破坏性变更且功能仍较粗糙。

**「社区讨论」** 社区中有人赞赏可追踪事件流是“杀手级功能”，尤其对比美国模型封闭的加密追踪；另一些评论则认为该框架只是将热加载/动态启停能力扩展到 UI 组件，实用性有限，并表达了对“一切皆插件”的疲劳感。作者确认当前为早期预览，欢迎反馈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview : Everything is a plugin</a></li>
<li><a href="https://qcode.cc/en/deepseek-harness-guide">DeepSeek Harness + Cordis (2026): Developer Preview ... | QCode.cc</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#ai-agents`, `#open-source`, `#developer-tools`, `#traceability`

---

<a id="item-tech-news-10"></a>
### [选择无聊技术：创新令牌的经典论点](https://mcfunley.com/choose-boring-technology) ⭐️ 7.0/10

Dan McKinley 在 2015 年发表的《Choose Boring Technology》提出，团队应把创新限制在少数关键领域，其余部分采用经过验证的“无聊”技术。文章用“创新令牌”作比喻：每家公司长期内只有约三枚令牌，花在哪里需要慎重选择。这一概念帮助工程与产品负责人解释技术权衡，避免为了新颖而引入不必要的复杂性和风险。该文虽非新内容，但在 Hacker News 上再次引发讨论，并被认为在工程管理和架构决策中仍具有持久价值。

hackernews · tosh · 8月13日 17:48 · [社区讨论](https://news.ycombinator.com/item?id=49289512)

**「背景：创新代币与无聊技术的定义」** 这篇由 Dan McKinley 于 2015 年发表的文章提出了“创新代币”（innovation tokens）模型：每个公司大约只有三次创新机会，应将有限的创新投入到最关键的业务领域，其余部分则采用成熟、经过验证的“无聊技术”。所谓“无聊技术”指熟悉、稳定、测试充分且被广泛采用的技术，如选择 Node.js 或 MongoDB 等就会消耗创新代币。该文后来有演讲版本，其核心思想在工程管理和技术选型中被广泛引用。

**「影响」** 该文为工程负责人提供了一个具体的决策约束：把少数创新令牌用于最关键的技术选择，从而降低系统整体风险并便于向团队解释取舍。

**「社区讨论」** HN 评论区多数人肯定该文，尤其“创新令牌”对跨层级沟通的作用；同时有评论将概念延伸到 AI 代理，主张把创新集中在代理技术、周边用无聊技术。也有人批评令牌比喻含混，认为新旧只是风险弱代理，应直接分析具体需求、风险与收益，而非套用固定数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mcfunley.com/choose-boring-technology">Choose Boring Technology - Dan McKinley</a></li>
<li><a href="https://boringtechnology.club/">Choose Boring Technology</a></li>
<li><a href="https://jadon.us/posts/notes-on-choose-boring-technology/">Notes on - Choose Boring Technology by Dan McKinley</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#architecture`, `#innovation tokens`, `#technology strategy`, `#engineering management`

---

<a id="item-tech-news-11"></a>
### [City2Graph：面向城市异构图神经网络与空间分析的 Python 库](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 7.0/10

City2Graph 是一个新发布的 Python 库，用于将城市地理空间数据转换为适用于空间分析、网络分析和图神经网络（GeoAI）的异构图。该库支持从 OpenStreetMap 和 Overture Maps 构建建筑物、街道与城市肌理的形态图；通过 DuckDB 加载 GTFS 和 GBFS 数据并生成站点间公交图；把 OD 矩阵和流量数据转换为加权空间图；并提供 KNN、Delaunay、Gilbert、Waxman、queen/rook 邻接等构图方法，距离度量包括欧氏、曼哈顿和网络距离。它能在一个图中保留多种节点与边类型，支持元路径派生边，并可在 GeoDataFrames、NetworkX、rustworkx 和 PyTorch Geometric 的 Data/HeteroData 之间往返转换，同时保留几何和属性信息。相关论文已于 2026 年发表在《Computers, Environment and Urban Systems》第 130 期，作者为 Sato、Pietrostefani、Mahabir 和 Arribas-Bel。论文论证了为何城市数据用异构图表示优于扁平特征表，并说明了形态、交通、移动性和邻近构图之间的关系，以及转换中保持几何与图结构一致性的方法。

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · 8月13日 11:59

**「背景」** 城市分析通常把建筑物、街道、公交线路、出行流等数据作为相互独立的表格或图层处理，难以建模它们之间的空间和网络关系。异构图用不同类型的节点和边同时表示这些实体及其关联，更适合图神经网络等 GeoAI 方法。City2Graph 为这一需求提供了统一接口，能够从 OpenStreetMap、Overture Maps、GTFS、GBFS 和 OD 矩阵等数据构建异构图，并与 GeoPandas、NetworkX、PyTorch Geometric 相互转换。

**「影响」** 对城市计算和 GeoAI 研究人员而言，City2Graph 将 OSM/Overture、GTFS/GBFS、OD 矩阵等数据直接转换为可输入 PyTorch Geometric 的异构图，同时保留几何和属性，可降低构建城市 GNN 数据管线的工程成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://city2graph.net/">city2graph — GeoAI with Graph Neural Network (GNN) in Python</a></li>
<li><a href="https://github.com/c2g-dev/city2graph">GitHub - c2g-dev/city2graph: Transform geospatial relations into graphs for Graph Neural Networks and spatial network analysis · GitHub</a></li>

</ul>
</details>

**标签**: `#python`, `#graph-neural-networks`, `#geospatial-analysis`, `#urban-computing`, `#open-source`

---

<a id="item-tech-news-12"></a>
### [worldproof：诊断世界模型预测失败与像素指标失效窗口](https://www.reddit.com/r/MachineLearning/comments/1vnliv7/worldproof_diagnosing_where_worldmodel/) ⭐️ 7.0/10

开源工具 worldproof 用于诊断世界模型预测失败，比较 rollout 与真值及物理不变量，定位预测失效的位置和原因。验证中发现，在真实机器人视频上，像素指标难以对模型排序：copy-last-frame 基线在 SO-101 记录（30fps、三摄像头、64 rollouts、6 步 horizon）上获得 SSIM 0.983 和 PSNR 53.9 dB，且逐步 SSIM 不随 horizon 单调下降（0.972/0.923/0.893/0.943/0.920/0.950）。对 DROID 数据（15fps、64 rollouts、48 步）的测量显示三个区间：1–3 步几乎所有模型接近满分而无法区分，4–24 步单调下降可分离模型，28 步后地板振荡在约 0.20 SSIM 和 10.3 dB，预测完全去相关。作者据此认为这一数据的有效评估 horizon 约为 8–24 步，其值取决于帧率与任务速度，应自行测量而非沿用论文默认值；方法使用 64 rollouts、interquartile mean 和 stratified bootstrap CI，并做动态区域掩码。LPIPS 未能区分两个数据集，且计入 step 0 会因高帧率下免费的第一步而膨胀汇总标量。

reddit · r/MachineLearning · /u/georgia\_bucea · 8月13日 19:58

**「背景」** 世界模型是预测未来帧的生成模型，输入起始上下文和动作序列。像素指标如 SSIM、PSNR 和 LPIPS 常用于衡量预测帧与真实帧的相似度，copy-last-frame 是假设画面不变的朴素基线。在真实机器人视频中，静态背景占比高，容易掩盖运动区域，因此评估时常使用动态区域掩码；但在帧率较高、场景运动较慢时，相邻帧差异很小，朴素基线也能获得高分，导致指标失去区分能力。

**「影响」** 在真实机器人视频上评估世界模型时，研究者应报告按 horizon 划分的指标曲线并测量像素指标的可分离窗口，而不是直接沿用论文中的默认 horizon 或依赖汇总标量，否则可能错误地得出模型无差异或指标无效的结论。

**标签**: `#world-models`, `#evaluation-metrics`, `#robotics`, `#open-source-tool`, `#machine-learning`

---

<a id="item-tech-news-13"></a>
### [Claude Chrome 扩展支持会话跨设备续传与同步](https://techmymoney.com/2026/08/12/claude-in-chrome-now-carries-your-session-to-the-desktop/) ⭐️ 7.0/10

Anthropic 重构了 Claude 的 Chrome 扩展，使其以完整 Cowork 会话运行：浏览器中开始的任务可延续到桌面、网页和移动 App，对话、技能与连接器随账户同步。新增的“自动批准”模式会对照原指令审查表单提交、消息和文件下载等操作，但购买和个人数据仍需人工确认。Max 和 Team 用户今日可用，Pro 用户将在未来几周开放，企业版默认关闭、由管理员启用。Anthropic 表示这些措施能降低风险但无法消除，网页内恶意指令仍是难题；本地文件、其他 Chromium 浏览器和移动端暂不支持。

telegram · zaihuapd · 8月13日 04:10

**「背景」** Claude 的 Chrome 扩展此前主要作为浏览器内助手运行；Cowork 会话指 Claude 可执行多步骤任务并调用技能与连接器。此次更新将其从单纯的浏览器扩展升级为跨设备同步的完整会话环境，使用户不必在设备间手动迁移任务。

**标签**: `#Claude`, `#Anthropic`, `#Chrome extension`, `#AI assistant`, `#cross-device sync`

---

<a id="item-tech-news-14"></a>
### [DeepSeek Harness 开源并开放 V4-Pro-0813 权重](https://mp.weixin.qq.com/s/mANdGRI4fO_sEbC1ECEoZQ) ⭐️ 7.0/10

DeepSeek 发布了一款新的 Harness 应用并以 MIT 协议开源，将模型、工具、技能、会话、沙箱、存储、调度和 UI 等能力设计为可替换插件，并提供标准、PTC、极简和创造四种运行模式。该消息还称，DeepSeek-V4-Pro-0813 权重已在 Hugging Face 开放，相关 GitHub 仓库也已开放，采用“一切皆插件”的架构并由 Cordis 驱动。发布后 Hugging Face 页面曾一度 404，随后恢复。该信息来自 Telegram 转发，尚未获得官方独立确认。

telegram · zaihuapd · 8月13日 12:39

**「背景」** DeepSeek Harness（dsh）是由 DeepSeek AI 开发的开源智能体（agent）套件，其核心架构是“一切皆插件”，即模型、工具、技能、会话、沙箱、存储、调度和 UI 等能力都作为可替换插件；该架构由 Cordis 驱动，其设计思想来自《A Programming Paradigm for Spatiotemporal Composability》。开源模型权重通常通过 Hugging Face 等平台分发，用户可下载用于本地推理或微调。

**「影响」** 开发者现可从 GitHub 获取 MIT 许可的 DeepSeek Harness 源码并将其模型、工具、技能等能力作为可替换插件重新组合，同时 DeepSeek-V4-Pro-0813 权重已在 Hugging Face 开放下载（页面曾短暂 404 后恢复）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek-ai/deepseek-harness: DeepSeek Harness ...</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek - ai / deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI model release`, `#open source`, `#plugin architecture`, `#Hugging Face`

---

<a id="item-tech-news-15"></a>
### [谷歌发布 Gemini 3.7 Flash，距上代仅三周](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

谷歌于 2026 年 8 月 13 日宣布推出 Gemini 3.7 Flash，并开始逐步推送以替代仅三周前发布的 3.6 Flash。此前谷歌承诺在 6 月推出的 3.5 Pro 仍未发布。新模型在编码和代理性能上提升明显：FrontierCode 1.1 Main 得分由 34.4%升至 43.6%，DeepSWE v1.1 由 49%升至 65.3%。

telegram · zaihuapd · 8月13日 17:32

**「背景」** Gemini 3.6 Flash 是三周前发布的前代模型，此次被 3.7 Flash 快速取代。FrontierCode 和 DeepSWE 是衡量模型编码和代理能力的基准测试。

**标签**: `#Gemini`, `#Google`, `#AI`, `#LLM`, `#software engineering`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [长鑫存储市值超越腾讯，登顶中国市值最高公司](https://www.bloomberg.com/news/articles/2026-08-13/cxmt-overtakes-tencent-to-become-most-valuable-chinese-company) ⭐️ 8.0/10

据彭博社报道，芯片制造商长鑫存储（CXMT）已超越腾讯，成为中国市值最高的公司；其周四市值仍为 5240 亿美元，腾讯估值为 5100 亿美元。

telegram · zaihuapd · 8月13日 10:10

**「背景」** 长鑫存储上月在上海上市，首日暴涨 467%，此后又上涨 8%；腾讯周四因加大 AI 投入股价下跌 4.5%，今年以来累计下跌超过 26%。

**标签**: `#CXMT`, `#Tencent`, `#China stock market`, `#semiconductors`, `#market capitalization`

---

<a id="item-finance-news-2"></a>
### [标普 500 指数二季度净利润率升至 16.9%，或创 2009 年以来最高](https://www.cnbc.com/2026/08/13/these-charts-show-why-stocks-keep-rallying-profit-margins-are-highest-on-record.html) ⭐️ 7.0/10

据 FactSet 数据，标普 500 指数第二季度混合净利润率达 16.9%，高于第一季度的 14.8%和去年同期的 12.9%，若保持将是 2009 年有记录以来最高。剔除 Alphabet 和亚马逊后，该利润率仍为 15%，同为纪录。

rss · CNBC Finance · 8月13日 20:21

**「背景」** 净利润率是公司在支付所有费用后从收入中保留的比例；FactSet 自 2009 年开始追踪该指标。

**标签**: `#profit margins`, `#S&amp;P 500`, `#stock market`, `#corporate earnings`, `#market analysis`

---

<a id="item-finance-news-3"></a>
### [Steve Eisman 警示：AI 热潮过度依赖 OpenAI 和 Anthropic](https://www.cnbc.com/2026/08/13/big-short-investor-steve-eisman-sees-an-achilles-heel-in-the-ai-boom.html) ⭐️ 7.0/10

投资者 Steve Eisman 周二在 CNBC 节目中警告，AI 热潮日益依赖 OpenAI 和 Anthropic 两家公司；他称这两家 AI 初创企业占微软、亚马逊、Alphabet 旗下谷歌和甲骨文 AI 相关收入的约 70%，占其云收入的 25%至 35%，并认为更便宜的中国开源模型可能抢占市场份额、引发价格战。

rss · CNBC Finance · 8月13日 15:16

**「背景」** Steve Eisman 因在全球金融危机前做空美国房地产市场而闻名，其观点常被市场关注。

**标签**: `#AI boom`, `#OpenAI`, `#Anthropic`, `#China`, `#cloud computing`

---

<a id="item-finance-news-4"></a>
### [长江存储升至全球 NAND 出货量第三，份额 14%超美光铠侠](https://www.cnbc.com/2026/08/13/chinese-firm-tops-micron-kioxia-shipments-nand-memory-chips.html) ⭐️ 7.0/10

据 Counterpoint Research，长江存储科技（YMTC）在 2026 年第二季度全球 NAND 闪存芯片出货量中升至第三位，市场份额 14%，超过美光（Micron）和铠侠（Kioxia），仅次于三星和 SK 海力士。

rss · CNBC Finance · 8月13日 02:59

**「背景」** 长江存储（YMTC）是一家 2016 年在武汉成立的中国 NAND 闪存芯片制造商，有政府投资背景，并面临美国出口管制限制。

**「潜在市场影响」** YMTC 在第二季度 NAND 出货量份额升至 14%，超越美光和铠侠，这可能加剧 NAND 存储芯片市场的价格竞争，使美光、铠侠等既有厂商的出货量和定价承压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.notebookcheck.net/YMTC-builds-homegrown-NAND-production-line-to-sidestep-U-S-sanctions.1064510.0.html">YMTC builds homegrown NAND production line to sidestep U.S ...</a></li>
<li><a href="https://www.tradingkey.com/analysis/stocks/us-stocks/262101853-ymtc-overtakes-micron-kioxia-nand-shipments-global-third-tradingkey">YMTC NAND Shipments Jump to Third Globally, Surpassing Micron and Kioxia as Micron&#x27;s eSSD Pricing Power Faces Pressure</a></li>
<li><a href="https://seekingalpha.com/news/4632116-chinas-ymtc-overtakes-kioxia-micron-in-global-nand-shipments-counterpoint">China’s YMTC overtakes Kioxia, Micron in global NAND shipments: Counterpoint (MU:NASDAQ) | Seeking Alpha</a></li>

</ul>
</details>

**标签**: `#NAND memory`, `#semiconductors`, `#YMTC`, `#market share`, `#China tech`

---

<a id="item-finance-news-5"></a>
### [电动汽车主导中国车市：7 月新能源车占新乘用车销量 65.1%](https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html) ⭐️ 7.0/10

中国最新汽车销售数据显示，7 月新能源汽车占新乘用车销量的 65.1%，高于去年同期的 54%；今年前 7 个月整体乘用车销量同比下降 20.3%。

rss · CNBC Finance · 8月13日 01:31

**「背景」** 中国乘用车市场信息联席会数据显示，去年同期新能源汽车占中国新乘用车销量的 54%，今年 7 月升至 65.1%；今年前七个月整体乘用车销量同比下降 20.3%，新能源汽车销量同比下降 12.5%。

**「影响」** 传统燃油车厂商和在华外资车企面临更激烈的竞争，其销量在中国市场承压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/12/china-car-sales-data-byd-tesla-geely-vw.html">EVs dominate China’s car market: 5 takeaways from ... - CNBC</a></li>

</ul>
</details>

**标签**: `#China auto market`, `#electric vehicles`, `#auto sales data`, `#BYD`, `#Tesla`

---

<a id="item-finance-news-6"></a>
### [中国经济放缓挤压就业：零工岗位增至 5300 万仍供过于求](https://www.ft.com/content/a3803e70-cb4d-444f-a31e-05be2f2c44f6?accessToken=zwAAAZ_5xcXzkdOjgD5wy01ET9OjHgW-LyxE9g.MEUCIQCWTIny3JTJV8e-PGyK0XL2tg5g_7Ay-rpKkwGZCpp1-AIgbMgJQPlqWgqAsX4s1k4gYaC4b8k0JveZOs35OJQvbZ4&amp;amp;sharetype=gift&amp;amp;token=7e8483bb-395d-429e-afca-2f4ab5ad150b) ⭐️ 7.0/10

据英国《金融时报》报道，中国经济放缓加剧就业挤压，截至 2025 年外卖和网约车司机超过 5300 万人，两年增加 1000 万人，但零工岗位仍供过于求。

telegram · zaihuapd · 8月13日 06:40

**「背景」** 房地产低迷、消费疲弱、建设制造业收缩及自动化使零工经济成为过剩劳动力的出口，而供过于求正在拉低从业者收入并延长工时。

**「影响」** 受此影响，数千万外卖骑手和网约车司机面临更低的单位收入和更长的排队等单时间。

**标签**: `#中国经济`, `#就业`, `#零工经济`, `#网约车`, `#外卖`

---