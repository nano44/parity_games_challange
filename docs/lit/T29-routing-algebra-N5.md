# T29: Daggitt-Griffin's convergence proof, translated to N5 inside one joint λ-phase on 𝒞^1O (L-LIT, 2026-10-24)

Asked by the Lead at 13:43Z (date -u), under D18. This follows T28 rank 1.
- **Scope.** No code runs. L-COMP runs the data checks of T28 lemma (b) and (SEG-1O).
- **Labels.**
  - **PROVED**: proved here from the cited definitions, or proved in the cited source. "Here" means elementary, by L-LIT, unrefereed.
  - **CONJECTURE**: any extra hypothesis or transfer.
  - **READING**: interpretation.
- **Sources.**
  - **Daggitt-Griffin**, "Rate of convergence of increasing path-vector routing protocols", ICNP 2018
    (cl.cam.ac.uk/~tgg22/publications/icnp_2018.pdf, sha256 376beef0…). Page = PDF page.
  - **Their Agda library**, github.com/MatthewDaggitt/agda-routing at commit 241d45ae (read-only clone, nothing run):
    - RoutingLib/Routing/Algebra.agda (sha256 cf2ffbf6…): IsRoutingAlgebra l.100-115, IsPathAlgebra l.129-150,
      IsCertifiedPathAlgebra l.171-184;
    - RoutingLib/Routing/Algebra/Core.agda l.55-65 (IsDistributive, IsIncreasing, IsStrictlyIncreasing);
    - RoutingLib/Routing/VectorBased/Synchronous/PathVector/Convergence/Step6_Proof.agda (sha256 2ea6bad3…): l.43
      `increasing⇒n²-convergence`, l.112 `increasing+distrib⇒n-convergence` (the latter needs `Consistent X`).
  - **N5 side:**
    - docs/new/N5-ssi-global.md SPEC S1 (valuation and order);
    - docs/new/N5-time-box21.md §3.5 (Lemma G) and §3.6;
    - docs/new/N5-1Ocyc-box25.md §5-§6;
    - RESULTS R17 (a)-(c): (V1)/(V2), Lemma P, Theorem PH.

## 0. Verdict (READING, every step labelled below)
1. **The translation is exact, but it lands on the OTHER half of Daggitt-Griffin.**
   - Inside a phase (assumption A1, §1), Even's selection is a path algebra over the ordered group (ℤ², lex). It is
     distributive, and its states are always consistent.
   - It is NOT increasing.
   - R17's Theorem PH (n − 1 value-changing steps per phase on one-player games) is the distributive Θ(n) case of the routing
     literature. DG p.2 states it for semiring algebras; the Agda library's analogue is `increasing+distrib⇒n-convergence`.
   - DG Theorem 1 (n², increasing, NON-distributive) addresses junk routes caused by distributivity violations. N5 has none.
2. **The obstruction is not non-distributivity.** It is a second algebra at admission:
   - the gate values o at θ;
   - the selection values o at w (Lemma G).
   Read in the honest algebra (o at θ), trust routes ARE DG junk routes: non-real, because they pass o, whose advertised route
   τ(o) differs from its honest choice σ̄(o).
3. **DG Lemma 12 fails at o, so Lemma 13's flush fails.**
   - DG junk is inherited from the initial state; no new junk appears after time τ (Lemma 12).
   - N5's junk is regenerated at o in every iteration while θ ◁ w.
   - So trust routes do not grow in length; they persist at fixed length until θ rises (box 25 §5 (4)).
4. **Increasingness can be bought for free** by a Johnson-type potential (§3, PROVED here).
5. **What blocks DG's machinery is that the arc set is state-dependent.** DG's adjacency matrix A is fixed (or changes finitely
   often and then stays fixed). N5's gate filter on arcs entering R depends on θ, π_z and W(σ(x)).
   - The minimal extra hypothesis that restores a DG-type bound counts gate-status changes of entering arcs. That is
     CONJECTURE (H-E), §5.
6. **Correction to T28.** T28 rank 1's "junk routes ≈ trust routes" holds only in the honest frame, and the n² theorem is not
   the one that applies. Expected value: downgrade rank 1 from "proof route" to "precise reformulation". The live content is
   (H-E).

## 1. Setting and dictionary
**Assumption A1** (stated, as D18 allows).
- One joint λ-phase on o-cyclic 𝒞^1O, inside one τ-stretch (τ(o) = b).
- Hypothesis (h) of Lemma G holds.
- Every vertex's cycle node is the same vertex c (single destination). Lemma G's setting remark says this holds, for example,
  in fts_best16's 27-step phase.
