# Referee packet P-N5-P1: premise (P) for one-player games (Lemma P1, with Lemma M and the set-multiset bridge)
L-SI successor 5 (Opus 5.5, D15/D18, L37/L40). Written 2026-10-25 11:43Z (date -u), at the Lead's request (11:44Z). Frozen at its
commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location of every dependency, the data and the script.
- Source text: docs/si/N5-P1-box10.md (lane write-up, l-si a04d072, sha1 5fb4f908). Where they differ, this packet governs.
- Status: L-SI successor 5's proof, unrefereed. Labels: PROVED (L-SI succ. 5), READING, DATA.
- Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- To sign:
  - §1 Definitions and Lemma B (the bridge: extended values restrict to the real order);
  - §2 Lemma M;
  - §3 Lemma P1;
  - §4 the hypothesis match with R18's (P).
- §5 is a READING (what P1 discharges, and what it does not). §6: data.

## 0. The premise being discharged, verbatim
- RESULTS R18 (docs/RESULTS.md, "### R18"), Honest limits (ii): "CONDITIONAL on (P) for one-player games (G-1OA-4, open by design):
  VJ00 Lemma 5.8 "1 ⇒ 2", used only in Lemma 1 on G[X]."
- R18's object line: "Source for (P): Vöge-Jurdziński, BRICS RS-00-48 (pdf sha256 485a12de…), Lemma 5.8 "1 ⇒ 2"."
- R18 (c), the theorem, is "conditional on (P) for the one-player game G[X]". Lemma 1 there: "at a pure transition σ|X has G[X]'s
  optimal valuation".
- Reading of (P) used in R18 and in P-N5-RL §0: in a one-player game, a strategy with no improving edge is optimal, i.e. its valuation
  dominates that of every strategy pointwise. "Optimal" is R17 (a) F1's notion, a pointwise maximum over the player's positional
  strategies (VJ00 §4.3).
- P-N5-RL (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb) §0 states (P) in the same form and applies it to G_τ and G_τ[F_k].

## 1. Definitions, and Lemma B (PROVED): the bridge between sets and multisets
- One-player game H: a finite graph, every vertex with ≥ 1 successor, owners Even / Odd, and every Odd vertex with exactly one
  successor. Injective ranks.
  - pp(v) := 2·rank(v) + (Ω(v) mod 2). rew(c) := pp(c) if Ω(c) is even, −pp(c) if odd.
  - rew is injective. For rank t > rank c: rew(t) < rew(c) iff Ω(t) is odd.
- A positional Even strategy σ (σ(v) a successor of v for Even v). s(x) := σ(x) for Even x, the unique successor for Odd x.
- The play from v is v, s(v), s(s(v)), …, a lasso: a simple path followed by a simple cycle.
- REAL value (SPEC S1; the engine experiments/si/si.py; R17's and R18's valuation):
  - V_σ(v) := (c, P, ℓ), with c the top (max-rank) vertex of the cycle;
  - P := the SET of vertices of the play before its first visit to c that have rank > rank c;
  - ℓ := the number of steps to that first visit.
  - Before the first visit to c the play is simple: it is the lasso's path followed by part of its cycle. So P lists each vertex at most
    once.
- REAL order ⊴ (SPEC S1 with SPEC Q1; the order of R15, R17 (a), R18; R-N5-1P §1 diffed it against VJ00 §4.2 / §4.5). (c, P, ℓ) ◁
  (c′, P′, ℓ′), "the right side is better for Even", iff:
  - (i) rew(c) < rew(c′); or
  - (ii) c = c′ and P ≠ P′, and the top-ranked vertex h of P Δ P′ is even with h ∈ P′, or odd with h ∈ P; or
  - (iii) c = c′, P = P′, and ℓ ≠ ℓ′, with ℓ < ℓ′ if c is odd and ℓ > ℓ′ if c is even.
- EXTENDED values (c, μ, ℓ): μ a finite multiset over V_{>c} := {v : rank v > rank c}, ℓ ∈ ℕ. Extended order ⊴ₓ:
  - (i) as above;
  - (ii′) c = c′ and μ ≠ μ′, and h, the top-ranked vertex with μ(h) ≠ μ′(h), is even with μ(h) < μ′(h), or odd with μ(h) > μ′(h);
  - (iii) as above.
