#!/usr/bin/env bash
# L-NEW self-check (< 1 min), run by scripts/verify.sh: N1 (anneal.py, no merging) agrees with Zielonka and passes the
# strategy check on 40 seeded random games; integer-scaled values equal the Fraction values (--xcheck) on a pinned
# instance whose N1 count is pinned (switchallexp N=3: 42 Even iterations); renum.cpp reproduces vjfast's zadeh count on
# L-SI's pinned zadehexp_N5 (271) at the identity numbering; the C++ port anneal.cpp equals anneal.py on 30 random games.
set -euo pipefail
cd "$(dirname "$0")"
tmp=$(mktemp -d)
python3 -I anneal_random.py "$tmp/r" 40 5 | grep -q "AGREE 40/40" && echo "N1 vs Zielonka, 40 random games: PASS"
got=$(python3 -I anneal.py instances/switchallexp_N3.pg --nocompress --xcheck --check)
echo "$got" | grep -q "even_iters=42 " && echo "$got" | grep -q "zielonka OK strategies verified" && echo "N1 pinned switchallexp N=3 (42), xcheck: PASS"
if command -v g++ >/dev/null; then
  g++ -O2 -std=c++17 -o "$tmp/renum" renum.cpp
  g++ -O2 -std=c++17 -o anneal_c_check anneal.cpp
  ANNEAL_C=./anneal_c_check python3 -I xcheck_c.py "$tmp/xc" 30 9 | grep -q "XCHECK-C PASS 30/30" && echo "anneal_c vs anneal.py (30 games): PASS"
  rm -f anneal_c_check
  "$tmp/renum" zadeh ../si/instances/zadehexp_N5.pg --restarts 0 --steps 0 | grep -q "identity=271 " && echo "renum identity = vjfast zadeh (271): PASS"
else
  echo "g++ not found: renum check skipped"
fi
# Box 49 (successor 30): P-N5-OFFMONO-fixes quotes (76, at the referee §C commits 96b2cd9a / c040084a and the packet freezes), with the
# shifted-line control that must fail. NOT RUN (named) if a source commit is absent from this clone.
if git cat-file -e 96b2cd9a^{commit} 2>/dev/null && git cat-file -e c040084a^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-OFFMONO-fixes-box49.md | grep -q "quotes=76 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-OFFMONO-fixes-box49.md --mut >/dev/null; then
    echo "OFFMONO-fixes quotes 76 + shifted control: PASS"
    [ "$(sha1sum ../../docs/new/P-N5-OFFMONO-fixes-box49.md | cut -d' ' -f1)" = "490fc7f3ff31605062ac4239c3387873c06276e9" ] && echo "OFFMONO-fixes frozen sha1: PASS" || { echo "OFFMONO-fixes frozen sha1: FAILED"; exit 1; }
  else
    echo "OFFMONO-fixes quotes: FAILED"; exit 1
  fi
else
  echo "OFFMONO-fixes quotes: NOT RUN (96b2cd9a or c040084a not in this clone)"
fi
# Box 49 (successor 30), N5-READER: the embedded reader l121_d29 keeps long121's run and has XR 86 > 2n; NOSW and SW-AMORT hold on long121.
t49=$(mktemp -d)
d49=$(python3 -I box49/dress.py box48/instances/long121_n40.pg box48/instances/long121_n40.start "$t49/d29" "1:0:0,1,2,5,6,7,8,17,20,22,23,24,30,36,39:5" "EDGE:29:h0")
if echo "$d49" | grep -q "^SAME" && echo "$d49" | grep -q "(40, 1, 86, 74)" && \
   python3 -I box49/cross.py 0 1 box48/instances/long121_n40.pg | grep -q "NOSW 0 PASS 303 SW 246 SWAMORT_viol 0"; then
  echo "N5-READER: embedded reader (run SAME, XR 86), NOSW, SW-AMORT on long121: PASS"
else
  echo "N5-READER checks: FAILED"; exit 1
fi
rm -rf "$t49"
# Box 49 (successor 30): packet P-N5-FBCK (frozen): quotes (9) with the shifted-line control, its sha1, and Theorem FB-C^K's data check on
# the plain reader l121_cf35_39 (|C_f| 8, |C^K_f| 5, KVIOL absent).
if git cat-file -e e83fd19d^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-FBCK-box49.md | grep -q "quotes=9 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-FBCK-box49.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-FBCK-box49.md | cut -d' ' -f1)" = "7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f" ] && \
     fk=$(python3 -I box49/fbconf.py 0 1 box49/inst/l121_cf35_39.pg) && echo "$fk" | grep -q " Cf 8 Cf_K 5 " && ! echo "$fk" | grep -q KVIOL; then
    echo "P-N5-FBCK quotes 9 + control, sha1, FB-C^K on l121_cf35_39: PASS"
  else
    echo "P-N5-FBCK checks: FAILED"; exit 1
  fi
else
  echo "P-N5-FBCK quotes: NOT RUN (e83fd19d not in this clone)"
fi
# Box 49 (successor 30): P-N5-RESTRICT-fixes (frozen): 31 quotes at the §C commits 3b2631be / 864302d0 and the freeze 7e56744a, shifted control, sha1.
if git cat-file -e 3b2631be^{commit} 2>/dev/null && git cat-file -e 864302d0^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-RESTRICT-fixes-box48.md | grep -q "quotes=31 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-RESTRICT-fixes-box48.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-RESTRICT-fixes-box48.md | cut -d' ' -f1)" = "f33f00b36ab5626e7ccd24e3b2fdd75ca56b2764" ]; then
    echo "RESTRICT-fixes quotes 31 + control, sha1: PASS"
  else
    echo "RESTRICT-fixes checks: FAILED"; exit 1
  fi
else
  echo "RESTRICT-fixes quotes: NOT RUN (3b2631be or 864302d0 not in this clone)"
fi
# Box 49 (successor 30): P-N5-FBCK-fixes (frozen): 25 quotes at the §C commits 6b752e89 / 991f9e27 and the freeze 0e63596d, shifted control, sha1.
if git cat-file -e 6b752e89^{commit} 2>/dev/null && git cat-file -e 991f9e27^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-FBCK-fixes-box49.md | grep -q "quotes=25 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-FBCK-fixes-box49.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-FBCK-fixes-box49.md | cut -d' ' -f1)" = "19237624d32db379db858ea961861bd094441db1" ]; then
    echo "FBCK-fixes quotes 25 + control, sha1: PASS"
  else
    echo "FBCK-fixes checks: FAILED"; exit 1
  fi
else
  echo "FBCK-fixes quotes: NOT RUN (6b752e89 or 991f9e27 not in this clone)"
fi
# Box 49 (successor 30): packet P-N5-TOPSHAPE (frozen): quotes (2) + shifted control + sha1, and Lemma TOP-SHAPE's checks on long121 (VIOL absent).
tq=$(python3 -I box49/topmono.py 0 1 box48/instances/long121_n40.pg)
if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-TOPSHAPE-box49.md | grep -q "quotes=2 bad=0" && \
   ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-TOPSHAPE-box49.md --mut >/dev/null && \
   [ "$(sha1sum ../../docs/new/P-N5-TOPSHAPE-box49.md | cut -d' ' -f1)" = "c5b0e8d86745d6db5e0c9f6e1551b10c5b511b8f" ] && \
   echo "$tq" | grep -q "PCH 769 TDOWN" && ! echo "$tq" | grep -q VIOL; then
  echo "P-N5-TOPSHAPE quotes 2 + control, sha1, TOP-SHAPE on long121: PASS"
else
  echo "P-N5-TOPSHAPE checks: FAILED"; exit 1
fi
# Box 49 (successor 30): P-N5-TOPSHAPE-fixes (frozen): 17 quotes at the §C commits e0499401 / 0e2063bf and the freeze 4c2ea43e, shifted control, sha1.
if git cat-file -e e0499401^{commit} 2>/dev/null && git cat-file -e 0e2063bf^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-TOPSHAPE-fixes-box49.md | grep -q "quotes=17 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-TOPSHAPE-fixes-box49.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-TOPSHAPE-fixes-box49.md | cut -d' ' -f1)" = "be683e9fd1dcd64f48c9d02f2fac66fc214cff0d" ]; then
    echo "TOPSHAPE-fixes quotes 17 + control, sha1: PASS"
  else
    echo "TOPSHAPE-fixes checks: FAILED"; exit 1
  fi
else
  echo "TOPSHAPE-fixes quotes: NOT RUN (e0499401 or 0e2063bf not in this clone)"
fi
# Box 50 (successor 31): N5-VC working note: Theorem VC-BOUND checks (VC PASS), pinned VC values, reader-proofness, MUT control, two climbed pins.
has() { grep -qE "(^| )$1( |$)" <<<"$2"; }
v1=$(python3 -I box50/vcrun.py --one ../si/runlin/instances/runfam_K10.pg ../si/runlin/instances/runfam_K10.start)
v2=$(python3 -I box50/vcrun.py --one ../si/grun/out/anc_K10.pg ../si/grun/out/anc_K10.start)
v3=$(MUT=1 python3 -I box50/vcrun.py --one ../si/runlin/instances/runfam_K10.pg ../si/runlin/instances/runfam_K10.start)
v4=$(python3 -I box50/vcrun.py --one box50/out/vpf3_vc4.pg box50/out/vpf3_vc4.start)
v5=$(python3 -I box50/vcrun.py --one box50/out/ent1_vc6.pg box50/out/ent1_vc6.start)
if grep -q "VC PASS" <<<"$v1" && has dsig_max=3 "$v1" && has run_VC_max=3 "$v1" && has exec_VC_max=3 "$v1" && \
   grep -q "VC PASS" <<<"$v2" && has dsig_max=3 "$v2" && has run_VCbar_max=4 "$v2" && \
   has exec_VC_max=4 "$v3" && \
   grep -q "VC PASS" <<<"$v4" && has run_VC_max=4 "$v4" && grep -q "VC PASS" <<<"$v5" && has run_ENT_max=6 "$v5" && has run_VC_max=3 "$v5" && \
   [ "$(sha1sum box50/out/vpf3_vc4.pg | cut -d' ' -f1)" = "1aef63fe2a33d6b07cdadf06636e26dfedeb5966" ] && [ "$(sha1sum box50/out/ent1_vc6.pg | cut -d' ' -f1)" = "129e9df12266a37722b92e45c5657e45d5fc7d0f" ]; then
  echo "box 50 VC: VC-BOUND 0 violations, runfam_K10 / anc_K10 dsig 3 (VCbar 1 -> 4), MUT bites, pins vpf3_vc4 (run VC 4) and ent1_vc6 (ENT 6, VC 3): PASS"
else
  echo "box 50 VC checks: FAILED"; exit 1
fi
# Box 50 (successor 31): packet P-N5-VC (frozen): 5 quotes at trunk e3b435ab + shifted control + sha1.
if git cat-file -e e3b435ab^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-VC-box50.md | grep -q "quotes=5 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-VC-box50.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-VC-box50.md | cut -d' ' -f1)" = "078ad604cd232eed26a3fff7ad632852b0613e93" ]; then
    echo "P-N5-VC quotes 5 + control, sha1: PASS"
  else
    echo "P-N5-VC checks: FAILED"; exit 1
  fi
else
  echo "P-N5-VC quotes: NOT RUN (e3b435ab not in this clone)"
fi
# Box 51 (successor 32): N5-VCPHASE: Proposition DLC (one-player family, phase VC d at n < 2^(2d+1); VC-PHASE DEAD), two engines, DS-PAIR data.
v1=$(for d in 1 2 3 4; do python3 -I box51/dlccheck.py $d; done)
v2=$(python3 -I ../si/root/n5bcmp.py box51/out/dlc_d3.pg box51/out/dlc_d3.start | head -1)
v3=$(python3 -I box51/alt.py ../red/seg/instances/runquad_K3_m4_n54.pg)
if [ "$(grep -c "DLC PASS" <<<"$v1")" = 4 ] && grep -q "d=4 n=455 len=31 traces on the 4 x-edges=16 phase_VC=4 DLC PASS" <<<"$v1" && \
   grep -q "identical state sequences: True" <<<"$v2" && grep -q "max pairwise alt in a run: (10, " <<<"$v3" && \
   [ "$(sha1sum box51/out/dlc_d4.pg | cut -d' ' -f1)" = "f77955fde03e36de8a1b3696523780368d28a184" ] && \
   [ "$(sha1sum box51/out/dlc_d5.pg | cut -d' ' -f1)" = "345fae4c9644f63323c84846b0f85f10a78db837" ]; then
  echo "box 51 DLC: d = 1..4 one phase, trace formula, phase VC = d; n5b identical (d 3); runquad_K3 alt 10; pins sha1: PASS"
else
  echo "box 51 DLC checks: FAILED"; exit 1
fi
# Box 51 (successor 32): P-N5-VC-fixes (frozen): F1 (VC-N5 FALSE by DLC_d), 3 quotes at 21f3285a / db1d3707, shifted control, sha1.
if git cat-file -e 21f3285a^{commit} 2>/dev/null && git cat-file -e db1d3707^{commit} 2>/dev/null; then
  if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-VC-fixes-box50.md | grep -q "quotes=3 bad=0" && \
     ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-VC-fixes-box50.md --mut >/dev/null && \
     [ "$(sha1sum ../../docs/new/P-N5-VC-fixes-box50.md | cut -d' ' -f1)" = "9e8b7bd208aae5eb3f540d0e5d7f8c77a0834370" ]; then
    echo "P-N5-VC-fixes quotes 3 + control, sha1: PASS"
  else
    echo "P-N5-VC-fixes checks: FAILED"; exit 1
  fi
else
  echo "P-N5-VC-fixes quotes: NOT RUN (21f3285a or db1d3707 not in this clone)"
fi
# Box 52 (successor 32): N5-RLV: arena-frozen cut (Lemma W-SPLIT''), reader pair long121 / l121reader (SBCH'' 30 = 30), comparator graft topfix_3 (SBCH'' 24).
v1=$(python3 -I box52/rlv.py --one ../si/root/instances/l121reader_n41.pg ../si/root/instances/l121reader_n41.start)
v2=$(python3 -I box52/rlv.py --one box48/instances/long121_n40.pg box48/instances/long121_n40.start)
v3=$(python3 -I box52/rlv.py --one box52/out/topfix_n3_cmp.pg box52/out/topfix_n3_cmp.start)
ok=1; for v in "$v1" "$v2" "$v3"; do for k in ARENA SPLIT FWBF2 FWLEN2; do grep -q "^$k PASS" <<<"$v" || ok=0; done; done
if [ $ok = 1 ] && grep -q ", 1, 122, 8, 0, 74, 30, 0, 25, 6, 6, 41)" <<<"$v1" && grep -q ", 1, 122, 8, 0, 33, 30, 0, 25, 6, 6, 40)" <<<"$v2" && \
   grep -q "0, 41, 0, 8, 24, 24, 0, 9, 1, 1, 66)" <<<"$v3" && \
   [ "$(sha1sum box52/out/topfix_n8_cmp.pg | cut -d' ' -f1)" = "6427c10505559df11a9660094dd4e235766e3b31" ]; then
  echo "box 52 RLV: SBCH'' reader-proof (74 -> 30 = 30), topfix_3 graft 24 = 2N^2+3N-3, checks PASS"
else
  echo "box 52 RLV checks: FAILED"; exit 1
fi
# Box 53 (successor 32): N5-RANK: exact Farkas-circuit certificates (no linear / lexicographic ranking function) for F24, F24m, F45, edge bits; corrupted control.
v=$(cd ../.. && python3 -I experiments/new/box53/cert.py experiments/new/box53/cert/f0_u23sw64_n32.json experiments/new/box53/cert/f4_b5_os_n16.json experiments/new/box53/cert/f5_returns_ph64.json experiments/new/box53/cert/f6_lend9_n8.json)
bad=$(mktemp); python3 -c "import json,sys; c=json.load(open('box53/cert/f6_lend9_n8.json')); c['y'][0][1]+=1; json.dump(c,open(sys.argv[1],'w'))" $bad
if [ "$(grep -c "CERT OK" <<<"$v")" = 4 ] && ! (cd ../.. && python3 -I experiments/new/box53/cert.py $bad >/dev/null); then
  echo "box 53 RANK: 4 certificates exact (F24 u23sw64_n32 / F24m b5_os_n16 / F45 returns_ph64 / edge bits lend9_n8), control fails: PASS"
else
  echo "box 53 RANK checks: FAILED"; exit 1
