#!/usr/bin/env python3
"""L-RED 57 R222: data check of Lemma PRIV-FLIP (docs/red/R222-lockup.md §3) on own.py runs (IDEAL-CYC, Howard best switch).
Unit: (mover B, SET-type option S = (w, Xi-target B, even beta), Lambda-interval I with Lambda(B) in {K1, K2}).
PRIV(I): at every state of I, no play from w (the successor of e_S) and none from a gate g_o (o != S) of B passes B.
flips = #consecutive state pairs in I where [sigma(B) = S] changes; bound = 1 + sum over v in {w} + {g_o} of (D_E,I(v) - 1).
Prints per genome: units, PRIV units, violations (PRIV and flips > bound), max flips with PRIV, max flips without PRIV.
Usage: priv222.py rand SEED COUNT   (R221 brute221.rgen genomes, d 1-4, width 1-4, degree 2-3)  |  priv222.py G.json ..."""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def check(G):
    out, V, O, ow = own.run(G); n, prio, own_, succ, _, _ = own.build(G); N = G["N"]
    evs = {V[("e", q)] for q in O}; K12 = {V["K1"], V["K2"]}
    def f_of(sig, tau):
        f = [None] * n
        for v in range(n):
            if own_[v] == 1: f[v] = tau[v]
            elif len(succ[v]) == 1: f[v] = succ[v][0]
        for x in range(N): f[V[("x", x)]] = sig[x]
        return f
    def passes(f, v, tgt):
        seen = set()
        while v not in seen:
            if v == tgt: return True
            seen.add(v); v = f[v]
        return False
    # Lambda-intervals
    cuts = [0] + [t for t in range(1, len(out)) if any(out[t - 1][1][v][0] != out[t][1][v][0] for v in range(n))] + [len(out)]
    res = {"units": 0, "priv": 0, "viol": [], "maxpriv": 0, "maxnopriv": 0, "nopriv_examples": []}
    fs = [f_of(s, tau) for (s, _, tau) in out]
    for a, b in zip(cuts, cuts[1:]):
        for x in range(N):
            xv = V[("x", x)]
            if out[a][1][xv][0] not in K12: continue
            for k, (wt, xt, bi) in enumerate(G["opts"][x]):
                if xt != x or G["bp"][bi] % 2: continue
                gS = V[("g", (x, k))]; eS = V[("e", (x, k))]; w = succ[eS][0]
                gates = [V[("g", (x, j))] for j in range(len(G["opts"][x])) if j != k]
                priv = all(not passes(fs[t], v, xv) for t in range(a, b) for v in [w] + gates)
                flips = sum((out[t - 1][0][x] == gS) != (out[t][0][x] == gS) for t in range(a + 1, b))
                D = lambda v: len({frozenset(u for u in out[t][1][v][1] if u in evs) for t in range(a, b)})
                bound = 1 + sum(D(v) - 1 for v in [w] + gates)
                res["units"] += 1
                if priv:
                    res["priv"] += 1; res["maxpriv"] = max(res["maxpriv"], flips)
                    if flips > bound: res["viol"].append((x, k, a, b, flips, bound))
                else:
                    if flips > res["maxnopriv"]: res["nopriv_examples"] = [(x, k, a, b, flips, bound)]
                    res["maxnopriv"] = max(res["maxnopriv"], flips)
    res["T"] = len(out) - 1; res["C"] = len(cuts) - 2
    return res
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../r221q"))
        from brute221 import rgen
        rng = random.Random(int(sys.argv[2])); tot = {"units": 0, "priv": 0, "viol": 0, "maxpriv": 0, "maxnopriv": 0, "genomes": 0}
        for i in range(int(sys.argv[3])):
            d = rng.randint(1, 4); w = rng.randint(1, 4); G = rgen(rng, d, w, rng.choice([2, 3]))
            r = check(G); tot["genomes"] += 1
            for kk in ("units", "priv"): tot[kk] += r[kk]
            tot["viol"] += len(r["viol"]); tot["maxpriv"] = max(tot["maxpriv"], r["maxpriv"]); tot["maxnopriv"] = max(tot["maxnopriv"], r["maxnopriv"])
            if r["viol"]: json.dump(G, open(f"out/priv_viol_{sys.argv[2]}_{i}.json", "w")); print("VIOL", i, r["viol"], flush=True)
            if r["maxnopriv"] >= 3: json.dump(G, open(f"out/priv_np_{sys.argv[2]}_{i}.json", "w")); print("NOPRIV", i, r["nopriv_examples"], flush=True)
        print("PRIV222 rand seed", sys.argv[2], tot, flush=True)
    else:
        for fn in sys.argv[1:]:
            r = check(json.load(open(fn)))
            print(f"PRIV222 {os.path.basename(fn)} T {r['T']} C {r['C']} units {r['units']} priv {r['priv']} viol {len(r['viol'])} maxpriv {r['maxpriv']} maxnopriv {r['maxnopriv']} {r['viol'][:3]} {r['nopriv_examples']}")
