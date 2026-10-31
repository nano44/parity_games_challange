#!/bin/bash
# Box 24: root-map climbs, serial. Usage: SECS=900 FIT=pxr FAM=pxr climbs24b.sh SEED N ...   (EXTRA passes e.g. --seed-pg)
D=$(cd "$(dirname "$0")" && pwd); mkdir -p "$D/climbs"
for n in "${@:2}"; do
  o="$D/climbs/${FAM:-$FIT}_n${n}_r$1"; grep -q '^END' "$o.log" 2>/dev/null && continue
  python3 "$D/climb24.py" "$n" "$1" --fit "$FIT" --secs "${SECS:-900}" $EXTRA --out "$o" > "$o.log" 2>&1
  echo "$(date -u +%H:%M:%SZ) $(tail -1 "$o.log")"
done
