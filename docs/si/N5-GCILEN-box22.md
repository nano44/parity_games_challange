# N5-GCILEN (box 22): GCI-LEN on ρ-free intervals. Where σ̄ is constant and the end-state dependency graph is acyclic, N5 settles by depth, so the interval has length ≤ n − 1
L-SI successor 18 (Opus 5.5; D18, Lead reading L40). Lead's queue 17:47Z: «GCI-LEN, a new proof target from L-RED 22 (l-red 54de3f2f, R91 §5):
every global C-interval of a λ_W-constant fallback-free run has length ≤ n − 1». Working note, unrefereed; not frozen. Not a TARGET.md claim.
Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
Labels: PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING.
Tools: experiments/si/root/staticdepth.py. Logs: experiments/si/root/logs/staticdepth_*.txt.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | setting; the dependency graph H_b; hypotheses (H1)-(H4), GEN_W | definitions |
| §2 | Theorem STATIC-DEPTH: under (H1)-(H4) and GEN_W, every vertex's W-play and honest play are final from index d*(v) on; the interval has length ≤ max d* ≤ n − 1 | PROVED (lane; landed premises only) |
| §2 | Corollary PURE-END: (H4) holds when every gate is D-direct at the last state; then every cycle is common to both frames | PROVED (elementary) |
| §3 | Corollary GCI-LEN-ρF: GCI-LEN holds for every global C-interval on which σ̄ is constant, (H3) holds and H_b is acyclic (in particular pure at its end) | PROVED (lane) |
| §4 | data: what the theorem covers and what it does not | DATA |
| §5 | what is left for GCI-LEN | OPEN + READING |

## 1. Setting (every game)
- Valuations, ⊴ and ⊕ as SPEC S1 / VJ00 (docs/new/N5-ssi-global.md). The valuation of a play from v is (cycle node c, P, ℓ). If v is not on
  its play's cycle, val(v) = v ⊕ val(next v), where ⊕ puts v into P when rank(v) > rank(c) and adds 1 to ℓ. A cycle vertex at distance ℓ from
  c along the cycle has valuation (c, ∅, ℓ).
- Ξ_t(v): the valuation of v's honest play (σ_t at Even vertices, σ̄_t at Odd vertices). W_t(v): the valuation of v's W-play ((σ_t, τ)).
  D_t := {Odd u : σ̄_t(u) ≠ τ(u)} (the gates). A_t := the vertices whose W-play meets no gate. A gate u is D-direct at t if σ̄_t(u), τ(u) ∈ A_t.
- An interval [a, b] of a phase with these hypotheses:
  - (H1) Every transition t → t + 1, a ≤ t < b, is an S4a step (no fallback). τ, λ (honest cycle nodes) and λ_W (W cycle nodes) are constant
    on [a, b].
  - (H2) σ̄_t = σ̄_a for every t ∈ [a, b]: a ρ-free interval in the sense of RESULTS R69 (d) STATIC. So D is constant, and σ̄ = τ off D.
  - (H3) At every t ∈ [a, b], the W-cycles and the honest cycles are the same cycles (as vertex sequences), and they do not change on [a, b].
    The CYCLE VERTICES are the vertices on them.
  - (H4) H_b is acyclic outside the cycle vertices. H_b has an edge v → σ_b(v) for Even v, v → τ(v) for Odd v ∉ D, and two edges u → τ(u),
    u → σ̄(u) for u ∈ D. Cycle vertices are sinks.
- d*(v) := 0 for cycle vertices; 1 + d*(σ_b v) for Even v; d*(τ v) for Odd v ∉ D; max(d*(τ u), d*(σ̄ u)) for u ∈ D. So d*(v) is the largest
  number of non-cycle Even vertices on an H_b-path from v. Every such path ends at a cycle vertex, so d*(v) ≤ n − 1.
- GEN_W: for every v, two different W-plays from v (paths to the same cycle) never have equal W-valuations. This fails only at W-ties
  (equal P and equal length).
