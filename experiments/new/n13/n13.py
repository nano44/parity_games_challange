#!/usr/bin/env python3
"""N13 SEESAW engine (L-NEW successor 78, 2026-11-14).  docs/new/N13-proposal.md has the pseudocode this file implements.

The parity game is read as a mean-payoff game: Even = Max, Odd = Min, every edge leaving v has weight (-1)^p (n+1)^p, p = the
compressed priority of v (order and parity preserved).  A potential phi changes weights to w(v) + phi(u) - phi(v); this never changes
a winner (P. Ohlmann, arXiv 2110.04533v1, Theorem 3, first item).  Loop on the remaining subgame X:
  1. sign partition (2110.04533v1 Section 3): N* = vertices from which Min forces the first non-zero weight to be negative
     (Min-attractor, along weight-0 edges, of the vertices whose forced first step is negative); P* = X - N*.
  2. first-exit values of both zones (lane step): g+(v), v in P*: what Max can force as the sum of the weights seen while the play
     stays in P* on edges of weight >= 0, until it leaves P* on such an edge (the edge is counted) or Max stops (allowed at a Max
     vertex with a negative edge); Min minimises.  One game-Dijkstra on non-negative integers.  g- on N* is the mirror image.
  3. vertices with infinite value form a reduced trap: Max (Min) keeps edges of weight >= 0 (<= 0) inside it for ever, so it is a
     dominion with that strategy (no zero cycle); it is removed with its attractor and the loop restarts.
  4. otherwise JUMP: phi += g+ on P* (turn +1) or phi -= g- on N* (turn -1); the other zone is next (mode alt+ starts with P*).
Output: winning regions and positional strategies.  Counters: jumps, peels, work (edge visits + heap pushes), maxbits (largest bit
length of a potential), wbits (largest weight).  Modes for controls: alt+ (the candidate), alt-, plus, minus, both.
Termination of the alternation is NOT proved: --cap bounds the number of jumps (status CAP).

usage: n13.py [--mode alt+|alt-|plus|minus|both] [--cap K] [--sol FILE] game.pg
"""
import sys
import heapq


def read_pg(path):
    owner, pr, succ = {}, {}, {}
    for line in open(path):
        line = line.strip()
        if not line or not line[0].isdigit():
            continue
        p = line.rstrip(';').split()
        v = int(p[0]); pr[v] = int(p[1]); owner[v] = int(p[2]); succ[v] = [int(x) for x in p[3].split(',')]
    ids = sorted(owner)
    idx = {v: i for i, v in enumerate(ids)}
    return len(ids), [owner[v] for v in ids], [pr[v] for v in ids], [sorted(set(idx[u] for u in succ[v])) for v in ids], ids


def compress(pr):
    out, cur = {}, -1
    for p in sorted(set(pr)):
        cur += 1
        if cur % 2 != p % 2:
            cur += 1
        out[p] = cur
    return [out[p] for p in pr]


class Result:
    pass


