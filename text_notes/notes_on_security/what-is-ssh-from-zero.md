# SSH — What It Actually IS, From Absolute Zero

## The most basic definition first

**SSH (Secure Shell) is a PROTOCOL** — a set of rules two computers agree to follow — that lets you **remotely control another computer using text commands, over the internet, safely.**

Think of it like this: imagine you could type commands on YOUR laptop, but those commands actually run on a completely different computer sitting in a data center on the other side of the world — and you see that computer's output/response right there on your own screen. That's literally what SSH does. It's a **remote command-line control tool.**

## Who "has" SSH? Nobody owns it — it's free, open software

This is the part that's genuinely confusing if nobody tells you: **SSH is not a product, not a company, not something you buy or subscribe to.** It's:

- An **open protocol/specification** — publicly documented rules, like how HTTP (the web) is also an open protocol nobody "owns"
- Implemented by **free, open-source software** — the most common one is called **OpenSSH**, which comes pre-installed on almost every Linux/Mac computer, and is now even built into Windows by default
- **Nobody pays for SSH itself.** It's just software sitting on your computer already, like how "typing" isn't something you pay for — it's just a built-in capability.

### So what DO people pay for, then?
People pay for the **REMOTE COMPUTER itself** (the server) — not for SSH. For example: you might rent a virtual server from Amazon (AWS), DigitalOcean, or Google Cloud for $5-$50/month. That rented computer comes with SSH software already running on it, ready for you to connect to, for free, using the SSH protocol. **SSH is the free doorway; the server/computer behind that door is what costs money.**

## Two sides, every single time: Client and Server

| Role | What it is | Example |
|---|---|---|
| **SSH Client** | The software on YOUR computer that initiates the connection | Terminal app on Mac/Linux, PowerShell/Terminal on Windows, or apps like PuTTY |
| **SSH Server** | The software running on the REMOTE computer, listening for incoming connections | `sshd` (SSH daemon) — runs quietly in the background on Linux servers, cloud VMs, etc. |

Both sides need SSH software running — but again, this software itself is free and usually pre-installed.

## Who actually uses SSH, in real life?

- **Software developers** — logging into a company's cloud server to deploy code, check logs, restart a service
- **System administrators** — managing/configuring remote servers (updating software, fixing issues) without physically being in the data center
- **Anyone using GitHub** — pushing code to GitHub over SSH instead of typing a password every time
- **Automated scripts/CI pipelines** — one server automatically logging into another server to deploy an app, with no human involved at all

## The complete flow — from typing the command to seeing a result

Let's say you type this on your own laptop:
```
ssh john@203.0.113.42
```

Here's EXACTLY what happens, start to finish:

```
STEP 1 — Your laptop's SSH client looks up "203.0.113.42" 
         (this is just an IP address — the remote computer's 
          "address" on the internet, same as any website's address)

STEP 2 — Your laptop opens a network connection to that IP, 
         specifically on "port 22" — SSH servers always listen 
         on this specific port by default, like how websites 
         always listen on port 443 for HTTPS

STEP 3 — The remote server's SSH software (sshd) responds: 
         "Hello, I'm an SSH server, here's my version info"

STEP 4 — Both sides perform a KEY EXCHANGE — this negotiates a 
         shared secret encryption key for THIS session, using 
         asymmetric encryption briefly (exact same TLS-style 
         handshake pattern from our HTTPS discussion earlier)

STEP 5 — From this point, EVERYTHING going back and forth is 
         encrypted (symmetric encryption, for speed) — nobody 
         snooping on the network can read anything anymore

STEP 6 — AUTHENTICATION happens next — proving you're allowed 
         to log in as "john" on this machine. Two common methods:
         
         a) PASSWORD — server asks for john's password, you type 
            it (travels safely because the tunnel is already 
            encrypted from Step 5), server checks it matches
         
         b) SSH KEY (the method from our earlier deep-dive) — 
            server sends a cryptographic challenge encrypted with 
            YOUR public key (already stored in john's 
            ~/.ssh/authorized_keys file on that server), you prove 
            you hold the matching private key by correctly 
            responding — no password ever typed at all

STEP 7 — Authentication succeeds → server creates a "shell" 
         session for you — literally starts a command-line 
         environment (bash, zsh, etc.) on the REMOTE machine, 
         tied specifically to your connection

STEP 8 — You now see a prompt like: 
         john@remote-server:~$ 
         This is NOT your laptop's terminal anymore — every 
         command you type from here runs on the REMOTE computer

STEP 9 — Example: you type "ls" (list files) 
         → this command travels (encrypted) to the remote server 
         → the remote server actually EXECUTES "ls" on ITSELF 
         → the remote server's OUTPUT (list of its files) travels 
           back (encrypted) to your screen
         → You see the REMOTE server's files, even though you 
           typed the command on your own laptop thousands of 
           miles away

STEP 10 — You type "exit" (or close the terminal) 
          → connection closes, remote shell session ends, 
            you're back to your own laptop's normal terminal
```

## The simplest possible mental model

Imagine a very long, secure telephone-style wire between your keyboard and someone else's computer's keyboard input. Whatever you type gets sent down that wire and typed "as if" on their machine; whatever their machine displays gets sent back down the wire and shown on your screen. That's SSH — nothing more mystical than that, just made completely private/encrypted and identity-verified.

## Common things people actually DO once connected via SSH

- Run any normal command-line commands (`ls`, `cd`, install software, restart a web server, check error logs)
- Copy files back and forth (a related tool called **SCP** or **SFTP** uses the same SSH connection specifically for file transfer)
- Run/manage entire applications (start/stop a website's backend process, view live logs, edit configuration files directly on the server)

## Quick recap, answering exactly what you asked

| Your question | Crisp answer |
|---|---|
| What IS SSH? | A protocol (and free software implementing it) that lets you remotely control another computer's command line, securely |
| Who has it? | Every Linux/Mac/modern Windows computer comes with SSH client software built in; servers run SSH server software (`sshd`) to accept connections |
| Who owns/sells it? | Nobody — it's free, open-source (OpenSSH is the standard implementation) |
| Who pays for what? | You pay (if anything) for the REMOTE SERVER/computer itself (e.g., renting a cloud VM) — never for SSH itself, which is free |
| What's the flow? | Connect to server's IP on port 22 → encrypt the connection (key exchange) → authenticate (password or SSH key) → get a remote command-line session → type commands, see remote output → exit |
