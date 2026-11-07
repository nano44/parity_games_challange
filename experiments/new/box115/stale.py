#!/usr/bin/env python3
"""L-NEW box 115: STALE switches of classical switch-all SI. At each SI step k, compute OPT_k := the pointwise-optimal valuation of the
one-player arena H_k = {sigma_k(v)} u Isigma_k(v) with Odd fixed to sigma-bar_k (ARSB, = S4a with sigma-bar for tau). A switch-all move
y -> z is STALE if it does not attain OPT_k at y, i.e. the arena-optimal strategy gives y a strictly better value than following z with
the rest of the arena optimum (checked as OPT_k(y) != value at y of the strategy OPT-strategy with y redirected to z). Prints the number of
steps, switch-all moves, stale moves, stale moves at vertex HEAD (label s), and steps with a stale move at s. Usage: stale.py G.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, Engine, dual
import pg
g = load(sys.argv[1]); n = g.n; own = g.owner
lab = [l.split('"')[1] if '"' in l else "" for l in open(sys.argv[1]) if l.strip() and l.strip()[0].isdigit()]
HEAD = lab.index("s"); E = Engine(g)
def opt(sig, sb, Is):
    o = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in Is: o[v].add(w)
    succ = [sorted(o[v]) if own[v] == 0 else [sb[v]] for v in range(n)]
    G1 = pg.Game(list(g.prio), list(own), succ); Er = Engine(dual(G1))
    _, best = Er.evaluate(tuple(sb[v] if own[v] == 1 else -1 for v in range(n)))
    best = tuple(best[v] if own[v] == 0 else sb[v] for v in range(n))
    return G1, best
HIST, FIRST, CC = {}, {}, [0, 0]
sig = tuple(E.initial("best")); steps = moves = stale = staleh = steph = 0
while True:
    vs, sb = E.evaluate(sig); Is = E.improving(sig, vs)
    if not Is: break
    new = E.rule_switch_all(sig, vs, Is, None); G1, best = opt(sig, sb, Is)
    E1 = Engine(G1); vbest = E1.evaluate(best)[0]; hs = False
    for y in range(n):
        if own[y] != 0 or new[y] == sig[y]: continue
        moves += 1; alt = list(best); alt[y] = new[y]; va = E1.evaluate(tuple(alt))[0]
        if E1.key(va[y]) < E1.key(vbest[y]):
            CC[0] += 1; CC[1] += bool(E.cycle_creating(sig, y, best[y])); HIST[lab[y]] = HIST.get(lab[y], 0) + 1; FIRST.setdefault(steps, []).append(lab[y] + "->" + lab[new[y]] + "(opt " + lab[best[y]] + ")")
            stale += 1
            if y == HEAD: staleh += 1; hs = True
    steps += 1; steph += hs; sig = new
print("HIST", sorted(HIST.items(), key=lambda a: -a[1])); [print("STEP", k, v) for k, v in sorted(FIRST.items())[:12]]
print(f"STALE {os.path.basename(sys.argv[1])} n {n} stale_opt_cycle_creating {CC[1]}/{CC[0]} steps {steps} moves {moves} stale {stale} stale_at_s {staleh} steps_with_stale_s {steph}")
