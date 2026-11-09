#!/usr/bin/env python3
"""Box 203 part 2 (L-NEW successor 68): hill-climb on genomes with Xi-feedback number k = 1, maximizing (maxasc, maxasc_faces, T) of
asc203.asc (ascents of e-sequences on IDEAL-CYC). Mutations keep every Xi-edge to a smaller index, to -1, or into the chosen f from
x <= f (so k <= 1); genomes with k != 1 are rejected. Resumable: state in OUT (json, rewritten every 25 iterations).
Usage: aclimb203.py SEED ITERS OUT   (env CMODE: eg195 generator mode for the start genome, default 'deep'; AC_START=G.json starts from
a given k = 1 genome (e.g. MWR4_2); AC_OBJ=flip maximizes (maxflip, D^tot sum at that gate, T) of gfc203 instead; AC_FREE=1 lets a mutation retarget a Xi-edge to ANY mover or -1, kept only if k stays 1)."""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import asc203, fvs202, eg195
FREE = os.environ.get("AC_FREE") == "1"; START = os.environ.get("AC_START")

def mutate(G, f, rng):
    H = copy.deepcopy(G); N = H["N"]; x = rng.randrange(N); j = rng.randrange(len(H["opts"][x])); o = H["opts"][x][j]; r = rng.random()
    if r < 0.35: o[1] = rng.choice(list(range(N)) + [-1]) if FREE else rng.choice(list(range(x)) + [-1] + ([f] if x <= f else []))
    elif r < 0.5 and H["lev"][x]: o[0] = rng.choice([y for y in range(N) if H["lev"][y] == H["lev"][x] - 1])
    elif r < 0.65: H["bp"][o[2]] ^= 1
    elif r < 0.8: b, c = o[2], rng.randrange(len(H["br"])); H["br"][b], H["br"][c] = H["br"][c], H["br"][b]
    elif r < 0.9: H["start"][x] = rng.randrange(len(H["opts"][x]))
    else:
        flat = [(y, i) for y in range(N) for i in range(len(H["opts"][y]))]
        (ya, ia), (yc, ic) = rng.choice(flat), rng.choice(flat); H["gate"][ya][ia], H["gate"][yc][ic] = H["gate"][yc][ic], H["gate"][ya][ia]
    return H

OBJ = os.environ.get("AC_OBJ", "asc")
def score(G):
    if OBJ == "flip":                        # the open quantity: per-gate flips and the faces' class heights (gfc203.census)
        import gfc203
        r = gfc203.census(G); return (r["maxflip"], sum(r["Dt"]), r["T"])
    r = asc203.asc(G); return (r["maxasc"], r["maxasc_faces"], r["T"])

if __name__ == "__main__":
    seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); mode = os.environ.get("CMODE", "deep")
    if os.path.exists(out): st = json.load(open(out)); G, f, it = st["G"], st["f"], st["it"]; rng.seed(seed * 100003 + it)
    elif START: G = json.load(open(START)); f = -1; it = 0
    else:
        while True:
            G = eg195.gen(rng, mode); N = G["N"]; f = rng.randrange(N)
            for x in range(N):
                for o in G["opts"][x]:
                    if o[1] >= 0 and not (o[1] < x or (o[1] == f and x <= f)): o[1] = -1
                    if x <= f and rng.random() < 0.4: o[1] = f
            if fvs202.kfvs(G)[0] == 1: break
        it = 0
    sc = score(G)
    while it < iters:
        it += 1; H = mutate(G, f, rng)
        if fvs202.kfvs(H)[0] != 1: continue
        s2 = score(H)
        if s2 >= sc:
            if s2 > sc: print("it", it, "score", s2, "N", H["N"], flush=True)
            G, sc = H, s2
        if it % 25 == 0: json.dump({"G": G, "f": f, "it": it, "score": sc}, open(out + ".tmp", "w")); os.replace(out + ".tmp", out)
    json.dump({"G": G, "f": f, "it": it, "score": sc}, open(out, "w")); print("FINAL seed", seed, "score", sc, flush=True)
