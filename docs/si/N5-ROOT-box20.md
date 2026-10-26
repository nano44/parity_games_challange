# N5, the root of a relay structure: where FRZ-U's single gate is used, BF-F_D and FREEZE-A on every game, and the root's ρ per piece (box 20)
L-SI successor 16 (Opus 5.5; D18, Lead reading L40). Lead's GO 13:55Z (Lead's stamp): "GO on (2), the root FRZ-U analogue ... The fallback-free
returns are exactly your root dynamics ... That is the place your FRZ-U analogue would bite. Say which."
Written 2026-10-26T14:11Z onward (date -u). Working note, unrefereed. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING.
Scripts: experiments/si/root/ (common.py, bffd.py, rootdyn.py, shrink.py, rootrun.py); logs in experiments/si/root/logs/.
Instances: nep90_n40 = experiments/red/rec0/instances/nep90_n40.pg with experiments/si/rund/instances/nep90_n40.start (as note §26);
nep76_n40 = experiments/n5-epoch/instances/nep76_n40.pg with its .start.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Which steps of R50 FRZ-U's Claim P^c use D = {o}: Fact B across two gates is the essential one; on nep90 / nep76 W(r) is constant on the whole phase while Ξ(r) changes 72 / 62 times, so a stretch (θ, w constant) is about one transition long and an FRZ-U-type freeze inside it is empty | READING, DATA |
| §2 | Lemma BF-F_D (every game): an S4a step is a Bellman-Ford round at every Even v of a class whose (σ, τ)-play avoids D before and after | PROVED |
| §3 | Theorem FREEZE-A (every game): on a fallback-free run on which A := F_D ∩ U_c does not grow, path weights on A freeze after |A_s| − 1 steps, and every Odd choice vertex whose choice lies in A then changes its path weight ≤ deg − 1 times | PROVED |
| §4 | Corollary ROOT-PIECE: per phase, the path-weight changes of q while its choice lies in A are ≤ (f + G_c + 1)(|U_c| + deg(q) − 2) + f + G_c, G_c := the A-gains of the class | PROVED |
| §5 | Data: BF-F_D 1.2 M checks, 0 failures; FREEZE-A non-vacuous; nep90: 22 cuts (7 fallbacks, 15 A-gains, all by a D-vertex LEAVING D), ρ_r ≤ 7 per piece; A-gains by an Even switch occur elsewhere (lib41: 283 of 9,085 entering vertices), never by a split vertex | DATA |
| §6 | Answer to "say which": the root count bites on R⁰ (inside fallback-free runs), not on NCONF; what remains is G_c (D-leaves and unsplit exits), the relays' own ROUTE events, and f | READING, OPEN |

