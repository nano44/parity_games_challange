#!/usr/bin/env python3
"""Box 48 DATA (N5-NCONF §11): QP(P) := #{Odd v with >= 2 edges in the used-edge game G^P} = |union of D_k over k in P| (asserted).
Per phase (>= 2 states): n, |Q|, QP, QPc := max over cycle nodes c of |union D_k inside lambda^-1(c)|, classes := classes meeting it, D0 := |D_x| at the phase's first state, ENT := vertices first entering D after x (QP = D0 + ENT),
N_ep (sigma-bar|Q changes + 1), NCONF, XDEG := sum over v of (distinct sigma-bar_k(v) incl. tau(v)) - 1, len.
Prints per-n-bin maxima and sums, and the worst phases. Usage: qp.py STARTS SEED (--list FILE | --rand C LO HI GSEED KFRAC | files)
[--nmax N] [--start F]; --rand makes rand_ckO games with k = max(2, round(KFRAC*n)) Odd choice vertices."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box45", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from multi import load, step, start_pair, Engine, dual, rand_ckO
from n5x import pg, readstart
BIN = {}; WORST = []
def run(g, start, nm, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), sb=tuple(sb)))
        if r is None: break
        s, t = r[0], r[1]
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        if j > i: phase(g, rows, i, j, Q, nm)
        i = j + 1
def phase(g, rows, i, j, Q, nm):
    tau = rows[i]["t"]
    D = [{q for q in Q if rows[k]["sb"][q] != tau[q]} for k in range(i, j + 1)]
    U = set().union(*D)
    used = {q: {tau[q]} | {rows[k]["sb"][q] for k in range(i, j + 1)} for q in Q}
    qp = sum(1 for q in Q if len(used[q]) >= 2)
    assert qp == len(U), (qp, len(U))
    d0 = len(D[0]); nep = 1 + sum(1 for k in range(i, j) if tuple(rows[k + 1]["sb"][q] for q in Q) != tuple(rows[k]["sb"][q] for q in Q))
    nconf = len({tuple(rows[k]["sb"][q] for q in Q) for k in range(i, j + 1)})
    xdeg = sum(len(used[q]) - 1 for q in Q)
    lam = rows[i]["lam"]; byc = {}
    for q in U: byc[lam[q]] = byc.get(lam[q], 0) + 1
    qpc = max(byc.values(), default=0); ncl = len(byc)
    b = BIN.setdefault((g.n // 10) * 10, dict(phases=0, maxQP=0, maxQ=0, sumQP=0, sumQ=0, maxENT=0, maxQPfrac=0.0, QPge3=0))
    b["phases"] += 1; b["maxQP"] = max(b["maxQP"], qp); b["maxQ"] = max(b["maxQ"], len(Q)); b["sumQP"] += qp; b["sumQ"] += len(Q)
    b["maxENT"] = max(b["maxENT"], qp - d0); b["QPge3"] += qp >= 3
    if Q: b["maxQPfrac"] = max(b["maxQPfrac"], round(qp / len(Q), 3))
    WORST.append((qp, g.n, len(Q), d0, qp - d0, nep, nconf, xdeg, j - i, qpc, ncl, nm))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); kf = float(a[5]); rng = random.Random(seed); gs = []
        for c in range(cnt):
            n = rng.randint(lo, hi); g = rand_ckO(rng, n, n, max(2, min(n - 1, round(kf * n))))
            if g is not None: gs.append((f"rand{c}_n{g.n}", g))
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: pass
    for n0 in sorted(BIN):
        b = BIN[n0]; print(f"n {n0}-{n0 + 9}: " + " ".join(f"{k} {v}" for k, v in b.items()))
    print("worst (QP n |Q| D0 ENT N_ep NCONF XDEG len QPc classes name):")
    for w in sorted(WORST, reverse=True)[:12]: print("  ", *w)
    print("longest phases (same columns):")
    for w in sorted(WORST, key=lambda w: (w[8], w[0]), reverse=True)[:15]: print("  ", *w)
    for L in (10, 30, 60):
        ws = [w for w in WORST if w[8] >= L]
        if ws: print(f"len >= {L}: phases {len(ws)} maxQP {max(w[0] for w in ws)} maxQPc {max(w[9] for w in ws)} maxENT {max(w[4] for w in ws)} max QP/|Q| {max(w[0] / max(1, w[2]) for w in ws):.3f}")
