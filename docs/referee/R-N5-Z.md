# Referee report R-N5-Z: crossings of N5 reduce to reversals of R (L-SI box 4 lemmas)

Referee: REFEREE (successor 4), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-Z: the Lead's message of 2026-10-24 20:3xZ (read
20:34Z). Pin: trunk claude/vibrant-johnson-nxvvxo fba7177 (an ancestor of my merged HEAD). Object: docs/si/P-N5-Z-box5.md, sha1
a027638f06d18143ed0779290b24f8e5decb8249 (219 lines; verified at the pin). L-SI successor 2, l-si 57dbb8b.
Context read: SPEC S1-S5; RESULTS R15, R18 (d), R19 (a), R21 (a), (c), (g) and its repairs (my R-N5-X, §C); the box 4 source text was not
needed (the packet governs). docs/referee-2/ was NOT read for this packet.
Written 2026-10-24 20:34Z-20:37Z by date -u. Every verdict is labelled (Opus 5.5, D15).
Convention as in the packet: R_k excludes o, R̄_k = R_k ∪ {o}, F_k = V ∖ R̄_k. The crossing transitions are the same as in R19-R21 (o is
in R̄ at every state).

## Verdict
| item | verdict (Opus 5.5, D15) |
|---|---|
| (1) §7 LV′: X ≤ (n − 1)(Z + 1) + Z, Z ≤ X | SIGNED WITH GAPS: Z-1 (wording: the proof's "maximal run of consecutive equal pure signs" must be read with a '±' crossing BREAKING a run; if a '±' were skipped, the step "each run has ≤ n − 1 crossings" would fail, since a '±' can lower \|R\| inside a '+' run. The inequality itself is true, by the breaking reading) |
| (2) §9 Corollary Z | SIGNED. R21 (g) is used inside its signed hypotheses: the same phase, the same X (crossing transitions are convention-independent), the same O. The O(n⁵(1 + Z + O)) arithmetic is checked. The READING part (Lemma Φ, τ-changes ≤ d − 1) is not signed |
| (3) §4 NOFE, strengthened form | SIGNED. Note Z-2: it also follows in one line from the signed R21 (c) FBL-N (ii) (λ_W(z) = y with z ∈ R̄ puts y on o's W-play, even as its cycle node). Z-3: "σ_k y ∈ F_k by (F0)" is a state-k fact (y ∈ F_k), not (F0); wording |
| (4) §1 Step (K) | SIGNED |
| (4) §2 ACT (i)-(ii) | SIGNED |
| (4) §3 LOOP and its Corollary | SIGNED |
| (4) §5 NOFL-E and its Corollary | SIGNED |
| (4) §6 GAP | SIGNED (the "Reading (integer form)" is not signed) |
| (4) §8 WM and its Corollary | SIGNED |
No statement is NOT SIGNED. No counterexample. (Z), (C) and G-N5-TIME stay OPEN; (X) = (Z) up to a factor n is a REDUCTION, as the Lead says.

## 1. LV′ (§7)
- Every crossing has a sign. Write Z = #'±' + #(pure-sign crossings whose sign differs from the previous pure-sign crossing).
- Read "a maximal run of consecutive equal pure signs" as a maximal block of consecutive CROSSING transitions that are all '+' or all '−'.
  A '±' crossing ends a run, but non-crossing transitions between them do not.
  - Inside such a run R changes only by ⊊ steps in one direction, so |R| is strictly monotone in {0, …, n − 1} (R ⊆ V ∖ {o}): ≤ n − 1
    crossings per run.
  - A run boundary is either a '±' or a sign change between consecutive pure crossings, so #runs ≤ Z + 1. Total: X ≤ (n − 1)(Z + 1) + Z.
    Z ≤ X since every counted item is a crossing. Correct.
- Z-1. If a '±' crossing were skipped when forming runs (Z's own definition compares a pure sign with the PREVIOUS PURE sign, skipping
  '±'), a "run" '+ ± + ± …' could contain arbitrarily many '+' crossings with |R| bounded, because each '±' may lower |R|. Then the
  per-run step fails, although the inequality still holds (every '±' is counted in Z). The proof needs the breaking reading. The packet's proof sentence "there are at most Z + 1 such runs, and at most Z '±' transitions" fits it.
- DATA: 596 phases, max X 78 (x32_waves48), max Z 22 (zcl_cu_n48), 0 failures; my Z values equal the packet's on zcl_fb2_n32 (18) and
  zcl_cu_n48 (22).

## 2. Corollary Z (§9)
- R21 (g), as landed with the repairs of R-N5-X: per PHASE (joint λ-phase, τ constant), with X = #crossing transitions and O =
  #OTHER-touching transitions. The packet uses the same phase notion. Its crossings ("R_{k+1} ≠ R_k" with o excluded) are R21's crossings
  (o ∈ R̄ always). O is R21's.
- Substituting X ≤ (n − 1)(Z + 1) + Z ≤ n(Z + 1): (3n²(1 + n(Z + 1) + O) + n(Z + 1) + O + 1)(4n(n − 1) + 1) = O(n⁵(1 + Z + O)). Checked.
- The READING (Lemma Φ is unrefereed, as the packet says; τ-changes ≤ d − 1 by R15 (c) on G^d, my R-N5-X §0) is not signed.

## 3. NOFE (§4), strengthened form
Checked step by step.
- The gate gives Ξ_k(z) ▷ Ξ_k(σ_k y).
- y ∈ F_k puts σ_k y in F_k: y's o-free play passes through σ_k y. That is a state-k fact; the citation of (F0) is misplaced (Z-3). Then
  Lemma G (a) and XW give W_k(z) ▷ W_k(σ_k y).
- If y is not on o's W-play, z's W-play (its route in R_k, then o's W-play, or o's W-play if z = o) avoids y. So σ_k[y → z] gives y
  exactly y ⊕ W_k(z).
- Case A (y ≠ λ_W(y)): (VAL), then (F-pre). y is on neither path and is neither cycle node: z's cycle avoids y, and λ(σ_k y) = λ(y) ≠ y.
  Correct.
- Case B (y = λ_W(y)): the cycle nodes of W_k(z) and W_k(σ_k y) = (y-cycle) differ, so the strict W-inequality is decided by them, and
  y ⊕ W_k(z) keeps the better cycle node. Correct.
- Step (K) then contradicts FBL-N (i). The case analysis does remove the "or on a (σ_k, τ)-cycle" escape of box 4: the only escape left
  is y on o's W-play. Correct.
- Z-2: R21 (c) FBL-N (ii) (signed) already gives, for every gate edge from F at such a fallback, λ_W(y) = y and λ_W(z) = y. With
  z ∈ R̄_k, z's W-play reaches o and then follows o's W-play to its cycle node y. So y lies on o's W-play, and is in fact o's W-cycle
  node. That is NOFE in one line, and stronger. The packet's own proof is valid and independent.
- DATA: 17 switched F_k → R̄_k edges at fallbacks (nofe_cyc_n8 + random), all with y on o's W-play; 0 failures.

## 4. Step (K), ACT, LOOP, NOFL-E, GAP, WM
- Step (K): σ_k[y → z] is an arena strategy when (y, z) is an arena edge. A pointwise optimum dominates every arena strategy ((F1);
  R21 (c) FBL-N (i) at a fallback with τ unchanged). A strict gain at y contradicts it. SIGNED.
- ACT (i): x ∈ R_{k+1} ∖ R_k ⊆ F_k, its new play stops at the first visit of o, and the switched vertices s_1, …, s_j are found on it
  (j ≥ 1, else old edges give x ∈ R_k). (F0) applies to every non-switched vertex, forced Odd ones included (τ fixed). It holds along each
  segment, including the segment σ_{k+1}(s_i) = s_{i+1}. The parity argument finds an F → R̄ switch. SIGNED.
- ACT (ii): as (i), with x ∈ R_k ∖ R_{k+1}. If no switch goes R̄ → F, the whole play (not containing o) lies in R_k, and its final cycle
  must contain a switched vertex, since old cycles inside R_k are impossible. SIGNED.
- LOOP: c := λ_{Ξ,k}(o) lies on o's honest final cycle, which avoids o (H1), and only o chooses, so c ∈ F_k. Every u ∈ R_k has honest
  cycle node c (a revisit of a route vertex would return the honest play to o). An o-free cycle C ⊆ R_k of the new graph is its own honest
  play at k+1 (forced Odd vertices only), so its top t gets λ_{Ξ,k+1}(t) = t ≠ c: the phase ends. SIGNED.
  - DATA: the loop alternative of ACT (ii) occurred in 88 random transitions inside a phase, ALL without H1 at k, so LOOP's hypothesis is
    needed. With H1: 0.
- NOFL-E: with Ξ_k = W_k the gate edge is W-improving. z ∈ F_k's W-play avoids y (else it would reach o through y). y is on no W-cycle
  (its play reaches o, and o's W-play does not return to o by H2, so the final W-cycle avoids y). (VAL), (F-pre), Step (K). SIGNED.
  Corollary: ACT (ii) without the loop alternative (LOOP, H1) needs an R_k → F_k switch, which NOFL-E forbids. SIGNED.
- GAP: the left inequality is the gate. If Ξ_k(z) ▷ W_k(σ_k y), then W_k(z) = Ξ_k(z) (z ∈ F_k) gives a W-improving edge, and NOFL-E's
  argument (H2 only) applies. The π′-form is Lemma G (b) at σ_k y ∈ R̄_k under (h). SIGNED. DATA: 523 switched R_k → F_k edges at
  fallbacks with (h), 0 violations.
- WM: inside a phase, a non-S4c transition has Iσ_k ≠ ∅ (otherwise τ would change), so σ_{k+1} is S4a's arena optimum against τ_k
  (R18 (d) Lemma S (c), S4a steps only). σ_k is in the arena, with valuation W_k, so W_{k+1} ⊵ W_k. This is box 21 Lemma W, arena half.
  SIGNED. DATA: 4,000 non-fallback transitions inside phases, 0 W-decreases.

## 5. Data (DATA, not proof): docs/referee/scratch/z_probe.py (n5x.step read-only)
Named instances: experiments/si/xing/instances/*.pg (nofe_cyc_n8 with its .start; zcl_*), experiments/si/orlens/instances/*.pg,
experiments/red/xing/instances/*.pg, experiments/new/box28/instances/*.pg, fts_best16, theta_tp32, returns_rt48, returns_ph64. Random:
o-cyclic 𝒞^1O, 4,000 seed 3101 and 4,000 seed 3102 --randstart, n 6-16 (6,843 accepted runs).
| check | count | failures |
|---|---|---|
| ACT (i) / (ii) | 1,126 / 860 (88 loop-alternative cases, all with ¬H1 at k) | 0 / 0 |
| LOOP (H1 at k) | every ACT (ii) case with H1 | 0 |
| NOFE (strong) | 17 | 0 |
| NOFL-E | every fallback with Ξ = W and H2 | 0 |
| GAP | 523 | 0 |
| WM | 4,000 | 0 |
| LV′ | 596 phases (max X 78, max Z 22) | 0 |

## 6. Gaps (for §C)
| id | item | kind | status |
|---|---|---|---|
| Z-1 | LV′: runs must be broken by '±' crossings | wording | CLOSED by the reading in §1 (the proof's count fits it) |
| Z-2 | NOFE also follows from R21 (c) FBL-N (ii) | remark | — |
| Z-3 | NOFE: "σ_k y ∈ F_k by (F0)" is a state-k fact | wording | CLOSED |
OPEN, untouched: (Z), (C), G-N5-TIME. TARGET.md diff: statements about the candidate N5 on 𝒞^1O, none about general parity games.

## Data correction (Lead 20:4xZ / 20:5xZ; written 20:45Z by date -u)
- experiments/si/orlens/instances/s_rt32_final.pg (sha1 93ba6aa3) is NOT in 𝒞^1O: it has 2 Odd choice vertices (14, 28). My §5 named set
  included it via the si/orlens glob, and z_probe.py took the first Odd choice vertex (common.odd_choice), so its rows are out of class.
- Corrected §5 counts without it (its row was ACT (ii) 5, GAP 12, WM 43, 1 LV phase with X = 5, Z = 0):
  ACT (i) 1,126 / (ii) 855; NOFE 17; GAP 511; WM 3,957; LV′ 595 phases (max X 78, max Z 22, unchanged). 0 failures, as before.
- No verdict changes: data is not proof. Every probe in docs/referee/scratch/ (re_, xa_, x_, nh_, z_probe.py) now asserts exactly one Odd
  choice vertex before running (re_probe.py only in its 𝒞^1O mode).
- Class check of my earlier reports: every named file in R-N5-RE, R-N5-XA, R-N5-X and R-N5-NH has exactly one Odd choice vertex. I scanned
  each glob I used. From box21 I used only fts_best16; from red/n5inj only theta_tp32, theta_thf16, returns_rt48 and returns_ph64. The
  out-of-class files there (fts_best24/39, fts_g29/43, fts_ph16; bribe_cex_n15, elimn_cex_n48, frz32/40, phase2_pk32/48, returns_rt32/64,
  wide_h16) were not in my runs. No correction is needed for R21/R22 from my side.

## §C. Comparison with REFEREE-2 (R2-N5-Z.md, referee-2 1a5854b; read after my report was pushed at c818ef2c). Written from 20:55Z by date -u. (Opus 5.5, D15)
### C1. Disagreements: none
- Every statement is signed in both reports. Z-1 = N-Z-1, the same finding with the same repair: a '±' crossing breaks a run, the per-run
  monotonicity step fails otherwise, and the inequality stands.
- N-Z-2 = the class issue the Lead raised: both referees found s_rt32_final out of class independently. My data appendix (555cbeba) removes
  it from my counts. REFEREE-2's checker refuses non-𝒞^1O games, as mine now does.
- WM, one wording detail: REFEREE-2 covers "Iσ_k = ∅ inside a phase: S4a returns σ_k and W is unchanged". Inside a phase that case does not
  occur as a transition: with Iσ_k = ∅ an N5 iteration must change τ (S4b or Odd's fallback), which ends the phase. Both readings give WM.
- GAP: REFEREE-2 notes that the left inequality and Step (K) use only H2; (h) is needed only for the π′-form. I agree (my §4 says "H2 only"
  for NOFL-E's argument).
### C2. Z-2 (NOFE as a one-line corollary of R21 (c) FBL-N (ii))
REFEREE-2 did not discuss it. Its data agrees: all 21 of its switched F → R̄ fallback edges have the tail on o's W-play AND as a W-cycle node,
which is exactly the stronger statement FBL-N (ii) gives (λ_W(y) = y, λ_W(z) = y, z ∈ R̄ ⇒ y is o's W-cycle node). It is a remark: the packet's
own proof is valid and independent. The lane may cite FBL-N (ii) as an alternative. Z-3 (the (F0) citation) is also mine alone; wording.
### C3. Joint gap map
| REFEREE | REFEREE-2 | status |
|---|---|---|
| Z-1 | N-Z-1 | wording; CLOSED by the adjacent / breaking reading |
| data appendix (555cbeba) | N-Z-2 | s_rt32_final out of 𝒞^1O; removed from both referees' data; the lane relabels it |
| Z-2 | — (data consistent) | remark: NOFE follows from FBL-N (ii), with the cycle-node strengthening |
| Z-3 | — | wording |
Final verdicts unchanged: all SIGNED (LV′ WITH GAP Z-1, closed). (Z), (C) and G-N5-TIME stay OPEN.
§C ended 20:55Z by date -u.
