#!/usr/bin/env python3
"""L-RED box 12 (produced on Opus 5.5): two-player hill climb against L-ALG's NEW-KEY potentials, judged by L-ALG's
experiments/alg/b12_pot.py run UNMODIFIED as a subprocess (LALG_DIR; order DTL_ORDER). Score (lexicographic): violations of
K-v-all, then of K-v-rs + K-v-rV + K-v-rjV, then of K-jRrV, then searches (from the transition count). Mutations as nestclimb.py.
Every game must verify on pinned Oink. A K-v-all violation is saved as KILL_*.pg and printed. Usage: keyclimb.py SEED.pg RNGSEED STEPS OUTDIR"""
import sys, os, random, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(os.environ["LALG_DIR"], "experiments", "harness"))
import tcpert as T, pg
BP = os.path.join(os.environ["LALG_DIR"], "experiments", "alg", "b12_pot.py")
seedf, rs, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(rs); os.makedirs(out, exist_ok=True)
tmp = os.path.join(out, f"k{rs}.pg"); g0 = pg.read(seedf)
def viol(o, key):
    m = re.search(r"^\s*" + re.escape(key) + r"\s+violations\s+(\d+)", o, re.M); return int(m[1]) if m else 0
def fit(pr, ow, su):
    g = pg.Game(pr, ow, su); pg.write(g, tmp)
    V = [[pr[i], ow[i], su[i], str(i)] for i in range(len(pr))]; r = T.solve(V, tmp + ".v.pg")
    if not r[1]: print("NOT VERIFIED", r, flush=True); return (-1,)
    o = subprocess.run([sys.executable, BP, tmp], capture_output=True, text=True, timeout=900, env=dict(os.environ, DTL_ORDER=os.environ.get("DTL_ORDER", "stable"))).stdout
    m = re.search(r"transitions (\d+)", o); tr = int(m[1]) if m else 0
    return (viol(o, "K-v-all"), viol(o, "K-v-rs") + viol(o, "K-v-rV") + viol(o, "K-v-rjV"), viol(o, "K-jRrV"), tr)
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
            if f[0] > 0: pg.write(pg.Game(pr, ow, su), os.path.join(out, f"KILL_r{rs}_it{it}.pg")); print("KILL K-v-all", flush=True)
print("done best", best)
