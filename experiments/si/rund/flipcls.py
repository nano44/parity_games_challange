#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §26. Classifies every relay flip (q1, q2, t1 < t2) of flipck.py (note §24.2; latest t1
before t2) by the necessary condition of Lemma FLIP:
  N1fb   p1 := p_t1(q1) BROKEN at t2 and some transition in [t1, t2) that changes a vertex of p1 is a FALLBACK (S4c);
  N1sw   p1 BROKEN, every transition in [t1, t2) that changes p1 is an ordinary S4a step;
  N2     p1 intact at t2 and p1 meets p2 := p_t2(q2);
  N3     p1 intact at t2, p1, p2 disjoint (N3b: p2 also intact at t1, the hypothesis of N3-LEVEL).
Counted per flip STATE and per ONSET (t2 the first state of a run with par(q2) = q1). For N3: GAP = (top rank of the class U_c at t1) -
rank(top(C)) (L-RED 21's measure; small GAP = top of C near the class top). For N1: BRK = the number of transitions in [t1, t2) that
change p1, and BRKV = the Even vertices of p1 that switch. Per phase: flips, onsets, phase length, rho events (Xi changes on Q).
CLS_V counts flips that fit none of N1fb / N1sw / N2 / N3 (none possible: the four cases partition; a check on the code).
Usage: flipcls.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from flipck import par
C = Counter(); VIOL = []; VERB = "-v" in sys.argv; GAPS = Counter(); MAXP = []

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, nxt=nxt, fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, E, name, rows, i, j, Q, Qs)
        i = j + 1

def phase(g, E, name, rows, i, j, Q, Qs):
    P = {}
    for k in range(i, j + 1):
        for q in Q:
            c = rows[i]["vs"][q][0]
            if c == q: continue
            p = par(rows[k]["nxt"], q, c, Qs)
            if p: P[(k, q)] = p
    nf = no = 0
    rho = sum(1 for k in range(i, j) for q in Q if tuple(rows[k]["vs"][q]) != tuple(rows[k + 1]["vs"][q]))
    for (t2, q2), (q1, y2, p2) in sorted(P.items()):
        t1s = [k for k in range(i, t2) if P.get((k, q1), (None,))[0] == q2]
        if not t1s: continue
        t1 = t1s[-1]; _, y1, p1 = P[(t1, q1)]; c = rows[i]["vs"][q2][0]
        onset = P.get((t2 - 1, q2), (None,))[0] != q1 if t2 > i else True
        A, B = rows[t1]["nxt"], rows[t2]["nxt"]
        intact = all(A[v] == B[v] for v in p1)
        if not intact:
            brk = [k for k in range(t1, t2) if any(rows[k]["nxt"][v] != rows[k + 1]["nxt"][v] for v in p1)]
            brkv = sorted({v for k in brk for v in p1 if rows[k]["nxt"][v] != rows[k + 1]["nxt"][v]})
            cls = "N1fb" if any(rows[k]["fb"] for k in brk) else "N1sw"
            C["brk_transitions_" + cls] += len(brk); C["max_brk"] = max(C["max_brk"], len(brk))
            if any(g.owner[v] != 0 for v in brkv): C["BRK_ODD_V"] += 1; VIOL.append(("BRK_ODD", name, i, q1, q2, t1, t2, brkv))
            extra = f"brk={[k - i for k in brk]} fb={[rows[k]['fb'] for k in brk]} v={brkv}"
        elif set(p1) & set(p2):
            cls = "N2"; extra = ""
        else:
            both = all(rows[t1]["nxt"][v] == B[v] for v in p2)
            cls = "N3b" if both else "N3"
            h = max([q1, *p1, q2, *p2], key=lambda v: E.rank[v])
            Uc = [v for v in range(g.n) if rows[t1]["vs"][v][0] == c]
            top = max(E.rank[v] for v in Uc); gap = top - E.rank[h]
            GAPS[(cls, gap)] += 1; C["max_gap_" + cls] = max(C["max_gap_" + cls], gap); extra = f"gap={gap} |Uc|={len(Uc)}"
        if cls not in ("N1fb", "N1sw", "N2", "N3", "N3b"): C["CLS_V"] += 1
        C["flips"] += 1; C["flips_" + cls] += 1; nf += 1
        if onset: C["onsets"] += 1; C["onsets_" + cls] += 1; no += 1
        if VERB: print(f"  FLIP {name} phase@{i} len={j - i} q1={q1} q2={q2} t1={t1 - i} t2={t2 - i} onset={int(onset)} {cls} {extra}")
    if nf:
        C["phases_with_flips"] += 1; C["max_flips_phase"] = max(C["max_flips_phase"], nf)
        MAXP.append((no, nf, j - i, rho, g.n, name, i))
    C["phases"] += 1

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
    print("GAPS", dict(sorted(GAPS.items())))
    for m in sorted(MAXP, reverse=True)[:5]: print("TOP onsets/flips/len/rho/n", m)
    for v in VIOL[:8]: print("VIOLATION", v)
    print("FLIPCLS PASS" if not VIOL and not C["CLS_V"] else "FLIPCLS FAIL")

if __name__ == "__main__":
    main()
