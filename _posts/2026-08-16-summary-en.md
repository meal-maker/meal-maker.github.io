---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 32 items, 8 important content pieces were selected

---

**Technology News**
1. [Anthropic Publishes Claude System Prompts](#item-tech-news-1) ⭐️ 7.0/10
2. [Cloudflare Silently Injects Analytics When Proxy Is Enabled](#item-tech-news-2) ⭐️ 7.0/10
3. [Qwen 3.8 27B Is Excellent but Defaults to Overthinking](#item-tech-news-3) ⭐️ 7.0/10
4. [PJM Grid Modeling Mistake Wasted $12B, Risk of Repeating](#item-tech-news-4) ⭐️ 7.0/10
5. [ECA Paper&\#x27;s Cross-Channel Claim Challenged by k=1 Experiment](#item-tech-news-5) ⭐️ 7.0/10
6. [US Reportedly Asks Allies to Choose Sides in AI Cooperation](#item-tech-news-6) ⭐️ 7.0/10
7. [Claude outage hits Claude.ai, Claude Code, and Claude Cowork](#item-tech-news-7) ⭐️ 7.0/10

**Financial News**
1. [Anthropic&\#x27;s preliminary Q2 revenue tops $11.5 billion, up over 14x](#item-finance-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Anthropic Publishes Claude System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 7.0/10

Anthropic has published the system prompts for its Claude models in the platform documentation release notes, giving developers direct visibility into model instructions and behavior. The release notes cover the system prompts used to shape Claude&\#x27;s responses. Community diff analysis highlights changes between Opus 4.8 and Opus 5, including additions that name Claude Fable 5 and Claude Mythos 5.

hackernews · tosh · Aug 16, 12:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**「What system prompts are」** System prompts are the initial instructions and context injected at the start of every conversation to shape a model&\#x27;s behavior and provide up-to-date information such as the current date. Anthropic&\#x27;s release notes page documents the core system prompts used in the Claude web interface \(claude.ai\) and iOS/Android apps, making versioned prompt changes publicly visible for the first time.

**「Impact」** Developers can now inspect and version-track Claude system prompt changes across model releases, which can help them understand and control model behavior more effectively.

**「Community Discussion」** Simon Willison maintains a git repository that rebuilds the prompts as commit history, and commenters highlight guardrails such as Claude checking whether an uploaded image actually exists; another commenter notes that system prompts are one layer in Anthropic&\#x27;s behavior-shaping stack. One off-topic comment raises a concern about Hacker News moderation of negative AI stories.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/release-notes/system-prompts">System Prompts - Claude Platform Docs - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#System Prompts`, `#Prompt Engineering`

---

<a id="item-tech-news-2"></a>
### [Cloudflare Silently Injects Analytics When Proxy Is Enabled](https://news.ycombinator.com/item?id=49322107) ⭐️ 7.0/10

Cloudflare reportedly injects a JavaScript analytics snippet into sites after users switch nameservers and enable its proxy, rather than opting in. The author, stagas, encountered this on the HTML-only, JS-free site textlog.cc while setting up R2 bucket serving through a subdomain and had to add the site in the Analytics dashboard before disabling the snippet. Additional commenters confirmed the injected module script from static.cloudflareinsights.com/beacon.min.js with a data-cf-beacon token and reported that it occurs only when Cloudflare terminates HTTPS/proxies traffic, not in DNS-only mode. A Cloudflare blog post about &\#x27;RUM diaries&\#x27; enabling web analytics was linked as further technical context. The issue raises privacy and trust concerns for developers using Cloudflare&\#x27;s proxy features.

hackernews · stagas · Aug 16, 17:49

**「Background」** Cloudflare can serve a domain in DNS-only mode or as a reverse proxy \(orange-clouded\). According to Cloudflare&\#x27;s documentation, automatic Web Analytics JavaScript snippet injection is available only when traffic to the domain is proxied through Cloudflare, and Web Analytics is enabled by default for proxied sites that previously used Browser Insights. Community comments in the thread reinforce that DNS-only domains do not receive the injected script.

**「Impact」** Developers enabling Cloudflare&\#x27;s proxy should expect an analytics script unless they disable it in the Analytics dashboard, and can block it with a Content-Security-Policy that restricts script-src. DNS-only mode does not inject the snippet.

**「Community Discussion」** Commenters confirmed the injection, pointed to Cloudflare&\#x27;s RUM diaries blog post, and suggested a Content-Security-Policy with script-src &\#x27;self&\#x27; to block it; several noted the behavior occurs only when Cloudflare is proxying traffic, not in DNS-only mode.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/web-analytics/faq/">FAQs · Cloudflare Web Analytics docs</a></li>
<li><a href="https://developers.cloudflare.com/web-analytics/get-started/">Enabling Cloudflare Web Analytics · Cloudflare Web Analytics docs</a></li>

</ul>
</details>

**Tags**: `#cloudflare`, `#privacy`, `#web-analytics`, `#javascript`, `#dns`

---

<a id="item-tech-news-3"></a>
### [Qwen 3.8 27B Is Excellent but Defaults to Overthinking](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

Simon Willison reports that Alibaba&\#x27;s newly released Qwen 3.8 27B—an Apache 2.0-licensed, vision-capable 27B-parameter LLM—is excellent but defaults to \`xhigh\` reasoning effort, which causes it to overthink even simple requests. On a 128GB M5 Max MacBook Pro, a pelican-riding-a-bicycle SVG generated at that default took 21 minutes and consumed 22,276 reasoning tokens to produce 3,223 output tokens, while the same prompt with reasoning disabled took 137 seconds and produced 3,715 tokens. Qwen&\#x27;s self-reported benchmarks show gains over Qwen 3.6 27B and the closed-weight Qwen 3.7-Plus, but independent benchmark results are still pending. Willison also found the model very good at returning bounding boxes for vision tasks and recommends ignoring the default and starting with low or no reasoning.

rss · Simon Willison · Aug 16, 22:00

**「Background」** Qwen 3.8 27B follows Qwen 3.6 27B, which Willison previously found impressive, and its 27B size plus 17GB Q4\_K\_M quantization makes it feasible on local hardware such as a MacBook Pro or DGX Spark. The model exposes a \`reasoning\_effort\` parameter with \`xhigh\`, \`medium\`, and \`low\` levels, and the default \`xhigh\` is intended only for complex tasks. Willison tested it through LM Studio and \`llama-server\`, initially hitting the default 8,192-token context limit before raising it to the maximum 262,144 tokens.

**「Impact」** For local users, the practical takeaway is to explicitly set reasoning to low or off: the default \`xhigh\` setting caused a 22,276-reasoning-token, 21-minute SVG generation on a high-end MacBook Pro, whereas disabling reasoning cut the same task to 137 seconds.

**Tags**: `#Qwen 3.8 27B`, `#LLM`, `#open source`, `#AI benchmarks`, `#model release`

---

<a id="item-tech-news-4"></a>
### [PJM Grid Modeling Mistake Wasted $12B, Risk of Repeating](https://newsletter.semianalysis.com/p/12b-of-us-ratepayers-money-wasted) ⭐️ 7.0/10

Robert Boswall reports that a grid modeling mistake by PJM wasted $12 billion of US ratepayer money, and PJM may repeat the mistake. The flawed modeling affected electricity market outcomes and is said to put ratepayers at risk by relying on bad models. The available excerpt does not provide specifics on how the models were flawed or which market processes were affected, but the source frames the error as a systemic modeling problem rather than an isolated event.

rss · Semianalysis · Aug 16, 22:27

**「PJM capacity market and 2024 modeling dispute」** PJM operates a capacity market in which modeling assumptions about electricity supply affect costs passed to ratepayers. In 2024, inappropriate assumptions about electricity supply led to a $12 billion cost increase for ratepayers, prompting a complaint that sought to prevent a repeat. A subsequent rule correction aims to avoid repeating that modeling mistake.

**「Impact on PJM ratepayers」** PJM&\#x27;s 67 million customers from Illinois to Virginia face higher electricity costs and reduced reliability because $12 billion was wasted on flawed grid modeling, and the risk of repeating the mistake is heightened by data-center interconnection queues where only about half of requests are credible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ucs.org/about/news/pjm-rule-correction-will-save-ratepayers-billions">PJM Rule Correction Will Save Ratepayers Billions</a></li>
<li><a href="https://www.zerohedge.com/energy/most-two-thirds-power-sought-us-data-centers-will-never-materialize">More Than Two-Thirds Of The Power Sought For US Data Centers ...</a></li>

</ul>
</details>

**Tags**: `#energy grid`, `#electricity markets`, `#modeling`, `#PJM`, `#infrastructure`

---

<a id="item-tech-news-5"></a>
### [ECA Paper&\#x27;s Cross-Channel Claim Challenged by k=1 Experiment](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 7.0/10

A Reddit user re-examined the widely cited Efficient Channel Attention \(ECA\) paper and found that its central claim—cross-channel interaction is a key ingredient—fails a simple ablation. Using 6-piece chess endgame tablebases as a complete, unbiased benchmark, they compared channel gates in a CNN and found ECA with kernel size k=3 reached 96.68% test accuracy while ECA with k=1 reached 96.61%, nearly matching it and beating SE \(96.17%\) and identity \(96.04%\). A center-masked k=3 variant \(\[1,0,1\]\) reached 96.63%, and a per-channel gate reached 96.65%. The author also reviewed official and third-party ECA implementations and found no pure k=1 ablation, with the official MobileNetV2 configuration mixing k=1 and k=3 and timm clamping k≥3. They argue the paper over-tuned k without testing the degenerate no-interaction case and recommend synthetic complete-dataset benchmarks to separate architectural gains from incidental regularization.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**「Background」** Efficient Channel Attention \(ECA\) was introduced in 2019 as a lightweight successor to Squeeze-and-Excitation \(SE\) for CNNs: after global average pooling, it applies a 1D convolution over the channel dimension, avoiding SE&\#x27;s hidden-layer dimensionality reduction. Convolutions are normally justified by locality and translation invariance on data with spatial or temporal topology, but channel indices in a feature map are not guaranteed to have such topology. The original ECA paper reports strong ImageNet results and has accumulated about 12,000 citations, according to the post.

**「Impact」** ML practitioners evaluating ECA-style channel attention should include a pure k=1 baseline in ablation studies, because the post&\#x27;s chess benchmark shows it can nearly match k=3 while using only one parameter per channel gate, challenging the stated cross-channel-interaction rationale.

**Tags**: `#machine learning`, `#attention mechanism`, `#computer vision`, `#convolutional neural networks`, `#research critique`

---

<a id="item-tech-news-6"></a>
### [US Reportedly Asks Allies to Choose Sides in AI Cooperation](https://www.neowin.net/news/us-warns-allied-nations-side-with-us-in-the-ai-race-against-china-or-face-the-consequences/) ⭐️ 7.0/10

The United States is reportedly requiring allied nations and countries seeking AI cooperation with Washington to choose sides, with possible exclusion from the U.S.-led AI alliance if they do not comply. A draft State Department letter states that signing the Pax Silica declaration means joining the alliance and also means participants cannot simultaneously join expected conflicting duplicate initiatives. The report, relayed by Neowin, is based on a draft letter and lacks confirmed details. The move could reshape global AI collaboration and standards by pressuring allies away from rival initiatives, notably in the context of U.S.-China competition.

telegram · zaihuapd · Aug 16, 02:30

**「Background on Pax Silica」** Pax Silica is a U.S.-led State Department initiative focused on securing supply chains for advanced technologies, including semiconductors, artificial intelligence, and rare earth elements. It is promoted as Washington&\#x27;s flagship effort on AI and supply chain security, working to build an economic security consensus among allies and trusted partners. The declaration has already been announced with signatories such as Australia and the U.K., while Singapore is cited as the only Southeast Asian signatory in reports.

**「Impact」** Countries seeking U.S.-led AI collaboration may have to avoid joining initiatives Washington considers conflicting, or risk exclusion from that cooperation, although the policy has not yet been formally confirmed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pax_Silica">Pax Silica - Wikipedia</a></li>
<li><a href="https://www.state.gov/pax-silica">Pax Silica - United States Department of State</a></li>
<li><a href="https://www.indexbox.io/blog/pax-silica-declaration-us-forges-ai-alliance-with-key-allies-singapore-as-sole-southeast-asian-signatory/">Pax Silica Declaration : U . S . AI Pact with Allies ... - IndexBox</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#US-China relations`, `#Pax Silica`, `#AI governance`, `#international cooperation`

---

<a id="item-tech-news-7"></a>
### [Claude outage hits Claude.ai, Claude Code, and Claude Cowork](https://www.ithome.com/0/990/404.htm) ⭐️ 7.0/10

On August 17, Anthropic Claude experienced a major service outage affecting Claude.ai, Claude Code, and Claude Cowork. The incident began around 5:58 Beijing time, and users may have been unable to log in, load pages, or complete requests. Anthropic&\#x27;s status page marked these services as a large-scale service outage, while Claude Console and Claude API remained operational. The cause had not been announced and was still under investigation.

telegram · zaihuapd · Aug 16, 22:49

**「Background」** Anthropic is an AI company whose Claude family includes a web assistant, a developer coding tool, and collaborative services. During an outage, users of the affected frontends can lose access even if backend services like the API and console continue to function normally.

**「Impact」** Users of Claude.ai, Claude Code, and Claude Cowork were unable to log in or use those services during the outage, while Claude Console and Claude API users were not affected.

**Tags**: `#Anthropic`, `#Claude`, `#outage`, `#AI services`, `#incident`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Anthropic&\#x27;s preliminary Q2 revenue tops $11.5 billion, up over 14x](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 8.0/10

Anthropic&\#x27;s preliminary second-quarter revenue rose to more than $11.5 billion from $787 million a year earlier, up over 14 times, and adjusted operating profit turned positive, Bloomberg reported, citing documents.

telegram · zaihuapd · Aug 16, 07:26

**「Background」** The preliminary revenue compares with $787 million in the year-earlier quarter and $4.73 billion in the first quarter of 2026, according to documents viewed by Bloomberg.

<details><summary>References</summary>
<ul>
<li><a href="https://www.whatjobs.com/news/anthropic-preliminary-q2-revenue-tops-11-5-billion/">Anthropic Preliminary Q 2 Revenue Tops $ 11 . 5 Billion</a></li>
<li><a href="https://thenextweb.com/news/anthropic-q2-2026-revenue-11-5-billion-operating-income">Anthropic ’s quarterly revenue passed $ 11 . 5 bn, up more than 14-fold</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#tech industry`

---