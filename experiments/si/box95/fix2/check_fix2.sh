#!/usr/bin/env bash
# L-SI P-N5-GATE fixes entry 2 self-check (called by box95/check95.sh): L-2 rebuilt from L-1 by mkL2.py and compared byte for byte;
# the fixes file = entry 1 (as check_fix1.sh rebuilds it) followed by entry 2 (mkfix2.py); L-RED's copied report against its sha1.
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
sha1sum -c --quiet --strict fix2.sha1
python3 -I -B mkL2.py $R > "$t/L2"; cmp -s "$t/L2" $R/docs/si/P-N5-GATE-line-L2.txt
s1=$(sha1sum < $R/docs/si/P-N5-GATE-line-L1.txt | cut -c1-40); b1=$(wc -c < $R/docs/si/P-N5-GATE-line-L1.txt)
s2=$(sha1sum < $R/docs/si/P-N5-GATE-line-L2.txt | cut -c1-40); b2=$(wc -c < $R/docs/si/P-N5-GATE-line-L2.txt)
python3 -I -B ../fix1/mkfix1.py $R "$s1" "$b1" > "$t/e1"
python3 -I -B mkfix2.py $R "$s2" "$b2" > "$t/e2"
cat "$t/e1" "$t/e2" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-N5-GATE-fixes.md | cmp -s - "$t/f"
echo "P-N5-GATE fix2 checks: PASS"
