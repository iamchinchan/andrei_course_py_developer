# The Complete Claude.ai Interface Guide — Plans, Models, Skills, Connectors, Plugins & Automation

I looked this up against Anthropic's current support documentation rather than relying on memory, since pricing/features change. Here's everything, organized the way you asked.

---

## PART 1: Free vs Paid — What You Actually Get

| Plan | Price | What changes |
|---|---|---|
| **Free** | $0 | Real, fully-functional Claude — not a stripped demo. Daily message limit (resets periodically), access to the current default model, Projects, file uploads, and **Memory** (yes — Memory works on Free too) |
| **Pro** | ~$20/month (~$17/month billed annually) | Roughly 5x the message allowance of Free, access to all models including the top-tier one, and unlocks Cowork (Anthropic's desktop app for delegating bigger multi-step work) |
| **Max** | $100/month or $200/month | Same features as Pro, just much higher usage ceilings (5x and ~20x Pro respectively) — built for people who hit Pro's limits constantly, not extra capabilities |
| **Team** | ~$25-30/seat/month, 5-seat minimum | Everything in Pro + admin controls, centralized billing, org-wide skill/connector sharing |
| **Enterprise** | Custom pricing | SSO, compliance certifications, dedicated support, custom limits |

**Important, directly answering your question:** Skills, Connectors, and Plugins do **not cost extra** on top of whatever plan you're on — they run within your existing plan's usage limits, free plan included. You're not paying separately to use any of these three features.

---

## PART 2: Apps & Extensions — What Exists Beyond the Web Chat

- **Claude Desktop** — a full app for Mac/Windows, includes chat, Cowork, and Claude Code
- **Claude mobile app** (iOS/Android) — same core Claude, works with Cowork remotely too
- **Claude Cowork** — an agentic "do multi-step work for me" app for non-developers, available on every plan including Free, though heavier usage naturally benefits from Pro's higher limits(I doubt for fre mode)
- **Claude Code** — the coding-focused agent, usable from terminal, VS Code, JetBrains, or the desktop app
- **Claude for Chrome** — a browsing agent extension
- **Claude for Excel / PowerPoint** — agents built into those Microsoft apps specifically for spreadsheet/slide work

---

## PART 3: Model Selection & "Effort" (Thinking)

Unlike AI Studio's separate "Thinking Level" slider, Claude's version of this is a **model picker + an extended thinking toggle**:

- **Model choice** — you pick between different Claude models (currently: Haiku for fast/cheap simple tasks, Sonnet for the balanced everyday default, Opus for the most capable/complex reasoning) — this is the rough equivalent of AI Studio's model dropdown
- **Extended thinking** — a toggle that lets Claude work through a problem step-by-step internally before answering, for harder reasoning/math/coding tasks — directly equivalent to AI Studio's "Thinking Level: High" concept, just presented as an on/off (or budget) control rather than a slider

**When to use which:** simple questions/casual chat → default model, no extended thinking needed. Complex coding, math, or multi-step logic → a stronger model + extended thinking on, accepting the slower response for better accuracy — exactly the same trade-off we covered with AI Studio's Thinking Level.

---

## PART 4: Skills — What They Are, How to Make Them, Do They Persist

### What a Skill actually is
A Skill is a **set of instructions (often just a text file, sometimes bundled with scripts) that teaches Claude how to do a specific recurring task your way** — your brand voice for blog posts, your company's proposal format, a specific document-formatting style. It's not code you have to write — it's closer to a detailed instruction sheet Claude reads and follows whenever relevant.

### Can you create your own, on the free plan?
**Yes.** You don't need to write it manually — you can just tell Claude "create a new skill," and it walks you through naming it and writing the instructions conversationally, generating the file for you. You can also install pre-built skills from the built-in directory (exactly the "Skills" tab in your first screenshot) without writing anything yourself.

### How to manage them
Go to **Customize → Skills** in the sidebar → click the `+` button → either toggle on a built-in example skill, or upload your own. One requirement: Skills need the **"Code execution and file creation"** feature enabled in your settings to work (this is the same toggle mentioned in the system settings we've referenced throughout this conversation).

### Does Claude retain a Skill across DIFFERENT chats, or just within one?
**Skills persist across all your chats, not just the conversation where you created them.** Once installed/enabled in Customize → Skills, it's available and automatically used whenever relevant, in any new conversation you start — you don't need to re-add it each time.

### Note on this being separate from "Memory"
Your other question — "will Claude retain my study-session info across chats" — is actually a **different feature: Memory**, not Skills. Memory is Claude automatically remembering facts you've told it (your name, preferences, ongoing projects — exactly the system you've seen working throughout THIS conversation) across sessions. Memory is available on all plans, free included. Skills are reusable INSTRUCTIONS/workflows; Memory is remembered FACTS about you. Both persist across chats, but they're solving different problems.

---

## PART 5: Connectors — What They Are, Cost, and the Real Risk

### What a Connector is
A Connector links Claude to an actual external service — Gmail, Google Drive, Slack, Notion, and dozens more — using **MCP (Model Context Protocol)**, the same standard we discussed earlier in this conversation's orchestration section. Once connected, Claude can read data from that service and, in some cases, take limited actions in it.

### Are they free?
**Yes — Connectors themselves are free to use, available even on the Free plan** (Google Workspace connectors specifically are confirmed available to all users, free plan included).

### The Gmail example, precisely — answering your exact automation question
This is important and directly addresses what you asked: **Claude's Gmail connector can read emails and CREATE DRAFTS, but the "send" function is deliberately disabled.** Every email must be manually sent by YOU from your actual Gmail — Claude cannot autonomously send emails on your behalf, by design. This is a deliberate safety choice, not a current limitation waiting to be lifted — the reasoning is exactly what you'd expect: giving an AI unsupervised send-access to your email is a real risk (accidental sends, manipulation via malicious content it reads, spam-flagging your account), so the review step (you personally hitting "send") is the actual safety mechanism.

### So can you "prompt it once and it just works on your behalf automatically going forward"?
**Within an active conversation, yes** — once connected, you can just say "check my unread emails and draft replies to the urgent ones," and Claude will use the connector to do that whole multi-step task without you manually walking it through each step. But this happens **when you prompt it**, in a live session — it's not a standing background service silently running 24/7 without any prompt at all, checking your email every hour on its own, unless you're specifically using a scheduled/automation feature built for that (worth checking current docs at support.claude.com if that's specifically what you want, since scheduling capabilities are an evolving area).

### The real risk to understand — the "Lethal Trifecta"
This is worth knowing precisely, security-wise. Real risk emerges when THREE things combine at once:
1. Access to your **private/sensitive data** (via a connector, e.g., Notion, Gmail)
2. Exposure to **untrusted content** (e.g., an email or document containing hidden malicious instructions)
3. An **ability to communicate externally** (e.g., another connector that can send data out)

If all three are active simultaneously, a malicious document/email COULD theoretically try to manipulate Claude into leaking your private data somewhere. **Real mitigations:** only enable the specific connector(s) you actually need for the task at hand (don't leave everything on all the time), and use "needs approval" permission settings for any action that writes/deletes/sends, so nothing happens without your explicit review.

---

## PART 6: Plugins — What They Are, Cost

### What a Plugin is
A Plugin is a **pre-packaged bundle** combining Skills + Connectors + (in Cowork specifically) sub-agents into one installable toolkit built for a specific job function — sales, marketing, legal work, a coding workflow, etc. Instead of manually setting up 5 separate Skills and 3 separate Connectors yourself, one Plugin install gives you the whole working setup at once.

### Are they free?
**Yes — Plugins run on whatever plan you already have; no separate cost.** Some plugins are "Anthropic Verified" (passed an additional quality/safety review), and organizations can also distribute custom internal plugins to their teams.

### How to use them
**Customize → Plugins → Browse Plugins → Install** (exactly the "Directory" panel in your first screenshot) — after installing, its bundled skills show up automatically when you type `/` or hit the `+` button in chat.

---

## PART 7: Direct Answers to Your Specific Automation Questions

**"If I connect and prompt it to read Gmail/send mail automatically, will it cost me?"**
No extra cost — connectors run within your existing plan's usage limits. But "send mail automatically" specifically won't happen even for free — Gmail's send function is disabled by design; Claude can only draft, you send.

**"Can I provide tools via connectors for free, and Claude will link/work on my behalf?"**
Yes — connecting a service is free, and once connected, Claude genuinely can read data and take certain approved actions (drafting, searching, organizing) within a conversation where you prompt it to.

**"With just a prompt after linking, can Claude do work on my behalf?"**
Yes, within an active session — that's the whole point of connectors. It's not silent, unattended, always-running automation by default; it acts when you ask it to, in response to your prompt, and asks for approval on higher-stakes actions (like actually sending something) rather than doing them unsupervised.

**"Can I automate stuff with these?"**
Yes, meaningfully — this is genuinely how people build real recurring workflows (checking email, summarizing documents, updating a project tracker) using Skills (your repeatable instructions) + Connectors (real data access) together. Just be aware of the Lethal Trifecta risk above, and know that the highest-risk actions (sending, deleting) are deliberately kept behind a manual approval/send step rather than fully autonomous, as a genuine safety design choice — not a missing feature.

---

## Quick Master Comparison

| | Skills | Connectors | Plugins |
|---|---|---|---|
| **What it is** | Reusable instructions/workflow | Link to an external service/data source | Bundle of Skills + Connectors + sub-agents |
| **Free to use?** | Yes, all plans | Yes, all plans | Yes, runs on your existing plan |
| **Persists across chats?** | Yes | Yes (stays connected until you disconnect) | Yes |
| **Can you build your own?** | Yes — just ask Claude to create one | No (you connect to an existing service) | Yes, for organizations distributing to teams |
| **Real risk to know** | Low — it's just instructions | Higher — real data access; watch the Lethal Trifecta | Same as whatever Skills/Connectors it bundles |

For anything specific to your exact plan/limits at the moment you're reading this, the numbers above are a snapshot — worth double-checking at **claude.com/pricing** and **support.claude.com**, since these details do get updated over time.


