# Premise (P) for one-player games: an elementary proof (Lemma P1)
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Box 10b, after the Lead's 11:14Z decision 3. Written 2026-10-25 (date -u, see the commit).
- Labels: PROVED (L-SI succ. 5, unrefereed), DATA.
- Target: (P), the premise of RESULTS R18 (G-1OA-4) and of P-N5-RL (docs/si/P-N5-RL-box10.md: BL (b), (c), (e), FREE-FREEZE, EV, EV+,
  TEV-RED). R18 states it as "(P) for one-player games: VJ00 Lemma 5.8 '1 ⇒ 2'".
- Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Relation to the existing re-derivation:
  - R-N5-1P §3 route (a) (REFEREE) re-derives the one-player case through VJ00's OverProg / Prop. 5.10 / Prop. 5.6. Prop. 5.10 is
    stated without proof in the source and "verified by me" there; the route was read as sound by REFEREE-2 but not signed.
  - The proof below uses no VJ00 lemma. It needs only the valuation's definition (SPEC S1, P-N5-FBW §0) and one device: path
    MULTISETS, which make prefixing monotone (the reason VJ00 §4.5 uses multisets).

## 0. Setting
- A ONE-PLAYER game H: every vertex not owned by Even has exactly one successor. Ranks are injective. pp(v) := 2·rank(v) + (Ω(v) mod 2).
  rew(c) := pp(c) if Ω(c) is even, −pp(c) if odd. rew is injective, and for rank t > rank c: rew(t) < rew(c) iff t is odd.
- A positional Even strategy σ gives every vertex a lasso play. V_σ(v) = (c, P, ℓ):
  - c := the top (max-rank) vertex of the cycle the play ends in;
  - P := the set of vertices of the play before its first visit to c with rank > rank c;
  - ℓ := the number of steps to that first visit.
- Order (better for Even):
  - first rew(c);
  - then the path part, decided by the top vertex of P Δ P′: Even-better if it is even and in the later set, or odd and in the earlier
    set (SPEC Q1);
  - then ℓ: longer is better if c is odd, shorter if c is even.
- s(x) := σ(x) for Even x, the unique successor otherwise. An Even edge (x, y) is IMPROVING for σ if V_σ(y) ▷ V_σ(σ x).
- EXTENDED values (c, μ, ℓ), with μ a finite multiset of vertices of rank > rank c. Same order, with the path part decided by the
  top-ranked vertex whose multiplicity differs: more of an even vertex is better, more of an odd vertex is worse. On sets this is the
  order above.
- PREFIX: x ⊕ (c, μ, ℓ) := (c, μ + [x if rank x > rank c], ℓ + 1).

## 1. Lemma M (monotone prefix; PROVED)
For fixed c, x ⊕ · is strictly order-preserving on extended values with cycle node c.
Proof.
- Adding x to both multisets leaves every multiplicity DIFFERENCE unchanged, so the path comparison is unchanged.
- Adding 1 to both lengths leaves the length comparison unchanged, and the length rule depends only on c. □
- On sets this fails: if x is the top of P Δ P′, then P ∪ {x} and P′ ∪ {x} compare differently. That is why the chains below are taken in
  multisets.

## 2. Lemma P1 (PROVED, L-SI succ. 5): (P) for one-player games
Let σ have no improving edge, and write V := V_σ. Then V(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v.
Proof.
- Step 1 (edge inequality). For every edge x → y of H: V(y) ⊴ V(s(x)).
  - For Even x this is "no improving edge" (y = σ(x) gives equality). For any other x, y = s(x).
- Step 2 (the prefix equation). If x is not the cycle node c(x) of V(x), then V(x) = x ⊕ V(s(x)), as real values and as extended values.
  - x's play is x followed by s(x)'s play, with the same cycle node.
  - x does not occur on s(x)'s play before c(x). Otherwise x would lie on the play's cycle, whose top c(x) is not x, and x's play would
    first visit c(x) only after returning to x, contradicting simplicity before the cycle.
  - If x = c(x), then s(x) lies on x's cycle, and V(s(x)) = (x, ∅, L − 1) with L the cycle length (x is the cycle's top).
- Step 3 (cycle nodes along edges). For every edge x → y: rew(c(y)) ≤ rew(c(x)).
  - c(s(x)) = c(x) in both cases of Step 2, and V(y) ⊴ V(s(x)) compares rew(c(y)) ≤ rew(c(s(x))) first.
- Step 4 (the super-solution chain). If x_0 → x_1 → … → x_m is a path of H and c(x_i) = c0 ≠ x_i for i < m, with c(x_m) = c0, then
  V(x_0) ⊵ x_0 ⊕ x_1 ⊕ … ⊕ x_{m−1} ⊕ V(x_m), in extended values.
  - Induction from the right: V(x_i) = x_i ⊕ V(s(x_i)) ⊵ x_i ⊕ V(x_{i+1}), by Step 2, Step 1 and Lemma M (all values have cycle node
    c0). Then use Lemma M again on the rest of the chain.
