#!/usr/bin/env bash
# L-SI box 69 self-check (~30 s): ABS-2 maxima; real tables reproduce D(2, tau); IM separates (500 bad tables: 0 IM graphs; 30 ENC
# tables: 30, the positive control); witness LP infeasible (only if scipy is installed).
set -euo pipefail
cd "$(dirname "$0")"
if command -v gcc >/dev/null; then gcc -O2 -o abs2_check abs2.c && ./abs2_check | head -n 1 | grep -q "max T0 4  max T1 7"; rm -f abs2_check; fi
python3 -I mine.py | grep -q "{1: 2, 2: 4, 3: 5, 4: 5}"
head -n 500 bad_tabs.txt > /tmp/box69_bad500.txt
python3 -I imtest.py /tmp/box69_bad500.txt | grep -q "tables 500 with an IM graph 0 "
python3 -I imtest.py enc30.txt | grep -q "tables 30 with an IM graph 30 "
rm -f /tmp/box69_bad500.txt
if python3 -I -c "import scipy" 2>/dev/null; then python3 -I lpreal.py a0ec2064a0ec2064 | grep -q "NOT additive-realisable"; fi
echo "box 69 IM mechanism: PASS"
