#!/usr/bin/env bash
# L-SI box 67 self-check (~5 s): bfd.c (box 66 bff.c + TAU hook) reproduces D(1, tau) = 0, 2, 3; the committed m = 2 enumeration
# (4 parts) gives D(2, tau) = 0, 2, 4, 5, 5 (tau = 0..4) and no class with T_1 = 2 tau at tau = 3, 4; m = 3 points (kf1_d4_t10: T_0 5,
# T_1 10) recomputed by flipdp.py.
set -euo pipefail
cd "$(dirname "$0")"
if command -v gcc >/dev/null; then
  gcc -O2 -DKMAX=1 -o bfd_check bfd.c
  d1=$(./bfd_check 1 0 1 2>/dev/null | awk '/^TAU/{printf "%s:%s;", $3, $7}'); rm -f bfd_check
  [ "$d1" = "0:0;1:2;2:3;" ] || { echo "box 67 D(1): $d1"; exit 1; }
fi
d2=$(awk '/^TAU/{t=$3; if (!(t in mx) || $7 > mx[t]) mx[t] = $7; d[t] += $9} END {for (t = 0; t <= 4; t++) printf "%s:%s:%s;", t, mx[t], d[t]}' out/bfd_m2_p0.txt out/bfd_m2_p1.txt out/bfd_m2_p2.txt out/bfd_m2_p3.txt)
case "$d2" in "0:0:24;1:2:"*";2:4:"*";3:5:0;4:5:0;") ;; *) echo "box 67 D(2): $d2"; exit 1;; esac
python3 -I - <<'PY'
import sys, json; sys.path.insert(0, '../box64'); from flipdp import analyse
assert analyse(json.load(open('../box64/wit/kf1_d4_t10.json')), K=1)['T'] == [5, 10]
PY
echo "box 67 tau table: PASS"
sha1sum -c --quiet pin/pins.sha1
python3 -I - <<'PY'
import sys, json, itertools
sys.path.insert(0, '../box64'); from flipdp import Ext
ns = {"__file__": "../box64/ref/box150/check.py"}; exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns)
Gen, restrict = ns["Gen"], ns["restrict"]
def t01(f):
    G = json.load(open(f)); E = Ext(G); T0 = T1 = 0
    def run(u, b):
        sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"]); return [tuple(st[v] for v in E.UP) for st in S]
    for u in itertools.product(*[range(2) for _ in E.UP]):
        for b in (0, 1):
            seq = run(u, b); T0 = max(T0, len(seq) - 1)
            for t, st in enumerate(seq): T1 = max(T1, t + len(run(st, 1 - b)) - 1)
    return T0, T1
assert t01('pin/tau_m3_t4_s2.json') == (4, 8)
assert t01('../box64/wit/kf1_d4_t10.json') == (5, 10)
PY
echo "box 67 m 3 pins (Gen replay): PASS"
