#!/bin/bash
# L-COMP box 46, successor 22, WORK item 1 (Lead brief + «go» 06:15Z 2026-11-13): the W_ess climb (climb46e.py, objective W_ess / (N + M),
# Ξ-cyclic genomes only, must-0 counters of win46e, sec46.py = n5b spec + rfd212 on every new global best) SEEDED at the B3 best
# out/climb46/BEST_B3_WU151_NM163_e934d333.json (W_ess 151 at N + M 163). Resumable (climb46e.py OUT.state). env LNEW212.
# A3: climb46s.py (objective W_ess absolute, smaller N + M on ties), same seed and band as S2.
# Usage: run46i.sh S1 | S2 | A3
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
: "${LNEW212:?set LNEW212}"
R=${RESTARTS:-2}; ST=${STEPS:-300}; S=out/climb46/BEST_B3_WU151_NM163_e934d333.json
case "$1" in
S1) python3 climb46e.py S1 140 190 $R $ST 4651 out/climb46e_S1.log $S ;;
S2) python3 climb46e.py S2 150 260 $R $ST 4652 out/climb46e_S2.log $S ;;
A3) python3 climb46s.py A3 150 260 $R $ST 4653 out/climb46s_A3.log $S ;;   # absolute W_ess (climb46s.py), growth probe
*) echo usage; exit 2 ;;
esac
echo "run46i $1 done"
}
main "$@"
