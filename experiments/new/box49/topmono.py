#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA for docs/new/N5-READER-box49.md §12: the Lead's CONJECTURE TOP-MONO (04:57Z). For a vertex v and a phase P,
at each P-change of v (P(Ξ_t v) != P(Ξ_{t+1} v) as vertex sets; λ is constant on P, so the cycle node is fixed) let d_t := the largest rank in
the symmetric difference P_t Δ P_{t+1}. TOP-MONO asks d to be non-increasing along the phase. Counts: PCH (P-changes), UP (steps with
d_{t'} > d_t for consecutive P-changes t < t'), and per (v, P) the number of distinct top values and of UP steps; the max over the corpus.
Usage: topmono.py STARTS SEED (--list FILE | files) [--nmax N]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter
C = Counter(); MAX = {}; FIRST = []
def mx(k, v, tag):
    if v > MAX.get(k, (-1,))[0]: MAX[k] = (v, tag)

def run(g, st, nm):
    E, R = rows(g, st); n = g.n
    for i, j in phases(R):
        for v in range(n):
            ds = []
            for t in range(i, j):
                a, b = R[t]["vs"][v][1], R[t + 1]["vs"][v][1]
                if a != b: ds.append(((a ^ b).bit_length() - 1, t))
            C["PCH"] += len(ds)
            # reading 2: the top rank of P(Ξ_t v) itself (the Lead's DATA sentence); TUP = steps where it goes UP at a P-change
            tops = [R[t]["vs"][v][1].bit_length() - 1 for t in range(i, j + 1)]
            tup = sum(1 for t in range(len(tops) - 1) if tops[t + 1] > tops[t])
            C["TUP"] += tup; C["TDOWN"] += sum(1 for t in range(len(tops) - 1) if tops[t + 1] < tops[t])
            isgate = g.owner[v] == 1 and len(g.succ[v]) >= 2
            # Lemma TOP-SHAPE checks (N5-READER §12): top(P) rises only to an EVEN rank (priority parity of the vertex of that rank), an
            # even top never falls, and once the top is even it stays even (P never empties again). VIOL_* must be 0.
            par = {E.rank[x]: E.par[x] for x in range(n)}
            for t in range(len(tops) - 1):
                u0, u1 = tops[t], tops[t + 1]
                if u1 > u0 and par.get(u1) != 0: C["VIOL_rise_to_odd"] += 1
                if u0 >= 0 and par.get(u0) == 0 and u1 < u0: C["VIOL_even_top_fell"] += 1
            seen_even = False
            for u in tops:
                if u >= 0 and par.get(u) == 0: seen_even = True
                elif seen_even: C["VIOL_not_even_after_even"] += 1; break
            if isgate: C["gate_TUP"] += tup
            if tup: C["vP_with_TUP"] += 1; mx("TUP_per_vP" + ("_gate" if isgate else ""), tup, (nm, (i, j), n, v, tops[:1] + [x for k, x in enumerate(tops[1:]) if x != tops[k]][:15]))
            ups = sum(1 for k in range(1, len(ds)) if ds[k][0] > ds[k - 1][0])
            C["UP"] += ups
            if ups:
                C["vP_with_UP"] += 1
                if len(FIRST) < 6: FIRST.append((nm, (i, j), n, v, [d for d, _ in ds][:20], [t for _, t in ds][:20]))
            tag = (nm, (i, j), n, v)
            mx("UP_per_vP", ups, tag); mx("distinct_tops_per_vP", len({d for d, _ in ds}), tag); mx("PCH_per_vP", len(ds), tag)

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    for f in files:
        try:
            g = load(f)
            if g.n > nmax: continue
            sf = f[:-3] + ".start"
            sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                      {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
            for st in sts: run(g, st, os.path.relpath(f, ROOT)); C["runs"] += 1
        except Exception: C["ERR"] += 1
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
    for k, v in sorted(MAX.items()): print("max", k, v)
    for e in FIRST: print("UP", e)
