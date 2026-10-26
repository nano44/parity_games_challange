# experiments/new/box47 (L-NEW successor 26): X_dir on G^{u,u'} (docs/new/N5-XDIR-box47.md)
DATA, not proof. Uses experiments/new/box43 (multi.rand_ckO, climb.mutate), box21 (n5x: SPEC N5 step, si.py Engine) and box45 (eprestrict.step_tau,
N5^tau). Run from this directory.
- xd2.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files [--start F]): every X_dir transition ({u} -> {u'}, in-phase) with its classifiers
  (SAME, SCH, RHO_U, RHO_U2, TIE_U, A2U, A2U1, VIA, HB, POS, DIR); every U-run (|U| = 2) holding an X_dir or a D = U state, with Corollary REPRO_U
  checked on G^U (REP_V, XI_V must be 0; SB_V counts S1 counterstrategy mismatches, allowed). VERB=1 prints one line per X_dir and per first SB
  mismatch; SBDUMP=DIR writes the random start of an SB run; MUT=1 drops u' from U (SB_V / XI_V must bite).
  out/xd2_lib41_k2.txt (`2 7 --list ../box41/lib41.txt`), out/xd2_rand3000.txt (`4 8 --rand 3000 5 18 111`), out/xd2_rand3000b.txt
  (`4 9 --rand 3000 6 24 222`).
- ppclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]: climb on (max X_dir in one U-run, max X_dir per phase, max D = U states in a U-run, total).
  out/ppclimb_*.txt; best games in out/climb/ (not kept except as instances below).
- mkpp2.py GAME K u u2 OUT.pg: cut GAME to G^{u,u2} at state K of its S3 run, and write OUT.start = (sigma_K, tau_K).
- dumprand.py C LO HI GSEED I OUT.pg: write game I of a --rand sample.
Instances: pp2_n19.pg (+ .start; 𝒞^2O ping-pong {1} -> {0} -> {1} in one phase, from S3 too; kills CONJECTURE XD-1), xdhon_n13.pg (X_dir at a
W-honest phase start; = --rand 3000 6 24 222 game 1841), sbmis_n12.pg (sigma-bar on G^{0,7} != sigma-bar on G at state 0, vertex 0 its own cycle
node; = --rand 3000 5 18 111 game 1132).
