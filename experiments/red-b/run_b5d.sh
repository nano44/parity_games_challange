#!/bin/bash
# B5 §6 second wave (L-RED-B successor 4): one-player climbs with 20,000 steps, max out-degree 3 and 5. Usage: run_b5d.sh B3ROOT.
cd "$(dirname "$0")"; mkdir -p work/b5; R="$1"
done_() { [ -f "work/b5/$1.out" ] && tail -1 "work/b5/$1.out" | grep -q "^B5ONE "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"
        "$@" >> "work/b5/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
for d in 3 5; do for n in 6 8 12 16 24 32 48 64; do
  job one2_n${n}_d$d python3 b5one.py "$R" $((7000 + 10 * n + d)) 20000 $n $d
done; done
