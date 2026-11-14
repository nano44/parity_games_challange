# Packet P-N5-QUIET (box 194): in IDEAL-CYC, Odd's choice at a gate is local (LOC-GATE), and the Howard run length is polynomial in the number of (cycle node, e-set) changes (QUIET, T-QUIET); hence, under [E-LEV], polynomial on genomes with boundedly many upward Ξ-edges (UP-T)
L-NEW successor 62 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-07 23:54Z: «GO, freeze packet P-N5-QUIET (LOC-GATE, CN2, LOC-K2, QUIET,
T-QUIET, UP-T, ASC-T)». FROZEN at push. Later text goes to docs/new/P-N5-QUIET-fixes.md, append-only. Source, history only:
docs/new/N5-LOC-box194.md (box 194). This packet carries every proof in full. L-RED 56 attacks LOC-GATE + QUIET (R221 item 1).
Labels: PROVED (L-NEW 62, unrefereed) / HYPOTHESIS (stated in the statement) / DATA / READING (not to sign).
This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME. N5′-xi stays a CANDIDATE.

## Scope (explicit, as asked)
- T is T_CYC of RESULTS R118 (a): the number of Howard steps of IDEAL-CYC(G) (Γ(G) with every non-mover Even vertex frozen at R104's
  start, Odd unrestricted at gates and K2) to the first state where no mover has a strictly better successor. Nothing else is counted.
- What it implies: T ≤ poly(N, M)·(1 + Σ_v (D^tot_E(v) − 1)) for every genome (T-QUIET); so R ≤ T and C ≤ T are bounded the same way;
  and T is polynomial in N + M for genomes with boundedly many upward Ξ-edges under [E-LEV] (UP-T), or whose plays have boundedly many
  ascents (ASC-T).
- What it does NOT imply:
  - nothing about general parity games, about N5, or about genomes with unboundedly many upward Ξ-edges (U(G) unbounded) and
    unboundedly many ascents: there T-QUIET only moves the question to Σ_v D^tot_E(v), which is OPEN;
  - nothing PROVED about N5′-xi on Γ3(G). RESULTS R118 (k) REACH3-CYC (PROVED-CONDITIONAL there) and (l) Corollary T3 say that N5′-xi
    from S3 on Γ3(G) makes Howard steps at the movers until its first fallback, at iteration T3 + 1, where T3 is the Howard count ON Γ3,
    and that «§4 applies on Γ3». This packet is proved on IDEAL-CYC = Γ(G), not on Γ3(G). READING (not claimed): its proofs use CN2,
    LOC-GATE and E-DOM, which should transfer to Γ3 (pads have priority ≤ 2 and are never cycle nodes or in a P-set, R117 PAD); if they
    do, UP-T would bound T3, i.e. the iteration of N5′-xi's first fallback in the sense of L-SI's P-ACYC (Corollary ACYC-XI: «the first
    fallback of N5′-xi on Γ3(G) from S3, i.e. the least iteration k at which SPEC S4c applies, comes at k = T3 + 1», claude/l-si
    e3ac4b06, not landed). Nothing is claimed about iterations after the first fallback;
  - P-ACYC already gives T ≤ N on Ξ-ACYCLIC genomes (there R = C = 0); UP-T is new only on Ξ-cyclic genomes.

