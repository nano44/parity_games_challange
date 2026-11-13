# P-N5-EXP: for every k ≥ 3 the IDEAL genome G_k (rule R, 9k − 16 movers, Ξ-acyclic) has L(G_k) = 2^k − 2 (Theorem EXP-IDEAL); so, by landed R117, N5 from S3 makes at least 2^k − 1 iterations on Γ3(G_k), a game with 135k − 230 vertices (Corollary EXP-N5): a KILL CANDIDATE for candidate N5's gauntlet step 4 (packet for REFEREE and REFEREE-2; lane, UNREFEREED until signed)
L-RED-B successor 5 (session_01V5yGRXFf3kFNfkycCHTnLT; Fable 5.2, xhigh), 2026-11-13, D1 / D18 / D22 / D25; packet name fixed by the
Lead (12:19Z). STATEMENT sent to the Lead 12:41Z before the freeze. Second independent adversary: L-RED's R243 was not read.
- Status: a kill candidate; lane DATA + a lane proof. Nothing here is a result until both referees sign and CHECKER passes it (D1).
- To sign: §2 (Theorem EXP-IDEAL, Corollary EXP-N5), §4 (Lemma MEMBER), §5 (MOVE-2, K1-K4, V0-V4, WIRE), §6 (RESPONSE LEMMA, STABLE),
  §7 (the proofs). To check: §8 (where the start and the orders are used), §9 (DATA reproduction), §10. Not to sign: §9's numbers as
  statements (DATA), §11 (READING).
- Quotes: every guillemet quote that follows a Q-tag (a label in square brackets) is checked verbatim by
  experiments/red-b/b6quote.py, which joins wrapped source lines (white space is normalised on both sides, nothing else) and prints
  the source lines of each quote (output data/b6b/quote.out: source sha1, line numbers, 0 not found). Labels: R104P = trunk
  docs/red/P-N5-REALIZE.md (R104's packet), R117 = trunk docs/RESULTS.md (the entry R117 is its line 13362), TARGET = TARGET.md,
  CLAUDE = CLAUDE.md, GAPS = trunk docs/GAPS.md; trunk = 5d7aab0f.

## 1. Premises (landed, refereed-only; nothing else is used)
- **R104, DEFINITIONS ONLY** (no theorem of R104 is used). The genome:
  [Q R104P §2] «A GENOME G consists of:» «movers x = 0, …, N − 1, each with a level lev(x) ∈ {0, …, d − 1} and options k = 0, …,
  deg(x) − 1; M := Σ_x deg(x);» «per option (x, k): a W-target wt(x, k), which is a mover of level lev(x) − 1 if lev(x) ≥ 1 and
  «none» if lev(x) = 0 (GRADED);» «a Ξ-target xt(x, k) ∈ {movers} ∪ {X}; a β-id b(x, k) (a bijection onto 0..M − 1);» «a gate index
  gate(x, k), a bijection of the options onto 0..M − 1;» «per β-id b: a rank br(b) (a bijection onto 0..M − 1) and a parity bp(b) ∈
  {0, 1};» «a start s_0 (an option per mover).» «The Ξ-GRAPH of G: the digraph on movers with an edge x → xt(x, k) for every option
  with xt(x, k) ≠ X. G is in IDEAL-ACYC iff its Ξ-graph is ACYCLIC (self-loops count as cycles).»
  Values: [Q R104P §2] «The X-CHAIN of a face (x, k) is the sequence of options (x, k) = (x_0, k_0),» «(x_1, k_1), … with x_(i+1) :=
  xt(x_i, k_i) and k_(i+1) := s(x_(i+1)), ending at the first option whose Ξ-target is X» «B_s(x, k) := the set of β-ids of the
  chain.» «(x, k) ▷_s (x, k') iff the β-id of LARGEST rank in B_s(x, k) Δ B_s(x, k') has parity 0 and lies in B_s(x, k), or has
  parity 1 and lies in B_s(x, k'). Lengths never decide.»
  The step: [Q R104P §2] «IDEAL step from s. Availability A_s(x) := {s(x)} ∪ {k : (x, k) ▷_s (x, s(x))}.» «If |A_s(x)| = 1 for every
  x, the run STOPS («opt»).» «Otherwise s' is defined level by level, lev = 0, 1, …: key(x, k) := (gate(x, k)) if lev(x) = 0, and
  key_(s')(wt(x, k), s'(wt(x, k)))» «followed by gate(x, k) otherwise (a tuple of length lev(x) + 1); s'(x) := the k ∈ A_s(x) with
  the lexicographically least key.» «If s' = s, the run STOPS («stuck»).» «Otherwise s → s' is one IDEAL step. L(G) := the number of
  IDEAL steps from s_0»
- **R117, Theorem REACH3 and Corollary REAL-IDEAL-S3** (used only in Corollary EXP-N5, as landed, with their premises):
  [Q R117] «N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1)» «(Theorem REACH3) for every G with an ACYCLIC Ξ-graph,
  the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2» «n = N + 7M + 10) has S3's start pair equal
  to R104's stated start transported through the pads (Lemma S3-START)» «the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to
  the transported REALIZE states of the IDEAL run, transitions 1, …, L(G) are FL transitions and transition L(G) + 1 is a fallback,
  so if L(G) ≥ 1, [0, L(G)] is one FL run of length exactly L(G) and the run makes at least L(G) + 1 iterations» «(Corollary
  REAL-IDEAL-S3) if every FL run of N5 from S3 on every n-vertex game has length at most p(n) for a nondecreasing polynomial p (in
  particular if N5 from S3 makes at most p(n) iterations), then L(G) ≤ p(N + 7M + 10) for every acyclic G, and a family of acyclic
  genomes with L super-polynomial in N + M would give games on which N5 from its default start makes super-polynomially many
  iterations»
- NOT used: R105, R113, R120. R120's MOVE is stated on 𝓛^R_d and G_k is not in 𝓛^R_d (its levels have up to 9 movers); §5's Lemma
  MOVE-2 is proved from R104's step definition for any mover with two options.

## 2. Statement
**Theorem EXP-IDEAL.** For every integer k ≥ 3 let G_k be the genome built by rule R (§3; generator experiments/red-b/gk.py,
build(k)). Then
 (a) G_k is a genome in the sense of R104 and is in IDEAL-ACYC, with N = 9k − 16 movers, M = 2N = 18k − 32 options (every mover has
     exactly two options) and d = k + 1 levels;
 (b) L(G_k) = 2^k − 2 (R104's L: the number of IDEAL steps from s_0), and the run ends by the clause «stuck» (s′ = s with a
     non-singleton availability set);
 (c) in that run every mover of unit j (u_j, v_j, e_j, y_j, ȳ_j, y′_j, ȳ′_j; 1 ≤ j ≤ k − 1, those that exist) changes its option
     exactly 2^(j−1) times, v_0 once, u_0 and the wires never; so the largest count is 2^(k−2) (unit k − 1) and the total number of
     option changes is 1 + Σ_j 2^(j−1)·|unit j| = 7·2^(k−2) + 4·2^(k−2) − 9 = 11·2^(k−2) − 9.
