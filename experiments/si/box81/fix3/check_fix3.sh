#!/usr/bin/env bash
# L-SI P-ACYC fixes entry 3 self-check (called by box81/check81.sh): L-4 rebuilt from L-3 by mkL4.py and compared byte for byte; the
# fixes file must equal entries 1-2 (as check_fix2.sh rebuilds them) followed by entry 3 (mkfix3.py); later entries may follow.
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
t=$(mktemp -d)
python3 -I -B mkL4.py $R > "$t/L4"; cmp -s "$t/L4" $R/docs/si/P-ACYC-line-L4.txt
s2=$(sha1sum $R/docs/si/P-ACYC-line-L2.txt | cut -c1-40); b2=$(wc -c < $R/docs/si/P-ACYC-line-L2.txt)
python3 -I -B ../fix1/mkfix1.py $R "$s2" "$b2" > "$t/e1"
s3=$(sha1sum $R/docs/si/P-ACYC-line-L3.txt | cut -c1-40); b3=$(wc -c < $R/docs/si/P-ACYC-line-L3.txt)
python3 -I -B ../fix2/mkfix2.py $R "$s3" "$b3" "$t/e1" > "$t/e2"; cat "$t/e1" "$t/e2" > "$t/f12"
s4=$(sha1sum $R/docs/si/P-ACYC-line-L4.txt | cut -c1-40); b4=$(wc -c < $R/docs/si/P-ACYC-line-L4.txt)
python3 -I -B mkfix3.py $R "$s4" "$b4" "$t/f12" > "$t/e3"; cat "$t/f12" "$t/e3" > "$t/f"; n=$(wc -c < "$t/f")
head -c "$n" $R/docs/si/P-ACYC-fixes.md | cmp -s - "$t/f"
rm -rf "$t"
echo "P-ACYC fix3 checks: PASS"
