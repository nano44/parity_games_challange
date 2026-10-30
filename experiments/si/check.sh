#!/usr/bin/env bash
# L-SI self-test (< 2 min), run by scripts/verify.sh: engine valuations equal the REFEREE-checked PGSolver port on random
# games and switch-all counts equal the port's (incl. switchallexp N=1,2: 10 and 30 iterations); every rule returns py-zlk's
# regions with strategies that pass harness/verify.py; pinned killer instances in instances/ reproduce their counts.
set -euo pipefail
cd "$(dirname "$0")"
python3 -I xcheck.py --tiny | tail -1 | grep -q "XCHECK PASS"
echo "xcheck --tiny: PASS"
python3 -I coarse/levcheck.py | grep -q "LEVCHECK PASS"
echo "coarse levcheck (level ∞ sentinel): PASS"
if command -v g++ >/dev/null; then
  # compile to a separate name: the lane's long runs use ./vjfast and must not see it replaced mid-run
  g++ -O2 -std=c++17 -o vjfast_check vjfast.cpp && FAST_BIN=./vjfast_check python3 -I xcheck_fast.py --games 40 --nmax 10 | tail -1 | grep -q "XCHECK-FAST PASS" && echo "vjfast vs si.py (40 games): PASS"
else
  echo "g++ not found: vjfast cross-check skipped"
fi
if [ -f instances/pinned.txt ]; then
  while read -r rule file iters startflag; do
    [ -z "$rule" ] && continue
    start=best
    [ "$startflag" = "start" ] && start="spec:$(cat "instances/${file%.pg}.start")"
    if [ "$rule" = "most-improved" ]; then
      [ -x ./vjfast_check ] || { echo "pinned $rule $file: needs vjfast_check (g++), skipped"; continue; }
      got=$(./vjfast_check "$rule" "instances/$file" /dev/null --start "$start" 2>&1 | grep -o "with [0-9]* iterations" | grep -o "[0-9]*")
    else
      got=$(python3 -I si.py "$rule" "instances/$file" /dev/null --start "$start" 2>&1 | grep -o "with [0-9]* iterations" | grep -o "[0-9]*")
    fi
    [ "$got" = "$iters" ] || { echo "pinned $rule $file: expected $iters got $got"; exit 1; }
  done < instances/pinned.txt
  echo "pinned instances: PASS"
fi
# box 17 (RUN_D): OFFSET / TWIN-GAP checks on lib2o, and the DEAD strict-raise instance reproduces its length-only twin change
python3 -I rund/gap.py --list fb2o/lib2o.txt 2 | grep -q "GAP PASS"
python3 -I rund/rund.py --one rund/instances/lenonly_n8.pg | grep -q "LENONLY ('rund/instances/lenonly_n8.pg', 1, 2, 6, 4"
echo "rund (gap lib2o, lenonly_n8): PASS"
python3 -I rund/gap.py --one rund/instances/offret_n23.pg rund/instances/offret_n23.start | grep -q "RETURN ('rund/instances/offret_n23.pg', 0, 3, 22, \[131204, 264200, 264200, 131204\])"
echo "rund (OFFSET-ONCE counterexample offret_n23): PASS"
python3 -I rund/piece.py --list fb2o/lib2o.txt 2 | grep -q "PIECE PASS"
echo "rund (PIECE_D / SPLIT-RED on lib2o): PASS"
python3 -I rund/lvl.py --one rund/instances/incdown_n23.pg rund/instances/incdown_n23.start | grep -q "('INC', 'rund/instances/incdown_n23.pg', 0, 3, 22, \[20, 19\])"
echo "rund (INC counterexample incdown_n23): PASS"
python3 -I rund/lvl.py --one ../red/h3/instances/lcount_n23.pg ../red/h3/instances/lcount_n23.start | grep -q "('LC', '../red/h3/instances/lcount_n23.pg', 0, 3, 1, 3, \[18, 21\])"
python3 -I rund/lvl2.py --one ../red/h3/instances/lcount_n23.pg ../red/h3/instances/lcount_n23.start | grep -q "LVL PASS"
python3 -I rund/lvl2.py --one ../red/h3/instances/lcount2_n23.pg ../red/h3/instances/lcount2_n23.start | grep -q "LVL PASS"
MUT=1 python3 -I rund/lvl2.py --one ../red/h3/instances/lcount_n23.pg ../red/h3/instances/lcount_n23.start | grep -q "LVL FAIL"
echo "rund (LEVEL-COUNT counterexample lcount_n23 (L-RED); LC2 / PAIR-OC on lcount_n23, lcount2_n23, control bites): PASS"
python3 -I rund/sched.py --one ../n5-exhaustive/instances/frz3_n24.pg ../n5-exhaustive/instances/frz3_n24.start | grep -q "SCHED PASS"
MUT=1 python3 -I rund/sched.py --one ../n5-exhaustive/instances/frz3_n24.pg ../n5-exhaustive/instances/frz3_n24.start | grep -q "SCHED FAIL"
echo "rund (P^c_sch / FRZ-SCH / CHARGE on frz3_n24, shifted-schedule control bites): PASS"
NOGEN=1 USTRUCT=1 python3 -I rund/sched.py --one ../n5-exhaustive/instances/frz1_n24.pg ../n5-exhaustive/instances/frz1_n24.start | grep -q "SCHED PASS"
echo "rund (FZ, UNF, OFFUP, U-SPLIT classes on frz1_n24): PASS"
# UF-ONCE DEAD (REFEREE-2 16, R2-N5-RUND §4): the only violation is UF_ONCE, at Even 24 (three U events into (24, 21)) / Even 44.
o=$(python3 -I rund/sched.py --one ../red/so/instances/so_th_n32.pg rund/instances/so_th_n32_s0.start)
grep -q "UF_ONCE_V=1 " <<<"$o"; [ "$(grep -c '^VIOLATION' <<<"$o")" = 1 ]
grep -q "(4, (24, 21)), (9, (30, 11)), (11, (7, 26)), (15, (24, 21)), (21, (24, 21))\])" <<<"$o"
o=$(python3 -I rund/sched.py --one ../red/n5inj/instances/phase2_pk48.pg rund/instances/phase2_pk48_s1.start)
grep -q "UF_ONCE_V=1 " <<<"$o"; [ "$(grep -c '^VIOLATION' <<<"$o")" = 1 ]
grep -q "(16, (44, 11)),.*(25, (44, 19))\])" <<<"$o"
echo "rund (UF-ONCE DEAD: so_th_n32 Even 24 x3, phase2_pk48 Even 44 x2; CHARGE/FZ/UNF/OFFUP 0 violations there): PASS"
# note §22: Lemma ROOT / ROUTE-RELAY hold on frz40; its phase@44 has the mutual relay 11 <-> 26; the inverted ROOT test (MUT=1) bites.
o=$(python3 -I rund/relay.py --one ../red/n5inj/instances/frz40.pg ../red/n5inj/instances/frz40.start)
grep -q "RELAY PASS" <<<"$o"; grep -q "CYC2 ('../red/n5inj/instances/frz40.pg', 44, {0: \[11\], 11: \[26\], 26: \[11\], 27: \[11\]})" <<<"$o"
MUT=1 python3 -I rund/relay.py --one ../red/n5inj/instances/frz40.pg ../red/n5inj/instances/frz40.start | grep -q "RELAY FAIL"
echo "rund (ROOT, ROUTE-RELAY on frz40; mutual relay 11 <-> 26 in one phase; MUT=1 bites): PASS"
# U-SPLIT DEAD (L-RED R80, usplit_rd_s3_n27, S3 start) and PAIR-OC DEAD (L-RED R81, pairoc_n58); LC2 survives on pairoc_n58.
o=$(NOGEN=1 USTRUCT=1 python3 -I rund/sched.py --one rund/instances/usplit_rd_s3_n27.pg -v)
[ "$(grep -c '^VIOLATION' <<<"$o")" = 1 ]; grep -q "VIOLATION ('U_OTHER', 'rund/instances/usplit_rd_s3_n27.pg', 0, 1, (26, 25))" <<<"$o"
grep -q "NB k=1 f=0 y=26 z=25 a_f=20 a_k=20 off_y 0->0" <<<"$o"
o=$(python3 -I rund/lvl2.py --one rund/instances/pairoc_n58.pg rund/instances/pairoc_n58.start)
grep -q "VIOLATION ('PAIROC', 'rund/instances/pairoc_n58.pg', 0, 3, 57, \[(0, 47, 52, True), (1, 48, 51, True), (2, 47, 49, True)\])" <<<"$o"
if grep -q "^VIOLATION ('LC2'" <<<"$o"; then echo "LC2 violated on pairoc_n58"; exit 1; fi
echo "rund (U-SPLIT DEAD usplit_rd_s3_n27 y=26 z=25 off 0->0; PAIR-OC DEAD pairoc_n58 v=57; LC2 holds there): PASS"
# note §23: CONJECTURE FRZ-RHO on frz40 (21 rho-free intervals, max length 6, last change at index 5 < n - 1).
python3 -I rund/frzrho.py --one ../red/n5inj/instances/frz40.pg ../red/n5inj/instances/frz40.start | grep -q "cuts=41 intervals=21 max_last=5 max_len=6 max_tex=2 max_xich=2 trans=49"
echo "rund (FRZ-RHO data on frz40): PASS"
# note §24: Lemma FLIP on frz40 (17 broken / 3 intact flip states) and L-RED's pp_K12_n161 (15 intact); reversed control fails.
o=$(python3 -I rund/flipck.py --one ../red/n5inj/instances/frz40.pg ../red/n5inj/instances/frz40.start)
for k in "broken=17 " "flipcost_checks=139 " "flips=20 " "intact=3 " "intact_with_rise=3 " "FLIP PASS"; do grep -q "$k" <<<"$o"; done
o=$(python3 -I rund/flipck.py --one rund/instances/pp_K12_n161.pg rund/instances/pp_K12_n161.start)
for k in "flips=15 " "intact=15 " "intact_with_rise=15 " "onsets=11" "FLIP PASS"; do grep -q "$k" <<<"$o"; done
MUT=1 python3 -I rund/flipck.py --one rund/instances/pp_K12_n161.pg rund/instances/pp_K12_n161.start | grep -q "FLIP FAIL"
echo "rund (FLIP on frz40 and pp_K12_n161; MUT=1 bites): PASS"
# note §25: Lemma N3-LEVEL; equality lev = rank(top C) on leanT_N6 (random starts), so the strict control MUT=2 bites there.
o=$(RS=4 python3 -I rund/flipck.py --list rund/instances/leanT_N6_list.txt 1)
grep -q "FLIP PASS" <<<"$o"; grep -q "both_intact=4 " <<<"$o"
MUT=2 RS=4 python3 -I rund/flipck.py --list rund/instances/leanT_N6_list.txt 1 | grep -q "VIOLATION ('N3LEV', 'experiments/red/tcpert/instances/leanT_N6.pg rs', 5, 21, 22, 5, 6, 42, 'p2', 42)"
echo "rund (N3-LEVEL on leanT_N6, tight; MUT=2 bites): PASS"
# note §26: flip classes on frz40 (onsets: one N1 by fallback, one N1 by ordinary switch); Lemma CHOSEN / Corollary RELAY-CHAIN on L-RED's
# nep90_n40 (rho_q up to 72 at n = 40; root 0's pieces between chosen-terminal events <= 12); the MUT=1 control (next state's choice) bites.
o=$(python3 -I rund/flipcls.py --one ../red/n5inj/instances/frz40.pg ../red/n5inj/instances/frz40.start)
for k in "onsets=2 " "onsets_N1fb=1 " "onsets_N1sw=1 " "flips_N3=3 " "FLIPCLS PASS"; do grep -q "$k" <<<"$o"; done
o=$(python3 -I rund/chosen.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start)
for k in "RELAY=139 " "ROUTE=153 " "max_chain=2" "CHOSEN PASS"; do grep -q "$k" <<<"$o"; done
if grep -q "TOG=" <<<"$o"; then echo "unexpected TOG on nep90"; exit 1; fi
MUT=1 python3 -I rund/chosen.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "CHOSEN FAIL"
o=$(UP=2 python3 -I rund/quiet.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start)
for k in "max_rho_q=72 " "quiet_max=12 " "rho_q_total=292 " "QUIET PASS"; do grep -q "$k" <<<"$o"; done
echo "rund (flip classes on frz40; CHOSEN / RELAY-CHAIN and chosen-terminal pieces on nep90_n40; MUT=1 bites): PASS"
# note §28: epoch boundaries on nep90 are all clean strict sigma-bar changes (89 boundaries, 119 STRICT, 0 residual); MUT=1 (ALT reversed) bites.
o=$(python3 -I rund/epcause.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start)
for k in "boundaries=89 " "boundaries_rho=89 " "chg_STRICT=119 " "strict_ROUTE=107" "EPCAUSE PASS"; do grep -q "$k" <<<"$o"; done
if grep -q "chg_TIE\|chg_NC\|boundaries_residual" <<<"$o"; then echo "unexpected residual on nep90"; exit 1; fi
MUT=1 python3 -I rund/epcause.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "EPCAUSE FAIL"
echo "rund (epoch causes on nep90: all clean strict; MUT=1 bites): PASS"
# P-N5-RUND fixes file: every «quote» verbatim at its tagged commit and lines; the shifted-lines control (--mut) must fail.
if git cat-file -e 62a1a01d && git cat-file -e e8d31c47 && git cat-file -e 762b7243 && git cat-file -e f1d2cf09 && git cat-file -e 6f9451e3; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-RUND-fixes-box17.md | grep -q "QUOTES PASS"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-RUND-fixes-box17.md --mut | grep -q "QUOTES FAIL"
  echo "rund (RUND fixes file: all quotes verbatim; shifted control fails): PASS"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-FLIP-box18.md | grep -q "QUOTES PASS"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-FLIP-box18.md --mut | grep -q "QUOTES FAIL"
  echo "rund (packet P-N5-FLIP-box18: all quotes verbatim; shifted control fails): PASS"
  if git cat-file -e 72db1b18 && git cat-file -e 75b8b52a; then
    python3 -I rund/quotecheck.py ../../docs/si/P-N5-FLIP-fixes-box18.md | grep -q "quotes=23 bad=0"
    python3 -I rund/quotecheck.py ../../docs/si/P-N5-FLIP-fixes-box18.md --mut | grep -q "QUOTES FAIL"
    echo "rund (P-N5-FLIP fixes file: 23 quotes verbatim; shifted control fails): PASS"
    python3 -I rund/quotecheck.py ../../docs/si/P-N5-CHOSEN-box19.md | grep -q "quotes=9 bad=0"
    python3 -I rund/quotecheck.py ../../docs/si/P-N5-CHOSEN-box19.md --mut | grep -q "QUOTES FAIL"
    echo "rund (packet P-N5-CHOSEN-box19: 9 quotes verbatim; shifted control fails): PASS"
  else
    echo "rund (P-N5-FLIP fixes file quotes): NOT RUN (referee commits 72db1b18 / 75b8b52a not in this clone)"
  fi
else
  echo "rund (RUND fixes file quotes): NOT RUN (source commits not in this clone; fetch claude/referee, claude/referee-2)"
