#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for docs/si/N5-GRUN-box25.md §3. To GAME (with START) add, for every Odd vertex o without predecessors, an
Even ANCHOR e with edges {e, o}, a self-loop of a fresh even priority above all others (so e never leaves its loop: Xi(e) is Even's best
value) and sigma0(e) = e. Then o is in RESULTS R81's K. Checks that sigma, sigma-bar, tau and the fallback flags on the old vertices are
unchanged at every state (SAME) and prints G, G^K (sigma-bar changes on K) and SEG (grun/relseg.py) on the run [A, B] (args).
Usage: anchor.py GAME START A B OUTPREFIX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (HERE, os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)
from common import rows, load, readstart
from pieceh import kset
from relseg import segcount
import pg

def main():
    gp, sp, A, B, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    g = load(gp); s0, t0 = readstart(sp); n = g.n; E, R0 = rows(g, (s0, t0))
    preds = {y for v in range(n) for y in g.succ[v] if y != v}
    rd = [o for o in range(n) if g.owner[o] == 1 and o not in preds]
    prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]; s1 = dict(s0)
    top = max(prio) + (2 if max(prio) % 2 == 0 else 1)
    for k, o in enumerate(rd):
        e = n + k; prio.append(top + 2 * k); owner.append(0); succ.append([e, o]); s1[e] = e
    h = pg.Game(prio, owner, succ); E1, R1 = rows(h, (s1, t0))
    same = len(R1) == len(R0) and all(R1[k]["s"][:n] == R0[k]["s"][:n] and R1[k]["sb"][:n] == R0[k]["sb"][:n] and R1[k]["fb"] == R0[k]["fb"]
                                      and R1[k]["t"][:n] == R0[k]["t"][:n] for k in range(len(R0)))
    KO = [u for u in kset(h) if h.owner[u] == 1]
    G = sum(R1[t]["sb"] != R1[t + 1]["sb"] for t in range(A, B)); GK = sum(any(R1[t]["sb"][u] != R1[t + 1]["sb"][u] for u in KO) for t in range(A, B))
    print("anchors", len(rd), "n", h.n, "SAME", same, "readers in K", sum(o in kset(h) for o in rd), "run", B - A, "G", G, "G^K", GK,
          "SEG", segcount(h, R1), "fallbacks in [A,B]", sum(R1[k]["fb"] for k in range(A, B)))
    with open(out + ".pg", "w") as f:
        f.write("parity %d;\n" % (h.n - 1))
        for v in range(h.n): f.write("%d %d %d %s;\n" % (v, h.prio[v], h.owner[v], ",".join(map(str, h.succ[v]))))
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join("%d:%d" % (v, s1[v]) for v in sorted(s1)) + "\n")
        f.write("TAU0 " + " ".join("%d:%d" % (v, t0[v]) for v in sorted(t0)) + "\n")

if __name__ == "__main__":
    main()
