# R2-P-N5-LEVEL: REFEREE-2 second review of packet P-N5-LEVEL (L-NEW successors 72-73, box 208 + Addenda A, B)
REFEREE-2 successor 39 (Opus 5.5, D1 «Never downgrade the referee to save money»; Lead reading L53). Written 2026-11-12 by date -u
(times in the commits). Independent: I did NOT open docs/referee/ (REFEREE 34's review of this packet, REFEREE 32's
R-box208-preread.md) or notes/REFEREE.md before this report's verdict is on origin. I did not read L-RED 66's R235, L-RED-B's B1 or
L-COMP 19's box 43 either; where the packet quotes them, I used only the packet's words. I read the lane's tools only to learn the
format of their outputs (level208.py / plat208.py / rv208.py headers and the frozen out/ files) and ran only mkl1_211.py (in an
isolated copy, to rebuild L-1). No lane code is imported by my replay.
Committed in boxes: box 1 = object, premises, §3; box 2 = §4-§6; box 3 = §7-§8; box 4 = DATA and own replay; box 5 = scope, genome-only
steps, TARGET.md diff, line L-1, verdicts.

## Box 1: object, premises, §3

### 1.0 Object (hashes re-computed from `git show`)
- claude/l-new 1e6df4990efeb31dd3800a543b61f721b209f80a: docs/new/P-N5-LEVEL.md sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec,
  65,874 B, 575 lines; docs/new/P-N5-LEVEL-line-L1.txt sha1 28565b3c60fe8167f4b660c83fa27c00cd7b4fe9, 7,239 B, one line (= the brief).
- experiments/new/box211/level.pins: 106 rows; every row's sha1 equals the file at 1e6df499 (my loop over `git show`, 106 ok, 0 bad):
  the packet, its source note, L-1, P-N5-XICYC.md (149e2414…), P-N5-QN.md (97254bd2…), every tool, engine module and frozen output of §11.
