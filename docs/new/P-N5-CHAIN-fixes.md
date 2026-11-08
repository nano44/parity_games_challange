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

## Fixes entry 3 (L-NEW successor 65; two referee-originated proof repairs + line; Lead 13:02Z: «same rule as QUIET's R-G (consistency under L41) … Write P-N5-CHAIN fixes entry 3 … + L-4 = L-3 (c484795c) + R-G3 … + R-B3»; 13:12Z: «ADD … a clause R-W … So CHAIN L-4 = L-3 + R-G3 + R-W + R-B3»; written 13:19Z by date -u)
### The (Q5) boundary step (credit: REFEREE 28 for P-N5-QUIET's form, R-P-N5-QUIET.md l. 118-120; REFEREE 30 and REFEREE-2 35 for finding it again and for the Γ3 form, claude/referee-2 09ce14fc R2-P-N5-CHAIN.md Addendum 3)
- §6 (Q5)'s Bellman-Ford step cites «(Q4)'s argument and simplicity» for F4′ at the face. (Q4)'s argument covers the face's own successor
  and the path; it does not cover the BOUNDARY value. The step that does, for each kind of boundary point of a B-class C = (w, S):
  - an e-face target y in class (w, S ∖ {e}): if β_g ∈ Π(y) for a β-face β_g ∈ C, then S = E(β_g) ⊆ E(y) = S ∖ {e}, impossible;
  - the core exit through pb: its Π is {K0, K3}, no β;
  - w itself: Π(w) = ∅.
- So β_g ∉ Π of any boundary value, and F4′ holds at the face. Read (Q5)'s «by (Q4)'s argument and simplicity» as including this step. No
  statement changes; the packet stays frozen. REFEREE-2 35 SIGNs it (Addendum 3); REFEREE 30 SIGNs it (R-P-N5-CHAIN.md §D follow-up 2, claude/referee 91334ccd,
  relayed by the Lead 13:12Z).
### The W-1 repair, restated (credit: REFEREE-2 35, R2-P-N5-CHAIN.md «W-1»; re-derived and SIGNED by REFEREE 30, claude/referee b5ac2304 R-P-N5-CHAIN.md §D follow-up 1)
- Recorded as a note in fixes entry 2; restated here because the line now names it (Lead ruling 13:12Z, L41). Three sentences of the frozen
  text are false over ALL vertices: (Core)'s «a play passes K0 iff it passes K3» (plays from pA or K3 pass K3, not K0); (F-cls3)'s «each
  class is a convex set of values»; E-MON3's reason «both plays have node w, so both or neither contain them».
- Repair: the only edge into the eight-vertex core {K0, pA, K3, K1, s, r, K2, q} from outside is pb_g → K0; the core vertices have constant
  values on every state (frozen core, σ̄(K2) = r by LOC-K2-3); for a non-core vertex v, K0 and K3 are both in Π_t(v) (node K1 or K2) or
  neither. So (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, and every use in the packet is of that kind.
### Line changes (applied in the order R-G3, R-W, R-B3)
| item | old | new |
| --- | --- | --- |
| R-G3 | «is a separate gauntlet step-4 item; DATA, clause by clause (unit:» | «is a separate gauntlet step-4 item; the step β_g ∉ Π(y) for the boundary points y in QUIET3's (Q5) F4′ (an e-face target y of class (w, S ∖ {e}): else S = E(β_g) ⊆ E(y); the pb exit: Π = {K0, K3}; w: Π = ∅) is referee-originated (REFEREE R-P-N5-QUIET §3 (Q4), l. 118-120, REFEREE 28, for P-N5-QUIET's form; REFEREE 30 and REFEREE-2 35, R2-P-N5-CHAIN Addendum 3, for the Γ3 form), signed by both referees; DATA, clause by clause (unit:» |
| R-W | «signed by both referees; DATA, clause by clause (unit:» (created by R-G3: once in L-3 + R-G3, absent from L-3) | «signed by both referees; (F-cls3)'s convexity and E-MON3's reason hold for non-core vertices, the eight core vertices being constant (referee-originated: REFEREE-2 R2-P-N5-CHAIN W-1, signed by both referees); DATA, clause by clause (unit:» |
| R-B3 | «frozen at l-new 93531b03, sha1 6e613ba7; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successor 64;» | «frozen at l-new 93531b03, sha1 6e613ba7, with its fixes entries 1-3, docs/new/P-N5-CHAIN-fixes.md; source box 196, docs/new/N5-CHAIN-box196.md; L-NEW successors 64-65;» |
- R-G3 placement: before «DATA, clause by clause», which occurs once in L-3 (the line's first DATA clause), as QUIET's R-G; R-W
  right after R-G3 (the Lead's clause, unchanged; it ends with «;» before « DATA»), R-B3 in the source note. R-G3's and R-B3's old strings occur once
  in L-3; R-W's old string is created by R-G3 and occurs once in L-3 + R-G3.
### Line L-4 (written by script)
- docs/new/P-N5-CHAIN-line-L4.txt = L-3 + R-G3 + R-W + R-B3 (in that order), by experiments/new/box196/mkl4_196.py (from the repo root): asserts the packet's
  sha1 (6e613ba7…), L-3's sha1 (c484795c…), each old string exactly once where applied (R-G3, R-B3 also once in L-3; R-W's absent from L-3), one line, no «|», «(» = «)». Result: sha1
  a69c8aa96fb0b67c6c0a3f6d11670a0b57ba9331, 9,082 B, 174 «(» = 174 «)». L-3 kept (superseded).
- chain.pins: this file re-pinned; L-4 and mkl4_196.py added.
