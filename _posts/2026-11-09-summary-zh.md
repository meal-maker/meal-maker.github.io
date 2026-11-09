---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 从 30 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [KetchUp：Rust 与 WebGPU 驱动的开源 SketchUp 替代品](#item-tech-news-1) ⭐️ 7.0/10
2. [Outlook.com 拒收未配置 DMARC 的域名邮件](#item-tech-news-2) ⭐️ 7.0/10
3. [高盛据报叫停银行家和交易员使用 Claude Code](#item-tech-news-3) ⭐️ 7.0/10
4. [Drex Max v1.1 据称达多模态决策模型 SOTA，公布训练论文与开放权重](#item-tech-news-4) ⭐️ 7.0/10
5. [苹果明年或让 Siri 更像智能体](#item-tech-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [KetchUp：Rust 与 WebGPU 驱动的开源 SketchUp 替代品](https://ketchup3d.github.io/app/) ⭐️ 7.0/10

KetchUp 是一个新的开源浏览器端 3D 建模工具，使用 Rust 和 WebGPU 构建，提供类似 SketchUp 的建模体验。它旨在填补 SketchUp 逐渐增加限制后留下的空白，为开发者与用户提供免费且可扩展的替代方案。目前公开信息未包含具体版本号、性能数据或功能清单，但社区反馈显示其浏览器内 Rust UI 运行流畅，文本渲染效果令人印象深刻。该项目的出现反映了开源社区对轻量、可定制 3D 建模工具的需求。

hackernews · dcoulmbe · 11月8日 22:35 · [社区讨论](https://news.ycombinator.com/item?id=50418176)

**「背景」** SketchUp 是一款以直观推拉建模著称的 3D 设计软件，但其许可模式逐渐收紧并历经多次易主。KetchUp 是一个使用 Rust、WebAssembly 和 WebGPU（也支持 WebGL2）构建的免费开源替代品，可在浏览器或桌面运行，无需账户，主要面向木工和家具设计。它支持导入 SketchUp（.skp）几何体，并可导出 Wavefront OBJ 文件以便在其他工作流中使用。

**「影响」** 对于需要轻量、免费且可嵌入浏览器的 3D 建模用户，KetchUp 提供了一个新的开源选项，但其成熟度与触控板等交互支持仍有待完善。

**「社区讨论」** 社区普遍欢迎这个 SketchUp 的精神续作，尤其赞赏其在浏览器中流畅的 Rust UI 和文本渲染效果；同时也提出缺少触控板支持、登录页缺少功能展示等改进建议，并有用户讨论用 AI 辅助构建自定义工具的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Ketchup3D/app">GitHub - Ketchup3D/app: Free, open-source 3D modeling ...</a></li>
<li><a href="https://daily.dev/posts/ketchup-open-source-sketchup-alternative-built-with-rust-and-webgpu-lquqfnjed">KetchUp – Open-source SketchUp alternative built with Rust ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#rust`, `#webgpu`, `#3d-modeling`, `#sketchup-alternative`

---

<a id="item-tech-news-2"></a>
### [Outlook.com 拒收未配置 DMARC 的域名邮件](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc) ⭐️ 7.0/10

据报道，Outlook.com 正在拒绝来自未配置 DMARC 的域名发送的电子邮件。DMARC 是一种用于防止域名被冒用的邮件验证制度，缺少该配置的域名将无法通过 Outlook.com 的接收检查。这一变化对邮件送达率有显著影响，域名管理员需要发布 DMARC 记录才能确保邮件到达 Outlook.com 收件箱。自建邮件服务器和小型域名的管理员受到的影响尤为明显。

hackernews · xmddmx · 11月8日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50416158)

**「背景：DMARC 与 Outlook.com 的退信规则」** DMARC 是基于 SPF 与 DKIM 的邮件认证策略，发件域通过 DNS TXT 记录声明未通过验证邮件的处理方式，收件方据此决定是否拒收或隔离。根据 MailRoute 的观察，微软的 Outlook.com 和 Hotmail 自 11 月 5 日起开始退回来自没有任何 DMARC 记录域名的邮件，小型发件人也受影响，常见错误为 550 5.7.1。只要 SPF 或 DKIM 与 From 域对齐，添加一条 DMARC TXT 记录即可满足要求。

**「影响」** 未配置 DMARC 的域名发给 Outlook.com 用户的邮件可能被直接拒绝，导致通知、事务邮件或业务沟通无法送达。

**「社区讨论」** 评论中多数认为发件方早应配置 DMARC，并支持微软改进；但也有管理员抱怨 Outlook.com 还使用不公开的 IP 封锁列表，甚至在 SPF/DKIM/DMARC 都正确时仍会无声丢弃邮件。另有评论指出实际会返回 5xx 永久投递失败，并非完全静默。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mailroute.net/blog/outlook-rejecting-email-without-dmarc">Outlook.com Is Quietly Rejecting Email From Domains Without DMARC</a></li>
<li><a href="https://news.lavx.hu/article/outlook-com-rejects-some-email-from-domains-without-dmarc-records">Outlook.com Rejects Some Email From Domains Without DMARC ...</a></li>

</ul>
</details>

**标签**: `#email`, `#DMARC`, `#Outlook.com`, `#Microsoft`, `#deliverability`

---

<a id="item-tech-news-3"></a>
### [高盛据报叫停银行家和交易员使用 Claude Code](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

据报道，高盛正在取消银行家和交易员等非工程人员使用 Claude Code 的权限，原因涉及安全、合规和计费挑战。这一限制被解读为企业级 AI 编程代理在金融核心岗位上面临治理、安全和成本压力的一个例子。社区评论补充指出，半无人值守的代理在可访问客户/交易/自营信息、邮件和互联网的同一台工作机器上运行风险过高，并且 Anthropic 的消费计费模式难以提供稳定预算。具体限制范围或持续时间尚未明确。

hackernews · TheWiggles · 11月8日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=50415628)

**「背景」** Claude Code 是 Anthropic 推出的 AI 编码工具，此前被高盛部分交易员和银行家用于追踪客户资金流向和构建市场模型。高盛同时与 Anthropic 合作，将 Claude 代理部署到交易会计与客户尽职调查等环节，但现已把 Claude Code 和 GitHub 限制给工程师使用。这反映出非工程场景中使用 AI 编码代理时，企业需要应对安全、合规和计费等方面的治理问题。

**「社区讨论」** Hacker News 评论普遍将其归因于治理风险与账单失控。有用户指出，让半自动代理运行在可接触客户/交易数据、邮件和内部网络的同一台机器上过于危险；另有人称本组织因 Claude 消费计费持续超支而收回权限，并转向 Gemini 的统一费率与节流；还有人提到团队因用 AI 生成给监管机构的文件出错而被解雇。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers">Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders</a></li>
<li><a href="https://www.finalroundai.com/blog/goldman-sachs-claude-ai-agents">Goldman Sachs Deploys AI Agents for Accounting and Compliance...</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#enterprise security`, `#fintech`, `#AI governance`, `#Claude Code`

---

<a id="item-tech-news-4"></a>
### [Drex Max v1.1 据称达多模态决策模型 SOTA，公布训练论文与开放权重](https://www.reddit.com/r/MachineLearning/comments/1xr4hkm/artificial_analysis_multimodal_decision_model/) ⭐️ 7.0/10

Nace 团队在 Reddit 上宣布对 Drex Max v1.1 进行小幅更新，自称在多模态决策模型上同时达到 SOTA 和 Pareto 前沿。该团队称 Drex Max v1 权重已在 Hugging Face 以 Open RAIL-M 许可证开放，v1.1 开放权重将在优化本地推理后发布。Drex Max 的上下文窗口约为 256k，对比 Glide1.2 的 64k、Mammoth 的 16k 和 pplxdecider 的 256k，并称在 AA 指数中比同类下一最佳模型便宜 8 倍。团队还发布了训练论文《Towards Foundation Decision Models: Drex》，并提供了可在 Mac 上使用的 Kapitsa 推理引擎。该说法目前来自厂商自我宣传，缺少独立验证和详细基准数据。

reddit · r/MachineLearning · /u/m4rkGS · 11月8日 17:54

**「背景」** 决策模型（decision model）接收文本、JSON 或图像作为上下文/状态，并对一个或多个命名问题返回每个选项的概率，与生成式模型不同，它在一个前向传播中给出明确的选项概率（tool-1-2, tool-1-3）。Artificial Analysis 的 Decision Index 通过比较模型所选答案的置信度与实际准确率来评估校准，并跨多个基准等权汇总，是此类模型排名的常用指标（tool-1-1）。Nace AI 此前已开源 27B 参数的 Drex Max v1，采用 Open RAIL-M 许可证，支持本地推理（tool-1-2, tool-1-3）。

**「影响」** 对多模态决策模型的本地推理和开放权重用户而言，这意味着在 v1.1 权重发布后可能获得更便宜且上下文更长的候选模型，但其 SOTA 与 Pareto 前沿说法目前缺少独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-decision-index">Artificial Analysis Decision Index | Artificial Analysis</a></li>
<li><a href="https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/">Nace AI Open-Sources Drex Max v 1 : A 27B Decision Model That...</a></li>
<li><a href="https://huggingface.co/nace-ai/drex-max-v1">nace-ai/ drex - max - v 1 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#decision-models`, `#open-source`, `#benchmarks`, `#AI`

---

<a id="item-tech-news-5"></a>
### [苹果明年或让 Siri 更像智能体](https://9to5mac.com/2026/11/08/apple-working-on-agentic-siri-ai-next-year-report/) ⭐️ 7.0/10

彭博记者马克·古尔曼在 Power On 中称，Siri 已在 iOS 27 实现个性化，但仍缺少主动代为操作的能力；苹果可能最早在 2027 年让 Siri 向智能体方向转变。为支持这一转变，苹果也调整了内部开发流程：iOS 28 的首个开发周期不再使用四周编码加四周整合，而是改为六周编码探索加两周收敛，以给工程师更多创新时间。该消息由 9to5Mac 报道，显示苹果正逐步推动 Siri 从被动助手走向可替用户执行任务。

telegram · zaihuapd · 11月8日 16:36

**「背景」** 在 2026 年关于 iOS 27 的预览中，Siri 被描述为已经“完全重建”，并将通过扩展系统接入 Claude、Gemini 等第三方模型；但这些变化集中在个性化和系统级搜索，并不是智能体式主动操作。彭博记者 Mark Gurman 另报道，苹果为 iOS 28 等系统改变了开发节奏，把常规的四周编码与四周整合改为六周编码探索加两周收敛，以便给工程师更多时间实现智能体功能。

**「影响」** 对等待 Siri 智能体化的人来说，实际变化可能最早要到 2027 年才会落地；当前 iOS 27 中的个性化并不等于可主动代为操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/11/08/apple-tweaks-ios-28-development-process/">Apple Taking New Approach to Developing iOS 28 and... - MacRumors</a></li>
<li><a href="https://9to5mac.com/2026/05/12/ios-27s-completely-rebuilt-siri-will-include-a-new-system-wide-search-gesture-report/">iOS 27’s ‘completely rebuilt’ Siri will include a new... - 9to5Mac</a></li>
<li><a href="https://felloai.com/it/wwdc-2026-preview/">WWDC 2026 Preview: iOS 27, Siri 2.0 &amp; AI Plans</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri`, `#agentic AI`, `#iOS`, `#tech industry`

---