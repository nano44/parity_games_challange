#!/usr/bin/env python3
"""REFEREE-2 succ. 29: own check of P-N5-REACH (l-new 73b3d1fd). No L-NEW code (no box21/n5x, no box189/*).
Uses REFEREE-2's own R2-N5-REALIZE/realize_check.py (my lane's Gamma(G) builder from R104's packet §3.1, my IDEAL run, and the SPEC
S1-S5 state loop on the fleet reference si.py Engine), plus, written here from P-N5-REACH §3 / §9 / SPEC S3 + FIX 1:
  pad3(G)   Gamma3(G) (pads appended in the order pA, s, q, r, pe, pbeta, pb, m)      s3(g)  SPEC S3 / FIX 1 start
For each genome: NO-REACH run on Gamma from S3 (every state: sigma(K0) = K1, sigma(K1) = K0; iterations), REACH3 run on Gamma3 from S3:
states 0..L projected to the movers = the IDEAL states, transitions 1..L FL (no fallback, tau kept, sigma changed, W = play value of
(sigma, tau) kept at every vertex), transition L+1 a fallback; W at movers = (c_W, 0, 5 lev + 5).
Control: CTRL=mprio0 gives every mover pad Omega 0 (S3 no longer picks the genome start: S3START / REACH3 must fail).
Usage: r2reach.py GENOME.json [PIN_PREFIX]...   |   subdiv"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-REALIZE"))
import realize_check as R
pg, Engine, dual = R.pg, R.Engine, R.dual

def s3(g):
    """SPEC S3 / FIX 1: Even: max (r(w), w if r(w) even else -w), r = Omega if even else -Omega; Odd: the same rule on G^d (Omega + 1)."""
    sig = [-1] * g.n; tau = [-1] * g.n
    for v in range(g.n):
        d = 0 if g.owner[v] == 0 else 1
        def key(w):
            o = g.prio[w] + d; r = o if o % 2 == 0 else -o
            return (r, w if r % 2 == 0 else -w)
        b = max(g.succ[v], key=key)
        if g.owner[v] == 0: sig[v] = b
        else: tau[v] = b
    return sig, tau

def pad3(G):
    g, sig, tau, m = R.build(G, esc=True)
    n0 = g.n; prio, own, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    faces, gv, bv, ev, K = m["faces"], m["gv"], m["bv"], m["ev"], m["K"]; K0, K1, K2, K3 = K
    newv = []
    def pad(a, b, om):
        p = len(prio); prio.append(om); own.append(0); succ.append([b])
        succ[a] = sorted(p if w == b else w for w in succ[a]); newv.append(p); return p
    bygate = sorted(faces, key=lambda f: G["gate"][f[0]][f[1]])
    P = {}
    P["pA"] = pad(K0, K3, 0); P["s"] = pad(K1, K1, 0); P["q"] = pad(K1, K0, 1); P["r"] = pad(K2, K1, 0)
    for f in bygate: P[("pe", f)] = pad(gv[f], ev[f], 1)
    for f in bygate: P[("pb_", f)] = pad(gv[f], bv[f], 0)          # pbeta
    for f in faces: P[("pu", f)] = pad(bv[f], K0, 1)                # pb (escape)
    for f in bygate: P[("m", f)] = pad(f[0], gv[f], 0 if os.environ.get("CTRL") == "mprio0" else (2 if f[1] == G["start"][f[0]] else 0))
    g3 = pg.Game(prio, own, succ)
    return g3, dict(m, P=P, n0=n0)

def std3(G, M3, s):
    """standard state of Gamma3 for mover state s (packet §3)"""
    g3 = M3["g3"]; P = M3["P"]; K0, K1, K2, K3 = M3["K"]; sig = [-1] * g3.n; tau = [-1] * g3.n
    for v in range(g3.n):
        if g3.owner[v] == 0: sig[v] = g3.succ[v][0]
        else: tau[v] = g3.succ[v][0]
    for f in M3["faces"]:
        xt = G["opts"][f[0]][f[1]][1]
        sig[M3["bv"][f]] = xt if xt >= 0 else P[("pu", f)]
        tau[M3["gv"][f]] = P[("pe", f)]
    for x in range(G["N"]): sig[x] = P[("m", (x, s[x]))]
    sig[K0], sig[K1], sig[K3] = P["pA"], P["s"], K2; tau[K2] = K2
    return sig, tau

def W(g, E, sg, tu):
    nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(g.n)]
    return [R.pval(E, nx, v)[0] for v in range(g.n)]

def runloop(g, sg, tu, cap=400):
    E = Engine(g); Ed = Engine(dual(g)); states = [(list(sg), list(tu))]; infos = []
    while len(infos) < cap:
        nxt, info = step(g, E, Ed, *states[-1]); infos.append(info)
        if nxt is None: break
        states.append((list(nxt[0]), list(nxt[1])))
    return E, states, infos

step = R.step

def genome(path, pin=None):
    G = json.load(open(path)); name = os.path.basename(path)
    ist, _, why = R.ideal_run(G); L = len(ist) - 1
    out = {"name": name, "L": L, "why": why}
    # NO-REACH on Gamma from S3
    g0, _, _, m0 = R.build(G, esc=True); K0, K1, K2, K3 = m0["K"]
    sg, tu = s3(g0); E0, st0, inf0 = runloop(g0, sg, tu)
    out["NOREACH_iters"] = len(st0) - 1
    out["NOREACH_core_ok"] = all(s[K0] == K1 and s[K1] == K0 for s, _ in st0)
    out["NOREACH_noKimpr"] = all(not any(v in (K0, K1) for v, _ in i["Is"]) for i in inf0)
    # Gamma3
    g3, M3 = pad3(G); M3["g3"] = g3; n3 = g3.n; M = M3["M"]; N = G["N"]
    out["n3"] = n3; out["n3_formula"] = N + 7 * M + 10
    if pin:
        pgt, stt = R.dumps(g3, *s3(g3))
        out["PIN_pg_equal"] = open(pin + ".pg").read() == pgt
        out["PIN_start_equal"] = open(pin + ".start").read() == stt
    sg, tu = s3(g3); sd, td = std3(G, M3, ist[0])
    out["S3START_eq_std"] = (sg == sd and tu == td)
    E, st, inf = runloop(g3, sg, tu, cap=L + 50)
    fails = []; Ws = []
    for j in range(min(L + 1, len(st))):
        a, b = std3(G, M3, ist[j])
        if st[j] != (a, b): fails.append(("notstd", j))
        Ws.append(W(g3, E, *st[j]))
    for j in range(1, L + 1):
        if j >= len(st): fails.append(("short", j)); break
        i = inf[j - 1]
        if i.get("fb", 1) or st[j][1] != st[j - 1][1] or st[j][0] == st[j - 1][0] or Ws[j] != Ws[j - 1]: fails.append(("notFL", j))
    if len(inf) <= L or not inf[L].get("fb", 0): fails.append(("noFB", L + 1))
    # W at movers
    for x in range(N):
        c, P_, l = Ws[0][x]
        if not (c == M3["cW"] and P_ == 0 and l == 5 * G["lev"][x] + 5): fails.append(("W", x)); break
    out["REACH3_fails"] = fails[:5]; out["REACH3_nfails"] = len(fails)
    out["iters3"] = len(st) - 1; out["fallbacks3"] = sum(i.get("fb", 0) for i in inf)
    # FL run lengths: maximal runs of non-fallback transitions keeping tau, changing sigma, keeping W
    fl = []; cur = 0; Wprev = Ws[0] if Ws else None
    allW = [W(g3, E, *x) for x in st]
    for j in range(1, len(st)):
        i = inf[j - 1]; ok = (not i.get("fb", 1)) and st[j][1] == st[j - 1][1] and st[j][0] != st[j - 1][0] and allW[j] == allW[j - 1]
        if ok: cur += 1
        else:
            if cur: fl.append(cur)
            cur = 0
    if cur: fl.append(cur)
    out["FL_runs"] = fl
    print(json.dumps(out))

def subdiv():
    """§9 instances A, B: G^pad = every priority + 4, EVERY edge (a, b) subdivided by an Even pad (indices n, n+1, ... in (a, b) order;
    Omega(p) = 2 if a Even and b = sigma0(a), 1 if a Odd and b = tau0(a), 0 otherwise). Compare N5 of G from (sigma0, tau0) with N5 of
    G^pad from S3."""
    inst = {"A": ([3, 3, 1], [1, 0, 1], [[1], [0, 1, 2], [0]], {1: 1}, {0: 1, 2: 0}),
            "B": ([3, 2, 4, 0, 0], [1, 1, 0, 1, 0], [[1, 3, 4], [2, 3], [3, 4], [0, 2, 3], [1, 4]], {2: 4, 4: 1}, {0: 4, 1: 2, 3: 2})}
    for nm, (pr, ow, sc, s0, t0) in inst.items():
        g = pg.Game(pr, ow, sc); n = g.n
        sg = [s0.get(v, sc[v][0]) if ow[v] == 0 else -1 for v in range(n)]; tu = [t0.get(v, sc[v][0]) if ow[v] == 1 else -1 for v in range(n)]
        _, st, inf = runloop(g, sg, tu)
        edges = [(a, b) for a in range(n) for b in sc[a]]
        prio = [p + 4 for p in pr]; own = list(ow); succ = [[] for _ in range(n)]; pid = {}
        for (a, b) in edges:
            p = len(prio); pid[(a, b)] = p
            prio.append(2 if (ow[a] == 0 and sg[a] == b) else 1 if (ow[a] == 1 and tu[a] == b) else 0); own.append(0); succ.append([b])
            succ[a].append(p)
        gp = pg.Game(prio, own, [sorted(s) for s in succ])
        sp, tp = s3(gp)
        trans = all(sp[a] == pid[(a, sg[a])] for a in range(n) if ow[a] == 0) and all(tp[a] == pid[(a, tu[a])] for a in range(n) if ow[a] == 1)
        _, stp, infp = runloop(gp, sp, tp)
        def projs(S):  # back to G: sigma(a) = b if a -> pad(a, b)
            inv = {p: b for (a, b), p in pid.items()}
            return [[inv[x[0][a]] if ow[a] == 0 else -1 for a in range(n)] + [inv[x[1][a]] if ow[a] == 1 else -1 for a in range(n)] for x in S]
        print("SUBDIV %s n %d: G from (s0,t0) iterations %d fallbacks %d | G^pad n %d from S3: iterations %d fallbacks %d | S3 = transported %s | projected states equal %s"
              % (nm, n, len(st) - 1, sum(i.get("fb", 0) for i in inf), gp.n, len(stp) - 1, sum(i.get("fb", 0) for i in infp), trans,
                 projs(stp) == [[x[0][a] if ow[a] == 0 else -1 for a in range(n)] + [x[1][a] if ow[a] == 1 else -1 for a in range(n)] for x in st]))

if __name__ == "__main__":
    if sys.argv[1] == "subdiv": subdiv()
    else:
        a = sys.argv[1:]
        genome(a[0], a[1] if len(a) > 1 else None)
