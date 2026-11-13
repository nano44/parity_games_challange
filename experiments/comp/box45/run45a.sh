#!/bin/bash
# L-COMP box 45 item (a): depthNS (deep45.py) — (1) TAIL invariance flip by flip on 8 pairs (G, TAIL_2(G)) + 2 controls; (2) the counts on the
# frozen sets. Resumable per genome / pair. env LNEW209 = an archive of claude/l-new 311bbf81 (experiments/new ...).
# Usage: run45a.sh tail | frozen | big | rand
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out inst
main() {
B43=../box43/inst
per() { local out="out/$1"; shift; touch "$out"; for f in "$@"; do b=$(basename $f); grep -q "^$b " "$out" || python3 deep45.py $f >> "$out" 2>> "$out.err"; done; }
case "$1" in
tail)
  [ -f inst/TRWX.json ] || python3 ../box43/tail43.py ../box40/inst/RWX_n95.json 2 inst/TRWX.json > /dev/null
  touch out/tail45.out
  for p in "$B43/MWR4_2.json $B43/TMWR4.json" "$B43/MWR8_2.json $B43/TMWR8.json" "$B43/MWR16_2.json $B43/TMWR16.json" \
           "../box40/inst/C6G8_n54.json $B43/TC6G8.json" "../box36/out/climb/BEST_C300_r34_C17_30d4ea76.json $B43/TREC.json" \
           "../box40/inst/DHIB26_2804.json $B43/TDHIB26.json" "../box40/inst/RWX_n95.json inst/TRWX.json" "$B43/MWR32_2.json $B43/TMWR32.json"; do
    set -- $p; grep -q "^TAIL45 $(basename $1) -> $(basename $2) .*ctrl 0$" out/tail45.out || python3 deep45.py --tail $1 $2 >> out/tail45.out
  done
  for p in "$B43/MWR8_2.json $B43/TMWR8.json" "../box40/inst/DHIB26_2804.json $B43/TDHIB26.json"; do
    set -- $p; grep -q "^TAIL45 $(basename $1) -> $(basename $2) .*ctrl 1$" out/tail45.out || CTRL=1 python3 deep45.py --tail $1 $2 >> out/tail45.out
  done ;;
frozen)
  N="$LNEW209/experiments/new"
  per deep45_mine.out ../box40/inst/*.json ../box39/inst/*.json ../box41/inst/*.json
  per deep45_lnew.out $N/box203/inst/MWR4_2.json $N/box206/inst/CW*_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json $N/box206/inst/K1L7_n48.json \
     $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX2*_n48.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json \
     $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json $N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json $N/box202/inst/*.json $N/box203/inst/K1C16_n400.json $N/box204/inst/B400_r32_a13d9661.json
  per deep45_fam.out ../box42/inst/CL0.json ../box42/inst/CL8.json ../box42/inst/CL16.json ../box42/inst/CL30.json $B43/D18_k4.json $B43/D18_k8.json $B43/D18_k16.json \
     $B43/D10_k16.json $B43/D80_k16.json $B43/DHIB26_k0.json $B43/TMWR4.json $B43/TMWR8.json $B43/TMWR16.json $B43/TC6G8.json $B43/TREC.json $B43/TDHIB26.json inst/TRWX.json ;;
big)
  per deep45_big.out ../box42/inst/CL45.json $B43/D10_k32.json $B43/D18_k32.json $B43/D80_k32.json $B43/TMWR32.json ../box42/inst/CL90.json $B43/D10_k64.json $B43/D80_k64.json ;;
rand)
  for px in 0.6 0.3 0.0; do python3 rand45.py 4511 300 60 $px out/deep45_rand.out; done
  python3 rand45.py 4512 200 160 0.3 out/deep45_rand.out ;;
*) echo usage; exit 2 ;;
esac
echo "run45a $1 done"
}
main "$@"
