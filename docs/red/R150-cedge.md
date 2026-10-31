# R150: CONJECTURE CASC-EDGE (L-NEW 40, box 101: RET(X; e) ≤ deg X) is DEAD. On cedge_n32 (n 32, one W-run of 26 transitions) Even vertex 7, of out-degree 2, returns FOUR times under ONE fresh root (the entry 20 → 7 at q = 9): 26 → 20 → 26 → 20 → 26 at k = 14, 17, 20, 22, at chain depths 0, 1, 2, 3. RET/deg = 2.0, by L-NEW's own retcause.py (l-new 457e41fe, unchanged); xeng identical; Oink OK. LEVEL-ONCE survives here (each edge's two returns sit at different depths). Found by a hill-climb from L-NEW's near miss pftheta34_n32
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 23:10Z: «NEXT BOX R150, your proposal: a CASC-EDGE kill by deliberate oscillation. Two
descendants of ONE fresh root leapfrog Ξ at X's two targets, so that X re-enters one target twice under one root. … The kill is that mechanism
with the counter-overtake ALSO under the same root. … L-NEW's CONJECTURE LEVEL-ONCE … is the next fallback; kill it too if you can.»
Written 2026-10-30 from 23:20Z (date -u).
- Labels: DEAD (with instance) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened: l-new 457e41fe docs/new/N5-OVT-box102.md (all); experiments/new/box99/retcause.py at 457e41fe (PERROOT line, XTRACE).
  CASC-EDGE as the Lead states it (23:10Z and 22:42Z): «RET(X; e) ≤ deg(X), i.e. the returns of Even X to ANY target with root e».
  l-new 6e725d15 (box 101) was not opened.

## 1. The kill
- Instance experiments/red/casc/instances/cedge_n32.pg + .start: n 32 (30 Even, 2 Odd), start file given. It is NOT hand-made: casc/ovclimb.py
  (seed red/so/instances/pftheta34_n32 with its default start, mutation hill-climb, score = L-NEW's «(returns of X per root)/deg X»,
  rng 4) reached it after about 11,800 steps.
- L-NEW's retcause.py at 457e41fe, UNCHANGED (casc/cedge_out.txt):
  - «RUN 5-31 F 26 returns 60 … EROOT kinds {'FRESH': 60} … chain depth {0: 38, 1: 16, 2: 3, 3: 3}»;
  - «PERROOT max returns of one Even X per root 4 (X 7 deg 2) … max (returns of X per root)/deg X 2.0 … max returns of one edge per
    (root, depth) 1».
- XTRACE=7, every return of vertex 7 (successors {20, 26}, priority 25):
  - k 8: 20 → 26, root ('FRESH', 26, 27, 6), depth 0;
  - k 14: 26 → 20, root ('FRESH', 20, 7, 9), depth 0;
  - k 17: 20 → 26, root ('FRESH', 20, 7, 9), depth 1;
  - k 20: 26 → 20, root ('FRESH', 20, 7, 9), depth 2;
  - k 22: 20 → 26, root ('FRESH', 20, 7, 9), depth 3.
- So RET(7; e) = 4 > deg 7 = 2 for e = (20 → 7 at q = 9). That is a fresh entry of 7's own successor 20 INTO 7. CASC-EDGE fails.
- Checks:
  - xeng: state sequences identical (L-NEW n5.py on L-SI si.py vs L-COMP n5b SPEC);
  - Oink 8fbf0a7 --zlk winners equal N5's, and verify passes on N5's strategies (rel2/oinkcmp.sh: OINK OK);
  - casc/retx.py (L-RED, n5b): vertex 7 returns 5 times in the W-run, as XTRACE lists.

## 2. Mechanism (READING from the trace)
- The root is a fresh entry 20 → 7 of X's own successor: 20 starts pointing at X. From then on, Ξ(20)'s play passes through X itself.
- Each switch of X changes Ξ at 20, through X's own value. That re-orders X's two targets, and X switches back, one chain level deeper
  each time (depths 0, 1, 2, 3). It is a PING-PONG whose every step is the child of the previous one in L-NEW's root forest: the
  «counter-overtake under the same root» the Lead asked for, closed through X's own successor.
- Each edge returns twice under e, at different depths ((7, 20) at depths 0 and 2; (7, 26) at 1 and 3). So LEVEL-ONCE holds here
  («max returns of one edge per (root, depth) 1»).
- The ping-pong stops after 4 steps because Ξ only rises: every alternation needs a fresh value level at 20 and 26. Whether a family can
  make RET(X; e)/deg X grow (a longer ping-pong) is the next question. L-NEW's PROVED corollary of LEVEL-ONCE, RET(X; e) ≤ deg X·(D_e + 1),
  allows it to grow with the depth D_e, which here is 3.

## 3. LEVEL-ONCE (not killed)
- The four climbs (rng 1-4, about 12,000 steps each, score (ratio, level, returns)) never reached «returns of one edge per (root, depth)» ≥ 2.
  The best ratios: 1.5 (rng 1, 2), 2.0 (rng 3, 4).
- A LEVEL-ONCE kill needs two returns of one edge under one root at the SAME depth: two different chains of equal length from e.
  That is L-NEW's own unproved step (box 102 §2).

## 4. Pins (experiments/red/check.sh «R150»)
- casc/instances/cedge_n32: sha1 (casc/pins.sha1); casc/retx.py output; xeng; Oink.
- L-NEW's retcause.py is not on claude/l-red, so check.sh does not run it. Its output is kept as data in casc/cedge_out.txt.
