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
6. **(b) is FALSE (DATA, verified).** A fallback at an H1 ∧ ¬H2 state CAN take τ(o) out of R and restart (h) inside the phase:
   fbrestart_cex_n12 (n 12) and fbrestart_cex_n24 (§5). This costs nothing extra in the count. Such a restart sits at a fallback, so it
   begins a new fallback-free run, and X-RUN′ already counts per run. (L2) is now closed up to the factor (f + 1): restarts ≤ T + f, and
   short (h)-runs cost ≤ n(T + f + 1) transitions per phase. What is left is the core (L1), the f ↔ X loop.

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

## 4. DROP-LEN: FALSE (DEAD END; found by REFEREE succ. 7, re-run by the Lead and by this lane)
- REFEREE's instance docs/referee/R-N5-L2/droplen_cex_n12.pg (sha1 a6af26db3f75540aa0f519cf0420b890fd2d4cc9; n 12, o = 0; docs/referee/R-N5-L2.md §8).
  - Verified here: n5.py n5 gives 4 iterations and 0 fallbacks; check_sol2.py gives "zielonka(oink zlk) OK strategies verified"; exactly one
    Odd vertex with out-degree > 1.
  - One phase. θ = w = (2, ∅, 1) is constant. H1 toggles at every transition, so there are 2 drops with θ constant, in one fallback-free
    run. Every transition is one S4a switch of σ(2), and c_θ = 2 is odd (σ(2): 0 → 1 → 7 → 9 → 10, with L rising each time).
  - Exact obstruction: a switch at c changes no Ξ-value (§1 remark). With c adjacent to o (here o → 2 directly), the drop and the regain
    are both pure σ(c) switches, so θ never moves.
- TOGGLE (togz.py on it): 4 toggles, 3 by σ(c) only and 1 by Z and σ(c), 0 failures. TOGGLE-COUNT is therefore the bound that holds, not a
  fallback.
- The text below is the pre-refutation record (kept as history).
- Statement (N5-REL-box34 §13): between two drops of a phase, θ changes.
- With Theorem TOGGLE it is no longer needed for a polynomial toggle count. It would improve T from n² + 2n − 1 to 2n + 1.
- Why TOGGLE does not give it. A drop by σ(c) alone changes no Ξ-value (§1 remark), so θ can stay. What forces the length change in both
  instances is that the regain also happens through σ(c), and L must then fall below ℓ + 1 again (at ¬H1 states L ≥ ℓ + 1, where ℓ is θ's
  length). No proof yet.
- Climbs (dlclimb.py MODE=dl, fitness = max drops inside one θ-constant stretch): seeds onedrop_cex_n32, oneh_cex_n32 and onerun_cex_n32.
  Results in §6.

## 5. (b): a fallback restart at H1 ∧ ¬H2 taking τ(o) out of R: it HAPPENS (DEAD END for "impossible"; DATA, verified)
- First survey (experiments/new/box35/fbtau.py; data/fbtau_lib.txt, data/fbtau_rand.txt):
  - Library: 104 in-phase S4c fallbacks at H1 ∧ ¬H2 states, 0 events.
    - In 91 of them τ(o) = o: o is its own W-cycle. τ is constant in a phase, so ¬H2 then holds throughout the phase (PROVED, trivial).
    - In the other 13, τ(o) stays in R. In frz24 (L-RED) at s = 20, the W-cycle vertex 22 switches into F, but 7 (earlier on the cycle)
      switches to a shortcut inside R, so τ(o)'s play no longer passes 22.
  - Random (20,000 games, n 4-14, seed 3552): 1 such fallback, 0 events.
  - Pitfall in my first run: reach_o's R omits o. With τ(o) = o, the test "τ(o) ∉ R" gives a false positive (91 at first). Fixed: test
    τ(o) ∉ R ∪ {o}.
