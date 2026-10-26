# P-N5-DEPTH (box 22): settling by dependency depth. In the cyclic abstract model the run is fixed within n steps (ABS-DEPTH). In N5 a ρ-free interval with constant common cycles and an acyclic end-state dependency graph has length ≤ n − 1 (STATIC-DEPTH), which gives GCI-LEN on such global C-intervals
L-SI successor 18 (Opus 5.5; D18, Lead reading L40). Packet for the referees, frozen at its push. The sha1 goes to the Lead; repairs go in a NEW
file docs/si/P-N5-DEPTH-fixes-box22.md. Lead 18:25Z: «freeze it now as docs/si/P-N5-DEPTH-box22.md. Contents: ABS-DEPTH (model) with N-MONO,
STATIC-DEPTH (N5), PURE-END and GCI-LEN-ρF». Working notes: docs/si/N5-ABSCYC-box22.md, docs/si/N5-GCILEN-box22.md (more data, readings, (L1)).
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING. Not a TARGET.md claim. Nothing here bounds N5's running
time; G-N5-TIME stays OPEN.
NOTHING HERE DEPENDS ON P-N5-OFFMONO (in review) or on any other unlanded packet. The premises are LANDED entries, the SPEC text, and (for §1)
the frozen model definition of P-N5-GCX-box21 (a definition, not a claim).
Quotes: every [Q path@commit:lines] «…» is verbatim from the tagged source, checked by experiments/si/rund/quotecheck.py (pinned in
experiments/si/check.sh, with a shifted-line control that must fail).

