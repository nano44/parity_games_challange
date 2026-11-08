# P-N5-CHAIN fixes (append-only; the packet docs/new/P-N5-CHAIN.md stays frozen at l-new 93531b03, sha1 6e613ba7)

## Line L-1 (L-NEW successor 64; Lead 08:27Z: «write its line L-1 by script in the house form»; written 08:39Z by date -u)
- docs/new/P-N5-CHAIN-line-L1.txt, one paragraph, no «|»; generator experiments/new/box196/mkl1_196.py (run from the repo root with
  `git show a1decf9a0:docs/RESULTS.md` as its argument). It asserts the packet's sha1 (6e613ba7…), the RESULTS quotes verbatim, every
  statement name of the «To sign» table, and balanced parentheses. sha1 bd152dd9c71ea47dbc7fa6655a9a18a87908781a, 8124 B. Pinned in
  box196/chain.pins.
- Labels in the line: PROVED (every genome) for ESC3-ALL, W3-ALL, REACH3-ALL, the HOW3 facts, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3,
  NO-TIE3, QUIET3, T-QUIET3, E-MON3, CHAIN-DECOMP3; HUB-ASC-G3 CONDITIONAL on P-N5-ASC §4; UP-JUMP3, UP-B3 under HYPOTHESIS [E-LEV];
  CHAIN3 PROVED under HYPOTHESIS [E-LEV] and CONDITIONAL on the unlanded P-N5-END and P-N5-ASC §4 (REFEREE 29 draft CH-4); DEAD
  RUN-TRANSFER with its instance. DATA clauses with counters (unit, set, scope); a TARGET.md §2 / §4 scope clause.

## Fixes entry 1 (L-NEW successor 65; REFEREE 29 first review, claude/referee 36d2932d, docs/referee/R-P-N5-CHAIN.md; written 10:18Z by date -u)
- Verdicts: every statement SIGN with its label (ESC3-ALL … UP-B3, CHAIN3 with its label, DEAD RUN-TRANSFER CONFIRMED); no GAP in any
  proof. Line L-1 NOT YET on CL-1 only. Lead ruling 10:18Z: «P-N5-CHAIN L-2 = L-1 + CL-1 exactly (e481d260, 8,248 B), CO-1 NOT taken,
  CN-1 in fixes entry 1: approved.» Form A taken (REFEREE 29's exact strings).
### CL-1 (taken, Form A): the DATA clause «controls fire (every fail counter has one)» is false as worded: ties (NO-TIE3's counter) is 0 in
  every control and spec row and is not among ctrl196.py's five injected counters. The line now reads «controls fire (every fail counter
  except ties, NO-TIE3's counter, which has none)», and names the control set (each control on 50 runs, family rand, seed 1963,
  check196.out) and the spec set (seed 1963, data/sweep196.out). No number changes.
### CN-1 (noted; the packet stays frozen): the packet's §9 makes the same claim, «(each fail counter of §5-§7 has a firing control: …)», and
  it is false for ties in the same way. Read §9 as «each fail counter of §5-§7 except ties (NO-TIE3's counter, which has no firing
  control)». NO-TIE3 itself is PROVED (Corollary, §5) and signed; only the DATA sentence about its control is corrected. No statement
  and no proof changes.
### CO-1 (optional, NOT taken, Lead ruling): «each PROVED (every genome)» before a list that includes conditional items stays; each later
  item names its own condition (REFEREE 29: «not false»), and the line stays byte-equal to the referee's prediction.
### Line L-2 (written by script)
- docs/new/P-N5-CHAIN-line-L2.txt = L-1 + CL-1, by experiments/new/box196/mkl2_196.py (run from the repo root, no argument): asserts the
  packet's sha1 (6e613ba7…), L-1's sha1 (bd152dd9…), the old string exactly once in L-1, one line, no «|», «(» = «)». Result: sha1
  e481d260884807424c545bd3f3cdd7fbfb25f05c, 8,248 B, 160 «(» = 160 «)» = REFEREE 29's prediction (§5, chain_logs/linefix.out).
- chain.pins: this file re-pinned; L-2 and mkl2_196.py added. check.sh block «P-N5-CHAIN» unchanged. L-1 kept (superseded).