fi
rm -f $bad
# Box 54 (successor 32): N5-SF: fallback instance (NOFB dead), W-frame twin cycles on theta_thf16, switchbestexp_2 (SF 58 vs N5 32), topfix_3 (SF 64).
v1=$(python3 -I box54/sfrun.py ../n5-exhaustive/instances/n3all_maxph_0.pg ../n5-exhaustive/instances/n3all_maxph_0.start)
v2=$(MODE=w python3 -I box54/sfrun.py ../red/n5inj/instances/theta_thf16.pg)
v3=$(python3 -I box54/sfrun.py box54/out/switchbestexp_2.pg)
v4=$(python3 -I box54/sfrun.py box52/out/topfix_n3.pg box52/out/topfix_n3.start)
ok=1; for v in "$v1" "$v3" "$v4"; do for k in WIN OPT R17 CYC; do grep -q "^$k PASS" <<<"$v" || ok=0; done; done
if [ $ok = 1 ] && grep -q "^ROW ../n5-exhaustive/instances/n3all_maxph_0.pg 3 3 1 2 1 False" <<<"$v1" && grep -q "^CYC FAIL" <<<"$v2" && \
   grep -q "^ROW box54/out/switchbestexp_2.pg 60 32 2 58 0 False 4 0 5 19" <<<"$v3" && grep -q "^ROW box52/out/topfix_n3.pg 63 61 2 64 0 False" <<<"$v4" && \
   [ "$(sha1sum ../red/n5inj/instances/theta_thf16.pg | cut -d' ' -f1)" = "90ed13cf9e2c81c1aa3ab3c2058ac736a1ed489b" ]; then
  echo "box 54 N5-SF: correct on the pins, fallback fires (n3all_maxph_0), W-frame twin cycles (theta_thf16), switchbestexp_2 58 vs 32: PASS"
else
  echo "box 54 N5-SF checks: FAILED"; exit 1
fi
# Box 55 (successor 33): packet P-N5-SF (docs/new/P-N5-SF-box55.md §4): pcheck on three pins (DECOUPLE orbit, SF-RED step identity, bounds), MUT bites, quotes; NO-TRANSFER on switchbestexp_2.
w1=$(python3 -I box55/pcheck.py ../n5-exhaustive/instances/n3all_maxph_0.pg ../n5-exhaustive/instances/n3all_maxph_0.start)
w2=$(python3 -I box55/pcheck.py box54/out/switchbestexp_2.pg)
w3=$(python3 -I box55/pcheck.py ../red/n3/instances/n3cov_lean.pg box113/inst/n3cov_lean_fixed.start)  # box 113: start repaired (3 wrong-player entries dropped, D-ODD-1 validation)
w4=$(MUT=1 python3 -I box55/pcheck.py box54/out/switchbestexp_2.pg || true)
w5=$(python3 -I box55/ntcheck.py box54/out/switchbestexp_2.pg)
if grep -q "^CHECK PASS" <<<"$w1" && grep -q "^CHECK PASS" <<<"$w2" && grep -q "^CHECK PASS" <<<"$w3" && \
   grep -q "^ROW E_ n 3 m 6 values 3 orbit 3 SBC 1 LAM 1 SEG 2 SEGMAX 1$" <<<"$w1" && \
   grep -q "^ROW E_ n 60 m 130 values 59 orbit 59 SBC 4 LAM 0 SEG 5 SEGMAX 18$" <<<"$w2" && \
   grep -q "^ROW E_ n 48 m 128 values 29 orbit 29 SBC 11 LAM 4 SEG 12 SEGMAX 6$" <<<"$w3" && \
   grep -q "^ROW O_ n 48 m 128 values 6 orbit 6 SBC 3 LAM 5 SEG 6 SEGMAX 0$" <<<"$w3" && \
   grep -q "^E_ORB_V" <<<"$w4" && grep -q "^CHECK FAIL" <<<"$w4" && grep -q "^NT PASS" <<<"$w5" && \
   [ "$(sha1sum box54/out/switchbestexp_2.pg | cut -d' ' -f1)" = "b3d5bc293d1b76ce5c7ae8dadc4e9b0b51294484" ] && \
   [ "$(sha1sum ../red/n3/instances/n3cov_lean.pg | cut -d' ' -f1)" = "bcf8dbf64cba48123dc7da849b179793257e13e1" ] && \
   [ "$(sha1sum ../../docs/new/P-N5-SF-box55.md | cut -d' ' -f1)" = "dbc2345f62454d442e951de025b1b2aef8a35317" ] && \
   python3 -I box49/quotecheck3.py ../../docs/new/P-N5-SF-box55.md | grep -q "quotes=18 bad=0" && \
   ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-SF-box55.md --mut >/dev/null; then
  echo "box 55 P-N5-SF: pcheck PASS on n3all_maxph_0 (fallback), switchbestexp_2 (SBC 4), n3cov_lean (LAM 4, SBC 11), MUT bites; quotes PASS: PASS"
else
  echo "box 55 P-N5-SF checks: FAILED"; exit 1
fi
# Box 56 (successor 33): Theorem EXIT / Lemma LOC-OPT on 400 random class games (half with H-EXIT broken), switchbestexp_2 classes, GROUP on switchbestexp_2.
x1=$(python3 -I box56/exit.py --rand 400 2 0.5)
x2=$(python3 -I box56/exit.py box54/out/switchbestexp_2.pg)
x3=$(python3 -I box55/grp.py box54/out/switchbestexp_2.pg)
if grep -q "^EXIT PASS" <<<"$x1" && grep -q "EXIT_V=0 FLIPMAX=3 FLIPMAX_GOOD=1 GOOD=2285 LOC_V=0 TIES=298" <<<"$x1" && \
   grep -q "^n=60 CH=2 EXIT=1 TOP=0 GOOD=0 TIES=0 FLIPMAX_GOOD=0 FLIPMAX=3 LOC_V=0 EXIT_V=0 values=59 SBC=4$" <<<"$x2" && \
   grep -q "groups 4 GVCmax 20 stretches_of_it 2 GSTEPmax 20 GVC>n-1 0" <<<"$x3"; then
  echo "box 56 EXIT: LOC-OPT 0 violations, EXIT flips <= 1 (2285 good vertices), switchbestexp_2 CC fails H-TOP, GROUP 20 <= 59: PASS"
else
  echo "box 56 EXIT checks: FAILED"; exit 1
fi
# Box 57 (successor 33): N5-CARRY: on switchbestexp_4, F 258 steps; the CLS=g hybrid (I^glo's step at the 4 stale-reset lags) restores I^glo's 286; forced strictly on switchbestexp_5 at 217.
y1=$(CLS=g python3 -I box56/hybrid.py box54/out/switchbestexp_4.pg CLS | head -1)
y2=$(python3 -I box56/hybrid.py box54/out/switchbestexp_4.pg F | head -1)
y3=$(python3 -I box56/forced.py box54/out/switchbestexp_5.pg 217)
if grep -q "^CLS g steps 286 glo_steps_used 4 patterns 27 distinct 16$" <<<"$y1" && grep -q "^F  steps 258 " <<<"$y2" && \
   [ "$(grep -c "stale frame: F-option STRICTLY better | true frame: F-option STRICTLY worse" <<<"$y3")" = 2 ]; then
  echo "box 57 CARRY: switchbestexp_4 F 258, hybrid with 4 stale-reset corrections 286 (= I^glo), lags strict in both frames: PASS"
else
  echo "box 57 CARRY checks: FAILED"; exit 1
fi
# P-N5-SF fixes file (successor 33): the quotes of F7-F13 hold at trunk e251d147; the shifted control fails.
if python3 -I box49/quotecheck3.py ../../docs/new/P-N5-SF-fixes-box55.md | grep -q "quotes=6 bad=0" && \
   ! python3 -I box49/quotecheck3.py ../../docs/new/P-N5-SF-fixes-box55.md --mut >/dev/null; then
  echo "P-N5-SF fixes F7-F13: quotes PASS: PASS"
else
  echo "P-N5-SF fixes quotes: FAILED"; exit 1
fi
# Box 58 (successor 33): look-ahead LA_1 = I^glo on switchbestexp_4 (286), F 258, LAG_1 155.
z1=$(python3 -I box58/la.py box54/out/switchbestexp_4.pg 1); z2=$(python3 -I box58/la.py box54/out/switchbestexp_4.pg 0); z3=$(LAG=1 python3 -I box58/la.py box54/out/switchbestexp_4.pg 0)
if grep -q "steps 286 distinct_sbar 16" <<<"$z1" && grep -q "steps 258 distinct_sbar 16" <<<"$z2" && grep -q "steps 155 distinct_sbar 14" <<<"$z3"; then
  echo "box 58 LA: switchbestexp_4 LA_1 286 (= I^glo), F 258, LAG_1 155: PASS"
else
  echo "box 58 LA checks: FAILED"; exit 1
fi
# Box 59 (successor 34): N5-FC: fcN's flip word is W_N with cascades only after records (fc_4, sha1 3562ec4d); PV data line on so_sor5_n24.
w1=$(python3 -I box59/fcword.py box59/out/fc_4.pg 4); w2=$(python3 -I box59/frec.py ../red/so/instances/so_sor5_n24.pg)
if grep -q "^FCWORD N 4 n 110 SBC 16 W PASS C PASS$" <<<"$w1" && grep -q "^FCOPEN N 4 PASS" <<<"$w1" && grep -q "^FCLAT N 4 PASS" <<<"$w1" && \
   grep -q "n 24 k 1 orbit 23 SBC 22 maxflips 22 " <<<"$w2" && [ "$(sha1sum box59/out/fc_4.pg | cut -c1-12)" = 3562ec4d15eb ]; then
  echo "box 59 FC: fc_4 word W_4 (SBC 16), FCOPEN, FCLAT; so_sor5_n24 maxflips 22 <= n 24: PASS"
else
  echo "box 59 FC checks: FAILED"; exit 1
fi
w3=$(python3 -I box59/relcheck.py box59/out/fcobs_3.pg)
if grep -q "^REL fcobs_3.pg n 88 m 208 |R| 87 orbit 122 SBC 111 SBC_R 9 LAM 0 SEGMAX 24 PASS$" <<<"$w3" && [ "$(sha1sum box59/out/fcobs_3.pg | cut -c1-12)" = 719d04830887 ]; then
  echo "box 59 REL: fcobs_3 raw SBC 111, SBC_R 9, SF-RED-R checks (LOC, VAL, SEG, TOT): PASS"
else
  echo "box 59 REL checks: FAILED"; exit 1
fi
w4=$(python3 -I box59/pvplay.py box59/out/fcobsP_3.pg)
if grep -q "^PVPLAY fcobsP_3.pg n 90 rawmax 108 playmax 108 playSBC 111 VIOL$" <<<"$w4" && [ "$(sha1sum box59/out/fcobsP_3.pg | cut -c1-12)" = df9fcc64bafd ]; then
  echo "box 60 PV-PLAY counterexample: fcobsP_3 on-play flips 108 > n 90: PASS"
else
  echo "box 60 PV-PLAY checks: FAILED"; exit 1
fi
w5=$(python3 -I box59/sbcg.py box59/out/fcobsP_3.pg)
if grep -q "^SBCG fcobsP_3.pg n 90 m 211 orbit 122 SBC 111 SBC_G 8 SEGMAX 27 maxGflips 5 PASS$" <<<"$w5"; then
  echo "box 60 SBC_G: fcobsP_3 raw SBC 111, SBC_G 8 (= fc_3), segments within SF-RED-G (a): PASS"
else
  echo "box 60 SBC_G checks: FAILED"; exit 1
fi
w6=$(python3 -I box59/coarse.py box59/out/fc_3.pg)
if grep -q "^COARSE fc_3.pg n 85 m 187 I 121 .* SBC_G 8 DEPTH 5 C 10 viol 5 " <<<"$w6"; then
  echo "box 61 DEPTH: fc_3 I 121, SBC_G 8, needed depth 5, coarse (K=1) records 10 miss 5 segments: PASS"
else
  echo "box 61 DEPTH checks: FAILED"; exit 1
fi
w7=$(python3 -I box59/dwopen.py box59/out/dw_4.pg 4); w8=$(python3 -I box54/n5sf.py box59/out/dw_4.pg)
if grep -q "^DWOPEN N 4 word BINARY sets_k>=1 7 every-set-opens-and-lane-first PASS SBC 26$" <<<"$w7" && grep -q "^iterations 286 " <<<"$w8" && \
   [ "$(python3 -I box59/dw.py 4 | sha1sum | cut -c1-12)" = 19783274245b ]; then
  echo "box 62 DW: dw_4 N5-SF 286 = 19*2^4-18, sbar binary counter, lane-first gap at every set: PASS"
else
  echo "box 62 DW checks: FAILED"; exit 1
fi
w9=$(EOPP=tau OOPP=sigma python3 -I box59/mix.py box59/out/dw_3.pg); w10=$(EOPP=sbar OOPP=sigma python3 -I box59/mix.py box59/out/dw_3.pg)
if grep -q "iterations 41 .* tau-changes 3 " <<<"$w9" && grep -q "iterations 134 " <<<"$w10"; then
  echo "box 62 FRAME: dw_3 with tau in Even's arena (N5) 41, with sbar(sigma) 134: PASS"
else
  echo "box 62 FRAME checks: FAILED"; exit 1
fi
w11=$(python3 -I box59/freeze2.py box59/out/dw_3.pg)
if grep -q "^FREEZE2 dw_3.pg states 42 hyp-hits 81 viol 0 PASS$" <<<"$w11"; then
  echo "box 63 ODD-FREEZE: dw_3 81 hypothesis hits, 0 improving: PASS"
else
  echo "box 59 FC checks: FAILED"; exit 1
fi
w12=$(python3 -I box64/frozen.py box59/out/dw_3.pg); w13=$(python3 -I box64/stretch.py ../red/ctl/instances/d_runquad_K8_m30_n192.pg --start)
if grep -q "max-stretch-sig 26 its-phases 4 its-causes {'fb': 0, 'sbar': 3, 'lx': 0, 'lw': 0} .* FWR-viol 0$" <<<"$w12" && grep -q " #sig-1 0 #tau-1 264 .* max-tau-per-sigma-stretch 264 " <<<"$w13"; then
  echo "box 64 STRETCH: dw_3 longest tau-stretch 26 = 4 frozen phases (3 sbar cuts); d_runquad_K8 mirror 264 tau-changes, sigma constant: PASS"
else
  echo "box 64 STRETCH checks: FAILED"; exit 1
fi
w14=$(python3 -I box64/stretch.py box64/mkr/mk_4_16.pg --start)
if grep -q "n 102 m 151 n+m 253 iters 76 fb 0 #sig-1 76 #tau-1 0 tau-stretches 1 " <<<"$w14"; then
  echo "box 64 FRAME-STRETCH DEAD family: mk_4_16 one tau-stretch of 76 sigma-changes: PASS"
else
  echo "box 64 mkr check: FAILED"; exit 1
fi
w15=$(python3 -I box64/frozen.py box59/out/dw_3.pg --wrun)
if grep -q "^WRUN dw_3.pg .* worst-frozen-phase {'len': 26, 'wch': 26, 'flat': 0, 'R': 4} FWR-viol 0$" <<<"$w15"; then
  echo "box 64 GP*-RUN: dw_3 one W-run of 26 W-changing transitions, 4 late adoptions, FW-R* holds: PASS"
else
  echo "box 64 wrun check: FAILED"; exit 1
fi
w16=$(python3 -I box66/latepair.py ../n5-exhaustive/instances/b6_xl2_n32.pg)
if grep -q "max-per-lambda-run-edge 4 max-per-piece-edge 1 .* viol 0$" <<<"$w16"; then
  echo "box 66 LATE: b6_xl2_n32 one edge late-adopted 4 times in one lambda-run, 1 per piece (boundary obstruction): PASS"
else
  echo "box 66 LATE check: FAILED"; exit 1
fi
w17=$(cd .. && python3 -I new/box67/energy.py n5-epoch/instances/lend9_n8.pg n5-epoch/instances/lend9_n8.start)
if grep -q "inphase-fb 3 fmax 3 FBUP \[3, 2, 3, 3, 3, 1\] .* ZGROW 0$" <<<"$w17"; then
  echo "box 67 FBENERGY: lend9_n8 3 in-phase fallbacks, gap set never grows (GAP-MON), never shrinks (E3 strict DEAD): PASS"
else
  echo "box 67 FBENERGY check: FAILED"; exit 1
fi
w18=$(cd .. && python3 -I new/box68/zflat.py n5-epoch/instances/nep22f_n64.pg n5-epoch/instances/nep22f_n64.start)
if grep -q "'fb': 10, 'zflat': 10, 'zflat_wch': 10, 'swout': 0, 'reop': 0, 'reopnw': 0" <<<"$w18"; then
  echo "box 68 ZFLAT: nep22f_n64 10 Z-flat fallbacks in a saturated gap, SW-IN and REOPEN-W hold: PASS"
else
  echo "box 68 ZFLAT check: FAILED"; exit 1
fi
w19=$(cd .. && python3 -I new/box70/silent.py red/xing/instances/u23sw64_n32.pg)
if grep -q "classes {'S': 31} .* SCrun 31 max-S-per-piece-edge 1 S-at-Wflat 31/31 GXCrun 64 S-not-GXC 0$" <<<"$w19"; then
  echo "box 70 SC: u23sw64_n32 31 W-silent re-entries in one lambda-run, all GXC events (SIL-Z): PASS"
else
  echo "box 70 SC check: FAILED"; exit 1
