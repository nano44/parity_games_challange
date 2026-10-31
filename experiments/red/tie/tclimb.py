#!/usr/bin/env python3
"""L-RED R152: hill-climb toward a long TIE ping-pong: score = (max W-flat re-entries of one Even X not in C in one W-run (o1.py maxX),
W-flat re-entries in total, longest W-run). Mutations as casc/ovclimb.py (redirect / add / drop an edge, swap two priorities, flip an
owner, change a start choice; n fixed; env PAD=k adds k spare Even self-loop vertices). In-process n5b SPEC (xcn.trace).
Writes the best to OUT.pg / OUT.start. Usage: tclimb.py SEED.pg SEED.start RNG SECONDS OUT"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn")); sys.path.insert(0, HERE)
import xcn, o1
pg = xcn.pg; n5b = xcn.n5b
g0 = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g0); rng = random.Random(int(sys.argv[3])); T = float(sys.argv[4]); out = sys.argv[5]
PAD = int(os.environ.get('PAD', '0')); n = g0.n + PAD
def write(st, p):
    pr, ow, succ, st0 = st
    with open(p + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, succ[v]))};\n")
    with open(p + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{st0[v]}" for v in range(n) if ow[v] == 1) + "\n")
def score(st):
    pr, ow, succ, st0 = st
    try:
        g = pg.Game(list(pr), list(ow), [list(s) for s in succ])
        s = [st0[v] if ow[v] == 0 else -1 for v in range(n)]; t = [st0[v] if ow[v] == 1 else -1 for v in range(n)]
        tr, fb = xcn.trace(g, s, t, cap=400); reent, viol, maxL = o1.o1(g, tr, fb)
    except Exception: return (0, 0, 0)
    per = {}
    for v in viol:
        if v[6][0] != v[2]: per[(v[0], v[2])] = per.get((v[0], v[2]), 0) + 1
    return (max(per.values(), default=0), sum(per.values()), maxL)
def mut(st):
    pr, ow, succ, st0 = list(st[0]), list(st[1]), [list(s) for s in st[2]], list(st[3])
    for _ in range(rng.randint(1, 2)):
        c = rng.randrange(6); v = rng.randrange(n)
        if c == 0: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
        elif c == 1 and len(succ[v]) < 4: succ[v].append(rng.randrange(n))
        elif c == 2 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
        elif c == 3: w = rng.randrange(n); pr[v], pr[w] = pr[w], pr[v]
        elif c == 4: ow[v] ^= 1
        else: st0[v] = rng.choice(succ[v])
        succ[v] = sorted(set(succ[v]))
    for v in range(n):
        if st0[v] not in succ[v]: st0[v] = rng.choice(succ[v])
    return [pr, ow, succ, st0]
cur = [list(g0.prio) + [0] * PAD, list(g0.owner) + [0] * PAD, [sorted(set(s)) for s in g0.succ] + [[g0.n + i] for i in range(PAD)],
       [s0[v] if g0.owner[v] == 0 else t0[v] for v in range(g0.n)] + [g0.n + i for i in range(PAD)]]
cs = score(cur); print("seed", cs, flush=True); bs = cs; t1 = time.time(); it = 0
while time.time() - t1 < T:
    it += 1; nx = mut(cur); ns = score(nx)
    if ns >= cs:
        cur, cs = nx, ns
        if cs > bs: bs = cs; write(cur, out); print(f"step {it} best {bs}", flush=True)
print("steps", it, "best", bs)
