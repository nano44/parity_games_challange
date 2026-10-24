#!/usr/bin/env python3
"""Lemma ONE-INR check (docs/si/N5-OR-lens-box2.md).  In each (w, u*)-run (urun.py's definition) of an N5 run on a one-Odd-choice
game: for every INR event (e = sbar_k(o) enters R at k -> k+1), D := ((p u {o}) above u*, above c) minus P(Xi_k(e)), where p = e's
sigma_{k+1}-path to o (o excluded).  Reports: INR events, those with D nonempty ('visible'), and violations of the lemma's
conclusion (a visible-INR exit e that is sbar(o) again later in the same run).  Also: laps inside runs (sbar(o) returns to an
exit it left earlier in the same run), and rank(o) vs rank(u*)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
from thclass import ustar, hstate
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    def path_to_o(sig, tau, v):
        seen = []; x = v
        while x not in seen:
            if x == o: return seen
            seen.append(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return None
    res = dict(INR=0, visible=0, viol=0, inrun_laps=0, o_above_u=0, runs=0, ex=[])
    for ph in OT.phases(E, Ed, states):
        key = []
        for k in ph:
            s = states[k]; w = playval(E, s[0], s[1], o); th = s[2][o]
            key.append((s[1], w, ustar(E, th, w)) if (th != w and hstate(g, E, s, o)) else None)
        t = 0
        while t < len(ph):
            if key[t] is None: t += 1; continue
            u = t
            while u + 1 < len(ph) and key[u + 1] == key[t]: u += 1
            us = key[t][2]; res["runs"] += 1
            if us is not None and E.rank[o] > us: res["o_above_u"] += 1
            left = set(); prev = states[ph[t]][3][o]
            for j in range(t + 1, u + 1):
                cur = states[ph[j]][3][o]
                if cur != prev:
                    left.add(prev)
                    if cur in left: res["inrun_laps"] += 1
                prev = cur
            for j in range(t, u):
                s0, s1 = states[ph[j]], states[ph[j + 1]]
                e = s0[3][o]
                p = path_to_o(s1[0], s1[1], e)
                if p is None or path_to_o(s0[0], s0[1], e) is not None: continue
                res["INR"] += 1
                c = s0[2][o][0]; thr = us if us is not None else -1
                Pa = s0[2][e][1]
                D = [x for x in p + [o] if E.rank[x] > E.rank[c] and E.rank[x] > thr and not (Pa >> E.rank[x]) & 1]
                if D:
                    res["visible"] += 1
                    if any(states[ph[jj]][3][o] == e for jj in range(j + 1, u + 1)):
                        res["viol"] += 1
                        if len(res["ex"]) < 3: res["ex"].append((ph[j], e))
            t = u + 1
    return n, o, res
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, o, r = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} o={o} {r}", flush=True)
