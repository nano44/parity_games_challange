#!/bin/sh
# REFEREE succ. 13, packet P-N5-STAU. Run from docs/referee/scratch/. Own engine only.
python3 -I stau_probe.py rand 20000 3 10 4 7 > stau_logs/rand20000_n3-10_k4_s7.txt
python3 -I stau_probe.py c1o 5000 5 20 22 > stau_logs/c1o5000_n5-20_s22.txt
RANDSTARTS=2 python3 -I stau_probe.py $(python3 -I -c "import sys;sys.path.insert(0,'.');import rho_probe as R;print(' '.join(R.lib()))") > stau_logs/lib41_rs2.txt
RANDSTARTS=0 python3 -I stau_probe.py stau_inputs/is0_c1o264.pg > stau_logs/is0_c1o264.txt
