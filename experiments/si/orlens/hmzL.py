#!/usr/bin/env python3
"""HMZ Lemma 6.4 shape, measured inside each joint lambda-phase of an N5 run (or switch-all, --switchall):
L_k = min over Even edges a in sigma_k of (last index in the phase at which a is in sigma) - k  (an edge of sigma_k that is
never used again after k + L_k).  Reported: Lmax = max_k L_k over states that are not the phase's last state, and the same
for the max-slack edges only (slack level w.r.t. the phase target T = Xi at the phase end; HMZ's argmax c^{pi*})."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def run(path, start=None, mode="n5"):
    g, st = OT.load(path, start)
    return run_g(g, st, mode)
def run_g(g, st=None, mode="n5", cap=10 ** 5):
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st, cap=cap, mode=mode)
    L = OT.Lex(E); n = g.n
    ev = [x for x in range(n) if g.owner[x] == 0]
    best = dict(Lmax=0, Lmax_maxslack=0, phase=0)
    for ph in OT.phases(E, Ed, states):
        if len(ph) < 2: continue
        T = states[ph[-1]][2]
        sig = [states[k][0] for k in ph]
        last = {}
        for i, s in enumerate(sig):
            for x in ev: last[(x, s[x])] = i
        Lm = Lms = 0
        for i in range(len(ph) - 1):
            s = sig[i]
            Lk = min(last[(x, s[x])] - i for x in ev) if ev else 0
            sl = {x: L.lev(T[x], L.pre(x, T[s[x]])) for x in ev if T[x][0] != x}
            if sl:
                S = max(sl.values()); Lks = min(last[(x, s[x])] - i for x in sl if sl[x] == S)
            else: Lks = 0
            Lm = max(Lm, Lk); Lms = max(Lms, Lks)
        if len(ph) - 1 > best["phase"]: best = dict(Lmax=Lm, Lmax_maxslack=Lms, phase=len(ph) - 1)
    return g.n, it, best
if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, it, b = run(p, s or None, mode)
        print(f"{mode:9s} {os.path.basename(p):22s} n={n:3d} it={it:5d} longest phase {b}", flush=True)
