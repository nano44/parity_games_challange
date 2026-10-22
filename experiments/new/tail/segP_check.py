#!/usr/bin/env python3
"""Box 10: the two-player bridge. Along N5's run (n5_lock.step = n5.py's loop, best-reward start) on random TWO-PLAYER games, split the run
into σ̄-SEGMENTS (maximal runs of iterations with Odd's best reply σ̄ = c constant). Inside a segment Even's honest values Ξσ are the values of
σ in the one-player game G_c. Test the Lemma-P analogue (P-N5): after k Even-moving iterations of the segment with every λ (cycle node of Ξσ)
unchanged, Ξσ(x) ⪰ value of every simple path in G_c from x to any cycle node u (of the segment's first σ) with ≤ k edges. Also tests the
weaker (SEG-LEN): Even moves per λ-phase of a segment ≤ n. Prints violations with the game. Usage: segP_check.py games seed nmax [deg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5_lock import step
from n5 import Engine, dual
INST = sys.argv[1] == "inst"; FAST = os.environ.get("FAST") == "1"   # FAST: only the (SEG-LEN) consequence, no path enumeration
if INST: games, seed, nmax, deg = len(sys.argv) - 2, 0, 0, 0
else: games, seed, nmax = map(int, sys.argv[1:4]); deg = int(sys.argv[4]) if len(sys.argv) > 4 else 3
rng = random.Random(seed)
viol = checks = segs = 0; longest = (0, 0); viol_len = 0
def best_paths(g, E, c, cycnodes):
    """best[(u, x, L)] = best value of a simple path with exactly L edges from x to u in G_c (Even edges all, Odd fixed to c)."""
    succ = [list(g.succ[v]) if g.owner[v] == 0 else [c[v]] for v in range(g.n)]
    best = {}
    for u in cycnodes:
        def dfs(x, path, seen):
            for w in succ[x]:
                if w == u:
                    P = 0
                    for v in path + [x]:
                        if E.rank[v] > E.rank[u]: P |= E.bit[v]
                    val = (u, P, len(path) + 1); key = (u, path[0] if path else x, len(path) + 1)
                    if key not in best or E.key(val) > E.key(best[key][0]): best[key] = (val, path + [x, u])
                elif w not in seen: dfs(w, path + [x], seen | {w})
        for x in range(g.n):
            if x != u: dfs(x, [], {x})
    return best
for gi in range(games):
    if INST:
        g = pg.read(sys.argv[2 + gi]); n = g.n; print("instance", os.path.basename(sys.argv[2 + gi]), "n", n, flush=True)
    else:
        n = rng.randint(4, nmax); owner = [rng.randrange(2) for _ in range(n)]; pr = rng.sample(range(2 * n), n)
        succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, deg)))) for v in range(n)]
        g = pg.Game(pr, owner, succ)
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(n) if g.owner[v] == 1]
    seg_c = None; k = 0; best = None; lam0 = None; cyc = None; segmoves = 0
    while True:
        vs, sbar = E.evaluate(tuple(s)); c = tuple(sbar[v] if g.owner[v] == 1 else -1 for v in range(n)); lam = tuple(vs[v][0] for v in range(n))
        if c != seg_c or lam != lam0:          # new segment or new λ-phase inside the segment: reset
            if seg_c is not None: segs += 1
            seg_c, lam0, k = c, lam, 0; cyc = sorted(set(lam)); best = {} if FAST else best_paths(g, E, c, cyc)
        else:
            for u in cyc:
                for x in range(n):
                    for L in range(1, k + 1):
                        if (u, x, L) in best:
                            checks += 1
                            if E.key(vs[x]) < E.key(best[(u, x, L)][0]):
                                viol += 1
                                if viol <= int(os.environ.get("SHOW", "5")):
                                    val, path = best[(u, x, L)]; z = path[1]; Is = set(E.improving(tuple(s), vs))
                                    r0 = step(g, E, Ed, s, t); moved = r0 is not None and r0[0][x] != s[x]
                                    print("VIOLATION (P-N5)", dict(n=n, k=k, x=x, owner=g.owner[x], u=u, L=L, xi=vs[x], path_value=val, path=path, first_hop_honest_improving=((x, z) in Is), sigma_x=s[x], x_moves_next=moved, next_sigma_x=(r0[0][x] if r0 else None), honest_improving_at_x=sorted(w for (y, w) in Is if y == x)))
            if k > n: viol_len += 1; print("SEG-LEN violation: Even moves in one λ-phase of a segment", k, "> n", n, g.prio, g.owner, g.succ)
        r = step(g, E, Ed, s, t)
        if r is None: break
        if r[0] != s: k += 1; longest = max(longest, (k, n))
        s, t = r[0], r[1]
print(f"games={games} nmax={nmax} deg={deg} segment-phases={segs} (P-N5) checks={checks} violations={viol}; (SEG-LEN) violations={viol_len}; longest in-phase Even-move count {longest[0]} at n={longest[1]}")
