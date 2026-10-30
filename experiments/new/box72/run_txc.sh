#!/bin/bash
# L-NEW box 72 §6: txc.py (N5 and --lzc) and L-SI's tied.py @ l-si 4fb0bfba (copied: tied_lsi_4fb0bfba.py; N5 and via runlzc.py)
# over the 719-game corpus (box59/sbcg.lst) and alt_all (413, with starts).
cd "$(dirname "$0")/../.."
one() { a=$(timeout 900 python3 -I new/box72/txc.py "$@" 2>&1 | tail -1); b=$(timeout 900 python3 -I new/box72/txc.py "$@" --lzc 2>&1 | tail -1)
        c=$(timeout 900 python3 -I new/box72/tied_lsi_4fb0bfba.py "$@" 2>&1 | tail -1); d=$(timeout 900 python3 -I new/box72/runlzc.py new/box72/tied_lsi_4fb0bfba.py "$@" 2>&1 | tail -1)
        echo "GAME $1 N5 $a LZC $b TIEDN5 $c TIEDLZC $d"; }; export -f one
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"' > new/box72/txc_sbcg.txt
cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _ > new/box72/txc_alt.txt
