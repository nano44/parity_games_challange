#!/usr/bin/env bash
# Box 3 N1 killer candidate "deep traps": Friedmann's switchallexp (experiments/hard-families/pgsolver_port.py, deterministic) plus
# a trap at every Even vertex with >= 2 successors (alltrap.py: t_v Odd, even priority P = B + 2 + 2k -> c_v Odd self-loop, odd
# priority B + 1; B = max original priority rounded up to even), with k = floor(B_max / 2) + 2, so P - q = 2k + 1 > B + 2: the traps
# release (n^P vs H n^q) only after the horizon at which the original game's discounted order equals its parity order.
# Usage: gen_deeptrap.sh N > game.pg
cd "$(dirname "$0")"; set -e
t=$(mktemp); python3 ../hard-families/pgsolver_port.py switchallexp "$1" > "$t"
B=$(python3 -c "import sys; sys.path.insert(0,'../harness'); import pg; print(max(pg.read('$t').prio))")
python3 alltrap.py "$t" $(( B / 2 + 2 )); rm -f "$t"
