#!/usr/bin/env python3
"""Box 25: find a state with σ|Z, τ unchanged across the transition and θ ◁ w (planted above part, random starts); write it out
(game + start), then greedily shrink (drop edges / vertices) keeping the property. Usage: abovefind.py m k seed out"""
from common import *
from propz import reach
def prop(g, start):
    try:
        o = odd_choice(g)
    except IndexError: return False
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) != 1 or any(not s for s in g.succ): return False
    Y = split(g, o); Z = set(range(g.n)) - Y | reach(g, o); ZE = [v for v in Z if g.owner[v] == 0]
    try: st, _ = trace(g, start, check=False, cap=500)
    except Exception: return False
    E = Engine(g)
    for j in range(len(st) - 1):
        if all(st[j + 1][0][v] == st[j][0][v] for v in ZE) and st[j + 1][1] == st[j][1]:
            Xi, _ = E.evaluate(st[j][0]); _, W = wvals(g, *st[j])
            if E.key(Xi[o]) != E.key(W[o]): return j
    return False
def write(g, start, out):
    open(out + ".pg", "w").write(f"parity {g.n-1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[0].items())) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(start[1].items())) + "\n")
if __name__ == "__main__":
    m, k, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        c = rand_c1o(rng, m, m, forced=0.1)
        if c is None: continue
        n = m + k; prio = list(c.prio) + [rng.randrange(n + 3) for _ in range(k)]; owner = list(c.owner) + [0] * k
        succ = [list(s) for s in c.succ] + [sorted(set(rng.sample(range(n), rng.choice((1, 2, 3))))) for _ in range(k)]
        for v in range(m, n):
            if not any(w < m for w in succ[v]): succ[v] = sorted(set(succ[v] + [rng.randrange(m)]))
        g = pg.Game(prio, owner, succ)
        start = ({v: rng.choice(succ[v]) for v in range(n) if owner[v] == 0}, {v: rng.choice(succ[v]) for v in range(n) if owner[v] == 1})
        if prop(g, start) is not False: break
    changed = True
    while changed:                                  # shrink: remove edges not used by the start, then vertices
        changed = False
        for v in range(g.n):
            for w in list(g.succ[v]):
                if len(g.succ[v]) < 2: break
                used = start[0].get(v) == w or start[1].get(v) == w
                if used: continue
                s2 = [list(s) for s in g.succ]; s2[v].remove(w); g2 = pg.Game(list(g.prio), list(g.owner), s2)
                if prop(g2, start) is not False: g = g2; changed = True
        for x in range(g.n - 1, -1, -1):
            keep = [v for v in range(g.n) if v != x]; idx = {v: i for i, v in enumerate(keep)}
            s2 = [[idx[w] for w in g.succ[v] if w != x] for v in keep]
            st2 = ({idx[v]: idx[w] for v, w in start[0].items() if v != x and w != x}, {idx[v]: idx[w] for v, w in start[1].items() if v != x and w != x})
            if any(not s for s in s2): continue
            g2 = pg.Game([g.prio[v] for v in keep], [g.owner[v] for v in keep], s2)
            for v in range(g2.n):
                if v not in st2[0] and g2.owner[v] == 0: st2[0][v] = s2[v][0]
                if v not in st2[1] and g2.owner[v] == 1: st2[1][v] = s2[v][0]
            if prop(g2, st2) is not False: g, start = g2, st2; changed = True; break
    write(g, start, out); print("n", g.n, "state", prop(g, start), out)
