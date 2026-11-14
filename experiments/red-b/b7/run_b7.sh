#!/usr/bin/env bash
# L-RED-B B7: regenerate the DATA of docs/red-b/B7-RF.md into OUT (default: this directory's out/). Each stage writes through
# a temporary file and is skipped when its output exists; a failing command stops the script with exit 1 and leaves no file.
# Usage: run_b7.sh [OUT]      (Oink must be built for the stage xoink: scripts/setup_oink.sh)
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; OUT="${1:-$HERE/out}"; mkdir -p "$OUT"; cd "$HERE"
export PYTHONDONTWRITEBYTECODE=1
stage() {  # stage NAME command...   (stdout of the command -> OUT/NAME.out)
  local name="$1"; shift
  [ -s "$OUT/$name.out" ] && return 0
  local tmp; tmp="$(mktemp)"
  if "$@" > "$tmp" 2>&1; then mv "$tmp" "$OUT/$name.out"; else echo "run_b7: stage $name FAILED:"; tail -5 "$tmp"; rm -f "$tmp"; exit 1; fi
}
ctrl() {   # ctrl NAME command...   the command must EXIT NONZERO (a firing control)
  local name="$1"; shift
  [ -s "$OUT/$name.out" ] && return 0
  local tmp; tmp="$(mktemp)"
  if "$@" > "$tmp" 2>&1; then echo "run_b7: control $name did NOT fire"; rm -f "$tmp"; exit 1; else mv "$tmp" "$OUT/$name.out"; fi
}
stage st7_bf      python3 st7.py bf 1 3000 7
ctrl  st7_bf_ctrl env B7_CTRL=1 python3 st7.py bf 1 300 7
stage st7_sol     python3 st7.py sol 2 3000 12
ctrl  st7_sol_ctrl env B7_CTRL=2 python3 st7.py sol 2 100 12
stage st7_howard_fig4   python3 st7.py howard 6 fig4
stage st7_howard_table4 python3 st7.py howard 5 table4
stage xoink_lmcs  python3 xoink.py lmcs 5
stage xoink_rand  python3 xoink.py rand 5 400 14
ctrl  xoink_ctrl  env B7_CTRL=2 python3 xoink.py rand 5 20 14
stage rf_lmcs     python3 -c "
import gens7, si7
for ver in ('fig4', 'table4'):
    for n in range(1, 8):
        g, s0 = gens7.lmcs(n, ver); r = [si7.Engine(g).run(s0, si7.root_first(t))[0] for t in ('high', 'low')]
        print(f'B7 rf lmcs {ver} n {n} |V| {g.n}: RF tie-high {r[0]} tie-low {r[1]} 3n+3 {3 * n + 3}')
"
stage rfc_linear  bash -c 'for n in 2 3 4 5 6 7 8; do python3 rfc.py $n 2 chain; done'
stage k_noskip    bash -c 'for n in 1 2 3 4 5 6 7; do python3 rfc2.py $n; done'
stage ks_py_1_9   python3 runks.py 1 2 3 4 5 6 7 8 9
stage ks_py_low_1_8 python3 runks.py 1 2 3 4 5 6 7 8 --tie low
stage ks_trace_2  python3 rfc2.py 2 --skip --trace
stage ks_trace_3  python3 rfc2.py 3 --skip --trace
stage ks_xoink    bash -c 'for n in 3 5 7; do python3 xoink.py pg inst/Ks_$n.pg inst/Ks_$n.start || exit 1; done'
if command -v g++ >/dev/null; then
  mkdir -p "$HERE/../work/b7"; [ -x "$HERE/../work/b7/rf7" ] || g++ -O2 -std=c++17 -o "$HERE/../work/b7/rf7" rf7.cpp || exit 1
  stage cmp7      python3 cmp7.py "$HERE/../work/b7/rf7" 7 11 400 14
  ctrl  cmp7_ctrl env B7_CTRL=4 python3 cmp7.py "$HERE/../work/b7/rf7" 2 11 400 14
fi
echo "run_b7: done ($(ls "$OUT" | wc -l) files in $OUT)"