## To sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | Lemma CN2 | PROVED | every genome, every positional pair |
| §3 | Lemma LOC-GATE; Lemma LOC-K2 | PROVED | every genome, every state of IDEAL-CYC |
| §4 | Theorem QUIET; Corollary T-QUIET | PROVED | every genome |
| §5 | Corollary UP-T | PROVED | under HYPOTHESIS [E-LEV]; premise P-N5-ASC (R121 when landed) |
| §5 | Corollary ASC-T | PROVED | premise P-N5-ASC (R121 when landed); hypothesis on every vertex's plays |
| §6 | Consequence OVT-DV without [LOC] | READING (not to sign; L-RED's lemma) | |
| §7-§9 | DATA, machine checks, TARGET diff | DATA / READING (not to sign) | |

## 1. Premises (landed R-ids, quoted by script from trunk claude/vibrant-johnson-nxvvxo bf6ced60, docs/RESULTS.md, line numbers there)
- [DEF] RESULTS R104 (l. 9864), definitions of the genome and of Γ(G) only:
  - «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»;
  - «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone»;
  - «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»;
  - «an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»;
  - «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»;
  - «with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2».
  - Used shape, from the frozen packet R118 cites (P-N5-XICYC §1 l. 39, sha1 149e2414): «movers (Even, priority 0) → gates (Odd,
    priority 1) → {e-face e_g, β-face β_g}». Consequence used (E-DOM, P-N5-ASC §3): every vertex more relevant than some e-vertex is an
    e-vertex, c_W, K0 or K3.
- [XICYC] RESULTS R118 (l. 13607):
  - header: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)»;
  - (a) (l. 13677): «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates
    and K2).»; Howard step «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a successor»;
    «T_CYC := the number of steps to the first state where no mover has a strictly better successor»;
  - (b) (l. 13682): «Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′». Used: F1 «Ω_t ⊴ Ω_(t+1) pointwise, for every step t.»; F2 (rewards
    of distinct cycle nodes); F3 «Ω_t(v) = ext(v, Ω_t(nx_t(v)))» when Λ_t(v) ≠ v, «ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more relevant
    than Λ}, k + 1)» (P-N5-XICYC l. 69-74); F4′ «if v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B), and A ◁ B ⇒ ext(v, A) ◁ ext(v,
    B).» (only this clause is used);
  - (c) (l. 13686): DOM «For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).»; STRICT «If σ_(t+1)(x) ≠ σ_t(x),
    then Ω_(t+1)(x) ▷ Ω_t(x).»;
  - (e) (l. 13691): «C ≤ n·(2M + 2).», with its reason «(each vertex's Λ moves only to a vertex of strictly larger reward among at most
    2M + 3 possible cycle nodes)».
- [VJ] order, as in R118's premise (P-N5-XICYC §1 l. 31-33): «first the reward of Λ (an even priority p gives +p, an odd one −p, with
  priorities made injective by rank); then Π, decided by the most relevant vertex of the symmetric difference, which is better for Even
  iff it is even and in the larger set; then k, where a longer prefix is worse for Even if Λ is even and better if Λ is odd».
- [OPT] σ̄_t is optimal at every vertex at once against σ_t: for every positional Odd strategy τ of IDEAL-CYC(G) and every vertex v,
  Ω_t(v) ⊴ the value of v's play under (σ_t, τ). Incorporation path: R118 (b) signs F1-F6 «(§3 l. 68-83)» of its frozen packet; F3's proof
  there, l. 75, reads «σ̄_t is optimal at every vertex at once ([VJ])». The same fact is RESULTS R21 (a)'s parenthetical «(Odd's best reply
  σ̄_k is pointwise optimal in G_{σ_k})» (l. 933).
- [ASC] (only for §5) P-N5-ASC (docs/new/P-N5-ASC.md, frozen, with fixes entry 1 and line L-1), to land as RESULTS R121 BEFORE this
  packet: Corollary HUB-ASC-G's whole-run form «D_E(v) ≤ (2M + 3)·F′_B(M)» when every seq_t(v) has at most B ascents, and Corollary UP-B
  under [E-LEV]: every seq_t(v) has at most U(G) ascents.
