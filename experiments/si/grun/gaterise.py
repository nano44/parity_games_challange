#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for Lemma GATE-RISE (docs/si/N5-GRUN-box25.md §2). For every fallback-free in-phase run S and every
change y1 -> y2 of sigma-bar at an Odd vertex u at t -> t+1: CYC if u is on an honest cycle at t or t+1; TIE if Xi_t(y1) = Xi_t(y2); THRU if y2's honest t-play passes through u;
otherwise the lemma says Xi_(t+1)(u) > Xi_t(u) strictly (RISE_V counts failures). Also checks Xi monotone (MONO_V: Xi_(t+1)(v) < Xi_t(v) at
some v, against RESULTS R15 (a)), and per run G <= sum over Odd u of XR_S(u) + TIE + CYC + THRU (SUM_V). XR_S(u): transitions of S changing Xi(u).
MUT=1 claims a strict rise of Xi(y2) instead (must bite). Usage: gaterise.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin")): sys.path.insert(0, p)
from common import rows, load, readstart
from staticdepth import walk
from trace import runs
C = Counter(); EX = []; MUT = os.environ.get("MUT") == "1"

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; K = [[E.key(x) for x in r["vs"]] for r in R]
    oncyc = [{v for v in range(n) if v in walk(r["nxt"], v)[1]} for r in R]
    for a, b, i, j in runs(R):
        if b <= a: continue
        C["runs"] += 1; G = 0; tie = cyc = 0
        for t in range(a, b):
            if any(K[t + 1][v] < K[t][v] for v in range(n)): C["MONO_V"] += 1
            if R[t]["sb"] != R[t + 1]["sb"]: G += 1
            for u in range(n):
                if g.owner[u] != 1: continue
                y1, y2 = R[t]["sb"][u], R[t + 1]["sb"][u]
                if y1 == y2: continue
                C["changes"] += 1
                if u in oncyc[t] or u in oncyc[t + 1]: C["cyc"] += 1; cyc += 1; continue
                if K[t][y1] == K[t][y2]: C["tie"] += 1; tie += 1; continue
                if u in walk(R[t]["nxt"], y2)[0] + walk(R[t]["nxt"], y2)[1]: C["thru"] += 1; cyc += 1; continue
                C["clean"] += 1
                ok = (K[t + 1][y2] > K[t][y2]) if MUT else (K[t + 1][u] > K[t][u])
                if not ok: C["RISE_V"] += 1; EX.append((name, t, u, y1, y2))
        xr = sum(sum(K[t + 1][u] != K[t][u] for t in range(a, b)) for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1)
        if G > xr + tie + cyc: C["SUM_V"] += 1
        gx = max((sum(K[t + 1][u] != K[t][u] for t in range(a, b)) for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1), default=0)
        C["XR_gate_max"] = max(C["XR_gate_max"], gx); C["XR_gate_over_n_x1000_max"] = max(C["XR_gate_over_n_x1000_max"], 1000 * gx // n)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in EX[:6]: print("EXAMPLE", x)
    print("GATERISE PASS" if not any(k in C for k in ("RISE_V", "MONO_V", "SUM_V")) else "GATERISE FAIL")

if __name__ == "__main__":
    main()
