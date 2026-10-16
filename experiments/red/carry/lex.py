#!/usr/bin/env python3
"""L-RED successor 3 (Opus 5.5), 2026-10-16: attack on L-ALG successor 4's (LEX) and (NR) (relayed by the Lead 16:16Z).
Per phase (player p, no dominion between) and depth-0 context R, consecutive best_vertices calls at R (L-ALG's dtl_regvec.py,
read-only via LALG_DIR; order from DTL_ORDER). d(v) = ACTUAL death round of each p-parity v in R (INF if in the stable
result). Vertices ordered by internal index (priority-major, = L-ALG's ids).
 (LEX): if d_s != d_s', the highest-index changed vertex v* has d_s'(v*) > d_s(v*).  Violation = it falls.
 (NR): a vertex that has FALLEN at this context is never again the top changed vertex there.
 Nesting level of a step = 0 if its top vertex never fell here before, else 1 + the level of the step that last knocked
 it down. (NR) says every level is 0; a nest of depth L would allow n^O(L) changes.
Usage: DTL_ORDER=oink LALG_DIR=.. lex.py G.pg ... (-v env LEX_V=1 prints every step)"""
import sys, os
INF = 10 ** 6

def _rv():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_regvec as RV, pg
    return RV, pg

def deaths(r, R, pr, p):
    D = {v: None for v in R if pr[v] % 2 == p}
    for i in range(1, len(r)):
        for x in r[i - 1] - r[i]: D[x] = i
    for x in r[-1]: D[x] = INF
    return D

def measure(path):
    RV, pg = _rv(); g = pg.read(path); d = RV.build(g); d.run()
    ctxs = []
    for (p, R), occ in d.calls.items():
        steps = []
        for (s1, r1, v1, h1, _), (s2, r2, v2, h2, _) in zip(occ, occ[1:]):
            t1, t2 = d.trace[s1 - 1], d.trace[s2 - 1]
            if t1["p"] != t2["p"] or t1["dom"] != t2["dom"]: continue      # same phase only
            if any(d.trace[k]["p"] != p or d.trace[k]["dom"] != t1["dom"] for k in range(s1 - 1, s2)): continue
            Da, Db = deaths(r1, R, d.pr, p), deaths(r2, R, d.pr, p)
            ch = [v for v in Da if Da[v] != Db[v]]
            if not ch: continue
            top = max(ch)
            steps.append(dict(s=s2, top=top, up=Db[top] > Da[top], fell=[v for v in ch if Db[v] < Da[v]],
                              ideal_same=h1 == h2, ideal_stable=h1[0] == 1, Da=Da, Db=Db))
        if steps: ctxs.append(dict(p=p, R=R, steps=steps))
    out = dict(ctx=len(ctxs), steps=0, lex_viol=0, nr_viol=0, maxlevel=0, maxsteps=0, ex=[])
    for c in ctxs:
        knocked = {}                                  # vertex -> level of the step that last knocked it down
        out["maxsteps"] = max(out["maxsteps"], len(c["steps"]))
        for st in c["steps"]:
            out["steps"] += 1
            lvl = 1 + knocked[st["top"]] if st["top"] in knocked else 0
            st["level"] = lvl
            if not st["up"]:
                out["lex_viol"] += 1
                if len(out["ex"]) < 6: out["ex"].append(("LEX", st["s"], d.idx[st["top"]], len(c["R"])))
            if lvl:
                out["nr_viol"] += 1; out["maxlevel"] = max(out["maxlevel"], lvl)
                if len(out["ex"]) < 6: out["ex"].append(("NR", st["s"], d.idx[st["top"]], len(c["R"]), lvl))
            for v in st["fell"]: knocked[v] = lvl
    return out, ctxs, d

def score(path):
    o, _, d = measure(path)
    return 100000 * o["maxlevel"] + 1000 * o["nr_viol"] + 100 * o["lex_viol"] + 10 * o["maxsteps"] + len(d.trace) / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        o, ctxs, d = measure(f)
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} searches={len(d.trace)} {o}")
        if os.environ.get("LEX_V"):
            nm = lambda x: "INF" if x == INF else x
            for c in ctxs:
                print(f"  player {c['p']} |R| {len(c['R'])}")
                for st in c["steps"]:
                    print(f"    s{st['s']} top {d.idx[st['top']]} {nm(st['Da'][st['top']])}->{nm(st['Db'][st['top']])} level {st['level']}"
                          f" fell {[(d.idx[v], nm(st['Da'][v]), nm(st['Db'][v])) for v in st['fell']]} ideal_same={st['ideal_same']}")

def score_falls(path):
    """successor 3: target = >= 2 FALL steps (some death decreases) at one (phase, context); (NR) depth >= 2 needs it.
    Score: 100000 x max fall steps at one context + 1000 x max steps at a context having a fall + steps."""
    o, ctxs, d = measure(path)
    mf = max((sum(1 for st in c["steps"] if st["fell"]) for c in ctxs), default=0)
    ms = max((len(c["steps"]) for c in ctxs if any(st["fell"] for st in c["steps"])), default=0)
    return 100000 * mf + 1000 * ms + 10 * o["maxsteps"] + len(d.trace) / 1000.0
