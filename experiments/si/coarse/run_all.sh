#!/usr/bin/env bash
# L-SI box 7: reproduce every DATA line of docs/si/N5-C-box7.md and docs/si/P-N5-FB-box7.md. Logs go to experiments/si/coarse/logs/.
# Named set = experiments/si/coarse/named.txt (53 files, each asserted one-Odd-choice). Usage: experiments/si/coarse/run_all.sh
set -u
cd "$(git rev-parse --show-toplevel)"
D=experiments/si/coarse; L=${LOGDIR:-$D/logs}; mkdir -p $L; N=$(cat $D/named.txt)
python3 $D/mono.py $N > $L/mono_named.txt 2>&1
python3 $D/mono.py --random 701 1500 4 14 > $L/mono_rand701.txt 2>&1
python3 $D/mono.py --random 702 1500 4 14 > $L/mono_rand702.txt 2>&1
python3 $D/fbcount.py $N > $L/fb_named.txt 2>&1
python3 $D/fbcount.py --random 711 1500 4 14 > $L/fb_rand711.txt 2>&1
python3 $D/fbcount.py --random 712 1500 4 14 > $L/fb_rand712.txt 2>&1
python3 $D/fbcount.py --c1o 721 2500 8 16 > $L/fb_c1o721.txt 2>&1
python3 $D/fbcount.py --c1o 722 2500 8 16 > $L/fb_c1o722.txt 2>&1
python3 $D/tame.py $N > $L/tame_named.txt 2>&1
python3 $D/jump.py $N > $L/jump_named.txt 2>&1
python3 $D/jumpeq.py $N > $L/jumpeq_named.txt 2>&1
python3 $D/dpot.py $N > $L/dpot_named.txt 2>&1
for f in $L/*.txt; do echo "$(basename $f): $(tail -1 $f | cut -c1-200)"; done
