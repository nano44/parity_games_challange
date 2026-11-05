#!/usr/bin/env python3
"""L-RED R199: extract the move schedule, start and R_l flip steps of a genome's IDEAL run (r187/ideal.py), and F_l (TOTAL flips,
steps 1..L), as a synth.py spec (ladder W-targets read from the genome). Usage: schedof.py genome.json [spec_out.json]"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def run(G):
    N = G["N"]; O = G["opts"]; lev = G["lev"]; d = max(lev) + 1
    S, why = ideal.traj(G, cap=100000)
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    K = [keys(s) for s in S]
    R = [[k[2 * l] < k[2 * l + 1] for l in range(d)] for k in K]
    flips = {l: [t for t in range(1, len(S)) if R[t][l] != R[t - 1][l]] for l in range(d)}
    sched = {v: [t for t in range(1, len(S)) if S[t][v] != S[t - 1][v]] for v in range(N)}
    return S, why, flips, sched
def runs(F):   # longest run of consecutive levels l >= 1 with F_l >= 2 F_(l-1) and F_(l-1) >= 2
    best = cur = 0
    for l in range(1, len(F)):
        cur = cur + 1 if (F[l - 1] >= 2 and F[l] >= 2 * F[l - 1]) else 0; best = max(best, cur)
    return best
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); S, why, flips, sched = run(G); F = [len(flips[l]) for l in sorted(flips)]
    print("L", len(S) - 1, why, "F", F, "DBLRUN", runs(F))
    for l in sorted(flips): print(" R_%d flips" % l, flips[l])
    if len(sys.argv) > 2:
        sp = dict(d=max(G["lev"]) + 1, L=len(S) - 1, movers=[[G["lev"][v], [o[0] for o in G["opts"][v]]] for v in range(G["N"])],
                  sched={str(v): s for v, s in sched.items()}, start={str(v): G["start"][v] for v in range(G["N"])})
        json.dump(sp, open(sys.argv[2], "w")); print("spec", sys.argv[2])
