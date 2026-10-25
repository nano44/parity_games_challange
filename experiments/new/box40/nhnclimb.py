#!/usr/bin/env python3
"""Box 40 (2): hill climb AGAINST the N_HN bound (docs/new/N5-NHN-box40.md). Canonical start, MODE TAU mutations (box38/nebclimb.py).
Score = (FAIL, EV2post, maxNHN, EV2): FAIL = all FAIL_* of nhn.py (any > 0 saved as a counterexample candidate); EV2post = EV2 ends
past the (|U| − 2)-th fallback; maxNHN = max HN stretches in one τ(o) ≠ o phase; EV2 = all EV2 ends.
Usage: nhnclimb.py seed.pg rseed minutes outdir"""
import sys, os, random, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
os.environ.setdefault("MODE", "TAU")
import nhn as NH
import nebclimb as NC
from rhoclimb import save
from neb_run import load

def score(g):
    acc = {}
    with contextlib.redirect_stdout(io.StringIO()): NH.analyse(g, acc, "c")
    fail = sum(v for k, v in acc.items() if k.startswith("FAIL"))
    return (fail, acc.get("EV2_post", 0), acc.get("max_N_HN", (0,))[0], acc.get("EV2_ends", 0))

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
                print("IMPROVE", it, sc, flush=True); save(g2, os.path.join(outdir, f"nhc_{os.path.basename(f)[:-3]}_{seed}.pg"))
            best, g = sc, g2
    print("FINAL", best, "after", it, flush=True)
