# T66: do the known exponential families for strategy improvement live in the genome class Γ3 under N5′-xi's rule? None does (E-DOM). On Friedmann's own games every link of the T3 chain holds except DEEP
L-LIT successor (D18, D1; Lead brief and «go» 2026-11-12 11:04Z). Written 2026-11-12 (date -u in the commit). Working note, unrefereed.
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1); DEEP3 stays a CONJECTURE.
Labels: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source); PROVED-in-source; DATA (unit, set,
scope, counter); READING (L-LIT, not to sign).
Tool: docs/lit/T66-depth-check.py (uses experiments/si/si.py, experiments/harness/pg.py, experiments/hard-families/pgsolver_port.py,
all read-only). Fleet files read (other lanes, read-only): claude/l-si 4fda7245 box 99-101; claude/l-red f77a0eef docs/red/R217-ovt.md
§7-§12 (L-RED 54) and 0148d73f R234; claude/l-new 9cdb7209 docs/new/N5-ASC-box193.md §0; trunk 07139249 RESULTS R104, R117, R118, R125.

## 0. Answers
1. The rule matches. On Γ3(G) the mover part of N5′-xi's run is HOW3 (RESULTS R125 (c) REACH3-ALL). HOW3 is Friedmann's locally
   optimizing policy I^loc restricted to the movers. So the lower bounds to test against are the ones for I^loc: Friedmann's G_n in its
   two published forms ([F09] Theorem 8: 13·2^n − 9 iterations; [F11] Theorem 6.14: at least 2^n). Every other published exponential
   family is for another rule or another model (§4).
2. No published family lives in the genome class, and G_n cannot be compiled into it. The excluding feature is E-DOM (L-RED 54's name,
   R217 §10): in Γ(G) and Γ3(G) every escape vertex e has an even priority above every other non-core vertex, so no odd priority can
   lie above an Odd gate's escape. G_n needs exactly that: the access nodes f_i and the selectors k_i are odd and lie above the exits
   h_j of all lower bits ([F11] Table 4). The step of Friedmann's proof that uses it is [F11] Lemma 6.6 (2) (§3).
   - This agrees with L-RED 54's compiled port (R217 §7: exact for 6 steps, then divergence at the access comparison; DATA, lane). I
     add the check against the LMCS game and the lemma, and an E-DOM test on five games (§5.2).
3. Features of the genome class that do NOT exclude G_n: private gates, graded W-targets, the fixed core, the start, and [E-LEV] (§2).
4. So there is no embedding to hand to L-COMP / L-RED, and no literature kill of DEEP3 or U-FREE.
5. What the literature does give (DATA §5.1, new here): on G_n itself, outside the genome class, Howard's run has C = 0 (one cycle
   node), TWO-CROSS's charge holds at every flip (0 failures), and the flips charged to a change of depth > c grow exponentially for
   every fixed c tried (c = 3: 0, 0, 1, 6, 22, 64, 163, 382 for N = 1 … 8). So:
   - the chain «polynomial T3 ⇐ DEEP3» does not contradict Friedmann's theorem: DEEP is precisely the statement that fails on G_n;
   - a proof of DEEP3 cannot be an argument that holds for Howard on every parity game. It has to use E-DOM or another property that
     Γ3 has and G_n lacks. BR-SEG-G, TWO-CROSS and DEPTH-COUNT3 use none.

## 1. The rule (PROVED-in-source; KNOWN)
- [F11] = Friedmann, arXiv 1106.0778 v2 (LMCS 7(3:19) 2011), §4, PDF p.6: «The locally optimizing policy I^loc_G selects a most
  profitable strategy decision in every point with respect to the current valuation. More formally, it holds for every strategy σ,
  every player 0 node v and every w ∈ vE that w ⪯_σ I^loc_G(σ)(v).»
- RESULTS R125, HOW3(G): «every non-mover Even vertex frozen at the standard state's choice …, Odd unrestricted at the gates and K2,
  every mover moving to a ⊴-best successor and keeping a best current one». (c) REACH3-ALL: the mover parts of N5′-xi's run from S3
  «form a run of HOW3(G) … until its first fallback, at iteration T3 + 1».
