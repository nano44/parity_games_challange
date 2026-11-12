#!/bin/bash
# Box 207 (L-NEW successor 71): R-LOCAL must-0 counters (rrep, ifail, qfail), the DEAD-charge witnesses (K1L10 deepnoR 5, B400_r32
# efail at step 43), the climb genomes, the control; run from experiments/new/box207. Output diffed against check207.out.
set -e
python3 rlocal207.py ../box203/inst/MWR4_2.json ../box206/inst/K1L10_n48.json ../box204/inst/B400_r32_a13d9661.json ../box206/inst/CWRR4_n.json inst/CFI3_n48.json inst/RINT_n48.json
RL_CTRL=1 python3 rlocal207.py ../box203/inst/MWR4_2.json | sed 's/^/ctrl /'
python3 window207.py ../box204/inst/B400_r32_a13d9661.json 83 | grep '^43 ' | sed 's/^/B400 /'
python3 window207.py inst/CFI3_n48.json 29 | grep '^6 ' | sed 's/^/CFI3 /'
python3 paid207.py inst/CFI3_n48.json ../box206/inst/K1L10_n48.json | sed 's/^/paid /'
PAID_CTRL=1 python3 paid207.py inst/CFI3_n48.json | sed 's/^/ctrlpaid /'
