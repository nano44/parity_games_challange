#!/bin/bash
# L-COMP box 43 item 3: the ONE-gate family TMWR(n) := TAIL_2(MWR(n)) (tail43.py on L-RED's MWR(n) = box37/genmw229_copy.py WTGT=R n 2;
# n = 4 reproduces box40/inst/MWR4_2.json, sha1 856d369b), and TAIL_2 of other frozen genomes. No search.
cd "$(dirname "$0")"; mkdir -p inst; T=$(mktemp -d)
for n in 4 8 16 32 48; do WTGT=R python3 ../box37/genmw229_copy.py $n 2 > $T/MWR$n.json 2>/dev/null; python3 tail43.py $T/MWR$n.json 2 inst/TMWR$n.json; cp $T/MWR$n.json inst/MWR${n}_2.json; done
python3 tail43.py ../box40/inst/DHIB26_2804.json 2 inst/TDHIB26.json; python3 tail43.py ../box40/inst/C6G8_n54.json 2 inst/TC6G8.json
[ -n "${EXTRA:-}" ] && python3 tail43.py "$EXTRA" 2 inst/TREC.json
rm -rf $T; (cd inst && sha1sum TMWR*.json MWR*_2.json TDHIB26.json TC6G8.json $( [ -f TREC.json ] && echo TREC.json ) > SHA1SUMS.tail43)
