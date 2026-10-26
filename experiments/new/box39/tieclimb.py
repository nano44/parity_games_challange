#!/usr/bin/env python3
"""Box 39 (1): hill climb toward many TIE steps (S4a transitions inside a block with W unchanged on R̄ and an honest R̄-rise;
docs/new/N5-RW-box39.md). Canonical start (SPEC S3). Score = (max TIE in one block, total TIE, #block transitions). Mutations as
box38/nebclimb.py MODE=TAU (one Odd vertex of out-degree > 1 kept). Usage: tieclimb.py seed.pg rseed minutes outdir"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
os.environ.setdefault("MODE", "TAU")
from rwclass import *
import nebclimb as NC

def score(g):
    acc = {}
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()): analyse(g, None, acc, "c")
    if any(k.startswith("FAIL") for k in acc): return (10 ** 6, 0, 0)   # a lemma failure: report it at once
    t = acc.get("_ties", [0]); return (max(t), sum(t), acc.get("block_transitions", 0))

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
                with open(os.path.join(outdir, f"tie_{os.path.basename(f)[:-3]}_{seed}.pg"), "w") as h:
                    h.write(f"parity {g2.n - 1};\n")
                    for v in range(g2.n): h.write(f"{v} {g2.prio[v]} {g2.owner[v]} {','.join(map(str, g2.succ[v]))};\n")
            best, g = sc, g2
    print("FINAL", best, "after", it, flush=True)
