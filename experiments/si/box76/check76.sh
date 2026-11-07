#!/usr/bin/env bash
# L-SI box 76 (TROPICAL-WINDOW; docs/si/N5-TROPICAL-box76.md) self-check (~60 s): pins (--strict) of tools, corpus, instances and
# frozen outputs; tw.py .. tw4.py reproduce their outputs byte for byte; the violation counters of ALT-MIN / HIT / MONO are 0; the
# DEAD instances replay (dead76.py asserts every number it prints).
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I -B tw.py > "$t/tw"
diff -q "$t/tw" tw.out
python3 -I -B tw2.py > "$t/tw2"
diff -q "$t/tw2" tw2.out
python3 -I -B tw3.py > "$t/tw3"
diff -q "$t/tw3" tw3.out
python3 -I -B tw4.py > "$t/tw4"
diff -q "$t/tw4" tw4.out
python3 -I -B tw5.py > "$t/tw5"
diff -q "$t/tw5" tw5.out
python3 -I -B tw5.py inst/lred/*.json > "$t/tw5l"
diff -q "$t/tw5l" tw5_lred.out
python3 -I -B dead76.py > "$t/dead"
diff -q "$t/dead" dead76.out
python3 -I -B replay77.py > "$t/r77"
diff -q "$t/r77" replay77.out
python3 -I -B tower77.py inst/lower/REC_d10_tower_mu30.json > "$t/tow"
diff -q "$t/tow" tower77.out
python3 -I -B fuel77.py inst/lower/REC_d10_tower_mu30.json > "$t/fuel"
diff -q "$t/fuel" fuel77.out
NEG=2 python3 -I -B tw4.py > "$t/n2"
diff -q "$t/n2" tw4_neg2.out
python3 -I -B append77.py inst/climbR_d4_s6.json 11011111 "$t/pf.json" > "$t/app"
diff -q "$t/app" <(sed "s|inst/passfreeze77_d5.json|$t/pf.json|" append77.out)
cmp "$t/pf.json" inst/passfreeze77_d5.json
rm -rf "$t"
grep -q "^INFO HIT_VIOL 238546 " tw4_neg2.out
grep -q "MONO_VIOL 226066 " tw3_neg2.out
grep -q "^INFO ALT 0 ALT_TIGHT 112372 MONO_VIOL 0 MOVEALT 0 MOVEALT_TIGHT 7085 RMV 0 TO_k 0 movers 577740 runs 63223$" tw3.out
grep -q "^INFO HIT_VIOL 0 pairs 577740$" tw4.out
grep -q "^INFO DBLEQ_VIOL 0 NONTRIVIAL_CONSEC 0 " tw5.out
grep -q "^INFO DBLEQ_VIOL 0 NONTRIVIAL_CONSEC 0 doubling levels 5396 " tw5_lred.out
grep -q "^INFO files 208 runs 63223 steps 140395$" tw.out
echo "box 76 TROPICAL-WINDOW checks (ALT-MIN, HIT, window tables, DBL-EQ, DBL-GAP data, DEAD SUM-COUPLE / RISE-N / SPAWN-2 replays, box 77 replays + NEG control + PASS-FREEZE): PASS"