- Premises (LANDED): SPEC S4a's step is Even's pointwise W-optimum among the strategies using only arena edges {σ_t(v)} ∪ Iσ_t(v) (premise
  P2 of 1E-N3, as listed in RESULTS R69); (SW) every Even switch is to an edge of Iσ_t; RESULTS R15 (a) (Ξ_t ⊴ Ξ_{t+1} pointwise at in-phase
  transitions); RESULTS R69 (d) STATIC (for the reading of (H2) only).

## 2. Theorem STATIC-DEPTH (PROVED, lane, unrefereed)
Statement. Under (H1)-(H4) and GEN_W, for every non-cycle vertex v and every t ∈ [a + d*(v), b]: v's W-play and honest play at t equal those
at b. Hence σ_t = σ_b for t ∈ [a + max d*, b], and b − a ≤ max_v d*(v) ≤ n − 1.
Facts.
- (W-MONO) W_{t+1} ⊵ W_t pointwise for a ≤ t < b. σ_t uses only its own choices, which are arena edges, so it is a candidate, and the step is
  pointwise W-optimal among candidates.
- (Ξ-SUCC) Ξ_t(σ_t v) is non-decreasing in t on [a, b] for Even v. Kept: Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) (R15 (a)). Switched: σ_{t+1}(v) ∈ Iσ_t(v)
  ((SW)), so Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v).
