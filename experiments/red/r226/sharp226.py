#!/usr/bin/env python3
"""L-RED 60 R226: check Lemma SHARP (R226-race.md §3): in every LEAPFROG-ASC unit (PRIV + NODE),
  #events <= |E_U| - 1 + eps + 2k,  eps = 1 iff the first event is an ON with b_t = empty (else 0),  k = #type-II events;
and its parts: (P1) an event with M = e_S is an ON with a_t = {e_S}, b_t = empty; (P2) at most one such event, and it is the first.
Modes: sharp226.py files G.json ... | sharp226.py rand SEED COUNT | sharp226.py climb SEED RESTARTS ITER (score = excess over the bound).
Witnesses (excess > 0 or P1/P2 fail) frozen to out/sharpwit_*.json."""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import exshow226 as ex, latch225
ex.THR = -10 ** 9
def units(G, cap=3000):
    ex.DUMP.clear(); c = ex.census(G, cap); assert len(ex.DUMP) == c["units_hyp"], "dump"; return list(ex.DUMP)
def judge(G, cap=3000):
    # returns (max excess over the bound, #units, p1fail, p2fail, #units with eps=1, max ev)
    us = units(G, cap); mx = -99; p1 = p2 = ne = 0; mev = 0
    for d in us:
        EU = d["EU"]; eS = (d["B"], d["k"]); evl = d["ev"]; mev = max(mev, len(evl))
        kk = 0; Mis = []
        for j, (i, dr, a, b, arg) in enumerate(evl):
            sa, sb = set(a), set(b)
            # the type-II test needs ranks; recompute from E_U order: E_U is sorted by (x, k) here, so use census's typeII count instead
            atS = (sa | sb) == {eS}          # M = e_S  <=>  a u b = {e_S} (a, b are subsets of E_U and e_S in a)
            Mis.append(j if atS else None)
            if atS and not (dr == "ON" and sa == {eS} and not sb): p1 += 1
        idx = [j for j in Mis if j is not None]
        if len(idx) > 1 or (idx and idx[0] != 0): p2 += 1
        eps = 1 if (evl and evl[0][1] == "ON" and not evl[0][3]) else 0; ne += eps
        kk = d.get("kII", 0)
        mx = max(mx, len(evl) - (len(EU) - 1 + eps + 2 * kk))
    return mx, len(us), p1, p2, ne, mev
def mutate(G, rng):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; r = rng.random()
    x = rng.randrange(N); k = rng.randrange(len(G["opts"][x]))
    if r < 0.3: G["opts"][x][k][1] = rng.choice(list(range(N)) + [-1, x])
    elif r < 0.45 and lev[x] >= 1: G["opts"][x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r < 0.65:
        i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.75: i = rng.randrange(len(G["bp"])); G["bp"][i] ^= 1
    elif r < 0.9:
        y = rng.randrange(N); k2 = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][k2] = G["gate"][y][k2], G["gate"][x][k]
    else: G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G
if __name__ == "__main__":
    mode = sys.argv[1]; agg = dict(g=0, units=0, p1=0, p2=0, eps1=0, mx=-99, mev=0)
    def acc(G, tag):
        mx, nu, p1, p2, ne, mev = judge(G); agg["g"] += 1; agg["units"] += nu; agg["p1"] += p1; agg["p2"] += p2; agg["eps1"] += ne
        agg["mev"] = max(agg["mev"], mev)
        if nu: agg["mx"] = max(agg["mx"], mx)
        if mx > 0 or p1 or p2: json.dump(G, open("out/sharpwit_%s.json" % tag, "w")); print("WIT", tag, mx, p1, p2, flush=True)
        return mx, mev
    if mode == "files":
        for f in sys.argv[2:]: print(os.path.basename(f), judge(json.load(open(f))), flush=True); acc(json.load(open(f)), os.path.basename(f)[:-5])
    elif mode == "rand":
        rng = random.Random(int(sys.argv[2]))
        for i in range(int(sys.argv[3])): acc(latch225.rgen(rng), "r%s_%d" % (sys.argv[2], i))
    elif mode == "climb":
        rng = random.Random(int(sys.argv[2]))
        for rr in range(int(sys.argv[3])):
            G = latch225.rgen(rng); m = judge(G, 400); s = (m[0], m[5])
            for it in range(int(sys.argv[4])):
                Hh = mutate(G, rng)
                try: m2 = judge(Hh, 400)
                except Exception: continue
                s2 = (m2[0], m2[5])
                if s2 >= s: G, s = Hh, s2
                if s[0] > 0: break
            acc(G, "c%s_%d" % (sys.argv[2], rr)); print("R", rr, s, flush=True)
    print("AGG", mode, sys.argv[2:4], agg, flush=True)
