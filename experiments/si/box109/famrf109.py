#!/usr/bin/env python3
"""L-SI box 109: FAMILY SEARCH against a rule of n6.py (default rf), after experiments/si/famsearch.py (falsification step 3b):
hill-climb over gadget TEMPLATES; a template with G vertices is instantiated as a chain of k copies plus a 1-sink (vertex 0: Odd,
priority 1, self-loop). Template: per vertex an owner, a priority offset in 2..2G+1, edges inside the copy, edges to the NEXT copy,
edges to the PREVIOUS copy (new against famsearch.py: RF is polynomial on acyclic chains, Lemma ACYC), and a sink edge flag.
Copy i gets priorities offset + 2G*i (--desc: the reverse). Objective: iterations at k = K minus iterations at k = K - 2 (growth,
not size). The best template is swept over k = 2..KMAX.
Usage: famrf109.py [--mode rf] [--G 4] [--K 6] [--kmax 12] [--restarts 20] [--steps 1500] [--seed 0] [--desc] [--out FILE.json]"""
import sys, os, random, argparse, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ap = argparse.ArgumentParser()
ap.add_argument("--mode", default="rf"); ap.add_argument("--G", type=int, default=4); ap.add_argument("--K", type=int, default=6)
ap.add_argument("--kmax", type=int, default=12); ap.add_argument("--restarts", type=int, default=20); ap.add_argument("--steps", type=int, default=1500)
ap.add_argument("--seed", type=int, default=0); ap.add_argument("--desc", action="store_true"); ap.add_argument("--out", default="")
a = ap.parse_args(); sys.argv = [sys.argv[0]]
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, n6
G = a.G; rng = random.Random(a.seed)

def instantiate(t, k):
    prio = [1]; owner = [1]; succ = [[0]]
    for i in range(k):
        for j in range(G):
            p = t["off"][j] + 2 * G * (i if not a.desc else k - 1 - i)
            s = {1 + G * i + l for l in t["intra"][j]}
            if i + 1 < k: s |= {1 + G * (i + 1) + l for l in t["nxt"][j]}
            if i > 0: s |= {1 + G * (i - 1) + l for l in t["prv"][j]}
            if t["sink"][j] or not s: s.add(0)
            prio.append(p); owner.append(t["owner"][j]); succ.append(sorted(s))
    return pg.Game(prio, owner, succ)

def its(t, k): return n6.run(instantiate(t, k), a.mode, cap=5000)["its"]
def score(t): return its(t, a.K) - its(t, a.K - 2)
def rnd():
    return dict(owner=[rng.randrange(2) for _ in range(G)], off=rng.sample(range(2, 2 * G + 2), G),
                intra=[sorted(rng.sample(range(G), rng.randint(0, 2))) for _ in range(G)], nxt=[sorted(rng.sample(range(G), rng.randint(0, 2))) for _ in range(G)],
                prv=[sorted(rng.sample(range(G), rng.randint(0, 1))) for _ in range(G)], sink=[rng.random() < 0.3 for _ in range(G)])
def mutate(t):
    t = json.loads(json.dumps(t)); j = rng.randrange(G); k = rng.randrange(6)
    if k == 0: t["owner"][j] = 1 - t["owner"][j]
    elif k == 1:
        i = rng.randrange(G); t["off"][i], t["off"][j] = t["off"][j], t["off"][i]
    elif k == 2: t["sink"][j] = not t["sink"][j]
    else:
        key = ("intra", "nxt", "prv")[k - 3]; l = rng.randrange(G); s = set(t[key][j]); s ^= {l}
        if len(s) <= 3: t[key][j] = sorted(s)
    return t
best = (-10 ** 9, None)
for r in range(a.restarts):
    cur = rnd(); sc = score(cur)
    for _ in range(a.steps):
        c = mutate(cur); s = score(c)
        if s >= sc: cur, sc = c, s
    if sc > best[0]: best = (sc, cur)
    print(f"F109 mode {a.mode} G {G} K {a.K}{' desc' if a.desc else ''} seed {a.seed} restart {r}: growth {sc} (best {best[0]})", flush=True)
sc, t = best
sweep = [(k, its(t, k)) for k in range(2, a.kmax + 1)]
hw = [(k, n6.run(instantiate(t, k), "howard", cap=5000)["its"]) for k in range(2, min(a.kmax, 9) + 1)]
print(f"F109 mode {a.mode} G {G} K {a.K}{' desc' if a.desc else ''} seed {a.seed}: BEST growth {sc}; sweep k:iterations " + " ".join(f"{k}:{i}" for k, i in sweep) + " | howard " + " ".join(f"{k}:{i}" for k, i in hw), flush=True)
if a.out: json.dump(dict(template=t, G=G, desc=a.desc, mode=a.mode, sweep=sweep), open(a.out, "w"))
