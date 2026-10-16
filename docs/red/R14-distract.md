# R14: van Dijk's "distractingly nice long path" recipe against A_DTL (L-RED, 11:19Z by date -u; produced on Opus 5.5)
Source (Lead 11:05Z, opened by L-LIT 11:01Z under D9; I have not opened it myself, so this file cites it only as the
Lead's verbatim quote): T. van Dijk, "Solving parity games, very slowly", DOI 10.1007/978-3-031-75778-5_21, p.15,
section 6 item 7: "There are also variations that prefer “good paths” where player Even (or Odd) dominates the path
often, and in that case we simply have a distractingly nice long path that eventually leads to a difficult to untangle
higher region of the opponent, while the dominion is small and uninteresting, and always the last choice of the
algorithm." It is prose only, with no game. Solver: pinned A_DTL (`oink --dtl --no-single --no-wcwc --no-loops`, 8fbf0a7).
Status words: DATA / READING. Verdict: no slow-down found. Every reading I built is either neutral or makes DTL FASTER.

## 1. What a "good path" is in A_DTL (code reading, dtl.cpp best_vertices 652-786)
- A p-top u in V is a CANDIDATE in a pruning round when it does not attract into Z, the union of the capped regions of V.
  It is RESCUED when the threshold attractor from Z at some t < pr(u) reaches it, i.e. when p can force a path from u
  into Z through vertices of priority below pr(u). That is the "good path". A candidate that is not rescued leaves V.
  Its death round is the "good path length" (Oink's distance).
- Stable (no candidates) means that every top of V attracts into Z. Then Z is p-closed inside the current R, and every
  cycle in it has a p-top as its maximum. So a top that is not part of a p-closed set in R ALWAYS dies. A good path can
  only DELAY a death. Its lever is the death-round order, i.e. the -1 return set prevV (the argmax) and with it the
  Dom(prevV) piece (search_rec 950-990). That is the death-round mechanism of R10-R13 and L-ALG's Phi / (H) analysis.
- A path is acyclic, so its vertices are in no tangle. Removing its head by Dom(prevV) learns nothing. It changes the
  search only through what the Dom(prevV) attractor (cap pr(head)) takes out of R for the rest of the search.

## 2. DATA (experiments/red/distract/, base region H = Oink's tc+ N, the hardest Oink family for DTL measured here)
Baseline A_DTL on tc+ N: N=2,4,6,8 -> 8, 30, 58, 94 tangles; 5, 10, 14, 18 iterations. All Oink counter_* families
(core, dp, m, ortl, qpt, rob, rr, symsi; N=2..10) are easier (<= 67 tangles, <= 3 iterations). TL on tc N takes
2^(N+1) iterations, DTL takes 6.
distract.py builds H plus a path x_1..x_L (p's parity, priorities rising along the path, so x_1 dies last and is the
argmax), x_L entering H, and a small p-dominion D of the lowest priority. sweep.sh runs it. All runs are verified by Oink.
Here L = N^2, and L = 1 for the qwin rows. Both players were run.
| reading (MODE) | effect on tangles / iterations vs tc+ N, N = 2..8 |
|---|---|
| own / opp / mix (path or H's opponent vertices may move to D or x_1) | identical to baseline |
| chain (path below H), chain-high (path above H) | identical to baseline |
| chain-back, chain-high-back (back edges from every p vertex of H to x_1) | collapse: 0-2 tangles, 1-2 iterations (p's new routes change winners) |
| chain-back-qwin, chain-high-back-qwin (x_L enters only q-won vertices of H; back edges only from p vertices q wins; no winner changes) | FASTER: N=8 9 tangles (baseline 94), 1-3 iterations |
| lure.py (every p-owned p-priority vertex u gets u -> y_u -> s_p, s_p a lowest-priority p-loop: the "small dominion") on tc N | collapse: the dominion is found in iteration 1 and its attractor takes every lured vertex |

## 3. READING: why the recipe does not bite on A_DTL
(i) A reachable small dominion is NOT "the last choice" of A_DTL. A p-dominion inside R is never pruned (its tops always
    attract into their own region), so best_vertices is stable on it and the search removes it. A low priority delays
    nothing.
(ii) A path with no predecessors in H changes nothing: Dom(prevV) from its head attracts only the path.
(iii) Predecessors that give p a real route change the winners (the collapse rows).
(iv) Predecessors that keep the winners (qwin rows) let the Dom(prevV) attractor from the path head remove q-won
    p-vertices of H for the rest of the search. That HELPS DTL: these are exactly the vertices that would be distractions
    in H.
So on A_DTL the good-path preference has no "long path" cost that survives the gauntlet. A working instance would need
the Dom(prevV) piece of a long-lived head to remove a set from H that makes the SAME search learn useless tangles, and
to do so again in later searches. That is the reset-and-replay requirement of R9/R10 (CARRY) again, not a new
mechanism. Lead reading (11:05Z): the item is about DTL-type solvers in general. A_DTL's (i) is a property of this
implementation, so the item may target other "good path" variants. Oink's interleaved variant --idtl (same flags), p=0,
N=4/8: chain is identical to its tc+ baseline (36/118 tangles, 8/17 iterations); the qwin rows are faster (5/9 tangles).
Other variants are not checked.
