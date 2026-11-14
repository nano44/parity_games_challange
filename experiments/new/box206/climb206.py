#!/usr/bin/env python3
"""Box 206 (L-NEW successor 70): hill-climb at Xi-feedback number k = 1 maximizing the CHANGE DEPTH of depth206 (score = (maxdepth,
#changes at that depth, T)), with box 203 aclimb203's mutations (AC_FREE=1: retarget a Xi-edge anywhere, kept only if k stays 1).
CL_OBJ=block: score = (Dtop - F0(b), Dtop, T) of block206.py (START may be rand:B). CL_OBJ=loud: score = (#loud steps of loud depth >= 2, max loud depth, T) instead.
Resumable: state in OUT (json, rewritten every 25 iterations). Usage: AC_FREE=1 climb206.py SEED ITERS OUT START.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "box203")]
os.environ.setdefault("AC_FREE", "1")
import aclimb203, fvs202, depth206

OBJ = os.environ.get("CL_OBJ", "deep")
def score(G):
    c, g = depth206.census(G)
    if OBJ == "block":                     # CONJECTURE BLOCK-DESC: maximize Dtop - F0(b) (block206.py)
        import block206
        r = block206.census(G); return (r["excess"], r["Dtop"], r["T"])
    if OBJ == "loud": return (sum(c["L%d" % i] for i in range(3, 10)), c["maxloud"], c["T"])   # loud steps of loud depth >= 2
    return (g, c["d%d" % min(g, 9)], c["T"])

if __name__ == "__main__":
    seed, iters, out, start = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]; rng = random.Random(seed)
    if os.path.exists(out): st = json.load(open(out)); G, it = st["G"], st["it"]; rng.seed(seed * 100003 + it)
    elif start.startswith("rand:"):      # rand:B = the first k = 1 genome of k1srch202.mk(seed) whose top block has B e-vertices
        os.environ["K1_MODE"] = "1"; import k1srch202, block206
        while True:
            G = k1srch202.mk(rng)
            if G is not None and fvs202.kfvs(G)[0] == 1 and block206.census(G)["b"] == int(start[5:]): break
        it = 0
    else: G = json.load(open(start)); it = 0
    assert fvs202.kfvs(G)[0] == 1
    sc = tuple(score(G)); print("start", sc, "N", G["N"], flush=True)
    while it < iters:
        it += 1; H = aclimb203.mutate(G, -1, rng)
        if fvs202.kfvs(H)[0] != 1: continue
        s2 = score(H)
        if s2 >= sc:
            if s2 > sc: print("it", it, "score", s2, "N", H["N"], flush=True)
            G, sc = H, s2
        if it % 25 == 0: json.dump({"G": G, "it": it, "score": sc}, open(out + ".tmp", "w")); os.replace(out + ".tmp", out)
    json.dump({"G": G, "it": it, "score": sc}, open(out, "w")); print("FINAL seed", seed, "score", sc, flush=True)
