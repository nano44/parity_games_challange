#!/usr/bin/env python3
"""REFEREE successor 35: an IDEAL simulator written from the text of docs/red/P-N5-REALIZE.md §2 (R104's packet) only.
No lane code is imported. Genome (my own dict):
  N; lev[x]; deg[x]; wt[x][k] (mover or None); xt[x][k] (mover or 'X'); bid[x][k]; gate[x][k]; br[b]; bp[b]; start[x].
Functions: check_def (R104 §2 clause by clause), xi_acyclic, chain / bset (X-chain and its beta-id set), better (the order of
Fact X), avail, step (level by level, lexicographically least key), run (L(G), stop reason, states).
"""
import json
import sys


def from_r178_json(path):
    """loader for the lanes' JSON genomes: opts[x][k] = [wt, xt, bid] with -1 for none / X."""
    g = json.load(open(path))
    N = g['N']
    G = {'N': N, 'lev': list(g['lev']), 'deg': [len(o) for o in g['opts']],
         'wt': [[(o[0] if o[0] >= 0 else None) for o in g['opts'][x]] for x in range(N)],
         'xt': [[(o[1] if o[1] >= 0 else 'X') for o in g['opts'][x]] for x in range(N)],
         'bid': [[o[2] for o in g['opts'][x]] for x in range(N)],
         'gate': [list(r) for r in g['gate']], 'br': list(g['br']), 'bp': list(g['bp']), 'start': list(g['start'])}
    return G


def check_def(G):
    """R104 packet §2, clause by clause. Returns a list of (clause, ok, detail)."""
    out = []
    N = G['N']; lev = G['lev']; deg = G['deg']
    M = sum(deg)
    d = max(lev) + 1
    out.append(('movers x = 0..N-1, each with a level in {0..d-1}', all(isinstance(l, int) and 0 <= l < d for l in lev) and len(lev) == N,
                'N=%d d=%d levels used %s' % (N, d, sorted(set(lev)))))
    out.append(('options k = 0..deg(x)-1; M = sum deg', all(len(G['wt'][x]) == deg[x] == len(G['xt'][x]) == len(G['bid'][x]) == len(G['gate'][x]) and deg[x] >= 1 for x in range(N)),
                'M=%d degs %s' % (M, sorted(set(deg)))))
    ok = True; bad = None
    for x in range(N):
        for k in range(deg[x]):
            w = G['wt'][x][k]
            if lev[x] == 0:
                if w is not None: ok = False; bad = (x, k, w)
            else:
                if w is None or not (0 <= w < N) or lev[w] != lev[x] - 1: ok = False; bad = (x, k, w)
    out.append(('W-target: a mover of level lev(x)-1 if lev(x) >= 1, none if lev(x) = 0 (GRADED)', ok, 'first violation %s' % (bad,)))
    ok = all((t == 'X') or (isinstance(t, int) and 0 <= t < N) for x in range(N) for t in G['xt'][x])
    out.append(('Xi-target in {movers} U {X}', ok, ''))
    bids = sorted(b for x in range(N) for b in G['bid'][x])
    out.append(('beta-id b(x,k): a bijection onto 0..M-1', bids == list(range(M)), ''))
    gates = sorted(b for x in range(N) for b in G['gate'][x])
    out.append(('gate index gate(x,k): a bijection of the options onto 0..M-1', gates == list(range(M)), ''))
    out.append(('rank br(b): a bijection onto 0..M-1', sorted(G['br']) == list(range(M)) and len(G['br']) == M, ''))
    out.append(('parity bp(b) in {0,1}', len(G['bp']) == M and all(p in (0, 1) for p in G['bp']), 'parities used %s' % sorted(set(G['bp']))))
    out.append(('start s_0: an option per mover', len(G['start']) == N and all(0 <= G['start'][x] < deg[x] for x in range(N)), ''))
    return out


