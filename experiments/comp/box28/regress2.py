#!/usr/bin/env python3
"""L-COMP box 28: regression of cnf2.py against the simulator (Lead 04:28Z items (b), (c)).
Pin a whole genome + start by unit clauses (the same pins as box27/pinck.py, applied to cnf2's variables): cnf2 must be SAT at
L = T and UNSAT at L = T + 1 (T = box27/sim.py's run length), and the SAT model, decoded by cnf2.decode, must give the simulator's
states s_0..s_T exactly (and the pinned genome back). Usage:
  regress2.py random N        N random 𝓛^R_3 and N random 𝓛^R_4 genomes (box27/pinck.rgen, seeds 2803/2804), stored starts
  regress2.py files F.json..  every start of each genome file (R-wired, 2-wide, degree 2)"""
import sys, os, json, itertools, random, types
B27 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27"); sys.path.insert(0, B27)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.environ.get("ENCDIR", "."))
import sim, importlib; cnf2 = importlib.import_module(os.environ.get("ENC", "cnf2"))
from pysat.solvers import Solver
_src = open(os.path.join(B27, "pinck.py")).read(); _src = _src[:_src.index('if sys.argv[1] == "files"')]
pinck = types.ModuleType("pinck"); pinck.__file__ = os.path.join(B27, "pinck.py"); exec(compile(_src, pinck.__file__, "exec"), pinck.__dict__)
def pinned(G, d, L):
    C, I = cnf2.build(d, L, None, "R")
    for (x, k) in I["opts"]:
        C.add([I["Xv"][(x, k)][G["opts"][x][k][1]]])
        b = G["opts"][x][k][2]; C.add([I["par"][(x, k)] if G["bp"][b] else -I["par"][(x, k)]])
    for o in I["opts"]:
        for o2 in I["opts"]:
            if o != o2: lit = I["rk"][(o, o2)]; C.add([lit if G["br"][G["opts"][o[0]][o[1]][2]] < G["br"][G["opts"][o2[0]][o2[1]][2]] else -lit])
    for l, V in I["gord"].items():
        for (a, b), lit in V.items(): C.add([lit if G["gate"][a[0]][a[1]] < G["gate"][b[0]][b[1]] else -lit])
    for x in range(G["N"]): a = I["S"][0][x]; C.add([a] if G["start"][x] else [-a])
    s = Solver(name="cadical195", bootstrap_with=C.cl); r = s.solve()
    return r, (cnf2.decode(s.get_model(), I) if r else None)
def check(G):
    d = G["N"] // 2; S, why = sim.run(G); T = len(S) - 1
    if T >= 1:
        r, M = pinned(G, d, T)
        if not r: return "SAT-at-T failed", T
        if [tuple(v) for v in M["states"]] != [tuple(v) for v in S]: return "decoded states differ", T
        if [[o[1] for o in ox] for ox in M["opts"]] != [[o[1] for o in ox] for ox in G["opts"]]: return "decoded Xi differ", T
    r, _ = pinned(G, d, T + 1)
    if r: return "SAT at T+1", T
    return None, T
os.environ.pop("SYM", None); os.environ.pop("CUBE", None)
bad = runs = 0; hist = {}
def one(G, tag):
    global bad, runs
    e, T = check(G); runs += 1; hist[T] = hist.get(T, 0) + 1
    if e: bad += 1; print("FAIL", tag, e, T, json.dumps(G), flush=True)
if sys.argv[1] == "random":
    n = int(sys.argv[2])
    for d in (3, 4):
        rng = random.Random(2800 + d)
        for i in range(n): one(pinck.rgen(rng, d), f"random d {d} #{i}")
else:
    for f in sys.argv[2:]:
        G0 = json.load(open(f))
        assert G0["lev"] == [x // 2 for x in range(G0["N"])] and all(G0["opts"][x][k][0] == (-1 if x < 2 else 2 * (x // 2 - 1) + k) for x in range(G0["N"]) for k in range(2)), f"{f} is not in the R-wired class"
        for st in itertools.product((0, 1), repeat=G0["N"]):
            G = dict(G0); G["start"] = list(st); one(G, f"{f} {st}")
print(f"regress2 {sys.argv[1]} ISO {os.environ.get('ISO')}: runs {runs}, T histogram {dict(sorted(hist.items()))}, failures {bad}", flush=True)
