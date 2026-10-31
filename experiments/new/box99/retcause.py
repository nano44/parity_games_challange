#!/usr/bin/env python3
"""L-NEW box 99 (docs/new/N5-QRET-box99.md): the cause of each Even-edge RETURN in a W-run. W-runs as box92/xirun.py.
A return: Even X re-enters g at k -> k + 1, its last leave of g in F at j -> j + 1 (X held g at j). By RET-XIRISE (P-N5-WRUN) Xi(g) rises
at some transition q -> q + 1 with j < q + 1 <= k, i.e. q in [j, k - 1]... we list every rise of Xi(g) for q in [j, k].
For each rise of Xi(g) at q -> q + 1, the FIRST DIVERGENCE of g's (sigma, sbar)-play: walk x = g, ... along the play at q and at q + 1 in
step; the first x whose successor differs is an Even switch (EVS, x Even) or an Odd flip (ODF, x Odd).  If the plays agree up to the cycle
the cycle-node data changed (CYC; cannot happen with the same play, counted as a check).  Also: does W(g) change in [j, k] (WCH)?
Per W-run prints: returns, distinct (X, g), distinct targets g, max returns per g, rises per return, the divergence classes, the top
divergence vertices with their owner and whether they are Odd heads (sbar != tau) at q + 1, and, for ODF, the flip (old -> new target).
ROOT of a return: its first Xi(g)-rise in the window, traced back: EVS divergence at x -> if x's entry at q is FRESH (x never held that
target earlier in F) the root is that fresh entry, if it is itself a return, recurse into that return's first rise; ODF divergence at o
-> recurse into the rise of o's old target at the same q (L-SI ROOT-FLIP), or TIE if the old target did not rise. Prints root kinds,
distinct roots, max returns per root and the chain depths.
EROOT (box 100): the same with the EVEN root map: from a change of Xi(z) at q, x := the first Even vertex on z's OLD play that switches at
q; FRESH entry -> root, a return -> recurse into its window's first rise. 'children per node' = returns whose first rise is at q and whose
first switching Even vertex is x, per (x, q).
Usage: retcause.py GAME.pg [START]   (TOP=k prints k top divergence vertices; default 8)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
TOP = int(os.environ.get('TOP', '8'))
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1; EVN = [v for v in range(n) if own[v] == 0]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
EVc = {}
def EV(k):
    if k not in EVc: EVc[k] = E.evaluate(S[k])
    return EVc[k]
def nxt(k, x): return S[k][x] if own[x] == 0 else EV(k)[1][x]
def diverge(q, z):
    x = z; seen = set()
    while x not in seen:
        seen.add(x)
        a, b = nxt(q, x), nxt(q + 1, x)
        if a != b: return ('EVS' if own[x] == 0 else 'ODF'), x, a, b
        x = a
    return 'CYC', x, None, None
for a, b in runs:
    tau = TAU[a]; held_last = {}; rets = []
    for y in EVN: held_last[(y, S[a][y])] = a
    for k in range(a, b):
        for y in EVN:
            if S[k + 1][y] != S[k][y]:
                e = (y, S[k + 1][y])
                if e in held_last: rets.append((y, S[k + 1][y], held_last[e], k))   # last state holding g, return transition k -> k+1
                held_last[(y, S[k][y])] = k
        for y in EVN: held_last[(y, S[k + 1][y])] = k + 1
    if not rets: continue
    retidx = {(y, z, k): (j) for y, z, j, k in rets}
    fresh_at = {}
    hl = {(y, S[a][y]) for y in EVN}
    for k in range(a, b):
        for y in EVN:
            if S[k + 1][y] != S[k][y] and (y, S[k + 1][y]) not in hl: fresh_at[(y, S[k + 1][y], k)] = True
        hl |= {(y, S[k + 1][y]) for y in EVN}
    memo = {}
    def cause(q, z, vis=None):
        # root of the change of Xi(z) at q -> q + 1 via the FIRST DIVERGENCE; returns (root tuple, relative depth)
        if (q, z) in memo: return memo[(q, z)]
        vis = vis or set()
        if (q, z) in vis: return (('LOOP', z, q), 0)
        vis.add((q, z))
        c, x, o, nw = diverge(q, z)
        if c == 'EVS':
            if (x, nw, q) in fresh_at: res = (('FRESH', x, nw, q), 0)
            elif (x, nw, q) in retidx:
                jj = retidx[(x, nw, q)]; rr = [qq for qq in range(jj, q) if EV(qq)[0][nw] != EV(qq + 1)[0][nw]]
                if rr:
                    sub, d = cause(rr[0], nw, vis); res = (sub, d + 1)
                else: res = (('NORISE', x, nw, q), 0)
            else: res = (('OUT', x, nw, q), 0)
        elif c == 'ODF':
            if EV(q)[0][o] != EV(q + 1)[0][o]:
                sub, d = cause(q, o, vis); res = (sub, d + 1)
            else: res = (('TIE', x, q), 0)
        else: res = (('CYC', x, q), 0)
        memo[(q, z)] = res; return res
    def firstev(q, z):
        # first Even vertex on z's OLD (sigma_q, sbar_q)-play that switches at q -> q + 1 (box 100 Lemma EVEN-ON-PLAY: exists if Xi(z) changes)
        x = z; seen = set()
        while x not in seen:
            seen.add(x)
            if own[x] == 0 and S[q + 1][x] != S[q][x]: return x
            x = nxt(q, x)
        return None
    memoE = {}
    def causeE(q, z):
        # returns (root tuple without depth, relative depth)
        if (q, z) in memoE: return memoE[(q, z)]
        x = firstev(q, z)
        if x is None: res = (('NOEVEN', z, q), 0)
        else:
            w = S[q + 1][x]
            if (x, w, q) in fresh_at: res = (('FRESH', x, w, q), 0)
            else:
                jj = retidx[(x, w, q)]; rr = [qq for qq in range(jj, q) if EV(qq)[0][w] != EV(qq + 1)[0][w]]
                if rr:
                    sub, d = causeE(rr[0], w); res = (sub, d + 1)
                else: res = (('NORISE', x, w, q), 0)
        memoE[(q, z)] = res; return res
    def chainE(q, z):
        # the node sequence (x, q) of the Even root chain from the change of Xi(z) at q
        out = []
        while True:
            x = firstev(q, z)
            if x is None: return out
            out.append((x, q)); w = S[q + 1][x]
            if (x, w, q) in fresh_at: return out
            jj = retidx[(x, w, q)]; rr = [qq for qq in range(jj, q) if EV(qq)[0][w] != EV(qq + 1)[0][w]]
            if not rr: return out
            q, z = rr[0], w
    chstat = Counter(); chmax = [0, 0, None]
    stepseen = set(); lcache = {}
    def blocked(t, y, w):
        Wt = Wv(t, tau); Xt = EV(t)[0]
        return S[t][y] != w and E.key(Wt[w]) > E.key(Wt[S[t][y]]) and not E.key(Xt[w]) > E.key(Xt[S[t][y]])
    def late(y, w, q):
        if (y, w, q) not in lcache: lcache[(y, w, q)] = any(blocked(t, y, w) for t in range(a, q + 1))
        return lcache[(y, w, q)]
    rootsE = Counter(); kindE = Counter(); depE = Counter(); kids = Counter(); perX = Counter(); perE = Counter(); perL = Counter(); perP = Counter(); perD = Counter(); sfs = Counter(); sfX = Counter(); nsX = Counter()
    for y, z, j, k in rets:
        rr = [q for q in range(j, k) if EV(q)[0][z] != EV(q + 1)[0][z]]
        if not rr: continue
        x = firstev(rr[0], z)
        if x is not None: kids[(x, rr[0])] += 1
        rt, d = causeE(rr[0], z); kindE[rt[0]] += 1; depE[d] += 1
        rootsE[rt] += 1
        perX[(y, rt)] += 1; perE[(y, z, rt)] += 1
        perL[(y, S[k][y], rt)] += 1
        perP[(y, S[k][y], z, rt)] += 1
        perD[(y, z, rt, d)] += 1
        pl = []; xx = z; sn = set()
        while xx not in sn: sn.add(xx); pl.append(xx); xx = nxt(k, xx)
        selff = y in sn
        if selff:
            sfs['self'] += 1; sfX[(y, rt)] += 1
            if firstev(rr[0], z) == y: sfs['first_is_X'] += 1
            if EV(k)[0][y][0] != EV(k + 1)[0][y][0]: sfs['lamXi_change'] += 1
            if Wv(k, tau)[y] != Wv(k + 1, tau)[y]: sfs['W_X_change'] += 1
            if Wv(k, tau)[y][0] != Wv(k + 1, tau)[y][0]: sfs['lamW_change'] += 1
            # self-fed: X on g's (sigma_k, sbar_k)-play at the state k just before the return; X on the cycle of its own (sigma_{k+1}, sbar_{k+1})-play after the return
            xx = y; sn2 = []
            while xx not in sn2: sn2.append(xx); xx = nxt(k + 1, xx)
            if y in sn2[sn2.index(xx):]: sfs['X_on_own_cycle_after'] += 1
            if EV(k + 1)[0][y][0] == y: sfs['X_own_cycle_node_after'] += 1
        else:
            nsX[(y, rt)] += 1
        ch = chainE(rr[0], z); xs = [x for x, _ in ch]; rep = len(xs) - len(set(xs))
        for (cx, cq) in ch:
            if (cx, cq) in stepseen: continue
            stepseen.add((cx, cq)); w = S[cq + 1][cx]
            chstat['steps'] += 1
            if Wv(cq, tau) != Wv(cq + 1, tau): chstat['wch'] += 1
            if late(cx, w, cq): chstat['late'] += 1
        chstat['chains'] += 1; chstat['rep'] += rep > 0
        if len(ch) > chmax[0]: chmax[:] = [len(ch), len(set(xs)), ch[:12]]
        chstat['maxrep'] = max(chstat['maxrep'], rep)
        if os.environ.get("XTRACE") and y == int(os.environ["XTRACE"]): print(f"  XTRACE return k {k}: {y} {S[k][y]} -> {z} (window from {j}, first rise {rr[0]}) root {rt} depth {d}")
    roots = Counter(); rkind = Counter(); dep = Counter()
    for y, z, j, k in rets:
        rr = [q for q in range(j, k) if EV(q)[0][z] != EV(q + 1)[0][z]]
        if not rr: continue
        rt, d = cause(rr[0], z); rkind[rt[0]] += 1; dep[d] += 1
        roots[rt] += 1
    cls = Counter(); dv = Counter(); flip = Counter(); per_g = Counter(); nr = Counter(); wch = 0; norise = 0; cache = {}
    for y, z, j, k in rets:
        per_g[z] += 1
        rises = [q for q in range(j, k) if EV(q)[0][z] != EV(q + 1)[0][z]]
        nr[len(rises)] += 1
        if not rises: norise += 1
        if any(Wv(q, tau)[z] != Wv(q + 1, tau)[z] for q in range(j, k)): wch += 1
        for q in rises:
            if (q, z) not in cache: cache[(q, z)] = diverge(q, z)
            c, x, o, nw = cache[(q, z)]
            cls[c] += 1; dv[(x, 'E' if own[x] == 0 else 'O', 'H' if own[x] == 1 and EV(q + 1)[1][x] != tau[x] else '-')] += 1
            if c == 'ODF': flip[(x, o, nw)] += 1
    print(f"RUN {a}-{b} F {b - a} returns {len(rets)} edges {len(set((y, z) for y, z, _, _ in rets))} targets {len(per_g)} "
          f"max_per_target {max(per_g.values())} norise {norise} wch_in_window {wch} rises_per_return {dict(sorted(nr.items()))} classes {dict(cls)}")
    print("  top targets", per_g.most_common(TOP))
    print("  top divergence vertices (v, owner, Odd-head)", dv.most_common(TOP))
    if flip: print("  top Odd flips (o, old, new)", flip.most_common(TOP))
    print(f"  ROOT kinds {dict(rkind)} distinct roots {len(roots)} max returns per root {max(roots.values()) if roots else 0} chain depth {dict(sorted(dep.items()))}")
    print("  top roots (kind, x, w, q)", roots.most_common(TOP))
    print(f"  EROOT kinds {dict(kindE)} distinct roots {len(rootsE)} max returns per root {max(rootsE.values()) if rootsE else 0} "
          f"chain depth {dict(sorted(depE.items()))} max children per node {max(kids.values()) if kids else 0} "
          f"max children per return node {max([v for (x, q), v in kids.items() if (x, S[q + 1][x], q) not in fresh_at] or [0])} mE {sum(len(set(g.succ[v])) for v in EVN)}")
    mxX = max(perX.values()); mxE = max(perE.values()); degr = max(perX[k] / len(set(g.succ[k[0]])) for k in perX)
    wX = [k for k in perX if perX[k] == mxX][0]
    print(f"  PERROOT max returns of one Even X per root {mxX} (X {wX[0]} deg {len(set(g.succ[wX[0]]))}) max returns of one edge per root {mxE} "
          f"max (returns of X per root)/deg X {round(degr, 3)} max returns of X per root leaving one target {max(perL.values())} max returns of X per root with one (left, entered) pair {max(perP.values())} max returns of one edge per (root, depth) {max(perD.values())}")
    nsr = max([nsX[k2] / len(set(g.succ[k2[0]])) for k2 in nsX] or [0])
    print(f"  SELFFED (X on g's play at state k) returns {sfs['self']} of {len(rets)}: first switching Even vertex is X {sfs['first_is_X']}, X on its own Xi-cycle after {sfs['X_on_own_cycle_after']}, X own cycle node after {sfs['X_own_cycle_node_after']}, lambda(Xi(X)) changes {sfs['lamXi_change']}, W(X) changes {sfs['W_X_change']}, lambda_W(X) changes {sfs['lamW_change']}; max self-fed returns of X per root {max(sfX.values()) if sfX else 0}; NONSELF max (returns of X per root)/deg X {round(nsr, 3)}")
    print(f"  CHAINSTEP distinct chain nodes {chstat['steps']} with a W-change at q {chstat['wch']} late adoptions (blocked at an earlier state of F) {chstat['late']}")
    print(f"  CHAIN chains {chstat['chains']} with a repeated Even vertex {chstat['rep']} max repeats {chstat['maxrep']} longest {chmax[0]} distinct {chmax[1]}")
    if os.environ.get("CHAINS"): print("  CHAIN longest", chmax[2])
    if os.environ.get("DBG"): print("  DBG", rootsE.most_common(3), kids.most_common(3))
