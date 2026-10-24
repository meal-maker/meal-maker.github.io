---
layout: default
title: "Horizon Summary: 2026-10-24 (ZH)"
date: 2026-10-24
lang: zh
---

> 从 33 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [iPhone 遭成功入侵：漏洞演示与社区讨论](#item-tech-news-1) ⭐️ 8.0/10
2. [Kimi K3.1 Pro 与 Highspeed 发布：开放权重并限制网络能力](#item-tech-news-2) ⭐️ 7.0/10
3. [Dessa：宣称最逼真的全双工语音模型](#item-tech-news-3) ⭐️ 7.0/10
4. [谷歌隐私政策更新：可能将 Gmail 与 Google Photos 数据用于广告](#item-tech-news-4) ⭐️ 7.0/10
5. [亚马逊 Trainium 挑战 AI 训练王者地位](#item-tech-news-5) ⭐️ 7.0/10
6. [蜂群模仿与多臂老虎机 RL 等价](#item-tech-news-6) ⭐️ 7.0/10
7. [字节火山引擎发布 Seedance 2.5 4K 模型](#item-tech-news-7) ⭐️ 7.0/10
8. [PHP 基金会建议暂时禁用上传进度功能](#item-tech-news-8) ⭐️ 7.0/10

**财经新闻**
1. [国办发文要求减缓 AI 应用就业替代影响](#item-finance-news-1) ⭐️ 8.0/10
2. [欧盟取消对中国太阳能玻璃双反关税](#item-finance-news-2) ⭐️ 7.0/10
3. [电动自行车等三类产品 CCC 认证新规 2026 年 11 月起实施](#item-finance-news-3) ⭐️ 7.0/10
4. [证监会核准设立花旗证券（中国）有限公司](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [iPhone 遭成功入侵：漏洞演示与社区讨论](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

一篇技术博客声称已成功入侵 iPhone，并发布了多个漏洞利用演示。该研究引发了对 iOS 安全边界、越狱可行性以及 Lockdown Mode 防护效果的讨论。公开条目未包含具体漏洞链、受影响 iOS 版本或利用条件，因此无法确认漏洞细节与适用范围。

hackernews · pavel\_lishin · 10月23日 16:21 · [社区讨论](https://news.ycombinator.com/item?id=50211474)

**「背景」** 该文作者在巴黎 Hexacon 会议上展示了多段 iPhone 入侵演示，并称所有细节将在后续公布（来源：tool-1-2）。在相关讨论中，用户关注“锁定模式”（Lockdown Mode）能否防御此类攻击，以及获取 root 权限后是否能阻止苹果更新或移除漏洞（来源：tool-1-1）。锁定模式是 iOS 为高风险用户提供的增强安全功能，通过限制攻击面降低被利用风险；越狱则指移除系统限制、获取 root 权限的过程。

**「对高风险用户的直接影响」** 对于面临此类攻击风险的用户，开启 Lockdown Mode 可能降低被类似漏洞利用链入侵的概率：苹果官方说明该模式可在设置中手动启用，且独立安全研究人员确认其对类似利用链有效。不过，源材料未提供这些具体演示是否已被 Lockdown Mode 覆盖的证据。

**「社区讨论」** 评论区的主要关切包括：越狱可能导致 iCloud 和 iMessage 被 Apple 锁定，使设备沦为普通播放器；Lockdown Mode 对这些漏洞是否有实际防护作用；以及安全研究圈外人员难以获得高级模型红队访问权限，被视作壁垒而非保障。也有用户提到早期 Android root 时代的自由感，并询问演示中的权限提升是否会阻止 Apple 更新或移除漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50211474">&quot; Today , we hacked what we &#x27; d set out to hack : the iPhone .&quot;</a></li>
<li><a href="https://blog.calif.io/p/iphone">Today , we hacked what we &#x27; d set out to hack : the iPhone .</a></li>
<li><a href="https://support.apple.com/en-us/105120">About Lockdown Mode - Apple Support</a></li>
<li><a href="https://www.linkedin.com/posts/rswebsols_gadget-rswebsols-activity-7440845971808460800-X_Pz">Apple Blocks DarkSword iPhone Spyware with Security ... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#iPhone`, `#security`, `#jailbreak`, `#exploit`, `#iOS`

---

<a id="item-tech-news-2"></a>
### [Kimi K3.1 Pro 与 Highspeed 发布：开放权重并限制网络能力](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

Moonshot AI 发布了 Kimi K3.1 Pro 和 K3.1 Pro Highspeed 两个开放权重模型，强调在开放权重中刻意不提供前沿的进攻性网络能力，并计划逐步提高。K3.1 Pro 在数据分析和工具调用方面的测试中，准确率从 7 月的 81% 提升到 98%，但生成速度较慢，部分问题会发起 73 次查询，而其他模型仅 18 次。社区用户报告订阅配额限制明显，有用户订阅 99 美元/月计划后在 47 分钟内触发 5 小时配额。另有反馈称模型推理内容中身份识别混乱，时而自称 Kimi 或 ChatGPT，并提及 Moonshot 或全局系统指南。

hackernews · Jowsey · 10月23日 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50212065)

**「背景」** Kimi K3 是 Moonshot AI 发布的 2.8T 参数开源权重模型，具备多模态能力和 100 万 token 上下文窗口，此前已通过 OpenRouter 等平台提供 API，定价约为每百万输入 token 1.39 美元、每百万输出 token 13 美元。K3.1 Pro 与 K3.1 Pro Highspeed 是 Moonshot AI 的新发布，其开源权重、API 访问和上下文限制等可参考现有 Kimi K3 生态。

**「影响」** 对开发者而言，K3.1 Pro 提供可部署的开放权重，但其订阅 API 的严格配额和大量工具调用导致的延迟，可能制约生产环境中的高频使用。

**「社区讨论」** 社区讨论关注模型行为更直接和推理时身份混乱，以及对开放权重但限制网络能力政策的质疑。用户同时报告了订阅配额紧张和数据分析基准的明显改进但速度较慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://k3-kimi.com/">Kimi K3: 2.8T Open - Weight Model — Benchmarks , Pricing &amp; Guides</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open weights`, `#Moonshot AI`, `#model release`

---

<a id="item-tech-news-3"></a>
### [Dessa：宣称最逼真的全双工语音模型](https://block.xyz/dessa) ⭐️ 7.0/10

Dessa 是一个全双工语音模型，声称能实现富有表现力、低延迟的对话，并可在 MacBook Pro M4 Max 或更高配置上本地运行；开发方还表示仅在单台 NVIDIA GB200 NVL72 上完成训练。该发布将“有史以来最逼真”作为宣传语，但未提供可验证的技术细节，这一说法属于营销用语。社区反馈认为对话样例令人印象深刻，但也指出标题夸大，且演示中机器“假装关心”的对话体验不自然。

hackernews · dsr12 · 10月23日 19:09 · [社区讨论](https://news.ycombinator.com/item?id=50213925)

**「背景：全双工语音模型」** 全双工语音模型允许用户与 AI 同时说话和聆听，无需等待对方结束，相比传统轮流式对话更接近自然人类交流。近期研究如 DyaPlex（全双工语音-动作模型）和 MultiTalk（扩展全双工语音模型）正在探索长上下文和多说话人场景，但此类模型通常计算资源需求较高；Dessa 声称在单台 MacBook Pro M4 Max 上本地低延迟运行，并在单个 NVIDIA GB200 NVL72 上完成训练，因此受到关注。

**「影响」** 如果声明属实，该模型可能让开发者在 MacBook Pro M4 Max 等消费级设备上获得低延迟、富有表现力的全双工语音交互，无需依赖云端 GPU。但目前技术细节和可复现性有限，实际效果尚未得到独立验证。

**「社区讨论」** 社区意见分歧：一些评论认为低延迟和本地运行“令人印象深刻”，另一些则批评“most authentic ever”是营销标题，且演示中机器假装关心的对话体验令人不适。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.03874">DyaPlex: Full - Duplex Speech -Motion Model for Dyadic Interaction</a></li>
<li><a href="https://www.alphaxiv.org/abs/2609.36903">MultiTalk: Scaling Full - Duplex Speech Models to Long... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#speech-ai`, `#full-duplex`, `#on-device-inference`, `#model-training`, `#ai`

---

<a id="item-tech-news-4"></a>
### [谷歌隐私政策更新：可能将 Gmail 与 Google Photos 数据用于广告](https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update) ⭐️ 7.0/10

谷歌正在更新其隐私政策，可能在用户主动关联某些 Google 服务后，将 Gmail 和 Google Photos 中的数据用于个性化广告。The Verge 报道称，这一变更与欧盟《数字市场法》\(DMA\) 第 5\(2\) 条相关：谷歌在欧盟向用户提供选择，可关联或不关联搜索、YouTube、广告服务、Google Play、Chrome、Google Shopping、Google Maps 等服务。谷歌表示，除非用户选择让这些服务的数据可被其他支持个性化广告的 Google 服务使用，否则不会将其用于广告。

hackernews · JustSkyfall · 10月23日 19:34 · [社区讨论](https://news.ycombinator.com/item?id=50214218)

**「背景」** 个性化广告通常依据用户在不同 Google 服务中的活动数据展示；欧盟《数字市场法》第 5\(2\)条自 2024 年 3 月 6 日起要求 Google 在欧盟让用户选择是否关联搜索、YouTube、广告服务、Google Play、Chrome、Google Shopping、Google Maps 等服务。本次政策调整意味着，当用户主动将这些服务关联后，Gmail 和 Google Photos 的数据便可能被用于支持个性化广告。Google 账户的“个人信息”页面也允许用户编辑在 Google 服务中使用的个人资料，但并非所有隐私关联选项都在此处管理。

**「影响」** 欧盟用户若不希望 Gmail 和 Google Photos 数据被用于广告，需在 DMA 关联选择中保持不关联，或通过 google.com/search-personalization 关闭个性化。

**「社区讨论」** 评论区有人提醒这是有条件的变化，并非直接读取数据；也有人认为“might”实际意味着“will”，并推荐通过 Google Takeout 配合 Immich 迁出或关闭个性化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://myaccount.google.com/intro/personal-info">Google Account</a></li>

</ul>
</details>

**标签**: `#privacy`, `#google`, `#advertising`, `#data-policy`, `#gmail`

---

<a id="item-tech-news-5"></a>
### [亚马逊 Trainium 挑战 AI 训练王者地位](https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at) ⭐️ 7.0/10

亚马逊 Trainium 此前主要被视为推理芯片，但最新分析指出它在 AI 训练任务中也已具备竞争力。该芯片提供原生 PyTorch 支持，并配套高质量 CI、TorchTitan 集成以及被称为“GPU Impossible Profiler”的性能分析工具。这些改进使 Trainium 成为现有训练硬件的有力替代选项。文章强调其工具链和软件生态的成熟度，而不仅仅是硬件性能。不过目前仍处于挑战阶段，尚未形成明确突破。

rss · Semianalysis · 10月23日 19:06

**「背景：Trainium 与 PyTorch 训练生态」** AWS Trainium 是亚马逊为 AI 训练和推理设计的定制 AI 芯片。此前，开发者需要通过 TorchNeuron 等工具在 Trainium 上运行 PyTorch，而 TorchNeuron 现已与 PyTorch 原生的分布式训练框架 TorchTitan 集成，支持使用 FSDP 等标准 PyTorch 模式在 Trainium 实例上扩展模型训练。TorchTitan 本身是一个 PyTorch 原生平台，用于快速实验和大规模生成式 AI 模型训练。

**「影响」** 对于需要训练大规模模型的开发者和云用户，Trainium 的原生 PyTorch 支持及配套工具链意味着它可能成为现有训练硬件之外的一个可行选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai">Amazon &#x27;s TorchNeuron runs PyTorch on AWS Trainium chips</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS | Amazon Web Services, Inc.</a></li>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch / torchtitan : A PyTorch native platform for training ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Amazon Trainium`, `#PyTorch`, `#machine learning infrastructure`, `#AI training`

---

<a id="item-tech-news-6"></a>
### [蜂群模仿与多臂老虎机 RL 等价](https://www.reddit.com/r/MachineLearning/comments/1xdhf7r/r_the_hive_mind_is_a_single_reinforcement/) ⭐️ 7.0/10

这篇 Reddit 研究帖证明，本地模仿驱动的集体决策（如蜜蜂通过摇摆舞选择巢址）与单智能体多臂老虎机强化学习之间存在精确数学等价。作者利用演化复制者动态，将选择各选项的个体比例视为单个宏观智能体的动作概率策略，并证明经典“成功模仿”协议的群体更新与 Cross Learning 老虎机算法的期望更新一致。对于蜜蜂摇摆舞的“加权投票”模型，群体在宏观层面执行一种新算法 Maynard-Cross Learning（MCL），其中 N 个个体相当于 N 个并行环境采样，有效每样本步长为 alpha=1/N。论文发表于 arXiv:2410.17517，项目页面与代码已公开。该结果为“蜂巢思维”作为群体级强化学习提供了形式化机制，并为群机器人和社会经济模仿动力学提供分析工具。

reddit · r/MachineLearning · /u/mistlab · 10月23日 15:37

**「背景」** 群体智能中，简单个体通过局部模仿或规则（如蜜蜂摆尾舞的“加权选民模型”）进行集体决策，演化博弈论常用复制者动态描述各选项比例的变化；多臂老虎机强化学习则让单个智能体根据奖励更新动作概率，Cross Learning 等经典算法的期望更新也具有类似形式。该论文从这一共同数学结构出发，把群体策略分布视作单个宏观智能体的策略，并在蜜蜂模型上导出了 Maynard-Cross Learning。

**「影响」** 该等价关系为研究群体智能与分布式机器人系统的研究者提供了一种宏观强化学习视角：蜂群式局部模仿可被视为以 α=1/N 为有效步长的 Maynard-Cross Learning 多臂老虎机算法，可用于分析社会/经济模仿动态并设计去中心化群体机器人策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent</a></li>
<li><a href="https://www.alphaxiv.org/abs/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent | alphaXiv</a></li>
<li><a href="https://www.researchgate.net/publication/385177126_Bridging_Swarm_Intelligence_and_Reinforcement_Learning">(PDF) Bridging Swarm Intelligence and Reinforcement Learning</a></li>
<li><a href="https://www.alphaxiv.org/abs/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent | alphaXiv</a></li>
<li><a href="https://arxiv.org/html/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#multi-armed bandits`, `#swarm intelligence`, `#collective decision-making`, `#theoretical machine learning`

---

<a id="item-tech-news-7"></a>
### [字节火山引擎发布 Seedance 2.5 4K 模型](https://mp.weixin.qq.com/s/yUa8oh-IWfl5lDQzGSKWeg) ⭐️ 7.0/10

字节跳动旗下火山引擎正式发布 Seedance 2.5 4K 模型，称其为该系列最强版本。该模型经过专项训练，更充分学习人物表情、细微动作与画面细节，并支持 Draft 模式：用户可先用 480P 样片快速验证分镜，满意后再生成 4K 正片。模型具备 10-bit 色深，色彩层次丰富、过渡平滑，官方称画面质感可胜任大荧幕。在影视文戏测试中，4K 版本对人物细微反应的呈现更充分，表演更有层次。目前该模型仅供部分企业客户试用，后续或将逐步扩大开放范围。

telegram · zaihuapd · 10月23日 08:27

**「背景」** Seedance 是字节跳动推出的视频生成模型系列，火山引擎是其云服务平台；此前 Seedance 2.0 版本已支持画面与声音同步生成，最高输出 1080p。此次 Seedance 2.5 4K 在分辨率、色彩深度及预览流程上进一步升级，因此更面向影视级应用。

**「影响」** 对于已获得试用资格的企业客户，Seedance 2.5 4K 可通过 480P Draft 模式降低创意验证成本并产出 10-bit 4K 画面；但当前开放范围有限，普通创作者尚无法直接使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://imagetopsd.ai/zh/models/seedance-2-0">Seedance 2 .0 视频生成器：画面和声音一起出 | ImageToPsd.AI</a></li>

</ul>
</details>

**标签**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#4K model`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [PHP 基金会建议暂时禁用上传进度功能](https://x.com/ThePHPF/status/2113580383875019242) ⭐️ 7.0/10

PHP 基金会发布安全建议，要求用户在下一个 PHP 版本发布前将 session.upload\_progress.enabled 设为 0，以缓解编号为 CVE-2026-115560 的远程代码执行漏洞。该漏洞仅在运行时将非默认 serialize\_handler 切换为“php”的应用程序中才会触发，因此实际受影响范围受限。基金会提醒满足该条件的应用应尽快禁用上传进度功能。此前基金会也曾因 CVE-2026-109619 建议保持该功能禁用。

telegram · zaihuapd · 10月23日 13:46

**「背景」** PHP 的上传进度功能允许在会话（session）中记录文件上传进度，由 session.upload\_progress.enabled 控制。serialize\_handler 用于决定会话数据的序列化格式；本漏洞发生在运行过程中把非默认序列化处理器切换到 php 的场景。

**「影响」** 满足触发条件的 PHP 应用如果继续启用上传进度，可能遭受远程代码执行，应在下一个版本修复前将 session.upload\_progress.enabled 设为 0。

**标签**: `#PHP`, `#security`, `#vulnerability`, `#RCE`, `#web development`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [国办发文要求减缓 AI 应用就业替代影响](https://mp.weixin.qq.com/s/St8URoMYcV-voM7kLAK3Bw) ⭐️ 8.0/10

国务院办公厅印发《关于适应人工智能技术发展助力构建就业友好型发展方式的意见》，要求减缓人工智能应用对就业的替代影响。文件提出优先在劳动力紧缺、环境高危等岗位推广 AI，稳慎把握其在劳动密集型行业应用的范围、力度和节奏，并鼓励企业探索建立失业缓冲期制度，提前告知受影响劳动者并提供转型转岗就业支持。

telegram · zaihuapd · 10月23日 12:54

**「背景」** 人工智能在劳动密集型行业的应用可能替代部分人工岗位，国务院办公厅此次发文意在通过优先推广紧缺和高危岗位、稳慎控制推广节奏及建立失业缓冲期来降低就业冲击。

**「对劳动者的影响」** 该政策若被企业采纳，将主要惠及劳动密集型行业可能受 AI 替代影响的劳动者，通过提前告知、转型转岗支持和失业缓冲期降低就业冲击风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.workercn.cn/papers/grrb/2026/07/13/7/grrb202607137.pdf">grrb0720260713B</a></li>

</ul>
</details>

**标签**: `#人工智能`, `#就业政策`, `#劳动市场`, `#国务院办公厅`, `#科技治理`

---

<a id="item-finance-news-2"></a>
### [欧盟取消对中国太阳能玻璃双反关税](https://www.163.com/dy/article/L9R94K6105484D40.html) ⭐️ 7.0/10

欧盟委员会 2026 年 10 月 21 日发布公告，废止对原产于中国的太阳能玻璃征收的反倾销和反补贴关税，原税率 84.2%，10 月 22 日生效；自 2025 年 7 月 22 日起缴纳的相关关税可申请退还，但不计利息。

telegram · zaihuapd · 10月23日 06:54

**「背景」** 欧盟此前对原产于中国的太阳能玻璃实施反倾销和反补贴措施，其中反倾销税率因企业而异（如 Flat Glass Group 42.1%、Xinyi Group 39.3%），并曾于 2019 年启动日落复审调查。

**「影响」** 此举将降低中国太阳能玻璃出口欧盟的关税成本，影响相关出口企业和欧盟下游光伏组件买家，但仅涉及太阳能玻璃这一单一产品细分市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bbs.fobshanghai.com/thread-4962645-1-107.html">bbs.fobshanghai.com/thread-4962645-1-107.html</a></li>
<li><a href="https://guangfu.bjx.com.cn/news/20190515/980630.shtml">欧 盟 对我光伏 玻 璃 发起 反 倾 销 反 补 贴 日落复审调查-北极星 太 阳 能 光伏网</a></li>

</ul>
</details>

**标签**: `#trade policy`, `#solar glass`, `#China-EU trade`, `#tariffs`, `#renewable energy`

---

<a id="item-finance-news-3"></a>
### [电动自行车等三类产品 CCC 认证新规 2026 年 11 月起实施](https://www.gelonghui.com/live/2726360) ⭐️ 7.0/10

中国市场监管总局宣布，从 2026 年 11 月 1 日起对电动自行车、玩具、童车实施更严格的 CCC 认证（中国强制性产品认证）新规。其中电动自行车须实行“一车一池一充一码”，出厂配齐全部必需部件并随车附一致性证书，新规还将加强证后跟踪检查和抽样检测。

telegram · zaihuapd · 10月23日 10:12

**「背景」** CCC 全称为中国强制性产品认证（China Compulsory Certification），是国家对部分产品实行的市场准入制度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://club.dns-shop.ru/wiki/t-83-portativnyie-akkumulyatoryi/152398-bez-znachka-sertifikata-ccc-china-compulsory-certification-na-p/">Без значка сертификата CCC ( China Compulsory Certification ) на...</a></li>

</ul>
</details>

**标签**: `#China`, `#regulation`, `#CCC certification`, `#electric bicycles`, `#product safety`

---

<a id="item-finance-news-4"></a>
### [证监会核准设立花旗证券（中国）有限公司](https://mp.weixin.qq.com/s/f_fCJUEObewqgAe5Ie7wHA) ⭐️ 7.0/10

中国证监会于 10 月 23 日核准设立花旗证券（中国）有限公司，注册地为上海，注册资本人民币 12 亿元，由花旗环球金融控股有限公司 100%出资，业务范围包括证券经纪、证券投资咨询、证券承销与保荐及证券自营。

telegram · zaihuapd · 10月23日 12:29

**「背景」** 此前，证监会已对花旗环球金融控股有限公司设立独资证券公司的申请文件提出反馈意见，要求补充主要股东财务状况、近三年长期信用评级及展望等信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lanjinger.com/d/227503">lanjinger.com/d/227503</a></li>

</ul>
</details>

**标签**: `#China`, `#securities regulation`, `#foreign investment`, `#Citigroup`, `#market access`

---