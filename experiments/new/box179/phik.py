#!/usr/bin/env python3
"""L-NEW box 179: exact check of the LP-found potential PHI_K(s) = sum_x (2^(d - lev(x)) - 1) * k_s(x) on L^R_d, k_s(x) = [s(x) != KP_s(x)]
(key-misaligned). Checks PHI_K(s) - PHI_K(step(s)) >= 1 at every step s -> step(s) != s. Every state for d <= 4, given starts otherwise.
Usage: phik.py ngen seed [files...]"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
rand_lr, is_lr = fl["rand_lr"], fl["is_lr"]
def phik(g, d, s):
    K = g.keys(s); t = 0
    for x in range(2 * d):
        kp = min((0, 1), key=lambda j: g.optkey(K, x, j)); t += ((1 << (d - x // 2)) - 1) * (s[x] != kp)
    return t
C = dict(transitions=0, viol=0, mindrop=10 ** 9, tight=0)
def chk(G, states, tag):
    g = Gen(G); d = G["N"] // 2
    for s in states:
        s = tuple(s); n, _ = g.step(s)
        if n is None: continue
        a, b = phik(g, d, s), phik(g, d, n); C["transitions"] += 1; C["mindrop"] = min(C["mindrop"], a - b); C["tight"] += a - b == 1
        if a - b < 1:
            C["viol"] += 1
            if C["viol"] <= 5: print("VIOL", tag, s, n, a, b)
rng = random.Random(int(sys.argv[2]))
for i in range(int(sys.argv[1])):
    d = rng.randint(1, 5); G = rand_lr(d, rng, iso=rng.random() < 0.3)
    chk(G, itertools.product((0, 1), repeat=2 * d) if d <= 4 else [G["start"]] + [[rng.randint(0, 1) for _ in range(2 * d)] for _ in range(200)], "rand%d" % i)
for f in sys.argv[3:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    g = Gen(G); S, _ = g.run(G["start"]); chk(G, S, f)
print(" ".join("%s %d" % kv for kv in C.items()))
