#!/bin/bash
# L-COMP box 45 item (b): climbs on the per-gate Λ-quiet flip maximum / (N + M) (climb45.py) in three size bands, to see whether the best
# ratio grows with size (a per-gate count beyond linear would show as a rising ratio). Resumable (climb45.py OUT.state).
# Usage: run45b.sh 1 | 2 | 3   (band 1: 100..130, seeds gen37(3), MWR(3); band 2: 185..220, gen37(6), MWR(6); band 3: 275..320, gen37(9), MWR(9))
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
R=${RESTARTS:-4}; ST=${STEPS:-400}
case "$1" in
1) python3 climb45.py B1 100 130 $R $ST 4541 out/climb45_B1.log inst/seed_gen37_3.json inst/seed_MWR_3.json ;;
2) python3 climb45.py B2 185 220 $R $ST 4542 out/climb45_B2.log inst/seed_gen37_6.json inst/seed_MWR_6.json ;;
3) python3 climb45.py B3 275 320 $R $ST 4543 out/climb45_B3.log inst/seed_gen37_9.json inst/seed_MWR_9.json ;;
*) echo usage; exit 2 ;;
esac
echo "run45b $1 done"
}
main "$@"
