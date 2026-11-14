#!/usr/bin/env python3
"""L-NEW box 147 RANK: for every step t >= 1 of the run: y_t = the max-pi mover of step t; RANK_t = 1 + #(unstable movers at state t-1
with pi > pi(y_t)) (unstable = Xi-better option != current, deg 2). Checks (must be 0): YSTAB (y_t unstable before and stable after),
ABOVE (an UNST bit above pi(y_t) changes at step t), so TOP_k (desc-sorted pi-positions of the k highest unstable movers, lex) never
rises, and falls at t iff RANK_t <= k. Prints per genome the max RANK over unchained steps (= the least k with TOP_k falling at every
unchained step), over chained steps, and over all steps; and the histogram of unchained RANKs. Usage: rank.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "stat.py")
ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns); analyse = ns["analyse"]
def ranks(G, R):
    S, FS, pos, lab = R["S"], R["FS"], R["pos"], R["lab"]; n = G["N"]; out = {}; ystab = above = 0
    for t in range(1, len(S)):
        mv = [x for x in range(n) if S[t][x] != S[t - 1][x]]; y = max(mv, key=lambda x: pos[x])
        a, b = FS[t - 1]["UNST"], FS[t]["UNST"]
        ystab += not (a[y] == 1 and b[y] == 0); above += any(a[x] != b[x] for x in range(n) if pos[x] > pos[y])
        out[t] = 1 + sum(1 for x in range(n) if a[x] and pos[x] > pos[y])
    return out, ystab, above
if __name__ == "__main__":
    allu = {}
    for p in sys.argv[1:]:
        G = json.load(open(p)); R = analyse(G); rk, ys, ab = ranks(G, R); lab = R["lab"]
        un = [rk[t] for t in lab if not lab[t]]; ch = [rk[t] for t in lab if lab[t]]
        for r in un: allu[r] = allu.get(r, 0) + 1
        print(f"RANK {os.path.basename(p)} N {G['N']} STEPS {R['T']} U {len(un)} YSTAB {ys} ABOVE {ab} MAXR_UNCH {max(un, default=0)} "
              f"MAXR_CH {max(ch, default=0)} MAXR_ALL {max(rk.values(), default=0)} UNCH_RANKS {sorted(un)}")
    print("HIST unchained RANK:", dict(sorted(allu.items())))
