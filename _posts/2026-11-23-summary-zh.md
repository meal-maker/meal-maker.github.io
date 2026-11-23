---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> 从 27 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [OpenAI：困惑度与智能呈明确相关趋势](#item-tech-news-1) ⭐️ 8.0/10
2. [英媒：太子集团涉案人员被指参与对华芯片走私](#item-tech-news-2) ⭐️ 8.0/10
3. [硅谷发生了什么？](#item-tech-news-3) ⭐️ 7.0/10

**财经新闻**
1. [美股科技股暴跌后亚洲多地出台稳定市场措施](#item-finance-news-1) ⭐️ 9.0/10
2. [蚂蚁集团领投 Simplexity Robotics 1 亿美元 pre-A 轮，估值 16 亿美元](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI：困惑度与智能呈明确相关趋势](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 8.0/10

OpenAI 发布文章《Perplexity and Intelligence》，探讨语言模型困惑度与智能之间的相关性。文章展示了一条清晰趋势：在预训练模型中，困惑度越低，模型在智能相关任务上的表现往往越高。作者认为预测误差（以困惑度衡量）可以作为一个简单而有用的基准，用于追踪语言模型的智能进展。这一观点被提出用于替代日益复杂且难以横向比较的评估方法。

hackernews · acossta · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**「背景」** 困惑度（perplexity）衡量语言模型在预测下一 token 时的意外程度，是交叉熵损失的指数形式；值越低表示模型对序列的预测越准确。TechCrunch 于 2026 年 11 月 22 日报道，OpenAI 首席科学家 Jakub Pachocki 在博客文章中提出，预训练交叉熵（以困惑度或对数困惑度评估）是衡量模型底层智能的稳定指标，并认为在特定对数困惑度阈值下才能稳定激发某些能力。该文章还引发了关于是否应通过困惑度来限制 AI 发展的讨论，并呼应了预测/压缩与智能之间关系的长期争论。

**「社区讨论」** 评论区普遍认可该趋势清晰且简单实用，并补充了困惑度定义：最差情况下等于词表大小，最好为 1。也有用户对 GPT-4.5 与推理模型的关系提出疑问，并称微软已在同一评测集上报告 MAI-2 Base 的对数困惑度为 0.819。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence - OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/">OpenAI ’s chief scientist has thoughts on how to limit AI ...</a></li>
<li><a href="https://community.openai.com/t/perplexity-and-intelligence/1419510">Perplexity and Intelligence - Community - OpenAI Developer ...</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#language models`, `#benchmarking`, `#openai`

---

<a id="item-tech-news-2"></a>
### [英媒：太子集团涉案人员被指参与对华芯片走私](https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1) ⭐️ 8.0/10

英国《金融时报》调查称，一个走私网络涉嫌经马来西亚将英伟达芯片转运至中国，被美国财政部指为柬埔寨太子集团“二号人物”的胡小伟被指参与其中。报道援引贸易数据称，2024 年 12 月至 2025 年 12 月，Megaspeed 马来西亚子公司申报进口货物价值约 46 亿美元，部分芯片据称流入中国黑市。该集团还被指控制涉及空壳公司和地下融资的渠道，并利用私人飞机走私货物。太子集团否认胡小伟曾为其工作，并称有关非法网络和私人飞机走私的指控缺乏事实依据。

telegram · zaihuapd · 11月22日 04:34

**「背景」** 美国近年来对华实施先进 AI 芯片出口管制，限制英伟达高性能 GPU 对华销售，导致经由东南亚等地中转的灰色供应链受到关注。此前已有公开讨论质疑新加坡云服务商 Megaspeed 是否将英伟达芯片改道运往中国，并讨论美国是否应予以处罚；另有报道称有人以能取得英伟达 GPU 为条件为东南亚数据中心项目融资，反映出管制下这些芯片的稀缺与需求。

**「影响」** 该调查揭示的经马来西亚、柬埔寨相关网络向中国走私英伟达芯片的路径，可能促使美国进一步收紧对东南亚中转渠道的出口管制——特朗普政府本周已宣布限制中国公司经该地区获取英伟达芯片，相关企业面临更严格的合规审查。

<details><summary>参考链接</summary>
<ul>
<li>Can an internal investigation resolve concerns about whether Singapore cloud company Megaspeed&#x27;s Nvidia chips were redirected to China? - Quora</li>
<li>Alleged Chinese Spy Touted Access to Nvidia GPUs - Yahoo</li>
<li><a href="https://www.ft.com/content/f3ad8a81-3890-4a8a-8853-ff0a94b08ba9?syn-25a6b1a6=1">Alice Huang’s links to the chip underworld</a></li>
<li><a href="https://www.nytimes.com/2026/11/22/us/politics/alice-huang-china-spy-agency-nvidia.html">U . S . Tracked Alice Huang’s Contacts With China Spy Agency During...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#export controls`, `#chip smuggling`, `#AI hardware`, `#supply chain`

---

<a id="item-tech-news-3"></a>
### [硅谷发生了什么？](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

一篇 O&\#x27;Reilly Radar 评论文章反思了硅谷从以丰裕驱动的创新文化转向以利润优化为目标的机制，并提出应将机制设计视为一种“逆向博弈论”，追问“我们应当玩什么游戏”。文章认为当前资本主义优化引擎的默认目标是股东价值而非人类繁荣，需要重新设计治理机制。该评论引发技术社区对硅谷治理、低利率时代影响和 AI 投资可持续性的讨论。

hackernews · greenyouse · 11月22日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50602947)

**「背景」** 该文章探讨了硅谷从早期注重丰裕与价值盈余的创新文化，转向以利润优化为目标的机制。文中提及的“机制设计”（mechanism design）是一种经济学与博弈论方法，强调通过设计规则来实现预期目标，而非被动接受现有市场规则。作者借此呼吁将目标从企业利润转向人类繁荣。

**「社区讨论」** 评论普遍认同文章的核心观点，即治理机制应当以人类繁荣而非企业利润为目标，并且需要承认市场是可设计、可重建的机器。有评论者回忆谷歌前首席经济学家哈尔·瓦里安曾估计仅约 6% 的谷歌搜索结果页含广告，以此说明早期丰裕文化；另有评论者认为低利率时代助长科技公司过度扩张，如今利率回升后 AI 投资是否会被市场惩罚仍存疑。

**标签**: `#Silicon Valley`, `#tech industry`, `#capitalism`, `#mechanism design`, `#governance`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美股科技股暴跌后亚洲多地出台稳定市场措施](https://news.bjd.com.cn/2026/11/22/12039852.shtml) ⭐️ 9.0/10

美国 AI 科技股周五遭遇大规模抛售，纳斯达克指数单日下跌 5.28%，费城半导体指数下跌近 11%。中国内地将融资保证金最低比例下调至 80%，韩国和中国台湾地区也宣布放宽回购限制、禁止平盘以下卖空等应对措施。

telegram · zaihuapd · 11月22日 13:24

**「背景」** 费城半导体指数主要衡量芯片股表现，此次重挫显示 AI 科技股抛售中芯片板块承压尤为明显。

**标签**: `#US tech selloff`, `#Nasdaq`, `#Asian markets`, `#short selling restrictions`, `#market stabilization`

---

<a id="item-finance-news-2"></a>
### [蚂蚁集团领投 Simplexity Robotics 1 亿美元 pre-A 轮，估值 16 亿美元](https://www.bloomberg.com/news/articles/2026-11-22/ant-group-bets-on-simplexity-to-thrive-in-china-s-humanoid-race) ⭐️ 7.0/10

彭博报道称，蚂蚁集团领投中国人形机器人公司 Simplexity Robotics 的 1 亿美元 pre-A 轮融资，投后估值为 16 亿美元；老股东阿里巴巴、腾讯、红杉中国和蓝驰创投跟投。

telegram · zaihuapd · 11月23日 02:02

**「背景」** Simplexity Robotics 于 2025 年 7 月在杭州成立，核心团队来自理想汽车，今年 3 月曾披露成立半年内完成五轮融资、累计 20 亿元人民币，当时投后估值已超 10 亿美元。

**标签**: `#humanoid robots`, `#venture capital`, `#Ant Group`, `#Simplexity Robotics`, `#China tech`

---