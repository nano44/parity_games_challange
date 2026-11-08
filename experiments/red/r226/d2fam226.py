#!/usr/bin/env python3
"""L-RED 60 R226: DEPTH-2 RACE family on CX4_n21 (hand-specified shape, parameters sampled).
Added to CX4: router r (level 0, 2 options, Xi-targets y1, y2 on the High chain H = {x9, x10, x13, x14, x15, x17, x18, x19}),
bonus mover f (level 1, 1 option: W-target r, Xi-target y3 in H) = a second race (r's two routes, f's gate carries the bonus e_f),
and the FEEDBACK: a new option at the High source x17 with Xi-target f (or r).  Gate / beta ranks of the 4 new options sampled.
Score: T, maxD, X (comp225). Usage: d2fam226.py CX4.json SEED COUNT OUTPREFIX"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compose226 import *
A = json.load(open(sys.argv[1])); rng = random.Random(int(sys.argv[2])); CNT = int(sys.argv[3]); PRE = sys.argv[4]
Hc = [9, 10, 13, 14, 15, 17, 18, 19]
def build(p):
    G = copy.deepcopy(A); N = G["N"]; r, f = N, N + 1
    G["N"] = N + 2; G["lev"] = G["lev"] + [0, 1]; G["opts"] = G["opts"] + [[], []]; G["gate"] = G["gate"] + [[], []]; G["start"] = G["start"] + [0, 0]
    G = add_opt(G, r, -1, p["y1"], p["g"][0], p["b"][0], p["bp"][0]); G = add_opt(G, r, -1, p["y2"], p["g"][1], p["b"][1], p["bp"][1])
    G = add_opt(G, f, r, p["y3"], p["g"][2], p["b"][2], p["bp"][2]); G = add_opt(G, 17, -1, p["fb"], p["g"][3], p["b"][3], p["bp"][3])
    G["start"][r] = p["s"]; return G
def sample():
    M0 = len(A["br"])
    return dict(y1=rng.choice(Hc), y2=rng.choice(Hc), y3=rng.choice(Hc), fb=rng.choice([len(A["opts"]), len(A["opts"]) + 1]),
                g=[rng.randint(0, M0 + i) for i in range(4)], b=[rng.randint(0, M0 + i) for i in range(4)], bp=[rng.randrange(2) for _ in range(4)], s=rng.randrange(2))
if __name__ == "__main__":
    best = None; hist = {}
    for i in range(CNT):
        p = sample(); G = build(p)
        try: m = measure(G)
        except AssertionError as e: continue
        hist[m["T"]] = hist.get(m["T"], 0) + 1
        if best is None or (m["T"], m["maxD"]) > (best[0]["T"], best[0]["maxD"]):
            best = (m, p); json.dump(G, open(PRE + "_best.json", "w")); print("NEW", i, m, p, flush=True)
    print("HIST T", sorted(hist.items())); print("BEST", best)
