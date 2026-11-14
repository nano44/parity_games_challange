#!/usr/bin/env python3
"""L-SI box 104, Addendum A probe: the GUIDED wrapper Wg(H, s0, rho0) and N5 (SPEC) on it. DATA only.
Wg is W(H, s0) of wrap104.py with two changes: (1) the fixed (S3) face of a gate g_(v,w) leads to w itself (pads pg (1), u1, u2 (0)),
not to a flat sink, and the fixed edge of o in V_O leads to rho0(o) (pads z1 (1), z2..z5 (0)); the beta-face of a gate and the other
edges of o pass a valve with an exit to the core, as in W; there is no c_W. (2) CORE=high (default): the core's odd K2 < K1 lie ABOVE
every vertex of H (K2 = the least odd number above max(prio) + 6, K1 = K2 + 2, K0 = K2 + 3, K3 = K2 + 4), so a valve's exit is never
Xi-improving before the core flips; CORE=low keeps K1 = 5, K2 = 3. Every H-edge is a path of 6 edges on either face.
Question: with tau frozen at these faces, S4a is Even's best response to the FIXED Odd strategy rho0 inside the improvement arena;
how long does N5 run on Friedmann's games in this shape?
Printed per game: S3 standard (S3's pair is s0, guide faces, rho0, y at the valves, the core's standard config); iterations,
fallbacks, first fallback; before it: tau changes (iterations at which tau changed), valve moves (iterations at which some valve
left y), steps with H-moves, H-moves; correct (regions = harness Zielonka).
Usage: guide104.py FAMILY RHO n...   FAMILY lmcs (G_n of arXiv 1106.0778v2, Figure 4 priorities, iota) | hn (H_n of its Section 8.4:
L-COMP's hn.py, mode fig, iota; env HN = the directory of hn.py) | fried (PGSolver switchallexp_n, best-reward start);
RHO opt (Odd's optimal counterstrategy to s0 in H) | first | last (first / last successor).  env ALG spec (default) | xi; CORE; LNEW, LRED, LLIT."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wrap104 as W
from wrap104 import pg, n5v, n5, n5x, zielonka
from si import Engine
ALG = os.environ.get("ALG", "spec"); CORE = os.environ.get("CORE", "high")

def wrapg(H, s0, rho0):
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
                b = valve(w); pbeta = new(0, 0, [b]); u2 = new(0, 0, [w]); u1 = new(0, 0, [u2]); pgd = new(1, 0, [u1])
                g = new(1, 1, [pgd, pbeta]); std_t[g] = pgd
                m = new(2 if w == s0[v] else 0, 0, [g]); mp[(v, w)] = m; out.append(m)
        else:
            for w in H.succ[v]:
                b = valve(w); x3 = new(0, 0, [b]); x2 = new(0, 0, [x3]); x1 = new(0, 0, [x2]); out.append(x1)
            z = rho0[v]
            for i in range(4): z = new(0, 0, [z])
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

def run(H, s0, rho0, cap=200000):
    g, std_s, std_t, mp, inv, valves = wrapg(H, s0, rho0); E, Ed = Engine(g), Engine(n5.dual(g)); n = H.n
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
    name, rho = sys.argv[1], sys.argv[2]
    for n in map(int, sys.argv[3:]):
        H, s0 = fam(name, n); s0 = list(s0)
        EH = Engine(H); sH = tuple(s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)); _, cs = EH.evaluate(sH)
        rho0 = {v: (cs[v] if rho == "opt" else H.succ[v][0] if rho == "first" else H.succ[v][-1]) for v in range(H.n) if H.owner[v] == 1}
        T, ties = W.howard(H, s0) if name != "hn" else (None, None)
        d = run(H, s0, rho0)
        print(f"GUIDE104 alg {ALG} core {CORE} {name} rho {rho} n {n}: |H| {H.n} Howard T {T} | |Wg| {d['W']} S3 standard {d['s3ok']} | iterations {d['its']} fallbacks {d['fbs']} first fallback {d['F1']} | before it: tau changes {d['tauch']} valve moves {d['valvech']} steps with H-moves {d['hsteps']} H-moves {d['hmoves']} | correct {d['ok']}", flush=True)
