#!/bin/sh
# Library run of fbx18.py in 4 parts: lib18.sh LISTFILE OUTDIR. Canonical start (SPEC S3).
L=$1; O=$2; mkdir -p "$O"; D=$(dirname "$0")
for i in 0 1 2 3; do
  awk -v i=$i 'NR % 4 == i' "$L" | xargs timeout 7000 python3 "$D/fbx18.py" > "$O/lib_$i.txt" 2>&1 &
done
wait
