#!/usr/bin/env python3
"""L-SI box 81 ASCENT CENSUS on IDEAL-CYC(G) (RESULTS R118's model: Gamma(G) of R104, every non-mover Even vertex frozen at R104's
stated start, Howard at the movers, Odd = VJ optimal counterstrategy). Runner = L-NEW's byte copies in ref/ (box191 idealcyc.py,
box189 gamma3.py, experiments/si/si.py Engine as idealcyc imports it); this file only reads their output.
Definitions (box 193, quoted in docs/si/box81-bridge.md §1): seq_t(v) = the e-vertices of Pi_t(v) in play order; an ASCENT = consecutive
a, b in seq_t(v) with rank(b) > rank(a). Unit = play (one per (state t, vertex v)); set = all plays of the run; scope = stored start.
Per instance prints: N, M, T (Howard steps), C/R/p counts, U(G) (strictly upward Xi-edges), Xi-acyclic?, histogram of ascents per play,
max ascents; e-set heights: maxDE (max over (v, Lambda) of distinct e-parts) and maxDEv (max over v of distinct (Lambda, e-part)), D;
gate flips (sigma-bar changes per gate), R_mov, L_g (face ties); checks: UP-B (max asc <= U), HUB-ASC-G (per (v, Lambda) interval,
distinct e-parts <= F'_B(M_w) with B = max ascents of v's seqs there), OVT-DV (flips(g) <= 2 min(D(e_g), D(beta_g)) - 1 when L_g = 0),
R-SPLIT (R <= R_mov + sum over X-gates of (4M + 5 + L_g)).  LOC=1 also lists every play with >= 2 ascents (signature: v's kind/level,
each ascent (a, b) as (lev, mover, option), the upward Xi-edges on each ascent segment as (lev x, x, k) -> (lev x', x')).
Usage: census81.py [--loc] FILES.json"""
import sys, os, json
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, "ref", "experiments", "new", "box191"), os.path.join(HERE, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3


def Fp(B, M):
    f = 1 + M * (M + 1) // 2
    for _ in range(B): f = (M * M + 3 * M + 1) * (1 + M * f * f)
    return f


def xi_acyclic(G):
    N = G["N"]; adj = [[o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col[y] == 1 or (col[y] == 0 and not dfs(y)): return False
        col[x] = 2; return True
    sys.setrecursionlimit(10000)
    return all(col[x] or dfs(x) for x in range(N))


def census(G, loc=False, cap=10 ** 5):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=cap)
    _, _, _, V = gamma3.build(G, set()); name = {v: k for k, v in V.items()}
    N, lev = G["N"], G["lev"]
    gi = {}
    for x in range(N):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    evs = [v for v in range(h.n) if name[v][0] == "e"]; ES = 0
    for v in evs: ES |= 1 << E.rank[v]
    gates = [v for v in range(h.n) if name[v][0] == "g"]
    U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    hist = Counter(); maxasc = 0; first2 = None
    seenE = defaultdict(set); Bmax = defaultdict(int); seenEv = defaultdict(set); seenV = defaultdict(set)
    lab = []; prev = None; flips = Counter(); ties = Counter(); Rmov = 0; Rx = 0
    locs = Counter(); locex = {}
    xt_of_gate = {V[("g", (x, k))]: G["opts"][x][k][1] for x in range(N) for k in range(len(G["opts"][x]))}
    for t, s in enumerate(st):
        cur = list(s0)
        for x in range(N): cur[movers[x]] = gi[(x, s[x])]
        vals, sb = E.evaluate(tuple(cur))
        nxt = [cur[v] if h.owner[v] == 0 else sb[v] for v in range(h.n)]
        lamv = [vals[v][0] for v in range(h.n)]; sbo = [sb[v] for v in range(h.n) if h.owner[v] == 1]
        if prev is not None:
            if lamv != prev[0]: lab.append("C")
            elif sbo != prev[1]: lab.append("R")
            else: lab.append("p")
            chg = [g for g in gates if sb[g] != prev[2][g]]
            for g in chg: flips[g] += 1
            if lab[-1] == "R":
                if any(xt_of_gate[g] >= 0 for g in chg): Rmov += 1
                else: Rx += 1
        prev = (lamv, sbo, list(sb))
        for g in gates:
            e, b = h.succ[g]
            if E.key(vals[e]) == E.key(vals[b]): ties[g] += 1
        for v in range(h.n):
            lam = vals[v][0]; path = []; vis = set(); u = v
            while u not in vis: vis.add(u); path.append(u); u = nxt[u]
            seq = [y for y in path if name[y][0] == "e" and (vals[v][1] >> E.rank[y]) & 1]
            na = sum(1 for p, q in zip(seq, seq[1:]) if E.rank[q] > E.rank[p])
            hist[na] += 1; maxasc = max(maxasc, na)
            ep = vals[v][1] & ES
            seenE[(v, lam)].add(ep); Bmax[(v, lam)] = max(Bmax[(v, lam)], na); seenEv[v].add((lam, ep)); seenV[v].add(vals[v])
            if na >= 2:
                if first2 is None: first2 = t
                if loc:
                    kind = name[v][0]; vl = lev[name[v][1]] if kind == "x" else (lev[name[v][1][0]] if kind in "gbe" else None)
                    asc = []
                    for p, q in zip(seq, seq[1:]):
                        if E.rank[q] <= E.rank[p]: continue
                        seg = path[path.index(p) + 1: path.index(q)]
                        ups = tuple((lev[name[z][1][0]], name[z][1][0], name[z][1][1], lev[name[nxt[z]][1]], name[nxt[z]][1])
                                    for z in seg if name[z][0] == "b" and name[nxt[z]][0] == "x" and lev[name[nxt[z]][1]] > lev[name[z][1][0]])
                        asc.append(((lev[name[p][1][0]],) + tuple(name[p][1]), (lev[name[q][1][0]],) + tuple(name[q][1]), ups))
                    sig = (kind, vl, tuple(asc)); locs[sig] += 1
                    locex.setdefault(sig, (t, v, na))
    M = len(evs); Rw = 4 * M + 5
    # bound checks
    hubfail = 0; hubslack = None
    for key, S in seenE.items():
        v, lam = key; Mw = sum(1 for y in evs if E.rank[y] > E.rank[lam])
        b = Fp(Bmax[key], Mw)
        if len(S) > b: hubfail += 1
        hubslack = b - len(S) if hubslack is None else min(hubslack, b - len(S))
    ovtfail = 0; ovtmax = 0
    D = {v: len(seenV[v]) for v in range(h.n)}
    for g in gates:
        e, b = h.succ[g]
        if ties[g] == 0:
            bd = 2 * min(D[e], D[b]) - 1
            if flips[g] > bd: ovtfail += 1
        ovtmax = max(ovtmax, flips[g])
    R = lab.count("R"); Lsum = sum(ties.values())
    rsplit = Rmov + sum(Rw + ties[g] for g in gates if xt_of_gate[g] < 0)
    r = dict(N=N, M=M, n=h.n, T=len(st) - 1, C=lab.count("C"), R=R, p=lab.count("p"), U=U, xiacyc=int(xi_acyclic(G)),
             maxasc=maxasc, hist=dict(sorted(hist.items())), plays=sum(hist.values()), first2=first2,
             maxDE=max(len(S) for S in seenE.values()), maxDEv=max(len(S) for S in seenEv.values()), maxD=max(D.values()),
             maxDmover=max(D[x] for x in movers), Rmov=Rmov, Rx=Rx, Lsum=Lsum, maxflips=ovtmax,
             upb="OK" if maxasc <= U else "VIOLATION", hubfail=hubfail, hubslack=hubslack, ovtfail=ovtfail,
             rsplit="OK" if R <= rsplit else "VIOLATION", labels="".join(lab))
    return r, locs, locex


if __name__ == "__main__":
    args = sys.argv[1:]; loc = "--loc" in args; args = [a for a in args if a != "--loc"]
    for f in args:
        G = json.load(open(f)); r, locs, locex = census(G, loc)
        lab = r.pop("labels")
        print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in r.items()).replace(": ", ":"))
        print("  labels", lab)
        if loc:
            for sig, c in locs.most_common():
                print("  LOC2", c, "kind", sig[0], "lev", sig[1], "first(t,v,asc)", locex[sig], "ascents", sig[2])
