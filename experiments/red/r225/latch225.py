#!/usr/bin/env python3
"""L-RED 59 R225 item 1: independent check of L-SI 45 box 86 (claude/l-si 2123ae7a) ACCESS-LATCH / LEAPFROG / SAME-E-MERGE on
IDEAL-CYC Howard runs (R221 own.py; no L-SI code). For every mover B, SET-type option S (Xi-target B), state t with
Lambda_t(B) = lam in {K1, K2} and sigma_t(B) = S:
  HYP_t := no play from another gate g_o of B passes B, every o != S has Lambda(g_o) = lam or lower reward, and E_t(g_o) <=lex E_t(w)
           for every o != S with Lambda(g_o) = lam   (w = successor of e_S).
  latchviol: HYP_t and sigma_(t+1)(B) != S.
OFF events (sigma_t = S, sigma_(t+1) != S) are classified: cross (Lambda_(t+1)(B) != lam: outside FLIP's I), pass (some g_o passes B),
over (some o with Lambda(g_o) = lam, E(g_o) >lex E(w)), high (some o with higher-reward node), none (= LEAPFROG violation).
ON events (sigma_t != S, sigma_(t+1) = S) with Lambda(B) = lam at t and t+1: onviol if some o != S with Lambda(g_o) = lam has
E_t(g_o) >=lex {e_S} cup E_t(w).
SAME-E-MERGE: indeg(e) = indeg(gate) = 1 on Gamma(G) (own.build) and indeg of e / pe / g / m = 1 on Gamma3 (r223/own3.build3);
mergeviol: two vertices whose plays share an e-vertex in Pi but differ after it.
Usage: latch225.py G.json ... | latch225.py rand SEED COUNT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r221"), os.path.join(H, "..", "r223")]
import own
def lexgt(a, b, rk):
    d = a ^ b
    return bool(d) and max(d, key=lambda u: rk[u]) in a
def check(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk
    evs = {V[("e", q)] for q in O}; K1, K2 = V["K1"], V["K2"]
    c = dict(states=len(out), on=0, off=0, cross=0, pas=0, over=0, high=0, none=0, hyp=0, latchviol=0, onev=0, onviol=0, mergeviol=0)
    indeg = [0] * n
    for v in range(n):
        for w in succ[v]: indeg[w] += 1
    c["indeg1_G"] = all(indeg[V[(k, q)]] == 1 for q in O for k in ("e", "g"))
    try:
        import own3
        pr3, ow3, su3, _, _, V3 = own3.build3(G); d3 = [0] * len(pr3)
        for v in range(len(pr3)):
            for w in su3[v]: d3[w] += 1
        c["indeg1_G3"] = all(d3[V3[(k, q)]] == 1 for q in O for k in ("e", "pe", "g", "m"))
    except Exception as ex: c["indeg1_G3"] = "n/a " + str(ex)[:40]
    def play(s, tau, v):
        nxt = lambda u: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]))
        seq = []; seen = set()
        while v not in seen: seen.add(v); seq.append(v); v = nxt(v)
        return seq
    for t in range(len(out)):
        s, vals, tau = out[t]
        E = lambda v, pl=None: frozenset(u for u in (pl or play(s, tau, v)) if u in evs and u in vals[v][1])
        if t % 3 == 0 and n < 400:    # SAME-E-MERGE spot check every 3rd state
            pls = {v: play(s, tau, v) for v in range(n)}; first = {}
            for v in range(n):
                for i, u in enumerate(pls[v]):
                    if u in evs and u in vals[v][1]:
                        tail = tuple(pls[v][i:])
                        if u in first and first[u] != tail: c["mergeviol"] += 1
                        first.setdefault(u, tail)
        if t + 1 >= len(out): break
        s1, vals1, _ = out[t + 1]
        for B in range(N):
            for k, o in enumerate(G["opts"][B]):
                if o[1] != B: continue
                gS = V[("g", (B, k))]; lam = vals[B][0]
                if lam not in (K1, K2): continue
                eS = V[("e", (B, k))]; w = succ[eS][0]; Ew = E(w)
                others = [V[("g", (B, j))] for j in range(len(G["opts"][B])) if j != k]
                pl = {g: play(s, tau, g) for g in others}
                pas = any(B in pl[g] for g in others)
                high = any(vals[g][0] != lam and vj.rew(vals[g][0]) > vj.rew(lam) for g in others)
                Eg = {g: E(g, pl[g]) for g in others}
                over = any(vals[g][0] == lam and lexgt(Eg[g], Ew, rk) for g in others)
                onS, onS1 = s[B] == gS, s1[B] == gS
                if onS:
                    hyp = (not pas) and (not high) and not over
                    c["hyp"] += hyp
                    if not onS1:
                        c["off"] += 1
                        if hyp: c["latchviol"] += 1
                        if vals1[B][0] != lam: c["cross"] += 1
                        elif pas: c["pas"] += 1
                        elif over: c["over"] += 1
                        elif high: c["high"] += 1
                        else: c["none"] += 1
                    else: c["on"] += 1
                elif onS1 and vals1[B][0] == lam:
                    c["onev"] += 1
                    up = frozenset(Ew | {eS})
                    if any(vals[g][0] == lam and not lexgt(up, Eg[g], rk) for g in others): c["onviol"] += 1
    return c
def rgen(rng):
    d = rng.randint(2, 4); w = rng.randint(1, 3); D = rng.randint(2, 3); N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        os_ = []
        for _ in range(D):
            r = rng.random(); xt = x if r < 0.3 else (-1 if r < 0.45 else rng.randrange(N))
            os_.append([(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), xt, 0])
        opts.append(os_)
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); tot = {}
        for i in range(int(sys.argv[3])):
            G = rgen(rng); c = check(G)
            for k, v in c.items():
                if isinstance(v, bool): tot[k + "_false"] = tot.get(k + "_false", 0) + (not v)
                elif isinstance(v, int): tot[k] = tot.get(k, 0) + v
            if c["latchviol"] or c["none"] or c["onviol"] or c["mergeviol"]:
                json.dump(G, open(f"out/latchwit_{sys.argv[2]}_{i}.json", "w")); print("WIT", i, c, flush=True)
        print("RAND", sys.argv[2], sys.argv[3], tot, flush=True)
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), check(json.load(open(f))), flush=True)
