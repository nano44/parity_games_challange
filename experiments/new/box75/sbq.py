#!/usr/bin/env python3
"""L-NEW box 75: R56's rho per PHASE (maximal run with (lambda_Xi, tau) constant; pairs (transition of the phase, q in Q) with Xi(q)
changing) and the Odd DECISION sequence sbar|Q inside a phase. Per (phase, q): SBQ = sbar(q)-changes, REVISIT = changes to a successor
held earlier in the phase (a return), DISTINCT = distinct choices. Also per phase: SBQ total and returns of the whole vector sbar|Q.
Usage: sbq.py GAME.pg [START] [--lzc]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
if "--lzc" in sys.argv:
    sys.path.insert(0, os.path.join(HERE, "..", "box72")); from n5lz import step
from collections import Counter, defaultdict
args = [a for a in sys.argv[1:] if not a.startswith("--")]
g = load(args[0]); n = g.n; start = readstart(args[1]) if len(args) > 1 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start)
S = [tuple(s)]; TAU = [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
T = len(S) - 1
EV = [E.evaluate(x) for x in S]; XI = [e[0] for e in EV]; SB = [e[1] for e in EV]; LX = [tuple(v[0] for v in x) for x in XI]
Q = [x for x in range(n) if g.owner[x] == 1 and len(set(g.succ[x])) >= 2]
ph = [0] * (T + 1)
for k in range(1, T + 1): ph[k] = ph[k - 1] + (LX[k] != LX[k - 1] or TAU[k] != TAU[k - 1])
rho = Counter(); sbq = Counter(); rev = Counter(); held = defaultdict(set); vecs = defaultdict(set); vrev = Counter(); perq = Counter(); sbnox = Counter()
for k in range(T + 1):
    p = ph[k]
    vec = tuple(SB[k][q] for q in Q)
    if k > 0 and ph[k - 1] == p:
        if vec != SB_prev and vec in vecs[p]: vrev[p] += 1
    vecs[p].add(vec); SB_prev = vec
    for q in Q:
        if k > 0 and ph[k - 1] == p:
            if XI[k][q] != XI[k - 1][q]: rho[p] += 1
            if SB[k][q] != SB[k - 1][q]:
                sbq[p] += 1; perq[(p, q)] += 1
                if SB[k][q] in held[(p, q)]: rev[p] += 1
                if XI[k][q] == XI[k - 1][q]: sbnox[p] += 1
        held[(p, q)].add(SB[k][q])
mx = lambda c: max(c.values()) if c else 0
mE = sum(len(set(g.succ[q])) - 1 for q in Q)
print(f"SBQ {os.path.basename(args[0])} n {n} |Q| {len(Q)} sum(deg-1) {mE} iters {T} phases {ph[-1] + 1} max-rho-phase {mx(rho)} "
      f"max-sbq-phase {mx(sbq)} max-sbq-per-q-phase {mx(perq)} revisits {sum(rev.values())} vec-returns {sum(vrev.values())} sbar-change-xi-same {sum(sbnox.values())}")