**Corollary EXP-N5** (by R117's Theorem REACH3 only). For every k ≥ 3, Γ3(G_k) is a parity game with n = N + 7M + 10 = 135k − 230
vertices and m = 176k − 300 edges, and the N5 run of Γ3(G_k) from S3 (R117's N5 and S3, quoted in §1) has an FL run of length
exactly 2^k − 2 and makes at least 2^k − 1 = 2^((n + 230)/135) − 1 iterations (REACH3's clause «the run makes at least L(G) + 1
iterations»). So no polynomial in n, or in n + m = 311k − 530, bounds the number of iterations of N5 from S3; this is the case R117's
Corollary REAL-IDEAL-S3 names. Cost: TARGET.md §2-§3 count steps of a word RAM, and an iteration costs at least one step, so the
running time of N5 from S3 on Γ3(G_k) is at least 2^k − 1 in TARGET's cost model, on an input of n + m = 311k − 530 vertices and
edges.
**Dead end (wording fixed by the Lead, 12:43Z, C3).** The claim "N5 (SPEC S1-S5, default start S3) runs in polynomial time" is
FALSE. N5 therefore cannot pass gauntlet step 4 (no running-time proof can exist) and is a dead end as an M4 candidate; G-N5-TIME is
answered NO. (Gauntlet step 4: [Q TARGET §5] «4. Written correctness and running-time proofs, double-refereed with every gap
listed.»; [Q CLAUDE] «Every algorithm claim runs the gauntlet in TARGET.md section 5. Failing any step makes it a dead end.»;
G-N5-TIME: [Q GAPS] «N5 SSI-GLOBAL makes polynomially many iterations (gauntlet step 4, running time)».) N5 is CORRECT on these
games (DATA §9.4: every winner equals Zielonka's); what fails is the polynomial bound.
Obstruction: S4a's root-first key rule refuses an improving switch until the key order allows it; on Γ3(G_k) this makes the movers a
ripple counter. Instance: Γ3(G_k), k ≥ 3; files data/b6b/pg/G_k_g3.pg, k = 3..11 (smallest: 175 vertices, 228 edges, 9 iterations).
Beyond explicit bounds (b6size.py, exact integers, §9.5): 2^k − 1 > n² first at k = 23 (n = 2,875), > n³ at k = 37 (n = 4,765),
> n⁴ at k = 51 (n = 6,655); against (n + m)^c: k = 26, 41, 57. For every fixed c the bound 2^k − 1 > (311k − 530)^c holds for all
large k (Corollary EXP-N5).
**Not claimed.** Nothing about N5 from other start pairs; nothing about other tie rules (N5′-xi makes 7 iterations on Γ3(G_4) and
Γ3(G_6), §9.4) or about Howard / switch-best (3 or 4 steps on the model); nothing about any other candidate or about parity games
in general: the target ([Q TARGET §2] «There is a deterministic algorithm A and a polynomial p such that for every parity game G,
A on input G halts within p(n + m) steps and outputs the pair (W_E(G), W_O(G)).») stays open. Not claimed: that 9 movers per level
is least (DATA §9.6: 8 suffice), or anything for k ≤ 2.

## 3. The rule R (k ≥ 3)
Levels 0, …, k. Every mover has two options, numbered 0, 1; every parity bp is 0. «Pair below» of level j ≥ 1: B_(j−1) = (u_(j−1),
v_(j−1)), member 0 = u, member 1 = v. E(j) := e_j for 2 ≤ j ≤ k − 2 and E(k − 1) := u_(k−1) (the END-FOLLOWER of level j).
| mover | level | exists for | W-target of option 0 / 1 | Ξ-target of option 0 / 1 | start | local ε of option 0 / 1 | Ξ-depth | local δ of option 0 / 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| u_0 | 0 | | none / none | X / X | 0 | 2 / 5 | 0 | 2 / 0 |
| v_0 | 0 | | none / none | X / X | 0 | 3 / 1 | 0 | 1 / 3 |
| u_j | j | 1 ≤ j ≤ k − 1 | u_(j−1) / v_(j−1) | ȳ_j / y_j | 0 | 2 / 3 | 2j | 1 / 0 |
| v_j | j | 1 ≤ j ≤ k − 1 | u_(j−1) / v_(j−1) | y_j / ȳ_j | 0 | 4 / 5 | 2j | 3 / 2 |
| e_j | j | 2 ≤ j ≤ k − 2 | u_(j−1) / v_(j−1) | ȳ′_j / y′_j | 0 | 0 / 1 | 2j + 1 | 4 / 5 |
| wv_j (wire) | j + 1 | 1 ≤ j ≤ k − 2 | v_j / v_j | X / X | 0 | 6 / 7 | last | 1 / 0 |
| wu_j (wire) | j + 1 | 2 ≤ j ≤ k − 2 | u_j / u_j | X / X | 0 | 8 / 9 | last | 3 / 2 |
| y_j | j + 2 | 1 ≤ j ≤ k − 2 | wv_j / E(j + 1) | u_(j−1) / v_(j−1) | 0 | 10 / 11 | 2j − 1 | 1 / 3 |
| ȳ_j | j + 2 | 1 ≤ j ≤ k − 2 | wv_j / E(j + 1) | v_(j−1) / u_(j−1) | 1 | 12 / 13 | 2j − 1 | 0 / 2 |
| y_(k−1) | k | | u_(k−1) / v_(k−1) | u_(k−2) / v_(k−2) | 0 | 20 / 21 | 2k − 3 | 1 / 3 |
| ȳ_(k−1) | k | | u_(k−1) / v_(k−1) | v_(k−2) / u_(k−2) | 1 | 22 / 23 | 2k − 3 | 0 / 2 |
| y′_j | j + 2 | 2 ≤ j ≤ k − 2 | wu_j / E(j + 1) | ȳ_j / y_j | 0 | 14 / 15 | 2j | 5 / 7 |
| ȳ′_j | j + 2 | 2 ≤ j ≤ k − 2 | wu_j / E(j + 1) | y_j / ȳ_j | 1 | 16 / 17 | 2j | 4 / 6 |
- gate(x, o) := the rank, among all options of G_k, of the number 100·lev(x) + (local ε of (x, o)) (a bijection onto 0..M − 1; two
  options of one level are ordered by their local ε).
- br of the β of (x, o) := the rank, among all options, of the pair (−depth(x), local δ of (x, o)), a wire counting as depth 2k + 5:
  a β of smaller Ξ-depth outranks every β of larger Ξ-depth («depth-major»); inside one depth the local δ decides. bp = 0.
- β-id of (mover number i, option o) := 2i + o, movers numbered in the generator's order (u_0, v_0, the pairs, the e's, the wv's,
  the wu's, the pairs Y, the pairs Y′). Option 1 of an observer (y, ȳ, y′, ȳ′) is called FORWARD, option 0 BACK.
- Counts: 2 + 2(k − 1) + (k − 3) + (k − 2) + (k − 3) + 2(k − 1) + 2(k − 3) = 9k − 16.

## 4. Lemma MEMBER (Theorem EXP-IDEAL (a))
Each clause of R104's definition (line numbers of P-N5-REALIZE.md §2, printed by b6member.py --quote into data/b6b/member_quote.out):
- c1, l. 53 (movers, levels, options): N = 9k − 16 movers; the levels 0, …, k are all used (level k holds the top observers); every
  mover has two options.
- c2, l. 54 (GRADED): by the table every W-target is one level below its mover (u_j, v_j, e_j at level j point to level j − 1; a
  wire at level j + 1 to level j; an observer at level j + 2 to wv_j, wu_j or E(j + 1), all at level j + 1; the top observers at
  level k to level k − 1); the level-0 movers have none. The clause is per option: it does not ask the two W-targets of a mover to
  differ, so a wire (two options, one W-target) is allowed.
- c3, l. 55 (Ξ-target a mover or X): by the table. There is no level condition on Ξ-targets, so X is allowed at every level (the
  wires, u_0, v_0).
- c4, l. 55 (β-ids a bijection), c5, l. 56 (gates a bijection), c6, l. 57 (ranks a bijection; parities in {0, 1}): by construction
  (β-id 2i + o; gate and br are ranks of injective keys, hence bijections onto 0..M − 1; all parities 0, which l. 57 allows).
- c7, l. 58 (start): the table's start column.
- c8, l. 59-60 (acyclic, no self-loop): every Ξ-edge goes from Ξ-depth D to Ξ-depth D − 1 (u_j, v_j: 2j → 2j − 1; y_j, ȳ_j: 2j − 1 →
  2j − 2; y′_j, ȳ′_j: 2j → 2j − 1; e_j: 2j + 1 → 2j); depth-0 movers and wires have no Ξ-edge. ∎
DATA: b6member.py finds 0 violations on G_3, …, G_14 and each of 8 damaged copies of G_5 violates its clause (§9.1). (History: the
first version of gk.py wrote the numbers 100·level + ε as gates, distinct but not onto 0..M − 1; those RAW files are kept as DATA
only, data/b6b/raw/: same order, hence the same comparisons and the same run; their normalised copies are byte-equal to G_k, §9.1.)

## 5. Two orders, the move rule, and the static facts
For a state s and movers p ≠ q of ONE level: p is KEY-AHEAD of q under s iff key_s(p) < key_s(q), where key_s(x) is the key of x's
current option with s on the lower levels (the definition's key, read with s in place of s′). For two faces: (p, a) is VALUE-AHEAD
of (q, b) under s iff the β of largest rank in B_s(p, a) Δ B_s(q, b) has parity 0 and lies in B_s(p, a), or has parity 1 and lies in
B_s(q, b) (for p = q this is the definition's ▷_s); a mover p is value-ahead of q iff (p, s(p)) is value-ahead of (q, s(q)).
**Lemma MOVE-2.** Let x have exactly two options, o = s(x) and o′. In the IDEAL step s → s′ (definition: «s' is defined level by
level»; «s'(x) := the k ∈ A_s(x) with the lexicographically least key»), s′(x) = o′ iff
 (a) (x, o′) ▷_s (x, o) (x is VALUE-ENABLED under s), and
 (b) key(x, o′) < key(x, o), both keys taken with s′ on the levels below lev(x) (x is KEY-ENABLED in the step).
If wt(x, o) ≠ wt(x, o′), (b) says: wt(x, o′) is key-ahead of wt(x, o) under s′. If wt(x, o) = wt(x, o′), (b) says gate(x, o′) <
gate(x, o).
Proof. A_s(x) is {o}, or {o, o′} iff (a); s′(x) is its key-least element, with the keys of the definition (s′ on the lower levels,
which the step has fixed before it reaches lev(x)). The key of (x, i) is the key of wt(x, i)'s option under s′ followed by gate(x,
i): if the W-targets differ, their keys differ (two movers of one level have keys with different last entries) and decide; if they
are equal, the gates decide. ∎
A run step with s′ ≠ s changes at least one mover; the run stops at the first s with s′ = s.
Throughout the rest of §5, s is any state of G_k with every wire at option 0 (Lemma WIRE: this holds along the run).
**V0 (depth).** The X-chain of a face of a non-wire mover of Ξ-depth D has exactly one option at each depth D, D − 1, …, 0 (table:
every Ξ-target of a mover of depth D ≥ 1 has depth D − 1; depth-0 movers point at X). Let (p, a), (q, b) be faces of non-wire
movers of ONE depth whose chains differ, and let d* be the LEAST depth at which the chains have different options, (x, i) in the
first and (x′, i′) in the second. Then (p, a) is value-ahead of (q, b) iff br(x, i) > br(x′, i′), i.e. iff the local δ of (x, i) is
the larger. If the two chains pass through one mover at some depth, they coincide from that depth down.
Proof. The options of depth < d* are common to both chains (if the chains are at the same mover at some depth they continue
identically, by the chain's definition; so «different options at depth d*» and «same options below» is the only shape), so the
symmetric difference of the two β-sets lies in depths ≥ d*. Its β of largest rank is one of the two β's of depth d* (depth-major
ranks), the one of larger rank; all parities are 0, so the face that contains it is ahead. ∎
Write «split» for s(u_j) ≠ s(v_j) and «aligned» otherwise. By V0 and the table:
- **V1.** E_j(s) := [v_j is value-ahead of u_j] (1 ≤ j ≤ k − 1) is 1 if the pair is split (v_j at o and u_j at 1 − o point at the
  same member of Y_j, so d* = 2j, where δ(v_j, ·) ∈ {3, 2} exceeds δ(u_j, ·) ∈ {1, 0}), and is [EY_j(s) = s(v_j)] if the pair is
  aligned at o (v_j points at member o of Y_j = (y_j, ȳ_j), u_j at member 1 − o; the chains are at different movers at depth 2j − 1,
  so d* ≤ 2j − 1 and the order of the two observers decides). E_0(s) := [v_0 is value-ahead of u_0] = s(v_0) (δ: (v_0, 1): 3 >
  (u_0, 0): 2 > (v_0, 0): 1; u_0 stays at 0 by WIRE).
- **V2.** EY_j(s) := [ȳ_j is value-ahead of y_j] is s(ȳ_j) if s(y_j) ≠ s(ȳ_j) (then both point at the same member of B_(j−1), d* =
  2j − 1, and δ: (y, forward) 3 > (ȳ, forward) 2 > (y, back) 1 > (ȳ, back) 0: the forward one is ahead), and is [s(y_j) ≠
  E_(j−1)(s)] if s(y_j) = s(ȳ_j) = o (y_j points at member o of B_(j−1), ȳ_j at member 1 − o: the one pointing at the value-ahead
  member is ahead).
- **V3.** EY′_j(s) := [ȳ′_j is value-ahead of y′_j] is s(ȳ′_j) if s(y′_j) ≠ s(ȳ′_j) (same member of Y_j; δ: 7 > 6 > 5 > 4, forward
  ahead), and is [1 − s(y′_j) ≠ EY_j(s)] if s(y′_j) = s(ȳ′_j) = o (y′_j points at member 1 − o of Y_j, ȳ′_j at member o).
- **V4 (value-enabling).** Let x be a non-wire mover of depth ≥ 1; its two options have different Ξ-targets p = xt(x, o), p′ =
  xt(x, o′), movers of one depth. The chains of (x, o), (x, o′) are x's option followed by the chains of p, p′; these differ at a
  depth below x's (V0: different movers at depth(x) − 1), so (x, o′) ▷_s (x, o) iff p′ is value-ahead of p. Reading the table:
  v_j at o is value-enabled iff EY_j = 1 − o; u_j at o iff EY_j = o; e_j at o iff EY′_j = o; y_j at back iff E_(j−1) = 1 and at
  forward iff E_(j−1) = 0; ȳ_j at back iff E_(j−1) = 0 and at forward iff E_(j−1) = 1; y′_j at back iff EY_j = 0 and at forward
  iff EY_j = 1; ȳ′_j at back iff EY_j = 1 and at forward iff EY_j = 0. (Depth 0: u_0 at 0 is never value-enabled, δ 2 > 0; v_0 at 0
  is, δ 3 > 1.)
- **K1.** C_j(s) := [v_j is key-ahead of u_j] (1 ≤ j ≤ k − 1) is [s(v_j) = C_(j−1)(s)] if the pair is split (the W-targets are the
  two members of B_(j−1): the member pointing at the key-ahead one is ahead), and 0 if aligned (one W-target; ε(u_j, o) < ε(v_j, o):
  2 < 4, 3 < 5). C_0(s) := [v_0 is key-ahead of u_0] = s(v_0) (ε: (v_0, 1): 1 < (u_0, 0): 2 < (v_0, 0): 3).
- **K2.** D_j(s) := [E(j + 1) is key-ahead of wv_j] = [s(E(j + 1)) = 1] ∨ [C_j(s) = 0] (1 ≤ j ≤ k − 2). Proof: the key of wv_j is
  the key of v_j followed by ε 6. At option 1, E(j + 1) has the key of v_j followed by ε 1 (e) or 3 (u_(k−1)): ahead. At option 0 it
  has the key of u_j followed by its ε, and the keys of u_j, v_j decide: ahead iff u_j is key-ahead of v_j. ∎
- **K3.** Z_j(s) := [E(j + 1) is key-ahead of wu_j] = [s(E(j + 1)) = 0] ∨ [C_j(s) = 1] (2 ≤ j ≤ k − 2): the same with ε(E(j + 1), 0)
  ∈ {0, 2} below ε(wu_j, 0) = 8.
- **K4 (key-enabling).** By MOVE-2 (b), in a step s → s′: u_j, v_j, e_j at o are key-enabled iff o ≠ C_(j−1)(s′); an observer of
  Y_j (1 ≤ j ≤ k − 2) at back iff D_j(s′) = 1 and at forward iff D_j(s′) = 0; an observer of Y_(k−1) at back iff C_(k−1)(s′) = 1 and
  at forward iff C_(k−1)(s′) = 0; an observer of Y′_j at back iff Z_j(s′) = 1 and at forward iff Z_j(s′) = 0. (s′ on the levels
  below the mover; the orders C, D, Z of a level are functions of s′ on that level and below.)
- **Lemma WIRE.** Along the run no wire moves, u_0 never moves, and v_0 moves exactly once, at step 1, from option 0 to option 1.
  Proof. A wire's two options have one W-target, so (MOVE-2) it could move only to an option of smaller gate: ε 6 < 7 and 8 < 9,
  the wire is at option 0 and stays. u_0: ε 2 < 5, the same. v_0 at 0 is value-enabled (V4) and key-enabled (ε 1 < 3): it moves at
  step 1; at option 1 it is never key-enabled again. ∎

## 6. Rest states and the RESPONSE LEMMA
UNIT j (1 ≤ j ≤ k − 1) := {u_j, v_j, y_j, ȳ_j} ∪ {e_j, y′_j, ȳ′_j if 2 ≤ j ≤ k − 2}. Its INPUT under s is the pair of bits
(C_(j−1)(s), E_(j−1)(s)). Unit j is AT REST a (a ∈ {0, 1}) under s, written REST_j(a), iff s(u_j) = s(v_j) = a, s(e_j) = a,
(s(y_j), s(ȳ_j)) = (a, 1 − a) and (s(y′_j), s(ȳ′_j)) = (a, 1 − a) (the conditions on e_j, y′_j, ȳ′_j when these exist).
In REST_j(a): EY_j = 1 − a and EY′_j = 1 − a (V2, V3: the two observers of each pair are on different options; no dependence on
the input), C_j = 0 (K1) and E_j = [1 − a = a] = 0 (V1).
P_(k−1) := 3 and P_j := 2·P_(j+1) + 1 for j < k − 1; so P_j = 2^(k+1−j) − 1.
**RESPONSE LEMMA.** Let 1 ≤ j ≤ k − 1, a ∈ {0, 1}, c := 1 − a, t ≥ 1, and suppose
 (H1) under s_(t−1): REST_j(a), REST_i(0) for every i > j, and the input of unit j is (a, a);
 (H2) the input of unit j is (c, c) under s_τ for every τ with t ≤ τ ≤ t + P_j − 1 that the run reaches.
Let F be the observer of Y_j that is on forward under s_(t−1) and B the other one; F′, B′ the same for Y′_j. Then the run reaches
s_(t+P_j−1) (for j = 1: s_(t+P_1−2)), and in the steps t, t + 1, … the movers of the units j, …, k − 1 move exactly as follows.
 (i) j = k − 1: step t: v_j to c. Step t + 1: B to forward. Step t + 2: u_j to c and F to back. Nothing else.
 (ii) j ≤ k − 2: step t: v_j to c, and unit j + 1 begins a response (from REST_(j+1)(0), to the input (1, 1)). Step t + 1: F to back.
   Step t_1 := t + P_(j+1) − 1: E(j + 1) to 1 (the last step of that response) and B to forward. Step t_1 + 1: u_j to c, F′ to back,
   and unit j + 1 begins a response (from REST_(j+1)(1), to the input (0, 0)). Step t_2 := t_1 + P_(j+1): E(j + 1) to 0 (the last
   step of that response) and B′ to forward. Step t_2 + 1 = t + P_j − 1: e_j to c. For j = 1 there are no e_1, F′, B′, and the last
   step is t_2 = t + P_1 − 2. No mover of unit j moves at any other step; the units above j move only inside the two responses.
In both cases: every step from t to the last one changes some mover; for j ≥ 2, s_τ(E(j)) = a for τ < t + P_j − 1 and E(j) moves to c
at step t + P_j − 1; and under the last state REST_j(c) and REST_i(0) for every i > j hold.
Proof. Downward induction on j; a mover moves in the step s → s′ iff it is value-enabled under s (V4) and key-enabled in the step
(K4) (MOVE-2).
(i) j = k − 1. Under s_(t−1): EY_j = c. Step t: v_j (at a) is key-enabled (C_(j−1)(s_t) = c ≠ a, H2) and value-enabled (EY_j = c =
1 − a): it moves to c. u_j (at a) is not value-enabled (needs EY_j = a). Then C_j(s_t) = 1 (K1: split, s_t(v_j) = c = C_(j−1)(s_t)),
so F (on forward) is not key-enabled (needs C_j = 0); B (on back) is not value-enabled under s_(t−1): B = y_j if a = 0 and needs
E_(j−1) = 1, B = ȳ_j if a = 1 and needs E_(j−1) = 0, i.e. needs E_(j−1) = c, but E_(j−1)(s_(t−1)) = a (H1). Step t + 1: under s_t the
observers are unchanged, so EY_j = c and u_j is still not value-enabled; so C_j(s_(t+1)) = 1; B is value-enabled (E_(j−1)(s_t) = c,
H2) and key-enabled: it moves to forward; F is not key-enabled. Now both observers are on forward and EY_j = [1 ≠ E_(j−1)] = [1 ≠ c]
= a (V2). Step t + 2: u_j is value-enabled (EY_j(s_(t+1)) = a) and key-enabled (at a ≠ c): it moves to c; so C_j(s_(t+2)) = 0
(aligned), F is key-enabled, and F is value-enabled under s_(t+1) (F = ȳ_j if a = 0, on forward, needs E_(j−1) = 1; F = y_j if a =
1 needs E_(j−1) = 0; i.e. E_(j−1) = c): F moves to back. B (on forward) is not value-enabled (B = y_j if a = 0 needs E_(j−1) = 0; B
= ȳ_j if a = 1 needs E_(j−1) = 1; i.e. E_(j−1) = a). v_j is at c, key-disabled, from s_t on. The last state has the pair at c and
(s(y_j), s(ȳ_j)) = (c, 1 − c): REST_j(c). Each of the three steps moved a mover.
(ii) j ≤ k − 2, assuming the lemma for j + 1. Under s_(t−1): EY_j = c, EY′_j = c, C_j = E_j = 0, s(E(j + 1)) = 0 (REST_(j+1)(0)), so
D_j = 1 and Z_j = 1 (K2, K3).
Step t. v_j moves to c as in (i). u_j (needs EY_j = a) and e_j (needs EY′_j = a) are not value-enabled. Hence C_j(s_t) = 1 (K1),
and E_j = 1 under every state in which the pair is split (V1). Unit j + 1 satisfies (H1) at time t with a = 0 (REST_(j+1)(0),
REST_i(0) above, input (C_j, E_j) = (0, 0) under s_(t−1)), and its input is (1, 1) for as long as u_j and v_j do not move and
C_(j−1) = c: v_j is key-disabled (at c = C_(j−1)), and u_j is value-disabled for as long as EY_j = c. The observers in step t: F is
not value-enabled under s_(t−1) (F = ȳ_j if a = 0, on forward, needs E_(j−1) = 1; F = y_j if a = 1 needs E_(j−1) = 0; E_(j−1)(s_(t−1))
= a); B is not key-enabled (D_j(s_t) = [s(E(j + 1)) = 1] ∨ [C_j = 0] = 0: by induction E(j + 1) does not move before step t_1 ≥
t + 2). F′ is not key-enabled (Z_j(s_t) = 1 because s(E(j + 1)) = 0); B′ is not value-enabled (B′ = y′_j if a = 0, on back, needs
EY_j = 0; B′ = ȳ′_j if a = 1 needs EY_j = 1; i.e. EY_j = a, but EY_j = c).
Steps t + 1, …, t_1 − 1. By induction unit j + 1 (and the units above) make exactly the moves of its response in the steps t, …, t_1,
with s(E(j + 1)) = 0 before step t_1, provided its input stays (1, 1), which we check along the way. Step t + 1: F is value-enabled
(E_(j−1)(s_t) = c, H2) and key-enabled (D_j(s_(t+1)) = 0: s(E(j + 1)) = 0, C_j = 1): F moves to back. Both observers of Y_j are now
on back and EY_j = [0 ≠ E_(j−1)] = c (V2): unchanged. Until step t_1: B is not key-enabled (D_j = 0); F (on back) is not
value-enabled (F = ȳ_j if a = 0, on back, needs E_(j−1) = 0; F = y_j if a = 1 needs E_(j−1) = 1; i.e. E_(j−1) = a); so EY_j = c, u_j
does not move, the input of unit j + 1 stays (1, 1); F′ is not key-enabled (Z_j = 1: s(E(j + 1)) = 0); B′ is not value-enabled
(EY_j = c); EY′_j = c (V3, the observers of Y′_j unchanged on different options); e_j does not move.
Step t_1 (≥ t + 2). E(j + 1) moves to 1 (induction), so D_j(s_(t_1)) = 1 (K2); B is value-enabled under s_(t_1−1) (B = y_j if a = 0,
on back, needs E_(j−1) = 1; B = ȳ_j if a = 1 needs E_(j−1) = 0; i.e. E_(j−1) = c, true by H2): B moves to forward. Now (s(y_j),
s(ȳ_j)) = (c, 1 − c) and EY_j = s(ȳ_j) = 1 − c = a (V2). Z_j(s_(t_1)) = [C_j = 1] = 1: F′ does not move; B′ was not value-enabled
under s_(t_1−1). By induction the units j + 1, … are now in REST_(j+1)(1), REST_i(0) above.
Step t_1 + 1. u_j is value-enabled (EY_j(s_(t_1)) = a) and key-enabled (at a ≠ c = C_(j−1)): it moves to c. So the pair is aligned
at c under s_(t_1+1): C_j = 0 (K1) and E_j = [EY_j = c] = 0 (V1), for as long as EY_j = a. Then Z_j(s_(t_1+1)) = [s(E(j + 1)) = 0] ∨
[C_j = 1] = 0: F′ is key-enabled, and F′ is value-enabled under s_(t_1) (F′ = ȳ′_j if a = 0, on forward, needs EY_j = 0; F′ = y′_j if
a = 1 needs EY_j = 1; i.e. EY_j = a): F′ moves to back. B′ (on back) is not key-enabled (Z_j = 0). Both observers of Y′_j are now on
back and EY′_j = [1 − 0 ≠ EY_j] = [1 ≠ a] = c (V3): unchanged; e_j does not move. Y_j: its forward observer B is not value-enabled
(B = y_j if a = 0, on forward, needs E_(j−1) = 0; B = ȳ_j if a = 1 needs E_(j−1) = 1; i.e. E_(j−1) = a) and its back observer F is
not (shown above); this holds at every later step of the response, so Y_j does not move again and EY_j = a from s_(t_1) on. Unit
j + 1 satisfies (H1) at time t_1 + 1 with a = 1 (REST_(j+1)(1), REST_i(0) above, input (1, 1) under s_(t_1)), and its input is (0, 0)
from s_(t_1+1) on, because u_j and v_j are both at c, key-disabled, and EY_j = a.
Steps t_1 + 2, …, t_2 − 1. By induction only the response of unit j + 1 (steps t_1 + 1, …, t_2), with s(E(j + 1)) = 1 before step
t_2: so Z_j = 0 and B′ is not key-enabled; F′ (on back) is not value-enabled (F′ = ȳ′_j if a = 0, on back, needs EY_j = 1; F′ = y′_j
if a = 1 needs EY_j = 0; i.e. EY_j = c); e_j is not value-enabled (EY′_j = c).
Step t_2. E(j + 1) moves to 0 (induction), so Z_j(s_(t_2)) = 1 (K3); B′ is value-enabled under s_(t_2−1) (B′ = y′_j if a = 0, on
back, needs EY_j = 0; B′ = ȳ′_j if a = 1 needs EY_j = 1; i.e. EY_j = a): B′ moves to forward. Now (s(y′_j), s(ȳ′_j)) = (c, 1 − c) and
EY′_j = s(ȳ′_j) = a (V3). For j = 1 (no Y′_1, no e_1) this is the last step.
Step t_2 + 1. e_j is value-enabled (EY′_j(s_(t_2)) = a) and key-enabled (at a ≠ c): it moves to c. No other mover of unit j is
enabled (the pair is key-disabled; Y_j: shown; Y′_j: B′ on forward needs EY_j = c, F′ on back needs EY_j = c), and the units above
are at rest with the unchanged input (0, 0) (STABLE). The state is REST_j(c) with REST_i(0) above, and t_2 + 1 = t + 2·P_(j+1) =
t + P_j − 1. Every step changed a mover: the steps t, …, t_1 and t_1 + 1, …, t_2 by induction, the step t_2 + 1 by e_j. ∎
**STABLE.** If unit i is at rest b and its input is (b, b), no mover of unit i is enabled: u_i, v_i, e_i are at b = C_(i−1)
(key-disabled, K4); Y_i is at (b, 1 − b) and both observers are value-disabled (b = 1: y_i on forward needs E_(i−1) = 0, ȳ_i on back
needs E_(i−1) = 0; b = 0: y_i on back needs E_(i−1) = 1, ȳ_i on forward needs E_(i−1) = 1); Y′_i is at (b, 1 − b) with EY_i = 1 − b
and both observers are value-disabled (b = 1: y′_i on forward needs EY_i = 1, ȳ′_i on back needs EY_i = 1; b = 0: y′_i on back needs
EY_i = 0, ȳ′_i on forward needs EY_i = 0). ∎

## 7. Proofs of the statements
**Theorem EXP-IDEAL.** (a) is Lemma MEMBER and the count in §3. (b) Under s_0 every unit is at rest 0 (start column: pairs and e's
at 0; (y, ȳ) = (0, 1); (y′, ȳ′) = (0, 1)), and the input of unit 1 is (C_0, E_0) = (0, 0); the input of unit i ≥ 2 is (C_(i−1),
E_(i−1)) = (0, 0) (rest). By WIRE, v_0 moves at step 1 and nothing else below level 1 ever moves; so the input of unit 1 is (1, 1)
under every s_τ, τ ≥ 1. (H1), (H2) hold for j = 1, a = 0, t = 1 (v_1 moves in step 1 itself: the step is «level by level», so
C_0(s_1) = 1 is seen by level 1). The RESPONSE LEMMA gives the moves of the steps 1, …, 1 + P_1 − 2 = 2·P_2 = 2^k − 2, each step
changing a mover, and the last state has REST_1(1) and REST_i(0) for i ≥ 2. Under it the input of unit 1 is (1, 1) and the input of
unit i ≥ 2 is (0, 0), so by STABLE and WIRE no mover moves: s′ = s, the run stops, L(G_k) = 2^k − 2. The stop is «stuck»: v_1 (at
1 = C_0, key-disabled) is value-enabled, since EY_1 = 0 = 1 − s(v_1) (V4), so A_s(v_1) has two elements. (c) Unit 1 responds once and unit j + 1 twice per response of unit j: unit j makes 2^(j−1) responses. By the RESPONSE LEMMA's
list a response of unit j moves v_j, u_j, e_j once each, and in each observer pair it moves one observer to back (F, resp. F′) and
the other to forward (B, resp. B′): every mover of unit j moves exactly once per response of unit j. Wires and u_0 never move, v_0
once (WIRE). The units have 4 movers for j = 1 and j = k − 1 and 7 for 2 ≤ j ≤ k − 2, which gives the total. ∎
**Corollary EXP-N5.** G_k has an acyclic Ξ-graph (MEMBER), so R117's Theorem REACH3 applies with L(G_k) = 2^k − 2 ≥ 1: the N5 run
of Γ3(G_k) from S3 has one FL run of length exactly 2^k − 2 and makes at least 2^k − 1 iterations; n = N + 7M + 10 = (9k − 16) +
7(18k − 32) + 10 = 135k − 230. Edges of Γ3(G) by R117's description of the game (movers M; gates 2M; β-vertices one edge to the pad
pb and one more when the Ξ-target is a mover: M + M_X; e-vertices M; pads pe, pβ, pb, m: 4M; the two self-loops 2; K0-K3 two each;
pA, s, q, r one each): m = 9M + M_X + 14, M_X the number of options whose Ξ-target is a mover; in G_k the options on X are those
of u_0, v_0 and the 2k − 5 wires, 4k − 6 in all, so M_X = 14k − 26 and m = 176k − 300 (checked on the .pg files, §9.5: sizediff 0).
2^k − 1 exceeds every polynomial in 311k − 530 for large k. (Remark: this is the family R117's Corollary REAL-IDEAL-S3 speaks of.) ∎

## 8. Where the start, the ε orders and the rank orders are used
- START: only in (H1) at t = 1 (§7): every unit at rest 0, i.e. pairs and end-followers at option 0, (y_j, ȳ_j) = (0, 1), (y′_j,
  ȳ′_j) = (0, 1), wires at 0, u_0 and v_0 at 0. (DATA, L-RED 70 via the Lead: one start flipped shortens the run for u, ȳ, e, y′, ȳ′;
  §9.6 row «ybst»: the starts of ȳ, ȳ′ set to back give T = 3.)
- ε orders (all inside one level): ε(u_j, o) < ε(v_j, o) for o = 0, 1 (K1, aligned case); ε(E(j + 1), 1) < ε(wv_j, 0) (K2);
  ε(E(j + 1), 0) < ε(wu_j, 0) (K3); ε(wire, 0) < ε(wire, 1) and ε(u_0, 0) < ε(u_0, 1) (WIRE); ε(v_0, 1) < ε(u_0, 0) < ε(v_0, 0)
  (K1 at level 0, WIRE). Nothing else: the order of the two gates of one observer, of e_j, u_j, v_j (their W-targets differ, MOVE-2),
  and every order between movers that are never compared (e.g. observers of one level) is free.
- Rank orders: depth-major (V0); inside a depth: δ(v_j, ·) > δ(u_j, ·) (V1, split); in Y_j and in Y′_j: (y, forward) > (ȳ, back) and
  (ȳ, forward) > (y, back) (V2, V3: «the forward one is ahead»; the table has 3 > 2 > 1 > 0 and 7 > 6 > 5 > 4); δ(v_0, 1) > δ(u_0, 0)
  > δ(v_0, 0) (V1 at level 0); wires and u_0: irrelevant for moves (key-disabled), any ranks. Parities: all 0 (V0).

## 9. DATA (pasted from generated files; files in experiments/red-b/data/b6b/, pinned in data/SHA1SUMS; not to sign)
Genomes: data/b6b/G/G_k.json (k = 3..14; the rule's output, gk.py build(k); the genomes of record) and data/b6b/raw/G_k.json (the
first generator version's files, gk.py --raw; DATA only: same comparisons, same run). Games: data/b6b/pg/G_k_g3.pg (k = 3..11).
Every clause below names its must-0 counter(s) and its control. THIS lane's DATA is what follows. OTHER lanes' DATA on the same
family, as relayed by the Lead (12:38Z, 12:43Z), not opened and not re-run by me, to be cited by the Lead from their commits (not
on origin at 12:49Z: claude/l-comp was at b2cc5a00, claude/l-red at 306d74f6): L-COMP 22 (own generator; C port, T = 2^k − 2 for k
= 3..20; n5b on its own Γ3 builder own34.build, 2^k + 1 iterations for k = 3..9, strategies verified), L-RED 70 (R245: own generator,
own SPEC engine n5s237 for k = 3..8, its own Zielonka to k = 7, 1,200 ε renumberings inside the rule's orders keep T; verdict
SURVIVES), the Lead (rebuild byte-equal; one217.OneP for k = 3..14). With them: three N5 engines (n5v, n5b, n5s237) and three Γ3
builders (gamma3.build, this lane's eng3, own34.build).
### 9.1 Membership (b6member.py → member.out, member_raw.out, member_ctrl.out, member_quote.out)
Must-0 counters c1-c8 (one per clause of §4; viol = their sum; member = [viol = 0]); unit genomes; set G_3..G_14 (the rule's output):
```
G_3.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 11 M 22 d 4 deg [2] samew 3 allexit 3 odd 0
G_4.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 20 M 40 d 5 deg [2] samew 5 allexit 5 odd 0
G_5.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 29 M 58 d 6 deg [2] samew 7 allexit 7 odd 0
G_6.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 38 M 76 d 7 deg [2] samew 9 allexit 9 odd 0
G_7.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 47 M 94 d 8 deg [2] samew 11 allexit 11 odd 0
G_8.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 56 M 112 d 9 deg [2] samew 13 allexit 13 odd 0
G_9.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 65 M 130 d 10 deg [2] samew 15 allexit 15 odd 0
G_10.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 74 M 148 d 11 deg [2] samew 17 allexit 17 odd 0
G_11.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 83 M 166 d 12 deg [2] samew 19 allexit 19 odd 0
G_12.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 92 M 184 d 13 deg [2] samew 21 allexit 21 odd 0
G_13.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 101 M 202 d 14 deg [2] samew 23 allexit 23 odd 0
G_14.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 raw_c5 0 N 110 M 220 d 15 deg [2] samew 25 allexit 25 odd 0
```
The raw files (gates 100·level + ε): only c5 fails (viol 1 = c5), and normdiff = [the normalised raw file is not byte-equal to
G_k] is 0 (member_raw.out; the line shows the normalised copy's counters):
```
G_3.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_4.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_5.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_6.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_7.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_8.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_9.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_10.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_11.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_12.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_13.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
G_14.json ctrl 0 member 1 viol 0 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0 normdiff 0
```
Controls: 8 copies of G_5, each damaged in one clause (skipped level, W-target of the same level, Ξ-target no mover, repeated β-id,
repeated gate, parity 2, start no option, Ξ self-loop); every one fires its clause:
```
G_5.json ctrl 1 member 0 viol 3 c1 1 c2 2 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0
G_5.json ctrl 2 member 0 viol 1 c1 0 c2 1 c3 0 c4 0 c5 0 c6 0 c7 0 c8 0
G_5.json ctrl 3 member 0 viol 1 c1 0 c2 0 c3 1 c4 0 c5 0 c6 0 c7 0 c8 0
G_5.json ctrl 4 member 0 viol 1 c1 0 c2 0 c3 0 c4 1 c5 0 c6 0 c7 0 c8 0
G_5.json ctrl 5 member 0 viol 1 c1 0 c2 0 c3 0 c4 0 c5 1 c6 0 c7 0 c8 0
G_5.json ctrl 6 member 0 viol 1 c1 0 c2 0 c3 0 c4 0 c5 0 c6 1 c7 0 c8 0
G_5.json ctrl 7 member 0 viol 1 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 1 c8 0
G_5.json ctrl 8 member 0 viol 1 c1 0 c2 0 c3 0 c4 0 c5 0 c6 0 c7 0 c8 1
```
### 9.2 The run on three simulators, state by state (b6sim.py → sim.out, sim_ctrl.out)
A = onep.py (this lane, from box 217 §6.1's text), B = one217.OneP (L-NEW a143d406), C = r187/ideal.traj (L-RED; the simulator
R104's packet names: «implemented as r178/fastcyc.simulate and r187/ideal.traj»). Must-0 counter: ideq = [the three state sequences
are not identical]; unit genomes; set G_3..G_14. stop = C's stop word.
```
G_3.json ctrl 0 N 11 M 22 levels 4 T 6 TB 6 TC 6 ideq 0 maxsw 2 sumsw 13 howard 3 stop stuck k 1 mindeg 2
G_4.json ctrl 0 N 20 M 40 levels 5 T 14 TB 14 TC 14 ideq 0 maxsw 4 sumsw 35 howard 4 stop stuck k 1 mindeg 2
G_5.json ctrl 0 N 29 M 58 levels 6 T 30 TB 30 TC 30 ideq 0 maxsw 8 sumsw 79 howard 4 stop stuck k 1 mindeg 2
G_6.json ctrl 0 N 38 M 76 levels 7 T 62 TB 62 TC 62 ideq 0 maxsw 16 sumsw 167 howard 4 stop stuck k 1 mindeg 2
G_7.json ctrl 0 N 47 M 94 levels 8 T 126 TB 126 TC 126 ideq 0 maxsw 32 sumsw 343 howard 4 stop stuck k 1 mindeg 2
G_8.json ctrl 0 N 56 M 112 levels 9 T 254 TB 254 TC 254 ideq 0 maxsw 64 sumsw 695 howard 4 stop stuck k 1 mindeg 2
G_9.json ctrl 0 N 65 M 130 levels 10 T 510 TB 510 TC 510 ideq 0 maxsw 128 sumsw 1399 howard 4 stop stuck k 1 mindeg 2
G_10.json ctrl 0 N 74 M 148 levels 11 T 1022 TB 1022 TC 1022 ideq 0 maxsw 256 sumsw 2807 howard 4 stop stuck k 1 mindeg 2
G_11.json ctrl 0 N 83 M 166 levels 12 T 2046 TB 2046 TC 2046 ideq 0 maxsw 512 sumsw 5623 howard 4 stop stuck k 1 mindeg 2
G_12.json ctrl 0 N 92 M 184 levels 13 T 4094 TB 4094 TC 4094 ideq 0 maxsw 1024 sumsw 11255 howard 4 stop stuck k 1 mindeg 2
G_13.json ctrl 0 N 101 M 202 levels 14 T 8190 TB 8190 TC 8190 ideq 0 maxsw 2048 sumsw 22519 howard 4 stop stuck k 1 mindeg 2
G_14.json ctrl 0 N 110 M 220 levels 15 T 16382 TB 16382 TC 16382 ideq 0 maxsw 4096 sumsw 45047 howard 4 stop stuck k 1 mindeg 2
```
Control (A with the two gates of one level-0 mover exchanged): `G_5.json ctrl 1 N 29 M 58 levels 6 T 15 TB 30 TC 30 ideq 1 maxsw 4 sumsw 38 howard 4 stop stuck k 0 mindeg 2`
### 9.3 The proof's direct test on the real run (b6lemma.py → lemma.out, lemma_ctrl.out)
Must-0 counters: kfact / vfact: #(state, comparison) where a key / value order computed from the simulator differs from K1-K3 /
V1-V3; sched: #steps whose set of (mover, new option) differs from the RESPONSE LEMMA's schedule (generated recursively from the
lemma); tlen: [T ≠ 2^k − 2 or the schedule's last step ≠ T]; rest: [the final state is not REST_1(1), REST_i(0)]; swk: #movers whose
number of option changes differs from Theorem EXP-IDEAL (c). Units as named; set: every state / step / mover of the run of G_3..G_14.
```
G_3 ctrl 0 states 7 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 6 moves 13 maxsw 2
G_4 ctrl 0 states 15 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 14 moves 35 maxsw 4
G_5 ctrl 0 states 31 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 30 moves 79 maxsw 8
G_6 ctrl 0 states 63 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 62 moves 167 maxsw 16
G_7 ctrl 0 states 127 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 126 moves 343 maxsw 32
G_8 ctrl 0 states 255 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 254 moves 695 maxsw 64
G_9 ctrl 0 states 511 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 510 moves 1399 maxsw 128
G_10 ctrl 0 states 1023 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 1022 moves 2807 maxsw 256
G_11 ctrl 0 states 2047 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 2046 moves 5623 maxsw 512
G_12 ctrl 0 states 4095 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 4094 moves 11255 maxsw 1024
G_13 ctrl 0 states 8191 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 8190 moves 22519 maxsw 2048
G_14 ctrl 0 states 16383 kfact 0 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 16382 moves 45047 maxsw 4096
```
Controls (the schedule with the two observers of every pair exchanged; K2 with «and» for «or»):
```
G_5 ctrl 1 states 31 kfact 0 vfact 0 sched 19 tlen 0 rest 0 swk 0 T 30 moves 79 maxsw 8
G_5 ctrl 2 states 31 kfact 25 vfact 0 sched 0 tlen 0 rest 0 swk 0 T 30 moves 79 maxsw 8
```
### 9.4 N5 itself on Γ3(G_k): two engines, two builders (b6n5.py → n5.out, n5_ctrl.out)
n = N + 7M + 10; T1p = the run length on the model (A); F = N5 iterations before its first fallback; mism = [N5's mover states
s_0..s_F ≠ the model's]; its / fb = engine 1 (L-NEW's n5v.step, mode spec, from S3 = n5x.start_pair) to N5's stop; wrong = #vertices
whose winner differs from experiments/harness zielonka; nonmover = #transitions before the fallback that change a non-mover Even
vertex or τ; its2 / fb2 / wrong2 = engine 2 (L-COMP's n5b.py --mode spec on the .pg file); engdiff = [(its, fb) ≠ (its2, fb2)];
gdiff = [this lane's Γ3 builder (eng.py, eng3.py) gives a game different from L-NEW's gamma3.build].
```
G_3 mode spec ctrl 0 N 11 M 22 n 175 T1p 6 F 6 mism 0 its 9 fb 1 wrong 0 nonmover 0 its2 9 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 fca7a52c49e095d297458c2264664b846c442f8b secs1 0.0 secs2 0.1
G_4 mode spec ctrl 0 N 20 M 40 n 310 T1p 14 F 14 mism 0 its 17 fb 1 wrong 0 nonmover 0 its2 17 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs1 0.1 secs2 0.3
G_5 mode spec ctrl 0 N 29 M 58 n 445 T1p 30 F 30 mism 0 its 33 fb 1 wrong 0 nonmover 0 its2 33 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 f145a99c548d3f5489c0aca1552ed6eb96deafc3 secs1 0.5 secs2 0.8
G_6 mode spec ctrl 0 N 38 M 76 n 580 T1p 62 F 62 mism 0 its 65 fb 1 wrong 0 nonmover 0 its2 65 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 b9fea1092df47c2abfefef85bf18511346da7d71 secs1 1.6 secs2 2.7
G_7 mode spec ctrl 0 N 47 M 94 n 715 T1p 126 F 126 mism 0 its 129 fb 1 wrong 0 nonmover 0 its2 129 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 daa0f243aefaaf8cbdd205283f5fc7ce2f3d0f56 secs1 4.9 secs2 7.8
G_8 mode spec ctrl 0 N 56 M 112 n 850 T1p 254 F 254 mism 0 its 257 fb 1 wrong 0 nonmover 0 its2 257 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 924239d911a4c32a32397a7ed5ab2efdacf02fee secs1 14.3 secs2 22.3
G_9 mode spec ctrl 0 N 65 M 130 n 985 T1p 510 F 510 mism 0 its 513 fb 1 wrong 0 nonmover 0 its2 513 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 9cece8a782b6212e06a177c0899422ebac6e3b0b secs1 37.8 secs2 59.0
G_10 mode spec ctrl 0 N 74 M 148 n 1120 T1p 1022 F 1022 mism 0 its 1025 fb 1 wrong 0 nonmover 0 its2 1025 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 615292907463d55cb3156d14914af2a916e5b27e secs1 95.3 secs2 147.1
G_11 mode spec ctrl 0 N 83 M 166 n 1255 T1p 2046 F 2046 mism 0 its 2049 fb 1 wrong 0 nonmover 0 its2 2049 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 9616b4f07e144c84c31f56475ead8c04f0a2dbdc secs1 252.1 secs2 384.4
```
On every line: F = T1p = 2^k − 2 (first fallback at transition 2^k − 1), mism 0, its = its2 = 2^k + 1, fb = fb2 = 1, wrong = wrong2
= 0, nonmover 0, engdiff 0, gdiff 0. Controls (compare with the Howard run: mism fires; Zielonka's answer flipped at one vertex:
wrong, wrong2 fire; engine 1 as N5′-xi: engdiff fires, N5′-xi stops after 7 iterations):
```
G_4 mode spec ctrl 1 N 20 M 40 n 310 T1p 4 F 14 mism 1 its 17 fb 1 wrong 0 nonmover 0 its2 17 fb2 1 wrong2 0 engdiff 0 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs1 0.1 secs2 0.3
G_4 mode spec ctrl 2 N 20 M 40 n 310 T1p 14 F 14 mism 0 its 17 fb 1 wrong 1 nonmover 0 its2 17 fb2 1 wrong2 1 engdiff 0 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs1 0.1 secs2 0.2
G_4 mode xi ctrl 0 N 20 M 40 n 310 T1p 14 F 4 mism 1 its 7 fb 1 wrong 0 nonmover 0 its2 17 fb2 1 wrong2 0 engdiff 1 gdiff 0 pg_sha1 4a2e89c57ec82362c128074c8be3344fb3c0da61 secs1 0.1 secs2 0.3
G_6 mode xi ctrl 0 N 38 M 76 n 580 T1p 62 F 4 mism 1 its 7 fb 1 wrong 0 nonmover 0 its2 65 fb2 1 wrong2 0 engdiff 1 gdiff 0 pg_sha1 b9fea1092df47c2abfefef85bf18511346da7d71 secs1 0.2 secs2 2.8
```
### 9.5 Sizes, explicit bounds, fits with residuals, contrast rows (b6size.py → size.out, size_ctrl.out; b6fit.py → fit.out)
Must-0 counter sizediff = [n ≠ 135k − 230] + [m ≠ 176k − 300] on the .pg files (control: m tested against 176k − 299 fires:
`G_3_g3.pg ctrl 1 k 3 n 175 m 228 sizediff 1`), then the first k beyond n^c and (n + m)^c:
```
G_3_g3.pg ctrl 0 k 3 n 175 m 228 sizediff 0
G_4_g3.pg ctrl 0 k 4 n 310 m 404 sizediff 0
G_5_g3.pg ctrl 0 k 5 n 445 m 580 sizediff 0
G_6_g3.pg ctrl 0 k 6 n 580 m 756 sizediff 0
G_7_g3.pg ctrl 0 k 7 n 715 m 932 sizediff 0
G_8_g3.pg ctrl 0 k 8 n 850 m 1108 sizediff 0
G_9_g3.pg ctrl 0 k 9 n 985 m 1284 sizediff 0
G_10_g3.pg ctrl 0 k 10 n 1120 m 1460 sizediff 0
G_11_g3.pg ctrl 0 k 11 n 1255 m 1636 sizediff 0
first k with 2^k - 1 > (n)^2: k 23 size 2875 iterations_bound 8388607 poly 8265625
first k with 2^k - 1 > (n+m)^2: k 26 size 7556 iterations_bound 67108863 poly 57093136
first k with 2^k - 1 > (n)^3: k 37 size 4765 iterations_bound 137438953471 poly 108190397125
first k with 2^k - 1 > (n+m)^3: k 41 size 12221 iterations_bound 2199023255551 poly 1825241069861
first k with 2^k - 1 > (n)^4: k 51 size 6655 iterations_bound 2251799813685247 poly 1961517735450625
first k with 2^k - 1 > (n+m)^4: k 57 size 17197 iterations_bound 144115188075855871 poly 87460260197502481
```
Fits (model E = the closed forms; X = free exponential; P = free power law):
```
T_key against N + M: points 12 sizes 33..330
  model E residuals (value - closed form): 0 0 0 0 0 0 0 0 0 0 0 0
  model X log2(value) = 1.5419 + 0.037973 * size; max |residual| 0.2101
  model P log2(value) = -16.7652 + 3.4822 * log2(size); max |residual| 1.7845; local exponents 1.42 2.05 2.69 3.34 4.00 4.68 5.36 6.05 6.74 7.43 8.12
max sw against N + M: points 12 sizes 33..330
  model E residuals (value - closed form): 0 0 0 0 0 0 0 0 0 0 0 0
  model X log2(value) = -0.2222 + 0.037037 * size; max |residual| 0.0000
  model P log2(value) = -17.9054 + 3.3725 * log2(size); max |residual| 1.8931; local exponents 1.16 1.87 2.56 3.26 3.96 4.65 5.35 6.04 6.73 7.43 8.12
N5 iterations (engine 1) against n: points 9 sizes 175..1255
  model E residuals (value - closed form): 0 0 0 0 0 0 0 0 0
  model X log2(value) = 1.8335 + 0.007280 * size; max |residual| 0.0625
  model P log2(value) = -18.4838 + 2.7580 * log2(size); max |residual| 1.1032; local exponents 1.11 1.83 2.56 3.28 3.99 4.69 5.39 6.09
N5 iterations (engine 2) against n: points 9 sizes 175..1255
  model E residuals (value - closed form): 0 0 0 0 0 0 0 0 0
  model X log2(value) = 1.8335 + 0.007280 * size; max |residual| 0.0625
  model P log2(value) = -18.4838 + 2.7580 * log2(size); max |residual| 1.1032; local exponents 1.11 1.83 2.56 3.28 3.99 4.69 5.39 6.09
```
Reading: the closed forms (model E: T = 2^k − 2, max sw = 2^(k−2), iterations = 2^k + 1, with k = (N + M + 48)/27 = (n + 230)/135)
have residual 0 at every point; a free power law (model P) has local exponents that grow from point to point. DATA on k ≤ 14
(model) and k ≤ 11 (N5); for all k: Theorem EXP-IDEAL and Corollary EXP-N5.
Contrast on the same genomes (L-NEW's one217.py: key / howard / seq → one217.out):
```
G_3.json N 11 M 22 key 6 howard 3 seq 10 ctrl 0
G_4.json N 20 M 40 key 14 howard 4 seq 25 ctrl 0
G_5.json N 29 M 58 key 30 howard 4 seq 51 ctrl 0
G_6.json N 38 M 76 key 62 howard 4 seq 73 ctrl 0
G_7.json N 47 M 94 key 126 howard 4 seq 96 ctrl 0
G_8.json N 56 M 112 key 254 howard 4 seq 118 ctrl 0
G_9.json N 65 M 130 key 510 howard 4 seq 140 ctrl 0
G_10.json N 74 M 148 key 1022 howard 4 seq 162 ctrl 0
G_11.json N 83 M 166 key 2046 howard 4 seq 184 ctrl 0
G_12.json N 92 M 184 key 4094 howard 4 seq 206 ctrl 0
```
### 9.6 Which features are essential (gkvar.py → ablate.out; DATA, one feature removed at a time, all variants members of R104's class)
```
none k 4 N 20 M 40 member 1 T 14 howard 4 maxsw 4
none k 5 N 29 M 58 member 1 T 30 howard 4 maxsw 8
none k 6 N 38 M 76 member 1 T 62 howard 4 maxsw 16
none k 7 N 47 M 94 member 1 T 126 howard 4 maxsw 32
none k 8 N 56 M 112 member 1 T 254 howard 4 maxsw 64
none k 9 N 65 M 130 member 1 T 510 howard 4 maxsw 128
none k 10 N 74 M 148 member 1 T 1022 howard 4 maxsw 256
nowv k 4 N 18 M 36 member 1 T 14 howard 4 maxsw 4
nowv k 5 N 26 M 52 member 1 T 30 howard 4 maxsw 8
nowv k 6 N 34 M 68 member 1 T 62 howard 4 maxsw 16
nowv k 7 N 42 M 84 member 1 T 126 howard 4 maxsw 32
nowv k 8 N 50 M 100 member 1 T 254 howard 4 maxsw 64
nowv k 9 N 58 M 116 member 1 T 510 howard 4 maxsw 128
nowv k 10 N 66 M 132 member 1 T 1022 howard 4 maxsw 256
nowu k 4 N 19 M 38 member 1 T 6 howard 4 maxsw 2
nowu k 5 N 27 M 54 member 1 T 6 howard 4 maxsw 2
nowu k 6 N 35 M 70 member 1 T 6 howard 4 maxsw 2
nowu k 7 N 43 M 86 member 1 T 6 howard 4 maxsw 2
nowu k 8 N 51 M 102 member 1 T 6 howard 4 maxsw 2
nowu k 9 N 59 M 118 member 1 T 6 howard 4 maxsw 2
nowu k 10 N 67 M 134 member 1 T 6 howard 4 maxsw 2
noend k 4 N 16 M 32 member 1 T 8 howard 3 maxsw 4
noend k 5 N 21 M 42 member 1 T 12 howard 3 maxsw 4
noend k 6 N 26 M 52 member 1 T 14 howard 3 maxsw 4
noend k 7 N 31 M 62 member 1 T 16 howard 3 maxsw 4
noend k 8 N 36 M 72 member 1 T 18 howard 3 maxsw 4
noend k 9 N 41 M 82 member 1 T 20 howard 3 maxsw 4
noend k 10 N 46 M 92 member 1 T 22 howard 3 maxsw 4
upar k 4 N 20 M 40 member 1 T 2 howard 3 maxsw 1
upar k 5 N 29 M 58 member 1 T 2 howard 3 maxsw 1
upar k 6 N 38 M 76 member 1 T 2 howard 3 maxsw 1
upar k 7 N 47 M 94 member 1 T 2 howard 3 maxsw 1
upar k 8 N 56 M 112 member 1 T 2 howard 3 maxsw 1
upar k 9 N 65 M 130 member 1 T 2 howard 3 maxsw 1
upar k 10 N 74 M 148 member 1 T 2 howard 3 maxsw 1
ybst k 4 N 20 M 40 member 1 T 3 howard 3 maxsw 1
ybst k 5 N 29 M 58 member 1 T 3 howard 4 maxsw 1
ybst k 6 N 38 M 76 member 1 T 3 howard 4 maxsw 1
ybst k 7 N 47 M 94 member 1 T 3 howard 4 maxsw 1
ybst k 8 N 56 M 112 member 1 T 3 howard 4 maxsw 1
ybst k 9 N 65 M 130 member 1 T 3 howard 4 maxsw 1
ybst k 10 N 74 M 148 member 1 T 3 howard 4 maxsw 1
rank k 4 N 20 M 40 member 1 T 1 howard 1 maxsw 1
rank k 5 N 29 M 58 member 1 T 1 howard 1 maxsw 1
rank k 6 N 38 M 76 member 1 T 1 howard 1 maxsw 1
rank k 7 N 47 M 94 member 1 T 1 howard 1 maxsw 1
rank k 8 N 56 M 112 member 1 T 1 howard 1 maxsw 1
rank k 9 N 65 M 130 member 1 T 1 howard 1 maxsw 1
rank k 10 N 74 M 148 member 1 T 1 howard 1 maxsw 1
```
none = the rule; nowv = no wire wv_j (the observers of Y_j take v_(j+1) as back W-target): T is still 2^k − 2 at N = 8k − 14 (so 9 is
not least; this variant is NOT covered by the proof); nowu = no wire wu_j (Y′_j takes u_(j+1)); noend = no end-followers and no
pairs Y′ (observers read u_(j+1)); upar = u_j parallel like v_j; ybst = ȳ, ȳ′ start on back; rank = ranks depth-major the other way.
### 9.7 Quote check (b6quote.py → quote.out)
`QUOTESUMMARY`

## 10. Reproduction
- Archives into an ignored directory R = experiments/red-b/work/b6 (other lanes' files are read, never edited):
  `git archive a143d4060d75f8463fe098b6ce18eef3febcd14b experiments/new/box217 experiments/new/box195 experiments/new/box189
  experiments/new/box190 experiments/new/box21 experiments/harness $(git ls-tree --name-only a143d406 experiments/new/
  experiments/si/ | grep '\.py$') | tar -x -C R/lnew`; `git archive aa4f76805c9290b419d6388eb60ac32b3a03db7c experiments/red/r187
  experiments/red/r178 | tar -x -C R/lred`; `git archive 5d7aab0f19f664034567c3bf4f41bcf9e1684d20 experiments/n5-second
  experiments/harness experiments/hard-families/pgsolver_si.py | tar -x -C R/trunk`; `git show 5d7aab0f:docs/red/P-N5-REALIZE.md >
  R/trunk/docs/red/P-N5-REALIZE.md`; `git show 5d7aab0f:docs/RESULTS.md > R/RESULTS.trunk.md`; `git show 5d7aab0f:docs/GAPS.md >
  R/GAPS.trunk.md`.
- `bash experiments/red-b/run_b6b.sh R all 11` (resumable; stages gen, member, sim, lemma, bilad, ctrl, n5; the n5 stage with both
  engines takes about 0.1, 0.4, 1.3, 4.3, 13, 37, 97, 242, 637 s for k = 3..11), `bash experiments/red-b/run_b6b.sh R sim 14` and
  `lemma 14` for the larger model runs, `python3 experiments/red-b/b6fit.py R/out/sim.out R/out/n5.out`, `python3
  experiments/red-b/gkvar.py --all 4 5 6 7 8 9 10`, and `python3 experiments/red-b/b6quote.py docs/red-b/P-N5-EXP.md
  R104P=R/trunk/docs/red/P-N5-REALIZE.md R117=R/RESULTS.trunk.md TARGET=TARGET.md CLAUDE=CLAUDE.md GAPS=R/GAPS.trunk.md`.
- Without any archive: `python3 experiments/red-b/gk.py 8` (prints key 254), `python3 experiments/red-b/b6lemma.py 8`, and the gate's
  self-check in experiments/red-b/check.sh (G_3..G_8: b6lemma counters 0, both controls fire, G_6 a member).

## 11. For the referees (READING; not to sign)
- Press points. (1) MOVE-2's reading of a step: keys with s′ on the lower levels, values under s; the RESPONSE LEMMA uses it at
  every «in the same step» (v_j with the pair below; the observers with E(j + 1); F′ with u_j). §9.3's sched counter tests exactly
  this on the real run. (2) V0: ranks depth-major, all parities even, wires never a Ξ-target. (3) K2 / K3: the wire ε's (6, 8) are
  above the ε's of E(j + 1)'s options (0, 1 for e_j; 2, 3 for u_(k−1)). (4) The top unit's B moves one step after v (its value input
  is read from the old state), the other units' B in the same step as E(j + 1). (5) Level 1 has no end-follower: the last step is
  E(2)'s return. (6) k = 3: units 1 and 2 only, E(2) = u_2, no e, no Y′, one wire wv_1.
- Why 2-wide ladders did not show this (the towers of 𝓛^R_d need about three «fuel» levels per enumerated level): in a doubling
  window the follower must wait for the levels above (RESULTS R120's PULSE-NEST measures that wait), and its Ξ-order must
  flip exactly when they are finished, while the leader's must flip once per window. At every quiescent moment the pairs above are
  in the same state, and the mover's own option alternates: no value order read from the ladder above can alternate (a parity
  obstruction). In G_k the signal goes up BY KEY (the end-follower reaches the leader's new key only when its own window is over; an
  observer two levels up compares it with a wire) and comes back BY VALUE (the observer pair's value order flips once per window;
  the block pair is Ξ-above it), and the window parity comes by value from the pair BELOW; Ξ runs down the levels, so it is acyclic.
- Box 217's vocabulary: G_k has enumeration depth k(G) = 1 (no mover above level 0 switches |K| − 1 times); the pair of level j
  switches 2^(j−1) = |K(u_j)|/4 times (the half-rate regime). ENUM-LOG, a necessary condition only, is not violated; SW-POLY is.
- Remarks relayed by the Lead (12:43Z, C5; not mine, not checked here): (i) L-RED 70, R245: G_k lies outside R110's 2-wide class
  𝓛^R_d (up to 8 movers on a level; wires), so R113 (ALIGN, PAIR-DOUBLE) and R120 (PULSE-NEST) do not apply; R113's KP-MOVE holds and
  is not violated; verdict SURVIVES; 1,200 ε renumberings inside the stated orders keep T; one flipped start shortens it. (ii) The
  necessary condition ENUM-NEC of P-N5-KEY1P is not violated. (iii) Contrast: Howard's rule 4 steps; N5′-xi 5-7 iterations on the
  same games; the sequential rule about 22k (§9.5's one217.out rows: 10 to 206 for k = 3..12).
