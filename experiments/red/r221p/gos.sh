#!/bin/bash
# L-RED 56 R221 (i) structured ENDGAME-3 attack; needs WT, WT3; output out/spost_<mode>.txt
cd "$(dirname "$0")"
i=0; for m in esc noesc deep dense late lvl0; do i=$((i+1)); echo "$m 6$i"; done | xargs -P 4 -L 1 bash -c '[ -f out/spost_$0.done ] || { python3 spost221.py $0 $1 300 > out/spost_$0.txt 2>&1 && touch out/spost_$0.done; }'
