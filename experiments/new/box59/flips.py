#!/usr/bin/env python3
"""L-NEW box 59 (successor 34): anatomy of Odd's best-reply changes (SBC_sigma) in N5-SF (box54/n5sf.py, default MODE, SPEC S3 start).
For every transition j -> j+1 of the distinct-sigma sequence and every Odd vertex u with sbar_j(u) = a != b = sbar_{j+1}(u) it prints
the decisive vertex of Odd's comparison of a and b at j and at j+1: dec(a, b) = the most relevant vertex of P(a) xor P(b) when a and b
have the same cycle node (else 'C' + cycle nodes; '=' if equal paths, length decides). Valuations Xi = (cycle node, P bitmask, length)
as in experiments/si/si.py. Usage: flips.py GAME.pg [--labels] [--summary]"""
import sys, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54"))
import n5sf
from n5x import load

def labels(path):
    lab = {}
    for line in open(path):
        m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s*"([^"]*)"', line)
        if m: lab[int(m.group(1))] = m.group(2)
    return lab

def dec(E, va, vb):
    if va[0] != vb[0]: return ("C", va[0], vb[0])
    x = va[1] ^ vb[1]
    if x == 0: return ("=",)
    # most relevant bit: E.bit[v] are distinct powers; the highest-rank vertex in x
    best = max((v for v in range(len(E.bit)) if E.bit[v] & x), key=lambda v: E.rank[v])
    return ("P", best, "a" if va[1] & E.bit[best] else "b")

def run(path):
    g = load(path); E, T = n5sf.trace(g)
    seq = [T[0]]
    for x in T[1:]:
        if x.get("cycle"): break
        if x["s"] != seq[-1]["s"]: seq.append(x)
    ev = []
    for j in range(len(seq) - 1):
        A, B = seq[j], seq[j + 1]
        if A["sb"] == B["sb"]: continue
        va, _ = E.evaluate(tuple(A["s"])); vb, _ = E.evaluate(tuple(B["s"]))
        for u in range(g.n):
            if g.owner[u] == 1 and A["sb"][u] != B["sb"][u]:
                a, b = A["sb"][u], B["sb"][u]
                ev.append(dict(j=j, u=u, a=a, b=b, old=dec(E, va[a], va[b]), new=dec(E, vb[a], vb[b])))
    return g, E, seq, ev

if __name__ == "__main__":
    path = sys.argv[1]; g, E, seq, ev = run(path)
    lab = labels(path) if "--labels" in sys.argv else {}
    L = lambda v: lab.get(v, str(v)) if isinstance(v, int) else v
    if "--summary" not in sys.argv:
        for e in ev:
            print(e["j"], L(e["u"]), L(e["a"]), ">", L(e["b"]), "old", tuple(map(L, e["old"])), "new", tuple(map(L, e["new"])))
    per = collections.Counter(e["u"] for e in ev); jj = len({e["j"] for e in ev})
    pd = collections.Counter((e["u"], e["new"]) for e in ev)
    print(f"SUMMARY n {g.n} orbit {len(seq)} SBC {jj} flips {len(ev)} maxflips/u {max(per.values()) if per else 0} "
          f"oddbranch {sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1)} max(u,newdec) {max(pd.values()) if pd else 0}")

def rec_stats(g, E, seq, ev):
    """per Odd vertex u: flips(u) and REC(u) = #j with top(Xi_j(u)) != top(Xi_{j+1}(u)), top = (cycle node, most relevant path vertex).
    Returns rows (u, flips, REC) for every Odd u with flips > 0, and SBC."""
    vals = [E.evaluate(tuple(st["s"]))[0] for st in seq]
    # REC0: path vertices whose own valuation is constant over the whole run (the sink zone) are ignored
    mask = 0
    for v in range(g.n):
        if any(vals[j][v] != vals[0][v] for j in range(len(seq))): mask |= E.bit[v]
    def top(val):
        x = val[1] & mask; t = max((v for v in range(g.n) if E.bit[v] & x), key=lambda v: E.rank[v]) if x else -1
        return (val[0], t)
    tops = [[None] * g.n for _ in seq]
    for j in range(len(seq)):
        for u in range(g.n):
            if g.owner[u] == 1: tops[j][u] = top(vals[j][u])
    import collections
    fl = collections.Counter(e["u"] for e in ev); rows = []
    for u in fl:
        rows.append((u, fl[u], sum(1 for j in range(len(seq) - 1) if tops[j][u] != tops[j + 1][u])))
    return rows
