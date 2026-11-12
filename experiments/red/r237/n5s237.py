#!/usr/bin/env python3
"""L-RED 67 R237: a SPEC-EXACT own engine for N5 (mode spec) and N5'-xi (mode xi), written from the SPEC TEXT only
(docs/new/N5-ssi-global.md «SPEC (EXACT)» S1-S5, FIX 1-4, Q1-Q4; box 190 section 1 for S4a'). No code from n5.py, n5v.py, n5x.py,
n5bxi.py, n5b.py or si.py; shares nothing with n5x236.py either (that engine computes optima by switch-all iteration and has its own
tie readings R1-R3; this one runs SPEC S1's Voege-Jurdzinski procedure (i)-(vi) with SPEC's tie-breaks, so its iteration counts are
meant to EQUAL the reference engine's, not only its regions).
SPEC lines implemented (quoted from the SPEC):
 S1 «For v in V in increasing order of reward(v) ..., skipping dead v: (i) v is a cycle node iff DFS from v over G_sigma-successors,
    visiting only alive vertices of rank < rank(v), returns to v ... (ii) R = alive vertices that reach v in G_sigma. (iii) Restricted
    graph on R ... For u in R with rank(u) > rank(v), in decreasing rank: if Omega(u) even: M = vertices of R reaching v without passing
    u; add u to path[q] for q not in M; delete edges from u and from every q in M to vertices outside M. If Omega(u) odd: M = vertices of
    R reaching u without passing v; add u to path[q] for q in M; delete edges from every q in M \\ {u} to vertices outside M. (iv) Lengths:
    if Omega(v) even, Odd takes the LONGEST path to v in the restricted graph (... first strict maximum wins); if Omega(v) odd, the
    SHORTEST (BFS from v over predecessors in list order; first discovery sets Odd's choice). (v) If v is Odd: its choice is the first
    successor on a DFS-found cycle back to v through alive vertices of rank < rank(v). (vi) Every x in R gets valuation (v, path[x],
    length[x]) and Odd's choice from (iv)/(v); R becomes dead.» FIX 2 (explicit-stack DFS over G_sigma, successors in increasing index,
    marked when pushed, last pushed popped first, scan stops at the first successor equal to v, choice = first vertex after v on the
    tree path); FIX 4 (longest: smallest index among the successors of maximum length; BFS: FIFO layers, predecessor lists in
    increasing index, choice = the vertex from which it was first discovered); Q4 (the cycle node's choice comes from (v) only).
 S2, S3 (FIX 1), S4a (S1 procedure on the dual of H), S4b (S1 procedure on H'), S4c (FIX 3), S5, A8 (iteration count).
 S4a' (mode xi; box 190 section 1): «for every Even v with |A(v)| >= 2 whose W*-cycle node is not v itself: TIE(v) := {w in A(v) :
    W*(v) = v (+) W*(w)} ...; if TIE(v) != {}, set sigma_new(v) := the element of TIE(v) that is best for Even under Xi_sigma ...;
    ties by «w = SPEC's sigma_new(v)» first, then by the larger index. Every other vertex keeps SPEC's sigma_new.»
Usage: n5s237.py GAME.pg [spec|xi]"""
import sys

class Ord:
    """SPEC S1's order on valuations (c, P, l) for the game with ranks rk and parities ev (ev[v]: Omega(v) even)."""
    def __init__(s, rk, ev): s.rk, s.ev = rk, ev
    def rew(s, v): return (s.rk[v] + 1) if s.ev[v] else -(s.rk[v] + 1)
    def better(s, a, b):
        """a strictly better than b for the player called Even in this game"""
        if a[0] != b[0]: return s.rew(a[0]) > s.rew(b[0])
        d = a[1] ^ b[1]
        if d:
            z = max(d, key=lambda u: s.rk[u]); return (z in a[1]) == s.ev[z]          # Q1: the top differing vertex decides
        if a[2] != b[2]: return (a[2] > b[2]) if not s.ev[a[0]] else (a[2] < b[2])
        return False