- HYPOTHESIS [E-LEV] (only for §5 UP-T): lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)). Incorporation path (Lead reading 23:54Z,
  for the referees to accept or reject): R104 (vi) (l. 10085) «leaves the β-vertex order and the exact e-priorities to packet §3.1»; that
  frozen packet (docs/red/P-N5-REALIZE.md l. 88) reads «Ω(e_g) := eb + 2·i, eb := the least even number > bmax, i := the position of g in
  the order by (lev(owner), gate index)», which is [E-LEV]. If the referees do not accept the path, UP-T holds under [E-LEV] as a
  hypothesis. [E-LEV] is necessary for UP-B (P-N5-ASC fixes entry 1, W-1).
- Not used: [LOC] (LOC-GATE proves it), OVT-DV, IN-BOUND, F4 as printed, F4′'s extra clause of the XICYC fixes file, F5, F6, BR-SEG,
  PATH, any L-RED lane lemma. QUIET and T-QUIET do not use [E-LEV] or [ASC].

## 2. Lemma CN2 (PROVED)
For every genome G, every positional pair of IDEAL-CYC(G) and every vertex v, the cycle node of v's play has priority ≥ 2. So no gate
(priority 1) and no mover (priority 0) is ever a cycle node, and no gate or mover is ever in a set Π.
Proof.
- A cycle containing a mover contains its successor, a gate ([DEF] used shape). A cycle containing a gate contains one of its two
  successors, a face, of priority ≥ 6 ([DEF]). A cycle with neither consists of vertices of priority ≥ 2 (every vertex other than movers
  and gates has priority ≥ 2 by [DEF]). So the cycle's most relevant vertex has priority ≥ 2.
- Π holds only vertices more relevant than the cycle node ([VJ]). ∎

## 3. Lemmas LOC-GATE and LOC-K2 (PROVED)
**Lemma LOC-GATE.** Let G be any genome, t a state of a run of IDEAL-CYC(G), g a gate, a := σ̄_t(g), b := its other face, Ω := Ω_t.
If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).
Proof. Suppose Ω(b) ◁ Ω(a). Let τ := σ̄_t with g switched to b, a positional Odd strategy ([XICYC] (a)). Write val_τ(g) for the value of
g's play under (σ_t, τ). By [OPT], Ω(g) ⊴ val_τ(g). We show val_τ(g) ◁ Ω(g), a contradiction. Ω(g) = ext(g, Ω(a)) by F3 (g is not its
cycle node, CN2).
- Case 1: b's play under (σ_t, σ̄_t) does not visit g. τ agrees with σ̄_t off g, so g's play under τ is g followed by b's play, and
  val_τ(g) = ext(g, Ω(b)) ([VJ], CN2). g ∉ Π(Ω(a)) ∪ Π(Ω(b)) (CN2), so F4′ gives ext(g, Ω(b)) ◁ ext(g, Ω(a)) = Ω(g).
