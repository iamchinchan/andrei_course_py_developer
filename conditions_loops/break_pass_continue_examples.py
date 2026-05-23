"""
Comprehensive examples and explanations for `break`, `continue`, and `pass`.

Run this file to see printed output demonstrating behaviors and edge-cases.

Sections:
 - `break` in `for` and `while` loops, with `else` clauses and nested loops
 - `continue` usage in `for` and `while` loops
 - `pass` as a no-op placeholder in various contexts

Each example is self-contained and prints a header so you can run the file
and follow the output sequence.
"""


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def break_simple_for():
    section("break - simple for loop")
    # We iterate numbers 0..4 and break when we hit 3
    for i in range(5):
        print("loop iteration:", i)
        if i == 3:
            print("breaking at", i)
            break
    print("loop finished")


def break_with_for_else():
    section("break - for/else behavior")
    # The `else` on a loop executes only if the loop completed normally
    # (i.e., no `break` happened).

    print("\nExample A: break occurs (else NOT executed)")
    for i in range(3):
        print("i =", i)
        if i == 1:
            print("break at", i)
            break
    else:
        print("else executed - no break (should NOT print here)")

    print("\nExample B: no break (else executed)")
    for i in range(3):
        print("i =", i)
    else:
        print("else executed - loop finished normally")


def break_nested_loops():
    section("break - nested loops (inner vs outer)")
    # Breaking inner loop only stops inner; outer keeps iterating.

    for outer in range(3):
        print("\nouter loop:", outer)
        for inner in range(5):
            print("  inner loop:", inner)
            if inner == 2:
                print("  break inner at", inner)
                break
        print("outer continues after inner break")

    # To stop both loops when a condition is met, common patterns include:
    # 1) using a flag variable
    section("break - stop both loops using a flag")
    found = False
    for a in range(3):
        for b in range(5):
            if a == 1 and b == 3:
                print("found at", a, b)
                found = True
                break
        if found:
            break
    print("exited both loops after finding")

    # 2) encapsulating loops in a function and `return`ing early
    section("break - stop both loops using return from function")

    def find_pair(limit_a, limit_b, target):
        for a in range(limit_a):
            for b in range(limit_b):
                if (a, b) == target:
                    return a, b
        return None

    print("find_pair:", find_pair(3, 5, (1, 3)))


def break_in_while():
    section("break - while loop example")
    n = 0
    while n < 10:
        print("n =", n)
        if n == 4:
            print("breaking at", n)
            break
        n += 1
    else:
        # This else won't run because we `break` when n == 4
        print("while else: completed without break")


def continue_examples():
    section("continue - basic examples")
    print("\nSkip odd numbers using continue in for loop:")
    for i in range(6):
        if i % 2 == 1:
            # Skip this iteration, do not execute remaining statements in loop body
            continue
        print("even number:", i)

    print("\nUse continue in a while loop:")
    i = 0
    while i < 6:
        i += 1
        if i % 3 == 0:
            print("skipping multiple of 3:", i)
            continue
        print("number (not multiple of 3):", i)

    print("\ncontinue inside nested loops affects only the current loop:")
    for a in range(3):
        for b in range(4):
            if b == 2:
                print(f"skipping b={b} in inner loop (a={a})")
                continue
            print("a=", a, "b=", b)


def pass_examples():
    section("pass - no-op placeholder examples")
    print("\n`pass` does nothing and is useful as a placeholder:")

    # 1) In an empty function body
    def placeholder_func():
        # TODO: implement later
        pass

    print("calling placeholder_func (does nothing) ->", placeholder_func())

    # 2) In an empty class body
    class PlaceholderClass:
        pass

    print("created PlaceholderClass, instance ->", PlaceholderClass())

    # 3) In conditionals where syntax requires a statement
    if False:
        pass  # nothing to do when condition is False
    else:
        print("if False branch skipped; else executed")

    # 4) pass inside a loop does NOT skip the iteration — it's a no-op
    print("\npass inside loop is a no-op (iteration still runs):")
    for i in range(3):
        if i == 1:
            pass  # placeholder, does not affect flow
        print("iteration", i)


def combined_examples():
    section("combined - show differences and gotchas")
    print("Example: pass vs continue in loop")
    for i in range(3):
        if i == 1:
            pass  # does nothing, iteration continues to next lines
        print("after pass, i =", i)

    for i in range(3):
        if i == 1:
            continue  # skip the rest of this iteration
        print("after continue, i =", i)

    print("\nExample: break vs continue effects on loop else:")
    for i in range(3):
        if i == 5:
            break
    else:
        print("loop else executed because no break occurred")


def main():
    break_simple_for()
    break_with_for_else()
    break_nested_loops()
    break_in_while()
    continue_examples()
    pass_examples()
    combined_examples()


if __name__ == "__main__":
    main()
