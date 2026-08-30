---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 26 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [腾讯发布并开源 Hy4 预览版模型](#item-tech-news-1) ⭐️ 8.0/10
2. [韩国选定联合体，预计年内提供全民免费韩国自研 AI 模型](#item-tech-news-2) ⭐️ 8.0/10
3. [索尼音乐等诉 Anthropic 盗用歌词训练 Claude](#item-tech-news-3) ⭐️ 8.0/10
4. [美国土安全部借冷门法律获取记者与组织记录](#item-tech-news-4) ⭐️ 7.0/10
5. [三星 Hot Chips 2026 内存内处理设计分析](#item-tech-news-5) ⭐️ 7.0/10
6. [百年 SPC 算法击败 SOTA 时序异常检测](#item-tech-news-6) ⭐️ 7.0/10
7. [长鑫存储诉美国防部求移出黑名单](#item-tech-news-7) ⭐️ 7.0/10

**财经新闻**
1. [美上诉法院裁定体育事件合约属体育博彩，预测市场或上诉至最高法院](#item-finance-news-1) ⭐️ 7.0/10
2. [四部门开展机动车质量专项行动，突击检查“速成车”](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [腾讯发布并开源 Hy4 预览版模型](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

腾讯发布了 Hy4 预览版并开源该模型。该模型在 OpenRouter 上迅速获得大量使用，几天内处理了数万亿 token，超过了 GLM 5.3 一周的用量；其缓存成本仅为 5%，低于常见的 10% 或 20%。腾讯称 Hy4 preview 首次参与自身开发过程，在训练方法、数据策略、评估框架和底层算子方面进行自动优化，提出方案、运行实验并根据结果迭代，形成早期递归自我改进循环。这些特性使其在 AI/ML 社区中引起关注，但也有人对发布图表中的基准展示方式提出批评。

hackernews · shenli3514 · 8月29日 19:33 · [社区讨论](https://news.ycombinator.com/item?id=49492632)

**「背景」** Tencent Hy4 preview 是腾讯发布并开源的大语言模型。它采用 MoE 架构，总参数 770B、激活参数 49B，上下文窗口超过 100 万 token，以 Apache 2.0 许可证发布。该模型可通过腾讯云、OpenRouter 及公开仓库获取。

**「对开发者的影响」** 开发者现在可以以每百万输入 token 0.834 美元、每百万输出 token 2.501 美元的价格，使用一个拥有 770B 总参数（49B 活跃）和 1M token 上下文的 MoE 模型，且权重以 Apache 2.0 开源，这使长上下文处理成本异常低廉，并可能加剧开放权重模型的价格竞争。

**「社区讨论」** 社区评论指出 Hy4 在 OpenRouter 上的采用速度惊人，且低价缓存策略可能提升其吸引力；也有用户批评发布材料中的基准图表存在刻意突出自身模型的“图表犯罪”。另有开发者提到前代 Hy3 在通用代理任务中表现接近 DeepSeek，但尚不确定其编码能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/">Tencent Releases and Open - Sources Tencent Hy 4 preview - Tencent</a></li>
<li><a href="https://www.testingcatalog.com/tencent-released-open-source-hy4-preview-model/">Tencent releases open - source Hy 4 preview model</a></li>
<li><a href="https://www.brocker.org/tencent-hy4-preview-open-source-770b-parameters-1m-context">Tencent open - sources Hy 4 preview 770B MoE model</a></li>
<li><a href="https://openrouter.ai/tencent/hy4-preview">Hy4 preview - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://explainx.ai/blog/tencent-hy4-preview-770b-moe-1m-context-august-2026">Hy4 Preview: 770B Open Weights at $0.83/M Input | explainx.ai Blog | explainx.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#LLM`, `#open source`, `#Tencent`

---

<a id="item-tech-news-2"></a>
### [韩国选定联合体，预计年内提供全民免费韩国自研 AI 模型](https://www.koreatimes.co.kr/business/tech-science/20260828/skt-kt-kakao-consortiums-selected-for-free-ai-service-for-public) ⭐️ 8.0/10

韩国科学技术信息通信部已选定由 SK Telecom、KT 和 Kakao 牵头的三个联合体，负责运营“AI for All”项目，向全体国民提供无 token 限制的免费 AI 服务。该服务采用韩国自研大模型，将于 9 月启动内测，并在年底前正式上线。政府将向三个联合体提供 512 块英伟达 B200 芯片，并从 2027 年起补贴全国运营成本。该服务可接入政府系统，用于预约就诊、找房和税务咨询。Naver 未参与该项目。

telegram · zaihuapd · 8月29日 15:31

**「背景」** 韩国政府将人工智能作为国家战略基础设施，并由科学技术信息通信部主导“AI for All”等公共 AI 项目。SK Telecom、KT 和 Kakao 分别是韩国主要电信运营商和互联网平台企业，此次各自牵头联合体参与该国家级 AI 服务建设。

**「影响」** 预计年底起，韩国全体国民可免费且无 token 限制使用国产大模型，并能通过政府系统入口处理预约就诊、找房和税务咨询等事务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.telecompaper.com/news/skt-kt-kakao-consortia-selected-for-national-ai-for-all-project-in-korea--1581062">SKT , KT , Kakao consortia selected for national &#x27; AI ... - Telecompaper</a></li>
<li><a href="https://www.ajupress.com/view/20260828104218642">Korea picks SKT , Kakao , KT for nationwide AI service ... | Aju Press</a></li>

</ul>
</details>

**标签**: `#South Korea`, `#AI policy`, `#domestic LLMs`, `#Nvidia B200`, `#free AI service`

---

<a id="item-tech-news-3"></a>
### [索尼音乐等诉 Anthropic 盗用歌词训练 Claude](https://www.musicbusinessworldwide.com/files/2026/08/COMPLAINT-in-Sony_Music_Publishing_US_LLC_e.pdf) ⭐️ 8.0/10

索尼音乐出版、华纳查佩尔音乐等公司向美国加州联邦法院起诉 Anthropic 及其创始人，指控其为训练 Claude 模型非法下载大量盗版书籍并抓取歌词。起诉书称，Anthropic 从 LibGen、PiLiMi 等盗版库下载了逾 700 万本书，并删除歌词的版权管理信息。原告寻求每件作品最高 15 万美元的法定赔偿和永久禁令。此前同类诉讼已促成 15 亿美元和解。

telegram · zaihuapd · 8月30日 01:00

**「背景」** LibGen、PiLiMi 等是常被用于大规模语言模型训练的盗版电子书和文本库，本次诉讼指控 Anthropic 从中下载逾 700 万本书并抓取歌词，同时删除版权管理信息。工具结果还显示，原告列举了《Ain&\#x27;t No Mountain High Enough》等具体歌曲，并要求对每首被侵权作品最高 15 万美元的法定赔偿。在此之前，音乐出版商已通过同类诉讼获得过 15 亿美元和解，凸显此类案件的高风险。

**「影响」** 若法院支持原告请求，Anthropic 可能需按每件作品最高 15 万美元支付赔偿并面临永久禁令，这将直接影响 Claude 模型的训练数据使用和后续运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.musicbusinessworldwide.com/now-sony-music-publishing-and-warner-chappell-sue-anthropic-in-multi-billion-dollar-lawsuit-one-of-the-largest-and-most-blatant-ongoing-thefts-of-intellectual-property-in-history/">Sony Music Publishing and Warner Chappell sue Anthropic in multi-billion dollar lawsuit</a></li>
<li><a href="https://www.businessinsider.com/anthropic-claude-training-copyright-music-lyrics-sony-lawsuit-2026-8">Sony accuses Anthropic of &#x27;brazen campaign&#x27; to train Claude on its music — and wants up to $150,000 a song</a></li>

</ul>
</details>

**标签**: `#copyright`, `#AI training data`, `#Anthropic`, `#music industry`, `#legal`

---

<a id="item-tech-news-4"></a>
### [美国土安全部借冷门法律获取记者与组织记录](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits) ⭐️ 7.0/10

美国国土安全部（DHS）正在利用一项冷门的“1509 传票”程序获取记者、非营利组织和工会的通话及短信记录，被指绕过法院的独立审查。多个案件中，DHS 在传票被诉至法院、法官尚未裁决合法性之前撤回，被质疑为规避司法裁定。报道称 T-Mobile 已向 DHS 交出一名记者 Fort 六个月、超过 1 万条通话和短信记录，且直到政府律师向 Fort 律师出示记录时她才得知；Google 则未配合。此做法引发科技公司在隐私保护与政府合规之间的压力。

hackernews · firefax · 8月29日 18:44 · [社区讨论](https://news.ycombinator.com/item?id=49492219)

**「背景：19 U.S.C. § 1509 与国土安全部传票」** 19 U.S.C. § 1509 是一项海关执法相关法律，允许美国国土安全部（DHS）在无事先司法审查的情况下签发行政传票，要求提供记录；该条款传统上用于进出口审计，但近期报道显示它被用来秘密获取记者、工会和非营利组织的通话与财务记录。收到此类传票的企业并不必须自动遵从，DHS 若需强制执行必须诉诸法院，而部分公司（如 T-Mobile）曾配合提供记录，Google 则未予配合。

**「影响」** 记者、非营利组织和工会等目标群体现面临电信运营商依据 1509 传票直接提交通信记录的实际风险，且部分公司如 T-Mobile 已配合，而 Google 拒绝，显示企业在是否挑战政府要求上不一致，增加了隐私保护的不确定性。

**「讨论」** 多数评论认为 DHS 在裁决前撤案是为避免司法审查，并批评 T-Mobile 配合而 Google 拒绝，强调公司可先不遵守、等待法院强制执行；也有观点以第四修正案为由反对必须由法官预先批准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits">Trump’s DHS is using an obscure law to secretly snoop on journalists, non-profits and unions: ‘It’s outrageous’ | Trump administration | The Guardian</a></li>
<li><a href="https://aaronparnas.substack.com/p/saturday-update-impeachment-calls">Saturday Update: Impeachment Calls, DHS Spies on Journalists, Cherry Trees Cut Down, McConnell Update, Major CSAM Ruling</a></li>
<li><a href="https://news.ycombinator.com/item?id=49492219">DHS is using obscure law to snoop on journalists, non-profits, unions | Hacker News</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#tech-policy`, `#telecom`, `#legal`

---

<a id="item-tech-news-5"></a>
### [三星 Hot Chips 2026 内存内处理设计分析](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing) ⭐️ 7.0/10

半导体分析网站 Chips and Cheese 针对三星在 Hot Chips 2026 上展示的内存内处理（PIM）设计发表了技术分析，讨论其在 AI 工作负载中的潜力与限制。该设计将计算单元置于内存中，试图减少数据搬运，但分析指出其适用性可能局限于 AI、游戏和加密等少数负载，而不是通用计算。社区评论提到类似概念早在 1980 年就已出现，三星在 2020 或 2021 年也展示过相近方案，因此这并非全新范式；具体实现中矩阵乘法仍需要大量数据移动，能量和硅面积开销主要来自移动而非乘加运算。分析认为该方向对 AI 硬件有一定价值，但能否从众多展会原型中走向实际产品仍不确定。

hackernews · ingve · 8月29日 06:06 · [社区讨论](https://news.ycombinator.com/item?id=49487341)

**「背景」** 在 Hot Chips 2026 上，三星展示了基于 LPDDR5X DRAM 的处理内存（PIM）方案 LPDDR5X-PIM，将乘加（MAC）单元直接集成到内存芯片中，同时保持与标准内存控制器的接口兼容性。该设计旨在减少 AI 推理等数据密集型工作负载中的数据移动开销，从而提升带宽和能效；根据三星的数据，其在 AI 推理场景下比普通 LPDDR5X 快 3.01 倍，并提供 8 倍带宽。处理内存的基本思路是将计算移到数据附近，以缓解传统冯·诺依曼架构中处理器与内存之间的数据传输瓶颈。

**「影响与局限」** 对于 AI/LLM 推理工作负载，内存带宽已成为主要瓶颈，三星 PIM 设计及其商用 HBM4 试图将计算靠近内存以减少数据搬运，但现有证据仅表明硬件已出货，尚未证明其能在通用矩阵乘法等任务上普遍加速，开发者仍需针对数据局部性和特定工作负载做联合优化。

**「社区讨论」** 评论区普遍认可内存内处理是未来方向，但对三星当前实现能否落地存在怀疑。多位评论者指出，此类架构要求精确控制数据位置，开发约束极大，类似概念已多次出现在学术和展会中但鲜有产品落地；也有评论认为矩阵乘法的数据移动开销仍是主要瓶颈，需要环形移位寄存器等额外机制。总体共识是这一方向适合 AI 等特定负载，但通用性不足，可能需要彻底改变计算机架构才可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing">Hot Chips 2026: Samsung&#x27;s Processing-in-Memory (PIM)</a></li>
<li><a href="https://www.servethehome.com/samsung-lpddr5x-pim-at-hot-chips-2026/">Samsung LPDDR5X-PIM at Hot Chips 2026 - ServeTheHome</a></li>
<li><a href="https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth">Hot Chips 2026: Samsung makes LPDDR5X smart with logic unit in memory ...</a></li>
<li><a href="https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing">Samsung Ships Industry-First Commercial HBM4 With Ultimate...</a></li>
<li><a href="https://winbuzzer.com/2026/01/26/memory-bottleneck-llm-inference-hardware-challenge-xcxwbn/">AI : Memory Bottleneck Emerges as Main LLM Inference Challenge</a></li>
<li><a href="https://arxiv.org/html/2603.03880">Joint Hardware - Workload Co-Optimization for In - Memory Computing...</a></li>

</ul>
</details>

**标签**: `#processing-in-memory`, `#Samsung`, `#AI hardware`, `#computer architecture`, `#Hot Chips`

---

<a id="item-tech-news-6"></a>
### [百年 SPC 算法击败 SOTA 时序异常检测](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 7.0/10

Reddit 用户 eamonnkeogh 指出，时间序列异常检测领域常用的 Paparrizos 的 TSB-AD-M 基准过于简单：他使用有百年历史的统计过程控制（SPC）算法，在多数基准数据集上击败了当前最先进的 TSAD 方法，在给出的心电图（ECG）示例中 SPC 甚至获得完美结果。他还提到许多标记为“TAO”的轨迹更加容易用 SPC 解决，并强调自己并不声称这些论文提出的算法本身有问题，而是认为该基准无法支撑有意义结论。他认为社区需要反思，过去十年的大部分进展可能是幻觉。作者表示自己虽未解决平凡性问题，但已完成 90%的工作引入更具挑战性的 TSAD 问题，如雪橇犬、金枪鱼、燃料电池和智能制造等。

reddit · r/MachineLearning · /u/eamonnkeogh · 8月29日 20:16

**「相关背景：TSB-AD 基准与统计过程控制」** TSB-AD 是 Paparrizos 等人提出的时间序列异常检测基准套件（含单变量 TSB-UAD 等变体），常用于 NeurIPS、SIGKDD、VLDB 等论文中的评估。该基准旨在提供端到端评估，并修正早期数据集中的缺陷。统计过程控制（SPC）是约百年前发展起来的质量控制方法，通过控制图监控过程均值和变异来识别异常。

**「对基准可信度的影响」** 由于 TSB-AD-M 基准被批评为过于简单、用百年前的统计过程控制即可在多数数据集上超越现有 SOTA 方法，因此依赖该基准发表的领先异常检测结果可能高估了模型能力，研究者应谨慎解读相关排行榜（如 tool-2-2 中的性能数据），并考虑采用作者提出的更难替代数据集进行验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vldb.org/pvldb/vol15/p1697-paparrizos.pdf">TSB -UAD: An End-to-End Benchmark Suite for Univariate</a></li>
<li><a href="https://github.com/TheDatumOrg/TSB-AD">GitHub - thedatumorg/ TSB - AD : Time - Series Anomaly Detection</a></li>
<li><a href="https://arxiv.org/pdf/2602.01359">PaAno: Patch-Based Representation Learning for Time - Series ...</a></li>
<li><a href="https://www.sota2.com/research/sota/time-series-anomaly-detection-on-tsb-ad-m">Time Series Anomaly Detection on TSB-AD-M benchmark leaderboard</a></li>

</ul>
</details>

**标签**: `#time series`, `#anomaly detection`, `#benchmarking`, `#machine learning`, `#statistical process control`

---

<a id="item-tech-news-7"></a>
### [长鑫存储诉美国防部求移出黑名单](https://www.bloomberg.com/news/articles/2026-08-29/chinese-chipmaker-cxmt-sues-pentagon-to-get-off-us-blacklist) ⭐️ 7.0/10

长鑫存储（CXMT）已向美国哥伦比亚特区联邦地方法院提起诉讼，要求美国国防部将其移出所谓与中国军方有关联的黑名单，并将国防部长赫格塞思列为被告之一。该公司称其 DRAM 芯片仅用于民用和商用，并非军事用途，自 2025 年 1 月被列入名单以来持续遭受声誉和商业损害。长鑫存储目前是全球第四大 DRAM 厂商，市值已超过腾讯成为中国最大公司。公司同时表示，此次被列入黑名单不会影响日常运营。

telegram · zaihuapd · 8月29日 05:43

**「背景」** 该黑名单指五角大楼维护的“中国军方公司”清单，长鑫存储于 2025 年 1 月被首次列入。五角大楼在拜登政府时期作出列名决定，特朗普政府在 2025 年 6 月的更新中保留了该列名。据诉状，长鑫存储已花费一年多时间向五角大楼提交信息以质疑决定，并称相关决定缺乏事实记录、适用法律或合理决策依据。

**「影响」** 对长鑫存储而言，此次列入黑名单已造成声誉和商业损害，但公司表示不会影响日常运营；诉讼结果将决定其能否被移出黑名单并减轻相关损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.cn/2026-08-29/detail-inipymqr3700531.d.html?vt=4&amp;pos=108">长鑫存储起诉五角大楼，赫格塞斯也被列为被告|美国国防部|彭博社|中国|芯片|黑名单_手机新浪网</a></li>
<li><a href="https://finance.ifeng.com/c/8vz5ghKcjD2">长鑫存储起诉美国国防部_凤凰网</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#US-China tech policy`, `#legal`, `#hardware`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美上诉法院裁定体育事件合约属体育博彩，预测市场或上诉至最高法院](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

美国第九巡回上诉法院驳回 Kalshi、Crypto.com 和 Robinhood 的禁令请求，认定体育相关事件合约属于体育博彩，而非受美国商品期货交易委员会（CFTC）监管的掉期（一种衍生品）。该裁决与第三巡回上诉法院 4 月的相反判决形成分歧，可能提交最高法院。

rss · CNBC Finance · 8月29日 02:23

**「背景」** 今年 4 月，第三巡回上诉法院曾裁定只有 CFTC 有权监管体育相关事件合约；CFTC 主张所有事件合约（不论标的内容）均属其专属管辖的掉期。

**标签**: `#prediction markets`, `#CFTC`, `#sports betting`, `#regulation`, `#Supreme Court`

---

<a id="item-finance-news-2"></a>
### [四部门开展机动车质量专项行动，突击检查“速成车”](https://weibo.com/1893892941/5336817496754349) ⭐️ 7.0/10

据北京日报报道，工信部等四部门于 2026 年 8 月 27 日启动为期一年的道路机动车辆生产一致性和质量提升专项行动，检查覆盖六类机动车生产企业、产品及检验检测机构。违规企业可能面临通报、暂停产品公告及认证、停止登记或罚款。

telegram · zaihuapd · 8月29日 13:30

**「背景」** 此前，工信部已于 2026 年 7 月 17 日表示将深入开展道路机动车辆产品生产一致性和质量提升行动，为此次四部门联合专项行动提供了先期部署背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://jjckb.xinhuanet.com/20260717/6f074de6236e4feeb51ccda9c8942923/c.html">jjckb.xinhuanet.com/20260717/6f074de6236e4feeb51ccda9c8942923...</a></li>

</ul>
</details>

**标签**: `#China auto regulation`, `#vehicle quality enforcement`, `#automotive industry`, `#regulatory policy`

---