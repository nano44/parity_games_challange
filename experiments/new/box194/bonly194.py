#!/usr/bin/env python3
"""P-N5-QUIET fixes entry 1: DATA for Lemma B-ONLY and Corollary NO-TIE on IDEAL-CYC runs (box191 idealcyc via box192 rpot192).
bonlyfail: (state, vertex) pairs, v not c_W and not an e whose successor is c_W, with Lambda_t(v) an e-vertex or at least as relevant as
the least relevant e-vertex; ties: (state, gate) pairs with Omega(e_g) = Omega(beta_g). Usage: bonly194.py FILES.json | rand COUNT SEED"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "box192"), os.path.join(HERE, "..", "box191")]
import rpot192, rand191

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    evs = [v for v in range(h.n) if name[v][0] == "e"]; emin = min(E.rank[v] for v in evs); cW = V["cW"]
    s0 = rpot192.idealcyc.build(G)[1]; excl = {cW} | {e for e in evs if s0[e] == cW}
    gates = [(v, name[v][1]) for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    r = dict(T=len(ev) - 1, pairs=0, bonlyfail=0, gatestates=0, ties=0)
    for vs, sb in ev:
        for v in range(h.n):
            if v in excl: continue
            r["pairs"] += 1
            if E.rank[vs[v][0]] >= emin: r["bonlyfail"] += 1
        for g, q in gates:
            r["gatestates"] += 1
            if E.key(vs[V[("e", q)]]) == E.key(vs[V[("b", q)]]): r["ties"] += 1
    return r

fmt = lambda r: " ".join(f"{k} {v}" for k, v in r.items())
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = {}
        for i in range(cnt):
            for k, v in analyse(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))).items():
                tot[k] = max(tot.get(k, 0), v) if k == "T" else tot.get(k, 0) + v
        print(f"rand count {cnt} seed {seed}:", fmt(tot))
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), fmt(analyse(json.load(open(f)))))
