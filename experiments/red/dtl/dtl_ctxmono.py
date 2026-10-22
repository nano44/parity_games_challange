#!/usr/bin/env python3
"""L-RED (2026-10-16): test of Claim P (context monotonicity of the pruning) on one or many games.
Claim P: for a fixed subgame R (the only context best_vertices sees; forgiveness = "not in R") and a fixed player, the
pruning round in which a vertex is removed from V never DECREASES from one search to a later search of the same player
(the tangle set only grows). Survivors (stable V*, or the last-round prevV of a -1 result) count as round infinity.
Also tests Claim Q: with R fixed, the surviving set V* of a STABLE result never shrinks; and reports whether the -1 return
set (argmax survivors) changes between visits of the same R (it may: F7).
Usage: dtl_ctxmono.py GAME.pg [GAME2.pg ...] | --random N nmax seed   (random games via experiments/harness rngame-free generator)
Prints per game: contexts seen, pairs compared, Claim P violations, Claim Q violations, -1-set changes."""
import sys, os, random, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ff", os.path.join(HERE, "dtl_flipflop.py")); ff = importlib.util.module_from_spec(spec); spec.loader.exec_module(ff)

def profile(bv):
    INF = 10 ** 6
    d = {v: INF for v in bv["R"] if True}
    own = {v for r in bv["rounds"] for v in r["V"]} if bv["rounds"] else set()
    d = {v: INF for v in own}
    for k, r in enumerate(bv["rounds"]):
        for v in r["distractions"]:
            d[v] = k + 1
    if bv["result"] == -1:              # last survivors: pruned in the last round but returned as prevV; keep their round
        pass
    return d

def check(d):
    P = Q = M = pairs = 0; ctx = {}
    for s in d.searches:
        for bv in s["bv"]:
            if not bv["rounds"]: continue
            key = (s["player"], bv["R"])
            prof = profile(bv)
            if key in ctx:
                pprof, pres, pV = ctx[key]
                pairs += 1
                for v in prof:
                    if v in pprof and prof[v] < pprof[v]: P += 1
                if pres == 1 and bv["result"] == 1 and not bv["V"] >= pV: Q += 1
                if pres == -1 and bv["result"] == -1 and bv["V"] != pV: M += 1
            ctx[key] = (prof, bv["result"], bv["V"])
    return len(ctx), pairs, P, Q, M

def write_random(path, n, rng):
    with open(path, "w") as f:
        f.write(f"parity {n-1};\n")
        for v in range(n):
            succ = sorted({rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))})
            f.write(f"{v} {rng.randrange(n+1)} {rng.randrange(2)} {','.join(map(str, succ))};\n")

if __name__ == "__main__":
    if sys.argv[1] == "--random":
        N, nmax, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        import tempfile
        tot = [0] * 5; worst = None
        for i in range(N):
            p = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name
            write_random(p, rng.randrange(4, nmax + 1), rng)
            r = check(ff.load(p, "oink")); tot = [a + b for a, b in zip(tot, r)]
            if r[2] or r[3]:
                print(f"VIOLATION game {i}: contexts {r[0]} pairs {r[1]} P {r[2]} Q {r[3]} -1set {r[4]} ({p})"); worst = p
            else: os.unlink(p)
        print(f"random {N} games nmax {nmax} seed {seed}: contexts {tot[0]} pairs {tot[1]} ClaimP violations {tot[2]} ClaimQ violations {tot[3]} -1-set changes {tot[4]}")
    else:
        for g in sys.argv[1:]:
            r = check(ff.load(g, "oink"))
            print(f"{os.path.basename(g)}: contexts {r[0]} pairs {r[1]} ClaimP violations {r[2]} ClaimQ violations {r[3]} -1-set changes {r[4]}")