fi
# box 20 (docs/si/N5-ROOT-box20.md): BF-F_D at every S4a step of nep90 (MUT=1, equality flagged, bites); FREEZE-A (a) on its pieces and on
# lib2o (MUT2=1, one edge too many, bites on lib2o); ROOT-PIECE on nep90: 22 cuts = 7 fallbacks + 15 D-leaves, every piece within its bound
# (MUT=1, bound 2, bites).
N90="../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start"
o=$(python3 -I root/bffd.py --one $N90)
for k in "checks=7827 " "BFFD PASS"; do grep -q "$k" <<<"$o"; done
MUT=1 python3 -I root/bffd.py --one $N90 | grep -q "BFFD FAIL"
o=$(python3 -I root/shrink.py --one $N90)
for k in "IN_DLEAVE=53 " "pieces=20 " "SHRINK PASS"; do grep -q "$k" <<<"$o"; done
if grep -q "IN_SWITCH\|SPLIT_IN" <<<"$o"; then echo "unexpected switch / split entry on nep90"; exit 1; fi
RS=4 MUT2=1 python3 -I root/shrink.py --list fb2o/lib2o.txt 1 | grep -q "SHRINK FAIL"
o=$(python3 -I root/rootrun.py $N90)
for k in "cuts=22 (fb 7, DLEAVE 15, SWITCH 0)" "ROOTRUN_V=0 "; do grep -q "$k" <<<"$o"; done
MUT=1 python3 -I root/rootrun.py $N90 | grep -q "ROOTRUN_V=10 "
echo "root (BF-F_D, FREEZE-A pieces, ROOT-PIECE on nep90; three controls bite): PASS"
# packet P-N5-ROOT-box20: every «quote» verbatim at its tagged commit; the shifted-lines control fails. dleave.py on nep90 (26 leaves).
if git cat-file -e a7c141b8 && git cat-file -e 3732ab55; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-box20.md | grep -q "quotes=9 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-box20.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-ROOT-box20: 9 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-ROOT-box20 quotes): NOT RUN (source commits not in this clone)"
fi
o=$(python3 -I root/dleave.py --one $N90)
for k in "leaves=26 " "y_ROUTE_OWN=21" "DLEAVE PASS"; do grep -q "$k" <<<"$o"; done
if grep -q "y_RELAY_OWN" <<<"$o"; then echo "unexpected RELAY-and-OWN leave on nep90"; exit 1; fi
echo "root (D-leaves on nep90: 26, no RELAY-and-OWN): PASS"
# note §8: the naive FREEZE on A u {D-direct gates} fails on nep90 (188 of 948 Bellman-Ford checks in the root's gate region).
o=$(python3 -I root/bfgate.py --one $N90)
for k in "BFG_fail=188 " "bfg_checks=948 " "cutsA=22 " "cutsB=18 " "gs_a_checks=684 " "gs_b_checks=943"; do grep -q "$k" <<<"$o"; done
if grep -q "GS_A_V\|GS_B_V" <<<"$o"; then echo "GATE-SHIFT violated on nep90"; exit 1; fi
echo "root (GATE-LAG on nep90: 188 / 948 naive failures; GATE-SHIFT (a), (b) hold): PASS"
# note §9: FREEZE-G (a) on nep90's 22 G-intervals (2,531 checks).
o=$(python3 -I root/freezeg.py --one $N90)
for k in "ga_checks=2531 " "intervals=22" "FREEZEG PASS"; do grep -q "$k" <<<"$o"; done
echo "root (FREEZE-G (a) on nep90): PASS"
# packet P-N5-ROOT-add-box20 (addendum): 11 quotes verbatim; shifted control fails.
if git cat-file -e a7c141b8 && git cat-file -e 3732ab55; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-add-box20.md | grep -q "quotes=11 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-add-box20.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-ROOT-add-box20: 11 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-ROOT-add-box20 quotes): NOT RUN (source commits not in this clone)"
fi
# note §10 / DEAD box 20: on nep90 the root has 63 offset resets, 32 with no charge but its own rho.
o=$(python3 -I root/resets.py --one $N90)
for k in "R_DELTA_U=63 " "R_DELTA_U_ONLYSELF=32 " "max_resets_run=13 "; do grep -q "$k" <<<"$o"; done
echo "root (per-gate resets on nep90; the dead PING/FLIP charge reproduces): PASS"
# P-N5-CHOSEN fixes file: 22 quotes verbatim at the referees' commits; shifted control fails.
if git cat-file -e b3473114 && git cat-file -e d08011be && git cat-file -e aab45be6 && git cat-file -e bde1ea77; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CHOSEN-fixes-box19.md | grep -q "quotes=22 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CHOSEN-fixes-box19.md --mut | grep -q "QUOTES FAIL"
  echo "rund (P-N5-CHOSEN fixes file: 22 quotes verbatim; shifted control fails): PASS"
else
  echo "rund (P-N5-CHOSEN fixes file quotes): NOT RUN (referee commits not in this clone)"
fi
# box 21 (docs/si/N5-GCX-box21.md): G_c and X_u per fallback-free run on nep90 and mkpp K12; C-ONCE (no vertex migrates twice inside a
# C-interval, none late); control MUT=1 (whole run as one interval) must find a double migration on nep90.
o=$(python3 -I root/gcx.py --one $N90)
for k in "G_sum=15 " "X_sum=5 " "xv=14 " "runs=8 " "cint=82 "; do grep -q "$k" <<<"$o"; done
if grep -q "MIG2_cint\|MIG_LATE" <<<"$o"; then exit 1; fi
MUT=1 python3 -I root/gcx.py --one $N90 | grep -q "MIG2_cint=4 "
o=$(python3 -I root/gcx.py --one ../red/usplit/instances/pp_K12_n161.pg ../red/usplit/instances/pp_K12_n161.start)
for k in "G_max=2 " "X_max=13 " "cint_migt=13 " "mig_per_vertex_max=1 "; do grep -q "$k" <<<"$o"; done
if grep -q "MIG2_cint\|MIG_LATE" <<<"$o"; then exit 1; fi
echo "root (gcx: G_c, X_u on nep90 and pp_K12; no double migration inside a C-interval there, whole-run control bites): PASS"
# box 21 §4: U events by C-interval on the UF-ONCE killer so_th_n32 (8 inside, 6 at cuts, none late: CONJECTURE UL_C); control ULMUT=1
# (threshold 0) must fire. DEAD instances: cone_n65 (a vertex migrates twice inside a C-interval without D-direct gates), ueonce_n27 (an
# edge unforbid-switched twice inside one C-interval).
SO="../red/so/instances/so_th_n32.pg rund/instances/so_th_n32_s0.start"
o=$(UEV=1 python3 -I root/gcx.py --one $SO)
for k in "UR_cut=6 " "UR_in=8 "; do grep -q "$k" <<<"$o"; done
if grep -q "UL_C=\|UE2_Cr=" <<<"$o"; then exit 1; fi
UEV=1 ULMUT=1 python3 -I root/gcx.py --one $SO | grep -q "UL_C=8 "
python3 -I root/gcx.py --one root/instances/cone_n65.pg | grep -q "MIG2_cint=1 "
UEV=1 python3 -I root/gcx.py --one root/instances/ueonce_n27.pg | grep -q "UE2_Cr=1 "
echo "root (gcx: UL_C on so_th_n32, control fires; DEAD C-ONCE broad (cone_n65) and UE-ONCE_C (ueonce_n27) reproduce): PASS"
# box 21 §7: the abstract model ABS (acyclic): Lemma ABS-HEIGHT (steps <= DAG height) on 3,000 random games and a climbed one that reaches
# n steps; control ABSMUT=1 (height - 1) must fire.
python3 -I root/absmodel.py --rand 3000 10 1 | grep -q "games=3000 steps_ge_n=0 steps_gt_n=0 max_steps 4"
o=$(python3 -I root/absmodel.py --climb 3000 5 1); grep -q "best steps 5 " <<<"$o"
if grep -q "HEIGHT_V\|MONO_V" <<<"$o"; then exit 1; fi
ABSMUT=1 python3 -I root/absmodel.py --climb 3000 5 1 | grep -q "HEIGHT_V="
echo "root (absmodel: ABS-HEIGHT on random and climbed DAGs, sharp at n = 5; control fires): PASS"
# box 21 §9: the cyclic-lift obstruction instance reproduces; FINAL-EACH holds on 3,000 random cyclic games (n = 5); with W-ties broken away
# from the current choice (SMALL=1 TIEMAX=1), Lemma ABS-TIE's bound holds on random DAGs.
python3 -I root/abscyc.py --deep | grep -q "DEEP REPRODUCED"
o=$(python3 -I root/abscyc.py --final 3000 5 5); grep -q "trans=3296" <<<"$o"
if grep -q "FINAL_EACH_V\|DEEP_ANY_V" <<<"$o"; then exit 1; fi
o=$(SMALL=1 TIEMAX=1 python3 -I root/absmodel.py --rand 3000 8 3); grep -q "games=3000" <<<"$o"
if grep -q "DSUM_V\|MONO_V" <<<"$o"; then exit 1; fi
SMALL=1 TIEMAX=1 ABSMUT=1 python3 -I root/absmodel.py --climb 3000 5 1 | grep -q "over_height="
echo "root (abscyc obstruction instance, FINAL-EACH; absmodel ABS-TIE with ties broken away from the current choice; control fires): PASS"
# P-N5-GCX-box21 packet: 5 quotes verbatim at trunk 7d87f9be; shifted control fails.
if git cat-file -e 7d87f9be; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-GCX-box21.md | grep -q "quotes=5 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-GCX-box21.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-GCX-box21: 5 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-GCX-box21 quotes): NOT RUN (source commit not in this clone)"
fi
# box 22 (docs/si/N5-EXIT-box22.md): exit changes on nep90_n40. Lemmas MONO-REF, PUSH, EXIT-RHO, DEPTH, EXIT-RED: 0 violations; sum EXIT = 53
# (= L-NEW's PARCHG), every value push is P1UP and DOWN; controls MRMUT=1 (reference off the play) and PUSHMUT=1 (rise demanded of p2) bite.
o=$(MR=1 python3 -I root/exitx.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start)
for k in "EXIT_sum=53 " "EXIT_max=18 " "chv_P1UP=13 " "chv_DOWN=13 " "n_alldown=18 " "n_other=22 " "mr_checks=4609 " "EXITX PASS"; do grep -q "$k" <<<"$o"; done
if grep -q "_V=\|chv_UP=" <<<"$o"; then echo "exitx: violation on nep90"; exit 1; fi
MR=1 MRMUT=1 python3 -I root/exitx.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "MR_V="
PUSHMUT=1 python3 -I root/exitx.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "PUSH_V=16 "
echo "root (exitx on nep90: MONO-REF, PUSH, EXIT-RHO, DEPTH hold, EXIT 53 / 18; controls MRMUT, PUSHMUT bite): PASS"
# box 22 (docs/si/N5-ABSCYC-box22.md): Theorem ABS-DEPTH in the cyclic model (play final from step d*(v), the depth in the final forest) on
# 2,844 random games (GEN held in all); the tie instance (GEN fails, vertex 2 past d*) reproduces; control MUT=1 (d* - 1) bites.
o=$(python3 -I root/absdepth.py 1000 4,5,6 1); grep -q "runs=2844 runs_nogen=0 steps_gt_maxfinaldepth=0" <<<"$o"; grep -q "ABSDEPTH PASS" <<<"$o"
python3 -I root/absdepth.py --tie | grep -q "TIE REPRODUCED"
MUT=1 python3 -I root/absdepth.py 1000 4,5,6 1 | grep -q "DEPTH_V=1938 "
echo "root (absdepth: ABS-DEPTH on 2,844 cyclic-model runs; tie instance; control bites): PASS"
# box 22 §8 (docs/si/N5-EXIT-box22.md): the Even side on nep90_n40. C-cuts by kind; no late Even switch in a pure C-interval; Lemma
# E-ONEWAY (no return of an Even vertex to a successor left by a nested switch) on 11 windows; control E1MUT=1 (window conditions dropped) bites.
o=$(python3 -I root/evenside.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start)
for k in "E1_chk=11 " "cut_AG=15 " "cut_DCH=19 " "cut_OSB=38 " "EXIT_at_cut=31 " "EXIT_in=2 "; do grep -q "$k" <<<"$o"; done
if grep -q "E1_V\|PURELATE" <<<"$o"; then echo "evenside: violation on nep90"; exit 1; fi
E1MUT=1 python3 -I root/evenside.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "E1_V=10 "
echo "root (evenside on nep90: cuts AG 15 / DCH 19 / OSB 38, exits at cuts 31 of 33, E-ONEWAY holds; control bites): PASS"
# box 22 (docs/si/N5-GCILEN-box22.md): Theorem STATIC-DEPTH (sigma-bar constant, (H3), (H4), GEN_W: settled from d*(v), length <= max d*):
# tight on b6_xs_n24 (length 21 = max d*), holds on long121 (28 intervals, global C-intervals too); control MUT=1 (d* - 1) bites.
o=$(python3 -I root/staticdepth.py --one ../n5-exhaustive/instances/b6_xs_n24.pg); grep -q "dstar_max=21 intervals=1 len_max=21 " <<<"$o"; grep -q "STATICDEPTH PASS" <<<"$o"
o=$(GCI=1 python3 -I root/staticdepth.py --one ../new/box48/instances/long121_n40.pg ../new/box48/instances/long121_n40.start)
grep -q "checked=27 " <<<"$o"; grep -q "gci=29 " <<<"$o"; grep -q "STATICDEPTH PASS" <<<"$o"
MUT=1 python3 -I root/staticdepth.py --one ../n5-exhaustive/instances/b6_xs_n24.pg | grep -q "SETTLE_V=21 "
echo "root (staticdepth: STATIC-DEPTH tight on b6_xs_n24, holds on long121 incl. global C-intervals; control bites): PASS"
# P-N5-DEPTH-box22 packet: 12 quotes verbatim (SPEC, RESULTS, FBPOLY at trunk 982f5c62; RESULTS at 58061d91; GCX at 02240121; R91 at l-red
# 54de3f2f); shifted control fails.
if git cat-file -e 982f5c629 && git cat-file -e 58061d91 && git cat-file -e 02240121 && git cat-file -e 54de3f2f; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-box22.md | grep -q "quotes=12 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-box22.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-DEPTH-box22: 12 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-DEPTH-box22 quotes): NOT RUN (a source commit is not in this clone)"
fi
# P-N5-DEPTH-add-box22 (conditional companion): 5 quotes verbatim at trunk 78bc0e6a; shifted control fails.
if git cat-file -e 78bc0e6a8; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-add-box22.md | grep -q "quotes=5 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-add-box22.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-DEPTH-add-box22: 5 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-DEPTH-add-box22 quotes): NOT RUN (source commit not in this clone)"
fi
# box 23 (docs/si/N5-ALT-box23.md): ALTERNATION / (G1). DEAD GATE-ONEWAY on pp_K12_n161 (21 gate returns inside one global C-interval, a gate of
# out-degree 3 changes 13 times); DEAD FRESH3 on ret14_n48 (2 sigma-bar-changing in-interval transitions with no fresh Even edge, no fresh gate
# option and no A-shrink); FRESH3 holds on post31_n48 and the control FMUT=1 (no credit for A-shrinks) bites there; DEAD TOP-ONCE on lev_l_sc
# (multiplicity 7 in one run); no Xi fall in a phase (WRONG absent).
o=$(python3 -I root/gateret.py --one ../red/usplit/instances/pp_K12_n161.pg ../red/usplit/instances/pp_K12_n161.start)
for k in "RET_gci_in=21 " "MAXCH_run=13 " "gch_in=23 "; do grep -q "$k" <<<"$o"; done
o=$(python3 -I root/fresh.py --one ../n5-epoch/instances/ret14_n48.pg ../n5-epoch/instances/ret14_n48.start); grep -q "NOFRESH3_gci_gch=2 " <<<"$o"
o=$(python3 -I root/fresh.py --one ../red/so/instances/post31_n48.pg); if grep -q "NOFRESH3_gci_gch" <<<"$o"; then echo "fresh: FRESH3 fails on post31"; exit 1; fi
FMUT=1 python3 -I root/fresh.py --one ../red/so/instances/post31_n48.pg | grep -q "NOFRESH3_gci_gch=1 "
o=$(python3 -I root/mrise.py --one orlens/instances/lev_l_sc.pg); grep -q "MULT_run=7 " <<<"$o"; if grep -q "WRONG" <<<"$o"; then echo "mrise: Xi fall"; exit 1; fi
echo "root (box 23 ALT: GATE-ONEWAY, FRESH3, TOP-ONCE dead with instances; FRESH3 holds on post31, control bites): PASS"
# P-N5-ROOT-fixes-box20 (repairs to P-N5-ROOT d3788bc0 + addendum af1c7ad4): 36 quotes verbatim (packets at ced5cf27 / 829003b2, FLIP at
# 7ea3d8cf, REFEREE 619fccf2 / 65f55427, REFEREE-2 3febbfaf / f5381a5c); shifted control fails.
if git cat-file -e ced5cf27 && git cat-file -e 829003b2 && git cat-file -e 7ea3d8cf && git cat-file -e 619fccf2 && git cat-file -e 65f55427 && git cat-file -e 3febbfaf && git cat-file -e f5381a5c; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-fixes-box20.md | grep -q "quotes=36 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-ROOT-fixes-box20.md --mut | grep -q "QUOTES FAIL"
  echo "root (P-N5-ROOT fixes: 36 quotes verbatim; shifted control fails): PASS"
else
  echo "root (P-N5-ROOT fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# box 23 §8 (docs/si/N5-ALT-box23.md): DEAD XR-LIN. long121_n40 + one Odd reader (l121reader_n41): the run on the old vertices is unchanged
