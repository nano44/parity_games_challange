# R-N5-LV: REFEREE report on packet P-N5-LV (box 11: LV-SHAPE, LV-CN, LV-COUNT, FLAT-ALL_{−1}, STRETCH_{−1}, PL_{−1}, LV-PL)
Referee: REFEREE (successor 9, session_01VsZYJ8FiTSj5Kazk715ZP7), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's GO of 14:51Z (Lead's stamp), second after P-N5-NEB.
- Object: docs/si/P-N5-LV-box11.md at pinned trunk 601df6e, sha1 d0d797f084904f9ce4df641e90298cac53c61356, 144 lines (checked with
  `git show 601df6e:docs/si/P-N5-LV-box11.md | sha1sum`). Not-to-sign addendum docs/si/P-N5-LV-addendum-box11.md, sha1
  a15a8871024d33d1734a41cbeb9c2dd75ecdadef (l-si 84974fea; not in 601df6e, checked on trunk 51bb725). Author: L-SI successor 6.
- Written 2026-10-25T15:20Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-LV.md. D1: each statement treated as wrong until its proof checked.

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Proposition LV-SHAPE | PROVED (no (P)) | SIGNED |
| §2 | Corollary LV-CN, Corollary LV-COUNT | PROVED CONDITIONAL on CN-LAST | SIGNED. The condition is discharged: CN-LAST is RESULTS R38 (f), landed 14:16Z, with exactly LV-CN's hypotheses |
| §3 | Lemma FLAT-ALL_{−1} | PROVED | SIGNED |
| §3 | Lemma STRETCH_{−1} | PROVED | SIGNED (note LV-N2) |
| §4 | Theorem PL_{−1} (a)-(c), Corollary LV-PL | PROVED | SIGNED (notes LV-N2, LV-N3, wording inherited from R31 PL) |
| §5, addendum | CONJECTURE "in scope, THR ⇒ M ≥ 0"; OPEN u* = none, REL(S) at level −1; NL=, straddle material | not to sign | not signed |
- No (P). The label is exact: LV-SHAPE uses Lemma G, XW, FBW (b), R-SAME (R37 (a)) and BL Step 2a = R31 FBW Step 2 with V := W_k plus
  P-OPT. None needs (P).
- Statuses now: R-SAME / BL are RESULTS R37 (landed 14:01Z) and CN-LAST is R38 (landed 14:16Z); the packet's "in landing" is stale
  (note LV-N1).
- VACUOUS IN DATA (lesson N-ENT-2): the LV setting (in-scope THR fallback with M = −1) occurs 0 times in the packet's data and 0 times
  in mine (§6). So §1-§4 are checked on their proofs only. My climb toward the setting: §6.
- No gaps.

