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