# (SAME) and the reader's Xi changes 86 > 2n = 82 times in phase [1, 122]. Six readers (l121reader6_n46): SAME, and C-cuts 53 -> 73.
o=$(python3 -I root/orcheck.py ../new/box48/instances/long121_n40.pg ../new/box48/instances/long121_n40.start root/instances/l121reader_n41.pg root/instances/l121reader_n41.start)
grep -q "^SAME " <<<"$o"; grep -q "phases_equal True" <<<"$o"; grep -q "XR_o 86 " <<<"$o"
o=$(python3 -I root/orcheck.py ../new/box48/instances/long121_n40.pg ../new/box48/instances/long121_n40.start root/instances/l121reader6_n46.pg root/instances/l121reader6_n46.start)
grep -q "^SAME " <<<"$o"
python3 -I root/evenside.py --one root/instances/l121reader6_n46.pg root/instances/l121reader6_n46.start | grep -q "K_sum=73 "
echo "root (box 23 §8: XR-LIN dead on l121reader_n41, run unchanged; six readers raise K 53 -> 73 with the run unchanged): PASS"
# box 23 §10: DEAD SW-LIN on swlin_kill_n26 (Even vertex 19 switches 27 > n = 26 times in phase [1, 47]); L-COMP's independent n5b (spec mode)
# gives the identical state sequence.
o=$(python3 -I root/n5bcmp.py root/instances/swlin_kill_n26.pg root/instances/swlin_kill_n26.start)
grep -q "identical state sequences: True" <<<"$o"; grep -q "switching 27 times; n = 26; > n: True" <<<"$o"
echo "root (box 23 §10: SW-LIN dead on swlin_kill_n26, n5b agrees): PASS"
# box 23 §12: an Even reader on long121_n40 (l121ereader_n41) leaves the run SAME (fallbacks included) and switches 16 times in phase [1, 122]
# (base maximum 12).
python3 -I root/ereader.py ../new/box48/instances/long121_n40.pg ../new/box48/instances/long121_n40.start 1,10,13,14,16,17,20,23,30,31,32,34,38 30 | grep -q "^SAME .* (16, 3, (1, 122))"
echo "root (box 23 §12: Even reader on long121 clean, 16 switches > base 12): PASS"
# P-N5-GCX-fixes-box21 (repairs to P-N5-GCX 5a91bebb): 29 quotes verbatim (packet at 02240121; REFEREE e01bdec6 / 159c8f04; REFEREE-2 fe04ca32 /
# fc63f1f1); shifted control fails.
if git cat-file -e 02240121 && git cat-file -e e01bdec6 && git cat-file -e 159c8f04 && git cat-file -e fe04ca32 && git cat-file -e fc63f1f1; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-GCX-fixes-box21.md | grep -q "quotes=29 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-GCX-fixes-box21.md --mut | grep -q "QUOTES FAIL"
  echo "root (P-N5-GCX fixes: 29 quotes verbatim; shifted control fails): PASS"
else
  echo "root (P-N5-GCX fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# box 23 §8 (REFEREE R-N5-READER, e83fd19d): condition (R) of Theorem READER-INV holds for l121reader_n41 and all six readers of l121reader6_n46.
for r in l121reader_n41 l121reader6_n46; do
  python3 -I root/orcheck.py ../new/box48/instances/long121_n40.pg ../new/box48/instances/long121_n40.start root/instances/$r.pg root/instances/$r.start | grep -q "^condition (R): True"
done
echo "root (box 23 §8: condition (R) holds on both reader instances): PASS"
# P-N5-CORE-box23: 10 quotes verbatim (RESULTS and SPEC at trunk 33f43c20, FBRED at 3732ab55); shifted control fails. corecheck on nep90_n40:
# (C1), (C3), (C4) hold (202 switches, 105 clean gate changes); control MUT=1 bites (167).
if git cat-file -e 33f43c20 && git cat-file -e 3732ab55; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CORE-box23.md | grep -q "quotes=10 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CORE-box23.md --mut | grep -q "QUOTES FAIL"
  echo "root (packet P-N5-CORE-box23: 10 quotes verbatim; shifted control fails): PASS"
else
  echo "root (packet P-N5-CORE-box23 quotes): NOT RUN (a source commit is not in this clone)"
fi
o=$(python3 -I root/corecheck.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start); grep -q "C3=202 C4_clean=105 " <<<"$o"; grep -q "CORE PASS" <<<"$o"
MUT=1 python3 -I root/corecheck.py --one ../red/rec0/instances/nep90_n40.pg rund/instances/nep90_n40.start | grep -q "C3_V=167 "
echo "root (corecheck: P-N5-CORE (C1), (C3), (C4) on nep90; control bites): PASS"
# P-N5-DEPTH-fixes-box22 (14 quotes) and P-N5-DEPTH-add-fixes-box22 (20 quotes): verbatim at 2201aa2d / aa6061d1 (packets), dc4e47b8 (REFEREE),
# 4eb5cbfb (REFEREE-2); shifted controls fail.
if git cat-file -e 2201aa2d && git cat-file -e aa6061d1 && git cat-file -e dc4e47b8 && git cat-file -e 4eb5cbfb; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-fixes-box22.md | grep -q "quotes=14 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-fixes-box22.md --mut | grep -q "QUOTES FAIL"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-add-fixes-box22.md | grep -q "quotes=20 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-DEPTH-add-fixes-box22.md --mut | grep -q "QUOTES FAIL"
  echo "root (P-N5-DEPTH and DEPTH-add fixes: 14 + 20 quotes verbatim; shifted controls fail): PASS"
else
  echo "root (P-N5-DEPTH / DEPTH-add fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# box 24 (docs/si/N5-RUNLIN-box24.md): the pinned RUN-LIN records (longest fallback-free run, two engines) and I_tau = empty along them.
o=$(python3 -I runlin/anatomy.py runlin/instances/best60_n34.pg runlin/instances/best60_n34.start); grep -q "run \[1,61\] len 60 " <<<"$o"
python3 -I root/n5bcmp.py runlin/instances/best60_n34.pg runlin/instances/best60_n34.start | grep -q "identical state sequences: True"
python3 -I runlin/keeper.py ../red/n3/instances/run49_n32.pg ../red/n3/instances/run49_n32.start | grep -q "with I_tau nonempty 0 "
echo "runlin (box 24: best60_n34 run 60, n5b identical; run49 I_tau empty along its run): PASS"
# box 24 §7: DEAD RUN-LIN. runfam_K10 (n 49): one phase, 0 fallbacks, fallback-free run 99 > 2n = 98 (n5x; n5b identical); the generator
# reproduces the pinned instance; I_tau empty along the run.
o=$(python3 -I runlin/anatomy.py runlin/instances/runfam_K10.pg runlin/instances/runfam_K10.start); grep -q "phase \[1,100\] run \[1,100\] len 99 " <<<"$o"
python3 -I root/n5bcmp.py runlin/instances/runfam_K10.pg runlin/instances/runfam_K10.start | grep -q "n5b iterations 100 fallbacks 0 states 101 | n5x states 101 | identical state sequences: True"
python3 -I runlin/keeper.py runlin/instances/runfam_K10.pg runlin/instances/runfam_K10.start | grep -q "with I_tau nonempty 0 "
t=$(mktemp -d); python3 -I runlin/mkrunfam.py 10 $t/f | grep -q "K 10 n 49 run 99 run-2n 1"
cmp -s $t/f.pg runlin/instances/runfam_K10.pg; cmp -s $t/f.start runlin/instances/runfam_K10.start; rm -rf $t
echo "runlin (box 24 §7: DEAD RUN-LIN, runfam_K10 run 99 > 98, n5b identical, generator reproduces the pin): PASS"
# P-N5-CORE-fixes-box23: 35 quotes verbatim (packet 081ae740, RESULTS 33f43c20 / 84ab5daf, REFEREE 8641ae40, REFEREE-2 b28d1ba9); shifted control fails.
if git cat-file -e 081ae740 && git cat-file -e 33f43c20 && git cat-file -e 84ab5daf && git cat-file -e 8641ae40 && git cat-file -e b28d1ba9; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CORE-fixes-box23.md | grep -q "quotes=35 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-CORE-fixes-box23.md --mut | grep -q "QUOTES FAIL"
  echo "root (P-N5-CORE fixes: 35 quotes verbatim; shifted control fails): PASS"
else
  echo "root (P-N5-CORE fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# box 25 (docs/si/N5-PIECE-box25.md): Theorem STATIC-DEPTH' data. kw25_n32's piece [0,25] fails R77's (H3) and (H4) and is covered by
# STATIC-DEPTH' (two-frame form); frz24 has a piece with an end-state cycle formed inside it ((H3') fails) and an epoch split; MUT=1 bites.
o=$(python3 -I piece/pieceh.py --one ../red/xing/instances/kw25_n32.pg); grep -q "F_len_max=25 " <<<"$o"; grep -q "h4=1 " <<<"$o"; grep -q "PIECE PASS" <<<"$o"
o=$(python3 -I piece/sdprime.py --one ../red/xing/instances/kw25_n32.pg); grep -q "beyond_len_max=25 checked=2 checked_beyond_H3=1 " <<<"$o"; grep -q "SDPRIME PASS" <<<"$o"
o=$(python3 -I piece/sdprime.py --one ../red/n5inj/instances/frz24.pg); grep -q "h3p_fail=1 " <<<"$o"; grep -q "SDPRIME PASS" <<<"$o"
MUT=1 python3 -I piece/sdprime.py --one ../red/n5inj/instances/frz24.pg | grep -q "SDPRIME FAIL"
o=$(python3 -I piece/epochs.py --one ../red/n5inj/instances/frz24.pg); grep -q "k_max=2 " <<<"$o"; grep -q "EPOCHS PASS" <<<"$o"
echo "piece (box 25: STATIC-DEPTH' covers kw25 [0,25] outside R77; frz24 (H3') failure and 2 epochs; MUT=1 bites): PASS"
# box 25 (docs/si/N5-GRUN-box25.md): Lemma GATE-RISE on pftheta34 (MUT bites); G is not intrinsic: runfam_K10 + 25 readers has G 91 at n 74
# with the run unchanged, + 25 anchors G^K 91 at n 99 (generator reproduces the pin); SEG stays 9; STATIC-DEPTH-REL checks pass.
python3 -I grun/gaterise.py --one ../red/so/instances/pftheta34_n32.pg | grep -q "GATERISE PASS"
MUT=1 python3 -I grun/gaterise.py --one ../red/so/instances/pftheta34_n32.pg | grep -q "GATERISE FAIL"
python3 -I grun/gstat.py --one grun/out/rdr_K10.pg grun/out/rdr_K10.start | grep -q "TOP G 91 n 74 run 99 "
o=$(python3 -I grun/relseg.py --one grun/out/rdr_K10.pg grun/out/rdr_K10.start); grep -q "SEG_max=9 " <<<"$o"; grep -q "RELSEG PASS" <<<"$o"
o=$(python3 -I grun/relseg.py --one runlin/instances/runfam_K10.pg runlin/instances/runfam_K10.start); grep -q "SEG_max=9 " <<<"$o"; grep -q "RELSEG PASS" <<<"$o"
t=$(mktemp -d); python3 -I grun/anchor.py grun/out/rdr_K10.pg grun/out/rdr_K10.start 1 100 $t/a | grep -q "anchors 25 n 99 SAME True readers in K 25 run 99 G 91 G^K 91 SEG 9 fallbacks in \[A,B\] 0"
cmp -s $t/a.pg grun/out/anc_K10.pg; cmp -s $t/a.start grun/out/anc_K10.start; rm -rf $t
echo "grun (box 25: GATE-RISE on pftheta34, MUT bites; readers G 9 -> 91 with run 99 fixed, anchors G^K 91, SEG 9; anchor generator reproduces the pin): PASS"
# P-N5-SDPRIME-box25 (FROZEN, sha1 54678c38a04842bd936a9bf4b241d47ad8ab90a3): 12 quotes verbatim (trunk 55e0bcbda); shifted control fails.
if git cat-file -e 55e0bcbda; then
  echo "54678c38a04842bd936a9bf4b241d47ad8ab90a3  ../../docs/si/P-N5-SDPRIME-box25.md" | sha1sum -c --quiet
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-SDPRIME-box25.md | grep -q "quotes=12 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-SDPRIME-box25.md --mut | grep -q "QUOTES FAIL"
  echo "piece (P-N5-SDPRIME frozen sha1; 12 quotes verbatim; shifted control fails): PASS"
else
  echo "piece (P-N5-SDPRIME quotes): NOT RUN (source commit 55e0bcbda not in this clone)"
fi
# P-N5-REL-box25 (FROZEN, sha1 f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb): 17 quotes verbatim (trunk b28123a58); shifted control fails.
if git cat-file -e b28123a58; then
  echo "f79300a2d01cfb0aa27ad7214bcefbd84eafd7bb  ../../docs/si/P-N5-REL-box25.md" | sha1sum -c --quiet
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-REL-box25.md | grep -q "quotes=17 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-REL-box25.md --mut | grep -q "QUOTES FAIL"
  echo "grun (P-N5-REL frozen sha1; 17 quotes verbatim; shifted control fails): PASS"
else
  echo "grun (P-N5-REL quotes): NOT RUN (source commit b28123a58 not in this clone)"
fi
# P-N5-SDPRIME-fixes-box25 (repairs only): 12 quotes verbatim (REFEREE d693a6fe7, REFEREE-2 9784229a2, RESULTS 55e0bcbda / b28123a58); shifted control fails.
if git cat-file -e d693a6fe7 && git cat-file -e 9784229a2 && git cat-file -e b28123a58; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-SDPRIME-fixes-box25.md | grep -q "quotes=12 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-SDPRIME-fixes-box25.md --mut | grep -q "QUOTES FAIL"
  echo "piece (P-N5-SDPRIME fixes: 12 quotes verbatim; shifted control fails): PASS"
else
  echo "piece (P-N5-SDPRIME fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# P-N5-REL-fixes-box25 (repairs only): 12 quotes verbatim (REFEREE a343d6b4, REFEREE-2 b6811cf1, RESULTS ab545081b / b28123a58); shifted control fails.
if git cat-file -e a343d6b4 && git cat-file -e b6811cf1 && git cat-file -e ab545081b && git cat-file -e b28123a58; then
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-REL-fixes-box25.md | grep -q "quotes=12 bad=0"
  python3 -I rund/quotecheck.py ../../docs/si/P-N5-REL-fixes-box25.md --mut | grep -q "QUOTES FAIL"
  echo "grun (P-N5-REL fixes: 12 quotes verbatim; shifted control fails): PASS"
else
  echo "grun (P-N5-REL fixes quotes): NOT RUN (a source commit is not in this clone)"
