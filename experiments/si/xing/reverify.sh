#!/usr/bin/env bash
# L-SI box 4: re-verify cited instances: sha1, n5.py n5 (iterations / fallbacks), check_sol2.py (Oink zlk + verify.py strategies).
# Usage: experiments/si/xing/reverify.sh game.pg ...   (writes solutions to experiments/si/xing/out/, gitignored)
set -u
cd "$(git rev-parse --show-toplevel)"
mkdir -p experiments/si/xing/out
for f in "$@"; do
  b=$(basename "$f" .pg); sol=experiments/si/xing/out/$b.sol
  r=$(python3 experiments/new/n5.py n5 "$f" "$sol" | sed 's/.*iterations=\([0-9]*\) fallback=\([0-9]*\).*/\1 \2/')
  c=$(python3 experiments/new/check_sol2.py "$f" "$sol" 120 2>&1 | tail -1)
  printf "%-22s sha1 %s n5 it/fb %s | %s\n" "$b" "$(sha1sum "$f" | cut -c1-8)" "$r" "$c"
done
