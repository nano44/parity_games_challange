#!/usr/bin/env python3
"""L-RED 66 R236: an INDEPENDENT implementation of N5'-xi (SPEC S1-S5 of docs/new/N5-ssi-global.md with box 190's S4a tie rule, as
RESULTS R118 (k) / R117 use it), written from the SPEC TEXT for the faithfulness check of L-SI 52's F_n (Lead 14:37Z). No code from
n5.py, n5v.py, n5bxi.py, n5b.py or si.py. Readings (each a deviation from SPEC's exact tie-breaks, which fix counts only):
 R1 valuations: VJ (c, P, l) with rank by (prio, index), order of SPEC S1 (reward of c; P by its most relevant differing vertex;
    l longer better iff c odd). Odd's optimal counterstrategy sigma-bar: computed by switch-all strategy iteration for the minimiser
    on the one-player game (Even fixed), warm-started; any optimal counterstrategy gives the same values (VJ00), SPEC's choice of
    sigma-bar among optimal ones is NOT reproduced (it matters only through ties in S4b's tau_new).
 R2 S4a (Even): A(v) = {sigma(v)} + improving; arena H (Odd fixed to tau). Even's optimal values W* in H by switch-all SI (max).
    sigma_new(v): if v is not its own H-cycle node, among w in A(v) with W*(v) = ext(v, W*(w)) take the one with the BEST Xi_sigma(w)
    (box 190 mode xi), ties: larger index. If v is its own H-cycle node: among w with Lambda(W*(w)) = v and Pi = {} (a cycle with top v),
    the best Xi_sigma(w), ties larger index (SPEC's DFS choice is NOT reproduced here).
 R3 S4b (Odd): arena H' (Even fixed to sigma, Odd v restricted to {tau(v)} + improving-on-dual); Odd's optimal values in H' (min);
    tau_new(v): an optimal successor, ties: keep tau(v) if optimal, else larger index.
 R4 S3 start = SPEC FIX 1; S4c fallback = SPEC (best (Xi, w), larger index; only sigma changes if I_sigma != {}); S5 stop and output.
Usage: n5x236.py GAME.pg [mode xi|spec] -> prints iterations, fallbacks, Even's region size, and writes nothing."""
import sys
def parse(fn):
    prio, owner, succ = [], [], []
    for line in open(fn):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("start"): continue
        parts = line.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2]); ss = [int(x) for x in parts[3].split(",")]
        while len(prio) <= v: prio.append(None); owner.append(None); succ.append(None)
        prio[v], owner[v], succ[v] = p, o, sorted(set(ss))
    return prio, owner, succ
class Val:
    def __init__(s, prio):
        n = len(prio); order = sorted(range(n), key=lambda v: (prio[v], v)); s.rk = [0] * n
        for r, v in enumerate(order): s.rk[v] = r
        s.ev = [prio[v] % 2 == 0 for v in range(n)]
    def rew(s, v): return (s.rk[v] + 1) if s.ev[v] else -(s.rk[v] + 1)
    def better(s, a, b):           # a strictly better for Even than b
        if a[0] != b[0]: return s.rew(a[0]) > s.rew(b[0])
        d = a[1] ^ b[1]
        if d:
            z = max(d, key=lambda u: s.rk[u]); return (z in a[1]) == s.ev[z]
        if a[2] != b[2]: return (a[2] > b[2]) if not s.ev[a[0]] else (a[2] < b[2])
        return False
    def values(s, nxt):
        """values of every vertex in the functional graph nxt: (c, frozenset P, l)"""
        n = len(nxt); val = [None] * n; state = [0] * n
        for v0 in range(n):
            if val[v0] is not None: continue
            path = []; v = v0; pos = {}
            while val[v] is None and v not in pos: pos[v] = len(path); path.append(v); v = nxt[v]
            if val[v] is None:               # new cycle path[pos[v]:]
                cyc = path[pos[v]:]; c = max(cyc, key=lambda u: s.rk[u]); i = cyc.index(c)
                L = len(cyc); val[c] = (c, frozenset(), 0)
                for j in range(1, L):        # walk backwards from c along the cycle
                    u = cyc[(i - j) % L]; w = val[nxt[u]]
                    val[u] = (c, w[1] | ({u} if s.rk[u] > s.rk[c] else frozenset()), w[2] + 1)
                path = path[:pos[v]]
            for u in reversed(path):
                w = val[nxt[u]]; c = w[0]
                val[u] = (c, w[1] | ({u} if s.rk[u] > s.rk[c] else frozenset()), w[2] + 1)
        return val
