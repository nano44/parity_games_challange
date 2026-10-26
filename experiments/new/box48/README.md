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
- cyc.py STARTS SEED (--list FILE | files) [--start F]: CYC_c per phase, c's cycle changes ZCH split STRICT / TIE / c-only (N5-KPOLY §8);
  ZCH_OTHER_V must be 0. out/cyc_lib41_n34_k2.txt, out/cyc_long7.txt, out/cyc_long2.txt.
- zch.py STARTS SEED (--list FILE | files) [--start F]: packet addendum P-N5-OFFMONO-add-box49 (successor 29): Remark Z-CONST (ZC_V), Lemma
  ZCH-COUNT (STRICT / TIE / CEVEN / ODDC split; PSI_V, CEVEN_V, STRICT_V, ZB_V, OTHER) and Corollary CHAIN-COUNT′ with cut ZC = ZCH ∩ CYC (PM_V,
  CC_V sum form, CCD_V stated form); all must be 0. Controls MUT=1 (no ZC cut; did not bite on lib41), MUT=2 (opposite length sign; bites),
  MUT=3 (no EXIT cut; bites). out/zch_lib41_n34_MUT{0,1,2,3}.txt (`2 7 --list ../box41/lib41.txt --nmax 34`), out/zch_long7.txt (`0 1 --start S G`
  on nep90_n40 (../../red/rec0/instances, start ../../si/rund/instances), nep76_n40 (../../n5-epoch/instances), long121_n40 (../../red/n3/instances),
  out/qpcclimb/best_qpc_{nep90_n40_s51,nep76_n40_s52,long121_n40_s53}, out/qpcclimb/scale/snap_n80_s62, each with its .start).
  out/quotecheck_offmono_add.txt: 16 quotes, 0 missing.
- ft.py (as zch.py) [MUT]: N5-KPOLY §11: Lemma FT-COUNT (FTB_V), Remark FT-CONST (OC_V), Corollary CHAIN-COUNT″ (PM_V, CC_V, CCD_V) with cut
  CYC ∩ FT (MUT=0) or CYC ∩ ZCH ∩ FT (MUT=5); all must be 0. MUT=1 (no cut), MUT=4 (one cut transition dropped) do not bite on lib41.
  out/ft_lib41_n34_MUT{0,1,4,5}.txt, out/ft_long7.txt, out/ft_long7_MUT5.txt (instances as zch.py).
- tie.py STARTS SEED (--list FILE | files) [VERB=1] [MUT]: TIE / ODDC events (P-N5-OFFMONO-add §3) and N5-KPOLY §11's Lemma PF-CHOICE (CHAR_V),
  Corollary TIE-CHARGE (FT_V), FT-COUNT (FTB_V); all must be 0. Controls MUT=1/2/3 (wrong tie-breaks; CHAR_V bites). out/tie_lib41_n34_k2.txt
  (VERB), out/tie2_lib41_n34_k2.txt, out/tie2_lib41_MUT{1,2,3}.txt.
- tieclimb.py NMAX STEPS SEED OBJ OUTDIR --seed G [--start S]: climbs ODDC_c / TIE_c per phase (OBJ oddc / tie / both), checking tie.charcheck on
  every scored game. out/tieclimb/ (oddc_s1, s2 from box31 u3ev_n16; tie_s3, s4 from red/kl klcount_n16; 3,000 steps, n ≤ 24).
- out/quotecheck_epc_fixes.txt: docs/new/P-N5-EPC-fixes-box48.md against cd4795f8 REFEREE (§C), c4975512 REFEREE-2 (§C), 81ab0b72 packet: 41 quotes, 0 missing.
- orun.py (as zch.py): offsets inside p-runs of x-pieces (cut EXIT_x ∪ ZC″): hypotheses HA-HE, DIR / REL split (N5-KPOLY §12 (ii)).
  out/orun_lib41_n34_k2.txt, out/orun_long7.txt.
- frz.py (as zch.py) [VERB=1]: the DEAD guess FRZ_c (M(κ) frozen after |U_c| − 1 transitions of a fallback-free run; N5-KPOLY §12 (iii)).
  out/frz_lib41_n34_k2.txt, out/frz_long7.txt, out/frz_so_th_n32_S3.txt (`0 1 ../../red/so/instances/so_th_n32.pg`, the kill).
