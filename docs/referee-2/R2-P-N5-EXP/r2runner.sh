#!/bin/bash
# REFEREE-2 successor 42: tests of the lane's two runners at claude/l-red-b 24f4d436 (R2-P-N5-EXP.md Addendum 2: item A1.2 of
# Addendum 1 and item F-4). Own script; the lane's files are unpacked into WORKDIR and only run there, never edited.
# Usage (from the repository root): bash docs/referee-2/R2-P-N5-EXP/r2runner.sh WORKDIR [every]
#   WORKDIR  a new directory outside the working tree.
#   T1  run_b6b.sh with a RELATIVE root, stage gen 4          expected: exit 0, 2 genomes written
#   T2  run_b6b.sh, stage n5 3 on a root without archives     expected: exit 1 (a failing stage is reported)
#   T3  run_b6b.sh, stage gen, with a python3 that exits 3    expected: exit 1
#   T4  run_b6fix.sh, stage exh, with the same python3        FOUND: exit 0 and an empty output file (item F-4)
#   T5  run_b6fix.sh, stage exh, RELATIVE outdir              expected: exit 0, prefix_exh.out byte-equal to the pinned file
#   every (optional, about 2 minutes): run_b6fix.sh OUT every; each of its eleven outputs compared byte for byte with the pinned file
# Exit 0 iff the pattern is the recorded one (exits 0, 1, 1, 0, 0; T5 equal; with «every»: 11 equal).
set -u
C=24f4d436a0fea1f62ae736f20f78ff9e84333a90
W="$1"; MODE="${2:-}"; mkdir -p "$W" || exit 2; W="$(cd "$W" && pwd)"
git archive "$C" experiments/red-b > "$W/lane.tar" || { echo "git archive failed"; exit 2; }
tar -x -C "$W" -f "$W/lane.tar" || exit 2
mkdir -p "$W/stub"; printf '#!/bin/sh\nexit 3\n' > "$W/stub/python3"; chmod +x "$W/stub/python3"
cd "$W" || exit 2
bad=0; D=experiments/red-b/data/b6b/out
strip() { tail -n 1 "$1" > "$1.last"; sed 's/ done [0-9TZ:-]*/ done/' "$1.last"; }
bash experiments/red-b/run_b6b.sh relroot gen 4 > t1.log 2>&1; e=$?; n=$(find relroot/G -name 'G_*.json' 2>/dev/null > t1.files; wc -l < t1.files)
echo "T1 run_b6b.sh relative-root gen 4: exit $e genomes $n | $(strip t1.log)"; [ "$e" = 0 ] && [ "$n" = 2 ] || bad=1
bash experiments/red-b/run_b6b.sh relroot n5 3 > t2.log 2>&1; e=$?
echo "T2 run_b6b.sh n5 3 without archives: exit $e | $(strip t2.log)"; [ "$e" = 1 ] || bad=1
PATH="$W/stub:$PATH" bash experiments/red-b/run_b6b.sh relroot2 gen 3 > t3.log 2>&1; e=$?
echo "T3 run_b6b.sh gen 3 with a failing python3: exit $e | $(strip t3.log)"; [ "$e" = 1 ] || bad=1
PATH="$W/stub:$PATH" bash experiments/red-b/run_b6fix.sh fixout exh > t4.log 2>&1; e=$?; z=$(wc -c < fixout/prefix_exh.out)
echo "T4 run_b6fix.sh exh with a failing python3: exit $e output-bytes $z | $(strip t4.log)"; [ "$e" = 0 ] && [ "$z" = 0 ] || bad=1
bash experiments/red-b/run_b6fix.sh fixout2 exh > t5.log 2>&1; e=$?; cmp -s fixout2/prefix_exh.out $D/prefix_exh.out; q=$?
echo "T5 run_b6fix.sh exh relative outdir: exit $e cmp-with-pinned $q | $(strip t5.log)"; [ "$e" = 0 ] && [ "$q" = 0 ] || bad=1
if [ "$MODE" = every ]; then
  bash experiments/red-b/run_b6fix.sh fixall every > t6.log 2>&1; e=$?; eq=0
  for f in prefix_run prefix_all prefix_off prefix_drive prefix_loc prefix_stable prefix_exh prefix_u0 brtie width prefix_ctrl; do
    if cmp -s fixall/$f.out $D/$f.out; then eq=$((eq + 1)); else echo "EVERY $f.out DIFFERS"; fi
  done
  echo "EVERY run_b6fix.sh every: exit $e byte-equal $eq of 11 | $(strip t6.log)"; [ "$e" = 0 ] && [ "$eq" = 11 ] || bad=1
fi
echo "RESULT pattern-as-recorded $((1 - bad))"
exit $bad
