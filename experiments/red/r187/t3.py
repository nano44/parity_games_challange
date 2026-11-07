import sys, os, json, random
sys.path[:0] = [os.path.dirname(os.path.abspath(__file__)), "../r178", "../r170", "../../new/box21"]
from n5x import Engine
import stabrun, fastcyc, stab
rng = random.Random(4)
for t in range(int(sys.argv[1])):
    G = fastcyc.randG(3, 2, rng)
    if t not in (2, 8, 13): continue
    R = stabrun.analyse(G, 0)
    print(t, "opts", G["opts"], "lev", G["lev"]); 
    for r in R["rows"][:3]: print("  j %d fb %d tau %s sbar %s W %s sbar!=X %d tau!=W %d moves %d" % r)
    g, sig, tau, gv, ev, bv = stab.build(G, 0, kgad=True, esc=True)
    s = tuple(sig.get(v, -1) for v in range(g.n)); vals, sb = Engine(g).evaluate(s)
    for q, x in sorted(gv.items()):
        if sb[x] != bv[q]: print("   gate", q, "sbar->", sb[x], "e", vals[ev[q]], "beta", vals[bv[q]])
    if t == 2:
        print("prio", g.prio); print("succ", g.succ); print("sig", s); print("sbar", sb)
        x = gv[(5, 0)]; print("gate", x, "e", ev[(5, 0)], "beta", bv[(5, 0)])
        for st in (ev[(5, 0)], bv[(5, 0)]):
            y = st; seen = []
            while y not in seen: seen.append(y); y = s[y] if g.owner[y] == 0 else sb[y]
            print("play", seen, "->", y, [g.prio[z] for z in seen])
