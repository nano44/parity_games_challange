#!/bin/bash
# Box 23 (c): fresh climbs, serial (one core). Usage: SECS=900 climbs.sh SEED N1 N2 ...   (skips finished logs)
D=$(dirname "$0"); S=$1; shift
for n in "$@"; do
  o="$D/climbs/rs_${FAM:-fresh}_n${n}_r${S}"
  grep -q '^END' "$o.log" 2>/dev/null && continue
  python3 "$D/climb23.py" "$n" "$S" --secs "${SECS:-900}" $EXTRA --out "$o" > "$o.log" 2>&1
  echo "$(date -u +%H:%M:%SZ) $(tail -1 "$o.log")"
done
