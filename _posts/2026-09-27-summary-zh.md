---
layout: default
title: "Horizon Summary: 2026-09-27 (ZH)"
date: 2026-09-27
lang: zh
---

> 从 31 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [DeepSeek DSec 论文：160 个 EPYC 节点运行 38 万并发沙箱](#item-tech-news-1) ⭐️ 7.0/10
2. [英特尔 Panther Lake 拆解与 18A 工艺解析](#item-tech-news-2) ⭐️ 7.0/10
3. [美国上诉法院维持五角大楼对 Anthropic 黑名单](#item-tech-news-3) ⭐️ 7.0/10

**财经新闻**
1. [10 年期美债收益率升至 5.23%，创 2007 年以来新高](#item-finance-news-1) ⭐️ 8.0/10
2. [Anthropic 创始团队据称寻求 IPO 后保留投票控制权](#item-finance-news-2) ⭐️ 7.0/10
3. [苹果因 Apple Pay 向发卡机构收费面临反垄断集体诉讼](#item-finance-news-3) ⭐️ 7.0/10
4. [香港证监会与普华永道就恒大审计达成 10 亿港元和解](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DeepSeek DSec 论文：160 个 EPYC 节点运行 38 万并发沙箱](https://arxiv.org/abs/2609.22978) ⭐️ 7.0/10

DeepSeek 在 arXiv 上发布了 DSec（DeepSeek Elastic Compute）论文，描述了一套弹性计算系统，据称可在 160 个基于 AMD EPYC 的服务器节点上运行 380,000 个并发沙箱。该论文由 shenli3514 提交到 Hacker News，但提交内容未包含摘要细节。社区评论主要关注论文作者数量庞大，有评论称仅页面显示外的作者就有 31 人，总作者数达 131 人，并推测这是为了隐藏关键人才。技术上，如果数据属实，这意味着每个节点平均支持约 2,375 个并发沙箱，对 AI 基础设施和分布式沙箱隔离具有一定参考意义。

hackernews · shenli3514 · 9月26日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=49859112)

**「背景」** DeepSeek Elastic Compute \(DSec\) 是一个生产级沙箱平台，为代理式训练（agentic training）提供隔离执行环境，并暴露 FnCall、容器、microVM 和 full-VM 等多种后端。代理式训练需要模型在受控环境中执行代码、调用工具并与外部系统交互，因此沙箱必须支持从轻量级函数调用到完整虚拟机的不同隔离级别。该论文（arXiv:2609.22978）系统性介绍了这一基础设施的设计与规模化能力。

**「社区讨论」** 评论大多聚焦于论文异常庞大的作者名单，而非技术细节；有人猜测这是资产保护策略，避免竞争对手挖走关键员工。也有评论担心，若 380,000 个并发沙箱用于训练，类似规模代理集群可能被用于大规模网络攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.22978v1">A Sandbox Infrastructure for Effective Agentic Training at Scale - arXiv</a></li>
<li><a href="https://www.alphaxiv.org/abs/2609.22978">DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#distributed systems`, `#sandboxing`, `#AI infrastructure`, `#server architecture`

---

<a id="item-tech-news-2"></a>
### [英特尔 Panther Lake 拆解与 18A 工艺解析](https://newsletter.semianalysis.com/p/intel-panther-lake-teardown) ⭐️ 7.0/10

SemiAnalysis 发布了一篇免费的 STEEL 拆解报告，作者为 Adith Shankar，主题是英特尔 Panther Lake 处理器和 18A 工艺技术。该拆解对芯片内部结构和制造工艺进行了近距离观察。报告面向对计算机系统和半导体感兴趣的读者，提供了详细的硬件层面信息。虽然这不是一项颠覆性突破，但对于芯片设计和技术分析仍具有较高参考价值。

rss · Semianalysis · 9月26日 13:36

**「背景」** 英特尔正式发布的 Panther Lake 是 Core Ultra 系列的最新一代处理器，也是该公司首款基于 18A 制程的产品。18A 是英特尔先进半导体工艺节点，据称带来重新设计的晶体管架构和新的供电方式，并用于即将推出的 Panther Lake SoC。此前有非官方消息称 18A 工艺性能出色，但官方细节仍有限。

**「影响」** 由于该拆解报告免费公开，半导体工程师和硬件爱好者无需订阅即可获得 Panther Lake 与 18A 的详细硬件分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/odrimedia_intel-unveils-panther-lake-processor-built-activity-7382338884468097024-bvkF">Intel introduces Panther Lake processor, built on 18 A process .</a></li>
<li><a href="https://wccftech.com/intels-18a-process-shows-great-performance-as-panther-lake-socs-are-finally-up/">Intel &#x27;s 18 A Process Shows &quot;Great Performance&quot; As Initial Panther ....</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/01/49713751/lip-bu-tan-says-they-over-delivered-on-18a-timeline-as-intel-shows-off-next-gen-panther-lake-ai-laptop-chips-at-ces-2026">Lip-Bu Tan Says They &#x27;Over-Delivered&#x27; On 18 A Timeline As Intel ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#semiconductors`, `#Intel`, `#chip design`, `#teardown`

---

<a id="item-tech-news-3"></a>
### [美国上诉法院维持五角大楼对 Anthropic 黑名单](https://www.reuters.com/world/us-appeals-court-declines-block-pentagons-blacklisting-anthropic-2026-09-25/) ⭐️ 7.0/10

9 月 25 日，美国华盛顿特区联邦上诉法院以 2 比 1 的裁决，维持五角大楼将 Anthropic 列为国家安全供应链风险并禁止其参与军事合同。多数法官认为，由于 Anthropic 拒绝允许其产品用于自主武器和大规模监控，五角大楼的担忧是合理的。Anthropic 表示不同意该裁决，并正在考虑请求全体上诉法院复审。此前，旧金山一名联邦法官曾依据另一部法律推翻相关列名，并阻止政府对 Anthropic 实施更广泛禁令。

telegram · zaihuapd · 9月26日 05:19

**「背景」** 五角大楼可通过将企业列入国家安全供应链风险清单来限制其参与军事采购。Anthropic 是一家人工智能公司，其可接受使用政策禁止客户将模型用于自主武器和大规模监控等用途，这使其在国防领域与部分军事应用要求发生冲突。

**「影响」** 该裁决使 Anthropic 在诉讼期间仍被禁止参与五角大楼军事合同，其国家安全供应链风险列名继续有效；除非全体上诉法院复审或更高级法院介入，否则这一限制仍将维持。

**标签**: `#Anthropic`, `#AI policy`, `#defense contracts`, `#AI safety`, `#legal`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [10 年期美债收益率升至 5.23%，创 2007 年以来新高](https://www.cnbc.com/2026/09/26/10-year-treasury-yield-is-at-its-highest-in-19-years-how-we-got-here.html) ⭐️ 8.0/10

10 年期美国国债收益率周五升至 5.23%，为 2007 年以来最高。CME FedWatch 显示市场对美联储 10 月加息的概率为 64%；密歇根大学消费者信心指数显示 9 月一年期通胀预期升至 4.6%。

rss · CNBC Finance · 9月26日 13:30

**「背景」** 债券收益率与价格反向变动；本轮上行既受到通胀持续高企和美联储加息预期推动，也来自政府赤字融资及 AI 基础设施相关公司大量发债带来的债券供给压力。

**「影响」** 该收益率影响抵押贷款成本，并可能通过推高企业借贷成本、提高债券相对吸引力而给股市带来压力。

**标签**: `#Treasury yields`, `#Federal Reserve`, `#inflation`, `#bond market`, `#AI investment`

---

<a id="item-finance-news-2"></a>
### [Anthropic 创始团队据称寻求 IPO 后保留投票控制权](https://techcrunch.com/2026/09/25/anthropics-founders-seek-voting-control-ahead-of-ipo/) ⭐️ 7.0/10

据 TechCrunch/The Information 报道，Anthropic 正要求股东批准一项特殊股权结构，使 CEO Dario Amodei 与六名联合创始人在满足持股条件时，合计拥有公司大多数事务 50.1%的投票权；该方案尚待股东批准，报道未显示 Anthropic 已完成 IPO。

telegram · zaihuapd · 9月26日 02:22

**「背景」** Anthropic 目前尚未完成 IPO；七位联合创始人各自持股约 2%，拟议的特殊股权结构将投票权与经济权益分离，但不附带额外经济权益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/anthropic-founders-voting-control-ipo">Anthropic seeks 50.1% voting control for founders , The...</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#corporate governance`, `#voting rights`, `#AI`

---

<a id="item-finance-news-3"></a>
### [苹果因 Apple Pay 向发卡机构收费面临反垄断集体诉讼](https://9to5mac.com/2026/09/25/apple-faces-class-action-over-apple-pay-fees-charged-to-card-issuers/) ⭐️ 7.0/10

美国一名联邦法官批准了一项针对苹果的反垄断集体诉讼。原告指控苹果就 Apple Pay 交易向发卡机构收取信用卡 0.15%、借记卡 0.5 美分的费用，每年最高 10 亿美元，并寻求退款及禁令。

telegram · zaihuapd · 9月26日 03:32

**「背景」** 原告称，安卓手机钱包不向发卡机构收取此类费用，并将此作为苹果收费过高的对比基准。

**标签**: `#Apple`, `#Apple Pay`, `#antitrust`, `#class action`, `#card issuers`

---

<a id="item-finance-news-4"></a>
### [香港证监会与普华永道就恒大审计达成 10 亿港元和解](https://wallstreetcn.com/articles/3782573) ⭐️ 7.0/10

香港证监会与普华永道香港就恒大审计失职达成 10 亿港元和解，普华永道不承认责任，但同意支付该款项补偿受影响的独立小股东。

telegram · zaihuapd · 9月26日 07:18

**「背景」** 审计机构负责核查上市公司财务报表是否真实；此次和解源于香港证监会指中国恒大财务报表存在虚假问题，并对审计机构普华永道香港的调查。

**「影响」** 该和解尚待香港高院判决，恒大清盘人已入禀要求撤销，因此小股东能否获得补偿仍有不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/zh/p/3780065714148610">8点1氪： 华 谊兄弟被申请破产重整， 普 华 永 道 因 恒 大 审 计 赔偿 10 ...</a></li>
<li><a href="https://stcn.com/article/detail/3790468.html">涉 恒 大 虚假财报！ 普 华 永 道 ，赔偿 10 亿 港 元 ！ 最新回应来了</a></li>

</ul>
</details>

**标签**: `#Hong Kong SFC`, `#PwC`, `#Evergrande`, `#audit failure`, `#settlement`

---