#!/bin/bash
# Box 36 (L-RED): verify one instance: 𝒞^1O assert, sha1, n5.py + n5b.py (iterations), Oink zlk + strategies (check_sol2), sox line.
# Usage: experiments/red/so/vrun.sh game.pg   (run from the repo root)
g=$1; out=$(mktemp -d)
echo "file $g sha1 $(sha1sum < "$g" | cut -c1-40)"
python3 -c "import sys; sys.path.insert(0,'experiments/red/so'); import sox; g=sox.load('$g'); print('C1O odd-choice vertices', sox.oddchoice(g))"
python3 experiments/new/n5.py n5 "$g" $out/a.sol
python3 experiments/n5-second/n5b.py "$g" $out/b.sol
python3 experiments/new/check_sol2.py "$g" $out/a.sol
python3 experiments/red/so/sox.py "$g" | grep -v "^TOTAL"
rm -rf $out
