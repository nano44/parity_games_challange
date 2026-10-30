#!/bin/bash
# Box 23: exh23.py N in PARTS resumable parts (skips parts whose JSON exists). Usage: JOBS=3 run_parts.sh N PARTS [extra exh23 args]
N=$1; P=$2; shift 2; D=$(dirname "$0"); mkdir -p "$D/results/parts"
for ((k = 0; k < P; k++)); do
  f="$D/results/parts/C${N}${TAG}_p${k}of${P}.json"
  [ -s "$f" ] && continue
  python3 "$D/exh23.py" "$N" --every "$P" --offset "$k" --split 4 --jobs "${JOBS:-4}" --out "$f" "$@" > "$f.log" 2>&1
  echo "part $k exit $?: $(grep RESULT "$f.log" | cut -c1-300)"
done
