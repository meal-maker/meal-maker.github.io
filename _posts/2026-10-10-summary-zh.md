---
layout: default
title: "Horizon Summary: 2026-10-10 (ZH)"
date: 2026-10-10
lang: zh
---

> 从 42 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [Cloudflare 收购 Deno，运行时再维护一年](#item-tech-news-1) ⭐️ 8.0/10
2. [Telegram Desktop 一键窃取任意文件漏洞曝光](#item-tech-news-2) ⭐️ 8.0/10
3. [Carrier-Explode：解码 iPhone、Pixel 与 Galaxy 运营商设置](#item-tech-news-3) ⭐️ 7.0/10
4. [YouTuber 自建 Flock 式摄像头追踪警车后称警方上门](#item-tech-news-4) ⭐️ 7.0/10
5. [亚马逊建成第 1000 颗卫星，太空互联网服务数周内启动](#item-tech-news-5) ⭐️ 7.0/10
6. [JetBrains 发布开源编程模型 Mellum2.1](#item-tech-news-6) ⭐️ 7.0/10

**财经新闻**
1. [美股午盘异动：Starlink Mobile 冲击电信股，医保股受星级评级大幅波动](#item-finance-news-1) ⭐️ 7.0/10
2. [SpaceX 频谱交易、达美航空盈利不及预期等推动美股盘前异动](#item-finance-news-2) ⭐️ 7.0/10
3. [苹果被曝削减 iPhone 18 Pro 订单，盘前股价跌逾 1.6%](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Cloudflare 收购 Deno，运行时再维护一年](https://deno.com/blog/cloudflare) ⭐️ 8.0/10

Cloudflare 已收购 Deno，Deno 运行时将在接下来一年内继续获得每月发布，包含错误修复和安全更新。一年后，Cloudflare 将停止对该运行时的开发。Deno 仍保持开源，并欢迎其他开发者继续其开发。若无人接手，Deno 将不再获得官方支持。此次收购对 JavaScript/TypeScript 运行时生态具有重大影响。

hackernews · ilreb · 10月9日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=50019911)

**「背景」** Deno 是由 Node.js 创始人 Ryan Dahl 创建的 JavaScript 和 TypeScript 运行时，强调安全性和现代标准。Cloudflare 是一家主要的云服务和边缘计算公司，其 Workers 平台用于运行无服务器函数。Deno 团队还开发了 Celld，即 Cloudflare Workers 的自托管版本，这为此次收购提供了背景。

**「影响」** 依赖 Deno 的开发者和项目将在未来一年内继续获得安全与修复更新，但此后除非出现社区维护分支，否则将不再有官方支持。

**「社区讨论」** 社区普遍对停止开发表示遗憾，有开发者认为早期版本更简洁，后期因优先 npm 兼容而变得臃肿。另有评论称这更像是“acquihire”，并列举了 Cursor、Bun、Astro.js 等一系列开发者工具被收购整合的例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl/">Cloudflare acquires Node.js creator’s startup that... - The New Stack</a></li>

</ul>
</details>

**标签**: `#deno`, `#cloudflare`, `#javascript`, `#runtime`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [Telegram Desktop 一键窃取任意文件漏洞曝光](https://telegram.me/zaihuapd/44307) ⭐️ 8.0/10

Telegram Desktop 7.2.9 以下版本存在严重漏洞（CVE-2026-107181），用户点击恶意 tg:// 链接后，系统文件可在无确认的情况下被悄悄窃取。漏洞源于链接中的分号未转义、被当作独立 IPC 命令，配合 interpret: 处理器可盗取文档、浏览器会话、SSH 密钥、加密钱包等任意文件。官方已在 7.2.9 修复，建议尽快升级、警惕异常 tg:// 链接并启用本地密码。

telegram · zaihuapd · 10月9日 09:51

**「背景」** Telegram Desktop 支持通过 tg:// 自定义链接调用应用内操作，链接参数会被解析为内部命令。若参数中的分号未被正确转义，则可能被拆分为独立 IPC 命令，导致恶意指令注入。

**「影响」** 使用 7.2.9 以下版本 Telegram Desktop 的用户应立即升级，并在升级前避免点击来源不明的 tg:// 链接，以防文档、浏览器会话、SSH 密钥或加密钱包等文件被静默窃取。

**标签**: `#security`, `#telegram`, `#vulnerability`, `#desktop-applications`, `#CVE`

---

<a id="item-tech-news-3"></a>
### [Carrier-Explode：解码 iPhone、Pixel 与 Galaxy 运营商设置](https://carrierexplode.com/) ⭐️ 7.0/10

作者 simplyalec 在 Hacker News 展示了副项目 Carrier-Explode，该项目持续归档并解码 iPhone、Pixel 和 Galaxy 等主流手机的运营商设置。工具包含常见基带配置的解码器和说明，但作者表示仍有假设需要验证。该工具已在若干爱好者群体中被证明有用；社区评论提到它在 MacRumors 的 AT&amp;T iPhone 18 Pro Max 卡死问题讨论中被引用，显示 AT&amp;T/Apple 可能禁用了 5G Standalone 模式以避免硬件损坏。

hackernews · simplyalec · 10月9日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=50024499)

**「背景」** 运营商设置（carrier settings）是手机固件中由运营商控制的配置，包括 APN、VoLTE、Wi-Fi 通话和 5G 等选项，不同品牌和运营商的设置分散且不透明。Carrier-Explode 通过持续归档并解码 iPhone、Pixel 和 Galaxy 固件中的这些设置，使其可搜索、可对比，并提供免费 JSON API；其价值取决于解码准确性，且配置应被视为网络服务的证据而非实际服务证明。

**「实际影响」** 对于受影响的 AT&amp;T iPhone 18 Pro Max 用户，Carrier-Explode 揭示出运营商设置更新（如禁用 5G Standalone）旨在缓解设备锁死问题，这与 Apple 建议安装 iOS 27.0.1 及运营商设置更新可预防该问题的指导一致。

**「社区讨论」** 社区反馈总体正面，有用户称赞其展示了非美国运营商的设置，并有人提到在 AT&amp;T iPhone 18 Pro Max 卡死事件中观察到 5G Standalone 被禁用。讨论中还提出了个人热点被运营商禁用、向 GNOME 项目贡献相关数据，以及该工具收集信息的实际用途等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://carrierexplode.com/">iPhone, Pixel and Galaxy carrier settings, decoded · carrier ...</a></li>
<li><a href="https://runtimewire.com/article/carrier-explode-alec-dusheck-carrier-settings">carrier-explode makes phone firmware searchable for carrier ...</a></li>
<li><a href="https://github.com/AlecDusheck/carrier-explode?ref=runtimewire">GitHub - AlecDusheck/carrier-explode at runtimewire</a></li>
<li><a href="https://support.apple.com/en-us/109324">Manually update carrier settings on your iPhone or iPad How to Update AT&amp;T Carrier Settings on iPhone 18 Pro Max ... Enable 5G Standalone on iPhone: Toggle &amp; Fixes - unanswered.io iPhone 18 Pro Max AT&amp;T Users: Update to iOS 27.0.1 and New ... Apple iPhone 18 Pro Max - Checking if your phone is carrier ...</a></li>

</ul>
</details>

**标签**: `#mobile`, `#carrier-settings`, `#reverse-engineering`, `#baseband`, `#tooling`

---

<a id="item-tech-news-4"></a>
### [YouTuber 自建 Flock 式摄像头追踪警车后称警方上门](https://gizmodo.com/youtuber-says-cops-paid-him-a-visit-after-he-built-flock-style-camera-to-track-cops-2000824306) ⭐️ 7.0/10

一名 YouTuber 建造了类似 Flock 的自动车牌识别摄像头来追踪警车，并表示事后有警察上门探访。该事件引发关于监控、隐私及自动车牌识别系统合法性的讨论。社区评论中有人引用新罕布什尔州法律，要求对非命中车牌图像在三分钟内删除、禁止将非命中图像上传至设备外，并认为这是可借鉴的起点。也有评论指出，将追踪警车并公开信息与执法机构可搜索的 Flock 数据并不等同，主张要么禁止包括政府在内的所有此类收集，要么通过立法严格限制数据搜索权限和审批要求。

hackernews · gumby · 10月9日 21:06 · [社区讨论](https://news.ycombinator.com/item?id=50026555)

**「背景」** Flock Safety 等公司销售的自动车牌识别（ALPR）摄像头通常由执法部门或社区安装，用于记录过往车辆车牌并建立可搜索数据库。此次事件中，YouTuber 自制了类似 Flock 的摄像头来记录警车车牌，引发关于“反向监控”是否合法、以及 ALPR 数据应如何限制的讨论。美国部分州（如新罕布什尔州）已立法限制 ALPR 收集非命中数据，但各地规定不一。

**「影响」** 该事件表明公民自建 ALPR 追踪系统可能引来警方接触，但报道未确认是否涉及指控或法律后果。

**「社区讨论」** 评论中存在分歧：一方支持以新罕布什尔州法律为模板约束 ALPR 数据保留，另一方认为应全面禁止或严格立法；还有评论提议建立 OpenFlock 公开追踪投票支持 Flock 摄像头的市议员，以形成对等透明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50026555">YouTuber Says Cops Visited Him After He Built a Flock - Style ...</a></li>
<li><a href="https://cybernews.com/privacy/youtuber-flock-surveillance-police/">YouTuber tracks cops with Flock - Style camera | Cybernews</a></li>
<li><a href="https://san.com/cc/he-built-his-own-flock-style-camera-to-track-police-the-police-didnt-like-it/">He built his own Flock - style camera to track police. The police...</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#ALPR`, `#law enforcement`, `#technology policy`

---

<a id="item-tech-news-5"></a>
### [亚马逊建成第 1000 颗卫星，太空互联网服务数周内启动](https://arstechnica.com/space/2026/10/amazon-builds-1000th-satellite-is-weeks-away-from-space-internet-rollout/) ⭐️ 7.0/10

亚马逊已在华盛顿州柯克兰工厂制造出第 1000 颗卫星，其 Amazon Leo 低轨卫星互联网项目距启动商业服务仅数周。这些卫星将搭乘 Vulcan 火箭执行即将到来的复飞任务，另一枚 Vulcan 也准备在 2026 年发射更多卫星。这一里程碑意味着亚马逊有望在年底前推出太空互联网服务。

telegram · zaihuapd · 10月9日 04:30

**「背景」** Amazon Leo 此前名为 Project Kuiper，是亚马逊的低轨卫星互联网项目，与 SpaceX 的 Starlink 等系统直接竞争。根据发射跟踪数据，截至 2026 年 4 月该项目已通过 11 次发射将 231 颗卫星送入轨道，并计划在 2026 年执行 20 余次发射、2027 年执行 30 余次发射；商业服务原定于 2026 年年中启动。

**「影响」** 对于卫星宽带用户，亚马逊 Project Kuiper 的第 1000 颗卫星和数周内启动商业服务的计划，将引入一个与 SpaceX Starlink 直接竞争的选项，比较焦点包括速度、延迟、价格、覆盖范围和发射进度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orbitalradar.com/satellite-internet/kuiper-launch-schedule">Amazon Kuiper Launch Schedule 2026 — Next Missions</a></li>
<li><a href="https://keeptrack.space/deep-dive/amazon-leo-progress-2026">Amazon Leo Satellites in Orbit, Timeline and Service Date ...</a></li>
<li><a href="https://thenextweb.com/news/amazon-leo-satellite-internet-mid-2026">Amazon Leo targets mid-2026 commercial launch as ... - TNW</a></li>
<li><a href="https://orbitalradar.com/satellite-internet/starlink-vs-kuiper">Starlink vs Amazon Kuiper: Speed, Price &amp; Coverage 2026</a></li>
<li><a href="https://satspeedcheck.com/blog/project-kuiper-vs-starlink/">Project Kuiper vs Starlink: Amazon&#x27;s Satellite Internet ...</a></li>

</ul>
</details>

**标签**: `#satellite-internet`, `#amazon`, `#leo-satellites`, `#broadband`, `#tech-industry`

---

<a id="item-tech-news-6"></a>
### [JetBrains 发布开源编程模型 Mellum2.1](https://blog.jetbrains.com/ai/2026/10/mellum2-1-gets-to-work-a-fast-open-model-for-coding-agents/) ⭐️ 7.0/10

JetBrains 推出了开源编程模型 Mellum2.1，采用 12B 参数的混合专家（MoE）架构，每次推理仅激活 2.5B 参数，并以 Apache 2.0 许可证发布。该模型经过真实环境强化学习训练，能够探索代码库、编辑文件并检查修改，面向本地运行的编程代理场景。模型权重已发布在 Hugging Face 上，使开发者可以在本地构建具备代码探索、编辑和验证能力的编程代理。

telegram · zaihuapd · 10月9日 07:30

**「背景」** 混合专家（MoE）架构通过每次只激活部分参数，在保持模型容量的同时降低推理计算量，更适合本地部署。真实环境强化学习让模型直接与代码库、文件编辑和自检等实际任务交互，而不是仅从静态文本中学习。Apache 2.0 许可证允许商业使用、修改和再分发。

**「影响」** 本地编程代理开发者现在可以从 Hugging Face 获取 Mellum2.1 权重，并在 Apache 2.0 下将其集成到自己的工具中，获得代码库探索、文件编辑和修改检查能力。

**标签**: `#open-source`, `#coding-agents`, `#large-language-model`, `#JetBrains`, `#AI`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美股午盘异动：Starlink Mobile 冲击电信股，医保股受星级评级大幅波动](https://www.cnbc.com/2026/10/09/stocks-making-the-biggest-moves-midday-tmus-vz-t-cci-teva.html) ⭐️ 7.0/10

SpaceX 加强 Starlink Mobile 服务后，电信股集体下跌：T-Mobile 跌 13%，AT&amp;T 和 Verizon 各跌 10%；蜂窝塔公司上涨，Crown Castle 涨 12%。美国联邦医保 2027 年星级评级公布后，Humana 涨 12%，Alignment Healthcare 跌近 14%。

rss · CNBC Finance · 10月9日 18:57

**「背景」** Starlink Mobile 是 SpaceX 的卫星直连手机服务；CMS 星级评级是美国联邦医疗保险优势计划的质量评分，影响保险公司参保和收入。

**标签**: `#stocks`, `#telecom`, `#health insurers`, `#earnings`, `#FDA approval`

---

<a id="item-finance-news-2"></a>
### [SpaceX 频谱交易、达美航空盈利不及预期等推动美股盘前异动](https://www.cnbc.com/2026/10/09/stocks-making-the-biggest-moves-premarket-dal-spcx-tmus.html) ⭐️ 7.0/10

SpaceX 宣布与 Grain Management 达成 800 MHz 频谱组合出售协议，其股价盘前上涨 4%，推动 T-Mobile、AT&amp;T、Verizon 分别下跌约 7%、6% 和 5%，American Tower 与 Crown Castle 上涨 6% 和近 8%。达美航空第三季度调整后每股收益 1.72 美元、营收 175.9 亿美元，低于 LSEG 分析师预期的 1.75 美元和 176.7 亿美元，股价下跌 4%；CMS 2027 星评级更新使 Humana 上涨 14%、Alignment Healthcare 下跌 23%。

rss · CNBC Finance · 10月9日 12:31

**「背景」** 此前，AI 概念股因 OpenAI 年化营收约低 200 亿美元的报道在周四下跌；CMS 星评级在 Medicare Plan Finder 上公布，用于秋季开放注册期比较 Medicare Advantage 计划。

**标签**: `#premarket movers`, `#telecom spectrum`, `#earnings`, `#Medicare Star Ratings`, `#stock market`

---

<a id="item-finance-news-3"></a>
### [苹果被曝削减 iPhone 18 Pro 订单，盘前股价跌逾 1.6%](https://www.forbes.com/sites/siladityaray/2026/10/09/apple-shares-dip-after-report-says-its-cutting-iphone-18-pro-component-orders/) ⭐️ 7.0/10

据报道，因 iPhone 18 Pro 与 Pro Max 需求弱于预期，苹果本月已将这两款机型的零部件订单至少削减 15%；消息传出后，苹果股价盘前下跌逾 1.6%。

telegram · zaihuapd · 10月9日 13:31

**「背景」** iPhone 18 Pro 上月发布，起售价 1199 美元，较上代上涨 100 美元；标准版 iPhone 18 被推迟到明年初发布，折叠屏 iPhone Duo 定于 10 月 23 日发售，尚不清楚其订单是否受影响。

**标签**: `#Apple`, `#iPhone`, `#supply chain`, `#demand`, `#stock market`

---