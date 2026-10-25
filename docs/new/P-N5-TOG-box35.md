# Referee packet P-N5-TOG: H1-toggles per phase are polynomial on 𝒞^1O (L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT)
L-NEW successor 15 (Opus 5.5, D15/D18). Written 2026-10-25 08:2xZ by date -u, for the Lead's referee queue after P-N5-NJB (Lead 08:17Z).
Working notes: docs/new/N5-DROP-box35.md. Labels (D18/L40): PROVED (L-NEW succ. 15, unrefereed), CONJECTURE, OPEN, DATA.
Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## 0. Objects and dependencies
- N5 as specified in docs/new/N5-ssi-global.md (SPEC S1-S5). S4a = Even's arena step, S4c = the fallback. Valuations x = (c, P, ℓ) and Even's
  order ⊴ are VJ00's (SPEC S1). For a fixed cycle node c, the order compares P by the injective signed weight Σ_{u∈P} ±2^rank(u), with
  weight(∅) = 0. Then it compares lengths: shorter is better for Even if Ω(c) is even, longer if Ω(c) is odd.
- Ξ_k := Even's honest valuation of σ_k (play values in H_k, the (σ_k, σ̄_k)-graph). next_k(v) := σ_k(v) for Even v, σ̄_k(v) for Odd v.
  λ_k(v) := the cycle node of Ξ_k(v), i.e. the most relevant vertex of the cycle on which v's H_k-play ends. A cycle node c has
  Ξ(c) = (c, ∅, 0).
- 𝒞^1O: exactly one Odd vertex o has out-degree > 1. So every Odd vertex other than o has one successor, at every state.
- PHASE (P-N5-SN §0, pinned 2c70ef6; RESULTS R27/R28): a run of consecutive states with λ_Ξ and τ constant. c := λ(o), constant in the
  phase. U := λ^{-1}(c). H1: o lies on no honest cycle. A transition k → k+1 inside a phase is an H1-TOGGLE if H1 differs at k and k+1,
  and a DROP if H1 holds at k and fails at k+1.
- Iσ_k := {(v, w) : v ∈ V_E, w ≠ σ_k(v), Ξ_k(w) ▷ Ξ_k(σ_k v)} (SPEC S2). At every transition, σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v):
  at S4a by the arena; at S4c the fallback sets σ(v) to an Iσ-target; at an Odd fallback σ is unchanged.
