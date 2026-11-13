#!/bin/bash
# L-RED-B packet P-N5-EXP, fixes entries 4-5: runner for b6prefix.py (resumable: a stage skips the lines its output file holds).
# Usage (from anywhere): bash experiments/red-b/run_b6fix.sh OUTDIR [STAGE]     STAGE = run | all | off | drive | loc | stable | exh | u0 |
#   tie | width | ctrl | every (default). No archive of another lane is needed. Seconds per stage, about three minutes in all.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
O="$1"; STAGE="${2:-every}"
mkdir -p "$O"
export PYTHONDONTWRITEBYTECODE=1
P() { (cd "$HERE" && python3 b6prefix.py "$@"); }
has() { [ -f "$1" ] && grep -q "^$2" "$1"; }
run()    { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do has "$O/prefix_run.out" "G_$k mode run " || P run $k >> "$O/prefix_run.out"; done; }
all()    { for k in 3 4 5 6 7 8 9 10 11 12; do has "$O/prefix_all.out" "G_$k mode all " || P all $k >> "$O/prefix_all.out"; done; }
off()    { for k in 4 5 6 7 8; do for s in 1 2; do has "$O/prefix_off.out" "G_$k mode off ctrl 0 seed $s " || P off $k $s 400 >> "$O/prefix_off.out"; done; done; }
drive()  { for k in 4 5 6 7 8 9 10; do for s in 1 2; do has "$O/prefix_drive.out" "G_$k mode drive ctrl 0 seed $s " || P drive $k $s 2000 >> "$O/prefix_drive.out"; done; done; }
loc()    { for k in 3 4 5 6 7 8; do has "$O/prefix_loc.out" "G_$k mode loc " || P loc $k 1 30 3000 >> "$O/prefix_loc.out"; done; }
stable() { for k in 3 4 5 6 7 8; do has "$O/prefix_stable.out" "G_$k mode stable " || P stable $k 1 6000 >> "$O/prefix_stable.out"; done; }
exh()    { for k in 3 4; do has "$O/prefix_exh.out" "G_$k mode exh " || P exh $k >> "$O/prefix_exh.out"; done; }
u0()     { for k in 3 4 5 6; do has "$O/prefix_u0.out" "G_$k mode u0 " || P u0 $k 1 8000 >> "$O/prefix_u0.out"; done; }
tie()    { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do has "$O/brtie.out" "G_$k mode tie " || P tie $k >> "$O/brtie.out"; done; }
width()  { for k in 3 4 5 6 7 8 9 10 11 12 13 14; do has "$O/width.out" "G_$k mode width " || P width $k >> "$O/width.out"; done; }
ctrl() {
  : > "$O/prefix_ctrl.out"
  (B6X_CTRL=5 P all 3 4 5 6 7 8; B6X_CTRL=2 P run 5; B6X_CTRL=1 P off 6 1 400; B6X_CTRL=2 P off 6 1 400
   B6X_CTRL=1 P drive 6 1 2000; B6X_CTRL=2 P drive 6 1 2000; B6X_CTRL=3 P loc 5 1 30 3000; B6X_CTRL=4 P loc 5 1 30 3000
   B6X_CTRL=2 P exh 4; B6X_CTRL=3 P exh 4) >> "$O/prefix_ctrl.out"
}
case "$STAGE" in
  run) run ;; all) all ;; off) off ;; drive) drive ;; loc) loc ;; stable) stable ;; exh) exh ;; u0) u0 ;; tie) tie ;; width) width ;;
  ctrl) ctrl ;;
  every) run; all; off; drive; loc; stable; exh; u0; tie; width; ctrl ;;
esac
echo "run_b6fix $STAGE done $(date -u +%Y-%m-%dT%H:%M:%SZ)"
