#!/usr/bin/env python3
"""L-RED 58 R223 item 2: DATA for extensions of Lemma FLIP (docs/red/R222-lockup.md §4) on own.py runs (IDEAL-CYC, Howard best switch,
ties keep). Unit: (mover B, option o of B, Lambda-interval I) with I a maximal interval on which NO vertex changes its cycle node.
Classes: typ = SETe / SETo (Xi-target B itself, beta parity even / odd) / NS (non-SET); lam = class of Lambda(B) on I: K12, bo (= b_o),
beta (another beta), cX, other. flips = #consecutive pairs of I where [sigma(B) = o] changes.
Vertex set Wset(o) = {w_o (successor of e_o)} + {b_o's successor if it is not B} + {g_o' : o' != o}.
  boundE = 1 + sum_{v in Wset} (D_E,I(v) - 1)   (FLIP's bound; D_E = #distinct e-sets of v on I)
  boundP = 1 + sum_{v in Wset} (D_P,I(v) - 1)   (D_P = #distinct full (Pi, length) of v on I)
Item (c): a switch of B at t (sigma_t(B) != sigma_(t+1)(B)) is E-DECIDED if the new and old options' values at t differ in cycle node
or e-set, else P-DECIDED (beta part or length decides). Counted per genome: psw.
Usage: flip223.py rand|ret SEED COUNT [OUTDIR] | flip223.py G.json ..."""
import sys, os, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [here, os.path.join(here, "../r222"), os.path.join(here, "../r221q")]
import own
def check(G):
    out, V, O, ow = own.run(G); n, prio, own_, succ, _, _ = own.build(G); N = G["N"]; vj = own.VJ(prio)
    evs = {V[("e", q)] for q in O}; K12 = {V["K1"], V["K2"]}; cX = V["cX"]; bset = {V[("b", q)]: q for q in O}
    cuts = [0] + [t for t in range(1, len(out)) if any(out[t - 1][1][v][0] != out[t][1][v][0] for v in range(n))] + [len(out)]
    units = collections.Counter(); viE = collections.Counter(); viP = collections.Counter(); mx = collections.Counter(); ex = {}
    for a, b in zip(cuts, cuts[1:]):
        for x in range(N):
            lam = out[a][1][x][0]
            for k, (wt, xt, bi) in enumerate(G["opts"][x]):
                q = (x, k); go = V[("g", q)]; bo = V[("b", q)]; eo = V[("e", q)]
                typ = ("SETo" if G["bp"][bi] % 2 else "SETe") if xt == x else "NS"
                lc = "K12" if lam in K12 else "bo" if lam == bo else "beta" if lam in bset else "cX" if lam == cX else "other"
                W = [succ[eo][0]] + [s for s in succ[bo] if s != x] + [V[("g", (x, j))] for j in range(len(G["opts"][x])) if j != k]
                flips = sum((out[t - 1][0][x] == go) != (out[t][0][x] == go) for t in range(a + 1, b))
                DE = lambda v: len({frozenset(u for u in out[t][1][v][1] if u in evs) for t in range(a, b)})
                DP = lambda v: len({(out[t][1][v][1], out[t][1][v][2]) for t in range(a, b)})
                bE = 1 + sum(DE(v) - 1 for v in W); bP = 1 + sum(DP(v) - 1 for v in W)
                key = (typ, lc); units[key] += 1; mx[key] = max(mx[key], flips)
                if flips > bE: viE[key] += 1; ex.setdefault(("E",) + key, (x, k, a, b, flips, bE))
                if flips > bP: viP[key] += 1; ex.setdefault(("P",) + key, (x, k, a, b, flips, bP))
    psw = esw = 0
    for t in range(len(out) - 1):
        for x in range(N):
            o1, o2 = out[t][0][x], out[t + 1][0][x]
            if o1 == o2: continue
            v1, v2 = out[t][1][o1], out[t][1][o2]
            if v1[0] != v2[0] or {u for u in v1[1] if u in evs} != {u for u in v2[1] if u in evs}: esw += 1
            else: psw += 1
    return dict(units=units, viE=viE, viP=viP, mx=mx, ex=ex, psw=psw, esw=esw, T=len(out) - 1)
if __name__ == "__main__":
    from priv222 import rgen_ret
    from brute221 import rgen
    if sys.argv[1] in ("rand", "ret"):
        fam, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); od = sys.argv[4] if len(sys.argv) > 4 else "."
        rng = random.Random(seed); U, VE, VP, MX = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
        PS = ES = 0; maxT = 0; saved = set()
        for i in range(cnt):
            if fam == "ret": G = rgen_ret(rng)
            else: d = rng.randint(1, 4); w = rng.randint(1, 4); G = rgen(rng, d, w, rng.choice([2, 3]))
            r = check(G); U += r["units"]; VE += r["viE"]; VP += r["viP"]; PS += r["psw"]; ES += r["esw"]; maxT = max(maxT, r["T"])
            for k, v in r["mx"].items(): MX[k] = max(MX[k], v)
            for k, e in r["ex"].items():
                if k not in saved:
                    saved.add(k); fn = os.path.join(od, f"flip223_{k[0]}_{k[1]}_{k[2]}_{fam}_{seed}_{i}.json"); json.dump(G, open(fn, "w"))
                    print("VIOL", k, e, os.path.basename(fn), flush=True)
        print(f"FLIP223 {fam} seed {seed} genomes {cnt} maxT {maxT} switches E-decided {ES} P-decided {PS}", flush=True)
        for k in sorted(U): print(f"  {k[0]:5s} {k[1]:6s} units {U[k]:6d} maxflips {MX[k]:3d} violE {VE[k]:5d} violP {VP[k]:5d}", flush=True)
    else:
        for fn in sys.argv[1:]:
            r = check(json.load(open(fn))); print(os.path.basename(fn), "T", r["T"], "psw", r["psw"], "esw", r["esw"], dict(r["viE"]), dict(r["viP"]), r["ex"])
