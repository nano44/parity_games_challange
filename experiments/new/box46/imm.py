#!/usr/bin/env python3
"""Box 46 DATA (CONJECTURE IMM, docs/new/N5-REC1-box46.md): for every W-honest state h of a phase whose transition h -> h+1 is an in-phase
S4a step (not a fallback), does the Xi-level rise at once: LEV(h+1) >= min(LEV(h) + 1, n - 1)? IMM_V counts failures (split: h+1 honest
or not; and whether some W-cycle node at h+1 differs from lambda (_split) or not (_UNSPLIT)). IMMP_V (CONJECTURE IMM'): failures where h+1 is NOT the last state of its phase. Also WIMM_V: the same for the W-level at h+1 (HON step 1 says W rises when no W-cycle node changes at h+1: WIMM_V_UNSPLIT must be 0; WIMM_V_split is allowed).
Usage: imm.py STARTS SEED (--list FILE | --rand C LO HI GSEED) [--nmax N] [--budget B]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L, hon
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
FIRST = []; MID = []
def check(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), xi=vs, w=w, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    for h in range(len(rows) - 1):
        a, b = rows[h], rows[h + 1]
        if not a["hon"] or a["fb"] or (a["lam"], a["t"]) != (b["lam"], b["t"]): continue
        frame = [[a["t"][v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
        try:
            l0 = L.level(E, g, frame, a["xi"], (), budget); l1 = L.level(E, g, frame, b["xi"], (), budget); w1 = L.level(E, g, frame, b["w"], (), budget)
        except Unknown: inc("UNK"); continue
        inc("steps"); need = min(l0 + 1, g.n - 1)
        split = any(b["w"][v][0] != a["lam"][v] for v in range(g.n))
        if split: inc("split_steps")
        if w1 < need: inc("WIMM_V_" + ("split" if split else "UNSPLIT"))
        if l1 < need:
            inc("IMM_V_" + ("hon" if b["hon"] else "nothon") + ("_split" if split else "_UNSPLIT"))
            last = h + 2 >= len(rows) or (rows[h + 2]["lam"], rows[h + 2]["t"]) != (b["lam"], b["t"])
            if not last:
                inc("IMMP_V")
                if not MID: MID.append((nm, start is not None, h, l0, l1))
            if not FIRST: FIRST.append((nm, start is not None, h, l0, l1))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 24, 1000000
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else:
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    for nm, g in gs:
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st, budget, nm)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())), "FIRST", FIRST, "MID", MID)
