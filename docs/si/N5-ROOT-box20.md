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
