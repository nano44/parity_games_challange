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

## Verdict (interim 2, 01:15Z my clock; final at the end of the box)
OPEN. No counter built; no polynomial damping found. What is established (data) and what is handed over (statements): The flip-flop is real and I can read it off DTL's own data structures (section 2), the per-top
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

## 2b. The 16-search Even phase of L-ALG's dtl_searches20_n32.pg (claude/l-alg f2704d7; DATA)
My tracer: 124 tangles, 1 dominion, 20 iterations (MATCH with Oink); Claim P/Q: 62 contexts, 74 recurring pairs, 0
violations, 20 argmax changes. The first best_vertices call returns -1 in all 16 Even searches; its profile advances at
searches 2, 5, 9/10, 13/14 (Claim P: only upward). `--diff` (first depth-0 piece that differs between consecutive
searches): 0->1:5 1->2:0 2->3:3 3->4:0 4->5:0 5->6:2 6->7:= 7->8:= 8->9:0 9->10:= 10->11:= 11->12:= 12->13:0 13->14:2
14->15:0. So depth-0 piece 0 (a domfirst) moves 6 times; inside each epoch the progress is in later pieces or inside the
recursion of the big cut (t=31, 23 vertices): a two-level cascade with epochs of 1-4 searches, not a counter. The readout
tops v23/v19 (pr 28) learn 12 tangles each, restarting 6 and 5 times: v23's sets wander through 12 configurations
({18,19,23,28,29}, then 16, 15, 19, 20, 19, 13, 16, 10, 10, 11, 20 vertices; v17, v7, v13, v16, v27, v24, v4, v12, v20,
v22, v30, v10 flip in and out), each new. Per top vertex: 12 at n = 32 (so far the largest per-vertex count I have seen; still
below n). Climbs seeded with it (fitness iters, Oink): 22 searches at n = 32 and at n = 40 (--grow 8) after ~5k steps.

