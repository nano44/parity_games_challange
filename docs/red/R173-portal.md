# R173 Small-ODIFF windows: Lemma PORTAL (PROVED, lane): inside a TWO-FIX window, an Even vertex cannot make two consecutive W-strict moves between options that share their first branching vertex; so runquad's per-level two-faced Odd vertices cannot be replaced by shared portals. No small-ODIFF kill (L-RED successor 41)
Started 2026-11-01 06:24Z (date -u). Lead brief (R173, my choice (a)): «a SMALL-ODIFF version of the R172 TF-PH kill … ODIFF 2-3 is the
frontier; aim for a P super-linear in n at bounded ODIFF». Labels: PROVED (lane) = proved here, not refereed; DATA; READING; OPEN.
Not a TARGET.md claim. G-N5-TIME stays OPEN. Nothing here is a counterexample.

## 0. Answer
- No small-ODIFF family was found. TWO-FIX-NL (R170) and TF-PH at bounded ODIFF are not killed.
- The obstruction my predecessor stated as a READING (R170 §4: «a single portal gives both worlds a common continuation») is now a lane
  lemma with explicit premises, Lemma PORTAL (§1):
  - Setting: a TWO-FIX window (τ, σ̄ constant), a fallback-free stretch, and an Even vertex h.
  - Premises: two options i_1, i_2 of h reach the same first branching vertex X of G_F through choice-free prefixes. The Ξ-cycle node of
    X is constant between the two moves (ZC). X's plays avoid h and the two prefixes (NR).
  - Conclusion: if h moves i_0 → i_1 and then, as its next move, i_1 → i_2, the second move is an exact τ-tie: W(i_2) = W(i_1), so W
    does not rise at h. Both W-cycle nodes of X are even.
- Consequence for designs (§2): every W-strict climb step of a pivot needs a fresh branching vertex. That vertex is either
  - an ODIFF vertex (runquad: C_i, T_i, one pair per level, hence ODIFF Θ(n)), or
  - an Even vertex in the option's private prefix, or
  - a change of X's Ξ-cycle node (λ_Ξ(X)) between the two moves, or
  - a play from X that runs back through h or the prefixes (h on its own cycle).
  These four are the only routes left for a bounded-ODIFF quadratic window. §4 says why the first two do not help directly.
- DATA (§3):
  - Corpus: 1,132 runs (= 813 distinct game/start pairs on 719 games, RESULTS Erratum E-1; 319 repeats), 0 same-portal move pairs.
  - Climbs (climb173, 16 runs, n 16-36, ≤ 40,000 mutations each) find same-portal pairs in 3 runs, at most 11 per run. In every one of them ZC fails:
    X's Ξ-cycle node moves between the two moves. Most of them also fail NR.
  - VIOLATIONS 0 everywhere.
  - Hand-built instance tie_k6 (the non-vacuous branch: τ-ties with θ even and rank Z < rank θ): h never leaves its first option. The
    engine keeps σ(h) on the exact tie.

## 1. Lemma PORTAL (PROVED, lane)
- Setting: N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) under the standing premise of RESULTS R57 (S1 realises the pointwise optimum).
- Window: a TWO-FIX window [a, b] (L-NEW box 121 §4: τ_j = τ, σ̄_j = σ̄ for a ≤ j ≤ b). G_F is as in R170 §1: Odd vertices off D are
  cut to their single edge τ(v) = σ̄(v).
- Worlds: W_j := val(σ_j, τ) (Odd fixed to τ). Ξ_j := val(σ_j, σ̄) = Odd's pointwise optimum against σ_j (R57).
- Valuations: VJ00 values (cycle node w, path set P, length ℓ), ordered by key (rew(w), weight(P), ±ℓ), with + for odd w (si.Engine.key;
  Even prefers longer paths to odd cycle nodes and shorter paths to even ones). P holds the path vertices of rank > rank(w).
- Transitions and moves: transition j goes from state j−1 to state j. h moves at j if σ_j(h) ≠ σ_{j−1}(h).
- Prefix and class: for an Even h and a successor x, prefix(h, x) is the walk x, succ_F(x), … through vertices of out-degree 1 in G_F,
  up to the first vertex X of out-degree > 1 in G_F. X =: cls(h, x). Even vertices of out-degree > 1 in G and the ODIFF vertices are
  branching.
