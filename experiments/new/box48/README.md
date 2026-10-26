# experiments/new/box48 (L-NEW successor 27): distinct Odd configurations per phase (docs/new/N5-NCONF-box48.md)
DATA, not proof. Uses box43 (multi: rand_ckO, SPEC N5 step), box21 (n5x.readstart), box46 (fbwlev.wlev, levels). Run from this directory.
- nconf.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--start F] [--minlen L]: per phase (maximal (λ, τ)-constant run, ALL
  phases): L, EPQ = N_ep (σ̄|Q changes + 1, R63/R64's epochs), EPD = D changes + 1 (L-SI §27.2's count; EPD ≤ EPQ), NCONF (distinct σ̄|Q), ND, REV =
  EPQ − NCONF, VIS (most epochs of one configuration), RET_NOFB (returns to a configuration with no in-phase fallback between), f, NCF (= |𝒞_f|,
  box47 fbconf's NCONF). VERB=1 one row per phase with L ≥ minlen; TRACE=1 adds the configuration and D sequences.
  out/nconf_liball_n40_k2.txt (`2 7 --list ../box47/out/liball.txt --nmax 40 --minlen 30`), out/nconf_rand3000.txt (`4 8 --rand 3000 5 18 111
  --minlen 12`), out/nconf_rand3000b.txt (`4 9 --rand 3000 6 24 222 --minlen 15`).
- laps.py GAME START: the longest phase state by state (config id, D, fallback, and the Even vertices whose σ differs from the first state with the
  same configuration). out/laps_nep90.txt.
- vislev.py STARTS SEED (... as nconf.py) [--budget B]: LEV_C (box47 fbconf) at the first state of each epoch of a returning configuration: STALL
  (LEV_C equal and < n − 1 at two consecutive C-epochs; CONJECTURE VIS-RISE says 0), LEV_DROP_V (must be 0, LEV_C non-decreasing), XI_EQ.
- quotecheck2.py FIXES.md REV1:FILE1 [REV2:FILE2 ...]: box47/quotecheck.py with a revision per source (the two referee §Cs sit on different branches).
  out/quotecheck_honff_fixes.txt (docs/new/P-N5-HONFF-fixes-box47.md against e7db1ab4 REFEREE, 11e3cfb1 REFEREE-2, 2fca63b8 packet): 45 quotes, 0 missing.
- retfb.py STARTS SEED (--list FILE | files) [--nmax N] [--budget B] [--start F]: Lemma RET-FB at every epoch start against the last fallback
  before it (RETFB_V must be 0; MUT=1 uses t := s − 1, must bite) and Corollary VIS (VIS_V must be 0); R0 against REV. out/retfb_*.txt.
- satfb.py (usage as vislev.py): every fallback from a saturated C-state (LEV_C = n − 1): FLAT, LAST, T1C, switches at own cycle nodes (SW_OWNCN),
  closing a cycle through x (SW_THRU); Lemma SAT-FB. out/satfb_*.txt.
- r0shape.py STARTS SEED --list FILE [--nmax N]: the fallback-free returns: |U| (vertices whose σ̄ changes in the stretch), max |D|, |D_C|, and per
  phase NCONF2 (distinct configurations with |D_C| ≥ 2). out/r0shape_liball_n40_k2.txt.
Instances: long121_n40.pg + .start (L-RED 21, l-red dee85909 experiments/red/n3/instances, copied; sha1 c667c085… / d750664a…): one phase of 121
transitions, |Q| 3; out/nconf_long121.txt, out/retfb_long121.txt.
- ncclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE.pg]: climb on (max NCONF_{≥2} in one phase, max N_ep^{≥2}) from the S3 start. Random seeds stay
  trivial (out/ncclimb_k*_s*.txt: best (4, 4)); seeded from nep90 / nep76 (S3 scores (10, 10)): out/ncclimb_nep*_s*.txt, best games in out/climb/.
- newconf.py GAME [START] / rootrel.py GAME [START]: new configurations of the longest phase (NEWPAIR / RECOMB); root × relay split (root = most
  changing vertex of Q, R = σ̄ on the rest) with each R's root sequence. out/rootrel_newconf.txt (nep90, nep76, long121 with starts; pft34 S3).
- fsrestrict.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]: the frozen-side u-run restriction G^{u|J} (N5-NCONF §9): XI_V, REP_V must be
  0; MUT=1 must bite. out/fsrestrict_liball_n34_k2.txt, out/fsrestrict_liball_n34_MUT.txt, out/fsrestrict_long3.txt.
- phrestrict.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]: Lemma RESTRICT_H on the used-edge game G^P of each phase (N5-NCONF §10):
  XI_V, REP_V must be 0; MUT=1 must bite. out/phrestrict_long3.txt, out/phrestrict_liball_n34_k2.txt, out/phrestrict_liball_n34_MUT.txt.
- qp.py STARTS SEED (--list FILE | --rand C LO HI GSEED KFRAC | files) [--nmax N] [--start F]: QP = |union of D_k| per phase (asserted), D0, ENT, N_ep,
  NCONF, XDEG, QP_c per class (N5-NCONF §11). out/qp_liball_n48_k2.txt, out/qp_dunion.txt.
- qpclimb.py QT K NMAX STEPS SEED OUTDIR [--seed FILE.pg]: climb on (min(QP, QT), len) of one phase from S3 (O fixed by climb.mutate). out/qpclimb/.
- dunion.py GAME START K OUT.pg OUT.start: k disjoint copies with copied start (instances/du/nep90x2..4).
- qpcclimb.py NMAX STEPS SEED OUTDIR --seed GAME.pg --start GAME.start: climb (game + start) with O-moves, objective (QP_c · len, len) (N5-NCONF §12).
  out/qpcclimb/ (logs, best games with .start, verify.txt = qp.py + phrestrict.py on each best).
- reset.py STARTS SEED (--list FILE | files) [--start F]: offsets to the routing parent, RESET / ENTRY / RISE / PARCHG / CHAIN_V (N5-KPOLY-box49 §2);
  MUT=1, MUT=2 controls. out/reset_lib41_n34_k2.txt, out/reset_long6.txt.
- swaps.py STARTS SEED (--list FILE | files) [--start F]: pairwise order swaps of an Odd choice vertex's options per phase (N5-KPOLY §4).
  out/swaps_long4.txt.
- offmono2.py STARTS SEED (--list FILE | files) [--start F]: Lemma OFFSET-MONO (packet P-N5-OFFMONO-box49) with p := par_{t+1}(q): V_Kc, V_M must be
  0; V_Kx (opposite length sign) and MUT=1 (p off q's play) are controls. out/offmono2_lib41_n34_k2.txt, _MUT.txt, out/offmono2_long7.txt.
