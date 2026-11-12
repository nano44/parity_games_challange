#!/usr/bin/env bash
# L-SI P-N5-GATE fixes entry 3 self-check (called by box95/check95.sh): the referee byte copies against fix3.sha1; L-3 rebuilt from L-2 by
# mkL3.py and compared byte for byte; the fixes file = entries 1-2 (as check_fix2.sh rebuilds them) followed by entry 3 (mkfix3.py); the
# copy95 rows identical on the two engines and 20 of 22 instances set-equal on every level.
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
sha1sum -c --quiet --strict fix3.sha1
python3 -I -B mkL3.py $R > "$t/L3"; cmp -s "$t/L3" $R/docs/si/P-N5-GATE-line-L3.txt
s1=$(sha1sum < $R/docs/si/P-N5-GATE-line-L1.txt | cut -c1-40); b1=$(wc -c < $R/docs/si/P-N5-GATE-line-L1.txt)
s2=$(sha1sum < $R/docs/si/P-N5-GATE-line-L2.txt | cut -c1-40); b2=$(wc -c < $R/docs/si/P-N5-GATE-line-L2.txt)
s3=$(sha1sum < $R/docs/si/P-N5-GATE-line-L3.txt | cut -c1-40); b3=$(wc -c < $R/docs/si/P-N5-GATE-line-L3.txt)
python3 -I -B ../fix1/mkfix1.py $R "$s1" "$b1" > "$t/e1"
python3 -I -B ../fix2/mkfix2.py $R "$s2" "$b2" > "$t/e2"
python3 -I -B mkfix3.py $R "$s3" "$b3" > "$t/e3"
cat "$t/e1" "$t/e2" "$t/e3" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-N5-GATE-fixes.md | cmp -s - "$t/f"
cmp -s <(cut -d' ' -f2- out/copy95_own.out) <(cut -d' ' -f2- out/copy95_g3.out)
[ "$(grep -c 'copy 0' out/copy95_own.out)" = 2 ] && [ "$(grep -c 'copy' out/copy95_own.out)" = 22 ]
echo "P-N5-GATE fix3 checks: PASS"