fi
w20=$(cd .. && python3 -I new/box70/silent.py new/box71/inst/s2piece_n32.pg new/box71/inst/s2piece_n32.start)
if grep -q "classes {'S': 26} max-S-per-edge 2 .* max-S-per-piece-edge 2 S-at-Wflat 26/26" <<<"$w20"; then
  echo "box 71 S2: s2piece_n32 two S re-entries of (15, 8) in one piece (<= 1 per (piece, edge) DEAD): PASS"
else
  echo "box 71 S2 check: FAILED"; exit 1
fi
w21=$(cd .. && python3 -I new/box72/gxc.py red/xing/instances/u23sw64_n32.pg; python3 -I new/box72/gxc.py red/xing/instances/u23sw64_n32.pg --lz --lzc)
if grep -q "iters 16 fallbacks 1 events 64 .*cat {('s4a', 'Wsame', 'open'): 64}" <<<"$w21" && grep -q "CHK u23sw64_n32.pg tie_ok 64 tie_bad 0" <<<"$w21" \
   && grep -q "iters 6 fallbacks 1 events 0 " <<<"$w21"; then
  echo "box 72 LZ: u23sw64_n32 64 GXC events all S4a W-ties (TIE 64/64); N5-LZC 6 iterations, 0 GXC: PASS"
else
  echo "box 72 LZ check: FAILED"; exit 1
fi
w22=$(cd .. && python3 -I new/box72/silentlz.py red/kw/instances/cw11_n24.pg; python3 -I new/box72/wincmp.py red/kw/instances/cw11_n24.pg)
if grep -q "iters 10 classes {'F': 12} max-S-per-edge 0 max-C-per-edge 0" <<<"$w22" && grep -q "WIN cw11_n24.pg SAME n5 17 lzc 10" <<<"$w22"; then
  echo "box 72 LZ: cw11_n24 N5-LZC no C / S re-entries (N5: C 3), same winners: PASS"
else
  echo "box 72 LZ cw11 check: FAILED"; exit 1
fi
w23=$(cd .. && python3 -I new/box72/txc.py new/box72/inst/wdepth_K4_m16.pg new/box72/inst/wdepth_K4_m16.start; python3 -I new/box72/runlzc.py new/box72/tied_lsi_4fb0bfba.py new/box72/inst/wdepth_K4_m16.pg new/box72/inst/wdepth_K4_m16.start)
if grep -q "txc 184 .* gxc 0 .* src {'SBAR': 93, 'WIT': 91}" <<<"$w23" && grep -q "rep 21 tied 21 untied 0 reblk 21" <<<"$w23"; then
  echo "box 72 TXC: wdepth_K4_m16 184 tied climbs, all Odd-sourced (SBAR 93, WIT 91), GXC 0; 21 tied REPEATs also on N5-LZC: PASS"
else
  echo "box 72 TXC check: FAILED"; exit 1
fi
w24=$(cd .. && python3 -I new/box73/fbo.py new/box73/inst/cf_n24.pg new/box73/inst/cf_n24.start)
if grep -q "fbo 96 per-phase 96 per-v-phase 9 rel {'SAME-C-fixed': 96} .* fb 9 rho 0 " <<<"$w24"; then
  echo "box 73 FBO: cf_n24 96 = 4n FBO events in one phase (rho 0, 9 fallbacks; FBO-LIN DEAD): PASS"
else
  echo "box 73 FBO check: FAILED"; exit 1
fi
w25=$(cd .. && python3 -I new/box74/rho.py new/box74/inst/cr_n24.pg new/box74/inst/cr_n24.start)
if grep -q "n 24 |Q| 10 .* max-len 17 .* max-rho 162 max-rho-per-q 17 max-sbq 32 " <<<"$w25"; then
  echo "box 74 RHO: cr_n24 rho 162 = 6.75n in one 17-step W-run (|Q| 10), sbar-changes 32: PASS"
else
  echo "box 74 RHO check: FAILED"; exit 1
fi
w26=$(cd .. && python3 -I new/box75/sbq.py n5-exhaustive/instances/thetaA_n7.pg n5-exhaustive/instances/thetaA_n7.start)
if grep -q "n 7 |Q| 1 sum(deg-1) 1 iters 3 phases 1 .* revisits 1 vec-returns 1 " <<<"$w26"; then
  echo "box 75 SBAR: thetaA_n7 sbar(6) = 5 -> 1 -> 5 in one phase (no sbar-potential): PASS"
else
  echo "box 75 SBAR check: FAILED"; exit 1
fi
w27=$(cd .. && python3 -I new/box76/sbqrun.py new/box76/inst/cs_n32.pg new/box76/inst/cs_n32.start)
if grep -q "n 32 mO 108 mE 39 wruns 1 max-len 9 max-sbq 173 max-new 57 max-ret 116 " <<<"$w27"; then
  echo "box 76 SBQ: cs_n32 173 = 5.4n sbar-changes in a 9-step W-run, 116 returns (SBQ-2 DEAD): PASS"
else
  echo "box 76 SBQ check: FAILED"; exit 1
fi
w28=$(cd .. && python3 -I new/box77/fixdepth.py n5-epoch/instances/nep92_n40.pg n5-epoch/instances/nep92_n40.start)
if grep -q "mono-viol 0 trans 93 strict 20 flat 73 max-stall 34 .* max-flat-changes-per-(v,phase) (66, 0, 5, 92)" <<<"$w28"; then
  echo "box 77 FIXD: nep92_n40 FIX-DEPTH monotone, 66 = 1.65n dead-branch climbs at v 0 in one phase (FLAT-LIN DEAD): PASS"
else
  echo "box 77 FIXD check: FAILED"; exit 1
fi
w29=$(cd .. && python3 -I new/box78/retwch.py red/so/instances/tog6b_n32.pg; python3 -I new/box78/retwch.py si/runlin/instances/runfam_K10.pg --lzc)
if grep -q "RETWCH tog6b_n32.pg n 32 wruns 1 {'returns': 4, 'paid-W': 3, 'paid-tie': 1} " <<<"$w29" && grep -q "RETWCH runfam_K10.pg n 49 wruns 1 {'returns': 71, 'paid-W': 71} " <<<"$w29"; then
  echo "box 78 RETWCH: every Even return paid by a W-change of its target or a tie-leave (tog6b_n32 N5; runfam_K10 N5-LZC 71/71): PASS"
else
  echo "box 78 RETWCH check: FAILED"; exit 1
fi
w30=$(cd .. && python3 -I new/box79/wchpk.py red/so/instances/tog6b_n32.pg; python3 -I new/box79/wchpk.py red/so/instances/tog6b_n32.pg --lzc; python3 -I new/box79/symtest.py ../docs/new/P-N5-WCH-box79-line-W1.txt | tail -1; python3 -I new/box79/quotecheck.py | tail -1)
if grep -q "WCHPK tog6b_n32.pg n 32 wruns 1 {'returns': 4, 'paid-W': 3, 'TT': 1, 'TIE': 2} " <<<"$w30" && grep -q "WCHPK tog6b_n32.pg n 32 wruns 1 {'returns': 3, 'paid-W': 3, 'TIE': 0} " <<<"$w30" && grep -q "^SYMTEST PASS" <<<"$w30" && grep -q "^QUOTECHECK PASS" <<<"$w30"; then
  echo "box 79 WCH: P-N5-WCH RET-WCH (TT form) on tog6b_n32 (N5 TT 1, N5-LZC TIE 0); line W1 strict symbol test PASS; SPEC quote check PASS"
else
  echo "box 79 WCH check: FAILED"; exit 1
fi
w31=$(cd .. && python3 -I new/box79/flatsrc.py n5-epoch/instances/nep92_n40.pg n5-epoch/instances/nep92_n40.start)
if grep -q "{'K-rise': 20, 'FLATTR': 73, 'FSW': 73} max-FLATTR-phase 73 max-FLATSW-(x,phase) 8" <<<"$w31"; then
  echo "box 79 FLATSRC: nep92_n40 all 73 flat transitions carry a flat Even switch (<= 8 per vertex): PASS"
else
  echo "box 79 FLATSRC check: FAILED"; exit 1
fi
w32=$(cd .. && python3 -I new/box80/ladder.py 8)
if grep -q "LADDER k 8 n 18 switches 749 T-rises 255 (2^k-1 = 255) distinct-T 256 strict True non-improving-switches 0 monotonicity-violations 0 cycle-nodes \[0\]" <<<"$w32"; then
  echo "box 80 LADDER: ladder_8 (n 18) one vertex takes 256 W-values under single improving switches (relaxation R0): PASS"
else
  echo "box 80 LADDER check: FAILED"; exit 1
fi
w33=$(cd .. && python3 -I new/box81/gladder.py 6; python3 -I new/box81/ladder_r1.py 4)
if grep -q "GLADDER k 6 n 36 steps 177 T-values 64 (2^k = 64) {'X>W': 0, 'X-decrease': 0, 'offer-mismatch': 0, 'non-improving': 0, 'W-decrease': 0}" <<<"$w33" && grep -q "LADDER-R1 k 4 n 10 max-T-rises from all-0 start 4 from any start 4 " <<<"$w33"; then
  echo "box 81 R1: ungated ladder_4 only 4 rises under ranking offers; gated gl_6 64 W-values under R1 (R1-POLY DEAD): PASS"
else
  echo "box 81 R1 check: FAILED"; exit 1
fi
w34=$(cd .. && python3 -I new/box82/ogladder.py 6)
if grep -q "OGLADDER k 6 n 36 odd-gates 22 steps 177 T-values 64 (2^k = 64) cycle-nodes \[0\] {'X>W': 0, 'X-decrease': 0, 'offer-mismatch': 0, 'non-improving': 0, 'W-decrease': 0}" <<<"$w34"; then
  echo "box 82 R2: Odd-gated ogl_6 64 W-values with X a pair valuation (R2-POLY DEAD): PASS"
else
  echo "box 82 R2 check: FAILED"; exit 1
fi
w35=$(cd .. && python3 -I new/box84/waits.py --rand 8 300 1 | head -1; python3 -I new/box84/altcheck.py 10 300 7 | tail -1; python3 -I new/box84/retclass.py red/so/instances/pftheta34_n32.pg | tail -1)
if grep -q "WAITS-RAND n 8 trials 300 seed 1 totals {'viol': 0, 'e0ret': 0, 'deadc': 0, 'reg': 601, 'e0': 85, 'xoncyc': 276}" <<<"$w35" && grep -q "ALTCHECK n 10 trials 300 seed 7 {'alt_reg': 8, 'alt_e0': 8, 'e0_max': 1, 'rise_viol': 0, 'charge_viol': 0," <<<"$w35" && grep -q "RETCLASS n 32 mE 80 runs 1 totals {'REG': 26, 'E0': 0, 'FREE': 16, 'sw': 74, 'bound_viol': 0} maxima {'REG': 3, 'E0': 0, 'FREE': 3, 'F': 34, 'wch': 7}" <<<"$w35"; then
  echo "box 84 WAIT: WAIT-CYCLE' 0 violations, DEADC 0, E0-BOUND / RISE / CHARGE 0 violations, return classes on pftheta34_n32: PASS"
else
  echo "box 84 WAIT check: FAILED"; exit 1
fi
w36=$(cd .. && python3 -I new/box85/freeclass.py red/so/instances/pftheta34_n32.pg | tail -1; python3 -I new/box85/xirise.py new/box52/out/topfix_n6.pg | tail -1)
if grep -q "FREECLASS n 32 mE 80 runs 1 totals {'REG': 26, 'E0': 0, 'FREE': 16, 'sw': 74, 'bound_viol': 0, 'F-LAT': 13, 'F-paidW': 16, 'F-TT': 0, 'F-GAP': 1, 'F-NT': 2}" <<<"$w36" && grep -q "XIRISE n 126 runs 2 {'ret': 80, 'viol_edge': 0, 'viol_rise': 0, 'viol_fr': 0} maxima {'ret': 9, 'xich': 20, 'wch': 20, 'rstar': 0, 'fl': 0, 'F': 34}" <<<"$w36"; then
  echo "box 85 FREE: FREE classes on pftheta34_n32; RET-XIRISE and FREE-RED 0 violations on topfix_n6: PASS"
else
  echo "box 85 FREE check: FAILED"; exit 1
fi
w37=$(cd .. && python3 -I new/box86/rstar.py red/usplit/instances/gate_K16_n197.pg red/usplit/instances/gate_K16_n197.start; python3 -I new/box86/pch.py red/xing/instances/j10_n24.pg)
if grep -q "RSTAR n 197 runs 1 {'gapdev_viol': 0, 'cap_viol': 1, 'blocked': 205} maxima {'rstar': 16, 'dev': 5, 'devch': 16, 'F': 23, 'n': 197}" <<<"$w37" && grep -q "PCH n 24 runs 2 {'lam_viol': 0, 'len_viol': 0, 'xich_viol': 0, 'rstar_viol': 0} maxima {'lch': 0, 'pch': 11, 'len': 1, 'xich': 11, 'rstar': 10, 'n': 24}" <<<"$w37"; then
  echo "box 86 RSTAR: GAP-DEV 0 violations, DEV-CAP DEAD on gate_K16_n197 (R* 16 > 5 deviation edges), RSTAR-PCH 0 violations on j10_n24: PASS"
else
  echo "box 86 RSTAR check: FAILED"; exit 1
fi
w38=$(cd .. && python3 -I new/box87/depth.py red/usplit/instances/gate_K16_n197.pg red/usplit/instances/gate_K16_n197.start; python3 -I new/box87/depth.py new/box54/out/switchbestexp_4.pg)
if grep -q "DEPTH n 197 runs 1 {'prefix_viol': 0} maxima {'depth': 2, 'd1': 1, 'd2': 1, 'd4': 0, 'xich': 15, 'flip': 1}" <<<"$w38" && grep -q "DEPTH n 110 runs 2 {'prefix_viol': 0} maxima {'depth': 15, 'd1': 14, 'd2': 14, 'd4': 13, 'xich': 15, 'flip': 2}" <<<"$w38"; then
  echo "box 87 ARV: PREFIX-MON 0 violations; SHALLOW-k DEAD on switchbestexp_4 (depth 15, DEEP_4 13): PASS"
else
  echo "box 87 ARV check: FAILED"; exit 1
fi
w39=$(cd .. && python3 -I new/box88/release.py red/usplit/instances/gate_K16_n197.pg red/usplit/instances/gate_K16_n197.start; python3 -I new/box88/release.py red/so/instances/pftheta34_n32.pg)
if grep -q "RELEASE n 197 runs 1 {'late': 18, 'ODD': 3, 'EVEN': 15, 'kept': 15} maxima {'F': 23, 'rstar': 16, 'sb': 16, 'dv': 16, 'wch_tr': 23, 'n': 197}" <<<"$w39" && grep -q "RELEASE n 32 runs 1 {'late': 7, 'ODD': 7, 'EVEN': 0, 'kept': 0} maxima {'F': 34, 'rstar': 4, 'sb': 34, 'dv': 34, 'wch_tr': 34, 'n': 32}" <<<"$w39"; then
  echo "box 88 ONEP: release classes (ODD / EVEN) on gate_K16_n197 and pftheta34_n32: PASS"
else
  echo "box 88 ONEP check: FAILED"; exit 1
fi
w40=$(cd .. && python3 -I new/box89/relpe.py si/root/instances/ueonce_n27.pg; STRICT=1 python3 -I new/box89/relpe.py si/root/instances/ueonce_n27.pg; python3 -I new/box89/bipprobe.py red/usplit/instances/gate_K16_n197.pg red/usplit/instances/gate_K16_n197.start)
if grep -q "RELPE n 27 mE 80 runs 1 maxima {'late_edge': 2, 'rstar': 4, 'F': 10, 'frozen_edge': 2} argmax-edge (10, 23)" <<<"$w40" && grep -q "RELPE n 27 mE 80 runs 1 maxima {'late_edge': 0, 'rstar': 0, 'F': 10, 'frozen_edge': 0} argmax-edge None" <<<"$w40" && grep -q "BIPPROBE n 197 {'single_dev': 1, 'no_driver_W': 1, 'lift_before': 1, 'lifter_plain': 1} maxima {'stretch': 3, 'rel': 1, 'nvals': 2, 'depth': 1}" <<<"$w40"; then
  echo "box 89 BIP: non-strict BIP-REL-1 DEAD on ueonce_n27 (2), strict form 0; release anatomy on gate_K16_n197: PASS"
else
  echo "box 89 BIP check: FAILED"; exit 1
fi
w41=$(cd .. && python3 -I new/box90/sbv.py red/so/instances/pftheta34_n32.pg; python3 -I new/box90/relrand.py 8 300 5)
if grep -q "SBV n 32 runs 1 maxima {'sb': 34, 'sbv': 34, 'ret': 18, 'F': 34} sb/n 1.06" <<<"$w41" && grep -q "RELRAND n 8 trials 300 seed 5 max-strict-per-edge 0" <<<"$w41"; then
  echo "box 90 REL: SB-LIN DEAD on pftheta34_n32 (34 > 32); random strict-release search 0: PASS"
else
  echo "box 90 REL check: FAILED"; exit 1