- (CV) Cycle vertices have constant W- and Ξ-valuations and constant plays on [a, b], by (H1) and (H3).
Proof. Induction along H_b (acyclic by (H4)), in the order of d*. Call v SETTLED from s if its W-play and honest play at every t ∈ [s, b] equal
those at b. Cycle vertices are settled from a by (CV).
- Odd v ∉ D. By (H2), σ̄_t(v) = τ(v) for every t, so both of v's plays are v followed by τ(v)'s plays. v is settled from wherever τ(v) is.
- Gate u ∈ D. By (H2), σ̄_t(u) = σ̄_b(u) for every t. u's W-play is u·(τ(u)'s W-play), and its honest play is u·(σ̄(u)'s honest play). u is
  settled from max of the two.
- Even v, y* := σ_b(v), with y* settled from s := a + d*(y*).
  - (A) For every t ∈ [s, b], y* ∈ {σ_t(v)} ∪ Iσ_t(v). Otherwise σ_t(v) ≠ y* and Ξ_t(y*) ⊴ Ξ_t(σ_t v). Since σ_b(v) = y*, v switches to y* at
    some t′ → t′ + 1 with t ≤ t′ < b. Then (SW) gives Ξ_{t′}(y*) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y*) (Ξ-SUCC). But Ξ_{t′}(y*) = Ξ_t(y*),
    because y* is settled and a valuation is a function of the play. Contradiction.
  - (B) Let t ∈ [s, b − 1] and s′ := σ_{t+1} with v's choice replaced by y*. By (A), s′ uses only arena edges of state t. y*'s W-play under
    σ_{t+1} is its W-play at b (t + 1 ≥ s). That play does not contain v: v is not a cycle vertex, so v's W-play at b is v·(y*'s W-play), a
    simple path followed by a cycle not through v. So y*'s W-play under s′ is the same, and W_{s′}(v) = v ⊕ W_b(y*) = W_b(v). Pointwise
    optimality of the step gives W_{t+1}(v) ⊵ W_b(v). W-MONO gives W_{t+1}(v) ⊴ W_b(v). So W_{t+1}(v) = W_b(v).
  - By GEN_W, v's W-play at t + 1 is its W-play at b, so σ_{t+1}(v) = y*. Then v's honest play at t + 1 is v·(y*'s honest play at t + 1) = v's
    honest play at b. So v is settled from s + 1 = a + d*(v).
- Conclusion. At t ≥ a + max d*, every non-cycle Even vertex has σ_t(v) = σ_b(v), because the first step of its W-play is fixed. Cycle Even
  vertices have it by (H3). So σ_t = σ_b on [a + max d*, b]. Every transition of [a, b] changes σ: τ is constant, and an S4a step with no
  change is a fallback (SPEC; n5x.step sets fb when σ and τ are unchanged). So b ≤ a + max d*. □
- Remarks. (i) This is P-N5-GCX's abstract-model argument (N5-ABSCYC-box22 Theorem ABS-DEPTH) carried out on N5 itself. It needs no frozen A,
  no constant gate terminals and no offsets. The model's M is Ξ, its N is W, and its terminals become the cycle vertices plus the
  σ̄-fixed gates. So it is lift (L1) of N5-ABSCYC §4, done for ρ-free intervals. (ii) Odd vertices cost no step: Odd's choices are fixed on
  the interval by (H2), and only Even's induction steps add 1. (iii) (A) uses only Ξ. (B) and GEN_W use only W. Ties: a W-tie can break the
  per-vertex statement, as in N5-ABSCYC §3's model instance; the length bound is then OPEN.
Corollary PURE-END (PROVED, elementary). If every gate is D-direct at b, then (H4) holds, and every cycle at b is common to both frames.
Proof. For z ∈ A_b, z's W-play meets no gate, and σ̄ = τ off D, so z's honest play is its W-play. Its H_b-path is that one play, ending in a
common cycle inside A_b. For v ∉ A_b, the W-play meets a first gate u, and every H_b-path from v is (v's W-play up to u, which has no other
gate), then τ(u) or σ̄(u) ∈ A_b, then that vertex's play inside A_b. The two parts are disjoint (vertices of the first part are not in A_b),
and each is simple. W-cycles are reached through A_b, so they lie in A_b and are honest cycles too. Honest cycles are reached through
σ̄(u) ∈ A_b or inside A_b, so they lie in A_b and are W-cycles. □ (Constancy of the cycles on [a, b], i.e. (H3), is still a hypothesis.)

## 3. Corollary GCI-LEN-ρF (PROVED, lane)
Every global C-interval of a λ_W-constant fallback-free run (P-N5-GCX §1; R91 §5) on which σ̄ is constant, and which satisfies (H3) and (H4),
has length ≤ max d* ≤ n − 1, under GEN_W. By PURE-END, (H4) can be replaced by: every gate is D-direct at the interval's last state.
- Relation to R91. R91 §3 proves the case D = ∅ (per class, bound |U_c| − 1, by value iteration and without (H3)). GCI-LEN-ρF is a different
  case: gates are allowed, σ̄ must be fixed and cycles constant. Neither contains the other.
- With UL-RED (P-N5-GCX §3): GCI-LEN implies UL_G. So for runs whose global C-intervals all satisfy §3's hypotheses, Corollary UL-RED's
  bounds hold unconditionally (|U(S)| ≤ n_E((n − 1)(K(S) + 1) + K(S))), with GEN_W.

## 4. DATA (experiments/si/root/staticdepth.py; logs root/logs/staticdepth_*.txt)
Checked on every σ̄-constant interval (default mode) and every global C-interval (GCI=1): SETTLE_V (a vertex not settled from a + d*(v)),
LEN_V (length > max d*), N1_V / GCI_N1_V (length > n − 1). Control MUT=1 (d* − 1) must bite.
| sample | σ̄-constant intervals: all / (H3)+(H4) checked / with gates | longest checked (with gates) | violations | global C-intervals: σ̄ const / σ̄ changes (longest) |
| --- | --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt, n ≤ 48, S3 + 2 random starts) | 1,709 / 1,368 / 906 | 44 (26) | 0 | 1,480 / 444 (40) |
| random 𝒞^kO (3,000 games, n 8-24, seed 51) | 700 / 563 | 3 | 0 | (not run) |
| nep90 / nep76 / long121 (n 40) | 2 / 1 / 28 checked | 1 / 1 / 6 | 0 | 2 / 8, 1 / 8, 27 / 2 (≤ 6) |
| L-NEW's climbs n64 (s61, s63), n80 (s62) | 19, 11, 13 checked | ≤ 4 | 0 | 12 / 2, 11 / 0, 9 / 3 |
| L-RED's pp_K12_n161, gate_K16_n197 | 2, 3 checked | 3, 3 | 0 | 0 / 1 (17), 3 / 0 |
| L-RED's reader_L10 / L20 / L40 (n 36 / 56 / 96; l-red 1e851da4, experiments/red/ul/instances) | 2 each: the long one [0, L + 1] fails (H3) and (H4); the short one checked | 11 / 21 / 41 (unchecked) | 0 | 2 / 0 each |
- Sharp. The bound max d* is attained exactly in 26 intervals. The longest are on the gate-free family b6_xs (experiments/n5-exhaustive/instances):
  length = max d* = 21, 29, 36 at n = 24, 32, 40 (= n − 3, n − 3, n − 4; also the GCI-LEN data maximum in R91 §5). With gates, the longest
  checked interval is 26 at n = 48 (experiments/red/xing/instances/x32_waves48.pg, one gate, max d* = 37).
