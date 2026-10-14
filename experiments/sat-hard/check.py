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


def odd_lasso(aut, g):
    """For an odd graph g whose reachable product with aut has a cycle: a lasso (u, v) of letters such that the run of
    aut on u.v^w never hits bottom and u.v^w labels an infinite path of g. Returns None if the product is acyclic."""
    n, E = g
    delta = aut["delta"]
    out = [[] for _ in range(n)]
    for (a, p, b) in E:
        out[a].append((p, b))
    starts = [(v, 0) for v in range(n)]
    parent = {s: None for s in starts}
    order, st = [], list(starts)
    while st:  # BFS tree of the reachable product
        x = st.pop(0); order.append(x)
        v, q = x
        for (p, v2) in out[v]:
            q2 = delta[q][p - 1]
            if q2 is not None and (v2, q2) not in parent:
                parent[(v2, q2)] = (x, p); st.append((v2, q2))
    adj = {x: [] for x in parent}
    for x in parent:
        v, q = x
        for (p, v2) in out[v]:
            q2 = delta[q][p - 1]
            if q2 is not None:
                adj[x].append((p, (v2, q2)))
    # DFS for a cycle
    col = {x: 0 for x in parent}
    for s in parent:
        if col[s]:
            continue
        stack = [(s, iter(adj[s]))]; col[s] = 1; path = [(s, None)]
        while stack:
            x, it = stack[-1]
            nxt = None
            for (p, y) in it:
                if col[y] == 1:
                    # cycle: y ... x -p-> y along path
                    idx = next(i for i, (z, _) in enumerate(path) if z == y)
                    loop = [lab for (_, lab) in path[idx + 1:]] + [p]
                    # prefix: BFS-tree path from a start to y
                    pre, z = [], y
                    while parent[z] is not None:
                        z, lab = parent[z]; pre.append(lab)
                    return list(reversed(pre)), loop
                if col[y] == 0:
                    nxt = (p, y); break
            if nxt:
                p, y = nxt; col[y] = 1; stack.append((y, iter(adj[y]))); path.append((y, p))
            else:
                col[x] = 2; stack.pop(); path.pop()
    return None


def accepts_lasso(aut, u, v):
    """Does aut accept u.v^w (never hits bottom)? Simulates |u| + k|v| letters (pigeonhole on v-boundary states)."""
    q = 0
    for p in u + v * (aut["k"] + 1):
        q = aut["delta"][q][p - 1]
        if q is None:
            return False
    return True
