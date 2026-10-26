#!/usr/bin/env python3
"""L-SI succ. 5, box 10: adversarial climb against CONJECTURE RISE-LAST (L-RED R68 §6), with a fitness built from Lemma BL
(docs/si/N5-RL-box10.md): an in-scope THR fallback needs (i) no W-improving gate, (ii) a gate R -> F (window gate, FBL) and (iii) a
BLOCKED edge (W-improving, not a gate). After a COARSE_L(θ) rise inside a scope run (L = level of the last fallback before it), each
in-scope state t scores 3·[RF_t > 0] + 3·[blocked_t > 0] + (5 − min(Wimp_t, 5)); 11 = all three fallback conditions on Even's side.
Fitness = (RISE-LAST violations = fallbacks after a rise in its scope run, best post-rise score, #post-rise in-scope states, rises).
𝒞^1O only (asserted). Mutation operator and o-cyclicity test: experiments/new/box21/climb_fix.py, box25/pureY.py (read-only), as in
experiments/si/coarse/jclimb.py. Usage: rlclimb.py seed secs OUT seed.pg   (writes OUT.pg on every improvement)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "coarse"))
from reltrace import *
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box21")); sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split

def scan_rl(g, name="climb"):
    o = odd_choice(g); assert o is not None
    runs, d_o, exits, out = runs_of(g, name); E = n5.Engine(g); C = Counter()
    for S in runs:
        L = None; risen = False
        for e in S:
            i = e["i"]; a = out[i]
            if e["k"] == "F":
                if risen: C["viol"] += 1
                L = e["M"]; risen = False; continue
            if L is None: continue
            if risen:
                R = a["R"]; W = a["W"]; X = a["Xi"]; s = a["s"]; gs = set(a["Is"])
                rf = sum(1 for y, z in gs if y in R and z not in R and z != o)
                wimp = sum(1 for y, z in gs if E.key(W[z]) > E.key(W[s[y]]))
                bl = sum(1 for v in range(g.n) if g.owner[v] == 0 for u in set(g.succ[v])
                         if u != s[v] and (v, u) not in gs and E.key(W[u]) > E.key(W[s[v]]))
                C["post"] += 1; C["best"] = max(C["best"], 3 * (rf > 0) + 3 * (bl > 0) + 5 - min(wimp, 5))
            if e["lt"] > L and e["r"] > L: risen = True; C["rises"] += 1
    return C

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-10 ** 9, -1, -1, -1)
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-10 ** 9, -1, -1, -1)
    try:
        c = scan_rl(g)
        return (c.get("viol", 0), c.get("best", 0), min(c.get("post", 0), 40), c.get("rises", 0))
    except AssertionError: raise
    except Exception: return (-10 ** 9, -1, -1, -1)

def write(path, G):
    n = len(G[0])
    open(path, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); write(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
