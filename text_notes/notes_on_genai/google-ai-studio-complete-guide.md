# Google AI Studio — Complete Interface Guide (Run Settings, Tools, Advanced Settings & Agent Environment)

This covers everything visible in your three screenshots, in the order they appear, explained from zero.

---

# PART 1: The Top of the Panel — Model Selector

## "Gemini Pro Latest" / "gemini-pro-latest"

This is the **model picker.** `gemini-pro-latest` is an **alias** — instead of locking you to one specific dated model version, this alias automatically points to whichever Pro-tier model is currently Google's newest, so your saved settings/code keep using an up-to-date model without you manually updating a version number every time Google releases something new.

**When to use it:** good default when you always want "the best available Gemini Pro" without tracking version numbers yourself. If you need perfectly consistent, unchanging behavior for something in production long-term, you'd instead pin an exact dated model version, since "latest" can shift underneath you over time.

---

# PART 2: System Instructions

**What it is:** a separate text box where you set persistent behavior rules for the model — tone, role, format, constraints — that apply to EVERY message in the conversation, not just one prompt.

## Why it's separate from just typing instructions in the chat box
This is the most important distinction to understand: **content typed in the regular chat box is a suggestion the model weighs alongside everything else; System Instructions carry much stronger, foundational priority** — think of it as the difference between a passing comment and a standing rule the model treats as close to non-negotiable throughout the whole conversation.

```
Example System Instruction:
"You are a technical documentation writer. Always respond in 
formal English, use bullet points for lists, and never use emojis."
```

## When to use it
- Building an app/bot with a consistent persona or output format across many different user messages
- Enforcing constraints that must NEVER be violated, regardless of what the user later asks in chat
- Setting domain/role context ("You are a customer support agent for a plumbing company")

## When NOT needed
- One-off, single-question testing in the playground — just type your question directly in the chat box instead

---

# PART 3: Temperature

**What it is:** a slider (0 to 2, default around 1) controlling **how random/creative vs. focused/predictable** the model's word choices are.

```
Low Temperature (0.0 - 0.3)  → Deterministic, focused, repeats the 
                                 "safest"/most probable word every time
                                 → BEST for: code generation, factual 
                                    Q&A, data extraction, summarization
                                    
Balanced (0.4 - 0.7)         → General-purpose tasks, some creative 
                                 flexibility with constraints

High (0.8 - 2.0)             → Explores less-probable word choices, 
                                 more surprising/creative output
                                 → BEST for: brainstorming, poetry, 
                                    creative writing
                                 → RISK: at very high settings, 
                                    output can become incoherent or 
                                    drift off-topic
```

