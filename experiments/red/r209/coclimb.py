#!/usr/bin/env python3
"""L-RED R209 COCLIMB: co-designed attack on TOP-C. Hill-climb a WHOLE genome of L_d (r207/gclimb.py mutations on every level, the
top included; AUX helpers, WFREE) under the constraint «exactly C couplings» (options of non-top movers with Xi-target in the top
level); score (gain', T) with gain' := T(G) - max over acyclic re-routings r of the couplings (X or any non-top mover) of T(G^-_r)
from the same start (R208 exact definition; exhaustive). SCORE=rearm scores (R, T), R := #steps after the first top-moving step that move a lower mover (re-armed lower steps; cheap);
SCORE=excess scores (T(G) - TREF, gain') instead (TREF env).
Seed: SEED=<genome> (extended to depth d by gclimb.extend); if it has != C couplings, random retargets / repairs are applied.
Usage: coclimb.py d C iters seed out.json"""
import sys, os, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r207"), os.path.join(H, "..", "r208"), os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import gclimb, ideal
from coupext import acyc
def T(G): return len(ideal.traj(G, cap=100000)[0]) - 1
def couplings(G):
    top = max(G["lev"]); return [(v, k) for v in range(G["N"]) if G["lev"][v] < top for k in range(len(G["opts"][v])) if G["opts"][v][k][1] >= 0 and G["lev"][G["opts"][v][k][1]] == top]
def gainp(G, cs=None):
    top = max(G["lev"]); U = {v for v in range(G["N"]) if G["lev"][v] == top}; keep = [v for v in range(G["N"]) if v not in U]
    mp = {v: i for i, v in enumerate(keep)}; cs = couplings(G) if cs is None else cs
    base = dict(N=len(keep), lev=[G["lev"][v] for v in keep], gate=[G["gate"][v] for v in keep], br=G["br"], bp=G["bp"], start=[G["start"][v] for v in keep],
                opts=[[[mp[o[0]] if o[0] >= 0 else -1, mp[o[1]] if o[1] in mp else -1, o[2]] for o in G["opts"][v]] for v in keep])
    best = -1
    for r in itertools.product(list(range(len(keep))) + [-1], repeat=len(cs)):
        Hh = json.loads(json.dumps(base))
        for (v, k), y in zip(cs, r): Hh["opts"][mp[v]][k][1] = y
        if acyc(Hh["opts"]): best = max(best, T(Hh))
    return T(G) - best, best
SC = os.environ.get("SCORE", "gain"); TREF = int(os.environ.get("TREF", "0"))
def rearm(G):
    top = max(G["lev"]); U = [v for v in range(G["N"]) if G["lev"][v] == top]; S = ideal.traj(G, cap=100000)[0]
    cuts = [t for t in range(1, len(S)) if any(S[t][u] != S[t - 1][u] for u in U)]
    if not cuts: return 0, len(S) - 1
    R = sum(1 for t in range(cuts[0] + 1, len(S)) if any(S[t][v] != S[t - 1][v] for v in range(G["N"]) if v not in U))
    return R, len(S) - 1
def score(G, C):
    if len(couplings(G)) != C: return None
    if SC == "rearm": return rearm(G)
    g, b = gainp(G); t = T(G)
    return (t - TREF, g) if SC == "excess" else (g, t)
def force(G, C, rng):
    top = max(G["lev"]); U = [v for v in range(G["N"]) if G["lev"][v] == top]
    for _ in range(1000):
        cs = couplings(G)
        if len(cs) == C: return G
        H2 = json.loads(json.dumps(G))
        if len(cs) > C: v, k = rng.choice(cs); H2["opts"][v][k][1] = -1
        else:
            v = rng.choice([u for u in range(G["N"]) if G["lev"][u] < top]); k = rng.randrange(len(G["opts"][v])); H2["opts"][v][k][1] = rng.choice(U)
            pos = sorted(range(H2["N"]), key=lambda u: H2["pi"][u])
            if not acyc(H2["opts"]): continue
            # recompute pi as a topological order
            N = H2["N"]; adj = [[o[1] for o in oo if o[1] >= 0] for oo in H2["opts"]]; indeg = [0] * N
            for a in range(N):
                for b in adj[a]: indeg[b] += 1
            order = [a for a in range(N) if indeg[a] == 0]; i = 0
            while i < len(order):
                for b in adj[order[i]]:
                    indeg[b] -= 1
                    if indeg[b] == 0: order.append(b)
                i += 1
            H2["pi"] = [0] * N
            for j, a in enumerate(order): H2["pi"][a] = j
        G = H2
    raise SystemExit("cannot force C")
if __name__ == "__main__":
    d, C, it, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); out = sys.argv[5]; rng = random.Random(seed)
    G = force(gclimb.extend(json.load(open(os.environ["SEED"])), d, rng), C, rng); sc = score(G, C)
    best = (sc, G); stale = 0
    for i in range(it):
        H2 = gclimb.mutate(G, rng); s2 = score(H2, C)
        if s2 is None: continue
        if s2 >= sc: G, sc = H2, s2
        if s2 > best[0]: best = (s2, json.loads(json.dumps(H2))); json.dump(H2, open(out, "w")); stale = 0
        stale += 1
        if stale > 6000: G, sc, stale = json.loads(json.dumps(best[1])), best[0], 0
    json.dump(best[1], open(out, "w")); print(f"COCLIMB d {d} C {C} AUX {gclimb.AUX} SCORE {SC} seed {seed} best {best[0]}")
