#!/usr/bin/env python3
"""L-SI box 26: DATA for Theorem LAST-STEP and its frontier (docs/si/N5-LWP-box26.md §7). In each maximal REL-admissible segment [a, b]
(lwp/seglast.py's cutting): S_t := the vertices whose W-play and honest play at every s in [t, b] equal those at b. A FRONTIER vertex at
t is an Even v in X_b outside T = T_W u T_H with sigma_t(v) != sigma_b(v) and sigma_b(v) in S_t. Checks per transition t -> t+1:
FR_V (no frontier vertex), FRL_V (a frontier vertex whose last switch is not at t: the theorem says this never happens when GEN_W holds),
and per segment whether (H4'_rel) fails (h4p_fail) and, then, whether every frontier step still existed (FR_V there). CYCSET_V: (H4'_rel)-failing segments with a J_b-cycle vertex not settled from a. MUT=1 asks for
sigma_b(v) in S_(t-1) instead (must bite). Usage: laststep.py --list FILE | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import seglast
from common import rows, load, readstart
from staticdepth import walk
from relseg import cycof
from sdprime import depths
C = Counter(); EX = []; MUT = os.environ.get("MUT") == "1"

def h4score(g, R):
    """for lwp/xclimb.py OBJ=H4: (frontier failures, longest segment where (H4'_rel) fails, or -1)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try: _run(g, R, "x"); return C["FR_V"] + C["FRL_V"] + C["CYCSET_V"], C.get("h4len_max_plus1", 0) - 1
    finally: C, EX = save

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def _run(g, R, name):
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        B = R[b]; X, st = set(), list(Q)
        while st:
            x = st.pop()
            if x in X: continue
            X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
        CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
        CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
        T = {v for c in CW for v in c} | {v for c in CH for v in c}
        try: depths(g, B, {v for c in CW for v in c}, {v for c in CH for v in c}, Q); h4 = True
        except (ValueError, RecursionError): h4 = False; C["h4p_fail"] += 1; C["h4len_max_plus1"] = max(C["h4len_max_plus1"], b - a + 1)
        pw = {v: walk(B["wn"], v) for v in range(n)}; ph = {v: walk(B["nxt"], v) for v in range(n)}
        # first[v]: least s in [a, b] with v settled from s
        first = {}
        for v in range(n):
            s = b
            while s > a and walk(R[s - 1]["wn"], v) == pw[v] and walk(R[s - 1]["nxt"], v) == ph[v]: s -= 1
            first[v] = s
        if not h4:                                # J_b-cycle vertices: are they settled from a? (CYC-SET)
            def nxt(v, fr):
                p = (pw if fr == "W" else ph)[v]; seq = list(p[0]) + list(p[1])
                for x in seq[1:]:
                    if g.owner[x] == 0 and x not in T: return x
                return None
            Ev = [v for v in X if v not in T]
            J = {v: {w for w in (nxt(v, "W"), nxt(v, "H")) if w is not None} for v in Ev}
            oncyc = set()
            for v in Ev:                          # v on a J_b-cycle iff v reaches itself
                seen, stk = set(), list(J[v])
                while stk:
                    x = stk.pop()
                    if x == v: oncyc.add(v); break
                    if x in seen or x not in J: continue
                    seen.add(x); stk.extend(J[x])
            C["jcyc_vertices"] += len(oncyc)
            bad = [v for v in oncyc if first[v] > a]
            if bad: C["CYCSET_V"] += 1; EX.append(("CYCSET", name, a, b, sorted(bad), {v: first[v] for v in bad}))
        last = {}
        for t in range(a, b):
            for v in range(n):
                if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: last[v] = t
        C["segs"] += 1
        for t in range(a, b):
            C["trans"] += 1
            fr = [v for v in X if v not in T and R[t]["s"][v] != B["s"][v] and first[B["s"][v]] <= t - (1 if MUT else 0)]
            if not fr: C["FR_V"] += 1; EX.append((name, a, b, t, h4)); C["FR_V_h4fail"] += (not h4)
            for v in fr:
                if last.get(v) != t: C["FRL_V"] += 1; EX.append(("FRL", name, a, b, t, v))

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p: run(load(os.path.join(ROOT, p[0])), p[0], readstart(os.path.join(ROOT, p[1])) if len(p) > 1 and os.environ.get("START") == "1" else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in EX[:8]: print("EXAMPLE", z)
    print("LASTSTEP PASS" if "FR_V" not in C and "FRL_V" not in C else "LASTSTEP FAIL")
    print("CYCSET PASS" if "CYCSET_V" not in C else "CYCSET FAIL")

if __name__ == "__main__":
    main()
