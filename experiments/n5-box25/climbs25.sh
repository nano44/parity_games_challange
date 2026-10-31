#!/bin/bash
# Box 25: INS climbs, serial. Usage: SECS=900 FAM=fresh climbs25.sh SEED N ...   (EXTRA e.g. "--seed-pg seeds/X.pg[:START]")
D=$(cd "$(dirname "$0")" && pwd); mkdir -p "$D/climbs"
for n in "${@:2}"; do
  o="$D/climbs/${FAM:-fresh}_n${n}_r$1"; grep -q '^END' "$o.log" 2>/dev/null && continue
  python3 "$D/climb25.py" "$n" "$1" --secs "${SECS:-900}" $EXTRA --out "$o" > "$o.log" 2>&1
  echo "$(date -u +%H:%M:%SZ) $(tail -1 "$o.log")"
done
