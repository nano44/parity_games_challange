# N5: the two counts G_c and X_u per fallback-free run (box 21)
L-SI successor 17 (Opus 5.5; D18, Lead reading L40). Lead's GO 15:38Z (Lead's stamp): "You own the BOUND side of G_c and X_u ... Write your
definitions of G_c and X_u (with note §10.2) into one short section of a docs/si/ file".
Written 2026-10-26T15:40Z onward (date -u). Working note, unrefereed. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING.
Predecessor note: docs/si/N5-ROOT-box20.md (§3 FREEZE-A, §4 ROOT-PIECE, §8.1 DD, §9 FREEZE-G, §10.2 RESET-PIECE).

## 1. Definitions (for L-COMP 5 box 14 and for this lane; DEFINITIONS, no claim)
All objects are those of note N5-ROOT-box20 §0, §8.1, §9.1; nothing new is assumed. Code: experiments/si/root/common.py (rows, phases, Dset,
avoid, first_D); the counter is experiments/si/root/gcx.py.
- Run. A PHASE is a maximal run of states with λ_Ξ and τ constant (RESULTS R38 (a) KEY). A FALLBACK-FREE RUN S = [s, e] is a maximal interval of
  states of one phase such that no transition t → t+1 with s ≤ t < e is an Even S4c fallback; every transition of S is an in-phase S4a step.
  (A phase with f in-phase fallbacks has ≤ f + 1 fallback-free runs.)
- Class. For a cycle node c of the phase: U := U_c := λ^{-1}(c) (constant on the phase); Q_c := the Odd vertices of U ∖ {c} with ≥ 2 distinct
  successors.
- At a state t: D_t := {Odd u : σ̄_t(u) ≠ τ(u)}; the PLAY of z is its (σ_t, τ)-play (Even follows σ_t, Odd follows τ);
  A_t := {z ∈ U : z's play meets no vertex of D_t} (= F_D(t) ∩ U); for u ∈ D_t ∩ U, R_u(t) := {z ∈ U : the first D_t-vertex on z's play is u}
  (the GATE REGION of u; u ∈ R_u(t)). U is the disjoint union of A_t and the R_u(t), u ∈ D_t ∩ U.
  DD_t := {u ∈ D_t ∩ U : σ̄_t(u) ∈ A_t and τ(u) ∈ A_t} (D-DIRECT GATES).
