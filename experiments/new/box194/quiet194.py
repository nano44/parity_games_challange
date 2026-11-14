#!/usr/bin/env python3
"""Box 194: Theorem QUIET data. class_t(v) := (Lambda_t(v), e-part of Pi_t(v)). A step t -> t+1 is LOUD if some vertex changes class,
else QUIET. A quiet window = a maximal run of consecutive quiet steps. Per run: T, Q (loud steps), W (longest quiet window, in steps),
the bound L = (M+1)(2M+1)(N+1) + N(n-1) of Theorem QUIET, wfail (quiet WINDOWS longer than L, each counted once), Tfail (T > Q + (Q+1)L);
crossflip: sigma-bar flips at a gate on a quiet step whose two faces are in different classes at both states (QUIET's proof: 0);
DEtot: max over vertices of the number of distinct classes; sumDE: sum over vertices of (distinct classes - 1) >= Q.
Usage: quiet194.py FILES.json | rand COUNT SEED | climb d w D seed iters OUT.json (hill-climb W, then W/N; box191 climb191.mut). Imports relative to this file."""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); B191 = os.path.join(HERE, "..", "box191"); B192 = os.path.join(HERE, "..", "box192")
sys.path[:0] = [B192, B191]
import rpot192, rand191

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    ES = 0
    for v in range(h.n):
        if name[v][0] == "e": ES |= 1 << E.rank[v]
    N = G["N"]; M = sum(len(o) for o in G["opts"]); n = h.n; T = len(ev) - 1
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    cls = [[(vs[v][0], vs[v][1] & ES) for v in range(n)] for vs, sb in ev]
    gates = [(v, name[v][1]) for v in range(n) if h.owner[v] == 1 and name[v][0] == "g"]
    r = dict(N=N, M=M, n=n, T=T, Q=0, W=0, L=L, wfail=0, Tfail=0, crossflip=0, DEtot=0, sumDE=0)
    cur = 0
    for t in range(1, T + 1):
        if cls[t] != cls[t - 1]:
            r["Q"] += 1; cur = 0; continue
        cur += 1; r["W"] = max(r["W"], cur)
        if cur == L + 1: r["wfail"] += 1                      # once per window (P-N5-QUIET fixes entry 2, D-1)
        for g, q in gates:
            if ev[t][1][g] != ev[t - 1][1][g]:
                e, b = V[("e", q)], V[("b", q)]
                if cls[t][e] != cls[t][b] and cls[t - 1][e] != cls[t - 1][b]: r["crossflip"] += 1
    for v in range(n):
        d = len({cls[t][v] for t in range(T + 1)}); r["DEtot"] = max(r["DEtot"], d); r["sumDE"] += d - 1
    if T > r["Q"] + (r["Q"] + 1) * L: r["Tfail"] = 1
    return r

def fmt(r): return " ".join(f"{k} {v}" for k, v in r.items())

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = {}
        for i in range(cnt):
            a = analyse(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)))
            for k in ("wfail", "Tfail", "crossflip"): tot[k] = tot.get(k, 0) + a[k]
            tot["maxW"] = max(tot.get("maxW", 0), a["W"]); tot["maxT"] = max(tot.get("maxT", 0), a["T"])
            tot["maxWoverN"] = max(tot.get("maxWoverN", 0), round(a["W"] / a["N"], 3))
        print(f"rand count {cnt} seed {seed}:", fmt(tot))
    elif sys.argv[1] == "climb":
        d, w, D, seed, iters = map(int, sys.argv[2:7]); out = sys.argv[7]; rng = random.Random(seed)
        src = open(os.path.join(B191, "climb191.py")).read(); i0 = src.index("def mut(G):"); i1 = src.index("\ncur = ")
        exec(src[i0:i1])
        cur = json.load(open(out)) if os.path.exists(out) else rand191.rgen(rng, d, w, D)
        sc = lambda G: (lambda a: (a["W"] - a["N"], a["W"], a["T"]))(analyse(G)); cs = sc(cur)
        for it in range(iters):
            G = mut(json.loads(json.dumps(cur)))
            try: s2 = sc(G)
            except Exception: continue
            if s2 >= cs: cur, cs = G, s2; json.dump(cur, open(out, "w"))
        print(f"climb d {d} w {w} D {D} seed {seed} iters {iters}:", fmt(analyse(cur)))
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), fmt(analyse(json.load(open(f)))))
