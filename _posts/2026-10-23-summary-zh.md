---
layout: default
title: "Horizon Summary: 2026-10-23 (ZH)"
date: 2026-10-23
lang: zh
---

> 从 42 条内容中筛选出 18 条重要资讯。

---

**科技新闻**
1. [OpenShell：面向自主 AI agent 集群的安全私有运行时](#item-tech-news-1) ⭐️ 8.0/10
2. [在 Android 设备上运行 iOS 16.5 固件的研究项目](#item-tech-news-2) ⭐️ 8.0/10
3. [任天堂 Switch 2 越狱实现解密文件系统读写](#item-tech-news-3) ⭐️ 8.0/10
4. [eMudhra 宣布退出全球 SSL/TLS 证书业务](#item-tech-news-4) ⭐️ 8.0/10
5. [比 earcut 更快：489 毫秒三角化 370 万地图多边形](#item-tech-news-5) ⭐️ 8.0/10
6. [澳洲法院裁定苹果开放第三方商店](#item-tech-news-6) ⭐️ 8.0/10
7. [甲骨文发布 Java SE 高危漏洞安全警报](#item-tech-news-7) ⭐️ 8.0/10
8. [333 个被植入后门的 Tor 出口节点下线](#item-tech-news-8) ⭐️ 8.0/10
9. [Nvidia 禁运 B300 芯片现身中国国有网络](#item-tech-news-9) ⭐️ 8.0/10
10. [Quad9 DNS 解析器将退出法国](#item-tech-news-10) ⭐️ 7.0/10
11. [pwn.watch：实时追踪被利用漏洞的仪表盘](#item-tech-news-11) ⭐️ 7.0/10
12. [Anthropic 向 Agentic AI 基金会捐赠 Agent Skills 标准](#item-tech-news-12) ⭐️ 7.0/10
13. [Carbon-X 14.8B 开放 DNA 文本联合模型](#item-tech-news-13) ⭐️ 7.0/10
14. [Open-XTTS-Trainer 开源：一键训练 XTTS v2 三组件并扩展新语言](#item-tech-news-14) ⭐️ 7.0/10
15. [可转向小型 TTS 压缩至 11.84 MB，WER 不变，UTMOS 降约 0.1](#item-tech-news-15) ⭐️ 7.0/10
16. [研究：智能电视关闭 ACR 后仍上报内容数据](#item-tech-news-16) ⭐️ 7.0/10
17. [米哈游清华开源 GameScaling 键鼠操作模型](#item-tech-news-17) ⭐️ 7.0/10

**财经新闻**
1. [沪深 300 较 6 月高点回落 20%，A 股逼近熊市](#item-finance-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenShell：面向自主 AI agent 集群的安全私有运行时](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA 发布了 OpenShell，一个开源运行时，用于安全、私密地运行自主 AI agent 集群。它允许 agent 读取文件、安装软件包、调用 API 和使用凭据，同时试图避免对用户数据、秘密或网络的无限制访问。社区讨论集中在 agent 隔离、容器化、审计和数据外泄等安全问题上。该项目来自 NVIDIA，在 Hacker News 上引发 152 条评论，显示软件工程师和 AI 从业者对此高度关注。

hackernews · niemandhier · 10月22日 17:44 · [社区讨论](https://news.ycombinator.com/item?id=50198675)

**「背景」** 自主 AI 智能体在执行任务时通常需要读取文件、安装软件包、调用 API 并使用凭据，但直接运行可能带来数据泄露、越权访问和失控网络活动等风险。NVIDIA 开源的 OpenShell 是一个面向自主智能体集群的安全、私有运行时，它采用沙箱执行环境和声明式策略，让每个智能体只获得完成当前任务所需的最小权限，并在智能体工作负载之外强制执行。该项目将沙箱隔离、资源访问控制、凭据保护以及形式化策略验证结合起来，用于在保护数据、密钥和基础设施的同时管理成规模的智能体。

**「影响」** 面向需要批量运行自主 agent 并限制其数据、网络和凭据访问的团队，OpenShell 提供了一个可集成的开源容器管理运行时，但其安全效果取决于策略配置和配套审计。

**「社区讨论」** 社区中既有肯定，认为容器化是必须的且 OpenShell 便于管理，也有质疑，认为工具宣传看似兼顾能力与安全实则存在矛盾，且数据外泄和审计绕过风险仍存。一位用户称已在生产中使用 OpenShell，并提到 agent 追踪显示需要边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://docs.nvidia.com/openshell/home">NVIDIA OpenShell Developer Guide</a></li>
<li><a href="https://build.nvidia.com/openshell">NVIDIA OpenShell</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#security`, `#open-source`, `#containerization`, `#nvidia`

---

<a id="item-tech-news-2"></a>
### [在 Android 设备上运行 iOS 16.5 固件的研究项目](https://github.com/oosexgang/hackios-xnu-kernel) ⭐️ 8.0/10

一个名为 hackios-xnu-kernel 的 GitHub 项目展示了在 QEMU 以及 POCO X5 Pro 5G 和部分小米设备上运行完整 iOS 16.5 固件的能力，并提供了开源代码和配套网站。该项目被定位为研究试验台而非可用 ROM：每次引导会话只持续指定秒数，随后内核返回加载器并交出日志。实现覆盖了 iOS 16.5 的 XNU 内核在选定 Android 硬件上的启动与执行，吸引了较高的社区关注。项目未宣称提供日常使用的稳定系统，相关兼容性和限制仍以官方仓库说明为准。

hackernews · aghuang · 10月22日 15:26 · [社区讨论](https://news.ycombinator.com/item?id=50196718)

**「背景」** XNU 是苹果用于 iOS 和 macOS 的开源内核，其中 xnu-8796.121.2 对应 iOS 16.5。安卓设备通常使用基于 Linux 的内核，硬件抽象层与 iOS 不同，因此直接运行 iOS 需要额外适配。此前类似项目 darwin-vm 能在 QEMU 中启动 iOS/macOS 至最简 root shell，但无法运行图形界面；而本项目在部分安卓手机（如 POCO X5 Pro 5G 及一些小米设备）和 QEMU 上启动该 XNU 内核，并运行未经修改的 iOS 16.5 用户空间（包括 launchd、backboardd、SpringBoard 和应用），但会话仅持续数秒即返回加载器，属于研究演示而非完整 ROM。

**「影响」** 对于从事 iOS 内核、Android 底层启动和逆向工程的研究人员，该项目提供了可复现的实验环境，但不能替代日常操作系统或用于生产设备。

**「社区讨论」** 评论者认可其在 QEMU 和部分小米设备上的技术价值，但也批评配套网站浏览体验差，并担心类似研究会加大辨别山寨 iPhone 的难度；部分讨论还延伸到对 iOS 现状和 Garmin 固件移植的期待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oosexgang/hackios-xnu-kernel">GitHub - oosexgang/hackios-xnu-kernel</a></li>
<li><a href="https://github.com/jprx/darwin-vm">GitHub - jprx/darwin-vm: Run iOS/ macOS in Qemu. Virtual ...</a></li>
<li><a href="https://www.zendot.org/posts/oosexgang-hackios-xnu-kernel">在安卓手机上启动苹果 XNU 内核，跑原版 iOS 16.5 · Zendot</a></li>

</ul>
</details>

**标签**: `#iOS`, `#Android`, `#emulation`, `#reverse-engineering`, `#kernel`

---

<a id="item-tech-news-3"></a>
### [任天堂 Switch 2 越狱实现解密文件系统读写](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/) ⭐️ 8.0/10

一篇发表于 pepsipu.com 的技术文章描述了针对任天堂 Switch 2 的越狱方法，通过利用漏洞获得了加密文件系统的读写权限。若该越狱确认真实，可能很快出现 Switch 2 游戏转储，并在重编译/反编译工具链支持下使主机独占游戏运行于任意硬件，这对任天堂构成安全风险。技术细节包括使用 JetKVM 设备让 Codex 通过 USB 发送手柄输入并通过 HDMI 获取视频输出，以及使用 SwitchBot Bot 或类似蓝牙开关装置自动按下电源键以在崩溃后重启。评论者提到已通过 JetKVM 连接并复制了匹配间距的文件内容，暗示非专业用户难以复现。目前该越狱仍处于技术验证阶段，实际可利用性和稳定性尚待确认。

hackernews · ledoge · 10月22日 08:01 · [社区讨论](https://news.ycombinator.com/item?id=50192536)

**「背景」** Nintendo Switch 2 是任天堂推出的最新游戏主机，其系统默认只允许运行已签名软件。ns2jb 是一个针对当前固件 23.0.1 的软件型漏洞利用，无需硬件芯片或焊接，但属于需要每次开机时连接设备注入的束缚（tethered）用户态漏洞。该漏洞可实现对 Switch 2 解密文件系统的读写访问，从而支持自制软件运行、游戏逆向与修改、存档备份，以及通过 MMIO 访问大部分外设。

**「影响」** 如果该越狱确实实现文件系统解密读写，任天堂 Switch 2 的独占游戏可能被转储并在其他硬件上运行，从而削弱其封闭生态的独占价值。

**「社区讨论」** 社区评论普遍认为该技术文章非常出色，若解密文件系统读写属实，可能数小时内出现游戏转储，而重编译/反编译环境将使 Switch 2 独占游戏运行于任意硬件，构成任天堂最坏情况。也有人指出整套自动化装置（JetKVM、SwitchBot Bot 等）极其复杂，普通用户难以复现，但对后续发展充满期待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/">pepsipu.com/blog/2026-10- switch 2 - jailbreak - ns 2 jb</a></li>
<li><a href="https://gbatemp.net/news/switch-2-jailbreak-ns2jb-released-software-only-exploit-tethered.685698/">Switch 2 jailbreak &quot; ns 2 jb &quot; released. Software-only... | GBAtemp.net</a></li>

</ul>
</details>

**标签**: `#console-security`, `#jailbreak`, `#reverse-engineering`, `#nintendo-switch-2`, `#game-emulation`

---

<a id="item-tech-news-4"></a>
### [eMudhra 宣布退出全球 SSL/TLS 证书业务](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) ⭐️ 8.0/10

eMudhra 宣布将退出全球 SSL/TLS 证书业务。该决定是在一起事件引发外界对其证书颁发机构运营和密钥管理的严重关切之后做出的。eMudhra 是一家公共证书颁发机构，此次退出对 Web PKI 信任和证书签发实践具有重要影响。

hackernews · bo0tzz · 10月22日 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50195110)

**「背景」** eMudhra 是一家印度证书颁发机构（CA），其董事会于周四决定退出全球 SSL/TLS 证书业务。这一决定是在一名研究人员报告恢复了其八个中间 CA 证书的私钥五天后做出的；受影响的证书已被吊销。全球 SSL/TLS 基础设施与该公司在印度及其他地区的数字签名、eSign 和企业 PKI 业务分开运行。

**「影响」** 依赖 eMudhra 全球 SSL/TLS 证书的组织需要尽快评估并迁移到其他受信任的证书颁发机构，以避免证书签发或续期中断。现有证书的过渡安排和具体时间表尚未在提供的资料中明确。

**「社区讨论」** 社区评论普遍批评 eMudhra 未就事件根因做出充分说明，并质疑其“受影响 CA 未签发最终实体证书”的说法，因为任何人似乎都可以从这些 CA 签发证书。另有评论提到 Chrome 团队向 eMudhra 公开提交了大量尖锐质询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business">eMudhra to Exit global SSL / TLS Certificate Business</a></li>
<li><a href="https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html">eMudhra to Exit Global SSL / TLS Business After 8 Intermediate CA...</a></li>
<li><a href="https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/">EMudhra Intermediate CA Certificates Compromised</a></li>

</ul>
</details>

**标签**: `#SSL/TLS`, `#certificate authority`, `#PKI`, `#web security`, `#security incident`

---

<a id="item-tech-news-5"></a>
### [比 earcut 更快：489 毫秒三角化 370 万地图多边形](https://globus.software/blog/2026/10/16/cutting-map-polygons/) ⭐️ 8.0/10

2026 年 10 月 16 日，globus.software 发布的一篇技术博客介绍了一种地图多边形三角化方法，报告称其在基准测试中处理 370 万个地图多边形仅耗时 489 毫秒，速度超过广泛使用的 earcut。博客还公开了基准测试数据集，供他人复现和对比。评论区提到的实现名为 Earstrip，基于 WASM 构建。这一性能提升对需要批量三角化地图多边形的 GIS 和地图渲染场景具有参考价值。

hackernews · molind · 10月22日 09:31 · [社区讨论](https://news.ycombinator.com/item?id=50193170)

**「背景」** 多边形三角化是将复杂多边形分割为三角形集合的过程，广泛用于地图渲染和计算几何。Earcut 是一种常用的耳切算法实现，因体积小、速度快被 Mapbox GL JS 等项目使用；Delaunay 三角化则往往生成质量更好的三角形但速度较慢。该博客发布的 earstrip 是一个 ISC 许可的多边形三角化库，源自其地图引擎，基准测试显示它在 370 万个地图多边形上耗时 489 毫秒，比同数据集上的 Delaunay 快 6.0 倍。

**「影响」** 对于需要高效处理大量地图多边形的 GIS 与地图渲染开发者，Earstrip 宣称的 3.7M 多边形 489 ms 性能可能提供比 earcut 更快的替代方案，但需结合评论区提到的三角形质量、WASM 体积及数据兼容性进行评估。

**「社区讨论」** 评论区讨论较为深入：Earcut 作者 mourner 表示会研究可借鉴的优化，但为保持 JS 库体积小巧（4.1k min/gz）而有意放弃部分优化，并关心 Earstrip 的 WASM 体积；其他读者提到 Triangle、Delaunay32 等算法，质疑结果中大量细长三角形可能对 GPU 光栅化不利，并讨论耳切法相对 Seidel 梯形法的工程取舍。Delaunay32 作者补充说其算法采用分治而非增量插入，尚未在该基准数据集上测试，且其多边形 API 要求简单环和非接触孔洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://globus.software/blog/2026/10/16/cutting-map-polygons/">Faster than earcut : triangulating 3 . 7 M map polygons in 489 ms</a></li>
<li><a href="https://www.npmjs.com/search?q=earcut">earcut - npm search</a></li>

</ul>
</details>

**标签**: `#triangulation`, `#computational-geometry`, `#performance`, `#algorithms`, `#mapping`

---

<a id="item-tech-news-6"></a>
### [澳洲法院裁定苹果开放第三方商店](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

澳大利亚联邦法院裁定，苹果须从 2027 年 3 月 1 日起允许澳区 iPhone 用户通过第三方应用商店和网站安装应用，并开放替代支付方式与外部支付链接。Fortnite 将立即重返澳区 App Store。该裁决源于 Epic Games 的反垄断诉讼，法官认定苹果在 iOS 应用分发和支付市场具有实质性市场力量，其限制竞争行为违反澳大利亚竞争法。苹果表示将上诉并申请暂缓执行。

telegram · zaihuapd · 10月22日 06:54

**「背景」** 苹果长期要求 iOS 应用只能通过官方 App Store 分发，并使用苹果支付系统，开发商需支付佣金。Epic Games 曾在《堡垒之夜》中加入外部支付选项，导致该游戏被下架，并在多个国家发起反垄断诉讼。澳大利亚竞争法禁止拥有实质性市场力量的企业限制竞争。

**「影响」** 澳大利亚 iPhone 用户将从 2027 年 3 月起获得侧载和替代支付选项，但苹果的上诉可能使该日期推迟。

**标签**: `#Apple`, `#Epic Games`, `#antitrust`, `#app store`, `#regulation`

---

<a id="item-tech-news-7"></a>
### [甲骨文发布 Java SE 高危漏洞安全警报](https://www.oracle.com/security-alerts/alert-cve-2026-91403.html) ⭐️ 8.0/10

甲骨文发布安全警报，披露 Java SE 中编号为 CVE-2026-91403 的严重漏洞，CVSS 评分高达 9.1。该漏洞位于 JSSE 组件，攻击者无需身份验证即可通过网络远程利用，可能严重破坏数据的机密性与完整性。受影响版本涵盖 Java SE 8u511、11.0.33、17.0.21、21.0.13、25.0.5、27.0.1 及 GraalVM 多个版本。甲骨文已同步推出修复补丁，并呼吁用户尽快升级至受支持版本。

telegram · zaihuapd · 10月22日 12:30

**「背景」** JSSE（Java Secure Socket Extension）是 Java 中负责 SSL/TLS 协议实现与证书信任管理的组件。此次警报涉及的 CVE-2026-91403 与 eMudhra 相关的中间 CA 证书有关，Oracle 提供的更新会将这些受影响证书从信任列表中移除，以阻断未经认证的远程利用路径。CVSS v3.1 基础评分 9.1 表示该漏洞属于严重级别，影响 Oracle Java SE、Oracle GraalVM for JDK 与 GraalVM Enterprise Edition。

**「影响」** 使用 Java SE 8u511、11.0.33、17.0.21、21.0.13、25.0.5、27.0.1 或受影响 GraalVM 版本的用户应立即应用甲骨文提供的补丁，以降低被未认证远程攻击的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oracle.com/security-alerts/alert-cve-2026-91403.html">Oracle Security Alert Advisory - CVE-2026-91403</a></li>
<li><a href="https://blogs.oracle.com/security/security-alert-cve-2026-91403-released">Security Alert CVE-2026-91403 Released - Oracle Blogs</a></li>
<li><a href="https://app.opencve.io/cve/CVE-2026-91403">CVE-2026-91403 - Vulnerability Details - OpenCVE</a></li>

</ul>
</details>

**标签**: `#Java`, `#Security Vulnerability`, `#Oracle`, `#CVE`, `#Patch Management`

---

<a id="item-tech-news-8"></a>
### [333 个被植入后门的 Tor 出口节点下线](https://kaba.cx/posts/20261020_Tor/) ⭐️ 8.0/10

一名 Tor 运营者扫描约 3000 个出口中继，发现 333 个被植入 Ebury 后门，约占总数的 10%。这些后门可将 22 端口的 SSH 连接劫持到 12 台拦截服务器并窃取凭据。10 月 4 日这些节点被标记为 BadExit，次日全部下线。攻击者早在今年 8 月就已入侵相关服务器，并屏蔽部分端口以专门收集未加密邮件流量；入侵途径尚无定论。

telegram · zaihuapd · 10月22日 14:52

**「背景：Tor 出口与 Ebury 后门」** Tor 出口中继是匿名网络中将用户流量发往目标站点的最后一跳，有机会看到未被端到端加密的流量内容。Ebury 是一种长期活跃的 Linux/OpenSSH 后门与 rootkit，常通过入侵托管服务器获取 SSH 凭据并控制大量主机，已知感染规模达数十万台，新版 1.8.2 还增强了混淆、域名生成算法和 rootkit 隐藏能力。在本事件中，一名 Tor 运营者扫描约 3000 个出口节点，发现其中 333 个被植入 Ebury，攻击者用这些节点劫持 SSH 22 端口连接并收集未加密邮件流量。

**「影响」** 使用这些出口节点的 SSH 和未加密邮件用户可能已被窃取凭据或邮件内容，但具体受影响用户范围和利用方式仍存不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2024/05/ssh-backdoor-has-infected-400000-linux-servers-over-15-years-and-keeps-on-spreading/">Linux maintainers were infected for 2 years by SSH -dwelling backdoor ...</a></li>
<li><a href="https://www.darkreading.com/threat-intelligence/400k-linux-servers-recruited-by-resurrected-ebury-botnet">400K Linux Servers Recruited by Resurrected Ebury Botnet</a></li>
<li><a href="https://kaba.cx/posts/20261020_Tor/">How I got over 300 Tor exit nodes removed - KABA</a></li>

</ul>
</details>

**标签**: `#security`, `#Tor`, `#Ebury`, `#malware`, `#networking`

---

<a id="item-tech-news-9"></a>
### [Nvidia 禁运 B300 芯片现身中国国有网络](https://theinference.org/article/china-s-state-money-bought-banned-nvidia-b300-servers-then-redacted-the-receipts) ⭐️ 8.0/10

中国国资控股的半导体租赁集团为 AI 公司荣耀视图科技融资购入 32 台搭载 Nvidia B300 芯片的华硕服务器，该交易属于 700 余台服务器采购的一部分，总额超 30 亿元人民币，计划部署于中国移动宁夏枢纽。B300 处于美国最严出口管制层级，对华基本禁运。备案记录受到关注后，该半导体租赁集团重新提交文件并抹去硬件描述。Nvidia 表示正联合代工伙伴调查此事，华硕则称遵守出口管制。

telegram · zaihuapd · 10月22日 15:22

**「背景」** B300 是 Nvidia 的高端 AI 芯片，被列入美国最严格的出口管制层级，对华基本禁运，直接或经由第三方转售通常受限制。此次事件中，中国国资背景的租赁公司为 AI 企业融资采购配备 B300 的华硕服务器，相关备案在受到关注后被修改，抹去了硬件描述。此类管制通常要求芯片设计方和代工厂对异常采购进行调查。

**「影响」** 该事件可能促使 Nvidia 及其代工伙伴收紧面向中国客户的最终用途核查；同一 B300 服务器在美国官方售价约 55 万美元，而中国买家通过违规渠道获取将面临更高成本和被追溯风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bregg.com/post.php?slug=ai-hardware-scarcity-healthcare-cost-crisis">When AI Hardware Hits $1 Million: The Supply Crunch Driving...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#B300`, `#export controls`, `#AI hardware`, `#China`

---

<a id="item-tech-news-10"></a>
### [Quad9 DNS 解析器将退出法国](https://quad9.net/news/blog/au-revoir-france/) ⭐️ 7.0/10

Quad9 宣布将退出法国，此前法国法院就其未完全执行盗版网站封锁令及地理封锁（geoIP）措施作出裁决并处以罚款。Quad9 首席技术官表示，公司可能在 11 月 24 日后使用 geoIP 过滤来屏蔽法国用户，尽管此前曾主张 geoIP 不足以实现选择性拒绝解析。此前索尼音乐通过 VPN 从德国访问了本应被封锁的内容，法院认定 Quad9 藐视法庭并罚款；Canal+ 也曾针对谷歌、Cloudflare 和思科等 DNS 解析商获得封锁令。Quad9 的退出与约两年前思科退出法国市场类似，凸显 DNS 基础设施中立性与国家封锁要求之间的冲突。

hackernews · farrokhi · 10月22日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=50195959)

**「背景」** Quad9 是由位于苏黎世的瑞士非营利基金会运营的公共 DNS 解析器，主打隐私保护和网络安全。自 2024 年起，法国法院多次要求公共 DNS 解析器屏蔽盗版体育直播网站，部分提供商如 OpenDNS 已暂停在法服务。Quad9 在相关诉讼中败诉，并宣布自 11 月 24 日起停止向法国用户提供免费服务。

**「影响」** 法国用户将无法继续使用 Quad9 的 DNS 解析服务，需改用其他公共解析器；Quad9 称可能通过 geoIP 屏蔽法国 IP 实现退出。

**「社区讨论」** 社区普遍对惩罚 DNS 解析器表示不解，将其类比为因电话簿列出罪犯号码而处罚电话簿公司；也有用户建议 Quad9 在被迫实施封锁时停止解析起诉公司的域名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quad9">Quad 9 - Wikipedia</a></li>
<li><a href="https://quad9.net/news/blog/au-revoir-france/">Farewell, France | Quad 9</a></li>
<li><a href="https://torrentfreak.com/dns-resolver-quad9-rejects-french-piracy-blocks-weighs-exit-as-bein-seeks-up-to-e580k-a-day/">DNS Resolver Quad 9 Rejects French Piracy Blocks , Weighs Exit as...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#internet censorship`, `#Quad9`, `#France`, `#network infrastructure`

---

<a id="item-tech-news-11"></a>
### [pwn.watch：实时追踪被利用漏洞的仪表盘](https://pwn.watch/) ⭐️ 7.0/10

pwn.watch 是一个实时仪表盘，用于跟踪当前被利用的安全漏洞和活跃漏洞利用情况。该链接由 Hacker News 用户 mrkd 提交，引起信息安全社区的关注，但原始提交本身未提供详细的功能说明。从分析摘要看，它被定位为面向软件工程与信息安全领域的实时安全监控资源，涉及 CVE 和漏洞利用等主题。社区评论反映出对漏洞发现速度的担忧，并认为此类实时工具具有参考价值。

hackernews · mrkd · 10月22日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=50195543)

**「背景信息」** pwn.watch 是一个实时安全事件监控页面，用于展示当前被积极利用的漏洞，并关联 CVE 编号以及 CISA 已知被利用漏洞（KEV）目录的收录情况。被列入 KEV 目录通常表示美国网络安全与基础设施安全局已确认该漏洞存在实际利用证据，因此这类信息可作为修补优先级参考。该页面由开发者 @thekitze 创建，并提示某些漏洞可与其他 CVE 串联利用；例如 CVE-2026-105134 与 CVE-2026-105133 于 2026-10-14 被 CISA 收录。

**「影响」** 对于需要及时掌握正在被利用漏洞的安全团队和开发者，pwn.watch 提供了一个集中查看活跃漏洞利用信息的入口，但本次提交未说明其数据来源、覆盖范围或更新频率，评估时需自行确认。

**「社区讨论」** 评论区普遍认为漏洞发现速度极快，安全形势严峻；有用户推荐 supplychain.fail 作为补充，也有人担心当前 LLM 技术会引发更多安全事件，并批评 AI 生成页面信息过密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pwn.watch/">pwn . watch · live security incidents</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerabilities`, `#CVE`, `#exploits`, `#infosec`

---

<a id="item-tech-news-12"></a>
### [Anthropic 向 Agentic AI 基金会捐赠 Agent Skills 标准](https://simonwillison.net/2026/Oct/22/donating-agent-skills/) ⭐️ 7.0/10

2026 年 10 月 22 日，Anthropic 宣布将其 Agent Skills 标准捐赠给 Linux 基金会旗下的 Agentic AI Foundation（AAIF），该基金会由 Anthropic 与 Block、OpenAI 于去年联合创立，并已是 Model Context Protocol（MCP）的归属地。Anthropic 表示此举旨在保持 Agent Skills 开放、社区驱动且供应商中立。Simon Willison 指出他早在 2025 年 12 月 19 日就预测该标准会进入 AAIF，当时 Anthropic 首次将 skills 称为“开放标准”。捐赠使技能标准的治理从单一厂商转移至中立的行业基金会。

rss · Simon Willison · 10月22日 18:09

**「背景」** Agent Skills 是 Anthropic 提出的用于定义 AI 代理技能的开放标准，使不同供应商的代理能够以一致方式使用和共享技能。Agentic AI Foundation（AAIF）是 Linux 基金会下的项目，由 Anthropic、Block 和 OpenAI 联合创立，此前已接收 Model Context Protocol（MCP）规范。

**「影响」** 对于开发者而言，Agent Skills 规范将改由 Linux 基金会的中立治理程序管理，其后续修订和知识产权不再由 Anthropic 单方控制。

**标签**: `#AI`, `#agents`, `#open-source`, `#standards`, `#Anthropic`

---

<a id="item-tech-news-13"></a>
### [Carbon-X 14.8B 开放 DNA 文本联合模型](https://www.reddit.com/r/MachineLearning/comments/1xchayq/carbonx_is_an_open_148b_model_trained_jointly_on/) ⭐️ 7.0/10

Carbon-X 是一个 14.8B 参数的解码器模型，在 DNA 和文本上联合训练，可在普通聊天中接收原始 DNA 序列并用英语回答。该模型使用 6-mer token，文本与 DNA 共享同一 token 流，并在 302B token 上进行了 mid-training；Hugging Face 报告在关闭思考时，五个 DNA 基准的平均得分为 66.7%，而 GPT-6.1 Sol 为 67.5%。权重以 bfloat16 格式可装入一张 80GB GPU，并以 Apache 2.0 许可开放。它尚未经过临床验证，模型卡指出精确序列操作仍应由代码处理。其价值在于让敏感数据集的序列分析可在本地运行。

reddit · r/MachineLearning · /u/jatingargiitk · 10月22日 12:32

**「背景」** 联合训练 DNA 与文本的模型通常需要将原始碱基序列转换为离散 token；Carbon-X 采用 6-mer 标记化，即把连续的 6 个碱基作为一个基本单元，并与自然语言共用同一 token 流。它属于仅解码器（decoder-only）架构，这类模型根据已有前缀预测下一个 token，适合生成式任务。在通用预训练之后，模型又进行了针对 DNA 和文本混合数据的中期训练（mid-training），以便在本地推理中直接以问答形式处理 DNA 序列。

**「对敏感基因组数据本地分析的影响」** 对于需要处理敏感基因组数据的实验室或开发者，Carbon-X 的 Apache 2.0 权重和可在单张 80GB GPU 上以 bfloat16 运行，意味着可以在本地完成 DNA 查询和变异效应预测等任务，避免将序列上传到云端。但目前未经过临床验证，且模型卡提示精确序列操作仍应由代码完成，因此在私有变异数据集上的实际收益尚需验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/HuggingFaceBio/Carbon-X">HuggingFaceBio/ Carbon - X · Hugging Face</a></li>
<li><a href="https://huggingface.co/HuggingFaceBio/Carbon-X">HuggingFaceBio/ Carbon - X · Hugging Face</a></li>

</ul>
</details>

**标签**: `#bioinformatics`, `#language models`, `#open source AI`, `#DNA sequence modeling`, `#multimodal models`

---

<a id="item-tech-news-14"></a>
### [Open-XTTS-Trainer 开源：一键训练 XTTS v2 三组件并扩展新语言](https://www.reddit.com/r/MachineLearning/comments/1xcurgj/i_built_openxttstrainer_now_you_can_add_new/) ⭐️ 7.0/10

开发者发布了 Open-XTTS-Trainer，一个模块化开源训练套件，可以一键训练 XTTS v2 的全部三个组件，并支持添加新语言脚本。该工具填补了 Coqui AI 关闭后官方未发布 DVAE 音频分词器和 Latent HiFi-GAN 声码器训练代码、以及新 Unicode 脚本因固定词表导致 token 越界或矩阵维度崩溃的空白。套件包含 Stage 1 DVAE 的 Gumbel-Softmax 码本退火与梅尔频谱重建、Stage 2 GPT 的词表扩展和动态嵌入矩阵调整、Stage 3 基于 MPD/MSD 判别器的潜在条件 HiFi-GAN 训练，采用 MPL-2.0 协议，可在现代 PyTorch 和 Python 3.10–3.13 上运行。在 NVIDIA T4 上使用 LJSpeech 与 JFK 人声验证，10 个 epoch 内 HiFi-GAN 梅尔重建损失下降 67%（190.83→63.49），DVAE 梅尔误差下降 67%（8.14→2.71），判别器稳定，但这些数据仅证明组件级训练收敛，尚未验证端到端合成效果，且项目为作者自述，缺乏独立验证。

reddit · r/MachineLearning · /u/yashubhakt · 10月22日 21:03

**「背景」** XTTS v2 是 Coqui AI 推出的零样本语音合成模型，但 Coqui 于 2024 年初宣布关闭，此后其官方训练代码维护中断。社区曾提出重新训练 HiFi-GAN 和 DVAE 的需求，但缺少完整开源实现；同时 XTTS v2 的 tokenizer 固定支持 17 种语言，添加新文字脚本会遇到词汇表外和维度崩溃问题。

**「影响」** 开发者现在可以使用 MPL-2.0 许可的模块化代码训练或微调 XTTS v2 的 DVAE 音频 tokenizer、GPT 和 Latent HiFi-GAN 声码器，并通过动态扩展词表支持印地语、阿拉伯语、泰语等新文字脚本，避免 token 超出词表或维度崩溃；该工具已在 Python 3.10–3.13 和 PyTorch 2.4+ 上验证，无需 torchcodec。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/coqui-ai/TTS/issues/3323">Retraining vocoder (hifigan) and dvae in XTTS #3323 - GitHub</a></li>
<li><a href="https://github.com/coqui-ai/TTS/discussions/3489">&quot;Coqui is shutting down.&quot; · coqui-ai TTS · Discussion #3489</a></li>

</ul>
</details>

**标签**: `#text-to-speech`, `#open-source`, `#machine-learning`, `#speech-synthesis`, `#fine-tuning`

---

<a id="item-tech-news-15"></a>
### [可转向小型 TTS 压缩至 11.84 MB，WER 不变，UTMOS 降约 0.1](https://www.reddit.com/r/MachineLearning/comments/1xcum4s/we_shrank_our_steerable_small_tts_to_1184_mb_wer/) ⭐️ 7.0/10

WhissleAI 发布了 SteerTTS 的 edge 变体，应用需打包的权重、声音、文本前端和 Python 运行时总计 11.84 MB。其声学模型（9.25M 参数，注意力 + 双向 Mamba-3）通过量化感知训练转为 int4，6.2M 参数的 Vocos 风格声码器蒸馏自 charactr/vocos-mel-24khz 并同样做 int4 QAT，文本前端为纯 numpy，运行时不依赖 NLTK、g2p\_en、torchaudio 或 num2words。在 Open TTS Leaderboard 协议本地测试中，WER 保持在 0.96%，UTMOS 从 fp32 的 4.20 降至 4.11，下降约 0.1，主要来自小型 int4 声码器。12 个控制参数（语速、响度、音高、音高范围、句末上扬、停顿、倾斜、气息感等）的量化后效果至少保留 fp32 的 95%，并提供 50 个风格标签和行内标记。CPU 上（2018 Threadripper，4 线程）RTF 为 0.053（约 19 倍实时），首包音频约 120 ms，支持句级流式。限制包括仅支持英语、200 种声音（全模型有 2825 种），设备端不支持声音克隆、自由文本提示或 flow refiner，权重加载时反量化为 fp32，因此收益是体积而非速度。

reddit · r/MachineLearning · /u/Working\_Hat5120 · 10月22日 20:57

**「背景」** SteerTTS v1 是一个可以用数字控制的小型英语文本转语音模型，提供 12 个可调节参数和风格标签。edge 变体旨在缩小部署体积，通过 int4 量化感知训练和蒸馏声码器实现，适合在边缘设备上使用。

**「影响」** 对于需要嵌入式或边缘英语 TTS 的开发者，该模型提供约 11.84 MB 的完整部署包，保持与 fp32 相同的 0.96% WER，但 UTMOS 下降约 0.1，且当前仅缩小体积、未加速推理（因为加载时反量化为 fp32）。

**标签**: `#text-to-speech`, `#model quantization`, `#edge computing`, `#model distillation`, `#efficient AI`

---

<a id="item-tech-news-16"></a>
### [研究：智能电视关闭 ACR 后仍上报内容数据](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 7.0/10

一项针对美国智能电视自动内容识别（ACR）的研究测试了 10 家厂商的 12 台电视，完成 5943 次受控实验，发现部分机型在设置中关闭 ACR 后仍会产生内容相关流量上报。其中 VIDAA OS 的数据通过 MQTT 明文发送，包含不可重置的设备 ID 和音频指纹；Vizio 的 WatchFree+ 则将节目名写入未加密的域名查询，且用户无法关闭。研究还指出两家平台的观看内容以未加密形式外传。

telegram · zaihuapd · 10月22日 09:50

**「背景」** 自动内容识别（ACR）是智能电视用来识别用户正在观看的节目或广告的技术，通常会采集屏幕画面或音频指纹。用户可以在设置中关闭 ACR，以期望停止此类识别和上报。

**「影响」** 使用 VIDAA OS 或 Vizio WatchFree+ 的用户即使关闭 ACR，仍可能被持续收集并向厂商发送可关联设备身份和观看内容的数据，且部分传输未加密。

**标签**: `#smart TV`, `#automatic content recognition`, `#privacy`, `#security`, `#data exfiltration`

---

<a id="item-tech-news-17"></a>
### [米哈游清华开源 GameScaling 键鼠操作模型](https://arxiv.org/abs/2610.28698v1) ⭐️ 7.0/10

米哈游崩坏 AI 团队联合清华大学等发布并开源 GameScaling，这是一个基于 Qwen3.5 视觉语言模型进行键鼠操作继续预训练的游戏操作模型，规模覆盖 0.8B 至 27B，每次输出未来 200 毫秒的键鼠动作。论文通过 120 组训练配置考察数据量、多样性与模型规模，发现增加数据能提升同源游戏表现，多样性有助于迁移到相近游戏，但对差异大的世界提升有限。发布方以 Apache-2.0 许可证开放八个检查点和推理客户端，但不包含训练代码。该工作为游戏 AI 和具身智能体提供了可复现的缩放实验参考。

telegram · zaihuapd · 10月22日 11:32

**「背景」** 视觉语言模型可以同时理解图像和文本；键鼠操作模型则根据游戏画面直接生成键盘和鼠标指令，用于模拟人类操作。GameScaling 在此类模型基础上进行继续预训练，并研究数据量、数据多样性和模型规模对游戏迁移表现的影响。

**「影响」** 对游戏 AI 和具身智能体开发者而言，Apache-2.0 开源的 0.8B 至 27B 检查点与推理客户端可直接用于相近游戏的键鼠操作任务，但训练代码缺失会限制完全复现与定制训练。

**标签**: `#game AI`, `#vision-language model`, `#open source`, `#scaling laws`, `#human-computer interaction`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [沪深 300 较 6 月高点回落 20%，A 股逼近熊市](https://www.bloomberg.com/news/articles/2026-10-22/china-stocks-set-for-bear-market-as-ai-trade-policy-hopes-fade) ⭐️ 7.0/10

10 月 22 日，沪深 300 指数盘中一度下跌 1.7%，较 6 月高点累计回落 20%，A 股逼近熊市；市场把下跌归因于实质性财政刺激缺位和宁德时代等公司业绩不及预期，宁德时代周三股价暴跌 12%。

telegram · zaihuapd · 10月22日 05:05

**「背景」** 指数较近期高点下跌 20%通常被视为进入熊市的技术门槛。

**标签**: `#China stocks`, `#bear market`, `#market decline`, `#earnings miss`, `#fiscal policy`

---