# Every Claude App/Surface — Fully Elaborated: Free or Not, Automated or Not, What It Can/Can't Do

## The full list, one at a time, in plain detail

---

### 1. Claude.ai (the basic web chat) — where this whole conversation has been happening

**Free or not:** Free, real, fully functional — this is what you've been using this entire time.

**Is it automated / agent-like?** **No.** This is a straightforward Q&A chat. You ask, it answers, in ONE response at a time. It cannot take multi-step actions on its own, cannot browse your files, cannot control anything outside this text box — unless you've enabled specific Connectors (Gmail, Drive, etc.), in which case IT CAN use those, but only when YOU prompt it in that exact moment, one request at a time, not autonomously running in the background.

**What it CAN do:** answer, search the web, create files/artifacts you download, use connected tools if you have them enabled — all reactively, per your message.

**What it CANNOT do:** run continuously without you prompting, control your desktop, open apps on your computer, act while you're not actively chatting with it.

---

### 2. Claude Desktop App (Mac/Windows)

**Free or not:** The app itself is free to download and use for basic chat. **Cowork and Claude Code specifically, INSIDE this app, require a paid plan (Pro or above)** — the desktop app is just the container; what unlocks inside it depends on your subscription.

**Is it automated?** Only the Cowork/Code portions are agent-like (see below) — the plain "Chat" tab inside Desktop behaves exactly like Claude.ai, non-automated.

---

### 3. Claude Cowork (Pro/Max/Team/Enterprise only — confirmed NOT free)

This is the actual **agentic, multi-step "do this whole task" mode** — the closest thing to what you saw in Antigravity.

**What it CAN actually do, concretely:**
- Read/write/organize real files on your computer (desktop version specifically)
- Write and run code
- Create real documents, spreadsheets, slides as actual output files
- Use your connected Skills and Connectors across MULTIPLE steps in a row, without you re-prompting after each one — e.g., "check these 5 emails, summarize each, put it in a doc" happens as one continuous task
- Work for extended periods (longer sessions than a normal chat), and on web/mobile (Max+), keep running even after you close the app

**What it CANNOT do (the real limits):**
- **Cannot send emails, delete things, or take irreversible actions without your explicit approval** — anything high-stakes still pauses and asks you first, by design, same as we covered with the Gmail connector
- Cannot control arbitrary desktop apps outside of what its specific tools/connectors support (it's not literally moving your mouse and clicking random buttons across your whole OS — it's not what's usually called a "computer use" screen-control agent by default, though Anthropic has separate, more experimental computer-control capabilities that aren't the same thing as standard Cowork)
- **No plugin installs at all on Free** — but this is moot anyway since Cowork itself isn't on Free
- Memory (what Claude remembers about you in regular chat) does NOT carry into Cowork sessions yet — they're currently separate memory pools, except within Cowork "projects" specifically

**Where the actual "limit" hits:** your PLAN's usage allowance. Cowork draws from the same usage pool as regular chat — long multi-step tasks (lots of file reading, tool calls, planning) consume that allowance faster than a normal short chat reply, so heavy Cowork use burns through Pro's limits noticeably quicker, which is exactly why Anthropic pushes heavy users toward Max.

---

### 4. Claude mobile app (iOS/Android)

**Free or not:** Free to download; same rule as Desktop — basic chat is free, Cowork-on-mobile requires Max specifically right now (rolling out gradually, Max first).

**Automated?** Same split as above — plain chat, no; Cowork portion, yes, agentic, and specifically useful here because a Cowork task can keep running in Anthropic's cloud even after you close the mobile app, letting you check back later.

---

### 5. Claude Code

**Free or not:** Requires a paid plan (part of Pro and above) — it is NOT a free-tier feature.

**Automated?** Yes — fully agentic for coding specifically: it can read/write/edit real code across multiple files, run terminal commands, fix bugs, and iterate on its own within a session, with your approval checkpoints along the way (you can configure how much autonomy you give it). Usable from terminal, VS Code, JetBrains, or inside the Desktop app.

**What it's for, specifically:** software development — writing/debugging/refactoring real codebases. It is NOT for general life-admin tasks (booking things, managing email) — that's Cowork's job instead.

---

### 6. Claude for Chrome

**Free or not:** This has been rolling out as a limited/beta browser extension, generally tied to paid plans — check current availability, since browser-extension rollouts change frequently.

**Automated?** Yes — this is a genuine **browsing agent**: it can navigate real websites, click buttons, fill forms, extract information from pages, on your behalf, inside your actual Chrome browser. This is the closest Claude gets to literally "controlling your screen," but scoped specifically to the browser, not your whole desktop OS.

**Real limit/risk:** because it can click/submit real forms on real websites, this is exactly where the "Lethal Trifecta" risk from earlier matters most — a malicious webpage could theoretically try to manipulate it, so approval prompts and careful scoping matter here more than almost anywhere else.

---

### 7. Claude for Excel / PowerPoint

**Free or not:** Bundled specifically with paid plans (part of the Pro-and-above feature set, similar to Cowork/Code).

**Automated?** Yes, but narrowly scoped — it works INSIDE Excel/PowerPoint specifically, building formulas, cleaning data, generating slides — genuinely autonomous within that one app, but it doesn't reach outside Excel/PowerPoint into your broader desktop.

---

## Direct Answer: "Will it work as an agent for my desktop?"

**Yes, specifically through Cowork (Pro and above) — but with real boundaries.** It can read/write your files, run code, and complete multi-step tasks autonomously within a session — but it stops and asks you before anything irreversible (sending, deleting, purchasing), and it's not a general "controls your entire OS, clicks anything, anywhere" agent by default. It's scoped to the tools/connectors/files you've explicitly given it access to.

---

## How This Differs From AI Studio / Antigravity — The Core Distinction

| | Google AI Studio / Antigravity | Claude (Cowork/Code) |
|---|---|---|
| Primary focus | Antigravity specifically = coding/software-building in a real, isolated remote Linux sandbox | Cowork = general knowledge work (docs, spreadsheets, email, files); Claude Code = coding specifically |
| Environment | Antigravity spins up a **fresh, isolated, disposable remote VM** per run, with explicit Network access rules | Cowork/Code typically act on YOUR ACTUAL local machine/files (desktop) or your real connected accounts (Gmail, Drive) — not a disposable sandbox VM by default |
| Free tier | AI Studio itself (prototyping/API access) is free; Antigravity specifically has had free access phases as a preview product | Cowork/Claude Code: **not free**, requires Pro or above |
| Autonomy level | Very high — designed for "build this whole app," looping autonomously for long stretches inside its sandbox | Deliberately capped at high-stakes moments — pauses for your approval before sending/deleting/irreversible actions |
| Best for | Building/testing software projects in a disposable, safe, isolated environment | Real day-to-day work directly on your real files/accounts, with built-in human-approval checkpoints for anything risky |

## The one-paragraph summary tying it all together

**Basic Claude.ai chat is free and purely reactive (no automation). Real automation/agent capability lives specifically in Cowork (general work) and Claude Code (coding) — both require a paid plan, both can genuinely do multi-step tasks on your real files/accounts without you re-prompting at every step, but both deliberately stop and ask your permission before anything irreversible, unlike a fully autonomous sandboxed agent like Antigravity, which is built to run much more independently precisely because it's operating in a disposable, isolated environment rather than your actual live computer and real accounts.**
