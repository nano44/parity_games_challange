#!/usr/bin/env python3
"""EVERY Howard run of a genome (L-RED-B): R118 (a) lets ties among best successors be broken by any rule, so at a step
where some movers leave a non-best successor and have several best ones, every combination of choices is followed (a tree
of runs; at most <cap> complete runs per genome are checked, counted in "capped" when the tree is larger). Each complete run
is checked by lev.check_run with every reference state. Usage: ties.py <seed> <count> <Nmax> <Mmax> [cap=64] [shape=mix]
Only genomes whose tree has at least 2 runs are counted in <count>."""
import sys, random, itertools, time
import eng, gen, lev

def all_runs(g, cap):
    """Yield complete run histories (lists of states), depth-first over the tie choices."""
    out = []; capped = [False]
    def rec(sig, hist):
        if len(out) >= cap: capped[0] = True; return
        sbar, val, lam, pim, kk = eng.best_reply(g, sig, None)
        hist = hist + [{"sig": list(sig), "sbar": dict(sbar), "val": val, "lam": lam, "pim": pim, "kk": kk}]
        choices = []
        for x in range(g.N):
            vals = [val[w] for w in g.succ[x]]; bv = max(vals)
            if vals[sig[x]] == bv: choices.append([sig[x]])
            else: choices.append([k for k in range(len(vals)) if vals[k] == bv])
        if all(c == [sig[x]] for x, c in enumerate(choices)):
            out.append(hist); return
        if len(hist) > 200: raise RuntimeError("cap")
        for comb in itertools.product(*choices):
            rec(list(comb), hist)
            if len(out) >= cap: capped[0] = True; return
    rec(list(g.start), [])
    return out, capped[0]

def main():
    seed, count, Nmax, Mmax = map(int, sys.argv[1:5]); cap = int(sys.argv[5]) if len(sys.argv) > 5 else 64
    shape = sys.argv[6] if len(sys.argv) > 6 else "mix"
    rng = random.Random(seed); t0 = time.time()
    tot = {k: 0 for k in lev.CNT}; genomes = 0; runs = 0; ncap = 0; tried = 0; maxruns = 0; difft = 0; maxT = 0
    while genomes < count:
        G = gen.shaped(rng, rng.randint(2, Nmax), shape); tried += 1
        if sum(len(o) for o in G["opts"]) > Mmax: continue
        g = eng.build(G)
        rs, capped = all_runs(g, cap)
        if len(rs) < 2: continue
        genomes += 1; runs += len(rs); ncap += capped; maxruns = max(maxruns, len(rs))
        Ts = set(len(h) - 1 for h in rs); difft += (len(Ts) > 1); maxT = max(maxT, max(Ts))
        for h in rs:
            c, d = lev.check_run(g, h, refs="all")
            for k in lev.CNT: tot[k] += c[k]
    print("TIES seed %d genomes-with-a-tie-tree %d (of %d tried) runs %d max-runs-per-genome %d capped %d genomes-with-different-T %d max T %d | " % (
        seed, genomes, tried, runs, maxruns, ncap, difft, maxT) + " ".join("%s %d" % (k, tot[k]) for k in lev.CNT) + " | %.0fs" % (time.time() - t0))

if __name__ == "__main__":
    main()
