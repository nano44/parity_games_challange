#!/usr/bin/env python3
"""L-NEW box 179: LP ranking-function search on 2-wide ladders L^R_d (R110 definition), IDEAL step of RESULTS R104 (box150 Gen).
A potential Phi(s) = sum_f w_f f(G, s) over a FEATURE CLASS; constraint Phi(s) - Phi(step(s)) >= 1 on every transition s -> step(s)
(s != step(s)) of every sampled genome G and EVERY state s (all starts), 0 <= Phi <= Mx; minimise Mx. If the decrease constraints are
infeasible, a Farkas certificate (lambda >= 0, sum 1, sum lambda_i (f(s_i) - f(s_i')) = 0) is computed and its support printed.
Usage: lpot.py CLASS d ngen seed [allstates|start] [genome files: those in L^R_d are added first]"""
import os, sys, json, random, itertools
import numpy as np
from scipy.optimize import linprog
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
rand_lr = fl["rand_lr"]

def xheight(G):
    N = G["N"]; h = {}
    def hh(v):
        if v < 0: return 0
        if v not in h: h[v] = 1 + max(hh(o[1]) for o in G["opts"][v])
        return h[v]
    return [hh(v) for v in range(N)]

def base(g, G, s):
    """per mover: z (other option strictly Xi-better), k (current != KP), u = z and k (moves); per level >= 1: c, b bits"""
    N = G["N"]; K = g.keys(s); z, k = [], []
    for x in range(N):
        cur, oth = s[x], 1 - s[x]
        z.append(int(g.face(s, x, oth) > g.face(s, x, cur)))
        kp = min((0, 1), key=lambda j: g.optkey(K, x, j)); k.append(int(cur != kp))
    return z, k, K

PV = {}
def pathvals(g, G, x):
    """sorted list of the integer values (ENC) of all maximal Xi-paths from mover x (choose an option at every mover on the way)"""
    key = (id(G), x)
    if key not in PV:
        def vals(v):
            out = set()
            for k in range(len(G["opts"][v])):
                e = g.eps(v, k); xt = G["opts"][v][k][1]
                if xt < 0: out.add(e)
                else: out |= {e + w for w in vals(xt)}
            return out
        PV[key] = sorted(vals(x))
    return PV[key]

def feats(cls, g, G, s, hx):
    N = G["N"]; d = N // 2; z, k, K = base(g, G, s); F = {}
    if "D" in cls:  # non-local: unstable (u = 1) Xi-descendants on the chain of the other / current option of x, per level of x
        u = [z[y] & k[y] for y in range(N)]
        for x in range(N):
            for tag, j in (("o", 1 - s[x]), ("c", s[x])):
                F["D%s%d" % (tag, x)] = sum(u[y] for y in g.play(s, x, j))
    if "V" in cls:  # value-rank of the current chain value cv(x) among x's path values (MONO: never decreases)
        for x in range(N):
            pv = pathvals(g, G, x); i = pv.index(g.face(s, x, s[x]))
            F["vi%d" % x] = i; F["vr%d" % x] = i / max(1, len(pv) - 1)
    for x in range(N):
        l = x // 2
        F["z%d" % x] = z[x]; F["k%d" % x] = k[x]; F["u%d" % x] = z[x] & k[x]
        if "H" in cls:  # Xi-height indexed copies (genome-dependent role)
            F["zH%d_%d" % (l, hx[x])] = F.get("zH%d_%d" % (l, hx[x]), 0) + z[x]
            F["uH%d_%d" % (l, hx[x])] = F.get("uH%d_%d" % (l, hx[x]), 0) + (z[x] & k[x])
    for l in range(d):
        p, q = 2 * l, 2 * l + 1
        if "P" in cls:  # pair automaton state: (k_p, k_q, z_p, z_q) one-hot + ord bit
            F["pair%d_%d%d%d%d" % (l, k[p], k[q], z[p], z[q])] = 1
            F["ord%d" % l] = int(K[p] < K[q])
        if "X" in cls and l + 1 < d:  # cross-level products: unstable here x key-misaligned above
            for a in (p, q):
                for b in (2 * l + 2, 2 * l + 3):
                    F["zk%d_%d" % (a, b)] = z[a] * k[b]; F["kz%d_%d" % (a, b)] = k[a] * z[b]
    return F

