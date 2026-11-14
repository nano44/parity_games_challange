#!/usr/bin/env bash
# L-SI box 84 milestone 3 (i): regenerate the frozen LOW instances (low84.py on HP2_mup) into inst/ (or $1).
set -euo pipefail; cd "$(dirname "$0")"; O=${1:-inst}
python3 -I -B low84.py ../inst/HP2_mup.json 2 M2 0 $O/LO2_priv.json
python3 -I -B low84.py ../inst/HP2_mup.json 2 B2 0 $O/LO2_nopriv.json
