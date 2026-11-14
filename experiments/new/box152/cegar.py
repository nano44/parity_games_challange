#!/usr/bin/env python3
"""L-NEW box 152 CEGAR: box151/xwake_anti.py (XT=1: per-option Xi-targets, ANTI=1, DEG ignored) proposes a schedule + Xi-targets for a
nested target; box152/valcheck.py logic checks it with those targets fixed (REL weights = distinct nonzero integers, a relaxation of
+-2^rank); on UNSAT a deletion-minimal core of C-requirements is turned into a NOGOOD: the core's C bits, the states (at the core's
states) of every mover on the two face chains of each core mover, and the Xi-targets of every option on those chains. The conflict
depends only on these literals (the face values involved are sums of the weights along exactly those chains), so every nogood is
sound. Loop until xwake UNSAT (=> exact UNSAT for the target with E levels above), a value-SAT proposal (=> REL witness; then EXACT
check), or the iteration cap. Usage: cegar.py target.json E workdir [ITERS=n]"""
import sys, os, json, subprocess, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box151")]
import req as RQ
tgt, E, wd = sys.argv[1], sys.argv[2], sys.argv[3]; os.makedirs(wd, exist_ok=True); ng_file = os.path.join(wd, "nogoods.json")
NG = json.load(open(ng_file)) if os.path.exists(ng_file) else []
ITERS = int(os.environ.get("ITERS", "50")); TMO = os.environ.get("TMO", "1200")
def reqs(W):
    S = W["states"]; KP = W["KP"]; lev = W["lev"]; N = len(lev); rq = {}
    for t in range(1, len(S)):
        for x in range(N):
            if lev[x] == 0 and S[t][x] == S[t - 1][x]: continue
            if S[t][x] != S[t - 1][x]: rq[(t - 1, x)] = S[t][x]
            elif KP[t][x] != S[t - 1][x]: rq[(t - 1, x)] = S[t - 1][x]
    return rq
import z3
def chain(S, xt, s, x, k):
    """options on the chain of (x, k) under state S[s], as a list of (mover, option)"""
    out = [(x, k)]; z = xt[(x, k)]
    while z >= 0: out.append((z, S[s][z])); z = xt[(z, S[s][z])]
    return out
def lincheck(S, xt, rq):
    """REL check with fixed targets: each face value is the sum of the weights on its chain; requirement (s, x) = b means
    face(x, b) > face(x, 1 - b). Strict linear inequalities over the reals (feasible set open, so distinct nonzero integer weights
    exist iff it is feasible). Returns ("sat"|"unsat", core) with a deletion-minimal core from z3 assumptions."""
    w = {}
    def W(f):
        if f not in w: w[f] = z3.Real(f"w{f[0]}_{f[1]}")
        return w[f]
    Z = z3.Solver(); A = {}
    for (s, x), b in rq.items():
        hi = z3.Sum([W(f) for f in chain(S, xt, s, x, b)]); lo = z3.Sum([W(f) for f in chain(S, xt, s, x, 1 - b)])
        a = z3.Bool(f"a{s}_{x}"); A[a] = (s, x); Z.add(z3.Implies(a, hi > lo))
    if Z.check(list(A)) == z3.sat: return "sat", None
    core = [A[a] for a in Z.unsat_core()]
    for key in list(core):
        trial = [k for k in core if k != key]
        if Z.check([a for a in A if A[a] in trial]) == z3.unsat: core = trial
    return "unsat", {k: rq[k] for k in core}
def premerge(S, xt, s, x):
    """the two pre-merge segments of x's face chains under S[s]: option lists up to (excluding) the first common mover, which is
    recorded as the last option's target; whole chains if they never meet"""
    A, B = chain(S, xt, s, x, 0), chain(S, xt, s, x, 1); ma = [y for (y, _) in A[1:]]; mb = [y for (y, _) in B[1:]]
    common = [y for y in ma if y in mb]
    if not common: return (tuple(A), tuple(B))
    m = common[0]; return (tuple(A[:ma.index(m) + 1]), tuple(B[:mb.index(m) + 1]))
for it in range(ITERS):
    json.dump(NG, open(ng_file, "w")); out = os.path.join(wd, f"w{it}.json"); t0 = time.time()
    env = dict(os.environ, XT="1", ANTI="1", TMO=TMO, NOGOODS=ng_file)
    p = subprocess.run(["python3", "-I", os.path.join(H, "..", "box151", "xwake_anti.py"), tgt, E, out], env=env, capture_output=True, text=True)
    line = [l for l in p.stdout.splitlines() if l.startswith("XWAKE")]
    res = line[0].split("->")[1].split()[0] if line else "error:" + p.stderr[-300:]
    print(f"IT {it} nogoods {len(NG)} xwake {res} ({time.time() - t0:.0f} s)", flush=True)
    if res != "sat": print("CEGAR END", res); break
    W = json.load(open(out)); S = [tuple(s) for s in W["states"]]; lev = W["lev"]; N = len(lev); WT = [m[1] for m in W["movers"]]
    xt = {(int(a.split(",")[0]), int(a.split(",")[1])): v for a, v in W["xt"].items()}; rq = reqs(W)
    r, core = lincheck(S, xt, rq)
    if r != "unsat":
        r2 = RQ.solve(lev, WT, S, rq, xtfix=xt, rel=False, tmo=1200)[0]
        print(f"CEGAR VALUE {r} (REL), EXACT {r2}: witness {out}"); break
    lits = set(); ks = sorted(core); pm = None
    if len(ks) == 2 and ks[0][1] == ks[1][1]:
        x = ks[0][1]; segs = [premerge(S, xt, s, x) for (s, _) in ks]
        if segs[0] == segs[1]: pm = segs[0]
    if pm is not None:
        # PREMERGE nogood: C(x) is a function of its two pre-merge segments (Lemma PREMERGE), so these literals alone conflict
        for (s, x2), b in core.items():
            lits.add(("C", s, x2, b))
            for k in (0, 1):
                for (y, kk) in pm[k]:
                    if y != x2: lits.add(("st", s, y, kk))
                    z = xt[(y, kk)]; lits.add(("eo", y, kk, z))
        NG.append(sorted(list(l) for l in lits)); print(f"  core {len(core)} {sorted(core.items())} PREMERGE nogood {len(lits)} lits", flush=True)
        continue
    for (s, x), b in core.items():
        lits.add(("C", s, x, b))
        for k in (0, 1):
            y, kk = x, k
            while True:
                z = xt[(y, kk)]; lits.add(("eo", y, kk, z))
                if z < 0: break
                lits.add(("st", s, z, S[s][z])); y, kk = z, S[s][z]
    NG.append(sorted(list(l) for l in lits)); print(f"  core {len(core)} {sorted(core.items())} nogood {len(lits)} lits", flush=True)
json.dump(NG, open(ng_file, "w"))