- Used results:
  - (M) := RESULTS R15 (a) (VJ00 Lemma 5.7, refereed). It is applied to I = {(v, σ_{k+1}(v)) : σ_{k+1}(v) ≠ σ_k(v)}: an unambiguous set of
    improvements, or empty. It gives Ξ_k(v) ⊴ Ξ_{k+1}(v) for every v and every transition k → k+1.
  - The phase key (λ constant).
  - Nothing from P-N5-FRZ or P-N5-L2 is used in §1-§4. §5 uses X-RUN′ (P-N5-L2, which rests on P-N5-FRZ's X-RUN). §6 uses H2-STICK,
    H3-CONST (P-N5-L2) and R30's H3H2.
- Dependency table:
  | item | depends on |
  | --- | --- |
  | L-MONO (§1) | (M), phase key |
  | Z-COUNT (§2) | (M), phase key |
  | TOGGLE (§3) | (M), phase key, 𝒞^1O |
  | TOGGLE-COUNT (§4) | §1-§3 |
  | X-SN-PHASE (§5) | §4 + X-RUN′ (P-N5-L2 §11, hence P-N5-FRZ) |
  | RESTARTS (§6) | §4 + H2-STICK, H3-CONST (P-N5-L2), H3H2 (R30) |
- Elementary fact (F). If x lies on the cycle of c's H_k-play and λ_k(c) = c, then Ξ_k(x) = (c, ∅, dist_k(x → c)): c is the most relevant
  vertex of its cycle, so no vertex before c on x's play is more relevant than c. If x ≠ c has λ_k(x) = c, then Ξ_k(x) = x ⊕ Ξ_k(next_k x):
  the same cycle node, P enlarged by x only if x is more relevant than c, and the length up by 1.

## 1. Lemma L-MONO (PROVED, L-NEW succ. 15)
Statement. Let c = λ(o) ≠ o in a phase, and let L_k be the length of the cycle of c's H_k-play (c lies on it, since λ_k(c) = c).
- If Ω(c) is even: L_{k+1} ≤ L_k, and L_{k+1} < L_k whenever σ_{k+1}(c) ≠ σ_k(c).
- If Ω(c) is odd: the same with both inequalities reversed.
- Hence σ(c) changes at most n − 1 times in a phase (1 ≤ L ≤ n).
Proof. Take Ω(c) even; for odd, reverse the length order.
- By (F), Ξ_k(next_k c) = (c, ∅, L_k − 1).
- Case next_{k+1}(c) = next_k(c) =: x (this includes every Odd c, which has one successor).
  - x lies on c's cycle at k+1, so Ξ_{k+1}(x) = (c, ∅, L_{k+1} − 1) by (F).
  - (M) gives Ξ_{k+1}(x) ⊵ Ξ_k(x). Same cycle node, same P = ∅, so L_{k+1} − 1 ≤ L_k − 1.
- Case σ_{k+1}(c) = z ≠ σ_k(c).
  - Then (c, z) ∈ Iσ_k (§0), so Ξ_k(z) ▷ (c, ∅, L_k − 1).
  - z lies on c's cycle at k+1, so Ξ_{k+1}(z) = (c, ∅, L_{k+1} − 1).
  - (M) gives Ξ_{k+1}(z) ⊵ Ξ_k(z).
  - So (c, ∅, L_{k+1} − 1) ▷ (c, ∅, L_k − 1), i.e. L_{k+1} < L_k. □
- Remark (not needed below). A switch at c changes no Ξ-value: Ξ(c) = (c, ∅, 0), and every other play stops at its first visit to c. This is
  R15 (b)'s length-only switch at a cycle node. It can still change the honest cycle, and with it H1.

## 2. Lemma Z-COUNT (PROVED, L-NEW succ. 15)
Statement. In a phase put Z_k := {(v, ℓ_k(v)) : v ∈ U, P(Ξ_k v) = ∅}, where ℓ_k(v) is the length of Ξ_k(v). Then Z_k ≠ Z_{k+1} at no more
than |U|(n + 1) transitions of the phase.
Proof.
- Fix v ∈ U. λ(v) = c at every state of the phase. By (M) and the order, weight(P(Ξ_k v)) is non-decreasing in k.
- weight is injective with weight(∅) = 0. So the states with P(Ξ_k v) = ∅ form one interval of the phase.
- On that interval Ξ_k(v) = (c, ∅, ℓ_k(v)). By (M), ℓ_k(v) is monotone there, with values in [0, n − 1]: at most n − 1 changes.
- So the pair (v ∈ Z_k?, ℓ_k(v)) changes at most 1 + 1 + (n − 1) = n + 1 times. A transition that changes Z changes it for at least one v. □

## 3. Theorem TOGGLE (PROVED, L-NEW succ. 15)
Statement. Let k → k+1 be an H1-toggle inside a phase with c = λ(o) ≠ o. If Z_{k+1} = Z_k, then next_{k+1}(c) ≠ next_k(c). Hence c ∈ V_E and
σ_{k+1}(c) ≠ σ_k(c).
Proof. Let a be the ¬H1 end of the transition and b its H1 end ({a, b} = {k, k+1}). Let C be the cycle of c's H_a-play.
- C passes o. At a, o lies on an honest cycle, namely the cycle of its own H_a-play. That cycle's node is λ(o) = c, so it is c's cycle.
- By (F), every x ∈ C has Ξ_a(x) = (c, ∅, d(x)), where d(x) := dist_a(x → c), and x ∈ U. So (x, d(x)) ∈ Z_a = Z_b =: Z for all x ∈ C,
  including o and c. Hence Ξ_b(x) = Ξ_a(x) = (c, ∅, d(x)) for all x ∈ C.
- Step 1: next_b(x) = next_a(x) for every x ∈ C \ {c, o}. Put x' := next_a(x) ∈ C, so d(x') = d(x) − 1 and Ξ_a(x') = Ξ_b(x') = (c, ∅, d(x) − 1).
  - By (F) at b (x ≠ c, λ_b(x) = c), Ξ_b(next_b x) = (c, ∅, d(x) − 1). By (F) at a, Ξ_a(next_a x) = (c, ∅, d(x) − 1).
  - Odd x ≠ o: one successor, nothing to show.
  - Even x, drop (a = k+1, b = k). Suppose σ_{k+1}(x) = x' ≠ σ_k(x). Then (x, x') ∈ Iσ_k: Ξ_k(x') ▷ Ξ_k(σ_k x) = Ξ_b(next_b x). Both sides
    equal (c, ∅, d(x) − 1). Contradiction.
  - Even x, regain (a = k, b = k+1). Suppose σ_{k+1}(x) = y ≠ x' = σ_k(x). Then (x, y) ∈ Iσ_k: Ξ_k(y) ▷ Ξ_k(x') = (c, ∅, d(x) − 1). By (M),
    Ξ_k(y) ⊴ Ξ_{k+1}(y) = Ξ_b(next_b x) = (c, ∅, d(x) − 1). Contradiction.
- Step 2. Suppose next_b(c) = next_a(c).
  - By step 1, c's H_b-play follows C from c until it first meets o or c. Along C, o comes before the return to c (o ∈ C, o ≠ c), so the
    play reaches o.
  - λ_b(c) = c, so c's H_b-play is a cycle through c, and o lies on it.
  - o's H_b-play then runs around that cycle, so o lies on its own honest cycle at b: ¬H1 at b. This contradicts the choice of b.
  - So next_b(c) ≠ next_a(c). Odd vertices other than o have one successor and c ≠ o, so c ∈ V_E and σ(c) changes. □

