#!/bin/bash
# N12 SETTLE (L-NEW successor 78): pins + a short live run (about 20 s).  Output pinned in check_n12.out (diffed by ../check.sh).
set -e
cd "$(dirname "$0")"
(cd inst && sha1sum -c --quiet SHA1SUMS) && echo "inst pinned"
(cd out && sha1sum -c --quiet SHA1SUMS) && echo "out pinned"
f() { python3 n12.py "$@" | awk '{print "calls", $8, "WE", $28}'; }
echo "Sbig  counter_symsi_7  $(f --policy Sbig inst/counter_symsi_7.pg)"
echo "topx  counter_symsi_7  $(f --policy topx inst/counter_symsi_7.pg)"
echo "Sbig  symsi_u50T0_7    $(f --policy Sbig inst/symsi_u50T0_7.pg)"
echo "topx  symsi_u50T0_7    $(f --policy topx inst/symsi_u50T0_7.pg)"
echo "duet  symsi_u50T0_7    $(f --policy duet inst/symsi_u50T0_7.pg)"
echo "topx  symsi_T0_7       $(f --policy topx inst/symsi_T0_7.pg)"
echo "Sbig  symsi_u50_8      $(f --policy Sbig inst/symsi_u50_8.pg)"
echo "sound lit_witness_n4   $(f --policy small --nopeel --no61 --no62 --no64 inst/lit_witness_n4.pg)"
echo "ctrl  lit_witness_n4   $(f --policy small --nopeel --no61 --no62 --no64 --literal inst/lit_witness_n4.pg)"
python3 rtest.py 150 21 14 Sbig topx duet small+literal+nopeel+n61+n62+n64 | grep '^games'
