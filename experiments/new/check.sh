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
w3=$(python3 -I box55/pcheck.py ../red/n3/instances/n3cov_lean.pg ../red/n3/instances/n3cov_lean.start)
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
rm -rf "$tmp"
