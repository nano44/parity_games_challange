#!/usr/bin/env python3
"""Recursive gap depth (docs/si/N5-OR-lens.md §4.4).  For a run interval [a, b] of states inside one joint lambda-phase:
target T = Xi_b; g_k(v) = lev(T(v), Xi_k(v)); a transition k -> k+1 is FLAT if g_{k+1} == g_k and Xi_{k+1} != Xi_k;
transitions with Xi_{k+1} == Xi_k (value-flat) are counted separately and do not recurse.
D([a, b]) = 0 if [a, b] has no value-changing transition, else 1 + max D over the maximal runs of consecutive FLAT
transitions (each run [c, d] recursed with its own target Xi_d).
By Theorem E6 an interval has <= n(n+1) non-flat transitions, so #value-changing transitions in a phase <= sum over the
recursion tree, < (n(n+1)+1)^D.  Prints per run: max D over phases, longest phase."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
sys.setrecursionlimit(10000)
def depth_run(g, states, E, Ed, L):
    n = g.n
    def D(a, b):
        T = states[b][2]
        vals = [states[k][2] for k in range(a, b + 1)]
        G = [[L.lev(T[v], vals[i][v]) for v in range(n)] for i in range(len(vals))]
        changing = [vals[i + 1] != vals[i] for i in range(len(vals) - 1)]
        if not any(changing): return 0
        best = 0; i = 0; m = len(vals) - 1
        while i < m:
            if changing[i] and G[i + 1] == G[i]:
                j = i
                while j < m and (not changing[j] or G[j + 1] == G[j]): j += 1
                best = max(best, D(a + i, a + j))
                i = j
            else: i += 1
        return 1 + best
    res = []
    for ph in OT.phases(E, Ed, states):
        res.append((len(ph) - 1, D(ph[0], ph[-1])))
    return res
def run(path, start=None, mode="n5"):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st, mode=mode)
    return g.n, it, depth_run(g, states, E, Ed, OT.Lex(E))
if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, it, res = run(p, s or None, mode)
        lp = max(res); md = max(d for _, d in res)
        print(f"{mode:9s} {os.path.basename(p):22s} n={n:3d} it={it:5d} max depth={md} (longest phase {lp[0]} has depth {lp[1]})", flush=True)
