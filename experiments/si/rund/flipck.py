#!/usr/bin/env python3
"""L-SI box 18 (successor 14): DATA for note §24 (relay flips). In a phase, par_t(q) := the exit (first vertex of Q u {c}) of
sigma-bar_t(q)'s honest play, when it is a terminal q' != q, c, with exit path p_t(q). A FLIP is (q1, q2, t1 < t2) in one phase with
par_t1(q1) = q2 and par_t2(q2) = q1. Checks (Lemma FLIP, note §24; both PROVED there):
  FLIPCOST_V  key_t2(q2) >= key_t1(q2) + wt(C) fails, C := the closed walk q1 . p_t1(q1) . q2 . p_t2(q2) (weights with multiplicity,
              ranks above c only; length |C|), compared as (weight, s_c * length) lexicographically.
  FLIP1_V     p_t1(q1) still INTACT at t2 (sigma-bar_t1(q1) still a successor, every vertex of the path has the same successor at t2) and
              the cycle reached from q1 at t2 with sigma-bar(q1) := sigma-bar_t1(q1) has a node w with rew[w] <= rew[c] (Odd-attractive).
Reports flips, intact / broken (latest t1), and the rise of q2 at broken flips. MUT=1: the reversed inequality key_t1 >= key_t2 + wt(C) (control; must fail).
ONSETS: flips whose t2 is the first state of a run with par(q2) = q1.
Usage: flipck.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); VIOL = []; VERB = "-v" in sys.argv; MUT = os.environ.get("MUT") == "1"

def par(nxt, q, c, Qs):
    y = nxt[q]; path, x, seen = [], y, set()
    while x not in seen and x not in Qs and x != c and x != q: seen.add(x); path.append(x); x = nxt[x]
    if x in Qs and x != q and x != c: return x, y, tuple(path)
    return None

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, nxt=nxt))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, E, name, rows, i, j, Q, Qs)
        i = j + 1

def wtv(E, v, c):
    if E.rank[v] <= E.rank[c]: return 0
    return (1 << E.rank[v]) if E.rankpar[E.rank[v]] == 0 else -(1 << E.rank[v])

def phase(g, E, name, rows, i, j, Q, Qs):
    P = {}
    for k in range(i, j + 1):
        for q in Q:
            c = rows[i]["vs"][q][0]
            if c == q: continue
            p = par(rows[k]["nxt"], q, c, Qs)
            if p: P[(k, q)] = p
    for (t2, q2), (q1, y2, p2) in P.items():
        t1s = [k for k in range(i, t2) if P.get((k, q1), (None,))[0] == q2]
        if not t1s: continue
        c = rows[i]["vs"][q2][0]; s_c = 1 if E.par[c] == 1 else -1
        C["flips"] += 1; onset = P.get((t2 - 1, q2), (None,))[0] != q1 if t2 > i else True
        C["onsets"] += onset
        for t1 in t1s:
            _, y1, p1 = P[(t1, q1)]
            walk = [q1, *p1, q2, *p2]
            wt = sum(wtv(E, v, c) for v in walk); ln = len(walk)
            k1 = E.key(rows[t1]["vs"][q2]); k2 = E.key(rows[t2]["vs"][q2])
            need = (k1[1] + wt, k1[2] + s_c * ln)
            have = (k2[1], k2[2])
            if MUT: have, need = (k1[1], k1[2]), (k2[1] + wt, k2[2] + s_c * ln)   # control: the reversed inequality must fail
            C["flipcost_checks"] += 1
            if have < need: C["FLIPCOST_V"] += 1; VIOL.append(("FLIPCOST", name, i, q1, q2, t1, t2))
        t1 = t1s[-1]; _, y1, p1 = P[(t1, q1)]; A, B = rows[t1]["nxt"], rows[t2]["nxt"]
        intact = y1 in g.succ[q1] and all(A[v] == B[v] for v in p1)
        if intact:
            C["intact"] += 1; C["intact_onsets"] += onset; nx = list(B); nx[q1] = y1; x, seen, order = q1, {}, []
            while x not in seen: seen[x] = len(order); order.append(x); x = nx[x]
            cyc = order[seen[x]:]; w = max(cyc, key=lambda v: E.rank[v])
            if E.rew[w] <= E.rew[c]: C["FLIP1_V"] += 1; VIOL.append(("FLIP1", name, i, q1, q2, t1, t2, w, c))
            k1 = E.key(rows[t1]["vs"][q2]); k2 = E.key(rows[t2]["vs"][q2])
            C["intact_with_rise"] += k2 > k1
        else:
            C["broken"] += 1; C["broken_onsets"] += onset
        if VERB: print(f"  FLIP {name} phase@{i} q1={q1} q2={q2} t1={t1 - i} t2={t2 - i} {'INTACT' if intact else 'broken'}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("FLIP PASS" if not VIOL else "FLIP FAIL")

if __name__ == "__main__":
    main()
