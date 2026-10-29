#!/usr/bin/env python3
"""L-NEW box 50 (successor 31): VC dimension (Vapnik-Chervonenkis / Sauer-Shelah) of the family of Even strategies visited by N5.
For a stretch R[s..e] of the N5 run (rows() of experiments/si/root/common.py, read-only), F := {sigma_t : t in [s, e]}, each sigma_t read as
the set of its edges (v, sigma_t(v)) over Even v. Ground set = the edges in some but not all members. A set A of edges is SHATTERED if
{sigma ∩ A : sigma in F} has 2^|A| members; VC(F) = the largest shattered |A| (Apriori: shattering is hereditary).
Sauer-Shelah: |F| <= sum_{i <= VC} C(m, i), m = |ground set|. Per run we also record |F| (= e - s + 1 iff no strategy repeats), the max
number of maximal intervals in which one edge is present (ENT), and the same VC for sigma-bar (Odd edges; not reader-proof).
Scopes: run (maximal fallback-free stretch of a phase), phase, whole execution. MUT=1 counts a set as shattered at 2^|A| - 1 traces (must
raise VC somewhere). Usage: vcrun.py --list FILE | --one GAME [START]"""
import sys, os
from itertools import combinations
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("root", "runlin"): sys.path.insert(0, os.path.join(ROOT, "experiments", "si", p))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43"))
from common import rows, load, readstart, phases
from trace import runs
MUT = os.environ.get("MUT") == "1"; C = Counter(); TOP = []

def vc(fam, cap=12):
    """fam: list of frozensets of edges. Returns (VC, m, |distinct|, witness)."""
    F = list(set(fam)); allE = set().union(*F) if F else set(); ground = sorted(e for e in allE if any(e not in S for S in F))
    idx = {e: i for i, e in enumerate(ground)}; M = [sum(1 << idx[e] for e in S if e in idx) for S in F]
    need = lambda k: (1 << k) - (1 if MUT and k >= 2 else 0)
    level = [(i,) for i in range(len(ground))]; d = 1 if level else 0; wit = level[0] if level else ()
    while level and d < cap:
        cur = set(level); nxt = []
        for a in level:
            for j in range(a[-1] + 1, len(ground)):
                b = a + (j,)
                if all(b[:k] + b[k + 1:] in cur for k in range(len(b) - 1)):
                    mask = sum(1 << i for i in b)
                    if len({x & mask for x in M}) >= need(len(b)): nxt.append(b)
        if not nxt: break
        level = nxt; d += 1; wit = nxt[0]
    return d, len(ground), len(F), tuple(ground[i] for i in wit)

def ent(seq):
    """max over edges of the number of maximal intervals of presence."""
    best = 0; prev = set()
    cnt = Counter()
    for S in seq:
        for e in S - prev: cnt[e] += 1
        prev = S
    return max(cnt.values(), default=0)

def sauer(d, m): return sum(comb(m, i) for i in range(d + 1))

def one(g, name, start=None):
    E, R = rows(g, start); n = g.n
    ev = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    od = [u for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) >= 2]
    sig = [frozenset((v, r["s"][v]) for v in ev) for r in R]; sb = [frozenset((u, r["sb"][u]) for u in od) for r in R]
    for scope, spans in (("run", [(s, e) for s, e, i, j in runs(R)]), ("phase", list(phases(R))), ("exec", [(0, len(R) - 1)])):
        for s, e in spans:
            if e <= s: continue
            fam = sig[s:e + 1]; d, m, nf, w = vc(fam); C[scope + "s"] += 1
            if nf < e - s + 1: C[scope + "_REPEAT"] += 1
            if nf > sauer(d, m): C[scope + "_SAUER_V"] += 1
            C[scope + "_VC_max"] = max(C[scope + "_VC_max"], d); C[scope + "_len_max"] = max(C[scope + "_len_max"], e - s)
            C[scope + "_ENT_max"] = max(C[scope + "_ENT_max"], ent(fam))
            db = vc(sb[s:e + 1])[0]; C[scope + "_VCbar_max"] = max(C[scope + "_VCbar_max"], db)
            TOP.append((scope, d, db, e - s, m, n, name, s, e, w))
    tau = [frozenset((u, r["t"][u]) for u in od) for r in R]; J = [sig[k] | tau[k] for k in range(len(R))]
    dj, mj, nj, wj = vc(J); C["joint_VC_max"] = max(C["joint_VC_max"], dj)
    if nj < len(R): C["joint_REPEAT"] += 1
    if nj > sauer(dj, mj): C["joint_SAUER_V"] += 1
    TOP.append(("joint", dj, 0, len(R) - 1, mj, n, name, 0, len(R) - 1, wj))
    ds, ms, ns, _ = vc(sig); dt, mt, nt, _ = vc(tau); it = len(R) - 1     # Theorem VC-BOUND: it <= Phi(ds, ms) + Phi(dt, mt) - 2
    chs = sum(sig[k] != sig[k + 1] for k in range(it)); cht = sum(tau[k] != tau[k + 1] for k in range(it))
    if ns != chs + 1: C["SIG_REPEAT"] += 1
    if nt != cht + 1: C["TAU_REPEAT"] += 1
    if it > sauer(ds, ms) + sauer(dt, mt) - 2: C["VCB_V"] += 1
    C["dsig_max"] = max(C["dsig_max"], ds); C["dtau_max"] = max(C["dtau_max"], dt)
    TOP.append(("bound", ds, dt, it, ms, mt, name, sauer(ds, ms) + sauer(dt, mt) - 2, ns, ()))
    TOP.append(("tau", dt, ds, it, mt, n, name, 0, it, ()))

def main():
    a = sys.argv[1:]
    if a[0] == "--rand":                  # --rand K SEED: K seeded random games (n 8..40, out-degree 1..4, priorities 0..n), default start
        import random, pg
        rng = random.Random(int(a[2]))
        for k in range(int(a[1])):
            n = rng.randint(8, 40); pr = [rng.randint(0, n) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
            su = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) for _ in range(n)]
            try: one(pg.Game(pr, ow, su), "rand%s_%d" % (a[2], k))
            except Exception as ex: C["ERR"] += 1; print("ERR", k, repr(ex)[:80])
    elif a[0] == "--one": one(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                X = lambda q: os.path.join(ROOT, "experiments", q)
                try: one(load(X(p[0])), p[0], readstart(X(p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
                except Exception as ex: C["ERR"] += 1; print("ERR", p[0], repr(ex)[:80])
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for sc in ("run", "phase", "exec", "joint", "bound", "tau"):
        fmt = {"bound": "TOP %s dsig %d dtau %d iters %d msig %d mtau %d %s sauer %d |Fsig| %d %s", "tau": "TOP %s dtau %d dsig %d iters %d mtau %d n %d %s [%d,%d] %s"}.get(sc, "TOP %s VC %d VCbar %d len %d m %d n %d %s [%d,%d] wit %s")
        for x in sorted([x for x in TOP if x[0] == sc], key=lambda x: (-x[1], -x[3]))[:5]: print(fmt % x)
    print("VC PASS" if not any(k.endswith("SAUER_V") or k in ("run_REPEAT", "phase_REPEAT", "SIG_REPEAT", "TAU_REPEAT", "VCB_V") for k in C) else "VC FAIL")

if __name__ == "__main__":
    main()
