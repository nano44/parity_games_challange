#!/usr/bin/env bash
# L-SI box 78 self-check (~10 s): landed potentials (pot78.py: PHI_K and EXACT-ENERGY fall at every step, start values), R105 RANK
# (rank78.py) on L-LOWER's records and the box 77 climb record reproduce their frozen outputs; pins --strict.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d)
python3 -I -B pot78.py ../box76/inst/lower/*.json ../box76/inst/climb77_d10_T45.json > "$t/pot"
diff -q "$t/pot" pot78.out
python3 -I -B rank78.py ../box76/inst/lower/*.json ../box76/inst/climb77_d10_T45.json > "$t/rank"
diff -q "$t/rank" rank78.out
rm -rf "$t"
echo "box 78 checks (potentials, RANK): PASS"
