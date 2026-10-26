#!/bin/sh
# REFEREE succ. 13, packet P-N5-RUND. Run from docs/referee/scratch/. Own engine only.
I=../../../experiments/n5-exhaustive/instances
PF=../../../experiments/red/so/instances/pftheta34_n32.pg:../../../docs/referee-2/R2-N5-H3/instances/pftheta34_n32_S3.start
LIB=$(python3 -I -c "import sys;sys.path.insert(0,'.');import rho_probe as R;print(' '.join(R.lib()))")
RANDSTARTS=0 PSCHMAX=0 python3 -I rund_probe.py $I/frz1_n24.pg $I/frz2_n24.pg $I/frz3_n24.pg $PF > rund_logs/long_runs.txt
MUT=1 RANDSTARTS=0 PSCHMAX=0 python3 -I rund_probe.py $I/frz1_n24.pg $I/frz3_n24.pg > rund_logs/mut1_control.txt
MUT=2 RANDSTARTS=0 PSCHMAX=0 python3 -I rund_probe.py $I/frz1_n24.pg $I/frz3_n24.pg > rund_logs/mut2_control.txt
python3 -I rund_probe.py rand 6000 4 9 3 21 > rund_logs/rand6000_n4-9_k3_s21.txt
SUFFIX=0 RANDSTARTS=2 MAXN=64 PSCHMAX=7 python3 -I rund_probe.py $LIB > rund_logs/lib41_rs2_nosuffix.txt
