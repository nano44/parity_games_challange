#!/usr/bin/env python3
"""Box 192: DEPTH test. For a step t -> t+1 and a vertex v with constant cycle node, pos(v) := 1 + #(e-vertices of Pi_t(v) more
relevant than the top of (Pi_t(v) xor Pi_t+1(v)) & E-set) (infinity if the e-part is unchanged). depth(t) := min_v pos(v).
If depth(t) <= c at every R-step, the top-c e-prefix argument bounds R by n (2M+3) (M+1)^c. Prints the depth sequence per label.
Usage: depth192.py FILES.json | depth192.py rand COUNT SEED"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192, rand191

INF = 99
def depths(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    ES = 0
    for v in range(h.n):
        if name[v][0] == "e": ES |= 1 << E.rank[v]
    K2 = [v for v in range(h.n) if name[v] == ("K", 2)][0]
    gates = [v for v in range(h.n) if h.owner[v] == 1]
    out = []
    for t in range(1, len(ev)):
        (pv, ps), (vs, sb) = ev[t - 1], ev[t]
        C = any(pv[v][0] != vs[v][0] for v in range(h.n)); fl = any(ps[g] != sb[g] for g in gates)
        lab = "C" if C else ("R" if fl else "p"); best = INF
        for v in range(h.n):
            if pv[v][0] != vs[v][0]: continue
            d = (pv[v][1] ^ vs[v][1]) & ES
            if not d: continue
            top = d.bit_length() - 1
            best = min(best, 1 + bin((pv[v][1] & ES) >> (top + 1)).count("1"))
        out.append((lab, best))
    return out

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); hist = {}
        for i in range(cnt):
            G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            for lab, d in depths(G): hist[(lab, d)] = hist.get((lab, d), 0) + 1
        print(f"rand {cnt} seed {seed}:", sorted(hist.items()))
    else:
        for f in sys.argv[1:]:
            G = json.load(open(f)); ds = depths(G)
            print(os.path.basename(f), "N", G["N"], "R-depth max", max([d for l, d in ds if l == "R"] or [0]), " ".join(f"{l}{d}" for l, d in ds))
