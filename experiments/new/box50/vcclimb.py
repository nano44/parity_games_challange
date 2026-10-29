#!/usr/bin/env python3
"""L-NEW box 50 (successor 31): kill search for CONJECTURE VC-RUN (docs/new/N5-VC-box50.md). Score = 100 * max over fallback-free in-phase
runs of VC({sigma_t}) + SH, SH = the most distinct traces on a (VC+1)-set extending a shattered VC-set (shaping), minus CN * n (env CN,
default 0). SCOPE=exec: the whole execution's joint (sigma, tau) family instead. Mutations: L-SI's runlin/growclimb.py + box43 climb.py
(read-only). Usage: vcclimb.py SEED.pg SEED.start|- STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in (os.path.join(ROOT, "experiments", "si", "root"), os.path.join(ROOT, "experiments", "new", "box43"), os.path.join(ROOT, "experiments", "si", "runlin")):
    sys.path.insert(0, p)
from common import rows, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices
from growclimb import clone, save, mkst
from trace import runs
CN = float(os.environ.get("CN", "0")); SCOPE = os.environ.get("SCOPE", "run")

def vcsh(fam):
    F = list(set(fam)); allE = set().union(*F) if F else set(); ground = sorted(e for e in allE if any(e not in S for S in F))
    idx = {e: i for i, e in enumerate(ground)}; M = [sum(1 << idx[e] for e in S if e in idx) for S in F]
    level = [(i,) for i in range(len(ground))]; d = 1 if level else 0
    while level:
        cur = set(level); nxt = []
        for a in level:
            for j in range(a[-1] + 1, len(ground)):
                b = a + (j,)
                if all(b[:k] + b[k + 1:] in cur for k in range(len(b) - 1)):
                    mask = sum(1 << i for i in b)
                    if len({x & mask for x in M}) == 1 << len(b): nxt.append(b)
        if not nxt: break
        level = nxt; d += 1
    sh, cnt = 0, 0
    for a in level[:400]:
        for j in range(len(ground)):
            if j in a: continue
            mask = sum(1 << i for i in a) | (1 << j); k = len({x & mask for x in M})
            if k > sh: sh, cnt = k, 1
            elif k == sh: cnt += 1
    return d, sh + min(cnt, 9999) / 10000

def score(g, st):
    try: E, R = rows(g, st, cap=1500)
    except (RecursionError, RuntimeError): return None
    if len(R) > 1500: return None
    n = g.n; ev = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    sig = [frozenset((v, r["s"][v]) for v in ev) for r in R]
    if SCOPE == "ent":                      # CONJECTURE ENT-RUN: max entries of one Even edge into sigma within one run
        best = (0, 0)
        for a, b, i, j in runs(R):
            if b <= a: continue
            cnt = {}
            for k in range(a + 1, b + 1):
                for e in sig[k] - sig[k - 1]: cnt[e] = cnt.get(e, 0) + 1
            for e in sig[a]: cnt[e] = cnt.get(e, 0) + 1
            mx = max(cnt.values(), default=0); best = max(best, (mx, sum(v == mx for v in cnt.values()) / 100))
        return best
    if SCOPE == "exec":
        od = [u for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) >= 2]
        d, sh = vcsh([sig[k] | frozenset((u, R[k]["t"][u]) for u in od) for k in range(len(R))]); return d, sh
    best = (0, 0)
    for a, b, i, j in runs(R):
        if b > a: best = max(best, vcsh(sig[a:b + 1]))
    return best

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g)); st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    d, sh = score(g, mkst(g, st)); cur = 100 * d + sh - CN * g.n; bestd = d; print("seed VC", d, "SH %.2f" % sh, "n", g.n, flush=True)
    for it in range(steps):
        res = clone(rng, g, O, nmax, st) if rng.random() < 0.25 else climb.mutate(rng, g, O, nmax, st)
        if res is None: continue
        g2, O2, st2 = res; r = score(g2, mkst(g2, st2))
        if r is None: continue
        c2 = 100 * r[0] + r[1] - CN * g2.n
        if c2 < cur: continue
        if c2 > cur: save(out + "_best", g2, st2); print("step", it, "VC", r[0], "SH %.2f" % r[1], "n", g2.n, flush=True)
        if r[0] > bestd: bestd = r[0]; save(out + "_vc%d" % r[0], g2, st2)
        g, O, st, cur = g2, O2, st2, c2
    save(out + "_last", g, st); print("final best VC", bestd)

if __name__ == "__main__":
    main()
