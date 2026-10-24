#!/usr/bin/env python3
"""Box 25: W-drops at Even fallbacks (τ fixed), split by whether hypothesis (h) of box 21 Lemma G holds at the state:
o on no cycle of the (σ,σ̄)-play or the (σ,τ)-play from o, and Ξ(o), W(o) with the same cycle node.
Usage: wdrop_h.py N nmin nmax seed [--randstart] [--write out]  |  wdrop_h.py game.pg [start]"""
from common import *
from abovefind import write
def oncycle(g, s, t2, o):
    nxt = [s[v] if g.owner[v] == 0 else t2[v] for v in range(g.n)]; x, seen = nxt[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = nxt[x]
    return False
def drops(g, start, cnt):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); o = odd_choice(g); hit = None
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: return hit
        ns, nt, Is, It, fb, vs, _ = r
        if fb and list(nt) == list(t):
            Eg, W0 = wvals(g, s, t); _, W1 = wvals(g, ns, t)
            if any(Eg.key(W1[v]) < Eg.key(W0[v]) for v in range(g.n)):
                _, sb = E.evaluate(tuple(s))
                h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and vs[o][0] == W0[o][0]
                cnt["drop_h" if h else "drop_noth"] += 1
                if h and hit is None: hit = True
        s, t = ns, nt
if __name__ == "__main__":
    a = sys.argv[1:]; cnt = {"runs": 0, "drop_h": 0, "drop_noth": 0}
    if a[0].endswith(".pg"):
        g = load(a[0]); drops(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(cnt); sys.exit()
    RS = "--randstart" in a; out = a[a.index("--write") + 1] if "--write" in a else None
    N, lo, hi, seed = map(int, a[0:4]); rng = random.Random(seed)
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        cnt["runs"] += 1
        if drops(g, start, cnt) and out:
            E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
            write(g, ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1}), out); out = None
            print("wrote n", g.n)
    print(cnt)
