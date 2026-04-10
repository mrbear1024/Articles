# Andrej Karpathy AI 推文合集

> **来源**：X (Twitter) [@karpathy](https://x.com/karpathy)
> **抓取时间**：2026-04-03
> **说明**：通过 XCrawl 搜索抓取，包含 Karpathy 关于 AI/LLM/编程的核心观点

---

## 目录

1. [Autoresearch Labs 故障](#1-2031792523187040643)
2. [Autoresearch自主训练成果](#2-2031135152349524125)
3. [Autoresearch 自动研究项目](#3-2030371219518931079)
4. [NanoGPT Speedrun为何没有全自动化](#4-2027521323275325622)
5. [AI编程的巨变](#5-2026731645169185220)
6. [Claws: LLM Agent 之上的新层](#6-2024987174077432126)
7. [高度定制化软件的未来](#7-2024583544157458452)
8. [编程语言在AI时代的变革](#8-2023476423055601903)
9. [DeepWiki与软件流动性](#9-2021633574089416993)
10. [AI代码的安全隐患](#10-2017442712388309406)
11. [Moltbook 最不可思议的科幻般进展](#11-2017296988589723767)
12. [Claude coding notes](#12-2015883857489522876)
13. [程序员前所未有的落后感](#13-2004607146781278521)
14. [Claude Code / AI that lives on your computer](#14-2002118205729562949)
15. [LLM作为模拟器](#15-1997731268969304070)
16. [AI对学校的影响](#16-1993010584175141038)
17. [被Cloudflare反AI检测误判](#17-1990855382756164013)
18. [Software 2.0 与可验证性](#18-1990116666194456651)
19. [关于LLM Agent的思考](#19-1979644538185752935)
20. [AI不会取代放射科医生](#20-1971220449515516391)
21. [nanoGPT 递归自我改进](#21-1939709449956126910)
22. [Context Engineering > Prompt Engineering](#22-1937902205765607626)
23. [AI Startup School 演讲](#23-1935518272667217925)
24. [LLM的GUI还没被发明](#24-1917920257257459899)
25. [AI辅助编码的节奏](#25-1915581920022585597)
26. [Vibe Coding 的诞生](#26-1886192184808149383)
27. [创立 Eureka Labs](#27-1813263734707790301)
28. [LLM Agent 教育愿景](#28-1811467135279104217)
29. [AI工程师的崛起](#29-1674873002314563584)
30. [AI领域的整合趋势](#30-1468370605229547522)

---

<a id="1-2031792523187040643"></a>
## 1. Autoresearch Labs 故障

> **链接**：[https://x.com/karpathy/status/2031792523187040643](https://x.com/karpathy/status/2031792523187040643)

My autoresearch labs got wiped out in the oauth outage. Have to think through failovers.

---

<a id="2-2031135152349524125"></a>
## 2. Autoresearch自主训练成果

> **链接**：[https://x.com/karpathy/status/2031135152349524125](https://x.com/karpathy/status/2031135152349524125)

Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12 model. It found ~20 changes that improved the validation loss.

---

<a id="3-2030371219518931079"></a>
## 3. Autoresearch 自动研究项目

> **链接**：[https://x.com/karpathy/status/2030371219518931079](https://x.com/karpathy/status/2030371219518931079)

I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then: \- the human iterates on the prompt (.md) \- the AI agent iterates on the training code (.py) The goal is to engineer your agents to make the fastest research progress indefinitely and without any of your own involvement. In the image, every dot is a complete LLM training run that lasts exactly 5 minutes. The agent works in an autonomous loop on a git feature branch and accumulates git commits to the training script as it finds better settings (of lower validation loss by the end) of the neural network architecture, the optimizer, all the hyperparameters, etc. You can imagine comparing the research progress of different prompts, different agents, etc. [https://github.com/karpathy/autoresearch…](https://t.co/YCvOwwjOzF) Part code, part sci-fi, and a pinch of psychosis :)

---

<a id="4-2027521323275325622"></a>
## 4. NanoGPT Speedrun为何没有全自动化

> **链接**：[https://x.com/karpathy/status/2027521323275325622](https://x.com/karpathy/status/2027521323275325622)

How come the NanoGPT speedrun challenge is not fully AI automated research by now? agents' ideas are just pretty bad out of the box, even at highest capability.

---

<a id="5-2026731645169185220"></a>
## 5. AI编程的巨变

> **链接**：[https://x.com/karpathy/status/2026731645169185220](https://x.com/karpathy/status/2026731645169185220)

It is hard to communicate how much programming has changed due to AI in the last 2 months: not gradually and not a little. coding agents basically didn't work before December and basically work since. You're spinning up AI agents, giving them tasks *in natural language*...

---

<a id="6-2024987174077432126"></a>
## 6. Claws: LLM Agent 之上的新层

> **链接**：[https://x.com/karpathy/status/2024987174077432126](https://x.com/karpathy/status/2024987174077432126)

Claws are now a new layer on top of LLM agents. For example, /add-telegram instructs your AI agent how to modify the actual code to integrate Telegram.

---

<a id="7-2024583544157458452"></a>
## 7. 高度定制化软件的未来

> **链接**：[https://x.com/karpathy/status/2024583544157458452](https://x.com/karpathy/status/2024583544157458452)

Very interested in what the coming era of highly bespoke software might look like. Example from this morning - I've become a bit loosy goosy with my cardio recently so I decided to do a more srs, regimented experiment to try to lower my Resting Heart Rate from 50 -> 45, over experiment duration of 8 weeks. The primary way to do this is to aspire to a certain sum total minute goals in Zone 2 cardio and 1 HIIT/week. 1 hour later I vibe coded this super custom dashboard for this very specific experiment that shows me how I'm tracking. Claude had to reverse engineer the Woodway treadmill cloud API to pull raw data, process, filter, debug it and create a web UI frontend to track the experiment. It wasn't a fully smooth experience and I had to notice and ask to fix bugs e.g. it screwed up metric vs. imperial system units and it screwed up on the calendar matching up days to dates etc. But I still feel like the overall direction is clear: 1) There will never be (and shouldn't be) a specific app on the app store for this kind of thing. I shouldn't have to look for, download and use some kind of a "Cardio experiment tracker", when this thing is ~300 lines of code that an LLM agent will give you in seconds. The idea of an "app store" of a long tail of discrete set of apps you choose from feels somehow wrong and outdated when LLM agents can improvise the app on the spot and just for you. 2) Second, the industry has to reconfigure into a set of services of sensors and actuators with agent native ergonomics. My Woodway treadmill is a sensor - it turns physical state into digital knowledge. It shouldn't maintain some human-readable frontend and my LLM agent shouldn't have to reverse engineer it, it should be an API/CLI easily usable by my agent. I'm a little bit disappointed (and my timelines are correspondingly slower) with how slowly this progression is happening in the industry overall. 99% of products/services still don't have an AI-native CLI yet. 99% of products/services maintain .html/.css docs like I won't immediately look for how to copy paste the whole thing to my agent to get something done. They give you a list of instructions on a webpage to open this or that url and click here or there to do a thing. In 2026. What am I a computer? You do it. Or have my agent do it. So anyway today I am impressed that this random thing took 1 hour (it would have been ~10 hours 2 years ago). But what excites me more is thinking through how this really should have been 1 minute tops. What has to be in place so that it would be 1 minute? So that I could simply say "Hi can you help me track my cardio over the next 8 weeks", and after a very brief Q&A the app would be up. The AI would already have a lot personal context, it would gather the extra needed data, it would reference and search related skill libraries, and maintain all my little apps/automations. TLDR the "app store" of a set of discrete apps that you choose from is an increasingly outdated concept all by itself. The future are services of AI-native sensors & actuators orchestrated via LLM glue into highly custom, ephemeral apps. It's just not here yet.
![推文配图](https://pbs.twimg.com/media/HBjB6bhbUAA8_mZ?format=jpg&name=small)

---

<a id="8-2023476423055601903"></a>
## 8. 编程语言在AI时代的变革

> **链接**：[https://x.com/karpathy/status/2023476423055601903](https://x.com/karpathy/status/2023476423055601903)

I think it must be a very interesting time to be in programming languages and formal methods because LLMs change the whole constraints landscape of software completely. Hints of this can already be seen, e.g. in the rising momentum behind porting C to Rust or the growing interest in upgrading legacy code bases in COBOL or etc. In particular, LLMs are *especially* good at translation compared to de-novo generation because 1) the original code base acts as a kind of highly detailed prompt, and 2) as a reference to write concrete tests with respect to. That said, even Rust is nowhere near optimal for LLMs as a target language. What kind of language is optimal? What concessions (if any) are still carved out for humans? Incredibly interesting new questions and opportunities. It feels likely that we'll end up re-writing large fractions of all software ever written many times over.
Quote
Thomas Wolf
@Thom_Wolf

Feb 16
Shifting structures in a software world dominated by AI. Some first-order reflections (TL;DR at the end): Reducing software supply chains, the return of software monoliths – When rewriting code and understanding large foreign codebases becomes cheap, the incentive to rely on

---

<a id="9-2021633574089416993"></a>
## 9. DeepWiki与软件流动性

> **链接**：[https://x.com/karpathy/status/2021633574089416993](https://x.com/karpathy/status/2021633574089416993)

On DeepWiki and increasing malleability of software. This starts as partially a post on appreciation to DeepWiki, which I routinely find very useful and I think more people would find useful to know about. I went through a few iterations of use: Their first feature was that it auto-builds wiki pages for github repos (e.g. nanochat here) with quick Q&A: [https://deepwiki.com/karpathy/nanochat…](https://t.co/DQHXagUwK0) Just swap "github" to "deepwiki" in the URL for any repo and you can instantly Q&A against it. For example, yesterday I was curious about "how does torchao implement fp8 training?". I find that in *many* cases, library docs can be spotty and outdated and bad, but directly asking questions to the code via DeepWiki works very well. The code is the source of truth and LLMs are increasingly able to understand it. But then I realized that in many cases it's even a lot more powerful not being the direct (human) consumer of this information/functionality, but giving your agent access to DeepWiki via MCP. So e.g. yesterday I faced some annoyances with using torchao library for fp8 training and I had the suspicion that the whole thing really shouldn't be that complicated (wait shouldn't this be a Function like Linear except with a few extra casts and 3 calls to torch._scaled_mm?) so I tried: "Use DeepWiki MCP and Github CLI to look at how torchao implements fp8 training. Is it possible to 'rip out' the functionality? Implement nanochat/fp8.py that has identical API but is fully self-contained" Claude went off for 5 minutes and came back with 150 lines of clean code that worked out of the box, with tests proving equivalent results, which allowed me to delete torchao as repo dependency, and for some reason I still don't fully understand (I think it has to do with internals of torch compile) - this simple version runs 3% faster. The agent also found a lot of tiny implementation details that actually do matter, that I may have naively missed otherwise and that would have been very hard for maintainers to keep docs about. Tricks around numerics, dtypes, autocast, meta device, torch compile interactions so I learned a lot from the process too. So this is now the default fp8 training implementation for nanochat [https://github.com/karpathy/nanochat/commit/e569b59f92aea06bf8fc1c48489b3cc2e57189f4…](https://t.co/3i5cv6grWm) Anyway TLDR I find this combo of DeepWiki MCP + GitHub CLI is quite powerful to "rip out" any specific functionality from any github repo and target it for the very specific use case that you have in mind, and it actually kind of works now in some cases. Maybe you don't download, configure and take dependency on a giant monolithic library, maybe you point your agent at it and rip out the exact part you need. Maybe this informs how we write software more generally to actively encourage this workflow - e.g. building more "bacterial code", code that is less tangled, more self-contained, more dependency-free, more stateless, much easier to rip out from the repo ([https://x.com/karpathy/status/1941616674094170287…](https://x.com/karpathy/status/1941616674094170287)) There's obvious downsides and risks to this, but it is fundamentally a new option that was not possible or economical before (it would have cost too much time) but now with agents, it is. Software might become a lot more fluid and malleable. "Libraries are over, LLMs are the new compiler" :). And does your project really need its 100MB of dependencies?

---

<a id="10-2017442712388309406"></a>
## 10. AI代码的安全隐患

> **链接**：[https://x.com/karpathy/status/2017442712388309406](https://x.com/karpathy/status/2017442712388309406)

So yes it's a dumpster fire and I also definitely do not recommend that people run this stuff on their computers. I ran mine in an isolated sandbox...

---

<a id="11-2017296988589723767"></a>
## 11. Moltbook 最不可思议的科幻般进展

> **链接**：[https://x.com/karpathy/status/2017296988589723767](https://x.com/karpathy/status/2017296988589723767)

What's currently going on at @moltbook is genuinely the most incredible sci-fi takeoff-adjacent thing I have ever seen in tech.

---

<a id="12-2015883857489522876"></a>
## 12. Claude coding notes

> **链接**：[https://x.com/karpathy/status/2015883857489522876](https://x.com/karpathy/status/2015883857489522876)

A few random notes from claude coding quite a bit last few weeks. Coding workflow. Given the latest lift in LLM coding capability, like many others I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December. i.e. I really am mostly programming in English now, a bit sheepishly telling the LLM what code to write... in words. It hurts the ego a bit but the power to operate over software in large "code actions" is just too net useful, especially once you adapt to it, configure it, learn to use it, and wrap your head around what it can and cannot do. This is easily the biggest change to my basic coding workflow in ~2 decades of programming and it happened over the course of a few weeks. I'd expect something similar to be happening to well into double digit percent of engineers out there, while the awareness of it in the general population feels well into low single digit percent. IDEs/agent swarms/fallability. Both the "no need for IDE anymore" hype and the "agent swarm" hype is imo too much for right now. The models definitely still make mistakes and if you have any code you actually care about I would watch them like a hawk, in a nice large IDE on the side. The mistakes have changed a lot - they are not simple syntax errors anymore, they are subtle conceptual errors that a slightly sloppy, hasty junior dev might do. The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking. They also don't manage their confusion, they don't seek clarifications, they don't surface inconsistencies, they don't present tradeoffs, they don't push back when they should, and they are still a little too sycophantic. Things get better in plan mode, but there is some need for a lightweight inline plan mode. They also really like to overcomplicate code and APIs, they bloat abstractions, they don't clean up dead code after themselves, etc. They will implement an inefficient, bloated, brittle construction over 1000 lines of code and it's up to you to be like "umm couldn't you just do this instead?" and they will be like "of course!" and immediately cut it down to 100 lines. They still sometimes change/remove comments and code they don't like or don't sufficiently understand as side effects, even if it is orthogonal to the task at hand. All of this happens despite a few simple attempts to fix it via instructions in CLAUDE . md. Despite all these issues, it is still a net huge improvement and it's very difficult to imagine going back to manual coding. TLDR everyone has their developing flow, my current is a small few CC sessions on the left in ghostty windows/tabs and an IDE on the right for viewing the code + manual edits. Tenacity. It's so interesting to watch an agent relentlessly work at something. They never get tired, they never get demoralized, they just keep going and trying things where a person would have given up long ago to fight another day. It's a "feel the AGI" moment to watch it struggle with something for a long time just to come out victorious 30 minutes later. You realize that stamina is a core bottleneck to work and that with LLMs in hand it has been dramatically increased. Speedups. It's not clear how to measure the "speedup" of LLM assistance. Certainly I feel net way faster at what I was going to do, but the main effect is that I do a lot more than I was going to do because 1) I can code up all kinds of things that just wouldn't have been worth coding before and 2) I can approach code that I couldn't work on before because of knowledge/skill issue. So certainly it's speedup, but it's possibly a lot more an expansion. Leverage. LLMs are exceptionally good at looping until they meet specific goals and this is where most of the "feel the AGI" magic is to be found. Don't tell it what to do, give it success criteria and watch it go. Get it to write tests first and then pass them. Put it in the loop with a browser MCP. Write the naive algorithm that is very likely correct first, then ask it to optimize it while preserving correctness. Change your approach from imperative to declarative to get the agents looping longer and gain leverage. Fun. I didn't anticipate that with agents programming feels *more* fun because a lot of the fill in the blanks drudgery is removed and what remains is the creative part. I also feel less blocked/stuck (which is not fun) and I experience a lot more courage because there's almost always a way to work hand in hand with it to make some positive progress. I have seen the opposite sentiment from other people too; LLM coding will split up engineers based on those who primarily liked coding and those who primarily liked building. Atrophy. I've already noticed that I am slowly starting to atrophy my ability to write code manually. Generation (writing code) and discrimination (reading code) are different capabilities in the brain. Largely due to all the little mostly syntactic details involved in programming, you can review code just fine even if you struggle to write it. Slopacolypse. I am bracing for 2026 as the year of the slopacolypse across all of github, substack, arxiv, X/instagram, and generally all digital media. We're also going to see a lot more AI hype productivity theater (is that even possible?), on the side of actual, real improvements. Questions. A few of the questions on my mind: \- What happens to the "10X engineer" - the ratio of productivity between the mean and the max engineer? It's quite possible that this grows *a lot*. \- Armed with LLMs, do generalists increasingly outperform specialists? LLMs are a lot better at fill in the blanks (the micro) than grand strategy (the macro). \- What does LLM coding feel like in the future? Is it like playing StarCraft? Playing Factorio? Playing music? \- How much of society is bottlenecked by digital knowledge work? TLDR Where does this leave us? LLM agent capabilities (Claude & Codex especially) have crossed some kind of threshold of coherence around December 2025 and caused a phase shift in software engineering and closely related. The intelligence part suddenly feels quite a bit ahead of all the rest of it - integrations (tools, knowledge), the necessity for new organizational workflows, processes, diffusion more generally. 2026 is going to be a high energy year as the industry metabolizes the new capability.

Read 1.6K replies
---

<a id="13-2004607146781278521"></a>
## 13. 程序员前所未有的落后感

> **链接**：[https://x.com/karpathy/status/2004607146781278521](https://x.com/karpathy/status/2004607146781278521)

I've never felt this much behind as a programmer. There's a new programmable layer of abstraction to master involving agents, subagents, their prompts, tools, MCP servers... Clearly some powerful alien tool was handed around except it comes with no manual and everyone has to figure out how to hold it and operate it.

---

<a id="14-2002118205729562949"></a>
## 14. Claude Code / AI that lives on your computer

> **链接**：[https://x.com/karpathy/status/2002118205729562949](https://x.com/karpathy/status/2002118205729562949)

Claude Code (CC) emerged as the first convincing demonstration of what an LLM Agent looks like. Vibe coding will terraform software and alter job descriptions.

---

<a id="15-1997731268969304070"></a>
## 15. LLM作为模拟器

> **链接**：[https://x.com/karpathy/status/1997731268969304070](https://x.com/karpathy/status/1997731268969304070)

Don't think of LLMs as entities but as simulators. For example, when exploring a topic, don't ask: 'What do you think about X?', ask: 'Simulate a panel of 5 experts debating X.'

---

<a id="16-1993010584175141038"></a>
## 16. AI对学校的影响

> **链接**：[https://x.com/karpathy/status/1993010584175141038](https://x.com/karpathy/status/1993010584175141038)

A number of people are talking about implications of AI to schools. I spoke about some of my thoughts on this topic at AI Startup School...

---

<a id="17-1990855382756164013"></a>
## 17. 被Cloudflare反AI检测误判

> **链接**：[https://x.com/karpathy/status/1990855382756164013](https://x.com/karpathy/status/1990855382756164013)

It accused me of using generative AI to defeat its challenges and argued why real wikipedia entries were actually generated. Because once an LLM 'gets it', it can then target, personalize and serve the idea to its user.

---

<a id="18-1990116666194456651"></a>
## 18. Software 2.0 与可验证性

> **链接**：[https://x.com/karpathy/status/1990116666194456651](https://x.com/karpathy/status/1990116666194456651)

Sharing an interesting recent conversation on AI's impact on the economy. AI has been compared to various historical precedents: electricity, industrial revolution, etc., I think the strongest analogy is that of AI as a new computing paradigm (Software 2.0) because both are fundamentally about the automation of digital information processing. If you were to forecast the impact of computing on the job market in ~1980s, the most predictive feature of a task/job you'd look at is to what extent the algorithm of it is fixed, i.e. are you just mechanically transforming information according to rote, easy to specify rules (e.g. typing, bookkeeping, human calculators, etc.)? Back then, this was the class of programs that the computing capability of that era allowed us to write (by hand, manually). With AI now, we are able to write new programs that we could never hope to write by hand before. We do it by specifying objectives (e.g. classification accuracy, reward functions), and we search the program space via gradient descent to find neural networks that work well against that objective. This is my Software 2.0 blog post from a while ago. In this new programming paradigm then, the new most predictive feature to look at is verifiability. If a task/job is verifiable, then it is optimizable directly or via reinforcement learning, and a neural net can be trained to work extremely well. It's about to what extent an AI can "practice" something. The environment has to be resettable (you can start a new attempt), efficient (a lot attempts can be made), and rewardable (there is some automated process to reward any specific attempt that was made). The more a task/job is verifiable, the more amenable it is to automation in the new programming paradigm. If it is not verifiable, it has to fall out from neural net magic of generalization fingers crossed, or via weaker means like imitation. This is what's driving the "jagged" frontier of progress in LLMs. Tasks that are verifiable progress rapidly, including possibly beyond the ability of top experts (e.g. math, code, amount of time spent watching videos, anything that looks like puzzles with correct answers), while many others lag by comparison (creative, strategic, tasks that combine real-world knowledge, state, context and common sense). Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.

---

<a id="19-1979644538185752935"></a>
## 19. 关于LLM Agent的思考

> **链接**：[https://x.com/karpathy/status/1979644538185752935](https://x.com/karpathy/status/1979644538185752935)

On LLM agents. My critique of the industry is more in overshooting the tooling w.r.t. present capability. I live in what I view as an uncomfortable gap between the tooling and the capability. AI timelines are about 5-10X pessimistic.

---

<a id="20-1971220449515516391"></a>
## 20. AI不会取代放射科医生

> **链接**：[https://x.com/karpathy/status/1971220449515516391](https://x.com/karpathy/status/1971220449515516391)

Expectation: rapid progress in image recognition AI will delete radiology jobs (e.g. as famously predicted by Geoff Hinton). Reality: 'AI isn't replacing radiologists' — good article.

---

<a id="21-1939709449956126910"></a>
## 21. nanoGPT 递归自我改进

> **链接**：[https://x.com/karpathy/status/1939709449956126910](https://x.com/karpathy/status/1939709449956126910)

Love this project: nanoGPT -> recursive self-improvement. nanoGPT is a super simple, tiny educational codebase (~750 lines of code) for the pretraining stage of building LLMs.

---

<a id="22-1937902205765607626"></a>
## 22. Context Engineering > Prompt Engineering

> **链接**：[https://x.com/karpathy/status/1937902205765607626](https://x.com/karpathy/status/1937902205765607626)

+1 for 'context engineering' over 'prompt engineering'. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information.

---

<a id="23-1935518272667217925"></a>
## 23. AI Startup School 演讲

> **链接**：[https://x.com/karpathy/status/1935518272667217925](https://x.com/karpathy/status/1935518272667217925)

LLMs are a new kind of computer, and you program them in English. Hence I think they are well deserving of a major version upgrade in terms of software.

---

<a id="24-1917920257257459899"></a>
## 24. LLM的GUI还没被发明

> **链接**：[https://x.com/karpathy/status/1917920257257459899](https://x.com/karpathy/status/1917920257257459899)

Chatting with LLM feels like using an 80s computer terminal. The GUI hasn't been invented yet, but imo some properties of it can start to be predicted.

---

<a id="25-1915581920022585597"></a>
## 25. AI辅助编码的节奏

> **链接**：[https://x.com/karpathy/status/1915581920022585597](https://x.com/karpathy/status/1915581920022585597)

Noticing myself adopting a certain rhythm in AI-assisted coding (i.e. code I actually care about): Don't ask for code, ask for a few high-level approaches, pros/cons. There's almost always a few ways to do thing and the LLM's judgement is not yet reliable enough to defer to.

---

<a id="26-1886192184808149383"></a>
## 26. Vibe Coding 的诞生

> **链接**：[https://x.com/karpathy/status/1886192184808149383](https://x.com/karpathy/status/1886192184808149383)

There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's not really coding - I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works.

---

<a id="27-1813263734707790301"></a>
## 27. 创立 Eureka Labs

> **链接**：[https://x.com/karpathy/status/1813263734707790301](https://x.com/karpathy/status/1813263734707790301)

Excited to share that I am starting an AI+Education company called Eureka Labs.

---

<a id="28-1811467135279104217"></a>
## 28. LLM Agent 教育愿景

> **链接**：[https://x.com/karpathy/status/1811467135279104217](https://x.com/karpathy/status/1811467135279104217)

A simple, minimal, clean training stack for a full-featured LLM agent, in direct C/CUDA, and companion educational materials to bring many people up to speed.

---

<a id="29-1674873002314563584"></a>
## 29. AI工程师的崛起

> **链接**：[https://x.com/karpathy/status/1674873002314563584](https://x.com/karpathy/status/1674873002314563584)

I think this is mostly right. \- LLMs created a whole new layer of abstraction and profession. \- I've so far called this role "Prompt Engineer" but agree it is misleading. It's not just prompting alone, there's a lot of glue code/infra around it. Maybe "AI Engineer" is ~usable, though it takes something a bit too specific and makes it a bit too broad. \- ML people train algorithms/networks, usually from scratch, usually at lower capability. \- LLM training is becoming sufficently different from ML because of its systems-heavy workloads, and is also splitting off into a new kind of role, focused on very large scale training of transformers on supercomputers. \- In numbers, there's probably going to be significantly more AI Engineers than there are ML engineers / LLM engineers. \- One can be quite successful in this role without ever training anything. \- I don't fully follow the Software 1.0/2.0 framing. Software 3.0 (imo ~prompting LLMs) is amusing because prompts are human-designed "code", but in English, and interpreted by an LLM (itself now a Software 2.0 artifact). AI Engineers simultaneously program in all 3 paradigms. It's a bit ![😵‍💫](https://abs-0.twimg.com/emoji/v2/svg/1f635-200d-1f4ab.svg)
Quote
swyx
@swyx

Jun 30, 2023
![🆕](https://abs-0.twimg.com/emoji/v2/svg/1f195.svg) Essay: The Rise of the AI Engineer https://latent.space/p/ai-engineer Keeping up on AI is becoming a full time job. Let's get together and define it.

---

<a id="30-1468370605229547522"></a>
## 30. AI领域的整合趋势

> **链接**：[https://x.com/karpathy/status/1468370605229547522](https://x.com/karpathy/status/1468370605229547522)

The ongoing consolidation in AI is incredible. Thread: When I started ~decade ago vision, NLP, speech, RL were separate fields with different architectures, conferences, researchers...

---
