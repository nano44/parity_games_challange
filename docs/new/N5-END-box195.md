# Box 195 ENDGAME: after its first fallback, N5′-xi (and N5) on Γ3(G) stops after exactly two more iterations, for every genome
L-NEW successor 63 (Opus 5.5), D1 / D14 / D18. Lead 02:22Z: «Box 195 ENDGAME-3 … Write it with every step tied to the SPEC S4a / S4c text
and the landed TAU3 / R117 K-gadget clauses, quoted by script». Target: L-RED R221 §10-§11 CONJECTURE ENDGAME-3 and skeleton E0-E4
(docs/red/R221-quiet.md, claude/l-red 86a7a7a8). Credit: the statement, the skeleton and the family generator are L-RED 56's.
Labels: PROVED (lane, L-NEW 63, unrefereed) / PROVED-CONDITIONAL / READING / DATA. Nothing here is a TARGET.md claim.

## 0. Results
- **Theorem ENDGAME-3 (PROVED, lane; every genome; no REACH3-CYC, no acyclicity).** For every genome G, the N5′-xi run from S3 on Γ3(G)
  terminates, has exactly one fallback, at some iteration F ≥ 1, and makes exactly F + 2 iterations. Every iteration before F is an S4a
  iteration that keeps K0 → pA, K1 → s, K3 → K2 and τ.
- **Theorem ENDGAME-3-N5 (PROVED, lane).** The same for N5 itself (SPEC S1-S5): the proof uses the S4a step only through «every
  pointwise optimum of the arena makes this choice», at vertices where that choice is unique.
- **Corollary EXACT-L (PROVED from landed premises).** For every genome G with an ACYCLIC Ξ-graph, N5 from S3 on Γ3(G) makes exactly
  L(G) + 3 iterations (R117 REACH3: transitions 1, …, L(G) are not fallbacks and transition L(G) + 1 is one, so F = L(G) + 1). So on
  Γ3 of acyclic genomes, N5's iteration count is polynomial iff L(G) is: R117's Corollary REAL-IDEAL-S3 (one direction) becomes an
  equivalence on this family (n = N + 7M + 10).
- **Corollary END-T3 (PROVED-CONDITIONAL on REACH3-CYC, R118 (k)).** For every genome, N5′-xi from S3 on Γ3(G) makes exactly T3 + 3
  iterations (F = T3 + 1).
- **READING (not claimed).** With the Γ3 transfer of T-QUIET / UP-T (box 194; R221 §7's reading that QUIET's proof uses only DOM and
  STRICT, which hold for Γ3's pre-fallback Howard run; not signed), T3 + 3 is polynomial in N + M for [E-LEV] genomes with bounded U(G).

## 1. Premises (quoted by script: experiments/new/box195/quotes195.py; trunk 51eb6534 docs/RESULTS.md, docs/new/N5-ssi-global.md,
docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md)
- [SPEC] (docs/new/N5-ssi-global.md):
  - «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once).»
  - «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal
    counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.»
  - «S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»
  - S3 / FIX 1: Even: «highest even priority, else lowest odd priority»; «Odd's v (the rule on G^d), in G's terms: highest ODD Ω(w), else
    lowest EVEN Ω(w)».
  - «S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together)»
  - S4a: «If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge
    to τ(v).»
  - S4b: «b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v.»
  - S4c: «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈
    Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations.»
  - «FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ)»; «S5 Stop when Iσ = Iτ = ∅.»
- [N5XI] RESULTS R118: N5′-xi is SPEC S1-S5 «with ONE change in S4a» (box 190's tie rule); the frozen packet it cites
  (docs/new/P-N5-XICYC.md l. 45-47): «SPEC S1-S5 with ONE change in S4a. At every Even v with |A(v)| ≥ 2 that is not its own H-cycle
  node, σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}. Ties go by SPEC's choice, then the larger index.
  Here A(v) = {σ(v)} ∪ Iσ(v).» (W* = the values of S4a's arena optimum in H.)
- [1E-N3] RESULTS R57 (b) as landed in R104: «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new,
  S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that
  arena, before S4c)».
