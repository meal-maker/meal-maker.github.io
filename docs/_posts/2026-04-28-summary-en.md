---
layout: default
title: "Horizon Summary: 2026-04-28 (EN)"
date: 2026-04-28
lang: en
---

> From 21 items, 11 important content pieces were selected

---

1. [Microsoft and OpenAI End Exclusive, Revenue-Sharing Deal](#item-1) ⭐️ 9.0/10
2. [Mercor Breach Exposes 4TB of Voice and ID Data of 40K Contractors](#item-2) ⭐️ 8.0/10
3. [SVG Sanitization Woes in Scratch Expose XSS Risks](#item-3) ⭐️ 8.0/10
4. [China Blocks Meta's $2 Billion Acquisition of AI Startup Manus](#item-4) ⭐️ 8.0/10
5. [Super ZSNES Revives Classic Emulator with GPU Power](#item-5) ⭐️ 8.0/10
6. [GitHub Copilot Moves to Usage-Based Billing](#item-6) ⭐️ 8.0/10
7. [OpenClaw Beta v2026.4.25-beta.3 Brings Major TTS and Plugin Upgrades](#item-7) ⭐️ 7.0/10
8. [Easyduino: Open Source KiCad Arduino Devboards](#item-8) ⭐️ 7.0/10
9. [Is My Blue Your Blue? Website Tests Color Perception Boundaries](#item-9) ⭐️ 7.0/10
10. [macOS 27 Mandates TLS 1.2, Alters SMB for Time Machine](#item-10) ⭐️ 7.0/10
11. [Smartphones Steal Disattention: The Value of Staring at Walls](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft and OpenAI End Exclusive, Revenue-Sharing Deal](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai) ⭐️ 9.0/10

Microsoft and OpenAI have agreed to end their exclusive cloud partnership and revenue-sharing arrangement, allowing OpenAI to use other cloud providers such as AWS or Google Cloud. This groundbreaking shift could reshape the AI industry by enabling OpenAI to diversify its infrastructure, intensifying competition among cloud providers and potentially accelerating AI model availability. The deal dissolution follows reports of Microsoft's stake in OpenAI dropping from 49% to 27%, and appears motivated by Microsoft's desire to protect its investment amid rising competition from rivals like Anthropic.

hackernews · helsinkiandrew · Apr 27, 13:22

**Background**: Microsoft and OpenAI entered a multi-billion dollar partnership in 2019, granting Microsoft exclusive rights to host OpenAI's models on Azure and a revenue share. This deal was central to OpenAI's growth and Azure's AI capabilities. However, as OpenAI scaled and sought more flexibility, tensions grew, leading to renegotiation.

**Discussion**: Commenters largely see this as a win for Google and AWS, with many noting OpenAI can now use Google's TPUs. Some question why Microsoft agreed, speculating it was to protect its investment as competition from Anthropic and DeepSeek intensifies. Others see it as a sign that Azure's AI advantage is eroding.

**Tags**: `#Microsoft`, `#OpenAI`, `#AI industry`, `#partnership`, `#cloud computing`

---

<a id="item-2"></a>
## [Mercor Breach Exposes 4TB of Voice and ID Data of 40K Contractors](https://app.oravys.com/blog/mercor-breach-2026) ⭐️ 8.0/10

A data breach at Mercor, an AI hiring startup, resulted in the theft of 4 terabytes of voice samples and ID documents from approximately 40,000 contractors. The stolen data was posted on the Lapsus$ leak site earlier this month, creating a deepfake-ready identity fraud toolkit. This breach is significant because it pairs voice samples with identity documents, enabling attackers to create convincing deepfakes for financial fraud, such as bypassing voiceprint authentication in banking or impersonating victims on video calls. It underscores the irreversible risk of biometric data exposure and the urgent need for data minimization practices. The stolen dataset includes voice recordings and high-resolution scans of government-issued IDs from AI training contractors. Unlike typical breaches that leak only one type of data, this combined dataset provides everything needed to create deepfake audio and video for identity fraud, including banking voiceprint bypass and Arup-style video call scams.

hackernews · Oravys · Apr 27, 09:57

**Background**: Mercor is an AI hiring startup that supplies human experts to train AI models, including through AI-conducted interviews that record voice samples. Many AI companies collect voice data to improve speech recognition and voice cloning technologies, but such biometric data, once leaked, cannot be changed like a password. The concept of 'Datensparsamkeit' (data frugality) highlights the importance of minimizing data collection to reduce breach impact.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mercor">Mercor - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Mercor_AI">Mercor AI</a></li>
<li><a href="https://www.mercor.com/">Mercor | Defining the future of work</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the irony of requiring victims to submit more voice samples for analysis, the practical deepfake threats (e.g., banking voiceprint bypass, Arup-style scams), and the need for data minimization. One commenter suggested labeling biometrics as 'forever passwords' to raise awareness, while another pointed out historical precedents of mass voice data collection.

**Tags**: `#data breach`, `#biometrics`, `#deepfake`, `#privacy`, `#AI safety`

---

<a id="item-3"></a>
## [SVG Sanitization Woes in Scratch Expose XSS Risks](https://muffin.ink/blog/scratch-svg-sanitization/) ⭐️ 8.0/10

A detailed article reveals that Scratch's custom regex-based SVG sanitization has repeatedly failed to prevent cross-site scripting (XSS) attacks, with new bypasses emerging from 2019 to 2026, including HTTP leaks via CSS @import and CSS nesting. This matters because Scratch is a widely-used educational platform with over 100 million users, many of whom are children, making such vulnerabilities a serious safety concern that could allow arbitrary code execution on user projects. The article documents multiple bypasses over years, and the latest post claims every version of Scratch is vulnerable to arbitrary code execution, with the author not following responsible disclosure practices.

hackernews · varun_ch · Apr 27, 15:31

**Background**: SVG (Scalable Vector Graphics) can contain JavaScript and event handlers, making them a vector for XSS if not properly sanitized. Scratch allows users to upload SVGs, and its sanitization used regex, which is notoriously unreliable for parsing SVG due to its complexity. Content Security Policy (CSP) is a more robust defense that can restrict what resources a page can load, but it was not properly implemented in Scratch.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scratch_(programming_language)">Scratch (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Security_Policy">Content Security Policy</a></li>
<li><a href="https://app.daily.dev/posts/the-woes-of-sanitizing-svgs-pwfqj7jvs">The woes of sanitizing SVGs | daily.dev</a></li>

</ul>
</details>

**Discussion**: Community comments praised the article for highlighting CSP as the only credible fix, and suggested using a subset of SVG that excludes dangerous elements. Others criticized Scratch's use of regex sanitization and the lack of responsible disclosure, with one comment noting the author's latest post shows how to exploit the vulnerability in the current version without prior disclosure.

**Tags**: `#SVG`, `#security`, `#XSS`, `#sanitization`, `#Scratch`

---

<a id="item-4"></a>
## [China Blocks Meta's $2 Billion Acquisition of AI Startup Manus](https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html) ⭐️ 8.0/10

China blocked Meta's proposed $2 billion acquisition of the AI startup Manus, citing national security and export control violations, and is now seeking the annulment of the deal that closed in February 2026. This decision marks a significant escalation in China's control over AI technology exports, potentially reshaping global AI merger and acquisition dynamics and setting a precedent for extraterritorial enforcement of China's export control laws. Manus was founded in China but relocated to Singapore after a $75 million fundraising round led by Benchmark in May 2025; China is invoking Article 12 (catch-all clause) and offshore affiliate rules to target the Singapore-based entity, complicating the legal unwinding of a completed deal.

hackernews · yakkomajuri · Apr 27, 11:43

**Background**: Manus develops general-purpose AI agents that can autonomously perform tasks like market research, coding, and data analysis, and gained prominence in early 2025. China's export control laws, including a catch-all clause and offshore affiliate regulations, allow Beijing to assert jurisdiction over Chinese-origin technology even when companies move abroad. This case parallels the TikTok situation, where China argued for control over algorithms developed by Chinese founders.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html">China blocks Meta's $2 billion takeover of AI startup Manus</a></li>

</ul>
</details>

**Discussion**: Community commenters debated the legal basis and implications of China's action, particularly regarding the Singapore relocation. Some argued China is simply applying its own version of export controls, like the US, and that the founders are under investigation, not 'held hostage.' Others noted that breaking Singapore's 'fig leaf' could be problematic for future cross-border tech arrangements.

**Tags**: `#AI`, `#Meta`, `#China`, `#acquisition`, `#geopolitics`

---

<a id="item-5"></a>
## [Super ZSNES Revives Classic Emulator with GPU Power](https://zsnes.com/) ⭐️ 8.0/10

The original developers of ZSNES, zsKnight and _Demo_, have released Super ZSNES, a modern GPU-accelerated version of the classic SNES emulator. It introduces features such as uncompressed audio replacements and enhanced graphics rendering via the GPU. This revival modernizes a beloved emulator from the late 1990s, offering significantly improved performance and accuracy for retro gaming enthusiasts. It also rekindles community interest in SNES emulation and showcases how legacy software can benefit from modern hardware. Super ZSNES offloads PPU (Picture Processing Unit) rendering to the GPU, enabling per-pixel effects and higher resolutions compared to the original software renderer. The emulator also supports replacing compressed audio with high-quality uncompressed samples, a feature that builds on community efforts to track down original sound sources.

hackernews · haunter · Apr 27, 17:50

**Background**: ZSNES is a free and open-source emulator for the Super Nintendo Entertainment System, originally released in the late 1990s and widely used for its speed and compatibility. Its development slowed after the early 2000s, but the original creators have now returned with Super ZSNES, which leverages GPU computing to overcome the emulator's former limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZSNES">ZSNES - Wikipedia</a></li>
<li><a href="https://arstechnica.com/gadgets/2026/04/super-zsnes-is-a-stab-at-a-modern-snes-emulator-from-the-original-developers/">"Super ZSNES" is a stab at a modern SNES emulator from the ...</a></li>
<li><a href="https://zsnes.com/">ZSNES Home Page - About ZSNES</a></li>

</ul>
</details>

**Discussion**: Commenters expressed nostalgia for the original ZSNES and excitement about the GPU-accelerated improvements. Technical discussions centered on the PPU rendering implementation, with one user analyzing whether the emulator renders tile-by-tile or uses per-pixel state. Another user raised the question of legally obtaining ROMs to play on the emulator.

**Tags**: `#emulation`, `#SNES`, `#GPU`, `#retro gaming`, `#ZSNES`

---

<a id="item-6"></a>
## [GitHub Copilot Moves to Usage-Based Billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) ⭐️ 8.0/10

GitHub announced it will transition Copilot from fixed monthly subscriptions to a usage-based billing model, effectively raising costs for heavy users and aligning pricing with API consumption. This change represents a major shift in how developers are charged for AI coding assistance, potentially making Copilot less cost-effective compared to direct API access from providers like OpenAI or Anthropic. Under the new plan, Copilot Pro remains $10/month but includes $10 in monthly AI credits, with model multipliers ranging from 1x to 27x for different models such as GPT and Sonnet or Opus.

hackernews · frizlab · Apr 27, 16:03

**Background**: Previously, GitHub Copilot offered a flat monthly fee for unlimited completions and chat, often allowing heavy users to consume substantial API resources at a fixed cost. The shift to usage-based billing mirrors broader industry trends where AI providers are moving away from fixed subscription models to consumption-based pricing.

**Discussion**: Community comments are largely critical, with many users calculating that the effective price increases are far larger than the stated multipliers, citing examples where heavy Opus usage could see a 50x equivalent increase. Several users are considering switching to pay-as-you-go API providers like OpenRouter or Deepseek, questioning what incentive remains to stay with Copilot.

**Tags**: `#GitHub Copilot`, `#pricing`, `#AI coding assistants`, `#usage-based billing`, `#developer tools`

---

<a id="item-7"></a>
## [OpenClaw Beta v2026.4.25-beta.3 Brings Major TTS and Plugin Upgrades](https://github.com/openclaw/openclaw/releases/tag/v2026.4.25-beta.3) ⭐️ 7.0/10

The v2026.4.25-beta.3 release of OpenClaw adds new TTS providers including Azure Speech, Xiaomi, and ElevenLabs v3, moves plugin startup to a cold persisted registry, expands OpenTelemetry coverage across model calls and tool loops, and enhances browser automation with CDP-native role snapshots and headless launch. These upgrades significantly enhance OpenClaw's voice reply capabilities, plugin reliability, observability, and browser automation, making it a more robust platform for developers building AI-powered conversational agents. Notable technical details include the addition of Azure Speech with SSML escaping and Ogg/Opus output, a new headless browser launch mode, and OpenTelemetry attributes for memory pressure and context assembly.

github · steipete · Apr 26, 13:00

**Background**: OpenClaw is an open-source platform for building conversational AI agents. Text-to-Speech (TTS) converts text into spoken audio, while OpenTelemetry is an observability framework for collecting traces, metrics, and logs. The Chrome DevTools Protocol (CDP) enables low-level browser automation. A cold persisted registry stores plugin metadata persistently, reducing the need to scan manifests at startup.

<details><summary>References</summary>
<ul>
<li><a href="https://opentelemetry.io/docs/what-is-opentelemetry/">What is OpenTelemetry? | OpenTelemetry</a></li>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol - version tot</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#OpenTelemetry`, `#plugin system`, `#browser automation`, `#open-source`

---

<a id="item-8"></a>
## [Easyduino: Open Source KiCad Arduino Devboards](https://github.com/Hanqaqa/Easyduino) ⭐️ 7.0/10

Easyduino is a new open-source GitHub repository that provides KiCad PCB design files for popular microcontroller devboards such as Arduino UNO, Arduino Nano, ESP32, ESP32-S3, Raspberry Pi Pico, and STM32 Bluepill, all converted to KiCad from other EDA tools and enhanced with USB-C and 4-layer stackup. This project fills a significant gap by providing high-quality, open-source KiCad designs for widely used devboards, enabling easier learning, customization, and integration into custom PCBs. It lowers the barrier for makers and professionals to design their own boards based on proven layouts. The designs are unified from original Eagle and Altium files into KiCad, and they incorporate USB-C connectors and a 4-layer copper stackup optimized for JLCPCB fabrication. The repository includes multiple form factors and aims to follow KiCad best practices.

hackernews · Hanqaqa · Apr 27, 17:45

**Background**: KiCad is a free, open-source electronic design automation (EDA) suite used for schematic capture and PCB layout. Development boards like Arduino are pre-built circuit boards with microcontrollers that simplify prototyping of electronic projects. Easyduino provides ready-to-use KiCad project files for these popular devboards, allowing users to modify and manufacture their own customized versions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Hanqaqa/Easyduino">GitHub - Hanqaqa/Easyduino: Eaily dive into different PCB ...</a></li>
<li><a href="https://app.daily.dev/posts/github---hanqaqa-easyduino-easily-dive-into-different-pcb-kicad-designs-of-the-most-popular-microco-cl8faa0hl">GitHub - Hanqaqa/Easyduino: Easily dive into different...</a></li>

</ul>
</details>

**Discussion**: Community members have warmly received Easyduino, praising it as a valuable learning resource that makes designing custom boards more accessible. One user noted that it fills a missing open-source design for commodity devboards, while another shared a personal project improving Arduino UNO. A user also asked for guidance on introducing PCB design to children, indicating the project's educational potential.

**Tags**: `#open-source`, `#KiCad`, `#Arduino`, `#PCB-design`, `#hardware`

---

<a id="item-9"></a>
## [Is My Blue Your Blue? Website Tests Color Perception Boundaries](https://ismy.blue/) ⭐️ 7.0/10

The website 'Is my blue your blue?' (ismy.blue) presents users with a series of color swatches and asks them to decide whether each swatch is blue or green, measuring where each individual draws the boundary between the two colors. The test reveals significant variation in color categorization across users, often correlated with cultural and linguistic backgrounds. This simple interactive tool provides a compelling demonstration of linguistic relativity—the idea that language influences perception—by showing that people disagree on a seemingly basic visual distinction. It has sparked widespread community discussion about individual differences in color vision and the role of cultural naming conventions in shaping how we perceive the world. The test presents a sequence of color swatches transitioning from green to blue and asks users to classify each as either blue or green, then calculates a personal boundary point. Commenters noted that many of the intermediate colors, such as cyan or turquoise, feel neither purely blue nor green, making the forced-choice task frustrating for some users.

hackernews · theogravity · Apr 27, 20:24

**Background**: Color perception is influenced by both biology and language. Research on linguistic relativity has shown that languages differ in how they segment the color spectrum—for example, some languages have a single word for blue and green, while others distinguish multiple shades. The classic work of Berlin and Kay (1969) identified universal patterns in color naming, but subsequent studies reveal that these linguistic categories can subtly shape how speakers perceive color boundaries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linguistic_relativity_and_the_color_naming_debate">Linguistic relativity and the color naming debate - Wikipedia</a></li>
<li><a href="https://www.smithsonianmag.com/science-nature/why-different-languages-name-different-colors-180964945/">The World Has Millions of Colors. Why Do We Only Name a Few?</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.1619666114">Color naming across languages reflects color use | PNAS</a></li>

</ul>
</details>

**Discussion**: Community comments reveal mixed feelings: some users found the test frustrating because intermediate colors like cyan or teal do not fit neatly into a blue/green binary, while others shared personal anecdotes of disagreement with family or friends over color names. A few participants noted that cultural background or monitor calibration might influence results, underscoring the complexity of the phenomenon.

**Tags**: `#color perception`, `#linguistics`, `#human-computer interaction`, `#cognitive science`, `#web app`

---

<a id="item-10"></a>
## [macOS 27 Mandates TLS 1.2, Alters SMB for Time Machine](https://eclecticlight.co/2026/04/23/networking-changes-coming-in-macos-27/) ⭐️ 7.0/10

macOS 27 will require a minimum of TLS 1.2 for network connections and introduce changes to the SMB protocol, which will affect Time Machine backups over the network. These changes enhance security by dropping outdated encryption, but may break compatibility with older servers and NAS devices. Users relying on AFP-based Time Machine backups will need to migrate to SMB, potentially requiring new network configurations. Apple is deprecating AFP (Apple Filing Protocol) for Time Machine backups in favor of SMB. TLS 1.0 and 1.1 will be blocked, which could affect connectivity to legacy web servers and some enterprise services.

hackernews · pvtmert · Apr 27, 15:36

**Background**: TLS (Transport Layer Security) is a cryptographic protocol that secures internet communications; TLS 1.2 has been the standard for years, while earlier versions are considered insecure. SMB (Server Message Block) is a network file sharing protocol used primarily by Windows, but also supported by macOS for accessing shared folders and network drives. AFP has long been Apple's proprietary protocol for file sharing and Time Machine backups over local networks, but Apple is transitioning to SMB for better cross-platform compatibility.

**Discussion**: Community comments indicate mixed reactions: some express frustration with Time Machine's buggy animations, while others recall past Apple networking changes that caused widespread issues. There is also a note that Time Capsule hardware has been unsupported since 2018, and users with AFP-based backups will need to switch to SMB, with one user sharing a guide for building Samba 4 on a Time Capsule.

**Tags**: `#macOS`, `#networking`, `#TLS`, `#SMB`

---

<a id="item-11"></a>
## [Smartphones Steal Disattention: The Value of Staring at Walls](https://www.alexselimov.com/posts/men_who_stare_at_walls/) ⭐️ 6.0/10

An essay argues that smartphones not only capture our focused attention but also eliminate valuable moments of 'disattention'—the unstructured, idle times like staring at a wall that allow the mind to wander, which are essential for creativity and mental reset. For tech professionals who often rely on deep focus, losing disattention may reduce creative problem-solving and mental recovery. This perspective highlights an overlooked cost of constant connectivity, urging a revaluation of unstructured thinking time. The author uses the term 'disattention' to contrast with 'attention', describing it as moments when the mind is not actively engaged. The article resonates strongly on Hacker News (445 points, 202 comments), with many readers sharing personal experiences of staring at walls as a form of mental reset.

hackernews · aselimov3 · Apr 27, 11:08

**Background**: The concept of disattention is related to mind-wandering and daydreaming, which cognitive science has shown to support creativity, memory consolidation, and problem-solving. In an age of constant smartphone notifications, these idle moments are increasingly replaced by passive content consumption or task switching, potentially harming mental well-being and innovative thinking.

**Discussion**: Commenters largely agree with the premise, sharing personal anecdotes about staring at walls as a childhood habit that has been lost. Some compare it to meditation, noting that while meditation is structured focus training, disattention is unstructured and equally valuable. A few humorous comments include a link to an Unsplash photo of a wall for those wanting to try it.

**Tags**: `#attention`, `#digital well-being`, `#meditation`, `#technology and society`, `#mental health`

---