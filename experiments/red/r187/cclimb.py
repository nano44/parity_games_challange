#!/usr/bin/env python3
"""L-RED R187 item 2: climb for up/shortcut ALTERNATION at the W-cycle node c of a CROOT game (score (alt, down, cm, L) of the best FL
run). Mutations: genome (downgen.mutacyc), c's option set, c's start. Writes OUT.json (genome + copt + cstart) at every improvement.
Usage: cclimb.py seed_genome.json iters seed OUT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import croot, downgen
G = json.load(open(sys.argv[1])); iters, seed, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
if "pi" not in G:   # R178 genomes: derive a pi consistent with their (acyclic) Xi-graph
    N = G["N"]; E = {v: {o[1] for o in G["opts"][v] if o[1] >= 0} for v in range(N)}; order = []; seen = set()
    def dfs(v):
        seen.add(v)
        for w in E[v]:
            if w not in seen: dfs(w)
        order.append(v)
    for v in range(N):
        if v not in seen: dfs(v)
    pi = [0] * N
    for i, v in enumerate(reversed(order)): pi[v] = i
    G["pi"] = pi
N = G["N"]; st = dict(G=G, copt=sorted(rng.sample(range(N), 3)), cstart=None); st["cstart"] = st["copt"][0]
def score(s):
    try:
        g, sig, tau, c = croot.build(s["G"], s["copt"], s["cstart"]); r = croot.measure(g, sig, tau, c, cap=400)
    except Exception as e:
        return (-1,), {}
    return (r["alt"], r["down"], r["cm"], r["L"]), r
best, br = score(st)
for it in range(iters):
    s = json.loads(json.dumps(st)); r = rng.random()
    if r < 0.5: s["G"] = downgen.mutacyc(s["G"], rng)
    elif r < 0.8:
        v = rng.randrange(N)
        if v in s["copt"] and len(s["copt"]) > 2: s["copt"].remove(v)
        elif v not in s["copt"]: s["copt"] = sorted(s["copt"] + [v])
        if s["cstart"] not in s["copt"]: s["cstart"] = s["copt"][0]
    else: s["cstart"] = rng.choice(s["copt"])
    sc, rr = score(s)
    if sc >= best:
        if sc > best: print("it", it, sc, rr, flush=True); json.dump(s, open(out, "w"))
        st, best, br = s, sc, rr
print("BEST", best, br)
