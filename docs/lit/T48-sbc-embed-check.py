#!/usr/bin/env python3
"""T48 DATA (L-LIT): along N5-SF's Even run (distinct-sigma sequence, L-NEW n5sf.py MODE default), per vertex:
EVMAX = most sigma-changes at one Even vertex; EVRET = Even returns to an edge left earlier (summed); EVDEG = out-degree of EVMAX vertex;
ODMAX / ODRET the same for sbar at Odd vertices; SBC; values (= #sigma); PLAYRET = returns of a vertex's joint play (sigma, sbar) to a play
it left earlier (summed); SEGRET = returns of a play SEGMENT x -> y (prefix of x's play up to the first visit of y) to a segment
witnessed earlier for the same (x, y) and then replaced by a different witnessed segment (summed over (x, y)); SEGPAIRS = pairs with a return.
Gusfield's induction (thesis 1980 Thm 4.4) needs every sub-pair to be optimal on one interval, so SEGRET > 0 rules out a generic
one-parameter linear embedding of the joint plays (T48 §1). Read-only use of experiments/new/box54/n5sf.py (L-NEW, sha1 1ea3bdc7) and box21/n5x.py.
Usage (from the repo root): python3 -I docs/lit/T48-sbc-embed-check.py GAME [START]"""
import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf
from n5x import load, readstart
from collections import Counter, defaultdict

def play(g, s, sb, v):
    seen = {}; p = []
    while v not in seen:
        seen[v] = len(p); p.append(v); v = s[v] if g.owner[v] == 0 else sb[v]
    return tuple(p) + (v,)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, T = n5sf.trace(g, st); T = [x for x in T if "lam" in x]; n = g.n
    seq = []
    for x in T:
        if not seq or seq[-1][0] != x["s"]: seq.append((x["s"], x["sb"]))
    ch = Counter(); ret = Counter(); used = defaultdict(set); sbc = 0
    plays = [None] * n; pused = defaultdict(set); pret = 0
    seglast = {}; segleft = defaultdict(set); segret = 0; segpairs = set(); segfirst = {}; wit = None
    def segs(pl):
        x = pl[0]; first = {}
        for i, y in enumerate(pl[:-1]):
            if y not in first: first[y] = i
        for y, i in first.items():
            if i > 0: yield (x, y), pl[:i + 1]
    for v in range(n):
        if g.owner[v] == 0: used[v].add(seq[0][0][v])
        else: used[v].add(seq[0][1][v])
        plays[v] = play(g, seq[0][0], seq[0][1], v); pused[v].add(plays[v])
        for k, sg in segs(plays[v]): seglast[k] = sg; segfirst[(k, sg)] = 0
    for i in range(1, len(seq)):
        s, sb = seq[i]; ps, psb = seq[i - 1]
        if any(g.owner[u] == 1 and sb[u] != psb[u] for u in range(n)): sbc += 1
        for v in range(n):
            a, b = (ps[v], s[v]) if g.owner[v] == 0 else (psb[v], sb[v])
            if a != b:
                ch[v] += 1
                if b in used[v]: ret[v] += 1
                used[v].add(b)
            q = play(g, s, sb, v)
            if q != plays[v]:
                for k, sg in segs(q):
                    old = seglast.get(k)
                    if old is not None and old != sg:
                        if sg in segleft[k]:
                            segret += 1; segpairs.add(k)
                            if wit is None: wit = (k, segfirst[(k, sg)], i, sg, old)
                        segleft[k].add(old)
                    segfirst.setdefault((k, sg), i)
                    seglast[k] = sg
                if q in pused[v]: pret += 1
                pused[v].add(q); plays[v] = q
    if wit and os.environ.get("WIT"):
        (x, y), j0, i, sg, old = wit
        print("WITNESS pair", x, y, "segment", list(sg), "first used at index", j0, "left, then the different segment", list(old),
              "used just before index", i, "and the first segment used again at index", i)
    ev = [v for v in range(n) if g.owner[v] == 0]; od = [v for v in range(n) if g.owner[v] == 1]
    evm = max(ev, key=lambda v: ch[v]) if ev else None
    m = sum(len(set(x)) for x in g.succ)
    print("ROW", os.path.basename(sys.argv[1]), "n", n, "m", m, "values", len(seq), "SBC", sbc,
          "EVMAX", ch[evm] if ev else 0, "EVDEG", len(set(g.succ[evm])) if ev else 0, "EVRET", sum(ret[v] for v in ev),
          "EVCHG", sum(ch[v] for v in ev), "ODMAX", max((ch[v] for v in od), default=0), "ODRET", sum(ret[v] for v in od), "PLAYRET", pret, "SEGRET", segret, "SEGPAIRS", len(segpairs), flush=True)
main()
