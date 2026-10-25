#!/usr/bin/env python3
"""Box 42 (2): Theorem KW-FREEZE check (docs/new/N5-KW-box42.md). Every stretch of every phase (R, θ, w constant), any class.
Specials S := {c_θ if ¬H1 and c_θ ≠ o} ∪ {c_w if ¬H2 and c_w ≠ o}; CLS(v) := S ∩ π_v (v ∈ R ∖ {o}). An EVENT transition has a
switching Even R-vertex y with CLS(y) changed, or y ∈ S. A SUB-RUN: maximal run of transitions of a stretch with no fallback and no
event. h := the more relevant of c_θ, c_w; COARSE_h(W) := (cycle node, path-set ∩ ranks above h).
Checks: (CLS) every CLS constant on a sub-run; (FZ) COARSE_h(W) on R constant from transition n − 1 of the sub-run on;
(HF) if c_θ ≻ c_w: Ξ's path set on R constant from transition n − 1 on; (KW) W-changing transitions of the sub-run
≤ (n − 1) + |R|(n − 1); (KS) per stretch: K_S ≤ E*_S + (E*_S + f_S + 1)(n² − 1).
Usage: kwfreeze.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from nhcheck import *

def rows_raw(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h1, h2 = not oncycle(g, s, sb, o), not oncycle(g, s, t, o)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), h1=h1, h2=h2, Xi=Xi, W=W, R=frozenset(reach_o(g, s, t, o)) | {o},
                         th=E.key(Xi[o]), w=E.key(W[o]), ct=Xi[o][0], cw=W[o][0], s=tuple(s), nxt=[s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)], fb=0))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = 1 if r[4] else 0; s, t = r[0], r[1]
    return rows, o, E

def go(g, acc, tag, start=None):
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
            r0 = rows[k]; R = r0["R"]; Rv = [v for v in R if v != o]; ct, cw = r0["ct"], r0["cw"]
            S = set()
            if not r0["h1"] and ct != o: S.add(ct)
            if not r0["h2"] and cw != o: S.add(cw)
            h = ct if rk[ct] > rk[cw] else cw; mask = ~((1 << (rk[h] + 1)) - 1)
            cls_ = lambda t_, v: frozenset(S & set(route(rows[t_]["nxt"], v, o)))
            Es = 0; fS = sum(rows[q]["fb"] for q in range(k, j)); KS = 0; st = k
            for t_ in range(k, j + 1):
                end = t_ == j; ev = False
                if not end:
                    sw = [v for v in Rv if g.owner[v] == 0 and rows[t_]["s"][v] != rows[t_ + 1]["s"][v]]
                    ev = any(v in S or cls_(t_, v) != cls_(t_ + 1, v) for v in sw)
                    Es += ev
                    if not rows[t_]["fb"] and any(rows[t_]["W"][v] != rows[t_ + 1]["W"][v] for v in R): KS += 1
                    end = ev or rows[t_]["fb"]
                if end:
                    sub = list(range(st, t_)); acc["subruns"] = acc.get("subruns", 0) + 1
                    if sub:
                        c0 = {v: cls_(st, v) for v in Rv}
                        for q in range(st + 1, t_ + 1):
                            if any(cls_(q, v) != c0[v] for v in Rv): bad("CLS", (st, q)); break
                        fz = st + n - 1
                        for q in range(fz, t_):
                            if any((rows[q]["W"][v][0], rows[q]["W"][v][1] & mask) != (rows[q + 1]["W"][v][0], rows[q + 1]["W"][v][1] & mask) for v in R): bad("FZ", (st, q))
                            if rk[ct] > rk[cw] and any(rows[q]["Xi"][v][1] != rows[q + 1]["Xi"][v][1] for v in R): bad("HF", (st, q))
                        wc = sum(any(rows[q]["W"][v] != rows[q + 1]["W"][v] for v in R) for q in sub)
                        if wc > (n - 1) + len(R) * (n - 1): bad("KW", (st, t_, wc))
                        acc["max_wc_sub"] = max(acc.get("max_wc_sub", 0), wc)
                        lastc = max([q - st for q in sub if any((rows[q]["W"][v][0], rows[q]["W"][v][1] & mask) != (rows[q + 1]["W"][v][0], rows[q + 1]["W"][v][1] & mask) for v in R)], default=-1)
                        acc["max_last_coarse_idx"] = max(acc.get("max_last_coarse_idx", -1), lastc)
                    st = t_ + 1
            if KS > Es + (Es + fS + 1) * (n * n - 1): bad("KS", (k, j))
            key = "S" + str(len(S)); acc[key] = acc.get(key, 0) + 1
            acc["max_E*"] = max(acc.get("max_E*", 0), Es); acc["sum_E*"] = acc.get("sum_E*", 0) + Es; acc["sum_KS"] = acc.get("sum_KS", 0) + KS
            k = j + 1

if __name__ == "__main__":
    args = sys.argv[1:]; acc = {}; root = os.path.join(HERE, "..", "..", "..")
    if args[0] == "--rand":
        RS = "--randstart" in args; N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            go(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go(g, acc, f)
    viol = {k: v for k, v in acc.items() if k in ("CLS", "FZ", "HF", "KW", "KS")}
    print("violations:", viol if viol else 0); print({k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
    for k, v in acc.items():
        if k.startswith("ex_"): print(k, v)