fi
# box 25 (DEAD.md box 25): DEAD L-WAVE. lwkill_n31: run [2,40] (38), non-L gap [2,39] of 37 > 30 (lwave FAIL), n5b identical; L-WAVE' holds there.
o=$(python3 -I grun/lwave.py --one grun/instances/lwkill_n31.pg grun/instances/lwkill_n31.start); grep -q "EXAMPLE ('grun/instances/lwkill_n31.pg', 2, 39, 31)" <<<"$o"; grep -q "LWAVE FAIL" <<<"$o"
python3 -I root/n5bcmp.py grun/instances/lwkill_n31.pg grun/instances/lwkill_n31.start | grep -q "n5b iterations 40 fallbacks 0 states 41 | n5x states 41 | identical state sequences: True"
PMODE=1 python3 -I grun/lwave.py --one grun/instances/lwkill_n31.pg grun/instances/lwkill_n31.start | grep -q "LWAVE PASS"
echo "grun (box 25: DEAD L-WAVE, lwkill_n31 gap 37 > 30, n5b identical; L-WAVE' holds there): PASS"
# box 26 (docs/si/N5-LWP-box26.md): L-WAVE' gap anatomy and the dead candidate invariants. lwp_a's gap [1,26] has 25 = n - 1 transitions:
# LAST-SWITCH per gap fails there (2 transitions) while SEG-LAST holds on its 3 segments; PV-STEP fails at t = 2; GAP-DEPTH 25 > 23;
# SEG-LAST fails on cw11_n24's pieces (control) and on whole runs (control); SWL / NEVEN hold on lwp_a.
o=$(python3 -I lwp/lastsw.py --one grun/out/lwp_a.pg grun/out/lwp_a.start); grep -q "LS_V=2 " <<<"$o"; grep -q "gap_minus_nEven_max_plus1000=1000 " <<<"$o"; if grep -q "SWL_V" <<<"$o"; then exit 1; fi
o=$(python3 -I lwp/seglast.py --one grun/out/lwp_a.pg grun/out/lwp_a.start); grep -q "segs=3 trans=23" <<<"$o"; grep -q "SEGLAST PASS" <<<"$o"
MODE=piece python3 -I lwp/seglast.py --one ../red/kw/instances/cw11_n24.pg | grep -q "SEGLAST FAIL"
MODE=run python3 -I lwp/seglast.py --one grun/instances/lwkill_n31.pg grun/instances/lwkill_n31.start | grep -q "SEGLAST FAIL"
python3 -I lwp/vstep.py --one grun/out/lwp_a.pg grun/out/lwp_a.start | grep -q "PV_V=1 "
python3 -I lwp/gapdepth.py --one grun/out/lwp_a.pg grun/out/lwp_a.start | grep -q "EXAMPLE ('grun/out/lwp_a.pg', 1, 26, 1, 26, 25, 23, 26)"
echo "lwp (box 26: lwp_a gap n - 1 kills per-gap LAST-SWITCH, PV-STEP, GAP-DEPTH; SEG-LAST holds there, fails on pieces / runs as controls): PASS"
# box 26 (docs/si/N5-LWP-box26.md §7): Theorem LAST-STEP data. Frontier vertices exist at every step of lwp_a's segments (MUT=1 bites);
# lwp/instances/cycset_kill_n60 (= climb h4a_k) kills CYC-SET with no frontier vertex at t = 0, while SEG-LAST and SET-STEP hold there.
python3 -I lwp/laststep.py --one grun/out/lwp_a.pg grun/out/lwp_a.start | grep -q "LASTSTEP PASS"
MUT=1 python3 -I lwp/laststep.py --one grun/out/lwp_a.pg grun/out/lwp_a.start | grep -q "LASTSTEP FAIL"
echo "957c7c9e2ce5a6d57890e42b0e8ca0a0911ecefd  lwp/instances/cycset_kill_n60.pg" | sha1sum -c --quiet
o=$(python3 -I lwp/laststep.py --one lwp/instances/cycset_kill_n60.pg); grep -q "CYCSET_V=1 FR_V=1 FR_V_h4fail=1 " <<<"$o"; grep -q "CYCSET FAIL" <<<"$o"
o=$(python3 -I lwp/seglast.py --one lwp/instances/cycset_kill_n60.pg); grep -q "SEGLAST PASS" <<<"$o"; if grep -q "SS_V" <<<"$o"; then exit 1; fi
echo "lwp (box 26: LAST-STEP frontier on lwp_a, MUT bites; cycset_kill_n60 kills CYC-SET, SEG-LAST / SET-STEP hold): PASS"
# box 26 (note §8): K-REDUCTION data. karena_kill_n71 kills K-ARENA (one terminal part at t = 0, not arena-complete); SEG-LAST holds.
echo "8b659497688c47075235957ae1e636b5564ec235  lwp/instances/karena_kill_n71.pg" | sha1sum -c --quiet
o=$(python3 -I lwp/laststep.py --one lwp/instances/karena_kill_n71.pg); grep -q "KARENA_V=1 " <<<"$o"; grep -q "kar_nontrivial=1 " <<<"$o"; grep -q "KSET PASS" <<<"$o"
python3 -I lwp/seglast.py --one lwp/instances/karena_kill_n71.pg | grep -q "SEGLAST PASS"
o=$(python3 -I lwp/laststep.py --one lwp/instances/cycset_kill_n60.pg); grep -q "KARENA PASS" <<<"$o"; grep -q "kar_nontrivial=1 " <<<"$o"
echo "lwp (box 26: K-REDUCTION holds on cycset_kill_n60's nontrivial part; karena_kill_n71 kills K-ARENA, SEG-LAST holds): PASS"
# box 26: setstep_kill_n71 kills SET-STEP (SS_V=1) while SEG-LAST holds; WX-ARENA fails on cycset_kill_n60.
echo "b6360888a8180a9afef84c38845500f46626b548  lwp/instances/setstep_kill_n71.pg" | sha1sum -c --quiet
o=$(python3 -I lwp/seglast.py --one lwp/instances/setstep_kill_n71.pg); grep -q "SS_V=1 " <<<"$o"; grep -q "SEGLAST PASS" <<<"$o"
python3 -I lwp/laststep.py --one lwp/instances/cycset_kill_n60.pg | grep -q "WXARENA FAIL"
echo "lwp (box 26: setstep_kill_n71 kills SET-STEP, SEG-LAST holds; WX-ARENA fails on cycset_kill_n60): PASS"
# box 27 (docs/si/N5-LAY-box27.md): W-sinks. On the three box-26 kill pins every sink lemma holds (SINK-OFF both frames, H-sinks ready,
# ready W-sinks keep sigma_b), CONJECTURE WSINK-READY (= W-GROW) holds at every step, and MUT=1 (sinks of the both-frame set N_t,
# box 26's WX-ARENA notion) bites on each pin: the W-frame sink is what covers the steps with no frontier vertex.
for p in karena_kill_n71:5:6:6 cycset_kill_n60:4:5:5 setstep_kill_n71:3:3:3; do
  IFS=: read f tr ws wr <<<"$p"
  o=$(python3 -I lay/wsink.py --one lwp/instances/$f.pg); grep -q "trans=$tr wsinks=$ws wsinks_ready=$wr" <<<"$o"
  if grep -q "FAIL" <<<"$o"; then echo "lay: sink lemma or WSINK-READY failure on $f"; exit 1; fi   # (a bare "! grep" is exempt from set -e)
  MUT=1 python3 -I lay/wsink.py --one lwp/instances/$f.pg | grep -q "^WSR FAIL"
done
python3 -I lay/wsink.py --one grun/out/lwp_a.pg grun/out/lwp_a.start | grep -q "steps_with_bothsink=23 trans=23 wsinks=31 wsinks_ready=31"
echo "lay (box 27: sink lemmas and WSINK-READY on the box-26 kill pins and lwp_a; MUT=1 (N_t-sinks) bites on each pin): PASS"
# box 27: lay/instances/wgrow_kill_n90 kills W-GROW (WSR_V=1, t = 1: W-sinks 37, 57 unready); n5b gives the identical state sequence;
# the sink lemmas, H-GROW and SEG-LAST hold there.
echo "f9a7ef090b3df5bb4293301e6bd1236e33a92cd0  lay/instances/wgrow_kill_n90.pg" | sha1sum -c --quiet
echo "a4ead4deae5534731a199c8697c072f407643ca2  lay/instances/wgrow_kill_n90.start" | sha1sum -c --quiet
o=$(python3 -I lay/wsink.py --one lay/instances/wgrow_kill_n90.pg lay/instances/wgrow_kill_n90.start)
grep -q "WSR_V=1 hsinks=6 segs=1 steps_hsink_switch=3 " <<<"$o"; grep -q "EXAMPLE ('WSR', 'lay/instances/wgrow_kill_n90.pg', 0, 3, 1, \[37, 57\]" <<<"$o"
for k in WSOFF HSOFF HSR WSL SS NOSINK; do grep -q "^$k PASS" <<<"$o"; done; grep -q "^WSR FAIL" <<<"$o"
python3 -I lwp/seglast.py --one lay/instances/wgrow_kill_n90.pg lay/instances/wgrow_kill_n90.start | grep -q "SEGLAST PASS"
python3 -I root/n5bcmp.py lay/instances/wgrow_kill_n90.pg lay/instances/wgrow_kill_n90.start | grep -q "n5b iterations 9 fallbacks 1 states 10 | n5x states 10 | identical state sequences: True"
echo "lay (box 27: wgrow_kill_n90 kills W-GROW, n5b identical; sink lemmas, H-GROW, SEG-LAST hold): PASS"
# box 27: lay/instances/hgrow_kill_n89 kills H-GROW (H-sinks switch to target at 1 of 7 steps) while W-GROW, SINK-GROW and SEG-LAST hold;
# no step has a frontier vertex; n5b gives the identical state sequence.
echo "998a4a5e770c97b409ebf9f0a9d0ca08fac9bcbd  lay/instances/hgrow_kill_n89.pg" | sha1sum -c --quiet
echo "5895810a61760e4180d70202911768bd75f2beea  lay/instances/hgrow_kill_n89.start" | sha1sum -c --quiet
o=$(python3 -I lay/wsink.py --one lay/instances/hgrow_kill_n89.pg lay/instances/hgrow_kill_n89.start)
grep -q "hsinks=21 segs=1 steps_hsink_switch=1 steps_unready_wsink=0 steps_with_bothsink=0 trans=7 wsinks=14 wsinks_ready=14" <<<"$o"
if grep -q "FAIL" <<<"$o"; then echo "lay: unexpected failure on hgrow_kill_n89"; exit 1; fi
python3 -I lwp/seglast.py --one lay/instances/hgrow_kill_n89.pg lay/instances/hgrow_kill_n89.start | grep -q "SEGLAST PASS"
python3 -I root/n5bcmp.py lay/instances/hgrow_kill_n89.pg lay/instances/hgrow_kill_n89.start | grep -q "n5b iterations 13 fallbacks 0 states 14 | n5x states 14 | identical state sequences: True"
echo "lay (box 27: hgrow_kill_n89 kills H-GROW, n5b identical; W-GROW, SINK-GROW, SEG-LAST hold): PASS"
# box 27: lay/instances/seglast_kill_n110 kills CONJECTURE SEG-LAST and SINK-GROW: REL segment [2, 8] of the run [2, 8], t = 2, the only
# switch is vertex 1, 82 -> 25, and 1 switches again at 7. Reproduced from n5b alone (lay/relcheck.py); observed GEN_W holds.
echo "8a2201816d3a522cd2c4da238678d9f6b075f68a  lay/instances/seglast_kill_n110.pg" | sha1sum -c --quiet
echo "107cbf0828cdf1120d8f70b80cdef0e75e9908a4  lay/instances/seglast_kill_n110.start" | sha1sum -c --quiet
o=$(python3 -I lwp/seglast.py --one lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start); grep -q "SEGLAST FAIL" <<<"$o"
grep -q "EXAMPLE ('lay/instances/seglast_kill_n110.pg', 2, 8, \[2\]" <<<"$o"
o=$(python3 -I lay/wsink.py --one lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start); grep -q "^SS FAIL" <<<"$o"
for k in WSOFF HSOFF HSR WSL NOSINK; do grep -q "^$k PASS" <<<"$o"; done
o=$(python3 -I lay/relcheck.py lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start 2 8 2)
grep -q "tau constant on \[a, b\]: True | no fallback at transitions a..b-1: True" <<<"$o"; grep -q "tau_(a-1) == tau_a: False" <<<"$o"
grep -q "REL-admissible on \[a, b\]: True | REL at a - 1: False" <<<"$o"; grep -q "switchers at t = 2: \[(1, 82, 25, 'switches again at', \[7\])\]" <<<"$o"
grep -q "SEG-LAST fails at t: True" <<<"$o"; grep -q "observed GEN_W failures on \[a, b\] (S1 rank order): 0" <<<"$o"
python3 -I root/n5bcmp.py lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start | grep -q "n5b iterations 16 fallbacks 0 states 17 | n5x states 17 | identical state sequences: True"
echo "lay (box 27: seglast_kill_n110 kills SEG-LAST and SINK-GROW, reproduced from n5b alone; sink lemmas hold): PASS"
# box 27: lay/instances/seglast_kill_n29 (seglast_kill_n110 shrunk by lay/wclimb.py OBJ=M) kills SEG-LAST: run [2, 4] = one REL segment,
# t = 2: the only switch is vertex 1, 9 -> 23, and 1 switches again at 3 (jointly with 25: SEG-COUNT tight). Reproduced from n5b alone
# (run boundaries from n5b's own (lambda_Xi, tau) key, the cutting into REL segments, the switch history, observed GEN_W).
echo "976fc4e88a514b1615ef81caa8b4af17a42b1c5f  lay/instances/seglast_kill_n29.pg" | sha1sum -c --quiet
echo "9afeb2aaf26dd63460216185b6a405a02b07474f  lay/instances/seglast_kill_n29.start" | sha1sum -c --quiet
python3 -I lwp/seglast.py --one lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start | grep -q "EXAMPLE ('lay/instances/seglast_kill_n29.pg', 2, 4, \[2\], 2, 2, 29)"
o=$(python3 -I lay/relcheck.py lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start 2 4 2)
grep -q "run containing t (n5b: (lambda_Xi, tau) constant, no fallback): (2, 4) | its REL segments: \[(2, 4)\] | \[a, b\] is one of them: True" <<<"$o"
grep -q "switchers at t = 2: \[(1, 9, 23, 'switches again at', \[3\])\]" <<<"$o"; grep -q "SEG-LAST fails at t: True" <<<"$o"; grep -q "S1 rank order): 0" <<<"$o"
o=$(python3 -I lay/relcheck.py lay/instances/seglast_kill_n110.pg lay/instances/seglast_kill_n110.start 2 8 2); grep -q "its REL segments: \[(2, 8)\] | \[a, b\] is one of them: True" <<<"$o"
python3 -I root/n5bcmp.py lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start | grep -q "n5b iterations 9 fallbacks 0 states 10 | n5x states 10 | identical state sequences: True"
echo "lay (box 27: seglast_kill_n29 kills SEG-LAST, run and segment recomputed from n5b alone): PASS"
# box 27: lay/instances/psidrop_kill_n70 kills PSI-DROP (PSI1 = 24 at t = 2 and 3 in segment [2, 5]); SEG-LAST holds there; n5b identical.
echo "9cd26eeded045052b769175e3c18dbb72936d404  lay/instances/psidrop_kill_n70.pg" | sha1sum -c --quiet
echo "6ba80572a67873884d21a7cfd26140f7950c2d59  lay/instances/psidrop_kill_n70.start" | sha1sum -c --quiet
o=$(python3 -I lay/psi.py --one lay/instances/psidrop_kill_n70.pg lay/instances/psidrop_kill_n70.start); grep -q "PSI0_V=2 PSI1_V=1 steps=3" <<<"$o"
grep -q "EXAMPLE ('lay/instances/psidrop_kill_n70.pg', 2, 5, 2, 24, 24)" <<<"$o"
python3 -I lwp/seglast.py --one lay/instances/psidrop_kill_n70.pg lay/instances/psidrop_kill_n70.start | grep -q "SEGLAST PASS"
python3 -I root/n5bcmp.py lay/instances/psidrop_kill_n70.pg lay/instances/psidrop_kill_n70.start | grep -q "n5b iterations 9 fallbacks 1 states 10 | n5x states 10 | identical state sequences: True"
python3 -I lay/psi.py --one lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start | grep -q "^PSI0_V=1 steps=2$"
echo "lay (box 27: psidrop_kill_n70 kills PSI-DROP, n5b identical; seglast_kill_n29: PSI0 fails at the deadlock, PSI1 drops): PASS"
# box 28 (docs/si/N5-CHG-box28.md): SEG-COUNT charging. Corollary BND (L(v) <= max(fW(jW v) - 1, fH(jH v))) and SUFFIX-COUNT hold on the
# box-27 kill pins and the ladder; MUT=1 (bound lowered by one) bites. General (a) (EARLY) fails on wgrow_kill_n90 (H-sink 34 at t = 0).
for i in seglast_kill_n29 seglast_kill_n110 psidrop_kill_n70; do
  o=$(python3 -I chg/suffix.py --one lay/instances/$i.pg lay/instances/$i.start); for k in BND SUFFIX JOINTX INTEREARLY; do grep -q "^$k PASS" <<<"$o"; done