fi
w42=$(cd .. && python3 -I new/box92/xirun.py red/so/instances/pftheta34_n32.pg; python3 -I new/box92/xirun.py red/free/instances/fx_K8_m32.pg red/free/instances/fx_K8_m32.start)
if grep -q "XIRUN n 32 mE 80 runs 1 {'noswitch': 0, 'viol_sw': 0, 'viol_ent': 0, 'viol_xirun': 0} maxima {'F': 34, 'xich': 34, 'bound': 1010, 'ratio': 0.034}" <<<"$w42" && grep -q "XIRUN n 250 mE 151 runs 1 {'noswitch': 0, 'viol_sw': 0, 'viol_ent': 0, 'viol_xirun': 0} maxima {'F': 280, 'xich': 137, 'bound': 2005, 'ratio': 0.14}" <<<"$w42"; then
  echo "box 92 WRUN: XI-RUN |F| <= m_E + sum d_E XICH on pftheta34_n32 and fx_K8_m32: PASS"
else
  echo "box 92 WRUN check: FAILED"; exit 1
fi
w43=$(cd .. && python3 -I hard-families/pgsolver_port.py switchallexp 4 > "$tmp/sae_4.pg" && python3 -I new/box93/swall_hw.py "$tmp/sae_4.pg"; python3 -I new/box93/elimwin.py red/so/instances/pftheta34_n32.pg)
if grep -q "SWALL sae_4.pg n 63 mE 117 iterations 150 bmon_viol 0 elim_viol 0 xi_flat_steps 0 HW 35 count_ok True" <<<"$w43" && grep -q "ELIMWIN n 32 mE 80 runs 1 {'viol_count': 0, 'viol_eq': 0, 'cert': 32, 'ncert': 0} maxima {'F': 34, 'HW': 7, 'revisit': 18, 'xiw': 2}" <<<"$w43"; then
  echo "box 93 ELIM: switch-all on switchallexp_4 keeps BETA-MON / ELIM-ORD-beta with HW 35; ELIM-WIN counting on pftheta34_n32: PASS"
else
  echo "box 93 ELIM check: FAILED"; exit 1
fi
w44=$(cd .. && python3 -I new/box94/kcount.py red/usplit/instances/gate_K64_n581.pg; python3 -I new/box90/sbv.py red/usplit/instances/gate_K64_n581.pg red/usplit/instances/gate_K64_n581.start)
if grep -q "KCOUNT red/usplit/instances/gate_K64_n581.pg n 581 k 5" <<<"$w44" && grep -q "SBV n 581 runs 1 maxima {'sb': 64, 'sbv': 62, 'ret': 61, 'F': 71}" <<<"$w44"; then
  echo "box 94 KO: gate_K64_n581 is in C^5O (prod deg 32) with 64 sbar-changes in one W-run (NO-REPEAT-kO DEAD): PASS"
else
  echo "box 94 KO check: FAILED"; exit 1
fi
w45=$(cd .. && python3 -I hard-families/pgsolver_port.py switchbestexp 3 > "$tmp/sbe_3.pg" && python3 -I new/box95/firstdiv.py "$tmp/sbe_3.pg")
if grep -q "FIRSTDIV sbe_3.pg n 85 N5_iter 41 first_div_GLO 14 first_div_V1 14 N5_tau_changes 3 first_tau_change 13" <<<"$w45"; then
  echo "box 95 HN: N5 = I^glo on switchbestexp_3 until its first tau-change (12 -> 13), split at state 14: PASS"
else
  echo "box 95 HN check: FAILED"; exit 1
fi
w46=$(cd .. && python3 -I hard-families/pgsolver_port.py switchbestexp 3 > "$tmp/sbe_3.pg" && python3 -I new/box96/taustart.py "$tmp/sbe_3.pg" OPT)
if grep -q "TAUSTART sbe_3.pg n 85 OPT iterations 19 tau_changes 0 fallbacks 0 maxWrun 19" <<<"$w46"; then
  echo "box 96 TAU: N5 on switchbestexp_3 with tau_0 = tau_end (tau never moves): 19 iterations, one W-run: PASS"
else
  echo "box 96 TAU check: FAILED"; exit 1
fi
w47=$(cd .. && python3 -I new/box97/orderdet.py n5-exhaustive/instances/n5s_maxph_0.pg; python3 -I new/box97/orderdet.py n5-exhaustive/instances/thetaA_n7.pg n5-exhaustive/instances/thetaA_n7.start; PERRUN=1 python3 -I new/box97/orderdet.py red/usplit/instances/gate_K64_n581.pg red/usplit/instances/gate_K64_n581.start)
if grep -q "ORDDET n5s_maxph_0.pg n 5 STATES 4 WRUNS 1 REFMINX 0 REFMINUX 0 ODU 1 ODA 0 ODR 0" <<<"$w47" && grep -q "ORDDET thetaA_n7.pg n 7 STATES 4 WRUNS 1 REFMINX 0 REFMINUX 0 ODU 0 ODA 0 ODR 0 NRU 1 NRA 1 NRR 1 NRRS 1" <<<"$w47" && grep -q "RUN 0-71 F 71 maxU 6 A 11 OF 5 SBT 64 ORDCH 64 ORD 6" <<<"$w47"; then
  echo "box 97 ORD: ORDER-DET U-form DEAD (n5s_maxph_0), NO-REPEAT DEAD (thetaA_n7), gate_K64: 64 sbar-change transitions over 6 refined orders on |A_F| = 11: PASS"
else
  echo "box 97 ORD check: FAILED"; exit 1
fi
w48=$(cd .. && python3 -I new/box98/retpay.py red/usplit/instances/gate_K64_n581.pg red/usplit/instances/gate_K64_n581.start)
if grep -q "RUN 0-71 F 71 mE 1119 entries 542 FRESH 71 RET 0 NORET 71 ORDRET 59 ORDRET_NR 59 ORDRET_FR 59 FLIPS 64 |A| 11" <<<"$w48"; then
  echo "box 98 RET: gate_K64 W-run has 59 order returns, 64 sbar-changes and no Even-edge return (all paid by fresh entries): PASS"
else
  echo "box 98 RET check: FAILED"; exit 1
fi
w49=$(cd .. && TOP=1 python3 -I new/box99/retcause.py new/box97/inst/sbq2_K8_m16.pg new/box113/inst/sbq2_K8_m16_fixed.start)
if grep -q "RUN 1-152 F 151 returns 450 edges 60 targets 60 max_per_target 8 norise 0 wch_in_window 450" <<<"$w49" && grep -q "ROOT kinds {'FRESH': 450} distinct roots 15 max returns per root 45" <<<"$w49" && grep -q "('FRESH', 4, 66, 17), 45" <<<"$w49"; then
  echo "box 99 QRET: sbq2_K8_m16 returns all rooted at fresh entries, clock vertex 4's ticks root 45 = 3m - 3 each: PASS"
else
  echo "box 99 QRET check: FAILED"; exit 1
fi
w50=$(cd .. && python3 -I new/box99/retcause.py new/box52/out/topfix_n10.pg; TOP=1 python3 -I new/box99/retcause.py new/box97/inst/obs_K12_m24.pg new/box97/inst/obs_K12_m24.start)
if grep -q "EROOT kinds {'FRESH': 252} distinct roots 27 max returns per root 50 chain depth {.*49: 1} max children per node 1 max children per return node 1 mE 651" <<<"$w50" && grep -q "EROOT kinds {'FRESH': 818} distinct roots 25 max returns per root 71 chain depth {0: 301, 1: 506, 2: 11} max children per node 24 max children per return node 2 mE 149" <<<"$w50"; then
  echo "box 100 CASC: EVEN root map total (all FRESH); topfix_n10 root chain depth 49 with width 1 (depth O(1) DEAD); obs_K12_m24 depth 2, return-node width 2: PASS"
else
  echo "box 100 CASC check: FAILED"; exit 1
fi
w51=$(cd .. && TOP=1 python3 -I new/box99/retcause.py new/box97/inst/obs_K12_m24.pg new/box97/inst/obs_K12_m24.start; python3 -I new/box99/retcause.py new/box52/out/topfix_n10.pg; python3 -I new/box99/retcause.py red/so/instances/pftheta34_n32.pg)
if grep -q "PERROOT max returns of one Even X per root 24 (X 247 deg 24) max returns of one edge per root 1 max (returns of X per root)/deg X 1.0" <<<"$w51" && grep -q "PERROOT max returns of one Even X per root 17 (X 193 deg 18) max returns of one edge per root 17" <<<"$w51" && grep -q "PERROOT max returns of one Even X per root 2 (X 3 deg 2) max returns of one edge per root 2 max (returns of X per root)/deg X 1.0 max returns of X per root leaving one target 2" <<<"$w51"; then
  echo "box 101 CEDGE: RET(X; e) <= deg X tight on obs (24/24); once-per-root DEAD (obs), edge-O(1) DEAD (topfix 17), left-target injection DEAD (pftheta34): PASS"
else
  echo "box 101 CEDGE check: FAILED"; exit 1
fi
w52=$(cd .. && XTRACE=3 python3 -I new/box99/retcause.py red/so/instances/pftheta34_n32.pg)
if grep -q "XTRACE return k 11: 3 13 -> 7 (window from 5, first rise 6) root ('FRESH', 7, 20, 6) depth 0" <<<"$w52" && grep -q "XTRACE return k 26: 3 13 -> 7 (window from 13, first rise 15) root ('FRESH', 7, 20, 6) depth 2" <<<"$w52" && grep -q "with one (left, entered) pair 2 max returns of one edge per (root, depth) 1" <<<"$w52"; then
  echo "box 102 OVT: pftheta34_n32 vertex 3 re-enters 7 from 13 twice under root (7 -> 20 @ 6) at depths 0 and 2 (overtake-once DEAD), LEVEL-ONCE holds: PASS"
else
  echo "box 102 OVT check: FAILED"; exit 1
fi
w53=$(cd .. && CHAINS=1 python3 -I new/box99/retcause.py new/box52/out/topfix_n10.pg)
if grep -q "CHAIN chains 252 with a repeated Even vertex 208 max repeats 47 longest 50 distinct 3" <<<"$w53" && grep -q "CHAIN longest \[(193, 58), (194, 57), (192, 56), (193, 55)" <<<"$w53" && grep -q "CHAINSTEP distinct chain nodes 252 with a W-change at q 252 late adoptions (blocked at an earlier state of F) 0" <<<"$w53"; then
  echo "box 103 DEPTH: topfix_n10 root chain of 50 nodes on 3 rotating Even vertices (depth <= distinct vertices DEAD), all W-changing, no late adoption: PASS"
else
  echo "box 103 DEPTH check: FAILED"; exit 1
fi
w54=$(cd .. && XTRACE=7 python3 -I new/box99/retcause.py new/box104/inst/cedge_n32.pg new/box104/inst/cedge_n32.start)
if grep -q "XTRACE return k 22: 7 20 -> 26 (window from 20, first rise 21) root ('FRESH', 20, 7, 9) depth 3" <<<"$w54" && grep -q "SELFFED (X on g's play at state k) returns 3 of 60" <<<"$w54" && grep -q "NONSELF max (returns of X per root)/deg X 2.0" <<<"$w54"; then
  echo "box 104 PING: cedge_n32 vertex 7 returns 4 times (non-self-fed) under root (20 -> 7 @ 9): self-fed split DEAD: PASS"
else
  echo "box 104 PING check: FAILED"; exit 1
fi
w55=$(cd .. && python3 -I new/box105/o1.py red/xing/instances/u23sw64_n32.pg; python3 -I new/box105/o1.py new/box104/inst/cedge_n32.pg new/box104/inst/cedge_n32.start)
if grep -q "O1 u23sw64_n32.pg n 32 W-runs 3 returns 31 O1W 31 O1IN 31 LEAVE_TIE 31 RET_TIE 31 BOTH_TIE 31" <<<"$w55" && grep -q "X 2 leaves 6 at 1, re-enters at 4" <<<"$w55" && grep -q "O1 cedge_n32.pg n 32 W-runs 2 returns 60 O1W 0 O1IN 39 LEAVE_TIE 0" <<<"$w55"; then
  echo "box 105 O1: O1 DEAD on u23sw64_n32 (31 W-tie returns), cedge_n32's ping-pong is non-tie (0 violations): PASS"
else
  echo "box 105 O1 check: FAILED"; exit 1
fi
w56=$(cd .. && python3 -I new/box105/keymon.py red/xing/instances/u23sw64_n32.pg; python3 -I new/box105/o1.py red/xing/instances/u23sw64_n32.pg)
if grep -q "KEYMON u23sw64_n32.pg n 32 intervals 1 KEYUP 0 SWNOTDOWN 0 ODDUP 0 KEYCH 8 SWI 6 TRETI 31 LEN 8" <<<"$w56" && grep -q "TIECLASS \[(('TIE', 'even', 'oneInterval', 'nonown'), 31)\]" <<<"$w56"; then
  echo "box 106 TIE: u23sw64_n32 tie returns all even-cycle-node, inside one W-constant interval; keys never rise, every switch lowers the key: PASS"
else
  echo "box 106 TIE check: FAILED"; exit 1
fi
w57=$(cd .. && python3 -I new/box107/finpot.py red/xing/instances/x31_rx48.pg new/box107/inst/x31_rx48.start; python3 -I new/box107/hier2.py red/xing/instances/x31_rx48.pg new/box107/inst/x31_rx48.start; python3 -I new/box107/hier2.py red/tie/instances/u23sw64_n32.pg red/tie/instances/u23sw64_n32.start; python3 -I new/box107/hier2.py red/so/instances/tog6a_n32.pg)
if grep -q "WT 47 RES 2 XDEC 0 WDEC 0 WOX 0" <<<"$w57" && grep -q "T1 0 T2 30 T3 0 T4 17" <<<"$w57" && grep -qF "HIER x31_rx48.pg n 48 WT 47 WCH 47 DEPTH 2 MONOX 0 MAXSUB1 13 NLEV1 30 NLEV2 17 | NOV 0 DEPTHV 2" <<<"$w57" && grep -qF "HIER u23sw64_n32.pg n 32 WT 13 WCH 5 DEPTH 1 MONOX 0 MAXSUB1 0 NLEV1 5 | NOV 0 DEPTHV 1 NLV1 13" <<<"$w57" && grep -qF "| NOV 1 DEPTHV 1" <<<"$w57"; then
  echo "box 107 FINPOT: W-MON / O-ARENA hold (x31_rx48), BW-alone DEAD (17 T4), hierarchy depth 2 pays them; u23sw64 floor paid by the joint level; NOV 1 on tog6a: PASS"
else
  echo "box 107 FINPOT check: FAILED"; exit 1
fi
w58=$(cd .. && python3 -I new/box108/newedge.py red/xing/instances/x31_rx48.pg new/box107/inst/x31_rx48.start; python3 -I new/box108/carrier.py red/xing/instances/x31_rx48.pg new/box107/inst/x31_rx48.start; python3 -I new/box108/na.py red/so/instances/tog6a_n32.pg)
if grep -qF "NEWEDGE x31_rx48.pg n 48 checked 295 viol 0 overtake_viol 0" <<<"$w58" && grep -qF "CARRIER x31_rx48.pg n 48 B2 2 carriers 49 fix_by_new_edge 49 fix_at_source 49" <<<"$w58" && grep -qF "NA tog6a_n32.pg n 32 mE 97 WT 5 NA 4 NAWC 0 CN 2" <<<"$w58" && grep -qF "BOUNDVIOL 0" <<<"$w58"; then
  echo "box 108 HDEPTH: NEW-EDGE 0 violations (x31_rx48, 295 W-changes), depth-2 carriers released by one new edge at a source event (49/49), ARENA-RED bound holds: PASS"
else
  echo "box 108 HDEPTH check: FAILED"; exit 1
fi
w59=$(cd .. && python3 -I new/box107/hier2.py new/box109/out/hit_b6a_1.pg new/box109/out/hit_b6a_1.start; python3 -I new/box109/climb4.py new/box109/out/hit_n16_1.pg chk 1 0 4)
if grep -qF "HIER hit_b6a_1.pg n 32 WT 38 WCH 38 DEPTH 3 MONOX 0 MAXSUB1 20 NLEV1 18 NLEV2 19 NLEV3 1 | NOV 0 DEPTHV 2" <<<"$w59" && grep -qF "START chk (1, 0, 10) 13" <<<"$w59"; then
  echo "box 109 HSEARCH: HDEPTH DEAD (hit_b6a_1 n 32 h^W 3, joint 2); hit_n16_1 unary-length depth 1: PASS"
else
  echo "box 109 HSEARCH check: FAILED"; exit 1
fi
w60=$(cd .. && python3 -I new/box110/resets2.py new/box110/hd_H40.pg new/box110/hd_H40.start; python3 -I new/box110/resets2.py new/box109/out/hit_b6a_1.pg new/box109/out/hit_b6a_1.start)
if grep -qF "RESETS hd_H40.pg n 122 WT 40 WCT 40 WCH 2420 GOOD 2420 TD 0 RT 0 ROOTRES 0 VIOL 0 VB 0 TDRANK 0 RTRANK 0" <<<"$w60" && grep -qF "RESETS hit_b6a_1.pg n 32 WT 38 WCT 38" <<<"$w60" && grep -qF "RT 34 ROOTRES 34 VIOL 0 VB 0 TDRANK 224 RTRANK 33" <<<"$w60"; then
  echo "box 110 WIDTH: hd_H40 depth 40 with 0 resets; hit_b6a_1 resets all rooted at switches (34/34), RESET-RED and BIT-ALT hold: PASS"
