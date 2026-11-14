#!/usr/bin/env python3
"""L-RED R200 PCEGAR: exact prefix CEGAR on the xcnf model. P = xcnf model of the target's first T0 steps, F = xcnf model of the full
target (same E). Loop: P proposes (extra movers' states at t <= T0, extra gate bits); F checks the proposal by assumptions; F SAT = a
genome (replayed under r187/ideal.py); F UNSAT -> its core (a subset of the proposal literals; every full solution violates it) is added
to P as a no-good. P UNSAT = EXACT UNSAT for the full target (every full solution's prefix satisfies P and all no-goods).
No-goods are written to <prefix>_nogoods.json as they are found and reloaded on restart (resumable).
Usage: pcegar.py target.json E T0 prefix     (env SOLVER, MAXIT)"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import xcnf, ideal
from pysat.solvers import Solver
T = json.load(open(sys.argv[1])); E = int(sys.argv[2]); T0 = int(sys.argv[3]); pre = sys.argv[4]
TP = dict(T); TP["states"] = T["states"][:T0 + 1]
CP, IP = xcnf.build(TP, E); CF, IF = xcnf.build(T, E); N0, N = IF["N0"], IF["N"]
keys = [("s", t, v) for t in range(T0 + 1) for v in range(N0, N)] + [("g", l, k) for (l, k) in sorted(IF["Gb"])]
def var(I, key): return I["st"][(key[1], key[2])] if key[0] == "s" else I["Gb"][(key[1], key[2])]
ngf = pre + "_nogoods.json"; NG = json.load(open(ngf)) if os.path.exists(ngf) else []
sn = os.environ.get("SOLVER", "cadical195")
P = Solver(name=sn, bootstrap_with=CP.cl); F = Solver(name=sn, bootstrap_with=CF.cl)
def addng(ng):   # ng: list of [key, value]; clause: not all of them
    P.add_clause([-var(IP, tuple(k)) if val else var(IP, tuple(k)) for k, val in ng])
for ng in NG: addng(ng)
print(f"PCEGAR {sys.argv[1]} E {E} T0 {T0}: P vars {CP.n} F vars {CF.n}; reloaded nogoods {len(NG)}", flush=True)
it = 0; t00 = time.time()
while it < int(os.environ.get("MAXIT", "100000")):
    t0 = time.time(); rp = P.solve(); dp = time.time() - t0
    if not rp:
        print(f"PCEGAR iter {it}: P UNSAT ({dp:.1f} s) -> EXACT UNSAT for {sys.argv[1]} with E {E}; nogoods {len(NG)}; total {time.time() - t00:.0f} s", flush=True); break
    m = set(l for l in P.get_model() if l > 0)
    prop = {key: (var(IP, key) in m) for key in keys}
    asm = [var(IF, k) if val else -var(IF, k) for k, val in prop.items()]; back = {abs(a): k for a, k in zip(asm, prop)}
    t0 = time.time(); rf = F.solve(assumptions=asm); df = time.time() - t0
    if rf:
        G = xcnf.decode(F.get_model(), IF); json.dump(G, open(pre + "_genome.json", "w")); S2, why = ideal.traj(G)
        L, S0 = IF["L"], IF["S0"]; ok = len(S2) > L and all(tuple(S2[t][:N0]) == S0[t] for t in range(L + 1))
        print(f"PCEGAR iter {it}: F SAT ({df:.1f} s) -> {pre}_genome.json replay L {len(S2) - 1} {why} main prefix matches: {ok}", flush=True); break
    core = list(F.get_core() or asm)
    if os.environ.get("MINCORE", "1") == "1":   # deletion-based minimisation; a bounded solve that does not finish keeps the literal
        t1 = time.time(); i = 0
        while i < len(core):
            trial = core[:i] + core[i + 1:]; F.conf_budget(int(os.environ.get("MCBUD", "20000")))
            r = F.solve_limited(assumptions=trial)
            if r is False: core = [l for l in (F.get_core() or trial)]; continue
            i += 1
        df += 0; print(f"  mincore {len(core)} ({time.time() - t1:.1f} s)", flush=True)
    ng = [[list(back[abs(l)]), prop[back[abs(l)]]] for l in core if abs(l) in back]
    NG.append(ng); json.dump(NG, open(ngf, "w")); addng(ng)
    print(f"PCEGAR iter {it}: P {dp:.1f} s, F UNSAT {df:.1f} s, core {len(ng)} of {len(asm)}; nogoods {len(NG)}", flush=True)
    it += 1
