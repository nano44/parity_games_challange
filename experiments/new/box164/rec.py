#!/usr/bin/env python3
"""L-NEW box 164: encoding-method records on IDEAL-ACYC runs (RESULTS R104 model; simulator = box150/check.py Gen).
For every step t and every mover x in Mv_t, the record of the move is (x, rho) with rho one of:
  A  : the decisive beta of the A-set comparison  Xi_{s_(t-1)}(x, s_t(x))  vs  Xi_{s_(t-1)}(x, s_(t-1)(x))  (old state)
  V  : the decisive beta of the value change       V_{s_t}(x)              vs  V_{s_(t-1)}(x)
(decisive beta = the beta of largest rank in the symmetric difference of the two beta-sets).
Prints per run: T, #moves, max multiplicity of a record (A and V), and the first repeated record.
Usage: rec.py file.json ...   |  rec.py rand d count seed"""
import os, sys, json, random, glob
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
F = os.path.join(H, "..", "box162", "flipcheck.py")
fns = {"__file__": F, "__name__": "lib"}; exec(open(F).read().split("\nif __name__")[0], fns); rand_lr = fns["rand_lr"]

def chain(g, st, v, k):
    out = []
    while True:
        out.append(g.opts[v][k][2]); xt = g.opts[v][k][1]
        if xt < 0: return frozenset(out)
        v, k = xt, st[xt]

def decisive(g, P, Q):
    D = P ^ Q
    return max(D, key=lambda m: g.br[m]) if D else None

def records(G, start=None):
    g = Gen(G); S, _ = g.run(start if start is not None else G["start"])
    recA, recV, moves = {}, {}, 0
    firstA = firstV = None
    for t in range(1, len(S)):
        a, b = S[t - 1], S[t]
        for x in range(g.N):
            if a[x] == b[x]: continue
            moves += 1
            rA = (x, decisive(g, chain(g, a, x, b[x]), chain(g, a, x, a[x])))
            rV = (x, decisive(g, chain(g, b, x, b[x]), chain(g, a, x, a[x])))
            recA.setdefault(rA, []).append(t); recV.setdefault(rV, []).append(t)
            if firstA is None and len(recA[rA]) > 1: firstA = (rA, recA[rA][:])
            if firstV is None and len(recV[rV]) > 1: firstV = (rV, recV[rV][:])
    mA = max((len(v) for v in recA.values()), default=0); mV = max((len(v) for v in recV.values()), default=0)
    return dict(T=len(S) - 1, moves=moves, multA=mA, multV=mV, nrecA=len(recA), nrecV=len(recV), firstA=firstA, firstV=firstV,
                N=g.N, M=sum(len(o) for o in g.opts))

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        d, cnt, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        best = {"multA": 0, "multV": 0}; T = 0; hist = {}
        for i in range(cnt):
            G = rand_lr(d, rng, iso=(i % 2 == 0)); r = records(G); T = max(T, r["T"])
            for k in ("multA", "multV"):
                hist[(k, r[k])] = hist.get((k, r[k]), 0) + 1
                if r[k] > best[k]: best[k] = r[k]; json.dump(G, open(os.path.join(H, "out", "rand_%s_d%d_m%d.json" % (k, d, r[k])), "w"))
        print("RAND d %d count %d maxT %d maxmultA %d maxmultV %d" % (d, cnt, T, best["multA"], best["multV"]))
        print("  hist", sorted(hist.items()))
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); r = records(G)
            print("%-28s N %d T %2d moves %2d multA %d multV %d nrecA %d nrecV %d firstA %s firstV %s" % (os.path.basename(f), r["N"],
                  r["T"], r["moves"], r["multA"], r["multV"], r["nrecA"], r["nrecV"], r["firstA"], r["firstV"]))
