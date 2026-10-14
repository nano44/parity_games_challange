"""Independent checker for weak separators (convention E): product reachability and cycle detection, no SAT.
Against the family produced by graphs.family (each graph re-verified even / odd by brute force)."""
from __future__ import annotations


def violations(aut, evens, odds, first=False):
    delta = aut["delta"]
    bad = []
    for gi, (n, E) in enumerate(evens):
        out = [[] for _ in range(n)]
        for (u, p, v) in E:
            out[u].append((p, v))
        seen, st, hit = set((v, 0) for v in range(n)), [(v, 0) for v in range(n)], False
        while st and not hit:
            v, q = st.pop()
            for (p, v2) in out[v]:
                q2 = delta[q][p - 1]
                if q2 is None:
                    hit = True; break
                if (v2, q2) not in seen:
                    seen.add((v2, q2)); st.append((v2, q2))
        if hit:
            bad.append(("even", gi))
            if first: return bad
    for gi, (n, E) in enumerate(odds):
        out = [[] for _ in range(n)]
        for (u, p, v) in E:
            out[u].append((p, v))
        # reachable product, then Kahn's algorithm: acyclic iff all nodes removed
        nodes, st = set((v, 0) for v in range(n)), [(v, 0) for v in range(n)]
        adj = {}
        while st:
            x = st.pop(); v, q = x; adj[x] = []
            for (p, v2) in out[v]:
                q2 = delta[q][p - 1]
                if q2 is None:
                    continue
                adj[x].append((v2, q2))
                if (v2, q2) not in nodes:
                    nodes.add((v2, q2)); st.append((v2, q2))
        indeg = {x: 0 for x in nodes}
        for x in nodes:
            for y in adj[x]:
                indeg[y] += 1
        q = [x for x in nodes if indeg[x] == 0]; removed = 0
        while q:
            x = q.pop(); removed += 1
            for y in adj[x]:
                indeg[y] -= 1
                if indeg[y] == 0:
                    q.append(y)
        if removed < len(nodes):
            bad.append(("odd", gi))
            if first: return bad
    return bad