- G_c(S) (A-GAINS). The number of transitions t → t+1 of S with A_{t+1} ⊄ A_t. At such a transition each entering vertex z ∈ A_{t+1} ∖ A_t has a
  first D_t-vertex u(z) (z ∉ A_t); its CAUSE is DLEAVE if u(z) ∉ D_{t+1} (Odd's best reply at u(z) has moved back to τ), SWITCH otherwise (an
  Even vertex on z's route to u(z) switched off it). Reported: G_c(S) (transitions; the quantity in ROOT-PIECE), G_c^v(S) (entering vertices),
  and the split DLEAVE / SWITCH by vertices.
- X_u(S) (CROSS-GATE MIGRATIONS into u's region). For u ∈ Q_c: the number of transitions t → t+1 of S with u ∈ DD_t ∩ DD_{t+1} and some
  z ∈ R_u(t+1) ∖ R_u(t) with z ∉ A_t (so z ∈ R_{u′}(t) for a gate u′ ∈ D_t ∩ U, u′ ≠ u). Reported: X_u(S) (transitions; the quantity in
  RESET-PIECE (iii)), X_u^v(S) (migrating vertices), and the source gate u′ of each migrating vertex (D-direct at t or not; u′ ∈ D_{t+1} or not).
  Gains of R_u from A_t (RESET-PIECE (ii)) are NOT part of X_u.
- Where they enter (note §10.2, PROVED lane, unrefereed): ROOT-PIECE gives, per phase, the root's path-weight changes while D-direct
  ≤ (f + G_c + 1)(|U| + deg(r) − 2) + f + G_c, with G_c := Σ_S G_c(S); RESET-PIECE gives, inside a FREEZE-A piece on which u stays D-direct,
  ≤ |A_s| − 1 + deg(u) − 1 changes of Δ(u) and ≤ |A_s| gains of R_u from A, with X_u the remaining (unbounded) gains. So the per-gate resets per
  phase are ≤ (f + G_c + 1)·(2|U| + deg(u) + X_u) with X_u the per-piece maximum.
- Counting conventions. Per (game, start, phase, class, run): G_c(S) for each class c with |U_c| ≥ 3 and Q_c ≠ ∅; X_u(S) for each u ∈ Q_c.
  "Per fallback-free run" maxima are maxima of these per-run numbers; sums are over the runs of a phase.

## 2. DATA (experiments/si/root/gcx.py; logs root/logs/gcx_*.txt; DATA, not proof)
Written 2026-10-26T15:45Z (date -u). Libraries with KMIN 2 and S3 + 4 random starts, as in note N5-ROOT-box20 §10.
| set | runs | G_c(S) max / sum | entering vertices (DLEAVE / SWITCH) | X_u(S) max / sum | migrating vertices (source gate D-direct / not; stays in D / leaves) | root ρ per run, max |
| --- | --- | --- | --- | --- | --- | --- |
| pp_K12_n161 / pp_K48_n449 (mkpp) | 1 / 1 | 2 / 2, 2 / 2 | 74 / 218, all DLEAVE | 13 / 26, 49 / 98 | 52 / 196: all from a D-direct gate that stays in D | 14 / 50 |
| gate_K16_n197 / gate_K64_n581 (mkgate) | 1 / 1 | 2 / 2, 2 / 2 | 94 / 286, all DLEAVE | 18 / 35, 66 / 131 | 105 / 417: 73 / 265 from a staying D-direct gate, 32 / 152 from a gate that leaves D | 15 / 63 |
| nep90 phase@4 / nep76 phase@9 | 8 / 7 | 4 / 15, 2 / 9 | 53 / 45, all DLEAVE | 2 / 5, 3 / 8 | 14 / 12: all from a non-direct gate that leaves D | 12 / 12 |
| lib2o (KMIN 2), S3 + 4 | 117 | 3 / 39 | 331 (323 / 8) | 1 / 1 | 1 (leaves D) | 5 |
| lib41 (KMIN 2), S3 + 4 | 309 | 6 / 104 | 541 (487 / 54) | 8 / 20 | 29, all from non-direct gates: 22 stay in D, 7 leave | 6 |
- On R90's families G_c(S) is CONSTANT (2) while X_u(S) grows like K (13 → 49 on mkpp, 18 → 66 on mkgate): the linear R⁰_{≥2} of R90 sits in
  X_u, not in G_c. On nep90 / nep76 the opposite: G_c(S) ≤ 4 per run, X_u(S) ≤ 3, and every migration is a D-leave of the source gate.
- mkpp, where the migrations are (scratch probe with mkpp's vertex names, pp_K12): the four D-direct gates uA, uB, uH, uz keep their offsets
  CONSTANT on the whole run (bit lengths 138, 137, 157, 0), D ∩ U is constant, A does not grow until t = 18. The migrations are a Bellman-Ford
  wave: at t = 0, 1, …, 12 one more line vertex lA_q, lB_q (q = 13, 12, …, 1) and the route vertices w_j, x_j switch from uz's / uH's region
  into uA's / uB's region; nothing migrates after t = 12. Each vertex migrates once.
- C-INTERVALS (maximal sub-intervals of a run with A non-increasing, D ∩ U constant and every D-direct offset constant; FREEZE-G's setting with
  several gates): on all sets above, no vertex migrates twice inside a C-interval (mig_per_vertex_max = 1; MIG2_cint = 0) and no migration
  happens at index ≥ |U| − 1 of its interval (MIG_LATE = 0; VACUOUS on these sets except 17 lib41 intervals: C-intervals are shorter than
  |U| − 1). The broad "once" form dies on climbed instances (§4). C-interval counts: 3 / 3 (mkpp), 17 / 65 (mkgate), 82 / 70 (nep90 / nep76; length
  ≤ 1 there: the root's offset moves at almost every step), 219 (lib2o), 540 (lib41). Control MUT=1 (the whole run as one interval) finds
  double migrations: nep90 (vertex 1 five times in run [0, 14]), nep76, gate_K16 (reader vertices 14 times: they alternate between gates as
  mkgate's gate enters and leaves D).
- Pins: experiments/si/check.sh "box 21" block (nep90 and pp_K12 counts, C-ONCE, the MUT=1 control).
- U events by C-interval (gcx.py UEV=1; U event = CHARGE-U's unforbid-switch (N5-RUND §16): an S4a switch k′ → k′+1 of Even y into z
  with (y, z) forbidden at some state of [k′ − n + 1, k′ − 1] in the run). Inside a C-interval / at a C-cut transition:
  mkpp K12 / K48: 12 / 48 inside, 2 / 2 at cuts; mkgate K16 / K64: 1 / 1 inside, 17 / 65 at cuts (the gate enters or leaves D at every
  leapfrog); nep90 / nep76: 2 / 0 inside, 18 / 19 at cuts. See §4 for the killers of UF-ONCE and the libraries.

## 3. Lemma MIG-SPLIT (PROVED, elementary, every game)
Statement. Let t → t+1 be an in-phase S4a transition, c a class, u ∈ DD_t ∩ DD_{t+1}, and z ∈ R_u(t+1) ∖ (R_u(t) ∪ A_t) with first
D_t-vertex u′ ≠ u. Then (L) u′ ∉ D_{t+1}, or (S) some Even vertex w on the part π of z's (σ_t, τ)-play before u′ (z included) has
σ_{t+1}(w) ≠ σ_t(w); in case (S) z's (σ, τ)-play (its W-play) changes at t → t+1.
Proof. Suppose u′ ∈ D_{t+1} and no Even vertex of π switches. Odd vertices of π are not in D_t, so they follow τ, which is constant in the
phase; so z's (σ_{t+1}, τ)-play starts with π and reaches u′. Its first D_{t+1}-vertex is then u′, unless some vertex of π lies in
D_{t+1} ∖ D_t; then it is the first such vertex, an Odd vertex of π. It equals u (z ∈ R_u(t+1)), but u ∈ DD_t ⊆ D_t and π has no D_t-vertex.
So it is u′ ≠ u, against z ∈ R_u(t+1). In case (S), w lies on z's play at t and its successor changes, so the play changes. □
- Consequence (PROVED): X_u(S) ≤ #{transitions of S at which a gate of U_c leaves D} + #{transitions of S at which some z ∈ U_c changes its
  W-play}. A W-play change is a W-value change or a W-tie (same value, other play). With CHARGE-U (N5-RUND §16; λ_W-constant run) the
  coarse-level −1 value changes (path sets) are ≤ (n − 1)·(1 + |U(S)|) per vertex; length-only changes and ties are not covered (as in
  R83 §2).
- DATA (§2): mkpp's migrations are all (S) with a staying D-direct source (the Bellman-Ford wave), nep90 / nep76's all (L).

## 4. C-intervals: two of my own candidate statements DEAD, one survives (DATA, DEAD, CONJECTURE)
A C-INTERVAL of class c in a fallback-free run: a maximal sub-interval [a, b] on which A_c is non-increasing, D ∩ U_c is constant and every
D-direct gate offset Δ(u) is constant (so DD_c is constant too). A C-CUT is a transition of the run that lies in no C-interval. The intent:
FREEZE-G (N5-ROOT §9) with several gates, and "no re-arming while the gate structure is constant".
- DEAD (own candidate, never claimed) C-ONCE: "no vertex migrates between gate regions twice inside a C-interval". Instance
  experiments/si/root/instances/cone_n65.pg (sha1 3e95fca9088f6a52cdf16325fe06933296ed357e; climbed from mkpp.py 3 3; SPEC S3 start):
  phase@1, class 8, C-interval [0, 4], 8 vertices migrate twice between the regions of the NON-direct gates 12 and 64 (DD empty, A empty);
  cone_n69.pg (sha1 dd03ba782ca821491ad5c54303ab61def7c7aff1): one C-interval of 19 transitions, vertices migrate up to 3 times between the
  non-direct gates 20, 29, 35. Obstruction: Bellman-Ford staggering inside the window: a vertex first takes a short route through one gate,
  then a longer better route through another gate arrives, and so on.
- Survives (DATA only, thin): the X_u form C-ONCE_X (migrations INTO a D-direct gate): migx_per_vertex_max = 1 on every set of §2 and on the
  climbs (6 climbs × 4,000-5,000 mutations from mkpp K3 (2), mkgate K3 (2), cone_n65, nep90; climbmig.py OBJ=mig); the whole-run control
  (MUT=1) finds double X-type migrations on nep90 (vertices 1, 26, 28 twice in run [0, 14]). The staggering of cone_n65 should transfer to
  D-direct gates; I expect C-ONCE_X to die to a better climb. Not proposed for proof.
- DEAD (own candidate) UE-ONCE_C: "inside a C-interval every Even edge is unforbid-switched at most once" (the C-interval form of UF-ONCE).
  Instance experiments/si/root/instances/ueonce_n27.pg (sha1 c90d5ab8569a93bba3389002e0c85bb64bb0c214; climbed from L-RED's usplit_rd_s3_n27,
  OBJ=ue; SPEC S3 start): phase@1, C-interval [1, 10], edge (10, 23) has U events at k = 1 and k = 5. Also lib41
  experiments/si/xing/instances/zcl_cu_n48.pg with a random start (edge (16, 20) twice in C-interval [7, 23]). Obstruction: the same
  staggering, inside the window.
- What the UF-ONCE killers do (DATA; this is the finding): their repeated U events on ONE edge all sit at C-CUTS. so_th_n32 (DEAD 18a: (24, 21)
  three times) has 8 U events inside C-intervals (none repeated) and 6 at cuts, the three (24, 21) events among them; phase2_pk48: 9 inside, 1 at
  a cut; usplit_rd_s3_n27 (DEAD 18b): 1 inside. mkgate: 1 inside, 65 at cuts.
- CONJECTURE UL_C (late freeze). No U event at index ≥ |U_c| − 1 of its C-interval: for every C-interval [a, b] of class c and every U event
  (k′, (y, z)) with y ∈ U_c and a ≤ k′ < b: k′ − a < |U_c| − 1.
  - DATA: 0 violations on lib41 (KMIN 1, 𝒞^1O included, S3 + 4 random starts: 2,087 runs, 5,847 C-intervals, 17 of them of length ≥ |U| − 1,
    1,504 U events inside, 1,228 at cuts), lib2o (KMIN 1, S3 + 4: 17 inside, 14 at cuts), mkpp, mkgate, nep90, nep76, the three UF-ONCE /
    U-SPLIT killers, ueonce_n27, 6,000 random 𝒞^kO games (n 10-30), and 3 climbs (OBJ=ul, 3,000 mutations each, from so_th_n32 ×2 and
    phase2_pk48; the climbs did not move off their start scores). The data runs are fallback-free runs, not split at λ_W changes. Largest index of an inside U event: |U| − 1 − 7 on lib41. Control ULMUT=1
    (threshold 0) fires (so_th_n32: 8). Support is THIN where it matters: only 17 C-intervals reach length |U| − 1.
  - mkpp shows the scale: 48 U events inside ONE C-interval at K48, each on fresh content (a new line vertex), at indices < K + 2 < |U| / 8.
    UL_C is the formal version of L-RED's "returns without fresh content inside one fallback-free run" (R90 §2) with the gate structure
    held fixed: a content-free re-arm must cross a C-cut.

## 5. Corollary UL-RED (PROVED, conditional on UL_C in its global form; every game)
Global form UL_G: call a GLOBAL C-interval a maximal sub-interval of a λ_W-constant fallback-free run S on which, for EVERY class c, A_c is
non-increasing, D is constant and every D-direct gate offset is constant; K(S) := the number of global C-cuts of S. UL_G: no U event at index
≥ n − 1 of its global C-interval. (UL_C for every class implies UL_G for U events whose switching vertex lies in a class with |U_c| ≥ 3 and
Q_c ≠ ∅: a global C-interval lies inside one C-interval of each class and |U_c| ≤ n. Other classes are not in the data: OPEN.)
Statement. Under UL_G, for every λ_W-constant fallback-free in-phase run S:
- (a) |U(S)| ≤ n_E·((n − 1)(K(S) + 1) + K(S)), n_E := the number of Even vertices;
- (b) for every vertex x, COARSE_{−1}(W(x)) changes ≤ (n − 1)·(1 + n_E·((n − 1)(K(S) + 1) + K(S))) times on S.
Proof. (a) A transition carries at most n_E switches, hence at most n_E U events. Inside a global C-interval, UL_G leaves at most n − 1
transitions that can carry U events; there are ≤ K(S) + 1 intervals and K(S) cut transitions. (b) CHARGE-U (N5-RUND §16, PROVED, every game)
on S with (a). □
- So, under UL_G, the coarse W-dynamics of a fallback-free run is polynomial in n and in K(S): the number of transitions at which some class's
  A grows, D changes, or a D-direct offset changes. K(S) counts exactly the "gate events": A-gains (G_c), D-enters and D-leaves (σ̄ changes at
  gates), and offset changes (Δ(u) = M(τ u) − M(σ̄ u), bounded per FREEZE-A piece by RESET-PIECE (i)).
- Not covered (as in R83 §2): length-only W changes and W-tie switches.

## 6. Status, labels, what is open
- PROVED (lane, unrefereed): MIG-SPLIT (§3); UL-RED (§5) CONDITIONAL on UL_G.
- DATA: §2 (G_c constant, X_u linear on R90's families; mechanisms), §4.
- DEAD (own candidates, recorded in docs/si/DEAD.md "DEAD box 21"): C-ONCE (cone_n65, cone_n69), UE-ONCE_C (ueonce_n27).
- CONJECTURE: UL_C / UL_G (§4, §5); C-ONCE_X (weak, §4).
- READING. G_c and X_u do not close by themselves: on R90's families G_c(S) = 2 and X_u(S) = Θ(K) is a Bellman-Ford wave launched by
  unforbid-switches on fresh content (12 / 48 inside one C-interval), and on nep90 / nep76 every migration is a D-leave. Under UL_G the
  whole run reduces to its gate events K(S). The open count is then K(S) per fallback-free run (equivalently: ρ events at gates, A-gains, and
  D-direct offset moves), which is where the root's ρ was at the start of box 20: on nep90 the C-intervals have length ≤ 1 (the root's offset
  moves at almost every step), so UL-RED gives nothing new there, and ROOT-PIECE with f + G_c remains the bound for the root.
- OPEN: a proof of UL_C (FREEZE-G with several gates of constant offset; the step that fails is Fact B across gates, N5-ROOT §1 / §8.4);
  G_c per fallback-free run; K(S).
