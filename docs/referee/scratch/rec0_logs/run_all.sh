#!/bin/sh
# REFEREE succ. 13, packet P-N5-REC0. Run from docs/referee/scratch/. Own engine only.
LIB=$(python3 -I -c "import sys;sys.path.insert(0,'.');import rho_probe as R;print(' '.join(R.lib()))")
LEVELS=1 python3 -I rec0_probe.py rand 20000 4 9 3 11 > rec0_logs/rand20000_n4-9_k3_s11_levels.txt
RANDSTARTS=2 python3 -I rec0_probe.py $LIB > rec0_logs/lib41_rs2.txt
RANDSTARTS=2 LEVELS=1 LEVELMAX=14 python3 -I rec0_probe.py $LIB > rec0_logs/lib41_rs2_levels_n14.txt
