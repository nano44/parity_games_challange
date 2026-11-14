#!/bin/bash
# N12 record tables, part 2 (policy topx and its kills).  usage: bash tables2.sh > out/tables2.txt   (same line format as tables.sh)
set -u
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
OINK=$ROOT/tools/oink/build
REDB=${REDB:-origin/claude/l-red-b}; LSI=${LSI:-origin/claude/l-si}
inst() {
  local f=$1 N=$2 p=$T/${1}_$2.pg
  if [ ! -s "$p" ]; then
    case $f in
      gk) git show $REDB:experiments/red-b/data/b6b/pg/G_${N}_g3.pg > $p ;;
      W|F|WL) git show $LSI:experiments/si/box104/inst/${f}_$N.pg > $p ;;
      recursiveladder|switchallexp|switchbestexp) python3 $ROOT/experiments/hard-families/pgsolver_port.py $f $N > $p ;;
      symsi_T0|symsi_D|symsi_u50|symsi_Y1) cp inst/${f}_$N.pg $p ;;
      *) $OINK/$f $N > $p ;;
    esac
  fi
  echo $p
}
run() {
  local c=$1 fl=$2 f=$3; shift 3
  for N in "$@"; do
    r=$(python3 n12.py $fl $(inst $f $N) | tail -1)
    set -- $r
    echo "$c $f $N $2 $4 $6 $8 ${10} ${12} ${14} ${16} ${18} ${20} ${22} ${24} ${26} ${28}"
  done
}
for f in counter_symsi tc counter_rob counter_core counter_dp counter_m counter_ortl counter_qpt counter_rr; do run P-topx "--policy topx" $f 1 2 3 4 5 6 7 8 9 10 11 12 16 20; done
run P-topx "--policy topx" tc+ 1 2 3 4 5 6 7 8 9 10 11 12 14 16
for f in recursiveladder switchallexp switchbestexp; do run P-topx "--policy topx" $f 1 2 3 4 5 6 7 8 10 12; done
run P-topx "--policy topx" gk 3 4 5 6 7 8 9 10 11 12 13
run P-topx "--policy topx" W 2 3 4 5 6 7 8; run P-topx "--policy topx" F 2 3 4 5 6 7 8; run P-topx "--policy topx" WL 1 2 3 4
run P-topx "--policy topx" symsi_u50 8 9 10 11 12 13
run P-top "--policy top" counter_symsi 1 2 3 4 5 6 7 8 9 10
run P-top "--policy top" tc+ 1 2 3 4 5 6 7 8 9 10
run KILL-topx "--policy topx" symsi_T0 3 4 5 6 7 8 9 10 11
run KILL-topx "--policy topx" symsi_D 3 4 5 6 7 8 9 10 11
run KILL-Sbig2 "--policy Sbig" symsi_T0 3 4 5 6 7 8 9 10 11
