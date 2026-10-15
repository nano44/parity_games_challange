#!/usr/bin/env python3
"""Family search (falsification step 3b, structured): hill-climb over gadget TEMPLATES, each instantiated as a chain of k
copies plus a 1-sink, scoring the iteration count at k = K; the best template is then swept over k = 2..KMAX to read the
growth.  Template: G vertices with owner, priority offset in 2..2G+1, intra-copy edges, edges to the next copy, edges to the
sink.  Copy i gets priorities offset + 2G·i (ascending with i; --desc reverses), so copies are ordered by relevance.
Usage: famsearch.py RULE [--G 4] [--K 7] [--kmax 10] [--restarts 30] [--steps 2000] [--samples 1] [--seed 0] [--desc] [--budget S]"""
import sys, os, random, argparse, time, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, si

ap = argparse.ArgumentParser()
ap.add_argument("rule"); ap.add_argument("--G", type=int, default=4); ap.add_argument("--K", type=int, default=7)
ap.add_argument("--kmax", type=int, default=10); ap.add_argument("--restarts", type=int, default=30); ap.add_argument("--steps", type=int, default=2000)
ap.add_argument("--samples", type=int, default=1); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--desc", action="store_true")
ap.add_argument("--budget", type=float, default=1e9); ap.add_argument("--tag", default="")
ap.add_argument("--seed-template", default="", help="dlmm: start every restart from the DLMM Bland counter level (a Even, b Odd) plus random extra vertices")
a = ap.parse_args()
G = a.G


def instantiate(t, k):
    """t: dict(owner[G], off[G], intra[G] list of targets, nxt[G] list of targets in the next copy, sink[G] bool)."""
    n = 1 + G * k
    prio = [1]; owner = [1]; succ = [[0]]
    for i in range(k):
        for j in range(G):
            p = t["off"][j] + 2 * G * (i if not a.desc else k - 1 - i)
            s = {1 + G * i + l for l in t["intra"][j]}
            if i + 1 < k:
                s |= {1 + G * (i + 1) + l for l in t["nxt"][j]}
            if t["sink"][j] or not s:
                s.add(0)
            prio.append(p); owner.append(t["owner"][j]); succ.append(sorted(s))
    return pg.Game(prio, owner, succ)


def score(t, k=None):
    k = k or a.K
    g = instantiate(t, k)
    tot = 0
    for s in range(a.samples):
        tot += si.solve(g, a.rule, seed=s)[2]
    return tot / a.samples


def rand_template(rng):
    t = _rand_template(rng)
    if a.seed_template == "dlmm" and G >= 2:
        t["owner"][0], t["owner"][1] = 0, 1; t["off"][0], t["off"][1] = 3, 4
        t["intra"][0], t["intra"][1] = [], []; t["nxt"][0], t["nxt"][1] = [0, 1], [0, 1]; t["sink"][0] = t["sink"][1] = False
    return t


def _rand_template(rng):
    return {"owner": [rng.randrange(2) for _ in range(G)], "off": [rng.randrange(2, 2 * G + 2) for _ in range(G)],
            "intra": [sorted(rng.sample(range(G), rng.randint(0, 2))) for _ in range(G)],
            "nxt": [sorted(rng.sample(range(G), rng.randint(0, 1))) for _ in range(G)],
            "sink": [rng.random() < 0.4 for _ in range(G)]}


def mutate(t, rng):
    t = json.loads(json.dumps(t)); j = rng.randrange(G); k = rng.randrange(6)
    if k == 0: t["owner"][j] ^= 1
    elif k == 1: t["off"][j] = rng.randrange(2, 2 * G + 2)
    elif k == 2:
        l = rng.randrange(G)
        if l in t["intra"][j]: t["intra"][j].remove(l)
        else: t["intra"][j].append(l); t["intra"][j].sort()
    elif k == 3:
        l = rng.randrange(G)
        if l in t["nxt"][j]: t["nxt"][j].remove(l)
        else: t["nxt"][j].append(l); t["nxt"][j].sort()
    elif k == 4: t["sink"][j] = not t["sink"][j]
    else:
        l = rng.randrange(G); t["off"][j], t["off"][l] = t["off"][l], t["off"][j]
    return t


rng = random.Random(a.seed); t0 = time.time(); best_t, best_s = None, -1
for r in range(a.restarts):
    if time.time() - t0 > a.budget: break
    t = rand_template(rng); s = score(t)
    for step in range(a.steps):
        t2 = mutate(t, rng); s2 = score(t2)
        if s2 >= s: t, s = t2, s2
    if s > best_s:
        best_t, best_s = t, s
        print(f"restart {r}: score {s} at k={a.K}", flush=True)
sweep = [(k, score(best_t, k)) for k in range(2, a.kmax + 1)]
print(f"{a.rule}{a.tag} G={G} K={a.K}: best {best_s}; sweep k->iters: " + " ".join(f"{k}:{it:g}" for k, it in sweep), flush=True)
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
json.dump(best_t, open(os.path.join(HERE, "out", f"famsearch_{a.rule}{a.tag}_G{G}.json"), "w"))
pg.write(instantiate(best_t, a.kmax), os.path.join(HERE, "out", f"famsearch_{a.rule}{a.tag}_G{G}_k{a.kmax}.pg"))
