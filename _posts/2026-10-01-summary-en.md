---
layout: default
title: "Horizon Summary: 2026-10-01 (EN)"
date: 2026-10-01
lang: en
---

> From 41 items, 15 important content pieces were selected

---

**Technology News**
1. [Google Announces Gemini 4 Argon Model Release](#item-tech-news-1) ⭐️ 8.0/10
2. [EDG C++ front-end goes public](#item-tech-news-2) ⭐️ 8.0/10
3. [CO₂Jump: Self-Correcting Sampler for Consistent Text-Image Generation](#item-tech-news-3) ⭐️ 8.0/10
4. [DeepSeek Open-Sources Huawei Ascend AI Foundational Components](#item-tech-news-4) ⭐️ 8.0/10
5. [OpenAI Disrupts Model Distillation Attack Tied to Moonshot AI](#item-tech-news-5) ⭐️ 8.0/10
6. [32 Researchers Publish Survey on Modern NLP Tokenization](#item-tech-news-6) ⭐️ 7.0/10
7. [Trump Signs AI Safety Agreement with Six Tech Giants](#item-tech-news-7) ⭐️ 7.0/10
8. [Cloudflare Plans Public Certificate Authority with Post-Quantum MTC by 2027](#item-tech-news-8) ⭐️ 7.0/10
9. [Microsoft Contractors Review Copilot Image Prompts and Outputs](#item-tech-news-9) ⭐️ 7.0/10
10. [Apple Plans October 13 Smart Home Launch](#item-tech-news-10) ⭐️ 7.0/10
11. [Bilibili Releases Open-Source Index-Translate Multilingual Translation Models](#item-tech-news-11) ⭐️ 7.0/10
12. [Reddit to End RSS Feeds and Public API Access](#item-tech-news-12) ⭐️ 7.0/10

**Financial News**
1. [China tightens IPO criteria for humanoid robot startups](#item-finance-news-1) ⭐️ 8.0/10
2. [Kalshi, Polymarket trading volumes questioned amid growth](#item-finance-news-2) ⭐️ 7.0/10
3. [China warns it will respond firmly if EU restricts Chinese businesses](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Google Announces Gemini 4 Argon Model Release](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 8.0/10

Google has announced Gemini 4 Argon, a new major version in its Gemini model family, according to the official blog post. The supplied announcement excerpt does not include concrete technical specifications, benchmark results, or release dates. Google said it will continue gathering feedback from early testers as it iterates on guardrails before making Argon available to developers, enterprises, and consumers as soon as possible. The announcement generated significant developer discussion, with commenters referencing Argon agents working on migrating C/C++ codebases to Rust across Google and noting broader competition among frontier AI labs.

hackernews · bradleyg223 · Sep 30, 20:04 · [Discussion](https://news.ycombinator.com/item?id=49913571)

**「Background」** Gemini 4 Argon is the latest model in Google&\#x27;s Gemini line of frontier AI systems, following earlier releases such as Gemini 3.8 Flash. According to Google, Argon is designed for deep reasoning across complex, long-horizon workflows, with emphasis on real-world coding, enterprise knowledge work, and cyber defense. The model is announced as Google&\#x27;s most advanced yet, rolling out soon, but not immediately available to all developers and consumers.

**「Impact」** Developers and enterprises cannot yet use Gemini 4 Argon because Google has not made it publicly available and has not announced a release date.

**「Community Discussion」** Some commenters reported being unexpectedly impressed by Gemini 3.8 Flash&\#x27;s debugging abilities. Others debated whether AI competition is winner-take-all and recommended making model and provider choices replaceable.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon - The Keyword</a></li>
<li><a href="https://www.cnbc.com/2026/09/30/google-gemini-4-argon-ai.html">Google rolls out Gemini 4 Argon, its most advanced model - CNBC</a></li>
<li><a href="https://9to5google.com/2026/09/30/gemini-4-argon-announcement/">Google announces Gemini 4 Argon as its new frontier model</a></li>

</ul>
</details>

**Tags**: `#artificial-intelligence`, `#machine-learning`, `#gemini`, `#google`, `#model-release`

---

<a id="item-tech-news-2"></a>
### [EDG C++ front-end goes public](https://edgcpp.org/#transition) ⭐️ 8.0/10

The EDG C++ front-end, a historically significant compiler component, has been made public as open source. According to community discussion, the Edison Design Group \(EDG\) company is winding down, which likely prompted the release. The source is available on GitHub under the Apache-2.0 WITH LLVM-exception license. The repository includes commit history dating back to 1990, and the front-end is widely known for being used in Visual C++ IntelliSense.

hackernews · iandinwoodie · Sep 30, 19:26 · [Discussion](https://news.ycombinator.com/item?id=49913192)

**「Background」** Edison Design Group is a company that has developed C++ front-end technology for decades. Its front-end is a component that parses and analyzes C++ source code, and it has been used in major products such as Microsoft Visual C++ IntelliSense. Open-sourcing this component makes its implementation available for inspection and modification.

**「Impact」** Developers and compiler projects can now incorporate or adapt the EDG front-end under the permissive Apache-2.0 WITH LLVM-exception license, potentially improving tooling and language support.

**「Community Discussion」** Commenters emphasized the historical importance of the release, noting the repository preserves commits back to 1990. Some also discussed the possibility of using its source-to-source capabilities to transpile C++ to other languages, though that remains speculative.

**Tags**: `#C++`, `#compiler`, `#open-source`, `#programming-languages`, `#software-engineering`

---

<a id="item-tech-news-3"></a>
### [CO₂Jump: Self-Correcting Sampler for Consistent Text-Image Generation](https://www.reddit.com/r/MachineLearning/comments/1wtyl5m/concurrent_image_understanding_and_generation/) ⭐️ 8.0/10

A NeurIPS 2026 paper from Google, Google DeepMind, and Stony Brook University introduces CO₂Jump, a training-free sampler for consistent concurrent text and image generation. CO₂Jump addresses mismatches where a model describes one solution but draws another by using text confidence and cross-modal attention to guide image updates during sampling. It also allows low-confidence tokens to be masked and regenerated, so earlier decisions can be revised, while requiring only one model forward pass per denoising step. The method was evaluated on image editing, maze solving, and nonograms using new datasets JEdit-1M, JMaze-200K, and JNono-200K. Across 8–512 sampling steps, CO₂Jump was the only compared sampler that improved monotonically on both editing quality and grounding.

reddit · r/MachineLearning · /u/Upstairs\_Theme2785 · Sep 30, 07:28

**「Background」** Concurrent text–image generation can produce inconsistent outputs when the textual answer and generated image are produced in parallel without a mechanism for revision. Markov jump processes model stochastic state transitions over time, and the paper couples these for text tokens and image latents so that low-confidence tokens can be revisited during sampling.

**「Impact」** Researchers and practitioners applying joint text-image models to puzzle solving or image editing can adopt CO₂Jump as a drop-in sampling change to improve joint accuracy and grounding without retraining or extra forward passes.

**Tags**: `#multimodal generation`, `#text-to-image consistency`, `#diffusion models`, `#sampling methods`, `#NeurIPS 2026`

---

<a id="item-tech-news-4"></a>
### [DeepSeek Open-Sources Huawei Ascend AI Foundational Components](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

On September 30, 2026, DeepSeek open-sourced foundational components for Huawei Ascend, including the TileLang high-level language compiler, compute libraries, and distributed communication libraries that correspond to its NVIDIA platform components. The release includes DeepGEMM Ascend, DeepEP Ascend, TileKernels, FlashMLA, and DeepSelect. DeepSeek reported that these components achieved performance near hardware limits in multiple tests. The company is also working with Huawei on a 128-card Ascend 950 supernode solution.

telegram · zaihuapd · Sep 30, 03:09

**「Background」** DeepSeek previously open-sourced low-level AI infrastructure tools for NVIDIA GPUs, and on September 30, 2026, it released Ascend versions of TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, and DeepSelect. Huawei Ascend refers to the company&\#x27;s AI accelerator hardware line; these components provide a high-level kernel programming model, matrix operation and distributed communication libraries, and Huawei detailed a jointly defined 128-card SuperPoD Flex design.

**「Impact」** Huawei Ascend adopters gain an open-source compiler, compute, and communication stack from DeepSeek that is reported to run near hardware limits and supports 128-card Ascend 950 supernodes, reducing dependence on NVIDIA&\#x27;s CUDA ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dqindia.com/news/deepseek-expands-huawei-ascend-push-with-six-open-source-ai-tools-12594158">DeepSeek expands Huawei Ascend push with six open - source AI tools</a></li>
<li><a href="https://www.geopolitechs.org/p/deepseek-builds-for-huawei-ascend">DeepSeek Builds for Huawei Ascend - Geopolitechs</a></li>
<li><a href="https://pandaily.com/deepseek-ascend-infra-oss-tilelang-deepgemm-deepep-superpod-flex">DeepSeek Open - Sources Ascend Versions of TileLang , DeepGEMM ...</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/19580/tilelang-deepseek-huawei-ascend-cuda">DeepSeek and Huawei release TileLang for Ascend chips, taking ...</a></li>
<li><a href="https://news.futunn.com/en/post/1000428379/benchmarking-nvidia-s-cuda-deepseek-has-open-sourced-its-ascend">Benchmarking NVIDIA&#x27;s CUDA! DeepSeek has open-sourced its ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AI-infrastructure`, `#Huawei-Ascend`, `#DeepSeek`, `#distributed-computing`

---

<a id="item-tech-news-5"></a>
### [OpenAI Disrupts Model Distillation Attack Tied to Moonshot AI](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/) ⭐️ 8.0/10

OpenAI says it has disrupted a coordinated model distillation campaign in which attackers manipulated interactions to extract protected reasoning content. According to the source, the activity first appeared in early July 2026, peaked on July 24–25 with more than 16,000 requests from over 4,000 users, and was disrupted for more than 15,000 users before July 28. OpenAI attributed the core activity to individuals associated with Moonshot AI, the developer of Kimi, and has shared information through the Frontier Model Forum and with industry and government partners.

telegram · zaihuapd · Oct 1, 01:18

**「Background」** Model distillation is a technique in which a smaller or student model is trained using outputs from a larger or teacher model. OpenAI describes adversarial distillation as the systematic and unauthorized use of one model&\#x27;s outputs or reasoning to train, reproduce, or improve another model. Moonshot AI is a Chinese AI company best known for developing the Kimi chatbot, and OpenAI says it shared information about the campaign through the Frontier Model Forum and with industry and government partners.

**「Impact」** The action and cross-industry information sharing may increase scrutiny of Moonshot AI-linked personnel and push AI model providers to coordinate more aggressively against unauthorized distillation of reasoning outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/">Disrupting a coordinated model - distillation campaign | OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-disrupts-coordinated-model-reasoning-extraction-campaign/">OpenAI Disrupts Coordinated Model -Reasoning Extraction Campaign</a></li>
<li><a href="https://metallab.ai/en/2026/10/openai-disrupts-model-distillation-campaign">OpenAI says it disrupted Moonshot -linked distillati… — METAL</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#model distillation`, `#OpenAI`, `#Moonshot AI`, `#cybersecurity`

---

<a id="item-tech-news-6"></a>
### [32 Researchers Publish Survey on Modern NLP Tokenization](https://www.reddit.com/r/MachineLearning/comments/1wuccjf/tokenization_a_survey_for_modern_nlp_r/) ⭐️ 7.0/10

A group of 32 tokenizer researchers has published a comprehensive survey of tokenization for modern NLP after about eight months of work. The survey covers tokenization algorithms, evaluation methods, multilinguality, encodings, and theory, as well as alternatives such as latent and visual tokenization. It also examines adjacent topics including constrained generation, token healing, and tokenizer security concerns. The authors describe tokenization as a widely understudied area despite its effects across language modeling. The survey is available on AlphaXiv.

reddit · r/MachineLearning · /u/mcmcmcmcmcmcmcmcmc\_ · Sep 30, 18:13

**「Background」** Tokenization is the initial text-processing step that splits language into units such as words, subwords, or characters. Subword-level tokenization is used in modern NLP models like BERT and GPT because it breaks words into smaller meaningful pieces to handle rare or unknown words. Earlier foundational work recognized tokenization at sentence and word levels, with morphemes as minimal meaningful units.

**「Impact」** NLP and LLM practitioners now have a single reference covering current tokenization methods, evaluation approaches, and alternatives, which may inform model design, evaluation, and research direction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/anagharamadas_tokenization-in-nlp-breaking-down-language-activity-7382751316026167296-QVh9">Learn Tokenization for NLP : A Beginner&#x27;s Guide | LinkedIn</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-981-15-6198-6_18">Study of Various Methods for Tokenization | Springer Nature Link</a></li>

</ul>
</details>

**Tags**: `#tokenization`, `#NLP`, `#language models`, `#survey`, `#machine learning`

---

<a id="item-tech-news-7"></a>
### [Trump Signs AI Safety Agreement with Six Tech Giants](https://www.zaobao.com.sg/news/world/story20260930-9758185) ⭐️ 7.0/10

On September 29, U.S. President Trump and the leaders of Google, Anthropic, Meta, OpenAI, xAI, and Nvidia signed an AI safety agreement and posted the one-page document on Truth Social. Trump described the agreement as morally binding rather than legally binding. The pact requires companies to implement four layers of control: cooperating with external auditors to independently assess AI management systems, establishing independent board oversight committees, and monitoring AI capabilities and alignment for cybersecurity, biological, and chemical threats during model training and deployment. The measures are intended to ensure that these safeguards function as expected.

telegram · zaihuapd · Sep 30, 02:30

**「Background」** Previous AI safety frameworks in the United States have largely been voluntary, with companies agreeing to external audits and board oversight rather than facing statutory requirements. The September 29, 2026 accord follows that model: Reuters calls it a voluntary safety pact, and other reports list the same signatory companies and the four-layer control system.

**「Impact」** The signatory companies are now publicly committed to adopting external audits, independent board committees, and monitoring of cybersecurity, biological, and chemical risks, but enforcement depends on voluntary compliance because the agreement is described as morally rather than legally binding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/legal/government/trump-host-zuckerberg-anthropics-amodei-other-ai-titans-tuesday-2026-09-29/">Trump, AI CEOs sign voluntary safety pact, back data center ...</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/google-anthropic-meta-nvidia-openai-101127588.html?fr=sycsrp_catchall">Google, Anthropic, Meta, Nvidia, OpenAI, xAI Executives Sign ...</a></li>
<li><a href="https://www.firstpost.com/tech/trump-signs-voluntary-ai-safety-accord-with-openai-anthropic-and-4-other-tech-leaders-14049284.html">Trump signs voluntary AI safety accord with OpenAI, Anthropic ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#policy`, `#big tech`, `#artificial intelligence`

---

<a id="item-tech-news-8"></a>
### [Cloudflare Plans Public Certificate Authority with Post-Quantum MTC by 2027](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 7.0/10

Cloudflare has announced plans to become a public certificate authority and has applied to join the Chrome, Apple, Microsoft, and Mozilla root certificate programs. It has signed an agreement with GlobalSign to acquire a widely trusted root certificate, but it is not yet issuing certificates. The new CA will prioritize ACME-based automatic issuance and renewal. Cloudflare also plans to issue production-grade Merkle Tree Certificates \(MTC\) in the first quarter of 2027 to support a post-quantum internet.

telegram · zaihuapd · Sep 30, 06:26

**「Background」** Public certificate authorities issue digital certificates that browsers and operating systems trust by default through embedded root certificates. ACME is a protocol for automating certificate issuance and renewal, used by services like Let&\#x27;s Encrypt. Merkle Tree Certificates are an emerging certificate format intended to support post-quantum use cases.

**「Impact」** For website operators and developers, this could eventually add a Cloudflare-operated ACME-based public CA option; however, no certificates are being issued yet and MTC production is targeted for Q1 2027.

**Tags**: `#Cloudflare`, `#Certificate Authority`, `#PKI`, `#ACME`, `#Post-Quantum Cryptography`

---

<a id="item-tech-news-9"></a>
### [Microsoft Contractors Review Copilot Image Prompts and Outputs](https://www.404media.co/humans-reading-copilot-prompts-images/) ⭐️ 7.0/10

Microsoft has outsourced review of Copilot image generation and editing to hundreds of contractors, meaning user prompts, requests, and uploaded images are not private and can be seen by human evaluators. According to 404 Media and The Verge, these reviewers are exposed to large volumes of disturbing content, including sexually suggestive &quot;upskirt&quot; photos and potentially illegal animal sacrifice imagery. The practice is intended to improve Copilot&\#x27;s image output quality. Workers report severe psychological trauma from the content they must assess. This raises privacy and labor ethics concerns for AI image generation tools.

telegram · zaihuapd · Sep 30, 07:13

**「Background」** Microsoft Copilot includes image-generation and editing features that process user-uploaded images and text prompts. Under Microsoft&\#x27;s consumer terms, a &quot;prompt&quot; is defined broadly to cover text, images, and other inputs, and Microsoft says it may use customer data to improve products and enforce its code of conduct. The practice of having human reviewers inspect AI inputs and outputs is part of quality and safety efforts, but it can create privacy exposure for users and distressing workloads for reviewers.

**「Impact」** Users of Microsoft Copilot&\#x27;s image generation and editing features should not treat their prompts or uploaded images as confidential, because outsourced human reviewers may inspect them.

<details><summary>References</summary>
<ul>
<li><a href="https://tech.yahoo.com/ai/copilot/articles/humans-reading-copilot-prompts-seen-174541565.html">Humans Are Reading Copilot Prompts – What They Have Seen Will ...</a></li>

</ul>
</details>

**Tags**: `#Microsoft Copilot`, `#AI privacy`, `#content moderation`, `#human-in-the-loop`, `#labor ethics`

---

<a id="item-tech-news-10"></a>
### [Apple Plans October 13 Smart Home Launch](https://www.bloomberg.com/news/articles/2026-09-30/apple-is-finally-ready-to-enter-its-next-big-category-the-smart-home) ⭐️ 7.0/10

Apple is reportedly preparing to enter the smart home market on October 13, according to Bloomberg sources. The centerpiece is a J490 hub with an approximately 6-inch screen that can recognize family members by voice or face, display personalized content, and control connected devices. The launch is also expected to include updates to HomePod mini and Apple TV, plus a demonstration of a new Siri AI; Apple has not announced the products and declined to comment.

telegram · zaihuapd · Sep 30, 12:56

**「Background」** Apple’s existing smart-home ecosystem has centered on the HomePod speaker and Apple TV set-top box, both of which serve as HomeKit hubs. The company’s long-delayed push into dedicated smart-home hardware has been anticipated for years, and Bloomberg reports the new lineup will be led by a hub code-named J490, alongside the first new HomePod mini since 2020 and a new Apple TV. The reported October 13 launch would be a critical product expansion for Apple under new Chief Executive Officer John Ternus.

**「Potential impact on Apple users and smart-home competition」** If the reported October 13 launch proceeds, Apple’s J490 hub would give existing HomeKit users a first-party smart-home controller with per-user face and voice recognition and Siri AI, likely increasing competitive pressure on Amazon and Google in the smart-home market.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-09-30/apple-is-finally-ready-to-enter-its-next-big-category-the-smart-home">Apple Is Finally Ready to Enter Its Next Big Category: the Smart Home</a></li>
<li><a href="https://thenextweb.com/news/apple-smart-home-hub-october-13">Apple will launch its smart home push on 13 October , Bloomberg ...</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/apple-plans-make-push-into-smart-home-market-oct-13-bloomberg-news-reports-2026-09-30/">Apple plans to launch new smart-home hub on Oct 13, Bloomberg ...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#smart home`, `#AI`, `#hardware`, `#tech industry`

---

<a id="item-tech-news-11"></a>
### [Bilibili Releases Open-Source Index-Translate Multilingual Translation Models](https://www.ithome.com/1/008/914.htm) ⭐️ 7.0/10

Bilibili&\#x27;s Index LLM team released the Index-Translate multilingual translation model family on September 30. The 2B, 9B, and 35B-A3B \(preview\) text model weights are available on Hugging Face and ModelScope, and the models support 150 languages. Built on Qwen3.5, Index-Translate accepts translation instructions for terminology, format, and preserved content, with extensions to speech, syllable-controlled translation, and long-document translation.

telegram · zaihuapd · Sep 30, 14:08

**「Background」** Qwen3.5 is a multilingual large language model family that can be fine-tuned for specialized tasks such as translation. Hugging Face and ModelScope are public model repositories where researchers can download open weights. Index-Translate adapts Qwen3.5 to translation with instruction-following for formats, terminology, and other constraints.

**「Impact」** Open weights let developers and researchers run or fine-tune translation systems locally for 150 languages using 2B, 9B, or 35B-A3B checkpoints.

**Tags**: `#machine translation`, `#open source`, `#AI models`, `#multilingual NLP`, `#Bilibili`

---

<a id="item-tech-news-12"></a>
### [Reddit to End RSS Feeds and Public API Access](https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/) ⭐️ 7.0/10

Reddit will stop supporting RSS feeds on November 13, 2026, citing their use in large-scale scraping and automated abuse, especially by AI bots. Public API access will be discontinued in March 2027. Third-party app and bot developers must complete registration by January 12, 2027, or lose API access, and the company advises moderators to switch to Discord Relay.

telegram · zaihuapd · Oct 1, 00:27

**「Background」** RSS \(Really Simple Syndication\) is a standardized web feed format that lets users and applications receive updates from a website without visiting it directly. Reddit has historically provided RSS feeds for subreddits and user pages, and its public API has allowed third-party apps, bots, and researchers to programmatically read and post Reddit content. Reddit states that these open channels have become common vectors for large-scale scraping and automation abuse, especially by AI bots, which is driving the shutdown.

**「Impact on developers and RSS users」** Third-party app and bot developers must complete registration by January 12, 2027 to retain API access, while RSS feed consumers will lose access on November 13, 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/">Reddit is killing RSS feeds and ending public API ... | TechCrunch</a></li>
<li><a href="https://techcrunch.com/2026/09/30/reddit-is-killing-rss-feeds-ending-public-api-access-because-of-ai-bots/">Reddit is killing RSS feeds and ending public API access ...</a></li>

</ul>
</details>

**Tags**: `#Reddit`, `#API`, `#RSS`, `#data access`, `#AI bots`

---

## Financial News

<a id="item-finance-news-1"></a>
### [China tightens IPO criteria for humanoid robot startups](https://www.cnbc.com/2026/09/29/china-criteria-humanoid-robot-ipos.html) ⭐️ 8.0/10

China&\#x27;s securities regulator is raising the bar for humanoid robot startups seeking IPOs, requiring sustainable revenue and commercial orders, narrowing losses with a three-year forecast, and core technology such as robotic hands or brains; unnamed sources say only a handful of the more than two dozen applicants may qualify, if any.

rss · CNBC Finance · Sep 30, 02:50

**「Background」** Hong Kong began letting tech companies file confidentially for IPOs in May 2025, and mainland firms seeking Hong Kong listings also need approval from China&\#x27;s securities regulator; that has contributed to at least two dozen humanoid-robot-related &\#x27;embodied AI&\#x27; companies filing in Hong Kong.

**Tags**: `#China`, `#humanoid robots`, `#IPO regulation`, `#AI bubble`, `#CSRC`

---

<a id="item-finance-news-2"></a>
### [Kalshi, Polymarket trading volumes questioned amid growth](https://www.cnbc.com/2026/09/30/kalshi-polymarket-trading-volume-scrutiny.html) ⭐️ 7.0/10

Industry observers are questioning whether trading volumes on Kalshi and Polymarket are inflated after a CNBC analysis found that nearly half of Kalshi&\#x27;s ether perpetual dollar volume on Sept. 20 came from trades sized between $5,495 and $5,505; both companies deny wash trading.

rss · CNBC Finance · Sep 30, 21:09

**「Background」** The scrutiny comes as Polymarket is raising at a valuation above $20 billion and Kalshi is reportedly in talks to raise at a $40 billion valuation, with both companies using surging trading volumes to support those figures.

**「Impact」** If reported volume overstates underlying trading demand, retail investors considering either platform in a possible public listing next year could rely on skewed activity metrics, according to finance professor Andre Guettler.

**Tags**: `#prediction markets`, `#trading volume`, `#wash trading`, `#Kalshi`, `#Polymarket`

---

<a id="item-finance-news-3"></a>
### [China warns it will respond firmly if EU restricts Chinese businesses](https://www.cnbc.com/2026/09/30/china-warns-europe-increases-trade-pressure.html) ⭐️ 7.0/10

China&\#x27;s commerce ministry said late Tuesday it would &quot;respond firmly&quot; if the EU imposes restrictions on Chinese businesses or products during ongoing trade talks, warning such actions would seriously undermine mutual trust and disrupt negotiations. EU Trade Commissioner Maroš Šefčovič has told Beijing it must deliver &quot;concrete results&quot; by October or face &quot;harsher measures.&quot;

rss · CNBC Finance · Sep 30, 03:39

**「Background」** The two sides have been in trade talks this summer as Europe tries to reduce its record trade deficit with China by October, meaning the EU buys much more from China than it sells.

**Tags**: `#China`, `#European Union`, `#trade policy`, `#tariffs`, `#international trade`

---