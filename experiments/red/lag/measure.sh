#!/usr/bin/env bash
# L-RED box 10 (produced on Opus 5.5): run L-ALG's UNMODIFIED tools on G.pg in both order data and print the box-10 targets:
# phases (dtl_spp), max re-steal depth (dtl_stealdepth), max exits per (context, step, vertex) (dtl_prefexits), first-difference
# contexts per phase (dtl_rootmono). LALG_DIR = a detached checkout of claude/l-alg (box 10: e0fc1bb0). Usage: measure.sh G.pg
set -u; A="$LALG_DIR/experiments/alg"; G="$(readlink -f "$1")"
echo "sha1 $(sha1sum "$G" | cut -c1-12)  l-alg $(git -C "$LALG_DIR" rev-parse --short=8 HEAD)"
for o in stable oink; do
  export DTL_ORDER=$o RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0
  ph=$(SPP_ROWS=1 python3 "$A/dtl_spp.py" "$G" 2>&1 | tail -n +1 | grep -o "S=[0-9]*" | tr '\n' ' ')
  sd=$(python3 "$A/dtl_stealdepth.py" "$G" 2>&1 | grep -E "^max k|INCOMPLETE")
  pe=$(python3 "$A/dtl_prefexits.py" "$G" 2>&1 | grep -iE "max exits|INCOMPLETE" | head -2 | tr '\n' ' ')
  rm=$(python3 "$A/dtl_rootmono.py" "$G" 2>&1 | grep -E "^distinct first-difference contexts per phase|INCOMPLETE" | sed 's/.*phase (file, contexts, transitions, |G.|)://' | cut -c1-160)
  echo "[$o] phases $ph| $sd | $pe | ctx $rm"
done
