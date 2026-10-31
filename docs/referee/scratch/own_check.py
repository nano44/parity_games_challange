#!/usr/bin/env python3
"""REFEREE s20: independent check of REFEREE-2's Lemma OWN (R2-N5-FIXD §5) with my own S1 implementation (rl_engine.evaluate).
sigma, sigma' differ only on X; every x in X is its own Xi-cycle node under both => same valuation AND same Odd choices.
Control ONE: x own cycle node under sigma only (expect valuations to differ often)."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
r = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
pairs = viol = ctl = ctl_diff = 0
for it in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4000):
    n = r.randint(3, 14)
    prio = [r.randint(0, n) for _ in range(n)]; own = [r.randint(0, 1) for _ in range(n)]
    succ = [sorted(set(r.sample(range(n), r.randint(1, min(3, n))))) for _ in range(n)]
    g = RE.Game(prio, own, succ)
    s = [r.choice(g.succ[v]) if own[v] == 0 else None for v in range(n)]
    val, ch = RE.evaluate(g, s)
    cn = [v for v in range(n) if own[v] == 0 and val[v][0] == v and len(g.succ[v]) > 1]
    if not cn: continue
    X = r.sample(cn, r.randint(1, len(cn)))
    s2 = list(s)
    for x in X: s2[x] = r.choice([w for w in g.succ[x] if w != s[x]])
    val2, ch2 = RE.evaluate(g, s2)
    if all(val2[x][0] == x for x in X):
        pairs += 1
        oddch = [ch[v] for v in range(n) if own[v] == 1] == [ch2[v] for v in range(n) if own[v] == 1]
        if val != val2 or not oddch: viol += 1; print("VIOL", prio, own, succ, s, s2, X)
    else:
        ctl += 1; ctl_diff += val != val2
print("pairs", pairs, "violations", viol, "control(own under sigma only)", ctl, "differ", ctl_diff)
