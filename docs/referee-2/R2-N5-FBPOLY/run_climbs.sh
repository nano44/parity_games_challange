#!/bin/bash
# REFEREE-2 succ. 11: two 1500 s climbs against P-N5-FBPOLY's untested regime (FIT frz), run from this directory; seeds are inputs only.
mkdir -p climb
python3 fbpoly_climb.py frz 4101 6 10 1500 > climb/frz_4101.txt 2>&1 &
python3 fbpoly_climb.py frz 4102 6 10 1500 ../R2-N5-RHO/climb/$(ls ../R2-N5-RHO/climb | grep '\.pg$' | head -1) > climb/frz_4102.txt 2>&1 &
wait
