#!/bin/bash
# usage: one7.sh file rev
f=$1; rev=$2; b=$(echo $f | tr / _)_r$rev
if [ $rev = 1 ]; then export R2_REV=1; fi
R2P7_LOG=${OUTD}/$b.log timeout 120 $SP/oinkp/build/oink --dtl --no-single --no-wcwc --no-loops -v $f /dev/null > ${OUTD}/$b.out 2>&1 || echo "OINKFAIL $f" >> ${OUTD}/$b.res
grep -q "solution verified" ${OUTD}/$b.out || echo "NOTVERIFIED $f" >> ${OUTD}/$b.res
timeout 900 python3 -I $SP/an8.py ${OUTD}/$b.log >> ${OUTD}/$b.res 2>&1 || echo "ANFAIL $f" >> ${OUTD}/$b.res
rm -f ${OUTD}/$b.log
