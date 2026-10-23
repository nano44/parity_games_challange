#!/usr/bin/env bash
# LRAT certificate for an n5.py UNSAT result: rebuild the CNF from the checkpointed graph set (n5.py --cnf), solve it
# with the CaDiCaL binary (apt cadical 1.7.4) writing a text LRAT proof, check the proof with the independent checker
# experiments/sat-hard/lrat_check.py (L-COMP). Usage: lrat.sh N D CONV MODE K   -> out/<case>.{cnf,lrat,lrat.log}
set -uo pipefail
cd "$(dirname "$0")"
case="$4_$3_n$1_d$2_k$5"
python3 n5.py "$1" "$2" "$3" "$4" "$5" --cnf-only || exit 1
cadical --lrat=true --binary=false -q "out/$case.cnf" "out/$case.lrat"; rc=$?
echo "cadical exit $rc (20 = UNSAT)"
[ $rc -eq 20 ] || exit 1
python3 ../sat-hard/lrat_check.py "out/$case.cnf" "out/$case.lrat" | tee "out/$case.lrat.log"
echo "proof lines: $(wc -l < out/$case.lrat); cnf sha256: $(sha256sum out/$case.cnf | cut -c1-64)" | tee -a "out/$case.lrat.log"