else
  echo "box 110 WIDTH check: FAILED"; exit 1
fi
w61=$(cd .. && python3 -I new/box111/desc.py new/box110/hd_H40.pg new/box110/hd_H40.start; python3 -I new/box111/desc.py new/box109/out/hit_b6a_1.pg new/box109/out/hit_b6a_1.start)
if grep -qF "DESC hd_H40.pg n 122 WT 40 WCH 2420 DESC 0 VIOL 0" <<<"$w61" && grep -qF "DESC hit_b6a_1.pg n 32 WT 38 WCH 113 DESC 24 VIOL 0 DSRC_NOW 4 DSRC_SINCE 14 MAXRUN 3" <<<"$w61"; then
  echo "box 111 STAIR: ASC-RUN holds; hd_H40 descent-free (2420 vertex W-changes, 0 descents); hit_b6a_1 24 descents: PASS"
else
  echo "box 111 STAIR check: FAILED"; exit 1
fi
w62=$(cd .. && python3 -I new/box113/desc5.py new/box113/inst/w_re3_1.pg new/box113/inst/w_re3_1.start; python3 -I new/box113/desc5.py new/box109/out/hit_b6a_1.pg new/box109/out/hit_b6a_1.start; python3 -I new/box113/desc5.py red/n5inj/instances/frz32.pg red/n5inj/instances/frz32.start; python3 -I new/box113/desc5.py red/h3/instances/lcount2_n23.pg red/h3/instances/lcount2_n23.start; python3 -I new/box113/desc5.py new/box113/inst/cp_K4.pg new/box113/inst/cp_K4.start)
if [[ $(grep -c "ONVIOL 0 " <<<"$w62") == 5 && $(grep -c "NFVIOL 0 " <<<"$w62") == 5 && $(grep -c "DMISS 0 " <<<"$w62") == 5 && $(grep -c "ROOTMISS 0 " <<<"$w62") == 5 && $(grep -c "WITVIOL_S 0 " <<<"$w62") == 5 ]] && grep -qF "DESC5 frz32.pg n 32 NFSW 44 NFVIOL 0 ORIGCH 44 ONVIOL 0 RD_K1 21 RD_NEWNOTFUEL 0 RD_OLDEDGE 3 RD_NEW 18 RD_FUEL 18" <<<"$w62" && grep -qF "DESC5 lcount2_n23.pg n 23 NFSW 5 NFVIOL 0 ORIGCH 4 ONVIOL 0 RD_K1 1 RD_NEWNOTFUEL 0 RD_OLDEDGE 0 RD_NEW 1 RD_FUEL 1 MAXRD_V 1 MAXRD_PAIR 1 DR 1 DT_ 1 DS 1" <<<"$w62" && grep -qF "DESC5 cp_K4.pg n 192 NFSW 3177 NFVIOL 0 ORIGCH 3177 ONVIOL 0 RD_K1 388" <<<"$w62" && grep -qF "DESC 388 SW 116 DESC_S 388" <<<"$w62" && grep -qF "DR 11 DT_ 0 DS 2 DMISS 0" <<<"$w62" && grep -qF "DR 17 DT_ 0 DS 1 DMISS 0" <<<"$w62"; then
  echo "box 113 DESCSTAR: SW-WIT, DESC-ROOT, ORIGIN-NEW, NEW-FUEL hold on 5 pins; frz32 3 old-edge relay root descents; lcount2 T-type 1; cp_K4 switch-site U not passive-proof (388): PASS"
else
  echo "box 113 DESCSTAR check: FAILED"; exit 1
fi
w63=$(cd .. && python3 -I new/box115/abl.py new/box115/inst/switchallexp_3.pg SI 3000; python3 -I new/box115/abl.py new/box115/inst/switchallexp_3.pg ARSB 3000; python3 -I new/box115/abl.py new/box115/inst/switchallexp_3.pg SAT 3000; python3 -I new/box115/swx.py new/box115/inst/switchallexp_3.pg new/box115/inst/switchallexp_3.start; python3 -I new/box115/stale.py new/box115/inst/switchallexp_2.pg)
if grep -qF "ABL switchallexp_3.pg SI n 49 iters 70 evenswitches 433 taumoves 0 MAXENT 17 (43, 46) MAXFR 8 (19, 17)" <<<"$w63" && grep -qF "ABL switchallexp_3.pg ARSB n 49 iters 8 " <<<"$w63" && grep -qF "MAXFR 1 (1, 5)" <<<"$w63" && grep -qF "ABL switchallexp_3.pg SAT n 49 iters 70 evenswitches 433 taumoves 3" <<<"$w63" && grep -qF "SWX switchallexp_3.pg N5 n 49 iters 7 fallbacks 0 tauchg 3 wruns 1 wlongest 3" <<<"$w63" && grep -qF "steps 30 moves 138 stale 37 stale_at_s 0" <<<"$w63" && [ "$(sha1sum box115/inst/switchallexp_3.pg | cut -d' ' -f1)" = "3ad1b30a06c0ab02c0dbdd9949866aed96d87cca" ]; then
  echo "box 115 SWX: switchallexp_3 SI 70 iters / pair fuel 8, ARSB 8 / 1, SAT 70 / 8, N5 7 iters one W-run; SI stale moves 37 (N 2): PASS"
else
  echo "box 115 SWX check: FAILED"; exit 1
fi
w64=$(cd .. && python3 -I new/box115/taumv.py new/box115/inst/switchbestexp_3.pg; python3 -I new/box116/tauc.py new/box115/inst/switchbestexp_3.pg new/box115/inst/switchbestexp_3.start; python3 -I new/box115/abl.py new/box115/inst/switchbestexp_3.pg TBR 5000)
if grep -qF "k 12 |Is| 17 |It| 1 fb 0 moves h2:e2->m2" <<<"$w64" && grep -qF "k 14 |Is| 16 |It| 1 fb 0 moves h0:e0->m0" <<<"$w64" && grep -qF "TAUC switchbestexp_3.pg n 85 ITERS 41 TCH 3 OSW 3 ORET 0" <<<"$w64" && grep -qF "ODDREPLY TBR tau changes 11 returns 8" <<<"$w64" && [ "$(sha1sum box115/inst/switchbestexp_3.pg | cut -d' ' -f1)" = "e1cd8f136e0583a1b679b477b9120163ba7b27c8" ]; then
  echo "box 116 TAU: switchbestexp_3 N5 tau moves 3 (h2, h1, h0 escape once, 0 returns); TBR's Odd reply returns 8 times: PASS"
else
  echo "box 116 TAU check: FAILED"; exit 1
fi
w65=$(cd .. && python3 -I new/box116/carry.py red/seg/instances/s3quad_K8_m30.pg new/box116/inst/s3quad_K8_m30_default.start)
if grep -qF "CARRY s3quad_K8_m30.pg n 479 iters 264 maxRE 7 ORET 0 TCH 0 FB 0 ES 0 V1 1 V2 1" <<<"$w65" && grep -qF "R3 7.000 (189, 476)" <<<"$w65"; then
  echo "box 116b CARRY-ODD: DEAD at constant 1 on s3quad_K8_m30 (7 re-entries, no Odd return, no source event, W(476) constant): PASS"
else
  echo "box 116b CARRY check: FAILED"; exit 1
fi
w66=$(cd .. && python3 -I new/box117/squeeze.py new/box115/inst/switchbestexp_2.pg N5; python3 -I new/box117/squeeze.py new/box115/inst/switchbestexp_2.pg TBR)
if grep -qF "SQZ switchbestexp_2.pg N5 n 60 iters 32 SANDV 0 LODROP 0 HIRISE 0 UNSET 0 set0 4 setK 60 growths 14 maxgap 16" <<<"$w66" && grep -qF "SQZ switchbestexp_2.pg TBR n 60 iters 53 SANDV 0 LODROP 0 HIRISE 2 UNSET 3 " <<<"$w66"; then
  echo "box 117 SQUEEZE: switchbestexp_2 N5 interval never widens (HIRISE 0, UNSET 0, settle gap 16); TBR widens (HIRISE 2, UNSET 3): PASS"
else
  echo "box 117 SQUEEZE check: FAILED"; exit 1
fi
w67=$(cd .. && python3 -I new/box118/gate.py new/box113/inst/cp_K4.pg new/box113/inst/cp_K4.start; python3 -I new/box118/gate.py new/box115/inst/switchbestexp_2.pg -)
if grep -qF "GATE cp_K4.pg n 192 iters 44 stretches 1 climbsteps 44 fb 0 flat 0 gated 43 " <<<"$w67" && grep -qF "onep 2 maxratio 22.0 INC 43 maxConsistentWindow 1" <<<"$w67" && grep -qF "onep 16 maxratio 1.1 INC 6 maxConsistentWindow 12" <<<"$w67"; then
  echo "box 118 GATE: cp_K4 one tau-stretch of 44, ungated one-player climb 2, INC 43; switchbestexp_2 INC 6, stretch 18 vs one-player 16: PASS"
else
  echo "box 118 GATE check: FAILED"; exit 1
fi
w68=$(cd .. && python3 -I new/box120/inphase.py n5-epoch/instances/lend107_n32.pg n5-epoch/instances/lend107_n32.start)
if grep -qF "INPHASE lend107_n32.pg n 32 K 112 maxFirst 107 maxInPhase 106 at (2, 107)" <<<"$w68"; then
  echo "box 120 fixes GATE-L1: lend107_n32 one lambda_W-phase of 106 W-changing in-phase transitions (107 by first state): PASS"
else
  echo "box 120 GATE-L1 check: FAILED"; exit 1
fi
w69=$(cd .. && python3 -I new/box121/brtree.py new/box113/inst/cp_K4.pg new/box113/inst/cp_K4.start; python3 -I new/box121/twofix.py new/box113/inst/cp_K4.pg new/box113/inst/cp_K4.start)
if grep -qF "XIN_OLD 4029/4029 (path only 4029) FF 43 IN_OLD 43 IN_NEW 43 PHL up/dn 39/5 PDEP up/dn 36/4" <<<"$w69" && grep -qF "TWOFIX cp_K4.pg n 192 K 44 windows 1 inwin 43 | longest [0, 43] L 43 ODIFF 16 SB 2 SBSTEP 1" <<<"$w69"; then
  echo "box 121 BRTREE: cp_K4 PLAY-CONTAIN 4029/4029, PHL falls 5 times (potential DEAD); one TWO-FIX window of 43 vs switch-best 2: PASS"
else
  echo "box 121 BRTREE check: FAILED"; exit 1
fi
w70=$(cd .. && python3 -I new/box122/windows.py n5-exhaustive/instances/b5_os_n40.pg new/box121/inst/b5_os_n40_default.start 4)
if grep -qF "WIN b5_os_n40.pg n 40 K 81 [0, 77] L 77 ODIFF 1 FB 9 SB 7 SBSTEP 9 MAXSEG 17 MAXPH 17 PHNF 17 FLATNF 0 LAMNF 7 O [(7, 2, 7)]" <<<"$w70"; then
  echo "box 122 TWOFIX: b5_os_n40 ODIFF 1 window 77 = 9 fallbacks + runs <= 17, PHNF 17 <= n - 1 (TF-PH): PASS"
else
  echo "box 122 TWOFIX check: FAILED"; exit 1
fi
w71=$(cd .. && python3 -I new/box123/fbcount.py red/n5inj/instances/frz24.pg red/n5inj/instances/frz24.start)
if grep -qF "FBW frz24.pg n 24 [13, 30] L 17 ODIFF 1 FB 2 REPW 0 REPWF 0 PEAKMON 1 TROUGHMON 1 SW 9 SWD 9 WDROP 6 WDROPD 6 GAPF [18, 18] NOTDESC 1 NOTDESC_NOXO 1 XOBETWEEN 0 XOALL 1" <<<"$w71"; then
  echo "box 123 FBCOUNT: frz24 gap 18 -> 18 between fallbacks with no Xi(o) change (GAP-DESC DEAD); W-drops all in D: PASS"
else
  echo "box 123 FBCOUNT check: FAILED"; exit 1
fi
w72=$(cd .. && python3 -I new/box124/lemmap.py red/n5inj/instances/frz24.pg red/n5inj/instances/frz24.start; python3 -I new/box124/lemmap.py red/n5inj/instances/block_bk20.pg -)
if grep -qF "LEMMAP frz24.pg n 24 K 39 pieces 5 longest 7 checks 335 viol 12 BLK 8 NOTBLK 4 INX 4 INZ 8" <<<"$w72" && grep -qF "LEMMAP block_bk20.pg n 24 K 27 pieces 3 longest 9 checks 303 viol 0 " <<<"$w72"; then
  echo "box 124 LEMMAP: Lemma P invariant fails in TWO-FIX pieces with D nonempty (frz24 12 / 335), holds with D empty (block_bk20 0 / 303): PASS"
else
  echo "box 124 LEMMAP check: FAILED"; exit 1
fi
w73=$(cd .. && python3 -I new/box125/chain.py new/box116/inst/fbA_K4_m8_m8.pg new/box116/inst/fbA_K4_m8_m8_fixed.start)
if grep -qF "CHAIN fbA_K4_m8_m8.pg n 136 K 44 stretches 1 T 44 WIN 34 SBC 33 FBX 0 VMOVES 72 VAL 72 TIE 0 TOW 44 AWAY 28 SIDE 0 DSW 72 MOVERS 23 MAXFLIP 8 " <<<"$w73"; then
  echo "box 125 CHAIN: fbA_K4 one tau-stretch of 44 = 34 TWO-FIX windows, 33 sbar-changes all Xi-changes at Odd vertices (SBC-XI): PASS"
else
  echo "box 125 CHAIN check: FAILED"; exit 1
fi
w74=$(cd .. && python3 -I new/box126/oddxi.py new/box113/inst/cp_K4.pg new/box113/inst/cp_K4.start 1)
if grep -qF "ODDXI cp_K4.pg n 192 K 44 XCHodd 329 MINRISE 329 SBMOVE 16 MOVES 16 OLDROSE 16 FLATMOVES 0 END sw 329 cyc 0 stop 0 MAXCHAIN 4" <<<"$w74"; then
  echo "box 126 ODDXI: cp_K4 every Odd Xi-change is a minimiser rise charged down the play to an Even switch (329 / 329): PASS"
else
  echo "box 126 ODDXI check: FAILED"; exit 1
fi
w75=$(cd .. && python3 -I new/box127/expir.py n5-epoch/instances/nep92_n40.pg n5-epoch/instances/nep92_n40.start)
if grep -qF "EXP nep92_n40.pg n 40 K 98 WRUNS 9 MAXRUN 14 SRCS 360 XCH 964 BLK 964 MAXXCH 11 MAXBLK 11 RET 0 AF 50 AFREV 0 SRCVIOL 27 QOFF 2 Q2OFF 50 NEITHER 0" <<<"$w75"; then
  echo "box 127 PARAM: nep92_n40 expiration (alternation-free) property fails inside W-runs (50 violations, all availability), no path-part returns: PASS"
else
  echo "box 127 PARAM check: FAILED"; exit 1
fi
w76=$(cd .. && python3 -I new/box128/pcount.py new/box52/out/topfix_n10.pg new/box128/topfix_n10_default.start; python3 -I new/box128/witness.py new/box52/out/topfix_n10.pg new/box128/topfix_n10_default.start | head -1; python3 -I new/box128/pcount.py n5-exhaustive/instances/n4all_maxph_0.pg -)
if grep -qF "PCOUNT topfix_n10.pg n 210 K 64 WIN 3 STRETCHES 3 MOVES 756 STRICT 756 FLAT 0 WORSE 0 FIRST 212 SAME 0 SAMEZCNR 0 PVIOL 0 DIFF 544 RET 252 STRICTDIFF 544 STRICTRET 252 STRICTSAME_NOZC 0 STRICTSAME_NONR 0 BVIOL 0 MAXSTRICT 36 MAXDIFF 35 MAXRET 18 LAMXI 70 NBSUM 366 MAXWINSTRICT 646 CORNER 9 WORSE_NOCORNER 0 STATVIOL 0 STATCORNER 0 PAID_XI 544 PAID_WONLY 0 LEADVIOL 24 MAXEXCESS 16 MAXMULTI 1 MULTI2 0 DEGVIOL 0 MAXRATIO 1.89" <<<"$w76" && grep -qF "WITNESS topfix_n10.pg n 210 window [6,64] stretch [6,64] h 192 (prio 67) STRICT 36 LC 20 EXCESS 16" <<<"$w76" && grep -qF "WORSE 1 " <<<"$w76" && grep -qF "CORNER 2 WORSE_NOCORNER 0 STATVIOL 0" <<<"$w76"; then
  echo "box 128 PCOUNT: topfix_n10 h 192 36 W-strict moves > per-h (#X)(#ZC) bound 20 (hub re-entries); STATIC-TIE 0 violations; WORSE only at the comparison corner: PASS"
