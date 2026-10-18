#!/usr/bin/env bash
# Box 3 N2 killer: switchallexp(N) (pgsolver_port.py) padded with one isolated self-loop dummy per priority (pad_prio.py), so
# priority compression merges nothing. Usage: gen_padsae.sh N > game.pg
cd "$(dirname "$0")"; set -e; t=$(mktemp); python3 ../hard-families/pgsolver_port.py switchallexp "$1" > "$t"; python3 pad_prio.py "$t"; rm -f "$t"
