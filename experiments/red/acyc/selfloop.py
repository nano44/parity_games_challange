"""L-RED box 30 (produced on Opus 5.5): direct test of the simplest (ACYC) counterexample shape on a seed game. For every vertex v
of the new part N of a straddling Dom acceptance (probe.py), try: (a) add a self-loop v -> v; (b) (a) and set pr(v) to each value
of parity p up to tpr; (c) (a) and flip owner. Re-run the Python reference (probe.run) and report fitness (ACYC failures, YZ excess,
straddles) of each variant; save any hit. Usage: selfloop.py G.pg OUTDIR"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probe  # noqa: E402
import pg  # noqa: E402
g = pg.read(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
d, ev = probe.run(g)
cands = sorted({(d.idx[v], e["p"], e["tpr"]) for e in ev for v in e["N"]})
print("new-part vertices (orig id, p, tpr):", cands)
tried = hits = 0
for v, p, tpr in cands:
    vars_ = []
    su = [list(s) for s in g.succ]; su[v] = sorted(set(su[v]) | {v})
    vars_.append(("loop", list(g.prio), list(g.owner), su))
    for q in range(p, tpr + 1, 2):
        pr = list(g.prio); pr[v] = q; vars_.append((f"loop+pr{q}", pr, list(g.owner), su))
    ow = list(g.owner); ow[v] = 1 - ow[v]; vars_.append(("loop+owner", list(g.prio), ow, su))
    for name, pr, ow, s2 in vars_:
        h = pg.Game(pr, ow, [list(x) for x in s2]); tried += 1
        try:
            dh, evh = probe.run(h)
        except Exception as ex:
            print(v, name, "ERROR", ex); continue
        ok = all(w is not None for w in dh.win)
        print(v, name, "complete" if ok else "INCOMPLETE", "acyc", dh.acyc_fail, "yz", dh.excess, "straddles", len(evh), "maxN", max((len(e["N"]) for e in evh), default=0))
        if dh.acyc_fail or dh.excess or not ok:
            hits += 1; pg.write(h, os.path.join(out, f"hit_{v}_{name}.pg"))
print("tried", tried, "hits", hits)
