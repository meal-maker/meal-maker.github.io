---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
lang: zh
---

> 从 47 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [OpenAI 开发者大会发布 Dots 智能体及 20 余项更新](#item-tech-news-1) ⭐️ 9.0/10
2. [对网页与移动端对话式 AI 助手的隐私分析](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI 推出 Dots：常驻代理引发平台锁定担忧](#item-tech-news-3) ⭐️ 8.0/10
4. [Anthropic Frontier Red Team：GLM-5.3 与 Claude Mythos Preview 实现控制流劫持](#item-tech-news-4) ⭐️ 8.0/10
5. [Cloudflare 推出面向 AI Agent 的 cf CLI 开放测试版](#item-tech-news-5) ⭐️ 8.0/10
6. [Anthropic 评估 GLM-5.3 自主网络攻击能力](#item-tech-news-6) ⭐️ 8.0/10
7. [GPT 6.1 Sol：以五分之一价格实现接近 Astra 的智能](#item-tech-news-7) ⭐️ 7.0/10
8. [美国政府推出基于 Gemini 的公共服务门户 America.gov](#item-tech-news-8) ⭐️ 7.0/10
9. [PS5 Relapse 漏洞利用公开](#item-tech-news-9) ⭐️ 7.0/10
10. [GPT 6.1 Sol：近 Astra 智能，价格五分之一](#item-tech-news-10) ⭐️ 7.0/10
11. [免费开源书：从芯片到智能体的模型加速系统指南](#item-tech-news-11) ⭐️ 7.0/10
12. [CoWindow 与 MassAlloc：减少长上下文注意力冗余计算](#item-tech-news-12) ⭐️ 7.0/10
13. [据报 OpenAI 发布 GPT-6.1 Sol，价格仅为 Astra 五分之一](#item-tech-news-13) ⭐️ 7.0/10

**财经新闻**
1. [三部门：10 月 1 日起首套房贷贴息 1 个百分点，最长 5 年、单户贷款上限 100 万元](#item-finance-news-1) ⭐️ 9.0/10
2. [美股盘前：Fair Isaac 大跌 18%，CarMax 业绩超预期](#item-finance-news-2) ⭐️ 7.0/10
3. [中国证监会据报对人形机器人 IPO 设三项新标准](#item-finance-news-3) ⭐️ 7.0/10
4. [星际之门数据中心因电力审批延期 甲骨文发不可抗力通知](#item-finance-news-4) ⭐️ 7.0/10
5. [苹果新 CEO 特努斯推动公司提速与精简](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 开发者大会发布 Dots 智能体及 20 余项更新](https://openai.com/zh-Hant/index/devday-2026-recap/) ⭐️ 9.0/10

OpenAI 在 2026 开发者大会上发布了 20 余项更新，包括可全天候自主运转的常驻智能体 Dots、GPT-6.1 Sol 与 Astra Ultrafast 模型、Codex 云端版、Agents API、Decisions API 以及“Sign in with ChatGPT”账号互通。GPT-6.1 Sol 专精编程和电脑操控，以五分之一的价格获得接近 Astra 的智能水平；Astra Ultrafast 速度最高提升 8 倍（API 提升 6 倍）。Codex 支持语音操控与自动修障，Agents API 原生开放电脑操控和 AWS Bedrock 托管，Decisions API 提供基于 Luna 模型的轻量实时决策接口。此外，新 Pro 500 档位算力额度为 Plus 的 25 倍，专享 Astra Ultrafast。

telegram · zaihuapd · 9月29日 17:52

**「背景」** OpenAI DevDay 是面向开发者的年度会议，用于发布模型、API 和平台能力更新。Dots 属于常驻智能体，可长期运行并学习用户习惯；GPT-6.1 Sol 与 Astra 是 OpenAI 的模型系列，其中 Astra 代表较高智能水平，Sol 为编程与电脑操控优化，Ultrafast 强调延迟与吞吐优化。

**「影响」** 开发者可以更低的成本（GPT-6.1 Sol 为 Astra 价格的五分之一）和更高的速度（Astra Ultrafast 最高 8 倍）构建自主智能体和编程工具，同时 Pro 500 档位为重度用户提供 Plus 25 倍算力。

**标签**: `#OpenAI`, `#AI agents`, `#GPT-6.1`, `#developer tools`, `#APIs`

---

<a id="item-tech-news-2"></a>
### [对网页与移动端对话式 AI 助手的隐私分析](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-%28clean%29.pdf) ⭐️ 8.0/10

《网页与移动端对话式 AI 助手的隐私分析》是一篇技术论文，考察了网络和移动平台上的对话式 AI 代理如何通过平台特定的跟踪机制和权限收集并可能泄露用户敏感数据。论文比较了网页与移动端实现之间的差异，并提供了具体的技术发现，表明这些代理在隐私与安全方面存在风险。该分析聚焦于隐私、AI、网页与移动安全主题，并以 PDF 形式发布。

hackernews · damaru2 · 9月29日 09:03 · [社区讨论](https://news.ycombinator.com/item?id=49890226)

**「背景」** 对话式 AI 代理是一类具有用户界面、服务端逻辑和数据库支持的系统，可处理自然语言交互（tool-1-1）。这类代理在 Web、桌面和移动端部署时，用户偏好和会话状态往往跨平台同步，例如 Mattermost 的 AI 代理选择会同步到各端（tool-1-2）。因此，分析其隐私时需区分代理自身的数据处理与不同平台提供的 API 和权限机制。

**「影响」** 该分析提醒用户，在使用网页或移动端对话式 AI 时，其未完成的输入、对话链接及敏感数据可能被平台追踪或通过 URL 暴露，因此改用本地运行的开源模型可降低此类隐私风险。

**「社区讨论」** 社区讨论中，多位用户报告了实际观测到的隐私问题：ChatGPT 会向 conversation/prepare 端点定期发送未完成的提示，Perplexity 的过往搜索链接可暴露完整对话。讨论普遍认为此类提示与结果不应被默认视为私密，并倾向于支持本地运行开源模型以避免跟踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/337925917_Conversational_AI_Social_and_Ethical_Considerations">( PDF ) Conversational AI : Social and Ethical Considerations</a></li>
<li><a href="https://docs.mattermost.com/end-user-guide/agents">AI Agents | Mattermost Documentation</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI`, `#web`, `#mobile`, `#security`

---

<a id="item-tech-news-3"></a>
### [OpenAI 推出 Dots：常驻代理引发平台锁定担忧](https://openai.com/index/introducing-dots/) ⭐️ 8.0/10

OpenAI 已推出 Dots，这是一款“always-on agents”（常驻代理）产品，定位为持续运行并代表用户执行任务的云端智能体。根据 Hacker News 讨论，Dots 的常驻特性意味着它会深度集成其他平台、保留工作历史，并在云端充当用户的“电脑”，从而可能增加用户迁移到其他代理的难度。社区同时指出，Dots 与 Codex、ChatGPT Work 以及 Meta 的 Muse 等产品在功能上出现重叠，产品边界变得模糊。有评论认为，这类常驻代理主要面向非技术用户和未来的 AI 原生一代，可能加速个人计算向云端迁移。但截至目前，该产品在能力、定价或兼容性方面的详细技术信息仍不明确。

hackernews · alvis · 9月29日 17:07 · [社区讨论](https://news.ycombinator.com/item?id=49896604)

**「背景」** Dots 是 OpenAI 在 2026 年 9 月 29 日的 DevDay 2026 活动上发布的“始终在线代理”，可根据用户需求定制并持续处理任务。这一发布发生在 Meta 的 Muse 头像代理引发广泛关注之后，被视为 OpenAI 对同类代理的回应。它反映了行业从一次性问答模型向长期运行、云端自主执行代理的转向。

**「社区讨论」** Hacker News 评论普遍对平台锁定表示担忧，认为与可替换的模型不同，常驻代理因集成、工作历史和云环境而更难切换。也有用户质疑 Codex、ChatGPT Work 与 Dots 的定位重叠，并认为 Meta 的 Muse 可能在大众市场更占优势，而 Dots 的定位尚不清晰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots - OpenAI</a></li>
<li><a href="https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/">OpenAI’s Dots Are Always-On AI Agents—and Its Answer to Meta ...</a></li>
<li><a href="https://9to5google.com/2026/09/29/openai-dots-agent/">OpenAI Dots are &#x27;always-on agents&#x27; that can do tasks for you</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#OpenAI`, `#automation`, `#software engineering`, `#platform lock-in`

---

<a id="item-tech-news-4"></a>
### [Anthropic Frontier Red Team：GLM-5.3 与 Claude Mythos Preview 实现控制流劫持](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/) ⭐️ 8.0/10

Anthropic Frontier Red Team 在随机选取的 100 个内部二进制利用基准任务上测试多个模型，发现 GLM-5.3 在 4%的试验中实现完整控制流劫持，Claude Mythos Preview 为 6%。虽然 GLM-5.3 的成功率低于 Claude Mythos Preview，但明确跨过了能力门槛：Claude Opus 4.6 和 GLM-5.2 等早期模型在这些任务上均未成功。

rss · Simon Willison · 9月29日 22:20

**「背景：内部二进制利用基准与能力门槛」** Anthropic Frontier Red Team 的内部 Binary Exploitation 基准测试从 Google OSS-Fuzz 项目中的开源软件随机选取 100 个任务，以“实现完整控制流劫持”作为成功标准，用于评估模型发现并利用真实漏洞的能力。此前的 Claude Opus 4.6 和 GLM-5.2 在该任务上成功率为 0%，因此 GLM-5.3 的 4% 与 Claude Mythos Preview 的 6% 被视为首次跨过该能力门槛。

**「影响」** 前沿模型已具备在部分二进制漏洞利用任务中实际完成控制流劫持的能力，可能改变漏洞研究与防御的威胁模型。但成功率仍低（4%和 6%），且限于随机抽取的内部基准任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/">A quote from Anthropic Frontier Red Team | Simon Willison’s Weblog</a></li>
<li><a href="https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities">GLM - 5 . 3 and the spread of advanced cyber capabilities \ Anthropic</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#generative-ai`, `#binary-exploitation`, `#anthropic`, `#cyber-capabilities`

---

<a id="item-tech-news-5"></a>
### [Cloudflare 推出面向 AI Agent 的 cf CLI 开放测试版](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 8.0/10

Cloudflare 已发布 cf CLI 的开放测试版，该工具由 Cloudflare API Schema 生成，可供开发者和 AI Agent 在命令行中发现并执行超过 3,000 项 API 操作；相比之下，现有 Wrangler 仅覆盖约 280 种操作。cf 默认输出 JSON，并支持命令搜索与引导，便于 Agent 自动发现、执行操作并处理结果。Cloudflare 示例显示，Agent 可通过同一工具创建和部署 Worker、监控服务、配置 Access 与 WAF，甚至购买域名。这一变化使 AI Agent 可调用的 Cloudflare 操作从约 280 项扩展到超过 3,000 项。

telegram · zaihuapd · 9月29日 13:46

**「背景」** Cloudflare 现有的 Wrangler CLI 主要面向 Workers 开发，覆盖约 280 种操作；新的 cf CLI 由 Cloudflare 的 OpenAPI Schema 通过内部 SDK 生成器 Forge 自动生成，因而能够覆盖超过 3,000 项 API 操作。cf 默认以 JSON 输出，并支持命令搜索、引导以及 TypeScript 配置，这使其不仅适合开发者手动使用，也便于 AI Agent 自动发现和执行操作。

**「影响」** 对于需要将 Cloudflare 基础设施管理接入 AI Agent 的开发者，cf CLI 可减少为有限 Wrangler 命令编写自定义封装的工作，并支持更多自动化部署、监控与配置场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/cloudflare-cf-cli-launch/">Introducing cf: the agentic CLI for the entire Cloudflare API</a></li>
<li><a href="https://creuto.com/cloudflare-cf-cli-3000-api-operations-agents">Cloudflare cf CLI: 3,000 API operations built for agents</a></li>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-09-28-cloudflare-cli-beta/">Cloudflare CLI is now in beta · Changelog</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#cli`, `#ai-agents`, `#developer-tools`, `#api`

---

<a id="item-tech-news-6"></a>
### [Anthropic 评估 GLM-5.3 自主网络攻击能力](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) ⭐️ 8.0/10

Anthropic 对智谱 AI（Z.ai）的 GLM-5.3 模型评估显示，该模型已具备自主构建端到端网络攻击的能力。在 ExploitBench 测试中，GLM-5.3 在 410 次尝试中成功 50 次，接近 Claude Mythos Preview 的 56 次成功。评估还发现，GLM-5.3 的安全防护可被简单方法绕过，模拟测试成功率为 64% 至 100%；开放权重使用户能改造模型以削弱拒答。Anthropic 认为，这将扩大恶意行为者可用的网络攻击能力。

telegram · zaihuapd · 9月29日 23:58

**「背景」** GLM-5.3 是智谱 AI（Z.ai）发布的前沿模型，在 CyberGym 基准中获得 84.5%，高于 Anthropic Mythos 5 的 83.8% 和 GPT-5.6 Sol 的 83.6%，但 ExploitBench 分数 54.4% 明显低于 Mythos 5 的 78.0%。该模型的权重在发布时未开放，Z.ai 曾承诺在进行两周安全测试和加固后放出；独立研究者尚无法复现其声称的排名。Anthropic 评估指出，GLM-5.3 不同于其他前沿模型，发布时缺乏实质性滥用防护，简单技术可在模拟测试中以 64% 至 100% 的比例绕过其安全防护。

**「影响」** 安全从业者和模型发布方需将 GLM-5.3 的 ExploitBench 成功率（50/410）及 64%–100% 的防护绕过率纳入风险审查，因为开放权重会降低后续滥用门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities">GLM - 5 . 3 and the spread of advanced cyber capabilities \ Anthropic</a></li>
<li><a href="https://www.remio.ai/post/z-ai-challenges-the-anthropic-google-coding-order-with-glm-5-3">Z.AI Challenges the Anthropic Google Coding Order With GLM - 5 . 3</a></li>
<li><a href="https://www.implicator.ai/z-ai-delays-glm-5-3-weights-two-weeks-after-cyber-score-beats-mythos-5/">Z.ai Delays GLM - 5 . 3 Weights After CyberGym Score Tops Mythos</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#cybersecurity`, `#large language models`, `#open source`, `#model evaluation`

---

<a id="item-tech-news-7"></a>
### [GPT 6.1 Sol：以五分之一价格实现接近 Astra 的智能](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 7.0/10

OpenAI 宣布推出 GPT-6.1 Sol，声称以五分之一的成本达到接近 Astra 的智能水平。社区指出，该模型的缓存输入成本为每百万 tokens 0.10 美元，比标准输入价格低 95%，比 GPT-6 Sol 的缓存输入价格低 50%，被视为更实际的重要更新。有用户猜测，GPT-6.1 Sol 可能是此前在文件中发现的 Astra-Minor 的紧急改名，因为 GPT-6 Sol 表现不佳而 Opus 5.5 表现强劲。多名用户报告 GPT-6 Sol 相比 Sol 5.6 出现明显倒退，并因此在编码等任务中转向 Opus 5.5。讨论还认为，token 价格正成为行业主要竞争点。

hackernews · crorella · 9月29日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=49896586)

**「背景」** OpenAI 的 GPT-6 系列包含 Sol 和 Astra 等模型，其中 GPT-6 Sol 此前发布时被描述为其性能水平上最具成本效益的模型。GPT-6.1 Sol 是 GPT-6 Sol 的升级版，旨在以 Astra 标准输入和输出令牌价格的五分之一，接近 Astra 在代理编码、计算机使用和专业工作上的智能水平。缓存输入价格降至每百万令牌 0.10 美元，被视为重要的成本变化。

**「影响」** 对于使用 OpenAI Codex 和缓存输入的用户，GPT-6.1 Sol 的缓存输入价格降低 50%，可能显著降低大规模调用成本；但用户对质量是否与宣称相符仍持怀疑。

**「社区讨论」** 社区普遍对 GPT-6 Sol 的质量表示失望，认为其相比 Sol 5.6 明显倒退，部分用户已转向 Opus 5.5；同时有人猜测 GPT-6.1 Sol 是 Astra-Minor 的改名，并认为 token 价格成为行业主要竞争点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT - 6 . 1 Sol | OpenAI</a></li>
<li><a href="https://digg.com/tech/a6fae1e5-6e03-4703-86ab-19c1a4870946">GPT - 6 . 1 Sol is pitched as near - Astra intelligence for a fifth of the ...</a></li>
<li><a href="https://yellow.com/news/gpt-6-1-sol-launch">OpenAI Launches GPT - 6 . 1 Sol At One- Fifth The Price Of Astra</a></li>

</ul>
</details>

**标签**: `#artificial-intelligence`, `#large-language-models`, `#openai`, `#pricing`, `#gpt`

---

<a id="item-tech-news-8"></a>
### [美国政府推出基于 Gemini 的公共服务门户 America.gov](https://america.gov/) ⭐️ 7.0/10

美国推出新的政府门户 America.gov，使用 Google Gemini 引导公民获取公共服务。Google 作为技术合作伙伴表示，该服务旨在帮助超过 1 亿人更快、更便捷地获取关键公共资源。该门户部署了防护措施，以确保回答符合法律边界；有用户反馈其对于进入国会大厦等违法行为给出了直接的法律警告。这一部署被视为大规模真实场景下 AI 辅助公共服务的典型案例，旨在缓解用户寻找服务困难及网络钓鱼风险。

hackernews · plesiv · 9月29日 14:04 · [社区讨论](https://news.ycombinator.com/item?id=49893509)

**「背景」** America.gov 是由美国政府推出的一站式联邦服务门户，旨在整合原本分散的政府服务入口，降低公民办理事务和遭遇钓鱼网站的风险。该门户采用 Google 的 Gemini 大语言模型作为底层 AI 助手，官方称将帮助超过 1 亿人更快获取公共资源。此前美国联邦服务信息分散在数千个网站中，用户常难以判断正确渠道。

**「影响」** America.gov 将近 30,000 个联邦政府网站整合到一个由 Google Gemini 和 Elon Musk 的 Grok 提供支持的 AI 聊天机器人中，公民可以通过提问获取公共服务和采购指导，这可能会降低查找政府服务的难度，但也将关键指引集中在单一自动化系统上。

**「社区讨论」** 部分用户认可该门户简化公共服务获取的潜力，但也对底层模型和防护措施存在疑虑。有评论称其回答在法律问题上表现诚实，另有人指出关于“中国模型”的截图可能为伪造，并提到该模型能回答 1989 年 6 月 3-4 日的事件，暗示部署前可能经过了调整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/google-s-gemini-ai-powers-new-america-gov-federal-portal">Google&#x27;s Gemini AI Powers New America.gov Federal Portal | The Tech Buzz</a></li>
<li><a href="https://www.whalesbook.com/news/English/technology/Google-Gemini-Powers-New-US-Government-Portal-Americagov/6abbee6b5aacb956d0853429">Google Gemini Powers New US Government Portal America.gov | Whalesbook</a></li>
<li><a href="https://blog.google/company-news/outreach-and-initiatives/public-policy/america-gov-google-public-sector/">Google Gemini powers new America.gov portal</a></li>
<li><a href="https://www.cnbc.com/2026/09/29/trump-ai-gemini-grok.html">Trump admin AI website uses Gemini , Grok: Joe Gebbia</a></li>
<li><a href="https://www.zerohedge.com/political/trump-launches-americagov-website-simplifying-access-government-services">Trump Launches America . Gov Website Simplifying... | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#government-technology`, `#ai-assistant`, `#google-gemini`, `#public-services`

---

<a id="item-tech-news-9"></a>
### [PS5 Relapse 漏洞利用公开](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 7.0/10

GitHub 仓库“Relapse-Exploit”公开了一个针对 PS5 的漏洞利用，该利用针对 WebKit JavaScriptCore 引擎中的缺陷。该仓库引发了关于主机安全和游戏存档备份的技术讨论。有用户询问能否将其用于将游戏存档备份到 USB，因为 PS5 不允许将存档备份到本地物理介质，只能通过订阅 PS Plus 启用云备份，且每个用户配置文件需单独订阅。讨论中还涉及索尼是否会通过禁用 JIT 来缩小攻击面，以及相关社区可能持有更多零日漏洞。

hackernews · therepanic · 9月29日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49895304)

**「背景」** PS5 的漏洞利用通常需要先通过浏览器（如 WebKit）获得内存读写原语，再配合内核漏洞提升权限；Relapse 是开发者 ntfargo 在 GitHub 发布的漏洞链，目标固件为 7.00 至 13.60。该链浏览器阶段利用 JavaScriptCore 信息泄露和一个结构化克隆对象池不匹配问题造成内存损坏，内核阶段则利用竞争条件来执行未签名代码，官方说明还提示 WebKit 阶段可能需要多次尝试，内核漏洞可能导致主机挂起或崩溃。

**「社区讨论」** 评论中，用户对利用的实用性提出疑问，如能否备份游戏存档到 USB 或让 Steam 游戏在 PS5 上运行。另有评论提到相关社区可能坐拥零日漏洞，以及希望该利用等到《GTA6》发布后再公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ntfargo/Relapse-Exploit">GitHub - ntfargo/Relapse-Exploit: Exploit chain for PS5 7.00 ...</a></li>
<li><a href="https://elsolitario.org/en/2026/09/29/relapse-repo-claims-ps5-exploit-firmware-7-00-to-13-60/">PS5 Jailbreak: What Is Relapse Exploit and Its Scope</a></li>

</ul>
</details>

**标签**: `#security`, `#exploit`, `#ps5`, `#webkit`, `#console-hacking`

---

<a id="item-tech-news-10"></a>
### [GPT 6.1 Sol：近 Astra 智能，价格五分之一](https://simonwillison.net/2026/Sep/29/hn-49898129/) ⭐️ 7.0/10

Simon Willison 在 Hacker News 上针对 GPT 6.1 Sol 的讨论发表了简短评论。该模型被宣传为以五分之一的价格提供接近 Astra 的智能。他链接了自己的 OpenAI DevDay 2026 主题演讲直播博客，并提供了 GPT-6.1-Sol 的基准测试“鹈鹕”可视化图表。Willison 表示这些图表与 GPT-6 系列的鹈鹕图没有显著差异。

rss · Simon Willison · 9月29日 18:27

**「背景」** OpenAI 在 2026 年 DevDay 上发布了 GPT-6.1 Sol，并声称其“以五分之一的价格获得接近 Astra 的智能”。据 The Next Web 和 TechCrunch 报道，其输入 token 价格为每百万 2 美元，是 GPT-6 Astra 标准价格的五分之一；OpenAI 表示它在代理编码、计算机使用和专业工作等任务上的表现接近 GPT-6 Astra。GPT-6 Astra 是 GPT-6 系列中价格较高的基准模型，因此 Sol 被视为面向成本敏感场景的低价版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/OpenAI/status/2104986129686741046">OpenAI on X: &quot;GPT-6.1 Sol: near-Astra intelligence for a fifth of the price. It’s the most cost-efficient model for its performance available today.&quot; / X</a></li>
<li><a href="https://thenextweb.com/news/openai-gpt-6-1-sol-price-astra-devday">‘Near-Astra intelligence for a fifth of the price’: GPT-6.1 Sol</a></li>
<li><a href="https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/">OpenAI launches GPT-6.1 Sol, says it nearly matches GPT-6 Astra and costs less | TechCrunch</a></li>

</ul>
</details>

**标签**: `#ai`, `#openai`, `#language-models`, `#llm`, `#hacker-news`

---

<a id="item-tech-news-11"></a>
### [免费开源书：从芯片到智能体的模型加速系统指南](https://www.reddit.com/r/MachineLearning/comments/1wt6ns4/i_wrote_a_free_opensource_book_on_making_ml/) ⭐️ 7.0/10

作者 /u/SoloTiger\_ 发布了一本免费开源的电子书《How to Make Your Model Fast: A Systems View of Efficient Machine Learning, from Silicon to Agents》（GitHub: https://github.com/usamahz/make-your-model-fast）。该书从系统视角讲解 ML 模型加速，强调减少 FLOPs 并不一定能让模型更快，需要先判断系统受计算、带宽、内存还是系统瓶颈约束。内容依次覆盖 roofline 分析和硬件、kernel、编译器、量化、剪枝、视觉、端侧 LLM、机器人、性能分析、服务，最后到智能体系统。目标是帮助读者建立直觉，在面对模型和硬件时判断极限速度以及哪种优化真正有效。作者欢迎 ML 系统、推理、编译器、边缘 AI 或性能工程领域的人提供反馈或贡献。

reddit · r/MachineLearning · /u/SoloTiger\_ · 9月29日 10:35

**「背景」** 在 ML 性能优化中，模型的实际速度不仅取决于浮点运算数（FLOPs），还受计算、带宽、内存和系统瓶颈约束；理解硬件特性与 roofline 模型是判断优化方向的基础。该书的内容与现有资源（如 Awesome AI Efficiency 和 JAX Scaling Book）形成互补，后者分别聚焦效率工具清单和大规模并行训练/推理。

**「影响」** 面向 ML 系统、推理、编译器或边缘 AI 的工程师可以直接使用这本免费开源书，系统性地先定位硬件/软件瓶颈，再决定是否值得做量化、剪枝或 kernel 优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PrunaAI/awesome-ai-efficiency">GitHub - PrunaAI/awesome-ai-efficiency: A curated list of ...</a></li>
<li><a href="https://jax-ml.github.io/scaling-book/">How To Scale Your Model - jax-ml.github.io</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#performance-engineering`, `#systems`, `#open-source-book`, `#hardware`

---

<a id="item-tech-news-12"></a>
### [CoWindow 与 MassAlloc：减少长上下文注意力冗余计算](https://www.reddit.com/r/MachineLearning/comments/1wt1gbk/cowindow_and_massalloc_attention_collective/) ⭐️ 7.0/10

作者提出了 CoWindow Attention（CoWA）和 MassAlloc Attention（MALA）两种方法，用于减少长上下文模型中注意力机制里的冗余计算。CoWA 通过互补窗口将远距离上下文分布到不同 KV 头，同时共享局部与前缀-sink 窗口；每个头仅进行稀疏注意力，但所有头的可见位置并集覆盖完整因果历史，且该模式由位置定义、无需学习路由或索引器。MALA 保留完整的因果 QK 打分，然后利用注意力自身的 softmax 统计信息决定是否为某个 tile 执行后续计算，从而跳过低贡献的后处理工作，并在训练与推理中使用共同容差。在 128K 上下文、8 张 H100 GPU、TP=8 的条件下，注意力算子相对 FullAttn 的加速为：CoWA 前向 7.4 倍、反向 8.6 倍、解码 3.0 倍；MALA 为 2.2、3.0、1.6 倍，但这些仅是算子级而非端到端模型加速。作者还报告在 14B 模型、32K 上下文下，CoWA 与 MALA 的总训练 FLOPs 分别降低 28.5% 和 23.1%，能力在报告评估上与 FullAttn 相当，同时强调集体覆盖不等同于逐头交互或输出相同，且未建立通用无损等价性。

reddit · r/MachineLearning · /u/BitExternal4608 · 9月29日 05:16

**「背景」** 标准因果注意力需要每个查询关注全部历史 token，产生 O\(n²\) 级计算量。现有高效方法常通过稀疏模式或跳过低贡献计算来降低开销；CoWindow 属于结构化稀疏注意力，MassAlloc 则是在完整 QK 打分后利用 softmax 统计量进行自适应计算分配。

**「影响」** 对于在 8 个 H100 GPU（TP=8）上处理 128K 长上下文的注意力算子开发者，CoWA 可带来前向 7.4 倍、反向 8.6 倍、解码 3.0 倍的算子级加速，MALA 为 2.2/3.0/1.6 倍；但这些并非端到端加速，且作者未声称与 dense attention 无损等价。

**标签**: `#attention mechanisms`, `#efficient transformers`, `#long-context models`, `#sparse attention`, `#kernel optimization`

---

<a id="item-tech-news-13"></a>
### [据报 OpenAI 发布 GPT-6.1 Sol，价格仅为 Astra 五分之一](https://openai.com/index/introducing-gpt-6-1-sol/) ⭐️ 7.0/10

据 Telegram 消息，OpenAI 推出了 GPT-6 Sol 的升级版 GPT-6.1 Sol，在智能体编程、计算机操作和专业任务上接近 GPT-6 Astra 的水平，输入输出价格仅为 Astra 标准价的五分之一，缓存输入每百万 token 0.10 美元。该模型已向 Plus、Pro、Business、Enterprise 和 Edu 用户在 ChatGPT Work 与 Codex 开放，暂未进入 Chat。开发者可通过 API 调用 gpt-6.1-sol，标准价格为每百万输入 token 2 美元、输出 token 10 美元。该消息来自未经验证的 Telegram 渠道，尚未得到 OpenAI 官方证实。

telegram · zaihuapd · 9月29日 17:09

**「背景」** GPT-6 Astra 是 OpenAI 的新一代旗舰模型，其 API 标准价格为每百万输入 token 10 美元、输出 50 美元。GPT-6.1 Sol 是定位编码、计算机使用和专业任务的低成本型号，官方页面称其智能接近 Astra，且价格约为 Astra 标准价的五分之一。

**「影响」** 若消息属实，开发者以 Astra 五分之一的价格即可调用接近 Astra 能力的模型，可显著降低智能体编程和计算机操作类任务的 API 成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-1-sol/">Introducing GPT-6.1 Sol | OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-6.1 Sol`, `#language model`, `#AI`, `#agentic coding`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [三部门：10 月 1 日起首套房贷贴息 1 个百分点，最长 5 年、单户贷款上限 100 万元](https://jrs.mof.gov.cn/zhengcefabu/phjr/202609/t20260929_3998312.htm) ⭐️ 9.0/10

中国财政部、中国人民银行、金融监管总局 9 月 29 日联合印发通知，自 2026 年 10 月 1 日起对符合条件的首套住房商业性个人住房贷款给予年化 1 个百分点贴息，最长 5 年、单户贷款本金上限 100 万元（每年最高约 1 万元）。家庭需使用新发放贷款、所购住房面积 120 平方米以下且价格 150 万元以下，政策暂定实施 1 年。

telegram · zaihuapd · 9月29日 10:18

**「背景」** 此前，中国人民银行、国家金融监督管理总局曾联合发布调整优化差别化住房信贷政策和降低存量首套住房贷款利率的通知。

**「对购房者的影响」** 符合条件的新发放首套房贷家庭（所购住房建筑面积 120 平方米以下、总价 150 万元以下）在最长 5 年内可按最多 100 万元贷款本金享受年化 1 个百分点贴息，单户每年最多减少约 1 万元利息支出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://item.btime.com/42c5hrjccr69jkb87hhvhc5ro1c">item.btime.com/42c5hrjccr69jkb87hhvhc5ro1c</a></li>

</ul>
</details>

**标签**: `#housing policy`, `#fiscal stimulus`, `#mortgage subsidy`, `#China economy`, `#real estate`

---

<a id="item-finance-news-2"></a>
### [美股盘前：Fair Isaac 大跌 18%，CarMax 业绩超预期](https://www.cnbc.com/2026/09/29/stocks-making-the-biggest-moves-premarket-fair-isaac-spacex-amd-more.html) ⭐️ 7.0/10

美股盘前，Fair Isaac 大跌 18%，因联邦住房金融局（FHFA）将房利美和房地美的抵押贷款定价统一为单一网格并纳入 VantageScore 评分。AMD 上涨逾 1%因以 82 亿美元收购 AI 公司 World Labs，CarMax 上涨逾 6%因第二财季每股收益 1.16 美元远超预期的 73 美分，营收 78.8 亿美元也高于预期的 70.9 亿美元。

rss · CNBC Finance · 9月29日 12:03

**「背景」** 此前，房利美和房地美的贷款定价仅使用 FICO Classic 评分网格；联邦住房金融局此次改为单一网格并纳入 VantageScore，打破了 Fair Isaac 在房贷信用评分领域的长期主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pomegra.io/news/fico-stock-plunges-25-on-vantagescore-mortgage-move">FICO stock plunges 25% on VantageScore mortgage… | Pomegra News</a></li>
<li><a href="https://finance.biggo.com/news/b0be5bcf-6c05-4db0-a1a2-f3aceb7794cd">Fair Isaac Plunges 20% as FHFA Orders Single Mortgage Pricing Grid — BigGo Finance</a></li>
<li><a href="https://www.fastcompany.com/91614972/fico-stock-collapsing-mortgage-industry-shakeup-credit-scores">FICO stock is collapsing as mortgage industry shakeup stands to reshape how credit scores are used</a></li>

</ul>
</details>

**标签**: `#premarket movers`, `#regulatory policy`, `#mergers and acquisitions`, `#earnings`, `#stock market`

---

<a id="item-finance-news-3"></a>
### [中国证监会据报对人形机器人 IPO 设三项新标准](https://www.cnbc.com/2026/09/29/china-criteria-humanoid-robot-ipos.html) ⭐️ 7.0/10

据三位知情人士透露，中国证监会正对人形机器人初创公司上市设置三项新标准：具备可持续营收和商业订单、亏损收窄且需提供三年预测、拥有机器人“大脑”或“手”等核心技术；消息人士称，这可能导致最终能上市的此类公司寥寥无几甚至没有。

rss · CNBC Finance · 9月29日 07:19

**「背景」** 香港自 2025 年 5 月起允许科技公司保密提交 IPO 申请，至少二十多家人形机器人相关“具身智能”公司已在香港递交申请；内地公司赴港上市仍需证监会批准。

**标签**: `#China`, `#humanoid robots`, `#IPO regulation`, `#artificial intelligence`, `#policy`

---

<a id="item-finance-news-4"></a>
### [星际之门数据中心因电力审批延期 甲骨文发不可抗力通知](https://www.bloomberg.com/news/articles/2026-09-24/oracle-cites-force-majeure-to-shield-itself-on-controversial-data-center) ⭐️ 7.0/10

甲骨文就星际之门旗下新墨西哥州 Project Jupiter 数据中心发出不可抗力通知，以 2.45 吉瓦配套微电网的环保与供电审批延迟为由，可能推迟部分付款并把 2028 年投运推迟。相关 180 亿美元银团贷款出现折价交易。

telegram · zaihuapd · 9月29日 05:46

**「背景」** 星际之门多数项目仍处于土建、审批和能源配套阶段，仅得州阿比林园区等少数投产，得州已暂停新数据中心项目审批。

**标签**: `#Oracle`, `#data centers`, `#project finance`, `#AI infrastructure`, `#energy approvals`

---

<a id="item-finance-news-5"></a>
### [苹果新 CEO 特努斯推动公司提速与精简](https://www.bloomberg.com/news/articles/2026-09-29/apple-s-new-ceo-moves-to-overhaul-company-to-run-faster-and-leaner) ⭐️ 7.0/10

据报道，苹果新任 CEO 约翰·特努斯上任数周后开始推动公司改革，目标是加快产品开发、扩大产品线并让组织更精简、更聚焦工程；具体措施包括考虑打破春季和秋季固定发布节奏、精简中层管理、缩短决策链条，并寻找新的收入来源。

telegram · zaihuapd · 9月30日 01:07

**「背景」** 约翰·特努斯在 2021 年至 2026 年担任苹果硬件工程高级副总裁，并于 2026 年接任 CEO，此次改革发生在其上任数周后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/John_Ternus">John Ternus - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#corporate restructuring`, `#CEO transition`, `#product strategy`, `#technology`

---