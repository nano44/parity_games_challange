#!/usr/bin/env bash
# L-SI P-N5-GATE fixes entry 5 self-check (called by box95/check95.sh): CHECKER's report copy against fix5.sha1; L-5 rebuilt by mkL5.py
# byte for byte; its nine-pair stage equals CHECKER C142's target sha1 and size; the tenth pair (Lead 17:58Z) is in; the fixes file = entries 1-4 (as check_fix4.sh rebuilds them)
# followed by entry 5 (mkfix5.py, which re-reads the cited numbers from the frozen box outputs).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
sha1sum -c --quiet --strict fix5.sha1
python3 -I -B mkL5.py $R --nine 2> /dev/null > "$t/L9"
[ "$(sha1sum < "$t/L9" | cut -c1-40)" = 7ebcf7355be9838473f05a7defe913940b6fd723 ] && [ "$(wc -c < "$t/L9" | tr -d ' ')" = 12923 ]
python3 -I -B mkL5.py $R 2> /dev/null > "$t/L5"; cmp -s "$t/L5" $R/docs/si/P-N5-GATE-line-L5.txt
[ "$(grep -c "with its fixes entries 1-5," $R/docs/si/P-N5-GATE-line-L5.txt)" = 1 ]
f() { sha1sum < $R/docs/si/P-N5-GATE-line-L$1.txt | cut -c1-40; }; g() { wc -c < $R/docs/si/P-N5-GATE-line-L$1.txt | tr -d ' '; }
python3 -I -B ../fix1/mkfix1.py $R "$(f 1)" "$(g 1)" > "$t/e1"
python3 -I -B ../fix2/mkfix2.py $R "$(f 2)" "$(g 2)" > "$t/e2"
python3 -I -B ../fix3/mkfix3.py $R "$(f 3)" "$(g 3)" > "$t/e3"
python3 -I -B ../fix4/mkfix4.py $R "$(f 4)" "$(g 4)" > "$t/e4"
python3 -I -B mkfix5.py $R "$(f 5)" "$(g 5)" > "$t/e5"
cat "$t/e1" "$t/e2" "$t/e3" "$t/e4" "$t/e5" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-N5-GATE-fixes.md | cmp -s - "$t/f"
echo "P-N5-GATE fix5 checks: PASS"
