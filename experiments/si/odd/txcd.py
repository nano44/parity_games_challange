#!/usr/bin/env python3
"""L-SI box 52 (docs/si/N5-TXCD-box52.md): the descent of a tied Xi-climb (TXC event (z, s): Xi_{s+1}(z) > Xi_s(z), W_{s+1}(z) = W_s(z),
inside a W-run) along z's (sigma_{s+1}, sigmabar_{s+1})-play to its TERMINAL x, the first vertex of the play that is
 T1: lambda_Xi(x) changes at s;  T2: Even, sigma_s(x) != sigma_{s+1}(x) (G if lambda_Xi is unchanged at s everywhere: a GXC event of L-NEW
 box 70; L otherwise);  T3: Odd with sigmabar_s(x) != tau(x) or sigmabar_{s+1}(x) != tau(x) (a GATE).
T4: lambda_W(x) = x (own W-cycle node; box 53 fix D2). Box 53 fix D1: after a tau-change W is re-read with the new tau.
Otherwise the descent steps to sigma(x) (Even) or tau(x) (Odd) and must find a TXC event there (DESC_V counts failures; CYC_V descents
that close a cycle without a terminal; TERM_V terminals that are not themselves tied climbs). Counters (sums over W-runs): TXC, T1, T2G,
T2L, T3, DESC_V, CYC_V, TERM_V, GXC (all GXC events with t in a W-run), GATE (distinct (x, s) gate terminals), CNW (TXC events at own W-cycle nodes), MULT (most TXC events with
one terminal). Usage: txcd.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
def run(g, start=None):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    WE = {}
    def W(s, t):
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
        e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
    def X(s):
        vx, sb = E.evaluate(s); return vx, [E.key(x) for x in vx], sb
    c = dict(TXC=0, T1=0, T2G=0, T2L=0, T3=0, T4=0, DESC_V=0, CYC_V=0, TERM_V=0, GXC=0, GATE=0, CNW=0, MULT=0)
    w0, wk0 = W(s, t); x0 = X(s)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w1, wk1 = W(ns, t); x1 = X(ns)
        inrun = not (nt != t or ns == s or fb or any(w1[x][0] != w0[x][0] for x in range(n)))
        if inrun:
            (v0, k0, sb0), (v1, k1, sb1) = x0, x1
            lamfix = all(v0[x][0] == v1[x][0] for x in range(n))
            tied = lambda x: k1[x] > k0[x] and wk1[x] == wk0[x]
            for v in range(n):                                     # GXC events (L-NEW box 70 §3) at this transition
                if g.owner[v] == 0 and ns[v] != s[v] and lamfix and k0[v] != wk0[v] and k1[v] > k0[v] and wk1[v] <= wk0[v]: c['GXC'] += 1
            term = {}
            for z in range(n):
                if not tied(z): continue
                c['CNW'] += w1[z][0] == z
                c['TXC'] += 1; x, seen, kind = z, set(), None
                while kind is None:
                    seen.add(x)
                    if v0[x][0] != v1[x][0]: kind = 'T1'
                    elif g.owner[x] == 0 and ns[x] != s[x]: kind = 'T2G' if lamfix else 'T2L'
                    elif g.owner[x] == 1 and (sb0[x] != t[x] or sb1[x] != t[x]): kind = 'T3'
                    elif w1[x][0] == x: kind = 'T4'                        # box 53 fix D2 / N-8: own W-cycle node
                    else:
                        y = ns[x] if g.owner[x] == 0 else t[x]
                        if y in seen: kind = 'CYC_V'
                        elif not tied(y): kind = 'DESC_V'
                        else: x = y
                c[kind] += 1
                if kind in ('T1', 'T2G', 'T2L', 'T3', 'T4'):
                    if not tied(x): c['TERM_V'] += 1
                    term[(kind, x)] = term.get((kind, x), 0) + 1
            if term: c['MULT'] = max(c['MULT'], max(term.values()))
            c['GATE'] += sum(1 for (k, x) in term if k == 'T3')
        if nt != t: w1, wk1 = W(ns, nt)                           # box 53 fix D1 / N-7: next W-run is read with the NEW tau
        s, t, w0, wk0, x0 = ns, nt, w1, wk1, x1
    return c
if __name__ == '__main__':
    args = sys.argv[1:]; g = load(args[0]); c = run(g, readstart(args[1]) if len(args) > 1 else None)
    print(f"TXCD {os.path.basename(args[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
