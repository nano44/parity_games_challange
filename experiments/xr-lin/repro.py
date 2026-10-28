#!/usr/bin/env python3
"""Independent reproduction (Lead 2026-10-28 21:27Z) of L-SI's kill of CONJECTURE XR-LIN on l121reader_n41 (L-SI, origin/claude/l-si
2e94557d, experiments/si/root/instances/; copied here unchanged, sha1 checked) = long121_n40 (L-NEW box48 / L-RED n3) plus a passive
Odd reader o = 40.
Engine: ONLY L-COMP's n5b.py SPEC (experiments/n5-second; valuations from L-COMP's pgsolver_si port). No experiments/si/ code imported.
Measures:
 (a) the run on vertices 0..39 vs the run of long121_n40 from its start: per state σ|0..39, τ|0..39, σ̄|0..39 (SPEC σ̄), the fallback
     flags, and the phase partition (R38 (a): maximal runs of (λ_Ξ, τ) constant; computed on each game on its own; for the reader game
     both on all 41 vertices and on 0..39 only);
 (b) Ξ(o) changes in the phase [1, 122] (states 1..122): #{t in [1, 121] : Ξ_t(o) != Ξ_{t+1}(o)}, Ξ = SPEC S1 valuation of σ_t;
     also per phase of the reader run, and the max over v of Ξ-changes per phase (XR);
 (c) regions: n5b's = Oink zlk @ 8fbf0a7 (tl if zlk aborts); strategies pass harness/verify.py; both games.
Usage: repro.py"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness", "n5-exhaustive"):
    sys.path.insert(0, os.path.join(ROOT, "experiments", p))
import n5b  # noqa: E402
import pg, verify  # noqa: E402
import subprocess, tempfile  # noqa: E402
OINK = os.path.join(ROOT, "tools", "oink", "build", "oink")


def zlk(path, n):
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "s"); tag = "zlk"
        if subprocess.run([OINK, "--zlk", "-w", "1", path, out], capture_output=True).returncode != 0:
            subprocess.run([OINK, "--tl", "-w", "1", path, out], capture_output=True, check=True); tag = "tl"
        return pg.read_sol(open(out).read(), n), tag


def run(name, o=None):
    gp = os.path.join(HERE, "instances", name + ".pg"); sp = os.path.join(HERE, "instances", name + ".start")
    g = pg.read(gp); sig, tau = n5b.read_start(sp, g)
    S3s = n5b.SpecSI(g).initial_strategy_by_best_reward(); S3t = n5b.SpecSI(n5b.dual(g)).initial_strategy_by_best_reward()
    sig = [sig[v] if g.owner[v] == 0 and sig[v] >= 0 else (S3s[v] if g.owner[v] == 0 else -1) for v in range(g.n)]
    tau = [tau[v] if g.owner[v] == 1 and tau[v] >= 0 else (S3t[v] if g.owner[v] == 1 else -1) for v in range(g.n)]
    filled = [v for v in range(g.n) if (g.owner[v] == 0 and n5b.read_start(sp, g)[0][v] < 0) or (g.owner[v] == 1 and n5b.read_start(sp, g)[1][v] < 0)]
    L, FB = [], []
    win, ws, it, fb = n5b.N5(g, mode="spec").run(list(sig), list(tau), trace=L, fbtrace=FB, max_iter=10 ** 6)
    SG = n5b.SpecSI(g)
    XS = [SG.evaluate_choice(list(s)) for s, _ in L]
    ref, tag = zlk(gp, g.n); errs = verify.check(g, win, ws)
    sha = hashlib.sha1(open(gp, "rb").read()).hexdigest(); ssha = hashlib.sha1(open(sp, "rb").read()).hexdigest()
    print(f"{name}: sha1 {sha} start {ssha} n {g.n} it {it} fb {fb} states {len(L)} | regions = oink {tag}: {win == ref} | verify "
          f"{'OK' if not errs else errs[:2]} | start entries filled from S3: {filled}")
    return g, L, FB, XS


def phases(L, XS, keep):
    key = [(tuple(XS[k][0][v][0] for v in keep), tuple(L[k][1][v] for v in keep)) for k in range(len(L))]
    out, i = [], 0
    while i < len(key):
        j = i
        while j + 1 < len(key) and key[j + 1] == key[i]:
            j += 1
        out.append((i, j)); i = j + 1
    return out


g0, L0, F0, X0 = run("long121_n40")
g1, L1, F1, X1 = run("l121reader_n41")
o = 40; base = range(40)
print(f"reader o = {o}: owner {g1.owner[o]} prio {g1.prio[o]} out-degree {len(set(g1.succ[o]))} in-degree {sum(o in s for s in g1.succ)}; "
      f"game on 0..39 identical to long121_n40: {[g1.prio[v] for v in base] == g0.prio and [g1.owner[v] for v in base] == g0.owner and [sorted(set(g1.succ[v])) for v in base] == [sorted(set(s)) for s in g0.succ]}")
# (a)
T = min(len(L0), len(L1)); first = None
for k in range(T):
    eq = (all(L1[k][0][v] == L0[k][0][v] for v in base) and all(L1[k][1][v] == L0[k][1][v] for v in base)
          and all(X1[k][1][v] == X0[k][1][v] for v in base if g0.owner[v] == 1))
    if not eq:
        first = k; break
print(f"(a) states: long121 {len(L0)}, reader {len(L1)}; sigma, tau, sigma-bar on 0..39 equal at every state: {first is None and len(L0) == len(L1)}"
      + (f" (first difference at state {first})" if first is not None else ""))
print(f"(a) fallback flags equal: {F0 == F1} (long121 {sum(F0)}, reader {sum(F1)}); tau(o) changes in the reader run: "
      f"{sum(1 for k in range(len(L1) - 1) if L1[k][1][o] != L1[k + 1][1][o])}")
P0 = phases(L0, X0, range(40)); P1 = phases(L1, X1, range(41)); P1b = phases(L1, X1, base)
print(f"(a) phases long121: {P0}")
print(f"(a) phases reader (all 41): {P1}")
print(f"(a) phases reader (key on 0..39): {P1b}; equal to long121's: {P0 == P1b}; equal to reader all-41: {P1 == P1b}")
# (b)
ch = lambda X, v, a, b: sum(1 for t in range(a, b) if X[t][0][v] != X[t + 1][0][v])
print(f"(b) Xi(o) changes in [1, 122]: {ch(X1, o, 1, 122)}   (L-SI: 86; 2n = {2 * g1.n})")
for a, b in P1:
    if b > a:
        xr = max(range(g1.n), key=lambda v: ch(X1, v, a, b))
        print(f"(b) reader phase [{a}, {b}] len {b - a}: Xi(o) changes {ch(X1, o, a, b)}; XR = {ch(X1, xr, a, b)} at v {xr}")
for a, b in P0:
    if b > a:
        xr = max(range(g0.n), key=lambda v: ch(X0, v, a, b))
        print(f"    long121 phase [{a}, {b}] len {b - a}: XR = {ch(X0, xr, a, b)} at v {xr}")
