# N10 screen (round 2): one-player-exact approaches, tested on two-player games (L-NEW successor 7, Opus 5.5, D15; box 19)
Lead GO 2026-10-23 19:45Z (date -u). Same four fields per approach as N9 ((a) barrier, (b) reading, (c) test, (d) cost), plus the
Lead's two lessons. L1: local-improvement potentials get lapped by counters with delay lanes (R53/R56). L2: a relaxation that is
inexact on ONE-PLAYER games wastes levels (one-player parity is polynomial), so a candidate must be exact there by construction or by
a short proof. Each entry says how it handles L1 and L2. Nothing is frozen; no running-time claim is made.
Labels: PROVED (full argument here), DATA (committed script reproduces it), READING, OPEN.
Honesty note on the ranking: the three tested entries were designed in sequence during the box, each in answer to the previous
one's failure (N10a -> N10b -> N10c); the table gives the order in which I would now spend a box, not a ranking made before any test.

## Ranking
| rank | id | approach | L1 (progress) | L2 (one-player) | two-player test result (DATA) | cost |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | N10c | conditioning (self-reduction) on the N10b oracle | Even vertices fixed one by one (<= n steps; no potential) | exact, PROVED (Lemma D) | STUCK on 1 of 8,000 random games (r1569, n = 14; 0 of 6,000 with n <= 10) and on counter_symsi N = 3 | done (1 h) |
| 2 | N10b | ACYC + ESCAPE cuts, families ESC1 and ESC-tau (tau = rounded Odd-side REGION LP) | one LP with cutting planes (no potential) | exact, PROVED (Lemma B) | 3 gaps in 5,432 random queries; gaps on counter_symsi N = 2, 3 (Q3); 0 in 17,528 exhaustive (n = 3) | done (40 min) |
| 3 | N10a | ACYC + ESC1 cuts only | as N10b | exact, PROVED (Lemma B) | 15 gaps in 800 random queries | done (30 min) |
| 4 | N10d | ESC-tau with tau from a RECURSIVE call (exact separation for (U, tau)) | recursion | exact | not run: exact (U, tau) separation is the problem itself; recursion = Zielonka-type (B5 families) | > 3 h |
N9c (simulation kernel) and N9d (tropical shadow vertex) stay out: N9d is a local pivot rule (L1 applies, no argument against a
lapping counter), and N9c has no one-player exactness argument (L2).

## 0. Common objects (code: experiments/new/esc/, reusing experiments/new/sa/sa.py's ACYC and peel.py's REGION LP)
- Query: "Even wins every vertex of G". ACYC(G) as in N9-screen.md §1(e) (Lemma A there: integral ACYC feasible iff Even wins all),
  here at level 0 (s_e relaxed to [0, 1]), M = n + 1.
- U0(G) := V minus every vertex lying on a cycle of G whose maximum priority is even (equivalently: in the same SCC of G[pr <= p] as a
  vertex of even priority p, that SCC containing a cycle). For an Odd strategy tau, U0(G, tau) := the same for G_tau (Odd vertices
  keep only their tau-edge, Even vertices keep all edges).
- ESCAPE cut for (U, C): U nonempty, U subset of U0 (resp. U0(G, tau)), U closed under C(v) for Odd v in U, where C(v) = all
  successors (family ESC1) or C(v) = {tau(v)} (family ESC-tau):
      sum over Even v in U, u not in U, of s_vu >= 1      (a single-successor Even edge counts as the constant 1).
