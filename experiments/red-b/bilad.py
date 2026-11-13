#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: the BI-LADDER family (a rule, not a climb).

A bi-ladder of depth d: movers 2l (u_l), 2l + 1 (v_l) at W-level l = 0..d-1.
  W (as in L^R_d): option k of a level-l mover has W-target 2(l - 1) + k (none at level 0).
  Xi (anti-aligned): option k of u_l has Xi-target 2(l + 1) + (k ^ a_l), of v_l 2(l + 1) + (k ^ b_l); at level d - 1 the exit.
  beta ranks LEVEL-MAJOR, top level most relevant (so a value is compared root-first from the exit, as a key is from level 0):
     rank(l, x, k) = 4 l + dl_l[2 (x - 2l) + k], dl_l a permutation of 0..3 (desirability of the 4 options of level l); all even
     (bp = 0), unless sg_l marks an option odd.
  eps: gate(l, x, k) = 4 l + ep_l[2 (x - 2l) + k], ep_l a permutation of 0..3.
  start: st_l in 0..3 = (s(u_l), s(v_l)) = (st >> 1, st & 1).
spec = list of d dicts {"a", "b", "dl", "ep", "st"} (optional "sg": 4 bits, 1 = odd priority).
genome(spec) returns the R104-format genome dict; `periodic` builds a spec from a bottom level, a list of interior level types
repeated, and a top level."""
import sys, json, itertools, random
import onep

PERM4 = list(itertools.permutations(range(4)))


def genome(spec):
    d = len(spec)
    N = 2 * d
    lev = [x // 2 for x in range(N)]
    opts = []
    gate = []
    br = [0] * (4 * d)
    bp = [0] * (4 * d)
    start = []
    for x in range(N):
        l, m = divmod(x, 2)
        L = spec[l]
        row = []
        grow = []
        for k in range(2):
            wt = 2 * (l - 1) + k if l > 0 else -1
            fl = L["a"] if m == 0 else L["b"]
            xt = 2 * (l + 1) + (k ^ fl) if l < d - 1 else -1
            b = 4 * l + 2 * m + k
            row.append([wt, xt, b])
            grow.append(4 * l + L["ep"][2 * m + k])
            br[b] = 4 * l + L["dl"][2 * m + k]
            bp[b] = (L.get("sg", 0) >> (2 * m + k)) & 1
        opts.append(row)
        gate.append(grow)
        start.append((L["st"] >> 1) & 1 if m == 0 else L["st"] & 1)
    return {"N": N, "lev": lev, "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": start}


def periodic(bottom, interior, top, d):
    spec = [bottom]
    i = 0
    while len(spec) < d - 1:
        spec.append(interior[i % len(interior)])
        i += 1
    spec.append(top)
    return spec


def T(spec, cap=200000):
    G = genome(spec)
    P = onep.OneP(G)
    return len(P.run("key", cap)) - 1


def rand_level(rng):
    return {"a": rng.randrange(2), "b": rng.randrange(2), "dl": list(rng.choice(PERM4)), "ep": list(rng.choice(PERM4)), "st": rng.randrange(4)}


if __name__ == "__main__":
    # quick random probe: bilad.py d count seed
    d, cnt, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    best = 0
    for i in range(cnt):
        spec = [rand_level(rng) for _ in range(d)]
        t = T(spec)
        if t > best:
            best = t
            print(f"d {d} i {i} T {t} spec {json.dumps(spec)}", flush=True)
