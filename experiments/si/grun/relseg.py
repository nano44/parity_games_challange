#!/usr/bin/env python3
"""L-SI box 25 (successor 21): DATA for Theorem STATIC-DEPTH-REL and Corollary REL-SPLIT (docs/si/N5-GRUN-box25.md §4). For a state b of a
fallback-free in-phase run: Q := Even vertices of out-degree >= 2; X_b := the closure of Q under adding the Even vertices of the W- and honest b-plays of
its members; RO_b := Odd vertices on the honest b-play of some v in X_b; CW_b / CH_b := the W-cycles / honest cycles reached by the W- /
honest b-plays of the vertices of X_b. [a, b] is REL-ADMISSIBLE if sigma-bar_t = sigma-bar_b on
RO_b and every cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every t in [a, b]. Each run is cut from its end into maximal
REL-admissible segments; per segment the two-frame depth d (piece/sdprime.py, terminals T_W = vertices of CW_b, T_H = of CH_b, Q only) is
computed ((H4') may fail) and the segment length is checked against max_Q d (LEN_V), and per vertex of Q its settling (SET_V).
Per run: SEG = number of segments, G = sigma-bar-changing transitions; prints max SEG, max G - (SEG - 1), and the runs with most SEG.
MUT=1: d - 1 (must bite). Usage: relseg.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.join(HERE, "..", "root"), os.path.join(HERE, "..", "runlin"), os.path.join(HERE, "..", "piece")): sys.path.insert(0, p)
from common import rows, load, readstart
from staticdepth import walk
from trace import runs
from pieceh import norm
from sdprime import depths
C = Counter(); TOP = []; MUT = os.environ.get("MUT") == "1"

def cycof(nx, v): return norm([walk(nx, v)[1]])

def segcount(g, R):
    """max over the fallback-free runs of R of the number of REL segments (cheap: no depth checks)."""
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]; best = 0
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    for s, e, i, j in runs(R):
        seg, b = 0, e
        while b >= s:
            B = R[b]; X, st = set(), list(Q)
            while st:
                x = st.pop()
                if x in X: continue
                X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
            RO = {y for v in X for y in sum(walk(B["nxt"], v), ()) if g.owner[y] == 1}
            CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
            CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
            a = b
            while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= CWt[a - 1] and CH <= CHt[a - 1]: a -= 1
            seg += 1; b = a - 1
        best = max(best, seg)
    return best

def run(g, name, start=None):
    E, R = rows(g, start); n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    CWt = [norm(frozenset(walk(r["wn"], v)[1] for v in range(n))) for r in R]; CHt = [norm(frozenset(walk(r["nxt"], v)[1] for v in range(n))) for r in R]
    for s, e, i, j in runs(R):
        if e <= s: continue
        C["runs"] += 1; G = sum(R[t]["sb"] != R[t + 1]["sb"] for t in range(s, e)); seg = 0; b = e
        while b >= s:
            B = R[b]
            X, st = set(), list(Q)                 # X: Q closed under "Even vertices on the W- or honest b-play of a vertex of X"
            while st:
                x = st.pop()
                if x in X: continue
                X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
            RO = {y for v in X for y in sum(walk(B["nxt"], v), ()) if g.owner[y] == 1}
            CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
            CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
            a = b
            while a > s and all(R[a - 1]["sb"][u] == B["sb"][u] for u in RO) and CW <= CWt[a - 1] and CH <= CHt[a - 1]: a -= 1
            seg += 1; ln = b - a; C["segments"] += 1; C["seg_len_max"] = max(C["seg_len_max"], ln)
            TW = {v for c in CW for v in c}; TH = {v for c in CH for v in c}
            try:
                dW, dH = depths(g, B, TW, TH, Q); dm = max([dW[v] for v in Q] + [dH[v] for v in Q], default=0)
                if ln > dm: C["LEN_V"] += 1
                if ln > n - 1: C["N1_V"] += 1
                for v in Q:
                    for fr, dd in (("wn", dW), ("nxt", dH)):
                        for t in range(a + max(dd[v] - MUT, 0), b + 1):
                            if walk(R[t][fr], v) != walk(B[fr], v): C["SET_V"] += 1; TOP.append(("SETV", name, a, b, v, t, dW[v], dH[v])); break
            except (ValueError, RecursionError): C["h4p_fail"] += 1
            b = a - 1
        C["SEG_max"] = max(C["SEG_max"], seg); C["G_minus_cuts_max"] = max(C["G_minus_cuts_max"], G - (seg - 1))
        C["SEG_over_n_x1000_max"] = max(C["SEG_over_n_x1000_max"], 1000 * seg // n)
        if seg - 1 > G + (e - s): C["CUT_V"] += 1
        TOP.append((seg, G, e - s, n, name, s, e))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in [x for x in TOP if x[0] == "SETV"][:6]: print("EXAMPLE", x)
    for x in sorted([x for x in TOP if x[0] != "SETV"], key=lambda x: -x[0] / x[3])[:8]: print("TOP SEG %d G %d run %d n %d %s [%d,%d]" % x)
    print("RELSEG PASS" if not any(k in C for k in ("LEN_V", "N1_V", "SET_V")) else "RELSEG FAIL")

if __name__ == "__main__":
    main()