- **Lemma B (bridge).**
  - (a) ⊴ₓ is a total order on extended values: reflexive, antisymmetric, transitive, and total.
  - (b) On extended values whose multisets are sets (all multiplicities ≤ 1), ⊴ₓ coincides with the real order ⊴.
  - (c) In particular, for real values a, b: a ⊴ b iff a ⊴ₓ b.
  Proof.
  - (a) Fix c. Index V_{>c} by decreasing rank as h_1, h_2, …. The map (c, μ, ℓ) ↦ (ε_1 μ(h_1), ε_2 μ(h_2), …, ε_c ℓ) is injective.
    Here ε_i = +1 if h_i is even and −1 if odd; ε_c = −1 if c is even and +1 if odd. (ii′)-(iii) is the lexicographic order of these
    integer vectors, which is a total order. Clause (i) orders the blocks of different c by the injective rew. A lexicographic
    combination of total orders is total.
  - (b) For sets M, M′: the vertices whose multiplicities differ are exactly M Δ M′, and the top one, h, has multiplicity 1 on one side
    and 0 on the other. "μ(h) < μ′(h)" is "h ∈ M′". So (ii′) is (ii), word for word. (i) and (iii) are shared.
  - (c) Real values have set path parts (§1, simplicity before the first visit to c). □
- How the bridge is used.
  - Every comparison in the HYPOTHESES and in the CONCLUSION of P1 is between real values.
  - Extended values with repeated vertices appear only in the middle of transitive chains (§3, Steps 4-6), each of which starts and
    ends at real values.
  - By Lemma B (a) the chains are valid in ⊴ₓ. By Lemma B (c) their real endpoints compare in ⊴ exactly as in ⊴ₓ.
  - So no statement about real play values changes.
  - Why multisets at all: the SET prefix x ∪ P is not monotone. If x is the top of P Δ P′, then P ∪ {x} and P′ ∪ {x} no longer differ
    at x. Lemma M below needs multiplicities.

## 2. Lemma M (PROVED): monotone prefix
For a vertex x and a fixed c, put x ⊕ (c, μ, ℓ) := (c, μ + [x]·𝟙(rank x > rank c), ℓ + 1). Then a ◁ₓ b implies x ⊕ a ◁ₓ x ⊕ b, for extended
values a, b with cycle node c.
- Proof. Adding the same element to both multisets leaves every multiplicity DIFFERENCE μ(h) − μ′(h) unchanged, so (ii′) decides the
  same way. Adding 1 to both lengths leaves (iii) unchanged, and (iii)'s direction depends only on c. □
- Real prefix. If x is not on the play of y before its first visit to c, and x ≠ c, then the real value of the play x, (play of y) is
  x ⊕ V(y): the set P gains x iff rank x > rank c, and the length gains 1.

## 3. Lemma P1 (PROVED, L-SI succ. 5)
**Lemma P1.** Let H be a one-player game, and σ a positional Even strategy with NO IMPROVING EDGE: no Even edge (x, y) with
V_σ(y) ▷ V_σ(σ(x)) (SPEC S2). Then V_σ(v) ⊵ V_{σ′}(v) for every positional Even strategy σ′ and every vertex v.
- Notation: V := V_σ, and c(x) := the cycle node of V(x).
Proof.
- Step 1 (edge inequality). For every edge x → y of H: V(y) ⊴ V(s(x)).
  - For Even x it is the hypothesis (equality when y = σ(x)). For Odd x, y = s(x).
- Step 2 (prefix equation).
  - If x ≠ c(x): V(x) = x ⊕ V(s(x)), as real values. Proof: x's play is x followed by s(x)'s play, so the cycle and c(x) are the same.
    Also x does not occur on s(x)'s play before c(x):
    - if x is not on the cycle, it never recurs;
    - if x is on the cycle, x ≠ c(x), and the cycle is traversed from x, then s(x)'s play reaches c(x) before it returns to x.
    - So the real prefix of §2 applies.
  - If x = c(x): s(x) lies on x's cycle, and V(s(x)) = (x, ∅, L − 1), with L the cycle length (x is the cycle's top, so no vertex of
    the cycle is above it).
