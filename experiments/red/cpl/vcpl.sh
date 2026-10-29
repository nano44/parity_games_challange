#!/bin/bash
# L-RED successor 27: verify a coupled pin. sha1 of game and start; n5b SPEC (L-COMP) and n5.py (L-NEW driver on L-SI si.py) from the
# start, state sequences compared (seg/xeng.py); both final solutions checked by Oink zlk + both strategies (new/check_sol2.py);
# per-joint-lambda-run counts (cpl.py). With START = S3 the game is run from the SPEC S3 default start (no start file).
# Usage (repo root): experiments/red/cpl/vcpl.sh GAME.pg START|S3
g=$1; s=$2; out=$(mktemp -d)
echo "game $g sha1 $(sha1sum < "$g" | cut -c1-40)"
if [[ "$s" == S3 ]]; then
  python3 experiments/n5-second/n5b.py "$g" $out/b.sol --mode spec
  python3 experiments/new/n5.py n5 "$g" $out/a.sol
else
  echo "start $s sha1 $(sha1sum < "$s" | cut -c1-40)"
  python3 experiments/n5-second/n5b.py "$g" $out/b.sol --start "$s" --mode spec
  python3 experiments/new/n5.py n5 "$g" $out/a.sol --start "$(grep SIGMA0 $s)" "$(grep TAU0 $s)"
  python3 experiments/red/seg/xeng.py "$g" "$s"
fi
echo "n5b solution: $(python3 experiments/new/check_sol2.py "$g" $out/b.sol)"
echo "n5.py solution: $(python3 experiments/new/check_sol2.py "$g" $out/a.sol)"
python3 experiments/red/cpl/cpl.py "$g" "$s"
rm -rf $out
