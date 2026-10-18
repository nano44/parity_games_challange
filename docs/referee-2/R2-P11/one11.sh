#!/bin/bash
# usage: one9.sh file mode   (mode: oink = pinned order; stable = relabel by (priority, id) + ascending ins)
f=$1; m=$2; b=$(echo $f | tr / _)_$m; O=$SP/runs11
if [ $m = stable ]; then python3 -I $SP/stablerel.py $f $SP/rel9/$b.pg; g=$SP/rel9/$b.pg; export R2_REV=1; else g=$f; unset R2_REV; fi
R2P7_LOG=$O/$b.log timeout 120 $SP/oinkp/build/oink --dtl --no-single --no-wcwc --no-loops -v $g /dev/null > $O/$b.out 2>&1 || echo "OINKFAIL $f" >> $O/$b.res
grep -q "solution verified" $O/$b.out || echo "NOTVERIFIED $f" >> $O/$b.res
timeout 900 python3 -I $SP/an11.py $O/$b.log >> $O/$b.res 2>&1 || echo "ANFAIL $f" >> $O/$b.res
rm -f $O/$b.log $SP/rel9/$b.pg
