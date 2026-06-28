---
layout: default
title: "Horizon Summary: 2026-06-22 (EN)"
date: 2026-06-22
lang: en
---

> From 23 items, 8 important content pieces were selected

---

1. [Anthropic mandates identity verification for Claude users](#item-1) ⭐️ 8.0/10
2. [Prefer duplication over the wrong abstraction](#item-2) ⭐️ 8.0/10
3. [Did My Old Job Exist Only Because of Fraud?](#item-3) ⭐️ 7.0/10
4. [Defining the smallest saleable piece of software](#item-4) ⭐️ 7.0/10
5. [AI-Driven Paradigm Shift in Software Engineering Introduced](#item-5) ⭐️ 7.0/10
6. [JSON-LD Guide for Personal Websites](#item-6) ⭐️ 6.0/10
7. [How LLMs Actually Work: A Beginner's Guide](#item-7) ⭐️ 6.0/10
8. [Go AMD64 Microarchitecture Levels Performance Impact](#item-8) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic mandates identity verification for Claude users](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) ⭐️ 8.0/10

Anthropic has introduced an identity verification requirement for accessing Claude, requiring users to submit government-issued IDs for processing by a third-party service, Persona. This policy change, likely driven by US export controls on AI models, restricts international access and raises significant privacy concerns, potentially reshaping the global AI market. Anthropic states that identity data will not be used to train its models, but the third-party provider Persona may use the data to improve its fraud prevention systems.

hackernews · bathory · Jun 21, 12:44

**Background**: The US government has imposed export controls on advanced AI models and chips to prevent adversaries like China from accessing cutting-edge technology. In January 2026, the Commerce Department ordered Anthropic to cut off access to its latest models for non-US citizens, prompting identity verification measures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>
<li><a href="https://cepa.org/article/us-ai-export-controls-cause-furor/">US AI Export Controls Cause Furor - CEPA</a></li>
<li><a href="https://www.sidley.com/en/insights/newsupdates/2025/01/new-us-export-controls-on-advanced-computing-items-and-artificial-intelligence-model-weights">New U.S. Export Controls on Advanced Computing Items and Artificial Intelligence Model Weights: Seven Key Takeaways | Insights | Sidley Austin LLP</a></li>

</ul>
</details>

**Discussion**: Commenters express frustration that US export controls are harming international users and creating a viable alternative market for non-US AI models. Some note that this help page has existed since April and is not new, while others compare Anthropic's process to OpenAI's similar identity checks.

**Tags**: `#identity-verification`, `#AI-regulation`, `#Claude`, `#Anthropic`, `#privacy`

---

<a id="item-2"></a>
## [Prefer duplication over the wrong abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction) ⭐️ 8.0/10

Sandi Metz's 2016 blog post 'The Wrong Abstraction' argues that when an abstraction is found to be incorrect, developers should reintroduce duplication and let the code reveal a better design, rather than forcing a flawed abstraction. This principle directly challenges the common over‑emphasis on avoiding duplication at all costs, offering a pragmatic guideline that can reduce long‑term maintenance complexity in software projects and prevent rigid, hard‑to‑change architectures. Metz suggests that the best time to introduce an abstraction is when you have at least three examples of similar code—a rule often called the 'Rule of Three'—and that prematurely abstracting from only two instances often leads to the wrong abstraction.

hackernews · rafaepta · Jun 21, 16:08

**Background**: In software engineering, abstraction is a technique to hide complexity and reuse logic, but creating a shared abstraction too early—before fully understanding the domain—can force future code into an unnatural shape. Sandi Metz is a well‑known author of 'Practical Object‑Oriented Design in Ruby' (POODR), and her article strongly influenced the 'prefer duplication over the wrong abstraction' meme on Hacker News and in programming communities. The discussion often contrasts the 'Single Source of Truth' principle, which demands that every piece of knowledge live in exactly one place, against the risk of locking in a bad abstraction.

<details><summary>References</summary>
<ul>
<li><a href="https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction">The Wrong Abstraction - Sandi Metz</a></li>
<li><a href="https://news.ycombinator.com/item?id=48620090">Prefer duplication over the wrong abstraction (2016) - Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with Metz's advice, with many sharing personal examples where premature abstraction caused more harm than duplication. Some emphasize that duplication is acceptable only when it does not violate a true 'single source of truth'—for instance, when the duplicated logic would be a bug if it diverged, then refactoring is still necessary. Others note that functional programming and duck‑typed interfaces can reduce the occurrence of duplication altogether, shifting the debate toward data structure abstractions.

**Tags**: `#software-engineering`, `#abstraction`, `#code-duplication`, `#refactoring`, `#programming-principles`

---

<a id="item-3"></a>
## [Did My Old Job Exist Only Because of Fraud?](https://david.newgas.net/did-my-old-job-only-exist-because-of-fraud/) ⭐️ 7.0/10

A personal reflection article examines whether the author's previous software engineering role was sustained by corporate fraud, supported by community anecdotes of billing fraud and wasteful contractor churn. This discussion highlights a widespread culture of fraud and mismanagement in the tech industry, raising uncomfortable questions about the legitimacy of many jobs and the ethical responsibilities of engineers. Commenters describe practices such as fraudulent billing of hours on government projects, contractor rehiring at inflated rates through outsourcing, and whole companies running as intentional losses for tax purposes.

hackernews · advisedwang · Jun 21, 21:40

**Background**: The tech industry has long faced criticism for inefficiency and waste, with many roles perceived as 'bullshit jobs'—positions with little real value. This article adds a darker dimension by suggesting that some jobs may exist primarily because of fraudulent activity, from padded billing to outright deception at the executive level.

**Discussion**: The community comments share real-world experiences that validate the author's suspicion. Examples include a manager editing billing entries on a government contract, contractor markup schemes at a large bank, and an executive convicted of massive fraud at WorldCom. The sentiment is one of resignation and confirmation that such practices are common.

**Tags**: `#corporate fraud`, `#software engineering`, `#workplace ethics`, `#tech industry`, `#personal reflection`

---

<a id="item-4"></a>
## [Defining the smallest saleable piece of software](https://brandur.org/minimum-viable-unit) ⭐️ 7.0/10

The article argues that while the cost to initially build software has dropped dramatically, the effort required to polish, maintain, and support software remains substantial, which reshapes the economics of side projects and the build versus buy decision. This analysis is significant for developers and businesses because it explains why many side projects stall despite cheaper building tools, and why purchasing third‑party software often remains practical even when internal development seems feasible. The article introduces a 'zone of viability' for software projects, where the total cost of polish and maintenance must be less than the utility gained or the cost of alternatives. It also notes that LLMs lower the building barrier but may increase competition in the software market.

hackernews · brandur · Jun 21, 16:41

**Background**: In software development, the 'build vs buy' decision weighs internal development costs against purchasing a commercial product. The article extends this by focusing on the ongoing maintenance and support efforts, not just the upfront build. This is especially relevant as AI tools drastically reduce initial coding time but do not eliminate the need for testing, documentation, and user support.

**Discussion**: Commenters largely agree with the article's core argument. One shares that several side projects stalled after a few weeks because the remaining effort still exceeded personal utility. Another notes that despite expecting quick rebuilds, making software well still takes time and iteration. A commenter also highlights that LLMs often rely on third‑party packages, undermining the idea of easily displacing existing software.

**Tags**: `#software economics`, `#build vs buy`, `#side projects`, `#software development`, `#viability`

---

<a id="item-5"></a>
## [AI-Driven Paradigm Shift in Software Engineering Introduced](https://colobu.com/2026/06/22/software-engineering-fifty-years-paradigm-shift/) ⭐️ 7.0/10

This article introduces a series arguing that software engineering is undergoing its most profound paradigm shift since the discipline's inception in 1968, driven by AI tooling. It highlights stories of prominent figures like Karpathy, who stopped writing code for six months, and Amodei, who predicts 90% of code will be written by AI. The article synthesizes viewpoints from leading technologists to frame a broader industry shift that could redefine the role of developers, moving from writing code to supervising AI-generated output. It provides a conceptual framework for understanding how structured knowledge can harness unstructured AI capabilities, which is relevant for everyone in software development. Five individual stories are used to illustrate the shift: Karpathy not writing code for six months, Amodei's 90% AI code prediction, Garry Tan's 810x output increase, Boris Cherny shifting to code review only, and antirez letting go of handcrafting every line. The article sets up a main theme: using structured knowledge to harness unstructured AI capabilities.

rss · 鸟窝 · Jun 21, 16:00

**Background**: Software engineering emerged as a formal discipline in 1968, born from the NATO Software Engineering Conference to address the 'software crisis.' A paradigm shift in this context means a fundamental change in how software is conceptualized, built, and maintained. The article argues that AI tooling is driving such a shift, altering the developer's role from manual coding to overseeing AI-assisted development.

**Tags**: `#software engineering`, `#AI`, `#paradigm shift`, `#productivity`, `#tooling`

---

<a id="item-6"></a>
## [JSON-LD Guide for Personal Websites](https://hawksley.dev/blog/json-ld-explained-for-personal-websites/) ⭐️ 6.0/10

A new guide explains how to use JSON-LD structured data on personal websites to improve search engine results and enable rich snippets. This matters because structured data can help personal websites gain richer search appearances, but community discussion highlights that Google's LLM-generated summaries may reduce the value of traditional SEO techniques. JSON-LD is one of three formats for structured data, along with Microdata and RDFa, and is recommended for its simplicity and ease of embedding in web pages.

hackernews · ethanhawksley · Jun 21, 18:51

**Background**: JSON-LD (JavaScript Object Notation for Linked Data) is a World Wide Web Consortium standard for encoding linked data using JSON. Schema.org provides a shared vocabulary of types and properties for structured data markup, used by major search engines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JSON-LD">JSON-LD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Schema.org">Schema.org</a></li>
<li><a href="https://json-ld.org/">JSON-LD - JSON for Linked Data</a></li>

</ul>
</details>

**Discussion**: Community comments question the relevance of JSON-LD given Google's shift to LLM-generated summaries, but others provide practical resources like Neil Patel's guide and a schema markup generator tool.

**Tags**: `#json-ld`, `#structured-data`, `#seo`, `#personal-websites`, `#schema-org`

---

<a id="item-7"></a>
## [How LLMs Actually Work: A Beginner's Guide](https://colobu.com/2026/06/21/how-llm-actually-works/) ⭐️ 6.0/10

A new accessible guide published on colobu.com explains the core mechanisms of modern transformer-based LLMs—tokenization, embedding, positional encoding, and attention—using minimal math. This guide helps bridge the gap for beginners who want to understand how LLMs work internally without diving into complex equations, making the technology more accessible to a wider audience. The article follows a four-step roadmap: tokenization converts text into integers, embedding gives those integers meaning, positional encoding tracks token order, and attention enables token-to-token communication.

rss · 鸟窝 · Jun 21, 03:09

**Background**: Modern LLMs are built by stacking transformer blocks, which rely on tokenization to break text into tokens, embedding to convert tokens into vectors, positional encoding to preserve word order, and attention to allow tokens to contextually interact. Tokenization simplifies text into manageable chunks that become the model's vocabulary. Positional encoding is essential because the transformer architecture itself is permutation-invariant and does not inherently understand sequence order. This article serves as an entry point for understanding these components without heavy mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://seantrott.substack.com/p/tokenization-in-large-language-models">Tokenization in large language models, explained</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/positional-encoding-in-transformers/">Positional Encoding in Transformers - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Transformer`, `#Machine Learning`, `#Natural Language Processing`, `#Attention Mechanism`

---

<a id="item-8"></a>
## [Go AMD64 Microarchitecture Levels Performance Impact](https://colobu.com/2026/06/21/amd64-microarchitecture-level-go-performance/) ⭐️ 6.0/10

Go 1.18 introduced four GOAMD64 microarchitecture levels (v1–v4) that control which instruction sets the compiler can use, enabling performance gains at the cost of dropping support for older CPUs. The Go toolchain does not yet generate AVX512 instructions. This allows Go developers to optimize binaries for modern processors, achieving significant speedups in compute-intensive tasks. However, it forces a trade-off between performance and compatibility, affecting deployment on older or diverse hardware. The levels are: v1 (baseline SSE2), v2 (adds POPCNT, SSE4.2, etc.), v3 (adds AVX2, BMI, FMA), and v4 (adds AVX512 subsets). Even at v1, the runtime may dynamically use newer instructions like POPCNT if the CPU supports them; AVX512 is not generated by the toolchain at any level.

rss · 鸟窝 · Jun 21, 01:38

**Background**: x86-64 processors have evolved over decades with many instruction set extensions. In 2020, Intel, AMD, Red Hat, and SUSE defined microarchitecture levels (v1–v4) to group these extensions. Go 1.18 adopted these levels via the GOAMD64 build tag, allowing developers to target a specific hardware generation. By default, Go compiles for v1 (circa 2003), missing all later optimizations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/X86-64">x86-64 - Wikipedia</a></li>
<li><a href="https://www.androidauthority.com/what-is-x86-64-v3-3415395/">What is x 86 - 64 -v3? Understanding the x 86 - 64 microarchitecture levels</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Vector_Extensions">Advanced Vector Extensions - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Go`, `#AMD64`, `#microarchitecture`, `#performance`, `#compilation`

---