#!/usr/bin/env python3
"""L-SI box 17: DATA for CONJECTURE LEVEL-COUNT (docs/si/N5-RUND-box17.md §12). Inside each stretch_D segment (D, R_D, the gates' two
values and (h3_D) constant; gap.py's key) of a fallback-free in-phase run, for every v with constant cycle nodes:
  OC     the transitions at which v's offset Delta(v) = s^W - s^Xi changes
  RL     the set of RISE LEVELS of v: top rank of P_k Δ P_{k+1} for each transition at which s^W(v) or s^Xi(v) rises (path set changes)
  LC_V   |OC| > |RL|                                            (CONJECTURE LEVEL-COUNT predicts 0)
  INC_V  the rise level at successive offset changes does not strictly increase (the stronger "levels only increase" form;
         rise level of a transition := max over the two frames of the top changed rank)
Usage: lvl.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED | --one GAME [START]  (NMAX, RS env)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
C = Counter(); VIOL = []

def top(m): return m.bit_length() - 1 if m else -1

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        uu = [next((x for x in lasso(wn, v)[0] if x in D), None) for v in range(g.n)]
        h3 = all(vs[u][0] == W[u][0] for u in D)
        stk = (D, frozenset(v for v in range(g.n) if uu[v] is not None), tuple((u, vs[u], W[u]) for u in sorted(D)), h3)
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), stk=stk, vs=vs, W=W, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        a = i
        while a <= j:
            b = a
            while b + 1 <= j and rows[b + 1]["stk"] == rows[a]["stk"]: b += 1
            if b > a and rows[a]["stk"][3]: seg(g, E, name, rows, a, b)
            a = b + 1
        i = j + 1

def seg(g, E, name, rows, a, b):
    C["segs"] += 1
    for v in range(g.n):
        if len({(rows[x]["vs"][v][0], rows[x]["W"][v][0]) for x in range(a, b + 1)}) > 1: continue
        oc, rl, levs = 0, set(), []
        for k in range(a, b):
            x0, x1, w0, w1 = rows[k]["vs"][v], rows[k + 1]["vs"][v], rows[k]["W"][v], rows[k + 1]["W"][v]
            lx = top(x0[1] ^ x1[1]); lw = top(w0[1] ^ w1[1])
            for L, y0, y1 in ((lx, x0, x1), (lw, w0, w1)):
                if L >= 0 and E.weight(y1[1]) > E.weight(y0[1]): rl.add(L)
            d = (E.weight(w1[1]) - E.weight(x1[1])) - (E.weight(w0[1]) - E.weight(x0[1]))
            if d:
                oc += 1; levs.append(max(lx, lw))
        if oc:
            C["v_with_oc"] += 1; C["oc"] += oc; C["max_oc"] = max(C["max_oc"], oc)
            if oc > len(rl): C["LC_V"] += 1; VIOL.append(("LC", name, a, b, v, oc, sorted(rl)))
            if any(levs[q + 1] <= levs[q] for q in range(len(levs) - 1)): C["INC_V"] += 1; VIOL.append(("INC", name, a, b, v, levs))
            C["oc_ge2"] += oc >= 2

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    elif a[0] == "--rand":
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
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("LVL PASS" if not VIOL else "LVL FAIL")

if __name__ == "__main__":
    main()
