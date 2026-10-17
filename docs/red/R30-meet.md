# R30: (MEET) of GAP-C §18r is FALSE on A_DTL, both order data; the run stays complete (L-RED box 7, 11:40Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Target named by the Lead at 11:32Z (date -u): (PHASE-IN-MEET) = (MEET) and (PHASE-IN), as measured by
L-ALG's experiments/alg/dtl_meetd.py (l-alg 2a715cd). Statement killed:
(MEET) search(p) with D := W_p(G') ≠ ∅ learns a new tangle MEETING D, or finds a dominion.

## Instances
- experiments/red/carry/instances/meet_viol_n17.pg (n = 17, 22 edges, sha1 ab3292976a7a7aa9111c227a2535877d6c52c3e6): the shrunk form.
- experiments/red/carry/instances/meet_viol_n29.pg (n = 29, sha1 4796d6b199d5261f6bcb2c784d6ea3d6edd22f03): the climb hit.
Found by dtl_search.py --fitness meet (screen experiments/red/meet/meetfit.py), seed 10001, DTL_ORDER=oink, from
carry/instances/kin_viol_n29.pg, at about 1,000 steps. Shrunk by meet/shrink.py (greedy edge removal, then vertex deletion with
ids compacted in their old order, keeping a (MEET) failure on a complete run in BOTH orders at every step).

## Evidence (every line re-run at this commit)
- L-ALG's dtl_meetd.py, UNMODIFIED (l-alg 2a715cd), on meet_viol_n17, DTL_ORDER=oink and =stable, identical:
  `(MEET) FAILS ... search 0 p=0 |G'|=17 |D|=7 new=[[7, 10, 11, 14]]`; table {(K) holds 5, (MEET) FAILS 1, (MEET) holds 4,
  (IN) FAILS 1, (PHASE-IN) holds 5, (PHASE-IN-MEET) FAILS 1}. No "INCOMPLETE RUN" line. Same verdict on meet_viol_n29
  (search 0, |D| = 8, new = [[10], [10,12,15,16,18,20,22,24,27], [14]] Oink order; the stable order drops 22 from the middle tangle).
- Pinned Oink 8fbf0a7, `oink --dtl --no-single --no-wcwc --no-loops -v`: meet_viol_n17 2 dominions, 4 tangles, solution verified;
  meet_viol_n29 2 dominions, 17 tangles, 9 iterations, solution verified.
- experiments/red/meet/oinkmeet.sh (pinned Oink only, no Python model): parses the `-t -t -t` trace of iteration 0-even, maps
  Oink's internal ids to file ids by reproducing game.cpp:492-495 (std::sort by priority; meet/omap.cpp, same libstdc++), and takes
  W_0(G) from `oink --zlk -v` (verified). meet_viol_n17: W_0(G) = {0,...,6}; iteration 0-even: no dominion, tangles = [[7,10,11,14]];
  "MEET FAILS at search 0". meet_viol_n29: W_0(G) = {0,1,2,3,4,5,7,8}; tangles [[10], [10,12,15,16,18,20,22,24,27], [14]];
  "MEET FAILS at search 0". The Oink tangle contents equal the model's Oink-order output exactly.
- Pinned in experiments/red/check.sh: dtl_flipflop counts for both instances, and oinkmeet.sh on meet_viol_n17 (when Oink and
  g++ are present).

## Run (meet_viol_n17, both orders identical; ids are file ids; * = in D)
| search | p | \|G'\| | D | dominion | new tangles |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 17 | {0..6} | no | {7,10,11,14} (inside W_1) |
| 1 | 0 | 17 | {0..6} | no | {0,2,4,5,6} (inside D) |
| 2 | 0 | 17 | {0..6} | no | {0,1,2} (inside D) |
| 3 | 0 | 17 | {0..6} | yes | {3,4} |
| 4 | 0 | 10 | {} | no | none |
| 5 | 1 | 10 | {7..16} | yes | none |

## Mechanism (L-ALG dtl_step5.py -v, unmodified, search 0)
P piece Dom(prevV) removes {9}; T piece (threshold 29, seed {16}) removes {1*, 16}; one S piece on |R| = 14 with region tops
{4*, 0*, 13, 11, 7, 14, 6*} removes everything else and learns only {7,10,11,14}. Removing the D vertex 1 in the T piece cuts Odd's
escape 2 -> 1. L-RED reading of the trace: inside R, the D vertices 0, 2, 3, 4, 5 are then Even-attracted into the closed region of top 14 (priority 20),
whose core cycle 14 -> 10 -> 11 -> 7 -> 14 lies in W_1; 7's escape 16 left R with the T piece. The extracted tangle is that core
only, so the search learns nothing meeting D. D's own tangles come in searches 1-3.
Game (file ids: priority, owner, successors): 0 4 E {2}; 1 1 E {0,16}; 2 3 O {1,5}; 3 1 E {4,10}; 4 2 O {3,6}; 5 11 E {4};
6 22 E {0}; 7 8 O {14,16}; 8 17 E {14}; 9 18 E {13}; 10 7 E {11}; 11 4 E {7}; 12 15 E {8}; 13 4 E {15}; 14 20 O {10};
15 13 O {12}; 16 29 E {9}.

## Consequences (Lead reading needed)
- (MEET), (IN) and (K-in) all fail at the same kind of search: a T piece removes a D vertex, and D is then absorbed into the
  attractor of a closed region whose tangle core lies in W_{1-p}. A search with D ≠ ∅ can learn only outside D.
- (PHASE-IN) survives, but (L-RED message to the Lead, sent between 11:33Z and 11:36Z by date -u; its header said 11:52Z,
  which was WRONG) it is equivalent to completeness of the phase (dtl.cpp 1068, 1106-1121): within
  one G', p searches again exactly while its last search learned something. It is not a local K step.
- What survives as a K-type step is plain (K) (learn anything, or find a dominion). A GAP-C proof needs a progress measure
  across the searches of a phase that tolerates searches learning only in W_{1-p}.

## Tools (experiments/red/meet/)
meetfit.py (graded screen, same predicates as dtl_meetd.py; LALGM_DIR = an l-alg >= 2a715cd checkout), umeet.py (umix
sampler with meetfit), shrink.py, oinkmeet.sh + omap.cpp (pinned-Oink check); dtl_search.py --fitness meet.