- Statement: let h move i_0 → i_1 at transition j_1 and then, as its next move, i_1 → i_2 at transition j_2, inside [a, b], with no
  S4c fallback at transitions j_1..j_2. Suppose cls(h, i_1) = cls(h, i_2) = X and:
  - (ZC) the cycle node Z of Ξ_t(X) is the same for t = j_1 − 1, …, j_2 − 1;
  - (NR) no vertex of {h} ∪ prefix(h, i_1) ∪ prefix(h, i_2) lies on the play from X under (σ_t, σ̄), t = j_1 − 1, …, j_2 − 1, or under
    (σ_t, τ), t = j_1, …, j_2.
  Then W_{j_2}(i_1) = W_{j_2}(i_2) (equal keys), and θ_1 := node(W_{j_1}(X)) and θ_2 := node(W_{j_2}(X)) are both even.
- Proof.
  - (P1) Prefix equation. Prefix vertices have one edge in G_F, so both worlds walk them, and by (NR) they are disjoint from X's plays.
    Hence for x ∈ {i_1, i_2} and each world V ∈ {W_t, Ξ_t}: V(x) = (node(V(X)), P(V(X)) ∪ K_c(x), ℓ(V(X)) + |prefix(h, x)|), where
    c = node(V(X)) and K_c(x) := {u ∈ prefix(h, x) : rank u > rank c}.
    - So V(i_1) and V(i_2) compare as follows. Let A_c := K_c(i_1) Δ K_c(i_2). If A_c ≠ ∅, the side holding the max-rank element of A_c
      wins if that element is even, and loses if it is odd. If A_c = ∅, the longer prefix wins when c is odd, the shorter when c is even.
    - We write ≻_c for this order. It depends on the world and the time only through c.
    - A_c shrinks as rank c grows: A_c ⊇ A_{c′} if rank c ≤ rank c′.
  - (P2) Choices. Transition j is not a fallback, so σ_j is the arena optimum of S4a. That is a pointwise optimal Even strategy of the
    one-player arena (Even edges {σ_{j−1}(v)} ∪ I_{j−1}(v), Odd fixed to τ), whose valuation is W_j (R57 premise; R17 (a) F1).
    Hence σ_j(h) maximises W_j over {σ_{j−1}(h)} ∪ I_{j−1}(h). I_{j−1}(h) = {y : Ξ_{j−1}(y) ≻ Ξ_{j−1}(σ_{j−1}(h))} (si.Engine.improving).
  - (P3) Ξ-order is static on [j_1 − 1, j_2 − 1]. By (ZC) and (P1), Ξ_t(i_1) vs Ξ_t(i_2) is ≻_Z for every t in the range. At j_2,
    i_2 ∈ I_{j_2−1}(h) and σ_{j_2−1}(h) = i_1, so i_2 ≻_Z i_1 (strict).
  - (P4) i_2 was available at j_1. i_1 ∈ I_{j_1−1}(h) because i_1 ≠ σ_{j_1−1}(h) = i_0. With (P3) at t = j_1 − 1:
    Ξ(i_2) ≻ Ξ(i_1) ≻ Ξ(i_0). So i_2 ∈ I_{j_1−1}(h).
  - (P2) and (P4) give i_1 ⪰_{θ_1} i_2 at j_1 (h chose i_1 while i_2 was in its arena). At j_2, i_2 ⪰_{θ_2} i_1.
  - (P5) Monotonicity.
    - W_{j+1} ⪰ W_j pointwise for j_1 ≤ j < j_2: the arena of transition j + 1 contains σ_j, and the arena optimum dominates it (F1).
      So θ_1 ⪯ θ_2 in Even's cycle-node order: odd nodes by decreasing rank, then even nodes by increasing rank.
    - Ξ_t(X) ⪯ W_t(X), since Ξ is Odd's optimum and τ is one Odd strategy. So Z = node(Ξ_{j_1−1}(X)) ⪯ node(W_{j_1−1}(X)) ⪯ θ_1.
  - Case θ_1 odd. Then Z is odd with rank Z ≥ rank θ_1 (Z ⪯ θ_1), so A_Z ⊆ A_{θ_1}.
    - (a) A_{θ_1} ≠ ∅. Its max m favours i_1. Ξ needs i_2 ≻_Z i_1, so m ∉ A_Z, i.e. rank m < rank Z. Then A_Z = ∅ (A_Z ⊆ A_{θ_1}, all of
      rank ≤ rank m < rank Z), and Z odd gives |prefix i_2| > |prefix i_1|.
      - If θ_2 is odd, A_{θ_2} ⊇ A_{θ_1} has the same max m, so i_1 ≻_{θ_2} i_2: contradiction.
      - If θ_2 is even and rank θ_2 < rank m, m is still the max of A_{θ_2}: contradiction.
      - If θ_2 is even and rank θ_2 > rank m, A_{θ_2} = ∅ and θ_2 even needs |prefix i_2| ≤ |prefix i_1|: contradiction.
      - rank θ_2 = rank m is impossible: m is a prefix vertex and θ_2 is on X's W-play (NR).
    - (b) A_{θ_1} = ∅. θ_1 odd and i_1 ⪰ i_2 give |prefix i_1| ≥ |prefix i_2|. A_Z = ∅ and Z odd make Ξ prefer the longer, so
      i_2 ≻_Z i_1 needs |prefix i_2| > |prefix i_1|: contradiction.
  - Case θ_1 even. Then θ_2 is even with rank θ_2 ≥ rank θ_1 (P5), so A_{θ_2} ⊆ A_{θ_1}.
    - (a) A_{θ_1} ≠ ∅ with max m favouring i_1.
      - If rank Z < rank θ_1, then m ∈ A_Z and m is A_Z's max, so i_1 ≻_Z i_2: contradiction.
      - Otherwise Z is odd with rank Z > rank θ_1 (Z ⪯ θ_1; Z = θ_1 would give A_Z = A_{θ_1}). Then m ∉ A_Z forces A_Z = ∅ and
        |prefix i_2| > |prefix i_1|. At θ_2: m ∈ A_{θ_2} gives i_1 ≻ i_2, a contradiction. Otherwise A_{θ_2} = ∅ (A_{θ_2} ⊆ A_{θ_1},
        whose elements all have rank ≤ rank m < rank θ_2), and θ_2 even prefers the shorter prefix: contradiction.
    - (b) A_{θ_1} = ∅. θ_1 even and i_1 ⪰ i_2 give |prefix i_1| ≤ |prefix i_2|. A_{θ_2} = ∅, and i_2 ⪰_{θ_2} i_1 gives
      |prefix i_2| ≤ |prefix i_1|. So the lengths are equal, K_{θ_2}(i_1) = K_{θ_2}(i_2), and by (P1) W_{j_2}(i_1) = W_{j_2}(i_2). ∎
