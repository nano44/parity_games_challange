#!/usr/bin/env bash
# L-RED-B B7: ONE long RF run on K^s_N with checkpoints (resumable after a container restart: run the same command again).
# The final line carries iterations, the law, |V|, |V|^2 and the sha1 of the instance. State = sigma and the iteration count
# (RF is memoryless), written every 20,000 iterations to OUTDIR/ck_N.txt.
# Usage: runks_big.sh RF7BIN N OUTDIR        (RF7BIN: g++ -O2 -std=c++17 -o rf7 rf7.cpp)
set -u
BIN="$1"; n="$2"; OUT="$3"; HERE="$(cd "$(dirname "$0")" && pwd)"; mkdir -p "$OUT"
grep -q "^B7 Ks-big n $n " "$OUT/ks_big.out" 2>/dev/null && { echo "n $n already done"; exit 0; }
[ -s "$OUT/Ks_$n.pg" ] || python3 -B "$HERE/rfc2.py" "$n" --skip --pgonly --pg "$OUT/Ks_$n.pg" "$OUT/Ks_$n.start" || exit 1
t0=$(date +%s)
line=$("$BIN" rf "$OUT/Ks_$n.pg" "$OUT/Ks_$n.start" --ckpt "$OUT/ck_$n.txt" 20000 2>> "$OUT/ck_$n.log") || exit 1
t1=$(date +%s)
python3 - "$n" "$line" "$(sha1sum "$OUT/Ks_$n.pg" | cut -c1-40)" "$((t1 - t0))" "$(grep -c resumed "$OUT/ck_$n.log")" >> "$OUT/ks_big.out" <<'PY'
import sys
n = int(sys.argv[1]); a = sys.argv[2].split(); its = int(a[a.index("iterations") + 1]); V = int(a[a.index("n") + 1])
law = 7 * 2 ** (n - 1) - 2 * n - 3
print(f"B7 Ks-big n {n} |V| {V} |V|^2 {V * V} iterations {its} law {law} diff {its - law} beyond-|V|^2 {int(its > V * V)} | {sys.argv[2]} | pg sha1 {sys.argv[3]} secs-last-process {sys.argv[4]} resumes {sys.argv[5]}")
PY
