import sys, os, json, random
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), "../r178", "../r170", "../../new/box21"]
from n5x import Engine
import downgen, stab
from n5x import Engine
rng = random.Random(1); G = downgen.randdown(3, 2, rng)
g, sig, tau, gv, ev, bv = stab.build(G, 0, kgad=True)
s = tuple(sig.get(v, -1) for v in range(g.n)); E = Engine(g); vals, sb = E.evaluate(s)
print("lev", G["lev"], "opts", G["opts"])
for q, x in sorted(gv.items()):
    print(q, "gate", x, "e", ev[q], "beta", bv[q], "sbar", sb[x], "val e", vals[ev[q]], "val beta", vals[bv[q]])
print("prio", g.prio); print("succ", g.succ)
