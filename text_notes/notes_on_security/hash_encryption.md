Good, this deserves a proper untangling — hashing does a genuinely different job than encryption OR signing, and it's worth seeing exactly why hashing alone is enough in some cases.

## The core property of hashing that makes ALL of this work

**A hash function takes any input and produces a fixed, unique-ish "fingerprint." The SAME input always produces the EXACT same hash. Change even one character, and the hash comes out completely different.** That's it — that one property is what enables everything below.

```
hash("Hello World")  → a591a6d40bf420...
hash("Hello World!") → f3b1c6a4c4f9d8...   ← totally different, 
                                              just from adding "!"
```

## Case 1: Checking File Integrity (simplest case — NO keys involved at all)

**Real example: downloading Ubuntu Linux from the internet**

```
STEP 1 — Ubuntu's website publishes the file, AND separately 
         publishes its official hash:
         ubuntu-24.04.iso  →  SHA256: 3f88202a1...

STEP 2 — You download the file from some server/mirror

STEP 3 — YOU, on your own computer, run:
         sha256sum ubuntu-24.04.iso
         → your computer computes: 3f88202a1...

STEP 4 — YOU compare your computed hash to the one Ubuntu published
         → MATCH → the file is 100% identical to the original, 
           byte for byte — no corruption during download, no 
           tampering by a malicious mirror server
         → MISMATCH → the file is different/corrupted/tampered 
           somehow — don't trust it
```

**Why hashing alone is enough here, no keys needed:** you're not verifying WHO sent it — you're only verifying the file matches a hash YOU already trust from a separate, known-good source (Ubuntu's official website). There's no signature, no key, no encryption anywhere in this — just: compute the hash yourself, compare to a trusted reference value.

## Case 2: Storing Passwords (hashing alone, still no keys)

```
STEP 1 — You sign up with password "MyPass123"
STEP 2 — Server computes: hash("MyPass123") → "ef92b778..."
STEP 3 — Server stores ONLY "ef92b778..." in the database — 
         never the real password
STEP 4 — Next login: you type "MyPass123" again
STEP 5 — Server computes hash("MyPass123") AGAIN → "ef92b778..."
STEP 6 — Compares to stored hash → MATCH → correct password
```

**Again — no keys, no encryption.** It's pure "does recomputing the hash give the same fingerprint as before." Nobody needs to reverse it; they just need to check it matches.

## Case 3: JWT Signatures — THIS is where hashing + a key combine (this answers your real confusion)

This is the one you're mixing up, so let's isolate it precisely. **A digital signature is hashing PLUS encryption of that hash, combined — not hashing alone, and not encryption alone.**

```
CREATING the signature (server, using its PRIVATE key):
STEP 1 — Take the JWT's header + payload (plain, readable data)
STEP 2 — Hash it: hash(header + payload) → "a3f8e91b..."
STEP 3 — ENCRYPT this hash using the PRIVATE key:
         signature = Encrypt("a3f8e91b...", PRIVATE_KEY)
STEP 4 — Attach this signature to the JWT

VERIFYING the signature (anyone, using the PUBLIC key):
STEP 1 — Take the received header + payload
STEP 2 — Hash it yourself, independently: 
         my_hash = hash(header + payload) → should be "a3f8e91b..." 
         if nothing was tampered with
STEP 3 — DECRYPT the attached signature using the PUBLIC key:
         decrypted_hash = Decrypt(signature, PUBLIC_KEY)
STEP 4 — Compare: does my_hash == decrypted_hash?
         → MATCH → data is authentic AND untampered
         → MISMATCH → either tampered with, OR not genuinely 
           signed by the real private key holder
```

**Why you need the KEY here, but not in Cases 1/2:** in file integrity and passwords, you're only checking "does this match a value I ALREADY trust." But with a JWT, there's no pre-shared trusted hash to compare against — a NEW token gets created constantly, for different users, at different times. You need a way to prove "I (the server) am the one who created this specific hash, right now" — and THAT proof requires a key (encrypting the hash), because otherwise anyone could just compute their own hash and claim it's legitimate.

## Case 4: Blockchain — hashing chained together (still fundamentally hashing, used cleverly)

```
Block 1: data = "Alice sends Bob $10"
         hash1 = hash(data of Block 1)

Block 2: data = "Bob sends Carol $5" + hash1 (included INSIDE Block 2)
         hash2 = hash(data of Block 2, which includes hash1)

Block 3: data = "..." + hash2
         hash3 = hash(data of Block 3, which includes hash2)
```

**Why this matters:** if anyone tries to secretly change Block 1's data afterward, `hash1` changes completely (remember — one tiny change = totally different hash) — which means Block 2's data (which included the OLD hash1) no longer matches, breaking `hash2` too, cascading through every single block after it. **Tampering with anything in the past becomes instantly, mathematically obvious** — this is pure hashing, chained together, no encryption involved in this specific mechanism at all (signatures ARE separately used in blockchain to prove who authorized a transaction, but that's a distinct, additional layer on top of the hash-chaining).

## The direct answer to your actual question

**Hashing alone (no keys) works when you're comparing against an ALREADY-TRUSTED reference value** (a published file hash, a previously-stored password hash) — you're just asking "does this match what I already know is correct?" **Signing (hashing + encryption combined, needs keys) is required when there's no pre-existing trusted value to compare against, and you instead need to PROVE that a specific, trusted party is the one who created this data right now** — which is exactly the JWT/certificate use case, and is a fundamentally different, harder problem than simple integrity-checking against a known reference.

## One-line summary table

| Case | Uses keys? | What it actually checks |
|---|---|---|
| File integrity (Ubuntu ISO) | No | "Does this match a hash I already trust from elsewhere?" |
| Password storage | No | "Does re-hashing what you typed match what I stored before?" |
| JWT / Digital Signature | **Yes** | "Was this specific data created, right now, by someone holding a specific private key?" — hashing PLUS encryption of that hash, together |
| Blockchain chaining | No (for the chaining itself) | "Does changing any past block break the mathematical chain of hashes that follow it?" |