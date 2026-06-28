---
layout: default
title: "Horizon Summary: 2026-05-02 (ZH)"
date: 2026-05-02
lang: zh
---

> From 23 items, 6 important content pieces were selected

---

1. [Flock 利用儿童体操室摄像头进行销售演示](#item-1) ⭐️ 8.0/10
2. [TI-84 Evo 升级至 ARM Cortex 处理器](#item-2) ⭐️ 7.0/10
3. [WhatCable：免费 macOS 应用识别 USB-C 线缆能力](#item-3) ⭐️ 7.0/10
4. [信用卡暴力破解攻击：已知但有缓解措施](#item-4) ⭐️ 7.0/10
5. [Openclaw v2026.4.29：新增主动运行转向和人员感知记忆](#item-5) ⭐️ 6.0/10
6. [我们能在梦中学习和交流吗？](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Flock 利用儿童体操室摄像头进行销售演示](https://www.404media.co/city-learns-flock-accessed-cameras-in-childrens-gymnastics-room-as-a-sales-pitch-demo-renews-contract-anyway/) ⭐️ 8.0/10

美国佐治亚州邓伍迪市发现 Flock Safety 公司曾访问儿童体操室的实时摄像头画面用于销售演示，但该市仍续签了与这家公司的合同。 这一事件引发了对隐私和道德的严重担忧，尤其是涉及儿童，并凸显了监控技术销售中缺乏适当监督和专用演示环境的问题。 Flock 的演示合作伙伴计划允许部分员工访问合作城市的实时摄像头画面用于产品演示，而本案中并未使用独立的演示环境。

hackernews · joshcsimmons · May 1, 18:37

**背景**: Flock Safety 是一家为警方、企业和业主协会提供自动车牌识别（ALPR）和视频监控系统的主要供应商。该公司运营着一个演示合作伙伴计划，允许城市授权访问实时画面用于演示。此前，Flock 的摄像头画面曾被发现在无密码的情况下暴露于开放互联网，引发了额外的隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/">Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves</a></li>
<li><a href="https://www.theverge.com/news/849624/flock-ai-camera-feeds-exposed-benn-jordan">Dozens of Flock AI camera feeds were just out there | The Verge</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑 Flock 为何没有独立的演示环境，并批评该市在发生隐私泄露后仍续签合同。一些人指出，体操室内安装摄像头本身就令人担忧，而另一些人则强调了无门槛大规模监控的更广泛问题。

**标签**: `#privacy`, `#surveillance`, `#ethics`, `#security`, `#children's safety`

---

<a id="item-2"></a>
## [TI-84 Evo 升级至 ARM Cortex 处理器](https://education.ti.com/en/products/calculators/graphing-calculators/ti-84-evo) ⭐️ 7.0/10

德州仪器发布了 TI-84 Evo，将经典的 Z80 处理器替换为运行频率 156 MHz 的 ARM Cortex CPU，性能提升 3 倍，同时保持与现有软件的完全向后兼容性。 这标志着这款广泛应用于中学和大学数学教育的经典图形计算器系列数十年来首次重大处理器变革。该升级在不干扰现有教育程序和考试生态的前提下提供现代性能，延长了平台的适用性。 ARM Cortex CPU 运行频率为 156 MHz，而之前 Z80 和 eZ80 型号为 48 MHz。TI-84 Evo 仍然需要使用相同的 TI-84 Plus 软件，并预计兼容标准的考试禁用限制。

hackernews · thatxliner · May 1, 20:06

**背景**: Zilog Z80 是一款 8 位微处理器，于 1976 年首次发布，为 TI-83 和 TI-84 Plus 系列提供了超过三十年的计算能力。经过近 50 年后 Z80 正被停产，迫使制造商寻求 ARM Cortex 等现代替代方案，这是一种性能更高、功耗更低的 32 位架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zilog_Z80">Zilog Z80 - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/retrobattlestations/comments/1cb2hs6/the_legendary_zilog_z80_cpu_is_being_discontinued/">The legendary Zilog Z80 CPU is being discontinued after nearly 50 years</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有关于在学校甚至监狱中使用 TI 计算器的怀旧故事，也有质疑昂贵图形计算器教育价值的批评观点，并推荐了 Casio 科学计算器等更便宜的替代品。还有技术讨论确认了 ARM Cortex 升级以及 Z80 时代的终结。

**标签**: `#graphing calculators`, `#TI-84`, `#ARM Cortex`, `#education`, `#hardware`

---

<a id="item-3"></a>
## [WhatCable：免费 macOS 应用识别 USB-C 线缆能力](https://github.com/darrylmorley/whatcable) ⭐️ 7.0/10

开发者 darrylmorley 发布了 WhatCable，一款免费开源的 macOS 菜单栏应用，能够读取 USB-C 线缆中的 e-marker 数据，以通俗易懂的英文显示其充电功率、数据传输速度、显示支持以及 Thunderbolt 能力。 USB-C 线缆外观相同但性能差异巨大，用户常因无法分辨哪条线缆支持快充或高速数据而烦恼。WhatCable 通过展示 macOS 已获取的线缆技术数据，消除了猜测，让用户能轻松选择合适的线缆用于对应任务。 该应用使用 Swift 和 SwiftUI 构建，通过 macOS 的 IOKit 服务读取线缆的 e-marker 数据，并以人类可读的格式呈现。开发者在收到社区反馈后的 7 小时内发布了 16 个版本，新增了传统窗口模式和命令行界面。

hackernews · sleepingNomad · May 1, 08:43

**背景**: USB-C 线缆内部包含一个 e-marker 芯片，存储线缆的能力信息，如最大功率（例如 240W）和数据传输速度（例如 USB4 40Gbps）。macOS 在插入线缆时已会查询此芯片以协商安全供电，但这些数据对普通用户是隐藏的。WhatCable 读取相同的系统数据并以通俗语言展示，帮助用户理解为何某些线缆会导致 Mac 充电缓慢等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/darrylmorley/whatcable">GitHub - darrylmorley/whatcable: macOS menu bar app that ...</a></li>
<li><a href="https://byteiota.com/whatcable-free-macos-usb-c-cable-inspector-for-devs/">WhatCable: Free macOS USB-C Cable Inspector for Devs</a></li>
<li><a href="https://zyrontech.com.au/blogs/news/e-marker-chip-usb-c-cable-guide">E - Marker Chip Explained: The Brain of USB - C Cables</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区称赞了应用的快速开发节奏，在 7 小时内发布 16 个版本并及时采纳用户反馈。评论者还讨论了将该应用移植到其他平台，有用户使用 AI 在 10 分钟内成功创建了 KDE Plasma 小组件，另有用户提到 ChromeOS 内置了类似的 USB-C 检测功能，并询问是否有 Linux 等效方案。

**标签**: `#USB-C`, `#macOS`, `#open-source`, `#hardware`, `#Swift`

---

<a id="item-4"></a>
## [信用卡暴力破解攻击：已知但有缓解措施](https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html) ⭐️ 7.0/10

一篇博客文章声称信用卡号码可被暴力破解，但社区指出支付处理器已采用反枚举措施，且分析忽略了授权与结算之间的关键区别。 虽然卡片枚举确实是一个安全威胁，但该文章忽略了现有缓解措施而夸大了风险；理解这些细节有助于消费者和开发者避免不必要的恐慌并实施正确的防御。 Stripe 等支付处理器会主动检测并阻止卡片测试，Visa 等卡组织会对未防止枚举的商户进行处罚。此外，成功的授权并不保证结算，因此欺诈性收费仍可被撤销。

hackernews · kodbraker · May 1, 20:26

**背景**: 信用卡暴力破解攻击，也称为卡片枚举或卡片破解，涉及尝试大量卡号、有效期和 CVV 组合以找出有效卡片。支付网络已实施反枚举最佳实践和速率限制来检测并阻止此类攻击。授权是初步检查资金是否可用，而结算是实际资金转移；一笔费用可能被授权但从未结算（如果被标记为可疑）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spreedly.com/blog/payment-authorization-vs-settlement">Payment Authorization vs . Settlement</a></li>
<li><a href="https://usa.visa.com/dam/VCOM/global/support-legal/documents/anti-enumeration-and-account-testing-best-practices-merchant.pdf">[PDF] Anti-Enumeration and Account Testing Best Practices for Merchants - Visa</a></li>
<li><a href="https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-010_Card_Cracking">OAT-010 Card Cracking | OWASP Foundation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该文章未提及结算与授权的区别（tialaramex），支付处理器已阻止枚举（janpeuker），以及用户可以冻结不使用的卡片（8cvor6j844qw_d6）。另一位评论者分享了即使换新卡后欺诈性收费仍在持续的个人经历，表明攻击可能不单纯是枚举（julienchastang）。

**标签**: `#security`, `#credit cards`, `#brute force`, `#payment systems`, `#hacker news`

---

<a id="item-5"></a>
## [Openclaw v2026.4.29：新增主动运行转向和人员感知记忆](https://github.com/openclaw/openclaw/releases/tag/v2026.4.29) ⭐️ 6.0/10

Openclaw v2026.4.29 默认启用了消息和自动化的主动运行转向，新增了具有溯源视图的人员感知记忆维基，扩展了提供商/模型支持（包括 NVIDIA 和 Bedrock Opus 4.7），并修复了网关和插件的可靠性问题。 此次发布通过使运行时行为更加动态和上下文感知，增强了 AI 代理编排，从而提高了自动工作流的可靠性和用户信任。扩展的提供商支持也降低了使用多种 AI 模型的团队的集成门槛。 记忆系统现在包含每对话的活跃记忆过滤器、超时时的部分召回以及有界的 REM 预览诊断，同时转向队列默认在下一个模型边界处清空所有待处理消息，并带有 500 毫秒的备用去抖。值得注意的修复包括 Slack Block Kit 限制、Telegram 弹性以及受限配置文件的启动警告，这些配置文件需要显式的 'alsoAllow' 条目。

github · steipete · Apr 30, 21:01

**背景**: Openclaw 是一个开源 AI 代理框架，使开发者能够构建和编排用于消息、自动化和复杂工作流的自主代理。它提供记忆管理、工具执行以及 Slack、Discord 和 Telegram 等多平台支持。'主动运行转向' 概念允许代理根据实时反馈在运行时调整其执行路径，而 '人员感知记忆' 则添加关于人类用户的元数据，以改善上下文召回和隐私处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.clawbot.blog/blog/openclaw-v2026429-released-active-run-steering-and-visible-reply-enforcement-for/">OpenClaw v2026.4.29 Released: Active - Run Steering ... — clawbot.blog</a></li>
<li><a href="https://docs.openclaw.ai/concepts/queue-steering">Steering queue - OpenClaw</a></li>

</ul>
</details>

**标签**: `#openclaw`, `#release`, `#automation`, `#memory`, `#AI`

---

<a id="item-6"></a>
## [我们能在梦中学习和交流吗？](https://www.newyorker.com/culture/annals-of-inquiry/its-possible-to-learn-in-our-sleep-should-we) ⭐️ 6.0/10

《纽约客》的一篇文章报道称，新研究表明人们可以在梦中学习新技能甚至与他人交流，这挑战了关于睡眠是心智完全中断的传统观点。 如果得到验证，这项研究可能改变我们对待学习和解决问题的方式，提供一种利用睡眠进行高效认知工作的途径。同时，它也引发了关于睡眠中意识边界的伦理和实践问题。 文章引用了软件工程师和数学家的轶事证据，他们报告在梦中解决复杂问题或发现漏洞。然而，关于睡眠中双向交流的科学证据仍然有限且存在争议。

hackernews · XzetaU8 · May 1, 17:47

**背景**: 睡眠，尤其是快速眼动（REM）睡眠，已知在记忆巩固和创造性解决问题中起关键作用。清醒梦（即做梦者意识到自己在做梦）已被研究用于可能的技能练习。这项新研究将这些想法扩展到探索与做梦者的实时交流。

**社区讨论**: 评论者分享了在梦中解决编程漏洞和数学问题的个人经历，多人指出这些洞察准确且立即可用。对于交流的说法，既有好奇也有怀疑，一位用户质疑两个睡眠中的人如何互动。

**标签**: `#sleep`, `#learning`, `#cognition`, `#problem-solving`, `#neuroscience`

---