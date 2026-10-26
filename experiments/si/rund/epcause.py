#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §28 (item (c)). Per phase, every EPOCH BOUNDARY (in-phase transition t -> t+1 with
sigma-bar|Q changing; RESULTS R61's epochs) and every q in Q whose sigma-bar(q) changes there, classified by R61 (e) ALT / (f)'s causes:
  CYC     lambda(q) = q (q is its own cycle node);
  NC      non-clean: q on an honest cycle at t or t + 1, or y2 := sigma-bar_t+1(q)'s honest play at t passes q;
  STRICT  clean, kappa_t+1(q) != kappa_t(q) (ALT: strict rise);
  TIE     clean, kappa unchanged (ALT: a tie at t).
Per boundary: whether it is a rho-transition (some Xi(q), q in Q, changes), and the kinds of its rho events (ROUTE / RELAY / CYC as in
chosen.py). Also: boundaries whose only changes are TIE / NC / CYC (residual boundaries, R61 (f)'s non-rho terms); and, per q, the
STRICT changes split by whether q's event at the boundary is ROUTE or RELAY. ALT_V counts clean changes with kappa going DOWN (ALT says
none; MUT=1 flips the comparison as a control).
Usage: epcause.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from relay import exits
from pot import oncycle
C = Counter(); VIOL = []; VERB = "-v" in sys.argv; MUT = os.environ.get("MUT") == "1"; TOP = []

def passes(nxt, y, q):
    x, seen = y, set()
    while x not in seen:
        if x == q: return True
        seen.add(x); x = nxt[x]
    return False

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt, fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, E, name, rows, i, j, Q)
        i = j + 1

def phase(g, E, name, rows, i, j, Q):
    Qs = set(Q); nb = 0; resid = 0
    for k in range(i, j):
        A, B = rows[k], rows[k + 1]
        ch = [q for q in Q if A["sb"][q] != B["sb"][q]]
        if not ch: continue
        nb += 1; C["boundaries"] += 1
        ev = [q for q in Q if tuple(A["vs"][q]) != tuple(B["vs"][q])]
        if ev: C["boundaries_rho"] += 1
        if A["fb"]: C["boundaries_fb"] += 1
        kinds = []
        for q in ch:
            c = rows[i]["vs"][q][0]
            if c == q: kd = "CYC"
            elif oncycle(A["nxt"], q) or oncycle(B["nxt"], q) or passes(A["nxt"], B["sb"][q], q): kd = "NC"
            else:
                k1, k2 = E.key(A["vs"][q]), E.key(B["vs"][q])
                if MUT: k1, k2 = k2, k1
                if k2 < k1: C["ALT_V"] += 1; VIOL.append(("ALT", name, i, k - i, q))
                kd = "TIE" if k2 == k1 else "STRICT"
                if kd == "STRICT":
                    rk = "ROUTE" if exits(A["nxt"], q, c, Qs, g.succ) != exits(B["nxt"], q, c, Qs, g.succ) else "RELAY"
                    C["strict_" + rk] += 1
            kinds.append(kd); C["chg_" + kd] += 1
        if set(kinds) <= {"TIE", "NC", "CYC"}:
            resid += 1; C["boundaries_residual"] += 1
            if not ev: C["boundaries_residual_norho"] += 1
        if VERB: print(f"  B {name} phase@{i} t={k - i} fb={A['fb']} chg={list(zip(ch, kinds))} rho={ev}")
    if nb:
        C["phases_with_boundaries"] += 1; C["max_boundaries_phase"] = max(C["max_boundaries_phase"], nb)
        TOP.append((nb, resid, j - i, g.n, name, i))

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
    for m in sorted(TOP, reverse=True)[:5]: print("TOP boundaries/residual/len/n", m)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("EPCAUSE PASS" if not VIOL else "EPCAUSE FAIL")

if __name__ == "__main__":
    main()