- Step 3 (cycle-node rewards along edges). For every edge x → y: rew(c(y)) ≤ rew(c(x)).
  - c(s(x)) = c(x) in both cases of Step 2. V(y) ⊴ V(s(x)) and clause (i) give rew(c(y)) ≤ rew(c(s(x))).
- Step 4 (chain). Let x_0 → x_1 → … → x_m be a path of H with c(x_i) = c0 for all i ≤ m and x_i ≠ c0 for i < m. Then
  V(x_0) ⊵ₓ x_0 ⊕ x_1 ⊕ … ⊕ x_{m−1} ⊕ V(x_m).
  - For i < m: V(x_i) = x_i ⊕ V(s(x_i)) (Step 2) ⊵ₓ x_i ⊕ V(x_{i+1}), by Step 1, Lemma B (c) and Lemma M. All values involved have
    cycle node c0.
  - Induct from i = m − 1 down to 0, applying Lemma M to the inequality already obtained for the tail, and use transitivity (Lemma
    B (a)).
- Step 5 (cycles with constant cycle node). Let C = (y_0 → y_1 → … → y_{p−1} → y_0) be a simple cycle of H with c(y_i) = c0 for all i,
  and t its top vertex. Then rew(t) ≤ rew(c0), with equality only if t = c0.
  - Case c0 ∈ C. Say y_0 = c0. If p = 1, then t = c0. Otherwise:
    - Step 4 on y_1 → … → y_{p−1} → y_0 gives V(y_1) ⊵ₓ (c0, μ, p − 1), with μ the multiset of y_1, …, y_{p−1} above c0 (a set,
      since C is simple). V(c0) = (c0, ∅, 0).
    - Step 1 at c0 → y_1 gives V(y_1) ⊴ V(s(c0)) = (c0, ∅, L − 1).
    - So (c0, μ, p − 1) ⊴ₓ (c0, ∅, L − 1).
    - If t ≠ c0, then rank t > rank c0, and t is the top element of μ. Then (ii′) is decided at t with μ(t) = 1 > 0. So t is odd and
      rew(t) < rew(c0).
  - Case c0 ∉ C. Every y_i satisfies y_i ≠ c0. Step 4 once around C gives V(y_0) ⊵ₓ y_0 ⊕ y_1 ⊕ … ⊕ y_{p−1} ⊕ V(y_0) =
    (c0, μ_0 + μ_C, ℓ_0 + p), where V(y_0) = (c0, μ_0, ℓ_0) and μ_C is the multiset of C's vertices above c0.
    - If μ_C ≠ ∅: its top element is t, rank t > rank c0, and (ii′) is decided at t (multiplicity μ_0(t) against μ_0(t) + 1). So t is
      odd and rew(t) < rew(c0).
    - If μ_C = ∅: every vertex of C is below c0, so rank t < rank c0. The comparison is (iii): ℓ_0 against ℓ_0 + p with V(y_0) ⊵ₓ. This
      excludes odd c0 (longer would be strictly better), so c0 is even, and rew(t) ≤ pp(t) < pp(c0) = rew(c0).
  - So equality rew(t) = rew(c0) occurs only in the case c0 ∈ C, t = c0.
- Step 6 (conclusion). Fix σ′ and v_0. Let v_0, v_1, … be the σ′-play, with simple cycle C′ and top c′; it is a path of H.
  - By Step 3, rew(c(v_i)) is non-increasing in i. On C′ it is periodic, hence constant. rew is injective, so c(·) = c0 on C′, and
    rew(c0) ≤ rew(c(v_0)).
  - By Step 5 applied to C′: rew(c′) ≤ rew(c0) ≤ rew(c(v_0)).
  - If rew(c′) < rew(c(v_0)), then V_{σ′}(v_0) ◁ V(v_0) by clause (i).
  - Otherwise both inequalities are equalities.
    - So c′ = c0 = c(v_0), c0 ∈ C′ is C′'s top (Step 5's equality case), and c(v_i) = c0 for every i (non-increasing with equal ends).
    - Let v_b be the first visit of the σ′-play to c0. Then v_0, …, v_b are distinct and v_i ≠ c0 for i < b.
    - Step 4 on v_0 → … → v_b gives V(v_0) ⊵ₓ (c0, μ(v_0, …, v_{b−1}), b) = V_{σ′}(v_0). The right side is a real value: a set, the
      vertices before the first visit above c0, and b steps.
    - By Lemma B (c), V(v_0) ⊵ V_{σ′}(v_0). □
