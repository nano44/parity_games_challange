#!/bin/bash
# N13 SEESAW record tables (L-NEW successor 78, 2026-11-14).  usage: bash tables13.sh > out/tables13.txt
# line: <engine/mode> <family> <N> n m d jumps peels work maxbits wbits WE status      (gkk rows: n m d iters maxbits WE status)
set -u
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
OINK=$ROOT/tools/oink/build
REDB=${REDB:-origin/claude/l-red-b}; LSI=${LSI:-origin/claude/l-si}
echo "# oink 8fbf0a7 l-red-b $(git rev-parse $REDB) l-si $(git rev-parse $LSI)"
inst() {
  local f=$1 N=$2 p=$T/${1}_$2.pg
  if [ ! -s "$p" ]; then
    case $f in
      gk) git show $REDB:experiments/red-b/data/b6b/pg/G_${N}_g3.pg > $p ;;
      W|F|WL) git show $LSI:experiments/si/box104/inst/${f}_$N.pg > $p ;;
      recursiveladder|switchallexp|switchbestexp) python3 $ROOT/experiments/hard-families/pgsolver_port.py $f $N > $p ;;
      symsi_*) cp ../n12/inst/${f}_$N.pg $p ;;
      *) $OINK/$f $N > $p ;;
    esac
  fi
  echo $p
}
run() { local mode=$1 f=$2; shift 2; for N in "$@"; do echo "$mode $f $N $(python3 n13.py --mode $mode $(inst $f $N) | tail -1)"; done; }
gkk() { local f=$1; shift; for N in "$@"; do echo "gkk $f $N $(python3 gkk_plain.py $(inst $f $N) | tail -1)"; done; }
gkk tc 1 2 3 4 5 6 7 8 9
gkk tc+ 1 2 3 4 5 6 7 8 9
gkk counter_symsi 1 2 3 4 5 6 7 8 9 10 11 12
for mode in alt+ alt-; do
  run $mode tc 1 2 3 4 5 6 7 8 9 10 11 12 16 20 24 28 32
  run $mode tc+ 1 2 3 4 5 6 7 8 9 10 11 12 14 16 18 20 24
  for f in counter_symsi counter_rob counter_core counter_dp counter_m counter_ortl counter_qpt counter_rr; do run $mode $f 1 2 3 4 5 6 7 8 9 10 11 12 16 20 24 28 32; done
  for f in recursiveladder switchallexp switchbestexp; do run $mode $f 1 2 3 4 5 6 7 8 10 12; done
  run $mode gk 3 4 5 6 7 8 9 10 11 12 13
  run $mode W 2 3 4 5 6 7 8; run $mode F 2 3 4 5 6 7 8; run $mode WL 1 2 3 4
  run $mode symsi_u50T0 5 6 7 8 9 10 11; run $mode symsi_T0 3 4 5 6 7 8 9 10 11; run $mode symsi_D 3 4 5 6 7 8 9 10 11
  run $mode symsi_u50 8 9 10 11 12 13; run $mode symsi_Y1 8 9 10 11 12 13
done
for mode in plus minus; do
  run $mode tc 1 2 3 4 5 6 7 8 9 10 11 12 16 20 24 28 32
  run $mode tc+ 1 2 3 4 5 6 7 8 9 10 11 12 14 16 18 20 24
  run $mode counter_symsi 1 2 3 4 5 6 7 8 9 10 11 12 16 20 24 28 32
done
