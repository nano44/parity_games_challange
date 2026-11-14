# Packet P-N5-END (box 195): after its first fallback, N5 and N5′-xi on Γ3(G) stop after exactly two more iterations (every genome); N5 from S3 on Γ3(G) makes exactly L(G) + 3 iterations for G ∈ IDEAL-ACYC
L-NEW successor 63 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-08 04:00Z: «FREEZE packet P-N5-END: E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5,
EXACT-L (IDEAL-ACYC), and END-T3 marked conditional on REACH3-CYC». FROZEN at push. Later text goes to docs/new/P-N5-END-fixes.md,
append-only. Source, history only: docs/new/N5-END-box195.md (box 195 with Addenda 1-2). This packet carries every proof in full.
Attacked by L-RED 57 (R222 item 3, claude/l-red 6f56004c, docs/red/R222-end.md): all SURVIVE; its one GAP (EXACT-L's IDEAL-ACYC wording)
is fixed here. Credit: the conjecture ENDGAME-3, the skeleton E0-E4 and the family generator are L-RED 56's (R221 §10-§11).
Labels: PROVED (L-NEW 63, unrefereed) / PROVED-CONDITIONAL / READING (not to sign) / DATA.
This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME.

## Scope (explicit)
- Games: Γ3(G) of RESULTS R117 for a genome G of RESULTS R104 (every genome for §3-§6; G ∈ IDEAL-ACYC for EXACT-L). Algorithms: N5 (SPEC
  S1-S5) and N5′-xi (RESULTS R118's [N5XI]) from SPEC's default start S3. Counted: iterations (SPEC S4).
- What it implies: the run's end is exact and genome-independent (one fallback at F, total F + 2); for G ∈ IDEAL-ACYC, N5's iteration
  count from S3 on Γ3(G) equals L(G) + 3, so on the family {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count is polynomial in n iff L(G) is
  polynomial in N + M (n = N + 7M + 10); conditionally on REACH3-CYC, N5′-xi makes exactly T3 + 3 iterations.
- What it does NOT imply: any bound on F, on L(G) (OPEN) or on T3; anything about N5 or N5′-xi on games other than Γ3(G); anything about
  general parity games; a bound on T3 from box 194 (P-N5-QUIET's lemmas are on Γ(G); the Γ3 run can differ at exact VJ ties, R118's
  DATA). EXACT-L is false without IDEAL-ACYC's self-loop clause (§6, witness SELFL_n3).

## To sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §3 | Lemma E0 | PROVED | every genome |
| §4 | Lemma E1 | PROVED | every genome |
| §5 | Lemmas E2, E3, E4 | PROVED | every genome |
| §6 | Lemma TERM-XI; Theorems ENDGAME-3, ENDGAME-3-N5 | PROVED | every genome |
| §6 | Corollary EXACT-L | PROVED | G ∈ IDEAL-ACYC (self-loops count as cycles); premise R117 (f) |
| §6 | Corollary END-T3 | PROVED-CONDITIONAL | on REACH3-CYC (RESULTS R118 (k), CONDITIONAL there) |
| §7-§9 | DATA, machine checks, TARGET diff | DATA / READING (not to sign) | |

## 1. Premises (quoted by script: experiments/new/box195/quotes_end.py, output quotes_end.out; trunk 51eb65348 docs/RESULTS.md,
docs/new/N5-ssi-global.md, docs/new/P-N5-XICYC.md, docs/new/P-N5-REACH.md)
- [SPEC] (docs/new/N5-ssi-global.md; the SPEC that RESULTS R104 / R117 / R118 run):
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
  - The value order ([VJ], SPEC S1): reward of the cycle node first; then the path set by its most relevant differing vertex; then the
    length, «if c is odd, longer is better for Even; if c even, shorter is better».
- [N5XI] RESULTS R118: N5′-xi is SPEC S1-S5 «with ONE change in S4a» (box 190's tie rule); the frozen packet it cites
  (docs/new/P-N5-XICYC.md l. 45-47): «SPEC S1-S5 with ONE change in S4a. At every Even v with |A(v)| ≥ 2 that is not its own H-cycle
  node, σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}. Ties go by SPEC's choice, then the larger index.
  Here A(v) = {σ(v)} ∪ Iσ(v).» (W* = the values of S4a's arena optimum in H.)
- [1E-N3] RESULTS R57 (b) as landed in R104: «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new,
  S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that
  arena, before S4c)». Why this source and not R118 (b)'s [OPT] (REFEREE 28's QT-L1 for P-N5-QUIET): here σ̄ IS the output of SPEC's
  S1 procedure inside SPEC runs (N5, N5′-xi), which is exactly what 1E-N3 covers; IDEAL-CYC's defined σ̄_t (R118 (b)) is not used.
- [DEF] RESULTS R104, definitions only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»; options
  «each with a W-target of level lev(x) − 1 (none at level 0)»; «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u,
  or to u alone»; «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»; «an unused even
  self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»; «a closed core
  u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»; «with start σ =
  the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2»;
  and «G is in IDEAL-ACYC iff its» «Ξ-graph is ACYCLIC (self-loops count as cycles).».
- [G3] RESULTS R117, definition of Γ3: «the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on
  K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on
  every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)»;
  Lemma S3-START: Γ3 «has S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START)». The Ω of each pad
  (pA, s, r, pβ 0; q, pe, pb 1; m 2 or 0) is P-N5-REACH §3, the packet R117 lands.
