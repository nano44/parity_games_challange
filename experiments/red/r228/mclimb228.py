#!/usr/bin/env python3
"""L-RED 62 R228 item 3: falsification climb for L-SI 47 BOX 90's CONJECTURE RA-MULT(K) (m(y, z) <= K) on R221 own.py (IDEAL-CYC Howard,
[E-LEV], the genome's start; cap 600 steps). Own census, no L-SI / L-NEW code:
  per (v, maximal Lambda-interval I): tops = most relevant element of each change of E_t(v) (e-vertices only); for letters y, z:
  m(y, z) := #gaps between consecutive y-tops whose most relevant top is z (box 90 §0's definition).
  Counters: maxm = max over (v, I, y, z) of m(y, z) (a PER-QUADRUPLE MAXIMUM); nm = #quadruples (v, I, y, z) with m(y, z) = maxm (a TOTAL);
  C = max over (v, I, y) of c_y (per-triple maximum); idfail (unit (v, I, y)): c_y - 1 != sum_z m(y, z); T = steps of the run.
Score = (maxm, C, nm, -size), size N + M <= CAP. Moves: sharp226.mutate and the GROW moves of depthclimb227 (copied).
Freezes every strict (maxm, C) gain to out/mc_<CAP>_<SEED>.json, and any maxm >= 3 genome also to out/mkill_<SEED>_<maxm>.json.
Resumable: RESUME=<frozen json>. Usage: mclimb228.py SEED CAP ITER START.json | mclimb228.py --census G.json ..."""
import sys, os, json, random, copy, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
def census(G, cap=600):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; c = dict(maxm=0, nm=0, C=0, idfail=0, T=T); ms = []
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            Es = [frozenset(e for e in out[i][1][v][1] if e in evs) for i in range(t, u + 1)]
            tops = [max(a ^ b, key=lambda e: rk[e]) for a, b in zip(Es, Es[1:]) if a != b]
            t = u + 1
            pos = collections.defaultdict(list)
            for i, z in enumerate(tops): pos[z].append(i)
            for y, P in pos.items():
                m = collections.Counter(max(tops[i + 1:j], key=lambda e: rk[e]) for i, j in zip(P, P[1:]) if j > i + 1)
                if len(P) - 1 != sum(m.values()): c["idfail"] += 1
                c["C"] = max(c["C"], len(P)); ms.extend(m.values())
    if ms: c["maxm"] = max(ms); c["nm"] = ms.count(c["maxm"])
    return c
size = lambda G: G["N"] + sum(len(o) for o in G["opts"])
if sys.argv[1] == "--census":
    print("instance N+M T maxm nm C idfail")
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G); c = census(G, 3000)
        print(os.path.basename(f), size(G), c["T"], c["maxm"], c["nm"], c["C"], c["idfail"], flush=True)
    sys.exit(0)
from sharp226 import mutate
from compose226 import add_opt, check
seed, CAP, IT, SG = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
def score(G): c = census(G); return (c["maxm"], c["C"], c["nm"], -size(G)), c
def grow(G):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"])
    if rng.random() < 0.6:
        x = rng.randrange(N); wt = -1 if G["lev"][x] == 0 else rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
        return add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
    lv = rng.choice([0, 1]); y = N; G["N"] += 1; G["lev"].append(lv); G["opts"].append([]); G["gate"].append([]); G["start"].append(0)
    wt = -1 if lv == 0 else rng.choice([z for z in range(N) if G["lev"][z] == 0])
    G = add_opt(G, y, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2)); M += 1
    x = rng.randrange(N); wx = -1 if G["lev"][x] == 0 else rng.choice([z for z in range(N) if G["lev"][z] == G["lev"][x] - 1])
    return add_opt(G, x, wx, y, rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
G = json.load(open(os.environ.get("RESUME", SG))); G = G.get("genome", G); s, c = score(G)
print("start", s, c, "N", G["N"], "M", len(G["br"]), flush=True)
for it in range(IT):
    Hh = grow(G) if (rng.random() < 0.3 and size(G) < CAP) else mutate(G, rng)
    if size(Hh) > CAP: continue
    try: check(Hh); s2, c2 = score(Hh)
    except Exception: continue
    if s2[:3] >= s[:3]:
        if s2[:2] > s[:2]:
            json.dump(Hh, open(f"{H}/out/mc_{CAP}_{seed}.json", "w"))
            if c2["maxm"] >= 3: json.dump(Hh, open(f"{H}/out/mkill_{seed}_{c2['maxm']}.json", "w"))
            print(it, "maxm", c2["maxm"], "nm", c2["nm"], "C", c2["C"], "idfail", c2["idfail"], "T", c2["T"], "N", Hh["N"], "M", len(Hh["br"]), flush=True)
        G, s = Hh, s2
print("FINAL cap", CAP, "score", s, "N", G["N"], "M", len(G["br"]), flush=True)