def main():
    cls, d, ngen, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    mode = sys.argv[5] if len(sys.argv) > 5 else "allstates"
    rng = random.Random(seed); idx = {}; rows_dec, rows_val, meta = [], [], []
    def vec(F):
        for nm in F:
            if nm not in idx: idx[nm] = len(idx)
        return F
    nontriv = 0; Tmax = 0
    files = [f for f in sys.argv[6:]]
    gens = []; files_used = []
    for f in files:
        try: G = json.load(open(f))
        except Exception: continue
        if isinstance(G, dict) and G.get("N") == 2 * d and fl["is_lr"](G): gens.append(G); files_used.append(f)
    nfile = len(gens); gens += [rand_lr(d, rng, iso=False) for _ in range(ngen)]
    print("corpus files at d %d: %d" % (d, nfile))
    for gi, G in enumerate(gens):
        g = Gen(G); hx = xheight(G)
        states = itertools.product((0, 1), repeat=2 * d) if mode == "allstates" else [tuple(G["start"])]
        for s in states:
            s = tuple(s); n, _ = g.step(s)
            Fs = vec(feats(cls, g, G, s, hx)); rows_val.append(Fs)
            if n is None: continue
            Fn = vec(feats(cls, g, G, n, hx)); nontriv += 1
            rows_dec.append((Fs, Fn)); meta.append((gi, s, n))
    m = len(idx) + 1  # + constant
    def dense(F):
        v = np.zeros(m); v[-1] = 1
        for nm, x in F.items(): v[idx[nm]] += x
        return v
    D = np.array([dense(a) - dense(b) for a, b in rows_dec]) if rows_dec else np.zeros((0, m))
    V = np.array([dense(a) for a in rows_val])
    D, Dinv = np.unique(D, axis=0, return_inverse=True); V = np.unique(V, axis=0)
    print("class %s d %d genomes %d transitions %d distinct-dec-rows %d distinct-states %d features %d" % (cls, d, ngen, nontriv, len(D), len(V), m - 1))
    # variables: w (m), Mx ; minimise Mx
    nv = m + 1; c = np.zeros(nv); c[-1] = 1
    A = np.vstack([np.hstack([-D, np.zeros((len(D), 1))]),            # -(w.D) <= -1
                   np.hstack([-V, np.zeros((len(V), 1))]),            # -(w.f) <= 0
                   np.hstack([V, -np.ones((len(V), 1))])])            # w.f - Mx <= 0
    b = np.concatenate([-np.ones(len(D)), np.zeros(len(V)), np.zeros(len(V))])
    r = linprog(c, A_ub=A, b_ub=b, bounds=[(None, None)] * nv, method="highs")
    if r.status == 0:
        w = r.x[:m]; names = sorted(idx, key=idx.get)
        print("FEASIBLE min max Phi = %.4f" % r.x[-1])
        big = sorted(((abs(w[i]), names[i], w[i]) for i in range(m - 1)), reverse=True)[:40]
        print("weights:", " ".join("%s=%.3g" % (nm, x) for _, nm, x in big if abs(x) > 1e-9), "const=%.3g" % w[-1])
        json.dump({"names": names, "w": list(w)}, open(os.path.join(H, "out", "w_%s_d%d.json" % (cls, d)), "w"))
        # dual certificate of the lower bound: marginals of the decrease rows and of the range rows
        y = -r.ineqlin.marginals; nd = len(D)
        inv = {}
        for j, ii in enumerate(Dinv.ravel()): inv.setdefault(int(ii), j)
        sup = [i for i in range(nd) if y[i] > 1e-9]
        src = {}
        for i in sup:
            gi = meta[inv[i]][0]; tag = files_used[gi] if gi < nfile else "rand"
            src[tag] = src.get(tag, 0) + y[i]
        names_ = sorted(idx, key=idx.get); dump = []
        for i in sup:
            gi, s0, n0 = meta[inv[i]]
            dump.append({"y": y[i], "src": files_used[gi] if gi < nfile else "rand", "genome": gens[gi], "s": s0, "next": n0,
                         "fdiff": {names_[j]: D[i, j] for j in range(m - 1) if abs(D[i, j]) > 1e-12}})
        json.dump(dump, open(os.path.join(H, "out", "dual_%s_d%d_s%d.json" % (cls, d, seed)), "w"), default=float)
        print("dual: %d decrease rows in support, sum of their multipliers %.4f (= the bound)" % (len(sup), sum(y[i] for i in sup)))
        print("dual mass by genome source:", " ".join("%s:%.3g" % (os.path.basename(k), v) for k, v in sorted(src.items(), key=lambda kv: -kv[1])[:12]))
        return
    print("LP status", r.status, r.message)
    # Farkas: lambda >= 0 over distinct dec rows (features only, constant cancels), sum lambda = 1, sum lambda D = 0; minimise support via L1 (sum)
    Df = D[:, :m - 1]
    r2 = linprog(np.ones(len(D)), A_eq=np.vstack([Df.T, np.ones((1, len(D)))]), b_eq=np.concatenate([np.zeros(m - 1), [1]]),
                 bounds=[(0, None)] * len(D), method="highs")
    if r2.status != 0: print("no Farkas certificate found:", r2.message); return
    lam = r2.x; sup = [i for i in range(len(D)) if lam[i] > 1e-9]
    print("INFEASIBLE: Farkas certificate on %d distinct transition rows" % len(sup))
    inv = {}
    for j, ii in enumerate(Dinv.ravel()): inv.setdefault(int(ii), j)
    names = sorted(idx, key=idx.get); cert = []
    for i in sup:
        gi, s, n = meta[inv[i]]
        diff = {names[j]: D[i, j] for j in range(m - 1) if abs(D[i, j]) > 1e-12}
        cert.append({"lambda": lam[i], "genome": gi, "s": s, "next": n, "fdiff": diff})
        print("  lambda %.4f genome %d s %s -> %s  f(s)-f(s') %s" % (lam[i], gi, "".join(map(str, s)), "".join(map(str, n)), diff))
    json.dump({"cls": cls, "d": d, "seed": seed, "ngen": ngen, "cert": cert}, open(os.path.join(H, "out", "farkas_%s_d%d_s%d.json" % (cls, d, seed)), "w"), default=float)

if __name__ == "__main__": main()
