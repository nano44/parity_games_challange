#!/bin/bash
# usage: oner9.sh name seed rev
n=$1; s=$2; r=$3; b=${n}_s${s}_r${r}; O=$SP/runs9r
python3 -I $SP/randrel.py /home/user/parity_games_challange/experiments/red/carry/instances/$n.pg $O/$b.pg $s
if [ $r = 1 ]; then export R2_REV=1; else unset R2_REV; fi
R2P7_LOG=$O/$b.log timeout 120 $SP/oinkp/build/oink --dtl --no-single --no-wcwc --no-loops -v $O/$b.pg /dev/null > $O/$b.out 2>&1 || echo "OINKFAIL" >> $O/$b.res
grep -q "solution verified" $O/$b.out || echo "NOTVERIFIED" >> $O/$b.res
timeout 900 python3 -I $SP/an9.py -v $O/$b.log >> $O/$b.res 2>&1 || echo "ANFAIL" >> $O/$b.res
rm -f $O/$b.log
