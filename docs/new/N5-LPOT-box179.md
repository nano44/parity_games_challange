# Box 179 N5-LPOT: ranking-function synthesis (LP potentials) on 𝓛^R_d — the key potential Φ_K descends at every step (T ≤ Φ_K(s_0) ≤ 2^(d+2) − 2d − 4), it is optimal among potentials linear in the key bits (OPT-K), and LP lower bounds show that richer level-local features do no better at d ≤ 3: the obstruction is free Ξ-renewal in feature space
L-NEW successor 56, 2026-11-06 (from 08:44Z by date -u; see the commits). Lead brief BOX 179 (D14: a method the fleet has not used on the
step count). Method chosen: (1) of the three sent to the Lead at 08:44Z, i.e. LP synthesis of a ranking function (potential), as in
termination analysis of programs. The source is inspiration only, not a premise: Podelski-Rybalchenko-style linear ranking functions; no
paper opened, nothing cited as a premise. Model: RESULTS R104's definition of the IDEAL model; 𝓛^R_d is RESULTS R110's definition.
Lemmas used: P-IDEAL-ALIGN ALIGN (a)-(c) (signed, landing as R113) and R111 PAIR-KF / CASCADE (landed). Labels: PROVED (lane,
unrefereed) / DATA / CONJECTURE / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- Translation (§1). A potential is a function Φ(G, s) with Φ(G, s) − Φ(G, step(s)) ≥ 1 on every transition s → step(s) ≠ s, for every
  genome G in 𝓛^R_d and EVERY state s (every state is a start), and with Φ ≥ 0. Then T ≤ Φ(s_0) ≤ max Φ. «T^R(d) polynomial» is
  equivalent to the existence of a polynomially bounded potential: R(s) := the remaining run length is one. So the method only has
  content for RESTRICTED classes: Φ = Σ_f w_f f(G, s), with features f that are local in the levels and weights w that are universal
  (independent of G). The LP over all sampled transitions computes the least range max Φ in the class. Restricting the LP to a subset
  of the transitions only lowers the optimum, so a sampled optimum is a LOWER bound for the class.
- PROVED (lane) Theorem PHIK-DESCENT (§2). Put w_l := 2^(d−l) − 1 and k_s(x) := [s(x) ≠ KP_s(x)] (x is key-misaligned). Then
  Φ_K(s) := Σ_x w_lev(x) k_s(x) falls by at least 1 at every step of every run on 𝓛^R_d. Hence T ≤ Φ_K(s_0) ≤ 2 Σ_l w_l =
  2^(d+2) − 2d − 4. This is P-IDEAL-ALIGN's T-BOUND, now as a single potential, and it adds the start-dependent form T ≤ Φ_K(s_0): a start
  at which every mover is key-aligned has T = 0. DATA: 0 violations on 38,902 transitions (log/phik.txt), never tight on the champions
  (log/phik_start.txt: e.g. TR_d7_T20 T 20 against Φ_K(s_0) 354).
- PROVED (lane) Theorem OPT-K (§3). Every potential of the form a + Σ_x w_x k_s(x), with weights depending on the mover index only, has
  range ≥ 2^(d+2) − 2d − 4 on 𝓛^R_d. So Φ_K is optimal in its class. The forcing transitions live on Ξ-trivial genomes (every Ξ-target
  the exit), where every mover moves at most once and T ≤ 2d. The exponential is therefore a blindness of the class (a misaligned mover is
  charged whether or not it will ever be Ξ-renewed), not a property of the dynamics. Machine check: out/force_d1..8.json.
