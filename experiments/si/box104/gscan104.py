#!/usr/bin/env python3
"""L-SI box 104, Addendum B probe: N5 (SPEC) on guided wrappers of Friedmann's H_n ([F11] Section 8.4; L-COMP's hn.py, mode fig, iota)
with different FIXED Odd faces at the cycle gates. DATA only; a negative result (no variant grows faster than quadratically).
The wrapper is guide104.py's Wg with two more parameters: gamma maps an Even edge (v, w) to the vertex its fixed face leads to (default
w); rho0(o) may be a vertex two Odd moves away. A face that skips e_i passes a pad with e_i's priority (COPY = 1) or not (COPY = 0).
In H_n the only Odd vertices with two successors are the e_i (-> d1_i or h_i); e_i is entered from d3_i (Even) and from f_i (Odd).
Parameters: GF = where the fixed face of f_i leads (e = to e_i, d1 = into the cycle, h = out to h_i); G3 = where the fixed face of the
edge d3_i -> e_i leads (e | d1 | h); RE = rho0(e_i) (d1 | h); COPY.   Usage: gscan104.py GF G3 RE COPY n...   (env as guide104.py)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wrap104 as W
from wrap104 import pg, n5v, n5, n5x, zielonka
from si import Engine
ALG = os.environ.get("ALG", "spec"); CORE = os.environ.get("CORE", "high")

def wrapg(H, s0, rho0, gamma=None, copy=True):
    gamma = gamma or {}
    n = H.n; prio = [p + 6 for p in H.prio]; own = list(H.owner); succ = [None] * n; std_s = {}; std_t = {}; mp = {}
    def new(p, o, s=None): prio.append(p); own.append(o); succ.append(s); return len(prio) - 1
    K = [new(0, 0) for _ in range(4)]; own[K[2]] = 1
    pA = new(0, 0, [K[3]]); s_ = new(0, 0, [K[1]]); q = new(1, 0, [K[0]]); r = new(0, 0, [K[1]])
    succ[K[0]] = [K[1], pA]; succ[K[1]] = [q, s_]; succ[K[2]] = [r, K[2]]; succ[K[3]] = [K[1], K[2]]
    std_s[K[0]] = pA; std_s[K[1]] = s_; std_s[K[3]] = K[2]; std_t[K[2]] = K[2]
    valves = []
    def valve(w):
        pb = new(1, 0, [K[0]]); y = new(2, 0, [w]); b = new(0, 0, [y, pb]); std_s[b] = y; valves.append(b); return b
    for v in range(n):
        out = []
        if H.owner[v] == 0:
            for w in H.succ[v]:
                b = valve(w); pbeta = new(0, 0, [b]); tg = gamma.get((v, w), w); u2 = new((H.prio[w] + 6) if (tg != w and copy) else 0, 0, [tg]); u1 = new(0, 0, [u2]); pgd = new(1, 0, [u1])
                g = new(1, 1, [pgd, pbeta]); std_t[g] = pgd
                m = new(2 if w == s0[v] else 0, 0, [g]); mp[(v, w)] = m; out.append(m)
        else:
            for w in H.succ[v]:
                b = valve(w); x3 = new(0, 0, [b]); x2 = new(0, 0, [x3]); x1 = new(0, 0, [x2]); out.append(x1)
            z = rho0[v]; via = None
            if isinstance(z, tuple): z, via = z
            z = new((H.prio[via] + 6) if (via is not None and copy) else 0, 0, [z])
            for i in range(3): z = new(0, 0, [z])
            z1 = new(1, 0, [z]); out.append(z1); std_t[v] = z1
        succ[v] = out
    top = max(prio)
    if CORE == "high":
        k2 = top + 1 + (top % 2 == 1) ; k2 += (k2 % 2 == 0)
        prio[K[2]], prio[K[1]], prio[K[0]], prio[K[3]] = k2, k2 + 2, k2 + 3, k2 + 4
    else:
        t = top + 2; t += t % 2
        prio[K[0]], prio[K[1]], prio[K[2]], prio[K[3]] = t + 2, 5, 3, t + 3
    inv = {m: w for (v, w), m in mp.items()}
    return pg.Game(prio, own, [sorted(s) for s in succ]), std_s, std_t, mp, inv, valves

def run(H, s0, rho0, cap=200000, gamma=None, copy=True):
    g, std_s, std_t, mp, inv, valves = wrapg(H, s0, rho0, gamma, copy); E, Ed = Engine(g), Engine(n5.dual(g)); n = H.n
    ev = [v for v in range(n) if H.owner[v] == 0]
    sigma, tau = n5x.start_pair(g, E, Ed, None)
    s3ok = all(sigma[v] == mp[(v, s0[v])] for v in ev) and all(sigma[v] == w for v, w in std_s.items()) and all(tau[v] == w for v, w in std_t.items())
    its = fbs = 0; F1 = None; tauch = 0; valvech = 0; hmoves = 0; hsteps = 0
    while its < cap:
        r = n5v.step(g, E, Ed, sigma, tau, ALG)
        if r is None: break
        ns, nt, _, _, fb = r; its += 1; fbs += fb
        if fb and F1 is None: F1 = its
        if F1 is None:
            tauch += int(any(nt[v] != tau[v] for v in std_t)); valvech += int(any(ns[b] != std_s[b] for b in valves))
            mv = sum(1 for v in ev if ns[v] != sigma[v]); hmoves += mv; hsteps += int(mv > 0)
        sigma, tau = ns, nt
    vs, _ = E.evaluate(tuple(sigma)); win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    ok = win == zielonka.solve(g)
    return dict(W=g.n, s3ok=s3ok, its=its, fbs=fbs, F1=F1, tauch=tauch, valvech=valvech, hsteps=hsteps, hmoves=hmoves, ok=ok)

def fam(name, n):
    if name == "lmcs": H, s0 = W.lmcs_game(n, "fig4"); return H, s0
    if name == "fried": r = W.fried_game(n); return r[0], r[1]
    if name == "hn":
        sys.path.insert(0, os.environ["HN"]); import hn
        H, ix = hn.build(n, "fig"); io = hn.iota(n, ix); s0 = [io.get(v, H.succ[v][0]) if H.owner[v] == 0 else -1 for v in range(H.n)]
        assert all(v in io for v in range(H.n) if H.owner[v] == 0 and len(H.succ[v]) > 1); return H, s0

if __name__ == "__main__":
    GF, G3, RE, COPY = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == "1"
    sys.path.insert(0, os.environ["HN"]); import hn
    for n in map(int, sys.argv[5:]):
        H, ix = hn.build(n, "fig"); io = hn.iota(n, ix); s0 = [io.get(v, H.succ[v][0]) if H.owner[v] == 0 else -1 for v in range(H.n)]
        rho0 = {v: H.succ[v][0] for v in range(H.n) if H.owner[v] == 1}; gamma = {}
        for i in range(1, n + 1):
            e, d1, d3, h, f = ix[f"e{i}"], ix[f"d1_{i}"], ix[f"d3_{i}"], ix[f"h{i}"], ix[f"f{i}"]
            rho0[e] = d1 if RE == "d1" else h
            if GF != "e": rho0[f] = (d1 if GF == "d1" else h, e)
            if G3 != "e": gamma[(d3, e)] = d1 if G3 == "d1" else h
        d = run(H, s0, rho0, gamma=gamma, copy=COPY)
        print(f"GSCAN104 alg {ALG} hn GF {GF} G3 {G3} RE {RE} copy {int(COPY)} n {n}: |Wg| {d['W']} S3 standard {d['s3ok']} | iterations {d['its']} fallbacks {d['fbs']} first fallback {d['F1']} | before it: tau changes {d['tauch']} valve moves {d['valvech']} steps with H-moves {d['hsteps']} H-moves {d['hmoves']} | correct {d['ok']}", flush=True)
