#!/usr/bin/env bash
# L-SI box 79 (packet P-IDEAL-DBL, FROZEN; docs/si/P-IDEAL-DBL.md) self-check (~30 s): pins --strict (tools, frozen outputs, packet and
# line); dblcheck.py reproduces dblcheck.out (all violation counters 0, controls > 0); NEG=2 control reproduces dblcheck_neg2.out (HIT and
# ALTa > 0); dead79.py replays the DEAD instances (asserts).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I -B dblcheck.py > "$t/c"
diff -q "$t/c" dblcheck.out
NEG=2 python3 -I -B dblcheck.py > "$t/n"
diff -q "$t/n" dblcheck_neg2.out
python3 -I -B dblcheck.py inst/RECF4_d20_F60.json inst/DBL4_d20_F30.json inst/H5_d20_F62.json inst/H6_d24_F126.json > "$t/x"
diff -q "$t/x" extra79.out
python3 -I -B wiring79.py inst/RECF4_d20_F60.json inst/DBL4_d20_F30.json inst/H5_d20_F62.json inst/H6_d24_F126.json > "$t/w"
diff -q "$t/w" wiring79.out
python3 -I -B dead79.py > "$t/d"
diff -q "$t/d" dead79.out
python3 -I -B reentry_levels.py > "$t/r"
diff -q "$t/r" reentry_levels.out
python3 -I -B mkL2.py > "$t/L2"
cmp "$t/L2" ../../../docs/si/P-IDEAL-DBL-line-L2.txt
python3 -I -B mkL3.py > "$t/L3"
cmp "$t/L3" ../../../docs/si/P-IDEAL-DBL-line-L3.txt
rm -rf "$t"
grep -q "^CORPUS violations: WO 0 HIT 0 ALTa 0 ALTb 0 ALTc 0 ALTd 0 DBLa 0 DBLb 0 DBLc 0 TN 0 PF 0 FU2 0$" dblcheck.out
grep -q "^LOWER violations: WO 0 HIT 0 ALTa 0 ALTb 0 ALTc 0 ALTd 0 DBLa 0 DBLb 0 DBLc 0 TN 0 PF 0 FU2 0$" dblcheck.out
grep -q "^EXTRA violations: WO 0 HIT 0 ALTa 0 ALTb 0 ALTc 0 ALTd 0 DBLa 0 DBLb 0 DBLc 0 TN 0 PF 0 FU2 0$" extra79.out
grep -q "^CORPUS violations: WO 0 HIT 238546 ALTa 86709 " dblcheck_neg2.out
echo "box 79 P-IDEAL-DBL (frozen) checks: PASS"
