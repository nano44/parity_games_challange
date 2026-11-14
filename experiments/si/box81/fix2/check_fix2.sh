#!/usr/bin/env bash
# L-SI P-ACYC fixes entry 2 self-check (called by box81/check81.sh): L-3 rebuilt from L-2 by mkL3.py and compared byte for byte; the
# fixes file must equal entry 1 (fix1/mkfix1.py) followed by entry 2 (mkfix2.py); later entries may follow.
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d)
python3 -I -B mkL3.py $R > "$t/L3"; cmp -s "$t/L3" $R/docs/si/P-ACYC-line-L3.txt
s2=$(sha1sum $R/docs/si/P-ACYC-line-L2.txt | cut -c1-40); b2=$(wc -c < $R/docs/si/P-ACYC-line-L2.txt)
python3 -I -B ../fix1/mkfix1.py $R "$s2" "$b2" > "$t/e1"
s3=$(sha1sum $R/docs/si/P-ACYC-line-L3.txt | cut -c1-40); b3=$(wc -c < $R/docs/si/P-ACYC-line-L3.txt)
python3 -I -B mkfix2.py $R "$s3" "$b3" "$t/e1" > "$t/e2"; cat "$t/e1" "$t/e2" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-ACYC-fixes.md | cmp -s - "$t/f"
rm -rf "$t"
echo "P-ACYC fix2 checks: PASS"
