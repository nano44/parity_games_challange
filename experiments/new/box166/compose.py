#!/usr/bin/env python3
"""L-NEW box 166: exact composition search for a PM kill. Clock = any IDEAL genome C (corpus file) with a start; V = the violator,
all V-movers on level L+1 (one above clock level L), V's Xi-graph disjoint from C's (no V-mover gains descendants; desc(x0) = 4).
A V-option W-points to a level-L clock mover, so KP_t(x) for x in V is decided by the clock keys under the NEW clock state s_t:
option k is preferred iff key_t(wt(x,k)) + gate < key_t(wt(x,1-k)) + gate', i.e. by the order of the two W-targets (ties = same
target -> own gates). The clock run is not affected by V (nobody W-points to V; Xi disjoint), so V's run is: s_t(x) = KP_t(x) if x is
unhappy at s_(t-1), else unchanged, with the combined run stopping when nothing changes (clock frozen after its own end).
Search: every clock file, starts (all if N <= 10 else a sample), every level L with >= 2 movers, every assignment of W-target pairs
(each V-mover: an ordered pair (p, q) of level-L movers, p = wt(x, 0), q = wt(x, 1); p = q allowed with both gate orders), every V start.
Reports the max moves(x0) and writes a full genome for any kill (moves(x0) > 5), re-verified by the plain simulator.
Usage: compose.py vfile x0 clockfile ..."""
import os, sys, json, itertools, random
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
V = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); gv = Gen(V); NV = V["N"]
vstates = list(itertools.product((0, 1), repeat=NV)); unh = {s: [x for x in range(NV) if len(gv.avail(s, x)) == 2] for s in vstates}
rng = random.Random(1)

def vrun(seqs, assign, s):
    # seqs[pairindex][t] = 1 if option 0 preferred at step t (t = 1..), last value repeats
    mv = 0; t = 0; Tc = len(seqs[0])
    while True:
        t += 1; n = list(s)
        for x in unh[s]:
            q = seqs[assign[x]][min(t, Tc) - 1]; n[x] = 0 if q else 1
        n = tuple(n)
        if n == s:
            if t >= Tc: return mv
            continue
        mv += n[x0] != s[x0]; s = n
        if t > 400: return mv

def build_kill(Cg, cstart, plist, levlist, vs):
    """full genome: clock movers 0..NC-1, V movers NC..; V-mover x on level levlist[x] + 1, W-targets plist[x] = (p, q, gate swap)"""
    NC = Cg["N"]; N = NC + NV; M0 = sum(len(o) for o in Cg["opts"])
    opts = [list(map(list, o)) for o in Cg["opts"]]; gate = [list(gg) for gg in Cg["gate"]]
    mg = max(x for gg in gate for x in gg) + 1
    br = list(Cg["br"]) + [0] * (2 * NV); bp = list(Cg["bp"]) + [0] * (2 * NV); topr = max(Cg["br"]) + 1
    for x in range(NV):
        p, q, gsw = plist[x]; o = []
        for k in range(2):
            xt = V["opts"][x][k][1]; m = M0 + 2 * x + k
            o.append([(p, q)[k], xt + NC if xt >= 0 else -1, m]); br[m] = topr + V["br"][V["opts"][x][k][2]]; bp[m] = V["bp"][V["opts"][x][k][2]]
        opts.append(o); gate.append([mg + 2 * x, mg + 2 * x + 1] if not gsw else [mg + 2 * x + 1, mg + 2 * x])
    return {"N": N, "lev": list(Cg["lev"]) + [levlist[x] + 1 for x in range(NV)], "opts": opts, "gate": gate, "br": br, "bp": bp,
            "start": list(cstart) + list(vs), "deg": [len(o) for o in opts]}

best = (0, None); report = []
for cf in sys.argv[3:]:
    try: Cg = json.load(open(cf)); assert "N" in Cg; gc = Gen(Cg)
    except Exception: continue
    NC = Cg["N"]; levs = sorted(set(Cg["lev"]))
    starts = [tuple(Cg["start"])]
    if NC <= 10: starts = list(itertools.product(*[range(len(o)) for o in Cg["opts"]]))
    else: starts += [tuple(rng.randrange(len(o)) for o in Cg["opts"]) for _ in range(60)]
    if len(starts) > 1024: starts = rng.sample(starts, 1024)
    fbest = 0
    for cs in starts:
        try: S, _ = gc.run(list(cs))
        except RuntimeError: continue
        if len(S) < 4: continue
        keys = [gc.keys(S[t]) for t in range(1, len(S))]
        pairs = []; plev = []
        for L in levs:
            ms = [v for v in range(NC) if Cg["lev"][v] == L]
            if len(ms) < 2: continue
            for pq in [(p, q, 0) for p in ms for q in ms if p != q]: pairs.append(pq); plev.append(L)
        if not pairs: continue
        pairs += [(pairs[0][0], pairs[0][0], 0), (pairs[0][0], pairs[0][0], 1)]; plev += [plev[0], plev[0]]
        seqs = [[int((k[p] + (0,)) < (k[q] + (1,))) if p != q else int(sw == 0) for k in keys] for p, q, sw in pairs]
        uniq = {}
        for i, sq in enumerate(seqs):
            if tuple(sq) not in uniq: uniq[tuple(sq)] = i
        idx = list(uniq.values())
        if len(idx) ** NV > 300000: idx = idx[:max(2, int(300000 ** (1 / NV)))]
        for assign in itertools.product(idx, repeat=NV):
            for vs in vstates:
                m = vrun(seqs, assign, vs)
                if m > fbest: fbest = m
                if m > best[0]:
                    best = (m, (os.path.basename(cf), cs, [(pairs[a], plev[a]) for a in assign], vs))
                    if m > 5:
                        G = build_kill(Cg, cs, [pairs[a] for a in assign], [plev[a] for a in assign], vs)
                        r = measure(G); xr = Cg["N"] + x0
                        ok = r["mv"][xr] > 1 + r["desc"][xr]
                        fn = os.path.join(H, "out", "KILL_PM_compose_%s.json" % os.path.basename(cf)[:-5])
                        json.dump(G, open(fn, "w"))
                        print("CANDIDATE KILL", os.path.basename(cf), "moves(x0) composed", m, "| re-verified plain run: moves", r["mv"][xr], "desc", r["desc"][xr], "T", r["T"], "KILL" if ok else "MISMATCH", fn, flush=True)
    report.append((os.path.basename(cf), fbest)); print("clock", os.path.basename(cf), "N", NC, "max moves(x0)", fbest, flush=True)
print("BEST", best[0], best[1])
