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

## Box 4: DATA (the lane's, re-read) and my own replay

### 4.1 The lane's DATA, re-read by column name (R2-P-N5-LEVEL/r2lvdata.py, out r2lvdata.out; not the lane's summ208*.py)
The frozen outputs of experiments/new/box208/out/ at 1e6df499 were read with `git show`. For each file the script gives the rows, the sum
of the must-0 counters by name (16 for level208 / own208 / mut208, 6 for plat208, 49 for rv208) and the descriptive maxima:
- level208: records 25 rows, corpus 53, rand 2,000 + 6 × 500 = 5,000, mut208 8 × 250 = 2,000; own208 (second engine) 25 + 53. Must-0 sum
  0 on every file. Descriptive values equal §11's table: corpus max T 199, Φ values 199, stalls 48 (loud 23), plateaus 15 (longest 13),
  windows 615; records max T 114, stalls 31 (loud 0), plateaus 14 (longest 9), windows 556; mutant maxima (e.g. MWR4_2 platmax 26).
- plat208: records 25, corpus 53, rand 3,600, mut 600 + mut2 600: must-0 sum 0; longest plateau 9 / 13 / 4 / 15 / 25 as in §11.
- rv208: frozen 81 genomes, mut 480, rand 3,300: must-0 sum 0, 0 VIOLATION lines; frozen max T 199, plateaus 538 (longest 13).
- Controls fire: level208_ctrl1 (winstall 8 on 4 genomes), ctrl1_rand (50), ctrl2 (198), plat208_ctrl1 (211), rv208_ctrl1 (1,930).
- L-1's DATA numbers (25 / 53 / 5,000 / 2,000; 78 / 3,600 / 1,200; 81 / 480 / 3,300; «at most 199 values of Φ», «no plateau longer than
  26 steps») equal these. DATA rule: every clause names its counters; nothing claimed from DATA is a statement. «NO RUN TESTS THE
  CONSTANTS» (§11): agreed; P = 2,120,796 on MW32_2 against 199 values of Φ.

### 4.2 Own replay: tool (R2-P-N5-LEVEL/r2lv.py; doc string has every counter and its unit)
- Engine: REFEREE-2's R2-P-ACYC/r2acyc.py (Γ(G) built from R104's text; own VJ values and order; Odd's optimum by strict switch-all policy
  iteration from the worst start, cross-checked against a second start at every state). The Howard loop is written in r2lv.py from R118
  (a)'s text: keep σ_t(x) if it is ⊴-best, else a ⊴-best gate chosen by --tie max | min | rand. e-priority order of [DEF] («even, above
  every β»): --eorder gate (gate index) or lev (level, then gate index); both satisfy [DEF].
- Class key: (reward(Λ), Σ 2^rel(e)), whose integer order is the packet's order (1.2).
- 44 must-0 counters: the landed premises re-tested (CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, F1, DOM, local optimality of σ̄, PI-start
  agreement, QUIET-N); (K1)-(K5) ((K2) on all pairs of non-core vertices at t, t and t, t + 1 when there are at most 110 of them, else on
  4,000 random pairs per pair of states); for every reference b (all b on the --ball runs and on every run with n·T² ≤ 3·10^7, else T and
  6 random b): (L1) both halves, (L2), (L3) («(α) or (β)», and the «then» of (α) for EVERY qualifying mover, of (β) for EVERY qualifying
  cycle), (L4) (the map s into FRONT_t, σ̄_t(g) = β_g at front gates, and an s-cycle mover → σ_b(x) → β-face → xt), (L5) (≤ P values, ≤
  M(N + 2M) under (α) everywhere, and m_t in the 2M-set), (C2), (C3), (C4); WIN (i)-(iii) for every maximal interval of every minimum
  Ξ-feedback set S (all of them at k ≤ 2, one at k = 3; k found by exhaustive search) and for S = all movers; R-HEIGHT at k = 1; the
  bounds K1-TCYC, FVS-TCYC, ALL-TCYC; for every plateau of every reference: (P1)-(P4), (P5) (H built on Y and valued by a separate VJ
  routine, equal to Ω_s on Y; σ_(s+1) an allowed H-Howard choice), (P6), (P7) (v − u ≤ n_E(H); no Λ change on Y), H0 on every step of
  H's own Howard run from σ_u|Y and its longest p-run ≤ n_E(H), and that run equal to σ_(u+1..v)|Y.