else
  echo "box 128 PCOUNT check: FAILED"; exit 1
fi
w77=$(cd .. && python3 -I new/box129/gatechg.py new/box52/out/topfix_n10.pg new/box128/topfix_n10_default.start)
if grep -qF "GATECHG topfix_n10.pg n 210 ODIFF0 WIN 2 STRICT 667 CHARGED 543 PAYXI 300 PAYW 243 CYC 0 P_FIRST 66 P_STRICT 477 P_FLAT 0 P_WEAK 0 SELFPAY 0 DEPTH 52 FANIN 9 MAXSTRICT_H 36 MAXSCC 3 REVISIT 225" <<<"$w77"; then
  echo "box 129 GATECHG: topfix_n10 ODIFF-0 charge chains depth 52, fan-in 9, mutual-payment SCC 3 (gate depth undefined): PASS"
else
  echo "box 129 GATECHG check: FAILED"; exit 1
fi
w78=$(cd .. && python3 -I new/box130/flatcnt.py red/xing/instances/u2flat73_n32.pg new/box130/u2flat73_n32_default.start; python3 -I new/box130/flatcnt.py red/so/instances/tog6a_n32.pg -)
if grep -qxF "FLATCNT u2flat73_n32.pg n 32 ODIFF1+ WIN 1 MOVES 75 STRICT 2 FLAT 73 WEAK 0 CORNER 0 FLATTRANS 0 FL 7 ONLYFLAT_VIOL 0 FLOPT_VIOL 0 FLTIGHT_VIOL 0 XIRISE_VIOL 0 MAXFLRUN 3 MAXFLWIN 73 FLATFIRST 49 ODIFF0FLAT 0 XIRISE_CYC 0 FLTIGHT_CYC 0 FL0_NONCORNER 0" <<<"$w78" && grep -qxF "FLATCNT tog6a_n32.pg n 32 ODIFF0 WIN 1 MOVES 25 STRICT 23 FLAT 1 WEAK 1 CORNER 6 FLATTRANS 0 FL 1 ONLYFLAT_VIOL 0 FLOPT_VIOL 0 FLTIGHT_VIOL 0 XIRISE_VIOL 0 MAXFLRUN 1 MAXFLWIN 1 FLATFIRST 1 ODIFF0FLAT 1 XIRISE_CYC 2 FLTIGHT_CYC 0 FL0_NONCORNER 0" <<<"$w78"; then
  echo "box 130 FLATCNT: u2flat73_n32 73 flat moves, 7 FL transitions (ODIFF >= 1); tog6a ODIFF-0 FL transition only at corner movers: PASS"
else
  echo "box 130 FLATCNT check: FAILED"; exit 1
fi
w79=$(cd .. && python3 -I new/box131/canon.py red/xing/instances/u2flat73_n32.pg -)
if grep -qxF "CANON u2flat73_n32.pg n 32 K 16 DEC_EVEN 51 FLDEC_EVEN 51 FLKEYDEC 73 FLKEYEQ 0 FLKEYEQ_CYCNODE 0 FLMOVES_EVEN 73 KEYMIN_EVEN 74 KEYTIES_EVEN 74 MAXFLMV_EVEN 2 MINIDX_EVEN 51 MOVETIE_EVEN 73 TIES_EVEN 74" <<<"$w79"; then
  echo "box 131 CANON: u2flat73_n32 every even-cycle-node tie broken by the lex-smallest BFS key (74 / 74), every FL move lowers the mover's key (73 / 73), index not monotone (51 / 73): PASS"
else
  echo "box 131 CANON check: FAILED"; exit 1
fi
w80=$(cd .. && python3 -I new/box132/anchor.py red/xing/instances/u23sw64_n32.pg new/box132/u23sw64_n32_default.start; python3 -I new/box132/anchor.py red/kw/instances/cw11_n24.pg new/box132/cw11_n24_default.start)
if grep -qxF "ANCHOR u23sw64_n32.pg n 32 RUNS 1 FL 8 EPOCHS 1 GCH 0 VIOL 0 LVLVIOL 0 CMOVES 0 CMNORISE 0 CMLATE 0 MAXEP 8 EPVIOL 0 BOUNDVIOL 0 XIB 0 SBB 0 CYB 0 MAXLEN 8 CMXICH 0" <<<"$w80" && grep -qxF "ANCHOR cw11_n24.pg n 24 RUNS 4 FL 7 EPOCHS 7 GCH 3 VIOL 0 LVLVIOL 0 CMOVES 7 CMNORISE 0 CMLATE 0 MAXEP 1 EPVIOL 0 BOUNDVIOL 0 XIB 0 SBB 0 CYB 3 MAXLEN 3 CMXICH 7" <<<"$w80"; then
  echo "box 132 ANCHOR: u23sw64_n32 FL run of 8 = one epoch, level timing holds; cw11_n24 3 gating changes (Xi at a W-cycle node), 7 cycle-node moves: PASS"
else
  echo "box 132 ANCHOR check: FAILED"; exit 1
fi
w81=$(cd .. && python3 -I new/box133/odxi.py new/box133/odxi_n37.pg new/box133/odxi_n37.start)
if grep -qxF "ODXI odxi_n37.pg n 37 RUNS 1 FL 8 XICH_ODIFF 5 GATEREL 1 EX [(1, 6, 35, 34, 33, 33)]" <<<"$w81"; then
  echo "box 133 ODXI: odxi_n37 Xi at ODIFF gate 33 changes 5 times inside the FL run [1, 9] and releases the FL move 35: 34 -> 33 at 5 -> 6: PASS"
else
  echo "box 133 ODXI check: FAILED"; exit 1
fi
w82=$(cd .. && python3 -I new/box132/anchor.py new/box134/inst/odxi_many_n32.pg new/box134/inst/odxi_many_n32.start; python3 -I new/box133/odxi.py new/box134/inst/odxi_min_n12.pg new/box134/inst/odxi_min_n12.start)
if grep -qxF "ANCHOR odxi_many_n32.pg n 32 RUNS 3 FL 8 EPOCHS 7 GCH 4 VIOL 0 LVLVIOL 0 CMOVES 0 CMNORISE 0 CMLATE 0 MAXEP 2 EPVIOL 0 BOUNDVIOL 0 XIB 4 SBB 0 CYB 0 MAXLEN 3 CMXICH 0" <<<"$w82" && grep -qxF "ODXI odxi_min_n12.pg n 12 RUNS 1 FL 1 XICH_ODIFF 1 GATEREL 0" <<<"$w82"; then
  echo "box 134 P-N5-ANCHOR pins: odxi_many_n32 (R179) 8 FL transitions, 4 gating changes, FL-ANCHOR items hold; odxi_min_n12 one ODIFF Xi-change in its FL run: PASS"
else
  echo "box 134 P-N5-ANCHOR pins check: FAILED"; exit 1
fi
w83=$(cd .. && python3 -I new/box134/cmpw.py new/box133/odxi_n37.pg new/box133/odxi_n37.start)
if grep -qxF "CMPW odxi_n37.pg n 37 MOVES 65 FLIPS 45 PREFIX 44 CROSS 1 INPREF 0 CYCNODE 0 SAMEW 0 NONFLIP 5" <<<"$w83"; then
  echo "box 134 CMPW: odxi_n37 order flips behind FL moves 44 PREFIX + 1 CROSS, SAMEW 0 (Lemma COMPARE-W): PASS"
else
  echo "box 134 CMPW check: FAILED"; exit 1
fi
w84=$(cd .. && STRETCH=1 python3 -I new/box135/dmerge.py new/box134/inst/odxi_many_n32.pg new/box134/inst/odxi_many_n32.start; STRETCH=1 python3 -I new/box135/dmerge.py red/xing/instances/u23sw64_n32.pg new/box132/u23sw64_n32_default.start)
if grep -qxF "DMERGES odxi_many_n32.pg n 32 RUNS 3 FL 8 ACYC 1 CYC 2 HMAX 8 CASCVIOL 0 SEGEDGES 274 MAXL 3 SELFL 7 CNMOV 0" <<<"$w84" && grep -qxF "DMERGES u23sw64_n32.pg n 32 RUNS 1 FL 8 ACYC 1 CYC 0 HMAX 9 CASCVIOL 0 SEGEDGES 305 MAXL 8 SELFL 0 CNMOV 0" <<<"$w84"; then
  echo "box 135 DMERGE: u23sw64_n32 stretch D' acyclic, height 9, FL 8 (CASC-M); odxi_many_n32 2 cyclic stretches via 7 self-edges: PASS"
else
  echo "box 135 DMERGE check: FAILED"; exit 1
fi
w85=$(cd .. && DOM=1 STRETCH=1 python3 -I new/box136/dmerge2.py new/box134/inst/odxi_many_n32.pg new/box134/inst/odxi_many_n32.start)
if grep -qxF "DMERGE2SD odxi_many_n32.pg n 32 RUNS 3 FL 8 ACYC 3 CYC 0 HMAX 8 CASCVIOL 0 SEGEDGES 255 MAXL 3 SELFL 0 CNMOV 0 DOMCUT 117" <<<"$w85"; then
  echo "box 136 DMERGE2: odxi_many_n32 all 3 stretches D''-acyclic under z-world + DOM (D' had 2 cyclic), CASC-M'' holds: PASS"
else
  echo "box 136 DMERGE2 check: FAILED"; exit 1
fi
w86=$(cd .. && python3 -I new/box137/rel.py new/box137/ret2_n37.pg new/box137/ret2_n37_default.start; python3 -I new/box137/rel.py new/box137/cwmov2_n57.pg new/box137/cwmov2_n57_default.start; python3 -I new/box132/anchor.py new/box137/ret2_n37.pg new/box137/ret2_n37_default.start)
if grep -qxF "REL ret2_n37.pg n 37 K 12 RUNS 1 FL 7 CEILVIOL 0 SATDEC 0 SATGAIN 0 MOVERS 74 FROZVIOL 0 SYNC 98 SYNCVIOL 0 CW 0 CWVIOL 0 RET 44 RETMAX 2 MOVMAX 6 CHAINVIOL 0 CNMOV 0 CWMOV 0 WWMOV 74 DEFVIOL 0" <<<"$w86" && grep -qxF "ANCHOR ret2_n37.pg n 37 RUNS 1 FL 7 EPOCHS 1 GCH 0 VIOL 0 LVLVIOL 0 CMOVES 0 CMNORISE 0 CMLATE 0 MAXEP 7 EPVIOL 0 BOUNDVIOL 0 XIB 0 SBB 0 CYB 0 MAXLEN 7 CMXICH 0" <<<"$w86" && grep -qxF "REL cwmov2_n57.pg n 57 K 15 RUNS 2 FL 6 CEILVIOL 0 SATDEC 0 SATGAIN 2 MOVERS 32 FROZVIOL 0 SYNC 113 SYNCVIOL 0 CW 102 CWVIOL 0 RET 14 RETMAX 1 MOVMAX 4 CHAINVIOL 0 CNMOV 0 CWMOV 2 WWMOV 30 DEFVIOL 0" <<<"$w86"; then
  echo "box 137 REL: ret2_n37 one FL run = one epoch (GCH 0), an option re-entered twice (RET-1 DEAD), box 137 lemma checks 0; cwmov2_n57 2 c-world FL moves, DEFICIT holds: PASS"
else
  echo "box 137 REL check: FAILED"; exit 1
fi
w87=$(cd .. && python3 -I new/box138/dmerge3.py new/box138/sbmany_n57.pg new/box138/sbmany_n57_default.start; python3 -I new/box138/dmerge3.py new/box133/odxi_n37.pg new/box133/odxi_n37.start)
if grep -qxF "DMERGE3 sbmany_n57.pg n 57 SSTRETCHES 1 FL 3 ACYC 1 CYC 0 EHEIGHT 9 CASCVIOL 0 EDGES 99 MAXL 3 CNMOV 1 SBIN 95 TIES 0 ODDNODES 8 SBSTR 1 SBACYC 1 SBFL 3" <<<"$w87" && grep -qxF "DMERGE3 odxi_n37.pg n 37 SSTRETCHES 1 FL 8 ACYC 1 CYC 0 EHEIGHT 9 CASCVIOL 0 EDGES 372 MAXL 8 CNMOV 0 SBIN 0 TIES 0 ODDNODES 54 SBSTR 0 SBACYC 0 SBFL 0" <<<"$w87"; then
  echo "box 138 GATE: sbmany_n57 95 sbar changes inside one acyclic S-stretch of 3 transitions (CASC-M3); odxi_n37 one S-stretch, Even-height 9: PASS"
else
  echo "box 138 GATE check: FAILED"; exit 1
fi
w88=$(cd .. && python3 -I new/box139/paths.py new/box139/genomes/big_d4_k3_W3.json new/box139/genomes/grow_top_N24.json)
if grep -qxF "PATHS big_d4_k3_W3.json N 12 STEPS 32 STOP stuck MOVES 57 MOVMAX 10 VXMAX 833 VWMAX 81 CURVIOL 0 KEYVIOL 0 BOUNDVIOL 0 SLACK 1.0000" <<<"$w88" && grep -qxF "PATHS grow_top_N24.json N 24 STEPS 64 STOP stuck MOVES 119 MOVMAX 10 VXMAX 8799 VWMAX 6561 CURVIOL 0 KEYVIOL 0 BOUNDVIOL 0 SLACK 1.0000" <<<"$w88"; then
  echo "box 139 PATHS: IDEAL-ACYC champions big_d4 / grow_top_N24: value and key monotone at every step, moves <= min(VX, VW) - 1: PASS"
else
  echo "box 139 PATHS check: FAILED"; exit 1
fi
w89=$(cd .. && python3 -I new/box140/alt.py new/box140/out/up_d5.json new/box140/out/up_d6.json)
if grep -qxF "ALT up_d5.json N 10 STEPS 11 LADDER True ALTVIOL 0 TOWARDVIOL 0 LFVIOL 0 MOVES [2, 5, 7, 4, 2] LFLIPS [2, 5, 5, 3, 2]" <<<"$w89" && grep -qxF "ALT up_d6.json N 12 STEPS 13 LADDER True ALTVIOL 0 TOWARDVIOL 0 LFVIOL 0 MOVES [2, 4, 7, 7, 3, 2] LFLIPS [2, 3, 7, 6, 6, 5]" <<<"$w89"; then
  echo "box 140 JOINT: UP-LADDER climb champions d 5 / 6 (FL 11 / 13): ALTERNATION, TOWARD-L, L-ACCOUNT hold; moves peak mid-ladder: PASS"
else
  echo "box 140 JOINT check: FAILED"; exit 1
fi
w90=$(cd .. && python3 -I new/box140/alt.py new/box141/out/up_d8_s8.json)
if grep -qxF "ALT up_d8_s8.json N 16 STEPS 19 LADDER True ALTVIOL 0 TOWARDVIOL 0 LFVIOL 0 MOVES [2, 6, 8, 9, 8, 4, 4, 2] LFLIPS [2, 6, 8, 9, 7, 6, 6, 5]" <<<"$w90"; then
  echo "box 141 UPLIN: UP-LADDER d 8 champion FL 19 (linear), ALTERNATION / TOWARD-L / L-ACCOUNT hold: PASS"
else
  echo "box 141 UPLIN check: FAILED"; exit 1
fi
w91=$(cd .. && python3 -I new/box142/lag.py new/box142/lag_min_d2.json new/box141/out/up_d8_s8.json)
if grep -qxF "LAG lag_min_d2.json STEPS 2 STOP opt LAGEVENTS 1 LAGMAX 1 DOUBLE 0 DELAY [0, 1] LFLIPS [1, 1] DELVIOL 0 EX (1, 1, [2, 3], 2, 1)" <<<"$w91" && grep -qxF "LAG up_d8_s8.json STEPS 19 STOP stuck LAGEVENTS 2 LAGMAX 1 DOUBLE 8 DELAY [0, 3, 3, 4, 2, 1, 1, 0] LFLIPS [2, 6, 8, 9, 7, 6, 6, 5] DELVIOL 0 EX (1, 11, [2, 3], 11, 12)" <<<"$w91"; then
  echo "box 142 LAG: NO-LAG dead (lag_min_d2, sibling Xi-read); DELAY-CHARGE holds on up_d8_s8: PASS"
else
  echo "box 142 LAG check: FAILED"; exit 1
