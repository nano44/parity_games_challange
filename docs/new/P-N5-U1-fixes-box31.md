# P-N5-U1 fixes (box 31): the referees' repairs, written out
L-NEW successor 11 (Opus 5.5, D15/D18). Lead request 21:3xZ. Written 2026-10-24 21:35Z onward (date -u).
- Object: packet docs/new/P-N5-U1-box31.md, frozen at l-new d8d6e1d0, sha1 eb90788d2949050f316ed983fa56c34d7a1dd9c7 (re-checked: the
  file is unchanged). The packet is NOT edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-U1.md (claude/referee 257fa4c), §1-§7. No NOT SIGNED, no counterexample.
  - REFEREE-2: pending (its successor is reviewing independently). Its items will be added in a new section.
- Rule: this file writes down the referees' repairs. A line of my own is marked "L-NEW".
- Scope unchanged: lemmas about the candidate N5 (SPEC tie-breaks) on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a
  step-4 pass. G-N5-TIME stays OPEN. NFB-O, the U2/U3 re-routings and (X) stay OPEN.

## Summary (REFEREE, R-N5-U1 verdict table)
| packet item | REFEREE | repair below |
| --- | --- | --- |
| §4 Theorem U1 (with the κ_w-freeze and the P3-1 transfer) | SIGNED | — (inherits C-1, closed) |
| §5 Lemma WC | SIGNED | — |
| §3 Lemma CASC | SIGNED WITH GAPS (C-1 closed; C-2, C-3 wording) | §3, §4 |
| §2 Lemma TB | SIGNED WITH GAPS (TB-1 closed; TB-2 wording) | §2 |
| §1 Lemma R | SIGNED WITH GAPS (R-1 restated, closed; R-2 citation) | §1 |
| §6 reduction | correct as a READING (its unsigned inputs are named) | — |
| §7 / §8 data | two DATA notes (D-1, D-2) | §5 |

## 1. Lemma R
### 1.1 R-1: restate in the fully optimal form (CLOSED by restating)
- The packet's literal hypothesis, "y is optimal for the optimiser at x in the cycle-node and path-set components", is FALSE as a
  sufficient condition in the case x = u.
  - REFEREE's instance: vertex 0 = c (Even, Ω 1, self-loop); 1 = u (Odd, the optimiser, Ω 2, edges to 0 and 2); 2 = y (Even, Ω 0,
    only edge to 1).
  - Engine.evaluate gives val[u] = (c, {u}, 1) and val[y] = (c, {u}, 2), so u ⊕ val[y] = (c, {u}, 3): the same (c, P).
  - Yet u → y is deleted: the restricted graph after the loop is {0: [0], 1: [0], 2: [1]}.
  - DATA (REFEREE, 20,000 random games, seed 61): 4,074 deleted edges with (c, P) equal to x's. In every one, y's optimal play
    passes x and x is above c.
- Replacement statement:
  "Let x ∈ R_c, and let y ∈ R_c be a successor of x that is FULLY optimal for the optimiser at x: W*(y) ⊕ x = W*(x) in all three
  components (cycle node, path set, length). Then the edge x → y survives the restriction."
  The "Hence" sentence of the packet's §1 is unchanged. It already speaks of fully optimal edges, and it is the only form the packet
  uses: TB step 2, with TB-1 below, delivers full equality.
- Proof, step 2, case "Even likes u, x = u": the play through y ∉ M returns to u before reaching c. Either that loop's cycle is
  Even's (top ⪰ u, even), which is worse for the optimiser, or y's optimal play passes u on its way to c. In the second case
  ℓ*(y) ≥ 1 + ℓ*(u), so y ⊕ u has length ℓ*(y) + 1 ≠ ℓ*(u), and y is not fully optimal. Either way the deleted edge is not fully optimal.
- DATA (REFEREE): 57,885 fully optimal edges, 0 deleted. At all 54,995 optimiser vertices the survivors of optimal length are
  exactly the fully optimal edges, and the engine's choice is always fully optimal.
