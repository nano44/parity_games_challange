#!/usr/bin/env python3
"""Box 39: hill climb AGAINST Theorem P-FREEZE (docs/new/N5-RW-box39.md §11). Canonical start. Score = (FAIL, lastP, fb): FAIL = #FBF/PFZ
failures (any > 0 is a counterexample candidate, saved), lastP = max over θ-constant phase runs of the #fallbacks completed
before the last P-change on U (the theorem: ≤ |U| − 1; a run with more counts as FAIL), fb = max fallbacks in one θ-run. Mutations as box38/nebclimb.py
MODE=TAU. Env PFZ_SCORE=excess: score = (FAIL, max over θ-runs with |U| ≥ 3 of #fallbacks − (|U| − 1), lastP): pushes runs into the
post-freeze regime. Usage: pfzclimb.py seed.pg rseed minutes outdir"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
os.environ.setdefault("MODE", "TAU")
import pfreeze as PF
import nebclimb as NC
from neb_run import load

def score(g):
    acc = {}
    with contextlib.redirect_stdout(io.StringIO()): PF.analyse(g, None, acc, "c")
    fail = acc.get("FAIL_FBF", 0) + acc.get("FAIL_PFZ", 0) + acc.get("post_freeze_crossings", 0) * 0
    late = acc.get("_late", -99); fb = acc.get("max_fb_in_run", (0,))[0]
    fail += 1 if late > 0 else 0
    if os.environ.get("PFZ_SCORE") == "excess": return (fail, acc.get("_excess", -99), acc.get("_lastP", 0))
    return (fail, acc.get("_lastP", 0), fb)

if __name__ == "__main__":
    f, seed, mins, outdir = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    os.makedirs(outdir, exist_ok=True); rng = random.Random(seed); g = load(f); assert NC.ok(g)
    best = score(g); t0 = time.time(); it = 0; print("START", best, flush=True)
    while time.time() - t0 < 60 * mins:
        it += 1; g2, _ = NC.mutate(rng, g, [-1] * g.n)
        if not NC.ok(g2): continue
        try: sc = score(g2)
        except Exception: continue
        if sc >= best:
            if sc > best:
                print("IMPROVE", it, sc, flush=True)
                with open(os.path.join(outdir, f"pfz_{os.path.basename(f)[:-3]}_{seed}.pg"), "w") as h:
                    h.write(f"parity {g2.n - 1};\n")
                    for v in range(g2.n): h.write(f"{v} {g2.prio[v]} {g2.owner[v]} {','.join(map(str, g2.succ[v]))};\n")
            best, g = sc, g2
    print("FINAL", best, "after", it, flush=True)
