#!/bin/bash
# L-COMP box 44 item 3: climbs on T3 / (N + M) in the band [LO, HI] (default 280..320), two seed streams. Resumable (climb44.py OUT.state).
# Usage: run44d.sh 1 | 2   (stream 1: RNG seed 4431, seeds gen37(9), MWR(10); stream 2: RNG seed 4432, seeds gen37(10), MWR(9))
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
LO=${LO:-280}; HI=${HI:-320}; R=${RESTARTS:-4}; ST=${STEPS:-500}
case "$1" in
1) python3 climb44.py S1 $LO $HI $R $ST 4431 out/climb44_S1.log inst/seed_gen37_9.json inst/seed_MWR_10.json ;;
2) python3 climb44.py S2 $LO $HI $R $ST 4432 out/climb44_S2.log inst/seed_gen37_10.json inst/seed_MWR_9.json ;;
*) echo usage; exit 2 ;;
esac
echo "run44d $1 done"
}
main "$@"
