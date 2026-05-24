---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 21 items, 6 important content pieces were selected

---

1. [C# 终于在 .NET 11 预览版中引入联合类型](#item-1) ⭐️ 9.0/10
2. [特朗普政府要求绿卡申请人离境申请](#item-2) ⭐️ 8.0/10
3. [从芯片图像反汇编 80386 微码](#item-3) ⭐️ 8.0/10
4. [Hengefinder：计算太阳与街道对齐的网页应用](#item-4) ⭐️ 7.0/10
5. [SpaceX 发射星舰 V3 超重型火箭](#item-5) ⭐️ 7.0/10
6. [HTML <dl> 元素：语义、历史与实际挑战](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [C# 终于在 .NET 11 预览版中引入联合类型](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 9.0/10

C# 在 .NET 11 预览版中引入了联合类型作为预览功能，使开发者能够用穷举模式匹配来建模来自封闭类型集合的值。 联合类型是长期需求的功能，能显著提升类型安全和代码清晰度，类似于 F# 或 Rust 中的可区分联合。这一添加使 C# 现代化，减少了处理替代状态时的一整类错误。 C# 提议的联合是类型联合，而非可区分联合或标记联合，但可以通过使用新类型声明作为分支类型来表达可区分联合。该功能处于预览阶段；微软警告设计可能会根据反馈而变化。

hackernews · ingve · May 22, 12:28

**背景**: 联合类型允许变量保存若干指定类型中的一个。C# 开发者此前使用 OneOf 等库或变通方法来实现类似效果。F# 已支持可区分联合数十年，TypeScript 和 Rust 等语言也普及了这种模式以实现更清晰的类型建模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union">Union types - C# reference | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/unions">Unions - C# feature specifications (preview) | Microsoft Learn</a></li>
<li><a href="https://blog.ndepend.com/csharp-unions/">C# 15 Unions - NDepend Blog</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，许多人表达了长期的期待和对团队努力的赞赏。一些人指出 F# 早已拥有此功能，并质疑为何 C# 获得更多关注；另一些人则认为这对于不愿或无法切换语言的团队来说是切实的改进。还有评论强调真正的考验将是是否在公共 API 中被采用。

**标签**: `#C#`, `#.NET`, `#union types`, `#type system`, `#programming languages`

---

<a id="item-2"></a>
## [特朗普政府要求绿卡申请人离境申请](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html) ⭐️ 8.0/10

特朗普政府宣布一项新规，要求大多数已在美国境内的绿卡申请人必须离境，通过海外领事程序申请，实质上终结了境内调整身份程序，除非有特殊情况。 这项政策打乱了技术工人（尤其是科技行业员工）当前在美国境内调整身份的主要路径，可能导致家人长期分离，并有损人才留存。 该规定适用于持有 H-1B、L-1、O-1 等非移民签证的申请人；只有“特殊情况”者才能在美国境内调整身份。该变更于 2026 年 5 月 22 日通过 USCIS 政策备忘录公布。

hackernews · tlhunter · May 22, 21:27

**背景**: 此前，已在美国持工作签证的外国人可以通过“调整身份”程序申请绿卡，这一过程允许他们在申请处理期间留在美国。另一种方式是“领事处理”，要求申请人回到本国或有美国领事馆的其他国家，参加面试并等待签证发放，这可能导致长时间等待以及与在美国的工作和家人分离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.uscis.gov/green-card/green-card-processes-and-procedures/adjustment-of-status">Adjustment of Status | USCIS</a></li>
<li><a href="https://www.uscis.gov/newsroom/news-releases/us-citizenship-and-immigration-services-will-grant-adjustment-of-status-only-in-extraordinary">U.S. Citizenship and Immigration Services Will Grant ‘Adjustment of Status’ Only in Extraordinary Circumstances | USCIS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Green_card">Green card - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈的沮丧和担忧，许多人认为该规定将严重扰乱科技工作者及其家人的生活，尤其是在美出生的孩子可能需要签证才能随父母出国。一些已经持有绿卡的人表示庆幸，而其他人则预测美国将失去全球人才，变得更加孤立主义。

**标签**: `#immigration`, `#US policy`, `#tech workforce`, `#green card`, `#visa`

---

<a id="item-3"></a>
## [从芯片图像反汇编 80386 微码](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

英特尔 80386 CPU 的微码 ROM 已成功从高分辨率芯片图像中提取，并通过图像处理、人工智能和人工验证相结合的方式反汇编成可读的微操作列表。 这一逆向工程成果使得像 z386 这样的开源项目能够忠实还原 80386 的微架构，保存并记录计算机历史上关键的一页。它还罕见地揭示了经典 x86 处理器微码层的内部运作。 提取的二进制数据经过交叉验证，最终的反汇编结果揭示了 CPU 为每条指令执行的完整微操作序列（例如 NEARCALL）。博客文章提到，之前的尝试认为这太难了，但新技术使其成为可能。

hackernews · nand2mario · May 23, 12:11

**背景**: 微码是 CPU 内部的低级固件，通过协调微操作来控制机器指令的执行。80386 于 1985 年推出，是英特尔首款 32 位 x86 处理器，被认为是现代计算的基石。从芯片图像逆向工程微码是一项极具挑战性的任务，因为它需要从硅片的显微照片中识别物理 ROM 单元并解码其比特模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/I386">i386 - Wikipedia</a></li>
<li><a href="https://sesamedisk.com/z386-open-source-80386-microcode-recreation/">z386: Open-Source Microcode Recreation of the 80386 CPU</a></li>

</ul>
</details>

**社区讨论**: 评论对这项工作的难度和独创性表示惊叹——liendolucas 询问提取过程的细节，bmenrigh 称其'极其困难但也极其有趣且回报丰厚'。还提到了关于 z386 项目的相关讨论，显示出社区的强烈兴趣。

**标签**: `#reverse engineering`, `#microcode`, `#80386`, `#computer architecture`, `#open-source hardware`

---

<a id="item-4"></a>
## [Hengefinder：计算太阳与街道对齐的网页应用](https://victoriaritvo.com/blog/hengefinder/) ⭐️ 7.0/10

Hengefinder 是一款网页应用，利用 Astral 库和 Jean Meeus 的天文学算法，精确计算太阳与指定街道方向对齐的时刻。它帮助摄影师和城市规划者确定特定街道的最佳光照条件。 这款工具将天文学与日常城市生活联系起来，为寻找黄金时刻完美拍摄的摄影师和分析建筑日照的城市规划者提供了实用价值。其专精方向与扎实的技术实现展示了专用工具如何通过相对简单的算法创造显著价值。 该应用使用 Python 的 Astral 库，该库采用 Jean Meeus《天文算法》中的方程，精度达到 0.01 角秒，忽略了其他行星和月球引力摄动。社区反馈指出网站目前屏蔽了移动端访问，限制了智能手机用户的现场使用。

hackernews · evakhoury · May 22, 20:39

**背景**: 太阳方位角和高度角计算用于确定太阳相对于地球上某一位置的位置。NOAA 太阳能位置计算器和 SunCalc 等工具提供类似的太阳位置数据，但 Hengefinder 专门聚焦于太阳与线性街道方向对齐的时刻，简化了流程，对于在夏至或春分等时刻捕捉戏剧性光线效果非常有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gml.noaa.gov/grad/solcalc/azel.html">NOAA Solar Position Calculator</a></li>
<li><a href="https://www.suncalc.org/">SunCalc - sunrise, sunset, shadow length, solar eclipse, sun position, sun phase, sun height, sun calculator, sun movement, map, sunlight phases, elevation, Photovoltaic system, Photovoltaic</a></li>

</ul>
</details>

**社区讨论**: 评论区突出了技术深度：infinet 称赞 Astral 库使用 Meeus 算法，而 TeMPOraL 希望有一款反向应用来预测炎热天气下的阴影区域以辅助导航。其他人则注意到移动端访问限制，并将 Hengefinder 与 The Photographer's Ephemeris 等类似工具进行了有利比较。

**标签**: `#astronomy`, `#photography`, `#tools`, `#urban planning`, `#Python`

---

<a id="item-5"></a>
## [SpaceX 发射星舰 V3 超重型火箭](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 7.0/10

SpaceX 于 2025 年 4 月的一个周五下午 6:30 左右进行了星舰 V3 火箭的首次试飞，这是星舰的第 12 次测试，也是这款最大版本火箭的首次亮相。飞行过程中，助推器出现发动机问题——上升阶段损失一台发动机，且未能重新点火进行返航推进，但星舰飞船在自身也损失一台发动机的情况下成功精准着陆。 这次飞行展示了 SpaceX 对快速迭代开发的坚持，即使出现部分失败也能收集宝贵数据，从而加速这款全球最强大火箭的改进。飞船在发动机异常情况下成功着陆，证明了其制导系统改进和隔热罩优化的可靠性，距离完全可重复使用更近一步。 助推器在上升阶段损失一台发动机，且未能重新点火进行返航推进，但着陆燃烧时发动机成功点火，不过触水时比预期更重且偏离目标。飞船在级分离后不久也损失一台发动机，但精准降落在目标点，再入时未见热点或烧穿现象，表明隔热罩性能得到改善。

hackernews · busymom0 · May 22, 23:41

**背景**: 星舰是 SpaceX 正在开发的两级完全可重复使用超重型运载火箭，旨在将大型载荷送入轨道、月球和火星。SpaceX 采用快速迭代开发方法，将工作组织为两周冲刺周期，并接受“负面结果学习体验”以快速收集数据并改进设计。星舰 V3 是迄今为止最高、最强大的型号，配备了升级的发动机和结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-will-launch-its-1st-ever-starship-v3-megarocket-today-the-stakes-couldnt-be-higher">SpaceX will launch its 1st-ever Starship V 3 megarocket on... | Space</a></li>
<li><a href="https://www.scientificamerican.com/article/spacex-launches-starship-v3-the-worlds-most-powerful-and-tallest-rocket-ever/">SpaceX launches Starship V 3 —the world's most... | Scientific American</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍对快速迭代步伐表示兴奋和赞赏，指出只要收集到数据，助推器失败是可以接受的。一位评论者强调了隔热罩的改进，再入时未见烧穿；另一位则注意到再入时飞船后方的模拟载荷卫星在燃烧。发动机舱的红色光芒被描述为不祥之兆，但飞船的精准着陆被视为制导软件的重大成功。

**标签**: `#SpaceX`, `#Starship`, `#rocket launch`, `#aerospace`, `#iterative development`

---

<a id="item-6"></a>
## [HTML <dl> 元素：语义、历史与实际挑战](https://benmyers.dev/blog/on-the-dl/) ⭐️ 6.0/10

Ben Myers 发表了一篇详细的博文，探讨了 HTML <dl> 元素的历史、语义以及实际使用中的困难，引发了关于语义 HTML 实用性的讨论。 这一讨论之所以重要，是因为它突出了语义 HTML 理想与实际 Web 开发需求之间的张力，影响了可访问性、可维护性和开发者工作流程。 <dl> 元素早在 Web 出现之前就已存在，可追溯至 1980 年代 IBM 的 GML，其语义在 HTML5 中已从“定义列表”演变为“描述列表”。

hackernews · ravenical · May 23, 13:03

**背景**: HTML <dl> 元素（描述列表）用于表示一组术语-描述对，常见于词汇表或元数据。尽管历史悠久，开发者在将其用于复杂布局时常常面临样式、嵌套和可访问性方面的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl">HTML description list element - HTML | MDN</a></li>
<li><a href="https://css-tricks.com/on-the-dl/">Blogging about HTML elements ¹? *chefs kiss* | CSS-Tricks</a></li>

</ul>
</details>

**社区讨论**: 社区评论包括历史背景，如该元素在 IBM 的 GML 中的前 Web 起源，以及开发者 kqp 等提出的实际批评——因灵活性不足而放弃语义 HTML。还讨论了 ARIA 角色限制以及该元素被误用于布局的问题。

**标签**: `#HTML`, `#semantic web`, `#web development`, `#accessibility`, `#technical debate`

---