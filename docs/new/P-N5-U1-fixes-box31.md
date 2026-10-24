# P-N5-U1 fixes (box 31): the referees' repairs, written out
L-NEW successor 11 (Opus 5.5, D15/D18). Lead request 21:3xZ. Written 2026-10-24 21:35Z onward (date -u).
- Object: packet docs/new/P-N5-U1-box31.md, frozen at l-new d8d6e1d0, sha1 eb90788d2949050f316ed983fa56c34d7a1dd9c7 (re-checked: the
  file is unchanged). The packet is NOT edited; this file is its correction layer.
- Sources:
  - REFEREE: docs/referee/R-N5-U1.md (claude/referee 257fa4c), §1-§7. No NOT SIGNED, no counterexample.
  - REFEREE-2: docs/referee-2/R2-N5-U1.md (claude/referee-2 28ddf6f), relayed by the Lead 21:5xZ; no NOT SIGNED. Its items: §7.
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

## 7. REFEREE-2's items (R2-N5-U1)
### 7.1 G-TB-1 (TB step 2; CLOSED): REFEREE-2's (F1)-only proof, next to REFEREE's TB-1 (§2.1)
Same chain W*(x) ⊵ W*(σ_k x) ⊕ x ⊵ W_k(σ_k x) ⊕ x = W_k(x) = W*(x), with y := σ_k(x).
- The second and third relations hold: (F1) gives W* ⊵ W_k, ⊕ is monotone, and (V1) at k holds because x is not its own cycle node.
- The first relation needs an argument only when x lies on y's W*-play; otherwise σ*[x → y] is an arena strategy with value
  W*(y) ⊕ x at x, and (F1) applies. Let c be x's cycle node, and assume W*(x) = W_k(x).
- (a) x on y's W*-path BEFORE c. Let Z := x → y → … → x, with top m. Z avoids c and x's W*-path after x.
  - m ≻ c, m even: σ*[x → y] gives x the cycle node m, which beats c for Even, against (F1) at x.
  - m ≻ c, m odd: since W_k(x) = W*(x), W_k(y) = (c, P* \ {x}, ℓ − 1). So W*(y).P \ W_k(y).P = Z ∩ (above c), whose top m is odd.
    That gives W*(y) ◁ W_k(y), against (F1) at y.
  - m ≺ c, c odd: cycle node m beats c for Even, against (F1) at x.
  - m ≺ c, c even: W*(y) ⊕ x has W*(x)'s path set and a strictly larger length, so W*(y) ⊕ x ◁ W*(x), against the relation already shown.
  So case (a) never occurs.
- (b) x only on the cycle part of y's W*-play (after c). Let m := top of W*(y).P.
  - If W*(y).P = ∅, σ*[x → y] realises W*(y) ⊕ x at x, and (F1) gives ⊴.
  - Otherwise the new cycle has top m ≻ c. If m is even, (F1) at x is contradicted. If m is odd, W*(y) ⊕ x ◁ W*(x), because x's
    path to c on the cycle has nothing above c. That contradicts the relation shown, so this sub-case does not occur.
- So equality holds in every case that occurs, and σ_k(x) is fully optimal in H_k at x.
- DATA (REFEREE-2): 277,668 step-2 instances in the batch. Case (a): 0. Cycle-only case: 27,336, equality every time. Climbs:
  5,879,798 more, equality every time.
