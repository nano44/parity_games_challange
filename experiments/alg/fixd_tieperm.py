"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28c addendum 3: permute the within-priority order of instances with same-priority-below events and count ABOVE events, the case-(a) precondition and case-(a) steals (stable order). Usage: fixd_tieperm.py K G.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'harness'))
sys.setrecursionlimit(100000)
import pg, fixd_stealentry as SE, zielonka
def stats(g):
    d = SE.run(g, "stable"); above = below = 0
    for ph, R, p, rounds in d.visits:
        for steps in rounds:
            for top, pref, rec, fz in steps:
                for t in fz:
                    vs = [v for v, _ in d.tv[t]]
                    if any(v > top and d.pr[v] == d.pr[top] for v in vs): above += 1
                    if any(v < top and d.pr[v] == d.pr[top] for v in vs): below += 1
    SE.PRE[:] = [0, 0, 0]; r = SE.analyze(d)
    return above, below, SE.PRE[0], r[1], r[3], d
def permute(g, rnd):
    perm = list(range(g.n)); rnd.shuffle(perm)        # new id of old vertex v is perm[v]; stable order = (prio, new id)
    inv = [0] * g.n
    for v, nv in enumerate(perm): inv[nv] = v
    return pg.Game([g.prio[inv[i]] for i in range(g.n)], [g.owner[inv[i]] for i in range(g.n)], [sorted(perm[w] for w in g.succ[inv[i]]) for i in range(g.n)])
files = sys.argv[2:]; K = int(sys.argv[1]); tot = [0, 0, 0, 0, 0, 0]; rnd = random.Random(11)
for f in files:
    g0 = pg.read(f)
    a, b, pre, ca, v, _ = stats(g0)
    if b == 0: continue
    for k in range(K):
        g = permute(g0, rnd); a, b, pre, ca, v, d = stats(g); tot[0] += 1; tot[1] += a; tot[2] += b; tot[3] += pre; tot[4] += ca; tot[5] += v
        if a or pre or ca or v:
            os.makedirs("tieperm_found", exist_ok=True); p = f"tieperm_found/tieperm_{os.path.basename(f)}_{k}.pg"; pg.write(g, p)
            W = [None] * g.n
            for i, w in enumerate(d.win): W[d.idx[i] if hasattr(d, 'idx') else i] = w
            print("HIT", f, k, "above", a, "precondition", pre, "case a", ca, "viol", v, "->", p, flush=True)
    print("after", f, "runs", tot[0], "ABOVE", tot[1], "precondition", tot[3], "case (a)", tot[4], "viol", tot[5], flush=True)
print("runs", tot[0], "ABOVE", tot[1], "below", tot[2], "precondition", tot[3], "case (a) steals", tot[4], "violations", tot[5])
