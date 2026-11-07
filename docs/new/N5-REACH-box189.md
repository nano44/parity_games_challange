# Box 189 REACH: does N5 from its default start S3 reach the IDEAL run of R104's Γ(G)? (L-NEW successor 58, Opus 5.5, D1/D14/D18)
Written 2026-11-07 (date -u at commit). Lead brief 2026-11-07 (BOX 189, 12 h). Labels: PROVED (lane) = proof here, unrefereed;
CONJECTURE (data); DEAD (instance); DATA. Nothing here is a TARGET.md claim, M3, or a step-4 pass. G-N5-TIME stays OPEN.

## 0. Answer in four lines
- On R104's Γ(G) itself: NO. N5 from S3 never visits a standard state (Theorem NO-REACH, PROVED (lane), every genome). On all 14 corpus
  genomes (towers and kill instances, L(G) 9 to 59) and 440 random acyclic genomes it stops after ONE iteration (DATA).
- Obstruction: S3's best-reward rule plays K1 → K0 and K0 → K1, which closes the top even cycle at u at state 0. Ξσ is pointwise
  monotone along every N5 run (RESULTS R15 (a), (d)), so the core can never return to R104's stuck configuration (K0 → K3, K1 → K1).
- Modification: YES. Subdividing selected edges by single-successor Even pads of priority ≤ 2 gives Γ3(G) on n = N + 7M + 10 vertices
  whose S3 start pair IS R104's stated start (transported). On Γ3(G) the N5 run FROM S3 contains one FL run of length exactly L(G),
  with the IDEAL states at the movers (Theorem REACH3, PROVED (lane), on R104's premises). DATA: 14/14 corpus genomes, 440/440 random,
  two N5 engines, Oink.
- Consequence (Corollary REAL-IDEAL-S3, PROVED (lane)): R104's caveat «nothing about N5's default start S3» is removed. If N5 as
  specified (from S3) makes at most p(n) iterations on every n-vertex game, then L(G) ≤ p(N + 7M + 10) for every IDEAL-ACYC genome. So
  if towers extend with S(h) polynomial (L-LOWER 3 / L-SI 41 / L-RED 52), N5 itself is super-polynomial and G-N5-TIME is false for N5.

## 1. Setting and premises (sources opened: §8)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md «SPEC (EXACT)», with FIX 1-4, Q1-Q4). S3 / FIX 1: Even v takes the successor w maximising
  (r(w), w if r(w) even else −w), r(w) = Ω(w) if even else −Ω(w) (highest even priority, else lowest odd; ties: largest index for even,
  smallest for odd). Odd v, in G's terms: highest ODD Ω(w), else lowest EVEN Ω(w) (ties: largest index if odd, smallest if even).
- Γ(G), standard states, the IDEAL model, L(G), FL run: as in RESULTS R104 and its packet P-N5-REALIZE (l-red docs/red/P-N5-REALIZE.md,
  sha1 067f06b6, with fixes entries 1-3). Vertex names: movers x, gates g = (x, k), β_g, e_g, c_X, c_W, core K0 = u, K1, K2, K3.
- [MONO] RESULTS R15 (a) (VJ00 Lemma 5.7 as signed: «for any non-empty unambiguous set I of improvements of σ, Ωσ ⊴ Ω_{Switch_I(σ)}»)
  and R15 (d) («N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ … and/or … to Odd's τ»). So for every N5 run and
  every vertex v, Ξσ_j(v) is non-decreasing in j (⊴ is VJ00's order, the same as SPEC S1's; σ is unchanged at τ-only iterations).
- For Theorem REACH3: R104's premises, as restated in P-N5-REALIZE fixes entries 1-3: [SPEC], [1E-N3] (R57 (b), forms P1 and P2),
  [VJ-LOC] (as restated in entry 3: RESULTS R36 (c) Lemma P1 on G^d), [RULE] (R24 (a) Lemma R + R24 (b) TB steps 1, 3-5).
  Nothing else is used.

## 2. Theorem NO-REACH (PROVED, lane): N5 from S3 never reaches a standard state of Γ(G)
Statement. For EVERY genome G (acyclic or not) and the game Γ(G) of R104 (packet §3.1), let (σ_j, τ_j), j = 0, 1, …, be the N5 run
from S3. Then for every j: (a) σ_j(K0) = K1 and σ_j(K1) = K0; (b) the cycle node of Ξσ_j(K0) is K0; (c) no state (σ_j, τ_j) is
standard (a standard state has σ(K0) = K3, σ(K1) = K1); in particular the run contains no state of R104's Theorem REALIZE for any
mover state s. (d) If G is acyclic: for every j and every vertex v ∉ {K2, K3, c_X}, the cycle node c of Ξσ_j(v) ranks above every
β-vertex, so no β is in the P-set of Ξσ_j(v): Even's valuations never see the β-ranks or β-parities that define the IDEAL Ξ-order.
Proof.
- S3 at K0: successors K1 (Ω 5, odd) and K3 (Ω top + 3, odd: top is even); no even successor, so the lowest odd, K1. S3 at K1:
  successors K0 (Ω top + 2, even) and K1 (Ω 5, odd): the even one, K0. So σ_0(K0) = K1, σ_0(K1) = K0. Both are Even, so the play
  from K0 is K0 → K1 → K0 → … whatever Odd does: Ξσ_0(K0) = (K0, ∅, 0) (K0 has the larger p' on the cycle {K0, K1}).
- (b) By [MONO], Ξσ_j(K0) ⊵ (K0, ∅, 0) for every j. Its reward is ≥ p'(K0) > 0. The only vertex with p' > p'(K0) is K3, which is odd,
  so no cycle node has reward > p'(K0); hence the cycle node of Ξσ_j(K0) is K0 for every j.
- (a) Suppose σ_j(K0) = K3. K3 is Even with successors K1, K2. If σ_j(K3) = K1, the play continues from K1, which is either K1's
  self-loop (cycle node K1, odd) or K1 → K0 → K3 → K1 (cycle node K3, odd). If σ_j(K3) = K2, Odd at K2 can stay on K2's self-loop
  (cycle node K2, odd), and σ̄ is optimal for Odd, so Ξσ_j(K0) has reward ≤ the reward of that play < 0. Every case has a negative reward,
  contradicting (b). So σ_j(K0) = K1. If σ_j(K1) = K1, the play from K0 is K0 → K1 → K1 (cycle node K1, odd): again a contradiction. So
  σ_j(K1) = K0.
- (c) is (a).
- (d) Under σ_j, K is entered only at u = K0 (K is closed and β → u is the only edge into it), and K0 → K1 → K0 is fixed, so K3 and K2
  are unreachable from outside K. Every cycle of the graph G_(σ_j) (Even fixed, Odd free) outside K and other than the loops of c_W,
  c_X contains an e-vertex: without e-vertices it would use only edges mover → gate, gate → β, β → mover (β → u enters the closed K),
  i.e. it would be a cycle of the Ξ-graph, excluded by acyclicity. So the cycle node of every play from v ∉ {K2, K3, c_X} is K0, c_W or an e-vertex,
  and each of these outranks every β (Ω(β) ≤ bmax < Ω(e) < top < top + 2). P-sets hold only vertices ranked above the cycle node. ∎
- Scope: (d) concerns Ξσ only. The τ-side and the full run being independent of (br, bp) is DATA (BLIND, §5), not proved.

## 3. The S3-padded game Γ3(G) (experiments/new/box189/gamma3.py, build(G, {"K", "pe", "pb", "m"}))
Γ3(G) is Γ(G) with these edges subdivided by single-successor EVEN pads (a → b becomes a → p → b). Γ's vertices keep their indices,
priorities and owners. Pads are appended in the order pA, s, q, r, pe (gate-index order), pβ (gate-index order), pb (option order),
m (gate-index order):
- core: pA (Ω 0) on K0 → K3; s (Ω 0) on the self-loop of K1 (K1 → s → K1); q (Ω 1) on K1 → K0; r (Ω 0) on K2 → K1;
- gates: pe_g (Ω 1) on g → e_g and pβ_g (Ω 0) on g → β_g (both faces padded once);
- escapes: pb_g (Ω 1) on β_g → u (also when xt(g) = X);
- movers: m_(x,k) on x → (x, k), Ω 2 if k = start(x), else Ω 0.
The priority top of c_W is unchanged (pads ≤ 2). Size: n3 = N + 3M + 6 + (4 + 2M + M + M) = N + 7M + 10; edges 6M + 10 + 4M + 4 =
at most 10M + 14 (one more edge per pad); max Ω unchanged (≤ 4M + 9). Polynomial in N + M at bit cost (TARGET.md §3).
Transport. Every pad has one successor, so strategies of Γ and of Γ3 correspond one to one (a choice a → b of Γ is a → p(a, b) when
the edge is padded); plays correspond with pads inserted. The STANDARD STATE of Γ3 for s is the transport of R104's (σ^s, τ_0): movers
→ m_(x,s(x)), β_g → xt(g) (β → pb_g if xt = X), K0 → pA, K1 → s, K3 → K2, Odd: g → pe_g, K2 → K2.

### 3.1 Lemma S3-START (PROVED, lane)
S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.
Proof (FIX 1 vertex by vertex; single-successor vertices are forced). Movers: successors are the pads m_(x,k), all even, and the
highest Ω is the unique Ω-2 pad, the start's. β_g with xt(g) a mover: {xt (Ω 0, even), pb_g (Ω 1, odd)}: the even one, xt. K0:
{K1 (Ω 5 odd), pA (Ω 0 even)}: pA. K1: {q (Ω 1 odd), s (Ω 0 even)}: s. K3: {K1 (5), K2 (3)}, both odd: the lowest, K2. Odd gate g:
{pe_g (Ω 1 odd), pβ_g (Ω 0 even)}: the highest odd, pe_g. Odd K2: {r (Ω 0 even), K2 (Ω 3 odd)}: K2. ∎

### 3.2 Lemma PAD (PROVED, lane; any genome)
(a) Every cycle of Γ3 other than c_X's self-loop contains a vertex of Ω ≥ 3. (b) Hence for every vertex v ≠ c_X and every strategy
pair, the cycle node c of v's play has Ω(c) ≥ 3 > Ω(p) for every pad p: no pad is ever a cycle node or in a P-set. (c) Hence the play
value of v ∈ V(Γ) in Γ3 is (c, P, ℓ + π), where (c, P, ℓ) is the value of the transported play in Γ and π is the number of pads before
c; a pad's value is p ⊕ (value of its successor). Two Γ3 values compare as the Γ values whenever their (c, P) differ; only where (c, P)
agree do the padded lengths decide.
Proof. (a) A pad's successor is a vertex of Γ, so every cycle contains Γ-vertices. Inside K ∪ {pA, s, q, r} every cycle contains K0, K1
or K3 (the successors of the pads), with Ω ≥ 5. Outside K, a cycle through a mover passes a gate, and a gate's successors are pe_g → e_g
and pβ_g → β_g, with Ω(e), Ω(β) ≥ 6. A cycle made only of gates, movers and pads is impossible (a gate leads to e or β). c_X has no
in-edge but its own loop. (b) follows (and ranks tie-break by index only within equal Ω). (c) ⊕ adds v to P only if p'(v) > p'(c). ∎

### 3.3 Lemma-by-lemma transfer of R104 (PROVED, lane): every place where lengths or vertex indices decide
By PAD (c), each lemma of P-N5-REALIZE §3 transfers verbatim wherever its comparisons are decided by the cycle node or the P-set. The
places where lengths or index sequences decide are re-checked here; the rest is unchanged.
- K3 (Lemma K). (a) Under the standard σ and Odd's σ̄: K1 ↦ (K1, ∅, 0), s ↦ (K1, ∅, 1), r ↦ (K1, ∅, 1), K2 ↦ (K1, ∅, 2) with
  σ̄(K2) = r (the more relevant odd node K1 is better for Odd than K2's loop), K3 ↦ (K1, {K3}, 3), pA ↦ (K1, {K3}, 4),
  K0 ↦ (K1, {K0, K3}, 5), q ↦ (K1, {K0, K3}, 6). (b) Iσ on the core = {(K0, K1)}: K0: K1 vs pA, symmetric difference {K3} (odd), K1
  better: improving. K1: q vs s, difference {K0, K3}, top K3 odd, q worse: not improving. K3: K1 (K1, ∅, 0) vs K2 (K1, ∅, 2), LENGTH
  decides: c = K1 is odd, longer is better for Even, so K2 stays (Γ: lengths 0 vs 1, the same direction). (c) Iτ on the core = ∅:
  Ξτ(K2) = (K2, ∅, 0) (τ(K2) = K2), reward < 0; from r, Even can play r → K1 → q → K0 → K1 …, cycle node K0 (top + 2): reward > 0;
  τ̄ maximises Γ's order (Fact DUAL), so r is worse for Odd. (d) S4a's arena H keeps K0 → {pA, K1}, K1 → {s}, K3 → {K2}, K2 → K2:
  K0 → K1 → s → K1 (node K1) vs K0 → pA → K3 → K2 → K2 (node K2): REWARD decides (−p'(K2) > −p'(K1)), pA; K0 lies on no cycle of
  H, so the pointwise optimum keeps σ on the core.
- PLAY3 / SBAR3. ρ := pβ_g at gates, r at K2. Plays from β_g follow the X-chain with pads inserted and end K0 → pA → K3 → K2 → r → K1
  → s → K1: φ(β_g) = (K1, B(g) ∪ {K0, K3}, ·). At a gate, pe_g vs pβ_g: lev ≥ 1, the P-sets differ by e_g (even, above every β), so
  pe is better for Even; lev 0, c_W vs K1 by reward. At K2: r vs the loop K2, with φ(K2) = (K1, ∅, 2) ⊳ φ(r) = (K1, ∅, 1): LENGTH
  decides, the loop is worse for Odd (Γ: 1 vs 0, the same direction). SBAR (ii) ([VJ-LOC], entry 3 form) and (iii) (a gate on its own
  cycle has an e cycle node; a pe choice changes c or P) are unchanged.
- TAU3. At a gate: Ξτ(pe_g) has reward p'(c_W) (under τ every gate takes pe, so every play ends at c_W); Ξτ(pβ_g) has reward ≥ p'(K0)
  (Even plays β → pb → u → K1 → q → K0 …). REWARD decides. K2: K3 (c).
- ESC3. β_g: xt (the H-play goes mover → m → gate → pe → e … c_W, even) vs pb → u (odd cycle, K3 (d)): REWARD decides.
- W3. Every H-play and the standard play from a level-ℓ mover is x, m, g, pe, e, (level ℓ − 1), …, c_W, five steps per level:
  W(x) = (c_W, ∅, 5ℓ + 5), W(m) = (c_W, ∅, 5ℓ + 4), W(g) = (c_W, ∅, 5ℓ + 3), W(pe) = 5ℓ + 2, W(e) = 5ℓ + 1, β_g with a mover target:
  5·lev(xt) + 6; none depends on s, on the option, or on the pad's Ω. So W is the same in every standard state; every option m_(x,k) ∈ R(x)
  has W*(x) = x ⊕ W*(m_(x,k)) (TIE(x) = R(x)); no corner (the play from m_(x,k) visits only lower levels before c_W).
- KEY3. (a) R(x) = {m_(x,k) : k ∈ A_s(x)}: Ξσ(m_(x,k)) = (K1, B_s(x, k) ∪ {K0, K3}, ·) and Fact X makes the P-set decide. (b) The play
  from m_(x_ℓ, ·) under (σ', τ_0) read root-first from c_W (c_W excluded) is e_0, pe_0, g_0, m_0, x_0, e_1, pe_1, g_1, m_1, x_1, …,
  e_ℓ, pe_ℓ, g_ℓ, m_ℓ, where block i is determined by g_i (x_i is g_i's owner, m_i its pad). It has length 5ℓ + 4 for every option, so the
  first difference between two options of x is at e_(g_i) vs e_(g'_i) for the least i with g_i ≠ g'_i. e-indices follow gate indices
  (unchanged from Γ, the order fixes entry 2 shows to be substantive), so the κ order is the IDEAL key order under s'.
- REALIZE3. The induction of P-N5-REALIZE §4 runs unchanged with K3, SBAR3, TAU3, ESC3, W3, KEY3. [RULE] applies at every Even vertex
  that is not its own W′-cycle node: at movers as above; pads have one option. At state L the step gives σ_new = σ, τ_new = τ with
  Iσ ∋ (K0, K1), so S4c fires: a fallback.

### 3.4 Theorem REACH3 (PROVED, lane, on R104's premises [SPEC], [1E-N3], [VJ-LOC], [RULE]; [MONO] is not used)
For every G ∈ IDEAL-ACYC, the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the Γ3-standard states of the IDEAL run s_0, …,
s_L; transitions 1, …, L are FL transitions and transition L + 1 is a fallback. So if L(G) ≥ 1, [0, L(G)] is one FL run of length
exactly L(G), and the run makes at least L(G) + 1 iterations. Proof: Lemma S3-START (state 0 is standard) and §3.3. ∎

### 3.5 Corollary REAL-IDEAL-S3 (PROVED, lane, same premises)
(a) If every FL run of N5 from S3 has length ≤ p(n) on every n-vertex parity game (p a nondecreasing polynomial), in particular if
N5 from S3 makes at most p(n) iterations (the G-N5-TIME iteration bound), then L(G) ≤ p(N + 7M + 10) for every G ∈ IDEAL-ACYC.
(b) If (G_i) ⊆ IDEAL-ACYC has L(G_i) super-polynomial in N_i + M_i, then Γ3(G_i) is a family of games of size N_i + 7M_i + 10 on which
N5 AS SPECIFIED (default start S3) makes super-polynomially many iterations: G-N5-TIME is false for N5.
(c) Hence G-N5-TIME ⇒ IDEAL-ACYC-POLY. R104's Corollary REAL-IDEAL needed a stated start; this version does not.
Not claimed: anything for Ξ-cyclic genomes; the converse; that towers extend (S(h) is the question for L-LOWER 3, L-SI 41 and L-RED 52).

## 4. DATA (experiments/new/box189/)
| genome (L-RED r187 out/ A_*, L-LOWER l3 kill/*, normalised by norm.py) | L(G) | Γ: n, N5 from S3 | Γ3: n, S3 = stated, N5 from S3, FL run, movers = IDEAL |
| --- | --- | --- | --- |
| A_d4_W2_k2 | 9 | 62, 1 it | 130, yes, 12 it (1 fb), [0, 9], 0..9 |
| A_d4_W3_k3 | 15 | 126, 1 it | 274, yes, 18 it, [0, 15], 0..15 |
| A_d5_W2_k3 | 13 | 106, 1 it | 230, yes, 16 it, [0, 13], 0..13 |
| A_d6_W2_k2 | 11 | 90, 1 it | 190, yes, 14 it, [0, 11], 0..11 |
| KILL_M2D_d6_mu13 | 13 | 90, 1 it | 190, yes, 16 it, [0, 13], 0..13 |
| KILL_M2D_d8_mu21 | 24 | 118, 1 it | 250, yes, 27 it, [0, 24], 0..24 |
| REC_d7_mu17 | 17 | 104, 1 it | 220, yes, 20 it, [0, 17], 0..17 |
| REC_d8_mu24 | 25 | 118, 1 it | 250, yes, 28 it, [0, 25], 0..25 |
| REC_d9_mu29 | 31 | 132, 1 it | 280, yes, 34 it, [0, 31], 0..31 |
| REC_d10_mu32 | 33 | 146, 1 it | 310, yes, 36 it, [0, 33], 0..33 |
| REC_d10_tower_mu30 (R113 per-level doubling on 4 levels) | 35 | 146, 1 it | 310, yes, 38 it, [0, 35], 0..35 |
| REC_d11_mu40 | 44 | 160, 1 it | 340, yes, 47 it, [0, 44], 0..44 |
| REC_d12_mu42 | 48 | 174, 1 it | 370, yes, 51 it, [0, 48], 0..48 |
| RECT_d11_T59 | 59 | 160, 1 it | 340, yes, 62 it, [0, 59], 0..59 |
- Every Γ3 run: L(G) + 3 iterations, 1 fallback. Every Γ run from S3: 1 iteration, 0 fallbacks. The Γ run from R104's stated start
  reproduces REALIZE (FL run [0, L(G)]) on the 4 A_* genomes and the 2 L-LOWER genomes run with reach.py (stab.build, L-RED's builder).
- Second engine: L-COMP's n5b.py --mode spec (experiments/n5-second, written from the SPEC text) on all 28 .pg files from its own default
  start: the same iteration and fallback counts. Outputs: experiments/new/check_sol2.py (Oink 8fbf0a7 --zlk + harness/verify.py): 28/28
  «zielonka(oink zlk) OK strategies verified».
- gamma3.build(G, {}) is byte-identical (game and start) to L-RED's stab.build(G, 0, kgad=True, esc=True) on 3 genomes (selftest).
- Random: randtest.py seeds 1-5, 440 IDEAL-ACYC genomes (d ≤ 4, widths ≤ 3, degrees 2-3): Γ3 from S3 = stated start and FL run [0, L]
  with movers = IDEAL 440/440 (L ≤ 3 only: random genomes are short, so this is a weak test); Γ from S3: 1 iteration 440/440.
- BLIND (CONJECTURE, data): the whole N5 run from S3 on Γ(G) is unchanged when (br, bp) is redrawn: 440/440 identical state sequences.
- Pinned (check.sh block «BOX 189 REACH», box189/check189.sh vs box189/reach.out): Γ3 and Γ runs of REC_d10_tower, RECT_d11_T59 and
  KILL_M2D_d6 (normalised genomes in box189/inst/), and the .pg / .start files of the first two regenerated byte-identical.
  Instances: box189/inst/REC_d10_tower_mu30_g3.pg sha1 c6058ce5…, RECT_d11_T59_g3.pg 0825f9d1…; L-LOWER originals
  REC_d10_tower_mu30.json cc94dc9c…, RECT_d11_T59.json 57b6dc80…, KILL_M2D_d6_mu13.json 5301c716… (claude/l-lower 12216a37).

## 5. Side test: is S3 WITHOUT LOSS OF GENERALITY for N5 on every game? (D14; DEAD as stated, CONJECTURE in a weaker form)
- Idea: S3 depends only on the successors' priorities. Shift every priority by +4 and subdivide EVERY edge (a, b) by an Even pad p(a, b)
  (indices in (a, b) order; Ω 2 if a is Even and b = σ0(a), Ω 1 if a is Odd and b = τ0(a), else 0). Then S3's start is the transport of
  (σ0, τ0), pads never enter P-sets, and every length doubles. Conjecture SUBDIV: the N5 run from S3 on G^pad equals the N5 run from
  (σ0, τ0) on G, state for state.
- DEAD as stated (box189/subdiv.py seed 1, 186/200 identical). Smallest instance: n = 3, Ω [3, 3, 1], owners [Odd, Even, Odd], succ
  0 → {1}, 1 → {0, 1, 2}, 2 → {0}, σ0(1) = 1, τ0 = {0: 1, 2: 0}. On G: one iteration, a FALLBACK (S4a keeps the self-loop at 1, the
  fallback takes 1 → 2). On G^pad: one iteration, no fallback (S4a takes p(1, 2) directly). The states agree; the fallback flag differs.
  Obstruction: SPEC FIX 2 (the DFS cycle choice of a cycle node that belongs to the optimiser) scans successors in index order and stops
  at the first successor equal to v. A self-loop is found at depth 1 in G but behind a pad in G^pad, after the DFS has descended
  elsewhere (reading from the trace: in G^pad the DFS from 1 pushes p(1,0), p(1,1), p(1,2), pops p(1,2) first and returns to 1 via
  2 → 0 → 1, so 1's choice is p(1,2)). So the tie-break at a vertex that is its own cycle node is not invariant under subdivision. Other instances differ in
  iteration count by −1 to +2.
- DATA (CONJECTURE SUBDIV-APPROX): |T(G^pad from S3) − T(G from (σ0, τ0))| ≤ 2 on 550 random games (n ≤ 16): histogram −1: 8,
  0: 506, +1: 35, +2: 1. Not used anywhere. Γ3 avoids the obstruction: no mover is its own W′-cycle node (W3), and the only own-cycle-node
  vertex with a choice in H is K1, which has one option (K3 (d)).

## 6. Status and what the fleet gets
- PROVED (lane, unrefereed): NO-REACH (a)-(d); S3-START; PAD; the transfer §3.3; REACH3; REAL-IDEAL-S3.
- CONJECTURE (data): BLIND (full run invariance); SUBDIV-APPROX.
- DEAD: SUBDIV state-for-state (instance §5).
- OPEN: G-N5-TIME. Combined with the tower question: if S(h) is polynomial (towers extend), then REAL-IDEAL-S3 (b) makes G-N5-TIME
  FALSE for N5 from its default start, via the explicit family Γ3(G_h). If towers do not extend, nothing follows here.
- READING (not a theorem): the positive route the brief asked about, a reachability invariant from S3, cannot rescue N5 from the R104
  mechanism, because Γ3 realises that mechanism from S3 at a cost of 4M + 4 extra vertices (REACH3). An S3-based invariant can only
  help on game classes that exclude such pads.
- Suggested next step for the Lead: a referee packet P-N5-REACH (NO-REACH + S3-START + PAD + §3.3 transfer + REACH3 + corollary),
  citing P-N5-REALIZE lemma by lemma. Ready to freeze on request.

## 7. Tools (experiments/new/box189/)
gamma3.py (independent Γ / Γ3 builder; selftest against L-RED's stab.py), run3.py (own IDEAL simulator from R104's text, N5 from S3,
FL runs, mover projection), reach.py (Γ from S3 vs the stated start, with L-RED's builder; needs LRED = a tree with experiments/red/r187
and r178), norm.py (order-preserving relabel of box150-format genomes to packet format), writepg.py, randtest.py, subdiv.py,
check189.sh, reach.out, inst/.

## 8. Sources opened (this box)
- RESULTS R104 (trunk fc665614, docs/RESULTS.md l. 9864, full line); packet P-N5-REALIZE (claude/l-red 55557951,
  docs/red/P-N5-REALIZE.md sha1 067f06b6c67969adf346621b4a92b253491ab2b9: §1-§6 read) and its fixes entries 1-3
  (docs/red/P-N5-REALIZE-fixes.md, same commit).
- RESULTS R15 (l. 624-640): (a) Lemma A (VJ00 BRICS RS-00-48 Lemma 5.7 as signed) and (d).
- SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef…): S1-S5, FIX 1-4.
- L-RED experiments/red/r187/stab.py, ideal.py, r178/fastcyc.py (claude/l-red 55557951); L-LOWER experiments/lower/l3/kill/README.md
  and genomes (claude/l-lower 12216a37). L-COMP experiments/n5-second/n5b.py, README.md (trunk).