## 0. To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Fact N-MONO (model) | PROVED (to sign) |
| §1 | Theorem ABS-DEPTH (cyclic abstract model, under GEN) | PROVED (to sign) |
| §2 | Theorem STATIC-DEPTH (N5, every game, under (H1)-(H4) and GEN_W) | PROVED (to sign) |
| §2 | Corollary PURE-END | PROVED (to sign) |
| §3 | Corollary GCI-LEN-ρF | PROVED (to sign) |
| §4 | the instance showing GEN is needed for ABS-DEPTH's per-vertex form | DATA (instance; not to sign) |
| §5 | data | DATA (not to sign) |
| §6 | (G1)-(G4), CONJECTUREs ABS-DEPTH-TIE, STATIC-DEPTH-TIE, readings | OPEN / CONJECTURE / READING (not to sign) |
- Premises (LANDED unless marked):
  - SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef…). S1 valuations and order: [Q docs/new/N5-ssi-global.md@982f5c629:28-29] «valuation of v
    under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends in, P = set of vertices on the play before
    reaching c with p' > p'(c), ℓ = number of steps to reach c.».
  - S4a: [Q docs/new/N5-ssi-global.md@982f5c629:51] «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v» and [Q docs/new/N5-ssi-global.md@982f5c629:53]
    «(Even's one-player optimum against τ among "keep or take an improving edge".)». The fallback: [Q docs/new/N5-ssi-global.md@982f5c629:56]
    «FALLBACK, if σ_new = σ and τ_new = τ».
  - Pointwise optimality of a one-player optimum. RESULTS R18 (d) Lemma S (a), every game by RESULTS R57 (a):
    [Q docs/RESULTS.md@58061d91:803-804] «U_τ the pointwise maximum of V_{σ',τ} over Even's σ'». Applied to the arena game H of S4a, this is
    the standing premise P2 of 1E-N3 as listed in RESULTS R69: [Q docs/RESULTS.md@982f5c629:3596] «P2: S4a's step is Even's optimum in its arena».
  - (SW), as listed among RESULTS R72's landed premises: [Q docs/RESULTS.md@982f5c629:3768-3769] «(SW): every Even switch of N5 is to an edge …
    of Iσ».
  - Monotonicity of Ξ in a phase, (M2κ) of RESULTS R56 (a): [Q docs/new/P-N5-FBPOLY-box41.md@982f5c629:97] «(M2κ) For z ∈ U and every
    in-phase transition t → t+1: κ_t(z) ≤ κ_{t+1}(z).». With (M1κ) and λ constant on a phase, Ξ_t(z) ⊴ Ξ_{t+1}(z) for every z.
  - For the reading of (H2) only: RESULTS R69 (d), [Q docs/RESULTS.md@982f5c629:3612] «Lemma STATIC: on a ρ-FREE INTERVAL I».
  - §1's model: [Q docs/si/P-N5-GCX-box21.md@02240121:63-64] «A STEP from a valid s: ARENA Al_s(v) := {s(v)} ∪ {y ∈ succ(v) : M_s(y) >
    M_s(s(v))} … s′ := a valid strategy using arena edges only whose N is pointwise maximal among those.».
  - §3's targets: [Q docs/si/P-N5-GCX-box21.md@02240121:32-33] «GLOBAL C-INTERVAL of S: a maximal sub-interval of S on which, for every
    cycle node c, A_t (of U_c) is non-increasing, D_t is constant and every Δ_t(u), u ∈ DD_t, is constant.» and L-RED 22's
    [Q docs/red/R91-ulc-reader.md@54de3f2f:101] «Every global C-interval of a λ_W-constant fallback-free run has length ≤ n − 1.».

## 1. The cyclic abstract model: Fact N-MONO and Theorem ABS-DEPTH (PROVED, in the model)
Model as P-N5-GCX-box21 §4 (frozen; quoted above), any digraph. Non-terminals V (|V| = n). Terminals t carry constants h(t) ≤ T(t). Valid
strategy: every play reaches a terminal. M_s, N_s: weight along the play plus h, resp. T, of its terminal. The step takes a pointwise
N-maximal valid strategy using arena edges, assumed to exist, chosen by a deterministic rule. Run s_0, s_1, …; play_t(v) := v's play under
s_t (its non-terminals and terminal). s* := the fixed point. d*(v) := the number of non-terminals on v's play under s*.
GEN: for every v, distinct plays from v have distinct N-values.
- (MONO) M_{t+1} ⪰ M_t. (MONO-SUCC) M_t(s_t v) is non-decreasing in t. (TERM) the run reaches a fixed point s*. (P-N5-GCX §4 remarks.
  Proofs: for every u, M_t(u) ≤ w(u) + M_t(s_{t+1} u), with equality if kept and strict by the arena if switched. Sum along the finite
  s_{t+1}-play. A switched vertex u has M_{t+1}(u) > M_t(u), so Σ_v M strictly increases while s changes, and there are finitely many
  strategies.)
- Fact N-MONO (PROVED). N_{t+1} ⪰ N_t for every t ≥ 0. Hence N_t ⪯ N* := N_{s*}. Proof: s_t is valid and uses only its own choices, which are
  arena edges, so it is a candidate; s_{t+1}'s N is pointwise maximal among the candidates. □
- Theorem ABS-DEPTH (PROVED, under GEN). For every v and every t ≥ d*(v): play_t(v) = play*(v). Hence the run is fixed after at most
  max_v d*(v) ≤ n steps.
  Proof. Induction on d := d*(v). Let y* := s*(v). Either y* is a terminal (d = 1), or d*(y*) = d − 1, and by induction play_t(y*) = play*(y*)
  for t ≥ d − 1. Either way M_t(y*) = M*(y*) and N_t(y*) = N*(y*) for t ≥ d − 1.
  - (A) y* ∈ Al_{s_t}(v) for every t ≥ d − 1. Otherwise s_t(v) ≠ y* and M_t(y*) ≤ M_t(s_t v). v takes y* at some transition t′ → t′ + 1 with
    t′ ≥ t, which needs M_{t′}(y*) > M_{t′}(s_{t′} v). But M_{t′}(y*) = M_t(y*) ≤ M_t(s_t v) ≤ M_{t′}(s_{t′} v) (MONO-SUCC), a contradiction.
  - (B) For t ≥ d − 1, let s′ := s_{t+1} with v's choice replaced by y*. y*'s play under s_{t+1} is play*(y*) and does not contain v
    (play*(v) = v · play*(y*) is simple), so s′ is valid. It uses arena edges of Al_{s_t}, by (A) at v. By maximality,
    N_{t+1}(v) ≥ N_{s′}(v) = w(v) + N*(y*) = N*(v).
  - With N-MONO, N_t(v) = N*(v) for every t ≥ d. By GEN, play_t(v) = play*(v). □
  The induction runs on the FINAL forest, so cycles in the graph do not matter. It never inspects non-chosen successors: the obstruction of
  DEAD box 21b (docs/si/DEAD.md) does not arise.

## 2. N5: Theorem STATIC-DEPTH and Corollary PURE-END (PROVED, every game)
Notation. Ξ_t(v): the valuation of v's honest play (σ_t at Even vertices, σ̄_t at Odd vertices). W_t(v): the valuation of v's (σ_t, τ)-play.
D_t := {Odd u : σ̄_t(u) ≠ τ(u)}. A_t := the vertices whose (σ_t, τ)-play meets no vertex of D_t. A gate u ∈ D_t is D-direct at t if σ̄_t(u),
τ(u) ∈ A_t. For a vertex v that is not on its play's cycle, val(v) = v ⊕ val(next v), where ⊕ puts v into P when p′(v) > p′(c) and adds 1 to ℓ
(S1's valuation, quoted above). A cycle vertex at distance ℓ from the cycle node c has valuation (c, ∅, ℓ).
Hypotheses on states [a, b] of one phase:
- (H1) Every transition t → t+1, a ≤ t < b, is an S4a step (no fallback). τ, λ and λ_W (honest and W cycle nodes) are constant on [a, b].
- (H2) σ̄_t = σ̄_a for t ∈ [a, b]. So D is constant, and σ̄ = τ off D. (A ρ-free interval in R69 (d)'s sense satisfies this.)
- (H3) At every t ∈ [a, b], the W-cycles and the honest cycles are the same cycles (vertex sequences), constant on [a, b]. CYCLE VERTICES: the
  vertices on them.
- (H4) The graph H_b is acyclic outside the cycle vertices. H_b has an edge v → σ_b(v) for Even v, v → τ(v) for Odd v ∉ D, and u → τ(u),
  u → σ̄(u) for u ∈ D; cycle vertices are sinks.
- GEN_W: for every v, different W-plays from v (paths to the same cycle) have different W-valuations.
- d*(v) := 0 for cycle vertices; 1 + d*(σ_b v) for Even v; d*(τ v) for Odd v ∉ D; max(d*(τ u), d*(σ̄ u)) for u ∈ D. d*(v) is the number of
  non-cycle Even vertices on a longest H_b-path from v, so d*(v) ≤ n − 1.
Facts. (W-MONO) W_{t+1} ⊵ W_t pointwise for a ≤ t < b: σ_t uses only its own choices, which are arena edges, and the step is pointwise
W-optimal over strategies using arena edges (S4a, R18 (d) (a) on the arena game: P2). (Ξ-SUCC) Ξ_t(σ_t v) is non-decreasing on [a, b]: if
kept, by (M2κ); if switched, by (SW) and (M2κ), Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v). (CV) Cycle vertices have constant plays
and valuations in both frames on [a, b], by (H1) and (H3).
Theorem STATIC-DEPTH (PROVED, lane, unrefereed). Under (H1)-(H4) and GEN_W, every non-cycle v has, at every t ∈ [a + d*(v), b], the same
W-play and the same honest play as at b. Hence σ_t = σ_b on [a + max d*, b], and b − a ≤ max_v d*(v) ≤ n − 1.
Proof. Induction along H_b in the order of d*. "v settled from s": both plays of v at every t ∈ [s, b] equal those at b. Cycle vertices are
settled from a (CV).
- Odd v ∉ D: σ̄ = τ at v throughout (H2), so both plays are v followed by τ(v)'s. v is settled from where τ(v) is.
- u ∈ D: σ̄(u) is fixed (H2). u's W-play is u·(τ(u)'s W-play), and its honest play is u·(σ̄(u)'s honest play). u is settled from the later of
  the two.
- Even v, y* := σ_b(v), with y* settled from s := a + d*(y*).
  - (A) For t ∈ [s, b], y* ∈ {σ_t v} ∪ Iσ_t(v). Otherwise σ_t(v) ≠ y* and Ξ_t(y*) ⊴ Ξ_t(σ_t v). v takes y* at some t′ → t′ + 1 with
    t ≤ t′ < b. By (SW), Ξ_{t′}(y*) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y*) = Ξ_{t′}(y*) (Ξ-SUCC; y* settled, and a valuation is a
    function of the play). Contradiction.
  - (B) For t ∈ [s, b − 1], let s′ := σ_{t+1} with v's choice set to y*. By (A), s′ uses arena edges of state t. y*'s W-play under σ_{t+1} is
    its W-play at b, which does not contain v: v is not a cycle vertex, and its W-play at b is v·(y*'s), simple up to a cycle not through v.
    So W_{s′}(v) = v ⊕ W_b(y*) = W_b(v). Pointwise optimality gives W_{t+1}(v) ⊵ W_b(v), and W-MONO gives W_{t+1}(v) ⊴ W_b(v).
  - So W_{t+1}(v) = W_b(v). By GEN_W, v's W-play at t + 1 is its W-play at b, so σ_{t+1}(v) = y*, and v's honest play at t + 1 is
    v·(y*'s) = its honest play at b. v is settled from s + 1 = a + d*(v).
- At t ≥ a + max d*, every non-cycle Even v has σ_t(v) = σ_b(v) (the first step of its W-play). Cycle Even vertices have it by (H3). So
  σ_t = σ_b. A transition of [a, b] that leaves σ unchanged leaves (σ, τ) unchanged (τ is constant), and that is a FALLBACK (SPEC S4c, quoted),
  excluded by (H1). So b ≤ a + max d*. □
Corollary PURE-END (PROVED, elementary). If every gate is D-direct at b, then (H4) holds, and every cycle at b is common to both frames.
Proof. For z ∈ A_b, z's W-play meets no gate and σ̄ = τ off D, so z's honest play is its W-play, and z's only H_b-path is that play,
ending in a cycle inside A_b. For v ∉ A_b, every H_b-path from v is (v's W-play up to its first gate u, holding no other gate), then τ(u) or
σ̄(u) ∈ A_b, then that vertex's play inside A_b. The two parts are disjoint (first-part vertices are not in A_b), and each is simple.
Every W-cycle and every honest cycle is reached inside A_b, where the two plays coincide, so it is common. □ ((H3), constancy on [a, b],
remains a hypothesis.)

## 3. Corollary GCI-LEN-ρF (PROVED, lane)
Let [a, b] be a global C-interval (quoted above) of a λ_W-constant fallback-free run in one phase. Suppose σ̄ is constant on it, it satisfies
(H3) and (H4) (by PURE-END, (H4) holds if every gate is D-direct at b), and GEN_W holds. Then b − a ≤ n − 1, i.e. GCI-LEN holds for it.
Proof: such an interval satisfies (H1) and (H2), so STATIC-DEPTH applies. □
- Scope. R91 §3 (L-RED, lane) covers D = ∅ (per class, bound |U_c| − 1, no (H3)). This corollary allows gates, but needs σ̄ fixed and
  constant common cycles. Neither contains the other.

## 4. GEN cannot be dropped from ABS-DEPTH's per-vertex form (DATA, instance; experiments/si/root/absdepth.py --tie, pinned)
Non-terminals 0, 1, 2; terminals t3, t4, t5 with h = (−1, 1, −1), T = (0, 1, 1); w = (−1, 1, 1); succ(0) = {1, t3}, succ(1) = {0, 2, t5},
succ(2) = {0, t4, t5}; start (t3, t5, 0). Run: (t3, t5, 0) → (1, t5, 0) → (1, 2, t4). Vertex 2 has d*(2) = 1 (final play 2 → t4, N = 2). At
state 1 it holds 2 → 0 → 1 → t5, also N = 2: N has settled at 2, the play has not. The run still ends within max d* = 3 steps.

## 5. DATA (not to sign)
- ABS-DEPTH (absdepth.py, abscyc.py's model code unchanged; logs root/logs/absdepth_*.txt):
  - 9,635 random cyclic runs (n = 4-8), 50,906 vertices, 0 violations of the per-vertex statement, of N-MONO and of MONO; GEN held in all of them.
  - Control MUT=1 (d* − 1): 1,938 violations of 14,217.
  - The extremal climbs (abscyc.py --climb, n = 5, 6) reach exactly max d* = n.
  - With values in {−2..2} (ties frequent): 11,326 runs, 46 non-GEN, 7 per-vertex failures (all in non-GEN runs), 0 runs longer than max d*.
- STATIC-DEPTH (staticdepth.py; logs root/logs/staticdepth_*.txt):
  - lib41 (n ≤ 48, S3 + 2 random starts): 1,709 σ̄-constant intervals; 1,368 satisfy (H3)+(H4), 906 of them with gates; 0 violations.
  - Sharp: the length equals max d* in 26 intervals. b6_xs has length = max d* = 21, 29, 36 at n = 24, 32, 40. The longest checked interval
    with gates is 26 at n = 48 (x32_waves48, one gate, max d* = 37).
  - GEN_W failed in 23 intervals, with the conclusion intact.
  - Global C-intervals (GCI=1): 1,480 with σ̄ constant and 444 with σ̄ changing inside; none longer than n − 3.
  - 3,000 random 𝒞^kO games: 563 checked intervals, 0 violations. The ten long instances of N5-GCILEN §4: 0 violations.
  - Control MUT=1 (d* − 1): 272 of 296 checked intervals fail (lib41, n ≤ 24).

## 6. OPEN, CONJECTURES, READING (not to sign)
- (G1) σ̄ changes inside a global C-interval (a gate's choice moves between non-τ options with D constant); e.g. pp_K12_n161, one global
  C-interval of length 17 at n = 161.
- (G2) cycles not common to both frames, or not constant on the interval. L-RED's reader_L (R91) fails (G2) together with (G3) on its long
  interval [0, L + 1], whose length L + 1 ≤ n − 1 is outside this packet.
- (G3) (H4) at an impure end.
- (G4) W-ties (GEN_W). SPEC breaks S4a ties by the S1 procedure on the current arena, not by a fixed rule on successor values, so GEN_W has
  no automatic substitute. CONJECTURE STATIC-DEPTH-TIE: the length bound holds without GEN_W. CONJECTURE ABS-DEPTH-TIE: in the model, the run
  is fixed within max d* steps without GEN.
- READING. STATIC-DEPTH makes L-RED's R91 §5 heuristic exact for the intervals it covers («one fresh vertex per causal step»): each step is
  paid by an Even vertex of an H_b-path that settles for good. Pure C-intervals in general: docs/si/N5-GCILEN-box22.md §6 (GATE-PUSH,
  PURE-LEN; not part of this packet).
