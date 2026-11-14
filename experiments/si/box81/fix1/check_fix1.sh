#!/usr/bin/env bash
# L-SI P-ACYC fixes entry 1 self-check (called by box81/check81.sh): pins (referee report copies, L-2); pacyc81t (W-3 (a), D-1, D-4)
# and tn81 (AC-2) re-run and diffed; L-2 rebuilt by mkL2.py and compared byte for byte; fixes entry 1 rebuilt by mkfix1.py and compared
# with the head of docs/si/P-ACYC-fixes.md (append-only: later entries follow).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../..
sha1sum -c --quiet --strict fix1.sha1
t=$(mktemp -d)
python3 -I -B pacyc81t.py 0 1 $(for i in H5_d20_F62 H6_d24_F126 SL41_d28 L6Z_KILL238_d28; do echo ../inst/$i.json; done) > "$t/a"; diff -q "$t/a" pacyc81t_towers.out
python3 -I -B pacyc81t.py 0 1 ../inst/rd2_d3.json ../inst/rd2_d4.json ../inst/rd3_d3.json ../inst/rf_d4.json ../inst/RS2.json > "$t/a"; diff -q "$t/a" pacyc81t_cyclic_control.out
python3 -I -B pacyc81t.py 300 7 > "$t/a"; diff -q "$t/a" pacyc81t_agen_300_7.out
python3 -I -B tn81.py > "$t/a"; diff -q "$t/a" tn81.out
python3 -I -B mkL2.py $R > "$t/L2"; cmp -s "$t/L2" $R/docs/si/P-ACYC-line-L2.txt
s=$(sha1sum $R/docs/si/P-ACYC-line-L2.txt | cut -c1-40); b=$(wc -c < $R/docs/si/P-ACYC-line-L2.txt)
python3 -I -B mkfix1.py $R "$s" "$b" > "$t/f"; n=$(wc -c < "$t/f"); head -c "$n" $R/docs/si/P-ACYC-fixes.md | cmp -s - "$t/f"
rm -rf "$t"
echo "P-ACYC fix1 checks: PASS"
