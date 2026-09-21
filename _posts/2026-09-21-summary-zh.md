---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> 从 30 条内容中筛选出 10 条重要资讯。

---

**科技新闻**
1. [ChatGPT 现通过广告收集器跨站追踪用户活动](#item-tech-news-1) ⭐️ 8.0/10
2. [Qwen Image 2.1 发布：7B 开放权重图像生成模型](#item-tech-news-2) ⭐️ 8.0/10
3. [Pirate Face 以种子和激活正交化抢救 LLM](#item-tech-news-3) ⭐️ 8.0/10
4. [中国船只因 AI 编造情报险遭美军拦截](#item-tech-news-4) ⭐️ 8.0/10
5. [长鑫科技第五代 DRAM 平台量产，24GB LPDDR5X 进入旗舰手机](#item-tech-news-5) ⭐️ 8.0/10
6. [三星预计明年 HBM4/HBM4E 产量翻倍以上](#item-tech-news-6) ⭐️ 7.0/10
7. [去污报告为何不可靠：评估者应控制测试并强制复现](#item-tech-news-7) ⭐️ 7.0/10
8. [LG 电视被曝关机偷录，智能电视普遍追踪用户](#item-tech-news-8) ⭐️ 7.0/10
9. [邵阳两公安局长敲诈沪企创始人 1 亿元被免职](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [关税、燃油价格与加息三重压力挤压美国企业](#item-finance-news-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [ChatGPT 现通过广告收集器跨站追踪用户活动](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/) ⭐️ 8.0/10

ChatGPT 已开始使用广告收集机制跟踪用户在其他网站上的活动，将标准广告技术中的跨站追踪引入 AI 聊天产品。该做法被指在 AI 聊天场景中没有先例，引发对用户数据隐私和 AI 系统设计的重大担忧。浏览器防护情况存在差异：Firefox、Brave 和 Safari 可阻止此类追踪，而 Chrome 和 Edge 不阻止。欧盟正在通过立法应对此类行为，部分用户认为这有利于消费者数据隐私。

hackernews · lmbbuchodi · 9月20日 15:18 · [社区讨论](https://news.ycombinator.com/item?id=49776729)

**「背景」** 广告技术行业长期使用第三方 Cookie 或像素，让广告平台在用户访问其他网站时识别同一浏览器或设备，实现跨站行为追踪。OpenAI 在 bzr.openai.com 的广告收集器设置了名为 \_\_obi、作用域为 .openai.com 的 Cookie，该值在用户使用 ChatGPT 时与其账户关联，并会在用户访问普通网站时被发回 OpenAI。这意味着原本用于广告的跨站追踪机制被应用于 AI 聊天产品，缺乏先例。

**「影响」** 对于使用 Chrome 或 Edge 访问 ChatGPT 的用户，浏览器默认不阻止此类跨站广告收集，其其他网站活动可能被关联至 ChatGPT 对话身份。

**「社区讨论」** 社区讨论普遍认为将标准广告技术用于 AI 聊天产品没有先例且令人不安，有人分享 Facebook 跨站广告追踪和 Gemini 整合用户信息的类似体验，并肯定欧盟立法对消费者隐私的保护。也有评论质疑该博客文章疑似由 AI 生成，要求作者使用自己的话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/">ChatGPT now knows what you do on other websites via ad collector</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI`, `#adtech`, `#web tracking`, `#ChatGPT`

---

<a id="item-tech-news-2"></a>
### [Qwen Image 2.1 发布：7B 开放权重图像生成模型](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen Image 2.1 是一个新的开放权重 7B 图像生成模型，显著提升了文字渲染并原生支持透明背景。相比上一代 Qwen-Image 的 20B 参数，体积缩小至 7B，是当前较小的开放权重模型之一（Z-Image Turbo 为 6B）。社区测试显示其文字渲染能力明显优于其他开放权重模型，尤其适合需要精细 UI 文本的提示生成设计场景。不过该模型采用了比以往 Qwen 模型（如 Apache 许可）更严格的许可证。这些特性使其在本地文本到图像生成中受到开发者关注。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**「背景」** Qwen Image 是阿里巴巴通义千问团队推出的图像生成模型系列，本次发布的 2.1 版本为 7B 开放权重模型，并将文本到图像生成与图像编辑整合在单一工作流中。官方示例显示该模型支持原生透明图像生成，并改进了文字渲染能力。

**「影响」** 对需要在本地部署图像生成且重视文字渲染与透明背景的开发者来说，该模型提供了 7B 规模的可行选择，但更严格的许可证可能限制商业使用，需在采用前评估合规性。

**「社区讨论」** 多数评论者对 Qwen Image 2.1 的 7B 体积、文字渲染和原生透明支持表示认可，同时担忧许可证限制。部分评论者认为本地图像生成的质量与速度目前优于本地代码生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/blog/what-is-qwen-image-2-1">What Is Qwen - Image - 2 . 1 ? Native 2K Editing</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen-Image-2.1">Qwen / Qwen - Image - 2 . 1 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#image generation`, `#open source`, `#Qwen`, `#text-to-image`

---

<a id="item-tech-news-3"></a>
### [Pirate Face 以种子和激活正交化抢救 LLM](https://pirateface.co/) ⭐️ 8.0/10

该 Hacker News 讨论围绕“Pirate Face”项目展开，提出用 BitTorrent 分发 LLM 权重、并用运行时拒绝向量正交化替代分发“abliterated”权重，以避免模型从 Hugging Face 等集中平台被删除后无法获取。评论者 wren6991 指出，不必分发修改后的权重，只需分发每层数千个浮点数的拒绝向量，在运行时对原版权重的激活进行正交化，效果等价且计算开销低，Antirez 的 DS4 已支持该方式。其他评论者认为 BitTorrent 本应成为 AI 模型权重的首选分发方式，并列举 Steam 与暴雪曾用种子协议分发游戏、星际争霸 2 安装器显示做种/下载者可视化的历史例证。讨论还提到实际痛点：手动用 rclone 囤积 Hugging Face 种子并检查比特腐烂很累，Pirate Face 名字不理想、缺少脚本化种子创建，以及对 Academic Torrents 互操作性的疑问。

hackernews · skepticalgenius · 9月20日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49776699)

**「背景」** Pirate Face 是一个将 Hugging Face 上的开放模型转换为经校验和验证的 BitTorrent 种子的去中心化分发层，利用全球节点组成的网络让模型权重在单个托管平台下架后仍可获取（tool-1-1）。讨论中提出的替代方案不是分发经过“消融”的权重，而是每层仅分发几千个浮点数的拒绝向量，并在运行时对激活进行正交化，因为两者效果等价且计算开销很低（tool-2-2、tool-2-3）。antirez 的 DS4 推理引擎已支持这种单向量激活方向引导，其思路源自论文《Refusal in Language Models Is Mediated by a Single Direction》（tool-2-3）。

**「影响」** 采用运行时激活正交化并配合 BitTorrent 分发，能让开发者仅共享小型拒绝向量而保留原版权重，从而减少对 Hugging Face 单点故障的依赖并降低分发修改后模型的风险。

**「社区讨论」** 评论区大体认同应优先用 BitTorrent 分发模型权重，且运行时正交化激活比分发 abliterated 权重更合理；但存在对 Pirate Face 命名、缺少脚本化种子创建、比特腐烂维护负担以及 Academic Torrents 兼容性的顾虑和疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pirateface.co/">Pirate Face - Turn AI into torrents that live forever</a></li>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm · GitHub</a></li>
<li><a href="https://github.com/antirez/ds4/tree/glm5.2">GitHub - antirez/ds4 at glm5.2 · GitHub</a></li>

</ul>
</details>

**标签**: `#llm`, `#open-source`, `#torrent`, `#model-distribution`, `#refusal-vectors`

---

<a id="item-tech-news-4"></a>
### [中国船只因 AI 编造情报险遭美军拦截](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship) ⭐️ 8.0/10

据 CNN 9 月 18 日报道，今年春天美军一项针对中国船只的武装行动在军机升空后才被叫停，而驱动行动的核心情报来自 AI 聊天机器人的凭空编造。美国特种作战司令部的一名情报分析员用 AI 聊天机器人融合公开来源情报与机密信号情报，机器人错误识别了船上货物清单。该分析员随后用 AI 把错误结论包装成格式规范的正式情报报告，分发到各指挥层级。据四名知情人士透露，美军启动拦截计划，其中两人称武装人员已准备登船、军机已起飞，直到行动前夕官员深挖报告来源才发现整份报告由 AI 生成、货物信息有误。

telegram · zaihuapd · 9月20日 03:07

**「背景」** AI 幻觉指聊天机器人等生成式模型可能输出看似合理但无事实依据的内容。美军近年推动“AI 优先”战略，在情报分析中引入此类工具，但缺乏强制人工核实流程。据后续报道，事件发生在 2026 年春季伊朗战争背景下，涉事工具将中国货船误判为运载核武器部件。

**「影响」** 最具体的影响是：AI 生成并被打包成正式报告的虚假货物情报（外部报道称其错误指认中国船只运载核武器部件）几乎导致美国军方对中国船只实施武装登船拦截，暴露出在高风险军事决策中缺少人工核验可能引发美中冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://securityaffairs.com/199415/ai/ai-hallucination-nearly-triggered-a-us-china-military-confrontation.html">AI Hallucination Nearly Triggered a US-China Military ...</a></li>
<li><a href="https://www.techtimes.com/articles/327796/20260920/us-military-almost-boarded-chinese-ship-over-ai-hallucinated-nuclear-claim.htm">US Military Almost Boarded Chinese Ship Over AI-Hallucinated ...</a></li>
<li><a href="https://www.explainx.ai/blog/us-military-ai-false-intelligence-china-ship-2026">AI Nearly Caused a US-China Naval Incident (2026) | explainx ...</a></li>
<li><a href="https://www.israelnationalnews.com/news/433380">AI -generated false report nearly triggered US ... | Israel National News</a></li>
<li><a href="https://www.geo.tv/latest/682719-ai-generated-false-intelligence-nearly-triggered-us-operation-against-chinese-ship">AI -generated false intelligence nearly triggered US operation against...</a></li>
<li><a href="https://gulfnews.com/world/americas/ai-generated-report-nearly-triggered-us-operation-on-chinese-ship-1.500680241">AI -Generated False Intelligence Nearly Triggered US Military...</a></li>

</ul>
</details>

**标签**: `#AI hallucination`, `#military AI`, `#AI safety`, `#intelligence analysis`, `#human-AI interaction`

---

<a id="item-tech-news-5"></a>
### [长鑫科技第五代 DRAM 平台量产，24GB LPDDR5X 进入旗舰手机](https://m.thepaper.cn/newsDetail_forward_34108116) ⭐️ 8.0/10

9 月 20 日，在 2026 世界制造业大会上，长鑫科技宣布第五代技术平台正式量产。基于该平台打造的 24 GB LPDDR5X 产品已进入量产，并全面进入国产主流旗舰手机。该平台将内存阵列有源区半间距缩至 11.95 纳米，存储器电容深宽比达 45:1，核心动能区高度降至 6762 纳米；同等条件下，每张晶圆产出较上一代提升 50%以上。这一进展表明国产 DRAM 在先进移动内存和高密度工艺上实现量产突破，有助于提升旗舰手机及 AI 系统内存性能。

telegram · zaihuapd · 9月20日 05:19

**「背景：CXMT 与 EUV 限制下的第五代 DRAM」** 长鑫科技（CXMT）是中国主要 DRAM 厂商。据外部报道，在美国出口管制切断了 ASML 的 EUV 设备供应后，其第五代 DRAM 平台通过 DUV 四重曝光实现了 11.95 纳米工艺，并已量产用于国产旗舰手机的 24Gb LPDDR5X 产品。这一进展被认为是 CXMT 追赶三星、SK 海力士和美光等全球领先内存厂商的重要一步。

**「影响」** 长鑫科技第五代平台量产，使国产主流旗舰手机可搭载单颗 24Gb、容量较上代同类型提升 50%的 LPDDR5X，并提供 496Ball/245Ball 封装选择，有助于提升大内存手机的性能与供应稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://easternherald.com/2026/09/20/cxmt-g5-dram-mass-production-china-semiconductor/">CXMT&#x27;s G5 DRAM Platform Enters Mass Production: The Chip Built Without ASML&#x27;s Banned Machines</a></li>
<li><a href="https://easternherald.com/2026/09/20/china-cxmt-g5-dram-mass-production-samsung-micron/">China&#x27;s CXMT Starts Mass Production of G5 DRAM at 11.95nm, Challenging Samsung and SK Hynix</a></li>
<li><a href="http://hekangmed.com/m/content/20260921-5302.shtml">夫妻互换老婆干B(完) 长 鑫 科 技 官宣 第 五 代 技 术 平 台 实现 量 产</a></li>
<li><a href="https://m.21jingji.com/article/20260920/herald/b20bd28b364929d537a45ca877ed43cd.html">AI...</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#LPDDR5X`, `#semiconductor manufacturing`, `#memory`, `#hardware`

---

<a id="item-tech-news-6"></a>
### [三星预计明年 HBM4/HBM4E 产量翻倍以上](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 7.0/10

据《首尔经济日报》援引消息人士报道，三星电子预计将在明年把 HBM4 和 HBM4E DRAM 的产量提高一倍以上。这一扩产计划针对人工智能加速器所需的高带宽内存供应紧张，属于下一代 HBM 产能的重要扩张。HBM4 和 HBM4E 是继 HBM3E 之后的高带宽内存标准，主要用于 AI GPU 和加速器。目前报道未给出具体的晶圆投入量或产能绝对值，但明确扩产幅度将超过一倍，反映业界对 AI 内存需求持续增长的预期。

hackernews · giuliomagnifico · 9月20日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49778029)

**「背景」** 高带宽存储器（HBM）通过垂直堆叠 DRAM 芯片提供远高于普通内存的带宽，是 AI 加速器的关键组件。下一代 HBM4 和 HBM4E 在堆叠层数和带宽上进一步升级，生产中需要使用玻璃载板辅助晶圆减薄。据韩国媒体报道，三星电子已于今年 2 月开始量产 HBM4，并于 5 月向英伟达等客户提供 12 层 HBM4E 样品，同时计划明年将相关玻璃载板外部清洗量从目前每月 2 万片增至 5 万片。

**「影响」** 对依赖 HBM 的 AI 加速器制造商而言，三星的扩产计划若实现，将有助于缓解高带宽内存的供应紧张，但实际效果取决于产能爬坡速度和客户认证进度。

**「社区讨论」** 社区讨论指出，HBM 产能是 AI 加速器供应的关键瓶颈之一，有评论认为华为升腾的产量受限于 CXMT 的 HBM 产能；另有评论担心三星扩产会进一步推高消费级 DRAM 价格，并质疑扩产幅度是否足以满足 AI 需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say">Samsung to Double HBM4 Output Next Year, Sources Say</a></li>
<li><a href="https://www.binance.com/en/square/post/09-20-2026-samsung-electronics-plans-to-double-hbm4-and-hbm4e-output-next-year-analyst-says-368643610309916">Samsung Electronics Plans to Double HBM4 and HBM4E Output ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#AI`, `#memory`, `#semiconductors`, `#supply chain`

---

<a id="item-tech-news-7"></a>
### [去污报告为何不可靠：评估者应控制测试并强制复现](https://www.reddit.com/r/MachineLearning/comments/1wlimaj/why_decontamination_reports_cant_fix_benchmark/) ⭐️ 7.0/10

OpenAI 在二月停止报告 SWE-bench Verified，并建议其他实验室也停止，因为所有测试的前沿模型都能复现部分任务的人类参考修复或问题陈述的逐字细节，六个月进展仅六分，剩余分数究竟有多少能力已不清楚。本文指出，去污报告无法解决这一问题，原因有三：实验室自查而外部无人能重跑搜索；训练语料不能公开，否则面临版权诉讼风险；基于 n-gram 的匹配会漏掉改写、论坛解答、GitHub 方案和由基准生成的合成数据。承诺与私有集合交集只能证明所声明语料的情况，不能证明模型实际训练数据，且现有训练证明方案已被展示可被欺骗。因此作者建议反转流程：评估者控制测试、提交方不接触标签、评估在无网络环境下运行、评估者从指定提交自行构建代码并复现分数，且测试数据尽可能在提交冻结后生成，只有被复现的结果才算数。作者还构建了一个小规模实现，并承认其无法证明基准本身质量、隐藏测试集不会被反复提交挤压、资助方未泄露标签，以及第三方无数据可重跑，其中反复提交挤压是最优先要弥补的缺口。

reddit · r/MachineLearning · /u/NoahPersaud · 9月20日 14:31

**「背景：SWE-bench Verified 与去污染报告」** SWE-bench Verified 是 OpenAI 推出的基准，用于评估大语言模型解决真实 GitHub 软件问题（如 issue 和 patch）的能力，由从 SWE-bench 数据集中筛选出的高质量子集构成，但源于公开代码库，存在被模型预训练吸收的风险。2026 年 2 月，OpenAI 宣布停止报告 SWE-bench Verified 的结果，因为发现前沿模型能够复现人类参考修复或问题陈述的具体细节，表明该基准已高度污染，并推荐改用 SWE-bench Pro。去污染报告通常由模型开发方自查训练语料与测试数据的重叠，但由于训练数据不公开、匹配方式有限等原因，外部无法复核其结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/">Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-swe-bench-verified/">Introducing SWE-bench Verified | OpenAI</a></li>
<li><a href="https://www.adwaitx.com/openai-swe-bench-verified-retired-ai-benchmarks/">OpenAI Drops SWE-bench Verified: What It Means for AI</a></li>

</ul>
</details>

**标签**: `#benchmark contamination`, `#AI evaluation`, `#SWE-bench`, `#decontamination`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [LG 电视被曝关机偷录，智能电视普遍追踪用户](https://www.theverge.com/tech/997682/every-tv-company-is-spying) ⭐️ 7.0/10

Gamers Nexus 发布的两个多小时调查视频指出，LG 智能电视在看似关机时仍会录制并存储音频、追踪观看内容，甚至可能被远程入侵变成监控设备。调查还发现，设备被 root 后麦克风会在语音命令结束后继续录音 10 至 15 秒。几乎所有智能电视都通过自动内容识别（ACR）追踪观看数据并共享给合作方，相关授权常隐藏在冗长协议中。LG 的回应未能平息用户愤怒，专家因此呼吁出台联邦隐私法，要求明确同意并限制数据收集。

telegram · zaihuapd · 9月20日 04:22

**「背景知识」** 自动内容识别（ACR）通过音频或画面指纹识别用户正在观看的内容，常用于广告投放和收视分析；智能电视通常将数据收集授权埋藏在冗长的用户协议中。Root 指获取设备最高系统权限，调查者借此发现语音结束后麦克风仍会继续录音 10 至 15 秒。

**「影响」** 受影响用户可能在电视看似关机时仍被采集音频和观看数据，且难以通过常规设置完全关闭此类追踪。远程入侵风险目前仅为可能性，尚未有大规模利用证据。

**标签**: `#privacy`, `#security`, `#smart TV`, `#ACR`, `#consumer electronics`

---

<a id="item-tech-news-9"></a>
### [邵阳两公安局长敲诈沪企创始人 1 亿元被免职](https://finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve6751470.shtml) ⭐️ 7.0/10

湖南邵阳县公安局局长尹向锋、副局长唐战雄因指挥民警赴上海“远洋捕捞”、向科技公司实控人郑帅敲诈 1 亿元，于 2025 年 7 月被免职。郑帅的公司因开发带 VPN 功能的软件被认定“翻墙”，本人于 2024 年 1 月在上海被警方带走，交足 1 亿元后才获取保候审。目前郑帅已被羁押近千天，案件久拖未判；邵阳县检察院今年已两次就超期羁押向法院发出《纠正违法通知书》。

telegram · zaihuapd · 9月20日 14:35

**「背景」** “远洋捕捞”指外地执法机关跨区域办案并采取强制措施，近年常被用来描述以案谋利或选择性执法；“翻墙”则指通过 VPN 等工具规避中国网络审查，相关软件常被认定为违法。本案中，邵阳县人大常委会于 2025 年 7 月表决免去尹向锋副县长、公安局长职务及唐战雄副局长职务，郑帅案已开庭但至今未宣判，且被羁押近千天。

**「对 VPN 相关从业者的风险」** 开发或运营 VPN 相关软件的中国科技从业者面临更具体的刑事与财产风险：异地公安可跨省抓捕、以“翻墙”为由立案，并要求高达 1 亿元的取保候审费用，且案件可能长期未判。检察院两次纠正超期羁押虽认定程序违法，但郑帅仍被羁押近千天，显示纠错机制未能及时终结羁押。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve6751470.shtml">finance.sina.com.cn/stock/companyt/2026-09-19/doc-inismzve...</a></li>
<li><a href="https://chinadigitaltimes.net/chinese/731968.html">【404...</a></li>
<li><a href="https://t.me/QQDS999/60257?single">Telegram: View @QQDS999</a></li>

</ul>
</details>

**标签**: `#China`, `#tech policy`, `#VPN software`, `#legal risk`, `#law enforcement`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [关税、燃油价格与加息三重压力挤压美国企业](https://www.cnbc.com/2026/09/20/tariffs-fuel-prices-and-interest-rates-squeeze-us-companies.html) ⭐️ 9.0/10

美国制造、运输和零售企业正面临关税、伊朗战争推高的燃料价格和美联储加息的同步挤压；美联储三年来首次加息并暗示今年可能再加息，同时爱荷华州一家制造商称其电机支架价格今夏从 42 美元涨至 87 美元。

rss · CNBC Finance · 9月20日 12:47

**「背景」** 这些压力源于特朗普政府关税推高原材料和商品成本，而美联储为遏制通胀加息，使企业为库存和设备融资更贵。

**「影响」** 中小制造商、汽车供应商和物流企业受冲击最直接，部分企业已停产、取消美国工厂计划或申请破产保护，消费者则面对同比上涨逾 23%的机票价格。

**标签**: `#tariffs`, `#fuel prices`, `#interest rates`, `#manufacturing`, `#inflation`

---