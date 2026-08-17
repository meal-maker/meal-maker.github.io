---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 42 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [DuckDB 2.0 预览版发布，社区关注新功能与路线图](#item-tech-news-1) ⭐️ 8.0/10
2. [AI 生成的 Copilot Autofix 致 Snowflake Jira 可被攻陷](#item-tech-news-2) ⭐️ 8.0/10
3. [Qwen3.8 27B 在 Artificial Analysis 上得分 52 超过前代及中型模型](#item-tech-news-3) ⭐️ 8.0/10
4. [稀有书追踪：亚马逊 AI 训练设施](#item-tech-news-4) ⭐️ 8.0/10
5. [GitHub 出现大面积过载并发布故障事件](#item-tech-news-5) ⭐️ 7.0/10
6. [如何让稀疏注意力与 KV 压缩在评测中显得出色](#item-tech-news-6) ⭐️ 7.0/10
7. [ChatGPT macOS 版上线 Computer History：记录点击按键但不截屏](#item-tech-news-7) ⭐️ 7.0/10
8. [苹果将调整 App 广告数据授权规则，第三方弹窗须中立](#item-tech-news-8) ⭐️ 7.0/10

**科技博客**
1. [分布式逐层卸载：vLLM-Omni 高效扩展 200B+ DiT 模型](#item-tech-blog-1) ⭐️ 9.0/10

**财经新闻**
1. [宇树科技 8 月 19 日科创板上市，发行价 150.8 元对应市销率 35.89 倍](#item-finance-news-1) ⭐️ 8.0/10
2. [知情人士称 Stripe 已敲定超 70 亿美元收购 OpenRouter](#item-finance-news-2) ⭐️ 7.0/10
3. [币安将限制与 HTX（火币）交易，8 月 23 日起生效](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DuckDB 2.0 预览版发布，社区关注新功能与路线图](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

DuckDB 官方发布了 2.0 版本的预览，介绍即将推出的功能和路线图。该消息在 Hacker News 上引起广泛关注。由于原始正文未提供，具体功能细节、兼容性限制、性能数据或发布日期尚不明确。社区评论反映出对嵌入式分析场景的持续热情，并提及名为 Quack 的功能、近期提交量以及增量物化视图等话题。这一大版本更新对依赖 DuckDB 的数据工程师和开发者具有重要意义。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**「DuckDB v2.0 背景」** DuckDB 是一个面向分析场景的嵌入式数据库，以单文件、列式存储和内存外处理能力著称，被广泛用于数据工程和本地分析。根据官方预览，v2.0 将在秋季发布，主要新增服务器模式（Quack）、触发器、VARIANT 类型、异步 I/O、新 SQL 解析器和新存储格式；项目由非营利 DuckDB 基金会治理，商业支持来自 Duck Labs。

**「社区讨论」** 多数评论对 DuckDB 表示肯定，有用户已在三家公司引入并用于超内存数据处理，另有人期待名为 Quack 的功能。部分讨论关注近六个月一万次提交是否依赖 AI，以及增量物化视图缺失是否让 ClickHouse 仍保有优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/08/17/duckdb-20-highlights?ref=upstract.com">A Preview of DuckDB v 2 . 0 – DuckDB</a></li>
<li><a href="https://runtimewire.com/article/duckdb-v2-server-mode-embedded-analytics">DuckDB previews v 2 . 0 plan to stabilize Quack server mode</a></li>
<li><a href="https://motherduck.com/blog/duckdb-ecosystem-newsletter-august-2026/">DuckDB Ecosystem Newsletter : August 2026</a></li>

</ul>
</details>

**标签**: `#duckdb`, `#database`, `#data-engineering`, `#olap`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [AI 生成的 Copilot Autofix 致 Snowflake Jira 可被攻陷](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

Wiz 研究人员披露，AI 生成的 GitHub Copilot Autofix 在 Snowflake 的一个 GitHub Actions 工作流中引入了模板注入漏洞，可能使 Snowflake 的 Jira 实例遭到攻击。该漏洞源于自动修复生成的代码在 workflow 的 run 块中未安全处理模板展开，攻击者可借此注入恶意命令或载荷。这一发现凸显 AI 生成修复在 CI/CD 管道中可能引入严重安全风险，需要与人类代码一样进行审查和扫描。

hackernews · galnagli · 8月17日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**「背景」** GitHub Copilot Autofix 是 GitHub 提供的自动安全补丁功能，会审查拉取请求并直接建议或应用代码修改。GitHub Actions 工作流可以被仓库事件触发，例如公开仓库的 issue 开启事件；如果工作流在 shell 脚本中直接展开不受信任的 issue 标题等输入，就会产生模板注入/脚本注入风险。Wiz 研究人员在 snowflakedb/snowflake-connector-net 仓库中发现，一个由 Copilot Autofix 共同编写的提交（PR \#1218，commit 4a1b8ce）重写了 jira\_issue.yml 工作流，使任何 GitHub 用户通过创建恶意标题的 issue 即可在该仓库的 Action runner 上执行任意命令，并可能被用于进一步访问 Snowflake 的 Jira 实例。

**「影响」** 对使用 GitHub Copilot Autofix 处理 GitHub Actions 工作流的团队而言，此案例表明自动修复可能引入模板注入漏洞，若未进行人工审查或静态扫描，可能使 CI/CD 管道及关联服务（如此处 Snowflake 的 Jira）面临未授权访问风险。目前尚无证据表明该漏洞已被实际利用。

**「社区讨论」** 评论区普遍认同 AI 生成的代码应像人类代码一样接受 SAST、SCA 等扫描，并建议在 CI 中使用 zizmor 检测模板注入；同时有人批评 YAML 规范本身充满陷阱。另有评论质疑相关 PR 中 Copilot 共同提交是否真的与漏洞相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug">Red Agent Exploits Snowflake Vuln Created by Copilot ... | Wiz Blog</a></li>
<li><a href="https://dev.to/jamilxt/copilot-autofix-introduced-a-critical-cicd-bug-at-snowflake-heres-how-to-harden-github-actions-1pf">Copilot Autofix Introduced a Critical CI/CD Bug at Snowflake .</a></li>
<li><a href="https://elsolitario.org/en/2026/08/17/wiz-red-agent-copilot-autofix-snowflake-en/">Copilot Autofix : The Bug an AI Exploited in Snowflake</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#CI/CD`, `#GitHub Actions`, `#vulnerability`

---

<a id="item-tech-news-3"></a>
### [Qwen3.8 27B 在 Artificial Analysis 上得分 52 超过前代及中型模型](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 8.0/10

Qwen3.8 27B 在 Artificial Analysis 基准中取得 52 分，相比 Qwen3.6 27B 的 38 分大幅提升。社区比较显示，该分数超过所有中型模型（40B–150B），并与 DeepSeek V4 Flash 0731 持平，后者暂列大模型类别第五。有用户评论称该模型在消费级游戏 PC 上可流畅运行，且表现接近或超过 Opus 4.6，但其部分说法尚未经独立复现。

hackernews · anana\_ · 8月17日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=49334544)

**「背景」** Artificial Analysis 是一个对开源和闭源模型进行综合评分的基准平台，分数反映模型在多个任务上的综合能力。Qwen3.8 27B 是阿里 Qwen 系列中的一个 27B 参数开源模型；DeepSeek V4 Flash 0731 是 DeepSeek 于 2026 年 7 月 31 日发布的大型混合专家模型（284B 总参数 / 13B 活跃参数），以极低价格提供接近前沿的性能。Opus 4.6 是 Anthropic 大约六个月前发布的前沿模型，曾被广泛认为处于领先地位。因此，一个 27B 参数的小模型在 Artificial Analysis 上获得与 DeepSeek V4 Flash 0731 相同的 52 分，并接近 Opus 4.6 的水平，是一个引人注目的效率突破。

**「影响」** 对于需要本地部署中等规模模型的开发者，27B 参数级别有望用游戏 PC 运行获得接近大型前沿模型的能力，但应自行验证其在具体工作流中的表现。

**「社区讨论」** 评论中既有惊叹其在小参数下接近前沿模型，也有用户表示难以置信并计划大量测试；有人称其推理方式类似 GPT-5.6-Sol-max，并认为 Opus 4.6 在世界知识上更强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lovableapp.org/blog/qwen-38-max-vs-glm-52-vs-kimi-k3-vs-deepseek-v4-flash">Qwen 3.8 Max vs GLM 5.2 vs Kimi K3 vs DeepSeek V4 Flash (2026): The Complete Frontier Model Comparison | Lovable APP Blog</a></li>

</ul>
</details>

**标签**: `#AI`, `#large language models`, `#benchmarks`, `#open-source`, `#efficiency`

---

<a id="item-tech-news-4"></a>
### [稀有书追踪：亚马逊 AI 训练设施](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media 于 2026 年 7 月在一批约 1000 本稀有书籍的大宗订单中放置了一枚 Apple AirTag，追踪结果显示这批书被送往美国拉斯维加斯东北部的亚马逊 LAS8 设施 VGT3 区域，入口处有一个“恐龙抓书”的标志。亚马逊仓库工人论坛的讨论确认 VGT3 会破坏性扫描大量书籍。此前图书经销商已多次收到来自价格不敏感匿名客户的大批量订单，并被怀疑用于 AI 训练数据采集，本次调查提供了具体实证。这一发现将亚马逊与大规模购书用于 AI 训练联系起来，引发版权与数据来源担忧。

rss · Simon Willison · 8月17日 15:21

**「背景」** 近年来，图书经销商多次收到价格不敏感匿名客户的大宗订单，普遍怀疑这些书籍被用于扫描以构建 AI 训练数据集。Simon Willison 曾在 2025 年 6 月报道过 Anthropic 的图书扫描活动，本次 404 Media 的 AirTag 追踪进一步验证了这类采购链条的存在。

**「影响」** 该调查为版权持有者提供了亚马逊可能未经许可批量扫描实体书用于 AI 训练的具体证据，可能加剧针对训练数据来源合法性的法律与伦理争议。

**标签**: `#AI training data`, `#copyright`, `#Amazon`, `#investigative reporting`, `#book scanning`

---

<a id="item-tech-news-5"></a>
### [GitHub 出现大面积过载并发布故障事件](https://www.githubstatus.com/incidents/zkxwbgr0cnmx) ⭐️ 7.0/10

GitHub 出现大面积过载或中断，用户访问时收到“No server is currently available to service your request”错误提示。发帖时 GitHub Status 页面尚未显示事件，随后官方创建了编号为 zkxwbgr0cnmx 的故障事件。有用户反映在事件发生近三小时后，GitHub 仍表示“正在定位根因”，且网页端无法查看 diff。该事件影响了依赖 GitHub 的代码托管、Pull Request 审查和协作开发等日常流程。

hackernews · SpyCoder77 · 8月17日 13:35 · [社区讨论](https://news.ycombinator.com/item?id=49330597)

**「背景」** GitHub 是广泛使用的代码托管与协作平台，其状态页面（githubstatus.com）用于发布服务中断事件及调查进展。此次事件中，用户最早反馈“无可用服务器”和部分页面 500 错误，官方随后确认正在调查影响拉取请求和问题页面的数据库基础设施问题，并最终标记事件已解决、承诺后续发布详细根因分析。

**「影响」** 此次中断直接导致 GitHub 用户在故障期间无法正常查看 diff、访问网站或使用代码托管功能，阻碍了依赖 GitHub 的开发与 CI/CD 流程，且恢复时间和根因在数小时内仍不明确。

**「社区讨论」** 评论区普遍表达失望与担忧：有观点将问题归因于规模扩张与领导层短视，也有人建议通过定价或限流应对 LLM 生成代码带来的流量激增，还有用户表示对 GitHub 的长期可靠性信心受挫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://statusfield.com/services/github/incidents">GitHub Incident History | Statusfield</a></li>
<li><a href="https://www.githubstatus.com/">GitHub Status</a></li>

</ul>
</details>

**标签**: `#github`, `#outage`, `#infrastructure`, `#developer-tools`, `#site-reliability`

---

<a id="item-tech-news-6"></a>
### [如何让稀疏注意力与 KV 压缩在评测中显得出色](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 7.0/10

Piotr Nawrot 在 X 上总结了自己多年来研究高效注意力和 KV 缓存压缩时发现的常见“美化”手法：使用无干扰项的单跳检索、已被污染的旧基准和冗余少样本示例，再结合滑动窗口注意力就能报告 5–10 倍压缩或稀疏度；不隔离自身贡献，改动窗口大小、块大小或仅优化自己方法的 Triton 内核，并利用聚合指标隐藏失败区域；此外还可用饱和任务、忽略统计显著性和不与更简单的替代方案（如更小模型、KV 量化）比较。文中以 RULER 的 13 个任务为例，指出其中 6 个 NIAH 任务、2 个 QA 任务和 VT 都容易让方法显得有效，而 NIAH-MK3 等真正压力测试常只在局限性中被略提。这些做法可能导致稀疏注意力和 KV 压缩研究中的性能提升被高估。

reddit · r/MachineLearning · /u/korec1234 · 8月17日 12:18

**「背景」** 稀疏注意力通过只计算部分注意力权重、KV 缓存压缩通过减少缓存中的键值对来降低长上下文推理的显存和计算成本。滑动窗口注意力只保留局部窗口内的 token，注意力汇聚点（attention sinks）则保留少数全局 token，因此很多检索任务不需要复杂压缩也能通过。RULER 是一套长上下文评测基准，其中 NIAH（needle-in-a-haystack）测试在大量文本中检索特定信息，NIAH-MK3 等变体包含多键和干扰项，更能检验无损压缩能力。

**「影响」** 研究人员和工程师在评估稀疏注意力或 KV 压缩方法时，应要求分离不同组件的影响、使用包含干扰项和未饱和的新基准并报告分项结果，否则可能将仅在简单检索或饱和任务上成立的结果误认为真实改进。

**标签**: `#sparse attention`, `#KV cache compression`, `#model evaluation`, `#benchmarks`, `#LLMs`

---

<a id="item-tech-news-7"></a>
### [ChatGPT macOS 版上线 Computer History：记录点击按键但不截屏](https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes) ⭐️ 7.0/10

ChatGPT 的 macOS 桌面应用新增“Computer History”功能，默认需手动开启，会把用户的点击和按键转化为事件，建立可供 ChatGPT 与 Codex 调用的活动时间线，用于学习工作方式、建议自动化和接手续办任务。该功能允许排除特定应用和网站、删除记录，并忽略无痕或隐私标签页。OpenAI 表示它不截取图像、视频或音频，只记录“事件”，与此前依赖截屏的 Windows Recall 类似但实现方式不同。该功能引发对隐私和安全的关注，因为点击和按键事件可能成为训练数据。

telegram · zaihuapd · 8月17日 04:16

**「背景」** Computer History 是 ChatGPT macOS 应用于 8 月 13 日推出的功能，通过 macOS 辅助功能 API 记录点击、按键和应用切换等事件，为 ChatGPT 和 Codex 建立可搜索的活动时间线。与 Windows Recall 依赖截屏不同，该功能不保存图像、视频或音频，而是将事件摘要以未加密的 Markdown 文件存储在用户本地磁盘。用户需手动开启，并可排除特定应用或网站、删除记录、忽略无痕或隐私标签页。

**「影响」** 对启用该功能的 ChatGPT macOS 用户而言，点击和按键事件会被转化为训练数据并用于 ChatGPT 与 Codex 的活动时间线，增加隐私暴露风险；用户可通过排除应用/网站和删除记录来降低风险，但该功能默认不截屏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/980742/chatgpts-computer-history-tracks-your-clicks-and-keystrokes">ChatGPT ’s Computer History tracks your clicks and... | The Verge</a></li>
<li><a href="https://best-ai.org/ai-news/openai-introduces-chatgpt-computer-history-for-macos-what-it-tracks-and-how-it-works-znqhif">OpenAI Introduces ChatGPT &#x27; Computer History &#x27; for macOS : What It...</a></li>
<li><a href="https://hwbusters.com/news/chatgpt-computer-history-logs-every-click-and-keystroke-on-your-mac/">ChatGPT Computer History Logs Every Click and Keystroke on...</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#AI agents`, `#privacy`, `#macOS`, `#computer-use`

---

<a id="item-tech-news-8"></a>
### [苹果将调整 App 广告数据授权规则，第三方弹窗须中立](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

路透社报道，苹果将调整 iPhone 和 iPad 上应用开发者使用个人数据投放定向广告的授权规则，结束多年调查。德国监管部门认定苹果 App 追踪透明度（ATT）框架对自家应用更有利，涉嫌违反竞争规则。苹果须在裁决送达后四个月内落实，承诺有效期七年；第三方授权弹窗需去除劝阻性措辞和符号。法国、意大利此前已分别对苹果罚款 1.5 亿欧元和 9860 万欧元。

telegram · zaihuapd · 8月17日 12:50

**「背景」** App Tracking Transparency（ATT）是苹果自 iOS 14.5 起推出的隐私框架，要求应用在跨应用或网站追踪用户前获得用户许可。德国联邦卡特尔局此前多年调查认为，苹果自身的 ATT 提示设计与第三方应用的弹窗相比可能自我优待，涉嫌违反竞争规则，因此要求其调整相关授权规则。

**「影响」** iOS 开发者及广告 SDK 将需要把第三方数据授权弹窗改为中性、无劝阻性设计，并在裁决送达后四个月内完成调整以满足德国合规要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://english.aawsat.com/technology/5307947-german-regulator-apple-change-app-data-consent-rules">German Regulator : Apple to Change App Data Consent Rules</a></li>
<li><a href="https://www.theverge.com/tech/980977/apple-app-tracking-transparency-settlement-germany">Apple ordered to stop scaring iPhone and iPad users away... | The Verge</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Tracking Transparency`, `#privacy`, `#antitrust`, `#iOS development`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [分布式逐层卸载：vLLM-Omni 高效扩展 200B+ DiT 模型](https://vllm.ai/blog/2026-08-17-distributed-layerwise-offload) ⭐️ 9.0/10

rss · vLLM Blog · 8月17日 00:00

**「背景」** 像 Cosmos3-Super（64B 参数、BF16 124GB）这样的视频生成 DiT 模型无法装入单卡 64GB HBM；作者指出，现有方案要么像 HSDP 那样把 HBM 塞到 56GB 只剩 8GB 余量，要么像纯 DP 逐层卸载那样每卡保存完整模型副本，导致主机内存随设备数线性膨胀（4 卡即 496GB），加载时 RSS 峰值更可达 O\(dp\_size×model\_size\)。

**「方案」** vLLM-Omni 团队的分布式逐层卸载同时解决两个瓶颈：先通过 meta 设备初始化与 mmap 加载让所有 rank 共享同一个 OS 页缓存，把冷启动 cgroup 峰值从 178GB 降到 47GB（-73%）。接着把权重切分到各 DP rank（每卡仅存 1/dp\_size），运行时用 AllGather 在专用通信流上重建当前层完整权重；配合固定双缓冲预取，HBM 上只保留约两层权重，不随总层数增长。作者实测 720p 10s 工作负载中，从 17B 到 64B 模型峰值 HBM 仅从 23.1GB 增至 28.1GB，而 HSDP 达 56.3GB。DP 多并发让每个 rank 并行处理不同请求，在 4 并发下达到单请求 HSDP 的 3.3 倍吞吐（约为理想 4 倍的 83%）；但在 8×B300 的 MiniMax-H3 测试中，AllGather 在 DP1×SP8 与 DP4×SP2 占优，DP8×SP1 则 rank-local DLO 更好，说明最优模式依赖拓扑。

**「启示」** 作者的核心结论是：通过权重切分+AllGather+双缓冲+mmap 共享页缓存，DLO 使主机内存从 O\(dp\_size×model\_size\) 降为 O\(model\_size+dp\_size×常数\)，HBM 保持有界，从而让 200B+ DiT 推理在 2TB 服务器上可行；但对 400GB 模型的估算尚未实测，生产环境仍需按拓扑验证。

**标签**: `#distributed inference`, `#layerwise offloading`, `#GPU memory`, `#Ascend NPU`, `#vLLM-Omni`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [宇树科技 8 月 19 日科创板上市，发行价 150.8 元对应市销率 35.89 倍](https://wap.eastmoney.com/a/202608173843415437.html) ⭐️ 8.0/10

宇树科技公告，公司股票将于 2026 年 8 月 19 日在上海证券交易所科创板上市，发行价 150.80 元/股，上市初期无限售流通股 3008.77 万股、占总股本 7.44%。发行价对应 2025 年摊薄后静态市销率 35.89 倍，高于可比公司平均水平。

telegram · zaihuapd · 8月17日 13:20

**「背景」** 宇树科技（Unitree）是一家总部位于杭州的民用机器人公司，由王兴兴于 2016 年创立，最初专注于消费级四足机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-sg/%E5%AE%87%E6%A0%91%E7%A7%91%E6%8A%80">宇 树 科 技 - 维基百 科 ，自由的百 科 全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics - Wikipedia</a></li>

</ul>
</details>

**标签**: `#IPO`, `#STAR Market`, `#Unitree Technology`, `#Robotics`, `#Valuation`

---

<a id="item-finance-news-2"></a>
### [知情人士称 Stripe 已敲定超 70 亿美元收购 OpenRouter](https://www.bloomberg.com/news/articles/2026-08-16/stripe-nears-deal-to-buy-ai-firm-openrouter-for-over-7-billion) ⭐️ 7.0/10

知情人士称，Stripe 已与 AI 模型访问服务商 OpenRouter 达成收购协议，金额超过 70 亿美元，但最终价格仍可能变动；Stripe 发言人称不评论传闻或猜测，OpenRouter 未置评。

telegram · zaihuapd · 8月17日 01:19

**「背景」** 此前《华尔街日报》上月曾报道 Stripe 与 OpenRouter 进行收购谈判；OpenRouter 成立于 2023 年，为开发者提供超过 400 个 AI 模型的访问服务，并于今年 5 月称已服务 800 万名开发者。

**「影响」** 若交易按报道完成，使用 OpenRouter 接入 400 多个 AI 模型的开发者和相关初创公司，可能会看到 Stripe 把支付计费与 AI 模型路由能力整合，改变其现有服务与基础设施选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/16/stripe-will-reportedly-acquire-ai-gateway-startup-openrouter-for-7b/">Stripe will reportedly acquire AI gateway startup OpenRouter for $7B+ | TechCrunch</a></li>
<li><a href="https://www.techtimes.com/articles/324688/20260817/stripe-closes-7-billion-openrouter-deal-payment-giant-now-bills-routes-ai-traffic.htm">Stripe Closes $7 Billion OpenRouter Deal: Payment Giant Now Bills and Routes AI Traffic</a></li>
<li><a href="https://forkast.news/stripe-acquires-openrouter-for-7b-turning-model-routing-into-a-payments-infrastructure-problem/">Stripe Acquires OpenRouter for $7B+, Turning Model Routing Into a Payments Infrastructure Problem – Forkast</a></li>

</ul>
</details>

**标签**: `#M&amp;A`, `#Stripe`, `#OpenRouter`, `#AI`, `#fintech`

---

<a id="item-finance-news-3"></a>
### [币安将限制与 HTX（火币）交易，8 月 23 日起生效](https://www.binance.com/en/support/announcement/detail/af2be67dc03c4673b4f56c42db948253) ⭐️ 7.0/10

币安宣布，自 2026 年 8 月 23 日起不再处理与 HTX（火币/Huobi Global SA）有关的直接或间接资产发送、接收及其他交易；相关交易可能被暂扣并接受合规审查，但不等于全球范围内禁止与火币进行任何交易。

telegram · zaihuapd · 8月17日 02:39

**「背景」** 币安称，这一限制是为遵守新的监管与制裁相关合规要求，不等于在全球范围内禁止与 HTX 进行任何交易。

**「影响」** 依赖火币与币安之间直接转账的加密货币交易者将失去一条直接通道，且被合规过滤器标记的关联普通钱包也可能受到限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/crypto/articles/binance-restrict-transactions-htx-10-152900808.html">Binance to Restrict Transactions With HTX, 10 Other Crypto Platforms</a></li>
<li><a href="https://en.coinotag.com/htx-binance-transfer-halt-aug-23">HTX (HTX) Faces Binance Transfer Halt Starting Aug. 23 - COINOTAG</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#exchange restriction`, `#Binance`, `#HTX`, `#compliance`

---