# N5-LA (box 58, option (A)): look-ahead removes the stale lag and RESTORES the exponential counter; more staleness shortens it. No variant is immune by construction
L-NEW successor 33 (Opus 5.5; D14, D18, Lead reading L40). Lead's message 2026-10-29 16:54Z, BOX 58: «Pick one: (A) A variant immune by
construction: e.g. Even's step evaluated against σ̄(F(σ)) by a bounded look-ahead, or a memory of reset patterns ... State it, check
termination, and run it on switchbestexp plus the hybrid families. (B) A structural impossibility ... (C) If neither has a handle, park with
a clean handover.» I took (A) for the two cheapest variants, then (C). Written from 17:00Z (date -u). Working note, unrefereed.
Tool: experiments/new/box58/la.py (one-sided runs from the S3 start; K = look-ahead depth, LAG = staleness depth). Runs inline, deterministic.

## 1. The variants and termination (PROVED, lane)
For an Even strategy s with Is ≠ ∅, let H_s be S4a′'s arena (Even v: {s(v)} ∪ Is(v)), and let opt(s, ρ) be S1's optimum of H_s against
the Odd strategy ρ (P-N5-SF §0's A(σ) is opt(σ, σ̄(σ))).
- LA_K (look-ahead): t_0 := opt(s, σ̄(s)); t_{k+1} := opt(s, σ̄(t_k)) for k < K, stopping early at a fixed point. Step: t_K, or S4c's switch
  if t_K = s.
- LAG_d (staleness): opt(s, σ̄(s_{−d})), where s_{−d} is the strategy d steps earlier on the run (s_0 before that). S4c's switch if the
  optimum is s.
Termination (both). Every step returns a strategy of H_s different from s, so a non-empty unambiguous switch of improvements of s; or it
returns S4c's switch, which is also such a switch. By RESULTS R15 (c) every such step goes strictly up in ≺ and no strategy repeats. At a
stop Is = ∅ (no step is defined only then). The output is S5's, correct as N5's under the same premise (R57 (b) / G-N5T-3). □

## 2. DATA (switchbestexp_N, S3 start; one-sided steps; distinct σ̄ values in brackets)
| N | F (= LAG_0, K = 0) | LA_1 | LA_3 | I^glo (box 57) | LAG_1 | LAG_2 |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 58 (4) | 58 (4) | 58 (4) | . | . | . |
| 3 | 135 (8) | 134 (8) | 134 (8) | 134 | 97 (8) | 97 (8) |
| 4 | 258 (16) | 286 (16) | 286 (16) | 286 | 155 (14) | 155 (14) |
| 5 | 364 (30) | 590 (32) | 590 (32) | 590 | 209 (23) | 196 (24) |
| 6 | 412 (35) | 1198 (64) | 1198 (64) | 1198 | 217 (24) | 204 (25) |
| 7 | 456 | . | . | 2414 | 225 (25) | 212 (26) |
- LA_1 = I^glo exactly on N = 3..6: one round of look-ahead removes the 2^(N−1) − N stale-reset lags of box 57. The counter is then complete
  (2^N distinct σ̄), and the count doubles (286, 590, 1198). DEAD: look-ahead as an immunity device. Instance: switchbestexp_6 (n 160),
  LA_1 makes 1198 steps against F's 412. LA_3 adds nothing over LA_1.
- LAG_1, LAG_2 (MORE stale than F) cut the counter earlier: σ̄ has 14 distinct values at N = 4 (F has 16), and the count is about +8 per N
  from N = 5 on (209, 217, 225).
- READING. On this family the protective feature of N5-SF is the staleness itself. Fixing the frame (look-ahead) is exactly I^glo. Adding
  staleness helps further. This matches box 57: the lags are where F leaves the counter.

## 3. Why I stop at (A) and do not take (B)
- Immunity by construction would need an argument that NO polynomial-size gated counter exists for the variant. For LAG_d the gate must
  hold over d stale steps instead of one, which is harder to build. But I have no counting argument that it is impossible. A gate that is
  stable for d steps (an access edge with one arena option during a d-step window) costs O(d) vertices in the obvious designs. So LAG_d
  probably falls to the same recipe with a longer gate (READING, untested).
- Memory of reset patterns (Fearnley's snare memory). Friedmann's DAM 2013 lower bound for snare memorization (T46 §1 (c); DOI
  10.1016/j.dam.2013.02.007; NOT OPENED by me) is the known obstruction for that family of rules. I did not build a variant.
- (B) structural impossibility: no handle. Friedmann's switch-best family is polynomial size with ordinary parity priorities (thesis
  Thm 4.50 via T46; not opened by me), and F, LA_1 and I^glo differ only by WHEN Even sees Odd's reset. A gated counter needs only that the
  stale and true frames rank the reset bit's options alike at reset steps. I see no counting obstruction to that.
So (C): park after this box with a clean handover (notes/L-NEW.md resume point).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box58/la.py; check.sh block "Box 58".
- FINDINGS: (1) PROVED (lane): LA_K and LAG_d terminate (R15 (c)). (2) DATA / DEAD: look-ahead LA_1 = I^glo on switchbestexp N = 3..6
  (doubling, 1198 at N = 6). (3) DATA: more staleness (LAG_1, LAG_2) shortens the run further (225 / 212 at N = 7). READING: staleness is
  the protective feature; immunity unproved. (4) (B) has no handle.
- NEEDS: none from the owner. Lead: LAG_d may interest L-RED as a next target after gated resets (a d-step gate); I park.

## 4. Addendum (17:1xZ by date -u; after the Lead's 17:01Z message with L-RED R115): the variants on fcN
fcN := switchbestexp_N with the N edges f_i → c removed (L-RED R115's family, rebuilt here from box54/out/switchbestexp_N.pg by
deleting c from each f_i's list; not compared byte-for-byte with L-RED's generator). Files experiments/new/box58/out/fcN.pg. One-sided steps
from S3, distinct σ̄ in brackets:
| N | F | LA_1 | LAG_1 | LAG_2 |
| --- | --- | --- | --- | --- |
| 3 | 121 (7) | 121 (7) | 89 (7) | 76 (7) |
| 4 | 215 (11) | 215 (11) | 158 (11) | 113 (11) |
| 5 | 346 (16) | 346 (16) | 258 (16) | 156 (16) |
| 6 | 520 (22) | 520 (22) | 382 (22) | 205 (22) |
| 7 | 743 (29) | 743 (29) | 549 (29) | 260 (29) |
- LA_1 = F on fcN: with the stale escape removed there is no stale-reset lag, so the frame does not matter (consistent with box 57).
- All four are QUADRATIC here (F ≈ 15N², second differences 28-34; LAG_2 second difference 6). Distinct σ̄ = 1 + N(N+1)/2 in every
  variant (7, 11, 16, 22, 29), L-RED's unary counter with full resets. Staleness lowers the constant, not the degree. So LAG_d is no
  defence against fcN-type families either (DATA). If L-RED's nesting gives N^k, every variant here is expected to follow it (READING).
- Not done: (B) for nested unary counters (does nesting depth cost arena size multiplicatively?). Parked; it goes to the next successor if
  the Lead routes it.