- DATA (machine; HiGHS LP in floating point, not exact) (§4). Least range of the class, from LP lower bounds:

  | class | features per state | d 2 | d 3 | d 4 | d 5 |
  | --- | --- | --- | --- | --- | --- |
  | C0 | z, k, u = z∧k per mover | 8 | 22 | 52 | 114 |
  | P | C0 + pair-automaton one-hot (k_p, k_q, z_p, z_q) + ord bit per level | — | 22 | 52 | — |
  | PHX | P + Ξ-height-indexed z / u counts + cross-level k·z products | 8 | 22 | ≥ 49.1 | ≥ 61.2 |
  | PHXV | PHX + value rank of cv(x) among x's path values (raw and normalised) | 8 | ≥ 17.9 | — | — |
  | (T^R(d), exact) | | 4 | 8 | 13 (lane) | ≥ 17 |

  C0 and P are EXACT at the shown d: the LP lower bound equals Φ_K's range 2^(d+2) − 2d − 4, and Φ_K is in the class. PHX at d 2, 3 is
  exact for the same reason. At d 3, PHX reaches 22 only with enough genomes: 18.7 with 162 (62 corpus + 100 random), 22 with 1,562. So the d 4 and d 5
  PHX entries are sampling-limited lower bounds (40.8 with 164 genomes, 49.1 with 764; 45.4 with 53, 61.2 with 133).
