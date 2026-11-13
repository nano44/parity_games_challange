#!/usr/bin/env bash
# L-SI P-N5-GATE fixes entry 1 self-check (called by box95/check95.sh): the frozen packet's sha1; L-1 rebuilt by mkL1.py and compared
# byte for byte; its premise quotes verbatim in their landed RESULTS entries (quotesL1.py); entry 1 rebuilt by mkfix1.py and compared
# with the head of docs/si/P-N5-GATE-fixes.md; the copied L-RED report and the Db / Dbr instances against their sha1s.
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
[ "$(sha1sum < $R/docs/si/P-N5-GATE.md | cut -c1-40)" = f3a584e68b5c998276ea717f42920bdeeca581ab ]
t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
python3 -I -B quotesL1.py $R > "$t/q"; tail -1 "$t/q" | grep -q "quotes: 12 of 12 verbatim"
python3 -I -B mkL1.py $R > "$t/L1"; cmp -s "$t/L1" $R/docs/si/P-N5-GATE-line-L1.txt
s=$(sha1sum < $R/docs/si/P-N5-GATE-line-L1.txt | cut -c1-40); b=$(wc -c < $R/docs/si/P-N5-GATE-line-L1.txt)
python3 -I -B mkfix1.py $R "$s" "$b" > "$t/e1"; n=$(wc -c < "$t/e1")
head -c "$n" $R/docs/si/P-N5-GATE-fixes.md | cmp -s - "$t/e1"
sha1sum -c --quiet --strict fix1.sha1
(cd inst && sha1sum -c --quiet --strict SHA1SUMS)
echo "P-N5-GATE fix1 checks: PASS"
