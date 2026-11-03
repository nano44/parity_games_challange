#!/usr/bin/env python3
"""L-RED R192 RKCLIMB: hill-climb IDEAL-ACYC W-ladders (r190/delclimb genome format and mutations; width w, degree D) for HIGH-RANK
unchained steps (L-NEW box 147 RANK, at any degree): pi := the genome's pi (a topological order of the Xi-graph); y_t := the max-pi
mover of step t; UNST(x) at state s := x has an option with a strictly better face; RANK_t := 1 + #{x unstable at s_(t-1) :
pi(x) > pi(y_t)}; unchained := box 144 ALL form as r190/delclimb SCORE=U (no least mover of step t-1 on the s_(t-1) Xi-chain of the
new option of any least mover of step t; steps t >= 2). Score = (#unchained steps with RANK > k, U, L); REL=1: RELRANK (frozen movers that move again later only).
stats(G, k) -> (L, U, HK, ranks of unchained steps, DEC) with DEC = #violations of box 147 DECREMENT read at degree D (y_t unstable
before, and no UNST bit above pi(y_t) changes). Usage: rkclimb.py d w D k iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r190")]
import ideal, fastcyc, delclimb
def unst(G, s):
    N, O = G["N"], G["opts"]; val, idx, _, _ = fastcyc.values(G, list(s))
    return [int(any(val(N + idx[(v, k)]) > val(N + idx[(v, s[v])]) for k in range(len(O[v])))) for v in range(N)]
def chain(G, s, v, k):
    O = G["opts"]; out = set(); x, kk = v, k
    while True:
        xt = O[x][kk][1]
        if xt < 0: return out
        out.add(xt); x, kk = xt, s[xt]
def stats(G, k, cap=5000):
    S, why = ideal.traj(G, cap=cap); N = G["N"]; lev = G["lev"]; pi = G["pi"]
    US = [unst(G, s) for s in S]; least = []; rk = {}; dec = 0
    for t in range(1, len(S)):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; l = min(lev[v] for v in mv); least.append([v for v in mv if lev[v] == l])
        y = max(mv, key=lambda v: pi[v]); rk[t] = 1 + sum(1 for x in range(N) if US[t - 1][x] and pi[x] > pi[y])
        if not US[t - 1][y] or any(US[t - 1][x] != US[t][x] for x in range(N) if pi[x] > pi[y]): dec += 1
    unch = [t for t in range(2, len(S)) if not (set(least[t - 2]) & set().union(*[chain(G, S[t - 1], h, S[t][h]) for h in least[t - 1]]))]
    if os.environ.get("REL") == "1":
        # RELRANK (r192/relrank.py): count only frozen movers above y_t that move again later (no padding)
        last = {v: max([t for t in range(1, len(S)) if S[t][v] != S[t - 1][v]], default=0) for v in range(N)}
        for t in unch:
            y = max((v for v in range(N) if S[t][v] != S[t - 1][v]), key=lambda v: pi[v])
            rk[t] = 1 + sum(1 for x in range(N) if US[t - 1][x] and pi[x] > pi[y] and last[x] > t)
    R = [rk[t] for t in unch]
    return len(S) - 1, len(unch), sum(1 for r in R if r > k), R, dec
if __name__ == "__main__":
    d, w, D, k, it, seed = map(int, sys.argv[1:7]); out = sys.argv[7]; rng = random.Random(seed)
    G = delclimb.rand(d, w, D, rng); L, U, hk, R, dec = stats(G, k); sc = (hk, U, L); best = (sc, G)
    for i in range(it):
        if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1])); sc = best[0]
        H2 = delclimb.mutate(G, rng); L, U, hk, R, dec = stats(H2, k); assert dec == 0, ("DECREMENT", dec)
        if (hk, U, L) >= sc: G, sc = H2, (hk, U, L)
        if sc > best[0]: best = (sc, json.loads(json.dumps(G))); json.dump(G, open(out, "w"))
    L, U, hk, R, dec = stats(best[1], k)
    print(f"RKCLIMB d {d} w {w} D {D} k {k} seed {seed} HIGH {hk} U {U} L {L} unchained ranks {sorted(R)}", flush=True)
