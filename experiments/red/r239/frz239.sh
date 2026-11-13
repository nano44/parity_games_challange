#!/usr/bin/env bash
# L-RED 68 R239: rf239.py on a list of frozen genomes (one per line in LIST), every rule, one process per (genome, rule) with a timeout
# (TO seconds, default 240); prints one line per pair ("FRZ239 <file> <rule> ..." or "FRZ239 <file> <rule> TIMEOUT") and a total.
# Usage: frz239.sh LIST [RULES]     (the 81 frozen genomes of box 212 §7: git archive 5fa64fe6 of experiments/new/box191..box207, list as run212.sh's ALL)
set -u
LIST=$1; RULES=${2:-howard,allleast,allworst,allrand,subrand,onebest,onerand,oneleast,onefirst,oneworst}; TO=${TO:-240}
D=$(cd "$(dirname "$0")" && pwd); to=0; nz=0; ok=0
for f in $(cat "$LIST"); do
  for r in ${RULES//,/ }; do
    l=$(timeout "$TO" python3 "$D/rf239.py" json "$r" "$f" 2>&1 | grep '^RF239')
    if [ -z "$l" ]; then echo "FRZ239 $(basename "$f") $r TIMEOUT"; to=$((to+1)); continue; fi
    echo "FRZ239 $(basename "$f") ${l#RF239 json 1 }"; ok=$((ok+1))
    m=$(echo "$l" | sed 's/.*must0 \(.*\) | desc.*/\1/' | tr ' ' '\n' | grep -E '^[0-9]+$' | paste -sd+ | bc)
    [ "$m" != "0" ] && nz=$((nz+1))
  done
done
echo "FRZ239 TOTAL pairs checked $ok timeouts $to pairs with a nonzero must-0 counter $nz"