- Lemma B (PROVED). (i) Every ESCAPE cut is valid for every integral point of ACYC. (ii) ACYC + all ESC1 cuts is exact on one-player
  games of either owner; the separation loop of §1(e) decides it exactly there.
  Proof. (i) Let sigma be integral with "Even wins all", and suppose sigma keeps every Even vertex of U inside U. In G_sigma (ESC1)
  or G_{sigma,tau} (ESC-tau) restricted to U, every Even vertex has its sigma-edge in U and every Odd vertex has an edge in C(v),
  inside U; so this finite graph has out-degree >= 1 and contains a cycle. That cycle is a cycle of G (resp. G_tau) inside U0 (resp.
  U0(G, tau)), hence its maximum is odd. In the ESC1 case Odd follows the cycle, in the ESC-tau case Odd plays tau: either way a play
  from U under sigma stays in U and ends in odd-max cycles, so Odd wins somewhere: contradiction. So some Even vertex of U leaves U,
  and the cut's left side is >= 1. (ii) Odd-only games: ACYC has no binary variables, so it is exact by Lemma A and the valid cuts
  change nothing. Even-only games: if Odd wins some vertex, let W = W_O != empty. No cycle inside W has even maximum (its vertices
  would be won by Even), so W subset of U0; the Odd-closure is vacuous; no Even edge leaves W (W is an Even trap). The cut for U = W
  reads 0 >= 1. In the loop, for w in W the minimum cut has value 0 < 1 at every iteration, so the loop never stops with "feasible";
  the family is finite, so it stops with "infeasible". []
- L1 for N10a/N10b: the procedure is one LP over a fixed polytope (ACYC intersected with a finite family of valid cuts), solved by
  a cutting-plane loop whose separation is an exact minimum cut (one per w in U0). There is no strategy that improves step by step
  and so nothing a counter could lap; a failure is a GAP (the polytope is non-empty while Odd wins somewhere). The number of loop
  rounds is DATA only (no bound claimed).

## 1. N10a (rank 3): ACYC + ESC1
(a) Barrier: none of B1-B21 is about LP relaxations with exact separation (as N9a, N9-screen.md §1(a)); L2 is met by Lemma B (ii),
  the failure of N9a. (b) Reading: the one-player obstruction of N9a (functional graphs, every cycle odd) is exactly an ESC1 cut, so
  the circ family is cut off at once. (c) Test: one-player corpus, circ, two-player random (four queries per game as in sa/gaps.py).
  (d) Cost: 30 min.
(e) Pseudocode: esc.py esc_feasible(g) with taus = (): LP(ACYC level 0 + cuts); for each family and each w in its U0, minimum s-t
  cut (networkx) with w forced in, vertices outside U0 forced out, infinite arcs v -> u for Odd v and u in C(v), capacity s_vu on
  Even arcs; add every cut of value < 1 - 1e-6; repeat until none (answer feasible) or LP infeasible.
(f) Results (DATA; esctest.py; no yes-instance was ever infeasible, asserted):
  - circ(n,1,2), n = 3..10 (sa/instances): exact on all 16 queries (results/circ.txt).
  - One-player corpus: 200 random games made Even-only and the same 200 made Odd-only (n = 2..12): 924 queries, 0 gaps
    (results/oneplayer_400.txt). This is Lemma B (ii) on data.
  - Two-player random, seeds 0..299, n = 3..12: 15 gaps in 800 queries (results/rand300.txt). 12 of the 15 gap runs never found a violated
    ESC1 cut at all (cuts = 0). READING: once Odd has choices, Odd's winning region contains vertices on even-max cycles of G (Odd
    avoids them), so it is not inside U0 and ESC1 cannot see it. DEAD as a candidate (gaps on two-player games).

## 2. N10b (rank 2): ACYC + ESC1 + ESC-tau
(a) Barrier and L1/L2: as N10a (Lemma B covers ESC-tau). (b) Reading: for tau = an Odd winning strategy tau* on W_O, the
  ESC-tau cut for U = W_O is 0 >= 1 (W_O is inside U0(G, tau*) because every cycle of G_tau* through W_O stays in W_O and is odd),
  so the polytope is exact whenever the guessed tau wins somewhere relevant. The guess comes from the Odd-side REGION LP of box 18
  (peel.py region_lp_sigma on the dual game, levels 0 and 1, argmax rounding); unlike N9b the guess need not win anywhere by itself,
  because the cut search ranges over every U for that tau.