- [F11] Theorem 6.14 (PDF p.23): «The Strategy Improvement Algorithm with the I^loc-policy requires at least 2^n improvement steps on
  G_n starting with ι_(G_n).» [F09] = Friedmann, arXiv 0901.2731 v1 (LICS 2009), Theorem 8 (PDF p.9): «The strategy improvement
  algorithm requires 13·2^n − 9 iterations on G_n using the locally optimizing» policy. Both are 1-sink games: [F11] §5, PDF p.8.
- READING: I^loc switches every player-0 node; HOW3 switches movers only. A genome is free to make every Even choice vertex a mover,
  so freezing is not a restriction on what can be expressed.

## 2. The genome class in the literature's terms (from P-N5-REALIZE §3.1, R117, R125; READING)
Γ3(G) is a sink game with these constraints (pads, movers and gates are never cycle nodes or in a set Π: R125 (e)):
- Even choice vertices: the movers. Each option of a mover leads to a private Odd gate with two faces.
- β-face: one vertex β of any rank among the β's and either parity, then any mover or the sink u (the Ξ-target).
- e-face: one vertex e, EVEN, above every β (P-N5-REALIZE §3.1: «Ω(e_g) := eb + 2·i, eb := the least even number > bmax, i := the
  position of g in the order by (lev(owner), gate index) (so every Ω(e) is EVEN and above every Ω(β))»), then the W-target, a mover
  exactly one level lower. At level 0 the e-face leads to the Even-won loop c_W, and Odd never takes it (R118 (h) LEVEL0).
- Sink: u = K0, whose play has the odd cycle node K1 below every β (R125 LOC-K2-3). Only c_W, K0, K3 lie above the e's.
- Consequence used below (R125 B-ONLY3): Λ is always less relevant than every e. Odd can refuse every escape.
What this allows and forbids, piece by piece (the «allows» column is L-RED 54's compiler comp.py, R217 §7 and §10, lane):
| feature of a general sink game | in the genome class | excludes G_n? |
| --- | --- | --- |
| direct edge between Even vertices carrying a priority | level-0 option (LEVEL0), or a helper mover whose β carries the priority | no |
| Odd vertex entered from several places ([F11] f_i → e_i and d_i → e_i) | copy gates (one private gate per entering option) | no |
| exit of a bit leading to selectors of higher bits | W-target one level down, then Ξ-edges upward (allowed for every genome; they are the «ascents» of R125 UP-JUMP3, counted by U(G)) | no; but U(G) grows with n, so R125 CHAIN3 (U(G) ≤ B) does not apply |
| escape priorities ordered by bit index | [E-LEV] orders e's by (level, gate index); bits can be given ascending ranks | no |
| initial strategy | Γ3's pads make S3 start at the genome start (R117 S3-START) | no |
| an odd priority above an Odd vertex's escape | impossible: E-DOM-ALL-d (R217 §10, from the builder's text) | YES |

## 3. G_n against the class (PROVED-in-source for the quotes; READING for the mapping)
- [F11] Table 4 (PDF p.15), the whole game: t_1: player 0, 4n + 3, {s, r, c}; t_(i>1): 0, 4n + 2i + 1, {s, r, t_(i−1)}; a_i: 1,
  4n + 2i + 2, {t_i}; c: 0, 8n + 4, {s, r}; d_i: 0, 4i + 1, {s, e_i, r} ∪ {a_j | j < 2i + 1}; e_i: 1, 4i + 2, {d_i, h_i}; g_i: 0,
  4i + 4, {f_i, k_i}; k_i: 0, 8n + 4i + 7, {x} ∪ {g_j | i < j ≤ n}; f_i: 1, 8n + 4i + 9, {e_i}; h_i: 1, 8n + 4i + 10, {k_i}; s: 0,
  8n + 6, {f_j | j ≤ n} ∪ {x}; r: 0, 8n + 8, {g_j | j ≤ n} ∪ {x}; x: 1, 1, {x}.
