#!/usr/bin/env python3
"""L-RED box 12 (produced on Opus 5.5): climb toward COMPOUNDING (L-ALG GAP-A-M §29): fitness from L-ALG's fixd_fdpos.py run
UNMODIFIED (subprocess; LALG_DIR): per phase, the chain positions of the first differences. CARRIES(p) = number of
consecutive pairs of transitions at position p with >= 2 transitions at deeper positions (> p) between them; score =
(max over phases of NEST (recursive nesting depth, see nest()), CARRIES, S). Base: disjoint union leanT(a) + leanT(b) as in prodclimb.py, with
<= K individual cross edges; every game must verify on pinned Oink. CC_COPIES=a,b,c,... uses k copies (cross edges between any two different copies).
Usage: carryclimb.py SEED STEPS A B K OUTDIR"""
import sys, os, random, subprocess, re, ast
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tcpert as T, lean as LE
seed, steps, a, b, K, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); tmp = os.path.join(out, f"c{seed}.pg")
FP = os.path.join(os.environ["LALG_DIR"], "experiments", "alg", "fixd_fdpos.py")
sizes = [int(x) for x in os.environ["CC_COPIES"].split(",")] if os.environ.get("CC_COPIES") else [a, b]   # k copies
U = []; sh = 0; owner = []
for ci, sz in enumerate(sizes):
    Cp = LE.lean(sz, T.LT); off = len(U)
    U += [[v[0] + sh, v[1], [w + off for w in v[2]], f"{ci+1}:" + v[3]] for v in Cp]; owner += [ci] * len(Cp)
    sh = max(v[0] for v in U) + 2; sh += sh % 2
nA = len(U) - len(LE.lean(sizes[-1], T.LT)) if len(sizes) == 2 else None; n = len(U)
def cross():
    while True:
        u, w = rng.randrange(n), rng.randrange(n)
        if owner[u] != owner[w]: return (u, w)
def build(E):
    V = [[x[0], x[1], list(x[2]), x[3]] for x in U]
    for u, w in E:
        if w not in V[u][2]: V[u][2].append(w)
    return V
def write(V, path):
    with open(path, "w") as f: f.write(f"parity {len(V)-1};\n" + "".join(f'{k} {v[0]} {v[1]} {",".join(map(str, v[2]))} "{v[3]}";\n' for k, v in enumerate(V)))
def carries(pos):
    best = 0
    for p in set(pos):
        idx = [i for i, x in enumerate(pos) if x == p]; c = 0
        for i0, i1 in zip(idx, idx[1:]):
            if sum(1 for x in pos[i0 + 1:i1] if x > p) >= 2: c += 1
        best = max(best, c)
    return best
def nest(pos):
    """Nested counter depth: 1 if any transition; else for a position p with >= 2 transitions, 1 + max over the gaps between
    consecutive transitions at p of nest(gap restricted to positions > p). leanT (all positions distinct) scores 1."""
    if not pos: return 0
    best = 1
    for p in set(pos):
        idx = [i for i, x in enumerate(pos) if x == p]
        for i0, i1 in zip(idx, idx[1:]):
            gap = [x for x in pos[i0 + 1:i1] if x > p]
            if gap: best = max(best, 1 + nest(gap))
    return best
def fit(E):
    V = build(E); r = T.solve(V, tmp)
    if not r[1]: print("NOT VERIFIED", E, r, flush=True); return (-1,), r
    o = subprocess.run([sys.executable, FP, tmp], capture_output=True, text=True, timeout=600, env=dict(os.environ, DTL_ORDER=os.environ.get("DTL_ORDER", "stable"))).stdout
    sc = (0, 0, 0)
    for line in o.splitlines():
        m = re.search(r"S (\d+) .* reset-depth proxy (\d+) positions (\[[^\]]*\])", line)
        if m: ps = [x for x in ast.literal_eval(m[3]) if x is not None]; sc = max(sc, (nest(ps), carries(ps), int(m[1])))
    return sc, r
if os.environ.get("CC_SHRINK"):   # CC_SHRINK="[label pairs]": greedily drop cross edges while NEST stays >= its start value
    ix = {x[3]: k for k, x in enumerate(U)}; E = [(ix[u], ix[w]) for u, w in ast.literal_eval(os.environ["CC_SHRINK"])]
    f0, r0 = fit(E); print("start", f0, r0, flush=True); i = 0
    while i < len(E):
        F = E[:i] + E[i + 1:]; g, rr = fit(F)
        if g[0] >= f0[0]: E = F; print("dropped; now", len(E), g, rr, flush=True)
        else: i += 1
    print("SHRUNK", fit(E), [(U[u][3], U[w][3]) for u, w in E], flush=True); write(build(E), os.path.join(out, "shrunk.pg")); sys.exit(0)
E = []
if os.environ.get("CC_INIT"):   # start from these label pairs
    ix = {x[3]: k for k, x in enumerate(U)}; E = [(ix[u], ix[w]) for u, w in ast.literal_eval(os.environ["CC_INIT"])]
f, r = fit(E); best = f; print("start", f, r, flush=True)
for it in range(steps):
    F = list(E); m = rng.random()
    if F and m < 0.3: F.pop(rng.randrange(len(F)))
    elif len(F) < K: F.append(cross())
    else: F[rng.randrange(len(F))] = cross()
    g, rr = fit(F)
    if g >= f:
        E, f = F, g
        if f > best:
            best = f; print(it, f, rr, [(U[u][3], U[w][3]) for u, w in E], flush=True); write(build(E), os.path.join(out, f"best_s{seed}.pg"))
print("done best", best)