- No global C-interval anywhere exceeds n − 1: the largest is n − 3, on lib41, as in R91.
- GEN_W failed in 23 lib41 intervals (equal W-valuations of two different W-plays), with no settling violation there.
- Control MUT=1 (d* − 1): SETTLE_V 272 of 296 checked intervals (lib41, n ≤ 24; logs/staticdepth_MUT_lib41_n24_rs2.txt), 21 on b6_xs_n24.

## 5. What is left for GCI-LEN (OPEN, READING)
- (G1) σ̄ changes inside a global C-interval: a gate's choice moves between non-τ options while D stays constant. That is R91 §6's (i) and
  pp's leapfrog regime. It occurs in data (gci_sbchg; on pp_K12 one global C-interval of length 17 at n = 161). Splitting at those
  changes gives pieces of length ≤ n − 1 each, but the number of pieces is not bounded here.
- (G2) (H3), constant common cycles. It failed together with (H4) on R91's reader_L (honest c_s ↔ u1 against W-plays through τ). reader_L's
  global C-interval [0, L + 1] has length L + 1 ≤ n − 1, but it is outside the theorem.
- (G3) (H4), acyclic H_b, for impure ends. Impure ends with acyclic H_b are covered; cyclic ones are not.
- (G4) GEN_W (W-ties).
- READING. The theorem confirms L-RED's R91 §5 heuristic («every mechanism spends at least one fresh vertex per time step of a causal
  chain») for ρ-free intervals with constant common cycles: each step of the run is paid by one Even vertex of an H_b-path, settled for good.
  A long global C-interval therefore needs one of (G1)-(G4). reader_L uses (G2) and (G3). pp's leapfrog uses (G1).

## 6. (L1) and (L2) of N5-ABSCYC §4 (Lead 17:59Z, 18:08Z; written 18:26Z by date -u)
(L1), the identification of a pure C-interval with the abstract model, is replaced by a direct N5 argument. STATIC-DEPTH on the σ̄-constant
stretches, FREEZE-A (b) for the prefix, and a push lemma for the σ̄ changes left at direct gates. The result is polynomial. It is not the
"< 2n" of the reading, because FREEZE-A (b) freezes path weights only, and lengths still move (P-N5-ROOT (R-LEN)).
- Setting. A pure per-class C-interval [a, b] of class c (P-N5-GCX §1; every gate of U_c D-direct at every state), L := max(|A_a| − 1, 0).
  STATIC-DEPTH holds per class here. W-plays from U_c stay in U_c (prefixes off D follow τ = σ̄, then τ(u) ∈ A ⊆ U_c), so (H1)-(H4) and
  GEN_W are needed on U_c only, and d* ≤ |U_c| − 1. (H4) holds at every state by PURE-END, and every cycle is common.