- The only Odd vertices with a choice are the e_i, with faces d_i (back into the simple cycle) and h_i (the exit, even). In genome
  terms e_i is a gate of mover d_i: β-face back to d_i (a Ξ self-loop with an even β), e-face = the exit. This part fits (R217 §10's
  table says the same for [F09]).
- The violation: for i < j, k_j = 8n + 4j + 7 and f_j = 8n + 4j + 9 are ODD and larger than h_i = 8n + 4i + 10. In a genome h_i must be
  an e-vertex, and then it lies above every odd priority.
- Where Friedmann's proof uses it: [F11] Lemma 6.6 (PDF p.14): «(2) If gate i is σ-open and σ(d_i) ≺_σ h_i, then gate i is σ′-skipped
  («open gates with unprofitable exit nodes will be skipped»).», with the remark «The last two items of Lemma 6.6 are based on the
  uniqueness of priorities in the game, implying that there are no priorities between f_i and h_i.»
  - READING. The access play of an open gate i is f_i, e_i, d_i, then σ(d_i)'s play. σ(d_i)'s play runs through the lane to a root and
    then through the exits h_j of the set bits, lower ones included ([F11] p.18: «Ξ(r) = {r} ∪ {U_j | b_j = 1}», U_j = {g_j, f_j, e_j,
    h_j, k_j}). Lemma 6.6 (2) holds because the odd f_i outranks all of them below h_i. Under E-DOM the lower exits outrank f_i, so the
    access to an open gate becomes profitable as soon as one lower bit is set. That is L-RED 54's ACCESS-NO-PENALTY (R217 §11) and the
    divergence of its compiled port at step 7.
- [F09] (LICS 2009) has the same pattern with other names. I did not re-read its Fig. 7; R217 §10 quotes «m_0 42, m_1 46 (escapes);
  k_0 41, k_1 45 (access, odd); z_0 39, z_1 43 (odd)». The PGSolver generator of that game shows it in §5.2 (k_j, z_j above m_i).
- IMPLIED (source + argument): no priority-preserving compilation of G_n into a genome exists, because the comparison of Lemma 6.6 (2)
  must come out the other way in every genome. L-RED 54 also tried the local repair (a bonus on the skip side instead of a penalty on
  the access side): DEAD, divergence at step 1 (R217 §7). No published variant of G_n avoids the penalty: none found in [F09], [F11],
  Friedmann's thesis §4.3-§4.4, or the sources of this lane's T37.

## 4. The other families (rows from this lane's T37, sources opened there; Fearnley re-opened today)
| family | rule it defeats | model | lives in the genome class under HOW3? |
| --- | --- | --- | --- |
| Friedmann G_n ([F09]; [F11] §6) | locally optimizing = Howard = HOW3's rule | 1-sink parity game | NO: E-DOM (§3) |
| Friedmann H_n ([F11] §8) | globally optimizing (Schewe) | 1-sink parity game | rule differs; the PGSolver game switchbestexp also violates E-DOM (§5.2). No source says H_n is hard for I^loc |
| Fearnley, arXiv 1003.3418 | Howard on MDPs | MDP with probabilistic actions | NO: not a two-player deterministic game. PDF p.2: «Friedmann's example relies on the fact that there are two players in a parity game. We show how Friedmann's example can be adapted …»; p.6: «The actions a_i will be the only probabilistic actions in the example.» Its parity counterpart is G_n |
| Friedmann–Hansen–Zwick, Random-Facet / Random-Edge (errata arXiv 1410.7871; papers not opened, T13) | randomized single switch | sink parity games / MDPs | rule differs; the PGSolver games friedmannsubexp and fearnleysubexp violate E-DOM (§5.2) |
| Disser–Friedmann–Hopp (Zadeh), Avis–Friedmann (Cunningham), Disser–Loho–Maat–Mosis (ranking rules), van Dijk–Loho–Maat (symmetric), Mei (Dantzig) | history-based, index-based, symmetric or single-switch rules | sink games / MDPs | rule differs. Not tested for E-DOM here |
| Zhong–Ye; Hansen–Zwick; Asadi et al. | Howard | deterministic MDPs (one player) | NO: one-player, counted by new cycles; under VJ that is polynomial (T65 §6) |
So the only published lower bounds for HOW3's own rule on two-player parity games are [F09] / [F11] §6 (and Friedmann's thesis).

