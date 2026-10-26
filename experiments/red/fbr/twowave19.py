#!/usr/bin/env python3
"""Box 45c (L-RED successor 19; Lead 05:44Z GO): the two-wave construction for f >= n in one phase, and where it breaks.
One honest class, cycle node c (Even, self-loop, lowest even priority). Chain z_1..z_L (Even, odd priorities: negative weights), exit E
(Even, top odd priority N: routes through E carry a dominant negative weight) -> c. Anchors: A (Even, even priority) -> c on the left
(z_1 -> A); right end z_L -> q, q Odd choice with x1 := H (Even, even priority above B, forced) -> z_L (the trigger reads z_L) and
x2 := B (Even, even priority above A) -> c. Edges: z_i -> {E, z_{i-1}, z_{i+1}} (z_1 -> {E, A, z_2}; z_L -> {E, z_{L-1}, q}).
Intended run: wave 1 left -> right (z_i -> z_{i-1} once z_{i-1} has switched), then q's σ̄ flips x1 -> x2 when z_L's value rises
(H + A-route > B-route), then wave 2 right -> left (B > A). Additivity obstruction (READING, R76 addendum): "z_L -> q not improving
before wave 1" needs wt(q) + wt(H) + wt(z_L) < 0, while "trigger" plus "wave 2" need wt(H) + wt(q) + wt(z_L) > 0.
Rank order: N > H > B > A > chain > c. Usage: twowave19.py L [variant]  (variant 'flip' gives H an odd priority instead)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbr19, pg
def build(L, variant="base"):
    prio, owner, succ = [], [], []
    def add(p, o): prio.append(p); owner.append(o); succ.append([]); return len(prio) - 1
    c = add(2, 0)
    z = [add(3 + 2 * i, 0) for i in range(L)]                 # odd priorities 3, 5, ..., above c
    base = 3 + 2 * L + 1
    A = add(base + 2, 0); B = add(base + 4, 0)                # base is even: A, B even
    H = add(base + 6 if variant == "base" else base + 5, 0)   # even (base) or odd (flip)
    N = add(base + 7, 0)                                      # E: top odd
    q = add(1, 1)
    succ[c] = [c]; succ[A] = [c]; succ[B] = [c]; succ[N] = [c]; succ[H] = [z[-1]]; succ[q] = [H, B]
    for i in range(L):
        s = [N]
        s.append(A if i == 0 else z[i - 1])
        s.append(q if i == L - 1 else z[i + 1])
        succ[z[i]] = sorted(set(s))
    start = [s[0] for s in succ]
    for i in range(L): start[z[i]] = N
    start[q] = H
    return pg.Game(prio, owner, succ), start
if __name__ == "__main__":
    L = int(sys.argv[1]); variant = sys.argv[2] if len(sys.argv) > 2 else "base"
    g, st = build(L, variant)
    r = fbr19.analyse(g, st, "n5", None, True)
    print(json.dumps({k: r[k] for k in ("n", "Q", "ITER", "phases", "fmax", "Nep", "rhomax", "levels", "late", "Nlate", "fmn", "fails")}))