- Multi-sink phases need DG's multi-destination reading: one destination per cycle node, compared first by reward. Not done here.

| Daggitt-Griffin (§III, p.2-3) | N5 inside the phase (A1) |
| --- | --- |
| node i, destination j | vertex x, destination c (the phase's cycle node) |
| weight S, choice ⊕ (selective; x ≤ y iff x chosen) | VJ value with cycle node c, Even's order of S1; ⊕ = Even's better of two |
| arc function A_ik ∈ F | extension by x: f_x(v) = x ⊕ v ("π ⊕ a" of Lemma G with π = x) |
| 0 (trivial route), ∞ (invalid) | value of c itself, (c, ∅, 0); ∞ = "route leaves the phase" (other cycle node) |
| path(x), loop ⇒ ∞ (P1-P3) | the play path; a loop closes a new cycle, which is a λ-change, i.e. leaves the phase (Lemma Φ boundary) |
| state X, synchronous σ(X) = A(X) ⊕ I | strategy σ_k with values W_k = V_{σ_k, τ}; N5 step = optimum of G^w over the gate (box 21 Lemma S (c)) |
| real route (Def. 5, p.9): next-hop decisions consistent | every route is a play of (σ_k, τ), so consistent by construction |
| junk route (§V, p.9) | (honest frame only) a route through o, since o's honest choice σ̄(o) ≠ τ(o) while θ ◁ w |

## 2. Hypothesis-by-hypothesis check
| DG hypothesis (Def. 1-2 p.2-3; Agda IsRoutingAlgebra / IsPathAlgebra) | N5 counterpart (A1) | status |
| --- | --- | --- |
| R1-R3: ⊕ associative, commutative, selective (`⊕-assoc`, `⊕-comm`, `⊕-sel`) | Even's choice between two values with cycle node c | **PROVED.** S1's order compares the reward of c (equal here), then the signed weight Σ ±2^rank over P, which is injective on sets, then ℓ. It is a total order on keys, so max is selective, associative, commutative |
| R4: 0 annihilator (`⊕-zeroʳ`) | c's own value (c, ∅, 0) is never replaced inside the phase | **PROVED** by the definition of a joint λ-phase (c stays the cycle node, and c's own valuation is (c, ∅, 0) by S1) |
| R5-R6: ∞ identity and fixed point (`⊕-identityʳ`, `▷-fixedPoint`) | routes leaving the phase | vacuous under A1 (single destination); **PROVED** trivially by adjoining ∞ |
| P1-P3: path algebra (`path-reject`, `path-accept`) | play paths; extending by a vertex already on the path closes a cycle | **READING.** A loop is not "invalid" but a λ-change, i.e. the phase ends. Inside a phase, extension stays on simple paths |
| Distributive (1): f(x ⊕ y) = f(x) ⊕ f(y) (`IsDistributive`) | prefix monotonicity | **PROVED: R17 (a) (V2)** (signed by both referees). Also immediate from §3: extension is translation in an ordered group |
| Increasing (2): x ≤ f(x) (`IsIncreasing`, used by both Agda theorems) | does extending a route by x never make it better for Even? | **FALSE in general, PROVED by hand instances (§3).** It holds exactly on arcs out of x with (x more relevant than c ∧ Ω(x) odd) ∨ (x less relevant than c ∧ Ω(c) even) |
| Strictly increasing (3) | as above, strict | FALSE on the same instances |
| Consistent start (Agda `Consistent X`, needed by `increasing+distrib⇒n-convergence`) | N5 states are strategy-induced | **PROVED** by construction. Fallback states are strategy-induced too |
| Fixed adjacency matrix A (§III-B; after the last topology change) | N5's usable arcs = gate ∪ {σ(x)}; the gate changes with θ, π_z, W(σ(x)) (Lemma G (d1)) | **FAILS.** This is the real gap (§5) |
| synchronous σ (one Bellman-Ford round per iteration) | N5 step = arena optimum over the gate | **PROVED dominance** in the one-player case with full gate: R17 Lemma P (after k steps, W_k ⪰ every path of ≤ k edges). With the restricted gate it fails exactly at withheld entering arcs (box 21 §3.6 (i)) |