def vjproc(n, rk, ev, gs, chooser):
    """SPEC S1 (i)-(vi). gs[x]: successors of x in G_sigma in increasing index (one successor at the fixed player's vertices);
    chooser[x]: x belongs to the minimiser («Odd» of this game). Returns (val, choice)."""
    alive = [True] * n; val = [None] * n; choice = {}
    gp = [[] for _ in range(n)]
    for x in range(n):
        for y in gs[x]: gp[y].append(x)                                               # predecessor lists, increasing index
    rew = lambda v: (rk[v] + 1) if ev[v] else -(rk[v] + 1)
    for v in sorted(range(n), key=rew):
        if not alive[v]: continue
        seen = {v}; stack = [v]; found = False                                       # (i)
        while stack and not found:
            x = stack.pop()
            for y in gs[x]:
                if y == v: found = True; break
                if alive[y] and rk[y] < rk[v] and y not in seen: seen.add(y); stack.append(y)
        if not found: continue
        R = {v}; stack = [v]                                                         # (ii)
        while stack:
            x = stack.pop()
            for p in gp[x]:
                if alive[p] and p not in R: R.add(p); stack.append(p)
        rs = {x: [y for y in gs[x] if y in R] for x in R}; path = {x: set() for x in R}   # (iii)
        def back(target, avoid):
            pr = {x: [] for x in R}
            for x in R:
                if x == avoid: continue
                for y in rs[x]:
                    if y != avoid: pr[y].append(x)
            M = {target}; st = [target]
            while st:
                x = st.pop()
                for p in pr[x]:
                    if p not in M: M.add(p); st.append(p)
            return M
        for u in sorted((x for x in R if rk[x] > rk[v]), key=lambda x: -rk[x]):
            if ev[u]:
                M = back(v, u)
                for q in R:
                    if q not in M: path[q].add(u)
                rs[u] = [y for y in rs[u] if y in M]
                for q in M: rs[q] = [y for y in rs[q] if y in M]
            else:
                M = back(u, v)
                for q in M: path[q].add(u)
                for q in M:
                    if q != u: rs[q] = [y for y in rs[q] if y in M]
        L = {v: 0}                                                                   # (iv)
        if ev[v]:                                                                    # longest path to v, first strict maximum
            for x0 in sorted(R):
                if x0 in L: continue
                st = [(x0, 0)]; onst = {x0}
                while st:
                    x, i = st[-1]
                    if i < len(rs[x]):
                        st[-1] = (x, i + 1); y = rs[x][i]
                        if y not in L:
                            assert y not in onst, "cycle in restricted graph (SPEC Q3)"
                            onst.add(y); st.append((y, 0))
                    else:
                        assert rs[x], ("no restricted successor", x)
                        best = None
                        for y in rs[x]:
                            if best is None or L[y] > L[best]: best = y
                        L[x] = L[best] + 1; st.pop(); onst.discard(x)
                        if chooser[x]: choice[x] = best
        else:                                                                        # shortest: BFS over predecessors
            pr = {x: [] for x in R}
            for x in sorted(R):
                for y in rs[x]: pr[y].append(x)
            queue = [v]; qi = 0
            while qi < len(queue):
                x = queue[qi]; qi += 1
                for p in pr[x]:
                    if p not in L:
                        L[p] = L[x] + 1; queue.append(p)
                        if chooser[p]: choice[p] = x
            assert len(L) == len(R), "a vertex of R does not reach v in the restricted graph"
        if chooser[v]:                                                               # (v), FIX 2, Q2
            par = {v: None}; stack = [v]; ch = None
            while stack and ch is None:
                x = stack.pop()
                for y in gs[x]:
                    if y == v:
                        z = x
                        while z != v and par[z] != v: z = par[z]
                        ch = z; break
                    if alive[y] and rk[y] < rk[v] and y not in par: par[y] = x; stack.append(y)
            assert ch is not None; choice[v] = ch
        for x in R: val[x] = (v, frozenset(path[x]), L[x]); alive[x] = False          # (vi)
    assert all(x is not None for x in val), "a vertex got no valuation"
    return val, choice

def ext(rk, v, w):
    return (w[0], w[1] | ({v} if rk[v] > rk[w[0]] else frozenset()), w[2] + 1)

