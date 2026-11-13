#!/bin/bash
# B5 runner (L-RED-B successor 4; docs/red-b/B5-second-fb.md). Usage: run_b5.sh B3ROOT (lemma | climbs)   Resumable: a job whose
# output already ends with its SUMMARY / B5CLIMB line is skipped. Outputs in work/b5/ (moved to data/b5/ before the commit).
cd "$(dirname "$0")"; mkdir -p work/b5; R="$1"
done_() { [ -f "work/b5/$1.out" ] && tail -1 "work/b5/$1.out" | grep -q "^B5LEMMA SUMMARY\|^B5CLIMB "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"
        : > "work/b5/$tag.out"; env "$@" >> "work/b5/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
ST="$(ls data/b3/*.json data/b4/*.json)"
if [ "$2" = lemma ]; then
  for c in high low; do
    job lemma_states_$c CORE=$c python3 b5lemma.py "$R" states $ST
    job lemma_fam_fried_$c CORE=$c python3 b5lemma.py "$R" fam fried 2 3 4 5 6 7 8
    job lemma_fam_lmcs_$c CORE=$c python3 b5lemma.py "$R" fam lmcs 2 3 4 5 6 7 8
    job lemma_fam_hn_$c CORE=$c python3 b5lemma.py "$R" fam hn 1 2 3 4
    job lemma_rand_$c CORE=$c python3 b5lemma.py "$R" rand 5101 1500 10
    job lemma_rand12_$c CORE=$c python3 b5lemma.py "$R" rand 5102 300 14
  done
  job ctrl1 CTRL=1 python3 b5lemma.py "$R" rand 5201 200 8
  job ctrl2 CTRL=2 python3 b5lemma.py "$R" rand 5202 200 8
  job ctrl_free CORE=high python3 b5lemma.py "$R" rand 5203 500 10 0.7
  job x2_mirror_rand MIRROR=1 python3 b5lemma.py "$R" rand 5204 500 10
  job x2_mirror_states MIRROR=1 python3 b5lemma.py "$R" states $ST
fi
if [ "$2" = climbs ]; then
  for obj in p1 k; do
    for n in 6 8 10 12; do job c_${obj}_rand_n$n CORE=high python3 b5climb.py "$R" $obj $((5300 + n)) 400 rand $n; done
    for n in 1 2 3; do job c_${obj}_hn_n$n CORE=high python3 b5climb.py "$R" $obj $((5400 + n)) 300 fam hn $n; done
    for n in 2 3 4; do job c_${obj}_fried_n$n CORE=high python3 b5climb.py "$R" $obj $((5500 + n)) 300 fam fried $n; done
    for n in 2 3 4; do job c_${obj}_lmcs_n$n CORE=high python3 b5climb.py "$R" $obj $((5600 + n)) 300 fam lmcs $n; done
  done
fi
