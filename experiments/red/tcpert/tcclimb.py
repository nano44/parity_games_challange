#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): hill climb over label-rule sets (tcpert.py rules, up to MAXR parts) on tc(N),
fitness = pinned-Oink DTL iterations at N = NB minus at N = NA (growth; TCC_RATIO=1: their ratio; TCC_RATIO=2: min of the ratios at NB/NA and NB-1/NA-1; TCP_EXT=1 adds cut/loop rules), every solution verified (an unverified run is
printed as NOT VERIFIED and rejected). Prints improvements with the iteration row at N = 3..NB.
TCC_TLHARD=K keeps only rule sets whose pinned-Oink TL iterations on tc(6) stay >= K.
Usage: tcclimb.py RNGSEED STEPS MAXR NA NB OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tcpert as T
seed, steps, maxr, na, nb, out = (int(x) for x in sys.argv[1:6]) + (sys.argv[6],) if False else (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
rng = random.Random(seed); os.makedirs(out, exist_ok=True); tmp = os.path.join(out, f"c{seed}.pg")
base = {N: T.gen(N) for N in range(3, nb + 1)}; cache = {}
def its(rule, Ns):
    r = []
    for N in Ns:
        k = (rule, N)
        if k not in cache:
            try: cache[k] = T.solve(T.apply(base[N], list(rule)), tmp)
            except Exception: cache[k] = (-2, False)
        r.append(cache[k])
    return r
def tlhard(rule):   # TCC_TLHARD=K: pinned Oink --tl iterations on the perturbed tc(6) must stay >= K (tc(6): 128)
    k = ("tl", rule)
    if k not in cache:
        import subprocess, re
        V = T.apply(base[6], list(rule)); p = tmp + ".tl.pg"
        with open(p, "w") as f: f.write(f"parity {len(V)-1};\n" + "".join(f'{i} {v[0]} {v[1]} {",".join(map(str, v[2]))} "{v[3]}";\n' for i, v in enumerate(V)))
        try:
            o = subprocess.run([os.path.join(T.T, "oink"), "--tl", "--no-single", "--no-wcwc", "--no-loops", p, "/dev/null"], capture_output=True, text=True, timeout=60).stdout
            m = re.search(r"solved in (\d+) iterations", o); cache[k] = int(m[1]) if m else 0
        except subprocess.TimeoutExpired: cache[k] = 10 ** 6
    return cache[k]
def fit(rule):
    if os.environ.get("TCC_TLHARD") and tlhard(rule) < int(os.environ["TCC_TLHARD"]): return -50
    if os.environ.get("TCC_RATIO") == "2":   # robust ratio: min(it(NB)/it(NA), it(NB-1)/it(NA-1)), all four verified
        rs = its(rule, [na - 1, na, nb - 1, nb])
        if not all(x[1] for x in rs):
            if all(x[0] >= 0 for x in rs): print("NOT VERIFIED", rule, rs, flush=True)
            return -99
        return min(rs[3][0] / rs[1][0], rs[2][0] / rs[0][0])
    a, b = its(rule, [na, nb])
    if not (a[1] and b[1]):
        if a[0] >= 0 and b[0] >= 0: print("NOT VERIFIED", rule, a, b, flush=True)
        return -99
    return (b[0] / a[0]) if os.environ.get("TCC_RATIO") == "1" else b[0] - a[0]
def one(): return T.randrule(rng)[0]
import ast
cur = tuple(ast.literal_eval(os.environ["TCC_INIT"])) if os.environ.get("TCC_INIT") else (); fc = fit(cur); best = fc   # TCC_INIT: start rule set
for it in range(steps):
    r = list(cur); m = rng.random()
    if r and m < 0.3: r.pop(rng.randrange(len(r)))
    elif r and m < 0.6: r[rng.randrange(len(r))] = one()
    elif len(r) < maxr: r.append(one())
    cand = tuple(r); f = fit(cand)
    if f >= fc:
        cur, fc = cand, f
        if f > best:
            best = f; print(it, f, cand, [x[0] for x in its(cand, list(range(3, nb + 1)))], flush=True)
print("done best", best, cur)
