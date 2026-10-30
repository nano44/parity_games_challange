#!/usr/bin/env python3
"""L-NEW box 77 (copy of box74/climb_rho.py, fitness FLAT): hill climb on max FLAT_P(v) (fixdepth.py: Xi-changes of v in a phase that do not deepen its lcp with the end-of-phase value), mutations = n5-epoch/climb.py's mutate; fitness
(max FLAT_P(v), length of that phase); sideways moves accepted. N5, or N5-LZC with --lzc.
Usage: climb_rho.py SEED.pg SEED.start|- --secs S --rng R --out PREFIX [--lzc]"""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-epoch"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
import pg
from climb import mutate
def opt(name, d=None): return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else d
def rho(g, s0, t0, cap=3000):
    """fitness: (max FLAT_P(v) over phases and vertices, length of that phase); FLAT as in fixdepth.py."""
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); S = [tuple(s0)]; TAU = [tuple(t0)]
    while True:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1]))
        if len(S) > cap: return (-1, 0)
    XI = [E.evaluate(x)[0] for x in S]; LX = [tuple(v[0] for v in x) for x in XI]; T = len(S) - 1
    def depth(a, b):
        if a == b: return n + 2
        if a[0] != b[0]: return 0
        x = a[1] ^ b[1]
        return 1 + (n - 1 - (x.bit_length() - 1)) if x else n + 1
    best = (0, 0); a = 0
    for k in range(1, T + 2):
        if k == T + 1 or LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1]:
            ks = list(range(a, k)); fin = XI[ks[-1]]
            for v in range(n):
                fl = sum(1 for k0 in ks[:-1] if XI[k0][v] != XI[k0 + 1][v] and depth(XI[k0][v], fin[v]) == depth(XI[k0 + 1][v], fin[v]))
                best = max(best, (fl, len(ks) - 1))
            a = k
    return best
g = load(sys.argv[1]); n = g.n; E0, Ed0 = Engine(g), Engine(dual(g))
st = readstart(sys.argv[2]) if sys.argv[2] != "-" else None
s, t = start_pair(g, E0, Ed0, st)
s = [s[v] if g.owner[v] == 0 else -1 for v in range(n)]; t = [t[v] if g.owner[v] == 1 else -1 for v in range(n)]
rng = random.Random(int(opt("--rng", "1"))); secs = float(opt("--secs", "600")); out = opt("--out")
def pair(s, t): return [x if x >= 0 else 0 for x in s], [x if x >= 0 else 0 for x in t]
best = rho(g, *pair(s, t)); cur = (g, s, t); t0 = time.time(); steps = 0
print("START", best, flush=True)
while time.time() - t0 < secs:
    steps += 1
    h, s2, t2 = mutate(*cur, rng)
    try: f = rho(h, *pair(s2, t2))
    except Exception: continue
    if f >= best:
        if f > best: print("BEST", steps, f, f"ratio {f[0] / n:.3f}", flush=True)
        best = f; cur = (h, s2, t2)
h, s, t = cur
with open(out + ".pg", "w") as fh:
    fh.write(f"parity {n - 1};\n" + "".join(f"{v} {h.prio[v]} {h.owner[v]} {','.join(map(str, h.succ[v]))};\n" for v in range(n)))
with open(out + ".start", "w") as fh:
    fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(n) if h.owner[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{t[v]}" for v in range(n) if h.owner[v] == 1) + "\n")
print("FINAL", best, f"ratio {best[0] / n:.3f}", "steps", steps)
