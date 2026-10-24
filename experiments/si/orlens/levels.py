#!/usr/bin/env python3
"""Level profile of theta-changes (theta = Xi(o)) in the longest joint lambda-phase of an N5 run on a one-Odd-choice game.
level of a change = top rank of P(theta_k) xor P(theta_{k+1}) ('L' if only the length changes).  Prints the sequence of
(level, class) and, per level r, the count of changes at level r and the number of changes at levels > r.  For an arbitrary
monotone sequence, count(=r) <= count(>r) + 1 (counter bound); 'slack' = count(>r) + 1 - count(=r)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ortrace as OT
from collections import Counter
def run(path, start=None):
    g, st = OT.load(path, start)
    return run_g(g, st)
def run_g(g, st=None, cap=10 ** 5):
    E, Ed, states, fbf, _ = OT.run_states(g, st, cap=cap)
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
    def inR(sig, tau, v):
        seen = set(); x = v
        while x not in seen:
            if x == o: return True
            seen.add(x); x = sig[x] if g.owner[x] == 0 else tau[x]
        return False
    ph = max(OT.phases(E, Ed, states), key=len)
    seq = []
    for t in range(len(ph) - 1):
        s0, s1 = states[ph[t]], states[ph[t + 1]]
        a, b = s0[2][o], s1[2][o]
        if a == b: continue
        d = a[1] ^ b[1]; lv = d.bit_length() - 1 if d else -1
        e = s0[3][o]
        cls = "INR" if inR(s1[0], s1[1], e) else ("SELF" if s1[3][o] == e else "OVER")
        seq.append((lv, cls))
    return n, seq
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        p, _, s = spec.partition(":")
        n, seq = run(p, s or None)
        c = Counter(l for l, _ in seq)
        print(f"{os.path.basename(p)} n={n} theta-changes={len(seq)}")
        print("   seq:", " ".join(f"{l}{c_[0]}" for l, c_ in seq))
        print("   per level (level: count, count above):", ", ".join(f"{r}:{c[r]}/{sum(v for q, v in c.items() if q > r)}" for r in sorted(c, reverse=True)))
