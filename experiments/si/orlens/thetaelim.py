#!/usr/bin/env python3
"""L-LIT T28 rank 2 (iii)(b), Post-Ye Lemma 3.6 analogue, measured: inside each joint lambda-phase of an N5 run on a game with
one Odd choice vertex o, the max number of theta-changes (theta = Xi(o)) inside a window of consecutive NON-eliminating
transitions (eliminating = some sigma- or tau-edge abandoned and not used again in the phase), and theta-changes per phase."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def run(path, start=None):
    g, st = OT.load(path, start)
    return run_g(g, st)
def run_g(g, st=None, cap=10 ** 5):
    E, Ed, states, fbf, _ = OT.run_states(g, st, cap=cap)
    n = g.n; odd = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]; o = odd[0]
    best = (0, 0, 0)
    for ph in OT.phases(E, Ed, states):
        S = [states[k][0] for k in ph]; Tt = [states[k][1] for k in ph]
        last = {}
        for i in range(len(ph)):
            for x in range(n): last[(x, S[i][x] if g.owner[x] == 0 else Tt[i][x], g.owner[x])] = i
        el = []
        for i in range(len(ph) - 1):
            e = False
            for x in range(n):
                a, b = (S[i][x], S[i + 1][x]) if g.owner[x] == 0 else (Tt[i][x], Tt[i + 1][x])
                if a != b and last[(x, a, g.owner[x])] == i: e = True
            el.append(e)
        th = [states[k][2][o] for k in ph]
        thch = [th[i + 1] != th[i] for i in range(len(ph) - 1)]
        cur = 0; mx = 0
        for i in range(len(ph) - 1):
            if el[i]: cur = 0
            else:
                cur += thch[i]; mx = max(mx, cur)
        best = max(best, (mx, sum(thch), len(ph) - 1))
    return n, o, best
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, o, b = run(p, s or None)
        print(f"{os.path.basename(p):22s} n={n:3d} o={o} max theta-changes in a non-eliminating window={b[0]} (theta-changes in that phase {b[1]}, phase {b[2]})", flush=True)
