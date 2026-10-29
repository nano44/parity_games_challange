#!/usr/bin/env python3
"""L-SI box 28 (docs/si/N5-CHG-box28.md): SEG-COUNT charging data per maximal REL segment [a, b] (lwp/seglast.py's cutting).
L(v) = last switch of Even v in [a, b]. slack(t) := #{v : L(v) >= t} - (b - t) for t in [a, b) (SUFFIX-COUNT: slack >= 0 at every t;
slack(a) >= 0 is SEG-COUNT). Deadlock step: no v with L(v) = t. Also checks the PROVED time bound (lay §6 W-STICK′ + READY):
  EARLY_V: an H-sink h at t, not a W-sink, with L(h) < fW(jW h) - 1 (finalizes before its W-chain settles: (a) of note §6)
  INTEREARLY_V: such h that makes an INTERMEDIATE switch at t (to neither sigma_t(h) nor sigma_b(h)) and finalizes early (INTER-JOINT)
  JOINTX_V: such h with L(h) = fW(jW h) - 1 but no other vertex finalizing then (Corollary JOINT says never)
  BND_V: a switching v in E_b with L(v) > max(fW(jW v) - 1, fH(jH v))  (fW/fH = first W-/H-settled state, a for ⊥)
and records, per deadlock step t, slack(t + 1) (DLS_k = deadlock steps with slack(t + 1) = k).
Usage: suffix.py --list FILE | --one GAME [START]   (START=1: read column 2 of the list as the start)"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "lwp")); sys.path.insert(0, os.path.join(HERE, "..", "root"))
import seglast
from common import rows, load, readstart
from staticdepth import walk
from relseg import cycof
C = Counter(); EX = []; MUT = int(os.environ.get("MUT", "0"))   # MUT=1 tightens BND by one step: must bite

def segdata(g, R, a, b):
    """E_b, T, jW, jH, fW, fH, L for the segment [a, b]."""
    n = g.n; B = R[b]; Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]; X, st = set(), list(Q)
    while st:
        x = st.pop()
        if x in X: continue
        X.add(x); st.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
    CW = frozenset().union(*[cycof(B["wn"], v) for v in X]) if X else frozenset()
    CH = frozenset().union(*[cycof(B["nxt"], v) for v in X]) if X else frozenset()
    T = {v for c in CW for v in c} | {v for c in CH for v in c}
    pw = {v: walk(B["wn"], v) for v in range(n)}; ph = {v: walk(B["nxt"], v) for v in range(n)}
    def first(v, key, p):
        s = b
        while s > a and walk(R[s - 1][key], v) == p[v]: s -= 1
        return s
    Ev = [v for v in X if v not in T]
    fW = {v: first(v, "wn", pw) for v in Ev}; fH = {v: first(v, "nxt", ph) for v in Ev}
    def jn(v, p):
        for x in (list(p[v][0]) + list(p[v][1]))[1:]:
            if g.owner[x] == 0 and x not in T: return x
        return None
    JW = {v: jn(v, pw) for v in Ev}; JH = {v: jn(v, ph) for v in Ev}
    L = {}
    for t in range(a, b):
        for v in range(n):
            if g.owner[v] == 0 and R[t]["s"][v] != R[t + 1]["s"][v]: L[v] = t
    return Ev, T, JW, JH, fW, fH, L

def _run(g, R, name):
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        Ev, T, JW, JH, fW, fH, L = segdata(g, R, a, b)
        C["segs"] += 1; C["trans"] += b - a
        if any(v not in Ev for v in L): C["SWOUT_V"] += 1; EX.append(("SWOUT", name, a, b, sorted(v for v in L if v not in Ev)))
        for v in L:
            if v not in Ev: continue
            fw = fW[JW[v]] if JW[v] is not None else a; fh = fH[JH[v]] if JH[v] is not None else a
            if L[v] > max(fw - 1 - MUT, fh - MUT): C["BND_V"] += 1; EX.append(("BND", name, a, b, v, L[v], fw, fh))
        F = Counter(L.values()); mins = 10 ** 9
        fWj = lambda v: fW[JW[v]] if JW[v] is not None else a
        fHj = lambda v: fH[JH[v]] if JH[v] is not None else a
        for t in range(a, b):
            UW = {v for v in Ev if fW[v] > t}; UH = {v for v in Ev if fH[v] > t}
            for h in UH:
                if JH[h] in UH or JW[h] not in UW: continue          # h: an H-sink at t that is not a W-sink
                C["hsink_nonw"] += 1; s_h = fWj(h) - 1
                if R[t]["s"][h] != R[t + 1]["s"][h] != R[b]["s"][h]:
                    C["hsink_inter"] += 1
                    if L.get(h, -1) < s_h: C["INTEREARLY_V"] += 1; EX.append(("INTEREARLY", name, a, b, t, h, L.get(h), s_h))
                if L.get(h, -1) < s_h: C["EARLY_V"] += 1; EX.append(("EARLY", name, a, b, t, h, L.get(h), s_h))
                elif L.get(h) == s_h and not any(x != h and L[x] == s_h for x in L): C["JOINTX_V"] += 1; EX.append(("JOINTX", name, a, b, t, h))
        for t in range(b - 1, a - 1, -1):
            sl = sum(1 for v in L if L[v] >= t) - (b - t); mins = min(mins, sl)
            if F[t] == 0:
                C["deadlock"] += 1; sl1 = sum(1 for v in L if L[v] >= t + 1) - (b - t - 1); C["DLS_%d" % min(sl1, 9)] += 1
                EX.append(("DEADLOCK", name, a, b, t, "slack(t+1)", sl1))
        if mins < 0: C["SUFFIX_V"] += 1; EX.append(("SUFFIX", name, a, b, mins))
        C["minslack_%d" % min(mins, 3)] += 1

def run(g, name, start=None):
    E, R = rows(g, start); _run(g, R, name)

def main():
    a = sys.argv[1:]
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        for line in open(a[1]):
            p = line.split() if line.strip() and not line.startswith("#") else None
            if p:
                f = p[0] if os.path.isabs(p[0]) else (os.path.join(ROOT, p[0]) if os.path.exists(os.path.join(ROOT, p[0])) else os.path.join(ROOT, "experiments", p[0]))
                s = None
                if len(p) > 1 and os.environ.get("START") == "1":
                    s = os.path.join(ROOT, p[1]) if os.path.exists(os.path.join(ROOT, p[1])) else os.path.join(ROOT, "experiments", p[1])
                run(load(f), p[0], readstart(s) if s else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for z in [e for e in EX if e[0] != "DEADLOCK"][:10] + [e for e in EX if e[0] == "DEADLOCK"][:10]: print("EXAMPLE", z)
    for k in ("SWOUT", "BND", "SUFFIX", "EARLY", "JOINTX", "INTEREARLY"): print(k, "PASS" if k + "_V" not in C else "FAIL")

if __name__ == "__main__":
    main()

def cscore(g, R):
    """counters of one run (for chg/cclimb.py)."""
    global C, EX
    save = (C, EX); C, EX = Counter(), []
    try: _run(g, R, "x"); return dict(C)
    finally: C, EX = save
