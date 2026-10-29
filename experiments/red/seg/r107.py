#!/usr/bin/env python3
"""L-RED successor 26 (R107, Lead 2026-10-29 11:07Z STEP 1): the mkr family from the S3 DEFAULT start and from mkr's explicit start.
Per game and start: total iterations, fallbacks, phases (PHASE = tau, lambda_sigma (cycle nodes of Xi_sigma on G) and lambda_tau (cycle
nodes of Xi_tau on G^d) constant; as experiments/red/sel/phsw.py), runs (segchk.py: tau, honest lambda constant, no fallback inside),
longest phase PL, longest run RUN, per-vertex switch counts (max over Even v inside the longest run and over the whole execution, with
the arg vertex's name), and the second engine (n5.py driver on si.py): iterations, fallbacks, and the full state sequence compared.
Usage: r107.py GAME.pg START|S3 [--noxeng]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new"))
import n5b

def measure(path, start):
    g = n5b.pg.read(path); n = g.n
    lab = {}
    for line in open(path):
        m = re.match(r'\s*(\d+)\s.*"(.*)"', line)
        if m: lab[int(m.group(1))] = m.group(2)
    s0, t0 = (None, None) if start == "S3" else n5b.read_start(start, g)
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    N.run(s0, t0, trace=tr, fbtrace=fb)
    K = len(tr); EV = [v for v in range(n) if g.owner[v] == n5b.EVEN]
    S = [s for s, _ in tr]; T = [t for _, t in tr]
    ES = [[s[v] if g.owner[v] == n5b.EVEN else -1 for v in range(n)] for s in S]
    lam_s = [tuple(x[0] for x in N.ev(N.SG, e)) for e in ES]
    lam_t = [tuple(x[0] for x in N.ev(N.SD, list(t))) for t in T]
    lam_h = [tuple(x[0] for x in N.opt(N.SG, e)[0]) for e in ES]          # segchk's run key (honest lambda)
    def cut(key, breakfb):
        out, a = [], 0
        for k in range(1, K + 1):
            if k == K or key(k) != key(k - 1) or (breakfb and fb[k - 1]):
                out.append((a, k - 1)); a = k
        return out
    phases = cut(lambda k: (T[k], lam_s[k], lam_t[k]), False)
    runs = cut(lambda k: (T[k], lam_h[k]), True)
    def sw(a, b):
        c = {v: sum(1 for t in range(a, b) if S[t][v] != S[t + 1][v]) for v in EV}
        v = max(EV, key=lambda v: (c[v], -v)); return c[v], lab.get(v, str(v)), sum(1 for x in c.values() if x)
    PL = max(phases, key=lambda p: p[1] - p[0]); RUN = max(runs, key=lambda p: p[1] - p[0])
    a, b = RUN                                    # L-SI's reduction quantities inside the longest run
    XI = [N.ev(N.SG, e) for e in ES]
    rises = {w: sum(1 for t in range(a, b) if XI[t][w] != XI[t + 1][w]) for w in range(n)}
    swc = {v: sum(1 for t in range(a, b) if S[t][v] != S[t + 1][v]) for v in EV}
    slack = {v: sum(rises[w] + 1 for w in dict.fromkeys(g.succ[v])) - swc[v] for v in EV if len(set(g.succ[v])) >= 2}
    vmin = min(slack, key=lambda v: (slack[v], v)) if slack else None
    red = dict(sumsw=sum(swc.values()), maxrise=max(rises.values()), minslack=slack.get(vmin), at=lab.get(vmin, vmin))
    return dict(n=n, it=K - 1, fb=sum(fb), phases=len(phases), runs=len(runs), PL=PL, RUN=RUN, red=red,
                sw_run=sw(*RUN), sw_all=sw(0, K - 1), tr=tr, fbl=fb, g=g, s0=s0, t0=t0)

def xeng(path, r):
    import n5, si
    g = n5.pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    log = {"s": [], "t": []}; orig = si.Engine.evaluate; ids = {}
    def ev(self, strat):
        if getattr(self, "_tag", None) is None:
            self._tag = "s" if not ids else ("t" if len(ids) == 1 else "x"); ids[id(self)] = self._tag
        if self._tag in "st": log[self._tag].append(tuple(strat))
        return orig(self, strat)
    si.Engine.evaluate = ev
    st = None if r["s0"] is None else ({v: w for v, w in enumerate(r["s0"]) if w >= 0}, {v: w for v, w in enumerate(r["t0"]) if w >= 0})
    it, f, win, ws, _ = n5.run(g, "n5", st)
    si.Engine.evaluate = orig
    A = [(tuple(x if g.owner[v] == 0 else None for v, x in enumerate(s)), tuple(x if g.owner[v] == 1 else None for v, x in enumerate(t)))
         for s, t in r["tr"]]
    B = [(tuple(x if g.owner[v] == 0 and x >= 0 else None for v, x in enumerate(s)),
          tuple(x if g.owner[v] == 1 and x >= 0 else None for v, x in enumerate(t))) for s, t in zip(log["s"], log["t"])]
    return it, f, A == B

if __name__ == "__main__":
    r = measure(sys.argv[1], sys.argv[2])
    line = (f"n {r['n']} start {sys.argv[2] if sys.argv[2] == 'S3' else 'explicit'} | n5b it {r['it']} fb {r['fb']} phases {r['phases']} "
            f"runs {r['runs']} | PL {r['PL'][1] - r['PL'][0]} {r['PL']} | RUN {r['RUN'][1] - r['RUN'][0]} {r['RUN']} | "
            f"maxsw in RUN {r['sw_run'][0]} ({r['sw_run'][1]}; switchers {r['sw_run'][2]}) | maxsw all {r['sw_all'][0]} ({r['sw_all'][1]}) | RUN: sum_v sw {r['red']['sumsw']} max Xi-changes {r['red']['maxrise']} "
            f"min_v [sum_succ (changes+1) - sw(v)] {r['red']['minslack']} at {r['red']['at']}")
    if "--noxeng" not in sys.argv:
        it, f, same = xeng(sys.argv[1], r)
        line += f" | n5.py it {it} fb {f} states identical {same}"
    print(line)
