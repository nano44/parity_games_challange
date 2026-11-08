#!/usr/bin/env python3
"""L-RED 61 R227 (hold gadget / K-carry High): BLOCK COPY of a genome's mover set S.
copy(G, S, gpos, bpos, entries): new movers S' (same levels, opts); an edge from S into S goes to S', an edge leaving S keeps its original target.
  Gate ranks of S' are placed by gpos: "top" (all S' gates more relevant than every old gate), "bottom", or an int p (inserted at rank p).
  Beta ranks of S' likewise by bpos. entries = list of (x, fromopt): mover x gets a NEW option equal to its option fromopt with the Xi-target
  replaced by the copy of that target (the entry into S'); gate rank of the new option = just above x's fromopt gate (inter) or "top".
The K-chain: chain(G, S, K, ...) repeats copy K times, copy j taken of copy j-1 (so the gates ascend j by j).
Score: ascore226 (A = max(1, maxalt), #tops, T) on own.py IDEAL-CYC Howard ([E-LEV]); size N + M.
Usage: blockcopy227.py search G.json  |  blockcopy227.py chain G.json S(comma) K gpos entryspec"""
import sys, os, json, copy, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
from compose226 import check
from ascore226 import ascore
def _insert(ranks_all, newcount, pos):
    """ranks_all: list of existing ranks 0..M-1; return (shifted old ranks, new ranks list) inserting newcount ranks starting at pos."""
    old = [r + (newcount if r >= pos else 0) for r in ranks_all]; new = list(range(pos, pos + newcount)); return old, new
def copy_block(G, S, gpos="top", bpos="top", entries=(), entry_gate="inter", cmap=None):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"]); S = list(S); m = {x: N + i for i, x in enumerate(S)}
    cm = lambda y: m.get(y, y) if y >= 0 else y
    newopts = [[[cm(w) if w >= 0 and w in m else w, cm(t), None] for (w, t, b) in G["opts"][x]] for x in S]
    k = sum(len(o) for o in newopts)
    # gate ranks: old order of S's gates kept inside S'
    sg = sorted((G["gate"][x][j], i, j) for i, x in enumerate(S) for j in range(len(G["opts"][x])))
    gp = M if gpos == "top" else (0 if gpos == "bottom" else int(gpos))
    G["gate"] = [[r + (k if r >= gp else 0) for r in g] for g in G["gate"]]
    newgate = [[None] * len(o) for o in newopts]
    for rnk, (_, i, j) in enumerate(sg): newgate[i][j] = gp + rnk
    # beta ranks
    sb = sorted((G["br"][G["opts"][x][j][2]], i, j) for i, x in enumerate(S) for j in range(len(G["opts"][x])))
    bp_ = M if bpos == "top" else (0 if bpos == "bottom" else int(bpos))
    G["br"] = [r + (k if r >= bp_ else 0) for r in G["br"]]
    for rnk, (_, i, j) in enumerate(sb):
        bidx = len(G["br"]); G["br"].append(bp_ + rnk); G["bp"].append(G["bp"][G["opts"][S[i]][j][2]]); newopts[i][j][2] = bidx
    G["N"] = N + len(S); G["lev"] += [G["lev"][x] for x in S]; G["opts"] += newopts; G["gate"] += newgate; G["start"] += [G["start"][x] for x in S]
    for (x, fo) in entries:
        x = cmap.get(x, x) if cmap else x
        w, t, b = G["opts"][x][fo]; Mn = len(G["br"])
        g0 = G["gate"][x][fo]; gp2 = (Mn if entry_gate == "top" else g0 + 1)
        G["gate"] = [[r + (r >= gp2) for r in g] for g in G["gate"]]; G["gate"][x].append(gp2)
        bb = G["br"][b] + 1; G["br"] = [r + (r >= bb) for r in G["br"]] + [bb]; G["bp"].append(G["bp"][b])
        G["opts"][x].append([w, m.get(t, t), Mn])
    return G, m
def size(G): return G["N"] + len(G["br"])
def chain(G, S, K, gpos="top", bpos="top", entries=(), entry_gate="inter"):
    cur = list(S); res = [G]; cmap = {}
    for _ in range(K):
        G, m = copy_block(G, cur, gpos, bpos, entries, entry_gate, None)
        # next copy is taken of this copy; entries keep their original mover (x17 etc.) but point at the newest copy
        entries = [(x, len(G["opts"][x]) - 1) for (x, _) in entries]
        cur = [m[x] for x in cur]; res.append(G)
    return res
if __name__ == "__main__":
    if sys.argv[1] == "search":
        G0 = json.load(open(sys.argv[2])); N = G0["N"]; base = [7, 8, 9]; rest = [x for x in range(N) if x not in base]
        ENT = {"17": [(17, 0)], "17+18": [(17, 0), (18, 0)]}
        best = None; seen = 0; maxsub = int(os.environ.get("MAXSUB", "2"))
        for r in range(maxsub + 1):
            for extra in itertools.combinations(rest, r):
                S = base + list(extra)
                for gpos in ("top", "inter"):
                    gp = "top" if gpos == "top" else max(G0["gate"][8])  # just above x8's gate
                    for en, ent in ENT.items():
                        for eg in ("inter", "top"):
                            try:
                                G, _ = copy_block(G0, S, gp, "top", ent, eg); check(G); a = ascore(G)
                            except Exception as ex: continue
                            seen += 1
                            if best is None or a[:2] > best[0][:2]:
                                best = (a, S, gpos, en, eg); json.dump(G, open("out/bc_best.json", "w")); print("NEW", best, "size", size(G), flush=True)
        print("seen", seen, "BEST", best, flush=True)
