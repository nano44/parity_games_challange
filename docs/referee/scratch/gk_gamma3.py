#!/usr/bin/env python3
"""REFEREE successor 35: Gamma(G) and Gamma3(G) built from the packets' text only (docs/red/P-N5-REALIZE.md §3.1 for Gamma(G),
docs/new/P-N5-REACH.md §3 for the pads). No lane builder is imported. Genome format: gk_ideal.py.
build3(G) returns (prio, owner, succ, names, idx) with idx a dict of the named vertices; standard(G, idx, s) the standard state
of Gamma3 for a mover state s (P-N5-REACH §3 «Transport»)."""


def build3(G):
    N = G['N']; lev = G['lev']; deg = G['deg']
    opts = [(x, k) for x in range(N) for k in range(deg[x])]          # option order = (x, k) order
    M = len(opts)
    gate = {(x, k): G['gate'][x][k] for (x, k) in opts}
    bygate = sorted(opts, key=lambda o: gate[o])                       # gate-index order
    n0 = N + 3 * M + 6
    prio = [None] * n0; owner = [None] * n0; succ = [None] * n0; names = [None] * n0
    idx = {}
    # movers: index x, Even, priority 0, edges to its gates
    for x in range(N):
        idx[('x', x)] = x
    # gates g = (x, k): index N + gate(x, k), Odd, priority 1, edges {e_g, beta_g}
    for o in opts:
        idx[('g', o)] = N + gate[o]
    # beta_g: indices N + M, ... (options in (x, k) order), Even, priority 6 + 2 br(b(g)) + bp(b(g))
    for i, o in enumerate(opts):
        idx[('b', o)] = N + M + i
    # e_g: indices N + 2M, ... allocated in GATE-INDEX order
    for i, o in enumerate(bygate):
        idx[('e', o)] = N + 2 * M + i
    cX = N + 3 * M; cW = N + 3 * M + 1
    K0, K1, K2, K3 = N + 3 * M + 2, N + 3 * M + 3, N + 3 * M + 4, N + 3 * M + 5
    idx.update({'cX': cX, 'cW': cW, 'K0': K0, 'K1': K1, 'K2': K2, 'K3': K3})
    u = K0
    for x in range(N):
        v = idx[('x', x)]; prio[v] = 0; owner[v] = 0; names[v] = 'x%d' % x
        succ[v] = [idx[('g', (x, k))] for k in range(deg[x])]
    bmax = 0
    for o in opts:
        x, k = o
        v = idx[('g', o)]; prio[v] = 1; owner[v] = 1; names[v] = 'g%d.%d' % o
        succ[v] = [idx[('e', o)], idx[('b', o)]]
        b = G['bid'][x][k]
        v = idx[('b', o)]; prio[v] = 6 + 2 * G['br'][b] + G['bp'][b]; owner[v] = 0; names[v] = 'beta%d.%d' % o
        t = G['xt'][x][k]
        succ[v] = [u] if t == 'X' else [idx[('x', t)], u]
        bmax = max(bmax, prio[v])
    eb = bmax + 1
    while eb % 2: eb += 1                                              # the least even number > bmax
    order_e = sorted(opts, key=lambda o: (lev[o[0]], gate[o]))         # position i in the order (lev(owner), gate index)
    for i, o in enumerate(order_e):
        x, k = o
        v = idx[('e', o)]; prio[v] = eb + 2 * i; owner[v] = 0; names[v] = 'e%d.%d' % o
        succ[v] = [cW] if lev[x] == 0 else [idx[('x', G['wt'][x][k])]]
    prio[cX] = 2; owner[cX] = 0; succ[cX] = [cX]; names[cX] = 'cX'
    sofar = max(p for p in prio if p is not None)
    top = sofar + 2
    while top % 2: top += 1                                            # the least even number >= 2 + max priority so far
    prio[cW] = top; owner[cW] = 0; succ[cW] = [cW]; names[cW] = 'cW'
    prio[K0] = top + 2; owner[K0] = 0; succ[K0] = [K1, K3]; names[K0] = 'K0'
    prio[K1] = 5; owner[K1] = 0; succ[K1] = [K0, K1]; names[K1] = 'K1'
    prio[K2] = 3; owner[K2] = 1; succ[K2] = [K1, K2]; names[K2] = 'K2'
    prio[K3] = top + 3; owner[K3] = 0; succ[K3] = [K1, K2]; names[K3] = 'K3'
    assert all(p is not None for p in prio)
    idx['top'] = top; idx['n0'] = n0
    # ---- pads (P-N5-REACH §3): appended in the order pA, s, q, r, pe (gate-index order), pbeta (gate-index order),
    #      pb (option order), m (gate-index order)

    def pad(a, b, pr, name, key):
        p = len(prio)
        prio.append(pr); owner.append(0); succ.append([b]); names.append(name)
        assert b in succ[a]
        succ[a] = [p if w == b else w for w in succ[a]]
        idx[key] = p
        return p
    pad(K0, K3, 0, 'pA', 'pA')
    pad(K1, K1, 0, 's', 's')
    pad(K1, K0, 1, 'q', 'q')
    pad(K2, K1, 0, 'r', 'r')
    for o in bygate: pad(idx[('g', o)], idx[('e', o)], 1, 'pe%d.%d' % o, ('pe', o))
    for o in bygate: pad(idx[('g', o)], idx[('b', o)], 0, 'pbeta%d.%d' % o, ('pbeta', o))
    for o in opts: pad(idx[('b', o)], u, 1, 'pb%d.%d' % o, ('pb', o))
    for o in bygate: pad(idx[('x', o[0])], idx[('g', o)], 2 if o[1] == G['start'][o[0]] else 0, 'm%d.%d' % o, ('m', o))
    n3 = len(prio)
    assert n3 == N + 7 * M + 10, (n3, N, M)
    idx['n3'] = n3
    return prio, owner, succ, names, idx


