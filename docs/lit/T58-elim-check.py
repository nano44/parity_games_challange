#!/usr/bin/env python3
"""L-LIT T58 (docs/lit/T58-action-elimination.md §3): an ordinal analogue of action elimination inside one W-run of N5.
W-runs as in l-si gate.py / docs/lit/T54-tiebreak-check.py (tau fixed, no fallback, W's cycle nodes fixed). For a W-run F with states
p..q, Xi_end := Xi_q (Xi is non-decreasing along F, R15). For an Even edge e = (v, w):
  beta_t(v) := Xi_t(sigma_t(v)) (non-decreasing along F, T58 §3);
  T_e := the first state t of F with beta_t(v) >= Xi_end(w) (e is then "eliminated");
  Lemma ELIM-ORD (T58 §3): no adoption of e (sigma_{s+1}(v) = w != sigma_s(v)) at any s >= T_e.  VIOL counts failures (must be 0).
  VIOLX: the same with the threshold Xi_t(v) |> v (+) Xi_end(w) (si.Engine.extend); BMON: beta falls somewhere (must be 0).
Per W-run: ADOPT (adoptions), RETMAX (max adoptions of one edge), WIN (max over states t of F of the number of transitions until some
edge e in sigma_t that is not in sigma_q gets eliminated, with T_e := min of the two thresholds; HMZ-shaped "window"; the rest of the
run if none is), WINB (the same with the beta threshold only), HW (the TRUE window, no threshold: max over t of min over e in sigma_t, e not in
sigma_q, of (last state at which e is in sigma) + 1 - t; HMZ Lemma 6.4's quantity), ELIMS (edges eliminated while in use), LEN (transitions). Output: maxima over W-runs, VIOL summed. Usage (repo root): python3 -I docs/lit/T58-elim-check.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def wruns(g, start=None):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); WE = {}
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    def W(s, t):
        if t not in WE:
            WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        return WE[t].evaluate(s)[0]
    run = [s]; w = W(s, t)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w1 = W(ns, nt) if nt == t else None
        if nt != t or fb or any(w1[x][0] != w[x][0] for x in range(n)):
            yield run; run = [ns]
        else:
            run.append(ns)
        s, t, w = ns, nt, W(ns, nt)
    yield run

def run(g, start=None):
    n = g.n; own = g.owner; E = Engine(g)
    c = dict(VIOL=0, VIOLX=0, BMON=0, ADOPT=0, RETMAX=0, WIN=-1, WINB=-1, HW=-1, ELIMS=0, LEN=0, RUNS=0)
    for F in wruns(g, start):
        if len(F) < 2: continue
        c['RUNS'] += 1; c['LEN'] = max(c['LEN'], len(F) - 1)
        X = [E.evaluate(s)[0] for s in F]; K = [[E.key(x) for x in xs] for xs in X]; end = X[-1]
        T, TX = {}, {}
        for v in range(n):
            if own[v] != 0: continue
            for i in range(len(F) - 1):
                if K[i + 1][F[i + 1][v]] < K[i][F[i][v]]: c['BMON'] += 1
            for w in g.succ[v]:
                th, thx = K[-1][w], E.key(E.extend(v, end[w]))
                T[(v, w)] = next((i for i in range(len(F)) if K[i][F[i][v]] >= th), None)
                TX[(v, w)] = next((i for i in range(len(F)) if K[i][v] > thx), None)
        cnt = {}
        for i in range(len(F) - 1):
            for v in range(n):
                if own[v] == 0 and F[i + 1][v] != F[i][v]:
                    e = (v, F[i + 1][v]); c['ADOPT'] += 1; cnt[e] = cnt.get(e, 0) + 1
                    if T[e] is not None and i >= T[e]: c['VIOL'] += 1
                    if TX[e] is not None and i >= TX[e]: c['VIOLX'] += 1
        c['RETMAX'] = max([c['RETMAX']] + list(cnt.values()))
        last = F[-1]
        TM = {e: min([x for x in (T[e], TX[e]) if x is not None], default=None) for e in T}
        for name, TT in (('WIN', TM), ('WINB', T)):
            for i in range(len(F)):
                used = [(v, F[i][v]) for v in range(n) if own[v] == 0 and F[i][v] != last[v]]
                nxt = [TT[e] - i for e in used if TT[e] is not None and TT[e] > i]
                if nxt: c[name] = max(c[name], min(nxt))
                elif used: c[name] = max(c[name], len(F) - 1 - i)
        lastuse = {}
        for i in range(len(F)):
            for v in range(n):
                if own[v] == 0: lastuse[(v, F[i][v])] = i
        for i in range(len(F)):
            ws = [lastuse[(v, F[i][v])] + 1 - i for v in range(n) if own[v] == 0 and F[i][v] != last[v]]
            if ws: c['HW'] = max(c['HW'], min(ws))
        c['ELIMS'] = max(c['ELIMS'], sum(1 for e, te in TM.items() if te is not None and any(F[i][e[0]] == e[1] for i in range(te))))
    return c

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None)
    print(f"T58 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
