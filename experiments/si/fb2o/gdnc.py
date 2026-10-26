#!/usr/bin/env python3
"""L-SI box 16: DATA for Lemma G_D-NC (docs/si/N5-2O-T-box16.md §6): RESULTS R55's G_D (b) and (c2) with (h_D) replaced by (NC):
no vertex of D_k lies on its own honest cycle or on its own W-cycle. At every state of every N5 run (n5x.py step, read-only) it checks:
  B   (NC) => for every v in R_D, with u := u(v) and pi_v := v's W-path before u:  Xi(v) = pi_v (+) Xi(u)  and  W(v) = pi_v (+) W(u)
      ((+) = iterated S1 extension, Engine.extend), and the honest and W-plays from u avoid pi_v
  C2  (NC) and (h3_D) => COARSE_L(Xi(v)) = COARSE_L(W(v)) for every v, at L = max(M_D, -1)
  FRZ (NC) and (h3_D) at every state of a fallback-free run S inside a phase, L := max(max_S M_D, -1): COARSE_L(W) is constant on S
      from its (n-1)-th state on (successor 10's CR-D with (NC) for (h_D))
Counts the states with (h_D) and with (NC), so the gain of the weaker hypothesis is visible. MUT=1 drops (NC) from B (control: must fail).
Usage: gdnc.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED  (K=2 env: C^2O only; odd #: S3 start, even #: random start pair)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso, wval
MUT = os.environ.get("MUT") == "1"
C = dict(FRZ_runs=0, FRZ_n=0, FRZ_V=0, states=0, D2=0, hD=0, NC=0, NC_not_hD=0, B_n=0, B_V=0, C2_n=0, C2_V=0)
VIOL = []

def lev(E, x, y):
    if x[0] != y[0]: return 10 ** 9
    d = x[1] ^ y[1]
    if d: return d.bit_length() - 1          # top differing rank
    return -1 if x[2] != y[2] else -2         # -2 stands for "bottom" (equal)

def coarse(x, L):
    return (x[0], (x[1] >> (L + 1)) << (L + 1)) if L >= 0 else (x[0], x[1])

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0; rows = []
    while k <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = {u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]}
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        hn = (lambda s, b: (lambda v: s[v] if g.owner[v] == 0 else b[v]))(list(s), list(sb))
        C["states"] += 1; C["D2"] += len(D) == 2
        oncyc = lambda nx, u: (lambda pl_i: u in pl_i[0][pl_i[1]:])(lasso(nx, u))
        nc = all(not oncyc(nx, u) for u in D for nx in (wn, hn))
        hd = all(not any(x in D for x in lasso(nx, nx(u))[0]) for u in D for nx in (wn, hn))
        C["hD"] += hd; C["NC"] += nc; C["NC_not_hD"] += nc and not hd
        W = {v: wval(E, wn, v) for v in range(g.n)}
        if nc or MUT:
            for v in range(g.n):
                pl, _ = lasso(wn, v); u = next((x for x in pl if x in D), None)
                if u is None or u == v: continue
                pi = pl[:pl.index(u)]
                okx, okw = vs[u], W[u]
                for x in reversed(pi): okx = E.extend(x, okx); okw = E.extend(x, okw)
                avoid = not any(x in pi for nx in (wn, hn) for x in lasso(nx, u)[0])
                C["B_n"] += 1
                if okx != vs[v] or okw != W[v] or not avoid:
                    C["B_V"] += 1; VIOL.append(("B", name, k, v, u))
        h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([lev(E, vs[u], W[u]) for u in D], default=-2) if h3 else 10 ** 9
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), hyp=nc and h3, M=M, W=W, fb=r[4] if r else 0))
        if nc and h3:
            L = max(M, -1)
            for v in range(g.n):
                C["C2_n"] += 1
                if coarse(vs[v], L) != coarse(W[v], L): C["C2_V"] += 1; VIOL.append(("C2", name, k, v))
        if r is None: break
        s, t = r[0], r[1]; k += 1
    # FRZ-U_D: maximal runs of consecutive non-fallback transitions inside one phase with (NC) and (h3_D) at every state
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"] and rows[i]["hyp"] and rows[j + 1]["hyp"]:
            j += 1
        if rows[i]["hyp"] and j > i:
            C["FRZ_runs"] += 1
            L = max(max(rows[x]["M"] for x in range(i, j + 1)), -1)
            base = i + g.n - 1
            for x in range(base + 1, j + 1):
                C["FRZ_n"] += 1
                if any(coarse(rows[x]["W"][v], L) != coarse(rows[base]["W"][v], L) for v in range(g.n)):
                    C["FRZ_V"] += 1; VIOL.append(("FRZ", name, i, x))
        i = j + 1

def main():
    a = sys.argv[1:]
    if a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, f"rand seed {seed} #{i}", None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 48 or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g, f)
    print(" ".join(f"{k}={v}" for k, v in C.items()))
    for v in VIOL[:10]: print("VIOLATION", v)
    print("GDNC PASS" if not VIOL else "GDNC FAIL")

if __name__ == "__main__":
    main()
