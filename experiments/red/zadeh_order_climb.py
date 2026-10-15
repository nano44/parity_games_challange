#!/usr/bin/env python3
"""Hill-climb over INDEX orders (vertex numberings) for Zadeh's rule with the exp-game start (L-RED, R7). An index order is
lexicographic in (v, w) by vertex index; a numbering is a permutation of the Even vertices plus the order of each one's
successors. Score = number of switches of Zadeh (least occurrence record, ties by the order) from the exp-game start
(zadeh_lb.py). Usage: zadeh_order_climb.py game.pg [--steps 2000] [--restarts 5] [--seed 0] [--lb] [--out best.pg]  (--lb: start the climb
from PGSolver's identity numbering)"""
import sys, os, random, time, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
path = sys.argv[1]; arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
steps, restarts, seed = arg("--steps", 2000), arg("--restarts", 5), arg("--seed", 0); rng = random.Random(seed)
prio, owner, succ = vj.read_pg(path); e = vj.VJ(prio, owner, succ); n_v = len(prio)
lab = {}
for line in open(path):
    mm = re.match(r'^(\d+)\s+\d+\s+[01]\s+[\d,]+\s*(?:"([^"]*)")?', line.strip())
    if mm: lab[int(mm.group(1))] = mm.group(2) or mm.group(1)
byname = {lab[v]: v for v in range(n_v)}; find = byname.get
parse = lambda v: (lab[v][0], int(lab[v][1:])) if len(lab[v]) > 1 and lab[v][1:].isdigit() else (lab[v][0], 0)
n = 0
while find(f"E{n}") is not None: n += 1
sigma0 = list(e.initial("best"))
for v in range(n_v):
    if owner[v] == 0 and len(succ[v]) >= 2:
        c, j = parse(v)
        t = {"a": f"o{j}", "b": f"p{j}", "v": f"r{j}", "w": f"q{j}", "o": "m1", "p": "m1", "q": "m1", "r": "m1", "d": f"E{j}",
             "g": f"c{j}", "s": "m0", "m": (f"m{j + 1}" if j < n - 1 else "Y")}.get(c)
        if t and find(t) is not None and find(t) in succ[v]: sigma0[v] = find(t)
sigma0 = tuple(sigma0)
evens = [v for v in range(n_v) if owner[v] == 0 and len(succ[v]) >= 2]


def run(pos):
    """pos[v] = index of vertex v in the numbering; returns the switch count"""
    sigma = sigma0; occ = {}; it = 0
    while True:
        val, _ = e.evaluate(sigma); imp = e.improving(sigma, val)
        if not imp: return it
        m = min(occ.get(x, 0) for x in imp)
        v, w = min((x for x in imp if occ.get(x, 0) == m), key=lambda x: (pos[x[0]], pos[x[1]]))
        occ[(v, w)] = m + 1; s = list(sigma); s[v] = w; sigma = tuple(s); it += 1


def mutate(pos):
    q = list(pos)
    if rng.random() < 0.5:
        a, b = rng.sample(range(n_v), 2); q[a], q[b] = q[b], q[a]
    else:
        v = rng.choice(evens); a, b = rng.sample(succ[v], 2); q[a], q[b] = q[b], q[a]
    return q


t0 = time.time(); overall = (0, None)
for r in range(restarts):
    pos = list(range(n_v)) if ("--lb" in sys.argv and r == 0) else rng.sample(range(n_v), n_v)
    cur = run(pos)
    for _ in range(steps):
        q = mutate(pos); sc = run(q)
        if sc >= cur: pos, cur = q, sc
    print(f"restart {r}: {cur}", flush=True)
    if cur > overall[0]: overall = (cur, pos)
if "--out" in sys.argv and overall[1] is not None:       # write the renumbered game (vertex v gets id pos[v])
    pos = overall[1]; inv = sorted(range(n_v), key=lambda v: pos[v])
    with open(sys.argv[sys.argv.index("--out") + 1], "w") as f:
        f.write(f"parity {n_v - 1};\n")
        for v in inv:
            f.write(f"{pos[v]} {prio[v]} {owner[v]} {','.join(str(pos[w]) for w in sorted(succ[v], key=lambda w: pos[w]))} \"{lab[v]}\";\n")
print(f"{os.path.basename(path)}: identity numbering {run(list(range(n_v)))}, best index order found {overall[0]} "
      f"({restarts} restarts x {steps} steps, {time.time() - t0:.0f}s)")