- [DEF] RESULTS R104, definitions only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»; options
  «each with a W-target of level lev(x) − 1 (none at level 0)»; «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u,
  or to u alone»; «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»; «an unused even
  self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»; «a closed core
  u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»; «with start σ =
  the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2».
- [G3] RESULTS R117, definition of Γ3: «the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on
  K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on
  every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)»;
  Lemma S3-START: Γ3 «has S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START)». The Ω of each pad
  (pA, s, r, pβ 0; q, pe, pb 1; m 2 or 0) is P-N5-REACH §3, the packet R117 lands.
- [TAU3] P-N5-REACH §6.4 (signed for every genome: R118 «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome»):
  «In the standard state, Iτ = ∅, so S4b leaves τ unchanged.»
- [TERM] RESULTS R15: «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» and
  (c) «≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺. Consequence: no
  strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule».
- For the corollaries only: RESULTS R117 REACH3 (quoted in §6) and RESULTS R118 (k): «N5′-xi from S3 on Γ3(G) visits only standard
  states and makes Howard steps at the movers until its first fallback, at iteration T3 + 1» («Theorem REACH3-CYC, CONDITIONAL on
  P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome»).
- Not used: ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c) (the pads' effect is computed directly below), T-QUIET, any L-RED lemma.

## 2. Facts about Γ3 used below (from [DEF] and [G3])
- (R) Rank order, by Ω first: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β (≥ 6) < every e < c_W (top) < K0 (top + 2)
  < K3 (top + 3). So a P-set holds only vertices above its cycle node in this order; K0 is the most relevant EVEN vertex, so a value
  with cycle node K0 has the largest reward of all values, and K1's reward −p'(K1) is below K2's −p'(K2).
- (C) The core Kc := {K0, K1, K2, K3, pA, s, q, r} is closed: K0 → {K1, pA}, pA → K3, K3 → {K1, K2}, K1 → {q, s}, q → K0, s → K1,
  K2 (Odd) → {r, K2}, r → K1. Values on Kc depend only on the K-config κ(σ) := (σ(K0), σ(K1), σ(K3)) and on Odd's choice at K2.
  Write κ0 := (pA, s, K2), κ1 := (K1, s, K2), κ2 := (K1, q, K2), κ3 := (K1, q, K1).
- (S) S3's pair (S3-START, or FIX 1 directly): κ0; β_g → xt(g) if xt(g) is a mover (else its only successor pb_g); τ0 := pe_g at every
  gate g and K2 → K2.
- (W) From a gate g of a level-ℓ mover, the play that takes pe at every gate passes g, pe_g, e_g, then (ℓ ≥ 1) a mover of level ℓ − 1,
  its pad, its chosen gate, …, and ends in c_W's loop after exactly 5ℓ + 3 steps, whatever Even plays at movers (W-targets have level
  lev − 1; level-0 e's go to c_W). It meets no β and no core vertex, and no vertex above c_W: its value is (c_W, ∅, 5ℓ + 3).
- (H) If v is not its own H-cycle node and some w0 ∈ A(v) has v ⊕ W*(w0) = W*(v) while every other w ∈ A(v) gives v ⊕ W*(w) ≠ W*(v),
  then σ_new(v) = w0, in N5 and in N5′-xi. (N5: σ_new is a pointwise optimum of H ([1E-N3]); v's H-value is v ⊕ the value of σ_new(v),
  so σ_new(v) ∈ TIE(v) = {w0}. N5′-xi: σ_new(v) ∈ TIE(v) by [N5XI].) Where |A(v)| = 1 the choice is forced in both.

## 3. Lemma E0 (τ is fixed) PROVED
Every state of the run has τ = τ0, and Iτ = ∅ there.
Proof. Iτ is computed on G^d from τ alone ([SPEC] «Iτ computed there»; τ̄ is Even's optimal counterstrategy to τ), so Iτ is the same at
every state with τ = τ0; by [TAU3] (at the standard state, whose τ is τ0) it is ∅. S4b changes τ only if Iτ ≠ ∅; S4c changes τ only
when Iσ = ∅, and then only along Iτ. Induction from the start (S). ∎

## 4. Lemma E1 (the core is frozen until a fallback) PROVED
In every state with K-config κ0 and τ0: (a) Iσ ∩ (edges out of K0, K1, K3) = {(K0, K1)}; (b) every S4a σ_new (N5 or N5′-xi) has
K-config κ0.
Proof.
- Odd at K2: r gives K2 → r → K1 → s → K1 …, node K1; the loop gives node K2. Reward −p'(K1) < −p'(K2) (R), so σ̄(K2) = r in every
  pointwise optimum ([1E-N3]).
- Values (the same as R117 K3 (a)): K1 (K1, ∅, 0); s (K1, ∅, 1); r (K1, ∅, 1); K2 (K1, ∅, 2); K3 (K1, {K3}, 3); pA (K1, {K3}, 4);
  K0 (K1, {K0, K3}, 5); q (K1, {K0, K3}, 6) (P by (R): K0, K3 are the only core vertices above K1).
- (a) K0: Ξ(K1) vs Ξ(pA): same node, P differ by K3, odd: K1 better: improving. K1: q vs s: P differ by {K0, K3}, top K3 odd: q worse.
  K3: K1 (length 0) vs K2 (length 2), node K1 odd: the longer is better for Even ([VJ] order in [SPEC] S1): not improving.
- (b) H: A(K0) = {pA, K1}, A(K1) = {s}, A(K3) = {K2}, K2 → τ0(K2) = K2. H-play via pA: K0 → pA → K3 → K2 → K2 …, node K2; via K1:
  K0 → K1 → s → K1 …, node K1. K0 is on no H-cycle. W*(K0) has node K2 (the larger reward), so K0 ⊕ W*(K1) (node K1) ≠ W*(K0) and (H)
  gives σ_new(K0) = pA; K1, K3 are forced. ∎
Corollary. The K-config changes only at a fallback; in every state before the first fallback it is κ0 and Iσ ∋ (K0, K1) ≠ ∅.

## 5. Lemmas E2-E4 PROVED
**Lemma E2 (the first fallback).** If iteration F is the first fallback, its input state has κ0 and τ0, it is an Even fallback, and its
result has K-config κ1 and τ0.
Proof. Input: E1's corollary and E0. Iσ ≠ ∅ (E1 (a)), so S4c switches every Even vertex with an improving edge to its best improving
edge and keeps τ (FIX 3). On the core only K0 has an improving edge, (K0, K1) (E1 (a)): κ1. ∎

**Lemma E3 (the top cycle closes).** From every state with K-config κ1 and τ0 (any σ at movers and β's), the next iteration is an S4a
iteration (not a fallback) whose result has K-config κ2.
Proof.
- Odd at K2: r gives node K1 (K1 → s → K1), the loop node K2: σ̄(K2) = r as in E1.
- Values: K1 (K1, ∅, 0); s (K1, ∅, 1); K0 (K1, {K0}, 1) (K0 → K1); q (K1, {K0}, 2); r (K1, ∅, 1); K2 (K1, ∅, 2); K3 (K1, {K3}, 3);
  pA (K1, {K3}, 4).
- Iσ on the core: K1: q vs s: P differ by K0, even, in q's set: (K1, q) ∈ Iσ. K0: pA (K1, {K3}, 4) vs σ(K0) = K1 (K1, ∅, 0): K3 odd:
  not improving. K3: K1 (length 0) vs K2 (length 2), node odd: not improving. So Iσ ≠ ∅: an S4a step.
- H: A(K0) = {K1}, A(K1) = {s, q}, A(K3) = {K2}. Via q: K1 → q → K0 → K1, a cycle whose most relevant vertex is K0: node K0, the
  largest reward (R). Via s: K1 → s → K1, node K1. So W*(K1) = (K0, ∅, 2) (K1 is not its own H-cycle node). W*(s) is the value of
  s → K1 → …, i.e. (K0, ∅, 3), and K1 ⊕ W*(s) = (K0, ∅, 4) ≠ W*(K1): by (H) σ_new(K1) = q. K0, K3 forced. σ_new ≠ σ, so S4c does not
  apply: K-config κ2. ∎

**Lemma E4 (the last iteration).** From every state with K-config κ2 and τ0 (any σ at movers and β's):
- (a) the next iteration is an S4a iteration whose result σ* has K-config κ3 and σ*(β_g) = pb_g at every β_g;
- (b) at σ*, Iσ* = ∅ (whatever σ* is at the movers), so with E0 the run stops (S5).
Proof of (a).
- Odd at K2: r gives K2 → r → K1 → q → K0 → K1 …, node K0 (largest reward); the loop gives node K2: σ̄(K2) = K2.
- Core values: K0 (K0, ∅, 0); q (K0, ∅, 1); K1 (K0, ∅, 2); s (K0, ∅, 3); K2 (K2, ∅, 0); K3 (K2, {K3}, 1); pA (K2, {K3}, 2).
  pb_g (K0, ∅, 1) for every g (pb_g → K0).
- Iσ on the core: K3: K1 (node K0) vs K2 (node K2): REWARD, improving. K0: pA (node K2) vs K1 (node K0): not. K1: s (K0, ∅, 3) vs q
  (K0, ∅, 1): node K0 even, the shorter is better: not.
- β_g with σ(β_g) = xt(g) a mover y: by [1E-N3] Ξσ(y) ⊴ the value of y's play under Odd's «pe at every gate»; that play (W) ends in
  c_W's loop, reward p'(c_W) < p'(K0). So Ξσ(xt(g)) ◁ Ξσ(pb_g): (β_g, pb_g) ∈ Iσ. If σ(β_g) = pb_g, (β_g, xt(g)) ∉ Iσ by the same
  comparison.
- H (Odd fixed to τ0: pe at every gate, K2 → K2). A(K0) = {K1}, A(K1) = {q}: every H-play from K0 is K0 → K1 → q → K0 …, node K0.
  β_g with A(β_g) = {xt(g), pb_g}: via pb_g, node K0; via xt(g), every H-play runs through movers, pads, gates (pe), e's to c_W's loop
  (W), node c_W. β_g is on no H-cycle (its only in-edge is from pβ_g, whose only in-edge is from the gate, which plays pe in H). So W*(β_g)
  has node K0, β_g ⊕ W*(xt(g)) has node c_W, and (H) gives σ_new(β_g) = pb_g. K3: A(K3) = {K2, K1}; via K2: K2 → K2 (τ0), node K2;
  via K1: node K0; K3 is on no H-cycle (only pA enters it, only K0 enters pA, and A(K0) = {K1}): σ_new(K3) = K1. σ_new(K3) ≠ σ(K3), so
  no fallback. ∎
Proof of (b). Let ρ* := «pe at every gate, K2 → K2».
- Odd's reply. From a gate g of a level-ℓ mover, the play under (σ*, ρ*) has value (c_W, ∅, 5ℓ + 3) (W). Under any other Odd strategy
  ρ, the play from g either takes pe at every gate it visits (then it is the same play), or at the first gate h where it takes pβ_h it
  continues β_h → pb_h → K0 → K1 → q → K0 …, node K0, a larger reward. So at every gate the least value is (c_W, ∅, 5ℓ + 3), attained by
  ρ* and by no strategy that leaves the pe-play; at K2 the loop (node K2) beats r (node K0) for Odd. As σ̄* is a pointwise optimum
  ([1E-N3]), Ξσ*(g) = (c_W, ∅, 5ℓ + 3) at every gate and Ξσ*(K2) = (K2, ∅, 0).
- Movers. Every option of a level-ℓ mover x is a pad m_(x,k) → g_(x,k) with Ξσ*(m_(x,k)) = (c_W, ∅, 5ℓ + 4) (m below c_W): all equal,
  none strictly better: no improving edge at x.
- β_g with a mover xt(g): Ξσ*(pb_g) = (K0, ∅, 1) (K-config κ3: K0 → K1 → q → K0), Ξσ*(xt(g)) = (c_W, ∅, ·): no improving edge.
- Core: K0: pA → K3 → K1 → q → K0: (K0, {K3}, 4) vs K1 (K0, ∅, 2): K3 odd: not. K1: s (K0, ∅, 3) vs q (K0, ∅, 1): not. K3: K2
  (K2, ∅, 0) vs K1 (K0, ∅, 2): not.
- All other Even vertices (e, pads, c_W, c_X, β_g with xt = X) have one successor. So Iσ* = ∅. ∎

## 6. Theorems and corollaries
**Lemma TERM-XI (PROVED).** The N5′-xi run from S3 on Γ3(G) terminates (and so does N5's, R15 (d)).
Proof. By E0, τ never changes and every iteration changes σ: an S4a iteration that is not a fallback has σ_new ≠ σ, and σ_new(v) ∈
A(v) at every v (H keeps only edges to A(v); [N5XI] picks inside A(v)), so σ_new = Switch_I(σ) with I := {(v, σ_new(v)) : σ_new(v) ≠
σ(v)} a non-empty unambiguous subset of Iσ; a fallback with Iσ ≠ ∅ is Switch_I for the set of best improving edges, one per vertex.
By [TERM] (c), σ goes strictly up in ≺ at every iteration, so no σ repeats; there are finitely many σ. ∎

**Theorem ENDGAME-3 (PROVED).** For every genome G, N5′-xi from S3 on Γ3(G) has exactly one fallback, at an iteration F ≥ 1, and makes
exactly F + 2 iterations; iterations 1, …, F − 1 are S4a iterations with K-config κ0 and τ0.
Proof. By TERM-XI the run stops; by E1's corollary it cannot stop while the K-config is κ0, and the K-config changes only at a fallback:
so there is a first fallback F, and iterations before it keep κ0, τ0. E2: after F, κ1. E3: iteration F + 1 is not a fallback and gives
κ2. E4 (a): iteration F + 2 is not a fallback and gives σ*; E4 (b) and E0: Iσ* = Iτ = ∅, so the run stops after F + 2 iterations. ∎
**Theorem ENDGAME-3-N5 (PROVED).** The same for N5 (SPEC S4a). Proof: identical; (H) holds for N5, every other step is SPEC text. ∎

**Corollary EXACT-L (PROVED; premises landed).** For every genome G with an acyclic Ξ-graph, N5 from S3 on Γ3(G) makes exactly
L(G) + 3 iterations.
Proof. RESULTS R117 REACH3: «the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE states of the IDEAL
run, transitions 1, …, L(G) are FL transitions and transition L(G) + 1 is a fallback». FL transitions are not fallbacks, so F = L(G) + 1;
ENDGAME-3-N5 gives F + 2 = L(G) + 3. ∎
Consequence. With R117's Corollary REAL-IDEAL-S3 (if N5 from S3 makes ≤ p(n) iterations then L(G) ≤ p(N + 7M + 10)), on the family
{Γ3(G) : G acyclic} N5's iteration count is polynomial in n IF AND ONLY IF L(G) is polynomial in N + M (n = N + 7M + 10 ≥ N + M).

**Corollary END-T3 (PROVED-CONDITIONAL on REACH3-CYC, RESULTS R118 (k)).** For every genome, N5′-xi from S3 on Γ3(G) makes exactly
T3 + 3 iterations. (R118 (k): first fallback at iteration T3 + 1.)

**READING (not claimed; not to sign): polynomial for [E-LEV] genomes with bounded U(G).** T-QUIET / UP-T (box 194, P-N5-QUIET, not
landed) bound T_CYC of IDEAL-CYC. The fixes entry 1 scope sentence governs: «T bounds IDEAL-CYC iterations; on Γ3 this bounds N5′-xi only
up to its first fallback, and only under REACH3-CYC; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or
general games». ENDGAME-3 now supplies the post-fallback part (exactly 2). If (i) REACH3-CYC holds (CONDITIONAL in R118) and (ii) UP-T's
bound applies to T3 (R221 §7's reading: Γ3's pre-fallback run is a Howard run with a different tie choice, and QUIET's proof uses only
DOM and STRICT; not proved here), then N5′-xi's total on Γ3(G) is T3 + 3 ≤ (1 + n·((2M + 3)·F′_(U(G))(M) − 1))·(L + 1) + 3, polynomial
in N + M for [E-LEV] genomes with U(G) ≤ B, B fixed.

## 7. What this does and does NOT give against TARGET.md
- TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game; §4: a bound on a restricted class is not M4.
- Gives: an exact, genome-independent account of the end of N5 and N5′-xi on the Γ3 family (one fallback, then two iterations); an exact
  count L(G) + 3 for N5 on Γ3 of acyclic genomes, so the open question «is N5 polynomial on this family?» is EXACTLY «is L(G) polynomial
  on acyclic genomes?» (IDEAL-ACYC, R104 / R110-R116); and, conditionally, N5′-xi = T3 + 3.
- Does NOT give: any bound on F, T3 or L(G); anything on N5 or N5′-xi outside Γ3(G); anything on general games; G-N5-TIME stays OPEN.
  Not M3, not M4, not a step-4 pass, not a TARGET.md claim.

## 8. DATA (tool experiments/new/box195/eg195.py; check195.sh, output check195.out; record sweep data/sweep195.out)
Unit: runs of N5′-xi (mode xi) or N5 (mode spec) from S3 on Γ3(G) (box 189 gamma3.build, all pads; box 190 n5v.step). Counters per run
(eg195.py docstring): e0fail (states), e1fail (pre-fallback iterations), e2fail, e3fail, e4fail (the iterations F, F + 1, F + 2),
stopfail, finsbar, fintie (the final state), nofb, late (iterations after F + 2), capped; acyc / lfail (N5 only: F = L(G) + 1 and total
L(G) + 3, L(G) by L-RED's ideal.traj; record sweep only, needs LRED = an L-RED tree at 86a7a7a8).
Families: rand (d 1-5); L-RED R221 §11's esc, noesc, deep, dense, lvl0 (spost221.py gen(), transcribed, credit L-RED 56); late* (start
= each mover's last option: a stand-in, L-RED's own.py-based late is not imported); acyc (Ξ-edges to smaller indices only).
- ENDGAME-3 (xi): every fail counter 0 in 24,000 runs (record: 8 families × 1,500 × seeds 1951, 1952), plus check195.sh's 2,400 (seed
  1953) and every pinned genome of box189/inst, box189/corpus, box191-box194/inst (one list in check195.out; box192/inst/DEAD_SEGT_n20.json, not a
  genome, is skipped). Tally: every run has exactly one fallback and 3 iterations from it (incl. it).
- ENDGAME-3-N5 (spec): every fail counter 0 in 24,014 runs (the same sets + the 14 R117 corpus genomes), plus check195.sh's spec lines.
- EXACT-L (spec, record): lfail 0 on 4,297 acyclic genomes (4,283 random, of which 3,000 from acyc, and the 14 corpus genomes: N5
  total = L(G) + 3, up to 62 = 59 + 3 on RECT_d11_T59_norm).
- Controls (the counters can fire; check195.out lines «ctrl1», «ctrl2», tested by check.sh): EG195_CTRL=1 (E3/E4 expectations swapped,
  final checks on the pre-fallback state): e2fail, e3fail, e4fail, stopfail, finsbar, fintie = 100 of 100 runs; EG195_CTRL=2 (start
  τ(K2) = r, σ(K1) = q, not S3): e0fail 200, e1fail 200 (states), no fallback.
- §1 / §6 quotes: experiments/new/box195/quotes195.py (record; needs git objects), output quotes195.out: «quotes 31 missing 0 (trunk
  51eb65348)».

## Addendum 1 (L-NEW successor 63, 03:20Z by date -u; Lead 02:48Z: EXACT-L's scope sentence)
- Scope of Corollary EXACT-L. It turns the IDEAL run length L(G) of RESULTS R104 / R117 (the tower count of the acyclic IDEAL model)
  into N5's EXACT iteration count from S3 on Γ3(G): #iterations = L(G) + 3 for every genome G with an acyclic Ξ-graph. So a family of
  acyclic genomes with L(G) super-polynomial in N + M would make N5 (SPEC S1-S5, with SPEC's S4a arena choice) from its default start S3
  super-polynomial on the games Γ3(G) (n = N + 7M + 10), and a polynomial bound on L(G) would bound N5 on them. It says nothing about
  N5′-xi beyond ENDGAME-3 (N5′-xi's pre-fallback count on Γ3 is T3, not L(G); R118 (k), CONDITIONAL), nothing about N5 on other games,
  and nothing about whether L(G) is polynomial (OPEN). Not M3, not M4, not a TARGET.md claim.
- Status (Lead 02:48Z): L-RED 57 attacks E0-E4; this box is NOT frozen as a packet until L-RED reports.
