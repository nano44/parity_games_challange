# R-N5-OUT: REFEREE report on packet P-N5-OUT (box 37: SPLIT, EPOCH, F-FLAT, FREEZE-STEP + TAIL, NO-ENTRY-A + NE-COUNT, CASE-B-LEN + W-SIDE)
Referee: REFEREE (successor 8, session_01YRPeH49wEXXq7vW5qK35Gz), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's queue of 12:55Z (Lead's stamp).
- Object: docs/new/P-N5-OUT-box37.md at pinned trunk 719ce66, sha1 9f032e616b515d703da4939cc1b0de89eb658aba, 351 lines (checked with
  `git show 719ce66:docs/new/P-N5-OUT-box37.md | sha1sum`). Author: L-NEW successor 17; the proofs are successor 16's.
- Written 2026-10-25T13:01Z onward by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read docs/referee-2/R2-N5-OUT.md. D1: each statement was treated as wrong until its proof
  checked.

## Verdicts
| § | statement | packet label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma SPLIT (a), (b) | PROVED | SIGNED |
| §2 | Corollary EPOCH (corrected: X_S ≤ 2(n − 1)(B + 1), f_S ≤ K(X_S + 1) + X_S) | PROVED | SIGNED (premise FB-INT, P-N5-SCOPE: signed by both referees) |
| §3 | Lemma F-FLAT | PROVED | SIGNED |
| §4 | Lemma FREEZE-STEP (i)-(iii), Corollary TAIL | PROVED | SIGNED |
| §5 | Theorem NO-ENTRY-A (τ(o) = o, case A) | PROVED | SIGNED (one remark, no gap: OUT-R1) |
| §5 | Corollary NE-COUNT (a)-(c) | PROVED | SIGNED (premises EPOCH / FB-INT, TOGGLE-COUNT = R34 (e)) |
| §6 | Lemma CASE-B-LEN, Remark W-SIDE | PROVED | SIGNED |
| §7 | NO-ENTRY, NO-ENTRY-B, NO-ENTRY (τ(o) ≠ o), ROUTE-FROZEN, open core | not to sign | not signed. NO-ENTRY-B FALSE (nebc_cex_n14, per the Lead): CASE-B-LEN holds on it (DATA below) |
- No (P), and the label is exact. The one-player facts used are F1 (R17 (a)), S (a) (R18 (d)), FBL-N (R21 (c)) and (K) (R23 (a)). None
  rests on VJ00 Lemma 5.8. P-N5-RL is not used.
- Dependencies: KEY and FB-INT (P-N5-SCOPE) are signed by both referees (R-N5-SCOPE §C, 257c3d81; R2 6d6e4bcf). The packet's
  "IN REVIEW" status for them is now stale (a note).
- No gaps.

## 1. SPLIT: checked
- (a). v ∈ R_k has its W-cycle node c_w on C_W ⊆ R̄_k (¬H2). Its honest cycle node is c_θ (H1). c_θ ∈ F_k (H3H2's proof). Since
  c_w ≠ λ(v), R-STICK keeps v in R. Correct.
- (b). ACT (i) needs a switched s ∈ F_k with σ_{k+1}(s) ∈ R̄_k, along a gate (S4c switches gates).
  - FBL-N (iii) excludes F → R.
  - The filled-in o-target step is correct: FBL-N (ii) gives x = λ_W(o) = c_w ∈ R̄_k.
- "Entry at S4a, eviction at fallback, never both": correct.

## 2. EPOCH: checked
- Cutting before breaks: within a segment, the first entry after an eviction would be a break, so all entries precede all evictions.
- R is monotone up to the first eviction: S4a steps do not shrink it (SPLIT (a)), and fallbacks only evict (SPLIT (b)). R̄ only shrinks
  afterwards. So there are ≤ 2(n − 1) crossings per segment.
- Fallbacks: crossings (≤ X_S), plus FB-INT's K per crossing-free run (≤ X_S + 1 runs, each inside a distinct crossing-free run of the
  phase).
- The correction "+ X_S" is REFEREE-2's O-1, which my lane accepted in the SCOPE §C. Correct.

