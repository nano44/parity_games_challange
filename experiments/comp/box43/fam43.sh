#!/bin/bash
# L-COMP box 43 item 2: the DHIB-line families (no search; growth rule = box42/clone42.py: k clones of one mover X of DHIB26_2804 with
# copies of its options and of its in-edge options, gate / β ranks just after the originals'). Three movers chosen by trace
# (trace43.py, probe43.py): D18 = the hub 18 (Ξ-target of the cascade gates (75..83, 1) and of the repeater gate (10, 0)),
# D10 = the repeater mover 10 (gate (10, 0): 7 deep flips), D80 = the cascade mover 80. k = 0 is DHIB26_2804 byte for byte.
cd "$(dirname "$0")"; B=../box40/inst/DHIB26_2804.json; mkdir -p inst
cp $B inst/DHIB26_k0.json
for k in 4 8 16 32; do python3 ../box42/clone42.py $B 18 $k inst/D18_k$k.json; done
for k in 16 32 64 128; do python3 ../box42/clone42.py $B 10 $k inst/D10_k$k.json; python3 ../box42/clone42.py $B 80 $k inst/D80_k$k.json; done
(cd inst && sha1sum DHIB26_k0.json D18_k*.json D10_k*.json D80_k*.json > SHA1SUMS.fam43)