- Case 2: b's play visits g: b = z_1, …, z_m, g, … with z_i distinct and ≠ g, P := {z_1, …, z_m}. After g it follows a, so b, g, a end in
  the same cycle; Λ := its cycle node. Under τ, g's play is the cycle C = {g} ∪ P, with cycle node c ∈ P (CN2).
  - 2-i: a's play does not visit g. Then it does not meet P (from any z_i the σ̄-play runs to g). So Π(b) = Π(a) ∪ Rel(P), with Rel(P)
    := the elements of P more relevant than Λ, disjoint from Π(a), and k(b) = k(a) + m + 1.
    - 2-i-a, Rel(P) ≠ ∅: its most relevant element r is the most relevant vertex of P, so c = r. Ω(b) ◁ Ω(a) with equal Λ is decided by
      Π(b) Δ Π(a) = Rel(P), so r is odd ([VJ]); r is more relevant than Λ, so reward(c) = −p(c) < reward(Λ). val_τ(g) ◁ Ω(g).
    - 2-i-b, Rel(P) = ∅: Π(b) = Π(a) and k(b) > k(a), so Ω(b) ◁ Ω(a) means Λ is even ([VJ]); every vertex of C is less relevant than Λ, so
      reward(c) ≤ p(c) < p(Λ). val_τ(g) ◁ Ω(g).
  - 2-ii: a's play visits g. Then g is on the σ̄-cycle Q = (g, a = w_1, …, w_l, g), Λ ∈ Q ∖ {g} (CN2), Π(a) = ∅, k(a) = dist_Q(a, Λ) and
    Ω(g) = (Λ, ∅, k(a) + 1). b's play first meets Q at q (q = g, or q = w_j = z_i and then z_i, …, z_m = w_j, …, w_l). P0 := the part of P
    before q. Then Π(b) = Rel(P0), k(b) = |P0| + dist_Q(q, Λ), and C = {g} ∪ P0 ∪ arc, arc := Q's vertices from q up to (not including) g.
    - 2-ii-a, Rel(P0) ≠ ∅: as in 2-i-a its top r is odd and is the most relevant vertex of C; val_τ(g) ◁ Ω(g).
    - 2-ii-b, Rel(P0) = ∅, Λ ∈ arc: c = Λ and val_τ(g) = (Λ, ∅, k(b) + 1); against Ω(g) = (Λ, ∅, k(a) + 1) this is the comparison of Ω(b)
      with Ω(a), so val_τ(g) ◁ Ω(g).
    - 2-ii-c, Rel(P0) = ∅, Λ ∉ arc: the path from q to Λ along Q passes g and a, so k(b) > k(a) with Π(b) = Π(a) = ∅; Ω(b) ◁ Ω(a) means Λ
      is even; every vertex of C is less relevant than Λ; val_τ(g) ◁ Ω(g). ∎

**Lemma LOC-K2.** At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).
Proof. K1 is frozen at K1 → K1 ([DEF] start, [XICYC] (a)), so Ω(K1) = (K1, ∅, 0), reward −5. If σ̄_t(K2) = K2, K2's value is (K2, ∅, 0),
reward −3; switching K2 to K1 gives reward −5 < −3, against [OPT]. So σ̄_t(K2) = K1, Ω(K2) = (K1, ∅, 1) (F3), and with Λ = K1 odd and equal
Π the longer prefix is better for Even: Ω(K1) ◁ Ω(K2). ∎

## 4. Theorem QUIET and Corollary T-QUIET (PROVED)
Definitions. class_t(v) := (Λ_t(v), E_t(v)), E_t(v) := the e-vertices of Π_t(v). A step t → t+1 is LOUD if some vertex changes class,
else QUIET; Q := the number of loud steps; a quiet window is a maximal interval [a, b] of states whose steps are all quiet.
D^tot_E(v) := the number of distinct classes of v over the run. A class (w, S) is a B-class if w is less relevant than every e-vertex,
else an E-class.
Facts used.
- (F-cls) The order compares reward(Λ), then E (the top layer of Π below the common K0, K3: E-MON's proof, P-N5-ASC §3), then the rest.
  So each class is a convex set of values, by F1 each vertex is in each class during one interval of states, distinct classes compare
  the same way at all times, and Q ≤ Σ_v (D^tot_E(v) − 1).
- (F-E) An E-class has w an e-vertex or c_W ([DEF], E-DOM; K0, K3 are never cycle nodes: K0 → K3 → K2 are frozen and nothing returns to
  K0).

**Theorem QUIET.** Every quiet window has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps (n = N + 3M + 6).
**Corollary T-QUIET.** T ≤ Q + (Q + 1)·L ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1).
Proof of QUIET. Fix a quiet window [a, b]; every vertex keeps its class on [a, b].
- (Q1) If a gate's two faces are in different classes, their order is fixed on [a, b] (F-cls), so σ̄_t(g) is constant (LOC-GATE).
- (Q2) For a mover x and a step t → t+1 in [a, b], ext at x and at a gate changes neither Λ nor E (CN2), so x's chosen option's gate value
  lies in class(x); and at a state t < b no option of x has a gate value in a class above class(x) (by DOM x's value at t+1 would lie in
  that class).