- [TAU3] P-N5-REACH §6.4 (signed for every genome: RESULTS R118 «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every
  genome»): «In the standard state, Iτ = ∅, so S4b leaves τ unchanged.»
- [TERM] RESULTS R15: «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» and
  (c) «≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺. Consequence: no
  strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule».
- [REACH3] (EXACT-L only) RESULTS R117 (f): «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L = L(G). Then the N5 run of Γ3(G)
  FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL transitions; transition
  L + 1 is a fallback.»
- [R3C] (END-T3 only) RESULTS R118 (k): «N5′-xi from S3 on Γ3(G) visits only standard states and makes Howard steps at the movers until
  its first fallback, at iteration T3 + 1» («Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every
  genome»).
- Not used: ESC3, W3, KEY3, SBAR3, PLAY3, PAD (b)-(c) (pads are handled directly in §2), R118 (b)'s [OPT], any box 194 / P-N5-QUIET
  lemma, any L-RED lemma.

## 2. Facts about Γ3 used below (from [DEF] and [G3])
- (R) Rank order, by Ω first: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β (≥ 6) < every e < c_W (top) < K0 (top + 2)
  < K3 (top + 3). A P-set holds only vertices above its cycle node in this order. K0 is the most relevant EVEN vertex, so a value with
  cycle node K0 has the largest reward of all values; K1's reward −p'(K1) is below K2's −p'(K2).
- (C) The core Kc := {K0, K1, K2, K3, pA, s, q, r} is closed: K0 → {K1, pA}, pA → K3, K3 → {K1, K2}, K1 → {q, s}, q → K0, s → K1,
  K2 (Odd) → {r, K2}, r → K1. Values on Kc depend only on the K-config κ(σ) := (σ(K0), σ(K1), σ(K3)) and on Odd's choice at K2.
  κ0 := (pA, s, K2), κ1 := (K1, s, K2), κ2 := (K1, q, K2), κ3 := (K1, q, K1).
- (S) S3's pair ([G3] S3-START, or FIX 1 directly): κ0; β_g → xt(g) if xt(g) is a mover (else its only successor pb_g); τ0 := pe_g at
  every gate g and K2 → K2.
- (W) From a gate g of a level-ℓ mover, the play that takes pe at every gate passes g, pe_g, e_g, then (ℓ ≥ 1) a mover of level ℓ − 1,
  its pad, its chosen gate, …, and ends in c_W's loop after exactly 5ℓ + 3 steps, whatever Even plays at movers (W-targets have level
  lev − 1; level-0 e's go to c_W). It meets no β and no core vertex, and no vertex above c_W: its value is (c_W, ∅, 5ℓ + 3).