### 4.3 Sets and results (sweep_sets.out, ball_every_b.out, frozen_max_gate.out; scripts sweep.sh, sweep2.sh; one process per file)
| set | runs | fail counters (sum) | descriptive |
| --- | --- | --- | --- |
| 25 frozen k = 1 genomes + 3 R118 (m) genomes, tie max, eorder gate | 28 | 0 | max T 114, plateaus 17 (longest 9), stalls 44 |
| the same, tie min, eorder lev | 28 | 0 | max T 114, plateaus 19 (longest 9), stalls 47 |
| 53 genomes of box202/inst, tie max, eorder gate | 53 | 0 | max T 199, plateaus 16 (longest 13), stalls 49 |
| the same, tie min, eorder lev | 53 | 0 | max T 199, plateaus 15 (longest 13), stalls 48 |
| all 81 above, EVERY reference b = 1, …, T (--ball) | 81 (2,655 references) | 0 | 465 plateau checks; P4 cases (1) 94,002, (2) 206, (3) 43 |
| random, r2end.gen «any» (Ξ-targets anywhere), seeds 3911-3918 | 2,000 | 0 | k 0: 88, 1: 540, 2: 692, 3: 437, ≥ 4 / not searched: 243; mover ties 127 |
| random «self» (≥ 1 Ξ self-loop), seeds 3921-3924 | 1,000 | 0 | mover ties 54 |
| random «acyc», seeds 3931-3932 | 500 | 0 | k = 0 on all 500 |
| random «any», tie rand, eorder lev, seeds 3941-3944 | 1,000 | 0 | mover ties 69 |
| own mutants (r2split.mutate) of BLKX26, CFI3, CW4_n, K1F21, K1L10, K1L7, MWR4_2, RINT, 100 each, seed 3951 | 800 | 0 | max T 37, plateaus 813 (longest 21) |
| the same, tie min, eorder lev, seed 3952 | 800 | 0 | max T 37, plateaus 798 (longest 22) |
- On every set: (L3) never had (α) and (β) at once at a state (rec_l3_both 0); (β)-only states occur (e.g. 567 on the --ball run);
  no plateau is longer than the number of movers of its Y (rec_plat_over_moversY 0): DATA consistent with remark SHARP, not a proof of it.
- The tie rule is free in R118 (a); my three rules (max, min, random) and two e-orders agree with the statements. My runs' lengths T
  and plateau counts differ slightly between configurations (as the tie rule and e-order change the run); the lane's numbers are for its
  own engine and rule.

### 4.4 Controls (controls.out; each must FIRE, and each does)
| control | what it breaks | set | fired |
| --- | --- | --- | --- |
| fronthigh | FRONT := the HIGHEST lagging class | 8 genomes (3 R118 (m), CFI3, MWR4_2, RINT, K1L10, WC8_2) | l1 713, l2 1,427, l3 1,427, l4map 1,986, l4cyc 1,126, l5 1,427, c2 84, p1 346, p2 167, p3 1,393, p4 179 |
| snonfvs | WIN with S := a mover in no minimum feedback set | same | winfail 9 |
| yfront | PLATEAU with Y := J | same | p2 2,500, p3 4,802 |
| k5t | (K5) with class_t(x) in place of class_(t+1)(x) | same | k5fail 280 |
| edom | [DEF] broken: one β-vertex gets an odd priority above every e-vertex (E-DOM fails) | same | bonly 188, notie 6, pistart 1, k1 38, k2 7,040, k3b 1, k3d 12, k4 15, k5 80, l1 22, l2 48, l3 7, l4map 8, l4cyc 3, l5 3, c2 8, win 1 |
| hval (mechanics) | H valued with relevance by index | same | p5val 65,080, p5step 3,848, p7run 101 |
| p6out (mechanics) | (P6) asked of the movers OUTSIDE Y | same | p6fail 304 |
| htie (mechanics) | H's own run with the opposite tie rule | same: NOTHING (no mover tie on those plateaus); 1,000 random (seeds 3911, 3912 any; 3921, 3922 self) | p7runfail 2 |
- edom is the control for the genome-only steps (5.2): with E-DOM broken on Γ(G) itself, (K1), (K2), (K4), (K5) and LEVEL fail.

## Box 5: scope, genome-only steps, TARGET.md diff, line L-1, verdicts

