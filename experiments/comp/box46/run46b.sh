#!/bin/bash
# L-COMP box 46 item 1, second side: L-NEW's rfd212.py (claude/l-new 5fa64fe6 box212, run unchanged with python3 -I from its own directory,
# RFD_MODE=spec) on the same 86 genomes as run46a.sh. One line per genome appended to out/rfd212_mine.out (resumable). env LNEW212.
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1
main() {
: "${LNEW212:?set LNEW212}"; N="$LNEW212/experiments/new"; O=$(pwd)/out/rfd212_mine.out; touch "$O"
for f in $N/box212/inst/*.json $(awk '{print $1}' out/win46_records.out out/win46_dead.out out/win46_corpus.out | while read b; do ls $N/box20[2-7]/inst/$b $N/box202/$b $N/box191/inst/$b 2>/dev/null | head -1; done); do
  b=$(basename $f); grep -q "^$b " "$O" && continue
  (cd $N/box212 && RFD_MODE=spec timeout 1800 python3 -I rfd212.py "$f") >> "$O" 2>> "$O.err"
done
echo "run46b done: $(wc -l < "$O") rows"
}
main "$@"
