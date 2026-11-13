#!/bin/bash
# B3 runner 2 (L-RED-B successor 3): longer guide climbs on H_n (budget check). Usage: run_b3b.sh B3ROOT
cd "$(dirname "$0")"; mkdir -p work; R="$1"
done_() { [ -f "work/$1.out" ] && tail -1 "work/$1.out" | grep -qE "^(GCLIMB|GFAM) "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"; python3 "$@" >> "work/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
for n in 2 3 4; do job gf_hn_n${n}_long gfam.py "$R" hn $n $((5000 + n)) 1500 1; done
