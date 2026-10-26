#!/usr/bin/env python3
"""Box 44: start-pair climb for a POST-FREEZE kind change (KIND-MONO content). Genome = game + start pair (σ_0, τ_0); trace ex16.trace.
Fitness (#FAIL, KM_postfreeze_kindchanges, U3x_postfreeze_len, U3x_kindchange_transitions). Saves best as OUT.pg + OUT.start.json.
Usage: kmpst18.py seed secs OUT seed.pg"""
import sys, os, random, time, io, contextlib, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import kw18, sox, pg
from soclimb import mutate, dump
NEG = (-1, -10 ** 6, -10 ** 6, -1)
def fit(G, st):
    try:
        g = pg.Game(*G)
        if any(not s for s in G[2]) or len(sox.oddchoice(g)) != 1 or any(st[v] not in g.succ[v] for v in range(g.n)): return NEG
        acc = {}
        with contextlib.redirect_stdout(io.StringIO()): kw18.analyse(g, acc, "c", st, cap=300)
    except Exception: return NEG
    return (sum(v for k, v in acc.items() if k.startswith("FAIL")), acc.get("KM_postfreeze_kindchanges", -10 ** 6), acc.get("U3x_postfreeze_len", -10 ** 6), acc.get("U3x_kindchange_transitions", 0))
seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
g = sox.load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
st = list(sox.trace(g, cap=1)[0][0][0]); st = [st[v] if g.owner[v] == 0 else sox.trace(g, cap=1)[0][0][1][v] for v in range(g.n)]
f = fit(G, st); t0 = time.time(); it = 0; print("start", f, flush=True)
while time.time() - t0 < secs:
    if rng.random() < 0.5:
        H = mutate(rng, G); s2 = [x if x in H[2][v] else rng.choice(H[2][v]) for v, x in enumerate(st)]
    else:
        H = G; s2 = list(st); v = rng.randrange(len(st)); s2[v] = rng.choice(G[2][v])
    it += 1; fh = fit(H, s2)
    if fh[0] > 0: dump(H, out + "_viol.pg"); json.dump(dict(start=s2), open(out + "_viol.start.json", "w")); print("HIT", it, fh, flush=True)
    if fh >= f:
        if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); dump(H, out + ".pg"); json.dump(dict(start=s2), open(out + ".start.json", "w"))
        G, f, st = H, fh, s2
print("FINAL", f, it, flush=True)
