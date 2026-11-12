#!/bin/bash
# L-COMP box 44 item 1: Lemma WRAP / FREE-REACH (claude/l-si 26704e01) on my builder and my engine. Resumable (finished rows are skipped;
# the long runs checkpoint). env LSI104 = an archive of claude/l-si 26704e01 (experiments/si/box104/inst).
# Usage: run44a.sh rand | order | cls | fam | famlsi | free | ctrl | spec | speclsi | w4
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
: "${LSI104:?set LSI104}"; I="$LSI104/experiments/si/box104/inst"; mkdir -p out
main() {
case "$1" in
rand)   VALB=1 python3 wchk44.py json $I/rand300.json out/wrap44_rand300.out ;;
order)  ORDER=rev python3 wchk44.py json $I/rand300.json out/wrap44_rand300_rev.out
        ORDER=rand:1 python3 wchk44.py json $I/rand300.json out/wrap44_rand300_rand1.out
        N5XI44_CTRL=1 python3 wchk44.py json $I/rand300.json out/wrap44_rand300_tiemin.out ;;
fam)    for n in 2 3 4 5 6 7 8; do VALB=1 python3 wchk44.py fam switchall $n out/wrap44_fam.out $I/W_$n.pg; done
        for n in 1 2 3 4; do VALB=1 python3 wchk44.py fam lmcs $n out/wrap44_fam.out $I/WL_$n.pg; done
        for n in 5 6 7 8; do VALB=1 python3 wchk44.py fam lmcs $n out/wrap44_fam.out; done
        for n in 1 2 3 4 5 6; do VALB=1 python3 wchk44.py fam lmcst4 $n out/wrap44_fam.out; done ;;
famlsi) for n in 2 3 4 5 6; do ORDER=lsi python3 wchk44.py fam switchall $n out/wrap44_famlsi.out $I/W_$n.pg; done
        for n in 7 8; do NORUN=1 ORDER=lsi python3 wchk44.py fam switchall $n out/wrap44_famlsi.out $I/W_$n.pg; done
        for n in 1 2 3 4; do ORDER=lsi python3 wchk44.py fam lmcs $n out/wrap44_famlsi.out $I/WL_$n.pg; done ;;
free)   for n in 2 3 4 5 6 7 8; do VALB=${VALBF:-10} python3 free44.py $I/F_$n.pg $n out/free44.out; done ;;
ctrl)   for c in 1 2 3 4 5; do CTRL=$c python3 wchk44.py json $I/rand300.json out/wrap44_ctrl$c.out 0 100; done
        for c in 1 2 3 4; do CTRL=$c python3 free44.py $I/F_2.pg 2 out/free44_ctrl.out; done ;;
spec)   MODE=spec python3 wchk44.py json $I/rand300.json out/wrap44_rand300_spec.out
        for n in 2 3 4 5 6; do MODE=spec python3 wchk44.py fam switchall $n out/wrap44_fam_spec.out; MODE=spec python3 free44.py $I/F_$n.pg $n out/free44_spec.out; done
        for n in 1 2 3 4 5 6; do MODE=spec python3 wchk44.py fam lmcs $n out/wrap44_fam_spec.out; done ;;
cls)    for m in rev rand:1 tiemin howard; do python3 cls44.py $I/rand300.json $m > out/cls44_${m/:/}.out.tmp && mv out/cls44_${m/:/}.out.tmp out/cls44_${m/:/}.out; done ;;
speclsi) MODE=spec ORDER=lsi python3 wchk44.py json $I/rand300.json out/wrap44_rand300_spec_lsi.out
        for n in 2 3 4 5 6; do MODE=spec ORDER=lsi python3 wchk44.py fam switchall $n out/wrap44_fam_spec_lsi.out $I/W_$n.pg; done
        for n in 1 2 3 4; do MODE=spec ORDER=lsi python3 wchk44.py fam lmcs $n out/wrap44_fam_spec_lsi.out $I/WL_$n.pg; done
        for n in 5 6; do MODE=spec ORDER=lsi python3 wchk44.py fam lmcs $n out/wrap44_fam_spec_lsi.out; done ;;
w4)     { python3 w4chk44.py json $I/rand300.json; W4CTRL=1 python3 w4chk44.py json $I/rand300.json; MODE=spec python3 w4chk44.py json $I/rand300.json
          for n in 2 3 4 5 6; do python3 w4chk44.py fam switchall $n; done; for n in 1 2 3 4 5 6; do python3 w4chk44.py fam lmcs $n; done
          W4CTRL=1 python3 w4chk44.py fam lmcs 3; } > out/w4chk44.out.tmp && mv out/w4chk44.out.tmp out/w4chk44.out ;;
*) echo usage; exit 2 ;;
esac
echo "run44a $1 done"
}
main "$@"
