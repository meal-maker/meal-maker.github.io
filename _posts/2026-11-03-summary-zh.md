---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 45 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [Linux 内核 IPv4 TCP 释放后使用漏洞预警（CVE-2026-98432）](#item-tech-news-1) ⭐️ 9.0/10
2. [vLLM v0.33.0rc3 发布：CUDA 13.0 与 PyTorch 2.14](#item-tech-news-2) ⭐️ 8.0/10
3. [ChatGPT 分享链接漏洞可致账号被接管](#item-tech-news-3) ⭐️ 8.0/10
4. [《连线》调查：400 多个 AI 应用暗藏色情深伪功能](#item-tech-news-4) ⭐️ 8.0/10
5. [Astra 权重编辑改进 Qwen](#item-tech-news-5) ⭐️ 7.0/10
6. [Subvocal 推出射频无声语音眼镜并开放预订](#item-tech-news-6) ⭐️ 7.0/10
7. [Cloudflare 将 DNS 构建延迟减半、内存使用降低 85%](#item-tech-news-7) ⭐️ 7.0/10
8. [美国人口普查局 AI 采用调查被行政令改问‘超级智能’](#item-tech-news-8) ⭐️ 7.0/10
9. [LightMIS：适用于边缘设备的超轻量医学图像分割模型](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [CNBC 盘中异动：Oracle 跌 6%，Marvell 1150 亿美元收购 Lumentum](#item-finance-news-1) ⭐️ 7.0/10
2. [英国拟将多数移民定居标准年限延至 10 年](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Linux 内核 IPv4 TCP 释放后使用漏洞预警（CVE-2026-98432）](https://telegram.me/zaihuapd/44866) ⭐️ 9.0/10

Linux 内核 IPv4 TCP 协议栈存在高危释放后使用漏洞（CVE-2026-98432），攻击者可从网络侧利用该漏洞，无需认证或用户交互。Anthropic 已公布针对 MPTCP 监听端口的远程代码执行（RCE）利用示例。该漏洞并非仅影响 MPTCP 场景：Go 官方安全团队提示，自 Go 1.24 起 Linux 上的 listen socket 默认启用 MPTCP，因此 Go 编写的服务默认处于暴露状态；即使没有 MPTCP 监听，也可能受到同类攻击。提醒服务器管理员更新内核以降低风险。

telegram · zaihuapd · 11月3日 02:37

**「背景」** CVE-2026-98432 是 Linux 内核 IPv4 TCP 握手路径中的释放后使用漏洞，影响内核 4.4 及更高版本（tool-1-1）。远程未认证攻击者可发送携带 IP 选项的构造 TCP 数据包，利用 TCP 连接请求处理中的竞争条件，造成内核内存破坏或远程代码执行（tool-1-2；tool-1-3）。该问题并非仅存在于 MPTCP 场景，但自 Go 1.24 起 Linux 上监听套接字默认启用 MPTCP，使得相关 Go 服务默认暴露于该攻击面。

**「影响」** 该漏洞可被网络侧攻击者无需认证或用户交互利用，实现远程代码执行（CVSS 9.8）；由于 Go 1.24 起 Linux 监听套接字默认启用 MPTCP，大量 Go 服务默认暴露，且已有针对 MPTCP 监听器的公开利用示例。所有相关系统应尽快更新内核（上游已于 10 月 15 日修复）或部署网络层过滤；仅依赖程序级禁用 MPTCP（如 godebug multipathtcp=0）并不完全可靠，可能因遗漏单个监听器而失效。

**「社区讨论」** 评论区有人提出可用 iptables/nftables 在 raw PREROUTING 阶段通过 u32 规则丢弃特定 TCP 选项来阻止利用，但也有用户质疑 Ubuntu 为何迟迟未修复，并担忧消费级路由器长期不更新内核。RHEL 提供了一种缓解措施，但官方声称只能减少暴露且无法完全防止，具体原因未作详细说明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/2026-160-aws/">CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free ...</a></li>
<li><a href="https://access.redhat.com/security/vulnerabilities/RHSB-2026-016">RHSB-2026-016 Use-after-free - kernel IPv4 (CVE-2026-98432 ...</a></li>
<li><a href="https://www.fosslinux.com/163418/cve-2026-98432-linux-tcp-use-after-free.htm">CVE-2026-98432: The Linux TCP Use-After-Free Flaw Explained</a></li>
<li><a href="https://lilting.ch/en/articles/linux-ipv4-tcp-options-uaf-mptcp-rce">CVE - 2026 - 98432 Linux TCP Use-After-Free Can Give... | lilting channel</a></li>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux&#x27;s October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>
<li><a href="https://www.openwall.com/lists/oss-security/2026/10/30/1">oss-security - Fwd: Protecting against CVE - 2026 - 98432 when using Go ...</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#CVE`, `#TCP vulnerability`, `#MPTCP`, `#Go`

---

<a id="item-tech-news-2"></a>
### [vLLM v0.33.0rc3 发布：CUDA 13.0 与 PyTorch 2.14](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) ⭐️ 8.0/10

vLLM v0.33.0rc3 已发布，包含 927 个提交、389 位贡献者，其中 122 位为新贡献者。该版本将 PyTorch 升级到 2.14.0（torchvision 0.29.0、Triton 3.8.0），并且只发布 CUDA 13.0 的 wheel 和镜像，不再发布 CUDA 12.9 产物；CUDA wheel 现在也对 libtorch 保持 ABI 稳定。新增 Reflection Beam-1.0、Yandex AliceAI-Foundation-80B-A3B、Recursive Flint、Muse Spark Open、Step-5 Preview 等多种模型支持。在 NVIDIA 与 AMD 平台上有明显解码性能提升，包括 FA4 稀疏 MLA、MXFP4 专家 FP8 路径、ROCm 10.0 与 MonoKernel 等。破坏性变更包括移除 Medusa 和 MLP speculator、删除旧 Ray compiled-graph executor，并停用若干参数。

github · khluu · 11月2日 10:10

**「背景」** vLLM 是一个广泛使用的 LLM 推理服务框架，其发布版本通过预编译 CUDA/ROCm wheel 和 Docker 镜像分发，用户依赖这些产物在 GPU 上部署模型。此前版本同时提供 CUDA 12.9 和更高版本的构建，而 v0.33.0 起转向仅支持 CUDA 13.0，这影响仍停留在较旧 CUDA 运行时的用户。libtorch ABI 稳定性意味着 CUDA wheel 与 libtorch 共享 ABI，能减少因 PyTorch 版本不一致导致的链接问题。

**「影响」** 对仍使用 CUDA 12.9 的 vLLM 部署，v0.33.0rc3 不再提供 wheel 和 Docker 镜像，必须升级到 CUDA 13.0；同时依赖 Medusa、MLP speculator 或旧 Ray compiled-graph executor 的用户需要切换到替代方案。

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#PyTorch`, `#CUDA`

---

<a id="item-tech-news-3"></a>
### [ChatGPT 分享链接漏洞可致账号被接管](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter 研究团队发现并披露了一个已被修复的 ChatGPT 分享链接漏洞。攻击者可构造恶意分享链接，当已登录用户仅打开链接且无需安装应用时，就能在该用户会话中执行代码，读取私密对话并将数据发送至外部服务器。漏洞源于预览功能与图表组件之间的消息处理缺陷。OpenAI 已将该问题定级为 P1，并于 10 月 26 日修复，同时向研究团队支付 5000 美元赏金。

telegram · zaihuapd · 11月2日 10:24

**「背景」** ChatGPT 允许用户将对话以链接形式分享给他人查看或继续交互，这类链接通常可在已登录状态下直接打开。分享链接中的预览和图表渲染等功能会处理消息内容，因此消息处理缺陷可能被用于恶意代码执行。

**「影响」** 在 10 月 26 日修复前打开过来源不明 ChatGPT 分享链接的用户，可能已泄露私密对话并面临账号被接管风险。

**标签**: `#security`, `#vulnerability`, `#ChatGPT`, `#OpenAI`, `#account-takeover`

---

<a id="item-tech-news-4"></a>
### [《连线》调查：400 多个 AI 应用暗藏色情深伪功能](https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/) ⭐️ 8.0/10

《连线》11 月 2 日报道，一个由 400 多个关联应用与网站组成的网络以宠物画像、语言学习等普通 AI 工具为掩护，在特定条件下加载色情深度伪造界面，允许用户上传他人照片生成露骨图像或视频。9 月时仍有 27 款相关应用在 Google Play 上架，累计下载超 35 万次，且不少被标为适合所有年龄。苹果收到《连线》线索后下架 19 款应用，称开发者审核通过后替换了远端网页内容；谷歌在被联系前已移除多数应用，Meta 则阻止 209 款相关应用投放广告。报道通过代码、域名和广告追踪将该网络与中文开发者及一家香港注册公司联系起来，但运营方未回应置评，关联属于调查判断。

telegram · zaihuapd · 11月2日 12:45

**「背景」** 深度伪造（deepfake）指利用人工智能生成或篡改图像、视频、音频的合成媒体，常被用于在未经同意的情况下制作色情内容。应用商店一般只审核提交时的应用包，如果开发者让应用在审核通过后从远程服务器加载不同界面或功能，就可能绕过内容审查，在普通工具外观下隐藏违规功能。

**「影响」** 苹果下架和谷歌移除表明，应用商店上架审核通过并不自动保证后续使用安全，因为开发者可在审核后替换远端网页内容，用户上传照片至这类看似无害的 AI 工具可能被用于生成露骨内容。

**标签**: `#AI伦理`, `#深度伪造`, `#应用安全`, `#科技调查`, `#平台审核`

---

<a id="item-tech-news-5"></a>
### [Astra 权重编辑改进 Qwen](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 7.0/10

一项名为 Astra 的工作展示了直接读取和编辑神经网络权重的能力，并在小规模 Qwen 模型上报告称可将其数学表现提升约 5 倍。该结果来自一篇技术博客，在 Hacker News 上引发大量讨论，部分观点认为这代表模型对自身权重具备超出预期的原生理解。但一位从事权重空间学习的研究者提醒，应阅读原论文后再下结论，并指出博客表述可能夸大成果，而权重编辑、生成和识别已有前期工作。由于缺乏可核实的源内容，具体方法、版本、提升幅度和可复现性仍需谨慎看待。

hackernews · dbreunig · 11月2日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**「背景」** 大型语言模型通常被用于优化提示词或代码等文本产物，而其自身的神经网络权重被视为固定数据。这篇博客提出“权重空间编程”：让 LLM 直接读取并修改另一个模型的权重。在实验中，一个名为 Astra 的前沿模型读取了 Qwen 3.5-0.8B 的权重，诊断出重复/循环问题并手工编辑了 131,072 个权重，据报告其数学表现得到改善。

**「对模型编辑实践的影响」** 该研究表明，像 GPT-6 Astra 这样的 LLM 可直接读取并编辑模型权重而无需训练；在 Qwen 上仅调整约 0.016% 的参数（131,072 个权重）就报告了数学性能提升，但社区指出结果可能被夸大且此前已有相关工作。

**「社区讨论」** HN 讨论中观点分歧明显：部分用户对模型能直接编辑权重并显著提升 Qwen 数学能力表示震惊，认为这超出人类对神经元层面的理解。另一些用户则认为当前大模型本就擅长快速掌握复杂系统，或指出该能力可能来自训练数据中的权重数据而非涌现，更有研究者提醒博客可能夸大了结果且权重空间编辑已有先例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://huggingface.co/akhaliq/Qwen3.5-0.8B-weight-space-programming">akhaliq/ Qwen 3.5-0.8B- weight - space - programming · Hugging Face</a></li>
<li><a href="https://elsolitario.org/en/2026/11/02/mit-csail-astra-edits-0-016-of-qwen3-weights/">Weight-Space Programming: How Astra Edits Weights</a></li>
<li><a href="https://kingy.ai/blog/weight-space-programming-ai-agent-model-weights/">Weight-Space Programming: GPT-6 Astra Edits Qwen - kingy.ai</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#neural networks`, `#large language models`, `#model editing`, `#AI research`

---

<a id="item-tech-news-6"></a>
### [Subvocal 推出射频无声语音眼镜并开放预订](https://news.ycombinator.com/item?id=50340088) ⭐️ 7.0/10

Subvocal Company \(YC F26\) 发布了一款智能眼镜原型，可通过射频（RF）感知用户无声唇动或闭口内部言语，并将其解码为文本，速度接近正常语速。创始人曾在佐治亚理工学院就读，最初在 TreeHacks 黑客松上用 EMG 电极构建原型，后因汗液、干扰和佩戴问题转向 RF 方案；眼镜发射类似蓝牙的无线电波穿过面部，被舌头、嘴唇和软腭调制，团队通过低噪声 RF 传感、天线布局仿真和大规模付费数据采集训练模型以实现跨用户泛化。演示视频展示了 YC 的 Dave 在仅约 20 句校准后使用该系统；团队计划继续研发以优化边缘情况，并在 2027 年第一季度发货，首批 500 台预购可享受 200 美元折扣。

hackernews · aarushyadav · 11月2日 17:16

**「背景」** 无声语音识别过去常通过肌电图（EMG）检测面部肌肉电信号，MIT Media Lab 的 AlterEgo 是知名研究原型；射频感知则是发射低功率无线电波并分析口腔内部运动对反射信号的调制，无需皮肤接触。Subvocal 的方案建立在后一种原理上，但此前从学术概念到可穿戴产品存在工程挑战。

**「影响」** 对于需要在图书馆、办公室等安静或隐私敏感环境进行语音输入的用户，这款眼镜提供了不发声、不贴电极的潜在替代方案，但当前仅开放 500 台预购且计划 2027 年第一季度发货，其跨用户一致性和实际性能尚未经独立验证。

**「社区讨论」** 评论区兴趣浓厚，有人已预购并提出针对大鼻梁、高鼻托或大头围的适配请求，希望保留可调节金属鼻托或提供可附加在现有眼镜上的版本；也有用户担心推断是否在设备端完成及隐私问题，并质疑能否用笔记本摄像头实现类似功能，但作者尚未回应。

**标签**: `#silent speech recognition`, `#wearable computing`, `#RF sensing`, `#accessibility`, `#smart glasses`

---

<a id="item-tech-news-7"></a>
### [Cloudflare 将 DNS 构建延迟减半、内存使用降低 85%](https://blog.cloudflare.com/dns-targeted-zone-builds/) ⭐️ 7.0/10

Cloudflare 在其技术博客中介绍了通过针对性 DNS 区域构建优化，将 DNS 构建延迟减半，内存使用降低 85%。这一改进聚焦于仅构建受变更影响的 DNS 区域，而非全量构建，从而提升了构建效率。该优化反映了在高内存成本环境下对基础设施效率的重视。

hackernews · wondersky · 11月2日 14:47 · [社区讨论](https://news.ycombinator.com/item?id=50337558)

**「背景」** 在 Cloudflare 的 DNS 架构中，DNS 区域（zone）包含该域名的全部记录；过去只要区域设置发生变化，系统就会重建整个区域，即使区域包含数千万条记录，导致内存占用和构建延迟很高。本次优化通过引入目标化构建规划器和统一调度器，只重建发生变化的区域部分，从而避免全量重建。根据工具结果，此前峰值内存曾达 79 GiB，最大 p99 构建延迟达 14.6 分钟，说明全量重建的资源消耗显著。

**「影响」** 对于 Cloudflare 及其 DNS 服务用户，该优化意味着 DNS 变更生效更快、基础设施资源消耗更低，可能改善服务响应和运营成本。

**「社区讨论」** 社区讨论中，有评论质疑每秒 700 次变更对于 Cloudflare 规模是否偏低，并关注此类优化前后可能引入的 bug；同时也有评论肯定 Cloudflare 的技术博客质量，并讨论内存成本上升背景下效率优化的投资回报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dns-targeted-zone-builds/">How we halved DNS build delay and cut memory use by 85%</a></li>
<li><a href="https://daily.dev/posts/how-we-halved-dns-build-delay-and-cut-memory-use-by-85--jhnmypmtx">How we halved DNS build delay and cut memory use by 85%</a></li>
<li><a href="https://runtimewire.com/article/cloudflare-dns-targeted-zone-builds-memory-delay">Cloudflare stops rebuilding 20-million-record DNS zones to ...</a></li>

</ul>
</details>

**标签**: `#dns`, `#cloudflare`, `#performance`, `#systems`, `#infrastructure`

---

<a id="item-tech-news-8"></a>
### [美国人口普查局 AI 采用调查被行政令改问‘超级智能’](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/) ⭐️ 7.0/10

西蒙·威利森重新分析了美国人口普查局企业趋势与展望调查（BTOS）的 AI 采用数据，发现该调查的问题措辞发生了两次重大变化。2025 年 11 月 17 日之前，问卷询问企业是否在“生产商品或服务”中使用 AI；之后改为“在任何业务职能中”使用 AI，导致前后数据不可直接比较。在更宽泛的措辞下，250 人以上大企业报告使用 AI 的比例从 2025 年 9 月旧口径的约 12%上升到 2026 年 2 月约 30%、2026 年 10 月约 40%。自 2026 年 10 月 19 日起，由于第 14434 号行政令，问卷将“AI”替换为“超级智能（Super Intelligence/SI）”，首批采用新措辞的调查结果预计于周四发布。

rss · Simon Willison · 11月2日 13:31

**「背景」** BTOS 是美国人口普查局每两周对约 20 万家雇主企业开展的一项调查，总样本池约 120 万家企业，单个企业每 12 周完成一次问卷；数据通常在隔周周四上午 10 点发布。该调查的 AI 采用数据曾因 Apollo Global Management 在 2025 年 9 月的图表显示大公司 AI 采用放缓而受到关注。

**「影响」** 对于依赖该调查追踪美国企业 AI 采用趋势的研究者、分析师和管理者，2025 年 11 月“生产商品或服务”改为“任何业务职能”以及 2026 年 10 月改为“超级智能”后，新旧序列不可直接比较；当前 250 人以上企业约 40%的数字反映的是更宽的业务职能口径，而非此前更窄的生产口径。

**标签**: `#AI`, `#policy`, `#data`, `#Census Bureau`, `#executive order`

---

<a id="item-tech-news-9"></a>
### [LightMIS：适用于边缘设备的超轻量医学图像分割模型](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 7.0/10

LightMIS 是一个具有 13.1 万参数的 2D 二值医学图像分割模型，作者在 Reddit 上以论文作者身份公布了该工作。该模型直接聚合多尺度编码器特征，省去可学习的逐级解码器；在与 nnWNet 相同的 nnU-Net 协议（nnU-Net v2.3.1）下训练和评估，覆盖 6 个数据集、5 种成像模态，其在模态平均 Dice 和 IoU 上接近 nnWNet，但参数量减少 98.14%，GFLOPs 减少 94.58%。在搭载 Arm Mali-G52 MC2 GPU 的实际边缘设备上，完整 LightMIS 模型运行速度约为 nnWNet 的 10.5 倍，所有变体均实现 100% GPU 算子覆盖，无 CPU 回退。代码、检查点和复现细节已公开。该结果目前主要由作者自行报告，尚未经独立验证。

reddit · r/MachineLearning · /u/OkLion2068 · 11月2日 20:22

**「背景」** 传统医学图像分割模型（如 nnU-Net 家族）通常采用编码器-解码器结构，并通过逐级解码器恢复分辨率，因此参数量和计算量较大，在边缘设备上部署受限。LightMIS 针对 2D 二值医学图像分割提出一种无学习式逐级解码器的超轻量卷积网络：它用五级编码器提取特征，通过尺度对齐投影块将多尺度输出统一到同一分辨率，再进行一次聚合并用自适应融合级联细化。该设计旨在以远少于 nnWNet 的参数和 GFLOPs 获得接近的分割精度，并提升边缘硬件上的推理速度。

**「影响」** 对于希望在边缘设备上部署 2D 医学图像分割的开发者，LightMIS 在作者自报的 nnU-Net v2.3.1 协议下以 131K 参数、比 nnWNet 少 98.14%参数和 94.58% GFLOPs，并在 Arm Mali-G52 MC2 GPU 上快约 10.5 倍，同时保持接近 nnWNet 的 Dice/IoU 均值。该结果尚未经独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.28327">LightMIS: Ultra-Lightweight Medical Image Segmentation ...</a></li>
<li><a href="https://arxiv.org/abs/2609.28327">[2609.28327] LightMIS : Ultra-Lightweight Medical Image ...</a></li>

</ul>
</details>

**标签**: `#medical image segmentation`, `#edge AI`, `#deep learning`, `#model efficiency`, `#computer vision`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [CNBC 盘中异动：Oracle 跌 6%，Marvell 1150 亿美元收购 Lumentum](https://www.cnbc.com/2026/11/02/stocks-making-the-biggest-moves-midday-orcl-spcx-tem-rivn.html) ⭐️ 7.0/10

CNBC 报道周一盘中多只个股异动：Oracle 因申请发行 100 亿美元普通股和 100 亿美元优先票据为 AI 建设融资，股价下跌 6%；Marvell 与 Lumentum 达成 1150 亿美元全股票收购，Lumentum 下跌 15%，Marvell 下跌 9%。IDEXX 三季度营收 12.1 亿美元、同比增长 10%，股价上涨 20%；Tempus AI 营收 4.115 亿美元、同比增长 23%，股价上涨近 12%。

rss · CNBC Finance · 11月2日 20:00

**「背景」** 此次盘中异动发生在三季度财报季，多家公司业绩与 FactSet 共识预期比较；同时，油价下跌拖累能源股。

**标签**: `#stock movers`, `#earnings`, `#mergers and acquisitions`, `#capital raise`, `#market update`

---

<a id="item-finance-news-2"></a>
### [英国拟将多数移民定居标准年限延至 10 年](https://www.gov.uk/government/news/home-secretary-unveils-new-rules-for-migrants-settling-in-the-uk) ⭐️ 7.0/10

英国政府向议会提交提案，拟将多数移民申请永久居留的标准年限从 5 年延长至 10 年。年收入超过 50,271 英镑者、医生护士教师等公共服务岗位人员可走 5 年通道，最高收入者最快 3 年即可申请。

telegram · zaihuapd · 11月2日 23:50

**「背景」** 英国内政部此前就相关变更进行了公开咨询，咨询期已于 2026 年 2 月 12 日结束，目前该方案尚未正式立法。

**「议员警告的潜在影响」** 英国议员警告，该提案可能加剧医疗和社会护理领域的人员短缺，并带来类似“疾风世代”丑闻的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gardencourtchambers.co.uk/potential-legal-challenge-to-home-office-proposals-to-retrospectively-extend-earned-settlement-ilr-to-ten-years/">Potential legal challenge to Home Office proposals to retrospectively...</a></li>
<li><a href="https://www.theguardian.com/politics/2026/nov/01/home-secretary-shabana-mahmood-immigration-leave-to-remain-windrush">Home secretary to make some migrants wait 10 years or more ...</a></li>

</ul>
</details>

**标签**: `#immigration policy`, `#UK`, `#labor market`, `#public services`, `#settlement rules`

---