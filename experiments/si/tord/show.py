import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abs2 import run, paths, pval
I = json.loads(sys.argv[1]); G, rho, pp, th1, c1, th2, c2 = I; n = len(G)
print("G", G, "pp", pp, "th1", th1, "th2", th2)
w, s, why, h = run(*I)
for k, (r, ch) in enumerate(h + [(None, None)]):
    if r is None: break
    P = paths(list(r), n)
    print(k, "rho", r, "W-changed next", ch)
    for x in range(n):
        print("   ", x, P[x], "Ξ", sorted(pval(P[x], pp, th1)[0]), pval(P[x], pp, th1)[1], "W", sorted(pval(P[x], pp, th2)[0]))
print(w, s, why)
