#!/bin/bash
# box 42 item 2: CL(k) on two engines. Mine: box41/deep41.py (own34). Second: L-SI cross100.py (env LSI100 = worktree claude/l-si 23d39400;
# RED = worktree claude/l-red 59daaef2; LNEW = archive of l-new fcba92fc), CMAX 3. Usage: meas42.sh mine|cross
cd "$(dirname "$0")"; L="inst/CL0.json inst/CL8.json inst/CL16.json inst/CL30.json inst/CL45.json inst/CL90.json inst/CL131.json"
if [ "$1" = mine ]; then python3 ../box41/deep41.py $L > out/meas42_mine.out 2>&1; echo "mine exit $?"
else for f in $L; do CMAX=3 python3 -I "$LSI100/experiments/si/box100/cross100.py" inst "$PWD/$f" | head -1; done > out/meas42_cross.out 2>&1; echo "cross exit $?"; fi
