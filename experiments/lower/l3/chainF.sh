#!/usr/bin/env bash
# Resumable lift->climb chain: best text genome at d -> lift.py +1 level -> psearch (all levels mutable) -> best at d+1.
# Usage: chain.sh START.txt d0 d1 iters seed ; outputs ${PFX:-out/chain}_d<d>.txt (best genome), ${PFX:-out/chain}_d<d>.log
set -u
cd "$(dirname "$0")"; SP=${SP:?}; cur=$1; d=$2; d1=$3; it=$4; seed=$5
while [ "$d" -lt "$d1" ]; do
  n=$((d+1)); if [ -s ${PFX:-out/chain}_d$n.txt ]; then cur=${PFX:-out/chain}_d$n.txt; d=$n; continue; fi
  python3 -I lift.py "$cur" 1 ${PFX:-out/chain}_seed_d$n.txt
  $SP/${BIN:-psearch} ${PFX:-out/chain}_seed_d$n.txt $((seed+n)) $it $d 3000000 > ${PFX:-out/chain}_d$n.log 2>&1
  sed -n '/^BEST/,$p' ${PFX:-out/chain}_d$n.log | tail -n +2 > ${PFX:-out/chain}_d$n.tmp && mv ${PFX:-out/chain}_d$n.tmp ${PFX:-out/chain}_d$n.txt
  echo "d $n $(grep ^BEST ${PFX:-out/chain}_d$n.log)"; cur=${PFX:-out/chain}_d$n.txt; d=$n
done