def xi_acyclic(G):
    """Xi-graph: edge x -> xt(x,k) for every option with xt != X; acyclic iff no cycle (self-loops count as cycles)."""
    N = G['N']
    adj = [sorted(set(t for t in G['xt'][x] if t != 'X')) for x in range(N)]
    color = [0] * N
    for r in range(N):
        if color[r]: continue
        stack = [(r, 0)]; color[r] = 1
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                stack[-1] = (v, i + 1)
                w = adj[v][i]
                if color[w] == 1: return False
                if color[w] == 0:
                    color[w] = 1; stack.append((w, 0))
            else:
                color[v] = 2; stack.pop()
    return True


def bset(G, s, x, k):
    """beta-ids of the X-chain of face (x,k) under s: (x,k), (xt, s(xt)), ... ending at the first option with Xi-target X."""
    B = set()
    seen = 0
    while True:
        B.add(G['bid'][x][k])
        t = G['xt'][x][k]
        if t == 'X': return frozenset(B)
        x, k = t, s[t]
        seen += 1
        if seen > G['N'] + 1: raise RuntimeError('X-chain does not end: Xi-cycle')


def better(G, B1, B2):
    """(x,k) |>_s (x,k') with B1 = B_s(x,k), B2 = B_s(x,k'): the beta-id of LARGEST rank in the symmetric difference has parity 0
    and lies in B1, or has parity 1 and lies in B2. (Fact X: for IDEAL-ACYC and two options of one mover the sets differ.)"""
    D = B1 ^ B2
    if not D: return False
    top = max(D, key=lambda b: G['br'][b])
    if G['bp'][top] == 0: return top in B1
    return top in B2


def avail(G, s, x):
    cur = bset(G, s, x, s[x])
    return [k for k in range(G['deg'][x]) if k == s[x] or better(G, bset(G, s, x, k), cur)]


def step(G, s):
    """one IDEAL step from s. Returns (s', reason) with reason in {'opt', 'stuck', None}."""
    N = G['N']; lev = G['lev']
    A = [avail(G, s, x) for x in range(N)]
    if all(len(a) == 1 for a in A): return list(s), 'opt'
    s2 = [None] * N
    key = {}

    def keyof(x, k):
        # key(x,k) := (gate(x,k)) if lev(x) = 0, and key_(s')(wt(x,k), s'(wt(x,k))) followed by gate(x,k) otherwise
        if lev[x] == 0: return (G['gate'][x][k],)
        w = G['wt'][x][k]
        return key[w] + (G['gate'][x][k],)
    for l in range(max(lev) + 1):
        for x in range(N):
            if lev[x] != l: continue
            ks = sorted(A[x], key=lambda k: keyof(x, k))
            assert len(set(keyof(x, k) for k in A[x])) == len(A[x])
            s2[x] = ks[0]
            key[x] = keyof(x, s2[x])
    if s2 == list(s): return s2, 'stuck'
    return s2, None


def run(G, maxsteps=10 ** 9, keep=False):
    s = list(G['start']); L = 0; states = [list(s)] if keep else None
    while True:
        s2, why = step(G, s)
        if why is not None: return L, why, states
        s = s2; L += 1
        if keep: states.append(list(s))
        if L > maxsteps: raise RuntimeError('maxsteps')


if __name__ == '__main__':
    for p in sys.argv[1:]:
        G = from_r178_json(p)
        acyc = xi_acyclic(G)
        defs = check_def(G)
        okdef = all(o for _, o, _ in defs)
        if acyc:
            L, why, _ = run(G)
            print('%s N %d M %d d %d DEF %s ACYC %s L %d stop %s' % (p.split('/')[-1], G['N'], sum(G['deg']), max(G['lev']) + 1, okdef, acyc, L, why))
        else:
            print('%s N %d M %d DEF %s ACYC False (not run)' % (p.split('/')[-1], G['N'], sum(G['deg']), okdef))
