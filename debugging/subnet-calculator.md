# Debugging: Subnet Calculator

Bugs I hit while building [subnet-calculator](https://github.com/raffytaffy627/network-tools/tree/main/subnet-calculator).

## Bug: "prefix" is not defined

**Date:** 2026-09-18

**What I saw:** Error Lens flagged `"prefix" is not defined` on both the `if prefix == 32:` and `elif prefix == 31:` lines.

**What I tried:** Checked that `prefix = network.prefixlen` was actually in the file (it was), then compared its indentation to the line below it.

**Cause:** The `prefix` line was indented 8 spaces instead of 4, which put it inside the `except ValueError:` block, after `continue`. `continue` jumps straight back to the top of the loop, so that line could never run and `prefix` was never created.

**Fix:** Moved the line back to 4 spaces (Shift+Tab) so it runs after the try/except.

**Lesson:** In Python, indentation decides which block a line belongs to. Anything after `continue` or `break` in the same block never runs.

## Bug: Spell checker broke my code

**Date:** 2026-09-18

**What I saw:** Code Spell Checker flagged `prefixlen` as an unknown word. I accepted its suggestion, and the line became `network.prefixed`, which doesn't exist.

**What I tried:** Hovered over the word. Python's tooling showed `(property) prefixlen: int`, which confirmed `prefixlen` was correct and the spell checker was wrong.

**Cause:** Spell checkers only know English words, not code. Accepting a suggestion replaces the text, and the script would have crashed with an `AttributeError`.

**Fix:** Changed it back to `prefixlen` and added it to `cSpell.userWords` in my VS Code settings so it stops getting flagged.

**Lesson:** Only accept spell check suggestions in comments, strings, and READMEs, never on code. Hovering over a name is a quick way to check if it's real.

## Bug: Wrong broadcast address for /31 and /32

**Date:** 2026-09-18

**What I saw:** `10.0.0.1/31` printed `Broadcast address: 10.0.0.1`, even though the host range line showed `10.0.0.1` as a usable host.

**What I tried:** Tested `/31`, `/32`, and `/24` side by side to see which cases were wrong.

**Cause:** The broadcast print line always used `network.broadcast_address`. But /31 (point-to-point links, RFC 3021) and /32 (a single host) don't have a broadcast address.

**Fix:** Created a `broadcast` variable in each branch of the if/elif/else: `"N/A (point-to-point)"` for /31, `"N/A (single host)"` for /32, and the real broadcast address for everything else. Then printed that variable.

**Lesson:** Edge cases break "normal" rules. Always test the extremes, not just the typical input.