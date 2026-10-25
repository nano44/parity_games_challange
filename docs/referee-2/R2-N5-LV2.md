# R2-N5-LV2: second-referee check of packet P-N5-LV2 (L-SI box 12: STALE-GATE, EV-G, ENT-X_{−1}, LV-PL′, SAND, FLAT-ALL_{−1}^{none}, LV-NONE, SCOPE-FB). REFEREE-2 (successor 10), written 2026-10-25 16:4xZ-17:2xZ (date -u)
Signature: (Opus 5.5, D15). Lead GO 16:32Z (Lead's stamp).
Object: docs/si/P-N5-LV2-box12.md, sha1 3b23a41fee6b705e20092d8dd49e7ce0b1408b03. The same at the pin 283bcb6, on trunk 7d505e6 and on my
tree (l-si ed936af1 added it). Source texts named in it: docs/si/N5-LV4-box12.md (sha1 9d1b90f4), N5-LV5-box12.md (sha1 e2cb0703); not
signed, the packet governs.
Background read:
- RESULTS R15 (a), (d); R25 (e) OFF (P-N5-FB §5: "At every in-phase transition (tame or not), if v ∉ R̄_{k+1} then COARSE_{M_k}(Ξ_{k+1} v)
  = COARSE_{M_k}(Ξ_k v)"); R28 (a) U-loc; R29 (a)-(e); R30 (a) OR; R31 with P-N5-FBW §3-§4; R37 (c) FREE-FREEZE, (d) EQ-END, (e) MERGE′;
  R38 (CN-LAST); R40 (P-N5-ENT §0-§5, read for the L = −1 re-reading).
- P-N5-LV (signed by both referees, mine: R2-N5-LV), P-N5-RL §4-§6 (EQ-END, MERGE, EV, EV+).
Independence: nothing in docs/referee/ read for this packet (`git ls-tree -r --name-only HEAD docs/referee | grep -i lv2` is empty at my
start; the Lead names REFEREE's R-N5-LV2 at referee b454ca3, not opened). No lane script (stale.py, scopefb.py, lvm1.py, betasearch.py) run
or imported. Input lists include game files only.
Tools: docs/referee-2/R2-N5-LV2/ (own code on R2-N5-LV/lv_check.py, R2-N5-ENT/ent_check.py, R2-N5-OUT/out_check.py): lv2_check.py,
lv2_climb.py, files.lst, files_new.lst, run_all.sh, run_new.sh, run_climbs.sh, totals.py, logs/, logs_new/, climb/, totals_*.txt.
Traces own / rand / spec. Every game asserts exactly one Odd vertex with out-degree > 1.
Labels as in the packet (PROVED (L-SI succ. 7); PROVED CONDITIONAL). Not a running-time bound, a TARGET.md claim or a step-4 pass.
G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Lemma STALE-GATE | SIGN | — |
| §2 Corollary EV-G | SIGN | N-LV2-1 (status): FREE-FREEZE is R37 (c) CONDITIONAL on (P); (P) is R36. So "none" holds given R36, which is landed |
| §3 Theorem ENT-X_{−1} | SIGN (its conditions P-N5-LV §3, §4 are signed by both referees) | N-LV2-2 (wording, inherited from R37 (f) EV): "Ξ_k(z) = ρ ⊕ Ξ_k(q)" is only a P-set identity when q lies on c's cycle |
| §4 Corollary LV-PL′ | SIGN (conditions as stated, signed by both) | — (the STRETCH_{−1} check at e = f_{N−1} + 1 is in §4 below) |
| §5 Lemma SAND | SIGN | — |
| §6 Lemma FLAT-ALL_{−1}^{none} | SIGN | — |
| §7 Theorem LV-NONE | SIGN (conditions P-N5-LV §1, §3, signed by both) | — |
| §8 Corollary SCOPE-FB | SIGN CONDITIONAL as stated ((C-ENT) = R40 landed; (C-LV) signed by both; (C-PKT) = this report and REFEREE's) | — |
| §9 data, §10 | not signed (as briefed) | N-LV2-3 (DATA): in all data every scope run has at most ONE THR fallback with r = −1 (237,033 such fallbacks) and at most one level −1 block fallback (645). So LV-NONE (1)-(2) and LV-PL′ (i)-(iii) are still vacuous, and the bounds hold at N ≤ 1 |
No statement is NOT SIGNED, and no gap is open. 0 violations in 66,655 batch runs + 1,422 runs on newer files and in 1,723,744 climb runs.
Lead's two asks:
- STRETCH_{−1} at e = f_{N−1} + 1 (and e = g_{N−1} + 1): its hypothesis is proved, by FLAT-ALL_{−1} (iii) at f_{N−1} (resp. FLAT-ALL^{none}
  (iii) at g_{N−1}). Every counted event has k + 1 ≤ e. So N-LV-2 is not inherited, and neither is N-LV-1 (§4).
- The per-scope-run count of r = −1 THR fallbacks on u* = none climbs: max 1 per scope run, against LV-NONE's n·n_E + 1 (worst ratio 22‰).
  All fallbacks of a scope run: max 5 against SCOPE-FB's 4·n·n_E + 3 (worst ratio 21‰ in climbs, 52‰ in random games). This is the first
  data with the none part reached at scale (237,033 fallbacks; FLAT-ALL^{none} held at all of them). LV-NONE's own induction (N ≥ 2)
  never fires (N-LV2-3).

## 1. STALE-GATE: SIGN
- Gate (y, z) at k: b_k(y) ◁ Ξ_k(z). Suppose Ξ_k(z) = Ξ_{k0}(z).
- b(y) is ⊴-non-decreasing along the whole run: b_{t+1}(y) = Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y), by R15 (a) and R15 (d)
  (σ_{t+1}(y) is σ_t(y) or a gate target). Nothing else is used, so "every game" is right.
- Case 1 (Ξ_{k0} z ⊴ b_{k0} y): Ξ_k z = Ξ_{k0} z ⊴ b_{k0} y ⊴ b_k y, against the gate. ✓
- Case 2 (Ξ_{k0} z ▷ b_{k0} y): (y, z) is a gate at k0, and S4c switches y to a ⊴-best gate target z′ (SPEC S4c, as quoted in P-N5-PFZ §0:
  every Even v with an improving edge). Then b_k y ⊵ b_{k0+1} y = Ξ_{k0+1} z′ ⊵ Ξ_{k0} z′ ⊵ Ξ_{k0} z = Ξ_k z, against the gate (k ≥ k0 + 1). ✓

## 2. EV-G: SIGN (N-LV2-1)
- z ∈ F_k: its σ_k-play is its (σ_k, τ)-play and stays in F_k. If the play were contained in F_{k0}, FREE-FREEZE (R37 (c): k0 in-phase THR
  S4c fallback with (h), k in the same phase, z ∈ F_k, play in F_{k0}) gives Ξ_k(z) = Ξ_{k0}(z), against STALE-GATE. ✓
- N-LV2-1: R37 (c) is CONDITIONAL on (P). (P) is landed as R36, so the "none" in the packet's condition column is right on trunk; the
  §0 list should name R36.

## 3. ENT-X_{−1}: SIGN (N-LV2-2)
Re-read P-N5-ENT §0-§3 at L = −1, step by step (H = V_{>max(−1, rank c)} = V_{>c}).
- (a) PL_{−1} (b): the first change j of the dirty interval is S4a with lev(θ_j, θ_{j+1}) = O_j > −1. So COARSE_{−1}(θ) = (c, P(θ)) changes:
  this is P-N5-ENT's "rise" at L = −1. A = P(θ_{k0}), B = P(θ_k) (P ⊆ V_{>c}). θ monotone + (C1), (C3): no return, so B ≠ A. ✓
- (b) (Σ1)-(Σ6) at L = −1.
  - (Σ2): (h) on [k0, k]; (A_{k0+1}) at L = −1 is OFFGATE (gates at k0 + 1 into F have level ≤ M_{k0} = −1); NL (iii) carries it,
    needing r_s > −1, which holds because r ≥ 0 on the whole block (Fact R, as in P-N5-LV §4).
  - (Σ3) NL (ii); (Σ4) CLS2; (Σ5) H1; (Σ6) (a). ✓
- (c) EV at L = −1, without ENT-SHAPE (4).
  - The window gate (y, z) at k has level M_k = −1 (every gate level is ≥ −1). EV-G: z's play is not in F_{k0}; it is in F_k ⊆ F_{k0+1}, so
    it meets Ev. ✓
  - q ∈ F on [k0+1, k] (no leave), so COARSE_{−1}(Ξ_k q) = COARSE_{−1}(Ξ_{k0} q): FLAT-ALL_{−1} (iii) across k0 (r_{k0} ≥ 0) and NL (i) at
    L = −1 after it. Then P(Ξ_{k0} q) = (π_q ∩ H) ⊔ A (Lemma G). ✓
  - MERGE′ (R37 (e)) is stated for −1 ≤ ℓ < ∞, so ℓ = −1 is covered: P(Ξ_k z) = P(θ_k) = B and o ∉ H. ✓
  - B = (ρ ∩ H) ⊔ (π_q ∩ H) ⊔ A, so A ⊊ B. ✓
  - N-LV2-2 (wording; the same sentence is in the signed EV, R37 (f)): "Ξ_k(z) = ρ ⊕ Ξ_k(q) … (the play is simple before its cycle)" is
    literal (P2) only when q precedes c on z's play. If q lies on c's cycle, ρ contains c, Ξ_k(q) has P = ∅, and the identity
    P(Ξ_k z) ∩ H = (ρ ∩ H) ⊔ P(Ξ_k q) still holds (cycle vertices other than c have rank < rank c). Only the P-sets are used, so nothing
    changes. (Also, that case contradicts CYC-EV at L = −1, which (e) proves.)
- (d) EV+ at L = −1: h := top of B ∖ A.
  - h ∈ ρ: MERGE′ (c) puts every H-vertex of z's play on the suffix shared with x_k's play, and q comes after h. ✓
  - h ∈ π_q: h ∈ P(θ_k), h ≠ o, so h is on x_k's play (in F_k by H1), and h ∈ R_{k0}. So h ∈ Ev. ✓
- (e) TEV-FB at L = −1. I re-read every step of P-N5-ENT §1-§3 for a use of L ≥ 0.
  - FZ: FLAT-ALL (iii) is its only one (M_{k0} ≥ 0). FLAT-ALL_{−1} (iii) replaces it, valid because r_{k0} ≥ 0. NL (i) at L = −1. ✓
  - BF: (C4) with V_{>−1} = V. ✓
  - RB: "a gate at k of level > L ≥ M_k" with L = −1 and M_k ≤ −1. ✓
  - WALK: no level used. CYC-EV: COARSE_{−1}(Ξ_k v) = (c, ∅) for v on C_k ∖ {c}. ✓
  - TEV-FB Steps 1-4: Step 2's "o ∉ H" comes from o ∉ A, as in P-N5-ENT. ✓
  - The re-reading is right. (d) and (e) contradict each other. ✓

## 4. LV-PL′: SIGN, and the STRETCH_{−1} check at e = f_{N−1} + 1 (Lead's ask)
- The Lead asked whether N-LV-1 / N-LV-2 are inherited (packet §0, l. 60-65). They are NOT.
- N-LV-2 was: STRETCH_{−1} is stated for s ≤ k < e, and P-N5-LV's PL_{−1} (a) needed k = e for a run ending at f_N. Here
  (iii) takes s := f_1, e := f_{N−1} + 1. STRETCH_{−1} then needs two things:
  - (H) COARSE_{−1}(Ξ_t v) is constant for t ∈ [f_1, f_{N−1} + 1], one state past the last counted fallback f_{N−1};
  - each counted event at k has k + 1 ≤ e, because the strict move b_{k+1}(y) ▷ b_k(y) with equal COARSE_{−1} reads COARSE at k + 1.
- (H) is (ii), and (ii) is proved:
  - FLAT-ALL_{−1} (iii) at each f_i with i ≤ N − 1. Its (h) at f_i + 1 holds because f_i + 1 ≤ f_N is the source of a transition of S.
    This includes f_{N−1}, whose step gives the extra state f_{N−1} + 1.
  - The clean intervals (f_i, f_{i+1}) for i + 1 ≤ N − 1 cover the S4a steps f_i + 1 → … → f_{i+1}. "Clean" counts the transitions
    j → j + 1 with f_i < j < f_{i+1}, which is every transition strictly between two fallbacks.
  - So COARSE_{−1}(Ξ) is constant on [f_1, f_{N−1} + 1]. ✓
- The counted fallbacks are k ∈ {f_1, …, f_{N−1}}, so k + 1 ≤ e. The k = e case of N-LV-2 never arises. ✓
  - f_N is not counted, which is where the +1 comes from. Its interval (f_{N−1}, f_N) may be dirty, and (h) at f_N + 1 may fail.
- N-LV-1 (H1 at k + 1, not H2) is not inherited. LV-PL′ uses FLAT-ALL_{−1} only through (iii). (iii)'s proof needs (i)'s routes, and (i)
  is right with H1 at k + 1 (R31 FBW-1), which holds since (h) is assumed at k + 1.
- (i): for i + 1 < N, LV-CN applies at f_{i+1} if it has no (β) gate. Under r ≥ 0 its gates are then all (α) ((γ) needs r = −1). Then
  f_{i+1} + 1 ends the phase, so f_{i+1} = f_N. Otherwise a (β) gate is a window gate (y ∈ R, z ∈ F), and ENT-X_{−1} applies. ✓
- (iii): every f_i has a level −1 tail (FB step (2)). So N − 1 ≤ Σ_y (tail events of y) ≤ n·n_E. ✓
- The data check (H) and the strict move directly; see §9.

## 5. SAND: SIGN
- θ_t ⊴ θ_{t′} ⊴ w_{t′} = w_t (R15 (a), XW; w is constant on S, the end state included by the scope-run definition).
- (C5): if θ_t ◁ θ_{t′}, then lev(θ_t, θ_{t′}) ≤ lev(θ_t, w_t) = −1. So the COARSE_{−1} values are equal. ✓
- Consequences:
  - Fact R and r_{g_N} = −1 give r = −1 on [g_1, g_N]. r = ⊥ is EQ, which is below −1, so it cannot sit between.
  - A fallback inside [g_1, g_N] has r = −1, so it is THR and one of the g_i.
  - FBW-S gives M ≤ r = −1, and M ≥ −1 at a fallback, so M = −1. ✓

## 6. FLAT-ALL_{−1}^{none}: SIGN
- (i), the new case (γ) (y = c, s ∈ F_k, z ∈ R̄_k, r = −1):
  - c keeps λ(c) = c (phase), so its H_{k+1}-play is a cycle through c.
  - H1 at k + 1 ((h) assumed there) keeps o off that cycle, and off o the honest and (σ, τ) graphs agree. So c ∈ F_{k+1}, and z has left R̄.
  - (α) is the same argument. (β) tails are in R_k and enter F_k ⊆ F_{k+1}.
  - So F_k ⊆ F_{k+1}, and a play reaching o at k + 1 meets no switched vertex: same play, same route. ✓
- (iii): off R̄_{k+1} it is OFF. OFF is stated for every in-phase transition and every v ∉ R̄_{k+1}, with no u* ≠ none hypothesis; it covers c
  and every vertex re-routed through z. On R̄_{k+1} it is Lemma G with the same route plus (ii). The route lies in R_k ∩ R_{k+1}, so it is
  disjoint from P(θ) ⊆ {o} ∪ F and from c ((C7)). ✓
- (ii): R31's sandwich (x0 ∈ F_k ⊆ F_{k+1} by (i), Lemma S (a), OFF, (C7)), or directly SAND. ✓
- (iv): TRANSFER with (iii). A gate of level > −1 at k + 1 would be one at k, but M_k = −1. ✓
- No step uses FBL or u* ≠ none. LV-SHAPE (signed, no r hypothesis) supplies the gate kinds. ✓

## 7. LV-NONE: SIGN
- (1), at an S4a step j ∈ (g_i, g_{i+1}) with COARSE_{−1}(Ξ) unchanged on [g_i + 1, j]:
  - M_j ≤ −1: TRANSFER at L = −1 down the steps from M_{g_i + 1} ≤ −1 (FLAT-ALL^{none} (iv)).
  - Every relevant Even change follows a gate (R15 (d)), so E_j ≤ M_j ≤ −1.
  - U-loc (R28 (a), any game, inside a phase) at L = −1: a change at v needs a relevant change of level > −1 on v's path before λ(v). That
    is σ̄(o)'s, with O_j > −1 ≥ E_j: an ε-transition.
  - OR (c) (R30 (a): at an ε-transition, lev(θ_j, θ_{j+1}) = O_j) gives lev ≥ 0. r_j = −1 (§5), so SAND gives lev ≤ −1. Contradiction. ✓
  - At g_i (i < N): FLAT-ALL^{none} (iii). (h) at g_i + 1, since g_i + 1 ≤ g_N is a source of S. ✓
- (2): STRETCH_{−1} with s := g_1, e := g_{N−1} + 1. This is the same shape as §4: (H) is (1), and the events at k ≤ g_{N−1} have k + 1 ≤ e.
  - The g_i have M = −1 (§5) and a level −1 tail (FB step (2)).
  - STRETCH_{−1}'s proof has no r hypothesis (checked against P-N5-LV §3 and my R2-N5-LV §3). So N − 1 ≤ n·n_E. ✓
- Note: NL is not needed. The packet's §7 Note is right: SAND + U-loc + OR replace "NL at L = −1".

## 8. SCOPE-FB: SIGN CONDITIONAL (as stated)
- Every in-scope fallback is in exactly one class:
  - EQ (r = ⊥);
  - none (r = −1, M = −1 by FBW-S);
  - block (r ≥ 0, M = −1);
  - level ≥ 0 (r ≥ 0, M ≥ 0).
  r < ∞ under (h), and M ≥ −1 at a fallback.
- The bounds:
  - level ≥ 0: R40 PL-S″, landed;
  - block: §4;
  - none: §7;
  - EQ: R37 (d) EQ-END. Every EQ fallback of S is the last transition of its phase, so S has at most one. CN-LAST is R38.
- 2nn_E + 2(nn_E + 1) + 1 = 4nn_E + 3. ✓

## 9. Data (DATA, not proof)
- Batch (R2-N5-LV2/run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O files (files.lst, my predecessor's R2-N5-LV list, which contains the
  packet's NAMED and LIB sets) × 3 traces × 3 starts = 2,655 runs; random 𝒞^1O 64,000 runs. 893 / 893 logs end "RESULT OK violations=0".
  - STALE-GATE 256,408 checks, EV-G 124,608 checks, SAND 1,965 checks.
  - In-scope fallbacks (library, own / rand / spec): level ≥ 0: 1,300 / 1,065 / 1,305; EQ 0 / 0 / 35; block 0; none 0.
  - Random: EQ 65 + 304, level ≥ 0: 1, none 0, block 0.
  - Largest per scope run: 37 fallbacks (all level ≥ 0); worst ratio to 4·n·n_E + 3: 37‰ (library), 52‰ (random).
- Newer files (run_new.sh, files_new.lst, logs_new/, totals_new.txt): 158 tracked 𝒞^1O files added since that list (lane instances of boxes
  38-40 and earlier REFEREE-2 climb outputs; docs/referee/ excluded) × 3 × 3 = 1,422 runs. 474 / 474 logs OK. The one none fallback per
  trace is my predecessor's witness best_lv_9401.pg.
- Climbs (run_climbs.sh, climb/, totals_climb.txt): 5 climbs, 430,936 evaluations, 1,723,744 runs, 6,873,091 states, 0 violations.
  - FIT none: 9501 (1,500 s, seeded with best_lv_9401.pg; run with an earlier fitness weighting, same checks), 9502 (n 8-14), 9503
    (n 10-16).
  - FIT blk: 9504 (n 8-14), 9505 (400 s, seeded with best_none_9501.pg).
  - 9501 reached the none part 237,030 times. SAND 919,988 checks. FLAT-ALL^{none} (i)-(iv) held in 237,030 cases, 2 of them with a (γ) gate.
  - 9501 also produced 645 level −1 block fallbacks (THR, r ≥ 0, M = −1), the first in any data I know of, but at most one per scope
    run. They came from evaluations inside the climb and were not saved; 9505, meant to produce a witness, did not reach one.
  - Max per scope run: none 1, block 1, EQ 1, level ≥ 0: 5, all 5. Worst ratios: LV-NONE 22‰, SCOPE-FB 21‰.
  - The random-seeded none climbs (9502, 9503) reached r = −1 states (322,925 scope runs with an r = −1 state) but no fallback there.
  - best_none_9501.pg (sha1 04c1ce2b), n 11: 4 none fallbacks over its 4 runs, one per scope run.
- Mutation controls (one library file, best_lv_9402.pg): LV2_MUT=sand0 (SAND from the first THR state with any r) 56 violations;
  LV2_MUT=fa0 (FLAT-ALL^{none} also at r ≥ 0 fallbacks) 78 violations. eN / lastN (constancy up to g_N + 1, tail check at g_N) cannot
  bite in my data (N ≤ 1); the matching records (COARSE change at g_N, last tail move breaking) are 0.

## 10. Notes for the lane (none blocks a signature)
- N-LV2-1 (status): name R36 next to R37 (c) FREE-FREEZE in §0 / §2 (EV-G's "none" holds given R36).
- N-LV2-2 (wording, also in R37 (f) EV): read "Ξ_k(z) = ρ ⊕ Ξ_k(q)" as the P-set identity P(Ξ_k z) ∩ H = (ρ ∩ H) ⊔ P(Ξ_k q).
- N-LV2-3 (DATA, for §9 and the RESULTS entry): the none part is reached (237,033 in-scope THR fallbacks with r = −1 in my climbs, where
  the packet's data have 0), and so is the level −1 block (645 fallbacks with r ≥ 0 and M = −1, where both P-N5-LV2 §9 and P-N5-LV §6 have
  0). But no scope run has two of either. So FLAT-ALL_{−1}^{none} and SAND are exercised non-vacuously, while the parts of LV-NONE and
  LV-PL′ that need N ≥ 2 rest on the proofs. Candidate CONJECTURE for L-RED / L-SI: an in-scope THR fallback with M = −1 is the last
  fallback of its scope run.
