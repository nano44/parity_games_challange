#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): graded fitness toward re-steal depth 2 (R37). Events, causes and depth exactly as in
L-ALG's dtl_stealdepth.analyze (l-alg 931fc221; same RM records via dtl_stealdepth.run_game, unmodified), recomputed here
to expose the causes. For each re-steal e and each cause c of e: pos(c) = how many events q(c) has had up to and including c
(pos(c) >= 2 means c is itself a re-steal, so depth(e) can be 2). Score: 1e12 incomplete + 1e9 max depth + 1e6 max pos(c)
+ 1e4 causek (max over cause quadruples of their event count in the phase) + 1e3 max k + #re-steals. Judge every hit with the unmodified dtl_stealdepth.py. Usage: depthgrad.py G.pg ..."""
import sys, os
for k, v in (("RM_DV", "0"), ("RM_LIGHT", "1"), ("RM_EXCL", "1"), ("RM_PREF", "1")): os.environ[k] = v
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_stealdepth as SD
FD = SD.FD


def measure_game(g, order):
    d = SD.run_game(g, order)
    m = dict(incomplete=int(not all(w is not None for w in d.win)), maxd=0, maxpos=0, causek=0, maxk=0, resteals=0)
    for ph in FD.phase_rows(d):
        visits = {}
        for r_ in ph:
            for rc in r_["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, rcs in visits.items():
            ev = []
            for i in range(len(rcs) - 1):
                x, y = rcs[i], rcs[i + 1]; ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
                for k in ey:
                    if k not in ex: continue
                    for t in ey[k]:
                        if t < x["ntv"] and t not in ex[k] and t in fx.get(k, frozenset()): ev.append((i, k, t))
            depth, last, kq, pos, cq = {}, {}, {}, {}, set()
            for e in ev:
                i, k, t = e; q = (k, t); kq[q] = kq.get(q, 0) + 1; pos[e] = kq[q]; m["maxk"] = max(m["maxk"], kq[q])
                if q not in last: depth[e] = 0; last[q] = i; continue
                j = last[q]; last[q] = i; tv = {v for v, _ in d.tv[t]}
                shr = [mm for mm in range(j + 1, i) if k in rcs[mm]["pref"] and k in rcs[mm + 1]["pref"] and (rcs[mm]["pref"][k] & tv) - rcs[mm + 1]["pref"][k]]
                causes = [c for c in ev if c[0] in shr and SD.earlier(c[1], k) and c in depth]
                if not causes: depth[e] = None; continue
                m["resteals"] += 1; m["maxpos"] = max(m["maxpos"], max(pos[c] for c in causes)); cq |= {(c[1], c[2]) for c in causes}
                ds = [depth[c] for c in causes if depth[c] is not None]
                depth[e] = 1 + min(ds) if ds else None
                if depth[e] is not None: m["maxd"] = max(m["maxd"], depth[e])
            if cq: m["causek"] = max(m["causek"], max(kq[q] for q in cq))
    return m


def score(path):
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e9 * min(m["maxd"], 999) + 1e6 * min(m["maxpos"], 999) + 1e4 * min(m["causek"], 99) + 1e3 * min(m["maxk"], 999) + min(m["resteals"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]: print(os.path.relpath(f), measure_game(pg.read(f), os.environ.get("DTL_ORDER", "stable")), flush=True)
