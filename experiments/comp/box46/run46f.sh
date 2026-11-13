#!/bin/bash
# L-COMP box 46 item 2, final pass: win46.py WITH the Ξ-cycle-use columns (Lead 02:38Z: run_used, nwin_used, Wused, offbeta, cycopt; must-0
# offbacyc) on every set: box 212's towers and L-NEW's 81 frozen (env LNEW212), my Ξ-cyclic sets (names as in out/win46_x{mine,best,big}.out),
# the 224 tower variants, the 1,000 random Ξ-cyclic genomes (same seeds) and 500 random Ξ-ACYCLIC genomes (for offbacyc; P(Ξ-target = X) 0.3 and 0.6: at 0.0 acyclic draws are too rare,
# the first attempt looped for 2 h until the task limit).
# Output out/win46u_<set>.out, resumable per genome. Usage: run46f.sh named | rand
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
: "${LNEW212:?set LNEW212}"; N="$LNEW212/experiments/new"
one() { local out="out/$1" f="$2"; touch "$out"; grep -q "^$(basename $f) " "$out" || python3 win46.py "$f" >> "$out" 2>> "$out.err"; }
loc() { ls "$@" 2>/dev/null | head -1; }
case "$1" in
named)
  for f in $N/box212/inst/*.json; do one win46u_tower.out $f; done
  for b in $(awk '{print $1}' out/win46_records.out out/win46_dead.out out/win46_corpus.out); do one win46u_lnew81.out $(loc $N/box20[2-7]/inst/$b $N/box202/$b $N/box191/inst/$b); done
  for b in $(awk '{print $1}' out/win46_xmine.out); do one win46u_xmine.out $(loc ../box40/inst/$b ../box39/inst/$b ../box41/inst/$b ../box42/inst/$b ../box43/inst/$b ../box45/inst/$b); done
  for b in $(awk '{print $1}' out/win46_xbest.out); do one win46u_xbest.out $(loc ../box44/inst/$b ../box44/out/climb44/$b ../box45/out/climb45/$b); done
  for f in inst/xtower/*.json; do one win46u_xtower.out $f; done
  for b in $(awk '{print $1}' out/win46_xbig.out); do one win46u_xbig.out $(loc ../box42/inst/$b ../box43/inst/$b); done ;;
rand)
  for px in 0.3 0.0; do python3 rand46.py 4611 300 60 $px out/win46u_xrand.out; done
  for px in 0.3 0.0; do python3 rand46.py 4612 200 160 $px out/win46u_xrand.out; done
  for px in 0.3 0.6; do python3 rand46.py 4621 150 60 $px out/win46u_arand.out --acyclic; done
  for px in 0.3 0.6; do python3 rand46.py 4622 100 160 $px out/win46u_arand.out --acyclic; done ;;
*) echo usage; exit 2 ;;
esac
echo "run46f $1 done"
}
main "$@"