### 1.2 R-2: citation (CLOSED)
- VJ00 = J. Vöge, M. Jurdziński, BRICS RS-00-48 (Dec 2000), sha256 485a12de…, §6 "Efficient implementation". Opened by REFEREE
  2026-10-24 21:18Z. L-NEW opened the same pdf in box 4 (N5-ssi-global.md, "CORRECTION (box 4)").
- Prop. 6.1 clause 1 states only that the restricted graph G(r) contains ONE shortest path from every vertex. Lemma R ("every fully
  optimal edge survives") is stronger. It is NOT in VJ00; it is a strengthening proved in the packet.
- What the proof does take from VJ00 is the membership / path-set correspondence of the restriction steps:
  - for r ∈ R+ (Even likes r): r ∉ Σ(v) iff some path avoids r, (15) and its Prop. 6.1 analogue;
  - for r ∈ R− (Odd likes r): r ∈ Σ(v) iff v reaches r, (22).
- Cite "VJ00 §6 (15), (22), Prop. 6.1" for it. The correspondence with si.py l.135-150 is REFEREE's §4.1.
- With the packet's step-1 invariant and the induction "every fully optimal edge has survived so far" (so the optimal plays lie in
  G(r)), the case analysis of step 2 is correct (REFEREE §4.1).

## 2. Lemma TB
### 2.1 TB-1: step 2 with set-valued ⊕ (CLOSED; REFEREE §3.2)
The packet's step 2 chain is W*(x) ⊵ W*(σ_k x) ⊕ x ⊵ W_k(σ_k x) ⊕ x = W_k(x) = W*(x). Write y := σ_k(x).
- (a) First inequality, W*(x) ⊵ W*(y) ⊕ x. This is VJ00 (7) for the optimal valuation when x is not on y's optimal play. If y's
  optimal play passes x, the loop x → y → … → x has a top t′.
  - If t′ is even and above c, or t′ is below c with c odd, Even would have a better cycle at x than c, contradicting optimality.
  - Otherwise the formal triple y ⊕ x is worse than W*(x): an odd t′ enters P, or the length is longer at an even c.
  So the inequality holds in every case.
- (b) Second inequality, W*(y) ⊕ x ⊵ W_k(y) ⊕ x. This needs monotonicity of · ⊕ x, which can fail only if x ∈ P*(y) \ P_k(y).
  (x ∉ P_k(y) holds: otherwise x lies on its own W_k-cycle above its cycle node.)
  - In that case W*(y) = seg ⊕ W*(x), with W*(x) = W_k(x) = W_k(y) ⊕ x.
  - W*(y) ⊵ W_k(y) then forces the top of seg ∪ {x} to be even. That is an even cycle through x above c, against W*(x) = W_k(x).
  So the case does not occur.
- With (a) and (b) the sandwich gives the full triple equality W*(σ_k x) ⊕ x = W*(x), i.e. σ_k(x) is a FULLY optimal edge of H_k at
  x. Lemma R (§1.1 form) then applies.
### 2.2 TB-2: wording
- In TB-even's hypothesis, replace "W′ = W_k at every vertex of v's σ_k-play from v to c" by "W′ = W_k at every vertex of v's
  σ_k-play before c".
- Step 2 is false at c itself (W(c) ≠ W(σ c) ⊕ c), and the proof uses only the vertices before c.
### 2.3 Match with SPEC (REFEREE §3.1, no repair)
The tie-breaks TB uses are exactly SPEC S1 (iv) + FIX 4 as coded in si.py: longest mode l.154-168, BFS mode l.172-180, with list
orders from l.33 / l.87-90, kept by restrict (l.128-134). The cycle node's own choice (S1 (v), FIX 2) is excluded by "v not its own
cycle node".

## 3. Lemma CASC: C-1 (CLOSED; REFEREE §2.2)
- Gap: CASC step 1 says "TB applies". But TB-even's hypothesis covers v's whole old play before c_w. Under H2 that play runs through
  o's W-continuation o → τ(o) → … → c_w inside F, where "W-flat" (a condition on R) says nothing.
