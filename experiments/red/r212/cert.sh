#!/bin/bash
# L-RED R212 CERT: certify a witness genome (fk text) for T_0..T_K. Usage: cert.sh genome.txt K "T_0,..,T_K"
# 1 fk eval; 2 verify.py (r187/ideal.py DP + box 150 Gen segment replay); 3 L-SI flipdp.py (self-checks + XSIM vs Gen);
# 4 embed.py (FROZEN-EMBED on this genome, every state, both c); 5 r189/lemck.py on the full genome at the T_K witness start.
cd "$(dirname "$0")"; g=$1; K=$2; exp=$3; m=$(head -1 "$g" | cut -d' ' -f2); T=${TMPD:-/tmp}; j=$T/cert_$$.json; ok=1
f=$(./fk eval $m < "$g" | cut -d' ' -f2-$((K + 2)) | tr ' ' ','); [[ "$f" == "$exp" ]] || { echo "fk: $f"; ok=0; }
v=$(python3 verify.py "$g" $K "$exp"); echo "$v" | grep -q " MATCH$" && ! echo "$v" | grep -q FAIL || { echo "verify: $v"; ok=0; }
python3 conv.py tojson "$g" $j; d=$(K=$K python3 flipdp_lsi.py $j); d=${d%%$'\n'*}; echo "$d" | grep -q "T_0..T_$K \[${exp//,/, }\].* bad 0 XSIM 0" || { echo "flipdp: $d"; ok=0; }
e=$(python3 embed.py $j | tail -1); echo "$e" | grep -q "mismatches 0" || { echo "embed: $e"; ok=0; }
st=$(echo "$v" | grep "^k $K " | sed 's/.*start \([01]*\) b \([01]\).*/\1 \2/'); s=${st% *}; b=${st#* }
python3 -c "
import json,sys,itertools; G=json.load(open('$j')); q={}
for a,c in itertools.product(range(2),range(2)): q.setdefault(int(G['gate'][0][a]<G['gate'][1][c]),(a,c))
G['start']=list(q[$b])+[int(x) for x in '$s']; json.dump(G,open('$j','w'))"
l=$(cd .. && python3 r189/lemck.py $j); echo "$l" | grep -q "SBAR 0 TAU 0 ESC 0 W 0 AV 0 KEY 0 FB 0" || { echo "lemck: $l"; ok=0; }
rm -f $j
[[ $ok == 1 ]] && echo "CERT OK $(basename $g) m $m T_0..T_$K $exp (fk, ideal+Gen replay, flipdp XSIM 0, embed 0, lemck 0)" || { echo "CERT FAIL $(basename $g)"; exit 1; }
