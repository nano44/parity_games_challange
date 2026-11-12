#!/bin/bash
# L-COMP box 43 items 2-3 on two engines. mine: box41/deep41.py (own34; Deep_3 = DeepInt, per-gate max gmaxInt, dmaxInt, T3); cross:
# L-SI cross100.py on L-RED how3_232 (env LSI100 = archive of claude/l-si 23d39400, RED = archive of claude/l-red 59daaef2 experiments/,
# LNEW = archive of claude/l-new fcba92fc; CMAX 3; whole-run deep, dmax, T3). Resumable per instance.
# Usage: meas43.sh mine|cross [fam|tail]   (fam = item 2, the DHIB-line clone families; tail = item 3: MWR(n) and TAIL_2 genomes)
cd "$(dirname "$0")"; SET=${2:-fam}
if [ $SET = fam ]; then L="inst/DHIB26_k0.json $(ls inst/D18_k*.json inst/D10_k*.json inst/D80_k*.json | sort -t k -k2 -n)"; O=out/meas43_$1.out
else L="inst/MWR4_2.json inst/TMWR4.json inst/MWR8_2.json inst/TMWR8.json inst/MWR16_2.json inst/TMWR16.json inst/TC6G8.json inst/TREC.json inst/TDHIB26.json inst/MWR32_2.json inst/TMWR32.json inst/MWR48_2.json inst/TMWR48.json"; O=out/meas43_tail_$1.out; fi
touch $O
for f in $L; do
  grep -q "^$(basename $f) " $O && continue
  if [ "$1" = mine ]; then python3 ../box41/deep41.py $f >> $O 2>&1
  else CMAX=3 python3 -I "$LSI100/experiments/si/box100/cross100.py" inst "$PWD/$f" | head -1 >> $O 2>&1; fi
done
echo "meas43 $1 $SET done: $(wc -l < $O) lines"
