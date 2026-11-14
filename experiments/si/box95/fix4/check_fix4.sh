#!/usr/bin/env bash
# L-SI P-N5-GATE fixes entry 4 self-check (called by box95/check95.sh): the report copy against fix4.sha1; L-4 rebuilt by mkL4.py byte for
# byte; the fixes file = entries 1-3 (as check_fix3.sh rebuilds them) followed by entry 4 (mkfix4.py).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
sha1sum -c --quiet --strict fix4.sha1
python3 -I -B mkL4.py $R > "$t/L4"; cmp -s "$t/L4" $R/docs/si/P-N5-GATE-line-L4.txt
f() { sha1sum < $R/docs/si/P-N5-GATE-line-L$1.txt | cut -c1-40; }; g() { wc -c < $R/docs/si/P-N5-GATE-line-L$1.txt; }
python3 -I -B ../fix1/mkfix1.py $R "$(f 1)" "$(g 1)" > "$t/e1"
python3 -I -B ../fix2/mkfix2.py $R "$(f 2)" "$(g 2)" > "$t/e2"
python3 -I -B ../fix3/mkfix3.py $R "$(f 3)" "$(g 3)" > "$t/e3"
python3 -I -B mkfix4.py $R "$(f 4)" "$(g 4)" > "$t/e4"
cat "$t/e1" "$t/e2" "$t/e3" "$t/e4" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-N5-GATE-fixes.md | cmp -s - "$t/f"
echo "P-N5-GATE fix4 checks: PASS"
