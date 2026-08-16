---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 32 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [Anthropic 公开 Claude 系统提示](#item-tech-news-1) ⭐️ 7.0/10
2. [Cloudflare 切换域名服务器后静默注入分析 JS](#item-tech-news-2) ⭐️ 7.0/10
3. [Qwen 3.8 27B 模型优秀但默认过度思考](#item-tech-news-3) ⭐️ 7.0/10
4. [PJM 电网建模错误浪费 120 亿美元且可能重蹈覆辙](#item-tech-news-4) ⭐️ 7.0/10
5. [重新审视 ECA 论文：核心假设不成立](#item-tech-news-5) ⭐️ 7.0/10
6. [美国据报要求盟友在 AI 合作中选边](#item-tech-news-6) ⭐️ 7.0/10
7. [Claude 大规模故障：多服务无法登录或加载](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [Anthropic 第二季初步营收超 115 亿美元，同比增逾 14 倍](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Anthropic 公开 Claude 系统提示](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 7.0/10

Anthropic 已在官方文档平台发布 Claude 模型的系统提示，使开发者能够直接查看模型的内部指令与行为设定。社区讨论中提到了系统提示中的具体内容，例如模型会自行检查图像是否存在，以及在用户处于危机时优先关注其福祉。此外，Simon Willison 在 GitHub 上维护了系统提示的提交历史，并对比了 Opus 4.8 与 Opus 5 的差异，其中新增内容涉及 Claude Fable 5 和 Claude Mythos 5 的发布说明。这些公开信息有助于开发者更精确地理解和控制 Claude 模型的行为。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**「背景」** 系统提示（system prompt）是指在 Claude 对话开始时预置的指令，用于提供当前日期等最新信息并引导模型行为。Anthropic 已在官方文档中公布 claude.ai 以及 iOS 和 Android 应用核心系统提示的更新记录（截至 2026 年 6 月 9 日），方便开发者跟踪模型行为约束的变化。

**「影响」** 开发者现在可以直接查阅 Claude 的系统提示，从而更精确地进行提示词工程、调试模型行为，并追踪不同版本间的指令变更。不过，系统提示只是塑造模型行为的多层机制之一，实际响应还受其他因素影响。

**「社区讨论」** 评论区中，Simon Willison 分享了在 GitHub 上跟踪系统提示版本历史的项目，并指出 Opus 4.8 与 Opus 5 之间的新增内容涉及 Claude Fable 5 和 Claude Mythos 5。其他用户讨论了提示的具体规定，例如模型会自行检查图像是否存在以及危机情境下的优先级处理；另有人对论坛移除 AI 负面报道表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#System Prompts`, `#Prompt Engineering`

---

<a id="item-tech-news-2"></a>
### [Cloudflare 切换域名服务器后静默注入分析 JS](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

用户 stagas 报告，几小时前将域名服务器切换到 Cloudflare 以便通过自有子域名提供 R2 存储桶服务后，发现 Cloudflare 悄悄向他的纯 HTML、无 JS 网站 textlog.cc 注入了分析 JavaScript 片段。注入的脚本是 Cloudflare Web Analytics 的 beacon.min.js（来自 static.cloudflareinsights.com），发生在启用 Cloudflare 代理并让其终止 HTTPS 连接的情况下。用户必须进入 Analytics 仪表板，先添加站点到 analytics，然后才能禁用该片段，这被批评为应默认不启用（opt-in）而非要求用户选择退出（opt-out）。帖子向可能不知情的用户发出隐私和信任方面的警告。

hackernews · stagas · 8月16日 17:49

**「背景：Cloudflare 代理与 Web Analytics 自动注入」** Cloudflare 的域名接入分为“仅 DNS”和“代理（橙色云）”两种：仅 DNS 不经过 Cloudflare 服务器，代理则由 Cloudflare 转发流量。Cloudflare Web Analytics 的自动 JavaScript 注入仅在流量经过 Cloudflare 代理时发生；官方文档明确，DNS-only 域名不能使用自动注入，只能手动部署。因此用户看到被注入脚本，通常是因为域名的云朵被开启为代理状态。

**「影响」** 对于使用 Cloudflare 代理（而不仅是 DNS）的站长，如未主动关闭 Web Analytics，其站点会被注入 beacon.min.js 分析脚本，需要到 Analytics 仪表板中禁用或通过内容安全策略（CSP）限制脚本来阻止。

**「社区讨论」** 评论者确认启用 Cloudflare 代理时会出现 beacon.min.js 注入（有人贴出 version 2024.11.0 的脚本），并指出仅使用 DNS-only 的域名未出现 Web Analytics 启用。建议包括通过 CSP 的 script-src &\#x27;self&\#x27; 限制脚本来源，或仅使用 DNS 模式来避免注入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/web-analytics/faq/">FAQs · Cloudflare Web Analytics docs</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#privacy`, `#web-analytics`, `#javascript`, `#dns`

---

<a id="item-tech-news-3"></a>
### [Qwen 3.8 27B 模型优秀但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

阿里巴巴 Qwen 实验室发布了 Qwen 3.8 27B，一个采用 Apache 2.0 许可证、具备视觉能力的 27B 参数大语言模型，其自我报告基准超过上一代 Qwen 3.6 27B 以及闭源 Qwen 3.7-Plus。西蒙·威利森在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上通过 LM Studio 运行其 17GB Q4\_K\_M 量化版本，发现默认 reasoning\_effort 为 xhigh 会导致严重过度思考。例如让模型生成“骑自行车的鹈鹕” SVG 时，默认设置耗时 21 分钟，使用 22,276 个推理 token 才生成 3,223 个输出 token；关闭推理后同一提示仅用 137 秒并生成 3,715 个 token。更简单的“画一个圆形的 SVG”请求也被默认设置演绎成几分钟后生成的复杂动画圆，而非用户要求的简单图形。他建议用户忽略默认设置，先以低推理级别甚至完全关闭推理来运行该模型。

rss · Simon Willison · 8月16日 22:00

**「背景」** Qwen 3.8 文档称该模型支持 reasoning\_effort 参数，提供 xhigh（默认，用于复杂任务）、medium（平衡准确与速度）和 low（高效推理）三档。27B 参数规模适合在配置较好的本地计算机上运行，前代 Qwen 3.6 27B 给人留下深刻印象。西蒙·威利森此前发布的博客回顾了 Qwen 3.6 27B 的表现。

**「影响」** 对于希望在本地消费级硬件上运行 Qwen 3.8 27B 的用户，保留默认 xhigh 设置会导致数倍甚至数十倍的生成延迟和大量无用推理 token，因此必须手动将 reasoning\_effort 调低或关闭推理才能获得可用的响应速度。

**标签**: `#Qwen 3.8 27B`, `#LLM`, `#open source`, `#AI benchmarks`, `#model release`

---

<a id="item-tech-news-4"></a>
### [PJM 电网建模错误浪费 120 亿美元且可能重蹈覆辙](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

PJM 的电网建模错误浪费了美国纳税人的 120 亿美元。该组织可能会再次犯下同样的错误，从而给能源基础设施带来风险。SemiAnalysis 文章称，美国最强大的电网因使用“糟糕的模型”而浪费了数十亿美元，并正将纳税人置于风险之中。

rss · Semianalysis · 8月16日 22:27

**「背景：PJM 容量市场与 2024 年模型争议」** PJM Interconnection 是美国一个区域性输电组织，负责协调多个州的批发电力市场，其中包括通过拍卖确保未来发电容量的容量市场。2024 年，PJM 在容量市场建模中采用了不恰当的电力供应假设，导致拍卖成本异常上升，使消费者额外承担了约 120 亿美元费用；相关投诉要求纠正规则以防止这一错误重演。

**「对 PJM 用户的影响」** PJM 电网覆盖的 6700 万美国用户已因错误建模承担了约 120 亿美元的浪费性成本，若 PJM 再次采用类似模型，这些用户可能继续面临重复的财务损失和电网基础设施风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.zerohedge.com/energy/most-two-thirds-power-sought-us-data-centers-will-never-materialize">More Than Two-Thirds Of The Power Sought For US Data Centers ...</a></li>

</ul>
</details>

**标签**: `#energy grid`, `#electricity markets`, `#modeling`, `#PJM`, `#infrastructure`

---

<a id="item-tech-news-5"></a>
### [重新审视 ECA 论文：核心假设不成立](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

Reddit 用户 /u/arkuto 发布了一篇技术分析，重新审视 2019 年提出、已有约 1.2 万次引用的 Efficient Channel Attention（ECA）论文，认为其用 1D 卷积在通道均值上滑动缺乏有效的拓扑基础。作者改用国际象棋 6 子残局库数据（可完整随机采样）进行实验，结果显示 IdentityGate 测试损失/准确率为 0.0981/96.04%，SE8 为 0.0954/96.17%，ECA k=3 为 0.0822/96.68%，ECA k=1 为 0.0826/96.61%，CenterMasked \[1,0,1\] 为 0.0821/96.63%，PerChannelGate 为 0.0815/96.65%。其中 k=1 没有跨通道交互却仍优于 SE 并接近 k=3，动摇了论文“跨通道交互是关键”的核心假设；\[1,0,1\] 掩码的结果又表明跨通道注意力可能在某些情况下有用，作者称尚无完整解释。此外，多个复现仓库（包括官方仓库）未对纯 k=1 做独立消融，官方 MobileNetV2 仅在通道数小于 96 时使用 k=1。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**「背景」** ECA 是卷积神经网络中的一种通道注意力机制，作为 SE（Squeeze-and-Excitation）的改进方案：SE 将全局平均池化后的通道描述压缩到较小隐藏层再还原，ECA 则直接用 1D 卷积在通道均值上建模局部跨通道交互。卷积原本依赖有序拓扑假设（局部性和平移不变性），而通道索引通常没有这样的自然顺序，这正是该分析质疑 ECA 设计的出发点。

**「影响」** 在该作者的国际象棋残局基准上，ECA k=1 与 k=3 表现接近且都优于 SE，说明至少在这一任务中跨通道交互并非 ECA 改进的必要条件，研究者和开发者在采用 ECA 时应谨慎对待其原始机理解释。不过 \[1,0,1\] 掩码的结果提示跨通道信息可能仍起作用，结论尚未完全确定。

**标签**: `#machine learning`, `#attention mechanism`, `#computer vision`, `#convolutional neural networks`, `#research critique`

---

<a id="item-tech-news-6"></a>
### [美国据报要求盟友在 AI 合作中选边](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 7.0/10

美国据报要求盟友及希望与华盛顿开展 AI 合作的国家选边，否则可能被排除在美国主导的 AI 联盟之外。据称美国国务院准备的信函草案写道，签署 Pax Silica 宣言不仅是加入该联盟，还意味着不能同时加入预期相冲突的重复倡议。目前报道基于一份据称的草案信函，细节尚未得到官方确认。

telegram · zaihuapd · 8月16日 02:30

**「背景：Pax Silica 是什么」** Pax Silica 是美国主导的国际倡议，重点保障半导体、人工智能和稀土等先进技术供应链安全，也是美国国务院在人工智能与供应链安全领域的旗舰行动。美国已宣布该宣言，签约方包括澳大利亚、英国等盟友，新加坡是唯一的东南亚签约国。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>
<li><a href="https://www.indexbox.io/blog/pax-silica-declaration-us-forges-ai-alliance-with-key-allies-singapore-as-sole-southeast-asian-signatory/">Pax Silica Declaration : U . S . AI Pact with Allies ... - IndexBox</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#US-China relations`, `#Pax Silica`, `#AI governance`, `#international cooperation`

---

<a id="item-tech-news-7"></a>
### [Claude 大规模故障：多服务无法登录或加载](https://www.ithome.com/0/990/404.htm) ⭐️ 7.0/10

8 月 17 日，Anthropic Claude 出现大规模服务故障，影响 Claude.ai、Claude Code 和 Claude Cowork。故障约于北京时间 5:58 开始，用户可能遇到无法登录、页面无法加载或请求无法完成等错误。Anthropic 状态页已将上述服务标记为“大规模服务故障”，但 Claude Console 和 Claude API 仍运行正常。具体原因尚未公布，仍在调查中。

telegram · zaihuapd · 8月16日 22:49

**「背景」** Claude 是 Anthropic 推出的生成式 AI 产品系列；Claude.ai 提供对话式网页服务，Claude Code 面向开发者辅助编程，Claude Cowork 用于团队协作。这些服务通常依赖 Anthropic 云端基础设施，因此单次故障可能同时影响多个前端入口。

**「影响」** 对使用 Claude.ai、Claude Code 和 Claude Cowork 的用户和开发者而言，本次故障从北京时间 8 月 17 日 5:58 起造成登录、页面加载和请求完成受阻，工作流可能中断；Claude Console 和 Claude API 调用则不受影响。

**标签**: `#Anthropic`, `#Claude`, `#outage`, `#AI services`, `#incident`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 第二季初步营收超 115 亿美元，同比增逾 14 倍](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

据彭博社援引文件报道，Anthropic 第二季初步营收超过 115 亿美元，同比增长逾 14 倍，高于去年同期的 7.87 亿美元和 2026 年第一季的 47.3 亿美元；当季调整后营业利润转正，数字为初步数据，仍可能调整。

telegram · zaihuapd · 8月16日 07:26

**「背景」** 该初步营收数字由彭博社援引文件报道，高于去年同期的 7.87 亿美元和 2026 年第一季的 47.3 亿美元，且仍可能调整；公司正筹备可能在今秋启动的大型 IPO。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.whatjobs.com/news/anthropic-preliminary-q2-revenue-tops-11-5-billion/">Anthropic Preliminary Q 2 Revenue Tops $ 11 . 5 Billion</a></li>
<li><a href="https://thenextweb.com/news/anthropic-q2-2026-revenue-11-5-billion-operating-income">Anthropic ’s quarterly revenue passed $ 11 . 5 bn, up more than 14-fold</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#tech industry`

---