- Closure: CASC uses only TB's CHOICE RULE, which needs no hypothesis on the old play:
  "At an S4a step, every optimiser vertex v that is not its own W′-cycle node gets σ_{k+1}(v) = the key-minimum over the fully
  optimal arena edges with respect to W′ (Lemma R in the §1.1 form, plus the longest / BFS selection: TB steps 3-5 without the old
  play)."
  - With W′ = W on R, the fully optimal R-candidates of v are its tied R-candidates.
  - The keys are σ_{k+1}-plays. In the even mode, the part of the key from c_w to o is common to all of R (it may change at F-ties
    under H2, but identically for every candidate), so comparisons inside R depend only on σ_{k+1} along π_z.
  - That is all step 3 uses.
- Wording repair: in CASC step 1, replace "so TB applies with c = c_w" by "so TB's choice rule (TB steps 3-5 and Lemma R) applies
  with c = c_w".
- Theorem U1 step 3 inherits this repair; nothing else changes there.
- DATA (REFEREE): the choice rule (TBc) holds in 381,241 checks with 0 failures. C1 (W unchanged on o's W-continuation at W-flat
  transitions of pieces under H2) has 0 failures. CASC's margin climbs from the three pinned instances reach best margin −2.

## 4. CASC wording: C-2, C-3
- C-2 (step 2). "Ξ_k(z) … depends only on σ_k along z's route, i.e. on levels < ℓ(z)" should read "on z and the vertices below it
  on its route, i.e. on levels ≤ ℓ(z)". The same applies to the key and σ_{k+1}. Step 3 uses only candidates z of level ℓ(v) − 1,
  for which "levels ≤ ℓ(v) − 1" is what is needed and what holds.
- C-3 (Setting, and Theorem U1). "Transitions of J" means transitions k → k+1 with both k and k+1 in J. J's exit transition can be a
  crossing, where v's choice may leave R. It is counted elsewhere: in (X), or as a θ- or w-change.

## 5. Data notes
### 5.1 D-1: the |R| convention
- With R as defined (P-N5-NH §0: o ∈ R), |R| at the three U1 pieces is 29 on u1t_cex_n32, 29 on u1t_cex2_n32, and 25 on L-RED's
  u1t_own6_n32. The packet's §7 quotes 28 for u1t_cex_n32 and for u1t_cex2_n32, i.e. |R \ {o}|. The same holds for the Lead's and
  R22's quotations.
- L-NEW: the cause is the lane's helper reach_o (experiments/new/box28/fbre.py l.9-15), which returns R \ {o}. Every "|R|" printed
  by box29/box31 scripts (u1vertex, runinfo, casccheck's U1 bound, p3long) is |R \ {o}| = |R| − 1.
- L-NEW: the bounds those scripts check are increasing in |R|, so checking with |R| − 1 is stricter. The 0-violation results stand.
- L-NEW: also in N5-U1T-box31.md §1 and §9, "|R| = 28", "|R| = 11" (p3long_n14) and the P3′ bound 101 are in the |R \ {o}|
  convention. With o counted: |R| = 12, and the bound |R| + (|R| − 2)(|R| − 1) = 122. The freeze index 9 against "≤ |R| − 1"
  becomes 9 ≤ 11; with the lane's count it was 9 ≤ 10.
- Convention from here on: |R| counts o, as in the packet's definitions. Script outputs say "|R minus o|" (runinfo.py) or "|R| (o counted)" (p3long.py); casccheck.py's U1 bound uses |R| with o.
- No bound in the packet is affected (all are loose by orders of magnitude).
### 5.2 D-2: σ(10) on u1t_cex_n32
- The packet's §7 says "vertex 10, with σ(10) fixed". In fact σ(10) switches once, 12 → 29 at transition 0, and is fixed from
  transition 1 on.
- From transition 1 on, its Ξ-changes are propagation only (REFEREE §7, confirmed). The refutation of U1-T is unaffected.

## 6. Labels after this layer (REFEREE's signature, D18/L40)
Once REFEREE-2 signs, TB, CASC, Lemma R (§1.1 form), Theorem U1 and Lemma WC would be PROVED (L-NEW; REFEREE, REFEREE-2), on 𝒞^1O,
given f (Theorem U1, WC). Until then they are PROVED (L-NEW), signed by REFEREE.
