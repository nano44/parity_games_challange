#!/usr/bin/env python3
"""L-SI P-IDEAL-DBL fix round 1 (Lead ruling 3): for each DEAD-REENTRY instance and every l in 0..d-2, does the statement
«the strict Xi-descendants of the fuel targets U_l lie at levels > l» (static Xi-graph) fail?
U_l = the Xi-targets (movers) of the upward options of movers of level <= l (an option (x, k) is upward if its Xi-target is a mover
of level > lev(x)). Strict Xi-descendants of y: the movers reachable from y along the Xi-targets of any options, y excluded.
Reading A (as worded): every y in U_l. Reading B: only the y in U_l of level > l.
For each failing l one witness x -> y -> ... -> z (x of level <= l, (x, k) upward to y in U_l, z a strict descendant of y with
lev(z) <= l; the first x, then y, in index order, shortest path y -> z, smallest z). Also checks the paths named by REFEREE-2 W-2 (d)."""
import json, os, hashlib, collections
H = os.path.dirname(os.path.abspath(__file__))
INST = [os.path.join(H, "..", "box76", "inst", "lower", "REC_d10_tower_mu30.json"),
        os.path.join(H, "..", "box76", "inst", "lower", "KILL_M2D_d6_mu13.json")]
def bfs(xt, y):
    par = {y: None}; q = collections.deque([y])
    while q:
        u = q.popleft()
        for v in xt[u]:
            if v >= 0 and v not in par: par[v] = u; q.append(v)
    return par
for p in INST:
    G = json.load(open(p)); N = G["N"]; d = N // 2; lev = G["lev"]; xt = [[G["opts"][x][k][1] for k in range(2)] for x in range(N)]
    print("%s sha1 %s d %d" % (os.path.basename(p), hashlib.sha1(open(p, "rb").read()).hexdigest(), d))
    for rd in ("A", "B"):
        fail = []
        for l in range(0, d - 1):
            cand = sorted((x, y) for x in range(N) if lev[x] <= l for y in xt[x]
                          if y >= 0 and lev[y] > lev[x] and (rd == "A" or lev[y] > l))
            wit = None
            for (x, y) in cand:
                par = bfs(xt, y)
                zs = sorted(z for z in par if z != y and lev[z] <= l)
                if zs:
                    path = [zs[0]]
                    while par[path[-1]] is not None: path.append(par[path[-1]])
                    wit = [x] + path[::-1]; break
            if wit:
                fail.append(l)
                print("  %s l %d FAILS: %s (levels %s)" % (rd, l, " -> ".join(map(str, wit)), " -> ".join(str(lev[v]) for v in wit)))
            else:
                print("  %s l %d holds" % (rd, l))
        print("  reading %s failing l: {%s}" % (rd, ", ".join(map(str, fail))))
    for path in ([1, 11, 3], [2, 5, 3]):
        ok = all(path[i + 1] in xt[path[i]] for i in range(len(path) - 1))
        print("  path %s: %s (levels %s)" % (" -> ".join(map(str, path)), "PRESENT" if ok else "absent",
                                             " -> ".join(str(lev[v]) for v in path)))