fi
w92=$(cd .. && python3 -I new/box143/cause.py new/box143/inst/x3_L8.json new/box143/out/dc_d12.json; python3 -I new/box143/rerise.py new/box143/inst/x3_L8.json)
if grep -qxF "CAUSE x3_L8.json d 3 STEPS 8 STOP stuck SUMDELAY 5 CELEMVIOL 0 LEAST {'DEL': 4, 'PRE': 3, 'OTHER': 0, 'CAR': 0} PRE 4 STEPBOUND 9 NOCAUSE 0 CAUSECLS {'DEL': 1, 'CAR': 3, 'PRE': 1} CAUSELEVDIFF {-2: 1, -1: 1, 0: 2, 1: 1} MOVES 13 BFLIPS 13" <<<"$w92" && grep -qxF "CAUSE dc_d12.json d 12 STEPS 26 STOP stuck SUMDELAY 63 CELEMVIOL 0 LEAST {'DEL': 23, 'PRE': 2, 'OTHER': 0, 'CAR': 0} PRE 7 STEPBOUND 31 NOCAUSE 0 CAUSECLS {'DEL': 42, 'CAR': 13, 'PRE': 8} CAUSELEVDIFF {-10: 4, -9: 2, -8: 2, -6: 2, -5: 1, -4: 4, -3: 3, -2: 4, -1: 6, 0: 6, 1: 3, 2: 9, 3: 5, 4: 4, 5: 3, 6: 3, 7: 2} MOVES 82 BFLIPS 89" <<<"$w92" && grep -qxF "RERISE x3_L8.json d 3 STEPS 8 PAIRS 12 RERISEVIOL 4 STRICTVIOL 5 MAXRISES 5" <<<"$w92"; then
  echo "box 143 DELAY: C-ELEM and STEP-DELAY hold on R188 pin x3_L8 and the d 12 Sum-DELAY champion (63 delays, 26 steps); literal re-rise hint dead on x3_L8: PASS"
else
  echo "box 143 DELAY check: FAILED"; exit 1
fi
w93=$(cd .. && python3 -I new/box144/merge.py new/box143/inst/x3_L8.json; python3 -I new/box144/chain.py new/box143/inst/x3_L8.json new/box143/out/dc_d12.json)
if grep -qxF "MERGE x3_L8.json d 3 STEPS 8 DELSTEPS 4 NOPRE 1 MAXX 2 MAXXK 2 MAXXC 2 MAXC 2 MAXXCK 2 PAIRS 2 CAUSECLS {'CAR': 2, 'DEL': 1} CLEAST 1 SEGLEN 2 KBARHIT 1 SUFHIT 1" <<<"$w93" && grep -qxF "CHAIN x3_L8.json d 3 STEPS 8 DELSTEPS 4 CHAINED 2 UNCHAINED 2 NOCAUSE 0 PIVIOL 0 MAXCHAIN 3 UNCLS {'CAR': 2} UNLEV {1: 2} | ALL: UNCH 3 NOCAUSE 0 PIVIOL 0 MAXBLOCK 3 BOUND N(1+U) 24 OK True" <<<"$w93" && grep -qxF "CHAIN dc_d12.json d 12 STEPS 26 DELSTEPS 23 CHAINED 10 UNCHAINED 13 NOCAUSE 0 PIVIOL 0 MAXCHAIN 7 UNCLS {'DEL': 10, 'CAR': 3} UNLEV {0: 1, 1: 5, 3: 1, 4: 2, 7: 3, 8: 1} | ALL: UNCH 14 NOCAUSE 0 PIVIOL 0 MAXBLOCK 7 BOUND N(1+U) 360 OK True" <<<"$w93"; then
  echo "box 144 MERGE-CHAIN: pre-merge cause premise dead on x3_L8 (NOPRE 1); CHAIN-BACK blocks <= n_E, steps <= n_E (1 + U) on x3_L8 and dc_d12: PASS"
else
  echo "box 144 MERGE-CHAIN check: FAILED"; exit 1
fi
w94=$(cd .. && python3 -I new/box145/thr.py new/box143/inst/x3_L8.json new/box144/inst/nest_d3_L4.json)
if grep -qxF "THR x3_L8.json N 6 STATES 64 IMAGES 30 NONUNATE 2 NONASUM2 3 WITNESS (2, 3, (1, 1, 0, 0, 1, 1), (1, 1, 1, 0, 0, 0))" <<<"$w94" && grep -qxF "THR nest_d3_L4.json N 6 STATES 64 IMAGES 18 NONUNATE 1 NONASUM2 1 WITNESS (5, 0, (0, 1, 1, 1, 0, 1), (0, 1, 0, 1, 1, 0))" <<<"$w94"; then
  echo "box 145 ENERGY: direct threshold cast dead (one-step map not unate on x3_L8 and nest_d3_L4): PASS"
else
  echo "box 145 ENERGY check: FAILED"; exit 1
fi
w95=$(cd .. && python3 -I new/box146/energy.py new/box146/small_d2.json new/box144/inst/lag1.json)
if grep -qxF "ENERGY small_d2.json N 4 STEPS 2 UNCH 0 CH 1 V0D 1 V0U 0 V1D 1 V1U 0 V2D 1 V2U 0 V3D 1 V3U 0 VLEXD 1 VLEXU 0" <<<"$w95" && grep -qxF "ENERGY lag1.json N 6 STEPS 2 UNCH 1 CH 0 V0D 1 V0U 1 V1D 1 V1U 0 V2D 1 V2U 0 V3D 1 V3U 0 VLEXD 0 VLEXU 1" <<<"$w95"; then
  echo "box 146 SPLITE: split-level energy dead (small_d2 chained rise; lag1 unchained non-fall): PASS"
else
  echo "box 146 SPLITE check: FAILED"; exit 1
fi
w96=$(cd .. && python3 -I new/box147/rank.py new/box143/inst/x3_L8.json new/box147/out/rk_d3.json; python3 -I new/box147/stat.py new/box144/inst/lag1.json)
if grep -qxF "RANK x3_L8.json N 6 STEPS 8 U 3 YSTAB 0 ABOVE 0 MAXR_UNCH 2 MAXR_CH 2 MAXR_ALL 3 UNCH_RANKS [1, 1, 2]" <<<"$w96" && grep -qxF "RANK rk_d3.json N 6 STEPS 2 U 1 YSTAB 0 ABOVE 0 MAXR_UNCH 5 MAXR_CH 0 MAXR_ALL 5 UNCH_RANKS [5]" <<<"$w96" && grep -q "^STAT lag1.json N 6 STEPS 2 U 1 CH 0 .* QUOT B:BAD1 UNST:lv1 AGR:lv1 KP:lv1 MRG:BAD1 " <<<"$w96"; then
  echo "box 147 COARSE: DECREMENT holds (YSTAB 0, ABOVE 0); unchained RANK 5 = n - 1 on rk_d3; B and MRG constant across lag1's unchained step: PASS"
else
  echo "box 147 COARSE check: FAILED"; exit 1
fi
w97=$(cd .. && python3 -I new/box148/charge.py new/box144/out/uc_d6.json; python3 -I new/box148/restrict.py new/box143/inst/x3_L8.json new/box144/out/uc_d10.json)
if grep -q "^CHARGE uc_d6.json N 12 STEPS 13 U 9 .* k1: H 6 NOFLIP_ABOVE 4 NOFLIP_FROZ 5 SAMETOP 6 FIRSTFAIL 3 " <<<"$w97" && grep -q "^RESTRICT x3_L8.json N 6 STEPS 8 U 3 INTERVALS 5 PREFIXVIOL 0 " <<<"$w97" && grep -q "^RESTRICT uc_d10.json N 20 STEPS 22 U 17 INTERVALS 4 PREFIXVIOL 0 MAXUNCH_IN 10 " <<<"$w97"; then
  echo "box 148 INTERVAL: per-step key-change charge dead on uc_d6; INTERVAL-RESTRICT prefix holds on x3_L8 and uc_d10: PASS"
else
  echo "box 148 INTERVAL check: FAILED"; exit 1
fi
w98=$(cd .. && python3 -I new/box149/keyflip.py new/box143/inst/x3_L8.json new/box143/out/dc_d12.json)
if grep -qxF "KEYFLIP x3_L8.json N 6 STEPS 8 MOVES 13 KFLIPS 10 VIOL 0" <<<"$w98" && grep -qxF "KEYFLIP dc_d12.json N 24 STEPS 26 MOVES 82 KFLIPS 86 VIOL 0" <<<"$w98"; then
  echo "box 149 KEYFLIP: moves(x) <= 1 + key flips(x) on x3_L8 and dc_d12: PASS"
else
  echo "box 149 KEYFLIP check: FAILED"; exit 1
