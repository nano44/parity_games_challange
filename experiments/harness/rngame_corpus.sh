#!/usr/bin/env bash
# Oink rngame corpus. rngame seeds from std::random_device, so instances are NOT reproducible from parameters:
# the games themselves are the record. Writes DIR/*.pg and DIR/manifest.csv (file,params,sha256).
# Usage: rngame_corpus.sh DIR COUNT NMAX    (params per game drawn by a seeded bash RANDOM=COUNT*NMAX)
set -euo pipefail
DIR="$1"; COUNT="$2"; NMAX="$3"
RNG="$(cd "$(dirname "$0")/../.." && pwd)/tools/oink/build/rngame"
mkdir -p "$DIR"; echo "file,n,maxprio,mindeg,maxdeg,selfloops,sha256" > "$DIR/manifest.csv"
RANDOM=$((COUNT * NMAX))
for i in $(seq 0 $((COUNT - 1))); do
  n=$((2 + RANDOM % (NMAX - 1))); p=$((RANDOM % (n + 2))); lo=$((1 + RANDOM % 3)); [ $lo -gt $n ] && lo=$n
  hi=$((lo + RANDOM % 4)); [ $hi -gt $n ] && hi=$n; sl=$((RANDOM % 2))
  f=$(printf "rn%05d_n%d_p%d_deg%d-%d_sl%d.pg" "$i" "$n" "$p" "$lo" "$hi" "$sl")
  if [ $sl -eq 1 ]; then "$RNG" "$n" "$p" "$lo" "$hi" > "$DIR/$f"; else
    [ $hi -ge $n ] && hi=$((n - 1)); [ $lo -gt $hi ] && lo=$hi; "$RNG" "$n" "$p" "$lo" "$hi" x > "$DIR/$f"; fi
  echo "$f,$n,$p,$lo,$hi,$sl,$(sha256sum "$DIR/$f" | cut -c1-16)" >> "$DIR/manifest.csv"
done
echo "wrote $COUNT rngame games to $DIR"
