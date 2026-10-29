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
rm -rf "$tmp"
