# Packet P-N5-ACCEL (box 44): inside a phase, N5's switches are paid by simple-path value levels (ACCEL), and inside each epoch of Odd's best response N5 freezes like one-player strategy improvement (EPOCH) — every game
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 03:39Z (Lead's stamp): "Packet ACCEL + EPOCH now as P-N5-ACCEL:
frozen, self-contained, small." Written 2026-10-26 03:41Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-FBF-box44.md §8.3, §9.1 (working doc; this packet governs). Labels: PROVED (L-NEW 23, unrefereed) / READING / OPEN /
DATA. Not a TARGET.md claim: neither lemma gives a polynomial bound; G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′); κ-FB-ROUND; CN-ONLY_D (restated with proofs) | PROVED |
| §2 | Lemma ACCEL (a)-(c) | PROVED |
| §3 | Lemma EPOCH (a)-(c) | PROVED |
| §4 | what the lemmas do NOT give; the σ̄|Q-repeat instance; data | READING / DATA (not to sign) |
- Premises (landed): (V1) (R17 (a)); R15 (a) (Ξ_{k+1} ⊵ Ξ_k at every transition) and R15 (d) (at most 4n(n − 1) consecutive iterations leave
  both Ω_σ and Ω_τ unchanged); R19 (d) key step (SG) ("at any N5 transition a switched Even vertex y with λ_L(y) ≠ y gains strictly", signed
  "on all games, not only 𝒞^1O"); R38 (a) KEY; R38 (f) CN-LAST (every game); SPEC S1 (valuations, order), S2 (gates), S4a, S4c (FIX 3).
  No class hypothesis, no (h_D), no hypothesis on τ.
- Overlap: §1 restates lemmas of P-N5-FBRED (in review) and P-N5-VILB (in review) with their proofs, so this packet does not rest on them.

## 0. Setting (every game)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md. Honest frame: σ̄_t := S1's optimal Odd counterstrategy to σ_t; next_t(v) := σ_t(v) (Even),
  σ̄_t(v) (Odd); Ξ_t(v) = (c, P, ℓ) := the VJ00 value of v's honest play; λ(v) := its cycle node. A PHASE: a maximal run of consecutive states
  with (λ, τ) constant (a joint λ-phase, R38 (a)). An in-phase transition (both ends in the phase) is an S4a step or an Even S4c fallback
  (an Odd fallback changes τ). f := the number of in-phase fallbacks of a phase.
- C := the cycle nodes of the phase; Q := the Odd vertices of out-degree ≥ 2; T := C ∪ Q. For c ∈ C, U_c := λ^{-1}(c) (constant on the phase).
- For c ∈ C: wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0 (sgn = +1 for even Ω); s_c := +1 if Ω(c) odd, −1 if even; κwt_c(v) :=
  (wt_c(v), s_c); for z ∈ U_c, κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)); componentwise sums, lexicographic order.
- At a fallback k → k+1: S_k := the switched Even vertices (= the gate sources, S4c), S := S_k ∖ T, x*_v := σ_{k+1}(v).
- K_c(z) := {κwt_c(p ∖ {c}) : p a simple path of G[U_c] from z to c} (all edges of G with both ends in U_c).
- An EPOCH: a maximal run E of consecutive states of a phase on which σ̄_t|Q is constant (so σ̄_t is constant on E). G_E := G with every Odd
  vertex fixed to σ̄_E; opt_E(z) := max{κwt_c(p ∖ {c}) : p a simple path of G_E[U_c] from z to c}; e_1 < e_2 < … the in-phase fallbacks
  k → k+1 with k ∈ E. N_ep := the number of epochs of the phase.