- Step 5 (any cycle on which V's cycle node is constant). Let C = (y_0 → y_1 → … → y_{p−1} → y_0) be a simple cycle of H with
  c(y_i) = c0 for all i, and t its top vertex. Then rew(t) ≤ rew(c0), with equality iff t = c0 (so c0 ∈ C).
  - Case c0 ∈ C, say y_0 = c0. Step 4 on y_1 → … → y_{p−1} → c0 gives V(y_1) ⊵ (c0, μ(y_1, …, y_{p−1}), p − 1).
    - Step 1 at the edge c0 → y_1 gives V(y_1) ⊴ V(s(c0)) = (c0, ∅, L − 1).
    - If t ≠ c0, then rank t > rank c0, and t is the top element of μ. The comparison (c0, μ, ·) ⊴ (c0, ∅, ·) is decided by t, so t
      is odd, and rew(t) < rew(c0).
  - Case c0 ∉ C. Every y_i is a non-cycle-node. Step 4 once around C gives V(y_0) ⊵ (c0, μ_0 + μ(C), ℓ_0 + p), where
    (c0, μ_0, ℓ_0) = V(y_0).
    - If μ(C) ≠ ∅: its top is t, with rank t > rank c0. The comparison is decided by t's multiplicity, so t is odd and
      rew(t) < rew(c0).
    - If μ(C) = ∅: every vertex of C is below c0, and the comparison is by length. ℓ_0 ⊵ ℓ_0 + p forces c0 to be even (for odd c0,
      longer is strictly better). Then rew(t) ≤ pp(t) < pp(c0) = rew(c0).
    - So rew(t) < rew(c0) strictly in this case.
- Step 6 (conclusion). Fix σ′ and v_0. Let v_0, v_1, … be its σ′-play, with cycle C′ and top c′.
  - By Step 3, rew(c(v_i)) is non-increasing along the play. On C′ it is constant, so c(·) = c0 on C′ (rew is injective), and
    rew(c0) ≤ rew(c(v_0)).
  - By Step 5, rew(c′) ≤ rew(c0).
  - If rew(c′) < rew(c(v_0)), then V_{σ′}(v_0) ◁ V(v_0).
  - Otherwise c′ = c0 = c(v_0), c0 ∈ C′ is its top, and c(v_i) = c0 for all i (non-increasing with equal ends).
    - Let v_b = c0 be the first visit of c0. The vertices v_0, …, v_b are distinct (the play is simple until it closes its cycle,
      and c0 ∈ C′).
    - Step 4 on v_0 → … → v_b gives V(v_0) ⊵ (c0, μ(v_0, …, v_{b−1}), b) = V_{σ′}(v_0). The multiset is a set here, and it is exactly
      the path part of V_{σ′}(v_0). □
- Consequence. Any two strategies without improving edges have equal valuations, and these are the pointwise optimum W* of R17 F1.

## 3. What this discharges (READING for the referees; each use should be re-checked against its signed text)
- RESULTS R18 (G-1OA-4): (P) is used "only in Lemma 1 on G[X]", a one-player game (G[X] has no Odd choice). Lemma P1 is (P) for it.
- P-N5-RL (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb):
  - BL (b) Step 2b applies (P) to G_τ ("Odd fixed to τ_k"), and BL (c) applies it to G_τ[F_k]. Both are one-player games, and the
    strategies involved are positional. So BL (b), (c), (e), FREE-FREEZE, EV, EV+ and TEV-RED become unconditional, once P1 is signed.
- N5's output correctness at S5 (R15's G-N5T-3) is the TWO-PLAYER form of VJ00 Lemma 5.8. It is NOT covered here.
  - P1 does give its one-player case: on a one-player game N5's output σ has no improving edge and is optimal.

## 4. DATA (DATA, not proof; experiments/si/p1/p1check.py, logs experiments/si/p1/logs/)
- Exhaustive over all Even positional strategies of random one-player games (Odd out-degree 1 asserted). Engine: experiments/si/si.py
  valuations; on a one-player game Ξ is the play valuation.
- Seed 5101: 3,000 games, n 3-9, 45,581 strategies. 3,336 have no improving edge, and every one is pointwise optimal: 0 violations.
  - 41,484 non-optimal strategies all have an improving edge.
  - The other 761 are optimal strategies that still have an improving edge: the own-cycle-node length-only case of FBW Step 2 /
    CN-LAST, which P1 does not need.
- Seed 5102: 1,500 games, n 8-12, 90,705 strategies (games with more than 4,000 strategies skipped). 1,930 have no improving edge,
  and every one is optimal: 0 violations.
- Independent data: R-N5-1P §6 (REFEREE): 7,945 games with n ≤ 6, 8,813 improvement-free strategies, 0 failures. R18: REFEREE-2, 2,283.
