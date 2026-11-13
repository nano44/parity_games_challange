#!/bin/bash
# B5 second climb wave (L-RED-B successor 4): larger budgets for random H outside W (FREE faces), objectives p1 and its. Usage:
# run_b5b.sh B3ROOT. Resumable (skip a job whose output ends with B5CLIMB; the climb itself resumes from work/b5c_<tag>.json).
cd "$(dirname "$0")"; mkdir -p work/b5; R="$1"
done_() { [ -f "work/b5/$1.out" ] && tail -1 "work/b5/$1.out" | grep -q "^B5CLIMB "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"
        env "$@" >> "work/b5/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
for obj in p1 its; do
  for n in 8 12 16 20; do for s in 1 2; do
    job w2_${obj}_rand_n${n}_s$s CORE=high python3 b5climb.py "$R" $obj $((5700 + 10 * n + s)) 4000 rand $n
  done; done
done
