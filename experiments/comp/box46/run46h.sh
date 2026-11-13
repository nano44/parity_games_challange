#!/bin/bash
# L-COMP box 46 item 3: wess / W_ess (win46e.py) on every seed (inst/seeds46) and the final best of every climb log (B0-B3, E3).
# One line per genome in out/wess46.out (resumable). Usage: run46h.sh
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
O=out/wess46.out; touch $O
L=$(for f in out/climb46_B*.log out/climb46e_E3.log; do [ -f $f ] && grep -o '^BEST [^ ]*\|^ALERT BEST [^ ]*' $f | tail -1 | awk '{print $NF}' | sed "s#^#$( [ $f = out/climb46e_E3.log ] && echo out/climb46e || echo out/climb46)/#"; done)
for f in inst/seeds46/*.json $L; do b=$(basename $f); grep -q "^$b " $O || python3 win46e.py $f >> $O 2>> $O.err; done
echo "run46h done: $(wc -l < $O) rows"
}
main "$@"
