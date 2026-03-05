---
layout: default
title: "Horizon Summary: 2026-03-05 (ZH)"
date: 2026-03-05
lang: zh
---

> From 17 items, 10 important content pieces were selected

---

1. [阿里通义千问团队核心研究员离职，Qwen 3.5 模型发布引关注](#item-1) ⭐️ 8.0/10
2. [NanoGPT Slowrun：有限数据与无限算力下的语言建模](#item-2) ⭐️ 8.0/10
3. [唐纳德·克努特承认 AI 解决其开放问题](#item-3) ⭐️ 8.0/10
4. [谷歌发布用于管理 Google Workspace 的命令行界面工具](#item-4) ⭐️ 7.0/10
5. [苹果宣布推出实惠型 MacBook Neo 笔记本电脑](#item-5) ⭐️ 7.0/10
6. [构建一个新的 Flash](#item-6) ⭐️ 7.0/10
7. [达里奥·阿莫代伊称 OpenAI 关于军事交易的信息是‘彻头彻尾的谎言’](#item-7) ⭐️ 7.0/10
8. [Moss：一个像素画布，其中每支画笔都是一个小程序](#item-8) ⭐️ 7.0/10
9. [警告：不要将未经审查的 AI 生成代码扔给团队](#item-9) ⭐️ 7.0/10
10. [谷歌发布低成本 AI 模型 Gemini 3.1 Flash-Lite，支持可调节思维水平。](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [阿里通义千问团队核心研究员离职，Qwen 3.5 模型发布引关注](https://simonwillison.net/2026/Mar/4/qwen/#atom-everything) ⭐️ 8.0/10

2026 年 3 月 4 日，阿里通义千问 AI 模型的首席研究员林俊阳及多位核心成员，包括负责代码开发的 Binyuan Hui、负责后训练研究的 Bowen Yu 和核心贡献者 Kaixin Li，宣布离职。此事发生在近期发布的 Qwen 3.5 系列开放权重模型之后，该系列始于 2026 年 2 月的 397B-A17B 模型。 这些高调离职可能严重阻碍开源 AI 模型的发展，因为通义千问团队在推进开放权重技术和开发如 Qwen 3.5 等竞争性模型方面发挥了关键作用。这也预示了阿里内部潜在的组织变动，可能影响其 AI 战略及更广泛的开源生态系统。 据报道，离职是由阿里的重组引发的，一位来自谷歌 Gemini 团队的新研究员被任命负责通义千问项目，但这一细节尚未确认。尽管资源少于竞争对手，该团队仍取得了显著成就，Qwen 3.5 模型因其大规模和在代理编码等任务中的能力而备受赞誉。

rss · Simon Willison · Mar 4, 15:50

**背景**: 通义千问（Qwen）是阿里云通义实验室开发的大型语言模型系列。开放权重模型是指其内部参数（权重）被公开的机器学习模型，允许透明度、修改和社区重用，但不一定包含完整的训练代码或数据，这与完全开源模型有所区别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/lets-code-future/open-weight-ai-models-what-they-are-and-why-openais-next-move-matters-f86fe481973a">Open - Weight AI Models : What They Are, and Why... | Medium</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-27B">Qwen/Qwen3.5-27B · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区对这些离职表示担忧，用户赞扬了 Qwen 3.5 的技术能力，特别是在代理编码任务中的表现，并指出其性能超出模型规模。讨论还强调了组织紧张关系，如研究团队与产品团队之间的冲突，并推测了经济影响及其他 AI 实验室可能进行的招聘。

**标签**: `#AI`, `#Open Source`, `#Machine Learning`, `#Alibaba`, `#Qwen`

---

<a id="item-2"></a>
## [NanoGPT Slowrun：有限数据与无限算力下的语言建模](https://qlabs.sh/slowrun) ⭐️ 8.0/10

NanoGPT Slowrun 项目启动，旨在研究在训练数据有限但计算资源充足约束下的语言建模，探索效率、架构选择和优化方法。它具体考察了如二阶优化器和集成多样性等方法来提高数据效率。 这很重要，因为它将焦点从规模驱动的 AI 训练转向数据高效范式，这可以揭示常被大数据集掩盖的基本模型设计洞见。它对数据稀缺或算力优先的领域，如专业 AI 应用或资源优化研究，具有影响。 关键细节包括使用 NanoGPT（一种极简 GPT 实现）作为基础模型，并探索了二阶优化器和架构变体以增强集成多样性。但需要注意的是，基准模型（modded-nanogpt）最初是针对运行速度优化的，这可能与数据效率目标不一致。

hackernews · sdpmas · Mar 4, 17:56

**背景**: NanoGPT 是 Andrej Karpathy 实现的一个简单、快速的代码库，用于训练中等规模的类 GPT 模型，旨在为实验和教育提供易用平台。Slowrun 指的是一种基准测试方法，旨在测试计算密集型想法，如重正则化和替代优化器，这些常在速度优化基准测试中被排除。这种范式通过优先探索而非训练时间效率，促进了数据高效学习的研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanoGPT">GitHub - karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs. · GitHub</a></li>
<li><a href="https://qlabs.sh/slowrun">NanoGPT Slowrun - Q</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示了积极参与实质性洞见，包括引用类似研究，如斯坦福大学关于有限数据预训练的论文。主要观点涉及对二阶优化器在数据效率中作用的疑问，对未被充分重视的集成多样性发现的赞赏，以及对基准模型选择的批评。还提出了关于元优化过程中可能过拟合的担忧。

**标签**: `#language-modeling`, `#machine-learning`, `#optimization`, `#benchmarking`, `#ai-research`

---

<a id="item-3"></a>
## [唐纳德·克努特承认 AI 解决其开放问题](https://simonwillison.net/2026/Mar/3/donald-knuth/#atom-everything) ⭐️ 8.0/10

唐纳德·克努特透露，Anthropic 三周前发布的混合推理模型 Claude Opus 4.6 解决了他几周来一直在研究的一个开放问题。这促使他重新考虑对生成式 AI 的看法。 此事意义重大，因为它展示了现代 AI 先进的推理和问题解决能力，甚至让像克努特这样的怀疑论者感到震惊，并可能加速 AI 在数学和计算研究中的应用。这标志着专家们对生成式 AI 在自动推理和创造性任务潜力的看法发生了转变。 Claude Opus 4.6 是一种混合推理模型，可以在标准和增强推理模式之间切换。克努特将 AI 的解决方案描述为'相当令人钦佩'，并称其为'自动推理的戏剧性进步'，该构造预计将收录在《计算机程序设计艺术》的未来版本中。

rss · Simon Willison · Mar 3, 23:59

**背景**: 唐纳德·克努特是传奇计算机科学家，以撰写多卷本系列著作《计算机程序设计艺术》而闻名。Claude Opus 4.6 是 Anthropic 开发的 AI 模型，具有混合推理能力，适用于编码和法规分析等复杂任务。自动推理指的是 AI 系统从事实中得出结论，这是人工智能研究中的一个核心问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.adafruit.com/2026/03/03/don-knuth-wrote-a-paper-thanking-claude-for-solving-an-open-math-problem/">Don Knuth wrote a paper thanking Claude for solving an open ...</a></li>
<li><a href="https://www.anthropic.com/claude/opus">Claude Opus 4.6 - Anthropic</a></li>

</ul>
</details>

**标签**: `#Donald Knuth`, `#Generative AI`, `#Claude`, `#AI Research`, `#Problem Solving`

---

<a id="item-4"></a>
## [谷歌发布用于管理 Google Workspace 的命令行界面工具](https://github.com/googleworkspace/cli) ⭐️ 7.0/10

谷歌发布了一款新的开源命令行界面工具，用于管理 Google Workspace，该工具可在 GitHub 上获取。它允许用户直接从终端执行管理任务。 该命令行界面工具可以通过自动化 Google Workspace 管理，显著提高管理员和开发人员的工作效率，支持企业环境中 DevOps 和基础设施即代码实践的日益普及。 该工具使用 OAuth 2.0 进行认证，但用户反馈设置困难，例如登录过程中选择范围时出现错误。尽管是 Rust 二进制文件，却通过 npm 分发，这引发了社区对其打包方式的讨论。

hackernews · gonzalovargas · Mar 5, 00:22

**背景**: Google Workspace 是一套基于云的生产力和协作工具套件，包括 Gmail、Drive 和 Docs 等。Google Workspace Admin SDK 提供了用于编程管理这些服务的 API，而 OAuth 2.0 是此类集成中用于授权的行业标准协议，可在不共享凭据的情况下实现安全访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postman.com/postman/google-api-workspace/collection/uc2iv4a/google-admin-sdk-api">️ Google Admin SDK API | Get Started - Postman</a></li>
<li><a href="https://oauth.net/2/">OAuth 2 . 0 — OAuth</a></li>

</ul>
</details>

**社区讨论**: 社区讨论体现了兴趣与挫折并存，用户对该工具的潜力表示兴奋，但反馈设置过程中遇到重大挑战，尤其是 OAuth 认证问题。技术建议包括实现 Streamable HTTP MCP 规范以提升客户端兼容性，并对使用 npm 分发 Rust 二进制文件感到好奇。

**标签**: `#google-workspace`, `#cli`, `#devops`, `#open-source`

---

<a id="item-5"></a>
## [苹果宣布推出实惠型 MacBook Neo 笔记本电脑](https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/) ⭐️ 7.0/10

苹果宣布推出 MacBook Neo，这是一款旨在比 MacBook Air 更实惠的新笔记本电脑型号，但在功能和规格上存在特定限制。 这很重要，因为它使苹果的生态系统对更广泛的受众更加亲民，可能挑战微软等竞争对手在预算笔记本电脑市场的地位，并影响软件开发向更低内存使用的方向发展。 关键细节包括仅支持 8 GB 统一内存、没有 MagSafe 或 Thunderbolt 支持，以及一个 USB-C 端口速度限制在 USB 2.0 的 480 Mb/s，不过它能以 60Hz 刷新率驱动 4K 显示器。

hackernews · dm · Mar 4, 14:16

**背景**: MacBook Air 是苹果公司的高端轻薄笔记本电脑，以性能和设计著称。苹果推出如 MacBook Neo 这样的更实惠型号，代表了其扩大市场覆盖和吸引价格敏感消费者的战略举措。

**社区讨论**: 社区讨论显示出不同的情绪：一些用户列出了与 MacBook Air 相比的技术妥协，另一些用户在价值上将其与微软 Surface 等 Windows 笔记本电脑进行有利比较，还有少数人指出如果 8 GB 内存成为常见基准，可能对软件开发有益。

**标签**: `#apple`, `#laptops`, `#hardware`, `#consumer-electronics`, `#development`

---

<a id="item-6"></a>
## [构建一个新的 Flash](https://bill.newgrounds.com/news/post/1607118) ⭐️ 7.0/10

HackerNews 上的讨论激发了人们对创建 Adobe Flash 现代替代品的兴趣，社区成员分享了关于 Flash 开发环境和技朧项目的轶事，包括一个能够导入和编辑旧版 .fla 文件的开源工具。 Flash 是早期网络和游戏开发的基石，实现了艺术家与程序员之间的独特协作，其衰落给交互式多媒体工具留下了空白；一个现代继任者可以保存遗留内容，同时推进创意工作流程。 提到的开源工具允许对 .fla 文件进行完整的创作和编辑，这在向后兼容性方面很罕见，但任何类似 Flash 的新平台都必须解决历史问题，如原始技术中固有的安全漏洞和性能限制。

hackernews · TechPlasma · Mar 4, 20:16

**背景**: Adobe Flash 是一个用于动画、游戏和网络应用程序的多媒体平台，依赖于 ActionScript 编程语言和 SWF 文件格式。ActionScript 演变为类似于 JavaScript 的 ECMAScript 实现，而 SWF 是一种基于矢量的格式，用于在网络上交付交互内容，但由于安全和性能问题，现已不再使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ActionScript">ActionScript - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SWF">SWF - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论反映了怀旧和积极的情绪，开发者们赞扬了 Flash 无缝集成编码者和艺术家的协作环境。关键观点包括关于 Flash 开发乐趣的轶事、构建 Flash 爬虫等技术挑战，以及对保持与旧文件兼容的开源工具的兴奋。

**标签**: `#Flash`, `#Web Development`, `#Game Development`, `#Legacy Systems`, `#Multimedia`

---

<a id="item-7"></a>
## [达里奥·阿莫代伊称 OpenAI 关于军事交易的信息是‘彻头彻尾的谎言’](https://techcrunch.com/2026/03/04/anthropic-ceo-dario-amodei-calls-openais-messaging-around-military-deal-straight-up-lies-report-says/) ⭐️ 7.0/10

Anthropic 首席执行官达里奥·阿莫代伊在一份报告中指控 OpenAI 就其与美国国防部的军事合同发表误导性声明，并将其信息称为‘彻头彻尾的谎言’。 这一公开指控凸显了 AI 行业内激烈的伦理和财务紧张关系，因为领先公司在安全性原则、利润丰厚的军事资金和竞争动态之间进行权衡。 争议焦点在于可能无法执行的合同条件，而 Anthropic 自身与监视公司 Palantir 的合作被指与其对军事用途的伦理立场相矛盾。

hackernews · SilverElfin · Mar 4, 23:51

**背景**: OpenAI 和 Anthropic 是前沿模型开发领域的主要 AI 研究实验室。Anthropic 强调以‘宪法 AI’确保安全性，而 OpenAI 则寻求各种商业和国防合作。军事 AI 合同常引发关于自主武器和监视的伦理辩论，影响行业信誉和监管审查。

**社区讨论**: 社区情绪存在分歧，讨论集中于推动军事交易的财务压力、对合同中伦理条件可执行性的怀疑，以及对 Anthropic 因与 Palantir 合作而被视为虚伪的批评。一些用户认为两家公司都在进行‘安全剧场’，而没有解决核心的 AI 对齐问题。

**标签**: `#AI ethics`, `#military AI`, `#industry news`, `#OpenAI`, `#Anthropic`

---

<a id="item-8"></a>
## [Moss：一个像素画布，其中每支画笔都是一个小程序](https://www.moss.town/) ⭐️ 7.0/10

Moss 是一款新的绘图工具，其中每支画笔都被实现为一个微型脚本，能够使用噪声、模式和笔触数据等参数在像素画布上进行程序化绘画。该工具最近被开发并在线分享，获得了高度参与，有 220 个赞和 25 条评论。 这很重要，因为它民主化了可编程艺术工具，使艺术家和程序员能够创建独特的、算法驱动的视觉效果，从而连接创意编程和数字艺术。它可能扩展生成艺术的边界，并影响创意工作流中编程工具的开发。 Moss 中的每支画笔脚本都可以访问整个画布状态，并利用笔触速度和压力等实时输入动态调整绘画行为，从而实现如真实喷罐或基于图案的绘图等效果。然而，创建自定义画笔需要基本的编程知识，这可能会限制非编码人员的可访问性。

hackernews · smusamashah · Mar 4, 10:21

**背景**: 创意编程涉及使用编程来创建视觉或交互艺术，通常利用算法和程序生成技术。像 Perlin 噪声这样的程序（一种梯度噪声）常用于生成艺术中，为数字画布产生有机的、随机的图案。基于脚本的绘画允许艺术家通过代码定义画笔行为，例如在 JavaScript 的 p5.js 库中所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perlin_noise">Perlin noise - Wikipedia</a></li>
<li><a href="https://www.ideo.com/journal/painting-with-code">Painting with Code</a></li>

</ul>
</details>

**社区讨论**: 社区对 Moss 表达了热情，用户赞扬其概念并建议添加时间轴录制、跟踪画笔使用情况以及添加 Shift 键用于直线绘画等功能。一些用户将其与 Aseprite 和 Procreate 等工具进行比较，而其他人则设想利用其可编程性进行创意开发。

**标签**: `#creative-coding`, `#digital-art`, `#programming-tools`, `#software-engineering`

---

<a id="item-9"></a>
## [警告：不要将未经审查的 AI 生成代码扔给团队](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/#atom-everything) ⭐️ 7.0/10

Simon Willison 明确指出，提交包含作者本人未亲自审查的 AI 生成代码的大型拉取请求是一种反模式。他强调初始审查是提交者的责任，并列举了良好的“代理工程”拉取请求应具备的具体特征。 这很重要，因为它解决了 AI 辅助开发中一个日益增长的矛盾点，旨在维护团队效率和协作信任。如果开发者逃避审查自己 AI 辅助工作的责任，就是将认知负担转嫁给同事并浪费他们的时间，从而破坏了该工具潜在的生产力提升价值。 Willison 建议提供个人审查的证据，例如手动测试记录、实现选择的说明或截图。一个关键细节是，即使是 AI 生成的、看似令人信服的拉取请求描述，也必须由人类作者进行审查和验证。

rss · Simon Willison · Mar 4, 17:34

**背景**: 代理工程是一种软件开发范式，其中人类定义目标和约束条件，AI 代理在结构化的人类监督下自主地规划、编写和测试代码。该术语由 OpenAI 的 Andrej Karpathy 提出，它代表了从简单的代码补全或建议工具（如 GitHub Copilot 聊天）向更自主的编码代理的演进。它强调工程师的角色从编写每一行代码转变为设计系统并提供高质量的监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>
<li><a href="https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/">Writing about Agentic Engineering Patterns | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#agentic-engineering`, `#code-review`, `#software-engineering`, `#AI-assistance`

---

<a id="item-10"></a>
## [谷歌发布低成本 AI 模型 Gemini 3.1 Flash-Lite，支持可调节思维水平。](https://simonwillison.net/2026/Mar/3/gemini-31-flash-lite/#atom-everything) ⭐️ 7.0/10

谷歌发布了 Gemini 3.1 Flash-Lite 模型，定价为每百万输入 token 0.25 美元，每百万输出 token 1.5 美元，仅为 Gemini 3.1 Pro 价格的八分之一。该模型还引入了对四种不同思维水平的支持，从最低到最高。 这次大幅降价使得 AI 在代理任务和数据提取等高容量应用中更易获取，可能推动其在成本敏感项目中的采用。可调节的思维水平让开发者能在推理深度和预算之间取得平衡，从而在不同场景中实现更高效的使用。 Gemini 3.1 Flash-Lite 是一个多模态模型，可接受文本、图像、语音和视频输入，但仅输出文本，其上下文窗口为 100 万个 token，知识截止至 2025 年 1 月。其思维水平可配置以整合外部工具和实时信息，从而增强推理能力。

rss · Simon Willison · Mar 3, 21:53

**背景**: 在 AI 语言模型中，token 是用于处理和定价的文本单位，输入和输出 token 通常按不同费率收费，输出 token 往往更昂贵。思维水平指的是模型在不同深度（从简单到复杂）进行推理的能力，这会影响响应质量和计算成本。谷歌的 Gemini 模型是为从对话到分析等多种任务设计的多模态 AI 系统，而基于 token 的定价是行业内扩展使用的常见做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview">Gemini 3.1 Flash-Lite Preview - Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/thinking">Gemini thinking | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Google Gemini`, `#Cost Reduction`, `#Machine Learning`

---