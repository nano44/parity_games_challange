#!/bin/bash
# L-RED successor 25 (R105): verify a SEG-COUNT kill pin. sha1 of game and start; n5b SPEC (L-COMP) and n5.py (L-NEW driver, L-SI si.py
# engine) from the start, state sequences compared (xeng.py); both final solutions checked by Oink zlk + both strategies (check_sol2);
# my segment checker (segchk.py); L-SI's lay/relcheck.py at each deadlock step and lay/segsw.py, lay/wsink.py.
# Usage: experiments/red/seg/vrun.sh GAME.pg START a b "t1 t2 ..."   (run from the repo root)
g=$1; s=$2; a=$3; b=$4; out=$(mktemp -d)
echo "game $g sha1 $(sha1sum < "$g" | cut -c1-40)"; echo "start $s sha1 $(sha1sum < "$s" | cut -c1-40)"
python3 experiments/n5-second/n5b.py "$g" $out/b.sol --start "$s" --mode spec
python3 experiments/new/n5.py n5 "$g" $out/a.sol --start "$(grep SIGMA0 $s)" "$(grep TAU0 $s)"
python3 experiments/red/seg/xeng.py "$g" "$s"
echo "n5b solution: $(python3 experiments/new/check_sol2.py "$g" $out/b.sol)"
echo "n5.py solution: $(python3 experiments/new/check_sol2.py "$g" $out/a.sol)"
python3 experiments/red/seg/segchk.py "$g" "$s" -v
for t in $5; do echo "--- L-SI lay/relcheck.py $a $b $t"; python3 experiments/si/lay/relcheck.py "$g" "$s" $a $b $t; done
echo "--- L-SI lay/segsw.py"; python3 experiments/si/lay/segsw.py --one "$g" "$s" | grep -v EXAMPLE
echo "--- L-SI lay/wsink.py"; python3 experiments/si/lay/wsink.py --one "$g" "$s" | grep -v EXAMPLE
rm -rf $out
