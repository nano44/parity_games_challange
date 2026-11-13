#!/bin/bash
# REFEREE successor 36: reproduces docs/referee/scratch/k1p_logs/*.out (first review of P-N5-KEY1P, l-new 44775605).
# Run from the repository root: bash docs/referee/scratch/k1p_logs/s36_k1p_run.sh   (resumable: a stage with its .out present is skipped)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
T="$HERE/.."
C=44775605d471b4f635a8c227b65744ac34bc6059
TR=5d7aab0f19f664034567c3bf4f41bcf9e1684d20
W="$(mktemp -d)"
mkdir -p "$W/inst" "$W/rec"
for f in DBL4_d20_F30 H5_d20_F62 H6_d24_F126 HIT7_d28_F254 RECF4_d20_F60; do git show $C:experiments/new/box212/inst/$f.json > "$W/inst/$f.json"; done
for f in $(git ls-tree -r --name-only $C experiments/new/box217/out/rec/ | grep '\.json$'); do git show $C:$f > "$W/rec/$(basename $f)"; done
git show $C:docs/new/P-N5-KEY1P.md > "$W/P-N5-KEY1P.md"; git show $TR:docs/RESULTS.md > "$W/RESULTS.md"
K="python3 -I $T/k1p.py"; N5="python3 -I $T/gkx_n5.py"
st() { [ -s "$HERE/$1.out" ] && { echo "skip $1"; return 1; }; echo "run $1"; return 0; }
st gk && $K gk 3 4 5 6 7 8 9 10 > "$HERE/gk.tmp" && mv "$HERE/gk.tmp" "$HERE/gk.out"
st towers && $K file "$W"/inst/*.json > "$HERE/towers.tmp" && mv "$HERE/towers.tmp" "$HERE/towers.out"
st rec && $K file "$W"/rec/*.json > "$HERE/rec.tmp" && mv "$HERE/rec.tmp" "$HERE/rec.out"
st rand && { $K rand 1 3000; $K rand 2 3000; } > "$HERE/rand.tmp" && mv "$HERE/rand.tmp" "$HERE/rand.out"
st mut && $K mut 7 100 "$W"/inst/*.json > "$HERE/mut.tmp" && mv "$HERE/mut.tmp" "$HERE/mut.out"
st lift && { $K lift 0 "$W/inst/H5_d20_F62.json"; $K lift 10 "$W/inst/H5_d20_F62.json"; $K lift 40 "$W/inst/H5_d20_F62.json"; } > "$HERE/lift.tmp" && mv "$HERE/lift.tmp" "$HERE/lift.out"
st ctrl && { for c in howard down a2half a3all a4any w0 perm; do $K file "$W/inst/HIT7_d28_F254.json" --ctrl $c; done; } > "$HERE/ctrl.tmp" && mv "$HERE/ctrl.tmp" "$HERE/ctrl.out"
st quotes && python3 -I "$T/k1p_quotes.py" "$W/P-N5-KEY1P.md" "$W/RESULTS.md" > "$HERE/quotes.tmp" && mv "$HERE/quotes.tmp" "$HERE/quotes.out"
st n5_towers && $N5 file "$W"/inst/*.json > "$HERE/n5_towers.tmp" && mv "$HERE/n5_towers.tmp" "$HERE/n5_towers.out"
st n5_lift && $N5 lift 10 "$W/inst/H5_d20_F62.json" > "$HERE/n5_lift.tmp" && mv "$HERE/n5_lift.tmp" "$HERE/n5_lift.out"
st n5_ctl && { for c in lastfb revE rank start; do $N5 file "$W/inst/H5_d20_F62.json" --ctl $c; done; } > "$HERE/n5_ctl.tmp" && mv "$HERE/n5_ctl.tmp" "$HERE/n5_ctl.out"
st n5_rec && $N5 file "$W"/rec/*.json > "$HERE/n5_rec.tmp" && mv "$HERE/n5_rec.tmp" "$HERE/n5_rec.out"
rm -rf "$W"
echo done
