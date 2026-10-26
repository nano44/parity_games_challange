#!/usr/bin/env python3
"""L-RED successor 21: exact checker for Lemma N3-LEVEL and Lemma FLIP (a) of docs/si/P-N5-FLIP-box18.md (sha1 96a7e088), written from
the frozen §1/§6 text, not from L-SI's flipck.py (whose N3LEV_V tests only flips with BOTH paths intact at BOTH times).
Definitions (packet §1, §6): phase = maximal run with (lambda_Xi, tau) constant; Q = Odd vertices with >= 2 distinct successors;
U_c = lambda^{-1}(c); Q_c = (Q cap U_c) - {c}. For q in Q_c: the class exit path p_s(q) = sigma-bar_s(q)'s honest play strictly before
its first vertex in Q_c u {c} (the exit); par_s(q) = the exit when it is in Q_c - {q}. FLIP = (q1, q2, t1 < t2) in one phase,
par_t1(q1) = q2, par_t2(q2) = q1; C = q1 . p1 . q2 . p2; X_s = P(Xi_s q2); lev = top rank of X_t1 xor X_t2 (-1 if equal).
N3-LEVEL (checked at EVERY flip, every t1): hypotheses p1 cap p2 = {}, h = top-ranked vertex of C has rank(h) > rank(c) and h even,
and (h in p2 => p2 intact at t1: every vertex of p2 has the same successor at t1 as at t2). Conclusion lev >= rank(h).
FLIP-COST (a): key_t2(q2) >= key_t1(q2) + wt(C) (weights of ranks > rank(c), with multiplicity; length s_c*|C|).
SG: Xi_{k+1}(v) >= Xi_k(v) at every v, every in-phase transition (the packet's premise; counted, not assumed).
Counters: flips, hyp (hypotheses hold), by position of h, eq (lev = rank(h)), top gap = (class top rank) - rank(h) at hyp flips.
Usage: n3x.py --one GAME [START] [-v] | --list FILE [NMAX] (env RS random starts per game, seeded by file name). MUT=1: demand lev > rank(h)."""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); VIOL = []; HYP = []; VERB = "-v" in sys.argv; MUT = os.environ.get("MUT") == "1"; EXT = {}

def trace(g, start, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(lam=tuple(x[0] for x in vs), tau=tuple(t), vs=vs, nxt=nxt, fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    return E, rows

def exitpath(nxt, q, Qc, c):
    y = nxt[q]; path, x, seen = [], y, set()
    while x not in Qc and x != c:
        if x in seen: return None          # cannot happen on an honest play (it reaches c); counted
        seen.add(x); path.append(x); x = nxt[x]
    return x, tuple(path)

def check(g, name, start=None):
    E, rows = trace(g, start)
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["tau"]) == (rows[i]["lam"], rows[i]["tau"]): j += 1
        C["phases"] += 1
        for k in range(i, j):
            for v in range(g.n):
                C["sg_checks"] += 1
                if E.key(rows[k + 1]["vs"][v]) < E.key(rows[k]["vs"][v]): C["SG_V"] += 1; VIOL.append(("SG", name, k, v))
        if j > i: phase(g, E, name, rows, i, j, Q)
        i = j + 1

def phase(g, E, name, rows, i, j, Q):
    lam = rows[i]["lam"]; par = {}
    classes = {}
    for q in Q:
        if lam[q] != q: classes.setdefault(lam[q], set()).add(q)
    for c, Qc in classes.items():
        for k in range(i, j + 1):
            for q in Qc:
                r = exitpath(rows[k]["nxt"], q, Qc, c)
                if r is None: C["EXIT_LOOP"] += 1; VIOL.append(("LOOP", name, k, q)); continue
                e, p = r
                if e != c and e != q: par[(k, q)] = (e, p)
    for (t2, q2), (q1, p2) in par.items():
        c = lam[q2]; s_c = 1 if E.par[c] == 1 else -1
        top_class = max(E.rank[v] for v in range(g.n) if lam[v] == c)
        for t1 in range(i, t2):
            pp = par.get((t1, q1))
            if not pp or pp[0] != q2: continue
            p1 = pp[1]; C["flips"] += 1
            walk = [q1, *p1, q2, *p2]
            wt = sum(((1 << E.rank[v]) if E.par[v] == 0 else -(1 << E.rank[v])) for v in walk if E.rank[v] > E.rank[c])
            k1 = E.key(rows[t1]["vs"][q2]); k2 = E.key(rows[t2]["vs"][q2])
            C["flipcost_checks"] += 1
            if (k2[1], k2[2]) < (k1[1] + wt, k1[2] + s_c * len(walk)) or k2[0] != k1[0]:
                C["FLIPCOST_V"] += 1; VIOL.append(("FLIPCOST", name, i, q1, q2, t1, t2))
            if set(p1) & set(p2): C["n2_overlap"] += 1; continue
            h = max(walk, key=lambda v: E.rank[v])
            if not (E.rank[h] > E.rank[c] and E.par[h] == 0): C["hyp_fail_top"] += 1; continue
            pos = "q2" if h == q2 else "q1" if h == q1 else "p1" if h in p1 else "p2"
            A, B = rows[t1]["nxt"], rows[t2]["nxt"]
            if pos == "p2" and not all(A[v] == B[v] for v in p2): C["hyp_fail_p2intact"] += 1; continue
            p1i = all(A[v] == B[v] for v in p1); p2i = all(A[v] == B[v] for v in p2)
            C["hyp"] += 1; C["hyp_" + pos] += 1; C["hyp_bothintact"] += p1i and p2i; C["hyp_p1broken"] += not p1i
            X1, X2 = rows[t1]["vs"][q2][1], rows[t2]["vs"][q2][1]
            lev = (X1 ^ X2).bit_length() - 1
            gap = top_class - E.rank[h]; C["gap_max"] = max(C["gap_max"], gap)
            key = (name, i, q1, q2)
            EXT[key] = EXT.get(key, 0) + 1
            HYP.append((lev - E.rank[h], pos, p1i, p2i))
            if lev == E.rank[h]: C["eq"] += 1
            if lev < E.rank[h] + (1 if MUT else 0):
                C["N3LEV_V_" + pos] += 1; VIOL.append(("N3LEV", name, i, q1, q2, t1, t2, h, pos, lev, E.rank[h]))
            if VERB: print(f"  FLIP {name} ph@{i} q1={q1} q2={q2} t1={t1-i} t2={t2-i} h={h}({pos}) rank={E.rank[h]} lev={lev} "
                           f"classtop={top_class} p1int={p1i} p2int={p2i}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); st = readstart(a[2]) if len(a) > 2 else None
        if st is None and os.path.exists(a[1][:-3] + ".start"): st = readstart(a[1][:-3] + ".start")
        check(g, a[1], st)
    else:
        nmax = int(a[2]) if len(a) > 2 else 64
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            path = f if os.path.isabs(f) else os.path.join(ROOT, f)
            g = load(path)
            if g.n > nmax: continue
            C["games"] += 1; check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    if EXT: print("max hyp flips per (phase, pair):", max(EXT.values()), max(EXT, key=EXT.get))
    for v in VIOL[:10]: print("VIOLATION", v)
    print("N3X PASS" if not VIOL else "N3X FAIL")

if __name__ == "__main__":
    main()