def run(prio, owner, succ, mode="spec", cap=10 ** 6, trace=None, fbtrace=None, start=None):
    n = len(prio); order = sorted(range(n), key=lambda v: (prio[v], v)); rk = [0] * n
    for r, v in enumerate(order): rk[v] = r
    ev = [p % 2 == 0 for p in prio]; evd = [not e for e in ev]; O, Od = Ord(rk, ev), Ord(rk, evd)
    succ = [sorted(set(s)) for s in succ]; isE = [o == 0 for o in owner]; isO = [o == 1 for o in owner]
    if start is None:                                                                # S3, FIX 1
        r = lambda p: p if p % 2 == 0 else -p
        sigma = {v: max(succ[v], key=lambda w: (r(prio[w]), w if prio[w] % 2 == 0 else -w)) for v in range(n) if isE[v]}
        tau = {v: max(succ[v], key=lambda w: (r(prio[w] + 1), w if (prio[w] + 1) % 2 == 0 else -w)) for v in range(n) if isO[v]}
    else: sigma, tau = dict(start[0]), dict(start[1])
    it = fb = 0
    while it < cap:
        if trace is not None: trace.append((dict(sigma), dict(tau)))
        vs, sbar = vjproc(n, rk, ev, [[sigma[v]] if isE[v] else succ[v] for v in range(n)], isO)          # Xi_sigma (S1)
        vt, tbar = vjproc(n, rk, evd, [[tau[v]] if isO[v] else succ[v] for v in range(n)], isE)           # Xi_tau on G^d
        Is = {v: [w for w in succ[v] if w != sigma[v] and O.better(vs[w], vs[sigma[v]])] for v in sigma}; Is = {v: ws for v, ws in Is.items() if ws}
        It = {v: [w for w in succ[v] if w != tau[v] and Od.better(vt[w], vt[tau[v]])] for v in tau}; It = {v: ws for v, ws in It.items() if ws}
        if not Is and not It: break
        ns, nt = dict(sigma), dict(tau)
        if Is:                                                                       # S4a: S1 procedure on the dual of H
            A = {v: sorted({sigma[v]} | set(Is.get(v, []))) for v in sigma}
            W, ch = vjproc(n, rk, evd, [A[v] if isE[v] else [tau[v]] for v in range(n)], isE)
            for v in sigma: ns[v] = ch[v]
            if mode == "xi":                                                         # S4a' (box 190 section 1)
                for v in sigma:
                    if len(A[v]) >= 2 and W[v][0] != v:
                        tie = [w for w in A[v] if ext(rk, v, W[w]) == W[v]]
                        if tie:
                            b = tie[0]
                            for w in tie[1:]:
                                if O.better(vs[w], vs[b]): b = w
                                elif not O.better(vs[b], vs[w]) and ((w == ch[v]) > (b == ch[v]) or ((w == ch[v]) == (b == ch[v]) and w > b)): b = w
                            ns[v] = b
        if It:                                                                       # S4b: S1 procedure on H'
            A = {v: sorted({tau[v]} | set(It.get(v, []))) for v in tau}
            _, ch = vjproc(n, rk, ev, [A[v] if isO[v] else [sigma[v]] for v in range(n)], isO)
            for v in tau: nt[v] = ch[v]
        if ns == sigma and nt == tau:                                                # S4c, FIX 3
            fb += 1
            if fbtrace is not None: fbtrace.append(it + 1)
            if Is:
                for v, ws in Is.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if O.better(vs[w], vs[b]) or (not O.better(vs[b], vs[w]) and w > b): b = w
                    ns[v] = b
            else:
                for v, ws in It.items():
                    b = ws[0]
                    for w in ws[1:]:
                        if Od.better(vt[w], vt[b]) or (not Od.better(vt[b], vt[w]) and w > b): b = w
                    nt[v] = b
        sigma, tau = ns, nt; it += 1
    vs, sbar = vjproc(n, rk, ev, [[sigma[v]] if isE[v] else succ[v] for v in range(n)], isO)
    win = [ev[vs[v][0]] for v in range(n)]
    return it, fb, win, sigma, sbar

def parse(fn):
    prio, owner, succ = [], [], []
    for line in open(fn):
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("start"): continue
        parts = line.split(); v, p, o = int(parts[0]), int(parts[1]), int(parts[2]); ss = [int(x) for x in parts[3].split(",")]
        while len(prio) <= v: prio.append(None); owner.append(None); succ.append(None)
        prio[v], owner[v], succ[v] = p, o, sorted(set(ss))
    return prio, owner, succ

if __name__ == "__main__":
    prio, owner, succ = parse(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else "spec"
    it, fb, win, s, sb = run(prio, owner, succ, mode)
    print("N5S237", sys.argv[1].split("/")[-1], "n", len(prio), "mode", mode, "iterations", it, "fallbacks", fb, "even_wins", sum(win), flush=True)
