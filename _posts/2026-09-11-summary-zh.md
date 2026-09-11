---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 41 条内容中筛选出 17 条重要资讯。

---

**科技新闻**
1. [Calif Research 发布 WeWorm：通过微信通话传播的零点击蠕虫](#item-tech-news-1) ⭐️ 9.0/10
2. [Shopify 从 React Native 迁回 Swift 与 Kotlin](#item-tech-news-2) ⭐️ 8.0/10
3. [微软将 Rust 列为一线编程语言](#item-tech-news-3) ⭐️ 8.0/10
4. [浏览器中运行任意 Nix 包：trynix.dev](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepSeek 发布 V4.1 Flash 多模态模型](#item-tech-news-5) ⭐️ 8.0/10
6. [研究者担心 OpenAI 使用未发表数学成果且不署名](#item-tech-news-6) ⭐️ 7.0/10
7. [PlanetScale 推出分片 Postgres 服务 Neki](#item-tech-news-7) ⭐️ 7.0/10
8. [索尼数字游戏“拥有”表述成诉讼证据](#item-tech-news-8) ⭐️ 7.0/10
9. [数据中心表后供电难点（上）](#item-tech-news-9) ⭐️ 7.0/10
10. [蚂蚁国际与 Visa、Mastercard 合作开发 AI 支付标准](#item-tech-news-10) ⭐️ 7.0/10
11. [DeepSeek-AI 发布 DeepSelect TopK 内核](#item-tech-news-11) ⭐️ 7.0/10
12. [中国 AI 芯片厂商因 HBM 短缺涨价](#item-tech-news-12) ⭐️ 7.0/10
13. [腾讯混元发布开源音频编辑模型 AuK 及 AuK-Flash](#item-tech-news-13) ⭐️ 7.0/10

**财经新闻**
1. [Kalshi 获 CFTC 批准推出黄金白银永续期货，为首个非加密永续合约](#item-finance-news-1) ⭐️ 8.0/10
2. [iPhone Duo 进入中国折叠屏市场，定价 15999 元](#item-finance-news-2) ⭐️ 7.0/10
3. [美股盘前异动：梅西百货上调全年指引，Enbridge 宣布 25.5 亿美元收购，铜矿股走低](#item-finance-news-3) ⭐️ 7.0/10
4. [蚂蚁国际与 Visa、万事达卡合作制定 AI 智能体支付标准](#item-finance-news-4) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Calif Research 发布 WeWorm：通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布 WeWorm 演示，这是首个通过微信通话在 iOS 和 Android 之间传播的零点击蠕虫。受害者无需接听或与手机交互，即使接听也听不到任何声音，漏洞利用仍会成功。该团队借助 AI 在约两天内发现漏洞并编写首个远程代码执行（RCE）漏洞利用，再用一周构建蠕虫。此前此类规模的蠕虫通常需要更大团队数月开发，而 AI 已能完成大部分工作，团队则负责选择目标和安全测试等判断。

rss · Simon Willison · 9月10日 00:56

**「背景」** 零点击蠕虫指无需用户点击、接听或进行任何交互即可自动传播的恶意软件，通常利用通话或消息处理中的远程代码执行漏洞。微信是中国广泛使用的即时通讯应用，支持语音和视频通话，其跨 iOS 和 Android 的用户规模使其成为安全研究的重要目标。AI 辅助漏洞研究利用大语言模型协助代码分析、漏洞发现和利用生成，能显著缩短从发现漏洞到编写远程代码执行利用的时间。

**「对微信用户的影响」** 对微信 iOS 和 Android 用户而言，未接听的语音来电即可在数秒内劫持其微信账户；腾讯已发布缓解措施，用户应尽快更新应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm - First 0-Click Worm Spreading Through WeChat Calls Across...</a></li>
<li><a href="https://www.cyberkendra.com/2026/09/weworm-zero-click-wechat-worm-ios-android.html">WeWorm : Zero-Click WeChat Worm Hijacks iOS and Android</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#zero-click`, `#WeChat`, `#vulnerability-research`

---

<a id="item-tech-news-2"></a>
### [Shopify 从 React Native 迁回 Swift 与 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 工程博客标题显示，该公司正在将其移动应用从 React Native 迁回原生 iOS（Swift）和 Android（Kotlin）。该消息在开发者社区引发大量讨论。多位开发者提到，LLM 和代码生成能力提升使原生开发成本下降，从而减少了 React Native 复用 Web 开发者的优势。也有评论指出，跨 JavaScript、C++ 和原生线程调试崩溃的成本可能超过维护两套代码库，但文章的具体技术细节和迁移时间表尚未在现有内容中给出。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**「背景」** React Native 是 Meta 推出的跨平台移动开发框架，允许使用 JavaScript 编写一套代码同时生成 iOS 和 Android 应用；Swift 是苹果 iOS 的原生开发语言，Kotlin 是谷歌 Android 的官方语言。原生方案通常能提供更好的性能、平台特性和调试体验，但需要分别维护两套代码。Shopify 此次公告解释了其从 React Native 迁回各自平台原生语言的原因。

**「影响」** 对于正评估 React Native 或维护跨平台移动应用的团队，Shopify 的转向可能削弱企业级场景下采用 React Native 的论据，但缺少官方技术细节使具体影响仍不确定。

**「社区讨论」** 社区评论普遍对回归原生表示认同，认为跨 JS、C++、原生线程调试崩溃的成本可能高于维护双代码库；但也有人质疑将迁移归因于 LLM 的准确性，称其中型 React Native 到原生迁移主要发生在 2026 年 1 月之前且未依赖 LLM。另有开发者指出，当前模型生成原生应用的能力提升，削弱了 RN 复用 Web 开发者的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shopify.engineering/back-to-native">Native is now the future of mobile at Shopify (2026) - Shopify</a></li>
<li><a href="https://hybridtonative.com/moving-from-react-native-to-swift-kotlin-what-you-need-to-know/">Moving from React Native to Swift &amp; Kotlin : What... - Hybrid to Native</a></li>

</ul>
</details>

**标签**: `#mobile development`, `#react-native`, `#swift`, `#kotlin`, `#software engineering`

---

<a id="item-tech-news-3"></a>
### [微软将 Rust 列为一线编程语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

根据 Rust 基金会的一篇客座文章，微软已正式将 Rust 列为其一线（tier-1）编程语言。这一认定凸显了 Rust 在系统和基础设施软件领域日益重要的作用，并标志着该语言在行业中的成熟度与采用程度。社区评论中提到了微软计划在 2030 年前通过自动化工具将 10 亿行代码转换为 Rust 的目标，以及 DARPA 正在资助从 C 到 Rust 的自动化转换，但这些信息来自评论者，未在原文中得到确认。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**「背景」** 在微软，编程语言被分为不同支持层级，Tier-1 表示最高级别的支持与关键基础设施地位，通常能得到官方工具链、内部库和长期维护承诺。Rust 此前已在微软内部用于部分系统组件，而根据 rustfoundation.org 的客座文章，这一正式分类意味着 Rust 将与 C++ 一同被纳入统一代码生成平台，以降低维护和演进成本。同时，微软作为 Rust 基金会的白金会员，也印证了其对 Rust 生态的持续投入。

**「影响」** 对微软的系统和基础设施开发者来说，Rust 升为一线语言意味着它已成为微软官方支持的关键技术选项，可能降低新项目的采用门槛。

**「社区讨论」** 社区评论总体持积极态度，认为这表明 Rust 已从新兴语言成长为可与 C++ 和 C\# 竞争的成熟选择；同时有人提到微软 10 亿行代码转换目标和 MSVC 集成传闻，但也指出这些细节尚未得到官方确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rust_%28programming_language%29">Rust (programming language) - Wikipedia</a></li>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>

</ul>
</details>

**标签**: `#rust`, `#microsoft`, `#programming-languages`, `#systems-programming`, `#industry-adoption`

---

<a id="item-tech-news-4"></a>
### [浏览器中运行任意 Nix 包：trynix.dev](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria 发布了 trynix.dev，该工具利用 qemu-wasm 在浏览器中通过 WebAssembly 运行 x86\_64 Linux 虚拟机，能够启动过去 13 年任意 Nix 软件包。用户可以通过 URL 访问特定版本，例如 https://trynix.dev/?pkg=python3%403.6.2，点击 Load 后获得运行 Python 3.6.2（2017 年）的交互式 shell。Zakaria 还构建了 trynix-preview，这是一个 GitHub Action，会在拉取请求中评论一个链接，让评审者直接在浏览器中启动该 PR 的构建，无需服务器。这种结合 Nix、QEMU 和 WebAssembly 的方法为代码评审和历史版本测试提供了新可能。

rss · Simon Willison · 9月10日 23:44

**「背景」** Nix 是一个可复现的包管理器，能够精确引用过去版本并重建环境。QEMU 是一个通用硬件模拟器，qemu-wasm 将其编译到 WebAssembly，使浏览器无需插件即可运行 x86\_64 虚拟机。trynix.dev 利用这些特性，将任意历史 Nix 包启动在浏览器虚拟机中。

**标签**: `#nix`, `#webassembly`, `#qemu`, `#virtualization`, `#developer-tools`

---

<a id="item-tech-news-5"></a>
### [DeepSeek 发布 V4.1 Flash 多模态模型](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布 V4.1 Flash，这是全新模型结构系列中最小尺寸的模型，采用 552B 参数的 Causal-Encoder-Decoder 结构，输入和输出激活分别为 8B、16B，并原生支持多模态视觉理解。该模型已上线 DeepSeek API，模型名为 deepseek-flash。新价格于 2026 年 9 月 10 日 12:00 生效；9 月 14 日 12:00 后，deepseek-v4-pro 请求将路由至 V4.1 Flash，并按其价格计费。

telegram · zaihuapd · 9月10日 05:54

**「背景」** DeepSeek 是一家总部位于杭州、由 High-Flyer 所有并资助的人工智能研究公司，联合创始人梁文锋担任 CEO。该公司此前已发布 DeepSeek-V4、DeepSeek-R1 和 DeepSeek-Coder 等前沿大型语言模型。V4.1 Flash 是其在全新模型结构系列中推出的最小尺寸模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://deepseek.com/en/index.html">DeepSeek | Into the Unknown</a></li>

</ul>
</details>

**标签**: `#deepseek`, `#large-language-models`, `#multimodal`, `#model-release`, `#api`

---

<a id="item-tech-news-6"></a>
### [研究者担心 OpenAI 使用未发表数学成果且不署名](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 7.0/10

Hacker News 上的讨论质疑 OpenAI 可能在没有署名的情况下使用了研究者未发表的数学想法。相关帖子指向 Andreas Thom 和 Valerio Capraro 等人在社交平台上的发言，讨论研究者与 OpenAI 模型合作后，模型产出的成果未归功于原研究者。评论指出，OpenAI 据称向至少 10 万名研究者提供免费访问，内部模型解决开放问题的速度惊人，研究者可能无意中提供了新的训练数据。还有评论称，OpenAI 在得知某个重大数学证明可能出现在模型训练数据后，立即从仍在训练中的模型生成了 3000 亿个输出 token，这一行为显得可疑。信任问题的核心是模型是否记住了聊天中的未发表思路，以及强化学习是否真正独立发现了超人类技巧。

hackernews · pred\_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**「背景」** OpenAI 最近公布了数学成果（例如与 Navier-Stokes 相关），但其是否使用了研究者未发表的想法引发争议。数学家 Tristan Buckmaster 和 Andreas Thom 要求证明他们在 Codex 和 ChatGPT 上的工作没有被用于训练 OpenAI 的模型。该争议触及 AI 辅助科学的核心信任问题：研究者能否安全地使用前沿实验室的工具处理未发表的发现。

**「影响」** 对于与 OpenAI 模型合作开展未发表数学研究的研究者来说，核心后果是可能丧失对自己未发表成果的控制权与署名权，且模型训练与输出规模放大后，追溯特定想法的来源变得更加困难。

**「社区讨论」** 评论中既有将 OpenAI 比作人类合作者、认为不署名极不道德的批评，也有观点认为模型预训练吸收聊天内容与通过强化学习独立发现超人类技巧可以同时成立。此外，有人怀疑 OpenAI 在得知训练数据可能包含重大证明后立即生成 3000 亿 token 是“平行构造”，但尚无确凿证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit">OpenAI&#x27;s historic math solution overshadowed by credit controversy</a></li>
<li><a href="https://news.ycombinator.com/item?id=49639408">More questions about whether researchers can trust OpenAI with unpublished math | Hacker News</a></li>
<li><a href="https://www.progressiverobot.com/2026/09/10/openai-math-mathematicians-want-proof-didnt-use-their-work/">OpenAI Math Risk: Mathematicians Want Definitive Proof</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#machine learning`, `#mathematics`

---

<a id="item-tech-news-7"></a>
### [PlanetScale 推出分片 Postgres 服务 Neki](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale 推出了 Neki，这是一个分片式 Postgres 产品，旨在应对 Postgres 的扩展和分布式部署需求。官方公告在开头未直接说明 Neki 的用途，且产品为闭源，社区的关注点集中在封闭发布、CEO 的态度以及一致性模型未明确等方面。由于缺少具体技术细节，尚无法确认 Neki 在可用性与一致性之间的实际权衡。

hackernews · simon\_weber · 9月10日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49645686)

**「背景」** PlanetScale 此前以 Vitess 闻名，Vitess 将 MySQL 的水平分片从运维难题变成可推广技术，支撑了 Slack、GitHub、Square 等大型站点。Neki 是该公司推出的 PostgreSQL 分片方案，由运营大规模 Vitess 集群的团队构建，目标是为 Postgres 用户提供同级别的扩展能力、可靠性以及零停机重新分片，并宣称可扩展到数亿 QPS 和 PB 级数据。

**「影响」** 对于正在评估分布式 Postgres 的团队，Neki 的闭源性质和未公开的一致性/可用性权衡意味着短期内缺乏可验证的决策依据。

**「社区讨论」** 社区意见分歧：有人认为 Neki 可能成为新标准，但更多人批评发布帖未清楚说明产品用途、CEO 对竞品 multigres 的贬低态度以及闭源策略，并追问其在高可用分布式场景下的一致性与可用性权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neki.dev/">Neki | Sharded Postgres by PlanetScale</a></li>
<li><a href="https://planetscale.com/docs/postgres/sharding">Horizontal sharding for Postgres - PlanetScale</a></li>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale</a></li>

</ul>
</details>

**标签**: `#databases`, `#postgres`, `#sharding`, `#distributed-systems`, `#planetscale`

---

<a id="item-tech-news-8"></a>
### [索尼数字游戏“拥有”表述成诉讼证据](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 7.0/10

一个位于 consumerrights.wiki 的页面汇总了索尼网站将数字游戏称为玩家“拥有”的表述，以支持一起 PlayStation 数字游戏所有权诉讼。该诉讼涉及数字游戏是销售还是许可的核心问题，可能影响消费者退款、转售与账号封禁后的权利。讨论中引用的诉讼文件显示，PlayStation 服务条款第 14 条包含强制仲裁和集体诉讼豁免，并要求用户在 30 天内书面通知才能退出。诉讼文件还提到，原告 Jason Mendoza 于 2026 年 2 月 14 日以 69.99 美元购买《Resident Evil Requiem》后，另一原告 Edward Heycock 于 2 月 25 日也购得该游戏，索尼据此主张若前者“拥有”则后者无法购买。

hackernews · haunter · 9月10日 12:18 · [社区讨论](https://news.ycombinator.com/item?id=49642531)

**「背景」** 这起集体诉讼指控索尼在 PlayStation Store 使用“立即购买”“确认购买”等所有权表述销售数字游戏，同时却在购买按钮上方以小号、未高亮文字声明玩家仅获得许可而非拥有游戏。索尼在回应诉讼时辩称，理性消费者应当明白购买数字游戏并不等于拥有它。然而，有玩家整理出索尼网站多次声称玩家“拥有”数字游戏的页面，用以反驳这一立场。

**「影响」** 如果法院采信索尼网站“拥有”表述，索尼可能需要澄清 PlayStation Store 购买是所有权还是可撤销许可，从而影响数字游戏的退款、转售和账号封禁政策。

**「社区讨论」** 有评论者抨击强制仲裁剥夺消费者和劳动者权利，认为应属非法。另有评论围绕索尼的“若首个买家拥有则后来者无法购买”论证展开，指出拥有一个副本不等于拥有所有副本，并质疑该辩护可能打开索尼不愿触及的复制权讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit">Sony PlayStation digital game ownership lawsuit</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lob0xQMEVSRmdzSm96YVJaay1pZ0FQAQ?hl=en-GB&amp;gl=GB&amp;ceid=GB:en">Google News - Gamers sue Sony over digital game ownership ...</a></li>
<li><a href="https://kotaku.com/fans-put-together-a-list-of-every-time-sony-said-players-owned-their-digital-games-after-the-company-argued-in-a-lawsuit-that-it-was-obvious-players-dont-2000733271">A List Of Times Sony Told People They Own Their Digital Games</a></li>

</ul>
</details>

**标签**: `#digital ownership`, `#consumer rights`, `#video games`, `#Sony`, `#software licensing`, `#legal`

---

<a id="item-tech-news-9"></a>
### [数据中心表后供电难点（上）](https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the) ⭐️ 7.0/10

这篇来自 SemiAnalysis 的文章（作者 Ellie Holbrook）探讨了为数据中心提供表后电力（behind-the-meter power）所面临的技术与经济挑战，并指出这是 AI 基础设施扩展的关键约束。文章以“Dumb Science Experiments vs. Money Printing Machines”为小标题，点出表后供电方案从实验性尝试转向可盈利运营的难度。由于该文仅为系列第一部分且预览内容有限，未披露具体技术方案、成本数据或案例细节。总体而言，分析聚焦于为何表后供电在技术、监管和商业层面难以大规模落地，以及这对 AI 算力扩张的潜在影响。

rss · Semianalysis · 9月10日 14:28

**「背景：表后电源与数据中心」** 表后电源（behind-the-meter）指在用户电表后侧就地发电并直接供负载使用、不经公共电网的供电方式，通常用于绕开电网容量限制与高电价。随着数据中心电力需求超过电网扩张速度，有分析指出表后方案可弥合近期电网瓶颈，但核心难点在于能否协调数据中心增长与可靠、可扩展且经济可行的电力基础设施。此外，英国分区定价预计十年内不会落地，而美国得克萨斯州通过参议院第 6 号法案及大负荷新规，对数据中心表后电源与用水提出更严格监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/goldman-sachs_behind-the-meter-power-may-be-a-solution-activity-7501706619647352833-qaod">&#x27; Behind - the - meter &#x27; power may be a solution to grid constraints...</a></li>
<li><a href="https://datacentrereview.com/2025/04/behind-the-meter-data-centres/">Now is the time for data centres to install behind - the - meter</a></li>
<li><a href="https://www.newsworthy.ai/news/202608112731/behind-the-meter-power-why-texas-data-centers-cant-lean-on-the-grid">Behind - the - Meter Power : Why Texas Data Centers ... | Newsworthy.ai</a></li>

</ul>
</details>

**标签**: `#datacenter power`, `#energy infrastructure`, `#AI hardware`, `#behind-the-meter`, `#semiconductor analysis`

---

<a id="item-tech-news-10"></a>
### [蚂蚁国际与 Visa、Mastercard 合作开发 AI 支付标准](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 7.0/10

蚂蚁国际宣布与 Visa、Mastercard 合作，为 AI 代理支付制定通用标准。三方将建立“了解你的代理”（Know Your Agent）机制，把 AI 代理与有效实体关联起来，评估其行为并监测风险，以提升不同支付系统间的互操作性和安全性。三方援引麦肯锡预测称，到 2030 年，AI 代理可能处理全球消费者商业交易中的 3 万亿至 5 万亿美元。

telegram · zaihuapd · 9月10日 03:00

**「背景」** AI 代理是能在用户授权下自主执行交易和支付的软件实体，在电商与金融服务中应用逐渐增多。由于不同支付系统之间缺乏统一识别和风险监测方式，蚂蚁国际、Visa 和 Mastercard 提出的“了解你的代理”（Know Your Agent）机制借鉴了传统“了解你的客户”（KYC）思路，旨在让代理在参与服务商间实现身份互认，减少重复注册并加强风险控制。

**「影响」** 该合作旨在为接入相关支付网络的商户、开发者与 AI 代理服务商提供一个可复用的代理身份与风险评估框架，从而减少跨支付系统的集成障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://crypto.news/ant-international-joins-visa-mastercard-to-build-ai-agent-payment-standards/">Ant International joins Visa , Mastercard to build AI agent payment ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#payments`, `#fintech`, `#standards`, `#interoperability`

---

<a id="item-tech-news-11"></a>
### [DeepSeek-AI 发布 DeepSelect TopK 内核](https://github.com/deepseek-ai/DeepSelect) ⭐️ 7.0/10

DeepSeek-AI 于 2026 年 9 月 10 日发布了 DeepSelect v1.0.0，这是一个面向 DeepSeek 稀疏注意力（DSA）和采样器的高性能 TopK 内核。该项目声称相比原生 torch.topk 可实现 2 至 20 倍的加速，旨在优化稀疏注意力及采样等场景中的 TopK 操作性能。目前发布公告未提供具体基准测试细节、支持的硬件/软件环境或已知限制，因此上述加速幅度仍需结合实际使用条件验证。源码已在 GitHub 上公开。

telegram · zaihuapd · 9月10日 07:28

**「背景」** DeepSeek 稀疏注意力（DSA）是 DeepSeek 风格模型使用的稀疏注意力路径，相关内核大多面向 Hopper \(SM90\) 与 Blackwell \(SM100+\) GPU。TopK 内核用于在注意力或采样过程中选取最重要的候选，PyTorch 原生的 torch.topk 是通用实现，但未必针对 DSA 的访存和计算模式优化。DeepSelect 以 CUDA 实现、MIT 协议发布，独立于 DeepGEMM 等库，专门为 DSA 和采样器提供 TopK 加速。

**「影响」** 对于使用 DeepSeek V3.2、V4、V4.1 稀疏注意力或采样器的开发者，DeepSelect v1.0.0 提供了比原生 torch.topk 快 2 至 20 倍的 TopK 内核，有望显著降低相关计算延迟。该加速数据来自项目自述，尚未见独立基准验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/deeplearning/cudnn/latest/fe-oss-apis/dsa.html">DeepSeek Sparse Attention (DSA) — NVIDIA cuDNN</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSelect">GitHub - deepseek-ai/ DeepSelect : DeepSelect : TopK kernels for...</a></li>

</ul>
</details>

**标签**: `#TopK kernel`, `#sparse attention`, `#performance optimization`, `#DeepSeek`, `#open source`

---

<a id="item-tech-news-12"></a>
### [中国 AI 芯片厂商因 HBM 短缺涨价](https://www.reuters.com/world/asia-pacific/chinas-ai-chipmakers-raise-prices-high-bandwidth-memory-shortage-bites-2026-09-10/) ⭐️ 7.0/10

全球高带宽存储器（HBM）供应紧张持续冲击中国 AI 芯片产业，华为、寒武纪等厂商已开始上调产品价格。华为升腾 950DT 芯片报价较两个月前上涨约 20%—50%，部分老款芯片价格上涨约 30%；寒武纪新一代思元 690 价格预计上涨约 20%—30%。HBM 主要由 SK 海力士、三星和美光供应，美国出口限制进一步加剧中国市场供应压力。随着国内 AI 算力需求增长，HBM 短缺正成为制约国产 AI 芯片扩张的重要瓶颈。

telegram · zaihuapd · 9月10日 09:29

**「背景：HBM 与出口管制」** 高带宽存储器（HBM）通过堆叠 DRAM 芯片提供远高于传统显存的带宽，是训练和推理大模型所需 AI 加速器的关键配套器件，其供应高度集中于 SK 海力士、三星和美光。美国近年对先进计算芯片及配套存储的出口管制，限制了这些厂商向中国供应高端 HBM；叠加中国本土 AI 算力需求快速增长，导致华为升腾、寒武纪思元等国产 AI 芯片所需的 HBM 出现短缺，并传导至芯片价格。

**「影响」** 依赖国产 AI 芯片的中国数据中心和算力用户可能面临采购成本上升，且短期内高端 HBM 供应不确定性因美国出口限制而难以缓解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://careeraheadonline.com/china-ai-chipmakers-hike-prices-amid-memory-shortage">China AI Chipmakers Hike Prices Amid Memory Shortage | Caree</a></li>
<li><a href="https://cryptobriefing.com/china-ai-chipmakers-raise-prices-hbm-shortage/">China&#x27;s AI chipmakers hike prices up to 50% as high-bandwidth memory shortage bites</a></li>
<li><a href="https://bhaskarlive.in/science-and-technology/china-ai-chip-prices-rise-as-hbm-supply-shortage-deepens-2139448">China AI Chip: Prices Rise as HBM Supply Shortage Deepens</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#HBM`, `#supply chain`, `#China`, `#semiconductors`

---

<a id="item-tech-news-13"></a>
### [腾讯混元发布开源音频编辑模型 AuK 及 AuK-Flash](https://x.com/TencentHunyuan/status/2097996926876795197) ⭐️ 7.0/10

腾讯混元正式发布开源音频编辑模型 AuK，可通过自然语言指令和参考音频统一完成语音生成与编辑，具体支持零样本文本转语音、音色/风格/情绪编辑、去口音和多人语音分离等功能。同时发布的 AuK-Flash 采用 4 步推理，在匹配条件下速度约提升 4.5 倍。代码、模型权重和演示均已上线。该开源发布来自主要 AI 实验室，为开发者在语音编辑与合成任务中提供了可直接获取的实现。

telegram · zaihuapd · 9月10日 11:56

**「背景」** 腾讯混元 AuK 是一个参数规模约 15 亿（1.5B）的开源语音模型，采用 MIT 许可证发布，目标是用单一基础模型替代多个专用语音工具，覆盖语音生成、编辑、分离等任务。相关技术报告显示，该模型以自然语言指令统一控制语音处理，但在纯信噪比等指标上与专用降噪/分离工具相比仍有一定取舍。

**「影响」** AI 与音频开发者可直接使用 AuK 完成自然语言驱动的语音生成和编辑，并可通过 AuK-Flash 在匹配条件下获得约 4.5 倍推理速度提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/auk-open-weights-speech-explained">AuK Technical Report: Tencent&#x27;s 1.5B Open Speech Model</a></li>
<li><a href="https://alphasignal.ai/news/tencent-s-auk-replaces-16-speech-tools-with-one-open-source-model">Tencent&#x27;s AuK Replaces 16 Speech Tools With One Open-Source Model | AlphaSignal</a></li>

</ul>
</details>

**标签**: `#audio generation`, `#open-source AI`, `#text-to-speech`, `#speech editing`, `#Tencent`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [Kalshi 获 CFTC 批准推出黄金白银永续期货，为首个非加密永续合约](https://www.cnbc.com/2026/09/10/kalshi-launches-perps-for-gold-and-silver-following-cftc-approval-expanding-futures-offerings.html) ⭐️ 8.0/10

Kalshi 在获得 CFTC 批准后于周四推出黄金和白银永续期货，成为美国首个非加密永续期货；据该平台网站数据，其加密永续合约自 5 月获批以来名义交易量已达 440 亿美元。

rss · CNBC Finance · 9月10日 14:00

**「背景」** 永续期货（“perps”）没有到期日、投资者无需持有标的资产，合约通过资金费率与现货价格保持一致；Kalshi 于 5 月底首次获批在美国上市加密永续期货。

**「影响」** 上市消息后，CBOE 和 CME Group 股价因市场担忧其现有期货业务受冲击而下跌，CME 还起诉 CFTC 以阻止该批准。

**标签**: `#perpetual futures`, `#CFTC`, `#gold`, `#silver`, `#commodity derivatives`

---

<a id="item-finance-news-2"></a>
### [iPhone Duo 进入中国折叠屏市场，定价 15999 元](https://www.cnbc.com/2026/09/11/the-iphone-duo-enters-chinas-crowded-foldable-market.html) ⭐️ 7.0/10

苹果首款折叠屏手机 iPhone Duo 在中国发布，定价 15999 元（2230 美元），低于华为 Mate XT2 的 19999 元，但高于小米 18 Fold 的 10999 元。

rss · CNBC Finance · 9月11日 00:19

**「背景」** 中国是苹果第三大市场，贡献约 17% 营收；华为、小米、荣耀、OPPO、vivo 已销售横折、竖折及三折机型，折叠屏品类更为成熟。

**标签**: `#Apple`, `#foldable phones`, `#China smartphone market`, `#product launch`, `#competition`

---

<a id="item-finance-news-3"></a>
### [美股盘前异动：梅西百货上调全年指引，Enbridge 宣布 25.5 亿美元收购，铜矿股走低](https://www.cnbc.com/2026/09/10/stocks-making-the-biggest-moves-premarket-.html) ⭐️ 7.0/10

美股盘前多只个股波动：梅西百货第二季度收入超预期并上调全年净销售额、可比销售额和每股收益指引，Enbridge 宣布以 25.5 亿美元收购 Tallgrass Energy 原油运输业务。铜矿股因铜价下跌大幅走低，Freeport-McMoRan 跌近 7%。

rss · CNBC Finance · 9月10日 11:54

**「背景」** 盘前交易是美股正式开盘前的交易时段，公司的财报、业绩指引、并购消息以及大宗商品价格变化通常会引发股价显著波动。

**标签**: `#premarket movers`, `#earnings`, `#mergers and acquisitions`, `#copper prices`, `#stock market`

---

<a id="item-finance-news-4"></a>
### [蚂蚁国际与 Visa、万事达卡合作制定 AI 智能体支付标准](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 7.0/10

蚂蚁国际周四宣布与 Visa 和万事达卡合作，共同制定 AI 智能体支付的“了解你的代理”标准。公司援引麦肯锡预测称，到 2030 年 AI 智能体可能处理 3 万亿至 5 万亿美元的全球消费者商务。

rss · CNBC Finance · 9月10日 01:53

**「背景」** 过去 12 个月，Visa、万事达卡和蚂蚁国际各自发布了 AI 智能体支付协议；蚂蚁国际运营 Alipay+，已与 50 多家电子钱包合作，此次合作旨在让不同系统的用户实现互操作。

**「影响」** 对商户和支付处理机构而言，统一标准可能减少重复注册，并让不同支付系统的用户更容易互操作。

**标签**: `#AI payments`, `#Ant International`, `#Visa`, `#Mastercard`, `#digital wallets`

---