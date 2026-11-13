#!/bin/bash
# L-RED-B packet P-N5-EXP, fixes entry 7 (REFEREE-2 42's F-4): tests of the runner run_b6fix.sh.
# Usage (from anywhere inside the repository): bash experiments/red-b/b6fixtest.sh WORKDIR [quick]
#   WORKDIR = a new directory outside the tracked paths (e.g. experiments/red-b/work/e7/runfix): everything is written there.
#   One line per test, without time stamps (the output is pinned). Exit 1 if a test of the runner fails or a control does not fire.
# The runner as it is now:
#   N1 stage width, every command failing (B6FIX_PY=false)             expected: exit 1, failures 12, no file left
#   N2 stage exh, a python3 on PATH that exits 1 (REFEREE-2's T4)       expected: exit 1, failures 2, no file left
#   N3 stage ctrl, every command failing                                expected: exit 1, failures 10, no file left
#   N4 stage ctrl, ONE middle command failing (B6X_CTRL=2, run 5)       expected: exit 1, failures 1, no file left
#   N5 an unknown stage                                                 expected: exit 2, no file left
#   N6 stage width failing, then twice without the failure              expected: exit 1; exit 0 and width.out equal to its
#                                                                        pinned file; exit 0 again (skip-if-done), still equal
#   N7 stage width, the command of k = 5 alone failing                  expected: exit 1, failures 1, width.out with the other
#                                                                        11 lines; a second run without the failure completes it
# Controls (the defect must show):
#   C1 the runner of 24f4d436 (git show), stage exh, failing python3    expected: exit 0 and an EMPTY prefix_exh.out (F-4)
#   C2 that runner plus ONLY the two lines of run_b6b.sh, stage exh     expected: exit 1, the empty prefix_exh.out still left
#   C3 the two-line variant, stage ctrl, ONE middle command failing     expected: exit 0, «failures 0», a prefix_ctrl.out of 14
#                                                                        lines that differs from the pinned one (15 lines)
# E  (not with `quick`; about two minutes) `run_b6fix.sh WORKDIR/every every`, then each of its 11 output files against
#   data/b6b/out/ (cmp) and against its pin in data/b6b/SHA1SUMS_b6b_fixes2 (sha1).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
W="$1"; QUICK="${2:-}"
mkdir -p "$W"; W="$(cd "$W" && pwd)"
[ -z "$(ls -A "$W")" ] || { echo "b6fixtest: WORKDIR is not empty" >&2; exit 2; }
export PYTHONDONTWRITEBYTECODE=1
REAL="$(command -v python3)"
PIN="$HERE/data/b6b/out"
bad=0
nfiles() { ls -A "$1" 2>/dev/null | wc -l | tr -d ' '; }
nfail() { sed -n 's/^run_b6fix .* failures \([0-9][0-9]*\)$/\1/p' "$1" | tail -n 1; }
ok() { if [ "$1" = "$2" ]; then echo 1; else echo 0; bad=$((bad + 1)); fi; }
# shims: a python3 that always fails; one that fails for the control «B6X_CTRL=2 ... run 5» only; one that fails for the argument 5
mkdir -p "$W/shimall" "$W/shimmid" "$W/shim5"
printf '#!/bin/bash\nexit 1\n' > "$W/shimall/python3"
printf '#!/bin/bash\nif [ "${B6X_CTRL:-0}" = 2 ] && [ "${2:-}" = run ]; then exit 3; fi\nexec "%s" "$@"\n' "$REAL" > "$W/shimmid/python3"
printf '#!/bin/bash\nfor a in "$@"; do [ "$a" = 5 ] && exit 3; done\nexec "%s" "$@"\n' "$REAL" > "$W/shim5/python3"
chmod +x "$W/shimall/python3" "$W/shimmid/python3" "$W/shim5/python3"
RUN="$HERE/run_b6fix.sh"

B6FIX_PY=false bash "$RUN" "$W/n1" width > "$W/n1.log" 2>&1; rc=$?
r="$rc $(nfail "$W/n1.log") $(nfiles "$W/n1")"; echo "N1 stage width all-fail: exit failures files = $r ok $(ok "$r" "1 12 0")"
PATH="$W/shimall:$PATH" bash "$RUN" "$W/n2" exh > "$W/n2.log" 2>&1; rc=$?
r="$rc $(nfail "$W/n2.log") $(nfiles "$W/n2")"; echo "N2 stage exh failing-python3-on-PATH: exit failures files = $r ok $(ok "$r" "1 2 0")"
B6FIX_PY=false bash "$RUN" "$W/n3" ctrl > "$W/n3.log" 2>&1; rc=$?
r="$rc $(nfail "$W/n3.log") $(nfiles "$W/n3")"; echo "N3 stage ctrl all-fail: exit failures files = $r ok $(ok "$r" "1 10 0")"
B6FIX_PY="$W/shimmid/python3" bash "$RUN" "$W/n4" ctrl > "$W/n4.log" 2>&1; rc=$?
r="$rc $(nfail "$W/n4.log") $(nfiles "$W/n4")"; echo "N4 stage ctrl one-middle-control-fails: exit failures files = $r ok $(ok "$r" "1 1 0")"
bash "$RUN" "$W/n5" nosuch > "$W/n5.log" 2>&1; rc=$?
r="$rc $(nfiles "$W/n5")"; echo "N5 unknown stage: exit files = $r ok $(ok "$r" "2 0")"
B6FIX_PY=false bash "$RUN" "$W/n6" width > "$W/n6a.log" 2>&1; rc1=$?
bash "$RUN" "$W/n6" width > "$W/n6b.log" 2>&1; rc2=$?; cmp -s "$W/n6/width.out" "$PIN/width.out"; e2=$?
bash "$RUN" "$W/n6" width > "$W/n6c.log" 2>&1; rc3=$?; cmp -s "$W/n6/width.out" "$PIN/width.out"; e3=$?
r="$rc1 $rc2 $e2 $rc3 $e3"; echo "N6 stage width fail, run, run again: exit; exit cmp; exit cmp = $r ok $(ok "$r" "1 0 0 0 0")"
B6FIX_PY="$W/shim5/python3" bash "$RUN" "$W/n7" width > "$W/n7a.log" 2>&1; rc1=$?
l1=$(wc -l < "$W/n7/width.out" | tr -d ' '); f1=$(nfail "$W/n7a.log"); g5=$(grep -c '^G_5 ' "$W/n7/width.out")
bash "$RUN" "$W/n7" width > "$W/n7b.log" 2>&1; rc2=$?; l2=$(wc -l < "$W/n7/width.out" | tr -d ' ')
sort "$W/n7/width.out" | cmp -s - <(sort "$PIN/width.out"); e2=$?
r="$rc1 $f1 $l1 $g5 $rc2 $l2 $e2"; echo "N7 stage width k=5-fails, then run: exit failures lines G_5-lines; exit lines same-lines-as-pin = $r ok $(ok "$r" "1 1 11 0 0 12 0")"

