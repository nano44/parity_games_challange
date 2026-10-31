#!/bin/bash
# REFEREE s20: src_probe over box 83/50b lists (sbcg.lst best-reward start; alt_all.lst listed start), MAXN 100; MUT 0 and MUT 2.
cd "$(dirname "$0")/../../../../experiments"
P=../docs/referee/scratch/src_probe.py; O=../docs/referee/scratch/src_logs
one() { f=$O/runs$MUT/$(echo "$1" | tr '/' '_').${2:+st}.txt; ( echo "GAME $1 ${2:-best}"; if [ -n "$2" ]; then STARTF=$2 ONLYSTART=1 timeout 3600 python3 -I $P $1; else NOSTART=1 timeout 3600 python3 -I $P $1; fi 2>&1; echo "RC $?" ) > $f; }
export -f one; export P O
for M in 0 1; do export MUT=$M; mkdir -p $O/runs$M
grep -v '^#' new/box59/sbcg.lst | grep . | xargs -P 4 -L 1 bash -c 'one "$@"' _
xargs -P 4 -L 1 bash -c 'one "$@"' _ < si/root/logs/alt_all.lst
cat $O/runs$M/*.txt | awk '/^(GAMES|wruns|trans|PC_chk|IDX_chk|LEX_chk|multi_tight|skip_big|maxit|CYC_case2|CYC_case2_Pb) /{s[$1]+=$2} /_V /{v[$1]+=$2} /^RC /{rc[$2]++} /^STAT maxblock/{if($3>m)m=$3} /^STAT maxtail/{if($3>mt)mt=$3} END{for(k in s)print k,s[k]; for(k in v)print k,v[k]; for(k in rc)print "RC"k,rc[k]; print "maxblock",m; print "maxtail",mt}' > $O/sum$M.txt
grep -h '^EX' $O/runs$M/*.txt | head -10 >> $O/sum$M.txt; echo "DONE $M" >> $O/sum$M.txt
done
