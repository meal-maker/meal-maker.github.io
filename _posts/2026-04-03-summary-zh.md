---
layout: default
title: "Horizon Summary: 2026-04-03 (ZH)"
date: 2026-04-03
lang: zh
---

> From 18 items, 11 important content pieces were selected

---

1. [谷歌发布 Gemma 4，一个具备先进能力的开源 AI 模型系列。](#item-1) ⭐️ 9.0/10
2. [前 Azure 核心工程师揭露侵蚀信任的决策和内部挑战。](#item-2) ⭐️ 8.0/10
3. [通义千问 3.6-Plus：面向真实世界智能体的新 AI 模型](#item-3) ⭐️ 8.0/10
4. [LinkedIn 扫描 Chrome 浏览器扩展用于指纹识别和数据收集。](#item-4) ⭐️ 8.0/10
5. [Tailscale 博客文章针对 macOS 刘海隐藏菜单栏图标提供解决方法](#item-5) ⭐️ 7.0/10
6. [Cursor 3 发布，增强 AI 代理功能](#item-6) ⭐️ 7.0/10
7. [关于 2008 年引语的讨论：好主意无需谎言即可获得接受](#item-7) ⭐️ 7.0/10
8. [OpenAI 收购技术媒体公司 TBPN](#item-8) ⭐️ 7.0/10
9. [OpenClaw v2026.4.1 新增任务面板、Bedrock 安全防护与协作工作流。](#item-9) ⭐️ 6.0/10
10. [因液氧烧烤和制冷研究闻名的工程师乔治·戈布尔逝世](#item-10) ⭐️ 6.0/10
11. [AI 可能加剧贫富分化，与其他技术不同](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemma 4，一个具备先进能力的开源 AI 模型系列。](https://deepmind.google/models/gemma/gemma-4/) ⭐️ 9.0/10

谷歌发布了 Gemma 4，这是一个开源模型系列，具备推理、多模态和工具调用能力，提供四种规模：Effective 2B、Effective 4B、26B Mixture of Experts 和 31B Dense。 此次发布意义重大，因为它将最先进的智能体 AI 能力带到了边缘设备，实现了强大的端侧工作流，并通过增强的多模态和工具集成推动了开源生态系统的发展。 关键细节包括中型模型支持高达 256K 的上下文窗口，31B 模型在 MMLU 基准测试中获得 88.4%的分数，以及社区报告的问题，例如 gemma-4-31b 模型在部分本地部署中仅输出'---'。

hackernews · jeffmcjunkin · Apr 2, 16:10

**背景**: Gemma 是谷歌设计的开源、轻量级语言模型系列，旨在提高效率和可访问性。多模态推理使 AI 能够处理和推理跨不同类型的数据，如文本和图像，而工具调用则允许模型与外部 API 和函数交互，以增强任务执行能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/">Gemma 4: Byte for byte, the most capable open models</a></li>
<li><a href="https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/">Bring state-of-the-art agentic skills to the edge with Gemma 4 - Google Developers Blog</a></li>

</ul>
</details>

**社区讨论**: 社区讨论非常活跃，用户分享了量化指南、与 Qwen 3.5 等模型的基准测试比较，并报告了积极结果（例如 26B-a4b 模型的强大性能）和关键问题（例如 31B 模型在某些设置中无法正常工作）。

**标签**: `#AI`, `#open-source`, `#language-models`, `#multimodal`, `#benchmarks`

---

<a id="item-2"></a>
## [前 Azure 核心工程师揭露侵蚀信任的决策和内部挑战。](https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion) ⭐️ 8.0/10

一名前 Azure 核心工程师发表了一篇揭露文章，详细说明了内部决策和工程实践（如因害怕破坏现有功能而拒绝代码重构）如何侵蚀了微软 Azure 云平台的信任，并引用了企业文化和技术债务等问题。 这一内部视角具有重要意义，因为它揭示了主要云提供商的系统性工程和管理问题，可能影响客户信心和运营可靠性，并反映了大型科技公司处理技术债务和创新方面的更广泛趋势。 关键细节包括工程师声称使用智能指针的错误修复和重构被拒绝以避免风险，并且社区反馈强调 Azure 用户界面整合不佳，文档经常过时或由 AI 生成，引发了对服务可靠性的担忧。

hackernews · axelriet · Apr 2, 16:00

**背景**: Azure 是微软的云计算平台，提供基础设施和软件等广泛服务。Azure 核心工程团队负责开发和维护 Azure 的基础设施，包括软件增强和新产品。技术债务指的是代码或设计中因采用捷径而导致的未来成本，这使得后续更改更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://careers.microsoft.com/v2/global/en/AzureCoreCareers.html">Power the world's workloads with Azure Core</a></li>
<li><a href="https://www.knowledgehut.com/blog/cloud-computing/azure-roles-and-responsibilities">Microsoft Azure Roles and Responsibilities in 2026</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出复杂情绪，一些用户基于个人使用 Azure 时遇到的界面问题和文档问题验证了这些说法，而另一些人则质疑工程师的动机是举报还是心怀不满，但总体上认为这一叙述可信且令人担忧。

**标签**: `#Azure`, `#Microsoft`, `#Cloud Computing`, `#Software Engineering`, `#Corporate Culture`

---

<a id="item-3"></a>
## [通义千问 3.6-Plus：面向真实世界智能体的新 AI 模型](https://qwen.ai/blog?id=qwen3.6) ⭐️ 8.0/10

通义千问发布了旗舰 AI 模型 Qwen3.6-Plus，旨在提升真实世界智能体能力，具备 100 万 token 的原生上下文窗口和增强的智能体编码性能。该模型仅作为托管服务提供，标志着与通义千问以往开源权重发布的背离。 该模型在开发能自主与真实世界环境交互的 AI 智能体方面取得重要进展，可能影响自动化和机器人等行业。仅托管模式标志着通义千问的战略转变，将影响 AI 市场的可及性，以及与 Claude 和 ChatGPT 等竞争对手的竞争格局。 Qwen3.6-Plus 拥有 100 万 token 的上下文窗口，最高 65536 个输出 token，并在 Terminal-Bench 2.0 等智能体编码基准测试中以 61.6 分领先。然而，它未开源权重，参数数量未公开，且其基准测试比较因使用 Claude Opus 4.5 等旧版本模型而非最新版本而受到批评。

hackernews · pretext · Apr 2, 14:28

**背景**: AI 中的真实世界智能体是能感知环境并自主采取行动以实现目标的智能系统，通常使用机器学习。仅托管模型通过云 API 部署，提供了便利性，但与自托管开源替代方案相比，限制了用户控制、隐私和定制化。通义千问因发布开源模型而享有声誉，因此在行业趋向开源和专有部署的背景下，转向仅托管模式尤为引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intelligent_agent">Intelligent agent - Wikipedia</a></li>
<li><a href="https://www.deployhq.com/blog/self-hosting-ai-models-privacy-control-and-performance-with-open-source-alternatives">Self-Hosting AI Models: Hardware Requirements, Model Selection, and Deployment Guide</a></li>
<li><a href="https://llm-stats.com/models/qwen3.6-plus">Qwen3.6 Plus: Pricing, Benchmarks & Performance</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂，批评集中在模型仅托管且未开源权重，这与通义千问以往的开源做法形成对比。讨论还强调了关于基准测试实践的辩论，例如与 Claude Opus 4.5 而非 4.6 的比较，并注意到通过 OpenRouter 等平台提供免费访问的可及性。

**标签**: `#AI`, `#Language Models`, `#Real-world Agents`, `#Qwen`, `#Benchmarking`

---

<a id="item-4"></a>
## [LinkedIn 扫描 Chrome 浏览器扩展用于指纹识别和数据收集。](https://browsergate.eu/) ⭐️ 8.0/10

LinkedIn 正在使用 JavaScript 在基于 Chrome 的浏览器中静默扫描已安装的浏览器扩展，通过 ID 探测数千个特定扩展，收集结果、加密数据并传输到其服务器。 这种侵入性做法增强了 LinkedIn 在未经同意的情况下跟踪用户的能力，加剧了普遍存在的浏览器指纹识别，损害在线隐私并影响该平台的所有用户。 扫描针对 Chrome 等基于 Chromium 的浏览器，使用 JavaScript 方法通过扩展 ID 和 DOM 痕迹检测扩展，LinkedIn 声称其目的是识别抓取数据或违反服务条款的扩展。

hackernews · digitalWestie · Apr 2, 13:09

**背景**: 浏览器指纹识别是一种跟踪技术，通过聚合字体、WebGL 和屏幕大小等微弱信号来创建唯一的用户标识符。JavaScript 可以通过探测特定扩展资源或分析它们留下的 DOM 变化来检测已安装的浏览器扩展，这是指纹识别工具中的常见方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>
<li><a href="https://datadome.co/anti-detect-tools/extension-detector/">Extension-detector: Browser Extension Fingerprinting Tool</a></li>

</ul>
</details>

**社区讨论**: 社区表达了严重的隐私担忧，用户就扫描的侵入性以及 LinkedIn 以针对恶意扩展为由的辩护展开辩论。情绪复杂，包括对伦理问题、指纹识别的技术细节以及用户与 LinkedIn 数据实践的个人经历的讨论。

**标签**: `#privacy`, `#browser-extensions`, `#fingerprinting`, `#linkedin`, `#javascript`

---

<a id="item-5"></a>
## [Tailscale 博客文章针对 macOS 刘海隐藏菜单栏图标提供解决方法](https://tailscale.com/blog/macos-notch-escape) ⭐️ 7.0/10

Tailscale 发布了一篇博客文章，探讨了 macOS 刘海遮挡菜单栏图标的问题，并提供了一个实用的解决方法以防止图标被隐藏。 此事之所以重要，是因为它突显了 macOS 中一个长期存在的 UI 缺陷，影响了用户体验和开发者支持，可能导致应用创作者面临退款和退单问题，同时也加剧了对苹果软件管理的批评。 解决方法涉及使用 defaults 写入等系统命令来减小菜单栏图标之间的间距，但此修复需针对每个应用进行，且无法在系统层面解决根本问题。

hackernews · tosh · Apr 2, 18:22

**背景**: Tailscale 是一家软件公司，提供基于 WireGuard 协议的无配置 VPN 服务，用于创建安全的点对点网状网络。macOS 设备上的刘海随新款 MacBook Pro 机型引入，可能会隐藏菜单栏图标，这是一个尽管有用户抱怨和解决方法但仍持续存在的已知 UI 问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/docs/concepts/what-is-tailscale">What is Tailscale? · Tailscale Docs</a></li>
<li><a href="https://mjtsai.com/blog/2023/12/08/mac-menu-bar-icons-and-the-notch/">Michael Tsai - Blog - Mac Menu Bar Icons and the Notch</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对刘海问题的沮丧，用户分享了减小图标间距等技术解决方法，并批评苹果未能修复。讨论还扩展到更广泛的网络需求，例如使用 Tailscale 进行远程访问解决方案。

**标签**: `#macOS`, `#UI/UX`, `#Tailscale`, `#software-development`, `#networking`

---

<a id="item-6"></a>
## [Cursor 3 发布，增强 AI 代理功能](https://cursor.com/blog/cursor-3) ⭐️ 7.0/10

Cursor 3 已发布，引入了新的以代理为先的界面，支持并行运行多个 AI 代理，同时提供云会话管理和重新设计的差异视图。此次重大更新基于 Cursor Alpha 用户的反馈，将 IDE 功能与最新的 AI 进展相结合。 此次发布标志着 AI 辅助编码工具演进的重要一步，通过自动化复杂任务可能提升开发者的生产力，并加剧了 IDE 市场中与 Claude Code 等替代品的竞争。这突显了将 AI 代理直接集成到软件开发工作流中的增长趋势。 Cursor 是基于 VS Code 分支构建的，并在每次交互中以 AI 辅助为核心，但用户评论指出其价格可能较高，企业版计划为每月每用户 40 美元，与 Claude Code 的比较揭示了定价和功能上的权衡。此次更新将 Composer 2 模型设为默认，虽然其智能程度不如 OpenAI 或 Anthropic 的旗舰模型，但对于某些任务更具直觉性。

hackernews · adamfeldman · Apr 2, 18:13

**背景**: Cursor 是一个基于 VS Code 分支的 AI 辅助集成开发环境（IDE），旨在将 AI 能力直接集成到编码工作流中，用于代码补全和导航等任务。Claude Code 是另一个用于编码的 AI 工具，采用基于代理的辅助，常因自动化开发任务的方法与 Cursor 进行比较。AI 辅助 IDE 旨在通过利用机器学习模型来建议代码、重构和调试，从而提升开发者的生产力，此类工具在软件工程中日益流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/blog/cursor-3">Meet the new Cursor · Cursor</a></li>
<li><a href="https://www.builder.io/blog/cursor-vs-claude-code">Claude Code vs Cursor: What to Choose in 2026 - Builder.io</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出复杂的情绪，一些用户因效率和集成性偏好 Cursor，而另一些用户认为 Claude Code 更具成本效益或更适合特定工作流程。有担忧指出 Cursor 的设计方向正转向以聊天为先的界面，一些开发者认为这削弱了对代码本身的关注，并且辩论突显了基于定价和可用性对这两种工具的持续比较。

**标签**: `#AI-Assisted Coding`, `#Code Editors`, `#Developer Tools`, `#Hacker News`, `#Software Engineering`

---

<a id="item-7"></a>
## [关于 2008 年引语的讨论：好主意无需谎言即可获得接受](https://blog.danieldavies.com/2004/05/d-squared-digest-one-minute-mba.html) ⭐️ 7.0/10

HackerNews 上重新讨论了一则关于诚实与好主意的 2008 年引语，引发了广泛对话，话题从历史上的科技公司股权激励实践延伸到当代人工智能伦理和营销策略的担忧。 此次讨论之所以重要，是因为它凸显了科技和商业领域中持续的伦理辩论，将股票期权的历史教训与现代人工智能炒作等问题联系起来，并质疑在获得公众接受时，诚实沟通是否能与有说服力的营销竞争。 该引语最初发表于 2004 年，并在 2008 年略有更新；社区讨论中包含多种观点，例如指出股票期权随着时间的推移得到了验证，而另一些人则认为好主意常因营销不佳而输给坏主意，并对人工智能公司夸大能力表示担忧。

hackernews · sedev · Apr 2, 17:29

**背景**: 该引语最初涉及科技公司的股票期权，这是一种薪酬形式，允许员工以固定价格购买公司股票，常用于吸引和留住人才。随着时间的推移，这种做法变得普遍并得到了验证，但也引发了关于会计伦理和管理诚实的辩论。此后的讨论已扩展到科技领域更广泛的伦理问题，如围绕人工智能开发和营销的议题，其中也存在类似的关于真实性与炒作的担忧。

**社区讨论**: 社区讨论展现出多样化的情绪，用户如 nostrademons 强调股票期权最终得到了验证，convexly 认为诚实的表述常输给更好的营销，而 didgetmaster 则对人工智能公司夸大能力表示担忧。总体而言，讨论混合了历史反思、对沟通有效性的实际关切以及对现代科技趋势的伦理忧虑。

**标签**: `#ethics`, `#technology`, `#business`, `#AI`, `#discussion`

---

<a id="item-8"></a>
## [OpenAI 收购技术媒体公司 TBPN](https://openai.com/index/openai-acquires-tbpn/) ⭐️ 7.0/10

OpenAI 已收购 TBPN（Technology Business Programming Network），这是一个由 John Coogan 和 Jordi Hays 主持的每日直播技术谈话节目，在 YouTube 和 X 等平台播放。此次收购在 OpenAI 官方网站上宣布，确认了 TBPN 作为科技领域增长最快的媒体公司之一的地位。 此次收购引发了关于 AI 行业对媒体独立性影响的辩论，可能使一家主要的 AI 参与者塑造公众对技术和商业新闻的讨论。它凸显了在快速发展的 AI 生态系统中，企业控制信息渠道的更广泛的伦理担忧。 TBPN 于 2025 年推出，已成为筹资公告的关键场所，有 296 家公司宣布了总额 709 亿美元的交易，涉及 314 笔交易。此次收购是 OpenAI 近期一系列举措的一部分，包括其他高调收购如 OpenClaw 和 Astral，表明其在核心 AI 研究之外的战略扩张。

hackernews · surprisetalk · Apr 2, 17:26

**背景**: OpenAI 是一家领先的人工智能研究公司，以开发 GPT 等模型而闻名。TBPN 是一家媒体公司，制作每日专注于技术商业新闻的播客，采访行业领袖并在 YouTube、X 和 Substack 等数字平台直播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TBPN">TBPN - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/04/02/openai-acquires-tech-podcast-tbpn.html">OpenAI acquires popular tech podcast TBPN</a></li>
<li><a href="https://openai.com/index/openai-acquires-tbpn/">OpenAI acquires TBPN | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示对 OpenAI 动机的怀疑，用户担忧隐含的编辑影响，并将此次收购视为一种愤世嫉俗的公关举措，以塑造“好人”形象。一些用户称赞 TBPN 内容的高信噪比及其在技术交易公告中的既定作用，尽管其他人质疑其突然的知名度。

**标签**: `#OpenAI`, `#acquisition`, `#AI-ethics`, `#media`

---

<a id="item-9"></a>
## [OpenClaw v2026.4.1 新增任务面板、Bedrock 安全防护与协作工作流。](https://github.com/openclaw/openclaw/releases/tag/v2026.4.1) ⭐️ 6.0/10

OpenClaw 发布了版本 2026.4.1，引入了多项新特性，包括原生的聊天任务面板、捆绑的 SearXNG 网络搜索插件、Amazon Bedrock Guardrails 支持、macOS 语音唤醒功能，以及专用于飞书云文档协作的评论事件处理流程。此外，该更新还包含了对智能体配置、会话路由和错误管理的多项改进。 此次更新通过在聊天界面直接集成任务管理和通过 Amazon Bedrock Guardrails 为生成式 AI 应用添加关键安全控制，增强了 OpenClaw 在团队和企业环境中的实用性。改进的飞书云文档集成简化了文档协作流程，使 AI 智能体能更无缝地融入现有的业务工作流。 值得注意的是，SearXNG 插件是一个可自托管、无需密钥的网络搜索替代方案，提供了更高的隐私性和控制力。该版本还解决了一个常见的用户体验问题，即防止原始的提供商或运行时错误信息泄露到外部聊天频道，取而代之的是友好的重试提示。

github · steipete · Apr 1, 16:58

**背景**: OpenClaw 是一个用于构建 AI 智能体的开源框架，可以连接到各种模型和通信渠道，如 Telegram 和飞书。SearXNG 是一个开源的元搜索引擎，可聚合来自谷歌、必应等多个来源的搜索结果。Amazon Bedrock Guardrails 是一项服务，提供可配置的防护措施，用于检测和过滤生成式 AI 应用中的有害内容。飞书是字节跳动推出的协作平台，包含文档编辑和工作流自动化功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.openclaw.ai/tools/searxng-search">SearXNG Search - OpenClaw</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">Detect and filter harmful content by using Amazon Bedrock ...</a></li>
<li><a href="https://docs.openclaw.ai/channels/feishu">Feishu - OpenClaw</a></li>

</ul>
</details>

**标签**: `#AI`, `#chatbot`, `#task-management`, `#web-search`, `#collaboration`

---

<a id="item-10"></a>
## [因液氧烧烤和制冷研究闻名的工程师乔治·戈布尔逝世](https://www.legacy.com/us/obituaries/wlfi/name/george-goble-obituary?id=61144779) ⭐️ 6.0/10

乔治·H·戈布尔已去世，其讣告和维基百科页面证实了这一消息。他是一位与普渡大学相关的电气工程师和发明家。 他的逝世标志着一位于早期计算基础设施和创新制冷解决方案做出贡献的先驱者的离去，突显了动手工程创造力的影响。液氧烧烤事件在技术社区中仍然是一个标志性故事，展示了科学与实践实验的结合。 戈布尔于 1996 年因在五秒内用液氧点燃 charcoal 烤架而获得搞笑诺贝尔化学奖，这一壮举有在线视频记录。他还发明了 R-406a 和 GHG-X8 等制冷剂替代品，这些替代品效果显著，但由于安全和环境问题面临 EPA 监管障碍。

hackernews · finaard · Apr 2, 18:21

**背景**: 乔治·H·戈布尔是普渡大学的电气工程师，普渡大学于 1962 年建立了美国第一个计算机科学系。液氧（LOX）是一种用作强效氧化剂的低温液体，以其在火箭推进中的作用以及像戈布尔烧烤演示中作为燃烧促进剂而闻名。制冷剂 R-12 是一种氯氟烃，因其消耗臭氧的特性而在全球被淘汰，这推动了戈布尔等人的替代品研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://engineering.purdue.edu/ECE/Alums/OECE/2022/George-Goble">George Goble - Elmore Family School of Electrical and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Liquid_oxygen">Liquid oxygen - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论分享了戈布尔技术成就的温馨回忆，包括他广为传播的液氧烧烤视频、用户称赞的有效 R-12 制冷剂替代品，以及他在普渡大学早期使用 PDP-11 系统进行计算的贡献。整体情绪是钦佩和怀旧，轶事突出了他的创新和前瞻性思维，例如早期移动电子邮件的使用。

**标签**: `#computing-history`, `#engineering`, `#obituary`, `#Purdue`, `#refrigeration`

---

<a id="item-11"></a>
## [AI 可能加剧贫富分化，与其他技术不同](http://www.ruanyifeng.com/blog/2026/04/weekly-issue-391.html) ⭐️ 6.0/10

在最新一期的科技爱好者周刊中，作者阮一峰提出论点，认为像月费 200 美元的 Claude Code Max 套餐和 OpenAI 设想的月费 2 万美元顶级服务这样的 AI 模型，可能通过使先进 AI 对大众不可及，导致严重的贫富分化。 这一点很重要，因为如果 AI 的获取因成本而分层，它可能逆转智能手机和互联网等大规模生产技术带来的消费者平等趋势，潜在地创造一个新的数字鸿沟，使富人从更优的 AI 能力中获得不成比例的优势。 值得注意的是，AI 模型的性能与计算资源挂钩，但缺乏规模效应——更多的服务器会增加成本而非降低成本，这与大规模生产后变得更便宜的工业品相反。具体例子包括 Claude Code 的 200 美元/月 Max 套餐和 OpenAI 传闻中 2 万美元/月的顶级 AI 智能体层级。

rss · 阮一峰的个人网站 · Apr 3, 00:08

**背景**: 消费者平等指的是像可口可乐、iPhone 或特斯拉汽车这样的技术，通过大规模生产变得对富人和穷人都负担得起且相同，从而减少了可见的财富差距。相比之下，AI 模型依赖于昂贵的计算能力，且无法通过规模实现类似的成本降低，因为其效果取决于计算力、上下文长度和参数等因素，这些都需要大量的资金投入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://www.theverge.com/openai/624692/20000-a-month-for-an-ai-chatbot">$20000 a month for an AI chatbot? - The Verge</a></li>

</ul>
</details>

**标签**: `#AI Ethics`, `#Social Impact`, `#Wealth Inequality`, `#AI Models`

---