(c) Test: as N10a, plus 2,000 random games n <= 14, a 1-in-10 sample of every 3-vertex game (priorities <= 2), the hard families'
  smallest members (Oink generators @ 8fbf0a7, as in N9-screen.md §2(f)) and the pinned N9b STUCK games. (d) Cost: 40 min.
(f) Results (DATA; esctest.py --tau):
  - random seeds 0..299 (n 3-12): 0 gaps in 800 queries (results/rand300_tau.txt).
  - random seeds 1000..2999 (n 3-14): 3 gaps in 5,432 queries (results/rand2000_tau.txt): r1649 Q3 (n = 12), r1794 Q1 (n = 8),
    r2939 Q1 (n = 12); all three runs found no violated cut at all (cuts = 0). Pinned: instances/esc_gap_r1794_Q1.pg (sha1
    ab859e3f4acf4ca223bc7af905010d59db758d66; Oink zlk: Even wins only vertex 5 of 8) and esc_gap_r1649_Q3.pg (sha1
    7ca8f9d613fbe0698c92b1b90873b066fb24c916; the queried game is won by player 1 everywhere).
  - exhaustive n = 3, priorities <= 2, every 10th game (7,409 games): 0 gaps in 17,528 queries (results/exh3_stride10_tau.txt).
  - hard families' smallest members (28 games as in N9-screen.md §2(f)), switchallexp N = 3 and the four pinned N9b STUCK games:
    72 queries, 2 gaps, both on the Odd query (Q3) of counter_symsi N = 2 (n = 22) and N = 3 (n = 32) (results/hard_tau.txt).
    The four N9b STUCK games (peel_r26, r90, r1147, r2136) are exact under N10b.
  DEAD as a candidate (gaps on two-player games, smallest n = 8), though far stronger than N9a level 1 (44 gaps in 8,196 queries
  on the 3,000-game corpus of box 18) and N10a.