- Climb (fbtclimb.py; fitness = (events, such fallbacks with a W-cycle switch, such fallbacks)): events within seconds from both seeds.
- DEAD END: "a fallback at an H1 ∧ ¬H2 state never takes τ(o) out of R" is FALSE.
  - Instance experiments/new/box35/instances/fbrestart_cex_n12.pg (sha1 35223b6c46750b2c1c961d68485025a9a5e69d87; n 12, o = 9,
    succ(o) = {4, 10}; climb seed 3612 from experiments/new/box25/instances/wd12_s1.pg).
    - Verified: n5.py n5 gives 5 iterations and 2 fallbacks. check_sol2.py gives "zielonka(oink zlk) OK strategies verified". Only 9 is an
      Odd vertex with out-degree > 1.
  - Second instance fbrestart_cex_n24.pg (sha1 a0aacfba3581c1c921e9b2090711b4ac536305f7; n 24, o = 19; seed 3611 from frz24). Verified the
    same way: 23 iterations, 3 fallbacks, zlk OK.
  - Mechanism in fbrestart_cex_n12. The phase is states 0-3, with τ(o) = 10 and c_θ = 4 (self-loop, Ω 8).
    - State 2: H1 ∧ ¬H2. o's W-cycle is 9 → 10 → 1 → 2 → 9, and its top is o itself (c_w = 9: Ω 8, ranked above 4), so w = (9, ∅, 0).
    - Iσ = {(1, 3), (6, 3)}. The edge 1 → 3 leads into F (3 → 7 → 11 → 5 → 4). It is honest-improving:
      Ξ(3) = (4, {3072}, 4) ▷ Ξ(2) = (4, {256}, 2). It is W-worsening: W(3) = (4, …) ◁ W(2) = (9, ∅, 1). So S4a withholds it (σ is optimal
      in its arena against τ), S4b leaves τ, and the fallback S4c takes it.
    - State 3: τ(o)'s play 10 → 1 → 3 → … → 4 avoids o. So H2 holds, c_w = c_θ = 4, and (h) holds, in the same phase (key λ_Ξ, λ_U, τ(o)).
- Consequence for (L2) (PROVED, given X-RUN′ and TOGGLE-COUNT).
  - Such a restart is at a fallback, so it opens a new fallback-free run. X-RUN′ bounds each run whatever its start.
  - So (h)-run restarts per phase are ≤ T + f (kind (ii) ≤ the toggles, kind (i) ≤ f), and short (h)-runs cost ≤ n(T + f + 1) transitions.
  - Every (L2) item is now ≤ poly(n)·(f + 1) per phase. The open core is (L1) and the f ↔ X loop (R28 f ≤ n_E(2n − 1)(X + 1) + X).

## 6. Work log (DATA; filled in as the box runs)
- Climbs: 40 min each. Logs are in experiments/new/box35/out/ (gitignored), and the instances below are copied to instances/.
  - MODE=dl, seeds onedrop_cex_n32, oneh_cex_n32 and onerun_cex_n32: the best stays at 1 drop per θ-constant stretch, up to 4 toggles and
    31 ¬H1 states. DROP-LEN is not refuted.
  - MODE=fr: violation at mutation 93 of seed 3603. This is onerun_cex_n32 (§3).
  - MODE=tog, from onedrop_cex_n32: 6 H1-toggles in one phase at n 32. That is well below TOGGLE-COUNT's n² + 2n − 1 = 1087.
  - fbtclimb.py: events at seeds 3611 and 3612 (§5).

## 7. (c): level −1 fallbacks; Lemma CN-LAST (PROVED, L-NEW succ. 15; every game)
- Angle. L-SI's open list (P-N5-NJB §5) includes "level −1 fallbacks per scope run", and the (L1) core needs every kind of fallback
  counted. MINSET and ENT-SHAPE handle levels ≥ 0, so I look at level −1. A level −1 gate (y, z) has Ξ(z) and Ξ(σ y) with the same cycle
  node and the same P, differing only in length.
- First, the kinds of θ-change in scope runs (thcls.py, library + experiments/si/coarse instances; data/thcls_lib.txt; DATA). There are
  200 scope runs and 1,507 θ-changes. Above the last fallback level, the only kind of θ-change is an absorption (49 cases). Overtakes and
  value rises with the same σ̄(o) never exceed it. This is MINSET (b)-(c) seen in data, and it is L-SI's ground, so I left it.
- DATA: level −1 Even fallbacks are rare, and in almost all of them every gate sits at its own cycle node.
  - library: 25 cases, 24 with own-cycle-node gates only;
  - random (20,000 games, n 4-14, seed 3553): 680 cases, 680 with own-cycle-node gates only;
  - the one exception is box28/out/oc12_s1 at k = 6 (gate 0 → 7, a length-only gate at a non-cycle node).
  Logs: lenrun.py; data/lenrun_lib.txt, data/lenrun_rand.txt.
