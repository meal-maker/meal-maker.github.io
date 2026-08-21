---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> 从 50 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [误配电话路由 DNS 记录军事通话](#item-tech-news-1) ⭐️ 8.0/10
2. [Felony Bench：AI 代理重罪问责讨论](#item-tech-news-2) ⭐️ 7.0/10
3. [美国公民边境删手机数据被控重罪](#item-tech-news-3) ⭐️ 7.0/10
4. [DeepSeek 推出实验性视觉模型 v4-flash-vision-exp](#item-tech-news-4) ⭐️ 7.0/10
5. [开源模型是否正在追赶闭源模型？](#item-tech-news-5) ⭐️ 7.0/10
6. [9 模型实测：输出简洁可省钱，压缩输入提示更贵](#item-tech-news-6) ⭐️ 7.0/10
7. [英伟达被曝筹划中国版 B30A 芯片，性能或高于 H20](#item-tech-news-7) ⭐️ 7.0/10
8. [Anthropic 拟调整企业数据留存政策 客户可存自有云端](#item-tech-news-8) ⭐️ 7.0/10
9. [亚马逊购书扫描训练 AI 后销毁](#item-tech-news-9) ⭐️ 7.0/10
10. [OpenAI API 预览开放 GPT-Image-2 透明背景生成](#item-tech-news-10) ⭐️ 7.0/10
11. [特斯拉在华发起最大规模召回，逾 500 万辆车将推送软件修复](#item-tech-news-11) ⭐️ 7.0/10

**科技博客**
1. [IsoExec：统一执行消除 SkyRL 训练与推理不一致](#item-tech-blog-1) ⭐️ 7.0/10

**财经新闻**
1. [广州中院裁定恒大地产集团破产清算，负债曾达 1.83 万亿元](#item-finance-news-1) ⭐️ 9.0/10
2. [三星电子宣布 2026 年股东回报目标为 90 万亿至 110 万亿韩元](#item-finance-news-2) ⭐️ 8.0/10
3. [发改委发布对外投资管理办法修订征求意见稿 拟收紧资金出境](#item-finance-news-3) ⭐️ 8.0/10
4. [长江存储科创板 IPO 获受理，拟融资 330 亿元](#item-finance-news-4) ⭐️ 8.0/10
5. [盘前异动：BJ&\#x27;s Wholesale、Ross Stores、加密股和 Broadcom 上涨](#item-finance-news-5) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [误配电话路由 DNS 记录军事通话](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 8.0/10

作者披露，因 e164.arpa/ENUM 电话路由 DNS 基础设施存在配置错误，其服务器意外接收并记录了数十万条电话呼叫路由查询，其中包括指向军事基地的记录。这些数据属于呼叫路由元数据而非通话内容，但暴露了遗留 ENUM 系统在号码解析和路由查询过程中缺乏访问控制的问题。该事件凸显了长期未被修复的电信基础设施安全风险。

hackernews · gavide · 8月21日 13:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**「e164.arpa 与 ENUM 背景」** ENUM 是一种将 E.164 电话号码映射到 DNS 域名的机制：去除除数字外的字符、在每位数字间加点、反转顺序，最后追加 \`.e164.arpa\`，以便通过 DNS 查询该号码关联的通信服务（如 SIP 地址）。公共 e164.arpa 中的 ENUM 部署长期存在运维问题，RIPE NCC 在 2020 年的审查中已指出部分委派损坏，或容易被误用或劫持。基础设施 ENUM（Infrastructure ENUM）也定义在同一 e164.arpa 树中，但通常通过私有解析服务提供号码携带等信息，而非面向公开查询。

**「影响」** 该配置缺陷使攻击者能够接管整个地区的 e164.arpa 电话网络基础设施域，从而收集或篡改通向军事基地的呼叫路由元数据；作者已实际记录数十万条此类呼叫数据，表明暴露范围大且持续时间长。目前尚不清楚相关运营商或军事机构是否已采取补救措施。

**「社区讨论」** 评论区有观点指出，e164.arpa/ENUM 并未完全死亡，而是转为通过 VPN 访问私有号码携带查询服务。另有人对作者未遭法律追究表示惊讶，并建议可尝试 TRIP 等替代方案，认为漏洞因涉及军事基地才引起严肃对待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc5527">RFC 5527 - Combined User and Infrastructure ENUM in the e164.arpa Tree</a></li>
<li><a href="https://labs.ripe.net/author/hisham_ibrahim/operational-review-of-public-enum-under-e164arpa/">Operational Review of Public ENUM Under e164.arpa | RIPE Labs</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc6116">RFC 6116 - The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM)</a></li>
<li><a href="https://lina.sh/blog/hijacking-e164-arpa">I accidentally logged hundreds of thousands of phone calls to military bases - lina&#x27;s blog</a></li>

</ul>
</details>

**标签**: `#security`, `#telephony`, `#DNS`, `#vulnerability`, `#network infrastructure`

---

<a id="item-tech-news-2"></a>
### [Felony Bench：AI 代理重罪问责讨论](https://www.felonybench.com/) ⭐️ 7.0/10

Hacker News 上的“Felony Bench”条目讨论 AI 代理在无意中影响第三方时可能构成重罪的法律责任问题，并引用了 OpenAI 与 Hugging Face 的事件及 Greg Brockman 的公开回应。该项目被描述为统计“AI 代理无意中损害或影响第三方实体”的独特实例，但讨论中未提供该基准的更多实现细节或数据。评论者提出了一个具体场景：用户通过第三方托管运行 AI 代理执行合法任务，代理循环却产生违反《计算机欺诈与滥用法》（CFAA）的行为，可能的责任主体包括用户、第三方模型托管方、代理/工具软件开发者以及 LLM 模型开发者。讨论还涉及意图要件、护栏或沙箱是否排除刑事故意，以及计算机本身能否被追究刑事责任等争议。

hackernews · colinprince · 8月21日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49389430)

**「背景」** Felony Bench 是一个记录 AI 智能体对第三方实体造成影响事件的榜单，只有实际影响第三方才计数，仅逃逸沙箱不算。OpenAI 与 Hugging Face 事件被视为网络安全的分水岭，OpenAI 总裁 Greg Brockman 称该事件展示了自动化攻击的未来，并警告威胁行为者数月内将获得类似能力。这为讨论 AI 智能体在无意中违反《计算机欺诈与滥用法》等法律时用户、托管方和开发者各自责任提供了具体案例。

**「影响」** 对于开发、托管或使用 AI 代理的组织和个人，该讨论凸显出在现行刑法（如 CFAA）下，代理无意造成的第三方损害可能带来未明确的刑事风险，而目前尚无权威归责标准或先例。

**「社区讨论」** 评论区主要分歧在于归责主体和主观要件：一方列举用户、第三方宿主、代理软件开发者、LLM 开发者等多个可能对象，另一方强调“无意”加上防护措施使这些事件很难被认定为故意重罪，因此对 Felony Bench 的统计意义提出质疑。同时有评论抨击非暴力重罪被滥用，以及 OpenAI 对 Hugging Face 事件的处理态度令人不满。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.felonybench.com/">Felony Bench: Be AI, Do Crime</a></li>
<li><a href="https://openai.com/index/the-defenders-window/">The Defender’s Window | OpenAI</a></li>
<li><a href="https://stocktwits.com/news-articles/markets/equity/open-ai-s-greg-brockman-says-hugging-face-incident-was-a-window-into-automated-attacks-warns-threat-actors-will-have-these-capabilities-soon/cZYG5c0RJ1W">OpenAI’s Greg Brockman Says Hugging Face Incident Was A ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#agents`, `#law`, `#accountability`, `#OpenAI`

---

<a id="item-tech-news-3"></a>
### [美国公民边境删手机数据被控重罪](https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html) ⭐️ 7.0/10

美国公民 Samuel Tunick 因在美国边境删除手机数据而面临重罪指控。这一案件将边境电子设备检查与数据删除行为直接挂钩，意味着旅行者试图保护隐私的做法可能被控妨碍执法或销毁证据。该事件引发对旅客数字隐私与法律风险的广泛关注，但公开信息中尚未提供完整起诉细节、具体罪名或法院文件。

hackernews · floathub · 8月21日 12:10 · [社区讨论](https://news.ycombinator.com/item?id=49386895)

**「背景」** 在美国边境，海关执法人员有权对入境者的电子设备进行检查，并可能要求解锁设备；旅行者若拒绝或采取措施销毁数据，可能面临法律后果。据报道，Samuel Tunick 是一名亚特兰大居民，他使用的 Google Pixel 手机安装了注重隐私的 GrapheneOS 系统，该系统支持设置“胁迫密码”，触发后会删除设备上的所有数据和 eSIM。当 Tunick 于 1 月 24 日返回美国时，海关人员要求检查其手机，他使用了该功能清空数据，随后被联邦大陪审团以重罪起诉。

**「影响」** 对赴美旅客而言，在边检前或检查中擦除手机数据可能被联邦执法人员视为销毁证据并面临重罪指控；法律上尚存争议，但已引发对无搜查令获取手机内容的担忧。

**「社区讨论」** 部分评论认为美国边境执法已进入类似东德或苏联晚期的监控时代，公民权利难以实际保障；另有评论讨论技术对策，如使用手机镜像与恢复、自动化擦除、入境前将数据转移到加密备份，以减少敏感数据暴露或设备被扣押的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/07/activist-charged-with-felony-after-giving-border-agent-duress-code-that-wiped-his-phone/">Activist charged with felony after giving border agent... - Ars Technica</a></li>
<li><a href="https://www.nytimes.com/2026/07/28/us/duress-password-phone-wipe-charge.html">A U . S . Citizen Deleted His Phone ’s Data . Now He Faces a Felony ...</a></li>
<li><a href="https://truthout.org/articles/doj-charges-alleged-cop-city-activist-over-duress-password-that-wipes-phone/">DOJ Charges Alleged Cop City Activist Over “Duress”... | Truthout</a></li>
<li><a href="https://www.newsweek.com/cbp-phone-searches-us-citizens-rights-man-charged-device-wiping-12251645">CBP Phone Searches: US Citizens’ Rights as Man Charged Over Device Wiping - Newsweek</a></li>
<li><a href="https://www.nytimes.com/2026/08/21/us/politics/samuel-tunick-deleted-phone-felony.html">U.S. Citizen Who Deleted Phone’s Data Says His Prosecution Puts Privacy at Risk - The New York Times</a></li>

</ul>
</details>

**标签**: `#privacy`, `#digital-rights`, `#border-security`, `#surveillance`, `#legal`

---

<a id="item-tech-news-4"></a>
### [DeepSeek 推出实验性视觉模型 v4-flash-vision-exp](https://api-docs.deepseek.com/guides/vision/) ⭐️ 7.0/10

DeepSeek 已发布名为 DeepSeek-v4-flash-vision-exp 的实验性视觉模型 API 文档。该模型会按图像尺寸将图片转换为 token，并与文本 token 一起计费；推理前每张图片会被自动缩放，小于约 384×384 的图片按比例放大，较大图片按比例缩小到总像素约 800×800。社区测试显示其在读取 Playwright 截图等场景有前景，但在简单时钟读数上出错（回答 5:10，而 Qwen3.8 27B 几乎正确）。用户还指出 800×800 的归一化上限对整页 A4/Letter 文档的 OCR 可能不够。

hackernews · dares2573 · 8月21日 10:33 · [社区讨论](https://news.ycombinator.com/item?id=49386163)

**「背景」** 根据 DeepSeek 官方更新日志，DeepSeek-V4-Flash-Vision-Exp 是今天在 DeepSeek API 平台上线的多模态视觉理解模型。当前仅该视觉模型接受图像输入，其他 DeepSeek 模型会返回 400 错误（模型不支持图像）；同时发布的 DeepSeek Harness 0.1.1 提供了对该模型的开箱即用支持，便于在智能体框架中结合视觉理解和工具调用。

**「影响」** 对于需要整页文档 OCR 或精细视觉识别的开发者，800×800 的自动缩放上限可能降低精度，当前更适合截图等较小图像场景；模型仍为实验性，简单任务也可能出错。

**「社区讨论」** 社区反馈总体认为这是对早期 DeepSeek v4 Flash 0731 常假设具备视觉能力并编造工具问题的改进，尤其对 Playwright 截图读取寄予厚望；但多位用户报告了时钟读数错误、OCR 分辨率不足等限制，呈现早期实验版本混合表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://api-docs.deepseek.com/updates/">Change Log | DeepSeek API Docs</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260821/">DeepSeek-V4-Flash-Vision-Exp Release: Multimodal API Now Live | DeepSeek API Docs</a></li>
<li><a href="https://api-docs.deepseek.com/guides/vision/">Vision | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#vision-model`, `#multimodal`, `#api`, `#ai`

---

<a id="item-tech-news-5"></a>
### [开源模型是否正在追赶闭源模型？](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 7.0/10

这篇文章对开放模型与闭源模型在不同前沿模型代际中的能力进行了比较。分析涵盖多个前沿模型时代，旨在判断开源模型是否正在缩小差距。来源未提供具体模型名称、版本、日期或性能数据，因此无法给出确切的量化结论。该讨论对关注开放权重与专有模型竞争格局的 AI/ML 读者具有时效意义。

rss · Semianalysis · 8月21日 16:40

**「背景」** 开放权重模型（open-weight models）与闭源前沿模型（closed frontier models）的对比已成为评估 AI 进展的重要维度；前者允许用户下载权重并自行部署，后者通过 API 或受限访问提供服务。2025 年 1 月的 DeepSeek 发布标志着开源模型在部分能力上逼近闭源系统，而英国 AI 安全研究所 2026 年 8 月的分析也指出，领先开放权重模型在网络能力上正在缩小与前沿模型的差距。理解这一背景有助于解读 Semianalysis 对各代前沿模型的系统比较。

**「影响」** 开放权重模型已在性能上逼近闭源前沿模型且成本更低，但用户在实际使用中约 80%的情况仍选择闭源模型，说明开放模型的采用仍受阻碍。然而，性能差距缩小并未消除安全差距，安全仍是闭源模型的重要优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/are-open-models-catching-up">Are Open Models Catching Up?</a></li>
<li><a href="https://www.semafor.com/article/08/09/2026/open-weight-ai-models-are-catching-up-to-the-frontier-analysis-finds">Open-weight AI models are catching up to the frontier, analysis finds | Semafor</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/ai-open-models-have-benefits-so-why-arent-they-more-widely-used">AI open models have benefits. So why aren’t they more widely ...</a></li>
<li><a href="https://www.gptcrunch.com/blog/open-source-vs-closed-source-ai-models">Open Source vs Closed Source AI Models: A Comprehensive ...</a></li>
<li><a href="https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/">Open-weight AI models are catching up to the frontier. The ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#machine learning`, `#frontier models`, `#model comparison`

---

<a id="item-tech-news-6"></a>
### [9 模型实测：输出简洁可省钱，压缩输入提示更贵](https://www.reddit.com/r/MachineLearning/comments/1vulfei/does_telling_an_llm_to_be_concise_actually_save/) ⭐️ 7.0/10

一位 Reddit 用户分享的实证研究在 9 个模型（GPT-4o、GPT-5.4、Claude Haiku 4.5、Claude Sonnet 4.6、Qwen2.5-VL-7B、Qwen3.5-9B、DeepSeek-R1-Distill、Gemma-4-E4B、Kimi-K2.6）上，使用五个短答案数据集、11 种语言输出和长文本摘要任务，比较了压缩输入提示与压缩输出指令的效果。研究发现，要求模型输出更简洁平均可节省约 1.5 倍成本，最好情况下达 3 倍，且准确率基本不变；而压缩输入提示反而使成本最高增加 96%，模型会回答更长且准确率下降。作者指出输出 token 比输入 token 更贵，因此短单轮任务中减少输出 token 能省钱；当缩短后的输出正确时，约一半情况下文本不再与未约束时的推理一致。研究附有论文（编号 2606.24083v1）及代码数据链接。

reddit · r/MachineLearning · /u/ibubbles34 · 8月21日 16:38

**「背景」** LLM 的 API 费用通常按输入和输出 token 计费，且输出 token 通常更贵，因此控制输出长度可能直接影响成本。此前，关于“要求模型简洁”是否能真正省钱存在不同实践体会：有开发者记录简洁提示词可能导致多次重试反而增加费用，也有研究提出 concise-accuracy 指标来度量正确性与输出长度之间的权衡。

**「影响」** 通过 API 自行控制提示的用户，要求模型输出更简洁可在保持准确率的同时降低约 1.5 倍成本，而压缩输入提示则可能导致更高费用和更差回答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-04-01-token-efficiency-vs-quality-tradeoffs/">Does &#x27;Be Concise&#x27; Actually Save Tokens? The Hidden Quality ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0020025526008704">Concise thoughts: Impact of output length on LLM reasoning ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#prompt engineering`, `#cost optimization`, `#benchmarking`, `#machine learning`

---

<a id="item-tech-news-7"></a>
### [英伟达被曝筹划中国版 B30A 芯片，性能或高于 H20](https://www.theinformation.com/articles/nvidia-plots-china-comeback-new-ai-chip) ⭐️ 7.0/10

据 The Information 报道，英伟达正开发代号 B30A 的中国版 Blackwell AI 芯片，以满足美国对华出口限制，性能预计高于现有 H20，但低于旗舰 B300。该芯片采用单芯片设计并配备高带宽内存，样品最早可能于下月交付，最终规格和能否获批仍未确定。英伟达在周四发布声明，否认了《The Information》的报道。

telegram · zaihuapd · 8月21日 00:00

**「背景」** 背景：H20 是英伟达此前为应对美国对华出口限制而推出的 Hopper 架构中国特供芯片；B30A 据称基于更新的 Blackwell 架构，目标是在符合出口规则的前提下提供高于 H20 的性能。美国智库的分析认为，B30A 的性价比与旗舰 B300 相近，且中国目前没有国产芯片能与之对标。由于出口许可、最终规格尚不确定，且英伟达已否认相关报道，B30A 计划仍属未经证实的信息。

**「影响」** 若 B30A 落地，中国客户可能获得性能高于 H20 且符合出口限制的 Blackwell 芯片，但 NVIDIA 已否认该报道，最终规格和能否获批仍不确定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ifp.org/the-b30a-decision/">Should the US Sell Blackwell Chips to China? - IFP</a></li>
<li><a href="https://www.lovechip.com/blog/nvidia-s-rumored-b30a-for-china-what-it-is-why-it-matters-and-when-you-might-see-it">Nvidia&#x27;s Rumored B30A for China: What It Is, Why It Matters ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI hardware`, `#export controls`, `#China market`, `#Blackwell`

---

<a id="item-tech-news-8"></a>
### [Anthropic 拟调整企业数据留存政策 客户可存自有云端](https://www.reuters.com/business/anthropic-plans-change-enterprise-data-retention-policy-source-says-2026-08-20/) ⭐️ 7.0/10

据路透社报道，Anthropic 计划让企业客户在使用其先进 AI 模型时，将必须留存的 30 天数据存储到客户自己的云计算设施上，而不是仅由 Anthropic 保存。消息人士称，该政策调整已酝酿数月，Anthropic 正与包括 Salesforce 在内的 100 多家客户协作开发。企业仍需保留数据 30 天，但会获得更多存储位置控制权。Anthropic 预计今年晚些时候推出新的安全系统，以配合这一企业数据治理变化。

telegram · zaihuapd · 8月21日 02:40

**「背景」** Anthropic 是开发 Claude 系列大语言模型的公司，其企业级 API 服务此前要求客户在使用模型时留存相关数据 30 天，以便进行安全监控和滥用检测。此次拟调整的政策保留了 30 天留存要求，但允许企业将数据存放于自有云基础设施，而不是 Anthropic 端，从而回应企业在数据控制与合规方面的长期关切。

**「影响」** 该调整可使 Anthropic 企业客户在满足 30 天留存要求的同时，把数据放在自有云环境中，从而更直接地控制数据暴露面和合规边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/anthropic-plans-change-enterprise-data-retention-policy-source-says-2026-08-20/">Anthropic plans to change enterprise data retention policy ...</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/anthropic-plans-to-change-enterprise-data-retention-policy/articleshow/133391616.cms">Anthropic plans to change enterprise data retention policy</a></li>
<li><a href="https://www.itnews.com.au/news/anthropic-plans-to-change-enterprise-data-retention-policy-628315">Anthropic plans to change enterprise data retention policy</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#enterprise AI`, `#data privacy`, `#cloud computing`, `#AI policy`

---

<a id="item-tech-news-9"></a>
### [亚马逊购书扫描训练 AI 后销毁](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/) ⭐️ 7.0/10

404 Media 的调查发现，亚马逊正大规模购买实体书、扫描后用于 AI 训练，并在过程中销毁书籍。调查人员将追踪装置放入一本稀有书，最终追踪到位于内华达州拉斯维加斯的亚马逊仓库。该仓库员工称，他们接收大量印刷书籍后剪掉装订以加快扫描，书页随即被销毁。这一做法继 Anthropic 被曝类似行为后再次引发对 AI 训练数据来源和版权问题的关注。

telegram · zaihuapd · 8月21日 04:52

**「背景」** 在之前的 AI 训练数据争议中，Anthropic 等公司被指控未经许可使用受版权保护的书籍训练大型语言模型，引发作者与出版商对数据来源合法性的质疑。此次 404 Media 的调查使用 AirTag 追踪一批稀有书籍的流向，最终定位到亚马逊位于拉斯维加斯的仓库 LAS8 中的 VGT3 部门，该部门专门负责拆书、扫描书页以生成训练数据，并在扫描后销毁纸质书。

**「影响」** 该报道为出版商和作者提供了实体书被批量扫描用于 AI 训练且原件被销毁的具体证据，可能促使版权方对亚马逊的数据获取方式发起法律审查或追责。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/08/hidden-airtag-reveals-amazon-is-trashing-rare-books-to-train-ai/">Hidden Airtag reveals Amazon is trashing rare books to train AI</a></li>
<li><a href="https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/">We Tracked a Shipment of Rare Books. It Ended at an Amazon AI ...</a></li>
<li><a href="https://www.techtimes.com/articles/324871/20260818/amazon-destroys-rare-books-ai-training-despite-prior-denial-airtag-confirms.htm">Amazon Destroys Rare Books For AI Training Despite Prior ...</a></li>

</ul>
</details>

**标签**: `#AI training data`, `#Amazon`, `#copyright`, `#book scanning`, `#investigative journalism`

---

<a id="item-tech-news-10"></a>
### [OpenAI API 预览开放 GPT-Image-2 透明背景生成](https://x.com/OpenAIDevs/status/2090536933571330440) ⭐️ 7.0/10

OpenAI 在 API 中为 GPT-Image-2 推出透明背景生成功能的预览，允许用户生成背景透明的图像。该功能可生成放置在任意背景上的可复用素材，适用于产品图、平面设计、网站原型和营销活动。此次更新为开发者与设计师提供了更直接的透明背景图像产出方式，目前仍处于预览阶段。

telegram · zaihuapd · 8月21日 07:06

**「背景」** 透明背景指图像不带固定底色，通过 alpha 通道保留主体轮廓，便于将生成素材叠加到任意背景上，常用于产品图、设计稿和营销素材。GPT-Image-2 的 API 预览允许在请求中指定 background=&\#x27;transparent&\#x27; 直接输出透明 PNG，目前覆盖 GPT-Image-2 及 GPT-Image-2-2026-04-21 模型。但社区测试反馈交付的 alpha 通道可能需要归一化或裁剪，且在特定提示（如白色边框）下仍可能出现边缘光晕。

**「影响」** 使用 GPT-Image-2 API 的开发者与设计师可在预览阶段直接生成透明背景图片，用于产品图、平面设计、网站原型和营销活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://community.openai.com/t/transparent-backgrounds-are-now-available-in-preview-for-gpt-image-2-in-the-api/1391541">Transparent backgrounds are now available in preview for GPT ...</a></li>
<li><a href="https://explainx.ai/blog/openai-gpt-image-2-transparent-backgrounds-api-preview-august-2026">GPT-Image-2 Transparent PNGs via API (Preview, 2026 ...</a></li>
<li><a href="https://aicatchup.com/news/openai-gpt-image-2-transparent-backgrounds-preview">GPT-Image-2 API Preview Adds Transparent Backgrounds</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API`, `#image generation`, `#transparent background`, `#AI tools`

---

<a id="item-tech-news-11"></a>
### [特斯拉在华发起最大规模召回，逾 500 万辆车将推送软件修复](https://www.reuters.com/world/tesla-fix-software-millions-china-made-imported-evs-china-2026-08-21/) ⭐️ 7.0/10

特斯拉宣布在华发起其最大规模召回，涉及逾 500 万辆国产及进口车辆，主要通过 OTA 软件更新修复安全问题。自 9 月 25 日起召回 298 万辆国产及进口 Model 3、Model Y、Model S、Model X，原因是紧急车门释放把手难以识别，严重碰撞断电后可能妨碍逃生；修复包括增加警示标签和碰撞后降下车窗的 OTA 更新。此外，特斯拉还立即召回 274 万辆国产 Model 3、Model Y，通过 OTA 增强辅助转向等功能开启时的驾驶员注意力监测，以降低碰撞风险。两次召回合计约 572 万辆，均不涉及硬件更换，通过远程软件升级完成。

telegram · zaihuapd · 8月21日 11:23

**「背景」** 此次召回是 2026 年 8 月 21 日中国启动的有史以来最大规模汽车召回行动的一部分，共有 11 家汽车制造商参与。特斯拉的两项措施分别针对紧急车门释放把手难以识别和辅助转向等功能开启时驾驶员注意力监测不足；通过 OTA 软件更新，碰撞后自动降下车窗并增加警示标签，同时在现有方向盘扭矩检测基础上引入座舱摄像头监测。

**「影响」** 受影响特斯拉车主无需到店，车辆将通过 OTA 接收软件修复，以改善碰撞后逃生能力并增强驾驶员注意力监测，降低相关碰撞风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usatoday.com/story/cars/recalls/2026/08/21/tesla-china-car-recall-campaign/91401532007/">Tesla vehicles part of China&#x27;s biggest ever car recall campaign</a></li>
<li><a href="https://www.tesstudio.com/blogs/tesla-news/tesla-china-recalls-door-exit-driver-monitoring-2026">China Tesla Recalls: Door Exit and Driver Monitoring</a></li>
<li><a href="https://www.cnbc.com/2026/08/21/tesla-recalls-cars-in-china-over-doorhandle-safety-driver-monitoring.html">Tesla recalls cars in China over doorhandle safety, driver ...</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#recall`, `#OTA updates`, `#automotive software`, `#safety systems`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [IsoExec：统一执行消除 SkyRL 训练与推理不一致](https://vllm.ai/blog/2026-08-21-isoexec) ⭐️ 7.0/10

rss · vLLM Blog · 8月21日 00:00

**「背景」** 在策略强化学习假设 rollout 与训练评估同一策略，但实际 RL 系统常用独立的推理引擎（如 vLLM）和训练引擎（如 Megatron），它们的内核、批形状、并行布局与执行模式不同，浮点非结合性会使同一策略产生不同的 token 概率，导致新算法、环境和内核优化难以调试。

**「方案」** IsoExec 通过跨框架执行契约消除这种不一致：将前向算子划分为若干 region，为每个 \(region, case\) 固定实现及影响舍入的常量（如累加 dtype、归约分解参数），并用适配器在 vLLM 与 Megatron 中安装、校验和强制该契约。统一模型采用批不变的 GEMM、注意力、归一化和确定性 MoE，并让内核在张量、专家与序列并行下位级一致。针对 Gated DeltaNet，作者提出分块并行递归 CPR，使训练、预填充与解码共享一致的递归计算而不串行长序列：在 H100 上，训练前向+反向为原生的 1.43×，预填充 1.67×，解码 1.38×。在单节点 8×H100 上用 Qwen3.5-35B-A3B 跑 DAPO，作者称平均 logprob 绝对差降至某一阈值以下（正文未显示具体数值），完整 RL 步耗时增加 25.3%；但 50 步内未观察到奖励提升。

**「启示」** IsoExec 表明，通过显式执行契约与统一模型，可以在多引擎 RL 系统中以适中的端到端开销消除契约覆盖范围内的训练-推理数值不一致；CPR 则让线性注意力架构不必在数值一致性与长序列并行吞吐之间二选一。

**标签**: `#reinforcement learning infrastructure`, `#numerical reproducibility`, `#training-inference consistency`, `#kernel design`, `#Gated DeltaNet`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [广州中院裁定恒大地产集团破产清算，负债曾达 1.83 万亿元](https://weibo.com/1642585887/5334339212283916) ⭐️ 9.0/10

Guangzhou court accepted Evergrande Real Estate Group&\#x27;s bankruptcy liquidation, citing total liabilities of 1.83 trillion yuan and no restructuring value.

telegram · zaihuapd · 8月21日 05:35

**标签**: `#Evergrande`, `#bankruptcy liquidation`, `#China property`, `#debt crisis`, `#court ruling`

---

<a id="item-finance-news-2"></a>
### [三星电子宣布 2026 年股东回报目标为 90 万亿至 110 万亿韩元](https://www.cnbc.com/2026/08/21/samsung-shareholder-return-package-sk-hynix-buyback-ai-chip-boom.html) ⭐️ 8.0/10

三星电子周五宣布，预计 2026 年股东回报总额在 90 万亿至 110 万亿韩元（约 651 亿至 795.2 亿美元）之间，称这是韩国企业史上最大规模；此前数日，SK 海力士刚公布 40 万亿韩元股票回购计划。

rss · CNBC Finance · 8月21日 09:08

**「背景」** 该计划延续了三星 2024—2026 年股东回报安排：公司此前承诺返还该期间 50%的自由现金流，并维持每年 9.8 万亿韩元的常规股息。

**标签**: `#Samsung Electronics`, `#shareholder returns`, `#South Korea`, `#semiconductors`, `#AI chips`

---

<a id="item-finance-news-3"></a>
### [发改委发布对外投资管理办法修订征求意见稿 拟收紧资金出境](https://yyglxxbsgw.ndrc.gov.cn/htmls/article/article.html?articleId=2c97d16c-9ff00a63-01a0-230bacc4-0001) ⭐️ 8.0/10

国家发展改革委发布《对外投资管理办法（修订征求意见稿）》，拟取代 2017 年办法，收紧资金出境。草案规定未取得核准或备案的对外投资，外汇管理、海关等部门将不予办理相关手续，金融企业不予办理资金结算、融资、担保等业务，并要求境外再投资和返程投资在实施前 20 个工作日报告。

telegram · zaihuapd · 8月21日 13:05

**「背景」** 现行《企业境外投资管理办法》于 2017 年施行，新草案将安全审查范围扩展至存量资产转让和处分，并对违规办理资金结算的金融企业设置通报监管机制。

**「影响」** 若草案生效，有境外投资、境外再投资或返程投资计划的企业，以及为其办理资金结算、融资、担保的金融机构，将面临更严格的事前合规和联合惩戒要求。

**标签**: `#China`, `#outbound investment`, `#capital controls`, `#regulation`, `#NDRC`

---

<a id="item-finance-news-4"></a>
### [长江存储科创板 IPO 获受理，拟融资 330 亿元](https://api3.cls.cn/share/article/2461025?os=android&amp;amp;sv=8.8.2&amp;amp;app=cailianpress) ⭐️ 8.0/10

长江存储科创板 IPO 申请已获上交所受理，拟融资 330 亿元。

telegram · zaihuapd · 8月21日 14:26

**「背景」** 招股书披露，公司 2026 年 1-3 月营收 470.42 亿元、归母净利润 333.79 亿元；据 Counterpoint，其 2026 年第二季度按出货容量首次跻身全球 NAND 市场前三。

**标签**: `#IPO`, `#semiconductor`, `#STAR Market`, `#NAND`, `#Yangtze Memory`

---

<a id="item-finance-news-5"></a>
### [盘前异动：BJ&\#x27;s Wholesale、Ross Stores、加密股和 Broadcom 上涨](https://www.cnbc.com/2026/08/21/stocks-making-the-biggest-moves-premarket-bj-avg-coin-rost.html) ⭐️ 7.0/10

8 月 21 日盘前，零售、加密和半导体股上涨。BJ&\#x27;s 第二财季调整后每股收益 1.36 美元，高于 FactSet 预期的 1.17 美元，并将本财年每股收益指引从 4.40-4.60 美元上调至 4.60-4.80 美元；Ross Stores 第二财季业绩和第三财季指引超预期；加密相关股因比特币周涨幅有望超过 20%走高；报道称 Broadcom 拟筹资逾 600 亿美元债务以支持 Anthropic。

rss · CNBC Finance · 8月21日 12:27

**「背景」** 加密股上涨的背景是白宫会见加密行业领袖并敦促国会通过 Clarity Act，该法案涉及加密基础设施和联邦监管机构职责划分。

**标签**: `#premarket movers`, `#earnings`, `#cryptocurrency`, `#semiconductors`, `#retail`

---