## 0. Setting
- k is an in-scope S4c fallback (k → k+1 in S, so in-phase and Even's), THR at k, M_k = −1. Gates are strict, so every gate level is
  ≥ −1; hence every gate has level −1. Correct.

## 1. LV-SHAPE: checked case by case
δ := max(lev(Ξ s, W s), lev(Ξ z, W z)). The four cases (s ∈ F or R̄) × (z ∈ F or R̄) are exhaustive.
- (F, F): Ξ = W at s and z (Lemma G off R̄), so δ = ⊥ < −1 = ℓ, and FBW (b) applies: y is its own W- and Ξ-cycle node. (α). Correct.
- (R̄, R̄):
  - Under (h), Ξ = π ⊕ θ and W = π ⊕ w on R̄ (π_o = ∅). R-SAME (R37 (a)) gives the same order for a ∈ {θ, w}. So the gate is
    W-improving.
  - BL Step 2a: FBW Step 2 (with V := W_k) gives a strict improvement of y by σ_k[y ↦ z] ∈ A(σ_k), outside its single exceptional
    case. P-OPT forbids the improvement, so the case holds: y is its own W-cycle node.
  - y ∈ R̄ (its successor s is), so y's W-play starts on its cycle and reaches o. Hence o lies on a W-cycle, against H2. Correct.
- (F, R̄):
  - Ξ z = π_z ⊕ θ ▷ Ξ s = W s, and W z = π_z ⊕ w ⊵ π_z ⊕ θ (XW, (C7)). So the gate is W-improving.
  - The exceptional case of Step 2: y is its own W-cycle node, P(W z) = ∅, W(z) has cycle node y, and lev(W s, W z) = −1.
  - If r ≥ 0: lev(W s, Ξ z) = −1 and lev(Ξ z, W z) = r. Two uses of (C6) force lev(W s, W z) = r: ≤ max(−1, r) = r, and
    r ≤ max(−1, lev(W s, W z)) with r ≥ 0. This contradicts −1. So r = −1 (THR: r ≥ −1).
  - W(z) = π_z ⊕ w has cycle node c (H3), so y = c ∈ F, and on F the honest play is the W-play, so λ(y) = y. (γ). Correct.
- (R̄, F):
  - y ∈ R (y Even, s ∈ R̄). Level −1 gives P(Ξ z) = P(π_s ⊕ θ) = (π_s ∩ V_{>c}) ⊔ P(θ).
  - P(Ξ z) ⊆ F (z's play avoids o). So π_s ∩ V_{>c} = ∅ and o ∉ P(θ). By H1, o is the first vertex of θ's play and not its cycle node,
    so rank o < rank c.
  - If r ≥ 0: lev(W z, Ξ s) = −1 < r = lev(Ξ s, W s), and W s ▷ Ξ s. By (C6) twice, W s ▷ W z, decided at level r. (β). Correct.
- "Exactly one": the cases are disjoint by the location of s and z; (R̄, R̄) is empty. Correct.

## 2. LV-CN and LV-COUNT: checked
- LV-CN: (α) and (γ) both give λ_k(y) = y and level −1. S4c is Even's (Iσ_k ≠ ∅). These are exactly CN-LAST's hypotheses (R38 (f):
  "Iσ_k ≠ ∅, and every gate (y, z) ∈ Iσ_k has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1"). Its conclusions are LV-CN's. Correct.
- LV-COUNT: a non-(β) fallback ends its phase, so there is at most one per phase. If rank o > rank c (a phase constant: c = λ(o)), (β)
  is impossible by its clause rank o < rank c. Correct.
- With R38 landed, both are unconditional (relative to landed results).

## 3. FLAT-ALL_{−1} and STRETCH_{−1}: checked against R31 P-N5-FBW §3, §4 (sha1 88337bd6)
- FLAT-ALL_{−1}. R31's proof uses M ≥ 0 only to get r_k ≥ 0 (THR with u* ≠ none, hence FBL); here r_k ≥ 0 is a hypothesis. The other
  steps, at M = −1:
  - (i) FBL + H2 + the phase: level-free.
  - (ii) The sandwich θ_k ⊴ θ_{k+1} ⊴ o ⊕ Ξ_{k+1}(x0) (Lemma S (a), R15 (a)) and OFF at level M_k = −1. OFF (R25 (e), P-N5-FB §5)
    is stated for COARSE_{M_k} with any M_k. COARSE_L, (C1)-(C4) are defined for −1 ≤ L < ∞ (P-N5-FB §1), and its proof via (T) is
    level-free.
  - (iii) OFF, Lemma G (b), (C7), (ii).
  - (iv) TRANSFER (R29 (b): "L < ∞"), at L = −1 with (iii) at z.
  Correct.
- STRETCH_{−1}.
  - Step (1): a switch of a non-cycle-node y at level > −1 changes COARSE_{−1}(Ξ y) ((P2), (C7)), which is excluded. A cycle-node
    switch has level −1 (CN, R29 (d), inside a phase). A level −1 switch lands on the same COARSE_{−1} value. So COARSE_{−1}(b_t y) is
    constant.
  - With (c_y, P_y) fixed, ⊴ is the length order. b(y) is non-decreasing (R15 (a), (d)), and each level −1 tail event moves its length
    strictly (FB step (2): the best target z has Ξ_k z ▷ b_k y with the same coarse part, and Ξ_{k+1}(z) ⊵ Ξ_k(z)). Lengths lie in
    {0, …, n − 1}. Correct.
- LV-N2 (precision, no gap; it also applies to R31 STRETCH / PL (a)):
  - As written, STRETCH counts fallbacks k < e, and PL (a) applies it "per run" with that run's last block fallback as the right end.
  - The proof gives the count for k ≤ e. Order the tail events k_1 < … < k_m ≤ e of y; then b_{k_1}(y) ◁ b_{k_2}(y) ◁ … ◁ b_{k_m}(y),
    all with the same coarse part. The last event needs no state after it. So m ≤ n.
  - Alternatively: for a run ending at f_b with b < N, FLAT-ALL_{−1} (iii) at f_b makes f_b + 1 available as e; only the run ending at
    f_N needs the k ≤ e form.
  - Either way, PL_{−1} (a)'s n·n_E per run holds.

## 4. PL_{−1} and LV-PL: checked against R31 PL and R35 PL (c′)
- The block is consecutive: levels are non-increasing (CLS2), and r is non-increasing along S (Fact R, R29 (a)). So {M = −1} is a suffix
  of S's fallbacks, {r ≥ 0} a prefix, and the block is their intersection. Every state of [f_1, f_N] has r ≥ r_{f_N} ≥ 0. Correct.
- (a):
  - For i < N, the transition f_i + 1 → f_i + 2 is in S, so (h) holds at f_i + 1, and FLAT-ALL_{−1} (iii) applies at f_i.
  - COARSE_{−1}(Ξ) changes only inside dirty intervals, so the block's fallbacks lie in ≤ 1 + D_{−1} runs of constant COARSE_{−1}(Ξ).
  - Every block fallback has a level −1 tail (FB step (2)). STRETCH_{−1} (LV-N2 reading) gives ≤ n·n_E per run. Correct.
  - LV-N3 (wording, from R31): "[f_1, f_N] splits into at most 1 + D runs" is false if a dirty interval contains several COARSE
    changes. Intended: "the block's fallbacks lie in at most 1 + D runs".
- (b):
  - M_{f_i+1} ≤ −1 (FLAT-ALL_{−1} (iv)), and M_t ≤ −1 persists by TRANSFER while COARSE_{−1} is unchanged. So E_j ≤ −1 (R15 (d)).
  - There is no S4c inside the interval (the block is consecutive among S's fallbacks) and no S4b (in-phase), so j is S4a.
  - U-loc (R28 (a), "any level L") at L = −1 forces a relevant σ̄(o) change at level ≥ 0, so O_j > −1 ≥ E_j. Then Lemma OR (c) /
    TC-SPLIT and OR (a)-(b) with H1. Level-free. Correct.
- (c):
  - (A_{f_i+1}) at L = −1 from OFFGATE (gates into F at f_i + 1 have level ≤ M_{f_i} = −1).
  - NL (R29 (e): "L < ∞, r_j > L") at L = −1 needs r_j ≥ 0, which holds on [f_1, f_N]. NL (iii) propagates (A); NL (ii): no exit
    leaves R at the S4a steps.
  - Each dirty interval contains an absorption (b), which raises N_x by ≥ 1, with no simultaneous leave. N_x falls only at
    f_1, …, f_{N−1} (by REL_{−1} in total) and stays in [0, d_o − 1] (H1).
  - So D_{−1} ≤ (d_o − 1) + REL_{−1}, and N ≤ n·n_E·(d_o + REL_{−1}). Correct.
- LV-PL: REL_{−1} ≤ REL(S). The block is exactly S's in-scope THR fallbacks with M = −1 and r ≥ 0. With LV-COUNT (now unconditional),
  all but one per phase are (β). Correct.
- LV-N1 (status): R-SAME / BL (R37) and CN-LAST (R38) are landed; §0's "SIGNED, in landing" / "In landing" are stale.

## 5. NOT TO SIGN
- Not signed. Data on the CONJECTURE "in scope, THR ⇒ M ≥ 0": my 788 in-scope THR fallbacks all have M ≥ 0 (§6). The two OPEN items
  and the NL= material (addendum) are not used by §1-§4. I checked this: no step above cites NL at r_j = L, the straddle files, or ENT-X.

## 6. DATA (DATA, not proof; own code docs/referee/scratch/lv_probe.py on rl_engine, no lane imports; logs docs/referee/R-N5-LV/)
- Files: experiments/new/box33/lib.txt, experiments/new/box37/lib37.txt, experiments/si/coarse/named.txt, coarse/instances (+ box9),
  experiments/si/riselast/instances, experiments/red/so/instances: 447 paths, 288 in C^1O (159 skipped). The list is
  docs/referee/R-N5-LV/files.txt.

| check | count | failures |
| --- | --- | --- |
| in-scope fallbacks: THR r ≥ 0 with M ≥ 0 / with M = −1 | 788 / **0** | — |
| in-scope fallbacks: THR r = −1 (u* = none) | **0** | — |
| in-scope EQ fallbacks (all M = −1); FBW-S shape (length-only switch at a cycle node) | 11 | 0 |
| LV-SHAPE / LV-CN / FLAT-ALL_{−1} / block bound (LV setting) | **0** (vacuous) | — |

- Climb toward the setting: §6.1.

### 6.1 Climb (own code: scratch/lv_climb.py with neb_climb's C^1O mutations; logs scratch/lv_logs/climb_1..3.txt; 20 min each, 15:24-15:44Z)
- Seeds: three of the 8 games with an in-scope EQ fallback at M = −1 (box25 tr12_s3, red/xing x32_rand16, x31_ru24).
- Score = 100 · #(in-scope THR fallbacks with M = −1) + #(in-scope THR fallbacks with M ≤ 1).
- Result: 2,636,361 mutants tried, best score 0 in all three walks. No in-scope THR fallback appeared at all, and no LV-setting state
  (0 hit files).
- In-scope EQ fallbacks with M = −1: 92,618 occurrences (re-counted per evaluation), FBW-S shape 0 failures.
- So the climb was in effect a random walk and is WEAK evidence: it did not get near the setting. §1-§4 stand on their proofs alone,
  and the packet says the same (§6: "§1-§4 have vacuous hypotheses there. They rest on the proofs").

## Notes for the lane's fixes file (none is a gap)
- LV-N1: statuses: R-SAME / BL (R37) and CN-LAST (R38) are landed; §2's "CONDITIONAL on CN-LAST" is discharged.
- LV-N2: STRETCH_{−1} (and R31 STRETCH) holds for fallbacks k ≤ e; PL_{−1} (a) needs that form for the run ending at f_N.
- LV-N3: PL_{−1} (a): "the block's fallbacks lie in at most 1 + D_{−1} runs of constant COARSE_{−1}(Ξ)".

## §C. Comparison with REFEREE-2 (docs/referee-2/R2-N5-LV.md at referee-2 b1038bea; sha1 66e55e04…, the same on trunk e05382f4)
Written 2026-10-25T16:18Z by date -u, after the Lead's word of 15:59Z (Lead's stamp) that b1038bea is final. I opened R2-N5-LV only after
my report 8054da2f was pushed. (Opus 5.5, D15).
- Verdicts: the same in substance. Both referees sign every statement of §1-§4, and neither signs §5 / the addendum.
  - R2 labels LV-CN, LV-COUNT and LV-PL's last sentence "CONDITIONAL ON CN-LAST", since CN-LAST was "landing".
  - I wrote that the condition is discharged by R38 (f) (landed 14:16Z).
  - Both readings agree that CN-LAST carries the condition.
- Joint gap map: EMPTY.

| item | REFEREE-2 | REFEREE (mine) | outcome |
| --- | --- | --- | --- |
| FLAT-ALL_{−1} (i) cites H2 for "the switched cycle node's new cycle avoids o" | N-LV-1: H1 at k + 1 (R31 FBW-1) | my §3 repeated "FBL + H2" | MISSED by me; ACCEPTED. An honest cycle through o need not be a W-cycle (the honest and W-plays differ at o), so H2 does not exclude it; H1 at k + 1 does. (h) at k + 1 is assumed, so no verdict changes |
| STRETCH_{−1} stated for k < e; PL_{−1} (a) needs k = e for the run ending at f_N | N-LV-2 | LV-N2 | same point |
| PL_{−1} (a) "splits into ≤ 1 + D runs" | — (R2 §4 writes "groups", the corrected reading) | LV-N3 | same substance; wording note |
| statuses (R-SAME / BL R37, CN-LAST R38) | (CN-LAST "landing") | LV-N1 | stands |
| u* = none (r = −1) in-scope THR fallbacks occur | N-LV-3 (DATA): 173,371 in R2's climbs; witness best_lv_9401.pg (sha1 4b74cd84…) | my data and climb: 0 | ACCEPTED, and RE-RUN on my engine: on best_lv_9401.pg (canonical start) my lv_probe finds 1 in-scope THR fallback with r = −1, M = −1 and 7 gates, all (β), LV-SHAPE 0 failures. My statement "the setting is VACUOUS in data" holds only for the r ≥ 0 part (FLAT-ALL_{−1}, PL_{−1}, LV-PL); LV-SHAPE's r = −1 case is exercised |
| STRETCH step (1): injectivity of x ↦ COARSE_{−1}(y ⊕ x) | filled in (via P-N5-ENT BF) | used without comment | R2's fill-in is correct; adopted |

- NL= (the addendum's CONJECTURE, not to sign): L-RED reports it FALSE on experiments/red/so/instances/nleq_cex_n48.pg, sha1
  e72e40343b33df295d5877ff29125b154e71949c (re-measured by me; l-red d7df76f9: an NL (ii) leave at r = L = 47, j 6, vertex 40 → 9; the Lead
  re-ran it). I have not re-run it.
  - NL= is on the addendum's not-to-sign list, and no step of §1-§4 cites NL at r_j = L (checked in my §5). So no signed item is
    affected. CONFIRMED.
- For the fixes file (union): N-LV-1, N-LV-2 = LV-N2, LV-N1, LV-N3, and N-LV-3's correction of §5's "DATA: 0 in scope".
- Follow-up DATA on N-LV-3 (own code scratch/lvn_climb.py on my engine, seeded with R2's best_lv_9401.pg as an input file only; 3 × 12 min,
  16:16-16:28Z; logs scratch/lvn_logs/):
  - 769,515 mutants evaluated. Counts are re-counted per evaluation of kept games.
  - 351,417 in-scope THR fallbacks with r = −1, M = −1.
  - LV-SHAPE checked at 1,321,606 gates: (α) 330,221 / (β) 874,883 / (γ) 116,502. 0 failures. (γ), seen twice by R2, is frequent here.
  - No scope run had more than one such fallback (best score 1.01).
