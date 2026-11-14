---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 42 items, 10 important content pieces were selected

---

**Technology News**
1. [Scaling a 1T MoE on TorchTitan: 14x Throughput on GH200 GPUs](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI Launches ChatGPT Wallet for Agent Payments](#item-tech-news-2) ⭐️ 8.0/10
3. [FAA Lifted Nationwide Ground Stop at 01:19Z After System Overload](#item-tech-news-3) ⭐️ 7.0/10
4. [Claude Code 2.1.323 Adds Experimental Code Mode](#item-tech-news-4) ⭐️ 7.0/10
5. [Tim Peters, Early Python Contributor and Timsort Author, Dies at 74](#item-tech-news-5) ⭐️ 7.0/10
6. [Microsoft Outlook, Teams, Copilot Global Outage Exceeds 12 Hours](#item-tech-news-6) ⭐️ 7.0/10
7. [DeepSeek Opens All-in-One App API](#item-tech-news-7) ⭐️ 7.0/10

**Financial News**
1. [Cantor Fitzgerald cut reported Nvidia stake by nearly half as Lutnick faced chip-smuggling pressure](#item-finance-news-1) ⭐️ 9.0/10
2. [Chicago Fed&\#x27;s Goolsbee Says Fed Has More Work to Do on Inflation](#item-finance-news-2) ⭐️ 7.0/10
3. [Moonshot AI Restructures to Pave Way for Hong Kong IPO](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Scaling a 1T MoE on TorchTitan: 14x Throughput on GH200 GPUs](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

The authors worked with TorchTitan and PyTorch maintainers to scale a ~1T-parameter Mixture-of-Experts model on 384 GH200 GPUs in the JUPITER supercomputer, reaching about 1,300 tokens/s per GPU—a 14x improvement over their initial baseline. They used 384-way FSDP plus 4-way node-local expert parallelism and skipped pipeline parallelism; the initial 84-second step spent 68 seconds waiting on InfiniBand&\#x27;s ~25 GB/s per GPU. Key optimizations included 64k-token sequences enabled by full activation checkpointing, offloading activations to Grace over the 900 GB/s C2C link, the Muon optimizer, FlexShard whole-expert sharding, and moving Newton-Schulz to GPU to cut the optimizer step from 42 s to ~2 s. Further gains came from attention-cost bucketing \(+13%\), group-limited routing \(+7%\), bf16 expert-gradient all-to-all to halve bytes on the wire, FP8 expert all-gather with blockwise scales \(+18%\), and fixing caching allocator stream segregation to eliminate retries and add 21% throughput. The team notes early routing results may hurt training, so that optimization remains uncertain.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**「Background」** TorchTitan is PyTorch&\#x27;s open-source distributed training framework for large models. Mixture-of-Experts models activate only a subset of expert parameters per token, making them too large for one GPU and requiring sharding strategies such as FSDP \(sharded weights with just-in-time gathering\), expert parallelism \(each GPU owns experts\), or pipeline parallelism. The GH200 superchip combines a Hopper GPU with a Grace CPU connected by a high-bandwidth C2C link, and the JUPITER supercomputer uses these chips with InfiniBand inter-node networking.

**「Impact」** Teams training large MoE models on similar Hopper/InfiniBand clusters can use these techniques to raise throughput from roughly 93 to 1,300 tokens/s per GPU. Group-limited routing may hurt training and needs validation before adoption.

**Tags**: `#TorchTitan`, `#Mixture of Experts`, `#distributed training`, `#GPU optimization`, `#PyTorch`

---

<a id="item-tech-news-2"></a>
### [OpenAI Launches ChatGPT Wallet for Agent Payments](https://openai.com/index/introducing-chatgpt-wallet/) ⭐️ 8.0/10

OpenAI introduced ChatGPT Wallet in partnership with American Express, Mastercard, and Visa to let AI agents make purchases without exposing users&\#x27; real card numbers. Starting today, it is available in the US through dots to ChatGPT Pro subscribers aged 18 and older who use a US-issued card. Users review each item and amount, then confirm the purchase with Face ID or fingerprint. The payment network issues a payment token that replaces the real card number for each transaction. This adds a biometric confirmation step to agent-mediated payments.

telegram · zaihuapd · Nov 13, 15:43

**「Context」** ChatGPT Wallet is OpenAI&\#x27;s agent-mediated payment product, built in partnership with American Express, Mastercard, and Visa, and initially distributed through the dots platform to US ChatGPT Pro subscribers. Tokenized card credentials replace actual card numbers when an AI agent initiates a purchase, and the cardholder must approve each transaction using Face ID or fingerprint. According to CNBC, existing cardholder rewards are retained under this flow.

**「Impact」** Eligible US ChatGPT Pro subscribers with US-issued cards can now allow AI agents to complete tokenized purchases that require per-transaction biometric confirmation.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-wallet/">Introducing ChatGPT Wallet | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/11/13/openai-chatgpt-wallet-dot-purchases.html">OpenAI &#x27;s ChatGPT Wallet allows &#x27; dots &#x27; AI agents to make purchases</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI agents`, `#payments`, `#fintech`, `#security`

---

<a id="item-tech-news-3"></a>
### [FAA Lifted Nationwide Ground Stop at 01:19Z After System Overload](https://www.fly.faa.gov/adv/adv_otherdis?adv_date=11142026&amp;advn=5) ⭐️ 7.0/10

On November 14, 2026, the FAA Command Center lifted a nationwide ground stop at 01:19 UTC \(0119Z\) after a reported incident that temporarily halted flights. The cancellation was announced in an ATCSCC advisory covering event time 01:16–01:30 UTC and effective from 01:19 UTC. According to Secretary Mullin&\#x27;s remarks in a White House briefing, the apparent cause was new equipment and patches overwhelming the older FAA system, illustrating the risks of integrating modern technology with legacy infrastructure. The advisory&\#x27;s reason field was left empty, and no official incident report was available at the time. This incident highlights the operational impact of legacy integration challenges in critical air-traffic-control systems.

hackernews · d3nit · Nov 14, 01:30 · [Discussion](https://news.ycombinator.com/item?id=50492601)

**「Context」** A nationwide ground stop is a rare Federal Aviation Administration order halting all departing flights across the United States because of safety or system failures. The FAA issued such a stop on November 13, 2026, at 20:54 UTC after a communication outage that began in the Chicago area, and the FAA Command Center later cancelled the stop at 01:19 UTC on November 14. This event is formally referred to as the 2026 FAA communication outage and was reported across major news outlets as an unusual disruption to the National Airspace System.

**「Impact」** The nationwide ground stop halted all departing flights in the U.S. for about four hours on November 13, 2026, disrupting thousands of flights and passengers.

**「Community Discussion」** Community comments highlight a White House briefing explanation from Secretary Mullin that new equipment and patches overwhelmed the older system. Others note the FAA advisory&\#x27;s reason field was empty, share early WSJ reporting that the outage may involve an L3Harris telecommunications network, and await the formal incident report.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_FAA_communication_outage">2026 FAA communication outage - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/live/2026/11/13/us/ground-stop-nationwide-flights-faa">Live Updates: FAA Declares Rare Nationwide Ground Stop of ...</a></li>
<li><a href="https://stockanalysis.com/news/faa-nationwide-ground-stop-november-2026/">FAA halts all departing US flights in a rare nationwide ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_FAA_communication_outage">2026 FAA communication outage - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/11/13/faa-ground-stop.html">FAA lifts ground stop after four hours, but flight ... - CNBC</a></li>

</ul>
</details>

**Tags**: `#air-traffic-control`, `#system-outage`, `#legacy-systems`, `#infrastructure`, `#incident-report`

---

<a id="item-tech-news-4"></a>
### [Claude Code 2.1.323 Adds Experimental Code Mode](https://code.claude.com/docs/en/changelog) ⭐️ 7.0/10

Claude Code 2.1.323 was released on November 12 and adds an experimental Code Mode that lets Claude invoke tools using JavaScript; the feature can be disabled for organizations. Plugin management is also stricter: plugins whose declared version ranges do not match will not be installed or updated, and plugin validate now performs type checking on TypeScript hooks. The same release expands .docx document uploads and includes improvements such as a 30-second hook heartbeat.

telegram · zaihuapd · Nov 13, 03:47

**「Background」** Claude Code is Anthropic&\#x27;s AI coding tool that normally calls its tools individually; version 2.1.323 was released on November 12 and bundles over 290 changes, with 20 breaking changes or deprecations according to one third-party count. The new experimental Code Mode changes this interaction by letting Claude write JavaScript to invoke its tools in a single script, and it can be disabled for an organization. Plugin compatibility is enforced through an engines field in plugin.json that specifies the Claude Code version range, and the plugin validate command now type-checks TypeScript hooks.

**「Impact」** Organizations can opt out of the experimental Code Mode, while plugin developers must ensure declared version ranges match or their plugins will be rejected during installation or updates.

<details><summary>References</summary>
<ul>
<li><a href="https://buildapps.co.uk/signals/claude-code-2-1-323-code-mode-plugin-version-ranges/">Claude Code 2.1.323 adds experimental Code Mode and plugin ...</a></li>
<li><a href="https://dev.to/piekwerk/claude-code-21323-pins-plugins-to-version-ranges-what-the-engines-field-enforces-and-6-things-to-13bc">Claude Code 2.1.323 pins plugins to version ranges: what the ...</a></li>
<li><a href="https://claudekit.io/en/updates/claude-code-2-1-323/">Claude Code 2.1.323 — ClaudeKit</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI coding tools`, `#JavaScript`, `#plugin management`, `#Anthropic`

---

<a id="item-tech-news-5"></a>
### [Tim Peters, Early Python Contributor and Timsort Author, Dies at 74](https://x.com/Itsfoss/status/2120957452937998716) ⭐️ 7.0/10

Guido van Rossum announced that Tim Peters, an early Python contributor, has died at age 74. Peters was Python&\#x27;s second real user, authored the Timsort sorting algorithm, wrote the Zen of Python \(PEP 20\), and served on the Python Software Foundation board for 13 years. His work shaped Python&\#x27;s standard library and community philosophy.

telegram · zaihuapd · Nov 13, 09:55

**「Background」** The Zen of Python is a set of 19 guiding principles for Python&\#x27;s design, written by Tim Peters and posted to the Python mailing list in 1999; it is accessible via \`import this\` and was later codified as PEP 20. Peters also designed Timsort, a hybrid sorting algorithm introduced for Python lists in 2002, which was later adopted by Java and Android.

**「Impact」** The Python community loses a foundational contributor whose early design feedback, Timsort algorithm, and Zen of Python shaped the language&\#x27;s philosophy and semantics, leaving a gap in historical and mentoring expertise.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python - Wikipedia</a></li>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Core Development...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50450488">Tim Peters has died | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tim_Peters_%28software_engineer%29">Tim Peters (software engineer) - Wikipedia</a></li>
<li><a href="https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028">In Memoriam: Tim Peters 1952–2026 - Discussions on Python.org</a></li>

</ul>
</details>

**Tags**: `#Python`, `#open source`, `#obituary`, `#software engineering`, `#Timsort`

---

<a id="item-tech-news-6"></a>
### [Microsoft Outlook, Teams, Copilot Global Outage Exceeds 12 Hours](https://www.reuters.com/technology/microsoft-365-outlook-down-thousands-us-users-downdetector-shows-2026-11-12/) ⭐️ 7.0/10

Microsoft Outlook, Teams, and Copilot remained down on November 13 after a global outage lasting more than 12 hours, disrupting business and government communications. Microsoft attributed the issue to a server problem, found no malicious activity, expanded remediation efforts, and reported signs of stabilization. Government agencies in Australia, Japan, and the United States were affected, Euronext experienced email disruption, and some Taiwanese financial institutions reverted to fax for trade confirmation. This is the second Microsoft 365 service interruption this year.

telegram · zaihuapd · Nov 13, 12:21

**「Background」** Microsoft 365 is a cloud-based productivity suite that integrates email \(Outlook\), messaging and collaboration \(Teams\), and AI assistance \(Copilot\). These services are widely used by businesses and government agencies for daily communication, scheduling, document collaboration, and automated workflows. Because they are hosted on Microsoft&\#x27;s servers, service disruptions can quickly propagate across regions and interrupt critical operations.

**「Impact」** The outage disrupted email and collaboration for government agencies and businesses across Australia, Japan, and the US, with Euronext reporting mail delays and some Taiwanese financial firms falling back to fax for trade confirmation.

**Tags**: `#Microsoft`, `#service outage`, `#cloud services`, `#enterprise software`, `#technology industry`

---

<a id="item-tech-news-7"></a>
### [DeepSeek Opens All-in-One App API](https://mp.weixin.qq.com/s/78KBHc4-4N5b2vfL9SkutQ) ⭐️ 7.0/10

DeepSeek has opened an all-in-one application API that lets developers enable capabilities such as deep-thinking search, file input, link reading, and voice conversations within the existing API by turning on corresponding parameters. The server automatically completes tool calling and context concatenation, and the V4.1-Flash model now supports these features across three interfaces. Search, Fetch, OCR, ASR, and TTS can also be called separately. DeepSeek also released an open-source chat demo repository, deepseek-ai/chat-demo, which can be deployed locally and supports importing historical conversations, with a live version available at https://deepseek-ai.github.io/chat-demo/.

telegram · zaihuapd · Nov 13, 14:27

**「Background」** DeepSeek&\#x27;s existing developer API previously covered core model calls; this update adds multimodal and tool-use capabilities without requiring a separate service. The separate endpoints for search, fetching links, OCR, speech recognition, and text-to-speech are standard primitives for building AI assistant applications. The open-source demo enables developers to self-host a frontend similar to DeepSeek&\#x27;s web interface and import prior chat history.

**「Impact」** Developers using DeepSeek&\#x27;s API can now add search, file parsing, OCR, ASR, TTS, and server-managed tool calling to their applications, and can self-host a chat frontend with conversation history import.

**Tags**: `#DeepSeek`, `#API`, `#AI`, `#multimodal`, `#developer-tools`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Cantor Fitzgerald cut reported Nvidia stake by nearly half as Lutnick faced chip-smuggling pressure](https://www.cnbc.com/2026/11/13/howard-lutnick-nvidia-jensen-huang-china-cantor-fitzgerald.html) ⭐️ 9.0/10

CNBC reports that Cantor Fitzgerald, the firm now led by Commerce Secretary Howard Lutnick&\#x27;s sons, cut its reported Nvidia share count by 49%—to 1.78 million by the end of March 2026 from more than 3.5 million in September 2025—while Lutnick faced White House and intelligence pressure over suspected AI-chip smuggling to China and Nvidia CEO Jensen Huang resigned.

rss · CNBC Finance · Nov 13, 23:42

**「Background」** Howard Lutnick left Cantor Fitzgerald to become commerce secretary in February 2025, and the firm has continued arranging billions of dollars in financing for Nvidia&\#x27;s business partners; the article says there is no evidence that his sons had advance knowledge of intelligence concerns or that the share decline was tied to warnings.

**Tags**: `#Nvidia`, `#export controls`, `#conflict of interest`, `#Cantor Fitzgerald`, `#AI chips`

---

<a id="item-finance-news-2"></a>
### [Chicago Fed&\#x27;s Goolsbee Says Fed Has More Work to Do on Inflation](https://www.cnbc.com/2026/11/13/chicago-feds-goolsbee-says-central-bank-has-definitely-got-work-to-do-on-inflation.html) ⭐️ 7.0/10

Chicago Federal Reserve President Austan Goolsbee said the central bank &quot;has definitely got work to do&quot; to restore its inflation credibility after hot PPI and CPI readings, with markets now fully pricing a quarter-point rate increase at the Fed&\#x27;s December 8-9 meeting.

rss · CNBC Finance · Nov 13, 14:22

**「Background」** Inflation has been above the Fed&\#x27;s 2% target for almost six years, and October&\#x27;s producer price index rose 0.3% monthly for a 6.5% annual gain, the highest since November 2022.

**Tags**: `#Federal Reserve`, `#inflation`, `#monetary policy`, `#interest rates`, `#economic data`

---

<a id="item-finance-news-3"></a>
### [Moonshot AI Restructures to Pave Way for Hong Kong IPO](https://www.wsj.com/tech/chinas-moonshot-ai-restructures-to-pave-way-for-ipo-49f09abb) ⭐️ 7.0/10

Moonshot AI is restructuring by moving early investor shares from its Cayman Islands holding company to its main operating entity in China, according to informed sources cited by The Wall Street Journal, a step intended to pave the way for a Hong Kong IPO.

telegram · zaihuapd · Nov 13, 11:29

**「Background」** Moonshot AI, the Beijing-based developer of the Kimi chatbot, had operated through a Cayman Islands holding company and a variable-interest entity \(VIE\) structure, a common setup for foreign investors to hold interests in Chinese internet companies; the company has told shareholders it will unwind that structure to remove regulatory obstacles for its Hong Kong listing.

**「Impact」** Early dollar investors are directly affected: their shares will be transferred from Moonshot AI&\#x27;s Cayman Islands holding company to its China operating entity, removing an offshore layer as the company prepares for a possible Hong Kong IPO.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibase.com/news/28223">Preparations for Hong Kong IPO : Moonshot AI Officially Begins to...</a></li>
<li><a href="https://thenextweb-com.nproxy.org/news/moonshot-ai-vie-unwind-hong-kong-ipo-kimi">$20bn Kimi developer Moonshot abandons VIE structure for HK listing</a></li>
<li><a href="https://www.studioglobal.ai/discover/answers/how-and-why-is-moonshot-ai-restructuring-6a0d754d2ac25e42352959d2">Why Moonshot AI Is Dismantling Its Cayman VIE Structure to ...</a></li>
<li><a href="https://www.wsj.com/tech/chinas-moonshot-ai-restructures-to-pave-way-for-ipo-49f09abb">China’s Moonshot AI Restructures to Pave Way for IPO</a></li>
<li><a href="https://thenextweb.com/news/moonshot-ai-vie-unwind-hong-kong-ipo-kimi">$20bn Kimi developer Moonshot abandons VIE structure ... - TNW</a></li>

</ul>
</details>

**Tags**: `#Moonshot AI`, `#IPO`, `#Hong Kong`, `#corporate restructuring`, `#AI startup`

---