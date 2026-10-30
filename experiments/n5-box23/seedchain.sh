#!/bin/bash
# Box 23 (c): seeded chain. Each n starts from the previous n's best (padded with Even self-loops), so the value is seed-dominated
# (a lower bound on the true max at that n, not an independent sample). Usage: SECS=1800 FAM=chain seedchain.sh SEED SEEDPG:START N1 N2 ...
D=$(dirname "$0"); S=$1; P=$2; shift 2
for n in "$@"; do
  o="$D/climbs/rs_${FAM:-chain}_n${n}_r${S}"
  grep -q '^END' "$o.log" 2>/dev/null || python3 "$D/climb23.py" "$n" "$S" --secs "${SECS:-1800}" $EXTRA --seed-pg "$P" --out "$o" > "$o.log" 2>&1
  echo "$(date -u +%H:%M:%SZ) $(tail -1 "$o.log")"; P="$o.pg:$o.start"
done
