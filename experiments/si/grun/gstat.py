#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for CONJECTURE G-RUN (docs/si/N5-GRUN-box25.md). Per fallback-free in-phase run S (runlin/trace.runs):
G(S) = transitions with sigma-bar_t != sigma-bar_(t+1); G^K(S) the same with sigma-bar compared on R81's K only; per Odd vertex u: CH(u) = changes of sigma-bar(u) in S, and RET(u) = changes back to
an option u held earlier in S. Prints per corpus: runs, max G, max G/n, max per-gate CH, max CH(u)/deg(u), max RET, and the top runs.
Usage: gstat.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
from trace import runs
sys.path.insert(0, os.path.join(HERE, "..", "piece")); from pieceh import kset
C = Counter(); TOP = []

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; K = [u for u in sorted(kset(g)) if g.owner[u] == 1]
    for a, b, i, j in runs(R):
        if b <= a: continue
        G = sum(R[t]["sb"] != R[t + 1]["sb"] for t in range(a, b)); C["runs"] += 1
        GK = sum(any(R[t]["sb"][u] != R[t + 1]["sb"][u] for u in K) for t in range(a, b))
        C["GK_max"] = max(C["GK_max"], GK); C["GK_over_n_x1000_max"] = max(C["GK_over_n_x1000_max"], 1000 * GK // n); C["G_minus_GK_max"] = max(C["G_minus_GK_max"], G - GK)
        ch, ret = Counter(), Counter()
        for u in range(n):
            if g.owner[u] != 1: continue
            held = {R[a]["sb"][u]}
            for t in range(a, b):
                x, y = R[t]["sb"][u], R[t + 1]["sb"][u]
                if x != y:
                    ch[u] += 1
                    if y in held: ret[u] += 1
                    held.add(y)
        mch = max(ch.values(), default=0); mret = max(ret.values(), default=0)
        mdeg = max((ch[u] / len(set(g.succ[u])) for u in ch), default=0)
        C["G_max"] = max(C["G_max"], G); C["G_over_n_x1000_max"] = max(C["G_over_n_x1000_max"], 1000 * G // n)
        C["CH_max"] = max(C["CH_max"], mch); C["RET_max"] = max(C["RET_max"], mret)
        C["CH_over_deg_x100_max"] = max(C["CH_over_deg_x100_max"], int(100 * mdeg))
        C["G_sum"] += G; C["gates_changing_max"] = max(C["gates_changing_max"], len(ch))
        TOP.append((G, n, b - a, len(ch), mch, mret, name, a, b))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if not p: continue
            st = readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None
            run(load(os.path.join(ROOT, p[0])), p[0], st)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in sorted(TOP, key=lambda x: (-x[0] / x[1]))[:12]: print("TOP G %d n %d run %d gates %d CHmax %d RETmax %d %s [%d,%d]" % x)

if __name__ == "__main__":
    main()