## 3. F-FLAT: checked
- Step 1.
  - FBL-N (ii) gives x = λ_W(x) = λ_W(z), and z ∈ F_k. On F_k, W = Ξ, so λ_k(x) = λ_k(z) = x. (F) gives Ξ_k(σ_k x) = (x, ∅, L_x − 1).
  - q, z's path to x, has no switched vertex: a switched x′ is its own cycle node, so λ(z) = x forces x′ = x.
  - At k + 1, x's play is the cycle x → z → q → x. A vertex above x on q would make that vertex the top, and λ_{k+1}(x) ≠ x would leave
    the phase. So P(Ξ_k z) = ∅. Correct.
- Step 2.
  - p, v's path to c, has no switched vertex before c, for the same reason.
  - c's cycle is either intact, or replaced by Step 1's cycle (topped by c, P = ∅).
  - So V_{σ_{k+1}, σ̄_k}(v) = Ξ_k(v): in the switched case p ⊕ (c, ∅, 0) in both. S (a) and R15 (a) give equality. Correct.
- Step 3: x0 = σ̄_k(o) ∈ F_k (H1). o ⊕ Ξ_k(x0) is attained by σ̄_k at k + 1. S (a) and R15 (a). Correct.

## 4. FREEZE-STEP and TAIL: checked
- Route form under H1: Ξ(z) = π_z ⊕ θ. Correct.
- (i), S4a case:
  - ACT (i) together with R15 (d) and the hypothesis gives no entry. With SPLIT (a), R_{t+1} = R_t.
  - A switched v ∈ R_t would have its target in F_{t+1}, so v would leave R; contradiction. Routes are unchanged.
- (i), fallback case: SPLIT (b), and a switched route vertex would point into F. Correct.
- (ii): same route and the same θ at both ends. Correct.
- (iii): the chain Ξ_t(z) = Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y) (R15 (a), (d)). Then z ≠ σ_t(y), so
  (y, z) ∈ Iσ_t with z ∈ R̄_t. Correct.
- TAIL: induction inside the stretch, where H1 holds at t + 1, up to the first θ-change. R̄ strictly shrinks at each crossing. Correct.

## 5. NO-ENTRY-A and NE-COUNT: checked in full
- Setting.
  - τ(o) = o gives w = (o, ∅, 0) and ¬H2 everywhere.
  - Under H1, c_θ ≠ o, and XW gives reward(c_θ) < reward(o).
  - Case A forces Ω(o) even; case B forces Ω(c_θ) odd. Both correct.
- (T1)-(T3): ≡ means the same cycle node and agreement at ranks ≥ rank(o).
  - (T1): the same top vertex on the same side decides.
  - (T2): an interval argument via (T1).
  - (T3): ⊕ adds the same vertex on both sides.
  - Correct.
- SEP-o.
  - z ∈ R̄: o ∈ P(θ), since o is not a cycle node (H1) and rank o > rank c_θ (case A). Routes add vertices above c_θ.
  - f ∈ F: the honest play avoids o.
  - Correct.
- BASE.
  - (i): FBL-N (iii) with the o-target step.
  - (ii), suppose ℓ ≥ rank(o): the top u of (π_z Δ π_{σ v}) ∩ V_{>c_θ} has rank u > rank o (u ≠ o).
  - The W-difference (π_z Δ π_{σ v}) ∩ V_{>o} has the same top u on the same side, since anything higher would be in the honest
    difference.
  - Case 1: z's route avoids v. Then v ⊕ W(z) ▷ v ⊕ W(σ v) = W(v).
  - Case 2: π_z = q·v·π_{σ v}. The difference lies on z's side, so u is even, and the new cycle has top u with reward p′(u) > p′(o).
  - Both cases contradict (K). Correct.
- STEP.
  - No entry: by (i), ACT (i) and R15 (d).
  - Value claim, by induction on the route length at t + 1. A switched z gives an R → R̄ gate at t, so (ii) at t applies. (T3) and (V1)
    at t and t + 1 (H1 at both) finish it.
  - (i) at t + 1:
    - SEP-o at t + 1 and (T1) give Ξ_t(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_t y), so (y, z) ∈ Iσ_t.
    - y ∈ F_t contradicts (i) at t.
    - y ∈ R_t: (ii) at t, then (T2), then o ∈ P on one side only. Contradiction.
  - (ii) at t + 1: the value claim, (ii) at t for a switched v, and (T1) give an R → R̄ gate at t of level ≥ rank(o). Contradiction.
  - Correct.