### 5.1 Scope (checked against every proof)
- Rule: Howard ALL-SWITCH, Even = MAXIMISER of ⊴ improves, Odd answers optimally ([OPT]), switch-best with keep-if-best, any choice among
  several ⊴-best non-current successors. Every statement of §6-§8 goes through (K5) (via (L4), or (P3) in PLATEAU), and (K5) rests on DOM,
  which needs every mover at a ⊴-best gate after every step: a single-switch rule is NOT covered, as the packet says. The tie choice is
  free: my replay uses three tie rules (max, min, random) and all counters are 0 on each (box 4).
- Games and run: IDEAL-CYC(G) of R118 (a), every R104 genome (Ξ-cycles and Ξ self-loops allowed), the run from R104's start. NOT N5 (its
  S4a step is not a Howard step), NOT N5′-xi (on Γ3 or off it), NOT M4, NOT M3. Nothing is claimed for Γ3: the level208_g3_* rows are
  DATA on another run, and no statement uses them.
- The packet's scope section says the same (P-N5-LEVEL l. 16-35), and L-1's tail says the same. Correct.

### 5.2 Genome-only steps (every step that uses a property of Γ(G) or of IDEAL-CYC beyond «a parity game under Howard's rule»)
My list, from the proofs as re-derived in boxes 1-3:
1. (K1): E-MON (R121, IDEAL-CYC). (The Λ half is general: F1 with (VJ-1), N-1.)
2. (K2): E-DOM ([DEF]'s priorities: above an e-vertex only e-vertices, c_W, K0, K3); (D3) (the core is entered only at K0); the frozen
   K0 → K3 and K1 → K1; LOC-K2 (σ̄(K2) = K1).
3. (K3): (b), (d) from B-ONLY (R123); (e) from [DEF]'s priorities (top), the freeze and LOC-K2. ((a), (c) are general.)
4. (K4): NO-TIE and LOC-GATE (R123), with (K2); every Odd vertex with a choice is a gate with exactly two faces, or K2 ([DEF]).
5. (K5): DOM (R118 (c), IDEAL-CYC) and CN2 (movers have priority 0 and are never cycle nodes), with (K2).
6. (L2): the successor kinds of [DEF] (e → mover or c_W; β → mover or K0) with (K3 (d), (e)).
7. (L3): CN2 (the cycle node of a fully lagging cycle is a β-vertex), (D4) (c_X has no in-edge from another vertex), and the alternation
   mover → gate → face → mover of [DEF].
8. (L4): (K5) at the movers, (K4) at b at the gates, the β-vertex's frozen successor = its Ξ-target: the front cycle IS a Ξ-graph cycle.
9. (L5): M gates, M β-vertices, |FRONT| ≤ N + 2M.
10. (C4), hence WIN (iii), R-INT, K1-TCYC, FVS-TCYC, ALL-TCYC: QUIET-N (R126).
11. WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC: the Ξ-graph and its feedback sets (R126's definition) meet every front cycle (L4) / (β) cycle.
12. (P4): (D1) in case (3), with (K3 (d), (e)) and the «largest class» clause; LOC-K2.
13. (P5): the only vertices with a choice are movers, gates and K2; every other Even vertex is frozen (R118 (a)).
14. (P7): H0 on H through CN2 for positional pairs of IDEAL-CYC(G); n_E(H) ≤ N + 2M + 5.
- N-3 (no change required; §9 is READING, not to sign): the packet's §9 names items 1, 2 (E-DOM), 3, 4, 5, 10, 12 and «(L2), (L4)»; it
  does not name (D3) / LOC-K2 inside (K2) (they are in (K2)'s proof), CN2 / (D4) in (L3), or CN2 in (P7)'s H0. These are genome steps too.
  None changes a statement. The «Friedmann G_N» DATA (L-COMP 19, cited, not re-run by the lane or by me) is consistent with item 2: the
  first failure is (K2) inside (K5) at an odd vertex above an escape vertex, which E-DOM excludes.
- My control edom (box 4) breaks item 2 on Γ(G) itself (one β-vertex gets an odd priority above every e-vertex): B-ONLY, NO-TIE, (K1), (K2),
  (K3 (b), (d)), (K4), (K5), (L1)-(L5), (C2) and WIN counters fire (4.4). The genome property is load-bearing, on my engine too.

### 5.3 TARGET.md diff (TARGET.md sha1 a41d5e1a…, same at 68c8d293 and 7fa6aff4)
- §2 (M4) and §4's first bullet are quoted verbatim (r2lvq.py, «TARGET» bullets). The packet has no algorithm for parity games and claims
  none: it counts steps of one improvement rule in the model IDEAL-CYC on the games Γ(G). Not M4. §4: «Polynomial only on a restricted
  class» does not count as M4; it may count as M3 only if stated in TARGET.md's vocabulary and checked for novelty by L-LIT (§7e); neither
  is done, and the packet presents no M3. Not M3.
- §5 step 4 («Written correctness and running-time proofs, double-refereed with every gap listed») is about an algorithm claim on every
  parity game; this packet is not one. Not a step-4 pass. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
- §3 (bit cost): no arithmetic is analysed; the bounds count steps. Nothing to diff.
- No statement of the packet is phrased in TARGET.md's vocabulary or claims to be. PASS.

### 5.4 Line L-1 against «To sign» (L-1 sha1 28565b3c…, 7,239 B; rebuilt byte-equal, 1.0)
Item by item, L-1's statement against the packet's row:
- Setting (IDEAL-CYC, the Howard step with keep-if-best, every genome, N, M, the run's states, class, loud / quiet, the order, P, A): equal.
- (K1), (K2) (for triples), (K5): equal in content. (K3): L-1 gives (c) and (d) («a vertex has the class of its successor on its play,
  except an e-vertex with a mover successor, whose class is strictly larger»); this also covers e-vertices into c_W (equal classes,
  (K3 (e))). (a), (b) and (e)'s constancy are not in L-1. (K4): L-1 omits «σ̄_t(g) has that class». Both say less, nothing wrong.
- LEVEL: «Φ never falls; it stays equal exactly at a stall», the stall cycle with options at b, gates at b and β-faces, at most P values:
  equal to (L1), (L4), (L5) (Φ is defined where LAG ≠ ∅; at a non-stall step with LAG_(t+1) = ∅ it is undefined, so «exactly» is right).
  (L2), (L3) and (L4)'s «σ̄_t(g_i) = β_(g_i)» are not in L-1 (lemma steps; fine).
- WIN: equal, except that (iii)'s «b − b′ ≤ N» is folded into «b − a ≤ A». R-INT: L-1 omits «at most M(N + 2M) of its steps are loud,
  and they come first». R-HEIGHT, K1-TCYC, FVS-TCYC, PLATEAU, ALL-TCYC: equal.
- ALL-TCYC's «Consequences» (a «To sign» row: «Theorem ALL-TCYC, with its bullet «Consequences»») is NOT in L-1. §13 of the packet says
  what a signed ALL-TCYC changes in R118 (the bound on R) and R126 (D^tot at k = 1); without the bullet the line does not state either.
- Premises: equal to §1 (R104 + (D1), (D3), (D4); R118 (a), (b) F1, (c), (e) with its stated reason, (i) BR-SEG-G (a) under H0; R121
  E-MON / E-DOM; R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, [OPT]; R126 QUIET-N). The sentence «the class facts, LEVEL, WIN, R-INT,
  R-HEIGHT, K1-TCYC and FVS-TCYC use neither PLATEAU nor F1, [OPT], (D1) or BR-SEG-G» is true (2.3).
- Tail: scope, «not an argument about Howard's rule on parity games in general», supersession arithmetic, the L41 credit of the (P6) step
  to REFEREE 32 with L-RED-B's independent G-1, DATA clause by clause (numbers equal to my re-read of the frozen outputs, box 4), not M4 /
  not M3 / not a step-4 pass / G-N5-TIME OPEN, related lane statements named as not premises. Correct.
- DATA rule (L43; every DATA clause names its counter): the packet has no DEAD row. Each DATA clause of L-1 names its counters (the 16 of
  level208.py by name, the 6 of plat208.py by name, «the 49 must-0 counters of rv208.py», «the counter of (K5)» on G_N); units are given
  by reference («units in the packet §11»). Met.
- R-1 (requested for L-2; L-1 is signed without it, as SIGN WITH GAP below). Old, exactly once in L-1:
  «(Theorem ALL-TCYC) for every genome G, T_CYC ≤ P·(N + 2M + 6) + N (premises:»
  New: «(Theorem ALL-TCYC) for every genome G, T_CYC ≤ P·(N + 2M + 6) + N, and so are the number R of steps at which σ̄ changes, the
  number Q of loud steps and D^tot(v) − 1 for every vertex v (D^tot as in RESULTS R126) (premises:»
- R-2 (optional). Old, exactly once in L-1: «through DOM with CN2 in (K5),» New: «through NO-TIE and LOC-GATE in (K4), through DOM with CN2
  in (K5) and in PLATEAU's H0,».

### 5.5 Verdicts (Opus 5.5, D1). Statements as frozen in P-N5-LEVEL at 1e6df499.
| statement | verdict | conditions, gaps |
| --- | --- | --- |
| §3 (K1)-(K5) | SIGN | (K1) on R118 (e)'s stated reason or on F1 with (VJ-1) (N-1) |
| §4 Lemma LEVEL (L1)-(L5) | SIGN | none |
| §5 (C1)-(C4) | SIGN | (C4) uses landed R126 QUIET-N only |
| §6 Theorem WIN | SIGN | none |
| §6 Corollary R-INT | SIGN | none |
| §6 Theorem R-HEIGHT | SIGN | none |
| §6 Theorem K1-TCYC | SIGN | none |
| §6 Theorem FVS-TCYC | SIGN | none |
| §7 Lemma PLATEAU (P1)-(P7) | SIGN | (P6) step (B) is referee-originated (REFEREE 32); signed here independently under L41 |
| §8 Theorem ALL-TCYC, with «Consequences» | SIGN | none |
| line L-1 (sha1 28565b3c) | SIGN WITH GAP | «L-1 omits ALL-TCYC's «Consequences», a «To sign» row» (R-1, exact strings in 5.4) |
- No statement is REFUSED. No signed proof keeps an open gap. Notes N-1 to N-3 ask for no change.
- Not M3, not M4, not a step-4 pass. G-N5-TIME stays OPEN. N5 and N5′-xi stay CANDIDATES (D1). The bound is polynomial in N + M for the
  one rule (Howard all-switch) in the one model (IDEAL-CYC) on the genome games, and for nothing else.

### Statement of independence
- These verdicts rest on my derivations in boxes 1-3 and on my own replay (box 4). Before this verdict was on origin I did not open
  docs/referee/ (REFEREE 34's review, REFEREE 32's R-box208-preread.md), notes/REFEREE.md, L-RED 66's R235, L-RED-B's B1 or L-COMP 19's
  box 43. The packet's §10 told me where REFEREE 32 found G-P6 and what its repair is; I re-derived the repaired step myself (3.1).
- Lane code read: the headers and output formats of level208.py, plat208.py, rv208.py (to read their frozen outputs by column name) and
  mkl1_211.py (run once, isolated, to rebuild L-1). Nothing of the lane is imported by my replay.

## Addendum 1 (REFEREE-2 successor 39; written after my verdict 43824abc was on origin): N-2 measured at claude/l-formal 78c32d90 (Lead 21:28Z, optional item 1)
Object: claude/l-formal 78c32d90 (on origin 21:5xZ), lean/lemmas/INDEX.md and the .lean files, read with `git show` / `git grep`. I did
not build Lean (no toolchain in this container): every row below is the lane's claim «Lean-checked (lane)» (lake build passes, no sorry,
axioms ⊆ propext, Classical.choice, Quot.sound, per the INDEX header), checked by me only for (i) the theorem name in INDEX, (ii) the
name declared in a .lean file or printed by Axioms.lean's `#print axioms`, (iii) 0 occurrences of the words sorry / admit in lean/*.lean
(`git grep -w`). None is a premise of P-N5-LEVEL, and none changes a verdict.
The packet's sentences under test: §3 «(K4) is stated there (K4Statement) and NOT proved in Lean»; §12 «(K4) is stated and not proved.
NO-TIE, LOC-GATE, (L2)-(L5), (P1)-(P4), (P6), QUIET-N and ALL-TCYC are NOT formalized.» (both about f74d38a4, the commit they name).
| packet item | at 78c32d90 | INDEX row / theorem (file) |
| --- | --- | --- |
| (K4) | Lean-checked (lane) | «box 208 §2 (K4) GATES»: Genome.k4 (GenomeK4) |
| LOC-GATE | Lean-checked (lane), in ⊴ form, for any game | OptCounter.le_succ (GenomeK4; in Axioms.lean) |
| NO-TIE | NOT formalized | INDEX «Not formalized: … RESULTS R123 NO-TIE (not needed on the route to ALL-TCYC)» |
| (L2), (L3), (L5) | Lean-checked (lane) | Genome.l2, Genome.l3, Genome.l5 (GenomeLevel); (L5) «as its two factors» |
| (L4) | NOT formalized | INDEX «Not formalized: box 208 §3 (L4) …» |
| (P1)-(P4), (P6) | discharged inside PLATEAU on the genome | Genome.plateau_g (GenomePlateau), with IdealCycRun.window_le and IdealCycRun.gate_const (the (P4) form); bound N, STRONGER than the packet's N + 2M + 5; (P6) with REFEREE 32's repair |
| QUIET-N | Lean-checked (lane), as «a window of constant classes has at most N steps» | Genome.quiet (GenomePlateau), with gate_of_cls_eq_none |
| ALL-TCYC | Lean-checked (lane), for EVERY run of IDEAL-CYC(G), and the sharper P(N + 1) + N | Genome.all_tcyc, Genome.all_tcyc_sharp (GenomeAllTCyc) |
| WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC | NOT formalized | INDEX «Not formalized: … §5-§6 (WIN, R-INT, R-HEIGHT, K1-TCYC, FVS-TCYC)» |
- For L-2 (a note, not a requirement of my signature; L-2 carries Lean only as «related lane statements, not premises»): if L-2 names
  L-FORMAL's theorems, it should name the commit it reads (78c32d90 or later) and the list above, not f74d38a4's. L-1's own sentence
  «L-FORMAL's lane-level Lean theorems Genome.k1, Genome.k2, Genome.k3, Genome.k5, level_count, plateau and brsegG (claude/l-formal
  f74d38a4)» is TRUE as written (those names exist at f74d38a4); it is only incomplete.
- Not a premise and not a change of verdict: the Lean route bounds PLATEAU by N through lane statements (the SHARP route); my signature
  stays on the packet's N + 2M + 5 from landed BR-SEG-G (3.1).
- INDEX 78c32d90 also records the level-0 sub-case in QUIET's Lean proof (`gate_of_cls_eq_none`: both faces of a gate of class (c_W, ∅))
  «that box 208's text lacks». P-N5-LEVEL does not prove QUIET-N: (C4) cites landed R126 QUIET-N. So this affects box 208's own text
  only, not the packet. (P4) case (3) handles the (c_W, ∅) case explicitly (3.1).

## Addendum 2 (REFEREE-2 successor 39; 2026-11-13 00:02Z by date -u): byte test of fixes entry 1 + line L-2 (claude/l-new 366a38ab)
Objects (commit 5d30968afeb82c50427ab17ecce4fdd393ba6a66
Author: Claude <noreply@anthropic.com>
Date:   Thu Nov 12 22:34:35 2026 +0000

    REFEREE-2 39: R2-P-N5-WRAP Addendum 1 — the packet's ten REFEREE 33 [Q] items are verbatim in R-WRAP-preread (claude/referee 90703a81), checked after my verdict 07fd5ae4
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
    Claude-Session: https://claude.ai/code/session_01V5yGRaEeN3dRqjQP5twiRH

diff --git a/docs/referee-2/R2-P-N5-WRAP.md b/docs/referee-2/R2-P-N5-WRAP.md
index 5ee730ce4..6fe8822db 100644
--- a/docs/referee-2/R2-P-N5-WRAP.md
+++ b/docs/referee-2/R2-P-N5-WRAP.md
@@ -273,3 +273,9 @@ WRAP uses no property of H (Remark 1): correct, my random games have any owners,
   this verdict was on origin I did not open docs/referee/ (REFEREE 33's R-WRAP-preread, any REFEREE review of WRAP), notes/REFEREE.md, box
   104, L-COMP 20's box 44 or L-RED 66's R236 / R237, nor any lane tool. Claim NT's proof route is REFEREE 33's as the packet quotes it; I
   re-derived each step against the PDF (1.2).
+
+## Addendum 1 (REFEREE-2 successor 39; 2026-11-12 22:34Z by date -u; written after my verdict 07fd5ae4 was on origin): REFEREE 33's quotes
+- The packet's ten [Q] items from REFEREE 33 (§6 T-2, T-3, T-4 and «Status»; §7 F-1, F-2, F-3; §9 W-2; §10 two items) are verbatim,
+  whitespace-normalised, in docs/referee/R-WRAP-preread.md at claude/referee 90703a81 (35,268 B): 10 of 10 found (nested «…» tested piece
+  by piece). This closes the item left open in 1.1. Nothing in it changes a verdict. I read R-WRAP-preread only for this check, after my
+  verdict; agreement with REFEREE's own review of the packet (when it exists) is a separate line.): docs/new/P-N5-LEVEL-line-L2.txt sha1 d18125ed1c62f8ad20396d9f94eac8bdbc624cf4, 7,970 B; docs/new/P-N5-LEVEL-fixes.md
sha1 43891337f77cc3f3cfd830d6acfb06e569ddc8d7 (entry 1, LINE-ONLY); the packet unchanged (7c956df4…) and L-1 unchanged (28565b3c…) at
366a38ab. REFEREE 34's report read now (claude/referee 4c8d6c4f, docs/referee/R-P-N5-LEVEL.md), after my verdict 43824abc.
### Bytes (own script R2-P-N5-LEVEL/bt_l2.py, out bt_l2.out; not the lane's mkl2_211.py)
- My parser takes REFEREE 34's LT-1, LT-2, LT-3 and LO-1 from its §5 (wrapped lines joined with one space) and my R-1, R-2 from my 5.4 at
  43824abc, and applies them to L-1 in the fixes entry's order; each old string occurs exactly once (6 × 1). After LT-1..LT-3: sha1
  389645a2a646522a8fb57f05dba4458695ac74f2, 7,706 B = REFEREE 34's L-1′ (its §5). After R-1, R-2, LO-1: sha1 d18125ed…, 7,970 B, one line,
  0 «|», 93 «(» = 93 «)»; cmp with the lane's L-2: EQUAL. So L-2 = L-1 + exactly the six items; nothing else changed.
### Meaning
- R-1 (mine, REQUIRED; = REFEREE 34's LO-2): ALL-TCYC's «Consequences» now in the line, my exact string. Met; closes my SIGN WITH GAP.
- R-2 (mine, optional, adopted): NO-TIE and LOC-GATE in (K4), CN2 in PLATEAU's H0. Met.
- LT-1 (REFEREE 34): «199 on MW32_2, out/level208_corpus.out, where P = 2,120,796»: P = 2·657·(300 + 2·657) = 2,120,796 and phivals 199
  on MW32_2 (my r2lvdata.out); «26 on mutants of MWR4_2, out/mut208_MWR4_2_s2086.out, and of CW4_n, out/rv208_mut_s2094.out»: platmax 26
  in both files (rv208's per-base rows: CW4_n 26, MWR4_2 24). True.
- LT-2: L-COMP's README (claude/l-comp a6cce717, experiments/comp/box43/README.md) has a column k5 in its G_N table (l. 53). True as a
  citation; the G_N numbers stay cited, not re-run (as in the packet).
- LT-3: PG.Genome.k1, k2, k3, k5, PG.level_count, PG.plateau, PG.brsegG exist at claude/l-formal f74d38a4 (namespace PG; files GenomeK15,
  GenomeK2, GenomeK3, LevelCount, Plateau, Corollaries); «Lean-checked (lane) …, not through CHECKER» is the right label. True. (My
  Addendum 1's later-commit list stays a note, as the Lead ruled.)
- LO-1: «(named in its header; a counter that is 0 is not printed)»: rv208.py's header says exactly this. True.
- No statement, bound, label or premise of the line changes; the fixes entry records my N-1..N-3 as notes. One remark (no change asked):
  the Lead's «REFEREE 34's N-L1» is the note N-L1 of REFEREE 34's GATE test (R-P-N5-GATE.md §L, about GATE's lamch columns), not a LEVEL
  item; the entry's choice to record R-P-N5-LEVEL's N-1..N-5 under that heading is harmless.
### Verdict: L-2 (366a38ab, sha1 d18125ed) MATCHES. My SIGN WITH GAP on L-1 is closed by R-1; every statement of P-N5-LEVEL stays SIGN.

## Correction (REFEREE-2 successor 39; 2026-11-13 00:48Z by date -u; Lead 00:48Z)
- l. 413-435: pasted git show of 5d30968a, not part of this report. Cause: the shell expanded a backquoted command inside an unquoted
  heredoc when Addendum 2 was appended. The intended words at l. 413 are «Objects (from git show): docs/new/P-N5-LEVEL-line-L2.txt sha1
  d18125ed…». Addendum 2's byte test, meaning checks and verdict (l. 435 ff.) are unchanged. The pushed text is not rewritten.