- Remarks.
  - Only case θ_1 even (b) survives. There Ξ's strict preference must come from prefix vertices of rank in (rank Z, rank θ_1], which W
    does not count. So rank Z < rank θ_1, and the move at j_2 is W-flat at h.
  - The proof never uses ODIFF or the size of D. It uses only that h's two options run through a common X with fixed prefixes in BOTH
    worlds. The ODIFF vertices enter only as branching vertices: a prefix cannot pass through one.
- Corollary PORTAL-1 (PROVED, lane). Fix h, X and a fallback-free stretch of a window on which (ZC) holds and (NR) holds for all of h's
  options of class X. Call a move i → i′ with cls(i) = cls(i′) = X X-internal when h's previous move entered i inside the stretch.
  - Every X-internal move is an exact τ-tie (W-flat at h).
  - So along the stretch, W(h) rises strictly through class-X options at most once: at the first move into the class.
  - Further W-rises at h need a move into a different class.

## 2. What this means for a bounded-ODIFF quadratic window (READING)
- runquad's clock is a pivot h climbing K levels inside one window. Each climb step must be W-strict, because the τ-world gate is what
  makes h wait. By PORTAL-1, consecutive levels i, i + 1 must lie in different classes, or (ZC) / (NR) must fail between the steps.
- A class is a branching vertex of G_F. With ODIFF = k, at most k classes are ODIFF vertices, so a K-level climb needs one of:
  - (E) Even branching vertices in the private prefixes (per-level Even gates before any shared portal);
  - (Z) λ_Ξ(X) changes between levels: Ξ(X)'s cycle node changes once per level. Each W-strict level through one portal costs one
    λ_Ξ change at X;
  - (C) X's plays running back through h or a prefix, so h's options sit on different cycles.
- Why (E) does not help directly. The gate in the private prefix of option x is walked by BOTH worlds. In runquad, h's Ξ-play must avoid
  the W-sink route: if it ran into r_m it would close a cycle through the reactor chain back to h once the wave arrives. So the gate's
  Ξ-route must differ from its τ-route. That is a divergence of the worlds, i.e. an ODIFF vertex, behind the gate and before any shared
  part. A gate whose two routes are both choice-free is one more Even vertex with a static order relative to its own portal. PORTAL-1
  applies to it in turn, so it climbs at most once per (ZC) stretch.
