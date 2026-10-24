---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 33 items, 12 important content pieces were selected

---

**Technology News**
1. [Today, we hacked what we&\#x27;d set out to hack: the iPhone](#item-tech-news-1) ⭐️ 8.0/10
2. [Moonshot AI Releases Kimi K3.1 Pro and Highspeed](#item-tech-news-2) ⭐️ 7.0/10
3. [Dessa Claims Most Authentic Full-Duplex Speech Model with Local Inference](#item-tech-news-3) ⭐️ 7.0/10
4. [Google may use Gmail and Photos data for ads if services are linked](#item-tech-news-4) ⭐️ 7.0/10
5. [Amazon&\#x27;s Trainium Challenges Incumbent AI Training Hardware](#item-tech-news-5) ⭐️ 7.0/10
6. [Exact Equivalence Derived Between Swarm Imitation and Multi-Armed Bandit RL](#item-tech-news-6) ⭐️ 7.0/10
7. [ByteDance Releases Seedance 2.5 4K Enterprise Video Model](#item-tech-news-7) ⭐️ 7.0/10
8. [PHP Foundation Recommends Disabling Upload Progress Feature](#item-tech-news-8) ⭐️ 7.0/10

**Financial News**
1. [State Council Issues Guidelines to Slow AI-Driven Job Replacement](#item-finance-news-1) ⭐️ 8.0/10
2. [EU Ends 84.2% Anti-Dumping and Countervailing Duties on Chinese Solar Glass](#item-finance-news-2) ⭐️ 7.0/10
3. [China tightens compulsory product certification for e-bikes, toys, strollers from Nov 2026](#item-finance-news-3) ⭐️ 7.0/10
4. [CSRC approves wholly foreign-owned Citigroup Securities](#item-finance-news-4) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Today, we hacked what we&\#x27;d set out to hack: the iPhone](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

A technical write-up from calif.io claims successful iPhone hacking, presenting multiple exploit demos that appear to use novel exploit chains. The post reports achieving the stated goal of compromising the iPhone, but the available source content does not provide specific iOS versions, exploit details, or affected models. Community discussion focuses on the implications for iOS security, the impact of Apple&\#x27;s ecosystem and jailbreak detection, and questions about whether Lockdown Mode would mitigate such attacks. Some commenters also express concern that advanced security models and red-team tools are restricted to a small inner circle, limiting independent verification.

hackernews · pavel\_lishin · Oct 23, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50211474)

**「Background」** Security researchers often present iOS vulnerability discoveries at conferences like Hexacon, where the source item&\#x27;s demos were revealed. Jailbreaking involves bypassing Apple&\#x27;s software restrictions to gain root access on iPhones, a long-standing interest among tinkerers. Apple&\#x27;s optional Lockdown Mode is designed to reduce the attack surface for users at high risk of targeted attacks, but its effectiveness against specific exploit chains is a recurring question.

**「Impact on users」** For high-risk iPhone users, updating iOS and enabling Lockdown Mode is recommended because independent security researchers have confirmed its effectiveness against similar exploit chains.

**「Community Discussion」** Comments express frustration with Apple&\#x27;s control over jailbroken devices and limited access to advanced security models, while some ask whether Lockdown Mode would block the exploits and whether root access could be retained without Apple disabling updates.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/iphone">Today , we hacked what we &#x27; d set out to hack : the iPhone .</a></li>
<li><a href="https://www.linkedin.com/posts/rswebsols_gadget-rswebsols-activity-7440845971808460800-X_Pz">Apple Blocks DarkSword iPhone Spyware with Security ... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#iPhone`, `#security`, `#jailbreak`, `#exploit`, `#iOS`

---

<a id="item-tech-news-2"></a>
### [Moonshot AI Releases Kimi K3.1 Pro and Highspeed](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 7.0/10

Moonshot AI announced Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed, two new open-weight models. The release includes an explicit policy on cyber capabilities: the company says it will not initially release open weights that extend the absolute frontier of offensive cyber capability, and K3.1 Pro&\#x27;s offensive cyber capability is by design below what its pipeline can produce and behind frontier proprietary models. Moonshot AI also states it intends to progressively raise the cyber capability available in open weights over time. The announcement links to model documentation and third-party evaluation pages but does not include detailed technical benchmarks in the provided source content.

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**「Context: Moonshot AI and the Kimi K3 model family」** Moonshot AI&\#x27;s prior release, Kimi K3, is a 2.8-trillion-parameter open-weight multimodal reasoning model with a 1-million-token context window, built on Kimi Delta Attention \(KDA\) and Attention Residuals \(AttnRes\). Open-weight models publish their parameters so others can run or adapt them, and Moonshot AI positions Kimi K3 as its most capable model to date with native vision and agentic behavior. Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed are successor releases in this family, introduced with explicit statements about not releasing open weights that would extend the frontier of offensive cyber capability.

**「Impact」** For developers and researchers, the open-weight release provides access to the model family, but the deliberate cap on offensive cyber capability means it is positioned below frontier proprietary models for those tasks, with future releases expected to increase capability.

**「Community Discussion」** Community reactions highlight mixed experiences: some users note blunt or inconsistent model identity and confusing reasoning traces, while others report restrictive subscription rate limits \(hitting a 5-hour quota in 47 minutes on the $99 plan\). Another commenter questions the cyber capability policy, and a benchmark report shows improved accuracy but high tool-call overhead compared to other models.

<details><summary>References</summary>
<ul>
<li><a href="https://k3-kimi.com/">Kimi K3: 2.8T Open - Weight Model — Benchmarks , Pricing &amp; Guides</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open weights`, `#Moonshot AI`, `#model release`

---

<a id="item-tech-news-3"></a>
### [Dessa Claims Most Authentic Full-Duplex Speech Model with Local Inference](https://block.xyz/dessa) ⭐️ 7.0/10

The item introduces Dessa as a full-duplex speech model claimed to achieve expressive, low-latency conversation and to run locally on a MacBook Pro M4 Max or better. Its creators also state that Dessa was trained on only one NVIDIA GB200 NVL72. The accompanying &\#x27;most authentic ever&\#x27; description is unverified marketing language, and the available technical detail is limited. No primary source content was provided for verification beyond these claims.

hackernews · dsr12 · Oct 23, 19:09 · [Discussion](https://news.ycombinator.com/item?id=50213925)

**「Full-duplex speech context」** Full-duplex speech models process incoming audio and generate spoken responses at the same time, unlike turn-based assistants that wait for a speaker to stop. Recent open-source work such as MultiTalk has pushed end-to-end full-duplex systems forward but still notes limitations in long-context robustness and multi-party interaction. Dessa enters this field with claims of expressive low-latency output, local inference on a MacBook Pro M4 Max, and training on a single NVIDIA GB200 NVL72.

**「Community Discussion」** Several commenters found the demo tracks and local low-latency claims technically impressive, with one calling the MacBook Pro M4 Max claim a &\#x27;holy shit&\#x27; moment. Others criticized the sensationalist &\#x27;most authentic&\#x27; title as marketing and found the simulated empathetic conversation &\#x27;cringe worthy&\#x27; rather than useful.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2609.36903">MultiTalk: Scaling Full - Duplex Speech Models to Long... | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#speech-ai`, `#full-duplex`, `#on-device-inference`, `#model-training`, `#ai`

---

<a id="item-tech-news-4"></a>
### [Google may use Gmail and Photos data for ads if services are linked](https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update) ⭐️ 7.0/10

Google is updating its privacy policy to state that it may use data from Gmail and Google Photos for personalized advertising when users choose to link certain Google services. This change is conditional: the data will not be used for ads unless users opt into linking that makes the data available to ad-supported services. The update does not mean automatic use of Gmail or Photos data for ad targeting, but it expands the circumstances under which that data could be used.

hackernews · JustSkyfall · Oct 23, 19:34 · [Discussion](https://news.ycombinator.com/item?id=50214218)

**「Context: DMA and linked Google services」** The Digital Markets Act \(DMA\) is an EU law effective March 6, 2024, whose Article 5\(2\) requires Google to offer EU users a choice about linking certain Google services such as Search, YouTube, Ads, Play, Chrome, Shopping, and Maps. When users choose to link Gmail or Google Photos with ad services, Google may then use data from those services for personalized ads; if they do not link them, that data cannot be used for ads. This opt-in linking model is the basis for Google&\#x27;s updated privacy policy language.

**「Impact」** Users who link Gmail or Google Photos with other Google services may have their data used for personalized ads unless they avoid linking or adjust their settings.

**「Community Discussion」** Comments reflect skepticism that &quot;might&quot; will become &quot;absolutely will,&quot; while others note the policy only applies when users actively link services, and some recommend leaving Google Photos or disabling personalization.

**Tags**: `#privacy`, `#google`, `#advertising`, `#data-policy`, `#gmail`

---

<a id="item-tech-news-5"></a>
### [Amazon&\#x27;s Trainium Challenges Incumbent AI Training Hardware](https://newsletter.semianalysis.com/p/amazons-trainium-takes-a-strike-at) ⭐️ 7.0/10

Amazon&\#x27;s Trainium, previously regarded as best suited for inference, is now positioned as a viable option for AI training workloads, according to a SemiAnalysis article by Kimbo Chen. The analysis highlights native PyTorch support on Trainium, high-quality CI infrastructure, integration with TorchTitan, and a profiler described as enabling tasks that are &\#x27;GPU Impossible.&\#x27; These capabilities challenge incumbent training hardware by providing practitioners with advanced tooling. The article frames this as an expanded role rather than a definitive breakthrough, with no quantitative performance data provided.

rss · Semianalysis · Oct 23, 19:06

**「Background」** AWS Trainium is Amazon&\#x27;s purpose-built AI accelerator for training and inference workloads, offering high performance and cost economics according to AWS. TorchNeuron integrates PyTorch with Trainium chips, providing a standard path for scaling model training using Fully Sharded Data Parallelism \(FSDP\). TorchTitan is a PyTorch native platform for rapid experimentation and large-scale training of generative AI models, serving as a flexible foundation for developers.

**「Impact」** AI practitioners evaluating alternatives to dominant training hardware can now consider Trainium for training with native PyTorch tooling, though its competitive position is not yet proven.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai">Amazon &#x27;s TorchNeuron runs PyTorch on AWS Trainium chips</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS | Amazon Web Services, Inc.</a></li>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch / torchtitan : A PyTorch native platform for training ...</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#Amazon Trainium`, `#PyTorch`, `#machine learning infrastructure`, `#AI training`

---

<a id="item-tech-news-6"></a>
### [Exact Equivalence Derived Between Swarm Imitation and Multi-Armed Bandit RL](https://www.reddit.com/r/MachineLearning/comments/1xdhf7r/r_the_hive_mind_is_a_single_reinforcement/) ⭐️ 7.0/10

Researchers prove a mathematical equivalence between decentralized social imitation and single-agent reinforcement learning in multi-armed bandits. Treating the fraction of individuals committed to each option as the macro-agent&\#x27;s action-probability policy, they use evolutionary replicator dynamics to show that a population using &\#x27;imitation of success&\#x27; evolves identically to the expected update of the Cross Learning bandit algorithm. Extending this to the honey bee waggle dance&\#x27;s weighted voter model yields a new macro-level algorithm called Maynard-Cross Learning \(MCL\). Under this duality, N non-learning individuals act as N parallel environment rollouts, with an effective per-sample step size of alpha=1/N. The work appears in arXiv:2410.17517 and includes code and a project page.

reddit · r/MachineLearning · /u/mistlab · Oct 23, 15:37

**「Background」** Multi-armed bandits are a reinforcement-learning setting in which an agent repeatedly chooses among options and updates its action probabilities from scalar reward feedback; Cross Learning is a classic bandit algorithm that increases the probability of the chosen action in proportion to the received reward and decreases unchosen actions accordingly. Honeybee nest-site selection is often modeled by the weighted voter model: scouting bees advertise sites for a duration proportional to quality, and undecided bees blindly adopt the first advertised option they encounter. The authors connect these settings through evolutionary replicator dynamics, which describe how the proportion of a population using each strategy changes under imitation.

**「Research impact」** For reinforcement-learning and swarm-intelligence researchers, the exact equivalence and the new Maynard-Cross Learning algorithm offer a formal way to analyze collective imitation as single-agent multi-armed-bandit RL with an effective learning rate of 1/N, and the authors suggest this could enable transferring RL analysis tools to social and economic dynamics as well as guiding decentralized swarm robotics design.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent</a></li>
<li><a href="https://www.alphaxiv.org/abs/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent | alphaXiv</a></li>
<li><a href="https://www.alphaxiv.org/abs/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent | alphaXiv</a></li>
<li><a href="https://arxiv.org/html/2410.17517">The Hive Mind is a Single Reinforcement Learning Agent</a></li>
<li><a href="https://www.linkedin.com/posts/abdullahrasheed-_swarmintelligence-reinforcementlearning-complexsystems-activity-7401410631842725888-e25c">Swarm Intelligence Redefined: Collective Learning as... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#multi-armed bandits`, `#swarm intelligence`, `#collective decision-making`, `#theoretical machine learning`

---

<a id="item-tech-news-7"></a>
### [ByteDance Releases Seedance 2.5 4K Enterprise Video Model](https://mp.weixin.qq.com/s/yUa8oh-IWfl5lDQzGSKWeg) ⭐️ 7.0/10

ByteDance&\#x27;s Volcano Engine has released Seedance 2.5 4K, described as the strongest version in the Seedance series, with specialized training that improves learning of facial expressions, subtle movements, and image details. The model supports a Draft mode that generates 480P previews for rapid storyboard validation before producing final 4K footage, balancing creative exploration and visual quality. It features 10-bit color depth for rich color gradation and smooth transitions, making the footage suitable for large-screen presentation. In film and television dialogue tests, the 4K version demonstrated more nuanced reactions and layered performances from characters. The model is currently available only to select enterprise customers for trial, with broader access expected to expand gradually.

telegram · zaihuapd · Oct 23, 08:27

**「Background: Seedance video model lineage」** Seedance is ByteDance&\#x27;s video generation model series; the earlier Seedance 2.0 supported synchronized audio and video generation with cinematic camera movement and output up to 1080p. Seedance 2.5 builds on this foundation, and community libraries already collect example prompts and outputs for Seedance 2.5.

<details><summary>References</summary>
<ul>
<li><a href="https://renoise.ai/showcase/awesome-seedance-2-5-prompts">Seedance 2 . 5 Prompts — Community Library (2026) | Renoise</a></li>
<li><a href="https://imagetopsd.ai/zh/models/seedance-2-0">Seedance 2 .0 视频生成器：画面和声音一起出 | ImageToPsd.AI</a></li>

</ul>
</details>

**Tags**: `#AI video generation`, `#ByteDance`, `#Seedance`, `#4K model`, `#machine learning`

---

<a id="item-tech-news-8"></a>
### [PHP Foundation Recommends Disabling Upload Progress Feature](https://x.com/ThePHPF/status/2113580383875019242) ⭐️ 7.0/10

The PHP Foundation has advised users to set session.upload\_progress.enabled to 0 until the next PHP release to mitigate a remote code execution vulnerability tracked as CVE-2026-115560. Only applications that switch a non-default serialize\_handler to &quot;php&quot; at runtime may be affected. The Foundation previously recommended keeping this feature disabled in connection with CVE-2026-109619.

telegram · zaihuapd · Oct 23, 13:46

**「Background」** PHP&\#x27;s session.upload\_progress.enabled option enables tracking of file upload progress in session data. The serialize\_handler setting determines how session data is encoded; under certain runtime configurations, switching to the &quot;php&quot; handler can create unsafe conditions.

**「Impact」** Applications that switch a non-default serialize\_handler to &quot;php&quot; at runtime should disable session.upload\_progress.enabled immediately to avoid potential remote code execution until an official fix is released in the next PHP version.

**Tags**: `#PHP`, `#security`, `#vulnerability`, `#RCE`, `#web development`

---

## Financial News

<a id="item-finance-news-1"></a>
### [State Council Issues Guidelines to Slow AI-Driven Job Replacement](https://mp.weixin.qq.com/s/St8URoMYcV-voM7kLAK3Bw) ⭐️ 8.0/10

China&\#x27;s State Council General Office issued guidelines to reduce employment displacement from artificial intelligence. The policy prioritizes AI adoption in labor-shortage and high-risk positions, urges a cautious pace in labor-intensive industries, and encourages companies to create unemployment buffer periods with advance notice and retraining support.

telegram · zaihuapd · Oct 23, 12:54

**「Background」** The State Council General Office&\#x27;s &\#x27;Opinions on Adapting to AI Technology Development and Helping Build an Employment-Friendly Development Model&\#x27; is a policy guidance document that directs government agencies and enterprises to balance AI adoption with protections for affected workers.

**「Impact」** The policy&\#x27;s call for advance notice, unemployment buffer periods, and retraining could shift adjustment costs onto employers in labor-intensive industries, slowing AI adoption there while giving at-risk workers more time to transition.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workercn.cn/papers/grrb/2026/07/13/7/grrb202607137.pdf">grrb0720260713B</a></li>

</ul>
</details>

**Tags**: `#人工智能`, `#就业政策`, `#劳动市场`, `#国务院办公厅`, `#科技治理`

---

<a id="item-finance-news-2"></a>
### [EU Ends 84.2% Anti-Dumping and Countervailing Duties on Chinese Solar Glass](https://www.163.com/dy/article/L9R94K6105484D40.html) ⭐️ 7.0/10

The EU Commission announced on 21 October 2026 that it has terminated the 84.2% anti-dumping and countervailing duty on Chinese solar glass, effective 22 October 2026; duties paid since 22 July 2025 may be refunded without interest.

telegram · zaihuapd · Oct 23, 06:54

**「Background」** The EU had imposed anti-dumping and countervailing duties of up to 84.2% on Chinese solar glass, but the Commission now says there are no active EU producers and Chinese imports have fallen to about 3% of the EU market, down from 30.5% during the original investigation.

**Tags**: `#trade policy`, `#solar glass`, `#China-EU trade`, `#tariffs`, `#renewable energy`

---

<a id="item-finance-news-3"></a>
### [China tightens compulsory product certification for e-bikes, toys, strollers from Nov 2026](https://www.gelonghui.com/live/2726360) ⭐️ 7.0/10

China&\#x27;s market regulator will tighten compulsory product certification \(CCC\) rules for electric bicycles, toys, and strollers from November 1, 2026, requiring e-bikes to follow &\#x27;one vehicle, one battery, one charger, one code&\#x27; and be delivered with all essential parts and a conformity certificate.

telegram · zaihuapd · Oct 23, 10:12

**「Background」** The State Administration for Market Regulation is the government body that administers China Compulsory Certification \(CCC\), a mandatory product-safety certification for certain goods sold in China.

**「Impact」** Manufacturers of these products will face additional sample-retention and post-certification inspection duties under the new rules.

**Tags**: `#China`, `#regulation`, `#CCC certification`, `#electric bicycles`, `#product safety`

---

<a id="item-finance-news-4"></a>
### [CSRC approves wholly foreign-owned Citigroup Securities](https://mp.weixin.qq.com/s/f_fCJUEObewqgAe5Ie7wHA) ⭐️ 7.0/10

China&\#x27;s securities regulator approved the establishment of Citigroup Securities \(China\) Co., Ltd., a wholly foreign-owned securities firm in Shanghai with RMB 1.2 billion in registered capital and a business scope covering securities brokerage, investment consulting, underwriting and sponsorship, and proprietary trading.

telegram · zaihuapd · Oct 23, 12:29

**「Background」** Before granting the approval, China&\#x27;s securities regulator had asked Citigroup Global Markets Holdings Inc. to provide additional details on its main shareholder&\#x27;s financial condition and long-term credit ratings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lanjinger.com/d/227503">lanjinger.com/d/227503</a></li>

</ul>
</details>

**Tags**: `#China`, `#securities regulation`, `#foreign investment`, `#Citigroup`, `#market access`

---