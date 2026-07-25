Good question to nail down with real testing rather than guessing — let me actually run these combinations to confirm exactly which ones work.That one broken line (intentionally testing invalid syntax) crashed the whole script before it could show the working examples. Let me isolate each test properly, one at a time.All confirmed by actually running the code — here's the full picture.

## Your exact case: `"'a'-'b'"` — **works perfectly, no problem at all**

```python
x1 = "'a'-'b'"
print(repr(x1))
# Output: "'a'-'b'"
```

**Yes — you can absolutely put single-quote pairs inside a double-quoted string.** The outer double quotes mark where the string begins/ends; anything inside (including single quotes) is just treated as plain text content, no escaping needed.

## The full rule, confirmed by testing every combination

| Combination | Works without escaping? | Example |
|---|---|---|
| Single quotes inside double quotes | ✅ Yes | `"'a'-'b'"` |
| Double quotes inside single quotes | ✅ Yes | `'"a"-"b"'` |
| Same quote type nested (single-in-single, unescaped) | ❌ No — breaks the string early | `'it's'` → error |
| Same quote type nested, WITH backslash escape | ✅ Yes | `'it\'s a test'` → `it's a test` |
| Double quote inside double, WITH escape | ✅ Yes | `"she said \"hi\""` → `she said "hi"` |
| Triple-quoted (`'''` or `"""`) — both quote types unescaped inside | ✅ Yes, both work freely inside | `'''has 'single' and "double"'''` |

## The one core rule tying it all together

**Python only cares about matching the EXACT quote character it started with, to know when the string ends. Whatever's inside — as long as it's a DIFFERENT quote character than the one framing the string — is just normal text, no special handling needed.** The only time you need a backslash (`\'` or `\"`) is when you want to use the SAME quote character inside that's already being used as the string's own boundary — otherwise Python would think the string ended right there.