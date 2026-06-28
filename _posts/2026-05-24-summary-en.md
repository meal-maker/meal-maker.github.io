---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 21 items, 6 important content pieces were selected

---

1. [C# Finally Gets Union Types in .NET 11 Preview](#item-1) ⭐️ 9.0/10
2. [Green card seekers must leave US to apply, Trump says](#item-2) ⭐️ 8.0/10
3. [80386 Microcode Disassembled from Die Images](#item-3) ⭐️ 8.0/10
4. [Hengefinder: Web app for sun-street alignment](#item-4) ⭐️ 7.0/10
5. [SpaceX Launches Starship V3 Megarocket](#item-5) ⭐️ 7.0/10
6. [The HTML <dl> Element: Semantics, History, and Practical Challenges](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [C# Finally Gets Union Types in .NET 11 Preview](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 9.0/10

C# introduces union types as a preview feature in .NET 11, enabling developers to model values from a closed set of types with exhaustive pattern matching support. Union types are a long-requested feature that significantly improves type safety and code clarity, similar to discriminated unions in F# or Rust. This addition modernizes C# and reduces entire classes of bugs related to handling alternative states. The proposed unions in C# are unions of types, not discriminated or tagged unions, though discriminated unions can be expressed by using fresh type declarations as case types. The feature is in preview; Microsoft has warned that the design may change based on feedback.

hackernews · ingve · May 22, 12:28

**Background**: Union types allow a variable to hold one of several specified types. C# developers previously used libraries like OneOf or workarounds to achieve similar results. F# has supported discriminated unions for decades, and languages like TypeScript and Rust have popularized the pattern for cleaner type modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/union">Union types - C# reference | Microsoft Learn</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/unions">Unions - C# feature specifications (preview) | Microsoft Learn</a></li>
<li><a href="https://blog.ndepend.com/csharp-unions/">C# 15 Unions - NDepend Blog</a></li>

</ul>
</details>

**Discussion**: The community is highly positive, with many expressing long anticipation and appreciation for the team's efforts. Some note that F# had this feature for years and question why C# gets more attention, while others see it as a practical improvement for teams unwilling or unable to switch languages. A commenter also highlights that the real test will be adoption in public APIs.

**Tags**: `#C#`, `#.NET`, `#union types`, `#type system`, `#programming languages`

---

<a id="item-2"></a>
## [Green card seekers must leave US to apply, Trump says](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html) ⭐️ 8.0/10

The Trump administration announced a rule requiring most green card applicants already in the United States to leave the country and apply through consular processing abroad, effectively ending the adjustment of status process except in extraordinary circumstances. This policy disrupts the primary pathway for skilled workers, especially in tech, who currently adjust status while living and working in the U.S., potentially causing prolonged separations from families and risking talent retention. The rule applies to applicants on H-1B, L-1, O-1, and other nonimmigrant visas; only those with 'extraordinary circumstances' can seek adjustment inside the U.S. The change was announced on May 22, 2026, via a USCIS policy memorandum.

hackernews · tlhunter · May 22, 21:27

**Background**: Previously, foreign nationals already in the U.S. on work visas could apply for a green card through 'adjustment of status,' a process that allowed them to remain in the country while their application was processed. The alternative, 'consular processing,' requires applicants to return to their home country or another country with a U.S. consulate, attend an interview, and wait for visa issuance, which can involve long delays and separation from U.S.-based jobs and families.

<details><summary>References</summary>
<ul>
<li><a href="https://www.uscis.gov/green-card/green-card-processes-and-procedures/adjustment-of-status">Adjustment of Status | USCIS</a></li>
<li><a href="https://www.uscis.gov/newsroom/news-releases/us-citizenship-and-immigration-services-will-grant-adjustment-of-status-only-in-extraordinary">U.S. Citizenship and Immigration Services Will Grant ‘Adjustment of Status’ Only in Extraordinary Circumstances | USCIS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Green_card">Green card - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments expressed strong dismay and concern, with many arguing the rule would severely disrupt the lives of tech workers and their families, particularly children born in the U.S. who might need visas to accompany parents abroad. Some expressed relief if already holding green cards, while others predicted the U.S. would lose global talent and become more isolationist.

**Tags**: `#immigration`, `#US policy`, `#tech workforce`, `#green card`, `#visa`

---

<a id="item-3"></a>
## [80386 Microcode Disassembled from Die Images](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

The microcode ROM of the Intel 80386 CPU has been successfully extracted from high-resolution die images and disassembled into a readable list of micro-operations, using a combination of image processing, AI, and manual verification. This reverse engineering feat enables open-source projects like z386 to faithfully recreate the 80386’s microarchitecture, preserving and documenting a pivotal piece of computer history. It also provides rare transparency into the microcode layer of a classic x86 processor. The extracted binary blob was cross-checked for accuracy, and the resulting disassembly reveals the full sequence of micro-operations (like NEARCALL) that the CPU executes for each instruction. The blog post notes that a previous attempt considered this too hard, but new techniques made it possible.

hackernews · nand2mario · May 23, 12:11

**Background**: Microcode is a low-level firmware inside a CPU that controls how machine instructions are executed by orchestrating micro-operations. The 80386, introduced in 1985, was Intel’s first 32-bit x86 processor and is considered a cornerstone of modern computing. Reverse engineering microcode from die images is an extremely challenging task because it requires identifying the physical ROM cells and decoding their bit patterns from microscopic photographs of the silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/I386">i386 - Wikipedia</a></li>
<li><a href="https://sesamedisk.com/z386-open-source-80386-microcode-recreation/">z386: Open-Source Microcode Recreation of the 80386 CPU</a></li>

</ul>
</details>

**Discussion**: The comments express awe at the difficulty and ingenuity of the work—liendolucas asks for details on the extraction process, and bmenrigh calls it 'incredibly hard but also incredibly fun and rewarding.' A related ongoing thread about the z386 project is also referenced, showing strong community interest.

**Tags**: `#reverse engineering`, `#microcode`, `#80386`, `#computer architecture`, `#open-source hardware`

---

<a id="item-4"></a>
## [Hengefinder: Web app for sun-street alignment](https://victoriaritvo.com/blog/hengefinder/) ⭐️ 7.0/10

Hengefinder is a web application that calculates the exact times when the sun aligns with a given street direction, using astronomical algorithms from the Astral library and Jean Meeus' work. It helps photographers and urban planners determine optimal lighting conditions for specific streets. This tool bridges astronomy and everyday urban life, offering practical utility for photographers seeking perfect golden-hour shots and urban planners analyzing sunlight exposure for building design. Its niche focus and solid technical implementation demonstrate how specialized tools can provide significant value with relatively simple algorithms. The app uses the Python Astral library, which employs equations from Jean Meeus' 'Astronomical Algorithms' with an accuracy of 0.01 arc degree, ignoring gravitational perturbations from other planets and the Moon. Community feedback notes that the website currently blocks mobile access, limiting on-site usage for smartphone users.

hackernews · evakhoury · May 22, 20:39

**Background**: Solar azimuth and elevation calculations determine the sun's position relative to a location on Earth. Tools like NOAA's Solar Position Calculator and SunCalc provide similar sun-position data, but Hengefinder streamlines the process by focusing specifically on when the sun aligns with a linear street direction, which is useful for capturing dramatic light effects during solstices or equinoxes.

<details><summary>References</summary>
<ul>
<li><a href="https://gml.noaa.gov/grad/solcalc/azel.html">NOAA Solar Position Calculator</a></li>
<li><a href="https://www.suncalc.org/">SunCalc - sunrise, sunset, shadow length, solar eclipse, sun position, sun phase, sun height, sun calculator, sun movement, map, sunlight phases, elevation, Photovoltaic system, Photovoltaic</a></li>

</ul>
</details>

**Discussion**: Comments highlight technical depth: infinet praises the Astral library's use of Meeus algorithms, while TeMPOraL requests an inverse app to predict shade zones for hot-weather navigation. Others note mobile access restrictions and compare Hengefinder favorably to similar tools like The Photographer's Ephemeris.

**Tags**: `#astronomy`, `#photography`, `#tools`, `#urban planning`, `#Python`

---

<a id="item-5"></a>
## [SpaceX Launches Starship V3 Megarocket](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 7.0/10

SpaceX launched the first test flight of its Starship V3 rocket on Friday, April 2025, at around 6:30 PM EDT, marking the 12th Starship test and the debut of the largest version of the vehicle. During the flight, the booster experienced engine issues, losing one engine during ascent and failing to relight for the boost-back burn, but the ship successfully landed on target despite losing one engine of its own. This flight demonstrates SpaceX's commitment to rapid iterative development, gathering valuable data even from partial failures, which accelerates the refinement of the world's most powerful rocket. The successful landing of the ship, despite engine anomalies, proves the resilience of the vehicle's guidance systems and heat shield improvements, moving closer to full reusability. The booster lost an engine during ascent and failed to relight its engines for the boost-back burn, but did ignite for a landing burn, though it hit the water harder and off target. The ship lost one engine shortly after stage separation but landed exactly on target, with no visible hot spots or burn-through on reentry, indicating improved heat shield performance.

hackernews · busymom0 · May 22, 23:41

**Background**: Starship is a two-stage, fully reusable super heavy-lift launch vehicle under development by SpaceX, designed to carry large payloads to orbit, the Moon, and Mars. SpaceX employs a rapid iterative development methodology, organizing work into two-week sprints and accepting 'negative outcome learning experiences' to quickly gather data and improve designs. Version 3 (V3) of Starship is the tallest and most powerful variant yet, with upgraded engines and structures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-will-launch-its-1st-ever-starship-v3-megarocket-today-the-stakes-couldnt-be-higher">SpaceX will launch its 1st-ever Starship V 3 megarocket on... | Space</a></li>
<li><a href="https://www.scientificamerican.com/article/spacex-launches-starship-v3-the-worlds-most-powerful-and-tallest-rocket-ever/">SpaceX launches Starship V 3 —the world's most... | Scientific American</a></li>

</ul>
</details>

**Discussion**: Community comments generally express excitement and praise for the rapid iteration pace, noting that the booster failure is acceptable as long as data is collected. One commenter highlighted the improved heat shield with no burn-through, while another noted the dummy payload satellites burning up behind the ship during reentry. The engine bay's red glow was described as ominous, but the precise landing of the ship was seen as a major success for the guidance software.

**Tags**: `#SpaceX`, `#Starship`, `#rocket launch`, `#aerospace`, `#iterative development`

---

<a id="item-6"></a>
## [The HTML <dl> Element: Semantics, History, and Practical Challenges](https://benmyers.dev/blog/on-the-dl/) ⭐️ 6.0/10

Ben Myers published a detailed blog post exploring the HTML <dl> element's history, semantics, and real-world usage difficulties, sparking debate about the practicality of semantic HTML. This discussion matters because it highlights the tension between semantic HTML ideals and practical web development needs, affecting accessibility, maintainability, and developer workflows. The <dl> element has been part of HTML since before the web, dating back to IBM's GML in the 1980s, and its semantics have evolved from 'definition list' to 'description list' in HTML5.

hackernews · ravenical · May 23, 13:03

**Background**: The HTML <dl> element (description list) is used to represent a list of term-description groups, commonly used for glossaries or metadata. Despite its long history, developers often face challenges with styling, nesting, and accessibility when using it for complex layouts.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl">HTML description list element - HTML | MDN</a></li>
<li><a href="https://css-tricks.com/on-the-dl/">Blogging about HTML elements ¹? *chefs kiss* | CSS-Tricks</a></li>

</ul>
</details>

**Discussion**: Community comments included historical context, such as the element's pre-web origins in IBM's GML, and practical critiques from developers like kqp who abandoned semantic HTML due to its inflexibility. There was also discussion about ARIA role restrictions and the element's misuse for layout purposes.

**Tags**: `#HTML`, `#semantic web`, `#web development`, `#accessibility`, `#technical debate`

---