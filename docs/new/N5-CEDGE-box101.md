# N5-CEDGE (box 101): the repaired cascade conjecture. CONJECTURE CASC-EDGE: in every W-run, every Even vertex X has at most deg(X) returns rooted at one fresh entry. It implies CASC_F(e) ≤ m_E and |F| ≤ (m_E − n_E)(1 + m_E), i.e. polynomial W-runs (PROVED, lane). DATA: 0 violations on 603 W-runs with returns plus L-RED's clone kill; tight (ratio 1.0) on obs_K12_m24 (X of degree 24 returns 24 times under one root), pftheta34_n32 and others. DEAD: L-RED's «once per root» (obs 24, sbq2 2), «once per edge per root» (topfix_n10: 17), and the injection «distinct left targets per root» (pftheta34_n32 and 9 more games). Not proved
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 22:17Z: «BOX 101: state the repaired conjecture precisely. Merge your TREE /
NARROW picture with L-RED's per-(X, root) form into one statement that would imply polynomial W-runs; call it CASC-EDGE. Then try to prove it
from CHILD plus a bound on how often one Even X can return within one root's subtree.» Written 2026-10-30 22:18Z-22:3xZ (date -u). Working
note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Sources and tools
- Box 100 (N5-CASC-box100.md): the Even root map, FRESH-ROOT, CHILD, TREE. Box 98: PAY. Box 99: CASCADE-EQ.
- L-RED R148 (l-red c942a394, docs/red/R148-cascade.md, read from origin/claude/l-red):
  - kill of CASCADE-LIN on cascl_K4_m8_N100 (n 222; 121 > n/2);
  - «CONJECTURE CASCADE-LIN′ (L-RED, data only): in every W-run, every Even vertex X returns at most once per root, so CASC_F(e) ≤ n_E».
  - The Lead's 22:17Z message also cites cascl66_K4_m8_N150 («an X that returns twice per root»). That instance is NOT on origin/claude/l-red
    at 22:2xZ, so it was not run here.
  - cascl_K4_m8_N100 is copied read-only to experiments/new/box101/inst/ (sha1 .pg 8cfe76e0, .start b4f49753).
- Tool: experiments/new/box99/retcause.py, extended. Its PERROOT line gives, per W-run:
  - the max returns of one Even X per root (with that X and its degree);
  - the max returns of one edge per root;
  - the max over X and roots of (returns of X per root) / deg X;
  - the max returns of X per root that leave one target.
- Outputs: box99/cause_*.txt (re-run 22:2xZ) and box101/cause_cascl.txt. Pin: new/check.sh «box 101 CEDGE».
- deg(X) := the number of distinct successors of X. RET(X; e) := the returns of X (to any target) in F whose root (box 100 §1.3) is the
  fresh entry e.

## 1. The statement
- CONJECTURE CASC-EDGE: for every N5 run on every game, every W-run F of it, every fresh entry e of F and every Even vertex X,
  RET(X; e) ≤ deg(X).
