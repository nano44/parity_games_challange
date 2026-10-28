#!/usr/bin/env python3
"""L-NEW box 49 (successor 30): local search for a passive gadget that maximises one new vertex's count while the run on the old vertices
stays the SAME (dress.py's comparison). KIND = oddreader (Odd o, edges S; the count = XR(o)), evenreader
(Even e, edges S; the count = e's Even switches) or evenmax2 (Odd readers o1, o2 on S1, S2 and an Even e with edges {o1, o2}; the count =
e's Even switches; S codes S1 by entries >= 0 and S2 by entries -x-1). S ranges over subsets of one class C (the vertices whose cycle node is C at the first state
of the longest phase). Hill climbing with single add / drop / swap moves, seeded. Prints the best S, its count, and the dressed files.
Usage: search.py BASE.pg BASE.start KIND OUT_PREFIX SEED ITERS [CLASS]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import dress
from dress import load, rows, phases, readstart

def specs_of(kind, S):
    if kind == "evenmax2":                      # two Odd readers (min-envelopes of S1, S2) under one Even vertex e: e = max of the two minima
        S1, S2 = sorted(x for x in S if x >= 0), sorted(-x - 1 for x in S if x < 0)
        if not S1 or not S2: return None
        return [f"1:0:{','.join(map(str, S1))}:{S1[0]}", f"1:0:{','.join(map(str, S2))}:{S2[0]}", "0:0:h0,h1:h0"]
    return [("0" if kind == "evenreader" else "1") + f":0:{','.join(map(str, sorted(S)))}:{min(S)}"]

def score(base, bst, kind, out, S):
    sp = specs_of(kind, S) if S else None
    if not sp: return -1, None
    dress.build(base, bst, out, sp)
    r = dress.compare(base, bst, out + ".pg", out + ".start", quiet=True)
    if not r["same"] or not r["rows"]: return -1, r
    row = max(r["rows"], key=lambda x: x["length"])
    z, own, xr, sw = row["new"][-1]             # the last new vertex is the counted one (o, e, or the Even top of evenmax2)
    return (xr if kind == "oddreader" else sw), r

def main():
    base, bst, kind, out, seed, iters = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
    g = load(base); E, R = rows(g, readstart(bst)); P = max(phases(R), key=lambda p: p[1] - p[0])
    A = R[P[0]]
    classes = {}
    for v in range(g.n): classes.setdefault(A["vs"][v][0], []).append(v)
    C = int(sys.argv[7]) if len(sys.argv) > 7 else max(classes, key=lambda c: len(classes[c]))
    U = classes[C]; rng = random.Random(seed)
    if kind == "evenmax2": U = U + [-x - 1 for x in U]   # negative entries code membership in S2
    cur = set(rng.sample(U, min(len(U), 6))); best, _ = score(base, bst, kind, out, cur); bestS = set(cur)
    for it in range(iters):
        cand = set(cur); mv = rng.random(); x = rng.choice(U)
        if mv < 0.4: cand.add(x)
        elif mv < 0.7 and len(cand) > 1: cand.discard(rng.choice(sorted(cand)))
        else:
            if cand: cand.discard(rng.choice(sorted(cand)))
            cand.add(x)
        sc, _ = score(base, bst, kind, out, cand)
        if sc >= best: cur = cand
        if sc > best: best, bestS = sc, set(cand); print(f"it {it} count {best} |S| {len(bestS)} S {sorted(bestS)}", flush=True)
    sc, r = score(base, bst, kind, out, bestS)
    print(f"BEST class {C} kind {kind} count {sc} S {','.join(map(str, sorted(bestS)))} phase {P} length {P[1] - P[0]} n_dressed {g.n + 1}")

if __name__ == "__main__":
    main()
