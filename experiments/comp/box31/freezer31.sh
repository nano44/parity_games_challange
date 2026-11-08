#!/bin/bash
# L-COMP 12 box 31: every 60 s scan the live LJ lane files (out/L7*_u*.txt, out/L7*_best.txt). A genome with lj_caps >= 7 and LJ score
# key K = floor(score / 1e5) (= caps, gate, -npaths, -n1, T/10: drops F(J) and T's last digit) greater than every K frozen so far FOR THE SAME LANE (L-COMP 12 02:5xZ: per lane, since LJSLACK lanes use another encoding) is copied
# to out/L7_FRZ_K<K>_<lane>.txt (a name no climb writes) with a line (UTC, file, K, sha1, npaths, n1, T, F vector) in out/FROZEN.txt.
# Restart-safe: the per-lane max is re-read from FROZEN.txt each time. HITs (F(0..7) exact) are written by lane31.sh to out/HITS.txt.
cd "$(dirname "$0")"
while true; do
  for g in out/L7*_u*.txt out/L7*_best.txt; do
    [ -f "$g" ] || continue; case "$g" in *FRZ*|*HIT*) continue;; esac; ln=$(tail -1 "$g")
    echo "$ln" | grep -Eq "lj_J 7 lj_caps ([7-9]|[1-9][0-9]) " || continue
    sc=$(echo "$ln" | awk '{print $3}'); [ -n "$sc" ] && [ "$sc" -gt 0 ] || continue; K=$((sc / 100000))
    lane=$(basename "$g" .txt | sed 's/_u[0-9]*$//; s/_best$//')
    M=$(awk -v L="_${lane}.txt" 'index($2, L) && substr($2, length($2) - length(L) + 1) == L {print $3}' out/FROZEN.txt 2>/dev/null | sort -n | tail -1); M=${M:--1}
    [ "$K" -gt "$M" ] || continue
    o=out/L7_FRZ_K${K}_${lane}.txt; cp "$g" "$o"
    [ "$(tail -1 "$o" | awk '{print $3}')" = "$sc" ] || { rm -f "$o"; continue; }
    echo "$(date -u +%FT%TZ) $o $K sha1 $(sha1sum < "$o" | cut -c1-40) $(tail -1 "$o" | grep -o 'lj_npaths [0-9]* lj_n1 [0-9]*') $(tail -1 "$o" | grep -o 'T [0-9]* F [-0-9 ]*moves' | sed 's/ moves//')" >> out/FROZEN.txt
  done; sleep 60; done
