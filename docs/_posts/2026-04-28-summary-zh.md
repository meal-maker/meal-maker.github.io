---
layout: default
title: "Horizon Summary: 2026-04-28 (ZH)"
date: 2026-04-28
lang: zh
---

> From 21 items, 11 important content pieces were selected

---

1. [微软与 OpenAI 终止独家收入分成协议](#item-1) ⭐️ 9.0/10
2. [Mercor 数据泄露：4TB 语音与 ID 文件](#item-2) ⭐️ 8.0/10
3. [Scratch 中 SVG 清理困境暴露 XSS 风险](#item-3) ⭐️ 8.0/10
4. [中国阻 Meta 购 AI 创企 Manus](#item-4) ⭐️ 8.0/10
5. [Super ZSNES 以 GPU 复兴经典模拟器](#item-5) ⭐️ 8.0/10
6. [GitHub Copilot 转向按使用量计费](#item-6) ⭐️ 8.0/10
7. [OpenClaw Beta 更新：TTS 与插件系统重大升级](#item-7) ⭐️ 7.0/10
8. [Easyduino: 开源 KiCad Arduino 开发板设计](#item-8) ⭐️ 7.0/10
9. [“你的蓝色和我的蓝色一样吗？”网站测试颜色感知边界](#item-9) ⭐️ 7.0/10
10. [macOS 27 强制要求 TLS 1.2，修改 SMB 协议影响 Time Machine](#item-10) ⭐️ 7.0/10
11. [智能手机偷走了‘非注意力’：盯着墙壁的价值](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [微软与 OpenAI 终止独家收入分成协议](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai) ⭐️ 9.0/10

微软与 OpenAI 已同意终止其独家云合作伙伴关系及收入分成安排，允许 OpenAI 使用其他云服务提供商，如 AWS 或谷歌云。 这一突破性转变可能重塑 AI 行业，使 OpenAI 能够多样化其基础设施，加剧云服务提供商之间的竞争，并可能加速 AI 模型的可用性。 此次协议解除前，微软在 OpenAI 的持股已从 49%降至 27%，似乎是为了在 Anthropic 等竞争对手崛起的背景下保护其投资。

hackernews · helsinkiandrew · Apr 27, 13:22

**背景**: 微软与 OpenAI 于 2019 年达成数十亿美元的合作伙伴关系，授予微软在 Azure 上托管 OpenAI 模型的独家权利及收入分成。该协议对 OpenAI 的成长和 Azure 的 AI 能力至关重要。但随着 OpenAI 的扩展和对灵活性的需求，双方矛盾加剧，最终导致重新谈判。

**社区讨论**: 评论者普遍认为这对谷歌和 AWS 是利好，许多人指出 OpenAI 现在可以使用谷歌的 TPU。一些人质疑微软为何同意，推测是为了在来自 Anthropic 和 DeepSeek 的竞争加剧时保护其投资。另一些人认为这表明 Azure 的 AI 优势正在削弱。

**标签**: `#Microsoft`, `#OpenAI`, `#AI industry`, `#partnership`, `#cloud computing`

---

<a id="item-2"></a>
## [Mercor 数据泄露：4TB 语音与 ID 文件](https://app.oravys.com/blog/mercor-breach-2026) ⭐️ 8.0/10

Mercor 是一家 AI 招聘初创公司，其数据泄露导致约 4 万名合同工的 4TB 语音样本和身份证件被盗。被盗数据已于本月初被 Lapsus$团伙发布在其泄露网站上，成为可用于深度伪造身份欺诈的完整工具包。 此次泄露事件严重之处在于将语音样本与身份证件配对，攻击者可借此制造逼真的深度伪造内容，用于金融欺诈，例如绕过银行的声纹认证或在视频通话中冒充受害者。这凸显了生物识别数据泄露的不可逆风险以及对数据最小化（Datensparsamkeit）原则的迫切需求。 被盗数据集包含来自 AI 培训合同工的语音录音和政府签发身份证件的高分辨率扫描件。与只泄露单一类型数据的典型泄露事件不同，这个组合数据集提供了制作深度伪造音频和视频以进行身份欺诈所需的全部材料，包括绕过银行声纹认证和进行类似 Arup 案风格的视频通话诈骗。

hackernews · Oravys · Apr 27, 09:57

**背景**: Mercor 是一家 AI 招聘初创公司，通过 AI 面试收集语音样本，为 AI 模型训练提供人力专家。许多 AI 公司收集语音数据以改进语音识别和语音克隆技术，但此类生物识别数据一旦泄露，无法像密码一样更改。'数据最小化'（Datensparsamkeit）原则强调应尽量减少数据收集以降低泄露影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mercor">Mercor - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Mercor_AI">Mercor AI</a></li>
<li><a href="https://www.mercor.com/">Mercor | Defining the future of work</a></li>

</ul>
</details>

**社区讨论**: 社区评论讽刺地指出，受害者需提交更多语音样本进行分析的悖论，并讨论了深度伪造的实际威胁（如银行声纹绕过、Arup 式诈骗）以及数据最小化的必要性。有评论者建议将生物识别标记为'永久密码'以提高警惕，另有评论者提及大规模语音数据收集的历史先例。

**标签**: `#data breach`, `#biometrics`, `#deepfake`, `#privacy`, `#AI safety`

---

<a id="item-3"></a>
## [Scratch 中 SVG 清理困境暴露 XSS 风险](https://muffin.ink/blog/scratch-svg-sanitization/) ⭐️ 8.0/10

一篇详细文章揭示，Scratch 基于正则表达式的自定义 SVG 清理方法反复未能防止跨站脚本攻击（XSS），从 2019 年到 2026 年不断出现新的绕过方式，包括通过 CSS @import 和 CSS 嵌套导致的 HTTP 泄漏。 这之所以重要，是因为 Scratch 是一个拥有超过 1 亿用户的广泛使用的教育平台，其中许多是儿童，因此此类漏洞成为严重的安全问题，可能允许在用户项目上执行任意代码。 文章记录了多年来多种绕过方式，最新帖子声称每个 Scratch 版本都容易受到任意代码执行攻击，且作者未遵循负责任的披露流程。

hackernews · varun_ch · Apr 27, 15:31

**背景**: SVG（可缩放矢量图形）可能包含 JavaScript 和事件处理程序，若未正确清理则可能成为 XSS 的载体。Scratch 允许用户上传 SVG，其清理过程使用了正则表达式，但由于 SVG 的复杂性，正则表达式极不可靠。内容安全策略（CSP）是一种更强大的防御手段，可以限制页面可以加载的资源，但 Scratch 未正确实施 CSP。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scratch_(programming_language)">Scratch (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Security_Policy">Content Security Policy</a></li>
<li><a href="https://app.daily.dev/posts/the-woes-of-sanitizing-svgs-pwfqj7jvs">The woes of sanitizing SVGs | daily.dev</a></li>

</ul>
</details>

**社区讨论**: 社区评论称赞该文章指出 CSP 是唯一可靠的修复方式，并建议使用排除危险元素的 SVG 子集。其他人批评 Scratch 使用正则表达式进行清理以及缺乏负责任的披露，有评论指出作者的最新帖子展示了如何在当前版本中利用漏洞，而事先未进行披露。

**标签**: `#SVG`, `#security`, `#XSS`, `#sanitization`, `#Scratch`

---

<a id="item-4"></a>
## [中国阻 Meta 购 AI 创企 Manus](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html) ⭐️ 8.0/10

中国以国家安全和出口管制违规为由，阻止了 Meta 对 AI 初创公司 Manus 价值 20 亿美元的收购案，该交易已于 2026 年 2 月完成，中国正寻求撤销该交易。 这一决定标志着中国对 AI 技术出口管制的显著升级，可能重塑全球 AI 并购格局，并为中国出口管制法律的域外执行树立先例。 Manus 在中国创立，但在 2025 年 5 月由 Benchmark 领投 7500 万美元融资后迁至新加坡；中国援引出口管制法第 12 条（兜底条款）及境外关联企业规则，针对这家新加坡实体，使已完成的交易在法理上更难撤销。

hackernews · yakkomajuri · Apr 27, 11:43

**背景**: Manus 开发能够自主执行市场调研、编程和数据分析等任务的通用 AI 智能体，并于 2025 年初崭露头角。中国的出口管制法包括兜底条款和境外关联企业规则，允许北京对源自中国的技术主张管辖权，即便公司已迁至海外。本案与 TikTok 的情况类似，中国曾主张对由中国创始人开发的算法拥有控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html">China blocks Meta's $2 billion takeover of AI startup Manus</a></li>

</ul>
</details>

**社区讨论**: 社区评论者就中国此举的法律依据及其影响展开辩论，特别是涉及公司迁至新加坡的情况。有人认为中国只是在运用其版本的出口管制，与美国类似，且创始人并非被‘扣押’，而是正在接受调查。另一些人指出，破坏新加坡的‘遮羞布’可能对未来跨境科技安排产生问题。

**标签**: `#AI`, `#Meta`, `#China`, `#acquisition`, `#geopolitics`

---

<a id="item-5"></a>
## [Super ZSNES 以 GPU 复兴经典模拟器](https://zsnes.com/) ⭐️ 8.0/10

ZSNES 的原开发者 zsKnight 和 _Demo_ 发布了 Super ZSNES，这是一款采用 GPU 加速的经典 SNES 模拟器现代版本。它引入了诸如无损音频替换和通过 GPU 增强图形渲染等功能。 这一复兴作品现代化了上世纪 90 年代末备受喜爱的模拟器，为复古游戏爱好者提供了显著的性能提升和准确性。它还重新点燃了社区对 SNES 模拟的兴趣，并展示了传统软件如何从现代硬件中受益。 Super ZSNES 将 PPU（图像处理单元）渲染任务卸载到 GPU，与原始软件渲染器相比，实现了逐像素效果和更高分辨率。该模拟器还支持用高质量的无损采样替换压缩音频，这一功能建立在社区追踪原始音源的努力之上。

hackernews · haunter · Apr 27, 17:50

**背景**: ZSNES 是一款免费开源的 Super Nintendo Entertainment System（SNES）模拟器，最初发布于 1990 年代末，以其速度和兼容性广受欢迎。其开发在 2000 年代初放缓，但原开发者如今携 Super ZSNES 回归，利用 GPU 计算突破了模拟器之前的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZSNES">ZSNES - Wikipedia</a></li>
<li><a href="https://arstechnica.com/gadgets/2026/04/super-zsnes-is-a-stab-at-a-modern-snes-emulator-from-the-original-developers/">"Super ZSNES" is a stab at a modern SNES emulator from the ...</a></li>
<li><a href="https://zsnes.com/">ZSNES Home Page - About ZSNES</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对原版 ZSNES 的怀念以及对 GPU 加速改进的兴奋。技术讨论集中在 PPU 渲染实现上，一位用户分析了模拟器是逐瓦片渲染还是使用逐像素状态。另一位用户则提出了如何在模拟器上合法获取 ROM 的问题。

**标签**: `#emulation`, `#SNES`, `#GPU`, `#retro gaming`, `#ZSNES`

---

<a id="item-6"></a>
## [GitHub Copilot 转向按使用量计费](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) ⭐️ 8.0/10

GitHub 宣布将 Copilot 从固定月度订阅转为基于使用量的计费模式，这实际上提高了重度用户的成本，并使定价与 API 消耗保持一致。 这一变化代表了开发者为 AI 编码辅助付费方式的重大转变，可能使 Copilot 相比于直接从 OpenAI 或 Anthropic 等提供商调用 API 变得不那么经济实惠。 根据新方案，Copilot Pro 的月费仍为 10 美元，但包含 10 美元的月度 AI 积分，不同模型（如 GPT、Sonnet 或 Opus）的倍率从 1 倍到 27 倍不等。

hackernews · frizlab · Apr 27, 16:03

**背景**: 此前，GitHub Copilot 提供固定月费的无限制补全和聊天功能，经常允许重度用户以固定成本消耗大量 API 资源。向按使用量计费的转变反映了更广泛的行业趋势，即 AI 提供商正从固定订阅模式转向基于消耗量的定价。

**社区讨论**: 社区评论大多持批评态度，许多用户计算出实际价格上涨远大于公布的倍率，举例称重度使用 Opus 时等效涨幅可能达到 50 倍。部分用户正在考虑转向按量付费的 API 提供商（如 OpenRouter 或 Deepseek），质疑留在 Copilot 的动力何在。

**标签**: `#GitHub Copilot`, `#pricing`, `#AI coding assistants`, `#usage-based billing`, `#developer tools`

---

<a id="item-7"></a>
## [OpenClaw Beta 更新：TTS 与插件系统重大升级](https://github.com/openclaw/openclaw/releases/tag/v2026.4.25-beta.3) ⭐️ 7.0/10

OpenClaw 的 v2026.4.25-beta.3 版本新增了包括 Azure Speech、小米和 ElevenLabs v3 在内的 TTS 提供商，将插件启动迁移至冷持久化注册表，扩展了 OpenTelemetry 对模型调用和工具循环的覆盖，并通过 CDP 原生角色快照和无头启动增强了浏览器自动化。 这些升级显著增强了 OpenClaw 的语音回复能力、插件可靠性、可观测性和浏览器自动化，使其成为构建 AI 驱动的对话式代理的开发人员更强大的平台。 值得注意的技术细节包括新增支持 SSML 转义和 Ogg/Opus 输出的 Azure Speech、新的无头浏览器启动模式，以及用于内存压力和上下文装配的 OpenTelemetry 属性。

github · steipete · Apr 26, 13:00

**背景**: OpenClaw 是一个用于构建对话式 AI 代理的开源平台。文本转语音 (TTS) 将文本转换为口语音频，而 OpenTelemetry 是一个用于收集追踪、指标和日志的可观测性框架。Chrome DevTools 协议 (CDP) 支持底层浏览器自动化。冷持久化注册表持久存储插件元数据，减少启动时扫描清单的需要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opentelemetry.io/docs/what-is-opentelemetry/">What is OpenTelemetry? | OpenTelemetry</a></li>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol - version tot</a></li>

</ul>
</details>

**标签**: `#TTS`, `#OpenTelemetry`, `#plugin system`, `#browser automation`, `#open-source`

---

<a id="item-8"></a>
## [Easyduino: 开源 KiCad Arduino 开发板设计](https://github.com/Hanqaqa/Easyduino) ⭐️ 7.0/10

Easyduino 是一个新的开源 GitHub 仓库，提供了流行微控制器开发板（如 Arduino UNO、Arduino Nano、ESP32、ESP32-S3、Raspberry Pi Pico 和 STM32 Bluepill）的 KiCad PCB 设计文件，这些设计从其他 EDA 工具转换而来，并增加了 USB-C 支持和四层板堆叠。 该项目填补了重要空白，为广泛使用的开发板提供了高质量的开源 KiCad 设计，使学习、定制和集成到自定义 PCB 更加容易。它降低了创客和专业人士基于成熟布局设计自己电路板的门槛。 这些设计从原始的 Eagle 和 Altium 文件统一转换为 KiCad，并集成了 USB-C 连接器和针对 JLCPCB 制造优化的四层铜箔堆叠。仓库包含多种外形尺寸，并遵循 KiCad 最佳实践。

hackernews · Hanqaqa · Apr 27, 17:45

**背景**: KiCad 是一款免费开源电子设计自动化（EDA）软件套件，用于原理图绘制和 PCB 布局。像 Arduino 这样的开发板是预制的电路板，带有微控制器，便于电子项目原型制作。Easyduino 为这些流行开发板提供了现成的 KiCad 项目文件，允许用户修改并制造自己的定制版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Hanqaqa/Easyduino">GitHub - Hanqaqa/Easyduino: Eaily dive into different PCB ...</a></li>
<li><a href="https://app.daily.dev/posts/github---hanqaqa-easyduino-easily-dive-into-different-pcb-kicad-designs-of-the-most-popular-microco-cl8faa0hl">GitHub - Hanqaqa/Easyduino: Easily dive into different...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Easyduino 反响热烈，称赞它是有价值的学习资源，使自定义电路板设计更加容易。一位用户指出它填补了常见开发板开源设计的空白，另一位用户分享了改进 Arduino UNO 的个人项目。还有用户询问如何向儿童介绍 PCB 设计，表明该项目的教育潜力。

**标签**: `#open-source`, `#KiCad`, `#Arduino`, `#PCB-design`, `#hardware`

---

<a id="item-9"></a>
## [“你的蓝色和我的蓝色一样吗？”网站测试颜色感知边界](https://ismy.blue/) ⭐️ 7.0/10

网站“Is my blue your blue?”（ismy.blue）向用户展示一系列色块，并要求他们判断每个色块是蓝色还是绿色，从而测量每个人在蓝色和绿色之间划分的界限。该测试揭示了用户之间在颜色分类上的显著差异，这些差异通常与文化及语言背景相关。 这个简单的交互工具通过展示人们对一个看似基本的视觉区分存在分歧，有力地证明了语言相对论——即语言影响感知的观点。它引发了社区关于颜色视觉个体差异以及文化命名习惯如何塑造我们感知世界的广泛讨论。 该测试呈现一系列从绿色过渡到蓝色的色块，要求用户将每个色块分类为蓝色或绿色，然后计算个人的边界点。评论者指出，许多中间颜色（如青色或蓝绿色）既不纯蓝也不纯绿，使得这种强制选择任务对某些用户来说令人沮丧。

hackernews · theogravity · Apr 27, 20:24

**背景**: 颜色感知同时受生物学和语言的影响。关于语言相对论的研究表明，不同语言对色谱的分割方式不同——例如，有些语言用一个词来指代蓝色和绿色，而有些语言则区分多种色调。Berlin 和 Kay（1969）的经典研究发现了颜色命名的普遍模式，但后续研究显示，这些语言类别会微妙地影响说话者对颜色边界的感知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linguistic_relativity_and_the_color_naming_debate">Linguistic relativity and the color naming debate - Wikipedia</a></li>
<li><a href="https://www.smithsonianmag.com/science-nature/why-different-languages-name-different-colors-180964945/">The World Has Millions of Colors. Why Do We Only Name a Few?</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.1619666114">Color naming across languages reflects color use | PNAS</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出复杂的情绪：一些用户认为该测试令人沮丧，因为像青色或蓝绿色这样的中间颜色无法整齐地归入蓝色/绿色的二元分类中；另一些人则分享了与家人或朋友在颜色名称上产生分歧的个人经历。少数参与者指出，文化背景或显示器校准可能会影响结果，这突显了该现象的复杂性。

**标签**: `#color perception`, `#linguistics`, `#human-computer interaction`, `#cognitive science`, `#web app`

---

<a id="item-10"></a>
## [macOS 27 强制要求 TLS 1.2，修改 SMB 协议影响 Time Machine](https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/) ⭐️ 7.0/10

macOS 27 将对网络连接强制要求至少 TLS 1.2 协议，并对 SMB 协议进行修改，这将影响通过网络进行的 Time Machine 备份。 这些变化通过淘汰过时的加密来增强安全性，但可能破坏与旧服务器和 NAS 设备的兼容性。依赖 AFP 协议的 Time Machine 用户需要迁移到 SMB，可能需要重新配置网络。 Apple 正在弃用用于 Time Machine 备份的 AFP（Apple 文件协议），转而支持 SMB。TLS 1.0 和 1.1 将被阻止，这可能影响与旧版 Web 服务器及某些企业服务的连接。

hackernews · pvtmert · Apr 27, 15:36

**背景**: TLS（传输层安全协议）是一种保护互联网通信的加密协议；TLS 1.2 多年来一直是标准，而早期版本被认为不安全。SMB（服务器消息块）是一种网络文件共享协议，主要被 Windows 使用，但 macOS 也支持它来访问共享文件夹和网络驱动器。AFP 长期以来是 Apple 专有的文件共享协议，用于本地网络上的文件共享和 Time Machine 备份，但 Apple 正在向 SMB 过渡以提高跨平台兼容性。

**社区讨论**: 社区评论显示反应不一：一些用户对 Time Machine 动画的 bug 表示不满，另一些则回忆起 Apple 过去的网络更改曾导致广泛问题。还有用户指出 Time Capsule 硬件自 2018 年起已不再受支持，依赖 AFP 备份的用户需要切换到 SMB，其中一位用户分享了在 Time Capsule 上构建 Samba 4 的指南。

**标签**: `#macOS`, `#networking`, `#TLS`, `#SMB`

---

<a id="item-11"></a>
## [智能手机偷走了‘非注意力’：盯着墙壁的价值](https://www.alexselimov.com/posts/men_who_stare_at_walls/) ⭐️ 6.0/10

一篇随笔指出，智能手机不仅占据了我们的集中注意力，还消除了宝贵的‘非注意力’——例如盯着墙壁这样让思绪自由游荡的无结构闲暇时刻，而这些对创造力和精神重启至关重要。 对于经常依赖深度专注的技术从业者而言，失去非注意力可能削弱创造性问题解决能力和精神恢复。这一观点揭示了持续在线的一个被忽视的成本，促使我们重新评估无结构思考时间的价值。 作者用‘disattention’一词与‘attention’形成对比，将其描述为思维未积极参与的时刻。这篇随笔在 Hacker News 上获得了强烈共鸣（445 分、202 条评论），许多读者分享了盯着墙壁作为精神重启方式的个人体验。

hackernews · aselimov3 · Apr 27, 11:08

**背景**: 非注意力的概念与思绪游离和白日梦相关，认知科学已证明这些活动有助于创造力、记忆巩固和问题解决。在智能手机通知不断的时代，这些闲暇时刻越来越多地被被动内容消费或任务切换所取代，可能损害心理健康和创新思维。

**社区讨论**: 评论者大多认同这一观点，分享了个人的童年习惯——盯着墙壁，但如今已遗失。有人将其与冥想比较，指出虽然冥想是结构化的专注训练，但非注意力是无结构的且同样宝贵。还有几条幽默评论附上了一张 Unsplash 墙壁照片链接，供想尝试的人使用。

**标签**: `#attention`, `#digital well-being`, `#meditation`, `#technology and society`, `#mental health`

---