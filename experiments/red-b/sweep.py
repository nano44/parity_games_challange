#!/usr/bin/env python3
"""Sweeps of lev.check_run over generated genomes (L-RED-B). Usage:
  sweep.py rand <seed> <count> <Nmax> <Mmax> [refs=all|T] [shape]   random genomes (gen.rand_genome), random tie rule per run
  sweep.py exh <N> <M> [part parts]                                  every genome with N movers and M options (tiny sizes);
                                                                     with part / parts: one residue class of the outer loop
Prints one summary line; a genome with a non-zero must-0 counter is written to viol_<tag>.jsonl (one JSON per line)."""
import sys, json, random, itertools, time
import eng, gen, lev

def summarize(tag, tot, cov, mx, nrun, t0, nviol):
    print("SWEEP %s runs %d viol %d | " % (tag, nrun, nviol) + " ".join("%s %d" % (k, tot[k]) for k in lev.CNT) + " | " +
          " ".join("%s %d" % (k, cov[k]) for k in sorted(cov)) + " | " + " ".join("max_%s %s" % (k, mx[k]) for k in sorted(mx)) +
          " | %.0fs" % (time.time() - t0), flush=True)

def run_one(G, tie, rng, refs, tot, cov, mx, vf):
    g = eng.build(G)
    h = eng.howard_run(g, tie=tie, rng=rng)
    c, d = lev.check_run(g, h, refs=refs)
    bad = any(c[k] for k in lev.CNT)
    for k in lev.CNT: tot[k] += c[k]
    for k in d:
        if k.startswith("cov_") or k in ("stalls", "stallloud", "plateaus", "beta", "platsharp"): cov[k] = cov.get(k, 0) + d[k]
    for k in ("T", "platmax", "mvals", "phivals"):
        if d[k] > mx.get(k, 0): mx[k] = d[k]
    r = d["T"] / max(1, g.N); 
    if r > mx.get("T_over_N", 0): mx["T_over_N"] = round(r, 2)
    if bad:
        vf.write(json.dumps({"G": G, "tie": tie, "c": {k: c[k] for k in lev.CNT if c[k]}}) + "\n"); vf.flush()
    return bad

def main():
    mode = sys.argv[1]; t0 = time.time()
    tot = {k: 0 for k in lev.CNT}; cov = {}; mx = {}; nrun = 0; nviol = 0
    if mode == "rand":
        seed, count, Nmax, Mmax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
        refs = sys.argv[6] if len(sys.argv) > 6 else "all"; shape = sys.argv[7] if len(sys.argv) > 7 else "mix"
        tag = "rand_s%d_N%d_M%d_%s_%s" % (seed, Nmax, Mmax, refs, shape)
        rng = random.Random(seed); vf = open("viol_%s.jsonl" % tag, "w")
        while nrun < count:
            N = rng.randint(1, Nmax)
            G = gen.shaped(rng, N, shape)
            if sum(len(o) for o in G["opts"]) > Mmax: continue
            tie = rng.choice(["keep-low", "high", "rand"])
            nviol += run_one(G, tie, rng, refs, tot, cov, mx, vf); nrun += 1
            if nrun % 20000 == 0: summarize(tag + " (partial)", tot, cov, mx, nrun, t0, nviol)
    elif mode == "exh":
        N, M = int(sys.argv[2]), int(sys.argv[3]); tag = "exh_N%d_M%d" % (N, M)
        part = int(sys.argv[4]) if len(sys.argv) > 4 else 0; parts = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        if parts > 1: tag += "_p%dof%d" % (part, parts)
        vf = open("viol_%s.jsonl" % tag, "w"); rng = random.Random(0)
        # one tie rule is enough: reversing the option order of every mover maps "high" to "keep-low", and the
        # enumeration contains the reversed genome
        for G in gen.all_genomes(N, M, part, parts):
            nviol += run_one(G, "keep-low", rng, "all", tot, cov, mx, vf); nrun += 1
            if nrun % 500000 == 0: summarize(tag + " (partial)", tot, cov, mx, nrun, t0, nviol)
    summarize(tag, tot, cov, mx, nrun, t0, nviol)

if __name__ == "__main__":
    main()
