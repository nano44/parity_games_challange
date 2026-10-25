# N5 on o-cyclic 𝒞^1O, box 35: H1-toggles per phase are polynomial (Theorem TOGGLE); the one-drop-per-run form is false
L-NEW successor 15 (Opus 5.5, D15/D18). Box 35 GO by the Lead at 08:02Z (Lead's stamp). Written 2026-10-25 08:06Z onward by date -u.
- Setting and notation: P-N5-SN §0 (docs/new/P-N5-SN-box33.md, pinned 2c70ef6) and N5-REL-box34.md §10-§13. A phase is a run of states with
  λ_Ξ and τ constant. c := c_θ = λ(o), fixed in the phase. U := λ^{-1}(c). H1: o lies on no honest cycle. A DROP is a transition H1 → ¬H1,
  and an H1-TOGGLE is a transition at which H1 changes. next_k(v) := σ_k(v) for Even v, σ̄_k(v) for Odd v (H_k, the honest graph). On 𝒞^1O
  every Odd vertex except o has exactly one successor. Every script here asserts this.
- Labels (D18/L40): PROVED (L-NEW succ. 15, unrefereed), CONJECTURE, OPEN, DATA. Nothing here is a running-time bound for N5, a TARGET.md
  claim or a step-4 pass. G-N5-TIME stays OPEN.
- Signed results used: R15 (a) (Ξ_k ⊴ Ξ_{k+1} at every transition; σ_{k+1} is σ_k with a set of improving switches applied, at S4a and at
  S4c); the phase key (λ constant); N5-REL-box34 §11 H1-INT (lane PROVED, in packet P-N5-L2): every ¬H1 state has P(θ) = ∅.

## Summary
1. **Lemma L-MONO (PROVED).** In a phase with c ≠ o, let L_k be the length of c's honest cycle. If Ω(c) is even, L is non-increasing; if
   Ω(c) is odd, L is non-decreasing. L changes strictly at every transition where σ(c) changes. So σ(c) changes at most n − 1 times per phase.
2. **Lemma Z-COUNT (PROVED).** Put Z_k := {(v, len Ξ_k(v)) : v ∈ U, P(Ξ_k(v)) = ∅}, the "∅-layer". Z changes at no more than |U|(n + 1)
   transitions of a phase.
3. **Theorem TOGGLE (PROVED).** In a phase with c ≠ o, every H1-toggle transition changes Z or changes σ(c). If c is an Odd vertex, it
   changes Z.
4. **Corollary TOGGLE-COUNT (PROVED).** A phase has at most |U|(n + 1) + n − 1 ≤ n² + 2n − 1 H1-toggles, so at most n²/2 + n drops. With
   X-RUN′ (N5-REL-box34 §11; P-N5-L2), summed over the fallback-free runs of a phase:
   X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T, with T := n² + 2n − 1. This holds with no hypothesis on H1. It replaces §12 item 1 of
   N5-REL-box34 (ONE-DROP, refuted in §13 there) and DROP-LEN, as far as these were needed for the count.
5. **The weak form of DROP-LEN is FALSE (DATA, verified).** Two drops occur in ONE fallback-free run: onerun_cex_n32 (§3). θ changes between
   the two drops there, so DROP-LEN itself survives. DROP-LEN stays CONJECTURE (§4). After item 4 it is no longer needed for the count.
6. **(b) A fallback restart via τ(o) leaving R (OPEN; DATA §5):** 0 cases. All 104 in-phase fallbacks at H1 ∧ ¬H2 in the library, and 1
   in 20,000 random games, keep ¬H2 at the next state.

## 1. Lemma L-MONO (PROVED, L-NEW succ. 15)
Statement. Let c = λ(o) ≠ o in a phase. Let L_k be the length of the cycle of c's H_k-play (c lies on it, since λ(c) = c). If Ω(c) is even, then
L_{k+1} ≤ L_k, with strict inequality if σ_{k+1}(c) ≠ σ_k(c). If Ω(c) is odd, the inequalities are reversed.
Proof. Take Ω(c) even (Even prefers shorter lengths to an even cycle node). The odd case only reverses the length order.
- On c's cycle, every vertex other than c is less relevant than c, since c is the cycle's top. So for x on the cycle,
  Ξ_k(x) = (c, ∅, dist_k(x → c)), and Ξ_k(next_k(c)) = (c, ∅, L_k − 1).
- If next_{k+1}(c) = next_k(c) =: x, then R15 (a) at x gives (c, ∅, L_{k+1} − 1) = Ξ_{k+1}(x) ⊵ Ξ_k(x) = (c, ∅, L_k − 1). Hence L_{k+1} ≤ L_k.
  This covers an Odd c (c ≠ o has one successor).
- If σ_{k+1}(c) = z ≠ σ_k(c), then (c, z) is improving at k (S4a's arena, S4c's switch set). So Ξ_k(z) ▷ Ξ_k(σ_k c) = (c, ∅, L_k − 1).
  - z lies on c's new cycle, so Ξ_{k+1}(z) = (c, ∅, L_{k+1} − 1).
  - By R15 (a), Ξ_{k+1}(z) ⊵ Ξ_k(z). Both values have cycle node c (λ is constant in the phase).
  - So (c, ∅, L_{k+1} − 1) ▷ (c, ∅, L_k − 1), i.e. L_{k+1} < L_k. □
- Remark. A switch at c changes no Ξ-value: Ξ(c) = (c, ∅, 0), and every other play stops at its first visit to c. It does change the honest
  cycle, and with it H1. In the data most toggles happen this way (§2, column S).

## 2. Lemma Z-COUNT and Theorem TOGGLE (PROVED, L-NEW succ. 15)
**Lemma Z-COUNT.** For v ∈ U, the states k of a phase with P(Ξ_k(v)) = ∅ form one interval. On that interval len Ξ_k(v) is monotone. So
(v ∈ Z, its length) changes at most n + 1 times, and Z changes at no more than |U|(n + 1) transitions.
Proof. λ(v) = c throughout the phase. VJ00's order compares path sets by the injective signed weight Σ ±2^rank, with weight(∅) = 0.
R15 (a) makes v's weight non-decreasing, so the states with weight 0 form an interval (as in H1-INT). Inside it, lengths move in one
direction (R15 (a)) within [0, n − 1]. That is one entry, one exit and at most n − 1 length changes. □
**Theorem TOGGLE.** Let k → k+1 be a transition of a phase with c ≠ o at which H1 changes, and suppose Z_{k+1} = Z_k. Then
σ_{k+1}(c) ≠ σ_k(c). In particular c ∈ V_E.
Proof. Let C be c's honest cycle at the ¬H1 end of the transition: C' at k+1 for a drop, C at k for a regain. C passes o (o lies on its honest
cycle, whose top is λ(o) = c). Every vertex of C lies in U and has P = ∅ there (c tops C). This includes o: θ = (c, ∅, ℓ) at ¬H1 states
(H1-INT). So all of C, with its lengths, lies in the common Z := Z_k = Z_{k+1}.
- Step 1: next_k(x) = next_{k+1}(x) for every x ∈ C \ {c, o}. Write x' for x's successor on C, so (x', len(x) − 1) ∈ Z, or x' = c with
  len(x) = 1.
  - At both states, Ξ(x) = (c, ∅, len(x)) with x ≠ c less relevant than c. So Ξ(next(x)) = (c, ∅, len(x) − 1) at both states.
  - Hence Ξ_k(x') = Ξ_k(next_k x) and Ξ_{k+1}(x') = Ξ_{k+1}(next_{k+1} x). (Ξ(c) = (c, ∅, 0) always.)
  - Odd x ≠ o has one successor, so nothing can change there.
  - Drop, Even x: x' = next_{k+1}(x). If σ_k(x) ≠ x', the switch (x, x') would be improving at k, i.e. Ξ_k(x') ▷ Ξ_k(σ_k x). But these
    two values are equal.
  - Regain, Even x: x' = next_k(x). If σ_{k+1}(x) = y ≠ x', then (x, y) is improving at k: Ξ_k(y) ▷ Ξ_k(x') = (c, ∅, len(x) − 1). But by
    R15 (a), Ξ_k(y) ⊴ Ξ_{k+1}(y) = Ξ_{k+1}(next_{k+1} x) = (c, ∅, len(x) − 1). Contradiction.
- Step 2. Suppose next_k(c) = next_{k+1}(c). By step 1, at the H1 end of the transition, c's honest play follows C from c up to o (the vertices
  between c and o on C keep their successors).
  - c is a cycle node at both states (λ(c) = c), so its play returns to c.
  - So o lies on c's cycle, and o's honest play (which reaches c, λ(o) = c) runs around it. o is then on its own honest cycle: ¬H1 at the
    H1 end. Contradiction.
  - So next(c) changes. Since only o among the Odd vertices has a choice, and c ≠ o, c is Even and σ(c) changes. □
**Corollary TOGGLE-COUNT.** The H1-toggle transitions of a phase are among the Z-changing transitions (≤ |U|(n + 1), Z-COUNT) and the
σ(c)-changing transitions (≤ n − 1, L-MONO). So there are ≤ |U|(n + 1) + n − 1 toggles and ≤ ⌈toggles / 2⌉ drops.
**Corollary X-SN-PHASE (PROVED, given X-RUN′).** X-RUN′ (N5-REL-box34 §11, in packet P-N5-L2, unrefereed): a fallback-free run Q has
≤ 13(d_o + 1)n³(t_Q + 1) + t_Q SN-prefix crossings, where t_Q counts the H1-toggles of Q's SN prefix. Sum over the ≤ f + 1 runs of a phase,
with Σ t_Q ≤ T := n² + 2n − 1: X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T per phase. This needs no ONE-DROP and no DROP-LEN.
- What this changes in N5-REL-box34 §12. Item 1 (ONE-DROP / DROP-LEN) is no longer needed. Item 3 (restarts through ¬H1 states) is
  ≤ drops ≤ n²/2 + n per phase. Item 4 (short (h)-runs) is ≤ the number of restarts. Item 2 (fallback restarts via τ(o) leaving R) stays OPEN
  (§5). The core (L1) is untouched: the f-dependence remains.
- DATA (experiments/new/box35/togz.py; data/togz_lib.txt, data/togz_rand.txt): 0 failures of L-MONO, of L-MONO's strict part, of Z-COUNT
  (interval and monotone length), and of TOGGLE.
  - Library (box34/lib.txt + box34 instances + experiments/red/*/instances + experiments/si/coarse/instances): 1,277 phases, 14 toggles.
    By what changes at the toggle: σ(c) only 9, Z only 1, both 4. 9 of the 14 are at fallbacks.
  - Random (20,000 games, n 4-14, seed 3551): 39,776 phases, 280 toggles. σ(c) only 198, Z only 29, both 53.
  - Max per phase: toggles 3 (library, onedrop_cex_n32), 2 (random); drops 2 / 1; σ(c)-changes 3 / 2; Z-changes 44 (x32_rand48) / 3.

## 3. The weak form of DROP-LEN is FALSE (DATA, verified)
- DEAD END: "at most one drop per fallback-free run" (N5-REL-box34 §13, the weaker form) is FALSE.
  - Instance: experiments/new/box35/instances/onerun_cex_n32.pg (sha1 70832fcb75b9b4b737034f9e0231d3b5e753959c; n 32, o = 27,
    succ(o) = {3, 17}). Climb: dlclimb.py MODE=fr seed 3603 from onedrop_cex_n32, violation at mutation 93.
  - Verified: n5.py n5 gives 8 iterations and 0 fallbacks. check_sol2.py gives "zielonka(oink zlk) OK strategies verified". Exactly one Odd
    vertex has out-degree > 1 (27).
  - The phase is states 2-8 with c = 13 (Ω 30). There are no fallbacks in the whole run.
    - State 2: H1, θ = (13, ∅, 14). At 2 → 3, 13 switches 8 → 27 = o: a drop by σ(c) (S4a).
    - State 3: ¬H1, θ = (13, ∅, 10). At 3 → 4, 13 switches 27 → 29: a regain by σ(c).
    - States 4-7: H1, θ = (13, ∅, 7). At 7 → 8, 13 switches 29 → 27: a second drop by σ(c), in the same fallback-free run.
  - c's cycle lengths L at states 2-8 (computed by togz.cyclen): 16, 11, 10, 10, 10, 9, 8. L drops strictly at each σ(13) switch, as
    L-MONO requires, and once more at 6 → 7 without one (29 switches 1 → 8 on the cycle). At the ¬H1 states L = ℓ + 1 (11 = 10 + 1,
    8 = 7 + 1), since 13 → o directly.
- θ changes between the two drops (length 10 → 7), so this instance is consistent with DROP-LEN.

## 4. DROP-LEN (CONJECTURE, DATA)
- Statement (N5-REL-box34 §13): between two drops of a phase, θ changes.
- With Theorem TOGGLE it is no longer needed for a polynomial toggle count. It would improve T from n² + 2n − 1 to 2n + 1.
- Why TOGGLE does not give it. A drop by σ(c) alone changes no Ξ-value (§1 remark), so θ can stay. What forces the length change in both
  instances is that the regain also happens through σ(c), and L must then fall below ℓ + 1 again (at ¬H1 states L ≥ ℓ + 1, where ℓ is θ's
  length). No proof yet.
- Climbs (dlclimb.py MODE=dl, fitness = max drops inside one θ-constant stretch): seeds onedrop_cex_n32, oneh_cex_n32 and onerun_cex_n32.
  Results in §6.

## 5. (b): a fallback restart at H1 ∧ ¬H2 taking τ(o) out of R (OPEN; DATA)
- Data (experiments/new/box35/fbtau.py; data/fbtau_lib.txt, data/fbtau_rand.txt):
  - Library: 104 in-phase S4c fallbacks at H1 ∧ ¬H2 states. In 91 of them τ(o) = o (a self-loop: o is its own W-cycle, and no fallback can
    change that). In the other 13, τ(o) stays in R. 104 / 104 have H1 ∧ ¬H2 at s + 1.
  - Random (20,000 games, n 4-14, seed 3552): 1 such fallback; τ(o) stays in R.
- Pitfall (my first run): reach_o's R omits o. With τ(o) = o, "τ(o) ∉ R" is a false positive (91 at first). Fixed: test τ(o) ∉ R ∪ {o}.
- Easy half (PROVED, L-NEW succ. 15). If τ(o) = o, ¬H2 holds at every state of the phase, so no restart of kind (i) can happen. τ is
  constant in a phase.
- The S4a proof (H2-STICK via R-STICK) uses WM, which fails at S4c. A proof attempt at fallbacks is in §6.

## 6. Work log (DATA; filled in as the box runs)
