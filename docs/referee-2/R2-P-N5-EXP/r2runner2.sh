#!/bin/bash
# REFEREE-2 successor 42: tests of the REPAIRED runner run_b6fix.sh at claude/l-red-b 10dfedb6 (fixes entry 7.4; item F-4 of
# R2-P-N5-EXP.md Addendum 2). Own script; the lane's files are unpacked into WORKDIR and only run there, never edited.
# Usage (from the repository root): bash docs/referee-2/R2-P-N5-EXP/r2runner2.sh WORKDIR
#   U1  stage exh, a python3 that always exits 3            expected: exit 1, no prefix_exh.out left
#   U2  stage exh, a python3 that fails only for «exh 4»    expected: exit 1, prefix_exh.out = the pinned file's first line only
#   U3  stage ctrl, a python3 that fails only for «run 5»   expected: exit 1, no prefix_ctrl.out left (the 2nd of its ten commands)
#   U4  an unknown stage                                    expected: exit 2
#   U5  every (about 2 minutes)                             expected: exit 0, «failures 0», 11 outputs byte-equal to the pinned files
# Exit 0 iff every expectation holds.
set -u
C=10dfedb6
W="$1"; mkdir -p "$W" || exit 2; W="$(cd "$W" && pwd)"
git archive "$C" experiments/red-b > "$W/lane.tar" || { echo "git archive failed"; exit 2; }
tar -x -C "$W" -f "$W/lane.tar" || exit 2
REAL="$(command -v python3)"; mkdir -p "$W/s1" "$W/s2" "$W/s3"
printf '#!/bin/sh\nexit 3\n' > "$W/s1/python3"
printf '#!/bin/sh\ncase "$*" in *"exh 4"*) exit 3;; esac\nexec "%s" "$@"\n' "$REAL" > "$W/s2/python3"
printf '#!/bin/sh\ncase "$*" in *"run 5"*) exit 3;; esac\nexec "%s" "$@"\n' "$REAL" > "$W/s3/python3"
chmod +x "$W/s1/python3" "$W/s2/python3" "$W/s3/python3"
cd "$W" || exit 2
bad=0; D=experiments/red-b/data/b6b/out; R=experiments/red-b/run_b6fix.sh
last() { tail -n 1 "$1" > "$1.last"; sed 's/ done [0-9TZ:-]*/ done/' "$1.last"; }
PATH="$W/s1:$PATH" bash $R o1 exh > u1.log 2>&1; e=$?; f=0; [ -e o1/prefix_exh.out ] && f=1
echo "U1 exh, python3 always fails: exit $e file-left $f | $(last u1.log)"; [ "$e" = 1 ] && [ "$f" = 0 ] || bad=1
PATH="$W/s2:$PATH" bash $R o2 exh > u2.log 2>&1; e=$?; n=0; [ -e o2/prefix_exh.out ] && n=$(wc -l < o2/prefix_exh.out); head -n 1 $D/prefix_exh.out > pin1; q=1; [ -e o2/prefix_exh.out ] && { cmp -s o2/prefix_exh.out pin1; q=$?; }
echo "U2 exh, python3 fails for k = 4 only: exit $e lines $n cmp-with-pinned-first-line $q | $(last u2.log)"; [ "$e" = 1 ] && [ "$n" = 1 ] && [ "$q" = 0 ] || bad=1
PATH="$W/s3:$PATH" bash $R o3 ctrl > u3.log 2>&1; e=$?; f=0; [ -e o3/prefix_ctrl.out ] && f=1
echo "U3 ctrl, its second command fails: exit $e file-left $f | $(last u3.log)"; [ "$e" = 1 ] && [ "$f" = 0 ] || bad=1
bash $R o4 nosuchstage > u4.log 2>&1; e=$?
echo "U4 unknown stage: exit $e"; [ "$e" = 2 ] || bad=1
bash $R o5 every > u5.log 2>&1; e=$?; eq=0
for f in prefix_run prefix_all prefix_off prefix_drive prefix_loc prefix_stable prefix_exh prefix_u0 brtie width prefix_ctrl; do
  if cmp -s o5/$f.out $D/$f.out; then eq=$((eq + 1)); else echo "U5 $f.out DIFFERS"; fi
done
echo "U5 every: exit $e byte-equal $eq of 11 | $(last u5.log)"; [ "$e" = 0 ] && [ "$eq" = 11 ] || bad=1
echo "RESULT all-as-expected $((1 - bad))"
exit $bad