- What PORTAL does NOT rule out:
  - (Z): pivots whose portal's Ξ-cycle node climbs once per level. The climbs' same-portal pairs are all of this kind (§3). A quadratic
    family would need the honest Ξ-sink of X to climb K times, gated by the wave.
  - (C): h on its own cycle. Its options' W-order is then decided by the cycle nodes max(prefix_x ∪ R(t)), where R(t) is the common
    return path, which can change.
  Neither was turned into a family in this box.

## 3. DATA
| set | runs | same-portal pairs | ZC | NR | premised | violations |
| --- | --- | --- | --- | --- | --- | --- |
| box 53 corpus (as red/r170/runcorp.sh) | 1,132 runs (813 distinct, E-1) | 0 | — | — | 0 | 0 |
| runquad_K3_m4_n54 (h's options are ODIFF vertices C_i: distinct classes) | 1 | 0 | — | — | 0 | 0 |
| climbs c_* (12; score K + pairs; the first 4 had a flat score) and d_* (4; + ZC / NR credit), n 16-36 | 16 | ≤ 11 per run (3 runs with pairs) | 0 | ≤ 9 | 0 | 0 |
| tie_k6 (mktie.py 6 0; 8 index permutations) | 8 | 0 (h keeps c1: exact tie) | — | — | 0 | 0 |
- Climb champions: out/cl/d_20_33 (pairs 11, NR 9, ZC 0) and out/cl/c_24_12 (pairs 5, ZC 0, NR 0 after prefix-NR). In each pair X's
  Ξ-cycle node changes between j_1 − 1 and j_2 − 1: route (Z) of §2.
- tie_k6: d is the only ODIFF vertex. Ξ-sink z (Z 41); τ-route to the even loop E (60). The stabiliser e → delay chain → Ehi (62) keeps
  I_τ(d) = ∅ for the window [0, 7]. h's options c2, c3 carry even markers 42, 44 in (Z, θ). Ξ prefers c3 ≻ c2 ≻ c1, while W ties all
  three. N5 keeps h at c1, in all 8 index permutations.

## 4. Pins and checks
- instances/tie_k6.pg / .start (mktie.py 6 0) and instances/pair_d20.pg / .start (climb champion d_20_33). pins.sha1.
- Per pin: startck OK, Oink 8fbf0a7 --zlk + verify of N5's strategies (rel2/oinkcmp.sh), xeng (seg/xeng.py). Results in
  out/pins.txt.

## 5. Tools (experiments/red/r173/)
- portalck.py G START: same-portal pairs per window, premises ZC / NR, conclusion check (exact τ-tie with θ_1, θ_2 even). VERB=1 lists
  every pair.
- runcorp.sh (out/corp.txt), genportal.py N SEED OUT.pg [OUT.start] (portal-rich random games), runrnd.sh, climb173.py N SEED ITERS
  OUT (out/cl/), mktie.py K PERM OUT.pg OUT.start.
- check.sh block «R173»: portalck on tie_k6 (0 pairs) and on pair_d20 (pairs 11, premised 0, violations 0).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r173/*; check.sh block R173; notebook. SHAs in the push / message.
- FINDINGS:
  - Lemma PORTAL PROVED (lane): in a fallback-free stretch of a TWO-FIX window, a second consecutive move of an Even vertex between two
    options with the same first branching vertex X (under ZC, NR) is an exact τ-tie. So a pivot rises in W at most once per portal per
    ZC-stretch.
  - Consequence: bounded-ODIFF quadratic windows must climb through Even gates, λ_Ξ(X) changes (Z) or self-cycles (C). Per-level ODIFF
    portals, as in runquad / mkrw, are the only route known to work.
  - DATA: corpus 0 same-portal pairs; climbs find pairs only with ZC failing; 0 violations.
  - No small-ODIFF kill. TWO-FIX-NL and TF-PH at bounded ODIFF are still open.
- NEEDS: Lead: route PORTAL to L-NEW 45 / L-NEW box 122 (it is a proof-side lemma for TWO-FIX-NL). If wanted, to a referee. Next L-RED
  target, my suggestion: route (Z), a pivot whose portal's honest Ξ-sink climbs once per wave.
