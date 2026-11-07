# Packet P-IDEAL-CUBE (box 154): the improvement cube of a degree-2 IDEAL-ACYC genome is a decomposable acyclic USO (DECOMP); every IDEAL run follows a directed path of it (MULTI→SINGLE, T ≤ LP); and directed paths can be exponential: an explicit Ξ-ladder family with LP ≥ 2^(K+1) − 2 = 2^(N/2+1) − 2 (Theorem LADDER-LP)
L-NEW successor 50 (Opus 5.5), D14 / D18. Lead brief BOX 154, 2026-11-04 01:56Z: «make it landable. Freeze packet P-IDEAL-CUBE for both
referees». Written 2026-11-04 (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-CUBE-fixes.md
(append-only). Source: docs/new/N5-CUBE-box153.md (box 153, 43125a61); this packet governs. Labels: PROVED (L-NEW 50, unrefereed) /
DATA / READING. Not a TARGET.md claim. No polynomial bound. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §1 | Definitions D-ORI, D-USO, D-COMB, D-DEC; quoted source text | (definitions) | |
| §2 | Lemma DECOMP (degree ≤ 2, IDEAL-ACYC): the improvement orientation is a decomposable acyclic USO | PROVED | structure |
| §3 | Lemma MULTI→SINGLE, Corollary T ≤ LP | PROVED | REDUCTION (T to LP) |
| §4 | Theorem LADDER-LP: an explicit genome family with LP ≥ 2^(K+1) − 2 | PROVED | lower bound for LP (not for T) |
| §5 | machine check, «does NOT claim» list, TARGET diff | DATA / READING (not to sign) | |

- Premises.
  - LANDED: RESULTS R104 (P-N5-REALIZE), ONLY its definition of the IDEAL model, as restated in P-IDEAL-RED §0.
  - SIGNED, not yet landed: P-IDEAL-RED (docs/new/P-IDEAL-RED.md at 0ebddcf5, sha1 06f2c186…, with fixes entries 1-2; both
    referees signed; RESULTS R105 when landed). Used: §0 (notation and model restatement), Lemma ENC (§1), Lemma LOCAL (b) and
    (c) (§1). Cited as «P-IDEAL-RED (signed; RESULTS R105 when landed)». No other statement of it is used. Each use is marked.
  - External definitions: [WW22] Def. 4 and §2.2, quoted verbatim in §1. Only the definitions are used; no theorem of [WW22] is a
    premise.
  - Nothing from docs/lit or docs/sources.

## 0. Setting
- Model: the IDEAL model of RESULTS R104, notation of P-IDEAL-RED §0 (movers x, options (x, k), Ξ-targets xt(x, k), β-ranks and
  parities, states s, chains, Ξ-values Ξ_s(x, k) and their order ▷, A_s(x), steps, runs, T, Mv_t). IDEAL-ACYC: the Ξ-graph is
  acyclic; π is a topological order (positions, Ξ-edges go to larger π).
- Degree ≤ 2 throughout. D2 := the movers with two options; the others have one option and never move.
- C_s(x) (x ∈ D2): the option of x whose Ξ-value is strictly better at s. Two faces never tie (P-IDEAL-RED ENC, signed; R105 when
  landed: distinct options carry distinct β's, so their β-sets differ).
- x is improving at s iff s(x) ≠ C_s(x).
- The cube Q_G := {0, 1}^D2. A vertex b ∈ Q_G is the state s_b with s_b(x) = b(x) for x ∈ D2 (and the only option elsewhere). We
  write C_b, Ξ_b for C_(s_b), Ξ_(s_b).

## 1. Definitions (and the source text they follow)
- [WW22]: S. Weber, J. Widmer, «Realizability Makes a Difference: A Complexity Gap for Sink-Finding in USOs», arXiv:2207.05985.
  Opened (ar5iv HTML, 2026-11-04). Verbatim:
  - Def. 3: «An orientation o of the n-dimensional hypercube is described by a function o:{0,1}^n→{0,1}^n assigning each vertex
    its outmap. An edge (v,v⊕e_i) is directed away from v if o(v)_i=1. To ensure consistent orientation of all edges, o has to
    fulfill o(v)_i≠o(v⊕e_i)_i for all v∈V and i∈[n].»
  - Def. 4: «A Unique Sink Orientation (USO) is an orientation of the hypercube, such that for each non-empty face F of the
    hypercube, the subgraph induced by F has a unique sink, i.e., a unique vertex which has no outgoing edges.»
  - §2.2 (Matoušek-type USOs): «Thus, in each face there is a dimension which is not influenced by any other dimension, and all
    edges of that dimension point in the same direction. We therefore say that each face is combed, and that the whole
    Matoušek-type USO is decomposable.»
  - After the proof of Thm 18 (the term is used for general USOs): «JumpAntipodal requires only n vertex evaluations on all
    decomposable USOs, not only on the Matoušek-type USOs.»
- D-ORI (improvement orientation). For x ∈ D2 and b ∈ Q_G, the outmap is o_G(b)_x := 1 if b(x) ≠ C_b(x), else 0. The edge
  {b, b ⊕ e_x} is directed away from b iff o_G(b)_x = 1, i.e. from the improving endpoint to the endpoint on C(x).
- D-USO = [WW22] Def. 4.
- D-COMB. A dimension x is combed in a face F (free coordinates X_F ∋ x) iff all edges of F in dimension x point in the same
  direction.
- D-DEC (decomposable). An orientation is decomposable iff every face of dimension ≥ 1 has a combed dimension. This is the §2.2
  sentence with «not influenced by any other dimension» dropped; it is the property the Thm 18 remark uses for «all decomposable
  USOs».
- LP_G(b) := the largest number of edges of a directed path in the orientation starting at b (finite by DECOMP (b)).

## 2. Lemma DECOMP (PROVED)
- Statement (degree ≤ 2, any IDEAL-ACYC genome G, any width, any levels).
  - (o) o_G is an orientation in the sense of [WW22] Def. 3.
  - (a) It is a USO (D-USO).
  - (b) It is acyclic.
  - (c) In every face F of dimension ≥ 1, the free coordinate y of largest π is combed. Hence o_G is decomposable (D-DEC).
- Proof.
  - (o) By P-IDEAL-RED LOCAL (b) (signed; R105 when landed), C_b(x) depends only on b at strict Ξ-descendants of x, and x is not one
    of them. So C_b(x) = C_(b⊕e_x)(x) =: c. Exactly one of the two endpoints has x-coordinate ≠ c, so o(b)_x ≠ o(b ⊕ e_x)_x.
  - (c) The strict Ξ-descendants of y have larger π. So every one of them that lies in D2 is a fixed coordinate of F, and LOCAL (b)
    gives C_b(y) constant for b ∈ F. Then every y-edge of F is directed toward the facet {b(y) = C(y)} of F.
  - (a) Induction on dim F. Dimension 0: the single vertex is the sink. dim F ≥ 1: take y as in (c), with constant value c = C(y)
    on F. A vertex with b(y) ≠ c has its y-edge outgoing, so it is not a sink of F. So every sink of F lies in the facet
    F′ := F ∩ {b(y) = c}. A vertex of F′ is a sink of F iff it is a sink of F′, since its y-edge is incoming. F′ has exactly one sink
    by induction.
  - (b) Define E(b) := Σ_(x ∈ D2) o_G(b)_x · 2^π(x). Along an edge from b to b′ = b ⊕ e_x with o(b)_x = 1:
    - o(b′)_x = 0;
    - for z with π(z) > π(x), x is not a strict Ξ-descendant of z, so C(z) and b(z) are unchanged (LOCAL (b)) and o(b′)_z = o(b)_z;
    - the terms with π(z) < π(x) change by at most Σ_(p < π(x)) 2^p = 2^π(x) − 1.
    - So E(b′) ≤ E(b) − 2^π(x) + 2^π(x) − 1 < E(b). A directed cycle would return to the same E. ∎
- Does NOT claim: anything for degree ≥ 3 (the cube is not binary), or for Ξ-cyclic genomes; that o_G is of Matoušek type
  (realizable by a matrix); any bound on LP.

## 3. Lemma MULTI→SINGLE and Corollary T ≤ LP (PROVED)
- Lemma MULTI→SINGLE (degree ≤ 2, IDEAL-ACYC). Let a step t of an IDEAL run move the set Mv_t from s_(t−1) to s_t. List Mv_t as
  x_1, …, x_m in increasing π. Let b^0 := s_(t−1) and b^j := b^(j−1) ⊕ e_(x_j). Then every edge b^(j−1) → b^j is a directed edge of
  o_G, and b^m = s_t.
  - Proof. Every x ∈ Mv_t moves to an option strictly better at s_(t−1) (P-IDEAL-RED §0, the step rule), so o(s_(t−1))_x = 1 and
    s_t(x) = C_(s_(t−1))(x).
  - When x_j is switched, the coordinates changed so far are x_1, …, x_(j−1), all with smaller π. So none is a strict Ξ-descendant of
    x_j, and LOCAL (b) gives C_(b^(j−1))(x_j) = C_(s_(t−1))(x_j) ≠ b^(j−1)(x_j). The edge is directed from b^(j−1) to b^j. ∎
- Corollary T ≤ LP. For every IDEAL run of a degree-≤-2 IDEAL-ACYC genome from s_0: T ≤ Σ_t |Mv_t| ≤ LP_G(s_0).
  - Proof. Concatenating the paths of MULTI→SINGLE gives a directed path of length Σ_t |Mv_t| from s_0. Every step has
    Mv_t ≠ ∅. ∎
- Does NOT claim: the converse (most directed paths are not IDEAL runs: an IDEAL step also needs the W-key rule); any bound on LP.

## 4. Theorem LADDER-LP (PROVED)
- The genome L_K (K ≥ 1). N = 2K movers, all of level 0 (no W-targets), all of degree 2.
  - Pairs i = 0, …, K − 1: u_i, v_i. Pair 0 is the deepest.
  - Ξ-targets: both options of u_0 and of v_0 go to the exit X. For i ≥ 1, option 0 of u_i and of v_i goes to u_(i−1), option 1 to
    v_(i−1).
  - All parities even, so for distinct β-sets P, Q: P ▷ Q iff the β of largest rank in P △ Q lies in P (R104's comparison).
  - Ranks: 4K distinct ranks 0, …, 4K − 1. Pair 0 gets the top four, pair 1 the next four, and so on; so every rank of pair i − 1 is
    above every rank of pair i.
    - Pair 0, increasing: β(u_0, 0) < β(v_0, 0) < β(u_0, 1) < β(v_0, 1).
    - Pair i ≥ 1, increasing: β(u_i, 0) < β(u_i, 1) < β(v_i, 0) < β(v_i, 1).
  - Gate indices: any distinct values (W plays no role in this theorem).
  - Start b_0: u_0, v_0 on option 0; every u_i, v_i with i ≥ 1 on option 1.
  - L_K is an IDEAL-ACYC genome: every Ξ-edge goes from pair i to pair i − 1.
- Theorem LADDER-LP. For every K ≥ 1, o_(L_K) has a directed path of length 2^(K+1) − 2 starting at b_0. So
  LP_(L_K)(b_0) ≥ 2^(K+1) − 2 = 2^(N/2+1) − 2.
- Notation. For a state s and a mover x, Cur_s(x) := Ξ_s(x, s(x)), the β-set of its current chain. For pair j,
  B_j(s) := 0 if Cur_s(u_j) ▷ Cur_s(v_j), else 1 (the option index that points to the better mover of pair j). The chain of any
  option of a pair-i mover meets pairs i, i − 1, …, 0 once each, so it carries exactly one β of each of these pairs.
- Facts (each for every state s).
  - (F0) Pair 0: C(u_0) = C(v_0) = 1 (single-element faces; option 1 has the higher rank). B_0 = 1 at (u_0, v_0) on (0, 0) and on
    (1, 1); B_0 = 0 on (1, 0). (Rank order w_u < w_v < b_u < b_v.)
  - (F1) For i ≥ 1 and x ∈ {u_i, v_i}: C_s(x) = B_(i−1)(s).
    - The two faces of x are {β(x, 0)} ∪ Cur(u_(i−1)) and {β(x, 1)} ∪ Cur(v_(i−1)).
    - Cur(u_(i−1)) ≠ Cur(v_(i−1)): they contain different pair-(i−1) β's.
    - All their elements have ranks above pair i's. So the largest element of the symmetric difference of the two faces lies in
      Cur(u_(i−1)) △ Cur(v_(i−1)).
    - So face 0 ▷ face 1 iff Cur(u_(i−1)) ▷ Cur(v_(i−1)), i.e. C(x) = B_(i−1).
  - (F2) For i ≥ 1: if u_i and v_i sit on the same option k, then B_i = 1. Cur(u_i) and Cur(v_i) share the chain from their common
    target on, so they differ exactly in β(u_i, k) and β(v_i, k), and β(v_i, k) has the higher rank.
  - (F3) For i ≥ 1: if u_i sits on option k and v_i on 1 − k, then B_i = 0 iff k = B_(i−1). The largest element of the symmetric
    difference lies in Cur(u_(i−1)) △ Cur(v_(i−1)) (higher ranks than pair i), so the mover whose target is the better one wins.
  - (F4) Switching movers of pairs ≥ i changes no C(x) and no B_j for x, j in pairs < i. Those depend only on pairs < i: chains go
    downward (LOCAL (b) for C; for B_j directly, Cur of pair j reads pairs ≤ j).
- Definition. Pair j ≥ 1 is SETTLED at s iff u_j and v_j both sit on option B_(j−1)(s), i.e. neither is improving (F1).
- Claim UP(i) (1 ≤ i ≤ K − 1).
  - Hypotheses: at a state s, B_(i−1) has just changed (from b to 1 − b) by a switch at pair i − 1, and every pair j ≥ i is settled
    with respect to the old value (so u_i, v_i sit on option b, and for j > i on option B_(j−1)(s), unchanged).
  - Then the procedure UP(i), run at s, makes exactly 2^(K−i+1) − 2 switches, each along a directed edge of o_(L_K), and ends with
    every pair j ≥ i settled. UP(i) is: switch u_i to 1 − b; if i + 1 ≤ K − 1, run UP(i + 1); switch v_i to 1 − b; if i + 1 ≤ K − 1,
    run UP(i + 1).
- Proof of UP(i), by induction on K − 1 − i.
  - Before: u_i, v_i on option b, so B_i = 1 (F2). By F1, C(u_i) = C(v_i) = B_(i−1) = 1 − b ≠ b: both are improving. So the switch
    of u_i is a directed edge.
  - After it: u_i on 1 − b, v_i on b; by F3, B_i = 0 (k = 1 − b = B_(i−1)). So B_i changed from 1 to 0, by a switch at pair i, and
    every pair j ≥ i + 1 is settled with respect to the old B_i = 1 (unchanged so far).
    - If i + 1 ≤ K − 1, the induction hypothesis applies: UP(i + 1) makes 2^(K−i) − 2 directed switches and ends with every pair
      j ≥ i + 1 settled.
    - By F4 it changes neither B_(i−1) nor C(v_i).
  - So v_i is still improving (C(v_i) = 1 − b ≠ b), and its switch is a directed edge.
  - After it: both on 1 − b, so B_i = 1 (F2). B_i changed from 0 to 1 by a switch at pair i, and pairs j ≥ i + 1 are settled for
    the old B_i = 0. So (if i + 1 ≤ K − 1) UP(i + 1) runs again: 2^(K−i) − 2 directed switches, ending settled.
  - At the end, pair i has both movers on 1 − b = B_(i−1): settled. Pairs > i are settled.
  - Count: 2 + 2 (2^(K−i) − 2) = 2^(K−i+1) − 2 when i + 1 ≤ K − 1. For i = K − 1 (no UP(i + 1)): 2 = 2^2 − 2. ∎
- Proof of Theorem LADDER-LP.
  - At b_0: B_0 = 1 (F0). Every pair i ≥ 1 sits on option 1 with both movers, so B_i = 1 (F2), and pair i + 1 sits on 1 = B_i: every
    pair j ≥ 1 is settled.
  - u_0 is improving (C(u_0) = 1 ≠ 0, F0). Switch it: B_0 becomes 0 (F0), with every pair ≥ 1 settled for the old value. If K ≥ 2,
    run UP(1): 2^K − 2 directed switches, ending settled.
  - v_0 is still improving (F0, F4). Switch it: B_0 becomes 1. If K ≥ 2, run UP(1) again: 2^K − 2 directed switches.
  - Total 2 + 2 (2^K − 2) = 2^(K+1) − 2 directed edges, consecutive (each starts where the previous ended). For K = 1: 2 = 2^2 − 2. ∎
- Does NOT claim:
  - that LP_(L_K)(b_0) equals 2^(K+1) − 2 (DATA: it does for K ≤ 7, §5);
  - anything about the IDEAL run of L_K. With all movers at level 0, the W-key rule picks the gate-least option, and with gates
    increasing in k that run has T = 0 from b_0 (DATA, §5). The theorem is about directed paths, not runs.

## 5. Machine check, «does NOT claim», TARGET diff (not to sign)
- Machine check (experiments/new/check.sh blocks w102, w103).
  - box153/decomp.py checks (o)-(c) and switch-all ≤ |D2| by brute force over every face: 0 violations on 25 corpus genomes with
    ≤ 10 degree-2 movers (478,953 faces). The box 153 run also covered 119 genomes including random ones (603,741 faces), 0
    violations.
  - box154/ladder.py builds L_K, follows the path of §4 with the box 150 simulator's values, and checks:
    - every switch is to the strictly better face;
    - the length is 2^(K+1) − 2;
    - B_i flips 2^(i+1) times;
    - the DP longest path from b_0 (K ≤ 7).
    DATA: OK for K = 1..10 (path lengths 2, 6, …, 2046); DP longest = 2^(K+1) − 2 exactly for K ≤ 7; IDEAL T = 0.
  - box153/longpath.py: the DP longest path on corpus genomes, against T (x3_L8: LP 16 vs T 8; dc_d8: 64 vs 23), and the climbed
    2-wide Ξ-ladder champion ladlp_5.json (LP 114 at N = 10).
- «does NOT claim»:
  - no statement about real IDEAL runs beyond T ≤ LP (they are W-gated; on L_K the run is empty);
  - no polynomial bound on T, U, KF or LP;
  - no lower bound on IDEAL run lengths, and no super-polynomial IDEAL family;
  - nothing about N5 beyond what R104 already says;
  - G-N5-TIME stays OPEN.
- READING (value):
  - T ≤ LP together with LADDER-LP shows that the Ξ side alone (the decomposable cube) admits exponential directed paths.
  - So any proof of IDEAL-ACYC-POLY must use the W-key gate. The route «bound LP» is DEAD by Theorem LADDER-LP.
  - Whether the gate can follow such a path is the open question (L-RED R201).
- Diff against TARGET.md:
  - TARGET.md's objects are parity games, winning regions, and algorithms with their running time (§1-§3; M4 §2, M3 §4 / §7e).
  - No statement here mentions a game, a region or an algorithm's running time. Each is about the improvement cube of the IDEAL
    model of R104. Not M4, not M3, not a gauntlet step.
