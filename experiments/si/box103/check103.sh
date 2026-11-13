#!/usr/bin/env bash
# L-SI box 103 check (~1 s): in both census files, the k = 1 class has lossy_d1 0 and esame_d1 0 (CONJECTURE NOLOSS-k1's counters) and
# lostE 0 in both classes (R125 E-MON3); the WC16_2 listing shows its one deep change as a pure gain.
set -u
cd "$(dirname "$0")"
fail=0
for f in out/mdeep103_inst.out out/mdeep103_rand.out; do
  grep -q "^TOTAL .*'k1': {[^}]*'lossy_d1': 0, [^}]*'esame_d1': 0, [^}]*'lostE': 0}" "$f" || { echo "BOX103 FAIL k1 counters $f"; fail=1; }
  grep -q "^TOTAL .*'k2+': {[^}]*'lostE': 0}" "$f" || { echo "BOX103 FAIL lostE $f"; fail=1; }
done
grep -q "gained e-depth 16" out/wcdeep_WC16_2.out && grep -q "lost e: \[\]  gained e: \[(33, 0)\]" out/wcdeep_WC16_2.out || { echo "BOX103 FAIL WC16 listing"; fail=1; }
[ $fail = 0 ] && echo "BOX103 checks: PASS"
exit $fail
