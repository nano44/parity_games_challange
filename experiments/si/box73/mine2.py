import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dyn2
tabs = [tuple(int(w, 16) for w in l.split()) for l in open("tables.txt")]
res = {}
for tab in tabs:
    for cc in range(4):
        c = {(1, 0): cc & 1, (1, 1): cc >> 1}
        T0, T1, pq = dyn2.analyse(tab, c)
        for b in (0, 1):
            best = {}
            for (bb, p, q) in pq:
                if bb == b: best[p] = max(best.get(p, -1), q)
            k = (T0[b], T0[1 - b]); r = res.setdefault(k, {})
            for p, q in best.items(): r[p] = max(r.get(p, -1), q)
for k in sorted(res): print("T0(pre bit) %d T0(post bit) %d : max post by pre %s" % (k + (dict(sorted(res[k].items())),)))
