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
- rtclimb.py --obj sw seeds 21-24 (01:35Z-01:40Z): best DIFFSW 0 (k 2, n ≤ 12), 8 (k 3, n 20), 0 (k 4, n 30), 21 (k 4, n 40).
  swphase.py FILE...: per-phase in-phase fallbacks and cross-terminal switches. instances/sw21_n40.pg (seed 24 best): one fallback
  switches 21 vertices across terminals; N5 output: Oink verify OK, regions = Oink --zlk, harness verify.py OK.
- fbf.py: frontier FB-POLY checks (CN-ONLY_D, EXIT-SWITCH_D, FREEZE-EXIT_D, FB-RED, per-terminal THETA-AFTER "TA"), FMAX per phase.
  fbclimb.py: climbs FMAX (or --obj ta: TA violations). docs/new/N5-FBF-box44.md §4. Runs from 01:56Z.
- fbclimb.py seeded runs 71-75 and --obj ta runs 81-84 (02:00Z-02:05Z): table in N5-FBF-box44.md §4. instances/fb17_n32.pg (sha1
  398e23e2…): 17 in-phase fallbacks in one phase, frontier (2 Odd, 23 Even choice vertices); N5 output verified (Oink verify,
  regions = Oink --zlk, harness verify.py).
- fbf.py: + FB-RED late form (REDL), N_late, ρ_late. fbclimb.py --obj rho (seeds 91-97, 02:31Z-02:33Z): max ρ per phase 6-32, N_late 0
  everywhere (no phase reaches n fallbacks). N5-FBF-box44.md §6.
- sgcheck.py (03:11Z-03:12Z): (SG) strict gain at every switched non-cycle-node Even vertex in-phase; lib41 12,653 checks, instances
  263, --rand 2000 5 20 71 430: 0 violations; max switching transitions per phase 112, max κ-levels per vertex per phase 52 (lib41).
- epoch.py (03:26Z): Lemma EPOCH checks (N_ep, σ̄|Q repeats, f ≤ 1 + n·N_ep, freeze), N5-FBF-box44.md §9. lib41: 91 phases with a σ̄|Q
  repeat (max 36), max N_ep 50 (n 32); 0 violations; freeze part vacuous (no epoch with n − 1 fallbacks).
- altcheck.py (03:46Z-03:47Z): Lemma ALT (N5-FBF-box44.md §10): lib41 2,051 in-phase σ̄(q) changes (1,910 strict, 75 ties, 65 non-clean,
  1 at a cycle node), 0 violations; instances + lap_n6 36; --rand 2000 5 20 91: 33.
