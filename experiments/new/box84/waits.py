#!/usr/bin/env python3
"""L-NEW box 84 (R3-POLY via R135's WAIT-CYCLE triple count). Runs N5 (SPEC S1-S5; box21/n5x.step) and at every state t records
every SELF-ROUTED BLOCK: Even X, successor g != sigma_t(X), (X, g) not in I_sigma_t, and the sigma-bar_t-play from g reaches X before
repeating a vertex and (if X lies on its own play's cycle) before meeting that cycle; pi = that play from g up to (excluding) X; c* = cycle node of Xi_t(X). Classes:
  REG : not E0 (Lemma WAIT-CYCLE' applies: the cycle C = X g pi X has rew(top C) < rew(c*), so C is never sigma-consistent again);
  E0  : X = c* and every vertex of pi ranks below X (the exception of WAIT-CYCLE'; X's competition is length only).
Checks over the whole run: VIOL = a later state with sigma(X) = g and the same Even pattern on pi after a REG block (must be 0);
E0RET = the same after an E0 block (allowed). DEADC = REG cycles whose top reward is NOT below rew(c*) (must be 0).
Per W-run F (R89; as box83/wchmax.py): for each (X, g): REG blocks, distinct Even patterns among them, ALT = takes of g by X preceded
(since X last took g, inside F) by a REG block of (X, g). Prints maxima and max WCH_F(e).
Usage: waits.py GAME.pg [START] | waits.py --rand N TRIALS SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def analyse(g, start):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
    S = [tuple(s)]; TAU = [tuple(t)]; FB = []
    for _ in range(20 * n * n + 50):
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]
    Wc = {}
    def Wv(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[k])[0]
    blocks = []                                   # (t, X, g, cls, pattern)
    out = dict(viol=0, e0ret=0, deadc=0, reg=0, e0=0, xoncyc=0)
    for k in range(T + 1):
        sig = S[k]; vs, sbar = E.evaluate(sig); Is = set(E.improving(sig, vs))
        nxt = lambda v: sig[v] if g.owner[v] == 0 else sbar[v]
        for X in ev:
            cstar = vs[X][0]
            for gg in g.succ[X]:
                if gg == sig[X] or (X, gg) in Is: continue
                path, y, ok = [], gg, False
                while y not in path:
                    if y == X: ok = True; break
                    path.append(y); y = nxt(y)
                if not ok: continue
                cyc, y = [X], sig[X]                      # X's own sigma-bar cycle if X lies on it; pi must enter it at X
                while y != X and y not in cyc and len(cyc) <= n: cyc.append(y); y = nxt(y)
                if y == X and any(v in cyc for v in path): continue
                pat = tuple((v, sig[v]) for v in path if g.owner[v] == 0)
                e0 = cstar == X and all(E.rank[v] < E.rank[X] for v in path)
                top = max(path + [X], key=lambda v: E.pp[v])
                if not e0 and not E.rew[top] < E.rew[cstar]: out['deadc'] += 1
                y, seen = sig[X], set()
                while y not in seen and y != X: seen.add(y); y = nxt(y)
                if y == X: out['xoncyc'] += 1
                out['e0' if e0 else 'reg'] += 1
                blocks.append((k, X, gg, 'E0' if e0 else 'REG', pat))
    # whole-run violation check
    idx = {}
    for b in blocks: idx.setdefault((b[1], b[2]), []).append(b)
    for (X, gg), bl in idx.items():
        for k in range(T + 1):
            if S[k][X] != gg: continue
            for (t1, _, _, cls, pat) in bl:
                if t1 < k and all(S[k][v] == w for v, w in pat):
                    out['viol' if cls == 'REG' else 'e0ret'] += 1
    # W-runs
    runs = []; cur = None
    for k in range(T):
        ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
        if not ok: cur = None; continue
        if cur is None: cur = [k, k]; runs.append(cur)
        cur[1] = k + 1
    mx = dict(wch=0, regF=0, patF=0, alt=0, runs=len(runs), T=T)
    for a, b in runs:
        W = [Wv(x, TAU[a]) for x in range(a, b + 1)]
        mx['wch'] = max([mx['wch']] + [sum(1 for i in range(b - a) if W[i + 1][e] != W[i][e]) for e in range(n)])
        for (X, gg), bl in idx.items():
            inF = [x for x in bl if a <= x[0] <= b and x[3] == 'REG']
            if not inF: continue
            mx['regF'] = max(mx['regF'], len(inF)); mx['patF'] = max(mx['patF'], len({x[4] for x in inF}))
            alt, pend = 0, False; times = {x[0] for x in inF}
            for k in range(a, b + 1):
                if k in times: pend = True
                if k > a and S[k][X] == gg and S[k - 1][X] != gg:
                    if pend: alt += 1
                    pend = False
            mx['alt'] = max(mx['alt'], alt)
    return out, mx

if __name__ == "__main__":
    if sys.argv[1] == "--rand":
        N, trials, seed = map(int, sys.argv[2:5]); rnd = random.Random(seed); tot = {}; best = {}
        for _ in range(trials):
            owner = [rnd.randint(0, 1) for _ in range(N)]; prio = rnd.sample(range(N), N)
            succ = [sorted(rnd.sample(range(N), rnd.randint(1, 3))) for _ in range(N)]
            g = pg.Game(prio, owner, succ)
            st = ({v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 0}, {v: rnd.choice(succ[v]) for v in range(N) if owner[v] == 1})
            out, mx = analyse(g, st)
            for k, v in out.items(): tot[k] = tot.get(k, 0) + v
            for k, v in mx.items():
                if v > best.get(k, (-1,))[0]: best[k] = (v, (prio, owner, succ, st) if k in ('alt', 'patF') else None)
            if out['viol'] or out['deadc']: print("VIOLATION", prio, owner, succ, st, out)
        print(f"WAITS-RAND n {N} trials {trials} seed {seed} totals {tot} maxima { {k: v[0] for k, v in best.items()} }")
        print("ARGMAX-alt", best['alt'][1]); print("ARGMAX-patF", best['patF'][1])
    else:
        g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
        out, mx = analyse(g, start); print(f"WAITS n {g.n} {out} {mx}")