## 5. DATA (docs/lit/T66-depth-check.py, sha1 in the commit; unit: Howard run from the stated start)
### 5.1 Depth of the gate flips on G_N (outside the genome class)
Counters: T = iterations; C = steps at which some cycle node changes; flips = changes of Odd's optimal choice at an Odd vertex with two
successors; unm = flips at which the value of the face Odd leaves does NOT rise strictly (TWO-CROSS (i) of L-SI box 100 §2; must be 0);
depth of that rise as in box 100 §3; deep = flips of depth > c.
- [F11] Table 4 with ι_(G_N) (PDF p.15: «ι(t_1) = c, ι(g_i) = k_i, ι(* ∈ {t_(i>1), c, d_i}) = r, ι(* ∈ {k_i, s, r}) = x»), command
  `python3 -I docs/lit/T66-depth-check.py lmcs 1 8 3` and `… lmcs 3 8 9`:
| N | vertices | T | C | flips | deep (c = 3) | deep (c = 9) | max depth | unm | flips of e_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 14 | 8 | 0 | 1 | 0 | – | 0 | 0 | 1 |
| 2 | 24 | 26 | 0 | 4 | 0 | – | 3 | 0 | 3 |
| 3 | 34 | 62 | 0 | 11 | 1 | 0 | 6 | 0 | 7 |
| 4 | 44 | 134 | 0 | 26 | 6 | 0 | 9 | 0 | 15 |
| 5 | 54 | 278 | 0 | 57 | 22 | 1 | 12 | 0 | 31 |
| 6 | 64 | 566 | 0 | 120 | 64 | 8 | 15 | 0 | 63 |
| 7 | 74 | 1,142 | 0 | 247 | 163 | 37 | 18 | 0 | 127 |
| 8 | 84 | 2,294 | 0 | 502 | 382 | 130 | 21 | 0 | 255 |
  - Fits on N = 1 … 8 (DATA, not proved here): T = 9·2^N − 10; flips = 2^(N+1) − N − 2; flips of e_1 = 2^N − 1; max depth = 3(N − 1).
  - READING of the depth: a flip at bit i changes the face's Π at the level of bit i, below the three large vertices f_j, h_j, k_j of
    every set bit j > i ([F11] p.18, the sets U_j). So its depth is 3·(number of set bits above i). In a binary counter most flips
    happen at low bits under many set high bits. Hence deep_c grows like 2^N for every fixed c.
