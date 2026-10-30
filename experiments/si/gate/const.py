#!/usr/bin/env python3
"""L-SI box 51b §3: on every W-constant interval of every W-run that contains a W-flat transition, test whether the gate data are
constant over the interval: D_k, the full gate map g_k (all vertices), lambda_Xi, lambda_W, Z_k and LEV_k on Z_k (the coordinate index of gate.py's PHI, length coordinate omitted).
Prints one line per such interval: W-run start, interval [p, q], flat transitions, and which of the data change. Usage: const.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gate as G
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
def run(g, start=None):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); own = g.owner
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    def snap(s, t):
        W = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)])).evaluate(s)[0]
        xv, sb = E.evaluate(s); D = frozenset(o for o in range(n) if own[o] == 1 and sb[o] != t[o])
        def gt(u):
            x, seen = u, set()
            while x not in D:
                if x in seen: return None
                seen.add(x); x = s[x] if own[x] == 0 else t[x]
            return x
        Z = frozenset(v for v in range(n) if E.key(xv[v]) != E.key(W[v]))
        def phi(v):
            a = [E.key(xv[v])[0]] + [((xv[v][1] >> r) & 1) for r in range(n - 1, -1, -1)]; b = [E.key(W[v])[0]] + [((W[v][1] >> r) & 1) for r in range(n - 1, -1, -1)]
            return next((i for i in range(len(a)) if a[i] != b[i]), len(a))
        return dict(W=[E.key(x) for x in W], D=D, gate=tuple(gt(u) for u in range(n)), lx=tuple(x[0] for x in xv), lw=tuple(x[0] for x in W), Z=Z,
                    phi=tuple(phi(v) for v in sorted(Z)))
    k = 0; cur = [snap(s, t)]; flat = 0; out = []
    def flush():
        if flat: out.append((k - len(cur) + 1, k, flat, [key for key in ('D', 'gate', 'lx', 'lw', 'Z', 'phi') if len({str(c[key]) for c in cur}) > 1]))
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt); k += 1
        S1 = snap(ns, nt)
        if nt == t and not fb and S1['W'] == cur[-1]['W']: cur.append(S1); flat += 1
        else: flush(); cur = [S1]; flat = 0
        s, t = ns, nt
    flush(); return out
if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0])
    for p, q, f, ch in run(g, readstart(a[1]) if len(a) > 1 else None): print(f"CONST {os.path.basename(a[0])} interval [{p}, {q}] flat {f} changes {','.join(ch) or 'none'}")
