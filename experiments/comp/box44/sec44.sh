#!/bin/bash
# L-COMP box 44 item 3: every climb best (out/climb44/BEST_*.json) on a SECOND engine: L-NEW's n5v (claude/l-new 311bbf81
# box208/level208.py --g3: N5'-xi from S3 on Γ3(G) to its first fallback; «T» = T3), run unchanged with python3 -I from its own directory.
# One line per best appended to out/sec44.out (resumable). env LNEW209 = an archive of claude/l-new 311bbf81.
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
: "${LNEW209:?set LNEW209}"; D="$LNEW209/experiments/new/box208"; O=$(pwd)/out/sec44.out; touch "$O"
for f in $(pwd)/out/climb44/BEST_*.json; do
  b=$(basename $f); grep -q "^$b " "$O" && continue
  (cd "$D" && python3 -I level208.py --g3 "$f") >> "$O" 2>&1
done
echo "sec44 done: $(wc -l < "$O") rows"
}
main "$@"
