#!/usr/bin/env python3
"""L-SI box 64: exact per-genome quantities of L-NEW's external-flip model E_m (docs/new/N5-SLOT-box160.md §0-§1, box 161).
Genome format = L-NEW box 150 JSON (levels 0..m, R197 2-wide ladder convention, ISO: no option has a level-0 mover as Xi-target).
Level 0 is the outside agent: only the bit b_0 = [key(mover 0) < key(mover 1)] matters above level 0 (box 160 Lemma W-ONLY), so the
level-0 movers are forced to a configuration q_b with that bit. A counted step moves a mover of level >= 1 (IDEAL step rule of
RESULTS R104, keys under the NEW state, lowest level first; own implementation, cross-checked against box 150's Gen).
Per genome and start s (states of levels >= 1) and initial bit b:
  Tk[k](s,b) = max number of steps with at most k flips of b (flips free, any time);   T_inf(s) = max over all flip schedules;
  LP(s)      = longest directed path from s in the improvement cube o_G restricted to the movers of level >= 1 (RESULTS R106);
  H_b run    = run with b fixed (k = 0).
Usage: flipdp.py genome.json ... [K=4]  -> one line per genome: max over starts and initial bit of T_0..T_K, T_inf, LP.
Self-checks (exit 1 on any failure): XSIM (k = 0 run equals box 150 Gen run of the genome restricted at level 0),
PATH (every step of every schedule is a directed path of o_G in increasing pi, R106 MULTI->SINGLE), MONO_K (T_k nondecreasing in k),
CAP (T_inf <= LP)."""
import sys, os, json, itertools
from functools import lru_cache
HERE = os.path.dirname(os.path.abspath(__file__))

class Ext:
    def __init__(s, G):
        s.G = G; s.N = G["N"]; s.lev = G["lev"]; s.opts = G["opts"]; s.gate = G["gate"]; s.br = G["br"]; s.bp = G["bp"]
        s.L0 = [v for v in range(s.N) if s.lev[v] == 0]; s.UP = [v for v in range(s.N) if s.lev[v] > 0]
        assert s.L0 == [0, 1], "R197 convention: level-0 movers 0 and 1"
        for v in s.UP:
            for o in s.opts[v]:
                assert o[1] not in s.L0, "not ISO"
        s.byl = sorted(range(s.N), key=lambda v: (s.lev[v], v))
        # level-0 configurations with each value of b_0 (keys of level-0 movers are their own gates)
        s.q = {}
        for q in itertools.product(*[range(len(s.opts[v])) for v in s.L0]):
            b = int(s.gate[0][q[0]] < s.gate[1][q[1]]); s.q.setdefault(b, q)
        assert set(s.q) == {0, 1}, "both values of b_0 must be realisable"
        s.order = s.topo()
    def topo(s):
        if "xorder" in s.G: return list(s.G["xorder"])
        N = s.N; indeg = [0] * N
        for v in range(N):
            for o in s.opts[v]:
                if o[1] >= 0: indeg[o[1]] += 1
        order, av = [], sorted(v for v in range(N) if indeg[v] == 0)
        while av:
            v = av.pop(0); order.append(v)
            for o in s.opts[v]:
                if o[1] >= 0:
                    indeg[o[1]] -= 1
                    if indeg[o[1]] == 0: av.append(o[1])
        return order
    def eps(s, v, k):
        m = s.opts[v][k][2]; return (1 if s.bp[m] == 0 else -1) * (1 << s.br[m])
    def face(s, st, v, k):
        tot = 0
        while True:
            tot += s.eps(v, k); xt = s.opts[v][k][1]
            if xt < 0: return tot
            v, k = xt, st[xt]
    def better(s, st, v):
        """options of v strictly Xi-better than its current one"""
        c = s.face(st, v, st[v]); return [k for k in range(len(s.opts[v])) if s.face(st, v, k) > c]
    def full(s, up, b):
        st = [0] * s.N
        for i, v in enumerate(s.L0): st[v] = s.q[b][i]
        for i, v in enumerate(s.UP): st[v] = up[i]
        return st
    def step(s, up, b):
        """one IDEAL step with level 0 forced to q_b; returns new up-state tuple (== up if nothing moves)"""
        st = s.full(up, b); A = {v: [st[v]] + s.better(st, v) for v in s.UP}
        if all(len(A[v]) == 1 for v in s.UP): return up
        key = [None] * s.N; ns = list(st)
        for v in s.byl:
            if s.lev[v] == 0:
                key[v] = (s.gate[v][st[v]],); continue
            def ok(k):
                wt = s.opts[v][k][0]; return (s.gate[v][k],) if wt < 0 else key[wt] + (s.gate[v][k],)
            k = min(A[v], key=ok); ns[v] = k; key[v] = ok(k)
        return tuple(ns[v] for v in s.UP)
    def cube_out(s, up):
        """directed edges of o_G (levels >= 1 only; level 0 irrelevant under ISO): coordinates i whose mover is not on its better option"""
        st = s.full(up, 0); return [i for i, v in enumerate(s.UP) if len(s.opts[v]) == 2 and s.better(st, v)]