# controls: the runner as it was at 24f4d436, and that runner with only the two lines of run_b6b.sh
mkdir -p "$W/old"
if git -C "$HERE" show 24f4d436a0fea1f62ae736f20f78ff9e84333a90:experiments/red-b/run_b6fix.sh > "$W/old/run_b6fix.sh" 2>/dev/null; then
  cp "$HERE/b6prefix.py" "$HERE/gk.py" "$HERE/onep.py" "$W/old/"
  sed -e "s/^export PYTHONDONTWRITEBYTECODE=1\$/export PYTHONDONTWRITEBYTECODE=1\nfail=0; set -E; trap 'fail=1' ERR/" \
      -e 's/^echo "run_b6fix \$STAGE done \(.*\)"$/echo "run_b6fix $STAGE done \1 failures $fail"\nexit $fail/' \
      "$W/old/run_b6fix.sh" > "$W/old/run_b6fix_two.sh"
  two=$(grep -c "trap 'fail=1' ERR\|^exit \$fail" "$W/old/run_b6fix_two.sh")
  PATH="$W/shimall:$PATH" bash "$W/old/run_b6fix.sh" "$W/c1" exh > "$W/c1.log" 2>&1; rc=$?
  r="$rc $(nfiles "$W/c1") $(wc -c < "$W/c1/prefix_exh.out" | tr -d ' ')"; echo "C1 runner of 24f4d436, stage exh failing-python3-on-PATH: exit files bytes = $r fires $(ok "$r" "0 1 0")"
  PATH="$W/shimall:$PATH" bash "$W/old/run_b6fix_two.sh" "$W/c2" exh > "$W/c2.log" 2>&1; rc=$?
  r="$two $rc $(nfiles "$W/c2") $(wc -c < "$W/c2/prefix_exh.out" | tr -d ' ')"; echo "C2 that runner + the two lines only, stage exh failing-python3-on-PATH: lines-added exit files bytes = $r fires $(ok "$r" "2 1 1 0")"
  PATH="$W/shimmid:$PATH" bash "$W/old/run_b6fix_two.sh" "$W/c3" ctrl > "$W/c3.log" 2>&1; rc=$?
  cmp -s "$W/c3/prefix_ctrl.out" "$PIN/prefix_ctrl.out"; e=$?
  r="$rc $(nfail "$W/c3.log") $(wc -l < "$W/c3/prefix_ctrl.out" | tr -d ' ') $(wc -l < "$PIN/prefix_ctrl.out" | tr -d ' ') $e"; echo "C3 the two-line variant, stage ctrl one-middle-control-fails: exit failures lines pinned-lines differs = $r fires $(ok "$r" "0 0 14 15 1")"
else
  echo "C1-C3 NOT RUN: commit 24f4d436 is not in this clone"; bad=$((bad + 1))
fi

if [ "$QUICK" != "quick" ]; then
  bash "$RUN" "$W/every" every > "$W/every.log" 2>&1; rc=$?
  r="$rc $(nfail "$W/every.log") $(nfiles "$W/every")"; echo "E run_b6fix.sh every: exit failures files = $r ok $(ok "$r" "0 0 11")"
  for f in prefix_run prefix_all prefix_off prefix_drive prefix_loc prefix_stable prefix_exh prefix_u0 brtie width prefix_ctrl; do
    cmp -s "$W/every/$f.out" "$PIN/$f.out"; e=$?
    s=$(sha1sum < "$W/every/$f.out" | cut -d' ' -f1); p=$(grep " out/$f.out\$" "$HERE/data/b6b/SHA1SUMS_b6b_fixes2" | cut -d' ' -f1)
    echo "E $f.out sha1 $s cmp-with-data $e sha1-equals-pin $(ok "$s" "$p")"; [ "$e" = 0 ] || bad=$((bad + 1))
  done
fi
echo "b6fixtest failed $bad"
[ "$bad" -eq 0 ] || exit 1
exit 0
