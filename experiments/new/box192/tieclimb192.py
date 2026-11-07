#!/usr/bin/env python3
"""Box 192: hill-climb GENERAL games for SEG-T: score = max p-run along the sigma-steps of N5'-xi (box190 n5v.py mode xi), then
#sigma-steps. A genome = (prio, owner, succ). Resumable (OUT.json). Env GAP=1: score (p-run - n_E, p-run, #sigma-steps). Usage: tieclimb192.py n seed iters OUT"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190")]
import n5v
pg = n5v.pg
n, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)

def score(G):
    g = pg.Game(*G); st, fb, E = n5v.run(g, "xi", cap=5000)
    sig = [st[0][0]] + [ns for (s, _), (ns, _) in zip(st, st[1:]) if ns != s]
    ev = [E.evaluate(tuple(s)) for s in sig]; lab = ""
    for k in range(1, len(sig)):
        (pv, ps), (vs, sb) = ev[k - 1], ev[k]
        lab += "C" if any(pv[v][0] != vs[v][0] for v in range(n)) else ("R" if any(ps[v] != sb[v] for v in range(n) if g.owner[v] == 1) else "p")
    mp = max((len(r) for r in lab.replace("R", "C").split("C")), default=0)
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    if os.environ.get("GAP") == "1": return (mp - nE, mp, len(lab)), nE, lab
    return (mp, len(lab)), nE, lab

def mut(G):
    pr, ow, su = copy.deepcopy(G); v = rng.randrange(n); r = rng.random()
    if r < 0.3: pr[v] = rng.randrange(n + 1)
    elif r < 0.4: ow[v] ^= 1
    elif r < 0.7 and len(su[v]) < 4: su[v] = sorted(set(su[v]) | {rng.randrange(n)})
    elif r < 0.85 and len(su[v]) > 1: su[v].remove(rng.choice(su[v]))
    else: su[v] = sorted(set(su[v]) - {rng.choice(su[v])} | {rng.randrange(n)}) or [v]
    return [pr, ow, su]

cur = json.load(open(out + ".json")) if os.path.exists(out + ".json") else \
    [[rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(rng.sample(range(n), rng.randint(1, 3))) for _ in range(n)]]
best, nE, lab = score(cur); print("start", best, nE, lab, flush=True)
for it in range(iters):
    G = mut(cur)
    if rng.random() < 0.5: G = mut(G)
    s, nE2, lab2 = score(G)
    if s >= best:
        if s > best:
            print(f"it {it} score {s} nE {nE2} {lab2}", flush=True); json.dump(G, open(out + ".json", "w"))
            if (s[1] if os.environ.get("GAP") == "1" else s[0]) > nE2: print("SEG-T VIOLATION", flush=True); json.dump(G, open(out + "_viol.json", "w"))
        cur, best = G, s
print("final", best, flush=True)