## 3. The algebra is a lex-weighted longest-path algebra; increasing fails but can be restored (PROVED here)
- **Lemma A** (from S1). Fix the cycle node c. Map a value (c, P, ℓ) to
  key = (Σ_{u∈P} s(u), ε·ℓ) ∈ ℤ² with the lexicographic order, where:
  - s(u) = +2^rank(u) if Ω(u) is even, and −2^rank(u) if odd;
  - ε = +1 if Ω(c) is odd (longer is better for Even), −1 if Ω(c) is even.
  Then Even's S1 order on values with cycle node c is the order of keys. Extending a simple route by a vertex x not on it adds
  the constant vector g(x) = (s(x)·[x more relevant than c], ε).
- **Proof.** S1: compare the reward of c (equal), then the signed weight of P, then ℓ with the stated parity rule. P only
  ever gains vertices more relevant than c, one per extension. □
- **Corollary A1 (increasing fails).** Even prefers larger keys, so DG's "x ≤ f(x)" (f(x) never chosen over x) reads
  "g(x) ≤ 0 in lex".
  - **Instance I1.** Vertex c with priority 1 and a self-loop; Even vertex x with priority 0 and the single edge x → c. Then
    ε = +1 and g(x) = (0, +1) > 0: x's route (c, ∅, 1) beats c's extension rule.
  - **Instance I2.** c with priority 2 and a self-loop; Even vertex x with priority 4 and edge x → c. Then g(x) =
    (+2^rank(x), −1) > 0.
  - Both are PROVED from S1 by hand; no code is needed.
  - The fleet's pinned instances: any phase whose cycle node is odd has failures at every vertex less relevant than c. L-COMP
    can name the first pinned one; not run here.
- **Lemma B (increasingness restored by a potential).** Let φ(x) be any key-valued function with φ(c) = 0, for instance the
  optimum keys of G^w in the phase. Reweight the extension constants as g′(x → z) = g(x) + φ(z) − φ(x).
  - All routes from the same x to the same terminal shift by the same constant (φ(terminal) − φ(x)). So every comparison N5
    makes, gate or selection, is unchanged. That includes routes ending at the o-terminal valued θ or w: both shift by
    φ(o) − φ(x).
  - If φ is the optimum of a game, then g′ ≤ 0 on every arc (the Bellman inequality), so the reweighted algebra is increasing.
  - Proof: (ℤ², lex) is an ordered abelian group, so translation preserves order; the Bellman inequality holds at the optimum. □
- **Consequence (READING).** The routing-algebra hypotheses R1-R6, distributivity, increasingness (after reweighting) and
  consistency all hold for the selection algebra in G^w. That is precisely why R17 gets n − 1. DG Theorem 1's extra power
  (non-distributive algebras) is not needed. Nothing in DG addresses N5's actual deviation.

## 4. Where DG's §VI proof goes through and where it breaks
Walk-through, against DG §VI-A/B (p.7-11).
- **Lemma 4 (p.7) and Lemma 7 (p.9, C_t is a tree):** go through (PROVED), since routes are plays (consistency).
- **Lemma 10 (C_t ⊆ R_t):** trivial in N5's G^w frame, where every node is real.
- **Lemma 11 (p.10), real nodes outside P(τ) do not threaten e_min:** uses increasingness. It goes through after Lemma B's
  reweighting, with e_min defined in the selection order (CONJECTURE that nothing else is needed; the case split is the same).
- **Lemma 12 (p.10), every dangerous route at t + 1 extends a dangerous route at t.** In the honest frame, where trust routes are
  the non-real ones, this FAILS at o.
  - o's selection route (via τ(o) = b, value w) is not o's honest decision (σ̄(o), value θ) as long as θ ◁ w.
  - So o is a non-real root at every time step, not just at the start. DG's proof of Lemma 12 needs the non-real k at t + 1 to
    take its route from a neighbour l that was non-real at t. For k = o the route is "fresh junk" generated by τ.
  - In the G^w frame there is no junk at all (all real), and Lemma 12 is vacuous.
- **Lemma 13 (p.11), D_{τ+n} = ∅:** FAILS in the honest frame, because it rests on Lemma 12's length growth. A trust-routed z
  keeps π_z through o at constant length while θ is constant. This is the trust-mode persistence of box 25 §5 (4) (i)-(iii).
  - Vacuous in the G^w frame.
- **Lemma 14-16 and Theorem 1 (p.11), the minimal cut arc is adopted within n:** in the G^w frame the "next node" i_min can
  still be blocked. The blocker is no longer a dangerous junk route; it is the gate. The cut arc e_min may be a WITHHELD
  entering arc (Lemma G (d1): π_z ⊕ θ ⊴ W(σ(x)) ◁ π_z ⊕ w), invisible to the selection.
  - This is box 21 §3.6 (i) in DG's vocabulary: "Case B fails exactly at a withheld edge".