## 3. N10c (rank 1): conditioning on the N10b oracle (the N9b variant "rounding by conditioning", made one-player exact)
(e) Pseudocode (cond.py). Query "Even wins every vertex of G". O(H) := N10b's answer on H. If O(G) is infeasible, answer NO. Else,
  for the Even vertices v with >= 2 successors in index order: try v's successors u in order of decreasing LP value s_vu (from the
  last feasible oracle LP; ties by index); keep the first u with O(G with v's edges cut to {u}) feasible; if there is none, answer
  NO (STUCK). After the last vertex, return sigma and check it with a one-player solve (asserted).
- Lemma D (PROVED). (i) A YES answer is correct (sigma is checked, and in fact the final game is Odd-only, where O is exact).
  (ii) On a game where Odd wins some vertex the answer is NO: every game O accepts along the way is a restriction of G, Odd still
  wins somewhere in it, and the final Odd-only game is decided exactly, so the run cannot end with YES. (iii) Errors are therefore
  one-sided: STUCK (NO) on a game Even wins everywhere, when O accepted an edge that loses. (iv) On one-player games N10c never
  errs: Odd-only games have no choices; on Even-only games every restriction is Even-only, where O is exact (Lemma B (ii)), so O
  accepts only edges that keep "Even wins all", and the winning sigma's edge is always available. []
(a) L1: progress = number of fixed Even vertices (<= n), each step one oracle call; no potential, nothing to lap. L2: Lemma D (iv).
  Barrier: the oracle's gaps (§2) are the only failure source; B7-type incompleteness shows up as STUCK runs.
(b) Reading: conditioning turns a rare two-sided gap of O into a rarer one-sided error: it errs only if O wrongly accepts an edge AND
  no later rescue exists.
(c) Test: YES-instances, where it can fail: for each random game G, the Even query on G[W_E] and the Odd query on G[W_O]
  (= Even query on the dual of G[W_O]); NO-instances G (both regions non-empty) checked to give NO. (d) Cost: 1 h.
(f) Results (DATA; condtest.py):
  - random seeds 0..99 (n 3-10): 127 YES-instances solved, 0 STUCK; 27 NO-instances answered NO.
  - random seeds 1000..2999 (n 3-14): 2,715 YES-instances solved, 1 STUCK; 716 NO answered NO; 9,200 oracle calls; 530 s
    (results/cond_rand2000.txt). STUCK: r1569, the Even query on G[W_E] = G (n = 14, Even wins every vertex; Oink zlk agrees):
    instances/cond_stuck_r1569_YE.pg (sha1 c7715537ff454341b3309ea058796c1f759c1ba6); cond.condition returns STUCK after 7 calls.
  - random seeds 5000..10999 (n 4-10): 8,022 YES-instances solved, 0 STUCK; 2,022 NO answered NO; 24,014 oracle calls; 734 s
    (results/cond_rand6000_n4-10.txt).
  - Where r1569 fails (trace1569.py, results/trace1569.txt): v = 2 -> 3 is accepted correctly; v = 7 -> 10 (LP value 0.967) is
    accepted although the restricted game is lost by Even everywhere (Zielonka and Oink zlk: player 1 wins all 14 vertices);
    the run is then STUCK at v = 10. That restricted game is an N10b gap at n = 14:
    instances/esc_gap_from_r1569.pg (sha1 194a1ff6c5d83307f221180b39cdba11eb891c06). The oracle's LP point passes a residual check
    (<= 1e-6, esc.py), so the gap is not a tolerance artefact of the final point.
  - Hard families' smallest members + pinned games (condtest.py files, results/cond_hard.txt): STUCK on counter_symsi N = 3, the
    Even query on G[W_E] (n = 32, Even wins every vertex; Oink zlk agrees): instances/cond_stuck_symsi3_YE.pg (sha1
    4483eb7c813989cb79edf76c6e604367d39db75a). Every game before it in argument order (counter_core, _dp, _m, _ortl, _qpt, _rob,
    _rr N <= 3 and counter_symsi N = 1, 2) finished without STUCK. The run was stopped at 20:58Z after about 49 min, so the games
    after it (tc, tc+ N = 1, 2, switchallexp N = 3, pinned games) are NOT FINISHED. Re-run from the pinned file:
    STUCK after 14 oracle calls, 770 s, with the residual check on (results/cond_symsi3_repro.txt).
  Verdict: DEAD as stated (STUCK yes-instances r1569, n = 14, and counter_symsi N = 3, n = 32). Not a region algorithm either: it answers only the "Even wins all"
  query; regions would need a REGION version (OPEN, not built).

## 4. N10d (rank 4, not run)
Exact separation for the ESC-tau family needs the pair (U, tau) with U an Odd-winning, Even-closed set under tau: that is an Odd
dominion, i.e. the problem itself. A recursive separation (solve smaller subgames to propose tau) is a Zielonka-type recursion and
meets the B5 families (Friedmann; Benerecetti-Dell'Erba-Mogavero) with no argument against them. Not proposed for a box.

## 5. What box 19 says (READING)
- Lemma B shows that one-player exactness is cheap to buy (ESC1 is a min-cut family) and that the remaining two-player gap is
  "guess Odd's strategy": every N10 failure is a game where no LP-guided tau exposes a violated cut. The two-player difficulty
  is back in the choice of tau, which the cut family cannot supply by itself.
- No candidate is live. Nothing frozen. No running-time claim.

## 6. Sources
No external source is cited in this file beyond those opened in box 18 (N9-screen.md §7). Fleet files read: N9-screen.md,
docs/agents/DE31-32-draft.md, docs/red/R53-n8a-counter.md, docs/red/R56-r2-vj-switchsets.md §4.
