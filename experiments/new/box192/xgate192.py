#!/usr/bin/env python3
"""Box 192: X-GATE / TIE data. Per run: face ties (gates g and states t with Omega_t(e_g) = Omega_t(beta_g)); sigma-bar flips at gates
whose Xi-target is X (exit) and at gates whose Xi-target is a mover; max flips at one X-gate inside one joint Lambda-interval of
(e_g, beta_g); LOC check: sigma-bar_t(g) is a <=-least face at every gate and state. Usage: xgate192.py FILES.json | rand COUNT SEED"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, rand191

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    gates = [(v, name[v][1]) for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    r = dict(ties=0, flipsX=0, flipsM=0, maxXint=0, locfail=0)
    for g, q in gates:
        e, b = V[("e", q)], V[("b", q)]; isX = G["opts"][q[0]][q[1]][1] < 0; cnt = 0
        for t in range(len(ev)):
            vs, sb = ev[t]; ka, kb = E.key(vs[e]), E.key(vs[b])
            if ka == kb: r["ties"] += 1
            if E.key(vs[sb[g]]) != min(ka, kb): r["locfail"] += 1
            if t == 0: continue
            pv, ps = ev[t - 1]
            if pv[e][0] != vs[e][0] or pv[b][0] != vs[b][0]: cnt = 0
            if ps[g] != sb[g]:
                r["flipsX" if isX else "flipsM"] += 1
                if isX: cnt += 1; r["maxXint"] = max(r["maxXint"], cnt)
    return r

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = {}
        for i in range(cnt):
            a = analyse(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)))
            for k, v in a.items(): tot[k] = max(tot.get(k, 0), v) if k == "maxXint" else tot.get(k, 0) + v
        print(f"rand count {cnt} seed {seed}:", " ".join(f"{k} {v}" for k, v in tot.items()))
    else:
        for f in sys.argv[1:]:
            print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in analyse(json.load(open(f))).items()))
