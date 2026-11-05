#!/usr/bin/env python3
"""L-NEW box 152: check of Lemma PREMERGE / Corollary PMDIFF and Lemma STABLE-PATH on simulated IDEAL-ACYC runs (degree <= 2;
box150/check.py simulator). For every mover x with two options and every ordered pair of states (a, c) of the run:
 PMDIFF   C_a(x) != C_c(x) and no mover on exactly one of x's face chains at a changes its option between a and c
 SPATH    C_a(x) = b, every Q-mover (pre-merge part of face 1-b at a) keeps its option at c, every P-mover (pre-merge part of face b)
          keeps its option or is stable at c, and C_c(x) != b
Both counters must be 0. Also counts the pairs where each premise applies (non-vacuity). ALL=1: every start for N <= ALLN.
Usage: lemcheck.py genome.json ..."""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def run(G, start):
    g = Gen(G); S, _ = g.run(start); return g, S
tot = {"runs": 0, "pairs": 0, "PMDIFF": 0, "SPATH": 0, "pm_prem": 0, "sp_prem": 0}
for p in sys.argv[1:]:
    G = json.load(open(p))
    if max(len(o) for o in G["opts"]) > 2: continue
    starts = [G["start"]]
    if os.environ.get("ALL") and G["N"] <= int(os.environ.get("ALLN", "8")):
        starts = [list(s) for s in itertools.product(*[range(len(o)) for o in G["opts"]])]
    for st in starts:
        g, S = run(G, st); tot["runs"] += 1; N = g.N
        def chain(s, x, k):
            out = []; z = g.opts[x][k][1]
            while z >= 0: out.append(z); z = g.opts[z][s[z]][1]
            return out
        C = [[(1 if g.face(s, x, 1) > g.face(s, x, 0) else 0) if len(g.opts[x]) == 2 else None for x in range(N)] for s in S]
        for x in range(N):
            if len(g.opts[x]) < 2: continue
            for a in range(len(S)):
                A = [chain(S[a], x, 0), chain(S[a], x, 1)]
                for c in range(len(S)):
                    if c == a: continue
                    tot["pairs"] += 1
                    sym = [y for y in set(A[0]) ^ set(A[1])]
                    if all(S[a][y] == S[c][y] for y in sym):
                        tot["pm_prem"] += 1
                        if C[a][x] != C[c][x]: tot["PMDIFF"] += 1
                    b = C[a][x]; Pm = [y for y in A[b] if y not in A[1 - b]]; Qm = [y for y in A[1 - b] if y not in A[b]]
                    if all(S[a][y] == S[c][y] for y in Qm) and all(S[a][y] == S[c][y] or C[c][y] == S[c][y] or C[c][y] is None for y in Pm):
                        tot["sp_prem"] += 1
                        if C[c][x] != b: tot["SPATH"] += 1
print("LEMCHECK", " ".join(f"{k} {v}" for k, v in tot.items()))
