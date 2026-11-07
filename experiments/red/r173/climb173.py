#!/usr/bin/env python3
"""R173: hill-climb against Lemma PORTAL. Genome: a genportal.py game + a valid start pair. Score: 10^6 * VIOLATIONS + 100 * premised
pairs + pairs (portalck.analyze). Mutations: swap two priorities, retarget one edge, flip a branching vertex's owner, change one
start entry. Usage: climb173.py N SEED ITERS OUT_PREFIX  (writes OUT_PREFIX.pg / .start for the best genome)."""
import sys, os, random, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from portalck import analyze, load, readstart
N, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
R = random.Random(seed)
subprocess.run([sys.executable, os.path.join(HERE, "genportal.py"), str(N), str(seed), out + ".pg", out + ".start"], check=True)
g = load(out + ".pg"); st = readstart(out + ".start")
G = dict(prio=list(g.prio), own=list(g.owner), succ=[list(x) for x in g.succ], s=dict(st[0]), t=dict(st[1]))
import pg
def sc(G):
    gg = pg.Game(G["prio"], G["own"], G["succ"])
    try: r = analyze(gg, (G["s"], G["t"]), cap=3000)
    except Exception as e: print("ERR", e, flush=True); return -1, None
    return 10 ** 6 * r["bad"] + 10 ** 4 * r["premised"] + 1000 * (r["zc"] + r["nr"]) + 100 * r["pairs"] + min(r["K"], 99), r
def fix(G):
    for v in range(N):
        d = G["s"] if G["own"][v] == 0 else G["t"]; o = G["t"] if G["own"][v] == 0 else G["s"]
        o.pop(v, None)
        if d.get(v) not in G["succ"][v]: d[v] = G["succ"][v][0]
def mutate(G):
    H = dict(prio=list(G["prio"]), own=list(G["own"]), succ=[list(x) for x in G["succ"]], s=dict(G["s"]), t=dict(G["t"]))
    k = R.random()
    if k < 0.3: a, b = R.sample(range(N), 2); H["prio"][a], H["prio"][b] = H["prio"][b], H["prio"][a]
    elif k < 0.55:
        v = R.randrange(N); i = R.randrange(len(H["succ"][v])); w = R.randrange(N)
        if w not in H["succ"][v]: H["succ"][v][i] = w
    elif k < 0.65:
        v = R.randrange(N)
        if len(H["succ"][v]) > 1: H["own"][v] ^= 1
    elif k < 0.75:
        v = R.randrange(N); w = R.randrange(N)
        if w not in H["succ"][v] and len(H["succ"][v]) < 4: H["succ"][v].append(w)
    else:
        v = R.randrange(N); (H["s"] if H["own"][v] == 0 else H["t"])[v] = R.choice(H["succ"][v])
    fix(H); return H
fix(G); best, br = sc(G)
for it in range(iters):
    H = mutate(G); s, r = sc(H)
    if s >= best:
        if s > best: print(f"it {it} score {s} {r}", flush=True)
        G, best, br = H, s, r
        with open(out + ".pg", "w") as f:
            f.write(f"parity {N - 1};\n")
            for v in range(N): f.write(f"{v} {G['prio'][v]} {G['own'][v]} {','.join(map(str, G['succ'][v]))};\n")
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(G["s"].items())) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(G["t"].items())) + "\n")
print(f"FINAL score {best} {br}")
