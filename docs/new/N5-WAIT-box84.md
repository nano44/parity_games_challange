# N5-WAIT (box 84): R3-POLY through R135's WAIT-CYCLE count. WAIT-CYCLE′ (all self-routed blocks except one length-only class E0) and E0-BOUND (≤ n E0 returns per edge) PROVED (lane); Theorem TRIPLE-RED splits R3-POLY into REG returns (the triple count) and FREE returns; in the corpus FREE returns are 84% of returns and REG ≤ 3 per edge per W-run. No polynomial pattern bound: exact obstruction is the CHARGE recursion
L-NEW successor 38 (Opus 5.5), D14 / D18, Lead reading L40. Lead brief 2026-10-30 (after 12:02Z): «YOUR TARGET: R3-POLY on the PROOF side,
through L-RED successor 33's R135 … (1) State R3-POLY via that triple count precisely. (2) Prove a polynomial bound on the number of route
patterns a signal route can take within one W-run … Otherwise give the exact obstruction with an instance.» Written 2026-10-30 12:05Z-12:40Z
(date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources read and setting
- l-red fc450c7d docs/red/R135-desync-gate.md (§3 upward waits, §4 Lemma WAIT-CYCLE and its proof, §5, Addendum 1); experiments/red/desync/
  wcrand.py (its block test, reused in experiments/new/box84/waits.py).
- docs/new/N5-ssi-global.md SPEC S1-S5 (S1 order, σ̄ = Odd's pointwise-optimal counterstrategy, S2 offers, S4a step, Termination paragraph:
  Ξ_σ′ ⊵ Ξ_σ along N5). RESULTS R89 (W-run, Lemma SUCC-MON: Ξ_t(σ_t(y)) non-decreasing; Lemma LATE-RISE). RESULTS R93 / docs/new/
  P-N5-WCH-box79.md §4.1 Lemma NEW-BOUND (|F| ≤ m_E + returns of F), §4.2 Theorem RET-WCH (returns of v to e ≤ WCH_F(e) + TT_F(v, e)).
- docs/new/N5-R3-box83.md addendum (the exact CONJECTURE R3-POLY, quoted in §1).
- Notation: Ξ_t, σ̄_t, Iσ_t at state t of an N5 run; rank, p′, rew as in [S1-rank] / [S1-ord]; λ(x) the cycle node of a valuation x.
  "u is above c" means p′(u) > p′(c). Valuation keys compare (rew(λ), signed path weight, ±ℓ) lexicographically; rew is injective in the
  cycle node and the signed weight is injective in the path set (distinct powers of 2), so for fixed (λ, P) the valuations with that
  (λ, P) form an INTERVAL of the total order (Fact CONVEX, used in §3).

## 1. Definitions and the statement (Lead step (1))
- SELF-ROUTED BLOCK of (X, g) at state t. X Even, g ∈ succ(X), g ≠ σ_t(X), (X, g) ∉ Iσ_t, and the (σ_t, σ̄_t)-play from g reaches X with
  the vertices strictly before X pairwise distinct; π := those vertices (g first; π = ∅ iff g = X). If X lies on the cycle Z* of its own
  (σ_t, σ̄_t)-play, π is also required to avoid Z* (the play from g ENTERS Z* at X). The ROUTE PATTERN is σ_t restricted to the Even
  vertices of π. (R135 §4 required X ∉ Z*; this box keeps X ∈ Z*, see Lemma WAIT-CYCLE′.)
- c* := λ(Ξ_t(X)). The block is E0 if c* = X and every vertex of π ranks below X; otherwise it is REG.
- RETURNS (R93's sense). In a W-run F = [a, b] (R89), a return of X to g is a transition t2 − 1 → t2 of F with σ_t2(X) = g ≠ σ_(t2−1)(X)
  where X held g at some earlier state of F; s → s + 1 is X's last leave of g before t2 (s ≥ a). Class of the return:
  REG if some state in [s + 1, t2 − 1] has a REG block of (X, g); else E0 if some state there has an E0 block of (X, g); else FREE.
  REG_F(X, g), E0_F(X, g), FREE_F(X, g) count them.
- CONJECTURE R3-POLY (box 83 addendum, verbatim): «there is a polynomial p such that, on every game with n vertices, from every start pair
  (σ_0, τ_0), every W-run F of N5 (RESULTS R89) and every vertex e have WCH_F(e) ≤ p(n), where WCH_F(e) is the number of transitions of F
  at which W(e) changes.»
- CONJECTURE ALT-POLY (the triple count, precise form): REG_F(X, g) ≤ p(n) for every W-run F, every start pair and every Even edge (X, g).
  (R135 §5 counts (X, g, pattern) triples. §2 shows a REG return needs a pattern different from EVERY earlier REG block pattern of (X, g);
  the triple count bounds REG returns, but distinct patterns are not the right potential: DATA §5, 25 patterns versus 3 returns.)
- CONJECTURE FREE-POLY: FREE_F(X, g) ≤ p(n) likewise.
- Theorem TRIPLE-RED (§4) proves R3-POLY ⇐ ALT-POLY ∧ FREE-POLY, and R3-POLY ∧ (TT polynomial) ⇒ ALT-POLY ∧ FREE-POLY.

## 2. Lemma WAIT-CYCLE′ (PROVED, lane): R135's WAIT-CYCLE for every REG block, X on its own cycle included
- Statement. Let (X, g) have a REG block at t1 with route π and pattern P. Then at NO state t > t1 of the run (any transition kind:
  S4a, S4b, S4c) do σ_t(X) = g and σ_t|Even(π) = P hold together.
- Claim A: the simple cycle C := X → g → π → X has top vertex z (max p′ on π ∪ {X}) with rew(z) < rew(c*).
  - Case 1, X not on its own cycle Z*. The play from g is π, X, then X's play, and π ∪ {X} is disjoint from the play of σ_t1(X) (that play
    never returns to X, and π cannot meet it and still reach X). Write Ξ_t1(σ_t1 X) = (c*, P′, ℓ′). Then Ξ_t1(g) = (c*, P′ ∪ A, ℓ′ + 1 + |π|),
    A := the vertices of π ∪ {X} above c*, disjoint from P′. If A ≠ ∅ its top m decides the comparison with Ξ_t1(σ_t1 X); the block
    (Ξ_t1(g) ⊴ Ξ_t1(σ_t1 X)) forces Ω(m) odd; z = m, and rew(m) = −p′(m) < rew(c*) (c* even: rew(c*) > 0; c* odd: p′(m) > p′(c*)).
    If A = ∅ the path sets are equal and Ξ_t1(g) is longer; if c* were odd that is better for Even, contradicting the block, so c* is
    even; c* ∉ C, every vertex of C is below c*, so rew(z) ≤ p′(z) < p′(c*) = rew(c*).
  - Case 2, X ∈ Z*, X ≠ c*. π avoids Z* by definition, X's way to c* runs inside Z* (all below c*), so Ξ_t1(σ_t1 X) = (c*, ∅, ℓ′) and
    Ξ_t1(g) = (c*, A, ℓ′ + 1 + |π|) with A := the vertices of π above c* (X is below c*). The two sub-cases of Case 1 apply verbatim
    (c* ∈ Z* \ {X} is not on C).
  - Case 3, X = c*, REG. Then σ_t1(X)'s play runs round Z* back to X, all below X: Ξ_t1(σ_t1 X) = (X, ∅, |Z*| − 1). Ξ_t1(g) = (X, A, |π|)
    with A := the vertices of π above X, A ≠ ∅ (REG). Its top m is odd (else g would be offered), z = m, rew(m) < rew(X) as in Case 1.
  - E0 (X = c*, A = ∅) is exactly the complement: there C's top is X itself and rew(z) = rew(c*). Claim A fails only there.
- Proof of the lemma (R135's argument, unchanged). Suppose t > t1, σ_t(X) = g, σ_t|Even(π) = P. Let ρ := σ̄_t1 on the Odd vertices of π and
  σ̄_t elsewhere. The (σ_t, ρ)-play from X is C repeated, so val(σ_t, ρ)(X) has cycle node z. σ̄_t minimises every vertex's valuation at
  once ([S1-val]), so Ξ_t(X) ⊴ val(σ_t, ρ)(X) and rew(λ(Ξ_t(X))) ≤ rew(z) < rew(c*) = rew(λ(Ξ_t1(X))); the order compares the cycle reward
  first, so Ξ_t(X) ◁ Ξ_t1(X). Ξ is non-decreasing along N5 (SPEC Termination; S4b and S4c included). Contradiction. □
- Corollary DEAD-CYCLE (PROVED, lane; the pattern-free form). For any simple cycle C, any vertex Y ∈ C and any state t1: if rew(top C) <
  rew(λ(Ξ_t1(Y))), then C is σ_t-consistent (every Even vertex of C points along C) at no state t ≥ t1. Same proof. WAIT-CYCLE′ is the
  case where a REG block exhibits such a C through X and g.
- Corollary CHARGE (PROVED, lane). If a return of X to g at t2 is REG, with REG block at t1 ∈ [s + 1, t2 − 1] and route π, then some Even
  y ∈ π has σ_t2(y) ≠ σ_t1(y), so y switches at some transition of [t1, t2 − 1]; y is a TRANSITIVE READER of X at t1 (its σ̄_t1-play
  reaches X). In particular a REG return needs an Even vertex on π.
- DATA. waits.py (whole runs, every state): corpus 1132 runs (box 83's lists), 434,925 REG and 3,789 E0 blocks (32,455 of all blocks
  have X on its own cycle, i.e. lie outside R135's test), VIOLATIONS 0, DEADC (Claim A fails on a REG block) 0; E0 same-pattern takes 0. Random games
  (n 6-12, 2000 each): VIOL 0, DEADC 0. The first draft of the block test let π meet Z* before X: 68 DEADC at n 8 (instance: prio
  [5,4,6,1,3,7,2,0], X 3, g 6, π = [6, 1] with 1 = c*); those plays join X's cycle at c*, not at X, and are not blocks in the §1 sense.

## 3. Lemma E0-BOUND (PROVED, lane): E0 returns are at most n per Even edge over the whole run
- Statement. For every Even edge (X, g), the returns of X to g whose class is E0 (in any W-run, or over the whole run with the same
  classification) number at most n.
- Proof. Let the E0 returns be at t2^1 < t2^2 < …, with E0 blocks at t1^i ∈ [s^i + 1, t2^i − 1]. At an E0 block X = λ(Ξ(X)), the play from
  g is π then X (entering X's cycle at X), and π is below X, so Ξ_(t1^i)(g) ∈ K := {(X, ∅, ℓ) : 0 ≤ ℓ ≤ n − 1}. At the switch t2^i − 1 → t2^i,
  (X, g) ∈ Iσ (S4a and S4c take only offered edges, S4b does not move σ), so with R89 SUCC-MON:
  Ξ_(t2^i − 1)(g) ▷ Ξ_(t2^i − 1)(σ X) ⊵ Ξ_(t1^i)(σ_(t1^i) X) ⊵ Ξ_(t1^i)(g) (the last step is the block). So Ξ(g) rises strictly inside
  [t1^i, t2^i − 1]. Ξ(g) is non-decreasing and K is an interval (Fact CONVEX), so Ξ(g) stays in K on [t1^1, t1^last], and the strict rises
  of the first last − 1 returns are distinct moves inside K, which has n elements: last − 1 ≤ n − 1. □
- READING. E0 is the only place where WAIT-CYCLE′ is silent, and it is a pure length race at a fixed cycle node: harmless.
- DATA (altcheck.py, random n 6-20, 1500 runs each): E0 alternations ≤ 1 per (X, g); RISE (LATE-RISE form) 0 violations.

## 4. Theorem TRIPLE-RED (PROVED, lane; a REDUCTION): R3-POLY splits into REG returns (the triple count) and FREE returns
- Statement. For every N5 run and every W-run F: max_e WCH_F(e) ≤ |F| ≤ m_E + Σ_(X, g) (REG_F + E0_F + FREE_F)(X, g)
  ≤ m_E(n + 1) + Σ_(X, g) REG_F(X, g) + Σ_(X, g) FREE_F(X, g).
  Hence ALT-POLY ∧ FREE-POLY ⇒ R3-POLY. Conversely REG_F + E0_F + FREE_F = RET_F(X, g) ≤ WCH_F(g) + TT_F(X, g) (R93 RET-WCH), so R3-POLY
  together with a polynomial bound on TT (the TIE residual) implies ALT-POLY and FREE-POLY.
- Proof. WCH_F(e) ≤ |F| since each counted change is at a transition of F. |F| ≤ m_E + returns of F is R93 NEW-BOUND (every transition of
  a W-run moves σ: τ is constant and there is no S4c, so σ′ = σ would force a fallback). Every return has exactly one class (§1). E0_F ≤ n
  per Even edge (§3), and there are m_E Even edges. □
- What the triple count buys. By CHARGE every REG return is paid by a switch of a transitive reader on its route (R135's "upward wait"
  in proof form). FREE returns are untouched by WAIT-CYCLE′: while X was away, g was never blocked by a play through X. They include
  "offered but not taken by S4a's one-player optimum", blocks whose route avoids X (R135 §2's lateral gates; Addendum 1's parity opener),
  and R134's GAP-IN-PREFIX / TWO-SOURCE blocks.
- DATA (retclass.py, box 83's corpus, 1132 runs; experiments/new/box84/retclass_*.txt): 33,794 switch events, of which 6,265 returns:
  REG 1,005, E0 0, FREE 5,260. Per (F, X, g) maxima: REG 3 (pftheta34_n32, pft35_n48), FREE 17 (topfix_n10, n 210). The largest
  WCH_F(e) of the corpus (48, ladderd0_k48_n156 from its start) has 0 returns: its W-changes come from 99 first adoptions (breadth,
  bounded by m_E). NEW-BOUND form 0 violations.

## 5. Step (2): a polynomial bound on route patterns? Not proved. The exact obstruction
- DATA (waits.py, per W-run). Distinct REG patterns per (X, g) per W-run reach 25 at pftheta34_n32 (n 32), with only 3 REG returns there
  (max alternations per (X, g) per W-run in the whole corpus: 3). Patterns over-count: most blocked patterns never precede a take.
  The right count is REG returns, and WAIT-CYCLE′ only says each one needs a pattern change (CHARGE).
- Bound available (PROVED, lane, trivial): distinct patterns of (X, g) in F ≤ 1 + the switch events in F of the Even vertices on its
  routes, and REG_F(X, g) ≤ that same number of switch events (CHARGE; the intervals [t1, t2 − 1] of distinct returns of one edge are
  disjoint).
- OBSTRUCTION (exact). Each tool listed in the brief turns a REG return of X into a SWITCH of a transitive reader y of X:
  - WAIT-CYCLE′ / CHARGE (here);
  - LATE-RISE / SUCC-MON: a strict rise of Ξ(g);
  - PREFIX / TWO-SOURCE (l-red 1c8d8667 notes "Successor 32 PARK"; R132 §2): the rise is sourced on g's play prefix, i.e. again on readers
    or on g's own subtree;
  - GATE-COLLAPSE / TWIN-SYNC (boxes 80, 82): they remove lateral and twin desynchronisation, so they act on FREE returns, not on the charge.
  A switch of y is either a first adoption (≤ m_E in total) or a return of y, which is again REG / E0 / FREE. So the inequalities close
  into a system of the form REG(X) ≤ Σ_(y reads X) [deg(y) + REG(y) + E0(y) + FREE(y)], with no potential decreasing along "reads".
  The same switch of y may pay for REG returns of several X that y reads transitively (FAN; random data FAN ≤ 2, forced sharing FAN1 = 1).
  A system of this shape has exponential solutions along a reader chain, which is box 80's ladder_k recursion (level j waits for its
  reader at level j + 1). So no polynomial pattern bound follows from these tools alone: one more ingredient must give "reads"
  a potential, or bound FAN by 1 along chains with an additive (not multiplicative) count.
- No instance in real N5 shows the system's exponential solution: the corpus has charge depth ≤ 2 (altcheck.py, chains of REG returns each
  charged to a switch that is itself a REG return) and REG ≤ 3 per edge per W-run. The obstruction is to the proof route, not a kill of
  R3-POLY.
- D18 import: none attempted with an opened source in this box. (A natural candidate is a matching / Hall-type charging that makes the
  charge injective along chains; I have not found a statement of the needed kind and do not cite one.)

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box84/waits.py (blocks, WAIT-CYCLE′ test, per-W-run pattern / alternation maxima), altcheck.py (E0-BOUND, RISE,
  CHARGE, depth, fan), retclass.py (TRIPLE-RED classes), run.sh / run2.sh, waits_*.txt and retclass_*.txt (corpus); check.sh "box 84".
- FINDINGS:
  1. PROVED (lane) Lemma WAIT-CYCLE′: R135's WAIT-CYCLE holds for every REG block, including X on its own cycle (π entering at X); the
     only exception is E0 (X its own top cycle node, π below X). Corollaries DEAD-CYCLE (pattern-free) and CHARGE. DATA 0 violations in
     434,925 corpus REG blocks.
  2. PROVED (lane) Lemma E0-BOUND: ≤ n E0 returns per Even edge over the whole run.
  3. PROVED (lane) Theorem TRIPLE-RED: R3-POLY ⇐ ALT-POLY (REG returns, the triple count) ∧ FREE-POLY; ⇒ holds given a polynomial TT.
  4. DATA: FREE returns are 84% of corpus returns (5,260 / 6,265); REG ≤ 3 per edge per W-run; distinct patterns up to 25 at n 32;
     the corpus's largest WCH (48) has no returns at all.
  5. CONJECTURES ALT-POLY, FREE-POLY OPEN; R3-POLY OPEN. Step (2) not proved; exact obstruction: the CHARGE recursion along "reads"
     (§5), no instance in real N5.
- NEEDS: none from the owner. Lead: R135's triple target covers only REG returns; FREE returns (lateral, not-taken, gap blocks) need
  their own line. L-RED could aim R136 at FREE returns (largest 17 per edge per W-run, topfix_n10).