## 0. Setting (every game)
N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, FIX 1-4), standing premise 1E-N3 as in R55-R69. A phase: a maximal run with λ_Ξ and τ constant
(RESULTS R38 (a) KEY). Every in-phase transition is an S4a step (σ_{t+1} is Even's optimum of the arena H_t against τ) or an Even S4c fallback.
- D_t := {Odd u : σ̄_t(u) ≠ τ(u)}. F_D(t) := the vertices whose (σ_t, τ)-play meets no vertex of D_t (RESULTS R55, R63). Q := the Odd vertices of
  out-degree ≥ 2.
- For a cycle node c of the phase: U := U_c := λ^{-1}(c), constant on the phase. wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0.
  M_t(z) := wt(P(Ξ_t z)) for z ∈ U (the first component of RESULTS R56's κ_t(z)). For a valuation x with cycle node c, Mx := wt(P(x)).
- A_t := F_D(t) ∩ U. G[A]: the graph on A in which every Even v ∈ A ∖ {c} keeps its edges into A, every Odd v ∈ A ∖ {c} keeps the edge to τ(v)
  if τ(v) ∈ A, and c is a sink. MoptA(z) := max{wt(p ∖ {c}) : p a simple path of G[A] from z to c} (−∞ if none).
- An A-GAIN (of class c) is an in-phase S4a transition t → t+1 with A_{t+1} ⊄ A_t.
- Facts used (all LANDED on every game): (Aκ), (A0κ), (M1κ), (M2κ), (SP′) of RESULTS R56 (a): for z ∈ U ∖ {c}, next_t(z) ∈ U and
  M_t(z) = wt(z) + M_t(next_t z); M_t(c) = 0; for valuations x, x′ with cycle node c, x ⊴ x′ ⇔ (Mx, s_c·ℓ(x)) ≤ (Mx′, s_c·ℓ(x′))
  lexicographically; M_{t+1}(z) ≥ M_t(z) at in-phase transitions; z's honest play up to its first visit of c is a simple path in U.
  (F1): RESULTS R17 (a), applied to S4a's arena H_t in G_τ (one-player on every game, RESULTS R55's premise list). XW: Ξ_t ⊴ W_t pointwise
  (RESULTS R21 (a); confirmed game-general in R55's premise list). G_D (a): Ξ_t = W_t on F_D(t) (RESULTS R55 (a)). (V1): RESULTS R17 (a).
  κ-Y-FORM_D: RESULTS R56 (d). Rewards are injective (SPEC S1).

## 1. Which steps of R50 FRZ-U's Claim P^c use D = {o} (READING, from docs/si/P-N5-KW-box15.md §3; DATA on nep90 / nep76)
| step of FRZ-U / Claim P^c | what it uses | with several gates (|D| ≥ 2) |
| --- | --- | --- |
| Fact A0 / A (values on R factor through o with constant terminals θ, w) | every Odd vertex but o is forced | R55 (b) G_D (b) / R62 (a) G_D-NC (b′): factorisation through the FIRST D-vertex u(v), under (h_D) or (NC). R splits into the gate regions R_u, u ∈ D, each with its own pair (Ξ(u), W(u)) |
| Fact B (Ξ- and W-orders agree above m* on R) | y, z share the gate o and its constants | holds for y, z with the same gate (G_D (c1)); FAILS in general for u(y) ≠ u(z): the comparison then involves Ξ(u) vs Ξ(u′) and W(u) vs W(u′), and these orders disagree exactly because u, u′ ∈ D. THIS is the step that uses D = {o} essentially |
| Case B (κ_k(z) ≻ κ_k(a) ⇒ (x, z) improving, then (F1)) | Fact B for z (next on ρ) and a = σ_k(x) | ρ is a path of G_τ: z and a can lie in different gate regions, so Case B needs Fact B across gates |
| (MON) and B2 / B3 (cycle node of x ∈ R_{k+1} is c_w) | WM and the constant w | WM-G (R62 (d)) is game-general; the constant must be W(u(x)), with u(x) constant |
| closing step (paths of ≤ r − 1 edges) | |R| constant | |R_u| constant |
| the stretch (R, θ, w constant) | one gate | all gate values constant |

- DATA (experiments/si/root/rootdyn.py; scratch probe for W(r), R_r). On the long phases of nep90 (phase@4, 91 transitions, root r = 0, c = 11,
  |U| = 40, deg(r) = 18) and nep76 (phase@9, 78 transitions, r = 0, c = 11, deg(r) = 15):
  - W(r) is CONSTANT on the whole phase (nep90 (16, 8192), nep76 (20, 32768)); Ξ(r) changes 72 / 62 times; R_r (the vertices whose first
    D-vertex is r) changes 36 / 36 times.
  - Every terminal of the class is UNSPLIT at every state (λ_W = λ = c); c ∉ Q and c ∉ D at every state.
  - So the W-frame sees r as a fixed sink of high value (its W path set holds an even vertex of high rank that Ξ(r)'s does not). An Even vertex
    takes an edge into r's gate region whenever that edge is Ξ-improving (S4a is W-best), and the next fallback (Ξ-best) takes it back out: this
    is L-RED 21's PING-PONG (R88), seen here at nep90 t = 39 (fallback: 23, 36 leave 0) and t = 41, 42 (S4a: 23 → 0, 36 → 0, 4 → 23).
- READING. An FRZ-U-type statement freezes Ξ / W on a gate region while the gate values are constant. On nep90 the gate value Ξ(r) moves at 72 of
  91 transitions, so such a freeze is empty there. The count that the long phase needs is a count of the gate's own value changes. On 𝒞^1O that
  count is RESULTS R27 (g) TH (θ-changes charged to crossings via F1° on F) and R45 (e) FREEZE-F (S4a steps are Bellman-Ford rounds on F ∩ U).
  §2-§4 port that pair, not FRZ-U, to every game.

## 2. Lemma BF-F_D (PROVED, every game)
Statement. Let t → t+1 be an in-phase S4a transition, c a cycle node of the phase, U := U_c, and v ∈ U Even, v ≠ c, with v ∈ F_D(t) ∩ F_D(t+1).
Then for every successor x ∈ U of v: M_{t+1}(v) ≥ wt(v) + M_t(x).
Proof.
- Case 1: M_t(x) ≤ M_t(σ_t v). By (Aκ), M_t(v) = wt(v) + M_t(σ_t v) ≥ wt(v) + M_t(x), and M_{t+1}(v) ≥ M_t(v) by (M2κ).
- Case 2: M_t(x) > M_t(σ_t v). σ_t(v) = next_t(v) ∈ U, so both values have cycle node c, and (M1κ) gives Ξ_t(x) ▷ Ξ_t(σ_t v). So (v, x) ∈ Iσ_t,
  and σ″ := σ_t[v ↦ x] is a strategy of the arena H_t. By (F1), W_{t+1} ⊵ W_{σ″} pointwise (W_{σ″}: the value of the (σ″, τ)-play). Since
  v ∈ F_D(t+1), G_D (a) gives W_{t+1}(v) = Ξ_{t+1}(v), whose cycle node is λ_{t+1}(v) = c.
  - (i) x's (σ_t, τ)-play avoids v. It is also x's (σ″, τ)-play, and v's (σ″, τ)-play is v followed by it, so v is not on its cycle and (V1)
    gives W_{σ″}(v) = v ⊕ W_t(x).
    - By XW, W_t(x) ⊵ Ξ_t(x), whose cycle node is c. If W_t(x) had another cycle node u, then reward(u) > reward(c), W_{σ″}(v) would have cycle
      node u, and W_{t+1}(v) ⊵ W_{σ″}(v) would force reward(λ(W_{t+1}(v))) ≥ reward(u) > reward(c), against λ(W_{t+1}(v)) = c. So W_t(x) has
      cycle node c, and (M1κ) gives MW_t(x) ≥ M_t(x).
    - v ∉ P(W_t(x)) (P lies on x's play). So W_{σ″}(v) has cycle node c and path weight wt(v) + MW_t(x). With (M1κ) on W_{t+1}(v) ⊵ W_{σ″}(v):
      M_{t+1}(v) = MW_{t+1}(v) ≥ wt(v) + MW_t(x) ≥ wt(v) + M_t(x).
  - (ii) x's (σ_t, τ)-play passes v. Write it as q · v · (v's (σ_t, τ)-play), with q the part before the first visit of v (q = ∅ if x = v).
    - v ∈ F_D(t): v's (σ_t, τ)-play is its honest play, W_t(v) = Ξ_t(v) (G_D (a)), cycle node c. So x's W-play ends on c's cycle, and its path
      weight is the sum of wt over its distinct vertices (a vertex of nonzero wt has rank > rank(c) and is not on the cycle, whose top is c).
      Its vertex set is q ∪ (v's play); a vertex of q that is also on v's play lies on v's cycle, hence has wt 0. So
      MW_t(x) = wt(q) + M_t(v) = wt(q) + wt(v) + M_t(σ_t v), by (Aκ).
    - XW: Ξ_t(x) ⊴ W_t(x), both with cycle node c, so M_t(x) ≤ MW_t(x). With Case 2: wt(q ∪ {v}) > 0.
    - Under σ″, v's (σ″, τ)-play is the cycle Z := v → x → q → v (vertices off v keep their edges). wt(Z) > 0, so the vertex u* of largest
      rank among Z's vertices of rank > rank(c) is even (it dominates the signed sum), and every other vertex of Z is below it: u* is Z's top.
      u* even with rank(u*) > rank(c) gives reward(u*) > reward(c).
    - (F1): W_{t+1}(v) ⊵ W_{σ″}(v), whose cycle node is u*; so reward(λ(W_{t+1}(v))) ≥ reward(u*) > reward(c), against λ(W_{t+1}(v)) = c.
      (ii) does not occur. □
- Remarks.
  - On 𝒞^1O at H1 ∧ ¬H2 states, F_D = F, and BF-F_D is RESULTS R45 (d) BF-F. Its sub-case "x ∈ R̄_k" (impossible there by ¬H2: c_w beats c_θ) is
    replaced here by (i)'s XW step: entering a gate region is allowed and gives the same inequality, because the gate's W-value dominates its
    Ξ-value. No hypothesis on H1, H2, (h_D), (h3_D), the number of gates or the class is used.
  - (i) does not use v ∈ F_D(t); (ii) does. DATA: the inequality also held at the 25,600 + 693 + 115 checks with v ∈ F_D(t+1) only (column
    onlyk1 in bffd.py), unproved.

## 3. Theorem FREEZE-A (PROVED, every game)
Statement. Let c be a cycle node of a phase, U := U_c, A_t := F_D(t) ∩ U, and [s, e] states of the phase such that every transition t → t+1 with
s ≤ t < e is an S4a step and A_{t+1} ⊆ A_t. Let L := max(|A_s| − 1, 0).
- (a) For t ∈ [s, e], z ∈ A_t and every simple path p of G[A_t] from z to c with ≤ t − s edges: M_t(z) ≥ wt(p ∖ {c}).
- (b) For t ∈ [s, e] and z ∈ A_t: M_t(z) ≤ MoptA_t(z). Hence for s + L ≤ t ≤ t′ ≤ e and z ∈ A_{t′}: M_{t′}(z) = M_t(z) = MoptA_t(z).
- (c) Let q ∈ U be Odd. Over the states t ∈ [s + L, e] with σ̄_t(q) ∈ A_t, M_t(q) takes at most deg(q) values, in non-decreasing order. So at most
  deg(q) − 1 transitions t → t+1 with s + L ≤ t < e, σ̄_t(q) ∈ A_t and σ̄_{t+1}(q) ∈ A_{t+1} change M(q).
Proof.
- (a) Induction on t − s. If p has no edge, z = c and M_t(c) = 0 (A0κ). Step t → t+1: z ∈ A_{t+1}, z ≠ c, p = z · p′ with p′ from x, ≤ t − s
  edges. p is a path of G[A_{t+1}], which is a subgraph of G[A_t] (A_{t+1} ⊆ A_t; Even edges into A_{t+1} are edges into A_t; Odd vertices keep
  their τ-edge, τ constant on the phase). So p′ is a simple path of G[A_t] and, by induction, M_t(x) ≥ wt(p′ ∖ {c}); also wt(p ∖ {c}) = wt(z) +
  wt(p′ ∖ {c}).
  - z Even: z ∈ A_{t+1} ⊆ A_t, so z ∈ F_D(t) ∩ F_D(t+1), and BF-F_D gives M_{t+1}(z) ≥ wt(z) + M_t(x).
  - z Odd: z ∈ F_D(t+1), so z ∉ D_{t+1} and σ̄_{t+1}(z) = τ(z) = x, i.e. next_{t+1}(z) = x. (Aκ) at t + 1 and (M2κ): M_{t+1}(z) = wt(z) +
    M_{t+1}(x) ≥ wt(z) + M_t(x).
- (b) Let z ∈ A_t, z ≠ c. z's (σ_t, τ)-play avoids D_t, and at its Odd vertices σ̄_t = τ, so it is z's honest play. Every vertex y on it has a
  suffix of it as its own play, so y ∈ F_D(t), and λ(y) = c, so y ∈ U: the play stays in A_t. Up to its first visit of c it is a simple path
  (SP′) whose Even vertices use σ_t-edges into A_t and whose Odd vertices use τ-edges: a simple path of G[A_t]. By (Aκ), (A0κ) iterated, M_t(z) =
  wt(that path ∖ {c}) ≤ MoptA_t(z) (for z = c both sides are 0).
  - Simple paths of G[A_t] have ≤ |A_t| − 1 ≤ L edges. So for t ≥ s + L, (a) gives M_t(z) ≥ MoptA_t(z), hence M_t = MoptA_t on A_t.
  - For s + L ≤ t ≤ t′ and z ∈ A_{t′} ⊆ A_t: M_{t′}(z) = MoptA_{t′}(z) ≤ MoptA_t(z) = M_t(z) ≤ M_{t′}(z) (fewer paths; (M2κ)).
- (c) Let t ∈ [s + L, e] with y* := σ̄_t(q) ∈ A_t, and V_q := {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩ A_{s+L}} (≤ deg(q) values). We show
  M_t(q) ∈ V_q.
  - If q ∉ D_t: q's honest play is q followed by y*'s, which avoids D_t, so q ∈ A_t ⊆ A_{s+L}. By (b), M_t(q) = M_{s+L}(q). As q ∈ A_{s+L},
    q ∉ D_{s+L}, so next_{s+L}(q) = τ(q), which lies on q's play and hence in A_{s+L}, and (Aκ) gives M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ∈ V_q.
  - If q ∈ D_t: q's honest play continues in A_t and never returns to q (it avoids D_t ∋ q), so q lies on no honest cycle; q ≠ c (c lies on
    y*'s play, so c ∉ D_t). By κ-Y-FORM_D (R56 (d)), κ_t(q) = κwt(q) + min over y ∈ Y^q_t of κ_t(y), Y^q_t := {y ∈ succ(q) ∩ U : y's honest
    play at t avoids q}, and by (Aκ) the minimum is attained at y*. Every y ∈ succ(q) ∩ A_t lies in Y^q_t (its play avoids D_t ∋ q). The
    κ-order compares M first, so M_t(y*) ≤ M_t(y) for all those y, and y* is one of them. So M_t(q) = wt(q) + M_t(y*), and M_t(y*) =
    M_{s+L}(y*) by (b) (y* ∈ A_t ⊆ A_{s+L}). Hence M_t(q) ∈ V_q.
  - M(q) is non-decreasing over the phase (M2κ). So over the states of (c) it takes ≤ deg(q) values in non-decreasing order, and changes at
    ≤ deg(q) − 1 of the counted transitions. □
- Remarks.
  - On 𝒞^1O at H1 ∧ ¬H2 HN runs this is RESULTS R45 (e) FREEZE-F, with A = F ∩ U (there SPLIT, R39 (a), makes F non-increasing) and q = o.
  - FREEZE-A differs from RESULTS R55 F1°_D (Ξ-changes on F_D ≤ |F_D| − 1 per D-crossing-free interval) in two ways: A may shrink inside the
    interval, and (c) bounds a D-vertex's own path weight, which F1°_D does not touch (q ∈ D is not in F_D).
  - Lengths. On [s + L, e], Ξ on A changes only by length (P frozen, cycle node c), monotonically, and lengths lie in [1, |U| − 1] (SP′). So the
    Ξ-changes (not only the path-weight changes) of q counted as in (c) are ≤ deg(q)·(|U| − 1) − 1.

## 4. Corollary ROOT-PIECE (PROVED, every game)
Statement. Fix a phase with f in-phase fallbacks, a cycle node c, U := U_c, and G_c := the number of A-gains of class c in the phase. Cut the
phase at its fallback transitions and at its A-gains. For an Odd q ∈ U, let ρ^P_q(A) := the transitions t → t+1 of the phase with σ̄_t(q) ∈ A_t,
σ̄_{t+1}(q) ∈ A_{t+1} and M_t(q) ≠ M_{t+1}(q). Then
- ρ^P_q(A) ≤ (f + G_c + 1)·(|U| − 1 + deg(q) − 1) + f + G_c.
Proof. The ≤ f + G_c cut transitions count at most once each. The remaining transitions lie in ≤ f + G_c + 1 pieces [s, e], each satisfying
FREEZE-A's hypothesis. In a piece, transitions before s + L number ≤ L ≤ |U| − 1, and after it ≤ deg(q) − 1 by FREEZE-A (c). □
- With lengths (§3 remark): the Ξ-changes of q at such transitions are ≤ (f + G_c + 1)·(|U| − 1 + deg(q)·(|U| − 1)) + f + G_c.
- READING. A D-direct terminal (its chosen option's play avoids D) is the multi-gate form of "o at H1". The root r of nep90 is D-direct at every
  state of its long phase (rootdyn.py: r direct at all 91 states; σ̄(r) ∈ A at every state, rootrun.py).

## 5. DATA (experiments/si/root/; DATA, not proof)
- bffd.py (Lemma BF-F_D at every in-phase S4a transition; W computed by wplay, cross-checked against experiments/new/box21/h1.py wvals on the
  first states of each list):
  | set | checks | BFFD_V | onlyk1 checks (v ∈ F_D(t+1) only) | failures there |
  | --- | --- | --- | --- | --- |
  | lib41 (experiments/new/box41/lib41.txt, KMIN 1, n ≤ 48), S3 + 4 random starts, 1,601 phases | 1,195,562 | 0 | 25,600 | 0 |
  | lib2o (experiments/si/fb2o/lib2o.txt), S3 + 4, 75 phases | 36,738 | 0 | 693 | 0 |
  | nep90_n40 / nep76_n40 | 7,827 / 8,701 | 0 / 0 | 110 / 115 | 0 / 0 |
  Also W = Ξ on F_D at every checked state (W_NE_XI_ON_F = 0; R55 (a)). Control MUT=1 (equality flagged too) bites on nep90 at its first check.
- shrink.py (per fallback-free run and class: A-gains by cause; each run cut at its A-gains into pieces; on every piece FREEZE-A (a) at every
  state (bfa: walk Bellman-Ford with ≤ t − s edges, a simple witness searched by DFS when it exceeds M_t(z)), and on pieces longer than
  |A_s| − 1 the freeze (b) and the count (c)):
  | set | runs | entering vertices (DLEAVE / SWITCH / split) | pieces (long) | (a) checks (binding) | (b), (c) violations | MUT=1 (freeze from s) | MUT2=1 (one more edge) |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | lib41, S3 + 4 | 2,166 | 9,085 (8,802 / 283 / 0) | 2,845 (347) | 444,719 (193,765), 0 failures | 0 / 0 | bites (1,581) | bites (410) |
  | lib2o, S3 + 4 | 122 | 331 (323 / 8 / 0) | 149 (7) | 18,609 (5,417), 0 failures | 0 / 0 | does not bite (thin) | bites (2) |
  | nep90 / nep76 | 8 / 7 | 53 / 45, all DLEAVE | 20 / 13 (0) | 2,740 / 2,521, 0 failures | vacuous (no long piece) | – | does not bite |
  - "binding" counts the checks with equality. The DFS budget never ran out on the unmutated runs.
  - So the hypothesis "A does not grow" fails in 592 of 2,166 lib41 runs, and A grows almost always because D shrinks (8,802 of 9,085 entering
    vertices); the Even-switch exits (283) are all by unsplit vertices.
- rootrun.py, nep90 phase@4 (r = 0, ρ_r = 72): 22 cuts = 7 fallbacks + 15 A-gains, every A-gain a DLEAVE (the entering vertices' first D-vertex
  left D: Odd's best reply there moved back to τ), 0 by an Even switch. Per piece ρ_r ≤ 7 (bound 44-56). nep76 phase@9 (r = 0, ρ_r = 62): 15
  cuts = 6 fallbacks + 9 DLEAVE; per piece ρ_r ≤ 9. ROOTRUN_V = 0 on both; control MUT=1 (bound 2) bites on nep90 (10 pieces).
- READING. On these two instances the long ρ_r is (cuts + 1) × (short pieces): ρ_r ≈ 3 × (f + G_c). The pieces are where the ruler of L-RED R88
  lives: a block re-run needs a cut between its laps (FREEZE-A forbids a re-run of more than |A| − 1 + deg(r) − 1 path-weight changes in one
  piece). On nep90 the lap restart at state 50 is a fallback (L-NEW 27 §1), the other cuts are relays leaving D.

## 6. Answer to "say which", and what is open (READING / OPEN)
- The root count bites on R⁰ (the fallback-free returns of L-NEW 27's Theorem EP-C), not on NCONF. Inside one fallback-free run, the root's
  path-weight changes while it is D-direct are ≤ (G(S) + 1)(|U| + deg(r) − 2) + G(S), G(S) := the A-gains inside S (§4). So a fallback-free
  return of the root's configuration with no A-gain in between costs ≤ |U| + deg(r) − 2 root events, and long fallback-free stretches of root
  events need many A-gains.
- What this does NOT give (OPEN):
  - G_c, the A-gains per phase. Two kinds: DLEAVE (some u ∈ D_t with σ̄_{t+1}(u) = τ(u), an epoch boundary at which D shrinks) and SWITCH (an
    unsplit vertex leaves the D-region by an Even switch; split vertices never do, RESULTS R63 (a) R-STICK_D; data: SPLIT_IN = 0). On nep90 /
    nep76 all A-gains are DLEAVE. No bound on DLEAVEs is known: each is a clean change of σ̄(u) and strictly raises κ(u) (R61 (e) ALT), which is
    ρ again, but at a RELAY, not at the root.
  - The relays' own ROUTE events (their chosen exit is the root, a D-vertex, so they are not D-direct and FREEZE-A (c) does not apply). The
    candidate for them is a W-frame freeze on the root's gate region R_r with W(r) constant (DATA: constant on both long phases); there,
    for y, z with the same gate, the Ξ- and W-orders agree (G_D (c1)), so S4a acts on R_r as Bellman-Ford toward a fixed sink. OPEN: R_r changes
    36 times on each long phase, at D-joins and D-leaves of relays and at ping-pong moves.
  - f per phase on general games (L-NEW), and the root's non-D-direct states (on nep76 the root routes through a relay for 6 + 6 transitions).
- Labels. PROVED (lane, unrefereed): BF-F_D, FREEZE-A, ROOT-PIECE. DATA: §1's W(r) / R_r / split columns, §5. READING: §1's map and its
  consequence, §4's last remark, §5's last item, §6's first item. OPEN: G_c, the relays' ROUTE events, f.

## 7. The D-leaves G_c (Lead's NEXT (a), 14:25Z): data first, a decomposition, no bound (DATA, PROVED (elementary), READING, OPEN)
Written 2026-10-26T14:28Z (date -u). Script experiments/si/root/dleave.py; logs root/logs/dleave_*.txt.
A D-LEAVE at u is an in-phase transition t → t+1 with u ∈ D_t ∖ D_{t+1} (σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u)); a D-ENTER is the reverse. Every S4a
A-gain of type DLEAVE contains a D-leave. Per leave: y1 := σ̄_t(u) and its exit e1 (first vertex of Q_c ∪ {c} on y1's play at t); τ(u) and its
exit e2; COPY if e1 ≠ c and e1 has a ρ event at t → t+1 (CHOSEN's mechanism: the relay follows its chosen exit), OWN otherwise.
### 7.1 DATA
| set | leaves | at fallbacks | S4a, OWN, e1 = c (u "D-direct") | S4a, COPY | S4a, OWN, e1 a terminal | root ρ at the same transition | max leaves of one u per phase |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nep90 phase@4 | 26 | 6 | 15 | 5 | 0 | 10 | 9 |
| nep76 phase@9 | 21 | 2 | 11 | 6 | 2 | 15 | 8 |
| lib41 (KMIN 2), S3 + 4 | 148 | 4 | 55 | 41 | 48 | 141 | 2 |
| lib2o, S3 + 4 | 39 | 0 | 32 | 3 | 4 | 37 | 2 |
- Leaves ≤ enters + 1 per vertex and phase (checked: LV_GT_EN_V = 0, a consistency check).
- Outside nep90 / nep76 a vertex leaves D at most twice per phase. On the two long instances the relays 1, 6, 8, 17 (37) leave 4-9 times each.
- The commonest S4a leave (15 of 20 on nep90, 55 of 144 on lib41) is by a relay that is momentarily D-DIRECT: its chosen option and τ(u)'s
  option both exit at c, and Odd's best reply switches between two direct options (nep90: u = 6 between 38 and 25, u = 8 between 36 / 14 and
  30). The relay is then a second root of the class, with its own direct ROUTE events.
- So the Lead's first question has a negative answer in data: on nep90, 15 of the 20 S4a leaves are not copies of a root event (no ρ at the root
  at that transition in 16 of the 26 leaves).
### 7.2 Decomposition (PROVED, elementary; from landed lemmas). SUPERSEDED by packet P-N5-ROOT-box20 §5 Lemma DL-SPLIT (clean changes, TOG
alternative at e1, as in Lemma CHOSEN); case (ii) below is stated there with its proof.
For an S4a D-leave at u at t → t+1, with u on no honest cycle at t and t + 1:
- (i) COPY: e1 ≠ c and κ(e1) changes at t → t+1. Then the transition carries a ROUTE, CYC or TOG event of the class (Corollary RELAY-CHAIN,
  note §26.2, from e1's event).
- (ii) OWN with u's class exit paths and exits unchanged: then every option value of u is κwt(path) + κ(exit) with the same paths, exits other
  than e1 can only rise (in-phase monotonicity), y1's value is unchanged, so y1 stays a minimiser and σ̄ changes only between tied minimisers:
  the change is a TIE in the sense of RESULTS R61 (e). DATA (dleave.py, y_* counters): a RELAY leave is always a COPY (RELAY-and-OWN: 0 on
  nep90, nep76, lib41, lib2o), so case (ii) never occurred.
- (iii) otherwise u has a ROUTE event at t → t+1.
So every S4a D-leave transition carries a ROUTE / CYC / TOG event of its class or a tie; at fallbacks, at most |Q_c| leaves per fallback.
Hence G_c ≤ SWITCH-gains + f·|Q_c| + #(S4a transitions with a class ROUTE / CYC / TOG event or a tie at a leaving vertex).
### 7.3 READING: why this does not close, and what would
- With ROOT-PIECE this is self-referential: ρ_r ≤ (f + G_c + 1)·B and G_c ≤ f·|Q_c| + (ROUTE / CYC / TOG transitions) + SW, and the ROUTE
  events are ρ again. Nothing here bounds the product; nep90's 26 leaves are 15 D-direct own routes of relays + 5 copies + 6 at fallbacks.
- What the D-direct leaves are: two "roots" of one class whose own direct routes interleave. In FREEZE-A each one alone freezes in a piece, but a
  leave of one cuts the other's piece. A joint statement would need FREEZE-A on a region that does NOT lose its freeze at a D-leave of a
  D-direct terminal u. At such a leave the vertices gated at u keep their W-play (σ, τ unchanged by the leave itself) and their Ξ rises to W;
  so the cut is harmless in the W frame, and the obstruction is again Fact B across gates (§1): a W-frame Bellman-Ford step needs the Ξ-order of
  two options (it decides the arena) to agree with their W-order, which fails when one option is gated at u and the other is not.
- OPEN: a count of D-direct own leaves (two interleaving direct roots), a count of COPY leaves beyond "≤ |Q_c| × root events", and the
  SWITCH gains. CONJECTURE: none stated (data outside nep90 / nep76 is too small: ≤ 2 leaves per vertex per phase).

## 8. GO (x) (Lead 14:40Z): FREEZE-A on A ∪ {D-direct gates} FAILS in its naive form; the obstruction is the gate offset (Lemma GATE-SHIFT, PROVED; DATA; counterexample shape GATE-LAG for L-RED)
Written 2026-10-26T14:45Z (date -u). Script experiments/si/root/bfgate.py; logs root/logs/bfgate_*.txt; scratch probe for §8.2's grouping.
### 8.1 Setting
DD_t := {u ∈ D_t ∩ U : σ̄_t(u) ∈ A_t and τ(u) ∈ A_t} (D-DIRECT GATES: both continuations direct). B_t := A_t ∪ {z ∈ U : the first D_t-vertex of
z's (σ_t, τ)-play lies in DD_t}. For u ∈ DD_t, its OFFSET Δ_t(u) := M_t(τ u) − M_t(σ̄_t u).
### 8.2 DATA: the naive extension fails, at the root's own gate region
- BFG (BF-F_D's inequality M_{t+1}(z) ≥ wt(z) + M_t(x) at Even z ∈ (B_t ∖ A_t) ∩ B_{t+1}, x ∈ succ(z) ∩ U):
  | set | checks | failures | cuts (fallbacks + A-gains) | cuts (fallbacks + B-gains) | long B-pieces, freeze failures |
  | --- | --- | --- | --- | --- | --- |
  | nep90 phase@4 | 948 | 188 | 22 | 18 | 0, – |
  | nep76 phase@9 | 639 | 138 | 15 | 25 | 0, – |
  | lib2o, S3 + 4 | 7,425 | 387 | 117 | 89 | 4, 0 |
  | lib41 (KMIN 2), S3 + 4 | 8,448 | 568 | 213 | 163 | 26, 0 |
- nep90, grouped (scratch probe): ALL 188 failures are in the gate region of the ROOT 0 itself (0 ∈ DD at those states), every one at an edge
  (z, x) that is Ξ-improving at t with x ∈ A_t that z does not take because W_t(σ_t z) ▷ W_t(x). The gap level of the root (top rank of
  P(Ξ(0)) Δ P(W(0))) is 36-39 at n = 40 at the failing states. The gate region of the D-direct relay 6: 24 checks, 0 failures.
- So B is not a better region: it loses the Bellman-Ford step exactly where the root's W-value runs ahead of its Ξ-value (the ping-pong of §1),
  and on nep76 it even has more cuts than A (25 > 15).
### 8.3 Lemma GATE-SHIFT (PROVED, every game)
Statement. Fix a phase and class c, U := U_c.
- (a) At a state t, for z ∈ U whose first D_t-vertex u := u(z) lies in DD_t: W_t(z) has cycle node c, and M_t(z) = MW_t(z) − Δ_t(u), with
  Δ_t(u) ≥ 0.
- (b) At an in-phase S4a transition t → t+1, for Even z ∈ U, z ≠ c, whose first D_{t+1}-vertex u lies in DD_{t+1}, and every successor x ∈ U of z
  whose (σ_t, τ)-play avoids z: MW_{t+1}(z) ≥ wt(z) + M_t(x); hence M_{t+1}(z) ≥ wt(z) + M_t(x) − Δ_{t+1}(u).
Proof.
- (a) Let π be z's (σ_t, τ)-path before u. Its Odd vertices are not in D_t, so σ̄_t = τ there, and z's honest play is π, u, then σ̄_t(u)'s play; z's
  W-play is π, u, then τ(u)'s play. Both continuations lie in A_t ⊆ F_D(t), hence avoid D_t and are disjoint from π (π's vertices lie in R_D(t))
  and avoid u. τ(u)'s play is its honest play and W = Ξ there (G_D (a)), with cycle node c. So both plays are lassos ending on c's cycle, z is on
  neither cycle, and summing wt over distinct vertices (as in §2 (ii)): M_t(z) = wt(π) + wt(u) + M_t(σ̄_t u) and MW_t(z) = wt(π) + wt(u) +
  M_t(τ u). τ(u)'s play avoids D_t ∋ u, so τ(u) ∈ Y^u_t; u is on no honest cycle (σ̄_t(u)'s play avoids u), so by κ-Y-FORM_D the minimum of κ
  over Y^u_t is attained at σ̄_t(u), and κ compares M first: M_t(σ̄_t u) ≤ M_t(τ u). So Δ_t(u) ≥ 0 and the identity holds.
- (b) By (a) at t + 1, W_{t+1}(z) has cycle node c and M_{t+1}(z) = MW_{t+1}(z) − Δ_{t+1}(u); it remains to show MW_{t+1}(z) ≥ wt(z) + M_t(x).
  - If M_t(x) ≤ M_t(σ_t z): (Aκ) and XW give wt(z) + M_t(x) ≤ M_t(z) ≤ MW_t(z) when W_t(z) has cycle node c (XW: Ξ_t(z) ⊴ W_t(z); if the cycle
    nodes differed, reward(λ(W_t z)) > reward(c)); and WM-G (RESULTS R62 (d): W never drops at an in-phase S4a step) gives W_{t+1}(z) ⊵ W_t(z).
    If W_t(z) had a cycle node of larger reward, W_{t+1}(z) ⊵ W_t(z) would contradict λ(W_{t+1} z) = c; so MW_{t+1}(z) ≥ MW_t(z) ≥ wt(z) +
    M_t(x) by (M1κ).
  - Otherwise (z, x) ∈ Iσ_t, σ″ := σ_t[z ↦ x] lies in the arena H_t, and §2 (i)'s argument applies verbatim with W_{t+1}(z) in place of Ξ_{t+1}(z)
    (it used only that W_{t+1}(z) has cycle node c): MW_{t+1}(z) ≥ wt(z) + MW_t(x) ≥ wt(z) + M_t(x). □
- DATA (bfgate.py, GS_A_V / GS_B_V): (a) 684 / 404 / 4,366 / 5,420 checks and (b) 943 / 661 / 5,868 / 7,044 checks on nep90 / nep76 /
  lib2o / lib41 (S3 + 4, KMIN 2), 0 failures. The control is BFG itself, i.e. (b) with Δ := 0: it fails 188 / 138 / 387 / 568 times (§8.2).
- So inside a D-direct gate region the honest Bellman-Ford step holds up to the gate's offset Δ(u), and the W-step holds exactly. A FREEZE on B
  would need Δ constant on the piece; after A's freeze (FREEZE-A (b)) Δ(u) takes ≤ deg(u) values (both terms are frozen values of A-vertices),
  but in a piece that has not yet frozen, Δ(u) moves with every root ρ event.
### 8.4 The obstruction, named (READING; counterexample SHAPE GATE-LAG for L-RED, not a counterexample to any statement of N5)
GATE-LAG: a D-direct gate u with a large offset Δ(u) (its W-continuation τ(u) beats Odd's best reply σ̄(u) at a high level), an Even z in u's
gate region, and a Ξ-improving direct option x of z with M(x) − M(σ z) < Δ(u). S4a keeps z on the gate (W-best), so Ξ(z) lags its direct
Bellman-Ford value by up to Δ(u). The lag is released when Δ(u) shrinks (σ̄(u) rises: a ρ event at u) or u leaves D; a fallback (Ξ-best) also
releases it and moves z off the gate. This is §1's ping-pong in Bellman-Ford terms, and it is where "Fact B across gates" fails: z's two
options sit behind different gates (u and none), and their Ξ- and W-orders disagree by exactly Δ(u). nep90 phase@4: u = 0 (the root),
gap level rank 36-39 of 40, 188 lagging (z, x) pairs over the phase (z ∈ {12, 23, 34, 36, …}).
- What a proof would need: a bound on how often Δ(u) changes inside a piece, i.e. on ρ at u itself. For the root that is the quantity we
  started from. For relays (small offsets in data: gate 6 on nep90, 0 lags), GATE-SHIFT (b) would give a freeze on their gate regions once
  their offsets are constant, but the relays' D-leaves are not where the cuts come from on nep90 alone (§7.1: they are 15 of 26 leaves).
- Labels: PROVED (lane): GATE-SHIFT (a), (b). DATA: §8.2. READING: §8.4. OPEN: a freeze on any region that contains the root's gate region.

## 9. GO (q) (Lead 14:53Z): the gate-region freeze in the W frame (Theorem FREEZE-G, Corollary RELAY-PIECE, PROVED; DATA)
Written 2026-10-26T14:56Z (date -u). Script experiments/si/root/freezeg.py; logs root/logs/freezeg_*.txt.
### 9.1 Setting
Fix a phase, class c, U := U_c, an Odd u ∈ U, u ≠ c. R_u(t) := {z ∈ U : the first D_t-vertex of z's (σ_t, τ)-play is u} (u ∈ R_u(t) iff
u ∈ D_t). E_t := A_t ∪ R_u(t). OFFSET off_t(z) := 0 for z ∈ A_t, Δ_t(u) for z ∈ R_u(t). N_t(z) := MW_t(z) (the path weight of W_t(z)) for
z ∈ E_t; N_t = M_t on A_t (G_D (a)). G′[E]: A-vertices keep their edges into A (Even) or their τ-edge into A (Odd); R_u-vertices keep their
edges into E (Even) or their τ-edge into E (Odd, u included); c is a sink. MoptG′[E](z) := the best wt-weight of a simple G′[E]-path from z to c.
A G-INTERVAL for u: states [s, e] such that every transition t → t+1 (s ≤ t < e) is an in-phase S4a step, u ∈ DD_t for all t ∈ [s, e]
(u ∈ D_t, σ̄_t(u) ∈ A_t, τ(u) ∈ A_t), A_{t+1} ⊆ A_t, R_u(t+1) ⊆ R_u(t), and Δ_t(u) = Δ is constant.
### 9.2 Theorem FREEZE-G (PROVED, every game)
On a G-interval [s, e] for u, with L := |E_s| − 1:
- (a) for t ∈ [s, e], z ∈ E_t and every simple path p of G′[E_t] from z to c with ≤ t − s edges: N_t(z) ≥ wt(p ∖ {c});
- (b) N_t(z) ≤ MoptG′[E_t](z); hence for s + L ≤ t ≤ t′ ≤ e and z ∈ E_{t′}: N_{t′}(z) = N_t(z), and M_{t′}(z) = M_t(z) (M = N − Δ on R_u, by
  GATE-SHIFT (a));
- (c) for every Odd q ∈ U ∖ {u, c}: over the states t ∈ [s + L, e] with σ̄_t(q) ∈ E_t, M_t(q) takes ≤ deg(q) values, non-decreasing; so ≤ deg(q) −
  1 transitions t → t+1 in [s + L, e) with σ̄(q) ∈ E at both ends change M(q).
Proof.
- Facts on E_t (from GATE-SHIFT (a) and its proof): for z ∈ R_u(t), W_t(z) has cycle node c and M_t(z) = N_t(z) − Δ; z's W-play is π_z, u, then
  τ(u)'s play in A_t, so for z ∈ R_u(t) ∖ {u}, next on the W-play is σ_t(z) (Even) or τ(z) (Odd), it lies in R_u(t), and N_t(z) = wt(z) +
  N_t(next z) (summing wt over distinct vertices, as in §2 (ii)); N_t(u) = wt(u) + M_t(τ u). N is non-decreasing on R_u along the interval: z ∈
  R_u(t+1) ⊆ R_u(t), W never drops at an in-phase S4a step (RESULTS R62 (d) WM-G), and both values have cycle node c. On A, N = M, non-decreasing
  (M2κ).
- (a) Induction on t − s; the base is N_t(c) = 0. Step t → t+1, z ∈ E_{t+1}, z ≠ c, p = z · p′, p′ from x, ≤ t − s edges; G′[E_{t+1}] ⊆ G′[E_t]
  (both parts non-increasing; the edge rule depends only on membership), so by induction N_t(x) ≥ wt(p′ ∖ {c}).
  - z ∈ A_{t+1}: then x ∈ A_{t+1} (G′ keeps A-edges into A), and FREEZE-A (a)'s step applies verbatim (BF-F_D for Even z; the τ-edge for Odd z).
  - z = u: x = τ(u) ∈ A_{t+1}; N_{t+1}(u) = wt(u) + M_{t+1}(τ u) ≥ wt(u) + M_t(τ u) = wt(u) + N_t(x).
  - z ∈ R_u(t+1) Odd, z ≠ u: z ∉ D, x = τ(z) = next(z); N_{t+1}(z) = wt(z) + N_{t+1}(x) ≥ wt(z) + N_t(x) (x ∈ E_{t+1}; N non-decreasing).
  - z ∈ R_u(t+1) Even: z ∈ R_u(t) and σ_t(z) ∈ R_u(t), so off_t(σ_t z) = Δ ≥ off_t(x) (x ∈ E_t).
    - Case 1, M_t(x) ≤ M_t(σ_t z): N_t(x) − off_t(x) ≤ N_t(σ_t z) − Δ, so N_t(x) ≤ N_t(σ_t z); then wt(z) + N_t(x) ≤ wt(z) + N_t(σ_t z) = N_t(z)
      ≤ N_{t+1}(z).
    - Case 2, (z, x) ∈ Iσ_t: σ″ := σ_t[z ↦ x] is in the arena H_t; (F1): W_{t+1}(z) ⊵ W_{σ″}(z). If x's (σ_t, τ)-play avoids z, W_{σ″}(z) = z ⊕
      W_t(x), and as in §2 (i) (XW for the cycle node, W_{t+1}(z) has cycle node c) N_{t+1}(z) ≥ wt(z) + N_t(x). If it passes z, it is q · z ·
      (z's play) and N_t(x) = wt(q) + N_t(z); under σ″, z's play is the cycle Z := z → x → q → z; if wt(Z) > 0 its top is even above c and
      (F1) contradicts λ(W_{t+1} z) = c (§2 (ii)); so wt(Z) = wt(q) + wt(z) ≤ 0 and wt(z) + N_t(x) = wt(Z) + N_t(z) ≤ N_t(z) ≤ N_{t+1}(z).
- (b) z ∈ E_t: z's W-play up to c is a simple path of G′[E_t] (R_u part: σ_t-edges and τ-edges inside R_u, then u's τ-edge into A; A part:
  edges inside A), so N_t(z) = its weight ≤ MoptG′[E_t](z). Simple paths of G′[E_t] have ≤ L edges, so for t ≥ s + L, (a) gives equality,
  and for s + L ≤ t ≤ t′: N_{t′}(z) = MoptG′[E_{t′}](z) ≤ MoptG′[E_t](z) = N_t(z) ≤ N_{t′}(z). M = N − off with off constant on the interval.
- (c) Let t ∈ [s + L, e] with y := σ̄_t(q) ∈ E_t. If q ∉ D_t: q's honest and W-plays agree up to their first D_t-vertex and q ∈ E_t (its play is
  q then y's, whose first D-vertex is u or none), so M_t(q) = M_{s+L}(q) by (b): one value, also of the form wt(q) + M_{s+L}(τ q) with τ q ∈
  E_{s+L} (q ∉ D_{s+L}, τ q on q's play). If q ∈ D_t: q's honest play is q then y's play; y ∈ E_t, and y's honest play does not return to q (if
  y ∈ A_t it avoids D_t ∋ q; if y ∈ R_u(t) it is π_y, u, σ̄_t(u)'s play in A_t, and π_y has no D_t-vertex), so q is not on its cycle and (Aκ)
  gives M_t(q) = wt(q) + M_t(y) = wt(q) + M_{s+L}(y) by (b) (y ∈ E_t ⊆ E_{s+L}). Either way M_t(q) ∈ {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩
  E_{s+L}}, ≤ deg(q) values; M(q) is non-decreasing on the phase (M2κ). □
### 9.3 Corollary RELAY-PIECE (PROVED, every game)
Let [s, e] be a FREEZE-A piece (§3) with L_A := |A_s| − 1, and u ∈ DD_t at every t ∈ [s, e] with R_u non-increasing. Then on [s + L_A, e] the
offset Δ(u) takes ≤ deg(u) values (both terms are frozen A-values: M(τ u) by FREEZE-A (b), M(σ̄ u) ∈ V_u by FREEZE-A (c)), so [s + L_A, e] splits
into ≤ deg(u) G-intervals. In each, after ≤ |E| − 1 steps, every relay q whose chosen option lies in E (in A or in u's gate region) changes its
path weight ≤ deg(q) − 1 times. So per FREEZE-A piece, a relay q of u (chosen option in E) has ≤ L_A + deg(u)·(|U| − 1 + deg(q)) path-weight
changes at transitions with its chosen option in E at both ends.
- What it gives: the relays' own ROUTE events (the open item of §6) are bounded per piece, GIVEN the pieces: a relay of a D-direct gate cannot
  re-route more than deg(q) − 1 times between consecutive changes of its gate's offset, once A and the gate region have frozen.
- What it does not give: the number of pieces (fallbacks, A-gains, gate-region gains such as the ping-pong entries into the root, §8), and
  relays whose chosen option lies behind a gate that is not D-direct.
- The root: FREEZE-G applies to the root's own gate region too (u = 0 on nep90): GATE-LAG (§8) is a failure of the Ξ-step, but the W-step
  (N) is exact and freezes; the honest values there are N − Δ(0) and move only when Δ(0) moves, i.e. at ρ events of the root.
### 9.4 DATA (freezeg.py)
| set | G-intervals | (a) checks (binding) | (a) failures | intervals longer than |E| − 1 |
| --- | --- | --- | --- | --- |
| nep90 / nep76 | 22 / 25 | 2,531 (332) / 2,386 (214) | 0 / 0 | 0 / 0 |
| lib2o (KMIN 2), S3 + 4 | 120 | 15,878 (3,555) | 0 | 0 |
| lib41 (KMIN 1), S3 + 4 | 729 | 95,488 (21,311) | 0 | 0 |
- Control MUT=1 (one more edge than (a) allows): bites on lib41 (11, e.g. so_sor5_n24); does not bite on nep90, nep76, lib2o.
- (b), (c) and RELAY-PIECE are VACUOUS in data: no G-interval outlives its freeze window. They rest on their proofs. G-intervals are short
  because Δ(u) changes at every ρ event of u and the gate region gains at every ping-pong entry.
### 9.5 Status, labels
- PROVED (lane, unrefereed): FREEZE-G (a)-(c), RELAY-PIECE. DATA: §9.4 ((a) non-vacuous with a biting control on lib41; (b), (c) vacuous).
- READING: the relays' ROUTE events are bounded per G-interval; what is unbounded is the number of intervals, i.e. the changes of the gates'
  offsets (ρ at the gates) and the gate-region gains (ping-pong entries), together with fallbacks and A-gains. The open count is the same
  one as in §6-§8, now stated per gate: how often a D-direct gate's offset or region can be reset inside one fallback-free run.

## 10. The per-gate reset count (Lead's 15:02Z item): charges in data, one dead charge, Corollary RESET-PIECE (PROVED), what stays open
Written 2026-10-26T15:11Z (date -u). Script experiments/si/root/resets.py; logs root/logs/resets_*.txt.
### 10.1 DATA: the resets of a D-direct gate inside fallback-free runs, and their charges
At an in-phase S4a transition with u ∈ DD_t, a RESET of u is: LEAVE (u ∉ DD_{t+1}), DELTA_U (Δ(u) changes with M(σ̄ u) changing, i.e. u's own
path weight), DELTA_T (Δ(u) changes via M(τ u) only), RGAIN (R_u gains), AGAIN (A gains). Charges at the same transition: ROOT (Ξ of the class
root r changes, u ≠ r), SELF (Ξ(u) changes), PING (an Even vertex outside R_u(t) switches into R_u(t)), FLIP (some Odd choice vertex of the class
changes its chosen exit). ONLYSELF: no charge but SELF.
| set | resets (root / relays) | root DELTA_U (ONLYSELF) | root RGAIN (with PING) | relay DELTA_U (with ROOT) | relay LEAVE (ONLYSELF) | R_u gains from A / from another gate's region | max resets of one gate in one run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nep90 phase@4 | 76 / 21 | 63 (32) | 22 (17) | 7 (7) | 10 (8) | 72 / 14 | 13 |
| nep76 phase@9 | (86 in all) | 51 (13) | 25 (17) | 10 (10) | 13 (0) | 54 / 12 | 12 |
| lib2o (KMIN 2), S3 + 4 | 186 / 89 | 21 (15) | 136 (136) | 7 | 33 | 275 / 1 | 18 |
| lib41 (KMIN 2), S3 + 4 | 175 / 173 | 18 (13) | 110 (110) | 11 | 80 | 253 / 29 | 18 |
- Relay offset resets on the long instances are all at a root ρ event (7 / 7, 10 / 10): copies, CHOSEN's mechanism.
- Root region gains carry a ping-pong entry in every library case (136 / 136, 110 / 110) and in 17 of 22 / 17 of 25 on nep90 / nep76; the
  rest are merges from another gate's region (with FLIP or SELF).
- DEAD CHARGE (recorded in docs/si/DEAD.md "DEAD box 20"): "every reset of the root's offset is charged to a ping-pong entry or a FLIP event at the
  same transition" is FALSE: nep90 phase@4 has 32 of 63 root offset resets with no charge but the root's own ρ (nep76: 13 of 51). They are the
  Bellman-Ford cascade events of the direct region (§1, note §28.2's PATH triggers), i.e. FREEZE-A (c) events inside pieces.
### 10.2 Corollary RESET-PIECE (PROVED, every game)
Let [s, e] satisfy FREEZE-A's hypothesis (§3), L_A := |A_s| − 1, and u ∈ DD_t for every t ∈ [s, e]. Then inside [s, e]:
- (i) Δ(u) changes at ≤ L_A + deg(u) − 1 transitions;
- (ii) the transitions at which R_u gains a vertex coming from A number ≤ |A_s|;
- (iii) the transitions at which R_u gains a vertex coming from another gate's region are NOT bounded here (OPEN; data: 14 / 12 vertices on
  nep90 / nep76, 29 on lib41).
Proof. (i) At most L_A transitions lie before s + L_A. For t ≥ s + L_A: τ(u), σ̄_t(u) ∈ A_t, so M_t(τ u) = M_{s+L_A}(τ u) (FREEZE-A (b)), and
M_t(σ̄_t u) = M_t(u) − wt(u) ((Aκ); u is on no honest cycle) with M_t(u) ∈ V_u (FREEZE-A (c)) non-decreasing: Δ(u) takes ≤ deg(u) values
there, in non-increasing order, and changes ≤ deg(u) − 1 times. (ii) A is non-increasing on [s, e], so a vertex leaves A at most once; each such
transition is counted once. □
- So inside a FREEZE-A piece the resets of a D-direct gate are polynomial except the cross-gate migrations (iii). Together with ROOT-PIECE
  (pieces ≤ f + G_c + 1) the per-gate reset count per phase is ≤ (f + G_c + 1)·(2|U| + deg(u) + X_u), X_u := the cross-gate migrations into
  R_u: a REDUCTION to f, G_c and X_u.
### 10.3 Status, labels
- PROVED (lane): RESET-PIECE (i), (ii). DATA: §10.1. DEAD: the PING / FLIP charge for root offset resets (nep90 phase@4, 32 of 63).
- OPEN: G_c (A-gains: relay D-leaves and unsplit exits), X_u (cross-gate migrations into a gate region), f. The three lines the Lead named
  (relay changes per fallback-free run, NCONF_{≥2}, R⁰_{≥2}) all reduce, through ROOT-PIECE, FREEZE-G and RESET-PIECE, to G_c and X_u per
  fallback-free run; no bound on either is proved here.
