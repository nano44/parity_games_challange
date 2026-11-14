#!/usr/bin/env python3
"""L-SI box 88: own implementation of L-RED 60's switch census (docs/red/R226-race.md §4, claude/l-red d08e317a; nest226.py not used).
A SWITCH: a step t -> t+1 at a mover x with >= 2 options and sigma_(t+1)(x) = g_new != g_old = sigma_t(x). «reward» if
Lambda_t(g_new) != Lambda_t(g_old). Else E_new, E_old := e-vertices on the plays from g_new, g_old at state t (Pi_t), z := max(E_new ^ E_old);
TYPE II iff some e in E_new & E_old is more relevant than z; head := the least relevant such e.
N2 := #type-II switches; depth := max over (x, maximal Lambda(x)-interval) of #distinct heads; maxII := max type II per (x, interval).
Usage: nest88.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
for f in sys.argv[2:]:
    G = json.load(open(f)); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
    ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
    rows = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); rows.append((s, cur, sb, vs))
    sw = rew = t1 = t2 = 0; heads = {}; cntII = {}; ivl = {x: 0 for x in range(N)}
    for t in range(len(rows) - 1):
        s, cur, sb, vs = rows[t]; s2 = rows[t + 1][0]
        for x in range(N):
            if t and rows[t][3][movers[x]][0] != rows[t - 1][3][movers[x]][0]: ivl[x] += 1   # new maximal Lambda(x)-interval
            if len(G["opts"][x]) < 2 or s2[x] == s[x]: continue
            sw += 1; gn, go = V[("g", (x, s2[x]))], V[("g", (x, s[x]))]
            if vs[gn][0] != vs[go][0]: rew += 1; continue
            nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
            def eset(v):
                seen = set(); out = set()
                while v not in seen: seen.add(v); out |= {v} & ev; v = nxt(v)
                return out
            En, Eo = eset(gn), eset(go); d = En ^ Eo
            if not d: t1 += 1; continue
            z = max(d, key=rank); H = [v for v in En & Eo if rank(v) > rank(z)]
            if H:
                t2 += 1; key = (x, ivl[x]); heads.setdefault(key, set()).add(min(H, key=rank)); cntII[key] = cntII.get(key, 0) + 1
            else: t1 += 1
    print(os.path.basename(f), "T", len(rows) - 1, "switches", sw, "reward", rew, "typeI", t1, "N2", t2,
          "maxII", max(cntII.values(), default=0), "depth", max((len(v) for v in heads.values()), default=0))