def build3_revE(G):
    """FIRING CONTROL: Gamma3(G) with the e-vertices' indices in REVERSED gate order (the failing construction of
    P-N5-REALIZE fixes entry 2). Same game up to the relabelling of the e-vertices; the root-first keys then order the options the
    other way round, so the real run must leave the IDEAL run."""
    prio, owner, succ, names, idx = build3(G)
    N = G['N']; M = sum(G['deg']); n = len(prio)
    perm = list(range(n))
    for i in range(M): perm[N + 2 * M + i] = N + 2 * M + (M - 1 - i)
    inv = [0] * n
    for a, b in enumerate(perm): inv[b] = a
    prio2 = [prio[inv[v]] for v in range(n)]; owner2 = [owner[inv[v]] for v in range(n)]; names2 = [names[inv[v]] for v in range(n)]
    succ2 = [[perm[w] for w in succ[inv[v]]] for v in range(n)]
    idx2 = {key: (perm[val] if key not in ('top', 'n0', 'n3') else val) for key, val in idx.items()}
    return prio2, owner2, succ2, names2, idx2


def standard(G, idx, s, n3):
    """the standard state of Gamma3 for the mover state s: sigma on Even vertices, tau on Odd vertices (None elsewhere)."""
    N = G['N']; deg = G['deg']
    sig = [None] * n3; tau = [None] * n3
    for x in range(N): sig[x] = idx[('m', (x, s[x]))]
    for x in range(N):
        for k in range(deg[x]):
            o = (x, k)
            t = G['xt'][x][k]
            sig[idx[('b', o)]] = idx[('pb', o)] if t == 'X' else idx[('x', t)]
            tau[idx[('g', o)]] = idx[('pe', o)]
    sig[idx['K0']] = idx['pA']; sig[idx['K1']] = idx['s']; sig[idx['K3']] = idx['K2']
    tau[idx['K2']] = idx['K2']
    return sig, tau


def write_pg(path, prio, owner, succ, names):
    with open(path, 'w') as f:
        f.write('parity %d;\n' % (len(prio) - 1))
        for v in range(len(prio)):
            f.write('%d %d %d %s "%s";\n' % (v, prio[v], owner[v], ','.join(str(w) for w in succ[v]), names[v]))
