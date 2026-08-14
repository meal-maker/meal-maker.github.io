---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 40 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [Qwen 3.8 27B 开源模型本地推理表现强劲](#item-tech-news-1) ⭐️ 8.0/10
2. [谷歌通过同态加密推进实用私有 AI](#item-tech-news-2) ⭐️ 8.0/10
3. [Firefox 成为最后完整支持 uBlock Origin 的主流浏览器](#item-tech-news-3) ⭐️ 8.0/10
4. [小红书开源 dots3-note：280B 参数仅 16B 激活](#item-tech-news-4) ⭐️ 8.0/10
5. [PostgreSQL 修复高危 to\_char 漏洞可导致任意代码执行](#item-tech-news-5) ⭐️ 8.0/10
6. [苹果自研中国专属 AI 模型获备案 联手阿里或成首个获批外企](#item-tech-news-6) ⭐️ 8.0/10
7. [RustDesk 现支持 Wayland 真正的无人值守远程访问](#item-tech-news-7) ⭐️ 7.0/10
8. [GLM-5.3：前沿编程模型，具备新兴网络能力](#item-tech-news-8) ⭐️ 7.0/10
9. [不要分类，让模型“幻觉”标签再用向量匹配](#item-tech-news-9) ⭐️ 7.0/10
10. [AI 人体组织实验年测 300 万次](#item-tech-news-10) ⭐️ 7.0/10
11. [谷歌被令一周内取消第三方商店安装障碍](#item-tech-news-11) ⭐️ 7.0/10

**科技博客**
1. [DSpark 置信度调度：vLLM 自适应验证](#item-tech-blog-1) ⭐️ 9.0/10

**财经新闻**
1. [伯克希尔二季度转净买入，Alphabet 升至第三大持股](#item-finance-news-1) ⭐️ 8.0/10
2. [高盛从 AI 基础设施融资潮中获利](#item-finance-news-2) ⭐️ 8.0/10
3. [监管机构与银行加大对预测市场的审查力度](#item-finance-news-3) ⭐️ 7.0/10
4. [Uber 与 Pony.ai 计划在欧洲部署 2,000 辆自动驾驶出租车并扩展至中东](#item-finance-news-4) ⭐️ 7.0/10
5. [中信旗下信宸资本据报接近收购阿里灵犀互娱，估值或超 15 亿美元](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen 3.8 27B 开源模型本地推理表现强劲](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 3.8 27B（FP8）作为一个新的开放权重模型发布，早期社区评测显示其本地推理能力突出。根据用户 CMay 的私有基准测试，它是继 Gemma 4 之后第二个能够正确推理该基准的本地模型，但消耗了约 5 倍的 token 并启用 MTP 后用时 12 分 30 秒，且 VRAM 效率明显低于 Gemma 4 或 Glimmer。Simon Willison 在其笔记本电脑上运行该模型生成了他见过最好的鹈鹕 SVG，说明其在本地创意任务上的表现也很强。社区还注意到与 Qwen 3.6 相比，其思考轨迹用词更省略，并有人怀疑这可能影响 MTP 预测；同时模型附带的 Jinja 模板存在问题，需要手动调整以减少或关闭某些功能。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**「背景」** Qwen 3.8 27B 是阿里通义千问团队发布的 27B 参数开源权重模型，提供 BF16 与 FP8 两种官方检查点；其中 FP8 约需 27GB 显存，BF16 约需 54GB，而 4-bit 量化可降至约 14–16GB，因此适合在 48GB 级显卡上本地运行。它是 Qwen3.6-27B 的后继版本，后者原生上下文长度为 262,144 token 并可扩展至 1,010,000 token；多个基准显示 3.8 相比 3.6 有稳定提升。目前 Qwen Cloud 托管与定价尚未上线，GGUF 文件为第三方转换。

**「影响」** 对需要本地部署推理模型的开发者和研究者而言，Qwen 3.8 27B 提供了接近前沿的推理能力，但需接受更高的 token/时间开销、较低的 VRAM 效率以及需要修复的模板配置。

**「社区讨论」** 社区总体上认可 Qwen 3.8 27B 的推理质量，尤其在私有基准和图像生成任务中表现亮眼；主要担忧包括 VRAM 效率不佳、思考轨迹省略词现象可能干扰 MTP，以及 Jinja 模板默认配置存在问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B-FP8">Qwen/Qwen3.6-27B-FP8 · Hugging Face</a></li>
<li><a href="https://kingy.ai/blog/qwen3-8-27b-specs-benchmarks-local-hardware/">Qwen3.8-27B: Specs, Benchmarks &amp; Verdict</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#Qwen`, `#inference`

---

<a id="item-tech-news-2"></a>
### [谷歌通过同态加密推进实用私有 AI](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 8.0/10

谷歌发布博客文章，宣布正通过同态加密技术使私有 AI 更加实用。同态加密允许在加密数据上直接进行计算，从而在机器学习推理等场景中保护用户隐私。该举措旨在解决隐私保护机器学习的关键瓶颈，但提供的材料未包含具体实现细节或性能数据。社区评论对同态加密的高计算开销和商业可行性表示怀疑。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**「背景」** 同态加密允许直接在密文上进行计算，无需先解密，从而在云服务器处理敏感数据时保护隐私。Google 的 HEIR（Homomorphic Encryption Intermediate Representation）编译器能够将针对明文输入训练的预训练模型转换为可在加密输入上运行的版本。早期同态加密推理开销极高（可达千倍以上），近年研究和框架优化正试图使其在部分场景变得实用，但仍需平衡隐私保证与计算可行性。

**「影响」** 对于关注数据隐私的 AI 开发者和用户，谷歌的这一方向可能开启在不暴露原始数据的情况下进行模型推理的路径，但当前约 1000 倍的计算开销使其难以大规模商用。

**「社区讨论」** 社区评论普遍关注同态加密的高计算开销，有人估计推理任务开销约为 1000 倍，质疑其商业可行性；也有评论者批评谷歌在隐私方面的记录，但认为若该技术可行，可能让谷歌重新获得竞争优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/">How Google is Making Private AI Practical with Homomorphic Encryption</a></li>
<li><a href="https://medium.com/google-cloud/homomorphic-encryption-47c353aed635">Homomorphic Encryption for AI: The Ultimate Guide to Secure, Confidential, and Encrypted Data in Motion | Google Cloud - Community</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2949948825000289">Encrypted intelligence: A comparative analysis of homomorphic encryption frameworks for privacy-preserving AI - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#homomorphic-encryption`, `#privacy`, `#AI`, `#machine-learning`, `#Google`

---

<a id="item-tech-news-3"></a>
### [Firefox 成为最后完整支持 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 8.0/10

在 Chrome 向 Manifest V3 过渡的背景下，Firefox 被报道为最后一个完整支持 uBlock Origin 的主流浏览器。这一变化意味着 Chrome 用户无法再以原有方式使用 uBlock Origin 的全部功能，对隐私和广告拦截生态产生直接影响。社区评论指出，Brave 通过 chrome://flags 和 brave://settings/extensions/v2 等设置仍可启用 Manifest V2 扩展，微软 Edge 的扩展商店也仍列出 uBlock Origin，Helium 浏览器则预装该扩展，但这些属于变通方案或非完整替代。

hackernews · DemiGuru · 8月14日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49303202)

**「背景」** uBlock Origin 是一个免费开源的内容过滤和广告拦截扩展，可用于 Firefox 和基于 Chromium 的浏览器。谷歌 Chrome 等 Chromium 浏览器正在推进 Manifest V3，限制旧版扩展的拦截能力，导致 uBlock Origin 被逐步淘汰。Firefox 明确表示将继续支持 uBlock Origin，因此在 Edge、Chrome 转向 Manifest V3 后，Firefox 成为唯一完全支持 uBlock Origin 的主要浏览器。

**「影响」** 在 Chrome 等强制执行 Manifest V3 的 Chromium 浏览器上，uBlock Origin 的广告与跟踪拦截能力被削弱，用户隐私与安全保护下降；只有 Firefox（以及仍保留 MV2 支持的 Brave）能继续提供接近完整的拦截功能。不过，Brave 等浏览器通过内置开关或企业策略仍可临时启用 MV2，但长期支持前景尚不确定。

**「社区讨论」** 评论者对“最后支持”的说法提出争议，指出 Brave、Edge 和 Helium 等浏览器仍提供不同形式的 uBlock Origin 支持；同时有人强调 Firefox 会对 uBlock Origin 每次更新进行代码审核以降低恶意软件风险，并认为 Google 通过 Manifest V3 限制了扩展的自由度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html">Firefox is now the last major browser that still supports uBlock Origin</a></li>
<li><a href="https://9to5windows.com/firefox-last-major-browser-supporting-ublock-origin/">Firefox Confirms It Remains the Last Major Browser Supporting ...</a></li>
<li><a href="https://factually.co/fact-checks/technology/ublock-origin-features-lost-under-manifest-v3-privacy-impact-8c0ddb">What uBlock Origin Features Are Lost Under Manifest V3...</a></li>
<li><a href="https://factually.co/fact-checks/technology/manifest-v3-ad-blockers-ublock-origin-brave-firefox-2026-4deb07">How Manifest V3 Changed Ad Blockers: uBlock Origin, Br...</a></li>

</ul>
</details>

**标签**: `#browser-extensions`, `#ad-blocking`, `#privacy`, `#Manifest V3`, `#open-source`

---

<a id="item-tech-news-4"></a>
### [小红书开源 dots3-note：280B 参数仅 16B 激活](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室开源了 dots3-note preview，这是 dots3 系列中首个开放权重的模型。该模型为总参数 280B、每次激活 16B 的混合专家（MoE）多模态模型，支持 512K 上下文，可处理文字、图片、视频和音频。模型引入了 TEMPO 新强化学习方法，通过自批判与测试时价值估计训练长程智能体。权重已在 Hugging Face 开源，并同步发布 VibeSearchBench 与 VibeLifeBench 两个真实场景智能体基准。

telegram · zaihuapd · 8月14日 08:27

**「背景」** 混合专家（MoE）模型将参数分布到多个专家子网络中，每次推理只激活部分专家，因此总参数量大但实际激活参数较少，可在保持容量的同时控制计算成本。“开放权重”指模型权重公开可下载，开发者可自行部署或微调，不同于仅提供 API 的闭源模型。dots3-note preview 即属于此类 MoE 模型，社区整理的信息显示其采用 256 个路由专家加一个共享专家、top-8 路由，以及 1 个密集层加 45 个 MoE 层的结构。

**「影响」** 对需要自托管或微调多模态大模型的开发者和研究者，这次开放权重提供了总参数 280B 但每次仅激活 16B 的模型，有助于降低推理资源门槛；但其在基准上的实际表现尚待独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/dots-studio/dots3-note-prev">dots-studio/dots3-note-prev · Hugging Face</a></li>
<li><a href="https://www.orcarouter.ai/blog/dots-note-3-0-leak">dots-note-3.0 Leak: vLLM PR Reveals the IMO-Perfect Model</a></li>

</ul>
</details>

**标签**: `#open-source`, `#large language model`, `#MoE`, `#multimodal`, `#AI agents`

---

<a id="item-tech-news-5"></a>
### [PostgreSQL 修复高危 to\_char 漏洞可导致任意代码执行](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 项目披露高危漏洞 CVE-2026-14669：to\_char\(timestamptz\) 在处理超长 POSIX 时区缩写时会发生堆缓冲区溢出，使能设置时区的数据库用户以 PostgreSQL 服务进程的操作系统权限执行任意代码，CVSS 评分为 8.8。受影响版本为 18.5、17.11、16.15、15.19 和 14.24 之前的版本；由于 18.5 因回归问题未正式发布，18 系列用户应直接升级至 18.6，其他系列分别升级至 17.11、16.15、15.19 或 14.24。此次小版本更新不需要转储数据库或运行 pg\_upgrade，更新程序文件并重启服务即可。

telegram · zaihuapd · 8月14日 14:35

**「背景」** PostgreSQL 的 to\_char\(timestamptz\) 函数在格式化时间戳时可能展开 POSIX 时区缩写；该处理路径未充分校验缩写长度时，可能越界写入堆缓冲区。漏洞利用前提是攻击者已拥有低权限数据库账户并能设置时区，不能匿名利用。

**「影响」** 所有运行受影响 PostgreSQL 小版本的数据库管理员应在条件允许时尽快应用 18.6、17.11、16.15、15.19 或 14.24 更新，否则低权限数据库用户可能将漏洞转化为操作系统级任意代码执行。

**标签**: `#PostgreSQL`, `#security vulnerability`, `#CVE`, `#database`, `#arbitrary code execution`

---

<a id="item-tech-news-6"></a>
### [苹果自研中国专属 AI 模型获备案 联手阿里或成首个获批外企](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 8.0/10

路透社援引知情人士报道，苹果已专门为中国市场训练一款大语言模型，并获得阿里巴巴支持，改变此前依赖第三方模型的策略。Apple Intelligence 预计将在未来数月随 iOS 更新在中国上线。中国网信办已于上月备案该生成式 AI 服务。若顺利落地，苹果或成为首个获北京批准在中国提供自有 AI 模型的外国公司。

telegram · zaihuapd · 8月14日 14:47

**「背景」** 在中国市场，生成式人工智能服务需向国家网信办备案并符合本地监管要求，外国厂商通常只能接入本地合规的第三方模型，因此苹果此前的 Apple Intelligence 在华依赖第三方方案。阿里巴巴作为本地合作方为苹果提供训练支持和合规经验，而苹果保留对该自研大语言模型的所有权。这种“自研＋本地支持”的双轨策略旨在同时满足监管要求并掌控中国用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investing.com/news/stock-market-news/apple-trains-own-ai-model-for-china-with-alibaba-support-reuters-reports-4859693">Apple trains own AI model for China with Alibaba support , Reuters ...</a></li>
<li><a href="https://qz.com/apple-china-ai-model-alibaba-training-081426">Apple trains China -specific AI model with Alibaba &#x27;s help</a></li>
<li><a href="https://www.remio.ai/post/alibaba-apple-ai-partnership-gives-apple-more-control-in-china">Alibaba Apple AI Partnership Gives Apple More Control in China</a></li>

</ul>
</details>

**标签**: `#Apple`, `#China`, `#Alibaba`, `#AI`, `#LLM`, `#Regulatory`

---

<a id="item-tech-news-7"></a>
### [RustDesk 现支持 Wayland 真正的无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 官方宣布现已支持在 Wayland 下进行真正的无人值守远程访问，解决了 Linux 远程管理中长期存在的限制。Wayland 的安全模型此前使无人值守远程访问难以实现，这一更新填补了开源远程桌面工具在该场景下的明显空白。该功能主要面向系统管理员和 Linux 用户，官方公告获得了社区积极反馈。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**「背景」** Wayland 的合成器安全模型默认禁止应用直接捕获屏幕或注入输入，通常需要用户通过 xdg-desktop-portal 弹窗授权，因此难以实现无人值守的远程控制；这使 Linux 远程管理长期依赖 X11 或 VNC 等传统方案。RustDesk 是一款开源远程桌面工具，此前在 Wayland 上也需要用户在会话端手动确认共享。此次官方博客宣布的新预览版通过底层接口（如 libei）实现了真正的 Wayland 无人值守访问，并支持多显示器，初步提供面向 Debian/Ubuntu x86\_64 系统。

**「影响」** 对于需要通过 Wayland 管理远程 Linux 机器的系统管理员，RustDesk 可直接用于无人值守场景，而不必依赖 X11 或额外会话代理。但具体兼容性和稳定性仍需结合实际发行版验证。

**「社区讨论」** 社区普遍欢迎该更新，有用户表示此前刚遇到此问题，现已解决。但也有评论指出自托管时 RustDesk 仍不支持加密连接，并有人询问其与 VNC、Remmina over SSH 等方案的差异及对树莓派等场景的适用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/blog/unattended-remote-access-wayland/">Unattended Remote Access on Wayland with RustDesk — RustDesk</a></li>
<li><a href="https://github.com/rustdesk/rustdesk/discussions/10016">Wayland : Select the screen to be shared (Operate on the peer side)...</a></li>

</ul>
</details>

**标签**: `#rustdesk`, `#wayland`, `#remote-desktop`, `#open-source`, `#linux`

---

<a id="item-tech-news-8"></a>
### [GLM-5.3：前沿编程模型，具备新兴网络能力](https://z.ai/blog/glm-5.3) ⭐️ 7.0/10

GLM-5.3 被发布为前沿编程模型，官方博客称其具备新兴网络能力并吸引开发者关注。社区用户报告称，该模型在红队场景中可执行安全研究，包括发现 WordPress 插件 0day、实现 RCE 以及适配 6.8 内核漏洞利用，并有另一个 GLM 智能体担任防御方。Z.AI 还通过 cvd.z.ai 披露在开源和流行软件中扫描到的漏洞，其中许多为高危或严重级别且处于保密期。有评论认为其表现仅略逊于 Sol 和 Fable，但目前尚未形成取代 OpenAI 的充分经济理由；模型权重预计两周后发布，当前仍是 GLM 5.2 加上后训练改进。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**「背景」** 据 Unite.AI 报道，GLM-5.3 于 2026 年 8 月 14 日发布，沿用与 GLM-5.2 相同的基础模型，所有能力提升来自大规模后训练；其在 Z.ai Code Bench 上较 GLM-5.2 提高 50%，并在 Terminal Bench 3.0 和 Agents&\#x27; Last Exam 等公开基准上取得开源最佳成绩。社区讨论还提到，该模型在红队场景中表现出超出预期的网络能力，Z.ai 同时通过 cvd.z.ai 对开源软件进行扫描并披露发现的漏洞。

**「影响」** 对参与红队或漏洞研究的开发者而言，GLM-5.3 可能显著降低 0day 发现和利用适配的成本，但需要更高订阅档位（用户报告从 18 美元升级至 80 美元）。不过其“新兴网络能力”的表述尚未得到独立验证。

**「社区讨论」** 社区总体认为 GLM-5.3 在编程与安全研究上接近前沿，但评论也提到其仍未完全超越 Sol 和 Fable，经济上不足以替代 OpenAI；同时有人对大规模扫描漏洞的成本下降和 Anthropic 类似项目表示关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unite.ai/z-ai-launches-glm-5-3-with-frontier-coding-and-a-cyber-capability-that-outgrew-its-training/">Z.ai Launches GLM-5.3 With Frontier Coding and a Cyber Capability That Outgrew Its Training – Unite.AI</a></li>
<li><a href="https://www.reddit.com/r/singularity/comments/1vnz30c/glm_53_released_frontier_coding_with_emergent/">r/singularity on Reddit: GLM 5.3 released: Frontier Coding with Emergent Cyber Capabilities</a></li>
<li><a href="https://news.ycombinator.com/item?id=49294997">GLM-5.3: Frontier coding with emergent cyber capabilities | Hacker News</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#cybersecurity`, `#software engineering`, `#GLM`

---

<a id="item-tech-news-9"></a>
### [不要分类，让模型“幻觉”标签再用向量匹配](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison 介绍了 Doug Turnbull 提出的标签分类方法：不给模型现有标签表，而是让 LLM 先“幻觉”出可能适合内容的候选标签，再用向量嵌入与已有的 1,856 个标签语料做相似度匹配，找到最接近的具体标签。这样避免把大量标签一次性塞进提示词。Turnbull 的示例提示会给出标签层级形状，帮助模型生成更可用的猜测。

rss · Simon Willison · 8月14日 21:54

**「背景」** 传统分类任务通常把候选标签列表放入提示词让模型选择，但当标签词汇很大时提示词会过长、成本高或超出上下文限制。向量嵌入可以把文本映射为可比较相似度的向量，常用于语义搜索和聚类。

**「影响」** 对于拥有大量标签但不想受提示词长度限制的开发者，这种方法提供了一种实际可行的替代方案，但匹配质量取决于嵌入模型和候选标签与现有词汇的语义接近程度。

**标签**: `#large language models`, `#vector embeddings`, `#tagging`, `#information retrieval`, `#prompt engineering`

---

<a id="item-tech-news-10"></a>
### [AI 人体组织实验年测 300 万次](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 7.0/10

Vivodyne 在旧金山南部部署了衣柜大小的机器人实验室，用于培养人体组织，并由 AI 设计实验以预测新药疗效与安全性。该系统的 12 个“蜂巢”机器人实验室每年可对 300 多万个人体组织样本开展受控试验，容量是美国全部临床试验总和的两倍。公司称目前约 90% 的临床试验在通过动物测试后仍失败，因此大规模人体组织实验有望减少对动物测试的依赖。这些数据由公司报告，尚未经过临床验证。

telegram · zaihuapd · 8月14日 01:48

**「背景」** 药物开发长期依赖动物实验，但约 90%进入临床试验的新药在通过动物测试后仍会失败，动物模型难以可靠预测人体反应。Vivodyne 是一家位于旧金山南部的生物技术公司，已融资 4000 万美元，开发自动化机器人平台来培养和测试人体组织；公司称其系统可在两周内自动培养并测试超过 10 万个人体组织，从而在临床试验前提供更接近人体的数据。

**「影响」** 若 Vivodyne 的平台获得临床验证，制药公司可能用每年 300 万次以上的人体组织测试替代部分动物实验，从而改善新药进入临床试验后的成功率。该能力目前为公司报告，尚未经过独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discover-pharma.com/vivodyne-raises-40m-to-advance-human-tissue-testing-as-alternative-to-animal-models/">Vivodyne raises $40M to advance human tissue testing as...</a></li>
<li><a href="https://www.businesswire.com/news/home/20250528498236/en/Vivodyne-to-Replace-Animal-Testing-With-$40-Million-Funding-to-Reverse-95-Clinical-Trial-Failure-Rate">Vivodyne to Replace Animal Testing With $40 Million Funding to...</a></li>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotech`, `#lab automation`, `#drug discovery`, `#robotics`

---

<a id="item-tech-news-11"></a>
### [谷歌被令一周内取消第三方商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

美国地区法官 James Donato 已下令谷歌简化竞品安卓应用商店的安装流程，删除 Play Store 中多余的步骤与警告弹窗。法院认定，用户需先“查看”后才会出现“安装”等多步操作属于蓄意制造的“反竞争摩擦”，用于吓退普通用户。谷歌须在一周内完成修改，使安装第三方市场像安装普通安卓应用一样直接。该指令源自 Epic 诉谷歌反垄断案，此前陪审团已裁定谷歌在安卓应用分发上构成非法垄断。

telegram · zaihuapd · 8月14日 09:55

**「背景」** Epic 诉谷歌案围绕谷歌 Play 商店对安卓应用分发的控制展开；陪审团此前裁定谷歌在该市场构成非法垄断。本次法官指令是裁决后的具体整改措施之一，要求消除用户在安装第三方应用商店时的额外警告和多步操作。

**「影响」** 最直接的影响是，一周内安卓用户安装第三方市场将不再需要经过 Play Store 的额外查看与警告步骤，第三方商店的安装路径与普通应用一致。

**标签**: `#antitrust`, `#android`, `#google-play`, `#epic-v-google`, `#app-stores`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [DSpark 置信度调度：vLLM 自适应验证](https://vllm.ai/blog/2026-08-14-dspark-adaptive-verification) ⭐️ 9.0/10

rss · vLLM Blog · 8月14日 00:00

**「背景」** 推测解码在 batch size 为 1 时，GPU 处于内存带宽受限、算力有富余的状态，额外草稿 token 几乎免费；但并发升至 256 时，被拒绝的草稿 token 会与真实 token 争抢算力，静态的草稿长度 num\_speculative\_tokens 无法同时适应低、高并发。作者指出，7 token 块的最后一个草稿 token 存活率不足 10%，而第一个超过 70%。

**「方案」** DSpark 先用置信头给每个草稿位置打分，再将其转化为沿请求递减的存活概率；给定草稿 token 预算 B，分配就是对存活分数做全局 top-B，各请求得到连续前缀，不同请求的槽位相互竞争。B 通过最大化每步时间内的期望 token 数决定：分子为采样请求的奖励 token 加上前 B 个草稿槽位的存活概率之和，分母是按 token 数和请求数索引的启动剖析成本表——作者在启动时对固定形状的假步骤各测五次取中位数，并强制曲线单调。CPU 在 GPU 执行上一步时用上一轮置信度数组计算 B，GPU 再按当前置信度把 B 个槽位分配给请求，整个过程不回读主机。为实现变长验证，作者引入 varlen decode CUDA graphs，依赖稀疏 MLA 和 DeepGEMM indexer。据作者报告，在 DeepSeek-V4-Pro-0813、TP=8 的 8×B300 上，并发 1 到 256 的自适应验证始终处于吞吐-交互 Pareto 前沿，低并发近似长固定块、高并发近似短固定块。目前该特性要求在 SM100 上报告 AttentionCGSupport.ALWAYS 的后端，且不支持 --enforce-eager、LoRA、流水线并行，并会拒绝输出 logprobs。

**「启示」** 该工作表明，用置信度驱动的逐步预算替代静态推测长度，可减少用户按负载调参，使 DSpark 更容易成为默认开启的推理优化。

**标签**: `#speculative-decoding`, `#vLLM`, `#cuda-graphs`, `#adaptive-verification`, `#LLM-inference`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [伯克希尔二季度转净买入，Alphabet 升至第三大持股](https://www.cnbc.com/2026/08/14/berkshire-hathaway-boosts-alphabet-to-a-top-three-holding-ups-delta-and-housing-bets.html) ⭐️ 8.0/10

监管文件显示，伯克希尔哈撒韦第二季度结束连续 14 个季度的股票净卖出，转为近 200 亿美元净买入；截至 6 月底其对 Alphabet 持股环比增长 83%，价值 379 亿美元，成为第三大美国上市持股。

rss · CNBC Finance · 8月14日 21:06

**「背景」** Alphabet 增持主要来自 6 月初宣布的 100 亿美元私募股票购买，用于其 AI 基础设施扩张；巴菲特对 CNBC 表示此次看多由他推动并得到 CEO Greg Abel 支持。

**标签**: `#Berkshire Hathaway`, `#Alphabet`, `#13F filing`, `#equity holdings`, `#Warren Buffett`

---

<a id="item-finance-news-2"></a>
### [高盛从 AI 基础设施融资潮中获利](https://www.cnbc.com/2026/08/14/goldmans-latest-cash-cow-is-all-about-funding-the-ai-infrastructure-boom.html) ⭐️ 8.0/10

高盛正从 AI 基础设施融资潮中获利：本周作为联合账簿管理人参与英特尔 20 亿美元股票发行，并与另外五家机构共同推进英伟达 500 亿美元 AI 建设融资计划；此前还参与 Alphabet 85 亿美元股票发行。

rss · CNBC Finance · 8月14日 20:05

**「背景」** 作为联合账簿管理人，高盛以折扣价从发行方买入股票再卖给机构客户，赚取承销费、管理费和销售佣金，这些收入计入其全球银行与市场部门。

**标签**: `#Goldman Sachs`, `#AI infrastructure`, `#investment banking`, `#Nvidia`, `#Intel`

---

<a id="item-finance-news-3"></a>
### [监管机构与银行加大对预测市场的审查力度](https://www.cnbc.com/2026/08/14/prediction-markets-scrutiny-mounts-from-regulators-and-banks.html) ⭐️ 7.0/10

美国商品期货交易委员会\(CFTC\)已对预测平台上的“提及市场”启动内部审查，华盛顿州法官下令阻止 Kalshi 在该州运营多个市场。英国《金融时报》报道摩根大通去年 10 月切断与 Polymarket 的金融服务，但 Polymarket 否认这一说法。

rss · CNBC Finance · 8月14日 19:21

**「背景」** “提及市场”是交易者押注特定词语是否会出现在演讲、财报电话会或电视广播中的合约，批评者认为其易被个人操纵。据 Dune Analytics 数据，Kalshi 上该类市场上月交易量约 330 万美元；上月 CFTC 还表示正在调查一名特朗普前提词器操作员，此人涉嫌在 Kalshi 上押注特朗普演讲内容并获利 9 万美元。

**标签**: `#prediction markets`, `#CFTC`, `#regulation`, `#Kalshi`, `#Polymarket`

---

<a id="item-finance-news-4"></a>
### [Uber 与 Pony.ai 计划在欧洲部署 2,000 辆自动驾驶出租车并扩展至中东](https://www.cnbc.com/2026/08/14/uber-partners-with-chinas-ponyai-for-2000-robotaxis-in-europe.html) ⭐️ 7.0/10

Uber 与 Pony.ai 周五宣布，计划在欧洲部署 2,000 辆 Pony.ai 自动驾驶出租车，并将合作扩展至中东；两家公司未公布具体城市和时间表。

rss · CNBC Finance · 8月14日 01:02

**「背景」** 此前，今年 3 月底，Uber 与 Pony.ai 已在克罗地亚首都萨格勒布推出商业自动驾驶出租车服务，并称这是欧洲首个此类服务。

**标签**: `#Uber`, `#Pony.ai`, `#robotaxis`, `#autonomous vehicles`, `#Europe`

---

<a id="item-finance-news-5"></a>
### [中信旗下信宸资本据报接近收购阿里灵犀互娱，估值或超 15 亿美元](https://www.bloomberg.com/news/articles/2026-08-14/trustar-is-said-to-near-1-5-billion-deal-for-alibaba-gaming-arm) ⭐️ 7.0/10

彭博报道，中信集团旗下的私募机构信宸资本（Trustar Capital）正接近收购阿里巴巴旗下游戏业务灵犀互娱，交易估值可能超过 15 亿美元，但磋商仍在进行且尚未作出最终决定。

telegram · zaihuapd · 8月14日 10:24

**「背景」** 阿里巴巴首席执行官吴泳铭正推动剥离非核心资产以聚焦人工智能和云计算，而灵犀互娱的旗舰游戏是与光荣特库摩合作开发的《三国志·战略版》。

**标签**: `#M&amp;A`, `#Alibaba`, `#CITIC Group`, `#gaming`, `#private equity`

---