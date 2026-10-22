#!/usr/bin/env bash
# L-RED box 10 (produced on Opus 5.5): sweep the uniform R39 family lagfam.py over D. Per D: n, sha1, max depth and max k by
# L-ALG dtl_stealdepth.py UNMODIFIED in both order data, pinned Oink iterations + verification, dtl_flipflop vs Oink.
# LALG_DIR = detached claude/l-alg checkout. Usage: famsweep.sh OUTDIR D1 D2 ...
set -u; out="$1"; shift; mkdir -p "$out"; here="$(cd "$(dirname "$0")" && pwd)"; red="$here/.."; oink="$red/../../tools/oink/build/oink"
for D in "$@"; do
  f="$out/fam_D$D.pg"; python3 "$here/lagfam.py" "$D" "$f"; n=$(($(head -1 "$f" | tr -dc 0-9) + 1)); row="D=$D n=$n sha1=$(sha1sum "$f" | cut -c1-12)"
  for o in stable oink; do
    r=$(cd "$LALG_DIR/experiments/alg" && RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=$o python3 dtl_stealdepth.py "$f" 2>&1 | grep -E '^max|INCOMPLETE' | tr '\n' ' ')
    row="$row | $o: $r"
  done
  row="$row | oink: $("$oink" --dtl --no-single --no-wcwc --no-loops -v "$f" 2>&1 | grep -E 'solved in|verified' | sed 's/.*] //' | tr '\n' ' ')"
  row="$row | $(python3 -I "$red/dtl/dtl_flipflop.py" "$f" --quiet --oink "$oink" 2>&1 | tail -1)"
  echo "$row"
done