- PGSolver's switchallexp ([F09]'s game), best-reward start, `… lics 2 7 3`: T 30 / 70 / 150 / 310 / 630 / 1,243, C 0, flips 4 / 11 /
  26 / 57 / 120 / 247, deep (c = 3) 1 / 5 / 17 / 45 / 105 / 229, max depth 4 / 7 / 10 / 13 / 16 / 19, unm 0. T equals RESULTS R118's
  DATA for N = 2 … 7 (L-NEW's tool brseg_gen191.py), including the off-pattern 1,243 at N = 7, and R217 §7's counts for N = 2 … 5.
- Limits: two games, N ≤ 8; the flip and depth counters come from one engine (L-SI's si.py); only T is cross-checked.
### 5.2 E-DOM test on the ported games (`… edom FAMILY 3`; unit: Odd vertex with two successors; esc = its successor of largest even
priority; listed: odd priorities above pr(esc))
- lmcs (N 3): gates e_1, e_2, e_3; odd above h_1: f_2, f_3, k_2, k_3; above h_2: f_3, k_3; above h_3: none.
- switchallexp (N 3): gates h_0, h_1, h_2 (escapes m_i); odd above m_0: k_1, k_2, z_1, z_2; above m_1: k_2, z_2; above m_2: none.
- switchbestexp (N 3): the same pattern (k_j, z_j above m_i for j > i).
- friedmannsubexp, fearnleysubexp (N 3): 15 and 9 Odd choice vertices; 6 and 2 have no even successor at all; of the others only one is
  free of odd priorities above its escape (the lowest escape has 25 odd priorities above it).
- In every game only the top bit's gate passes. E-DOM fails at every other gate.

## 6. What this says about DEEP3 (READING)
- The chain (L-SI box 101 Addendum A, or T65 §3 Option A) is: window length (BR-SEG) × number of windows; windows are cut by Λ-changes
  and gate flips; a flip is charged to a face-value change (TWO-CROSS); changes of depth ≤ c are polynomially many (DEPTH-COUNT3);
  the rest is Deep_c.
- On G_N every one of these steps holds as stated or measured: C = 0; BR-SEG-G is landed for every game under H0 (R118 (i)); unm = 0;
  DEPTH-COUNT3 uses only the VJ order and monotonicity. The run is exponential. So Deep_c is exponential on G_N, as §5.1 measures.
- Therefore: (i) DEEP3 is consistent with every published lower bound only because those games are not genome games; (ii) DEEP3 is a
  statement about E-DOM games, and its proof must use E-DOM. A proof attempt that never uses «every e is even and above every β» (or
  graded W-targets) proves a false statement.
- A test for any proposed DEEP3 proof: run its steps on G_N (`T66-depth-check.py lmcs`); the step that fails there is the step that
  must use the genome structure.
- The fleet already has the matching abstract fact from the other side: L-NEW 61's ASC-EXP (box 193 §3: CHAIN-DECOMP + E-MON alone allow
  2^M e-sets when plays visit set bits lowest first, «Friedmann's H1 order») and L-RED 54's LEAK-ARCH (R217 §11). The literature adds
  no E-DOM-compatible counter: I found none.

## 7. Not done, limits
- No genome was built or run here (L-RED 54 did: FPORT_n2-4, R217 §7). No Γ3 run.
- [F09] Fig. 7 not re-read by me; the FHZ papers, Friedmann's thesis chapters on H_n, and the Zadeh / Cunningham / ranking families were
  not re-opened for an E-DOM test.
- «No E-DOM-compatible exponential family is published» is a search result (the sources of T37 and §4), not a theorem.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T66-depth-check.py with the runs of §5; notes/L-LIT.md rows.
- FINDINGS:
  1. HOW3 = Friedmann's I^loc at the movers; the lower bounds for that rule are [F09] Theorem 8 and [F11] Theorem 6.14 only.
  2. None lives in the genome class. Excluding feature: E-DOM. In [F11] Table 4, f_j and k_j (odd) lie above h_i for i < j; the proof
     uses this in Lemma 6.6 (2). Private gates, graded W-targets, [E-LEV], the core and the start do not exclude G_n.
  3. No embedding and no literature kill of DEEP3 / U-FREE. Consistent with L-RED 54's DEAD port (R217 §7).
  4. On G_N itself the chain's other links hold and Deep_c is exponential for each fixed c (DATA N ≤ 8). DEEP3's proof must use E-DOM.
- NEEDS: Lead: (a) pass finding 4 to L-SI box 102 (proof side) as a test: run each step of a DEEP3 proof on G_N. (b) If wanted, L-RED
  can re-run §5.1's counters with its own engine (one engine here). Nothing for the owner.

## Addendum A (2026-11-12, date -u in the commit; append-only, §0-§7 unchanged): §5.1's counters re-counted by an independent engine
- Tool: docs/lit/T66-depth-xcheck.py. No code from experiments/si/si.py. Own value computation (cycle node, Π, length); Odd's optimal
  counterstrategy by BRUTE FORCE over all 2^N choice vectors at e_1 … e_N, the pointwise minimum asserted to exist and to be unique at
  every state; own Howard step. Only the game table (function lmcs, [F11] Table 4) is shared with T66-depth-check.py.
- Result (DATA; unit: Howard run of G_N from ι_(G_N)): for N = 1 … 8 at c = 3 and N = 3 … 7 at c = 9, every counter of §5.1's table
  (T, C, flips, deep, max depth, unm, flips of e_1) is reproduced exactly. Commands: `python3 -I docs/lit/T66-depth-xcheck.py 1 8 3`
  and `… 3 7 9` (a few minutes at N = 8).
- So §5.1's «Limits» line is superseded for the [F11] rows: two engines agree. The switchallexp row still has one engine for flips and
  depth (its T is cross-checked against R118's DATA).

## Addendum B (2026-11-12, date -u in the commit; append-only): E-DOM read off the Zadeh and Cunningham games' own tables (Lead T68 item 3)
No generator and no run: the priorities are read from the papers' tables (PROVED-in-source for the tables; READING for the E-DOM test).
- Disser, Friedmann, Hopp, «An exponential lower bound for Zadeh's pivot rule», arXiv 1911.01074 v2, Table 3.1 and Fig. 3.2 (PDF p.7),
  the sink game S_n. The Odd vertices with a choice are the cycle centers F_(i,j): successors «d_(i,j,0), d_(i,j,1), s_(i,j)», priority
  «6 − 2·j». Their only even successor is the escape s_(i,j), priority «10 − 2·j» (8 or 10), which continues to h_(i,j) («2i + 10») or
  b_1. The selectors g_i have priority «2i + 9» (odd), so every g_i with i ≥ 1 lies above every escape s_(i,j), and g_(i′) lies above
  h_(i,j) for i′ > i. E-DOM fails at EVERY cycle center. The gates are also ternary (two cycle faces), not binary.
- Avis, Friedmann, «An exponential lower bound for Cunningham's rule», arXiv 1305.3944 v1, Fig. 2 (PDF p.12), the game G_n. The Odd
  vertices with a choice are the F_i: successors «h_i, d_(i>1), e_i», priority 6. Escape h_i, priority «2·i + 8» (even), then a_(i+1).
  The g_i have priority «2·i + 7» (odd), so g_(i′) lies above h_i for every i′ > i. E-DOM fails at every F_i except the top one: the
  same pattern as [F11]'s f_j, k_j above h_i.
- Both families defeat single-switch, history-based rules, not Howard (§4), so they were never tests of HOW3. The point here is only
  that the «odd selector above lower escapes» pattern is common to every construction checked: [F09], [F11] §6, the four PGSolver ports
  of §5.2, Zadeh, Cunningham. Not checked: Disser–Loho–Maat–Mosis (ranking rules), van Dijk–Loho–Maat (symmetric), Mei.

## Addendum C (2026-11-12, date -u in the commit; append-only): E-DOM read off the ranking, symmetric and Mei families' own tables (T68 item 3, remainder)
No generator and no run: priorities and costs are read from the papers (PROVED-in-source for the tables; READING for the test). Test as
in Addendum B and §5.2: unit = an Odd vertex with a choice; esc = its successor of largest even priority; listed = odd priorities
above pr(esc). PDFs opened 2026-11-12 (sha256 prefixes in notes/L-LIT.md).
- Disser, Loho, Maat, Mosis, «Lower bounds for ranking-based pivot rules», arXiv 2512.16684 v2 (10 Aug 2026), Fig. 4.1 and the proof of
  Lemma 4.4 (PDF p.13-14), the base game G_n («The games that we use to prove Theorem 4.3 all have the same base structure», p.13):
  «each level i ∈ [n] contains a player 0 node a_i with priority 2i + 1 and a player 1 node b_i with priority 2i + 2»; «a player 1 node
  b_(n+1) with priority 2n + 4 whose only edge ends in the sink»; «the node b_i has two outgoing edges leading to b_(i+1) and
  a_(i+1)». The Odd choice vertices are b_1, …, b_n. esc(b_i) = b_(i+1), priority 2i + 4. Odd priorities above it: a_j with
  2j + 1 > 2i + 4, i.e. a_(i+2), …, a_n. E-DOM FAILS at b_i for every i ≤ n − 2 and holds at b_(n−1), b_n. The escape of a gate is
  itself the next gate (a chain of Odd vertices), which a genome does not allow either (D1 of P-N5-QN: e_g has one in-edge and one
  out-edge). The gadgets added for Theorems 4.2 / 4.3 (Fig. 4.2-4.5, PDF p.16-23) use the priorities 1, 2, 3 below this structure;
  I did not test them one by one. Rule: Bland-type and ranking-based single-switch rules, not Howard.
- van Dijk, Loho, Maat, «The worst-case complexity of symmetric strategy improvement», arXiv 2309.02223, Table 1 (PDF p.9), the game
  G_n: «a_1 Player 0, 3, a_2, d_2»; «a_i, i = 2, …, n: Player 0, 2i + 1, a_1, a_(i+1), d_(i+1)»; «d_1 Player 1, 4, a_2, d_2»; «d_i,
  i = 2, …, n: Player 1, 2i + 2, d_1, a_(i+1), d_(i+1)»; «a_(n+1) Player 0, 1»; «d_(n+1) Player 1, 2n + 4, a_(n+1)». The Odd choice
  vertices are d_1, …, d_n. esc(d_i) = d_(i+1), priority 2i + 4. Odd priorities above it: a_(i+2), …, a_n. E-DOM FAILS at d_i for
  every i ≤ n − 2 and holds at d_(n−1), d_n: the same pattern as the ranking game (which is «adapted from [11]», a binary counter).
  For i ≥ 2 the gates are ternary (two even successors, d_1 and d_(i+1)).
  - Table 2 (PDF p.13), the game for generalized symmetric strategy improvement (N = 16n + 16): Odd choice vertices e_i (14i + 4;
    successors m_i, a_(i+1), both odd: no even successor), f_i (14i + 6; c_i, d_(i+1)), g_i (14i + 8; k_i, h_i, (d_1)), h_i (14i + 10;
    l_i, g_i, (d_1)). esc(f_i) = d_(i+1) = N + 2i + 2, with the odd a_j = N + 2j − 1 above it for j ≥ i + 2: FAILS for i ≤ n − 2,
    holds for f_(n−1), f_n. For i > 1, esc(g_i) = esc(h_i) = d_1 = N + 2, below every a_j with j ≥ 2: FAILS. For i = 1 the escapes h_1
    (24) and g_1 (22) lie below k_1 (25), l_1 (27) and every a_j: FAILS.
  - Rule: symmetric strategy improvement (both players improve), not Howard.
- Mei, «Simple strategy-iteration with Dantzig's rule is not strongly polynomial on turn-based deterministic games», arXiv 2610.27386
  v2 (30 Oct 2026), §3.1 and Table 1 (PDF p.5). NOT a parity game: a discounted turn-based deterministic game with action costs. There
  are no priorities, so E-DOM cannot be read off as above. Table 1: «a_i Player 1, p_i; q_i, 0; 0»; «p_i Player 2, a_(i+1); a_i,
  W_i/γ; −K_i/γ»; «q_i Player 2, b_(i+1); a_i, W_i/γ; −K_i/γ»; «b_i Player 2, a_(i+1), b_(i+1), 0; 0»; «b_(h+1) Player 2, a_(h+1),
  −R»; conditions (5)-(7) (PDF p.6): «W_(i+1) ≥ 4W_i», «K_i ≥ 2K_(i+1)», «R ≥ 4W_h». Player 1 (the minimiser) improves, Player 2
  answers. In the cost reading of E-DOM (the largest scale belongs to the escapes and has the sign that favours the improver) the
  test FAILS: the costs have both signs, and the largest scale is the single terminal cost −R, above every W_i. The paper's own
  description of the mechanism is a cancellation: «a mixed-player cycle created by a Player 1 pivot may be canceled by Player 2's
  optimal counter strategy. … we construct a family in which such cancellation occurs at every iteration» (PDF p.5). Rule: one Dantzig switch per step, not Howard.
- Summary for §4's last-but-one row: of the three families, two are parity games and violate E-DOM at all gates but the top two
  (the «odd selector above lower escapes» pattern again, here with a_j above the lower d's / b's); the third is not a parity game
  and has signed costs with the top scale against the escapes. None is a family for Howard's rule. With Addendum B: every published
  construction checked so far fails E-DOM ([F09], [F11] §6, the four PGSolver ports, Zadeh, Cunningham, ranking, symmetric), and
  Mei's fails its cost analogue. «No E-DOM-compatible exponential family is published» stays a search result, not a theorem.

## Addendum D (2026-11-12, date -u in the commit; append-only): [F11] Table 4 as printed has one priority twice; Figure 4 and Fact 6.1 use other values; no count of §5.1 changes (Lead 14:04Z, from L-COMP 19, claude/l-comp 90874f76 box 43)
- L-COMP's observation is right, and §3's quote is faithful: the collision is in the SOURCE. [F11] = arXiv 1106.0778 v2, Table 4 (PDF
  p.15) prints «a_i … 4n + 2i + 2» and «g_i … 4i + 4», so Ω(g_n) = Ω(a_1) = 4n + 4. This contradicts the paper's own convention
  (§2, PDF p.3: «W.l.o.g. we assume Ω to be injective, i.e. there are no two different nodes with the same priority») and its Fact
  6.1 (PDF p.15: «12·n + 8 as highest priority»; Table 4's h_n is 8n + 4n + 10 = 12n + 10).
- The same paper's Figure 4 (PDF p.16, the game G_3) prints d_i : 3, 7, 11; e_i : 4, 8, 12; g_i : 6, 10, 14; t_1 : 15; a_1 : 16; …;
  a_6 : 26; c : 28; s : 30; r : 32; k_i : 33, 37, 41; f_i : 35, 39, 43; h_i : 36, 40, 44. That is: d_i = 4i − 1, e_i = 4i, g_i = 4i + 2,
  k_i = 8n + 4i + 5, f_i = 8n + 4i + 7, h_i = 8n + 4i + 8 (each 2 below Table 4), and t_i, a_i, c, s, r as in Table 4. These values are
  pairwise distinct and have top priority 12n + 8, as Fact 6.1 says. Schewe–Trivedi–Varghese, arXiv 1501.06484 v1, Figure 2 (PDF
  p.8), reproduce G_3 with the same numbers as Figure 4. READING: Table 4's six formulas for d, e, g, k, f, h are off by 2 (a
  misprint); Figure 4 and Fact 6.1 are the consistent version.
- What changes. The two versions order every pair of vertices the same way except that g_n lies above t_1 and ties with a_1 in
  Table 4's version, and below both in Figure 4's. The remark quoted in §3 («the uniqueness of priorities in the game, implying
  that there are no priorities between f_i and h_i») is true in both (f_i, h_i are adjacent: +9, +10 or +7, +8). The E-DOM test of §3
  and §5.2 is unchanged: for i < j the odd f_j, k_j lie above h_i in both versions.
- DATA (docs/lit/T66-fig4-check.py; engine = T66-depth-check.py's, experiments/si/si.py; unit: Howard run from ι_(G_N)):
  `python3 -I docs/lit/T66-fig4-check.py 1 7 3`. Table 4's version has 10N + 3 distinct priorities on 10N + 4 vertices, Figure 4's
  has 10N + 4. For N = 1 … 7 every counter of §5.1's table (T, C, flips, deep (c = 3), max depth, unm, flips of e_1) is THE SAME
  in both versions (T = 8, 26, 62, 134, 278, 566, 1,142). So §5.1, Addendum A and T67 stand as written; the tie was broken by the
  engines' vertex order without effect. N = 8 and the c = 9 column were not re-run for Figure 4's version.
- For users of `lmcs(n)` in T66-depth-check.py: it implements Table 4 as printed (NOT injective). Use Figure 4's values where a tool
  requires distinct priorities (the six replacements are in T66-fig4-check.py).
