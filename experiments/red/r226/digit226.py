#!/usr/bin/env python3
"""L-RED 60 R226: THIRD-DIGIT family on CX4_n21. CX4's High source x17 runs a 2-digit counter
{e13} < {e14} < {e9,e8} < {e13,e8} < {e14,e8} (low digit e9/e13/e14, carry e8 brought to the low routes by x2's switch).
A multiplying depth would add a digit e_h above e8 and replay the 5 values with e_h (e8 dropped at the carry).
Gadget: h (level 1, 1 option: W-target wh in level 0, Xi-target yh), p (level 0 router, 2 options, Xi-targets p1, p2), and one new
option at an existing mover c (c in {x2, x7, x9, x17, x18}) with Xi-target h or p.  e_h's gate rank is TOP (above e8) with prob 1/2.
All targets sampled from all movers; ranks sampled. Score (Hn17 = #distinct values of x17 while Lambda(x17) is constant, T, maxD).
Usage: digit226.py CX4.json SEED COUNT OUTPREFIX"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
from compose226 import *
import own
A = json.load(open(sys.argv[1])); rng = random.Random(int(sys.argv[2])); CNT = int(sys.argv[3]); PRE = sys.argv[4]
def hn(G, x=17):
    out, V, O, ow = own.run(G, 3000); best = 0; t = 0
    while t < len(out):
        u = t
        while u + 1 < len(out) and out[u + 1][1][x][0] == out[t][1][x][0]: u += 1
        best = max(best, len({out[i][1][x][1] for i in range(t, u + 1)})); t = u + 1
    return best
def build(p):
    G = copy.deepcopy(A); N = G["N"]; h, r = N, N + 1
    G["N"] = N + 2; G["lev"] = G["lev"] + [1, 0]; G["opts"] = G["opts"] + [[], []]; G["gate"] = G["gate"] + [[], []]; G["start"] = G["start"] + [0, p["s"]]
    M = len(G["br"])
    G = add_opt(G, h, p["wh"], p["yh"], (M if p["top"] else p["g"][0]), p["b"][0], p["bp"][0])
    G = add_opt(G, r, -1, p["p1"], p["g"][1], p["b"][1], p["bp"][1]); G = add_opt(G, r, -1, p["p2"], p["g"][2], p["b"][2], p["bp"][2])
    G = add_opt(G, p["c"], (-1 if G["lev"][p["c"]] == 0 else p["wc"]), p["fb"], p["g"][3], p["b"][3], p["bp"][3])
    return G
L0 = [x for x in range(A["N"]) if A["lev"][x] == 0]
def sample():
    M0 = len(A["br"]); N = A["N"]; allx = list(range(N + 2)) + [-1]
    return dict(wh=rng.choice(L0 + [N + 1]), yh=rng.choice(allx), p1=rng.choice(allx), p2=rng.choice(allx), c=rng.choice([2, 7, 9, 17, 18]),
                wc=rng.choice(L0 + [N + 1]), fb=rng.choice([N, N + 1]), top=rng.random() < 0.5, g=[rng.randint(0, M0 + i) for i in range(4)],
                b=[rng.randint(0, M0 + i) for i in range(4)], bp=[rng.randrange(2) for _ in range(4)], s=rng.randrange(2))
if __name__ == "__main__":
    best = None; hist = {}
    for i in range(CNT):
        p = sample(); G = build(p)
        try: m = measure(G); m["Hn17"] = hn(G)
        except AssertionError: continue
        key = (m["Hn17"], m["T"], m["maxD"]); hist[key[:2]] = hist.get(key[:2], 0) + 1
        if best is None or key > best[0]:
            best = (key, m, p); json.dump(G, open(PRE + "_best.json", "w")); print("NEW", i, key, m, p, flush=True)
    print("HIST (Hn17, T)", sorted(hist.items())); print("BEST", best, flush=True)