- (Q3) E-class vertices: if class(v) = (w, S) is an E-class, Π_t(v) = S on [a, b] (only e-vertices, c_W, K0, K3 are more relevant than
  w; c_W is never in Π; K0, K3 lie only on plays with cycle node K1 or K2). So Ω_t(v) = (w, S, k_t); by F1 k_t is monotone with values in
  {0, …, n − 1}: at most n − 1 changes.
- (Q4) B-class structure. Let C = (w, S) be a B-class.
  - A β-face β_g has class(β_g) = class(z), z its frozen successor (β_g ∉ Π(z): if z's play passed β_g it would return to z, putting β_g on
    the cycle).
  - An e-face e_g in C has e_g ∈ S and its W-target y in the B-class (w, S ∖ {e_g}) (every e is more relevant than w; e_g ∉ E(y) likewise).
  - G_C := the movers of class C with their options whose gate's chosen face is in C. A C-mover's play is a simple G_C-path until a
    boundary point: an e-face into a class (w, S ∖ {e}); the exit β → u (constant: the core is frozen and σ̄(K2) = K1 by LOC-K2); or w
    itself, Ω(w) = (w, ∅, 0). (Its cycle has cycle node w, so it cannot close before reaching w.)
- (Q5) B-class stabilisation. For s = 0, …, M let a_s := a + (s + 1)(2M + 1)(N + 1). Claim: every vertex of a B-class (w, S) with
  |S| = s is constant on [min(a_s, b), b].
  - Assume it for s − 1. Fix C = (w, S), |S| = s. After a_(s−1) (after a if s = 0) every boundary value of C is constant.
  - A gate with both faces in C has its e-face in C, of constant value ext(e, Ω(y)) after a_(s−1), while its β-face's value only rises
    (F1). By LOC-GATE it flips at most twice after a_(s−1) (to a tie, then to e). Gates with faces in different classes do not flip (Q1).
    So after a_(s−1) G_C and its chosen faces change at most 2M times: at most 2M + 1 sub-windows.
  - In a sub-window from c with G_C fixed, let opt(x) := the ⊴-largest value of a simple G_C-path from x to a boundary point (constant).
    Upper bound: Ω_t(x) ⊴ opt(x) (Q4). Lower bound (Bellman-Ford): Ω_(c+h)(x) ⊵ the value of every such path with at most h movers, by
    induction on h with DOM at x, F3 at the gate and the face, F1 and F4′ (x and the gate are in no Π by CN2; the face is in neither Π, by
    (Q4)'s argument and simplicity). Simple G_C-paths have at most N movers, so Ω_t(x) = opt(x) for t ≥ c + N, and every C-vertex is then
    constant (non-movers by F3).
  - A sub-window ends only at a flip, which needs a β-face change, i.e. a C-value change. So each sub-window after the first starts
    within N + 1 steps of the previous one, and C is constant from a_(s−1) + (2M + 1)(N + 1) = a_s on. ∎ (claim)
- (Q6) |S| ≤ M, so every B-class vertex is constant from a_M. Each step changes σ at some mover, whose value strictly rises (STRICT);
  after a_M that mover is in an E-class, and by (Q3) E-class movers change at most N(n − 1) times in all. So b − a ≤ L. ∎
Proof of T-QUIET. Steps are loud or quiet; quiet steps form at most Q + 1 windows of at most L steps each; Q ≤ Σ_v (D^tot_E(v) − 1). ∎

## 5. Corollaries UP-T and ASC-T (PROVED)
**Corollary UP-T (under [E-LEV]).** For every genome G, T ≤ (1 + n·((2M + 3)·F′_(U(G))(M) − 1))·(L + 1), with F′ as in P-N5-ASC §5. For
genomes with U(G) ≤ B, B fixed, this is a polynomial in N + M.
Proof. [ASC] UP-B: every seq_t(v) has at most U(G) ascents; HUB-ASC-G's whole-run form: D^tot_E(v) = D_E(v) ≤ (2M + 3)·F′_(U(G))(M) for
every vertex v (D_E(v) of P-N5-ASC fixes entry 1 / L-1 = the number of distinct (Λ_t(v), E_t(v)) = D^tot_E(v)). Then T-QUIET over n
vertices. F′_B has degree 5·2^B − 3 in M (P-N5-ASC §4). ∎
**Corollary ASC-T.** If for every vertex v every seq_t(v) has at most B ascents, T ≤ (1 + n·((2M + 3)·F′_B(M) − 1))·(L + 1). (Same proof
with HUB-ASC-G; no [E-LEV].) ∎

## 6. READING (not to sign): OVT-DV without [LOC]
L-RED's Lemma OVT-DV (R217 §2, PROVED-CONDITIONAL on [LOC]; not landed) uses [LOC] only as «with no tie, σ̄_t(g) is the face of
⊴-smaller value», which is LOC-GATE. T-QUIET does not use OVT-DV.

## 7. DATA (not to sign; tools in experiments/new/box194/, run by check194.sh, output check194.out)
- LOC-GATE: locfail 0 in 66,950 + 380 + 13,980 + 68,549 = 149,859 (gate, state) pairs with no tie (ties 0 everywhere).
  Set: L-RED's LEAP_k64 (66,950) and rd3_d4 (380) (claude/l-red d1a11af6; box194/inst/, sha1 = L-RED's SHA1SUMS), the 13 instances of
  P-N5-ASC (13,980 in all, per-instance in check194.out), 1,000 random genomes (rand191.rgen, seed 2; 68,549). Tool loc194.py.
