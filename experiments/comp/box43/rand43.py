#!/usr/bin/env python3
"""L-COMP box 43 item 1: MY counters (lev43.census, genome mode, my engine) on genomes L-NEW's data did not draw:
  rand SEED COUNT NMMAX PX : random genomes by this lane's law (box40 ties40.rgen = box38 samp38's law at random (N, M), N + M <= NMMAX,
                             Ξ-target X with probability PX, else a uniform mover), every Ξ-feedback number (no resampling);
  mut SEED COUNT BASE.json : mutants of a frozen genome: 1 to 6 moves of box39/mut39.mutate (this lane's nine move kinds), not L-NEW's
                             aclimb203.mutate.
Prints the totals of the must-0 counters and the maxima of T, q, platmax, q / P, platmax / (N + 2M + 5), T / bound.
Usage: rand43.py rand SEED COUNT NMMAX PX | rand43.py mut SEED COUNT BASE.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box39")]
import lev43, mut39


def rgen(r, NMMAX, px):
    N = r.randint(3, NMMAX // 2); M = r.randint(N, min(3 * N, NMMAX - N)); lev = [0]
    for _ in range(N - 1): lev.append(lev[-1] + r.randrange(2))
    cuts = sorted(r.sample(range(1, M), N - 1)); D = [b - a for a, b in zip([0] + cuts, cuts + [M])]
    gate = list(range(M)); r.shuffle(gate); br = list(range(M)); r.shuffle(br); opts, gg, b = [], [], 0
    for x in range(N):
        oo, g1 = [], []
        for _ in range(D[x]):
            lower = [y for y in range(N) if lev[y] == lev[x] - 1]
            oo.append([-1 if lev[x] == 0 else r.choice(lower), (-1 if r.random() < px else r.randrange(N)), b]); g1.append(gate[b]); b += 1
        opts.append(oo); gg.append(g1)
    return {"N": N, "lev": lev, "opts": opts, "gate": gg, "br": br, "bp": [r.randrange(2) for _ in range(M)], "start": [r.randrange(d) for d in D]}


if __name__ == "__main__":
    a = sys.argv[1:]; r = random.Random(int(a[1])); cnt = int(a[2]); tot = dict.fromkeys(lev43.KEYS, 0)
    mx = dict(T=0, q=0, stalls=0, plateaus=0, platmax=0); rat = dict(qP=0.0, plat=0.0, T=0.0); done = 0; firsts = []
    G0 = json.load(open(a[3])) if a[0] == "mut" else None
    if G0 is not None: G0 = G0.get("genome", G0)
    while done < cnt:
        if a[0] == "rand": G = rgen(r, int(a[3]), float(a[4]))
        else:
            G = mut39.canon(G0)
            for _ in range(r.randint(1, 6)):
                G2 = mut39.mutate(G, r)
                if G2 is not None: G = G2
        P = lev43.genome_hist(G); c, d, first = lev43.census(P); done += 1
        for k in lev43.KEYS: tot[k] += c[k]
        for k in mx: mx[k] = max(mx[k], d[k])
        rat["qP"] = max(rat["qP"], d["q"] / P["bP"]); rat["plat"] = max(rat["plat"], d["platmax"] / P["bplat"]); rat["T"] = max(rat["T"], d["T"] / P["bT"])
        if first and len(firsts) < 3: firsts.append((done, first, json.dumps(G, sort_keys=True)))
    print(a[0], " ".join(a[1:]) if a[0] == "rand" else "%s seed %s" % (os.path.basename(a[3]), a[1]), "genomes", done, "ctrl", lev43.CTRL, "TOTALS", " ".join("%s %d" % (k, tot[k]) for k in lev43.KEYS),
          "MAX", " ".join("%s %d" % (k, mx[k]) for k in mx), "q/P %.2e platmax/(N+2M+5) %.3f T/bound %.2e" % (rat["qP"], rat["plat"], rat["T"]), flush=True)
    for i, f, G in firsts: print("   FAIL sample", i, f, G[:2000], flush=True)
