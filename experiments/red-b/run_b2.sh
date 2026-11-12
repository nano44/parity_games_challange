#!/bin/bash
# B2 runner (L-RED-B successor 3): resumable; each job writes work/<tag>.out and is skipped when that file ends in a final
# SWEEP3 line. Usage: run_b2.sh frozen | exh | rand | ctrl
cd "$(dirname "$0")"; mkdir -p work
done_() { [ -f "work/$1.out" ] && tail -1 "work/$1.out" | grep -qE "^(SWEEP3 [^(]*runs.*s|N5XI3 SUMMARY.*|CLIMB3 .*)$" && ! tail -1 "work/$1.out" | grep -q partial; }
job() { local tag=$1; shift; if done_ "$tag"; then echo "skip $tag"; return; fi; echo "run $tag $(date -u +%H:%M:%S)"; python3 "$@" > "work/$tag.out" 2>&1; echo "end $tag rc $? $(date -u +%H:%M:%S)"; }
source ./frozen.sh
DEAD="../new/box191/inst/DEAD_SEG2P_d4_N8.json ../new/box191/inst/DEAD_SEG2P_d7_N14.json ../new/box191/inst/DEAD_SEG2P_d9_N18.json"
case "$1" in
frozen)
  for tie in keep-low high rand; do
    job frozen_rec_$tie sweep3.py files $tie T $REC
    job frozen_cor_$tie sweep3.py files $tie T $COR
    job frozen_dead_$tie sweep3.py files $tie all $DEAD
  done
  job frozen_rec_allref sweep3.py files keep-low all $REC
  job frozen_cor_allref sweep3.py files keep-low all $COR ;;
exh)
  for nm in "1 1" "1 2" "1 3" "1 4" "1 5" "2 2" "2 3" "2 4" "3 3"; do
    set -- $nm; job exh_N$1_M$2 sweep3.py exh $1 $2
  done ;;
rand)
  for sh in mix rand dense deep noX self flat k1; do job rand_${sh}_s301 sweep3.py rand 301 20000 6 14 all $sh; done
  for sh in mix deep k1 dense; do job randbig_${sh}_s302 sweep3.py rand 302 4000 16 40 T $sh; done ;;
esac
case "$1" in
n5xi)
  S="$2"
  job n5xi_rec n5xi3.py "$S" $REC
  job n5xi_cor n5xi3.py "$S" $COR
  job n5xi_dead n5xi3.py "$S" $DEAD
  job n5xi_rand_s401 n5xi3.py "$S" --rand 401 3000 6 14 ;;
climb)
  for spec in "Tabs 501 3000 12 26" "Tabs 502 3000 24 52" "plat 503 3000 12 26" "phi 504 3000 12 26" "stall 505 3000 12 26" "tail 506 3000 12 26" "T 507 3000 24 52" "plat 508 3000 24 52"; do
    set -- $spec; job climb3_$1_s$2 climb3.py $1 $2 $3 $4 $5 rand
  done ;;
esac
case "$1" in
mut)
  job mut_s601_rec sweep3.py mut 601 150 $REC
  job mut_s602_dead sweep3.py mut 602 300 $DEAD ;;
esac
