---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 21 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [黎曼猜想 Lean 形式化证明通过验证](#item-tech-news-1) ⭐️ 10.0/10
2. [GPGME 2.3.0 前版本漏洞影响 GitLab 等应用](#item-tech-news-2) ⭐️ 8.0/10
3. [微软用 USB4 让多台 PC 合跑一个 AI 模型](#item-tech-news-3) ⭐️ 8.0/10
4. [浙江大学首次真机实现量子随机存储器 QRAM](#item-tech-news-4) ⭐️ 8.0/10
5. [特斯拉推送 FSD v15：安全处理提升 25 倍](#item-tech-news-5) ⭐️ 8.0/10
6. [Graham Dumpleton 发布 AI 辅助 Rust 服务器 Muru](#item-tech-news-6) ⭐️ 7.0/10
7. [OpenRouter 警告 MiniMax 提示词疑遭第三方读取](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [特朗普称仍支持卢特尼克，望黄仁勋道歉后回归](#item-finance-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [黎曼猜想 Lean 形式化证明通过验证](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 10.0/10

2026 年 11 月 20 日，Levent Alpöge 发布了黎曼猜想的 Lean 形式化证明，代码库约 1700 万行。次日，Lean FRO 与 Mathlib Initiative 联合声明认证该命题与证明均正确：社区确认命题与 Mathlib 的 RiemannHypothesis 一致、代码库可无错编译，且多个独立证明检查器验证证明有效。据分析摘要与评论所述，Claude AI 在证明过程中形式化了大量现代数学，因此该结果被视为数学基础与 AI 辅助定理证明的里程碑。社区评论指出，多个不同实现和自证一致性的内核使单一 bug 导致误证的概率大幅降低，但历史上曾有伪造 Collatz 反证通过个别检查器，因此仍保留适度谨慎。

hackernews · g-b-r · 11月21日 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**「背景」** 黎曼猜想是数论中关于黎曼ζ函数所有非平凡零点实部均为 1/2 的著名未决命题，广义黎曼猜想（GRH）是其推广形式。Lean 是一种交互式定理证明器与编程语言，可将数学定义和证明形式化，并由内核独立检查；Mathlib 是 Lean 社区维护的大型数学库。在本次事件中，Levent Alpöge 于 2026 年 11 月 20 日发布了一个约 1700 万行的 Lean 库，其中使用了 Claude 模型辅助形式化大量现代数学，并依赖多个独立检查器进行交叉验证。

**「影响」** 对 Lean 和 Mathlib 生态，黎曼猜想现已成为可机器检查、可被后续形式化数论工作引用的认证结果，可能加速大规模数学库的交叉验证实践。

**「社区讨论」** 多数评论认为多内核交叉检查显著降低了证明利用内核漏洞的风险，并肯定 Levent Alpöge 对 Claude 的引导作用。少数提醒过去有伪造 Collatz 反证通过单个检查器，交叉检查并非完全独立，仍需人类专家复核。

<details><summary>参考链接</summary>
<ul>
<li>Lean verification of the Riemann Hypothesis | Lean community blog</li>
<li>Anthropic mathematician proves Riemann hypothesis, most famous ...</li>

</ul>
</details>

**标签**: `#Lean`, `#Riemann Hypothesis`, `#formal verification`, `#AI-assisted theorem proving`, `#mathematics`

---

<a id="item-tech-news-2"></a>
### [GPGME 2.3.0 前版本漏洞影响 GitLab 等应用](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

GnuPG 项目披露了 GPGME 2.3.0 之前版本中的一个漏洞，该漏洞可能被利用导致远程代码执行。所有以共享库、DLL 或静态链接方式使用受影响 GPGME 版本的软件均受影响，包括 GitLab、Gpg4win、GnuPG Desktop/VS-Desktop、多数邮件客户端、许多 XMPP 客户端、Samba 和 Flatpak。该漏洞由 Johan Carlsson 发现，GitLab 于 2026-11-12 通知项目，原定 2026-11-25 协调披露，后因 Ruby2Shell 漏洞提前至 2026-11-20。社区中有评论认为该问题实际是双重释放（double free）漏洞，而非完整的远程代码执行链，因此对严重性存在争议。

hackernews · gdgghhhhh · 11月21日 08:32 · [社区讨论](https://news.ycombinator.com/item?id=50587208)

**「背景」** GPGME（GnuPG Made Easy）是 GnuPG 项目提供的加密 API 库，许多应用通过它处理 OpenPGP 密钥和签名操作。该漏洞被编号为 CVE-2026-129975，是一个双重释放（double free）缺陷，可由恶意构造的 OpenPGP 密钥触发；GnuPG 公告明确指出不能排除远程代码执行，并建议立即更新到 2.3.0 或更高版本。受影响软件包括使用 GPGME 作为共享库、DLL 或静态链接的邮件客户端、XMPP 客户端、Samba、Flatpak 以及 GitLab 等。

**「影响范围」** 所有使用 GPGME 2.3.0 之前版本的软件均受 CVE-2026-129975 影响，包括多数邮件客户端、XMPP 客户端、Samba、Flatpak 以及 GitLab 的签名提交路径。攻击者可通过恶意 OpenPGP 密钥触发该缺陷，导致数据泄露或潜在的远程代码执行；社区对是否构成完整 RCE 链仍有争议。

**「社区讨论」** 社区对严重性存在分歧：有评论指出该漏洞实际是双重释放（double free）而非完整的 RCE 链，并质疑报告是否夸大。另有评论提到 Red Hat 五年前已修复但上游遗漏，并主张使用 Rust 级工具链防止此类 C/C++ 问题。

<details><summary>参考链接</summary>
<ul>
<li>GnuPG Warns Critical GPGME Flaw Could Expose App Data via ...</li>
<li>Fwd: GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975)</li>
<li>GPGME Double Free Bug Hid in GnuPG&#x27;s Glue Library for 24 Years ...</li>
<li>GnuPG Warns Critical GPGME Flaw Could Expose App Data via ...</li>
<li>GnuPG Security Advisory for GPGME (T8557,CVE-2026-129975)</li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#GPGME`, `#GnuPG`

---

<a id="item-tech-news-3"></a>
### [微软用 USB4 让多台 PC 合跑一个 AI 模型](https://videocardz.com/newz/microsoft-brings-rdma-over-usb4-to-windows-allowing-multiple-pcs-to-run-one-local-ai-model) ⭐️ 8.0/10

微软发布了 Windows 下 RDMA over USB4 的开发者预览，允许通过普通 USB4 连接在多个 PC 之间共享内存和 GPU 算力，共同运行同一个本地 AI 模型，而无需专用网卡或交换机。演示中，三台搭载 AMD Ryzen AI Max+ 395 的设备以 4-bit 量化运行 Qwen3-235B-A22B，推理速度约为 18.5 token/s。该功能将通过 Windows Insider 渠道推送。

telegram · zaihuapd · 11月21日 06:13

**「背景」** RDMA（远程直接内存访问）允许一台计算机直接访问另一台计算机的内存，绕过操作系统和 CPU，降低延迟与开销；此前在 Windows 上通常需要专用 RDMA 网卡或交换机。微软于 11 月 19 日的开发者预览将 RDMA over USB4 加入 Windows 的 NetworkDirect 接口，使兼容框架能通过标准 USB4 线缆连接多台 PC，共享内存容量与 GPU 计算资源，从而运行单台机器放不下的本地 AI 模型。

**「影响」** 拥有多台支持 USB4 的 Windows PC 的开发者可组合这些机器的内存与 GPU 运行单个超出单机内存的本地模型，官方预览演示三台 AMD Ryzen AI Max+ 395 以 4-bit 量化运行 Qwen3-235B-A22B 约 18.5 token/s，无需专用 RDMA 网卡或交换机。该功能目前仅为开发者预览，需等待 Windows Insider 推送，实际可用性与兼容性仍有限。

<details><summary>参考链接</summary>
<ul>
<li>Introducing RDMA over USB4® on Windows: run larger local AI models ...</li>
<li>Microsoft previews linking Windows PCs over USB4 to run larger AI ...</li>
<li><a href="https://techcommunity.microsoft.com/blog/microsoftusbblog/introducing-rdma-over-usb4%C2%AE-on-windows-run-larger-local-ai-models-across-pcs/4574602">Introducing RDMA over USB4® on Windows: run larger local AI ...</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#RDMA`, `#USB4`, `#Local AI`, `#AI infrastructure`

---

<a id="item-tech-news-4"></a>
### [浙江大学首次真机实现量子随机存储器 QRAM](https://finance.sina.com.cn/stock/2026-11-21/doc-iniznhsk3530826.shtml) ⭐️ 8.0/10

浙江大学团队在自主制备的超导量子芯片“天目 2 号”上，全球首次真机实现量子随机存储器（QRAM），成果发表于《自然·物理》。该原型成功运行了可调取 4 位和 8 位数据的方案，准确率分别为 80.9%和 60.4%，线路深度较未优化方案降低 30%以上，并首次验证该架构具备局部抗噪特性。这一进展相当于为量子计算机配备“高速内存”，但当前 8 位数据的准确率仍偏低，规模化能力也尚未验证。

telegram · zaihuapd · 11月21日 08:31

**「背景」** 量子随机存储器（QRAM）是量子计算中用于按地址读取叠加态数据的存储模型，类似于经典计算机中的内存，对加速数据库搜索、量子机器学习等算法至关重要。此前 QRAM 主要停留在理论设计和仿真阶段，尚未在真实量子硬件上实现。浙江大学团队在自研超导量子芯片“天目 2 号”上完成真机演示，相关成果发表于《自然·物理》。

**「影响」** 对量子计算硬件和算法研究者而言，该成果提供了首个可在超导芯片上运行的真机 QRAM 原型，但其 60.4%的 8 位准确率表明该方案距离容错量子内存应用仍有明显差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.mydrivers.com/1/1167/1167501.htm">news.mydrivers.com/1/1167/1167501.htm</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#QRAM`, `#superconducting qubits`, `#quantum memory`, `#Nature Physics`

---

<a id="item-tech-news-5"></a>
### [特斯拉推送 FSD v15：安全处理提升 25 倍](https://x.com/Tesla/status/2124222447855743019) ⭐️ 8.0/10

特斯拉今日开始向海外用户推送 FSD v15。本次更新将安全关键场景的处理能力提升至 25 倍，并引入“Tesla Reality View”可视化界面，可在车机屏幕叠加摄像头画面与 FSD 行驶规划，支持全屏、地图或分屏视图以及安静模式。导航可将转弯等信息叠加显示，转向灯提示音更轻柔并逐渐减弱。更新还优化了坑洼、碎片等路况的行驶体验，以及学校、恶劣天气下的速度控制。

telegram · zaihuapd · 11月22日 00:03

**「背景」** 特斯拉的 FSD（Full Self-Driving）是该公司的高级驾驶辅助与自动驾驶软件套件；此前 FSD 主要在北美推送，2026 年 7 月才通过 FSD v14 Lite 在韩国向部分早期用户开放，且仅限美国生产的 Model 3 和 Model Y。根据发布前的预告，FSD v15 预计随假日更新到来，并将带来新的可视化界面，马斯克称其会以“令人震撼的方式呈现现实”。

**「影响」** 海外 FSD 用户可预期在安全关键场景、坑洼/碎片路况及学校/恶劣天气速度控制上获得改进，并通过 Reality View 更直观查看 FSD 行驶规划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot">Tesla Autopilot - Wikipedia</a></li>
<li><a href="https://www.notateslaapp.com/news/5057/tesla-fsd-v15-coming-next-month-with-holiday-update-musk">Tesla FSD V 15 Arriving Next Month: Home Garage... - Not a Tesla App</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#FSD`, `#autonomous driving`, `#AI`, `#software update`

---

<a id="item-tech-news-6"></a>
### [Graham Dumpleton 发布 AI 辅助 Rust 服务器 Muru](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

2026 年 11 月 4 日至 21 日，mod\_wsgi 创始人 Graham Dumpleton 发布了名为 Muru 的新 AI 辅助 Rust 服务器，用于在开发和生产环境运行 ASGI 与 WSGI Python 应用。他在三周内连续发表了 18 篇详细开发日志，涵盖 worker 架构、导入一次多次 fork、开发环境 HTTPS、WSGI/ASGI 共存、变更式发布、金丝雀、Kubernetes 协同、扩缩容至零、定时 overlay 以及页面工具栏与追踪等功能。Muru 目前处于早期阶段，但结合 Dumpleton 在 mod\_wsgi 上 20 年的经验，目标是打造他本人信任且用户也能信任的 Python web 服务工具。

rss · Simon Willison · 11月21日 23:56

**「背景」** WSGI 是 Python Web 应用与服务器之间的同步接口标准，而 ASGI 是其异步后继，支持 WebSocket 等协议。Graham Dumpleton 大约 20 年前创建了 mod\_wsgi，用于在 Apache 中托管 Python WSGI 应用。Muru 是他基于 Rust 并用 AI 辅助开发的新服务器，旨在兼顾开发与生产环境。

**「影响」** 对关注 Python Web 服务部署的开发者来说，Muru 提供了一个由资深维护者设计、但尚未证明生产就绪的早期 Rust ASGI/WSGI 服务器选项。

**标签**: `#Python`, `#Rust`, `#ASGI`, `#WSGI`, `#web servers`

---

<a id="item-tech-news-7"></a>
### [OpenRouter 警告 MiniMax 提示词疑遭第三方读取](https://news.ycombinator.com/item?id=50585962) ⭐️ 7.0/10

OpenRouter 通过邮件警告用户，发往 MiniMax 模型的请求内容可能已被第三方读取。安全研究者在 2026 年 7 至 10 月向 MiniMax 模型发送包含测试 URL 的提示词，第三方在 40 到 130 小时后访问了这些 URL。OpenRouter 认定问题出在 MiniMax 及其转发方 AtlasCloud、Novita、StreamLake，并已下架相关端点的“零数据保留”标签。OpenRouter 建议曾发送敏感凭证的用户更换 API Key 和密码，但其官网尚未公布相关消息。

telegram · zaihuapd · 11月21日 06:53

**「背景」** OpenRouter 是一个统一的 LLM API 平台，其“零数据保留”标签表示提供商不会保留用户请求数据。此次测试通过发送唯一 URL 并观察是否被访问，可推断提示词是否被外部读取。

**「影响」** 使用 OpenRouter 调用 MiniMax 或上述转发方的用户应假定这些提示词可能已泄露，并立即更换其中涉及的 API Key、密码等敏感凭证。

**标签**: `#security`, `#AI`, `#OpenRouter`, `#MiniMax`, `#data-privacy`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [特朗普称仍支持卢特尼克，望黄仁勋道歉后回归](https://www.reuters.com/world/us/trump-says-he-still-backs-lutnick-urges-nvidias-huang-apologize-2026-11-20/) ⭐️ 8.0/10

据路透社报道，美国总统特朗普 11 月 20 日表示，他仍支持商务部长卢特尼克，并希望已辞职的英伟达 CEO 黄仁勋“郑重道歉后回归”；此前英伟达风波引发外界质疑卢特尼克对中国芯片销售的处理，特朗普称已与中国国家主席习近平谈及此事，但这一说法与财长贝森特称通话未涉黄仁勋相矛盾。

telegram · zaihuapd · 11月21日 05:03

**「背景」** 此前，英伟达因向中国出售先进 AI 芯片引发争议，黄仁勋已辞职，卢特尼克因被指放宽对华芯片销售而面临共和党人批评。

**「影响」** 黄仁勋辞职已使英伟达失去在美国对华人工智能芯片管控中最具影响力的反对声音，特朗普要求其道歉后回归的表态可能影响该公司领导层走向及美中芯片管控博弈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/11/trump-was-in-bed-with-jensen-critics-balk-at-huangs-wish-to-return-to-nvidia/">“ Trump was in bed with Jensen ”: Critics balk at Huang ’s wish to...</a></li>
<li><a href="https://www.cnn.com/2026/11/20/politics/trump-news-conference-takeaways">Takeaways from Trump ’s news briefing on Putin, Xi | CNN Politics</a></li>
<li><a href="https://observer.com/2026/11/jensen-huang-resigns-leaving-nvidias-china-chip-fight-without-its-chief-advocate/">Jensen Huang Resigns, Leaving Nvidia’s China Chip Fight In ...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-11-13/jensen-huang-exit-sets-up-us-china-showdown-over-ai-chip-curbs">Jensen Huang Exit Sets Up US-China Showdown Over AI Chip ...</a></li>

</ul>
</details>

**标签**: `#US-China trade`, `#Nvidia`, `#semiconductor export controls`, `#Trump administration`, `#corporate leadership`

---