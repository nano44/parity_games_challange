#!/bin/bash
# B5 §6 runner (L-RED-B successor 4): N5 from S3 on ONE-PLAYER games, climbs on I per n. Usage: run_b5c.sh B3ROOT. Resumable.
cd "$(dirname "$0")"; mkdir -p work/b5; R="$1"
done_() { [ -f "work/b5/$1.out" ] && tail -1 "work/b5/$1.out" | grep -q "^B5ONE "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"
        "$@" >> "work/b5/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
for n in 8 12 16 24 32 48; do for s in 1 2; do
  job one_n${n}_s$s python3 b5one.py "$R" $((6000 + 10 * n + s)) 3000 $n 3
done; done