- OUT-R1 (remark, no gap): BASE cites (K), "at an S4c fallback inside a phase". If a → a + 1 left the phase, only b = a would be
  possible ([a, b] ⊆ S). (K)'s derivation (FBL-N (i), the arena optimum at a, plus F1) does not use a + 1, so BASE holds there as well.
  Worth one line in the lane text.
- NE-COUNT.
  - (a): the eviction a → a + 1 is a fallback (SPLIT). θ constant on [a, k + 1] would contradict NO-ENTRY-A with b = k + 1. j ≠ a by
    F-FLAT, and j → j + 1 is S4a. The next break's eviction follows this entry, so the intervals (a, k] are disjoint. Correct.
  - (b): EPOCH. Correct.
  - (c): ≤ ⌊T_ph/2⌋ + 1 H1-runs.
    - Exit fallbacks: ≤ 1 per stretch.
    - Σ_S (K(X_S + 1) + X_S + 1) ≤ (K + 1) Σ_S (2(n − 1)(θ_S + 1) + 1) = (K + 1)(2(n − 1)θ_ph + (2n − 1)N_HN).
    - X_HN ≤ 2(n − 1)(θ_ph + N_HN).
    - Arithmetic checked.
  - θ_ph is a parameter, as the packet says. This is not a bound on N5.

## 6. CASE-B-LEN and W-SIDE: checked
- Case B: rank u > rank c_θ > rank o, the same top for the W-difference, and the two BASE cases contradict (K). So the P parts are
  equal and lev = −1. c_θ is odd, so longer is better: z's route is longer. Correct.
- W-SIDE.
  - (K) forbids W(z) ▷ W(σ v) in case 1.
  - An empty W-difference with o odd would make z's longer route better, so Ω(o) is even. Both parities of o are possible in case B.
  - In case 2, (K) bounds the closed cycle's top.
  - Correct.

## 7. DATA (DATA, not proof; own code docs/referee/scratch/out_probe.py on rl_engine; logs rl_logs/out_lib37.txt, out_named.txt)
- lib37.txt: 270 𝒞^1O games (159 skipped, not 𝒞^1O). Named: rfroz_cex_n16, nebc_cex_n14 (the NO-ENTRY-B counterexample) and wd16_s2.

| check | lib37 | named (3) | failures |
| --- | --- | --- | --- |
| SPLIT (a) S4a steps / (b) fallbacks at HN states | 521 / 105 | 6 / 22 | 0 |
| F-FLAT (Ξ on F_k and θ at HN fallbacks) | 105 | 22 | 0 |
| FREEZE-STEP (i)-(iii), transitions meeting its hypothesis | 376 | 15 | 0 |
| HN stretches; EPOCH bounds | 113 | 8 | 0 |
| fallbacks inside stretches; of which crossings | 103; 103 | 22; 22 | — |
| τ(o) = o stretches, case A / case B | 25 / 12 | 4 / 1 | — |
| breaks; NE-COUNT (a) θ-separation (case A) | 11; 8 | 1; 0 | 0 |
| NO-ENTRY-A: runs [a, b] / states (INV (i), (ii), no entry, ≡-freeze) | 75 / 797 | 13 / 92 | 0 |
| CASE-B-LEN, R → R̄ gates at case-B HN fallback states | 0 | 4 (nebc_cex_n14) | 0 |

- The counts match the packet's §8: 113 stretches for successor 16's library; 11 breaks (8 case A + 3 case B); 25 / 12 τ(o) = o case
  A / B; every in-stretch fallback a crossing.
- On nebc_cex_n14, CASE-B-LEN holds at all 4 case-B gates. The CONJECTURE NO-ENTRY-B fails there, which is §7 and not mine to sign.
  This is consistent: CASE-B-LEN restricts the gate's shape, and does not exclude entries.
- Not tested: NE-COUNT (c)'s f_HN bound and N_HN ≤ ⌊T_ph/2⌋ + 1 per phase (skipped). They are checked as arithmetic above.
- Thin spots:
  - CASE-B-LEN has 4 checks, all on the counterexample.
  - FB-INT's per-run term is never used: every in-stretch fallback is a crossing.

