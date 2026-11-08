#!/usr/bin/env bash
# L-RED 58 R223 item 1: re-run R222's end222.py (9 families) on P-N5-END's FROZEN tools (claude/l-new 131b4c1c).
# Needs env WT = WT3 = a worktree of claude/l-new 131b4c1c0b98cca2c0b40f6e9cf96c840a4deb25 (git worktree add --detach <dir> <sha>).
# Usage: sweep_end223.sh SEED COUNT OUTDIR
set -u
: "${WT:?}"; : "${WT3:?}"
here=$(cd "$(dirname "$0")" && pwd); seed=$1; cnt=$2; out=$3; mkdir -p "$out"
for fam in rand esc noesc deep dense lvl0 late self wide; do
  python3 "$here/../r222/end222.py" "$fam" "$seed" "$cnt" "$out/end_$fam.txt" > "$out/end_$fam.log" 2>&1; echo "$fam exit $?"
done
CTRL=1 python3 "$here/../r222/end222.py" rand "$seed" 100 "$out/ctrl_rand.txt" > "$out/ctrl_rand.log" 2>&1; echo "ctrl exit $?"
