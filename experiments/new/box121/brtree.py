#!/usr/bin/env python3
"""L-NEW box 121 N5-BRTREE: Odd's best-response forest of G_sigma along an N5 run, inside tau-stretches.
F_k := the functional graph f_k(v) = sigma_k(v) (Even v), sbar_k(v) (Odd v; sbar = si.Engine's optimal Odd counterstrategy to sigma_k),
with the out-edge of each cycle node c = Xi_k(v)[0] cut, so F_k is an in-forest rooted at the cycle nodes; ROOTOK counts vertices whose
f-path does not reach Xi_k(v)'s cycle node (expected 0).
Per transition k -> k+1 inside a tau-stretch (tau_k = tau_(k+1)):
- LINKE / LINKO: vertices whose F-parent changes, Even (= sigma switches) / Odd (best-response changes); XCH := vertices with Xi changing.
- XIN_OLD counts the play (tree path plus the cycle closed from the root); «path only» omits the cycle.
- OCH := stretch transitions with LINKO > 0; SBCH := those where sbar changes anywhere (cycle nodes included); maxOW := the longest run
  of consecutive stretch transitions with LINKO = 0 (Odd's best-response forest part fixed).
- CONTAIN test (fresh feeding, box 119): for an inconsistent transition k with k-1 in the same stretch and a switched edge (y, z) not in
  Is_(k-1) (so Xi(z) changed at k-1): IN_OLD := z's F_(k-1)-path to its root meets a vertex whose sigma changed at k-1 (z included);
  IN_NEW := the same in F_k. Also per Xi-change of any vertex x at any stretch transition j: XIN_OLD := x's F_j-path meets a sigma-switched
  vertex of j.
- Potentials on F_k: PHL := sum_v log2(subtree size), PDEP := sum_v depth, PROOT := number of roots; UP / DN := transitions where each rises /
  falls (inside stretches only).
Usage: brtree.py G.pg [START|-]   prints one BRT line."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1
EV = [E.evaluate(x) for x in S]
ISS = [set(E.improving(S[k], EV[k][0])) for k in range(K + 1)]
rootbad = 0
def forest(k):
    global rootbad
    val, sb = EV[k]
    par = [None] * n
    for v in range(n):
        c = val[v][0]
        if v == c: continue
        par[v] = S[k][v] if own[v] == 0 else sb[v]
    # depth, root, subtree sizes
    dep = [None] * n; root = [None] * n
    for v in range(n):
        path = []; x = v; steps = 0
        while dep[x] is None and par[x] is not None and steps <= n: path.append(x); x = par[x]; steps += 1
        if dep[x] is None:
            if par[x] is None: dep[x] = 0; root[x] = x
            else: rootbad += 1; dep[x] = 0; root[x] = x   # cycle not through a cut node
        for y in reversed(path): dep[y] = dep[par[y]] + 1; root[y] = root[par[y]]
    for v in range(n):
        if root[v] != val[v][0]: rootbad += 1
    size = [1] * n
    for v in sorted(range(n), key=lambda x: -dep[x]):
        if par[v] is not None: size[par[v]] += size[v]
    return par, dep, size
F = [forest(k) for k in range(K + 1)]
def fnext(k, v): return S[k][v] if own[v] == 0 else EV[k][1][v]
def meets(k, z, sw, cyc=True):
    """z's F_k-path to its root meets sw; with cyc, also the play's cycle (from the root along f_k back to it)."""
    par = F[k][0]; x = z; c = 0; last = z
    while x is not None and c <= n:
        if x in sw: return True
        last = x; x = par[x]; c += 1
    if cyc:
        x = fnext(k, last); c = 0
        while x != last and c <= n:
            if x in sw: return True
            x = fnext(k, x); c += 1
    return False
pot = []
for k in range(K + 1):
    par, dep, size = F[k]
    pot.append((sum(math.log2(x) for x in size), sum(dep), sum(p is None for p in par)))
tot = dict(st=0, le=0, lo=0, xch=0, ff=0, inold=0, innew=0, xin=0, xinp=0, xall=0, inc=0, och=0, mow=0, sbch=0)
ow = 0
UP = [0, 0, 0]; DN = [0, 0, 0]; maxlo = 0
for k in range(K):
    if T[k + 1] != T[k]: ow = 0; continue
    if k == 0 or T[k - 1] != T[k]: ow = 0
    tot["st"] += 1
    p0, p1 = F[k][0], F[k + 1][0]
    swk = {v for v in range(n) if own[v] == 0 and S[k][v] != S[k + 1][v]}
    le = len(swk); lo = sum(1 for v in range(n) if own[v] == 1 and p0[v] != p1[v])
    tot["le"] += le; tot["lo"] += lo; maxlo = max(maxlo, lo)
    sbch = any(own[v] == 1 and EV[k][1][v] != EV[k + 1][1][v] for v in range(n))
    if lo: tot["och"] += 1; ow = 0
    else: ow += 1; tot["mow"] = max(tot["mow"], ow)
    tot["sbch"] += sbch
    xc = [x for x in range(n) if EV[k][0][x] != EV[k + 1][0][x]]; tot["xch"] += len(xc)
    for x in xc: tot["xall"] += 1; tot["xin"] += meets(k, x, swk); tot["xinp"] += meets(k, x, swk, False)
    for i in range(3):
        UP[i] += pot[k + 1][i] > pot[k][i] + 1e-9; DN[i] += pot[k + 1][i] < pot[k][i] - 1e-9
    # inconsistent / fresh-fed at k (needs k-1 in the same stretch)
    if k >= 1 and T[k - 1] == T[k]:
        sw = [(v, S[k + 1][v]) for v in swk]
        if any(e not in ISS[k - 1] for e in sw):
            tot["ff"] += 1
            swp = {v for v in range(n) if own[v] == 0 and S[k - 1][v] != S[k][v]}
            zs = [z for (y, z) in sw if (y, z) not in ISS[k - 1]]
            tot["inold"] += all(meets(k - 1, z, swp) for z in zs); tot["innew"] += all(meets(k, z, swp) for z in zs)
print(f"BRT {os.path.basename(sys.argv[1])} n {n} K {K} ROOTOK {int(rootbad == 0)} stretchT {tot['st']} LINKE {tot['le']} LINKO {tot['lo']} "
      f"maxLINKO {maxlo} OCH {tot['och']} SBCH {tot['sbch']} maxOW {tot['mow']} XCH {tot['xch']} XIN_OLD {tot['xin']}/{tot['xall']} (path only {tot['xinp']}) FF {tot['ff']} IN_OLD {tot['inold']} IN_NEW {tot['innew']} "
      f"PHL up/dn {UP[0]}/{DN[0]} PDEP up/dn {UP[1]}/{DN[1]} PROOT up/dn {UP[2]}/{DN[2]}")
