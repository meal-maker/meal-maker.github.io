---
layout: default
title: "Horizon Summary: 2026-03-14 (ZH)"
date: 2026-03-14
lang: zh
---

> From 23 items, 11 important content pieces were selected

---

1. [Claude 的 100 万令牌上下文窗口现已全面适用于 Opus 4.6 和 Sonnet 4.6](#item-1) ⭐️ 9.0/10
2. [推出用于评估本地 AI 模型部署可行性的工具](#item-2) ⭐️ 8.0/10
3. [卡塔尔氦气停产使芯片供应链面临两周缓冲期危机。](#item-3) ⭐️ 8.0/10
4. [39 个 Algolia 管理 API 密钥在开源文档站点中被暴露](#item-4) ⭐️ 7.0/10
5. [MouseControl：针对 macOS 的 Logitech Options Plus 开源替代方案](#item-5) ⭐️ 7.0/10
6. [Hammerspoon v2 将为 macOS 自动化从 Lua 切换至 JavaScript](#item-6) ⭐️ 7.0/10
7. [Parallels 确认 MacBook Neo 可以在虚拟机中运行 Windows 11。](#item-7) ⭐️ 7.0/10
8. [欧洲监管机构将对含战利品箱的游戏强制执行最低 16 岁年龄限制](#item-8) ⭐️ 7.0/10
9. [埃隆·马斯克在 AI 编码项目遇挫之际驱逐更多 xAI 创始人](#item-9) ⭐️ 7.0/10
10. [瑞典电子政务源代码泄露，官方声称影响仅限于测试服务器。](#item-10) ⭐️ 7.0/10
11. [字节跳动 ArkClaw 实现 OpenClaw AI 代理的零安装使用](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Claude 的 100 万令牌上下文窗口现已全面适用于 Opus 4.6 和 Sonnet 4.6](https://claude.com/blog/1m-context-ga) ⭐️ 9.0/10

Anthropic 已将其 Claude Opus 4.6 和 Sonnet 4.6 模型的 100 万令牌上下文窗口推向全面可用，实现了整个窗口的定价标准化，取消了长上下文附加费，并将媒体限制提高到 600 张图像或 PDF 页面。 这标志着 AI 能力的一次重大飞跃，使得模型能够一次性处理远更多的信息，从而可能彻底改变长文本内容生成、复杂文档分析和大型代码库管理等应用，推动大型语言模型行业的发展。 值得注意的是，现在整个 100 万令牌上下文窗口的定价是统一的，媒体处理能力也得到了提升，但社区讨论中强调了关于有效上下文可用性以及在高令牌数下性能可能下降的担忧。

hackernews · meetpateltech · Mar 13, 17:19

**背景**: 在大型语言模型中，上下文窗口指的是模型为生成响应而能一次性考虑的文本范围，以令牌为单位衡量。令牌是自然语言处理中文本处理的基本单位，通常对应单词或子词。Claude Opus 4.6 和 Sonnet 4.6 是 Anthropic 开发的高级 AI 模型，专为高级推理和理解任务而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/context-window">What is a Context Window for Large Language Models?</a></li>
<li><a href="https://www.datacamp.com/blog/what-is-tokenization">Tokenization in NLP: How It Works, Challenges, and Use Cases | DataCamp</a></li>
<li><a href="https://www.anthropic.com/news/claude-sonnet-4-6">Introducing Sonnet 4 . 6 \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户赞扬 Opus 4.6 在编码任务中的智能性和实用性，同时讨论集中在长上下文定价的取消、媒体限制的扩大，以及对高令牌量下有效上下文窗口可用性和连贯性的担忧。

**标签**: `#LLM`, `#Context Window`, `#Claude`, `#AI`, `#Natural Language Processing`

---

<a id="item-2"></a>
## [推出用于评估本地 AI 模型部署可行性的工具](https://www.canirun.ai/) ⭐️ 8.0/10

一款名为'Can I run AI locally?'的新工具已上线，它通过分析内存需求和模型规格来评估 AI 模型是否能在本地硬件上运行。该工具在 HackerNews 上引发讨论，用户对其准确性提出批评并分享了技术见解。 这很重要，因为它简化了开发者和爱好者本地部署 AI 模型的过程，有助于提升隐私、节省成本并减少对云服务的依赖，尽管其准确性限制凸显了硬件估计的复杂性。 该工具的估计可能对如 GPT-OSS-20B 这样的专家混合模型不准确，因为每个令牌激活的参数较少，并且因未明确标注量化模型而受到批评，导致对实际内存需求的混淆。

hackernews · ricardbejarano · Mar 13, 12:46

**背景**: 本地 AI 部署指的是在个人设备而非云服务器上运行模型，以获得隐私和更低延迟等好处。模型量化，如 4 位量化（例如 Q4_K_M），通过降低数值精度来减小模型大小，从而实现边缘部署。此外，专家混合架构每个令牌只激活部分参数，使其在推理中比密集模型更节省内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ygorml/local_inference_calculator">GitHub - ygorml/local_inference_calculator: Local Inference ...</a></li>
<li><a href="https://moschip.com/blog/ai-engineering/model-quantization-for-edge-ai/">Model Quantization for Edge AI</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出复杂情绪，既有对工具意图的赞赏，也有对其不准确性的批评。关键观点包括对模型架构的技术纠正（如密集模型与专家混合模型），使用小模型进行编码等任务的实际经验，以及对量化和内存需求误导信息的沮丧。

**标签**: `#AI`, `#local-deployment`, `#hardware-requirements`, `#machine-learning`, `#discussion`

---

<a id="item-3"></a>
## [卡塔尔氦气停产使芯片供应链面临两周缓冲期危机。](https://www.tomshardware.com/tech-industry/qatar-helium-shutdown-puts-chip-supply-chain-on-a-two-week-clock) ⭐️ 8.0/10

卡塔尔的氦气生产已停产，使全球半导体供应链仅剩两周的库存缓冲。这一中断可能导致芯片制造短缺和成本上升。 此事至关重要，因为氦气对半导体制造工艺（如化学气相沉积 CVD）必不可少，任何短缺都可能延误整个电子行业的生产。它凸显了全球供应链的脆弱性，并可能导致消费电子产品和技术产品的价格上涨。 氦气在半导体工厂中被用作化学气相沉积工艺的载气以及用于泄漏检测，因此对制造至关重要。卡塔尔是全球主要的氦气供应国，停产使得替代方案的反应时间极短，对生产构成直接风险。

hackernews · johnbarron · Mar 13, 12:31

**背景**: 氦气是一种主要从天然气中提取的稀有气体，在半导体制造中至关重要，用于沉积工艺中的载气以及真空泄漏检测等应用。卡塔尔是全球最大的氦气生产国之一，其生产设施对全球供应链至关重要。此次停产凸显了关键工业气体对特定地区的依赖，这可能扰乱技术领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reportsanddata.com/report-detail/semiconductor-grade-helium-gas-market">reportsanddata.com/report-detail/ semiconductor -grade- helium -gas...</a></li>
<li><a href="https://www.linde-engineering.com/products-and-services/process-plants/natural-gas-processing/helium-recovery-and-liquefaction-plants">Helium Recovery & Liquefaction Plants | A Linde Company</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对 PC 组件成本上升的担忧，用户们批评美国氦气政策的撤资，并质疑官方通胀数据。另有观点提及氮肥等其他商品的供应链问题，反映出更广泛的经济焦虑。

**标签**: `#supply-chain`, `#semiconductors`, `#helium`, `#manufacturing`

---

<a id="item-4"></a>
## [39 个 Algolia 管理 API 密钥在开源文档站点中被暴露](https://benzimmermann.dev/blog/algolia-docsearch-admin-keys) ⭐️ 7.0/10

一位安全研究员在其博客文章中披露，在多个开源文档网站的公开前端代码中发现了 39 个 Algolia 管理 API 密钥。这一漏洞是由于密钥被嵌入在公开可访问的站点中导致的。 此次暴露非常重要，因为管理密钥授予对 Algolia 账户的完全访问权限，可能导致受影响项目的数据被抓取、索引被操纵或服务中断。这反映了在开源和云服务中 API 密钥管理方面更广泛的安全挑战。 这些密钥是通过 Algolia 的 DocSearch 功能暴露的，当项目选择运行自己的爬虫时，该系统会发放具有管理员权限的密钥而缺乏适当的安全防护。值得注意的是，Algolia 未对研究人员的披露做出回应，且暴露的管理密钥在手动撤销或轮换前会一直保持活跃。

hackernews · kernelrocks · Mar 13, 22:52

**背景**: Algolia 是一个搜索即服务平台，使用 API 密钥进行身份验证，其中管理 API 密钥拥有管理索引、设置和数据的完全权限。管理密钥暴露可能导致未经授权的访问、数据窃取或拒绝服务攻击，因为它们授予对整个账户的控制权。API 密钥常被硬编码在源代码中，使其在如开源项目的公开仓库中容易泄露。安全最佳实践包括避免密钥嵌入、使用安全的后端服务以及定期轮换密钥以降低风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.algolia.com/doc/guides/security/api-keys">Generate API keys with limitations to secure your Algolia ...</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/appsonazureblog/lets-move-away-from-api-keys/4217697">Let's move away from API keys!</a></li>

</ul>
</details>

**社区讨论**: 社区对 Algolia 无视研究人员的披露表示强烈批评，认为这种不回应比密钥暴露本身更糟糕。一些评论批评报告包含了不必要的图表，而另一些人则质疑为何像 HomeAssistant 这样的特定受影响站点尚未修复。此外，有提及正在开发自动化工具来利用此类漏洞，并有观察表明暴露的密钥可能已被恶意行为者使用。

**标签**: `#security`, `#algolia`, `#api-keys`, `#open-source`, `#documentation`

---

<a id="item-5"></a>
## [MouseControl：针对 macOS 的 Logitech Options Plus 开源替代方案](https://github.com/TomBadash/MouseControl) ⭐️ 7.0/10

GitHub 上的开源项目 MouseControl 已被开发为 Logitech 专有 Options Plus 软件的轻量级替代品，特别旨在消除遥测数据收集并解决在 macOS 上的性能问题，如高 CPU 使用率。它使用户能够在不依赖 Logitech 软件的情况下重新映射 Logitech 鼠标的按钮。 这很重要，因为它解决了专有外设软件常见的隐私问题和软件臃肿，为 macOS 用户提供了一个社区驱动的解决方案，可提升系统性能并增强对设备的控制。这反映了优先考虑用户自主权和透明度的开源替代方案的更广泛趋势。 MouseControl 专为重新映射 Logitech MX Master 3S 鼠标的按钮而设计，需要 Python 运行，但它可能不支持所有 Logitech 设备，且目前专注于 macOS。该项目托管在 GitHub 上，并鼓励社区贡献以扩展其功能。

hackernews · avionics-guy · Mar 13, 18:42

**背景**: Logitech Options Plus 是用于 Logitech 鼠标和键盘的自定义软件，允许用户个性化设置和快捷键。然而，它因遥测数据收集和性能问题而受到批评，例如在 macOS 上的高 CPU 使用率，引发了隐私担忧和系统不稳定。像 MouseControl 这样的开源项目应运而生，旨在提供类似功能而无这些缺点，利用社区开发来避免专有软件的臃肿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.logitech.com/en-us/software/logi-options-plus">Logi Options+ Software | Logitech</a></li>
<li><a href="https://www.reddit.com/r/logitech/comments/13viej8/logi_options_requiring_input_monitoring_is_this/">Logi Options + requiring input monitoring - is this safe ...</a></li>
<li><a href="https://github.com/TomBadash/MouseControl">GitHub - TomBadash/MouseControl: A lightweight, open-source alternative to Logitech Options+ for remapping buttons on the Logitech MX Master 3S mouse · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对 Logitech Options Plus 的强烈不满，因其遥测和性能问题，形容其不可靠且侵犯隐私。用户推荐了多种替代方案，如 MacMouseFix、适用于 Linux 的 Piper、BetterTouchTool 和 SteerMouse，突显了对更好、更透明软件选项的共同需求。

**标签**: `#open-source`, `#privacy`, `#mouse-software`, `#macOS`, `#hardware`

---

<a id="item-6"></a>
## [Hammerspoon v2 将为 macOS 自动化从 Lua 切换至 JavaScript](https://github.com/Hammerspoon/hammerspoon) ⭐️ 7.0/10

Hammerspoon 的维护者在社区讨论中宣布，这个 macOS 自动化工具即将发布的版本 2 将把核心脚本语言从 Lua 切换为 JavaScript。 这一转变非常重要，因为 JavaScript 拥有更庞大、更多样化的开发者社区，这可能扩大 Hammerspoon 的吸引力，吸引新的贡献者，并更无缝地与现代基于 Web 的自动化工作流程集成。 Hammerspoon 充当底层 macOS API 与脚本引擎之间的桥梁，通过扩展暴露系统功能；版本 2 切换到 JavaScript 可能提升 Web 开发者的可访问性，但需要依赖 Lua 脚本的现有用户进行迁移工作。

hackernews · tosh · Mar 13, 18:34

**背景**: Hammerspoon 是一个用于 macOS 的开源桌面自动化工具，它使用 Lua 脚本来控制系统级功能，如窗口、屏幕和键盘。Lua 是一种轻量级、可嵌入的编程语言，专为应用程序中的效率和可扩展性而设计。JavaScript 是一种广泛使用的脚本语言，常见于 Web 开发，并越来越多地应用于自动化场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hammerspoon.org/">Hammerspoon</a></li>
<li><a href="https://notes.nicolasdeville.com/apps/hammerspoon/">Hammerspoon (macOS automation) | Nic's notes</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lua_scripting_language">Lua scripting language</a></li>

</ul>
</details>

**社区讨论**: 讨论显示出高参与度，用户热情分享实用用例，如自动化 Safari 标签页、创建自定义快捷键绑定和模拟平铺窗口管理器。维护者关于 v2 切换到 JavaScript 的公告引起了兴趣，混合了对工具现代化的兴奋和一些对从 Lua 迁移的担忧。

**标签**: `#Hammerspoon`, `#macOS`, `#automation`, `#JavaScript`, `#scripting`

---

<a id="item-7"></a>
## [Parallels 确认 MacBook Neo 可以在虚拟机中运行 Windows 11。](https://www.macrumors.com/2026/03/13/macbook-neo-runs-windows-11-vm/) ⭐️ 7.0/10

Parallels 已正式确认，苹果的平价机型 MacBook Neo 能够使用 Parallels Desktop 软件在虚拟机中运行 Windows 11。这一公告明确了该设备在 Apple silicon 上对 Windows 虚拟化的兼容性。 这很重要，因为它极大地提升了 MacBook Neo 在教育、企业等注重成本的细分市场中的吸引力，这些市场通常需要 Windows 软件。它可能通过提供一台能无缝运行 Windows 虚拟化的 macOS 设备，扰乱平价 PC 市场。 据报道，MacBook Neo 配备 8GB 内存，虽然 Windows 11 对虚拟机有 4GB 内存的最低要求，但用户可以在安装后调整内存分配，可能以更低内存运行。性能可能受设备硬件限制，尤其在资源密集型任务中。

hackernews · tosh · Mar 13, 14:11

**背景**: 虚拟机（VM）是一种基于软件的计算机系统仿真，通过虚拟化硬件资源，允许一个操作系统在另一个操作系统上运行。Parallels Desktop for Mac 是一款虚拟化软件，它使用管理程序技术，在 Mac（特别是 Apple silicon 机型）上运行 Windows 和其他操作系统。这使得 Mac 用户无需双启动即可访问 Windows 特定应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Virtual_machine">Virtual machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Parallels_Desktop_for_Mac">Parallels Desktop for Mac - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户赞扬了 MacBook Neo 在教育领域的潜力及其竞争性定价。主要担忧包括 Parallels 许可成本对平价设备来说过高，以及在 8GB 内存上运行虚拟机的实用性，不过有人指出 Windows 11 可以在低于官方最低要求的内存下运行。

**标签**: `#virtualization`, `#apple`, `#windows`, `#macbook`, `#parallels`

---

<a id="item-8"></a>
## [欧洲监管机构将对含战利品箱的游戏强制执行最低 16 岁年龄限制](https://www.bbc.com/news/articles/cge84xqjg5lo) ⭐️ 7.0/10

欧洲监管机构宣布，将对含有战利品箱的视频游戏实施最低 16 岁的年龄分级，旨在解决全欧洲范围内对类似赌博功能的担忧。 这具有重要意义，因为它代表了保护未成年人免受游戏中潜在赌博危害的重大监管举措，可能影响行业实践，并为全球类似行动开创先例。 该规定是设定最低年龄分级而非全面禁止，意味着含战利品箱的游戏仍可销售，但对年轻玩家的访问受限；然而，摘要中未提供具体的实施细节和执行时间表。

hackernews · gostsamo · Mar 14, 00:02

**背景**: 战利品箱是游戏内的一种功能，允许玩家购买随机虚拟物品包，通常使用真实货币，由于奖励基于机会，常被比作赌博。这种货币化策略因可能利用类似于赌博的心理机制而存在争议，导致全球监管审查日益加强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Loot_box">Loot box - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了复杂情绪：一些用户质疑监管战利品箱与像宝可梦卡牌这类实体收藏品的不一致性，而另一些人则争论术语，主张全面禁止儿童赌博，或建议对所有年龄段进行强制标签。

**标签**: `#gaming`, `#regulation`, `#loot-boxes`, `#gambling`, `#age-rating`

---

<a id="item-9"></a>
## [埃隆·马斯克在 AI 编码项目遇挫之际驱逐更多 xAI 创始人](https://www.ft.com/content/e5fbc6c2-d5a6-4b97-a105-6a96ea849de5) ⭐️ 7.0/10

埃隆·马斯克的人工智能公司 xAI 正面临内部不稳定，多名创始人在其 AI 编码计划遇到重大困难时被驱逐。据报道，这在开发用于编码任务的人工智能系统时遇到了挑战。 这很重要，因为它凸显了前沿 AI 研究中人才保留和理念对齐的挑战，这可能影响 xAI 与 OpenAI 和 Anthropic 等竞争对手的能力。内部动荡可能减缓创新并影响 AI 技术的发展。 关键细节包括对 AI 编码努力的关注，这是 xAI 战略的核心，以及像 Grokpedia 这样的项目被一些社区成员批评为分散注意力。此外，xAI 获取 Twitter 数据用于 AI 训练的价值存在争议。

hackernews · merksittich · Mar 13, 16:40

**背景**: xAI 是埃隆·马斯克创立的一家人工智能公司，旨在开发安全有益的 AI，常被定位为 OpenAI 和 Anthropic 的竞争对手。该公司一直致力于开发用于编码和其他任务的 AI 系统，利用来自 Twitter 等平台的数据。前沿 AI 研究涉及对顶级人才的激烈竞争，这些人才通常对 AI 发展持有强烈的理念信念。

**社区讨论**: 社区讨论强调了由于与埃隆·马斯克理念不合，xAI 吸引顶级人才的能力受到担忧。一些评论者批评像 Grokpedia 这样的项目是浪费资源，而其他人则争论 Twitter 数据对 AI 训练的价值，有一种观点认为 xAI 可能难以与理念更一致的公司竞争。

**标签**: `#AI`, `#xAI`, `#Elon Musk`, `#startup`, `#talent-acquisition`

---

<a id="item-10"></a>
## [瑞典电子政务源代码泄露，官方声称影响仅限于测试服务器。](https://darkwebinformer.com/full-source-code-of-swedens-e-government-platform-leaked-from-compromised-cgi-sverige-infrastructure/) ⭐️ 7.0/10

瑞典电子政务平台的完整源代码及部分个人数据从其服务提供商 CGI Sverige 的基础设施中被泄露。瑞典当局和 CGI 公司声称，被泄露的信息仅限于测试服务器。 此次泄露事件之所以重要，是因为它暴露了关键国家数字基础设施的内部架构，可能揭示可被利用的安全漏洞。即使仅限于测试服务器，其中也可能包含敏感的配置或数据模式，这会削弱公众对政府 IT 服务及其管理承包商安全性的信任。 除源代码外，据报道泄露的数据还包括公民个人可识别信息（PII）数据库和电子签名文档，这些正在被单独出售。值得注意的是，有社区成员指出，瑞典的个人身份号码通过 SPAR 数据库等官方渠道本就相对容易获取，这为部分泄露数据的敏感性提供了背景。

hackernews · tavro · Mar 13, 09:45

**背景**: 瑞典 eID 框架是一套用于实现安全电子身份验证和签名的技术规范，常用于政府服务。它定义了身份验证和数据交换的协议。SPAR（国家人口地址登记册）是瑞典的国家人口登记册，一个包含居民个人详细信息的中央数据库，许多官方服务都依赖它进行身份验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/swedenconnect/technical-framework/blob/master/00+-+Swedish+eID+Framework+-+Introduction.md">technical-framework/00 - Swedish eID Framework - Introduction.md at master · swedenconnect/technical-framework</a></li>
<li><a href="https://github.com/swedenconnect/technical-framework">GitHub - swedenconnect/technical-framework: Technical Specifications for the Swedish eID Framework</a></li>

</ul>
</details>

**社区讨论**: 社区讨论提供了重要的背景信息和质疑。一位用户澄清，瑞典的个人身份号码并非高度机密，可通过 SPAR 数据库获取。另一用户分享了官方淡化泄露事件影响范围的声明。有人对 PII 数据库被单独出售表示担忧，一位瑞典公民则对具体哪个政府平台受影响感到困惑。

**标签**: `#cybersecurity`, `#data-privacy`, `#government-it`, `#source-code-leak`

---

<a id="item-11"></a>
## [字节跳动 ArkClaw 实现 OpenClaw AI 代理的零安装使用](http://www.ruanyifeng.com/blog/2026/03/arkclaw.html) ⭐️ 6.0/10

字节跳动推出了 ArkClaw，这是开源 AI 代理 OpenClaw 的云 SaaS 版本，无需本地安装。用户可以通过字节跳动的 Coding Plan 订阅服务使用，其中 Pro 套餐提供长期使用权。 这一进展显著降低了使用高级 AI 自动化工具的门槛，使非技术用户也能轻松使用 OpenClaw。它顺应了基于云的 AI 服务趋势，提供 24/7 可用性，并易于与企业通信平台集成。 ArkClaw 托管在字节跳动的火山引擎云上，作为 Coding Plan 的一部分提供，其中 Lite 套餐提供 7 天试用，Pro 套餐才能持续使用。它具有简化的网页界面，支持与飞书、钉钉和企业微信集成，并允许设置定时自动化任务。

rss · 阮一峰的个人网站 · Mar 12, 08:01

**背景**: OpenClaw 是一个开源的自助 AI 助手，允许用户使用自然语言命令自动化任务。ArkClaw 是字节跳动基于 OpenClaw 的云版本，托管在其火山引擎平台上，提供了一个零安装的解决方案，用于持续在线操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://aicost.org/blog/arkclaw-2026-byte-dance-openclaw-cloud-ai-agent">ArkClaw 2026: ByteDance's Zero-Setup Cloud AI Agent That ...</a></li>

</ul>
</details>

**标签**: `#Artificial Intelligence`, `#Cloud Computing`, `#Software Tutorial`, `#AI Tools`, `#Chinese Technology`

---