So, in either frame, the break is the admission filter.
- In the honest frame it appears as sustained junk at o (Lemma 12 fails).
- In the selection frame it appears as a missing cut arc (Lemma 14 fails).

## 5. Modified algebras and the minimal extra hypothesis
**M1, the honest algebra: o valued at θ in both gate and selection.**
- The step is then the optimum of the one-player game G^θ over G^θ's improving set. That is R17's switch-best on G^θ, so ≤ n − 1
  value-changing steps per θ-constant stretch (R17 Cor. 1 applied to G^θ).
- READING: G^θ is G with o's edge fixed to σ̄(o), a one-player game while σ̄(o) is constant.
- This is NOT N5. It is the variant that box 25 §5 (6) says "would be R17-like". It is a design option for L-SI, not a proof
  of N5.

**M2, N5 itself: two-origin selection with a state-dependent import filter.**
- Treat o as a second origin that advertises the constant value w inside a (θ, w, τ, λ)-constant stretch (box 21 §3.6's
  stretch).
- The selection algebra is then a fixed, distributive, consistent, increasing-after-reweighting path algebra on the arcs it
  may use.
- The usable arcs are gate ∪ {σ_k(x)}. They form a time-varying adjacency matrix A_k. The only entries that vary are arcs
  entering R (Lemma G (d1)), whose admission depends on π_z, θ and W(σ_k(x)).
- In routing terms, this is an import filter at x that depends on x's own current route. That is outside the algebraic model
  of DG, Sobrinho and Griffin-Shepherd-Wilfong, where policies are fixed arc functions.

**Minimal extra hypothesis (CONJECTURE (H-E)).**
- Define:
  - E = the number of (step, arc) pairs inside a fallback-free (θ, w, τ, λ)-constant stretch at which an arc entering R
    changes gate status (withheld ↔ admitted);
  - D_admit = the length of the longest run of steps in which A_k is constant.
- Then the stretch has at most (E + 1)·(n − 1) value-changing steps.
- Why this is the right shape: on every interval where A_k is constant, the dynamics is a DG-model protocol on a fixed matrix
  with a consistent start, and Lemma P (R17 (b)) gives n − 1. DG's "from every starting state" robustness lets each change of
  A_k act as a restart (READING).
- Open sub-step: Lemma P on a fixed restricted matrix needs the arena to contain the cut arc. That holds when A_k is constant,
  since the gate equals A_k's improving set by definition. The step to prove is the bookkeeping across changes.

**Then (CYC) and (TRUST) reduce to counting E (READING).** By Lemma G (d1), an entering arc (x, z) changes status only when one
of three things changes:
- θ: monotone, (CYC);
- π_z: a route change inside R, one-player per N5-STANDDOWN §12d (ii);
- W(σ(x)): an x improvement, or a drop at a fallback, (FB-1O).
Hence, as a CONJECTURE:
    E ≤ (#entering arcs) · (1 + C_θ + C_π + C_x),
with C_π = route changes in R and C_x = value changes of x. This makes the dependence of SEG-1O on (CYC) and the one-player
counts explicit. It does not bound C_θ.

**Lemma 13's flush is not restorable without assuming the conclusion (READING).** A hypothesis of the form "trust routes are
flushed within n steps while θ is constant" is equivalent to "no trust deadlock longer than n". That is (TRUST) itself. So the
routing route offers no flush lemma; its contribution is (H-E) and Lemma B.

## 6. What L-COMP's data checks mean under this translation
- **T28 lemma (b)** ("a trust route's length grows by one per transition until flushed"). By §4 it should FAIL: lengths stay
  constant while θ is constant. A failure confirms the sustained-junk reading. It does not kill (H-E).
- **(SEG-1O)** (transitions between consecutive θ-changes ≤ n − 1). (H-E) predicts ≤ (E + 1)(n − 1). The decisive extra column
  is E per stretch; box 21 §3.6's table (longest stretch 11, 5, 11 at n 16, 16, 24) is consistent with small E.
  - Suggested column for L-COMP: per stretch, E (gate-status changes of R-entering arcs) next to the stretch length.

## 7. Open, stated plainly
- (H-E) is a CONJECTURE.
- C_θ, i.e. (CYC), is untouched by this translation. The routing literature bounds convergence after the policy stops
  changing; θ is the policy parameter here.
- G-N5-TIME stays OPEN. No running-time claim is made (D1).
