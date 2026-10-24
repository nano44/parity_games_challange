#!/usr/bin/env python3
"""Ye/HMZ-style action elimination measured directly inside each joint lambda-phase of an N5 run.
A transition k -> k+1 is ELIMINATING if some Even edge (x, sigma_k(x)) with sigma_{k+1}(x) != sigma_k(x) never occurs in
sigma_l for l > k inside the phase (also counted for Odd's best reply sbar at Odd vertices: 'oelim').
Prints per longest phase: transitions, eliminating transitions, longest run of non-eliminating transitions, edges used."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT

def elim(path, start=None, mode='n5'):
    g, st = OT.load(path, start)
    return elim_g(g, st, mode)

def elim_g(g, st=None, mode='n5', cap=10 ** 5):
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st, cap=cap, mode=mode)
    n = g.n; rows = []
    for ph in OT.phases(E, Ed, states):
        sig = [states[k][0] for k in ph]; sb = [states[k][3] for k in ph]
        used = set((x, s[x]) for s in sig for x in range(n) if g.owner[x] == 0)
        lastuse = {}
        for i, s in enumerate(sig):
            for x in range(n):
                if g.owner[x] == 0: lastuse[(x, s[x])] = i
        olast = {}
        for i, s in enumerate(sb):
            for x in range(n):
                if g.owner[x] == 1 and s[x] is not None and s[x] >= 0: olast[(x, s[x])] = i
        el = []; oel = []
        for i in range(len(ph) - 1):
            el.append(any(sig[i][x] != sig[i + 1][x] and lastuse[(x, sig[i][x])] == i for x in range(n) if g.owner[x] == 0))
            oel.append(any(sb[i][x] != sb[i + 1][x] and olast.get((x, sb[i][x])) == i for x in range(n) if g.owner[x] == 1))
        def longest(bs):
            best = cur = 0
            for b in bs:
                cur = 0 if b else cur + 1; best = max(best, cur)
            return best
        tau = [states[k][1] for k in ph]; tlast = {}
        for i, t in enumerate(tau):
            for x in range(n):
                if g.owner[x] == 1: tlast[(x, t[x])] = i
        tel = [any(tau[i][x] != tau[i + 1][x] and tlast[(x, tau[i][x])] == i for x in range(n) if g.owner[x] == 1)
               for i in range(len(ph) - 1)]
        st = [a or b for a, b in zip(el, tel)]
        both = [a or b for a, b in zip(el, oel)]
        rows.append(dict(start=ph[0], trans=len(ph) - 1, elim=sum(el), noelimrun=longest(el), oelim=sum(oel),
                         noelimrun_both=longest(both), noelimrun_st=longest(st), used=len(used)))
    return g.n, it, rows

if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, it, rows = elim(p, s or None, mode)
        r = max(rows, key=lambda q: q["trans"])
        print(f"{os.path.basename(p):24s} n={n:3d} it={it:4d} longest phase {r}", flush=True)
