#!/bin/bash
# B4 climb runner (L-RED-B successor 3): objective P1 (iterations after N5's first fallback). Usage: run_b4.sh B3ROOT
cd "$(dirname "$0")"; mkdir -p work; R="$1"
done_() { [ -f "work/$1.out" ] && tail -1 "work/$1.out" | grep -q "^B4CLIMB "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"; python3 "$@" >> "work/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
for n in 2 3 4 5 6; do job b4c_fried_n$n b4climb.py "$R" fried $n $((6000 + n)) 400 1; done
for n in 2 3 4 5 6; do job b4c_lmcs_n$n b4climb.py "$R" lmcs $n $((6100 + n)) 400 1; done
for n in 1 2 3 4; do job b4c_hn_n$n b4climb.py "$R" hn $n $((6200 + n)) 400 1; done