- L-NEW: REFEREE's TB-1 and REFEREE-2's G-TB-1 close the same step by different case splits (REFEREE on the loop top and on the
  monotonicity of · ⊕ x; REFEREE-2 on where x sits on y's play). Either suffices; both are recorded.
### 7.2 G-R-1 (Lemma R step 1; CLOSED, wording)
- The invariant "every surviving edge joins two vertices with the same membership in each processed set M_u" is false for the edges
  out of u itself.
  - Even likes u: u ∉ M, yet u keeps its edges INTO M.
  - Odd likes u: u ∈ M, and its edges are not restricted.
- Correct invariant: for a surviving edge x → y and every processed u ≠ x, [x ∈ M_u] = [y ∈ M_u].
- That is what step 2 uses. When x = u′ is processed, x's own bit is on both sides, since the value via y is W*(y) ⊕ x. So for every u′
  processed before u the two path sets agree at u′, and at u they differ against the optimiser.
### 7.3 G-R-2 (= REFEREE's R-1; CLOSED by the §1.1 restatement)
- The "(cycle node, path set)" reading with the formal ⊕ is FALSE as a sufficient condition for survival. REFEREE-2's instance:
  tb_general.py seed 532, game #13, iteration 1, a dual-arena evaluation at cycle node 19. Edge 11 → 13 is deleted at step u = 11,
  although W*(13) ⊕ 11 has W*(11)'s cycle node and path set; only the length differs.
- Every self-loop u → u at an Even-liked u above c is another case.
- DATA (REFEREE-2): 8,464 such deleted edges in the batch, all with u = x, 2,117 of them with x ≠ y. Climbs: 110,573 and 84,178.
- The full-equality form (length included) is TRUE: for x = u, every y → c path in the restricted graph passes u, so
  dist[y] ≥ dist[u] + 1 and the lengths differ. That is the §1.1 statement.
- REFEREE-2 also notes that VJ00's text at Prop. 6.1 (p. 25) asserts the stronger "every shortest path survives", but its proof states only
  clause 1 ("We omit considering the other case"). So Lemma R is the packet's own lemma, as in §1.2.
### 7.4 N-U1-1 (Theorem U1 step 2; wording)
- K is the number of post-freeze NON-FALLBACK transitions with a W-change on R. A fallback can change W in either direction and is
  counted separately (the + f).
- With this reading, K ≤ (f + 1)(|R| − 1)(|R| − 2) and the sum are right. Read literally, K could be off by ≤ f; the total is unaffected.
### 7.5 N-U1-3 (§6 reading: EQ-state fallbacks in WC's f_I)
- The gap: WC(I) ≤ (f_I + 1)|R|² counts ALL fallbacks in I. Under ¬H1 ∧ ¬H2, I contains EQ states (TC (iv)), and fallbacks occur
  there (REFEREE-2: 110 in the batch and 20 in the climbs, all with w unchanged). §6 lists only "fallbacks at OTHER states".
- Closure (L-NEW; REFEREE-2's proposed line, written as a proof; label PROVED (L-NEW), unrefereed until the referees check it).
  - Claim: at a fallback transition k → k+1 inside a phase whose state k is EQ, W_{k+1} ⊵ W_k pointwise.
  - Proof:
    1. Inside a phase the fallback is Even's (SPEC S4c; FIX 3: τ_{k+1} = τ). It sets σ_{k+1}(v) to an edge of I_σ at every Even
       v with an improving edge, and leaves the other Even vertices unchanged.
    2. At an EQ state Ξ_k = W_k at every vertex. An edge (v, z) ∈ I_σ satisfies Ξ_k(z) ▷ Ξ_k(σ_k v), so W_k(z) ▷ W_k(σ_k v). It is
       an improving edge of σ_k in the game G_τ (Odd fixed to τ), whose valuation of σ is exactly W (S1 applied to G_τ, where
       Odd's counterstrategy is forced).
    3. σ_{k+1} is σ_k with a set of improving switches of G_τ applied, at most one per vertex. By the strategy-improvement lemma for
       Vöge-Jurdziński valuations (VJ00, the improvement theorem of §4-5; the same lemma under R15 (a)), applied to the game G_τ, the
       new valuation dominates the old one pointwise: W_{k+1} ⊵ W_k.
  - So an EQ-state fallback never lowers W, and in particular never lowers w. In Lemma WC's count it does not end a monotone stretch.
    It is still a transition, and it may change w, at most once: it is then counted as one of the ≤ |R|² − 1 monotone changes.
  - DATA (L-NEW, experiments/new/box31/eqfb.py): at every Even fallback from an EQ state, W against the old τ never drops at any
    vertex. Random games n 4-14 (4,000, seed 71): 110 such fallbacks, 0 violations. Random o-cyclic 𝒞^1O n 6-16 (4,000, seed 72):
    139, 0 violations.
  - Restated §6 input: WC(I) ≤ (f^O_I + 1)|R|² + f^O_I, where f^O_I counts the fallbacks at OTHER states of I. So §6's list ("(X),
    NFB-O, U2/U3") stands as written.
  - L-NEW, caveat for the referees: step 3 cites the improvement lemma for an arbitrary game. G_τ is a parity game (Odd's vertices have
    one successor each), so the lemma applies. I have not re-opened VJ00 for its theorem number in this box; the citation is VJ00 §4-5
    as used throughout R15.
### 7.6 N-U1-4 / N-U1-5 = D-2 / D-1 (§5 above); N-U1-2 (DATA note)
- N-U1-2: the f > 0 and K > 0 branches of Theorem U1 are never exercised by REFEREE-2's data. The theorem rests on the proof there.

## 8. Labels after this layer (both signatures, D18/L40)
With both signatures (REFEREE R-N5-U1, REFEREE-2 R2-N5-U1; §C pending), TB, CASC, Lemma R (§1.1 form, invariant as in §7.2), Theorem U1
and Lemma WC are PROVED (L-NEW; REFEREE, REFEREE-2), on 𝒞^1O, given f (Theorem U1, WC). §7.5's EQ-fallback claim is PROVED (L-NEW),
unrefereed. §6 of the packet stays a READING.
