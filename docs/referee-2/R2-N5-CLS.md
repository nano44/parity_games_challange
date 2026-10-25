# R2-N5-CLS: second-referee check of packet P-N5-CLS (L-SI box 8: gates into F, frozen values, fallback levels across a scope run). REFEREE-2 (successor 6), 2026-10-25 02:43Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-CLS (Lead 02:40Z), pinned at trunk claude/vibrant-johnson-nxvvxo 486107a (merged into my branch
as e44385dc). Object: docs/si/P-N5-CLS-box8.md, sha1 5bbfd872383d9b2c2d3caaf902b174d0aa54e4ae (181 lines; checked at the pin and on my tree).
Background read: P-N5-FB (R25: (T), OFF, NOINF, FB step (2), J1), P-N5-XA (R20 FBL) with my lane's R2-N5-XA §2 (the u* ≠ none strong
gate form), P-N5-RE §1 ((h)), RESULTS R19 (a)/(b), R21 (a), R23 (f)/(g).
Independence: I have not read docs/referee/ for this packet (no CLS report is on my tree). I did not run or import cls2.py, rfinv.py,
clscope.py or any REFEREE probe. Lane instances are inputs only.
Tools (docs/referee-2/R2-N5-CLS/, own code on R2-N5-LP/lp_check.py and R2-N5-FB/fb_check.py): cls_check.py (every statement, with NL
tested at EVERY admissible L and CLS1's (A_j) chain asserted step by step), cls_climb.py, run_all.sh, totals.py, logs/, climb/. Every
𝒞^1O probe asserts exactly one Odd vertex with out-degree > 1.
Labels (D18 / L40): PROVED (L-SI succ. 3) is the packet's label. §7 is not to sign. Nothing here is a running-time bound, a TARGET.md
claim or a step-4 pass. G-N5-TIME stays OPEN.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 (C5), (C6), (C7) | SIGN | — |
| §1 Fact R | SIGN | — |
| §1 Lemma CLU | SIGN | — |
| §2 TRANSFER (every game) | SIGN | — |
| §3 OFFGATE (𝒞^1O) | SIGN | N-CLS-1: OFF's R̄ is honest reachability; the packet's (σ, τ)-R̄ is the same set (§0's R23 remark) |
| §4 CN (every game, in a phase) | SIGN | — |
| §5 Lemma NL (𝒞^1O) | SIGN | — (minimal-counterexample induction checked step by step, §5) |
| §6 Theorem CLS1 + Corollary (𝒞^1O) | SIGN WITH GAPS | G-CLS-1 (citation, CLOSED): FBL as signed in R20 (b) is a statement about a transition with both ends in a throttled stretch; "a single fallback state is a stretch of length 1" does not satisfy it. The strong gate form for u* ≠ none (R2-N5-XA §2, G-XA-1 repair) uses state k1 alone, so it applies. N-CLS-2: (α)/(β) is exhaustive because under (h), θ = w ⟺ EQ (Lemma G) |
| §7 | not signed (as briefed) | OG′ refutation reproduced (x31_re24, 1 → 2) |
No statement is NOT SIGNED. No counterexample.

## 1. (C5)-(C7), Fact R, CLU: SIGN
- (C5): with L = lev(a, c), lev(a, b) > L makes COARSE_L(b) ≠ COARSE_L(a) = COARSE_L(c). (C1) with a ◁ b gives COARSE_L(c) ◁_L COARSE_L(b);
  b ⊴ c gives ⊴_L the other way; (C3). L = ⊥ and L = ∞ are trivial. ✓
- (C6): ultrametric, by (C2). ✓
- (C7): with equal cycle nodes, the same vertices join both path sets and both lengths grow by |π|, so the top of the difference and the
  verdict are unchanged. The length verdict depends only on the cycle node's parity. With different cycle nodes, lev stays ∞ and the
  verdict is the cycle-node comparison. ✓
- Mechanical: 21,060 random triples from run valuations (C7 with a random disjoint prefix), 0 failures.
- Fact R: θ_k ⊴ θ_{k+1} ⊴ w_{k+1} = w_k (R15 (a), XW at k+1, scope run). Then (C5), (C6). ✓
  - Holds at the run's last state too: r_{k+1} ≤ r_k < ∞ needs no (h) at k+1. 8,158 scope transitions, 0 rises.
- CLU: GAP (R23 (f)) + Lemma G (b) at k + (C5) + (C7). ✓
  - (C7)'s disjointness: π′ ⊆ R_k. P(θ) ∖ {o} and P(w) ∖ {o} lie on o's honest / W-play after o, which never returns to o (H1, H2), so
    those vertices are in F. The common cycle node is on that tail, hence in F.
  - 1,948 switched R → F edges at in-scope fallbacks, 0 above r.

## 2. TRANSFER: SIGN
- The chain COARSE_L(Ξ_k z) = COARSE_L(Ξ_{k+1} z) ▷_L COARSE_L(Ξ_{k+1} u) ⊵_L COARSE_L(Ξ_k u) ⊵_L COARSE_L(Ξ_k σ_k y) is right. ▷_L because the gate
  at k+1 is strict and of level > L ((C1) + (C2)); the two ⊵_L by R15 (a), (d) and (C1).
- So the COARSE_L values at k differ, and lev > L by (C2). The direction is ▷ by (C1)'s contrapositive, and z ≠ σ_k(y). ✓
- It uses only R15 and (C1)-(C3). It holds on every game, which matches the label.
- Mechanical: every in-phase transition, every L ∈ {⊥, −1, …, n − 1}, every z with COARSE_L frozen; 442,864 checks (library) + random
  general and 𝒞^1O games; 0 failures.

## 3. OFFGATE: SIGN (N-CLS-1)
- OFF (R25 §5) is stated for v ∉ R̄_{k+1} with "v's H_{k+1}-play avoids o", i.e. honest reachability.
  - N-CLS-1: the packet's R̄ uses (σ, τ)-plays. The two sets coincide because both plays agree up to the first visit of o (§0, R23
    remark). Worth one clause in the text.
- TRANSFER with L = M_k < ∞. M_k = ⊥ cannot occur at an in-phase transition (no gate and τ fixed would change nothing). ✓
- Mechanical: 26,464 gate checks, 0 failures.
- The Remark is right: x31_re24 1 → 2 has gate (4, 8) of level 22 into F at state 2, while M_1 = 23 (§7).

## 4. CN: SIGN
- y is its own cycle node at k and at k+1 (phase). Its H_{k+1}-play is a cycle topped by y through z, so P(Ξ_{k+1} z) = ∅.
- σ_k(y) lies on its H_k-cycle, so P(Ξ_k σ_k y) = ∅.
- Ξ_k(z) ⊴ Ξ_{k+1}(z) with the same cycle node y, and Ξ_k(z) ▷ Ξ_k(σ_k y) (R15 (d): a switch is along a gate). These force P(Ξ_k z) = ∅,
  since the signed weight is injective. So the level is −1. ✓
- Mechanical: 48 library + 711 random own-cycle-node switches (general and 𝒞^1O), all of level −1.

## 5. Lemma NL: SIGN (the Lead's "hardest" item 1)
- (K*): Lemma G (b) at j (needs (h) at j) and (C7) give lev(Ξ_j q, W_j q) = r_j > L with Ξ_j q ◁ W_j q, so COARSE_L(Ξ_j q) ◁_L COARSE_L(W_j q).
  q ∉ R̄_{j+1} gives W_{j+1}(q) = Ξ_{j+1}(q) (G (a)). WM (S4a, in phase) gives W_{j+1}(q) ⊵ W_j(q). With (i) at q this gives the reverse
  ⊵_L. ✓
  - L = ⊥ is included: r_j > ⊥ means θ_j ≠ w_j, and XW makes it strict.
- (i), the minimal-counterexample induction. I checked each step.
  - Measure: steps of v's H_{j+1}-play to its cycle node c_v = λ_{j+1}(v). It is finite, since c_v tops the play's cycle.
  - The play avoids o. It agrees with the (σ_{j+1}, τ)-play up to o, and v ∉ R̄_{j+1}. So all Odd vertices on it are forced.
  - v = c_v is excluded: (P3) at both states, and λ_j(v) = v by the phase.
  - p_1 ∉ R̄_{j+1} (it lies on v's play) and is one step nearer, so (i) holds at p_1 by minimality. This includes p_1 = c_v.
  - (E) at v (unchanged edge, a forced Odd vertex, or a switch along a gate of level ≤ L). Then COARSE_L(Ξ_{j+1} v) = f_v(COARSE_L Ξ_{j+1} p_1) =
    f_v(COARSE_L Ξ_j p_1) = f_v(COARSE_L Ξ_j σ_j v) = COARSE_L(Ξ_j v).
    - (P2) holds in set form at j+1 and at j: v is not its own cycle node at either state. At j, if σ_j v's path passed v, v would lie on
      a cycle under c_v and have rank < rank c_v, so v ∉ P anyway.
    - (C4) gives each equality. This is R25's "(T) (iii)" step. ✓
  - Otherwise v is Even and switched along a gate (v, q) at j of level > L (R15 (d)). (A_j) gives q ∉ F_j. And q ∉ R̄_{j+1} with q ≠ o,
    so q ∈ R_j ∖ R̄_{j+1} with (i) at q, against (K*). ✓
- (ii): any q ∈ R_j ∖ R̄_{j+1} satisfies (i) (it is ∉ R̄_{j+1}), so (K*) excludes it. ✓
- (iii): (ii) gives R̄_j ⊆ R̄_{j+1}, so F_{j+1} ⊆ F_j. (i) freezes COARSE_L at z ∈ F_{j+1}. TRANSFER carries a gate of level > L back to j,
  into F_j, against (A_j). ✓
- Mechanical. At every in-phase S4a transition with (h) at j I tested EVERY L with r_j > L for which (A_j) holds, not just the L of
  CLS1's chain.
  - Library: 40,516 (j, L) checks at 3,198 transitions (2,900 with R_j ≠ ∅). Climbs: 20,283 more. 0 failures of (i), (ii), (iii).
  - The hypothesis has bite. At S4a (h)-transitions where no admissible L exists (every L < r_j violates (A_j)), leaves happen:
    1,298 in the library and 14,775 in the climbs.

## 6. Theorem CLS1 and Corollary: SIGN WITH GAPS (G-CLS-1 closed; the Lead's "hardest" item 2)
- Induction and (α)/(β).
  - Only consecutive fallbacks k0 < k1 of S are compared; the induction supplies min = M_{k0}.
  - N-CLS-2: under (h), θ = w ⟺ EQ (Lemma G (a), (b)). So every in-scope state is THR or EQ, and (β) (r ≤ −1) contradicts Fact R. ✓
  - Data: no θ = w state that is not EQ (checked at 23 in-scope EQ fallbacks); 0 u* = none fallbacks.
- G-CLS-1 (citation). R20 (b) signs FBL for a transition k → k+1 with k, k+1 in a throttled stretch (θ, w, τ constant, (h) at every
  state). The packet applies it at k1, whose successor k1+1 need have only H2 and w_{k1+1} = w_{k1}. "A single fallback state is a
  stretch of length 1" puts k1+1 outside the stretch, so FBL's statement does not apply literally.
  - What CLS1 uses is the strong gate form at the state k1 alone: no F → R and no R → R gate edge; switched edges are R → F or flat at
    own cycle nodes.
    - That form is my lane's G-XA-1 repair (R2-N5-XA §2), part of R20 (b)'s signed "strong form". It uses only state k1: S4a returned
      σ_{k1}; flatness of W-improving gate edges; Lemma G (c) under (h) for R → R; P(w) = ∅ ⇒ u* = none for F → R.
    - F → F gate edges are W-improving, hence flat (own cycle node tail).
  - So the citation holds. Fixes-file line: cite "R20 (b), strong gate form (R2-N5-XA §2), at the fallback state alone". CLOSED.
- Case r_{k1} ≤ L. FB step (2): M attained by a switched edge. R → F edges are ≤ r ≤ L (CLU); own-cycle-node edges are −1 (CN). L ≥ −1. ✓
- Case r_{k1} > L, the chain.
  - Fact R gives r_j > L on [k0, k1].
  - (A_{k0+1}) by OFFGATE at k0 → k0+1.
  - NL (iii) step by step at the S4a transitions in between ((h) at each j: they are in S; no fallback: k0 is the last).
  - At k1, switched edges into F are gates into F, ≤ L by (A_{k1}). There are none into R̄ but flat ones (strong gate form). ✓
- Mechanical:
  - 760 CLS1 comparisons in the library (82 with r ≤ L, 678 with r > L; 117 strict drops).
  - In case r > L, (A_j) was asserted at all 1,731 intermediate states; the longest chain k1 − k0 was 27.
  - The climbs (FIT=gt) added 22,158 comparisons, 20,544 of them in case r > L.
  - Corollary (non-increasing level sequence per scope run, up to 33 fallbacks in one run): 0 failures.
  - FBL strong form at every in-scope r ≥ 0 fallback: 0 gates into R̄, 0 other switched edges.
  - FB step (2) at every in-scope fallback: 0 failures.

## 7. §7 (not signed) and the phase key
- OG′ FALSE: reproduced with my code on x31_re24 (sha1 49eaf50e), transition 1 → 2 (in phase, S4a):
  - |R| 21 → 1 (R̄_2 = {12, 18}, o = 18);
  - MF_1 = −1, M_1 = 23;
  - at state 2, gate (4, 8) has level 22 with 8 ∈ F_2; at state 1, (8, 14) is a level-22 R → R gate.
  As the packet states.
- (H-EQ), the per-level count and Θ per scope run: OPEN, not tested beyond the counters above.
- Phase key. The packet's phase is R21's (λ_Ξ, λ_U, τ). My default key is the coarser (λ_Ξ, τ), a stronger test; every cited dependency
  uses only λ_Ξ and τ (as in R2-N5-OE §4). I also ran the fine key (c1o seed 974, and jcl_zcl_cu_n48): 0 failures.

## 8. Data (DATA, not proof)
| batch | runs | key counts | violations |
| --- | --- | --- | --- |
| library ∪ named.txt ∪ coarse/instances ∪ j7 (234 distinct files, 3 starts each) | 702 | in-phase transitions 10,257; scope runs 568 (8,158 transitions); in-scope fallbacks 913 (890 THR u* ≠ none, 23 EQ, 0 u* = none); CLS1 760 (r > L 678); NL 40,516; TRANSFER 442,864; OFFGATE 26,464; CLU 1,948 | 0 |
| random general n 4-12 (seed 971) | 3,000 | TRANSFER, CN | 0 |
| random 𝒞^1O n 6-16 / 16-28 (seeds 972, 973), fine key (974) | 9,000 | 204 in-scope fallbacks | 0 |
| climbs (FIT=gt from ccl_fb2_n32 and fb32_inr2_final; FIT=nl from x31_re24 and df_cex) | 12,400 | CLS1 22,158 (r > L 20,544); NL 20,283 | 0 |
- The lane's set is 53 + 12 files. My 234 files include all of them (n ≤ 64). Counts are larger because I use 3 starts.
- Thin spots:
  - CN has only 48 library cases (random adds 711).
  - No u* = none fallback anywhere, so (β) is never exercised; it rests on Fact R.

## Signature
REFEREE-2 (successor 6), Opus 5.5 (D15), 2026-10-25:
- SIGN: (C5)-(C7), Fact R, CLU, TRANSFER, OFFGATE (note N-CLS-1), CN, Lemma NL.
- SIGN WITH GAPS: Theorem CLS1 and its Corollary (G-CLS-1, a citation gap, closed; note N-CLS-2).
After two signatures (D18/L40) these become PROVED (L-SI successor 3; REFEREE-2, and REFEREE if it signs). OPEN: (H-EQ), the per-level
count, θ-changes per scope run, G-N5-TIME.

## §C. Comparison with REFEREE (R-N5-CLS, referee a0b92ec; trunk merged as be255e1d). Written 2026-10-25 02:57Z onward by date -u
Order: my report (ffe10e1b) was pushed before I opened docs/referee/R-N5-CLS.md (Lead 02:55Z). REFEREE did not read mine.
### C.1 Verdicts
| statement | REFEREE | REFEREE-2 | agree? |
| --- | --- | --- | --- |
| (C5)-(C7), Fact R, CLU | SIGNED | SIGN | yes |
| TRANSFER | SIGNED | SIGN | yes |
| OFFGATE | SIGNED WITH GAP CLS-1 (wording) | SIGN, note N-CLS-1 | yes on substance; I noted the same vacuity in §3 ("M_k = ⊥ cannot occur") without filing it |
| CN | SIGNED WITH GAP CLS-2 (wording: Even y) | SIGN | yes; accept CLS-2 |
| NL | SIGNED | SIGN | yes |
| CLS1 | SIGNED WITH GAP CLS-3 (citation, closed) | SIGN WITH GAPS G-CLS-1 (citation, closed) | yes: the same gap |
| Corollary | SIGNED WITH GAP CLS-4 (wording: "evicting" undefined) | SIGN (with CLS1) | yes; accept CLS-4, which I missed |
| §7 OG′ | FALSE, CONFIRMED | reproduced (not signed, as briefed) | yes; same numbers (MF_1 −1, M_1 23, gate (4, 8) level 22, R 21 → 1) |
No disagreement of substance. Neither report has a counterexample.
### C.2 Item by item
- CLS-1 (M_k = ⊥ clause vacuous in a phase; the packet's reason is not the right one): accept.
  - My §3 says the same: no gate and τ fixed would change nothing, so the transition is not in a phase.
- CLS-2 (CN's y must be Even): accept. My checker tests Even y only.
- CLS-3 = G-CLS-1, the same citation gap, both closed. The two closures differ only in what they cite:
  - REFEREE: FBL's proof (R-N5-XA §3) is statewise given that the fallback is Even's.
  - Mine: the strong gate form for u* ≠ none (R2-N5-XA §2, G-XA-1 repair) at the state alone.
  - Both are part of R20 (b)'s signed u* ≠ none form. Its F → R exclusion is the D = ∅ argument (P(w) = ∅ ⇒ u* = none), which needs only
    state k1. The packet's own FBL text excludes F → R by (h) at k+1, which a length-1 stretch does not give (R2-N5-XA G-XA-1 (b)).
  - The fixes-file line should cite the u* ≠ none strong form at the single state (row 3).
- CLS-4 ("evicting fallbacks" undefined in the Corollary): accept. Every in-scope fallback with u* ≠ none is THR, so the clause holds under
  any definition.
- N-CLS-1 (mine only): OFF's R̄ is honest reachability, the packet's is the (σ, τ) one. They are equal because both plays agree up to o.
  REFEREE uses OFF without remark. One clause in the text (row 5).
- N-CLS-2 = REFEREE §1 "state kinds under (h) are exhaustive" (θ = w ⟺ EQ). Same argument, neither files it as a gap. No row needed.
- Data: consistent. REFEREE ran the canonical start with the fine key. I ran 3 starts with the coarse key, plus a fine-key batch.
  - Library in-scope fallbacks: 534 (REFEREE) vs my 913 over 3 starts; both have 0 u* = none.
  - Both have 0 failures. Both say random games are vacuous for CLS1, with the named / library instances carrying the evidence.
  - My climbs add 20,544 case-r > L comparisons; REFEREE has none of that kind.
### C.3 Joint gap map (one fixes-file line per row)
| row | REFEREE | REFEREE-2 | fixes-file line |
| --- | --- | --- | --- |
| 1 | CLS-1 | (§3 remark) | §3 OFFGATE proof: replace "If M_k = ⊥, σ and Ξ are unchanged" by "M_k ≥ −1 at every in-phase transition (no gate ⇒ σ unchanged ⇒ τ changes, which leaves the phase)" |
| 2 | CLS-2 | — (accepted) | §4 CN statement: "If λ_{k+1} = λ_k and an Even y with λ_k(y) = y switches to z …" |
| 3 | CLS-3 | G-CLS-1 | §6 CLS1: "FBL (R20 (b)) in its u* ≠ none strong form, applied at the single state k1: no F → R and no R → R gate edge; the proof uses only state k1 (fallback Even's, S4a returned σ_{k1}, Lemma G (c), P(w) = ∅ ⇒ u* = none; R-N5-XA §3, R2-N5-XA §2)" |
| 4 | CLS-4 | — (accepted) | §6 Corollary: drop "evicting", or define it; every in-scope fallback with u* ≠ none is THR |
| 5 | — | N-CLS-1 | §3 OFFGATE: "OFF's R̄ (honest reachability) is the packet's R̄, since honest and (σ, τ)-plays agree up to o (§0)" |
### C.4 Labels after two signatures (D18/L40)
PROVED (L-SI successor 3; REFEREE and REFEREE-2, Opus 5.5, D15), pending CHECKER:
- on every game: (C5)-(C7), TRANSFER, and CN (inside a phase);
- on 𝒞^1O: Fact R, CLU, OFFGATE, NL, Theorem CLS1 and its Corollary (rows 1-5 as wording / citation).
FALSE: OG′ (x31_re24). OPEN: (H-EQ), the per-level count, θ-changes per scope run, G-N5-TIME. Not a TARGET.md claim; not a step-4 pass.
