#!/usr/bin/env bash
# L-SI box 79 (packet P-IDEAL-DBL, DRAFT; docs/si/P-IDEAL-DBL.md) self-check (~30 s): pins --strict (tools, frozen outputs, packet and
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
python3 -I -B dead79.py > "$t/d"
diff -q "$t/d" dead79.out
rm -rf "$t"
grep -q "^CORPUS violations: WO 0 HIT 0 ALTa 0 ALTb 0 ALTc 0 ALTd 0 DBLa 0 DBLb 0 DBLc 0 TN 0 PF 0 FU2 0$" dblcheck.out
grep -q "^LOWER violations: WO 0 HIT 0 ALTa 0 ALTb 0 ALTc 0 ALTd 0 DBLa 0 DBLb 0 DBLc 0 TN 0 PF 0 FU2 0$" dblcheck.out
grep -q "^CORPUS violations: WO 0 HIT 238546 ALTa 86709 " dblcheck_neg2.out
echo "box 79 P-IDEAL-DBL (draft) checks: PASS"
