#!/usr/bin/env bash
# L-RED 71 R246 runner. Usage: run246.sh JOB   with env LNEW (tree of claude/l-new a143d406: experiments/new, experiments/si/si.py,
# experiments/harness, experiments/hard-families, experiments/n5-second), TRUNK (tree of trunk: experiments/n5-second, experiments/harness,
# experiments/hard-families/pgsolver_si.py), OINK (path of the oink binary). Outputs in out/ (one file per job; a job is skipped if its
# output ends with «JOB END»). Jobs: build census_s census_v n5b zchk trace rand ctrl k10
set -uo pipefail
cd "$(dirname "$0")"; mkdir -p out pg
J="$1"; O="out/$J.out"
if [ -f "$O" ] && tail -1 "$O" | grep -q "^JOB END"; then echo "skip $J"; exit 0; fi
GK=../r244/gk
N() { echo $((9 * $1 - 16)); }
{
case "$J" in
  build)
    for k in 3 4 5 6 7 8 9 10; do
      python3 g3_246.py r104 $GK/G_${k}_renum.json pg/G_${k}_r104.pg
      python3 g3_246.py top $GK/G_${k}_renum.json pg/G_${k}_top.pg
    done
    (cd pg && sha1sum G_*_top.pg > SHA1SUMS_top && sha1sum G_*_r104.pg > SHA1SUMS_r104) ;;
  census_s)
    for k in 3 4 5 6 7 8 9; do
      python3 tie246.py s spec $(N $k) pg/G_${k}_r104.pg
      python3 tie246.py s spec $(N $k) pg/G_${k}_top.pg
      python3 tie246.py s xi $(N $k) pg/G_${k}_top.pg
    done ;;
  census_v)
    for k in 3 4 5 6 7; do
      python3 tie246.py v spec $(N $k) pg/G_${k}_r104.pg
      python3 tie246.py v spec $(N $k) pg/G_${k}_top.pg
      python3 tie246.py v xi $(N $k) pg/G_${k}_top.pg
    done ;;
  n5b)
    t=$(mktemp -d)
    for k in 3 4 5 6 7 8 9; do
      echo "N5B G_${k}_top.pg mode spec $(python3 $TRUNK/experiments/n5-second/n5b.py pg/G_${k}_top.pg $t/o.sol --mode spec 2>&1 | tail -1)"
    done
    for k in 3 4 5 6; do
      echo "N5B G_${k}_r104.pg mode spec $(python3 $TRUNK/experiments/n5-second/n5b.py pg/G_${k}_r104.pg $t/o.sol --mode spec 2>&1 | tail -1)"
    done
    rm -rf "$t" ;;
  zchk)
    for k in 3 4 5 6 7; do
      python3 zchk246.py $OINK spec pg/G_${k}_top.pg
      python3 zchk246.py $OINK xi pg/G_${k}_top.pg
    done
    ZCHK246_CTRL=1 python3 zchk246.py $OINK spec pg/G_3_top.pg ;;
  trace)
    for k in 3 4 5 6 7 8; do python3 trace246.py spec $GK/G_${k}_renum.json r104 top; done
    for k in 3 4 5 6; do python3 trace246.py xi $GK/G_${k}_renum.json top; done ;;
  rand)
    python3 rand246.py 1 300 6 3 3
    python3 rand246.py 2 300 8 4 3
    python3 rand246.py 3 200 10 4 2 2
    python3 rand246.py files ../r243/inst/H5PLUS_L5.json ../r244/inst/LAD_d5_k3_s13.json $GK/G_3_renum.json $GK/G_4_renum.json $GK/G_5_renum.json $GK/G_6_renum.json
    python3 rand246.py perm 7 100 4 $GK/G_4_renum.json
    python3 rand246.py perm 8 60 6 $GK/G_5_renum.json
    RAND246_CTRL=1 python3 rand246.py 1 300 6 3 3
    RAND246_CTRL=1 python3 rand246.py perm 7 100 4 $GK/G_4_renum.json ;;
  ctrl)
    for k in 3 4 5; do TIE246_CTRL=1 python3 tie246.py s spec $(N $k) pg/G_${k}_top.pg; done ;;
  k10)
    python3 tie246.py s spec $(N 10) pg/G_10_top.pg
    t=$(mktemp -d); echo "N5B G_10_top.pg mode spec $(python3 $TRUNK/experiments/n5-second/n5b.py pg/G_10_top.pg $t/o.sol --mode spec 2>&1 | tail -1)"; rm -rf "$t" ;;
  *) echo "unknown job $J"; exit 2 ;;
esac
echo "JOB END $J $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$O" 2>&1
tail -1 "$O"
