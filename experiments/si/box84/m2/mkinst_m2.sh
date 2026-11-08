#!/usr/bin/env bash
# L-SI box 84 milestone 2 (ii): regenerate the frozen CYC instances (cyc84.py on frozen box 83 / box 84 genomes) into inst/.
set -euo pipefail; cd "$(dirname "$0")"; O=${1:-inst}
python3 -I -B cyc84.py ../../box83/inst/LR2_exitup.json B1 B2 1 0 $O/CY2_lr.json
python3 -I -B cyc84.py ../inst/HP2_mup.json B1 B2 1 0 $O/CY2_hp.json
python3 -I -B cyc84.py ../inst/HP3_mup.json B1 B2 1 0 $O/CY3_hp_1.json
python3 -I -B cyc84.py $O/CY3_hp_1.json B2 B3 1 0 $O/CY3_hp.json
python3 -I -B cyc84.py ../inst/HP4_mup.json B1 B2 1 0 $O/CY4_hp_1.json
python3 -I -B cyc84.py $O/CY4_hp_1.json B2 B3 1 0 $O/CY4_hp_2.json
python3 -I -B cyc84.py $O/CY4_hp_2.json B3 B4 1 0 $O/CY4_hp.json
rm -f $O/CY3_hp_1.json $O/CY3_hp_1.names.json $O/CY4_hp_1.json $O/CY4_hp_1.names.json $O/CY4_hp_2.json $O/CY4_hp_2.names.json
