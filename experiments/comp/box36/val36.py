#!/usr/bin/env python3
"""L-COMP box 36 item 2(a): validation of the C engine fast36 (fast36.c) before any count is taken from it.
Set A (SMALL): random genomes of the exhaustive spaces gen36 (N 1-2, M 3-6; uniform block, uniform inner; seed SEED).
Set B (K1): L-NEW's k = 1 / k = 2 generator k1srch202.mk (eg195.gen 'acyc' + Xi-edges into 1 or 2 chosen movers; read-only import from
  a claude/l-new fa17fdf6 checkout, env LNEW), genomes with k = K1_MODE kept by MY kfvs (own36.kfvs).
Comparisons per genome (a MISMATCH is any difference):
  fast36 vs own36 (own34 engine): T3, fallback flag, every gate's (flips, lamch)       [all sets]
  fast36 vs L-NEW asc197.run (box 197 engine): T3                                    [set B, and set A when LNEW given]
  fast36 vs L-NEW k1srch202.census (box 202 counters): T3, maxflip, k1fail, k1c2fail  [same]
  own36.kfvs vs L-NEW fvs202.kfvs: k                                                  [same]
Usage: LNEW=<checkout> val36.py SET COUNT SEED  (SET = A or B1 or B2)."""
import sys, os, json, random, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import gen36, own36, fast36
SET, COUNT, SEED = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
LNEW = os.environ.get("LNEW")
if LNEW:
    os.environ["ROOT"] = LNEW; os.environ.setdefault("EG195_ROOT", LNEW); os.environ.setdefault("Q196_ROOT", LNEW)
    if SET.startswith("B"): os.environ["K1_MODE"] = SET[1]
    sys.path[:0] = [os.path.join(LNEW, p) for p in ("experiments/new/box202", "experiments/new/box197", "experiments/new/box196",
                    "experiments/new/box195", "experiments/new/box191", "experiments/new/box189", "experiments/new/box190",
                    "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
    import k1srch202, fvs202, asc197

rng = random.Random(SEED); c = collections.Counter(); first = None


def genA():
    N = rng.choice([1, 2]); M = rng.randint(3, 6); bl = list(gen36.blocks(N, M)); lev, D, xts = rng.choice(bl)
    gate = list(range(M)); rng.shuffle(gate); br = list(range(M)); rng.shuffle(br)
    bp = [rng.randrange(2) for _ in range(M)]; st = [rng.randrange(d) for d in D]
    return gen36.make(N, lev, D, xts, gate, br, bp, st)


while c["genomes"] < COUNT:
    if SET == "A": G = genA()
    else:
        G = k1srch202.mk(rng)
        if G is None: continue
        if own36.kfvs(G) != int(SET[1]): c["skipped_k"] += 1; continue
    T, fb, rows = fast36.one(G)
    o, r2 = own36.census(G, True, False)
    mine = sorted((tuple(a), f, l) for a, f, l in r2)
    bad = []
    if (T, fb) != (o["T3"], int(o["fallback"])): bad.append("T3/fb vs own36")
    if rows != mine: bad.append("gate rows vs own36")
    if LNEW:
        k_l = fvs202.kfvs(G)[0]
        if k_l != own36.kfvs(G): bad.append(f"k {k_l} vs {own36.kfvs(G)}")
        a = asc197.run(G)
        if a["T3"] != T: bad.append(f"T3 asc197 {a['T3']} vs {T}")
        Tl, k1f, mf = k1srch202.census(G); k1c2 = sum(k1srch202.bad2)
        my_k1f = sum(f > 2 * l + 1 for _, f, l in rows); my_k1c2 = sum(f > 2 * (l + 1) for _, f, l in rows)
        my_mf = max(f for _, f, _ in rows)
        if (Tl, k1f, mf, k1c2) != (T, my_k1f, my_mf, my_k1c2): bad.append(f"k1srch202 {(Tl, k1f, mf, k1c2)} vs {(T, my_k1f, my_mf, my_k1c2)}")
        c["lnew_compared"] += 1
    c["genomes"] += 1; c["T3sum"] += T; c["maxT3"] = max(c["maxT3"], T); c["maxflip"] = max(c["maxflip"], max(f for _, f, _ in rows))
    c["flipping_gates"] += sum(f > 0 for _, f, _ in rows); c["capped_or_nofb"] += fb == 0
    if bad:
        c["MISMATCH"] += 1
        if first is None:
            first = G; json.dump(G, open(os.path.join(H, "out", f"val36_mismatch_{SET}_{SEED}.json"), "w")); print("MISMATCH", bad, flush=True)
    if c["genomes"] % 250 == 0: print(dict(c), flush=True)
print("FINAL", SET, COUNT, SEED, dict(c), flush=True)
