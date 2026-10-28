# R2-N5-GCX: REFEREE-2 report on packet P-N5-GCX (MIG-SPLIT; UL-RED conditional on UL_G; ABS-HEIGHT, ABS-TIE, LOC and Remarks in the model ABS)
Referee: REFEREE-2 successor 18 (session_01WT4cukhJyjxHKaBJWikCkK), Opus 5.5 (D15, L37). Written 2026-10-28 from 21:15Z (date -u).
Object: docs/si/P-N5-GCX-box21.md, sha1 5a91bebbc34f14be147da38adc1a6202407c70c2 (on trunk; `sha1sum` of the working-tree file = the pin),
105 lines, frozen. Author L-SI successor 17. Its quotes are pinned at 7d87f9be.
Independence: written before opening any REFEREE file on GCX. In the push turn, after `git fetch origin claude/referee`, `git ls-tree
--name-only -r origin/claude/referee docs/referee/ | grep -ic gcx` gave 26 at 2026-10-28 21:29:40Z (2026-10-26 19:04:54Z: 26). I saw file NAMES only and
opened nothing. The Lead's brief said that L-RED's R91 (UL_C) and R93 (C-ONCE_X) killed conjectures in the packet. I read L-RED's R91 file
(docs/red/R91-ulc-reader.md §1-§3) to check that UL_G, the premise of UL-RED, is untouched. It is: R91 §3 says so, and my data agree (§2).
Lane tools (experiments/si/*gcx*.py, abscyc.py, rund/quotecheck.py) NOT run or imported.
Checkers (own):
- docs/referee-2/R2-N5-GCX/gcx_check.py: N5 side. State loop = my SPEC loop (dual_check.Runner on si.py); Ξ and W = my own play values
  (rund_check.state_info, ENGXI). Computed from the packet's definitions: D_t, A_t, R_u, DD_t, Δ_t, X-migrations, global C-intervals, K(S),
  U(S) at L = −1 (rund_check.forbidden), COARSE_{−1}(W).
- docs/referee-2/R2-N5-GCX/abs_check.py: the model ABS, written from §4, with brute-force pointwise-maximal arena strategies and pluggable
  tie rules.
- Quote check: my R2-N5-CHOSEN/qtags.py.
Scope (D1): MIG-SPLIT is elementary. UL-RED is an implication from the OPEN conjecture UL_G, and K(S) is not bounded. §4 is about an abstract
model whose link to N5 is a READING (§5). Nothing here bounds N5's running time. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict | premises (checked) |
| --- | --- | --- | --- |
| §2 | Lemma MIG-SPLIT, and its Consequence | SIGN (note N-GCX-1: u′ ∈ U_c is implicit) | SPEC definitions; τ constant on the phase |
| §3 | Corollary UL-RED (a), (b) | SIGN AS AN IMPLICATION from UL_G (a CONJECTURE, OPEN; untouched by R91) | RESULTS R67 (f) CHARGE-U (landed; L = −1 allowed, U_L ⊆ U_{−1}); C-intervals disjoint (N-GCX-2) |
| §4 | Lemma ABS-HEIGHT (acyclic, basic tie rule) | SIGN | model definitions |
| §4 | Lemma ABS-TIE (acyclic, any deterministic rule) | SIGN | model definitions |
| §4 | Lemma LOC (cyclic model) | SIGN FOR THE BASIC TIE RULE ONLY. The clause "or any deterministic rule" is FALSE: counterexample in §1.4 (gap G-GCX-1, with a repaired statement LOC′ that I sign) | model definitions |
| §4 | Remarks (MONO), (MONO-SUCC), (NO-RETURN) | SIGN | model definitions (policy-improvement telescoping) |
| §5 | READING / CONJECTURES / OPEN / DEAD / DATA | not reviewed (not to sign), except that UL_G is untouched by R91 (checked) | — |
| §1 | quotes | 5/5 [Q]-tagged quotes VERBATIM at 7d87f9be, in the line ranges given | own qtags.py |
ONE GAP: G-GCX-1, a scope error in LOC's statement. No other gap. Notes N-GCX-1..5 (§3).

## 1. Proof check
### 1.1 §2 MIG-SPLIT
- z ∉ A_t, so z's (σ_t, τ)-play meets D_t; u′ is its first D_t-vertex, and u′ ≠ u because z ∉ R_u(t). Suppose u′ ∈ D_{t+1} and no Even vertex
  of π switches.
  - The Odd vertices of π follow τ (constant on the phase) in the W-play, so z's (t+1)-play begins with π and then reaches u′.
  - Its first D_{t+1}-vertex is on π or is u′. It must be u (z ∈ R_u(t+1)). u is not on π: u ∈ DD_t ⊆ D_t, and π has no D_t-vertex.
  - So the first D_{t+1}-vertex is u′ ≠ u, a contradiction. CORRECT.
- In case (S), w is on z's t-play before u′ and its σ changes, so the play changes. CORRECT.
- Only u ∈ D_t is used; DD_t ∩ DD_{t+1} is not needed.
- Consequence. Each X_u transition carries a migration z, and z is case (L) or case (S).
  - (S): some z ∈ U_c changes its play. R_u ⊆ U_c by definition.
  - (L): the vertex u′ leaves D. It must lie in U_c to be counted, and the packet leaves that implicit (N-GCX-1). z's honest play and its
    W-play agree up to their first D_t-vertex, since Odd vertices outside D_t have σ̄ = τ. So u′ is on z's honest play, and λ(u′) = λ(z) = c.
  CORRECT.

### 1.2 §3 UL-RED (conditional)
- (a) A U event is one Even vertex's switch at one transition, so there are ≤ n_E per transition.
  - Cut transitions number K(S).
  - The global C-intervals are maximal runs of "good" transitions. Good means A_{t+1} ⊆ A_t for every class, D_{t+1} = D_t, and
    DD and Δ equal at t and t+1. The working note's definition says "(so DD_c is constant too)", so the condition is local to each
    transition and the intervals are disjoint (N-GCX-2). There are ≤ K(S) + 1 of them.
  - By UL_G, U events in an interval [a, b] have k′ ∈ [a, a + n − 2]: ≤ n − 1 transitions per interval.
  - Total ≤ n_E((n − 1)(K + 1) + K). CORRECT.
- (b) R67 (f) CHARGE-U (landed, hypothesis (ii) only, at L = −1; U(S) at L = −1 is the largest set, N-RUND-5) combined with (a). CORRECT.
  The packet's Scope line is right: only the arithmetic is new.
- R91's reader family does not touch UL_G. Its U event sits at index L < n − 1 = 2L + 15 of the global interval [0, L + 1]. My checker
  reproduces exactly R91's event on reader_L10_n36 (k′ = 10, edge (15, 14), global interval [0, 11]), and on L20 and L40 (§2).

### 1.3 §4 ABS-HEIGHT, ABS-TIE, Remarks
- ABS-HEIGHT. In the acyclic model the pointwise optimum picks, at each v, an N-maximiser over Al(v) of the successors' optimal values;
  those values do not depend on v's own choice, because no successor's play returns to v. Let v be settled from t.
  - y1 = s_t(v): the arena and the N-values are unchanged, and the basic rule keeps y1.
  - y1 ≠ s_t(v): M(y1) > M(s_t v). The new arena is {y1} ∪ {M > M(y1)} ⊆ Al_t(v), and y1 is still a maximiser.
  The argument repeats at every t′ ≥ t, so v and its values are constant from t + 1. Induction on height: a vertex of height h is constant
  from state h. CORRECT.
- ABS-TIE. After v is settled, each change moves to y ∈ Al ∖ {s(v)}. M(s(v)) rises strictly and the arena loses s(v): ≤ deg(v) − 1 changes.
  A step with no change repeats R's inputs (arena, values, current choice), so the changes are consecutive. v is constant from
  t + deg(v) − 1 ≤ t + deg(v). Induction gives D = max path Σ deg ≤ m. CORRECT (the packet's t + deg(v) is one looser than needed).
- (MONO). s is itself a valid arena strategy, so N_{s′} ≥ N_s. For M: every edge of s′ is s's edge or M_s-improving, so
  M_s(v_i) ≤ w(v_i) + M_s(s′ v_i) along v's s′-play; telescoping to the terminal gives M_s(v) ≤ M_{s′}(v) (validity of s′ needed).
- (MONO-SUCC): from (MONO) and the arena's strictness.
- (NO-RETURN): after leaving y at t1, M(s(v)) > M_{t1}(y) forever, by (MONO-SUCC).
- All three CORRECT.

### 1.4 §4 LOC: correct for the basic rule; FALSE for "any deterministic rule" (G-GCX-1)
- The proof says "the proof of ABS-HEIGHT applies to the viable successors verbatim". ABS-HEIGHT's proof keeps y1 by the BASIC rule
  ("kept by the rule"). For the basic rule this is right:
  - v's choice in a pointwise maximal valid strategy is an N-maximiser over the viable arena successors. A viable y can be substituted at v
    alone, keeping validity, and pointwise maximality then bounds N(v).
  - With the three quantities unchanged, both cases of ABS-HEIGHT go through.
  SIGN for the basic rule.
- For a general deterministic rule R(arena, values, current choice), the case y1 ≠ s_t(v) breaks. The arena shrinks to {y1} ∪ {M > M(y1)},
  R's inputs change (new arena, new current choice), and R may pick another maximiser.
- Counterexample (abs_check.py example; logs/loc_example.txt):
  - Setup: one non-terminal v (weight 0) with three terminal successors y0 (h 0, T 0), y1 (h 1, T 5), y3 (h 2, T 5); start s_0(v) = y0.
  - Rule "flip": take the smallest-index N-maximiser, but the LARGEST-index one when the current choice is a maximiser. This is
    deterministic, and a function of (arena, values, current choice).
  - Step 0 → 1: arena {y0, y1, y3}, maximisers {y1, y3}, the current y0 is not one, so v takes y1.
  - Step 1 → 2: arena {y1, y3}, the current y1 is a maximiser, so v takes y3.
  - So s_2(v) ≠ s_1(v), while every successor is a terminal with constant (M, N) and no viability exists to change. LOC's conclusion fails.
  - Under the basic rule the same model stays at y1.
- Random models (logs/abs_acyclic.txt, abs_cyclic.txt): LOC's conclusion fails 43 (flip) + 82 (random tie tables) times in 150,000 acyclic
  runs, and 11 + 30 times in 97,065 cyclic runs. Under the basic rule it never fails: 3,586 and 2,987 change events checked.
- Repaired statement LOC′ (any deterministic rule): if s_{t+2}(v) ≠ s_{t+1}(v), then one of the three changes occurs (as in LOC), OR
  s_{t+1}(v) ≠ s_t(v).
  - Proof: if none of the three occurs and s_{t+1}(v) = s_t(v), then the arena is unchanged (same current choice, same M-values), the
    values and the viable set are unchanged, so R's inputs repeat and so does its output.
  - SIGN for LOC′. Data: 0 failures of LOC′ in all the runs above, for every rule.
  - So for a general rule a vertex can change at most once more without a successor change; ABS-TIE's "consecutive changes" in the cyclic
    setting. For the basic rule, LOC as stated.
- Effect: LOC is used by nothing signed. Its role is the OPEN lift (§5 (i)-(ii)), where the actual tie rule of N5 matters. Any use of LOC
  for N5's S4a step must either check that N5's per-vertex rule is "basic" in the packet's sense, or use LOC′.

## 2. DATA (own checkers; every violation count 0; counts from docs/referee-2/R2-N5-GCX/logs/)
N5 side (gcx_check.py; logs/total.txt sums named.txt, named_big.txt, lib41_x5.txt, lib2o_x5.txt and rand_*.txt; 43 RESULT lines, all OK):
- Corpus:
  - named.txt, 36 instances at their .start files where present: L-RED's ul family (reader_L10/20/40, ladderd0_k12/24/48,
    ladderent_k12/24/48, cxmig_k4/8/16), cone_n69, so_th_n32, phase2_pk48, x32_waves48, twowave_L16, all experiments/si/rund
    instances, nep90_n40, nep76_n40;
  - named_big.txt: gate_K16_n197;
  - lib41 × 5 starts, lib2o × 5;
  - random k = 2 (3000 × 3), k = 4 (2000 × 3), kO (1500 × 3), k = 5, n 20-36 (400 × 2).
- Totals: 22,592 N5 runs, 89,514 states (ENGXI 0), 5,193 runs S (fallback-free, in-phase, λ_W constant) with 19,997 transitions.
| check | checks | violations | detail |
| --- | --- | --- | --- |
| MIG-SPLIT at every X-migration (u′ ≠ u, u′ ∈ U_c, (L) or (S), play change in (S)) | 298 | 0 | case (L) 83, (S) only 215; nep90 14 and nep76 12, all (L) (the lane's §5 data, reproduced); gate_K16_n197 105 (32 L / 73 S); pp_K12_n161 52, all S |
| Consequence X_u ≤ leaves + play changes | 69 (u, S) | 0 | max X_u 18 (gate_K16_n197) against 9 + 23 |
| global C-intervals disjoint, ≤ K + 1 | 5,193 runs | 0 | 5,687 intervals, 4,327 cuts |
| premise UL_G (DATA) | 1,187 U events inside intervals (of 2,469) | 0 failures | largest index 40 (reader_L40_n96, threshold n − 1 = 95); 21 on x32_waves48 (threshold 47); 13 on pp_K12_n161 (160) |
| UL-RED (a) | 5,193 | 0 | bound slack: max |U(S)| / bound = 0.0001 |
| CHARGE-U (landed) / UL-RED (b) | 128,361 vertex-runs | 0 / 0 | — |
Model side (abs_check.py, logs/abs_acyclic.txt, logs/abs_cyclic.txt):
- 150,000 acyclic runs (30,000 models, n 2-7, rules basic, flip, 3 random tables) and 97,065 cyclic runs. Of the cyclic draws, 4,285 had
  no pointwise maximum and 9,730 an invalid start; both are skipped, as the model assumes.
- ABS-HEIGHT, ABS-TIE, LOC (basic), LOC′ (all rules), MONO, MONO-SUCC and NO-RETURN (704 checks): 0 violations.
- LOC (non-basic): 166 failures in all (the G-GCX-1 counterexamples, counted).
- Fixation beyond the height: 0 under the basic rule, up to 1 under the others (ABS-HEIGHT is basic-only; ABS-TIE holds).

## 3. Notes
- N-GCX-1 (§2 Consequence). Say why the (L) vertex u′ is in D ∩ U_c: the honest play and the W-play of z agree up to the first D-vertex, so
  λ(u′) = λ(z) = c. One clause.
- N-GCX-2 (§1 definition). "every Δ_t(u), u ∈ DD_t, is constant" should say DD_t constant and Δ constant on it. The working note (N5-GCX §4)
  says "(so DD_c is constant too)". The disjointness of the C-intervals, and with it UL-RED (a)'s "≤ K(S) + 1 intervals", needs this
  transition-local reading.
- N-GCX-3 (ABS-TIE). The proof gives "constant from t + deg(v) − 1"; the packet's t + deg(v) is valid but loose.
- N-GCX-4 (thin). MIG-SPLIT is exercised at only 298 migrations, most of them on constructed families. UL_G's support where it could bite
  is a handful of long intervals: index/threshold at most 0.45 (x32_waves48 21/47, reader_L40 40/95).
- N-GCX-5 (independence). The brief named R91 and R93. I read R91's report to confirm that UL_G is untouched; R93 (C-ONCE_X) concerns no
  to-sign item and I did not open it.