**Important real-world caution (this comes directly from Google's own guidance):** high temperature makes the model prioritize "sounding fluent" over "being factually correct" — if you need accurate facts, keep temperature low (below ~0.2). Also worth knowing: for the newest Gemini 3 models specifically, Google now recommends generally leaving temperature at its default (1.0) rather than manually lowering it, since forcing it very low can sometimes cause looping/repetition issues on complex reasoning tasks in these newer models specifically.

---

# PART 4: Thinking Level

**What it is:** controls how much internal step-by-step reasoning the model does BEFORE producing its final answer — essentially the "inference-time scaling" concept we discussed earlier in this conversation, made into a user-adjustable setting.

```
Thinking Level: Low  → Fast, cheap, minimal internal reasoning steps
                        → Good for: simple questions, quick replies, 
                           casual conversation ("write a thank-you email")

Thinking Level: High → Slower (can be several times slower), but 
                        noticeably more logical/thorough — the model 
                        works through the problem more like a person 
                        reasoning on paper before answering
                        → Good for: logic puzzles, complex architecture/
                           coding decisions, multi-step problems
                        → Wasteful for: simple tasks — you pay in 
                           latency for reasoning depth you don't need
```

**Rule of thumb:** match the thinking level to the actual difficulty of the task — using "High" for a casual one-line question just adds unnecessary delay for no real benefit.

---

# PART 5: Tools (Image 2)

Each toggle here gives the model an extra CAPABILITY beyond just generating text from its own trained knowledge — exactly the "tool calling" concept from our earlier orchestration discussion.

## Structured Outputs
Forces the model's response to conform to a specific data format/schema you define (e.g., strict JSON with exact field names), instead of free-form prose.
**When to use:** you're feeding the output into another program/database that needs predictable, parseable structure — data extraction, building an app that consumes the AI's response programmatically.

## Code Execution
Lets the model actually WRITE and RUN code (in a sandboxed environment) to compute something, rather than just guessing an answer from pattern-matching alone.
**When to use:** math-heavy questions, data analysis, anything where you want a verified computed answer rather than the model's "best guess" at arithmetic (remember — pure language prediction is genuinely unreliable at exact calculation; letting it run real code fixes that).

## Function Calling
Lets the model call YOUR OWN custom-defined functions/APIs (not Google's built-in tools) — e.g., "check my company's inventory database" or "call this specific weather API." You define what functions exist and what they do; the model decides when to invoke them based on the conversation.
**When to use:** building a real application that needs the model to interact with your own systems/data, not just Google's built-in web search or maps.

## Grounding with Google Search
Lets the model actually run live Google searches and base its answer on real, current search results — rather than only its (potentially outdated) training data. This is conceptually identical to the web_search tool I use in this very conversation.
**When to use:** anything involving current events, recent facts, or information that could have changed since the model's training cutoff. **When NOT to use:** simple logic/reasoning tasks — turning this on unnecessarily adds latency and can introduce irrelevant "noise" from web results into otherwise straightforward answers.

## Grounding with Google Maps
Same grounding concept, but specifically pulls in real, current location/place data from Google Maps (addresses, business info, geographic details) rather than the model's memorized/possibly-outdated knowledge of places.
**When to use:** apps involving real-world locations, directions, business info lookups.

## URL Context
Lets you give the model a specific web link, and it will actually fetch and read that page's content as part of forming its answer — rather than guessing based on the URL alone or old training data about that page.
**When to use:** "summarize this article," "what does this documentation page say" — anywhere you want the model reading one specific, real source directly.

---

# PART 6: Advanced Settings (Image 2, continued)

## Media Resolution
Controls how much visual detail/token-budget is spent processing images, video, or PDFs you upload — higher resolution = more accurate reading of fine visual detail (like small text in a PDF), but costs more tokens/processing.

## Safety Settings
Google's models have built-in content-safety filters across several categories (typically: Harassment, Hate Speech, Sexually Explicit content, Dangerous Content). This panel lets you adjust the **sensitivity threshold** for each category — how aggressively borderline content gets blocked.
**When to adjust:** developers building specific applications (e.g., medical, legal, or creative-writing tools) sometimes need to carefully tune these thresholds for their legitimate use case — this is NOT a way to bypass genuine safety protections, but a way to reduce false-positive over-blocking for legitimate professional content that a default filter might flag unnecessarily.

## Add Stop Sequence
A specific string of text that, if the model generates it, immediately halts generation right there. Useful for enforcing a hard structural boundary — e.g., stopping generation the instant the model writes `"###END###"`, for programmatic parsing.

## Output Length
The maximum number of tokens the model is allowed to generate in one response — a hard ceiling, same concept as the "hard technical cap" we discussed in the AI response-length conversation earlier.

## Top P
A second randomness-control dial, related to Temperature but working differently: instead of adjusting HOW randomly words are picked, Top P limits the POOL of words the model is even allowed to consider at each step, cutting off unlikely options entirely before any randomness is applied.
```
Top P = 0.95 → model only considers the smallest set of words whose 
               combined probability adds up to 95%, discarding the 
               remaining unlikely long-tail options entirely
```
**Practical note:** Temperature and Top P interact; most guidance suggests adjusting mainly ONE of them at a time, rather than aggressively tuning both simultaneously.

---

# PART 7: Antigravity Agent Preview — What This Actually Is (Image 3)

This is a **different mode entirely** from the normal chat/prompt playground shown in Images 1–2 — it's Google's newer **agentic mode**, where instead of just generating text back to you, the model can autonomously take real actions: writing and running code, browsing, and managing files, inside its own dedicated remote environment.

## "A general-purpose autonomous agent running in a remote, Google-hosted Linux environment"
This is the key sentence to understand: rather than just answering in a chat window, this mode gives the model an **actual remote Linux computer** (hosted by Google, not your own machine) that it can freely act inside of — writing files, running terminal commands, executing code — much closer to the "agent" concept from our earlier orchestration discussion, where the model can loop through "decide action → take action → observe result → decide next action" on its own, rather than a single one-shot text reply.

## Tools section (specific to this agent mode)
- **Code Execution, Grounding with Google Search, URL Context** — same meanings as Part 5 above, just now used autonomously by the agent as part of a longer working process, not just for one text answer
- **Filesystem tools** — lets the agent actually create, read, edit, and organize files inside its remote environment, rather than only outputting text — this is what makes it capable of genuinely "building a project" across multiple files, not just describing one

## The "Environment" section — this is the part you specifically asked about

**"Each execution spins up an isolated environment where your agent can run code and manage files"** — every time you run this agent, Google provisions a **fresh, sandboxed, temporary virtual computer** specifically for that run. "Isolated" means: nothing the agent does here can affect your real computer or any other environment — it's a contained, disposable Linux box, similar in spirit to the sandboxed testing environment we discussed with SSH earlier, just automatically created and destroyed by Google per run.

### Type: New / Existing
- **New** — spin up a completely fresh, empty environment for this run, with nothing carried over from any previous session
- **Existing** — resume/reuse a previously created environment, keeping whatever files/state the agent already built up in an earlier run, instead of starting from scratch

### Sources
This lets you feed the agent **starting material** to work from before it begins — e.g., an existing code repository, uploaded documents, or reference files — so the agent doesn't start completely blank, but has real context/existing code to build on or modify.

### Network — "Add rules"
This controls what the agent's remote environment is allowed to reach **on the actual internet.** Since the agent can autonomously run code and make requests, this is a genuine security boundary: by default, you can restrict/whitelist which external domains/services the isolated environment is permitted to contact — preventing an autonomous agent from freely reaching arbitrary external servers, uploading data somewhere unintended, or downloading and running untrusted code from anywhere it wants. This is precisely the kind of guardrail that matters MORE here than in the plain chat mode, because this mode can actually take real, autonomous action instead of just producing a text answer for you to review first.

## Why this exists as a totally separate mode from the normal chat
The plain "Gemini Pro Latest" mode (Images 1-2) is fundamentally a **single question → single answer** system — you stay in full control of every step. The Antigravity agent mode is built for **delegating a whole task** ("build me this app," "fix this bug across these files") and letting the model work autonomously through multiple steps on its own, inside a safely contained sandbox — which is exactly why it needs its own separate settings for environment isolation, sources, and network restrictions that the simple chat mode doesn't need at all.

---

# PART 8: Get Code

The button at the top of every settings panel (`<> Get code`) converts whatever configuration you've built in this visual UI (model choice, system instructions, temperature, tools enabled, etc.) into ready-to-use **API code** (Python, JavaScript, etc.) that a developer can paste directly into their own application — letting you experiment visually first, then take the exact same configuration into real production code without manually re-writing it from scratch.

---

## Quick Master Reference Table

| Setting | One-line purpose | Use when |
|---|---|---|
| Model picker | Choose which underlying model answers | Match model size/capability to task complexity |
| System Instructions | Persistent, high-priority behavior rules | Building a consistent bot/app persona |
| Temperature | Controls randomness/creativity of word choice | Low for facts/code, high for creative writing |
| Thinking Level | How much internal reasoning happens before answering | High for complex logic, low for simple/fast replies |
| Structured Outputs | Force a strict data format (e.g., JSON) | Feeding output into another program |
| Code Execution | Model writes/runs real code | Math, data analysis, verified computation |
| Function Calling | Model calls YOUR custom functions/APIs | Connecting to your own systems/data |
| Grounding (Search/Maps) | Model uses live, real-world data instead of memory | Current events, real locations, up-to-date facts |
| URL Context | Model reads one specific webpage you provide | Summarizing/analyzing a specific real page |
| Media Resolution | Detail level for processing images/PDFs/video | Higher for fine print/small text, lower for speed/cost |
| Safety Settings | Adjust content-filter sensitivity | Legitimate professional use cases needing fewer false positives |
| Stop Sequence | Hard string that halts generation immediately | Programmatic parsing needing a clean cutoff |
| Output Length | Max tokens the response can generate | Controlling response length/cost |
| Top P | Limits the pool of words considered, before randomness | Fine-tuning alongside (not instead of) Temperature |
| Antigravity Agent mode | Autonomous multi-step agent in a real remote sandbox | Delegating a whole build/fix task, not just one Q&A |
| Environment Type (New/Existing) | Fresh sandbox vs. resuming a previous one | Continuing prior agent work vs. starting clean |
| Sources | Starting material fed to the agent | Giving it existing code/docs to build from |
| Network rules | Whitelist what the sandbox can reach online | Security boundary for autonomous internet access |
| Get Code | Exports your visual settings as real API code | Moving from experimentation to production |


Short answer: **not directly from AI Studio itself — but yes, using what it gives you.** Here's the precise distinction, since this is exactly the kind of thing worth being clear-eyed about before you invest time in it.

## What AI Studio actually is
It's a **testing/prototyping console + API access point.** It lets you experiment with prompts, settings, and tools, then hit "Get Code" to export that configuration as code. It is **not itself** an app that sits on your desktop watching your screen or doing tasks in the background — it's the workshop where you design the AI's behavior, not the finished tool.

## Two real paths to what you're describing

### Path 1: Google Antigravity (the separate product I mentioned in the last file)
This is the actual **desktop-agent-style tool** — a standalone IDE app (built on VS Code) where Gemini agents can autonomously write/run code, browse, and manage files in a real environment on your behalf, with a "manager view" to delegate whole tasks rather than one Q&A at a time. This is much closer to what you're picturing — but it's aimed at **coding/software tasks** specifically (building apps, fixing bugs, running terminal commands), not general life admin ("book my appointments," "organize my desktop files").

### Path 2: Build your own agent using AI Studio's API + Function Calling
This is the flexible, DIY route:
```
1. In AI Studio, you design the "brain" — the prompt, system 
   instructions, and which Function Calling tools it can request
2. You "Get Code" to export this as a real API integration
3. YOU write the actual surrounding program (Python/Node script) 
   that runs on your computer, defines real functions 
   ("open_file", "send_email", "click_button", etc.), and executes 
   whatever the model asks for
4. This is precisely the "orchestration" pattern from our earlier 
   conversation — AI Studio configures the model, but the actual 
   "desktop agent" is a program YOU build around it
```
This is genuinely how most "AI does tasks on my computer" tools are built under the hood — they're not AI Studio itself, they're custom apps calling Gemini's (or another provider's) API with function-calling enabled.

## The honest bottom line

**AI Studio alone won't give you a running desktop agent — it's the design/testing layer, not the deployed app.** If you want something coding-related, Antigravity is the closest existing Google product built for exactly that. If you want a general personal-task agent, you'd be building your own lightweight app around the Gemini API (using what you already learned about function calling, tool orchestration, and access tokens in this conversation) — which is a real, doable project, just one you'd have to build yourself rather than flip a switch for inside AI Studio.