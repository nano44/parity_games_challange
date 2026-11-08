#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 1 (W-3 fix (a), D-1, D-4): box81/pacyc81.py (unchanged, cited by the frozen packet) copied here with
REFEREE-2 32's two diffs applied (claude/referee-2 bf02e618 docs/referee-2/R2-P-ACYC/pacyc81_tau_counter.diff, pacyc81_full_run.diff):
  taubad    states 0..k1-1 whose tau is not R118 (k)'s standard tau (tau(g) = pe_g at every gate, tau(K2) = K2)
  after     histogram: iterations after the first fallback until N5'-xi stops (value: genomes)
Original docstring follows.
L-SI box 81, packet P-ACYC DATA on Gamma3(G) (R117's padded game; ref/ gamma3.build with pads {K, pe, pb, m}). N5'-xi from S3
(ref/ box190 n5v.step, mode xi, one iteration at a time; S3 = n5x.start_pair with no start). Records the FIRST FALLBACK k1 (least k such
that iteration k, the transition from state k-1 to state k, has S4c's fallback flag), then on states 0..k1-1:
  notbeta   (state, gate) pairs where sigma-bar (si.py Engine, the optimal counterstrategy to sigma_t) is not the beta-face pad pbeta_g
  nonstd    states where some Even vertex other than a mover differs from S3's start (non-standard state)
  lamchg    consecutive state pairs where some vertex's cycle node changes (C-steps)
  sbchg     consecutive state pairs where sigma-bar changes somewhere, cycle nodes equal (R-steps)
  bigT      genomes with k1 - 1 > N (P-ACYC Corollary ACYC-XI says 0 on Xi-acyclic genomes)
Sets: FILES, and COUNT Xi-acyclic genomes from lemma81.agen (seed SEED). Usage: pacyc81.py COUNT SEED [FILES.json]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RN = os.path.join(HERE, "ref", "experiments", "new")
sys.path[:0] = [HERE, os.path.join(RN, "box190"), os.path.join(RN, "box21"), os.path.join(RN, "box189")]
import n5v, n5x, gamma3, lemma81
PADS = {"K", "pe", "pb", "m"}


def one(G, cap=10 ** 4):
    g, sig0, tau0, V = gamma3.build(G, PADS); N = G["N"]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    movers = {V[("x", x)] for x in range(N)}
    gates = [(V[("g", (x, k))], V[("pbeta", (x, k))]) for x in range(N) for k in range(len(G["opts"][x]))]
    states = [list(sigma)]; taus = [list(tau)]; k1 = None; it = 0
    while it < cap:
        r = n5v.step(g, E, Ed, sigma, tau, "xi")
        if r is None: break
        it += 1; sigma, tau, _, _, fb = r; sigma, tau = list(sigma), list(tau)
        if fb and k1 is None: k1 = it
        if k1 is None: states.append(list(sigma)); taus.append(list(tau))
        continue
    s0 = states[0]; notb = nonstd = lamchg = sbchg = 0; prev = None
    for s in states:
        vals, sb = E.evaluate(tuple(s))
        notb += sum(1 for gt, pb in gates if sb[gt] != pb)
        if any(s[v] != s0[v] for v in range(g.n) if g.owner[v] == 0 and v not in movers): nonstd += 1
        key = ([vals[v][0] for v in range(g.n)], [sb[v] for v in range(g.n) if g.owner[v] == 1])
        if prev is not None:
            if key[0] != prev[0]: lamchg += 1
            elif key[1] != prev[1]: sbchg += 1
        prev = key
    K2 = V[("K", 2)]; pe = [V[("pe", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))]
    gts = [V[("g", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))]
    taubad = sum(1 for t in taus if t[K2] != K2 or any(t[gq] != pq for gq, pq in zip(gts, pe)))
    return dict(taubad=taubad, N=N, k1=k1, T3=(k1 - 1) if k1 else None, iters=it, notbeta=notb, nonstd=nonstd, C=lamchg, R=sbchg)


if __name__ == "__main__":
    cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
    tot = dict(taubad=0, genomes=0, states=0, nofallback=0, notbeta=0, nonstd=0, C=0, R=0, bigT=0, maxT3_over_N=0.0)
    for f in sys.argv[3:]:
        r = one(json.load(open(f)))
        print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in r.items()))
    gl = [json.load(open(f)) for f in sys.argv[3:]]
    for i in range(cnt):
        gl.append(lemma81.agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)))
    import collections; after = collections.Counter()
    for G in gl:
        r = one(G); tot["genomes"] += 1; after[r["iters"] - (r["k1"] or 0)] += 1
        if r["k1"] is None: tot["nofallback"] += 1; continue
        tot["states"] += r["T3"] + 1
        for k in ("notbeta", "nonstd", "C", "R", "taubad"): tot[k] += r[k]
        tot["bigT"] += r["T3"] > r["N"]; tot["maxT3_over_N"] = max(tot["maxT3_over_N"], round(r["T3"] / r["N"], 3))
    print("iterations after the first fallback (value: genomes):", dict(sorted(after.items())))
    print(f"pacyc81 count {cnt} seed {seed} files {len(sys.argv) - 3}:", " ".join(f"{k} {v}" for k, v in tot.items()))
