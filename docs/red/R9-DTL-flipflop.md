# R9: the DTL distraction flip-flop as a counter? (L-RED, box 2026-10-16 00:25Z-06:25Z, Lead go 00:25Z)
Candidate: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (L22/L24; statement
docs/alg/DTL-proof.md section 0). Task (Lead 00:15Z/00:25Z): turn the proof lane's observed flip-flop of distraction status
across searches (docs/alg/GAP-A-data.md F8, claude/l-alg d6129e3) into an exponential counter, or say exactly which DTL
mechanism damps it. Status words: DATA (measured, command given) / READING (mine, unrefereed) / OPEN.
Tools (experiments/red/dtl/): dtl_flipflop.py (instrumented run on L-COMP's independent dtl_py.py: pieces, pruning rounds,
forgiveness, tangle births and firings; `--oink` cross-checks tangle/iteration counts with the pinned binary),
dtl_ctxmono.py (Claims P and Q below), dtl_search.py fitnesses iters / restarts / maxrestarts / osc / rep / excess / evens,
option --grow. Instances: experiments/red/dtl/instances/lalg_dtl_restart8_n20.pg and lalg_dtl_pertop31_n18.pg are byte
copies of L-ALG's experiments/alg/instances/dtl_restart8_n20.pg and dtl_pertop31_n18.pg at claude/l-alg d6129e3.

## Verdict (interim; final at the end of the box)
OPEN. No counter built. The flip-flop is real and I can read it off DTL's own data structures (section 2), the per-top
count that motivated it is an artefact of equal priorities (section 1), and every non-monotone event I can produce is
funnelled through one of two mechanisms (section 3). I have not found a mechanism that bounds their composition
polynomially; section 4 states exactly what a counter must do, as the proof lane's target or mine.