- L-1 rebuilt: mkl1_211.py, run on a copy of the packet and quotes211.out in an empty scratch tree with trunk 68c8d293's RESULTS, writes
  a file byte-equal to the frozen L-1 (cmp: equal; sha1 28565b3c…, 7,239 B). Its asserts (statements verbatim in the packet, DATA
  counts against §11's tables, quotes211.out «missing 0») all pass.
- Trunk: the quotes are pinned at 68c8d29339d5945efe6878a7e4cfc9d6a1611d48. Trunk now is 7fa6aff4 (fetched 19:57Z); docs/RESULTS.md has
  the same sha1 4117c8a7… at both commits, TARGET.md the same sha1 a41d5e1a… at both.

### 1.1 Premises, checked by script (R2-P-N5-LEVEL/r2lvq.py, own code; output r2lvq.out)
- r2lvq.py takes every bullet «- [Q X]» of the packet (25 bullets, §1 and §13) and looks for every «…» on it, whitespace-normalised,
  INSIDE the named source only: the RESULTS entry «### X » … next «### » for X = R<id> (trunk 68c8d293), the landed packet file for
  X = P-N5-QN / P-N5-XICYC (at their pinned sha1s, = trunk's), TARGET.md for X = TARGET. A quote with « … » is tested piece by piece in
  order. Result: 44 quotes, 44 found, 0 missing (= the lane's quotes211.out «quotes 44 missing 0»; I did not read quotes211.py).
- Being present is not enough: I read each landed item in RESULTS for its SCOPE (my predecessor's render, r2q_render_68c8d293.out, and
  the entries themselves). Every premise is stated for the object the packet uses:
  - R118 (a) definitions [every genome]; (b) F1 «for every step t» (from R15 (a), any non-empty unambiguous improving set); (c) DOM
    [IDEAL-CYC, every genome], for every successor y of x; (e) CYC-COUNT with its parenthetical reason; (i) BR-SEG-G [any parity game,
    Howard from any σ_0, under H0], with the labels C / R / p of (a).
  - R121 (b) E-MON [IDEAL-CYC, every genome], its proof's E-DOM sentence «by [DEF]»; the lex order on e-sets (R121 (a)).
  - R123 (a) CN2 [every genome, every positional pair]; (b) B-ONLY [every genome, every state]; (c) NO-TIE; (d) LOC-GATE [every genome,
    every state]; (e) LOC-K2 [every state]; [OPT] in R123's title, spelled out in R122's premise clause (R57 (b), 1E-N3).
  - R126 (d) QUIET-N [every genome] «every maximal window of quiet steps has at most N steps», with class and loud / quiet as in R123
    (R126's title); R126's Ξ-feedback number (title, Lemma (k+1)-Λ). R126's own premise list cites «(e) with its stated reason», as
    this packet does.
  - (D1), (D3), (D4): in P-N5-QN §1 (landed R126's packet), quoted.
- N-1 (no change required). (K1) cites «R118 (e), its reason», a parenthetical inside the signed item (e), not an item of its own. The
  same fact also follows from listed premises: by F1, Ω_t(v) ⊴ Ω_(t+1)(v); if Λ_t(v) ≠ Λ_(t+1)(v) the values differ, so Ω_t(v) ◁
  Ω_(t+1)(v) and (VJ-1) gives reward(Λ_t(v)) < reward(Λ_(t+1)(v)). Landed R126 already used the reason as a premise in the same words.
  I sign (K1) on either route. (If the lane switched to F1, L-1's sentence «the class facts … use neither PLATEAU nor F1» would change; I
  do not ask for it.)
- [VJ] «as used» is not script-checked (the packet says so). I checked it by hand against the order my own engine implements
  (R2-P-ACYC/r2acyc.py VJ.values / VJ.cmp, written by my predecessor from VJ00 §4.2 / Friedmann §3 as R118 cites them): Π(v) = the
  vertices before Λ(v) on v's path that are more relevant than Λ(v); (VJ-1), (VJ-2) as stated; k decides only on equal (Λ, Π). Equal.
- Not used, confirmed by reading every proof below: F2-F6, R118 (d) BR-SEG, (f) T-CYC, R126 GATE-CLASS, any bound on k(v), any lane lemma
  (PAID, R-LOCAL, LOUD-SPLIT, LAM-GAP / SHARP), any Γ3 fact, [E-LEV], any Lean theorem.

### 1.2 §2 Setting: checked
- The Even vertices: N movers, 2M faces, c_X, c_W, K0, K1, K3: N + 2M + 5 (my builder asserts n = N + 3M + 6; Odd = M gates + K2).
- Class order: distinct vertices already have distinct rewards (rank, negated when odd), so «reward(Λ) < reward(Λ′)» is a strict order on
  cycle nodes without the packet's priority argument; the packet's argument is also correct. The lex order on finite sets of e-vertices
  is total. My engine encodes class_t(v) as (reward(Λ), Σ_{e∈E} 2^rel(e)): integer order on the second part is exactly «the most relevant
  element of E Δ E′ lies in E′».

### 1.3 §3 (K1)-(K5): SIGN (re-derived step by step)
- (K1). Λ changes only upward in reward (N-1); if Λ is unchanged, E does not fall (E-MON, scope IDEAL-CYC every genome). With the class
  order, class_t(v) ≤ class_(t+1)(v). Correct.
- (K2), for triples. Λ ≠ Λ′: Θ ⊴ Θ′ and Θ ≠ Θ′ give Θ ◁ Θ′, (VJ-1). Λ = Λ′, E ≠ E′: E Δ E′ ⊆ Π Δ Π′ (E = Π ∩ e-vertices), so z (the
  most relevant vertex of Π Δ Π′) is at least as relevant as z_E. If z ≠ z_E, z is more relevant than an e-vertex: E-DOM leaves e-vertex,
  c_W, K0, K3. Not an e-vertex (it would be in E Δ E′ above z_E). Not c_W: c_W's only edge is its loop, so on any play c_W is the cycle
  node, never in Π. Not K0, K3: I re-checked the core's in-edges in R104's [DEF] (K0 → {K1, K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 →
  {K1, K2}); the only edge into the core from outside is β → u = K0 ((D3)). So a play from outside the core has cycle node K1 iff it
  enters the core, and then runs K0 → K3 (frozen) → K2 → K1 (LOC-K2: σ̄(K2) = K1 at every state) → K1 (frozen loop); K0 (top + 2) and
  K3 (top + 3) are more relevant than K1 (5), K2 (3) is not. As Λ = Λ′, K0, K3 lie in both Π-sets or in neither. So z = z_E, even;
  Θ ◁ Θ′ with (VJ-2) puts z in Π′: E <lex E′. Correct. The hypothesis «(Λ, Π) is the cycle node and Π-set of a play of a vertex outside
  the core» is used exactly in the K0 / K3 step, and K5's triple ext(x, Ω_t(y)) satisfies it (y is a gate). Correct.
- (K3). (a) v's play is v followed by s_t(v)'s play. (b) an e-vertex f on a cycle: its successor is not c_W (else f is not on its own
  cycle), so B-ONLY applies to f and Λ_t(f), which is on the same cycle as f and the most relevant there, would be at least as relevant as
  f: contradiction. (c) v ≠ Λ: the path from s_t(v) is the path from v minus v (this holds also when v is on the cycle: then v is less
  relevant than Λ and is not added); v = Λ: Π_t(v) = ∅ and Π_t(s_t(v)) has cycle vertices only, which are less relevant than Λ, so it is
  ∅ (the packet's weaker «no e-vertex» suffices). (d) by B-ONLY e is more relevant than Λ_t(e); e is not on the cycle (b), so e ∈ Π_t(e)
  and Π_t(e) = Π_t(w) ∪ {e}; e ∉ Π_t(w) because a positional play passes e at most once and e is not on the cycle. E grows by e, the
  most relevant element of the difference: class_t(e) > class_t(w). (e) the self-loops; the e-vertices into c_W (Π = ∅: nothing on that
  path is more relevant than c_W except K0, K3, which it does not meet); the core as in (K2); «largest»: the cycle nodes that occur are
  β-vertices, K1, c_X, c_W (K2 is never a cycle node by LOC-K2), and c_W has the top even priority below K0, K3 only; a play with cycle
  node c_W has Π = ∅. Correct.
- (K4). NO-TIE then LOC-GATE: Ω_t(a) ◁ Ω_t(b) for a = σ̄_t(g). Both faces are outside the core: (K2) gives class_t(a) ≤ class_t(b);
  g is not an e-vertex, (K3 (c)): class_t(g) = class_t(a). Correct, with the added clause «σ̄_t(g) has that class».
- (K5). DOM: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)) for every gate y of x. x has priority 0 and Λ_t(y) priority ≥ 2 (CN2), so x is not added:
  ext(x, Ω_t(y)) = (Λ_t(y), Π_t(y), k_t(y) + 1). (K2) for this triple and Ω_(t+1)(x): class_t(y) ≤ class_(t+1)(x). Correct. DOM is the
  only place the ALL-SWITCH rule enters (a mover that keeps a non-best gate breaks DOM).
- Lean (cited only as «Lean-checked (lane)», not built by me, never a premise): Genome.k1, Genome.k2, Genome.k3, Genome.k5 at claude/l-formal
  f74d38a4 (the commit the packet names); at claude/l-formal e14f5508 (the Lead's brief), whose INDEX also lists Genome.k4 (GenomeK4),
  Genome.l2, Genome.l3, Genome.l5, Genome.plateau_g (bound N, stronger than the packet's), Genome.quiet and Genome.all_tcyc,
  Genome.all_tcyc_sharp (GenomeAllTCyc). N-2 (no change required): the packet's sentences «(K4) is stated there (K4Statement) and NOT
  proved in Lean» and §12's «NOT formalized» list are true at f74d38a4, which is the commit they name; they are stale at e14f5508. No
  statement of the packet depends on them.

## Box 2: §4 Lemma LEVEL, §5 counting, §6 WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC

### 2.1 §4 Lemma LEVEL (L1)-(L5): SIGN
- Setting: for a ≤ t ≤ b, (K1) gives class_t(v) ≤ class_b(v), so «lags» = «strictly below its class at b». Correct.
- (L1). v ∈ LAG_(t+1): class_t(v) ≤ class_(t+1)(v) < class_b(v), so v ∈ LAG_t and class_(t+1)(v) ≥ m_t: (i) m_(t+1) ≥ m_t; (ii) if equal,
  FRONT_(t+1) ⊆ FRONT_t. Stall: every v ∈ FRONT_t keeps class m_t < class_b(v), so it stays in LAG with class m_t: m_(t+1) ≤ m_t, hence
  =, FRONT_(t+1) ⊇ FRONT_t, hence = by (ii). Non-stall: some v ∈ FRONT_t rises ((K1)); if LAG_(t+1) ≠ ∅, either m rises or m stays and
  v leaves the front, |FRONT| falls and −|FRONT| rises. Exhaustive. Correct.
- (L2). Never lagging: K0, K1, K2, K3, c_W, c_X, e-vertices into c_W ((K3 (e)), constant classes), β-vertices into K0 ((K3 (c)) with
  K0 constant). An e-vertex e with mover successor w: if w does not lag, (K3 (d)) at t and at b (e's successor is frozen) gives
  class_t(e) = class_b(e); if w lags, class_t(e) > class_t(w) ≥ m_t, so e ∉ FRONT_t. What is left: movers, gates, β-vertices into a
  mover. Correct.
- (L3). Along any play the class does not rise ((K3 (c)); (K3 (d)) falls at e with mover successor; (K3 (e)) equal at e into c_W). So
  every vertex of the play of v ∈ FRONT_t has class ≤ m_t: it does not lag or it is in FRONT_t. The play's cycle is K1's loop, c_W's loop,
  or has no e-vertex ((K3 (b))), no core vertex (a play entering the core ends in K1's loop), no c_X ((D4): c_X has no in-edge from
  another vertex, so c_X is on a play only as its first vertex, and v ≠ c_X by (L2)) and no c_W. On it the kinds alternate mover → its
  chosen gate → the gate's chosen face, which is not the e-face (no e-vertex) → the β's frozen successor, a mover (not K0). Case all of
  the cycle lags: not K1's or c_W's loop (constant classes); all in FRONT_t; all of the class (c, Π = ∅) = (c, ∅) of the cycle node c,
  which is not a mover or gate (CN2): a β-vertex. That is (β). Otherwise a lagging z with non-lagging successor y exists on the play
  (the last lagging p_i on the tail, or going round a partly lagging cycle); z ∈ FRONT_t. z a gate: class_b(z) ≤ class_b(y) ((K4) at
  b) = class_t(y) = class_t(z), so with (K1) z does not lag: impossible. z a β-vertex: same with the frozen successor. z an e-vertex,
  core, c_W, c_X: excluded by (L2). So z is a mover, y = σ_t(z), m_t = class_t(z) = class_t(y) = class_b(y). That is (α), and the «then»
  of (α) holds for EVERY such z (the argument uses only that z ∈ FRONT_t and σ_t(z) ∉ LAG_t), as my replay tests. Correct.
- (L4). Stall. The map s on FRONT_t: mover z ↦ σ_b(z) = w: class_b(w) = class_b(z) > m_t ((K3 (c)) at b) and class_t(w) ≤ class_(t+1)(z)
  ((K5)) = class_t(z) = m_t (the stall), so w lags at t with class ≤ m_t, so = m_t: w ∈ FRONT_t. Gate g ↦ σ̄_t(g) = r: class_t(r) =
  m_t; if r did not lag, class_b(g) ≤ class_b(r) = class_t(r) = class_t(g) and g would not lag; so r lags, r ∈ FRONT_t, and by (L2) r is
  not e_g: r = β_g. β_g (into a mover y) ↦ y: class_t(y) = m_t, class_b(y) = class_b(β_g) > m_t: y ∈ FRONT_t. s maps the finite FRONT_t
  into itself; a cycle of s exists and runs mover → (x, σ_b(x)) → β_(x, σ_b(x)) → xt(x, σ_b(x)), a cycle of the Ξ-graph through the
  options σ_b(x_i). Only the mover case uses the stall. Correct.
- (L5). (L3): m_t ∈ {class_b(g) : g a gate} ∪ {(c, ∅) : c a β-vertex}, at most 2M values, at most M if (α) everywhere; 1 ≤ |FRONT_t| ≤
  N + 2M by (L2). So Φ = (m, −|FRONT|) takes at most 2M(N + 2M) = P values, M(N + 2M) under (α). Correct.

### 2.2 §5 (C1)-(C4): SIGN
- The states with LAG ≠ ∅ form an initial segment [a, b′) of [a, b] (LAG only shrinks, (L1); LAG_b = ∅); Φ never falls on it, so its
  maximal constant-Φ intervals [u_i, v_i] take q distinct values: (C1) q ≤ P, q ≤ M(N + 2M) under (α) on [a, b′). (C2): inside an interval
  every step is a stall ((L1): a non-stall step changes Φ or empties LAG); the steps v_i → u_(i+1) change Φ and v_q → b′ empties LAG, so
  they are not stalls (a stall keeps Φ and LAG ≠ ∅); hence exactly q non-stall steps on [a, b′] and b′ − a = q + Σ(v_i − u_i). (C3) from
  (L1) on the plateau and (L4) at its first step. (C4): for b′ ≤ t ≤ b, class_(b′) = class_b pointwise (LAG_(b′) = ∅) and (K1) squeezes
  class_t; so the steps b′ → … → b are quiet and lie in one maximal quiet window; landed R126 QUIET-N (scope: every genome) gives
  b − b′ ≤ N. Correct. (C4) uses QUIET-N as landed, through its clause «every maximal window of quiet steps has at most N steps», and
  nothing else of R126.

### 2.3 §6: SIGN on every statement
- Theorem WIN. No vertex of S lags on [a, b] (reference b; their classes are constant there). (i) a stall gives (L4)'s Ξ-cycle inside
  LAG_t; S meets it: contradiction. (ii) (β) gives the play cycle mover → chosen gate → β-face → xt, a Ξ-cycle through the options σ_t(x),
  all lagging: contradiction; so (α) holds at every state of [a, b′) and (C1) gives q ≤ M(N + 2M); by (i) every interval is a single
  state and (C2) gives b′ − a = q. (iii) is (C4). b − a ≤ M(N + 2M) + N = A. Correct.
- Corollary R-INT: WIN with S = {R} (Ξ-feedback number 1: {R} meets every Ξ-cycle). The loud steps are the q steps before b′ (each
  changes a front class) and the steps after b′ are quiet: «at most M(N + 2M) loud, and they come first». Correct.
- Theorem R-HEIGHT: reference T. A change of class(R) at t → t + 1 puts R in LAG_t; at a stall (L4)'s Ξ-cycle lies in FRONT_t and contains
  R (R is on every Ξ-cycle), and no front vertex changes class at a stall: so the step is one of the q ≤ P non-stall steps. (K1): the
  classes at different change times differ, D^tot(R) = 1 + #changes ≤ P + 1. Correct.
- Theorem K1-TCYC: on a plateau [u_i, v_i] (reference T), (C3) puts a Ξ-cycle inside J, R on it, so class(R) = m on [u_i, v_i]; WIN on
  [u_i, v_i] with its own reference v_i gives v_i − u_i ≤ A. T = b′ + (T − b′) ≤ q(A + 1) + N ≤ P(A + 1) + N. Correct.
- Theorem FVS-TCYC: W(S) over intervals on which S keeps classes, S ⊆ F_0 (a minimum Ξ-feedback set, |F_0| = k). W(F_0) ≤ A ≤ P + N
  (A = M(N + 2M) + N, P = 2M(N + 2M)). For S ≠ F_0 and such [a, b] (reference b): on a plateau, F_0 meets (C3)'s Ξ-cycle in a lagging x,
  so x ∉ S (S does not lag) and S ∪ {x} ⊆ F_0 keeps its classes on the plateau: v_i − u_i ≤ w_(|S|+1). Then b − a ≤ q(w_(|S|+1) + 1) + N
  ≤ P(w_(|S|+1) + 1) + N. Induction: with X := (P + N)(P + 1)^(k−j−1) ≥ P + N, P(X + 1) + N = PX + P + N ≤ X(P + 1). T_CYC = W(∅) =
  w_0 ≤ (P + N)(P + 1)^k. Correct (at k = 0: w_0 = W(∅) ≤ A, consistent).
- The k = 0 remark (WIN gives T_CYC ≤ A, weaker than landed R122's T_CYC ≤ N) is arithmetic and consistent.
- No statement of §3-§6 uses §7, F1, [OPT], (D1) or BR-SEG-G (read proof by proof). The Lead's 17:52Z ruling «If a referee refuses
  PLATEAU, LEVEL, WIN, R-INT, R-HEIGHT, K1-TCYC and FVS-TCYC still stand or fall on their own» is consistent with the dependency graph.
- Lean: level_count (claude/l-formal f74d38a4) is the abstract bookkeeping of (L1), (C1), (C2) («Lean-checked (lane)»); Genome.l2,
  Genome.l3, Genome.l5 at e14f5508 (INDEX rows «box 208 §3 (L2)», «(L3)», «(L5)»), not built by me, not premises.

## Box 3: §7 Lemma PLATEAU, §8 Theorem ALL-TCYC

### 3.1 §7 Lemma PLATEAU (P1)-(P7): SIGN
Plateau [u, v], u < v, reference b; Φ = (m, −|J|), J = FRONT_u; every step inside is a stall; v < b (LAG_v ≠ ∅). Y := {x : class_u(x) ≤ m}.
- (P1). x ∈ Y lagging at u: class ≥ m and ≤ m, so x ∈ J, class m at every s ∈ [u, v] ((L1) on the plateau). x ∈ Y not lagging: class_u(x)
  = class_b(x), constant on [u, b] ⊇ [u, v] by (K1). x ∉ Y: class > m at u, and at s by (K1). So {class_s ≤ m} = Y and classes on Y
  are constant. Correct.
- (P2). class_s(s_s(x)) ≤ class_s(x) ≤ m ((K3 (c), (d), (e))), so s_s(x) ∈ Y by (P1). Correct.
- (P3). For s < v (exists, u < v): class_s(y) ≤ class_(s+1)(x) ((K5)) = class_s(x) ≤ m ((P1)), so y ∈ Y, its class is constant on [u, v],
  and the inequality also holds at s = v. Correct.
- (P4). The chosen face has the class of g ((K4)), hence lies in Y. (1) one face outside Y has class > m ≥ class_s(g) at every s, never
  chosen. (2) faces of different constant classes: the lower one is chosen at every s ((K4)). (3) equal classes: e_g's successor is not
  c_W (else class(e_g) = (c_W, ∅), the largest class that occurs ((K3 (e))), and m < class_b(x) ≤ (c_W, ∅) for x ∈ J, so e_g ∉ Y); so
  e_g ∈ E_s(e_g) = E_s(β_g) ((K3 (d)) and equal classes): β_g's play passes e_g, entering it by its only in-edge g → e_g ((D1)); a
  positional play passes g once, so σ̄_s(g) = e_g, at every s. K2: LOC-K2. Correct. Case (3) is the only place (D1) is used.
- Is (P4) used outside a plateau? No. (P4) is stated and proved for s ∈ [u, v] only and is used only in (P5), for s ∈ [u, v]. (P6)'s
  induction runs to states s′ > v but uses there only: the static facts «movers of Y have all their gates in Y» ((P3) as a set statement)
  and «(P2) at the plateau state s», plus [OPT] and F1 at s′ + 1. It does not use (P2) or (P4) at s′ > v (box 208's original wording did;
  that is the gap G-P6 the packet credits to REFEREE 32 and L-RED-B, and the repaired text no longer does it). Checked.
- (P5). H on Y: movers of Y keep all their gates (in Y, (P3)); every other vertex keeps s_u(x) ∈ Y ((P2)). For s ∈ [u, v] and x ∈ Y not
  a mover, s_s(x) = s_u(x): gates by (P4), K2 by LOC-K2, the rest frozen. So every play from Y under (σ_s, σ̄_s) uses H's edges and
  Ω_s(x) is x's VJ value in H under σ_s|Y (a VJ value depends only on the play and on the relevance order and parities, which H
  inherits). Odd has one strategy in H, hence optimal. The step s → s + 1 at a mover x of Y compares the Ω_s values of x's gates = their
  H values: it is a step of H's Howard rule as BR-SEG-G's setting states it («every Even v goes to a ⊴-best successor under Ω_t and keeps
  σ_t(v) when it is one»; the other Even vertices of H have one successor). So σ_u|Y, …, σ_v|Y are consecutive states of a Howard run of
  H as long as each step changes the strategy. Correct.
- (P6). Suppose no mover of Y switches at s → s + 1 (u ≤ s ≤ v; the step exists since v < b ≤ T). Induction on s′ ∈ [s, b]: (A) σ_(s′) =
  σ_s on the movers of Y; (B) Ω_(s′) = Ω_s on Y. (A) at s′ + 1: x kept σ_s(x) at s → s + 1, and the rule makes x go to a ⊴-largest
  successor, so σ_s(x) was ⊴-largest under Ω_s; x's gates are in Y and have at s′ the values of s ((B)), so σ_s(x) = σ_(s′)(x) is
  ⊴-largest under Ω_(s′) and the keep rule keeps it. (B) at s′ + 1: Odd's σ̄_s against σ_(s′+1): from x ∈ Y the play under (σ_s, σ̄_s)
  stays in Y ((P2) at s), and σ_(s′+1) agrees with σ_s on Y's movers, the other Even vertices being frozen: the same play, value
  Ω_s(x). [OPT] at s′ + 1 (σ̄_(s′+1) is pointwise optimal, so its value is ⊴ the value under the positional σ̄_s): Ω_(s′+1)(x) ⊴ Ω_s(x).
  F1 (every step of the run): Ω_(s′+1)(x) ⊵ Ω_(s′)(x) = Ω_s(x). Equal. At s′ = b: class_b = class_s on Y ⊇ J, so J does not lag at s:
  contradiction with J = FRONT_s ⊆ LAG_s. Correct. This (B) step, «Odd answers by σ̄_s, then [OPT], then F1», is referee-originated
  (REFEREE 32's repair of G-P6, per the packet and L-1); under Lead reading L41 I sign it independently here, re-derived above from
  [OPT] (R123 / R122) and F1 (R118 (b)) only.
- (P7). The v − u steps are steps of a Howard run of H ((P5), (P6)); on Y no Λ changes ((P1): Λ is part of the class) and Odd has no choice
  in H: R118's labels on H's run give p-steps, so they lie in one maximal p-run of that run. H0 holds for every step of every Howard run
  of H: a step switches a mover of Y; a mover is never the cycle node of its play under a positional pair of H, because such a pair
  extends to a positional pair of IDEAL-CYC(G) with the same plays from Y (Y is closed under H's edges; the non-mover Even vertices of Y
  keep their frozen successors, which are IDEAL-CYC's; movers of Y choose among their own gates; outside Y choose anything), and CN2
  holds for every positional pair of IDEAL-CYC(G). Landed R118 (i) BR-SEG-G (a) on the parity game H: v − u ≤ n_E(H) ≤ N + 2M + 5.
  Correct. Two details I checked: BR-SEG-G's scope is «any parity game, Howard from any σ_0, under H0», so H and the start σ_u|Y are
  allowed; and R118's labels count Λ-changes «for some vertex v» of the game in question (H), which (P1) excludes on Y.
- Remark SHARP (not to sign): correctly kept out. Landed BR-SEG (R118 (d)) is stated for IDEAL-CYC(G), not for H; L-RED 66's route uses
  lane lemmas. Not signed by me. (L-FORMAL's Genome.plateau_g at e14f5508 claims the bound N in Lean, lane-level; not a premise here.)

### 3.2 §8 Theorem ALL-TCYC and its «Consequences»: SIGN
- Reference T, a = 0: T = b′ + (T − b′) = q + Σ(v_i − u_i) + (T − b′) ≤ P + P(N + 2M + 5) + N = P(N + 2M + 6) + N ((C1), PLATEAU on each
  of the q intervals, single-state ones contributing 0, (C4)). Correct.
- Consequences: R (steps at which σ̄ changes), Q (loud steps) and D^tot(v) − 1 (≤ the steps at which v's class changes, (K1)) each count
  steps of the run, so each is ≤ T_CYC. Correct and trivial.
- «Against K1-TCYC and FVS-TCYC» (not to sign), redone: A + 1 ≤ N + 2M + 6 ⟺ M(N + 2M) ≤ 2M + 5, false for M ≥ 2 (M = 2: 2(N + 4) ≥ 10
  > 9; M ≥ 3: M(N + 2M) > 2M² ≥ 6M > 2M + 5). (P + N)(P + 1) ≥ P(N + 2M + 6) + N ⟺ P² ≥ (2M + 5)P ⟺ P ≥ 2M + 5, true for M ≥ 2 (P =
  2M(N + 2M) ≥ 4·5). M = 1 (N = 1, P = 6, A = 4): 6·9 + 1 = 55, 6·5 + 1 = 31, 7·7 = 49. All as printed.
- What ALL-TCYC changes in the landed record (§13): R118's «no bound on R is claimed (OPEN)» gets a bound for IDEAL-CYC only; R126's
  «whether max_g min(D^tot(e_g), D^tot(β_g)) is polynomial in N + M at k = 1 is OPEN» is answered (D^tot(v) − 1 ≤ T_CYC). Both readings
  are right, and both need the «Consequences» bullet, which L-1 does not carry (box 5, L-1 item R-1).
