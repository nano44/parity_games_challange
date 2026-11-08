#!/bin/bash
# Box 192 R-POT (L-NEW successor 60): DATA behind the DEAD potentials and the PROVED lemmas' checks. Run from experiments/new/box192.
set -e
cd "$(dirname "$0")"
python3 rpot192.py inst/rd2_d4.json inst/rd2_d9.json inst/rd3_d5.json inst/rf_d5.json
python3 depth192.py inst/rd2_d8.json inst/rd2_d9.json
python3 xgate192.py inst/rd2_d4.json inst/rd2_d9.json inst/rd3_d5.json inst/rf_d5.json
python3 xgate192.py rand 100 1
python3 tie192.py 300 1 12
python3 trunc192.py inst/rd2_d9.json inst/rf_d5.json
python3 mtype192.py inst/rd2_d9.json inst/rf_d5.json
python3 ret192.py inst/rd2_d9.json inst/rf_d5.json
python3 segt192.py inst/DEAD_SEGT_n20.json
python3 charge192.py inst/rf_d5.json inst/cR_d2_w8_R22.json
python3 src192.py inst/rf_d5.json
python3 vcyc192.py inst/rd2_d9.json
python3 tiep192.py inst/DEAD_SEGT_n20.json 3 10
python3 dv192.py inst/rd2_d9.json inst/rf_d5.json
