#!/usr/bin/env python3
"""L-SI box 16: DATA for docs/si/N5-2O-T-box16.md §8. At states with |D_k| = 2 whose two gates u, u' are TWINS (same honest cycle node c,
same W-cycle node c_w) and (h3_D) fails (c_w != c), it compares the cross-terminal disagreement levels
  L_X := top rank of P(Xi(u)) sym-diff P(Xi(u')),  L_W := top rank of P(W(u)) sym-diff P(W(u'))  (-1 if equal sets)
with rank(m*), m* := the more relevant of c and c_w. "above" counts states where max(L_X, L_W) > rank(m*): there R50's Fact B fails
across the two terminals above m*, so the kind bit c_w is below the cross-terminal disagreement. Usage: twin.py --list F [KMIN] | --rand ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso, wval
C = dict(states=0, D2=0, twin=0, twin_noh3=0, above=0, below=0, cw_above_c=0)

def top(m): return m.bit_length() - 1 if m else -1

def check(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0
    while k <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = sorted(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); C["states"] += 1
        if len(D) == 2:
            C["D2"] += 1
            wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
            a, b = D; Wa, Wb = wval(E, wn, a), wval(E, wn, b)
            if vs[a][0] == vs[b][0] and Wa[0] == Wb[0]:
                C["twin"] += 1
                c, cw = vs[a][0], Wa[0]
                if c != cw:
                    C["twin_noh3"] += 1; C["cw_above_c"] += E.rank[cw] > E.rank[c]
                    m = max(E.rank[c], E.rank[cw])
                    L = max(top(vs[a][1] ^ vs[b][1]), top(Wa[1] ^ Wb[1]))
                    C["above" if L > m else "below"] += 1
        if r is None: break
        s, t = r[0], r[1]; k += 1

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
            check(g, None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 48 or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g)
    print(" ".join(f"{k}={v}" for k, v in C.items()))

if __name__ == "__main__":
    main()
