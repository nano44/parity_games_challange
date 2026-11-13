#!/bin/bash
# L-COMP box 46 item 3: climbs on Wused / (N + M) over Ξ-cyclic genomes (climb46.py), four bands, two seeds each (inst/seeds46/, chosen from
# out/seedcand46.out and the random set: the best Ξ-cycle-USING genomes of item 2 in each band). Resumable (climb46.py OUT.state).
# env LNEW212 (sec46.py's rfd212). Usage: run46g.sh 0 | 1 | 2 | 3
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
R=${RESTARTS:-2}; ST=${STEPS:-300}; S=inst/seeds46
case "$1" in
0) python3 climb46.py B0 60 80 $R $ST 4640 out/climb46_B0.log $S/xrand_s4611_nm60_px0.0_215.json $S/xrand_s4612_nm160_px0.3_180.json ;;
1) python3 climb46.py B1 105 135 $R $ST 4641 out/climb46_B1.log $S/H5_x0_glo_blo_p0.json $S/RECF4_x32_glo_blo_p0.json ;;
2) python3 climb46.py B2 130 160 $R $ST 4642 out/climb46_B2.log $S/H6_x0_glo_blo_p0.json $S/H6_x0_glo_bhi_p0.json ;;
3) python3 climb46.py B3 155 185 $R $ST 4643 out/climb46_B3.log $S/HIT7_x0_glo_blo_p0.json $S/HIT7_x48_glo_blo_p0.json ;;
*) echo usage; exit 2 ;;
esac
echo "run46g $1 done"
}
main "$@"
