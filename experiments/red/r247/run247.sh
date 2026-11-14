#!/usr/bin/env bash
# L-RED 71 R247 runner. Usage: run247.sh JOB   env TRUNK (tree of trunk with experiments/hard-families/pgsolver_port.py) for job pgs.
# Outputs out/<job>.out; a job whose output ends with «JOB END» is skipped. Jobs: engine viol decoy patch pgs
set -uo pipefail
cd "$(dirname "$0")"; mkdir -p out; J="$1"; O="out/$J.out"
if [ -f "$O" ] && tail -1 "$O" | grep -q "^JOB END"; then echo "skip $J"; exit 0; fi
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
{
case "$J" in
  engine)   # Howard on Friedmann's G_n from iota (9 * 2^n - 10); RF on G_n, on Gamma3(G_k) and on Gamma3^top(G_k) from S3
    for n in 1 2 3 4 5 6 7; do
      python3 ../gens_red.py friedmann_Gn $n > $T/g.pg
      [ $n -le 6 ] && python3 si247.py howard $T/g.pg file | sed "s/g.pg/friedmann_G$n/"
      python3 si247.py rf $T/g.pg file | sed "s/g.pg/friedmann_G$n/"
    done
    for k in 3 4 5 6 7 8; do
      python3 ../r246/g3_246.py r104 ../r244/gk/G_${k}_renum.json $T/a.pg > /dev/null
      python3 si247.py rf $T/a.pg s3 | sed "s/a.pg/Gamma3_G$k/"
      python3 si247.py rf ../r246/pg/G_${k}_top.pg s3
      [ $k -le 6 ] && python3 si247.py howard ../r246/pg/G_${k}_top.pg s3
    done ;;
  viol)
    for n in 2 3 4; do python3 ../gens_red.py friedmann_Gn $n > $T/g.pg; echo "== friedmann_G$n"; python3 viol247.py $T/g.pg $([ $n -eq 3 ] && echo 16 || echo 0); done
    python3 ../gens_red.py friedmann_Gn 2 > $T/g.pg; echo "== RF trace on friedmann_G2"; python3 trace247.py $T/g.pg rf ;;
  decoy)
    for n in 2 3 4; do
      for d in none all 1; do
        if [ $d = none ]; then python3 fvar247.py $n $T/g.pg; else python3 fvar247.py $n $T/g.pg decoy=$d; fi
        for rule in howard rf; do
          python3 - $T/g.pg $rule $n $d <<'PY'
import sys, os
sys.path[:0] = [".", "../r237"]
import si247, rf247
fn, rule, n, d = sys.argv[1:5]
e = si247.SI(*si247.parse(fn)); st = e.s3(); st.update(si247.read_start(fn)); r = e.run(rule, st)
print("DECOY247 friedmann_G" + n, "decoy", d, "n", e.n, "rule", rule, "iterations", r["its"], "even_wins", sum(1 for w in r["win"] if w == 0), flush=True)
PY
        done
      done
    done ;;
  patch)
    for opts in "" "buf=1" "buf=2" "noCS" "buf=2 noCS"; do
      for n in 1 2 3 4 5; do
        python3 fvar247.py $n $T/g.pg $opts
        echo "PATCH247 opts [$opts] n $n $(python3 si247.py rf $T/g.pg file | cut -d' ' -f9,10) $(python3 si247.py howard $T/g.pg file | cut -d' ' -f5,9,10)"
      done
    done ;;
  pgs)
    for fam in switchbestexp switchallexp; do
      for N in 1 2 3 4 5 6 7 8 9 10 12 14 16; do
        python3 $TRUNK/experiments/hard-families/pgsolver_port.py $fam $N > $T/g.pg
        python3 si247.py rf $T/g.pg s3 | sed "s/g.pg/${fam}_N$N/"
        [ $N -le 6 ] && python3 si247.py howard $T/g.pg s3 | sed "s/g.pg/${fam}_N$N/"
      done
    done ;;
  *) echo "unknown job $J"; exit 2 ;;
esac
echo "JOB END $J $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$O" 2>&1
tail -1 "$O"
