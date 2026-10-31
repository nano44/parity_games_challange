#!/bin/bash
# Box 24: exh24.py N in PARTS resumable parts. Usage: JOBS=2 run_parts24.sh N PARTS [extra exh24 args]
N=$1; P=$2; shift 2; D=$(dirname "$0"); mkdir -p "$D/results/parts"
for ((k = 0; k < P; k++)); do
  f="$D/results/parts/C${N}_p${k}of${P}.json"; [ -s "$f" ] && continue
  python3 "$D/exh24.py" "$N" --every "$P" --offset "$k" --split 4 --jobs "${JOBS:-4}" --out "$f" "$@" > "$f.log" 2>&1
  echo "part $k exit $?: $(grep RESULT "$f.log" | cut -c1-400)"
done
