---
layout: default
title: "Horizon Summary: 2026-06-17 (ZH)"
date: 2026-06-17
lang: zh
---

> From 32 items, 11 important content pieces were selected

---

1. [机械手表机制的交互式深度解析](#item-1) ⭐️ 9.0/10
2. [GrapheneOS 已移植至 Android 17，官方版本即将发布](#item-2) ⭐️ 8.0/10
3. [本地模型运行：够好了还是仍痛苦？](#item-3) ⭐️ 8.0/10
4. [Qwen 发布机器人基础模型套件](#item-4) ⭐️ 8.0/10
5. [Bash 的 /dev/tcp 让你无需 curl 即可发起 HTTP 请求](#item-5) ⭐️ 7.0/10
6. [Hacker News 热议 JWT 用于 Web 会话的安全性](#item-6) ⭐️ 7.0/10
7. [AI 是否正在扼杀自助类非虚构书籍？](#item-7) ⭐️ 7.0/10
8. [改用 Broadcom SFP+ 模块实现 10GbE 网络](#item-8) ⭐️ 7.0/10
9. [《杀戮尖塔 2》自定义 PRNG 修复跨平台种子一致性问题](#item-9) ⭐️ 7.0/10
10. [荷兰宣布主权语言模型 GPT-NL](#item-10) ⭐️ 6.0/10
11. [雅克剃毛很有趣：2019 年的反思](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [机械手表机制的交互式深度解析](https://ciechanow.ski/mechanical-watch/) ⭐️ 9.0/10

巴托什·切哈诺夫斯基（Bartosz Ciechanowski）的文章《机械手表》通过逐步交互式可视化，展示了机械手表的工作原理，涵盖发条、齿轮系、擒纵机构和摆轮。该文于 2022 年发布，仅使用纯 HTML、CSS 和 JavaScript，无需任何框架即可提供教育体验。 这篇文章代表了在线技术教育的最高水准，让复杂的机械工程概念对广泛受众变得易于理解。其纯代码实现确保了长期兼容性和跨设备可用性，与现代网页的臃肿形成鲜明对比。 该文章完全交互式，读者可以 3D 探索每个部件并观察其互动方式。它在 Hacker News 上获得了超过 630 个点赞和 114 条评论，用户称赞其教学清晰度和技术工艺水平。

hackernews · razin · Jun 16, 11:26

**背景**: 机械手表由发条提供动力，上链时储存能量。擒纵机构以受控步骤释放能量，使齿轮系按精确速率前进。摆轮和游丝摆动以调节计时，类似于时钟中的摆锤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Escapement">Escapement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mainspring">Mainspring - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Balance_wheel">Balance wheel - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对文章的教育质量和纯技术表达表示高度赞赏。一位读者受文章启发，在现实中制作了手表机芯的分解展示；另一位则指出作者使用纯代码，即使在旧设备上也能运行。一位教师称赞其逐步解释是罕见的教学成就。

**标签**: `#interactive-article`, `#mechanical-engineering`, `#educational`, `#visualization`, `#horology`

---

<a id="item-2"></a>
## [GrapheneOS 已移植至 Android 17，官方版本即将发布](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) ⭐️ 8.0/10

注重隐私的移动操作系统 GrapheneOS 已成功移植至 Android 17，这是该项目的一个重要里程碑。官方版本预计很快发布，将强化版操作系统带到最新的 Android 版本上。 此次移植确保 GrapheneOS 用户能够在不牺牲隐私的前提下受益于最新的 Android 安全补丁和功能。作为最知名的安全优先 Android 衍生系统之一，保持及时更新对其注重隐私的用户群体至关重要。 该移植基于 Android 开源项目（AOSP）17 版本，并应用了 GrapheneOS 广泛的加固和攻击面缩减措施。用户可预期与现有 Android 应用的兼容性，因为 GrapheneOS 保持完整的 Android 应用兼容性。

hackernews · Cider9986 · Jun 16, 20:34

**背景**: GrapheneOS 是一个非营利、开源的移动操作系统，专注于对 AOSP 进行隐私和安全增强。它适用于 Google Pixel 设备以及未来的 Motorola 设备，截至 2026 年 4 月拥有约 40 万活跃用户。该项目强调纵深防御、应用沙箱改进和权限模型加固。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**社区讨论**: 社区对该移植表现出强烈热情，用户分享了使用 GrapheneOS 的长期积极体验。部分用户指出与原生 Android 相比缺少一些小功能，例如光标导航手势，而另一些用户则强调需要 Pixel 手机以外的设备支持，例如即将到来的 Motorola 兼容性。整体情绪非常正面，许多人赞扬 GrapheneOS 提供的隐私和控制力。

**标签**: `#GrapheneOS`, `#Android`, `#Security`, `#Privacy`, `#Open Source`

---

<a id="item-3"></a>
## [本地模型运行：够好了还是仍痛苦？](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) ⭐️ 8.0/10

一篇最新博文认为本地运行大型语言模型现在已成为可行选择，但社区讨论指出了在性能、量化质量和用户体验方面与云端模型相比依然存在的权衡。 这一讨论之所以重要，是因为随着本地模型的改进，它们可能通过为许多用户和工作负载提供经济高效、私密的替代方案，从而颠覆云端人工智能订阅模式。 用户报告称，像 Qwen 27B 和 Gemma 31B 这样的密集型模型智能但速度慢，而混合专家（MoE）模型如 Gemma 26B 和 Qwen 35B 较快但容易出错。运行在 4 位量化时，常会削弱工具调用能力。

hackernews · jfb · Jun 16, 14:36

**背景**: 量化是一种通过降低数值精度来减小模型大小的技术，使得更大模型能在消费级硬件上运行，但会牺牲一定准确性。本地模型在用户自己的机器上运行，提供隐私保护和更低的持续成本，但历史上在质量上落后于云端 API。混合专家（MoE）模型每个词元只激活部分参数，用原始智能换取速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/quantization-for-large-language-models">Quantization for Large Language Models (LLMs): Reduce AI ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同看法：一些人认为本地模型仍然缓慢或容易出错，而另一些人则更喜欢本地模型的手感和个性，而非 Claude Sonnet 等云端模型。人们就成本效益权衡展开辩论，一些人认为本地模型最终将减少对昂贵云端订阅的需求。

**标签**: `#local-llm`, `#AI`, `#machine-learning`, `#open-source`, `#llm-deployment`

---

<a id="item-4"></a>
## [Qwen 发布机器人基础模型套件](https://qwen.ai/blog?id=qwen-robotsuite) ⭐️ 8.0/10

阿里巴巴 Qwen 团队发布了 Qwen-Robot Suite，这是一套包含三个基础模型的系列——Qwen-RobotNav、Qwen-RobotManip 和 Qwen-RobotWorld——基于超过 38,000 小时的开源数据训练，并于 2026 年 6 月 16 日宣布。 该套件将语言理解与机器人导航、操作和世界建模相连接，有望加速用于制造、服务和国防应用的集成机器人系统的开发。 这三个模型将语言与不同领域的物理动作对齐；该套件在 RoboChallenge 基准测试中名列前茅，并正在进入企业试点测试，以解决中国机器人生态系统中的硬件碎片化问题。

hackernews · ilreb · Jun 16, 13:15

**背景**: 物理世界智能指的是在现实世界中运行和交互的 AI 系统，结合了感知、决策和物理执行。像 Qwen-Robot Suite 这样的基础模型旨在提供可适应各种机器人平台的通用能力（导航、操作、世界建模），从而超越狭窄的单任务模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen-robotsuite">Qwen-Robot Suite: A Foundation Model Suite for Physical World ...</a></li>
<li><a href="https://chinabizinsider.com/alibabas-qwen-enters-robotics-with-embodied-ai-suite-to-tackle-hardware-fragmentation/">Alibaba Qwen-Robot: 3 Embodied AI Models Target Robotics</a></li>
<li><a href="https://robotsbeat.com/alibaba-qwen-robot-suite-embodied-ai-models-robotnav-robotmanip-robotworld/">Alibaba Launches Qwen Robot Suite, Its First AI Model Family ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍积极，用户称赞 Qwen 的持续交付能力，并猜测快速量产（例如每年 100 万台）以及在类人机器人领域的战略优势，尽管关于实时预测（例如接住球）的一些技术问题仍悬而未决。

**标签**: `#Robotics`, `#Foundation Models`, `#AI`, `#Qwen`, `#Physical World Intelligence`

---

<a id="item-5"></a>
## [Bash 的 /dev/tcp 让你无需 curl 即可发起 HTTP 请求](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) ⭐️ 7.0/10

Marek Šuppa 的一篇博客文章展示了如何使用 Bash 内建的 /dev/tcp 特性，在不依赖 curl 或 wget 等外部工具的情况下发起原始 HTTP 请求。该技术通过 exec 打开 TCP 连接，并用 printf 发送格式正确的 HTTP 头。 这个技巧在调试以及 curl 或 wget 不可用的受限环境（如精简 Docker 容器）中很有价值。但由于它不能正确解析 HTTP 响应，面对真实服务器时很容易出错，因此不适用于生产环境。 /dev/tcp 路径并非真实设备文件，而是 Bash 内部处理的重定向，因此 ls /dev/tcp 找不到任何内容，从其他 shell 执行 cat /dev/tcp/... 会失败。正确的 HTTP 请求需要使用 \r\n 作为换行符，添加 Authorization 等头信息需要在最后的空行之前增加以 \r\n 结尾的行。

hackernews · mrshu · Jun 16, 16:40

**背景**: Bash 包含一个内建的 /dev/tcp 功能（编译时需启用 --enable-net-redirections），允许通过文件描述符打开 TCP 连接。该功能在某些发行版或安全环境中常被禁用，但当可用时，它可以用于基本的网络连通性检查或简单的 HTTP 请求。这是一个底层的套接字接口，而非 HTTP 客户端，用户必须手动构造有效的 HTTP/1.1 消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/">Making HTTP requests from a container that has no curl, using bash /dev/tcp · Marek Šuppa</a></li>
<li><a href="https://rednafi.com/misc/http_requests_via_dev_tcp/">HTTP requests via /dev/tcp | Redowan's Reflections</a></li>
<li><a href="https://unix.stackexchange.com/questions/436200/different-ways-to-use-dev-tcp-host-port-command-and-where-to-find-manual-pages">bash - Different ways to use /dev/tcp/host/port command and ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对该技巧在调试和精简环境中的优雅性表示兴奋，mrshu 和 simonw 等用户提供了具体示例。但 basilikum 强烈警告说，这并非真正的 HTTP 客户端，在自动化使用中会出错，因为它不能正确解析 HTTP 响应或处理真实世界中的边界情况。

**标签**: `#bash`, `#http`, `#networking`, `#shell`, `#dev/tcp`

---

<a id="item-6"></a>
## [Hacker News 热议 JWT 用于 Web 会话的安全性](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452) ⭐️ 7.0/10

Hacker News 上一场获得 250 多分和 149 条评论的讨论，就 JSON Web Token（JWT）在基于浏览器的用户会话中的安全性展开了辩论，许多评论者认为 JWT 并非天生不安全，并强调了正确的使用场景，例如服务间通信以及结合刷新机制的短期令牌。 这场讨论之所以重要，是因为 JWT 被广泛用于身份验证，而对其安全性的误解可能导致过度依赖或全盘否定；理解其中的权衡——例如算法混淆攻击、令牌生命周期限制以及吊销策略——对于构建安全的 Web 应用至关重要。 评论者强调，JWT 具有防篡改性，并且当使用适当的签名方法（RSA 或 ECDSA）和短生命周期（例如 5–15 分钟）并配合刷新令牌时是安全的。讨论还指出，当服务器信任 JWT 的 'alg' 头而不强制使用固定算法时，算法混淆攻击是真实存在的威胁。

hackernews · dzonga · Jun 16, 16:49

**背景**: JSON Web Token (JWT) 是一种紧凑、自包含的格式，用于在各方之间传输声明，通常用于身份验证和会话管理。然而，它们存在已知的漏洞，尤其是算法混淆攻击，攻击者更改 'alg' 头以绕过签名验证；此外，撤销令牌很困难，因为令牌在过期之前可能一直有效。正确的缓解措施包括使用强算法、限制令牌生命周期、采用刷新令牌以及维护黑名单或吊销列表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://portswigger.net/web-security/jwt/algorithm-confusion">Algorithm confusion attacks | Web Security Academy - PortSwigger</a></li>
<li><a href="https://supertokens.com/blog/revoking-access-with-a-jwt-blacklist">Revoke Access Using a JWT Blacklist | SuperTokens</a></li>

</ul>
</details>

**社区讨论**: 评论呈现出微妙的观点分歧：有人主张 JWT 在服务间通信且正确配置时是安全的，而另一些人则警告普遍滥用（例如没有吊销机制的长期令牌）会带来实际风险。几位评论者质疑 JWT 根本性不安全的说法，并指出 Auth0 和 AWS STS 是基于 JWT 的安全系统的例子。

**标签**: `#JWTs`, `#authentication`, `#security`, `#web development`, `#session management`

---

<a id="item-7"></a>
## [AI 是否正在扼杀自助类非虚构书籍？](https://tim.blog/2026/06/12/has-ai-already-killed-nonfiction/) ⭐️ 7.0/10

Tim Ferriss 博客上的一篇文章及 Hacker News 的讨论探讨了 AI 是否正在减少自助类非虚构书籍的需求，评论者提出了其他解释，包括行业动态、有声书趋势以及内容质量批评。 这很重要，因为自助类书籍是一个重要的出版类别；如果 AI 取代了它，可能会重塑出版行业、内容消费习惯以及人们寻求个人发展建议的方式。 讨论指出，观察到的下降可能仅限于纸质书，而非虚构类有声书的销售额显著增长，一些读者认为 LLM 生成的摘要比传统的自助书籍更简洁。

hackernews · imakwana · Jun 16, 17:11

**背景**: 自助类非虚构书籍长期以来一直是一个受欢迎的体裁，提供有关生产力、人际关系和幸福感的建议。像 ChatGPT 这样的大型语言模型（LLM）的兴起，使读者能够即时获得提炼后的建议，可能减少阅读整本书的需求。然而，行业动态和形式转变（如有声书）等其他因素也在起作用。

**社区讨论**: 评论者提出了多种观点：有人批评自助行业是一个交叉推广的‘黑帮’，有人强调转向有声书的趋势以及 LLM 提炼内容在剔除‘冗赘填充物’方面的吸引力，还有评论者提到 Anna's Archive 将 LLM 训练与销量下降联系起来。

**标签**: `#AI`, `#self-help`, `#publishing`, `#nonfiction`, `#industry analysis`

---

<a id="item-8"></a>
## [改用 Broadcom SFP+ 模块实现 10GbE 网络](https://www.gilesthomas.com/2026/06/10g-ethernet-switching-to-broadcom-sfp-plus) ⭐️ 7.0/10

一篇博客文章记录了作者改用 Broadcom SFP+ 模块以实现 10 Gigabit Ethernet 的个人经验，重点介绍了家庭网络中硬件兼容性的实际考量。 这一亲身实践的报道意义重大，因为 10GbE 在家庭网络中的普及仍然缓慢，而从铜缆转向光纤的趋势正由功耗和散热问题所驱动。 作者改用了一款 Broadcom SFP+ 模块——一种用于高速网络的小型可插拔收发器，并指出某些模块可能缺少温度诊断功能。

hackernews · gpjt · Jun 16, 17:48

**背景**: SFP+ 模块是 10 Gigabit Ethernet 连接的关键组件，可将电信号转换为光信号用于光纤或铜缆。家庭网络在采用超过 1 Gbps 的速度方面一直进展缓慢，但 Ubiquiti SFP Wizard 等工具允许重新编程模块以实现更好的兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://store.ui.com/us/en/products/uacc-sfp-wizard">SFP Wizard - Ubiquiti Store United States</a></li>
<li><a href="https://docs.broadcom.com/doc/957414A4142CC-DS">BCM957414A4142CC Data Sheet - Broadcom</a></li>
<li><a href="https://www.wolontek.com/sfp-modules-guide-types-compatibility/">The Ultimate Guide to SFP Modules (2026): Types, Speeds ...</a></li>

</ul>
</details>

**社区讨论**: 评论者主张在新安装中采用光纤而非铜缆以降低功耗和散热，另一些则指出家庭网络速度自 2000 年代中期以来一直停滞不前。部分用户分享了使用 Ubiquiti SFP Wizard 等设备重新编程 SFP 模块的经验。

**标签**: `#10GbE`, `#SFP+`, `#networking`, `#fiber`, `#ethernet`

---

<a id="item-9"></a>
## [《杀戮尖塔 2》自定义 PRNG 修复跨平台种子一致性问题](https://tck.mn/blog/correlated-randomness-sts2/) ⭐️ 7.0/10

Andy Tockman 的文章解释了《杀戮尖塔 2》如何实现自定义伪随机数生成器（PRNG），以规避依赖 C# System.Random 所导致的关联随机性和跨平台种子不一致问题。 这确保了种子在所有平台上产生相同的游戏结果，并随时间保持稳定，防止基于可预测 RNG 模式的利用，从而保证玩家无论使用何种设备都能获得公平体验。 在《杀戮尖塔 1》中，桌面版和移动版对同一种子产生了不同的序列，因为 System.Random 的实现因平台而异；新的 PRNG 还避免了简单顺序种子常见的关联性问题。

hackernews · rdmuser · Jun 16, 09:46

**背景**: 伪随机数生成器（PRNG）是一种算法，在给定种子时产生近似真随机的确定性序列。在《杀戮尖塔》这样的游戏中，种子控制着遭遇战、奖励和地图布局的流程生成。许多游戏依赖标准库的 PRNG，但 C# System.Random 无法在不同的运行时或平台上保证一致行为，导致种子不兼容。自定义 PRNG（如 PCG32）提供确定性、高质量的随机性且可移植。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tck.mn/blog/correlated-randomness-sts2/">Correlated randomness in Slay the Spire 2 - Andy Tockman</a></li>
<li><a href="https://news.ycombinator.com/item?id=48552844">Correlated randomness in Slay the Spire 2 | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pseudorandom_number_generator">Pseudorandom number generator - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者赞赏这篇技术深度文章，有人提到其他游戏中类似的问题，例如《我的世界》中基于种子的粘土与钻石关联。一位评论者指出 Godot 内置的 GDScript RNG 使用 PCG32，可以避免此问题，但《杀戮尖塔 2》使用了带有 System.Random 的 C#绑定。另一位评论者提到了原版《杀戮尖塔》中发现的一个不可获胜的种子，引发了对理论上的“RNG 地狱”场景的讨论。

**标签**: `#PRNG`, `#game development`, `#C#`, `#randomness`, `#Slay the Spire`

---

<a id="item-10"></a>
## [荷兰宣布主权语言模型 GPT-NL](https://www.tno.nl/en/digital/artificial-intelligence/gpt-nl/) ⭐️ 6.0/10

荷兰研究机构 TNO 宣布了 GPT-NL，这是一个专为荷兰开发的主权大语言模型。该项目旨在构建尊重荷兰语言和价值观的国家级 AI 模型。 此次公告重新引发了关于各国是否应从头构建自己的语言模型，还是利用现有开源模型的争论。其结果可能影响欧洲各国的 AI 战略及公共研究资金的分配。 GPT-NL 尚未公布技术细节，而类似的主权 LLM 项目（如瑞典的 GPT-SW3）曾因成本高、影响力有限而受到批评。该项目在荷兰科技界日益受到质疑，一些人认为应转而微调现有的开源模型。

hackernews · root-parent · Jun 16, 17:54

**背景**: 主权大语言模型（LLM）是指由国家或政府开发的 AI 模型，旨在确保对数据的控制、符合当地语言和文化规范，以及独立于外国 AI 供应商。支持者认为这类模型能保护国家利益并促进本地创新，而批评者则指出其成本高昂，且开源模型已在许多任务上表现出色且快速进步。近期基准测试中，Qwen、Kimi 等开源模型已与专有模型持平甚至超越，这引发了对完全自主开发必要性的质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2503.04745v1">Sovereign Large Language Models: Advantages, Strategy and ...</a></li>
<li><a href="https://www.nvidia.com/en-us/lp/industries/global-public-sector/sovereign-ai-technical-overview/">A Technical Guide to Building Sovereign AI Models - NVIDIA</a></li>
<li><a href="https://www.vellum.ai/open-llm-leaderboard">Open Source LLM Leaderboard 2026 — Compare Open-Weight Models</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一。一些评论者支持该举措，认为小国用自己的语言构建模型并保持研究多样性至关重要。然而，许多人也表示怀疑，引用瑞典的 GPT-SW3 作为资源浪费的前车之鉴，并认为各国应在本国安全基础设施上托管和微调现有开源模型。有具体批评指向一篇质疑该项目价值的荷兰科技新闻报道。

**标签**: `#sovereign AI`, `#language models`, `#Netherlands`, `#national LLM`, `#AI policy`

---

<a id="item-11"></a>
## [雅克剃毛很有趣：2019 年的反思](https://parksb.github.io/en/article/32.html) ⭐️ 6.0/10

这篇 2019 年的反思文章探讨了为什么雅克剃毛对软件工程师来说可以是一项愉快且有回报的活动，并在 Hacker News 上获得了 212 分和 63 条评论的热烈讨论，大家分享了各自的亲身经历。 这次讨论证实了雅克剃毛——常被视为浪费时间的行为——实际上可以激发创造力、加深理解并带来长期的满足感。最近的评论还指出，AI 工具正在降低此类旁支任务的成本，使这个话题愈发具有现实意义。 这篇随笔写于 2019 年，但至今仍具有高度相关性，Hacker News 上的热烈讨论便证明了这一点。评论中有人描述了持续多年的雅克剃毛项目，比如长达 30 年的游戏引擎开发之旅，也有人提到利用 AI 降低了构建工具的门槛。

hackernews · parksb · Jun 16, 14:26

**背景**: 雅克剃毛是软件工程中的一个口语化术语，指为了达成一个更大目标而必须完成的一系列看似不相关的子任务。该词源自动画片《莱恩和史丁比》中的一集，后在编程文化中得到推广。它常用来描述被细小但必要的任务带偏，最终又绕回原定目标的那种感觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yak_shaving">Yak shaving</a></li>
<li><a href="https://en.m.wiktionary.org/wiki/yak_shaving">yak shaving - Wiktionary, the free dictionary</a></li>

</ul>
</details>

**社区讨论**: 评论者们分享了非常个人化的雅克剃毛故事：一位用户描述了自己长达 30 年的历程，从 QBasic 游戏演变为混合 C/Lua 引擎；另一位指出 AI 大幅降低了此类旁支任务的成本；还有一位认为，“雅克剃毛羞耻”会限制工程创造力，因为它阻碍了在现有模式之外的探索。

**标签**: `#yak shaving`, `#software engineering`, `#productivity`, `#hacker culture`, `#personal projects`

---