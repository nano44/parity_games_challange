#!/bin/bash
# N12 record tables (L-NEW successor 78, 2026-11-14).  Run once from experiments/new/n12; output pinned in out/SHA1SUMS.
# usage: bash tables.sh > out/tables.txt     (needs tools/oink/build and the branches origin/claude/l-red-b, origin/claude/l-si fetched)
# line: <config> <family> <N> n m d calls settles settled rounds cuts peels depth work maxbits wbits WE
set -u
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
OINK=$ROOT/tools/oink/build
REDB=${REDB:-origin/claude/l-red-b}; LSI=${LSI:-origin/claude/l-si}
echo "# oink $(cd $ROOT/tools/oink && git rev-parse --short HEAD 2>/dev/null) l-red-b $(git rev-parse $REDB) l-si $(git rev-parse $LSI)"
inst() {  # family N -> path
  local f=$1 N=$2 p=$T/${1}_$2.pg
  if [ ! -s "$p" ]; then
    case $f in
      gk) git show $REDB:experiments/red-b/data/b6b/pg/G_${N}_g3.pg > $p ;;
      W|F|WL) git show $LSI:experiments/si/box104/inst/${f}_$N.pg > $p ;;
      recursiveladder|switchallexp|switchbestexp) python3 $ROOT/experiments/hard-families/pgsolver_port.py $f $N > $p ;;
      symsi_u50|symsi_Y1) cp inst/${f}_$N.pg $p ;;
      *) $OINK/$f $N > $p ;;
    esac
  fi
  echo $p
}
run() {  # config-name "flags" family N...
  local c=$1 fl=$2 f=$3; shift 3
  for N in "$@"; do
    r=$(python3 n12.py $fl $(inst $f $N) | tail -1)
    set -- $r
    echo "$c $f $N $2 $4 $6 $8 ${10} ${12} ${14} ${16} ${18} ${20} ${22} ${24} ${26} ${28}"
  done
}
A0="--no61 --no62 --no64 --nopeel --policy small"; A1="--nopeel --policy small"; A2="--nopeel --policy large"
A3="--nopeel --policy sup"; A4="--nopeel --policy inf"
run A0 "$A0" gk 3 4 5
run A1 "$A1" gk 3 4 5 6 7 8 9 10 11 12 13
run A2 "$A2" gk 3 4 5 6 7 8 9 10 11 12 13
for c in A1 A2 A3 A4; do eval fl=\$$c; run $c "$fl" counter_symsi 1 2 3 4 5 6 7 8 9; done
run A1 "$A1" tc 1 2 3 4 5 6 7 8
run A2 "$A2" tc 1 2 3 4 5 6 7 8 9 10 11 12 16 20
run A1 "$A1" counter_rob 1 2 3 4 5 6 7 8 9 10 11 12
run A1 "$A1" switchallexp 1 2 3 4 5 6 7 8 10 12
for pol in small large sup inf duet Sbig; do
  case $pol in
    small) run P-$pol "--policy $pol" counter_symsi 1 2 3 4 5 6 7 8 9 10 11 12 16 20; run P-$pol "--policy $pol" tc 1 2 3 4 5 6 7 8; run P-$pol "--policy $pol" tc+ 1 2 3 4 5 6 7 8 9 ;;
    large|sup|inf) run P-$pol "--policy $pol" counter_symsi 1 2 3 4 5 6 7 8 9; run P-$pol "--policy $pol" tc 1 2 3 4 5 6 7 8 9 10 11 12 16 20; run P-$pol "--policy $pol" tc+ 1 2 3 4 5 6 7 8 9 10 11 12 ;;
    duet) run P-$pol "--policy $pol" counter_symsi 1 2 3 4 5 6 7 8 9 10 11 12; run P-$pol "--policy $pol" tc 1 2 3 4 5 6 7 8 9 10 11 12 16 20; run P-$pol "--policy $pol" tc+ 1 2 3 4 5 6 7 8 9 10 11 12 ;;
    Sbig) for f in counter_symsi tc counter_rob counter_core counter_dp counter_m counter_ortl counter_qpt counter_rr; do run P-$pol "--policy $pol" $f 1 2 3 4 5 6 7 8 9 10 11 12 16 20; done
          run P-$pol "--policy $pol" tc+ 1 2 3 4 5 6 7 8 9 10 11 12 14 16
          for f in recursiveladder switchallexp switchbestexp; do run P-$pol "--policy $pol" $f 1 2 3 4 5 6 7 8 10 12; done
          run P-$pol "--policy $pol" gk 3 4 5 6 7 8 9 10 11 12 13
          run P-$pol "--policy $pol" W 2 3 4 5 6 7 8; run P-$pol "--policy $pol" F 2 3 4 5 6 7 8; run P-$pol "--policy $pol" WL 1 2 3 4
          run KILL-Sbig "--policy $pol" symsi_u50 8 9 10 11 12 13; run KILL-Sbig "--policy $pol" symsi_Y1 8 9 10 11 12 13 ;;
  esac
done
run FLIP1 "--policy flip1" counter_symsi 1 2 3 4 5 6 7 8 9