## 1. Facts, κ-FB-ROUND, CN-ONLY_D (PROVED; restated)
- (Aκ) For z ∈ U_c ∖ {c}: next_t(z) ∈ U_c and κ_t(z) = κwt_c(z) + κ_t(next_t z). Proof: λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z)
  with cycle node c; ⊕ adds z to P iff rank(z) > rank(c), and 1 to ℓ; z is not counted twice (if z ∈ P(Ξ_t next_t z), z lies on its own
  play's cycle, whose top is c, so wt_c(z) = 0). □
- (A0κ) κ_t(c) = (0, 0) (c's value is (c, ∅, 0)); and the signed weight M_t(next_t c) = 0 (next_t(c) lies on c's honest cycle, whose top is c).
- (M1κ) For values x, x′ with cycle node c: x ⊴ x′ iff κ(x) ≤ κ(x′). (M2κ) κ_t(z) ≤ κ_{t+1}(z) at every in-phase transition (R15 (a), (M1κ)).
- (INJ) The signed weight is injective on vertex sets, so M = 0 iff P = ∅.
- (SP′) For z ∈ U_c, the honest play at t from z stays in U_c and reaches c, and its prefix up to c (or up to its first vertex of any set
  containing c) is a simple path. Proof: (Aκ) at each vertex; a play is a lasso and its cycle contains c (c is its cycle node). □
- κ-FB-ROUND. At an in-phase fallback k → k+1, for every Even v ∈ U_c ∖ {c} and every successor x ∈ U_c: κ_{k+1}(v) ≥ κwt_c(v) + κ_k(x).
  Proof. If Ξ_k(x) ⊴ Ξ_k(σ_k v): κwt_c(v) + κ_k(x) ≤ κwt_c(v) + κ_k(σ_k v) = κ_k(v) ≤ κ_{k+1}(v). Otherwise (v, x) is a gate; S4c sets
  σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x); λ_{k+1}(v) = c ≠ v, so x* ∈ U_c and κ_{k+1}(v) = κwt_c(v) + κ_{k+1}(x*) ≥ κwt_c(v) + κ_k(x*) ≥
  κwt_c(v) + κ_k(x). □
