#!/usr/bin/env python3
"""Box 38 (c): hill climb toward a NO-ENTRY-B violation (docs/new/N5-NEB-box38.md). State = (𝒞^1O game with o -> o, start σ0);
N5 runs from (σ0, τ0) with τ0(o) = o (SPEC S3: a start pair may be given). Score per run, over case-B in-phase HN fallbacks a with
τ(o) = o: (V, C, Rr, L) = (#NO-ENTRY violations, #states a+1 in the phase, HN, θ unchanged, with an honest gate F -> R̄ (INV (i)
fails), #low-route R-rises at a -> a+1, #case-B τ(o) = o fallbacks). Mutations: priority, edge add / remove, owner flip, σ0 entry. Env MODE = B (default) | TAU (τ(o) ≠ o) | TAUW (τ(o) ≠ o, c_w ≠ o).
Keeps exactly one Odd vertex with out-degree > 1 (asserted). With seed.state = "-" the start is canonical (SPEC S3) and σ0 is not mutated.
Usage: nebclimb.py seed.pg seed.state rseed minutes outdir"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from neb_run import *
import pg

MODE = os.environ.get("MODE", "B")   # B: case B, τ(o) = o (default); TAU: τ(o) ≠ o, any case; TAUW: τ(o) ≠ o with c_w ≠ o

def cw_of(g, r, o):
    nx = [r["s"][v] if g.owner[v] == 0 else r["t"][v] for v in range(g.n)]; C = [o]; x = nx[o]
    while x != o: C.append(x); x = nx[x]
    return C

def score(g, s0):
    rows, o, E = trace(g, s0, cap=400); N = len(rows); V = C = Rr = L = 0
    HN = [r["h1"] and not r["h2"] for r in rows]
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"]): continue
        if MODE == "B" and (r["t"][o] != o or E.rank[o] > E.rank[r["Xi"][o][0]]): continue
        if MODE in ("TAU", "TAUW") and r["t"][o] == o: continue
        if MODE == "TAUW" and max(cw_of(g, r, o), key=lambda v: E.rank[v]) == o: continue
        L += 1; cth = r["Xi"][o][0]; b = rows[a + 1]
        Rb0, Rb1 = set(r["R"]) | {o}, set(b["R"]) | {o}
        if any(b["Xi"][u] != r["Xi"][u] for u in Rb0 & Rb1 if u != o): Rr += 1
        if HN[a + 1] and b["th"] == r["th"]:
            if any(y not in Rb1 and z in Rb1 for y, z in E.improving(tuple(b["s"]), b["Xi"])): C += 1
        k = a
        while k + 1 < N and HN[k + 1] and rows[k + 1]["ph"] == r["ph"] and rows[k + 1]["th"] == r["th"]:
            if set(rows[k + 1]["R"]) > set(rows[k]["R"]): V += 1
            k += 1
    return (V, C, Rr, L)

def ok(g):
    oc = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    return len(oc) == 1 and all(g.succ[v] for v in range(g.n)) and (MODE != "B" or oc[0] in g.succ[oc[0]])

def mutate(rng, g, s0):
    pr, ow, sc, s = list(g.prio), list(g.owner), [list(x) for x in g.succ], list(s0); n = g.n
    o = [v for v in range(n) if ow[v] == 1 and len(set(sc[v])) > 1][0]; k = rng.random(); v = rng.randrange(n)
    if k < 0.3: pr[v] = rng.randrange(n + 3)
    elif k < 0.55:
        w = rng.randrange(n)
        if w not in sc[v] and (ow[v] == 0 or v == o): sc[v] = sorted(sc[v] + [w])
    elif k < 0.75:
        if len(sc[v]) > 1 and not (v == o and len(sc[v]) <= 2): sc[v].remove(rng.choice([w for w in sc[v] if not (v == o and w == o)]))
    elif k < 0.85:
        if v != o and len(sc[v]) == 1: ow[v] ^= 1
    else:
        if ow[v] == 0: s[v] = rng.choice(sc[v])
    for u in range(n):
        if ow[u] == 0 and s[u] not in sc[u]: s[u] = sc[u][0]
        if ow[u] == 1: s[u] = -1
    return pg.Game(pr, ow, sc), s

if __name__ == "__main__":
    f, fs, seed, mins, outdir = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
    os.makedirs(outdir, exist_ok=True); rng = random.Random(seed)
    g = load(f); CANON = fs == "-"; s0 = None if CANON else list(map(int, open(fs).read().split())); assert ok(g)
    best = score(g, s0); t0 = time.time(); it = 0; print("START", best, flush=True)
    while time.time() - t0 < 60 * mins:
        it += 1; g2, s2 = mutate(rng, g, s0 if s0 else [-1] * g.n)
        if CANON: s2 = None
        if not ok(g2): continue
        try: sc = score(g2, s2)
        except Exception: continue
        if sc >= best:
            if sc > best:
                print("IMPROVE", it, sc, flush=True)
                p = os.path.join(outdir, f"neb{'c' if CANON else ''}{MODE}_{seed}.pg")
                with open(p, "w") as h:
                    h.write(f"parity {g2.n - 1};\n")
                    for v in range(g2.n): h.write(f"{v} {g2.prio[v]} {g2.owner[v]} {','.join(map(str, g2.succ[v]))};\n")
                if s2: open(p + ".state", "w").write(" ".join(map(str, s2)) + "\n")
            best, g, s0 = sc, g2, s2
    print("FINAL", best, "after", it, flush=True)
