#!/usr/bin/env python3
"""L-RED successor 24: graft a chain c_1..c_w (Even, priority P, c_i -> {gate, c_(i-1)}, c_1 -> {gate, SRC}) onto a game; start c_i -> gate
(mode g) or -> c_(i-1) (mode c). Prints f, CR (multi-switch carries re-switching), R1, for each w. Usage: graft.py GAME.pg START GATE SRC P MODE w..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
import trace as T, fbphase as F
def graft(g, st, gate, src, P, mode, w):
    n = g.n; prio = list(g.prio) + [P] * w; owner = list(g.owner) + [0] * w
    succ = [list(x) for x in g.succ] + [sorted({gate, src if i == 0 else n + i - 1}) for i in range(w)]
    s0 = dict(st[0]); 
    for i in range(w): s0[n + i] = gate if mode == "g" else (src if i == 0 else n + i - 1)
    return T.pg.Game(prio, owner, succ), (s0, dict(st[1]))
if __name__ == "__main__":
    a = sys.argv; g = T.pg.parse(open(a[1]).read()); st = T.readstart(a[2]) if a[2] != "S3" else ({}, {})
    gate, src, P, mode = int(a[3]), int(a[4]), int(a[5]), a[6]
    out = []
    for w in map(int, a[7:]):
        G, S = graft(g, st, gate, src, P, mode, w)
        try:
            F.MODE_RF = 4; f, cr = F.reuse(G, S, cap=5000); F.MODE_RF = 2; _, r1 = F.reuse(G, S, cap=5000)
            out.append("w%d:f%d/cr%d/r1%d" % (w, f, cr, r1))
        except Exception as e: out.append("w%d:ERR" % w)
    print("src", src, "P", P, mode, " ".join(out))
