#!/usr/bin/env bash
# switchbestexp against the ported PGSolver switch-best strategy improvement (pgsolver_si.py --switchbest).
set -uo pipefail
cd "$(dirname "$0")"
python3 sweep.py switchbestexp-pgsbest --gen "python3 pgsolver_port.py switchbestexp {N}" --sizes 1 2 3 4 5 6 7 8 \
  -s pgs-switchbest --timeout 600 | tail -2
