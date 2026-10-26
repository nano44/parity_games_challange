#!/usr/bin/env python3
"""Box 38 (c): STATE-level search for NO-RR-B (docs/new/N5-NEB-box38.md). Samples random 𝒞^1O games with a self-loop at o, τ(o) = o,
and random σ. Keeps states a at which N5 takes an in-phase Even fallback (S4a and S4b no-ops, Iσ ≠ ∅, a+1 has the same (λ_Ξ, λ_U, τ))
with H1 at a (¬H2 holds since τ(o) = o). CASE A: rank(o) > rank(c_θ), else B. Counts R -> R̄ gates at a, and fallbacks that SWITCH some v ∈ R to a target in R̄ (an R-rise), by case;
an R-RISE is u ∈ R̄_a ∩ R̄_{a+1} whose Ξ changes; a LOW-ROUTE rise has its route below c_θ at a and a+1 (only
those can collide with an F-value: P(Ξ u) = P(θ)); saves case-B states with a low-route rise.
A state-level counterexample refutes the state-level lemma only, not NO-ENTRY-B for runs. One Odd choice vertex asserted.
Usage: statesamp.py N lo hi seed [outdir]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); B37 = os.path.join(HERE, "..", "box37")
sys.path.insert(0, B37); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *
from mono import lev
import pg

def c1o(rng, lo, hi):
    n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
    for v in range(n):
        if v != o and rng.random() < 0.15: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
    succ[o] = sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 3)))) + [o]))
    if len(succ[o]) < 2: return None, None
    pr = rng.sample(range(n + 3), n) if rng.random() < 0.5 else [rng.randrange(n + 3) for _ in range(n)]
    return pg.Game(pr, owner, succ), o

def probe(g, o, s, acc, name, outdir):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    E, Ed = Engine(g), Engine(dual(g)); t = [g.succ[v][0] if g.owner[v] == 1 else -1 for v in range(g.n)]; t[o] = o
    r = step(g, E, Ed, s, t)
    if r is None or not r[4] or not r[2]: return
    ns, nt = r[0], r[1]
    Xi, sb = E.evaluate(tuple(s)); Xi2, _ = E.evaluate(tuple(ns)); U, _ = Ed.evaluate(tuple(t)); U2, _ = Ed.evaluate(tuple(nt))
    if [x[0] for x in Xi] != [x[0] for x in Xi2] or [x[0] for x in U] != [x[0] for x in U2] or nt != t: return
    if oncycle(g, s, sb, o): return            # need H1
    case = "A" if E.rank[o] > E.rank[Xi[o][0]] else "B"; bump(acc, case + "_fb_states")
    Rb = set(reach_o(g, s, t, o)) | {o}; k = 0
    for y, z in E.improving(tuple(s), Xi):
        if y in Rb and z in Rb and y != o:
            k += 1; bump(acc, case + "_RRgates"); L = lev(Xi[s[y]], Xi[z]); bump(acc, f"{case}_RRgate_lev{'-1' if L == -1 else ('<ro' if L < E.rank[o] else '>=ro')}")
    Rb2 = set(reach_o(g, ns, t, o)) | {o}; cth = Xi[o][0]
    def low_route(sig, u):
        nx = [sig[x] if g.owner[x] == 0 else t[x] for x in range(g.n)]
        while u != o:
            if E.rank[u] > E.rank[cth]: return False
            u = nx[u]
        return True
    rise = [u for u in Rb & Rb2 if u != o and Xi2[u] != Xi[u]]
    good = [u for u in rise if low_route(s, u) and low_route(ns, u)]
    if rise: bump(acc, case + "_states_with_Rrise")
    if good: bump(acc, case + "_states_with_lowroute_Rrise")
    if k:
        bump(acc, case + "_states_with_RRgate")
        if case == "B" and good and outdir and acc.get("B_saved", 0) < 20:
            bump(acc, "B_saved"); p = os.path.join(outdir, f"{name}.pg")
            with open(p, "w") as f:
                f.write(f"parity {g.n - 1};\n")
                for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
            with open(p + ".state", "w") as f: f.write(" ".join(map(str, s)) + "\n")
            mx(acc, "ex_B", g.n, name)

if __name__ == "__main__":
    N, lo, hi, seed = map(int, sys.argv[1:5]); outdir = sys.argv[5] if len(sys.argv) > 5 else None
    if outdir: os.makedirs(outdir, exist_ok=True)
    rng = random.Random(seed); acc = {}
    for d in range(N):
        g, o = c1o(rng, lo, hi)
        if g is None: continue
        for j in range(6):
            s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
            probe(g, o, s, acc, f"ss{seed}_{d}_{j}", outdir)
    for key in sorted(acc): print(key, acc[key])
