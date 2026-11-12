#!/bin/bash
# L-COMP box 44 item 2, the cross: L-NEW's OWN counter code (claude/l-new 311bbf81 box208/level208.py --hist: 16 counters; box209/plat209.py
# --hist: 9 counters) on the runs of MY builder + MY engine (lev44.py's history dump, DUMP44). Resumable per genome; the dumps are deleted.
# env LNEW209 = an archive of claude/l-new 311bbf81 with experiments/new, experiments/si/si.py, experiments/harness, experiments/n5-second,
# experiments/hard-families.  Usage: run44c.sh records | corpus | dead | mine
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
: "${LNEW209:?set LNEW209}"; N="$LNEW209/experiments/new"; mkdir -p out
main() {
T=$(mktemp -d)
REC="$N/box203/inst/MWR4_2.json $N/box203/inst/MWR8_2.json $N/box203/inst/MWR16_2.json $N/box206/inst/CW4_n.json $N/box206/inst/CW8_n.json $N/box206/inst/CW16_n.json
$N/box206/inst/CWRR4_n.json $N/box206/inst/CWRR8_n.json $N/box206/inst/CWRR16_n.json $N/box206/inst/CWRQ8_n.json $N/box203/inst/K1F21_n48.json $N/box204/inst/K1F34_n84.json
$N/box203/inst/K1C16_n400.json $N/box206/inst/K1L7_n48.json $N/box206/inst/K1L10_n48.json $N/box206/inst/K1D4_n48.json $N/box206/inst/BLKX23_n48.json $N/box206/inst/BLKX26_n48.json
$N/box204/inst/B400_r32_a13d9661.json $N/box207/inst/CFI3_n48.json $N/box207/inst/RINT_n48.json $N/box202/k1fail_202.json $N/box205/inst/naive_k1_s71.json
$N/box203/inst/ST4_k1.json $N/box203/inst/ST8_k1.json"
case "$1" in
records) L="$REC" ;;
corpus)  L="$(ls $N/box202/inst/*.json)" ;;
dead)    L="$N/box191/inst/DEAD_SEG2P_d4_N8.json $N/box191/inst/DEAD_SEG2P_d7_N14.json $N/box191/inst/DEAD_SEG2P_d9_N18.json" ;;
mine)    L="$(ls ../box39/inst/*.json ../box40/inst/*.json ../box42/inst/CL0.json ../box42/inst/CL30.json)" ;;
*) echo usage; exit 2 ;;
esac
lo=out/lnewctr44_level_$1.out; po=out/lnewctr44_plat_$1.out; touch $lo $po
for f in $L; do
  b=$(basename $f)
  grep -q "^$b " $lo && grep -q "^plat3 hist $b " $po && continue
  DUMP44=$T BREF=T python3 lev44.py $f > /dev/null 2>> out/run44c.err || { echo "$b MY ENGINE FAILED" >> out/run44c.err; continue; }
  grep -q "^$b " $lo || (cd $N/box208 && python3 -I level208.py --hist $T/$b) >> $lo 2>> out/run44c.err
  grep -q "^plat3 hist $b " $po || (cd $N/box209 && python3 -I plat209.py --hist $T/$b) >> $po 2>> out/run44c.err
  rm -f $T/$b
done
rmdir $T 2>/dev/null
echo "run44c $1 done: $(wc -l < $lo) level rows, $(wc -l < $po) plat rows"
}
main "$@"
