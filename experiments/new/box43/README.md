# experiments/new/box43 (L-NEW successor 22, box 43: N5 beyond C^1O)
All outputs are DATA. Engine: box21/n5x.py step (= SPEC S1-S5; n5x.trace(check=True) asserts n5.py's counts), L-SI's si.py.
- multi.py: N5 run on any game; measures it, fb, J (joint lambda-runs), T / Tv (tau-changing transitions, per Odd choice vertex),
  TJ (max tau-changes inside one joint lambda-run), P / maxP / maxF (phases = (lambda, tau)-constant runs), prodeg. `--rand` mode.
- climb.py: hill-climb on C^kO games (k fixed; `--deg2`: every Odd choice vertex has out-degree 2), objective lexicographic over
  multi.py measures plus ret / retn (returns of tau(o_i); retn excludes own-cycle-node switches) and tx = T - sum (deg(o_i) - 1).
- shrink.py: greedy shrink keeping TX / RET / RETN / TJ>=m from the best-reward start.
- exh2.py: exhaustive canonical C^2O games (L-COMP exh.py's canonical form), best-reward start or every start pair.
## Instances (best-reward start, SPEC S3; each: n5.py n5 run + check_sol2.py "zielonka(oink zlk) OK strategies verified")
- instances/ret2_n7.pg (sha1 8a354f5704c6e18d62d50cc467794f5a2b78738d): C^2O, Odd choice vertices 1 and 3 (out-degree 2 each).
  n5.py: iterations=2 fallback=0. tau(1): 3 -> 0 -> 3 (a return; 1 is not its own lambda^U cycle node), so tau(1) changes twice
  > deg(1) - 1 = 1: the per-vertex form of Corollary Phi-1O (a) fails. Cause: S4b best-responds to the OLD sigma (route 1 -> 0 -> 4 ->
  5 -> {5,6}); Even cuts it in the same iteration (4 -> 4).
- instances/tx2_n8.pg (sha1 c0f7b214e4e50720ea2d3082b181959f4aaa9f86): C^2O, Odd choice vertices 1 and 3 (out-degree 2). n5.py: iterations=3
  fallback=0. tau = (3,2) -> (0,2) -> (0,1) -> (3,1): all 4 joint strategies, T = 3 > sum (deg - 1) = 2. Even idle after step 1.
- instances/retf_n6.pg (sha1 8b936bfbc78d3d16ab17ed7bfedf1f7db05da73d): FRONTIER (Even choice 4, 5; Odd choice 0, 1). n5.py: iterations=3
  fallback=0. tau(0): 2 -> 1 -> 5 -> 1 (non-own-cycle-node return). Smallest frontier return found (exhaustive n 4: none).
- mirror.py (Lemma DUAL check), dualsym.py, dblfb.py (two-sided fallbacks), dset.py (disagreement set D_k per phase).
  Runs (2026-10-25 ~22:15Z): mirror.py --list ../box41/lib41.txt: 412 runs, 15 with two-sided fallbacks, 0 violations;
  mirror.py --rand 3000 4 14 11: 0 violations. dblfb.py --list lib41: 781 fallbacks, 54 two-sided (15 runs).
  dset.py --list lib41: 1O maxD 1, D-changes/phase 10; frontier (135 runs) maxD 106, D-changes/phase 5.
- results/: exh2 tables (n 3 canonical / all starts, n 4 canonical (+ RETN), n 4 frontier).
