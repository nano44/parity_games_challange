#!/usr/bin/env python3
"""L-RED box 12 (produced on Opus 5.5): general hill climb on NEST (carryclimb.nest over L-ALG fixd_fdpos.py positions, run
UNMODIFIED as a subprocess), then S. Mutations: add / remove an edge (keeping one successor), flip an owner, shift a priority
by +-1 or +-2 (>= 0). Every game must verify on pinned Oink. Usage: nestclimb.py SEED.pg RNGSEED STEPS OUTDIR"""
import sys, os, random, subprocess, re, ast
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(os.environ["LALG_DIR"], "experiments", "harness"))
import tcpert as T, pg
src = open(os.path.join(H, "carryclimb.py")).read(); ns = {}; exec(src[src.index("def nest"):src.index("def fit")], ns); nest = ns["nest"]
FP = os.path.join(os.environ["LALG_DIR"], "experiments", "alg", "fixd_fdpos.py")
seedf, rs, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(rs); os.makedirs(out, exist_ok=True)
tmp = os.path.join(out, f"n{rs}.pg"); g0 = pg.read(seedf)
def fit(pr, ow, su):
    V = [[pr[i], ow[i], su[i], str(i)] for i in range(len(pr))]; r = T.solve(V, tmp)
    if not r[1]: print("NOT VERIFIED", r, flush=True); return (-1,)
    o = subprocess.run([sys.executable, FP, tmp], capture_output=True, text=True, timeout=600, env=dict(os.environ, DTL_ORDER=os.environ.get("DTL_ORDER", "stable"))).stdout
    sc = (0, 0)
    for line in o.splitlines():
        m = re.search(r"S (\d+) .*positions (\[[^\]]*\])", line)
        if m: sc = max(sc, (nest([x for x in ast.literal_eval(m[2]) if x is not None]), int(m[1])))
    return sc
pr, ow, su = list(g0.prio), list(g0.owner), [list(s) for s in g0.succ]; n = len(pr); f = fit(pr, ow, su); best = f; print("start", f, flush=True)
for it in range(steps):
    p2, o2, s2 = list(pr), list(ow), [list(s) for s in su]; v = rng.randrange(n); k = rng.randrange(4)
    if k == 0: s2[v] = sorted(set(s2[v] + [rng.randrange(n)]))
    elif k == 1 and len(s2[v]) > 1: s2[v].remove(rng.choice(s2[v]))
    elif k == 2: o2[v] ^= 1
    else: p2[v] = max(0, p2[v] + rng.choice([-2, -1, 1, 2]))
    g = fit(p2, o2, s2)
    if g >= f:
        pr, ow, su, f = p2, o2, s2, g
        if f > best:
            best = f; print(it, f, flush=True); pg.write(pg.Game(pr, ow, su), os.path.join(out, f"best_r{rs}.pg"))
print("done best", best)
