#!/usr/bin/env python3
"""Mutants of given genomes (L-RED-B): for each base file, <count> mutants, each 1..<maxmut> random mutations (mut.mutate,
Xi-edges free, so the Xi-feedback number is not kept), run on eng.py and checked by lev.check_run.
Usage: mutsweep.py <seed> <count> <maxmut> <refs: T|all> <file>...   One line per base and a total."""
import sys, os, json, random, time
import eng, lev, mut
seed, count, maxmut, refs = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
tot = {k: 0 for k in lev.CNT}; allrun = 0; t0 = time.time()
vf = open("viol_mut_s%d.jsonl" % seed, "a")
for f in sys.argv[5:]:
    rng = random.Random(seed * 7919 + sum(map(ord, os.path.basename(f))))
    base = mut.normalize(json.load(open(f)))
    c0 = {k: 0 for k in lev.CNT}; cov = {}; mx = {"T": 0, "platmax": 0, "mvals": 0}; n = 0
    while n < count:
        G = base
        for _ in range(rng.randint(1, maxmut)):
            G2 = mut.mutate(G, rng)
            if G2 is not None: G = G2
        if G is base: continue
        g = eng.build(G); tie = rng.choice(["keep-low", "high", "rand"])
        try: h = eng.howard_run(g, tie=tie, rng=rng, cap=20000)
        except RuntimeError: continue
        c, d = lev.check_run(g, h, refs=refs); n += 1
        if any(c[k] for k in lev.CNT): vf.write(json.dumps({"G": G, "tie": tie, "c": {k: c[k] for k in lev.CNT if c[k]}}) + "\n"); vf.flush()
        for k in lev.CNT: c0[k] += c[k]; tot[k] += c[k]
        for k in ("stalls", "stallloud", "plateaus", "beta", "cov_tie", "cov_bothY", "cov_bothYeq", "platsharp"): cov[k] = cov.get(k, 0) + d[k]
        for k in mx: mx[k] = max(mx[k], d[k])
    allrun += n
    print("MUT %s seed %d mutants %d refs %s | must0 %d | " % (os.path.basename(f), seed, n, refs, sum(c0.values())) +
          " ".join("%s %d" % (k, cov[k]) for k in sorted(cov)) + " | " + " ".join("max_%s %d" % (k, mx[k]) for k in sorted(mx)), flush=True)
print("MUTTOTAL seed %d runs %d | " % (seed, allrun) + " ".join("%s %d" % (k, tot[k]) for k in lev.CNT) + " | %.0fs" % (time.time() - t0))
