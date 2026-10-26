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
- ffdeep.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B] [--start F]: Lemma FB-RISE (docs/new/N5-HONFF-box47.md)
  at every non-honest in-phase fallback: GEN_V (general form, must be 0), CTRL_T (control without the Odd term; fails, always with GEN_ODDBIND),
  and after a W-honest state FBRISE_V (honest form, must be 0), XI_AT, DEEP, STEP_V (HON step 1, must be 0). VERB=1 prints failures and DEEP events.
  out/ffdeep_liball_n20_k6.txt (`6 5 --list out/liball.txt --nmax 20 --budget 3000000`), out/ffdeep_rand3000*.txt, out/ffdeep_ffin*.txt (L-COMP 5's
  pinned gaps, read from l-comp 15bcfa06 with `git show`, run with their .start), out/ffdeep_xing3.txt (j10_n24, j7_n32, j8_n32, S3, budget 3·10⁷).
  out/liball.txt = every pinned .pg under experiments/*/instances, experiments/*/*/instances, docs/referee*/*/instances (735 files).
- ffclimb2.py NMAX STEPS SEED OUTDIR --seed FILE.pg [--budget B]: climb against FB-RISE / HON-FF (fitness HONFF_V, DEEP, XI-EARLY failures, after-honest
  fallbacks). Seeded j10_n24, seeds 111/112, 1,500 steps: (0, 0, 0, 1) both (out/ffclimb2_j10_s*.txt).
- fbph.py STARTS SEED --list FILE [--nmax N]: max in-phase fallbacks per phase (liball n ≤ 64, S3 + 2 random, seed 7: 38 at n = 48, fr39_q4_n48).
- fbcount.py / fbpot.py / fbconf.py (docs/new/N5-FB-box47.md): the τ-frame split of the fallbacks (NB / OB / SAT) and the failed ρ / epoch charge
  (fbcount: OB_NORHO, CHARGE_V); per-vertex G_τ-levels at fallbacks (fbpot: POT_FLAT, XIFLAT); Theorem FB-C in the honest frame H_C (fbconf: FBC_V,
  NSC_V, LEVC_MONO_V must be 0). out/fbconf_liball_n34.txt, out/fbconf_fr39.txt, out/fbconf_rand3000.txt. instances/fr39_q4_n48.start = the
  "n5py_start" lines of experiments/red/fbr/instances/fr39_q4_n48.start.json (L-RED), copied.
