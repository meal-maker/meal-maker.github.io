---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 22 items, 8 important content pieces were selected

---

1. [首个公开的苹果 M5 macOS 内核内存损坏漏洞利用](#item-1) ⭐️ 9.0/10
2. [拆除 2024 款 RAV4 混动版调制解调器与 GPS](#item-2) ⭐️ 8.0/10
3. [Antirez 发布 DwarfStar4，用于本地 DeepSeek 4 推理](#item-3) ⭐️ 8.0/10
4. [M4 MacBook Air 外接 RTX 5090 显卡](#item-4) ⭐️ 8.0/10
5. [新 Nginx 漏洞可实现特定条件下的代码执行](#item-5) ⭐️ 8.0/10
6. [arXiv 计划对虚假参考文献实施一年禁令](#item-6) ⭐️ 8.0/10
7. [Codex 现已在 ChatGPT 移动应用中免费提供](#item-7) ⭐️ 7.0/10
8. [硬盘固件逆向工程揭示薄弱的混淆防护](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [首个公开的苹果 M5 macOS 内核内存损坏漏洞利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

安全研究公司 Calif 发布了首个针对苹果 M5 芯片的公开内核内存损坏漏洞利用，展示了绕过基于硬件的内存标记扩展（MTE）安全功能的能力。 这是针对苹果最新芯片的一项重大安全发现，表明即使像 MTE 这样的硬件防御也可能被绕过。它可能会显著影响 macOS 安全研究、漏洞悬赏估值，以及让内存损坏攻击变得更困难的整体努力。 该漏洞利用了 MTE 的标签检查机制，但研究人员尚未披露完整的技术细节，预计将发布一份 55 页的技术报告。社区猜测，根据演示方式，该漏洞在苹果漏洞悬赏平台上的估值可能在 10 万至 150 万美元之间。

hackernews · quadrige · May 14, 18:25

**背景**: 内存标记扩展（MTE）是 ARM 在 2019 年提出的规范，通过为内存分配分配标签，在硬件层面帮助检测内存损坏漏洞。苹果已在其最新的 M5 芯片及其他设备中集成 MTE 以提升内存安全性。内核内存损坏漏洞利用可使攻击者获得提升的权限或绕过操作系统内的安全边界。M5 是苹果最新的处理器，采用了 MTE 等增强安全措施来防御此类攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory safety in...</a></li>
<li><a href="https://support.apple.com/en-ph/guide/security/sec8b776536b/web">Operating system integrity - Apple Support (PH)</a></li>

</ul>
</details>

**社区讨论**: 评论中混合了兴奋、怀疑和好奇的情绪。一些用户期待阅读即将发布的 55 页报告，而另一些则指出缺乏详细披露，质疑漏洞如何绕过 MTE。还有关于潜在漏洞悬赏价值的讨论，以及一些关于虚假漏洞的讽刺言论。

**标签**: `#kernel exploit`, `#Apple M5`, `#macOS security`, `#memory corruption`, `#MTE`

---

<a id="item-2"></a>
## [拆除 2024 款 RAV4 混动版调制解调器与 GPS](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

2026 年 5 月 13 日发布的一份详细技术指南，提供了从 2024 款丰田 RAV4 混动版上物理拆除数据通信模块（DCM）和 GPS 天线的分步说明，以阻止车辆远程信息处理数据的传输。 这份指南凸显了消费者隐私与汽车远程信息处理之间日益紧张的关系，使车主能够从物理层面控制车辆数据。它还引发了关于汽车制造商数据收集实践以及选择退出远程信息处理共享之困难的广泛讨论。 作者指出，即使拆除了调制解调器，通过蓝牙连接手机仍会使车辆利用手机的互联网连接发送远程信息数据，而有线 USB 连接则可避免。此外，CarPlay 和 Android Auto 本身也会收集车辆远程信息。

hackernews · arkadiyt · May 14, 17:08

**背景**: 像 2024 款 RAV4 这样的现代车辆配备了数据通信模块（DCM），它利用蜂窝网络连接将远程信息数据（包括位置、驾驶行为和诊断信息）传输给制造商。令人担忧的是，这些数据可能会在未获得车主明确同意的情况下与第三方（如保险公司）共享。对于追求完全隐私的车主来说，物理禁用 DCM 是一种极端措施，因为标准的退出选项往往有限或不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rav4world.com/threads/where-is-the-telemetry-device-that-communicates-with-the-app.330240/">Where is the telemetry device that communicates with the app? - Toyota RAV4 Forums</a></li>
<li><a href="https://www.toyotanation.com/threads/how-to-turn-off-sharing-data-with-toyota.1699485/">How To Turn Off Sharing Data With Toyota? | Toyota Forum</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了额外见解：有人警告说蓝牙仍可通过手机实现数据传输，另一人指出福特 Maverick 的远程信息处理单元只有一个保险丝，拔除后不会引发错误。还有评论澄清说，丰田仅在车主在经销商设置过程中无意中选择了相关项目时，才会将驾驶数据分享给保险公司。

**标签**: `#privacy`, `#automotive`, `#telemetry`, `#Toyota`, `#IoT`

---

<a id="item-3"></a>
## [Antirez 发布 DwarfStar4，用于本地 DeepSeek 4 推理](https://antirez.com/news/165) ⭐️ 8.0/10

Antirez 发布了 DwarfStar4（DS4），这是一个专为 DeepSeek 4 设计的紧凑型 LLM 推理运行时，支持 Metal 和 CUDA 后端，目标硬件至少需要 96GB VRAM。 该项目将高质量的本地 LLM 推理引入强大的消费级硬件，可能减少对云端 API 的依赖，并在 MacBook 和 NVIDIA DGX Spark 等设备上实现保护隐私的 AI 应用。 DS4 当前需要 96GB VRAM，主要支持 Metal（Apple Silicon）和 CUDA（NVIDIA），而 ROCm 支持由社区维护，因为 antirez 没有直接硬件访问权限。

hackernews · caust1c · May 14, 22:29

**背景**: DwarfStar4 是一个推理运行时，即一种轻量级软件层，可以在本地运行大型语言模型而无需云端连接。DeepSeek 4 是中国 AI 实验室 DeepSeek 推出的最新大型语言模型，以高性能和高效率著称。该项目基于 llama.cpp 和 GGML 等先前工作，这些工作开创了高效的本地 LLM 推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forums.developer.nvidia.com/t/fully-custom-cuda-native-deepseek-4-flash-optimized-for-1x-spark-antirez-ds4/369791">Fully custom CUDA-native Deepseek 4 Flash optimized for 1x Spark! antirez/ds4</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 : 1T Parameter AI Model Guide | Independent DeepSeek ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 DS4 的性能表示兴奋，一位用户指出其质量接近 Claude 但速度较慢，另一位强调 imatrix 量化似乎优于 OpenRouter 上的后端。人们对本地模型的发展轨迹持乐观态度，并质疑几年后类似的智能是否能在 16GB 硬件上运行。

**标签**: `#LLM inference`, `#local AI`, `#DeepSeek`, `#DwarfStar`, `#antirez`

---

<a id="item-4"></a>
## [M4 MacBook Air 外接 RTX 5090 显卡](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

一篇博客文章展示了如何在 M4 MacBook Air 上通过外接显卡运行 RTX 5090，成功实现了 Windows 游戏运行，并大幅提升了 LLM 提示处理速度。 这一成果与苹果官方关于 Apple Silicon 不支持 eGPU 的立场相悖，为之前缺乏此类选项的 Mac 用户打开了 GPU 密集型游戏和 AI 推理的大门。 该方案依赖于带有 GPU 直通的虚拟机，但仍面临限制，如 1.5 GB 的有限内存窗口以及缺乏苹果官方支持。

hackernews · allenleee · May 14, 15:47

**背景**: eGPU 是一种外接图形处理器，可连接至计算机以提升图形性能，常用于缺乏强大内置 GPU 的笔记本电脑。苹果官方声明 eGPU 仅适用于 Intel 芯片的 Mac，且仅支持 AMD 显卡，不支持 NVIDIA。这一社区驱动的破解方法绕过了 Apple Silicon Mac 上的这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lenovo.com/us/en/glossary/external-gpu/">What is an external graphics processing unit (GPU)?</a></li>
<li><a href="https://biztechmagazine.com/article/2022/08/what-external-graphics-processing-unit-perfcon">What Is an External Graphics Processing Unit (eGPU) and How Does it Boost Performance?</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这一解决方案表示惊讶和赞赏，一位虚拟机开发者指出他们多年来一直在请求 GPU 直通功能。许多人强调 LLM 性能提升是最实用的好处，但也有人指出剩余的限制，如小内存窗口和缺乏官方支持。

**标签**: `#eGPU`, `#Apple Silicon`, `#Mac Gaming`, `#LLM`, `#RTX 5090`

---

<a id="item-5"></a>
## [新 Nginx 漏洞可实现特定条件下的代码执行](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

一个名为 Nginx-Rift 的新型 Nginx 漏洞已在 GitHub 上公开，展示了在 rewrite 指令包含问号且随后 set 指令引用编号正则捕获组时可能实现代码执行。该漏洞已被分配编号 CVE-2026-42945，并在 Nginx 1.31.0 和 1.30.1 版本中得到修复。 该漏洞影响重大，因为 Nginx 支撑着互联网上很大比例的 Web 服务器；但利用需要特定配置条件，且地址空间布局随机化（ASLR）可缓解已公布的概念验证攻击，尽管作者声称存在可靠的 ASLR 绕过方法。 该漏洞利用要求 rewrite 指令的替换字符串中包含问号，随后 set 指令引用编号正则捕获组（例如 set $var $1）。已公布的概念验证假设 ASLR 已禁用，官方缓解措施是在 rewrite 规则中使用命名捕获代替未命名捕获。

hackernews · hetsaraiya · May 14, 17:17

**背景**: Nginx 是广泛使用的开源 Web 服务器和反向代理。其 rewrite 模块使用正则表达式处理 URL 重写，捕获组可通过$1、$2 等引用。set 指令用于给 Nginx 变量赋值。该漏洞已存在 18 年，利用了 rewrite 模块处理 PCRE 捕获时的内存损坏。地址空间布局随机化（ASLR）是一种纵深防御技术，通过随机化内存地址增加利用难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/18-year-old-nginx-vulnerability-allows-dos-potential-rce/">18-year-old NGINX vulnerability allows DoS, potential RCE - Bleeping Computer</a></li>
<li><a href="https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html?m=1">18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated RCE</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，虽然公布的 PoC 要求禁用 ASLR，但作者声称存在可靠的 ASLR 绕过方法，安全从业者应认真对待。其他人讨论了具体的利用前提（rewrite 带问号和 set 带$1），并提到 F5 推荐使用命名捕获作为缓解措施。有用户询问 Caddy 和 Jetty 等内存安全替代方案，但对其安全记录表示怀疑。

**标签**: `#security`, `#nginx`, `#exploit`, `#vulnerability`, `#cve`

---

<a id="item-6"></a>
## [arXiv 计划对虚假参考文献实施一年禁令](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 宣布一项新政策：如果作者提交包含 AI 编造参考文献的论文，将被禁发一年，且后续提交必须先在知名同行评审期刊或会议上被接收才能上传到 arXiv。 该政策直接应对 AI 生成的虚假引用污染科学文献这一日益严重的问题——《自然》杂志的分析估计，2025 年可能有数万篇论文受到影响。它维护了学术诚信，并要求作者对 AI 生成的内容进行核实。 该禁令针对提交论文的作者，解禁后，后续提交必须先在知名同行评审场所被接受。该政策似乎仍在计划中，尚未正式实施，因为在 arXiv 的政策页面上尚未明确列出。

hackernews · gjuggler · May 14, 20:39

**背景**: 虚假参考文献是由大型语言模型（LLM）生成的虚假或不存在的引用，它们可能编造作者姓名、论文标题和出版细节。随着研究人员越来越多地使用 ChatGPT 等 AI 工具辅助写作，这一问题变得普遍。《自然》杂志的分析发现，2025 年可能有数万篇论文包含此类无效引用，甚至 NeurIPS 等顶级会议也发现已接收的论文中存在编造的引用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific literature. What can be done? - Nature</a></li>

</ul>
</details>

**社区讨论**: 社区普遍支持这项政策，评论者称赞其对科学‘非常有益’，并指出 arXiv 是一种特权而非权利。一些人对实施禁令前的仔细审查表示担忧，例如无意中包含的虚假引用是否会导致处罚。还有人指出，LLM 的支持者对任何阻碍 AI 快速普及的措施感到愤怒。

**标签**: `#arXiv`, `#academic integrity`, `#AI-generated content`, `#hallucinated references`, `#scientific publishing`

---

<a id="item-7"></a>
## [Codex 现已在 ChatGPT 移动应用中免费提供](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 7.0/10

OpenAI 已将其 AI 编码助手 Codex 免费集成到 ChatGPT 移动应用中，用户可直接在手机上借助 AI 辅助进行编码。 此举通过免费在移动设备上提供 AI 辅助编码，大幅降低了使用门槛，有望提升开发者的移动办公效率，并扩大 AI 编码工具的用户群体。 ChatGPT 移动应用中的 Codex 包含在免费计划内，但交互数据可能用于模型训练。该功能同样适用于桌面应用和 CLI，但应用版本尚未支持 Linux，且无键盘的移动端体验可能效率较低。

hackernews · mikeevans · May 14, 20:06

**背景**: Codex 是 OpenAI 开发的 AI 模型，能将自然语言转换为代码，最初为 GitHub Copilot 提供支持。ChatGPT 移动应用此前已具备通用对话功能，此次更新将 Codex 直接集成到该界面中，使用户能随时随地进行编码和调试。免费计划包含使用限制，且数据可能用于训练。

**社区讨论**: 社区成员对 Codex 免费提供感到惊讶和赞赏，部分人原以为需要付费。然而，多位用户反映移动端效果参差不齐，指出小屏幕和缺乏键盘限制了编码效率。还有用户讨论了集成问题，例如桌面应用不支持 Linux 以及远程仓库访问的困难。

**标签**: `#OpenAI`, `#Codex`, `#ChatGPT`, `#AI coding`, `#mobile app`

---

<a id="item-8"></a>
## [硬盘固件逆向工程揭示薄弱的混淆防护](https://icode4.coffee/?p=1465) ⭐️ 7.0/10

一篇详细的博客系列文章展示了如何转储、分析和修改硬盘固件，揭示了供应商使用的简单混淆技术，并提供了包括 JTAG 调试在内的实用利用方法。 这项工作凸显了硬盘固件的安全脆弱性——一旦被攻破，攻击者就能获得持久且难以检测的控制权；同时也让安全研究人员和数据恢复专家能更深入地理解并保护嵌入式存储系统。 作者通过 JTAG 转储固件，在不借助 AI 的情况下对代码进行逆向工程，并展示了供应商的混淆很容易被绕过——例如，某个工具在上传前会解密固件，而一个简单的 seccomp 过滤就能截获解密后的版本。

hackernews · jsploit · May 14, 16:19

**背景**: 硬盘固件是控制硬盘内部操作的底层软件。逆向工程通常需要 JTAG 调试器等专用硬件以及嵌入式系统知识。此前的工作，包括 SpritesMods 的 HDD 黑客和 malwaretech 系列，已探索了类似领域，而 NSA 文件也证实固件可被用于持久性间谍活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://icode4.coffee/?p=1465">HDD Firmware Hacking Part 1 – I Code 4 Coffee</a></li>
<li><a href="https://malwaretech.com/2015/04/hard-disk-firmware-hacking-part-1.html">Hard Disk Firmware Hacking (Part 1)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Obfuscation_(software)">Obfuscation (software) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实际案例，如三星 SSD 固件的反编译以及利用 seccomp 的简单绕过；有人指出该文章对面试中的 CTF 挑战很有用，还有人链接了相关的 NSA 固件黑客披露信息。

**标签**: `#firmware`, `#reverse-engineering`, `#hard-drive`, `#security`, `#embedded-systems`

---