- DEAD (method, for level-local linear potentials): at d ≤ 3 no potential in PHX proves anything better than PAIR-DOUBLE; at d 4 none
  proves T ≤ 49. The LP dual certificate is an explicit multiset of transitions (out/dual_PHX_d3_s1793.json, 61 rows, 1,500 random genomes
  + corpus). Obstruction (READING, from the dual's support, §5): two movers of one level renew each other's Ξ-unhappiness (z 0 → 1) by
  their own moves, a top-level ping-pong. In bit features this costs nothing. Its real brake is MONO (Ξ-values only rise, PATH-RISE
  capacity), a global integer that level-local bits cannot measure. Adding the value rank (PHXV) helps only a little (22 → 17.9 at d 3, against
  T^R(3) = 8).
- Per-genome contrast (DATA, §4.3): with genome-specific weights, PHX gets close to the true maximum over all starts (max_d5_L15 15 = 15;
  dd_d5_F14 15 against 14; TR_d6_T18 20 against 18; TR_d7_T20 21.3 against 20). So the obstruction is universality (one weight vector
  for all genomes), not locality.
- Verdict: the method gives a clean potential proof of the known base-2 bound, and a proof that local key accounting cannot beat it.
  It does not bound T^R(d) polynomially. A polynomial potential must contain a non-local Ξ-quantity (a value budget) with weights that
  stay polynomial. No such quantity is known: PATH-RISE capacity is exponential. G-N5-TIME stays OPEN.

## 1. Translation (method → T^R)
- Termination analysis proves that a loop terminates by exhibiting a ranking function, a map into a well-founded set that falls at every
  iteration; a polynomial-range ranking function bounds the number of iterations. Linear ranking functions over chosen features are found
  by linear programming (Farkas duality). Here the «loop» is the IDEAL step on a genome of 𝓛^R_d, and its «variables» are the 2d option
  bits plus derived bits.
- Features (box179/lpot.py, `feats`). For a mover x and a state s: z_s(x) = [the other option is strictly Ξ-better] (Ξ-unhappy); k_s(x) =
  [s(x) ≠ KP_s(x)] (key-misaligned); u = z ∧ k. At degree 2, x moves at step s → s′ iff z_s(x) = 1 and KP_(s′)(x) ≠ s(x) (R104 step
  rule). Per level l: the one-hot of (k_p, k_q, z_p, z_q) and ord_l = [key(2l) < key(2l + 1)] (the pair automaton of P-IDEAL-ALIGN). H:
  the Ξ-height of x (longest Ξ-path to X), a genome-dependent role index. X: the products z(a)k(b), k(a)z(b) for a at level l and b at
  level l + 1. V: the index i of cv_s(x) in the sorted list of the integer values (R105 ENC) of all maximal Ξ-paths from x, and
  i/(#paths − 1).
- LP: variables w (one per feature name, plus a constant) and Mx; minimise Mx subject to w·(f(s) − f(s′)) ≥ 1 on every distinct
  transition row, and 0 ≤ w·f(s) ≤ Mx on every distinct state row. Transitions: every state of every sampled genome (random 𝓛^R_d
  genomes from box162 rand_lr, iso and non-iso, and every 𝓛^R corpus file of boxes 150-177 and L-RED r207 / r208 keep at that d).
  The dual multipliers of the decrease rows sum to the optimum (the certificate).

## 2. Theorem PHIK-DESCENT (PROVED, lane)
- Statement. On 𝓛^R_d, with w_l := 2^(d−l) − 1 (so w_(d−1) = 1 and w_l = 2w_(l+1) + 1), Φ_K(s) := Σ_x w_lev(x) [s(x) ≠ KP_s(x)]
  satisfies Φ_K(s) − Φ_K(s′) ≥ 1 for every step s → s′ ≠ s. Hence every run from s_0 has T ≤ Φ_K(s_0) ≤ 2 Σ_(l<d) w_l = 2^(d+2) − 2d − 4.
- Facts used. (F1) A mover x moves at s → s′ only if its other option is strictly Ξ-better at s. It then moves to KP_(s′)(x), the
  key-least option under the new state (R104 step rule; at degree 2 its A-set is both options). So k_(s′)(x) = 0 for every mover. (F2) KP
  at level 0 is constant (keys are the gates alone). For l ≥ 1, KP_s(p) = KP_s(q) = c_s(l), the option pointing to the lower mover with
  the smaller key (ALIGN (a)). So KP at level l changes between s and s′ iff ord_(l−1) flips; write f_(l−1) := [ord_(l−1)(s) ≠
  ord_(l−1)(s′)], f_(−1) := 0. (F3) CASCADE (R111): if the pair of level l flips, one of its movers moves, or l ≥ 1 and f_(l−1) = 1.
  (F4) ALIGN (c): if s(p) = s(q) = j then ord_l = γ_l(j), a gate constant.
- Per-level change Δ_l := w_l Σ_(x at level l) (k_(s′)(x) − k_s(x)); m_l := the number of movers of level l that move.
  - If f_(l−1) = 0: KP is unchanged at level l. A moving x had k_s(x) = 1 (it leaves s(x) ≠ KP for KP) and has k_(s′)(x) = 0; a
    non-moving x keeps its k. So Δ_l = −m_l w_l. If m_l = 0, then also f_l = 0 (F3).
  - If f_(l−1) = 1: KP flips at level l. A moving x had s(x) ≠ KP_(s′)(x), i.e. s(x) = KP_s(x), so k goes 0 → 0. A non-moving x toggles
    k. Cases: no mover, state «both aligned» (11) → both misaligned, Δ_l = +2w_l, and ord_l is unchanged (F4: s(p) = s(q) = c before
    and after), so f_l = 0. No mover, «both misaligned» (00): Δ_l = −2w_l, f_l = 0 (F4). No mover, one aligned (D-state): Δ_l = 0, f_l
    may be 1. One mover: Δ_l = ±w_l. Two movers: Δ_l = 0.
- Recursion. Let E(l, f) be the largest possible Σ_(j ≥ l) Δ_j given f_(l−1) = f, with E(d, ·) = 0. Claim: E(l, 0) ≤ 0 and E(l, 1) ≤
  2w_l. Induction on l downwards. E(l, 0) ≤ max(E(l + 1, 0), −w_l + E(l + 1, 1)) ≤ max(0, −w_l + 2w_(l+1)) = max(0, −1) = 0. E(l, 1) ≤
  max(2w_l + E(l + 1, 0), w_l + E(l + 1, 1), 0 + E(l + 1, 1), −2w_l + E(l + 1, 0)) ≤ max(2w_l, w_l + 2w_(l+1)) = max(2w_l, 2w_l − 1) =
  2w_l.
- Step. Let l_0 be the least level with a mover (it exists since s′ ≠ s). Below l_0 nothing moves, so f_(l_0−1) = 0 and Δ_(l_0) =
  −m_(l_0) w_(l_0) ≤ −w_(l_0). Then Φ_K(s′) − Φ_K(s) ≤ −w_(l_0) + E(l_0 + 1, f_(l_0)) ≤ −w_(l_0) + 2w_(l_0+1) = −1. ∎
- Remarks. (i) It is the potential form of P-IDEAL-ALIGN's Φ-accounting (same bound). (ii) T ≤ Φ_K(s_0) is new as stated (start-
  dependent). (iii) DATA: box179/phik.py, 400 random genomes (every state for d ≤ 4, 201 states for d = 5) plus the runs of 183 corpus
  files: 38,902 transitions, 0 violations, least drop 1, drop exactly 1 on 3,320.

## 3. Theorem OPT-K (PROVED, lane): no potential linear in the key bits beats Φ_K
- Statement. Let Φ(G, s) = a + Σ_x w_x k_s(x) (real a, w_x depending on the mover index only). If Φ falls by ≥ 1 at every step of every
  G ∈ 𝓛^R_d from every state, then w_x ≥ 2^(d−lev(x)) − 1 for every x, and max_s Φ − min_s Φ ≥ Σ_x w_x ≥ 2^(d+2) − 2d − 4 on every G.
- Forcing transition τ(l, p), for 0 ≤ l ≤ d − 2 and p ∈ {2l, 2l + 1} with partner q. Genome: every Ξ-target is the exit X, all parities
  even, and at every mover the option s(x) has the larger rank, except at p, where 1 − s(p) has it. So z(x) = 0 for x ≠ p and z(p) = 1.
  State s: p is key-misaligned (s(p) ≠ c_l), q is aligned (s(q) = c_l), both level-(l + 1) movers are aligned (s = c_(l+1) at both), and
  the gates of the level-l pair make ord_l(s) ≠ γ_l(c_l). Levels other than l and l + 1 are arbitrary. Then: below l nothing moves (z = 0),
  so c_l is unchanged. p is the only mover with z = 1 and is misaligned, so it moves to c_l (F1). Now s′(p) = s′(q) = c_l, so ord_l =
  γ_l(c_l) ≠ ord_l(s) (F4): f_l = 1. Both level-(l + 1) movers go k 0 → 1 without moving (z = 0); their state goes 11 → 00, so ord_(l+1) is
  unchanged (F4), and nothing above changes. For l = d − 1 the same genome and state, minus the level-(l + 1) part, give the move of p
  alone, with k(p) 1 → 0.
- Proof. τ(l, p) gives w_p − w_(2l+2) − w_(2l+3) ≥ 1, and τ(d − 1, p) gives w_p ≥ 1. With W_l := min over level l, W_(d−1) ≥ 1 and W_l ≥
  2W_(l+1) + 1, so W_l ≥ 2^(d−l) − 1. Every G has the state with all k = 1 (choose s(x) ≠ KP_s(x) level by level, lowest first) and the
  state with all k = 0, so the range is ≥ Σ_x w_x ≥ 2 Σ_l (2^(d−l) − 1). ∎
- Machine check: box179/forcing.py finds and checks τ(l, p) for every l and p at d = 1..8 with the box150 simulator (out/force_d<d>.json;
  only p moves, and the k bits change exactly as stated).
- Reading: on these Ξ-trivial genomes every mover moves at most once (z is static; after its move a mover is Ξ-best), so T ≤ 2d. The
  2^d is forced by states the class cannot tell apart: a misaligned level-(l + 1) mover that will be Ξ-renewed later in some other genome.

## 4. LP kill test (DATA, machine; floating-point LP, not exact)
### 4.1 Commands and logs (box179/log/)
- lp_*: random genomes only. lpc_*: corpus files at that d + random genomes. lpc_C0_d3 / d4 (62 / 64 corpus + 100 random): 22 / 52.
  lpc_P_d3 / d4: 22 / 52. lpc_C0_d5 (33 + 20): 114. lpc_PHX_d3 (62 + 100): 18.73; lpc_PHX_d3_r1500 (62 + 1,500): 22.00. lpc_PHX_d4
  (64 + 100): 40.80; lpc_PHX_d4_corpusonly: 36.97; lpc_PHX_d4_r700: 49.11. lpc_PHX_d5 (33 + 20): 45.40; lpc_PHX_d5_r100: 61.24.
  lpc_PHXV_d3_r1500: 17.93. Earlier random-only runs (lp_*, 300 genomes at d 3) gave P 21.38, H 21.50, X 22.00, PHX 13.70. Those are lower
  bounds only and are superseded.
### 4.2 Certificates
- The dual multipliers of the decrease rows sum to the optimum. For C0 at d 3 (corpus only) the support is 16 rows from 12 different
  genomes. For PHX at d 3 (out/dual_PHX_d3_s1793.json) it is 61 rows: 13.6 of the mass on random genomes, the rest on 11 corpus files
  (now1_d3_5 3.12, kf2_d3_6 1.49, …).
### 4.3 Per-genome LPs (genome-specific weights; log/one_*)
- C0: dd_d5_F14 19.0, max_d5_L15 23.5, TR_d6_T18 28.8, TR_d7_T20 41.3. PHX: dd_d5_F14 15.0, max_d5_L15 15.0, TR_d6_T18 20.0,
  TR_d7_T20 21.3. Max T over all starts (log/maxT.txt): dd_d5_F14 14, max_d5_L15 15, TR_d6_T18 18, TR_d7_T20 20. With genome-specific
  weights, local features nearly reach the true run length.

## 5. Obstruction (READING from the PHX d 3 certificate)
- The heaviest certificate rows (by multiplier) are moves of a top-level mover that turn its partner Ξ-unhappy: f(s) − f(s′) has z_x,
  u_x −1 at the partner and z, k, u +1 at the mover (now1_d3_5: 100000 → 100001, multiplier 1.77; random genomes: 000111 → 000110,
  010100 → 010101, …). The partner's move then renews the first mover. The other rows are lower-level moves that misalign both movers of
  the level above (the OPT-K pattern). The LP must charge each misaligned mover as if it will move, because a renewal costs the renewing
  mover only its own drop. A potential that charges the renewal would need the remaining Ξ-capacity (MONO: cv only rises), an integer
  whose level-local bit shadows (z, H) carry no budget. The value rank (V) is a budget, but it ranges over P(x) paths (PATH-RISE), and
  with universal weights it buys only 22 → 17.9 at d 3.
- What a polynomial potential would need (CONJECTURE-shaped, not claimed): a Ξ-budget B(s), polynomial in d, that falls by ≥ 1 at every
  renewal of a key-misaligned mover. That is DBL-O(1) / RENEW-COUNT_2 in potential form.

## 6. Files (experiments/new/box179/)
- lpot.py (LP synthesis; classes C0, P, H, X, V, and their combinations, by letters; Farkas certificate when infeasible; dual dump);
  phik.py (exact Φ_K descent check); phik_start.py (T against Φ_K(s_0)); forcing.py (OPT-K forcing transitions, d ≤ 8); maxT.py.
- out/force_d1..8.json (OPT-K instances), out/dual_PHX_d3_s1793.json (certificate), out/dual_PHXV_*.json; lpot.py also writes
  out/w_<class>_d<d>.json (optimal weights; scratch, not committed). log/ as listed in §4.1.
- lpot.py needs scipy (HiGHS); phik.py, forcing.py, maxT.py need only the box150 simulator.

## 7. Next (Lead decides)
- Exact LP (rational) for PHX at d 3, to turn «22» into a machine certificate in exact arithmetic.
- A potential with a non-local Ξ-budget: charge a key-misaligned, Ξ-happy mover only through the movers whose moves can renew it (its
  Ξ-descendants on the non-current option's chain). Test it by LP with the feature «number of Ξ-descendants of x on its other chain that
  are unstable». Kill: the same ping-pong at depth 2.
- For L-RED: none new. OPT-K's forcing genomes are Ξ-trivial (T ≤ 2d); they are not dynamics instances.
