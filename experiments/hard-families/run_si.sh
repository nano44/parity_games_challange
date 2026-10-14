#!/usr/bin/env bash
# Friedmann's SI families against the ported PGSolver switch-all strategy improvement (pgsolver_si.py).
set -uo pipefail
cd "$(dirname "$0")"
python3 sweep.py switchallexp-pgs --gen "python3 pgsolver_port.py switchallexp {N}" --sizes 1 2 3 4 5 6 7 8 9 10 \
  -s pgs-switchall oink-psi-raw oink-zlk-raw --timeout 300 | tail -2
python3 sweep.py switchbestexp-pgs --gen "python3 pgsolver_port.py switchbestexp {N}" --sizes 1 2 3 4 5 6 7 8 \
  -s pgs-switchall oink-psi-raw oink-zlk-raw --timeout 300 | tail -2