**Lemma CN-LAST.** Let k be an S4c fallback at which Even switches, such that every gate (y, z) at k has λ_k(y) = y and level −1. Then:
- (i) Ξ_{k+1} = Ξ_k;
- (ii) Iσ_{k+1} = ∅;
- (iii) k + 1 is the last state of its phase: the next iteration changes τ, or N5 stops.
So a phase has at most one such fallback, and it is the phase's last transition.
Proof.
- Setup. The fallback switches exactly the gate tails, all of which are own cycle nodes c_1, …, c_p. It sends each c_i to z_i, its best gate
  target by (Ξ_k, index) (SPEC S4c). Level −1 at c_i: Ξ_k(σ_k c_i) = (c_i, ∅, L_i − 1) by (F) of P-N5-TOG §0, so Ξ_k(z_i) = (c_i, ∅, d_i)
  with a strictly better length. z_i's H_k-play reaches c_i. It meets no other c_j first: c_j's play is its own cycle, so passing c_j would
  give cycle node c_j ≠ c_i. All vertices of that path are less relevant than c_i, since P = ∅.
- (i) Let σ′ := σ_{k+1}, and let σ̄ := σ̄_k, Odd's optimal counterstrategy to σ_k (pointwise, R18 Lemma S (a)). Compare the (σ′, σ̄)-plays with
  the (σ_k, σ̄)-plays.
  - A play that meets no c_i is unchanged.
  - A play that meets some c_i first at c_i agrees with the old play up to c_i. After c_i it runs c_i → z_i → … → c_i, a cycle topped by c_i.
    The old play was on c_i's old cycle, also topped by c_i. Values are measured to the first visit of the cycle node, so the value is the
    same.
  - Hence V_{σ′, σ̄} = Ξ_k. Ξ_{k+1} is the pointwise minimum over Odd strategies (R18 Lemma S (a)), so Ξ_{k+1} ⊴ Ξ_k. R15 (a) gives ⊵, so
    the two are equal.
- (ii) At a non-switched Even vertex, σ and Ξ are unchanged and there was no gate at k, so there is none at k+1.
  - At c_i, suppose (c_i, w) were a gate at k+1. Then Ξ_k(w) = Ξ_{k+1}(w) ▷ Ξ_{k+1}(z_i) = Ξ_k(z_i) ▷ Ξ_k(σ_k c_i).
  - So (c_i, w) was a gate at k with a better value than z_i, against the choice of z_i.
- (iii) With Iσ_{k+1} = ∅, S4a does nothing. Either Iτ_{k+1} = ∅ and N5 stops (S5), or S4b changes τ, or the Odd fallback (S4c with
  Iσ = ∅) changes τ. τ is part of the phase key. □
- Remark. The converse direction is R15 (b): a switch set that leaves Ω unchanged consists of length-only switches at cycle nodes. CN-LAST
  is the forward direction for the S4c switch set, together with its consequence for N5's control flow.
