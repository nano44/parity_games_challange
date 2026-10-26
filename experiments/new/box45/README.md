# experiments/new/box45 (L-NEW successor 24): epochs as runs of N5 on the restricted game G'_E (docs/new/N5-EPR-box45.md)
DATA, not proof. Uses experiments/new/box43 (multi.rand_ckO) and box21 (n5x: SPEC N5 step, si.py Engine). Run from this directory.
- eprestrict.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files): RESTRICT_E (i), (iv), REPRO, EP-0 checks per epoch; DIV, epochs
  and max length by |D|, G1PH. EPR_MUT=1: mutation control (u in D keeps only tau(u)).
- Runs 2026-10-26 05:47Z-05:50Z (date -u), outputs in out/:
  - out/lib41_k2.txt: `eprestrict.py 2 7 --list ../box41/lib41.txt` (S3 + 2 random starts; games with n > 64 skipped).
  - out/rand3000.txt: `eprestrict.py 4 8 --rand 3000 5 18 111`.
  - out/lib41_mut.txt: `EPR_MUT=1 eprestrict.py 0 7 --list ../box41/lib41.txt` (mutation bites: XI_V 2,788, REP_V 1,615).
  All three: XI_V, OPT_V, REP_V, EP0_V = 0 (unmutated), DIV = 0.
- itcheck.py STARTS SEED (--list FILE | --rand ...): in-phase states with (u, sigma-bar(u)) in I_tau (IT1), |D| = 1 among them, and W = Xi
  there (Lemma TIE-W). Runs 06:10Z-06:12Z: out/itcheck_lib41_k2.txt (`itcheck.py 2 7 --list ../box41/lib41.txt`), out/itcheck_rand3000.txt
  (`itcheck.py 4 8 --rand 3000 5 18 111`): IT1 65 (|D| = 1: 0) and 25 (|D| = 1: 7, all with W = Xi).
- divsearch.py COUNT NLO NHI K SEED STARTS: random 𝒞^KO games, random start pairs; counts in-phase tie states with D = {u} and
  (u, sigma-bar(u)) in I_tau (tie1; W = Xi there by TIE-W) and DIV (SPEC's own S4b on G'_E moves tau there). Runs 06:36Z-06:45Z
  (date -u), out/divsearch_*.txt: 40000 4 8 2 11 (tie1 64, DIV 0), 40000 4 10 3 12 (34, 0), 20000 6 14 2 13 (35, DIV 1),
  20000 6 14 3 14 (32, 0); earlier 4 small runs (seeds 1-4): tie1 8, DIV 0. out/divsearch2_*.txt (06:33Z-06:36Z by date -u): seeds 11, 13, 14
  re-run with tie1_cyc / DIV_cyc, plus 20000 8 16 2 15 (tie1 17, DIV 1): tie1_cyc = tie1 in all four (148 of 148), DIV_cyc = DIV.
- instances/div_n8.pg (sha1 4ed57ef2c1c92ee526ccd2683ae7c28b1caf5bfa) with start pair instances/div_n8.start (the state itself): the
  first DIV instance (seed 13). divshow.py prints it (out/divshow_n8.txt): N5 on G, first transition in-phase (S4a, sigma(6): 7 -> 0),
  Q = {3, 7}, D = {3}, Xi(3) = (3, {}, 0) (u is its own cycle node), W = Xi; on G'_E SPEC's S4b moves tau(3): 5 -> 7 (S1's
  counterstrategy on G'_E picks 7 at the cycle node), N5^tau keeps tau. So N5 and N5^tau on G'_E DO differ on some epochs: premise
  (Sigma-tau) is exercised there (it is not exercised in the samples of P-N5-EPR §5).
- n5tau.py STARTS SEED (--list | --rand C LO HI GSEED): runs N5^tau on 𝒞^1O games; R48 (i) per N5^tau phase (FB_V), TIEKEEP. Runs
  finished by 06:44Z (date -u): out/n5tau_kwfiles_k2.txt (`n5tau.py 2 7 --list ../../../docs/referee-2/R2-N5-KW/files.lst`), out/n5tau_lib41_k2.txt
  (`n5tau.py 2 7 --list ../box41/lib41.txt`), out/n5tau_rand5000.txt (`n5tau.py 4 9 --rand 5000 5 20 22`): FB_V 0; TIEKEEP 88 / 29 / 613.
- nep.py STARTS SEED (--list | --rand | files): per phase N_ep, distinct sigma-bar|Q configurations, recurrences of one configuration, distinct
  one-player optima O_E (Even's optimum of G_{sigma-bar_E}), phases whose epochs all have |D| <= 1. Runs 07:20Z-07:26Z (date -u):
  out/nep_lib41_k2.txt (`nep.py 2 7 --list ../box41/lib41.txt`), out/nep_rand3000.txt (`nep.py 4 8 --rand 3000 5 18 111`), out/nep_named.txt
  (`nep.py 0 1 ../box25/laps/lap_n6_s1_110421.pg ../../red/so/instances/so_th_n32.pg`). docs/new/N5-NEP-box45.md §1.
- recclimb.py K NMAX STEPS SEED OUTDIR [--seed FILE] [--d0]: climbs on (max recurrences of one configuration, max N_ep) via nep.py. Runs
  07:33Z-07:35Z (date -u): out/recclimb_k2_n12_s31.txt, out/recclimb_k3_n16_s32.txt, out/recclimb0_k2_n12_s33.txt (--d0),
  out/recclimb_seed_so.txt (seed so_th_n32); best games in out/climb/. Table in docs/new/N5-NEP-box45.md §4.
- rec0.py STARTS SEED (--list | --rand): Lemma REC-0 check (N0 <= (f+1)(n+1) + 4n(n-1) + 1), N0 max, kind-(iii) steps per run. Runs 07:42Z-07:47Z
  (date -u): out/rec0_lib41_k2.txt (`rec0.py 2 7 --list ../box41/lib41.txt`), out/rec0_rand3000.txt (`rec0.py 4 8 --rand 3000 5 18 111`): 0 violations.
  recclimb.py --d0 runs 07:48Z-07:53Z: out/recclimb0_seed_so.txt (seed 41), out/recclimb0_k3_n20_s42.txt, out/recclimb0_k2_n16_s43.txt.
