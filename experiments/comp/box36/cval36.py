#!/usr/bin/env python3
"""L-COMP box 36 item 3: validation of fast36's C counter (bin/next build) against own34.measure(extra=True)['C'] (and T3).
Sets: every genome file given on the command line, plus COUNT random genomes of the gen36 space (N 1-3, M 3-5, seed SEED).
Usage: cval36.py COUNT SEED [G.json ...]"""
import sys, os, json, random, subprocess, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box34")]
import fast36, own34, gen36
COUNT, SEED = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(SEED); c = collections.Counter()


def cc(G):
    n = G["N"] + 8 * sum(len(o) for o in G["opts"]) + 10; w = next(w for w in (1, 8, 16, 48) if n <= 64 * w)
    h = subprocess.run([os.path.join(H, "bin", "next", f"fast36_w{w}"), "one"], input=fast36.gtext(G), capture_output=True, text=True,
                       check=True).stdout.split("\n")[0].split()
    return int(h[1]), int(h[7])


def check(G, tag):
    T, C = cc(G); m = own34.measure(G, True, True); c["genomes"] += 1; c[f"C={m['C']}"] += 1
    if (T, C) != (m["T3"], m["C"]): c["MISMATCH"] += 1; print("MISMATCH", tag, (T, C), (m["T3"], m["C"]), flush=True)


for f in sys.argv[3:]: check(json.load(open(f)), os.path.basename(f))
for i in range(COUNT):
    N = rng.choice([1, 2, 3]); M = rng.randint(max(3, N), 5); lev, D, xts = rng.choice(list(gen36.blocks(N, M)))
    gate = list(range(M)); rng.shuffle(gate); br = list(range(M)); rng.shuffle(br)
    check(gen36.make(N, lev, D, xts, gate, br, [rng.randrange(2) for _ in range(M)], [rng.randrange(d) for d in D]), f"rand{i}")
print("FINAL cval36", COUNT, SEED, dict(c), flush=True)
