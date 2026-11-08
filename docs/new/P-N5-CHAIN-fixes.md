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

## Fixes entry 2 (L-NEW successor 65; line-only; REFEREE-2 35 second review, claude/referee-2 0e5c7c37, docs/referee-2/R2-P-N5-CHAIN.md; written 11:37Z by date -u)
- Verdicts: every statement SIGN (labels as the packet's); no GAP; L-2 NOT YET on R-1, R-2, R-4 (its R-3 is met by CL-1, entry 1). Lead
  ruling 11:38Z: «take its exact STRINGS (not tool fixes), so no pinned output changes»; «N-1 / N-2 optional: your call».
### W-1 (note; REFEREE-2 closed it itself; no statement, proof claim used, or line change)
- (Core)'s «a play passes K0 iff it passes K3» is false for plays starting at pA or K3; (F-cls3)'s «each class is a convex set of values»
  is false over ALL vertices (REFEREE-2's witness r2nonconv.out: x_1 ◁ e_(3,1) ◁ K1 at one S3 state, K3 ∈ Π deciding before E); E-MON3's
  stated reason («both plays have node w, so both or neither contain them») is not a valid inference.
- REFEREE-2's repair, which I accept as the reading of the frozen text: every vertex outside {K0, pA, K3, K1, s, r, K2, q} reaches the
  core only through some pb → K0, so its plays with node K1 or K2 contain both K0 and K3 and its other plays neither; the eight core
  vertices have constant values on every state (frozen core, σ̄(K2) = r by LOC-K2-3). So on one vertex's trajectory, and between two
  non-core vertices, the order is reward, then E, then the rest; every use in the packet is of that kind ((Q1) pe_g vs pβ_g, (Q2) a mover
  vs its pads, the per-vertex interval property for Q ≤ Σ(D − 1), E-MON3 one vertex at t and t + 1). Read (F-cls3)'s convexity sentence
  and E-MON3's reason as restricted to non-core vertices, core vertices being constant.
- The same reading applies to box 197 (docs/new/N5-CORE-box197.md), whose ASC-WIT (c) cites «as in E-MON3's proof»: there both compared
  vertices (pe_g1, pβ_g1) are non-core pads, so the repaired reason covers it.
### R-1, R-2, R-4 (REQUIRED, taken; REFEREE-2's exact strings) and N-1 (optional, taken)
| item | old (once in L-2) | new |
| --- | --- | --- |
| R-1 | «QUIET3: wfail 0 (unit: quiet windows)» | «QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their window)» |
| R-2 | «T-QUIET3: Tfail 0 (unit: runs)» | «T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of loud steps; the Σ_v form is not counted)» |
| R-4 | «LOC-K2-3: k2fail 0 (unit: states)» | «LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct Ω_t(r) ◁ Ω_t(K2) is not counted)» |
| N-1 | «spec on 100 runs and 5 pinned genomes, check196.out)» | «spec on 100 runs, and 5 pinned genomes in xi mode, check196.out)» |
- N-2 (a counter of T3's definition) NOT taken: it is a tool change, and the Lead ruled strings only; REFEREE-2's own t3def is 0.
- No number changes; no pinned output changes.
### Line L-3 (written by script)
- docs/new/P-N5-CHAIN-line-L3.txt = L-2 + R-1 + R-2 + R-4 + N-1, by experiments/new/box196/mkl3_196.py (from the repo root): asserts the
  packet's sha1 (6e613ba7…), L-2's sha1 (e481d260…), each old string exactly once in L-2, one line, no «|», «(» = «)». Each old and new
  string was checked verbatim against the report (whitespace-joined). Result: sha1 c484795c888ab46cee07038094368ba28da0055d, 8,450 B,
  164 «(» = 164 «)». L-2 kept (superseded).
- chain.pins: this file re-pinned; L-3 and mkl3_196.py added. check.sh block «P-N5-CHAIN» unchanged.