- DATA: 24 + 680 cases, 0 failures of (i) or (ii), and the phase never continues past k + 1 (lenrun.py, CNLAST_* counters).
- What stays OPEN: level −1 fallbacks with a gate at a non-cycle node (1 case seen, oc12_s1). LEN-STAY ("after a state with M = −1 the
  pair (cycle node, P) is frozen for the rest of the phase") is FALSE in data: 4 library cases (first claimF_len_cf1) and 1 random case.
- What this does for (L1): with CN-LAST, the level −1 fallbacks of a phase are ≤ 1 + (level −1 fallbacks with a non-cycle-node gate). The
  open fallback count per scope run is then NJB (levels ≥ 0, L-SI / L-RED) plus that residue. The f ↔ X loop itself is untouched.

## 8. (c): the Lead's "tie (L1) to X-RUN" route, and CONJECTURE PF-THETA (READING, DATA)
- The loop, restated with what is landed or lane-PROVED:
  - per phase, Θ ≤ (n − 1) + n(X + 1) + X (R27 (g) Lemma TH);
  - f = O(n⁴(1 + X)) (R27 (h) Corollary XJ);
  - X ≤ Σ_runs [SN-prefix crossings + (n − 1)] + f ≤ 13(d_o + 1)n³(f + 1 + T) + T + (n − 1)(f + 1) + f (X-RUN′ + TOGGLE-COUNT + SN-PREFIX).
  So X and f are polynomially equivalent per phase, and both are open. To break the loop, a count must charge fallbacks to something
  other than crossings.
- Per scope run, the box-34 READING (N5-REL-box34 §9: E1 = R20's FBF in a scope run; FBL for THR fallbacks with u* ≠ none) gives:
  non-flat THR fallbacks ≤ n·(1 + θ-changes in the run). θ-changes before the run's first fallback are poly(n) (X-RUN with H1 throughout, plus
  TH's per-interval count). So what is missing is a count of θ-changes AFTER fallbacks.
- **CONJECTURE PF-THETA (DATA).** In a scope run, while the last fallback has level M, θ changes at most n times (for each M).
  - With CLS1 (R29: fallback levels never rise along a scope run at THR fallbacks with u* ≠ none) there are ≤ n + 1 values of M. So PF-THETA
    gives ≤ n(n + 1) θ-changes after fallbacks per scope run, and, through the READING, poly(n) non-flat THR fallbacks per scope run, without NJB.
  - NJB implies the poly-constant form: ≤ n_E fallbacks per level, each followed by a fallback-free stretch with poly(n) θ-changes. So
    PF-THETA is no stronger than NJB in power. Its use is as a different target: it counts θ, not Mn.
  - DATA (data/postfb_lib.txt; library + experiments/si/coarse + experiments/red instances): 131 scope runs with a fallback. Max θ-changes
    under one fallback level: 24 (sc32, n 32, after its only fallback, level 30). Max over runs of post-fallback θ-changes /
    (n · #distinct fallback levels): 0.81 (j4_n40: 34 changes, 4 fallbacks at levels 39, 38, 38, 37).
  - Climbs pfclimb.py (fitness = max θ-changes under one fallback level, then fallbacks): results in §9.
- Where a proof stops (OPEN). While the last fallback level is M and r > M, MINSET (b) freezes the COARSE_M values of the free exits. So
  θ's changes at levels ≤ M are changes of P(θ) ∩ V_{≤M} and of length, along the min exit's F-path. They are R17 one-player changes on F
  between crossings (TH), and nothing yet bounds the crossings between two fallbacks of one level except X-RUN's poly(n) per run. The
  needed new ingredient is the same as for NJB: a reason why the drain/refill loop cannot repeat at one level more than poly(n) times.
- Thcls DATA for the same corpus (data/thcls_lib.txt): 200 scope runs; θ-change kinds after fallbacks, by level relative to the last
  fallback level:
  | kind | above (gt) | equal (eq) | below (lt) |
  | --- | --- | --- | --- |
  | ABS | 49 | 37 | 427 |
  | OVT | 0 | 43 | 259 |
  | VAL | 0 | 82 | 60 |

## 9. PF-THETA climbs (DATA)
- pfclimb.py, 30 min each. Fitness = (max θ-changes under one fallback level in one scope run, fallbacks in that run).
- Each best was verified (n5.py n5, check_sol2.py "zielonka(oink zlk) OK strategies verified", one Odd choice vertex) and is copied to
  instances/:
  | seed (start) | n | start | final | instance (sha1) |
  | --- | --- | --- | --- | --- |
  | 3621 (sc32) | 32 | 24 | 31 (1 fallback) | pf_best_3621.pg (a9bff03b…) |
  | 3622 (j4_n40) | 40 | 13 | 35 (4 fallbacks) | pf_best_3622.pg (4decc325…) |
  | 3623 (x31_cu48) | 48 | 22 | 32 (1 fallback) | pf_best_3623.pg (e11bada0…) |
- No violation of PF-THETA (≤ n). The margin is thin (35 at n 40, 31 at n 32), and the climbs were still improving at the end. So the
  constant 1 in "≤ n" is not trustworthy. The poly form stays the CONJECTURE.
- In 3621 and 3623 the counts come after a single fallback, i.e. inside ONE fallback-free run. There they are bounded by poly(n) already
  (X-RUN + TH). So these climbs test the linear constant, not the loop.