def analyse(G, K=4, check=True):
    E = Ext(G); n = len(E.UP); deg = [len(E.opts[v]) for v in E.UP]
    states = list(itertools.product(*[range(d) for d in deg]))
    nxt = {(u, b): E.step(u, b) for u in states for b in (0, 1)}
    pos = {v: i for i, v in enumerate(E.order)}
    bad = []
    if check:  # PATH: each step = switches toward the better option, done one at a time in increasing pi, each an edge of o_G
        for (u, b), w in nxt.items():
            if w == u: continue
            mv = sorted([i for i in range(n) if u[i] != w[i]], key=lambda i: pos[E.UP[i]])
            cur = list(u)
            for i in mv:
                if i not in E.cube_out(tuple(cur)): bad.append(("PATH", u, b)); break
                cur[i] = w[i]
            if tuple(cur) != w: bad.append(("PATH2", u, b))
    # T_inf(u) = longest path with free choice of b at every step
    sys.setrecursionlimit(100000)
    @lru_cache(None)
    def Tinf(u):
        best = 0
        for b in (0, 1):
            w = nxt[(u, b)]
            if w != u: best = max(best, 1 + Tinf(w))
        return best
    @lru_cache(None)
    def Tk(k, u, b):
        w = nxt[(u, b)]; best = 1 + Tk(k, w, b) if w != u else 0
        if k > 0: best = max(best, Tk(k - 1, u, 1 - b))
        return best
    @lru_cache(None)
    def LP(u):
        best = 0
        for i in E.cube_out(u):
            w = list(u); w[i] = 1 - w[i]; best = max(best, 1 + LP(tuple(w)))
        return best
    res = {"T": [max(Tk(k, u, b) for u in states for b in (0, 1)) for k in range(K + 1)],
           "Tinf": max(Tinf(u) for u in states), "LP": max(LP(u) for u in states), "n_up": n}
    if check:
        if any(res["T"][k] > res["T"][k + 1] for k in range(K)): bad.append(("MONO_K",))
        if res["Tinf"] > res["LP"] or res["T"][K] > res["Tinf"]: bad.append(("CAP",))
    res["bad"] = bad
    res["_f"] = (Tk, Tinf, LP, nxt, states, E)
    return res

def xsim(G):
    """XSIM: for each b, run of E with b fixed equals box 150 Gen run of G with level 0 restricted to q_b, from every start"""
    ns = {"__file__": os.path.join(HERE, "ref", "box150", "check.py")}
    src = open(ns["__file__"]).read().split("\nif __name__")[0]
    exec(src, ns); Gen, restrict = ns["Gen"], ns["restrict"]
    E = Ext(G); bad = 0
    for b in (0, 1):
        for u in itertools.product(*[range(len(E.opts[v])) for v in E.UP]):
            sa = E.full(u, b); H = restrict(G, E.L0, sa); g = Gen(H); S, _ = g.run(H["start"])
            cur = u; seq = [u]
            while True:
                w = E.step(cur, b)
                if w == cur: break
                seq.append(w); cur = w
            ref = [tuple(st[v] for v in E.UP) for st in S]
            if ref != seq: bad += 1
    return bad

if __name__ == "__main__":
    K = int(os.environ.get("K", "4")); tot_bad = 0
    for p in sys.argv[1:]:
        G = json.load(open(p)); r = analyse(G, K); xb = xsim(G)
        print(os.path.basename(p), "m", max(G["lev"]), "T_0..T_%d" % K, r["T"], "T_inf", r["Tinf"], "LP", r["LP"],
              "bad", len(r["bad"]), "XSIM", xb)
        tot_bad += len(r["bad"]) + xb
    print("TOTAL bad", tot_bad); sys.exit(1 if tot_bad else 0)