def solve(n, owner, pr, succ, mode='alt+', cap=10 ** 7, trace=None):
    cpr = compress(pr)
    B = n + 1
    w0 = [(B ** p) if p % 2 == 0 else -(B ** p) for p in cpr]
    pred = [[] for _ in range(n)]
    for v in range(n):
        for u in succ[v]:
            pred[u].append(v)
    phi = [0] * n
    X = set(range(n))
    win = [None] * n
    strat = [None] * n
    R = Result()
    R.jumps = R.peels = R.work = 0
    R.maxbits = 0
    R.wbits = max(abs(x).bit_length() for x in w0)
    R.status = 'done'
    turn = -1 if mode in ('alt-', 'minus') else 1

    def attract(T, player):
        """player-attractor of T inside X, with the attractor strategy for the player's vertices outside T"""
        A = set(T); Q = list(T); cnt = {}
        while Q:
            u = Q.pop()
            for v in pred[u]:
                if v not in X or v in A:
                    continue
                R.work += 1
                if owner[v] == player:
                    A.add(v); Q.append(v); strat[v] = u
                else:
                    if v not in cnt:
                        cnt[v] = sum(1 for x in succ[v] if x in X)
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        A.add(v); Q.append(v)
        return A

    while X:
        # ---- 1. modified weights and the sign partition ----
        W = {}
        for v in X:
            base = w0[v] - phi[v]
            W[v] = [(u, base + phi[u]) for u in succ[v] if u in X]
            R.work += len(succ[v])
        inN = set(); cnt = {}; Q = []
        for v in X:
            if owner[v] == 1:
                if any(w < 0 for _, w in W[v]):
                    inN.add(v); Q.append(v)
            else:
                if all(w < 0 for _, w in W[v]):
                    inN.add(v); Q.append(v)
                elif all(w <= 0 for _, w in W[v]):
                    cnt[v] = sum(1 for _, w in W[v] if w == 0)
        zp = {}
        for v in X:
            if v in inN:
                continue
            for u, w in W[v]:
                if w == 0:
                    zp.setdefault(u, []).append(v)
        while Q:
            u = Q.pop()
            for v in zp.get(u, ()):
                if v in inN:
                    continue
                if owner[v] == 1:
                    inN.add(v); Q.append(v)          # a Min vertex without a < 0 edge and with a 0 edge into N*
                elif cnt.get(v, 0) > 0:
                    cnt[v] -= 1
                    if cnt[v] == 0:
                        inN.add(v); Q.append(v)      # a Max vertex without a > 0 edge all of whose 0 edges lead into N*
        Pst = X - inN

        # ---- 2. first-exit values of a zone: s = +1 the zone P* (mover Max), s = -1 the zone N* (mover Min) ----
        def first_exit(s):
            Zs = Pst if s == 1 else inN
            mover = 0 if s == 1 else 1
            g = {}; heap = []; tent = {}; rem = {}; best = {}; ipred = {}
            for v in Zs:
                if owner[v] == mover:
                    b = None; r = 0; hasneg = False
                    for u, w in W[v]:
                        ew = s * w
                        if ew < 0:
                            hasneg = True
                        elif u in Zs:
                            r += 1; ipred.setdefault(u, []).append((v, ew))
                        elif b is None or ew > b:
                            b = ew                    # leave the zone on an edge of weight >= 0
                    if hasneg and b is None:
                        b = 0                         # stop
                    best[v] = b; rem[v] = r
                    if r == 0:
                        tent[v] = b; heapq.heappush(heap, (b, v)); R.work += 1
                else:
                    t = None
                    for u, w in W[v]:
                        ew = s * w                    # >= 0 for every edge of an opponent vertex of the zone
                        if u in Zs:
                            ipred.setdefault(u, []).append((v, ew))
                        elif t is None or ew < t:
                            t = ew
                    if t is not None:
                        tent[v] = t; heapq.heappush(heap, (t, v)); R.work += 1
            while heap:
                x, v = heapq.heappop(heap)
                if v in g or tent.get(v) != x:
                    continue
                g[v] = x
                for (p, ew) in ipred.get(v, ()):
                    if p in g:
                        continue
                    c = ew + x
                    if owner[p] == mover:
                        if best[p] is None or c > best[p]:
                            best[p] = c
                        rem[p] -= 1
                        if rem[p] == 0:
                            tent[p] = best[p]; heapq.heappush(heap, (best[p], p)); R.work += 1
                    elif p not in tent or c < tent[p]:
                        tent[p] = c; heapq.heappush(heap, (c, p)); R.work += 1
            return g, Zs - set(g)

        gp, trap_p = first_exit(1)
        gm, trap_m = first_exit(-1)

        # ---- 3. reduced traps: dominions with their strategies ----
        if trap_p or trap_m:
            for s, T, player in ((1, trap_p, 0), (-1, trap_m, 1)):
                if not T:
                    continue
                for v in T:
                    if owner[v] == player:
                        strat[v] = min(u for u, w in W[v] if u in T and s * w >= 0)
                A = attract(T, player)
                for v in A:
                    win[v] = player
                X -= A
                R.peels += 1
            if trace is not None:
                trace.append(('peel', len(trap_p), len(trap_m), len(X)))
            continue

        # ---- 4. jump ----
        if mode == 'both':
            sides = (1, -1)
        elif mode == 'plus':
            sides = (1,)
        elif mode == 'minus':
            sides = (-1,)
        else:
            sides = (turn,); turn = -turn
        for s in sides:
            for v, x in (gp if s == 1 else gm).items():
                phi[v] += s * x
                b = abs(phi[v]).bit_length()
                if b > R.maxbits:
                    R.maxbits = b
        R.jumps += 1
        if trace is not None:
            trace.append(('jump', sides, len(Pst), len(inN)))
        if R.jumps >= cap:
            R.status = 'CAP'
            break
    R.win = win; R.strat = strat; R.phi = phi
    return R


def main():
    args = sys.argv[1:]
    mode = 'alt+'; cap = 10 ** 7; sol = None
    while args and args[0].startswith('--'):
        if args[0] == '--mode': mode = args[1]
        elif args[0] == '--cap': cap = int(args[1])
        elif args[0] == '--sol': sol = args[1]
        args = args[2:]
    n, owner, pr, succ, ids = read_pg(args[0])
    R = solve(n, owner, pr, succ, mode, cap)
    print('n %d m %d d %d jumps %d peels %d work %d maxbits %d wbits %d WE %d %s' % (n, sum(map(len, succ)), len(set(pr)), R.jumps,
          R.peels, R.work, R.maxbits, R.wbits, sum(1 for x in R.win if x == 0), R.status))
    if sol and R.status == 'done':
        with open(sol, 'w') as f:
            f.write('paritysol %d;\n' % max(ids))
            for v in range(n):
                if owner[v] == R.win[v]:
                    f.write('%d %d %d;\n' % (ids[v], R.win[v], ids[R.strat[v]]))
                else:
                    f.write('%d %d;\n' % (ids[v], R.win[v]))


if __name__ == '__main__':
    main()
