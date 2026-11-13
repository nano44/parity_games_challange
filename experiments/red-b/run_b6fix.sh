#!/bin/bash
# L-RED-B packet P-N5-EXP, fixes entries 4-5: runner for b6prefix.py (resumable: a stage skips the lines its output file holds).
# Usage (from anywhere): bash experiments/red-b/run_b6fix.sh OUTDIR [STAGE]     STAGE = run | all | off | drive | loc | stable | exh | u0 |
#   tie | width | ctrl | every (default). No archive of another lane is needed. Seconds per stage, about three minutes in all.
# Fixes entry 7 (REFEREE-2 42's F-4): a failing stage command is counted and the runner then exits 1 (its last line ends
#   «failures N»). Each command is tested where it runs, and its output reaches the output file only if it exits 0 (it is written
#   to a temporary file first), so a failure leaves no empty or partial output file. The two lines of run_b6b.sh (the ERR trap and
#   the exit code) are here too, as a backstop for every other command; by themselves they would miss a failing control that is
#   not the last command of the ctrl stage and would leave the empty file (entry 7, 7.4). An unknown STAGE exits 2.
#   The stage commands, their arguments and their order are those of the runner at 24f4d436: the outputs are byte-equal.
#   Test hook: B6FIX_PY names the interpreter (default python3); check.sh runs one stage with B6FIX_PY=false and expects exit 1.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
O="$1"; STAGE="${2:-every}"
mkdir -p "$O"
export PYTHONDONTWRITEBYTECODE=1
PY="${B6FIX_PY:-python3}"
fail=0; set -E; trap 'fail=$((fail + 1))' ERR   # backstop: any other failing command of a stage is counted too
P() { (cd "$HERE" && "$PY" b6prefix.py "$@"); }
has() { [ -f "$1" ] && grep -q "^$2" "$1"; }
# line FILE PREFIX ARGS...: unless FILE holds a line that starts with PREFIX, append the output of `b6prefix.py ARGS` to FILE
line() {
  local f="$1" pre="$2"; shift 2
  has "$f" "$pre" && return 0
  local tmp="$f.tmp.$$"
  if P "$@" > "$tmp"; then cat "$tmp" >> "$f"; else fail=$((fail + 1)); echo "run_b6fix: FAILED: b6prefix.py $*" >&2; fi
  rm -f "$tmp"
}
run()    { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do line "$O/prefix_run.out" "G_$k mode run " run $k; done; }
all()    { for k in 3 4 5 6 7 8 9 10 11 12; do line "$O/prefix_all.out" "G_$k mode all " all $k; done; }
off()    { for k in 4 5 6 7 8; do for s in 1 2; do line "$O/prefix_off.out" "G_$k mode off ctrl 0 seed $s " off $k $s 400; done; done; }
drive()  { for k in 4 5 6 7 8 9 10; do for s in 1 2; do line "$O/prefix_drive.out" "G_$k mode drive ctrl 0 seed $s " drive $k $s 2000; done; done; }
loc()    { for k in 3 4 5 6 7 8; do line "$O/prefix_loc.out" "G_$k mode loc " loc $k 1 30 3000; done; }
stable() { for k in 3 4 5 6 7 8; do line "$O/prefix_stable.out" "G_$k mode stable " stable $k 1 6000; done; }
exh()    { for k in 3 4; do line "$O/prefix_exh.out" "G_$k mode exh " exh $k; done; }
u0()     { for k in 3 4 5 6; do line "$O/prefix_u0.out" "G_$k mode u0 " u0 $k 1 8000; done; }
tie()    { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do line "$O/brtie.out" "G_$k mode tie " tie $k; done; }
width()  { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do line "$O/width.out" "G_$k mode width " width $k; done; }
# the controls are regenerated as a whole: prefix_ctrl.out is replaced only if every one of the ten control commands exits 0
ctrl() {
  local tmp="$O/prefix_ctrl.out.tmp.$$" bad=0
  : > "$tmp"
  c() { local v="$1"; shift; B6X_CTRL="$v" P "$@" >> "$tmp" || { bad=$((bad + 1)); echo "run_b6fix: FAILED: B6X_CTRL=$v b6prefix.py $*" >&2; }; }
  c 5 all 3 4 5 6 7 8; c 2 run 5; c 1 off 6 1 400; c 2 off 6 1 400
  c 1 drive 6 1 2000; c 2 drive 6 1 2000; c 3 loc 5 1 30 3000; c 4 loc 5 1 30 3000
  c 2 exh 4; c 3 exh 4
  if [ "$bad" -eq 0 ]; then mv "$tmp" "$O/prefix_ctrl.out"; else rm -f "$tmp"; fail=$((fail + bad)); fi
}
case "$STAGE" in
  run) run ;; all) all ;; off) off ;; drive) drive ;; loc) loc ;; stable) stable ;; exh) exh ;; u0) u0 ;; tie) tie ;; width) width ;;
  ctrl) ctrl ;;
  every) run; all; off; drive; loc; stable; exh; u0; tie; width; ctrl ;;
  *) echo "run_b6fix: unknown STAGE $STAGE" >&2; exit 2 ;;
esac
echo "run_b6fix $STAGE done $(date -u +%Y-%m-%dT%H:%M:%SZ) failures $fail"
[ "$fail" -eq 0 ] || exit 1
exit 0
