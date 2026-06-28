---
layout: default
title: "Horizon Summary: 2026-05-22 (ZH)"
date: 2026-05-22
lang: zh
---

> From 24 items, 13 important content pieces were selected

---

1. [Freenet 以 WebAssembly 去中心化应用重新发布](#item-1) ⭐️ 8.0/10
2. [西雅图盾牌网络引隐私担忧](#item-2) ⭐️ 8.0/10
3. [Google Antigravity 更名引发开发者强烈不满](#item-3) ⭐️ 8.0/10
4. [Project Hail Mary 恒星导航图](#item-4) ⭐️ 7.0/10
5. [运行 10 年的 Ubuntu 16.04 博客迁移至 FreeBSD](#item-5) ⭐️ 7.0/10
6. [开发者用 Gemma4-31B 在 MacBook 上本地索引一年视频](#item-6) ⭐️ 7.0/10
7. [Python 3.15 被忽视的特性：延迟导入、同步原语、计数器运算](#item-7) ⭐️ 7.0/10
8. [1945 年三位一体核试验失传影像得以修复，清晰度前所未有](#item-8) ⭐️ 7.0/10
9. [Waymo 因自动驾驶车驶入洪水暂停服务](#item-9) ⭐️ 7.0/10
10. [Kagi 搜索助力低视力用户](#item-10) ⭐️ 6.0/10
11. [Spotify 将为超级粉丝预留演唱会门票](#item-11) ⭐️ 6.0/10
12. [BBEdit 16：经典 macOS 文本编辑器的新大版本](#item-12) ⭐️ 6.0/10
13. [财富正向 AI 集中](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Freenet 以 WebAssembly 去中心化应用重新发布](https://freenet.org/) ⭐️ 8.0/10

全新的 Freenet 是对原始点对点网络的彻底重新设计，于 2024 年 12 月上线，使用 WebAssembly 合约定义状态验证和同步，并附带早期应用如 River（去中心化群聊）和 Delta（去中心化内容管理系统）。 这一重新设计以现代技术复兴了历史性的点对点项目，使得去中心化应用可以直接从网络下载并在浏览器中运行，从而减少对中心化服务器和大型科技基础设施的依赖。 每个合约必须定义一个可交换的合并操作，使状态更新像病毒一样在网络中传播，并在数秒内达到全局一致性。应用在客户端运行，通过 WebSocket 连接本地 Freenet 节点，而非远程 API。

hackernews · sanity · May 21, 14:34

**背景**: 最初的 Freenet（现更名为 Hyphanet）是 2000 年代初期的点对点网络，专注于匿名通信和抗审查。新版本将其重新构想为一个全局去中心化的键值存储，其中键是 WebAssembly 合约。WebAssembly 是一种二进制指令格式，能在浏览器及其他环境中以接近原生的速度运行。可交换合并操作是冲突自由复制数据类型（CRDT）的核心概念，使得无需中心协调即可实现最终一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://freenet.org/">Freenet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_censorship_circumvention">Internet censorship circumvention - Wikipedia</a></li>
<li><a href="https://medium.com/@sairaju.atukuri123/crdts-explained-simply-how-distributed-systems-stay-consistent-without-locks-b331a9a2d115">CRDTs Explained Simply: How Distributed Systems Stay... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些人对使用 WebAssembly 和类似 CRDT 的合并函数的技术创新表示赞赏，而另一些人则强烈批评项目治理，称原始开发团队在未事先讨论的情况下被董事会决定边缘化。其它技术讨论包括对幽灵密钥及声誉中心化的担忧，以及关于使用更新日志等替代状态同步方法的建议。

**标签**: `#p2p`, `#decentralized`, `#webassembly`, `#freenet`, `#distributed-systems`

---

<a id="item-2"></a>
## [西雅图盾牌网络引隐私担忧](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) ⭐️ 8.0/10

Prism Reports 的调查披露，西雅图警方运营的情报共享网络“西雅图盾牌”（Seattle Shield）包含亚马逊、Facebook 等大型企业以及 ICE 等联邦机构，引发对大规模监控和隐私侵犯的担忧。 此事意义重大，因为它凸显了私营部门监控与执法机构日益融合的趋势，可能导致未经适当监督的公民监视，并在科技行业引发公民自由讨论。 西雅图盾牌的官方使命是反恐情报共享，但批评者认为它被用于监控抗议活动和活动人士，且一些成员如科学教会和美国海军已退出该网络。

hackernews · root-parent · May 21, 17:55

**背景**: 西雅图盾牌是一个类似融合中心的本地网络，旨在促进西雅图警察局与私营实体之间的信息共享。此类网络是后 9/11 时期情报基础设施的一部分，但往往缺乏透明度和问责机制。科技巨头和移民执法机构的参与引发了对边缘社区数据收集的具体担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/">Amazon, Facebook, ICE have access to Seattle police ...</a></li>
<li><a href="https://seattleshield.org/PageMenuSwitch2.aspx?AspxAutoDetectCookieSupport=1">Seattle Shield</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些人批评报道是耸人听闻的点击诱饵，而另一些人则对助长监控表示担忧，并敦促科技工作者抵制。少数人则为该网络辩护，认为它是一个合法的商业社区守望项目。

**标签**: `#privacy`, `#surveillance`, `#police`, `#technology-ethics`, `#civil-liberties`

---

<a id="item-3"></a>
## [Google Antigravity 更名引发开发者强烈不满](https://www.0xsid.com/blog/antigravity-bait-n-switch) ⭐️ 8.0/10

Google 对其 Antigravity 开发者工具进行了品牌重塑，覆盖了原有安装，迫使现有用户经历破坏性的迁移过程，导致工作流程和设置损坏。 这种“诱饵换货”式操作削弱了开发者对 Google 产品一致性的信任，并突显了依赖那些可能不顾现有用户而突然彻底改造的工具所存在的风险。 用户报告称，更新在未警告的情况下覆盖了旧版 Antigravity IDE，需要手动重新配置；一位开发者记录下了长达 90 分钟的迁移过程；社区贡献者发布了一个 Python 脚本，用于在 Mac 上自动恢复。

hackernews · ssiddharth · May 21, 13:50

**背景**: Google Antigravity 是一个由 AI 驱动的集成开发环境（IDE），利用 Gemini 模型实现智能体式软件开发。它于 2025 年 11 月发布，旨在将开发任务委托给自主 AI 代理。最近的品牌重塑似乎转移了产品重点，给现有用户留下了破损的迁移路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>
<li><a href="https://antigravity.google/">Google Antigravity - Build the new way</a></li>

</ul>
</details>

**社区讨论**: 用户普遍感到不满，评论称这次品牌重塑令人困惑且是“诱饵换货”。一位开发者创建了一个零依赖的 Python 脚本来恢复 VS Code 设置和聊天历史记录，而其他人则批评 Google 缺乏重点，且修复 bug 的速度远不及其他 AI 实验室。

**标签**: `#Google`, `#developer tools`, `#IDE`, `#bait-and-switch`, `#migration`

---

<a id="item-4"></a>
## [Project Hail Mary 恒星导航图](https://valhovey.github.io/gaia-mary/) ⭐️ 7.0/10

该项目提供了一个基于欧空局盖亚 DR3 星表的交互式恒星导航图，利用自定义 Python 脚本渲染了超过 18 亿颗恒星。 它展示了如何将真实的恒星观测数据转化为沉浸式可视化体验，让公众和教育工作者能够直观感受星表数据的宏大规模。 星图使用了盖亚 DR3 的实际恒星位置和颜色数据，但少数亮星未被包含；社区评论指出，图中行星、恒星的大小和轨道间距并未按真实比例缩放。

hackernews · speleo · May 21, 16:23

**背景**: 盖亚探测器自 2014 年起由欧空局运行，持续绘制银河系星图。其第三次数据发布（DR3）提供了超过 18 亿颗恒星的精确位置、亮度和颜色信息。该项目利用该数据集生成可交互导航的天球背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cosmos.esa.int/web/gaia/dr3">Gaia Data Release 3 (Gaia DR3) - ESA Cosmos</a></li>

</ul>
</details>

**社区讨论**: 制作者在评论中解释了技术实现细节。评论者对可视化效果表示赞赏，但也指出天体大小和距离未按比例缩放，还有用户推荐了类似体验的游戏《精英：危险》。

**标签**: `#astronomy`, `#data visualization`, `#GAIA`, `#python`, `#space`

---

<a id="item-5"></a>
## [运行 10 年的 Ubuntu 16.04 博客迁移至 FreeBSD](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) ⭐️ 7.0/10

博客作者将其运行了十年的服务器从 Ubuntu 16.04 迁移到 FreeBSD，并记录了迁移过程中的技术挑战和收益。 这一迁移案例突显了长期不更新系统的风险，并展示了 FreeBSD 作为自托管服务的可行替代方案，其设计简洁且集成了 ZFS 等功能。 Ubuntu 16.04 已于 2021 年 4 月停止支持，服务器不再获得安全更新；迁移涉及将 WordPress 博客及所有服务转移至 FreeBSD。

hackernews · speckx · May 21, 18:54

**背景**: FreeBSD 是一款免费开源的类 Unix 操作系统，源自伯克利软件套件（BSD）。它以高性能、先进网络能力以及完全集成的 ZFS 文件系统著称。与 Linux 不同，FreeBSD 的内核和用户空间在同一个源代码树中开发，提供高度一致的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FreeBSD">FreeBSD - Wikipedia</a></li>
<li><a href="https://www.freebsd.org/">The FreeBSD Project</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似的长运行系统经验，指出迁移旧配置的困难。有人称赞 FreeBSD 的简洁和“朋克摇滚”风格，也有人报告了调试日志和防火墙配置等痛点。还讨论了 Docker 和 Caddy 等替代方案。

**标签**: `#FreeBSD`, `#Ubuntu`, `#server migration`, `#self-hosting`, `#Linux`

---

<a id="item-6"></a>
## [开发者用 Gemma4-31B 在 MacBook 上本地索引一年视频](https://blog.simbastack.com/indexed-a-year-of-video-locally/) ⭐️ 7.0/10

一位开发者使用 Gemma4-31B 大语言模型在 2021 款 MacBook 上成功索引了一年的个人视频素材，依赖 50GB 的交换内存，并将工具开源在 github.com/Simbastack-hq/framedex。 该实验表明，即使在内存有限的消费级硬件上，本地运行 310 亿参数模型用于视频索引等实际任务也是可行的，突显了本地 LLM 部署的潜力与权衡。 使用的模型是 Google 的稠密 310 亿参数模型 Gemma4-31B，系统因 MacBook 仅有 16GB 统一内存而依赖大量交换内存（50GB）。该工具名为 Framedex，可创建带有人脸和地点等元数据的视频帧可搜索索引。

hackernews · asenna · May 21, 14:01

**背景**: 大语言模型（LLM）需要大量内存来加载所有参数。2021 款 MacBook 等消费级笔记本通常只有 16GB 内存，不足以运行 310 亿参数模型。为运行此类模型，操作系统可使用 SSD 上的交换空间作为虚拟内存，但这会降低速度并加速 SSD 磨损。Gemma4-31B 是 Google 开放 Gemma 系列的一部分，旨在适用于从边缘设备到工作站的各种部署场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/google/gemma-4-31b-it">gemma - 4 - 31 b -it Model by Google | NVIDIA NIM</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 is a family of open models , purpose-built for advanced...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: 评论者担心大量交换内存导致 SSD 磨损，指出 4-bit 量化后的 Gemma4-31B 仅需约 19 GiB，50GB 交换显得过多。也有人分享了在旧硬件上运行 LLM 的类似经历，如升级内存的 ThinkPad。作者回应并开源了工具，计划将索引与 DaVinci Resolve 视频编辑集成。

**标签**: `#local LLM`, `#video indexing`, `#Gemma 4`, `#personal archive`, `#practical AI`

---

<a id="item-7"></a>
## [Python 3.15 被忽视的特性：延迟导入、同步原语、计数器运算](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) ⭐️ 7.0/10

一篇详尽的博客文章重点介绍了 Python 3.15 中不太引人注目的特性，包括通过 lazy 关键字实现的显式延迟导入、用于线程的迭代器同步原语，以及对 collections.Counter 对象进行集合运算（并集、交集、对称差）。文章还澄清，延迟导入是基于 PEP 810 实现的，此前的 PEP 690 已被拒绝。 这些特性提升了 Python 的性能和表现力：延迟导入减少了 CLI 工具和大型应用的启动时间与内存占用；迭代器同步原语简化了安全的并发迭代；Counter 集合运算使数据分析更直观。社区讨论纠正了示例错误并补充了实际用例，帮助开发者正确采用这些特性。 延迟导入的语法使用新的软关键字 'lazy' 放在 import 或 from 语句之前，仅在首次访问名称时才加载模块。迭代器同步原语包括在迭代器上的 acquire() 等方法，以安全地协调线程，补充了现有的线程工具。Counter 集合运算现在支持对称差 (^) 等集合方法，不过评论者纠正了博文中减法示例 (c-d) 的实际行为。

hackernews · rbanffy · May 21, 11:10

**背景**: 延迟导入将模块加载推迟到实际使用名称时，从而减少不必要的导入并打破导入循环。这个话题已讨论多年（PEP 690 于 2022 年被拒绝），最终以 PEP 810 的形式被接受并纳入 Python 3.15。迭代器同步原语有助于避免多个线程消费共享迭代器时的竞态条件。Counter 是用于计数可哈希对象的 dict 子类，在 Python 3.15 中新增了并集和对称差等集合运算以合并计数数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0690/">PEP 690 – Lazy Imports | peps.python.org</a></li>
<li><a href="https://docs.python.org/3/library/asyncio-sync.html">Synchronization Primitives — Python 3.14.5 documentation</a></li>
<li><a href="https://www.geeksforgeeks.org/python/counters-in-python-set-1/">Python Collections Counter - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极但谨慎：有评论者询问延迟导入是否终于实现，另一人赞赏迭代器同步原语并分享了自己的 threaded-generator 包。有评论者指出 Counter 的对称差 (^) 有实际用途，另一人则纠正了博文中的减法示例，给出了正确的 Counter 输出。此外还提到了关于自由线程改进的采访，表明人们对 Python 并发有更广泛的兴趣。

**标签**: `#Python`, `#Python 3.15`, `#language features`, `#software engineering`, `#developer tools`

---

<a id="item-8"></a>
## [1945 年三位一体核试验失传影像得以修复，清晰度前所未有](https://spectrum.ieee.org/trinity-nuclear-test) ⭐️ 7.0/10

历史学家修复了 1945 年三位一体核试验的失传照片，首次以前所未有的清晰度展示了第一颗原子弹爆炸的瞬间。 此次修复提供了这一历史关键时刻更清晰的视觉记录，使研究人员和公众能够更好地理解核时代的开端。同时也引发了关于试验对下风向居民影响以及早期核摄影技术挑战的讨论。 修复后的图像捕捉到了 1945 年 7 月 16 日山区战争时间上午 5:29:45 爆炸的确切瞬间。文章指出，修复技术展现了原始已经降解的底片中先前不可见的细节。

hackernews · pseudolus · May 21, 11:02

**背景**: 三位一体试验是人类首次核武器爆炸，由美国在二战期间作为曼哈顿计划的一部分进行。这次爆炸标志着核时代的开始。几十年来，原始照片逐渐退化，但现代数字修复技术现已恢复了丢失的细节。试验场如今仍是一个历史地标，尽管仍存在辐射问题。

**社区讨论**: 评论者强调了三位一体试验的历史意义，一位前教师指出这是他教授当代科学史的起点。另一位评论者深入探讨了试验所用的时间区（山区战争时间）。还有评论提到受试验影响的下风向居民被排除在《辐射暴露补偿法案》之外，引发了关于健康和环境正义的讨论。

**标签**: `#history`, `#nuclear science`, `#technology`, `#restoration`, `#photography`

---

<a id="item-9"></a>
## [Waymo 因自动驾驶车驶入洪水暂停服务](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) ⭐️ 7.0/10

Waymo 在亚特兰大暂停了其自动驾驶出租车服务，原因是多次发生机器人出租车驶入积水的街道的事故。该公司还在一次洪水检测故障导致车辆被冲走后，召回了 3,791 辆机器人出租车。 这一事件凸显了自动驾驶汽车的关键局限：它们无法处理非典型环境条件（即边缘案例）。这引发了人们对自动驾驶技术是否准备好大规模部署，以及在不可预测的真实场景中依赖人工智能是否安全的质疑。 根据美国国家公路交通安全管理局（NHTSA）的召回通知，该缺陷是软件决策堆栈中的一个分类错误，可能导致车辆在高速道路上减速并驶入积水。Waymo 已通过空中推送软件更新来改进洪水检测和响应能力。

hackernews · mattas · May 21, 16:30

**背景**: 自动驾驶汽车依赖传感器和算法进行导航，但在训练数据中不常见的罕见或异常条件（即边缘案例）下会出现困难。积水道路是一个典型的边缘案例，因为水深和路况千差万别且难以预测。Waymo 被认为是自动驾驶技术的领导者之一，但这一事件表明，即使是先进的系统也存在盲点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kognic.com/articles/edge-cases-autonomous-driving">Edge Cases in Autonomous Driving: Detection and Handling Guide</a></li>
<li><a href="https://www.yankodesign.com/2026/05/15/waymos-self-driving-car-saw-the-flood-and-drove-in-anyway-heres-the-problem-plaguing-every-robotaxi/">Waymo’s Self-Driving Car Saw the Flood and Drove In Anyway. Here’s The Problem Plaguing Every Robotaxi. - Yanko Design</a></li>
<li><a href="https://www.tesevo.com/blogs/tesla-news/waymo-recalls-3-791-robotaxis-after-flood-incident-ota-software-fix-deployed">Waymo Recalls 3,791 Robotaxis After Flood Incident: OTA Software Fix D</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些评论者将暂停视为现实世界测试的正常环节，也是改进的机会（如 dhbradshaw）；而另一些人对经过多年发展后 AI 仍无法处理这种边缘案例表示怀疑（如 etempleton）。少数用户幽默地将此与人类行为相比较，指出机器人出租车通过驶入明显的积水实现了'人类级别的智能'。

**标签**: `#autonomous vehicles`, `#Waymo`, `#AI safety`, `#real-world testing`, `#edge cases`

---

<a id="item-10"></a>
## [Kagi 搜索助力低视力用户](https://veroniiiica.com/using-kagi-search-with-low-vision/) ⭐️ 6.0/10

一位低视力用户 Veronica 的博客文章详细介绍了 Kagi Search 极简、无广告的界面如何显著改善她的搜索体验，引发了社区关于 Google 等主流搜索引擎可访问性缺陷的讨论。 这一亲身经历揭示了默认搜索引擎界面中存在的关键可及性和神经多样性挑战，并表明像 Kagi 这样付费、注重隐私的替代方案可以为视障和神经多样性人群提供更易用的体验。 Kagi 是一款付费元搜索引擎，聚合其他搜索引擎的结果并运行自己的爬虫 Teclis；作者本人的博客也设计了大字体、高对比度和极简布局以辅助低视力用户。

hackernews · speckx · May 21, 19:32

**背景**: Kagi（商标写作 kagi）是由位于加州帕洛阿尔托的 Kagi Inc.推出的付费无广告搜索引擎，其名称在日语中意为“钥匙”。与依赖广告和追踪的免费搜索引擎不同，Kagi 优先考虑用户隐私和高质量结果。低视力用户常常在主流搜索引擎上遇到搜索结果页面杂乱、广告过多以及屏幕阅读器兼容性差等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kagi_(search_engine)">Kagi (search engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kagi">Kagi - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，神经多样性用户也面临类似的多余内容问题，Google 搜索结果页在文本转语音时表现糟糕。一位用户称赞博客的界面在远距离阅读时很舒适，另一位则怀念 Google 地图的推荐功能。还有一位用户表示 Kagi 是唯一他们会“强力支持”的产品。

**标签**: `#accessibility`, `#search engines`, `#Kagi`, `#low vision`, `#user experience`

---

<a id="item-11"></a>
## [Spotify 将为超级粉丝预留演唱会门票](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/) ⭐️ 6.0/10

Spotify 宣布将为其最忠实的听众（即超级粉丝）预留演唱会门票，以此打击倒票行为并提高现场活动的购票机会。 这一举措可能从根本上改变音乐行业演唱会门票的分配方式，确保真正的粉丝有更大概率以原价购票，同时减少黄牛和机器人的获利空间。 该计划将门票获取直接与用户在 Spotify 上的收听数据挂钩，仅允许经过验证的超级粉丝提前或获得预留门票，从而建立了一个数据驱动的准入机制。

hackernews · elffjs · May 21, 16:26

**背景**: 演唱会门票倒卖是一个普遍问题，机器人和票贩子大量购买门票并以虚高价格转售，导致普通粉丝难以观看演出。Spotify 此举利用其庞大的用户流媒体数据来识别并奖励其最活跃的听众，为其他平台提供了一个可借鉴的潜在解决方案。

**社区讨论**: 许多评论者表示支持这一想法，也有人提出了拍卖或动态定价等替代性反黄牛方案。还有评论呼吁苹果公司进入这一领域，指出 Apple Music 已经包含了演唱会日期信息。

**标签**: `#spotify`, `#concert-tickets`, `#scalping`, `#music-industry`, `#fan-engagement`

---

<a id="item-12"></a>
## [BBEdit 16：经典 macOS 文本编辑器的新大版本](https://www.barebones.com/products/bbedit/bbedit16.html) ⭐️ 6.0/10

BBEdit 16，这款长期存在的 macOS 文本编辑器的新大版本已经发布，采用一次性许可证费用，售价 60 美元。 此次发布重申了 Bare Bones Software 对永久许可证模式的承诺，与行业内普遍转向订阅制的趋势形成对比，并在长期用户中引发了怀旧欣赏，同时引发了与 Zed 和 CotEditor 等现代编辑器的比较。 BBEdit 16 是一个增量更新而非突破性变革，保持了其通过 Shell 脚本、Python 工具或 Rust 应用进行扩展的标志性能力。价格从 1998 年的 120 美元（经通胀调整后约 245 美元）大幅下降至现在的 60 美元。

hackernews · qaz_plm · May 21, 18:21

**背景**: BBEdit 是一款 macOS 文本编辑器，起源于 20 世纪 90 年代初的共享软件，由 Rich Siegel 开发。长期以来，它因原生 Mac 性能和强大的文本处理能力而受到开发者和写作者的青睐。近年来，像 Zed（一款基于 Rust、注重速度的开源编辑器）和 CotEditor（一款轻量级的原生 macOS 编辑器）这样的现代编辑器已经出现，成为替代选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zed_(text_editor)">Zed (text editor ) - Wikipedia</a></li>
<li><a href="https://coteditor.com/">CotEditor -Text Editor for macOS</a></li>

</ul>
</details>

**社区讨论**: 社区的反响充满了怀旧和赞赏，用户注意到价格从 120 美元显著降至 60 美元，并赞扬 Bare Bones 避免了订阅模式。一些用户提到已转向 Zed 或 CotEditor 等其他编辑器，但仍然尊重 BBEdit 的可扩展性和长久历史。

**标签**: `#BBEdit`, `#text editor`, `#macOS`, `#software pricing`, `#developer tools`

---

<a id="item-13"></a>
## [财富正向 AI 集中](http://www.ruanyifeng.com/blog/2026/05/weekly-issue-397.html) ⭐️ 6.0/10

该周刊观察到，内存、半导体、液冷、光通信等 AI 相关行业的股票价格大幅上涨，例如 SK 海力士员工平均获得 610 万人民币奖金，OpenAI 从 600 名员工手中回购了 66 亿美元股票。 这一趋势表明社会财富正在大规模重新分配并向 AI 集中，即使不直接使用 AI 的人也会受到影响，因为电子产品、原材料价格上涨，非 AI 行业的投资减少。 该周刊指出，仅韩国两大内存厂商就将韩国股市从 2600 点一年内拉到 7600 点。此外，文章警告不要使用大语言模型进行精确医疗估算，显示 AI 估算碳水含量的结果在不同模型和测试中波动极大。

rss · 阮一峰的个人网站 · May 21, 23:58

**背景**: 高带宽内存 (HBM) 是一种 3D 堆叠的 SDRAM 接口，对 GPU 等 AI 加速器至关重要，因为它为大模型训练提供高带宽。液冷和光通信是 AI 数据中心的关键支撑技术，分别应对巨大的散热和数据传输需求。这些股票的大幅上涨反映了 AI 基础设施投资的快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/27118812779">AI 数据中心液冷未来：直接芯片液冷技术解析 - 知乎</a></li>

</ul>
</details>

**标签**: `#AI`, `#stock market`, `#technology trends`, `#semiconductors`

---