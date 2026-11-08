#!/usr/bin/env python3
"""L-RED 61 R227: HOLD GADGET template between a designed tower (HP_h_mup, L-SI pair84 generator) and GROW7's replaying low race.
Build: union(GROW7, HP) (compose226.union, tower gates/betas placed gm in {below, above}); u := the tower's top mover (most options), its options
k = 0..K-1 have Xi-targets z_k. For each k a NEW level-1 hold mover h_k with option A (W -> w, Xi -> z_k) and, if two, option B (W -> w, Xi -> x18:
the race; CX4's x9 / x14 pattern, whose improvement waits for the race tick). x17's options are REPLACED by K options Xi -> h_k (W -> cW), gate
ranks ascending in k, placed at x17's old top gate (hp = "old") or the global top (hp = "top"); beta ranks ascending (bq = "asc") or descending.
Sweep: gm x w (GROW7 level-0 movers) x two in {0, 1} x hp x bq. Score ascore226 (A, #tops, T) and ALT-H's H at the max-alt pair (alth227.check).
Freezes the best genome to out/hold_h<h>.json. Env KEEP=1: the KEEP variant (addhold). Usage: hold227.py GROW7.json HP.json TAG"""
import sys, os, json, copy, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import union, add_opt, check
from ascore226 import ascore
def build(A, B, gm, w, two, hp, bq, X=17, RACE=18, keep=0):
    G = union(A, B, gm); NA = A["N"]; u = NA + max(range(B["N"]), key=lambda x: len(B["opts"][x])); zs = [o[1] for o in G["opts"][u]]; K = len(zs)
    G = copy.deepcopy(G)
    if keep: return addhold(G, X, RACE, w, two, hp, bq, zs)
    # remove x17's options (gate and beta ranks compacted)
    gone = [o[2] for o in G["opts"][X]]; gr = sorted(G["gate"][X]); top_old = max(G["gate"][X])
    keep_b = [b for b in range(len(G["br"])) if b not in gone]; bmap = {b: i for i, b in enumerate(keep_b)}
    G["opts"][X] = []; G["opts"] = [[[w_, t, bmap[b]] for (w_, t, b) in o] for o in G["opts"]]
    allg = sorted(r for x, g in enumerate(G["gate"]) if x != X for r in g); gm_ = {r: i for i, r in enumerate(allg)}
    G["gate"] = [[gm_[r] for r in g] if x != X else [] for x, g in enumerate(G["gate"])]
    brs = [G["br"][b] for b in keep_b]; bo = {r: i for i, r in enumerate(sorted(brs))}; G["br"] = [bo[r] for r in brs]; G["bp"] = [G["bp"][b] for b in keep_b]
    gpos0 = sum(1 for r in allg if r < top_old) if hp == "old" else len(allg)
    hs = []
    for k in range(K):
        y = G["N"]; G["N"] += 1; G["lev"].append(1); G["opts"].append([]); G["gate"].append([]); G["start"].append(0); hs.append(y); M = len(G["br"])
        G = add_opt(G, y, w, zs[k], M, M, 0)
        if two: M = len(G["br"]); G = add_opt(G, y, w, RACE, M, 0, 0)
    for k in range(K):
        M = len(G["br"]); G = add_opt(G, X, -1, hs[k], gpos0 + k if hp == "old" else M, (M if bq == "asc" else 0), 0)
    G["start"][X] = 0
    return G
def addhold(G, X, RACE, w, two, hp, bq, zs):
    """KEEP variant: x17 keeps its own options (the low digit routes); the K hold options are ADDED (gates just above x17's top gate, or global top)."""
    hs = []
    for z in zs:
        y = G["N"]; G["N"] += 1; G["lev"].append(1); G["opts"].append([]); G["gate"].append([]); G["start"].append(0); hs.append(y); M = len(G["br"])
        G = add_opt(G, y, w, z, M, M, 0)
        if two: M = len(G["br"]); G = add_opt(G, y, w, RACE, M, 0, 0)
    for k, y in enumerate(hs):
        M = len(G["br"]); gp = (max(G["gate"][X]) + 1) if hp == "old" else M
        G = add_opt(G, X, -1, y, gp, (M if bq == "asc" else 0), 0)
    return G
if __name__ == "__main__":
    import alth227
    A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2])); TAG = sys.argv[3]; KEEP = int(os.environ.get("KEEP", "0")); L0 = [x for x in range(A["N"]) if A["lev"][x] == 0]
    best = None; hist = collections.Counter(); n = 0
    for gm in ("below", "above"):
        for w in L0:
            for two in (0, 1):
                for hp in ("old", "top"):
                    for bq in ("asc", "desc"):
                        try: G = build(A, B, gm, w, two, hp, bq, keep=KEEP); check(G); a = ascore(G)
                        except Exception as ex: hist["err"] += 1; continue
                        n += 1; hist[a[0]] += 1
                        if best is None or a[:2] > best[0][:2]:
                            best = (a, gm, w, two, hp, bq); json.dump(G, open(f"out/hold_{TAG}.json", "w")); print("NEW", best, "N", G["N"], "M", len(G["br"]), flush=True)
    nI, viol, al, Hc, T = alth227.check(json.load(open(f"out/hold_{TAG}.json")))
    print("runs", n, "A hist", sorted((k, v) for k, v in hist.items() if k != "err"), "err", hist["err"], "BEST", best, "ALT-H viol", viol, "H", Hc, flush=True)
