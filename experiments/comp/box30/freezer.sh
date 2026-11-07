#!/bin/bash
# L-COMP box 30 (Lead 20:5xZ item 2): every 20 s, scan the live L6 lane files (out/D_l6z_*, out/D_l6h_*); any genome with l6_caps 6,
# l6_npaths 0 and F(6) greater than every F(6) frozen so far (start: 238) is copied to out/L6_FRZ_F<F6>_<lane>.txt (a name no climb
# writes) with a line (UTC, file, sha1, F vector, T) in out/FROZEN.txt. Restart-safe: the running max is re-read from FROZEN.txt.
cd "$(dirname "$0")"
while true; do
  M=$(awk '{print $4}' out/FROZEN.txt 2>/dev/null | sort -n | tail -1); M=${M:-238}
  for g in out/D_l6z_u*.txt out/D_l6z_best.txt out/D_l6h_u*.txt out/D_l6h_best.txt out/D_l6w_u*.txt out/D_l6w_best.txt; do
    [ -f "$g" ] || continue; ln=$(tail -1 "$g")
    echo "$ln" | grep -Eq "l6_caps 6 l6_q5 [0-9]+ l6_npaths 0( l6_len1w6 [0-9]+)?$" || continue
    f6=$(echo "$ln" | awk '{for(i=1;i<=NF;i++) if($i=="F"){print $(i+7); exit}}')
    [ -n "$f6" ] && [ "$f6" -gt "$M" ] || continue
    lane=$(basename "$g" .txt | sed 's/_u[0-9]*\(_killed\)\?$//; s/_best$//'); o=out/L6_FRZ_F${f6}_${lane}.txt; cp "$g" "$o"
    grep -Eq "l6_npaths 0( l6_len1w6 [0-9]+)?$" "$o" || { rm -f "$o"; continue; }
    echo "$(date -u +%FT%TZ) $o F6 $f6 sha1 $(sha1sum < "$o" | cut -c1-40) $(tail -1 "$o" | grep -o 'T [0-9]* F [-0-9 ]*moves' | sed 's/ moves//')" >> out/FROZEN.txt; M=$f6
  done; sleep 20; done
