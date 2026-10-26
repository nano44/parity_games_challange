#!/usr/bin/env python3
"""Box 39 (L-RED): independent counter for L-NEW's CONJECTURE PF-THETA (linear form), docs/new/N5-DROP-box35.md §8 (l-new 3939d3b):
"in a scope run, while the last fallback has level M, θ changes at most n times (for each M)". Written from that text, not pfclimb.py.
Scope run, M_k, θ = Ξ(o): as sox3.py (P-N5-CLS §0). For every scope run S and every in-scope fallback k with level M = M_k, the stretch
starts after k and lasts until the next in-scope fallback of S with a DIFFERENT level (exclusive) or the end of S; θ-changes at its
transitions are summed per (S, M) (a later fallback of the same level continues the stretch). PFT counts (S, M) with > n changes.
Usage: sox5.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, sox3

def analyse(g, cap=5000):
    import pg, n5
    from si import Engine
    from sox import lev, BOT
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n
    S, FB, E = sox.trace(g, cap)
    it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    N = len(S); ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]; Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd == "tau" else sb[k][x])
        return out
    H1 = [o not in play(k, sb[k][o], "sbar") for k in range(N)]; H2 = [o not in play(k, S[k][1][o], "tau") for k in range(N)]
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    cw = [Wv[k][o][0] for k in range(N)]
    scope = [inph[k] and H1[k] and H2[k] and cw[k] == lam[k][o] and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    def M(k): return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in E.improving(S[k][0], Xi[k])), default=BOT)
    best = 0; bestM = None; cnt = 0; runs = 0; k = 0
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]; runs += 1
        per = {}
        for i, f0 in enumerate(fbs):
            Mf = M(f0)
            if i > 0 and M(fbs[i - 1]) == Mf: continue          # same level continues the previous stretch
            j = i
            while j + 1 < len(fbs) and M(fbs[j + 1]) == Mf: j += 1
            end = fbs[j + 1] if j + 1 < len(fbs) else e + 1     # exclusive
            c = sum(Xi[t][o] != Xi[t + 1][o] for t in range(f0 + 1, end))
            per[Mf] = per.get(Mf, 0) + c
        for Mf, c in per.items():
            if c > best: best, bestM = c, Mf
            if c > n: cnt += 1
        k = e + 1
    return dict(n=n, it=len(FB), fb=sum(FB), runs=runs, best=best, M=bestM, PFT=cnt)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: continue
        r = analyse(g); print(os.path.basename(f), r, flush=True)
