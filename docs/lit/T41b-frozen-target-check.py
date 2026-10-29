# L-LIT T41b (docs/lit/T41b-frozen-wphases.md). T41-target-check.py split by L-SI's FROZEN W-PHASES (claude/l-si docs/si/N5-FRZ-box29.md §0;
# the cut rule below is copied from experiments/si/frz/fwphase.py fwphases() at l-si 4e928f11, read only). Reads L-SI's helpers read-only
# (experiments/si/root/common.py -> experiments/new/box21/n5x.py, si.py). Usage (repo root): python3 -I docs/lit/T41b-frozen-target-check.py GAME.pg [START]
# Inside a phase P (λ_Ξ, τ constant), each transition t -> t+1 is of one KIND: FB (S4c fallback), LW (non-fallback, changes λ_W), SB (non-fallback,
# keeps λ_W, changes σ̄), or FZ (none of these: inside a frozen W-phase). Target c = σ^c_τ (S1 on G^d against τ, all edges), fixed on P.
# Per Even switch: MISS (σ_{t+1}(v) ≠ c(v)), AWAY (σ_t(v) = c(v), leaves it), tallied by KIND. Per frozen W-phase F = [a, b] and switching vertex v:
# SW_F (switches of v in F), AWAY_F, SBR_F (switches up to the first landing on c(v) inside F), NEVER_F. Prints totals and maxima.
import os, sys
from collections import Counter
ROOT = os.getcwd(); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from n5x import Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, R = rows(g, st, cap=20000); n = g.n; Ed = Engine(dual(g)); EV = [v for v in range(n) if g.owner[v] == 0]
lam = lambda t: tuple(x[0] for x in R[t]["W"])
def kind(t):
    if R[t]["fb"]: return "FB"
    if lam(t) != lam(t + 1): return "LW"
    if R[t]["sb"] != R[t + 1]["sb"]: return "SB"
    return "FZ"
def fwphases(i, j):                       # = fwphase.py fwphases(R, i, j)
    out, a = [], i
    for t in range(i, j):
        if kind(t) != "FZ":
            if t > a: out.append((a, t))
            a = t + 1
    if j > a: out.append((a, j))
    return out
TR, SW, MISS, AWAY = Counter(), Counter(), Counter(), Counter()
F = Counter(); mx = Counter(); worst = {}
for i, j in phases(R):
    c = Ed.evaluate(tuple(R[i]["t"]))[1]
    for t in range(i, j):
        k = kind(t); TR[k] += 1
        for v in EV:
            if R[t]["s"][v] == R[t + 1]["s"][v]: continue
            SW[k] += 1; MISS[k] += R[t + 1]["s"][v] != c[v]; AWAY[k] += R[t]["s"][v] == c[v]
    for a, b in fwphases(i, j):
        F["fwphases"] += 1; sw, aw, hit = Counter(), Counter(), {}
        for t in range(a, b):
            for v in EV:
                if R[t]["s"][v] == R[t + 1]["s"][v]: continue
                sw[v] += 1; aw[v] += R[t]["s"][v] == c[v]
                if R[t + 1]["s"][v] == c[v] and v not in hit: hit[v] = sw[v]
        for v in sw:
            F["verts"] += 1; F["never"] += v not in hit; F["sbr_gt1"] += hit.get(v, 1) > 1; F["away_verts"] += aw[v] > 0
            for key, val in (("sw_max", sw[v]), ("away_max", aw[v]), ("sbr_max", hit.get(v, 0))):
                if val > mx[key]: mx[key] = val; worst[key] = (v, a, b, sw[v], aw[v], hit.get(v), b - a)
print(f"{os.path.basename(sys.argv[1])}: n={n} | transitions " + " ".join(f"{k}={TR[k]}" for k in ("FZ", "LW", "SB", "FB"))
      + " | switches " + " ".join(f"{k}={SW[k]}" for k in ("FZ", "LW", "SB", "FB")) + " | MISS " + " ".join(f"{k}={MISS[k]}" for k in ("FZ", "LW", "SB", "FB"))
      + " | AWAY " + " ".join(f"{k}={AWAY[k]}" for k in ("FZ", "LW", "SB", "FB")) + " | frozen " + " ".join(f"{k}={v}" for k, v in F.items())
      + " " + " ".join(f"{k}={v}" for k, v in mx.items()) + f" | argmax (v, a, b, SW_F, AWAY_F, SBR_F, |F|): {worst}")
