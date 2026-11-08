#!/usr/bin/env bash
# L-SI P-ACYC fixes entry 4 self-check (called by box81/check81.sh): L-5 rebuilt from L-4 by mkL5.py and compared byte for byte, with
# CHECKER C136's sha1; the fixes file must equal entries 1-3 (as check_fix3.sh rebuilds them) followed by entry 4 (mkfix4.py).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d)
python3 -I -B mkL5.py $R > "$t/L5"; cmp -s "$t/L5" $R/docs/si/P-ACYC-line-L5.txt
[ "$(sha1sum < $R/docs/si/P-ACYC-line-L5.txt | cut -c1-40)" = 7a84e0944b0f33ce4d569604bec41d6e9236d82f ]
n3=$(grep -n "^## Entry 4" $R/docs/si/P-ACYC-fixes.md | cut -d: -f1); head -n $((n3 - 2)) $R/docs/si/P-ACYC-fixes.md > "$t/f123"
s5=$(sha1sum $R/docs/si/P-ACYC-line-L5.txt | cut -c1-40); b5=$(wc -c < $R/docs/si/P-ACYC-line-L5.txt)
python3 -I -B mkfix4.py $R "$s5" "$b5" "$t/f123" > "$t/e4"; cat "$t/f123" "$t/e4" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-ACYC-fixes.md | cmp -s - "$t/f"
rm -rf "$t"
echo "P-ACYC fix4 checks: PASS"
