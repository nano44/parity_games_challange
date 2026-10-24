#!/usr/bin/env python3
"""The contraction step of Ye / Hansen-Miltersen-Zwick in VJ valuations (docs/si/N5-OR-lens.md §3).
Bellman operator on valuation vectors: T(V)(x) = max_z x+V(z) (Even), min_z x+V(z) (Odd); a vertex that is its own cycle node
in V keeps V(x).  x+V = VJ prefix (adds x to the path set iff rank(x) > rank(cycle node), length + 1).
(D) "Howard dominates value iteration" (HMZ Lemma 5.3): Xi_{k+1} >= T(Xi_k) at every vertex x that is not a cycle node and
    whose T-maximiser keeps x's cycle node (checked only inside joint lambda-phases).
(VI) value iteration from V_0 = Xi_0: rounds until the (cycle node, path set) part of V_j equals that of the final Xi.
Usage: vi.py [--switchall] game.pg[:start] ...  """
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
def Top(g, E, L, V):
    out = list(V)
    for x in range(g.n):
        if V[x][0] == x: continue
        cands = [L.pre(x, V[z]) for z in E.succ[x]]
        out[x] = (max if g.owner[x] == 0 else min)(cands, key=E.key)
    return out
def run(path, start=None, mode="n5", vicap=5000):
    g, st = OT.load(path, start)
    E, Ed, states, fbf, (it, fb) = OT.run_states(g, st, mode=mode)
    L = OT.Lex(E); n = g.n
    viol = 0; checked = 0; first = None
    for ph in OT.phases(E, Ed, states):
        for i in range(len(ph) - 1):
            V0, V1 = states[ph[i]][2], states[ph[i + 1]][2]
            TV = Top(g, E, L, V0)
            for x in range(n):
                if V0[x][0] == x or TV[x][0] != V0[x][0]: continue
                checked += 1
                if E.key(V1[x]) < E.key(TV[x]):
                    viol += 1
                    if first is None: first = (ph[i], x)
    Vf = states[-1][2]; V = list(states[0][2]); rounds = None
    for j in range(vicap):
        if all(V[x][:2] == Vf[x][:2] for x in range(n)): rounds = j; break
        V = Top(g, E, L, V)
    return n, it, checked, viol, first, rounds
if __name__ == "__main__":
    mode = 'switchall' if '--switchall' in sys.argv else 'n5'
    for spec in [a for a in sys.argv[1:] if not a.startswith('--')]:
        p, _, s = spec.partition(":")
        n, it, checked, viol, first, rounds = run(p, s or None, mode)
        print(f"{mode:9s} {os.path.basename(p):22s} n={n:3d} iterations={it:5d} (D) checked={checked} violations={viol} first={first} | VI rounds to final (c,P)={rounds}", flush=True)
