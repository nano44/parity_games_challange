#!/usr/bin/env python3
"""L-SI box 32 (docs/si/N5-RTC-box32.md §5): exit-entry ROUNDS of one vertex in |D| = 1, c1 = c2 frozen W-phases. A round of x: x leaves S
(the vertices whose (rho, tau)-play meets the gate o) at q1 -> q1+1 and re-enters at q2 -> q2+1 (q1 < q2). Old side: W_{q1}(x) = pre1 (+) a2
(a2 = W_{q1}(o)); new side: Xi_{q2+1}(x) = pre2 (+) a1 (a1 = Xi_{q2+1}(o)). By W-MON and the arena, new > old strictly (checked: ORD_V).
Class of the round by the top rank of the symmetric difference of the two P-masks: A = it lies in the prefix parts only (the prefix climbed
above the tails' difference), B = in the tail parts only (the gate's Xi tail at q2+1 passed its W tail at q1), M = a vertex in a prefix on
one side and in the tail on the other, L = equal masks (length decides). Also: gate crossings GC (maximal chains a2_{t} < a1_{t'}, t < t').
Usage: rounds.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "frz")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart, phases
from fwphase import fwphases
from gates import basins
C = Counter(); MX = {}; EX = []

def _run(E, g, R, name):
    n = g.n
    for i, j in phases(R):
        for a, b in fwphases(R, i, j):
            D = [u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]]
            if len(D) != 1: continue
            o = D[0]
            if R[a]["vs"][o][0] != R[a]["W"][o][0]: continue
            C["phases"] += 1
            F = [basins(R[t]["wn"], {o}, n) for t in range(a, b + 1)]
            td = all(F[t - a][R[t]["t"][o]] == -1 and F[t - a][R[t]["sb"][o]] == -1 for t in range(a, b + 1))
            C["phases_TD"] += td
            inS = [[F[t - a][v] == o for v in range(n)] for t in range(a, b + 1)]
            # gate crossings: greedy chain t0 = a; next = first t' with Xi_t'(o) > W_t(o)
            gc, t = 0, a
            while True:
                kw = E.key(R[t]["W"][o]); nxt = next((u for u in range(t + 1, b + 1) if E.key(R[u]["vs"][o]) > kw), None)
                if nxt is None: break
                gc += 1; t = nxt
            ent = Counter(); rd = Counter()
            pinc = Counter()
            for x in range(n):
                if x == o: continue
                prev = None
                for t in range(a, b + 1):
                    if not inS[t - a][x]: continue
                    Wx, Wo = R[t]["W"][x], R[t]["W"][o]
                    ln = Wx[2] - Wo[2]; pk = (E.weight(Wx[1] ^ Wo[1]), ln if E.par[Wo[0]] == 1 else -ln)
                    if prev is not None and pk > prev[0]: C["PREINC"] += 1; pinc[x] += 1
                    if prev is not None and (pk > prev[0] if os.environ.get("MUT") == "rev" else pk < prev[0]):
                        C["PREDEC_" + ("round" if prev[1] < t - 1 else "stay")] += 1
                        if len(EX) < 8: EX.append(("PREDEC", name, a, b, "x", x, "t", t, "after", prev[1]))
                    prev = (pk, t)
            for x in range(n):
                if x == o: continue
                last_exit = None
                for t in range(a, b):
                    s0, s1 = inS[t - a][x], inS[t + 1 - a][x]
                    if s0 and not s1: last_exit = t
                    if not s0 and s1:
                        ent[x] += 1
                        if last_exit is None: continue
                        q1, q2 = last_exit, t
                        Wo, Wx = R[q1]["W"][o], R[q1]["W"][x]; Xo, Xx = R[q2 + 1]["vs"][o], R[q2 + 1]["vs"][x]
                        if (Wx[1] & Wo[1]) != Wo[1] or (Xx[1] & Xo[1]) != Xo[1]: C["MASK_NOT_SUPERSET"] += 1
                        p1, t1, p2, t2 = Wx[1] ^ Wo[1], Wo[1], Xx[1] ^ Xo[1], Xo[1]
                        if not E.key(Xx) > E.key(Wx): C["ORD_V"] += 1
                        d = (p1 | t1) ^ (p2 | t2)
                        if d == 0: cl = "L"
                        else:
                            top = 1 << (d.bit_length() - 1)
                            inpre, intail = bool(top & (p1 | p2)), bool(top & (t1 | t2))
                            cl = "A" if inpre and not intail else ("B" if intail and not inpre else "M")
                        C["round_" + cl] += 1; rd[x] += 1
                        if cl == "B" and E.key(Xo) > E.key(R[q1]["W"][o]): C["B_with_gate_crossing"] += 1
                        if len(EX) < 8: EX.append((name, a, b, "x", x, "q1", q1, "q2", q2, cl))
            C["rounds"] += sum(rd.values())
            for key, v in (("entries/vertex", max(ent.values(), default=0)), ("rounds/vertex", max(rd.values(), default=0)), ("GC", gc), ("preinc/vertex", max(pinc.values(), default=0)), ("preinc_total/(n-1)", sum(pinc.values()) / (n - 1))):
                if v > MX.get(key, (-1,))[0]: MX[key] = (v, n, b - a, td, name, a, b)

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
                except Exception as e: C["SKIPPED_input"] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("columns: value, n, phase length, TD, game, a, b")
    for k in sorted(MX): print("MAX", k, MX[k])
    for z in EX: print("EXAMPLE", z)

if __name__ == "__main__": main()
