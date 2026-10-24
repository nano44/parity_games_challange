#!/usr/bin/env python3
"""theta = Xi(o) on one-Odd-choice games: per joint lambda-phase, number of theta-changes, how many of them lower the gap
level g(o) w.r.t. the phase target T, and the exits used by Odd's best reply sbar(o) with their Odd-slack levels."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def run(path, start=None):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, _ = OT.run_states(g, st)
    L = OT.Lex(E); n = g.n
    odd = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    out = []
    for ph in OT.phases(E, Ed, states):
        T = states[ph[-1]][2]
        for o in odd:
            th = [states[k][2][o] for k in ph]; ex = [states[k][3][o] for k in ph]
            ch = sum(1 for i in range(len(ph) - 1) if th[i + 1] != th[i])
            gd = sum(1 for i in range(len(ph) - 1) if th[i + 1] != th[i] and L.lev(T[o], th[i + 1]) < L.lev(T[o], th[i]))
            exch = sum(1 for i in range(len(ph) - 1) if ex[i + 1] != ex[i])
            out.append((ph[0], len(ph) - 1, o, ch, gd, exch))
    return n, odd, out
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, odd, out = run(p, s or None)
        best = max(out, key=lambda r: r[3]) if out else None
        print(f"{os.path.basename(p):22s} n={n:3d} odd-choice={odd} max theta-changes in a phase: (phase start, trans, o, theta-changes, of which g(o)-drops, sbar(o)-changes)={best}", flush=True)
