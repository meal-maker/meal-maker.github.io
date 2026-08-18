---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 38 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [修复 Framework 13 固件更新变砖指南](#item-tech-news-1) ⭐️ 8.0/10
2. [Linux 7.3 改善 VRAM 耗尽时的性能](#item-tech-news-2) ⭐️ 8.0/10
3. [Mojo🔥 编译器与工具链现已开源](#item-tech-news-3) ⭐️ 8.0/10
4. [国产 AI 芯片 2026 年将占中国近九成，寒武纪与华为领跑](#item-tech-news-4) ⭐️ 8.0/10
5. [Claude Code 每周用量促销将于 8 月 19 日结束](#item-tech-news-5) ⭐️ 7.0/10
6. [Qwen 3.8 27B 获 Artificial Analysis 智能指数 52 分](#item-tech-news-6) ⭐️ 7.0/10
7. [相机版 AirPods 现身 macOS Tahoe 26.7 RC 展示视觉智能](#item-tech-news-7) ⭐️ 7.0/10
8. [企业微信 5.0.10 开放 CLI 与 MCP 接入主流 Agent](#item-tech-news-8) ⭐️ 7.0/10
9. [中国要求政府机构提前数月卸载定制版 Windows 10](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [先买后付贷款覆盖水电房租，美国 2025 年借贷额达 1600 亿美元](#item-finance-news-1) ⭐️ 8.0/10
2. [茅台上半年净利润下降 1.95%，为 2014 年以来首次半年报下滑](#item-finance-news-2) ⭐️ 7.0/10
3. [美债收益率上升推高房贷与柴油成本，普通家庭承压](#item-finance-news-3) ⭐️ 7.0/10
4. [湖人老板珍妮·巴斯反对向伊格与库什纳出售家族股份](#item-finance-news-4) ⭐️ 7.0/10
5. [苹果美国 App Store 佣金收入下降 18%，二季度用户消费降 6%](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [修复 Framework 13 固件更新变砖指南](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 8.0/10

本文记录了修复一台因固件更新失败而变砖的 Framework 13 AMD 7040 笔记本电脑的完整过程，并给出了具体操作步骤。文章指出此类固件更新导致设备无法启动的问题并不少见，且涉及底层固件恢复。由于需要直接操作硬件和固件，用户应具备一定技术经验并自行承担风险。

hackernews · jp\_sc · 8月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49345220)

**「背景」** Framework 13 是一款主打模块化和可维修性的笔记本电脑，其 BIOS/UEFI 固件更新失败可能导致设备无法启动，即“变砖”。本文作者使用的是一台搭载 AMD 7040 系列处理器的 Framework 13，因 BIOS 更新失败而变砖；Framework 官方支持建议更换主板，但作者使用约 20 美元的工具自行重刷固件完成修复。这一案例凸显了固件更新风险以及厂商在保修外维修政策上的争议。

**「影响」** 遭遇相同故障的 Framework 13 AMD 7040 用户可参考本文的恢复步骤尝试自行修复，以减少因固件更新失败导致的损失。

**「社区讨论」** 社区评论普遍对固件更新导致设备变砖表示不满，有用户提到类似情况也发生在 ThinkPad Nano 上，并认为 PC 厂商对此不够重视。部分用户主张厂商应对官方更新造成的损坏承担法律责任或延长保修，也有用户对 Framework 的配件锁定和库存问题表示失望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/">Fixing a bricked AMD 7040 series Framework 13” laptop with $20 tools | Quantum</a></li>
<li><a href="https://blog.adafruit.com/2026/08/18/fixing-a-bricked-framework-laptop/">Fixing a bricked Framework laptop</a></li>

</ul>
</details>

**标签**: `#hardware`, `#firmware`, `#bios`, `#repair`, `#framework-laptop`

---

<a id="item-tech-news-2"></a>
### [Linux 7.3 改善 VRAM 耗尽时的性能](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

该文章介绍了一项内核改动，可能随 Linux 7.3 推出，旨在改善显存（VRAM）耗尽时的性能。其核心是更好地处理显存超额分配（memory overcommit），而不是直接失败或严重降级。目前该改动尚未合入上游主线。这一方向被认为有助于提升 GPU 内存管理，在超出物理显存时降低性能损失。

hackernews · flaburgan · 8月18日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49342719)

**「背景」** VRAM 过量使用是指应用程序请求的显存超过物理 VRAM，内核需要通过分页或压缩等方式管理；此前 Linux 内核对 AMD GPU 的显存管理在低端显卡显存不足时可能导致性能不稳定。相关内核补丁已在邮件列表讨论数月，现已合并进入 Linux 7.3 队列，用于改进低端 GPU（尤其是 AMDGPU）的显存管理，且该工作已先在 SteamOS 稳定版和预览版内核中启用。

**「影响」** 使用有限显存的 Linux 用户（尤其是游戏玩家）可期待 Linux 7.3 内核引入初步的显存管理改进，在显存超量分配时减少性能问题，但该工作仍处于早期阶段而非完整修复。

**「社区讨论」** 社区普遍认可这一改进并期待其上游化；同时有用户指出 NVIDIA 显卡不支持任何分页，显存不足问题依然突出，并有人询问内核是否可以对虚拟内存碎片进行原地整理。另有评论担心普通 RAM 耗尽时系统冻结，希望类似机制也能改善内存压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7.3 To Land Initial Code Improving vRAM Management, More Improvements Coming - Phoronix</a></li>
<li><a href="https://pixelcluster.dev/VRAM-Overcommit/">VRAM Management Part 2: Beyond the Limits of Physical VRAM | pixelcluster&#x27;s GPU blog</a></li>
<li><a href="http://pixelcluster.dev/VRAM-Mgmt-fixed/">Fixing AMDGPU&#x27;s VRAM management for low-end GPUs | pixelcluster&#x27;s GPU blog</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7 . 3 To Land Initial Code Improving vRAM Management , More...</a></li>
<li><a href="https://pixelcluster.dev/VRAM-Overcommit/">VRAM Management Part 2: Beyond the... | pixelcluster&#x27;s GPU blog</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#VRAM`, `#GPU`, `#memory management`, `#performance`

---

<a id="item-tech-news-3"></a>
### [Mojo🔥 编译器与工具链现已开源](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 8.0/10

Mojo 编程语言现已开源，其编译器与工具链采用 Apache 2 许可证发布。该语言最初承诺自 2023 年 5 月起开源，上周发布了 1.0 版本，如今兑现了这一承诺。Mojo 最初目标是成为 Python 的超集，但 2025 年 8 月左右的路线图已改变，官方表示它不一定会成为 Python 完整超集。如今 Mojo 是独立语言，使用受 Python 启发的语法来优化 GPU 编程，但并非与现有 Python 代码 100% 兼容。此次开源包含编译器与工具链。

rss · Simon Willison · 8月18日 21:39

**「背景」** Mojo 由 Modular 公司开发，是一种面向 AI 与系统编程的高性能语言，语法受 Python 启发。Apache 2 是一种宽松开源许可证，允许用户自由使用、修改和分发代码，包括用于商业用途。

**「影响」** 开发者现在可以在 Apache 2 许可下自由获取、修改和分发 Mojo 编译器与工具链；但需要注意 Mojo 不再是 Python 的超集，现有 Python 代码可能无法直接运行，需借助迁移工具或修改。

**标签**: `#programming-languages`, `#open-source`, `#AI-systems`, `#compilers`, `#high-performance-computing`

---

<a id="item-tech-news-4"></a>
### [国产 AI 芯片 2026 年将占中国近九成，寒武纪与华为领跑](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-homegrown-ai-accelerators-to-supply-90-percent-of-the-countrys-domestic-market-analysts-suggest-cambricon-and-huawei-expected-to-be-the-biggest-winners-in-the-shift-away-from-nvidia-and-amd) ⭐️ 8.0/10

TrendForce 预测，到 2026 年，中国本土 AI 加速器在国内市场的份额将从去年的 45% 大幅提升至近 90%，寒武纪和华为被视为最大受益者。作为参照，2025 年英伟达出货 220 万颗、占 55% 市场份额，华为出货 81.2 万颗、占 20.3%。这一转变意味着中国需要在约一年内把高端 AI 芯片产量提高 2.2 倍至约 196 万颗，但产能能否跟上仍存在疑问。

telegram · zaihuapd · 8月18日 13:03

**「背景」** AI 加速器是用于加速人工智能训练和推理的专用芯片，目前英伟达在该领域全球领先。中国市场因出口管制和国产替代政策，正推动本土芯片企业扩大份额，寒武纪和华为升腾是主要参与者。

**「影响」** 如果这一预测实现，英伟达在中国 AI 加速器市场的份额将从 2025 年的 55% 明显收缩，而寒武纪和华为将获得更大国内订单，前提是高端芯片产能提升 2.2 倍的瓶颈能够解决。

**标签**: `#AI accelerators`, `#semiconductors`, `#China tech`, `#market forecast`, `#Huawei`

---

<a id="item-tech-news-5"></a>
### [Claude Code 每周用量促销将于 8 月 19 日结束](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion) ⭐️ 7.0/10

Anthropic 的 Claude Code 每周用量限时提升促销将于 2026 年 8 月 19 日结束：从 2026 年 5 月 13 日至 8 月 19 日，Claude Code 的每周用量限制提高了 50%，之后将恢复至促销前水平。该变化直接影响经常在 200 美元/月套餐上用到 90%–100% 用量的开发者。部分社区用户表示，如果限制回落将立即转向 Codex；有用户称已在一个月前完全切换到 Codex 和 5.6 sol，认为其限制更高、输出优于 Opus 4.8，而 Opus 5 对其不可用。此外，有讨论认为 Anthropic 的 token 最大化策略与 OpenAI 的效率优先策略将决定长期竞争。

hackernews · tyre · 8月18日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=49348751)

**「背景」** Claude Code 是 Anthropic 提供的 AI 编程助手，按月订阅用户有每周用量限额，超过后会被限流或降级。Anthropic 于 2026 年 5 月 13 日启动一项限时促销，将 Claude Code 的每周用量上限临时提高 50%，原定持续至 2026 年 8 月 19 日太平洋时间晚上 11:59。促销到期后，限额将恢复至促销前水平，而不是取消每周限额。

**「影响」** 促销结束后，Claude Code 的每周用量限制将回落到 2026 年 5 月 13 日之前的水平，对经常达到 90%–100% 上限的 $200/月用户意味着可用额度下降，部分用户已表示将切换到 Codex。

**「社区讨论」** 评论中普遍对促销结束表示担忧，尤其是经常触及上限的用户；多人表示会转向 Codex，称其输出优于 Opus 4.8 且限制更高，但也有用户对 Anthropic 的整体稳定性和 Opus/Fable 的实用性不满。争论点还在于 Anthropic 的 token 最大化与 OpenAI 的效率优先哪种长期更优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.threads.com/@technewsonweb/post/Da8TDHqEykX/claude-code-may-august-weekly-limits-promotion-now-run-through-august-limited/">Claude Code May–August 2026 weekly limits promotion - now run through August 19, 2026. ( limited-time promotion that increases weekly usage limits in Claude Code by 50%. )</a></li>
<li><a href="https://aicatchup.com/news/claude-code-weekly-limits-50-percent-promo">Claude Code Weekly Limits +50% Promo -- Now Through August 19 | AI Catchup</a></li>
<li><a href="https://www.explainx.ai/blog/claude-usage-limits-2026-timeline-explained">Claude Usage Limits 2026: Every Change, Dated and Explained | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#Anthropic`, `#AI coding tools`, `#usage limits`, `#product update`

---

<a id="item-tech-news-6"></a>
### [Qwen 3.8 27B 获 Artificial Analysis 智能指数 52 分](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 7.0/10

在 Artificial Analysis 智能指数上，Qwen 3.8 27B 取得 52 分。该分数与 GPT-5.6 Luna（max）持平，仅比 GLM-5.2（max）和 DeepSeek V4 Pro 0813（max）低 1 分。对比而言，GLM-5.2 拥有 753B 参数，DeepSeek V4 Pro 0813 拥有 1.7T 参数，而 GPT-5.6 Luna 参数规模未知但推测远大于 27B。作者 Simon Willison 称 Qwen 3.8 27B 是“真正令人惊叹的模型”。

rss · Simon Willison · 8月17日 23:58

**「背景」** Artificial Analysis Intelligence Index 是一个用于比较不同大语言模型综合智能表现的指数。Qwen 3.8 27B 是一款参数规模为 27B 的大型语言模型，而 GPT-5.6 Luna、GLM-5.2（753B 参数）和 DeepSeek V4 Pro 0813（1.7T 参数）属于规模更大或参数未知的竞品。

**「影响」** 该结果凸显了 27B 参数模型在综合智能基准上已能匹敌或接近参数量高一个数量级以上的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen3.8 27B - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**标签**: `#ai`, `#llms`, `#qwen`, `#benchmark`, `#model-efficiency`

---

<a id="item-tech-news-7"></a>
### [相机版 AirPods 现身 macOS Tahoe 26.7 RC 展示视觉智能](https://www.macrumors.com/2026/08/17/camera-equipped-airpods-macos-26-7/) ⭐️ 7.0/10

苹果正在开发配备摄像头的 AirPods，内部代号为 B790。在 macOS Tahoe 26.7 RC 的演示中，摄像头可识别书名并通过视觉智能保存信息，Siri 则能回答佩戴者周围环境的问题并记录信息。Mark Gurman 称该产品最快可能于 9 月发布。目前这仍是传闻，苹果尚未正式公布相关硬件或系统功能。

telegram · zaihuapd · 8月18日 02:00

**「背景」** 视觉智能（Visual Intelligence）是苹果此前在 iPhone 16 系列上推出的 AI 功能，可通过摄像头识别周围物体与文字。彭博社记者 Mark Gurman 已在 2026 年 5 月首次报道代号为 B790 的配备摄像头 AirPods 计划；本次 macOS 26.7 RC 中的演示资源进一步展示了该产品调用视觉智能和 Siri 的交互方式。

**「影响」** 若该产品按传闻发布，佩戴者将能通过耳机摄像头直接识别书籍、物品等并交由 Siri 记录，而无需拿出手机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/17/airpods-with-camera-get-their-clearest-leak-yet/">AirPods with cameras get their clearest leak yet - 9to5Mac</a></li>
<li><a href="https://www.macrumors.com/2026/08/17/camera-equipped-airpods-macos-26-7/">Apple&#x27;s Camera-Equipped AirPods Confirmed: See Them in Action - MacRumors</a></li>
<li><a href="https://www.engadget.com/2238891/apple-appears-to-have-leaked-its-camera-equipped-airpods/">Apple appears to have leaked its camera-equipped AirPods - Engadget</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AirPods`, `#visual intelligence`, `#macOS`, `#AI`

---

<a id="item-tech-news-8"></a>
### [企业微信 5.0.10 开放 CLI 与 MCP 接入主流 Agent](https://mp.weixin.qq.com/s/uJf57P15-FQL_u6jLHiGYA) ⭐️ 7.0/10

企业微信 5.0.10 版本面向所有企业开放 CLI 与 MCP 能力。WorkBuddy、DeepSeek Harness 以及企业自建 Agent 可直接调用 10 大核心办公模块。接入支持人员与 AI 权限隔离、关键操作人工审批、限时授权和完整审计。AI 还可读取文档和表格、分析数据，并生成提案 PPT 或经营看板。

telegram · zaihuapd · 8月18日 06:22

**「背景」** 企业微信是腾讯面向企业用户的通讯与办公协作平台，本次开放的 CLI（命令行接口）和 MCP（模型上下文协议）用于让外部 AI Agent 安全调用企业微信内的办公能力。WorkBuddy 是腾讯云代码助手推出的 AI Agent 办公工具，可自主规划并交付多模态复杂任务结果，支持多智能体并行工作。

**「影响」** 企业开发者和现有 Agent 可获得标准化的办公模块调用入口，但相关调用须受权限隔离、人工审批、限时授权与审计约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.workbuddy.cn/">WorkBuddy - AI Agent 办 公 新范式</a></li>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>

</ul>
</details>

**标签**: `#enterprise-software`, `#ai-agents`, `#mcp`, `#enterprise-wechat`, `#automation`

---

<a id="item-tech-news-9"></a>
### [中国要求政府机构提前数月卸载定制版 Windows 10](https://www.bloomberg.com/news/articles/2026-08-18/china-axing-microsoft-windows-from-state-agencies-ahead-of-plan) ⭐️ 7.0/10

中国国家安全部已要求部分政府相关机构卸载定制版 Windows 10，使原定于 2027 年 2 月的停用计划提前数月。该指令源于数据安全担忧，但知情人士未说明具体漏洞或风险细节。微软表示，未发现影响该产品的安全事件，且该定制版 Windows 10 仍定期获得安全更新。

telegram · zaihuapd · 8月18日 06:22

**「背景」** 被要求卸载的定制版 Windows 10 是微软面向中国政府机构提供的特殊版本，于 2016 年在满足中国多项安全要求后推出。相比普通 Windows 10，该版本需要符合中国特定的安全合规标准，因此此次提前停用与数据安全担忧直接相关。

**「影响」** 该要求将迫使相关政府机构提前数月完成定制版 Windows 10 的卸载与替代系统迁移，而具体安全依据尚未公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/software/operating-systems/china-reportedly-orders-state-agencies-to-uninstall-its-government-only-edition-of-windows-10">China reportedly orders state agencies to uninstall ... | Tom&#x27;s Hardware</a></li>
<li><a href="https://wccftech.com/china-state-agencies-uninstall-windows-10-cmit-government-edition/">China ’s State -Linked Firms Are Moving Away From Windows 10 Due...</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Windows 10`, `#data security`, `#government IT`, `#technology policy`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [先买后付贷款覆盖水电房租，美国 2025 年借贷额达 1600 亿美元](https://www.nytimes.com/2026/08/17/business/buy-now-pay-later.html) ⭐️ 8.0/10

据《纽约时报》报道，“先买后付”贷款已扩展到水电、通信、房租等日常支出，美国消费者 2025 年通过此类贷款借款 1600 亿美元，较 2023 年近乎翻倍。

telegram · zaihuapd · 8月18日 01:41

**「背景」** 这类分期付款贷款此前多用于网购，如今被用来支付生活账单，但多数贷款尚未纳入征信，直接扣款失败可能产生透支费。

**「影响」** 对依赖此类贷款维持收支的家庭来说，同时背负多笔贷款可能加重债务负担，形成债务陷阱。

**标签**: `#buy now pay later`, `#consumer credit`, `#household debt`, `#fintech`, `#US economy`

---

<a id="item-finance-news-2"></a>
### [茅台上半年净利润下降 1.95%，为 2014 年以来首次半年报下滑](https://www.cnbc.com/2026/08/19/china-economy-moutai-ai-property.html) ⭐️ 7.0/10

贵州茅台今年上半年净利润同比下降 1.95%至 445 亿元（约 66 亿美元），为 2014 年以来首次半年报利润下滑。分析师认为这反映出中国经济从房地产驱动转向科技/AI、以及反腐收紧对高端白酒需求的拖累，但花旗和晨星认为批发转直销渠道变化可能扭曲了数据。

rss · CNBC Finance · 8月18日 23:18

**「背景」** 茅台 2025 年全年净利润已下降 4.5%，为有记录以来首次年度下降；其股票在 2020 至 2023 年是中国内地市值最大的上市公司，长期用于政府与企业宴请。

**「影响」** 财报发布后，茅台股价周一短暂下跌，截至周二年内累计下跌 5.7%；中央汇金和中国证券金融已不再位列前十大股东。

**标签**: `#Moutai`, `#China economy`, `#earnings`, `#consumer staples`, `#baijiu`

---

<a id="item-finance-news-3"></a>
### [美债收益率上升推高房贷与柴油成本，普通家庭承压](https://www.cnbc.com/2026/08/18/bond-market-treasury-yields-warsh-main-street.html) ⭐️ 7.0/10

美国国债收益率上升和债券市场承压，正推高美国家庭的借贷与生活成本：周二 10 年期美债收益率突破 4.7%，30 年期抵押贷款利率达到 6.75%。

rss · CNBC Finance · 8月18日 16:48

**「背景」** 近期债券抛售的直接触发因素是伊朗战争推高油价，柴油价格同比上涨 48%；同时科技公司为 AI 基础设施大举发债，与美国政府本财年预计 2.1 万亿美元（约 GDP 的 6.4%）的赤字争夺资金。

**「影响」** 购房者和依赖柴油的消费者已直接面临更高成本；分析认为，除非债券收益率回落，否则美国家庭的压力可能持续。

**标签**: `#Bond market`, `#Treasury yields`, `#Federal Reserve`, `#Consumer impact`, `#Inflation`

---

<a id="item-finance-news-4"></a>
### [湖人老板珍妮·巴斯反对向伊格与库什纳出售家族股份](https://www.cnbc.com/2026/08/17/jeanie-buss-opposes-sale-family-stake.html) ⭐️ 7.0/10

洛杉矶湖人队控制人珍妮·巴斯反对把巴斯家族持有的 17.8%球队股份出售给鲍勃·伊格和乔舒亚·库什纳；其律师称，根据 2017 年法院命令，未经她同意，任何出售均无效。

rss · CNBC Finance · 8月18日 21:29

**「背景」** 此前，珍妮的五个兄弟姐妹表示已决定出售家族剩余股份，而伊格和库什纳已同意收购马克·沃尔特的湖人多数股权，该交易对球队估值为 125 亿美元。

**标签**: `#Los Angeles Lakers`, `#sports team ownership`, `#mergers and acquisitions`, `#Bob Iger`, `#Joshua Kushner`

---

<a id="item-finance-news-5"></a>
### [苹果美国 App Store 佣金收入下降 18%，二季度用户消费降 6%](https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/) ⭐️ 7.0/10

苹果美国 App Store 佣金收入自 2026 年初下降 18%（Appfigures 数据）；Sensor Tower 称美国用户第二季度 App Store 消费额同比下降 6%，而上年同期增长 9%。苹果表示监管变化已拖累服务业务增长。

telegram · zaihuapd · 8月18日 12:17

**「背景」** 此前监管压力已迫使苹果在部分市场放宽应用内购买规则，其服务业务在 2026 年第三财季出现自 2022 年以来首次环比收入下滑。

**「影响」** 苹果 6 月季度服务收入为 307 亿美元，创同期纪录，但低于分析师预期的 314 亿美元；公司已表示 App Store 监管变化拖累了服务业务增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/">Apple&#x27;s US App Store Commission Revenue Down 18% This Year</a></li>
<li><a href="https://www.ithinkdiff.com/app-store-regulatory-changes-apple-services-revenue-q3-2026/">App Store Regulatory Changes Are Starting to Hurt Apple&#x27;s ...</a></li>
<li><a href="https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/">Apple&#x27;s US App Store Commission Revenue Down 18% This Year - MacRumors</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#regulatory changes`, `#services revenue`, `#consumer spending`

---