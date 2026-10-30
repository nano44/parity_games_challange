#!/usr/bin/env python3
"""L-RED R141: inside W-constant intervals (wint.py's definition), does every switch go to a LOWER-index successor (a static list order)?
Prints switches inside intervals, how many go up (to a higher successor index) and the cycle-node parity of the switcher's W.
Usage: idxmono.py GAME.pg [START]  |  idxmono.py --rand SEED GAMES NMIN NMAX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import wint
n5b = wint.n5b
def scan(g, s0=None, t0=None):
    N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
    try: N.run(s0, t0, trace=tr, fbtrace=fb, max_iter=5000)
    except Exception: return (0, 0, [])
    Wc = {}
    def W(s, t):
        if t not in Wc: Wc[t] = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]))
        return Wc[t].evaluate(list(s))
    sw = up = 0; ups = []
    for i in range(len(tr) - 1):
        (s, t), (s2, t2) = tr[i], tr[i + 1]
        if t == t2 and not fb[i] and s != s2:
            w = W(s, t)
            if w == W(s2, t):
                for v in range(g.n):
                    if g.owner[v] == 0 and s[v] != s2[v]:
                        sw += 1
                        if s2[v] > s[v]: up += 1; ups.append((v, s[v], s2[v], g.prio[w[v][0]] % 2))
    return (sw, up, ups)
if sys.argv[1] == "--rand":
    seed, games, a, b = map(int, sys.argv[2:6]); rng = random.Random(seed); S = U = 0; par = {0: 0, 1: 0}
    for _ in range(games):
        sw, up, ups = scan(wint.rand_game(rng, rng.randint(a, b))); S += sw; U += up
        for x in ups: par[x[3]] += 1
    print(f"IDXMONO rand seed {seed} games {games} interval-switches {S} upward {U} upward-by-W-cycle-parity {par}")
else:
    g = n5b.pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    sw, up, ups = scan(g, *st); print(f"IDXMONO {os.path.basename(sys.argv[1])} interval-switches {sw} upward {up} {ups[:6]}")
