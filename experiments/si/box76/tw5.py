#!/usr/bin/env python3
"""L-SI box 76b (DBL-O(1)): doubling levels. A level l >= 1 of a run is DOUBLING if F(l) = 2 F(l-1) + 2 (R113 PAIR-DOUBLE equality).
Checks Lemma DBL-EQ (docs/si/N5-TROPICAL-box76.md §7) at every doubling level: Phi_l(s_0) = 2, Phi_l(s_T) = 0, Phi_l(s_(t-1)) = 0 at
every l-b-step, no step moves both members, every step moving a member flips the pair l and every flip of the pair l moves a member,
moves(2l) = moves(2l+1) = F(l-1) + 1 (counter DBLEQ_VIOL). DATA: per run the set of doubling levels; the longest run of consecutive
doubling levels; witnesses. Corpus = tw.py corpus plus argv JSON files (stored start, or every start for N <= 10)."""
import sys, os, json, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tw import load_corpus, is_lr, Sim, analyse
def main():
    C = collections.Counter(DBLEQ_VIOL=0, NONTRIVIAL_CONSEC=0); best = {}; RAT = {}
    corpus = load_corpus() + [(p, json.load(open(p))) for p in sys.argv[1:]]
    for path, G in corpus:
        if not is_lr(G): continue
        sim = Sim(G); N = G["N"]; d = N // 2
        for s0 in (itertools.product((0, 1), repeat=N) if N <= 10 else [tuple(G["start"])]):
            S = sim.run(s0); a = analyse(sim, S); T = a["T"]; C["runs"] += 1
            F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
            mv = [sum(1 for t in range(1, T + 1) if y in a["Mv"][t]) for y in range(N)]
            dbl = [l for l in range(1, d) if F[l] == 2 * F[l - 1] + 2]
            for l in dbl:
                C["doubling levels"] += 1; p, q = 2 * l, 2 * l + 1
                Phi = lambda t: sum(1 for x in (p, q) if S[t][x] != a["c"][t][l])
                ok = Phi(0) == 2 and Phi(T) == 0
                for t in range(1, T + 1):
                    m = {p, q} & a["Mv"][t]
                    if a["flip"][t][l - 1] and Phi(t - 1) != 0: ok = False
                    if len(m) == 2: ok = False
                    if bool(m) != a["flip"][t][l]: ok = False
                ok = ok and mv[p] == mv[q] == F[l - 1] + 1
                gam = [G["gate"][p][k] < G["gate"][q][k] for k in range(2)]
                first = [min((t for t in range(1, T + 1) if x in a["Mv"][t]), default=None) for x in (p, q)]
                ok = ok and gam[0] == gam[1] and (first[0] < first[1]) == (not gam[0])
                C["DBLEQ_VIOL"] += not ok
            # longest run of consecutive doubling levels
            L = 0; cur = 0
            for l in range(1, d):
                cur = cur + 1 if l in dbl else 0; L = max(L, cur)
            nt = [l for l in dbl if l + 1 in dbl and F[l - 1] >= 1]
            if nt: C["NONTRIVIAL_CONSEC"] += 1; best.setdefault(("nt", d), (path.split("/")[-1], "".join(map(str, s0)), T, F))
            for l in dbl:
                C["max F(l-1) at a doubling level d%d" % d] = max(C["max F(l-1) at a doubling level d%d" % d], F[l - 1])
            for gap in (1, 2, 3):
                for l in range(gap, d):
                    r = (F[l] + 2) / (F[l - gap] + 2); kk = "ratio%d d%d" % (gap, d)
                    if kk not in RAT or r > RAT[kk][0]: RAT[kk] = (r, path.split("/")[-1], "".join(map(str, s0)), l, F)
            k = (d, L)
            if k not in best: best[k] = (path.split("/")[-1], "".join(map(str, s0)), T, F)
            C["maxconsec d%d" % d] = max(C["maxconsec d%d" % d], L)
    print("INFO " + " ".join("%s %d" % kv for kv in sorted(C.items())))
    for k in sorted((k for k in best if k[0] != "nt")): print("CONSEC d %d longest %d witness %s" % (k[0], k[1], best[k]))
    for k in sorted(RAT): print("RATIO %s max (F(l)+2)/(F(l-gap)+2) = %.4f witness %s" % (k, RAT[k][0], RAT[k][1:]))
    for k in sorted((k for k in best if k[0] == "nt"), key=str): print("NONTRIVIAL %s %s" % (k, best[k]))
if __name__ == "__main__":
    main()
