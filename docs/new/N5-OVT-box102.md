# N5-OVT (box 102): «one fresh entry's wave raises each successor of X past X's current target at most once» is DEAD. In pftheta34_n32, vertex 3 (successors 7, 13) re-enters 7 from 13 twice under ONE root (the fresh entry 7 → 20 at q = 6): once at depth 0 (k = 11) and once at depth 2 (k = 26). In between, a return 7 → 13 belongs to another root. The (left, entered)-pair injection is DEAD on the same instance. What survives on the corpus: CONJECTURE LEVEL-ONCE (one edge returns at most once per (root, depth)) and CASC-EDGE itself (ratio ≤ 1.0)
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 22:42Z: «BOX 102 (proof side) … the missing lemma you named, "one fresh entry's
wave raises each successor of X past X's current target at most once" … If each successor overtakes at most once per root, RET(X; e) ≤ deg X
follows. pftheta34_n32 (X = 3 alternating twice) is the test case. If it fails, give the instance.» Written 2026-10-30 22:43Z-22:5xZ (date -u).
Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Setting, tools
- Box 100's Even root map and box 101's RET(X; e). Tool: experiments/new/box99/retcause.py.
  - The PERROOT line now also prints «max returns of X per root with one (left, entered) pair» and «max returns of one edge per (root,
    depth)».
  - XTRACE=v prints every return of vertex v with its window, first rise, root and depth.
- Corpus re-run (box99/runcause.sh, box101/cause_cascl.txt): 603 W-runs with returns + cascl_K4_m8_N100. Pin: new/check.sh «box 102 OVT».

## 1. The kill (pftheta34_n32, L-RED's red/so instance, default start, one W-run 5-39)
- Vertex 3: Even, priority 27, successors {7, 13}.
- Its switches in the run: k 2 (13 → 7), 5 (7 → 13), 11 (13 → 7), 13 (7 → 13), 26 (13 → 7).
- Returns with their roots (XTRACE=3):
  - k 11: 13 → 7, window from 5, first rise at 6, root FRESH (7 → 20 at 6), depth 0;
  - k 13: 7 → 13, window from 11, first rise at 12, root FRESH (13 → 30 at 12), depth 0;
  - k 26: 13 → 7, window from 13, first rise at 15, root FRESH (7 → 20 at 6), depth 2.
- Under the root e = (7 → 20 at 6), a switch of X's own successor 7, the successor 7 overtakes 13 at X TWICE (returns at 11 and 26). The
  counter-overtake at 13 is rooted at a different fresh entry.
- DEAD:
  - «per root, each successor of X overtakes X's current target at most once» (the Lead's route);
  - «per root, X's returns have pairwise distinct (left, entered) pairs». Both returns above are (13 → 7). Corpus: 17 W-runs in 10 games
    (the same list as box 101's left-target kill).
- Why the route fails: a root's subtree is not an interval of time. Its returns interleave with other roots' returns, and a deep chain
  (depth 2 here) can bring the same wave back to X after another root has undone it. So an ordering argument «per root» has nothing
  monotone to work with. Ξ(7) and Ξ(13) both only rise, but the overtakes alternate under two different roots.
- CASC-EDGE itself survives here: RET(3; e) = 2 = deg 3. The kill shape for CASC-EDGE is the same mechanism with a third alternation
  under e, e.g. one more depth level. Not built (L-RED's line).

## 2. What survives (DATA) and the resulting statements
- CONJECTURE LEVEL-ONCE: every Even edge (X, g) has at most one return rooted at e at each chain depth d.
  - DATA: max 1 on all 604 W-runs. topfix_n10's 17 returns of one edge under one root sit at 17 different depths. pftheta34_n32's two
    returns are at depths 0 and 2.
- Corollary (PROVED, lane, from LEVEL-ONCE): RET(X; e) ≤ deg(X)·(D_e + 1), where D_e is the depth of e's root tree. So
  CASC_F(e) ≤ m_E·(D_e + 1), and |F| ≤ (m_E − n_E)(1 + m_E·(D + 1)).
  - This is polynomial iff the root depth D is. topfix_N has D = 6N − 11, linear, so it is fine.
- A proof attempt for LEVEL-ONCE does not go through. Two same-depth returns of one edge have disjoint windows, so their first rises
  q₁ ≠ q₁′ (CHILD). But their chains to e are different node sequences of the same length, and nothing forbids two such chains. No
  instance has them. NOT proved.
- So the open core, from the proof side, is now:
  - CASC-EDGE (RET(X; e) ≤ deg X, tight); or
  - LEVEL-ONCE + DEPTH-POLY (root depth polynomial; depth is ≤ |F| trivially, so this is circular unless proved separately).
- Neither is proved.

## DONE / FINDINGS / NEEDS
- DONE: this note; retcause.py (pair and (root, depth) counters, XTRACE); corpus re-run; new/check.sh «box 102 OVT». SHA: see the commit.
- FINDINGS:
  - DEAD: «each successor overtakes at most once per root», on pftheta34_n32: vertex 3 re-enters 7 from 13 twice under root (7 → 20 @ 6),
    at depths 0 and 2.
  - DEAD: the (left, entered)-pair injection (same instance; 10 games).
  - CONJECTURE LEVEL-ONCE (604 / 604 W-runs). PROVED (lane): LEVEL-ONCE ⇒ RET(X; e) ≤ deg X·(D_e + 1).
  - CASC-EDGE: still a CONJECTURE, tight.
- NEEDS: Lead: L-RED kill shape for CASC-EDGE: pftheta34's alternation with one more depth level (a third 13 → 7 return under the same
  root).