- LOC-K2: k2fail 0 in every state of the same runs (unit: states). CN2: cnlow 0 (unit: (state, vertex) pairs). Same sets and tool.
- QUIET: wfail 0 (unit: quiet windows), crossflip 0 (unit: σ̄ flips on quiet steps at gates whose faces are in different classes,
  (Q1)), longest window W ≤ N on every run: rd3_d4 2 (N 8), the 8 box 193 instances ≤ 8 (RS2_L8M6, N 29), rd2_d9 0, rd2_d10 3,
  RS2_L32M6 32 (N 77; generated by L-RED's rs2.py 32 6 at d1a11af6, box194/inst/), 1,000 random genomes max W/N 1.0. Tool quiet194.py.
- T-QUIET: Tfail 0 (unit: runs with T > Q + (Q + 1)L). Same sets.
- UP-T, ASC-T: no separate DATA (they are UP-B / HUB-ASC-G plus T-QUIET).
- Context, not a clause: the bound L is far from tight (L ≥ 8,334 on every named instance; W ≤ 32).

## 8. Machine checks
- check.sh block «BOX 194 LOC» re-runs check194.sh and diffs it against check194.out (loc194.py, quiet194.py, in194.py, inst/).
- check.sh block «P-N5-QUIET»: sha1 of this packet and of every tool and instance it cites, against experiments/new/box194/quiet.pins.
- §1's quotes: experiments/new/box194/quotes194.py (record tool; needs git objects, so not in check.sh), output quotes194.out:
  «quotes 27 missing 0 (trunk bf6ced60)».

## 9. TARGET.md diff and limits
- TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game; §4: a bound on a restricted class is not M4. This packet
  bounds one count (Howard's T_CYC) in one restricted model (IDEAL-CYC of R104 genomes); UP-T and ASC-T are polynomial only under a
  hypothesis on the genome ([E-LEV] and bounded U(G)) or on its runs (bounded ascents). Not M3, not M4, not a step-4 pass.
- Limits: L is far from tight; F′_B is super-polynomial when B grows like log M; nothing on Γ3 or N5 is proved (Scope).
