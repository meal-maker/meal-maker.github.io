---
layout: default
title: "Horizon Summary: 2026-06-21 (EN)"
date: 2026-06-21
lang: en
---

> From 16 items, 4 important content pieces were selected

---

1. [SMPTE Opens Its Standards Library to All, Free of Charge](#item-1) ⭐️ 8.0/10
2. [UHF X11 Brings X11 to Apple Vision Pro's VisionOS](#item-2) ⭐️ 6.0/10
3. [DOS Game F-15 Strike Eagle II Reverse Engineering Project Seeks Testers](#item-3) ⭐️ 6.0/10
4. [CSSQuake: Quake Recreated Entirely in CSS](#item-4) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [SMPTE Opens Its Standards Library to All, Free of Charge](https://www.smpte.org/blog/smpte-makes-its-standards-freely-accessible-openingstandards-library-to-the-global-media-technology-community) ⭐️ 8.0/10

SMPTE, the Society of Motion Picture and Television Engineers, has announced that all of its standards, recommended practices, and engineering guidelines are now freely accessible to the public without any cost or registration barriers. This move opens the entire SMPTE standards library to developers, engineers, and media professionals worldwide. By removing paywalls from its standards, SMPTE lowers a significant barrier for startups, independent developers, and smaller production houses who previously had to purchase expensive documents to ensure compliance. This shift aligns SMPTE with the open-standards movement and could accelerate innovation in media production and distribution technologies. The free access applies to all SMPTE Standards, Recommended Practices, and Engineering Guidelines, which are now available for download from the SMPTE website. SMPTE is also modernizing its standards development process by adopting GitHub-based workflows, structured HTML authoring, and an integrated publishing pipeline.

hackernews · zdw · Jun 20, 17:01

**Background**: SMPTE is a global professional society that develops technical standards for the motion picture and television industry, including widely used specifications such as SMPTE timecode and digital cinema packages. Historically, these standards were only available for purchase, which limited access for many developers and smaller organizations. By making them freely accessible, SMPTE follows the example of other successful open-standards bodies like the IETF, whose no-cost availability contributed to the explosive growth of the internet. This change is part of a broader effort to modernize SMPTE's standards development and publication processes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.smpte.org/standards/overview">Standards Overview | Society of Motion Picture & Television ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Society_of_Motion_Picture_and_Television_Engineers">Society of Motion Picture and Television Engineers - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly positive, with commenters like lambdaone praising the move as long overdue and noting that free access was a key factor in the success of IETF standards. Others, such as geerlingguy, expressed surprise that any standards body would not do this by default. There is also appreciation for SMPTE's parallel modernization efforts, including the adoption of GitHub workflows and structured authoring.

**Tags**: `#standards`, `#media technology`, `#open access`, `#SMPTE`, `#video production`

---

<a id="item-2"></a>
## [UHF X11 Brings X11 to Apple Vision Pro's VisionOS](https://www.lispm.net/apps/uhf-x11/) ⭐️ 6.0/10

UHF X11 is a new app that ports the X11 window system to Apple Vision Pro's visionOS, enabling traditional Linux GUI applications to run in a spatial computing environment. Each X11 top-level window opens as its own visionOS window, allowing users to position them anywhere in their space. This project bridges legacy Linux desktop environments with Apple's spatial computing platform, opening up a vast library of classic Unix GUI applications for Vision Pro users. It represents a novel convergence of traditional desktop computing and AR/VR, though its practical impact may be limited to enthusiasts. The app supports OpenGL clients via GLX rendering over X11, though compatibility varies depending on GL versions and features. UHF X11 is available on the App Store, and its community discussion includes references to alternative projects like WayVR for using Linux desktops on headsets.

hackernews · zdw · Jun 20, 17:04

**Background**: X11 is the traditional windowing system for Unix and Linux systems, widely used for decades in desktop environments. Apple Vision Pro runs visionOS, an extended reality operating system derived from iPadOS and designed for mixed reality experiences. Porting X11 to visionOS allows Linux GUI apps to be displayed in a 3D spatial environment, each in its own window.

<details><summary>References</summary>
<ul>
<li><a href="https://apps.apple.com/us/app/uhf-x11/id6772673274">UHF X11 App - App Store</a></li>
<li><a href="https://en.wikipedia.org/wiki/VisionOS">visionOS - Wikipedia</a></li>
<li><a href="https://developer.apple.com/documentation/visionos">visionOS | Apple Developer Documentation</a></li>

</ul>
</details>

**Discussion**: Community comments are light-hearted and moderately engaged, with one user noting the humor of '3D in 2D in 3D' and reminiscing about GLX compatibility challenges. Another commenter suspects X11 will outlive visionOS, while a third recommends the alternative WayVR project for Linux desktop use on headsets.

**Tags**: `#X11`, `#VisionOS`, `#Apple Vision Pro`, `#AR/VR`, `#Linux compatibility`

---

<a id="item-3"></a>
## [DOS Game F-15 Strike Eagle II Reverse Engineering Project Seeks Testers](https://neuviemeporte.github.io/f15-se2/2026/06/20/needyou.html) ⭐️ 6.0/10

A developer is reverse engineering the DOS flight simulator F-15 Strike Eagle II, converting its assembler code into equivalent C to eventually port it to modern platforms. They are currently asking for testers to help find bugs introduced during the conversion. This project preserves a classic game beyond DOS emulation, enabling native play on modern operating systems without requiring DOSBox. It also contributes to the retro computing community's understanding of code porting from assembler to C. The conversion process first fully reverse-engineered the game into assembler, and now aims to rewrite that assembler into binary-equal compiled C code, all still running under DOS until no assembler remains, after which the port to Linux and Windows can begin.

hackernews · LowLevelMahn · Jun 20, 15:10

**Background**: F-15 Strike Eagle II is a classic DOS flight simulator from the early 1990s. Reverse engineering is the process of analyzing a compiled program to understand its structure and logic, often to recreate source code. The developer's approach is to convert the original assembler back to C, preserving exact behavior, which can then be compiled for different platforms.

**Discussion**: Commenters expressed interest and nostalgia, noting the game's place in their childhood. Some asked why not simply emulate the game via DOSBox, while others highlighted the value of native ports for better compatibility and lower overhead. There was also a suggestion that AI could help infer structure from decompiled code without symbol names.

**Tags**: `#reverse engineering`, `#DOS`, `#game porting`, `#retro computing`, `#open source`

---

<a id="item-4"></a>
## [CSSQuake: Quake Recreated Entirely in CSS](https://cssquake.com/) ⭐️ 6.0/10

CSSQuake is a playable demo that recreates the classic first-person shooter Quake using only CSS, HTML, and JavaScript, with no Canvas or WebGL. This project showcases the creative and technical limits of CSS as a rendering medium, sparking discussion about web capabilities and nostalgia for classic games. The implementation is a full recreation of Quake's engine logic in JavaScript, with rendering done through CSS transforms and HTML elements, but it suffers from performance issues and behavioral inaccuracies compared to the original game.

hackernews · msalsas · Jun 20, 10:49

**Background**: Quake is a landmark 1996 first-person shooter known for its fully 3D environment. CSS (Cascading Style Sheets) is normally used for styling web pages, not real-time 3D rendering. CSSQuake is a technical demo that pushes CSS beyond its typical use, but it lacks the performance and accuracy of native game engines.

**Discussion**: Commenters were impressed by the achievement but noted that it runs slower than the original game on modern hardware and has some gameplay inaccuracies, such as buttons needing to be shot instead of touched. Some users found it nostalgic and fun despite the quirks.

**Tags**: `#css`, `#quake`, `#web development`, `#game`, `#demo`

---