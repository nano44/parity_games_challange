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
