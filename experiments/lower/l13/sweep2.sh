#!/bin/bash
# L-LOWER 13: all-pairs helper sweep at ONE prefix P (pgad3). For each pair h1 < h2 of helper movers in HLIST (G = [h1, h2]):
# RESULT at prefix P. Worker W of NW takes pairs with index % NW == W. Usage: sweep2.sh BASE TARGET XS HLIST P W NW OUT [TLIM]
B=$1; C=$2; XS=$3; HL=$4; P=$5; W=$6; NW=$7; OUT=$8; TL=${9:-1800}; cd "$(dirname "$0")"
python3 -c "import sys
o=[]
for p in sys.argv[1].split(','):
    a,b=(p.split('-')+[p])[:2]; o+=range(int(a),int(b)+1)
i=0
for x in range(len(o)):
    for y in range(x+1,len(o)):
        if i % int(sys.argv[3]) == int(sys.argv[2]): print(o[x], o[y])
        i+=1" $HL $W $NW | while read a b; do
  tag="$(basename $B .txt) XS $XS G $a,$b prefix $P"; grep -qF "$tag " $OUT 2>/dev/null && continue
  q=$(timeout $TL python3 pgad3.py $B $C $P $XS $a,$b out/pp_${W} 2>&1 | grep -E "RESULT|CHECK|SOLVE" | tr '\n' ' ')
  case "$q" in *MISMATCH*) r=MISMATCH;; *UNSAT*) r=UNSAT;; *"RESULT SAT"*) r=SAT; cp out/pp_${W}_dec.txt out/PAIRSAT_${a}_${b}_P${P}_dec.txt;; *) r=NO_ANSWER;; esac
  echo "$tag  $r  ($q)" >> $OUT
done