fi
w99=$(cd .. && python3 -I new/box150/check.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json | tail -1; ALL=1 python3 -I new/box150/check.py new/box150/out/rand/*.json | tail -1; NEG=3 python3 -I new/box150/check.py new/box150/out/rand/*.json | tail -1)
if grep -qxF "TOTAL genomes 46 runs 46 steps 386 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)" <<<"$w99" && grep -qxF "TOTAL genomes 200 runs 75518 steps 93963 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)" <<<"$w99" && grep -q "^TOTAL genomes 200 runs 200 .* XINEW [1-9]" <<<"$w99"; then
  echo "box 150 P-IDEAL-RED: every packet inequality, 0 violations on 46 corpus genomes and 75,518 all-start runs of 200 random genomes; negative control fires: PASS"
else
  echo "box 150 P-IDEAL-RED check: FAILED"; exit 1
fi
if python3 -c "import z3" 2> /dev/null; then
  w100=$(bash box151/run.sh check 2>&1)
  exp100="NEST k 3 E 0 DEG 1 ANTI 0 FREEKP 0 xwake -> sat
NEST k 3 E 0 DEG 0 ANTI 1 FREEKP 0 xwake_anti -> unsat
NEST k 3 E 1 DEG 0 ANTI 1 FREEKP 0 xwake_anti -> unsat
NEST k 2 E 2 DEG 0 ANTI 1 FREEKP 0 xwake_anti -> sat
NEST k 4 E 2 DEG 0 ANTI 1 FREEKP 0 xwake_anti -> unsat
NEST k 3 E 1 DEG 0 ANTI 1 FREEKP 1 xwake_anti -> unsat
NEST k 4 E 2 DEG 0 ANTI 1 FREEKP 1 xwake_anti -> sat"
  if [ "$w100" == "$exp100" ]; then
    echo "box 151 NEST: xwake.py without antisymmetry SAT on bare k 3; with it UNSAT k 3 E 0/1, k 4 E 2, SAT k 2 E 2; gate-free UNSAT k 3 E 1, SAT k 4 E 2: PASS"
  else
    echo "box 151 NEST check: FAILED"; echo "$w100"; exit 1
  fi
else echo "box 151 NEST checks skipped (no z3)"; fi
w101=$(cd .. && python3 -I new/box152/lemcheck.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*_d5_*.json)
if grep -qxF "LEMCHECK runs 50 pairs 92308 PMDIFF 0 SPATH 0 pm_prem 32586 sp_prem 37303" <<<"$w101"; then
  echo "box 152 PMDIFF / STABLE-PATH: 0 violations on 92,308 state pairs of 50 runs (incl. R198/R199 d 5 pins): PASS"
else
  echo "box 152 lemcheck: FAILED"; echo "$w101"; exit 1
fi
w102=$(cd .. && NMAX=10 python3 -I new/box153/decomp.py new/box14*/out/*.json new/box14*/inst/*.json new/box152/*_d5_*.json; python3 -I new/box153/longpath.py new/box153/ladlp_5.json)
if grep -qxF "DECOMP genomes 25 faces 478953 USO 0 COMB 0 ORDER 0 ACYC 0 JUMP 0 maxjump 7" <<<"$w102" && grep -qxF "LONGPATH ladlp_5.json n2 10 longest 114 ideal_T 1" <<<"$w102"; then
  echo "box 153 DECOMP: improvement orientation is a decomposable AUSO (0 violations); Xi-ladder K 5 longest improving path 114: PASS"
else
  echo "box 153 check: FAILED"; echo "$w102"; exit 1
fi
w103=$(cd .. && python3 -I new/box154/ladder.py 10)
if [ "$(grep -c ' OK$' <<<"$w103")" = 10 ] && grep -qF "LADDER K 7 N 14 path 254 = 2^(K+1)-2 True nonimproving 0 flips [2, 4, 8, 16, 32, 64, 128] DP_longest 254 ideal_T 0 OK" <<<"$w103"; then
  echo "box 154 LADDER-LP: Xi-ladder L_K has a directed improving path of length 2^(K+1)-2 (K = 1..10; DP exact K <= 7): PASS"
else
  echo "box 154 LADDER check: FAILED"; echo "$w103"; exit 1
fi
# frozen-file pins (CHECKER C116 G-3): P-IDEAL-CUBE packet and line L-1 (d97555d4)
pin104=$(cd ../.. && sha1sum docs/new/P-IDEAL-CUBE.md docs/new/P-IDEAL-CUBE-line-L1.txt docs/new/P-IDEAL-CUBE-line-L2.txt docs/new/P-IDEAL-CUBE-fixes.md)
if grep -q "^366afedcf7cd04a31302e25cec47c7fb3df455bb  docs/new/P-IDEAL-CUBE.md$" <<<"$pin104" && grep -q "^99ae8face50615b4ce1ce5cd5e69f223f17208e1  docs/new/P-IDEAL-CUBE-line-L1.txt$" <<<"$pin104" && grep -q "^449421e4cfaedbef577f68720fab4924111cd170  docs/new/P-IDEAL-CUBE-line-L2.txt$" <<<"$pin104" && grep -q "^006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e  docs/new/P-IDEAL-CUBE-fixes.md$" <<<"$pin104"; then
  echo "P-IDEAL-CUBE pins (packet 366afedc, line L-1 99ae8fac, line L-2 449421e4, fixes 006274ec): PASS"
else
  echo "P-IDEAL-CUBE pin check: FAILED"; echo "$pin104"; exit 1
fi
# P-IDEAL-M2 (box 156; L-NEW 51): MULTI-CHARGE (mcharge.py), TRIGGER / XIFLIP (trig.py, with NEG=3 control), LIN-156 DEAD instance, pins
w105=$(cd .. && python3 -I new/box155/mcharge.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*.json new/box153/*.json new/box156/ext/*.json; ALL=1 ALLN=8 python3 -I new/box155/mcharge.py new/box150/out/rand/*.json; python3 -I new/box156/trig.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*.json new/box153/*.json new/box156/ext/*.json; ALL=1 python3 -I new/box156/trig.py new/box150/out/rand/*.json; NEG=3 python3 -I new/box156/trig.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*.json new/box153/*.json new/box156/ext/*.json; python3 -I new/box156/val.py new/box156/ext/max_d4_L13.json)
if grep -qxF "MCHARGE runs 54 steps 468 unch 222 M2 300 VIOL 0 BOUND 0 single_runs 0 single_maxT_over_N 0.0" <<<"$w105" && grep -qxF "MCHARGE runs 34934 steps 38676 unch 2148 M2 5188 VIOL 0 BOUND 0 single_runs 6114 single_maxT_over_N 1.0" <<<"$w105" && grep -qxF "TRIG runs 54 moves 919 NEITHER 0 WNOLOW 0 XNODESC 0 XiT 707 WT 333 BOTH 121 multi 270 WREL 162 XIBR 108 XIFLIP 0" <<<"$w105" && grep -qxF "TRIG runs 3981 moves 298 NEITHER 0 WNOLOW 0 XNODESC 0 XiT 298 WT 0 BOTH 0 multi 12 WREL 0 XIBR 12 XIFLIP 0" <<<"$w105" && grep -q "^TRIG runs 54 moves 488 NEITHER 141 " <<<"$w105" && grep -qxF "new/box156/ext/max_d4_L13.json N 8 T 13 M2 5 U 4 mv [1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1]" <<<"$w105" && [ "$(sha1sum box156/ext/max_d4_L13.json | cut -d' ' -f1)" = f0735b61312bdbfe1bb553496d7e9ee38681dcee ]; then
  echo "P-IDEAL-M2: MULTI-CHARGE 0 viol. (54 + 34,934 runs), TRIGGER / XIFLIP 0 viol. (54 + 3,981 runs; NEG=3 fires), max_d4_L13 T 13 > 12: PASS"
else
  echo "P-IDEAL-M2 check: FAILED"; echo "$w105"; exit 1
fi
pin105=$(cd ../.. && sha1sum docs/new/P-IDEAL-M2.md docs/new/P-IDEAL-M2-line-L1.txt docs/new/P-IDEAL-M2-line-L2.txt docs/new/P-IDEAL-M2-fixes.md)
if grep -q "^bc47b06c4b8d90ceb28939c966083e0c057a442b  docs/new/P-IDEAL-M2.md$" <<<"$pin105" && grep -q "^0160d1e3ffa832536454a74c559b20280b87f53e  docs/new/P-IDEAL-M2-line-L1.txt$" <<<"$pin105" && grep -q "^c890f2685edf3725a5fccb12cf93e9d3dd7d44ff  docs/new/P-IDEAL-M2-line-L2.txt$" <<<"$pin105" && grep -q "^66fd61731df0667e380e8ac231ee27062ee6b8a8  docs/new/P-IDEAL-M2-fixes.md$" <<<"$pin105"; then
  echo "P-IDEAL-M2 pins (packet bc47b06c, line L-1 0160d1e3, line L-2 c890f268, fixes 66fd6173): PASS"
else
  echo "P-IDEAL-M2 pin check: FAILED"; echo "$pin105"; exit 1
fi
# box 157 (L-NEW 51): Lemma SEG, SEG-ONCE, Corollary LEVEL-PRODUCT (segcheck.py; BADLEV=2 negative control)
w106=$(cd .. && python3 -I new/box157/segcheck.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*.json new/box153/*.json new/box156/ext/*.json new/box157/max_d5_L15.json new/box139/genomes/*.json; ALL=1 ALLN=8 python3 -I new/box157/segcheck.py new/box150/out/rand/*.json; BADLEV=2 python3 -I new/box157/segcheck.py new/box14*/out/*.json new/box14*/inst/*.json new/box142/*.json new/box146/*.json new/box152/*.json new/box153/*.json new/box156/ext/*.json new/box157/max_d5_L15.json new/box139/genomes/*.json)
if grep -qxF "SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 0.3333" <<<"$w106" && grep -qxF "SEGCHECK runs 34934 steps 38676 intervals 57755 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 1.0" <<<"$w106" && grep -qxF "SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 112 COUNT 0 PROD 0 maxratio 0.3333" <<<"$w106" && [ "$(sha1sum box157/max_d5_L15.json | cut -d' ' -f1)" = ba963aceabeb35d95f9c47d80d1d0e87b87baf21 ]; then
  echo "box 157 SEG / SEG-ONCE / LEVEL-PRODUCT: 0 violations (59 + 34,934 runs; BADLEV=2 control fires): PASS"
else
  echo "box 157 segcheck: FAILED"; echo "$w106"; exit 1
fi
# P-IDEAL-SEG (box 157; L-NEW 51): REPLAY DEAD instance data (seg.py on max_d5_L15) + frozen-file pins; SEG checks are block w106
w107=$(cd .. && python3 -I new/box157/seg.py new/box157/max_d5_L15.json)
pin107=$(cd ../.. && sha1sum docs/new/P-IDEAL-SEG.md docs/new/P-IDEAL-SEG-line-L1.txt docs/new/P-IDEAL-SEG-fixes.md)
if grep -qxF "max_d5_L15.json N 10 T 15 L 0 cuts [7, 8]" <<<"$w107" && grep -qF "  seg t9-15 len 7 NEWSTATES 7 REPLAY False: " <<<"$w107" && grep -qF "  seg t1-6 len 6 NEWSTATES 6 REPLAY False: " <<<"$w107" && [ "$(sha1sum box157/max_d5_L15.json | cut -d' ' -f1)" = ba963aceabeb35d95f9c47d80d1d0e87b87baf21 ] && grep -q "^7fa847843cb950e87dac38bf3d612effd5a9834e  docs/new/P-IDEAL-SEG.md$" <<<"$pin107" && grep -q "^a18f6f0c61d6d5f33adc61519d94252dd5ba9721  docs/new/P-IDEAL-SEG-line-L1.txt$" <<<"$pin107" && grep -q "^2e3dd53211b44ca752611aadf4f30e5a0e7c165f  docs/new/P-IDEAL-SEG-fixes.md$" <<<"$pin107"; then
  echo "P-IDEAL-SEG: REPLAY DEAD data on max_d5_L15 (segment t9-15 all new); pins packet 7fa84784, line L-1 a18f6f0c, fixes 2e3dd532: PASS"
else
  echo "P-IDEAL-SEG check: FAILED"; echo "$w107"; echo "$pin107"; exit 1
fi
# box 158 (L-NEW 51): Lemma LIFT on three champions (same run one level up, no level-0 move) and their segment data
w108=$(cd .. && for f in new/box156/ext/max_d4_L13.json new/box157/max_d5_L15.json new/box152/dd_d5_F14.json; do python3 -I new/box158/lift.py $f "$tmp/lift_$(basename $f)"; done; python3 -I new/box158/three.py "$tmp"/lift_*.json)
if [ "$(grep -c ' SAME True$' <<<"$w108")" = 3 ] && grep -qxF "lift_max_d4_L13.json d 5 T 13 cuts [] seg1 13" <<<"$w108" && grep -qxF "lift_max_d5_L15.json d 6 T 15 cuts [] seg1 15" <<<"$w108"; then
  echo "box 158 LIFT: max_d4_L13 / max_d5_L15 / dd_d5_F14 lift one level up with the same run and seg1 = T: PASS"
else
  echo "box 158 LIFT check: FAILED"; echo "$w108"; exit 1
fi
# P-IDEAL-SLOT (box 158; L-NEW 51): instance lift_max_d4_L13 (box 150 checker), frozen-file pins; LIFT runs are block w108
w109=$(cd .. && python3 -I new/box150/check.py new/box158/lift_max_d4_L13.json | tail -1; python3 -I new/box158/three.py new/box158/lift_max_d4_L13.json)
pin109=$(cd ../.. && sha1sum docs/new/P-IDEAL-SLOT.md docs/new/P-IDEAL-SLOT-line-L1.txt experiments/new/box158/lift_max_d4_L13.json docs/new/P-IDEAL-SLOT-line-L2.txt docs/new/P-IDEAL-SLOT-fixes.md docs/new/P-IDEAL-SLOT-line-L3.txt docs/new/P-IDEAL-SLOT-line-L4.txt)
if grep -qxF "TOTAL genomes 1 runs 1 steps 13 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)" <<<"$w109" && grep -qxF "lift_max_d4_L13.json d 5 T 13 cuts [] seg1 13" <<<"$w109" && grep -q "^62901b5f951598fb44426942b0fb1d999325625a  docs/new/P-IDEAL-SLOT.md$" <<<"$pin109" && grep -q "^17236fb18d70c1e2968689108a74a1acac938bd5  docs/new/P-IDEAL-SLOT-line-L1.txt$" <<<"$pin109" && grep -q "^33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38  experiments/new/box158/lift_max_d4_L13.json$" <<<"$pin109" && grep -q "^55e74726f0c7e6c6e27f780b779788014cc97e29  docs/new/P-IDEAL-SLOT-line-L2.txt$" <<<"$pin109" && grep -q "^e7bd036111a2a87a67183b998a62f10f533aff9f  docs/new/P-IDEAL-SLOT-fixes.md$" <<<"$pin109" && grep -q "^0c51ce6da0a655c31112515c78cb0b5d22690168  docs/new/P-IDEAL-SLOT-line-L3.txt$" <<<"$pin109" && grep -q "^008b10ad8ee340793c5167fe5f990b7b71020630  docs/new/P-IDEAL-SLOT-line-L4.txt$" <<<"$pin109"; then
  echo "P-IDEAL-SLOT: instance lift_max_d4_L13 (d 5, T 13, seg1 13, 0 violations); pins packet 62901b5f, line L-1 17236fb1, instance 33fec48f, line L-2 55e74726, fixes e7bd0361, line L-3 0c51ce6d, line L-4 008b10ad: PASS"
else
  echo "P-IDEAL-SLOT check: FAILED"; echo "$w109"; echo "$pin109"; exit 1
fi
# P-IDEAL-FLIP (box 162; L-NEW 53): W-ONLY / NOW-ONCE / SWAP / FLIP-1 checks (flipcheck.py), instance iso_d4_st9 (box 150 checker), pins
w162=$(cd .. && python3 -I new/box162/flipcheck.py; python3 -I new/box150/check.py new/box160/out/iso_d4_st9.json | tail -1)
pin162=$(cd ../.. && sha1sum docs/new/P-IDEAL-FLIP.md docs/new/P-IDEAL-FLIP-line-L1.txt experiments/new/box160/out/iso_d4_st9.json experiments/new/box162/out/kf0_d2_t2.json experiments/new/box162/out/kf1_d2_t3.json docs/new/P-IDEAL-FLIP-fixes.md docs/new/P-IDEAL-FLIP-line-L2.txt docs/new/P-IDEAL-FLIP-line-L3.txt)
if grep -qE "WONLY 0 ISOA 0 FROZ 0 CONS 0 SWAP 0 SWAPNEG [1-9][0-9]* NOWONCE 0 NOWCTRL [1-9][0-9]* FLIP1 0$" <<<"$w162" && grep -qxF "INST iso_d4_st9 LR True ISO True d 4 T 11 level-0 steps [7, 8] seg1 6 tail 3" <<<"$w162" && grep -qxF "WIT kf0_d2_t2.json LR True ISO True V_0 2" <<<"$w162" && grep -qxF "WIT kf1_d2_t3.json LR True ISO True V_1 3" <<<"$w162" && grep -qxF "TOTAL genomes 1 runs 1 steps 11 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)" <<<"$w162" && grep -q "^92803bd5b750924f0d0bc7db3c57eddf5725dfcb  docs/new/P-IDEAL-FLIP.md$" <<<"$pin162" && grep -q "^36418d164ac759472fadf0b411d81901db32e6da  docs/new/P-IDEAL-FLIP-line-L1.txt$" <<<"$pin162" && grep -q "^7ca1e68c52e4bb02ee260ccc36e8323146cdc6b3  experiments/new/box160/out/iso_d4_st9.json$" <<<"$pin162" && grep -q "^c2233e05b6212233acf5e3121b0ed088b7863b3c  experiments/new/box162/out/kf0_d2_t2.json$" <<<"$pin162" && grep -q "^d368d441b13b512c3453ea168d187734fe92b45e  experiments/new/box162/out/kf1_d2_t3.json$" <<<"$pin162" && grep -q "^4220c44e6caa0bc6e2b2d4363ba3f5ec97505de6  docs/new/P-IDEAL-FLIP-fixes.md$" <<<"$pin162" && grep -q "^4089bd73baf65929cf5b6094ef31882df817fd53  docs/new/P-IDEAL-FLIP-line-L3.txt$" <<<"$pin162" && grep -q "^8099415b58689ea9241f2da9d642ba8a1af74cf9  docs/new/P-IDEAL-FLIP-line-L2.txt$" <<<"$pin162"; then
  echo "P-IDEAL-FLIP: flipcheck 0 violations (controls fire), instance iso_d4_st9 (T 11, seg1 6, tail 3), FLIP-1 instances V_0 2 / V_1 3; pins packet 92803bd5, line L-1 36418d16, instance 7ca1e68c, I-0 c2233e05, I-1 d368d441, fixes 4220c44e, line L-2 8099415b, line L-3 4089bd73: PASS"
else
  echo "P-IDEAL-FLIP check: FAILED"; echo "$w162"; echo "$pin162"; exit 1
fi
# P-IDEAL-KEYS (box 172; L-NEW 55): key-side lemma checks (keycheck.py, frozen output), DEAD instances (box 150 checker), pins
w172=$(cd .. && python3 -I new/box172/keycheck.py | diff - new/box172/keycheck.out && echo KEYCHECK SAME; for f in box166/out/KILL_PM_compose_dd_d5_F14.json box172/inst/dd_d5_F14.json box170/out/T1_dd_top8.json; do python3 -I new/box150/check.py new/$f | tail -1; done)
pin172=$(cd ../.. && sha1sum docs/new/P-IDEAL-KEYS.md docs/new/P-IDEAL-KEYS-line-L1.txt experiments/new/box172/keycheck.py experiments/new/box172/keycheck.out experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json experiments/new/box172/inst/dd_d5_F14.json experiments/new/box170/out/T1_dd_top8.json docs/new/P-IDEAL-KEYS-fixes.md docs/new/P-IDEAL-KEYS-line-L2.txt docs/new/P-IDEAL-KEYS-line-L3.txt)
if grep -qxF "KEYCHECK SAME" <<<"$w172" && [ "$(grep -cxF "TOTAL genomes 1 runs 1 steps 14 XSIM 0 TOPO 0 MONO 0 XINEW 0 RISE 0 CHAIN 0 KEYFLIP 0 DECR 0 TOPMONO 0 RBOUND 0 RESTR 0 ICHARGE 0 REC 0 VIOL 0 (info REC148 0)" <<<"$w172")" = 3 ] && grep -qxF "LOCALKP 0 LOCALCTL 48435 KFWE 0 PAIRKF 0 CASCADE 0 LADDER 0 FLET 0 RENEW 0 RENEWB 0 MERGE 0 MERGECTL 23272 RETURN 0 RETCNT 0 KEYFLIP 0" box172/keycheck.out && grep -q "^62b35bf7ed7616bb66ff512edc30fe30431db0e5  docs/new/P-IDEAL-KEYS.md$" <<<"$pin172" && grep -q "^f36c6402064f61511048887bde28a72e270382ee  docs/new/P-IDEAL-KEYS-line-L1.txt$" <<<"$pin172" && grep -q "^6ce4693dda9f5baac0f524312009955d89a0a41a  experiments/new/box172/keycheck.py$" <<<"$pin172" && grep -q "^5100eb30482a1c5ceb60b7ed84b38d7700213770  experiments/new/box172/keycheck.out$" <<<"$pin172" && grep -q "^c025a4b61cd6342775aba6cbe2f89a9362dfa172  experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json$" <<<"$pin172" && grep -q "^06f0e5015d09c0f1e03f1b9293ab3cd8483e435b  experiments/new/box172/inst/dd_d5_F14.json$" <<<"$pin172" && grep -q "^9aead80e6123c720255cfbf75af12992bbc8e9b9  experiments/new/box170/out/T1_dd_top8.json$" <<<"$pin172" && grep -q "^504403c3816279bee51da5358e0e77250ffb8f69  docs/new/P-IDEAL-KEYS-fixes.md$" <<<"$pin172" && grep -q "^c29f0a9365e700e0888018be42caf8757df1ac74  docs/new/P-IDEAL-KEYS-line-L3.txt$" <<<"$pin172" && grep -q "^fb1b22763f5cc5e64fa2cab78468718b1321a846  docs/new/P-IDEAL-KEYS-line-L2.txt$" <<<"$pin172"; then
  echo "P-IDEAL-KEYS: keycheck 0 violations (controls fire, output = frozen keycheck.out), DEAD instances PM / PMV / tower replayed (XSIM 0); pins packet 62b35bf7, line L-1 f36c6402, tool 6ce4693d, output 5100eb30, instances c025a4b6 / 06f0e501 / 9aead80e, fixes 504403c3, line L-2 fb1b2276, line L-3 c29f0a93: PASS"
else
  echo "P-IDEAL-KEYS check: FAILED"; echo "$w172"; echo "$pin172"; exit 1
fi
# P-IDEAL-ALIGN (box 178; L-NEW 55): ALIGN / PAIR-DOUBLE / MOVES / T-BOUND / PATH-RISE checks (aligncheck.py, frozen output), pins
w178=$(cd .. && python3 -I new/box178/aligncheck.py | diff - new/box178/aligncheck.out && echo ALIGNCHECK SAME)
pin178=$(cd ../.. && sha1sum docs/new/P-IDEAL-ALIGN.md docs/new/P-IDEAL-ALIGN-line-L1.txt experiments/new/box178/aligncheck.py experiments/new/box178/aligncheck.out experiments/new/box172/inst/dd_d5_F14.json docs/new/P-IDEAL-ALIGN-fixes.md docs/new/P-IDEAL-ALIGN-line-L2.txt docs/new/P-IDEAL-ALIGN-line-L3.txt)
if grep -qxF "ALIGNCHECK SAME" <<<"$w178" && grep -qxF "KPEQ 0 LAND 0 ORD 0 DBL 0 F0 0 KFF 0 MOV 0 TB 0 PATH 0" box178/aligncheck.out && grep -q "^d8acdececb507bfad476341411bddd579fcc5b00  docs/new/P-IDEAL-ALIGN.md$" <<<"$pin178" && grep -q "^e46b0417295bfbde7f4cb2d434deed5d0f2e209c  docs/new/P-IDEAL-ALIGN-line-L1.txt$" <<<"$pin178" && grep -q "^9335dee71554491004b5f7567bb1a6784c5292dd  experiments/new/box178/aligncheck.py$" <<<"$pin178" && grep -q "^b653b01bbdca19c8e0c7d406b1bd2470c35c55fc  experiments/new/box178/aligncheck.out$" <<<"$pin178" && grep -q "^06f0e5015d09c0f1e03f1b9293ab3cd8483e435b  experiments/new/box172/inst/dd_d5_F14.json$" <<<"$pin178" && grep -q "^64e83e68e4a3642b724b2a5d3b712bec4162c21a  docs/new/P-IDEAL-ALIGN-fixes.md$" <<<"$pin178" && grep -q "^cb5f0398431cc1a5122e13327e7bbae9f9985e51  docs/new/P-IDEAL-ALIGN-line-L2.txt$" <<<"$pin178" && grep -q "^4d28b1f36f610c6ecda7ab48891edb5feae97d66  docs/new/P-IDEAL-ALIGN-line-L3.txt$" <<<"$pin178"; then
  echo "P-IDEAL-ALIGN: aligncheck 0 violations (output = frozen aligncheck.out); pins packet d8acdece, line L-1 e46b0417, tool 9335dee7, output b653b01b, instance 06f0e501, fixes 64e83e68, line L-2 cb5f0398, line L-3 4d28b1f3: PASS"
else
  echo "P-IDEAL-ALIGN check: FAILED"; echo "$w178"; echo "$pin178"; exit 1
fi
rm -rf "$tmp"
