#!/bin/bash
# REFEREE-2 successor 35: P-N5-CHAIN own replay. Usage: sweep.sh ARCHIVE_DIR (git archive of claude/l-new 93531b03) OUTDIR
A=$1; O=$2; T=$(dirname "$0")/r2chain.py; X=$A/experiments/new
P="$X/box189/corpus/*.json $X/box191/inst/*.json $X/box192/inst/*.json $X/box193/inst/*.json $X/box194/inst/*.json $X/box195/inst/*.json $X/box196/inst/*.json $X/box196/inst_si85/*.json"
python3 $T $P > $O/pinned.out
python3 $T --gen 3000 3501 any > $O/gen_any.out
python3 $T --gen 1500 3502 self > $O/gen_self.out
python3 $T --gen 1500 3503 acyc > $O/gen_acyc.out
python3 $T --ctrl0 --gen 200 3504 any > $O/ctrl0.out
python3 $T --ctrlX --gen 200 3504 any > $O/ctrlX.out
python3 $T --ctrl0 $P | tail -1 > $O/ctrl0_pinned.out
python3 $T --ctrlX $P | tail -1 > $O/ctrlX_pinned.out
grep -h TOTAL $O/*.out
