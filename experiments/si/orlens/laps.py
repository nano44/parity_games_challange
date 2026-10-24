#!/usr/bin/env python3
"""Lead 14:45Z, target (a): sigma-bar laps and (theta, w)-changes per joint lambda-phase on one-Odd-choice games.
A LAP = sbar(o) returns to an exit e it left earlier in the same phase (left at transition i, back at transition j).
RETIRED-IN-LAP = some transition t in [i, j-1] is eliminating (a sigma- or tau-edge abandoned at t, absent from every later
state of the phase).  Also: theta-changes and w-changes per phase, and theta-changes at which sbar(o) does NOT change ('same-exit')
inside one non-eliminating window."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from stretchret import playval
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    res = dict(laps=0, laps_retired=0, max_theta=0, max_w=0, max_pair=0, max_sameexit_in_window=0, miss=[])
    for ph in OT.phases(E, Ed, states):
        L = len(ph)
        S = [states[k][0] for k in ph]; T = [states[k][1] for k in ph]; SB = [states[k][3][o] for k in ph]
        def edges(i): return {(x, S[i][x] if g.owner[x] == 0 else T[i][x]) for x in range(n)}
        later = [set() for _ in range(L + 1)]
        for i in range(L - 1, -1, -1): later[i] = later[i + 1] | edges(i)
        el = [bool((edges(t) - edges(t + 1)) - later[t + 1]) for t in range(L - 1)]
        th = [states[k][2][o] for k in ph]; w = [playval(E, states[k][0], states[k][1], o) for k in ph]
        tc = sum(th[t] != th[t + 1] for t in range(L - 1)); wc = sum(w[t] != w[t + 1] for t in range(L - 1))
        pc = sum((th[t], w[t]) != (th[t + 1], w[t + 1]) for t in range(L - 1))
        res["max_theta"] = max(res["max_theta"], tc); res["max_w"] = max(res["max_w"], wc); res["max_pair"] = max(res["max_pair"], pc)
        leftat = {}
        for t in range(L - 1):
            if SB[t] != SB[t + 1]:
                leftat[SB[t]] = t
                e = SB[t + 1]
                if e in leftat:
                    i = leftat[e]; res["laps"] += 1
                    if any(el[i:t + 1]): res["laps_retired"] += 1
                    elif len(res["miss"]) < 4: res["miss"].append((ph[i], ph[t + 1], e))
        cur = 0
        for t in range(L - 1):
            if el[t]: cur = 0
            elif th[t] != th[t + 1] and SB[t] == SB[t + 1]:
                cur += 1; res["max_sameexit_in_window"] = max(res["max_sameexit_in_window"], cur)
    return n, o, res
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, o, r = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} {r}", flush=True)