done
L=../red/ul/instances/ladderd0_k12_n48
o=$(python3 -I chg/suffix.py --one $L.pg $L.start); for k in BND SUFFIX EARLY JOINTX INTEREARLY; do grep -q "^$k PASS" <<<"$o"; done; grep -q "hsink_inter=11 " <<<"$o"
if ! MUT=1 python3 -I chg/suffix.py --one $L.pg $L.start | grep -q "^BND FAIL"; then echo "box 28 BND MUT did not bite"; exit 1; fi
if ! MUT=1 python3 -I chg/suffix.py --one lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start | grep -q "^BND FAIL"; then echo "box 28 BND MUT n29"; exit 1; fi
o=$(python3 -I chg/suffix.py --one lay/instances/wgrow_kill_n90.pg lay/instances/wgrow_kill_n90.start); grep -q "^EARLY FAIL" <<<"$o"
grep -q "EXAMPLE ('EARLY', 'lay/instances/wgrow_kill_n90.pg', 0, 3, 0, 34, 0, 2)" <<<"$o"
echo "si (box 28: BND and SUFFIX-COUNT on kill pins and ladder, MUT bites; general (a) dead on wgrow_kill_n90): PASS"
# box 28: chg/instances/interjoint_kill_n70 kills INTER-JOINT: H-sink 10 (intermediate switches at 1, 2, 3) finalizes at 5 < s_h = 6;
# n5b state sequence identical; chg/ijcheck.py recomputes run, REL segment, sink status and L(h) from n5b alone.
echo "79a7c76af6e44bce47a6bd2c8e52b47ddf926d23  chg/instances/interjoint_kill_n70.pg" | sha1sum -c --quiet
echo "9b313151306069cb9c1f470bf0846730ae111331  chg/instances/interjoint_kill_n70.start" | sha1sum -c --quiet
o=$(python3 -I chg/suffix.py --one chg/instances/interjoint_kill_n70.pg chg/instances/interjoint_kill_n70.start); grep -q "^INTEREARLY FAIL" <<<"$o"
grep -q "EXAMPLE ('INTEREARLY', 'chg/instances/interjoint_kill_n70.pg', 1, 7, 1, 10, 5, 6)" <<<"$o"; grep -q "^SUFFIX PASS" <<<"$o"
o=$(python3 -I chg/ijcheck.py chg/instances/interjoint_kill_n70.pg chg/instances/interjoint_kill_n70.start 1 7 1 10)
grep -q "its REL segments: \[(1, 7)\] | \[a, b\] is one of them: True" <<<"$o"; grep -q "REL-admissible on \[a, b\]: True | REL at a - 1: False" <<<"$o"
grep -q "sigma_k(h) for k in \[a, b\]: \[32, 21, 36, 24, 24, 28, 28\] | y_h = 28" <<<"$o"; grep -q "jW(h) = 0 first W-settled state of jW(h): 7" <<<"$o"
grep -q "h H-unsettled at t: True | jH(h) H-settled at t (h an H-sink): True | jW(h) W-unsettled at t (h not a W-sink): True" <<<"$o"
grep -q "intermediate switch at t: True | L(h) = 5 | s_h = fW(jW h) - 1 = 6" <<<"$o"; grep -q "S1 rank order): 0" <<<"$o"
python3 -I root/n5bcmp.py chg/instances/interjoint_kill_n70.pg chg/instances/interjoint_kill_n70.start | grep -q "n5b iterations 10 fallbacks 1 states 11 | n5x states 11 | identical state sequences: True"
echo "si (box 28: interjoint_kill_n70 kills INTER-JOINT, reproduced from n5b alone): PASS"
# box 28: chg/instances/growpers_kill_n73 kills GROW-PERSIST (segment [2, 5], pattern G F G); n5b identical. CONJECTURE DL-RUN (deadlock
# steps only at run starts; DEAD later on L-RED R105, block below), DL-FIRST, DL-JOINT (NOEARLY), DL-SOMEH, ZIG on the 48 box-27 climb instances.
echo "ff73bab1641c7f5b8f0756b25df2b24709d1bcdb  chg/instances/growpers_kill_n73.pg" | sha1sum -c --quiet
echo "b496c9b9dffb33880c4fe632ad47d606ef8ffd84  chg/instances/growpers_kill_n73.start" | sha1sum -c --quiet
o=$(python3 -I chg/dlock.py --one chg/instances/growpers_kill_n73.pg chg/instances/growpers_kill_n73.start); grep -q "^GROWPERS FAIL" <<<"$o"
grep -q "EXAMPLE ('GROWPERS', 'chg/instances/growpers_kill_n73.pg', 2, 5, 'GFG')" <<<"$o"
python3 -I root/n5bcmp.py chg/instances/growpers_kill_n73.pg chg/instances/growpers_kill_n73.start | grep -q "n5b iterations 9 fallbacks 1 states 10 | n5x states 10 | identical state sequences: True"
o=$(START=1 python3 -I chg/dlock.py --list chg/climbcorpus_box27.lst); grep -q "deadlock=13 " <<<"$o"
for k in DLRUN DLFIRST NOEARLY DLSOMEH ZIG DLSEP GROWFIN MATCH; do grep -q "^$k PASS" <<<"$o"; done; grep -q "^DLHS FAIL" <<<"$o"; grep -q "^DLNEXT FAIL" <<<"$o"
if ! MUT=1 python3 -I chg/dlock.py --one lay/instances/seglast_kill_n29.pg lay/instances/seglast_kill_n29.start | grep -q "^DLRUN FAIL"; then echo "box 28 DLRUN MUT"; exit 1; fi
echo "si (box 28: growpers_kill_n73 kills GROW-PERSIST; DL-RUN, DL-FIRST, DL-JOINT hold on 13 climb deadlocks, MUT bites): PASS"
# box 28: L-RED's R105 instances (byte-identical copies of claude/l-red 22d7c6ab experiments/red/seg/instances) kill DL-RUN, DL-FIRST and
# NEWFINAL (deadlocks at t = 0 and t = 2 of the run [0, 4]); DL-SEP, DL-NOCONSEC, FROZEN-COUNT, DL-JOINT, BND hold; n5b identical.
echo "2783f64d82f271ebc9a26b470b26a9938fd5295c  chg/instances/red/segcount_kill_n20.pg" | sha1sum -c --quiet
echo "97ba6b298917676e10cb209e21f49ee442b73686  chg/instances/red/segcount_kill_n20.start" | sha1sum -c --quiet
echo "0d242a9b99f81b1f5dc91e32da1211d12c426982  chg/instances/red/segfam_k3_n29.pg" | sha1sum -c --quiet
echo "c0f9d1af61d74af696e6b378f33279968b448bd3  chg/instances/red/segfam_k3_n29.start" | sha1sum -c --quiet
o=$(VERB=1 python3 -I chg/dlock.py --one chg/instances/red/segcount_kill_n20.pg chg/instances/red/segcount_kill_n20.start)
for k in DLRUN DLFIRST NEWFINAL MATCH; do grep -q "^$k FAIL" <<<"$o"; done; for k in DLSEP DLCONSEC FRZLEN NOEARLY DLSOMEH ZIG NEWEDGE GROWFIN; do grep -q "^$k PASS" <<<"$o"; done
grep -q "\[0,4\] t=0 switch=\[(6, 0, 11)\]" <<<"$o"; grep -q "\[0,4\] t=2 switch=\[(6, 11, 18)\]" <<<"$o"
o=$(python3 -I chg/dlock.py --one chg/instances/red/segfam_k3_n29.pg chg/instances/red/segfam_k3_n29.start); grep -q "deadlock=3 finalsteps=3 growsteps=3" <<<"$o"
for k in DLSEP DLCONSEC FRZLEN NOEARLY; do grep -q "^$k PASS" <<<"$o"; done; grep -q "^DLRUN FAIL" <<<"$o"
o=$(python3 -I chg/suffix.py --one chg/instances/red/segfam_k3_n29.pg chg/instances/red/segfam_k3_n29.start); grep -q "^BND PASS" <<<"$o"
python3 -I root/n5bcmp.py chg/instances/red/segcount_kill_n20.pg chg/instances/red/segcount_kill_n20.start | grep -q "n5b iterations 6 fallbacks 0 states 7 | n5x states 7 | identical state sequences: True"
echo "si (box 28: L-RED's segcount_kill_n20 / segfam_k3_n29 kill DL-RUN, DL-FIRST, NEWFINAL; DL-SEP, DL-NOCONSEC, FROZEN-COUNT, BND hold): PASS"
# box 28: chg/instances/dlsep_kill_n70 kills DL-SEP, DL-NOCONSEC, FROZEN-COUNT, DL-SOMEH, ZIG: REL segment [0, 12], deadlocks 1-3, 5-9,
# frozen run [0, 10) with 9 switchers; every deadlock reproduced from n5b alone (lay/relcheck.py); n5b state sequence identical.
echo "e500ea47e1dc0163b32a97042ff9752daf6db83a  chg/instances/dlsep_kill_n70.pg" | sha1sum -c --quiet
echo "f5569821f5d951de4922a4a9853b3bb4c9bf0284  chg/instances/dlsep_kill_n70.start" | sha1sum -c --quiet
o=$(python3 -I chg/dlock.py --one chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start)
for k in DLSEP DLCONSEC FRZLEN DLSOMEH ZIG; do grep -q "^$k FAIL" <<<"$o"; done; for k in NOEARLY GROWFIN NEWEDGE; do grep -q "^$k PASS" <<<"$o"; done
grep -q "deadlock=8 finalsteps=5 growsteps=3" <<<"$o"
for t in 1 2 3 5 6 7 8 9; do
  o=$(python3 -I lay/relcheck.py chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start 0 12 $t)
  grep -q "its REL segments: \[(0, 12)" <<<"$o"; grep -q "REL-admissible on \[a, b\]: True" <<<"$o"; grep -q "SEG-LAST fails at t: True" <<<"$o"; grep -q "S1 rank order): 0" <<<"$o"