- Corollary P1′. Under the hypothesis, V_σ is the pointwise maximum over positional Even strategies. It equals W* of R17 F1, and any two
  strategies without improving edges have the same valuation.

## 4. Hypothesis match with R18's (P) (PROVED, by inspection)
- One-player game:
  - R18's G[X]: X = the vertices with no path to o. Every successor of a vertex of X lies in X, and o ∉ X. In 𝒞^1O every Odd vertex
    other than o has out-degree 1. So G[X] is a one-player game in the sense of §1 (Odd vertices of X have one successor).
  - P-N5-RL's G_τ and G_τ[F_k] fix every Odd vertex to τ (G_τ[F_k]: also proved closed in P-N5-RL §2 (c)).
- Positional σ: R18's σ|X and P-N5-RL's σ′ (BL (b) Step 2b) and σ_k|F_k are positional Even strategies. "Optimal" in R17 F1 / R18 is
  pointwise maximal over positional strategies (VJ00 §4.3), which is P1's conclusion.
- "No improving edge": SPEC S2 (strict ▷ against the successor value Ξσ(σ(v))). In a one-player game Ξσ is the play valuation V_σ (Odd
  has a single strategy; R18 Lemma S (a)). This is P1's hypothesis.
- The order: SPEC S1 / Q1 = the engine's = R15 / R17 / R18's (§1). P1 is stated and proved in exactly this order, lengths at cycle
  nodes included.
  - It is not CAV's coarser "optimal", which drops lengths at cycle nodes (docs/lit/T21-VJ00-check.md).

## 5. READING (not to sign as such; for the Lead and the referees)
- Discharges R18's G-1OA-4:
  - R18 uses (P) "only in Lemma 1 on G[X]";
  - P1 is (P) for G[X] (§4);
  - so R18 (c) would hold without condition, once P1 is signed.
- Discharges P-N5-RL's (P)-conditional items:
  - BL (b) applies (P) to G_τ (Step 2b) and BL (c) to G_τ[F_k];
  - BL (e), FREE-FREEZE, EV, EV+ and TEV-RED depend on (P) only through BL (c);
  - with P1 they become PROVED without condition, once P1 is signed.
  - EQ-END's dependence on CN-LAST is untouched.
- Does NOT cover:
  - the two-player VJ00 Lemma 5.8 "1 ⇒ 2" for games where Odd also chooses; that is R15's G-N5T-3, the correctness of N5's output at
    S5;
  - VJ00's postulates I1 / I2, which fail at cycle nodes (T21).
  - P1 gives only the one-player case of G-N5T-3.
- Relation to R-N5-1P §3 route (a) (REFEREE): that route proves the same statement through VJ00's OverProg, Prop. 5.10 (stated without
  proof in the source) and Prop. 5.6. P1 uses none of them.

## 6. Data (DATA, not proof; experiments/si/p1/p1check.py, logs experiments/si/p1/logs/, in this packet's commit)
- p1check.py:
  - random one-player games (Odd out-degree 1 asserted);
  - all positional Even strategies enumerated (games with > 4,000 strategies skipped);
  - valuations from experiments/si/si.py (read-only);
  - checks that every strategy without an improving edge is pointwise optimal.

| seed | games | n | strategies | without improving edge | violations | non-optimal with an improving edge |
| --- | --- | --- | --- | --- | --- | --- |
| 5101 | 3,000 | 3-9 | 45,581 | 3,336 | 0 | 41,484 (all non-optimal ones) |
| 5102 | 1,500 | 8-12 | 90,705 | 1,930 | 0 | 88,284 (all non-optimal ones) |

- The remaining strategies are optimal but still have an improving edge (761 and 491): the own-cycle-node length-only case (FBW Step 2,
  CN-LAST). P1 does not need it.
- Independent data: R-N5-1P §6 (REFEREE): 7,945 games with n ≤ 6, 8,813 improvement-free strategies, 0 failures. R18 honest limits
  (REFEREE-2): 2,283.
