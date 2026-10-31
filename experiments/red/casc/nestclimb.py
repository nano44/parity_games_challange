#!/usr/bin/env python3
"""L-RED R151: nesting test for cedge_n32's ping-pong loop. Game = two disjoint copies A (0..31) and B (32..63) of SEED (+ start).
Mutations act ONLY on cross edges: add an edge from a vertex of one copy to a vertex of the other, drop a cross edge, or redirect a cross
edge (start choices of touched vertices kept valid). Score = longest W-run (R89, n5b SPEC; xcn.wruns), then total iterations. If a copy's
loop could re-trigger the other's, the longest W-run would grow past the single-copy value. Writes the best to OUT.pg / OUT.start.
Usage: nestclimb.py SEED.pg SEED.start RNG STEPS OUT"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "xcn"))
import xcn
pg = xcn.pg; n5b = xcn.n5b
g0 = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g0); rng = random.Random(int(sys.argv[3])); steps = int(sys.argv[4]); out = sys.argv[5]
m = g0.n; n = 2 * m
pr = list(g0.prio) * 2; ow = list(g0.owner) * 2
base = [sorted(set(s)) for s in g0.succ] + [sorted(set(x + m for x in s)) for s in g0.succ]
st0 = [s0[v] if g0.owner[v] == 0 else t0[v] for v in range(m)]; st0 = st0 + [x + m for x in st0]
def score(cross):
    succ = [sorted(set(base[v]) | cross.get(v, set())) for v in range(n)]
    g = pg.Game(pr, ow, succ)
    try: tr, fb = xcn.trace(g, [st0[v] if ow[v] == 0 else -1 for v in range(n)], [st0[v] if ow[v] == 1 else -1 for v in range(n)], cap=2000)
    except Exception: return (0, 0)
    runs, _ = xcn.wruns(g, tr, fb)
    return (max(len(F) - 1 for F in runs), len(tr) - 1)
def mut(cross):
    c = {v: set(s) for v, s in cross.items()}
    for _ in range(rng.randint(1, 2)):
        r = rng.randrange(3); v = rng.randrange(n); other = (m if v < m else 0)
        if r == 0 or not c: c.setdefault(v, set()).add(other + rng.randrange(m))
        elif r == 1:
            u = rng.choice(list(c)); c[u].discard(rng.choice(list(c[u]))) if c[u] else None
        else:
            u = rng.choice(list(c))
            if c[u]: c[u].discard(rng.choice(list(c[u]))); c[u].add((m if u < m else 0) + rng.randrange(m))
    return {v: s for v, s in c.items() if s}
def write(cross):
    succ = [sorted(set(base[v]) | cross.get(v, set())) for v in range(n)]
    with open(out + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n")
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 1) + "\n")
cur = {}; cs = score(cur); print("union", cs, flush=True); bs = cs
for it in range(steps):
    nx = mut(cur); ns = score(nx)
    if ns >= cs:
        cur, cs = nx, ns
        if cs > bs: bs = cs; write(cur); print(f"step {it} best {bs} cross {sum(len(s) for s in cur.values())}", flush=True)
