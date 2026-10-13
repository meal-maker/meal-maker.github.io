---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 42 条内容中筛选出 16 条重要资讯。

---

**科技新闻**
1. [黑客激活欧洲超市冰箱自动除霜](#item-tech-news-1) ⭐️ 8.0/10
2. [将 WiFi 7 路由器改造为 320Msps 软件定义无线电接收器](#item-tech-news-2) ⭐️ 8.0/10
3. [Python 3.15 发布：显式惰性导入、推导式解包与采样分析器](#item-tech-news-3) ⭐️ 8.0/10
4. [循环扩散 Transformer：去噪步内复用模块并在采样时调节深度](#item-tech-news-4) ⭐️ 8.0/10
5. [用 C 构建现代 Web 应用](#item-tech-news-5) ⭐️ 7.0/10
6. [Codex CLI 默认安装持久自更新后台守护进程](#item-tech-news-6) ⭐️ 7.0/10
7. [Meta 发布 Muse Wonder 模型，社区报告隐私与性能问题](#item-tech-news-7) ⭐️ 7.0/10
8. [U-Space：揭示语言模型不确定性的时机与原因](#item-tech-news-8) ⭐️ 7.0/10
9. [learnc 自动调优 C 常量：JPEG 改善 9.1%、WebRTC VAD F1 提升 4.9](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic：蒸馏数据减少 90%至 99%](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [中欧就混动及电动汽车贸易达成共识，中方配额不低于其他来源](#item-finance-news-1) ⭐️ 8.0/10
2. [新能源汽车出口退税率由 13%下调至 9%](#item-finance-news-2) ⭐️ 8.0/10
3. [美联储官员称或需进一步加息以防通胀心态固化](#item-finance-news-3) ⭐️ 7.0/10
4. [皇岗口岸今晨开通，实施“一地两检”新模式](#item-finance-news-4) ⭐️ 7.0/10
5. [DeepSeek 拟领投前腾讯科学家创立的机器人初创 Winverse AI](#item-finance-news-5) ⭐️ 7.0/10
6. [税务处罚新裁量基准 11 月施行 社保欠缴最高罚 3 倍](#item-finance-news-6) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [黑客激活欧洲超市冰箱自动除霜](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

2026 年 10 月 12 日前后，欧洲超市制冷系统遭到网络攻击，攻击者远程激活自动除霜功能，导致冷藏设备停止正常制冷，并影响配送和门店价格。法国连锁超市 Intermarché受影响，路透社报道有 150 家门店成为攻击目标。安全研究人员将问题指向老旧的 Danfoss 制冷控制器，例如已于 2021 年停止支持的 SM800 和已于 2016 年停止支持的 SC355；这些设备存在已知 CVE 但未得到修复。攻击暴露了遗留工业控制系统联网后缺乏安全更新和维护的现实约束。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**「背景」** Danfoss 控制器广泛用于超市冷藏柜，支持通过互联网进行远程诊断和控制，但许多老型号已经停止支持且存在已知漏洞。连接这些设备可减少人工巡检，但也会暴露在公网攻击面中。

**「影响」** 使用未修补 Danfoss 控制器的欧洲超市面临制冷中断、食品变质风险以及配送和定价混乱。目前尚不清楚该事件是否与 2026 年 8 月美国军事基地冷冻设备入侵有关。

**「社区讨论」** 评论者普遍认为，遗留控制器因成本压力无法及时替换或修复是根本原因，并指出部分新设备甚至要求联网订阅才能运行。也有人将此次攻击与 2026 年 8 月美国军事基地冷冻柜事件联系，但尚无证据确认同一攻击者。

**标签**: `#cybersecurity`, `#industrial-control-systems`, `#IoT`, `#vulnerability`, `#retail-technology`

---

<a id="item-tech-news-2"></a>
### [将 WiFi 7 路由器改造为 320Msps 软件定义无线电接收器](https://github.com/h0m3us3r/w1700k-sdr) ⭐️ 8.0/10

GitHub 项目 w1700k-sdr 展示了如何将一款 WiFi 7 路由器重新编程为 320Msps 的软件定义无线电（SDR）接收器，利用现有高带宽无线芯片实现 5 GHz 频段的射频信号采集。该方法为高带宽射频实验提供了一条低成本路径，避免了购买专用高速 SDR 硬件的高昂费用。项目由开发者 h0m3us3r 发布，此前该开发者还曾基于 ESP32 Wi-Fi 微控制器实现过 SDR。社区反馈认为这种思路有望扩展到更多常见 Wi-Fi 网卡，使普通笔记本电脑也能成为经济型 SDR 平台。但该项目仍属于实验性质，尚未形成面向最终用户的完整产品。

hackernews · djfergus · 10月12日 12:41 · [社区讨论](https://news.ycombinator.com/item?id=50055593)

**「背景」** 软件定义无线电（SDR）使用通用射频硬件采集 IQ 数据并由软件完成解调等处理，而 Wi-Fi 7 路由器通常只将 MediaTek MT7996 等射频芯片用于无线通信。该项目使用的 Gemtek W1700K 路由器中，MT7996 可输出 14 位 IQ 数据，速率最高 320 Msps，并由 Airoha AN7581 SoC 通过 10 GbE 网络流式传输到 Linux 主机，从而将一台普通路由器变成宽带 SDR 接收机。

**「影响」** 对于 SDR 爱好者和硬件黑客，该项目提供了以低成本获取 5 GHz 频段 320 Msps 接收能力的实验途径，但兼容性和长期稳定性仍需实际测试验证。

**「社区讨论」** 社区评论普遍积极，认为这是低成本获取高频宽带 SDR 能力的一种有趣方向，并期待类似方法能普及到常见 Wi-Fi 网卡。有用户指出相同芯片组可能也适用于 Banana Pi R4，另有人建议搭配衰减器、滤波器和混频器将设备扩展为服务监视器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/h0m3us3r/w1700k-sdr">GitHub - h0m3us3r/w1700k-sdr</a></li>
<li><a href="https://hackaday.com/2026/10/12/wifi-router-does-software-defined-radio/">WiFi Router Does Software-Defined Radio | Hackaday</a></li>

</ul>
</details>

**标签**: `#software-defined-radio`, `#wifi-7`, `#hardware-hacking`, `#open-source`, `#rf-systems`

---

<a id="item-tech-news-3"></a>
### [Python 3.15 发布：显式惰性导入、推导式解包与采样分析器](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 已正式发布，What&\#x27;s New 指南由 3.14 和 3.15 版本经理 Hugo van Kemenade 整理。本版引入 PEP 810 显式惰性导入，可使用 \`lazy import json\` 和 \`lazy from pathlib import Path\` 语法，模块在代码中首次使用相应符号时才真正导入；这解决了 Simon Willison 的 LLM CLI 工具因插件依赖 \`sentence\_transformers\` 等重型模块导致每次调用延迟数秒的启动成本问题。还新增 PEP 798 推导式解包（支持列表、集合和字典）以及内置采样分析器 \`profiling.sampling\`（Tachyon），原有追踪分析器从 \`cProfile\` 更名为 \`profiling.tracing\`。Miguel Grinberg 的性能测试显示 3.15 与 3.14 基本持平，仅实验性 JIT 在 Fibonacci 基准上首次带来 1.2 倍提升。随着 Python 3.10 支持周期结束，维护兼容所有支持版本的开源开发者可以告别 3.10 并开始采用 3.11 特性。

rss · Simon Willison · 10月12日 18:15

**「背景」** Python 3.10 已不再受支持，因此维护跨版本兼容的开发者需要升级到 3.11 及更高版本。显式惰性导入由 PEP 810 提出，允许按需加载昂贵模块；推导式解包由 PEP 798 提出，是对 PEP 448 的扩展，后者于 2015 年在 Python 3.5 中引入。采样分析器通过周期性捕获运行中进程的栈跟踪来计算函数耗时热点，此前类似功能通常依赖 py-spy 等外部工具。

**「影响」** 维护跨 Python 版本开源项目的开发者现在可以停止支持 Python 3.10，并启用 3.11 特性；像 LLM CLI 这类依赖插件的工具，插件作者可直接使用 \`lazy import\` 避免重型依赖拖慢每次命令调用。

**标签**: `#python`, `#python-3.15`, `#pep-810`, `#lazy-imports`, `#software-engineering`

---

<a id="item-tech-news-4"></a>
### [循环扩散 Transformer：去噪步内复用模块并在采样时调节深度](https://www.reddit.com/r/MachineLearning/comments/1x49d61/looped_diffusion_transformer_the_same_blocks_run/) ⭐️ 8.0/10

Reddit 用户测试了 Looped Diffusion Transformer，该模型在每个去噪步骤内多次运行同一组共享 transformer 模块，而不是扩大文本到图像 DiT 的规模。论文（arXiv 2609.40305，9 月 30 日）指出朴素循环不可靠，并通过每一循环的深度监督和自调制注意力解决；其核心结果是 260M 循环模型在多个基准上超过大 6.5 倍的模型，推理计算少 4.9 倍，且在固定推理预算下增加循环深度比增加去噪步骤更有效。代码和权重采用 MIT 许可并发布在 Hugging Face（sensenova），该用户在 M5 Pro 上用 PyTorch MPS fp32、100 个 Euler 步、CFG 6.0 和每个提示同一随机种子测试了循环深度 1 到 4；模型在深度 4 训练，但 README 说明其他深度无需重新训练。结果显示大部分变化发生在深度 3 之前，深度 3 和 4 在每个所示提示上都非常接近；循环深度在采样时选择，类似循环/递归深度语言模型中的迭代次数，可在每张图像上权衡计算与细化，该机器上深度 1 约 23 至 24 秒，深度 4 约 43 至 47 秒。

reddit · r/MachineLearning · /u/Fit-Ant2238 · 10月12日 18:13

**「背景」** 扩散 transformer（DiT）通过多个去噪步骤逐步从噪声生成图像，扩大模型通常意味着增加 transformer 模块参数。循环深度语言模型已经在采样时调整迭代次数；Looped Diffusion Transformer 将类似思路用于单个去噪步骤内部的模块复用，使计算量可按循环深度调节。

**「影响」** 对使用所发布 MIT 代码和 Hugging Face 权重的开发者，模型可在采样时把循环深度从 1 调到 4 而无需重训；实际测试表明深度 3 已接近深度 4 的质量，因此可在该配置下以明显低于深度 4 的延迟获得相近效果。

**标签**: `#diffusion models`, `#transformers`, `#generative AI`, `#efficiency`, `#machine learning`

---

<a id="item-tech-news-5"></a>
### [用 C 构建现代 Web 应用](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 7.0/10

这篇博文解释了如何用 C 语言构建现代 Web 应用，并引发社区对 CGI、FastCGI、安全机制与部署方式的讨论。作者（prophittcorey）的观点被评论者认为合理，尤其提到使用 pledge、chroot 等机制降低权限。评论中还提及 BusyBox 内置 CGI 支持、rclone serve webdav 以及用 C++ 和 WebAssembly 构建游戏服务器的实例。讨论涉及两种对立的部署思路：层层堆叠复杂组件与保持简单直接的 CGI/FastCGI 方式。整体内容对系统开发者和开源 Web 基础设施有参考价值，但不属于广泛行业突破。

hackernews · prophittcorey · 10月12日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50058528)

**「背景知识」** 早期动态网站通常将 C 程序放入 cgi-bin 目录，由 Apache 按请求 fork 执行；该文也提到类似的现代部署方式。文中讨论的 BCHS 栈（BSD、C、Httpd、SQLite）及 pledge/chroot 等权限分离机制，是理解用 C 构建 Web 应用的关键背景。

**「影响」** 对于考虑用 C 构建小型 Web 服务的系统开发者，这篇帖子提供了结合 CGI/FastCGI 与 pledge/chroot 特权分离的部署参考，但并未显示业界广泛采用此类方案。

**「社区讨论」** 评论者大多肯定帖子的技术判断，并引用了 BusyBox 内置 CGI 支持、FastCGI 和 C++/WebAssembly 的部署实例。也有一些评论者倾向于有状态的框架（如 Rust 加 SQLite），而不是每次请求调用 CGI 二进制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://upstract.com/x/ff7e87d60c67529f">A Modern Web App in C - upstract.com</a></li>
<li><a href="https://zeli.app/story/50058528">A Modern Web App in C · 153 HN comments | Zeli</a></li>

</ul>
</details>

**标签**: `#c`, `#web-development`, `#systems-programming`, `#cgi`, `#open-source`

---

<a id="item-tech-news-6"></a>
### [Codex CLI 默认安装持久自更新后台守护进程](https://github.com/openai/codex/issues/48195) ⭐️ 7.0/10

Codex CLI 被指默认安装一个持久、可自动更新的后台守护进程，且没有文档化的关闭选项。用户可编辑 ~/.codex/config.toml，在 \[features\] 部分设置 daemon\_auto\_start = false 来关闭；也可将 pid 文件、锁文件等替换为指向 /dev/null 的符号链接，并用 chattr +i 锁定。社区报告该守护进程曾占用约 12GB 磁盘空间并堆积旧版本，还导致权限损坏、.git 变为只读、任务每隔几小时随机阻塞等问题。有评论者指出，对于通过 NPM 安装的 CLI 来说，这种默认行为令人担忧。

hackernews · whimblepop · 10月12日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50060694)

**「背景」** Codex CLI 是 OpenAI 提供的代码助手命令行工具，用户通常通过 npm 在本地安装运行。自 0.157.0 版本起，仅打开交互式会话就会启动一个名为 codex app-server --managed-daemon 的持久后台守护进程，该进程会自行更新并常驻。相关 issue \#48195 要求将此行为改为默认关闭或至少先询问用户，以解决默认安装带来的意外后台进程问题。

**「影响」** 对 Codex CLI 用户而言，默认守护进程可能引发权限破坏、任务随机阻塞和约 12GB 磁盘占用，因此建议在配置中关闭 daemon\_auto\_start 或采用文件锁定等变通方案。

**「社区讨论」** 评论普遍对默认守护进程感到不安，并报告磁盘和权限问题；也有用户转向使用 hax 等极简工具，认为 Codex 在多个指标上更差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex/issues/48195">CLI: make ` daemon _ auto _ start ` opt-in — a persistent, self-updating...</a></li>

</ul>
</details>

**标签**: `#openai`, `#codex`, `#cli`, `#developer-tools`, `#software-bugs`

---

<a id="item-tech-news-7"></a>
### [Meta 发布 Muse Wonder 模型，社区报告隐私与性能问题](https://research.meta.ai/blog/muse-wonder) ⭐️ 7.0/10

Meta 宣布推出 Muse Wonder 模型，该模型同时涉及多模态与代码生成能力。尽管公布时带有较高的基准分数，但 Hacker News 上的用户实测显示其图像转 HTML 表现明显不及 Opus 5.5，有评论认为更接近 Sonnet 或 Haiku。另有用户尝试从 Muse Code 站点登录时，在认证页面看到了他人的个人资料，引发隐私泄露担忧。社区还通过 SVG 渲染示例比较了 Muse Spark 1.2 和 Muse 1.3 的输出效果。

hackernews · meetpateltech · 10月12日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=50059115)

**「模型背景」** Meta 于近期推出 Muse Wonder 与 Muse Wonder Full，称其为迄今最强大的模型系列，针对个人与专业智能体任务、记忆和编程提供最先进性能。Muse Wonder 系列在多项关键基准测试中取得最先进结果，其中 Muse Wonder Full 在智能体和编程基准（包括 DeepSWE 和 SWE-Marathon）的独立第三方评测中排名靠前。

**「影响」** 根据用户报告，Muse Code 登录流程可能向无关访问者显示用户资料和邮箱，构成潜在隐私风险，目前尚未见 Meta 确认或修复。

**「社区讨论」** 社区观点分歧：有评论认为更多公司接近前沿可避免权力集中，也有人强调实测性能与基准不符。讨论中包含了用户提供的隐私报告以及针对 Muse Spark 1.2、Muse 1.3 和 Muse Wonder 的生成效果对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/10/introducing-muse-wonder-models/">Introducing Muse Wonder and Muse Wonder Full: Frontier Models ...</a></li>
<li><a href="https://research.meta.ai/blog/muse-wonder">Muse Wonder | Meta AI Research</a></li>
<li><a href="https://dev.meta.ai/models/muse-wonder">Muse Wonder | Meta</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#model release`, `#multimodal`, `#code generation`

---

<a id="item-tech-news-8"></a>
### [U-Space：揭示语言模型不确定性的时机与原因](https://www.reddit.com/r/MachineLearning/comments/1x44f9m/uspace_uncovering_when_and_why_uncertainty_arises/) ⭐️ 7.0/10

研究人员发布了 U-Space/U-Lens，一种面向开放权重推理模型的单次、无标签不确定性估计方法，其分数由隐藏状态的“怀疑”方向投影与推理 token 平均熵相乘得到。该方法无需正确性标签、训练、微调或多次采样，可区分歧义、信息缺失、证据冲突和一般不确定性四类不确定性。作者在 3 个随机种子、3 个模型（Gemma 4、Qwen3.5、Magistral）、4 个基准上的评估中称其优于 5 次、10 次采样及监督基线。实现依赖 Anthropic 全局工作空间论文中的 Jacobian lens；构建一次 4 方向 U-Space 只需 CPU 和数百个词的 unembedding 行，推理时取思考结束处的一层隐藏状态点积四个向量再乘平均熵即可。Hugging Face 上已有 40 多个预拟合 lens（neuronpedia/jacobian-lens），代码位于 github.com/s2labres/U-Space，目前为研究代码而非 pip 包。

reddit · r/MachineLearning · /u/AdRevolutionary3242 · 10月12日 15:10

**「背景」** 大语言模型通常通过多次采样、裁判模型或标注数据来估计答案置信度，但这些方法成本高或依赖标签。Jacobian lens 是一种可解释性工具，来自 Anthropic 的全局工作空间论文，用于分析隐藏状态与输出词汇的关系。U-Space 利用该 lens 将隐藏状态投影到“怀疑”方向，以避免额外训练和多次推理。

**「影响」** 对于使用 Gemma 4、Qwen3.5、Magistral 等开放权重推理模型并需要置信度信号的实践者，U-Space 提供了一种单次推理即可计算的不确定性得分，可用于路由低置信度答案、触发检索或标记 RAG 中的证据冲突，但目前仅为研究代码且性能声明需在更多模型和任务上验证。

**标签**: `#uncertainty-quantification`, `#large-language-models`, `#model-interpretability`, `#reasoning-models`, `#single-pass-inference`

---

<a id="item-tech-news-9"></a>
### [learnc 自动调优 C 常量：JPEG 改善 9.1%、WebRTC VAD F1 提升 4.9](https://www.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to/) ⭐️ 7.0/10

learnc 是一个工具，可在未修改的 C 代码中针对用户用 C 编写的评分函数调优命名常量，并将新值写回同一文件。在留出数据上的结果是：对 stb\_image\_write.h 的 JPEG 编码器（128 个量化表项，在 12 张 Kodak 图像上调优，在另外 12 张上测试），在相同 SSIM 下实现了 9.1% 的 BD-rate 改善，并已用 libjpeg 和 scikit-image 独立验证；mozjpeg 的量化表则获得 2.7% 的改善。对 Google 的 WebRTC VAD（vad\_core.c 中的每个常量，在 LibriParty dev 上调优），LibriParty eval 上的 F1 从 0.810 提升到 0.859。限制条件包括：低于 1 bpp 时 JPEG 没有增益，且该工具最适合数十到数百个常量，而非大型权重集。代码以 MIT 许可证发布在 https://github.com/devanmolsharma/learnc。

reddit · r/MachineLearning · /u/keep\_up\_sharma · 10月12日 20:51

**「背景：C 代码常量自动调参与相关模块」** learnc 是一个面向 C 代码的自动调参工具，它允许开发者将程序中的具名常量视为可优化参数，并依据用户编写的 C 评分函数自动搜索更优取值，然后直接写回原文件。相关示例涉及 stb\_image\_write.h 图像编码库中的 JPEG 量化表条目，以及 Google WebRTC 语音活动检测器（VAD）核心代码中的常量；这些常量通常由开发者手工设定，而非通过数据驱动方式优化。该工具适合几十到几百个常量的场景，不适合大规模权重集合。

**「影响」** 对于使用 stb\_image\_write.h JPEG 编码器或 WebRTC VAD 的开发者，learnc 可以在留出测试上分别实现 9.1% 的 BD-rate 改善或 F1 从 0.810 到 0.859 的提升，但需要自行编写评分函数，且低于 1 bpp 时 JPEG 无增益、大型权重集不适用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismix.dev/news/dd5fee40b9ef">learnc: fit the constants in existing C code to data (9.1% ...</a></li>
<li><a href="https://github.com/DragonDev07/LearnC/blob/main/constants.c">LearnC/constants.c at main · DragonDev07/LearnC · GitHub</a></li>

</ul>
</details>

**标签**: `#C programming`, `#auto-tuning`, `#optimization`, `#JPEG`, `#WebRTC`

---

<a id="item-tech-news-10"></a>
### [Anthropic：蒸馏数据减少 90%至 99%](https://www.anthropic.com/research/distillation-defenses) ⭐️ 7.0/10

Anthropic 于 10 月 12 日公布，针对模型蒸馏攻击的新防护措施使被提取的 Claude 数据初步减少约 90% 至 99%。公司表示已封禁数万个相关账号，部分账号在攻击开始后不到两小时即被封禁。新措施包括限制推理内容跨会话、模型和账号流转，部署双阶段分类器，并持续修补已发现的绕过手法。整体误报率低于 0.1%，但部分开发者需要更新集成，且被拦截的请求仍可能产生费用。

telegram · zaihuapd · 10月13日 01:25

**「背景：模型蒸馏攻击与防护背景」** 模型蒸馏攻击指攻击者通过大量查询闭源模型 API，将其输入输出作为训练数据，复制其能力；与从零训练前沿模型需要数亿至数十亿美元和数月算力相比，蒸馏能大幅降低门槛。Anthropic 此前已支持出口管制，并指出开源蒸馏模型会放大能力扩散风险。此次公布的是其针对此类攻击的检测与防护初步结果。

**「影响」** 对依赖 Claude API 的开发者而言，部分集成需更新以避免请求被拦截，同时被拦截的请求仍可能产生费用；API 滥用者的数据提取成本将大幅上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-industry-has-data-problem-anthropic-just-made-ignore-dimitrova-5uvce">Who, What, How stole data from Anthropic</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#LLM APIs`, `#abuse prevention`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [中欧就混动及电动汽车贸易达成共识，中方配额不低于其他来源](https://www.mofcom.gov.cn/xwfb/sjfzrfb/art/2026/art_4d502e1d49fd4480b39a6cfd0d752038.html) ⭐️ 8.0/10

中国商务部表示，中欧在贸易投资磋商机制下就混动汽车和电动汽车贸易达成共识，混动汽车安排以 2025 年为基准向上调整，中方配额不低于欧盟其他进口来源地，欧盟将继续推进电动汽车价格承诺复审。

telegram · zaihuapd · 10月12日 06:19

**「背景」** 混动汽车安排以 2025 年为基准向上调整，用于兼顾中方企业出口空间和双方产业关切。

**「影响」** 这一共识为中国混动和电动汽车出口商设定了配额下限，欧盟进口商及车企需关注后续价格承诺复审程序。

**标签**: `#China-EU trade`, `#electric vehicles`, `#hybrid cars`, `#trade policy`, `#automotive industry`

---

<a id="item-finance-news-2"></a>
### [新能源汽车出口退税率由 13%下调至 9%](https://www.news.cn/20261012/9709731f470b42f9a84825c2e4eb914b/c.html) ⭐️ 8.0/10

财政部、税务总局 10 月 12 日公告，自 2027 年 4 月 1 日起，新能源汽车增值税出口退税率由 13%下调至 9%，并取消电子烟设备装置等产品的增值税出口退税。

telegram · zaihuapd · 10月12日 11:00

**「背景」** 出口退税指政府向出口企业退还其在生产、流通环节已缴纳的增值税，退税率下调会减少企业可获得的退税。此前，中国已公告自 2027 年 1 月 1 日起取消节能汽车车船税减半和新能源商用车免征车船税优惠。

**「影响」** 2027 年 4 月 1 日起，新能源汽车出口增值税退税率从 13%降至 9%，中国新能源汽车出口企业获得的出口退税将减少，出口成本相应上升，可能压缩利润或促使企业上调出口价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nev.ofweek.com/2026-07/ART-71008-8480-30694135.html">新 能 源 汽 车 要交 车 船 税 了，你的 车 要多花多少钱 - OFweek 新 能 源 汽 车 网</a></li>

</ul>
</details>

**标签**: `#new energy vehicles`, `#export tax rebate`, `#China`, `#trade policy`, `#fiscal policy`

---

<a id="item-finance-news-3"></a>
### [美联储官员称或需进一步加息以防通胀心态固化](https://www.cnbc.com/2026/10/12/beth-hammack-fed-inflation-policy.html) ⭐️ 7.0/10

克利夫兰联储主席哈马克表示，可能需要进一步收紧货币政策以防止通胀心态固化；8 月个人消费支出价格指数同比上涨 3.4%，交易员预计美联储 12 月加息概率接近 88%。

rss · CNBC Finance · 10月13日 02:58

**「背景」** 美联储上个月进行了三年来的首次加息，9 月会议纪要显示官员可能再次加息，但未说明具体时间。

**标签**: `#Federal Reserve`, `#Monetary Policy`, `#Inflation`, `#Interest Rates`, `#Economy`

---

<a id="item-finance-news-4"></a>
### [皇岗口岸今晨开通，实施“一地两检”新模式](https://sc.isd.gov.hk/TuniS//www.info.gov.hk/gia/general/202610/09/P2026100900280.htm) ⭐️ 7.0/10

据香港政府新闻网报道，重建后的皇岗口岸于 2026 年 10 月 12 日上午 6 时 30 分正式开通，实施“一地两检”及“合作查验、一次放行”新模式，提供 24 小时通关服务。整体通关时间由约 30 分钟缩短至约 5 分钟，自助通道最快约 20 秒完成通关；新口岸初期预计每日可处理高峰流量 20 万人次，未来可提升至 30 万人次。

telegram · zaihuapd · 10月12日 05:12

**「背景」** 皇岗口岸是连接深圳与香港的 24 小时陆路口岸，重建后把内地与香港边检查验集中在同一区域，旅客和车辆只需一次排队即可完成通关。

**标签**: `#Hong Kong`, `#infrastructure`, `#customs clearance`, `#cross-border trade`, `#public policy`

---

<a id="item-finance-news-5"></a>
### [DeepSeek 拟领投前腾讯科学家创立的机器人初创 Winverse AI](https://www.bloomberg.com/news/articles/2026-10-12/deepseek-backs-ex-tencent-ai-scientist-s-400-million-robot-lab) ⭐️ 7.0/10

据彭博社援引知情人士报道，DeepSeek 拟领投前腾讯科学家胡瀚创立的机器人 AI 初创公司 Winverse AI 的种子轮，金额达数千万美元，投后估值约 4 亿美元；美团的龙珠资本等也已承诺出资，但交易尚未最终敲定，估值与参投方仍可能变化。

telegram · zaihuapd · 10月12日 14:59

**「背景」** Winverse AI 由前腾讯科学家 Hu Han 创立；DeepSeek 此前已入股宇树科技，此次拟领投是其迄今最大的初创投资之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startupreader.com/news/deepseek-leads-dollar400m-seed-for-winverse-chinas-robot-ai-play">DeepSeek leads $400M seed for Winverse, China’s robot AI play</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Winverse AI`, `#robotics`, `#venture capital`, `#funding round`

---

<a id="item-finance-news-6"></a>
### [税务处罚新裁量基准 11 月施行 社保欠缴最高罚 3 倍](https://fgk.chinatax.gov.cn/zcfgk/c100012/c5252754/content.html) ⭐️ 7.0/10

国家税务总局发布《全国税务行政处罚裁量基准（2026 年版）》，自 2026 年 11 月 1 日起施行。新规将用人单位逾期不缴或少缴社保费纳入处罚事项，按欠缴金额和占比分档，最高可处欠缴金额 3 倍罚款；处罚前提是经责令限期缴纳后逾期仍不缴纳，并需补缴及按日加收万分之五滞纳金。

telegram · zaihuapd · 10月13日 02:45

**「背景」** 该基准在此前国家税务总局公开征求意见后发布，旨在统一全国税务行政处罚裁量标准；此前不同地区已有各自的地方裁量基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://paper.people.com.cn/rmrb/pc/attachement/202607/18/0378ed27-fe07-41dc-95b0-b5fb063d3b93.pdf">paper.people.com.cn/rmrb/pc/attachement/202607/18/0378ed27-fe07...</a></li>
<li><a href="https://qks.shufe.edu.cn/J/PDFFull/A0shcjdxxb-2022-2-18.pdf">Journal of Shanghai University of Finance and Economics</a></li>

</ul>
</details>

**标签**: `#tax policy`, `#social insurance`, `#regulatory compliance`, `#China`, `#penalties`

---