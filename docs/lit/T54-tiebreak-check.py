#!/usr/bin/env python3
"""L-LIT T54 (docs/lit/T54-stalling.md §4): what SPEC S1's tie-break does inside a W-constant interval (L-SI box 51b, INTERVAL-SI).
W-runs and W-flat transitions exactly as in l-si experiments/si/gate/gate.py (tau fixed, no fallback, W's cycle nodes fixed, W fixed).
At every W-flat transition k -> k+1, every switched Even v is put in one branch by its W-cycle node c := lambda_W(v):
  CN  : v = c (v is its own W-cycle node; SPEC S1 (v), the DFS choice);
  ODD : Omega(c) odd  (in the dual arena c is dual-even: S1 (iv) longest path, recursion, "first strict maximum" = smallest index);
  EVEN: Omega(c) even (dual-odd: S1 (iv) BFS over predecessors, first discovery).
Per branch:
  DOWN / UP     : index of sigma_{k+1}(v) below / above index of sigma_k(v).
  PMIN_OK / BAD : sigma_{k+1}(v) is / is not the smallest-index TIGHT arena edge (arena {sigma_k(v)} u Isigma_k(v); tight = in OPT_W(v)).
  PMAX_OK / BAD : the same for the largest index.
  LEX_DN / UP   : key_{k+1}(v) < / > key_k(v), key_j(v) := indices of the (sigma_j, tau)-path v = x_0 -> ... -> x_l = c read from c's
                  side: (x_{l-1}, ..., x_0), compared lexicographically (EVEN branch only; equal lengths l inside I).
  PLEX_OK / BAD : sigma_{k+1}(v) is / is not the tight arena edge y minimising key_{k+1}(y) (EVEN branch; the lex-BFS model).
  NT            : sigma_{k+1}(v) not tight (must be 0 by INTERVAL-SI (i)).
Also: FLI (max W-flat transitions in one W-constant interval), SWV (max switches of one vertex in one interval), INT (intervals with
>= 1 flat transition), NFLAT (all flat transitions). Usage (from the repo root): python3 -I docs/lit/T54-tiebreak-check.py GAME.pg [START]
Imports experiments/new/box21/n5x.py (trunk) read-only."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def run(g, start=None):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); WE = {}
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    def W(s, t):
        if t not in WE:
            WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        return WE[t].evaluate(s)[0]
    def tight(w, v, e):
        return (w[e][0] == v and w[e][1] == 0) if w[v][0] == v else E.extend(v, w[e]) == w[v]
    def key(strat, v, c):
        p, x = [], v
        while x != c and len(p) <= n:
            p.append(x); x = strat[x] if own[x] == 0 else t[x]
        return tuple(reversed(p))
    c = {k: 0 for k in ['NFLAT', 'INT', 'FLI', 'SWV', 'NT'] + [b + '_' + k for b in ('CN', 'ODD', 'EVEN')
         for k in ('DOWN', 'UP', 'PMIN_OK', 'PMIN_BAD', 'PMAX_OK', 'PMAX_BAD', 'LEX_DN', 'LEX_UP', 'PLEX_OK', 'PLEX_BAD')]}
    w = W(s, t); fli = 0; swv = {}
    def close():
        nonlocal fli, swv
        if fli: c['INT'] += 1
        c['FLI'] = max(c['FLI'], fli); c['SWV'] = max([c['SWV']] + list(swv.values())); fli = 0; swv = {}
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, Is, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        if nt != t or ns == s or fb:
            close(); s, t = ns, nt; w = W(s, t); continue
        w1 = W(ns, t)
        if w1 != w:
            close(); s, w = ns, w1; continue
        c['NFLAT'] += 1; fli += 1
        arena = {}
        for (x, e) in Is: arena.setdefault(x, set()).add(e)
        for v in range(n):
            if own[v] != 0 or ns[v] == s[v]: continue
            swv[v] = swv.get(v, 0) + 1
            cn = w[v][0]; b = 'CN' if cn == v else ('ODD' if E.par[cn] == 1 else 'EVEN')
            if not tight(w, v, ns[v]): c['NT'] += 1
            c[b + ('_DOWN' if ns[v] < s[v] else '_UP')] += 1
            tg = sorted(e for e in arena.get(v, set()) | {s[v]} if tight(w, v, e))
            c[b + ('_PMIN_OK' if tg and ns[v] == tg[0] else '_PMIN_BAD')] += 1
            c[b + ('_PMAX_OK' if tg and ns[v] == tg[-1] else '_PMAX_BAD')] += 1
            if b == 'EVEN':
                k0, k1 = key(s, v, cn), key(ns, v, cn)
                c['EVEN_LEX_DN' if k1 < k0 else 'EVEN_LEX_UP'] += 1
                best = min(tg, key=lambda y: key(ns, y, cn) if y != cn else ())
                c['EVEN_PLEX_OK' if best == ns[v] else 'EVEN_PLEX_BAD'] += 1
        s = ns
    close(); return c

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None)
    print(f"T54 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
