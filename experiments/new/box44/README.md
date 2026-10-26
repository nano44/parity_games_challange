# experiments/new/box44 (L-NEW successor 23): Route Δ, R20 coarse port in set form (docs/new/N5-DELTA-box44.md)
DATA, not proof. Uses experiments/new/box43 (multi, n5x via box21, f1d.hD). Run from this directory.
- crd.py: LAM_D, CR_D, C_D (ii), FBL_D (b)/(c), cross-terminal disagreements (RTDIS). Usage: crd.py --list FILE | --rand COUNT NLO NHI
  SEED | files. Runs 2026-10-26 01:13Z-01:19Z: --list ../box41/lib41.txt; --rand 2000 5 14 31; --rand 1000 10 24 32 (before RTDIS);
  --rand 3000 8 20 41; --rand 1500 15 30 42; ../box43/instances/*.pg. 0 violations; table in N5-DELTA-box44.md §9.
- rtdump.py FILE.pg: lists each cross-terminal disagreement (state, D, edge, terminals, coarse equality, S4a's choice).
  ../box43/instances/dch16_n44.pg: k = 28, 30 (5 edges), M_D = 43 = n − 1.
- (fixed 01:29Z) crd.py FBL_D (b): same-terminal edges are a violation only at states with (h3D) (the statement's hypothesis); NOH3 counts
  the others; DIFFSW = cross-terminal edges switched by S4c; RTREV/RTREV1 = reverse disagreements. Re-run of every sample 01:29Z-01:30Z.
- fbldump.py FILE.pg: every R_D-sourced gate edge at an in-phase fallback with (hD), with values and S4c's choice.
- rtclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE]: climb (DIFF, RTDIS, ST2); stops on any crd.py violation. Seeds 11-14 (01:26Z).
- shrinksw.py in out: greedy shrink keeping DIFFSW >= 1.
- instances/rtf_cex.pg (sha1 2203e77f…, shrunk from rtclimb seed 13) and rtf_cex_inj.pg (sha1 9b55eee6…, rank-equivalent, injective
  priorities): refute CONJECTURE Δ-RT-F (N5-DELTA-box44.md §8). instances/rtdis_k4_n24.pg (sha1 00529ed5…): climb seed 12 best.
  N5 outputs on all three: Oink verify OK, regions = Oink --zlk, harness verify.py OK.