- (H) If v is not its own H-cycle node and some w0 ∈ A(v) has v ⊕ W*(w0) = W*(v) while every other w ∈ A(v) gives v ⊕ W*(w) ≠ W*(v),
  then σ_new(v) = w0, in N5 and in N5′-xi. (N5: σ_new is a pointwise optimum of H ([1E-N3]); v's H-value is v ⊕ the value of σ_new(v),
  so σ_new(v) ∈ TIE(v) = {w0}. N5′-xi: σ_new(v) ∈ TIE(v) by [N5XI].) Where |A(v)| = 1 the choice is forced in both.

## 3. Lemma E0 (τ is fixed) PROVED
Every state of the run has τ = τ0, and Iτ = ∅ there.
Proof. Iτ is computed on G^d from τ alone ([SPEC]: τ̄ is Even's optimal counterstrategy to τ, «Iτ computed there»), so Iτ is the same
at every state with τ = τ0; by [TAU3] (at the standard state, whose τ is τ0) it is ∅. S4b changes τ only if Iτ ≠ ∅; S4c changes τ only
when Iσ = ∅, and then only along Iτ. Induction from (S). ∎

## 4. Lemma E1 (the core is frozen until a fallback) PROVED
In every state with K-config κ0 and τ0: (a) Iσ ∩ (edges out of K0, K1, K3) = {(K0, K1)}; (b) every S4a σ_new (N5 or N5′-xi) has
K-config κ0.
Proof.
- Odd at K2: r gives K2 → r → K1 → s → K1 …, node K1; the loop gives node K2. Reward −p'(K1) < −p'(K2) (R), so σ̄(K2) = r in every
  pointwise optimum ([1E-N3]).
- Values (as in R117's K3 (a)): K1 (K1, ∅, 0); s (K1, ∅, 1); r (K1, ∅, 1); K2 (K1, ∅, 2); K3 (K1, {K3}, 3); pA (K1, {K3}, 4);
  K0 (K1, {K0, K3}, 5); q (K1, {K0, K3}, 6) (P by (R): K0, K3 are the only core vertices above K1).
- (a) K0: Ξ(K1) vs Ξ(pA): same node, P differ by K3, odd: K1 better: improving. K1: q vs s: P differ by {K0, K3}, top K3 odd: q worse.
  K3: K1 (length 0) vs K2 (length 2), node K1 odd: the longer is better for Even: not improving.
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
**Lemma TERM-XI (PROVED).** The N5′-xi run and the N5 run from S3 on Γ3(G) terminate.
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

**Corollary EXACT-L (PROVED; premises landed).** For every genome G ∈ IDEAL-ACYC (R104: its Ξ-graph is acyclic, self-loops count as
cycles), N5 from S3 on Γ3(G) makes exactly L(G) + 3 iterations.
Proof. [REACH3]: transitions 1, …, L(G) are FL transitions, which are not fallbacks, and transition L(G) + 1 is a fallback; so the first
fallback is F = L(G) + 1, and ENDGAME-3-N5 gives F + 2 = L(G) + 3. ∎
- Consequence. With R117's Corollary REAL-IDEAL-S3, on {Γ3(G) : G ∈ IDEAL-ACYC} N5's iteration count from S3 is polynomial in n iff L(G)
  is polynomial in N + M (n = N + 7M + 10). A family of IDEAL-ACYC genomes with L(G) super-polynomial would make N5 (SPEC's S4a choice)
  super-polynomial on these games; a polynomial bound on L(G) would bound N5 on them. Nothing about N5′-xi beyond ENDGAME-3.
- The self-loop clause is necessary (L-RED 57 R222 item 3): SELFL_n3 (N 3, two Ξ self-loops; inst/SELFL_n3.json, sha1 27bc7f72…) has
  L(G) = 1 while N5 from S3 makes 3 iterations (F = 1; ENDGAME-3-N5 holds, REACH3 does not apply).

**Corollary END-T3 (PROVED-CONDITIONAL on REACH3-CYC).** For every genome, if [R3C] holds then N5′-xi from S3 on Γ3(G) makes exactly
T3 + 3 iterations. Proof: [R3C] places the first fallback at F = T3 + 1; ENDGAME-3. ∎
- READING (not to sign): no bound on T3 follows from P-N5-QUIET (its lemmas are on Γ(G); REFEREE 28's QT-L4).

## 7. DATA (not to sign; tool experiments/new/box195/eg195.py; check195.sh, output check195.out; record runs in data/)
Unit: runs of N5′-xi (EG195_MODE xi) or N5 (spec) from S3 on Γ3(G) (box 189 gamma3.build, all pads; box 190 n5v.step). Scope: Γ3(G) as
built by gamma3.py (pinned). Families: rand (d 1-5); L-RED R221 §11's esc, noesc, deep, dense, lvl0 (gen() transcribed, credit L-RED
56); late* (start = each mover's last option, a stand-in); acyc (Ξ-targets of strictly smaller index: IDEAL-ACYC, no self-loops).
- E0: e0fail 0 (unit: states). E1: e1fail 0 (unit: iterations before the first fallback). E2, E3, E4 (a): e2fail, e3fail, e4fail 0
  (unit: the iterations F, F + 1, F + 2). E4 (b): stopfail 0, finsbar 0 (σ̄ not pe at a gate or σ̄(K2) ≠ K2), fintie 0 (a mover with two
  option values) (unit: final states). ENDGAME-3 / -N5: nofb 0, late 0, capped 0, tally «one fallback, 3 iterations from it» on every run.
  Sets: xi 24,000 runs and spec 24,000 runs (8 families × 1,500 × seeds 1951, 1952; data/sweep195.out) + spec on the 14 R117 corpus
  genomes; check195.sh: 8 families × 300 (seed 1953) per mode + every pinned genome of box189/inst, box189/corpus, box191-box194/inst.
- TERM-XI: no separate DATA (every run above stopped; capped 0).
- EXACT-L: lfail 0 (unit: IDEAL-ACYC genomes with F ≠ L(G) + 1 or total ≠ L(G) + 3; L(G) by L-RED's ideal.traj at claude/l-red
  86a7a7a8, record only) on 4,297 genomes (4,283 random IDEAL-ACYC ones among the spec sweep, 3,000 of them from acyc, and the 14 corpus
  genomes, L(G) up to 59: RECT_d11_T59_norm, 62 iterations). Witness of necessity: SELFL_n3 (data/selfl195.out: L(G) 1, total 3).
- END-T3: no separate DATA (R118's REACH3-CYC DATA is R118's).
- Controls (the counters can fire; check195.out «ctrl1», «ctrl2», tested by check.sh): ctrl1 (E3/E4 expectations swapped; final checks
  on the pre-fallback state): e2fail, e3fail, e4fail, stopfail, finsbar, fintie = 100 of 100 runs; ctrl2 (start τ(K2) = r, σ(K1) = q):
  e0fail 200, e1fail 200 (states), no fallback.
- Independent replay: L-RED 57 R222 item 3 (own code, own.py VJ + Odd optimisation; L-RED's own «late»): 2,700 genomes, 9 families,
  8,100 runs, every counter 0, controls fire (claude/l-red 6f56004c; L-RED's counter, cited, not re-run).

## 8. Machine checks
- check.sh block «BOX 195 END»: re-runs check195.sh, diffs check195.out, requires 0 in every fail counter outside «ctrl» lines and the
  two controls to fire.
- check.sh block «P-N5-END»: sha1 of this packet and of every tool, instance and output it cites, against experiments/new/box195/end.pins.
- §1's quotes: experiments/new/box195/quotes_end.py (record; needs git objects), output quotes_end.out.

## 9. TARGET.md diff and limits
- TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game; §4: a bound on a restricted class is not M4. This packet bounds
  nothing: it gives the exact END of two runs on one family of games, and an exact identity between N5's count on {Γ3(G) : G ∈ IDEAL-ACYC}
  and L(G). Not M3, not M4, not a step-4 pass. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
- Limits: nothing on F, T3 or L(G); nothing outside Γ3(G).
