#!/usr/bin/env python3
"""L-COMP box 38 item 2(b): U-LADDERS = genome families in which ONLY U(G) changes, at FIXED N + M (N, levels, options, gates, br, bp,
start and every W-target unchanged; only Xi-targets xt move). U(G) as u38.py (P-N5-ASC §6 l. 179 / R121 (g)).
  down: from the base, one upward option per rung gets xt := -1 (K0), U drops by 1 per rung, to U = 0.
  up:   from the base, one non-upward option per rung gets xt := a mover of level > its owner's, U rises by 1, until none is left.
  pick: greedy = the candidate with the largest T3 (ties: first in option order) = a lower bound on max T3 at that (U, N + M) inside
        the family; rand<s> = a uniformly random candidate (seed s).
Score/counter: T3 from fast36 (box36 bin/k build; [E-LEV], or FAST36_NOELEV with --noelev) = N5'-xi iterations from S3 on Gamma3
before the first fallback (TOTAL up to the first fallback). Each rung's genome is saved (OUTDIR/<tag>_U<u>.json) for the full-run engines.
Usage: ladder38.py BASE.json down|up greedy|rand<s> OUTDIR TAG [--noelev]"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import fast36, u38
a = [x for x in sys.argv[1:] if not x.startswith("--")]; NOE = "--noelev" in sys.argv
BASE, DIR, PICK, OUTD, TAG = a[0], a[1], a[2], a[3], a[4]; os.makedirs(OUTD, exist_ok=True)
G = json.load(open(BASE)); lev = G["lev"]; N = G["N"]
T3 = lambda G: fast36.one(G, noelev=NOE, bindir="bin/k")[0]
rng = random.Random(PICK)


def cands(G):
    out = []
    for x in range(N):
        for k, o in enumerate(G["opts"][x]):
            up = o[1] >= 0 and lev[o[1]] > lev[x]
            if DIR == "down" and up: out.append((x, k, -1))
            if DIR == "up" and not up:
                out += [(x, k, y) for y in range(N) if lev[y] > lev[x]]
    return out


def apply(G, c):
    H2 = json.loads(json.dumps(G)); H2["opts"][c[0]][c[1]][1] = c[2]; return H2


def emit(G, t):
    u = u38.U(G); fn = os.path.join(OUTD, f"{TAG}_U{u}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
    print(json.dumps(dict(tag=TAG, U=u, NM=u38.NM(G), T3=t, elev=not NOE, file=os.path.basename(fn))), flush=True)


t = T3(G); emit(G, t)
while True:
    C = cands(G)
    if not C: break
    if PICK == "greedy":
        best = None
        for c in C:
            H2 = apply(G, c); tc = T3(H2)
            if best is None or tc > best[0]: best = (tc, H2)
        t, G = best
    else:
        G = apply(G, rng.choice(C)); t = T3(G)
    emit(G, t)
