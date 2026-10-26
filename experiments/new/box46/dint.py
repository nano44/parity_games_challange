#!/usr/bin/env python3
"""Box 46 DATA: D-intervals of N5 phases (docs/new/N5-REC1-box46.md). In a phase (lambda_Xi, tau constant), D_k := {q in Q : sigma-bar_k(q)
!= tau(q)}; a D-INTERVAL is a maximal run of consecutive states of the phase with D_k constant (as a set). For |D| = 1 intervals {u}:
the entry type (from D = empty: ENT0; from another {u'}: ENTDIR; from |D| >= 2: ENTBIG; phase start: ENTSTART), the epochs inside
one {u}-interval (EPI1MAX) and its length (LENI1MAX). Also N0 (D = empty epochs per phase) against REC-0' (N0 <= f + 4n^2 - 3n,
R0P_V) and REC-0 ((f+1)(n+1) + 4n(n-1) + 1). REC1R_V: per phase and |D| = 1 configuration C, #C-epochs <= sum over {u}-intervals of
their epochs (trivial) and #{u}-intervals <= N0 + 1 + ENTDIR(u) + ENTBIG(u) (the reduction; must be 0).
Usage: dint.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), q=tuple(sb[q] for q in Q), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, rows, i, j, Q); i = j + 1
def phase(g, rows, a, b, Q):
    inc("phases"); n = g.n; tau = rows[a]["t"]
    f = sum(rows[k]["fb"] for k in range(a, b))
    Dk = [frozenset(q for q, w in zip(Q, rows[k]["q"]) if w != tau[q]) for k in range(a, b + 1)]
    eps = []; k = a
    while k <= b:
        e = k
        while e + 1 <= b and rows[e + 1]["q"] == rows[k]["q"]: e += 1
        eps.append((k, e)); k = e + 1
    N0 = sum(1 for (x, y) in eps if not Dk[x - a])
    if N0 > f + 4 * n * n - 3 * n: inc("R0P_V")
    if N0 > (f + 1) * (n + 1) + 4 * n * (n - 1) + 1: inc("R0_V")
    mx("N0MAX", N0)
    ivs = []; k = 0
    while k <= b - a:
        e = k
        while e + 1 <= b - a and Dk[e + 1] == Dk[k]: e += 1
        ivs.append((k, e)); k = e + 1
    ent = {}; nint = {}
    for idx, (x, y) in enumerate(ivs):
        D = Dk[x]
        if len(D) != 1: continue
        (u,) = D; nint[u] = nint.get(u, 0) + 1
        if idx == 0: typ = "ENTSTART"
        else:
            P = Dk[ivs[idx - 1][0]]
            typ = "ENT0" if not P else ("ENTDIR" if len(P) == 1 else "ENTBIG")
        inc(typ); ent.setdefault(u, {}); ent[u][typ] = ent[u].get(typ, 0) + 1
        ne = sum(1 for (p, q) in eps if x <= p - a <= y); mx("EPI1MAX", ne); mx("LENI1MAX", y - x + 1)
        inc("I1")
    for u, m in nint.items():
        e = ent[u]
        if m > N0 + 1 + e.get("ENTDIR", 0) + e.get("ENTBIG", 0): inc("REC1R_V")
        mx("I1PERU_MAX", m)
    if all(len(Dk[x - a]) <= 1 for (x, y) in eps):
        inc("ALL1"); mx("ALL1_NEP", len(eps)); mx("ALL1_I1", sum(nint.values())); mx("ALL1_DIR", sum(e.get("ENTDIR", 0) for e in ent.values()))
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())))
