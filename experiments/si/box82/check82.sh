#!/usr/bin/env bash
# L-SI box 82 CYCLIC TOWERS (docs/si/box82-cyctower.md) self-check (~1 min): pins --strict (HS2_d3 baseline, climb-best genomes, the K = 2
# scan output); re-runs the K = 1 mutation scan of HS2_d3, the per-level anatomy (anal82.py), the real runners (box81/real81.py) and
# the ascent census of best_R_d5_s3 (box81/census81.py --loc) and diffs them with the frozen outputs. The climbs and the K = 2 scan are
# not re-run (minutes; commands in the note).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I -B scan82.py inst/HS2_d3.json 1 ../box81 > "$t/s"; diff -q "$t/s" out/scan82_HS2_K1.out
for f in out/climbKF/best_kf_d6_s1.json out/climbR/best_R_d6_s1.json out/climbR/best_R_d6_s2.json out/climbR/best_R_d5_s3.json; do
  python3 -I -B anal82.py $f ../box81
done > "$t/a"
diff -q "$t/a" out/anal82.out
python3 -I -B ../box81/real81.py out/climbKF/best_kf_d6_s1.json out/climbR/best_R_d6_s2.json > "$t/r"; diff -q "$t/r" out/real82.out
python3 -I -B ../box81/census81.py --loc out/climbR/best_R_d5_s3.json > "$t/c"; diff -q "$t/c" out/census_R_d5_s3.out
rm -rf "$t"
grep -q "KF \[2, 6, 14," out/anal82.out
echo "box 82 checks: PASS"
