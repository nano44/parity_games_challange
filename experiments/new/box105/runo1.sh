#!/bin/bash
# L-NEW box 105: o1.py on box 50b's corpus + box-97 pins + cascl / cedge.
cd "$(dirname "$0")/../.."
one() { timeout 300 python3 -I new/box105/o1.py "$@" 2>&1 | tr '\n' ' ' | sed "s|^|GAME $1 |"; echo; }; export -f one
{ grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -I{} bash -c 'one "{}"'
  cat si/root/logs/alt_all.lst | xargs -P 4 -L 1 bash -c 'one "$@"' _
  for f in new/box97/inst/sbq2_K8_m16 new/box97/inst/obs_K12_m24 new/box97/inst/latew_K16_m32 new/box101/inst/cascl_K4_m8_N100 new/box104/inst/cedge_n32; do one $f.pg $f.start; done; } > new/box105/o1_corpus.txt
