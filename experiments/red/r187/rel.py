#!/usr/bin/env python3
"""L-RED R187 REL: release statistics of an IDEAL trajectory (option index per mover per state).
M[l] = moves at level l (l = 0 bottom). SEG: the states are cut at every transition with a move at level <= j ("key change below
level j+1"); a transition belongs to the segment of its NEW state. DREL[j] = max over segments of the moves at level j+1 inside it;
D2[j] = number of segments with >= 2 level-(j+1) moves. KCHMAX = max over x of KCH_x (transitions changing sigma on B_x, the movers
below x on W-target paths). Lib: stats(G, S)."""
def below(G, x):
    N, opts = G["N"], G["opts"]; B = set(); st = [o[0] for o in opts[x] if o[0] >= 0]
    while st:
        u = st.pop()
        if u in B: continue
        B.add(u); st += [o[0] for o in opts[u] if o[0] >= 0]
    return B
def stats(G, S):
    N, lev = G["N"], G["lev"]; d = max(lev) + 1; T = len(S) - 1
    mv = [[v for v in range(N) if S[t][v] != S[t - 1][v]] for t in range(1, T + 1)]
    M = [sum(1 for t in mv for v in t if lev[v] == l) for l in range(d)]
    DREL, D2 = [], []
    for j in range(d - 1):
        segs = [0]
        for t in mv:
            if any(lev[v] <= j for v in t): segs.append(0)
            segs[-1] += sum(1 for v in t if lev[v] == j + 1)
        DREL.append(max(segs)); D2.append(sum(1 for c in segs if c >= 2))
    K = {}
    for x in range(N):
        B = below(G, x); K[x] = sum(1 for t in mv if any(v in B for v in t))
    return dict(T=T, M=M, DREL=DREL, D2=D2, KCHMAX=max(K.values()) if K else 0)
def pervertex(G, S):
    """per level l: mu = max moves of a level-l mover, kch = max KCH_x, per = max moves of one mover inside one key-stretch
    (OVT-KEY: <= deg - 1), twice = #(x, stretch) with >= 2 moves of x."""
    N, lev = G["N"], G["lev"]; d = max(lev) + 1; T = len(S) - 1
    out = []
    for l in range(d):
        mu = kch = per = tw = 0
        for x in (v for v in range(N) if lev[v] == l):
            B = below(G, x); sid = 0; cnt = {}
            for t in range(1, T + 1):
                if any(S[t][v] != S[t - 1][v] for v in B): sid += 1
                if S[t][x] != S[t - 1][x]: cnt[sid] = cnt.get(sid, 0) + 1
            mu = max(mu, sum(cnt.values())); kch = max(kch, sid); per = max([per] + list(cnt.values())); tw += sum(1 for c in cnt.values() if c >= 2)
        out.append((mu, kch, per, tw))
    return out
def avail(G, S):
    """per level: max over movers of AVN_x = #transitions t at which A_t(x) contains an option not in A_(t-1)(x) (fresh availability,
    R178 XI-NEW's event), and of moves_x; plus sum over the level."""
    import fastcyc
    N, lev, opts = G["N"], G["lev"], G["opts"]; d = max(lev) + 1; A = []
    for s in S:
        val, idx, _, M = fastcyc.values(G, list(s)); face = lambda v, k: val(N + idx[(v, k)])
        A.append([frozenset(k for k in range(len(opts[v])) if k == s[v] or face(v, k) > face(v, s[v])) for v in range(N)])
    out = []
    for l in range(d):
        xs = [v for v in range(N) if lev[v] == l]
        avn = {x: sum(1 for t in range(1, len(S)) if A[t][x] - A[t - 1][x]) for x in xs}
        mv = {x: sum(1 for t in range(1, len(S)) if S[t][x] != S[t - 1][x]) for x in xs}
        out.append((max(avn.values()), sum(avn.values()), max(mv.values()), sum(mv.values())))
    return out
