#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md §13): L-LIT T37 §3's CONJECTURE (carries of a vertex per λ-run ≤ poly(n) × the reopenings of
gates on its play), measured with an explicit operational reading. Per λ-run (λ_Ξ constant) and vertex y:
  NM(y)  carries of y (T33 §1.2) in the λ-run;
  RW(y)  transitions s of the λ-run with an Odd switch (τ_s(e) ≠ τ_(s+1)(e)) at a vertex e on y's W-play (σ_s, τ_s) at s or at s + 1;
  RH(y)  the same with y's honest play (σ, σ̄);
  RI(y)  states s of the λ-run with some Odd e on y's W-play having Iτ_s(e) ≠ ∅ (a gate open for Odd, taken or not).
A gate REOPENING in T37's sense (an Odd switch back into a cycle region) is a special RW/RH event, so RW + RH + RI over-count reopenings.
Counters: zero_reopen (vertices with NM > 0 and RW = RH = RI = 0 in their λ-run; the literal multiplicative form fails there),
nm_zero_max (their largest NM), ratio_max (max NM / (RW + RH + 1)). Usage: reopen.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
from common import rows, load, readstart, Engine, dual
from compose import matched, bits
from staticdepth import walk
C = Counter(); EX = []

def onplay(nx, y):
    p, c = walk(nx, y); return set(p) | set(c)

def _run(E, g, R, name):
    n = g.n; rk2v = {E.rank[v]: v for v in range(n)}; odd = lambda r: E.par[rk2v[r]] == 1; T = len(R) - 1
    Ed = Engine(dual(g)); OD = [e for e in range(n) if g.owner[e] == 1]
    It = [set(e for e, w in Ed.improving(tuple(r["t"]), Ed.evaluate(tuple(r["t"]))[0])) for r in R]
    lam = [tuple(x[0] for x in r["vs"]) for r in R]; i = 0
    while i < T:
        j = i
        while j < T and lam[j + 1] == lam[i]: j += 1
        if j > i:
            nm = Counter(); rw = Counter(); rh = Counter(); ri = Counter()
            for s in range(i, j):
                A, B = R[s], R[s + 1]; tsw = {e for e in OD if A["t"][e] != B["t"][e]}
                for y in range(n):
                    a, b = A["vs"][y], B["vs"][y]
                    if a[1] != b[1]:
                        rc = E.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
                        if not matched(bits(a[1]), bits(b[1]), w, odd): nm[y] += 1
                    if tsw and (tsw & (onplay(A["wn"], y) | onplay(B["wn"], y))): rw[y] += 1
                    if tsw and (tsw & (onplay(A["nxt"], y) | onplay(B["nxt"], y))): rh[y] += 1
                    if It[s] and (It[s] & onplay(A["wn"], y)): ri[y] += 1
            for y in nm:
                C["carrying_vertex_runs"] += 1
                if rw[y] == rh[y] == ri[y] == 0:
                    C["zero_reopen"] += 1; C["nm_zero_max"] = max(C["nm_zero_max"], nm[y])
                    if nm[y] == C["nm_zero_max"]: EX.append(("ZERO", name, i, j, y, nm[y], n))
                C["ratio_max_x100"] = max(C["ratio_max_x100"], 100 * nm[y] // (rw[y] + rh[y] + 1))
        i = j + 1 if j > i else i + 1

def run(g, name, start=None):
    E, R = rows(g, start, cap=20000); _run(E, g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0])
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                try: run(load(f), p[0], readstart(s) if s else None)
                except Exception: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[-4:]: print("EXAMPLE", z)

if __name__ == "__main__":
    main()
