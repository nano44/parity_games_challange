#!/usr/bin/env python3
"""Box 4: independent check of the flat-improvement instance against VJ00's OWN definitions (BRICS RS-00-48 §4.1-4.4), not
using si.py. Game given in the player-⊕ view (distinct priorities; the vertex order ≤ is the priority order). Ωσ(v) = min_⊴ over
plays consistent with σ, computed by enumerating the opponent's positional strategies (the min is attained positionally, VJ00 (11)).
Usage: vj_bruteforce.py  (runs the box-4 instance: the dual of prio [2,6,0,1], owner [0,1,0,0], succ [[0,2],[1,3],[0],[0,1,2]])"""
import itertools
def play(v, nxt):
    seq, pos = [], {}
    while v not in pos: pos[v] = len(seq); seq.append(v); v = nxt[v]
    return seq[:pos[v]], seq[pos[v]:]
def value(v, nxt, pr):
    pre, cyc = play(v, nxt); l = max(cyc, key=lambda x: pr[x])
    full = pre + cyc[:cyc.index(l)]          # Prefix(P): vertices before the first visit to λ(P)
    return (l, frozenset(x for x in full if pr[x] > pr[l]), len(full))
def reward(x, pr): return pr[x] if pr[x] % 2 == 0 else -pr[x]     # R+ = even priority = ⊕'s
def less(a, b, pr):
    """a ◁ b in VJ00's order E on play values (§4.2)."""
    if a[0] != b[0]: return reward(a[0], pr) < reward(b[0], pr)
    l, B, C = a[0], a[1], b[1]
    if B != C:
        m = max(B ^ C, key=lambda x: pr[x])
        return (m in B and pr[m] % 2 == 1) or (m in C and pr[m] % 2 == 0)
    return a[2] < b[2] if pr[l] % 2 == 1 else a[2] > b[2]           # ℓ ∈ R−: k ≤ k' ; ℓ ∈ R+: k' ≤ k
def omega(sig, pr, own, succ):
    opp = [v for v in range(len(pr)) if own[v] == 1]; best = {}
    for ch in itertools.product(*[succ[v] for v in opp]):
        nxt = dict(sig); nxt.update(zip(opp, ch))
        for v in range(len(pr)):
            val = value(v, nxt, pr)
            if v not in best or less(val, best[v], pr): best[v] = val
    return best
# dual of the instance: priorities + 1, owners swapped (⊕ = original Odd)
pr = [3, 7, 1, 2]; own = [1, 0, 1, 1]; succ = [[0, 2], [1, 3], [0], [0, 1, 2]]
for tau1 in (1, 3):
    om = omega({1: tau1}, pr, own, succ)
    print(f"⊕ strategy 1->{tau1}: Ω =", {v: (om[v][0], sorted(om[v][1]), om[v][2]) for v in range(4)})
om = omega({1: 1}, pr, own, succ)
print("edge (1,3) is an improvement for 1->1 (VJ00 (2): Ω(σ(1)) ◁ Ω(3)):", less(om[1], om[3], pr))
print("Ω unchanged by the switch:", omega({1: 1}, pr, own, succ) == omega({1: 3}, pr, own, succ))
# both of ⊕'s strategies (vertex 1 is ⊕'s only vertex) have the same Ω, so both are maximum elements of (Strategies⊕, ⊑)
print("1->1 is a maximum (its Ω equals that of every ⊕ strategy):", omega({1: 1}, pr, own, succ) == omega({1: 3}, pr, own, succ))
