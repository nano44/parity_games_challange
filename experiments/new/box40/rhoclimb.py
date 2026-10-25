#!/usr/bin/env python3
"""Box 40: hill climb into the post-freeze regime of HAT-FREEZE / RHO-TAIL (docs/new/P-N5-RHO-box40.md). Canonical start.
A phase is PAST the hat freeze at state t if |U| ≥ 3 and t > g_{|U|−2} (the phase's (|U| − 2)-th in-phase fallback transition).
Score = (FAIL, H1post, excess): FAIL = all FAIL_* counters of box39/rho.py (any > 0 is a counterexample candidate, saved);
H1post = number of H1 states past the hat freeze, over phases with |U| ≥ 3; excess = max over phases with |U| ≥ 3 of
#fallbacks − (|U| − 2) (over phases with |U| above the largest |U| already past the freeze). Env RHC_SCORE=bigU: score =
(FAIL, maxU past the freeze with an H1 state after it, excess, H1post). Mutations: box38/nebclimb.py (MODE default TAU here). Usage:
  rhoclimb.py survey game.pg ...          per-file (H1post, excess, maxU of such phases)
  rhoclimb.py climb seed.pg rseed minutes outdir"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
os.environ.setdefault("MODE", "TAU")
import rho as RH
import nebclimb as NC
from neb_run import load, trace

def post(g):
    rows, o, E = trace(g, None); N = len(rows); h1post = 0; a = 0; maxU = 0; ph = []
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        ct = rows[a]["Xi"][o][0]; u = sum(1 for z in range(g.n) if rows[a]["Xi"][z][0] == ct)
        fbs = [k for k in range(a, b) if rows[k]["fb"]]
        if u >= 3 and any(r["h1"] for r in rows[a:b + 1]):
            c = sum(1 for t in range(fbs[u - 3] + 1, b + 1) if rows[t]["h1"]) if len(fbs) >= u - 2 else 0
            h1post += c; ph.append((u, len(fbs) - (u - 2)))
            if c: maxU = max(maxU, u)
        a = b + 1
    excess = max([e for u, e in ph if u > maxU], default=-99)
    return h1post, excess, maxU
def score(g):
    acc = {}
    with contextlib.redirect_stdout(io.StringIO()): RH.analyse(g, acc, "c")
    fail = sum(v for k, v in acc.items() if k.startswith("FAIL"))
    h, e, m = post(g)
    if os.environ.get("RHC_SCORE") == "bigU": return (fail, m, e, h)
    return (fail, h, e)

def save(g, p):
    with open(p, "w") as h:
        h.write(f"parity {g.n - 1};\n")
        for v in range(g.n): h.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")

if __name__ == "__main__":
    if sys.argv[1] == "survey":
        for f in sys.argv[2:]:
            try: g = load(f)
            except Exception: continue
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            print(f, g.n, *post(g), flush=True)
        sys.exit(0)
    f, seed, mins, outdir = sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    os.makedirs(outdir, exist_ok=True); rng = random.Random(seed); g = load(f); assert NC.ok(g)
    best = score(g); t0 = time.time(); it = 0; print("START", best, flush=True)
    while time.time() - t0 < 60 * mins:
        it += 1; g2, _ = NC.mutate(rng, g, [-1] * g.n)
        if not NC.ok(g2): continue
        try: sc = score(g2)
        except Exception: continue
        if sc >= best:
            if sc > best:
                print("IMPROVE", it, sc, flush=True); save(g2, os.path.join(outdir, f"rhc_{os.path.basename(f)[:-3]}_{seed}.pg"))
            best, g = sc, g2
    print("FINAL", best, "after", it, flush=True)