## 4. Corollary TOGGLE-COUNT (PROVED, L-NEW succ. 15)
In a phase with c ≠ o, every H1-toggle transition changes Z (≤ |U|(n + 1) such transitions, §2) or changes σ(c) (≤ n − 1, §1). So:
- H1-toggles per phase ≤ T := |U|(n + 1) + n − 1 ≤ n² + 2n − 1;
- drops per phase ≤ ⌈T / 2⌉, since drops and regains alternate.
If c = o, o lies on its own honest cycle at every state of the phase, so there are no toggles.

## 5. Corollary X-SN-PHASE (PROVED given X-RUN′; P-N5-L2 §11 X-RUN′, hence P-N5-FRZ)
- X-RUN′: in a fallback-free run Q of a phase, the SN prefix has ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q crossing transitions. Here t_Q is the number
  of H1-toggles in Q's SN prefix.
- A phase has ≤ f + 1 fallback-free runs, and Σ_Q t_Q ≤ T by §4. Summing:
  X_SN per phase ≤ 13(d_o + 1)n³(f + 1 + T) + T, with no hypothesis on H1.
- This replaces CONJECTURE ONE-DROP (refuted: onedrop_cex_n32) and CONJECTURE DROP-LEN in N5-REL-box34 §12 item 1.

## 6. Corollary RESTARTS (PROVED given H2-STICK and H3-CONST from P-N5-L2, and H3H2 from R30)
Statement. In a phase, the number of maximal (h)-runs is ≤ 1 + T + f.
Proof. Let k → k+1 start a new (h)-run, so ¬(h) at k and (h) at k+1. The phase has an (h) state, so by H3-CONST, H3 holds at every H2 state
of the phase. So ¬(h) at k means ¬H1 at k, or H1 ∧ ¬H2 at k.
- ¬H1 at k: the transition is an H1-toggle (≤ T).
- H1 ∧ ¬H2 at k: by H2-STICK the transition is not S4a. τ is constant in a phase, so it is not an Odd fallback. So it is an Even S4c
  fallback (≤ f).
- Both kinds occur:
  - toggle restarts: oneh_cex_n32, onedrop_cex_n32;
  - fallback restarts: fbrestart_cex_n12 and fbrestart_cex_n24 (§8). □
- So short (h)-runs (fewer than n states) cost ≤ n(1 + T + f) transitions per phase. Every (L2) item of N5-REL-box34 §12 is now
  ≤ poly(n)·(f + 1) per phase. The core (L1) and the f ↔ X loop are untouched (OPEN).

## 7. Not to sign (DATA, CONJECTURE, OPEN)
- CONJECTURE DROP-LEN (N5-REL-box34 §13): θ changes between two drops of a phase. It is optional after §4, and would improve T to 2n + 1.
  DATA: holds in every instance seen. Climbs dlclimb.py MODE=dl: work log N5-DROP-box35 §6.
- DEAD END (DATA, verified): "≤ 1 drop per fallback-free run" is FALSE.
  - Instance: experiments/new/box35/instances/onerun_cex_n32.pg, sha1 70832fcb75b9b4b737034f9e0231d3b5e753959c. Lead re-run 08:17Z.
  - Run: 8 iterations and 0 fallbacks. Two drops, at 2 → 3 and 7 → 8, both S4a switches of σ(13) into o.
- DEAD END (DATA, verified): "a fallback at H1 ∧ ¬H2 never takes τ(o) out of R" (N5-REL-box34 §12 item 2) is FALSE.
  - Instance: experiments/new/box35/instances/fbrestart_cex_n12.pg, sha1 35223b6c46750b2c1c961d68485025a9a5e69d87. Mechanism:
    N5-DROP-box35 §5.
  - Second instance: fbrestart_cex_n24.pg, sha1 a0aacfba3581c1c921e9b2090711b4ac536305f7.
- OPEN: (L1), i.e. re-entries after fallback evictions inside frozen blocks, equivalently θ-changes after fallbacks per scope run. Also the
  f ↔ X loop, and K.

## 8. Data (DATA; experiments/new/box35; each script asserts exactly one Odd vertex of out-degree > 1)
- togz.py checks L-MONO (both parts), Z-COUNT (interval and monotone length) and TOGGLE at every transition. 0 failures:
  - library (experiments/new/box34/lib.txt + box34 instances + experiments/red/*/instances + experiments/si/coarse/instances): 1,277 phases,
    14 toggles (σ(c) only 9, Z only 1, both 4; 9 of them at fallbacks); data/togz_lib.txt;
  - random (20,000 games, n 4-14, seed 3551): 39,776 phases, 280 toggles (σ(c) only 198, Z only 29, both 53); data/togz_rand.txt.
- Max per phase:
  | quantity | library | random |
  | --- | --- | --- |
  | toggles | 3 (onedrop_cex_n32) | 2 |
  | drops | 2 | 1 |
  | σ(c)-changes | 3 | 2 |
  | Z-changes | 44 (x32_rand48) | 3 |
- fbtau.py, fbtclimb.py: fallback restarts (§6, §7). n5.py n5 and check_sol2.py (Oink zlk, pinned 8fbf0a7) gave "OK strategies verified" on
  every instance named here.
- Reproduce: `python3 experiments/new/box35/togz.py $(cat experiments/new/box34/lib.txt)`, and `--rand 20000 4 14 3551`, from the repo root.