## 1. Correction to GAP-A-data F2: "31 tangles at one top" is 31 at one top PRIORITY (DATA)
dtl_pertop31_n18.pg has eight tops of priority 17 (v0, v1, v3, v4, v5, v10, v11, v17). Counting the top as the VERTEX at
which sptl extracted the tangle (dtl_flipflop.py, `== tangles per top`), the counts are 4, 4, 4, 4, 4, 4, 4, 3 (sum 31);
no top vertex learns more than 4 in the whole run (44 tangles, 6 searches). The release trace's "new tangle P" names the
priority P, and dtl_pertop.py keys on it. The same holds for every climbed instance: perhead climbs grown from this
instance reach "90 at one priority" at n = 42 with 19 tops of priority 25 learning 4 each (ph_p31g24: max per top vertex
4); dtl_restart8_n20: max 5 (top v2); the best oscillation climb (osc_r8_s31, n = 20): max 6. So "at most n tangles per
top vertex" is NOT refuted by any instance I have; what IS refuted is "at most n per priority", which only matters if the
proof counts per priority. The reduction of GAP-A-data section 4 should read: tangles <= n * #{(top VERTEX, search) with a
restart} (F3's in-search chain is per vertex, 0 breaks here too).

## 2. The flip-flop in DTL's terms (DATA on dtl_restart8_n20.pg, Even phase, 5 searches)
Notation. A search runs search_rec(G, Even, 0): a sequence of PIECES removed from R into X. The pruning best_vertices sees
only R (forgiveness = "not in R"). Piece kinds: domfirst (result -1 with no vertex of R attracting to X: Dom(prevV) with
prevV = the last survivors of the pruning, the argmax of the pruning round), cut (result -1, X nonempty: the attractor
with the LOWEST threshold t to X, its threshold vertices and their Odd-attractor go to X, the rest is recursed with X = empty
again), stable (result 1: sptl learns tangles at the tops of V*, then Dom(V*) is removed).
Search 0: domfirst {4,9,19}; cut t=11 seed 8 (8 -> 9 in X); cut t=17 seeds {11,18}; stable, V* = 13 vertices, 12 tangles,
among them T6 at top v12 = {7,10,12,13,14,16,17}.
Search 1: in piece 0 the search-0 tangles rescue v2, v15, v19 for more rounds (2@17, 19@17 forgiven), so the LAST survivor is
{4} alone: domfirst {4}. X is smaller, 8 no longer attracts to X, the t=11 cut is gone, 0 and 8 stay in R: v13's exits to 0
and 8 are no longer forgiven, v13 is pruned (domfirst piece 3 removes {0,5,8,13,19}) and v16 (-> 13, 17) too (piece 2
removes {16}). The stable piece's tangle at v12 is {7,9,10,12,14,17}: 9 in, 13 and 16 out (a restart).
Search 2: T18 (top v2's search-1 tangle, escapes {0,4,5,8,13,16,18,19}) fires in piece 2's pruning while 13 and 16 are
still tops, rescues v2 one round, the argmax of piece 2 becomes {15,16}, its Dom removes {0,8,15,16}: 13's exits are
forgiven again, 13 is back in the stable piece: tangle at v12 = {7,9,10,12,13,14,17}.
Search 3: 13 and 16 are rescued in piece 2 (forgiven@17 by the search-2 tangles), argmax {15}, Dom {0,8,15}: 16 stays in R and
is back: tangle at v12 = {7,9,10,12,13,14,16,17}. Search 4: dominion.
Membership of 13, 16 in v12's tangle: (1,1) (0,0) (1,0) (1,1). Each configuration is a NEW set because 9 joined once and
stayed (monotone part); the 13/16 part oscillates. Tangle firing table (dtl_flipflop.py --tangles): 12 of the 36 tangles
never fire after the sptl pass that learned them (T14-T17, T20-T23, T27-T30: their escapes include a vertex that is in
R and uncovered in every later context); the drivers are the top-level tangles T18, T25, T32 (top v2), which fire in the
pruning of pieces 0-2 of the next searches.

## 3. Two claims that hold on all data, and the two sources of non-monotonicity (DATA + READING)
Claim P (context monotonicity). For a fixed player and a fixed subgame R (the whole context of best_vertices), the round in
which a vertex is pruned never decreases from a search to a later search of the same player (survivors = infinity).
Claim Q. For fixed (player, R), a stable result's V* never shrinks.
dtl_ctxmono.py: dtl_restart8_n20 (12 contexts, 8 recurring pairs), dtl_pertop31_n18 (13, 10), tc+ 3 (19, 55), tc+ 5 (59,
156), osc_r8_s31 (15, 12), rep_r8g8_s52 (5, 2), 400 random games n <= 12 (1,154 contexts, 203 pairs): 0 violations of
P, 0 of Q. (L-ALG's F5 is Claim P for R = G only.) The -1 return set (the argmax) DOES change between visits of the same R
(3, 2, 1, 1, 4, 1, 2 changes): that is F7.
Consequences if P and Q are proved (READING):
(a) In a fixed context, pieces are monotone in the tangle set: a cut's seeds and threshold do not depend on tangles at all
    (attracts() is edge-only) and its attractor grows; a stable piece's V* grows and Dom(V*) grows; so for fixed (R, X)
    the only piece that can SHRINK is a domfirst piece (Dom of the argmax survivors; the argmax of a monotone profile is
    not monotone). domfirst happens at the first piece of every search_rec call (depth 0 and every recursion).
(b) A vertex can regress (become a distraction again, leave a top's SCC) in two ways only: (R1) an earlier piece shrank
    (argmax change), so fewer exits are forgiven in its piece (search 1 above: 13, 16); (R2) an earlier piece GREW and
    removed a vertex its good path ran through (an Even-owned vertex whose good successor is now in X is then a cut seed
    at its own priority and moves to an earlier piece). Both change the context R of every later piece.
(c) Tree bound. With R_1 = G fixed for the phase, piece 1's profile takes at most n^2 + 1 values (each change raises a
    round); each value fixes R_2; for each R_2 value piece 2 takes at most n^2 + 1 values; and so on: at most (n^2 + 1)^k
    searches for k depth-0 pieces (k <= n), and the same nesting again inside every cut's recursion. This is exponential
    only if the counter is MULTIPLICATIVE at many levels: every time level i-1 changes, level i must run through many
    states again at a FRESH context R_i, and each state must learn a tangle set never seen before.

## 4. What the counter must do (the requirement; READING)
(1) Reset at level i: when the context R_i is fresh, the tangles learned so far must not fire in piece i's pruning: every
    old tangle relevant to level i needs an escape that is in R_i and uncovered there (R1 makes this possible: the escape
    was forgiven in the old context and is not now; see the 12 never-again tangles of section 2).
(2) Replay at level i: in the fresh context, m new tangles must fire one after another in piece i's pruning, each learned in
    the stable piece of the previous search, each with all its escapes covered at level i (in the regions Z of the
    surviving tops of that round, or in X_i) and at least one escape uncovered at levels < i (else it advances a higher
    level instead; firing while a bit-vertex is still a surviving top is how T18 does it).
(3) Fresh sets: the stable piece's SCC at the readout top must contain a configuration-dependent set (section 2: v12's SCC
    contains exactly the bit vertices still in R at its piece).
(4) Carry: when level i exhausts its m states the next search must advance level i-1 by one argmax change (R1) that makes
    R_i fresh again, and nothing else. tc+ is this structure with ONE level: every search drops one gadget's Z-vertex out of
    the argmax of piece 0 (tc+ 3 search 1 -> 2: survivors {3,4,5,12,22} -> {3,4,5,12}; 22 is then stable in piece 1), and the
    rescues are permanent because the driving tangle (top H's, escapes = the surviving Z's) fires at R = G.
Every one of (1)-(4) is realised somewhere in dtl_restart8_n20 for one step; none is realised repeatedly. Free-form
climbs do not find the composition: fitness iters (searches) converges to chains of self-loop singletons (13 searches at
n = 20, 11 at n = 16, each search one new singleton, linear); fitness rep (repeated learning per top) and perhead are
gamed by equal-priority towers (section 1); fitness excess = searches - distinct learning tops is the measure of
restart-driven searches: chain 2, tc+ 3: -6, dtl_restart8: -9; climbs on it are running at the time of writing.

## 5. Not done / open
- No hand-built two-level gadget yet (reset + replay); section 4 is its specification.
- Claims P, Q unproved; a proof of P would make section 3(c) a theorem and move GAP-A to "polynomially many argmax changes
  per context", which is the open combinatorial core.
