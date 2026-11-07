#!/usr/bin/env bash
# L-SI box 81 BRIDGE (docs/si/box81-bridge.md) self-check: pins --strict (L-NEW byte copies in ref/, frozen instances in inst/);
# regenerates every frozen output in out/ and diffs: ascent census (census81.py --loc), real runners on Gamma3 from S3 and on Gamma from
# R104's stated start (real81.py), the independent xcheck (xchk81.py), Lemma BETA-ACYC / Theorem ACYC-LIN data (lemma81.py).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict ref.sha1
sha1sum -c --quiet --strict inst.sha1
t=$(mktemp -d)
LIB="rd2_d3 rd2_d4 rd3_d3 rf_d4 RS2 RS2_L8M6 RSG_K4 FPORT_n2"; TOW="H5_d20_F62 H6_d24_F126 SL41_d28 L6Z_KILL238_d28"
for i in $LIB $TOW; do
  python3 -I -B census81.py --loc inst/$i.json > "$t/c"; diff -q "$t/c" out/census_$i.out
  python3 -I -B real81.py inst/$i.json > "$t/r"; diff -q "$t/r" out/real_$i.out
done
for i in $TOW; do
  python3 -I -B real81.py --stated --modes spec,xi inst/$i.json > "$t/s"; diff -q "$t/s" out/stated_$i.out
done
for i in rd2_d3 rd2_d4 rd3_d3 rf_d4 RS2 RSG_K4 RS2_L8M6 H5_d20_F62 H6_d24_F126 L6Z_KILL238_d28; do
  python3 -I -B xchk81.py inst/$i.json > "$t/x"; diff -q "$t/x" out/xchk_$i.out
  grep -q "game SAME states SAME .* valuediffs 0 hist SAME .* labels SAME" out/xchk_$i.out
done
python3 -I -B lemma81.py agen 300 7 > "$t/l"; diff -q "$t/l" out/lemma81_agen_300_7.out
python3 -I -B lemma81.py agen 0 1 $(for i in $TOW; do echo inst/$i.json; done) > "$t/l"; diff -q "$t/l" out/lemma81_towers.out
python3 -I -B lemma81.py rgen 0 1 inst/rd2_d3.json inst/rd2_d4.json inst/rd3_d3.json inst/rf_d4.json inst/RS2.json > "$t/l"
diff -q "$t/l" out/lemma81_cyclic_control.out
# packet P-ACYC (docs/si/P-ACYC.md): premise quotes verbatim; Gamma3 N5'-xi data; packet + line pins
python3 -I -B quotes81.py > "$t/q"; diff -q "$t/q" out/quotes81.out
python3 -I -B pacyc81.py 0 1 $(for i in $TOW; do echo inst/$i.json; done) > "$t/p"; diff -q "$t/p" out/pacyc81_towers.out
python3 -I -B pacyc81.py 0 1 inst/rd2_d3.json inst/rd2_d4.json inst/rd3_d3.json inst/rf_d4.json inst/RS2.json > "$t/p"
diff -q "$t/p" out/pacyc81_cyclic_control.out
python3 -I -B pacyc81.py 300 7 > "$t/p"; diff -q "$t/p" out/pacyc81_agen_300_7.out
sha1sum -c --quiet --strict pacyc.sha1
rm -rf "$t"
grep -q "nofallback 0 notbeta 0 nonstd 0 C 0 R 0 bigT 0" out/pacyc81_agen_300_7.out
grep -q "nofallback 0 notbeta 0 nonstd 0 C 0 R 0 bigT 0" out/pacyc81_towers.out
grep -q "^quotes: 28 of 28 verbatim$" out/quotes81.out
grep -q "notbeta 0 nonstrict 0 C 0 R 0 T_gt_N 0" out/lemma81_agen_300_7.out
grep -q "notbeta 0 nonstrict 0 C 0 R 0 T_gt_N 0" out/lemma81_towers.out
! grep -q "notbeta 0 " out/lemma81_cyclic_control.out
for i in $LIB $TOW; do grep -q "upb OK hubfail 0 .* ovtfail 0 rsplit OK" out/census_$i.out; done
echo "box 81 checks: PASS"
