#!/bin/bash
# L-COMP box 46 item 2: win46.py on the Ξ-cyclic tower variants (mkx46.py, inst/xtower/). Resumable per genome. Usage: run46d.sh
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
O=out/win46_xtower.out; touch $O
for f in inst/xtower/*.json; do b=$(basename $f); grep -q "^$b " $O || python3 win46.py $f >> $O 2>> $O.err; done
echo "run46d done: $(wc -l < $O) rows"
}
main "$@"
