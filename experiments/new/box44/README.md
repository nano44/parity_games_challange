# experiments/new/box44 (L-NEW successor 23): Route Δ, R20 coarse port in set form (docs/new/N5-DELTA-box44.md)
DATA, not proof. Uses experiments/new/box43 (multi, n5x via box21, f1d.hD). Run from this directory.
- crd.py: LAM_D, CR_D, C_D (ii), FBL_D (b)/(c), cross-terminal disagreements (RTDIS). Usage: crd.py --list FILE | --rand COUNT NLO NHI
  SEED | files. Runs 2026-10-26 01:13Z-01:19Z: --list ../box41/lib41.txt; --rand 2000 5 14 31; --rand 1000 10 24 32 (before RTDIS);
  --rand 3000 8 20 41; --rand 1500 15 30 42; ../box43/instances/*.pg. 0 violations; table in N5-DELTA-box44.md §9.
- rtdump.py FILE.pg: lists each cross-terminal disagreement (state, D, edge, terminals, coarse equality, S4a's choice).
  ../box43/instances/dch16_n44.pg: k = 28, 30 (5 edges), M_D = 43 = n − 1.
