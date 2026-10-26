#!/usr/bin/env python3
"""Box 42 (2): KW-FREEZE without events. RUN := maximal run of transitions of a stretch with no fallback (events allowed).
h := the more relevant of c_θ, c_w. Checks on every run of every stretch (any class):
(FZW) COARSE_h(W) = (cycle node, W path set ∩ ↑h) constant on R from run transition n − 1 on;
(FZX) COARSE_h(Ξ) constant on R from n − 1 on;
(CS)  CSTRICT for all successors: at every state, for Even x ∈ R ∖ {o} and successors z, a = σ(x) in R: COARSE_h(W(z)) ≻ COARSE_h(W(a))
      (same cycle node c_w; path-set ∩ ↑h compared by Engine weight) implies Ξ(z) > Ξ(a);
(KW)  W-changing transitions of the run ≤ (n − 1) + 2n|R|;  (NX) if c_θ ≻ c_w: Ξ-changing-on-R transitions ≤ (n − 1) + 2n|R|.
Usage: kwfreeze2.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kwfreeze import *

def go2(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = rows_raw(g, start); n = g.n; rk = E.rank; acc["runs"] = acc.get("runs", 0) + 1
    bad = lambda key, info: (acc.__setitem__(key, acc.get(key, 0) + 1), acc.setdefault("ex_" + key, (tag, info)))
    a = 0
    for i in range(1, len(rows) + 1):
        if not (i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]): continue
        x, y_ = a, i - 1; a = i; k = x
        while k <= y_:
            j = k
            while j + 1 <= y_ and all(rows[j + 1][f] == rows[k][f] for f in ("R", "th", "w")): j += 1
            r0 = rows[k]; R = r0["R"]; ct, cw = r0["ct"], r0["cw"]
            h = ct if rk[ct] > rk[cw] else cw; mask = ~((1 << (rk[h] + 1)) - 1)
            cW = lambda q, v: (rows[q]["W"][v][0], rows[q]["W"][v][1] & mask)
            cX = lambda q, v: (rows[q]["Xi"][v][0], rows[q]["Xi"][v][1] & mask)
            for q in range(k, j + 1):   # CSTRICT at every state of the stretch
                W, Xi, s = rows[q]["W"], rows[q]["Xi"], rows[q]["s"]
                for xv in R:
                    if xv == o or g.owner[xv] != 0: continue
                    av = s[xv]
                    if av not in R: continue
                    for z in g.succ[xv]:
                        if z == av or z not in R: continue
                        if W[z][0] != W[av][0]: bad("CS_cyc", (q, xv, z)); continue
                        if E.weight(W[z][1] & mask) > E.weight(W[av][1] & mask):
                            acc["cs_cases"] = acc.get("cs_cases", 0) + 1
                            if not E.key(Xi[z]) > E.key(Xi[av]): bad("CS", (q, xv, z))
            st = k
            for t_ in range(k, j + 1):
                if t_ == j or rows[t_]["fb"]:
                    sub = list(range(st, t_))
                    if sub:
                        acc["fbfree_runs"] = acc.get("fbfree_runs", 0) + 1
                        for q in range(st + n - 1, t_):
                            if any(cW(q, v) != cW(q + 1, v) for v in R): bad("FZW", (st, q))
                            if any(cX(q, v) != cX(q + 1, v) for v in R): bad("FZX", (st, q))
                        wc = sum(any(rows[q]["W"][v] != rows[q + 1]["W"][v] for v in R) for q in sub)
                        xc = sum(any(rows[q]["Xi"][v] != rows[q + 1]["Xi"][v] for v in R) for q in sub)
                        if wc > (n - 1) + 2 * n * len(R): bad("KW", (st, t_, wc))
                        if rk[ct] > rk[cw] and xc > (n - 1) + 2 * n * len(R): bad("NX", (st, t_, xc))
                        acc["max_wc_run"] = max(acc.get("max_wc_run", 0), wc)
                        lc = max([q - st for q in sub if any(cW(q, v) != cW(q + 1, v) or cX(q, v) != cX(q + 1, v) for v in R)], default=-1)
                        if lc >= 0: acc["max_lastc_over_n"] = max(acc.get("max_lastc_over_n", 0.0), round(lc / (n - 1), 3))
                    st = t_ + 1
            k = j + 1

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    if args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            go2(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go2(g, acc, f)
    viol = {k: v for k, v in acc.items() if k in ("CS", "CS_cyc", "FZW", "FZX", "KW", "NX")}
    print("violations:", viol if viol else 0); print({k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
    for k, v in acc.items():
        if k.startswith("ex_"): print(k, v)
