#!/bin/bash
# Box 24: |F|-fitness climbs (n5-box23/climb23.py --fit F), free start pair or --s3. Usage: SECS=900 FAM=F climbs24.sh SEED N ...
D=$(cd "$(dirname "$0")" && pwd); mkdir -p "$D/climbs"
for n in "${@:2}"; do
  o="$D/climbs/${FAM:-F}_n${n}_r$1"; grep -q '^END' "$o.log" 2>/dev/null && continue
  python3 "$D/../n5-box23/climb23.py" "$n" "$1" --fit F --secs "${SECS:-900}" $EXTRA --out "$o" > "$o.log" 2>&1
  echo "$(date -u +%H:%M:%SZ) $(tail -1 "$o.log")"
done
