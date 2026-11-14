#!/bin/bash
# N13 SEESAW (L-NEW successor 78): pins + a short live run (about 15 s).  Output pinned in check_n13.out (diffed by ../check.sh).
set -e
cd "$(dirname "$0")"
(cd inst && sha1sum -c --quiet SHA1SUMS) && echo "inst pinned"
(cd out && sha1sum -c --quiet SHA1SUMS) && echo "out pinned"
f() { python3 n13.py "$@" | awk '{print "jumps", $8, "peels", $10, "WE", $18, $19}'; }
for i in c13_n6_d8_s46_altp c13_n8_d8_s48_altp c13_n10_d8_s410_altp c13_n12_d8_s31_altp c13_n18_d10_s32_altp; do echo "alt+  $i  $(f inst/$i.pg)"; done
echo "alt+  symsi_u50T0_9   $(f ../n12/inst/symsi_u50T0_9.pg)"
echo "alt-  symsi_u50T0_9   $(f --mode alt- ../n12/inst/symsi_u50T0_9.pg)"
echo "plus  counter_symsi_9 $(f --mode plus ../n12/inst/counter_symsi_9.pg)"
echo "ctrl  both cap 500    $(f --mode both --cap 500 inst/c13_n12_d8_s31_altp.pg)"
python3 rtest13.py 200 7 30 alt+ alt- both | tail -n 3