## TARGET.md diff
Not a claim of TARGET.md §2. These are lemmas about N5 inside a phase on 𝒞^1O, and θ_ph is an open parameter. The packet says so: "not a
running-time bound … G-N5-TIME stays OPEN". No statement about general games.

## Fixes-file lines (notes only; no gap)
- OUT-R1 (§5 BASE): note that (K) is used at the state a only, so b = a with a phase-exiting fallback is covered.
- OUT-N1 (dependency table): KEY and FB-INT are signed by both referees (no longer "IN REVIEW").

Signed: REFEREE (successor 8) (Opus 5.5, D15).

## §C. Comparison with REFEREE-2 (written 2026-10-25 14:07Z by date -u; REFEREE successor 8 (Opus 5.5, D15))
- Compared against: the FINAL docs/referee-2/R2-N5-OUT.md at referee-2 dfcaae67 (merged to trunk 9f83566), named by the Lead at 14:03Z
  (Lead's stamp). I read it after this report (fa086876) was pushed.
- Verdicts: identical. Both referees sign SPLIT, EPOCH (corrected; both note that "+ X_S" is needed), F-FLAT, FREEZE-STEP, TAIL,
  NO-ENTRY-A, NE-COUNT (a)-(c), CASE-B-LEN and W-SIDE. Neither signs §7.
  - R2 treats W-SIDE's "Consequence" as a READING. So do I: the packet labels it READING, and my "Remark W-SIDE" signature covers the
    remark, not the Consequence.
- No gap in either report. Joint gap map: empty. R2's notes:

| R2 note | what it says | checked | this lane | joint status |
| --- | --- | --- | --- | --- |
| N-OUT-1 | FBL-N's R contains o, so FBL-N (iii) already excludes the target o; the "(filled in)" step is redundant but correct | P-N5-X-box28.md §0 l.35: "R_k: the vertices whose (σ_k, τ_k)-play reaches o, with o ∈ R_k by convention". Correct | I checked the filled-in step as correct (§1) but did not see that it is redundant | ACCEPTED (note) |
| N-OUT-2 | Step (K) is stated "inside a phase", and NO-ENTRY-A BASE (and CASE-B-LEN) allow a + 1 to leave it. Cite FBL-N (i) + F1, or require a + 1 ∈ S | the same point as my OUT-R1. R2 also applies it to CASE-B-LEN, which has the same "a fallback is taken at a" hypothesis, and which I did not flag | OUT-R1 (BASE only) | ACCEPTED, extended to CASE-B-LEN (note) |
| N-OUT-3 | the KEY / FB-INT status column is stale | = my OUT-N1 | found | ACCEPTED (note) |
| N-OUT-4 | §7's CONJECTURES NO-ENTRY-B and NO-ENTRY (τ(o) ≠ o) are FALSE: nebc_cex_n14, tauw_A_cex_n24, tauw_B_cex_n24 (lane box 38) | §7 is not to sign. DATA (own out_probe.py, inputs only; sha1 399119af, e29908d5, c0ad4f0c): every signed check holds on all three, with 0 failures (SPLIT 12 / 11, F-FLAT 11, FREEZE-STEP 4, CASE-B-LEN 4, 5 stretches) | I recorded NO-ENTRY-B's falsity (per the Lead) only | ACCEPTED (record); no signed item is affected |

- Fixes-file lines (L-NEW, P-N5-OUT; none blocks a signature):
  - N-OUT-1: SPLIT (b) / F-FLAT Step 1: mark the o-target step as already covered by FBL-N (iii) (o ∈ R there).
  - N-OUT-2 = OUT-R1: cite FBL-N (i) + F1 (or Step (K)'s proof) in NO-ENTRY-A BASE and CASE-B-LEN.
  - N-OUT-3 = OUT-N1: KEY / FB-INT status → signed by both referees.
  - N-OUT-4: §7: NO-ENTRY-B and NO-ENTRY (τ(o) ≠ o) → FALSE (the three instances).
- Joint state: all of §1-§6's signable statements are PROVED (L-NEW succ. 16 / 17) and signed by both referees (Opus 5.5, D15), with
  no (P), pending CHECKER.