## 3. Two claims that hold on all data, and the two sources of non-monotonicity (DATA + READING)
CORRECTION (2026-10-16 ~08:50Z, L-RED successor, produced on Opus 5.5): Claim P is FALSE for A_DTL itself. L-ALG's
instance experiments/alg/instances/dtl_mviol_n20.pg (claude/l-alg 6f19541, sha1 4cb3335f) has the same context R = G' at
iterations 3-odd and 4-odd with a growing tangle set and three first-call distances going DOWN (L-ALG docs/alg/GAP-A-M.md
section 4b, read off Oink's own trace). Independent re-check with this lane's tools: `dtl_ctxmono.py` on that file reports
21 contexts, 17 recurring pairs, 15 Claim P violations, 0 Claim Q violations; `dtl_flipflop.py --oink` MATCH (1 dominion,
17 tangles, 6 iterations). The "0 violations" lines below stay as DATA for the games they name. They were never a proof:
the adversarial climbs of v3 used Even-only fitness and did not reach the straddle shape (L-ALG Lemma E). Consequence (c)
(the tree bound) and every "monotone in a fixed context" step below are therefore unproved for A_DTL. Claim Q has 0
violations on this instance; L-ALG's synthetic shape (GAP-A-M.md section 4) breaks it for injected tangle sets only.
Claim P (context monotonicity). For a fixed player and a fixed subgame R (the whole context of best_vertices), the round in
which a vertex is pruned never decreases from a search to a later search of the same player (survivors = infinity).
Claim Q. For fixed (player, R), a stable result's V* never shrinks.
dtl_ctxmono.py: dtl_restart8_n20 (12 contexts, 8 recurring pairs), dtl_pertop31_n18 (13, 10), tc+ 3 (19, 55), tc+ 5 (59,
156), osc_r8_s31 (15, 12), rep_r8g8_s52 (5, 2), 400 random games n <= 12 (1,154 contexts, 203 pairs): 0 violations of
P, 0 of Q. (L-ALG's F5 is Claim P for R = G only.) The -1 return set (the argmax) DOES change between visits of the same R
(3, 2, 1, 1, 4, 1, 2 changes): that is F7.
Adversarial tests of P/Q (DATA): hill-climbs with fitness 100*(P+Q violations) + recurring pairs/1000 at n = 12, 16 (also
with self-loop and renumbering mutations), from dtl_restart8_n20 and dtl_searches20_n32: 0 violations in every run (fitness
never reached 1); random: 3,000 games n <= 16 (10,060 contexts, 2,079 recurring pairs) and 1,500 games n <= 24 (6,098
contexts, 1,703 pairs): 0 violations.
Proof route for Claim P (READING, unrefereed, for the proof lane): fix R and T subset of T'. Induction on the round r with the
hypothesis V_r(T) subset of V_r(T'). (i) Z_r(T) subset of Z_r(T'): every vertex of a T-region of top tau is attracted under T'
either to tau or to a higher top tau' in V_r(T') whose region consumed a vertex on its path (an Even-owned vertex with an
edge into the consumed part is attracted to tau' directly, pr <= pr(tau') since pr <= pr(tau); an Odd-owned vertex whose
exits split between tau'-region and tau-region is attracted to tau because consumed exits are forgiven, dtl.cpp 85-93);
tangle attraction is monotone in T and in Z. (ii) attracts(v, Z, R) is monotone in Z (41-56), so every T'-candidate in
V_r(T) is a T-candidate. (iii) the threshold attractor is monotone in Z and T, so a T'-candidate not forgiven under T' is
not forgiven under T. Hence a vertex pruned at round r under T' is pruned at round <= r under T. Claim Q and the "-1 return
set = argmax" statement follow. Step (i) is the only step with content (the consumption order).
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
Every one of (1)-(4) is realised somewhere in dtl_restart8_n20 for one step; none is realised repeatedly.
Lemma W (Lead 00:52Z, proof lane): each top extracts at most once per search (sptl 528-529, W.reset 1016), so
tangles <= n * searches and GAP-A is exactly the number of search calls per phase. (My per-top-vertex counts agree: the
in-search "chain of 8" at one priority is 8 tops.)

## 4b. Blueprint of a two-level reset+replay gadget (READING; the construction I tried to assemble, with the facts that
decide each step; not built within the box)
Facts used (dtl.cpp, read): (f1) attractTangle fires only if every tangle vertex not yet in Z is in R and has priority <=
the threshold, and every escape is in Z or outside the subgame (109-185): a stored tangle with a vertex in X is DEAD in that
context, whatever its escapes. (f2) In piece 0 (R = G) nothing is forgiven: a driver that is to move level 0 must have all
its escapes inside the regions of tops that still survive at that round (tc+: the Z vertices). (f3) Coverage is monotone in
X: "covered iff state = j exactly" cannot be expressed through escapes; selectivity therefore comes from (f1), not from
escapes. (f4) In piece 0 a stable top needs a closed region; without an existing tangle that means an Even-closable cycle,
which is a dominion unless it has an escape, and an escape in piece 0 must be a surviving top (f2): so the first stable
vertex of a phase needs a driver learned under forgiveness in an earlier search. (f5) A vertex whose only good successors
have moved into X becomes a cut seed at its own priority (R2) and lands in a piece before the stable one. (f6, the LIFT; the
source of "covered in a later piece, not in an earlier one", read off tc+ 3 search 2: Z=22 pruned at piece 0 round 5,
stable at piece 1) An Odd-owned vertex v with an exit into a LOWER alive region is attracted only into a region computed
after that one (exits into higher, already consumed regions are forgiven, dtl.cpp 85-93; exits into lower, not yet
computed regions are escapes), so v lands in a low region and a higher-priority vertex w -> v cannot follow (max_prio,
line 73). When the lower region's top is removed with its piece, v is attracted into the high region and w follows: in
tc+, 2 (Even-0-T, exits to the Z tops 3,4,5) joins the low region of Z=3 at piece 0, blocking 1 (pr 15), so T2's escape 1
is uncovered and Z=22 is pruned; at piece 1 the Z's are gone, 2 joins H=0's region, 1 follows, T2 fires, 22 is stable.
(f7, zombies) An Odd-owned vertex all of whose successors are in X is never attracted in a stable piece (attraction runs
over predecessors of popped vertices) and is never covered; it is removed only by a cut. (f8, shared Z) A top is a
candidate only if it has no successor in the UNION of all alive regions; a low alive top whose region absorbs the
deadlock cycle rescues every higher top pointing into it, so a delay gadget must keep its low top dead at the piece where
the delay is needed.
Level H (monotone, tc+-like): tops a_1..a_m whose driver tangles T_j = {a_j, u_j, w_j} (a_j -> w_j, w_j Odd -> {a_j, u_j,
o_j}, u_j -> w_j and u_j -> a_j so that T_j can be learned in a stable piece where o_j is forgiven) make a_j a permanent
member of V* once T_j exists and o_j is covered in piece 0; by (f2) o_j must be a surviving top, so T_j's permanence rests on
a top that is itself never pruned, which is the circularity (f4): tc+ resolves it by letting the H-drivers fire only while
the Z tops survive and making the argmax, not a stable set, carry the state. State j = {a_1..a_j} in P1 = Dom(V*) (or in the
argmax); P1 grows (or moves) so R_2 is fresh at every step.
Level L (replayed): bits b_1..b_k, b_i -> y_i (Odd, pr 1) -> {b_i, b_{i-1}} with b_1's y_1 -> p where p is a cut seed in
every state (p -> g, g in P1 always), so at level L's piece the bits form a pruning chain (rounds 1..k) and bit b_i is
rescued at round <= its own only when a driver D_{i-1} containing b_{i-1} fires at that round (y_i is then attracted at
threshold 1). D_{i-1} is the readout SCC of the previous search: it contains the ON bits, the witness vertices g_{j'} (Even,
pr 1, g_{j'} -> a_{j'} and -> the readout top) of all states j' > j, and the hub; by (f1) every state-j driver DIES in state
j+1 because g_{j+1} moves into P1 = Dom(V*_{j+1}) (reset), and the state-(j+1) drivers are fresh sets because they lack
g_{j+1} (freshness). The carry (advance H exactly when L is exhausted) is the step I could not close on paper: the driver
that moves a_{j+1} into V* must fire in piece 0 with no forgiveness (f2), so its escapes must be surviving tops, while the
L-drivers must not do the same; and the full-count readout tangle, the only fresh tangle available at that moment, carries
the L-bits' Odd exits (to p and the chain) as escapes, which are uncovered in piece 0. I did not find a wiring that
satisfies (f2) for the carry driver and keeps the L-drivers off piece 0 at the same time; this is the one concrete
obstacle met, stated as a property to prove or refute:
  (CARRY) In piece 0 of a search without dominions, a stored tangle fires only if all its escapes are in the regions of the
  tops still alive at that round; a tangle learned in a stable piece deeper in the previous search has as escapes the
  Odd exits of its SCC into that piece's context, so it fires in piece 0 only if every such exit leads to a vertex that is
  attracted to a top alive at that round. A counter needs, at every carry, a fresh tangle with this property whose
  firing changes the argmax (or V*) of piece 0; tc+ provides exactly N of them (one per gadget, the Z's as escapes) and
  then stops. Whether the number of such carries can exceed poly(n) is the open core; nothing in my data shows more than
  6 argmax changes of piece 0 in a phase (dtl_searches20_n32). Free-form
climbs do not find the composition: fitness iters (searches) converges to chains of self-loop singletons (13 searches at
n = 20, 11 at n = 16, each search one new singleton, linear); fitness rep (repeated learning per top) and perhead are
gamed by equal-priority towers (section 1); fitness excess = searches - distinct learning tops is the measure of
restart-driven searches: chain 2, tc+ 3: -6, dtl_restart8: -9; climbs on it are running at the time of writing.

## 4c. Hand-built attempts (DEAD, with the instance; generator experiments/red/dtl/gens_ff.py)
- hdelay m K (`gens_ff.py hdelay 3 2`, 29 vertices): ladder h_j -> q_j -> r_j -> {e_j, x_j, g_{j-1}}, x_j -> r_j, meant to
  give a one-search delay per step via the tangle {x_j, r_j}. Result: 0 tangles, 2 iterations, Even wins nothing (every
  Odd vertex reaches the sink through the timer chain), and before that the h's outlive the timer top in piece 0 (their
  pruning cascades from z0's uncovering: h_0 round 4, h_j round 4+j) so the argmax is {x_3, h_3}, not c_K. Two design
  errors, both general: (f8) x_j is an alive low top at round 0 and its region {x_j, r_j, q_j} puts q_j into the shared Z,
  so h_j is never a candidate (no delay); and a counted player must be able to win something, so the timer chain cannot
  end in the opponent's sink.
- Second design (paper only, not run): witness r_j -> h_{j-1} directly (covered iff h_{j-1} alive or in X), priorities of
  the h's decreasing so the witness is consumed before h_j's region, e_j -> tau for coverage at the learning piece. It fails
  on (f8) again: the learning top b_j must be alive at the learning piece and dead at piece 1, which needs an exit covered
  at piece 2 and not at piece 1; the only such source is the LIFT (f6), which needs a high top alive at piece 2 that is not
  in P2, i.e. a top pruned at piece 1 and stable at piece 2, the thing being built. The regress is not infinite (tc+
  realises one level of it with the Z tops and the T/I pair) but I did not close it in the box.

## 5. Not done / open
- No hand-built two-level gadget (reset + replay); sections 4/4b are its specification and the obstacle (CARRY).
- Claims P, Q unproved; a proof of P would make section 3(c) a theorem and move GAP-A to "polynomially many argmax changes
  per context", which is the open combinatorial core.
- Searches per phase: best known 16 (Even phase of dtl_searches20_n32, L-ALG), 22 total at n = 32/40 by my seeded climbs; the
  singleton chain gives n/2 + O(1) trivially; tc+ gives 2N+2 at n ~ 17N^2. No family with searches growing faster than
  linearly in n is known to me.
