#!/usr/bin/env python3
"""Box 42: data checks of two L-SI 10 claims (docs/si/N5-KW-box15.md) not covered by my checkers:
(FRZ-U) κ(π_v) := π_v ∩ V_{>m*} constant on R from run state k0 + r − 1 (r = |R|), m* = more relevant of c_θ, c_w;
(KM)    KIND-MONO: on U3/U23 runs with c_w ≻ c_θ, after k0 + r − 1 each vertex changes kind at most once, in direction B -> A
        (c_w even; odd is vacuous by Lemma PAR). Usage: sicross.py --list FILE | --rand N lo hi seed [--randstart]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from kwfreeze import *

def go5(g, acc, tag, start=None):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1: return
    rows, o, E = rows_raw(g, start); rk = E.rank; acc["runs"] = acc.get("runs", 0) + 1
    bad = lambda key, info: (acc.__setitem__(key, acc.get(key, 0) + 1), acc.setdefault("ex_" + key, (tag, info)))
    a = 0
    for i in range(1, len(rows) + 1):
        if not (i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]): continue
        x, y_ = a, i - 1; a = i; k = x
        while k <= y_:
            j = k
            while j + 1 <= y_ and all(rows[j + 1][f] == rows[k][f] for f in ("R", "th", "w")): j += 1
            r0 = rows[k]; R = r0["R"]; r = len(R); ct, cw = r0["ct"], r0["cw"]; m = ct if rk[ct] >= rk[cw] else cw
            kap = lambda q, v: frozenset(u for u in route(rows[q]["nxt"], v, o) if rk[u] > rk[m])
            u3 = (not r0["h2"]) and cw != o and rk[cw] > rk[ct]
            st = k
            for t_ in range(k, j + 1):
                if t_ == j or rows[t_]["fb"]:
                    if t_ > st:
                        acc["runs_chk"] = acc.get("runs_chk", 0) + 1; f0 = st + r - 1
                        for q in range(f0, t_):
                            if any(kap(q, v) != kap(q + 1, v) for v in R if v != o): bad("FRZU", (st, q))
                        if u3:
                            cnt = {}
                            for q in range(max(f0, st), t_):
                                for v in R:
                                    if v == o: continue
                                    A0 = cw in route(rows[q]["nxt"], v, o) or v == cw; A1 = cw in route(rows[q + 1]["nxt"], v, o) or v == cw
                                    if A0 != A1:
                                        acc["km_changes"] = acc.get("km_changes", 0) + 1
                                        if A0 and not A1: bad("KM_dir", (q, v))
                                        cnt[v] = cnt.get(v, 0) + 1
                                        if cnt[v] > 1: bad("KM_once", (q, v))
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
            go5(g, acc, ("rand", seed, i), st)
    else:
        for f in [l.strip() for l in open(args[1])]:
            p = f if os.path.exists(f) else os.path.join(root, f)
            try: g = load(p)
            except Exception: continue
            go5(g, acc, f)
            if "--starts" in args:
                rng = random.Random(4209)
                for t in range(40):
                    go5(g, acc, (f, t), ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    viol = {k: v for k, v in acc.items() if k in ("FRZU", "KM_dir", "KM_once")}
    print("violations:", viol if viol else 0); print({k: v for k, v in sorted(acc.items()) if not k.startswith("ex_") and k not in viol})
    for k, v in acc.items():
        if k.startswith("ex_"): print(k, v)
