#!/usr/bin/env python3
"""L-RED R147: count HEAD-RED' small terms per W-run on n5b SPEC traces (L-SI box 53 §3 definitions).
W-run (RESULTS R89): maximal run of consecutive states of one tau-stretch none of whose transitions is an S4c fallback or changes lambda_W.
Per W-run F: |F| (transitions), CN = transitions switching sigma at an Even c in C (C = W-cycle nodes, fixed on F), CNmax = max_c CN_F(c),
XCN = transitions with a sigma-bar flip at an Odd o that is its own Xi-cycle node at k or at k+1, XCNmax = max_o.
Prints the W-run maximising each. Usage: xcn.py GAME.pg [START] [--all]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
pg = n5b.pg
def trace(g, s0=None, t0=None, cap=5000):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=cap)
    return tr, fb
def wruns(g, tr, fb):
    Wc = {}
    def W(s, t):
        if t not in Wc:
            h = pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)])
            Wc[t] = n5b.SpecSI(h)
        return Wc[t].evaluate(list(s))
    lam = lambda s, t: tuple(x[0] for x in W(s, t))
    runs = []; cur = [0]
    for k in range(len(tr) - 1):
        (s, t), (s2, t2) = tr[k], tr[k + 1]
        if t == t2 and not fb[k] and lam(s, t) == lam(s2, t):
            cur.append(k + 1)
        else:
            runs.append(cur); cur = [k + 1]
    runs.append(cur)
    return runs, W
def analyse(g, tr, fb):
    runs, W = wruns(g, tr, fb); SG = n5b.SpecSI(g); X = {}
    def Xi(k):
        if k not in X: X[k] = SG.evaluate_choice(list(tr[k][0]))
        return X[k]
    out = []
    for F in runs:
        if len(F) < 2: out.append(dict(L=0, CN=0, CNmax=0, XCN=0, XCNmax=0, F=F)); continue
        s0, t = tr[F[0]]; Wv = W(s0, t); C = [v for v in range(g.n) if Wv[v][0] == v and g.owner[v] == 0]
        cn = {}; xc = {}; CN = XCN = 0
        for k in F[:-1]:
            s, s2 = tr[k][0], tr[k + 1][0]
            sw = [c for c in C if s[c] != s2[c]]
            if sw: CN += 1
            for c in sw: cn[c] = cn.get(c, 0) + 1
            (x1, b1), (x2, b2) = Xi(k), Xi(k + 1)
            fl = [o for o in range(g.n) if g.owner[o] == 1 and b1[o] != b2[o] and (x1[o][0] == o or x2[o][0] == o)]
            if fl: XCN += 1
            for o in fl: xc[o] = xc.get(o, 0) + 1
        out.append(dict(L=len(F) - 1, CN=CN, CNmax=max(cn.values(), default=0), XCN=XCN, XCNmax=max(xc.values(), default=0), F=F, cn=cn, xc=xc))
    return out
if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    g = pg.read(a[0]); st = n5b.read_start(a[1], g) if len(a) > 1 else (None, None)
    try: tr, fb = trace(g, *st)
    except Exception as e: print(f"XCN {os.path.basename(a[0])} n {g.n} RUN-ERROR {e}"); sys.exit(0)
    out = analyse(g, tr, fb)
    big = lambda key: max(out, key=lambda r: r[key])
    print(f"XCN {os.path.basename(a[0])} n {g.n} iters {len(tr)-1} wruns {len(out)} maxL {big('L')['L']} "
          f"maxCN {big('CN')['CN']} maxCNc {big('CNmax')['CNmax']} maxXCN {big('XCN')['XCN']} maxXCNo {big('XCNmax')['XCNmax']} "
          f"sumCN {sum(r['CN'] for r in out)} sumXCN {sum(r['XCN'] for r in out)}")
    if "--all" in sys.argv:
        for r in out:
            if r['CN'] or r['XCN']: print(f"  run {r['F'][0]}-{r['F'][-1]} L {r['L']} CN {r['cn']} XCN {r['xc']}")
