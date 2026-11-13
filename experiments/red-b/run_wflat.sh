#!/bin/bash
# FLAT-IDX test runner (L-RED-B successor 3). Usage: run_wflat.sh B3ROOT
cd "$(dirname "$0")"; mkdir -p work; R="$1"
done_() { [ -f "work/$1.out" ] && tail -1 "work/$1.out" | grep -q "^WFLAT SUMMARY"; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"; python3 "$@" > "work/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
job wflat_spec_rand_s11 wflat.py "$R" spec rand 11 3000 10
job wflat_xi_rand_s11 wflat.py "$R" xi rand 11 3000 10
job wflat_spec_fried wflat.py "$R" spec fam fried 2 3 4 5 6 7 8
job wflat_spec_lmcs wflat.py "$R" spec fam lmcs 2 3 4 5 6 7 8
job wflat_spec_hn wflat.py "$R" spec fam hn 1 2 3 4 5 6
job wflat_xi_fried wflat.py "$R" xi fam fried 2 3 4 5 6
job wflat_spec_rand_s12 wflat.py "$R" spec rand 12 1000 30
