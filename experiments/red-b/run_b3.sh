#!/bin/bash
# B3 runner (L-RED-B successor 3): resumable gclimb batches; B3ROOT = directory holding the git archives lnew/, lred/, lsi/
# (see gclimb.py's header). Usage: run_b3.sh B3ROOT climbs
cd "$(dirname "$0")"; mkdir -p work; R="$1"
done_() { [ -f "work/$1.out" ] && tail -1 "work/$1.out" | grep -qE "^(GCLIMB|GFAM) "; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"; python3 "$@" >> "work/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
case "$2" in
climbs)
  for n in 6 8 10 12 16; do for s in 1 2; do
    job gc_its_n${n}_s$((700 + 10 * n + s)) gclimb.py "$R" its $((700 + 10 * n + s)) 2000 $n 1
  done; done
  for n in 8 12; do job gc_its0_n${n}_s$((800 + n)) gclimb.py "$R" its $((800 + n)) 2000 $n 0; done
  for n in 8 12; do job gc_perv_n${n}_s$((900 + n)) gclimb.py "$R" perv $((900 + n)) 2000 $n 1; done ;;
fam)
  for n in 2 3 4 5 6; do for s in 1 2; do job gf_fried_n${n}_s$s gfam.py "$R" fried $n $((1000 + 10 * n + s)) 600 1; done; done ;;
fam2)
  for n in 1 2 3 4 5; do job gf_hn_n${n}_s1 gfam.py "$R" hn $n $((2000 + 10 * n + 1)) 400 1; done
  for n in 2 3 4 5 6; do job gf_lmcs_n${n}_s1 gfam.py "$R" lmcs $n $((3000 + 10 * n + 1)) 400 1; done ;;
esac
