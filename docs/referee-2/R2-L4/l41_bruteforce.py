#!/usr/bin/env python3
"""Brute-force check of Lemma L4.1 (a)-(b): for EVERY edge-labelled multigraph H with k <= 2 vertices over Sigma_3
(all 2^12 subsets of V x Sigma x V; sinks pruned first, see check()) and random ones with k = 3, d = 4: build H' = V x Sigma, pr'(v,p) = p,
E' = {((u,p),(v,q)) : (u,q,v) in E}; check (b) 'H even <=> H' even' and 'H odd <=> H' odd' by enumerating all simple
cycles, and (a) 'finite words of length L of H' = {p.w : p in Sigma, w finite word of H of length L-1}' for L <= 5."""
import itertools, random
def simple_cycles_max(V, succ):          # succ[v] = list of (label, w); returns set of max labels over all simple cycles
    maxes = set()
    def dfs(start, v, path, labels):
        for lab, w in succ[v]:
            if w == start:
                maxes.add(max(labels + [lab]))
            elif w not in path and w > start:
                dfs(start, w, path | {w}, labels + [lab])
    for s in V:
        dfs(s, s, {s}, [])
    return maxes
def parity_class(maxes):                 # 'even' if all cycle maxima even, 'odd' if all odd, 'none' if no cycle, 'mixed'
    if not maxes: return "none"
    ev = all(m % 2 == 0 for m in maxes); od = all(m % 2 == 1 for m in maxes)
    return "even" if ev else "odd" if od else "mixed"
def words(V, succ, L):
    out = set()
    def go(v, w):
        if len(w) == L: out.add(tuple(w)); return
        for lab, u in succ[v]: go(u, w + [lab])
    for v in V: go(v, [])
    return out
def check(k, d, E):
    # the lemma is about INFINITE paths: prune sinks of H iteratively first (this does not change Words(H) or Words(H')
    # and prunes exactly the sinks (v,p) of H'); without this, finite prefixes of dead-end paths break the finite test
    V = list(range(k)); S = list(range(1, d + 1))
    while True:
        alive = {v for v in V if any(u == v and w in V for (u, q, w) in E)}
        if alive == set(V): break
        V = sorted(alive); E = [e for e in E if e[0] in alive and e[2] in alive]
    if not V: return None
    succ = {v: [(q, w) for (u, q, w) in E if u == v] for v in V}
    Vp = [(v, p) for v in V for p in S]
    succp = {x: [(x[1], (w, q)) for (u, q, w) in E if u == x[0]] for x in Vp}   # V convention: edge (x,y) carries pr(x)
    cH, cHp = parity_class(simple_cycles_max(V, succ)), parity_class(simple_cycles_max(Vp, succp))
    if (cH == "even") != (cHp == "even") or (cH == "odd") != (cHp == "odd"):
        return f"(b) fails: H {cH}, H' {cHp}, E={E}"
    for L in range(1, 6):
        lhs = words(Vp, succp, L)
        rhs = {(p,) + w for p in S for w in words(V, succ, L - 1)}
        if lhs != rhs:
            return f"(a) fails at L={L}: E={E}"
    return None
fails = 0; total = 0
k, d = 2, 3
edges = [(u, q, w) for u in range(k) for q in range(1, d + 1) for w in range(k)]
for mask in range(1 << len(edges)):
    E = [e for i, e in enumerate(edges) if mask >> i & 1]
    r = check(k, d, E); total += 1
    if r: fails += 1; print(r)
rnd = random.Random(1)
for _ in range(300):
    k, d = 3, 4
    edges = [(u, q, w) for u in range(k) for q in range(1, d + 1) for w in range(k)]
    E = [e for e in edges if rnd.random() < 0.25]
    r = check(k, d, E); total += 1
    if r: fails += 1; print(r)
print(f"L4.1 (a)-(b) brute force: {total} graphs, {fails} failures")
