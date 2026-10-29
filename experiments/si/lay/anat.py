#!/usr/bin/env python3
"""L-SI box 27: anatomy of a REL segment step: for each unsettled Even vertex of X_b \\ T, sigma over [t, b], its W- and honest
J_b-successors, arena readiness at t, first W-/H-/both-settled state. Usage: anat.py GAME [START] [T]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "lwp"))
import seglast
from common import rows, load, readstart
from staticdepth import walk
from relseg import cycof
from n5x import Engine

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    E, R = rows(g, st); EN = Engine(g); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    for a, b in seglast.segs(g, R):
        if b <= a: continue
        B = R[b]; X, stk = set(), list(Q)
        while stk:
            x = stk.pop()
            if x in X: continue
            X.add(x); stk.extend(y for y in sum(walk(B["wn"], x), ()) + sum(walk(B["nxt"], x), ()) if g.owner[y] == 0)
        CW = frozenset().union(*[cycof(B["wn"], v) for v in X]); CH = frozenset().union(*[cycof(B["nxt"], v) for v in X])
        TW = {v for c in CW for v in c}; TH = {v for c in CH for v in c}; T = TW | TH
        pw = {v: walk(B["wn"], v) for v in range(n)}; ph = {v: walk(B["nxt"], v) for v in range(n)}
        def first(v, key, p):
            s = b
            while s > a and walk(R[s - 1][key], v) == p[v]: s -= 1
            return s
        fW = {v: first(v, "wn", pw) for v in range(n)}; fH = {v: first(v, "nxt", ph) for v in range(n)}
        def jn(v, p):
            seq = list(p[v][0]) + list(p[v][1])
            for x in seq[1:]:
                if g.owner[x] == 0 and x not in T: return x
            return None
        print(f"segment [{a}, {b}] |X|={len(X)} |T|={len(T)}")
        for t in range(a, b):
            I = set(EN.improving(tuple(R[t]["s"]), R[t]["vs"]))
            Nt = sorted(v for v in X if v not in T and max(fW[v], fH[v]) > t)
            print(f" t={t} N_t={Nt}")
            for v in Nt:
                sig = [R[s]["s"][v] for s in range(t, b + 1)]
                rd = R[t]["s"][v] == B["s"][v] or (v, B["s"][v]) in I
                print(f"   v={v} sigma[t..b]={sig} JW={jn(v, pw)} JH={jn(v, ph)} ready={rd} fW={fW[v]} fH={fH[v]}"
                      f" sw_tgt={B['s'][v]} wplay={pw[v][0][:8]}|{pw[v][1][:4]}")
            if len(sys.argv) > 3: break
main()