done
python3 -I root/n5bcmp.py chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start | grep -q "n5b iterations 16 fallbacks 0 states 17 | n5x states 17 | identical state sequences: True"
o=$(python3 -I chg/lenstat.py --one chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start); grep -q "^LEN2 PASS" <<<"$o"; grep -q "^LENE PASS" <<<"$o"; grep -q "^FRZLEN FAIL" <<<"$o"
grep -q "EXAMPLE ('FRZLEN', 'chg/instances/dlsep_kill_n70.pg', 0, 12, 0, 10, 9)" <<<"$o"
echo "si (box 28: dlsep_kill_n70 kills DL-SEP, DL-NOCONSEC, FROZEN-COUNT; 8 deadlocks in one REL segment, reproduced from n5b alone): PASS"
# box 28: L-RED's R106 runquad_K8_m30_n192 (copy) kills LENE and LEN2 (one REL segment [0, 263], |E_b| = 49, SW = 47); BND, FROZEN-COUNT
# hold. Lemma SW-RISE: every switch off the switcher's own cycle strictly raises its Xi (chg/pervert.py SWRISE PASS; reactors switch 15 times).
echo "ebaa6ac57ec60948fb986210c27479cb3a7961d9  chg/instances/red/runquad_K8_m30_n192.pg" | sha1sum -c --quiet
echo "4ba9f8605a1b18891dffb40d508bce929cf7c952  chg/instances/red/runquad_K8_m30_n192.start" | sha1sum -c --quiet
o=$(python3 -I chg/lenstat.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
grep -q "^LENE FAIL" <<<"$o"; grep -q "^LEN2 FAIL" <<<"$o"; grep -q "^FRZLEN PASS" <<<"$o"
grep -q "TOP (5.367, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 49, 47, 45, 218, 45, 481, 15, 192)" <<<"$o"
python3 -I chg/suffix.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start | grep -q "^BND PASS"
o=$(python3 -I chg/pervert.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
grep -q "^SWRISE PASS" <<<"$o"; grep -q "^PERV PASS" <<<"$o"; grep -q "TOP (0.078, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 263, 15, 15, 16, 192)" <<<"$o"
echo "si (box 28: runquad_K8_m30_n192 kills LENE and LEN2; BND, SW-RISE hold; max 15 switches per vertex at n 192): PASS"
# box 28 §9: Theorem COMPOSE (phase length <= sum (1 + RISE(c)) <= sum n (PCH(c) + 1)) and Corollary COMPOSE-RUN (whole run, Odd side on G^d)
# measured with every inequality's slack on runquad, dlsep_kill_n70, segcount_kill_n20 and seglast_kill_n110; LEN-MONO (LDIR, LBLK) holds.
o=$(python3 -I chg/compose.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
for k in I0 I1 LDIR LBLK I2 I3; do grep -q "^$k PASS" <<<"$o"; done
grep -q "TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 481, 1016, 195072, 265890048, 8, 15, 15, 15, 192)" <<<"$o"
o=$(python3 -I chg/compose.py --one chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start); for k in I0 I1 LDIR LBLK I2 I3; do grep -q "^$k PASS" <<<"$o"; done
grep -q "TOP (12, 'chg/instances/dlsep_kill_n70.pg', 0, 12, 39, 387, 26810, 14059640, 5, 6, 7, 4, 70)" <<<"$o"
for f in chg/instances/red/segcount_kill_n20 lay/instances/seglast_kill_n110; do
  o=$(MODE=run python3 -I chg/compose.py --one $f.pg $f.start); for k in RUNI0 R47 EI1 OI1 ELDIR OLDIR ELBLK OLBLK; do grep -q "^$k PASS" <<<"$o"; done
done
grep -q "TOP (16, 'lay/instances/seglast_kill_n110.pg', 0, 16, 27, 152, 16066, 0, 20, 1, 4, 2, 110)" <<<"$o"
echo "si (box 28 §9: COMPOSE and COMPOSE-RUN inequalities hold with their slack on runquad, dlsep_kill_n70, R105 and n110 pins): PASS"
# box 28: packet docs/si/P-N5-COMPOSE-box28.md (FROZEN): its 16 verbatim quotes, and the shifted-line control that must fail.
python3 -I rund/quotecheck.py ../../docs/si/P-N5-COMPOSE-box28.md | grep -q "quotes=16 bad=0"
python3 -I rund/quotecheck.py ../../docs/si/P-N5-COMPOSE-box28.md --mut | grep -q "QUOTES FAIL"
echo "si (box 28: P-N5-COMPOSE quotes verbatim, shifted control fails): PASS"
# box 28 §12: Lemma INHERIT (a vertex's carry is the carry of the switch where its honest play diverges): 0 failures on runquad and dlsep.
o=$(python3 -I chg/carrysrc.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
grep -q "^carries=856 nm_max=8 phases=1 src_even=856 srcs_max_per_phase=256$" <<<"$o"; grep -q "^INH PASS" <<<"$o"
o=$(python3 -I chg/carrysrc.py --one chg/instances/dlsep_kill_n70.pg chg/instances/dlsep_kill_n70.start); grep -q "src_odd=26" <<<"$o"; grep -q "^INH PASS" <<<"$o"
echo "si (box 28 §12: INHERIT holds on runquad (856 carries) and dlsep_kill_n70): PASS"
# box 28 §13: carries with no gate reopening and no open Odd gate on the vertex's plays (L-LIT T37 §3's CONJECTURE, multiplicative form):
# all 121 carrying (vertex, λ-run) pairs of runquad_K8_m30_n192 and all 67 of L-RED's s3quad_K3_m4 (copy, S3 default start).
echo "675778af8ea65724a053fe1e4cbbf8b8fe33f8ad  chg/instances/red/s3quad_K3_m4.pg" | sha1sum -c --quiet
python3 -I chg/reopen.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start | grep -q "^carrying_vertex_runs=121 nm_zero_max=8 ratio_max_x100=800 zero_reopen=121$"
python3 -I chg/reopen.py --one chg/instances/red/s3quad_K3_m4.pg | grep -q "^carrying_vertex_runs=67 nm_zero_max=3 ratio_max_x100=300 zero_reopen=67$"
echo "si (box 28 §13: carries without reopenings on runquad (121/121) and s3quad_K3_m4 (67/67)): PASS"
# box 28 §14: R17's Lemma P breaks in two frames on runquad (σ̄ constant on the phase): W-better edges outside the arena (3,102 pairs, first
# t = 0, x = 5, z = 4) and honest switches beaten in Ξ by S4a's τ-optimum (2,096, first t = 0, x = 3, z = 27); |D| = 32.
o=$(python3 -I chg/r17.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
grep -q "TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 481, 263, 0, 3102, (0, 5, 4, 6, 6), 192, 32, 2096, (0, 3, 27, 0, 9))" <<<"$o"
grep -q "^ESWSB FAIL" <<<"$o"; grep -q "^D0 PASS" <<<"$o"
echo "si (box 28 §14: R17's Lemma P fails in both frames on runquad with σ̄ constant): PASS"
# box 29 (docs/si/N5-FRZ-box29.md): W-SPLIT bookkeeping and CN-W on runquad (all 263 transitions change lambda_W, W has 0 P-changes);
# FW-BF/FW-LEN hold on s_elim24_final's frozen W-phases; the W-phase form dies on x135_n59; SETTLE dies on s_elim24_final, SETTLE_X on the ladder.
echo "ddb99d6c103e4d60b1b1d4a6b8c3b5ab9070b21b  frz/instances/s_elim24_final.pg" | sha1sum -c --quiet
o=$(python3 -I frz/phstat.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start)
grep -q "TOP (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 0, 263, 0, 0, 0, 192)" <<<"$o"; grep -q "^WSPLIT PASS" <<<"$o"; grep -q "^CNW PASS" <<<"$o"
python3 -I frz/frozen.py --one chg/instances/red/runquad_K8_m30_n192.pg chg/instances/red/runquad_K8_m30_n192.start | grep -q "EXT (263, 'chg/instances/red/runquad_K8_m30_n192.pg', 0, 263, 32, 0, 0, 0, 15, 1419, 192)"
o=$(python3 -I frz/fwphase.py --one frz/instances/s_elim24_final.pg frz/instances/s_elim24_final.start)
grep -q "^fwphases=5 phases=1 sbch=0$" <<<"$o"; grep -q "^FWBF PASS" <<<"$o"; grep -q "^FWLEN PASS" <<<"$o"
o=$(python3 -I frz/wphase.py --one runlin/instances/x135_n59.pg runlin/instances/x135_n59.start)
grep -q "TOP (135, 'runlin/instances/x135_n59.pg', 1, 136, 135, 5, 7, 1, 1, 11, 59, 218)" <<<"$o"
o=$(python3 -I frz/settle.py --one frz/instances/s_elim24_final.pg frz/instances/s_elim24_final.start); grep -q "^SETTLE FAIL" <<<"$o"; grep -q "^SETTLE_X PASS" <<<"$o"
o=$(python3 -I frz/settle.py --one ../red/ul/instances/ladderd0_k12_n48.pg ../red/ul/instances/ladderd0_k12_n48.start); grep -q "^SETTLE_X FAIL" <<<"$o"; grep -q "^SETTLE PASS" <<<"$o"
echo "si (box 29: W-SPLIT/CN-W on runquad, FW-BF on s_elim24_final, W-phase form dead on x135_n59, SETTLE/SETTLE_X kills): PASS"
# box 29 §7: Lemma EPOCH-U holds (R17 on the untrapped part) and TRAP-MONO dies on fbrestart_cex_n12 (play form) and lend107_n32 (value form).
echo "35223b6c46750b2c1c961d68485025a9a5e69d87  frz/instances/fbrestart_cex_n12.pg" | sha1sum -c --quiet
o=$(python3 -I frz/epoch.py --one frz/instances/fbrestart_cex_n12.pg frz/instances/fbrestart_cex_n12.start)
grep -q "^TMONO_P_V=1 fw=2$" <<<"$o"; grep -q "^R17U PASS" <<<"$o"; grep -q "^TMONO_V PASS" <<<"$o"
o=$(python3 -I frz/epoch.py --one ../n5-epoch/instances/lend107_n32.pg ../n5-epoch/instances/lend107_n32.start)
grep -q "^TMONO_P_V=3 TMONO_V_V=3 fw=10$" <<<"$o"; grep -q "^R17U PASS" <<<"$o"
echo "si (box 29 §7: EPOCH-U holds; TRAP-MONO dead on fbrestart_cex_n12 and lend107_n32): PASS"
# box 28 fixes: P-N5-COMPOSE stays frozen (sha1) while P-N5-COMPOSE-fixes-box28.md appends F1-F10.
echo "e1b977aa9cf1583d5e0c442a8f87d024230b6524  ../../docs/si/P-N5-COMPOSE-box28.md" | sha1sum -c --quiet
grep -q "^## F1 (COMP-E1" ../../docs/si/P-N5-COMPOSE-fixes-box28.md
echo "si (box 28 fixes: P-N5-COMPOSE unchanged, fixes file present): PASS"
# box 28 fixes, successor 26: quote pins of P-N5-COMPOSE-fixes-box28.md (19 quotes, 0 bad); a mutated quote must fail.
o=$(cd ../.. && python3 -I docs/si/P-N5-COMPOSE-fixes-quotecheck.py)
grep -q "^quotes=19 bad=0$" <<<"$o"
qm=$(mktemp); sed 's/the number of TRANSITIONS t → t + 1/the number of STATES t → t + 1/' ../../docs/si/P-N5-COMPOSE-fixes-box28.md > "$qm"
o=$(cd ../.. && python3 -I docs/si/P-N5-COMPOSE-fixes-quotecheck.py "$qm"); rm -f "$qm"
grep -q "^quotes=19 bad=[1-9]" <<<"$o"
echo "si (box 28 fixes: 19 quote pins exact; mutated quote caught): PASS"
# box 30 (docs/si/N5-TORD-box30.md): |D| = 1 prefix frame. PMON / H-P / TORD / TRAP-FIX / FW-D1 hold on oneodd_c16 (5 W> frozen W-phases,
# one epoch each); the HLP control (H constant from step 1 instead of s) must fail there; kw25_n32 (X>, one epoch, 25 W-changes ≤ 3 + 28²);
# the abstract two-order climb's best EE instance reproduces 8 W-changing steps = n_abs (tord/logs/out_c8_ee.txt).
echo "827976e24f9634029595d0f8d957ff8d4bc9308b  ../new/box21/instances/oneodd_c16.pg" | sha1sum -c --quiet
o=$(python3 -I tord/epoch2.py --one ../new/box21/instances/oneodd_c16.pg)
grep -q "^checked_TD_epochs=5 ep_TD=5 ep_W>=5 fw1=5 fw1_diff=5$" <<<"$o"
for k in PMON1 PMON2 HLP LMON CNT TRAPFIX FWD1; do grep -q "^$k PASS$" <<<"$o"; done
o=$(MUT=hlp0 python3 -I tord/epoch2.py --one ../new/box21/instances/oneodd_c16.pg); grep -q "^HLP FAIL$" <<<"$o"
echo "607f1cc05b2230b3c2f43d451a6c0518094d953b  ../red/xing/instances/kw25_n32.pg" | sha1sum -c --quiet
o=$(python3 -I tord/epoch2.py --one ../red/xing/instances/kw25_n32.pg)
grep -q "'diff_wch': (0.8064516129032258, 25, '../red/xing/instances/kw25_n32.pg', 0, 25, 28, 32)" <<<"$o"; grep -q "^TRAPFIX PASS$" <<<"$o"; grep -q "^FWD1 PASS$" <<<"$o"
o=$(python3 -I tord/show.py "$(grep best tord/logs/out_c8_ee.txt | tail -1 | cut -d' ' -f6-)" | tail -1); test "$o" = "8 8 STOP"
echo "si (box 30: PMON, H-P, TORD, TRAP-FIX, FW-D1 on oneodd_c16 and kw25_n32; HLP control fails; abstract EE best = n_abs): PASS"
# box 30 §11: gate classes (any D): general TRAP-FIX, FW-DG and FW-D hold on lend107_n32 (|D| = 3) and oneodd_c16 (G1 G2 G3).
o=$(python3 -I tord/gates.py --one ../n5-epoch/instances/lend107_n32.pg ../n5-epoch/instances/lend107_n32.start)
grep -q "^D3_G3=10 fw=10$" <<<"$o"; for k in GTF GB FWDG FWD; do grep -q "^$k PASS$" <<<"$o"; done
o=$(python3 -I tord/gates.py --one ../new/box21/instances/oneodd_c16.pg); grep -q "'G1G2G3')" <<<"$o"; grep -q "^FWDG PASS$" <<<"$o"
echo "si (box 30 §11: gate classes, FW-DG on lend107_n32 and oneodd_c16): PASS"
# box 31 (docs/si/N5-SPC-box31.md): same-pair core. §2 DEAD: runfam_K100 (pinned start) frozen W-phase [52, 167] lags R17's W-frame
# Lemma P by 113 steps with TC = 2 (gap-step form dead; Ξ / mixed / admitted forms 109 / 108 / 108). §3-§4: Lemma GP+ and Corollary FW-R
# hold on ccl_w48_n48 (R = 12); the plain W-frame Lemma P (MUT=all) must fail there.
echo "86cf1884919b223c18f982eed6a00a4256a501dd  runlin/instances/runfam_K100.pg" | sha1sum -c --quiet
echo "843b9f4e83a21d8ee5bd56df97f7b43f59edc394  runlin/instances/runfam_K100.start" | sha1sum -c --quiet
o=$(python3 -I core/sp.py --one runlin/instances/runfam_K100.pg runlin/instances/runfam_K100.start)
grep -q "^MAX D1:def (113, 'runlin/instances/runfam_K100.pg', 52, 167, 139, 1, 115, 2, 115, 113, 133, False, 109, 108, 108, 127)$" <<<"$o"
grep -q "^CTRL PASS$" <<<"$o"
echo "a7056dea01cd9c6398e054ef6edaaa40f60dabb1  xing/instances/ccl_w48_n48.pg" | sha1sum -c --quiet
o=$(PLUS=1 python3 -I core/gp.py --one xing/instances/ccl_w48_n48.pg)
grep -q "'D1': (12, 3, 3, 48, 1, 'xing/instances/ccl_w48_n48.pg', 15, 18)" <<<"$o"; for k in GP RED RLIN; do grep -q "^$k PASS$" <<<"$o"; done
o=$(MUT=all PLUS=1 python3 -I core/gp.py --one xing/instances/ccl_w48_n48.pg); grep -q "^GP FAIL$" <<<"$o"
echo "si (box 31: gap-step Lemma P dead on runfam_K100; GP+, FW-R on ccl_w48_n48; plain W-frame Lemma P control fails): PASS"
# box 31 §5: R-LIN dead on rlin_cex_n40 (R = 129 > 39 in 10 transitions); FW-R and FW-R′ (R_T = 9) hold there; n5b identical.
echo "670ba1ffc22c8f9b170e11ca3e43c33cee9329ca  core/instances/rlin_cex_n40.pg" | sha1sum -c --quiet
echo "e488c00fe1359818b9a665a415cc7b2962015318  core/instances/rlin_cex_n40.start" | sha1sum -c --quiet
o=$(PLUS=1 python3 -I core/gp.py --one core/instances/rlin_cex_n40.pg core/instances/rlin_cex_n40.start)
grep -q "'D1:R_T/(n-1)': (0.23076923076923078, 9, 10, 40, 1, 'core/instances/rlin_cex_n40.pg', 1, 11)" <<<"$o"
grep -q "'D1': (129, 10, 10, 40, 1, 'core/instances/rlin_cex_n40.pg', 1, 11)" <<<"$o"
grep -q "^RLIN FAIL$" <<<"$o"; grep -q "^RED PASS$" <<<"$o"; grep -q "^GP PASS$" <<<"$o"
o=$(python3 -I root/n5bcmp.py core/instances/rlin_cex_n40.pg core/instances/rlin_cex_n40.start | head -1); grep -q "identical state sequences: True" <<<"$o"
echo "si (box 31 §5: R-LIN dead on rlin_cex_n40; FW-R, FW-R′ hold; n5b identical): PASS"
# box 31 §6: GP* / FW-R* (only blocked edges excluded): rlin_cex_n40 has R* = 0 (FW-BF proved there by FW-R*), ccl_w48_n48 R*_T = 1;
# the plain W-frame Lemma P (MUT=all) still fails on ccl_w48_n48.
o=$(STAR=1 python3 -I core/gp.py --one core/instances/rlin_cex_n40.pg core/instances/rlin_cex_n40.start)
grep -q "'D1': (0, 10, 10, 40, 1, 'core/instances/rlin_cex_n40.pg', 1, 11)" <<<"$o"; for k in GP RED RLIN; do grep -q "^$k PASS$" <<<"$o"; done
o=$(STAR=1 python3 -I core/gp.py --one xing/instances/ccl_w48_n48.pg)
grep -q "'D1:R_T/(n-1)': (0.02127659574468085, 1, 3, 48, 1, 'xing/instances/ccl_w48_n48.pg', 15, 18)" <<<"$o"; grep -q "^GP PASS$" <<<"$o"
o=$(MUT=all STAR=1 python3 -I core/gp.py --one xing/instances/ccl_w48_n48.pg); grep -q "^GP FAIL$" <<<"$o"
echo "si (box 31 §6: GP*, FW-R* on rlin_cex_n40 and ccl_w48_n48; MUT=all control fails): PASS"
# box 31 packet docs/si/P-N5-GP-box31.md (frozen): its 14 verbatim quotes hold at their pinned commit; shifting every line range by one fails.
o=$(python3 -I rund/quotecheck.py ../../docs/si/P-N5-GP-box31.md); grep -q "^quotes=14 bad=0$" <<<"$o"; grep -q "^QUOTES PASS$" <<<"$o"
o=$(python3 -I rund/quotecheck.py ../../docs/si/P-N5-GP-box31.md --mut); grep -q "^QUOTES FAIL$" <<<"$o"
echo "si (box 31 packet P-N5-GP: 14 quotes exact; shifted control fails): PASS"
# box 32 (docs/si/N5-RTC-box32.md): R*-TC by injection. Same-pair core: lend47_n32 (pinned start) has a non-basin-changing late*
# transition (s = 8) charged to the basin change at 7; matching exists, Lemma LATE-BASIN holds; MUT=lastonly (per-transition form) fails.
# General R*-TC DEAD: kt6_n58 (S3 start, written out as core/instances/kt6_n58_S3.start), D = {18}, c1 ≠ c2: R*_T = 5 > TC = 0.
o=$(python3 -I core/inj.py --one ../n5-epoch/instances/lend47_n32.pg ../n5-epoch/instances/lend47_n32.start)
grep -q "^SP_RT=3 SP_TC=15 SP_late_noBC=1 SP_phases=2$" <<<"$o"; if grep -q "MATCH_FAIL\|LEMMA_VIOL" <<<"$o"; then exit 1; fi
o=$(MUT=lastonly python3 -I core/inj.py --one ../n5-epoch/instances/lend47_n32.pg ../n5-epoch/instances/lend47_n32.start); grep -q "SP_MATCH_FAIL=1" <<<"$o"
o=$(python3 -I core/inj.py --one ../red/fbx/instances/kt6_n58.pg core/instances/kt6_n58_S3.start)
grep -q "^NSP_MATCH_FAIL=1 NSP_RT=5 NSP_RT>TC=1 NSP_TC=0 NSP_late_noBC=5 NSP_noBC_empty=5 NSP_phases=1$" <<<"$o"; if grep -q "LEMMA_VIOL" <<<"$o"; then exit 1; fi
echo "si (box 32: LATE-BASIN + matching on lend47_n32, lastonly control fails; general R*-TC dead on kt6_n58): PASS"
# box 32 §5: rounds of one vertex (|D| = 1, c1 = c2): on x31_re24 every one of the 33 rounds is a strict prefix climb (class A) and prefixes
# never decrease (34 strict increases); MUT=rev (flag increases as decreases) must fire.
o=$(python3 -I core/rounds.py --one ../red/xing/instances/x31_re24.pg); for k in " PREINC=34 " " round_A=33 " " rounds=33"; do grep -q "$k" <<<"$o"; done; if grep -q "PREDEC" <<<"$o"; then exit 1; fi
o=$(MUT=rev python3 -I core/rounds.py --one ../red/xing/instances/x31_re24.pg); grep -q "PREDEC_round=33 PREDEC_stay=1" <<<"$o"
echo "si (box 32 §5: rounds all class A, prefixes monotone on x31_re24; MUT=rev control fires): PASS"
# box 32 §6: Lemma ROUND-G holds on x31_re24 (all 33 rounds have equal tail masks, no ROUNDG_V); distinct climb tops fail on rtt16 (TOPREP 7).
o=$(python3 -I core/rounds.py --one ../red/xing/instances/x31_re24.pg); grep -q " round_tails_equal=33 " <<<"$o"; if grep -q "ROUNDG_V" <<<"$o"; then exit 1; fi
o=$(python3 -I core/rounds.py --one ../new/box25/instances/rtt16.pg); grep -q "^HC_toprep=0 PREINC=24 TOPREP=7 " <<<"$o"
echo "si (box 32 §6: ROUND-G on x31_re24; distinct climb tops dead on rtt16): PASS"
# box 33 (docs/si/N5-ODD-box33.md): Odd re-entries on plain N5 against R86's Odd side. d_hntop_n3 (L-RED's dualised hntop, own
# regenerated copy): 251 re-entries, 0 protected (ODD-FREEZE), every window has a U(e)-change (SW-RETURN), NM^U max 28 = 2N²+5N−5;
# MUT flips H3 (protected re-entries must appear). d_runquad_K2_m30: 61 re-entries with no carry of U(e) in the window (charge_MAT).
# d_runquad_K3_m30: ENT ≤ 1 + NM^U(e) DEAD. lev74_n40 (S3): ENT ≤ 1 + PCH^U(e) DEAD; Lemma LEN-REENTRY holds; MUT control fires.
o=$(python3 -I odd/reent.py odd/inst/d_hntop_n3.pg odd/inst/d_hntop_n3.start)
for k in " reentries 251 " " max_per_o 22 " " NMU_max 28 " " charge_CAR 184 " " charge_LAM 67 " " class_X 248 " " class_Z 3 "; do grep -q "$k" <<<"$o"; done
grep -q " PASS$" <<<"$o"; if grep -q "PROT_V\|SWR_V\|LENTIE_V" <<<"$o"; then exit 1; fi
o=$(python3 -I odd/reent.py odd/inst/d_hntop_n3.pg odd/inst/d_hntop_n3.start --mut); grep -q " PROT_V 3 " <<<"$o"
o=$(python3 -I odd/reent.py odd/inst/d_runquad_K2_m30.pg odd/inst/d_runquad_K2_m30.start); grep -q " charge_MAT 61 " <<<"$o"; grep -q " PASS$" <<<"$o"
o=$(python3 -I odd/reent.py odd/inst/d_runquad_K3_m30.pg odd/inst/d_runquad_K3_m30.start); grep -q "'ENTNM': (0, 99, 42, 43, 3, 1)" <<<"$o"
o=$(python3 -I odd/reent.py ../red/fbr/instances/lev74_n40.pg); grep -q "'ENTPCH': (0, 18, 6, 0, 2, 0)" <<<"$o"; grep -q " charge_LEN 1 " <<<"$o"; grep -q " PASS$" <<<"$o"
o=$(python3 -I odd/reent.py ../red/fbr/instances/lev74_n40.pg --mut); grep -q " LENTIE_V 1 " <<<"$o"
echo "si (box 33: ODD-FREEZE / SW-RETURN on Odd re-entries; carry-charge, ENT-NM, ENT-PCH dead; LEN-REENTRY; controls fire): PASS"
# box 34 (docs/si/N5-CARX-box34.md): d_hntop's NM^U = 2N²+5N−5 as N lane sweeps (N = 3: [7, 11, 10]); CARRY-CLIMB dead on d_hntop_n2;
# SWEEP-GAIN dead on wide_h16 (Odd) and fc_3 (Even); CARRY-SEG holds there; --mut flips the gain test and must fire on d_hntop_n3.
o=$(python3 -I odd/carx.py odd/inst/d_hntop_n3.pg odd/inst/d_hntop_n3.start)
grep -q "^SWEEPS d_hntop_n3.pg vertex d3_3(56) NM 28 sweeps \[7, 11, 10\]$" <<<"$o"
o=$(python3 -I odd/carx.py odd/inst/d_hntop_n2.pg odd/inst/d_hntop_n2.start); grep -q "CLIMB_V 61 .* ex (4, 0, 7, 38, 35) FAIL" <<<"$o"
o=$(python3 -I odd/carx.py ../red/n5inj/instances/wide_h16.pg); grep -q "SEG_V 0 .* GAIN_V 3 .* exg (2, 13, 23, 18, 18) FAIL" <<<"$o"
o=$(SIDE=E python3 -I odd/carx.py ../new/box59/out/fc_3.pg); grep -q "SEG_V 0 .* GAIN_V 12 .* exg (6, 0, 23, 155, 88) FAIL" <<<"$o"
o=$(python3 -I odd/carx.py odd/inst/d_hntop_n3.pg odd/inst/d_hntop_n3.start --mut); grep -q "GAIN_V 5 " <<<"$o"
echo "si (box 34: d_hntop sweeps; CARRY-CLIMB, SWEEP-GAIN dead; CARRY-SEG holds on the kills; control fires): PASS"
# box 35 (docs/si/N5-RESET-box35.md): reset potentials Φ_d. fc_3 (Even side) kills d = 2 and 3 at the same resets (t 0, 23); wide_h16
# (Odd side) passes for d = 2; S1's exact weight (PHID=w) never falls across resets (sanity: it rises at every P-change).
o=$(PHID=2 SIDE=E python3 -I odd/carx.py ../new/box59/out/fc_3.pg); grep -q "exg (6, 0, 23, 11587, 5786) FAIL" <<<"$o"
o=$(PHID=3 SIDE=E python3 -I odd/carx.py ../new/box59/out/fc_3.pg); grep -q "exg (6, 0, 23, 872765, 373618) FAIL" <<<"$o"
o=$(PHID=2 python3 -I odd/carx.py ../red/n5inj/instances/wide_h16.pg); grep -q "GAIN_V 0 .* PASS$" <<<"$o"
o=$(PHID=w SIDE=E python3 -I odd/carx.py ../new/box59/out/fc_3.pg); grep -q "GAIN_V 0 .* PASS$" <<<"$o"
echo "si (box 35: Φ_2, Φ_3 dead on fc_3; Φ_2 passes wide_h16; exact weight monotone): PASS"
# box 36 (docs/si/N5-PIVOT-box36.md): Lemma INHERIT-λ (pivot's ΔP = x's ΔP on λ-runs; --mut must fire), PIVOT-DISTINCT /
# PIVOT-DEEP / EDGE-DISTINCT dead on fc_3 (Even) and wide_h16 (Odd); BARRIER-SI: switch-all on switchallexp_7 (one λ-run) has
# 126 matched resets of vertex 101 (> n = 105) and a 375-carry segment, with F-MON, SUCC-MON, LATE-RISE, SW-RETURN all holding.
o=$(SIDE=E python3 -I odd/pivot.py ../new/box59/out/fc_3.pg); grep -q "INH_V 0 " <<<"$o"; grep -q "PD_V 339 DP_V 420 ED_V 168 " <<<"$o"; grep -q "PASS$" <<<"$o"
o=$(SIDE=E python3 -I odd/pivot.py ../new/box59/out/fc_3.pg --mut); if grep -q "INH_V 0 " <<<"$o"; then exit 1; fi
o=$(python3 -I odd/pivot.py ../red/n5inj/instances/wide_h16.pg); grep -q "INH_V 0 .*PD_V 48 DP_V 56 ED_V 2 " <<<"$o"
o=$(python3 -I odd/barrier.py odd/inst/switchallexp_7.pg); grep -q "n 105 iter 1243 lambda_runs 1 FMON_V 0 SUCCMON_V 0 LATERISE_V 0 SWRET_V 0 STILL 0 maxPCH 984 (NM 858 MAT 126 vertex 101 run \[0,1244)) maxSEG 375 PASS" <<<"$o"
o=$(python3 -I odd/barrier.py ../new/box54/out/switchallexp_2.pg --mut); grep -q "FMON_V 255 SUCCMON_V 166 LATERISE_V 179 " <<<"$o"   # control: reversed run
echo "si (box 36: INHERIT-λ exact, mutation bites; pivot laws dead; switch-all kills RESET-LIN and CARRY-SEG with all generic lemmas holding): PASS"
# box 36 §5: the frozen guide alone breaks the counter: FG(τ) (S4a with τ frozen) on switchallexp_7, τ = first / last.
o=$(python3 -I odd/fg.py odd/inst/switchallexp_7.pg first last)
grep -q "tau first iter 142 stalls 24 lambda_runs 1 maxPCH 63 maxMAT 1 vertex 102 DONE" <<<"$o"; grep -q "tau last iter 14 stalls 0 lambda_runs 1 maxPCH 12 maxMAT 1 vertex 102 DONE" <<<"$o"
echo "si (box 36 §5: FG(τ) on switchallexp_7: 142 / 14 iterations, ≤ 1 matched reset per vertex): PASS"
# box 37 (docs/si/N5-WRET-box37.md): switch-target forms on L-RED's R120 pins (observer 248 MATCHED, targets ≤ K = 8, both sides);
# Lemma W-RETURN (0 violations under S4a on fc_3; --mut fires; the switch-all control violates W-MON and W-RETURN).
o=$(SIDE=E python3 -I odd/pivot.py odd/inst/red/wobs_K8_m32.pg odd/inst/red/wobs_K8_m32.start | grep TARGET)
grep -q "n 231 MAT_ALL 248 MAT_T 8 at (104, 0) SEG_ALL 2 SEG_T 1 PCH_ALL 263 PCH_T 15 RESETLINT PASS CARRYSEGT PASS PCHQUADT PASS" <<<"$o"
o=$(python3 -I odd/pivot.py odd/inst/red/d_wobs_K8_m32.pg odd/inst/red/d_wobs_K8_m32.start | grep TARGET)
grep -q "side O n 231 MAT_ALL 248 MAT_T 8 .* RESETLINT PASS" <<<"$o"
o=$(python3 -I odd/wret.py ../new/box59/out/fc_3.pg); grep -q "WMON_V 0 WRET_V 0 REENT 62 WPAID 62 SILENT 0 .* PASS$" <<<"$o"
o=$(python3 -I odd/wret.py ../new/box59/out/fc_3.pg --mut); grep -q "WRET_V 62 " <<<"$o"
o=$(MODE=fg:first python3 -I odd/wret.py ../new/box59/out/fc_3.pg); grep -q "WMON_V 0 WRET_V 0 REENT 218 WPAID 218 SILENT 0 .* PASS$" <<<"$o"
o=$(MODE=sa:first python3 -I odd/wret.py ../new/box54/out/switchallexp_3.pg); grep -q "WMON_V 22 WRET_V 39 REENT 377 .* FAIL$" <<<"$o"
o=$(python3 -I odd/wret.py ../red/so/instances/tog6b_n32.pg); grep -q "WRET_V 0 REENT 4 WPAID 3 SILENT 0 VFORM_V 0 CYC 1 OPT_V 0 .* PASS$" <<<"$o"   # own-cycle-node re-entry excluded
echo "si (box 37: target forms on R120 pins; W-RETURN holds under S4a, mutation and switch-all control fire): PASS"
# box 38 (docs/si/N5-SPAN-box38.md): Lemma SPAN (ENT ≤ n(1 + PCH^span), 0 violations); the in-window form is inflated on R121's
# tobs_K8_m32 (248 MATCHED in one in-window), the out-window and span forms are not (7).
o=$(SIDE=E python3 -I odd/win.py odd/inst/red/tobs_K8_m32.pg odd/inst/red/tobs_K8_m32.start)
grep -q "n 233 pairs 96 maxENT 8 SPAN_V 0 .*OUTRISE_V 0 | IN: MAT 248 PCH 263 SEG 2 at (231, 198, 0) OUT: MAT 7 PCH 14 SEG 1 at (102, 104, 0) SPAN: MAT 7 PCH 14 SEG 1" <<<"$o"; grep -q "PASS$" <<<"$o"
o=$(SIDE=E python3 -I odd/win.py ../red/n5inj/instances/returns_rt32.pg --mut); grep -q "SPAN_V 1 SPAN1 1 .*ex (12, 10, 3, 2, 0)" <<<"$o"   # control: length-only re-entry needs the factor n
echo "si (box 38: Lemma SPAN holds; in-window form inflated on tobs, span form not): PASS"
# box 38 §6: W-frame windows on hntop_N (N = 3 pinned: one guided stretch of 61; all 31, span 28, out 28 = 2N²+5N−5).
o=$(python3 -I odd/wret.py odd/inst/hn/hntop_n3.pg odd/inst/hn/hntop_n3.start); grep -q "iter 61 .*WRET_V 0 .*OPT_V 0 maxSW 28 maxWR 31 maxWRspan 28 maxWRout 28 .*PASS$" <<<"$o"
echo "si (box 38 §6: hntop_3 W-window counts): PASS"
# box 39 (docs/si/N5-SPANW-box39.md): span P-changes without W-changes (rise_thin51_n40 pair (28, 1): 55 vs 0); co-movement on hntop_3.
o=$(python3 -I odd/spanw.py ../red/so/instances/rise_thin51_n40.pg); grep -q "PCH 759 CO 388 WCH 388 TQ 759 maxPCH 55 maxDIFF 55 .*ex (28, 1, 9, 55, 0, 0)" <<<"$o"
o=$(python3 -I odd/spanw.py odd/inst/hn/hntop_n3.pg odd/inst/hn/hntop_n3.start); grep -q "PCH 373 CO 373 WCH 392 .*maxDIFF 0 " <<<"$o"
echo "si (box 39: span P-changes need not come with W-changes): PASS"
# box 40 (docs/si/N5-CUT-box40.md): Lemma W-RETURN-G (anchored re-entries are W-paid or silent), classes of re-entries across cuts.
o=$(python3 -I odd/cuts.py ../red/so/instances/rise_thin51_n40.pg); grep -q "REENT 125 CUTRE 14 FRESH 92 CYC 0 WPAID 19 SILENT 0 VIOL 0 .*LRISE_V 0 .*maxFRESHCUT 4 .* PASS" <<<"$o"
o=$(FR=1 python3 -I odd/cuts.py ../new/box59/out/fc_3.pg); grep -q "REENT 166 CUTRE 0 FRESH 97 .*VIOL 0 .* PASS" <<<"$o"
o=$(FR=1 MUT=nofresh python3 -I odd/cuts.py ../red/so/instances/rise_thin51_n40.pg); grep -q "VIOL 16 .* FAIL" <<<"$o"
o=$(MUT=off1 python3 -I odd/cuts.py ../red/so/instances/rise_thin51_n40.pg); grep -q "VIOL 92 .* FAIL" <<<"$o"
o=$(python3 -I odd/cuts.py odd/inst/red/spanobs_K12_m48.pg odd/inst/red/spanobs_K12_m48.start); grep -q "REENT 1077 CUTRE 0 FRESH 0 CYC 0 WPAID 1077 SILENT 0 VIOL 0 .* PASS" <<<"$o"
o=$(python3 -I odd/cuts.py odd/inst/red/carryobs_K12_m48.pg odd/inst/red/carryobs_K12_m48.start); grep -q "REENT 1609 CUTRE 0 FRESH 0 CYC 0 WPAID 1609 SILENT 0 VIOL 0 .* PASS" <<<"$o"
o=$(FR=1 python3 -I odd/cutsx.py ../red/so/instances/rise_thin51_n40.pg); grep -q "FR_WC 68 FR_GAIN 24 FR_SAME 0 FR_GAIN0 9 FR_CYC 0 FR_LATE 15 FR_LATE_V 0" <<<"$o"
echo "si (box 40: W-RETURN-G and cut-attached re-entries): PASS"
# box 42 (docs/si/N5-LATE-box42.md): late adoptions FIRST / REPEAT; a REPEAT needs a W-rise of z since the leave (RV 0).
o=$(python3 -I odd/laterep.py ../red/so/instances/so_th_n32.pg); grep -q "'late': 6, .*'first': 4, 'repeat': 2, 'RV': 0, 'cyc': 0, 'MAXE': 3" <<<"$o"
o=$(python3 -I odd/laterep.py ../red/so/instances/rise_thin51_n40.pg); grep -q "'late': 23, .*'first': 23, 'repeat': 0, 'RV': 0" <<<"$o"
echo "si (box 42: late adoptions FIRST / REPEAT): PASS"
# box 43 (docs/si/P-N5-CUT-box43.md, FROZEN packet): quotes verbatim (shifted control must fail); hntop_n3 W-runs have R* = 0 (L-NEW frozen.py --wrun).
python3 -I rund/quotecheck.py ../../docs/si/P-N5-CUT-box43.md | grep -q "quotes=13 bad=0"
python3 -I rund/quotecheck.py ../../docs/si/P-N5-CUT-box43.md --mut | grep -q "QUOTES FAIL"
o=$(cd ../new && python3 -I box64/frozen.py ../si/odd/inst/hn/hntop_n3.pg --start --wrun | tail -1); grep -q "its-phases 13 .*'lw': 12.*'R': 0} FWR-viol 0" <<<"$o"
echo "si (box 43: P-N5-CUT quotes, hntop_n3 R* 0): PASS"
# box 44 (docs/si/N5-REPCH-box44.md): REPEAT cause chains have depth 1, plain-switch parents.
o=$(python3 -I odd/repchain.py ../red/so/instances/so_th_n32.pg); grep -q "rep 2 silent 0 parF 0 parR 0 parS 2 maxdepth 1 LDEC_V 2 late 6" <<<"$o"
o=$(python3 -I odd/repchain.py ../new/box59/out/fc_8.pg); grep -q "rep 6 silent 0 parF 0 parR 0 parS 6 maxdepth 1 LDEC_V 0 late 30" <<<"$o"
echo "si (box 44: repeat cause chains): PASS"
# box 45 (docs/si/N5-PLAIN-box45.md): plain-wave transition form DEAD (runfam_K10 85 > 48); REP-PLAIN DEAD on latew_K20_m32 (570 FIRST parents).
o=$(python3 -I odd/repchain.py runlin/instances/runfam_K10.pg); grep -q "late 19 PLAINW 85 PLAINV 5" <<<"$o"
o=$(python3 -I odd/repchain.py odd/inst/red/latew_K20_m32.pg odd/inst/red/latew_K20_m32.start); grep -q "rep 570 silent 0 parF 570 parR 0 parS 0 maxdepth 1 .*late 641 PLAINW 60 PLAINV 39 WCHW 700 RTW 640 RLOCW 640 REPW 570 LOC_V 0 WIN0 0 WINF 570 WINR 0 PERWIN 30 WINCH_V 0 MAXWD 1 SELF 0" <<<"$o"
echo "si (box 45: plain-wave and REP-PLAIN kills): PASS"
# box 46 (docs/si/N5-SUB-box46.md): Corollary LOC-R* (WCH <= (n-1)(RLOC+1) per W-run) on runfam_K40; latew is pinned in «box 45».
o=$(python3 -I odd/repchain.py runlin/instances/runfam_K40.pg); grep -q "WCHW 159 RTW 8 RLOCW 8 REPW 1 LOC_V 0" <<<"$o"
echo "si (box 46: local late adoptions): PASS"
# box 47 (docs/si/N5-READ-box47.md): READ-CHARGE (every W-change has a switching cause on the play: RC_V 0); chain depth on runfam_K40.
o=$(python3 -I odd/readch.py runlin/instances/runfam_K40.pg); grep -q "wchg 343 roots 8 maxdepth 73 WRUN 5 RC_V 0" <<<"$o"
o=$(python3 -I odd/readch.py ../red/so/instances/so_th_n32.pg); grep -q "wchg 93 roots 10 maxdepth 21 WRUN 15 RC_V 0" <<<"$o"
echo "si (box 47: reader chains): PASS"
# box 48 (docs/si/N5-WDEPTH-box48.md): windows of late adoptions; a REPEAT-opened window feeds a repeat (so_th_n32, depth 2); Lemma WIN.
o=$(python3 -I odd/repchain.py ../red/so/instances/so_th_n32.pg); grep -q "WIN0 0 WINF 1 WINR 1 PERWIN 1 WINCH_V 0 MAXWD 2 SELF 0" <<<"$o"
echo "si (box 48: window depth): PASS"
# box 49 (docs/si/P-N5-REPD-box49.md, FROZEN packet): quotes verbatim (shifted control must fail). Data pins: «box 45», «box 46», «box 48».
python3 -I rund/quotecheck.py ../../docs/si/P-N5-REPD-box49.md | grep -q "quotes=3 bad=0"
python3 -I rund/quotecheck.py ../../docs/si/P-N5-REPD-box49.md --mut | grep -q "QUOTES FAIL"
echo "si (box 49: P-N5-REPD quotes): PASS"
# box 50 (docs/si/N5-ADD-box50.md): window DAG; R130's chain is a path (depth 7 at m 16), no (z, t*) token shared, no edge twice on a chain.
t=$(mktemp -d); LATE=2 python3 -I ../red/span/mkrw.py 4 16 $t/w.pg $t/w.start >/dev/null
cmp -s $t/w.pg odd/inst/red50/wdepth_K4_m16.pg
o=$(python3 -I odd/windag.py odd/inst/red50/wdepth_K4_m16.pg odd/inst/red50/wdepth_K4_m16.start); grep -q "RT 36 REP 21 X 0 NWIN 37 BETA 1 INDEG 1 NPATH 1 LONG 7 TOK 21 TOKSH 1 ETOK_V 0 SELFL 0 CHREP 0 EPATH 1" <<<"$o"
o=$(python3 -I odd/windag.py ../red/so/instances/so_th_n32.pg); grep -q "LONG 2 TOK 2 TOKSH 1 ETOK_V 0 SELFL 1 CHREP 0 EPATH 2" <<<"$o"
echo "si (box 50: window DAG): PASS"
# box 50 §6: re-blocked REPEATs paid by tied Xi-climbs (wdepth m 16 all re-blocked and tied).
o=$(python3 -I odd/tied.py odd/inst/red50/wdepth_K4_m16.pg odd/inst/red50/wdepth_K4_m16.start); grep -q "rep 21 tied 21 untied 0 reblk 21 untied_reblk 0 tsh 1" <<<"$o"
echo "si (box 50 §6: tied climbs): PASS"
# box 51 (docs/si/N5-LATEP-box51.md): TIED-RB DEAD (two engines); LATE' keeps FW-R* (FWV 0), no W-silent LATE' repeat (XP 0), GAP-CLIMB (GAPV 0, GTOKV 0).
C=odd/inst/si51/tiedmut_so_th_n32_11
python3 -I ../red/seg/xeng.py $C.pg $C.start | grep -q "state sequences identical: True"
o=$(python3 -I odd/tied.py $C.pg $C.start); grep -q "rep 1 tied 0 untied 1 reblk 1 untied_reblk 1" <<<"$o"
o=$(python3 -I odd/latep.py $C.pg $C.start); grep -q "RTP 4 REPP 1 XP 0 FWV 0 RSUB_V 0 LP 6 GAPV 0 GTOKV 0 TIEDG 4" <<<"$o"
o=$(python3 -I odd/latep.py odd/inst/red50/wdepth_K4_m16.pg odd/inst/red50/wdepth_K4_m16.start); grep -q "RT 36 RTP 36 REPP 21 XP 0 FWV 0 RSUB_V 0 LP 37 GAPV 0 GTOKV 0 TIEDG 35" <<<"$o"
o=$(python3 -I odd/latep.py ../new/box59/out/fc_6.pg); grep -q "RT 4 RTP 3 REPP 0 XP 0 FWV 0" <<<"$o"
echo "si (box 51: LATE', GAP-CLIMB, TIED-RB dead): PASS"
# box 52 (docs/si/N5-TXCD-box52.md): TXC-DESCENT (0 descent failures); gates carry the tied climbs (no GXC event on wdepth).
o=$(python3 -I odd/txcd.py ../red/so/instances/so_th_n32.pg); grep -q "TXC 73 T1 0 T2G 0 T2L 0 T3 73 T4 0 DESC_V 0 CYC_V 0 TERM_V 0 GXC 0 GATE 16 CNW 0 MULT 13" <<<"$o"   # re-derived after P-N5-LATEP fix D1 (was TXC 63 / GATE 15)
o=$(python3 -I odd/txcd.py odd/inst/red50/wdepth_K4_m16.pg odd/inst/red50/wdepth_K4_m16.start); grep -q "TXC 184 T1 0 T2G 0 T2L 0 T3 184 T4 0 DESC_V 0 CYC_V 0 TERM_V 0 GXC 0 GATE 93 CNW 0 MULT 32" <<<"$o"
o=$(python3 -I odd/txcd.py ../n5-exhaustive/instances/b5_o11.pg); grep -q "TXC 1 .* CNW 1 " <<<"$o"   # fix D2: a TXC event at an own W-cycle node (REFEREE-2 N-8)
echo "si (box 52: TXC descent): PASS"
# box 53 (docs/si/P-N5-LATEP-box53.md, FROZEN packet; line docs/si/P-N5-LATEP-line.txt): quotes verbatim (shifted control must fail). Data pins: «box 51», «box 52».
python3 -I rund/quotecheck.py ../../docs/si/P-N5-LATEP-box53.md | grep -q "quotes=6 bad=0"
python3 -I rund/quotecheck.py ../../docs/si/P-N5-LATEP-box53.md --mut | grep -q "QUOTES FAIL"
echo "si (box 53: P-N5-LATEP quotes): PASS"
# box 50b (docs/si/N5-FL-box50b.md): FL_F on W-runs; FLAT-Z (Z only shrinks at W-flat transitions); FL-GAP; u23sw64 FL = ZFL = 8.
o=$(python3 -I fl/flat.py ../red/xing/instances/u23sw64_n32.pg); grep -q "ZFL 8 ZA 32 ZSHR_V 0 ZIN_V 0 FLGAP_V 0 FL 8 FLI 8 FLV 6 LCTFL 0 SW 64 NOTZ_V 0 NOCL_V 0 WCH_V 0 GXC 64" <<<"$o"
o=$(python3 -I fl/flat.py ../red/kw/instances/cw11_n24.pg); grep -q "ZSHR_V 0 ZIN_V 0 FLGAP_V 0" <<<"$o"
echo "si (box 50b: FL, FLAT-Z): PASS"
# box 51b (docs/si/N5-GATE-box51b.md): Lemma GATE classes (no SPD climb without a gate climb, TRV_V 0), INTERVAL-SI checks (TIGHT_V, IMP_V 0),
# LEV-FLAT (MONO_V 0); u23sw64: 8 ZFL all SUB (Phi constant), gate data constant on [2, 10]; mkrw LATE=1: TXV 2K, XCV 2K + 1; L-RED copies.
o=$(python3 -I gate/gate.py ../red/xing/instances/u23sw64_n32.pg); grep -q "ZFL 8 SUB 8 PR 0 WCI 4 FLAT 8 TRV_V 0 ZZ_V 0 MONO_V 0 XFL 0 TIGHT_V 0 IMP_V 0 FLI 8 DMAX 1 TXC 72 TXV 8 XCV 8 NSPW 72 XGRD 60 XNGRD 4 LAZY 23" <<<"$o"
grep -q "ALL_GSELF 0 ALL_NOG 0 ALL_GCH 0 ALL_NDEC 0 ALL_NSP 72 ALL_SPD 0" <<<"$o"
python3 -I gate/const.py ../red/xing/instances/u23sw64_n32.pg | grep -q "interval \[2, 10\] flat 8 changes none"
o=$(python3 -I gate/gate.py ../red/xing/instances/u2flat73_n32.pg); grep -q "TRV_V 0 .* XGRD 62 XNGRD 11 LAZY 0" <<<"$o"
t=$(mktemp -d); LATE=1 python3 -I ../red/span/mkrw.py 4 16 $t/w.pg $t/w.start >/dev/null; LATE=1 python3 -I ../red/span/mkrw.py 8 16 $t/v.pg $t/v.start >/dev/null
python3 -I gate/gate.py $t/w.pg $t/w.start | grep -q "FLAT 0 .* TXV 8 XCV 9 "
python3 -I gate/gate.py $t/v.pg $t/v.start | grep -q "FLAT 0 .* TXV 16 XCV 17 "
echo "6d34c1617bb410ce78c392eb360ca28b6afea90f  gate/inst/latew_K16_m32.pg" | sha1sum -c --quiet
echo "e995709e256b55aa40cb94896a7dcb52446baf57  gate/inst/fx_K8_m32.pg" | sha1sum -c --quiet
echo "si (box 51b: GATE, INTERVAL-SI, potentials dead): PASS"
# box 51b §6-§7: DEEP_4 split (fcobs_6 all at W-changing transitions, D4 = box 87's 42); S1 not a fixed-order rule (u23sw64 REV 31).
python3 -I gate/deepint.py ../new/box59/out/fcobs_6.pg | grep -q "N4_IN 0 N4_BD 634 D4 42 D4_IN 0 D4_BD 42 FLAT 0"
python3 -I gate/deepint.py ../red/xing/instances/u23sw64_n32.pg | grep -q "D4_IN 5 .* FLAT 8 PERFLAT4 10"
python3 -I gate/revisit.py ../red/xing/instances/u23sw64_n32.pg | grep -q "interval \[2, 10\] flat 8 REV 31 SWV 6 OPT 5 BRANCH even"
echo "si (box 51b §6-§7: DEEP_4 split, REVISIT): PASS"
# box 51b §8: CONJECTURE LAYER-RESET data (UNX 0) and its control (MUT=1 must give UNX > 0).
python3 -I gate/layer.py ../red/xing/instances/u23sw64_n32.pg | grep -q "RET 31 UNX 0 RETL2 0 DEPTH 10 FLAT 8"
MUT=1 python3 -I gate/layer.py ../red/xing/instances/u23sw64_n32.pg | grep -q "RET 31 UNX 6 "
echo "si (box 51b §8: LAYER-RESET): PASS"
# box 51b §10: Lemma RETURN-CHARGE (RCV 0, RCX 0 on u23sw64's 31 returns), XCI 8.
python3 -I gate/layer.py ../red/xing/instances/u23sw64_n32.pg | grep -q "RET 31 UNX 0 RETL2 0 DEPTH 10 FLAT 8 RCV 0 RCX 0 XCI 8"
echo "si (box 51b §10: RETURN-CHARGE): PASS"
# box 51b §11-§12: RETURN-CHARGE' over whole runs (Even and Odd), SEG-XCH W-run bound, T-bound; charge OFF kill (cw11_n24).
python3 -I gate/retx.py ../red/xing/instances/u23sw64_n32.pg | grep -q "T 16 MONO_V 0 IMP_V 0 RET 70 RCV 0 FB_V 0 SLACK 247 LMAX 8 OMONO_V 0 OIMP_V 0 ORET 0 ORCV 0 TB_V 0"
# (box 52 fix: the old form «grep && ! grep» could not fail under set -e; same test, explicit exit)
grep -q "RETX" gate/retx_sbcg.txt
if grep -q "RCV [1-9]\|FB_V [1-9]\|TB_V [1-9]\|MONO_V [1-9]\|IMP_V [1-9]" gate/retx_sbcg.txt gate/retx_alt.txt gate/retx_red.txt; then echo "box 51b: retx violation"; exit 1; fi
python3 -I gate/charge.py ../red/kw/instances/cw11_n24.pg | grep -q "D4_OFF 1 D4_SELF 0 ALL_ON 6 ALL_OFF 4 ALL_SELF 12"
echo "si (box 51b §11-§12: RETURN-CHARGE', SEG-XCH, charge OFF): PASS"
# box 51b §13: head Xi-changes per W-run (mkrw LATE=1 K 4 m 16: HX 8 = 2K).
t=$(mktemp -d); LATE=1 python3 -I ../red/span/mkrw.py 4 16 $t/w.pg $t/w.start >/dev/null
python3 -I gate/heads.py $t/w.pg $t/w.start | grep -q "HX 8 XX 9 NHEAD 32 SUMHX 125 LMAX 76"
echo "si (box 51b §13: heads): PASS"
# box 52 (docs/si/N5-HEADS-box52.md): Theorem RUN-SETTLE's front (BADW 0; MUT=1 control bites on gci2_n12), the Xi-distance front DEAD
# (ladderd0_k12_n48 BAD1 11), proof cases on u23sw64 (TT 5, RR 0, OT 0, no violations), x32_rand48 one window of 44 at n 48,
# sbar avoids I_tau DEAD (lend107_n32 INIT 106), one old-target-fixed flip (nep13_n24 NOX 1, NONE 0); corpus outputs carry no violation.
python3 -I heads52/bffront.py ../red/ul/instances/ladderd0_k12_n48.pg ../red/ul/instances/ladderd0_k12_n48.start | grep -q "BAD1 11 BAD0 22 MINW1 2 BADW 0 SWB 11"
python3 -I heads52/bffront.py ../n5-epoch/instances/gci2_n12.pg ../n5-epoch/instances/gci2_n12.start | grep -q "MINW1 1 BADW 0 "
MUT=1 python3 -I heads52/bffront.py ../n5-epoch/instances/gci2_n12.pg ../n5-epoch/instances/gci2_n12.start | grep -q "MINW1 1 BADW 2 "
python3 -I heads52/swcase.py ../red/xing/instances/u23sw64_n32.pg | grep -q "NE 44 WR 0 TT 5 RR 0 OT 0 VNE 0 VWR 0 VTT 0 VRR 0 VOT 0 MINJ 3"
python3 -I heads52/rwin.py ../red/xing/instances/x32_rand48.pg | grep -q "LMAX 44 E 0 WMAX 44 .* WALL 44"
python3 -I heads52/dset.py ../n5-epoch/instances/lend107_n32.pg ../n5-epoch/instances/lend107_n32.start | grep -q "INIT 106 WSB 106 WSE 0 WSW 212"
python3 -I heads52/flipc.py ../n5-epoch/instances/nep13_n24.pg ../n5-epoch/instances/nep13_n24.start | grep -q "FLIPS 20 OLDX 19 NOX 1 .* NONE 0 "
if grep -q "BADW [1-9]" heads52/bffront_*.txt; then echo "box 52: BADW violation in corpus output"; exit 1; fi
if grep -q "V[A-Z]* [1-9]\|RR [1-9]\|OT [1-9]" heads52/swcase_*.txt; then echo "box 52: swcase violation"; exit 1; fi
if grep -q "NONE [1-9]" heads52/flipc_*.txt; then echo "box 52: flip NONE"; exit 1; fi
for f in rwin:RWIN swcase:SWC bffront:BFF flipc:FLIPC; do
  [ "$(cat heads52/${f%%:*}_*.txt | grep -c "${f##*:}")" = 1134 ] || { echo "box 52: ${f%%:*} outputs incomplete"; exit 1; }
done
cat heads52/rwin_*.txt | awk '{for(i=1;i<=NF;i++){if($i=="n")n=$(i+1); if($i=="WALL")w=$(i+1)}; if(w>=n-1) bad=1} END{exit bad}' || { echo "box 52: a window reaches n - 1"; exit 1; }
echo "si (box 52: RUN-SETTLE front, Xi-front DEAD, proof cases, defect set, flips): PASS"
# box 52 §3 (17:5xZ): FLIP-CAUSE'' DEAD on two kinds of vertex (n5b agrees: heads52/flipx.py), FLIP-EV data (corpus EVX 0).
python3 -I heads52/flipc.py heads52/inst/flipnone_n14.pg heads52/inst/flipnone_n14.start | grep -q "NONE 1 ENTX 0 OWNCN 1 NONEX 0 EXIX 0 EVX 1 EVXC 1"
python3 -I heads52/flipc.py heads52/inst/flipnonex_a_n10.pg heads52/inst/flipnonex_a_n10.start | grep -q "NONE 1 ENTX 0 OWNCN 0 NONEX 1 EXIX 1 EVX 0 "
python3 -I heads52/flipx.py heads52/inst/flipnonex_a_n10.pg heads52/inst/flipnonex_a_n10.start | grep -q "FLIP k 1 o 8 tau 4 old 9 new 4 oldXi_changed False newXi_changed False"
python3 -I heads52/flipx.py heads52/inst/flipnone_n14.pg heads52/inst/flipnone_n14.start | grep -q "FLIP k 1 o 12 tau 1 old 6 new 1 oldXi_changed False newXi_changed False"
if grep -q "EVX [1-9]" heads52/flipc_*.txt; then echo "box 52: FLIP-EV corpus violation"; exit 1; fi
echo "si (box 52 §3: FLIP-CAUSE'' DEAD, FLIP-EV data): PASS"
# box 52 packet P-N5-SETTLE FROZEN (Lead 18:14Z): the packet and its line file must not change (repairs go to P-N5-SETTLE-fixes.md).
echo "aef403c3d8a003bcfc6742c4d1da084a1e21669f  ../../docs/si/P-N5-SETTLE-box52.md" | sha1sum -c --quiet
echo "6aa094e32b03317797a551ac2fc719749cf59ca7  ../../docs/si/P-N5-SETTLE-line.txt" | sha1sum -c --quiet
echo "si (box 52: P-N5-SETTLE frozen): PASS"
# box 52 §3 (18:5xZ): FLIP-EV DEAD on flipev_n20 (EXI at non-own node 10, no event (iii) in the W-run; n5b agrees).
python3 -I heads52/flipc.py heads52/inst/flipev_n20.pg heads52/inst/flipev_n20.start | grep -q "NONEX 1 EXIX 1 EVX 1 EVXC 0 "
python3 -I heads52/rwin.py heads52/inst/flipev_n20.pg heads52/inst/flipev_n20.start | grep -q "EIII 0 "
python3 -I heads52/flipx.py heads52/inst/flipev_n20.pg heads52/inst/flipev_n20.start | grep -q "FLIP k 2 o 10 tau 4 old 1 new 4 oldXi_changed False newXi_changed False"
python3 -I heads52/flipx.py heads52/inst/flipev_n20.pg heads52/inst/flipev_n20.start | grep -q "FLIP k 2 o 14 tau 8 old 8 new 11 oldXi_changed True newXi_changed False"
echo "si (box 52 §3: FLIP-EV DEAD, flipev_n20): PASS"
