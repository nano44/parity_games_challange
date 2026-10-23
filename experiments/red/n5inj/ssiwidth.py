"""L-RED box 26 (produced on Opus 5.5): R58 Theorem W on an EXPONENTIAL symmetric run: SSI (n5.run mode 'ssi' = 2309.02223 Alg. 2,
SWITCH-ALL; loop replicated, iteration count asserted equal to n5.run) on DLM family 1 / 2 from DLM's start pair. Prints, per player,
the moves by the mover's |I| (Theorem W bounds moves at |I| <= k by (2n(n-1)+1) * sum_{j<=k} C(m, j)), and the max number of visited
strategies sharing one improving set. Usage: ssiwidth.py G.pg STARTFILE"""
import math, os, sys
from collections import Counter, defaultdict
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "red", "n5"))
import n5tr  # noqa: E402
import n5  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = n5tr.read_start(sys.argv[2])
E, Ed = Engine(g), Engine(n5.dual(g))
sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
for v, w in st[0].items(): sigma[v] = w
for v, w in st[1].items(): tau[v] = w
mv = (Counter(), Counter()); sh = (defaultdict(set), defaultdict(set)); it = 0
while True:
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    sh[0][frozenset(Is)].add(tuple(sigma)); sh[1][frozenset(It)].add(tuple(tau))
    if not Is and not It: break
    it += 1
    ns, nt = list(sigma), list(tau)
    for v, w in Is:
        if tbar[v] == w: ns[v] = w
    for v, w in It:
        if sbar[v] == w: nt[v] = w
    if ns != sigma: mv[0][len(Is)] += 1
    if nt != tau: mv[1][len(It)] += 1
    sigma, tau = ns, nt
    E.cache.clear(); Ed.cache.clear()
assert it == n5.run(g, "ssi", st)[0]
mE = sum(len(E.succ[v]) for v in range(g.n) if g.owner[v] == 0 and len(E.succ[v]) > 1)
mO = sum(len(E.succ[v]) for v in range(g.n) if g.owner[v] == 1 and len(E.succ[v]) > 1)
print(f"{os.path.basename(sys.argv[1])} n {g.n} SSI iterations {it}; choice edges Even {mE} Odd {mO}; max visited strategies per I: "
      f"Even {max(len(s) for s in sh[0].values())} Odd {max(len(s) for s in sh[1].values())}")
for k, side in ((0, "Even"), (1, "Odd")):
    print(f"  {side} moves by |I|: " + " ".join(f"{j}:{mv[k][j]}" for j in sorted(mv[k])))
