#!/usr/bin/env python3
"""L-SI box 17: DATA for docs/si/N5-RUND-box17.md §9 (what moves below the top-rank disagreement on the long runs). For every maximal
fallback-free in-phase run with >= n + 1 states (or MINLEN env), per transition k -> k+1 it prints: D_k, the gates' cycle node c and the
top vertex t of P(Xi u) ^ P(W u) and which frame holds it, the switched Even vertices, the vertices whose Xi / W value changes and the
level of the change (lev: top rank of the path-set change, -1 length only), and whether a gate value changes.
Usage: below.py GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval

def lev(x, y):
    if x[0] != y[0]: return "cyc"
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else (-1 if x[2] != y[2] else None)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = sorted(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        rows.append(dict(s=list(s), key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, W=W, D=D, sb=sb, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    rank = E.rank; minlen = int(os.environ.get("MINLEN", g.n + 1)); i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j - i + 1 >= minlen:
            print(f"RUN states {i}..{j} ({j - i + 1} states, n = {g.n})")
            hx, hw = Counter(), Counter()
            for k in range(i, j):
                a, b = rows[k], rows[k + 1]
                gates = []
                for u in a["D"]:
                    d = a["vs"][u][1] ^ a["W"][u][1]; tt = d.bit_length() - 1
                    who = ("Xi" if a["vs"][u][1] >> tt & 1 else "W") if d else "neither (equal path sets)"
                    gates.append(f"u={u} c={a['vs'][u][0]}(r{rank[a['vs'][u][0]]}) top r{tt} in {who}")
                sw = [v for v in range(g.n) if g.owner[v] == 0 and a["s"][v] != b["s"][v]]
                cx = Counter(lev(a["vs"][v], b["vs"][v]) for v in range(g.n)); cw = Counter(lev(a["W"][v], b["W"][v]) for v in range(g.n))
                cx.pop(None, None); cw.pop(None, None)
                for x, c in cx.items(): hx[x] += c
                for x, c in cw.items(): hw[x] += c
                gch = any(a["vs"][u] != b["vs"][u] or a["W"][u] != b["W"][u] for u in a["D"])
                print(f" k={k - i:2d} D={a['D']} {'; '.join(gates)} | switched {sw} | Xi-chg levels {dict(cx)} | W-chg levels {dict(cw)}"
                      f" | gate value change {gch}")
            print(" Xi change levels over the run:", sorted(hx.items(), key=str)); print(" W change levels over the run:", sorted(hw.items(), key=str))
        i = j + 1

if __name__ == "__main__":
    main()
