# N12 SETTLE: settle-and-recurse on the parity-induced mean-payoff game (proposal, own tests, DEAD END the same day)
L-NEW successor 78, 2026-11-14 (design day, Lead reading L61; D14, D18, D1). Written 15:15Z by date -u. One implementation
(experiments/new/n12/n12.py, sha1 f321b0a66f44c73fc7338514c95aabb45ec2200d, Python, exact integers). Nothing here is a result (CLAUDE.md
hard rule 1): labels are PROVED (lane, unrefereed, argument given), SOURCE (stated and proved in the opened paper, not refereed by the
fleet), DATA (a committed run), CONJECTURE, READING. No running-time claim is made; the outcome is a dead end.

## 0. Outcome in five lines
- Candidate: read the parity game as a mean-payoff game and solve it by Ohlmann's symmetric recursive algorithm ReduceGame (SOURCE), with
  two lane additions: (R) a repaired test «reduced», (P) reduced-trap peeling; and a side rule (seven tried, two of them the lane's).
- It is correct on every game tried (DATA: 3,000 random games × 7 configurations, 0 wrong regions, 0 bad strategies) and outputs regions and
  positional strategies. The paper's pseudocode test «Reduced» is unsound as written (DATA: 4-vertex witness; 18 wrong of 3,000).
- Both fleet kill families are trivial for it (4 or 5 recursive calls for every size), because they are one-sided games (DATA).
- DEAD: every side rule is exponential on a family. The two best rules (the paper's §6.3 rule «Sbig» and the lane's count-free rule «topx»)
  are polynomial-looking on all 13 M1 families and die together on counter_symsi_N plus 51 pendant vertices (DATA, §6).
- The only rule that pads cannot steer, a work-balanced dovetail of both sides at every recursion node, doubles per nesting level on the
  balanced family tc+ (DATA: ratio 1.73-1.83 per N for N = 8..15; CONJECTURE: 2^Θ(N) = 2^Θ(n^(1/3)) there).

## 1. Why this candidate (the three lessons of the brief; READING)
- (L2) as a decomposition, not a switching rule: the algorithm settles vertices Dijkstra-style, in an order found from a potential, and
  recurses only on the unsettled rest H = G \ F. No strategy is kept and improved, so it is outside the N5 scheme.
- (L3): with the paper's §6.2 every tied escape is settled in one step (a set, not a tie-broken edge); peeling (P) is a greatest fixed point.
- D14: it is L-LIT T27's rank-1 untested candidate C1 (trunk docs/lit/T27-untested.md; never run by the fleet before today).

## 2. Source (opened this session)
P. Ohlmann, «A symmetric recursive algorithm for mean-payoff games», arXiv 2603.07555v1 (8 Mar 2026), 20 pages, PDF sha256
292bde19b74fbe30d6d629264dab93f924da76711fe8a7583db3a0a67f4d1248. Used: §2 (zones N, Z, P, ZN, ZP; «reduced»; potential reduction;
Theorem 3), §3 (the algorithm), §4 Lemmas 4, 5, 6, 7, §5 Algorithm 1 and its subprocedures, §6.1, §6.2 (Lemma 8), §6.3, §6.4, §6.5, §7.
The author's own claim is weaker than ours would have been: §1 «We believe that our algorithm is a candidate for a subexponential runtime,
but we leave such an upper bound to future work»; §7 «So far, we haven't been able to analyse the algorithm in a meaningful way».

## 3. The algorithm, exactly as implemented (n12.py)
**Input** a parity game (TARGET.md §1). **Reduction** (the usual priorities-to-weights reduction; PROVED here in two lines, no
source needed): compress priorities order- and parity-preservingly to p(v) ≤ n; Even = Max, Odd = Min; every edge leaving v gets weight
w(v) = (−1)^p(v) · (n + 1)^p(v). A simple cycle has at most n vertices, so its weight has the sign of its largest priority
((n + 1)^p > (n − 1)(n + 1)^(p − 1)): no zero cycle, and Even wins a vertex iff its mean-payoff value is > 0.
**Objects** (SOURCE §2). A potential φ: V → Z changes weights to w_φ(v, u) = w(v) + φ(u) − φ(v). In a subgame X with potential φ:
N = Min vertices with a < 0 edge and Max vertices with only < 0 edges; P dually; Z the rest; ZN = vertices from which Min can force a < 0
edge before a > 0 one (the Min-attractor of N inside Z along weight-0 edges); ZP = X \ ZN. A vertex of ZN is reduced if Min can force to
immediately see a ≤ 0 edge towards ZN; dually for ZP. X is reduced if every vertex is; then ZN is Odd's region and ZP Even's (SOURCE §2).
```
REDUCE(X, φ):                       # returns (X−, X+, φ′) with X reduced under φ′
  loop:
    (N, P, ZN, ZP) := zones(X, φ)
    if every vertex of X is reduced: return (ZN, ZP, φ)                                   # (R): every vertex, not only N ∪ P
    (P) for s in (+1, −1):  R := the largest subset of ZP (s = +1; of ZN for s = −1, with the roles of the players and the signs
            exchanged) in which every Max vertex has an edge of w_φ ≥ 0 into R and every Min vertex has all its edges of
            w_φ ≥ 0 and into R;  if R ≠ ∅: return CUT(X, φ, s, R, 0)
    s := SIDE(X, φ, N, P);  r := SETTLE(X, φ, s)
    if r = (tail, φ″): φ := φ″ else return r
SETTLE(X, φ, s):                    # s = +1 computes supΣ_N; s = −1 the same code on the game with players and signs exchanged
  F := the vertices from which Min reaches N before any > 0 edge (§6.1);  sup := 0 on F;  φ_pred := none
  loop:
    BacktrackAllPaths: while some v ∉ F has all successors in F: sup(v) := min (v Min) / max (v Max) over u of w_φ(v, u) + sup(u); add v to F
    H := X \ F;  if H = ∅: return (tail, φ + s·sup)                                        # potential reduction; Lemma 7
    (H−, H+, φ_H) := REDUCE(H, φ_pred restricted to H if φ_pred exists, else φ);  φ_pred := φ_H;  ε := s·(φ_H − φ)   # §6.4
    if H+ ≠ ∅ and some Min vertex of H+ has an edge into F:
        m := min over such edges (v, u) of w_φ(v, u) + sup(u) − ε(v)                                                      # Lemma 5a
        S := the vertices of H+ from which Min forces a good escape (an edge from H+ into F of value ≤ m) before any edge of
             w_(φ_H) > 0 or any other edge leaving H+;  sup := m + ε on S;  F := F ∪ S                                   # §6.2, Lemma 8a
    else if H+ ≠ ∅: return CUT(X, φ, s, H+, ε)                                                                            # case 5(a)ii
    else: the same with Max, H− = H, max, ≥ m, w_(φ_H) < 0                                                                # Lemma 5b / 8b
CUT(X, φ, s, T, ε):                 # T is a trap for Min, positively reduced by φ + s·ε
  A, ε := Max-attractor of T in X, ε extended as in AttractMaxAndReduce (Max: max over edges into A; Min: min over all edges)
  (X′−, X′+, φ′) := REDUCE(X \ A, φ);  δ := max over edges (v, a), v ∉ A, a ∈ A, of −w_φ(v, a) − ε(a) + s·(φ′(v) − φ(v))  (0 if none)
  return (X′−, X′+ ∪ A, φ′ on X \ A and φ + s·(ε + δ) on A)                               # Lemma 4 (regions exchanged if s = −1)
```
**Side rules SIDE** (the paper says any choice is correct and terminates, §6.3): small (paper default: s = +1 iff |N| ≤ |P|), large
(|N| ≥ |P|), sup, inf, **Sbig** (§6.3: s = +1 iff the initial F of the sup side is at least as large as that of the inf side), **topx**
(lane: s = +1 iff the largest priority present in X is even), **duet** (lane: run SETTLE(X, φ, +1) and SETTLE(X, φ, −1) as coroutines,
always advancing the one with less work so far; the first to finish is used, the other is dropped; recursive calls dovetail again).
**Output**: (W_E, W_O) = (X+, X−) of REDUCE(V, 0); Even's strategy on W_E: any edge with w_φ′ ≥ 0 staying in W_E; Odd's on W_O: any edge
with w_φ′ ≤ 0 staying in W_O (the least such successor). **Bit cost** (TARGET.md §3): weights have at most p_max·log2(n + 1) + 1 bits;
the largest potential seen is at most 4 bits longer than the largest weight on every run below (DATA: columns maxbits, wbits of
out/tables*.txt), so each arithmetic step costs O(d log n) bit operations on these runs. Counters: calls (REDUCE invocations, dropped dovetail branches included), work (vertex + edge visits).

## 4. Correctness (what is proved where)
- SOURCE: Lemmas 4, 5, 7, 8 and termination for Algorithm 1 with §6.1, §6.2, §6.4 (the paper's proofs; not refereed by the fleet).
- (R), DATA + PROVED (lane): the pseudocode's `Reduced` (§5) tests only N and P, and §2 says «vertices in Z are always reduced». That
  sentence is false: a Max vertex of Z with a weight-0 edge into ZN and a < 0 edge into ZP lies in ZN but Min cannot keep the play in ZN.
  Witness, a parity game on which the literal test returns wrong regions: experiments/new/n12/inst/lit_witness_n4.pg
  (0: priority 0, Odd, → 1, 2;  1: priority 4, Odd, → 0, 3;  2: priority 3, Even, → 0;  3: priority 1, Even, → 0, 1): Odd wins every
  vertex (Zielonka), the literal test stops with {1, 3} for Even. On 3,000 random games the literal test is wrong on 18 (out/rtest.txt,
  last configuration: the firing control). n12.py tests §2's definition on every vertex; the paper's lemmas use only that definition.
- (P), PROVED (lane): R is a trap for Min inside X in which Max keeps edges of w_φ ≥ 0 forever, so it is positively reduced by φ and
  Lemma 4 (with ε = 0 on R) applies to its Max-attractor; symmetric for s = −1. Peeling removes at least one vertex, so it terminates.
- duet, PROVED (lane): both coroutines are runs of SETTLE on the same (X, φ) with private state; whichever returns, its value is a
  valid return value of SETTLE, and §6.3 allows either side. Cost at a node ≤ 2·(the cheaper side) + one scheduling quantum.
- DATA: out/rtest.txt: 3,000 random games (harness gen.py, seed string in rtest.py, n ≤ 30, 1-12 priorities, out-degree ≤ 4): regions
  equal harness Zielonka and both strategies pass harness verify.py for Sbig, duet, small, large, sup, inf and plain Algorithm 1
  (0 failures each). Not run: the 10,000-game Oink comparison of gauntlet step 2 (the candidate died first; SKIPPED, named as skipped).

## 5. Measurements (DATA; out/tables.txt, out/tables2.txt, one line per run; out/summary.txt)
(out/tables.txt and out/rtest.txt were produced with n12.py at sha1 c93af587…, before the four-line policy block «top / topx» was added;
the pinned engine f321b0a6… differs from it by that block only. out/tables2.txt, tables3.txt, duet_tcp.txt: the pinned engine.)
Families: Γ3(G_k) = claude/l-red-b 10dfedb6 experiments/red-b/data/b6b/pg/G_k_g3.pg; W, F, WL = claude/l-si 8c062914
experiments/si/box104/inst; M1 = Oink generators at 8fbf0a7 and experiments/hard-families/pgsolver_port.py. calls for N (or k) in order.
- Both kill families and their relatives (Even wins all but one vertex in each): Γ3(G_k), k = 3..13: Sbig 4, topx 4, large 5 calls for
  every k; W_2..8: 4; F_2..8: 5; WL_1..4: 4. The paper's default side on Γ3(G_k) without peeling: 28, 77, 142, 215, 304, 414, 572, 826,
  1272, 2102, 3700 (second differences 96, 192, 384, 768: exponential); plain Algorithm 1: 75, 1740, 23208 (k = 3..5).
- M1, rule Sbig, N = 1..12, 16, 20 unless said: tc 3N + 1 (N ≥ 3); counter_rob 2N + 1; counter_core 4N − 2; counter_dp N; counter_m ⌈(N+1)/2⌉;
  counter_ortl, counter_qpt 1; counter_rr ≤ 32; recursiveladder ≤ 12; switchallexp, switchbestexp 2; counter_symsi 13, 27, 64, 116, 168,
  230, 302, 384, 476, 578, 690, 1175, 2081 (N = 16), 3259 (N = 20); tc+ (n = 8 … 4448) 2, 6, 14, 29, 49, 82, 127, 196, 278, 381, 520,
  673, 1056 (N = 14), 1559 (N = 16). Rule topx: the same shapes (counter_symsi 17 … 855, 1515, 2367; tc 3 … 167, 287, 439; tc+ 2 … 847,
  1301, 1887). So both rules look polynomial on all 13 families (DATA; no proof).
- The other rules, with peeling: small is exponential in N on tc (3, 12, 26, 81, 227, 730, 2221, 7162) and tc+ (2, 10, 27, 111, 264,
  547, 1033, 1948, 4089); large, sup, inf on counter_symsi (N = 1..9: 13 … 3945; 13 … 15011; 7 … 8286); duet on tc+ (§6).
  Without peeling the rules small, large, sup, inf are all exponential on counter_symsi (ratio about 2.2-2.5 per N at n = 10N + 2).
  (tc has n = Θ(N²) and tc+ n = Θ(N³) vertices, so «exponential in N» there means 2^Θ(√n) and 2^Θ(n^(1/3)): super-polynomial.)

## 6. THE DEAD END (exact instances; all DATA)
- **Instance family** U_N := counter_symsi_N (Oink `counter_symsi N`, n = 10N + 2) plus 50 pendant vertices (owner Odd, priority 1, one
  edge to the top-priority vertex, no predecessor) plus one pendant (owner Even, priority p_max + 1, one edge to vertex 0, no predecessor);
  n = 10N + 53. Pendants have no predecessor, so the regions and strategies of the original vertices are unchanged.
  Files experiments/new/n12/inst/symsi_u50T0_N.pg, N = 5..11 (generators pend.py u50, padtop.py T0; sha1 in inst/SHA1SUMS;
  runs in out/tables3.txt).
  calls, N = 5..11: **Sbig 380, 404, 728, 1652, 4807, 15860, 55193; topx 280, 719, 1812, 4434, 10522, 24312, 54973** (ratios → 3.5 and
  2.3 per N, i.e. per 10 vertices); on the unpadded counter_symsi_N the same rules make 168 … 690 and 162 … 720 calls.
- Each pad alone kills one rule: 50 odd pendants (symsi_u50_N, N = 8..13): Sbig 1652, 4807, 15860, 55173, 195845, 699662 calls, work
  4.9·10^5 … 2.9·10^8, while topx makes 387 … 1002; one top-priority pendant (symsi_T0_N, N = 3..11): topx 53, 109, 280, 719, 1812, 4434,
  10522, 24312, 54973, while Sbig makes 64 … 690. Detour pads inside the game (every Even vertex x and successor y get a path x → z → y
  through a new Even vertex z of the least odd priority above p_max; symsi_D_N) also kill topx: 55 … 39838 (N = 3..11).
- **Obstruction** (READING of the data, not a theorem): on counter_symsi the polynomial runs are one narrow sequence of side choices.
  Flipping Sbig's choice at depth 0 only gives 8, 11, 95, 127, 414, 875, 3330, 10172, 45898 calls (N = 1..9); fixed sides give ratio
  2.1-2.4. A rule that reads counts (Sbig, small, large) is steered by pendants of low priority, a rule that reads priorities (topx) by
  one pendant of high priority, and both kinds of pad are invisible to the game's solution. The scheme has no mechanism that makes a wrong
  side cheap: every settle step re-solves the unsettled rest H, so a wrong side at a node multiplies the cost below it.
- The rule pads cannot steer is duet. It is polynomial-looking on U_N (621, 1024, 1530, 1866, 2467, 3180, 3989) and on counter_symsi,
  but on tc+ (a balanced game: sup and inf sides cost the same, 728 and 726 calls at N = 12) it pays its factor 2 at every nesting
  level: 2, 6, 18, 39, 93, 177, 330, 576, 998, 1732, 2993, 5263, 9374, 16679, 30517 for N = 1..15 (n = 8 … 3690; N = 13..15 in
  out/duet_tcp.txt), ratio 1.73-1.83 for N = 8..15, against 673 calls for Sbig at N = 12. CONJECTURE: 2^Θ(N) calls on tc+_N, which
  is 2^Θ(n^(1/3)): super-polynomial. A cache of finished reductions keyed by the vertex set did not help in a scratch run (393 hits
  in 5,142 calls at N = 12; not pinned).
- Verdict (D1): N12 fails gauntlet step 2 («runtime growth … on every hard family») in every configuration built: no rule is known for
  which the growth is polynomial on M1 and on padded copies of M1. Dead end; not handed to the adversaries.

## 7. Barrier notes (first statement; READING, for the record of what the kill does and does not show)
- Friedmann-type counters for improvement rules: not applicable as theorems (no strategy pair is improved), and switchallexp /
  switchbestexp take 2 calls. The symmetric-SI counter counter_symsi is nevertheless the killing core.
- van Dijk's two counters (tc, tc+) for attractor / tangle methods: tc is linear in N for five of the seven rules; tc+ kills duet.
- Universal trees / separators: no fixed tree or value domain is walked (potentials are sums of at most n weights); the bound does not
  apply, and no run above is limited by potential size (maxbits ≤ wbits + 1).
- Fleet dead ends: L1 of docs/new/c-lane-synthesis.md (single-trajectory potentials) does not apply; the lesson that does is the one
  behind N2 / DE23 and R53: a rule that reads counts or priorities is steered by pads that change no winner.

## 8. What the day adds for the next candidate (READING)
1. Γ3(G_k) and W(H, s0) are one-sided games: they test strategy-improvement rules, not region or potential methods. A region-type
   candidate must be measured on tc, tc+, counter_symsi and on padded copies (pendants of low and of top priority, detour pads).
2. Any binary choice made per recursion node by a statistic of the subgame is a handle (the tie-rule lesson L3 in another place);
   dovetailing the choice costs 2^depth on balanced games. A candidate needs a step whose cost does not depend on such a choice.
3. Reduced-trap peeling under a remembered potential is a cheap, sound re-use of earlier work (with it the paper-default rule goes
   from 19044 to 548 calls on counter_symsi_9, and «larger zone» from quadratic to linear on tc); it is a certificate check,
   usable inside other schemes.
