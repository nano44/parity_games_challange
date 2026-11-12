#!/usr/bin/env python3
"""Sweeps of lev3.check3 over genomes on Gamma3 (L-RED-B, B2 / box 209). Usage:
  sweep3.py rand <seed> <count> <Nmax> <Mmax> [refs=all|T] [shape]   random genomes (gen.shaped), random tie rule per run
  sweep3.py exh <N> <M> [part parts]                                  every genome with N movers and M options (gen.all_genomes;
           its two reductions hold on Gamma3 as well: pads are never cycle nodes and in no set Pi (R117 PAD), so their indices
           and priorities never decide a comparison; tie rule keep-low, reference every state)
  sweep3.py files <tie> <refs> FILE...                                frozen genomes
  sweep3.py mut <seed> <per> FILE...                                  per mutants (1-6 mutations, mut.mutate) of each file; random tie
Prints one summary line; a genome with a non-zero must-0 counter is appended to work/viol3_<tag>.jsonl."""
import sys, json, random, time, os
import eng, eng3, gen, lev3

def summarize(tag, tot, cov, mx, nrun, t0, nviol):
    print("SWEEP3 %s runs %d viol %d | " % (tag, nrun, nviol) + " ".join("%s %d" % (k, tot[k]) for k in lev3.CNT) + " | " +
          " ".join("%s %d" % (k, cov[k]) for k in sorted(cov)) + " | " + " ".join("max_%s %s" % (k, mx[k]) for k in sorted(mx)) +
          " | %.0fs" % (time.time() - t0), flush=True)

def run_one(G, tie, rng, refs, tot, cov, mx, vf):
    g = eng3.build3(G)
    h = eng3.how3_run(g, tie=tie, rng=rng)
    c, d = lev3.check3(g, h, refs=refs)
    bad = any(c[k] for k in lev3.CNT)
    for k in lev3.CNT: tot[k] += c[k]
    for k in ("stalls", "plateaus", "case3", "alpha", "beta"): cov[k] = cov.get(k, 0) + d[k]
    for k in ("T", "platmax", "mvals", "phivals", "tailmax", "intervals"):
        if d[k] > mx.get(k, 0): mx[k] = d[k]
    if d["platratio"] > mx.get("platratio", 0): mx["platratio"] = round(d["platratio"], 3)
    r = d["T"] / max(1, g.N + g.M)
    if r > mx.get("T_over_NM", 0): mx["T_over_NM"] = round(r, 3)
    if bad:
        vf.write(json.dumps({"G": G, "tie": tie, "c": {k: c[k] for k in lev3.CNT if c[k]}}) + "\n"); vf.flush()
    return bad, d

def main():
    mode = sys.argv[1]; t0 = time.time()
    tot = {k: 0 for k in lev3.CNT}; cov = {}; mx = {}; nrun = 0; nviol = 0
    os.makedirs("work", exist_ok=True)
    if mode == "rand":
        seed, count, Nmax, Mmax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
        refs = sys.argv[6] if len(sys.argv) > 6 else "all"; shape = sys.argv[7] if len(sys.argv) > 7 else "mix"
        tag = "rand_s%d_N%d_M%d_%s_%s" % (seed, Nmax, Mmax, refs, shape)
        rng = random.Random(seed); vf = open("work/viol3_%s.jsonl" % tag, "a")
        while nrun < count:
            N = rng.randint(1, Nmax)
            G = gen.shaped(rng, N, shape); G.pop("eorder", None)
            if sum(len(o) for o in G["opts"]) > Mmax: continue
            tie = rng.choice(["keep-low", "high", "rand"])
            nviol += run_one(G, tie, rng, refs, tot, cov, mx, vf)[0]; nrun += 1
            if nrun % 20000 == 0: summarize(tag + " (partial)", tot, cov, mx, nrun, t0, nviol)
    elif mode == "exh":
        N, M = int(sys.argv[2]), int(sys.argv[3]); tag = "exh_N%d_M%d" % (N, M)
        part = int(sys.argv[4]) if len(sys.argv) > 4 else 0; parts = int(sys.argv[5]) if len(sys.argv) > 5 else 1
        if parts > 1: tag += "_p%dof%d" % (part, parts)
        vf = open("work/viol3_%s.jsonl" % tag, "a"); rng = random.Random(0)
        for G in gen.all_genomes(N, M, part, parts):
            nviol += run_one(G, "keep-low", rng, "all", tot, cov, mx, vf)[0]; nrun += 1
            if nrun % 200000 == 0: summarize(tag + " (partial)", tot, cov, mx, nrun, t0, nviol)
    elif mode == "files":
        tie, refs = sys.argv[2], sys.argv[3]; tag = "files_%s_%s" % (tie, refs)
        vf = open("work/viol3_%s.jsonl" % tag, "a"); rng = random.Random(11)
        for p in sys.argv[4:]:
            G = eng.load(p)
            bad, d = run_one(G, tie, rng, refs, tot, cov, mx, vf); nviol += bad; nrun += 1
            print("FILE %s N %d M %d T3 %d tie %s bad %d phivals %d mvals %d plateaus %d platmax %d tail %d" % (
                os.path.basename(p), G["N"], sum(len(o) for o in G["opts"]), d["T"], tie, bad, d["phivals"], d["mvals"],
                d["plateaus"], d["platmax"], d["tailmax"]), flush=True)
    elif mode == "mut":
        seed, per = int(sys.argv[2]), int(sys.argv[3]); tag = "mut_s%d_x%d" % (seed, per)
        import mut
        vf = open("work/viol3_%s.jsonl" % tag, "a"); rng = random.Random(seed)
        for p in sys.argv[4:]:
            G0 = eng.load(p); G0.pop("name", None)
            for i in range(per):
                G = G0
                for _ in range(rng.randint(1, 6)):
                    H = mut.mutate(G, rng)
                    if H is not None: G = H
                G.pop("eorder", None)
                nviol += run_one(G, rng.choice(["keep-low", "high", "rand"]), rng, "T", tot, cov, mx, vf)[0]; nrun += 1
    summarize(tag, tot, cov, mx, nrun, t0, nviol)

if __name__ == "__main__":
    main()
