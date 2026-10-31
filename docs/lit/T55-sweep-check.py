#!/usr/bin/env python3
"""L-LIT T55 (docs/lit/T55-lexbfs-sweeps.md §3): is SPEC S1's EVEN-branch choice inside a W-constant interval a LexBFS sweep, and are the
successive sweeps LBFS+-type? W-runs / W-flat transitions as in docs/lit/T54-tiebreak-check.py (l-si gate.py).
At a W-flat transition k -> k+1, for every even W-cycle node c with a switched Even vertex: T_k := the W-tight arena graph on
{x : lambda_W(x) = c} (Even x: tight edges of {sigma_k(x)} u Isigma_k(x); Odd x: tau(x)); searches run from c over REVERSE edges.
  S1   : plain BFS, layer by layer, undiscovered predecessors appended in increasing index (SPEC S1 (iv); T54 LEX-BFS). choice(x) := the
         tight arena successor of x that is earliest in the search order.
  LEX  : LexBFS (Rose-Tarjan-Lueker) on the same reverse graph: label(z) = visit positions of the already-visited tight successors of z,
         ascending; next vertex = the unvisited z with the lexicographically smallest label+(inf,) (earlier neighbour wins, longer label wins
         on a prefix tie); equal labels by smallest index. choice(x) as above.
  PLUS : BFS as S1, but siblings (same discoverer) are appended in DECREASING position of the previous sweep (the '+' rule: the vertex
         that is last in the previous order goes first); previous sweep := S1's order of the tight tree of sigma_k (its key order).
Counts over Even x with lambda_W(x) = c, x != c: S1_BAD (S1 choice != sigma_{k+1}(x); must be 0), LEX_DIFF, PLUS_DIFF (choice !=
sigma_{k+1}(x)); ORD_LEX / ORD_PLUS: transitions at which the full search order differs from S1's. WIT prints the first witness of each.
Usage (repo root): python3 -I docs/lit/T55-sweep-check.py GAME.pg [START]   (WIT=1 in the environment prints witnesses)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
INF = float('inf')

def run(g, start=None, wit=False):
    n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g)); WE = {}
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    def W(s, t):
        if t not in WE:
            WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        return WE[t].evaluate(s)[0]
    def tight(w, v, e):
        return (w[e][0] == v and w[e][1] == 0) if w[v][0] == v else E.extend(v, w[e]) == w[v]
    def bfs(c, comp, succ, sib):
        pred = {x: [] for x in comp}
        for z in comp:
            for x in succ[z]:
                if x in pred: pred[x].append(z)
        order, pos, layer = [c], {c: 0}, [c]
        while layer:
            nxt = []
            for x in layer:
                new = [z for z in pred[x] if z not in pos]
                for z in sib(new):
                    pos[z] = len(order); order.append(z); nxt.append(z)
            layer = nxt
        return order, pos
    def lexbfs(c, comp, succ):
        pred = {x: [] for x in comp}
        for z in comp:
            for x in succ[z]:
                if x in pred: pred[x].append(z)
        lab = {z: [] for z in comp}; order, pos = [c], {c: 0}
        for z in pred[c]: lab[z].append(0)
        while True:
            cand = [z for z in comp if z not in pos and lab[z]]
            if not cand: break
            z = min(cand, key=lambda z: (tuple(lab[z]) + (INF,), z))
            pos[z] = len(order); order.append(z)
            for y in pred[z]:
                if y not in pos: lab[y].append(pos[z])
        return order, pos
    def choice(succ, pos, x):
        return min((y for y in succ[x] if y in pos), key=lambda y: pos[y])
    c_ = {k: 0 for k in ['NFLAT', 'NEV', 'S1_BAD', 'LEX_DIFF', 'PLUS_DIFF', 'ORD_LEX', 'ORD_PLUS', 'TR']}
    seen = set()
    w = W(s, t)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, Is, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        if nt != t or ns == s or fb:
            s, t = ns, nt; w = W(s, t); continue
        w1 = W(ns, t)
        if w1 != w:
            s, w = ns, w1; continue
        c_['NFLAT'] += 1; c_['TR'] += 1
        arena = {}
        for (x, e) in Is: arena.setdefault(x, set()).add(e)
        cs = {w[v][0] for v in range(n) if own[v] == 0 and ns[v] != s[v] and w[v][0] != v and E.par[w[v][0]] == 0}
        for c in cs:
            comp = {x for x in range(n) if w[x][0] == c}
            succ = {x: ([] if x == c else sorted(e for e in (arena.get(x, set()) | {s[x]}) if tight(w, x, e)) if own[x] == 0
                        else [t[x]]) for x in comp}
            prevsucc = {x: ([] if x == c else [s[x]] if own[x] == 0 else [t[x]]) for x in comp}
            _, ppos = bfs(c, comp, prevsucc, sorted)
            o1, p1 = bfs(c, comp, succ, sorted)
            ol, pl = lexbfs(c, comp, succ)
            op, pp = bfs(c, comp, succ, lambda new: sorted(new, key=lambda z: -ppos.get(z, -1)))
            if ol != o1: c_['ORD_LEX'] += 1
            if op != o1: c_['ORD_PLUS'] += 1
            for x in comp:
                if own[x] != 0 or x == c or not succ[x]: continue
                c_['NEV'] += 1
                for name, p in (('S1_BAD', p1), ('LEX_DIFF', pl), ('PLUS_DIFF', pp)):
                    if choice(succ, p, x) != ns[x]:
                        c_[name] += 1
                        if wit and name not in seen:
                            seen.add(name)
                            print(f"WIT {name} transition {c_['TR']} c {c} x {x} sigma_k {s[x]} sigma_k+1 {ns[x]} "
                                  f"choice {choice(succ, p, x)} tight-arena {succ[x]} S1-order {o1} other-order "
                                  f"{ol if name == 'LEX_DIFF' else op}")
        s = ns
    return c_

if __name__ == '__main__':
    a = sys.argv[1:]; g = load(a[0]); c = run(g, readstart(a[1]) if len(a) > 1 else None, os.environ.get('WIT') == '1')
    print(f"T55 {os.path.basename(a[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