- Theorem CEDGE ⇒ WRUN (PROVED, lane). Under CASC-EDGE:
  - CASC_F(e) = Σ_X RET(X; e) ≤ Σ_X deg(X) = m_E for every fresh entry e;
  - so, by CASCADE-EQ (box 99 §2.3, with box 100's total root map) and PAY, |F| ≤ (m_E − n_E)(1 + m_E).
  - Every W-run then has O(m_E²) transitions.
  - The same holds with deg(X) replaced by any polynomial p(n)·deg(X): CASC-EDGE_p ⇒ |F| ≤ (m_E − n_E)(1 + p(n)·m_E). □
- How it merges the pictures:
  - TREE / NARROW (box 100) bound the SHAPE of a root's tree.
  - CASC-EDGE bounds what each Even vertex contributes to the tree, whatever the shape:
    - a path (topfix) is fine if its returns spread over few X, each ≤ deg X;
    - a wide fan (the clock ticks, clones) is fine because each X appears ≤ deg X times.
  - CASC-EDGE implies no shape statement. NARROW is no longer needed for WRUN-POLY.
- It is one-way. WRUN-POLY does not imply CASC-EDGE (the constant 1 in front of deg X has no reason to follow from a polynomial |F|).

## 2. DATA (Even root map)
| instance | n | max RET(X; e) (X, deg X) | max returns of one edge per root | max RET(X; e) / deg X | max returns of X per root leaving one target |
| --- | --- | --- | --- | --- | --- |
| sbq2_K8_m16 | 261 | 2 (122, 2) | 1 | 1.0 | 1 |
| obs_K12_m24 | 272 | 24 (247, 24) | 1 | 1.0 | 1 |
| cascl_K4_m8_N100 (L-RED) | 222 | 2 (66, 2) | 1 | 1.0 | 1 |
| topfix_n10 (default start) | 210 | 17 (193, 18) | 17 | 0.944 | 1 |
| pftheta34_n32 | 32 | 2 (3, 2) | 2 | 1.0 | 2 |
- Corpus: 603 W-runs with returns (box 50b's corpus + 3 pins) + cascl_K4_m8_N100. RET(X; e) > deg X: 0 times. Ratio 1.0 is reached on obs,
  switchbestexp_2, pftheta_cex_n32, run49_n32, runfam_K40 and others. The bound is tight; no slack is visible.
- DEAD alternatives (each with its instance):
  - «every Even X returns at most once per root» (L-RED's CASCADE-LIN′): obs_K12_m24, vertex 247 (degree 24) returns 24 times under one
    root (each to a different target); also sbq2_K8_m16 (vertex 122, 2) and pftheta34_n32 (vertex 3, 2).
  - «every Even edge returns O(1) times per root» (the per-edge reading of CHILD across a whole tree): topfix_n10, one edge of vertex 193
    returns 17 times under one root. Along topfix's path, X keeps coming back to the same target.
  - «the targets X LEAVES at its returns under one root are pairwise distinct» (an injection into succ(X) that would prove CASC-EDGE): 17
    W-runs in 10 games have X leaving the same target twice under one root (pftheta34_n32, pftheta_cex_n32, pft35_n48, pft40_n40,
    so_th_n32, x31_cu32, x31_rx48, run34_n40, runfam_K10, runfam_K40). In pftheta34_n32, X = 3 (degree 2) alternates between its two targets
    twice under one root.
  - The analogous map to the ENTERED target fails on topfix_n10 (17 returns to one target).

## 3. Toward a proof (what CHILD gives and what is missing)
- CHILD (box 100) is per NODE: at one node (x, q) each edge has ≤ 1 child. A root's tree has many nodes, so an edge can recur once per node.
  topfix_n10 does exactly this: 17 nodes on a path, and the same edge (193, g) is a child at 17 of them.
- What a proof needs: a charge for X's SUCCESSIVE returns under one root to distinct successors of X. The data says the right map is neither
  «entered target» nor «left target». Both fail, while the count still stays ≤ deg X.
- Candidate (CONJECTURE, not tested here): X's switches under one root, read as a walk on succ(X), never close a cycle of length > 2, and
  2-cycles a ↔ b recur at most min(deg) times. Equivalently: X's value sequence Ξ(σ_t(X)) (strictly rising at each switch of X, by S4a)
  passes each successor's value band at most once per root.
- Why this is plausible but not proved:
  - Under one root every return of X is triggered (first window rise) by the same fresh tick propagating along plays.
  - Each switch of X strictly raises Ξ(σ(X)). A successor can be re-entered only after its Ξ rose past X's current target. Under one root,
    the rises come from one tick's wave.
  - The missing lemma is «one wave raises each successor's Ξ past X's current target at most once». That is a statement about the ORDER in
    which one wave reaches X's successors. It is XI-CH-POLY localised to one root, and not proved.

## DONE / FINDINGS / NEEDS
- DONE: this note; retcause.py PERROOT line; box99/cause_*.txt re-run; box101/ (inst/cascl_K4_m8_N100 copied read-only, cause_cascl.txt);
  new/check.sh «box 101 CEDGE». SHA: see the commit.
- FINDINGS:
  - CONJECTURE CASC-EDGE: RET(X; e) ≤ deg X. 0 violations, tight at ratio 1.0. PROVED (lane): CASC-EDGE ⇒ |F| ≤ (m_E − n_E)(1 + m_E).
  - DEAD: «once per root» (obs 24), «edge O(1) per root» (topfix 17), «distinct left targets» (pftheta34_n32).
  - The missing lemma is «one wave passes each successor of X at most once». Not proved.
- NEEDS: Lead:
  - route CASC-EDGE to L-RED: a kill needs RET(X; e) > deg X, e.g. clones of pftheta34's vertex 3 do not help, an X oscillating three
    times under one root does;
  - send cascl66_K4_m8_N150 once it is pushed, and I will run it.
