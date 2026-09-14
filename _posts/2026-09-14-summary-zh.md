---
layout: default
title: "Horizon Summary: 2026-09-14 (ZH)"
date: 2026-09-14
lang: zh
---

> 从 39 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [Homebrew 7.0.0 发布：官方 macOS 原生图形界面及安全变更](#item-tech-news-1) ⭐️ 9.0/10
2. [汽车收集的数据被出售给第三方](#item-tech-news-2) ⭐️ 8.0/10
3. [4-hi HBM：同带宽、更少裸片，降低推理成本](#item-tech-news-3) ⭐️ 8.0/10
4. [Fable 5.1 声称破解 370 年未解的 Cyphral Distich 密码](#item-tech-news-4) ⭐️ 7.0/10
5. [谷歌为何仍在投放欺诈广告？](#item-tech-news-5) ⭐️ 7.0/10
6. [保罗·格雷厄姆：初创企业如何变强大](#item-tech-news-6) ⭐️ 7.0/10
7. [Garry Tan 主张美国开放权重实验室可蒸馏前沿模型](#item-tech-news-7) ⭐️ 7.0/10
8. [CUDA 护城河：AMD DeepSeek v4.1 性能落后最多 42 倍](#item-tech-news-8) ⭐️ 7.0/10
9. [GitHub 故障影响 Issues、Pages 和 Pull Requests](#item-tech-news-9) ⭐️ 7.0/10
10. [麒麟 9050 Pro 评测：3D 堆叠提升性能与能效](#item-tech-news-10) ⭐️ 7.0/10
11. [苹果 OS 27 被曝支持第三方模型接入 Siri](#item-tech-news-11) ⭐️ 7.0/10
12. [特朗普拒绝放缓 AI 发展及安全监管呼吁](#item-tech-news-12) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Homebrew 7.0.0 发布：官方 macOS 原生图形界面及安全变更](https://brew.sh/2026/09/13/homebrew-7.0.0/) ⭐️ 9.0/10

Homebrew 于 2026 年 9 月 13 日发布 7.0.0 版本，带来官方 macOS 原生图形界面、更快的安装与升级速度、更严格的沙箱保护，以及内置漏洞检查与安全公告数据库。该版本停止支持 macOS 10.15 及更早版本，Intel Mac 被降为 Tier 3，不再提供新预编译包；Linux 沙箱由 Bubblewrap 改用 Landlock。这些变化提升了用户界面体验和软件供应链安全，但使用老旧 macOS 或 Intel Mac 的用户将无法获得新的预编译包。

telegram · zaihuapd · 9月13日 11:23

**「背景」** Homebrew 是 macOS 和 Linux 上广泛使用的开源包管理器。其 6.0.0 版本引入了 Bubblewrap 沙箱以增强安装安全，但该方案需要额外依赖，并在 Docker 环境中出现权限设置问题；7.0.0 改用 Linux 的 Landlock 安全机制，无需额外依赖或提升 Docker 权限，从而简化部署并避免这些限制。此外，Homebrew 的 macOS 安装包改为仅支持 Apple Silicon，反映了对旧硬件支持收缩的趋势。

**「对旧版 macOS 与 Intel Mac 用户的直接影响」** 对于仍在使用 macOS 10.15 或更早系统的用户，Homebrew 7.0.0 将不再提供支持或新预编译包，Intel Mac 用户也会转为 Tier 3 并失去新预编译包，需升级 macOS 或改用源码安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://brew.sh/2026/09/13/homebrew-7.0.0/">Homebrew: 7.0.0</a></li>
<li><a href="https://daily.dev/posts/homebrew-7-0-0-cj7h7kzxv">Homebrew 7.0.0 | daily.dev</a></li>
<li><a href="https://github.com/Homebrew/brew/releases/tag/7.0.0">Release 7.0.0 · Homebrew/brew</a></li>
<li><a href="https://brew.sh/2026/09/13/homebrew-7.0.0/">Homebrew : 7 . 0 . 0</a></li>

</ul>
</details>

**标签**: `#homebrew`, `#macos`, `#package-manager`, `#developer-tools`, `#security`

---

<a id="item-tech-news-2"></a>
### [汽车收集的数据被出售给第三方](https://www.theverge.com/column/994172/your-car-is-selling-your-data) ⭐️ 8.0/10

据 The Verge 专栏报道，汽车制造商正在收集并出售车辆数据及驾驶员数据，包括地理位置信息，引发隐私担忧。社区讨论指出，加州议会已通过 AB-1542 法案，可能将出售或共享精确定位（可映射至 1850 英尺半径内个人）等敏感个人信息定为非法。有评论区分了“车辆事实数据”（如 VIN、规格、召回状态、里程表）与“驾驶员遥测数据”（如速度、位置、时间戳），并认为后者需要禁止而非依赖匿名化。即使车主关闭数据收集功能，里程等数据仍可能通过 Carfax 等渠道被共享，表明数据可能持续存在。缺乏有效数据保护法律是此类监控存在的原因之一。

hackernews · bookofjoe · 9月13日 13:45 · [社区讨论](https://news.ycombinator.com/item?id=49683953)

**「背景」** 现代联网汽车会通过内置系统收集车辆状态和驾驶行为数据，包括 GPS 位置、速度和时间戳。社区评论将数据分为两类：车辆事实数据（如 VIN、规格、召回状态、里程表）和驾驶员遥测数据（如速度、位置、时间戳），后者曾被通用汽车出售。有评论指出，美国现有的 DRIVER 法案因将两类数据混同而无法有效解决问题，且缺乏有效数据保护法律是此类监控存在的原因之一。

**「影响」** 据社区评论，加州议会已通过 AB-1542 法案，若州长签署，将使出售或共享可定位个人至 1850 英尺半径内的敏感地理位置数据成为非法，这可能直接限制车企和第三方此类数据交易。

**「社区讨论」** 社区讨论普遍认为汽车数据收集和出售缺乏有效监管，但对解决路径存在分歧。有评论主张直接禁止收集驾驶员遥测数据而非依赖匿名化，并指出 DRIVER 法案因混同车辆事实与驾驶员数据而难以奏效；也有评论询问法拉第笼等技术手段的可行性，并担忧法律隐私保护正在削弱。

**标签**: `#car data`, `#privacy`, `#telemetry`, `#data regulation`, `#connected vehicles`

---

<a id="item-tech-news-3"></a>
### [4-hi HBM：同带宽、更少裸片，降低推理成本](https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi) ⭐️ 8.0/10

SemiAnalysis 作者 Myron Xie 的分析指出，4-hi HBM 堆叠能够用更少的 DRAM 裸片实现与更高堆叠相同的带宽。该设计通过减少每堆叠所需的裸片数量，直接降低 AI 推理加速器的内存成本和 DRAM 总用量。在 HBM 供应紧张、DRAM 晶圆稀缺的背景下，这使有限的 DRAM 容量可以支撑更多推理工作负载。文中强调关键在于带宽相同，而非堆叠高度本身。

rss · Semianalysis · 9月13日 18:19

**「背景」** 高带宽内存（HBM）通过将多个 DRAM 芯片垂直堆叠并采用宽接口实现高吞吐量；例如，一个 4-hi HBM 堆栈包含四颗 DRAM 芯片，每颗提供两个 128 位通道，总位宽达 1024 位（tool-1-1）。在 AI 推理等以内存带宽为主要瓶颈的工作负载中，更短的堆叠高度可能以更少的芯片提供相同的带宽，从而改善每美元带宽和每 token 成本（tool-1-2）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://newsletter.semianalysis.com/p/long-live-the-short-king-why-4-hi">Long Live the Short King: Why 4 - hi HBM Wins</a></li>

</ul>
</details>

**标签**: `#HBM`, `#AI inference`, `#memory bandwidth`, `#semiconductor hardware`, `#cost optimization`

---

<a id="item-tech-news-4"></a>
### [Fable 5.1 声称破解 370 年未解的 Cyphral Distich 密码](https://www.vals.ai/blogs/fable-solves-cyphral-distich) ⭐️ 7.0/10

Fable 5.1 据称解决了 Cyphral Distich，这是一道有 370 年历史的未解密码。该结果由模型供应商 Vals.ai 发布，展示了大语言模型在历史密码破解方面的能力。目前公开信息中缺少密码具体内容和破解方法的技术细节。这一说法来自厂商博客，尚未经过独立学术或密码学社区验证。

hackernews · u1hcw9nx · 9月13日 21:06 · [社区讨论](https://news.ycombinator.com/item?id=49688695)

**「背景」** Cyphral Distich 是托马斯·厄克特爵士在其 1653 年著作《Logopandecteision》中发布的一种密码，约 370 年来一直未解，并被列入克劳斯·施梅的“50 个未解密码”名单。该密文由点号分隔的数字组成，例如“1.2.12.1.20.20.49.20.20.35.33.4.6.8.35.5.33.5.5.18.10.3.11.32.42”。

**「影响」** 该结果主要影响历史密码研究和 AI 密码分析评估，表明当前模型可以尝试解决长期未解的经典密码，但需独立验证其真实性和可复现性。

**「社区讨论」** 社区对结果存在分歧：有用户分享 ChatGPT 在 20 分钟内破解家人童年密码的正面经验；但也有人指出该成果可能实际依赖底层模型（如 Opus 5），或是因为历史密码少有人研究而属于“低垂果实”，不一定代表通用能力突破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich</a></li>
<li><a href="https://itdoeswhatnow.com/m/2026-08-31-claude-fable-5-1-solves-a-370-year-old-cipher/">Claude Fable 5.1 solves a 370-year-old cipher in a Vals AI test • It Does What Now?</a></li>
<li><a href="https://securityonline.info/claude-fable-decrypts-cyphral-distich/">Claude Fable 5.1 Decrypts 370-Year-Old Cyphral Distich Mystery</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptography`, `#historical-cipher`, `#codebreaking`, `#machine-learning`

---

<a id="item-tech-news-5"></a>
### [谷歌为何仍在投放欺诈广告？](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads) ⭐️ 7.0/10

这篇文章分析了谷歌为何仍在向用户投放欺诈性广告，认为平台审核不严与收入激励是主要原因。文章指出，诈骗者利用云服务子域名和人工智能生成内容快速更换广告素材，使谷歌的审核机制难以跟进，YouTube 等平台上因此出现大量虚假促销。作者认为谷歌在追求广告收入的同时未能有效保护用户，这引发了对其平台责任和信任度的质疑。

hackernews · iamflimflam1 · 9月13日 17:37 · [社区讨论](https://news.ycombinator.com/item?id=49686445)

**「背景」** 谷歌广告政策明确禁止模仿操作系统对话框、系统警告或错误提示的广告，但诈骗者常利用 cloaking（内容伪装）和每日更换子域名等手法绕过平台审查。这类手段使大量虚假广告仍能混入搜索、YouTube 和第三方网站；此前谷歌还以“未发现违规”为由驳回相关投诉，而 Gemini 对同一广告的分析则识别出多处欺骗特征。

**「对发布商和用户的影响」** 对于使用 Google AdSense 的发布商和普通用户，诈骗广告仍会持续出现在其网站和 YouTube 等平台，且广告主无法屏蔽诈骗者租用的某些域名；尽管 Google 在 2025 年移除了超过 6.02 亿条与诈骗相关的广告并暂停了 400 多万个诈骗关联账户，但这反而揭示了问题的规模，并未消除持续存在的诈骗广告。

**「社区讨论」** 多位评论者提供了具体案例：发布商在 AdSense 上持续看到诈骗广告，诈骗者使用 azurestaticapps.net、azurewebsites.net、herokuapp.com、ondigitalocean.app、digitaloceanspaces.com、netlify.app 等子域名，而谷歌不允许按域名屏蔽。还有人指出 YouTube 广告几乎全是人工智能生成的诈骗内容，并认为谷歌为了掩盖 AI 失利或榨取广告收入而故意放宽审核，有人呼吁对平台施加严格责任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads">Why is Google still serving dodgy ads ? | atomic 14</a></li>
<li><a href="https://sesamedisk.com/problems-with-google-ads/">Why Are Google Ads Still Serving Dodgy Ads ? - Sesame Disk</a></li>
<li><a href="https://dzen.ru/b/aqbya-6lSHKwoSKj">Google отклонила жалобы на рекламу, которую забраковала... | Дзен</a></li>
<li><a href="https://blog.google/products/ads-commerce/google-ads-safety-report-2023/">Our 2023 Ads Safety Report - The Keyword ads_safety_report_2024 - services.google.com Google’s 2025 Ads Safety Report - The Keyword 2023 Ads Safety Report - Google Search Why advertisers can no longer trust Google - LinkedIn Google Ads Safety Report 2025: 8.3B Ads Removed - almcorp.com</a></li>

</ul>
</details>

**标签**: `#google`, `#online-advertising`, `#trust-safety`, `#tech-industry`, `#scam-ads`

---

<a id="item-tech-news-6"></a>
### [保罗·格雷厄姆：初创企业如何变强大](https://paulgraham.com/powerful.html) ⭐️ 7.0/10

保罗·格雷厄姆的新文章《Making Startups Powerful》为初创企业提供战略建议，核心是创造比捕获更多的价值、采用全栈方式，并留意用户对产品的非预期使用。文章认为慷慨能增强企业实力，而非软弱表现，例如不要从客户身上榨取每一分钱。这一观点与 Tim O&\#x27;Reilly “创造的价值应大于捕获的价值”相呼应，并针对创始人与职业 CEO 的不同视角展开。

hackernews · tosh · 9月13日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49684196)

**「背景」** Paul Graham 的创业相关文章多次强调，创业失败的核心通常是“没有做出用户想要的东西”，并建议尽早发布最小版本、根据用户反馈持续改进，以及创始人应全情投入（tool-1-1, tool-1-3）。他还总结了执行层面的原则，如避免分心、不轻易放弃等（tool-1-2）。这篇《Making Startups Powerful》延续了他对创始人策略的讨论，社区评论中引用的核心理念包括创造多于捕获的价值、走全栈路线以及重视用户对产品的意外使用。

**「社区讨论」** 评论区普遍赞同文章观点，多位读者引用自身经验。Bob1029 描述了为客户完成最困难工作、逐步“吃掉”客户的全栈变体；CM30 强调用户误用产品是强烈需求信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gavrilobozovic.com/thoughts/paul-graham">Paul Graham&#x27;s greatest advice for startuppers — Gavrilo Bozovic</a></li>
<li><a href="https://www.jaakkoj.com/blog/graham">Paul Graham 101</a></li>
<li><a href="https://medium.com/swlh/graham-for-the-lazy-51a170dacc86">Paul Graham’s Startup Advice for the Lazy | by Stelios Constantinides | The Startup | Medium</a></li>

</ul>
</details>

**标签**: `#startups`, `#business strategy`, `#paul graham`, `#technology industry`, `#entrepreneurship`

---

<a id="item-tech-news-7"></a>
### [Garry Tan 主张美国开放权重实验室可蒸馏前沿模型](https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/) ⭐️ 7.0/10

Y Combinator 的 Garry Tan 主张，美国开放权重 AI 实验室应被允许蒸馏前沿模型，理由是前沿实验室在训练时同样未经许可抓取了大量人类知识。他批评 Anthropic 等闭源实验室在讨论蒸馏时缺乏道德制高点，并警告真正的 AI 末日情景是前沿 AI 权力集中于单一闭源提供商。该观点于 2026 年 9 月 11 日发表，正值模型蒸馏与版权政策争论升温之际。

hackernews · TheJCDenton · 9月13日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49685253)

**「背景：模型蒸馏与开放权重之争」** 模型蒸馏（distillation）是一种让较小模型模仿较大“前沿”模型输出或中间表示，从而以更低成本获得接近能力的技术，常被用于从大型专有模型生成训练数据。开放权重（open-weight）模型公开参数、可被下载后微调或蒸馏，而“前沿模型”通常指 OpenAI、Anthropic 等实验室通过 API 提供的性能最强但参数不公开的模型。Garry Tan 主张允许美国开放权重实验室蒸馏美国前沿模型，背景是美国希望在开放权重赛道上减少对中国模型的依赖，同时专有实验室与开放社区对“能否蒸馏”存在分歧。

**「社区讨论」** 社区评论普遍同意前沿实验室使用大量版权数据训练，因此缺乏限制蒸馏的道德立场；部分评论还指出开源模型已接近前沿水平，并预测 OpenAI 和 Anthropic 可能难以收回巨额训练成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/11/y-combinators-garry-tan-wants-u-s-open-weight-ai-labs-to-distill-frontier-models-too/">Y Combinator&#x27;s Garry Tan wants US open-weight AI labs to &#x27;distill&#x27; frontier models, too | TechCrunch</a></li>
<li><a href="https://github.com/hanzhad/squelch-news-engine/issues/831">Y Combinator’s Garry Tan wants US open-weight AI labs to ‘distill’ frontier models, too · Issue #831 · hanzhad/squelch-news-engine</a></li>
<li><a href="https://www.newsbeep.com/us/845129/">Y Combinator&#x27;s Garry Tan wants US open-weight AI labs to &#x27;distill&#x27; frontier models, too - United States News Beep | NewsBeep.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#model distillation`, `#open source`, `#policy`, `#copyright`

---

<a id="item-tech-news-8"></a>
### [CUDA 护城河：AMD DeepSeek v4.1 性能落后最多 42 倍](https://x.com/SemiAnalysis_/status/2098618867035557984) ⭐️ 7.0/10

CUDA 版 vLLM 在 DeepSeek v4.1 Flash 发布两天后即提供支持，而 AMD 随后才发布其 DeepSeek v4.1 Flash 镜像。功能虽可开箱即用，但按每美元性能计算，AMD 方案比 H200 最多落后 14.8 倍，比 B200/B300 最多落后 42 倍。SemiAnalysis 指出，NVIDIA 与约 600 万开发者生态的合作使 CUDA 在第一天就完成优化，这正是 CUDA 生态护城河的体现。这一差距突显了在 AI 基础设施中，软件生态和及时优化对硬件实际价值的关键影响。

telegram · zaihuapd · 9月13日 05:55

**「背景」** SemiAnalysis 持续追踪 DeepSeek V4 系列在不同 GPU 上的推理表现，并多次强调 CUDA 生态的先发优势。例如，其 DeepSeekV4 1.6T 性能跟踪指出 CUDA 栈使分布式推理在发布首日即可用（tool-1-1），而 AgentX 基准中 NVIDIA 硬件的每美元性能可达 H100 的 12 倍以上（tool-1-2）。这解释了为何 AMD 需要更晚发布 DeepSeek v4.1 Flash 镜像，并出现显著的每美元性能差距。

**「对硬件选型的影响」** 对于在 AMD GPU 上运行 DeepSeek v4.1 Flash 的团队，每美元推理性能可能比 H200 低至 1/14.8、比 B200/B300 低至 1/42，意味着同等预算下吞吐量大幅缩水，实际部署会强烈倾向于 NVIDIA 硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/deepseekv4-16t-day-0-to-day-43-performance">DeepSeekV4 1.6T Day 0 to Day 43 Performance Over Time - GB300 NVL72, Huawei, MI355X, B200</a></li>
<li><a href="https://aiweekly.co/alerts/semianalysis-agentx-benchmark-says-cuda-moat-holds-in-agents">SemiAnalysis AgentX benchmark says CUDA moat holds in agents | AI Weekly</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#AMD`, `#DeepSeek`, `#AI hardware`, `#performance`

---

<a id="item-tech-news-9"></a>
### [GitHub 故障影响 Issues、Pages 和 Pull Requests](https://www.githubstatus.com/incidents/0rn90wk115q9) ⭐️ 7.0/10

GitHub 发生了一次影响 Issues、Pages 和 Pull Requests 的故障。官方状态页面在 17:36 更新称，协作平台数据库复制延迟导致系统错误率上升；18:28 更新表示通过内部限流降低了集群负载，但 Pull Requests 功能仍有性能下降；18:44 更新确认问题已解决。该事件说明底层数据库复制问题可能波及多个核心开发者功能，也展示了官方通过限流缓解集群压力的处理过程。

telegram · zaihuapd · 9月13日 09:20

**「背景」** 数据库复制延迟指主数据库与副本之间的同步滞后，可能导致读取旧数据或系统错误率升高。GitHub 的 Issues、Pages 和 Pull Requests 等服务依赖底层数据库，因此复制问题会直接影响这些功能。GitHub Status 是官方发布服务状态和事件进展的页面。

**「影响」** 在故障窗口内，依赖 GitHub Issues、Pages 或 Pull Requests 的开发者可能遇到错误率上升或性能下降，但官方已确认问题解决，用户无需采取额外措施。

**标签**: `#github`, `#outage`, `#incident report`, `#developer tools`, `#platform status`

---

<a id="item-tech-news-10"></a>
### [麒麟 9050 Pro 评测：3D 堆叠提升性能与能效](https://www.bilibili.com/video/BV1HEYv6XETo) ⭐️ 7.0/10

极客湾评测显示，麒麟 9050 Pro 采用微观电路 3D 堆叠，9 核 16 线程 CPU 在 2.75 GHz 同频下较前代功耗降低超 30%，3.1 GHz 峰值频率下功耗未明显增加。马良 955 GPU 的 3DMark 成绩较前代提升近 40%，NPU 实测 INT8 算力为 67.7 TOPS。在 Mate XT 2 上，三款重载手游的整体表现达到骁龙 8 Elite 级别。这些提升显著，但评测认为并非范式转变，且受华为生态限制，全球影响有限。

telegram · zaihuapd · 9月13日 13:22

**「背景」** 麒麟 9050 Pro 是华为用于 Mate XT 2 折叠屏手机的新一代移动 SoC，采用名为 LogicFolding 的微观电路 3D 堆叠技术，搭载 HarmonyOS 7 系统。极客湾 Geekerwan 对该芯片进行了能效实测，相关评测视频已在 YouTube 发布，为理解其性能与功耗表现提供了第三方数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=gQRnAoAdwfA">麒 麟 9050 Pro 能效实测！ 华为Mate XT2性能有多强？ - YouTube</a></li>
<li><a href="https://www.ixbt.com/news/2026/09/12/435253-noveisii-kirin-9050-pro-2-tb-pamiati-ocen-iarkii-ekran-6500-nit-privacy-display-i-novaia-konstrukciia-huawei-mate-xt-2-postupil-v-prodazu-v-kitae.html">Новейший Kirin 9050 Pro , 2 ТБ памяти, очень яркий экран 6500 нит...</a></li>

</ul>
</details>

**标签**: `#Kirin 9050 Pro`, `#3D stacking`, `#mobile SoC`, `#NPU`, `#hardware review`

---

<a id="item-tech-news-11"></a>
### [苹果 OS 27 被曝支持第三方模型接入 Siri](https://x.com/itspdfu/status/2099122424209916015) ⭐️ 7.0/10

爆料称 iOS 27 和 macOS Golden Gate 包含私有 Model Delegation API，应用可通过 App Intents 添加 Siri 扩展并将第三方模型（如 Claude）用作后端。帖子以 Claude 为例，称其可出现在 Siri 的“询问……”菜单中并生成 CSV；涉及设置提醒等系统操作时，Claude 可将请求转回 Siri 执行。相关功能需要私有 entitlement com.apple.developer.model-delegation。该消息来源为非官方账号，能力尚未得到证实。

telegram · zaihuapd · 9月13日 13:48

**「背景」** 根据 MacRumors 论坛讨论，macOS 27 中已出现 \`com.apple.developer.model-delegation\` 这一 entitlement，并有用户展示了让 Claude 处理 Siri 请求的“Ask Claude”功能。App Intents 是苹果允许应用向 Siri 暴露操作能力的框架，而 Model Delegation 可能是在此基础上的新扩展点，使第三方模型能够接收部分请求，并在需要系统操作时转回 Siri 执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forums.macrumors.com/threads/apples-rumored-siri-extensions-quietly-shipped-in-macos-27-i-got-ask-claude-working.2486206/">Apple ’s rumored Siri Extensions quietly shipped in macOS 27 . I got...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Siri`, `#iOS`, `#macOS`, `#third-party AI`, `#API leak`

---

<a id="item-tech-news-12"></a>
### [特朗普拒绝放缓 AI 发展及安全监管呼吁](https://www.ft.com/content/cae60732-f929-4735-a627-db8c14e7c7ed?syn-25a6b1a6=1) ⭐️ 7.0/10

据《金融时报》报道，美国总统特朗普拒绝了科技业高管关于放缓人工智能发展的呼吁，并反对以安全风险为由加强监管。他表示相关担忧受到“非常负面的力量”影响，并强调美国不能在人工智能竞赛中落后于中国。这一表态回应了科技界和民主党要求收紧规则的主张，但报道未提供具体监管或行政措施的细节。

telegram · zaihuapd · 9月14日 00:07

**「背景」** 此前，Anthropic 的 Amodei 等人工智能企业负责人公开呼吁放慢 AI 模型开发速度，OpenAI 的 Altman 和马斯克也公开支持 Amodei 的提议。特朗普在访问爱尔兰时拒绝了这些呼吁，并把 AI 竞赛视为全球主导权的关键考验；民主党人则借其政府抵制监管作为攻击点。这些背景有助于理解其“不能落后于中国”的表态。

**「影响」** 受影响最直接的是美国 AI 开发商和科技业高管：其放缓发展与加强安全监管的诉求未被采纳，联邦政策方向仍以加速发展和与中国竞争为先。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.washingtonpost.com/politics/2026/09/13/trump-rejects-calls-so-slow-ai-development-citing-chinese-competition/">Trump rejects calls to slow AI development, citing Chinese competition - The Washington Post</a></li>
<li><a href="https://www.timesnownews.com/world/us/us-news/whoever-wins-ai-wins-trump-rejects-tech-bosses-call-for-an-ai-slow-down-article-156152473">&#x27;Whoever Wins AI, Wins&#x27;: Trump Rejects Tech Bosses&#x27; Call for an AI Slow Down | Times Now</a></li>
<li><a href="https://world-today-journal.com/trump-rejects-calls-to-slow-ai-development-citing-race-against-china/">Trump Rejects Calls to Slow AI Development, Citing Race Against China - World Today Journal</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#US politics`, `#AI safety`, `#technology regulation`, `#US-China competition`

---