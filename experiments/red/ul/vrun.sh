#!/bin/bash
# L-RED successor 22: verify one instance with its start pair: sha1 of game and start, n5.py (SPEC) and n5b.py --mode spec (independent
# implementation) iteration counts from the same start, Oink zlk solution + strategies (check_sol2.py), and ulx.py (UL_C) on the run.
# Usage (repo root): experiments/red/ul/vrun.sh GAME.pg START
g=$1; st=$2; out=$(mktemp -d)
echo "file $g sha1 $(sha1sum < "$g" | cut -c1-40) start sha1 $(sha1sum < "$st" | cut -c1-40)"
python3 experiments/new/n5.py n5 "$g" $out/a.sol --start "$(sed -n 1p "$st")" "$(sed -n 2p "$st")"
python3 experiments/n5-second/n5b.py "$g" $out/b.sol --start "$st" --mode spec | tail -2
python3 experiments/new/check_sol2.py "$g" $out/a.sol
python3 experiments/new/check_sol2.py "$g" $out/b.sol
python3 experiments/red/ul/ulx.py --one "$g" "$st" | grep -E "^UL_C|^U_events|^MAX IDX_SLACK |^MAX LEN_SLACK "
rm -rf $out
