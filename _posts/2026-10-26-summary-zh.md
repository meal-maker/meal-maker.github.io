---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 28 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Brotli 高危漏洞影响 Python 与 Node.js 组件](#item-tech-news-1) ⭐️ 8.0/10
2. [老旧 CNN 在皮肤癌诊断中胜过前沿 LLM](#item-tech-news-2) ⭐️ 7.0/10
3. [Nanbeige 发布 Apache 2.0 教师模型 Nanbeige4.3-33B](#item-tech-news-3) ⭐️ 7.0/10
4. [苹果周三发布首款触屏 MacBook Pro](#item-tech-news-4) ⭐️ 7.0/10

**财经新闻**
1. [2025 年末全国总人口 140489 万人，比上年减少 339 万](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Brotli 高危漏洞影响 Python 与 Node.js 组件](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

谷歌 Brotli 解码器漏洞 CVE-2026-111497 被评定为 CVSS 4.0 9.2 分，影响 1.0.3 至 1.2.0 版本。远程未认证攻击者可发送特制压缩流，导致内存损坏、敏感数据泄露、进程崩溃或可能执行任意代码。该漏洞最初以 Node2Shell 名称披露，后被称为 HTTP2Shell，Node.js 与 Python 相关 HTTP 组件均受影响。Python Brotli 需升级至 1.2.1、brotlicffi 至 1.2.1.0；Node.js 修复版本为 22.23.4、24.22.1 或 26.12.1。OpenAI 表示于今年 2 月发现该问题。

telegram · zaihuapd · 10月25日 02:42

**「背景」** Brotli 是谷歌开发的通用无损压缩格式，常用于 HTTP 内容编码和 Web 资源传输，以减小传输体积。该漏洞位于其解码器，处理恶意构造的压缩流时发生内存损坏。因为 Brotli 解码器被 Node.js 与 Python 常见 HTTP 库集成，攻击面包括任何接收不可信压缩数据的服务端或客户端组件。

**「影响」** 使用 Brotli 1.0.3–1.2.0 或受影响的 Node.js、Python 组件的用户和组织应立即升级到上述修复版本，否则可能被远程未认证攻击者执行任意代码或导致服务崩溃。

**标签**: `#security`, `#vulnerability`, `#Brotli`, `#Python`, `#Node.js`

---

<a id="item-tech-news-2"></a>
### [老旧 CNN 在皮肤癌诊断中胜过前沿 LLM](https://lynchlab.net/llm-skin-cancer) ⭐️ 7.0/10

一项对比显示，一个约 10 年前的 Inception v3 卷积神经网络在皮肤癌诊断上优于前沿大语言模型（LLM）。该 CNN 在 ISIC Archive 的 68011 张皮肤镜和临床图像上进行了微调，并在 200 个测试病灶上评估，且训练前已排除同一病灶或患者的其他照片。结果显示专用微调模型在皮肤病变分类上比通用 LLM 更准确。这一案例说明在医学影像等专业任务中，小而专门的模型可能比大而通用的 LLM 更具优势。

hackernews · sungam · 10月25日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=50233779)

**「背景」** 皮肤癌诊断任务通常基于皮肤镜或临床照片对病变进行分类。卷积神经网络（CNN）是专门处理图像空间特征的架构，而大语言模型（LLM）虽具备多模态能力，但主要面向通用视觉问答，并非为医学影像分类优化。在此背景下，使用大规模皮肤病变图像数据集（如 ISIC 档案）微调的旧式 CNN，可能比未针对该任务专门训练的前沿 LLM 表现更好。

**「影响」** 对于皮肤癌图像分类等医疗 AI 场景，这一对比提示微调专用 CNN 可能比直接使用前沿 LLM 更可靠，但该结论基于单一数据集和仅 200 例测试，外推需谨慎。

**「社区讨论」** Hacker News 评论大多认为这一结果并不意外，专用窄模型在特定任务上常优于通用 LLM，例如计算器优于 LLM 做乘除法、KataGo 在围棋上超人类。也有评论提醒该对比可能属于针对基准过度优化（benchmaxxing），并指出早些年人们曾用医疗诊断应用为 LLM 的负面外部性辩护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lynchlab.net/llm-skin-cancer">A 10-year-old CNN outperforms frontier LLMs for skin cancer ...</a></li>
<li><a href="https://www.promptzone.com/ayaka_nkrumah/a-10-year-old-cnn-outperforms-gpt-4o-on-skin-cancer-diagnosis-3p1k">A 10-Year-Old CNN Outperforms GPT-4o on Skin Cancer Diagnosis</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#computer vision`, `#LLMs`, `#medical AI`

---

<a id="item-tech-news-3"></a>
### [Nanbeige 发布 Apache 2.0 教师模型 Nanbeige4.3-33B](https://www.reddit.com/r/MachineLearning/comments/1xf6x35/nanbeige_releases_nanbeige4333b_an_apache_20/) ⭐️ 7.0/10

Nanbeige 发布了 Nanbeige4.3-33B，这是一个采用 Apache 2.0 许可证的教师模型，用于其规划中的更小智能体（包括即将推出的 3B 模型），并标称支持 512K 上下文窗口。发布方报告称，在 Terminal-Bench 2.1 上得分为 80.9，高于 Qwen3.8-27B 的 73.0，但在 SWE-Bench Pro 上得分为 60.3，低于后者的 61.7。这些结果是发布方自己的评估，尚未经过独立复现。为复现智能体结果，评估保留了先前推理（preserve\_thinking=true）；模型卡建议在多轮工具调用中使用该设置，但不建议在一般聊天中使用。

reddit · r/MachineLearning · /u/jatingargiitk · 10月25日 16:32

**「背景」** Nanbeige LLM Lab 发布的 Nanbeige4.3-33B 是一个 33B 参数稠密 Transformer，采用 Apache 2.0 许可，上下文窗口高达 512K（524,288 token），面向智能体编码、工具调用及中英文任务。该模型被团队定位为 Nanbeige4.3 系列的旗舰“教师模型”，用于指导后续更小的智能体模型（包括规划中的 3B 模型），并在约 30B 参数级别的开放模型中宣称具有领先的智能体性能。

**「影响」** 开发者可使用该 Apache 2.0 权重构建多轮工具调用 agent，但需按模型卡设置 preserve\_thinking=true，且当前基准分数仅来自发布方、未经独立复现，因此不宜作为部署排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context">Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with ...</a></li>
<li><a href="https://aiweekly.co/alerts/nanbeige-opens-33b-model-under-apache-20-with-512k-context">Nanbeige Opens 33B Model Under Apache 2.0 With 512K Context</a></li>
<li><a href="https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/">Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding ...</a></li>

</ul>
</details>

**标签**: `#open-source LLM`, `#agentic AI`, `#Apache 2.0`, `#benchmarks`, `#software engineering`

---

<a id="item-tech-news-4"></a>
### [苹果周三发布首款触屏 MacBook Pro](https://www.bloomberg.com/news/newsletters/2026-10-25/apple-to-unveil-touch-screen-macbook-pro-executive-promotions-in-box-checker) ⭐️ 7.0/10

苹果将于本周三发布其首款触屏 MacBook Pro，这将是 Mac 首次支持触摸操作和 OLED 屏幕，并加入灵动岛；产品提供 14 英寸和 16 英寸版本，起售价将高于现款 2499 美元。此前苹果高管多年以人体工学为由否定触屏笔记本，此次转变被指更多关乎营收与营销，触控将作为键盘和触控板的补充。这一变化也反映出苹果态度调整，不再强推行业跟随自己，而是更愿意反思和调整做法。

telegram · zaihuapd · 10月25日 14:25

**「背景」** 苹果多年来以人体工学为由拒绝为 Mac 笔记本加入触控屏，当前 14 与 16 英寸 MacBook Pro 仍采用 LCD 屏幕和刘海设计，不支持触摸。近期 Macworld 和 9to5Mac 等报道指出，苹果即将推出的 14 与 16 英寸 MacBook Pro 将首次采用触控 OLED 屏幕和灵动岛，并可能搭载 M5 Pro/M5 Max 芯片。这一背景说明苹果正在改变长期坚持的产品策略，触控将被定位为键盘和触控板的补充而非替代。

**「对 Mac 用户与开发者的影响」** 苹果首款触屏 MacBook Pro 起售价将高于现款 2499 美元，并首次引入 OLED 屏幕与灵动岛，现有 macOS 应用需适配触摸交互，专业用户升级成本可能上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macworld.com/article/2931833/touchscreen-macbook-pro-design-processor-specs-release.html">Touchscreen MacBook Pro: OLED, design and release date rumors</a></li>
<li><a href="https://www.macworld.com/article/3070324/touchscreen-macbook-pro-to-feature-dynamic-island-and-big-macos-changes.html">Apple’s touchscreen MacBook Pro might get its own Dynamic Island</a></li>
<li><a href="https://9to5mac.com/2026/10/18/new-macbook-pro-with-touchscreen-and-oled-november-6-release/">Apple’s first touchscreen MacBook could debut on November 6 ...</a></li>
<li><a href="https://www.zdnet.com/article/is-it-finally-happening-apple-is-apparently-working-on-a-touchscreen-macbook/">Is it finally happening? Apple is apparently working on a touchscreen ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#MacBook Pro`, `#touchscreen`, `#OLED`, `#hardware`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [2025 年末全国总人口 140489 万人，比上年减少 339 万](https://weibo.com/1796087453/5357878513767954) ⭐️ 7.0/10

《中国统计年鉴 2026》数据显示，2025 年末全国总人口 140489 万人，比 2024 年末减少 339 万人；全年出生人口 792 万人，自然增长率为-2.41‰。

telegram · zaihuapd · 10月25日 12:02

**「背景」** 该数据出自《中国统计年鉴 2026》。分地区看，2025 年有 9 个省份出生率超过 7‰、7 个省份自然增长率为正，主要集中在西部和华南；黑龙江、吉林、辽宁出生率最低。

**「直接影响」** 年轻人口减少将直接削弱劳动力供应并改变消费需求结构，区域出生率分化（西部和华南较高、东北较低）可能促使人口向高出生率地区流动，使相关地区的住房、教育和医疗等公共服务承压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/linux_do_channel/545902">LINUX DO Channel – Telegram</a></li>
<li><a href="https://www.163.com/dy/article/KM7B36K70517RUP3.html">全 国 人 口 减 少 339 万 ，未来 中 国 超过一半 人 口 ，将会流入到这地方！</a></li>
<li><a href="https://www.brookings.edu/wp-content/uploads/2010/11/1127_china_wang.pdf">Untitiled</a></li>

</ul>
</details>

**标签**: `#population decline`, `#China demographics`, `#birth rate`, `#macroeconomic data`, `#natural growth`

---