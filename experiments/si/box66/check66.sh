#!/usr/bin/env bash
# L-SI box 66 self-check (~5 s): bff.c (box 65 bfg.c + FRONTIER hook) reproduces the m = 1 pair set; the committed m = 2 enumeration
# (4 parts) gives exactly {(pre, post): post <= 4, pre + post <= 5} and T_1(2) = 5.
set -euo pipefail
cd "$(dirname "$0")"
want1="0 0;0 1;0 2;1 0;1 1;1 2;2 0;"
if command -v gcc >/dev/null; then
  gcc -O2 -DKMAX=1 -o bff_check bff.c
  got1=$(./bff_check 1 0 1 2>/dev/null | awk '/^PAIR/{print $3" "$5}' | sort -u -n -k1 -k2 | tr '\n' ';'); rm -f bff_check
  [ "$got1" = "$want1" ] || { echo "box 66 m 1 pairs: $got1"; exit 1; }
fi
got2=$(awk '/^PAIR/{print $3" "$5}' out/bff_m2_p0.txt out/bff_m2_p1.txt out/bff_m2_p2.txt out/bff_m2_p3.txt | sort -u -n -k1 -k2 | tr '\n' ';')
want2=$(for a in 0 1 2 3 4; do for c in 0 1 2 3 4; do if [ $((a + c)) -le 5 ]; then printf '%d %d;' $a $c; fi; done; done)
[ "$got2" = "$want2" ] || { echo "box 66 m 2 pairs: $got2"; exit 1; }
[ "$(grep -h '^T_1(2)' out/bff_m2_p*.txt | sort -u)" = "T_1(2) 5" ]
echo "box 66 frontier: PASS"
# m = 3 frozen champions (lower bounds), replayed with L-NEW's box 150 Gen
sha1sum -c --quiet pin/pins.sha1
python3 -I - <<'PY'
import sys, json, itertools
sys.path.insert(0, '../box64'); from flipdp import Ext
ns = {"__file__": "../box64/ref/box150/check.py"}; exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns)
Gen, restrict = ns["Gen"], ns["restrict"]
def pairs(G):
    E = Ext(G); out = set()
    def run(u, b):
        sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"]); return [tuple(st[v] for v in E.UP) for st in S]
    for u in itertools.product(*[range(2) for _ in E.UP]):
        for b in (0, 1):
            seq = run(u, b)
            for t, st in enumerate(seq): out.add((t, len(run(st, 1 - b)) - 1))
    return out
want = {"../box64/wit/kf1_d4_t10.json": [(5, 5)], "pin/f_m3_p4_s1.json": [(0, 8), (7, 1), (8, 0)], "pin/f_m3_p2_s1.json": [(1, 7)],
        "../box65/pin/j1_m3_s1.json": [(2, 7)], "pin/f_m3_p6_s1.json": [(6, 3)]}
for f, pts in want.items():
    P = pairs(json.load(open(f)))
    assert all(p in P for p in pts), f
assert max(a + c for a, c in pairs(json.load(open("pin/f_m3_p4_s1.json")))) == 9
PY
echo "box 66 m 3 pins (Gen replay): PASS"