- Lemma GATE-PUSH (PROVED, lane; premises FREEZE-A (b) of P-N5-ROOT, signed by REFEREE; (M2κ); BEST of N5-EXIT §2). Let a + L ≤ t < b and let
  σ̄ change at a gate u ∈ D ∩ U_c from y1 to y2 at t → t+1. Then M(y1) is unchanged and κ(y1) rises strictly in its length component, unless
  κ_{t+1}(y1) = κ_{t+1}(y2) (tie).
  Proof. u is on no honest cycle (its honest play continues in A, which holds no gate; as in FREEZE-A (c)), so BEST applies. y1, y2 ∈ A
  (direct gates), so by FREEZE-A (b) M_t(y_i) = M_{t+1}(y_i). By BEST at t and at t + 1, and (M2κ):
  κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1), and the last step is strict unless there is a tie. With M fixed, the rise is in the length. □
  By (R-LEN), each y ∈ A has ≤ |U_c| − 2 length rises after a + L. So gate σ̄ changes after a + L number N_σ̄ ≤ Σ_{u ∈ D ∩ U_c} deg(u)(|U_c| − 2)
  + TIES_c.
- Proposition PURE-LEN (PROVED, lane; GEN_W). b − a ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc. Here N_cyc is the number of transitions
  of [a + L, b] at which a cycle of class c changes; L-NEW 28's ZCH-COUNT (KPOLY §8, in-lane) bounds it by (n − 1)(|U_c| − 1) + n + TIE_c +
  ODDC_c.
  Proof. Cut [a + L, b] at every σ̄ change in U_c and every cycle change. Each stretch is σ̄-constant on U_c with constant common cycles, and
  STATIC-DEPTH bounds it by |U_c| − 1. □
  So pure C-intervals are polynomially long, ties excepted (GEN_W, Odd ties in GATE-PUSH, TIE_c / ODDC_c). The "< 2n" reading holds exactly
  when no gate σ̄ change and no cycle change occur after a + L.
- (L2), ties (OPEN). N5's S4a step breaks ties among W-equal arena options by the S1 counter-strategy procedure run on the current arena game
  (SPEC docs/new/N5-ssi-global.md l. 52-57; si.py Engine.evaluate). That is not a fixed rule on successor values: the arena changes, so the
  rule can pick a different W-equal successor at different states. GEN_W therefore has no automatic substitute, and N5-ABSCYC §3 shows
  ties really can break the per-vertex statement in the model.
  DATA: GEN_W failed in 23 lib41 intervals, and STATIC-DEPTH's conclusion held in every one of them. CONJECTURE STATIC-DEPTH-TIE: the
  length bound max d* holds without GEN_W under SPEC's tie rules.

## 7. (G1) DATA: σ̄ changes inside global C-intervals (written 18:40Z by date -u; staticdepth.py GCI=1, logs/staticdepth_gci_lib41_n48_rs2.txt)
- lib41 (n ≤ 48, S3 + 2): 444 of 1,924 global C-intervals have σ̄ changes inside, 1,095 changes in all. At most 21 in one interval: so_sorl_n32
  (experiments/red/so/instances), global C-interval [0, 21] at n = 32, where σ̄ changes at EVERY transition. so_tie15_n32 has 17 changes in
  length 18. The longest σ̄-constant piece inside such an interval is 21. pp_K12_n161: 12 changes in its length-17 interval, pieces ≤ 3.
- So on (G1) intervals STATIC-DEPTH bounds nothing (its pieces are trivial). The lengths still respect n − 1 (21 < 31). What would be
  needed (OPEN): each σ̄ change at a gate inside the interval is a value push (BEST + (M2κ): the abandoned option's κ rises strictly, ties
  aside, as in GATE-PUSH). A bound would charge those rises to fresh vertices, as in R91 §6's (O1)/(O2).
