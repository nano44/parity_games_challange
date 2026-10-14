#!/usr/bin/env bash
# Re-run every M1 family sweep. Results (csv/md/png) go to results/. Bounded: each run has a timeout; a solver that
# times out is skipped at larger sizes. Usage: ./run_all.sh [family ...]   (default: all)
set -uo pipefail
cd "$(dirname "$0")"
O=../../tools/oink/build
T=20
fam() { local name="$1"; shift; if [ -n "${ONLY:-}" ] && ! [[ " $ONLY " == *" $name "* ]]; then return; fi
        echo "=== $name"; python3 sweep.py "$name" --timeout $T "$@" | tail -3; }
ONLY="${*:-}"
# Oink generators (github.com/trolando/oink @ 8fbf0a7, src/tools/*.cpp)
fam tc            --gen "$O/tc {N}"            --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 \
  -s oink-tl oink-zlk oink-uzlk oink-rr oink-dp oink-fpi oink-tspm oink-zlkq oink-rtl oink-psi
fam tc+           --gen "$O/tc+ {N}"           --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 \
  -s oink-rtl oink-tl oink-zlk oink-ortl oink-psi
fam counter_symsi --gen "$O/counter_symsi {N}" --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-ssi oink-uzlk oink-psi oink-tl
fam counter_rr    --gen "$O/counter_rr {N}"    --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-rr oink-rrdp oink-zlk oink-tl oink-psi
fam counter_dp    --gen "$O/counter_dp {N}"    --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-dp oink-pp oink-zlk oink-tl oink-psi
fam counter_m     --gen "$O/counter_m {N}"     --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-pp oink-dp oink-rr oink-zlk oink-tl oink-psi
fam counter_core  --gen "$O/counter_core {N}"  --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-uzlk oink-zlk oink-zlkpp-std oink-tl oink-psi
fam counter_rob   --gen "$O/counter_rob {N}"   --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 \
  -s oink-uzlk oink-zlk oink-zlkpp-std oink-tl oink-psi
fam counter_ortl  --gen "$O/counter_ortl {N}"  --sizes 2 4 6 8 10 12 14 16 18 20 24 28 32 40 \
  -s oink-ortl oink-rtl oink-tl oink-psi
# counter_qpt is solved by Oink's preprocessing; the -raw variants switch it off so the solver sees the game.
fam counter_qpt   --gen "$O/counter_qpt {N}"   --sizes 2 4 8 16 32 64 128 256 512 \
  -s oink-qpt-raw oink-sspm-raw oink-zlk-raw oink-tl-raw
# PGSolver generators, Python port (pgsolver_port.py; github.com/tcsprojects/pgsolver @ d3cd624); -raw as above.
fam recursiveladder --gen "python3 pgsolver_port.py recursiveladder {N}" --sizes 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 34 38 \
  -s oink-uzlk-raw oink-zlk-raw oink-zlkpp-std-raw oink-tl-raw oink-psi-raw
fam switchallexp  --gen "python3 pgsolver_port.py switchallexp {N}"  --sizes 1 2 4 8 16 32 64 \
  -s oink-psi-raw oink-ssi-raw oink-zlk-raw oink-tl-raw
fam switchbestexp --gen "python3 pgsolver_port.py switchbestexp {N}" --sizes 1 2 4 8 16 32 64 \
  -s oink-psi-raw oink-ssi-raw oink-zlk-raw oink-tl-raw
