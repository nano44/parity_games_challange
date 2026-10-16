#!/usr/bin/env python3
"""REFEREE-2 independent check of L-RED's Transfer Lemma (docs/red/R2-RAR.md) on tiny FHZ graphs: G_{n,r,s,t} built from
FHZ arXiv 1410.7530 Table 1 (costs scaled by rs); the parity side P built from the lemma's description (bands per level:
class A -> even g_i on top of the band, class C offset d -> odd o_{i,d} = base_i + 1 + 2d, class B nothing; relays of
priority 0; sink odd).  VJ comparison written from Friedmann 1106.0778 section 3: compare the sets of class vertices on the
two paths by the maximum of the symmetric difference (even -> the set containing it wins), then length (odd sink: longer
wins).  For EVERY tree B and EVERY edge e not in B: strict improvement in G  <=>  strict improvement in P.
Usage: tl_exhaustive.py n r s t   (exhaustive over all trees; n=2,r=s=t=1 is 6561 trees)."""
import sys, itertools
n, r, s, t = map(int, sys.argv[1:5]); rs = r * s
V = ["t"]; E = []       # edges: (src, dst, cost, level, cls, offset, name)
def add(src, dst, cost, lvl, cls, off, name, copies):
    for l in range(copies): E.append((src, dst, cost, lvl, cls, off, name))
for i in range(1, n + 1):
    V += [f"u{i}", f"w{i}"] + [f"a{i},{j},{k}" for j in range(1, r + 1) for k in range(1, s + 1)] + [f"b{i},{j}" for j in range(1, rs + 1)]
U = lambda i: "t" if i == n + 1 else f"u{i}"; W = lambda i: "t" if i == n + 1 else f"w{i}"
for i in range(1, n + 1):
    big, small = rs * 2 ** (2 * i + 1), rs * 2 ** (2 * i)
    for j in range(1, r + 1):
        for k in range(1, s + 1):
            add(f"a{i},{j},{k}", f"a{i},{j},{k+1}" if k < s else f"b{i},1", 0, i, None, None, "a1", 1)
            add(f"a{i},{j},{k}", U(i + 1), big + (k - 1), i, "C", k - 1, "a0", t)
    for j in range(1, rs + 1):
        add(f"b{i},{j}", f"b{i},{j+1}" if j < rs else W(i + 1), 0, i, "A" if j == rs else None, None, "b1", 1)
        add(f"b{i},{j}", U(i + 1), big + rs + (j - 1), i, "C", rs + j - 1, "b0", t)
    add(f"u{i}", f"b{i},1", 0, i, None, None, "u1", t); add(f"u{i}", U(i + 1), small, i, "B", None, "u0", t)
    for j in range(1, r + 1): add(f"w{i}", f"a{i},{j},1", 0, i, None, None, "w", t)
    add(f"w{i}", W(i + 1), small, i, "B", None, "w0", t)
out = {v: [e for e, ed in enumerate(E) if ed[0] == v] for v in V if v != "t"}
base = lambda i: 2 + (i - 1) * (4 * rs + 2)
def classvertex(ed):                 # priority of the class vertex on this edge in P, or None
    _, _, _, i, cls, off, _ = ed
    if cls == "A": return base(i) + 4 * rs
    if cls == "C": return base(i) + 1 + 2 * off
    return None
def path(B, v):
    """G-cost, P-set (frozenset of class-vertex priorities, all distinct by construction), P-length (edges of P)."""
    cost, S, L = 0, set(), 0
    while v != "t":
        ed = E[B[v]]; cost += ed[2]; cv = classvertex(ed); L += 2 + (1 if cv is not None else 0)
        if cv is not None: S.add(cv)
        v = ed[1]
    return cost, frozenset(S), L
def vj_better(a, b):
    """a, b = (set, length): is a strictly better for Even than b? (odd sink)"""
    Sa, La = a; Sb, Lb = b
    d = Sa ^ Sb
    if d:
        m = max(d); return (m % 2 == 0) == (m in Sa)
    return La > Lb
verts = sorted(out); total = bad = 0
for choice in itertools.product(*[out[v] for v in verts]):
    B = dict(zip(verts, choice))
    # acyclicity is automatic (G acyclic). Evaluate all vertices.
    val = {v: path(B, v) for v in verts}
    for v in verts:
        for e in out[v]:
            if e == B[v]: continue
            ed = E[e]
            cG, SG, LG = val[ed[1]] if ed[1] != "t" else (0, frozenset(), 0)
            cv = classvertex(ed)
            impG = ed[2] + cG < val[v][0]
            Se = SG | ({cv} if cv is not None else set()); Le = LG + 2 + (1 if cv is not None else 0)
            impP = vj_better((Se, Le), (val[v][1], val[v][2]))
            total += 1
            if impG != impP:
                bad += 1
                if bad <= 5: print("DISAGREE tree", {k: E[x][6] for k, x in B.items()}, "edge", v, ed[6], "->", ed[1], "G:", impG, "P:", impP)
print(f"n={n} r={r} s={s} t={t}: {total} (tree, edge) tests over all trees; disagreements: {bad}")