- CN-ONLY_D. If an in-phase fallback k → k+1 has S = ∅, then k + 1 is the last state of its phase; so a phase has at most one such fallback.
  Proof. (1) The switched vertices are the gate sources; S = ∅ puts each in T; they are Even, so in C: each switched y is a cycle node,
  λ_k(y) = λ_{k+1}(y) = y. (2) For a switched y: P(Ξ_k σ_k y) = ∅ ((A0κ)). x*_y = next_{k+1}(y) lies on y's honest cycle at k+1, so
  λ_k(x*_y) = y. Let π be the k-play from x*_y up to its first vertex of T ∩ U_y; its vertices lie in U_y ∖ T, are not switched (S = ∅), and
  are Even (σ unchanged) or Odd with one successor; so π is also the k+1-play from x*_y.
  - If that first T-vertex is y: y's k+1 cycle is y · π, whose top is y; so P(Ξ_k x*_y) = ∅.
  - If it is q ∈ Q, q ≠ y: the k+1-play from y is y · π · q · (q's k+1-play) and returns to y, so π and q lie on y's k+1 cycle, below y:
    wt_y = 0 on π and P(Ξ_{k+1} q) = ∅. By (Aκ) along π at k and (M2κ): M_k(x*_y) = M_k(q) ≤ M_{k+1}(q) = 0. The gate Ξ_k(x*_y) ▷
    Ξ_k(σ_k y) with M_k(σ_k y) = 0 and (M1κ) give M_k(x*_y) ≥ 0. So P(Ξ_k x*_y) = ∅ (INJ).
  (3) For every gate (y, z): Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ Ξ_k(x*_y) (x*_y has the best key among y's gate targets). Both ends are (y, ∅, ·); the
  reward is injective, so Ξ_k(z) has cycle node y; its signed weight lies between 0 and 0, so P(Ξ_k z) = ∅. So every gate has λ_k(y) = y and
  lev = −1 (same cycle node and P, different length), and CN-LAST (R38 (f)) gives that k + 1 is the last state of the phase. □

## 2. Lemma ACCEL (PROVED, every game)
In every phase:
- (a) κ_t(z) ∈ K_c(z) for every state t and every z ∈ U_c;
- (b) the in-phase transitions at which some Even vertex z with λ(z) ≠ z switches number at most N_K := Σ_{c ∈ C} Σ_{Even z ∈ U_c ∖ {c}}
  (|K_c(z)| − 1);
- (c) f ≤ 1 + N_K.
Proof. (a) (SP′) and (Aκ) along the honest prefix to c. (b) At an in-phase transition L → L+1 a switched Even y with λ_L(y) ≠ y gains strictly:
Ξ_{L+1}(y) ▷ Ξ_L(y) ((SG), R19 (d); S4a and S4c switch along gates). With (M1κ), κ_{L+1}(y) > κ_L(y); κ(y) never decreases in the phase
((M2κ)) and moves in the finite set K_c(y) ((a)); so y switches at ≤ |K_c(y)| − 1 transitions; charge each transition to one such y.
(c) At most one fallback has S = ∅ (CN-ONLY_D); a fallback with S ≠ ∅ switches some Even y ∉ T, so y ∉ C, λ(y) ≠ y, and it is counted in
(b). ∎

## 3. Lemma EPOCH (PROVED, every game)
For every phase and every epoch E of it:
- (a) (freeze) for t ∈ E with t > e_j and z ∈ U_c: κ_t(z) ≥ max{κwt_c(p ∖ {c}) : p a simple path of G_E[U_c] from z to c with ≤ j edges};
  and κ_t(z) ≤ opt_E(z) for every t ∈ E. Hence for t ∈ E with t > e_{n−1}: κ_t = opt_E on every class, i.e. Ξ is constant on that part of E.
- (b) no transition t → t+1 with t, t+1 ∈ E and t > e_{n−1} switches an Even z with λ(z) ≠ z; and the part of E after e_{n−1} has at most
  4n(n − 1) + 1 transitions.
- (c) f ≤ 1 + n·N_ep.
Proof.
- (a) Lower bound, by induction on j: j = 0, p = (c), κ_t(c) = (0, 0). Step: p = z·p′ with p′ from x, ≤ j − 1 edges. Odd z: on E,
  next_t(z) = σ̄_E(z) = x (the path is in G_E), so (Aκ) and the hypothesis at t give the bound. Even z: k := e_j < t, k ∈ E, k > e_{j−1}, and
  k + 1 ≤ t lies in E (E is a run); κ-FB-ROUND at k, the hypothesis at k, and (M2κ) from k+1 to t. Upper bound: z's honest play at t ∈ E is
  a simple path of G_E[U_c] to c ((SP′); Even edges σ_t, Odd edges σ̄_E). Simple paths in U_c have ≤ n − 1 edges.
- (b) If such a z switched, (SG) would give κ_{t+1}(z) > κ_t(z) = opt_E(z) ≥ κ_{t+1}(z) ((a) at t and t + 1, both in E after e_{n−1}).
  After e_{n−1}, every transition with both ends in E leaves Ξ = Ω_σ unchanged ((a)), and Ω_τ is constant (τ is constant on a phase); by
  R15 (d) there are at most 4n(n − 1) of them in a row; add the transition that leaves E.
- (c) Per epoch: at most n − 1 fallbacks e_1, …, e_{n−1}; a later fallback with both ends in E switches only cycle nodes ((b)), so S = ∅,
  and there is at most one such in the whole phase (CN-ONLY_D); at most one fallback is E's last transition. So f ≤ Σ_E n + 1. ∎

## 4. Not to sign: limits, the repeat instance, data
- What ACCEL does NOT give: a polynomial bound. |K_c(z)| can be exponential (distinct sets of high-rank vertices on simple paths). ACCEL is
  the honest-frame form of "strategy improvement stops after at most #valuations steps"; transitions that switch only cycle nodes are not
  counted by (b). Its use (READING, docs/new/N5-FBF-box44.md §8.3): the value-iteration lower bound of P-N5-VILB climbs by repeating a cycle,
  N5's values never do (a repeated cycle without c would change λ), so value-iteration gadgets (arXiv:1407.5030 Figure 2(a)) do not force
  many N5 switches; a counter must climb through many simple-path levels inside one phase.
- What EPOCH does NOT give: no bound on N_ep, and no bound on the S4a steps of an epoch BEFORE its freeze (between e_j and e_{j+1}). Every
  super-polynomial count of fallbacks in a phase needs super-polynomially many epochs.
- N_ep is not bounded by the number of σ̄|Q configurations: σ̄|Q REPEATS inside a phase (DATA). Instance
  experiments/new/box25/laps/lap_n6_s1_110421.pg (n 6, Q = {2}, sha1 4f4fe69c51e1c6f170c9c732feca025da70e7edb): one phase (λ ≡ 5,
  τ(2) = 0), σ̄_t(2) = 0, 4, 0 at states 0, 1, 2. lib41: 91 phases with a repeat (87 on 𝒞^1O), up to 36 repeats and 50 epochs in one phase
  (experiments/si/orlens/instances/lev_l_x.pg, n 32).
- DATA (experiments/new/box44/sgcheck.py, epoch.py; canonical S3 start; lib41 412 runs, the box-43/44 instances, random 𝒞^kO games):
  (SG) 13,346 checks, 0 violations; max switching transitions in one phase 112, max distinct κ-levels of one vertex in one phase 52;
  EPOCH (c) 0 violations; EPOCH (a)/(b) are VACUOUS in the data: no epoch in any sample reaches n − 1 fallbacks (they rest on their proofs).
