#!/usr/bin/env python3
"""L-SI box 36 (docs/si/N5-PIVOT-box36.md §3): BARRIER-SI data. Plain one-sided switch-all strategy improvement (si.py
rule_switch_all, start 'best' = PGSolver's initial_strategy_by_best_reward) on a game; per lambda-run (cycle-node map of Xi
constant) and per vertex: P-changes (PCH), carries (NM, R85's definition), matched changes (MAT), longest carry segment between
matched changes (SEG). Also checks (F-MON), SUCC-MON (L-NEW 35), LATE-RISE (L-NEW 35), SW-RETURN (R86) (must be 0 violations) and that
every transition changes Xi somewhere. --mut reverses the run (control: the premise counters must fire). Usage: barrier.py GAME.pg [RULE] [--mut]   (RULE default switch-all)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si"))
from n5x import load, Engine
from compose import matched, bits
g = load(sys.argv[1]); n = g.n; E = Engine(g)
av = [a for a in sys.argv[1:] if not a.startswith("--")]
rule = {"switch-all": E.rule_switch_all}[av[1] if len(av) > 1 else "switch-all"]
s = E.initial("best"); S = [s]
while True:
    val, _ = E.evaluate(s); imp = E.improving(s, val)
    if not imp: break
    s = rule(s, val, imp, None); S.append(s)
if "--mut" in sys.argv: S = S[::-1]                       # control: the reversed run must violate the premises
U = [E.evaluate(x)[0] for x in S]; T = len(S) - 1
rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1
def kind(a, b):
    if a == b or a[0] != b[0] or a[1] == b[1]: return None
    rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"
mon = sum(1 for t in range(T) for v in range(n) if E.key(U[t + 1][v]) < E.key(U[t][v]))
still = sum(1 for t in range(T) if U[t + 1] == U[t])
K = lambda t, v: E.key(U[t][v])
ev = [v for v in range(n) if g.owner[v] == 0]
smon = sum(1 for t in range(T) for y in ev if K(t + 1, S[t + 1][y]) < K(t, S[t][y]))           # SUCC-MON violations
late = 0                                                                                    # LATE-RISE violations
for y in ev:
    for z in g.succ[y]:
        inI = [K(t, z) > K(t, S[t][y]) for t in range(T + 1)]
        for u in range(T + 1):
            if inI[u]:
                tl = max((t for t in range(u) if not inI[t]), default=None)
                if tl is not None and not K(u, z) > K(tl, z): late += 1
swr = 0                                                                                     # SW-RETURN on the whole run
for y in ev:
    for z in g.succ[y]:
        ent = sum(1 for t in range(T) if S[t + 1][y] == z and S[t][y] != z); rise = sum(1 for t in range(T) if U[t + 1][z] != U[t][z])
        if ent > 1 + rise: swr += 1
lam = [tuple(u[v][0] for v in range(n)) for u in U]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
best = (0,); seg = 0
for i, j in zip(runs, runs[1:] + [T + 1]):
    for x in range(n):
        pc = nm = ma = cur = 0
        for t in range(i, j - 1):
            k = kind(U[t][x], U[t + 1][x])
            if k: pc += 1
            if k == "CAR": nm += 1; cur += 1; seg = max(seg, cur)
            if k == "MAT": ma += 1; cur = 0
        best = max(best, (pc, nm, ma, x, i, j))
pc, nm, ma, x, i, j = best
print(f"BARRIER {os.path.basename(sys.argv[1])} n {n} iter {T} lambda_runs {len(runs)} FMON_V {mon} SUCCMON_V {smon} LATERISE_V {late} SWRET_V {swr} STILL {still} "
      f"maxPCH {pc} (NM {nm} MAT {ma} vertex {x} run [{i},{j})) maxSEG {seg} {'PASS' if mon == smon == late == swr == still == 0 else 'FAIL'}")