def optimum(V, owner, succ, fixed, chooser_owner, start, maximise):
    """one-player optimum: vertices with owner == chooser_owner choose (from succ), the others follow fixed[v].
    Switch-all strategy iteration from start; returns (values, strategy dict for the chooser)."""
    n = len(succ); st = dict(start)
    while True:
        nxt = [st[v] if owner[v] == chooser_owner else fixed[v] for v in range(n)]
        val = V.values(nxt); ch = False
        for v in st:
            b = st[v]
            for w in succ[v]:
                if (V.better(val[w], val[b]) if maximise else V.better(val[b], val[w])): b = w
            if b != st[v]: st[v] = b; ch = True
        if not ch: return val, st
def ext(V, v, w):
    return (w[0], w[1] | ({v} if V.rk[v] > V.rk[w[0]] else frozenset()), w[2] + 1)
def run(prio, owner, succ, mode="xi", cap=10 ** 6):
    n = len(prio); V = Val(prio); dprio = [p + 1 for p in prio]; Vd = Val(dprio); downer = [1 - o for o in owner]
    def r(p): return p if p % 2 == 0 else -p
    sigma = {v: max(succ[v], key=lambda w: (r(prio[w]), w if prio[w] % 2 == 0 else -w)) for v in range(n) if owner[v] == 0}
    tau = {v: max(succ[v], key=lambda w: (r(dprio[w]), w if dprio[w] % 2 == 0 else -w)) for v in range(n) if owner[v] == 1}
    sbar = {v: succ[v][0] for v in range(n) if owner[v] == 1}; tbar = {v: succ[v][0] for v in range(n) if owner[v] == 0}
    it = fb = 0
    while it < cap:
        fs = [sigma.get(v) for v in range(n)]; vs, sbar = optimum(V, owner, succ, fs, 1, sbar, False)
        Is = {v: [w for w in succ[v] if w != sigma[v] and V.better(vs[w], vs[sigma[v]])] for v in sigma}
        Is = {v: ws for v, ws in Is.items() if ws}
        ft = [tau.get(v) for v in range(n)]; vt, tbar = optimum(Vd, downer, succ, ft, 1, tbar, False)
        It = {v: [w for w in succ[v] if w != tau[v] and Vd.better(vt[w], vt[tau[v]])] for v in tau}
        It = {v: ws for v, ws in It.items() if ws}
        if not Is and not It: break
        ns, nt = dict(sigma), dict(tau)
        if Is:                         # S4a
            A = [None] * n
            for v in range(n):
                A[v] = sorted({sigma[v]} | set(Is.get(v, []))) if owner[v] == 0 else [tau[v]]
            W, _ = optimum(V, owner, A, [tau.get(v) for v in range(n)], 0, dict(sigma), True)
            for v in sigma:
                if W[v][0] != v:
                    opts = [w for w in A[v] if ext(V, v, W[w]) == W[v]]
                else:
                    opts = [w for w in A[v] if W[w][0] == v and not W[w][1]]
                assert opts, ("no optimal option", v)
                if mode == "xi":
                    b = opts[0]
                    for w in opts[1:]:
                        if V.better(vs[w], vs[b]) or (not V.better(vs[b], vs[w]) and w > b): b = w
                else:
                    b = sigma[v] if sigma[v] in opts else max(opts)
                ns[v] = b
        if It:                         # S4b (Odd minimises on G, in arena H')
            A = [None] * n
            for v in range(n):
                A[v] = sorted({tau[v]} | set(It.get(v, []))) if owner[v] == 1 else [sigma[v]]
            W, _ = optimum(V, owner, A, [sigma.get(v) for v in range(n)], 1, dict(tau), False)
            for v in tau:
                opts = [w for w in A[v] if (ext(V, v, W[w]) == W[v] if W[v][0] != v else (W[w][0] == v and not W[w][1]))]
                assert opts, ("no optimal Odd option", v)
                nt[v] = tau[v] if tau[v] in opts else max(opts)
        if ns == sigma and nt == tau:  # S4c fallback
            fb += 1
            if Is:
                for v, ws in Is.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if V.better(vs[w], vs[b]) or (not V.better(vs[b], vs[w]) and w > b): b = w
                    ns[v] = b
                nt = dict(tau)
            else:
                for v, ws in It.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if Vd.better(vt[w], vt[b]) or (not Vd.better(vt[b], vt[w]) and w > b): b = w
                    nt[v] = b
        sigma, tau = ns, nt; it += 1
    fs = [sigma.get(v) for v in range(n)]; vs, sbar = optimum(V, owner, succ, fs, 1, sbar, False)
    win = [V.ev[vs[v][0]] for v in range(n)]
    return it, fb, win, sigma, sbar
if __name__ == "__main__":
    prio, owner, succ = parse(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else "xi"
    it, fb, win, s, sb = run(prio, owner, succ, mode)
    print("N5X236", sys.argv[1].split("/")[-1], "n", len(prio), "mode", mode, "iterations", it, "fallbacks", fb, "even_wins", sum(win), flush=True)
