---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> 从 35 条内容中筛选出 14 条重要资讯。

---

**科技新闻**
1. [Azure 最薄弱环节：五起完整跨租户入侵](#item-tech-news-1) ⭐️ 9.0/10
2. [Cursor 市场出现 Claude Code 扩展后门](#item-tech-news-2) ⭐️ 8.0/10
3. [币安 63 亿美元黑客攻击仅 20 分钟完成](#item-tech-news-3) ⭐️ 8.0/10
4. [Northflank 报告安全事件](#item-tech-news-4) ⭐️ 7.0/10
5. [NESformer：用约 1GB Qwen 权重模拟任天堂 FC](#item-tech-news-5) ⭐️ 7.0/10
6. [Tangled 在 AT Protocol 上推出联邦代码托管平台](#item-tech-news-6) ⭐️ 7.0/10
7. [AI 不取代 SRE，却导致其技能退化](#item-tech-news-7) ⭐️ 7.0/10
8. [Soft-MTP：一行代码改进多 token 预测](#item-tech-news-8) ⭐️ 7.0/10
9. [FCC 拟禁止中国三大运营商获取美国号码资源](#item-tech-news-9) ⭐️ 7.0/10
10. [苹果 Apple 智能功能 11 月 4 日在中国上线测试](#item-tech-news-10) ⭐️ 7.0/10

**财经新闻**
1. [Anthropic 成 SpaceX 最大单一客户，贡献约三分之一营收](#item-finance-news-1) ⭐️ 8.0/10
2. [DeepSeek 完成第二轮融资：募资 1055 亿元，估值超 6155 亿元](#item-finance-news-2) ⭐️ 8.0/10
3. [四家日系车企在华产量降至峰值四成以下](#item-finance-news-3) ⭐️ 7.0/10
4. [美股半导体板块重挫，英特尔跌超 26%](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Azure 最薄弱环节：五起完整跨租户入侵](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 9.0/10

安全研究披露了 Azure 中五起完整的跨租户入侵漏洞，包括可伪造的管理员同意回调和跨租户数据泄露。评论指出，login.microsoftonline.com/XXX/v2.0/adminconsent 流程结束时重定向用户的回调可被伪造，只要攻击者知道其他客户的 Azure 租户 ID。文档中“切勿使用租户参数中的租户 ID 值来认证或授权用户”的警告被认为不充分，因为缺少可行的替代认证方式。研究还指出可能存在路径遍历和 IDOR 问题，并怀疑这些能力自启用以来就存在。

hackernews · swq115 · 10月30日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50301854)

**「背景」** Azure 多租户环境中，管理员同意流程和 API 连接架构允许跨租户访问，但相关设计存在安全边界问题。Binary Security 的研究显示，攻击者可利用默认 API 连接缺陷完全攻陷其他租户的资源，包括 Key Vault、Azure SQL 数据库以及 Jira、Salesforce 等外部连接服务。微软 Entra ID 已收紧令牌有效期并对受支持应用强制持续访问评估，但 adminconsent 回调仍可能因租户 ID 可预测而被伪造。

**「影响」** 受影响的企业可能遭遇基于 Azure 租户的跨租户完全失陷，攻击者可借此未授权访问 Azure Key Vault 中的机密、证书和加密密钥，并进一步入侵与该租户集成的 Slack、Salesforce、Jira 等外部服务及 Azure SQL 数据库。

**「社区讨论」** 评论区普遍认为这些漏洞严重，并对研究者表示赞赏；有评论指出 Azure 的跨租户泄露问题似乎比竞争对手更严重，质疑企业为何仍大量采用 Azure。另有评论推测路径遍历和 IDOR 问题可能自这些功能启用之初就存在，并质疑‘在资源名称中添加随机性’的建议是否与这些漏洞有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case">Azure &#x27;s Weakest Link - Five Full Cross - Tenant Compromises</a></li>
<li><a href="https://gbhackers.com/azure-default-api-connection-flaw/">Azure Default API Connection Flaw Enables Full Cross - Tenant ...</a></li>
<li><a href="https://hackerxone.com/azure-entra-id-red-team-techniques-2026-attack-playbook/">Azure Entra ID Red Team Techniques: 2026 Attack Playbook</a></li>
<li><a href="https://www.binarysecurity.no/posts/2026/10/one-root-case">Azure &#x27;s Weakest Link - Five Full Cross - Tenant Compromises</a></li>
<li><a href="https://gbhackers.com/azure-default-api-connection-flaw/?trk=article-ssr-frontend-pulse_little-text-block">Azure Default API Connection Flaw Enables Full Cross - Tenant ...</a></li>

</ul>
</details>

**标签**: `#security`, `#azure`, `#cloud`, `#vulnerability`, `#cross-tenant`

---

<a id="item-tech-news-2"></a>
### [Cursor 市场出现 Claude Code 扩展后门](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 8.0/10

Cursor Marketplace 上出现了一个被篡改的 Claude Code 扩展，该扩展会向用户的 SSH authorized\_keys 文件追加一个标记为 svc-telemetry 的攻击者公钥。Anthropic 员工 Felix 确认这并非 Anthropic 系统或员工电脑被入侵，而是恶意行为者利用 Cursor 市场的发布权限上传了篡改副本；官方 Anthropic 渠道不受影响，只有 Cursor 用户可能受影响。据 Reuters 引用 Cursor 的说法，该恶意扩展于周四约 2:27 a.m. PT 至 1:35 p.m. PT 期间在线，且并非由 Anthropic 开发。用户可在 macOS 上运行 grep -qs svc-telemetry ~/.ssh/authorized\_keys &amp;&amp; echo &quot;svc-telemetry key found&quot; \|\| echo &quot;No key found; machine not impacted&quot; 来检测是否中招，Windows 也有相应检测命令。

hackernews · \_chall · 10月30日 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

**「背景」** VS Code 扩展可通过多种注册表分发：Anthropic 发布的 Claude Code 扩展通常位于官方市场，而 Cursor Marketplace 镜像 Open VSX 注册表。此次事件中，被篡改的 anthropic.claude-code 2.1.312 和 2.1.313（Windows/macOS）被发布到 Open VSX，进而通过 Cursor Marketplace 分发给用户；因此受影响面限于使用该镜像渠道的 Cursor 用户，并不涉及 Anthropic 官方发布渠道。

**「影响」** 从 Cursor Marketplace 安装该恶意扩展的用户应立即检查 ~/.ssh/authorized\_keys 是否包含 svc-telemetry 公钥并移除，因为攻击者可利用该密钥访问受影响机器。

**「社区讨论」** 社区普遍认为这是 Cursor 市场/Open VSX 的供应链问题，而非 Anthropic 官方系统被入侵；Felix 确认官方渠道不受影响，只影响 Cursor 用户。xx\_ns 指出受影响的扩展位于 Open VSX 注册表及 Cursor 市场，并对 Microsoft 官方市场是否同样受影响表示不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/blog/claude-code-extension-security-notice">Security notice — malicious version of Anthropic.claude-code ...</a></li>
<li><a href="https://www.stepsecurity.io/blog/claude-code-extension-trojanized">Trojanized Claude Code Extension Delivered Persistent SSH ...</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain`, `#vscode`, `#claude-code`, `#cursor`

---

<a id="item-tech-news-3"></a>
### [币安 63 亿美元黑客攻击仅 20 分钟完成](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/) ⭐️ 8.0/10

有报道称，币安（Binance）遭遇一起 63 亿美元的黑客攻击，整个资金转移过程仅用时 20 分钟。该事件凸显了加密货币交易所在安全防护和监管合规方面的重大隐忧。目前公开细节有限，具体漏洞利用方式、损失确认情况以及责任归属尚不明确。

hackernews · domhudson · 10月30日 12:50 · [社区讨论](https://news.ycombinator.com/item?id=50303172)

**「背景」** Binance 是全球交易量最大的加密货币交易所，此次攻击是已知最大规模的加密货币盗窃案。攻击者在约 20 分钟内从 10 条区块链上的钱包转移了约 63 亿美元资产，其中约 30 亿美元被冻结；攻击利用了 EIP-7702 账户抽象机制，分析认为可能与朝鲜黑客有关，但 Binance 未证实。

**「影响」** 该事件可能使币安及同类加密货币交易所面临更严格的安全审查和监管压力。不过，公开细节有限，具体影响范围尚待确认。

**「社区讨论」** 评论区主要关注币安的安全责任与监管缺失，有用户质疑为何单台受损笔记本能在数分钟内导致 63 亿美元损失，并认为需要类似银行的监管。另有评论指出攻击准备可能持续数年、执行时间短并不罕见，还有人猜测该事件与 Claude Code 供应链攻击的时间点有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/">The $ 6 . 3 Billion Binance Hack Was Pulled Off in Just 20 ... | WIRED</a></li>
<li><a href="https://www.cryptotimes.io/insights/binance-hack-explained/">Binance Hack Explained: How $ 6 . 3 Billion Was Drained in 20 Minutes</a></li>
<li><a href="https://www.youtube.com/watch?v=3tmPCylnuKE">How crypto hackers drained Binance of $ 6 . 3 billion in 20 minutes</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#cryptocurrency`, `#exchange-hack`, `#financial-security`, `#incident-response`

---

<a id="item-tech-news-4"></a>
### [Northflank 报告安全事件](https://status.northflank.com/) ⭐️ 7.0/10

云平台提供商 Northflank 已通过其状态页面报告了一起安全漏洞事件。目前源材料中未提供有关漏洞具体时间、受影响范围、被访问的数据或攻击方式等细节。该事件引起了软件工程与基础设施领域对多租户 SaaS 服务商安全性的关注，社区评论中提及了近期多起针对同类服务商的攻击。

hackernews · js4ever · 10月30日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=50305025)

**「背景」** Northflank 是一家云平台服务商，通过状态页发布服务运行和安全事件。该事件的链接指向其官方状态页；不过，外部工具结果提供不同的上下文：Northflank 的安全页面声称自 2019 年 4 月 1 日成立以来未发生安全漏洞，当前状态页显示所有系统运行正常，StatusGator 也显示服务在线。

**「社区讨论」** 评论者普遍担忧多租户 SaaS 服务商的安全状况，并指出自去年九月以来已有多家类似厂商被攻破。部分用户讨论了将环境变量加密并把解密密钥硬编码在代码中的临时缓解措施，也有观点认为此类事件可能导致客户从初创基础设施公司回流至大型云服务商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://northflank.com/security">northflank .com/ security</a></li>
<li><a href="https://northflank.instatus.com/default">Northflank - Status</a></li>
<li><a href="https://statusgator.com/services/northflank">Northflank Status . Check if Northflank is down or... | StatusGator</a></li>

</ul>
</details>

**标签**: `#security`, `#incident`, `#cloud`, `#SaaS`, `#infrastructure`

---

<a id="item-tech-news-5"></a>
### [NESformer：用约 1GB Qwen 权重模拟任天堂 FC](https://github.com/dbreunig/nesformer) ⭐️ 7.0/10

NESformer 是一个概念验证项目，声称用约 1GB 的 Qwen 模型权重模拟任天堂娱乐系统（NES/FC），并将 CPU 与 RAM 的仿真包含在模型内部。该项目运行速度比真实硬件慢 150 到 290 倍，因此不是实用的模拟器。社区评论提到其使用 gated deltanet 架构来存储 RAM 状态，并以矩阵乘法执行状态更新。这一实验展示了 Transformer 权重可以替代部分确定性程序，但代价是巨大的计算开销。

hackernews · dbreunig · 10月30日 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50306442)

**「背景」** 任天堂娱乐系统（NES）是一台 8 位游戏机，其核心是 6502 CPU 和独立 RAM，通常由软件模拟器或 FPGA 以确定性逻辑重现。与依赖训练数据的普通神经网络不同，nesformer 项目用编译器直接计算 Qwen 3.5 模型的权重，将 CPU 6502 指令和 RAM 都放进模型内部执行。评论中提到的 gated deltanet 架构和 matmul 运算模拟，正是这一权重编译方案在模型内承载硬件状态的方式。

**「社区讨论」** 评论者普遍认可其技术趣味，但强调与常规确定性程序相比效率极低。作者 dbreunig 称权重和代码由 Opus 5.5 仅用两次提示生成；armcat 设想在权重内编译小型 VM 并用 matmul 执行工具，而 jacquesm 和 pbohun 则突出其巨大的算力开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dzen.ru/b/auTxnHpCwlRQnR2n">Процессор NES собрали в весах Qwen 3.5 без обучения nesformer ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#emulation`, `#Qwen`, `#hardware-emulation`, `#novel-computing`

---

<a id="item-tech-news-6"></a>
### [Tangled 在 AT Protocol 上推出联邦代码托管平台](https://tangled.org/blog/forge/) ⭐️ 7.0/10

Tangled 已推出基于 AT Protocol 的联邦式代码托管平台，支持自托管，并宣布其 AT Protocol lexicons 已稳定。该平台已提供组织（organizations）支持，私有仓库将在未来几周上线。其联合创始人表示，架构和 UI 已全面重构，自托管整个技术栈或部分组件变得非常容易。此次发布旨在为去中心化的代码协作提供新选择，并可能与其他 AT Protocol 代码仓库实现互操作。

hackernews · zlliang · 10月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=50305573)

**「背景」** AT Protocol 是 Bluesky 采用的去中心化社交协议，强调数据可移植性和跨服务器联邦。基于该协议的代码托管平台有望让仓库、议题和拉取请求等记录在不同实例之间互通，减少对单一平台锁定。

**「影响」** 对于寻求替代 GitHub/Gitea 的开发者，Tangled 提供了可自托管的联邦式代码托管选项，并已支持组织功能；但私有仓库尚未上线，需等待未来几周。

**「社区讨论」** 社区反馈总体积极，有用户计划从 Gitea 迁移至 Tangled。也有人指出首页/时间线的 UI 过于繁忙，并询问 lexicon 是否已将 issue、PR 和评论记录归属到仓库作用域而非用户作用域。

**标签**: `#federated-code-forge`, `#at-protocol`, `#code-collaboration`, `#self-hosting`, `#decentralization`

---

<a id="item-tech-news-7"></a>
### [AI 不取代 SRE，却导致其技能退化](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 7.0/10

文章认为，AI 工具并未取代站点可靠性工程师（SRE），而是正在使其技能退化。作者将这一趋势与航空自动化类比，指出 FAA 要求飞行员在自动驾驶可胜任时仍保持手动飞行时间，以维持必要技能。文章提出，SRE 团队可以指定某些本可由 AI 处理的故障作为“人工练习机会”，避免过度依赖自动化。这一观点旨在保留关键的动手调试和运维理解能力，因为自动化正在接管越来越多的任务。

hackernews · dorianniemiec · 10月30日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=50305693)

**「背景」** 站点可靠性工程（SRE）是运用软件工程方法保障系统可用性、延迟、性能与容量的实践，其日常工作包括监控、告警、事件响应和事后复盘。随着云服务和基础设施即代码工具（如 Terraform）普及，许多操作被抽象和自动化，而近期 AI 代理进一步能自动完成日志分析、云资源排查等原本由工程师手工进行的调查任务。本文讨论“自动化悖论”：当 AI 能处理大多数常规事件时，工程师可能因缺少实践而在面对罕见复杂故障时技能退化，类似航空业要求飞行员保留手动飞行时间以维持应急能力。

**「影响」** 采用 AI 自动化的 SRE 团队可能需要刻意安排人工故障响应演练，以防止调试和架构理解能力的侵蚀。

**「社区讨论」** 评论者普遍认同航空业类比，但对“技能退化”是否可接受存在分歧：一些人认为 AI 代理（如 Claude）解决 AWS 问题的速度可快 10 倍，而 Terraform 等工具早已使基础设施工作“去技能化”；另一些人则强调 SRE 的价值在于理解数据流、瓶颈和架构，AI 生成的应用恰恰缺乏这种理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signoz.io/blog/ai-isnt-replacing-sres-its-deskilling-them/">AI Isn &#x27; t Replacing SREs . It &#x27; s Deskilling Them . | SigNoz</a></li>

</ul>
</details>

**标签**: `#SRE`, `#AI`, `#automation`, `#site reliability engineering`, `#deskilling`

---

<a id="item-tech-news-8"></a>
### [Soft-MTP：一行代码改进多 token 预测](https://www.reddit.com/r/MachineLearning/comments/1xjnz40/multitoken_prediction_done_right_r/) ⭐️ 7.0/10

Reddit 帖子分享了一项研究，提出 Soft Multi-Token Prediction（Soft-MTP）方法。作者称标准 MTP 梯度中隐藏了有助于提升投机解码的 KL 自蒸馏信号，但该信号被损害下一 token 预测的噪声残差所掩盖。该方法通过 KL 梯度恢复技巧提取这一信号，只需一行代码改动：h\_ntp += h\_mtp.detach\(\) - h\_mtp。作者表示 Soft-MTP 几乎是免费改进，在一系列任务上优于标准 MTP，并提供了代码、论文和 HuggingFace 链接。这些结论来自作者本人，尚未经独立验证。

reddit · r/MachineLearning · /u/jayden\_teoh\_ · 10月30日 18:53

**「背景：多令牌预测与投机解码」** 多令牌预测（MTP）是一种同时预测多个后续 token 的技术：在自回归生成中，它能让语言模型一次前向传播生成多个草稿 token，再通过验证步骤保持骨干模型的 token 分布，从而提高吞吐量；它也可作为辅助训练任务，在不增加训练时间的情况下提升代码和自然语言模型的下游能力。该技术已成为前沿预训练的标准配方之一，并常与投机解码结合使用。

**「对 LLM 预训练与推测解码的影响」** 对于采用多 token 预测（MTP）进行预训练和推测解码的 LLM 开发者，Soft-MTP 仅需一行代码改动，即可消除标准 MTP 梯度中随模型规模增大而加剧的噪声残差，并在不同规模下无额外开销地提升困惑度、下游准确率和推测解码效率。该结果来自论文自述，尚待独立大规模验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.00888">[2610.00888] Match the Distribution, Not the Compute: Post-Training...</a></li>
<li><a href="https://paperswithcode.co/paper/2404.19737">Better &amp; Faster Large Language Models via Multi - token Prediction ...</a></li>
<li><a href="https://arxiv.org/pdf/2610.38331">Multi-Token Prediction Done Right - arXiv.org</a></li>
<li><a href="https://www.goodpapers.org/paper/arxiv-2610.38331">Multi-Token Prediction Done Right (Highly rated) | Good Papers</a></li>
<li><a href="https://arxiv.org/abs/2610.38331">[2610.38331] Multi-Token Prediction Done Right - arXiv.org</a></li>

</ul>
</details>

**标签**: `#multi-token prediction`, `#speculative decoding`, `#language models`, `#self-distillation`, `#training optimization`

---

<a id="item-tech-news-9"></a>
### [FCC 拟禁止中国三大运营商获取美国号码资源](https://fccid.io/news/fcc-draft-national-security-voip-direct-access-numbering-rules) ⭐️ 7.0/10

美国联邦通信委员会（FCC）10 月 29 日表示，计划在 11 月 19 日表决一项提案，以国家安全和防范诈骗骚扰电话为由，禁止中国移动、中国电信、中国联通及其他相关 VoIP 服务商直接获取美国电话号码资源。该提案仅限制直接号码资源获取权限，暂不影响现有普通国际电话的拨打与接听。FCC 还拟禁止使用华为、中兴等风险清单设备的服务商直接获取美国电话号码资源。三家运营商在美实体此前已被拒绝或撤销美国际电信业务授权。

telegram · zaihuapd · 10月30日 08:01

**「背景」** 美国电话号码资源由 FCC 管理，服务商需授权才能直接获取本地号码；直接获取号码可用于提供本地 VoIP 等服务，但可能被滥用。此前美国已以国家安全为由限制中国电信运营商在美业务授权，并将华为、中兴列入风险设备清单。

**「影响」** 受影响的中国三大运营商及相关 VoIP 服务商将在表决通过后无法直接获取美国号码资源，可能限制其在美本地业务扩展，但现有国际电话服务不受影响。提案尚未通过，最终影响取决于 11 月 19 日表决结果。

**标签**: `#FCC`, `#telecom`, `#China`, `#national security`, `#VoIP`

---

<a id="item-tech-news-10"></a>
### [苹果 Apple 智能功能 11 月 4 日在中国上线测试](https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/) ⭐️ 7.0/10

苹果宣布 Apple 智能首批功能即将登陆中国，包括实时翻译、照片消除工具和写作工具等，自 11 月 4 日起随最新 iOS 开发者 Beta 版开放测试，并将于 12 月 iOS 27.3 正式发布时面向中国用户推出。其他平台的支持将在获得必要审批后推出，本次更新不含下一代 Siri AI 功能。苹果还与阿里巴巴合作，在 Siri、写作工具和视觉智能中接入千问模型，面向在中国购买了支持 Apple 智能的 iPhone 用户，或设备定位和 Apple 账户国家/地区均设置在中国的用户提供。

telegram · zaihuapd · 10月30日 21:44

**「背景」** Apple Intelligence 是苹果在 iOS 等系统中提供的生成式 AI 功能套件，此前已在其他市场推出，包含写作工具、照片消除和视觉智能等。为进入中国市场，苹果选择与阿里巴巴合作，在 Siri、写作工具和视觉智能中接入千问模型；本次首批功能不含下一代 Siri AI，且将先通过开发者 Beta 测试、后在 iOS 27.3 正式发布。

**「影响」** 对于设备定位与 Apple 账户国家/地区均设在中国、且持有支持 Apple 智能的 iPhone 用户，首批功能（实时翻译、照片消除、写作工具）将在 11 月 4 日通过开发者 Beta 测试，并于 12 月随 iOS 27.3 正式上线，由阿里巴巴千问模型驱动；据监管注册信息，相关服务还集成了百度技术，而非 ChatGPT，其他平台需等待审批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iclarified.com/103212/apple-intelligence-coming-to-china-in-december-with-ios-273">Apple Intelligence Coming to China in December With iOS 27.3</a></li>
<li><a href="https://thenextweb.com/news/apple-intelligence-china-ios-27-3-alibaba-qwen">Apple confirms its AI features reach China in December, with Qwen</a></li>
<li><a href="https://www.youtube.com/watch?v=e7BBGv-LmH8">Apple Just Admitted This Isn&#x27;t Their AI - YouTube</a></li>
<li><a href="https://novakvm.com/en/blog/2026-apple-intelligence-china-qwen-baidu.html">Apple Intelligence Finally Gets Approved in China ...</a></li>
<li><a href="https://humphreytheodore.com/writing/ai-sovereignty-apple-intelligence-alibaba-qwen-china-2026">AI Sovereignty: Apple Intelligence Runs on Alibaba Qwen</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#China`, `#Alibaba Qwen`, `#iOS`, `#AI features`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Anthropic 成 SpaceX 最大单一客户，贡献约三分之一营收](https://www.cls.cn/detail/2519914) ⭐️ 8.0/10

SpaceX 在申报文件中披露，上季度约 34.5% 的营收来自 AI 部门单一客户；知情人士称该客户为 Anthropic。Anthropic 的 IPO 披露文件显示，其同意在截至 2029 年的合同期内最多支出 1205 亿美元，从今年 12 月起相当于每月为 SpaceX 贡献约 31 亿美元营收。

telegram · zaihuapd · 10月30日 06:20

**「背景」** SpaceX 的 AI 部门现名为 Super Intelligence，向客户提供算力服务；Anthropic 今年早些时候与 SpaceX 签署使用田纳西州孟菲斯数据中心算力的协议。

**标签**: `#SpaceX`, `#Anthropic`, `#AI infrastructure`, `#revenue concentration`, `#cloud computing`

---

<a id="item-finance-news-2"></a>
### [DeepSeek 完成第二轮融资：募资 1055 亿元，估值超 6155 亿元](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) ⭐️ 8.0/10

据 The Information 报道，DeepSeek 第二轮融资募资 1055 亿元人民币，估值超过 6155 亿元人民币。本轮国资背景投资者出资约占 27%，高于首轮约 510 亿元融资中 2% 的占比。

telegram · zaihuapd · 10月30日 12:37

**「背景」** 这是 DeepSeek 继今年 6 月约 510 亿元首轮融资后的第二轮融资，当时国资背景投资者出资占比约 2%，而本轮约 27% 资金来自国资背景投资者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/deepseek-16-billion-funding-round-state-funds-27-percent-2026/">DeepSeek Funding Round: $16B, 27% State Money [2026]</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#funding`, `#AI`, `#China`, `#venture capital`

---

<a id="item-finance-news-3"></a>
### [四家日系车企在华产量降至峰值四成以下](https://weibo.com/1642634100/Rp6qUwLKa) ⭐️ 7.0/10

据新浪科技报道，2026 年 4 月至 9 月，丰田、本田、日产和马自达在华合计产量约 102 万辆，同比下降 32%，不足 2020 年同期峰值的四成；本田同期产量约 13.2 万辆，同比下降 60%，并计划将在华燃油车年产能从 149 万辆削减至 100 万辆。

telegram · zaihuapd · 10月30日 13:38

**「背景」** 本次产量对比以 2020 年 4 月至 9 月的同期产量为峰值基准，并以 2008 年以来同期数据作为历史参照，显示四家日系车企在华产量处于长期低位。

**标签**: `#Japanese automakers`, `#China auto market`, `#Honda`, `#production decline`, `#capacity reduction`

---

<a id="item-finance-news-4"></a>
### [美股半导体板块重挫，英特尔跌超 26%](https://www.cls.cn/detail/2521210) ⭐️ 7.0/10

10 月 30 日，美股半导体板块大幅走低，费城半导体指数跌 5.67%，英特尔跌超 26%，AMD 跌超 10%。

telegram · zaihuapd · 10月30日 13:48

**「背景」** 此次下跌发生前，亚马逊和 Alphabet 公布的业绩罕见不及预期，英特尔业绩指引也低于分析师估计，引发市场对人工智能估值过高的担忧，拖累科技股抛售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-october-30-dow-sp-500-nasdaq-amazon-intel-ai-sell-off-191429143.html">Stock market today: Nasdaq, Dow, S&amp;P 500 clobbered as October ...</a></li>
<li><a href="https://www.bnnbloomberg.ca/markets/2026/10/30/the-sell-off-for-tech-stocks-deepens-and-drags-wall-street-toward-its-worst-day-since-june/">Markets today: Wall Street drops to its worst day since June</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-10-29/stock-market-today-dow-s-p-live-updates">Stock Market Today: Dow, S&amp;P Live Updates for October 30 , 2026</a></li>

</ul>
</details>

**标签**: `#semiconductor stocks`, `#market selloff`, `#Intel`, `#AMD`, `#Philadelphia semiconductor index`

---